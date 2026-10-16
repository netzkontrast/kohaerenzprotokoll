---
source: Sources/drive/projekt-ockham-narrative-systemik-reduktion.md
drive_id: "1SFuKU0hZCgwwiHgYuCba7J8WFbszyxh6d1RnNEpekjY"
title: "Projekt Ockham: Narrative Systemik Reduktion"
category: plot-outline
index_date: "2026-01-02"
extracted: "2026-10-14"
candidates: 110    # the terms capture.py counted
---

# Term census — Projekt Ockham: Narrative Systemik Reduktion

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py projekt-ockham-narrative-systemik-reduktion`

```
  lines                445  (frontmatter ends at 9)
  body words           4678
  headings             34   bold-only lines 1
  table rows           9   code fences 0
  question marks       15
  backslash escapes    151
  typographic marks    227   ascii quotes 92
  invisible characters none
  math symbol lines    0
  glued ref numbers    51
  repeated labels      none
  longest line         919 chars
```

## Stance, read per passage

The document is a report („Dieser Bericht liefert eine erschöpfende technische und theoretische Dekonstruktion“ ^[L21]) in numbered sections, 1.0 to 8.0, with a technical appendix and a numbered reference list. It speaks in four registers.

**Programme and definition (L15 to L21, L35, L44).** It states a mandate for `Projekt Ockham` and defines its own terms in bold, with abbreviations in parentheses (L35 sets the `Dual-Kernel-Theorie (DKT)`). It marks its argument as a postulate: „Projekt Ockham postuliert daher“ ^[L31].

**Report of design decisions (L55 to L73).** A past-tense account of the failure of `NovelOS 1.0` and a labelled „Entscheidung für NovelOS“ ^[L73]; the framework comparison at L69 to L71 reports properties of three external tools.

**Specification by example (L138 to L216, L332 to L406).** YAML, Python, JSON and shell blocks, each introduced by a label and followed by a paragraph headed „Operative Nutzung“ ^[L167] (twice in the document; the second at L191). The schema values for „Kael“ and „Juna“ are sample data inside these blocks; the appendix says its specifications were taken from other documents: „Um die sofortige Implementierung zu erleichtern, wurden die folgenden Spezifikationen aus den „Golden Source“-Dokumenten extrahiert.“ is the line, quoted only as the document writes it at ^[L330]. That is the document's own claim about its sources; it is recorded, not applied.

**Case study (L301 to L318).** The document applies the system to the novel in a scenario („Das Szenario“ ^[L305]), a mapping of figures to kernels, and a simulated run with a stated result. The operative-conflict paragraph at L40 is introduced by „Der operative Konflikt“ ^[L40].

**Questions.** The 15 question marks stand on lines 25, 92, 132, 224, 266, 270, 283 and 290 in the text (example questions and rhetorical questions such as „Warum halluzinieren LLMs Inkonsistenzen über die Zeit?“ ^[L25] and „Soll Kael kämpfen oder fliehen?“ ^[L266]) and on lines 420, 432, 435 and 440 in the reference list (a URL and titles). A term that stands only inside such a question has no reading.


## Candidates and counts

110 candidates, written while reading and frozen by the count (`Plan/runs/projekt-ockham-narrative-systemik-reduktion/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `projekt-ockham-narrative-systemik-reduktion.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Projekt Ockham` ^[projekt-ockham-narrative-systemik-reduktion.md:#10] | 10 | 10 | 11, 19, 31, 40, 53, 120, 264, 303, 322 |  |
| `NovelOS` ^[projekt-ockham-narrative-systemik-reduktion.md:#24] | 24 | 28 | 21, 35, 37, 40, 44, 47, 55, 57, 61, 63, 67, 69 … | `NovelOS-Architektur` ×2, `NovelOS-System` ×1, `NovelOS-Reaktion` ×1 |
| `NovelOS 1.0` ^[projekt-ockham-narrative-systemik-reduktion.md:#3] | 3 | 3 | 21, 55, 57 |  |
| `NovelOS 2.0` ^[projekt-ockham-narrative-systemik-reduktion.md:#6] | 6 | 6 | 21, 61, 63, 67, 326, 415 |  |
| `Epistemische Isolation` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 322 |  |
| `Epistemischen Isolation` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 21, 63 |  |
| `Epistemische Kontamination` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 59 |  |
| `Epistemische Konsistenz` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 167 |  |
| `Coherence Protocol` ^[projekt-ockham-narrative-systemik-reduktion.md:#3] | 3 | 3 | 21, 414, 444 |  |
| `Kohärenz Protokoll` ^[projekt-ockham-narrative-systemik-reduktion.md:#4] | 4 | 4 | 35, 46, 301, 303 |  |
| `Dual-Kernel-Theorie` ^[projekt-ockham-narrative-systemik-reduktion.md:#3] | 3 | 3 | 21, 33, 35 |  |
| `DKT` ^[projekt-ockham-narrative-systemik-reduktion.md:#3] | 3 | 3 | 33, 35 |  |
| `Dual-Kernel-Theorie (DKT)` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 33, 35 |  |
| `Dual Kernel` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 326 |  |
| `K\_1` ^[projekt-ockham-narrative-systemik-reduktion.md:#13] | 13 | 13 | 21, 37, 40, 69, 92, 104, 309, 317, 326 |  |
| `K\_0` ^[projekt-ockham-narrative-systemik-reduktion.md:#10] | 10 | 10 | 21, 38, 40, 70, 104, 310, 326 |  |
| `Kohärenz-Kernel` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 37 |  |
| `Kollaps-Kernel` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 38 |  |
| `Kernel` ^[projekt-ockham-narrative-systemik-reduktion.md:#6] | 6 | 11 | 21, 33, 35, 37, 38, 40, 309, 310, 326 |  |
| `ARCHON` ^[projekt-ockham-narrative-systemik-reduktion.md:#3] | 3 | 3 | 21, 102, 104 |  |
| `ARCHON Stack` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 104 |  |
| `Narrative Reliability Engineer` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 4 | 13, 21, 320, 324 |  |
| `Narrative Reliability Engineering` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 13, 320 |  |
| `Narrative Entropie` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 17 |  |
| `Kontext-Fäule` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 27, 29 |  |
| `Context Rot` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 29 |  |
| `Context Engineering` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 31 |  |
| `Aktives Vergessen` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 260 |  |
| `Hard Canon` ^[projekt-ockham-narrative-systemik-reduktion.md:#5] | 5 | 5 | 37, 115, 309, 380, 406 |  |
| `Soft Canon` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 38, 310 |  |
| `Storyform` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 37 |  |
| `Storytelling` ^[projekt-ockham-narrative-systemik-reduktion.md:#3] | 3 | 3 | 38, 264, 413 |  |
| `Muse` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 38, 40 |  |
| `Architekt` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 13 | 13, 21, 23, 35, 37, 40, 44, 63, 73, 100, 295, 415 | `Architektur` ×4, `Architekten` ×3 |
| `Mediator` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 40 |  |
| `Isomorphie-Prinzip` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 44 |  |
| `Isomorphie` ^[projekt-ockham-narrative-systemik-reduktion.md:#3] | 3 | 4 | 42, 44, 49, 307 | `Isomorphie-Prinzip` ×1 |
| `DIS` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 46 |  |
| `ANP` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 46, 47 |  |
| `EP` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 46, 47 |  |
| `Kael` ^[projekt-ockham-narrative-systemik-reduktion.md:#20] | 20 | 22 | 79, 84, 90, 97, 98, 126, 127, 167, 226, 248, 258, 259 … | `Kaels` ×1 |
| `Juna` ^[projekt-ockham-narrative-systemik-reduktion.md:#5] | 5 | 5 | 79, 127, 155, 167, 276 |  |
| `AEGIS` ^[projekt-ockham-narrative-systemik-reduktion.md:#5] | 5 | 6 | 154, 305, 309, 314, 317 | `AEGIS-Agent` ×1 |
| `Librarian` ^[projekt-ockham-narrative-systemik-reduktion.md:#22] | 22 | 23 | 37, 73, 115, 191, 218, 220, 241, 246, 248, 254, 256, 268 … | `Librarian-Prozess` ×1 |
| `The Librarian` ^[projekt-ockham-narrative-systemik-reduktion.md:#4] | 4 | 4 | 37, 115, 218, 290 |  |
| `Sensory Drafter` ^[projekt-ockham-narrative-systemik-reduktion.md:#6] | 6 | 6 | 47, 113, 191, 289, 310, 404 |  |
| `System Architect` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 47, 324 |  |
| `Narrative Director` ^[projekt-ockham-narrative-systemik-reduktion.md:#3] | 3 | 3 | 57, 111, 288 |  |
| `Brainstormer` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 112 |  |
| `Weaver` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 116 |  |
| `Ontologist` ^[projekt-ockham-narrative-systemik-reduktion.md:#3] | 3 | 3 | 287, 400 |  |
| `Ontologist Agent` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 287 |  |
| `Editor / Critic` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 114 |  |
| `Character Bots` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 75 |  |
| `Environment Loop` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 86, 88 |  |
| `Gemini CLI` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 77 |  |
| `Telepathie-Verbot` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 86 |  |
| `Agenten-Telepathie` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 88 |  |
| `God Mode` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 19, 57 |  |
| `Externe Gehirn` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 114 |  |
| `Narrativen Datenbank` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 120 |  |
| `Wissens-Hypergraph` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 124 |  |
| `Atomare Entität` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 124 |  |
| `Atomic Entity` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 134 |  |
| `BDI-Modell` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 5 | 134, 140, 289, 317, 324 | `BDI-Modelle` ×3 |
| `BDI-Modelle` ^[projekt-ockham-narrative-systemik-reduktion.md:#3] | 3 | 3 | 134, 289, 324 |  |
| `BDI-Agent` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 138 |  |
| `Scene Card` ^[projekt-ockham-narrative-systemik-reduktion.md:#5] | 5 | 6 | 111, 113, 288, 289, 402, 404 |  |
| `Storybeat` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 3 | 111, 288, 402 | `Storybeats` ×1 |
| `Skill Library` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 195 |  |
| `Doppelt verkettete Liste der Kausalität` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 216 |  |
| `Waisen-Events` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 216 |  |
| `Kausalketten-Verifikation` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 216 |  |
| `Semantisches Linting` ^[projekt-ockham-narrative-systemik-reduktion.md:#3] | 3 | 3 | 115, 218, 322 |  |
| `Semantischen Lintings` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 220 |  |
| `Coherence Digest` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 252 |  |
| `Shadow Git` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 262, 264 |  |
| `Thematische Resonanz` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 270 |  |
| `Coherence Loop` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 281, 283 |  |
| `Obsidian Canvas` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 293, 295 |  |
| `Watchdog-Skript` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 298 |  |
| `NCP` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 270, 328 |  |
| `Narrative Context Protocol` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 328 |  |
| `Golden Source` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 330 |  |
| `Sektor 4` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 353 |  |
| `Keycard` ^[projekt-ockham-narrative-systemik-reduktion.md:#5] | 5 | 5 | 226, 248, 258, 259 |  |
| `OntologyValidator` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 378 |  |
| `Hallucination Drift` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 171 |  |
| `Lost in the Middle` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 27, 31 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kohärenztheorie der Wahrheit` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 37 |  |
| `Korrespondenztheorie der Wahrheit` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 38 |  |
| `Dissoziativer Identitätsstruktur` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 46 |  |
| `Strukturellen Dissoziation` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 46 |  |
| `TSDP` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 46 |  |
| `Anscheinend Normale Persönlichkeitsanteile` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 46 |  |
| `Emotionale Persönlichkeitsanteile` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 46 |  |
| `Klassischer Logik` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 309 |  |
| `Parakonsistenter Logik` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 310 |  |
| `Gödel-Gambit` ^[projekt-ockham-narrative-systemik-reduktion.md:#1] | 1 | 1 | 314 |  |
| `Fabula` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 201, 205 |  |
| `Syuzhet` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 201, 205 |  |
| `Zettelkasten` ^[projekt-ockham-narrative-systemik-reduktion.md:#3] | 3 | 5 | 122, 124, 287, 291, 418 | `Zettelkasten-Hypergraph` ×1, `Zettelkasten-Methodik` ×1 |
| `GraphRAG` ^[projekt-ockham-narrative-systemik-reduktion.md:#3] | 3 | 3 | 122, 127, 433 |  |
| `Model Context Protocol` ^[projekt-ockham-narrative-systemik-reduktion.md:#3] | 3 | 3 | 295, 431, 443 |  |
| `Prompt Injection` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 274, 276 |  |
| `Garbage Collection` ^[projekt-ockham-narrative-systemik-reduktion.md:#2] | 2 | 2 | 252, 254 |  |
| `Voyager` ^[projekt-ockham-narrative-systemik-reduktion.md:#6] | 6 | 6 | 193, 195, 199, 434, 435 |  |
| `LangGraph` ^[projekt-ockham-narrative-systemik-reduktion.md:#6] | 6 | 6 | 65, 69, 73, 421, 422 |  |
| `AutoGen` ^[projekt-ockham-narrative-systemik-reduktion.md:#7] | 7 | 7 | 65, 70, 73, 424, 429 | `autogen-multi-agent-conversation-memory` ×1 |
| `CrewAI` ^[projekt-ockham-narrative-systemik-reduktion.md:#8] | 8 | 8 | 65, 71, 73, 425, 426, 427 |  |

## What the extraction ran into

**Zeros:** 0.

Every candidate stands alone at least once; the list was tested before the count with a hyphen-and-letter boundary, because a hyphen is not a word boundary here (a term inside a compound would count 0 standing alone).

**Standing alone less often than with compounds:** 12 — `NovelOS` 24/28, `Kernel` 6/11, `Narrative Reliability Engineer` 2/4, `Architekt` 1/13, `Isomorphie` 3/4, `Kael` 20/22, `AEGIS` 5/6, `Librarian` 22/23, `BDI-Modell` 2/5, `Scene Card` 5/6, `Storybeat` 2/3, `Zettelkasten` 3/5.

Read from the counts' own compound lists: `NovelOS` 24/28 (as `NovelOS-Architektur`, `NovelOS-System`, `NovelOS-Reaktion`); `Kernel` 6/11 (compounds such as `Kohärenz-Kernel`, `Dual-Kernel-Theorie`); `Narrative Reliability Engineer` 2/4 (the longer `Narrative Reliability Engineering` stands twice, so the two forms are one name in the singular and a field); `Architekt` 1/13 is a substring trap, 13 being mostly `Architektur` and `Architekten`; `Isomorphie` 3/4 (once inside `Isomorphie-Prinzip`); `Kael` 20/22 (`Kaels`, a genitive); `AEGIS` 5/6 (`AEGIS-Agent`); `Librarian` 22/23 (`Librarian-Prozess`); `BDI-Modell` 2/5 (`BDI-Modelle` stands three times and is listed as its own surface); `Scene Card` 5/6; `Storybeat` 2/3 (`Storybeats`, a plural); `Zettelkasten` 3/5 (`Zettelkasten-Hypergraph`, `Zettelkasten-Methodik`).

**Export artifacts.** The export escapes underscores (`K\_1`, `K\_0`, `char\_kael`) and asterisks in the table (L110 to L116); the two kernel symbols are listed as the export writes them, in the form `K\_1`, with the dollar signs of the maths markup outside. The subscript is written with a plain digit after an escaped underscore, never as a true subscript. The reference numbers are glued to the words they annotate (51 by the profile), as at L17. Code blocks are flattened to plain lines with the language name (YAML, Python, JSON, Bash) as a line of its own, and a formula-like state (L154) has quotation marks both straight and typographic. The document has the bare names `BDI-Modell`, `BDI-Modelle` and `BDI-Agent` only as compounds with a hyphen; the lower-case `bdi_model` of the schema (L152, escaped) is not a candidate.

**The two kernels.** `K\_1` and `K\_0` carry a role in the case study: the case study at L309 and L310 assigns them to AEGIS and Kael respectively, while the earlier definition at L37 and L38 gives them as `Der Architekt` and `Die Muse`. These are the document's own mappings; they are recorded here and not compared.

**Lens.** The lens section holds concepts the document applies from outside the novel's world: truth theories (L37, L38), the dissociation model (L46), logics (L309, L310), the fabula/syuzhet distinction (L205), and tools it compares (L69 to L71). No person's name is listed; the document names several in L37 and L40 and they are left off.

**Standing.** The document calls itself a „Bericht“ and in its appendix draws on `Golden Source` documents (L330) it does not name; both are the document's own claims and nothing is decided by them. The index_date is 2026-01-02 and the web references carry an access date of 2 January 2026 (L421 and following). The document says that the novel `Kohärenz Protokoll` is its test case (L303) and not that it is canon.
