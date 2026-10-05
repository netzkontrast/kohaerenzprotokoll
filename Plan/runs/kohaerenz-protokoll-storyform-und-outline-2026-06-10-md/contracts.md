# Contracts on `kohaerenz-protokoll-storyform-und-outline-2026-06-10-md`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

4 runs of 4 contracts: 4 yielded; $1.75.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `CausalLinks` | `causallinks-haiku-2026-09-30` | haiku | yielded | 42 | 34 | 1 ambiguous quote: choose its passage, 2 quote not placed, 5 surface absent from document | — | $0.354 |
| `ChapterCards` | `chaptercards-sonnet-2026-10-05b` | sonnet | yielded | 40 | 33 | 1 ambiguous quote: choose its passage, 2 chapter is neither on the quoted line nor the heading above it, 1 joined or shortened quote, 2 quote not placed, 1 surface absent from document | 31 | $0.643 |
| `TermContrasts` | `termcontrasts-haiku-2026-09-30` | haiku | yielded | 140 | 110 | 1 ambiguous quote: choose its passage, 9 joined or shortened quote, 16 quote not placed, 4 surface absent from document | — | $0.400 |
| `TermDefinitions` | `termdefinitions-haiku-2026-09-30` | haiku | yielded | 96 | 84 | 5 ambiguous quote: choose its passage, 7 quote not placed | — | $0.356 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `ChapterBeats`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
