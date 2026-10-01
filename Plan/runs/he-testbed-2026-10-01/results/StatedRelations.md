# StatedRelations — the testbed's results

> StatedRelations — relations one document states in a sentence, each with that sentence.
> provisional — first design, 2026-09-24; never run on the corpus
> derived from: no gold. The wiki's [[links]] mark terms a page names and are untyped, so
> nothing here measures a typed relation. This is a trial that lets the graph tools
> (knowledge-graph-extract, grawiki, graphify) be compared on equal terms.
> may not: become a [[link]] — a link is never inferred (CLAUDE.md) — detect a conflict,
> or supply a count. A relation whose quote read.py --find cannot place is dropped by code.
> retire when: on documents 5 and 6 a person keeps none of its relations as a candidate edge

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/statedrelations-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

Not run yet.

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
