# Contracts on `kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

2 runs of 2 contracts: 2 yielded; $0.78.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `TermContrasts` | `termcontrasts-haiku-2026-09-30` | haiku | yielded | 148 | 119 | 11 ambiguous quote: choose its passage, 1 joined or shortened quote, 13 quote not placed, 3 surface absent from document | — | $0.405 |
| `TermDefinitions` | `termdefinitions-haiku-2026-09-30` | haiku | yielded | 212 | 174 | 16 ambiguous quote: choose its passage, 2 joined or shortened quote, 11 quote not placed, 3 surface absent from document | — | $0.380 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `CausalLinks`, `ChapterBeats`, `ChapterCards`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
