# qmd over the unread sources — 2026-09-26

The author asked on 2026-09-26: „Update qmd - and make a Search in ovet the uninfeszed sources".

**A search places a document to look at. It measures nothing** (the `qmd` skill; `CLAUDE.md`). Every count below is a count of *search hits*, not of occurrences, and is not a number about the corpus.

## The index

The container was fresh and the index empty. `qmd update` rebuilt the BM25 index in 14 s: 1,641 files in seven collections, 371 of them landed sources. `scripts/setup_qmd.sh --check` reported every file in a collection. The embedding models and vectors were started in the background with `scripts/setup_qmd.sh`; this scan uses `qmd search` (BM25) only, so nothing here depends on them.

## Method

One record per open item: the 15 conflicts, the 5 questions, and 15 questions for the author from `NOW.md` (A1–A15). Each record is one to four short German queries (`queries.tsv`) against `sources` with `-n 40`. Short queries, because a multi-word query returned nothing for eight records on a first pass — qmd's BM25 wants most terms present. Hits on the 24 documents with a census were dropped; the rest are in `hits.jsonl`, one row per hit with its line.

1562 hits on unread documents, 302 documents. 347 landed documents have no census; 242 manifest rows are not landed and cannot be searched.

## A search that would have told a falsehood

`Mira` returned six hits on unread documents. All six are the stemmer: „miracle" matched. `grep -rw Mira Sources/drive` finds the name in one document, the Doppel-Klammer Abhandlung, so `NOW.md`'s claim stands. A3 is left out of every table below. This is the rule the `qmd` skill keeps, met on the first day it was tested on a name.

## Canon-era documents still unread — all fifteen were hit

| records hit | date | document | scanned 2026-09-25 | records |
|--:|---|---|:-:|---|
| 22 | 2026-05-08 | `worldbuilding-konzept-kohaerenzprotokoll-md` | yes | A1 A10 A12 A14 A2 A4 A5 A8 A9 C10 C11 C12 C13 C14 C2 C3 C5 C6 C7 Q1 Q3 Q5 |
| 16 | 2026-05-08 | `kohaerenz-protokoll-philosophischer-bericht-md` |  | A10 A12 A2 A8 C10 C11 C12 C13 C14 C3 C6 C7 C9 Q1 Q3 Q4 |
| 11 | 2026-05-08 | `dual-storyform-hintergruende-md` |  | A10 A12 A2 A5 A8 C12 C2 C6 C7 C8 Q1 |
| 10 | 2026-06-10 | `kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md` | yes | A10 A12 A14 A15 A2 A6 A7 A9 C5 C7 |
| 9 | 2026-09-14 | `2026-09-14-kap25-vertiefung-md` |  | A10 A12 A13 A2 A8 C11 C6 C9 Q3 |
| 8 | 2026-05-08 | `mining-report-kohaerenz-protokoll-narrative-building-blocks` |  | A1 A12 A15 A5 A9 C12 C8 Q2 |
| 8 | 2026-05-08 | `systemic-architecture-specification-the-coherence-protocol-w` |  | A12 A14 A2 A5 A9 C1 Q1 Q5 |
| 5 | 2026-05-08 | `companion-guide-to-the-coherence-protocol-understanding-love` |  | A12 A2 A5 C1 Q5 |
| 5 | 2026-05-08 | `mining-report-kohaerenz-protokoll-plot-outline-construction` |  | A12 A14 C11 C12 C8 |
| 4 | 2026-05-08 | `the-architecture-of-fracture-a-compendium-of-the-kael-system` |  | A14 A9 C1 Q5 |
| 3 | 2026-05-17 | `koharenz-protokoll-kapitel-0-v2-md` |  | A10 C10 C12 |
| 3 | 2026-09-14 | `kp-kap25-2026-09-14-md` |  | A8 C14 Q3 |
| 2 | 2026-05-08 | `systems-narrative-analysis-the-coherence-protocol-kanon-2026` |  | A12 C8 |
| 2 | 2026-05-08 | `the-physics-of-heartbreak-5-surprising-takeaways-from-the-ko` |  | A14 C1 |
| 1 | 2026-05-08 | `editorial-style-dossier-somatic-and-linguistic-implementatio` |  | C1 |

## Older unread documents with the most records hit (top twelve)

