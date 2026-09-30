#!/usr/bin/env python3
"""A document reader outside the session: `claude -p`, shut in its own directory.

    python3 clean_reader.py <slug> --task <file> [--model sonnet] [--thinking 0]
                            [--timeout 3600] [--apply]

A subagent of the session starts from 67 thousand tokens a call — the system
prompt, every tool definition, `CLAUDE.md`, the skill listing — and its thinking
stays in the context; `transcripts.py` measured both. This runs the same reader
through the CLI the way `scripts/claude_lm.py` isolates a call (decision 011):

- **cwd is an empty directory outside the repository**, so no `CLAUDE.md` is
  loaded, and `--setting-sources ""`, `--strict-mcp-config` and
  `--disable-slash-commands` keep settings, MCP servers and skills out;
- **tools: Bash, Read, Write, Edit.** Bash may run only `python3` on the
  repository's scripts, Read may read anything, and `acceptEdits` lets Write and
  Edit touch only the reader's own directory — a write into the repository is
  refused (tried 2026-09-30: refused, recorded as a permission denial);
- **thinking is a budget** (`MAX_THINKING_TOKENS`), 0 by default;
- the CLI reports what the run consumed, output and thinking tokens included,
  which a transcript does not.

The reader writes `terms.md`, `notes.md` and `05-verify.txt` into its own
directory. This script copies them to `Plan/runs/<slug>/clean-<stamp>/`, runs
`census.py check` and `quotes.py` on them, checks that both are this document's
and that the note is one, and with `--apply` — only if every check held, and
never over a census or note that exists — puts them where a census and a note
live. The run's numbers go to `clean-runs.jsonl` beside this file. Standard
library only.

    python3 clean_reader.py selftest   # each gate handed the file it must refuse

Until the review of #120 (2026-09-30) the note was checked by `quotes.py` alone:
an empty file has no wrong quotation, so it held, and `--apply` would have copied
it over an existing note.
"""

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
HERE = Path(__file__).resolve().parent
SCRATCH = Path(os.environ.get("CLEAN_READER_TMP", tempfile.gettempdir()))
SCRIPTS = ROOT / "scripts"
ALLOWED = [f"Bash(python3 {SCRIPTS}/{name}:*)" for name in
           ("read.py", "capture.py", "census.py", "quotes.py", "runlog.py", "profile.py")] + ["Read"]


def proxy(u: dict) -> float:
    return (u.get("input_tokens", 0) + 1.25 * u.get("cache_creation_input_tokens", 0)
            + 0.1 * u.get("cache_read_input_tokens", 0) + 5 * u.get("output_tokens", 0))


def run(slug: str, task: str, model: str, thinking: int, timeout: int) -> tuple[dict, Path]:
    work = Path(tempfile.mkdtemp(prefix=f"clean-{slug[:24]}-", dir=SCRATCH))
    if ROOT in work.parents:
        raise SystemExit(f"{work} is inside the repository: CLAUDE.md would be loaded")
    command = ["claude", "-p", "--output-format", "json", "--model", model,
               "--tools", "Bash,Read,Write,Edit", "--permission-mode", "acceptEdits",
               "--allowedTools", *ALLOWED, "--no-session-persistence", "--setting-sources", "",
               "--strict-mcp-config", "--disable-slash-commands", task]
    env = dict(os.environ, MAX_THINKING_TOKENS=str(thinking))
    started = time.time()
    proc = subprocess.run(command, cwd=work, env=env, capture_output=True, text=True, timeout=timeout)
    try:
        result = json.loads(proc.stdout)
    except json.JSONDecodeError:
        result = {"is_error": True, "result": proc.stdout[-2000:], "stderr": proc.stderr[-2000:]}
    result["wall_s"] = round(time.time() - started)
    return result, work


FRONT = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def whose(slug: str, text: str) -> str | None:
    """Why a census or note is not this document's, or None.

    `quotes.py` resolves a bare `^[Lnn]` against the file's own `source:`, so a
    note of another document passes it; only its frontmatter says whose it is.
    """
    front = FRONT.match(text)
    if not front:
        return "no frontmatter"
    source = re.search(r"^source: *\"?([^\"\n]*)\"?$", front.group(1), re.M)
    if not source or source.group(1).strip() != f"Sources/drive/{slug}.md":
        return f"its source is {source.group(1).strip() if source else 'not given'}, not Sources/drive/{slug}.md"
    return None


