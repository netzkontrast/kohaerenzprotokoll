"""The census, drafted by code where it is mechanical, so a reader writes only judgement.

A census (`Sources/terms/<slug>.md`) has four parts. Three were typed by hand
for 53 documents and are mechanical:

- the frontmatter, from the manifest (`profile.py --frontmatter`);
- the structural profile, which is `profile.py`'s output in a code block;
- the candidate tables — every row of the frozen list with the counts `capture.py
  --count` computed, the lines, the inflected surfaces, and a count mark
  `quotes.py` checks. 63 to 318 rows per document.

The reader of 2026-09-29 typed those tables row by row, and nine of twelve
readers read script sources to find out what they looked like
(`Plan/runs/reader-lab-2026-09-30/`). So `draft` writes them, and leaves two
places for the reader, each marked `<!-- reader: … -->`:

- `## Stance, read per passage` — how the document speaks, passage by passage;
- `## What the extraction ran into` — which code opens with the facts a reader
  must explain: every zero, every term whose standing-alone count differs from its
  count with compounds, every `- ` line read as prose.

`check` fails on a census that still carries a `<!-- reader:` mark, lacks a
section, or whose mechanical parts are no longer the ones `draft` writes from
`counts.json` and the document: a row dropped, added or doubled, any cell of one
changed by hand — counts, lines or surfaces — or the frontmatter, the profile or
one of the facts changed. A candidate written with „…“ in it cites the line its
quotation stands on, so `quotes.py` checks it. Standard library only.

    python3 scripts/census.py draft <slug>    # writes Plan/runs/<slug>/census-draft.md
    python3 scripts/census.py check <slug>    # the census in Sources/terms/ against counts.json
    python3 scripts/census.py selftest
"""

from __future__ import annotations

import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from capture import PROSE, body_of, surfaces  # noqa: E402

RUNS = ROOT / "Plan" / "runs"
SECTIONS = ("## Structural profile", "## Stance, read per passage", "## Candidates and counts",
            "## What the extraction ran into")
READER = "<!-- reader:"
ROW = re.compile(r"^\| `(?P<term>(?:[^`]|``)+)` \^\[(?P<slug>[A-Za-z0-9\-]+)\.md:#(?P<n>\d+)\] "
                 r"\| (?P<word>\d+) \| (?P<inside>\d+) \|", re.M)
QUOTE = re.compile(r"„(?P<quote>[^„“]{1,400})[“\"]")


def grouped(candidates_md: str) -> tuple[list[str], list[str]]:
    """The list's terms as the document names them, and the lens — `## lens` sections.

    Headings vary from list to list; `## lens` (with or without a line range) is
    the one every reader has used for borrowed concepts since decision 012.
    """
    named, lens, in_lens = [], [], False
    for line in candidates_md.split("\n"):
        if line.startswith("## "):
            in_lens = line[3:].strip().lower().startswith("lens")
            continue
        if not line.startswith("- "):
            continue
        term = line[2:].strip()
        if term and not PROSE.search(term):
            (lens if in_lens else named).append(term)
    return named, lens


def cited(slug: str, term: str, lines: list[int]) -> str:
    """The line references a candidate's quotations need, or "".

    A candidate written with „…“ in it — `„Aufmerksamkeit“ (Energie)` — is a
    quotation to `quotes.py`, and one with no reference on its row is reported
    unchecked (the review of #120, 2026-09-30). So each quotation gets the line
    `read.py` places it on, preferring a line the candidate itself stands on.
    Where a quotation stands on no line, nothing is cited and `draft` says so.
    """
    import read
    from subject import document
    refs = []
    for m in QUOTE.finditer(term):
        at = read.locate(document(slug), m.group("quote"))
        if at:
            refs.append(f"^[L{next((n for n in at if n in lines), at[0])}]")
    return (" " + " ".join(refs)) if refs else ""


