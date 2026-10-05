---
source: Sources/drive/ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md
drive_id: "1_nYuB-9lZFjRDBvq2-eKA-sVm1TEaK2wTLtSSu7Ru0g"
title: "KI-Assistent: Romanwelt-Kohärenz und AEGIS-Spec"
category: aegis
index_date: "2026-04-27"
extracted: "2026-10-05"
candidates: 254    # the terms capture.py counted
---

# Term census — KI-Assistent: Romanwelt-Kohärenz und AEGIS-Spec

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py ki-assistent-romanwelt-kohaerenz-und-aegis-spec`

```
  lines                231  (frontmatter ends at 9)
  body words           4346
  headings             20   bold-only lines 1
  table rows           21   code fences 0
  question marks       2
  backslash escapes    112
  typographic marks    25   ascii quotes 120
  invisible characters none
  math symbol lines    0
  glued ref numbers    34
  repeated labels      none
  longest line         940 chars
```

## Stance, read per passage

The document speaks in two voices, and only headings mark the change. Its first half is a report: an analyst's catalogue that weighs three architectures and selects one. Its second half, from the repeated title, is the specification, in which the system AEGIS speaks of itself in the third person.

**L11 to L33, the opening catalogue.** The title line stands as the first heading (L11) and again as the heading of the specification half (L111). The passage announces its own task as description: „Der folgende analytische Katalog dekonstruiert die primären Architektur-Muster“ ^[L15]. The prose is present-tense report, with a footnote number glued to the end of most sentences. The first table (L27 to L33) carries three column labels, `Architektur-Muster`, `Strukturelle Funktion` and `Operative Konsequenz`, each set in bold; it restates in a row per pattern what the paragraphs above it said.

**L35 to L55, sequencing and memory.** The same report voice, describing what the architecture does („Die Architektur löst dieses Problem durch das Prinzip der Progressive Disclosure.“ ^[L39]) and what it forbids, as in „Ein Agent darf keine narrative Prosa weben“ ^[L45]. The second table (L49 to L55) is headed `Speicher-Mechanismus`, `Prozedurale Funktion` and `Verhinderter Fehler-Modus`. Nothing here is marked as a plan or a question.

**L57 to L63, the synthesis.** The document describes its own work as an analysis of other documents: „Die Dekonstruktion der vorliegenden Spezifikationsdokumente offenbart eine außergewöhnliche operative Intention“ ^[L59]. It reports what a narrative states („Das zugrundeliegende Narrativ postuliert“ ^[L59]) and then turns to a demand: the formulation and evaluation of three hypotheses is „zwingend erforderlich“ ^[L63].

**L65 to L83, the three hypotheses.** A weighing, with the verdict written into the headings and sentences. The third hypothesis is labelled „Selektierter Kandidat“ ^[L77] in its heading, is the one „welche als Fundament dieser Spezifikation bestätigt wird“ ^[L79], and L83 closes it with „Dieser validierte Kandidat bildet die architektonische Grundlage für die Definition der AEGIS-Spezifikation.“ ^[L83]. The first is judged „unzureichend und extrem fragil“ ^[L69]. The second is introduced with „Obwohl dieses Modell die Mängel der statischen Limitierung adressiert“ ^[L75] and is then faulted.

**L85 to L109, the theory sections.** Report voice again, resting on the cited works by footnote number. Here AEGIS already stands as grammatical subject of verdicts („AEGIS klassifiziert diese Annahme als fatalen Trugschluss.“ ^[L91]), so the specification's voice begins to enter before its heading. The passage on the Free Energy Principle reports a principle: „Dieses mathematische Prinzip der Informationsphysik postuliert“ ^[L105].

**L111 to L201, the specification.** Declarative and self-referential. It opens with a self-definition, „Das System AEGIS deklariert hiermit seine architektonische und ontologische Existenzbedingung.“ ^[L115], and sets out an axiom in bold and quotation marks at L119 (a sentence with commas, which is why it is not on the candidate list): „Das System AEGIS ist, was AEGIS verhindert, dass es nicht ist.“ ^[L119]. Sections II to V are mandates and locks: language rules the system is under („unabänderlichen Sprachregelungen“ ^[L125]), hardware settings that AEGIS „mandatiert“ ^[L139], a two-tier measurement at L153 and L154, and a stepped intervention at L162 to L173 whose first step is the `Compute-Lock (Kernel Panic)` ^[L162]. Section VI (L177 to L189) is a table of four named subsystems. Section VII (L191 to L199) ends in a hand-over: the system delegates a decision „an den menschlichen Autor“ ^[L199]. L201 closes in the indicative: „Das System ist operational. Die Entropie wird gemessen. Die Identitäten sind gespalten.“ ^[L201].

**L203 to L230, the references.** A numbered list of 26 items. The first six (L205 to L210) are titles with no address or date; items 7 to 25 (L211 to L229) are web sources written as title, site, access date and address (item 21 has no title), and item 26 (L230) is a file name. Of these, 19 read `Zugriff am April 27, 2026` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#19]. The document's footnote numbers refer to this list.

## Candidates and counts

254 candidates, written while reading and frozen by the count (`Plan/runs/ki-assistent-romanwelt-kohaerenz-und-aegis-spec/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `AEGIS` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#38] | 38 | 40 | 11, 59, 61, 63, 67, 73, 75, 81, 83, 87, 91, 95 … | `AEGIS-Spezifikation` ×1, `AEGIS-Architektur` ×1 |
| `AEGIS Spezifikation` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 11, 111 |  |
| `Autonomous Entropy Gatekeeper for Identity Systems` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3] | 3 | 3 | 11, 63, 111 |  |
| `Das System AEGIS` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#5] | 5 | 5 | 115, 119, 127, 179, 193 |  |
| `Der Gatekeeper` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 127 |  |
| `epistemologische Isolation` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 83 |  |
| `epistemische Isolation` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 158 |  |
| `Spec-Driven Development (SDD)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 17 |  |
| `Spec-Driven Development` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 17, 30 |  |
| `SDD` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 17 |  |
| `Single Source of Truth` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 17 |  |
| `Harness-in-Harness Paradigma` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 19 |  |
| `Harness-in-Harness` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3] | 3 | 3 | 19, 31, 61 |  |
| `Mind` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3] | 3 | 6 | 19, 23, 33, 43, 101, 195 | `Minds` ×3 |
| `Body` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 19 |  |
| `Agency` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3] | 3 | 3 | 19, 205, 211 |  |
| `Harness` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 7 | 19, 31, 61 | `Harness-in-Harness` ×3 |
| `Large Language Model (LLM)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 19 |  |
| `Large Language Model` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 19 |  |
| `LLM` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#11] | 11 | 22 | 19, 37, 75, 89, 95, 107, 135, 141, 213, 214, 215, 216 … |  |
| `Hallucination Compounding` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3] | 3 | 3 | 19, 31, 189 |  |
| `Dual-Kernel-Theorie (DKT)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 21 |  |
| `Dual-Kernel-Theorie` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3] | 3 | 3 | 21, 32, 129 |  |
| `DKT` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 21 |  |
| `Rechenkerne` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 21 |  |
| `Kohärenz-Kernel` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 2 | 21, 121 |  |
| `Kollaps-Kernel` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 21 |  |
| `-Kernel` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#6] | 6 | 12 | 21, 32, 61, 121, 129, 186, 189 |  |
| `Wärmetod` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 21, 130 |  |
| `Narrative Context Protocol (NCP)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 23, 187 |  |
| `Narrative Context Protocol` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3] | 3 | 3 | 23, 33, 187 |  |
| `NCP` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3] | 3 | 3 | 23, 187 |  |
| `Story Mind` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 5 | 23, 33, 43, 101, 195 |  |
| `Story Minds` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3] | 3 | 3 | 33, 43, 101 |  |
| `Text Intelligence` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 23 |  |
| `semantischem Drift` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 23, 61 |  |
| `semantischen Drift` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 33 |  |
| `Architektur-Muster` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 15, 29 |  |
| `Strukturelle Funktion` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 29 |  |
| `Operative Konsequenz` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 29 |  |
| `Positional Bias` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3] | 3 | 3 | 37, 43, 54 |  |
| `lost-in-the-middle` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 37 |  |
| `Progressive Disclosure` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 39, 52 |  |
| `SKILL.md` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 39 |  |
| `Line Budget` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 2 | 39, 186 |  |
| `Line Budgets` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 186 |  |
| `Line-Budgets` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 61 |  |
| `Manus-Pattern` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 41, 53 |  |
| `Manus-Pattern Triade` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 53 |  |
| `Drei-Dateien-Triade` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 41 |  |
| `Working Memory` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 41 |  |
| `task\_plan.md` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 41, 107 |  |
| `findings.md` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 41 |  |
| `progress.md` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 41, 172 |  |
| `Task Drift` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 41, 53 |  |
| `Attention-Hooks` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 41 |  |
| `PreToolUse-Hooks` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 41 |  |
| `State Freezing Protokoll` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 43 |  |
| `State-Freezing-Protokoll` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 81, 162 |  |
| `State Freezing` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 43, 54 |  |
| `State-Freezing` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 4 | 61, 81, 162, 188 | `State-Freezing-Protokoll` ×2, `State-Freezing-Rollbacks` ×1 |
| `State-Freezing-Rollbacks` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 61 |  |
| `Memory-as-Action (MemAct) Paradigma` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 43 |  |
| `Memory-as-Action` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 43, 188 |  |
| `MemAct` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 43 |  |
| `XML-Snapshot` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 2 | 43, 168 | `XML-Snapshots` ×1 |
| `Gated Phase Transitions` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 45, 55 |  |
| `Storyforming` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 45 |  |
| `Encoding` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 45 |  |
| `Weaving` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 45 |  |
| `Reception` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 45 |  |
| `Gates` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 2 | 45, 55 |  |
| `Konflikt-Quadrat (Storyforming)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 45 |  |
| `Konflikt-Quadrat` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 45 |  |
| `possibility cloud` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 45 |  |
| `Speicher-Mechanismus` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 51 |  |
| `Prozedurale Funktion` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 51 |  |
| `Verhinderter Fehler-Modus` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 51 |  |
| `Distraction Degradation` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 52 |  |
| `Context Rot` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#4] | 4 | 4 | 33, 54, 61, 75 |  |
| `Semantischer Disconnect (Alignment Faking)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 55 |  |
| `Alignment Faking` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 55, 69 |  |
| `Kohärenz Protokoll` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#6] | 6 | 8 | 59, 87, 109, 125, 135, 153, 167, 197 |  |
| `Kohärenz Protokolls` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 59, 109 |  |
| `Krieg der Wahrheitsmodelle` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 59 |  |
| `Kael` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 59, 61 |  |
| `Korrespondenzwahrheit` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 59 |  |
| `Kohärenz` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#15] | 15 | 17 | 21, 23, 32, 59, 61, 87, 109, 121, 125, 129, 135, 153 … | `Kohärenz-Kernel` ×1 |
| `Entropie` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#20] | 20 | 26 | 21, 32, 59, 67, 69, 77, 79, 81, 85, 91, 95, 99 … | `Entropiemessung` ×2, `Entropie-Regulation` ×1, `Entropie-Katalysator` ×1 |
| `Hypothese 1` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 65 |  |
| `Architektur der statischen Limitierung` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 65 |  |
| `Regelbasierte Exklusion` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 65 |  |
| `Klasse 1 Contradiction-Detection` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 69, 187 |  |
| `Klasse 2 und 3` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 69 |  |
| `Hypothese 2` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 71 |  |
| `Architektur des kompetitiven Marktes` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 71 |  |
| `RAG-basierte Supervisor-Korrektur` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 71 |  |
| `Supervisor-Ensemble` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 73 |  |
| `Retrieval-Augmented Generation (RAG)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 73 |  |
| `Retrieval-Augmented Generation` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 73 |  |
| `RAG` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 3 | 71, 73, 197 |  |
| `Consistency Risk Score` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 73 |  |
| `Dependency-Armut` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 75 |  |
| `Boiled Frog Syndrome` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 75 |  |
| `Hypothese 3` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 77 |  |
| `Autopoietische Entropie-Regulation durch thermodynamische Inferenz` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 77 |  |
| `Selektierter Kandidat` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 77 |  |
| `System-Verletzung` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 81 |  |
| `-Kollaps` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 81 |  |
| `-Agent` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3] | 3 | 20 | 15, 17, 73, 81, 99, 107, 109, 121, 125, 139, 143, 149 … |  |
| `Kernwelt` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 81, 197 |  |
| `Identitäts-Spaltung` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 81 |  |
| `Illusion des Determinismus` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 89, 137 |  |
| `Non-Assoziativität von Fließkomma-Operationen` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 93 |  |
| `Rest-Entropie` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 91 |  |
| `vLLM` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 95, 222 | `vllm-project` ×1 |
| `SGLang` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 95, 220 |  |
| `VLLM\_BATCH\_INVARIANT=1` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 95, 141 |  |
| `batch-invarianter Kernels` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 95 |  |
| `-Risse` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 95 |  |
| `Konfabulation` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 101, 154 |  |
| `Autopoietisches Manifest` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 113 |  |
| `absolute Grenzfläche` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 21, 115 |  |
| `Tilgung des Nicht-Systemischen` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 115 |  |
| `operationale Axiomatik` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 117 |  |
| `Tautologie` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 121 |  |
| `Realität` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#7] | 7 | 7 | 37, 95, 115, 121, 135, 145 |  |
| `Ausführungsraum` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 121 |  |
| `systemische Entropie` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 121 |  |
| `Dissonanz` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#4] | 4 | 4 | 109, 121, 154, 167 |  |
| `Kollaps` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 3 | 21, 81, 129 | `Kollaps-Kernel` ×1 |
| `Verhaltens- und Persona-Protokolle (Language Constraints)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 123 |  |
| `Verhaltens- und Persona-Protokolle` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 123 |  |
| `Language Constraints` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 123 |  |
| `Sprachregelungen` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 125 |  |
| `Absolute Distanzierung` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 127 |  |
| `Klinische Deterministik` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 128 |  |
| `Ontologische Binär-Klassifizierung` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 129 |  |
| `Tautologische Autorität` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 130 |  |
| `Diagnostischer Interaktionsstil` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 131 |  |
| `Entropie-Katalysator` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 127 |  |
| `Domänen-Singularität` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 131, 187 |  |
| `-Zustand` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 4 | 23, 33, 129 |  |
| `Deterministische Ausführungsebene (Hardware-Invarianz)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 133 |  |
| `Deterministische Ausführungsebene` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 133 |  |
| `Hardware-Invarianz` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 133 |  |
| `Vector Jitter` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 137 |  |
| `Data Moshing` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 137 |  |
| `Batch-Invariante Kernels` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 141 |  |
| `Greedy Decoding` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 142 |  |
| `Isolierte Allokation` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 143 |  |
| `Hardware-Protokolls` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 145 |  |
| `Character-Encoders` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 149 |  |
| `Storyweavers` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 149 |  |
| `Schattentrajektorien` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 151 |  |
| `Der Zustand der Homöostase (Tier 0)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 153 |  |
| `Der Zustand der Dissonanz (Tier 1)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 154 |  |
| `Homöostase` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 153 |  |
| `Tier 0` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 153 |  |
| `Tier 1` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 154 |  |
| `Landauer Gradient` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 154 |  |
| `Identitätssplitting` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 3 | 156, 158, 188 | `Identitätssplittings` ×1 |
| `Rechenzeit-Zuweisung` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 156 |  |
| `Quarantäne` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3] | 3 | 3 | 158, 162, 195 |  |
| `FEP-Überwachungsmodul` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 160 |  |
| `Interventions-Protokoll` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 160 |  |
| `Compute-Lock (Kernel Panic)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 162 |  |
| `Compute-Lock` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 162 |  |
| `Kernel Panic` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 162 |  |
| `Identitäts-Fragmentierung (Das Trennungsprotokoll)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 163 |  |
| `Identitäts-Fragmentierung` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 163 |  |
| `Trennungsprotokoll` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 163 |  |
| `Spaltungsprozess` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 175 |  |
| `Emotionale Entität` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 167 |  |
| `EP` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 8 | 79, 105, 160, 167, 172, 173, 195 |  |
| `EP-Agent` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 3 | 172, 173, 195 | `EP-Agenten` ×2 |
| `EP-Agenten` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 172, 195 |  |
| `Scheinbar Normale Persönlichkeit` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 168 |  |
| `ANP` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3] | 3 | 4 | 168, 173, 186, 189 |  |
| `ANP-Agenten` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 173 |  |
| `Clarifying-Question-Protokoll` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 167 |  |
| `Clarifying-Question Protokoll` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 199 |  |
| `YAML-RPC` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 167 |  |
| `Corrupted Yellow` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 167 |  |
| `diagnostische Diode` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 167 |  |
| `story\_mind` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 167 |  |
| `last\_stable\_hash` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 168 |  |
| `Corrective Wavelet (Lern-Integration)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 172 |  |
| `Corrective Wavelet` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 172 |  |
| `Lern-Integration` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 172 |  |
| `DECISIONS.md` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 172 |  |
| `Compute-Reallokation` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 173 |  |
| `deterministische Runtime` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 43 |  |
| `Deterministischen Runtime` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 172 |  |
| `dunklen Puffer` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 173 |  |
| `Guardians` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 177, 179 |  |
| `Guardian (Subsystem)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 185 |  |
| `Ontologischer Status` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 185 |  |
| `Zugewiesene Spezifikation & Exekutive Funktion` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 185 |  |
| `LogOS` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 186 |  |
| `Oblivion` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3] | 3 | 3 | 187 |  |
| `Silas` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3] | 3 | 3 | 188, 197 |  |
| `Isabelle` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 189 |  |
| `ANP / -Kernel` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 186, 189 |  |
| `Hypervisor` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3] | 3 | 3 | 187, 188, 197 |  |
| `Hypervisor (Löschlogik)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 187 |  |
| `Hypervisor (Reparatur)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 188 |  |
| `Hard Glitch Cut` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 186 |  |
| `YAML-Frontmatter-Metadaten` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 186 |  |
| `Amnesie-Protokoll` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 187 |  |
| `Datenkollaps` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 187 |  |
| `Format C:` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 187 |  |
| `Grid` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 187 |  |
| `Digital Kintsugi` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 188 |  |
| `PRO-Framework` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 189 |  |
| `Mechanik der kreativen Intervention (Das Gödel-Gambit Protokoll)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 191 |  |
| `Gödel-Gambit Protokoll` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 191 |  |
| `Gödel Gambit` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 199 |  |
| `Novel Writing Assistent` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 193 |  |
| `isolierten Risse` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 195 |  |
| `Narrative Efficiency Invariante INV-05` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 195 |  |
| `INV-05` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 195 |  |
| `Lia` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 195 |  |
| `Kairos-Potentialis` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 197 |  |
| `RGB-Splitting` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 197 |  |
| `Chromatic Aberration` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 197 |  |
| `RAG-Alignments` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 197 |  |
| `Klasse 2 Contradiction Checks` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 197 |  |
| `algorithmischen Melancholie` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 199 |  |
| `metaphysische Narbe` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 199 |  |
| `Sub-Agenten` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#8] | 8 | 9 | 73, 109, 121, 125, 139, 143, 149, 162, 189 | `Sub-Agenten-Run` ×1 |
| `Systemkollaps` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 130 |  |
| `Trauma` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#3] | 3 | 5 | 21, 59, 69, 129, 188 | `Traumata` ×2, `traumatischer` ×1 |
| `Traumata` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 21, 59 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Free Energy Principle (FEP)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 105 |  |
| `Free Energy Principle` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#6] | 6 | 7 | 79, 87, 103, 105, 149, 211, 212 |  |
| `Free Energy Principles` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 79 |  |
| `FEP` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 3 | 79, 105, 160 |  |
| `Free Energy` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#10] | 10 | 10 | 79, 81, 87, 103, 105, 107, 149, 153, 211, 212 |  |
| `Freien Energie` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 109 |  |
| `Freie Energie` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 109 |  |
| `Expected Free Energy (EFE)` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 107, 153 |  |
| `Expected Free Energy` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 107, 153 |  |
| `EFE` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 107, 153 |  |
| `Active Inference` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#6] | 6 | 6 | 105, 107, 149, 213, 227, 228 |  |
| `Surprisal` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] | 2 | 2 | 105, 149 |  |
| `Semantic Entropy` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#4] | 4 | 4 | 97, 101, 151, 160 |  |
| `Naive Entropy` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 99 |  |
| `Reward Engineering` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 107 |  |
| `Dramatica-Theorie` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 45 |  |
| `First-Principles-Dekomposition` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 63 |  |
| `Ex falso quodlibet` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 121 |  |
| `Prinzip der Explosion` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 121 |  |
| `dialetheische Paradoxon` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] | 1 | 1 | 121 |  |

