"""Structural profile of one landed source document.

Every term census starts from this output, so that each document is described by
the same probes in the same order rather than by whatever the reader happened to
notice. The probes are deliberately dumb: they count, they do not interpret.

Nothing here reads a second document. Comparing documents is a separate step, on
purpose -- knowledge carried from one document into the reading of the next is
exactly what makes a term look unimportant in the document where it conflicts.

Usage:
    python3 scripts/profile.py <slug> [<slug> ...]
    python3 scripts/profile.py --all
"""

from __future__ import annotations

import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "Sources" / "manifest.jsonl"

HEADING = re.compile(r"^#{1,6} ")
BOLD_ONLY = re.compile(r"^\*\*.+\*\*\s*$")
ESCAPE = re.compile(r"\\[\[\]*\"_]")
GLUED_REF = re.compile(r"([A-ZÄÖÜ][A-Za-zäöüß\-]{3,})\s(\d{1,2})\b")
INLINE_LABEL = re.compile(r"\*\*([A-ZÄÖÜ][^*\n]{2,40}):\*\*")
MATH = re.compile(r"[\u2205\u2192\u2261\u2208\u2286\u2227\u2228\u22c3\u03bb\u03a3\u03c3\u03bc\u03a0\u0394\u03b8\u03b1\u03d5\u2295\u22a2]")
TYPOGRAPHIC = "\u201e\u201c\u201d\u2018\u2019\u2013\u2014"
INVISIBLE = {"\u200b", "\u200c", "\u200d", "\u2060", "\ufeff"}


def split_frontmatter(lines: list[str]) -> tuple[int, list[str]]:
    """Return (last frontmatter line number, body lines).

    The frontmatter boundary is found, never assumed: a document whose header is
    a different length must not silently shift every count by a few lines.
    """
    marks = [i for i, line in enumerate(lines) if line.strip() == "---"]
    if len(marks) >= 2 and marks[0] == 0:
        return marks[1] + 1, lines[marks[1] + 1 :]
    return 0, lines


def repeated_labels(text: str, minimum: int = 3) -> list[tuple[str, int]]:
    """Inline bold labels the document repeats, e.g. `**Bewertung:**`.

    Whether a document labels its own passages is a fact about the file and is
    counted here. What those labels *mean* is read, never inferred from the
    count -- see Plan/decisions/004.
    """
    counts: dict[str, int] = {}
    for label in INLINE_LABEL.findall(text):
        counts[label] = counts.get(label, 0) + 1
    hits = [(label, n) for label, n in counts.items() if n >= minimum]
    return sorted(hits, key=lambda pair: (-pair[1], pair[0]))


def invisible_chars(text: str) -> dict[str, int]:
    found: dict[str, int] = {}
    for ch in text:
        if ch in INVISIBLE or unicodedata.category(ch) in ("Cf", "Mn", "Me"):
            found[ch] = found.get(ch, 0) + 1
    return found


def profile(path: Path) -> dict:
    lines = path.read_text(encoding="utf-8").split("\n")
    fm_end, body = split_frontmatter(lines)
    text = "\n".join(body)
    return {
        "slug": path.stem,
        "lines": len(lines),
        "frontmatter_ends": fm_end,
        "body_words": sum(len(line.split()) for line in body),
        "headings": sum(1 for line in body if HEADING.match(line)),
        "bold_only_lines": sum(1 for line in body if BOLD_ONLY.match(line)),
        "table_rows": sum(1 for line in body if line.startswith("|")),
        "code_fences": sum(1 for line in body if line.startswith("```")),
        "question_marks": text.count("?"),
        "backslash_escapes": len(ESCAPE.findall(text)),
        "typographic_marks": sum(text.count(c) for c in TYPOGRAPHIC),
        "ascii_quotes": text.count('"'),
        "invisible_chars": {f"U+{ord(c):04X}": n for c, n in invisible_chars(text).items()},
        "math_symbol_lines": sum(1 for line in body if MATH.search(line)),
        "glued_ref_numbers": len(GLUED_REF.findall(text)),
        "repeated_labels": repeated_labels(text),
        "longest_line": max((len(line) for line in body), default=0),
    }


def render(p: dict) -> str:
    inv = ", ".join(f"{k}x{v}" for k, v in p["invisible_chars"].items()) or "none"
    labels = ", ".join(f"{name} x{n}" for name, n in p["repeated_labels"]) or "none"
    return "\n".join(
        [
            f"# {p['slug']}",
            f"  lines                {p['lines']}  (frontmatter ends at {p['frontmatter_ends']})",
            f"  body words           {p['body_words']}",
            f"  headings             {p['headings']}   bold-only lines {p['bold_only_lines']}",
            f"  table rows           {p['table_rows']}   code fences {p['code_fences']}",
            f"  question marks       {p['question_marks']}",
            f"  backslash escapes    {p['backslash_escapes']}",
            f"  typographic marks    {p['typographic_marks']}   ascii quotes {p['ascii_quotes']}",
            f"  invisible characters {inv}",
            f"  math symbol lines    {p['math_symbol_lines']}",
            f"  glued ref numbers    {p['glued_ref_numbers']}",
            f"  repeated labels      {labels}",
            f"  longest line         {p['longest_line']} chars",
        ]
    )


def landed_paths() -> list[Path]:
    paths = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
        if row.get("export_path"):
            path = ROOT / row["export_path"]
            if path.exists():
                paths.append(path)
    return paths


def resolve(slug: str) -> Path:
    path = ROOT / "Sources" / "drive" / f"{slug}.md"
    if not path.exists():
        sys.exit(f"no landed document with slug {slug!r}")
    return path


def main(argv: list[str]) -> int:
    if not argv:
        sys.exit(__doc__)
    if argv[0] == "--all":
        for path in landed_paths():
            print(json.dumps(profile(path)))
        return 0
    for slug in argv:
        print(render(profile(resolve(slug))))
        print()
    return 0


if __name__ == "__main__":
    try:
        import signal

        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (ImportError, AttributeError, ValueError):
        pass
    raise SystemExit(main(sys.argv[1:]))
