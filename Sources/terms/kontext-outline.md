---
source: Sources/drive/kontext-outline.md
drive_id: "1ci5TNH4nAXZUYniv6IKM3VbRSThBroLDAUGx2MkT4y4"
title: "Kontext outline"
category: plot-outline
index_date: "2025-05-03"
extracted: "2026-10-05"
candidates: 87    # the terms capture.py counted
---

# Term census — Kontext outline

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py kontext-outline`

```
  lines                505  (frontmatter ends at 9)
  body words           4661
  headings             40   bold-only lines 6
  table rows           0   code fences 0
  question marks       88
  backslash escapes    80
  typographic marks    34   ascii quotes 32
  invisible characters none
  math symbol lines    0
  glued ref numbers    44
  repeated labels      Core Theme x40, Kael Sys Focus x40, Plot Summary x40, Setting x40, AEGIS Focus x37
  longest line         1030 chars
```

## Stance, read per passage

The file is a briefing for an outline task, and it speaks in three registers that its own headings separate. **Observed:** the first body paragraph (L11) is English prose in the voice of an analyst, opening „Core Concept Analysis“ ^[L11]; the rest of the briefing is German, and the outline fields keep English labels (`Core Theme`, `Plot Summary`) over German content, lines 65 to 504.

**Orientation for the commission.** The paragraph is headed „Projekt Kontext (Zur Orientierung für den Auftrag)“ ^[L16] and describes the novel project in the present tense, as a report of what the project is: „Die Erzählung folgt einer“ ^[L18] three-act structure. It names its genre mix and its core paradox in one paragraph (L18).

**Glossary, framed as provisional.** The block is headed „Basis-Glossar (Zur Orientierung für den Autor)“ ^[L22], and its note says what the glossary is for: „Dieses Glossar dient als Grundlage.“ ^[L24] The same note commissions further work: „Sie sind beauftragt“ ^[L24] to refine or extend the concepts. The glossary entries are definitions (L26 to L53), marked in two places with a question mark about the item itself: „Aggressiver/kämpferischer Anteil (?)“ ^[L43], and „Potenziell integrierter/koordinierender Anteil am Ende“ ^[L44].

**Outline, as plan with hedges.** From L59 the document is headed with `Kontext für` the novel's title and „Prolog + 39 Kapitel“ ^[L59] and carries forty chapter blocks, in three acts: „Act Prologue“ ^[L61], „Act: Innere Reise (Heroine's Journey Fokus)“ ^[L74] (the file writes `Act 1:` with its digit, and `read.py` shows the line without it), and „Act: Äußere Konfrontation & Rückkehr (Hero's Journey Fokus)“ ^[L368]. Every chapter block carries the same labelled fields, and each field marks its own status by form: the text is written as plan, in noun phrases and present-tense summaries, and open points carry a question mark, as in „Selene als Koordinatorin?“ ^[L361] and „Selene führt?“ ^[L481]. The question marks stand on 68 lines, the first at L43 and then from L66 on; the sample line „Wer bin ich“ ^[L201] is a question the text puts in the characters' mouths, not an open point about the plan. The late chapters leave the outcome open on purpose: „Ende kann offen bleiben“ ^[L500]; and a field can offer two outcomes, as „Finale Rolle klar (oder rätselhaft)“ ^[L463].

**Labelled side fields.** The outline has fields beyond the five fixed ones: `Philo Hint`, `Trope Note`, `Subplot Focus`, `Turning Point`, `Foreshadowing`, `Other Concept`, `Juna/V Focus` and `Fundament Focus`. The Philo Hint entries name thinkers and topics, for instance „Hume (Identität/Erinnerung)“ ^[L84]; the Trope Note entries are English genre names, for instance „Unreliable Narrator“ ^[L85]. Both are lists of labels without a sentence about the world; a name that stands only there is a lens reference or a trope, and the census lists the thinkers under the lens heading.

## Candidates and counts

87 candidates, written while reading and frozen by the count (`Plan/runs/kontext-outline/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `kontext-outline.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kohärenz Protokoll` ^[kontext-outline.md:#4] | 4 | 4 | 11, 18, 59, 66 |  |
| `System Kael` ^[kontext-outline.md:#3] | 3 | 3 | 18, 34, 66 |  |
| `Kael` ^[kontext-outline.md:#107] | 107 | 114 | 11, 18, 27, 34, 38, 52, 66, 67, 70, 72, 79, 80 … | `Kaels` ×7 |
| `AEGIS` ^[kontext-outline.md:#115] | 115 | 124 | 11, 18, 26, 28, 48, 49, 50, 51, 53, 65, 66, 68 … | `AEGIS-Überwelt` ×3, `AEGIS-Entitäten` ×1, `AEGIS-Logik` ×1, `AEGIS-Interface` ×1 |
| `Komponente 734` ^[kontext-outline.md:#1] | 1 | 1 | 26 |  |
| `KW` ^[kontext-outline.md:#2] | 2 | 51 | 11, 28, 30, 31, 32, 33, 48, 53, 79, 81, 82, 90 … |  |
| `Konstrukt-Welt` ^[kontext-outline.md:#1] | 1 | 1 | 28 |  |
| `KW1` ^[kontext-outline.md:#11] | 11 | 12 | 30, 79, 81, 82, 90, 93, 101, 104, 115, 156, 159, 386 |  |
| `KW2` ^[kontext-outline.md:#15] | 15 | 15 | 31, 122, 123, 124, 125, 126, 134, 137, 145, 148, 245, 248 … |  |
| `KW3` ^[kontext-outline.md:#10] | 10 | 10 | 32, 166, 167, 169, 170, 324, 327, 330, 416, 419 |  |
| `KW4` ^[kontext-outline.md:#8] | 8 | 8 | 33, 215, 256, 259, 261, 262, 363, 484 |  |
| `Logos-Prime` ^[kontext-outline.md:#3] | 3 | 3 | 30, 82, 93 |  |
| `Mnemosyne-Archipel` ^[kontext-outline.md:#3] | 3 | 3 | 31, 126, 251 |  |
| `Cerberus-Labyrinth` ^[kontext-outline.md:#3] | 3 | 3 | 32, 170, 330 |  |
| `Kairos-Potentialis` ^[kontext-outline.md:#2] | 2 | 2 | 33, 262 |  |
| `Guardians` ^[kontext-outline.md:#16] | 16 | 16 | 33, 48, 94, 127, 138, 171, 252, 259, 263, 331, 373, 375 … |  |
| `Guardian` ^[kontext-outline.md:#9] | 9 | 25 | 30, 31, 32, 33, 48, 90, 94, 123, 127, 138, 167, 171 … | `Guardians` ×16 |
| `LogOS` ^[kontext-outline.md:#13] | 13 | 13 | 30, 48, 89, 90, 92, 94, 156, 380, 383, 385, 387, 394 | `Logos-Prime` ×3 |
| `Mnemosyne` ^[kontext-outline.md:#18] | 18 | 21 | 31, 48, 123, 125, 126, 127, 133, 134, 136, 138, 247, 248 … | `Mnemosyne-Archipel` ×3 |
| `Cerberus` ^[kontext-outline.md:#13] | 13 | 16 | 32, 48, 166, 167, 169, 170, 171, 327, 329, 330, 331, 413 … | `Cerberus-Labyrinth` ×3 |
| `Kairos` ^[kontext-outline.md:#5] | 5 | 7 | 33, 48, 259, 261, 262, 263 | `Kairos-Potentialis` ×2 |
| `Sophia` ^[kontext-outline.md:#5] | 5 | 5 | 33, 48, 259, 261, 263 |  |
| `Anteile` ^[kontext-outline.md:#9] | 9 | 14 | 27, 34, 175, 178, 201, 260, 305, 306, 311, 328, 360, 374 … | `Anteilen` ×4 |
| `Kael System` ^[kontext-outline.md:#1] | 1 | 1 | 34 |  |
| `ANP` ^[kontext-outline.md:#6] | 6 | 13 | 36, 52, 94, 102, 105, 113, 116, 134, 135, 145, 146, 178 … |  |
| `Apparently Normal Part` ^[kontext-outline.md:#1] | 1 | 1 | 36 |  |
| `EP` ^[kontext-outline.md:#3] | 3 | 20 | 45, 47, 52, 112, 113, 116, 123, 124, 127, 133, 134, 135 … |  |
| `Emotional Part` ^[kontext-outline.md:#1] | 1 | 1 | 45 |  |
| `Host (Kael)` ^[kontext-outline.md:#1] | 1 | 1 | 38 |  |
| `Host` ^[kontext-outline.md:#3] | 3 | 4 | 38, 79, 80, 124 | `Host-Dominanz` ×1 |
| `Lex` ^[kontext-outline.md:#20] | 20 | 20 | 39, 79, 80, 89, 90, 91, 101, 102, 156, 157, 190, 226 … |  |
| `Alex` ^[kontext-outline.md:#9] | 9 | 9 | 40, 100, 101, 102, 104, 157, 168, 328 |  |
| `Rhys` ^[kontext-outline.md:#12] | 12 | 12 | 41, 111, 112, 113, 124, 178, 179, 249, 305, 306, 405, 406 |  |
| `Argus` ^[kontext-outline.md:#11] | 11 | 11 | 42, 190, 202, 226, 227, 238, 270, 271, 294, 384, 438 |  |
| `Nyx` ^[kontext-outline.md:#3] | 3 | 3 | 43, 168, 328 |  |
| `Selene` ^[kontext-outline.md:#11] | 11 | 12 | 44, 67, 179, 305, 306, 360, 361, 374, 395, 438, 480, 481 | `Selene-Potenzial` ×1 |
| `Kiko` ^[kontext-outline.md:#5] | 5 | 5 | 47, 123, 134, 168, 328 |  |
| `Lia` ^[kontext-outline.md:#2] | 2 | 2 | 47, 134 |  |
| `Moros` ^[kontext-outline.md:#3] | 3 | 3 | 47, 123, 134 |  |
| `Juna/V` ^[kontext-outline.md:#29] | 29 | 29 | 11, 18, 49, 66, 70, 189, 191, 193, 216, 279, 282, 284 … |  |
| `Juna` ^[kontext-outline.md:#29] | 29 | 29 | 11, 18, 49, 66, 70, 189, 191, 193, 216, 279, 282, 284 … |  |
| `Fundament` ^[kontext-outline.md:#12] | 12 | 14 | 11, 18, 50, 205, 445, 448, 450, 451, 452, 460, 462, 480 … | `fundamentally` ×1, `fundamental` ×1, `Fundament-Erkenntnisse` ×1, `Fundament-Kontakt` ×1 |
| `Überwelt` ^[kontext-outline.md:#19] | 19 | 23 | 53, 69, 192, 215, 223, 226, 228, 229, 237, 240, 273, 282 … | `Überwelt-Interface` ×1 |
| `Paradox (AEGIS)` ^[kontext-outline.md:#1] | 1 | 1 | 51 |  |
| `Fehlausgerichtete Kohärenz` ^[kontext-outline.md:#4] | 4 | 4 | 51, 68, 292, 338 |  |
| `Fehlausgerichteten Kohärenz` ^[kontext-outline.md:#2] | 2 | 2 | 18, 335 |  |
| `Kernparadoxon` ^[kontext-outline.md:#5] | 5 | 5 | 18, 68, 293, 295, 340 |  |
| `TSDP` ^[kontext-outline.md:#1] | 1 | 3 | 18, 52, 144 | `TSDP-Prinzipien` ×1, `TSDP-Dynamiken` ×1 |
| `Theorie der Strukturellen Dissoziation der Persönlichkeit` ^[kontext-outline.md:#1] | 1 | 1 | 52 |  |
| `Echo` ^[kontext-outline.md:#7] | 7 | 9 | 11, 66, 67, 87, 133, 234, 437, 468 | `Echos` ×2 |
| `Genesis` ^[kontext-outline.md:#2] | 2 | 2 | 63, 405 |  |
| `Nichts Rauschen` ^[kontext-outline.md:#1] | 1 | 1 | 69 |  |
| `Inneres Konferenzzimmer` ^[kontext-outline.md:#1] | 1 | 1 | 181 |  |
| `Task Force` ^[kontext-outline.md:#1] | 1 | 1 | 213 |  |
| `Riss` ^[kontext-outline.md:#4] | 4 | 8 | 186, 189, 191, 192, 201, 282, 285, 352 | `Risse` ×3, `Riss-Manifestation` ×1 |
| `Glitches` ^[kontext-outline.md:#2] | 2 | 2 | 79, 189 |  |
| `Phobien` ^[kontext-outline.md:#5] | 5 | 7 | 52, 80, 112, 113, 142, 145, 146 |  |
| `Switches` ^[kontext-outline.md:#2] | 2 | 2 | 145, 146 |  |
| `Ko-Bewusstsein` ^[kontext-outline.md:#2] | 2 | 2 | 178, 179 |  |
| `funktionale Multiplizität` ^[kontext-outline.md:#2] | 2 | 2 | 364, 501 |  |
| `funktionaler Multiplizität` ^[kontext-outline.md:#3] | 3 | 3 | 491, 492, 500 |  |
| `Externe Ebene` ^[kontext-outline.md:#2] | 2 | 2 | 352, 494 |  |
| `Meta-Beobachter` ^[kontext-outline.md:#3] | 3 | 3 | 42, 202, 271 |  |
| `Drei-Akt-Struktur` ^[kontext-outline.md:#1] | 1 | 1 | 18 |  |
| `Innere Reise` ^[kontext-outline.md:#2] | 2 | 2 | 18, 74 |  |
| `Meta-Analyse` ^[kontext-outline.md:#2] | 2 | 2 | 18, 272 |  |
| `Äußere Konfrontation` ^[kontext-outline.md:#2] | 2 | 2 | 18, 368 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Heroine's Journey` ^[kontext-outline.md:#2] | 2 | 2 | 18, 74 |  |
| `Hero's Journey` ^[kontext-outline.md:#1] | 1 | 1 | 368 |  |
| `Zweite-Ordnung-Kybernetik` ^[kontext-outline.md:#2] | 2 | 2 | 269, 275 |  |
| `Panoptismus` ^[kontext-outline.md:#1] | 1 | 1 | 81 |  |
| `Hume` ^[kontext-outline.md:#2] | 2 | 2 | 84, 242 |  |
| `Kant` ^[kontext-outline.md:#1] | 1 | 1 | 95 |  |
| `Hobbes` ^[kontext-outline.md:#1] | 1 | 1 | 106 |  |
| `Sartre` ^[kontext-outline.md:#3] | 3 | 3 | 150, 217, 485 |  |
| `Buber` ^[kontext-outline.md:#1] | 1 | 1 | 183 |  |
| `Kuhn` ^[kontext-outline.md:#1] | 1 | 1 | 194 |  |
| `Locke` ^[kontext-outline.md:#1] | 1 | 1 | 206 |  |
| `Parfit` ^[kontext-outline.md:#1] | 1 | 1 | 206 |  |
| `von Foerster` ^[kontext-outline.md:#1] | 1 | 1 | 275 |  |
| `Luhmann` ^[kontext-outline.md:#1] | 1 | 1 | 275 |  |
| `Levinas` ^[kontext-outline.md:#1] | 1 | 1 | 287 |  |
| `Russell` ^[kontext-outline.md:#1] | 1 | 1 | 298 |  |
| `Gödel` ^[kontext-outline.md:#2] | 2 | 2 | 298, 388 |  |
| `Popper` ^[kontext-outline.md:#1] | 1 | 1 | 399 |  |
| `Aristoteles` ^[kontext-outline.md:#1] | 1 | 1 | 264 |  |
| `Qualia` ^[kontext-outline.md:#1] | 1 | 1 | 128 |  |

## What the extraction ran into

**Zeros:** none of the 87 candidates counts 0, so no inflection and no export damage hides a name. The two spellings of the paradox (`Fehlausgerichtete Kohärenz` and `Fehlausgerichteten Kohärenz`) and of the multiplicity (`funktionale Multiplizität` and `funktionaler Multiplizität`) were both listed because the document writes each, in a different case; each counts above zero. `Juna` and `Juna/V` count the same, 29 each, because the document never writes `Juna` without the `/V`.

**Standing alone less often than with compounds:** 19 rows, and what fills the difference is read from the lines, not guessed. `Kael` ×7 as `Kaels` (inflection). `AEGIS` ×6 in hyphen compounds. `KW` stands alone only twice (L28 and L376, `KW(en)`); the other 49 are `KW1` to `KW4` with the digit written glued, and `KWs` ×4. `Guardian` stands alone 9 times against 25, because `Guardians` ×16 contains it. `Mnemosyne`, `Cerberus`, `Kairos` and `Überwelt` differ by the world names and compounds (`Mnemosyne-Archipel`, `Cerberus-Labyrinth`, `Kairos-Potentialis`, `AEGIS-Überwelt`, `Überwelt-Interface`). `Anteile` ×4 as `Anteilen` (inflection). `ANP` 6 alone against 13: `ANPs` ×4 and the hyphen compounds `ANP-Konflikt` and `ANP-Dynamik`. `EP` 3 alone against 20: `EPs` ×11 and slash and hyphen compounds such as `ANP/EP-Phobien`. `Host` ×1 as `Host-Dominanz`. `Selene` ×1 as `Selene-Potenzial`. `Fundament` 12 alone against 14, with `Fundament-Erkenntnisse` and `Fundament-Kontakt`; the English words `fundamentally` (L11) and `fundamental` also contain the stem and are counted by `in`, not by the term. `TSDP` stands alone once and in `TSDP-Prinzipien` and `TSDP-Dynamiken`. `Echo` ×2 as `Echos`. `Riss` ×3 as `Risse` and ×1 as `Riss-Manifestation`. `Phobien` ×2 in `ANP/EP-Phobien`.

**Export artifacts.** The export writes 80 backslash escapes: chapter headings read `\[Genesis\]`, and `-\>` stands for an arrow. The display of `read.py` and the quotation checker normalise the escapes, so quotations of those lines are written without them. Digits glued to words are 44 in the profile: the chapter headings are written `Chapter 1:` in the file, but `read.py` shows the heading without the number, so a chapter number is visible in the file and cannot be quoted. `Wendepunkt (Plot Point 1)` at L218 reads without its digit in the display. The frontmatter ends at L9 and the first body line is blank.

**Repeated labels.** The profile names five labels that repeat: `Core Theme` ×40, `Plot Summary` ×40, `Kael Sys Focus` ×40, `Setting` ×40 and `AEGIS Focus` ×37. These are the template's field names, not the document's terms; they stand under every chapter and are left off the candidate list. `AEGIS Focus` is absent from the last three chapters (L477 to L504); the fields `Juna/V Focus` (L463, L482) and `Fundament Focus` (L483) stand beside it or in its place.

**Writing in two languages.** English glossary names (`Apparently Normal Part`, `Emotional Part`) are written beside the German text, and the glossary abbreviates them (`ANP`, `EP`). `TSDP` is spelled out once (L52) and used elsewhere as the short form. Several plan fields put a name in quotation marks, for instance „Inneres Konferenzzimmer“ ^[L181] and „Task Force“ ^[L213]; nothing in the document says whether the marks mean invention or citation.

**The document's own standing.** The glossary note calls itself a base: „Dieses Glossar dient als Grundlage.“ ^[L24] The same note authorises revision: „Sie sind beauftragt“ ^[L24]. That is the document's claim about itself; the census records it and applies nothing. The title line, `Kontext outline`, comes from the manifest and the document does not write it.

**What the document defines and what it assumes.** `Komponente 734` stands once (L26) in a definition of `AEGIS` and nowhere else; the document does not define it. The glossary defines `Überwelt`, `Fundament`, `KW` and the four named worlds; the outline then uses the worlds with their digits (`KW1` to `KW4`), a form the glossary also writes in its headings.

---

Facts to explain, as the draft lists them:

**Zeros:** 0.

**Standing alone less often than with compounds:** 19 — `Kael` 107/114, `AEGIS` 115/124, `KW` 2/51, `KW1` 11/12, `Guardian` 9/25, `Mnemosyne` 18/21, `Cerberus` 13/16, `Kairos` 5/7, `Anteile` 9/14, `ANP` 6/13, `EP` 3/20, `Host` 3/4, `Selene` 11/12, `Fundament` 12/14, `Überwelt` 19/23, `TSDP` 1/3, `Echo` 7/9, `Riss` 4/8, `Phobien` 5/7.