def note_problems(slug: str, path: Path) -> list[str]:
    """What keeps a file from being this document's note: the note skeleton's
    frontmatter, its heading, and at least one quotation verified on its line."""
    sys.path.insert(0, str(SCRIPTS))
    import quotes
    text = path.read_text(encoding="utf-8")
    if not text.strip():
        return ["empty"]
    problems = [p for p in [whose(slug, text)] if p]
    front = FRONT.match(text)
    if front and not re.search(r"^read: *\S", front.group(1), re.M):
        problems.append("no `read:` in the frontmatter")
    if not re.search(r"^# Note — \S", text, re.M):
        problems.append("no `# Note — <title>` heading")
    verified = sum(1 for m, refs in quotes.pairs(text)
                   if quotes.verdict(refs, slug, m.group("quote"))[0] == "verified")
    if not verified:
        problems.append("no quotation verified on its line")
    return problems


def checks(slug: str, folder: Path) -> dict:
    out = {}
    terms, notes = folder / "terms.md", folder / "notes.md"
    for name, path in (("census", terms), ("note", notes)):
        if not path.exists():
            out[name] = "absent"
            continue
        q = subprocess.run([sys.executable, str(SCRIPTS / "quotes.py"), str(path)],
                           capture_output=True, text=True)
        last = q.stdout.strip().splitlines()[-1] if q.stdout.strip() else q.stderr[-160:]
        clean = re.search(r"\b0 unresolved; 0 quotes had no citation", last) and ", 0 wrong;" in last
        out[f"{name} quotes"] = "held" if q.returncode == 0 and clean else "FAILED: " + last[:160]
    if terms.exists():
        sys.path.insert(0, str(SCRIPTS))
        import census
        problems = [p for p in [whose(slug, terms.read_text(encoding="utf-8"))] if p]
        problems += census.check(slug, terms)
        out["census format"] = "held" if not problems else "FAILED: " + "; ".join(problems[:5])
    if notes.exists():
        problems = note_problems(slug, notes)
        out["note format"] = "held" if not problems else "FAILED: " + "; ".join(problems)
    return out


