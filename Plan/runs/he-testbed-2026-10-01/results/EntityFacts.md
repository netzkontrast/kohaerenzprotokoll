# EntityFacts — the testbed's results

> EntityFacts — an established fact about a figure, a place or an object — name, look, age, relation, feature, number — with how firmly the source states it.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the continuity-editor's style sheet (a fielded entry per character and place: appearance, age, relationships, established facts, each with its first occurrence and a
> confidence, stated or inferred) and the copy-editor's word list of coined terms and numbers. Sources are not canon: what they hold is research a continuity check may
> name, never a correction (writing-skills rule 3).
> measured against: the style sheet the pass returns once chapters exist; until then, a fact whose entity resolves to a wiki term or a verified entity is the attachable subset. A quote is placed by read.py --find (P26).
> may not: decide a fact, or say that two sources' facts collide — a collision is read by a person, and a source's fact is never a chapter's; a fact here is a P_HE_FACT proposal
> retire when: on three documents a person keeps no fact beyond what the wiki's pages already quote

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/entityfacts-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0579, 19.8 s. **4 rows**: 4 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | Kael | die Manifestation des Lesers | relationship/stated | asserts | dass Kael die Manifestation des Lesers ist | 13 |
| 2 | relation_reading | candidate | Leser | Beobachter | name_variant/stated | asserts | den Leser (den Beobachter) | 28 |
| 3 | relation_reading | candidate | Juna | diejenige, die Kael die Wahrheit flüstert | relationship/stated | asserts | Juna ist diejenige, die Kael die Wahrheit flüstert. | 39 |
| 4 | relation_reading | candidate | Kael | die Sonde, die der Leser in das Trauma geschickt hat | relationship/claimed | asserts | Kael ist die Sonde, die der Leser in das Trauma geschickt hat. | 42 |

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
