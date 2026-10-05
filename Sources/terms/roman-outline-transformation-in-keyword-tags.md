---
source: Sources/drive/roman-outline-transformation-in-keyword-tags.md
drive_id: "10KCBpSEnyWIF3zQ7FfndeOUhsxqKoEICnRqoP8tgI08"
title: "Roman-Outline-Transformation in Keyword-Tags"
category: plot-outline
index_date: "2025-05-03"
extracted: "2026-10-05"
candidates: 181    # the terms capture.py counted
---

# Term census — Roman-Outline-Transformation in Keyword-Tags

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py roman-outline-transformation-in-keyword-tags`

```
  lines                1009  (frontmatter ends at 9)
  body words           12583
  headings             8   bold-only lines 0
  table rows           0   code fences 0
  question marks       15
  backslash escapes    1708
  typographic marks    1   ascii quotes 24
  invisible characters none
  math symbol lines    0
  glued ref numbers    18
  repeated labels      AEGIS State Tags x6, Core Theme Tags x6, Kael State Tags x6, Plot Keywords x6, Reader Experience Strategy x6, Setting Tags x6, Zusammenfassung (Mensch) x6, Key Beats (Keywords) x5, Konzept-Cluster x5, Konzept-Handling x5, Narrative Goals Summary Tags x5
  longest line         437 chars
```

## Stance, read per passage

The document has two parts, and neither speaks as a report or a plan about the world; both are an index. The first, headed `Glossar` at L13, runs from L15 to L738 as one list of `tag: definition` entries; its definitions describe the tag and, where a world-name is meant, say where it applies („KW1“, „Prolog“, „Akt 3“). The second part, from L740, holds one block per chapter, each headed `### Kapitel …`: „Kapitel P: Genesis“ ^[L740] and then chapters 1 to 4 (L793, L849, L901, L950) and a fifth at L1000.

The glossary describes the outline's own purpose in its tags. One entry gives the main aim as „maximale Information auf kompaktem Raum für maschinelle Analyse bereitzustellen“ ^[L291]; another says the optimisation aims at machine processing, „Ein Hinweis darauf, dass die primäre Optimierung des Outlines auf maschinelle Verarbeitung abzielt“ ^[L450]. A third asks for the outline to be „extrem kompakt und hochstrukturiert zu sein“ ^[L621]. These are the document's statement of what it is for, recorded and not applied.

Each chapter block repeats one set of field labels (the profile counts them: six times for `Plot Keywords`, `Kael State Tags`, `AEGIS State Tags`, `Setting Tags`, `Core Theme Tags`, `Reader Experience Strategy` and `Zusammenfassung (Mensch)`). The one prose field is `Zusammenfassung (Mensch)`, which the glossary defines as „Prosatext, der die Kernhandlung des Kapitels zusammenfasst“ ^[L733]. The other fields are lists of snake_case tags, some in `key=value` form, e.g. the line that begins with the chapter-P state tags at L744. The labels are the template; the tags after them are the content. `Konzept-Handling` marks each concept with `NEU`, `REF` or `PROG`: „Markierung im Konzept-Handling für ein Konzept, das in diesem Kapitel zum ersten Mal eingeführt oder thematisiert wird“ ^[L486] for `NEU`, and for `REF` „Markierung im Konzept-Handling für ein bekanntes Konzept, das im Kapitel referenziert wird, aber keine signifikante neue Entwicklung erfährt“ ^[L559]. `INNOVATION` is defined at L292 and does not appear in a chapter block read here.

The document hedges inline with a question mark after a tag. The profile counts 15 question marks; they stand in the glossary at L143, L180, L208 and L590 and in the chapter blocks at L742, L906, L919, L955, L993, L1002 and L1004, always after a guess about a name or a state (`Juna/V?`, `nyx?`, `kiko\_aktiv?`). L590 is not a hedge but the quoted question „Wer bin ich?“ ^[L590]. The question marks therefore mark uncertainty about a name or state in the outline, not open questions to a reader.

