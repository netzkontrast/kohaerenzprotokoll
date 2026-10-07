"""The AEGIS logs and their Lean proofs (`Manuscript/aegis-logs/`): checked, verified, and their status.

A log is a working draft of the novel (never canon by itself) with six parts — the reading version,
the formal claim, the definitions and assumptions, a relative link to its Lean file, the reach of
the proof, and its relation to chapter, character and storyform B. This script keeps two statuses
apart: the **editorial** status is the log's `redaktion:` field and changes only with the author;
the **formal** status is measured, never typed in.

    python3 scripts/aegis_logs.py               # check: structure, references, forbidden tokens, status
    python3 scripts/aegis_logs.py verify        # run Lean, ask `#print axioms` for every listed theorem,
                                                # write Plan/runs/aegis-logs/verifikation.json
    python3 scripts/aegis_logs.py verify --no-write   # the same, writing nothing (CI)
    python3 scripts/aegis_logs.py selftest      # every check, proved able to fail

`check` needs only the standard library and runs on GitHub with the other checks. `verify` needs the
Lean of `Manuscript/aegis-logs/lean/lean-toolchain` (`scripts/install.sh lean`); without it, it says so
and exits 2 — a log nobody could verify is `ungeprüft`, never `geprüft`.

A theorem counts as verified when Lean accepts the file with no error and no `sorry`, the file holds
none of `sorry`, `admit`, `axiom`, `native_decide`, `implemented_by`, `extern`, `unsafe` outside
comments, and `#print axioms` names only Lean's three standard axioms. The record keeps, per log, a
fingerprint of what the proof verifies: the Lean file, the toolchain, and the log's sections
„Formale Behauptung“ and „Definitionen und Voraussetzungen“. When any of them changes, the log reads
`geändert seit Prüfung` until `verify` runs again; the reading version and the reach may change freely.
"""

from __future__ import annotations

import hashlib
import json
import re
import shutil
import subprocess
import sys
import tempfile
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import wiki_index  # noqa: E402

LOGS = ROOT / "Manuscript" / "aegis-logs"
TOOLCHAIN = LOGS / "lean" / "lean-toolchain"
RECORD = ROOT / "Plan" / "runs" / "aegis-logs" / "verifikation.json"
TREATMENT = ROOT / "Manuscript" / "plot" / "treatment.md"
KANON = ROOT / "Manuscript" / "kanon.md"
CARD = ROOT / "Manuscript" / "figuren" / "aegis.md"

SECTIONS = ["Lesefassung", "Formale Behauptung", "Definitionen und Voraussetzungen", "Lean-Beweis",
            "Reichweite und Ausgeblendetes", "Kapitel, Figurenhandlung und Storyform B"]
FINGERPRINTED = ["Formale Behauptung", "Definitionen und Voraussetzungen"]
FIELDS = ["id", "titel", "kapitel", "art", "redaktion", "lean", "theoreme", "kanon"]
REDAKTION = ["entwurf", "vorgelegt", "freigegeben"]
FORBIDDEN = ["sorry", "admit", "axiom", "native_decide", "implemented_by", "extern", "unsafe"]
ALLOWED_AXIOMS = {"propext", "Quot.sound", "Classical.choice"}
ID = re.compile(r"AL-\d{2}")

STATUS_OK, STATUS_CHANGED, STATUS_NONE, STATUS_FAILED = (
    "geprüft", "geändert seit Prüfung", "ungeprüft", "Prüfung fehlgeschlagen")


# ---------------------------------------------------------------- reading

def sections(text: str) -> dict[str, str]:
    """`## Heading` -> its body, from the text after the front matter."""
    body = re.sub(r"\A---\n.*?\n---\n", "", text, flags=re.S)
    parts = re.split(r"^## (.+)$", body, flags=re.M)
    return {parts[j].strip(): parts[j + 1].strip("\n") for j in range(1, len(parts), 2)}


