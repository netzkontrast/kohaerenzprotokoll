---
source: Sources/drive/outline-2.md
drive_id: "1I5alNL9AbvjY1L9eDko9CKtY_wHPfv2mpN-EWSYaRGM"
title: "Outline"
category: plot-outline
index_date: "2025-05-03"
extracted: "2026-10-05"
candidates: 93    # the terms capture.py counted
---

# Term census — Outline

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py outline-2`

```
  lines                586  (frontmatter ends at 9)
  body words           5021
  headings             0   bold-only lines 5
  table rows           0   code fences 0
  question marks       127
  backslash escapes    80
  typographic marks    46   ascii quotes 16
  invisible characters none
  math symbol lines    0
  glued ref numbers    44
  repeated labels      Core Theme x40, Genre/Trope x40, Kael Internal x40, Philosophy x40, Setting x40, Subplots x40, AEGIS Focus x37
  longest line         686 chars
```

## Stance, read per passage

The document is one long outline, and it names itself: „Zusammenstellung der Outline-Informationen (Neues Format)“ ^[L15]. It sorts the story into acts, each headed in bold: the prologue as „Act Prologue:“ ^[L17], then acts whose headings give a focus, „Innere Reise (Heroine's Journey Fokus)“ ^[L33], „Meta-Ebene & Zyklen (Meta-Exploration)“ ^[L217] and „Äußere Konfrontation & Rückkehr (Hero's Journey Fokus)“ ^[L401]. Under each act every chapter has the same shape: a label (`Chapter` ^[outline-2.md:#40]), a bracketed title, one paragraph of prose, and seven field lines.

**Prologue, L17 to L31.** The paragraph is a synopsis in the present tense, with one question mark about the external anomaly: „Die Erzählung fokussiert auf die Entität AEGIS oder ihr Vorläufer-Ich (Komponente 734).“ ^[L23] The synopsis ends in „der Geburtsstunde von System Kael“ ^[L23].

**Chapters 1 to 39, L35 to L583.** Each chapter paragraph is a plan, not a report, and it hedges by grammar. It uses modal verbs and parenthetical questions about its own content, for example „Kael (Lex/Argus?) erkennt dies als Bedrohung (Kollaps?) und Chance (Flucht? Schwachstelle?).“ ^[L179] and „Natur bleibt mysteriös (Andere Simulation? Höhere Realität? Andere KI? Fundament-Manifestation?).“ ^[L293]. The question marks are the document's own open points about who acts and what a thing is, not questions put to a reader. 86 lines of the file carry a `?` (counted by grep, in 05-verify.txt). Candidates that stand only inside such a guess have no reading of their own: `Lia` ^[outline-2.md:#2] and `Moros` ^[outline-2.md:#4] appear only in the guessing lists, for instance „Ein oder mehrere EPs (Kiko, Lia, Moros?) werden stärker präsent“ ^[L109].

**The seven field lines.** Under every paragraph the same labels repeat: `Core Theme` ^[outline-2.md:#40], `Kael Internal` ^[outline-2.md:#40], `AEGIS Focus` ^[outline-2.md:#37], `Setting` ^[outline-2.md:#40], `Subplots` ^[outline-2.md:#40], `Philosophy` ^[outline-2.md:#40] and `Genre/Trope` ^[outline-2.md:#40]. They are the template, not terms of the story. Chapters 35 and 37 add labels: chapters 35 and 37 each add `Juna/V Focus` ^[outline-2.md:#2], chapter 37 also has `Fundament Focus` ^[outline-2.md:#1] and no `AEGIS Focus`, which is also why `AEGIS Focus` stands 37 times against 40 for the others (chapters 37, 38 and 39 carry none).

**The lens fields.** The `Philosophy` line names thinkers in brackets or alone, for example „Epistemologischer Bruch; Anomalien (Kuhn); Chaostheorie.“ ^[L186] and „Sartre (Bad Faith/Selbsttäuschung)“ ^[L130]. They are applied to a chapter as a theme; they are listed under the lens heading. The `Genre/Trope` line writes tropes in English (`Plot Point` ^[outline-2.md:#2] stands twice, both in this line) and is diction about how a chapter is told, not a description of the world.

**Lock or canon.** The document carries no label for a lock, a sync or a status. It claims no standing for itself beyond calling its own format „Neues Format“ ^[L15].

## Candidates and counts

93 candidates, written while reading and frozen by the count (`Plan/runs/outline-2/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `outline-2.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `AEGIS` ^[outline-2.md:#124] | 124 | 132 | 23, 25, 27, 28, 29, 43, 45, 53, 57, 59, 71, 73 … | `AEGIS-Überwelt` ×3, `AEGIS-Interface` ×1, `AEGIS-Paradoxon` ×1, `AEGIS-Kernbereiche` ×1 |
| `Komponente 734` ^[outline-2.md:#3] | 3 | 3 | 23, 491 |  |
| `Nichts Rauschen` ^[outline-2.md:#2] | 2 | 2 | 23, 28 |  |
| `Echo` ^[outline-2.md:#5] | 5 | 8 | 23, 26, 51, 111, 235, 491, 532 | `Echos` ×3 |
| `Juna/V` ^[outline-2.md:#31] | 31 | 32 | 23, 29, 179, 183, 185, 213, 229, 291, 293, 297, 299, 301 … | `Juna/V-Infos` ×1 |
| `Kohärenz Protokoll` ^[outline-2.md:#1] | 1 | 1 | 23 |  |
| `System Kael` ^[outline-2.md:#1] | 1 | 1 | 23 |  |
| `Kael` ^[outline-2.md:#131] | 131 | 138 | 23, 26, 29, 39, 42, 45, 53, 56, 59, 67, 70, 73 … | `Kaels` ×7 |
| `Host` ^[outline-2.md:#3] | 3 | 4 | 39, 42, 95, 98 | `Host-Dominanz` ×1 |
| `KW1` ^[outline-2.md:#13] | 13 | 13 | 39, 43, 44, 53, 58, 67, 72, 86, 95, 137, 142, 426 |  |
| `KW2` ^[outline-2.md:#14] | 14 | 14 | 95, 97, 98, 99, 100, 109, 114, 123, 128, 249, 251, 256 … |  |
| `KW3` ^[outline-2.md:#9] | 9 | 9 | 151, 153, 155, 156, 347, 349, 354, 463, 468 |  |
| `KW4` ^[outline-2.md:#9] | 9 | 9 | 212, 263, 265, 269, 270, 279, 396, 554 |  |
| `Logos-Prime` ^[outline-2.md:#3] | 3 | 3 | 44, 58, 72 |  |
| `Mnemosyne-Archipel` ^[outline-2.md:#4] | 4 | 4 | 95, 100, 114, 256 |  |
| `Cerberus-Labyrinth` ^[outline-2.md:#3] | 3 | 3 | 151, 156, 354 |  |
| `Kairos-Potentialis` ^[outline-2.md:#2] | 2 | 2 | 265, 270 |  |
| `Überwelt` ^[outline-2.md:#21] | 21 | 25 | 28, 184, 212, 221, 223, 227, 228, 237, 242, 279, 284, 293 … | `Überwelt-Interface` ×1 |
| `Meta-Ebene` ^[outline-2.md:#4] | 4 | 4 | 207, 217, 221, 223 |  |
| `Fundament` ^[outline-2.md:#14] | 14 | 18 | 29, 199, 293, 377, 503, 505, 509, 510, 511, 519, 523, 534 … | `Fundament-Manifestation` ×1, `fundamentaler` ×1, `Fundament-Erkenntnisse` ×1, `Fundament-Kontakt` ×1 |
| `Externe Ebene` ^[outline-2.md:#2] | 2 | 2 | 382, 567 |  |
| `Externen Ebene` ^[outline-2.md:#2] | 2 | 2 | 295, 298 |  |
| `Lex` ^[outline-2.md:#24] | 24 | 24 | 39, 42, 53, 55, 56, 67, 70, 81, 123, 137, 140, 179 … |  |
| `Alex` ^[outline-2.md:#17] | 17 | 17 | 67, 69, 70, 72, 75, 81, 123, 140, 151, 154, 321, 349 … |  |
| `Rhys` ^[outline-2.md:#13] | 13 | 13 | 81, 83, 84, 98, 165, 168, 254, 321, 324, 449, 452 |  |
| `Nyx` ^[outline-2.md:#4] | 4 | 4 | 151, 154, 349, 463 |  |
| `Kiko` ^[outline-2.md:#10] | 10 | 10 | 95, 98, 109, 112, 151, 154, 321, 349, 352, 463 |  |
| `Lia` ^[outline-2.md:#2] | 2 | 2 | 109, 112 |  |
| `Moros` ^[outline-2.md:#4] | 4 | 4 | 95, 98, 109, 112 |  |
| `Selene` ^[outline-2.md:#10] | 10 | 11 | 26, 168, 321, 324, 391, 394, 410, 438, 494, 548, 551 | `Selene-Potenzial` ×1 |
| `Argus` ^[outline-2.md:#12] | 12 | 12 | 179, 182, 196, 223, 226, 240, 279, 282, 307, 310, 424, 494 |  |
| `Meta-Beobachter` ^[outline-2.md:#2] | 2 | 2 | 196, 282 |  |
| `LogOS` ^[outline-2.md:#14] | 14 | 14 | 53, 55, 57, 58, 59, 95, 137, 419, 421, 425, 427, 435 | `Logos-Prime` ×3 |
| `Guardian LogOS` ^[outline-2.md:#1] | 1 | 1 | 53 |  |
| `Mnemosyne` ^[outline-2.md:#18] | 18 | 23 | 95, 99, 100, 101, 109, 111, 113, 114, 115, 123, 251, 253 … | `Mnemosyne-Archipel` ×4, `Mnemosynes` ×1 |
| `Cerberus` ^[outline-2.md:#12] | 12 | 15 | 151, 153, 155, 156, 157, 349, 353, 354, 355, 461, 463, 467 … | `Cerberus-Labyrinth` ×3 |
| `Guardian Cerberus` ^[outline-2.md:#1] | 1 | 1 | 151 |  |
| `Kairos` ^[outline-2.md:#3] | 3 | 5 | 265, 269, 270, 271 | `Kairos-Potentialis` ×2 |
| `Sophia` ^[outline-2.md:#3] | 3 | 3 | 265, 269, 271 |  |
| `Guardians` ^[outline-2.md:#13] | 13 | 13 | 59, 101, 115, 157, 257, 265, 271, 355, 411, 413, 427, 455 … |  |
| `ANPs` ^[outline-2.md:#8] | 8 | 8 | 59, 70, 81, 84, 109, 112, 123, 165 |  |
| `EPs` ^[outline-2.md:#12] | 12 | 12 | 81, 84, 87, 98, 109, 111, 123, 165, 254, 449, 452 |  |
| `Fehlausgerichtete Kohärenz` ^[outline-2.md:#4] | 4 | 4 | 27, 307, 309, 363 |  |
| `Kernparadoxon` ^[outline-2.md:#5] | 5 | 5 | 27, 223, 307, 311, 367 |  |
| `AEGIS Paradoxon` ^[outline-2.md:#32] | 32 | 32 | 29, 45, 59, 73, 87, 101, 115, 129, 143, 157, 171, 185 … |  |
| `Kael Integration` ^[outline-2.md:#34] | 34 | 34 | 29, 45, 59, 73, 87, 101, 115, 129, 143, 157, 171, 185 … |  |
| `funktionale Multiplizität` ^[outline-2.md:#2] | 2 | 2 | 397, 579 |  |
| `funktionaler Multiplizität` ^[outline-2.md:#3] | 3 | 3 | 563, 565, 576 |  |
| `Multiplizität` ^[outline-2.md:#7] | 7 | 7 | 210, 397, 563, 565, 576, 578, 579 |  |
| `Ko-Bewusstsein` ^[outline-2.md:#2] | 2 | 2 | 165, 168 |  |
| `Phobien` ^[outline-2.md:#7] | 7 | 8 | 42, 81, 84, 121, 123, 126, 165, 463 |  |
| `Switches` ^[outline-2.md:#2] | 2 | 2 | 123, 126 |  |
| `TSDP` ^[outline-2.md:#0] | 0 | 1 | 125 | `TSDP-Dynamiken` ×1 |
| `Inneres Konferenzzimmer` ^[outline-2.md:#1] | 1 | 1 | 170 |  |
| `Glitches` ^[outline-2.md:#2] | 2 | 2 | 39, 179 |  |
| `Riss` ^[outline-2.md:#4] | 4 | 10 | 177, 179, 183, 184, 193, 223, 293, 298, 382 | `Risse` ×3, `Riss-Manifestation` ×1, `Risses` ×1, `Rissen` ×1 |
| `Task Force` ^[outline-2.md:#1] | 1 | 1 | 210 |  |
| `Gaslighting` ^[outline-2.md:#4] | 4 | 4 | 137, 141, 145, 407 |  |
| `Panoptismus` ^[outline-2.md:#1] | 1 | 1 | 43 |  |
| `Kerntrauma` ^[outline-2.md:#2] | 2 | 2 | 449, 452 |  |
| `Genesis` ^[outline-2.md:#2] | 2 | 2 | 21, 449 |  |
| `Vorläufer-Ich` ^[outline-2.md:#1] | 1 | 1 | 23 |  |
| `Ursprungs-Ich` ^[outline-2.md:#1] | 1 | 1 | 23 |  |
| `Zweite-Ordnung-Kybernetik` ^[outline-2.md:#3] | 3 | 3 | 279, 281, 286 |  |
| `Heroine's Journey` ^[outline-2.md:#1] | 1 | 1 | 33 |  |
| `Hero's Journey` ^[outline-2.md:#1] | 1 | 1 | 401 |  |
| `Plot Point` ^[outline-2.md:#2] | 2 | 2 | 215, 399 |  |
| `Core Theme` ^[outline-2.md:#40] | 40 | 40 | 25, 41, 55, 69, 83, 97, 111, 125, 139, 153, 167, 181 … |  |
| `Kael Internal` ^[outline-2.md:#40] | 40 | 40 | 26, 42, 56, 70, 84, 98, 112, 126, 140, 154, 168, 182 … |  |
| `AEGIS Focus` ^[outline-2.md:#37] | 37 | 37 | 27, 43, 57, 71, 85, 99, 113, 127, 141, 155, 169, 183 … |  |
| `Setting` ^[outline-2.md:#40] | 40 | 40 | 28, 44, 58, 72, 86, 100, 114, 128, 142, 156, 170, 184 … |  |
| `Subplots` ^[outline-2.md:#40] | 40 | 40 | 29, 45, 59, 73, 87, 101, 115, 129, 143, 157, 171, 185 … |  |
| `Philosophy` ^[outline-2.md:#40] | 40 | 40 | 30, 46, 60, 74, 88, 102, 116, 130, 144, 158, 172, 186 … |  |
| `Genre/Trope` ^[outline-2.md:#40] | 40 | 40 | 31, 47, 61, 75, 89, 103, 117, 131, 145, 159, 173, 187 … |  |
| `Juna/V Focus` ^[outline-2.md:#2] | 2 | 2 | 524, 552 |  |
| `Fundament Focus` ^[outline-2.md:#1] | 1 | 1 | 553 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Hume` ^[outline-2.md:#2] | 2 | 2 | 46, 244 |  |
| `Kant` ^[outline-2.md:#3] | 3 | 3 | 60, 230, 342 |  |
| `Hobbes` ^[outline-2.md:#1] | 1 | 1 | 74 |  |
| `Sartre` ^[outline-2.md:#3] | 3 | 3 | 130, 214, 556 |  |
| `Buber` ^[outline-2.md:#1] | 1 | 1 | 172 |  |
| `Kuhn` ^[outline-2.md:#1] | 1 | 1 | 186 |  |
| `Locke` ^[outline-2.md:#1] | 1 | 1 | 200 |  |
| `Parfit` ^[outline-2.md:#1] | 1 | 1 | 200 |  |
| `Bostrom` ^[outline-2.md:#1] | 1 | 1 | 200 |  |
| `Levinas` ^[outline-2.md:#1] | 1 | 1 | 300 |  |
| `Russell` ^[outline-2.md:#1] | 1 | 1 | 314 |  |
| `Gödel` ^[outline-2.md:#2] | 2 | 2 | 314, 428 |  |
| `Nietzsche` ^[outline-2.md:#2] | 2 | 2 | 398, 414 |  |
| `Popper` ^[outline-2.md:#1] | 1 | 1 | 442 |  |
| `Luhmann` ^[outline-2.md:#1] | 1 | 1 | 286 |  |
| `von Foerster` ^[outline-2.md:#1] | 1 | 1 | 286 |  |
| `Aristoteles` ^[outline-2.md:#1] | 1 | 1 | 272 |  |

## What the extraction ran into

**Zeros:** 1 — `TSDP`. It is not export damage: the document writes it only joined, in „Interne Barrieren und die Angst voreinander (TSDP-Dynamiken)“ ^[L125], so `TSDP` alone counts 0 and with compounds 1. The expansion of the abbreviation is not written anywhere in the document.

**Standing alone less often than with compounds:** 13 terms, all of them compounds or inflections, none of them a different thing. `AEGIS` stands in `AEGIS-Überwelt`, `AEGIS-Interface`, `AEGIS-Paradoxon` and `AEGIS-Kernbereiche`; `Kael` takes the genitive `Kaels`; `Echo` takes `Echos` ×3 and the plural reads as a compound count; `Mnemosyne` stands in `Mnemosyne-Archipel` ×4 and `Mnemosynes`; `Cerberus` in `Cerberus-Labyrinth` ×3; `Kairos` in `Kairos-Potentialis` ×2; `Riss` stands alone 4 times and 10 times with `Risse` ×3, `Riss-Manifestation`, `Risses` and `Rissen`. `Phobien`, `Host`, `Fundament`, `Überwelt`, `Selene` and `Juna/V` each gain one to four compound uses.

**Two surfaces, written both ways.** `Externe Ebene` ^[outline-2.md:#2] and `Externen Ebene` ^[outline-2.md:#2] are one phrase in two cases (nominative and dative), and `funktionale Multiplizität` ^[outline-2.md:#2], `funktionaler Multiplizität` ^[outline-2.md:#3] and `Multiplizität` ^[outline-2.md:#7] split the same way. `Guardian LogOS` ^[outline-2.md:#1] and `Guardian Cerberus` ^[outline-2.md:#1] stand once each, in one parenthesis, where the paragraph names a figure; elsewhere the field lines write the figure alone, `LogOS` and `Cerberus`. `Logos-Prime` is also a compound that contains `LogOS` case-insensitively, which is why `LogOS` shows `Logos-Prime` ×3 among its compounds.

**KW numbers.** The document writes the worlds with a plain digit (`KW1` to `KW4`) and never subscripted.

**Export damage.** The 40 bracketed chapter titles are written with escaped brackets (`\[` and `\]`), and the line L273 carries an escaped exclamation mark in the trope list of chapter 17. No invisible characters are in the export (profile). The field labels are written in bold (`**Core Theme:**`) and as a nested bullet; the count reads them as written. Inner ASCII quotation marks stand in the field lines (for example around `Nichts Rauschen` at L28), which is why those marks are not used as quotations here.

**The paragraph in the prologue and the repeated labels.** Chapter titles are bracketed on their own line and are not counted as candidates. The label `Chapter` stands 40 times (prologue and 39 chapters, `Chapter` ^[outline-2.md:#40] in the prose above), the label `Act` 4 times as a whole word.

**An idea without its word.** The kernel paradox of the system is rendered in several words. `Kernparadoxon` ^[outline-2.md:#5] and `Fehlausgerichtete Kohärenz` ^[outline-2.md:#4] name it; the sub-plot label `AEGIS Paradoxon` ^[outline-2.md:#32] follows it as a thread across chapters. The document writes the name `Kohärenz Protokoll` ^[outline-2.md:#1] once, in the prologue, and the German spelling there is with a space, not a hyphen.

**What it says of its own standing.** Nothing is claimed as canon. The document marks its content as open by question marks and `evtl.`/`möglicherweise` hedges, and calls itself a compilation in a „Neues Format“ ^[L15].

**Zeros:** 1 — `TSDP`.

**Standing alone less often than with compounds:** 13 — `AEGIS` 124/132, `Echo` 5/8, `Juna/V` 31/32, `Kael` 131/138, `Host` 3/4, `Überwelt` 21/25, `Fundament` 14/18, `Selene` 10/11, `Mnemosyne` 18/23, `Cerberus` 12/15, `Kairos` 3/5, `Phobien` 7/8, `Riss` 4/10.
