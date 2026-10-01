# Contracts on `koharenz-protokoll-strukturierter-outline-2026-05-18-md`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

3 runs of 3 contracts: 3 yielded; $1.45.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `CausalLinks` | `causallinks-haiku-2026-09-30` | haiku | yielded | 52 | 40 | 1 ambiguous quote: choose its passage, 2 quote not placed, 9 surface absent from document | — | $0.462 |
| `TermContrasts` | `termcontrasts-haiku-2026-09-30` | haiku | yielded | 147 | 121 | 9 ambiguous quote: choose its passage, 13 quote not placed, 4 surface absent from document | — | $0.518 |
| `TermDefinitions` | `termdefinitions-haiku-2026-09-30` | haiku | yielded | 164 | 151 | 10 ambiguous quote: choose its passage, 2 quote not placed | — | $0.473 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `ChapterBeats`, `ChapterCards`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
