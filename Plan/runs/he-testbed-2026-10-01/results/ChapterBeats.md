# ChapterBeats — the testbed's results

> ChapterBeats — what a document says happens in a numbered chapter, with the participants, each with that sentence.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: decision 013: the chapter is a unit beside the term, and 98 chapter mentions in read documents still have no reading on their
> chapter's page; 218 plot-outline documents are unread. The mechanical NAMES_CHAPTER relation says a line names a chapter,
> not what happens there or who takes part.
> measured against: the readings on the chapter pages (`Wiki/chapters/kap-NN.md`); a beat whose chapter is a page of the wiki is the attachable subset. A quote is placed by read.py --find (P26).
> may not: write a chapter reading, decide what a chapter is about, or reconcile two plans' chapters — a beat is a P_HE_BEAT candidate for a reader
> retire when: on three plot-outline documents a person keeps no beat beyond what the chapter pages already quote

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/chapterbeats-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0498, 17.2 s. **1 rows**: 1 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Kapitel 39 | Kael spürt, dass die Aufmerksamkeit schwindet | event | hedges | In Kapitel 39 müssen wir beschreiben, wie Kael spürt, dass die Aufmerksamkeit schwindet. | 48 |

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
