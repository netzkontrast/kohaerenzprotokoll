---
source: Sources/drive/kohaerenz-protokoll-konzeptionelle-themen-struktur.md
drive_id: "1auXjKTMTulpVfh5QPKLZcPk5hpiaVgHUgK1qr9Tj_BU"
title: "Kohärenz Protokoll: Konzeptionelle Themen & Struktur"
category: plot-outline
index_date: "2025-11-25"
extracted: "2026-10-06"
candidates: 113    # the terms capture.py counted
---

# Term census — Kohärenz Protokoll: Konzeptionelle Themen & Struktur

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py kohaerenz-protokoll-konzeptionelle-themen-struktur`

```
  lines                431  (frontmatter ends at 9)
  body words           3732
  headings             22   bold-only lines 39
  table rows           14   code fences 0
  question marks       9
  backslash escapes    172
  typographic marks    213   ascii quotes 2
  invisible characters none
  math symbol lines    0
  glued ref numbers    10
  repeated labels      Konzept x39, Physik x3
  longest line         814 chars
```

## Stance, read per passage

The whole text speaks in one expository, report-like voice about the novel; it names no speaker and no date. It calls itself „Dieser Bericht liefert eine erschöpfende Analyse“ ^[L27] and its title says „Eine Exegese der narrativen Systemarchitektur, Ontologie und Psychodynamik“ ^[L13] (heading of L13: `Das Kohärenz Protokoll: Eine Exegese ...`). It describes the project as a thing that exists and works: „Es ist nicht bloß ein Roman“ ^[L23] is a description, never a plan or a question.

- Lines 19 to 31 (section 1, 2) and 35 to 77 (section 2): description of the world's physics and its two antagonists. The voice is declarative ("AEGIS ist ..."); a maxim of AEGIS is quoted inside the report, and the passage on AEGIS opens „Der Antagonist AEGIS ist kein einfacher Schurke“ ^[L60].
- Lines 81 to 119 (section 3): the physics-as-structure passage, a table that the document introduces as „Die folgende Tabelle illustriert, wie physikalische Konzepte“ ^[L103]; the table (L105 to L111) carries a header row of five columns and four rows.
- Lines 123 to 342 (section 4): the 39 themes as a numbered list in three parts, each theme a bold heading line followed by a bullet labelled `Konzept` (the label stands `Konzept` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#41] times as a whole word; 39 of them are the theme labels, one stands in running prose on L93 and one in the table header on L107) and by one or two bullets with a second label such as Insight, Physik, Mechanismus or Systemtheorie. The section introduces itself as „Dieser Abschnitt dekonstruiert die konzeptionellen Themen“ ^[L127]. The parts are introduced as „Hier verlagert sich der Fokus auf die externe Simulation“ ^[L208] and „Die Integration wird zur Waffe“ ^[L281]. These are plan-like descriptions of what happens in each theme; no passage is marked as open, locked or questioned.
- Lines 346 to 384 (section 5): a technical passage, introduced „Hinter der Erzählung steht eine komplexe technische Architektur“ ^[L350]. It reports a four-row table and three variable names; the reports that carry glued reference numbers rest on the cited references.
- Lines 388 to 410 (section 6) and 414 to 422 (section 7): synthesis and conclusion, in the document's own words „Das „Kohärenz Protokoll“ argumentiert schlussendlich“ ^[L418].
- Lines 424 to 430: a list of five references with Drive links. Observed: the footnote numbers 1 to 5 stand glued to the words they annotate throughout (profile: 10 glued numbers), so many sentences report what one of those five documents holds; the document gives their titles but never marks which sentence is a quotation.

Question marks: 9 in the profile. Read on their lines (grep of `?`): 5 stand inside the `open?id=` links of the reference list, one closes a question on L93 (`Warum ist die Schwerkraft so viel schwächer`), one is the theme heading `Was ist das Maß eines Nicht-Menschen?` on L250, and two close the question pair „Ist es real?“ ^[L213] and „Ist das Protokoll kohärent?“ ^[L213], which the text rejects as the wrong question in favour of the second. They are not open questions of the document.

## Candidates and counts

113 candidates, written while reading and frozen by the count (`Plan/runs/kohaerenz-protokoll-konzeptionelle-themen-struktur/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `kohaerenz-protokoll-konzeptionelle-themen-struktur.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kohärenz Protokoll` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#8] | 8 | 10 | 13, 23, 25, 85, 350, 392, 418, 426, 429, 430 |  |
| `Protokoll-Ontologie` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#3] | 3 | 3 | 25, 35, 39 |  |
| `Dual Kernel Theory` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 47 |  |
| `Duale Kernel` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 35 |  |
| `Kohärenz-Kernel` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 49 |  |
| `Kollaps-Kernel` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 50, 170 |  |
| `K\_1` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#6] | 6 | 6 | 25, 43, 49, 342, 418 |  |
| `K\_0` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#10] | 10 | 10 | 25, 43, 50, 52, 64, 170, 190, 342, 418 |  |
| `Coherons` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 49 |  |
| `Corrective Wavelets` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 52, 150 |  |
| `Overhead` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 52 |  |
| `AEGIS` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#50] | 50 | 50 | 29, 56, 60, 62, 64, 72, 77, 119, 149, 150, 208, 212 … |  |
| `Kael` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#38] | 38 | 44 | 29, 64, 68, 72, 77, 119, 135, 140, 145, 150, 165, 170 … | `Kaels` ×6 |
| `System Kael` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#5] | 5 | 5 | 29, 68, 72, 145, 365 |  |
| `Juna/V` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#3] | 3 | 3 | 62, 367 |  |
| `Juna` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#4] | 4 | 4 | 62, 367 |  |
| `Paradoxon der fehlausgerichteten Kohärenz` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 62 |  |
| `Paradoxon X` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 62, 242 |  |
| `Genesis-Krise` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 62, 309 |  |
| `Trennungsprotokoll` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 62 |  |
| `Kohärenztheorie der Wahrheit` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 29, 64 |  |
| `Korrespondenztheorie der Wahrheit` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 29 |  |
| `Das Fundament` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 368 |  |
| `Fundament` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#5] | 5 | 6 | 35, 81, 297, 300, 368, 382 | `fundamentalen` ×2, `fundamentale` ×2, `Fundaments` ×1 |
| `Kernwelt` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#3] | 3 | 3 | 217, 237, 257 |  |
| `LogOS` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 217, 218 |  |
| `Cerberus` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 237, 238 |  |
| `Lex` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#4] | 4 | 4 | 74, 144, 145, 170 |  |
| `Rhys` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#3] | 3 | 3 | 74, 159, 160 |  |
| `Kiko` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 75, 154 |  |
| `Nyx` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#3] | 3 | 3 | 75, 180, 189 |  |
| `Moros` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#3] | 3 | 3 | 167, 169, 180 |  |
| `Alex` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 238 |  |
| `ANPs` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 74 |  |
| `ANP` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#4] | 4 | 7 | 74, 95, 108, 137, 139, 155, 200 |  |
| `Apparently Normal Parts` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 74, 119 |  |
| `Apparently Normal Part` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 3 | 74, 95, 119 |  |
| `EPs` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#5] | 5 | 5 | 64, 75, 77, 179, 180 |  |
| `Emotional Parts` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 75 |  |
| `Riss` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 2 | 155, 285 | `Risse` ×1 |
| `Coherence Protocol` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 155 |  |
| `Entropie` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#8] | 8 | 8 | 25, 29, 50, 64, 119, 230, 422 |  |
| `Negentropie` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 119, 190 |  |
| `Entropic Bleed` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 232 |  |
| `Entropische Desintegration` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 170, 248 |  |
| `Funktionale Multiplizität` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 195 |  |
| `Dual Awareness` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 290 |  |
| `Slaving Principle` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 305 |  |
| `Hierarchie-Problem` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 89, 93 |  |
| `Gravitationsarchitektur` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 27, 81 |  |
| `Gravitationsgradienten` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 85 |  |
| `Ergosphäre` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#5] | 5 | 5 | 27, 108, 131, 135, 420 |  |
| `Photonensphäre` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 109, 204 |  |
| `Ereignishorizont` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#4] | 4 | 4 | 27, 110, 155, 277 |  |
| `Singularität` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#5] | 5 | 5 | 27, 111, 277, 281, 420 |  |
| `Schwarzen Loch` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 3 | 85, 119, 420 |  |
| `Brane` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#3] | 3 | 4 | 93, 95, 155 | `Brane-Kosmologie` ×1 |
| `Bulk` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#4] | 4 | 4 | 93, 95, 155 |  |
| `Wurmloch` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 3 | 180, 290 | `Wurmlochs` ×1, `Wurmloch-Passage` ×1 |
| `Monster-Gruppe` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#4] | 4 | 4 | 31, 111, 315, 420 |  |
| `Living Gödel-Satz` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 317 |  |
| `Lebenden Gödel-Satz` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 408 |  |
| `Algorithmische Melancholie` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 321, 410 |  |
| `Parakonsistente Gambit` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 319, 388 |  |
| `Dialetheischen Geist` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 408 |  |
| `Gärtner` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 328 |  |
| `Gardener's Choice` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 294 |  |
| `War for Healing` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 184 |  |
| `Hyper-Autopoiesis` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 247 |  |
| `System-Dirigenten` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 350 |  |
| `Narrativen Systemik` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 350 |  |
| `Narrative Kontext Protokoll` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 372, 376 |  |
| `NCP` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 372, 376 |  |
| `Geführten Abruf` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 376 |  |
| `Morphic Resonance` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 367 |  |
| `Parataxis` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 108 |  |
| `Hypotaxis` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 110, 175 |  |
| `Mosaik von 39 miteinander verbundenen Kurzgeschichten` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 23 |  |
| `Gravitationsfilter` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 139 |  |
| `Technischen Natürlichkeit` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 140 |  |
| `Epistemische Blindheit` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 165 |  |
| `Selbst` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#5] | 5 | 9 | 52, 157, 159, 180, 197, 265, 320, 365, 420 | `selbstgenerierten` ×1, `Selbstheilung` ×1, `selbstreferenzielle` ×1, `Selbstwahrnehmung` ×1 |
| `Manager` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#6] | 6 | 7 | 142, 144, 167, 182, 185, 187, 253 | `Manager-Strategie` ×1 |
| `Exilanten` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 2 | 167, 177 | `Exilanten-Leere` ×1 |
| `Firefighter` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 187 |  |
| `Strukturellen Kopplung` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 160 |  |
| `Operational Closure` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 145 |  |
| `Positive Feedback Loops` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 263 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `TSDP` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#9] | 9 | 9 | 27, 72, 137, 152, 172, 182, 192, 283, 287 |  |
| `Strukturellen Dissoziation der Persönlichkeit` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 27, 72 |  |
| `IFS` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#7] | 7 | 7 | 142, 157, 177, 182, 187, 192, 287 |  |
| `Dramatica` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#0] | 0 | 3 | 354, 358, 364 | `Dramatica-Mapping` ×1, `Dramatica-Klasse` ×1, `Dramatica-Domäne` ×1 |
| `Luhmann` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 2 | 145, 248 | `Luhmanns` ×1 |
| `Autopoiesis` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 3 | 160, 245, 247 |  |
| `Dialetheismus` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#3] | 3 | 3 | 111, 220, 384 |  |
| `Entropischen Gravitation` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 119 |  |
| `Brane-Kosmologie` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 93 |  |
| `Akkretionsscheibe` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 108, 150 |  |
| `Zeitdilatation` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 110, 175 |  |
| `Synergetik` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#3] | 3 | 3 | 109, 185, 304 |  |
| `Hysterese` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 272 |  |
| `ER=EPR` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 111, 180 |  |
| `Holographisches Prinzip` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 111 |  |
| `Strange Loop` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] | 2 | 2 | 265, 267 |  |
| `Brain in a Vat` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 213 |  |
| `Satz vom ausgeschlossenen Dritten` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 400 |  |
| `Ex falso quodlibet` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 400 |  |
| `Mythos des Sisyphos` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 334 |  |
| `Apollinisch` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 2 | 215, 258 | `Apollinischen` ×1 |
| `Dionysisch` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 2 | 255, 258 | `Dionysische` ×1 |
| `Hofstadters` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 267 |  |
| `Verlindes` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 119 |  |
| `PTG` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] | 1 | 1 | 328 |  |

