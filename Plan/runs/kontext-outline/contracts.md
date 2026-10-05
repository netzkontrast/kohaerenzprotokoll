# Contracts on `kontext-outline`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

2 runs of 1 contracts: 1 yielded, 1 found nothing; $0.95.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `ChapterCards` | `chaptercards-sonnet-2026-10-05` | sonnet | found nothing · stale (template changed, source current) | 0 | 0 | — | 23 | $0.339 |
| `ChapterCards` | `chaptercards-sonnet-2026-10-05b` | sonnet | yielded | 142 | 133 | 6 ambiguous quote: choose its passage, 3 surface absent from document | 23 | $0.615 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `CausalLinks`, `ChapterBeats`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermContrasts`, `TermDefinitions`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
