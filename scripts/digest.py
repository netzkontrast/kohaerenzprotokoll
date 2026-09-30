"""What a reader needs of a page to add a reading to it — not the whole page.

A reading used to be an edit of the page, and an edit reads the page first: for
documents 32–51 that was 0.5–1.8 MB of pages per document, 89 % of it other
documents' readings (`Plan/concept/pipeline-optimization_2026-09-29.md`). A
reader needs the lead, `## Where the sources differ` and `## Open` — the claims it
must keep true — and to know which documents the page already reads, which the
reading headings say in one line each. With `--doc`, the readings this document
already has on the page are printed whole, so a scanned page's reading is checked
rather than repeated.

Chapter navigation written by code (`## Candidate sources`, `## Raw qmd answers`)
is left out.

Usage:
    python3 scripts/digest.py <page> [--doc <slug>] [--root DIR]   # a page; DIR: a worktree
    python3 scripts/digest.py --size <page> ...          # bytes of page and digest
    python3 scripts/digest.py selftest
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
FOLDERS = ("Wiki/candidates", "Wiki/chapters", "Wiki/conflicts", "Wiki/questions", "Wiki/overview")
READING = re.compile(r"^## (?:Readings? — |\d{4}-\d{2}-\d{2} — )`([a-z0-9-]+)`")
SKIP = ("## Candidate sources", "## Raw qmd answers")


def page_path(page: str, root: Path = ROOT) -> Path:
    if page.endswith(".md") and (root / page).exists():
        return root / page
    for folder in FOLDERS:
        for candidate in (root / folder / f"{page}.md", *sorted((root / folder).glob(f"{page}-*.md"))):
            if candidate.exists():
                return candidate
    raise SystemExit(f"no page {page!r} under {', '.join(FOLDERS)}")


def sections(text: str) -> list[tuple[str, str]]:
    parts = re.split(r"(?m)^(## .*)$", text)
    return [("", parts[0])] + [(parts[i], parts[i + 1]) for i in range(1, len(parts), 2)]


def digest(text: str, doc: str | None = None) -> str:
    out = []
    for heading, body in sections(text):
        m = READING.match(heading)
        if m:
            slug = m.group(1)
            if doc and (doc.startswith(slug) or slug.startswith(doc)):
                out.append(heading + body)
            else:
                out.append(heading + "\n")
        elif heading.startswith(SKIP):
            out.append(heading + "\n(navigation written by code — not needed for a reading)\n\n")
        else:
            out.append(heading + body)
    return "".join(out)


def selftest() -> int:
    page = ("---\ntitle: X\n---\n\n# X\n\nLead sentence.\n\n"
            "## Reading — `doc-a`, 2025-01-01, A — one\n\nLong body A „q“ ^[doc-a.md:L3]\n\n"
            "## Reading — `doc-b`, 2026-01-01, B — two\n\nLong body B.\n\n"
            "## Where the sources differ\n\n- A against B.\n\n## Open\n\n- Why?\n\n"
            "## Raw qmd answers\n\n```qmd\nsource text\n```\n")
    d = digest(page)
    checks = [
        ("lead kept", "Lead sentence." in d),
        ("reading heading kept", "## Reading — `doc-a`" in d),
        ("reading body dropped", "Long body A" not in d),
        ("differences kept", "A against B." in d),
        ("open kept", "Why?" in d),
        ("navigation dropped", "source text" not in d),
        ("--doc keeps that document's reading whole", "Long body B." in digest(page, "doc-b")),
        ("--doc keeps others short", "Long body A" not in digest(page, "doc-b")),
    ]
    failed = [name for name, ok in checks if not ok]
    print(f"digest: {len(checks) - len(failed)} of {len(checks)} cases hold" +
          (f" — FAILED: {', '.join(failed)}" if failed else ""))
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        return selftest()
    if not argv:
        print(__doc__)
        return 2
    if argv[0] == "--size":
        for page in argv[1:]:
            text = page_path(page).read_text(encoding="utf-8")
            print(f"{page:30s} page {len(text.encode()):8d} B   digest {len(digest(text).encode()):7d} B")
        return 0
    doc = argv[argv.index("--doc") + 1] if "--doc" in argv else None
    root = Path(argv[argv.index("--root") + 1]).resolve() if "--root" in argv else ROOT
    print(digest(page_path(argv[0], root).read_text(encoding="utf-8"), doc), end="")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
