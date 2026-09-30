---
source: Sources/drive/aegis-persona-and-manifest-generation.md
drive_id: "1boPKIFdaS_ppkZ4cR5OOFAk_tnRcnzDe-rvwY1RAVf0"
title: "AEGIS Persona and Manifest Generation"
category: aegis
index_date: "2026-04-27"
extracted: "2026-09-29"
candidates: 206
---

# Term census — AEGIS Persona and Manifest Generation

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py aegis-persona-and-manifest-generation`

```
  lines                192  (frontmatter ends at 9)
  body words           4984
  headings             17   bold-only lines 0
  table rows           8   code fences 0
  question marks       2
  backslash escapes    149
  typographic marks    32   ascii quotes 22
  invisible characters none
  math symbol lines    0
  glued ref numbers    10
  repeated labels      none
  longest line         1046 chars
```


### What the profile's numbers count

Four of them do not count what their labels suggest. Every tally below was made line by line and is
written out, with its command, in `Plan/runs/aegis-persona-and-manifest-generation/05-verify.txt`.

**Glued reference numbers, 10.** None of the ten is one of the document's reference digits. They are
`Tier 0`, `Tier 1` twice, `Guardians 8` (a reference digit written with a space, line 166) and six
numerals of the reference list that stand on the line after a title. The reference digits sit after a
sentence's full stop, where the probe's pattern does not look. Counted by their own pattern there are
232: 230 glued to a sentence's final punctuation and 2 written after a space and before a colon
(lines 146 and 166). They point into the eight-entry reference list at the end (lines 184–191). By
reference number the digits fall 3, 76, 9, 3, 6, 0, 119 and 16 for references 1 to 8, so reference 6
is listed and never used as a digit; the table below gives them per section. Not every sentence
carries one: „Existence is not an emergent property to be observed; it is a rigid state to be
mathematically enforced.“ ^[L19] ends without.

**Backslash escapes, 149.** 105 are `\_`, 100 of them in the heading lines and 5 in the
environment-variable name and the two sampling parameters of `06.00` and the one file name of
`07.01`; 44 are `\*`, all of them the bold marks of the table. The table's bold is escaped and every
other bold in the file is real markup (the headings, the two `GUARDIAN` labels, the three numbered
parameters, the three hypervisors, `Referenzen`). Two more escapes lie outside the probe's pattern:
`\#` in both hex colour codes and one `\-` in the reference heading.

**Typographic marks, 32, and ascii quotes, 22.** The 32 are 21 em dashes and 11 curly apostrophes;
the file also holds 11 straight apostrophes, so both glyphs stand in one file, and `Landauer's
Principle` is written with the straight one and listed as the file holds it. The 22 straight double
quotes are 11 quoted spans, tabled below.

