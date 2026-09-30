# What each contract yielded

Per contract, over every run staged in `Plan/runs/*/hyperextract/`. A row enters the store on one of two footings (`hegraph.staged`): **names** — its quotation is placed on one line and every name the model wrote stands in the document — or **quote** — refused only because a slot is the model's own wording (an inflection, a clause, a three-letter name before the gate learned them), while its quotation is placed on one line, so the line is evidence and the code finds the pages in it. `refused` is what stays out: a quotation not placed, on several lines, joined, or an empty reply. Precision is only what a reader labelled (`labels.jsonl`): `ok` the quotation states what the record says, `part` something near it, `wrong` neither.

| contract | documents tried | answered, found nothing | rows: names / quote | refused for good | cost, USD | per row | names: labelled, ok / ok+part | quote: labelled, ok / ok+part | names: every end / one end is a page or entity | pages found in a quotation | lines a page also cites | the pages' cited lines it finds |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| AliasPairs | 1 | 0 | 32 / 11 | 4 (3 quote not placed, 1 ambiguous quote) | 0.29 | 0.007 | 14: 36% / 64% | 1: 100% / 100% | 34% / 75% | 74% |  | |
| Analogies | 2 | 0 | 16 / 2 | 0 | 0.11 | 0.006 | 15: 47% / 80% |  | 0% / 6% | 11% | 13% (2/15) | 10% (2/20) |
| Anchors | 2 | 0 | 20 / 20 | 0 | 0.14 | 0.003 | 10: 20% / 70% | 20: 20% / 70% | 5% / 70% | 80% | 28% (9/32) | 45% (9/20) |
| Attributions | 1 | 1 | 0 / 0 | 0 | 0.03 | 0.032 |  |  | 0% / 0% | 0% |  | |
| CardFields | 1 | 0 | 39 / 23 | 5 (5 quote not placed) | 0.16 | 0.003 | 10: 80% / 100% | 4: 100% / 100% | 10% / 90% | 29% | 100% (16/16) | 31% (16/52) |
| CastRoles | 1 | 0 | 15 / 9 | 0 | 0.09 | 0.004 | 11: 64% / 100% | 1: 0% / 100% | 60% / 93% | 92% |  | |
| CausalLinks | 1 | 0 | 0 / 6 | 0 | 0.03 | 0.006 |  | 6: 83% / 100% | 0% / 0% | 33% | 83% (5/6) | 25% (5/20) |
| ChapterBeats | 1 | 0 | 32 / 10 | 1 (1 quote not placed) | 0.10 | 0.002 | 12: 92% / 100% | 3: 100% / 100% | 16% / 94% | 98% |  | |
| ChapterCards | 1 | 0 | 36 / 31 | 3 (3 quote not placed) | 0.12 | 0.002 | 12: 83% / 100% | 3: 100% / 100% | 14% / 64% | 79% |  | |
| DiegeticTerms | 1 | 0 | 5 / 0 | 0 | 0.13 | 0.027 | 5: 20% / 100% |  | 0% / 60% | 80% | 80% (4/5) | 8% (4/52) |
| EntityFacts | 1 | 0 | 60 / 7 | 19 (10 quote not placed, 8 ambiguous quote) | 0.17 | 0.002 | 10: 90% / 100% |  | 18% / 67% | 55% | 95% (18/19) | 35% (18/52) |
| Knowledge | 1 | 0 | 2 / 10 | 0 | 0.04 | 0.003 | 2: 0% / 100% | 10: 30% / 100% | 50% / 50% | 50% | 91% (10/11) | 50% (10/20) |
| Locks | 1 | 1 | 0 / 0 | 0 | 0.07 | 0.070 |  |  | 0% / 0% | 0% |  | |
| OpenPoints | 1 | 0 | 3 / 0 | 0 | 0.03 | 0.011 | 3: 33% / 67% |  | 0% / 0% | 67% | 67% (2/3) | 10% (2/20) |
| Pitch | 1 | 1 | 0 / 0 | 0 | 0.11 | 0.113 |  |  | 0% / 0% | 0% |  | |
| Precedence | 1 | 0 | 33 / 5 | 1 (1 quote not placed) | 0.10 | 0.003 | 11: 18% / 27% | 1: 0% / 100% | 3% / 30% | 84% |  | |
| ProseRules | 1 | 0 | 50 / 7 | 7 (6 quote not placed, 1 ambiguous quote) | 0.16 | 0.003 | 10: 90% / 100% | 1: 100% / 100% | 12% / 78% | 16% | 95% (21/22) | 40% (21/52) |
| Quantities | 1 | 1 | 0 / 0 | 0 | 0.07 | 0.071 |  |  | 0% / 0% | 0% |  | |
| Rules | 2 | 0 | 21 / 10 | 0 | 0.11 | 0.004 | 10: 20% / 100% | 1: 0% / 100% | 0% / 10% | 13% | 33% (7/21) | 35% (7/20) |
| StandingClaims | 2 | 2 | 0 / 0 | 0 | 0.14 | 0.144 |  |  | 0% / 0% | 0% |  | |
| Storypoints | 1 | 0 | 11 / 10 | 4 (2 quote not placed, 2 surface absent from docu) | 0.19 | 0.009 | 11: 36% / 100% |  | 18% / 55% | 48% | 65% (13/20) | 15% (13/84) |
| StructureBeats | 1 | 0 | 11 / 17 | 1 (1 quote not placed) | 0.10 | 0.004 | 11: 100% / 100% | 1: 100% / 100% | 27% / 64% | 79% |  | |
| TermContrasts | 1 | 0 | 62 / 8 | 14 (9 quote not placed, 5 joined or shortened quot) | 0.32 | 0.005 | 14: 79% / 100% | 1: 100% / 100% | 24% / 68% | 81% |  | |
| TermDefinitions | 1 | 0 | 90 / 0 | 2 (2 quote not placed) | 0.29 | 0.003 | 14: 79% / 93% |  | 53% / 53% | 70% |  | |
| TermReadings | 1 | 0 | 66 / 4 | 4 (4 quote not placed) | 0.16 | 0.002 |  |  | 12% / 12% | 51% | 76% (13/17) | 65% (13/20) |
| TermTaxonomy | 1 | 0 | 7 / 1 | 0 | 0.04 | 0.004 | 7: 43% / 43% |  | 14% / 57% | 50% | 71% (5/7) | 25% (5/20) |
| ThemeMotifs | 1 | 0 | 4 / 4 | 0 | 0.04 | 0.004 | 4: 75% / 100% |  | 0% / 75% | 50% | 88% (7/8) | 35% (7/20) |
| Utterances | 2 | 0 | 3 / 68 | 1 (1 ambiguous quote) | 0.27 | 0.004 | 3: 100% / 100% | 9: 44% / 100% | 0% / 100% | 1% | 34% (15/44) | 14% (15/108) |

