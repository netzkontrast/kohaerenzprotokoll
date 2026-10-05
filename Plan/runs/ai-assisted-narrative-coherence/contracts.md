# Contracts on `ai-assisted-narrative-coherence`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

2 runs of 1 contracts: 2 yielded; $2.18.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `ChapterCards` | `chaptercards-sonnet-2026-10-05b` | sonnet | yielded | 72 | 34 | 2 ambiguous quote: choose its passage, 31 chapter is neither on the quoted line nor the heading above it, 5 surface absent from document | 171 | $2.183 |
| `ChapterCards` | `chaptercards-sonnet-2026-10-05c` |  | yielded | 72 | 55 | 2 ambiguous quote: choose its passage, 10 chapter is neither on the quoted line nor the heading above it, 5 surface absent from document | — | $0.000 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `CausalLinks`, `ChapterBeats`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermContrasts`, `TermDefinitions`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