def apply(slug: str, keep: Path, root: Path = ROOT) -> list[str]:
    """Put a checked census and note in place; refuse, writing nothing, over one that exists.

    A census is frozen once it is written, and the note beside it is read by every
    later step: a second run's files go to its run folder, never over the first.
    """
    targets = {keep / "terms.md": root / "Sources" / "terms" / f"{slug}.md",
               keep / "notes.md": root / "Sources" / "notes" / f"{slug}.md"}
    there = [str(dst.relative_to(root)) for dst in targets.values() if dst.exists()]
    if there:
        return [f"{t} exists — a census and its note are frozen once written; nothing was copied"
                for t in there]
    for src, dst in targets.items():
        shutil.copy2(src, dst)
    if (keep / "05-verify.txt").exists():
        (root / "Plan" / "runs" / slug).mkdir(parents=True, exist_ok=True)
        shutil.copy2(keep / "05-verify.txt", root / "Plan" / "runs" / slug / "05-verify.txt")
    return []


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        return selftest()
    ap = argparse.ArgumentParser()
    ap.add_argument("slug")
    ap.add_argument("--task", required=True, help="a file holding the reader's instructions")
    ap.add_argument("--model", default="sonnet")
    ap.add_argument("--thinking", type=int, default=0)
    ap.add_argument("--timeout", type=int, default=3600)
    ap.add_argument("--apply", action="store_true")
    a = ap.parse_args(argv)
    task = Path(a.task).read_text(encoding="utf-8")
    result, work = run(a.slug, task, a.model, a.thinking, a.timeout)
    stamp = datetime.now(timezone.utc).strftime("%Y%m%dT%H%MZ")
    keep = ROOT / "Plan" / "runs" / a.slug / f"clean-{stamp}"
    keep.mkdir(parents=True)
    for name in ("terms.md", "notes.md", "05-verify.txt"):
        if (work / name).exists():
            shutil.copy2(work / name, keep / name)
    verdicts = checks(a.slug, keep)
    usage = result.get("usage", {}) or {}
    row = {"slug": a.slug, "at": stamp, "model": a.model, "thinking_budget": a.thinking,
           "task": str(Path(a.task).resolve().relative_to(ROOT)) if ROOT in Path(a.task).resolve().parents else a.task,
           "turns": result.get("num_turns"), "wall_s": result.get("wall_s"),
           "duration_ms": result.get("duration_ms"), "cost_usd": result.get("total_cost_usd"),
           "usage": {k: usage.get(k) for k in ("input_tokens", "cache_creation_input_tokens",
                                                "cache_read_input_tokens", "output_tokens")},
           "thinking_tokens": (usage.get("output_tokens_details") or {}).get("thinking_tokens"),
           "proxy": round(proxy(usage)), "is_error": result.get("is_error"),
           "denials": [d.get("tool_name") for d in result.get("permission_denials", [])],
           "checks": verdicts, "kept": str(keep.relative_to(ROOT)),
           "result": (result.get("result") or "")[:1500]}
    with open(HERE / "clean-runs.jsonl", "a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    print(json.dumps({k: v for k, v in row.items() if k != "result"}, ensure_ascii=False, indent=1))
    held = held_all(verdicts)
    if a.apply:
        if not held:
            print("not applied: a check failed")
            return 1
        refused = apply(a.slug, keep)
        for why in refused:
            print(f"not applied: {why}")
        if refused:
            return 1
        print(f"applied: Sources/terms/{a.slug}.md, Sources/notes/{a.slug}.md")
    return 0 if held else 1


def held_all(verdicts: dict) -> bool:
    """Every check held, and the census and the note were both there to check."""
    return (all(k in verdicts for k in ("census format", "note format"))
            and all(v == "held" for v in verdicts.values()))


def selftest() -> int:
    """Each gate handed the file it exists to refuse, on a real document's files."""
    sys.path.insert(0, str(SCRIPTS))
    import census
    slug = "kohaerenz-protokoll-meta-foreshadowing-beobachter-logik"
    other = "ontologische-inversion-von-aegis-kritisches-framework"
    cases = []
    with tempfile.TemporaryDirectory() as tmp:
        keep = Path(tmp) / "keep"
        keep.mkdir()
        terms, notes = keep / "terms.md", keep / "notes.md"
        terms.write_text(re.sub(r"<!-- reader:.*?-->", "Written.", census.draft(slug), flags=re.S),
                         encoding="utf-8")
        real_note = (ROOT / "Sources" / "notes" / f"{slug}.md").read_text(encoding="utf-8")
        notes.write_text(real_note, encoding="utf-8")
        cases.append(("a drafted census and a real note hold", held_all(checks(slug, keep))))
        notes.write_text("", encoding="utf-8")
        cases.append(("an empty note is refused", not held_all(checks(slug, keep))))
        notes.write_text((ROOT / "Sources" / "notes" / f"{other}.md").read_text(encoding="utf-8"),
                         encoding="utf-8")
        cases.append(("another document's note is refused", "not Sources/drive"
                      in checks(slug, keep).get("note format", "")))
        notes.write_text(real_note.split("\n---\n", 1)[0] + "\n---\n\n# Note — x\n", encoding="utf-8")
        cases.append(("a note with no verified quotation is refused", "no quotation verified"
                      in checks(slug, keep).get("note format", "")))
        notes.unlink()
        cases.append(("a missing note is refused", not held_all(checks(slug, keep))))
        notes.write_text(real_note, encoding="utf-8")
        root = Path(tmp) / "root"
        for folder in ("Sources/terms", "Sources/notes"):
            (root / folder).mkdir(parents=True)
        frozen = root / "Sources" / "notes" / f"{slug}.md"
        frozen.write_text("the note already in place\n", encoding="utf-8")
        refused = apply(slug, keep, root)
        cases.append(("apply over an existing note copies nothing",
                      bool(refused) and frozen.read_text(encoding="utf-8") == "the note already in place\n"
                      and not (root / "Sources" / "terms" / f"{slug}.md").exists()))
        frozen.unlink()
        cases.append(("apply into an empty place copies both",
                      apply(slug, keep, root) == [] and frozen.read_text(encoding="utf-8") == real_note))
    failed = [n for n, ok in cases if not ok]
    print(f"clean_reader: {len(cases) - len(failed)} of {len(cases)} cases hold"
          + (" — FAILED: " + ", ".join(failed) if failed else ""))
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
