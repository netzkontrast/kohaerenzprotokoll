#!/usr/bin/env python3
"""Every cited claim of a note and census beside the line it cites — code writes the pairs, a reader writes two cells.

`quotes.py` checks a quotation against its line and cannot check what the sentence around it
*says*. That is the defect class that survived every mechanical check: 7 of the 11 defects of
the quality sample of 2026-09-29, and in the lab of 2026-09-30 four of sixteen claims of one
Haiku reader (R2) and nine of about thirty of another (R3), whose prose pass wrote „Verified“ under
each. R4 was asked for a table and left it out. So the table is drafted by code, the way
`census.py` drafts a census: the reader fills what only a reader can.

    python3 scripts/claims.py draft <slug>     # Plan/runs/<slug>/claims-draft.md
    python3 scripts/claims.py check <slug>     # Plan/runs/<slug>/claims.md against the note and census
    python3 scripts/claims.py show <slug>      # a reviewer's view: each sentence, then its whole line
    python3 scripts/claims.py selftest

`draft` takes the whole note and the census's two hand-written sections — `## Stance, read
per passage` and `## What the extraction ran into` — and writes one row per citation
`^[Lnn]`, `^[slug.md:Lnn]` or a range:

    | # | where | your sentence, up to its citation | line | its opening words | cues in the line | who says it | holds? |

Code fills the first six. **The cues are code's, and only reminders:** a line that opens with
`Das Protokoll`, `Das Audit`, `Laut …`, `gemäß …` or carries `argumentiert`, `postuliert`,
`konstatiert` reports another source; a sentence that says something is `open`, `undefined` or
`missing` should be asked of `read.py --count` first. Both patterns come from the defects the
lab found, not from a theory of German.

The reader fills two cells per row:

- **who says it** — `document` when the line states it itself, or `source: <who>` when the line
  reports another source (a framework, a person, another document). If the line reports a
  source, the sentence must say so.
- **holds?** — `yes`, or `fixed` when the sentence had to change (the row's `where` and line stay).

`check` fails when the saved `claims.md` lacks a row the note now has, keeps one it no longer
has, leaves a cell empty or unfilled, or writes a value that is not one of the four above.
It prints, without failing, each row whose line has a reporting cue and whose speaker is
`document` — the case R3 got wrong five times. Standard library only.
"""

from __future__ import annotations

import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

RUNS = ROOT / "Plan" / "runs"
CITE = re.compile(r"\^\[(?:(?P<slug>[a-z0-9-]+)\.md:)?L(?P<n>\d+)(?:[–-]L?(?P<m>\d+))?\]")
CENSUS_SECTIONS = ("## Stance, read per passage", "## What the extraction ran into")
FILL = "<fill>"
HEAD = "| # | where | your sentence, up to its citation | line | its opening words | cues in the line | who says it | holds? |"
RULE = "|---|---|---|---|---|---|---|---|"

# a line that reports another source: its subject, or its verb
REPORTS = re.compile(
    r"\b(?:Das|Der|Die)\s+(?:Dokument|Protokoll|Audit|Modell|Konzept|Framework|Bericht|Text|Autor|Autoren|"
    r"Studie|Analyse|Architekturdokument|Manifest|Papier)\b"
    r"|\b(?:laut|gemäß|zufolge|nach\s+[A-ZÄÖÜ]\w+|so\s+[A-ZÄÖÜ]\w+|wie\s+[A-ZÄÖÜ]\w+\s+(?:sagt|beschreibt))\b"
    r"|\b(?:argumentiert|postuliert|behauptet|konstatiert|betont|verweist|zitiert|definiert|bezeichnet|nennt)\b",
    re.I)
OPEN = re.compile(r"\b(?:open|undefined|missing|unnamed|unresolved|nowhere|never|no definition|not defined|absent|"
                  r"leaves? (?:it |this )?(?:open|unsaid|undefined))\b", re.I)
SPEAKERS = re.compile(r"^(?:document|source:\s*\S.*)$")


