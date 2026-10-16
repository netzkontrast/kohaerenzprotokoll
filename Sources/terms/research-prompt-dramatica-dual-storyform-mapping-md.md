---
source: Sources/drive/research-prompt-dramatica-dual-storyform-mapping-md.md
drive_id: "1E9mumGPuWIJbo95MW5Yr1pOyVVuNiG07A1KTaBStN_Q"
title: "research-prompt_dramatica-dual-storyform-mapping.md"
category: storyform
index_date: "2026-04-30"
extracted: "2026-10-11"
candidates: 119    # the terms capture.py counted
---

# Term census — research-prompt_dramatica-dual-storyform-mapping.md

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py research-prompt-dramatica-dual-storyform-mapping-md`

```
  lines                1040  (frontmatter ends at 9)
  body words           6457
  headings             43   bold-only lines 12
  table rows           0   code fences 0
  question marks       48
  backslash escapes    176
  typographic marks    274   ascii quotes 173
  invisible characters none
  math symbol lines    18
  glued ref numbers    78
  repeated labels      Example trigger in this research context x5, How to apply it — step by step x5, What it is x5, When to stop / escape criterion x5, Why it is in this prompt x5
  longest line         619 chars
```

## Stance, read per passage

This document is a prompt: it asks for work and specifies how the work is to be done, and it reports no finding of its own. It addresses an executing agent in the second person („Dieser Prompt ist vollständig selbsthaltend“ ^[L45]) and closes with an order („Ende des Forschungsprompts. Führe jetzt aus.“ ^[L1039]). What it says about the novel is a brief it hands over, not a reading of the novel.

- **Front matter and header (L11 to L45).** A flattened block of the prompt generator's fields (topic, methods, frameworks, constraint blocks, version), then the title and an address to the agent. It is configuration of the prompt, not statements about the novel. The export has run the fields together on a few lines and escaped underscores.
- **Meta-Header and MIRROR (L51 to L157).** Plan and self-description of the prompt. The search is declared an exploration, not an extraction: „Diese Recherche ist eine Exploration, keine Extraktion.“ ^[L57]. The structural frame is named a made-to-measure one: „bespoke Framework synthetisiert“ ^[L121], and its six components are traced to RISEN, TIDD-EC, CRISPE, CARE and CO-STAR as provenance „für Auditierbarkeit“ ^[L142]. These framework names are borrowed lens terms that the prompt cites only as sources of its own MIRROR parts.
- **Forschungsziel (L161 to L181).** The task, in the imperative: define a mirroring of two Dramatica storyforms and produce at least two alternatives. It states a standing of the earlier storyforms: „Keiner der bisherigen Storyforms gilt als Kanon.“ ^[L225], attributed by the prompt to a dated user directive. This is a claim the prompt makes about the status of other material and is recorded, not applied.
- **Story-Hintergrund (L187 to L225).** A block of one-line capsule descriptions of the novel's world, with the instruction that they serve as constraints and are not to be elaborated ^[L189]. Each capsule (Kael, AEGIS, Juna, Moonshine-Link, Guardians, Alter-System, Dual-Kernel-Theorie, Vortex-Inversion) is a summary the prompt gives of the novel, not a reading with evidence.
- **Constraint Blocks 0 to 5 (L231 to L332).** Rules: reflection after each checkpoint, source priority, temporal scope, exclusions, a limit of two sentences per story concept („Dieser Block hat Vorrang vor jedem Drang nach Vollständigkeit der Story-Beschreibung.“ ^[L313]), and the questioning of notebooks. A rulebook, not a report.
- **Critical-Thinking Methods (L336 to L499).** Five methods, each with five repeated labels (What it is, Why it is in this prompt, How to apply it, When to stop, Example trigger). The labels are the template, not terms; the example triggers are sample situations for the agent, for instance a pair of invented notebook statements about Juna and the Quad ^[L419]; they are not claims about the novel.
- **MIRROR sections (L503 to L585).** The formal contract: axioms of Dramatica (domains, pronouns, a tuple of driver, limit, outcome and judgment) and a definition of a valid mirroring. These are borrowed theory stated as rules to restate, with the hard constraint of two levels per throughline („Drei oder mehr Ebenen sind verboten“ ^[L533]).
- **Steps 1 to 10 (L589 to L759).** A plan in order. Two steps are imported from other prompt categories and labelled as such („Dieser Step importiert eine Extraktions-Disziplin aus Kategorie B“ ^[L687]).
- **Integrity check, synthesis schema, checklist (L763 to L1023).** A checklist of confirmations the agent must write and an empty output template with placeholders in square brackets (the Synthesis block is escaped markdown inside the export). Nothing in it is filled.
- **Spezial-Erinnerung (L1029 to L1039).** A last reminder: „Das Notebook ist Sparringspartner, nicht Orakel.“ ^[L1031].

The prompt speaks of itself as a prompt (`Restate` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#7] stands seven times as an instruction word) and uses `Kanon` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#4] four times, always about the status of other storyforms or as a negation; none of these statements sets a canon.

## Candidates and counts

119 candidates, written while reading and frozen by the count (`Plan/runs/research-prompt-dramatica-dual-storyform-mapping-md/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `research-prompt-dramatica-dual-storyform-mapping-md.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kohärenz Protokoll` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#6] | 6 | 6 | 15, 43, 45, 57, 163, 813 |  |
| `Kael` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#5] | 5 | 5 | 193, 205, 213, 313, 559 |  |
| `AEGIS` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#6] | 6 | 8 | 197, 201, 205, 209, 213, 217, 313, 559 | `AEGIS-unsichtbar` ×1, `AEGIS-Echo` ×1 |
| `Juna` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#12] | 12 | 19 | 131, 175, 201, 205, 213, 313, 419, 539, 551, 560, 570, 637 … | `Juna-Anker` ×3, `Juna-Echo` ×1, `Juna-Anker-Punkte` ×1, `Juna-Verankerung` ×1 |
| `Moonshine-Link` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#2] | 2 | 2 | 205, 313 |  |
| `Guardians` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 209 |  |
| `LogOS` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 209 |  |
| `Mnemosyne` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 209 |  |
| `Cerberus` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 209 |  |
| `Kairos/Sophia` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 209 |  |
| `Kernwelten` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 209 |  |
| `Alter-System` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#2] | 2 | 2 | 193, 213 |  |
| `ANPs` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 193 |  |
| `EPs` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 193 |  |
| `Sonder-Alter` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 193 |  |
| `Spiegel-Alter` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 193 |  |
| `Host` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 3 | 213, 317, 1031 | `Hostsystem` ×2 |
| `Rationalist` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 213 |  |
| `Beschützer` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 213 |  |
| `Versorger` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 213 |  |
| `ISH` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 213 |  |
| `Fight` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 213 |  |
| `Freeze` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 213 |  |
| `Ambivalent` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 213 |  |
| `Sexualisiert` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 213 |  |
| `Kollaps` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 2 | 197, 213 | `Kollaps-Kern` ×1 |
| `Meta-Kognitiv` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 213 |  |
| `Juna-Echo` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 213 |  |
| `AEGIS-Echo` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 213 |  |
| `Dual-Kernel-Theorie` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 217 |  |
| `DKT` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#2] | 2 | 2 | 217, 313 |  |
| `Kohärenz-Kern` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 217 |  |
| `Entropie-Kern` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 217 |  |
| `Vortex-Inversion` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#2] | 2 | 2 | 221, 313 |  |
| `Leech-Lattice` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 205 |  |
| `Vertex-Operator-Algebra` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 205 |  |
| `Landauer-Hitze` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 197 |  |
| `Erasure-Sweeps` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 197 |  |
| `Quanten-Witness` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 201 |  |
| `Gödel-Satz` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 201 |  |
| `Chaitin` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#0] | 0 | 1 | 201 | `Chaitin-Ω` ×1 |
| `Heuristics of Integration` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#3] | 3 | 3 | 163, 306, 679 |  |
| `Phoenix Collapse` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#3] | 3 | 3 | 163, 306, 679 |  |
| `MIRROR` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#11] | 11 | 17 | 23, 119, 121, 125, 138, 155, 243, 503, 505, 545, 624, 628 … | `MIRROR-bindend` ×3, `MIRROR-Komponente` ×1, `MIRROR-Vertrag` ×1, `MIRROR-Framework-Synthese` ×1 |
| `Dual-Storyform-Spiegelung` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#4] | 4 | 6 | 57, 65, 163, 446, 527, 630 | `Dual-Storyform-Spiegelungen` ×2 |
| `Dual-Mapping-Spiegelung` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#2] | 2 | 2 | 130, 167 |  |
| `Spiegelungs-Definition` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#3] | 3 | 3 | 138, 527, 825 |  |
| `Mathematische Axiome` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#3] | 3 | 3 | 24, 129, 505 |  |
| `Inversions-Spiegel-Definition` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#3] | 3 | 3 | 25, 130, 545 |  |
| `Reibungs-Topologie` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#5] | 5 | 5 | 26, 131, 148, 553, 921 |  |
| `Rationalisierungs-Audit` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#8] | 8 | 8 | 29, 134, 151, 572, 585, 743, 745, 969 |  |
| `Anti-Rationalisierungs-Wächter` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 285 |  |
| `Output-Alternativen` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#3] | 3 | 3 | 28, 133, 568 |  |
| `Hypothesen-Baum` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#4] | 4 | 5 | 68, 691, 713, 741, 833 | `Hypothesen-Baum-Struktur` ×1 |
| `Mapping-Hypothese` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#7] | 7 | 11 | 65, 132, 322, 325, 354, 531, 566, 641, 691, 721, 837 | `Mapping-Hypothesen` ×4 |
| `Validitäts-Kriterium` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 539 |  |
| `Sekundär-Schicht` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#3] | 3 | 6 | 551, 562, 570, 637, 861, 925 | `Sekundär-Schicht-Wahl` ×1, `Sekundär-Schicht-Reibung` ×1, `Sekundär-Schicht-Reibungspunkte` ×1 |
| `Throughline-Kreuzungen` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#2] | 2 | 2 | 559, 925 |  |
| `Juna-Anker` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#3] | 3 | 5 | 560, 570, 861, 865, 925 | `Juna-Anker-Punkte` ×1, `Juna-Anker-Mechanismus` ×1 |
| `Reflexions-Template` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 251 |  |
| `Restatement Checkpoint` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#3] | 3 | 3 | 593, 595, 1009 |  |
| `Pre-Synthesis Integrity Check` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#5] | 5 | 5 | 103, 246, 489, 751, 1018 |  |
| `CONSTRAINT BLOCK` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#23] | 23 | 24 | 231, 233, 287, 295, 299, 311, 315, 601, 602, 603, 604, 605 … |  |
| `Reflection Baseline` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#4] | 4 | 4 | 32, 233, 601, 1010 |  |
| `Source Priority Rules` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#3] | 3 | 3 | 33, 287, 602 |  |
| `Temporal Scope` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#4] | 4 | 4 | 34, 295, 603, 1016 |  |
| `Output Exclusions` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#4] | 4 | 4 | 35, 299, 604, 1017 |  |
| `Story-Knappheit-Disziplin` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#3] | 3 | 3 | 36, 311, 605 |  |
| `Contradiction Log` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#14] | 14 | 14 | 21, 293, 329, 394, 408, 410, 481, 617, 659, 773, 929, 1013 … |  |
| `Query Expansion Log` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#7] | 7 | 7 | 328, 477, 659, 781, 937, 1011, 1019 |  |
| `Adversarial Query Expansion` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#10] | 10 | 10 | 23, 83, 117, 448, 614, 661, 663, 773, 1011, 1013 |  |
| `Falsification` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#6] | 6 | 6 | 19, 340, 615, 733, 773, 1013 |  |
| `Steelmanning` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#8] | 8 | 8 | 20, 367, 388, 616, 677, 679, 773, 1013 |  |
| `First-Principles Decomposition` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#6] | 6 | 6 | 22, 421, 618, 630, 773, 1013 |  |
| `Hypothesis Half-Life Audit` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#2] | 2 | 2 | 715, 953 |  |
| `Surviving-Mapping-Triangulation` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#2] | 2 | 2 | 30, 685 |  |
| `Cross-Pollination` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#2] | 2 | 3 | 785, 945, 1019 | `Cross-Pollination-Audit` ×1 |
| `single-source-supported` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 709 |  |
| `contested` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#2] | 2 | 2 | 357, 837 |  |
| `NotebookLM` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#8] | 8 | 15 | 33, 37, 45, 132, 290, 315, 317, 409, 564, 606, 655, 789 … | `NotebookLM-Notebooks` ×5, `NotebookLM-Adversarial-Befragung` ×1, `NotebookLM-Mandat` ×1 |
| `ReAct` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#2] | 2 | 3 | 23, 75, 77 | `ReAct-Zyklus` ×1 |
| `Exploration` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#4] | 4 | 5 | 15, 55, 57, 687, 717 |  |
| `Dramatica-Quad-Axiom` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 511 |  |
| `Pronomen-Achse` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#4] | 4 | 5 | 129, 130, 515, 532, 725 | `Pronomen-Achsen` ×1 |
| `Driver-Limit-Outcome-Tupel` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 427 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Dramatica` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#25] | 25 | 48 | 15, 31, 33, 34, 43, 45, 129, 138, 181, 201, 289, 290 … | `Dramatica-Theorie` ×6, `Dramatica-Primärquellen` ×3, `Dramatica-Axiome` ×2, `dramatica-dual-storyform-mapping` ×1 |
| `Storyform` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#8] | 8 | 30 | 15, 43, 57, 65, 133, 163, 167, 221, 225, 306, 373, 392 … | `Storyforms` ×6 |
| `Throughline` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#18] | 18 | 23 | 130, 177, 427, 511, 515, 531, 533, 534, 551, 559, 560, 561 … | `Throughlines` ×2, `Throughline-Kreuzungen` ×2, `throughlines` ×1 |
| `Domain` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#11] | 11 | 26 | 129, 355, 427, 454, 511, 515, 531, 533, 551, 562, 570, 636 … | `Domain-Inversion` ×3, `Domain-Muster` ×3, `Domain-Inversionsmuster` ×2, `Domain-Achsen` ×1 |
| `Quad` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#3] | 3 | 12 | 129, 175, 201, 419, 427, 493, 511, 634, 637, 725 | `Quad-Struktur` ×1, `Quad-Pronomen` ×1, `Quad-Methodologien` ×1, `Quad-Strukturen` ×1 |
| `Universe` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#8] | 8 | 8 | 167, 365, 392, 511, 531, 679 |  |
| `Mind` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#9] | 9 | 15 | 65, 133, 167, 285, 355, 365, 373, 511, 531, 679, 849 | `mindestens` ×14, `Mindestens` ×4, `Mind-Physics` ×1, `Minderheits-` ×1 |
| `Physics` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#7] | 7 | 8 | 167, 355, 365, 511, 531, 679 |  |
| `Psychology` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#8] | 8 | 8 | 167, 365, 392, 511, 531, 679 |  |
| `Driver` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#4] | 4 | 7 | 129, 221, 427, 472, 519, 889 | `Driver-Pivot` ×1, `Driver-Limit-Outcome-Tupel` ×1 |
| `Limit` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#4] | 4 | 5 | 129, 427, 519, 889 |  |
| `Outcome` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#4] | 4 | 8 | 129, 221, 427, 519, 535, 889 | `Outcomes` ×2, `Outcome-Asymmetrie` ×1 |
| `Judgment` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#2] | 2 | 5 | 129, 519, 535, 889 | `Judgment-Tupel` ×2, `Judgments` ×1 |
| `Optionlock` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 519 |  |
| `Timelock` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 519 |  |
| `Resolve` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 2 | 523 |  |
| `Growth` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#2] | 2 | 2 | 523 |  |
| `Approach` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#2] | 2 | 2 | 523 |  |
| `Steadfast` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 523 |  |
| `Do-er` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 523 |  |
| `Be-er` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 523 |  |
| `Holistic` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 523 |  |
| `Popper` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#2] | 2 | 2 | 19, 340 |  |
| `RISEN` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#9] | 9 | 9 | 24, 25, 27, 28, 121, 146, 147, 149, 150 |  |
| `TIDD-EC` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#7] | 7 | 7 | 24, 26, 27, 121, 146, 148, 149 |  |
| `CO-STAR` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#3] | 3 | 3 | 28, 121, 150 |  |
| `CARE` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#5] | 5 | 5 | 26, 29, 121, 148, 151 |  |
| `CRISPE` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#5] | 5 | 5 | 25, 29, 121, 147, 151 |  |
| `Gruppentheorie` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#3] | 3 | 3 | 181, 292, 454 |  |
| `Kategorientheorie` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#3] | 3 | 3 | 454, 473, 671 |  |
| `Topos-Theory` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 671 |  |
| `Sheaf-Cohomology` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 671 |  |
| `Type Theory` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#2] | 2 | 2 | 473, 671 |  |
| `Bayesian-Networks` ^[research-prompt-dramatica-dual-storyform-mapping-md.md:#1] | 1 | 1 | 671 |  |

## What the extraction ran into

**The one zero, `Chaitin`.** The line writes the name joined to a symbol, `Chaitin-Ω`: the hyphen glues it, so it stands alone 0 times and 1 time inside the compound (the table row shows `Chaitin-Ω` as the surface). It is an inflection-like compound, not an absence and not export damage: the Ω survived the export in the raw file.

**Standing alone less often than with compounds (28 rows).** Each is a compound or a longer word that contains the candidate, not a second sense, with these readings of the lines:
- Names of the world: `AEGIS` is also in `AEGIS-Echo` and `AEGIS-unsichtbar`; `Juna` is also in `Juna-Anker`, `Juna-Echo`, `Juna-Anker-Punkte` and `Juna-Verankerung`; `Kollaps` is also in `Kollaps-Kern`.
- `Host` is the name of one of the thirteen alters on one line, and the two other hits are `Hostsystem`, the system hosting the executing agent (the draft marks it substring). The table does not list the alter apart from the host system. `read.py --count "Host"` gives 1 standing alone and 3 in compounds.
- Prompt terms with compounds: `MIRROR` (`MIRROR-bindend`, `MIRROR-Vertrag`, `MIRROR-Komponente`, `MIRROR-Framework-Synthese`), `Dual-Storyform-Spiegelung` (plural `Dual-Storyform-Spiegelungen`), `Hypothesen-Baum` (`Hypothesen-Baum-Struktur`), `Mapping-Hypothese` (plural `Mapping-Hypothesen`, four), `Sekundär-Schicht`, `Juna-Anker`, `CONSTRAINT BLOCK` (once in a longer compound), `Cross-Pollination` (`Cross-Pollination-Audit`), `NotebookLM` (`NotebookLM-Notebooks`, five, `NotebookLM-Mandat`), `ReAct` (`ReAct-Zyklus`), `Exploration`, `Pronomen-Achse` (`Pronomen-Achsen`).
- Borrowed Dramatica words, where the document joins them: `Dramatica` (`Dramatica-Theorie`, `Dramatica-Primärquellen`, `Dramatica-Axiome` and the slug in the front matter), `Storyform` (plural `Storyforms`, and the front matter slug in lower case), `Throughline` (plural `Throughlines`, `Throughline-Kreuzungen`), `Domain` (`Domain-Inversion`, `Domain-Muster`, `Domain-Achsen`), `Quad` (`Quad-Struktur`, `Quad-Pronomen`, `Quad-Methodologien`, `Quad-Strukturen`), `Driver`, `Limit`, `Outcome`, `Judgment` (`Judgment-Tupel`), `Physics` (`Mind-Physics`), `Resolve` (a second hit in the same line).
- `Mind` stands alone 9 times, but its compound count of 15 includes 14 `mindestens` and 4 `Mindestens`, which are the ordinary German adverb for 'at least' and not the Dramatica domain. The count mark for `Mind` is therefore the right figure and the compound figure is not.

**Export artifacts.** The profile gives 176 backslash escapes and 78 glued reference numbers. Digits are lost or glued in several places: the core names are written `K1` and `K0` in the raw file (the document writes no subscripted form, and `read.py --find` prints the sentence with the digit dropped), formulas appear as `$\\Sigma\_A$`, and numerals in headings such as `CONSTRAINT BLOCK 0` are glued, so `--find` shows them without a digit. The front matter runs several fields together on one line and escapes underscores (`research\_category`). The Synthesis template is escaped markdown inside the text (`\#\#`). The mathematics is LaTeX in dollar signs; none of its symbols is a candidate. Five labels repeat five times each (the profile lists them): they are the template of the five methods, not terms.

