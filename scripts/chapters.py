"""The chapter as a unit of the wiki, beside the term — pages checked, an overview derived.

Decision 001 named its own reversal: „if most questions are about chapters and
plot rather than terms, the unit is wrong". On 2026-09-25 the author asked for
exactly that — „start to Focus on Plot and the Chapters a Bit more" (decision
013). So `Wiki/chapters/kap-NN.md` holds one page per chapter of the planned
novel, and each collects what every read source says about that chapter, one
`## Reading` per document, quoted, cited and unmerged — the term page's rule
applied to a chapter.

A chapter page is written by a person, like a term page. This script does the
three things about them that are decidable:

- **check** — the page is what it claims: its file name and `chapter:` agree,
  every reading is of a reconciled document, `ingested:` and `sources:` list
  exactly the documents read onto it, a citation inside a reading names that
  reading's document, every `[[link]]` resolves, and the overview is current.
- **overview** — `Wiki/overview/chapters.md` is *derived* from the pages: every
  source's title for every chapter, side by side, each with its citation. A
  table written by hand beside forty pages would drift on the first edit (P6).
- **missing** — P10's `MISSING`, measured: which read documents name a chapter
  as `Kap N` and have no reading on that chapter's page.

What `missing` can see is a pattern, and it says what the pattern misses. It
finds `Kap 7`, `Kapitel 7`, `Kap. 7`, `Kap-7-Lock`, `Kap0`, lists (`Kap 18/21/22`,
`Kap 2, 10, 25`, `Kap 0↔40`) and ranges (`Kap 1–13`, and `Kap 14–~20` with the
approximate bound escaped as the export writes it). **A range is not counted
as naming each chapter in it** — `Kap 14–26` is an act, not thirteen statements.
**A numbered list under an act heading is invisible to it**: the storyform
outline's Akt I is `7.  **Die Stimme im Rauschen**`, with no `Kap`. So `missing`
under-counts; it never reports a chapter a document does not name.

    python3 scripts/chapters.py                 # check; non-zero on any defect
    python3 scripts/chapters.py overview        # rewrite Wiki/overview/chapters.md
    python3 scripts/chapters.py missing [slug]  # read documents naming a chapter it has no reading from
    python3 scripts/chapters.py index N         # every line of a read document naming Kap N
    python3 scripts/chapters.py selftest        # each check handed the defect it exists to name
"""

from __future__ import annotations

import re
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from subject import PAGES, cli, document  # noqa: E402
from wiki_index import frontmatter  # noqa: E402

CHAPTERS = ROOT / "Wiki" / "chapters"
OVERVIEW = ROOT / "Wiki" / "overview"
TABLE = OVERVIEW / "chapters.md"
RUNS = ROOT / "Plan" / "runs"
LAST = 40                                    # Kap 0 … Kap 40: the highest any read source counts

# `Kap` or `Kapitel`, then a number, then any further numbers joined by a list or
# range mark. Not preceded by a letter, so `Unterkapitel 3` is not Kap 3; the
# number may not run on into a decimal or a longer number. A number may carry an
# approximate `~`, which the export escapes as `\\\~`: `Kap 14–\\\~20` is a range.
MENTION = re.compile(
    r"(?<![A-Za-zÄÖÜäöüß])Kap(?:itels?)?(?:\\?\.|\s|-)*(?:\\*~)?(\d{1,2})(?![\d,.]\d)"
    r"((?:\s*(?:[–—-]|/|,|↔|\+|&|und|bis)\s*(?:\\*~)?\d{1,2}(?![\d.]\d))*)")
JOIN = re.compile(r"\s*([–—-]|bis|/|,|↔|\+|&|und)\s*(?:\\*~)?(\d{1,2})")
READING = re.compile(r"^## Reading — `([^`]+)`", re.M)
SECTION = re.compile(r"^## ", re.M)
CITE = re.compile(r"\^\[([^\]]+?)\.md:L\d+(?:[–-]L?\d+)?\]")
WIKILINK = re.compile(r"\[\[([^\]|#]+)(?:[|#][^\]]*)?\]\]")
TITLE = re.compile(r"^Title: (?P<quote>„[^“\"]+[“\"]) (?P<cite>\^\[[^\]]+\])", re.M)
NAME = re.compile(r"^kap-(\d{2})$")


