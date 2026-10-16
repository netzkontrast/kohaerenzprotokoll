---
source: Sources/drive/spec-entwicklung-fuer-agentic-dramatica-roman.md
drive_id: "1UDDSiplXfZuNcpMVsmse5i4FRE8FP07sPjWlTgnb6qM"
title: "Spec-Entwicklung für Agentic Dramatica-Roman"
category: storyform
index_date: "2026-04-26"
extracted: "2026-10-13"
candidates: 98    # the terms capture.py counted
---

# Term census — Spec-Entwicklung für Agentic Dramatica-Roman

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py spec-entwicklung-fuer-agentic-dramatica-roman`

```
  lines                593  (frontmatter ends at 9)
  body words           5589
  headings             39   bold-only lines 3
  table rows           33   code fences 0
  question marks       12
  backslash escapes    338
  typographic marks    6   ascii quotes 212
  invisible characters none
  math symbol lines    3
  glued ref numbers    83
  repeated labels      Decision x9, Begründung x8, Context x8, Rejected Alternatives Note x6, Consequences x5, Acceptance Criteria x4, Beschreibung x4, Falsification Test (M01) x4, Finding x4, Immutable Fields x4, In-Phase-Activities x4, Modify-Conclusion x4, Post-Conditions x4, Pre-Conditions x4
  longest line         1070 chars