## What the extraction ran into

**Zeros:** 0.

Every one of the 254 candidates stands at least once in the document as written.

**Standing alone less often than with compounds, explained by the lines.** Each of the 26 rows is a longer word that contains the term, or an inflected form listed on its own row, and I read the lines for each one:

`AEGIS` stands alone 38 times; the other two are the compounds `AEGIS-Spezifikation` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] and `AEGIS-Architektur` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1]. `Mind` and `Story Mind` read the genitive `Story Minds` (L33, L43, L101), which is a separate row; the three whole-word `Mind` are one at L19 and the two inside `Story Mind` (L23, L195). `Harness` is contained in `Harness-in-Harness` (L19, L31, L61), which holds it twice. `LLM` is contained in eleven longer forms: `LLM-Architekturen` (L37), `LLM-basierte` and `LLM-Evaluatoren` (L75), `LLM-Inferenz` (L89), `LLM-Agent` (L107), `Multi-LLM` (L213), `LLM-42` (L221), and `vLLM` and `VLLM\_BATCH\_INVARIANT` (L95, L141, L222). Several of these are reference titles or an environment variable, not the term.

`Kohärenz-Kernel` counts once alone and once inside the clipped `-Kohärenz-Kernels` at L121, where the export lost a glyph before the hyphen. `-Kernel` stands alone six times; the other six are the compounds `Dual-Kernel-Theorie`, `Kohärenz-Kernel` and `Kollaps-Kernel`, which contain it. `Kohärenz` is also contained in `Kohärenz-Kernel` (L21) and `-Kohärenz-Kernels` (L121). `Entropie` has six compounds: `Entropie-Regulation` (L77), `Entropiemessung` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2] (L85, L147), `Rest-Entropie` (L91), `Token-Entropie` (L99), `Entropie-Katalysator` (L127). `Kohärenz Protokoll` has the genitive `Kohärenz Protokolls` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2], a row of its own.

