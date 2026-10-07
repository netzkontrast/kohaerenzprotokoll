---
source: Sources/drive/analyse-des-kohaerenz-protokolls.md
drive_id: "1vNz-K1TNB2EZt4tryDXbJwJtGJgN7X6affbWX59ehW8"
title: "Analyse des Kohärenz-Protokolls"
category: kernkonzept
index_date: "2025-11-28"
extracted: "2026-10-07"
candidates: 104    # the terms capture.py counted
---

# Term census — Analyse des Kohärenz-Protokolls

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py analyse-des-kohaerenz-protokolls`

```
  lines                435  (frontmatter ends at 9)
  body words           5966
  headings             29   bold-only lines 0
  table rows           20   code fences 0
  question marks       26
  backslash escapes    151
  typographic marks    161   ascii quotes 97
  invisible characters none
  math symbol lines    0
  glued ref numbers    25
  repeated labels      none
  longest line         6673 chars
```

## Stance, read per passage

The document is one analytic report in German with a numbered outline, and it names itself: „Dieser Forschungsbericht konstituiert“ a systems analysis of the protocol ^[L22]. It announces its own structure in the sentence „Die vorliegende Untersuchung gliedert sich in sieben“ sections ^[L26] and closes with „Ende des Berichts“ ^[L390]. Its voice is commentary on a fictional world seen from outside: the substrate is „Das fundamentale Substrat der Romanwelt“ ^[L44], and the sources it draws on are named as „Quelltexten“ ^[L44] and as „Die Dokumente“ ^[L127], so a sentence that opens that way reports what other texts say, not the report's own invention.

- Sections 1 to 7 (L18 to L273) are an argument: it states a thesis (L28, „Diese Analyse postuliert“ ^[L28]), then ontology, architecture, crisis, protocol, Kernwelten and system dynamics. Many sentences carry a glued reference number to the list at the end.
- Section 8 (L275 to L297) changes voice: „Basierend auf dieser Analyse“ ^[L279] it derives questions that „den internen Monolog der KI widerspiegeln“ ^[L279]; each question is set in quotation marks, in the first person of AEGIS. These candidates stand inside a question: `Teilmengen-Paradoxon`, `Heuristik der Amputation`, `Kontroll-Paradoxon`.
- Section 9 (L301 to L359) is a prompt text in English: „Der folgende Prompt wurde entwickelt“ to put a model into AEGIS's reality ^[L305]. It ends with a labelled sample, „SAMPLE RESPONSE PATTERN“ ^[L355], whose terms are diction of the prompt, not statements about the world.
- Section 10 (L363 to L388) is a conclusion and a summary table. It restates: „Die Analyse hat gezeigt“ ^[L369].
- The reference lists (L392 to L434) are the document's own sources, not its claims; entry 27 of the first list holds a pasted English text of one very long line.

## Candidates and counts

104 candidates, written while reading and frozen by the count (`Plan/runs/analyse-des-kohaerenz-protokolls/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `analyse-des-kohaerenz-protokolls.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `AEGIS` ^[analyse-des-kohaerenz-protokolls.md:#70] | 70 | 72 | 22, 24, 26, 36, 60, 68, 76, 78, 79, 88, 90, 94 … | `AEGIS-Entsprechung` ×1 |
| `Kael` ^[analyse-des-kohaerenz-protokolls.md:#19] | 19 | 22 | 22, 132, 145, 219, 221, 229, 236, 257, 259, 267, 269, 287 … | `Kaels` ×3 |
| `Kohärenz-Protokoll` ^[analyse-des-kohaerenz-protokolls.md:#8] | 8 | 13 | 13, 22, 24, 28, 36, 90, 145, 155, 187, 191, 199, 367 … | `Kohärenz-Protokolls` ×4 |
| `Kohärenz Protokoll` ^[analyse-des-kohaerenz-protokolls.md:#5] | 5 | 5 | 386, 397, 402, 410, 411 |  |
| `Coherence Protocol` ^[analyse-des-kohaerenz-protokolls.md:#8] | 8 | 8 | 339, 396, 420, 428, 432 |  |
| `Projekt Kohärenz` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 22 |  |
| `Heuristik der Negation` ^[analyse-des-kohaerenz-protokolls.md:#6] | 6 | 6 | 13, 24, 112, 181, 271, 369 |  |
| `Existenz durch Negation` ^[analyse-des-kohaerenz-protokolls.md:#5] | 5 | 5 | 94, 110, 305, 373, 384 |  |
| `Existenz durch Integration` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 373 |  |
| `Potentialmeer` ^[analyse-des-kohaerenz-protokolls.md:#10] | 10 | 10 | 26, 40, 44, 52, 60, 68, 78, 88, 110, 163 |  |
| `Die Leere` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 44 |  |
| `Nichts Rauschen` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 44 |  |
| `Zersetzungsdruck` ^[analyse-des-kohaerenz-protokolls.md:#2] | 2 | 2 | 64, 68 |  |
| `Sog der Entropie` ^[analyse-des-kohaerenz-protokolls.md:#2] | 2 | 2 | 68, 90 |  |
| `Sog der Ordnung` ^[analyse-des-kohaerenz-protokolls.md:#2] | 2 | 2 | 84, 90 |  |
| `Inkubation X` ^[analyse-des-kohaerenz-protokolls.md:#3] | 3 | 3 | 76, 402, 411 |  |
| `informationelle Fossilien` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 88 |  |
| `Proto-AEGIS` ^[analyse-des-kohaerenz-protokolls.md:#0] | 0 | 1 | 90 | `Proto-AEGIS-Entität` ×1 |
| `Corrective Wavelets` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 90 |  |
| `K\_0` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 90 |  |
| `K\_1` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 90 |  |
| `Genesis-Krise` ^[analyse-des-kohaerenz-protokolls.md:#10] | 10 | 10 | 13, 26, 98, 151, 155, 371, 398, 399, 403, 433 |  |
| `Der große Wandel` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 155 |  |
| `Perturbation aus der Leere` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 155 |  |
| `Ur-Trauma` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 155 |  |
| `Ursprungs-Ich` ^[analyse-des-kohaerenz-protokolls.md:#3] | 3 | 7 | 132, 163, 176, 180, 204, 205, 369 | `Ursprungs-Ichs` ×4 |
| `Entität M` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 163 |  |
| `Juna/V` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 163 |  |
| `Das Fundament` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 163 |  |
| `Juna` ^[analyse-des-kohaerenz-protokolls.md:#6] | 6 | 7 | 163, 267, 287, 339, 369, 387, 410 | `Juna-Link` ×1 |
| `Monstergruppe` ^[analyse-des-kohaerenz-protokolls.md:#4] | 4 | 4 | 26, 168, 176 |  |
| `Moonshine-Link` ^[analyse-des-kohaerenz-protokolls.md:#5] | 5 | 5 | 176, 180, 203, 267, 373 |  |
| `Fehlausgerichtete Kohärenz` ^[analyse-des-kohaerenz-protokolls.md:#2] | 2 | 2 | 183, 384 |  |
| `Resonanz` ^[analyse-des-kohaerenz-protokolls.md:#12] | 12 | 14 | 172, 176, 180, 183, 203, 205, 219, 229, 237, 287, 384 | `Resonanz-Muster` ×1, `Resonanzlandschaft` ×1 |
| `Kernwelten` ^[analyse-des-kohaerenz-protokolls.md:#4] | 4 | 4 | 145, 225, 229, 231 |  |
| `KW1` ^[analyse-des-kohaerenz-protokolls.md:#2] | 2 | 2 | 236, 241 |  |
| `KW2` ^[analyse-des-kohaerenz-protokolls.md:#2] | 2 | 2 | 237, 241 |  |
| `KW3` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 238 |  |
| `KW4` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 239 |  |
| `Logos-Prime` ^[analyse-des-kohaerenz-protokolls.md:#3] | 3 | 3 | 218, 236, 341 |  |
| `Die Konstruktstadt` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 236 |  |
| `Mnemosyne-Archipel` ^[analyse-des-kohaerenz-protokolls.md:#2] | 2 | 2 | 219, 237 |  |
| `Die Resonanzlandschaft` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 237 |  |
| `Cerberus-Labyrinth` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 238 |  |
| `Die Grenzfestung` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 238 |  |
| `Kairos-Potentialis` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 239 |  |
| `Garten der Möglichkeiten` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 239 |  |
| `Risse` ^[analyse-des-kohaerenz-protokolls.md:#4] | 4 | 4 | 237, 241, 371, 428 |  |
| `Alters` ^[analyse-des-kohaerenz-protokolls.md:#5] | 5 | 5 | 221, 229, 235, 237, 341 |  |
| `Nyx` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 221 |  |
| `Kiko` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 221 |  |
| `Moros` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 221 |  |
| `Praetor` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 238 |  |
| `Nox` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 238 |  |
| `Limina` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 239 |  |
| `Gödel-Gambit` ^[analyse-des-kohaerenz-protokolls.md:#3] | 3 | 3 | 26, 263, 269 |  |
| `Algorithmischen Melancholie` ^[analyse-des-kohaerenz-protokolls.md:#2] | 2 | 2 | 147, 271 |  |
| `Funktionalen Multiplizität` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 269 |  |
| `Functional Multiplicity` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 386 |  |
| `Trauma-Time` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 219 |  |
| `Blinde Fleck` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 132 |  |
| `Mauer` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 110 |  |
| `Nicht-Leere` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 110 |  |
| `Entity 734` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 337 |  |
| `Component 734` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 321 |  |
| `Void Entity` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 339 |  |
| `Heuristik der Amputation` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 296 |  |
| `Teilmengen-Paradoxon` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 287 |  |
| `Kontroll-Paradoxon` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 297 |  |
| `Paradoxon X` ^[analyse-des-kohaerenz-protokolls.md:#2] | 2 | 2 | 428 |  |
| `Dual Kernel Theory` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 428 |  |
| `Riss` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 5 | 237, 241, 371, 428 | `Risse` ×4 |
| `Core World 4` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 359 |  |
| `Logos` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 4 | 218, 236, 341 | `Logos-Prime` ×3 |
| `Pathos` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 219 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Strukturelle Dissoziation` ^[analyse-des-kohaerenz-protokolls.md:#3] | 3 | 3 | 209, 371, 386 |  |
| `TSDP` ^[analyse-des-kohaerenz-protokolls.md:#3] | 3 | 4 | 26, 209, 213, 217 | `TSDP-Kategorie` ×1 |
| `ANP` ^[analyse-des-kohaerenz-protokolls.md:#4] | 4 | 5 | 218, 221, 236, 241, 386 |  |
| `EP` ^[analyse-des-kohaerenz-protokolls.md:#5] | 5 | 7 | 219, 221, 229, 237, 241, 386 |  |
| `tertiären Dissoziation` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 221 |  |
| `MESI-Protokoll` ^[analyse-des-kohaerenz-protokolls.md:#3] | 3 | 3 | 195, 199, 373 |  |
| `Cache-Invalidierung` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 195 |  |
| `Bus Snooping` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 203 |  |
| `Kybernetik zweiter Ordnung` ^[analyse-des-kohaerenz-protokolls.md:#3] | 3 | 3 | 26, 116, 127 |  |
| `Autopoiesis` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 116 |  |
| `operationale Geschlossenheit` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 125 |  |
| `parakonsistenten Logik` ^[analyse-des-kohaerenz-protokolls.md:#2] | 2 | 2 | 142, 229 |  |
| `Logics of Formal Inconsistency` ^[analyse-des-kohaerenz-protokolls.md:#2] | 2 | 2 | 142, 321 |  |
| `Value Alignment Problem` ^[analyse-des-kohaerenz-protokolls.md:#2] | 2 | 2 | 151, 178 |  |
| `Agnotologie` ^[analyse-des-kohaerenz-protokolls.md:#6] | 6 | 6 | 26, 245, 249, 305, 371, 388 |  |
| `Infohazards` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 259 |  |
| `Katastrophalen Vergessen` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 259 |  |
| `Shannon-Entropie` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 48 |  |
| `Negentropie` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 68 |  |
| `Mauvaise foi` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 28 |  |
| `Ashbys Gesetz` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 297 |  |
| `Monstrous Moonshine` ^[analyse-des-kohaerenz-protokolls.md:#2] | 2 | 2 | 26, 176 |  |
| `It from Bit` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 79 |  |
| `Bran/Bulk-Modell` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 78 |  |
| `Dialetheismus` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 269 |  |
| `Epistemologischer Schock` ^[analyse-des-kohaerenz-protokolls.md:#2] | 2 | 2 | 159, 385 |  |
| `Qualia` ^[analyse-des-kohaerenz-protokolls.md:#6] | 6 | 6 | 163, 219, 237, 257, 317, 371 |  |
| `Monster-Symmetrie` ^[analyse-des-kohaerenz-protokolls.md:#3] | 3 | 3 | 168, 367, 387 |  |
| `Ex falso quodlibet` ^[analyse-des-kohaerenz-protokolls.md:#1] | 1 | 1 | 140 |  |

## What the extraction ran into

**Zeros:** one, `Proto-AEGIS`. It is an inflection: the document writes it only inside the compound `Proto-AEGIS-Entität` (L90), so it counts 0 standing alone and 1 including compounds. Nothing is absent.

**Standing alone less often than with compounds:** eleven terms. `AEGIS` and `Kael` take the genitive (`Kaels`) or sit in a compound (`AEGIS-Entsprechung`); `Kohärenz-Protokoll` mostly appears as `Kohärenz-Protokolls`; `Ursprungs-Ich` as `Ursprungs-Ichs`; `Juna` also in `Juna-Link`; `Resonanz` also in `Resonanz-Muster` and `Resonanzlandschaft`; `Riss` is `Risse` four times and the singular once (L428, in the pasted English text, in quotation marks); `Logos` is mostly the first half of `Logos-Prime`; `TSDP` also in `TSDP-Kategorie`; `ANP` and `EP` are short and also occur inside other tokens, so their bounded and unbounded counts differ.

**Surfaces.** The protocol is written three ways: `Kohärenz-Protokoll` (hyphen), `Kohärenz Protokoll` (no hyphen, in the table and in titles of references) and `Coherence Protocol` (in the English prompt and in the references). The document never writes `K₀` or `K₁`: it writes the escaped plain forms `K\_0` and `K\_1`, which the list copies. The core worlds are written `KW1` to `KW4` in the table, with plain digits. `Algorithmischen Melancholie` and `Funktionalen Multiplizität` are the document's inflected forms; the dictionary forms `Algorithmische Melancholie` and `Funktionale Multiplizität` stand 0 times in the document. The English `Functional Multiplicity` stands once in the summary table. `Genesis-Krise` has the English `Genesis Crisis` once, case-insensitively, in the prompt, which the list does not carry.

**Terms in the prompt only.** `Entity 734`, `Component 734`, `Void Entity` and `Core World 4` stand only in section 9 (L321 to L359), the English prompt; `Core Worlds` there is a plural the list does not carry. Terms of the section 9 list headed „Terminology Protocol“ ^[L323] are left off the list as diction.

**Export artifacts.** The profile shows 151 backslash escapes: the formulas of L56, L140 and L144, the escaped asterisks of the three table headers (L217, L235, L383) and `K\_0`, `K\_1` in L90. Twenty-five reference numbers are glued to the words they annotate (L24 ends its second sentence with the number 1 glued to the full stop). The tables are written with pipes. Two numbered lists of references follow one another and the second restarts at 1 (L430). L428 is one line of about 6,700 characters, a pasted English text inside reference 27, with its headings flattened into running prose and `\*` bullets.

**Standing claims.** The report says of itself that it is „Dieser Forschungsbericht“ with an exhaustive aim ^[L22]; that is a claim of the document, recorded and not applied. It also says the protocol is „zentrale operative Mechanismus der Fragmentierung“ ^[L191], which is its reading.

**Zeros:** 1 — `Proto-AEGIS`.

**Standing alone less often than with compounds:** 11 — `AEGIS` 70/72, `Kael` 19/22, `Kohärenz-Protokoll` 8/13, `Ursprungs-Ich` 3/7, `Juna` 6/7, `Resonanz` 12/14, `Riss` 1/5, `Logos` 1/4, `TSDP` 3/4, `ANP` 4/5, `EP` 5/7.