def sentence_before(paragraph: str, end: int, floor: int) -> str:
    """The text from the last sentence boundary (or `floor`) to `end`: the sentence the citation closes."""
    text = paragraph[floor:end]
    cut = max((m.end() for m in re.finditer(r"(?<=[.!?…])\s+(?=[A-ZÄÖÜ„*])|\n", text)), default=0)
    sentence = " ".join(text[cut:].split())
    return sentence if len(sentence) <= 150 else "…" + sentence[-149:]


def opening(line: str, words: int = 8) -> str:
    return " ".join(line.split()[:words])


def rows_from(text: str, where: str, lines) -> list[dict]:
    """One row per citation in `text`; `lines(n)` gives the cited document's file line n."""
    rows = []
    heading = where
    for block in re.split(r"\n\s*\n", text):
        head = re.match(r"#+\s+(.*)", block.strip())
        if head:
            heading = f"{where} — {head.group(1).strip()[:40]}"
            block = block[block.index("\n") + 1:] if "\n" in block else ""
        floor = 0
        for m in CITE.finditer(block):
            n = int(m.group("n"))
            line = lines(n)
            claim = sentence_before(block, m.start(), floor)
            floor = m.end()
            cues = sorted({c.group(0).strip() for c in REPORTS.finditer(line)})
            note = "ASK read.py --count: says something is open" if OPEN.search(claim) else ""
            rows.append({"where": heading, "claim": claim, "line": n, "opening": opening(line),
                         "cues": ", ".join(cues[:4]) + (("; " if cues and note else "") + note)})
    return rows


def cell(text: str) -> str:
    return text.replace("|", "\\|").replace("\n", " ")


def draft_text(rows: list[dict]) -> str:
    out = [f"# Claims — every cited sentence beside its line", "",
           "Fill the last two columns of every row and save the file as `claims.md` beside this one. "
           "`python3 scripts/claims.py check <slug>` fails on an empty cell. Read the lines: "
           "`python3 scripts/read.py <slug> --from N --to N`, several in one call.", "",
           "- **who says it** — `document`, or `source: <who>` when the line reports another source;",
           "- **holds?** — `yes`, or `fixed` after you changed the sentence.", "", HEAD, RULE]
    for i, r in enumerate(rows, 1):
        out.append(f"| {i} | {cell(r['where'])} | {cell(r['claim'])} | L{r['line']} | {cell(r['opening'])} | "
                   f"{cell(r['cues'])} | {FILL} | {FILL} |")
    return "\n".join(out) + "\n"


def section(text: str, heading: str) -> str:
    start = text.find(heading + "\n")
    if start < 0:
        return ""
    end = text.find("\n## ", start + len(heading))
    return text[start:end if end >= 0 else len(text)]


def source_rows(slug: str, root: Path = ROOT) -> list[dict]:
    """The rows of the note and of the census's two hand-written sections."""
    from subject import document
    doc = document(slug)
    frontier = doc.offset + len(doc.lines()) - 1

    def lines(n: int) -> str:
        if n < doc.offset:
            return doc.path.read_text(encoding="utf-8").split("\n")[n - 1] if n >= 1 else ""
        return doc.lines()[n - doc.offset] if n <= frontier else ""

    note = (root / "Sources" / "notes" / f"{slug}.md").read_text(encoding="utf-8")
    body = note.split("\n---\n", 1)[1] if note.startswith("---") else note
    rows = rows_from(body, "note", lines)
    census = (root / "Sources" / "terms" / f"{slug}.md").read_text(encoding="utf-8")
    for heading in CENSUS_SECTIONS:
        rows += rows_from(section(census, heading), "census", lines)
    return rows


def key(row: dict) -> tuple[str, int]:
    return (row["where"].split(" — ")[0], row["line"])


