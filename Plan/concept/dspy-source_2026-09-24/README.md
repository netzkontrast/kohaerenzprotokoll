# What DSPy 3.3.1 and GEPA 0.1.4 themselves contain — the readers' notes, 2026-09-24/25

The `dspy` skill (`.agents/skills/dspy/`) was built from nine third-party
repositories that use DSPy (`Plan/concept/dspy-extract_2026-09-24/`), and
checked against the installed package wherever a probe could run. Nobody had read
DSPy itself. The author asked for „all there is about dspy", so nine readers read
the **primary sources**: the installed DSPy 3.3.1 package, its tests and its
official documentation (git tag `3.3.1`), GEPA 0.1.4 (tag `v0.1.4`), and the
papers behind both. Each was given `00-brief.md`, one slice, and the skill's
matching reference file as its map, and asked for every fact with its line and,
for each, whether the skill has it, has it wrong, or has it without a check.

| file | slice | reader |
|---|---|---|
| `programming-model.md` | signatures, primitives, `dspy/core/types.py`, settings, saving | Sonnet |
| `modules.md` | `dspy/predict/` — `RLM`, `Flex`, `ReAct`/`ReActV2`, `Refine`, `BestOfN`, `Parallel` … — and the Deno interpreter | Sonnet |
| `lm-and-retrieval.md` | `dspy/clients/`, `dspy/retrievers/`, the cache, usage, history | Sonnet |
| `adapters-and-types.md` | `dspy/adapters/` and its types, `dspy/streaming/` | Sonnet |
| `runtime-eval-data.md` | `dspy/evaluate/`, `dspy/datasets/`, callbacks, the parallelizer, exceptions | Sonnet |
| `optimizers-classic.md` | `dspy/teleprompt/` except GEPA, `dspy/propose/` | Sonnet |
| `gepa-core.md` | `dspy/teleprompt/gepa/` and GEPA's engine, proposers, strategies, adapters | Sonnet |
| `gepa-anything.md` | `gepa.optimize_anything`, gskill, the other adapters, „Claude CLI as proposer" | Sonnet |
| `research.md` | the papers (DSPy, Assertions, MIPRO, BetterTogether, GEPA, LangProBe, RLM, mmGRPO), GEPA's blog, DSPy's community pages | Sonnet, with the web |

## How to read them

- **They are notes, not the skill.** Each item carries its `path:line` in the
  tagged source tree and a tag — `[api]`, `[recipe]`, `[number]`, `[trap]`,
  `[pattern]`, or `[claim]` where the documentation asserts something the reader
  could not find in code — and a `skill:` field: `new`, `wrong`, `unchecked` or
  `same`. Paths are relative to the tag's root (`dspy/…`, `docs/docs/…`,
  `gepa:src/gepa/…`); the clones themselves are not kept, and the installed
  package is the same code (`diff -rq`, 2026-09-24).
- **Where a note and the skill disagree, the skill has been re-run against the
  installed package; the note has not.** On 2026-09-25 the skill took from these
  notes what bore on this repository's own code, each with a probe in
  `scripts/check_dspy_skill.py` where one could run: `rollout_id` changes the
  cache key at temperature 0 too, and the skill had it backwards
  (`rollout-id-busts-cache-at-zero-temperature`); GEPA's own cost tracking is 0.0
  for any callable (`gepa-tracking-lm-cost-inert`); a bad `gepa_kwargs` key raises
  only at `.compile()` (`gepa-kwargs-fail-at-compile`); and the skill's „both
  adapters raise `AdapterParseError`" was wrong for the JSON fallback
  (`json-fallback-literal-is-valueerror`).
- **Every reader ran with every `*_API_KEY` unset** and no real LM; probes used
  `scripts/lm_fixture.py` or monkeypatched `litellm.completion`.
- **The readers were cut off once.** On 2026-09-24 all nine hit the account's usage
  limit within the hour; `research.md` had been written by then, the other eight
  were resumed the next morning from their own transcripts, in two batches.

## What the read changed in this repository

- **The skill** — the three corrections above, the two model routes of decision
  011, and the facts that bite about the Claude CLI.
- **`scripts/claude_lm.py`** was compared against GEPA's documented „Claude CLI
  as proposer", which is prose only in 0.1.4 and would run in the project
  directory, loading `CLAUDE.md` into every prompt (`gepa-anything.md`).
- **`pairs.py`'s cost accounting** sums DSPy's own LM history rather than
  anything GEPA reports, because GEPA reports 0.0 (`gepa-core.md`).
- **`lmrun.call` recorded an unparseable answer as a crash.** `JSONAdapter.parse()`
  lets a value outside a `Literal` escape as a bare `ValueError`, and `ChatAdapter`
  falls back to it by default — this repository's own configuration. `call()`
  re-raised it, so one such answer would have ended a run; it now records
  `unparsed`, and its selftest carries the case (`adapters-and-types.md`).
- **`claude_lm.py` dropped image and audio parts without a word**; it refuses
  them now (`adapters-and-types.md`).

## What they found that nothing here acts on yet

Kept so the next change that touches one of these starts from the note, not from
memory:

- `dspy.Evaluate` throws away which examples raised: a crash becomes an empty
  `Prediction` at `failure_score`, indistinguishable from a wrong answer, and the
  documentation calls that a feature (`runtime-eval-data.md`) — why `pairs.py`
  scores held-out pairs through `lmrun.call`, never `Evaluate`.
- `LabeledFewShot` and `BootstrapFewShot` return every predictor with `.lm =
  None`, even after `set_lm()` (`optimizers-classic.md`).
- `.finetune()` on an `openai/` model reaches the real OpenAI API whatever
  `api_base` says (`lm-and-retrieval.md`) — the one path in this slice by which
  text could leave for a provider `route.py` does not see.
- `dspy.ProgramOfThought` and `dspy.CodeAct` are deprecated in 3.3.1; `ReActV2`
  becomes `ReAct` in 3.5 (`modules.md`).
- SIMBA's `append_a_rule` sends each example's gold label to its reflection
  model, and samples at temperature 1.0 whatever the LM says
  (`optimizers-classic.md`).
- `dspy.RLM` is marked experimental in its docstring and warns nowhere at
  runtime; `rlm_ingest.py` is built on it (`programming-model.md`).
- A string signature resolves a custom type by walking up to 100 stack frames,
  and `Signature.load_state` matches fields by position, not name
  (`programming-model.md`).
- `dspy/core/types.py` is the typed `LMRequest`/`LMResponse` contract a custom LM
  can declare with `forward_contract = "typed_lm"`; `claude_lm.py` and
  `lm_fixture.py` use the legacy one, which DSPy keeps through 3.4
  (`programming-model.md`, `lm-and-retrieval.md`).
- The only published InferRules result near this repository's scale is a null
  result at n = 60 (`research.md`) — and the ladder's own InferRules run did not
  beat Bootstrap either (`Plan/concept/dspy-optimization_2026-09-25.md`).
