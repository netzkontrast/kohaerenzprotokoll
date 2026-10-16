---
source: Sources/drive/kohaerenz-protokoll-agentive-narrative.md
drive_id: "1owe7uOMZe--SNvvgyP9qTSA4ca1Co8jayRA29w6MQms"
title: "Kohärenz Protokoll: Agentive Narrative"
category: plot-outline
index_date: "2025-07-03"
extracted: "2026-10-14"
candidates: 76    # the terms capture.py counted
---

# Term census — Kohärenz Protokoll: Agentive Narrative

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py kohaerenz-protokoll-agentive-narrative`

```
  lines                671  (frontmatter ends at 9)
  body words           7274
  headings             26   bold-only lines 4
  table rows           33   code fences 0
  question marks       14
  backslash escapes    193
  typographic marks    182   ascii quotes 486
  invisible characters none
  math symbol lines    0
  glued ref numbers    108
  repeated labels      Aufgaben x4, Ziel x4, Mitigation x3
  longest line         833 chars
```

## Stance, read per passage

The document is one report in a single register: a technical recommendation that moves from theory to specification to advice. It opens by naming itself: „Das vorliegende Dokument stellt den grundlegenden architektonischen Entwurf für das Projekt“ ^[L22]. Its passages sort into five kinds.

**Plan and recommendation (Teil II to IV).** The report proposes rather than reports: „Es wird daher eine hybride Datenbankstrategie empfohlen“ ^[L314], and for the build order „Eine schrittweise Implementierung wird dringend empfohlen“ ^[L533]. The four build phases (L535 to L567) carry the repeated labels `Aufgaben` ^[kohaerenz-protokoll-agentive-narrative.md:#4] and `Ziel` ^[kohaerenz-protokoll-agentive-narrative.md:#7], which here name fields of a phase; the risk list (L400 to L421) repeats `Mitigation` ^[kohaerenz-protokoll-agentive-narrative.md:#3] as the field after each risk.

**Critique of a prior brief.** The report corrects an earlier design: an assumption of that brief „stellt jedoch einen kritischen Designfehler dar“ ^[L374], and the report's own fix is the symbolic overseer (L378 to L390).

**Mapping (Teil I).** The four layers are assigned to Dramatica components in Table 1, which the report calls not arbitrary: „Diese Zuordnungen sind nicht willkürlich“ ^[L51]. The psychological, logical-systemic, ontological and metaphysical layers are each tied to a borrowed theory (L76 to L116); these theories are lens, applied to the layers.

**Specification.** The JSON schema block (L138 to L289) and the variable dictionary in Table 2 (L294 to L304) are samples of a data format, written in English keys; they define fields for a system, they do not narrate the world. The report also states a standing for the schema: „Das NCP ist die alleinige Quelle der Wahrheit für das gesamte System“ ^[L132]; this is the document's own claim about a proposed schema, recorded here and applied to nothing.

**Reference list (L581 to L670).** 88 numbered web titles with access dates; they contribute no candidates, and the numbers glued into the body text (profile: 108 glued reference numbers) point at them.


## Candidates and counts

76 candidates, written while reading and frozen by the count (`Plan/runs/kohaerenz-protokoll-agentive-narrative/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `kohaerenz-protokoll-agentive-narrative.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kael` ^[kohaerenz-protokoll-agentive-narrative.md:#16] | 16 | 20 | 57, 76, 80, 82, 94, 104, 177, 299, 300, 388, 446, 519 … | `Kaels` ×4, `kaelState` ×2 |
| `AEGIS` ^[kohaerenz-protokoll-agentive-narrative.md:#15] | 15 | 16 | 57, 88, 92, 94, 104, 178, 301, 302, 446, 520, 544, 548 | `aegisState` ×2, `AEGIS-Storyform` ×1 |
| `Juna/V` ^[kohaerenz-protokoll-agentive-narrative.md:#9] | 9 | 9 | 57, 98, 102, 104, 105, 303, 522, 557 |  |
| `Juna` ^[kohaerenz-protokoll-agentive-narrative.md:#9] | 9 | 11 | 57, 98, 102, 104, 105, 179, 303, 522, 557 | `JunaV` ×2, `junaVState` ×2 |
| `Das Fundament` ^[kohaerenz-protokoll-agentive-narrative.md:#6] | 6 | 6 | 57, 109, 115, 523, 557 |  |
| `Fundament` ^[kohaerenz-protokoll-agentive-narrative.md:#10] | 10 | 12 | 22, 34, 57, 102, 109, 115, 116, 180, 304, 523, 557 | `Fundaments` ×2, `fundamentalen` ×2, `fundamentState` ×2, `fundamentale` ×1 |
| `Kohärenz Protokoll` ^[kohaerenz-protokoll-agentive-narrative.md:#5] | 5 | 9 | 13, 22, 26, 51, 115, 145, 349, 575, 579 |  |
| `Narrative Kontext Protokoll` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 128 |  |
| `NCP` ^[kohaerenz-protokoll-agentive-narrative.md:#7] | 7 | 8 | 51, 83, 128, 132, 134, 294, 539 |  |
| `System-Dirigent` ^[kohaerenz-protokoll-agentive-narrative.md:#2] | 2 | 3 | 24, 42, 146 | `System-Dirigenten` ×1 |
| `System-Dirigenten` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 42 |  |
| `Theorie der Narrativen Systemik` ^[kohaerenz-protokoll-agentive-narrative.md:#2] | 2 | 2 | 24, 34 |  |
| `dramaturgischen Aufseher` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 2 | 51, 374 |  |
| `Dramaturgische Aufseher` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 370 |  |
| `Aufseher` ^[kohaerenz-protokoll-agentive-narrative.md:#4] | 4 | 7 | 51, 370, 374, 378, 404, 412, 557 | `Aufsehers` ×2 |
| `Prompt-Kaskade` ^[kohaerenz-protokoll-agentive-narrative.md:#7] | 7 | 7 | 312, 323, 327, 412, 474, 496, 539 |  |
| `worldState` ^[kohaerenz-protokoll-agentive-narrative.md:#14] | 14 | 16 | 72, 161, 240, 292, 294, 312, 316, 319, 329, 332, 382, 400 … | `worldState-Variablen` ×1, `worldState-JSON-Objekt` ×1 |
| `interferenceRules` ^[kohaerenz-protokoll-agentive-narrative.md:#9] | 9 | 9 | 72, 116, 156, 304, 355, 381, 449, 548, 557 |  |
| `interferenceRule` ^[kohaerenz-protokoll-agentive-narrative.md:#3] | 3 | 12 | 72, 116, 134, 156, 159, 235, 304, 355, 381, 449, 548, 557 | `interferenceRules` ×9 |
| `Story Mind` ^[kohaerenz-protokoll-agentive-narrative.md:#3] | 3 | 3 | 38, 42, 64 |  |
| `Throughlines` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 42 |  |
| `State Analysis Prompt` ^[kohaerenz-protokoll-agentive-narrative.md:#2] | 2 | 2 | 317, 329 |  |
| `Context Compression Prompt` ^[kohaerenz-protokoll-agentive-narrative.md:#3] | 3 | 3 | 330, 349, 353 |  |
| `Narrative Generation Prompt` ^[kohaerenz-protokoll-agentive-narrative.md:#2] | 2 | 2 | 331, 388 |  |
| `State Update Prompt` ^[kohaerenz-protokoll-agentive-narrative.md:#4] | 4 | 4 | 332, 382, 404, 421 |  |
| `activeFocalSystem` ^[kohaerenz-protokoll-agentive-narrative.md:#3] | 3 | 3 | 170, 355, 517 |  |
| `userModel` ^[kohaerenz-protokoll-agentive-narrative.md:#3] | 3 | 4 | 187, 416, 420, 421 | `userModel-Historie` ×1 |
| `narrativeInstruction` ^[kohaerenz-protokoll-agentive-narrative.md:#2] | 2 | 2 | 388, 408 |  |
| `Kael.integrationProgress` ^[kohaerenz-protokoll-agentive-narrative.md:#2] | 2 | 2 | 299, 388 |  |
| `AEGIS.entropyLevel` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 301 |  |
| `AEGIS.protocolAdherence` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 302 |  |
| `JunaV.resonanceFrequency` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 303 |  |
| `Fundament.activeBinaryOpposition` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 304 |  |
| `Psychologische Ebene` ^[kohaerenz-protokoll-agentive-narrative.md:#2] | 2 | 2 | 57, 76 |  |
| `Logisch-Systemische Ebene` ^[kohaerenz-protokoll-agentive-narrative.md:#2] | 2 | 2 | 57, 88 |  |
| `Ontologische Ebene` ^[kohaerenz-protokoll-agentive-narrative.md:#2] | 2 | 2 | 57, 98 |  |
| `Metaphysische Ebene` ^[kohaerenz-protokoll-agentive-narrative.md:#2] | 2 | 2 | 57, 109 |  |
| `Semantische Drift` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 400 |  |
| `Kontextfenster-Kollaps` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 416 |  |
| `Inter-Agenten-Fehlausrichtung` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 408 |  |
| `Zustands-Audits` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 404 |  |
| `narrative Gravitationsmechanik` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 404 |  |
| `Decaying-Resolution Memory` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 420 |  |
| `Geführter Abruf` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 355 |  |
| `Geführte Korrektur` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 388 |  |
| `Harte Zurückweisung` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 387 |  |
| `Hybridarchitektur` ^[kohaerenz-protokoll-agentive-narrative.md:#2] | 2 | 2 | 378, 577 |  |
| `Constraint Solver` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 378 |  |
| `Answer Set Programming` ^[kohaerenz-protokoll-agentive-narrative.md:#6] | 6 | 6 | 378, 577, 637, 640, 644, 646 |  |
| `ASP` ^[kohaerenz-protokoll-agentive-narrative.md:#2] | 2 | 9 | 378, 382, 388, 390, 400, 412, 557 |  |
| `clingo` ^[kohaerenz-protokoll-agentive-narrative.md:#7] | 7 | 7 | 380, 382, 641, 642, 643 |  |
| `Retrieval-Augmented Generation` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 351 |  |
| `RAG` ^[kohaerenz-protokoll-agentive-narrative.md:#3] | 3 | 6 | 351, 412, 507, 577, 632, 633 |  |
| `Desire Paths` ^[kohaerenz-protokoll-agentive-narrative.md:#2] | 2 | 2 | 448 |  |
| `SCORE-Framework` ^[kohaerenz-protokoll-agentive-narrative.md:#2] | 2 | 2 | 435 |  |
| `LangGraph` ^[kohaerenz-protokoll-agentive-narrative.md:#3] | 3 | 3 | 496, 502 |  |
| `Redis` ^[kohaerenz-protokoll-agentive-narrative.md:#10] | 10 | 10 | 316, 319, 616, 617, 618, 619, 620, 621 | `redis-vs-mongodb` ×2, `redis-vs-mongodb-which-database-is-right-for-you` ×1 |
| `MongoDB` ^[kohaerenz-protokoll-agentive-narrative.md:#8] | 8 | 9 | 318, 319, 616, 617, 618, 619, 620, 621 | `mongodb-vs-redis` ×2, `MongoDB-Collection` ×1 |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Dramatica` ^[kohaerenz-protokoll-agentive-narrative.md:#13] | 13 | 20 | 38, 42, 44, 53, 150, 381, 438, 523, 539, 577, 583, 584 … | `dramaticaStoryform` ×3, `Dramatica-Theorie` ×2, `Dramatica-Storyforms` ×2, `Dramatica-Komponenten-Mapping` ×1 |
| `Jungsche Schattenintegration` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 82 |  |
| `Schatten` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 2 | 82 | `Schattenintegration` ×1 |
| `Internal Family Systems` ^[kohaerenz-protokoll-agentive-narrative.md:#3] | 3 | 3 | 84, 597, 598 |  |
| `IFS` ^[kohaerenz-protokoll-agentive-narrative.md:#4] | 4 | 5 | 84, 300, 596, 597 |  |
| `Manager` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 84 |  |
| `Firefighter` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 84 |  |
| `Exiles` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 84 |  |
| `Selbst` ^[kohaerenz-protokoll-agentive-narrative.md:#3] | 3 | 4 | 83, 84, 300 | `Selbstakzeptanz` ×1 |
| `verwundeten Heilers` ^[kohaerenz-protokoll-agentive-narrative.md:#2] | 2 | 2 | 94 |  |
| `Morphische Resonanz` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 104 |  |
| `Transzendentalismus` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 105 |  |
| `Über-Seele` ^[kohaerenz-protokoll-agentive-narrative.md:#2] | 2 | 2 | 105 |  |
| `Lévi-Strauss'scher Strukturalismus` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 115 |  |
| `Mythemen` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 115 |  |
| `binären Oppositionen` ^[kohaerenz-protokoll-agentive-narrative.md:#2] | 2 | 2 | 115 |  |
| `Perceive-Analyze-Plan-Act` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 327 |  |
| `Agent Drift` ^[kohaerenz-protokoll-agentive-narrative.md:#1] | 1 | 1 | 400 |  |

## What the extraction ran into


**Zeros:** 0.

**Standing alone less often than with compounds:** 19 — `Kael` 16/20, `AEGIS` 15/16, `Juna` 9/11, `Fundament` 10/12, `Kohärenz Protokoll` 5/9, `NCP` 7/8, `System-Dirigent` 2/3, `dramaturgischen Aufseher` 1/2, `Aufseher` 4/7, `worldState` 14/16, `interferenceRule` 3/12, `userModel` 3/4, `ASP` 2/9, `RAG` 3/6, `MongoDB` 8/9, `Dramatica` 13/20, `Schatten` 1/2, `IFS` 4/5, `Selbst` 3/4.

**Reading the zeros and the gaps.** No candidate counts zero. The 19 terms that stand alone less often than inside compounds are explained by inflection and compounding, not by damage: the genitive `Kaels` ^[kohaerenz-protokoll-agentive-narrative.md:#4] and the state names such as `kaelState` ^[kohaerenz-protokoll-agentive-narrative.md:#2] lift `Kael`; the plural `interferenceRules` ^[kohaerenz-protokoll-agentive-narrative.md:#9] accounts for most of the 3/12 of `interferenceRule`; `Fundaments` ^[kohaerenz-protokoll-agentive-narrative.md:#2] and the type name `fundamentState` ^[kohaerenz-protokoll-agentive-narrative.md:#2] lift `Fundament`; the genitive `Aufsehers` ^[kohaerenz-protokoll-agentive-narrative.md:#2] lifts `Aufseher`; `dramaticaStoryform` ^[kohaerenz-protokoll-agentive-narrative.md:#3] and the hyphen compounds with `Dramatica` lift that term; `MongoDB` and `Redis` also stand inside lower-cased URL slugs of the reference list (the draft's compound lists name them).

**Export damage met.** The conversion left 193 backslash escapes (`\*\*` around bold cell text in the tables, `\_` in field names, `\#` and `\[` in the schema), 108 reference numbers glued to the words they annotate, and in the JSON block (L138 to L289) several array values lost entirely: `"enum":,` at L171 and `"required":,` at L221 have no value, and `"required":` at L182, L185, L269, L276 and L286 end the line empty. Digits glued to words are also lost in running text: the model name `Claude 3.7 Sonnet` ^[kohaerenz-protokoll-agentive-narrative.md:#2] loses its inner digit at L474 and a section number is lost at L566, so those forms are not quotable whole. The tables are written with pipes (L55 to L62, L296 to L304, L480 to L487, L500 to L507), the first with an empty header row. A French-named lens term keeps its apostrophe form, `Lévi-Strauss'scher Strukturalismus`, as an adjective; it is listed as the document writes it. Two surfaces of one name stand in the list on purpose, `Dramaturgische Aufseher` (heading, capitalised) and `dramaturgischen Aufseher` (running text), because the count is case- and inflection-bound.

**Voice and two layers.** Two languages run together: German prose with English field names, English prompt names (`State Analysis Prompt`, `Context Compression Prompt`) and English JSON descriptions. Several candidates stand only in the schema or in a table (`AEGIS.entropyLevel`, `JunaV.resonanceFrequency`, `Fundament.activeBinaryOpposition`), where they name a variable, not a thing of the story. The document does not write a speaker's name for the quoted prompts; they are sample texts for the system.

**The document's own standing.** It describes itself as the basis for development: „Das vorliegende Dokument stellt den grundlegenden architektonischen Entwurf für das Projekt“ ^[L22]. It also grants the schema a rank of its own at L132 (see stance). Both are recorded, neither applied.
