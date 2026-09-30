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
`census.py check` and `quotes.py` on them, and with `--apply` — only if every
check held — puts them where a census and a note live. The run's numbers go to
`clean-runs.jsonl` beside this file. Standard library only.
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
        problems = census.check(slug, terms)
        out["census format"] = "held" if not problems else "FAILED: " + "; ".join(problems[:5])
    return out


def main(argv: list[str]) -> int:
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
    held = verdicts and all(v == "held" for v in verdicts.values())
    if a.apply:
        if not held:
            print("not applied: a check failed")
            return 1
        shutil.copy2(keep / "terms.md", ROOT / "Sources" / "terms" / f"{a.slug}.md")
        shutil.copy2(keep / "notes.md", ROOT / "Sources" / "notes" / f"{a.slug}.md")
        if (keep / "05-verify.txt").exists():
            shutil.copy2(keep / "05-verify.txt", ROOT / "Plan" / "runs" / a.slug / "05-verify.txt")
        print(f"applied: Sources/terms/{a.slug}.md, Sources/notes/{a.slug}.md")
    return 0 if held else 1


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