def named(line: str) -> tuple[set[int], set[int]]:
    """The chapters a line names singly, and those it names only inside a range."""
    single, spanned = set(), set()
    for match in MENTION.finditer(line):
        numbers, marks = [int(match.group(1))], []
        for mark, number in JOIN.findall(match.group(2)):
            marks.append(mark)
            numbers.append(int(number))
        previous = numbers[0]
        single.add(previous)
        for mark, number in zip(marks, numbers[1:]):
            if mark in "–—-" or mark == "bis":
                single.discard(previous)
                spanned.update(range(previous, number + 1))
            else:
                single.add(number)
            previous = number
    keep = set(range(LAST + 1))
    return single & keep, (spanned - single) & keep


def reconciled() -> list[str]:
    """The documents read into the wiki: a run directory holding a reconcile.json."""
    return sorted(p.parent.name for p in RUNS.glob("*/reconcile.json"))


def index(slugs: list[str] | None = None) -> dict[int, dict[str, list[int]]]:
    """chapter → document → the file lines naming it singly."""
    out: dict[int, dict[str, list[int]]] = defaultdict(lambda: defaultdict(list))
    for slug in slugs if slugs is not None else reconciled():
        doc = document(slug)
        for number, line in enumerate(doc.lines(), start=doc.offset):
            for chapter in named(line)[0]:
                out[chapter][slug].append(number)
    return out


def pages(root: Path = CHAPTERS) -> dict[int, dict]:
    """Every chapter page: chapter → {path, meta, text, readings}."""
    out = {}
    for path in sorted(root.glob("kap-*.md")):
        text = path.read_text(encoding="utf-8")
        match = NAME.match(path.stem)
        number = int(match.group(1)) if match else -1
        out[number] = {"path": path, "meta": frontmatter(text), "text": text,
                       "readings": READING.findall(text)}
    return out


def sections(text: str) -> list[tuple[str | None, str]]:
    """(the document a `## Reading` section reads, or None; the section's text)."""
    starts = [m.start() for m in SECTION.finditer(text)] + [len(text)]
    out = [(None, text[:starts[0]])]
    for start, end in zip(starts, starts[1:]):
        body = text[start:end]
        reading = READING.match(body)
        out.append((reading.group(1) if reading else None, body))
    return out


def record_ids() -> set[str]:
    """The ids a chapter page's `records:` may name: every conflict and question record."""
    ids = set()
    for path in list((ROOT / "Wiki" / "conflicts").glob("*.md")) + list((ROOT / "Wiki" / "questions").glob("*.md")):
        found = frontmatter(path.read_text(encoding="utf-8")).get("id")
        if found:
            ids.add(found)
    return ids


def targets() -> set[str]:
    """What a `[[link]]` may point at: a term page or a chapter page."""
    return {p.stem for p in PAGES.glob("*.md")} | {p.stem for p in CHAPTERS.glob("kap-*.md")}


def check_readings(name: str, text: str, read: set[str], known: set[str],
                   records: set[str] | None = None) -> list[str]:
    """The defects any page made of `## Reading` sections can have: a chapter page or plot.md."""
    problems = []
    meta = frontmatter(text)
    readings = READING.findall(text)
    for slug in readings:
        if slug not in read:
            problems.append(f"{name}: a reading of {slug}, which no reconcile.json records as read")
    if len(set(readings)) != len(readings):
        problems.append(f"{name}: a document with two readings")
    if sorted(meta.get("ingested", [])) != sorted(set(readings)):
        problems.append(f"{name}: ingested lists {sorted(meta.get('ingested', []))}, "
                        f"the readings are {sorted(set(readings))}")
    if meta.get("sources") != str(len(set(readings))):
        problems.append(f"{name}: sources: {meta.get('sources')} for {len(set(readings))} readings")
    for slug, body in sections(text):
        for cited in CITE.findall(body):
            if slug is not None and cited != slug:
                problems.append(f"{name}: the reading of {slug} cites {cited}")
            elif cited not in read:
                problems.append(f"{name}: cites {cited}, which is not a read document")
    for target in WIKILINK.findall(text):
        if target.strip() not in known:
            problems.append(f"{name}: [[{target}]] points at no page")
    for record in meta.get("records", []):
        if records is not None and record not in records:
            problems.append(f"{name}: records names {record}, which no conflict or question record has as its id")
    return problems


