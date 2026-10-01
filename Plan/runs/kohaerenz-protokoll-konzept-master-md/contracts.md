# Contracts on `kohaerenz-protokoll-konzept-master-md`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

3 runs of 3 contracts: 3 yielded; $1.16.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `CausalLinks` | `causallinks-haiku-2026-09-30` | haiku | yielded | 91 | 61 | 2 ambiguous quote: choose its passage, 10 quote not placed, 18 surface absent from document | — | $0.378 |
| `TermContrasts` | `termcontrasts-haiku-2026-09-30` | haiku | yielded | 164 | 128 | 30 quote not placed, 6 surface absent from document | — | $0.412 |
| `TermDefinitions` | `termdefinitions-haiku-2026-09-30` | haiku | yielded | 147 | 128 | 1 ambiguous quote: choose its passage, 12 quote not placed, 2 surface absent from document | — | $0.373 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `ChapterBeats`, `ChapterCards`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