```

## Stance, read per passage

Die Spezifikation spricht in mehreren Stimmen, und nur die Überschriften und Labels des Dokuments trennen sie.

**Spezifikation als Regelwerk.** Sie nennt sich selbst ein „als primäres, maschinenlesbares und unmittelbar ausführbares Artefakt“ ^[L15]; ihre Version steht als „2.1.0 (NCP-Integrated & State-Freezing Optimized)“ ^[L17]. Die Stimme ist die der Vorschrift: „Agenten dürfen keine offenen Freitextfragen stellen.“ ^[L215], „Keine zwei Throughlines dürfen zu irgendeinem Zeitpunkt dieselbe Domain belegen.“ ^[L151]. Die Tabellen (L121 bis L127, L135 bis L141, L206 bis L211, L375 bis L387) tragen diese Regeln als Zeilen mit den Labels BLOCKER, WARNING und NOTICE.

**Phasen als Verträge.** Zwischen den vier Schreibphasen gilt: „Ein Übergang erfolgt erst, wenn alle Acceptance Criteria (Gates) erfüllt sind.“ ^[L259]. Jede Phase hat dieselben Felder (Pre-Conditions, Acceptance Criteria, Post-Conditions, Immutable Fields, L261 bis L331); ein gesperrtes Feld heißt dort „gegen Schreibzugriffe gesperrt“ ^[L277].

**Methodenanhang.** Er beginnt mit „Dieser Appendix dokumentiert die epistemologische Genese der Spezifikation“ ^[L408] und enthält die Entscheidungsprotokolle ADR-01 bis ADR-08 (L412 bis L448) mit den Labels Context, Decision, Begründung, Consequences und Rejected Alternatives Note, dann Reflection History, Query Expansion Log, Cross-Pollination Logs, Pre-Mortem-Analyse, Red-Team-Review, Contradiction Log und Falsifikations-Audit (L450 bis L557).

**Reflexionsliste in der Ich-Form.** Die Reflection History spricht ohne Sprecherangabe in der ersten Person: „Ich bin sehr sicher, dass das Einbinden des Narrative Context Protocol (NCP) der Schlüssel ist“ ^[L452]. Die Einträge sind nummeriert und mit Kürzeln wie F1 bis F5 versehen (L452 bis L481).

**Rollenwechsel und Frage.** Das Red-Team-Review beginnt mit „Wechsel in Critic-Modus:“ ^[L527]; der dritte Angriff endet als offene Frage: „Hier existiert ein Restrisiko.“ ^[L549]. Der letzte Abschnitt Open Questions / Unresolved nennt noch einmal „Hier besteht ein Restrisiko für Bias in der automatisieren Evaluierung.“ ^[L562].

**Bericht über eine Studie.** Das Falsifikations-Audit berichtet: „Die Hypothese wurde massiv falsifiziert.“ ^[L557]; die Studie, die es anführt, ist dort die genannte Quelle der Aussage, nicht das Dokument selbst.

**Szenario.** Die Pre-Mortem-Analyse beginnt mit „Szenario: Das agentische System in Produktion generiert unbrauchbare Romane.“ ^[L512]. Das ist ein gedachter Fall, keine Beobachtung.

## Candidates and counts

98 candidates, written while reading and frozen by the count (`Plan/runs/spec-entwicklung-fuer-agentic-dramatica-roman/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `spec-entwicklung-fuer-agentic-dramatica-roman.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Spec-Metadata` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 13 |  |
| `Choice-Space` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#7] | 7 | 7 | 115, 117, 265, 385, 453, 467, 515 |  |
| `Interaction-Constraints` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 129, 131 |  |
| `Coherence-Invarianten` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 143 |  |
| `Contradiction-Detection` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 4 | 200, 326, 424, 557 | `Contradiction-Detection-Ansatz` ×1, `Contradiction-Detection-Klassen` ×1 |
| `Clarifying-Question Protocol` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 213, 529 |  |
| `Phase-Definitions` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 257 |  |
| `Failure-Modes Catalog` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 369 |  |
| `Regression-Checks` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 389 |  |
| `Self-Verification Test Suite` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 397 |  |
| `Reflection History` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 450 |  |
| `Query Expansion Log` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 483 |  |
| `Cross-Pollination Logs` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 490 |  |
| `Pre-Mortem-Analyse` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 2 | 371, 510 | `Pre-Mortem-Analysen` ×1 |
| `Red-Team-Review` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 525 |  |
| `Contradiction Log` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 551 |  |
| `Falsifikations-Audit` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 555 |  |
| `Open Questions` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 549, 559 |  |
| `Architectural Decision Records` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 410 |  |
| `Narrative Context Protocol` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#7] | 7 | 7 | 22, 26, 40, 434, 452, 574, 591 |  |
| `NCP` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#22] | 22 | 28 | 17, 22, 24, 26, 40, 163, 255, 276, 312, 342, 361, 363 … |  |
| `State Freezing` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#11] | 11 | 11 | 342, 382, 438, 455, 463, 473, 487, 508, 514 |  |
| `Context Rot` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#15] | 15 | 15 | 145, 250, 335, 342, 382, 436, 455, 463, 477, 486, 506, 514 … |  |
| `Progressive Disclosure` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#6] | 6 | 6 | 339, 438, 454, 473, 553 |  |
| `Line Budgets` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 340 |  |
| `Branching Rule` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#3] | 3 | 3 | 341, 387, 517 |  |
| `Hierarchical Routing` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 343 |  |
| `Narrative Efficiency` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#5] | 5 | 5 | 191, 195, 382, 514, 583 |  |
| `Consistency Risk Score` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#3] | 3 | 3 | 210, 219, 290 |  |
| `CRS` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#4] | 4 | 4 | 210, 219, 290, 549 |  |
| `Latent Space Projection` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#4] | 4 | 4 | 211, 381, 520, 561 |  |
| `Phase-Transition-Contracts` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 259, 488 |  |
| `Cross-Output Alignment` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 163, 210 |  |
| `Chain-of-Justification` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 210, 533 |  |
| `Decoupled Semantic Encoding` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 211 |  |
| `Strukturelle Contradictions` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 209 |  |
| `Inhaltliche Contradictions` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 210 |  |
| `Pragmatische Contradictions` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 211 |  |
| `Domänen-Singularität` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 147 |  |
| `Archetypische Motivationsexklusion` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 169 |  |
| `Vocabulary Drift` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#3] | 3 | 3 | 117, 385, 515 |  |
| `Task Drift` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#4] | 4 | 4 | 202, 378, 500, 523 |  |
| `Reward Hacking` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 380, 516 |  |
| `Alignment Faking` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#3] | 3 | 3 | 381, 486, 520 |  |
| `Parameter Hallucination` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 379 |  |
| `Degeneration Loops` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 383 |  |
| `Ordering Errors` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 384, 518 |  |
| `Asymmetric Architecture` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 386 |  |
| `Distraction Degradation` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#5] | 5 | 5 | 341, 387, 465, 517, 553 |  |
| `State Contamination` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 366, 522 |  |
| `Trigger Overlap` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 521 |  |
| `YAML-RPC` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#6] | 6 | 6 | 211, 223, 404, 444, 464, 529 |  |
| `Immutable Fields` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#4] | 4 | 4 | 277, 295, 313, 331 |  |
| `Acceptance Criteria` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#6] | 6 | 6 | 259, 266, 284, 302, 320, 494 |  |
| `Storyformer Agent` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 261 |  |
| `Storyencoder Agent` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 279 |  |
| `Storyweaver Agent` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 297 |  |
| `Storyreceptor Agent` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 315 |  |
| `Narrova` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 5 | 418, 458, 474, 496, 587 | `Narrova-Architektur` ×2, `Narrova-Dramatica-Architektur` ×1 |
| `Author's Argument` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#4] | 4 | 5 | 52, 139, 263, 466, 520 |  |
| `IC-01` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#6] | 6 | 6 | 138, 271, 394, 402, 426, 468 |  |
| `IC-02` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 139, 271 |  |
| `IC-03` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#3] | 3 | 3 | 140, 244, 271 |  |
| `IC-04` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#3] | 3 | 3 | 141, 271, 468 |  |
| `INV-01` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 147, 395 |  |
| `INV-02` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 158, 325 |  |
| `INV-03` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 169, 289 |  |
| `INV-04` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#5] | 5 | 5 | 180, 307, 380, 469, 516 |  |
| `INV-05` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#3] | 3 | 3 | 191, 325, 395 |  |
| `FM-01` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 378, 523 |  |
| `FM-02` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 379 |  |
| `FM-03` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 380, 516 |  |
| `FM-04` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 381, 520 |  |
| `FM-05` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 382, 514 |  |
| `FM-06` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 383, 519 |  |
| `FM-07` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 384, 518 |  |
| `FM-08` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 385, 515 |  |
| `FM-09` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#1] | 1 | 1 | 386 |  |
| `FM-10` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#3] | 3 | 3 | 387, 465, 517 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Dramatica` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#13] | 13 | 32 | 11, 15, 20, 24, 28, 40, 131, 162, 259, 363, 379, 385 … | `Dramatica-Theorie` ×4, `Dramatica-Struktur` ×3, `Dramatica-basierte` ×1, `Dramatica-Konzepte` ×1 |
| `Storyforming` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#5] | 5 | 5 | 18, 259, 261, 418, 496 |  |
| `Story Encoding` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 259, 279 |  |
| `Storyweaving` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#3] | 3 | 3 | 235, 259, 297 |  |
| `Story Reception` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 259, 315 |  |
| `Storyform Alignment` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#5] | 5 | 5 | 20, 28, 428, 430, 461 |  |
| `Narrative Field` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#6] | 6 | 6 | 20, 28, 158, 299, 469, 541 |  |
| `Mental Sex` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#4] | 4 | 4 | 28, 67, 428, 430 |  |
| `Story Limit` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 28, 69 |  |
| `Story Mind` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 5 | 58, 263, 414, 434, 553 |  |
| `Throughline` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#5] | 5 | 8 | 125, 126, 139, 151, 265, 301, 306, 386 | `Throughlines` ×3, `throughlines` ×2 |
| `Signposts` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#5] | 5 | 5 | 93, 162, 301, 306, 313 |  |
| `Journeys` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#4] | 4 | 4 | 162, 301, 308, 313 |  |
| `Domain` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 7 | 124, 139, 151, 265, 453, 454, 455 | `Domains` ×2 |
| `Concern` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#3] | 3 | 6 | 125, 139, 265, 578 | `Concerns` ×2, `concerns` ×1 |
| `Positional Bias` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#6] | 6 | 6 | 335, 382, 438, 477, 487, 507 |  |
| `Retrieval-Augmented Generation` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 210, 504 |  |
| `Spec-Driven Development` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#3] | 3 | 3 | 21, 497, 571 |  |
| `Model Context Protocol` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#2] | 2 | 2 | 19, 567 |  |