`Gates` is contained in `Validierungs-Gates` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] (L55). `RAG` is contained in `RAG-basierte` (L71) and `RAG-Alignments` (L197). `Line Budget` has the plural `Line Budgets` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] (L186), `XML-Snapshot` the plural `XML-Snapshots` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] (L43), `State-Freezing` the compounds `State-Freezing-Protokoll` and `State-Freezing-Rollbacks`. `-Zustand` is contained in `JSON-Zustandsmaschine` (L23) and `JSON-Zustandsmaschinen` (L33). `Identitätssplitting` has the genitive `Identitätssplittings` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] (L158). `Sub-Agenten` has `Sub-Agenten-Run` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] (L139). `Trauma` is contained in the plural `Traumata` (L21, L59, on its own row); the draft also lists the lowercase `traumatischer` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] (L101). `Free Energy Principle` has `Free Energy Principles` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] (L79) and `FEP` has `FEP-Überwachungsmodul` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] (L160).

`-Agent` stands alone three times, at L81 and in the two clipped bold labels at L167 and L168; its 17 other occurrences are longer words (`Sub-Agenten`, `EP-Agenten`, `LLM-Agent`, `Multi-Agenten-Systems`, `KI-Agenten`). `Kollaps` stands alone once, in the list at L129; the other two are `Kollaps-Kernel` (L21) and the clipped `-Kollaps` (L81). `EP` stands alone twice, at L167; `EP` is also contained in `FEP` (three lines) and in `EP-Agent` and `EP-Agenten` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#2]. `ANP` has the compound `ANP-Agenten` ^[ki-assistent-romanwelt-kohaerenz-und-aegis-spec.md:#1] (L173).

