# Record audit, 2026-09-24 — do the conflict and question records hold what documents 7–13 say?

Asked because the author asked how well reading works. The quotations in
`Wiki/conflicts/` and `Wiki/questions/` are checked mechanically (`quotes.py`),
but **what a record says a document says** was never checked, and neither was
**what a document says that no record holds**. Documents 7–9 were reconciled
before ingest step 6 existed — *read every open conflict and question against
the document* — and document 9's first pass reached none of the six records it
spoke to.

## How it ran

The saved workflow `record-audit`, one agent at a time per role:

1. **One auditor per document** read all twelve conflict records and five
   question records, then the document's reconciliation record. It checked
   **every** statement a record attributes to the document against the lines
   (`faithful` / `distorted` / `unsupported`). Then it read the whole document
   for passages that take a position on a record's subject, relate positions, or
   contradict one, where no record holds that passage. Every line number came
   from `read.py --find`.
2. **Two skeptics per document**, each told to refute and to default to
   refuted when unsure. *Text*: is the quote at the line, and does no record
   or linked page already hold it? *Matters*: is it a position, a relation or a
   contradiction on the record's question, rather than a mention or a
   restatement?

Every auditor read its document to the last line. 21 agents, 3,725,408 subagent
tokens, 65 minutes at two agents at a time. `audit.json` holds every
attribution checked, every finding, both verdicts and the outcome per finding.
The records the auditors read already carried document 14's readings, because
`main` moved while the run was going.

## What it found

| document | attributions checked | faithful | findings | both skeptics upheld | one upheld | neither |
|---|--:|--:|--:|--:|--:|--:|
| 7 `…storyform-und-outline…` | 58 | 54 | 13 | 3 | 5 | 5 |
| 8 `…charakter-bibel…` | 51 | 51 | 16 | 1 | 8 | 7 |
| 9 `…konzept-konsolidiert…` | 68 | 65 | 20 | 4 | 9 | 7 |
| 10 `kapitel-kompendium-…` | 23 | 22 | 3 | 0 | 1 | 2 |
| 11 `…kernwelten-vollstaendig…` | 31 | 28 | 13 | 0 | 4 | 9 |
| 12 `dramatica-…` | 23 | 21 | 6 | 1 | 1 | 4 |
| 13 `…begriffe-und-konzepte…` | 35 | 33 | 12 | 0 | 2 | 10 |
| **all** | **289** | **274 (95 %)** | **83** | **9** | **30** | **44** |

- **What the records attribute is almost always right.** 274 of 289
  statements hold at the lines they cite. Most of the fifteen that do not lose
  something small: a qualifier („in A", „Mnemosyne dominiert klar in KW2"), a
  count (two where there are four), a distance (eleven lines where there are
  thirteen). Two are false about the document outright: that document 7 never
  writes `Wächter`, and that it does not name the outline it overrides.
- **Most of what the auditors called a miss is held elsewhere.** The skeptics
  refuted 44 of 83. The usual reason is that a page the record links already
  quotes the passage from that document, so the record does not repeat it. The
  wiki is the records and the pages together. An auditor that reads only the
  records overcounts what is missing.
- **What is really missing sits where the process was weakest.** Five of the
  nine upheld findings are documents 7–9 missing from records they speak to.
  Those three were read before step 6 existed.

## What was written, and by what rule

**Rule:** a finding goes into a record when both skeptics upheld it, or when
the text skeptic confirmed that the document's own words contradict what a
record says about it: a count, a „never", a file it names, a qualifier it
drops. A statement true in the record's own terms stays, whatever the words
(13-A12). A false statement is a defect whatever its weight, and a record is
append-only, so the correction is a new dated section beside the old one. A
page is corrected in place, with the correction noted beside it. Every citation
comes from `read.py --find`. Each file is its own commit, and the commit names
the source document.

| finding | file | from |
|---|---|---|
| 7-A50, 7-A51, 7-M8 — `Wächter` does occur, in Kap 31's line with `Guardian`; `Wächterin` four times | `Wiki/questions/q4-waechter-four-bearers.md`, `Wiki/candidates/guardians.md` | document 7 |
| 7-M6 — both orders of the Genesis | `Wiki/conflicts/c12-genesis-beats.md` | document 7 |
| 7-A33 — its Quellen-Register names the outline it overrides | `Wiki/conflicts/c11-landauer-warmth-or-cold-ozone.md` | document 7 |
| 8-M2 — AEGIS is the entropy it fights, a month before C2's „first" | `Wiki/conflicts/c2-entropie-sense.md` | document 8 |
| 9-M1 — AEGIS' blindness as a law | `Wiki/conflicts/c4-guardians-and-aegis.md` | document 9 |
| 9-M5 — „die operative Hälfte", in a locked section | `Wiki/conflicts/c3-emergenz-origin.md` | document 9 |
| 9-M12 — both orders of the Genesis | `Wiki/conflicts/c12-genesis-beats.md` | document 9 |
| 9-M16 — `Wächter` beside `Guardian` in Kap 31 | `Wiki/questions/q4-waechter-four-bearers.md` | document 9 |
| 9-A15 — thirteen lines, not eleven | `Wiki/conflicts/c5-garten-scale.md` | document 9 |
| 9-A22 — „nicht je ein Guardian-Reich", and Mnemosyne „dominiert klar in KW2" on the same line | `Wiki/conflicts/c6-guardians-count-and-pairing.md` | document 9 |
| 12-M2 — a Juna-POV row in the routing table | `Wiki/conflicts/c7-juna-first-appearance.md` | document 12 |
| 12-A23 — the objective story „in A" | `Wiki/questions/q1-guardians-and-aegis.md` | document 12 |

The other split findings are in `audit.json` with both reasons, and none was
written: in each, one skeptic showed the point already held, or not on the
record's question, or — 11-A19 — the record's words supported by what they
cite.

## What it does not show

That the records are complete. The auditors checked records, not pages, and
seven documents, not fourteen. And every agent here was Claude, like every
reader before it.
