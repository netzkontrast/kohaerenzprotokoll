---
source: Sources/drive/research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md
drive_id: "1cerl5kpzYP4LBhz4jWbwquIUD_LQnw04OpS1aCAtJiU"
title: "research-prompt_dual-storyform-rebuild-kohaerenz-protokoll.md"
category: storyform
index_date: "2026-04-30"
extracted: "2026-10-11"
candidates: 116    # the terms capture.py counted
---

# Term census — research-prompt_dual-storyform-rebuild-kohaerenz-protokoll.md

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m`

```
  lines                1211  (frontmatter ends at 9)
  body words           7959
  headings             47   bold-only lines 30
  table rows           17   code fences 0
  question marks       40
  backslash escapes    286
  typographic marks    320   ascii quotes 180
  invisible characters none
  math symbol lines    17
  glued ref numbers    92
  repeated labels      How to apply it — step by step x5, What it is x5, When to stop / escape criterion x5, Why it is in this prompt x5, Example trigger in this research context x4
  longest line         548 chars
```

## Stance, read per passage

Light pass: the document is a research prompt, written as instructions to an executing AI agent, not a narrative or a design statement of the novel. It speaks in four registers, and this census follows the first two only for the novel's world.

**Header block (L15 to L36).** Metadata keys (`topic`, `constraint_blocks`, `cross_pollination`) flattened onto single lines by the export; read as the prompt's own packaging, not as statements about the world.

**Self-description (L44, L56).** The prompt calls itself „Dieser Prompt ist selbstcontained“ ^[L44] and names its research kind: „Diese Forschung ist eine Exploration, keine Extraktion“ ^[L56]. It is a plan and a contract for another agent; its section heading „Forschungsziel (M — Mandate)“ ^[L170] sets the task.

**World statements (L347 to L399, the Compact Primer).** Written in the declarative present, one bullet per concept (Roman, Kael, Juna, AEGIS, Moonshine-Link, Guardians, Kernwelten, Alter-System, Dual-Kernel-Theorie, Physik, Zeit, Wahrheit, Dramatica-Status). The block introduces itself with „Damit du die Designvorgaben interpretieren kannst, hier die minimal nötige Story-Architektur“ ^[L347]. These are the only passages that describe the novel; they are the prompt's report of the project's architecture, handed over as a primer for the agent, not a definition of the world.

**Author quotation (L624 to L628).** One passage is marked as the author's own words: „Vom Autor übergebenes Beispiel (verbatim, weil bedeutungstragend)“ ^[L624]; the prompt then calls it a data point: „Das Beispiel ist ein Datenpunkt, keine Theorie“ ^[L668].

**Design contract (L676 to L691).** The heading „T — Tensioning (Bindende Designvorgaben)“ ^[L676] introduces the table T1 to T7; these are constraints the prompt sets on every variant the agent generates, not facts of the novel.

**Method, template and checklist passages (L405 to L572, L697 to L1210).** Method blocks with the repeated labels listed in the profile, steps with placeholder text in square brackets, an output schema („Iteration [i] Output Schema (alle Felder ausfüllen)“ ^[L930]) and a closing checklist. Left out of the note on purpose; the candidate list keeps the method names as the document's own terms. The prompt ends: „Ende des Forschungsprompts. Führe jetzt aus.“ ^[L1210]

## Candidates and counts

116 candidates, written while reading and frozen by the count (`Plan/runs/research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kohärenz Protokoll` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#5] | 5 | 5 | 15, 42, 172, 351, 1024 |  |
| `Kael` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#9] | 9 | 10 | 355, 359, 367, 379, 465, 527, 689 | `Kael-Host` ×1 |
| `Juna` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#9] | 9 | 12 | 140, 300, 311, 359, 367, 379, 685, 689 | `Juna-Verankerung` ×1, `Juna-Verortung` ×1 |
| `AEGIS` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#18] | 18 | 22 | 311, 327, 359, 363, 367, 371, 379, 383, 465, 496, 527, 689 … | `AEGIS-Architektur` ×1, `AEGIS-Sensoren` ×1 |
| `Moonshine-Link` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#2] | 2 | 3 | 359, 367, 1160 | `Moonshine-Link-Boundary` ×1 |
| `Guardians` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#2] | 2 | 2 | 371, 379 |  |
| `LogOS` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 371 |  |
| `Mnemosyne` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 2 | 371, 690 | `Mnemosyne-Archipel-Konvergenz` ×1 |
| `Cerberus` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 371 |  |
| `Kairos/Sophia` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 371 |  |
| `Kernwelten` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#2] | 2 | 3 | 311, 371, 375 | `Kernwelten-Logik` ×1 |
| `KW1` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 375 |  |
| `KW2` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 2 | 375 |  |
| `KW3` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 2 | 375 |  |
| `KW4` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 375 |  |
| `Alter-System` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#2] | 2 | 2 | 311, 379 |  |
| `ANP` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 2 | 355, 379 |  |
| `EP` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 2 | 355, 379 |  |
| `Lex` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#0] | 0 | 1 | 379 |  |
| `Alex` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#0] | 0 | 1 | 379 | `Alex-Beschützer` ×1 |
| `Rhys` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#0] | 0 | 1 | 379 | `Rhys-Pfleger` ×1 |
| `Selene` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#0] | 0 | 1 | 379 | `Selene-ISH` ×1 |
| `Nyx` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#0] | 0 | 1 | 379 |  |
| `Kiko` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#0] | 0 | 1 | 379 | `Kiko-Freeze` ×1 |
| `Lia` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#0] | 0 | 1 | 379 |  |
| `Isabelle` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#0] | 0 | 1 | 379 | `Isabelle-Sexualisiert` ×1 |
| `Moros` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#0] | 0 | 1 | 379 | `Moros-Kollaps` ×1 |
| `Argus` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#0] | 0 | 1 | 379 | `Argus-Meta` ×1 |
| `Silas` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#0] | 0 | 1 | 379 | `Silas-Juna-Echo` ×1 |
| `Oblivion` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#0] | 0 | 1 | 379 | `Oblivion-AEGIS-Echo` ×1 |
| `Silas-Juna-Echo` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 379 |  |
| `Oblivion-AEGIS-Echo` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 379 |  |
| `Dual-Kernel-Theorie` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#2] | 2 | 2 | 311, 383 |  |
| `DKT` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 2 | 383, 387 |  |
| `K0` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#4] | 4 | 4 | 327, 363, 383 |  |
| `K1` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#4] | 4 | 4 | 327, 363, 383 |  |
| `Kollaps-Kern` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#2] | 2 | 2 | 363, 383 |  |
| `Kohärenzkern` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#2] | 2 | 2 | 363, 383 |  |
| `Erasure` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 2 | 363, 383 | `Erasure-Sweeps` ×1 |
| `Erasonen` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#2] | 2 | 3 | 383, 387, 391 | `Erasonen-Aktivität` ×1 |
| `Coheronen` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#2] | 2 | 3 | 383, 387, 391 | `Coheronen-Schicht` ×1 |
| `Erasure-Sweeps` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 363 |  |
| `Landauer-Hitze` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 363 |  |
| `PAL-Operator` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 391 |  |
| `Zeitpfeil` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 383 |  |
| `Wächter-Zwiespalt` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#0] | 0 | 2 | 371, 1160 | `Wächter-Zwiespalts` ×1, `Wächter-Zwiespalt-Soziopolitik` ×1 |
| `Truth Rotation` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 395 |  |
| `Vortex` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 2 | 395, 1160 |  |
| `Ouroboros` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 351 |  |
| `Algorithmische Melancholie` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 363 |  |
| `Dialetheia-Logik` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 395 |  |
| `Witness Function` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#2] | 2 | 2 | 359, 387 |  |
| `Mnemosyne-Archipel` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#0] | 0 | 1 | 690 | `Mnemosyne-Archipel-Konvergenz` ×1 |
| `Leech-Lattice` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 367 |  |
| `Vertex Operator Algebras` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 367 |  |
| `Monstergruppe` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 367 |  |
| `Storyform A` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#12] | 12 | 12 | 181, 183, 284, 395, 399, 446, 465, 685, 686, 922, 923, 936 |  |
| `Storyform B` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#11] | 11 | 11 | 181, 183, 284, 395, 399, 496, 686, 923, 937 |  |
| `Heuristics of Integration` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#3] | 3 | 3 | 183, 284, 399 |  |
| `Phoenix Collapse` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#3] | 3 | 3 | 183, 284, 399 |  |
| `Suno Album` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 286 |  |
| `The Weight of Why` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 286 |  |
| `Memory-Slot-Architektur` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 286 |  |
| `Dual-Mapping` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#3] | 3 | 6 | 64, 138, 181, 415, 508, 517 | `Dual-Mapping-Spiegelregeln` ×1, `Dual-Mapping-Spiegelung` ×1, `Dual-Mapping-Hypothese` ×1 |
| `Dual-Storyform-Spiegelung` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#8] | 8 | 8 | 138, 180, 539, 616, 620, 745, 1036, 1044 |  |
| `Spiegelregel` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#14] | 14 | 25 | 64, 68, 424, 434, 527, 636, 648, 652, 667, 688, 784, 798 … | `Spiegelregeln` ×2, `Spiegelregel-Hypothese` ×1, `Spiegelregel-Variante` ×1, `Spiegelregel-Logik` ×1 |
| `Mirror-Operator` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#2] | 2 | 3 | 181, 660, 1048 | `Mirror-Operators` ×1 |
| `Maximum-2-Ebenen-Überlagerung` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#3] | 3 | 3 | 140, 527, 652 |  |
| `Maximum 2 Ebenen pro Throughline` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 687 |  |
| `Fixpunkte` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#4] | 4 | 4 | 656, 1056, 1060 |  |
| `Guardian-Kollektiv` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 689 |  |
| `MAPIT` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#7] | 7 | 8 | 23, 130, 132, 160, 164, 584, 697 | `MAPIT-Komponente` ×1 |
| `ReAct` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#3] | 3 | 6 | 23, 86, 88, 132, 164 | `ReAct-Framework` ×1, `ReAct-Zyklus` ×1, `ReAct-Wirbelsäule` ×1 |
| `NotebookLM` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#6] | 6 | 21 | 35, 93, 139, 187, 272, 286, 302, 309, 311, 339, 347, 477 … | `NotebookLM-Notebooks` ×14, `NotebookLM-Befragung` ×1 |
| `Contradiction Log` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#15] | 15 | 17 | 21, 255, 273, 276, 324, 471, 477, 485, 487, 566, 728, 764 … |  |
| `Query Expansion Log` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#5] | 5 | 5 | 562, 992, 1124, 1190, 1198 |  |
| `Falsification` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#4] | 4 | 4 | 19, 409, 726, 984 |  |
| `Contrast Classes` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#5] | 5 | 5 | 20, 440, 727, 818, 984 |  |
| `Adversarial Query Expansion` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#8] | 8 | 8 | 23, 94, 128, 533, 724, 984, 992, 1190 |  |
| `First-Principles Decomposition` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#5] | 5 | 5 | 22, 502, 725, 745, 984 |  |
| `Reflection Baseline` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#4] | 4 | 4 | 31, 211, 711, 1189 |  |
| `Pre-Synthesis Integrity Check` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#4] | 4 | 4 | 114, 220, 574, 1197 |  |
| `Mandate` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#8] | 8 | 8 | 24, 136, 144, 152, 170, 586, 588, 744 |  |
| `Architecture` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#4] | 4 | 8 | 25, 36, 137, 153, 345, 590, 596, 716 |  |
| `Permutation Mathematics` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#5] | 5 | 5 | 26, 138, 154, 614, 688 |  |
| `Interrogation` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#10] | 10 | 10 | 27, 35, 139, 155, 309, 672, 715, 766, 954, 1148 |  |
| `Tensioning` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#5] | 5 | 7 | 28, 140, 144, 156, 182, 676, 744 | `Tensioning-Liste` ×2 |
| `Compact Primer` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#4] | 4 | 4 | 36, 345, 596, 716 |  |
| `Surviving-Branch Triangulation` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#3] | 3 | 3 | 29, 825, 996 |  |
| `Hypothesis Half-Life Audit` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#4] | 4 | 4 | 30, 863, 893, 996 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Throughline` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#15] | 15 | 23 | 140, 181, 299, 508, 517, 527, 605, 608, 652, 685, 686, 687 … | `Throughlines` ×7, `Throughline-Position` ×1 |
| `Domains` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#5] | 5 | 5 | 180, 605, 640, 688 |  |
| `Universe` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#6] | 6 | 7 | 496, 605, 628, 640, 803, 804 | `Universe-Domain` ×1 |
| `Physics` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#4] | 4 | 4 | 605, 640, 803, 804 |  |
| `Mind` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#6] | 6 | 10 | 260, 605, 640, 686, 690, 784, 802, 803, 804 | `mindestens` ×20, `Mindestens` ×4 |
| `Psychology` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#5] | 5 | 5 | 605, 628, 640, 803, 804 |  |
| `Perspektiven` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#5] | 5 | 8 | 180, 605, 606, 641, 688, 745, 805, 922 | `Perspektiven-Set` ×1, `Perspektiven-getriebene` ×1, `Perspektiven-Zuweisung` ×1 |
| `Overall Story` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 605 |  |
| `Main Character` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 605 |  |
| `Influence Character` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 605 |  |
| `Relationship Story` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 605 |  |
| `Quad` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#2] | 2 | 10 | 68, 424, 434, 527, 547, 555, 605, 648, 803 | `Quad-Konsistenz` ×2, `Quad-Logik` ×1, `Quad-Constraint-Erhaltung` ×1, `Quads` ×1 |
| `Driver` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#10] | 10 | 13 | 180, 527, 607, 643, 669, 688, 690, 746, 921, 922, 925, 935 … | `Driver-Pivot` ×2, `Drivers` ×1 |
| `Limit` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#5] | 5 | 11 | 180, 527, 607, 643, 669, 688, 746, 921, 922, 935, 1052 | `Limit-Regel` ×4, `Limits` ×1, `Limit-Konsistenz` ×1 |
| `Outcome` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#10] | 10 | 12 | 24, 136, 152, 180, 607, 643, 669, 746, 921, 922, 935, 1052 | `Outcome-Specification` ×1, `Outcome-Spezifikation` ×1 |
| `Judgment` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#6] | 6 | 9 | 180, 607, 643, 669, 746, 921, 922, 935, 1052 | `Judgment-Regel` ×3 |
| `Optionlock` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 607 |  |
| `Timelock` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 607 |  |
| `Concerns` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#3] | 3 | 3 | 180, 608, 644 |  |
| `Issues` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#3] | 3 | 3 | 180, 608, 644 |  |
| `Problems` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#3] | 3 | 3 | 180, 608, 644 |  |
| `Solutions` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#3] | 3 | 3 | 180, 608, 644 |  |
| `Storypoints` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#4] | 4 | 8 | 138, 180, 608, 620, 652, 656, 746 |  |
| `Dynamics` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 3 | 517, 607, 745 | `Dynamics-Sechsergruppen` ×1, `Dynamics-Set` ×1 |
| `Dialetheia` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#0] | 0 | 3 | 375, 395, 656 | `Dialetheia-tolerant` ×1, `Dialetheia-Logik` ×1, `Dialetheia-Achsen` ×1 |
| `Deus ex Machina` ^[research-prompt-dual-storyform-rebuild-kohaerenz-protokoll-m.md:#1] | 1 | 1 | 359 |  |

## What the extraction ran into

The facts above, explained.

**Zeros (15).** All fifteen are written differently here, not absent. Twelve are the names of the alters in the Alter-System bullet (`Lex`, `Alex`, `Rhys`, `Selene`, `Nyx`, `Kiko`, `Lia`, `Isabelle`, `Moros`, `Argus`, `Silas`, `Oblivion`): the line writes each only as the first half of a hyphenated compound with its role word (`Lex-Rationalist`, `Alex-Beschützer`, `Rhys-Pfleger`, `Selene-ISH`, `Nyx-Fight`, `Kiko-Freeze`, `Lia-Ambivalent`, `Isabelle-Sexualisiert`, `Moros-Kollaps`, `Argus-Meta`, `Silas-Juna-Echo`, `Oblivion-AEGIS-Echo`) ^[L379], so the standing-alone count is 0 and the compound count is 1 each. `Silas-Juna-Echo` and `Oblivion-AEGIS-Echo` are listed whole as well and count 1. `Wächter-Zwiespalt` is an inflection and a compound: the Primer writes the genitive „Träger des“ ^[L371] with `Wächter-Zwiespalts` and the open-questions line writes `Wächter-Zwiespalt-Soziopolitik`. `Mnemosyne-Archipel` stands only inside `Mnemosyne-Archipel-Konvergenz` in the T6 row. `Dialetheia` stands only inside compounds (`Dialetheia-tolerant`, `Dialetheia-Logik`, `Dialetheia-Achsen`); the Logik compound is listed whole and counts 1. `Argus-Meta` is a role compound on the Argus line and is not a separate candidate.

**Standing alone less often than with compounds (35).** Mostly hyphenated role or compound uses (`Kael-Host`, `AEGIS-Sensoren`, `NotebookLM-Notebooks` 14 times, `Spiegelregel-` compounds, `Limit-Regel`). Three rows carry a substring warning that is not the same word: `Mind` also finds `mindestens`/`Mindestens` (the Dramatica domain `Mind` is the 6 whole-word uses), `Limit` finds `Limits` and `Limit-` compounds, and `Dialetheia` is the compound case above.

**Export artifacts.** 286 backslash escapes (`\_`, `\[`, `\#`, `\*\*` in the table rows and the output-schema template, which the export wrote as escaped markdown instead of a code fence); the numbered lists all start with `1.` as the export renders them, so ordinals do not identify steps by their digit; 92 glued reference numbers (digits that sit against words, for instance `13 Alters`, which `read.py --find` drops, so such lines are quoted around the digit). Quotation marks are mixed: an opening curly mark with a straight closing mark throughout the Primer and the method blocks. The document never writes a subscripted form: `K0`, `K1`, `KW1` to `KW4` are plain digits (no subscript character in the file), and `π_D`, `π_P` stand with an escaped underscore on most lines (`π\_D`) and without it on one (L805). No candidate carries a comma, ordinal or abbreviation.

**What the reading met.** The Primer is dense and sits in L347 to L399; the rest is method. The prompt states its own standing in two places: the earlier architecture material, `Storyform A` (`Heuristics of Integration`) and `Storyform B` (`Phoenix Collapse`), is declared not canon ^[L399], and the prompt itself bars any output that canonises a variant (L298). These are the prompt's claims about status, recorded here and applied to nothing. The prompt says „keine politische Throughline“ ^[L299] and „Therapeutische Glättung“ ^[L301] as output exclusions. Numbers inside the prompt that do not agree with each other are listed in the note, section 6.

**Zeros:** 15 — `Lex`, `Alex`, `Rhys`, `Selene`, `Nyx`, `Kiko`, `Lia`, `Isabelle`, `Moros`, `Argus`, `Silas`, `Oblivion`, `Wächter-Zwiespalt`, `Mnemosyne-Archipel`, `Dialetheia`.

**Standing alone less often than with compounds:** 35 — `Kael` 9/10, `Juna` 9/12, `AEGIS` 18/22, `Moonshine-Link` 2/3, `Mnemosyne` 1/2, `Kernwelten` 2/3, `KW2` 1/2, `KW3` 1/2, `ANP` 1/2, `EP` 1/2, `DKT` 1/2, `Erasure` 1/2, `Erasonen` 2/3, `Coheronen` 2/3, `Vortex` 1/2, `Dual-Mapping` 3/6, `Spiegelregel` 14/25, `Mirror-Operator` 2/3, `MAPIT` 7/8, `ReAct` 3/6, `NotebookLM` 6/21, `Contradiction Log` 15/17, `Architecture` 4/8, `Tensioning` 5/7, `Throughline` 15/23, `Universe` 6/7, `Mind` 6/10, `Perspektiven` 5/8, `Quad` 2/10, `Driver` 10/13, `Limit` 5/11, `Outcome` 10/12, `Judgment` 6/9, `Storypoints` 4/8, `Dynamics` 1/3.
