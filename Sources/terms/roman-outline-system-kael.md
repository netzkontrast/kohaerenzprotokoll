---
source: Sources/drive/roman-outline-system-kael.md
drive_id: "1g9GmHtugee33U-ema8l5S9XviEfRDDH0msae_J6WMi8"
title: "Roman-Outline: System Kael"
category: charaktere
index_date: "2025-06-24"
extracted: "2026-10-05"
candidates: 101    # the terms capture.py counted
---

# Term census — Roman-Outline: System Kael

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py roman-outline-system-kael`

```
  lines                288  (frontmatter ends at 9)
  body words           4187
  headings             24   bold-only lines 0
  table rows           48   code fences 0
  question marks       14
  backslash escapes    144
  typographic marks    87   ascii quotes 0
  invisible characters none
  math symbol lines    0
  glued ref numbers    30
  repeated labels      none
  longest line         952 chars
```

## Stance, read per passage

The document is a plan: it calls itself a „Plot-Blueprint“ ^[L22] for the first part of a novel, and its appendix is headed „Zu integrierende Referenzmatrizen“ ^[L203]. The appendix says the tables are recommended as tools for working out scenes: „wird die Verwendung der folgenden“ ^[L207] tables `empfohlen`. It speaks in the present tense about events of the planned novel (what Kael does in each chapter) and does not report a finished text or a decision.

Each of the four parts (L28, L71, L116, L161) carries the same four sub-headings: `Set the Scene` (4 times), a sub-heading on Kael's psychological state, `Plot Progression & Systemic Reaction` (4 times) and `Thematische Resonanz` (4 times). The first is a description of the world, the second a reading of the psychological state, the third the chapter-by-chapter bullets, the fourth a statement of the theme: „Kontrolle vs. Akzeptanz“ ^[L67].

Two passages are hedged. The assignment of parts to Kael's Anteile in Teil II and III is put as a possibility: Rhys „versucht möglicherweise, eine Verbindung zu Echo herzustellen“ ^[L92], Nyx and Alex „sich möglicherweise in der Figur“ ^[L135] of Silas bündeln, and Isabelle „könnte hier seinen Einfluss ausüben“ ^[L137]. Tables 1 and 3 carry question marks in cells, for example (L220, L255, L257, L258, L260) beside the matrix legend „Legende: S = Signifikante“ ^[L241].

Nearly every sentence about the world ends in a glued reference number `1` (30 such, per the profile); the reference list at L287 names a single source. The outline therefore restates what that text says and is not itself the definition of the terms.

## Candidates and counts

101 candidates, written while reading and frozen by the count (`Plan/runs/roman-outline-system-kael/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `roman-outline-system-kael.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kael` ^[roman-outline-system-kael.md:#53] | 53 | 79 | 13, 22, 24, 37, 43, 47, 55, 56, 57, 58, 59, 67 … | `Kaels` ×26 |
| `Juna` ^[roman-outline-system-kael.md:#5] | 5 | 17 | 24, 39, 59, 67, 82, 100, 127, 172, 188, 227, 233, 234 … | `Juna-Verbindung` ×7, `Juna-Echos` ×2, `Juna-Echo` ×1, `Juna-Kontakt` ×1 |
| `AEGIS` ^[roman-outline-system-kael.md:#21] | 21 | 23 | 24, 39, 56, 57, 59, 67, 100, 102, 149, 189, 191, 199 … | `AEGIS-Hub` ×1, `AEGIS-Überwachung` ×1 |
| `LogOS` ^[roman-outline-system-kael.md:#3] | 3 | 3 | 37, 58, 234 |  |
| `Mnemosyne` ^[roman-outline-system-kael.md:#4] | 4 | 7 | 37, 57, 80, 103, 104, 235, 273 | `Mnemosyne-Archive` ×2, `Mnemosyne-Archiv` ×1 |
| `Cerberus` ^[roman-outline-system-kael.md:#5] | 5 | 5 | 125, 127, 147, 149, 236 |  |
| `Kairos` ^[roman-outline-system-kael.md:#3] | 3 | 3 | 170, 189, 237 |  |
| `Sophia` ^[roman-outline-system-kael.md:#3] | 3 | 3 | 170, 189, 237 |  |
| `Lex` ^[roman-outline-system-kael.md:#11] | 11 | 11 | 47, 57, 104, 148, 190, 191, 217, 219, 247 |  |
| `Nyx` ^[roman-outline-system-kael.md:#9] | 9 | 9 | 135, 137, 146, 148, 180, 190, 191, 217, 220 |  |
| `Alex` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 135 |  |
| `Silas` ^[roman-outline-system-kael.md:#7] | 7 | 7 | 135, 146, 190, 247, 277 |  |
| `Isabelle` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 137 |  |
| `Rhys` ^[roman-outline-system-kael.md:#7] | 7 | 7 | 92, 180, 190, 191, 217, 222 |  |
| `Selene` ^[roman-outline-system-kael.md:#4] | 4 | 4 | 180, 190, 217, 223 |  |
| `Kiko` ^[roman-outline-system-kael.md:#5] | 5 | 5 | 80, 90, 190, 217, 221 |  |
| `Lia` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 80 |  |
| `Echo` ^[roman-outline-system-kael.md:#10] | 10 | 18 | 39, 55, 56, 82, 90, 92, 104, 190, 227, 233, 235, 247 … | `Echos` ×4, `Echo-Anteil` ×1 |
| `Echos` ^[roman-outline-system-kael.md:#4] | 4 | 6 | 39, 55, 56, 82, 92, 227 |  |
| `Schattenkind` ^[roman-outline-system-kael.md:#3] | 3 | 4 | 56, 149, 247, 279 | `Schattenkindes` ×1 |
| `Schattenkindes` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 56 |  |
| `Argus` ^[roman-outline-system-kael.md:#4] | 4 | 4 | 102, 247, 275 |  |
| `Thorne` ^[roman-outline-system-kael.md:#5] | 5 | 5 | 59, 247, 279 |  |
| `Sibyl` ^[roman-outline-system-kael.md:#4] | 4 | 4 | 188, 247, 280 |  |
| `Anya` ^[roman-outline-system-kael.md:#4] | 4 | 5 | 147, 190, 191, 247, 278 | `Anyas` ×1 |
| `Limina` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 247 |  |
| `Nox` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 247 |  |
| `Chronos` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 247 |  |
| `Einheit 734` ^[roman-outline-system-kael.md:#3] | 3 | 3 | 101, 247, 275 |  |
| `Host-Anteil Kael` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 47 |  |
| `Anscheinend Normalen Persönlichkeitsanteilen` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 37 |  |
| `ANPs` ^[roman-outline-system-kael.md:#4] | 4 | 4 | 37, 47, 92 |  |
| `Emotionalen Persönlichkeitsanteile` ^[roman-outline-system-kael.md:#2] | 2 | 2 | 47, 80 |  |
| `EPs` ^[roman-outline-system-kael.md:#4] | 4 | 4 | 47, 80, 90 |  |
| `Kernphobie` ^[roman-outline-system-kael.md:#2] | 2 | 3 | 47, 90, 211 | `Kernphobien` ×1 |
| `Juna-Echos` ^[roman-outline-system-kael.md:#2] | 2 | 2 | 39, 227 |  |
| `Juna-Verbindung` ^[roman-outline-system-kael.md:#7] | 7 | 7 | 59, 67, 82, 100, 127, 172, 188 |  |
| `K-Juna-Paradoxon` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 24 |  |
| `Paradoxon X` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 191 |  |
| `System-Entropie` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 24 |  |
| `Risse` ^[roman-outline-system-kael.md:#13] | 13 | 14 | 24, 39, 47, 55, 57, 59, 82, 127, 172, 227, 233, 272 | `Rissen` ×1 |
| `Kern-Welten` ^[roman-outline-system-kael.md:#4] | 4 | 4 | 22, 24, 189, 225 |  |
| `Kern-Welt` ^[roman-outline-system-kael.md:#5] | 5 | 10 | 22, 24, 37, 80, 125, 170, 189, 225, 233 | `Kern-Welten` ×4, `Kern-Weltmechanik` ×1 |
| `KW1` ^[roman-outline-system-kael.md:#7] | 7 | 7 | 28, 33, 37, 39, 90, 100, 234 |  |
| `KW2` ^[roman-outline-system-kael.md:#10] | 10 | 10 | 71, 76, 80, 90, 102, 103, 125, 145, 235 |  |
| `KW3` ^[roman-outline-system-kael.md:#5] | 5 | 5 | 116, 121, 125, 145, 236 |  |
| `KW4` ^[roman-outline-system-kael.md:#5] | 5 | 5 | 161, 166, 170, 189, 237 |  |
| `Konstrukt-Stadt` ^[roman-outline-system-kael.md:#4] | 4 | 4 | 28, 33, 37, 234 |  |
| `Resonanz-Landschaft` ^[roman-outline-system-kael.md:#5] | 5 | 5 | 71, 76, 80, 102, 235 |  |
| `Grenzfeste` ^[roman-outline-system-kael.md:#5] | 5 | 5 | 116, 121, 125, 147, 236 |  |
| `Möglichkeits-Garten` ^[roman-outline-system-kael.md:#5] | 5 | 5 | 161, 166, 170, 188, 237 |  |
| `Threshold Zone` ^[roman-outline-system-kael.md:#2] | 2 | 2 | 100, 275 |  |
| `Glitching Market` ^[roman-outline-system-kael.md:#3] | 3 | 3 | 145, 277 |  |
| `Garten der Möglichkeiten` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 147 |  |
| `Abgrund der Ängste` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 148 |  |
| `Nexus of Whispers` ^[roman-outline-system-kael.md:#2] | 2 | 2 | 188, 280 |  |
| `Mnemosyne-Archive` ^[roman-outline-system-kael.md:#2] | 2 | 2 | 37, 273 |  |
| `Mnemosyne-Archiv` ^[roman-outline-system-kael.md:#1] | 1 | 3 | 37, 57, 273 | `Mnemosyne-Archive` ×2 |
| `Kaels Apartment` ^[roman-outline-system-kael.md:#2] | 2 | 2 | 37, 271 |  |
| `Spiegelscherben-Korridor` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 271 |  |
| `Sektor Gamma` ^[roman-outline-system-kael.md:#2] | 2 | 2 | 272, 274 |  |
| `Sektor Alpha` ^[roman-outline-system-kael.md:#2] | 2 | 2 | 189, 281 |  |
| `Zentralplatz` ^[roman-outline-system-kael.md:#2] | 2 | 2 | 189, 281 |  |
| `AEGIS Hub` ^[roman-outline-system-kael.md:#2] | 2 | 2 | 281, 283 |  |
| `Entropie-Knotenpunkt` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 283 |  |
| `Innerer Konferenzraum` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 282 |  |
| `Sicherer Unterschlupf` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 282 |  |
| `Chaos-Zone` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 275 |  |
| `Überwelt` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 191 |  |
| `Fundaments` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 188 |  |
| `Ego-Tod` ^[roman-outline-system-kael.md:#2] | 2 | 2 | 148 |  |
| `Innere Rat` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 190 |  |
| `Inneren Rat` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 190 |  |
| `Wir-Geflecht` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 190 |  |
| `Mosaik-Herz` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 180 |  |
| `Welle von Unmöglichkeit` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 189 |  |
| `Zero-Trust Execution Model` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 58 |  |
| `ZTEM` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 58 |  |
| `System-Neustart` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 55 |  |
| `Kern-KI` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 191 |  |
| `Guardian Blind Spot` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 233 |  |
| `Guardians` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 225 |  |
| `Wächter` ^[roman-outline-system-kael.md:#7] | 7 | 11 | 37, 57, 80, 102, 125, 170, 189, 191, 227, 236 | `Wächters` ×3, `Wächter-Anteil` ×1 |
| `Welle der Unmöglichkeit` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 189 |  |
| `Plot-Blueprint` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 22 |  |
| `Set the Scene` ^[roman-outline-system-kael.md:#4] | 4 | 4 | 33, 76, 121, 166 |  |
| `Plot Progression & Systemic Reaction` ^[roman-outline-system-kael.md:#4] | 4 | 4 | 51, 96, 141, 184 |  |
| `Thematische Resonanz` ^[roman-outline-system-kael.md:#4] | 4 | 4 | 63, 108, 153, 195 |  |
| `Referenzmatrizen` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 203 |  |
| `Charakter-Integrationsmatrix` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 239 |  |
| `Lokalitäten-Aktivierung` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 262 |  |
| `Matrix Interner Konflikte und Phobien` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 209 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Heldinnenreise` ^[roman-outline-system-kael.md:#2] | 2 | 2 | 22, 157 |  |
| `Environmental Storytelling` ^[roman-outline-system-kael.md:#3] | 3 | 3 | 39, 172, 264 |  |
| `EST` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 39 |  |
| `psychologischen Horrors` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 82 |  |
| `DIS` ^[roman-outline-system-kael.md:#1] | 1 | 1 | 233 |  |
| `DID` ^[roman-outline-system-kael.md:#0] | 0 | 1 | 271 |  |
| `Trauma` ^[roman-outline-system-kael.md:#1] | 1 | 10 | 22, 56, 80, 82, 104, 112, 149, 235 | `traumatischen` ×3, `Traumas` ×2, `Trauma-Anteile` ×1, `Trauma-Landschaft` ×1 |
| `Depersonalisation` ^[roman-outline-system-kael.md:#2] | 2 | 2 | 55, 271 |  |
| `Multiplizität` ^[roman-outline-system-kael.md:#2] | 2 | 2 | 180, 190 |  |

## What the extraction ran into

**The zero, `DID`.** The document writes it once, in a table cell: „Erste DID-Andeutung“ ^[L271]. It stands inside a hyphenated compound, so the whole-word count is 0 and the compound count is 1 (`read.py --count "DID"`). It is an inflection of the hyphen rule, not an absence. The long form is not written; the document writes `DIS` once, in the header „Kaels DIS“ ^[L233], and neither is expanded.

**Standing alone less often than with compounds (14).** `Kael` 53 of 79 (`Kaels` 26 times, plus compounds such as `Host-Anteil Kael`), `Juna` 5 of 17 (the hyphen compounds `Juna-Verbindung`, `Juna-Echos`, `Juna-Echo`, `Juna-Kontakt`), `AEGIS` 21 of 23, `Mnemosyne` 4 of 7 (the `Mnemosyne-Archive` and `Mnemosyne-Archiv` compounds), `Echo` 10 of 18 (`Echos`, `Echo-Anteil`), `Echos` 4 of 6, `Schattenkind` 3 of 4 (`Schattenkindes`), `Anya` 4 of 5 (`Anyas`), `Kernphobie` 2 of 3 (`Kernphobien`), `Risse` 13 of 14 (`Rissen`), `Kern-Welt` 5 of 10 (`Kern-Welten` 4, `Kern-Weltmechanik`), `Mnemosyne-Archiv` 1 of 3 (the plural `Mnemosyne-Archive`), `Wächter` 7 of 11 (`Wächters`, `Wächter-Anteil`) and `Trauma` 1 of 10 (`traumatischen`, `Traumas`, `Trauma-Anteile`, `Trauma-Landschaft`). All are inflections or compounds.

**Five lines read as prose, not counted.** `Dr. Thorne`, `Ext. Schnittstelle`, `Kontrolle vs. Akzeptanz`, `Logik vs. Resonanz` and `Fragmentierung vs. Ganzheit` carry a period and a space and were not counted by `capture.py`. They are counted by hand in `05-verify.txt`: `Dr. Thorne` 3, `Ext. Schnittstelle` 1, each of the three `vs.` pairs 1.

**Numbered series.** The place labels `E0` to `E6` are written in parentheses behind a place, for example „Möglichkeits-Garten (E5)“ ^[L188]; the digit is glued to the letter and the number means a different place in each world (`E1` is Kaels Apartment in KW1 and the Glitching Market in KW3). The labels are not candidates.

**Export artifacts.** The file has 144 backslash escapes (the table cells write `\*\*` around the chapter number and `\\-` for an empty cell), 30 glued reference numbers from dropped footnote superscripts, and bold names split across a line break after the sentence they belong to (`K-Juna-Paradoxon` on L24 stands at the start of the line after `das zentrale`). The count reads each line as written, so a name in the break is found. Names carry the digit in the form `KW1`; the document never writes a subscript form. The table of Tabelle 3 is flattened to pipe rows with sixteen columns.

**Surfaces that are one thing in two forms, or two things under one.** `Echo` and `Echos` appear as the figure and as the plural of echoes; at L90 the text says Kiko `manifestiert sich als die Figur` Echo, so the name is also the form of a part. `Innere Rat` is the heading of Kapitel 12 and `Inneren Rat` is the accusative inside that chapter; both are listed. `Welle von Unmöglichkeit` is the quotation inside the Kapitel 11 text, `Welle der Unmöglichkeit` the chapter title. `Guardians` appears once, in the title of Tabelle 2; the text says `Wächter`. `Lia` stands once, at L80, with Kiko.

**Standing.** The document claims no canon standing for itself. It calls itself an outline and recommends tables for later use.

**Facts the draft lists, unchanged.**

**Zeros:** 1 — `DID`.

**Standing alone less often than with compounds:** 14 — `Kael` 53/79, `Juna` 5/17, `AEGIS` 21/23, `Mnemosyne` 4/7, `Echo` 10/18, `Echos` 4/6, `Schattenkind` 3/4, `Anya` 4/5, `Kernphobie` 2/3, `Risse` 13/14, `Kern-Welt` 5/10, `Mnemosyne-Archiv` 1/3, `Wächter` 7/11, `Trauma` 1/10.

**`- ` lines read as prose and not counted:** 5 — Dr. Thorne · Ext. Schnittstelle · Kontrolle vs. Akzeptanz · Logik vs. Resonanz · Fragmentierung vs. Ganzheit.
