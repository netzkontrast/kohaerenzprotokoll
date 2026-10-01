# TermTaxonomy — the testbed's results

> TermTaxonomy — what a term is a kind of, a part of, or a member of, each with the sentence that says it.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the graph laboratory's diagnosis (Plan/runs/graph-lab-2026-09-30/diagnose.md): 38 of 96 gold pages are reached and
> outranked, and the outranking pages are hubs of one kind. The stated `[[links]]` are untyped, so a class and its
> members look like any two linked pages.
> measured against: the wiki's own hierarchies where a page lists its members; a pair whose quote holds both names is the precise subset. A quote is placed by read.py --find (P26).
> may not: create a page or a class — a class named here is a P_HE_TAXON endpoint, never a page — or decide that two things belong together
> retire when: on three documents a person keeps no pair beyond what StatedRelations already gives as part_of

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/termtaxonomy-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0503, 16.5 s. **0 rows**: 0 candidates, 0 refused, 0 duplicates.

Staging refused the run: `empty or invalid candidate list: not a successful extraction`

Beside the Haiku pilot of 2026-09-30 on this document: the candidates stand on 0 lines here and 7 there, 0 of them the same.

The model returned no row on this document.

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
