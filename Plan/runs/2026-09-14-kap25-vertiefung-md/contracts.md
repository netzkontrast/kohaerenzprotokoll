# Contracts on `2026-09-14-kap25-vertiefung-md`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

32 runs of 32 contracts: 28 yielded, 1 refused, 1 found nothing, 2 not staged; $5.09.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `AliasPairs` | `aliaspairs-sonnet-2026-10-01` | sonnet | yielded | 8 | 8 | — | 8 | $0.156 |
| `Analogies` | `analogies-sonnet-2026-10-01` | sonnet | found nothing | 0 | 0 | — | 8 | $0.114 |
| `Anchors` | `anchors-sonnet-2026-10-01` | sonnet | yielded | 10 | 7 | 2 quote not placed, 1 surface absent from document | 8 | $0.158 |
| `Attributions` | `attributions-sonnet-2026-10-01` | sonnet | yielded | 6 | 3 | 3 quote not placed | 8 | $0.132 |
| `CardFields` | `cardfields-sonnet-2026-10-01` | sonnet | yielded | 1 | 1 | — | 8 | $0.141 |
| `CastRoles` | `castroles-sonnet-2026-10-01` | sonnet | yielded | 2 | 2 | — | 8 | $0.136 |
| `CausalLinks` | `causallinks-sonnet-2026-10-01` | sonnet | yielded | 2 | 2 | — | 8 | $0.149 |
| `ChapterBeats` | `chapterbeats-sonnet-2026-10-01` | sonnet | yielded | 23 | 21 | 2 quote not placed | 8 | $0.193 |
| `ChapterCards` | `chaptercards-sonnet-2026-10-01` | sonnet | yielded | 6 | 6 | — | 8 | $0.162 |
| `DiegeticTerms` | `diegeticterms-sonnet-2026-10-01` | sonnet | refused | 1 | 0 | 1 quote not placed | 8 | $0.129 |
| `EntityFacts` | `entityfacts-sonnet-2026-10-01` | sonnet | yielded | 17 | 14 | 3 surface absent from document | 8 | $0.191 |
| `Knowledge` | `knowledge-sonnet-2026-10-01` | sonnet | yielded | 3 | 1 | 2 quote not placed | 8 | $0.130 |
| `LocationRegistry` | `locationregistry-sonnet-2026-10-01` | sonnet | not staged | 12 | 0 | — | 8 | $0.133 |
| `Locks` | `locks-sonnet-2026-10-01` | sonnet | yielded | 1 | 1 | — | 8 | $0.114 |
| `OpenPoints` | `openpoints-sonnet-2026-10-01` | sonnet | yielded | 7 | 7 | — | 8 | $0.118 |
| `Pitch` | `pitch-sonnet-2026-10-01` | sonnet | yielded | 1 | 1 | — | 8 | $0.109 |
| `Precedence` | `precedence-sonnet-2026-10-01` | sonnet | yielded | 2 | 2 | — | 8 | $0.134 |
| `ProseRules` | `proserules-sonnet-2026-10-01` | sonnet | yielded | 17 | 11 | 1 quote not placed, 5 surface absent from document | 8 | $0.171 |
| `Quantities` | `quantities-sonnet-2026-10-01` | sonnet | yielded | 39 | 30 | 1 ambiguous quote: choose its passage, 1 quote not placed, 7 surface absent from document | 8 | $0.200 |
| `RelationReadings` | `relationreadings-sonnet-2026-10-01` | sonnet | yielded | 97 | 85 | 3 joined or shortened quote, 3 quote not placed, 6 surface absent from document | 8 | $0.300 |
| `Rules` | `rules-sonnet-2026-10-01` | sonnet | yielded | 8 | 5 | 3 quote not placed | 8 | $0.150 |
| `StandingClaims` | `standingclaims-sonnet-2026-10-01` | sonnet | yielded | 7 | 5 | 2 joined or shortened quote | 8 | $0.148 |
| `StatedRelations` | `statedrelations-sonnet-2026-10-01` | sonnet | yielded | 27 | 19 | 5 joined or shortened quote, 3 quote not placed | 8 | $0.238 |
| `Storypoints` | `storypoints-sonnet-2026-10-01` | sonnet | yielded | 3 | 3 | — | 8 | $0.125 |
| `StructureBeats` | `structurebeats-sonnet-2026-10-01` | sonnet | yielded | 7 | 7 | — | 8 | $0.155 |
| `TermCensus` | `termcensus-sonnet-2026-10-01` | sonnet | not staged | 122 | 0 | — | 8 | $0.223 |
| `TermContrasts` | `termcontrasts-sonnet-2026-10-01` | sonnet | yielded | 9 | 7 | 1 quote not placed, 1 surface absent from document | 8 | $0.167 |
| `TermDefinitions` | `termdefinitions-sonnet-2026-10-01` | sonnet | yielded | 11 | 11 | — | 8 | $0.162 |
| `TermReadings` | `termreadings-sonnet-2026-10-01` | sonnet | yielded | 70 | 65 | 2 joined or shortened quote, 2 quote not placed, 1 surface absent from document | 8 | $0.228 |
| `TermTaxonomy` | `termtaxonomy-sonnet-2026-10-01` | sonnet | yielded | 7 | 7 | — | 8 | $0.144 |
| `ThemeMotifs` | `thememotifs-sonnet-2026-10-01` | sonnet | yielded | 3 | 2 | 1 quote not placed | 8 | $0.134 |
| `Utterances` | `utterances-sonnet-2026-10-01` | sonnet | yielded | 6 | 5 | 1 ambiguous quote: choose its passage | 8 | $0.148 |