## What the extraction ran into

**Zeros:** 0.

**Standing alone less often than with compounds:** 10 — `Contradiction-Detection` 2/4, `Pre-Mortem-Analyse` 1/2, `NCP` 22/28, `Narrova` 2/5, `Author's Argument` 4/5, `Dramatica` 13/32, `Story Mind` 2/5, `Throughline` 5/8, `Domain` 2/7, `Concern` 3/6.

There is no zero in the count. The ten rows with fewer standing-alone hits than compound hits are inflections or compounds and not damage: `Contradiction-Detection` stands inside `Contradiction-Detection-Ansatz` and `Contradiction-Detection-Klassen`, `Pre-Mortem-Analyse` inside `Pre-Mortem-Analysen`, `Dramatica` inside hyphen compounds (Dramatica-Theorie, Dramatica-Struktur, Dramatica-basierte, Dramatica-Konzepte), `Narrova` inside `Narrova-Architektur` and `Narrova-Dramatica-Architektur`, `Throughline` and `Concern` as plurals, `Domain` as „Domains“ and in compounds, and `Story Mind` and `Author's Argument` in genitive forms. Italic marks and the glued digits are the export's: `Story Dynamics` is written between asterisks at L418 and L541, so it was left off the list.

**Export artifacts.** The profile counts 338 backslash escapes, 83 glued reference numbers and 212 ASCII quotes. The escapes sit in identifiers (`storyform\_layer`, `working\_state`, `beat\_layer`), so a plain `storyform_layer` would count zero; the list holds none of them. The glued digits are the footnote numbers of the source list (L566 to L592), e.g. in `Spec-Driven Design (SDD).1` at L15; the quotations stop before them. Schema enums are empty in the export (`enum:` at L64 to L71), so the document gives no value list for the story dynamics there. The YAML block of L39 to L112 and the one at L232 to L250 are flattened into plain lines with a stray „YAML“ line before each.

**What the document names of any novel.** Nothing. The document is a generic specification; I found no figure, place, event, chapter or storyform value of any particular novel in it. `Kap` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#0], `Kapitel` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#0], `Kael` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#0], `AEGIS` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#0], `Nexus` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#0] and `Guardians` ^[spec-entwicklung-fuer-agentic-dramatica-roman.md:#0] stand zero times. The only Dramatica values it gives are the generic choice lists, e.g. „Universe, Physics, Mind, Psychology“ ^[L124], and an example case with „Charakter X wählt in Signpost 3 eine Aktion“ ^[L236], which is a placeholder, not a figure.

**A claim about its own standing.** The document calls its state object a single source: „Das NCP als Single Source of Truth ist nicht verhandelbar.“ ^[L462], and ADR-06 decides „SSOT über das Narrative Context Protocol (NCP), verwaltet als zentrales JSON-Objekt.“ ^[L434]. It also rates itself: „Die Spec übersteigt die Qualität des Vorgängers massiv“ ^[L481]. These are the document's own claims about itself and are recorded, not applied.

**Repeated labels.** The repeated labels of the profile (Decision, Begründung, Context, Rejected Alternatives Note, Consequences) are the ADR template and the phase template, not terms; they are not on the list.
