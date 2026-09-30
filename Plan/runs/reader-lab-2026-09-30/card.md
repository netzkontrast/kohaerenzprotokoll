# Reader card — steps 1–4 of `ingest`, on one page

A lab artifact, 2026-09-30. It is not a rule of the repository until the lab shows that a
reader holding only this card and the briefing writes a census and a note as good as one
that read the ingest skill and its references in full. The rules here are the skill's own,
shortened. Where they differ, the skill wins.

## What you may read and write

- **Read:** this card, `Plan/briefings/extract.md` (procedural knowledge about German Drive
  exports — read it before the document), the document through `read.py`, and your own
  run folder `Plan/runs/<slug>/`. Nothing else: never `Wiki/`, another document's files,
  `NOW.md`, the ingest skill, or any script's source. What a tool does is below.
- **Write:** `Plan/runs/<slug>/03-candidates.md` (only if there is none), `05-verify.txt`,
  `Sources/terms/<slug>.md`, `Sources/notes/<slug>.md`. Never run `git`, `reconcile.py`,
  `wiki_index.py`, `link.py` or `readings.py`.
- **A `03-candidates.md` that exists is frozen.** It was written while reading and counted;
  never change it.

**Before your first quotation, read `.agents/skills/reader-tools/references/failures.md`**: the failures measured in this repository, the check that catches each, and what to write instead.

## The tools, and what each answers

```bash
python3 scripts/read.py <slug> [--from N --to M]   # the document, each line prefixed NNN| (file lines)
python3 scripts/read.py <slug> --find "<words>"    # ^[Lnn] for words that stand on a line, or the nearest lines
python3 scripts/read.py <slug> --count "<words>"   # three counts and a paste-ready count mark ^[slug.md:#N]
python3 scripts/capture.py <slug> --count          # counts every candidate of 03 into 04-counts.txt, counts.json
python3 scripts/census.py draft <slug>             # the census with everything mechanical already written
python3 scripts/census.py check <slug>             # the census against counts.json; must say „holds"
python3 scripts/quotes.py --strict <file>          # every quotation and count mark against its line; ends `strict: PASS` or `strict: FAIL`
python3 scripts/claims.py draft <slug>             # every cited sentence of your note and census beside its line: a table
python3 scripts/claims.py check <slug>             # the table you filled, saved as claims.md; fails on an empty cell
python3 scripts/runlog.py <slug> start|end <phase> # read, list, count, census, note
```

## The census — `Sources/terms/<slug>.md`

`census.py draft <slug>` writes `Plan/runs/<slug>/census-draft.md`. That file already holds:
- the frontmatter;
- the structural profile;
- every candidate row with its counts and count mark;
- the facts the last section must explain.

Fill its two sections marked `<!-- reader: … -->`, delete the marks, and save it as
`Sources/terms/<slug>.md`. Never edit a table row: `census.py check` fails on a changed
number or a dropped row.

- **`## Stance, read per passage`** — how the document speaks, passage by passage, each with
  its lines: plan, report, lock, question, sample text. Use its own labels, quoted with
  `^[Lnn]`. It describes this document only: no other source, no count from elsewhere.
- **`## What the extraction ran into`** — explain every fact the draft lists. A zero is an
  inflection, export damage, or a term the document truly lacks; name which, with
  `read.py --count`. Add what the reading met: export artifacts, repeated labels, a claim
  about the document's own standing. A canon claim is recorded, never applied.

## The note — `Sources/notes/<slug>.md`

What the document says about the terms that matter, quoted. The skeleton:

```markdown
---
source: Sources/drive/<slug>.md
read: "<date>, the whole document (L<first> to L<last>) through read.py with line numbers; <who>"
stance_markers: ["<the document's own labels, verbatim>", …]
stance_marker_count: <how many times they stand — ask read.py --count>
reads_as: "<one line: what kind of text this is, in its own terms>"
---

# Note — <title>

What this document says about the terms that matter in it. Every quotation carries its file line
on the same line of this note; a number about the whole document is a count mark that
`quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a
gap) and the claim rests on the lines or counts it names. <One sentence on its stance.>

## 1 · What kind of text this is, and how it marks itself
## 2 · <a term or subject that matters> …
## <n> · Said two ways, or left open — recorded, not resolved
## <n+1> · Absent, counted
```

**Each bullet is one claim.**
- It holds one quotation „…“ copied from the line `read.py --find` returned, followed by
  `^[Lnn]`. Ask for the line; never type it.
- A claim with no citation is dropped. A structure you can only see is marked
  **Observed:**, with the lines or counts it rests on.
- Quote verbatim and never translate. Never join two passages. Never merge two statements.
- Say nothing about another document. „The only", „the first" and „unlike" compare, so leave
  them out.
- A number about the whole document is a count mark from `read.py --count`, e.g.
  `` `Nutze` ^[<slug>.md:#3] ``. There is no quotation for an absence.

## Before you finish

`census.py check <slug>` holds. `quotes.py --strict` on the census and on the note ends
`strict: PASS`: it fails on an unresolved quotation and on an uncited one, and „0 wrong“ at the end of
its summary line is only the count marks' figure. `claims.py draft <slug>` writes every cited sentence
beside its line; fill the last two columns of each row (`document` or `source: <who>`, and `yes` or
`fixed`), save it as `Plan/runs/<slug>/claims.md`, and `claims.py check <slug>` must say „holds“. `05-verify.txt` holds every number your
prose states, each with the command that produced it.
