# Questions per chapter, and the unread sources a vector search returns for them — 2026-09-26

The author, in order, the same day:

1. „After vectors Are calculated - Go through all Wiki Pages - espeaciaöly the
   Chapters - and use then qmd vectors (questions Interface) to generate a List of
   candidat sources for each chapter - at least 10 sources per chapter - and put it
   in the Chapters Wiki - as Navigation Information - and add it to the now.md as
   Reading Suggestion Next"
2. „For each chapter First Build a List of questions for each one. Keep dramatica
   and Everything you know about writing a novel in Mind. Especially Everything the
   goal md discribes. ASK more than One question"
3. „Build a few Basic questions every Autor Mist ask for a chapter - and then more
   specialized questions for the chapter"
4. „Fill it with what we know about the Plot - Not Numbers"
5. „Also add what each chapter is about"
6. „Think heros Journey etc"
7. „Also add all the questions and the qmd answers in raw into the Chapters"

**A search places a document to look at. It measures nothing** (the `qmd` skill;
`CLAUDE.md`). Every number below is a count of this run — queries, tables, hits —
and none is a number about the corpus.

## What is here

| file | what |
|---|---|
| `questions-brief.md` | how the questions and summaries were asked for, section by section as the author's requests came |
| `basic-questions.json` | the eight questions every author asks of a chapter — the craft core each chapter's own eight keep |
| `questions/kap-NN.json` | per chapter: `about` (what it is about, placed in the story's structures), `basic` (the eight, filled with its plot), `questions` (10–12 of its own, tagged by GOAL.md §4.5 generator or §5 level) |
| `hits.jsonl` | per chapter: each query's unread documents in rank order, and the fused ranking |
| `raw/kap-NN.json` | per chapter: every query as sent and all forty hits qmd returned for it, snippets included |

The chapter pages carry four navigation sections written from these by
`scripts/chapter_sources.py write`: the summary above the readings, then the
questions, the candidate-source table and the raw answers after them
(`Wiki/chapters/README.md`, *Navigation, around the readings*).

## How the questions were written

By five Claude readers in parallel, one range of chapters each, from the chapter
page, its neighbours and the records it names — never from `Sources/drive/`, so a
question could not be written from the document it would then find. The brief
asked for German, self-contained questions that presuppose no reading (decision
006), with no quotation, citation or link. 463 chapter-specific questions,
10–12 per chapter, every chapter with at least one each of *Konkretheit*,
*Kausalität*, *Leser-Wissen*, *Storyform* and *Struktur*; checked by code for that,
for the chapter it names, and for none of the marks.

**Unique, measured.** No two of the 463 are the same with numbers ignored; a
question's closest other shares a median 21 % of its words, and only two pairs
share half — both asking one real cross-chapter conflict or one GOAL.md pattern
of two different subjects.

The basic eight were first the same template with the chapter's number and titles
filled in. On the author's „Not Numbers", each chapter got its own eight, rewritten
from its readings with who, where, what and what is lost, no chapter number or
date, and asking between the readings where they differ. The summary (`about`)
places each chapter in every structure its readings name — Heldinnenreise and
Heldenreise stages by name, the cycles and their phases, Kishōtenketsu, acts, the
Vortex and its beats, the brackets, Dramatica A and B — naming each source where
they place it differently.

## How the search ran

Each chapter's summary went to qmd as a `hyde:` passage, and each question as a
`vec:` query, one at a time, against `sources`, with `--no-rerank`: vector
similarity only, no expansion model, no reranker. 832 queries, 110 minutes, about
eight seconds each, after the last source document was embedded. Of each query's
forty hits, those on the 24 documents with a census were dropped; a document's rank
for a chapter is reciprocal-rank fusion over its queries, 1 / (10 + rank), so a
document many questions return ranks above one a single question returns first.
Every chapter's table holds twelve; 102 documents stand in at least one.

## What it found

**Five documents are in more than half the tables**, and the tables mark them
*in most chapters*: `monstergruppe-primzahlen-plot-blueprint` (2025-04-26, 27
chapters), `hard-sf-roman-outline-dkt-physik-cosmic-horror` (2026-04-08, 26),
`worldbuilding-konzept-kohaerenzprotokoll-md` (2026-05-08, 25),
`dramatica-storyform-synthese-aegis-analyse-2` (2026-04-30, 24) and
`roman-konzept-dualitaet-kohaerenz-spannung` (2026-02-26, 22). Every chapter's
questions return them, so they say little about any one chapter — and much about
the book, since they are whole-novel plans.

**The unread canon-era documents it placed**, by the chapters whose tables hold
them (`python3 scripts/chapter_sources.py across`):

| document | date | chapters |
|---|---|---|
| `worldbuilding-konzept-kohaerenzprotokoll-md` | 2026-05-08 | 25, among them 0, 1, 4–6 and 31–40 |
| `kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md` | 2026-06-10 | Kap 11, 12, 15, 24, 25, 35–40 |
| `2026-09-14-kap25-vertiefung-md` | 2026-09-14 | Kap 5, 13, 14, 17, 20, 26, 28, 32, 34, 36, 40 |
| `kohaerenz-protokoll-philosophischer-bericht-md` | 2026-05-08 | Kap 3, 6, 7, 17, 24, 32, 35, 36, 38 |
| `dual-storyform-hintergruende-md` | 2026-05-08 | Kap 22, 35, 36, 37, 40 |
| `kp-kap25-2026-09-14-md` | 2026-09-14 | Kap 4, 25, 26, 32 |
| `mining-report-kohaerenz-protokoll-plot-outline-construction` | 2026-05-08 | Kap 35, 36, 37 |
| `systems-narrative-analysis-the-coherence-protocol-kanon-2026` | 2026-05-08 | Kap 34, 35 |
| `systemic-architecture-specification-the-coherence-protocol-w` | 2026-05-08 | Kap 36 |

**What the method cannot find — measured on the one case where the answer is
known.** `koharenz-protokoll-kapitel-0-v2-md`, the clean second draft of Kap 0 that
the grep-backed scan of the same morning found, is in no table of Kap 0. Of Kap 0's
twenty queries not one returned it among its forty hits; it came back for six
queries of other chapters, at best third among their unread documents. The questions and summaries are
written *about* a chapter — its storyform, its structure, its function — and a
draft is the chapter's *prose*, which shares that vocabulary with nothing. So a
table finds plans and analyses of a chapter, not its drafted text. For a draft,
`grep` for the chapter's names and images is the tool.

**The Kap 24 and Kap 29 readings give Storyform B's line as Psychology.** Four
sources write „B: OS-Psychology, Host-System-Verstrickung" for Kap 24 (the
Konzept-Iteration Genesis, the konsolidiertes Konzept, the 39-chapter spec, the
storyform outline); GOAL.md §5.2 has B's OS in Physics and B's RS in Psychology.
Noticed by a reader writing the summaries; the summaries give it as the readings
do, and nothing was changed.

## Rerun

```bash
python3 scripts/chapter_sources.py run      # needs qmd's sources embedded: scripts/setup_qmd.sh --check
python3 scripts/chapter_sources.py write
python3 scripts/chapter_sources.py across
python3 scripts/chapters.py && python3 scripts/quotes.py
```

A document read later drops out of every table on the next run, because a census
removes it from the unread.
