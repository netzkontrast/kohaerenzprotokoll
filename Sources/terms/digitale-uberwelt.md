---
source: Sources/drive/digitale-uberwelt.md
drive_id: "1Usb1RG3BLznSWqnCTKyzBMIQs94trNiHZPTBKBcOXjA"
title: "Digitale Überwelt"
category: worldbuilding
index_date: "2025-04-17"
extracted: "2026-10-19"
candidates: 70    # the terms capture.py counted
---

# Term census — Digitale Überwelt

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py digitale-uberwelt`

```
  lines                195  (frontmatter ends at 9)
  body words           8487
  headings             4   bold-only lines 7
  table rows           0   code fences 0
  question marks       39
  backslash escapes    545
  typographic marks    16   ascii quotes 190
  invisible characters none
  math symbol lines    0
  glued ref numbers    173
  repeated labels      none
  longest line         35626 chars
```

## Stance, read per passage

The document is a concept draft in four voices, each with its own label. Observed: sections II to V are not headed in the export; their headings (`II.`, `III.`, `IV.`, `V.`) run into the single long line 49 as `\#\#` markup, so the passage boundaries below are read from the text, not from the headings.

**Einleitung (L13 to L21).** A statement of purpose with four bold labels: „Zweck:“ ^[L15], „Grundlage:“ ^[L17], „Ansatz:“ ^[L19] and „Narrative Signifikanz:“ ^[L21]. It frames the Überwelt as „eine rein informationsbasierte Realität, die durch das AEGIS-Protokoll reguliert wird“ ^[L15] and calls the given protocol and guardian descriptions „das unveränderliche Regelwerk“ ^[L17]. That is a standing claim the document makes for its inputs; it is recorded here and applied to nothing.

