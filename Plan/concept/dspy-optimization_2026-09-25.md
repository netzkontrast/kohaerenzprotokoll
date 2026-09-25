# DSPy optimization of the scripts — the ladder on real models, 2026-09-25

*The author asked, in this order: „Use dspy Optimierung on the Scripts", „Learn
all there is about dspy", „Add openrouter free Models in the mix". This page is
what ran and what it says. Every number comes from `python3 scripts/pairs.py
report`, `Plan/runs/baselines.jsonl` or the per-call records under
`Plan/runs/surface-pairs/lm/`. **Nothing here entered `judgements.jsonl`,
`fold()`, reconciliation or a wiki page.** A model's merge is a proposal; the
ledger is a person's.*

## What ran

**The one DSPy program with an optimizer harness**, `scripts/pairs.py`: one term
or two, over the 63 labelled pairs of `Plan/runs/judgements.jsonl`. The plural
rule of decision 010 answers first and decides 44; a model is asked only about
the 51 it leaves — **19 the ledger calls one term, 32 it calls two**. Five
stratified folds, so every pair is scored by a program compiled without it; each
held-out pair asked three times with no cache (P18); the six never-merge canaries
asked of the program compiled on all 63. The metric is the person's decision,
with the person's recorded rule as feedback.

**The models, under decision 011** (written for these runs):

| model | route | notes |
|---|---|---|
| Claude Haiku 4.5 | `claude-cli/haiku` — `scripts/claude_lm.py`, first party | thinking off; the task model of every rung |
| Claude Sonnet | `claude-cli/sonnet` | GEPA's reflection model, thinking on |
| `google/gemma-4-31b-it:free` | `route/…` — `route.py`, pinned | **not reached**: „temporarily rate-limited upstream" for the whole attempt, its provider's shared free pool exhausted. Stopped after 22 attempts; no row (P15) |
| `nex-agi/nex-n2.5-mini:free` | `route/…` | answered every call; 6–98 s a call as the morning went on |
| `dots-studio/dots-3-note-preview:free` | `route/…` | *(see the table)* |

Free models got what `pairs.py` sends — two term surfaces, the person's rule
sentences, the program's instructions and demos — and never a line of a
document; `--evidence` refuses a free model in code.

## The results

`python3 scripts/pairs.py report`, 2026-09-25. **merges found** is the sum,
over the 19 pairs the rule leaves that the ledger calls one term, of the share
of repeats that merged them; **kept apart** the same over the 32 it calls two;
a **false merge** is a two-term pair merged in at least one repeat.

| candidate | score | merges found /19 | kept apart /32 | false merges | cost |
|---|--:|--:|--:|---|--:|
| `rule:fold` | 0.571 | 0 | 32 | — | $0 |
| `rule:plural` — the floor | 0.698 | 0 | 32 | — | $0 |
| + LabeledFewShot, Haiku | 0.852 | 10.67 | 31.00 | J74 (3 of 3) | $0.38 |
| + LabeledFewShot **with evidence**, Haiku | 0.878 | 14.00 | 29.33 | J68 (3 of 3), J11, J38, J48 | $0.55 |
| + BootstrapFewShot, Haiku | **0.884** | 12.67 | 31.00 | J74 (3 of 3) | $0.45 |
| + InferRules, Haiku | 0.857 | 11.00 | 31.00 | J47 (3 of 3) | $5.40 |
| + GEPA (200 calls a compile), Haiku, Sonnet reflecting | 0.847 | 10.33 | 31.00 | J74 (3 of 3) | $5.38 |
| + LabeledFewShot, `nex-n2.5-mini:free` | 0.741 | 10.33 | 24.34 | **17 pairs**, J5 `Negentropie`/`Entropie` among them | $0 |
| + LabeledFewShot, `dots-3-note-preview:free` | *(pending)* | | | | $0 |

SIMBA was not run; see *What was not run*.

## Reading them

**Every Claude rung beats the rule, and the gain is recall bought with very
little precision.** Bootstrap found 12.7 of the 19 merges the plural rule misses
and merged one pair the ledger keeps apart. The rule itself merges nothing
wrongly and finds none of the 19.

**The one false merge of the plain rungs is J74, `AEGIS-Echo`/`Echo-AEGIS`, in
every repeat.** The ledger's rule: a compound is placed by what it names, and two
compounds of the same parts in the other order can name different things. A
model that reads surfaces sees the same two words.

