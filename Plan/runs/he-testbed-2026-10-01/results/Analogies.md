# Analogies — the testbed's results

> Analogies — a term of the fictional world and the real concept the document says it corresponds to.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the wiki's readings of borrowed concepts (the census's `lens` sections, written by hand for every document) and the
> questions a hard-SF novel keeps asking: which real physics, mathematics or psychology stands behind a fictional name.
> StatedRelations records relations inside the fictional world only and drops a comparison with an outside work.
> measured against: the `lens` lists of the censuses and the borrowed concepts named in the note of the same document; a pair whose quote holds both names is the precise subset. A quote is placed by read.py --find (P26).
> may not: say the fiction is right about the science, or merge a fictional term with a real one; a pair is a P_HE_ANALOGY proposal for a reader
> retire when: on three documents a person keeps no pair beyond the census's own lens list

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/analogies-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0517, 17.0 s. **1 rows**: 0 candidates, 1 refused, 0 duplicates.

Beside the Haiku pilot of 2026-09-30 on this document: the candidates stand on 0 lines here and 1 there, 0 of them the same.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | refused: surface absent from document | Das Zuklappen des Buches | Wärmetod des Universums (Entropie) | metaphor_for | asserts | Das Zuklappen des Buches wird als der „Wärmetod des Universums“ (Entropie) geframt. | 46 |

## `2026-09-14-kap25-vertiefung-md`

8 calls (0 failed), 8 chunks (0 without a valid reply), $0.1136, 28.7 s. **0 rows**: 0 candidates, 0 refused, 0 duplicates.

Staging refused the run: `empty or invalid candidate list: not a successful extraction`

The model returned no row on this document.
