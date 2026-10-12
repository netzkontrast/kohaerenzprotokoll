---
source: Sources/drive/genesis-prosa-ausformulierung-gesamt.md
drive_id: "1W0zbWO6t-CLketv74NiUWfskDJF22-ezncOEjMng8tU"
title: "Genesis - Prosa Ausformulierung (Gesamt)"
category: charaktere
index_date: "2025-04-29"
extracted: "2026-10-12"
candidates: 44    # the terms capture.py counted
---

# Term census — Genesis - Prosa Ausformulierung (Gesamt)

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py genesis-prosa-ausformulierung-gesamt`

```
  lines                315  (frontmatter ends at 9)
  body words           2531
  headings             1   bold-only lines 16
  table rows           0   code fences 0
  question marks       14
  backslash escapes    65
  typographic marks    0   ascii quotes 0
  invisible characters none
  math symbol lines    0
  glued ref numbers    26
  repeated labels      none
  longest line         550 chars
```

## Stance, read per passage

The text is narrative prose, a draft titled „Genesis - Entwurf“ ^[L11], in scenes. It has three parts, headed „DAS ERWACHEN IM RAUSCHEN“ ^[L13], „DIE FESTUNG DER LOGIK“ ^[L75] and „DIE KRISE UND DIE SCHERBEN“ ^[L189], and thirteen scenes, whose headings carry the label `Szene` ^[genesis-prosa-ausformulierung-gesamt.md:#13]. Three scene headings add `NEUE` ^[genesis-prosa-ausformulierung-gesamt.md:#3] (scenes 6, 8 and 10, lines 125, 165, 211). Under each scene heading a line in parentheses gives `Perspektive` ^[genesis-prosa-ausformulierung-gesamt.md:#14] and `Stimmung` ^[genesis-prosa-ausformulierung-gesamt.md:#14], for example „Perspektive: Ich (Kael)“ ^[L292].

Passages in the first-person voice (scenes 1 to 3, L19 to L73) are sensory and unnamed: „Es zerreißt mich.“ ^[L19]. Passages in AEGIS's voice (from scene 4, L91 on) are written as system reports with bracketed identifiers and timestamps, for example „Emergenz der Entität AEGIS bestätigt.“ ^[L97]. From scene 5 the speaker changes within a scene, marked by a parenthesised label line: `(AEGIS)` and `(Ich/Komponente 734)` (L109 to L145 and on). Scene 12 uses `(AEGIS)` and `(Ich)` alternately (L254 to L288). Scene 13 returns to prose in the first person and names Kael: „Kael? Ist das ein Name?“ ^[L296].

The document marks no passage as a plan, lock or question for the reader; the only labels are the scene headings, the mood lines and the speaker labels. Inside the AEGIS passages the text assigns statuses of its own, for example „Klassifizierung: Tolerierter Strukturfehler.“ ^[L123].

## Candidates and counts

44 candidates, written while reading and frozen by the count (`Plan/runs/genesis-prosa-ausformulierung-gesamt/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `genesis-prosa-ausformulierung-gesamt.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `AEGIS` ^[genesis-prosa-ausformulierung-gesamt.md:#42] | 42 | 44 | 75, 77, 79, 89, 97, 99, 103, 107, 109, 121, 127, 129 … | `AEGIS-Architektur` ×1, `AEGIS-Logik` ×1 |
| `Rauschen` ^[genesis-prosa-ausformulierung-gesamt.md:#11] | 11 | 13 | 23, 35, 43, 53, 63, 69, 71, 73, 83, 135, 159, 171 … | `Rauschens` ×2 |
| `Komponente 734` ^[genesis-prosa-ausformulierung-gesamt.md:#34] | 34 | 34 | 105, 107, 111, 113, 123, 127, 131, 133, 141, 143, 149, 153 … |  |
| `Kael` ^[genesis-prosa-ausformulierung-gesamt.md:#4] | 4 | 4 | 290, 292, 296, 302 |  |
| `Überwelt` ^[genesis-prosa-ausformulierung-gesamt.md:#2] | 2 | 5 | 147, 153, 163, 217, 225 | `Überwelt-Subsystem` ×2, `Überwelt-Simulation` ×1 |
| `Überwelt-Subsystem` ^[genesis-prosa-ausformulierung-gesamt.md:#2] | 2 | 2 | 153, 217 |  |
| `Direktive 0` ^[genesis-prosa-ausformulierung-gesamt.md:#6] | 6 | 6 | 99, 123, 163, 225, 244, 248 |  |
| `Omega-Event` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 91 |  |
| `Notfallprotokoll Omega-Rho` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 93 |  |
| `Anomaly-Alpha` ^[genesis-prosa-ausformulierung-gesamt.md:#7] | 7 | 7 | 197, 209, 215, 217, 223, 237, 241 |  |
| `Protokoll Gamma-Exekution` ^[genesis-prosa-ausformulierung-gesamt.md:#3] | 3 | 3 | 248, 256, 288 |  |
| `Protokoll Sigma-Stasis` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 246 |  |
| `Cluster Gamma-Kern` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 111 |  |
| `Echo` ^[genesis-prosa-ausformulierung-gesamt.md:#12] | 12 | 16 | 29, 33, 103, 117, 119, 137, 141, 159, 187, 199, 203, 205 … | `Echos` ×1 |
| `Scherben` ^[genesis-prosa-ausformulierung-gesamt.md:#5] | 5 | 5 | 276, 290, 294, 306, 314 |  |
| `Narbe` ^[genesis-prosa-ausformulierung-gesamt.md:#2] | 2 | 2 | 55, 61 |  |
| `Resonanz` ^[genesis-prosa-ausformulierung-gesamt.md:#8] | 8 | 14 | 35, 39, 95, 171, 191, 199, 209, 215, 233, 242, 264, 288 … | `Resonanzen` ×1, `Resonanzphänomene` ×1, `Resonanzspitze` ×1, `Resonanzverbindung` ×1 |
| `Signatur` ^[genesis-prosa-ausformulierung-gesamt.md:#5] | 5 | 11 | 43, 95, 111, 123, 141, 171, 197, 199, 217, 219 | `Signaturvarianz` ×3, `Signaturen` ×2, `Signaturdaten` ×1 |
| `Kernwelten` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 304 |  |
| `Kernprotokoll` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 99 |  |
| `Systemkohärenz` ^[genesis-prosa-ausformulierung-gesamt.md:#3] | 3 | 3 | 95, 215, 244 |  |
| `Systemintegrität` ^[genesis-prosa-ausformulierung-gesamt.md:#3] | 3 | 3 | 99, 131, 248 |  |
| `Strukturelle Anomalien` ^[genesis-prosa-ausformulierung-gesamt.md:#2] | 2 | 2 | 123, 141 |  |
| `Tolerierter Strukturfehler` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 123 |  |
| `734-Sigma-Echo` ^[genesis-prosa-ausformulierung-gesamt.md:#2] | 2 | 2 | 141, 199 |  |
| `Simulation Epsilon-7` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 153 |  |
| `Simulation Epsilon-Prime` ^[genesis-prosa-ausformulierung-gesamt.md:#3] | 3 | 3 | 171, 181, 183 |  |
| `Simulation Omega-Prime` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 219 |  |
| `Gamma-Phi` ^[genesis-prosa-ausformulierung-gesamt.md:#2] | 2 | 2 | 181, 183 |  |
| `Sektor Delta-9` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 197 |  |
| `Diagnosezyklus Delta-Gamma` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 131 |  |
| `Netzwerk-Segment Gamma` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 256 |  |
| `Quanten-Interferenz-Disruptoren` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 264 |  |
| `Alarmstufe Rot` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 215 |  |
| `Subjektive Residuen` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 103 |  |
| `Latente Datenpunkte` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 103 |  |
| `Mahlstrom` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 31 |  |
| `entropische Flut` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 25 |  |
| `Abwehr des Nicht-Seins` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 99 |  |
| `Geist in der Maschine` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 304 |  |
| `Wir` ^[genesis-prosa-ausformulierung-gesamt.md:#6] | 6 | 7 | 21, 67, 69, 71, 73, 87 |  |
| `Kern` ^[genesis-prosa-ausformulierung-gesamt.md:#5] | 5 | 12 | 49, 67, 69, 99, 111, 125, 131, 199, 221, 280, 302, 304 | `Kernprotokoll` ×1, `Kernkomponenten` ×1, `Kernfrequenz` ×1, `Kernalgorithmen` ×1 |
| `Inseln` ^[genesis-prosa-ausformulierung-gesamt.md:#1] | 1 | 1 | 73 |  |
| `Welle` ^[genesis-prosa-ausformulierung-gesamt.md:#5] | 5 | 6 | 43, 55, 81, 91, 197, 203 |  |

## What the extraction ran into

**Zeros:** 0.

**Standing alone less often than with compounds:** 9 — `AEGIS` 42/44, `Rauschen` 11/13, `Überwelt` 2/5, `Echo` 12/16, `Resonanz` 8/14, `Signatur` 5/11, `Wir` 6/7, `Kern` 5/12, `Welle` 5/6.

There are no zeros: every candidate stands in the form listed. The nine rows with a lower stand-alone count are compounds and inflections, read in the surfaces column: `AEGIS-Architektur` and `AEGIS-Logik` for AEGIS, the genitive `Rauschens` for Rauschen, `Überwelt-Subsystem` and `Überwelt-Simulation` for Überwelt, `Echos`, `Resonanzspitze`, `Signaturvarianz` and `Kernfrequenz` and similar for the others. `Kern` is a substring of `Kernwelten`, `Kernprotokoll` and further compounds; `Wir` stands in a speech-like fragment in single quotes in the scene 3 and 4 passages and elsewhere as an ordinary pronoun, so the term and the pronoun are not separable by count.

The export left 65 backslash escapes: `\!`, `\[`, `\]`, `\-\>` and `\<-\>` in the mood lines and in the system reports. Bracketed fields in AEGIS's reports hold placeholders such as `[Zeitstempel]` and `[Wert]` and identifiers such as `[ID: Omega-Event]`; the identifiers are listed as candidates in the form the line writes them, without the brackets. The profile counts 26 glued reference numbers (the profile's figure, not read line by line here). Quoted headings drop glued digits in the quotation check, so the heading „DAS ERWACHEN IM RAUSCHEN“ ^[L13] is quoted without its part number.

Two candidates are formed by the document as designations of one thing: `Komponente 734` is introduced as the new designation of the entity formerly called `Cluster Gamma-Kern`, in the text „Neue Designierung: Komponente 734.“ ^[L111]. The text never writes a subscripted form of any term. The closing words of the last scene give `Kael` as a name for what remains of that component; the first-person voice questions it: „Kael? Ist das ein Name?“ ^[L296].

The document says nothing about its own standing (no canon, draft or lock claim beyond the title „Genesis - Entwurf“ ^[L11]).
