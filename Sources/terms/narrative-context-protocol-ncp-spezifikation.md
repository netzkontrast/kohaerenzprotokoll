---
source: Sources/drive/narrative-context-protocol-ncp-spezifikation.md
drive_id: "1vCVfo6_vxaw0kHHUteedKI6oLmz1KnomYTSiQOs6DoM"
title: "Narrative Context Protocol (NCP) Spezifikation"
category: storyform
index_date: "2025-07-03"
extracted: "2026-10-13"
candidates: 84    # the terms capture.py counted
---

# Term census — Narrative Context Protocol (NCP) Spezifikation

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py narrative-context-protocol-ncp-spezifikation`

```
  lines                224  (frontmatter ends at 9)
  body words           3667
  headings             16   bold-only lines 3
  table rows           20   code fences 0
  question marks       13
  backslash escapes    72
  typographic marks    75   ascii quotes 92
  invisible characters none
  math symbol lines    0
  glued ref numbers    16
  repeated labels      none
  longest line         4676 chars
```

## Stance, read per passage

Observed: the document is one continuous German white paper in three parts, headed „Teil I: Das theoretische Fundament – Eine Tiefenanalyse der Narrativen Systemik“ ^[L13], with numbered sections 1.1 to 3.3. It speaks as a specification in the present tense and does not mark its passages with labels such as lock or sample. It has no voice change and names no speaker.

Self-description (L11 to L15). The document calls itself a foundation and names its object „ein agentives, interaktives Erzählerlebnis“ ^[L15]. Plan or report: it reports its own purpose.

Proposal (L45 to L63). Table 1 is introduced as „Die folgende Tabelle präsentiert einen Vorschlag für die hochrangigen Dramatica-Spezifikationen“ ^[L45], so its storyform values are the document's proposal. Two lines later it ranks that table: „Diese Tabelle ist die entscheidende kreative und logische Grundlage.“ ^[L63]. That is a claim about its own standing and is recorded, not applied.

Architecture (L77 to L105). The second part describes „Die vorgeschlagene Architektur unterscheidet sich fundamental von gängigen Paradigmen“ ^[L83] and gives the schema of the Narrative Context Protocol. Its standing claim is „Single Source of Truth“ ^[L105], set in quotation marks in the document.

Schema block (L109 to L157). Observed: a JSON block with initial values for the four subsystem states of Kael, AEGIS, JunaV and DasFundament; the export lost the array contents (`"storyforms":,` at L111, `"interferenceRules":,` at L112, `"narrativeLog":` at L156). The block is sample data of the protocol's own schema, not narrated story.

Prompt cascade (L160 to L167). Each of four prompts is described by its task and instruction, with example instruction texts in quotation marks (L165, L167); no label marks them.

Control and interface (L173 to L191). The oversight component is declared: „Dies ist kein vages Konzept, sondern eine konkrete architektonische Komponente“ ^[L175]; the interface part proposes a hybrid model (L189).

Risks and roadmap (L193 to L219). A risk is named open: „ist eine ungelöste Forschungsfrage“ ^[L202]. The roadmap is five numbered phases (L211 to L215) and ends in a statement of intent (L219).

References (L221 to L223). Observed: a heading „Quellenangaben“ ^[L221] followed by 32 numbered web references run together in one line. The text between L11 and L219 carries glued footnote numbers (the profile counts 16); one stands at the end of the sentence of L36 before its colon.

## Candidates and counts

84 candidates, written while reading and frozen by the count (`Plan/runs/narrative-context-protocol-ncp-spezifikation/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `narrative-context-protocol-ncp-spezifikation.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kohärenz Protokoll` ^[narrative-context-protocol-ncp-spezifikation.md:#6] | 6 | 11 | 11, 15, 19, 30, 47, 67, 79, 87, 171, 195, 219 |  |
| `Theorie der Narrativen Systemik` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 15 |  |
| `Kael` ^[narrative-context-protocol-ncp-spezifikation.md:#8] | 8 | 8 | 30, 51, 71, 115, 117, 166, 190, 213 |  |
| `AEGIS` ^[narrative-context-protocol-ncp-spezifikation.md:#8] | 8 | 8 | 30, 51, 71, 126, 165, 166, 190 |  |
| `Juna/V` ^[narrative-context-protocol-ncp-spezifikation.md:#3] | 3 | 3 | 30, 51, 190 |  |
| `Das Fundament` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 30, 51 |  |
| `JunaV` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 132 |  |
| `DasFundament` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 137 |  |
| `Story-Subsysteme` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 30 |  |
| `System-Dirigent` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 3 | 77, 79, 162 | `System-Dirigenten` ×2 |
| `LLM-Dirigenten` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 32 |  |
| `Narrative Context Protocol` ^[narrative-context-protocol-ncp-spezifikation.md:#3] | 3 | 3 | 45, 103, 107 |  |
| `NCP` ^[narrative-context-protocol-ncp-spezifikation.md:#9] | 9 | 9 | 45, 75, 103, 105, 107, 175, 191, 201, 211 |  |
| `Single Source of Truth` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 105 |  |
| `Story Mind` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 105, 223 |  |
| `Prompt-Kaskade` ^[narrative-context-protocol-ncp-spezifikation.md:#5] | 5 | 5 | 89, 91, 160, 162, 203 |  |
| `State Analysis Prompt` ^[narrative-context-protocol-ncp-spezifikation.md:#4] | 4 | 4 | 96, 164, 189, 191 |  |
| `Context Compression Prompt` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 97, 165 |  |
| `Narrative Generation Prompt` ^[narrative-context-protocol-ncp-spezifikation.md:#3] | 3 | 3 | 98, 166, 189 |  |
| `State Update Prompt` ^[narrative-context-protocol-ncp-spezifikation.md:#3] | 3 | 3 | 99, 167, 175 |  |
| `dynamische Kontext-Kompression` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 101 |  |
| `narrativ bewussten Zustandsabstraktion` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 101 |  |
| `narrativen Vektor` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 3 | 32, 101, 165 |  |
| `Nicht-Fokal-Systeme` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 97 |  |
| `Fokal-System` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 2 | 97, 165 |  |
| `activeFocalSystem` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 115, 190 |  |
| `worldState` ^[narrative-context-protocol-ncp-spezifikation.md:#9] | 9 | 9 | 87, 96, 99, 101, 113, 164, 167, 175, 179 |  |
| `interferenceRules` ^[narrative-context-protocol-ncp-spezifikation.md:#8] | 8 | 8 | 67, 75, 112, 164, 167, 201, 214, 219 |  |
| `userModel` ^[narrative-context-protocol-ncp-spezifikation.md:#3] | 3 | 3 | 144, 191 |  |
| `narrativeLog` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 156, 181 |  |
| `systemStates` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 116, 167 |  |
| `thematicTension` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 119, 180 |  |
| `plotProgress` ^[narrative-context-protocol-ncp-spezifikation.md:#5] | 5 | 5 | 118, 127, 133, 138, 180 |  |
| `entropyLevel` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 128, 166 |  |
| `compressedContext` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 166 |  |
| `expressedContext` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 166 |  |
| `narrativePotential` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 3 | 180, 189, 191 | `narrativePotentials` ×2 |
| `narrativePotentials` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 189, 191 |  |
| `thematicAffinity` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 149, 191 |  |
| `decisionHistory` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 146 |  |
| `resonanceSignalStrength` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 134 |  |
| `Dramaturgische Aufseher` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 173, 183 |  |
| `Dramaturgischer Aufseher` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 175 |  |
| `Meta-Agent` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 175, 177 |  |
| `Strukturelle Integritätsprüfung` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 179 |  |
| `Konvergenzprüfung` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 180 |  |
| `Kontradiktionsprüfung` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 181 |  |
| `Dynamische Paar-Interferenz` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 71 |  |
| `Begleiter-Paar-Interferenz` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 72 |  |
| `Abhängige Paar-Interferenz` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 73 |  |
| `Kern-Storyforms` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 43 |  |
| `Dramatica-Storyform` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 3 | 30, 179, 201 | `Dramatica-Storyforms` ×1 |
| `Dramatica-Quads` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 67 |  |
| `genetische Signatur` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 45 |  |
| `hybrides Modell` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 189 |  |
| `Primäre Rolle` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 52 |  |
| `Domäne` ^[narrative-context-protocol-ncp-spezifikation.md:#4] | 4 | 6 | 38, 39, 53, 63 | `Domänen` ×2 |
| `Anliegen` ^[narrative-context-protocol-ncp-spezifikation.md:#3] | 3 | 3 | 39, 54 |  |
| `Thema` ^[narrative-context-protocol-ncp-spezifikation.md:#5] | 5 | 5 | 40, 41, 55, 191 | `thematische` ×4, `thematischen` ×3, `thematicTension` ×2, `thematicAffinity` ×2 |
| `Problem` ^[narrative-context-protocol-ncp-spezifikation.md:#7] | 7 | 9 | 19, 26, 41, 56, 63, 71, 101, 223 | `problematische` ×4, `Probleme` ×2, `problemlösenden` ×1 |
| `Lösung` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 57, 101 |  |
| `Symptom` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 58 |  |
| `Response` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 59 |  |
| `Ziel` ^[narrative-context-protocol-ncp-spezifikation.md:#4] | 4 | 5 | 25, 60, 63, 101, 165 | `Ziele` ×1, `zielorientierten` ×1 |
| `Konsequenz` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 61, 63 |  |
| `Faith` ^[narrative-context-protocol-ncp-spezifikation.md:#5] | 5 | 5 | 55, 71, 150, 191 |  |
| `Disbelief` ^[narrative-context-protocol-ncp-spezifikation.md:#3] | 3 | 3 | 55, 71 |  |
| `Doubt` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 56 |  |
| `Control` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 56, 151 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Dramatica` ^[narrative-context-protocol-ncp-spezifikation.md:#22] | 22 | 34 | 17, 19, 23, 30, 36, 45, 47, 67, 69, 179, 201, 219 … | `Dramatica-Theorie` ×2, `Dramatica-Storyform` ×2, `Dramatica-Modell` ×1, `Dramatica-Spezifikationen` ×1 |
| `Throughlines` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 23, 30 |  |
| `Table of Story Elements` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 36 |  |
| `Storyform` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 9 | 30, 43, 47, 71, 75, 179, 201, 211 | `Storyform-Spezifikationen` ×1, `Storyforms` ×1, `storyforms` ×1, `Storyform-Authoring` ×1 |
| `Quad` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 4 | 67, 69, 71, 164 | `Quad-Beziehungen` ×1 |
| `Objective Story` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 25, 52 |  |
| `Main Character` ^[narrative-context-protocol-ncp-spezifikation.md:#3] | 3 | 3 | 26, 27, 52 |  |
| `Obstacle Character` ^[narrative-context-protocol-ncp-spezifikation.md:#4] | 4 | 4 | 27, 28, 52 |  |
| `Subjective Story` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 28, 52 |  |
| `OODA-Loop` ^[narrative-context-protocol-ncp-spezifikation.md:#0] | 0 | 1 | 95 | `OODA-Loop-Phase` ×1 |
| `ReAct` ^[narrative-context-protocol-ncp-spezifikation.md:#0] | 0 | 1 | 95 | `Reaction` ×1, `ReAct-Framework-Phase` ×1 |
| `Standard-RAG` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 85 |  |
| `Agentic RAG` ^[narrative-context-protocol-ncp-spezifikation.md:#4] | 4 | 4 | 86, 223 |  |
| `LangGraph` ^[narrative-context-protocol-ncp-spezifikation.md:#2] | 2 | 2 | 87, 223 | `langgraph-a-framework-for-building-stateful-multi-agent-llm-applications-a51d5eb68d03` ×1 |
| `Few-Shot` ^[narrative-context-protocol-ncp-spezifikation.md:#1] | 1 | 1 | 164 |  |

## What the extraction ran into

**Zeros:** 2 — `OODA-Loop`, `ReAct`.

**Standing alone less often than with compounds:** 12 — `Kohärenz Protokoll` 6/11, `System-Dirigent` 1/3, `narrativen Vektor` 2/3, `Fokal-System` 1/2, `narrativePotential` 1/3, `Dramatica-Storyform` 2/3, `Domäne` 4/6, `Problem` 7/9, `Ziel` 4/5, `Dramatica` 22/34, `Storyform` 2/9, `Quad` 2/4.

**`- ` lines read as prose and not counted:** 1 — fraktalen, verschachtelten psychologischen Architektur.

`OODA-Loop` ^[narrative-context-protocol-ncp-spezifikation.md:#0] and `ReAct` ^[narrative-context-protocol-ncp-spezifikation.md:#0] are zeros by compounding: the document writes them only as column text inside the longer words `OODA-Loop-Phase` ^[narrative-context-protocol-ncp-spezifikation.md:#1] and `ReAct-Framework-Phase` ^[narrative-context-protocol-ncp-spezifikation.md:#1] at L95, and both are counted by the compound row. They name frameworks and stand in the lens list.

Standing alone less often than with compounds is ordinary German compounding and inflection: `Kohärenz Protokoll` is also written `Kohärenz Protokolls` ^[narrative-context-protocol-ncp-spezifikation.md:#5] in the genitive, `Storyform` also as `Storyforms` ^[narrative-context-protocol-ncp-spezifikation.md:#1] and `storyforms` ^[narrative-context-protocol-ncp-spezifikation.md:#1], `Domäne` as `Domänen` ^[narrative-context-protocol-ncp-spezifikation.md:#2], and `Problem` as `Probleme` ^[narrative-context-protocol-ncp-spezifikation.md:#2]. `Thema`, `Anliegen`, `Ziel` and `Problem` are the labels of Table 1 and are common German nouns in their other uses, so their counts mix the table label with ordinary prose.

The one `- ` line read as prose is a candidate that carries a comma, written by the reader against the briefing; it is the document's phrase at L32 and is counted by nobody. The mistake is in the reader's list and the list is frozen, so it is reported rather than corrected.

Export damage met: table cells carry escaped asterisks (`\*\*Primäre Rolle\*\*`, L52 to L61); the schema block has lost its array contents (L111, L112, L146, L156); `4 \\times 4 = 16` at L32 is formula text with its backslash, not rendered. The JSON field names (`worldState`, `interferenceRules`, `userModel`, `narrativeLog`) are written in camelCase, and `JunaV` and `DasFundament` (L132, L137) are the schema's spellings of the subsystems that the prose and Table 1 write `Juna/V` and `Das Fundament`.

Words of the novel's world: the document names the four subsystems Kael, AEGIS, Juna/V and Das Fundament (L30, L51) and gives their Dramatica values in Table 1 (L51 to L61). The prose names the Kohärenz Protokoll as the system itself. No chapter is named: `Kap` ^[narrative-context-protocol-ncp-spezifikation.md:#0] and `Kapitel` ^[narrative-context-protocol-ncp-spezifikation.md:#0] both count zero.

Claim about its own standing (recorded, never applied): „Single Source of Truth“ ^[L105] for the Narrative Context Protocol, and Table 1 as „die entscheidende kreative und logische Grundlage“ ^[L63].
