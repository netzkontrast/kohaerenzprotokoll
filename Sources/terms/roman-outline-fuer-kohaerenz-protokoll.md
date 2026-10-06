---
source: Sources/drive/roman-outline-fuer-kohaerenz-protokoll.md
drive_id: "1y6dHc6rsHOoUhRlzDRefnFNBK4d4tReKBTwTguHHB7c"
title: "Roman-Outline für Kohärenz Protokoll"
category: plot-outline
index_date: "2025-05-03"
extracted: "2026-10-06"
candidates: 109    # the terms capture.py counted
---

# Term census — Roman-Outline für Kohärenz Protokoll

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py roman-outline-fuer-kohaerenz-protokoll`

```
  lines                902  (frontmatter ends at 9)
  body words           16371
  headings             16   bold-only lines 26
  table rows           0   code fences 0
  question marks       39
  backslash escapes    178
  typographic marks    42   ascii quotes 180
  invisible characters none
  math symbol lines    0
  glued ref numbers    23
  repeated labels      Core Theme x14, Kael System Dynamics x14, AEGIS Strategy/Manifestation x13, Conceptual Deep Dive x13, Genre/Trope Application x13, Key Beats / Abstract Scenes (ca. 3-5) x13, Key Concepts/Foreshadowing x13, Key Symbols/Motifs x13, Narrative Goals & Pacing x13, Narrative Technique Focus x13, Philosophical Resonance x13, Setting & Atmosphere x13, Subplot Progression x13
  longest line         1101 chars
