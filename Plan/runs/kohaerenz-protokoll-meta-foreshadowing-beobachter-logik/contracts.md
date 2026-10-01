# Contracts on `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

47 runs of 32 contracts: 33 yielded, 2 refused, 11 found nothing, 1 not staged; $2.33.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `AliasPairs` | `aliaspairs-sonnet-2026-10-01` | sonnet | yielded | 3 | 3 | — | 3 | $0.061 |
| `Analogies` | `analogies-haiku-2026-09-30` | haiku | yielded | 2 | 1 | 1 surface absent from document | — | $0.033 |
| `Analogies` | `analogies-sonnet-2026-10-01` | sonnet | refused | 1 | 0 | 1 surface absent from document | 3 | $0.052 |
| `Anchors` | `anchors-haiku-2026-09-30` | haiku | yielded | 14 | 6 | 8 surface absent from document | — | $0.038 |
| `Anchors` | `anchors-sonnet-2026-10-01` | sonnet | found nothing | 0 | 0 | — | 3 | $0.049 |
| `Attributions` | `attributions-haiku-2026-09-30` | haiku | found nothing | 0 | 0 | — | — | $0.032 |
| `Attributions` | `attributions-sonnet-2026-10-01` | sonnet | yielded | 2 | 2 | — | 3 | $0.050 |
| `CardFields` | `cardfields-sonnet-2026-10-01` | sonnet | yielded | 6 | 5 | 1 surface absent from document | 3 | $0.063 |
| `CastRoles` | `castroles-sonnet-2026-10-01` | sonnet | yielded | 6 | 6 | — | 3 | $0.050 |
| `CausalLinks` | `causallinks-haiku-2026-09-30` | haiku | refused | 6 | 0 | 6 surface absent from document | — | $0.035 |
| `CausalLinks` | `causallinks-sonnet-2026-10-01` | sonnet | yielded | 5 | 5 | — | 3 | $0.073 |
| `ChapterBeats` | `chapterbeats-sonnet-2026-10-01` | sonnet | yielded | 1 | 1 | — | 3 | $0.050 |
| `ChapterCards` | `chaptercards-sonnet-2026-10-01` | sonnet | yielded | 1 | 1 | — | 3 | $0.047 |
| `DiegeticTerms` | `diegeticterms-sonnet-2026-10-01` | sonnet | yielded | 1 | 1 | — | 3 | $0.051 |
| `EntityFacts` | `entityfacts-sonnet-2026-10-01` | sonnet | yielded | 4 | 4 | — | 3 | $0.058 |
| `Knowledge` | `knowledge-haiku-2026-09-30` | haiku | yielded | 12 | 2 | 10 surface absent from document | — | $0.037 |
| `Knowledge` | `knowledge-sonnet-2026-10-01` | sonnet | yielded | 6 | 6 | — | 3 | $0.072 |
| `LocationRegistry` | `locationregistry-sonnet-2026-10-01` | sonnet | found nothing | 0 | 0 | — | 3 | $0.040 |
| `Locks` | `locks-sonnet-2026-10-01` | sonnet | found nothing | 0 | 0 | — | 3 | $0.038 |
| `OpenPoints` | `openpoints-haiku-2026-09-30` | haiku | yielded | 3 | 3 | — | — | $0.032 |
| `OpenPoints` | `openpoints-sonnet-2026-10-01` | sonnet | found nothing | 0 | 0 | — | 3 | $0.040 |
| `Pitch` | `pitch-sonnet-2026-10-01` | sonnet | found nothing | 0 | 0 | — | 3 | $0.043 |
| `Precedence` | `precedence-sonnet-2026-10-01` | sonnet | found nothing | 0 | 0 | — | 3 | $0.047 |
| `ProseRules` | `proserules-sonnet-2026-10-01` | sonnet | yielded | 4 | 4 | — | 3 | $0.066 |
| `Quantities` | `quantities-sonnet-2026-10-01` | sonnet | yielded | 5 | 5 | — | 3 | $0.057 |
| `RelationReadings` | `relationreadings-sonnet-2026-10-01` | sonnet | yielded | 32 | 31 | 1 surface absent from document | 3 | $0.068 |
| `Rules` | `rules-haiku-2026-09-30` | haiku | yielded | 8 | 5 | 3 surface absent from document | — | $0.035 |
| `Rules` | `rules-sonnet-2026-10-01` | sonnet | yielded | 5 | 5 | — | 3 | $0.059 |
| `StandingClaims` | `standingclaims-haiku-2026-09-30` | haiku | found nothing | 0 | 0 | — | — | $0.031 |
| `StandingClaims` | `standingclaims-sonnet-2026-10-01` | sonnet | found nothing | 0 | 0 | — | 3 | $0.040 |
| `StatedRelations` | `statedrelations-sonnet-2026-10-01` | sonnet | yielded | 16 | 16 | — | 3 | $0.084 |
| `Storypoints` | `storypoints-sonnet-2026-10-01` | sonnet | found nothing | 0 | 0 | — | 3 | $0.038 |
| `StructureBeats` | `structurebeats-sonnet-2026-10-01` | sonnet | yielded | 1 | 1 | — | 3 | $0.053 |
| `TermCensus` | `termcensus-sonnet-2026-10-01` | sonnet | not staged | 18 | 0 | — | 3 | $0.059 |
| `TermContrasts` | `termcontrasts-sonnet-2026-10-01` | sonnet | yielded | 4 | 4 | — | 3 | $0.051 |
| `TermDefinitions` | `termdefinitions-sonnet-2026-10-01` | sonnet | yielded | 8 | 8 | — | 3 | $0.065 |
| `TermReadings` | `termreadings-haiku-2026-09-30` | haiku | yielded | 9 | 6 | 3 quote not placed | — | $0.061 |
| `TermReadings` | `termreadings-haiku-2026-09-30b` | haiku | yielded | 17 | 15 | 2 surface absent from document | — | $0.035 |
| `TermReadings` | `termreadings-haiku-2026-09-30c` | haiku | yielded | 19 | 17 | 2 surface absent from document | — | $0.036 |
| `TermReadings` | `termreadings-r1a-haiku-2026-09-30` | haiku | yielded · stale | 14 | 14 | — | — | $0.048 |
| `TermReadings` | `termreadings-r1b-haiku-2026-09-30` | haiku | yielded · stale | 15 | 14 | 1 quote not placed | — | $0.035 |
| `TermReadings` | `termreadings-sonnet-2026-10-01` | sonnet | yielded | 23 | 22 | — | 3 | $0.082 |
| `TermTaxonomy` | `termtaxonomy-haiku-2026-09-30` | haiku | yielded | 8 | 7 | 1 surface absent from document | — | $0.035 |
| `TermTaxonomy` | `termtaxonomy-sonnet-2026-10-01` | sonnet | found nothing | 0 | 0 | — | 3 | $0.050 |
| `ThemeMotifs` | `thememotifs-haiku-2026-09-30` | haiku | yielded | 8 | 4 | 4 surface absent from document | — | $0.036 |
| `ThemeMotifs` | `thememotifs-sonnet-2026-10-01` | sonnet | yielded | 7 | 5 | 2 surface absent from document | 3 | $0.066 |
| `Utterances` | `utterances-sonnet-2026-10-01` | sonnet | yielded | 3 | 3 | — | 3 | $0.053 |