| records hit | date | category | document | scanned |
|--:|---|---|---|:-:|
| 15 | 2026-04-30 | storyform | `dramatica-storyform-synthese-aegis-analyse-2` |  |
| 15 | 2026-02-26 | theorie-logik | `roman-konzept-dualitaet-kohaerenz-spannung` | yes |
| 14 | 2025-04-27 | kernkonzept | `kohaerenz-protokoll` |  |
| 14 | 2025-07-29 | worldbuilding | `welt` |  |
| 12 | 2025-04-18 | worldbuilding | `umfassendes-lokalitaeten-konzept-fuer-roman` |  |
| 11 | 2025-07-29 | aegis | `aegis` |  |
| 11 | 2025-11-28 | kernkonzept | `analyse-des-kohaerenz-protokolls` |  |
| 11 | 2026-04-08 | theorie-physik | `hard-sf-roman-outline-dkt-physik-cosmic-horror` |  |
| 11 | 2025-04-17 | kernkonzept | `kohaerenz-protokoll-2` |  |
| 11 | 2025-04-18 | worldbuilding | `orte-konzept-fuer-kohaerenz-protokoll` |  |
| 11 | 2025-06-24 | charaktere | `roman-outline-system-kael` |  |
| 10 | 2025-04-18 | charaktere | `charakterkonzepte-fuer-kohaerenz-protokoll` |  |

## Per record: where to look first

Up to three unread documents per record, canon-era first, then by BM25 score; `slug:line` is the hit's chunk.

