# 019 — The HyperExtract backfill is stopped after 14 of 137 runs

**Date:** 2026-09-30 · **Decided by:** the session, on the author's conditional instruction · **Status:** in use

## What was asked

> Is the backfill usefull?
> If not - stop it

The backfill is the author's „Use Haiku agents to Backpoet hyperextract for all allready Read sources“ of the same day: the three
contracts of the scaled pass (`TermDefinitions`, `TermContrasts`, `CausalLinks`) over the 46 read documents that had not had them,
Haiku through `claude -p`, one run at a time, the documents holding most of the bench's gold first — 137 runs, estimated at $56 and
six and a half hours. It had run 14 of them ($11.44, 77 minutes) when the question came; a container restart at 20:16 had killed the driver once, and
it was found dead again at 20:52, its last run begun at 20:27. The session measured what the 14 runs had moved, and answered it.

## What was measured

`Plan/runs/hyperextract-backfill-2026-09-30/` holds every number (`reach.py`, `ceiling.py`, `ask-finders/`); the note's §6.5 reads them.

| | earlier runs (14 documents) | the backfill so far (5 documents) |
|---|---|---|
| gold lines in those documents | 493 | 175 |
| gold lines some row is on | 297 (60 %) | 93 (53 %) |
| share of the rows' lines that are gold, against the base rate | 19.3 % against 6.1 % | 7.7 % against 2.9 % |
| cost, and dollars a gold line reached | $12.32, $0.041 | $11.44, $0.123 |

The second column is dearer because the plan's order — most gold lines first, then smallest — put `kohaerenz-protokoll`, 372 KB,
first: $7.45 of the $11.44 for 21 gold lines ($0.35 each); the other four documents reached 72 for $3.99 ($0.055).

| `he-lines`, document recall against the default of the same store | after the scaled pass (15 of the 55 gold documents read, 46 % of the gold lines) | now (19 of 55 read, 57 % of the gold lines) |
|---|---|---|
| 10 lines | +0.009 [+0.003, +0.018] | +0.009 [+0.003, +0.018] |
| 20 lines | +0.018 [+0.006, +0.034] | +0.016 [+0.006, +0.028] |
| **40 lines** | **+0.029 [+0.011, +0.049]**, seven cases up, none down | **+0.029 [+0.012, +0.048]**, the same seven cases up, none down |
| 80 lines | +0.021 [−0.007, +0.046] | +0.021 [−0.016, +0.058] |

Five documents holding 14 % of all gold lines were read, and the share of gold lines in documents some contract has read went from
46 % to 57 %. The finder's gain did not move. Four cases changed by 0.031 or less, in both directions; the default pack is identical.
Four of the 24 document slots the finder recovers are in documents the scaled store had not read (`kohaerenz-protokoll` in C2, C6
and Q5, `storyform-und-outline` in Q5), and in those cases document recall did not rise — the finder's 40 lines are a fixed budget,
and lines of the new documents replaced lines of the old. Of 569 gold-document slots over the 24 cases the default finds 139 and
`he-lines` recovers 24; 182 are missed although a contract has read the document, and 226 are missed in documents no contract has
read. The paired difference over the 24 cases — not two intervals laid side by side — is −0.0003 [−0.0028, +0.0021] in document recall and −0.0005 [−0.0017, +0.0008] in
line recall, 22 of 24 cases identical (`Plan/runs/graph-lab-2026-09-30/eval-audit.py`). **Coverage did not limit the finder here; that its seeds and its ranking do is an
inference from the ceiling counts, not a test** (`Plan/concept/evaluation-audit_2026-09-30.md`).

## What was chosen

**Stopped, and stays stopped.** The 14 runs stay (nothing is thrown away: they are staged proposals like the 36 before them). A
committed `STOP` file in the backfill's folder makes the driver end before its first run and makes `backfill.py status` say why;
the scheduled check-in no longer restarts it; `NOW.md` names it stopped. Nothing is adopted and nothing in the core graph changed.

## What was rejected

- **Finishing the pass** (123 runs, about $40 to $46, five hours of the author's usage). The last $11.44 bought nothing the bench
  can see, and the remaining documents hold less gold each (the last 22 in the plan's order hold 177 of the 586 gold lines left).
- **Finishing only the cheap, gold-dense documents** (ordered by gold reached per dollar, $11 would reach 62 % of what the rest
  could). That is a better order and the wrong question: reach is not what the finder lacks.
- **Finishing one contract.** `CausalLinks` reaches fewest gold lines per dollar on the backfill's documents ($0.142), `TermDefinitions` most ($0.065);
  neither changes the finder's gain.

## What would change our mind

- A finder that spends its lines better — per seed, or by the question's wording (*was ist X* from `TermDefinitions`, *warum* from
  `CausalLinks`) — so that an unread document's rows could enter its top lines. Then `ceiling.py` names where to read next, cheapest
  first (226 slots in unread documents), and the pass is worth a second look.
- The author turning `he-lines` on (`NOW.md`, question 4) or naming the contracts and categories to run (question 2): the pass was
  run before either was answered, and that is the plainer reason to have stopped it.
- A labelled sample of the backfill's rows (`sample.py` draws it) showing them as right as the twelve documents' — none has been
  labelled, and three rows drawn by eye looked looser.

To resume: delete `Plan/runs/hyperextract-backfill-2026-09-30/STOP` and follow `NOW.md`.
