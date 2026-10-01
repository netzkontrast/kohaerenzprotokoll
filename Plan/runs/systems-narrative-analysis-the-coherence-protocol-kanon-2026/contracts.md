# Contracts on `systems-narrative-analysis-the-coherence-protocol-kanon-2026`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

3 runs of 3 contracts: 3 yielded; $0.29.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `CausalLinks` | `causallinks-haiku-2026-09-30` | haiku | yielded | 34 | 7 | 16 quote not placed, 11 surface absent from document | — | $0.101 |
| `TermContrasts` | `termcontrasts-haiku-2026-09-30` | haiku | yielded | 26 | 24 | 2 surface absent from document | — | $0.096 |
| `TermDefinitions` | `termdefinitions-haiku-2026-09-30` | haiku | yielded | 43 | 39 | 3 quote not placed, 1 surface absent from document | — | $0.095 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `ChapterBeats`, `ChapterCards`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
