---
name: dspy
description: DSPy 3.3.1 as this repository uses it — what nine DSPy repositories (dspy-agent-skills, dspydantic, dspy-session, dspy-optimizer, dspy-agents, dspy-auto-gepa, braid-dspy, dspy-advanced-prompting, Agentic-Dspy-Rag) teach, checked against the installed package and sorted by the job at hand — calling a model through lmrun.py, signatures and modules, metrics that can fail, the optimizer ladder in pairs.py and what each rung costs, offline fixtures, dspy.RLM for rlm_ingest.py, retrieval for graphrag.py, optimizing a SKILL.md description with gepa.optimize_anything, trainsets, cost and traces — and which of their ideas were taken, wait for an instance, or were refused. Use before writing or changing code that imports dspy or gepa, before any model call, when choosing a module, metric or optimizer, when a DSPy error, an empty answer or a surprising score appears, and when an idea from one of those repositories is being considered.
allowed-tools: Bash(python3 scripts/*), Bash(.venv-dspy/bin/python scripts/*), Bash(scripts/install.sh:*), Bash(git:*)
---

# DSPy, as this repository uses it

Nine DSPy repositories under `netzkontrast/` were read in full on 2026-09-24,
at the commits in `references/repos.md`: four readers for `dspy-agent-skills`,
the largest, and one for each other repository or pair of them. Every fact they
contain was written down with the line it came from. The notes are in
`Plan/concept/dspy-extract_2026-09-24/`. This skill is those facts, sorted by
what an agent here is about to do. Every claim about DSPy itself was checked
against the installed package, DSPy 3.3.1 in `.venv-dspy`, and
`scripts/check_dspy_skill.py` keeps checking it.

**The skill this project needed was never a DSPy tutorial.** Every failure here
with a model has been a failure of method, not of the API. One model tied the
baseline while merging `Negentropie` with `Entropie`. An RLM reproduced the
document's own off-by-one, „vier" where five are named, which looks like a
correct answer. 94% against 82% turned out to be 16 against 14 out of 17
(`Plan/concept/skills_2026-09-17.md`). Another RLM ran out of budget and began
rebuilding the document from its own scrollback; only a parse failure kept that
from being handed over as a reading (`scripts/rlm_ingest.py`). So this skill
holds two things:

- the rules that must hold before a model's output may go anywhere, and where
  each one already exists as code;
- the DSPy knowledge needed to write the code that keeps them.

## Before any model call

The project goal puts it in one line (`GOAL.md`, rule 13): „Ein Modell schlägt
vor, es entscheidet nie, und nichts verlässt den Container ohne Ja." Scripts
hold it, and `CLAUDE.md`, *Calling a model — the DSPy toolchain*, says what each
one guarantees. What to run:

- **a DSPy model call** goes through `lmrun.call` inside
  `dspy.context(lm=lmrun.make_lm(...))`. It refuses a cached LM and a real LM
  without `approval=`, and records one line per call under
  `Plan/runs/<subject>/lm/` with a status, never a score;
- **a third-party tool, or a call outside DSPy**, goes through
  `scripts/route.py`: free models only, the consent file of decision 007, and
  every call recorded so it replays offline;
- **a dry run** goes through `lm_fixture.offline(FixtureLM(...))`, which cannot
  reach the network;
- **a scored run** becomes a row through `baseline.py`, and
  `python3 scripts/baseline.py compare <task>` says whether it beats the floor;
- **`python3 scripts/selftests.py`** runs every check, one line each, and a
  suite that could not run says `not run`, never `held`.

**Nothing leaves the container without the author's yes for that run.** Three
DSPy runs are built and waiting on one: `pairs.py run --optimizer labeled
--rule plural`, `graphrag.py ask --answer`, and `rlm_ingest.py`. `NOW.md` says what each would
send. Decision 007 lets documents 5 and 6 go to free models and Jev through
`route.py`, to test the tools installed that day; it says nothing about these
three. The rule has three encodings — `lmrun.py`, `rlm_ingest.py`, `route.py` —
and which one the others should call is open (`NOW.md`). The dry run of each
DSPy run is free:

```bash
.venv-dspy/bin/python scripts/pairs.py run --optimizer labeled --dry-run
.venv-dspy/bin/python scripts/graphrag.py ask "Nexus Überraum" --answer --dry-run
python3 scripts/selftests.py                 # every suite, one line each
```

A cloud session builds `.venv-dspy` at start, through `scripts/install.sh`:
DSPy 3.3.1 with numpy (SIMBA raises without it) and Deno (`dspy.RLM`'s
sandbox), `dspy-skills` and `drg-kg`. By hand:

```bash
scripts/install.sh --check dspy    # present or not, changes nothing
scripts/install.sh dspy            # build it
```

## Where to look, by what you are about to do

| you are about to | read | run |
|---|---|---|
| call a model at all | `references/operations.md` | `lmrun.call` inside `dspy.context(lm=lmrun.make_lm(...))`; a third-party tool: `route.py` |
| write or change a signature, a module, an adapter | `references/api.md` | `check_dspy_skill.py` |
| write a metric, a judge, a scorer | `references/metrics.md` | `baseline.py selftest` |
| choose or run an optimizer | `references/optimizers.md` | `pairs.py score`, then `pairs.py run --dry-run` |
| build a trainset, split it, fold it | `references/data.md` | `trainset.py` |
| write an offline test or a dry run | `references/testing.md` | `selftests.py` |
| read a long document with `dspy.RLM` | `references/rlm.md` | `rlm_ingest.py --selftest` |
| retrieve, rank or answer from the wiki | `references/retrieval.md` | `graphrag.py ask`, `graphrag.py bench` |
| optimize a SKILL.md or other text | `references/text-artifacts.md` | `check_skills.py` |
| record cost, trace, save, cache, handle errors | `references/operations.md` | `lmrun.py` |
| borrow a pattern: review, critique→repair, sessions, planning graphs, prompting techniques | `references/patterns.md` | — |
| weigh one of the nine repositories, or one of its ideas | `references/repos.md` | — |

## The facts that bite

Each is checked against DSPy 3.3.1 or cited to its source, in the file named.

1. **`dspy.LM` caches by default**, so a repeated call replays its first answer
   and repeats measure nothing (P18). `lmrun.make_lm()` builds its LM with
   `cache=False`, and `rlm_ingest.py` builds its own the same way. → `api.md`
2. **`dspy.Evaluate` reports a percentage, and scores a crash as a wrong
   answer**: `failure_score` 0.0, counted in the mean. An unreachable model scores
   0% (P15). [checked: evaluate-failure-is-zero] Nothing here reads its aggregate
   as a measurement. → `api.md`, `metrics.md`
3. **A metric returns `dspy.Prediction(score=…, feedback=…)`, never a dict.** A
   dict crashes `Evaluate`. [checked: metric-dict-crashes] → `metrics.md`
4. **`bool(dspy.Prediction(score=0.0))` is `True`.** So `BootstrapFewShot`,
   given a Prediction-returning metric, keeps every wrong demo.
   [checked: bootstrap-keeps-wrong-demos-on-prediction] Hand `.score` to the
   bootstrap family; only GEPA takes the Prediction, which is what `pairs.py`
   does. → `optimizers.md`
5. **GEPA needs `reflection_lm` at construction**
   [checked: gepa-asserts-reflection-lm], and `auto="light"` means about
   380 + 4 × valset metric calls for one predictor.
   [checked: gepa-light-budget] Without a valset it selects on the trainset. →
   `optimizers.md`
6. **`InferRules` without a valset uses the first half of the trainset for rules
   and the second half to choose among them, in the order given.**
   [checked: inferrules-halves-trainset] **`SIMBA` refuses a trainset smaller
   than `bsize`** (32 by default). [checked: simba-trainset-below-bsize] →
   `optimizers.md`
7. **A `Literal` output field is enforced by the adapter.** A value outside it is
   an unparseable answer, not a wrong one, and `lmrun` records it as `unparsed`.
   [checked: literal-out-of-set-unparsed] → `api.md`
8. **An answer `ChatAdapter` cannot parse is retried through `JSONAdapter`, at the
   cost of a second call.** [checked: chat-adapter-json-fallback] → `api.md`
9. **DSPy 3.3 raises its own error types.** A refused connection arrives as
   `dspy.LMTransportError`. [checked: refused-connection-is-transport-error]
   `lmrun.call` re-raised these instead of recording `unreachable` until
   2026-09-24. → `api.md`, `operations.md`
10. **`dspy.RLM` needs Deno, and it answers even when it did not finish.** When
    `max_iters` runs out it builds an answer from the trajectory, marked only by
    `final_reasoning == "Extract forced final output"`.
    [checked: rlm-forced-final-output] `rlm_ingest.py` calls that a
    reconstruction. → `rlm.md`
11. **`Refine` and `BestOfN` return `None` when every attempt fails and N ≤ 2.**
    [checked: refine-none-when-all-fail] → `patterns.md`
12. **`dspy.load` refuses a pickled program unless `allow_pickle=True`, and a
    saved program carries no API key.** [checked: load-refuses-pickle] →
    `api.md`, `operations.md`
13. **`gepa.optimize_anything` hands the evaluator its example by keyword,
    `example`.** An evaluator whose parameter has another name never receives
    it. [checked: example-reaches-evaluator-by-name] → `text-artifacts.md`

## The finding that repeats across the nine repositories

**Most of them contain a check that cannot fail**, each in a different costume.
Some score an empty input as a pass. Some fold a parse failure into 0.5. Some
count keywords in the model's own words. Some compare a run only with the one
before it. This project's founding defect was a coverage term that returned 1.0
when given no gold, and it turns out to be what evaluation code looks like by
default. `references/metrics.md` has the table, one row per repository with the
line. The consequence here is not new doctrine: every metric ships with a case in
which it must fail, and with a third state, *could not score*, that never becomes
0 or 1 (P15, P23).

## What this skill may not do

- Send corpus text to any model without the author's yes for that run. The
  scripts refuse it without an approval; the skill does not route around them.
- Let a model's output into `Sources/` or `Wiki/`, decide a near match, detect a
  conflict, infer a link, or merge two readings. Where a pattern from the nine
  repositories does one of these, `patterns.md` says so and it is not taken.
- Install one of the nine repositories as a dependency. Every reader reached the
  same conclusion for its own repository: the value is a pattern of tens of
  lines, and the package would bring a pin, a floor or a runtime this project
  does not need.
- Restate what a script enforces (P6). It says: run this, here is what the
  output means.

## Provisional

```yaml
name: dspy              # provisional
# may not: send corpus text anywhere, write into Sources/ or Wiki/, decide a
#          near match or a conflict, or mark a DSPy behaviour [checked] when
#          no probe runs it
# retire when: a DSPy upgrade leaves more probes failing than holding, then
#          rewrite it from the installed package rather than patch it
```