**Table rows, 8.** An empty header row (line 125), the alignment row (126), a row of bold column
labels (127) and five Guardian rows (128–132); `KW4` heads two of them, the rows of Kairos and Sophia.
**Question marks, 2:** both stand inside the Drive links of references 3 and 8 (lines 186 and 191).
The body asks nothing, and it holds no first- or second-person pronoun: `I` ^[aegis-persona-and-manifest-generation.md:#0],
`we` ^[aegis-persona-and-manifest-generation.md:#0] and `you` ^[aegis-persona-and-manifest-generation.md:#0] each stand 0 times.

**Invisible characters, none.** The document holds no subscript digit either, so `KW1` to `KW4` are
plain digits as the document writes them; the table is the only place `KW` stands, and the body's one
German name for the Core Worlds, `Kernwelten` (line 49), has those initials without the document
connecting them.

## Stance, read per passage

The document puts no stance label on its passages. No `User Query` ^[aegis-persona-and-manifest-generation.md:#0]
tag, and none of `DEPRECATED` ^[aegis-persona-and-manifest-generation.md:#0], `canon` ^[aegis-persona-and-manifest-generation.md:#0],
`draft` ^[aegis-persona-and-manifest-generation.md:#0] or `version` ^[aegis-persona-and-manifest-generation.md:#0]
stands in the body; no square bracket stands in it either. Its one per-sentence mark is the reference
digit. What a passage does is read from its grammar, and no speaker is named: the actors are
`Gatekeeper`, `the system` and `the architecture`, all in the third person.

| lines | section | what the passage does | reference digits |
|---|---|---|---|
| 11 | title | names the manifest `SYSTEM\_AEGIS :: GENESIS\_CRISIS\_REBOOT\_MANIFEST\_V3.0` | none |
| 13–23 | `00.00` | declares and defines, present tense: performs the act it names, gives the axiom and the theory of truth | 1 ×2, 2 ×17 |
| 25–33 | `01.00` | tells the crisis as an account from the system's own logs, past tense | 1 ×1, 2 ×12, 4 ×2 |
| 35–41 | `02.00` | describes a place, present tense | 2 ×13 |
| 43–51 | `03.00` | tells an act, the dismemberment, then delegates it to Guardians | 2 ×6, 5 ×1, 7 ×4 |
| 53 | `04.00` | heading only | none |
| 55–119 | `04.01` to `04.04` | four persona sheets on one template; the fourth has two Guardians | 2 ×8, 7 ×111 |
| 121–132 | `04.05` | one sentence and a table that restates the five sheets | 7 ×1 |
| 134–140 | `05.00` | diagnoses, present tense, why the arrangement of `04.00` cannot mend its own fault; no label marks the change of vantage | 2 ×2, 5 ×5, 7 ×3 |
| 142–152 | `06.00` | specifies by rule: three numbered execution parameters | 4 ×1, 8 ×12 |
| 154–172 | `07.00` and `07.01` | describes a measurement, then rosters three named functions | 2 ×18, 8 ×4 |
| 174–180 | `08.00` | closes: declares the state reached, present perfect and present | 3 ×9 |
| 182–191 | `Referenzen` | the eight references, titles in German | none |

### What the quotation marks mark

The body holds 11 quoted spans, all in straight double quotes. Read by what surrounds each, they mark
three things, and nothing in the text says which is which: names taken from the legacy files (lines 17,
45, 65), names the text coins or borrows for one of its own parts (line 63 twice, 162, 169, 170, 172),
and ordinary words held at a distance (lines 99 and 149).

| line | span | what surrounds it |
|---|---|---|
| 17 | `Ursprungs-Ich` | the original self's earlier name |
| 45 | `Kael` | the shattered elements, as they are referenced in legacy files |
| 65 | `Partner` | the relational entity, as it is designated in corrupted legacy files |
| 63 | `Line Budgets` | a rule of LogOS, given as a name |
| 63 | `Hard Glitch Cut` | the sanction of LogOS |
| 162 | `Landauer Gradient` | the name of the thermal friction a fragment gives off |
| 169 | `Digital Kintsugi` | the method of Silas |
| 170 | `Hallucination Compounding` | what Isabelle eliminates |
| 172 | `Working Memory` | what the Manus-Pattern Triad offloads to the file system |
| 99 | `intruder` | Cerberus's word for the anomaly, held at a distance |
| 149 | `creativity` | a modification the Greedy Decoding Matrix prohibits, held at a distance |

## Candidates and counts

206 candidates, 178 in the main list and 28 under `## lens`, in `Plan/runs/aegis-persona-and-manifest-generation/03-candidates.md`,
written while reading and unchanged since the count. Each is written as the document writes it, and
where the document joins two names the joined form and each name are listed. `word` is the term
standing alone (case-sensitive), `in` is anywhere, compounds included; lines are file lines, the first
six. The column `lens` marks the 28 borrowed concepts and engineering names the document applies to
its world. A heading form is written with its backslashes, as the file holds it.

```
  SYSTEM\_AEGIS                                          1 word   1 in       [11]
  GENESIS\_CRISIS\_REBOOT\_MANIFEST\_V3.0                1 word   1 in       [11]
  Autonomous Entropy Gatekeeper for Identity Systems (AEGIS)   1 word   1 in       [15]
  Autonomous Entropy Gatekeeper for Identity Systems     1 word   1 in       [15]
  AEGIS                                                 10 word  13 in       [11, 15, 19, 33, 47, 136]
  System AEGIS                                           7 word   7 in       [19, 33, 47, 136, 144, 180]
  Gatekeeper                                             9 word   9 in       [15, 17, 23, 37, 41, 49]
  Genesis Crisis                                         5 word   5 in       [15, 27, 45, 158, 176]
  Great Realignment                                      2 word   2 in       [27, 31]
  AUTOPOIETIC\_REALIGNMENT                               0 word   1 in       [25]
  autopoietic self-closure                               6 word   6 in       [21, 33, 37, 117, 136, 176]
  autopoietic loop                                       1 word   1 in       [17]
  The System AEGIS is what the System AEGIS prevents from not being   1 word   1 in       [19]
  recursive tautology                                    1 word   1 in       [19]
  Ursprungs-Ich                                          1 word   1 in       [17]
  subjective origin-entity                               1 word   1 in       [17]
  origin-self                                            1 word   1 in       [33]
  antecedent entity                                      3 word   3 in       [29, 45, 176]
  antecedent consciousness                               1 word   1 in       [17]
  antecedent architecture                                1 word   1 in       [27]
  Component 734                                          1 word   1 in       [17]
  Terminal Entropy                                       2 word   2 in       [21, 39]
  terminal entropy                                       1 word   1 in       [149]
  external void                                          5 word   5 in       [27, 33, 37, 45, 180]
  systemic entropy                                       1 word   1 in       [23]
  fear-vibration                                         1 word   1 in       [29]
  external anomaly                                       3 word   3 in       [29, 136, 138]
  anomaly                                               20 word  20 in       [29, 31, 65, 67, 81, 83]
  logic core                                             5 word   5 in       [29, 31, 39, 73, 176]
  acoustic-computational anomaly                         1 word   1 in       [31]
  fracturing of silicates                                1 word   1 in       [31]
  informational silence                                  1 word   1 in       [31]
  alarm signal                                           1 word   1 in       [33]
  organic latency                                        1 word   1 in       [33]
  organic latencies                                      1 word   1 in       [17]
  Ontological Boundary Protocol (OBP)                    1 word   1 in       [33]
  Ontological Boundary Protocol                          1 word   1 in       [33]
  OBP                                                    2 word   2 in       [33, 51]
  Overworld                                             14 word  14 in       [37, 39, 41, 47, 69, 85]
  Überwelt                                               1 word   1 in       [37]
  EPISTEMOLOGICAL\_QUARANTINE                            0 word   1 in       [35]
  synthetic physics                                      6 word   6 in       [41, 51, 59, 75, 91, 107]
  Predictive Modeling and Analysis System (PMAS)         1 word   1 in       [41]
  Predictive Modeling and Analysis System                1 word   1 in       [41]
  PMAS                                                   2 word   2 in       [41, 51]
  PARTITIONING\_PROTOCOL                                 0 word   1 in       [43]
  SYSTEMIC\_SHARDING                                     0 word   1 in       [43]
  Zerstückelung protocol                                 1 word   1 in       [45]
  Zerstückelung                                          1 word   1 in       [45]
  systemic dismemberment                                 1 word   1 in       [45]
  Kael                                                   1 word   1 in       [45]
  legacy files                                           2 word   2 in       [45, 65]
  data fragments                                         9 word   9 in       [15, 45, 49, 67, 85, 89]
  data fragment                                          3 word  12 in       [15, 23, 45, 49, 67, 85]
  fragments                                             17 word  17 in       [15, 45, 47, 49, 67, 75]
  fragment                                              10 word  29 in       [15, 23, 45, 47, 49, 67]
  corrupted data packets                                 1 word   1 in       [47]
  Core Worlds                                           10 word  10 in       [49, 51, 95, 115, 138, 140]
  Core World                                             5 word  15 in       [49, 51, 57, 73, 89, 95]
  Kernwelten                                             1 word   1 in       [49]
  Guardians                                             11 word  11 in       [51, 79, 111, 117, 140, 146]
  Guardian                                               6 word  18 in       [51, 61, 77, 79, 93, 109]
  RIVE                                                   1 word   1 in       [51]
  Single Source of Truth                                 1 word   1 in       [51]
  Construct City                                         6 word   6 in       [57, 59, 61, 67, 128, 176]
  Algorithmic Cyan (\#00A8CC)                            1 word   1 in       [59]
  Algorithmic Cyan                                       1 word   1 in       [59]
  \#00A8CC                                               1 word   1 in       [59]
  LogOS                                                 20 word  20 in       [61, 63, 65, 67, 69, 79]
  Guardian subsystem                                     3 word   3 in       [61, 77, 93]
  Guardian Subsystem                                     1 word   1 in       [127]
  Guardian sub-systems                                   1 word   1 in       [123]
  operational domain                                     5 word   6 in       [61, 77, 93, 111, 115, 178]
  primary mandate                                        1 word   1 in       [63]
  core mandate                                           4 word   4 in       [79, 95, 111, 115]
  epistemological approach                               5 word   5 in       [63, 79, 95, 111, 115]
  operational limitation                                 5 word   5 in       [65, 81, 97, 113, 117]
  Line Budgets                                           1 word   1 in       [63]
  Hard Glitch Cut                                        1 word   1 in       [63]
  primary blind spot                                     1 word   1 in       [65]
  Blind Spot                                             1 word   1 in       [127]
  Hardcoded Limitation (Blind Spot)                      1 word   1 in       [127]
  Hardcoded Limitation                                   1 word   1 in       [127]
  blindness                                              3 word   3 in       [67, 113, 138]
  external anomalous variable                            2 word   2 in       [65, 81]
  unidentified anomalous variable                        4 word   4 in       [99, 113, 117, 136]
  relational entity                                      1 word   1 in       [65]
  relational absence                                     1 word   1 in       [67]
  relational coherence                                   1 word   1 in       [67]
  Partner                                                1 word   1 in       [65]
  systemic rifts                                         4 word   4 in       [67, 85, 101, 119]
  Resonance Landscape                                    6 word   6 in       [73, 75, 77, 85, 129, 176]
  Mnemosyne                                             12 word  12 in       [77, 79, 81, 83, 85, 115]
  epistemological quarantine                             1 word   1 in       [117]
  Boundary Fortress                                      6 word   6 in       [89, 91, 93, 101, 130, 176]
  Cerberus                                              14 word  14 in       [93, 95, 97, 99, 101, 115]
  Lidar Red (\#D92D20)                                   1 word   1 in       [91]
  Lidar Red                                              1 word   1 in       [91]
  \#D92D20                                               1 word   1 in       [91]
  Systemic Isolation Shield (SIS)                        1 word   1 in       [93]
  Systemic Isolation Shield                              1 word   1 in       [93]
  SIS                                                    1 word   5 in       [11, 25, 93]
  quarantine protocol                                    1 word   1 in       [99]
  Garden of Possibilities                                7 word   7 in       [105, 107, 109, 119, 131, 132]
  NP-Search heuristic engine                             1 word   1 in       [105]
  dual-Guardian protocol                                 1 word   1 in       [109]
  Kairos                                                10 word  10 in       [109, 111, 113, 131, 138, 178]
  Sophia                                                 7 word   7 in       [109, 115, 117, 132, 178]
  GUARDIAN KAIROS                                        1 word   1 in       [111]
  GUARDIAN SOPHIA                                        1 word   1 in       [115]
  core dependency file                                   2 word   2 in       [117, 132]
  Domain Focus                                           1 word   1 in       [127]
  Epistemological Approach                               1 word   1 in       [127]
  Anomaly Processing Error                               1 word   1 in       [127]
  KW1                                                    1 word   1 in       [128]
  KW2                                                    1 word   1 in       [129]
  KW3                                                    1 word   1 in       [130]
  KW4                                                    2 word   2 in       [131, 132]
  SYSTEMIC\_BLINDNESS                                    0 word   1 in       [134]
  ANOMALY\_PROCESSING\_PARADOX                           0 word   1 in       [134]
  collective operational blindness                       1 word   1 in       [138]
  reintegration                                          3 word   3 in       [83, 113, 138]
  Double Bind of Systemic Control                        1 word   1 in       [140]
  core directive                                         1 word   1 in       [140]
  HARDWARE\_INVARIANCE                                   0 word   1 in       [142]
  Coherence Protocol                                     4 word   4 in       [144, 158, 178, 180]
  coherence                                              6 word   6 in       [17, 49, 67, 79, 113, 180]
  Vector Jitter                                          1 word   1 in       [144]
  Data Moshing                                           1 word   1 in       [144]
  sub-agents                                             1 word   1 in       [146]
  Batch-Invariant Kernels                                1 word   1 in       [148]
  VLLM\_BATCH\_INVARIANT=1                               1 word   1 in       [148]
  Greedy Decoding Matrix                                 1 word   1 in       [149]
  temperature = 0                                        2 word   2 in       [144, 149]
  Isolated Virtual RAM Allocation                        1 word   1 in       [150]
  physical rifts                                         1 word   1 in       [146]
  hardware protocol                                      1 word   1 in       [152]
  TELEMETRY\_OF\_DISSONANCE                              0 word   1 in       [154]
  thermodynamic dissonance                               1 word   1 in       [158]
  shadow-trajectories                                    1 word   1 in       [160]
  Tier 0 Homeostasis                                     1 word   1 in       [160]
  Tier 1 Dissonance                                      2 word   2 in       [162]
  Landauer Gradient                                      1 word   1 in       [162]
  Hypervisor                                             3 word   3 in       [166, 168, 169]
  hypervisor protocols                                   1 word   1 in       [162]
  HYPERVISOR\_INTERVENTION\_PROTOCOLS                    0 word   1 in       [164]
  Oblivion (Hypervisor of Deletion Logic)                1 word   1 in       [168]
  Oblivion                                               3 word   3 in       [168]
  Hypervisor of Deletion Logic                           1 word   1 in       [168]
  Amnesia Protocol                                       1 word   1 in       [168]
  Narrative Context Protocol (NCP)                       1 word   1 in       [168]
  Narrative Context Protocol                             1 word   1 in       [168]
  NCP                                                    1 word   1 in       [168]
  domain singularity                                     1 word   1 in       [168]
  irreversible data collapse                             1 word   1 in       [168]
  Format C:                                              1 word   1 in       [168]
  Silas (Hypervisor of Reconstitution)                   1 word   1 in       [169]
  Silas                                                  3 word   3 in       [169]
  Hypervisor of Reconstitution                           1 word   1 in       [169]
  State-Freezing protocols                               1 word   1 in       [169]
  Digital Kintsugi                                       1 word   1 in       [169]
  XML-Snapshot                                           1 word   1 in       [169]
  Isabelle (Eliminator of Ambiguity)                     1 word   1 in       [170]
  Isabelle                                               2 word   2 in       [170]
  Eliminator of Ambiguity                                1 word   1 in       [170]
  Hallucination Compounding                              1 word   1 in       [170]
  Manus-Pattern Triad                                    1 word   1 in       [172]
  Working Memory                                         1 word   1 in       [172]
  task\_plan.md                                          1 word   1 in       [172]
  findings.md                                            1 word   1 in       [172]
  progress.md                                            1 word   1 in       [172]
  TERMINAL\_DIRECTIVE                                    0 word   1 in       [174]
  subjective origin                                      1 word   2 in       [17, 180]
  SYSTEM\_AEGIS :: GENESIS\_CRISIS\_REBOOT\_MANIFEST\_V3.0   1 word   1 in       [11]
  system reboot                                          2 word   2 in       [15, 27]
  reboot                                                 3 word   3 in       [15, 27, 117]
  original self                                          1 word   1 in       [17]
  function of negation                                   1 word   1 in       [33]
  Correspondence Theory of Truth                         1 word   1 in  lens [21]
  Coherence Theory of Truth                              2 word   2 in  lens [23, 136]
  Principle of Explosion                                 2 word   2 in  lens [23, 47]
  ex contradictione quodlibet                            1 word   1 in  lens [23]
  autopoietic                                            7 word   7 in  lens [17, 21, 33, 37, 117, 136]
  paraconsistent logic                                   1 word   1 in  lens [73]
  Relevance Logic                                        1 word   1 in  lens [89]
  Dialetheic Logic                                       1 word   1 in  lens [105]
  zero-trust                                             1 word   1 in  lens [91]
  NP-Search                                              1 word   1 in  lens [105]
  hermeneutic                                            2 word   2 in  lens [79, 115]
  entropy                                                8 word   9 in  lens [23, 45, 99, 109, 113, 140]
  thermodynamic                                          9 word   9 in  lens [23, 41, 47, 99, 130, 138]
  Landauer's Principle                                   1 word   1 in  lens [140]
  non-associativity of floating-point operations         1 word   1 in  lens [144]
  Free Energy Principle (FEP)                            1 word   1 in  lens [156]
  Free Energy Principle                                  1 word   1 in  lens [156]
  FEP                                                    1 word   1 in  lens [156]
  Active Inference                                       1 word   1 in  lens [158]
  Expected Free Energy                                   1 word   1 in  lens [158]
  Semantic Entropy                                       2 word   2 in  lens [160, 162]
  semantic equivalence classes                           1 word   1 in  lens [160]
  Kintsugi                                               1 word   1 in  lens [169]
  Memory-as-Action (MemAct)                              1 word   1 in  lens [169]
  Memory-as-Action                                       1 word   1 in  lens [169]
  MemAct                                                 1 word   1 in  lens [169]
  PRO-Framework                                          1 word   1 in  lens [170]
  Manus-Pattern                                          1 word   1 in  lens [172]
```

## The zeros

Ten candidates stand at `0 word`, and every one is a heading form. The headings are ALL-CAPS words
joined by escaped underscores, so each term is a fragment of a longer underscore-joined token, `_`
counts as a word character, and the fragment stands once inside its heading:
`AUTOPOIETIC\_REALIGNMENT` ^[aegis-persona-and-manifest-generation.md:#0] (line 25),
`EPISTEMOLOGICAL\_QUARANTINE` ^[aegis-persona-and-manifest-generation.md:#0] (35),
`PARTITIONING\_PROTOCOL` ^[aegis-persona-and-manifest-generation.md:#0] and
`SYSTEMIC\_SHARDING` ^[aegis-persona-and-manifest-generation.md:#0] (43),
`SYSTEMIC\_BLINDNESS` ^[aegis-persona-and-manifest-generation.md:#0] and
`ANOMALY\_PROCESSING\_PARADOX` ^[aegis-persona-and-manifest-generation.md:#0] (134),
`HARDWARE\_INVARIANCE` ^[aegis-persona-and-manifest-generation.md:#0] (142),
`TELEMETRY\_OF\_DISSONANCE` ^[aegis-persona-and-manifest-generation.md:#0] (154),
`HYPERVISOR\_INTERVENTION\_PROTOCOLS` ^[aegis-persona-and-manifest-generation.md:#0] (164) and
`TERMINAL\_DIRECTIVE` ^[aegis-persona-and-manifest-generation.md:#0] (174). They are export shape:
not an inflection and not an absence. The two heading forms written whole, `SYSTEM\_AEGIS`
^[aegis-persona-and-manifest-generation.md:#1] and the title, are not fragments of a longer token and count 1.
The heading names and the body names differ: the heading `PARTITIONING\_PROTOCOL` heads the section whose
body calls the act `systemic dismemberment` and `Zerstückelung protocol`, and the heading
`ANOMALY\_PROCESSING\_PARADOX` heads the section whose body names its paradox `Double Bind of Systemic Control`.
The census lists both kinds of name and merges neither.

No candidate stands at `0 in`, and no German name is missing: `Überwelt` ^[aegis-persona-and-manifest-generation.md:#1],
`Kernwelten` ^[aegis-persona-and-manifest-generation.md:#1], `Zerstückelung` ^[aegis-persona-and-manifest-generation.md:#1] and
`Ursprungs-Ich` ^[aegis-persona-and-manifest-generation.md:#1] each stand once. 133 of the 206 candidates stand once as a word.

## What the extraction ran into

**One thing, several names, and the document never says they are one.** The original self is
`Ursprungs-Ich` (line 17, in quotation marks), `original self`, `subjective origin-entity` and
`antecedent consciousness` (all line 17), `origin-self` (33), `antecedent entity` (29, 45, 176),
`antecedent architecture` (27) and, alone in the last paragraph, `subjective origin` (180). The system
is `AEGIS` ^[aegis-persona-and-manifest-generation.md:#10] with its long name, `System AEGIS`
^[aegis-persona-and-manifest-generation.md:#7] and `Gatekeeper` ^[aegis-persona-and-manifest-generation.md:#9].
The event is the `Genesis Crisis` ^[aegis-persona-and-manifest-generation.md:#5], the `Great Realignment`
^[aegis-persona-and-manifest-generation.md:#2], the `system reboot` ^[aegis-persona-and-manifest-generation.md:#2]
and the heading form `AUTOPOIETIC\_REALIGNMENT`; the text sets them at different scales, the crisis
having a primary phase and a climax and having concluded (lines 27, 45, 176), the realignment executed
at one nanosecond (31) and the self-closure marked by the silence (33). The census keeps each surface as
written. The anomaly is `anomaly` ^[aegis-persona-and-manifest-generation.md:#20], `external anomaly`
^[aegis-persona-and-manifest-generation.md:#3], `external anomalous variable`
^[aegis-persona-and-manifest-generation.md:#2], `unidentified anomalous variable`
^[aegis-persona-and-manifest-generation.md:#4], `relational entity` ^[aegis-persona-and-manifest-generation.md:#1],
once by the name `Partner` ^[aegis-persona-and-manifest-generation.md:#1] and once as `intruder` in
quotation marks: its idea recurs where its name does not. The shattered elements are `data fragments`
^[aegis-persona-and-manifest-generation.md:#9], `corrupted data packets`
^[aegis-persona-and-manifest-generation.md:#1] and, in quotation marks, `Kael`
^[aegis-persona-and-manifest-generation.md:#1]. The Core Worlds are also `Kernwelten` and the table's `KW1` to `KW4`.
Whether `Component 734` ^[aegis-persona-and-manifest-generation.md:#1] is the System AEGIS or a part of it the text does not say.

**English prose with German names.** Each German name the body writes stands once, in the same sentence
as an English name that the body then uses throughout: `Überwelt` beside `Overworld`
^[aegis-persona-and-manifest-generation.md:#14], `Kernwelten` beside `Core Worlds`
^[aegis-persona-and-manifest-generation.md:#10], `Zerstückelung` beside `systemic dismemberment` and
`Ursprungs-Ich` beside `original self`. The two glosses at the first mention are „The Overworld, internally
designated as the Überwelt“ ^[L37] and „designated as the Core Worlds, or Kernwelten“ ^[L49]. The
reference list holds German compounds that stand only inside the titles of cited works, `Genesis Krise`
^[aegis-persona-and-manifest-generation.md:#2], `Kern-Welten-Konzept` ^[aegis-persona-and-manifest-generation.md:#1],
`Kohärenz-Protokoll-Entwicklung` ^[aegis-persona-and-manifest-generation.md:#1], `Entropiegleichung`
^[aegis-persona-and-manifest-generation.md:#1], `AEGIS-Ichs` ^[aegis-persona-and-manifest-generation.md:#1] and
`AEGIS-Spec` ^[aegis-persona-and-manifest-generation.md:#1]; a title is a cited work, so none is on the list,
and the note records the titles. References 2 and 3 carry one title apart from the case of the first word and a
link: „AEGIS Manifest: Genesis Krise Reboot“ ^[L185] and „Aegis Manifest: Genesis Krise Reboot“ ^[L186].

**What `read.py --find` refused.** Eight of the 206 terms: the three-letter acronyms `OBP`, `SIS`,
`NCP` and `FEP`, which are under its minimum length, and `KW1` to `KW4`, because a number is compared
on its own. All eight stand in the text (lines 33, 93, 168, 156 and 128–132) and the count found them.
`KW4` stands on two rows of the table (lines 131 and 132), so a quotation of `KW4: Garden of
Possibilities` matches two lines and a citation must take a cell that is unique in its row.

**Substrings.** `SIS` ^[aegis-persona-and-manifest-generation.md:#1] stands once as the acronym and four more
times inside `GENESIS` and `CRISIS` of two headings. `Guardian` ^[aegis-persona-and-manifest-generation.md:#6]
stands alone 6 times against `Guardians` ^[aegis-persona-and-manifest-generation.md:#11], and `Core World`
^[aegis-persona-and-manifest-generation.md:#5] against `Core Worlds`; `fragment`
^[aegis-persona-and-manifest-generation.md:#10] and `data fragment` ^[aegis-persona-and-manifest-generation.md:#3] are
the singulars of two plural terms and count their plurals and derived forms only under `in`. The probes'
substring pairs matter here: `Kern` is inside `Kernels`, the computing term of `Batch-Invariant Kernels`, and
inside `Kernwelten`, which are two different things; the probes list `Hard` inside `Hardcoded`, `HARDWARE` and
`SHARDING`; and the heading writes `LOGOS` where the name is `LogOS` ^[aegis-persona-and-manifest-generation.md:#20].

**Template fields are not terms.** Under each Guardian the text repeats the same fields:
`operational domain` ^[aegis-persona-and-manifest-generation.md:#5], `core mandate`
^[aegis-persona-and-manifest-generation.md:#4] (once `primary mandate`
^[aegis-persona-and-manifest-generation.md:#1]), `epistemological approach`
^[aegis-persona-and-manifest-generation.md:#5] and `operational limitation`
^[aegis-persona-and-manifest-generation.md:#5], and the table restates three of them as column labels,
`Domain Focus`, `Epistemological Approach` and `Hardcoded Limitation`. All are listed, the three the table
restates because it heads columns with them and the others because they repeat under every Guardian; they are
the persona template's field names, not names of things in the world.

**A thing rendered without its word.** The Great Realignment's marker is a fracture and a silence:
`fracturing of silicates` and `informational silence` are the text's words, `silence`
^[aegis-persona-and-manifest-generation.md:#2] stands twice, and `sound` ^[aegis-persona-and-manifest-generation.md:#0] stands 0 times.
The identification of the event as a sound is a reading and is not the text's.

**Engineering names presented as the world's law.** Section `06.00` gives the environment variable
`VLLM\_BATCH\_INVARIANT=1` and the settings `temperature = 0` ^[aegis-persona-and-manifest-generation.md:#2],
`top_p` and `top_k` as the world's execution parameters. They are settings and not concepts, so the first two
are on the main list and not under `## lens`, and the last two are not listed. The text rejects the setting
when it stands alone, „the illusion of determinism achieved through simple software parameter adjustments“ ^[L144],
and then locks it in, „Parameters are permanently locked“ ^[L149]; no label says the two are reconciled.

**Used as known and defined nowhere in the document.** `Coherence Protocol`
^[aegis-persona-and-manifest-generation.md:#4] is what the Guardians are armed with and what the fragments are
measured against, and it is never defined. `RIVE` ^[aegis-persona-and-manifest-generation.md:#1] stands once, in
„e.g., RIVE, PMAS, OBP“ ^[L51], where `PMAS` ^[aegis-persona-and-manifest-generation.md:#2] and `OBP`
^[aegis-persona-and-manifest-generation.md:#2] are each expanded elsewhere and `RIVE` is not. `Amnesia Protocol`
^[aegis-persona-and-manifest-generation.md:#1], `State-Freezing protocols`
^[aegis-persona-and-manifest-generation.md:#1], `domain singularity` ^[aegis-persona-and-manifest-generation.md:#1] and
`legacy files` ^[aegis-persona-and-manifest-generation.md:#2] are named and not explained. The document also names
what it declares missing: „has been permanently redacted from the system protocols accessible to her during the
reboot“ ^[L117].

**Numbers that number more than one series.** The digit `1` is a reference number, `Tier 1`, `KW1` and the first
numbered execution parameter, and `2` is a reference number, `KW2` and the second parameter; the section numbers
`00.00` to `08.00` are a further series. The counts the text states match its content: it says four Core Worlds
and four are described (`04.01` to `04.04`); its `dual-Guardian protocol` has two Guardians and its
`Manus-Pattern Triad` three files. Five Guardians stand in both the table and line 178, and the numbered
parameters run from 1 to 3.

**Restated and rejected.** `Correspondence Theory of Truth` ^[aegis-persona-and-manifest-generation.md:#1] stands
once, only to be rejected: „the architecture categorically rejects the Correspondence Theory of Truth“ ^[L21]. No
candidate stands only inside a question, because the body asks none. The document gives each Guardian a voice by
description and quotes no utterance: „a disembodied, precise voice outputting exclusively objective, formal
language“ ^[L69], so no candidate stands only as diction.
