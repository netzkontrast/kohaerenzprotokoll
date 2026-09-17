# The ledger was already a trainset, and a free model already beats the rule

**Date:** 2026-09-17.

## The claim being tested

*RLM optimises the calls when you use an optimizer, so it can only get better —
you just need training data.*

Correct, and the second half is where this project stands. So: what gold data
exists, what does the existing deterministic code score on it, and does a model
beat that?

## What exists

`Plan/runs/judgements.jsonl` was written for a different purpose — keeping
mechanised rules replayable. It turns out to be a labelled dataset, and an
unusually well-shaped one:

| | |
|---|--:|
| labelled examples (`one-term` / `two-terms`) | **17** |
| of those, carrying a stated rule in words | **17** |
| distinct `env_features` | 29 |

**Every record says in words why.** GEPA's row in the optimizer table asks for
exactly that — *"failures can be described in words, not just scored"* — and
names no example count. The ledger was written that way by accident of a
different requirement.

## The baseline, measured before spending anything

The rule already in the repository, `fold()` equality, on those 17:

**14/17 = 82%.** The three misses are not bugs:

| id | pair | why `fold()` will not decide it |
|---|---|---|
| J4 | `Kern-Welten` / `Kern-Welt` | folding is deliberately not stemming — a stemmer that merges a plural also merges `Negentropie` with `Entropie` |
| J6, J14 | `… / Nexus-Vorstufe` / `Möglichkeits-Garten` | no rule exists for a slash inside a heading |

So the 18% gap is **the boundary of what a safe deterministic rule can claim**,
which is the right place to put a model.

## The measurement

Zero-shot, no optimizer, free models, plus a held-out canary that is in no
trainset: `Negentropie` / `Entropie`, which must stay **two terms**.

| model | score | canary held | verdict |
|---|--:|---|---|
| `nex-agi/nex-n2.5-pro:free` | **16/17 = 94%** | ✅ | beats the baseline |
| `nex-agi/nex-n2.5-mini:free` | 14/17 = 82% | ❌ **merged them** | ties on score, **worse than the baseline** |
| `fold()` | 14/17 = 82% | ✅ by construction | the thing to beat |

The pro model's single miss was an unparsable answer, not a wrong decision.

**The canary earned its place immediately.** The mini model matched the
baseline's score while merging two opposites — the exact failure `fold()` is
built to avoid. A scalar would have called them equal.

## What this does and does not establish

**Does:** a zero-shot free model already beats the hand-written rule on this
task, without an optimizer, and the metric to keep it honest exists and is
deterministic. The path the claim describes is real and open.

**Does not:** 94% against 82% on **17 items is 16 right against 14** — two
examples. There is no held-out split; the canary is one case. Nothing here
justifies replacing `fold()` in the pipeline, and `scripts/trainset.py` prints
the baseline next to every result so the comparison cannot quietly go missing.

## The actual bottleneck, named

Not this task. The one that matters:

| task | usable gold | blocked by |
|---|--:|---|
| one-term-or-two | **17** | nothing — measurable today |
| extract candidate terms | **0** of 4 | every candidate list so far is a *reconstruction* written after the counts |
| is this a conflict | **0** of 5 | four conflicts and one false positive; and conflict detection is deliberately never mechanised |

Term extraction is the bulk of the work and has **no gold set at all**.
`capture.py` already refuses to count before a candidate list exists, so
**document 5 onward can produce real ones** — the first four cannot be repaired,
only outgrown.

`state.py` now derives `trainset.gold_candidate_lists`, currently **0**. That
number going up is the precondition for optimising the step that matters, and it
goes up as a byproduct of doing documents rather than as a separate project.
