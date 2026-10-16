---
source: Sources/drive/juna.md
drive_id: "18N07htwP86U6jD1PMVYidcvOITovxjDOAsyyYgUCEWE"
title: "Juna"
category: charaktere
index_date: "2025-07-30"
extracted: "2026-10-14"
candidates: 44    # the terms capture.py counted
---

# Term census — Juna

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py juna`

```
  lines                105  (frontmatter ends at 9)
  body words           2872
  headings             4   bold-only lines 0
  table rows           0   code fences 0
  question marks       0
  backslash escapes    0
  typographic marks    182   ascii quotes 0
  invisible characters none
  math symbol lines    0
  glued ref numbers    0
  repeated labels      none
  longest line         1013 chars
```

## Stance, read per passage

The text is two passes over one outline, each opened in a role voice. The first pass opens with „Als Konzept-Dramaturg ist es meine Aufgabe“ ^[L11] and runs to L52; the second opens with „Als Narrativer Architekt ist es meine vorrangige Aufgabe“ ^[L54] and runs to L104, repeating the sections I (`Das Fundament`, L15 and L60) and II (`Juna/V-Verbindung`, L33 and L81) with additions. Both passes are definitions and design proposals in the register of a plan: each section is labelled `Natur und Definition` `Mechanik und Funktionsweise` `Rolle im Narrativ und Konflikt` and `Vermeidung eines` `Deus ex Machina` (counts in the note). The sections are written as settled statements, with no question marks in the body (profile: 0), and no passage is marked as a lock, a report or a question.

The first pass ends mid-sentence: the last line of it reads „erst vollständig und überzeugend“ ^[L52] and nothing completes it (export or source truncation; the line is the end of the paragraph). The second pass adds a philosophical-influence passage (L66) and physics borrowings (L89, L91), which are the lens candidates, and it states a hedge about `Juna/V`: „Ihre genaue Natur bleibt mysteriös und unklar.“ ^[L85] The bullets under `Vermeidung eines` `Deus ex Machina` are the document's design rules for the two concepts (L29 to L31, L47 to L50, L76 to L79, L101 to L104).

## Candidates and counts

44 candidates, written while reading and frozen by the count (`Plan/runs/juna/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `juna.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Das Fundament` ^[juna.md:#29] | 29 | 29 | 11, 15, 17, 19, 21, 23, 25, 27, 29, 31, 50, 52 … |  |
| `Juna/V-Verbindung` ^[juna.md:#12] | 12 | 12 | 11, 33, 35, 43, 50, 52, 54, 81, 83, 91, 93, 104 |  |
| `Juna/V` ^[juna.md:#27] | 27 | 39 | 11, 33, 35, 37, 39, 43, 45, 47, 48, 49, 50, 52 … | `Juna/V-Verbindung` ×12 |
| `Moonshine-Link` ^[juna.md:#2] | 2 | 5 | 39, 41, 89 | `Moonshine-Links` ×3 |
| `Kael-Juna (K-J) Verbindung` ^[juna.md:#1] | 1 | 1 | 91 |  |
| `Paraiyas` ^[juna.md:#3] | 3 | 3 | 21, 64 |  |
| `Paradoxon X` ^[juna.md:#3] | 3 | 3 | 25, 70, 78 |  |
| `Potentialmeers` ^[juna.md:#2] | 2 | 2 | 37, 85 |  |
| `alternatives Kohärenzprotokoll` ^[juna.md:#2] | 2 | 2 | 37, 85 |  |
| `Kohärenz Protokoll` ^[juna.md:#7] | 7 | 7 | 11, 17, 31, 52, 54, 78, 91 |  |
| `Kernprozessor` ^[juna.md:#2] | 2 | 2 | 43, 95 |  |
| `Kernwelten` ^[juna.md:#1] | 1 | 1 | 97 |  |
| `Kontaktquelle` ^[juna.md:#2] | 2 | 2 | 37, 85 |  |
| `Reboots` ^[juna.md:#1] | 1 | 1 | 104 |  |
| `AEGIS` ^[juna.md:#46] | 46 | 46 | 21, 25, 35, 37, 39, 41, 43, 47, 52, 68, 70, 72 … |  |
| `Kael` ^[juna.md:#22] | 22 | 41 | 23, 25, 29, 30, 31, 39, 43, 48, 52, 68, 70, 72 … | `Kaels` ×18, `Kael-Juna` ×1 |
| `Impact Character (IC)` ^[juna.md:#1] | 1 | 1 | 95 |  |
| `Monster Group (M)` ^[juna.md:#1] | 1 | 1 | 91 |  |
| `Monstrous Moonshine` ^[juna.md:#1] | 1 | 1 | 91 |  |
| `ontologischer Exploit` ^[juna.md:#4] | 4 | 4 | 11, 43, 56, 93 |  |
| `lebendiger Gödel-Satz` ^[juna.md:#2] | 2 | 2 | 43, 93 |  |
| `Gödel-Satz` ^[juna.md:#3] | 3 | 3 | 43, 93 |  |
| `Gödel-Gambit` ^[juna.md:#1] | 1 | 1 | 95 |  |
| `architektonische Hintertür` ^[juna.md:#3] | 3 | 3 | 47, 91, 95 |  |
| `seltsamer Attraktor` ^[juna.md:#3] | 3 | 3 | 23, 68 |  |
| `Anziehungsbecken` ^[juna.md:#2] | 2 | 2 | 23, 68 |  |
| `schwache Emergenz` ^[juna.md:#2] | 2 | 2 | 23, 68 |  |
| `parakonsistenter Rahmen` ^[juna.md:#2] | 2 | 2 | 21, 64 |  |
| `Gnosis` ^[juna.md:#2] | 2 | 2 | 25, 72 |  |
| `Ankerpunkte` ^[juna.md:#1] | 1 | 1 | 104 |  |
| `blindem Fleck` ^[juna.md:#1] | 1 | 1 | 97 |  |
| `Verdiente Einsicht` ^[juna.md:#2] | 2 | 2 | 29, 76 |  |
| `Frühes Foreshadowing` ^[juna.md:#2] | 2 | 2 | 30, 77 |  |
| `Begrenzte Erklärungskraft` ^[juna.md:#2] | 2 | 2 | 31, 78 |  |
| `Deus ex Machina` ^[juna.md:#6] | 6 | 6 | 11, 27, 45, 56, 74, 99 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Quantenverschränkung` ^[juna.md:#2] | 2 | 2 | 41, 89 |  |
| `Prehension` ^[juna.md:#2] | 2 | 2 | 41, 89 |  |
| `Prähension` ^[juna.md:#1] | 1 | 1 | 89 |  |
| `Qualia` ^[juna.md:#3] | 3 | 3 | 41, 91 |  |
| `Advaita Vedanta` ^[juna.md:#1] | 1 | 1 | 66 |  |
| `Madhyamaka Buddhismus` ^[juna.md:#1] | 1 | 1 | 66 |  |
| `Pleroma` ^[juna.md:#1] | 1 | 1 | 66 |  |
| `Yin und Yang` ^[juna.md:#1] | 1 | 1 | 66 |  |
| `Śūnyatā` ^[juna.md:#1] | 1 | 1 | 66 |  |

## What the extraction ran into

**Zeros:** 0. Every candidate was found as written, because each was asked of the text with `read.py --find` before the count.

**Standing alone less often than with compounds:** 3. `Juna/V` stands alone 27 times and 39 times in all: the 12 others are the compound `Juna/V-Verbindung`, which is also a candidate. `Moonshine-Link` stands alone 2 times and 5 in all because the document inflects it as `Moonshine-Links` 3 times (`Moonshine-Links` ^[juna.md:#3]). `Kael` stands alone 22 times and 41 in all: `Kaels` 18 times and `Kael-Juna` once.

**Export artefacts and inflection.** The bold markers sit inside the headings and run-in labels, and the italic `Deus ex Machina` of L11 and L27 sits between asterisks; the count reads the text as it is stored and found the term 6 times. Candidates were listed in the case the document uses: `Potentialmeers` (genitive), `Reboots` (genitive), `blindem Fleck` (dative). A lens term `Prehension` has a second spelling, `Prähension`, at L89. The line numbering shows a frontmatter of 9 lines; the body begins at L10.

**What the document names and does not number.** The document writes no `Kap` and no `Kapitel` (`Kap` ^[juna.md:#0], `Kapitel` ^[juna.md:#0]), so it holds no chapter-level content; it speaks of „im Finale“ ^[L43] and „Im finalen Akt des Romans“ ^[L72] without a number.

**Names of real persons** occur inside the lens passages (L41, L66, L89, L91) and are deliberately not listed as candidates; only the concepts they are named in are, as the document writes them.

**Own standing.** The document claims a standing for its definitions only in a design sense: it calls the two concepts „die transzendenten Pfeiler der Erzählwelt“ ^[L11]. That is recorded as the document's own claim and applied nowhere.

**Zeros:** 0.

**Standing alone less often than with compounds:** 3 — `Juna/V` 27/39, `Moonshine-Link` 2/5, `Kael` 22/41.
