# HyperExtract templates, 2026-09-30

Two pieces of work, both measured with Haiku through `claude -p` (`scripts/he_claude.py`, decision 011):

1. **A template revision** (`TermReadings` r1), measured against the active template on one document, and not promoted.
2. **Thirty-two contracts** (`Plan/hyperextract/*.yaml`, 24 of them new) tried on a pilot of eight documents, then on the
   documents that hold most of the bench's gold. The note is `Plan/concept/graph-contracts_2026-09-30.md`.

| file | what it is |
|---|---|
| `yield.md` | what each contract yielded — `python3 scripts/hegraph.py report` writes it from `Plan/runs/*/hyperextract/` |
| `labels.jsonl` | 261+ rows a reader labelled `ok`, `part` or `wrong` from the quotation and its line — the only measure of precision |
| `trials.sh`, `trial-log.txt` | the pilot: one pass per (document, contract), one at a time |
| `scaled.sh`, `scaled2.sh`, `scaled-log*.txt` | the second pass: `TermDefinitions`, `TermContrasts`, `CausalLinks` over the twelve documents that hold most of the bench's gold lines; `scaled2.sh` is the rest after the first was paused for a readings batch |
| `TermReadings-r1/` | the revision below |

## TermReadings r1 — not promoted

The document is `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik` (58 lines), whose note, by a
Sonnet reader, cites 25 lines. Parent `80f445fb2e07cf45`. r1 names the two failures of the first live pass in the
guidelines:
- a term exactly as its line writes it, inflection included;
- German „…“ copied as they stand.

| run | rows | candidates | refused | lines placed | of the note's 25 | lines the note lacks | calls (failed) | cost |
|---|---|---|---|---|---|---|---|---|
| active, b | 17 | 15 | 2 (surface absent) | 12 | 12 (48 %) | 0 | 3 (0) | $0.035 |
| active, c | 19 | 17 | 2 (surface absent) | 13 | 13 (52 %) | 0 | 3 (0) | $0.036 |
| r1, a | 14 | 14 | 0 | 10 | 10 (40 %) | 0 | 4 (1) | $0.035 |
| r1, b | 15 | 14 | 1 (quote not placed) | 11 | 11 (44 %) | 0 | 3 (0) | $0.035 |

**r1 removes the inflection refusals and covers fewer of the note's lines, so it is kept
here and not promoted.** The active template's two refusals are correct: the stage
refuses a surface the document does not write, and the passage stays for a reader to
see. Two runs a side measure little (P18).

**What HyperExtract adds on this document: nothing the note lacks.** Every line it
placed, in all four runs, is a line the note already cites, and it covered about half of
them. This is the first datapoint of the model comparison the author asked for on
2026-09-30. A second reader on Haiku through a template finds a subset of what a Sonnet
reader found; on longer documents that may differ.

**A second datapoint, from the pilot of the thirty-two contracts** (`yield.md`, the per-document table): on the style
guide, five contracts together find 52 % of the lines the pages cite and 94–100 % of *their* lines are lines a page
cites; on the foreshadowing plan, eleven contracts find 80 %. Each contract is a slice of what a reader chose, not a
superset of it — and for the documents no page cites yet they are a pre-reading.

The runs are in `Plan/runs/kohaerenz-protokoll-meta-foreshadowing-beobachter-logik/hyperextract/`.
The failures behind r1 are also on `.agents/skills/reader-tools/references/failures.md`,
for every reader.
