# Contracts on `detaillierte-kapiteluebersicht`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

6 runs of 6 contracts: 6 yielded; $0.61.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `Anchors` | `anchors-haiku-2026-09-30` | haiku | yielded | 26 | 14 | 12 surface absent from document | — | $0.097 |
| `CastRoles` | `castroles-haiku-2026-09-30` | haiku | yielded | 24 | 15 | 9 surface absent from document | — | $0.094 |
| `ChapterBeats` | `chapterbeats-haiku-2026-09-30` | haiku | yielded | 43 | 32 | 1 quote not placed, 10 surface absent from document | — | $0.103 |
| `ChapterCards` | `chaptercards-haiku-2026-09-30` | haiku | yielded · stale (template changed, source current) | 71 | 36 | 3 quote not placed, 31 surface absent from document | — | $0.118 |
| `Precedence` | `precedence-haiku-2026-09-30` | haiku | yielded | 39 | 33 | 1 quote not placed, 5 surface absent from document | — | $0.101 |
| `StructureBeats` | `structurebeats-haiku-2026-09-30` | haiku | yielded | 29 | 11 | 1 quote not placed, 17 surface absent from document | — | $0.099 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Attributions`, `CardFields`, `CausalLinks`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `TermCensus`, `TermContrasts`, `TermDefinitions`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