| record | subject | look first |
|---|---|---|
| C1 | AEGIS: what the name stands for | `the-architecture-of-fracture-a-compendium-of-the-kael-system`:47 (0.76, 2026-05) · `the-physics-of-heartbreak-5-surprising-takeaways-from-the-ko`:17 (0.73, 2026-05) · `companion-guide-to-the-coherence-protocol-understanding-love`:43 (0.71, 2026-05) |
| C2 | Entropie: which sense | `worldbuilding-konzept-kohaerenzprotokoll-md`:33 (0.68, 2026-05) · `dual-storyform-hintergruende-md`:52 (0.67, 2026-05) · `duale-storyform-synthese-kohaerenz-protokoll`:32 (0.87, 2026-04) |
| C3 | Emergenz: where AEGIS comes from | `worldbuilding-konzept-kohaerenzprotokoll-md`:435 (0.75, 2026-05) · `kohaerenz-protokoll-philosophischer-bericht-md`:49 (0.60, 2026-05) · `emergenz-aegis-und-selbststrukturierung`:25 (0.82, 2025-04) |
| C4 | the blind spot: AEGIS' or each Guardian's | `welten`:46 (0.90, 2025-04) · `charakterkonzepte-fuer-kohaerenz-protokoll`:50 (0.89, 2025-04) · `aegis-paradoxon-konzeption-und-analyse`:79 (0.85, 2025-04) |
| C5 | Möglichkeits-Garten: a world or a place | `worldbuilding-konzept-kohaerenzprotokoll-md`:584 (0.76, 2026-05) · `kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md`:451 (0.67, 2026-06) · `roman-outline-system-kael`:147 (0.83, 2025-06) |
| C6 | Guardians: five or two | `dual-storyform-hintergruende-md`:347 (0.76, 2026-05) · `kohaerenz-protokoll-philosophischer-bericht-md`:294 (0.74, 2026-05) · `worldbuilding-konzept-kohaerenzprotokoll-md`:192 (0.72, 2026-05) |
| C7 | Juna's first direct appearance | `worldbuilding-konzept-kohaerenzprotokoll-md`:667 (0.84, 2026-05) · `kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md`:180 (0.82, 2026-06) · `dual-storyform-hintergruende-md`:419 (0.77, 2026-05) |
| C8 | AEGIS' Approach in Storyform B | `dual-storyform-hintergruende-md`:114 (0.81, 2026-05) · `mining-report-kohaerenz-protokoll-narrative-building-blocks`:15 (0.77, 2026-05) · `mining-report-kohaerenz-protokoll-plot-outline-construction`:27 (0.76, 2026-05) |
| C9 | Konstrukt-Stadt: its scale | `kohaerenz-protokoll-philosophischer-bericht-md`:63 (0.71, 2026-05) · `2026-09-14-kap25-vertiefung-md`:60 (0.67, 2026-09) · `nichts-ordnung-fragmentierung-resonanz-nebel`:15 (0.75, 2025-04) |
| C10 | the bleeding knuckles | `worldbuilding-konzept-kohaerenzprotokoll-md`:29 (0.77, 2026-05) · `koharenz-protokoll-kapitel-0-v2-md`:607 (0.70, 2026-05) · `kohaerenz-protokoll-philosophischer-bericht-md`:535 (0.63, 2026-05) |
| C11 | Landauer: warm or cold ozone | `mining-report-kohaerenz-protokoll-plot-outline-construction`:46 (0.81, 2026-05) · `worldbuilding-konzept-kohaerenzprotokoll-md`:29 (0.80, 2026-05) · `2026-09-14-kap25-vertiefung-md`:47 (0.79, 2026-09) |
| C12 | Genesis: three beats or four; 734's order | `worldbuilding-konzept-kohaerenzprotokoll-md`:180 (0.76, 2026-05) · `mining-report-kohaerenz-protokoll-plot-outline-construction`:29 (0.73, 2026-05) · `kohaerenz-protokoll-philosophischer-bericht-md`:276 (0.70, 2026-05) |
| C13 | Externe Ebene / Basisrealität | `worldbuilding-konzept-kohaerenzprotokoll-md`:431 (0.68, 2026-05) · `kohaerenz-protokoll-philosophischer-bericht-md`:443 (0.16, 2026-05) · `konsolidierung-des-hard-canon-protokolls`:29 (0.82, 2026-03) |
| C14 | AEGIS in the first person | `kohaerenz-protokoll-philosophischer-bericht-md`:247 (0.84, 2026-05) · `worldbuilding-konzept-kohaerenzprotokoll-md`:415 (0.75, 2026-05) · `kp-kap25-2026-09-14-md`:44 (0.11, 2026-09) |
| C15 | who carries Flight | `a-guide-to-the-society-of-self-understanding-system-kael`:29 (0.78, 2025-10) · `project-coherence-protocol-a-canon-of-core-identity-and-anta`:39 (0.77, 2025-11) · `concept-paper-the-architectural-foundations-of-kohaerenz-pro`:114 (0.76, 2025-11) |
| Q1 | Guardians and AEGIS | `systemic-architecture-specification-the-coherence-protocol-w`:1 (0.77, 2026-05) · `kohaerenz-protokoll-philosophischer-bericht-md`:507 (0.71, 2026-05) · `worldbuilding-konzept-kohaerenzprotokoll-md`:192 (0.66, 2026-05) |
| Q2 | the eight protocols | `mining-report-kohaerenz-protokoll-narrative-building-blocks`:37 (0.81, 2026-05) · `kohaerenz-protokoll-aktuelle-gesamtkonzept-synthese`:16 (0.84, 2025-04) · `digitale-uberwelt-konzept-und-gestaltung`:76 (0.82, 2026-03) |
| Q3 | how many worlds and alters | `worldbuilding-konzept-kohaerenzprotokoll-md`:388 (0.81, 2026-05) · `kohaerenz-protokoll-philosophischer-bericht-md`:41 (0.79, 2026-05) · `kp-kap25-2026-09-14-md`:48 (0.74, 2026-09) |
| Q4 | Wächter | `kohaerenz-protokoll-philosophischer-bericht-md`:203 (0.61, 2026-05) · `kael-charakterarchitektur-und-konfliktdynamik-3`:40 (0.81, 2025-04) · `kael-charakterarchitektur-und-konfliktdynamik`:40 (0.81, 2025-04) |
| Q5 | Guardian–world pairing, Erasure-Pol, Sophia | `worldbuilding-konzept-kohaerenzprotokoll-md`:201 (0.74, 2026-05) · `the-architecture-of-fracture-a-compendium-of-the-kael-system`:52 (0.72, 2026-05) · `companion-guide-to-the-coherence-protocol-understanding-love`:50 (0.72, 2026-05) |
| A1 | Ursprungs-Ich | `mining-report-kohaerenz-protokoll-narrative-building-blocks`:33 (0.76, 2026-05) · `worldbuilding-konzept-kohaerenzprotokoll-md`:178 (0.73, 2026-05) · `genesis-krise-aegis-prosa-auftrag`:17 (0.80, 2025-04) |
| A2 | Alex before the separation | `worldbuilding-konzept-kohaerenzprotokoll-md`:435 (0.75, 2026-05) · `companion-guide-to-the-coherence-protocol-understanding-love`:43 (0.70, 2026-05) · `2026-09-14-kap25-vertiefung-md`:31 (0.70, 2026-09) |
| A3 | Mira | — the six hits are the stemmer („miracle“); see above |
| A4 | Mosaik-Herz: one thing or two | `worldbuilding-konzept-kohaerenzprotokoll-md`:620 (0.65, 2026-05) · `kohaerenz-protokoll-kapitel-39-das-mosaik-herz`:3 (0.83, 2026-02) · `aegis-und-der-kollaps-kritische-analyse`:65 (0.78, 2026-03) |
| A5 | KW2: Resonanz-Landschaft or Mnemosyne-Archipel | `worldbuilding-konzept-kohaerenzprotokoll-md`:200 (0.74, 2026-05) · `dual-storyform-hintergruende-md`:356 (0.73, 2026-05) · `mining-report-kohaerenz-protokoll-narrative-building-blocks`:54 (0.71, 2026-05) |
| A6 | the final form's name | `kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md`:70 (0.73, 2026-06) · `projektanalyse-kohaerenz-protokoll-dis`:3 (0.72, 2025-12) · `roman-entwicklung-ontologie-trauma-horror`:82 (0.71, 2026-04) |
| A7 | Kael-Julia-Bindung | `kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md`:420 (0.74, 2026-06) · `kohaerenz-protokoll-weltkonzept-synthese`:41 (0.88, 2025-04) · `monstergruppe-kohaerenz-protokoll-fundament`:15 (0.85, 2025-04) |
| A8 | Einheit 734 | `kp-kap25-2026-09-14-md`:56 (0.80, 2026-09) · `2026-09-14-kap25-vertiefung-md`:22 (0.80, 2026-09) · `dual-storyform-hintergruende-md`:420 (0.73, 2026-05) |
| A9 | world names after C6 | `the-architecture-of-fracture-a-compendium-of-the-kael-system`:67 (0.77, 2026-05) · `systemic-architecture-specification-the-coherence-protocol-w`:74 (0.76, 2026-05) · `mining-report-kohaerenz-protokoll-narrative-building-blocks`:1 (0.72, 2026-05) |
| A10 | Kap 40's last line | `koharenz-protokoll-kapitel-0-v2-md`:123 (0.81, 2026-05) · `kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md`:2 (0.74, 2026-06) · `dual-storyform-hintergruende-md`:43 (0.72, 2026-05) |
| A11 | the Abhandlung's Setzungen | — no unread hit |
| A12 | one Vortex or two | `kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md`:592 (0.85, 2026-06) · `dual-storyform-hintergruende-md`:168 (0.75, 2026-05) · `systems-narrative-analysis-the-coherence-protocol-kanon-2026`:2 (0.74, 2026-05) |
| A13 | eleven alters or thirteen | `2026-09-14-kap25-vertiefung-md`:31 (0.86, 2026-09) · `charaktermodellierung-mit-aieos-schema`:17 (0.89, 2026-02) · `charaktere`:25 (0.88, 2025-07) |
| A14 | the living Gödel statement | `worldbuilding-konzept-kohaerenzprotokoll-md`:285 (0.75, 2026-05) · `the-physics-of-heartbreak-5-surprising-takeaways-from-the-ko`:39 (0.75, 2026-05) · `kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md`:293 (0.74, 2026-06) |
| A15 | does AEGIS have qualia | `kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md`:372 (0.74, 2026-06) · `mining-report-kohaerenz-protokoll-narrative-building-blocks`:33 (0.72, 2026-05) · `aegis-philosophie-und-manifest-entwicklung`:19 (0.87, 2025-04) |

