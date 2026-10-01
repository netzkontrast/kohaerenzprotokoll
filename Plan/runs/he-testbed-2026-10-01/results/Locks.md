# Locks — the testbed's results

> Locks — a decision a source records as fixed, with its date and the sentence.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: GOAL.md 4.2's claim schema (`lock: {locked, date, source}`) and the rules table (each with a lock date): the sources say which decisions were fixed on which day, and
> the record C11 on heat and ozone shows the risk of applying one. The censuses note locks by hand.
> measured against: the wiki's conflict and question records that carry a dated decision; a record whose subject and date stand inside its quote is the precise subset. A quote is placed by read.py --find (P26).
> may not: treat a source's lock as the author's decision — the author's decisions are the records with status decided (writing-skills rule 2) — or say a lock holds; a lock here is a P_HE_LOCK claim about a source
> retire when: on three documents a person keeps no lock beyond what the records already carry

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/locks-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

Not run yet.

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
