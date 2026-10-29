"""The writing findings ledger: an editor's finding keeps its identity across runs, and the author's disposition follows it.

Taken from `netzkontrast/lit-critic` (`core/domain.py` `SnapshotFinding.build_correlation_key`, `SilenceRule`): a
finding is keyed by what it points at, so a later run that finds the same thing is the same finding, and a finding
the author has settled does not come back as new. Ported as a design, not as code: lit-critic keys with Python's
`hash()` (salted per process); here the key is sha256 of the file and the verbatim line the citation names — the line
`quotes.py` would check — so moving a paragraph keeps the finding, and rewriting the line makes it `stale`.

    python3 scripts/findings.py import <report.md>          every `path:Lnn` citation in an editor report becomes a finding
    python3 scripts/findings.py list [--file <path>]         each finding: open, stale (its line is gone) or the author's disposition
    python3 scripts/findings.py dispose <id> --as kept|settled|silenced --words "…"     the author's words, verbatim
    python3 scripts/findings.py selftest

The ledger is `Plan/runs/writing/ledger.jsonl`, append-only: an import adds a sighting, a disposition adds a row;
nothing is deleted or rewritten. A disposition without the author's words is refused (P0); no tool decides one.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "Plan" / "runs" / "writing" / "ledger.jsonl"
DISPOSITIONS = ("kept", "settled", "silenced")
CITE = re.compile(r"`?((?:Manuscript|Plan|Wiki)/[^\s`:]+\.md):L(\d+)")


def key(file: str, line_text: str) -> str:
    return hashlib.sha256(f"{file}\n{line_text.strip()}".encode("utf-8")).hexdigest()[:16]


def read(ledger: Path) -> list[dict]:
    if not ledger.exists():
        return []
    return [json.loads(ln) for ln in ledger.read_text(encoding="utf-8").splitlines() if ln.strip()]


def append(ledger: Path, row: dict) -> None:
    ledger.parent.mkdir(parents=True, exist_ok=True)
    with ledger.open("a", encoding="utf-8") as f:
        f.write(json.dumps(row, ensure_ascii=False) + "\n")


def import_report(report: Path, ledger: Path = LEDGER, root: Path = ROOT, today: str | None = None) -> list[dict]:
    """One sighting per cited line of the report: the finding's id, the cited file and line text, the report bullet."""
    today = today or datetime.date.today().isoformat()
    rows, seen = [], set()
    rel_report = report.relative_to(root).as_posix() if report.is_relative_to(root) else report.name
    for bullet in report.read_text(encoding="utf-8").split("\n"):
        for file, n in CITE.findall(bullet):
            path = root / file
            if not path.exists():
                continue
            lines = path.read_text(encoding="utf-8").split("\n")
            if not 1 <= int(n) <= len(lines) or not lines[int(n) - 1].strip():
                continue
            fid = key(file, lines[int(n) - 1])
            if (fid, rel_report) in seen:
                continue
            seen.add((fid, rel_report))
            row = {"kind": "sighting", "id": fid, "file": file, "line_text": lines[int(n) - 1].strip(), "cited_line": int(n),
                   "report": rel_report, "finding": bullet.strip(), "on": today}
            append(ledger, row)
            rows.append(row)
    return rows


def dispose(fid: str, as_: str, words: str, ledger: Path = LEDGER, today: str | None = None) -> dict:
    if not words.strip():
        raise SystemExit("a disposition records the author's words verbatim: --words is required (P0)")
    if as_ not in DISPOSITIONS:
        raise SystemExit(f"--as is one of {', '.join(DISPOSITIONS)}")
    if not any(r["id"] == fid for r in read(ledger) if r["kind"] == "sighting"):
        raise SystemExit(f"no finding {fid}")
    row = {"kind": "disposition", "id": fid, "as": as_, "words": words.strip(), "on": today or datetime.date.today().isoformat()}
    append(ledger, row)
    return row