def strip_lean(src: str) -> str:
    """Lean source without comments and string literals, so a token in prose is not code."""
    out, i, depth, n = [], 0, 0, len(src)
    while i < n:
        if src.startswith("/-", i):
            depth, i = depth + 1, i + 2
        elif depth and src.startswith("-/", i):
            depth, i = depth - 1, i + 2
        elif depth:
            i += 1
        elif src.startswith("--", i):
            j = src.find("\n", i)
            i = n if j < 0 else j
        elif src[i] == '"':
            j = i + 1
            while j < n and src[j] != '"':
                j += 2 if src[j] == "\\" else 1
            i = j + 1
        else:
            out.append(src[i])
            i += 1
    return "".join(out)


def forbidden(src: str) -> list[str]:
    code = strip_lean(src)
    return [t for t in FORBIDDEN if re.search(r"(?<![\w.'])" + re.escape(t) + r"(?![\w'])", code)]


def theorems(src: str) -> list[str]:
    return re.findall(r"^\s*(?:theorem|lemma)\s+([\w']+)", strip_lean(src), re.M)


def namespace(src: str) -> str:
    m = re.search(r"^\s*namespace\s+([\w.]+)", strip_lean(src), re.M)
    return m.group(1) if m else ""


def fingerprint(text: str, lean_src: str, toolchain: str) -> dict:
    """The sha256 of each part a verification covers, and of all of them together."""
    secs = sections(text)
    parts = {"lean": lean_src, "toolchain": toolchain}
    parts.update({name: secs.get(name, "").strip() for name in FINGERPRINTED})
    each = {k: hashlib.sha256(v.encode("utf-8")).hexdigest() for k, v in parts.items()}
    whole = hashlib.sha256("\n".join(f"{k}:{each[k]}" for k in sorted(each)).encode()).hexdigest()
    return {"sha256": whole, "parts": each}


def load(path: Path, root: Path = ROOT) -> dict:
    text = path.read_text(encoding="utf-8")
    meta = wiki_index.frontmatter(text)
    lean_rel = str(meta.get("lean") or "")
    lean_path = (path.parent / lean_rel).resolve() if lean_rel else None
    lean_src = lean_path.read_text(encoding="utf-8") if lean_path and lean_path.is_file() else ""
    toolchain = TOOLCHAIN.read_text(encoding="utf-8") if TOOLCHAIN.is_file() else ""
    return {"path": path, "f": path.relative_to(root).as_posix(), "text": text, "meta": meta,
            "lean_path": lean_path, "lean_src": lean_src, "toolchain": toolchain,
            "fp": fingerprint(text, lean_src, toolchain)}


def all_logs() -> list[dict]:
    return [load(p) for p in sorted(LOGS.glob("al-*.md"))] if LOGS.is_dir() else []


def read_record() -> dict:
    try:
        return json.loads(RECORD.read_text(encoding="utf-8"))
    except (OSError, ValueError):
        return {}


def status(log: dict, record: dict) -> str:
    entry = (record.get("logs") or {}).get(str(log["meta"].get("id")))
    if not entry:
        return STATUS_NONE
    if not entry.get("ok"):
        return STATUS_FAILED
    return STATUS_OK if entry.get("sha256") == log["fp"]["sha256"] else STATUS_CHANGED


# ---------------------------------------------------------------- check

def kanon_ids() -> set[str]:
    if not KANON.is_file():
        return set()
    return {m.group(1) for m in re.finditer(r"^\| *`?([^|`]+?)`? *\| *\d{4}-\d{2}-\d{2}", KANON.read_text(encoding="utf-8"), re.M)}


def treatment_chapters() -> set[int]:
    if not TREATMENT.is_file():
        return set()
    return {int(n) for n in re.findall(r"^### Kap (\d+) ", TREATMENT.read_text(encoding="utf-8"), re.M)}


