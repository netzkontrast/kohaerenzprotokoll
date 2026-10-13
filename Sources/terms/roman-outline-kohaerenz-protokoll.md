---
source: Sources/drive/roman-outline-kohaerenz-protokoll.md
drive_id: "1UBVbKlmaAY9o-yUQfWt_Pek4GAIqZbC4tr8z1JbOWHU"
title: "Roman-Outline: Kohärenz Protokoll"
category: plot-outline
index_date: "2026-02-25"
extracted: "2026-10-12"
candidates: 71    # the terms capture.py counted
---

# Term census — Roman-Outline: Kohärenz Protokoll

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py roman-outline-kohaerenz-protokoll`

```
  lines                114  (frontmatter ends at 9)
  body words           691
  headings             3   bold-only lines 0
  table rows           0   code fences 0
  question marks       0
  backslash escapes    0
  typographic marks    14   ascii quotes 0
  invisible characters none
  math symbol lines    0
  glued ref numbers    3
  repeated labels      none
  longest line         245 chars
```

## Stance, read per passage

The document is a plan: an outline that announces itself as „ein detaillierter Entwurf für den Roman in 3 Teilen und 39 Kapiteln“ ^[L11]. The opening sentence says what it rests on: „Basierend auf dem“ ^[L11] a cited master outline and „begleitenden technischen Dossiers“ ^[L11]; those two texts are the document's report of its basis, not text it contains. L13 is the document's own statement of the model the novel follows, from three stages: „Erfahrung des Horrors“ ^[L13], „Erkenntnis der Systemik“ ^[L13] and „existenziellen Fusion“ ^[L13].

Each of the three parts has a heading and one label line. The headings give the chapter range of the part: „Teil I: Die Ästhetik des Unerklärlichen (Kapitel 1–13)“ ^[L17], „Teil II: Die Erkenntnis der Systemik (Kapitel 14–26)“ ^[L53] and „Teil III: Die existenzielle Fusion (Kapitel 27–39)“ ^[L85]. The label line under each uses the same two fields, `Genre-Fokus` ^[roman-outline-kohaerenz-protokoll.md:#3] and `Thema` ^[roman-outline-kohaerenz-protokoll.md:#3]: „Genre-Fokus: Hard Sci-Fi Horror / Mystery.“ ^[L19], „Genre-Fokus: Technothriller / Epistemologische Sci-Fi.“ ^[L55] and „Genre-Fokus: Metaphysische Sci-Fi / Posthumanismus.“ ^[L87]. These are template fields, not terms.

Under each part stand 13 numbered chapter entries, each a bold title, a colon and a one-sentence plan, for example „Kael erwacht in der Konstrukt-Stadt“ ^[L25] (Part I, first entry) and „Die Enthüllung des eigentlichen Ziels von AEGIS“ ^[L82] (Part II, twelfth entry). The entries are written in the present tense as what happens; none is marked as a question, a lock or a report. Some entries name a frame in parentheses, such as „Mengen-Paradoxon“ ^[L40]; the parenthesis is the document's pointer to a borrowed concept, which the list gives under lens.

The last entry is written as a report inside the plan: „Statusbericht: Zielkohärenz erreicht“ ^[L113], described as „Ein finaler Systembericht von AEGIS mit veränderten Parametern.“ ^[L113]. That report is a chapter title within the outline, not a status of the outline itself.

## Candidates and counts

71 candidates, written while reading and frozen by the count (`Plan/runs/roman-outline-kohaerenz-protokoll/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `roman-outline-kohaerenz-protokoll.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Kael` ^[roman-outline-kohaerenz-protokoll.md:#15] | 15 | 17 | 25, 27, 30, 40, 47, 59, 62, 64, 69, 73, 75, 80 … | `Kaels` ×2 |
| `Juna` ^[roman-outline-kohaerenz-protokoll.md:#6] | 6 | 8 | 28, 73, 83, 96, 106, 112 | `Junas` ×2 |
| `AEGIS` ^[roman-outline-kohaerenz-protokoll.md:#8] | 8 | 8 | 33, 59, 71, 82, 101, 106, 112, 113 |  |
| `Konstrukt-Stadt` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 25 |  |
| `Stadt` ^[roman-outline-kohaerenz-protokoll.md:#5] | 5 | 10 | 25, 27, 28, 30, 35, 60, 64, 69, 75, 96 | `Stadtstruktur` ×2, `Stadtviertel` ×1, `Stadt-Erscheinung` ×1 |
| `Mosaik-Herz` ^[roman-outline-kohaerenz-protokoll.md:#2] | 2 | 2 | 83, 106 |  |
| `PSM` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 49 |  |
| `Phänomenales Selbstmodell` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 49 |  |
| `PSM (Phänomenales Selbstmodell)` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 49 |  |
| `Technischen Dossiers` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 59 |  |
| `Protokoll` ^[roman-outline-kohaerenz-protokoll.md:#2] | 2 | 3 | 11, 82, 109 | `Protokolls` ×1 |
| `Kohärenz` ^[roman-outline-kohaerenz-protokoll.md:#4] | 4 | 4 | 11, 82, 101, 112 |  |
| `Membran` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 96 |  |
| `Rauschen` ^[roman-outline-kohaerenz-protokoll.md:#2] | 2 | 2 | 33, 101 |  |
| `Konstrukt` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 4 | 25, 42, 45, 78 | `Konstrukt-Stadt` ×1, `Konstruktion` ×1, `Konstrukts` ×1 |
| `Der Erwachen-Zyklus` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 25 |  |
| `Geometrie der Isolation` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 27 |  |
| `Das flüchtige Echo` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 28 |  |
| `Die unentscheidbare Zone` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 30 |  |
| `Das Rauschen von AEGIS` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 33 |  |
| `Sprachliche Schatten` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 35 |  |
| `Der Riss im Kontinuum` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 38 |  |
| `Russellsche Trümmer` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 40 |  |
| `Phantomschmerz der Identität` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 42 |  |
| `Gravitationsanomalien` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 45 |  |
| `Grenzsituationen` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 47 |  |
| `Der blinde Fleck des Selbst` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 49 |  |
| `Der erste Zusammenbruch` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 51 |  |
| `Das Archiv der Grenzen` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 59 |  |
| `Turing-Mechanik` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 60 |  |
| `Die Diktatur der Komplexität` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 62 |  |
| `Phaenomena` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 64 |  |
| `Noumena` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 64 |  |
| `Das Qualia-Informationsparadox` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 67 |  |
| `Chaitins Konstante` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 69 |  |
| `Schwarze Löcher der Information` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 71 |  |
| `Das konstruierte Narrativ` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 73 |  |
| `Die Planck-Barriere` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 75 |  |
| `Symmetriebruch` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 78 |  |
| `Epigenetische Geister` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 80 |  |
| `Das Protokoll der Kohärenz` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 82 |  |
| `Junas Demaskierung` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 83 |  |
| `Der Sprung ins Nichts` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 91 |  |
| `Sein zum Tode` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 94 |  |
| `Die Auflösung der Membran` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 96 |  |
| `Der Schiffbruch des Denkens` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 99 |  |
| `Entropische Akzeptanz` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 101 |  |
| `Die Chiffren der Realität` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 102 |  |
| `Jenseits des Ereignishorizonts` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 104 |  |
| `Das Mosaik-Herz` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 106 |  |
| `Das Ende der Subjekt-Objekt-Spaltung` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 107 |  |
| `Der Spiegel-Effekt` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 109 |  |
| `Das absolute Limit` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 110 |  |
| `Fusion der Ebenen` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 112 |  |
| `Statusbericht` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 113 |  |
| `Zielkohärenz` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 113 |  |
| `Erfahrung des Horrors` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 13 |  |
| `Erkenntnis der Systemik` ^[roman-outline-kohaerenz-protokoll.md:#2] | 2 | 2 | 13, 53 |  |
| `existenziellen Fusion` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 13 |  |
| `Hard Sci-Fi Horror` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 19 |  |
| `Technothriller` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 55 |  |
| `Metaphysische Sci-Fi` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 87 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Unvollständigkeit` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 30 |  |
| `Grenze des Sagbaren` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 35 |  |
| `Mengen-Paradoxon` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 40 |  |
| `Halteproblem` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 60 |  |
| `universelle Turingmaschine` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 60 |  |
| `Ding an sich` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 64 |  |
| `Kontingenz` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 91 |  |
| `Entropie` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 87 |  |
| `Transzendenz` ^[roman-outline-kohaerenz-protokoll.md:#1] | 1 | 1 | 99 |  |

## What the extraction ran into

**Zeros:** 0.

**Standing alone less often than with compounds:** 5 — `Kael` 15/17, `Juna` 6/8, `Stadt` 5/10, `Protokoll` 2/3, `Konstrukt` 1/4.

There is no zero: every listed form stands in the text as written. The five rows where the standing-alone figure is below the compound figure are inflections and compounds. `Kael` and `Juna` carry the genitive in `Kaels` and `Junas` (twice each, the surfaces column). `Stadt` is also inside `Stadtstruktur`, `Stadtviertel` and `Stadt-Erscheinung`. `Protokoll` stands in the genitive once as `Protokolls` (L109). `Konstrukt` stands once alone (L78) and inside `Konstrukt-Stadt`, `Konstruktion` and `Konstrukts`; only the last is the same word.

The numbered lists restart at 1 in each part, because the export numbers each list from 1. The chapter numbers of the document therefore stand only in the part headings (`Kapitel` ^[roman-outline-kohaerenz-protokoll.md:#3]; the word `Kap` ^[roman-outline-kohaerenz-protokoll.md:#0] stands nowhere), and a chapter's global number is inferred from its position: each part holds 13 entries, matching the ranges 1–13, 14–26 and 27–39 in L17, L53 and L85. The three part headings begin with the export's „-----“ after an escaped dash; this is damage, not text.

The stray `+1` ^[roman-outline-kohaerenz-protokoll.md:#8] stands on 8 lines, either alone (L21) or indented under an entry (for example L31); it belongs to no sentence and is export damage. Ten entries end with a space before the full stop (L40, L60, L62, L67, L69, L71, L78, L94, L102, L104), the place where a footnote number was probably dropped; the profile reports 3 glued reference numbers, and I did not locate them in the body.

Chapter titles are listed as the document sets them in bold. Two titles hold a name in front of the title proper (`Juna: Das flüchtige Echo` at L28 and `Statusbericht: Zielkohärenz erreicht` at L113); the whole form holds a colon, so the list gives the parts `Das flüchtige Echo`, `Statusbericht` and `Zielkohärenz` and the name `Juna` separately. `Phaenomena vs. Noumena` (L64) holds an abbreviation point and is listed as its two names. The title of the master outline in L11 is a cited work and is not listed. `PSM (Phänomenales Selbstmodell)` is written plain in L49 and is listed joined and as each half. `Technischen Dossiers` stands in quotation marks in L59, glossed there as the internal handbook of the system; the lower-case „technischen Dossiers“ ^[L11] in L11 is the document's reference to the companion texts of its basis.

The document makes no claim about its own standing as canon: it calls itself a draft („Entwurf“ ^[L11]) built on other texts, and nothing in it is marked as locked or decided.