def row(slug: str, term: str, c: dict, text: str) -> str:
    """One candidate's row, exactly as `draft` writes it and `check` expects it."""
    forms = ", ".join(f"`{f}` ×{n}" for f, n in surfaces(term, text))
    lines = ", ".join(str(n) for n in c["lines"][:12]) + (" …" if len(c["lines"]) > 12 else "")
    return (f"| `{term}` ^[{slug}.md:#{c['n']}] | {c['n']} | {c['n_including_compounds']} "
            f"| {lines}{cited(slug, term, c['lines'])} | {forms} |")


def table(slug: str, terms: list[str], counts: dict, text: str) -> list[str]:
    out = ["| candidate | word | in | lines | surfaces |", "|---|---|---|---|---|"]
    return out + [row(slug, term, counts[term], text) for term in terms if term in counts]


def draft(slug: str, runs: Path = RUNS) -> str:
    import profile as prof
    from subject import document
    run = runs / slug
    counts_file = run / "counts.json"
    if not counts_file.exists():
        raise SystemExit(f"no {counts_file.relative_to(ROOT)} — capture.py {slug} --count first")
    counts_json = json.loads(counts_file.read_text(encoding="utf-8"))
    counts = counts_json["counts"]
    named, lens = grouped((run / "03-candidates.md").read_text(encoding="utf-8"))
    text, _ = body_of(slug)
    # `census_frontmatter` writes the frontmatter, the title, the one-document header
    # and the structural profile. Until R1 of the reader lab (2026-09-30) `draft`
    # wrote the last three again after it.
    front = prof.census_frontmatter(slug)
    front = re.sub(r"^candidates: .*$", f"candidates: {len(counts)}    # the terms capture.py counted",
                   front, flags=re.M)
    zero = [t for t in named + lens if t in counts and counts[t]["n"] == 0]
    differ = [t for t in named + lens if t in counts and counts[t]["n"] and
              counts[t]["n"] != counts[t]["n_including_compounds"]]
    prose = counts_json.get("read_as_prose") or []
    unplaced = [t for t in named + lens if t in counts and QUOTE.search(t)
                and len(QUOTE.findall(t)) > len(re.findall(r"\^\[L", cited(slug, t, counts[t]["lines"])))]
    out = [front.rstrip("\n"), "",
           "## Stance, read per passage", "",
           f"{READER} how the document speaks, passage by passage, each passage with its lines. "
           "What it marks as a plan, a report, a lock or a question, in its own words. -->", "",
           "## Candidates and counts", "",
           f"{len(counts)} candidates, written while reading and frozen by the count "
           f"(`Plan/runs/{slug}/03-candidates.md`, counted by `capture.py --count`). `word` is the "
           "term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also "
           "a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; "
           "`lines` are the file lines that hold the term as a substring. The list is in order of first "
           f"appearance. `{slug}.md` in a mark is this document. Rows written by `census.py draft`.", "",
           "### As the document names them", ""] + table(slug, named, counts, text)
    if lens:
        out += ["", "### Lens", "", "Borrowed concepts the document applies to its world, set apart by "
                "the list under a `## lens` heading.", ""] + table(slug, lens, counts, text)
    out += ["", "## What the extraction ran into", "",
            f"{READER} explain each fact below — an inflection, export damage, or a term the document "
            "truly lacks — then anything else the reading met. Delete this mark and keep the facts. -->", "",
            f"**Zeros:** {len(zero)}" + (" — " + ", ".join(f"`{t}`" for t in zero) if zero else "") + ".", "",
            f"**Standing alone less often than with compounds:** {len(differ)}"
            + (" — " + ", ".join(f"`{t}` {counts[t]['n']}/{counts[t]['n_including_compounds']}"
                                 for t in differ[:40]) + (" …" if len(differ) > 40 else "") if differ else "")
            + ".", ""]
    if prose:
        out += [f"**`- ` lines read as prose and not counted:** {len(prose)} — "
                + " · ".join(prose) + ".", ""]
    if unplaced:
        out += [f"**A quotation in a candidate that no line holds:** {len(unplaced)} — "
                + ", ".join(f"`{t}`" for t in unplaced) + ". `quotes.py` reports each as unchecked.", ""]
    return "\n".join(out).rstrip("\n") + "\n"


