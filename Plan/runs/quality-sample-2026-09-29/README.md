# Quality sample — documents 32–51, 2026-09-29

On the author's „Bitte prüfe auch die Qualität stichprobenartig". How much of
what the last twenty runs wrote onto the wiki holds against the source lines
**after** the session's review had already corrected what it caught.

| file | what |
|---|---|
| `frame.py` | the frame and the sample: every reading section, record entry, chapter and overview reading documents 32–51 added, split into claims (a paragraph or bullet); 3 term, 1 record, 1 chapter, 1 overview and 1 uncited claim per document where they exist; seed 20260929 |
| `frame.json`, `sample.jsonl` | 3,603 claims (1,598 term, 330 record, 1,520 chapter, 155 overview; 254 uncited); 119 sampled |
| `packets/S001–S119.md` | each sampled claim with its cited lines ±1, read by code |
| `verdicts-1…3.jsonl` | three Sonnet auditors, 40, 40 and 39 claims: OK, MINOR or DEFECT, with evidence |

## Result

**87 OK, 21 MINOR, 11 DEFECT of 119 claims.** Every DEFECT was re-checked by the
session against the source lines, and all 11 held. In two cases the defect was
narrower than the auditor said:

- S073: the day count was wrong, and so was an uncited comparison. The auditor's
  reading of the konsolidiertes Konzept was not the error.
- S114: the count was wrong. The auditor's „at least ten" counted the file's
  duplicated reports twice.

All 11 are corrected, one commit per page naming the document.

| kind | OK | MINOR | DEFECT |
|---|--:|--:|--:|
| term page | 39 | 16 | 8 |
| record | 13 | 3 | 3 |
| chapter | 18 | 0 | 0 |
| overview (`plot.md`) | 17 | 2 | 0 |

**What the defects are.**

- **Support: 7.** The prose says more than, or other than, the cited line:
  - a Beat number wrong twice;
  - a plural read as a singular;
  - a self-description misread;
  - a Lücken-Analyse credited with a gap it does not name;
  - a figure left out;
  - Guardians named where the document writes only „Carrier".
- **Scope: 2.** A comparison with other documents that no quotation carried:
  „every later source", „the only one", „the oldest read source".
- **Count: 2.** „Four to three alters per world" where the table gives two to
  three; „six sections" with seven listed and eight standing.

**None of the 11 is visible to `quotes.py`.** Every quotation in them resolves.
Wording checks cannot find these defects; reading or the new flags can.

**The 21 MINOR are mostly uncited comparisons (13).** `lint_readings.py` flags
that class now. Two of its phrases, „every later source" and „the oldest read
source", passed its first patterns, and this sample is why they are in it.

**Where it is best.** Chapter readings and `plot.md` had no defect in 37 claims.
Short, table-shaped readings quote and place; the prose readings on term pages
and in records interpret, and that is where the defects are.

**Every stated count in the sample was recounted** with `grep -cw` and `-ciw`.
Apart from S060 and S114, all held, and no claimed zero was non-zero by case.

**What it does not say.** One sample of 119, with a 95 % interval of about
4–15 % around the 9 % defect rate. The auditors were Sonnet and the session
confirmed only their DEFECT verdicts, so an OK the auditors got wrong is not
counted. Documents 1–31 are not sampled.
