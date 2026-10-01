# TermReadings — the testbed's results

> TermReadings — the passages where one document says something about a term.
> provisional — first design, 2026-09-24; never run on the corpus
> derived from: the notes (Sources/notes/<slug>.md), which quote each reading with its line
> measured against: the lines the note for the same document cites. A quote is placed by
> read.py --find (P26), never by the model; a quote it refuses is reported, not repaired.
> may not: write a note, a reading or a page; merge readings — it is a list and never merges
> (P13); or settle a stance for the record — stance is read per passage by a person
> (decision 004), so the model's label only orders what a person reads first
> retire when: for two documents its quotes land on none of the note's cited lines

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/termreadings-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

Not run yet.

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
