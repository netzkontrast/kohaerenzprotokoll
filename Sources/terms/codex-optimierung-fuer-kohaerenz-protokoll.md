---
source: Sources/drive/codex-optimierung-fuer-kohaerenz-protokoll.md
drive_id: "1ErrA2EisDX9xQV9kbm1sHlEP1dGuv00CQJ1wv4-nqyQ"
title: "Codex-Optimierung für „Kohärenz Protokoll“"
category: kernkonzept
index_date: "2025-04-29"
extracted: "2026-10-15"
candidates: 47    # the terms capture.py counted
---

# Term census — Codex-Optimierung für „Kohärenz Protokoll“ ^[L11]

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py codex-optimierung-fuer-kohaerenz-protokoll`

```
  lines                583  (frontmatter ends at 9)
  body words           6133
  headings             16   bold-only lines 12
  table rows           36   code fences 0
  question marks       17
  backslash escapes    315
  typographic marks    35   ascii quotes 244
  invisible characters none
  math symbol lines    0
  glued ref numbers    36
  repeated labels      none
  longest line         1231 chars
```

## Stance, read per passage

The document is a report with a proposed design; it does not narrate the novel. Passage by passage:

- **Introduction, L13–L15.** A report on a research commission: „Dieser Bericht adressiert den Forschungsauftrag“ ^[L15]. It describes the novel's setting only as a reason for needing compact context for a text generator (protagonist, AI antagonist, simulated worlds).
- **Part A, L17–L66 — analysis.** An analysis of seven „Ebene“ headings: narrative, character (POV), character (others), world, conceptual, thematic, stylistic, methodical. The novel's names stand as examples inside these levels, for instance „externe Figuren wie Juna“ ^[L38]. Section A.2 is a discussion of how the levels interact.
- **Part B.1, L74–L81 — assessment, hedged.** The existing templates are judged with „vermutlich“ and „unklar“ ^[L76]; the section closes „Fazit der Bewertung“ ^[L81].
- **Part B.2–B.3, L83–L155 — proposal.** A design in principles and two tables of field names; the fields are offered: „werden folgende spezifische Custom Details für die relevanten Codex-Eintragstypen vorgeschlagen“ ^[L123]. The example values in the tables (world metaphors, emotions, relations) are sample entries of the proposal, not statements about the novel.
- **Part C.1–C.2, L159–L312 — template and strategy.** A prompt template in code form (L169–L252) with placeholders and conditional blocks, then a mechanism list and three priority tiers. Its text addresses a writing model, not a reader of the novel.
- **Part C.3, L314–L517 — worked examples.** Two scenes marked as invented: „anhand von zwei hypothetischen Szenen-Beats“ ^[L316]; the codex data of each is headed „Hypothetisch gezogene Codex-Daten“ ^[L333], and each ends with a prediction headed „Erwarteter Output-Fokus“ ^[L407]. Everything the examples say about Kael, AEGIS and the worlds is hypothetical in the document's own label.
- **Part 4, L519–L555 — recommendations.** Imperative advice, headed „Empfehlungen für die Codex-Optimierung“ ^[L531].
- **Part 5 and references, L557–L582.** An optional appendix offered „Bei Bedarf“ ^[L559], then twenty numbered web references, each with an access date; the sources of the Part A and B claims are these third-party pages, marked by glued reference numbers.

No passage is marked as a lock or as canon, and the document names no chapter by number (`Kap` standing alone: 0).

## Candidates and counts

47 candidates, written while reading and frozen by the count (`Plan/runs/codex-optimierung-fuer-kohaerenz-protokoll/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `codex-optimierung-fuer-kohaerenz-protokoll.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kael` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#12] | 12 | 13 | 26, 38, 94, 111, 133, 150, 318, 324, 402, 409, 415, 510 … | `Kaels` ×1 |
| `AEGIS` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#32] | 32 | 33 | 15, 38, 50, 62, 63, 96, 103, 112, 114, 135, 139, 147 … | `AEGIS-Projektion` ×1 |
| `Juna` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 38, 112, 139 |  |
| `Kael System` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 94, 111, 534 |  |
| `Der Wächter` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#4] | 4 | 4 | 318, 329, 337, 370 |  |
| `Wächter` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#7] | 7 | 8 | 138, 318, 324, 329, 337, 370, 402, 407 | `Wächters` ×1 |
| `Das Kind` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#6] | 6 | 6 | 409, 415, 420, 428, 471, 510 |  |
| `Anteil` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#41] | 41 | 60 | 26, 30, 31, 32, 34, 38, 52, 59, 60, 63, 64, 66 … | `Anteile` ×4, `Anteils` ×2, `Anteilen` ×1, `Anteils-Einträge` ×1 |
| `Anteile` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#4] | 4 | 5 | 26, 38, 60, 534, 550 | `Anteilen` ×1 |
| `ANP` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#5] | 5 | 5 | 30, 132, 318, 341, 371 |  |
| `EP` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#7] | 7 | 7 | 30, 101, 111, 132, 409, 432, 472 |  |
| `Anscheinend Normale Persönlichkeit` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 30 |  |
| `Emotionale Persönlichkeit` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 30 |  |
| `TSDP-System` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 30 |  |
| `TSDP-Dynamiken` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 50, 62 |  |
| `TSDP-basiert` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 15 |  |
| `TSDP-Rolle` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 284 |  |
| `Kernwelt` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#16] | 16 | 18 | 43, 44, 63, 95, 101, 113, 141, 318, 409, 415, 420, 450 … | `Kernwelt-Eintrag` ×1, `Kernwelten` ×1 |
| `Kernwelten` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 550 |  |
| `Kernwelt B` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#6] | 6 | 6 | 409, 415, 420, 450, 488, 510 |  |
| `Welt B` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 513, 515 |  |
| `Co₁` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#10] | 10 | 10 | 43, 101, 113, 318, 324, 329, 348, 378, 402, 407 |  |
| `McL` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 43 |  |
| `Ly` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 43 |  |
| `Riss` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#12] | 12 | 20 | 46, 59, 113, 142, 147, 225, 226, 297, 318, 324, 329, 353 … | `Risse` ×6, `Rissen` ×1, `Risses` ×1 |
| `Risse` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#6] | 6 | 8 | 46, 113, 142, 147, 297, 353, 380, 407 | `Rissen` ×1, `Risses` ×1 |
| `Paradoxon X` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#21] | 21 | 21 | 50, 62, 96, 103, 114, 145, 222, 223, 297, 420, 444, 446 … |  |
| `Fundaments` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 50 |  |
| `Fundament` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] | 1 | 2 | 50, 114 | `Fundaments` ×1 |
| `Cache Kohärenz` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 50 |  |
| `Switching` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 50 |  |
| `Co-Präsenz` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 50 |  |
| `Heldinnenreise` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 25 |  |
| `Heldenreise` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 25, 61 |  |
| `Novelcrafter` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#22] | 22 | 26 | 15, 79, 89, 90, 103, 159, 163, 257, 261, 269, 528, 541 … | `Novelcrafter-Funktionen` ×2, `Novelcrafter-Funktion` ×1, `Novelcrafter-Begriffe` ×1, `novelcrafter-review` ×1 |
| `Codex` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#13] | 13 | 55 | 11, 15, 19, 68, 70, 76, 83, 85, 90, 101, 102, 103 … | `Codex-Struktur` ×14, `Codex-Eintrag` ×9, `Codex-Einträge` ×7, `Codex-Daten` ×3 |
| `Custom Details` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#15] | 15 | 15 | 78, 89, 103, 121, 123, 125, 258, 270, 333, 424, 527, 533 … |  |
| `Master-Prompt` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#6] | 6 | 16 | 15, 89, 159, 163, 165, 265, 270, 517, 528, 541, 550, 552 … | `Master-Prompt-Struktur` ×5, `Master-Prompts` ×2, `Master-Prompt-Vorlage` ×1, `Master-Prompt-Strategie` ×1 |
| `Voice Sheet` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] | 1 | 2 | 116, 552 |  |
| `Scene Beat Completion` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 163, 165 |  |
| `Lore` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#8] | 8 | 8 | 103, 114, 145, 358, 440, 460, 533 |  |
| `Style Guide` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#5] | 5 | 5 | 116, 117, 153, 182, 271 |  |
| `Genre Guide` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 152, 181, 271 |  |
| `Minimal Sufficiency` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 276 |  |
| `Minimalität` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#4] | 4 | 5 | 77, 87, 88, 270, 527 | `Minimalitätsstrategie` ×1 |
| `Suffizienz` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 76, 88, 527 |  |
| `KI-Zugänglichkeit` ^[codex-optimierung-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 78, 89, 527 |  |

## What the extraction ran into

**TSDP.** The bare `TSDP` stands alone 0 times case-sensitively (`read.py --count`: 0 whole word, 6 case-insensitive, 10 with compounds). Upper-case `TSDP` occurs only in compounds, so the compounds `TSDP-System`, `TSDP-Dynamiken`, `TSDP-basiert` and `TSDP-Rolle` are listed as written; the lower-case occurrences are inside export-mangled field and tag names. The document does not expand the abbreviation `TSDP`; it expands only `ANP` and `EP` ^[L30].

**Standing alone less often than with compounds (14 rows).** These are compounds and inflections, not damage: `Codex` is 13 alone and 55 with `Codex-Struktur`, `Codex-Eintrag`, `Codex-Einträge` and `Codex-Daten`; `Anteil` is 41 alone and 60 with `Anteile`, `Anteils`, `Anteilen` and `Anteils-Einträge`; `Master-Prompt` has 16 with `Master-Prompt-Struktur`, `Master-Prompts` and others; `Riss` includes `Risse`, `Rissen` and `Risses`; `Kael` includes `Kaels`; `Wächter` includes `Wächters`; `Fundament` includes the genitive `Fundaments`, which is why both are listed.

**Export damage.** The profile counts 315 backslash escapes and 36 glued reference numbers. The export escapes underscores and asterisks, so the field names the tables write (the `Anteil_…`, `Welt_…`, `Konzept_…` families) stand in the file with doubled backslashes and are not listed; `read.py` strips the underscores in its output, so a quotation of such a name cannot be checked against the raw line. The subscript in the world name `Co₁` is kept as the document writes it. Tables are flattened with pipes, and rows continue below a first cell that is empty (L133 to L139). The prompt template (L169 to L252) is an unfenced code block whose braces, hash marks and angle brackets are escaped. Several lines show gaps where the export dropped placeholder text, for instance L197 `{context.povCharacter.customDetail}` without its field name, and L249, where the sentence about the word count has lost its number and reads `Schreibe ca. Wörter` ^[L249].

**Names the document gives as bare letters.** L43 writes the world names as the list `Co₁, McL, B, Ly` ^[L43]; `McL` and `Ly` stand once each and are not defined; `B` is listed only as `Kernwelt B` and `Welt B` because the single letter stands 39 times, mostly as a letter inside other names.

**Terms of a tool, not of the novel.** `Novelcrafter`, `Codex`, `Custom Details`, `Master-Prompt`, `Voice Sheet`, `Scene Beat Completion`, `Lore`, `Style Guide` and `Genre Guide` are the writing software's or the report's own vocabulary; `Minimal Sufficiency`, `Minimalität`, `Suffizienz` and `KI-Zugänglichkeit` are principles the report states for its design.

**Terms named without explanation.** `Fundament`, `Cache Kohärenz`, `Switching` and `Co-Präsenz` stand once each, in one list ^[L50], and no other line of the document explains them (`read.py --count`: 1 each). `Paradoxon X` recurs 21 times; the keywords the examples give it are „Widerspruch, Systemfehler, Unlösbare Aufgabe“ ^[L464], inside the hypothetical codex data of the second example.

**Self-standing claims.** The document makes no claim of canon or authority for itself; its own hedges are `vermutlich` (1, at L76) and `wahrscheinlich` (4, among them L81).

**Zeros:** 0.

**Standing alone less often than with compounds:** 14 — `Kael` 12/13, `AEGIS` 32/33, `Wächter` 7/8, `Anteil` 41/60, `Anteile` 4/5, `Kernwelt` 16/18, `Riss` 12/20, `Risse` 6/8, `Fundament` 1/2, `Novelcrafter` 22/26, `Codex` 13/55, `Master-Prompt` 6/16, `Voice Sheet` 1/2, `Minimalität` 4/5.