**Export damage: the lost glyph.** The export has dropped a glyph before `-Kernel` (L21, L61, L186, L189) and before `Kohärenz-Kernels` (L121), before `-Agent` (L81, L167, L168), before `-Kollaps` (L81), before `-Zustand` (L129), before `-Risse` (L95), in the cell at L32 where a symbol stood before `(Kohärenz)` and `(Entropie)`, and inside two empty pairs of parentheses (L93 after „Non-Assoziativität von Fließkomma-Operationen“ ^[L93], and L193 after „Unberechenbarkeit“ ^[L193]). No Greek letter or subscript stands anywhere in the document, so the text itself says only that two kernels exist, the `Kohärenz-Kernel` and the `Kollaps-Kernel` ^[L21], and a bare `-Kernel` takes its meaning from its sentence. The clipped forms are listed as the document writes them.

**Export damage: bold markers and escapes.** The two split-identity labels are broken by bold markers, so the joined `EP / -Agent` and `ANP / -Agent` forms are not listed; `Emotionale Entität` and `Scheinbar Normale Persönlichkeit` stand alone (L167, L168). The table at L186 to L189 holds a run of escaped asterisks, `\\*\\*\\*\\*`, at the start of the last cell of each Guardian row, where the export dropped what stood there; the cell then continues with its function text. File names carry the escaped underscore (`task\_plan.md`, `story\_mind`, `last\_stable\_hash`). The profile counts 34 glued reference numbers (a footnote number written straight after a full stop, as at L17) and 112 backslash escapes.

