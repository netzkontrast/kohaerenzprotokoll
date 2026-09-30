# Pipeline measurement — 2026-09-29

What the reading pipeline spent its effort on over every read document, measured
for `Plan/concept/pipeline-optimization_2026-09-29.md`. Nothing here reads a new
document, calls a model or changes the wiki.

| file | what |
|---|---|
| `measure.py` | the measurement, standard library, about 4 s; writes nothing |
| `measure.txt` | its output on 2026-09-29, at `07487f1` |

```bash
python3 Plan/runs/pipeline-2026-09-29/measure.py > Plan/runs/pipeline-2026-09-29/measure.txt
```

## Measured beside it, with the command

**The invariants, 2026-09-29, all green, about 80 s together:** `selftests.py`
34 of 34 suites held (56 s); `account.py order` holds; `state.py --prose` 0
contradictions (16 s); `quotes.py` 20,811 cited quotations checked, 0 unresolved
(4 s); `judgements.py` 120 judgements, 8 agree, 0 disagree; `chapters.py` 0
defects; `reconcile.py --sweep-open` 0 open; `sources.py check` ok.

**Wiki growth per run** — lines added and removed in `Wiki/candidates`,
`Wiki/conflicts`, `Wiki/questions`, `Wiki/chapters` and `Wiki/overview`:

| run | `git diff --shortstat <before> <after> -- <those folders>` |
|---|---|
| document 47 | `549df9e 4e27331`: 62 files, +740 −157 |
| documents 48–50 | `4e27331 7f11861`: 71 files, +735 −167 |
| document 51 | `7f11861 48e3351`: 55 files, +611 −141 |

**The readers' half of a run, from commit times** — the readers' brief to the
reconciliation record: document 31, 17:41 → 18:03 (22 minutes, eight readers, 57
pages); document 51, 08:17 → 09:31 (74 minutes, four readers, 42 pages). Nothing
bounds the reading half: the session read each next document while the last
one's readers wrote, and no run since document 4 has a `run.md`.

**The size of the always-loaded files over time** — `git show <commit>:CLAUDE.md
| wc -c`, the same for `NOW.md`: 36,180 and 14,137 bytes at the first commit of
the shallow clone (2026-09-23 20:30), 113,433 and 133,665 at `07487f1`
(2026-09-28 12:44).

**What a subagent carries before it does anything** — a Sonnet
`general-purpose` subagent was asked, with no tool allowed, whether project
instructions were in its context. It quoted CLAUDE.md's first heading and named
the section that mentions `Coherence Protocol.mp3` correctly, and said NOW.md was
not in its context. The run cost **96,427 tokens** and one tool use, its reply.
That is the fixed context of one subagent with this session's tool set; how much
of it is CLAUDE.md was not separated.

## What it cannot say

- **Tokens and minutes per step.** No run records them; the plan's step 1 is
  the recording.
- **Page sizes at the time of each run.** Section 4 measures today's pages; a
  run in the past loaded smaller ones, so its column is an upper bound for that
  run and today's cost for the same run.
- **Whether a digest is enough.** Section 4's digest is what a reader would
  load; whether it misses something the whole page would have shown is what
  the pilot measures.
- Sections 6 and 7 are **negative results**, kept because each closes a
  shortcut that looks obvious.
