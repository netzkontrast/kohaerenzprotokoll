# Contracts on `briefing-core-concepts-of-the-kohaerenz-protokoll-project`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

2 runs of 2 contracts: 2 found nothing; $0.23.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `Pitch` | `pitch-haiku-2026-09-30` | haiku | found nothing | 0 | 0 | — | — | $0.113 |
| `StandingClaims` | `standingclaims-haiku-2026-09-30` | haiku | found nothing | 0 | 0 | — | — | $0.113 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CardFields`, `CastRoles`, `CausalLinks`, `ChapterBeats`, `ChapterCards`, `DiegeticTerms`, `EntityFacts`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Precedence`, `ProseRules`, `Quantities`, `RelationReadings`, `Rules`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermContrasts`, `TermDefinitions`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`, `Utterances`.
