# HyperExtract templates, 2026-09-30

Two pieces of work, both measured with Haiku through `claude -p` (`scripts/he_claude.py`, decision 011):

1. **A template revision** (`TermReadings` r1), measured against the active template on one document, and not promoted.
2. **Thirty-two contracts** (`Plan/hyperextract/*.yaml`, 27 of them new) tried on a pilot of eight documents, then on the
   documents that hold most of the bench's gold. The note is `Plan/concept/graph-contracts_2026-09-30.md`.

| file | what it is |
|---|---|
| `yield.md` | what each contract yielded — `python3 scripts/hegraph.py report` writes it from `Plan/runs/*/hyperextract/` |
| `labels.jsonl` | 297 rows a reader (the working session) labelled `ok`, `part` or `wrong` from the quotation and its line — the only measure of precision; 261 from the pilot, 36 drawn by hash from the scaled documents (`sample: "scaled documents"`) |
| `trials.sh`, `trial-log.txt` | the pilot: one pass per (document, contract), one at a time |
| `scaled.sh`, `scaled2.sh`, `scaled-log*.txt` | the second pass: `TermDefinitions`, `TermContrasts`, `CausalLinks` over the twelve documents that hold most of the bench's gold lines; `scaled2.sh` is the rest after the first was paused for a readings batch |
| `TermReadings-r1/` | the revision below |

The scaled pass is in the note's §6 (`Plan/concept/graph-contracts_2026-09-30.md`); the retrieval measured on it is in `Plan/runs/graph-lab-2026-09-30/`.

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

## The scaled pass — three contracts, twelve documents

`TermDefinitions`, `TermContrasts` and `CausalLinks` over twelve of the fifteen documents that hold the most of the bench's gold
(493 of its 1,226 lines): **36 runs, 957 calls (21 failed), 82 minutes of model time, $11.68**, one run at a time
(`scaled.sh`, then `scaled2.sh` after a pause for a readings batch). Staged: 2,899 rows on names and 268 on their quotation, 504
refused for good. Twelve rows per contract were labelled, drawn by the hash of the row's id: 21 `ok`, 15 `part`, none `wrong`,
against 28 `ok`, 6 `part` and 1 `wrong` of the same three contracts' 35 pilot rows. What it cost per megabyte corrected the pilot's
estimate from $63 to about $190 a contract for the corpus (§4.5 of the note).

## The cue gate against the ungated run

`gate-ab.sh` ran `CausalLinks` once more ungated and once gated (`he_claude.py run --gate`) on three German documents of the
twelve; `gate-ab.py` compares both with the first ungated run (`gate-ab.md`), `gate-offline.py` asks the same of the cue and its
neighbours with no model (`gate-offline.txt`). **The gate found 26 % of the lines for 29 % of the cost**, where a repeat of the
ungated run finds 88 % of its own first run: a thinning, not a filter (§4.6 of the note). The six runs stand in `gate-ab/`, out of
`Plan/runs/<document>/hyperextract/`, because the store loads every run that stands there and would count a line twice.