## What the hits pointed at, checked by `grep` (orientation only)

**`koharenz-protokoll-kapitel-0-v2-md` (2026-05-17, 639 lines) is the annotated draft's clean text with its own review carried out.** None of the passages the annotated draft marks for deletion stands in it — K-1 to K-3, H-2 to H-4, M-1, N-1, each by a fixed-string `grep`, 0 lines. Neither does „Position halten", the line the annotated draft gives Alex's Vorform, which its deeper revision proposed to cut. The knuckle line is kept (L607). And the formula has a third form: „*Es ist, was es verhindert, dass es nicht ist.*" (L211) — the annotated draft wrote „*Ich bin, …*", the plans „*AEGIS ist, …*". It speaks to the Alex question, C10, C12 and `formel-inversion`, and it was in neither scan.

**`kohaerenz-protokoll-philosophischer-bericht-md` (2026-05-08) was hit for 16 records and never scanned.** C3, C6, C7, C9–C14, Q1, Q3, Q4 among them.

**The newest documents in the corpus are unread**: `2026-09-14-kap25-vertiefung-md` and `kp-kap25-2026-09-14-md`, a Kap-25 deepening of 2026-09-14, four months after every read document.

## What this changes

Nothing in the wiki. It names where to read next; `NOW.md` has the order.
