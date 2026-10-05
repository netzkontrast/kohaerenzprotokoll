# Contracts on `hard-sf-roman-outline-dkt-physik-cosmic-horror`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

4 runs of 4 contracts: 4 yielded; $1.63.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `CausalLinks` | `causallinks-haiku-2026-09-30` | haiku | yielded | 89 | 53 | 4 quote not placed, 32 surface absent from document | — | $0.335 |
| `ChapterCards` | `chaptercards-sonnet-2026-10-05b` | sonnet | yielded | 88 | 82 | 6 surface absent from document | 26 | $0.622 |
| `TermContrasts` | `termcontrasts-haiku-2026-09-30` | haiku | yielded | 89 | 75 | 8 quote not placed, 6 surface absent from document | — | $0.335 |
| `TermDefinitions` | `termdefinitions-haiku-2026-09-30` | haiku | yielded | 105 | 97 | 2 ambiguous quote: choose its passage, 5 quote not placed, 1 surface absent from document | — | $0.340 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `ChapterBeats`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
