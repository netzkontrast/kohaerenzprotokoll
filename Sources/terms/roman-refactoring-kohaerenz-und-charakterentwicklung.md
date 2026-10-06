---
source: Sources/drive/roman-refactoring-kohaerenz-und-charakterentwicklung.md
drive_id: "1smMGBTWAarYWuqTEmq84BkAyZf8dXrGfjbqfqptf8WA"
title: "Roman-Refactoring: Kohärenz und Charakterentwicklung"
category: charaktere
index_date: "2026-02-26"
extracted: "2026-10-06"
candidates: 96    # the terms capture.py counted
---

# Term census — Roman-Refactoring: Kohärenz und Charakterentwicklung

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py roman-refactoring-kohaerenz-und-charakterentwicklung`

```
  lines                166  (frontmatter ends at 9)
  body words           4560
  headings             20   bold-only lines 0
  table rows           14   code fences 0
  question marks       4
  backslash escapes    110
  typographic marks    8   ascii quotes 70
  invisible characters none
  math symbol lines    0
  glued ref numbers    38
  repeated labels      none
  longest line         1423 chars
```

## Stance, read per passage

The whole document speaks in the first person of an assistant to the author, and says so at the start: „Herzlich willkommen.“ ^[L13] It names its own role as „Novel Writing Assistent“ ^[L13], and it calls itself a plan: „Der vorliegende Refaktorierungsplan zielt darauf ab“ ^[L15]. Every passage is a proposal or a reading-in of the author's material, never a report of finished text; the document marks its proposals in its own words: „empfehle ich die narrative Integration“ ^[L33], „Ich schlage für die Überarbeitung vor“ ^[L68], „Ich empfehle Ihnen“ ^[L134].

**L17 to L23, section 1 (the repository).** An account of the author's digital project structure; it names directories and files as the place where the novel is administered, for example „Die Analyse des Repositorium-Strukturbaums“ ^[L19] and „ncp_validate.py“ ^[L21]. These are file names, not terms of the world, and they are not on the list.

**L25 to L33, section 2 (ontology).** The document states how the novel's system is built: „Die Systemarchitektur des Romans beruht auf der Dual-Kernel-Theorie“ ^[L27]. It assigns roles in the world and the philosophy that goes with each: „als die absolute Verkörperung der Korrespondenztheorie der Wahrheit begreifen“ ^[L29] for AEGIS, and „Dieser dogmatischen Ordnung stellt sich die Anomalie Juna entgegen“ ^[L31]. The section ends with a question to the author, „Ist diese philosophische Ausrichtung für die Interaktionen“ ^[L33].

**L35 to L68, section 3 (the psychology).** The document describes the protagonist's structure: „Das System Kael besteht aus elf hochspezialisierten Anteilen“ ^[L41]. The matrix of L49 to L62 gives each Anteil four fields in a table whose header cells are written with escaped asterisks; its own description is „dient als primäres Werkzeug für das Refactoring“ ^[L45]. The last passage ends in a question, „Haben Sie bereits spezifische sprachliche Eigenheiten“ ^[L68].

**L70 to L138, sections 4 to 7 (the three acts and the recommendations).** The acts are headed `Refactoring Akt` three times (L70, L86, L108), with chapter ranges in the headings. The passages are written in the indicative as the plan for what happens in the novel, for example „Der dritte Akt ist das Crescendo“ ^[L110] and „Der Roman kulminiert in einem metaleptischen Bruch der vierten Wand“ ^[L128]. Section 7 recommends and asks again: „Wie genau stellen Sie sich die sprachliche Signatur“ ^[L136] and „Sind Sie bereit, die Architektur der Konstrukt-Stadt“ ^[L138].

**L140 to L165, the reference list.** The footnote numbers glued to the sentences point to this list; it is headed `Referenzen` and its entries are titles of other texts and web pages. Fourteen entries end with `Zugriff am Februar 26, 2026` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#14]. Theory and physics passages carry such a number, and the sentence then reports what that reference says, so the names of philosophers and physicists in those sentences are the references' and the document's report of them, not the novel's own invention.

## Candidates and counts

96 candidates, written while reading and frozen by the count (`Plan/runs/roman-refactoring-kohaerenz-und-charakterentwicklung/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `roman-refactoring-kohaerenz-und-charakterentwicklung.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kohärenz Protokoll` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#4] | 4 | 4 | 11, 13, 128, 158 |  |
| `Dual-Kernel-Theorie` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#4] | 4 | 4 | 15, 21, 25, 27 |  |
| `DKT` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 27 |  |
| `Kohärenz-Kernel` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 27 |  |
| `Kollaps-Kernel` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 2 | 27, 31 | `Kollaps-Kernels` ×1 |
| `AEGIS` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#41] | 41 | 41 | 27, 29, 31, 33, 37, 39, 54, 55, 58, 59, 60, 66 … |  |
| `Autonomous Entropic Gatekeeper for Integrity Systems` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 29 |  |
| `Juna` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#11] | 11 | 12 | 27, 31, 33, 80, 84, 100, 104, 106, 116 | `Junas` ×1 |
| `Anomalie Juna` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#2] | 2 | 2 | 27, 31 |  |
| `Kael` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#43] | 43 | 57 | 15, 21, 29, 33, 35, 37, 39, 41, 51, 52, 58, 61 … | `Kaels` ×14 |
| `System Kael` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#3] | 3 | 3 | 35, 41, 51 |  |
| `Konstrukt-Stadt` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#6] | 6 | 6 | 21, 54, 60, 72, 110, 138 |  |
| `Überwelt` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#4] | 4 | 4 | 86, 88, 100, 110 |  |
| `Nexus` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 88 |  |
| `Guardians` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 88 |  |
| `LogOS` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#7] | 7 | 7 | 90, 92, 94 |  |
| `Mnemosyne` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#5] | 5 | 5 | 96, 98, 100 |  |
| `Genesis-Krise` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 39 |  |
| `Tertiären Strukturellen Dissoziation der Persönlichkeit` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 39 |  |
| `TSDP` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 3 | 39, 51, 132 | `TSDP-Typ` ×1, `TSDP-Traumastruktur` ×1 |
| `Phänomenales Selbstmodell` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 39 |  |
| `PSM` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#3] | 3 | 3 | 39, 98 |  |
| `Anscheinend Normale Persönlichkeitsanteile` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 41 |  |
| `ANPs` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#2] | 2 | 2 | 41, 84 |  |
| `Emotionale Persönlichkeitsanteile` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 41 |  |
| `EPs` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#6] | 6 | 6 | 41, 61, 80, 92, 98, 100 |  |
| `Cache-Inkohärenz` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#2] | 2 | 2 | 52, 98 |  |
| `Selene` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#4] | 4 | 4 | 53, 92, 106 |  |
| `Nyx` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#6] | 6 | 6 | 54, 68, 126 |  |
| `Lex` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#7] | 7 | 8 | 55, 68, 76, 126, 136 |  |
| `Moros` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#6] | 6 | 6 | 56, 60, 116, 136 |  |
| `Kiko` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#7] | 7 | 7 | 57, 76, 98, 116, 126 |  |
| `Lia` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#3] | 3 | 3 | 58, 98 |  |
| `Isabelle` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#3] | 3 | 3 | 59 |  |
| `Rhys` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#5] | 5 | 5 | 60, 100, 126 |  |
| `Alex` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#3] | 3 | 3 | 61 |  |
| `Argus` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#4] | 4 | 4 | 62, 92 |  |
| `Funktionale Multiplizität` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 64 |  |
| `Funktionalen Multiplizität` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 66 |  |
| `Final Fusion` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#2] | 2 | 2 | 66, 126 |  |
| `Mosaik-Herz` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#3] | 3 | 3 | 108, 124, 126 |  |
| `External Awakening` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 128 |  |
| `Nichts-Rauschen` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#3] | 3 | 3 | 78, 80, 120 |  |
| `Russellschen Trümmer` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 84 |  |
| `Erwachen-Zyklus` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 76 |  |
| `Jenseits des Ereignishorizonts` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 104 |  |
| `Verschränkungs-Inseln` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#2] | 2 | 2 | 102, 104 |  |
| `Entanglement Islands` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#2] | 2 | 2 | 53, 104 |  |
| `Replica Wormholes` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#2] | 2 | 2 | 53, 104 |  |
| `Großen Faktum` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 33 |  |
| `Große Faktum` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 94 |  |
| `Schiffbruch des Denkens` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 84 |  |
| `existenzielle Erschütterung` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 100 |  |
| `Existential Shattering` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 100 |  |
| `Architectural Storytelling` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 76 |  |
| `Integratorin` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#2] | 2 | 2 | 53, 106 |  |
| `Wächter` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#3] | 3 | 4 | 29, 33, 92, 100 | `Wächter-Algorithmen` ×1 |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Korrespondenztheorie` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#5] | 5 | 5 | 29, 31, 92, 126 |  |
| `Kohärenztheorie` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#3] | 3 | 3 | 31, 126 |  |
| `Slingshot-Arguments` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 33 |  |
| `Slingshot-Argument` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 2 | 33, 94 | `Slingshot-Arguments` ×1 |
| `Protokollsatzdebatte` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 29 |  |
| `Konstatierungen` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 29 |  |
| `Schiffsmetapher` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 31 |  |
| `Landauer-Prinzip` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#2] | 2 | 2 | 78, 80 |  |
| `Kachelproblem` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 76 |  |
| `Wang-Kacheln` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 76 |  |
| `Halteproblem` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#2] | 2 | 2 | 55, 76 |  |
| `Gödelsche Unvollständigkeitssatz` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#2] | 2 | 2 | 55, 128 |  |
| `Bekenstein-Schranke` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 61 |  |
| `Hubble-Volumen` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 52 |  |
| `Big Rip` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#2] | 2 | 3 | 52, 60, 114 |  |
| `Big Freeze` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#2] | 2 | 2 | 56, 114 |  |
| `Page-Wootters-Mechanismus` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#2] | 2 | 2 | 112, 116 |  |
| `Wheeler-DeWitt-Gleichung` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 114 |  |
| `Quantenuhr` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 116 |  |
| `Platonia` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 128 |  |
| `Zeitkapseln` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 128 |  |
| `Grenzsituation` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#2] | 2 | 4 | 82, 84 | `Grenzsituationen` ×2 |
| `Grenzsituationen` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#2] | 2 | 2 | 84 |  |
| `Sein zum Tode` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#2] | 2 | 2 | 118, 122 |  |
| `Vorlaufen in den Tod` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 122 |  |
| `Ayin` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#3] | 3 | 3 | 118, 120 |  |
| `Pauli-Ausschlussprinzip` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 59 |  |
| `Zeno-Effekt` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 62 |  |
| `Planck-Skala` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 57 |  |
| `Hawking-Strahlung` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 53 |  |
| `Ultrafinitismus` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 57 |  |
| `Theorem von Paris-Harrington` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 92 |  |
| `Satz von Goodstein` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 92 |  |
| `Peano-Arithmetik` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 92 |  |
| `Polyphonie` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 68 |  |
| `polyphonen Narration` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 68 |  |
| `Mutuale Information` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 106 |  |
| `Meinigkeit` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 39 |  |
| `Epigenetik` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] | 1 | 1 | 98 |  |

