---
source: Sources/drive/narrative-techniken-fuer-kohaerenz-protokoll.md
drive_id: "1GY8gHHSD50-5byKhrLCWX3Bd6If0151unkE3mCmsKeo"
title: "Narrative Techniken für Kohärenz Protokoll"
category: plot-outline
index_date: "2025-04-27"
extracted: "2026-10-14"
candidates: 80    # the terms capture.py counted
---

# Term census — Narrative Techniken für Kohärenz Protokoll

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py narrative-techniken-fuer-kohaerenz-protokoll`

```
  lines                633  (frontmatter ends at 9)
  body words           14439
  headings             25   bold-only lines 37
  table rows           28   code fences 0
  question marks       58
  backslash escapes    139
  typographic marks    207   ascii quotes 18
  invisible characters none
  math symbol lines    0
  glued ref numbers    152
  repeated labels      none
  longest line         1352 chars
```

## Stance, read per passage

The document speaks as a report that advises on how to write the chapters of the novel; it labels itself „Dieser Bericht dient als umfassende Ressource“ ^[L17] and ends with a numbered reference list under the heading „Referenzen“ ^[L516]. Its sections repeat one pattern: a block headed „Kernkonzepte: Perspektive und Stimme“ ^[L31] reports borrowed concepts from outside texts, then a block headed `Anwendung auf` applies them to the novel in the conditional and the imperative, with `sollte` and `könnte` as its working verbs (counted in `05-verify.txt`).

- L13 to L26, introduction: a statement of purpose and method. The report places itself beside a chapter blueprint it calls `Blaupause`, whose requirements it reports; „Die Blaupause sieht die Möglichkeit vor“ ^[L41] is the document reporting the blueprint, not a statement of the novel.
- L29 to L159, section 1 (voice, environment, metaphors, pacing): proposals for how to write. „Die Instabilität von AEGIS sollte nicht nur als technische Fehlfunktion dargestellt werden“ ^[L338] is the proposal register; the same register runs through all four subsections.
- L161 to L278, section 2 (conceptual core): a framework is reported (Kernkonzepte), then mapped onto the worlds and onto Kael; „AEGIS und die Kernwelt Co₁ verkörpern den extremen apollinischen Drang nach Ordnung“ ^[L175] is a mapping the document proposes, in the indicative.
- L280 to L388, section 3 (character dynamics): includes questions the document asks of its own mapping, such as „Welcher Anteil ist ein Manager?“ ^[L302]; a candidate that stands only in such a question has no reading. The table that follows is offered tentatively: „Die folgende Tabelle bietet eine mögliche Zuordnung als Ausgangspunkt“ ^[L305].
- L390 to L476, section 4 (structure and Gestalt): the three-part structure of the novel is reported from the blueprint: „Die geplante dreiteilige Struktur des Romans“ ^[L404]; three tables carry a comparison, an IFS mapping and a Gestalt mapping.
- L478 to L514, section 5 (synthesis): a summary and, for use, „werden folgende strategische Empfehlungen gegeben“ ^[L497].
- L516 to L632, references: a list of web pages with access dates; none of its entries is a candidate.

## Candidates and counts

80 candidates, written while reading and frozen by the count (`Plan/runs/narrative-techniken-fuer-kohaerenz-protokoll/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `narrative-techniken-fuer-kohaerenz-protokoll.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kael` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#64] | 64 | 174 | 29, 41, 43, 44, 45, 46, 47, 59, 61, 62, 63, 65 … | `Kaels` ×102, `Kael-M` ×5, `Kael-Juna-Einheit` ×1 |
| `Juna` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#7] | 7 | 10 | 99, 103, 105, 146, 363, 365, 406, 408, 455 | `Junas` ×2 |
| `AEGIS` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#73] | 73 | 82 | 29, 41, 45, 46, 47, 51, 59, 64, 69, 93, 94, 104 … | `AEGIS-System` ×3, `AEGIS-Systems` ×2, `AEGIS-Umgebung` ×2, `AEGIS-Kael` ×1 |
| `M` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#34] | 34 | 275 | 19, 27, 41, 43, 45, 46, 48, 59, 61, 63, 65, 69 … |  |
| `Moonshine` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#11] | 11 | 11 | 69, 71, 99, 106, 176, 345, 369, 371, 487, 505 |  |
| `Monstergruppe/M` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 89 |  |
| `Monstergruppe` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 89 |  |
| `K-J Verbindung` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#16] | 16 | 16 | 99, 145, 176, 251, 345, 362, 369, 371, 413, 487, 493, 511 … |  |
| `Kael-M` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#5] | 5 | 5 | 206, 270, 305, 315, 321 |  |
| `Kael-Juna-Einheit` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 455 |  |
| `ICH` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#6] | 6 | 6 | 175, 206, 270, 305, 315, 321 |  |
| `Anteile` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#24] | 24 | 33 | 43, 143, 159, 176, 203, 205, 208, 220, 221, 225, 267, 268 … | `Anteilen` ×8 |
| `Logik-Anteil` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#7] | 7 | 7 | 43, 176, 298, 302, 313, 318 |  |
| `Kind-Anteil` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#4] | 4 | 5 | 43, 298, 303, 312, 318 | `Kind-Anteils` ×1 |
| `Schatten` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#11] | 11 | 15 | 176, 208, 267, 298, 303, 304, 312, 314, 317, 318, 377, 382 … | `Schattens` ×2, `Schatten-Anteile` ×1, `Schattenfiguren` ×1 |
| `Wächterin` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#6] | 6 | 6 | 206, 298, 305, 313, 315, 319 |  |
| `Risse` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#5] | 5 | 5 | 45, 64, 249, 338, 339 |  |
| `Cache Kohärenz` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#16] | 16 | 16 | 44, 71, 75, 79, 85, 159, 203, 204, 257, 261, 276, 484 … |  |
| `Kernwelt` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#11] | 11 | 27 | 59, 61, 62, 63, 67, 95, 144, 175, 177, 222, 239, 253 … | `Kernwelten` ×9, `Kernwelt-Guardians` ×5, `Kernwelt-Guardian` ×2 |
| `Kernwelten` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#9] | 9 | 9 | 59, 67, 239, 253, 337, 407, 493 |  |
| `Kernwelt Co₁` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 61, 175, 255 |  |
| `Kernwelt B` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 62, 175 |  |
| `Kernwelt Ly` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#4] | 4 | 4 | 63, 95, 175, 222 |  |
| `Co₁` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#16] | 16 | 17 | 51, 61, 62, 67, 137, 138, 175, 177, 181, 243, 253, 255 … |  |
| `B` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#42] | 42 | 249 | 17, 21, 25, 41, 45, 47, 48, 51, 55, 61, 62, 63 … |  |
| `Ly` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#10] | 10 | 11 | 51, 63, 67, 95, 175, 222, 245, 253, 381, 589 |  |
| `McL` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#1] | 1 | 2 | 381, 577 |  |
| `AEGIS-System` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#3] | 3 | 5 | 59, 64, 407, 413 | `AEGIS-Systems` ×2 |
| `Innerer Raum Kaels` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 65 |  |
| `Innerer Raum` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 59, 65 |  |
| `Log-Format` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 45, 46 |  |
| `Kernwelt-Guardians` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#5] | 5 | 5 | 144, 177, 373, 386, 489 |  |
| `Kernwelt-Guardian` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#2] | 2 | 7 | 144, 177, 373, 381, 386, 388, 489 | `Kernwelt-Guardians` ×5 |
| `Guardians` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#8] | 8 | 13 | 144, 177, 373, 377, 384, 386, 388, 489 |  |
| `Architekt` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#3] | 3 | 10 | 55, 61, 62, 63, 114, 233, 243, 381, 383, 384 | `Architektur` ×5, `Architekturen` ×2, `architektonischen` ×1 |
| `Netzweber` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 381, 383, 384 |  |
| `Chaos-Regulator` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 381, 383, 384 |  |
| `Möglichkeits-Weber` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 381, 383, 384 |  |
| `Blaupause` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#25] | 25 | 30 | 17, 21, 41, 45, 48, 69, 85, 106, 181, 225, 255, 362 … | `Blaupause78` ×1 |
| `Kapitel-Blaupause` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#4] | 4 | 4 | 17, 482, 499, 514 |  |
| `Kohärenzprotokolle` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#2] | 2 | 3 | 261, 270, 278 |  |
| `Cache-Kohärenz-Metapher` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 276 |  |
| `Sprachwechsel` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 49 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Environmental Storytelling` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#10] | 10 | 10 | 51, 55, 59, 67, 69, 177, 253, 493, 499, 539 |  |
| `Alignment Faking` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 46, 333, 342 |  |
| `Apollinisch/Dionysische` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 163 |  |
| `Apollinische` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#3] | 3 | 6 | 167, 169, 176, 179, 181 | `Apollinischen` ×2, `apollinischen` ×2, `Apollinischem` ×1 |
| `Dionysische` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#4] | 4 | 8 | 163, 167, 169, 179, 181, 485 | `Dionysischen` ×2, `dionysischer` ×1, `dionysisches` ×1, `Dionysischem` ×1 |
| `Dissoziation` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#14] | 14 | 14 | 85, 183, 187, 197, 199, 203, 204, 208, 269, 276, 290, 314 |  |
| `Dissoziativen Identitätsstörung` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 189 |  |
| `Amnesie` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#6] | 6 | 6 | 83, 85, 191, 203, 204, 484 |  |
| `Depersonalisation` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#7] | 7 | 7 | 84, 85, 192, 203, 204, 269, 484 |  |
| `Derealisation` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#4] | 4 | 4 | 84, 85, 193, 204 |  |
| `Holismus` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#10] | 10 | 10 | 75, 89, 210, 214, 221, 225, 369, 493, 506 |  |
| `Reduktionismus` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#8] | 8 | 8 | 210, 214, 220, 225, 369, 487, 506 |  |
| `Emergenz` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#13] | 13 | 13 | 210, 216, 221, 222, 223, 225, 227, 339, 381, 443, 512 |  |
| `Symmetrie` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#35] | 35 | 41 | 61, 71, 110, 115, 116, 229, 233, 235, 239, 243, 244, 245 … | `Symmetrien` ×3, `Symmetrie-Konzept` ×1, `Symmetriekonzepte` ×1, `Symmetriearten` ×1 |
| `Asymmetrie` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#7] | 7 | 7 | 115, 235, 244, 250, 253 |  |
| `Internal Family Systems` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#8] | 8 | 8 | 286, 488, 526, 616, 617, 618, 625, 626 |  |
| `IFS` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#16] | 16 | 25 | 205, 208, 282, 286, 292, 298, 307, 311, 317, 318, 319, 321 … |  |
| `Exiles` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#10] | 10 | 10 | 205, 208, 288, 289, 290, 294, 313, 314, 317, 319 |  |
| `Managers` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 205, 289 |  |
| `Firefighters` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 205, 290 |  |
| `Self-Leadership` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#4] | 4 | 4 | 292, 315, 319, 321 |  |
| `Polarisation` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#5] | 5 | 5 | 294, 318, 488 |  |
| `MESI` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#1] | 1 | 2 | 274, 278 | `MESI-Protokoll` ×1 |
| `Heldenreise` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#14] | 14 | 14 | 377, 396, 398, 399, 400, 408, 411, 413, 421, 490 |  |
| `Heldinnenreise` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#12] | 12 | 12 | 388, 396, 399, 406, 411, 413, 421, 490 |  |
| `Zyklische Narrative` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 400, 421 |  |
| `Schwellenhüter` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#4] | 4 | 4 | 377, 382, 388, 398 |  |
| `Archetypen` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 377, 386, 398 |  |
| `Gestaltprinzipien` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#9] | 9 | 9 | 255, 429, 433, 457, 461, 463, 491, 493 |  |
| `Figur-Grund` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#2] | 2 | 3 | 435, 450, 469 | `Figur-Grund-Trennung` ×1 |
| `Prägnanz` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#5] | 5 | 5 | 235, 255, 440, 454, 474 |  |
| `Geschlossenheit` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#8] | 8 | 11 | 439, 453, 457, 459, 473, 491 |  |
| `Pacing` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#12] | 12 | 15 | 118, 122, 137, 138, 510, 609, 613 | `Pacings` ×2, `Pacing-Techniken` ×1 |
| `Dramatische Ironie` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 129 |  |
| `Cliffhanger` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 131, 154 |  |
| `Psychische Distanz` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 366 |  |
| `Telepathie` ^[narrative-techniken-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 106, 371 |  |

## What the extraction ran into


**Zeros:** 0.

**Standing alone less often than with compounds:** 26 — `Kael` 64/174, `Juna` 7/10, `AEGIS` 73/82, `M` 34/275, `Anteile` 24/33, `Kind-Anteil` 4/5, `Schatten` 11/15, `Kernwelt` 11/27, `Co₁` 16/17, `B` 42/249, `Ly` 10/11, `McL` 1/2, `AEGIS-System` 3/5, `Kernwelt-Guardian` 2/7, `Guardians` 8/13, `Architekt` 3/10, `Blaupause` 25/30, `Kohärenzprotokolle` 2/3, `Apollinische` 3/6, `Dionysische` 4/8, `Symmetrie` 35/41, `IFS` 16/25, `MESI` 1/2, `Figur-Grund` 2/3, `Geschlossenheit` 8/11, `Pacing` 12/15.

Beyond these facts the reading met the following.

The document is a report and names the novel's world only to advise on it. It names no chapter by number; its only structural divisions of the novel are the three parts it reports from the blueprint (Teil 1 to Teil 3, L49 and L406 to L408) and sections of the blueprint it cites (L69, L369). That absence of „Kap N“ is observed, not quoted.

No candidate counts zero. The core worlds are written with a subscript, `Co₁`, and the count finds that form; the plain-digit spelling is not the document's. `McL` stands once in the guardian list, and its second hit in the table is the beginning of an unrelated word in the reference list, not the world name.

Standing alone less often than with compounds has these causes, read from the surfaces column: `Kael`, `Juna` and `AEGIS` also stand in genitive forms and in hyphen compounds (`Kaels`, `Junas`, `AEGIS-System`); `M` and `B` are single letters that sit inside many longer words, so their wider counts are substring noise; `Kernwelt` occurs inside `Kernwelten` and `Kernwelt-Guardians`; `Architekt` occurs inside `Architektur`; `Blaupause` carries a glued reference number, see below; the lens terms (`Apollinische`, `Dionysische`, `Symmetrie`, `IFS`, `MESI`, `Pacing`, `Figur-Grund`, `Geschlossenheit`) also stand in inflected adjective forms or hyphen compounds.

Export damage: footnote numbers are glued to words throughout the text, and one of them sits on the term itself, `Blaupause78` ^[L369] read without its digits; quotations around such a place stop before the digit. Table cells carry escaped asterisks (`\*\*`) in L311 to L315, L421 to L427 and L467 to L476, and quotation marks are mixed typographic and ASCII, as the profile above lists.

A claim about the document's own standing: it presents itself as a resource that supports the blueprint, not as a source of canon; „Dieser Bericht dient als umfassende Ressource“ ^[L17]. The blueprint it reports is another text; this document's description of it is its own claim about that text and is recorded, not applied.

The document names real thinkers, therapists and web pages inside the frameworks it reports; the census leaves those names off the list, and it lists the framework terms under `## lens`.
