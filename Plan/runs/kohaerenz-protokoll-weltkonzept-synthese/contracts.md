# Contracts on `kohaerenz-protokoll-weltkonzept-synthese`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

3 runs of 3 contracts: 3 yielded; $0.90.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `AliasPairs` | `aliaspairs-haiku-2026-09-30` | haiku | yielded | 47 | 32 | 1 ambiguous quote: choose its passage, 3 quote not placed, 11 surface absent from document | — | $0.291 |
| `TermContrasts` | `termcontrasts-haiku-2026-09-30` | haiku | yielded | 84 | 62 | 5 joined or shortened quote, 9 quote not placed, 8 surface absent from document | — | $0.315 |
| `TermDefinitions` | `termdefinitions-haiku-2026-09-30` | haiku | yielded | 92 | 90 | 2 quote not placed | — | $0.295 |

**Never run on this source:** `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `CausalLinks`, `ChapterBeats`, `ChapterCards`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
