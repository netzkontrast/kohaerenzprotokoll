# Contracts on `dramatica-storyform-synthese-aegis-analyse-2`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

3 runs of 3 contracts: 3 yielded; $1.42.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `CausalLinks` | `causallinks-haiku-2026-09-30` | haiku | yielded | 118 | 75 | 4 quote not placed, 38 surface absent from document | — | $0.476 |
| `TermContrasts` | `termcontrasts-haiku-2026-09-30` | haiku | yielded | 135 | 117 | 1 joined or shortened quote, 9 quote not placed, 8 surface absent from document | — | $0.497 |
| `TermDefinitions` | `termdefinitions-haiku-2026-09-30` | haiku | yielded | 143 | 135 | 2 ambiguous quote: choose its passage, 4 quote not placed | — | $0.451 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `ChapterBeats`, `ChapterCards`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
