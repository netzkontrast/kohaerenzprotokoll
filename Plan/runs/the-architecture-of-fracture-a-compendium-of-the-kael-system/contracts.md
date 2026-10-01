# Contracts on `the-architecture-of-fracture-a-compendium-of-the-kael-system`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

3 runs of 3 contracts: 3 yielded; $0.21.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `CausalLinks` | `causallinks-haiku-2026-09-30` | haiku | yielded | 14 | 8 | 4 quote not placed, 2 surface absent from document | — | $0.068 |
| `TermContrasts` | `termcontrasts-haiku-2026-09-30` | haiku | yielded | 25 | 14 | 10 quote not placed, 1 surface absent from document | — | $0.074 |
| `TermDefinitions` | `termdefinitions-haiku-2026-09-30` | haiku | yielded | 42 | 21 | 18 quote not placed, 3 surface absent from document | — | $0.072 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `ChapterBeats`, `ChapterCards`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