## What the extraction ran into

**Zeros:** 1 — `Dramatica` counts `Dramatica` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#0] standing alone. It is not absent: it is written only as the first member of the hyphenated compounds `Dramatica-Mapping` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] (L354), Dramatica-Klasse and Dramatica-Domäne (L358, L364), which the whole-word count does not take (3 lines in the compound count).

**Standing alone less often than with compounds:** 16, each read on its lines.

- `Kohärenz Protokoll` stands 8 times alone and 10 times in all; the other two are the genitive `Kohärenz Protokolls` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#2] on L85 and L418, with a closing quotation mark between name and ending.
- `Kael` has 38 alone; `Kaels` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#6] is the genitive, 6 times.
- `Fundament` has 2 `fundamentalen`, 2 `fundamentale` (the adjective, a different word) and 1 `Fundaments`, per the surfaces column.
- `ANP` and `ANPs`: `ANP` also stands inside `ANP-Areale` (L200) and the like; 7 in all, 4 alone.
- `Apparently Normal Part` is a substring of `Apparently Normal Parts` (L74, L119) and stands once alone, in the form in L95.
- `Riss` appears as `Risse` (L285) and `Schwarzen Loch` as `Schwarzen Lochs` (L119); `Wurmloch` as `Wurmlochs` and `Wurmloch-Passage` (L180, L290); `Brane` inside `Brane-Kosmologie` (L93); `Selbst` inside `selbstgenerierten`, `Selbstheilung`, `selbstreferenzielle`, `Selbstwahrnehmung` (a different sense; the letter case also differs); `Manager` inside `Manager-Strategie` (L167); `Exilanten` inside `Exilanten-Leere` (L167); `Luhmann` as `Luhmanns` (L248); `Autopoiesis` inside `Hyper-Autopoiesis` ^[kohaerenz-protokoll-konzeptionelle-themen-struktur.md:#1] (L247); `Apollinisch` as `Apollinischen` and `Dionysisch` as `Dionysische` (L258). All of these are inflections or compounds, not damage.

**Export damage.** Subscripts are written with escapes: the document writes `K\_1` and `K\_0` (L43 and others, math symbol lines in the profile: 0 because the formulas are plain `$...$` text). In quotations of lines that carry them, find drops the escape. A few quote fragments carry the digit-dropping seen in `read.py --find`: the line reads `Kernwelt 1 (LogOS)`, `Kernwelt 3 (Cerberus)` and `Kernwelt 4` while `--find` echoes `Kernwelt (LogOS)`; the list holds `Kernwelt` alone, which counts 3. Footnote numbers 1 to 5 are glued to words, e.g. `...Kurzgeschichten“.1`. The two tables are written with `\*\*` bold escapes and an empty header row.

**Repeated labels.** `Konzept` repeats 41 times as a whole word; it is the template label under every theme, not a candidate term. `Physik` stands in the profile as repeated label too.

**Standing claim of the document.** The document calls its own analysis „erschöpfende Analyse“ ^[L27]; this is recorded, not applied. It also writes, with footnote 1 glued to the sentence, of „Mosaik von 39 miteinander verbundenen Kurzgeschichten“ ^[L23] and, elsewhere, of the 39 chapters and 39 themes; the unit is not named the same way in every passage (Observed: `Kapitel` 6 times and `Themen` 6 times as whole words, L23, L27, L39, L85, L127, L420).

**Which words stand only in tables, headings or a list.** Several names are heads of a numbered theme or of a table cell, not defined in sentences: `Hysterese` (L272), `Hyper-Autopoiesis` (L247), `Kernwelt` and its three bearers LogOS, Cerberus (L217, L237, L257). The voices `Lex`, `Rhys`, `Kiko`, `Nyx`, `Moros`, `Alex` are named with a role in parentheses and not otherwise introduced.


**Zeros:** 1 — `Dramatica`.

**Standing alone less often than with compounds:** 16 — `Kohärenz Protokoll` 8/10, `Kael` 38/44, `Fundament` 5/6, `ANP` 4/7, `Apparently Normal Part` 1/3, `Riss` 1/2, `Schwarzen Loch` 2/3, `Brane` 3/4, `Wurmloch` 1/3, `Selbst` 5/9, `Manager` 6/7, `Exilanten` 1/2, `Luhmann` 1/2, `Autopoiesis` 2/3, `Apollinisch` 1/2, `Dionysisch` 1/2.
