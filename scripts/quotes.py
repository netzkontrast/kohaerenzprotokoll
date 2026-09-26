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

**A number is compared on its own.** The footnote rule below drops a number of
one or two digits after a word on both sides, so for the words alone „Kap 33
Beat 3" and „Kap 38 Beat 3" were the same sentence. In a chapter outline that
is every chapter, beat and world number: 268 on one document, not one of them a
footnote. So every number the quote writes must also stand on the line, in the
same order, with the footnote rule off (`missing_number`).

Usage:
    python3 scripts/quotes.py            # every note, census and wiki page
    python3 scripts/quotes.py <path>     # one file
    python3 scripts/quotes.py --unchecked [path]  # list every unchecked quotation
"""

from __future__ import annotations

import re
import sys
from bisect import bisect_right
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
# The end of the text is a boundary like a space: without it a quote ending in
# „Kap 38" kept the number its line had dropped, and could never resolve. What
# the words no longer see, `missing_number` compares.
GLUED_REF = re.compile(r"(?<=[A-Za-zäöüßÄÖÜ)\"]) ?\d{1,2}(?=[\s,.;:)]|$)|(?<=[a-zäöüß]\.)\d{1,2}(?= |$)")
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
# A ```qmd fence holds a search's raw answer, copied by code from a source file
# with each line's number beside it: a place to look, never a quotation the page
# makes. Only this info string is skipped; a quotation in any other fence counts.
RAW_FENCE = re.compile(r"^```qmd\n.*?^```", re.S | re.M)
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
    return GLUED_REF.sub("", unmarked(text)).strip()


def unmarked(text: str) -> str:
    """The context-free part of `normalise`: escaping, emphasis, wrapping, markers.

    `entities.py` compares names with this and without the footnote rule, which
    needs the same context on both sides and a name does not carry it. Both are
    built here so neither can gain a step the other lacks. `missing_number`
    compares a quotation's numbers the same way, for the same reason.
    """
    text = ESCAPE.sub(r"\1", text)
    text = EMPHASIS.sub("", text)
    return MARKER.sub("", WRAP.sub(" ", text))


NUMBER = re.compile(r"\d+")


def missing_number(line: str, quote: str) -> str | None:
    """The first number the quote writes that the raw line does not, in order.

    The footnote rule is kept off here: a number the quote writes is a claim, and
    extra numbers on the line — footnote debris among them — are allowed, so a
    quote that correctly drops a footnote still resolves.
    """
    have = NUMBER.findall(unmarked(line))
    cursor = 0
    for number in NUMBER.findall(unmarked(quote)):
        try:
            cursor = have.index(number, cursor) + 1
        except ValueError:
            return f"the number {number}"
    return None


def on_line(line: str, quote: str, parts: list[str] | None = None) -> str | None:
    """Is the quote on this one raw line? None if so, else what is missing.

    The one comparison `resolve` asks of a cited line and `read.py --find` asks of
    every line, so the two directions cannot disagree: the words in order after
    normalising, then the numbers in order without the footnote rule.
    """
    gap = missing_part(normalise(line), parts if parts is not None else parts_of(quote))
    return gap if gap is not None else missing_number(line, quote)


def source_line(slug: str, number: int) -> str | None:
    doc = document(slug)
    lines = doc.lines()
    index = number - doc.offset
    return lines[index] if 0 <= index < len(lines) else None


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


def line_starts(text: str) -> list[int]:
    """The offset each line of `text` starts at, then one past the end."""
    starts = [0]
    for line in text.split("\n"):
        starts.append(starts[-1] + len(line) + 1)
    return starts


def line_of(starts: list[int], pos: int) -> int:
    """The 0-based line holding character `pos` of the text `starts` describes."""
    return bisect_right(starts, pos) - 1


def unraw(text: str) -> str:
    """`text` with every ```qmd fence blanked, same length and same lines."""
    return RAW_FENCE.sub(lambda m: re.sub(r"[^\n]", " ", m.group(0)), text)


def pairs(text: str) -> list[tuple[re.Match, list[str]]]:
    """Every quotation in `text`, with the references that belong to it.

    The one implementation of pairing: `check_file` verdicts on it, and
    `graph.py` serves its quotations as evidence from it, so the two can never
    disagree about which reference a quotation carries.
    """
    text = unraw(text)
    starts = line_starts(text)

    # A line may carry several quotes and one reference -- a table row often does.
    # The reference belongs to the quote nearest it, and the others on that line
    # are uncited rather than wrong. Pairing by nearest position says so.
    owner: dict[int, list[str]] = {}
    quotes = list(QUOTE.finditer(text))
    spans = [(line_of(starts, q.start()), line_of(starts, q.end())) for q in quotes]
    lines = text.split("\n")
    for m in CITE.finditer(text):
        row = line_of(starts, m.start())
        # A blockquote puts its citation on the line after the quote closes:
        #     > „…text…"
        #     > ^[slug.md:L137]
        # so a reference alone on its line also claims the quote ending just above.
        body = lines[row].lstrip("> ").strip() if row < len(lines) else ""
        rows = {row, row - 1} if body.startswith("^[") else {row}
        same = [q for q, (first, last) in zip(quotes, spans)
                if first in rows or last in rows]
        if not same:
            continue
        nearest = min(same, key=lambda q: min(abs(q.start() - m.start()), abs(q.end() - m.start())))
        owner.setdefault(nearest.start(), []).append(m.group("ref"))
    return [(match, owner.get(match.start(), [])) for match in quotes]


def verdict(refs: list[str], default_slug: str | None, quote: str) -> tuple[str, str | None]:
    """(`verified` | `unresolved` | `unchecked`, why) for one quotation."""
    failures, resolvable = [], False
    for raw in refs:
        outcome = resolve(raw, default_slug, quote)
        if outcome == UNKNOWN_SOURCE:
            continue
        resolvable = True
        if outcome is None:
            return "verified", None
        failures.append(outcome)
    if not resolvable:
        return "unchecked", None
    return "unresolved", failures[0]


def check_file(path: Path, default_slug: str | None,
               text: str | None = None) -> tuple[list[dict], int]:
    problems, unchecked = [], 0
    for match, near in pairs(path.read_text(encoding="utf-8") if text is None else text):
        status, why = verdict(near, default_slug, match.group("quote"))
        if status == "unchecked":
            unchecked += 1
        elif status == "unresolved":
            problems.append({"quote": match.group("quote")[:60], "ref": near[0], "why": why})
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
    for raw in [line for line in span if line is not None]:
        gap = on_line(raw, quote, parts)
        if gap is None:
            return None
        missing = gap
    return f"not on that line: {missing[:60]!r}"


def slug_of(path: Path, text: str | None = None) -> str | None:
    """Which document a file's bare ^[Lnn] refers to.

    A census or a note says so in `source:`. A wiki page does not -- it says
    which documents it was built from in `ingested:`, and a bare `^[Lnn]` on a
    page written during one document's reconciliation means that document. When
    a page carries several, a bare reference is ambiguous and is **not** checked
    rather than checked against a guess.
    """
    head = (path.read_text(encoding="utf-8") if text is None else text)[:900]
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


def tally(targets: list[Path] | None = None) -> dict:
    """Check every quotation in `targets` — by default every census, note and wiki file.

    `{checked, unresolved, unchecked, problems: [(path, problem)]}`. The one count:
    `main` prints it, and `state.py` and `ui.py` read it here instead of parsing
    the printout, which returned 0 unresolved without a word the day the wording
    changed.
    """
    if targets is None:
        targets = sorted(
            list((ROOT / "Sources" / "notes").glob("*.md"))
            + list((ROOT / "Sources" / "terms").glob("*.md"))
            + list((ROOT / "Wiki").rglob("*.md"))
        )
    checked = uncited = 0
    problems: list[tuple[Path, dict]] = []
    for path in targets:
        text = path.read_text(encoding="utf-8")
        found, skipped = check_file(path, slug_of(path, text), text)
        checked += len(QUOTE.findall(unraw(text))) - skipped
        uncited += skipped
        problems += [(path, problem) for problem in found]
    return {"checked": checked, "unresolved": len(problems), "unchecked": uncited,
            "problems": problems}


def summary(counts: dict, wrap: str = " ") -> str:
    """The tally as one sentence: what `main` ends with, and the line ui.py shows."""
    return (f"{counts['checked']} cited quotes checked, {counts['unresolved']} unresolved; "
            f"{counts['unchecked']} quotes had no citation on their own line, or none naming a"
            f"{wrap}document that could be resolved, and were not checked.")


def main(argv: list[str]) -> int:
    show_unchecked = "--unchecked" in argv
    paths = [arg for arg in argv if arg != "--unchecked"]
    if len(paths) > 1:
        raise SystemExit("usage: quotes.py [--unchecked] [path]")
    targets = [Path(paths[0]).resolve()] if paths else None
    result = tally(targets)
    if show_unchecked:
        if targets is None:
            targets = sorted(list((ROOT / "Sources" / "notes").glob("*.md"))
                             + list((ROOT / "Sources" / "terms").glob("*.md"))
                             + list((ROOT / "Wiki").rglob("*.md")))
        for path in targets:
            source = path.read_text(encoding="utf-8")
            starts = line_starts(source)
            default = slug_of(path, source)
            for match, refs in pairs(source):
                if verdict(refs, default, match.group("quote"))[0] == "unchecked":
                    where = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
                    row = line_of(starts, match.start()) + 1
                    fragment = WRAP.sub(" ", match.group("quote"))[:100]
                    print(f"UNCHECKED  {where}:{row}  {fragment!r}  refs={refs!r}")
    for path, problem in result["problems"]:
        where = path.relative_to(ROOT) if path.is_relative_to(ROOT) else path
        print(f"UNRESOLVED  {where}  ^[{problem['ref']}]")
        print(f"            „{problem['quote']}…\"")
        print(f"            {problem['why']}")
    print("\n" + summary(result, wrap="\n")
          + "\nA bare ^[Lnn] resolves against the file's own `source:`.")
    return 1 if result["unresolved"] else 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
