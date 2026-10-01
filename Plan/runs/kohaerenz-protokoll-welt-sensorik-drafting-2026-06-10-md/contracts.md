# Contracts on `kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

3 runs of 3 contracts: 3 yielded; $1.31.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `CausalLinks` | `causallinks-haiku-2026-09-30` | haiku | yielded | 38 | 29 | 3 ambiguous quote: choose its passage, 1 joined or shortened quote, 2 quote not placed, 3 surface absent from document | — | $0.413 |
| `TermContrasts` | `termcontrasts-haiku-2026-09-30` | haiku | yielded | 144 | 115 | 3 ambiguous quote: choose its passage, 21 quote not placed, 5 surface absent from document | — | $0.466 |
| `TermDefinitions` | `termdefinitions-haiku-2026-09-30` | haiku | yielded | 148 | 132 | 5 ambiguous quote: choose its passage, 2 joined or shortened quote, 6 quote not placed, 2 surface absent from document | — | $0.427 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `ChapterBeats`, `ChapterCards`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