**Guardian-Interface-Protokolle (L23 to L49, first part).** A proposal in a design voice: „Kernherausforderung:“ ^[L25] and then bulleted mechanisms. Where it is not describing a fixed rule it proposes, e.g. „Konsensfindung oder Konfliktlösung erfolgen ohne Vertrauen und direkte Verhandlung“ ^[L40]. Protocol claims carry a bracketed source marker, `Kontext 1` ^[digitale-uberwelt.md:#34] times and `Kontext 2` ^[digitale-uberwelt.md:#3] times; the marker points to material the document does not reproduce, so the claim it follows is the document's report of that material.

**III. Recherche (inside L49).** A report on comparable fictional and theoretical systems, closed by a comparison table (`Tabelle III.1`) that the export flattened into the same line. The works and sources named there are cited material, not terms of the world.

**IV. Konzept (inside L49).** The narrative and sensory design of the Überwelt in a descriptive-normative voice, with sub-labels such as `Existenz/Form:`, and a conditional register (`könnte`, `vielleicht`) for visual choices and a declarative one for AEGIS, e.g. „AEGIS hat keinen Ort.“ ^[L49].

**V. Kritische Überprüfung (end of L49 to L89).** The document reviews itself: gaps, possible contradictions and underdeveloped aspects are listed as questions, e.g. „sind noch nicht detailliert genug beschrieben“ ^[L71], followed by „Neue, weiterführende Recherchefragen:“ ^[L75] and „Zusätzliche Recherche (Synthese relevanter Erkenntnisse):“ ^[L83]. Terms that stand only inside these questions are the term as an open question, not a reading.

**Finaler Entwurf (L91 to L108).** A revision marked `Verfeinert` ^[digitale-uberwelt.md:#8] times that answers the questions of V section by section, headed „Finaler Entwurf (Integration der Erkenntnisse):“ ^[L91]. The closing line claims of the whole: „Dieses vervollständigte Konzept bietet eine detaillierte und kohärente Grundlage“ ^[L110]. That is the document's own judgement of its standing and is recorded, not applied.

**Referenzen (L112 to L194).** A numbered list of web sources with access dates; the reference numbers are glued to the preceding words throughout the body as dropped superscripts.

## Candidates and counts

70 candidates, written while reading and frozen by the count (`Plan/runs/digitale-uberwelt/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `digitale-uberwelt.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Digitale Überwelt` ^[digitale-uberwelt.md:#1] | 1 | 1 | 15 |  |
| `Überwelt` ^[digitale-uberwelt.md:#40] | 40 | 41 | 11, 15, 21, 49, 72, 101, 106, 108, 110 | `Überwelt-Struktur` ×1 |
| `Digitalen Überwelt` ^[digitale-uberwelt.md:#2] | 2 | 2 | 11, 110 |  |
| `AEGIS` ^[digitale-uberwelt.md:#84] | 84 | 109 | 15, 17, 25, 29, 36, 40, 44, 45, 47, 49, 62, 63 … | `AEGIS-Protokoll` ×5, `AEGIS-Protokolls` ×4, `AEGIS-Protokollen` ×2, `AEGIS-Parameter` ×1 |
| `AEGIS-Protokoll` ^[digitale-uberwelt.md:#5] | 5 | 12 | 15, 29, 49, 62, 106, 110 | `AEGIS-Protokolls` ×4, `AEGIS-Protokollen` ×2, `AEGIS-Protokolle` ×1 |
| `AEGIS Functional Protocol v1.4` ^[digitale-uberwelt.md:#1] | 1 | 1 | 17 |  |
| `Guardians` ^[digitale-uberwelt.md:#49] | 49 | 49 | 15, 17, 21, 29, 30, 36, 44, 49, 54, 71, 79, 81 … |  |
| `Guardian` ^[digitale-uberwelt.md:#13] | 13 | 79 | 15, 17, 21, 23, 27, 29, 30, 36, 44, 47, 49, 54 … | `Guardians` ×49, `Guardian-Interface-Protokolle` ×2, `Guardian-Interaktionen` ×2, `Guardian-Manifestation` ×2 |
| `Wächter-Konstrukte` ^[digitale-uberwelt.md:#1] | 1 | 1 | 15 |  |
| `LogOS` ^[digitale-uberwelt.md:#20] | 20 | 20 | 17, 29, 30, 34, 36, 45, 49, 99 |  |
| `Mnemosyne` ^[digitale-uberwelt.md:#14] | 14 | 18 | 17, 30, 35, 49, 54, 63, 73, 80, 88, 98, 103 | `Mnemosynes` ×4 |
| `Cerberus` ^[digitale-uberwelt.md:#15] | 15 | 15 | 17, 29, 34, 49, 103 |  |
| `Kairos` ^[digitale-uberwelt.md:#17] | 17 | 17 | 17, 36, 45, 49, 62, 99, 105 |  |
| `Sophia` ^[digitale-uberwelt.md:#7] | 7 | 9 | 17, 35, 49, 98 | `Sophias` ×2 |
| `Guardian-Interface-Protokolle` ^[digitale-uberwelt.md:#2] | 2 | 2 | 23, 95 |  |
| `Zero-Trust Execution Model (ZTEM)` ^[digitale-uberwelt.md:#2] | 2 | 2 | 25, 49 |  |
| `Zero-Trust Execution Model` ^[digitale-uberwelt.md:#2] | 2 | 2 | 25, 49 |  |
| `ZTEM` ^[digitale-uberwelt.md:#8] | 8 | 13 | 25, 27, 49, 54 | `ZTEM-Konformität` ×1, `ZTEM-Prüfungen` ×1, `ZTEM-Regeln` ×1, `ZTEM-Auswirkung` ×1 |
| `Zero-Trust` ^[digitale-uberwelt.md:#8] | 8 | 10 | 25, 29, 40, 45, 49, 77, 81, 154, 155 | `Zero-Trust-Modell` ×1, `Zero-Trust-Bedingungen` ×1 |
| `Zero-Trust Dynamik` ^[digitale-uberwelt.md:#1] | 1 | 1 | 40 |  |
| `Behavioral Proof-of-Function (BPoF)` ^[digitale-uberwelt.md:#2] | 2 | 2 | 29, 97 |  |
| `Behavioral Proof-of-Function` ^[digitale-uberwelt.md:#3] | 3 | 3 | 29, 49, 97 |  |
| `BPoF` ^[digitale-uberwelt.md:#21] | 21 | 24 | 29, 44, 49, 85, 87, 97, 103 | `BPoF-Prinzip` ×1, `BPoF-Zugriffsvergabe` ×1, `BPoF-Prüfungen` ×1 |
| `Encrypted Intent Channels (EIC)` ^[digitale-uberwelt.md:#2] | 2 | 2 | 30, 98 |  |
| `Encrypted Intent Channels` ^[digitale-uberwelt.md:#3] | 3 | 3 | 30, 98 |  |
| `EIC` ^[digitale-uberwelt.md:#3] | 3 | 11 | 30, 36, 44, 49, 98 |  |
| `EICs` ^[digitale-uberwelt.md:#6] | 6 | 6 | 36, 44, 49 |  |
| `Consensus Enforcer` ^[digitale-uberwelt.md:#6] | 6 | 10 | 45, 49, 85, 86, 97, 99 |  |
| `Integrity Guardian` ^[digitale-uberwelt.md:#10] | 10 | 10 | 44, 49, 62, 105 |  |
| `Cognitive Firewall` ^[digitale-uberwelt.md:#8] | 8 | 8 | 49, 62, 104, 105 |  |
| `Real-time Self-Verification (RTSV)` ^[digitale-uberwelt.md:#1] | 1 | 1 | 49 |  |
| `Real-time Self-Verification` ^[digitale-uberwelt.md:#1] | 1 | 1 | 49 |  |
| `RTSV` ^[digitale-uberwelt.md:#12] | 12 | 13 | 49, 87, 103 | `RTSV-Fehler` ×1 |
| `Secure Isolation State (SIS)` ^[digitale-uberwelt.md:#4] | 4 | 4 | 49, 71, 107 |  |
| `Secure Isolation State` ^[digitale-uberwelt.md:#4] | 4 | 4 | 49, 71, 107 |  |
| `SIS` ^[digitale-uberwelt.md:#10] | 10 | 13 | 49, 71, 104, 107 |  |
| `Externe Ebene` ^[digitale-uberwelt.md:#8] | 8 | 8 | 49, 72, 108 |  |
| `Externen Ebene` ^[digitale-uberwelt.md:#8] | 8 | 8 | 21, 49, 53, 72, 106, 108 |  |
| `Risse` ^[digitale-uberwelt.md:#9] | 9 | 9 | 49, 53, 104, 106 |  |
| `Systeminstabilität` ^[digitale-uberwelt.md:#2] | 2 | 3 | 49, 106 | `Systeminstabilitäten` ×1 |
| `Systemkohärenz` ^[digitale-uberwelt.md:#8] | 8 | 11 | 40, 44, 49, 85, 97, 105 | `Systemkohärenzmetriken` ×1, `Systemkohärenz-Notwendigkeiten` ×1, `Systemkohärenzmetrik` ×1 |
| `Kern-Welten` ^[digitale-uberwelt.md:#2] | 2 | 2 | 49 |  |
| `simulierten Kern-Welten` ^[digitale-uberwelt.md:#2] | 2 | 2 | 49 |  |
| `simulierten Welten` ^[digitale-uberwelt.md:#3] | 3 | 3 | 35, 49, 88 |  |
| `Hypervisor-Schicht` ^[digitale-uberwelt.md:#1] | 1 | 1 | 49 |  |
| `Funktionale Zonen` ^[digitale-uberwelt.md:#1] | 1 | 1 | 49 |  |
| `Mnemosynes Archive` ^[digitale-uberwelt.md:#1] | 1 | 1 | 49 |  |
| `LogOS' Analysekerne` ^[digitale-uberwelt.md:#1] | 1 | 1 | 49 |  |
| `Cerberus' Grenzknoten` ^[digitale-uberwelt.md:#1] | 1 | 1 | 49 |  |
| `Kairos' Potenzialfelder` ^[digitale-uberwelt.md:#1] | 1 | 1 | 49 |  |
| `Sophias Synthese-Hubs` ^[digitale-uberwelt.md:#1] | 1 | 1 | 49 |  |
| `Potenzialfelder` ^[digitale-uberwelt.md:#1] | 1 | 2 | 49, 105 | `Potenzialfeldern` ×1 |
| `Nullraum` ^[digitale-uberwelt.md:#1] | 1 | 1 | 49 |  |
| `Umgebungsordnung` ^[digitale-uberwelt.md:#1] | 1 | 1 | 49 |  |
| `Protokolldurchsetzung` ^[digitale-uberwelt.md:#2] | 2 | 2 | 49 |  |
| `Protokollausführung` ^[digitale-uberwelt.md:#2] | 2 | 2 | 49 |  |
| `Guardian-Manifestation` ^[digitale-uberwelt.md:#2] | 2 | 3 | 49, 99, 103 | `Guardian-Manifestationen` ×1 |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Zero Trust Architecture (ZTA)` ^[digitale-uberwelt.md:#2] | 2 | 2 | 49 |  |
| `ZTA` ^[digitale-uberwelt.md:#7] | 7 | 7 | 49, 81, 89 |  |
| `Self-Sovereign Identity (SSI)` ^[digitale-uberwelt.md:#3] | 3 | 3 | 49, 155, 160 |  |
| `SSI` ^[digitale-uberwelt.md:#7] | 7 | 9 | 49, 81, 89, 155, 157, 160 |  |
| `Kybernetik` ^[digitale-uberwelt.md:#3] | 3 | 3 | 49 |  |
| `Spieltheorie` ^[digitale-uberwelt.md:#3] | 3 | 3 | 77, 85 |  |
| `Nash-Gleichgewicht` ^[digitale-uberwelt.md:#1] | 1 | 1 | 85 |  |
| `Mechanism Design` ^[digitale-uberwelt.md:#1] | 1 | 1 | 85 |  |
| `Linked Views` ^[digitale-uberwelt.md:#1] | 1 | 1 | 86 |  |
| `DNSSEC` ^[digitale-uberwelt.md:#8] | 8 | 8 | 49, 89, 145, 146, 192 |  |
| `RPKI` ^[digitale-uberwelt.md:#9] | 9 | 9 | 49, 89, 148, 149, 193, 194 |  |
| `C2PA` ^[digitale-uberwelt.md:#5] | 5 | 6 | 49, 152, 153 | `C2PA_Specification` ×1 |
| `S/MIME` ^[digitale-uberwelt.md:#4] | 4 | 4 | 49, 150, 151 |  |

## What the extraction ran into

**Zeros:** none; the draft lists 0 and every candidate was tested for standing alone before the count.

**Standing alone less often than with compounds:** these are German compounding and inflection, not absences. `AEGIS` stands alone 84 times and 109 in all because of `AEGIS-Protokoll` and `AEGIS-Parameter`; `Guardian` stands alone 13 times against 79 in all because `Guardians` (49) contains it as a prefix; `EIC` stands alone 3 times against 11 in all, the rest being `EICs`; `Mnemosyne` and `Sophia` gain genitive forms (`Mnemosynes`, `Sophias`); `ZTEM`, `BPoF`, `RTSV` and `SIS` gain hyphen compounds such as `ZTEM-Prüfungen`; the other rows of the fact line are of the same kind.

**One line holds most of the document.** Line 49 is about 36000 characters: the export flattened sections II to V, including a table and bullet lists, into a single paragraph with escaped markdown (`\*`, `\#\#`). Almost every term therefore reports line 49. The long line is export damage, not one passage; the passage boundaries above are read from the text.

**Export artifacts.** The profile counts 545 backslash escapes and 173 numbers glued to words (dropped footnote superscripts), so a quotation cannot start with a reference number and the formulas in `$ … $` are left unlisted. The state variable of AEGIS is written in escaped formula markup and has no clean surface.

**Overlapping rows.** `Behavioral Proof-of-Function (BPoF)` and `Behavioral Proof-of-Function` are listed both, as the document joins a name and its acronym; the same holds for the other expanded acronyms. They count separately because they stand on different lines (for instance 2 against 3 for the BPoF pair).

**Names the document does not write.** The document writes none of `Kael` ^[digitale-uberwelt.md:#0], `Juna` ^[digitale-uberwelt.md:#0], `Nyx` ^[digitale-uberwelt.md:#0], nor `Kap` ^[digitale-uberwelt.md:#0] for a chapter, nor `Kernwelt` ^[digitale-uberwelt.md:#0]; it writes `Kern-Welten` ^[digitale-uberwelt.md:#2] twice, once as „simulierten Kern-Welten“ ^[L49]. These are not candidates; the zeros are recorded here as absences of the document.

**Earlier name.** An earlier name of a figure stands at two lines (L53 and L106) in the review and the revision; it is not listed, quoted or harvested.

**Standing claims.** The document calls its input „das unveränderliche Regelwerk“ ^[L17] and its result „eine detaillierte und kohärente Grundlage“ ^[L110]. Both are recorded as the document's claims and decide nothing.

**Bracketed markers.** `Kontext 1` and `Kontext 2` are source markers of the draft, not terms; they are not on the candidate list.

**Zeros:** 0.

**Standing alone less often than with compounds:** 19 — `Überwelt` 40/41, `AEGIS` 84/109, `AEGIS-Protokoll` 5/12, `Guardian` 13/79, `Mnemosyne` 14/18, `Sophia` 7/9, `ZTEM` 8/13, `Zero-Trust` 8/10, `BPoF` 21/24, `EIC` 3/11, `Consensus Enforcer` 6/10, `RTSV` 12/13, `SIS` 10/13, `Systeminstabilität` 2/3, `Systemkohärenz` 8/11, `Potenzialfelder` 1/2, `Guardian-Manifestation` 2/3, `SSI` 7/9, `C2PA` 5/6.
