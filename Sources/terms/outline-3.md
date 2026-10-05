---
source: Sources/drive/outline-3.md
drive_id: "1SRa5ciSqKEyq-WSUG0EoMpnSdAKcJdoQ4lPEIwnIPDQ"
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

`python3 scripts/profile.py outline-3`

```
  lines                659  (frontmatter ends at 9)
  body words           6959
  headings             0   bold-only lines 4
  table rows           0   code fences 0
  question marks       112
  backslash escapes    160
  typographic marks    65   ascii quotes 22
  invisible characters none
  math symbol lines    0
  glued ref numbers    44
  repeated labels      none
  longest line         695 chars
```

## Stance, read per passage

The document is an outline, and it speaks as a plan throughout. It is headed „Act Prologue:“ ^[L11] and „Chapter Prologue:“ ^[L13], and then runs 39 chapters, each headed `Chapter N:` and holding two labelled blocks, `\[Handlung\]` (a prose paragraph, 40 of them) and `\[Konzeptionelles\]` (seven fixed field labels as an indented list). The profile's 160 backslash escapes are the brackets of these labels: 80 `\[` and 80 `\]`, one pair per label, plus one `\!` at L303. The profile finds no heading and four bold-only lines; those are the Prologue act line and the three act headings.

**Prologue, L11 to L27.** The `\[Handlung\]` at L17 is a summary of an origin that comes before the story, written in the present tense as a statement of what happens: „Die Erzählung fokussiert auf die Entität AEGIS oder ihr Vorläufer-Ich“ ^[L17]. It writes the external cause with a question mark: „Resonanz des Echos mit einer externen Anomalie (Juna/V?)“ ^[L17].

**Acts, L29, L239, L449.** The three bold headings name a lens in their own words: „Innere Reise (Heroine's Journey Fokus)“ ^[L29], „Meta-Ebene & Zyklen (Meta-Exploration)“ ^[L239] and „Äußere Konfrontation & Rückkehr (Hero's Journey Fokus)“ ^[L449].

**Chapter paragraphs.** The `\[Handlung\]` paragraphs are a plan in the subjunctive and in hedges: „möglicherweise erster Einfluss von Lex“ ^[L35], „könnte scheitern oder unerwünschte Systemreaktionen provozieren“ ^[L67]. A flat statement of what the plan fixes stands, for instance, „Es ist ein Punkt ohne Wiederkehr.“ ^[L227]. The ending is said to be able to stay open on some mysteries: „Das Ende kann offen bleiben bezüglich einiger Mysterien“ ^[L648].

**Questions.** The `\[Konzeptionelles\]` lists put open points as question marks, for example „Selene-Potenzial beginnt zu keimen?“ ^[L184]. The profile counts 112 question marks, and 82 lines hold at least one. Chapter 12 (L211) also writes questions as the character's own: „Wer oder was bin ich wirklich?“ ^[L211] and „Ist das alles nur eine Simulation?“ ^[L211].

**The field template, and where it bends.** `Core Theme`, `Kael Internal`, `Setting`, `Subplots`, `Philosophy` and `Genre/Trope` each stand 40 times (once per block), `AEGIS Focus` 37 times. They are the template and are not listed as candidates. The template changes in the last chapters: „Juna/V Fokus: Finale Rolle im Konflikt“ ^[L590] stands in chapter 35, a further `Juna/V Fokus` label (L622) and „Fundament Fokus: Beziehung zum Fundament als Option/Hintergrund.“ ^[L623] stand in chapter 37 where `AEGIS Focus` is missing, and the last block adds „Narrative Funktion: Bietet thematischen Abschluss“ ^[L658]. Chapters 38 and 39 have no `AEGIS Focus` line either. Late `Subplots` lines say only „Alle Subplots konvergieren hier.“ ^[L592].

## Candidates and counts