def problems_of(log: dict, chapters: set[int], kanon: set[str]) -> list[str]:
    """Everything wrong with one log that the standard library can see."""
    out, meta, text = [], log["meta"], log["text"]
    for field in FIELDS:
        if field not in meta:
            out.append(f"no `{field}:` in the front matter")
    lid = str(meta.get("id", ""))
    if lid and not ID.fullmatch(lid):
        out.append(f"id {lid!r} is not AL-NN")
    if lid and not log["path"].name.startswith(lid.lower() + "-"):
        out.append(f"the file name does not start with {lid.lower()}-")
    kap = str(meta.get("kapitel", ""))
    if kap and (not kap.isdigit() or int(kap) not in chapters):
        out.append(f"kapitel {kap} has no `### Kap {kap} ` heading in Manuscript/plot/treatment.md")
    red = meta.get("redaktion")
    if red is not None and red not in REDAKTION:
        out.append(f"redaktion {red!r} is not one of {', '.join(REDAKTION)}")
    ids = meta.get("kanon") or []
    for k in ids:
        if k not in kanon:
            out.append(f"kanon id {k} is not in Manuscript/kanon.md")
    if red == "freigegeben" and not ids:
        out.append("redaktion freigegeben, but no kanon id names the author's approval")
    secs = sections(text)
    have = [s for s in SECTIONS if s in secs]
    for s in SECTIONS:
        if s not in secs:
            out.append(f"no section „## {s}“")
    order = [h for h in secs if h in SECTIONS]
    if order != have:
        out.append("the six sections are not in their order")
    if "Lesefassung" in secs and "```" not in secs["Lesefassung"]:
        out.append("the reading version is not a fenced block")
    for target in re.findall(r"\]\(([^)#\s]+)", text):
        if not re.match(r"[a-z]+:", target) and not (log["path"].parent / target).exists():
            out.append(f"link {target} points at nothing")
    if meta.get("lean"):
        if not log["lean_path"] or not log["lean_path"].is_file():
            out.append(f"lean file {meta['lean']} does not exist")
        elif f"]({meta['lean']})" not in secs.get("Lean-Beweis", ""):
            out.append(f"„## Lean-Beweis“ does not link {meta['lean']}")
    if log["lean_src"]:
        for t in forbidden(log["lean_src"]):
            out.append(f"{meta.get('lean')} uses `{t}` outside a comment")
        defined = set(theorems(log["lean_src"]))
        listed = meta.get("theoreme") or []
        if not listed:
            out.append("no theorem is listed under `theoreme:`")
        for t in listed:
            if t not in defined:
                out.append(f"theorem {t} is listed but not defined in {meta.get('lean')}")
            elif f"`{t}`" not in secs.get("Formale Behauptung", ""):
                out.append(f"theorem {t} is listed but the formal claim never names it")
        if not namespace(log["lean_src"]):
            out.append(f"{meta.get('lean')} opens no namespace")
    if not log["toolchain"].startswith("leanprover/lean4:v"):
        out.append("Manuscript/aegis-logs/lean/lean-toolchain pins no Lean version")
    return out


def check() -> tuple[list[str], list[str]]:
    """(problems, status lines) over every log, the README's table and the AEGIS card."""
    logs, record = all_logs(), read_record()
    chapters, kanon = treatment_chapters(), kanon_ids()
    probs, lines, seen = [], [], set()
    if not logs:
        probs.append("Manuscript/aegis-logs/ holds no log")
    readme = (LOGS / "README.md").read_text(encoding="utf-8") if (LOGS / "README.md").is_file() else ""
    card = CARD.read_text(encoding="utf-8") if CARD.is_file() else ""
    if "aegis-logs/README.md" not in card:
        probs.append("Manuscript/figuren/aegis.md does not link aegis-logs/README.md")
    for log in logs:
        lid = str(log["meta"].get("id", log["f"]))
        if lid in seen:
            probs.append(f"{log['f']}: id {lid} twice")
        seen.add(lid)
        probs += [f"{log['f']}: {p}" for p in problems_of(log, chapters, kanon)]
        if f"]({log['path'].name})" not in readme:
            probs.append(f"Manuscript/aegis-logs/README.md does not list {log['path'].name}")
        if lid not in card:
            probs.append(f"Manuscript/figuren/aegis.md does not name {lid}")
        lines.append(f"{lid}  Kap {log['meta'].get('kapitel', '?'):>2}  redaktion {log['meta'].get('redaktion', '?'):<11} "
                     f"verifikation {status(log, record)}")
    stale = sorted(set((record.get("logs") or {})) - seen)
    probs += [f"Plan/runs/aegis-logs/verifikation.json names {s}, which no log holds" for s in stale]
    return probs, lines


