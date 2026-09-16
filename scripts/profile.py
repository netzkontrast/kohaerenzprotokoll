"""Structural profile of one landed source document.

Every term census starts from this output, so that each document is described by
the same probes in the same order rather than by whatever the reader happened to
notice. The probes are deliberately dumb: they count, they do not interpret.

Nothing here reads a second document. Comparing documents is a separate step, on
purpose -- knowledge carried from one document into the reading of the next is
exactly what makes a term look unimportant in the document where it conflicts.

Usage:
    python3 scripts/profile.py <slug> [<slug> ...]
    python3 scripts/profile.py --all          # one JSON object per landed document
    python3 scripts/profile.py --summary      # medians per category
    python3 scripts/profile.py --frontmatter <slug>   # census header, from the manifest
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


def manifest_rows() -> list[dict]:
    return [json.loads(line) for line in MANIFEST.read_text(encoding="utf-8").splitlines()]


def summarise() -> str:
    """Medians per category, so the corpus can be compared against one document.

    Which category to read next is a question about where the unfamiliar shapes
    are, and guessing it from three documents of one category is how a claim ends
    up generalised from a sample of one.
    """
    import statistics
    from collections import defaultdict

    category = {r["slug"]: r["category"] for r in manifest_rows() if r.get("export_path")}
    groups: dict[str, list[dict]] = defaultdict(list)
    for path in landed_paths():
        p = profile(path)
        groups[category.get(p["slug"], "?")].append(p)

    def median(items: list[dict], key: str) -> float:
        return statistics.median([item[key] for item in items])

    head = f"{'category':22} {'n':>4} {'words':>7} {'head':>5} {'tbl':>5} {'math':>5} {'esc':>5} {'zwsp':>5} {'lbl':>5}"
    lines = [head, "-" * len(head)]
    for name, items in sorted(groups.items(), key=lambda kv: -len(kv[1])):
        lines.append(
            f"{name:22} {len(items):4} {median(items, 'body_words'):7.0f} "
            f"{median(items, 'headings'):5.0f} {median(items, 'table_rows'):5.0f} "
            f"{median(items, 'math_symbol_lines'):5.0f} {median(items, 'backslash_escapes'):5.0f} "
            f"{sum(1 for i in items if i['invisible_chars']):5} "
            f"{sum(1 for i in items if i['repeated_labels']):5}"
        )
    lines.append("")
    lines.append("medians, except zwsp and lbl, which count documents:")
    lines.append("  zwsp  documents containing zero-width spaces (flattened subscripts)")
    lines.append("  lbl   documents that label their own passages with repeated bold labels")
    return "\n".join(lines)


def census_frontmatter(slug: str) -> str:
    """The census header for one document, copied from the manifest.

    It exists because typing it by hand produced a fabricated `drive_id` once.
    A provenance identifier that is invented rather than copied breaks the one
    guarantee the whole repository rests on -- that anything derived traces back
    to a real Drive document -- and it fails silently, because a wrong id looks
    exactly like a right one.
    """
    import datetime

    for row in manifest_rows():
        if row.get("slug") != slug:
            continue
        if not row.get("export_path"):
            sys.exit(f"{slug!r} is in the manifest but has not landed")
        p = profile(ROOT / row["export_path"])
        return "\n".join(
            [
                "---",
                f"source: {row['export_path']}",
                f"drive_id: \"{row['drive_id']}\"",
                f"title: \"{row['title']}\"",
                f"category: {row['category']}",
                f"index_date: \"{row.get('index_date', '')}\"",
                f"extracted: \"{datetime.date.today().isoformat()}\"",
                "candidates: 0    # fill in by hand -- this is the one number nothing can count",
                "---",
                "",
                f"# Term census — {row['title']}",
                "",
                "> **This file describes one document and nothing else.** No count, comparison or",
                "> expectation from any other source appears here. Comparing documents is a",
                "> separate step, and mixing the two is what lets a term look unimportant in the",
                "> document where it conflicts.",
                "",
                "## Structural profile",
                "",
                f"`python3 scripts/profile.py {slug}`",
                "",
                "```",
                render(p).split("\n", 1)[1],
                "```",
            ]
        )
    sys.exit(f"no manifest row with slug {slug!r}")


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
    if argv[0] == "--frontmatter":
        if len(argv) != 2:
            sys.exit("--frontmatter takes exactly one slug")
        print(census_frontmatter(argv[1]))
        return 0
    if argv[0] == "--summary":
        print(summarise())
        return 0
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
