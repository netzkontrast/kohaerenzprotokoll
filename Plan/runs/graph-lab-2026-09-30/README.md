# The graph laboratory, 2026-09-30

What each relation, weight and finder is worth to retrieval, measured on the wiki's own labels. The note that reads these
tables is `Plan/concept/graph-contracts_2026-09-30.md`; the tool is `scripts/graphlab.py` (the `ask` finders are
`scripts/ask.py bench`). Nothing here changes what `graphrag.py` or `ask.py` return by default.

**Which wiki a table is of.** The files at this level are of the wiki as the branch left it: 58 documents with a census,
106 pages, the 24 labelled cases, and for the finders and E5 a store that holds the scaled contract pass. `rerun.sh` made them.
`first-run/` holds the tables of the first run — the diagnosis and E1 before the readings of documents 52–54 were merged
(13:53), E2–E5 after them — which the rerun overwrote. Where a number moved, the note gives both.

| file | what it is |
|---|---|
| `diagnose.md` | per case: seeds, the gold pages hit, reached and outranked, or not reached |
| `e1-core.md`, `.json`, `.log` | E1: the seven stated relation types — uniform, one alone, one off, learned, cross-validated |
| `e2-enrich.md` | E2: relations the corpus adds (co-occurrence, co-mention in three scales) at every weight |
| `e2b-comention.md` | E2b: the normalised co-mention relation, sparsified, at every weight; 96 configurations and the leave-one-out choice |
| `e2c-links.md` | E2c: **a second label set — the wiki's own `[[links]]`**, 91 pages; co-mention and the contracts' page pairs on it; and the 40 co-mentioned pairs no page links |
| `e4-hub.md` | E4: the hub correction and the seed specificity of `graphrag.pagerank` |
| `e5-he.md` | E5: the page pairs the HyperExtract contracts read, by relation family, at every weight |
| `rerun.sh`, `rerun-*.txt` | the commands of the second run and what each printed |
| `ask-finders/` | E3: `ask.py bench` for each finder switched off or on; `run.sh`–`run3.sh` on the store before the scaled pass, `run4.sh`–`run6.sh` after it; `paired-scaled.py` compares them with the default (`paired.json` is the first set, `paired-scaled.json` the second) |
| `ask-bench-baseline.txt` | the bench's default at the start, per case |

Every configuration is also a row of `Plan/runs/baselines.jsonl` (`graph-lab-*` tasks), so `baseline.py compare` reads it.

`ask.py bench` also writes `Plan/runs/ask/bench-<date>-<budget><finders>.json`. Those files are the first run's: a rerun with the
same finders on the same day overwrote them, so the second run's are copied into `ask-finders/*-scaled.json` and the first
run's restored. A bench's name now ends with the first eight characters of the store's input hash, and a rerun on another
store is another file.

**What the tables cannot say.** The labels are written by the hand that wrote the pages. With 24 cases and two of them
finding no seed, a difference smaller than its interval is not a difference; the 91 link cases are a second set, the same
hand's. `graphlab.py selftest` holds the lab's own rules (a run against itself moves nothing; a hidden link is found only
through another relation; the seed is not its own answer).