# ---------------------------------------------------------------- verify

def lean_binary() -> Path | None:
    if not TOOLCHAIN.is_file():
        return None
    m = re.match(r"leanprover/lean4:v([\w.\-]+)", TOOLCHAIN.read_text(encoding="utf-8").strip())
    if not m:
        return None
    exe = ROOT / ".lean" / f"lean-{m.group(1)}-linux" / "bin" / "lean"
    return exe if exe.is_file() else None


def parse_run(output: str, returncode: int, ns: str, listed: list[str]) -> tuple[dict, list[str]]:
    """({theorem: [axioms]}, problems) from one Lean run with `#print axioms` appended."""
    axioms, probs = {}, []
    for m in re.finditer(r"'([\w.']+)' (?:does not depend on any axioms|depends on axioms: \[([^\]]*)\])", output):
        name = m.group(1)[len(ns) + 1:] if m.group(1).startswith(ns + ".") else m.group(1)
        axioms[name] = [a.strip() for a in (m.group(2) or "").split(",") if a.strip()]
    if returncode:
        probs.append(f"lean exited {returncode}")
    for ln in output.splitlines():
        if re.search(r":\d+:\d+: error", ln):
            probs.append(ln.strip())
        elif "declaration uses 'sorry'" in ln:
            probs.append(ln.strip())
    for t in listed:
        if t not in axioms:
            probs.append(f"#print axioms said nothing about {t}")
        else:
            bad = [a for a in axioms[t] if a not in ALLOWED_AXIOMS]
            if bad:
                probs.append(f"{t} depends on {', '.join(bad)}")
    return axioms, probs


def verify_one(log: dict, lean: Path) -> dict:
    meta, listed = log["meta"], list(log["meta"].get("theoreme") or [])
    ns = namespace(log["lean_src"])
    static = [p for p in problems_of(log, treatment_chapters(), kanon_ids())
              if "outside a comment" in p or "not defined" in p or "does not exist" in p]
    with tempfile.TemporaryDirectory() as tmp:
        probe = Path(tmp) / log["lean_path"].name
        probe.write_text(log["lean_src"].rstrip("\n") + "\n\n" +
                         "".join(f"#print axioms {ns}.{t}\n" for t in listed), encoding="utf-8")
        proc = subprocess.run([str(lean), str(probe)], capture_output=True, text=True, timeout=600, cwd=tmp)
    axioms, probs = parse_run(proc.stdout + proc.stderr, proc.returncode, ns, listed)
    probs = static + probs
    return {"ok": not probs, "sha256": log["fp"]["sha256"], "parts": log["fp"]["parts"],
            "lean": meta.get("lean"), "axioms": axioms, "problems": probs}


