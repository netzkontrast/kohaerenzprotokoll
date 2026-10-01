# Do we measure correctly? An audit of the retrieval bench, and how to improve the evaluations

**2026-09-30 · Measured; one proposal, for the author to decide.** On the author's „Do we measure correctly? Or how can we improve our
evaluations?“, after the HyperExtract backfill was stopped (decision 019). The numbers are `Plan/runs/graph-lab-2026-09-30/eval-audit.py`
(output `eval-audit.txt`); they are counts over the repository's files and no model was called. Nothing here changes what `graphrag.py`,
`ask.py` or the store return.

## 0. The answer on one page

**Partly.** What we measure is sound for **comparing two configurations on one store**, for **cost** and for **whether a checker can fail**.
It is not sound as evidence that a change *finds evidence that helps*, and three of our headline claims are weaker than they were worded.

1. **The gold is circular.** The bench's gold is the file lines the conflict and question records cite. **92 % of those lines (1,130 of 1,226) are
   lines that a term or chapter page also quotes**; per case the median is 95 %. A finder that returns the wiki's own verified quotations
   (`graph-evidence`) is rewarded for returning what the records already cite. The bench is a regression test of the wiki's own graph, not a
   measure of discovery.
2. **Discovery cannot score at all.** All 55 gold documents are read ones (58 have a census), and a case's gold is 24.5 of them (median), 42 % of the
   read corpus. No unread document is gold in any case, so finding a relevant document nobody has read — the use the project exists for — is invisible,
   and `entity-unread` measures nothing *by construction*.
3. **Twenty-four cases are fewer, and more alike, than they look.** The cases' gold document sets overlap (mean Jaccard 0.35); 54 of the 55 gold
   documents are gold in two or more cases and one is gold in 23 of the 24. The standard error of the `he-lines` effect is 0.0107, so the smallest
   true mean effect the bench can show (80 % power, two-sided 90 % interval) is **about 0.027** — and the gain we reported, +0.029, is at that limit,
   picked from four limits (10, 20, 40, 80). Expect it to shrink: the co-mention effect did, to a third, on the second label set (note §5.2b).