def check_page(path: Path, text: str, read: set[str], known: set[str],
               records: set[str] | None = None) -> list[str]:
    """Every defect on one chapter page, each named."""
    match = NAME.match(path.stem)
    if not match:
        return [f"{path.name}: a chapter page is named kap-NN.md"]
    problems = []
    chapter = frontmatter(text).get("chapter")
    if chapter != str(int(match.group(1))):
        problems.append(f"{path.name}: chapter: {chapter!r} is not {int(match.group(1))}")
    return problems + check_readings(path.name, text, read, known, records)


def overview(chapters: dict[int, dict]) -> str:
    """Wiki/overview/chapters.md, derived from the pages' Title lines and frontmatter."""
    rows = []
    for number in sorted(chapters):
        page = chapters[number]
        titles = [f"{m.group('quote')} {m.group('cite')}" for m in TITLE.finditer(page["text"])]
        records = ", ".join(page["meta"].get("records", [])) or "—"
        rows.append(f"| [Kap {number}](../chapters/{page['path'].name}) | {page['meta'].get('sources', '0')} "
                    f"| {' · '.join(titles) or '—'} | {records} |")
    return OVERVIEW_HEAD + "\n".join(rows) + "\n"


OVERVIEW_HEAD = """\
# Chapters — every source's title, side by side

**Derived, not written.** `python3 scripts/chapters.py overview` writes this page
from the `Title:` line of every reading on every page in `Wiki/chapters/`, and
`python3 scripts/chapters.py` fails when it is stale. Change a chapter page, not
this one.

A title is quoted from its source and cited to its line; the citation names the
document. Where two titles differ, both stand — which one the novel uses is the
author's call. **Records** are the conflict and question records the chapter page
names in its `records:` frontmatter. The plot these chapters make up is in
[plot.md](plot.md).

| chapter | readings | titles, as each source gives them | records |
|---|--:|---|---|
"""


def missing(slugs: list[str] | None = None) -> list[tuple[str, int, list[int]]]:
    """(document, chapter, lines) for each chapter a read document names with no reading from it."""
    chapters = pages()
    out = []
    for chapter, docs in sorted(index(slugs).items()):
        have = set(chapters.get(chapter, {}).get("readings", []))
        for slug, lines in sorted(docs.items()):
            if slug not in have:
                out.append((slug, chapter, lines))
    return out