def parse_saved(text: str) -> list[dict]:
    """The saved table's rows; a cell's escaped pipe is read back."""
    rows = []
    for raw in text.split("\n"):
        if not raw.startswith("| ") or raw.startswith("| #") or raw.startswith("|---"):
            continue
        cells = [c.strip().replace("\\|", "|") for c in re.split(r"(?<!\\)\|", raw.strip().strip("|"))]
        if len(cells) != 8:
            rows.append({"bad": raw})
            continue
        n, where, claim, line, opening_, cues, speaker, holds = cells
        rows.append({"n": n, "where": where, "claim": claim, "line": int(line.lstrip("L")) if line.lstrip("L").isdigit() else -1,
                     "opening": opening_, "cues": cues, "speaker": speaker, "holds": holds})
    return rows


def check_rows(want: list[dict], saved: list[dict]) -> tuple[list[str], list[str]]:
    """(failures, cautions): what fails the table, and what a reviewer should look at."""
    fails, cautions = [], []
    if any("bad" in r for r in saved):
        fails.append(f"{sum('bad' in r for r in saved)} rows do not have the eight columns")
        saved = [r for r in saved if "bad" not in r]
    have, need = {}, {}
    for r in saved:
        have.setdefault((r["where"].split(" — ")[0], r["line"]), []).append(r)
    for r in want:
        need.setdefault(key(r), []).append(r)
    for k, rows in need.items():
        missing = len(rows) - len(have.get(k, []))
        if missing > 0:
            fails.append(f"{missing} row(s) missing for {k[0]} L{k[1]}")
    for k, rows in have.items():
        extra = len(rows) - len(need.get(k, []))
        if extra > 0:
            fails.append(f"{extra} row(s) for {k[0]} L{k[1]} that the note no longer has")
    for r in saved:
        where = f"{r['where'].split(' — ')[0]} L{r['line']}"
        if FILL in (r["speaker"], r["holds"]) or not r["speaker"] or not r["holds"]:
            fails.append(f"{where}: a cell is empty or still {FILL}")
            continue
        if not SPEAKERS.match(r["speaker"]):
            fails.append(f"{where}: who says it is `document` or `source: <who>`, not `{r['speaker'][:30]}`")
        if r["holds"] not in ("yes", "fixed"):
            fails.append(f"{where}: holds? is `yes` or `fixed`, not `{r['holds'][:30]}`")
        if r["speaker"] == "document" and REPORTS.search(r["cues"]):
            cautions.append(f"{where}: the line has a reporting cue ({r['cues'][:50]}) and the speaker is `document`")
    return fails, cautions


def cmd_show(slug: str, width: int = 700) -> str:
    """What a reviewer reads: each sentence with the whole line it cites, no columns to fill."""
    from subject import document
    doc = document(slug)
    out = []
    for i, r in enumerate(source_rows(slug), 1):
        n = r["line"]
        whole = doc.lines()[n - doc.offset] if doc.offset <= n < doc.offset + len(doc.lines()) else ""
        out.append(f"[{i}] {r['where']}  L{n}" + (f"   ({r['cues']})" if r["cues"] else "")
                   + f"\n  SAYS  {r['claim']}\n  LINE  {' '.join(whole.split())[:width]}\n")
    return "\n".join(out)


def cmd_draft(slug: str) -> Path:
    rows = source_rows(slug)
    out = RUNS / slug / "claims-draft.md"
    out.write_text(draft_text(rows), encoding="utf-8")
    return out


def cmd_check(slug: str) -> int:
    saved = RUNS / slug / "claims.md"
    if not saved.exists():
        print(f"claims {slug}: no {saved.relative_to(ROOT)} — run `claims.py draft {slug}`, fill it, save it there")
        return 1
    fails, cautions = check_rows(source_rows(slug), parse_saved(saved.read_text(encoding="utf-8")))
    for c in cautions:
        print(f"  look   {c}")
    for f in fails:
        print(f"  FAIL   {f}")
    n = len(parse_saved(saved.read_text(encoding="utf-8")))
    print(f"claims {slug}: " + (f"holds ({n} rows, {len(cautions)} to look at)" if not fails else f"{len(fails)} failures"))
    return 1 if fails else 0