```

## Stance, read per passage

**Observed:** the document is an outline, a plan for chapters not yet written. Its title line calls it „Kohärenz Protokoll - Detaillierte Roman-Outline“ ^[L11]. Each chapter is a heading `Chapter` (14 times: the Prolog and Chapters 1 to 13, `read.py --count "Chapter"`) followed by the same fields, which the profile lists as repeated labels; the last, `Key Beats / Abstract Scenes`, stands 13 times (`read.py --count "Key Beats / Abstract Scenes"`).

- L13 to L19, and each chapter's opening: five bulleted fields (`Core Theme`, `Kael System Dynamics`, `AEGIS Strategy/Manifestation`, `Setting & Atmosphere`, `Narrative Goals & Pacing`). They speak in the plan's voice, hedged: „Das Tempo beginnt langsam, möglicherweise abstrakt oder mythisch“ ^[L19], and the technique field says „Möglicher Einsatz einer mythischen oder hochsymbolischen Sprache zu Beginn“ ^[L63]. The fields give goals, not events that happened.
- L21 to L72, and each chapter's middle: under `Conceptual Deep Dive` the fields `Subplot Progression`, `Philosophical Resonance`, `Genre/Trope Application`, `Key Concepts/Foreshadowing`, `Narrative Technique Focus` and `Key Symbols/Motifs`. The foreshadowing field looks forward by its own label, for example „Foreshadowt die Notwendigkeit, diese Abwehrmechanismen später strategisch zu überwinden“ ^[L655].
- L73 to L79, and each chapter's end: numbered beats in the form `1.  **:**`, the title part of each beat empty in the export, each followed by a note in the document's own marker `<*Notiz: …>`. The label `Notiz` stands 64 times (`read.py --count "Notiz"`). The note is a second voice about the beat, for example „Etabliert die existenziellen Einsätze und AEGIS' grundlegende Motivation“ ^[L75].
- `Philosophical Resonance`, last bullet: a paragraph that applies the named philosophy to the chapter and tags it `[Philo Hint]` (21 times, `read.py --count "Philo Hint"`), for example „Die Konfrontation mit LogOS und den Paradoxien des Systems demonstriert jedoch die Grenzen dieses Ansatzes“ ^[L172]. The philosophers' statements in the field are the document's reports of them, not the novel's world.
- Sample text: a few beats put a thought in quotation marks, as the voice a part would have, for example „Vielleicht war es wirklich nur Einbildung?“ ^[L606] and „Wer oder was bin ich wirklich, jenseits dieser fragmentierten Reflexionen?“ ^[L876]. They stand inside a beat, not as dialogue.
- L887 to L901: a list headed „Referenzen“ ^[L887] of 13 web references with access dates, numbered; the numbers glued to sentences in the body (the profile counts 23 glued reference numbers) point to it.
- L885: the text ends mid-sentence, in Chapter 13: „Aus dieser Krise heraus trifft Kael“ ^[L885] and no further chapter follows. The document refers forward to chapters it does not contain, e.g. „Foreshadowt den Kontakt in Kap. 19 und 25.“ ^[L790].

## Candidates and counts

109 candidates, written while reading and frozen by the count (`Plan/runs/roman-outline-fuer-kohaerenz-protokoll/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `roman-outline-fuer-kohaerenz-protokoll.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `AEGIS` ^[roman-outline-fuer-kohaerenz-protokoll.md:#180] | 180 | 190 | 15, 17, 18, 19, 27, 37, 38, 39, 47, 48, 56, 69 … | `AEGIS-Überwelt` ×3, `AEGIS-Paradoxon` ×2, `AEGIS-Logik` ×1, `AEGIS-Taktik` ×1 |
| `Kael` ^[roman-outline-fuer-kohaerenz-protokoll.md:#114] | 114 | 166 | 16, 19, 28, 37, 47, 57, 70, 78, 83, 84, 85, 87 … | `Kaels` ×49, `Kael-System` ×1, `Kael-Systems` ×1, `Kael-Integration` ×1 |
| `System Kael` ^[roman-outline-fuer-kohaerenz-protokoll.md:#13] | 13 | 13 | 16, 57, 78, 279, 341, 342, 482, 498, 612, 681, 816, 885 |  |
| `Echo` ^[roman-outline-fuer-kohaerenz-protokoll.md:#10] | 10 | 12 | 15, 16, 17, 28, 38, 39, 59, 71, 77, 78, 79 | `Echos` ×2 |
| `Selene` ^[roman-outline-fuer-kohaerenz-protokoll.md:#6] | 6 | 7 | 16, 28, 59, 682, 722, 885 | `Selene-Aspekt` ×1 |
| `Nichts Rauschen` ^[roman-outline-fuer-kohaerenz-protokoll.md:#7] | 7 | 7 | 17, 18, 37, 39, 48, 68, 75 |  |
| `Fehlausgerichtete Kohärenz` ^[roman-outline-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 56, 190, 557 |  |
| `MisalignedCoherence` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 17 |  |
| `Kohärenz Protokoll` ^[roman-outline-fuer-kohaerenz-protokoll.md:#3] | 3 | 6 | 11, 17, 29, 77, 216, 480 |  |
| `AEGIS Paradoxon` ^[roman-outline-fuer-kohaerenz-protokoll.md:#8] | 8 | 8 | 27, 56, 96, 161, 354, 557, 759, 828 |  |
| `Kael Fragmentation` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 28 |  |
| `Kael Integration` ^[roman-outline-fuer-kohaerenz-protokoll.md:#12] | 12 | 12 | 95, 160, 226, 290, 353, 423, 490, 558, 623, 693, 761, 827 |  |
| `Juna/V` ^[roman-outline-fuer-kohaerenz-protokoll.md:#9] | 9 | 10 | 19, 29, 58, 76, 748, 749, 760, 788, 790 | `Juna/Vs` ×1 |
| `Kernparadoxon` ^[roman-outline-fuer-kohaerenz-protokoll.md:#3] | 3 | 4 | 17, 38, 77, 789 | `Kernparadoxons` ×1 |
| `Kerntrauma` ^[roman-outline-fuer-kohaerenz-protokoll.md:#3] | 3 | 4 | 16, 70, 78, 454 | `Kerntrauma-Ereignis` ×1 |
| `Überwelt` ^[roman-outline-fuer-kohaerenz-protokoll.md:#0] | 0 | 3 | 18, 79, 750 |  |
| `Host` ^[roman-outline-fuer-kohaerenz-protokoll.md:#4] | 4 | 8 | 83, 84, 130, 141, 160, 342, 404, 412 | `Hosts` ×4 |
| `Glitch` ^[roman-outline-fuer-kohaerenz-protokoll.md:#6] | 6 | 23 | 84, 95, 96, 104, 105, 106, 115, 126, 130, 135, 136, 141 … | `Glitches` ×17 |
| `Lex` ^[roman-outline-fuer-kohaerenz-protokoll.md:#63] | 63 | 63 | 84, 125, 142, 148, 149, 150, 151, 152, 160, 161, 170, 171 … |  |
| `Alex` ^[roman-outline-fuer-kohaerenz-protokoll.md:#56] | 56 | 56 | 214, 215, 216, 217, 218, 226, 234, 235, 236, 244, 245, 253 … |  |
| `Rhys` ^[roman-outline-fuer-kohaerenz-protokoll.md:#48] | 48 | 48 | 278, 279, 280, 282, 290, 298, 299, 307, 315, 322, 327, 329 … |  |
| `Kiko` ^[roman-outline-fuer-kohaerenz-protokoll.md:#10] | 10 | 13 | 342, 383, 399, 404, 412, 414, 452, 470, 479, 537, 612, 623 … | `Kikos` ×3 |
| `Lia` ^[roman-outline-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 412, 452, 479 |  |
| `Moros` ^[roman-outline-fuer-kohaerenz-protokoll.md:#9] | 9 | 9 | 342, 383, 399, 407, 412, 414, 452, 479, 537 |  |
| `Kernwelt 1` ^[roman-outline-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 85, 86 |  |
| `KW1` ^[roman-outline-fuer-kohaerenz-protokoll.md:#48] | 48 | 48 | 85, 87, 96, 105, 106, 124, 137, 143, 144, 148, 149, 150 … |  |
| `Logos-Prime` ^[roman-outline-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 86, 151, 548 |  |
| `Kernwelt 2` ^[roman-outline-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 344, 382 |  |
| `KW2` ^[roman-outline-fuer-kohaerenz-protokoll.md:#35] | 35 | 35 | 316, 337, 342, 343, 345, 354, 363, 365, 373, 384, 390, 395 … |  |
| `Mnemosyne-Archipel` ^[roman-outline-fuer-kohaerenz-protokoll.md:#2] | 2 | 3 | 344, 382, 414 | `Mnemosyne-Archipels` ×1 |
| `Guardian LogOS` ^[roman-outline-fuer-kohaerenz-protokoll.md:#5] | 5 | 5 | 150, 152, 162, 189, 547 |  |
| `Guardian Mnemosyne` ^[roman-outline-fuer-kohaerenz-protokoll.md:#6] | 6 | 6 | 343, 345, 355, 384, 406, 413 |  |
| `Guardians` ^[roman-outline-fuer-kohaerenz-protokoll.md:#4] | 4 | 4 | 162, 355, 424, 624 |  |
| `ANPs` ^[roman-outline-fuer-kohaerenz-protokoll.md:#27] | 27 | 27 | 149, 160, 215, 278, 279, 280, 299, 322, 337, 342, 353, 404 … |  |
| `EPs` ^[roman-outline-fuer-kohaerenz-protokoll.md:#48] | 48 | 48 | 78, 144, 191, 215, 278, 279, 280, 281, 282, 290, 299, 317 … |  |
| `Apparently Normal Parts` ^[roman-outline-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 160, 479 |  |
| `Emotional Parts` ^[roman-outline-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 191, 383, 479 |  |
| `Emotionale Teile` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 342 |  |
| `Inneren Konferenzzimmers` ^[roman-outline-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 281, 727 |  |
| `TSDP` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 478 |  |
| `Theory of Structural Dissociation of the Personality` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 478 |  |
| `Panoptismus` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 85 |  |
| `Philo Hint` ^[roman-outline-fuer-kohaerenz-protokoll.md:#21] | 21 | 21 | 39, 172, 236, 299, 365, 434, 500, 567, 634, 702, 771, 840 |  |
| `Core Theme` ^[roman-outline-fuer-kohaerenz-protokoll.md:#14] | 14 | 14 | 15, 83, 148, 214, 278, 341, 411, 478, 545, 611, 681, 747 … |  |
| `Kael System Dynamics` ^[roman-outline-fuer-kohaerenz-protokoll.md:#14] | 14 | 14 | 16, 84, 149, 215, 279, 342, 412, 479, 546, 612, 682, 748 … |  |
| `AEGIS Strategy/Manifestation` ^[roman-outline-fuer-kohaerenz-protokoll.md:#13] | 13 | 13 | 17, 85, 150, 216, 280, 343, 413, 480, 547, 613, 683, 749 … |  |
| `Setting & Atmosphere` ^[roman-outline-fuer-kohaerenz-protokoll.md:#13] | 13 | 13 | 18, 86, 151, 217, 281, 344, 414, 481, 548, 614, 684, 750 … |  |
| `Narrative Goals & Pacing` ^[roman-outline-fuer-kohaerenz-protokoll.md:#13] | 13 | 13 | 19, 87, 152, 218, 282, 345, 415, 482, 549, 615, 685, 751 … |  |
| `Conceptual Deep Dive` ^[roman-outline-fuer-kohaerenz-protokoll.md:#13] | 13 | 13 | 21, 89, 154, 220, 284, 347, 417, 484, 551, 617, 687, 753 … |  |
| `Subplot Progression` ^[roman-outline-fuer-kohaerenz-protokoll.md:#13] | 13 | 13 | 23, 91, 156, 222, 286, 349, 419, 486, 553, 619, 689, 755 … |  |
| `Philosophical Resonance` ^[roman-outline-fuer-kohaerenz-protokoll.md:#13] | 13 | 13 | 33, 100, 166, 230, 294, 359, 428, 494, 562, 628, 697, 765 … |  |
| `Genre/Trope Application` ^[roman-outline-fuer-kohaerenz-protokoll.md:#13] | 13 | 13 | 43, 110, 176, 240, 303, 369, 438, 504, 571, 638, 706, 775 … |  |
| `Key Concepts/Foreshadowing` ^[roman-outline-fuer-kohaerenz-protokoll.md:#13] | 13 | 13 | 52, 119, 185, 249, 311, 378, 448, 513, 580, 648, 715, 784 … |  |
| `Narrative Technique Focus` ^[roman-outline-fuer-kohaerenz-protokoll.md:#13] | 13 | 13 | 63, 130, 195, 259, 322, 390, 458, 524, 591, 660, 727, 796 … |  |
| `Key Symbols/Motifs` ^[roman-outline-fuer-kohaerenz-protokoll.md:#13] | 13 | 13 | 64, 131, 196, 260, 323, 391, 459, 525, 592, 661, 728, 797 … |  |
| `Nyx` ^[roman-outline-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 612, 623, 656 |  |
| `Argus` ^[roman-outline-fuer-kohaerenz-protokoll.md:#11] | 11 | 11 | 748, 791, 807, 808, 810, 816, 859, 876, 878 |  |
| `Meta-Beobachter` ^[roman-outline-fuer-kohaerenz-protokoll.md:#4] | 4 | 4 | 748, 791, 816, 859 |  |
| `Kernwelt 3` ^[roman-outline-fuer-kohaerenz-protokoll.md:#4] | 4 | 4 | 611, 612, 614, 652 |  |
| `KW3` ^[roman-outline-fuer-kohaerenz-protokoll.md:#22] | 22 | 22 | 611, 612, 613, 615, 632, 633, 634, 642, 673, 674, 675, 676 … |  |
| `Cerberus-Labyrinth` ^[roman-outline-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 614, 652 |  |
| `Guardian Cerberus` ^[roman-outline-fuer-kohaerenz-protokoll.md:#5] | 5 | 5 | 613, 615, 624, 653, 675 |  |
| `Cerberus` ^[roman-outline-fuer-kohaerenz-protokoll.md:#16] | 16 | 18 | 611, 613, 614, 615, 624, 632, 633, 634, 643, 652, 653, 669 … | `Cerberus-Labyrinth` ×2 |
| `Gaslighting` ^[roman-outline-fuer-kohaerenz-protokoll.md:#10] | 10 | 16 | 545, 546, 547, 548, 549, 558, 567, 575, 584, 604, 605, 606 … | `Gaslightings` ×5, `Gaslighting-Techniken` ×1 |
| `Riss` ^[roman-outline-fuer-kohaerenz-protokoll.md:#32] | 32 | 47 | 115, 748, 749, 750, 751, 759, 760, 761, 769, 770, 771, 779 … | `Risses` ×14, `Risse` ×1 |
| `Der Riss` ^[roman-outline-fuer-kohaerenz-protokoll.md:#10] | 10 | 10 | 749, 759, 760, 769, 770, 779, 788, 790, 792, 801 |  |
| `Ko-Bewusstsein` ^[roman-outline-fuer-kohaerenz-protokoll.md:#4] | 4 | 5 | 682, 683, 693, 719, 741 | `Ko-Bewusstseins` ×1 |
| `Inneres Konferenzzimmer` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 684 |  |
| `Fundament` ^[roman-outline-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 829 | `fundamentalen` ×6, `fundamental` ×4, `fundamentaler` ×2, `fundamentalster` ×1 |
| `Akt 2` ^[roman-outline-fuer-kohaerenz-protokoll.md:#5] | 5 | 5 | 520, 816, 819, 860, 884 |  |
| `Fragmente der Vergangenheit` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 409 |  |
| `Die Logik des Gaslichts` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 543 |  |
| `Die Mauern der Grenzfeste` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 609 |  |
| `Relation R` ^[roman-outline-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 106, 837, 840 |  |
| `Switches` ^[roman-outline-fuer-kohaerenz-protokoll.md:#6] | 6 | 6 | 479, 482, 509, 518, 524, 538 |  |
| `Dissoziation` ^[roman-outline-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 412, 471, 517 |  |
| `Phobien` ^[roman-outline-fuer-kohaerenz-protokoll.md:#27] | 27 | 30 | 57, 84, 126, 279, 281, 282, 290, 299, 316, 322, 337, 478 … |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Hume` ^[roman-outline-fuer-kohaerenz-protokoll.md:#4] | 4 | 4 | 104, 106 |  |
| `Parfits` ^[roman-outline-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 106, 837, 840 |  |
| `Kant` ^[roman-outline-fuer-kohaerenz-protokoll.md:#3] | 3 | 4 | 170, 172, 298 | `Kantianismus` ×1 |
| `Hobbes` ^[roman-outline-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 234 | `hobbessche` ×2 |
| `Logischer Positivismus` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 171 |  |
| `Ethik der Fürsorge` ^[roman-outline-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 298, 299 |  |
| `Qualia` ^[roman-outline-fuer-kohaerenz-protokoll.md:#4] | 4 | 4 | 364, 365, 390 |  |
| `Emergenz` ^[roman-outline-fuer-kohaerenz-protokoll.md:#8] | 8 | 8 | 37, 38, 39, 59 |  |
| `Ontologie` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 37 |  |
| `Loftus` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 433 |  |
| `Body Keeps the Score` ^[roman-outline-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 432, 443 |  |
| `Glitch in the Matrix` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 115 |  |
| `Unreliable Narrator` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 114 |  |
| `Cosmic Horror` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 48 |  |
| `Origin Story` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 47 |  |
| `Rules Lawyer` ^[roman-outline-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 181 |  |
| `Psychological Horror` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 444 |  |
| `Sartre` ^[roman-outline-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 499, 839 |  |
| `Bad Faith` ^[roman-outline-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 499 |  |
| `Mauvaise Foi` ^[roman-outline-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 499, 500 |  |
| `Locke` ^[roman-outline-fuer-kohaerenz-protokoll.md:#2] | 2 | 3 | 837, 840 | `Lockes` ×1 |
| `Buber` ^[roman-outline-fuer-kohaerenz-protokoll.md:#2] | 2 | 3 | 701, 702 | `Bubers` ×1 |
| `Ich-Du` ^[roman-outline-fuer-kohaerenz-protokoll.md:#3] | 3 | 4 | 701, 702 | `Ich-Du-Begegnungen` ×1 |
| `Kuhn` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 2 | 770 | `Kuhns` ×1 |
| `Epistemologischer Bruch` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 769 |  |
| `Simulationstheorie` ^[roman-outline-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 838, 840 |  |
| `Existentialismus` ^[roman-outline-fuer-kohaerenz-protokoll.md:#2] | 2 | 2 | 839, 840 |  |
| `Threshold Guardian` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 643 |  |
| `Deadly Maze` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 642 |  |
| `Hope Spot` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 779 |  |
| `Erkenntnistheorie` ^[roman-outline-fuer-kohaerenz-protokoll.md:#3] | 3 | 3 | 566, 567 |  |
| `Philosophie der Angst` ^[roman-outline-fuer-kohaerenz-protokoll.md:#1] | 1 | 1 | 632 |  |

## What the extraction ran into

**Zeros:** 1 — `Überwelt`.

Explained: it is an inflection-like case of a compound: the word stands only inside `AEGIS-Überwelt`, 3 times (L18, L79, L750; `read.py --count "AEGIS-Überwelt"`), never alone, so the term the list wrote counts 0 standing alone and 3 in compounds. It is not absent from the document.

**Standing alone less often than with compounds:** 22 — `AEGIS` 180/190, `Kael` 114/166, `Echo` 10/12, `Selene` 6/7, `Kohärenz Protokoll` 3/6, `Juna/V` 9/10, `Kernparadoxon` 3/4, `Kerntrauma` 3/4, `Host` 4/8, `Glitch` 6/23, `Kiko` 10/13, `Mnemosyne-Archipel` 2/3, `Cerberus` 16/18, `Gaslighting` 10/16, `Riss` 32/47, `Ko-Bewusstsein` 4/5, `Phobien` 27/30, `Kant` 3/4, `Locke` 2/3, `Buber` 2/3, `Ich-Du` 3/4, `Kuhn` 1/2.

Explained: most are inflections or hyphen compounds, which the table's last column names: the genitive `Kaels` (49) and `Kael-System`, `Kael-Systems`, `Kael-Integration` for `Kael`; `AEGIS-Überwelt`, `AEGIS-Paradoxon`, `AEGIS-Logik`, `AEGIS-Taktik` for `AEGIS`; the plural `Glitches` (17) for `Glitch`; `Hosts` for `Host`; `Risses` (14) and `Risse` for `Riss`; `Gaslightings` and `Gaslighting-Techniken`; `Kikos`; `Echos`; `Cerberus-Labyrinth`. `Kohärenz Protokoll` stands 3 times alone and 6 in all because the document also writes the genitive `Kohärenz Protokolls` 3 times (`read.py --count "Kohärenz Protokolls"`). `Phobien` 27/30: the three further occurrences are `ANP/EP-Phobien`. For `Kant`, `Locke`, `Buber`, `Ich-Du`, `Kuhn` and `Juna/V` the table names the genitive or compound.

**`- ` lines read as prose and not counted:** 1 — Key Beats / Abstract Scenes (ca. 3-5).

Explained: the period after „ca“ and the space make the line look like a sentence to the counter, so the list entry was dropped. The label itself stands 13 times (`read.py --count "Key Beats / Abstract Scenes"`); that is a count by hand, recorded in `05-verify.txt`.

**Export artifacts met.** The beat numbers read `1.  **:**` with an empty bold title in all 13 beat lists. Chapter headings are written `### \-----**Chapter 1:**`, with escaped brackets in the three titled ones („Fragmente der Vergangenheit“ ^[L409], „Die Logik des Gaslichts“ ^[L543], „Die Mauern der Grenzfeste“ ^[L609]); `Chapter Prologue: [Genesis]` stands at L13. The marker `<!-- end list -->` stands between the bullet groups. Reference numbers are glued to sentence ends (profile: 23). The text is cut off at L885.

**Terms assumed and not defined.** `Nyx` stands 3 times (L612, L623, L656) and is only called „ein noch unentdeckter Anteil wie Nyx“ ^[L612]; `Argus` is called „der Meta-Beobachter“ ^[L748]; `Selene` is named an „aufkeimenden Selene-Aspekt“ ^[L885] at L885 and only hinted at: „wird hier erstmals angedeutet, wenn auch nur als ferne Möglichkeit.“ ^[L682]. `TSDP` is written out once: „Teil der TSDP - Theory of Structural Dissociation of the Personality“ ^[L478]. `Fundament` stands twice alone (both in L829); the 13 further words the surfaces column lists begin `fundamental` and are another word. `Kernwelt 1` is also written `KW1`, `Kernwelt 2` also `KW2`, `Kernwelt 3` also `KW3`; the document never writes the subscripted form.

**Standing.** The document speaks in plan terms. It does not call itself canon: `read.py --count "Canon"` and `read.py --count "Kanon"` both give 0. Its `index_date` is 2025-05-03 and every reference in the list carries an access date in May 2025 (written `Zugriff am Mai`).