## What the extraction ran into

**Zeros:** 0. No candidate stands at zero, so no term was found missing and no list entry was a form the document does not write; the lens forms and the two surfaces `Funktionale Multiplizität` (heading, L64) and `Funktionalen Multiplizität` (inflected, in a sentence, L66) are each written as their lines write them.

**Standing alone less often than with compounds, each read from its lines:**

The document writes the genitive `Kaels` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#14] times, so `Kael` stands 43 times alone and 57 including it. `Juna` stands 11 times alone and once as `Junas` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1]. `Kollaps-Kernel` once alone and once as `Kollaps-Kernels` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1], the genitive on L31. `TSDP` has two compounds on other lines: `TSDP-Typ` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] in a table header cell (L51) and `TSDP-Traumastruktur` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] (L132). The eighth hit for `Lex` is no inflection of the name but the unrelated word `Lexik` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] (L68), so `Lex` stands 7 times as the name. `Wächter` stands 3 times alone and once in `Wächter-Algorithmen` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1]. `Slingshot-Argument` stands once alone (L94) and once inside the genitive `Slingshot-Arguments` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] (L33), which is also a list entry of its own. `Big Rip` stands twice alone and once as `Big Rips` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#1] (L114). `Grenzsituation` stands twice alone and twice as the plural `Grenzsituationen` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#2], which is also a list entry of its own.

