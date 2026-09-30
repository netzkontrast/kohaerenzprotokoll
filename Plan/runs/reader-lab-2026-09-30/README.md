# Reader lab — step 6's ten remaining documents, one at a time, 2026-09-30

The author, 2026-09-30, after ten of twelve parallel readers had been stopped by the
session's usage limit:

> „starte diese nicht parallel — sondern nutze die Chance und beobachte jeden der zehn —
> und versuche diese als lernlabor zu verstehen.. Probier ander Dinge aus.. vielleicht
> mal… gib ihnen unterschiedliche Anweisungen"

So the ten are read one after another. Each run gets its own instruction, and each is
measured from its transcript before the next one starts.

## What the first twelve cost — measured from their transcripts

`transcripts.py` reads Claude Code's own record of each subagent. The transcripts live
outside the repository and die with the container, so `transcripts.json` keeps their
numbers. It holds no text, only numbers. The twelve ran on 2026-09-29 as
`general-purpose` agents on Sonnet, all at once, each told to follow
`.claude/agents/document-reader.md`.

| | per reader, range over the twelve |
|---|---|
| API calls | 55–87 |
| wall-clock | 28–35 minutes (ten stopped at the limit after 29–35) |
| cache reads | 11.7–21.8 million tokens |
| largest context | 325–462 thousand tokens |
| cost proxy (`transcripts.py`) | 1.6–2.8 million |
| what the Agent notification reported | 380 and 396 thousand for the two that finished — the last call's size, not the consumption |

**Where it goes.** Each call re-reads the whole context, so the cost is the number of
calls times the size of the context. Four things make the context large:

1. **The fixed part is 67 thousand tokens at the first call.** It holds the system
   prompt, the tool definitions, `CLAUDE.md` and the skill listing. A run of 62 calls
   re-reads it 62 times, about 4 million of 13.8 million cache reads.
2. **The rules are read in full, once, and then carried.** That is five files, 70–105
   thousand characters of `Read` results, before the document. They are
   `document-reader.md`, the ingest skill, `german.md`, `artifacts.md` and the briefing.
3. **Nine of twelve readers read script sources** — `capture.py` twice, `gold.py`,
   `reconcile.py`, `ui.py` — to find out what a census looks like. No rule file shows
   one. No reader ran `reconcile.py` on its document, so no census saw the wiki.
4. **About half of the context's growth is not in the transcript: 35–54 %.** The
   best explanation is thinking, which is stored redacted. The estimate calibrates
   characters per token on the transcript itself (2.0–2.35) and subtracts what is
   visible. The pilot's four `wiki-reader`s, working from a brief, show 7–17 %.

Output is not measured. The transcript keeps the first stream event's usage, not the
final count, so `wrote` counts characters instead: 97–170 thousand per reader.

**The lists are long by design.** The candidate lists have 63–318 rows. Even the
40-line technical audit (9 kB) has 216. Decision 012's rule is exhaustive, and this
lab does not change what a census lists.

## The runs

The ten documents differ in size and in what the stopped reader left
(`Plan/runs/<slug>/partial-2026-09-29/`). So a run is an observation, not a controlled
comparison. The runs ratchet: each keeps what held in the run before and changes one
thing. The baseline is the twelve transcripts above.

| # | document | lines | left by the stopped reader | the change |
|---|---|---|---|---|
| R1 | `technical-audit-research-mandate-the-kohaerenz-protokoll-fra` | 40 | census, note, at the note | the `document-reader` agent type, with its six tools; resume from the partial |

Quality is checked the same way each time:

- `quotes.py` on the census and the note: 0 unresolved and 0 unchecked;
- the census and note formats, as `account.py order` and the reconciliation read them;
- after reconciliation, what the readings step took from each document.

Five claims of each note are read against their lines. That is the check that found
the 11 defects of the quality sample, which `quotes.py` could not see.
