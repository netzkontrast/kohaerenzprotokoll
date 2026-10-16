---
source: Sources/drive/research-prompt-kohaerenz-protokoll-verification-md.md
drive_id: "16NBS_PWcAMhHjNzS5q8w9Yhm709Ur_ut_AOsgbSt-OI"
title: "research-prompt_kohaerenz-protokoll-verification.md"
category: kernkonzept
index_date: "2026-04-29"
extracted: "2026-10-16"
candidates: 63    # the terms capture.py counted
---

# Term census — research-prompt_kohaerenz-protokoll-verification.md

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py research-prompt-kohaerenz-protokoll-verification-md`

```
  lines                1428  (frontmatter ends at 9)
  body words           6022
  headings             34   bold-only lines 61
  table rows           16   code fences 0
  question marks       88
  backslash escapes    194
  typographic marks    68   ascii quotes 256
  invisible characters none
  math symbol lines    7
  glued ref numbers    53
  repeated labels      Observe x20, Reason x18, Act (Search Protocol M06 + M01) x8, What it is x5, Act (Search Protocol M01 + M06) x4, Act (Search Protocol M06) x4, Example trigger in this research context x4, How to apply it — step by step x4, When to stop / escape criterion x4, Why it is in this prompt x4, Method Adherence x3
  longest line         360 chars