def check(slug: str, census: Path | None = None, runs: Path = RUNS) -> list[str]:
    census = census or ROOT / "Sources" / "terms" / f"{slug}.md"
    if not census.exists():
        return [f"no census at {census}"]
    text = census.read_text(encoding="utf-8")
    if "census.py draft" not in text:
        return [f"not drafted by census.py — its tables were typed by hand, in a format this check "
                f"does not read (the 53 censuses before 2026-09-30)"]
    problems = []
    if READER in text:
        problems.append("a `<!-- reader:` mark is still in it — a section was not written")
    for section in SECTIONS:
        if section not in text:
            problems.append(f"no `{section}`")
    counts = json.loads((runs / slug / "counts.json").read_text(encoding="utf-8"))["counts"]
    # Every cell of a row is mechanical, so the row is compared whole with the one
    # `draft` writes. Until the review of #120 (2026-09-30) only the mark and the
    # two counts were, and a row claiming line 999999 and a surface `FAKE` held.
    body, _ = body_of(slug)
    got: dict[str, list[str]] = {}
    for line in text.split("\n"):
        m = ROW.match(line)
        if m and m.group("slug") == slug:
            got.setdefault(m.group("term").replace("``", "`"), []).append(line.rstrip())
    for term, c in counts.items():
        rows = got.get(term, [])
        want = row(slug, term, c, body)
        if not rows:
            problems.append(f"`{term}` has no row")
            continue
        if len(rows) > 1:
            problems.append(f"`{term}` has {len(rows)} rows")
        for line in rows:
            if line != want:
                problems.append(f"`{term}`: the row is not the one census.py draft writes — "
                                f"{line[len(term) + 4:][:90]!r}, expected {want[len(term) + 4:][:90]!r}")
    for term in got:
        if term not in counts:
            problems.append(f"`{term}` has a row but was not counted")
    # Everything else `draft` writes is as mechanical as the rows: the frontmatter
    # (its `extracted:` date aside), the profile, the candidates section around its
    # rows, and the facts the last section opens with.
    want = draft(slug, runs)
    if front_of(text) != front_of(want):
        problems.append("the frontmatter is not the one census.py draft writes")
    if section_of(text, "## Structural profile") != section_of(want, "## Structural profile"):
        problems.append("the structural profile is not the one census.py draft writes")
    if not problems and section_of(text, SECTIONS[2]) != section_of(want, SECTIONS[2]):
        problems.append("the candidates section is not the draft's outside its rows — a line added, "
                        "dropped or changed")
    for fact in (section_of(want, SECTIONS[3]) or "").split("\n"):
        if fact.startswith("**") and fact not in text.split("\n"):
            problems.append(f"a fact the draft states is gone or changed: {fact[:80]}")
    return problems


def front_of(text: str) -> list[str]:
    m = re.match(r"\A---\n(.*?)\n---\n", text, re.S)
    return [l for l in (m.group(1).split("\n") if m else []) if not l.startswith("extracted:")]


def section_of(text: str, heading: str) -> str | None:
    """A section from its heading to the next `## ` heading, or None."""
    start = text.find(heading + "\n")
    if start < 0:
        return None
    end = text.find("\n## ", start + len(heading))
    return text[start:end if end >= 0 else len(text)].rstrip()


