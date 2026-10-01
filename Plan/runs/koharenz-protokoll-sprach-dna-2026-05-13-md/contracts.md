# Contracts on `koharenz-protokoll-sprach-dna-2026-05-13-md`

Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging admitted, not rows anyone judged right.

5 runs of 5 contracts: 5 yielded; $0.77.

| contract | run | model | outcome | rows | candidates | refused | chunks | cost |
|---|---|---|---|---|---|---|---|---|
| `CardFields` | `cardfields-haiku-2026-09-30` | haiku | yielded | 67 | 39 | 5 quote not placed, 23 surface absent from document | — | $0.163 |
| `DiegeticTerms` | `diegeticterms-haiku-2026-09-30` | haiku | yielded | 5 | 5 | — | — | $0.134 |
| `EntityFacts` | `entityfacts-haiku-2026-09-30` | haiku | yielded | 86 | 60 | 8 ambiguous quote: choose its passage, 10 quote not placed, 8 surface absent from document | — | $0.184 |
| `ProseRules` | `proserules-haiku-2026-09-30` | haiku | yielded | 64 | 50 | 1 ambiguous quote: choose its passage, 6 quote not placed, 7 surface absent from document | — | $0.157 |
| `Utterances` | `utterances-haiku-2026-09-30` | haiku | yielded | 3 | 3 | — | — | $0.130 |

**Never run on this source:** `AliasPairs`, `Analogies`, `Anchors`, `Attributions`, `CastRoles`, `CausalLinks`, `ChapterBeats`, `ChapterCards`, `Knowledge`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `Quantities`, `RelationReadings`, `Rules`, `StandingClaims`, `StatedRelations`, `Storypoints`, `StructureBeats`, `TermCensus`, `TermContrasts`, `TermDefinitions`, `TermReadings`, `TermTaxonomy`, `ThemeMotifs`.
