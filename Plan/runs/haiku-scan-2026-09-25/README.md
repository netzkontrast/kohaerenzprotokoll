# Ten unread documents, one Haiku reader each — 2026-09-25

The author asked for this on 2026-09-25: „Read current Wiki and Search with qmd in the sources
and start 10 Haiku subagents with each 1 documents in sources your Search Marks as
interessant“.

**These are triage scans, not readings.** No census, no `03-candidates.md`, no
note, no reconciliation. A scan says what one document says about the wiki's open
records and suggests whether it should be read in full next. Nothing here is gold
(decision 009), and no scan decides a conflict.

## How the ten were chosen

The qmd index was empty in the fresh container. `qmd update` built the BM25 index
in 12 s; there are no embeddings, so only `qmd search` was used. There were 18
searches, one per open record (C7, C8, C10–C15, Q5, the Erasure-Pol, Sophia, Kap 40,
Mosaik-Herz, Ursprungs-Ich, Wir-AEGIS-plural, KW3, KW2, Alex), each written in
German against `sources` with `-n 25`. Each hit on a landed document with no note
added its score to that document. The ten highest were taken as they came.

**The ranking places a document to look at. It measures nothing.** Short documents
and early chunks score well under BM25 (the `qmd` skill), so this is a list of
places to look.

| score | document | date | lines | verdict |
|--:|---|---|--:|---|
| 8.31 | `worldbuilding-konzept-kohaerenzprotokoll-md` | 2026-05-08 | 968 | READ NEXT |
| 3.38 | `kap0-kap40-doppelklammer-abhandlung-2026-05-08-md` | 2026-05-08 | 616 | READ NEXT |
| 3.30 | `kap0-v1-annotiert-md` | 2026-05-17 | 1237 | READ NEXT |
| 3.22 | `charakter-kompilation-fuer-kohaerenz-protokoll` | 2026-03-31 | 356 | READ NEXT |
| 3.17 | `kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md` | 2026-06-10 | 831 | READ NEXT |
| 2.51 | `the-sensory-rulebook-the-body-as-a-measuring-device-in-the-p` | 2025-11-03 | 111 | READ NEXT |
| 2.33 | `roman-konzept-dualitaet-kohaerenz-spannung` | 2026-02-26 | 170 | READ NEXT |
| 2.32 | `three-mode-architecture-39-chapters-md` | 2026-05-08 | 646 | READ NEXT |
| 2.18 | `an-inquiry-into-the-unresolved-questions-and-thematic-tensio` | 2025-10-15 | 1813 | READ NEXT |
| 1.75 | `ki-prompt-analyse-hard-problem-of-consciousness` | 2026-04-28 | 437 | READ LATER |

**The verdict does not separate the documents.** Nine readers of ten said READ
NEXT, so for choosing a document the column says nothing. What a scan's sections
say is more useful: which records a document takes a position on, and with which
line.

## What the readers got wrong, measured

The brief required every line number to come from `read.py --find`, and every
reader reported that it had done so. The raw scans are commit `1bef2e0`. After
their quotation marks were normalised, **44 of the 152 quotations the checker could
find did not resolve to the line they cited (29 %)**. Some of those failures come
from the normalising itself, where ASCII quotes were nested inside quotes. Checking
by hand found every kind of defect `quotes.py` exists to name:

- **a wrong word:** „erkannt“ for „erkennbar“, and „reiner Funktionalismus“ for „ein
  perfekter Funktionalist“;
- **shifted lines:** one scan's line numbers ran 20 lines short all the way through;
- **a line past the end of the document** (L642 in a 638-line file);
- **a sentence the document does not contain**, stitched together from a list;
- **two lines quoted as one.**

A second pass made each reader rewrite its quotations as `„…“ ^[Lnn]` and run
`quotes.py` until it passed. All ten now resolve. That is **0 unresolved**, and
some quotations are still unchecked because they carry no citation on their line.
**A reader who says it used the tool is not evidence that it did. The check is the
evidence.**

Readers also broke the rule against settling conflicts: „settles C6, C9, C12“, and
„Juna appears here in Kapitel 0, not in Kap 38“, which is C7 decided from one
line that calls itself a „Doppel-Lesart“. The second pass removed these. They are
the reason a scan feeds only a person's reading and never a record.

## What came of it

Page writers used the scans to find terms the wiki has no page for. The writers
worked from `PAGES-BRIEF.md` and drew every quotation from the document itself,
never from a scan. The pages this run created are listed in `CLAUDE.md` under
*State*, and `NOW.md` records the positions on open records that the scans found.
