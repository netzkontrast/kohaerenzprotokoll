# Contracts on `dual-storyform-hintergruende-md`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

4 runs of 4 contracts: 4 yielded; $0.83.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `CausalLinks` | `causallinks-haiku-2026-09-30` | haiku | yielded | 48 | 33 | 1 ambiguous quote: choose its passage, 1 quote not placed, 12 surface absent from document | — | $0.205 |
| `Storypoints` | `storypoints-haiku-2026-09-30` | haiku | yielded | 25 | 11 | 2 quote not placed, 12 surface absent from document | — | $0.192 |
| `TermContrasts` | `termcontrasts-haiku-2026-09-30` | haiku | yielded | 96 | 67 | 1 ambiguous quote: choose its passage, 21 quote not placed, 6 surface absent from document | — | $0.229 |
| `TermDefinitions` | `termdefinitions-haiku-2026-09-30` | haiku | yielded | 68 | 59 | 3 ambiguous quote: choose its passage, 4 quote not placed, 2 surface absent from document | — | $0.201 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `ChapterBeats`, `ChapterCards`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `StructureBeats`, `TermCensus`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
