# The HyperExtract backfill, 2026-09-30 — stopped after 14 of 137 runs

The author: „Use Haiku agents to Backpoet hyperextract for all allready Read sources“. A source is *read* when it has a census
in `Sources/terms/`: 58 of the 586 landed. The three contracts the graph laboratory measured — `TermDefinitions`,
`TermContrasts`, `CausalLinks`, the ones whose lines the `he-lines` finder answers from — had run on twelve of them
(`Plan/runs/hyperextract-templates-2026-09-30/scaled.sh`), and `CausalLinks` on a thirteenth, in the pilot. This was to run the
rest: 137 runs over 46 documents.

**It was stopped after 14 runs, on the author's question „Is the backfill usefull? If not - stop it“ (decision 019,
`Plan/decisions/019-the-hyperextract-backfill-stopped.md`).** Five documents had been read, $11.44 spent, 77 minutes; `he-lines`
at 40 lines gained +0.029 document recall before and +0.029 after, the same seven cases up. The note's §6.5
(`Plan/concept/graph-contracts_2026-09-30.md`) has the numbers. `STOP` is committed, so `backfill.py run` ends before its first run
and `backfill.py status` says why; delete it to resume (`NOW.md` has the command).

| file | what it is |
|---|---|
| `backfill.py` | the driver: `plan`, `run`, `status`. Resumable, ordered by the gold, one run at a time, stops by itself |
| `STOP` | committed on purpose (decision 019): while it exists the driver ends before its first run |
| `log.txt` | one line a run: the document, the contract, the clock, and what `he_claude.py` printed |
| `commit_batch.sh` | stages the finished run directories and the log, commits with the message given, pushes |
| `stats.py`, `stats-stopped.txt` | runs, calls, cost and rows per contract and pass; the output at the stop |
| `reach.py`, `reach-stopped.txt` | what the rows reach of the bench's gold, the lift over the base rate, and dollars a gold line reached; the output at the stop |
| `ceiling.py` | how much of the gold documents the default pack misses, and whether a contract has read them: what more runs could even try |
| `measure.sh`, `paired.py` | the whole post-pass measurement (store, bench with `he-lines` at 10/20/40/80, E5, yield, the note's tables), and the paired comparison against the default of the same store |
| `ask-finders/` | the bench results at the stop, `*-interim14.{txt,json}`, `paired-interim14.json` and the log |
| `sample.py` | draws the rows to label, by the hash of their id; none has been labelled |

**What was chosen, and why.** *Which contracts:* the three of the scaled pass, because they are the ones whose rows a measured
finder answers from (+0.029 document recall with 40 lines, `Plan/concept/graph-contracts_2026-09-30.md` §5.4) and whose records
were right or near in 36 of 36 labelled rows on the bench's documents. `TermReadings`, the pipeline's first template, is not
among them: on the one document it was measured against it found a subset of what a Sonnet reader's note cites. The structure
contracts (`ChapterBeats`, `CardFields`, …) were 86–100 % right, and their retrieval value is untested. *Haiku through
`claude -p`* and not subagents: a subagent would wrap the same call, and `he_claude.py` records every call, its cost and its
failures. *One at a time:* the author's „achte auf mein Nutzungslimit - starte diese nicht parallel“. *Gold first:* `he-lines` is
worth what the contracts have read of the documents that hold the answers, so the documents the conflict and question records
cite most came first. **That order was blind to size**: it put `kohaerenz-protokoll` (372 KB) first, $7.45 of the $11.44 for 21
gold lines; ordered by gold reached per dollar the same money would have read far more of them.

**What it cost**, estimated from the scaled pass before it ran: 46 documents, 2.54 MB, about $19 a contract, $56 for the three,
about 6.5 hours. Measured over the 14 runs: $7.11 a megabyte a contract (the note's estimate was $7.3), 956 calls of which 12
returned no valid JSON (their chunk yields no rows). The pass stopped at $11.44.

Each run is staged where the twelve are, `Plan/runs/<slug>/hyperextract/<contract>-haiku-2026-09-30/`, with its calls, candidates,
report and usage, so `hegraph.py` loads it into the store as `P_HE_*` proposals and `hegraph.py report` counts it. Its
`usage.json` names the author's instruction as its approval. Nothing is adopted and nothing in the core graph changed.