**What else the reading met.**

Export artifacts: the profile counts 110 backslash escapes. They are the escaped underscores in file names (`kg\_core.py` style, L21 and L23), and the escaped asterisks that make the table's cells look bold (L51 to L62). Neither touches a candidate. The profile's 38 glued reference numbers are the footnote digits at the end of sentences (for example in the sentence at L19 that names the directory `.claude/`): a digit stands directly after the final period or word. Chapter numbers glued to `Kapitel` are dropped from `--find` output, but they stand in the file. `Kapitel` ^[roman-refactoring-kohaerenz-und-charakterentwicklung.md:#11] stands eleven times.

Aliases: the document writes `Dual-Kernel-Theorie` and then `DKT` once (L27); it writes `Autonomous Entropic Gatekeeper for Integrity Systems` once (L29) and `AEGIS` 41 times; `Tertiären Strukturellen Dissoziation der Persönlichkeit` is followed by `TSDP`, `Phänomenales Selbstmodell` by `PSM`, and the two Anteile families are written out once (L41) and then as `ANPs` and `EPs`. `Anomalie Juna` is the long form of `Juna`; `Nexus` stands once in parentheses after `Überwelt` (L88) and `Guardians` once, where the document in the same sentence names them „personifizierte, engstirnige Algorithmen“ ^[L88]. The document writes `Großen Faktum` (L33, in quotation marks of the document) and `Große Faktum` (L94). The `Integratorin` is the role of `Selene`, written in the table cell and in L106.

The document gives each of the eleven Anteile a row in the matrix (L52 to L62), with a type in parentheses: Kael as „Primärer ANP“ ^[L52], `Argus` as „Emergierender ANP/EP“ ^[L62]; the types are the document's own assignments and no list elsewhere in the document gives them.

Not on the list: the repository names of section 1, the titles of references, and the many bearers of borrowed theory (Russell, Wittgenstein, Davidson, Jaspers, Heidegger, Bachtin, Barbour) as people. Their ideas stand under the lens heading as the document names them; the sentences carry a footnote number that points at the reference list, and so the report of those ideas is the document's report of what its references say.

Own standing: the document describes its own result as „garantiert eine unvergleichliche inhaltliche Kohärenz“ ^[L132] and as a „profundes epistemologisches und psychologisches Meisterwerk“ ^[L132]. That is a claim of the document about its own proposal, recorded and not applied.

**Zeros:** 0.

**Standing alone less often than with compounds:** 9 — `Kollaps-Kernel` 1/2, `Juna` 11/12, `Kael` 43/57, `TSDP` 1/3, `Lex` 7/8, `Wächter` 3/4, `Slingshot-Argument` 1/2, `Big Rip` 2/3, `Grenzsituation` 2/4.
