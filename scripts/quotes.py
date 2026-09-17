"""Verify that every quoted passage still resolves to the line it cites.

A note or a page quotes a source and cites a file line: „…" ^[L137], or
^[slug.md:L61] when the source is another document. Nothing checked those. Three
were wrong in the first note this ran against -- „ein umfassendes
Referenzdokument" against a source that says „die Schaffung eines umfassenden
Referenzdokuments", and two more of the same kind: right line, right meaning,
wrong words.

That is the worst shape a defect can take here. The citation looks precise, the
line number is correct, and the sentence in quotation marks was never in the
document. Nothing downstream can tell the difference, and a reader who trusts the
quotation marks is reading something the project wrote and attributed to a source.

## What it checks and what it cannot

Resolution is by substring against the cited line, after undoing two things the
export and the notes each do:

- **export escaping** -- `\[`, `\"` and friends, the same damage
  `rules/export_damage.py` counts; without this the check reports false failures
- **the note's own escaping** -- `\"` written inside a `„…"` quote

An ellipsis (`…` or `[…]`) splits the quote and every part must resolve, in
order, on that line. A quote spanning two lines is reported as unresolved rather
than silently searched for nearby: the line number is part of the claim.

Usage:
    python3 scripts/quotes.py            # every note, census and wiki page
    python3 scripts/quotes.py <path>     # one file
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from subject import document, documents  # noqa: E402

ESCAPE = re.compile(r"\\+([\[\]*\"_„“.\-()#+])")
EMPHASIS = re.compile(r"\*{1,3}|_{1,3}|`")
WRAP = re.compile(r"\s*\n\s*(?:>\s*)?|\s{2,}")
# The footnote numbers the export glues to the word they annotate -- the same
# damage `rules/export_damage.py` counts. A quote reproduces the sentence; the
# number was never part of it, so it is dropped from the source side too.
GLUED_REF = re.compile(r"(?<=[A-Za-zäöüßÄÖÜ)\"]) ?\d{1,2}(?=[\s,.;:)])|(?<=[a-zäöüß]\.)\d{1,2}(?= )")
# An inline attribution marker is not part of the sentence it annotates -- it is
# derived separately by `rules/attribution.py`. A quote that reproduces the
# sentence and drops the marker is quoting correctly, so it is dropped from the
# source side too rather than counted as a word the document does not have.
MARKER = re.compile(r"\s*\[(?:User Query|Adressiert)[^\]]{0,60}\]")
# A quote and the citation it belongs to, in either order: files write both
# „…" ^[L12] and ^[L12] „…". Pairing is by **line**, not by character distance.
# A window picks up the wrong reference inside a markdown table, where each row
# carries its own line number -- it reported a quote from one row against the
# reference in another and called it unresolved.
#
# The cost is stated rather than hidden: a quote with no reference on its own
# line (or on the line its last fragment ends on) is **not checked at all**. The
# run prints how many those are.
QUOTE = re.compile(r"„(?P<quote>[^„“]{8,400})[“\"]")
CITE = re.compile(r"\^\[(?P<ref>[^\]\n]{2,80})\]")
UNKNOWN_SOURCE = "which document this ^[Lnn] means cannot be determined"
REF = re.compile(r"^(?:(?P<slug>[A-Za-z0-9\-]+)\.md:)?L(?P<line>\d+)(?:\s*[-\u2013]\s*(?P<last>\d+))?")


def normalise(text: str) -> str:
    """Both sides of the comparison, reduced to what is actually being claimed.

    Four things differ between a quote as written and its source line and none of
    them is a defect: export backslash escaping, markdown emphasis added by the
    quoting file (or present in the source and dropped by it), the line wrapping
    and `> ` prefixes a quote picks up inside a blockquote, and runs of spaces.

    Normalising all four is what makes a genuine failure -- a word that was never
    in the document -- the only thing left to report.
    """
    text = ESCAPE.sub(r"\1", text)
    text = EMPHASIS.sub("", text)
    text = MARKER.sub("", WRAP.sub(" ", text))
    return GLUED_REF.sub("", text).strip()


def source_line(slug: str, number: int) -> str | None:
    doc = document(slug)
    lines = doc.body.split("\n")
    index = number - doc.offset
    return normalise(lines[index]) if 0 <= index < len(lines) else None


def parts_of(quote: str) -> list[str]:
    """A quote with an ellipsis is several fragments, each of which must resolve."""
    pieces = re.split(r"\s*(?:\[…\]|…|\[\.\.\.\])\s*", normalise(quote))
    return [p.strip(" ,;:.") for p in pieces if len(p.strip(" ,;:.")) >= 4]


def missing_part(line: str, parts: list[str]) -> str | None:
    """The first fragment not found, in order, on this one normalised line.

    `scripts/read.py` asks this of every line to answer „which line is this quote
    on"; `resolve` asks it of the cited line to answer „is it on the one claimed".
    Both directions have to agree, so there is one implementation.
    """
    cursor = 0
    for part in parts:
        found = line.find(part, cursor)
        if found < 0:
            return part
        cursor = found + len(part)
    return None


def check_file(path: Path, default_slug: str | None) -> tuple[list[dict], int]:
    text = path.read_text(encoding="utf-8")
    starts = [0]
    for line in text.split("\n"):
        starts.append(starts[-1] + len(line) + 1)

    def line_of(pos: int) -> int:
        lo, hi = 0, len(starts) - 1
        while lo < hi - 1:
            mid = (lo + hi) // 2
            if starts[mid] <= pos:
                lo = mid
            else:
                hi = mid
        return lo

    cites: dict[int, list[str]] = {}
    for m in CITE.finditer(text):
        cites.setdefault(line_of(m.start()), []).append(m.group("ref"))

    # A line may carry several quotes and one reference -- a table row often does.
    # The reference belongs to the quote nearest it, and the others on that line
    # are uncited rather than wrong. Pairing by nearest position says so.
    owner: dict[int, list[str]] = {}
    quotes = list(QUOTE.finditer(text))
    for m in CITE.finditer(text):
        row = line_of(m.start())
        # A blockquote puts its citation on the line after the quote closes:
        #     > „…text…"
        #     > ^[slug.md:L137]
        # so a reference alone on its line also claims the quote ending just above.
        body = text.split("\n")[row].lstrip("> ").strip() if row < len(text.split("\n")) else ""
        rows = {row, row - 1} if body.startswith("^[") else {row}
        same = [q for q in quotes
                if line_of(q.start()) in rows or line_of(q.end()) in rows]
        if not same:
            continue
        nearest = min(same, key=lambda q: min(abs(q.start() - m.start()), abs(q.end() - m.start())))
        owner.setdefault(nearest.start(), []).append(m.group("ref"))

    problems, unchecked = [], 0
    for match in quotes:
        near = owner.get(match.start(), [])
        if not near:
            unchecked += 1
            continue
        failures, resolvable = [], False
        for raw in near:
            outcome = resolve(raw, default_slug, match.group("quote"))
            if outcome == UNKNOWN_SOURCE:
                continue
            resolvable = True
            if outcome is None:
                failures = []
                break
            failures.append(outcome)
        if not resolvable:
            unchecked += 1
            continue
        if failures:
            problems.append({"quote": match.group("quote")[:60], "ref": near[0],
                             "why": failures[0]})
    return problems, unchecked


def resolve(raw: str, default_slug: str | None, quote: str) -> str | None:
    """None when the quote resolves against this reference, else why it did not."""
    ref = REF.match(raw)
    if not ref:
        return UNKNOWN_SOURCE
    slug = ref.group("slug") or default_slug
    if not slug:
        return UNKNOWN_SOURCE
    first = int(ref.group("line"))
    last = int(ref.group("last") or first)
    # A range cites a passage: the quote must resolve within it, on one line.
    span = [source_line(slug, n) for n in range(first, min(last, first + 40) + 1)]
    if all(line is None for line in span):
        return "line is past the end of the document"
    parts = parts_of(quote)
    missing = "quote is empty after normalising"
    for clean in [line for line in span if line is not None]:
        gap = missing_part(clean, parts)
        if gap is None:
            return None
        missing = gap
    return f"not on that line: {missing[:60]!r}"


def slug_of(path: Path) -> str | None:
    """Which document a file's bare ^[Lnn] refers to.

    A census or a note says so in `source:`. A wiki page does not -- it says
    which documents it was built from in `ingested:`, and a bare `^[Lnn]` on a
    page written during one document's reconciliation means that document. When
    a page carries several, a bare reference is ambiguous and is **not** checked
    rather than checked against a guess.
    """
    head = path.read_text(encoding="utf-8")[:900]
    match = re.search(r"^source:\s*Sources/drive/([A-Za-z0-9\-]+)\.md", head, re.M)
    if match:
        return match.group(1)
    ingested = re.search(r"^ingested:\s*\[(?P<list>[^\]]*)\]", head, re.M)
    if ingested:
        slugs = re.findall(r"[A-Za-z0-9\-]{4,}", ingested.group("list"))
        if len(slugs) == 1:
            return slugs[0]
        return None
    return path.stem if any(d.slug == path.stem for d in documents()) else None


def main(argv: list[str]) -> int:
    if argv:
        targets = [Path(argv[0]).resolve()]
    else:
        targets = sorted(
            list((ROOT / "Sources" / "notes").glob("*.md"))
            + list((ROOT / "Sources" / "terms").glob("*.md"))
            + list((ROOT / "Wiki").rglob("*.md"))
        )
    checked = failed = uncited = 0
    for path in targets:
        default = slug_of(path)
        problems, skipped = check_file(path, default)
        checked += len(QUOTE.findall(path.read_text(encoding="utf-8"))) - skipped
        uncited += skipped
        for problem in problems:
            failed += 1
            where = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
            print(f"UNRESOLVED  {where}  ^[{problem['ref']}]")
            print(f"            „{problem['quote']}…\"")
            print(f"            {problem['why']}")
    print(f"\n{checked} cited quotes checked, {failed} unresolved; "
          f"{uncited} quotes had no citation on their own line, or none naming a\ndocument that could be resolved, and were not checked."
          f"\nA bare ^[Lnn] resolves against the file's own `source:`.")
    return 1 if failed else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
