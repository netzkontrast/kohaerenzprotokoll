# TermDefinitions — the testbed's results

> TermDefinitions — the sentence in which a document says what a term is, copied verbatim.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: TermReadings, whose list holds every passage that says something about a term and so
> ranks a definition no higher than a remark. A question of the kind „what is X“ is best answered by the
> sentence that defines X, and a graph edge to that sentence (P_HE_DEFINES) can carry more weight than
> an edge to any mention. The graph laboratory's diagnosis (Plan/runs/graph-lab-2026-09-30/diagnose.md)
> found the misses to be ranking misses: the right pages are reached and outranked.
> measured against: the first reading of each wiki page from a document (`## Reading`), which is
> usually its defining passage; the share of a page's definitions that this list's quotes land on.
> A quote is placed by read.py --find (P26).
> may not: write a note, a reading or a page; decide which document's definition is right — where two
> documents define one term differently that is a conflict, and conflicts are read, never detected
> retire when: for three documents its quotes land on none of the pages' first readings

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/termdefinitions-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

Not run yet.

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