**What stays out of reach is what the ledger decided from another document.**
J54 `Basisrealität`/`Externe Ebene` and J50/J58 (two numbers for one dwelling)
were missed in every repeat of every Claude rung, evidence included: the second
surface of each is not in the pair's document, so code placed no line for it.
J29 `AEGIS`/`Rest-AEGIS` and J70 `Kael-MC`/`Kael` were missed by every plain rung
and found by every repeat with evidence, where both stand on one line. The
facility letters J64/J65, which `NOW.md` counted among the pairs decided from the
passage, were found by Bootstrap in every repeat and by no other Claude rung; why is not
measured, because that run's fold programs were not kept. (The pair-by-pair table
is `pairs.py report`'s rows read per id; this paragraph first said all of these
were missed by every plain rung, from the first rung alone.)

**Evidence lines raise recall and cost precision, and the cost is instructive.**
`--evidence` adds, beside the two surfaces, the lines of the pair's document that
hold them, placed by code (`pairs.evidence`) — never the lines the person cited,
because a deployed program meets a new pair before anyone has read it. Merges
found rose from 10.67 to 14.00; kept apart fell from 31.00 to 29.33. The new
false merges are not noise: **J68 `Ursprungs-Ich`/`Juna`** was merged in every
repeat, because the line code placed is the glossary's own „das Ursprungs-Ich
(Juna)" — the very reading `NOW.md` holds open as a question for the author. **J11
`Zero-Trust`/`Zero-Trust-Architektur`** is the pair behind the project's founding
false conflict. A line where two surfaces stand together is evidence of
proximity, and a model reads it as identity.

**InferRules cost twelve times Bootstrap and scored below it** — the one
published result near this scale is a null result too, at n = 60
(`Plan/concept/dspy-source_2026-09-24/research.md`). Its rules, recovered with
`pairs.py final` and kept in `Plan/runs/surface-pairs/programs/`, are the
comparison this project wanted from it: they restate the ledger's own rules in
general form — slash aliases, numbered instances, a prefix naming a later state
of the same bearer, a negation prefix — and garble one (plural endings).

