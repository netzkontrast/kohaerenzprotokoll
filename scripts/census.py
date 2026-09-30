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
section, or whose tables no longer equal `counts.json` — a row dropped, added,
or its numbers changed by hand. Standard library only.

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
HEADER = """> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts."""


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


def table(slug: str, terms: list[str], counts: dict, text: str) -> list[str]:
    out = ["| candidate | word | in | lines | surfaces |", "|---|---|---|---|---|"]
    for term in terms:
        c = counts.get(term)
        if c is None:
            continue
        forms = ", ".join(f"`{f}` ×{n}" for f, n in surfaces(term, text))
        lines = ", ".join(str(n) for n in c["lines"][:12]) + (" …" if len(c["lines"]) > 12 else "")
        out.append(f"| `{term}` ^[{slug}.md:#{c['n']}] | {c['n']} | {c['n_including_compounds']} "
                   f"| {lines} | {forms} |")
    return out


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
    front = prof.census_frontmatter(slug)
    front = re.sub(r"^candidates: .*$", f"candidates: {len(counts)}    # the terms capture.py counted",
                   front, flags=re.M)
    title = re.search(r'^title: "?(.*?)"?$', front, re.M).group(1)
    zero = [t for t in named + lens if t in counts and counts[t]["n"] == 0]
    differ = [t for t in named + lens if t in counts and counts[t]["n"] and
              counts[t]["n"] != counts[t]["n_including_compounds"]]
    prose = counts_json.get("read_as_prose") or []
    out = [front.rstrip("\n"), "", f"# Term census — {title}", "", HEADER, "",
           "## Structural profile", "", f"`python3 scripts/profile.py {slug}`", "", "```",
           prof.render(prof.profile(document(slug))).split("\n", 1)[1].rstrip("\n"), "```", "",
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
    rows = {}
    for m in ROW.finditer(text):
        if m.group("slug") == slug:
            rows[m.group("term").replace("``", "`")] = (int(m.group("n")), int(m.group("word")),
                                                          int(m.group("inside")))
    for term, c in counts.items():
        got = rows.get(term)
        if got is None:
            problems.append(f"`{term}` has no row")
        elif got != (c["n"], c["n"], c["n_including_compounds"]):
            problems.append(f"`{term}`: the row says {got[1]}/{got[2]}, counts.json {c['n']}/"
                            f"{c['n_including_compounds']}")
    for term in rows:
        if term not in counts:
            problems.append(f"`{term}` has a row but was not counted")
    return problems


def selftest() -> int:
    slug = "kohaerenz-protokoll-meta-foreshadowing-beobachter-logik"
    cases = []
    text = draft(slug)
    counts = json.loads((RUNS / slug / "counts.json").read_text(encoding="utf-8"))["counts"]
    cases.append(("every counted term has a row", all(f"| `{t}` ^[{slug}.md:#" in text for t in counts)))
    cases.append(("the draft carries both reader marks", text.count(READER) == 2))
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
    import quotes
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
