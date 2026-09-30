# Query rewrite into the wiki's German terms — 2026-09-30

Step 3 of `Plan/concept/dspy-learning_2026-09-30.md`. Before this, six of the 24 bench records
found no seed term. Their titles are English (`knuckles`, `Flight`, `blind spot`, `Be-er/Do-er`),
the page surfaces are German, and the glosses covered none of them.

**What ran.** One Sonnet subagent read `input.json`: the 24 bench questions and the 106 pages'
surfaces. It saw no document text and no record. For each question it wrote `rewrite.json`:
- 1–5 page slugs from the list;
- 2–6 German search words.

`ask.py bench --rewrite rewrite.json` built each pack from the question plus those terms
(`ask.expand`). The pack still shows the question as asked.

| | document recall | line recall |
|---|--:|--:|
| without rewrite (`bench-2026-09-30-60000.json`) | 0.270 | 0.094 |
| with rewrite (`bench-2026-09-30-60000-rewrite.json`) | **0.339** | 0.092 |

**What moved:**
- Three cases with no recall at all now have some: C5 from 0 to 0.35 documents, Q2 from 0 to
  0.46, C4 from 0 to 0.13.
- C10, the knuckles, rose from 0.07 to 0.37 line recall on „Knöchel" and „blutende".
- Five cases fell: C2, C7, C9, Q1 and Q6. The added terms put more documents in the pack, and the
  budget then cuts the gold documents.

**Caveats:**
- The labels are the records' own references, written by the same hand as the pages. That is the
  caveat `graphrag.py bench` carries too.
- The subagent saw the records' titles as questions, which is how the bench poses them, but no
  record body.
- One run, no repeat.

**In the pipeline.** A rewrite is optional input: `ask.py pack "…" --terms '{"pages": [...], "words": [...]}'`.
Worth doing first for English questions and for any question that names no wiki term.