93 candidates, written while reading and frozen by the count (`Plan/runs/outline-3/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `outline-3.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `AEGIS` ^[outline-3.md:#153] | 153 | 159 | 17, 21, 23, 24, 25, 39, 41, 42, 43, 51, 57, 59 … | `AEGIS-Überwelt` ×3, `AEGIS-Basiskontrolle` ×1, `AEGIS-Paradoxon` ×1, `AEGIS-Kern` ×1 |
| `Komponente 734` ^[outline-3.md:#3] | 3 | 3 | 17, 551 |  |
| `Vorläufer-Ich` ^[outline-3.md:#1] | 1 | 1 | 17 |  |
| `Nichts Rauschen` ^[outline-3.md:#2] | 2 | 2 | 17, 24 |  |
| `Echo` ^[outline-3.md:#4] | 4 | 8 | 17, 22, 119, 265, 405, 551, 604 | `Echos` ×4 |
| `Kohärenz Protokoll` ^[outline-3.md:#1] | 1 | 1 | 17 |  |
| `System Kael` ^[outline-3.md:#1] | 1 | 1 | 17 |  |
| `Schutz-Clustern` ^[outline-3.md:#1] | 1 | 1 | 17 |  |
| `Juna/V` ^[outline-3.md:#33] | 33 | 33 | 17, 25, 195, 201, 203, 235, 253, 325, 329, 331, 333, 335 … |  |
| `Kael` ^[outline-3.md:#148] | 148 | 160 | 17, 22, 25, 35, 40, 43, 51, 56, 59, 67, 72, 75 … | `Kaels` ×12 |
| `Host` ^[outline-3.md:#3] | 3 | 4 | 35, 40, 99, 104 | `Host-Dominanz` ×1 |
| `Lex` ^[outline-3.md:#26] | 26 | 26 | 35, 40, 51, 55, 56, 67, 72, 83, 88, 131, 147, 152 … |  |
| `Alex` ^[outline-3.md:#19] | 19 | 19 | 67, 71, 72, 74, 77, 83, 88, 131, 152, 163, 168, 232 … |  |
| `Rhys` ^[outline-3.md:#18] | 18 | 18 | 83, 87, 88, 89, 104, 120, 179, 184, 232, 282, 357, 362 … |  |
| `Nyx` ^[outline-3.md:#4] | 4 | 4 | 163, 168, 389, 519 |  |
| `Kiko` ^[outline-3.md:#10] | 10 | 10 | 99, 104, 115, 120, 163, 168, 357, 389, 394, 519 |  |
| `Lia` ^[outline-3.md:#2] | 2 | 2 | 115, 120 |  |
| `Moros` ^[outline-3.md:#4] | 4 | 4 | 99, 104, 115, 120 |  |
| `Selene` ^[outline-3.md:#9] | 9 | 11 | 22, 184, 357, 362, 437, 442, 460, 492, 556, 616, 621 | `Selene-Potenzial` ×1, `Selenes` ×1 |
| `Argus` ^[outline-3.md:#12] | 12 | 12 | 195, 200, 216, 245, 250, 266, 309, 314, 341, 346, 476, 556 |  |
| `ANP` ^[outline-3.md:#4] | 4 | 16 | 55, 59, 72, 75, 83, 88, 91, 115, 120, 131, 136, 140 … |  |
| `ANPs` ^[outline-3.md:#9] | 9 | 9 | 59, 72, 83, 88, 115, 120, 131, 140, 179 |  |
| `EP` ^[outline-3.md:#2] | 2 | 21 | 83, 88, 91, 99, 104, 107, 115, 119, 120, 123, 131, 136 … |  |
| `EPs` ^[outline-3.md:#13] | 13 | 14 | 83, 88, 91, 104, 115, 119, 131, 171, 179, 282, 471, 503 … |  |
| `TSDP` ^[outline-3.md:#1] | 1 | 2 | 39, 135 | `TSDP-Dynamiken` ×1 |
| `Switches` ^[outline-3.md:#2] | 2 | 2 | 131, 136 |  |
| `Ko-Bewusstsein` ^[outline-3.md:#2] | 2 | 2 | 179, 184 |  |
| `Ko-Präsenz` ^[outline-3.md:#1] | 1 | 1 | 183 |  |
| `funktionaler Multiplizität` ^[outline-3.md:#3] | 3 | 3 | 633, 637, 653 |  |
| `Funktionale Multiplizität` ^[outline-3.md:#1] | 1 | 1 | 652 |  |
| `Phobien` ^[outline-3.md:#7] | 7 | 8 | 83, 88, 131, 135, 136, 179, 184, 519 |  |
| `Task Force` ^[outline-3.md:#1] | 1 | 1 | 232 |  |
| `Inneres Konferenzzimmer` ^[outline-3.md:#1] | 1 | 1 | 186 |  |
| `Glitches` ^[outline-3.md:#2] | 2 | 2 | 35, 195 |  |
| `Riss` ^[outline-3.md:#6] | 6 | 11 | 195, 199, 201, 202, 205, 211, 245, 325, 332, 428 | `Risse` ×3, `Risses` ×1, `Rissen` ×1 |
| `Risse` ^[outline-3.md:#3] | 3 | 5 | 211, 245, 325, 332, 428 | `Risses` ×1, `Rissen` ×1 |
| `KW1` ^[outline-3.md:#12] | 12 | 13 | 35, 41, 42, 51, 58, 67, 74, 90, 99, 147, 154, 478 |  |
| `KW2` ^[outline-3.md:#16] | 16 | 16 | 99, 103, 104, 105, 106, 115, 122, 131, 138, 147, 179, 277 … |  |
| `KW3` ^[outline-3.md:#10] | 10 | 10 | 163, 167, 169, 170, 179, 389, 393, 396, 519, 526 |  |
| `KW4` ^[outline-3.md:#9] | 9 | 10 | 234, 293, 297, 299, 300, 309, 444, 471, 624 |  |
| `Kernwelten` ^[outline-3.md:#3] | 3 | 3 | 245, 261, 600 |  |
| `Logos-Prime` ^[outline-3.md:#3] | 3 | 3 | 42, 58, 74 |  |
| `Mnemosyne-Archipel` ^[outline-3.md:#4] | 4 | 4 | 99, 106, 122, 284 |  |
| `Cerberus-Labyrinth` ^[outline-3.md:#3] | 3 | 3 | 163, 170, 396 |  |
| `Kairos-Potentialis` ^[outline-3.md:#2] | 2 | 2 | 293, 300 |  |
| `Überwelt` ^[outline-3.md:#22] | 22 | 25 | 24, 202, 234, 245, 249, 251, 252, 261, 268, 309, 316, 325 … |  |
| `AEGIS-Überwelt` ^[outline-3.md:#3] | 3 | 3 | 24, 252, 462 |  |
| `Meta-Ebene` ^[outline-3.md:#4] | 4 | 4 | 227, 239, 245, 249 |  |
| `Fundament` ^[outline-3.md:#17] | 17 | 21 | 25, 219, 325, 341, 405, 421, 567, 571, 573, 574, 575, 583 … | `Fundaments` ×3, `fundamentale` ×2, `Fundament-Kontakt` ×1 |
| `Externen Ebene` ^[outline-3.md:#4] | 4 | 4 | 325, 329, 332, 428 |  |
| `Guardians` ^[outline-3.md:#15] | 15 | 15 | 59, 107, 123, 171, 285, 293, 301, 397, 455, 461, 463, 479 … |  |
| `Guardian LogOS` ^[outline-3.md:#1] | 1 | 1 | 51 |  |
| `LogOS` ^[outline-3.md:#15] | 15 | 15 | 51, 55, 57, 58, 59, 99, 147, 471, 475, 477, 479, 487 … | `Logos-Prime` ×3 |
| `Mnemosyne` ^[outline-3.md:#19] | 19 | 24 | 99, 105, 106, 107, 115, 119, 121, 122, 123, 131, 277, 281 … | `Mnemosyne-Archipel` ×4, `Mnemosynes` ×1 |
| `Cerberus` ^[outline-3.md:#14] | 14 | 17 | 163, 167, 169, 170, 171, 173, 389, 395, 396, 397, 519, 523 … | `Cerberus-Labyrinth` ×3 |
| `Kairos` ^[outline-3.md:#3] | 3 | 5 | 293, 299, 300, 301 | `Kairos-Potentialis` ×2 |
| `Sophia` ^[outline-3.md:#3] | 3 | 3 | 293, 299, 301 |  |
| `Kernparadoxon` ^[outline-3.md:#6] | 6 | 6 | 23, 245, 341, 347, 411, 471 |  |
| `AEGIS Paradoxon` ^[outline-3.md:#32] | 32 | 32 | 25, 43, 59, 75, 91, 107, 123, 139, 155, 171, 187, 203 … |  |
| `Fehlausgerichtete Kohärenz` ^[outline-3.md:#5] | 5 | 5 | 23, 245, 341, 345, 405 |  |
| `Kael Integration` ^[outline-3.md:#34] | 34 | 34 | 25, 43, 59, 75, 91, 107, 123, 139, 155, 171, 187, 203 … |  |
| `Gaslighting` ^[outline-3.md:#5] | 5 | 5 | 147, 153, 157, 455 |  |
| `Panoptismus` ^[outline-3.md:#1] | 1 | 1 | 41 |  |
| `Kerntraumata` ^[outline-3.md:#1] | 1 | 1 | 503 |  |
| `Genesis` ^[outline-3.md:#1] | 1 | 1 | 503 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Heroine's Journey` ^[outline-3.md:#1] | 1 | 1 | 29 |  |
| `Hero's Journey` ^[outline-3.md:#1] | 1 | 1 | 449 |  |
| `Plot Point 1` ^[outline-3.md:#1] | 1 | 1 | 237 |  |
| `Plot Point 2` ^[outline-3.md:#1] | 1 | 1 | 447 |  |
| `Care Ethics` ^[outline-3.md:#1] | 1 | 1 | 92 |  |
| `Zweite-Ordnung-Kybernetik` ^[outline-3.md:#2] | 2 | 2 | 313, 318 |  |
| `Hume` ^[outline-3.md:#2] | 2 | 2 | 44, 270 |  |
| `Kant` ^[outline-3.md:#3] | 3 | 3 | 60, 254, 382 |  |
| `Hobbes` ^[outline-3.md:#1] | 1 | 1 | 76 |  |
| `Locke` ^[outline-3.md:#2] | 2 | 2 | 108, 220 |  |
| `Bergson` ^[outline-3.md:#1] | 1 | 1 | 108 |  |
| `Sartre` ^[outline-3.md:#3] | 3 | 3 | 140, 236, 626 |  |
| `Kierkegaard` ^[outline-3.md:#1] | 1 | 1 | 172 |  |
| `Buber` ^[outline-3.md:#1] | 1 | 1 | 188 |  |
| `Kuhn` ^[outline-3.md:#1] | 1 | 1 | 204 |  |
| `Parfit` ^[outline-3.md:#1] | 1 | 1 | 220 |  |
| `Bostrom` ^[outline-3.md:#1] | 1 | 1 | 220 |  |
| `Levinas` ^[outline-3.md:#1] | 1 | 1 | 334 |  |
| `Russell` ^[outline-3.md:#1] | 1 | 1 | 350 |  |
| `Gödel` ^[outline-3.md:#2] | 2 | 2 | 350, 480 |  |
| `Nietzsche` ^[outline-3.md:#2] | 2 | 2 | 446, 464 |  |
| `Popper` ^[outline-3.md:#1] | 1 | 1 | 496 |  |
| `Luhmann` ^[outline-3.md:#1] | 1 | 1 | 318 |  |
| `von Foerster` ^[outline-3.md:#1] | 1 | 1 | 318 |  |
| `Aristoteles` ^[outline-3.md:#1] | 1 | 1 | 302 |  |
| `Logischer Positivismus` ^[outline-3.md:#1] | 1 | 1 | 60 |  |
| `Kybernetik` ^[outline-3.md:#1] | 1 | 4 | 254, 309, 313, 318 |  |
| `Cosmic Horror` ^[outline-3.md:#3] | 3 | 3 | 27, 335, 577 |  |

## What the extraction ran into

The draft lists no zero: all 93 candidates stand at least once as written, so no inflection, export damage or absence needs explaining as a zero.

Twenty rows stand alone less often than inside compounds or inflected forms, and each was read on its lines.

- `AEGIS` 153/159: six compounds, `AEGIS-Überwelt` ×3, `AEGIS-Basiskontrolle` ×1, `AEGIS-Paradoxon` ×1 (hyphenated, while the list's `AEGIS Paradoxon` is the spaced form the document writes in the Subplots lines) and `AEGIS-Kern` ×1.
- `Echo` 4/8 and `Kael` 148/160 and `Selene` 9/11 and `Mnemosyne` 19/24 and `Kairos` 3/5: inflection or a name inside a compound, `Echos` ×4 (L17, L119, L405, L551), `Kaels` ×12, `Selenes` and `Selene-Potenzial`, `Mnemosynes` and `Mnemosyne-Archipel` ×4, `Kairos-Potentialis` ×2.
- `Host` 3/4 and `ANP` 4/16 and `EP` 2/21 and `EPs` 13/14 and `TSDP` 1/2: compounds with a hyphen or slash. `Host-Dominanz`, `TSDP-Dynamiken`, and the abbreviations in `ANP-Dominanz`, `ANP-Konflikt`, `ANP-Dynamik`, `ANP/EP-Phobien`, `EP-Intrusion`, `EP-Bewusstwerdung`, `EP-Intrusionen`, `EP-Differenzierung`. `ANPs` and `EPs` are listed as their own surfaces; the extra `EPs` is `Abwehr-EPs` at L171. The document never writes either abbreviation out in full; `ANP` and `EP` are used as already known.
- `Phobien` 7/8: the eighth is `ANP/EP-Phobien` (L136). The singular `Phobie` stands once, separately.
- `Riss` 6/11 and `Risse` 3/5: the plural and case forms `Risse`, `Risses`, `Rissen` ×3, ×1, ×1 are one family counted twice by design, because the list holds both.
- `KW1` 12/13 and `KW4` 9/10: `KW1-Ordnung` (L41) and `KW4-Erfahrung` (L471). The document writes the world names with a plain digit and never with a subscript; the digit is part of the name and the profile's 44 glued reference numbers are such cases and chapter references.
- `Überwelt` 22/25: `AEGIS-Überwelt` ×3.
- `Fundament` 17/21: `Fundaments` ×3, `Fundament-Kontakt` ×1 and `fundamentale` ×2 (L341, L535), which is the ordinary adjective and not the term.
- `Cerberus` 14/17: `Cerberus-Labyrinth` ×3.
- `Kybernetik` 1/4: the three others are the compounds `Zweite-Ordnung-Kybernetik` (L313, L318) and the inflected `Zweiten-Ordnung-Kybernetik` (L309).

`Heroine's Journey` and `Hero's Journey` each stand once, in an act heading (L29, L449). `Plot Point 1` and `Plot Point 2` stand in `Genre/Trope` lines; the export keeps the digit.

The protocol the Prologue activates is written `Kohärenz Protokoll` ^[outline-3.md:#1] with a space; the hyphenated `Kohärenz-Protokoll` ^[outline-3.md:#0] stands 0 times, a true absence of that surface. `Komponente 734` is written with a plain 734 and the 734 recurs at L551. The document says in L83 that „Der Fürsorger-Anteil Rhys tritt hervor“ ^[L83], and in L67 „Der Beschützer-Anteil Alex wird aktiviert“ ^[L67], so the text calls `Alex` and `Rhys` an „Anteil“ each, a part. Two further roles stand in parentheses, `Kael (Host)` at L35 and `Argus (Meta-Beobachter)` at L216.

Export findings: Mixed quote glyphs occur, 22 ASCII and 65 typographic marks per the profile, and the document's own `Fehlausgerichtete Kohärenz` stands in curly marks at L245, L341, L345 and L405 and in straight marks at L23. The digit after `Akt` is dropped by the line preview for `Akt 1` and similar, so a `read.py --find` for „Akt 1“ is refused although `Akt 1` stands in the file at L227. The document makes no claim about its own standing: `Canon` ^[outline-3.md:#0] and `Kanon` ^[outline-3.md:#0] stand 0 times, so there is no canon claim to record.

**Zeros:** 0.

**Standing alone less often than with compounds:** 20 — `AEGIS` 153/159, `Echo` 4/8, `Kael` 148/160, `Host` 3/4, `Selene` 9/11, `ANP` 4/16, `EP` 2/21, `EPs` 13/14, `TSDP` 1/2, `Phobien` 7/8, `Riss` 6/11, `Risse` 3/5, `KW1` 12/13, `KW4` 9/10, `Überwelt` 22/25, `Fundament` 17/21, `Mnemosyne` 19/24, `Cerberus` 14/17, `Kairos` 3/5, `Kybernetik` 1/4.
