# TermContrasts — the testbed's results

> TermContrasts — two terms a document sets against each other or holds in tension, each with that sentence.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the author's reading of 2026-09-30 of a line about a „Große Stille“ and a line about
> „das große Schweigen“ as a tension between silence and stillness, found by a BM25 relation
> (Plan/runs/bm25/) and not by any stated relation; and StatedRelations, whose types are open
> and mostly structural (part_of, controls), so that a contrast the text states is not a type the graph has.
> measured against: the relations a person labels `tension` in Plan/runs/bm25/verdicts.jsonl, and the
> contrast the wiki's conflict and question records already name. A quote is placed by read.py --find (P26).
> may not: detect or state a conflict — CLAUDE.md: conflict detection is never mechanised, and two readings
> are compared by reading them. A contrast inside one document is a P_HE_CONTRAST proposal for a reader,
> not a conflict record, and two documents' contrasts are never compared by a program
> retire when: on three documents a person keeps no contrast beyond what StatedRelations already gives

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/termcontrasts-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

Not run yet.

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
