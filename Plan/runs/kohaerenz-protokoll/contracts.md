# Contracts on `kohaerenz-protokoll`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

3 runs of 3 contracts: 3 yielded; $7.45.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `CausalLinks` | `causallinks-haiku-2026-09-30` | haiku | yielded | 603 | 355 | 3 ambiguous quote: choose its passage, 7 joined or shortened quote, 48 quote not placed, 190 surface absent from document | — | $2.533 |
| `TermContrasts` | `termcontrasts-haiku-2026-09-30` | haiku | yielded | 794 | 655 | 1 ambiguous quote: choose its passage, 33 joined or shortened quote, 50 quote not placed, 55 surface absent from document | — | $2.685 |
| `TermDefinitions` | `termdefinitions-haiku-2026-09-30` | haiku | yielded | 224 | 189 | 7 ambiguous quote: choose its passage, 9 joined or shortened quote, 13 quote not placed, 6 surface absent from document | — | $2.234 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `ChapterBeats`, `ChapterCards`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
