# Contracts on `systemic-architecture-specification-the-coherence-protocol-w`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

3 runs of 3 contracts: 3 yielded; $0.25.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `CausalLinks` | `causallinks-haiku-2026-09-30` | haiku | yielded | 18 | 8 | 6 quote not placed, 4 surface absent from document | — | $0.081 |
| `TermContrasts` | `termcontrasts-haiku-2026-09-30` | haiku | yielded | 22 | 16 | 6 quote not placed | — | $0.082 |
| `TermDefinitions` | `termdefinitions-haiku-2026-09-30` | haiku | yielded | 55 | 31 | 1 ambiguous quote: choose its passage, 22 quote not placed | — | $0.088 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `ChapterBeats`, `ChapterCards`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