**Not listed on purpose.** The stub placeholders `Σ`, the step labels `S6` and `S7`, the indices `M.1` to `M.6` and the method labels `M01` and `M13` are names of slots in the template; the ordinary German words are left out. The five pronouns of Dramatica are written `I`, `You`, `They`, `We` and are too short to count meaningfully; they are not listed.

**The prompt's own standing.** The document says of itself: „Dieser Prompt ist vollständig selbsthaltend.“ ^[L45] It claims no canon for itself; it says that earlier storyforms are no longer canon and that the steelman it asks for is „Vergleichspunkt, nicht Lösung“ ^[L683]. Both are recorded, not applied.

**Spelling of the novel's own title.** The title is written `Kohärenz Protokoll` (no hyphen) in the topic, the heading and the body.

The facts the extraction lists, kept as drafted:

**Zeros:** 1 — `Chaitin`.

**Standing alone less often than with compounds:** 28 — `AEGIS` 6/8, `Juna` 12/19, `Host` 1/3, `Kollaps` 1/2, `MIRROR` 11/17, `Dual-Storyform-Spiegelung` 4/6, `Hypothesen-Baum` 4/5, `Mapping-Hypothese` 7/11, `Sekundär-Schicht` 3/6, `Juna-Anker` 3/5, `CONSTRAINT BLOCK` 23/24, `Cross-Pollination` 2/3, `NotebookLM` 8/15, `ReAct` 2/3, `Exploration` 4/5, `Pronomen-Achse` 4/5, `Dramatica` 25/48, `Storyform` 8/30, `Throughline` 18/23, `Domain` 11/26, `Quad` 3/12, `Mind` 9/15, `Physics` 7/8, `Driver` 4/7, `Limit` 4/5, `Outcome` 4/8, `Judgment` 2/5, `Resolve` 1/2.