def state(ledger: Path = LEDGER, root: Path = ROOT) -> list[dict]:
    """Per finding: its last sighting, how many reports saw it, the author's latest disposition, and whether its
    line still stands verbatim in the file (anywhere — a moved paragraph keeps the finding)."""
    out = {}
    for r in read(ledger):
        f = out.setdefault(r["id"], {"id": r["id"], "reports": set(), "disposition": None})
        if r["kind"] == "sighting":
            f.update(file=r["file"], line_text=r["line_text"], finding=r["finding"])
            f["reports"].add(r["report"])
        else:
            f["disposition"] = r
    for f in out.values():
        path = root / f["file"]
        present = path.exists() and f["line_text"] in (ln.strip() for ln in path.read_text(encoding="utf-8").split("\n"))
        f["status"] = f["disposition"]["as"] if f["disposition"] else ("open" if present else "stale")
        f["present"] = present
        f["reports"] = sorted(f["reports"])
    return list(out.values())


def selftest() -> int:
    results = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "Manuscript" / "kap-01").mkdir(parents=True)
        scene = root / "Manuscript" / "kap-01" / "szene-1.md"
        scene.write_text("Das Licht ist schon da.\n\nIch gehe. Ich stehe.\n\nDie Bank ist leer.\n", encoding="utf-8")
        rep = root / "Plan" / "r.md"
        rep.parent.mkdir(parents=True)
        rep.write_text("- `Manuscript/kap-01/szene-1.md:L3` „Ich gehe.“ — Ich-Lauf.\n- `Manuscript/kap-01/szene-1.md:L99` ins Leere\n", encoding="utf-8")
        led = root / "ledger.jsonl"
        rows = import_report(rep, led, root, "2026-10-28")
        results.append(("a cited line becomes one finding keyed by file and verbatim line; a citation past the file is skipped",
                        len(rows) == 1 and rows[0]["id"] == key("Manuscript/kap-01/szene-1.md", "Ich gehe. Ich stehe.")))
        rep2 = root / "Plan" / "r2.md"
        rep2.write_text("- Manuscript/kap-01/szene-1.md:L3 again\n", encoding="utf-8")
        import_report(rep2, led, root, "2026-10-29")
        st = state(led, root)
        results.append(("a second report citing the same line is the same finding, seen twice", len(st) == 1 and len(st[0]["reports"]) == 2 and st[0]["status"] == "open"))
        scene.write_text("Das Licht ist schon da.\n\nNeu davor.\n\nIch gehe. Ich stehe.\n", encoding="utf-8")
        results.append(("a moved line keeps the finding open", state(led, root)[0]["status"] == "open"))
        scene.write_text("Das Licht ist schon da.\n\nIch gehe, dann stehe ich.\n", encoding="utf-8")
        results.append(("a rewritten line makes the finding stale", state(led, root)[0]["status"] == "stale"))
        fid = st[0]["id"]
        try:
            dispose(fid, "settled", "", led)
            results.append(("a disposition without the author's words is refused", False))
        except SystemExit as e:
            results.append(("a disposition without the author's words is refused", "--words" in str(e)))
        dispose(fid, "kept", "Der Ich-Lauf bleibt, so geht er morgens.", led, "2026-10-30")
        st = state(led, root)
        results.append(("the author's disposition is the finding's status, with the words kept", st[0]["status"] == "kept"
                        and st[0]["disposition"]["words"].startswith("Der Ich-Lauf")))
        results.append(("the ledger only grows", len(read(led)) == 3))
    for name, ok in results:
        print(f"{'held' if ok else 'FAILED':7} {name}")
    held = sum(ok for _, ok in results)
    print(f"{held} of {len(results)} held")
    return 0 if held == len(results) else 1


def main(argv: list[str]) -> int:
    def opt(name):
        return argv[argv.index(name) + 1] if name in argv and argv.index(name) + 1 < len(argv) else ""
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    verb = argv[0]
    if verb == "selftest":
        return selftest()
    if verb == "import" and len(argv) > 1:
        rows = import_report(Path(argv[1]).resolve())
        print(f"{len(rows)} sighting(s) from {argv[1]}")
        return 0
    if verb == "list":
        only = opt("--file")
        for f in state():
            if only and f["file"] != only:
                continue
            print(f"{f['id']}  {f['status']:8} {f['file']}  „{f['line_text'][:70]}“  ({len(f['reports'])} report(s))")
        return 0
    if verb == "dispose" and len(argv) > 1:
        print(json.dumps(dispose(argv[1], opt("--as"), opt("--words")), ensure_ascii=False))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
