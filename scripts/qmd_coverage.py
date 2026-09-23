"""Which markdown in this repository qmd can find, and which it cannot.

qmd indexes directories as named collections. A file in a directory no collection
covers is simply absent from every search, and **nothing says so** — the search
just returns fewer results and looks like it worked. A new directory is the risk:
`Wiki/questions/` happened to fall inside the existing `wiki` collection, but the
next one may not.

So coverage is checked rather than remembered.

## The known exclusions, stated rather than discovered

| path | why |
|---|---|
| `Legacy/` | a shelf, read by nothing. Indexing it would put the retired pipeline into every search for the live one — the exact thing decision 001 removed |
| `.lit-critic-src/`, `.venv*/`, `.tools-node/`, `node_modules/` | vendored clones and dependencies, git-ignored |
| the four root files | `CLAUDE.md`, `NOW.md`, `PRINCIPLES.md`, `README.md`. **qmd's `--pattern` flag is ignored and every collection is `**/*.md`**, so a collection rooted at `.` pulls in Legacy and the vendored clones — 1,382 files. Tried, measured, removed. These four are loaded by an agent directly anyway; the loss is that a search cannot find them |
| `Sources/README.md` | the same shape one level down: the collections are `Sources/drive`, `Sources/notes` and `Sources/terms`, so a file at `Sources/` itself falls between them, and a collection rooted at `Sources/` would index all three twice |

Anything else uncovered is a gap and this prints it.

Usage:
    python3 scripts/qmd_coverage.py          # what is covered, what is not
    python3 scripts/qmd_coverage.py --paths  # the uncovered files themselves
"""

from __future__ import annotations

import argparse
import json
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
QMD = ROOT / ".tools-node" / "node_modules" / ".bin" / "qmd"

SKIP = ("Legacy/", ".lit-critic-src/", ".venv", ".tools-node/", "node_modules/",
        ".qmd/", ".git/", ".cache/",
        # vendored: wuyoscar/jev-skill v0.2.0, third-party skill text, not corpus
        ".claude/skills/jev")
# Stated above, with the measurement that produced the decision.
KNOWN = {"CLAUDE.md", "NOW.md", "PRINCIPLES.md", "README.md", "Sources/README.md"}


def collection_names() -> list[str]:
    """`collection list` prints names and qmd:// URLs but never a filesystem path."""
    out = subprocess.run([str(QMD), "collection", "list"],
                         capture_output=True, text=True, cwd=ROOT).stdout
    return [line.split(" (qmd://")[0].strip()
            for line in out.splitlines() if " (qmd://" in line]


def covered_roots() -> list[Path]:
    """The path of each collection, from `collection show` — the only command that says."""
    roots = []
    for name in collection_names():
        out = subprocess.run([str(QMD), "collection", "show", name],
                             capture_output=True, text=True, cwd=ROOT).stdout
        for line in out.splitlines():
            if line.strip().startswith("Path:"):
                roots.append(Path(line.split("Path:", 1)[1].strip()).resolve())
                break
    return roots


def repo_markdown() -> list[Path]:
    return [p for p in ROOT.rglob("*.md")
            if not any(part in str(p.relative_to(ROOT)) for part in SKIP)]


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--paths", action="store_true")
    args = parser.parse_args()

    roots = covered_roots()
    files = repo_markdown()
    uncovered = [p for p in files
                 if not any(str(p).startswith(str(r) + "/") for r in roots)]
    surprising = [p for p in uncovered if p.relative_to(ROOT).as_posix() not in KNOWN]

    print(f"{len(files)} markdown files outside the shelf and the vendored clones")
    print(f"{len(roots)} collections cover {len(files) - len(uncovered)} of them\n")
    for root in sorted(roots):
        try:
            print(f"  covered  {root.relative_to(ROOT)}")
        except ValueError:
            print(f"  covered  {root}")
    print(f"\n{len(uncovered)} uncovered, {len(surprising)} of them unexplained")
    if args.paths or surprising:
        for path in sorted(uncovered):
            name = path.relative_to(ROOT).as_posix()
            mark = "known" if name in KNOWN else "GAP  "
            print(f"  {mark}  {name}")
    if surprising:
        print("\nA GAP is a directory no collection covers. Add one:")
        print("  qmd collection add <dir> --name <name>")
        print("  qmd context add qmd://<name>/ \"what this holds\"")
    return 1 if surprising else 0


if __name__ == "__main__":
    raise SystemExit(main())