```

## Stance, read per passage

The document is an instruction to a research agent, written in English around a German title, and speaks throughout in the imperative and in the voice of a plan. It does not narrate the novel; the world's names stand inside claims it says the framework makes („The framework claims …“ ^[L656]), in one input list and in two step headings.

Frontmatter and opening (L15–L48): a metadata block names the topic, method labels and a creation date, then „This research prompt uses three integrated layers:“ ^[L34] and lists them. The first layer calls the task an audit of „an existing theoretical framework“ against published sources ^[L38].

Constraint blocks (L52–L167): rules marked as MANDATORY or as a block number. One block excludes the story from the audit: „Narrative application is the writer's responsibility; your task is framework verification.“ ^[L135] Another prescribes a record format for contradictions: „Every contradiction enters the final Contradiction Log, not a silent note.“ ^[L167]

Method sections (L209–L390): each method is defined under the same repeated labels (What it is, Why it is in this prompt, How to apply it, When to stop, Example trigger). The document describes its own subject there: „The Kohärenz-Protokoll framework is self-contained and coherent.“ ^[L354] An example trigger also names AEGIS, at ^[L342].

Role, input and steps (L492–L1190): each step is a Reason, Act, Observe triple. Plot-world claims appear inside „Reason:“ lines, each introduced by „The framework claims“ and set in quotation marks, so the speaker of such a line is the framework the prompt reports, not the prompt (for example ^[L875], ^[L1053], ^[L1078], ^[L1104]).

Output schema and checklists (L1196–L1427): a table of empty fields, a report skeleton and two checklists. The closing line declares its own standing: „This prompt is ready for autonomous research execution.“ ^[L1421]

Voice and speaker: the prompt addresses an executing agent in the second person and names no narrator of the novel. Quotation marks in this document mark claims of the audited framework and search strings, not invention. Candidates that stand only in a search string or a Reason line are the framework's claims as reported; the prompt itself defines none of the world's names.

## Candidates and counts

63 candidates, written while reading and frozen by the count (`Plan/runs/research-prompt-kohaerenz-protokoll-verification-md/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `research-prompt-kohaerenz-protokoll-verification-md.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kael` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#3] | 3 | 3 | 125, 656, 1053 |  |
| `Juna` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#3] | 3 | 3 | 538, 871, 875 |  |
| `AEGIS` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#5] | 5 | 5 | 342, 656, 1053, 1074, 1078 |  |
| `Lex` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#2] | 2 | 2 | 724, 1053 |  |
| `Nyx` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#2] | 2 | 2 | 724, 1053 |  |
| `Kiko` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#2] | 2 | 2 | 724, 1053 |  |
| `Lia` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#2] | 2 | 2 | 724, 1053 |  |
| `Mnemosyne-Archipel` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#3] | 3 | 3 | 625, 634, 1273 |  |
| `Nichts-Rauschen` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#1] | 1 | 1 | 990 |  |
| `Algo Melancholie` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#1] | 1 | 1 | 1074 |  |
| `Algorithmische Melancholie` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#1] | 1 | 1 | 1047 |  |
| `Silence` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#3] | 3 | 3 | 1100, 1104, 1209 |  |
| `foundational phone call` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#1] | 1 | 1 | 1104 |  |
| `Vortex Inversion` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#1] | 1 | 1 | 1049 |  |
| `Climax Inversion` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#3] | 3 | 3 | 362, 498, 1047 |  |
| `Reader Function` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#4] | 4 | 4 | 362, 498, 538, 932 |  |
| `Reader/Witness Function` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#1] | 1 | 1 | 986 |  |
| `Witness Function` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#2] | 2 | 2 | 538, 986 |  |
| `Husserlian Spectator` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#1] | 1 | 1 | 1016 |  |
| `transcendental ego` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#2] | 2 | 2 | 1016, 1024 |  |
| `Dual-Kernel Theory` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#5] | 5 | 5 | 534, 589, 621, 633, 636 |  |
| `DKT` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#9] | 9 | 9 | 98, 129, 245, 362, 498, 640, 644, 688, 1205 |  |
| `K\_1` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#9] | 9 | 10 | 245, 342, 534, 621, 625, 635, 749, 1100, 1173 |  |
| `K\_0` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#8] | 8 | 8 | 245, 342, 534, 621, 625, 635, 1173 |  |
| `K\_1/K\_0` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#4] | 4 | 4 | 245, 534, 625, 1173 |  |
| `Moonshine-Link` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#3] | 3 | 3 | 845, 849, 1173 |  |
| `Monster Group` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#17] | 17 | 17 | 99, 114, 130, 269, 293, 372, 536, 577, 784, 790, 794, 802 … |  |
| `Leech Lattice` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#8] | 8 | 9 | 99, 130, 269, 536, 820, 824, 832, 833, 837 |  |
| `VOA` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#9] | 9 | 9 | 98, 114, 130, 577, 784, 824, 833, 837, 883 |  |
| `orbifold construction` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#3] | 3 | 4 | 130, 871, 883, 885 |  |
| `Orbifold Construction` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#1] | 1 | 1 | 875 |  |
| `Landauer heat` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#3] | 3 | 3 | 656, 1049, 1053 |  |
| `Landauer heat spike` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#2] | 2 | 2 | 1049, 1053 |  |
| `informational firewalls` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#1] | 1 | 1 | 728 |  |
| `Janetian action systems` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#2] | 2 | 2 | 535, 711 |  |
| `Apparently Normal Parts` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#1] | 1 | 1 | 712 |  |
| `Emotional Parts` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#1] | 1 | 1 | 712 |  |
| `Autobiographical Anchor` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#1] | 1 | 1 | 1047 |  |
| `Participatory Universe` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#1] | 1 | 1 | 538 |  |
| `Information Thermodynamics` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#2] | 2 | 2 | 534, 589 |  |
| `Psychological Modularity` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#2] | 2 | 2 | 535, 696 |  |
| `Paraconsistent Logic` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#2] | 2 | 2 | 537, 932 |  |
| `Algorithmic Advance` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#1] | 1 | 1 | 537 |  |
| `Structural Waveforms` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#1] | 1 | 1 | 536 |  |
| `Monstrous Symmetry` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#1] | 1 | 1 | 536 |  |
| `Axis I` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#10] | 10 | 17 | 86, 87, 88, 342, 388, 420, 534, 535, 536, 589, 595, 686 … |  |
| `Hidden Contradiction Discovery Protocol` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#1] | 1 | 1 | 23 |  |
| `Assumption Stability Audit` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#2] | 2 | 2 | 24, 1161 |  |
| `Contradiction Log` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#16] | 16 | 18 | 21, 141, 167, 195, 273, 299, 313, 448, 583, 644, 1211, 1300 … |  |
| `Source Triangulation` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#6] | 6 | 6 | 20, 191, 251, 1239, 1305, 1351 |  |
| `Adversarial Query Expansion` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#4] | 4 | 4 | 22, 348, 404, 462 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `TSDP` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#26] | 26 | 26 | 100, 114, 125, 129, 362, 370, 371, 498, 535, 548, 576, 696 … |  |
| `Dramatica` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#11] | 11 | 11 | 362, 498, 536, 577, 784, 897, 901, 909, 910, 914, 1207 |  |
| `Dialetheism` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#10] | 10 | 10 | 362, 498, 537, 578, 934, 938, 946, 948, 952, 1208 |  |
| `Moonshine` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#11] | 11 | 14 | 98, 129, 362, 498, 536, 784, 845, 849, 857, 859, 863, 1173 … | `Moonshine-Link` ×3 |
| `Landauer's Principle` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#13] | 13 | 13 | 225, 370, 388, 534, 575, 591, 595, 603, 604, 605, 613, 1174 |  |
| `Halting Probability` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#3] | 3 | 3 | 960, 964, 972 |  |
| `Omega` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#5] | 5 | 5 | 537, 960, 964, 972, 974 |  |
| `Falsification` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#3] | 3 | 3 | 19, 211, 1300 |  |
| `ReAct` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#9] | 9 | 9 | 22, 42, 396, 398, 470, 1383, 1404 |  |
| `RISEN` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#14] | 14 | 14 | 22, 46, 452, 468, 470, 474, 492, 520, 554, 897, 1196, 1262 … |  |
| `quad structure` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#3] | 3 | 3 | 897, 901, 909 |  |
| `storyform` ^[research-prompt-kohaerenz-protokoll-verification-md.md:#1] | 1 | 1 | 910 |  |

## What the extraction ran into

**Zeros:** 0. Every candidate was tested with the standing-alone pattern before the count and none stood at 0.

**Export damage:** the document writes the kernel symbols with an escaped underscore, `K\_1` and `K\_0`, and the list keeps them as written; `read.py --find` strips the escape and the digit glued to the symbol, so quotations around them stop before the symbol.

**Standing alone less often than with compounds:** `Leech Lattice` also stands in a plural (^[L269]), `Contradiction Log` in „Contradiction Logging Format“ (^[L141]), `orbifold construction` in a plural (^[L885]); `Axis I` is the stem of the other numerals (Axis II and so on); `Moonshine` is the stem of `Moonshine-Link`. The reader has not looked at the one remaining difference for `K\_1`.

**Document-type note:** the document is a prompt, not a canon text. Most of its candidates are method vocabulary or lens vocabulary (the `## lens` rows), and the world's names (Kael, Juna, AEGIS and the four alters) occur only inside reported claims, in a handful of lines each.


**Zeros:** 0.

**Standing alone less often than with compounds:** 6 — `K\_1` 9/10, `Leech Lattice` 8/9, `orbifold construction` 3/4, `Axis I` 10/17, `Contradiction Log` 16/18, `Moonshine` 11/14.
