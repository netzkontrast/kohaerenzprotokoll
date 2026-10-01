# Contracts on `kohaerenz-protokoll-philosophischer-bericht-md`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

3 runs of 3 contracts: 3 yielded; $1.27.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `CausalLinks` | `causallinks-haiku-2026-09-30` | haiku | yielded | 115 | 80 | 6 ambiguous quote: choose its passage, 7 quote not placed, 22 surface absent from document | — | $0.416 |
| `TermContrasts` | `termcontrasts-haiku-2026-09-30` | haiku | yielded | 157 | 131 | 6 ambiguous quote: choose its passage, 1 joined or shortened quote, 11 quote not placed, 8 surface absent from document | — | $0.436 |
| `TermDefinitions` | `termdefinitions-haiku-2026-09-30` | haiku | yielded | 178 | 158 | 6 ambiguous quote: choose its passage, 11 quote not placed, 3 surface absent from document | — | $0.415 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `ChapterBeats`, `ChapterCards`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
