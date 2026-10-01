# TermCensus — the testbed's results

> TermCensus — the terms of one document, as the document writes them.
> provisional — first design, 2026-09-24; never run on the corpus
> derived from: the reader's lists (Plan/runs/<slug>/03-candidates.md) and the entity-lists
> reader prompt (.claude/workflows/entity-lists.js), whose entity kinds it keeps
> may not: seed or replace a reader's 03-candidates.md, create a page, supply a count,
> or merge two surfaces. No field carries a line: names in, lines by code (P26).
> retire when: on documents 5 and 6 it scores below the Haiku entity lists against the
> same gold (entities.py score: F1 0.25 and 0.69)

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/termcensus-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

Not run yet.

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
