#!/usr/bin/env python3
"""Report where Graph/ chapter bodies and the Manuscript/ files diverge.

    python3 scripts/chapter_drift.py            # table of every chapter
    python3 scripts/chapter_drift.py --strict   # exit 1 when any chapter drifts
    python3 scripts/chapter_drift.py --json     # machine-readable report

`Manuscript/` is the source of truth for chapter prose; `Graph/` is the source
of truth for facts (codex entries, axioms, events, claims). The two overlap in
one place: a Chapter record carries a `body`, seeded from Canon/ as an outline.
For 40 of the 41 chapters the file on disk carries substantially more prose
than that outline, which is the expected state while the book is being
written.

This replaces `materialize_manuscript.py`, which rendered chapter files *from*
the graph through the retired engine's file driver. Rendering in that direction
would overwrite drafted prose with outline stubs, so the capability is not
worth restoring; knowing where the two disagree is.

A chapter is reported as `ahead` when the file holds more prose than the graph
body by more than THRESHOLD_WORDS, `behind` when the graph holds more, and
`aligned` otherwise.
"""
from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools import kpgraph  # noqa: E402  (needs ROOT on the path)

THRESHOLD_WORDS = 100
PROSE_MARKER = "\n# Kapitel "
EXIT_OK, EXIT_DRIFT, EXIT_CANNOT_RUN = 0, 1, 2


def chapter_files() -> dict[int, Path]:
    """Chapter number -> manuscript file, from the first chapters/ tree found."""
    directories = sorted(ROOT.glob("Manuscript/**/chapters"))
    if not directories:
        return {}
    found = {}
    for path in sorted(directories[0].glob("*.md")):
        prefix = path.name[:2]
        if prefix.isdigit():
            found.setdefault(int(prefix), path)
    return found


def prose_words(path: Path) -> int:
    """Words in the reader-facing prose body, which starts at the first heading."""
    try:
        text = path.read_text(encoding="utf-8")
    except OSError:
        return 0
    marker = text.find(PROSE_MARKER)
    return len(text[marker:].split()) if marker != -1 else 0


def classify(graph_words: int, disk_words: int) -> str:
    if disk_words > graph_words + THRESHOLD_WORDS:
        return "ahead"
    if graph_words > disk_words + THRESHOLD_WORDS:
        return "behind"
    return "aligned"


def report() -> dict:
    graph = kpgraph.load(ROOT)
    files = chapter_files()
    rows = []
    for chapter in graph.chapters():
        number = int(chapter.get("number", 0))
        path = files.get(number)
        graph_words = len(str(chapter.get("body", "")).split())
        disk_words = prose_words(path) if path else 0
        rows.append({"number": number, "title": chapter.get("title", ""),
                     "file": path.name if path else "", "graph_words": graph_words,
                     "disk_words": disk_words,
                     "state": classify(graph_words, disk_words) if path else "no file"})
    counts: dict[str, int] = {}
    for row in rows:
        counts[row["state"]] = counts.get(row["state"], 0) + 1
    return {"chapters": len(rows), "counts": counts, "rows": rows}


def render(data: dict) -> str:
    lines = [f"{'ch':>3}  {'graph':>7}  {'disk':>7}  {'state':<8} title", "-" * 62]
    for row in data["rows"]:
        lines.append(f"{row['number']:>3}  {row['graph_words']:>7}  {row['disk_words']:>7}  "
                     f"{row['state']:<8} {row['title'][:28]}")
    lines.append("")
    lines.append("  ".join(f"{state}={count}" for state, count in sorted(data["counts"].items())))
    lines.append("Manuscript/ is the source of truth for prose; 'ahead' is the normal state "
                 "while a chapter is being written.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--strict", action="store_true", help="exit 1 when any chapter drifts")
    parser.add_argument("--json", action="store_true", help="print the report as JSON")
    args = parser.parse_args(argv)
    if not (ROOT / "Graph").is_dir():
        print(f"no graph at {ROOT / 'Graph'}", file=sys.stderr)
        return EXIT_CANNOT_RUN
    data = report()
    print(json.dumps(data, ensure_ascii=False, indent=2) if args.json else render(data))
    drifted = data["counts"].get("ahead", 0) + data["counts"].get("behind", 0)
    return EXIT_DRIFT if args.strict and drifted else EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
