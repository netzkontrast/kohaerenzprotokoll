# Contracts on `mining-report-kohaerenz-protokoll-narrative-building-blocks`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

3 runs of 3 contracts: 3 yielded; $0.59.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `CausalLinks` | `causallinks-haiku-2026-09-30` | haiku | yielded | 29 | 7 | 14 quote not placed, 8 surface absent from document | — | $0.191 |
| `TermContrasts` | `termcontrasts-haiku-2026-09-30` | haiku | yielded | 42 | 25 | 12 quote not placed, 4 surface absent from document | — | $0.206 |
| `TermDefinitions` | `termdefinitions-haiku-2026-09-30` | haiku | yielded | 70 | 51 | 16 quote not placed, 3 surface absent from document | — | $0.193 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `ChapterBeats`, `ChapterCards`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
