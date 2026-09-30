# The HyperExtract backfill, 2026-09-30

The author: „Use Haiku agents to Backpoet hyperextract for all allready Read sources“. A source is *read* when it has a census
in `Sources/terms/`: 58 of the 586 landed. The three contracts the graph laboratory measured — `TermDefinitions`,
`TermContrasts`, `CausalLinks`, the ones whose lines the `he-lines` finder answers from — had run on twelve of them
(`Plan/runs/hyperextract-templates-2026-09-30/scaled.sh`). This runs them on the other 46.

| file | what it is |
|---|---|
| `backfill.py` | the driver: `plan`, `run`, `status`. Resumable, ordered by the gold, one run at a time, stops by itself |
| `log.txt` | one line a run: the document, the contract, the clock, and what `he_claude.py` printed |
| `stage_batch.sh` | stages the run directories that are finished, for the commit |
| `STOP` | not committed: `touch` it and the pass ends after the run in progress |

**What was chosen, and why.** *Which contracts:* the three of the scaled pass, because they are the ones whose rows a measured
finder answers from (+0.029 document recall with 40 lines, `Plan/concept/graph-contracts_2026-09-30.md` §5.4) and whose records
were right or near in 36 of 36 labelled rows on the bench's documents. `TermReadings`, the pipeline's first template, is not
among them: on the one document it was measured against it found a subset of what a Sonnet reader's note cites. The structure
contracts (`ChapterBeats`, `CardFields`, …) were 86–100 % right, and their retrieval value is untested. *Haiku through
`claude -p`* and not subagents: a subagent would wrap the same call, and `he_claude.py` records every call, its cost and its
failures. *One at a time:* the author's „achte auf mein Nutzungslimit - starte diese nicht parallel“. *Gold first:* `he-lines` is
worth what the contracts have read of the documents that hold the answers, so the documents the conflict and question records
cite most come first, and the pass can be stopped at any point with the best part done.

**What it costs**, estimated from the scaled pass before it ran: 46 documents, 2.54 MB, about $19 a contract, **$56 for the three,
about 6.5 hours**. `python3 backfill.py status` says what it has cost so far; the pass stops at $90.

Each run is staged where the twelve are, `Plan/runs/<slug>/hyperextract/<contract>-haiku-2026-09-30/`, with its calls, candidates,
report and usage, so `hegraph.py` loads it into the store as `P_HE_*` proposals and `hegraph.py report` counts it. Its
`usage.json` names the author's instruction as its approval.
