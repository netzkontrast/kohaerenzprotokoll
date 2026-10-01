# CastRoles — the testbed's results

> CastRoles — the role or function a document gives a figure of its world, with the sentence.
> provisional — first design, 2026-09-30; never run on the corpus
> derived from: the wiki's character pages and the storyform documents, which assign figures to roles (protagonist, antagonist, guardian of a
> world, a personality part of a system); AliasPairs' trial put such sentences under role_of and mistyped them as aliases.
> measured against: the roles the character pages quote; a figure that resolves to a wiki term is the attachable subset. A quote is placed by read.py --find (P26).
> may not: merge two figures, decide who a figure really is, or say two documents give a figure different roles — that is read
> retire when: on three documents a person keeps no role beyond what the character pages already quote

Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: `Plan/runs/<document>/hyperextract/castroles-sonnet-2026-10-01/`. A row's *status* is staging's (`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed here by `read.locate` where it has one. No row is judged right or wrong.

## `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

3 calls (0 failed), 3 chunks (0 without a valid reply), $0.0496, 15.7 s. **6 rows**: 6 candidates, 0 refused, 0 duplicates.

| # | kind | status | source | target | type | stance | quote | lines |
|---|---|---|---|---|---|---|---|---|
| 1 | relation_reading | candidate | AEGIS | Verwalter | role | asserts | AEGIS agiert nicht als autonomer Gott, sondern als Verwalter | 25 |
| 2 | relation_reading | candidate | AEGIS | autonomer Gott | role | denies | AEGIS agiert nicht als autonomer Gott | 25 |
| 3 | relation_reading | candidate | Kael | die Manifestation des Lesers | role | asserts | dass Kael die Manifestation des Lesers ist | 13 |
| 4 | relation_reading | candidate | Juna | diejenige, die Kael die Wahrheit flüstert | role | asserts | Juna ist diejenige, die Kael die Wahrheit flüstert. | 39 |
| 5 | relation_reading | candidate | Kael | die Sonde, die der Leser in das Trauma geschickt hat | role | asserts | Kael ist die Sonde, die der Leser in das Trauma geschickt hat. | 42 |
| 6 | relation_reading | candidate | Er | das Werkzeug, mit dem der Leser versucht, seine eigene Dissoziation | function | asserts | Er ist das Werkzeug, mit dem der Leser versucht, seine eigene Dissoziation (seine Trennung von der Welt) zu heilen. | 42 |

## `2026-09-14-kap25-vertiefung-md`

Not run yet.