def verify(write: bool) -> int:
    lean = lean_binary()
    if not lean:
        print("Lean is not installed for this toolchain — scripts/install.sh lean; every log stays ungeprüft")
        return 2
    version = subprocess.run([str(lean), "--version"], capture_output=True, text=True).stdout.strip()
    record = {"toolchain": TOOLCHAIN.read_text(encoding="utf-8").strip(), "lean": version,
              "date": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
              "allowed_axioms": sorted(ALLOWED_AXIOMS), "logs": {}}
    failed = 0
    for log in all_logs():
        entry = verify_one(log, lean)
        record["logs"][str(log["meta"].get("id"))] = entry
        used = sorted({a for v in entry["axioms"].values() for a in v})
        print(f"{log['meta'].get('id')}  {'verified' if entry['ok'] else 'FAILED'}  "
              f"{len(entry['axioms'])} theorems, axioms: {', '.join(used) or 'none'}")
        for p in entry["problems"]:
            print(f"    {p}")
        failed += not entry["ok"]
    if write:
        RECORD.parent.mkdir(parents=True, exist_ok=True)
        RECORD.write_text(json.dumps(record, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"wrote {RECORD.relative_to(ROOT)}")
    print(version)
    return 1 if failed else 0


# ---------------------------------------------------------------- export, for scripts/ui.py

def export() -> dict:
    """Every log with its sections, both statuses and what the record says; nothing inferred."""
    record = read_record()
    out = []
    for log in all_logs():
        meta = log["meta"]
        entry = (record.get("logs") or {}).get(str(meta.get("id")), {})
        changed = [k for k, v in (entry.get("parts") or {}).items() if log["fp"]["parts"].get(k) != v]
        out.append({"id": meta.get("id"), "f": log["f"], "t": meta.get("titel") or meta.get("id"),
                    "kap": int(meta["kapitel"]) if str(meta.get("kapitel", "")).isdigit() else None,
                    "art": meta.get("art", ""), "redaktion": meta.get("redaktion", ""),
                    "kanon": meta.get("kanon") or [], "lean": meta.get("lean", ""),
                    "theoreme": meta.get("theoreme") or [], "status": status(log, record),
                    "changed": changed, "axioms": entry.get("axioms") or {},
                    "lean_src": log["lean_src"], "text": log["text"]})
    return {"logs": out, "lean": record.get("lean", ""), "toolchain": record.get("toolchain", ""),
            "date": record.get("date", ""), "readme": "Manuscript/aegis-logs/README.md"}


# ---------------------------------------------------------------- selftest

def selftest() -> int:
    bad = []

    def expect(cond: bool, what: str) -> None:
        if not cond:
            bad.append(what)

    expect(forbidden("theorem t : 1 = 1 := by sorry") == ["sorry"], "sorry in code is not found")
    expect(forbidden("-- no sorry here\n/- nor axiom -/\ntheorem t : True := trivial") == [], "a comment counts as code")
    expect(forbidden('def s := "admit"') == [], "a string counts as code")
    expect(forbidden("axiom magic : False") == ["axiom"], "an axiom declaration is not found")
    expect(forbidden("/- a /- nested -/ comment -/ theorem t := by native_decide") == ["native_decide"],
           "code after a nested comment is lost")
    expect(theorems("theorem a : True := trivial\n-- theorem b\nlemma c : True := trivial") == ["a", "c"],
           "theorems are not read from code alone")
    text = ("---\nid: AL-99\n---\n# X\n\n## Lesefassung\n\n```\nA\n```\n\n## Formale Behauptung\n\nC\n\n"
            "## Definitionen und Voraussetzungen\n\nD\n\n## Reichweite und Ausgeblendetes\n\nR\n")
    fp = fingerprint(text, "theorem t : True := trivial", "leanprover/lean4:v4.24.0\n")
    expect(fp == fingerprint(text.replace("\nA\n", "\nB\n").replace("\nR\n", "\nS\n"),
                             "theorem t : True := trivial", "leanprover/lean4:v4.24.0\n"),
           "the reading version or the reach changes the fingerprint")
    expect(fp != fingerprint(text.replace("\nC\n", "\nC2\n"), "theorem t : True := trivial",
                             "leanprover/lean4:v4.24.0\n"), "a changed claim keeps the fingerprint")
    expect(fp != fingerprint(text, "theorem t : True := by trivial", "leanprover/lean4:v4.24.0\n"),
           "a changed Lean file keeps the fingerprint")
    expect(fp != fingerprint(text, "theorem t : True := trivial", "leanprover/lean4:v4.25.0\n"),
           "a changed toolchain keeps the fingerprint")
    log = {"meta": {"id": "AL-99"}, "fp": fp}
    expect(status(log, {}) == STATUS_NONE, "no record is not ungeprüft")
    expect(status(log, {"logs": {"AL-99": {"ok": True, "sha256": fp["sha256"]}}}) == STATUS_OK, "a match is not geprüft")
    expect(status(log, {"logs": {"AL-99": {"ok": True, "sha256": "0"}}}) == STATUS_CHANGED, "a change is not flagged")
    expect(status(log, {"logs": {"AL-99": {"ok": False, "sha256": fp["sha256"]}}}) == STATUS_FAILED,
           "a failed run reads as geprüft")
    ok_out = "'N.a' does not depend on any axioms\n'N.b' depends on axioms: [propext, Quot.sound]\n"
    expect(parse_run(ok_out, 0, "N", ["a", "b"])[1] == [], "a clean run has problems")
    expect(parse_run(ok_out.replace("Quot.sound", "sorryAx"), 0, "N", ["a", "b"])[1], "sorryAx passes")
    expect(parse_run(ok_out.replace("Quot.sound", "N.magic"), 0, "N", ["a", "b"])[1], "an own axiom passes")
    expect(parse_run(ok_out.replace("Quot.sound", "Lean.ofReduceBool"), 0, "N", ["a", "b"])[1], "ofReduceBool passes")
    expect(parse_run(ok_out, 0, "N", ["a", "b", "c"])[1], "a theorem nobody printed passes")
    expect(parse_run("x.lean:3:0: warning: declaration uses 'sorry'\n" + ok_out, 0, "N", ["a"])[1], "a sorry warning passes")
    expect(parse_run("x.lean:3:4: error: unsolved goals\n" + ok_out, 1, "N", ["a"])[1], "an error passes")
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        (d / "lean").mkdir()
        (d / "lean" / "X.lean").write_text("namespace X\ntheorem t : True := trivial\nend X\n", encoding="utf-8")
        good = ("---\nid: AL-99\ntitel: X\nkapitel: 6\nart: x\nredaktion: entwurf\nlean: lean/X.lean\n"
                "theoreme: [t]\nkanon: []\n---\n# X\n\n" + "".join(
                    f"## {s}\n\n" + ("```\nA\n```" if s == "Lesefassung" else "`t`" if s == "Formale Behauptung"
                                      else "[X](lean/X.lean)" if s == "Lean-Beweis" else "x") + "\n\n" for s in SECTIONS))
        (d / "al-99-x.md").write_text(good, encoding="utf-8")
        global TOOLCHAIN
        saved, TOOLCHAIN = TOOLCHAIN, d / "lean" / "lean-toolchain"
        TOOLCHAIN.write_text("leanprover/lean4:v4.24.0\n", encoding="utf-8")
        try:
            def probs(text: str) -> list[str]:
                (d / "al-99-x.md").write_text(text, encoding="utf-8")
                return problems_of(load(d / "al-99-x.md", d), {6}, {"C6"})
            expect(probs(good) == [], f"a good log has problems: {probs(good)}")
            expect(probs(good.replace("kapitel: 6", "kapitel: 7")), "a chapter outside the treatment passes")
            expect(probs(good.replace("redaktion: entwurf", "redaktion: kanon")), "an unknown redaktion passes")
            expect(probs(good.replace("redaktion: entwurf", "redaktion: freigegeben")), "freigegeben without a kanon id passes")
            expect(probs(good.replace("kanon: []", "kanon: [C99]")), "an unknown kanon id passes")
            expect(probs(good.replace("theoreme: [t]", "theoreme: [t, u]")), "an undefined theorem passes")
            expect(probs(good.replace("## Reichweite und Ausgeblendetes", "## Reichweite")), "a missing section passes")
            expect(probs(good.replace("[X](lean/X.lean)", "[X](lean/Y.lean)")), "a broken link passes")
            expect(probs(good.replace("`t`", "t")), "a theorem the claim never names passes")
            (d / "lean" / "X.lean").write_text("namespace X\ntheorem t : True := by sorry\nend X\n", encoding="utf-8")
            expect(probs(good), "sorry in the Lean file passes")
        finally:
            TOOLCHAIN = saved
    for b in bad:
        print(f"FAILED: {b}")
    print(f"aegis_logs selftest: {'held' if not bad else 'FAILED'} ({len(bad)} of the cases failed)")
    return 1 if bad else 0


def main(argv: list[str]) -> int:
    cmd = argv[0] if argv else "check"
    if cmd == "selftest":
        return selftest()
    if cmd == "verify":
        return verify(write="--no-write" not in argv)
    if cmd == "check":
        probs, lines = check()
        for ln in lines:
            print(ln)
        for p in probs:
            print(f"PROBLEM  {p}")
        print(f"{len(lines)} logs, {len(probs)} problems" + ("" if lean_binary() else " — Lean not installed here; `verify` needs scripts/install.sh lean"))
        return 1 if probs else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
