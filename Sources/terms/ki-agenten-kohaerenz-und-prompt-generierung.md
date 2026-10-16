---
source: Sources/drive/ki-agenten-kohaerenz-und-prompt-generierung.md
drive_id: "1Ba99zXBtczS3Fd7HBkQSohOOpq9u2ayhnapSTlKoX_0"
title: "KI-Agenten: Kohärenz und Prompt-Generierung"
category: kernkonzept
index_date: "2025-08-05"
extracted: "2026-10-12"
candidates: 60    # the terms capture.py counted
---

# Term census — KI-Agenten: Kohärenz und Prompt-Generierung

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py ki-agenten-kohaerenz-und-prompt-generierung`

```
  lines                368  (frontmatter ends at 9)
  body words           4736
  headings             33   bold-only lines 0
  table rows           14   code fences 0
  question marks       10
  backslash escapes    87
  typographic marks    8   ascii quotes 110
  invisible characters none
  math symbol lines    0
  glued ref numbers    42
  repeated labels      none
  longest line         1760 chars
```

## Stance, read per passage

This is a German whitepaper about AI agents and a knowledge base of notes; it does not speak about the novel's world, and it names none of its figures. It speaks in the register of a research proposal, passage by passage:

The abstract (L18 to L26) announces what the paper presents: „stellt einen neuartigen, zweigeteilten Lösungsansatz vor“ ^[L22]. The hypothesis section (L73 to L95) is put as a postulate: „Wir postulieren, dass die Überwindung“ ^[L77] and „Unsere zentrale Hypothese lautet daher“ ^[L79]. The same section names its own term by announcement, „Wir nennen diesen Regelsatz das“ ^[L87]. The three theory pillars (L99 to L197) report and adapt published ideas; the paper says of its use of one of them „Wir adaptieren diesen Ansatz für unsere Zwecke“ ^[L175].

The methodology (L201 to L267) is a design: it is written as a specification of rules, „Der Agent kann die Regeln nicht brechen“ ^[L213], and as an enumeration, „Das Protokoll selbst lässt sich in fünf konzeptionelle Phasen unterteilen“ ^[L215]. Table 1 (L241 to L246) gives the articles of the constitution, each with a quoted instruction to the agent in the voice of a prompt; Table 2 (L260 to L267) assigns agent roles, and the paper says of it „eine Multi-Agenten-Architektur vorgeschlagen“ ^[L248].

The expected results (L271 to L305) speak in the future and in expectation: „wird erwartet, dass der Agent ein kohärentes Verständnis entwickelt“ ^[L293]. The conclusion (L307 to L339) sums up with „Dieses Whitepaper hat argumentiert“ ^[L319], and the outlook offers possibilities, „Man kann sich vorstellen, wie mehrere solcher Agenten zusammenarbeiten“ ^[L334]. The reference list (L341 to L367) is numbered; 24 of its entries end in an access date, and the entries are titles of cited works, not terms of this document.

The document labels no passage as a lock, a report of a decision or a canon; it presents everything as proposal and expectation.

## Candidates and counts

60 candidates, written while reading and frozen by the count (`Plan/runs/ki-agenten-kohaerenz-und-prompt-generierung/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `ki-agenten-kohaerenz-und-prompt-generierung.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kohärenz-Protokoll` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#8] | 8 | 13 | 13, 24, 83, 87, 197, 201, 209, 275, 293, 319, 321, 337 … | `Kohärenz-Protokolls` ×5 |
| `Kohärenz-Protokolls` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#5] | 5 | 5 | 201, 209, 275, 293, 337 |  |
| `Kohärenz-Lücke` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2] | 2 | 2 | 22, 77 |  |
| `Meta-Prompt` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#8] | 8 | 22 | 24, 91, 95, 163, 175, 191, 195, 197, 201, 225, 229, 237 … | `Meta-Prompting` ×7, `Meta-Prompts` ×6, `Meta-Promptings` ×1, `meta-prompting-llm-self-optimization` ×1 |
| `Meta-Prompts` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#6] | 6 | 6 | 197, 201, 225, 237, 267, 275 |  |
| `kognitive Verfassung` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 24 |  |
| `kognitiven Verfassung` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2] | 2 | 2 | 233, 303 |  |
| `Mandat zur Selbst-Evaluation` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 245 |  |
| `Mandat zur Prompt-Generierung` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2] | 2 | 2 | 246, 303 |  |
| `Kognitive Direktive` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 244 |  |
| `Orientierung am Anker-Dokument` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 217 |  |
| `Anker-Dokument` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 217 |  |
| `Navigation über MOCs` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2] | 2 | 2 | 218, 219 |  |
| `Fokussierung auf atomare Notizen` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 219 |  |
| `Kontext-Kapselung` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 220 |  |
| `Selbst-Aktualisierung` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 221 |  |
| `Selbst-Evaluation` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#6] | 6 | 7 | 24, 197, 237, 245, 246, 267 | `Selbst-Evaluations-` ×1 |
| `Maps of Content` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#4] | 4 | 4 | 137, 149, 334, 357 |  |
| `MOC der MOCs` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2] | 2 | 2 | 159, 217 |  |
| `MOC\_Tender` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 3 | 197, 221, 285 | `MOC\_Tender-Agent` ×1, `MOC\_Tender-Agenten` ×1 |
| `MOC\_Tender-Agent` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 2 | 197, 285 | `MOC\_Tender-Agenten` ×1 |
| `\_INDEX.md` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2] | 2 | 3 | 159, 217, 218 | `\_INDEX.md-Datei` ×1 |
| `Navigations-Kortex` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 137 |  |
| `Hierarchische Abstraktion` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 153 |  |
| `Atomizität` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 131 |  |
| `Emergente Struktur` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 133 |  |
| `Kontextfenster` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#6] | 6 | 17 | 22, 34, 38, 42, 44, 54, 55, 56, 65, 67, 131, 145 … | `Kontextfensters` ×8, `Kontextfenstern` ×1, `Kontextfensterproblem` ×1 |
| `Kontextamnesie` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2] | 2 | 2 | 48, 111 |  |
| `Lost-in-the-Middle` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 56 |  |
| `Working Memory` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#3] | 3 | 3 | 22, 38, 42 |  |
| `Knowledge Graph` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#5] | 5 | 10 | 115, 121, 129, 141, 197, 321, 349, 351, 352, 357 |  |
| `KG-RAG` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 121 |  |
| `Tool-Server` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 213 |  |
| `Exekutivsystem` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 87 |  |
| `Wissens-Kultivator` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 279 |  |
| `digitaler Gärtner` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 283 |  |
| `Gärtner` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#3] | 3 | 3 | 197, 221, 283 |  |
| `Autonomie der Methode` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 301 |  |
| `Agent-on-the-Loop` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 303 |  |
| `Human-in-the-Loop` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 303 |  |
| `Agenten-Psychologie` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2] | 2 | 2 | 336 |  |
| `Multi-Agenten-Architektur` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2] | 2 | 2 | 248, 252 |  |
| `create\_note` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#0] | 0 | 1 | 221 | `create\_note-Tool` ×1 |
| `update\_note\_links` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#0] | 0 | 1 | 221 | `update\_note\_links-Tool` ×1 |
| `update\_note\_status` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 221 |  |
| `Prioritizer\\\_Agent` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 263 |  |
| `Analyzer\\\_Agent` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 264 |  |
| `Synthesizer\\\_Agent` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 265 |  |
| `Generator\\\_Integrator\\\_Agent` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 266 |  |
| `Orchestrator / Main\\\_Agent` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 267 |  |
| `Framework für Kritisches Denken` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2] | 2 | 2 | 244, 264 |  |
| `Wert-Aufwand-Matrix` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 263 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Konstitutionellen KI` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2] | 2 | 2 | 24, 175 |  |
| `Konstitutionelle KI` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 163 |  |
| `Meta-Prompting` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#7] | 7 | 8 | 24, 95, 163, 191, 195, 246, 361 | `Meta-Promptings` ×1, `meta-prompting-llm-self-optimization` ×1, `meta-prompting-a-practical-guide-to-optimising-prompts-automatically-c0a071f4b664` ×1 |
| `Zettelkasten-Methode` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2] | 2 | 2 | 125, 129 |  |
| `Retrieval-Augmented Generation` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#3] | 3 | 3 | 65, 119, 352 |  |
| `Context Engineering` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2] | 2 | 2 | 220, 363 |  |
| `Prompt Engineering` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#1] | 1 | 1 | 303 |  |
| `RLAIF` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#2] | 2 | 4 | 245, 365 |  |

## What the extraction ran into

**Zeros:** 2 — `create\_note`, `update\_note\_links`.

**Standing alone less often than with compounds:** 10 — `Kohärenz-Protokoll` 8/13, `Meta-Prompt` 8/22, `Selbst-Evaluation` 6/7, `MOC\_Tender` 1/3, `MOC\_Tender-Agent` 1/2, `\_INDEX.md` 2/3, `Kontextfenster` 6/17, `Knowledge Graph` 5/10, `Meta-Prompting` 7/8, `RLAIF` 2/4.

Both zeros are export damage and a hyphen compound, not absences. Line 221 writes them as `create\_note-Tool` and `update\_note\_links-Tool`, so the whole word is followed by a hyphen and counts as "in" only (1 each); line 266 writes the same tool names with three backslashes, `create\\\_note` and `update\\\_note\\\_links`, which the list did not write. `read.py --count` finds each of those forms once.

For the ten that stand alone less often than with compounds, the compounds are inflections and longer words that contain the term: `Kohärenz-Protokoll` also stands in `Kohärenz-Protokolls` (listed as its own candidate), `Meta-Prompt` stands in `Meta-Prompting`, `Meta-Prompts` and `Meta-Promptings`, `Selbst-Evaluation` in `Selbst-Evaluations-`, `Kontextfenster` in `Kontextfensters` and a compound with `-problem`, `Meta-Prompting` in two reference-list URL slugs. `MOC\_Tender`, `MOC\_Tender-Agent` and `\_INDEX.md` stand inside longer forms with `-Agenten` and `-Datei`. `Knowledge Graph` and `RLAIF` also stand inside reference-list entries (L349 to L352, L357, L365), which are titles of cited works.

**Export damage the reading met.** The profile counts 87 backslash escapes, and the underscores of file names, tool names and agent names are escaped (`\_INDEX.md`, `MOC\_Tender`); the agent names of Table 2 carry a triple backslash. Candidates are listed exactly so. The table of Table 1 and Table 2 is written with a literal `\*\*` around its first cells. The document writes `Kohärenz-Protokolls 1.0` in a heading (L209); it is not listed because a period inside the term is read as a sentence by the count, and its base form `Kohärenz-Protokolls` is listed. The 42 glued reference numbers are footnote digits stuck to the words they annotate (for example after a closing full stop of a sentence).

**What the document is.** It is a technical whitepaper (a specification of a protocol and a prompt design for AI agents), not a text about the novel. Of the novel's names, `Kael` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#0] and `AEGIS` ^[ki-agenten-kohaerenz-und-prompt-generierung.md:#0] stand in no line; the title phrase „Das Kohärenz-Protokoll“ ^[L13] is this paper's own name for its rule set. Its standing claims are recorded and not applied: it presents its approach „neuartigen, zweigeteilten Lösungsansatz“ ^[L22] and says of its log files „bieten eine beispiellose Transparenz“ ^[L337]; both are the document's own assertions.

**Persons.** The paper names a person once in running text as the originator of a method, and the reference list names authors of web articles; none of them is a figure of the novel, and none is listed.
