# Contracts on `kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

4 runs of 4 contracts: 4 yielded; $1.58.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `CausalLinks` | `causallinks-haiku-2026-09-30` | haiku | yielded | 96 | 70 | 1 joined or shortened quote, 6 quote not placed, 19 surface absent from document | — | $0.358 |
| `ChapterCards` | `chaptercards-sonnet-2026-10-05b` | sonnet | yielded | 17 | 15 | 1 quote not placed, 1 surface absent from document | 29 | $0.499 |
| `TermContrasts` | `termcontrasts-haiku-2026-09-30` | haiku | yielded | 156 | 129 | 1 ambiguous quote: choose its passage, 2 joined or shortened quote, 16 quote not placed, 8 surface absent from document | — | $0.384 |
| `TermDefinitions` | `termdefinitions-haiku-2026-09-30` | haiku | yielded | 111 | 98 | 12 quote not placed | — | $0.343 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `ChapterBeats`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
