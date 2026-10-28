"""Before anything is published: does the built output carry what the server never serves?

Taken from `netzkontrast/agent-file`'s share gate (scan an exported state for secrets and personal data before it
leaves), with this repository's own rule as the pattern: `rag.py`'s `WITHHELD_LINE` — a figure's earlier name and the
trauma symbol (decisions 028, 029) — is the one definition, imported, never copied. The MCP server withholds those
lines; the website's frames are built from the same records and were never scanned. This scans them.

    python3 scripts/share_check.py [<dir> ...]     default: Plan/derived/web (what web.py publishes)
    python3 scripts/share_check.py --json
    python3 scripts/share_check.py selftest

It reports, per file, how many strings match — whole words apart from matches inside other words — and where — the match itself printed as `[withheld]`, so the report can
be read and committed. Exit 1 when anything matches. It changes nothing: whether a frame is scrubbed, and how, is the
author's question (Plan/questions-for-the-author.md, the frame scrub); it is not in CI until the author says so.
"""

from __future__ import annotations

import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from rag import WITHHELD_LINE, WITHHELD_TEXT  # noqa: E402  the one definition

DEFAULT = [ROOT / "Plan" / "derived" / "web"]
TEXT = {".html", ".js", ".json", ".txt", ".md", ".css", ".svg", ".xml"}
CONTEXT = 40


LETTER = re.compile(r"[A-Za-zÄÖÜäöüß]")


def scan_text(text: str) -> list[dict]:
    """Every match as {line, col, word, context}, the matched span replaced by the withheld marker. `word` is true when
    the match stands as a whole word; `rag.py`'s pattern has no word boundaries, so it also matches inside other
    words („Foreshadowing“) — those are counted apart, never dropped: the rule is the author's. A hyphen counts as a boundary (a compound may carry
    the name), so CSS `box-shadow` is counted as a whole word: the count errs toward reporting."""
    out = []
    for i, line in enumerate(text.split("\n"), 1):
        for m in WITHHELD_LINE.finditer(line):
            lo, hi = max(0, m.start() - CONTEXT), min(len(line), m.end() + CONTEXT)
            ctx = WITHHELD_LINE.sub(WITHHELD_TEXT, line[lo:hi])
            whole = not (m.start() and LETTER.match(line[m.start() - 1])) and not (m.end() < len(line) and LETTER.match(line[m.end()]))
            out.append({"line": i, "col": m.start() + 1, "word": whole, "context": ctx})
    return out


def scan(dirs: list[Path]) -> dict:
    files, missing = {}, []
    for d in dirs:
        if not d.exists():
            missing.append(str(d))
            continue
        for p in sorted(d.rglob("*")) if d.is_dir() else [d]:
            if p.is_file() and p.suffix in TEXT:
                hits = scan_text(p.read_text(encoding="utf-8", errors="replace"))
                if hits:
                    files[p.relative_to(ROOT).as_posix() if p.is_relative_to(ROOT) else str(p)] = hits
    return {"files": files, "matches": sum(len(h) for h in files.values()),
            "whole_words": sum(h["word"] for hs in files.values() for h in hs), "missing": missing}


def selftest() -> int:
    results = []
    probe = "Mich" "ael"
    hits = scan_text(f"<p>Kael geht.</p>\n<p>Früher hieß er {probe}, sagt die Quelle.</p>")
    results.append(("a withheld name is found with its line and column", [(h["line"], h["col"], h["word"]) for h in hits] == [(2, 19, True)]))
    results.append(("the report never prints the withheld word itself", probe not in json.dumps(hits) and WITHHELD_TEXT in hits[0]["context"]))
    results.append(("clean text has no match", scan_text("Das Licht ist schon da, als ich erwache.") == []))
    results.append(("a match inside another word is reported, and marked as not a whole word; a hyphen is a boundary",
                    [h["word"] for h in scan_text("Fore" "sha" "dowing; box-sha" "dow: 0")] == [False, True]))
    with tempfile.TemporaryDirectory() as tmp:
        d = Path(tmp)
        (d / "a.html").write_text(f"x {probe} y\n", encoding="utf-8")
        (d / "b.json").write_text('{"k": "clean"}', encoding="utf-8")
        (d / "c.png").write_bytes(probe.encode())
        r = scan([d, d / "absent"])
        results.append(("a directory is scanned for text files only, and a missing one is named, not passed",
                        list(r["files"]) == [str(d / "a.html")] and r["matches"] == 1 and r["missing"] == [str(d / "absent")]))
    for name, ok in results:
        print(f"{'held' if ok else 'FAILED':7} {name}")
    held = sum(ok for _, ok in results)
    print(f"{held} of {len(results)} held")
    return 0 if held == len(results) else 1


def main(argv: list[str]) -> int:
    if argv and argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    if argv and argv[0] == "selftest":
        return selftest()
    dirs = [Path(a) if Path(a).is_absolute() else ROOT / a for a in argv if not a.startswith("--")] or DEFAULT
    r = scan(dirs)
    if "--json" in argv:
        print(json.dumps(r, ensure_ascii=False, indent=1))
    else:
        for f, hits in r["files"].items():
            whole = [h for h in hits if h["word"]]
            print(f"{len(hits):6}  {f}  ({len(whole)} as a whole word)")
            for h in (whole or hits)[:3]:
                print(f"        L{h['line']}:{h['col']}{'' if h['word'] else ' (inside a word)'}  …{h['context']}…")
        for m in r["missing"]:
            print(f"not built: {m} — run web.py first; an unbuilt output has not passed")
        print(f"{r['matches']} match(es) in {len(r['files'])} file(s), {r['whole_words']} of them whole words")
    return 1 if r["matches"] or r["missing"] else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