def selftest() -> int:
    cases = []
    src = {12: "Das Protokoll argumentiert, dass dieser Moment der Stille keinen Mangel darstellt.",
           30: "Der Kern ist die Domäne der reversiblen Berechnungen.", 41: "Die Zeit hat eine Richtung."}
    lines = lambda n: src.get(n, "")  # noqa: E731
    text = ("## 1 · Stille\n\nThe audit says silence is intact: „Das Protokoll argumentiert“ ^[L12]. "
            "The kernel is described as „die Domäne der reversiblen Berechnungen“ ^[L30] and time has a direction ^[L41–L42].\n\n"
            "Nothing about the index is defined, it stays open ^[L30].\n")
    rows = rows_from(text, "note", lines)
    cases.append(("one row per citation, a range at its first line", [r["line"] for r in rows] == [12, 30, 41, 30]))
    cases.append(("a sentence starts after the previous citation", rows[1]["claim"].startswith("The kernel is described")))
    cases.append(("the line's opening words are code's", rows[0]["opening"] == "Das Protokoll argumentiert, dass dieser Moment der Stille"))
    cases.append(("a reporting cue is shown", "Das Protokoll" in rows[0]["cues"] and "argumentiert" in rows[0]["cues"]))
    cases.append(("an open claim is flagged for a count", "ASK read.py --count" in rows[3]["cues"]))
    cases.append(("a line with no cue shows none", rows[1]["cues"] == ""))
    cases.append(("the heading is where the row stands", rows[0]["where"] == "note — 1 · Stille"))
    saved = parse_saved(draft_text(rows))
    fails, _ = check_rows(rows, saved)
    cases.append(("an unfilled table fails, once per row", len(fails) == 4 and all("empty or still" in f for f in fails)))
    for r in saved:
        r["speaker"], r["holds"] = "document", "yes"
    saved[0]["speaker"] = "source: the Protokoll"
    fails, cautions = check_rows(rows, saved)
    cases.append(("a filled table holds", fails == [] and cautions == []))
    saved[1]["speaker"] = "document"
    saved[0]["speaker"] = "document"
    fails, cautions = check_rows(rows, saved)
    cases.append(("a reporting line credited to the document is cautioned, not failed", fails == [] and len(cautions) == 1))
    fails, _ = check_rows(rows, saved[:-1])
    cases.append(("a dropped row fails", any("missing" in f for f in fails)))
    fails, _ = check_rows(rows[:-1], saved)
    cases.append(("a row the note no longer has fails", any("no longer has" in f for f in fails)))
    saved[2]["holds"] = "probably"
    fails, _ = check_rows(rows, saved)
    cases.append(("a value that is not yes or fixed fails", any("holds?" in f for f in fails)))
    saved[2]["holds"], saved[3]["speaker"] = "yes", "the audit"
    fails, _ = check_rows(rows, saved)
    cases.append(("a speaker that is not document or source: fails", any("who says it" in f for f in fails)))
    real = source_rows("ki-narrative-kollaps-kohaerenz-paradoxie")
    cases.append(("a real note yields a row per citation", len(real) >= 15 and all(r["opening"] for r in real if r["line"] > 0)))
    failed = [n for n, ok in cases if not ok]
    print(f"claims: {len(cases) - len(failed)} of {len(cases)} cases hold"
          + (" — FAILED: " + ", ".join(failed) if failed else ""))
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        return selftest()
    if argv[:1] == ["draft"] and len(argv) == 2:
        print(f"wrote {cmd_draft(argv[1]).relative_to(ROOT)} — fill the last two columns, save it as "
              f"Plan/runs/{argv[1]}/claims.md")
        return 0
    if argv[:1] == ["check"] and len(argv) == 2:
        return cmd_check(argv[1])
    if argv[:1] == ["show"] and len(argv) == 2:
        print(cmd_show(argv[1]))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