**GEPA rewrote the instruction and reached about where eight labelled demos
reach, at fourteen times the cost.** It changes instructions only, and the program
it starts from has none of the demos the other rungs carry, so its row is a
zero-shot program with an evolved instruction: 10.33 merges found, the same one
false merge as Bootstrap, 0.847 against Bootstrap's 0.884. Inside each fold its
search climbed from about 0.80 to 0.86–0.88 on the training rows, which GEPA uses
as its validation set when given none; held out, that did not carry. Its Sonnet
reflections wrote training pairs into the instruction as worked examples —
„Beispiel: "Basisrealität" vs. "Externe Ebene" → one-term" — so the instruction
became a place for demos. Its final instruction (`pairs.py final`, kept in
`Plan/runs/surface-pairs/programs/`) is a German check list of five rules in
order of priority, four of them the ledger's own — articles, compounds by what
they name, opposites, a numbered instance of a class — and a first one the
ledger states for one pair only: a surface that cites an outside concept stays
apart from a corpus term of the same stem, J38 `Limina`/`Liminale Räume` as its
example — **and the example is backwards**. The instruction says `Limina` cites
the outside concept and `Liminale Räume` is the corpus's own; the ledger says
`Limina` is an Alter and `Liminale Räume` the design concept cited to an outside
reference (J38). A rule a model writes reads as right and is wrong in the one
detail that decides it, which is why no rule it writes enters the ledger by
itself. With 200 metric calls a compile the search accepted
exactly three new candidates in every fold and two in the final compile on all
63, which spends more of its budget scoring the larger set (the run's log,
„New program candidate index"); `auto="light"` would allow about 580 calls.

**A free model's score hid seventeen false merges.** `nex-n2.5-mini` beat the
floor on score, 0.741 against 0.698, by finding as many merges as Haiku's first
rung while merging seventeen pairs the ledger keeps apart at least once —
`Realitätsebenen`/`Kern-Welten`, `Logos-Prime`/`LogOS`, and **J5
`Negentropie`/`Entropie`**, the founding canary, in one repeat of three. The run
was not vetoed, because the veto asked each canary once, of the final program,
and that one answer was „two terms". **Fixed**: a canary is now asked as often
as a held-out pair, and a ledger row that is a canary pair vetoes the run when
any repeat merges it; `pairs.py report` flags the rows recorded before the fix.

## What was not run

- **SIMBA.** At `pairs.py`'s settings it is about 3,200 Haiku calls a run,
  roughly $8. No paper measures it; the one measured run in the skill made its
  task worse at the highest cost of twelve; and the account's usage limit was
  reached once during this work. It is one command:
  `pairs.py run --optimizer simba --rule plural --model claude-cli/haiku
  --approval "decision 011" --repeats 3 --threads 4 --record`.
- **GEPA at `auto="light"`** — about 3,500 Haiku calls a run; the run above used
  `--gepa-calls 200`, a stated budget on the same folds.
- **Any upper rung on a free model.** GEPA or SIMBA needs thousands of calls, and
  OpenRouter's free tier allows about a thousand a day across all free models.

## What it cost

Claude through the CLI, list prices as `claude -p` reports them: $0.15 for the
first attempt with thinking on (stopped; its 18 calls are kept in
`pairs-labeled.aborted-with-thinking-2026-09-25.jsonl`), $0.38, $0.55, $0.45,
$5.40, $5.38 for GEPA, and $0.02 and $0.69 for the `final` compiles of Bootstrap
and GEPA; the InferRules `final` compile ran before `final` printed its cost, and
at a sixth of its fold run's compile cost it was about $0.8 — **about $13.80 in
all**, the one estimate marked. Free
models: $0 — `route.py` stops a run on any charged call. **Claude calls draw on
the author's usage**: the nine readers of DSPy's own sources, running beside
these calls, reached the account's usage limit once, on 2026-09-24.

## What was built, and what building it found

- `scripts/claude_lm.py` — Claude as a `dspy.BaseLM` through `claude -p`, and
  `lmrun.make_lm("claude-cli/…")`. **Thinking had to be switched off**: with
  `--effort low` alone, 18 calls spent 590–3,282 output tokens on a one-sentence
  answer; with `MAX_THINKING_TOKENS=0`, 153 calls spent 42–131.
- `lmrun.make_lm("route/…")` — a DSPy program on one free model through
  `route.py`'s proxy, **pinned**: the proxy used to answer with any free model,
  right for a tool and wrong for a measurement (P16).
- **`route.py` keyed its recording without the model**, so a pinned run on a
  second model would have been answered from the first model's recording. Found
  by reading the new record files, fixed before the second model ran, and held by
  a self-test case.
- **A pinned model can be gone for an hour**: gemma's upstream pool never
  answered. A pinned call now gives up after 240 s, and a run after six
  unreachable calls in a row, recording nothing (P15).
- **`pairs.py` asserted German on the `rule` field**, whose demos are the
  ledger's English rules; every answer was flagged. It asserts English now.
- **`pairs.py` kept no compiled program.** InferRules' rules left with its
  process, and no fold program survived to say why Bootstrap found J64/J65;
  every real run now saves its final program and each fold's to
  `Plan/runs/surface-pairs/programs/`, and `pairs.py final` compiles once and
  saves without a ledger row.
- `pairs.py report` — every row split by direction, the false merges by id.
- `pairs.py --evidence`, `--gepa-calls`, `--threads`.

## What it does not mean

- **No merge is proposed to the ledger.** A row here is agreement with one
  person's decisions on 63 pairs (P27); 0.88 is agreement, not correctness.
- **`fold()` and reconciliation are unchanged**, and decision 010's plural rule
  stays a ledger row.
- **One task, one run per candidate.** The three repeats measure a model's
  variance on a pair, not a candidate's variance across compiles.

## What it leaves for the author

`NOW.md`, *Questions for the author*, carries these:

- **Decision 011's Claude precedent** — Claude through `claude -p` treated as
  first party, like the second readers — confirm or narrow.
- **Whether a model's merge may become a review queue**: the pairs the rule
  misses and Bootstrap finds, listed for a person to judge into the ledger or
  not. Nothing does this now.
- **J68**: the evidence run merged `Ursprungs-Ich` and `Juna` from the
  glossary's own gloss. The ledger says two terms; `NOW.md` asks which.
- **SIMBA** — run it, at about $8?
