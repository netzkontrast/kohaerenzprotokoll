# Contracts on `koharenz-protokoll-konzept-konsolidiert-2026-05-08-md`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

3 runs of 3 contracts: 3 yielded; $2.01.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `CausalLinks` | `causallinks-haiku-2026-09-30` | haiku | yielded | 151 | 116 | 8 ambiguous quote: choose its passage, 5 quote not placed, 22 surface absent from document | — | $0.644 |
| `TermContrasts` | `termcontrasts-haiku-2026-09-30` | haiku | yielded | 261 | 186 | 13 ambiguous quote: choose its passage, 1 joined or shortened quote, 51 quote not placed, 8 surface absent from document | — | $0.719 |
| `TermDefinitions` | `termdefinitions-haiku-2026-09-30` | haiku | yielded | 250 | 214 | 12 ambiguous quote: choose its passage, 3 joined or shortened quote, 20 quote not placed | — | $0.650 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `ChapterBeats`, `ChapterCards`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