def selftest() -> int:
    import quotes
    slug = "kohaerenz-protokoll-meta-foreshadowing-beobachter-logik"
    cases = []
    text = draft(slug)
    counts = json.loads((RUNS / slug / "counts.json").read_text(encoding="utf-8"))["counts"]
    cases.append(("every counted term has a row", all(f"| `{t}` ^[{slug}.md:#" in text for t in counts)))
    cases.append(("the draft carries both reader marks", text.count(READER) == 2))
    cases.append(("one title, one header, one profile",
                  text.count("\n# Term census — ") == 1 and text.count("describes one document and nothing else") == 1
                  and text.count("\n## Structural profile\n") == 1))
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp) / "census.md"
        f.write_text(text, encoding="utf-8")
        cases.append(("an unwritten section fails", any("reader" in p for p in check(slug, f))))
        filled = re.sub(r"<!-- reader:.*?-->", "Written.", text, flags=re.S)
        f.write_text(filled, encoding="utf-8")
        cases.append(("a written draft holds", check(slug, f) == []))
        term = next(iter(counts))
        f.write_text(filled.replace(f"| `{term}` ^[{slug}.md:#{counts[term]['n']}] | {counts[term]['n']} |",
                                    f"| `{term}` ^[{slug}.md:#{counts[term]['n']}] | {counts[term]['n'] + 1} |"),
                     encoding="utf-8")
        cases.append(("a number changed by hand fails", any(term in p for p in check(slug, f))))
        f.write_text("\n".join(l for l in filled.split("\n") if not l.startswith(f"| `{term}` ")),
                     encoding="utf-8")
        cases.append(("a dropped row fails", any("has no row" in p for p in check(slug, f))))
        # The review of #120 (2026-09-30): a row whose lines and surfaces were forged held.
        mine = next(l for l in filled.split("\n") if l.startswith(f"| `{term}` "))
        forged = "|".join(mine.split("|")[:4] + [" 999999 ", " `FAKE` ×99 ", ""])
        f.write_text(filled.replace(mine, forged), encoding="utf-8")
        cases.append(("forged lines and surfaces fail", any(term in p for p in check(slug, f))))
        f.write_text(filled.replace(mine, mine + "\n" + mine), encoding="utf-8")
        cases.append(("a doubled row fails", any("2 rows" in p for p in check(slug, f))))
        f.write_text(filled.replace(mine, mine + "\n| `ERFUNDEN` | 3 | 3 | 1, 2, 3 |  |"), encoding="utf-8")
        cases.append(("a row with no count mark fails", any("outside its rows" in p for p in check(slug, f))))
        fact = next(l for l in filled.split("\n") if l.startswith("**Zeros:**"))
        f.write_text(filled.replace(fact, "**Zeros:** none."), encoding="utf-8")
        cases.append(("a changed fact fails", any("fact the draft states" in p for p in check(slug, f))))
        # ... and a candidate written with „…“ came out as an uncited quotation.
        f.write_text(filled, encoding="utf-8")
        problems, unchecked = quotes.check_file(f, slug)
        cases.append(("the whole draft passes quotes.py, its candidates' quotations cited",
                      any("„" in t for t in counts) and not problems and unchecked == 0))
    marks_made, marks_wrong = quotes.check_marks(text)
    cases.append(("every count mark holds for quotes.py", marks_made >= len(counts) and not marks_wrong))
    failed = [n for n, ok in cases if not ok]
    print(f"census: {len(cases) - len(failed)} of {len(cases)} cases hold"
          + (" — FAILED: " + ", ".join(failed) if failed else ""))
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        return selftest()
    if len(argv) != 2 or argv[0] not in ("draft", "check"):
        print(__doc__)
        return 2
    verb, slug = argv
    if verb == "draft":
        out = RUNS / slug / "census-draft.md"
        out.write_text(draft(slug), encoding="utf-8")
        print(f"wrote {out.relative_to(ROOT)} — fill the two `<!-- reader:` sections, "
              f"then save it as Sources/terms/{slug}.md")
        return 0
    problems = check(slug)
    for p in problems:
        print(f"  {p}")
    print(f"census {slug}: " + ("holds" if not problems else f"{len(problems)} problems"))
    return 1 if problems else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
