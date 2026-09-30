# Pilot of the readings step — documents 48–50, 2026-09-29

Plan step 4 (`Plan/concept/pipeline-optimization_2026-09-29.md`, decision 015),
run on documents already read, so no new document was started.

## How it ran

- **Four `wiki-reader` subagents on Sonnet**, split by page group: figures;
  worlds and physics; concepts and chapters; records. The rules came from
  `.claude/agents/wiki-reader.md` and the document knowledge from the original
  brief (`Plan/runs/readings-brief-documents-48-50.md`), its rules left out.
- **The pages were a worktree at `3d97d39`**: the three documents' censuses,
  notes and brief were committed there, and none of their readings yet.
- Readers read **digests** (`digest.py --root`), never the pages. They wrote 117
  files into `readings/`, each quotation followed by `^[?]`.
- **Eight decoy pages** were added to the groups, pages the original run gave no
  reading from these documents: `emergenz`, `coheron`, `ueberwelt`, `nexus`,
  `erason`, `vortex`, `dkt`, `kap-01`.
- `readings.py apply pilot-48-50 --root <worktree>` wrote 65 pages (829 lines) with
  every line placed by code. `applied.diff` is the result. It is not merged into
  `main`, which already holds the original readings of these documents.

## Against the bar set before the run

| | pilot | bar |
|---|---|---|
| quotations unresolved, 65 pages | **0** | 0 |
| quotations unchecked (no citation), 65 pages | **11, on 7 pages** — measured 2026-09-30; this row said 0 until then | 0 — **not met** |
| corrections in review, against the original run's | **not measured** — the pilot's pages were never reviewed | no more than the original — **not met** |
| (page, document) pairs against the original run (`compare.py`) | **F1 0.89** — precision 0.81, recall 0.98; 94 shared, 22 only the pilot's, 2 only the original's | ≥ 0.8 |
| comparison flags from `lint_readings.py` in the three documents' sections | 2, one of them in a scan reading from before the pilot | — |
| stray quotes, empty spans, joins | 0 | 0 |

**So the pilot met two of its four bars, not all of them.** The review of
2026-09-30 found the gaps, and a re-run confirmed the first. The 117 files were
applied again, by the `readings.py` of `116f79c`, to a fresh worktree at
`3d97d39`, and `quotes.check_file` was run on every page before and after. The
result was 0 new unresolved and 11 new unchecked quotations, on 7 pages.

Among the 11 are a name the Hard-Problem-Analyse cites, „Hard Canon
Masterfile“, a profile field in a heading, „Schicksal“, and two phrases in
differ lines. Each is a quotation with no citation, and `quotes.py` counts such
a quotation as unchecked, not as checked.

The row said 0 because only `unresolved` was read off the run. **The
`readings.py` of 2026-09-30 refuses all of them before a page is touched.** Run
on the same 117 files, it refused 10: the nine that carry the 11 quotations, and
one whose count mark had no words before it. The pilot's readings are a
comparison and were never merged, so no page in `main` carries them.

**The corrections bar was never measured.** It needs the pilot's pages reviewed
the way the original run's were, and that review did not happen. F1 compares
which pages got a reading from which document; it says nothing about whether a
reading is right. The quality sample (`Plan/runs/quality-sample-2026-09-29/`)
reads that, and it found its 11 defects in the original run, not in the pilot.

**The two readings only the original run has** are C3 and C13 from the
Charakter-Kompilation. The pilot's records reader judged that the document does
not speak to either.

**The 22 only the pilot has** are readings the original run did not write:

- the world pages from the Charakter-Kompilation and the Hard-Problem-Analyse;
- `dkt`, `emergenz` and `erason` — three of the decoys;
- `kap-01`, a weak reading of the range „Kap 1-5", its reader said;
- „states no rule" readings on `hitze-polaritaetsregel`.

Whether each belongs on its page is the review's call.

**What `readings.py check` stopped before any page was touched.** Five of one
reader's files were refused: nested quotation marks, and a straight `"` inside a
quotation. The reader fixed them. One other file was refused for a quotation its
line did not hold, and was fixed before `apply`. In the old step, each of these
would have reached a page and waited for `quotes.py` or the review.

## Cost

| | |
|---|---|
| readers | 4, Sonnet: 213,717 + 240,492 + 232,654 + 274,571 = **961,434 tokens**, 27–32 tool uses each |
| wall-clock of the readers' phase | **489 s**, from `runlog.py` start to end |
| the 65 pages as whole files at `3d97d39` | 2.36 MB |
| the same pages as digests | 0.46 MB (5.2× less) |

**No baseline to compare the tokens with.** The original run of 2026-09-27/28
recorded none, which is why step 1 exists. Its commits bound its readers' half
only from 22:39 to 08:48 across a night.

## What it leaves

- The review of `applied.diff`: the pilot readings are a proposal for comparison,
  and nothing here enters the wiki.
- `05-verify-readers.txt` is outside a reader's write list now; absences are
  count marks inside the readings.
- `lint_readings.py` reads pages, not reading files. Pointing it at a batch
  folder would let readers check themselves before `apply`.