def check() -> list[str]:
    read, known, records = set(reconciled()), targets(), record_ids()
    problems = []
    for number, page in sorted(pages().items()):
        problems += check_page(page["path"], page["text"], read, known, records)
    for path in sorted(OVERVIEW.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        if path != TABLE and frontmatter(text).get("ingested") is not None:
            problems += check_readings(f"overview/{path.name}", text, read, known, records)
            continue
        for target in WIKILINK.findall(text):
            if target.strip() not in known:
                problems.append(f"overview/{path.name}: [[{target}]] points at no page")
        for cited in CITE.findall(text):
            if cited not in read:
                problems.append(f"overview/{path.name}: cites {cited}, which is not a read document")
    chapters = pages()
    if chapters and (not TABLE.exists() or TABLE.read_text(encoding="utf-8") != overview(chapters)):
        problems.append("overview/chapters.md is stale — python3 scripts/chapters.py overview")
    return problems


# ---------------------------------------------------------------- selftest

PAGE = """---
chapter: {n}
status: candidate
sources: {sources}
ingested: [{ingested}]
records: [{records}]
gathered: "2026-09-25"
---

# Kap {n}

## Reading — `{slug}`, 2026-05-18

Title: „Die Stimme im Rauschen“ ^[{cited}.md:L391]

- Story: „Telefon-Stille als erster expliziter Anker“ ^[{cited}.md:L399] {link}
"""


def selftest() -> int:
    """Each check handed the exact defect it exists to name, and a clean page it must pass."""
    failures = []
    mentions = {
        "Kap 7 — Die Stimme": ({7}, set()),
        "Kap 18/21/22 als Flashback-Träger": ({18, 21, 22}, set()),
        "Zahl 734 (Kap 2, 10, 25).": ({2, 10, 25}, set()),
        "Ouroboros-Spiegelungen Kap 0↔40": ({0, 40}, set()),
        "Akt I (Kap 1–13)": (set(), set(range(1, 14))),
        "Kapitel 14 / Teil 2": ({14}, set()),
        "Kap-1-Locks (2026-05-30)": ({1}, set()),
        "Kap0-Kap40-Doppelklammer": ({0, 40}, set()),
        "Kap 38 Beat 3": ({38}, set()),
        "Kapitel-Kompendium 2026-05-31": (set(), set()),
        "Unterkapitel 3": (set(), set()),
        "\\*\\*Kap 33\\*\\* | Überwelt": ({33}, set()),
        "Kap 734": (set(), set()),
        "Akt II (Kap 14–\\\\\\~20)": (set(), set(range(14, 21))),
        "Akt II (Kap \\\\\\~20–26)": (set(), set(range(20, 27))),
        "Vortex-Vorläufer ab \\~Kap 28.": ({28}, set()),
    }
    for line, want in mentions.items():
        if named(line) != want:
            failures.append(f"named({line!r}) = {named(line)}, want {want}")

    slug = "koharenz-protokoll-strukturierter-outline-2026-05-18-md"
    read, known, records = {slug}, {"juna", "kap-07"}, {"C7"}
    clean = dict(n=7, sources=1, ingested=f'"{slug}"', slug=slug, cited=slug, link="[[juna]]", records='"C7"')
    defects = {
        "is not 7": dict(clean, n=8),
        "no reconcile.json records": dict(clean, slug="unread-document", ingested='"unread-document"'),
        "ingested lists": dict(clean, ingested='"other-md"'),
        "sources: 2 for 1": dict(clean, sources=2),
        f"the reading of {slug} cites": dict(clean, cited="kohaerenz-protokoll-charakter-bibel-2026-05-08-md"),
        "[[nowhere]] points at no page": dict(clean, link="[[nowhere]]"),
        "records names C99": dict(clean, records='"C99"'),
    }
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "kap-07.md"
        found = check_page(path, PAGE.format(**clean), read, known, records)
        if found:
            failures.append(f"a clean page reported {found}")
        for expect, fields in defects.items():
            found = check_page(path, PAGE.format(**fields), read, known, records)
            if not any(expect in problem for problem in found):
                failures.append(f"defect {expect!r} not named; got {found}")
        page = {"path": path, "meta": frontmatter(PAGE.format(**clean)), "text": PAGE.format(**clean)}
        table = overview({7: page})
        if f"„Die Stimme im Rauschen“ ^[{slug}.md:L391]" not in table or "| C7 |" not in table:
            failures.append("overview dropped a title or its citation")
    for failure in failures:
        print("FAIL", failure)
    print(f"chapters selftest: {len(mentions)} mention cases, {len(defects)} page defects, "
          f"{'held' if not failures else f'{len(failures)} FAILED'}")
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    command = argv[0] if argv else "check"
    if command == "selftest":
        return selftest()
    if command == "overview":
        TABLE.parent.mkdir(parents=True, exist_ok=True)
        TABLE.write_text(overview(pages()), encoding="utf-8")
        print(f"wrote {TABLE.relative_to(ROOT)} from {len(pages())} chapter pages")
        return 0
    if command == "missing":
        rows = missing(argv[1:] or None)
        for slug, chapter, lines in rows:
            print(f"Kap {chapter:>2}  {slug}  L{', L'.join(map(str, lines[:8]))}"
                  f"{' …' if len(lines) > 8 else ''}")
        print(f"{len(rows)} chapter mentions in read documents with no reading on the chapter's page "
              f"(single `Kap N` mentions only; ranges and numbered lists are not counted)")
        return 0
    if command == "index":
        chapter = int(argv[1])
        for slug, lines in sorted(index().get(chapter, {}).items()):
            print(f"{slug}  L{', L'.join(map(str, lines))}")
        return 0
    if command != "check":
        raise SystemExit(__doc__)
    problems = check()
    for problem in problems:
        print(problem)
    chapters = pages()
    print(f"{len(chapters)} chapter pages, {sum(len(p['readings']) for p in chapters.values())} readings, "
          f"{len(problems)} defects")
    return 1 if problems else 0


if __name__ == "__main__":
    cli(main)