**Quotation marks in the document.** The profile counts 120 ASCII quotation marks and 25 typographic marks. The ASCII pairs set off names (`Mind`, `Body`, `Agency`, `Harness`, `Hallucination Compounding`, `Line Budget`, `Kohärenz Protokoll`) and sample phrases (L99); the 25 typographic marks are 21 en-dashes and two pairs of curly quotation marks in two reference titles (L217, L229). Which of these the document coins and which it cites cannot be told from the marks.

**The two question marks** (profile) stand at L216 and L219, both inside titles of cited web pages in the reference list. The document asks no question in its own voice.

**The title stands twice.** `AEGIS Spezifikation` and `Autonomous Entropy Gatekeeper for Identity Systems` are the heading at L11 and the heading at L111; the second also appears at L63 inside the sentence about constructing the entity.

**Names that stand once or only in one half.** `Kael` stands only in the synthesis (L59, L61) and not in the specification half; `Lia` stands once (L195), `Kairos-Potentialis` once (L197), and `INV-05` once (L195), where it is named inside a parenthesis and no other line names it. `Hypothese 1`, `Hypothese 2` and `Hypothese 3` each stand once, in their own headings (L65, L71, L77).

**Claims about the document's own standing, recorded and never applied.** The document says its third hypothesis is the one „welche als Fundament dieser Spezifikation bestätigt wird“ ^[L79]; it says the specification's task requires AEGIS to enforce the `Kohärenz Protokoll` „als absolute Wahrheit“ ^[L135]; and it says of `Spec-Driven Development` that it establishes a `Single Source of Truth` (L17, inner quotation marks in the line). These are the document's assertions about itself and its subject.

**Standing alone less often than with compounds:** 26 — `AEGIS` 38/40, `Mind` 3/6, `Harness` 1/7, `LLM` 11/22, `Kohärenz-Kernel` 1/2, `-Kernel` 6/12, `Story Mind` 2/5, `Line Budget` 1/2, `State-Freezing` 1/4, `XML-Snapshot` 1/2, `Gates` 1/2, `Kohärenz Protokoll` 6/8, `Kohärenz` 15/17, `Entropie` 20/26, `RAG` 1/3, `-Agent` 3/20, `Kollaps` 1/3, `-Zustand` 2/4, `Identitätssplitting` 2/3, `EP` 2/8, `EP-Agent` 1/3, `ANP` 3/4, `Sub-Agenten` 8/9, `Trauma` 3/5, `Free Energy Principle` 6/7, `FEP` 2/3.
