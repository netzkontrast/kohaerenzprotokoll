---
source: Sources/drive/spec-entwicklung-fuer-agentische-roman-entwicklung.md
drive_id: "1B1UqQeEHsC2sa3PSnGkBw4nS_vY4keKLIM4IWLc6-LA"
title: "Spec-Entwicklung für agentische Roman-Entwicklung"
category: plot-outline
index_date: "2026-04-26"
extracted: "2026-10-13"
candidates: 78    # the terms capture.py counted
---

# Term census — Spec-Entwicklung für agentische Roman-Entwicklung

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py spec-entwicklung-fuer-agentische-roman-entwicklung`

```
  lines                499  (frontmatter ends at 9)
  body words           5524
  headings             28   bold-only lines 7
  table rows           34   code fences 0
  question marks       6
  backslash escapes    312
  typographic marks    4   ascii quotes 126
  invisible characters none
  math symbol lines    0
  glued ref numbers    114
  repeated labels      Entscheidung x8, Status x8, Kontext x4, Erwogene Optionen x3
  longest line         1141 chars
```

## Stance, read per passage

The document speaks as a specification throughout, in one voice that gives rules to a consuming agent system and, after a marked break, in a second voice that reports how the specification came to be.

**Opening (L15 to L19), a mandate.** The text names itself an executable artefact: „Sie fungiert als primäres, ausführbares Artefakt im Sinne des Spec-Driven Design (SDD)“ ^[L15]. It binds itself to two requirements, „Die Architekturvorgabe (Komponente A) verlangt zwingend“ ^[L15], and says of the target system „Die Spezifikation ist agnostisch gegenüber dem zugrundeliegenden Basismodell“ ^[L19].

**Ontology and choice space (L21 to L145), a lock.** The Dramatica model is stated as a schema: „Die Dramatica-Theorie betrachtet eine vollständige Geschichte als Analogie für einen einzelnen menschlichen Verstand“ ^[L23]. The text reports a theory here and applies it. The limit on admissible values is stated as „wird der Choice-Space hart limitiert“ ^[L133]. Observed: the YAML block gives `enum:` with nothing after it at L50, L51 and L70 to L73, so the export (or the source) lost the values; the table at L137 to L143 carries them in prose.

**Constraints and invariants (L147 to L218), rules with severities.** Each IC rule has a rule and a rationale, for example „Diese Anordnung maximiert die narrative Reibung“ ^[L156]. A violating state is „wird vom Validator auf Protokollebene blockiert“ ^[L161]. The five INV rules are declared in a fixed shape (Deklaration, Detection-Heuristik, Severity, Resolution-Protokoll), for example „Keine zwei Throughlines dürfen zu irgendeinem Zeitpunkt dieselbe Domain belegen“ ^[L171] and „Deterministischer Rollback des States durch das System“ ^[L174].

**Contradiction classes and the question protocol (L220 to L286), a procedure.** The text demands „zwingt das Agenten-System zur Implementierung einer dreistufigen, aktiven Widerspruchserkennung“ ^[L222] and allows an exception for one class: „Inhaltliche Widersprüche können gelegentlich stilistisch gewollt sein“ ^[L235]. The question format is a sample payload (`cq_event` with the id „CQ-8934“ is a template value, not an event), and the YAML is sample structure, not narrative text.

**Phase contracts and working state (L288 to L344), a table of gates.** „Ein Phasenübergang erfolgt nur, wenn alle Akzeptanzkriterien“ ^[L290] are met; the table cell for the first phase says „Der Agent berechnet die 75 Appreciations“ ^[L297] and locks „Das gesamte story\_mind-Objekt wird gegen Schreibzugriffe gesperrt“ ^[L297]. The last phase ends in „Das finale Manuskript des Romans“ ^[L300]; this is the only line of the contract table that names the novel as a product, and it names no particular novel.

**Failure catalogue and regression suite (L346 to L372), a table.** Ten rows FM-01 to FM-10, each with a severity; the regression suite opens with „Die Spezifikation ist inhärent instabil“ ^[L368].

**Audit part (L374 to L448), a report with its own voice.** A heading marks the break: „Systemic Architectural Audit and Evaluative Records“ ^[L374]. It says the specification „resultiert aus einem iterativen Designprozess“ ^[L376] and, of the evaluation blocks, „wurde die Spezifikation iterativ gehärtet“ ^[L432]. Each ADR carries the labels Status, Kontext, Erwogene Optionen, Entscheidung, Konsequenzen, Falsifikations-Test, Verworfene Alternativen; the evaluation blocks are narrated in past tense. The closing claim about standing is recorded, not applied: the specification „behält durch die Hybridstruktur aus Markdown und strukturierten Datenschemata ihre Singularität als selbsttragendes Artefakt“ ^[L448].

**References (L450 to L498), a numbered list** of 47 entries with access dates; in the body the numbers stand glued to words (114 glued numbers by the profile), which is export damage.

## Candidates and counts

78 candidates, written while reading and frozen by the count (`Plan/runs/spec-entwicklung-fuer-agentische-roman-entwicklung/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `spec-entwicklung-fuer-agentische-roman-entwicklung.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Story Mind` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#5] | 5 | 7 | 21, 23, 35, 48, 242, 388, 436 |  |
| `Storyform` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#4] | 4 | 12 | 182, 283, 297, 298, 396, 416, 420, 438, 464 | `Storyforming` ×4, `Storyforming-Phase` ×2, `Storyforms` ×1, `Storyform-Datensatz` ×1 |
| `Storyforming` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#4] | 4 | 6 | 182, 297, 396, 438 | `Storyforming-Phase` ×2 |
| `Story Encoding` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 298 |  |
| `Story Weaving` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] | 2 | 3 | 269, 299, 357 |  |
| `Story Reception` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 300 |  |
| `Throughlines` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#5] | 5 | 5 | 156, 157, 171, 297, 363 |  |
| `Domain` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#9] | 9 | 11 | 140, 141, 156, 157, 159, 171, 297 | `Domains` ×2 |
| `Concern` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] | 2 | 5 | 141, 157, 297 | `Concerns` ×3 |
| `Signposts` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#8] | 8 | 8 | 112, 204, 205, 299, 396 |  |
| `Journeys` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#5] | 5 | 5 | 112, 204, 299 |  |
| `Story Dynamics` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 142 |  |
| `Story Goal` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 2 | 215, 240 |  |
| `Story Outcome` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 182 |  |
| `Story Judgment` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 182 |  |
| `Story Limit` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 226 |  |
| `Story Growth` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 159 |  |
| `Timelock` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#3] | 3 | 3 | 142, 226 |  |
| `Optionlock` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#3] | 3 | 3 | 142, 226 |  |
| `Author's Argument` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] | 2 | 2 | 215, 388 |  |
| `Main Character` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] | 2 | 3 | 156, 182 |  |
| `Influence Character` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] | 2 | 2 | 156 |  |
| `Objective Story` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] | 2 | 2 | 156, 193 |  |
| `Relationship Story` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 156 |  |
| `Choice-Space` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#3] | 3 | 3 | 131, 133, 149 |  |
| `Appreciations` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 297 |  |
| `Coherence-Invarianten` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] | 2 | 2 | 163, 442 |  |
| `Domänen-Singularität` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 167 |  |
| `Clarifying-Question-Protokoll` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#3] | 3 | 6 | 15, 185, 236, 245, 422, 448 | `Clarifying-Question-Protokolls` ×2, `Clarifying-Question-Protokolle` ×1 |
| `CQ` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 6 | 245, 267, 358, 360, 368, 424 |  |
| `Phasen-Transitions-Verträge` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] | 2 | 2 | 15, 288 |  |
| `Strukturelle Contradictions` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 224 |  |
| `Inhaltliche Contradictions` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 231 |  |
| `Pragmatische Contradictions` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 238 |  |
| `Consistency Risk Score` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] | 2 | 2 | 234, 251 |  |
| `CRS` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 251 |  |
| `Context Rot` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#5] | 5 | 5 | 222, 344, 359, 420, 444 |  |
| `Task Drift` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#3] | 3 | 3 | 222, 355, 469 |  |
| `Reward Hacking` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#3] | 3 | 3 | 357, 438, 469 |  |
| `Alignment Faking` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] | 2 | 2 | 358, 469 |  |
| `Vocabulary Drift` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] | 2 | 2 | 133, 362 |  |
| `Parameter Hallucination` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 356 |  |
| `Degeneration Loops` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 360 |  |
| `Ordering Error` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 2 | 361, 444 |  |
| `Asymmetric Architecture` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 363 |  |
| `State Overwrite` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 364 |  |
| `Working-State` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#3] | 3 | 4 | 19, 227, 302, 414 | `Working-State-Dokuments` ×1 |
| `working\_state` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#5] | 5 | 5 | 273, 274, 313, 368, 416 |  |
| `story\_mind` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#4] | 4 | 4 | 37, 52, 286, 317 |  |
| `encoding\_context` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] | 2 | 2 | 273, 319 |  |
| `weaving\_timeline` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] | 2 | 2 | 274, 330 |  |
| `execution\_memory` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 335 |  |
| `last\_stable\_hash` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] | 2 | 2 | 339, 444 |  |
| `Episodic Memory` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 304 |  |
| `Working Memory` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 304 |  |
| `Alert Fatigue` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] | 2 | 2 | 247, 448 |  |
| `Lazy Querying` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 247 |  |
| `Chain-of-Justification` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 236 |  |
| `Forward-Fix` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] | 2 | 2 | 362, 428 |  |
| `State Rollback` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 229 |  |
| `Self-Correction-Loop` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 218 |  |
| `Regression-Verification Suite` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 366 |  |
| `Architectural Decision Records` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 378 |  |
| `Falsifikations-Test` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] | 2 | 2 | 388, 396 |  |
| `Hybrid-Container` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 388 |  |
| `Single-Artifact-Mandat` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 448 |  |
| `Komponente A` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 15 |  |
| `Komponente O` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 15 |  |
| `INV-01` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#3] | 3 | 3 | 167, 297, 372 |  |
| `INV-05` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#3] | 3 | 3 | 211, 300, 372 |  |
| `IC-01` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] | 2 | 2 | 156, 297 |  |
| `FM-01` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 355 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Dramatica-Theorie` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#6] | 6 | 6 | 15, 23, 149, 380, 384, 436 |  |
| `Spec-Driven Design` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#2] | 2 | 2 | 15, 380 |  |
| `Model Context Protocol` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#6] | 6 | 6 | 19, 229, 304, 452, 453, 472 |  |
| `Relational Blockworld` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 2 | 442, 473 |  |
| `Janus-Prinzip` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#1] | 1 | 1 | 216 |  |
| `Pre-Mortem` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#3] | 3 | 4 | 348, 432, 444 | `Pre-Mortem-Analysen` ×1 |

## What the extraction ran into


**Zeros:** 0.

**Standing alone less often than with compounds:** 14 — `Story Mind` 5/7, `Storyform` 4/12, `Storyforming` 4/6, `Story Weaving` 2/3, `Domain` 9/11, `Concern` 2/5, `Story Goal` 1/2, `Main Character` 2/3, `Clarifying-Question-Protokoll` 3/6, `CQ` 1/6, `Ordering Error` 1/2, `Working-State` 3/4, `Relational Blockworld` 1/2, `Pre-Mortem` 3/4.

**Why no zeros, and what the rows hide.** No candidate counts 0: every one stands in the form written. The 14 rows that stand alone less often than with compounds are, by the lines: `Story Mind` also as `Story Minds` (L242, L436); `Storyform` and `Storyforming` inside `Storyforming-Phase`, `Storyforms` and `Storyform-Datensatz`; `Story Weaving` also in `Story Weaving-Phase` (L357); `Domain` as `Domains`; `Concern` as `Concerns`; `Story Goal` as `Story Goals` (L240); `Main Character` as `Main Characters` (L182); `Clarifying-Question-Protokoll` as `Clarifying-Question-Protokolls` and `Clarifying-Question-Protokolle`; `CQ` stands alone once (L245, the heading `(CQ)`) and otherwise inside `CQ-Protokoll`, `CQ-Event` and the id string (L267, L358, L360, L368, L424); `Ordering Error` also as `Ordering Errors` (L444); `Working-State` also as `Working-State-Dokuments` (L227); `Relational Blockworld` stands alone at L442 and at L473 inside the cited title `Coherence-Relational Blockworld`; `Pre-Mortem` also as `Pre-Mortem-Analysen` (L348). All are inflections or compounds, not damage.

**Export damage met.** Underscores are escaped in the YAML names (`working\_state`, `story\_mind`, `last\_stable\_hash` and others); they were listed with the escape because the line writes them so. Heading bold markers appear in the tables as `\*\*`. Footnote numbers are glued to words, for example the word `Standards` followed by digits at L388, and the quotations here stop before them. Digits inside table cells are dropped by `--find` (a heading cell reading `Phase 1:` is found as `Phase:`), so no candidate with an ordinal was listed: `Phase` is not a candidate. The enum values are missing in the YAML at L50 and L51. One reference (L488) carries the access date `Januar 1, 1970`, an export placeholder.

**Standing and labels.** The repeated labels of the profile are the ADR template: `Status` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#8], `Entscheidung` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#8], `Erwogene Optionen` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#3] and the eight times `Akzeptiert` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#8]. They are field labels of the template and not candidates. The severity words `BLOCKER` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#11] and `WARNING` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#7] are values of a field, not terms.

**The novel.** The document names no chapter: `Kap` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#0] and `Kapitel` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#0] stand 0 times as words (the one compound is `Kapiteln` at L420, in `späteren Kapiteln`, which speaks of the generated novel in general). `Kohärenz-Protokoll` ^[spec-entwicklung-fuer-agentische-roman-entwicklung.md:#0] stands 0 times. `Coherence-Invarianten` is the document's own name for its five INV rules (L163), not a term of a novel's world. No figure and no place is named; the Dramatica terms are given as a generic schema, and no storyform value is filled in for any particular story (the one sample payload at L266 to L283 uses `Charakter X`).

**The document's standing.** It calls itself „primäres, ausführbares Artefakt“ ^[L15] and says it keeps „ihre Singularität als selbsttragendes Artefakt“ ^[L448] and fulfils „alle aufgestellten Qualitätsinvarianten (Q1-Q10)“ ^[L448]. These are its own claims about itself; the Q1 to Q10 invariants are not listed anywhere in the document. Recorded, not applied.