## Does the grade predict a good record?

Over every labelled row: the share a reader marked `ok`, by the grade code gave it (2: a cue of the contract and every name stand in the quotation; 1: one of the two; 0: neither). A grade that does not separate them is not a filter and is not used as one; only `CUE_REQUIRED` contracts drop a row without its cue.

| grade | labelled | ok | part | wrong | ok share |
|---|---|---|---|---|---|
| 0 | 150 | 88 | 45 | 17 | 59% |
| 1 | 90 | 46 | 32 | 12 | 51% |
| 2 | 21 | 16 | 3 | 2 | 76% |

## Per document: how much of what the pages cite the contracts, together, find

| document | lines the pages cite | lines any contract found | of them cited | contracts run | cost, USD |
|---|---|---|---|---|---|
| briefing-core-concepts-of-the-kohaerenz-protokoll-project | 0 | 0 | — | 2 | 0.23 |
| detaillierte-kapiteluebersicht | 0 | 43 | — | 6 | 0.61 |
| dual-storyform-hintergruende-md | 84 | 20 | 13 (15% of the pages’ lines) | 1 | 0.19 |
| kohaerenz-protokoll-meta-foreshadowing-beobachter-logik | 20 | 20 | 16 (80% of the pages’ lines) | 11 | 0.51 |
| kohaerenz-protokoll-weltkonzept-synthese | 0 | 79 | — | 3 | 0.90 |
| koharenz-protokoll-sprach-dna-2026-05-13-md | 52 | 29 | 27 (52% of the pages’ lines) | 5 | 0.75 |
| kp-kap25-2026-09-14-md | 56 | 41 | 12 (21% of the pages’ lines) | 1 | 0.14 |
| the-coherence-protocol-the-hidden-rules-that-hold-reality-to | 0 | 20 | — | 4 | 0.30 |

## Names that attach to nothing — the 15 most frequent

A name a contract found in a quotation and no page or entity contains. Each is a candidate for a page, an alias or an entity, and none is any of them until a person says so.

- `Kohärenz-Insel` × 16
- `Rendering-Grenzen` × 15
- `Wir-Stimme` × 14
- `Kapitel 35-40` × 12
- `Kapitel 27-34` × 11
- `Erzähler-Stimme` × 9
- `Lese-Abhängigkeit` × 7
- `Große Stille` × 7
- `Resonanz` × 7
- `Stasis-Lücken` × 6
- `Stilebene 1` × 6
- `Stilebene 2` × 6
- `Juna-Spiegelung` × 5
- `Stilebene 3` × 5
- `Der Geschmack von Wut` × 4