4. **The score depends on the case, not only on the method.** Spearman −0.56 between a case's number of gold documents and the default pack's
   document recall; in 9 of 24 cases the gold has more documents than the pack holds (the pack's size caps the mean at 0.90, so the budget is not the main limit).
5. **One conclusion was argued by eye and is now tested, and it stands.** Decision 019 said five more gold documents left the `he-lines` gain where it was,
   and I had compared two intervals side by side, which is not a test. The paired difference over the 24 cases is **−0.0003 [−0.0028, +0.0021]** in document
   recall and −0.0005 [−0.0017, +0.0008] in line recall, 22 of 24 cases identical. The stop stands. The further claim that the finder's *seeds and ranking*
   limit it is an inference from the ceiling counts (182 gold-document slots missed although read), not a test.

## 1. What is sound, and stays

- **Same-store, paired comparison with the default.** Every finder and relation is scored against the default *of the same store*, never against an
  earlier default, because the gold grows with the records. That is what made the backfill's null result readable.
- **Weights chosen leaving each case out** (`graphlab.py`), so a weight is not tuned on the case that scores it.
- **A second label set** (the wiki's own links, 91 pages) that contradicted the first in size and so caught an optimistic effect.
- **Cost from the ledgers**, failed calls included. The one estimate made without them was out by a factor of three and was corrected when they were summed.
- **The two-reader ceiling** for candidate lists (F1 0.66 between two blind readers), **hash-drawn** samples, a **quality sample** that read 119 claims against
  their lines, and self-tests that **hand each checker the defect it must name**.

## 2. What is weak, and what each weakness does to a claim we made

| claim | what the audit says |
|---|---|
| `graph-evidence` earns its place (−0.079 when removed) | it returns lines the pages quote, and 92 % of the gold is such lines: partly memorisation of the wiki's own citations |
| `bm25-lines` earns its place (−0.129) | the gold lines were themselves found by lexical search while the wiki was read, so they are the lines BM25 finds best: selection bias toward lexical findability, unmeasured |
| `he-lines` adds +0.029 at 40 lines | at the detection limit, one of four limits, on gold that is definitions, contrasts and causes — what the contracts extract and what a record cites. Direction plausible, size not established |
| `entity-unread` is inert | inert by construction: no gold document is unread |
| co-mention lifts conflicts and questions by 0.06–0.11 | on the same 24 cases it was tuned on; a third of that on the second label set. The smaller number is the better estimate |
| a contract is 58–100 % right | labelled by the working session — the model family that wrote the contracts — 3 to 30 rows a contract, no second labeler, no agreement figure |
| the backfill moved nothing | true of this bench (paired difference −0.0003 [−0.0028, +0.0021]); what the bench cannot see it cannot say |

## 3. How to improve the evaluations — in order of value for cost

1. **Freeze and version the evaluation sets** (offline, about an hour). Snapshot the gold with a hash, split the cases into a development and a held-out
   part (by document cluster, not at random, given the overlap), log the set's hash with every `baselines.jsonl` row, and give new cases to the held-out split
   first. The gold drifts as records grow; a trend line needs a fixed set.
2. **Pre-state the comparison** (free). Before a run, in the lab's README: the metric, the paired comparison, the smallest effect worth having, the smallest the
   bench can show, and the stop rule. Report every configuration tried as a family (`baselines.jsonl` already counts them) and adopt nothing that has not
   replicated on the held-out cases or the second label set.
3. **Leave-one-document-out for the graph finders** (offline, moderate code). For a gold document *d*, hide *d*'s readings — the page quotations from *d*, its
   `P_HE_*` rows, its graph edges — and ask whether the pack still finds *d*'s gold lines. That simulates an unread document, which is the real use, and it
   removes the circularity the pages cause. BM25, which reads the raw text, is unaffected, and that is itself the finding.
4. **An independent gold, built by pooling** (a few dollars of first-party Claude, with the author's yes). Take the union of the top lines of several finders
   and a random sample outside them, and have a judge that sees only the question and the line with its neighbours — never a page, a record or the finder —
   grade each line (relevant / partly / not). **Calibrate the judge on about 60 lines the author grades.** Pooled judgements measure relevance directly and
   do not depend on what the wiki already cites; pooling favours the systems in the pool, which the random sample estimates. This is the usual way to evaluate
   retrieval without a hand-built gold.
5. **Better metrics, reported per case.** Success — at least one relevant line in the pack — beside recall; recall normalised by what the gold size and the
   budget allow; nDCG or the rank of the first relevant line, which a fixed pack hides; each with its paired interval and the detection limit.
6. **Contract labels that can carry a number** (the working session plus the author's time). Hash-drawn rows only, at least 30 per contract before a figure is
   quoted, two independent labelers with different instructions and their agreement (Cohen's kappa), the author's grades on 50–100 rows as the anchor, Wilson
   intervals, no pooling across contracts. §5 says what a blind reader's relation lists, written since, already add.
7. **Answer-level evaluation for the goal.** `ask` answers are checked for placed quotations and fabrication by code. What they never meet is a reader: a blind
   pairwise comparison of two answers by the author on about twenty questions, which calibrates any model judge before it is used.
8. **Spend by the first slice.** Before a pass over the corpus, run a tenth of it, measure the marginal gain with a paired test, and stop by a rule written
   beforehand (`hyperextract-learning`, learning 9).

Items 1–3 and 5 cost no model call. Item 4 needs a yes and a small spend; items 4, 6 and 7 need the author's grades, which are the one input nothing here can replace.

## 4. What this audit does not show

- It does not say the finders are useless: a finder that reproduces the wiki's citations may still be what a writer wants at the desk. It says the bench
  cannot tell that from finding new evidence.
- The 92 % counts lines quoted *anywhere* on a term or chapter page, not on the page of the case's own terms: an upper bound on the leakage. The cases do not
  all lean on it equally (per-case minimum 68 %).
- The power figure is for one comparison of one finder against the default. A comparison of two stores that differ in a few lines has a far smaller
  standard error (±0.003 here), which is why the paired test of the backfill could say more than the bench can say about the finder.
- Nothing here measures the project's other goals — conflict detection, the plot model as checkable rules, the quality of generated questions. They have no
  evaluation yet beyond the records' own self-checks.

## 5. Added after the note was merged: what PR #131's gold relations show

The same day a parallel session added `scripts/goldeval.py` (every extractor against every gold candidate list) and `scripts/goldrel.py` (one blind
reader's definitions, contrasts and causes, in the contracts' own ten types; `Plan/runs/gold-2026-09-30/README.md`). Both scorers run offline; I re-ran them
for this section and the figures are theirs. No model was called here.

- **It is a label that did not come from the working session — the kind §3 item 6 asks for, one step short.** The reader wrote its lists without the
  contracts' rows in view, code checks that each row's line holds its surfaces, and code does the scoring. It is another Claude (Sonnet subagents): independent
  of the working session's labels and of the contracts' output, not of the model family. On three documents the contracts' pairs have **precision 49 %**
  (`TermDefinitions`), **27 %** (`TermContrasts`) and **36 %** (`CausalLinks`) against that list — 49, 38 and 52 % counting a row that stands on a gold row's
  line and meets one of its endpoints — and recall 52, 50 and 33 %. For the names alone, over 17 gold documents, precision is 62 %, 12 % and 12 %.
- **It neither contradicts nor confirms the „58–100 % right" of §2.** The working session asked whether a row's quotation states what the row says
  (`ok`, `part`, `wrong`); the reader's list answers whether one blind reader also wrote the row. A true row can be missing from one reader's list — which lines
  count as defining a term, where an endpoint is cut — so the two figures measure different things. What they share is that each rests on one reader. **No single
  number for a contract's precision is established**, and a claim that quotes one should say which.
- **The ceiling is still missing.** One blind relation reader is one reading. For term lists two blind readers agreed at F1 0.66 when each selected and at
  0.82–0.93 when both listed exhaustively (P27); for relations nobody has measured it, and until someone does the 50 % recall above reads as neither good nor
  bad. A second blind relation reader on the same three documents — that session's own open item — gives the figure §3 item 6 asks of every label set, the agreement
  between two labelers.
- **It scores extractors, not retrieval.** The bench's circular gold (§0 item 1) and the missing unread-document cases (§0 item 2) are untouched by it: nothing
  in `goldeval.py` or `goldrel.py` says whether a finder returns evidence that helps.