The text names no speaker and no date apart from the manifest; no passage marks itself as a lock, a canon or a decision. The title line calls the document an outline ^[L11].

## Candidates and counts

181 candidates, written while reading and frozen by the count (`Plan/runs/roman-outline-transformation-in-keyword-tags/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `roman-outline-transformation-in-keyword-tags.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `AEGIS` ^[roman-outline-transformation-in-keyword-tags.md:#144] | 144 | 181 | 15, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29 … | `AEGIS-Überwelt` ×9, `AEGIS-System` ×7, `AEGIS-Systems` ×6, `AEGIS-Paradoxon` ×4 |
| `Kael` ^[roman-outline-transformation-in-keyword-tags.md:#61] | 61 | 169 | 15, 16, 19, 35, 36, 38, 40, 41, 42, 43, 44, 45 … | `Kaels` ×42, `Kael-System` ×32, `Kael-Systems` ×21, `Kael-Integration` ×12 |
| `Echo` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 7 | 145, 249, 363, 543, 596, 742, 849 | `Echos` ×5 |
| `Kohärenz Protokoll` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 5 | 11, 154, 331, 543, 742 |  |
| `Kael-System` ^[roman-outline-transformation-in-keyword-tags.md:#32] | 32 | 53 | 16, 40, 68, 70, 77, 80, 83, 85, 86, 87, 88, 89 … | `Kael-Systems` ×21 |
| `Juna/V` ^[roman-outline-transformation-in-keyword-tags.md:#36] | 36 | 36 | 39, 42, 129, 134, 154, 190, 204, 207, 208, 280, 300, 320 … |  |
| `Fundament` ^[roman-outline-transformation-in-keyword-tags.md:#11] | 11 | 18 | 104, 129, 204, 233, 234, 235, 236, 237, 238, 344, 386, 477 … | `fundamentalen` ×6, `Fundament-Kontakt` ×4, `Fundaments` ×3, `fundamentaleren` ×1 |
| `Konstrukt-Welt` ^[roman-outline-transformation-in-keyword-tags.md:#15] | 15 | 17 | 58, 191, 264, 405, 406, 410, 411, 414, 415, 417, 418, 506 … | `Konstrukt-Welten` ×2 |
| `Konstrukt-Welten` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 2 | 58, 264 |  |
| `Konstrukt-Stadt` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 849 |  |
| `Logos-Prime` ^[roman-outline-transformation-in-keyword-tags.md:#4] | 4 | 4 | 191, 261, 405, 795 |  |
| `Mnemosyne-Archipel` ^[roman-outline-transformation-in-keyword-tags.md:#3] | 3 | 3 | 262, 410, 1002 |  |
| `Cerberus-Labyrinth` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 2 | 259, 415 |  |
| `Kairos-Potentialis` ^[roman-outline-transformation-in-keyword-tags.md:#3] | 3 | 3 | 260, 263, 417 |  |
| `Resonanz-Landschaft` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 1000 |  |
| `KW1` ^[roman-outline-transformation-in-keyword-tags.md:#22] | 22 | 22 | 101, 110, 148, 158, 161, 251, 261, 407, 408, 409, 436, 439 … |  |
| `KW2` ^[roman-outline-transformation-in-keyword-tags.md:#11] | 11 | 11 | 102, 186, 187, 262, 318, 412, 413, 449, 462, 472, 664 |  |
| `KW3` ^[roman-outline-transformation-in-keyword-tags.md:#9] | 9 | 9 | 78, 105, 119, 133, 209, 259, 288, 416, 470 |  |
| `KW4` ^[roman-outline-transformation-in-keyword-tags.md:#12] | 12 | 13 | 100, 103, 139, 147, 260, 263, 349, 392, 400, 468, 539, 653 … |  |
| `Guardian LogOS` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 2 | 381, 851 |  |
| `Guardian Cerberus` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 2 | 119, 378 |  |
| `Guardian Mnemosyne` ^[roman-outline-transformation-in-keyword-tags.md:#3] | 3 | 3 | 382, 462, 1002 |  |
| `Guardians` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 2 | 265, 266 |  |
| `LogOS` ^[roman-outline-transformation-in-keyword-tags.md:#14] | 14 | 14 | 135, 253, 381, 406, 435, 436, 437, 442, 455, 689, 851, 882 … | `Logos-Prime` ×4 |
| `Mnemosyne` ^[roman-outline-transformation-in-keyword-tags.md:#9] | 9 | 15 | 47, 109, 184, 210, 211, 262, 382, 410, 411, 462, 463, 464 … | `Mnemosynes` ×3, `Mnemosyne-Archipel` ×3 |
| `Cerberus` ^[roman-outline-transformation-in-keyword-tags.md:#7] | 7 | 9 | 119, 120, 259, 378, 414, 415, 416, 654, 704 | `Cerberus-Labyrinth` ×2 |
| `Kairos` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 4 | 260, 263, 417, 418 | `Kairos-Potentialis` ×3 |
| `Sophia` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 418 |  |
| `Überwelt` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 11 | 59, 60, 61, 62, 63, 64, 132, 146, 395, 453, 685 |  |
| `Host` ^[roman-outline-transformation-in-keyword-tags.md:#4] | 4 | 8 | 151, 193, 281, 364, 640, 670, 795, 1002 | `Host-Anteils` ×2, `Host-Anteil` ×2 |
| `Lex` ^[roman-outline-transformation-in-keyword-tags.md:#16] | 16 | 18 | 341, 374, 394, 427, 428, 429, 430, 431, 432, 440, 545, 577 … |  |
| `Alex` ^[roman-outline-transformation-in-keyword-tags.md:#15] | 15 | 18 | 16, 68, 69, 70, 277, 341, 374, 432, 460, 461, 583, 585 … | `Alex-Anteils` ×2, `Alex-Anteil` ×1 |
| `Rhys` ^[roman-outline-transformation-in-keyword-tags.md:#15] | 15 | 18 | 97, 159, 175, 194, 273, 341, 374, 571, 572, 573, 616, 642 … | `Rhys-Anteils` ×1, `Rhys-Anteil` ×1 |
| `Argus` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 4 | 98, 99, 452, 456 | `Argus-Anteils` ×2 |
| `Nyx` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 2 | 16, 492 |  |
| `Kiko` ^[roman-outline-transformation-in-keyword-tags.md:#3] | 3 | 4 | 78, 367, 675, 1002 | `Kiko-Anteil` ×1 |
| `Lia` ^[roman-outline-transformation-in-keyword-tags.md:#0] | 0 | 1 | 676 |  |
| `Moros` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 2 | 677, 1002 | `Moros-Anteil` ×1 |
| `Selene` ^[roman-outline-transformation-in-keyword-tags.md:#7] | 7 | 9 | 97, 143, 197, 356, 592, 593, 594, 595, 596 | `Selenes` ×2 |
| `Beschützer-Anteil` ^[roman-outline-transformation-in-keyword-tags.md:#3] | 3 | 4 | 68, 85, 583, 903 | `Beschützer-Anteils` ×1 |
| `Fürsorger-Anteil` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 2 | 616, 952 | `Fürsorger-Anteils` ×1 |
| `Anteile` ^[roman-outline-transformation-in-keyword-tags.md:#18] | 18 | 44 | 44, 77, 80, 95, 96, 97, 116, 140, 248, 273, 295, 305 … | `Anteilen` ×25, `Anteile-Kommunikation` ×1 |
| `ANP` ^[roman-outline-transformation-in-keyword-tags.md:#7] | 7 | 20 | 83, 84, 164, 174, 175, 176, 296, 339, 340, 341, 362, 532 … |  |
| `ANPs` ^[roman-outline-transformation-in-keyword-tags.md:#12] | 12 | 12 | 83, 84, 164, 175, 176, 339, 340, 341, 362, 673, 678, 932 |  |
| `EP` ^[roman-outline-transformation-in-keyword-tags.md:#7] | 7 | 24 | 78, 83, 84, 88, 90, 91, 164, 174, 175, 176, 210, 296 … |  |
| `EPs` ^[roman-outline-transformation-in-keyword-tags.md:#14] | 14 | 14 | 78, 83, 84, 164, 174, 175, 176, 210, 340, 342, 362, 673 … |  |
| `Apparently Normal Parts` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 2 | 83, 374 |  |
| `Emotional Parts` ^[roman-outline-transformation-in-keyword-tags.md:#5] | 5 | 5 | 83, 174, 175, 385, 674 |  |
| `TSDP` ^[roman-outline-transformation-in-keyword-tags.md:#5] | 5 | 14 | 75, 83, 84, 532, 634, 669, 670, 671, 672, 674, 675, 676 … | `TSDP-Theorie` ×7, `TSDP-Modell` ×2 |
| `Risse` ^[roman-outline-transformation-in-keyword-tags.md:#3] | 3 | 3 | 206, 505, 575 |  |
| `Riss` ^[roman-outline-transformation-in-keyword-tags.md:#3] | 3 | 6 | 81, 206, 505, 511, 574, 575 | `Risse` ×3, `risse` ×1 |
| `Kernparadoxon` ^[roman-outline-transformation-in-keyword-tags.md:#10] | 10 | 10 | 28, 29, 33, 34, 36, 215, 522, 587, 604, 742 |  |
| `Glitches` ^[roman-outline-transformation-in-keyword-tags.md:#3] | 3 | 3 | 39, 252, 795 |  |
| `Prolog` ^[roman-outline-transformation-in-keyword-tags.md:#16] | 16 | 17 | 104, 122, 130, 150, 152, 153, 154, 165, 223, 228, 335, 404 … | `Prologs` ×1 |
| `Genesis` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 740 |  |
| `Der Glitch im Spiegel` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 793 |  |
| `Echos in der Konstrukt-Stadt` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 849 |  |
| `Der Schatten des Beschützers` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 901 |  |
| `Stimmen der Fürsorge` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 950 |  |
| `Der Ruf der Resonanz-Landschaft` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 1000 |  |
| `Glossar` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 13 |  |
| `Plot Keywords` ^[roman-outline-transformation-in-keyword-tags.md:#6] | 6 | 6 | 743, 796, 852, 904, 953, 1003 |  |
| `Kael State Tags` ^[roman-outline-transformation-in-keyword-tags.md:#6] | 6 | 6 | 744, 797, 853, 905, 954, 1004 |  |
| `AEGIS State Tags` ^[roman-outline-transformation-in-keyword-tags.md:#6] | 6 | 6 | 745, 798, 854, 906, 955, 1005 |  |
| `Setting Tags` ^[roman-outline-transformation-in-keyword-tags.md:#6] | 6 | 6 | 746, 799, 855, 907, 956, 1006 |  |
| `Core Theme Tags` ^[roman-outline-transformation-in-keyword-tags.md:#6] | 6 | 6 | 747, 800, 856, 908, 957, 1007 |  |
| `Reader Experience Strategy` ^[roman-outline-transformation-in-keyword-tags.md:#6] | 6 | 6 | 748, 801, 857, 909, 958, 1008 |  |
| `Konzept-Cluster` ^[roman-outline-transformation-in-keyword-tags.md:#9] | 9 | 9 | 528, 546, 624, 667, 749, 802, 858, 910, 959 |  |
| `Konzept-Handling` ^[roman-outline-transformation-in-keyword-tags.md:#9] | 9 | 9 | 292, 486, 540, 559, 762, 815, 871, 923, 972 |  |
| `Key Beats (Keywords)` ^[roman-outline-transformation-in-keyword-tags.md:#5] | 5 | 5 | 780, 836, 888, 937, 987 |  |
| `Key Beat` ^[roman-outline-transformation-in-keyword-tags.md:#4] | 4 | 9 | 122, 404, 543, 569, 780, 836, 888, 937, 987 |  |
| `Narrative Goals Summary Tags` ^[roman-outline-transformation-in-keyword-tags.md:#5] | 5 | 5 | 791, 847, 899, 948, 998 |  |
| `Zusammenfassung (Mensch)` ^[roman-outline-transformation-in-keyword-tags.md:#6] | 6 | 6 | 742, 795, 851, 903, 952, 1002 |  |
| `Plot Reflection` ^[roman-outline-transformation-in-keyword-tags.md:#0] | 0 | 2 | 565, 600 |  |
| `Research\_Keywords` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 537 |  |
| `NEU` ^[roman-outline-transformation-in-keyword-tags.md:#46] | 46 | 46 | 388, 766, 767, 768, 769, 770, 771, 772, 773, 774, 775, 776 … |  |
| `REF` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 2 | 388, 828 |  |
| `PROG` ^[roman-outline-transformation-in-keyword-tags.md:#5] | 5 | 5 | 388, 881, 882, 932, 982 | `Progression` ×1 |
| `INNOVATION` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 388 |  |
| `Beat` ^[roman-outline-transformation-in-keyword-tags.md:#24] | 24 | 29 | 122, 404, 543, 569, 780, 784, 785, 786, 787, 836, 840, 841 … | `Beats` ×5 |
| `Subplots` ^[roman-outline-transformation-in-keyword-tags.md:#7] | 7 | 8 | 351, 387, 623, 757, 810, 866, 918, 967 |  |
| `Foreshadowing` ^[roman-outline-transformation-in-keyword-tags.md:#8] | 8 | 9 | 77, 356, 387, 595, 758, 811, 867, 919, 968 | `Foreshadowing-Elemente` ×1 |
| `Philosophie` ^[roman-outline-transformation-in-keyword-tags.md:#8] | 8 | 8 | 387, 457, 494, 753, 806, 862, 914, 963 |  |
| `Psychologie` ^[roman-outline-transformation-in-keyword-tags.md:#6] | 6 | 6 | 387, 754, 807, 863, 915, 964 |  |
| `Trope` ^[roman-outline-transformation-in-keyword-tags.md:#70] | 70 | 72 | 73, 114, 118, 124, 128, 131, 132, 133, 134, 135, 142, 190 … |  |
| `Symbol` ^[roman-outline-transformation-in-keyword-tags.md:#12] | 12 | 12 | 143, 387, 423, 447, 613, 756, 809, 831, 832, 865, 917, 966 | `symbolischer` ×1 |
| `Keyword-/Tag-basiertes Outline` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 11 |  |
| `aegis\_paradoxon` ^[roman-outline-transformation-in-keyword-tags.md:#21] | 21 | 22 | 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 743 … |  |
| `aegis\_ueberwelt` ^[roman-outline-transformation-in-keyword-tags.md:#8] | 8 | 9 | 58, 59, 60, 61, 62, 63, 64, 501, 746 |  |
| `aegis\_kern` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 2 | 20, 21 | `aegis\_kernlogik` ×1 |
| `aegis\_kernlogik` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 21 |  |
| `aegis\_origin` ^[roman-outline-transformation-in-keyword-tags.md:#3] | 3 | 5 | 25, 150, 743, 784, 791 |  |
| `aegis\_motivation` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 2 | 24, 785 |  |
| `aegis\_ueberlebensparadoxon` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 2 | 57, 747 |  |
| `aegis\_status\_emergent` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 52 |  |
| `aegis\_status\_final` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 53 |  |
| `aegis\_state\_tags` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 50 |  |
| `fragmentierung\_als\_kontrolle` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 2 | 226, 769 |  |
| `fehlausgerichtete\_kohaerenz` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 215 |  |
| `kohaerenz\_protokoll\_activation` ^[roman-outline-transformation-in-keyword-tags.md:#4] | 4 | 4 | 370, 743, 745, 787 |  |
| `echo\_fragmentation` ^[roman-outline-transformation-in-keyword-tags.md:#3] | 3 | 3 | 145, 743, 787 |  |
| `kael\_system\_birth` ^[roman-outline-transformation-in-keyword-tags.md:#3] | 3 | 3 | 363, 743, 787 |  |
| `kael\_system\_host` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 2 | 364, 819 |  |
| `kael\_integration` ^[roman-outline-transformation-in-keyword-tags.md:#29] | 29 | 29 | 336, 337, 338, 339, 340, 341, 342, 343, 344, 345, 346, 347 … |  |
| `funktionale\_multiplizitaet` ^[roman-outline-transformation-in-keyword-tags.md:#3] | 3 | 5 | 239, 240, 241, 289, 345 |  |
| `selene\_potenzial` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 2 | 596, 744 |  |
| `anteil\_alex` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 85 |  |
| `anteil\_argus` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 86 |  |
| `anteil\_host` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 87 |  |
| `anteil\_kiko` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 88 |  |
| `anteil\_lex` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 89 |  |
| `anteil\_lia` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 90 |  |
| `anteil\_moros` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 91 |  |
| `anteil\_nyx` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 92 |  |
| `anteil\_rhys` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 93 |  |
| `anteil\_selene` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 94 |  |
| `guardian\_cerberus` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 259 |  |
| `guardian\_kairos` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 260 |  |
| `guardian\_logOS` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 2 | 261, 876 |  |
| `guardian\_mnemosyne` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 262 |  |
| `guardian\_sophia` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 263 |  |
| `juna\_v` ^[roman-outline-transformation-in-keyword-tags.md:#19] | 19 | 23 | 154, 319, 320, 321, 322, 323, 324, 325, 326, 327, 328, 329 … |  |
| `juna\_v\_trigger` ^[roman-outline-transformation-in-keyword-tags.md:#3] | 3 | 5 | 154, 331, 743, 786, 791 |  |
| `fundament\_kontakt` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 2 | 236, 601 |  |
| `kw1\_logos\_prime` ^[roman-outline-transformation-in-keyword-tags.md:#7] | 7 | 8 | 406, 506, 798, 799, 820, 855, 907, 956 |  |
| `kw2\_mnemosyne\_archipel` ^[roman-outline-transformation-in-keyword-tags.md:#3] | 3 | 4 | 411, 507, 1005, 1006 |  |
| `kw3\_cerberus\_labyrinth` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 2 | 414, 508 |  |
| `kw4\_kairos\_potentialis` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 2 | 418, 509 |  |
| `kw\_konstrukt\_welt` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 419 |  |
| `nichts\_rauschen` ^[roman-outline-transformation-in-keyword-tags.md:#3] | 3 | 4 | 488, 510, 746, 784 |  |
| `ort\_nichts\_rauschen` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 510 |  |
| `externe\_resonanz` ^[roman-outline-transformation-in-keyword-tags.md:#4] | 4 | 4 | 208, 743, 745, 786 |  |
| `chaos\_to\_order` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 2 | 123, 743 |  |
| `chaos\_geburt` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 122 |  |
| `krise\_kontrolle` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 404 |  |
| `resonanz\_trigger` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 569 |  |
| `protokoll\_fragmentierung` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 543 |  |
| `gaslighting` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 3 | 43, 243, 408 |  |
| `panoptismus` ^[roman-outline-transformation-in-keyword-tags.md:#7] | 7 | 7 | 517, 518, 519, 796, 798, 830, 843 |  |
| `unreliable\_narrator` ^[roman-outline-transformation-in-keyword-tags.md:#5] | 5 | 8 | 193, 640, 690, 801, 808, 823, 841, 847 |  |
| `glitch\_in\_matrix` ^[roman-outline-transformation-in-keyword-tags.md:#3] | 3 | 3 | 250, 808, 822 |  |
| `unsichtbarer\_kaefig` ^[roman-outline-transformation-in-keyword-tags.md:#3] | 3 | 3 | 692, 800, 829 |  |
| `anteile\_koordination` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 97 |  |
| `ko\_bewusstsein` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 398 |  |
| `switches` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 634 |  |
| `shift` ^[roman-outline-transformation-in-keyword-tags.md:#5] | 5 | 5 | 600, 601, 602, 603, 604 |  |
| `plot\_keywords` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 536 |  |
| `konzept\_handling` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 388 |  |
| `konzept\_cluster` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 387 |  |
| `key\_beats` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 366 |  |
| `zusammenfassung\_mensch` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 733 |  |
| `tag\_basiert` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 635 |  |
| `informationsverdichtung\_ki` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 291 |  |
| `menschliche\_lesbarkeit\_sekundaer` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 450 |  |
| `struktur\_praegnanz` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 621 |  |
| `Dysregulation` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 2 | 952, 991 |  |
| `Ko-Bewusstheit` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 295 |  |
| `Gaslighting` ^[roman-outline-transformation-in-keyword-tags.md:#4] | 4 | 4 | 168, 408, 431, 708 |  |
| `Cosmic Horror` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 2 | 129, 130 |  |
| `Hard SF` ^[roman-outline-transformation-in-keyword-tags.md:#0] | 0 | 3 | 270, 271, 272 |  |
| `Archetyp` ^[roman-outline-transformation-in-keyword-tags.md:#3] | 3 | 4 | 642, 648, 654, 667 | `Archetypen` ×1 |
| `Heldenreise` ^[roman-outline-transformation-in-keyword-tags.md:#4] | 4 | 4 | 131, 275, 641, 654 |  |
| `Kybernetik zweiter Ordnung` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 224 |  |
| `Panoptismus` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 519 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Thomas Kuhns` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 82 |  |
| `David Humes` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 2 | 282, 283 |  |
| `Foucault` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 517 |  |
| `Niklas Luhmanns` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 443 |  |
| `Heinz von Foersters` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 224 |  |
| `Gödels` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 253 |  |
| `Bertrand Russells` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 579 |  |
| `Immanuel Kants` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 254 |  |
| `Jean-Paul Sartres` ^[roman-outline-transformation-in-keyword-tags.md:#2] | 2 | 2 | 201, 580 |  |
| `Derek Parfits` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 524 |  |
| `John Lockes` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 434 |  |
| `Karl Poppers` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 520 |  |
| `Martin Bubers` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 116 |  |
| `Thomas Hobbes'` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 277 |  |
| `Emmanuel Levinas'` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 426 |  |
| `Aristoteles'` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 100 |  |
| `mauvaise foi` ^[roman-outline-transformation-in-keyword-tags.md:#1] | 1 | 1 | 580 |  |

## What the extraction ran into

**What the zeros are.** `Lia`: the word stands once, inside the tag `tsdp\_ep\_lia` and its definition „Anwendung der TSDP-Theorie auf den Lia-Anteil (Emotional Part)“ ^[L676]; the form is a hyphen compound `Lia-Anteil`, so it counts zero standing alone and one with compounds (inflection by compounding, not damage). `Plot Reflection`: written only as the compound `Plot Reflection-Abschnitt`, e.g. „Tags im optionalen Plot Reflection-Abschnitt“ ^[L565], so zero alone, two with compounds. `Hard SF`: written only as `Hard SF-Prinzipien` and similar, e.g. „Spezifische Anwendung von Hard SF-Prinzipien auf das Thema Hacking“ ^[L270], zero alone and three with compounds. None of the three is absent.

**Export damage.** The profile shows 1708 backslash escapes: every underscore in every tag is written `\_`, so a tag is listed with its escape (`aegis\_paradoxon`), and the same tag written plain would count zero. The profile also counts 18 glued reference numbers and 24 ascii quotes; the glossary writes inner quotes straight, as in „Wer bin ich?“ ^[L590]. The markdown list is also broken by `<!-- end list -->` lines between the label of a field and its sub-list (e.g. L749 to L760), and a line at L1008 ends in a stray backslash-backtick and stops mid-word. The document ends at L1008 in chapter 5 while the glossary speaks of an epilogue in chapter 39 (entry `epilog`, L177), so the export is cut or the outline unfinished; the file does not say which.

**Compounds and tags.** The 49 terms standing alone less often than with compounds are mostly names that the document hyphen-joins (`Kael-System`, `AEGIS-Überwelt`, `Host-Anteil`, `Alex-Anteil`) or that sit inside a longer tag (`aegis\_paradoxon` in `aegis\_paradoxon\_latent`). `Kael` stands alone 61 times and 169 times with compounds; the surfaces column of the table gives the split. Names such as `LogOS` are written with that capitalisation in tags (`guardian\_logOS`) and as `Guardian LogOS` in prose; `Logos-Prime` is a separate place name.

**Label and tag at once.** `Plot Keywords`, `Konzept-Handling`, `Konzept-Cluster`, `Key Beats (Keywords)` and `Narrative Goals Summary Tags` are the template's field labels; each also has a snake_case glossary entry (`plot\_keywords`, `konzept\_handling`, `konzept\_cluster`, `key\_beats`) that defines it as a category of tags. They are listed in both surfaces.

**The glossary is not fully listed.** The glossary defines several hundred tags; this list holds the world's names, the document's own labels and marks, and a selection of tags that name a figure, a place, a state of AEGIS or Kael, or a strategy. Most mood, emotion and trope tags are not on the list; the counts say nothing about them.

**Lens.** The glossary names thinkers in genitive or hyphen forms (`Thomas Kuhns`, `David Humes`, `Foucault`); the list keeps the form the line has, and each is a lens, set under the heading as the document's own borrowing. Where the glossary gives a theory without a name in the list, the tag is not repeated.
**Zeros:** 3 — `Lia`, `Plot Reflection`, `Hard SF`.

**Standing alone less often than with compounds:** 49 — `AEGIS` 144/181, `Kael` 61/169, `Echo` 2/7, `Kohärenz Protokoll` 2/5, `Kael-System` 32/53, `Fundament` 11/18, `Konstrukt-Welt` 15/17, `KW4` 12/13, `Mnemosyne` 9/15, `Cerberus` 7/9, `Kairos` 1/4, `Überwelt` 2/11, `Host` 4/8, `Lex` 16/18, `Alex` 15/18, `Rhys` 15/18, `Argus` 2/4, `Kiko` 3/4, `Moros` 1/2, `Selene` 7/9, `Beschützer-Anteil` 3/4, `Fürsorger-Anteil` 1/2, `Anteile` 18/44, `ANP` 7/20, `EP` 7/24, `TSDP` 5/14, `Riss` 3/6, `Prolog` 16/17, `Key Beat` 4/9, `Beat` 24/29, `Subplots` 7/8, `Foreshadowing` 8/9, `Trope` 70/72, `aegis\_paradoxon` 21/22, `aegis\_ueberwelt` 8/9, `aegis\_kern` 1/2, `aegis\_origin` 3/5, `funktionale\_multiplizitaet` 3/5, `juna\_v` 19/23, `juna\_v\_trigger` 3/5 ….
