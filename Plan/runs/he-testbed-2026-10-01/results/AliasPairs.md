# AliasPairs — the testbed's results

> AliasPairs — two names a document itself puts in one relation of identity or naming, each with that sentence.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the graph laboratory's diagnosis (Plan/runs/graph-lab-2026-09-30/diagnose.md). Of 96 gold
> pages of the wiki's own cases 9 have no seed, because the question names a page under a name no page
> carries; and a search for the lines that share a page's words without writing its names found the
> same thing twice, a name under two names (Plan/runs/bm25/). bilingual.py reaches only the
> parenthetical form `A (B)`; a sentence can equate two names in other ways.
> measured against: the pairs bilingual.py and the pages' `aliases:` already hold; a pair whose two names
> both stand inside its quote is the precise subset. A quote is placed by read.py --find (P26).
> may not: merge two names or two pages — a pair is a P_HE_ALIAS proposal for a reader, never a
> `[[link]]` or an `aliases:` entry (CLAUDE.md: a link is never inferred) — say which name is canonical,
> or supply a count
> retire when: on three documents a person keeps no pair beyond the glosses bilingual.py finds

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/aliaspairs-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0612, 21.2 s. **3 rows**: 3 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Leser | Beobachter | same_as | asserts | den Leser (den Beobachter) | 28 |
| 2 | relation_reading | candidate | Beobachters | Lesers | same_as | asserts | der Verstand des Beobachters (des Lesers) | 35 |
| 3 | relation_reading | candidate | Kael | Sonde | role_of | asserts | Kael ist die Sonde, die der Leser in das Trauma geschickt hat. | 42 |

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
