# The nine repositories

One section per repository: what is in it, and what this project took. "What
is in repository X" and "what did this project take" both have one answer,
here. A repository fact is `repo:path:line`, at the commit read below
(`repo:path` alone for a whole-file pattern); a bare backtick path
(`scripts/pairs.py`) is this repository and exists. This file carries no
`[checked: …]` marks — those are DSPy behaviour, in `api.md`.

Nine readers' notes, each reading its repository whole: `das-core.md`,
`das-book.md`, `das-rlm-rag.md`, `das-patterns.md` (four slices of
`dspy-agent-skills`, split for size), `session-optimizer.md` (`dspy-session`
+ `dspy-optimizer`), `agents-rag.md` (`dspy-agents` + `Agentic-Dspy-Rag`),
`braid-prompting.md` (`braid-dspy` + `dspy-advanced-prompting`),
`dspydantic.md`, `auto-gepa.md`. **The full notes live in
`Plan/concept/dspy-extract_2026-09-24/`.** Every commit was re-verified with
`git -C /home/user/<repo> rev-parse --short HEAD` and `git log -1
--format=%ci`; all nine matched. "2026-09-23 report, corrected" is what
changed against the first scan in `Plan/concept/dspy-repos_2026-09-23/`;
`Plan/concept/dspy-toolchain_2026-09-23.md` ("the toolchain doc") is that
scan's design and what got built from it — the new notes win where the two
disagree. Six of the nine repositories also carry a check that cannot fail,
in a different costume each time (`metrics.md` has the shared shape); below,
each repository's own version, with its line.

---

## `dspy-agent-skills`

github.com/netzkontrast/dspy-agent-skills (fork of `intertwine/dspy-agent-skills`),
`9d13f98`, 2026-09-16, "Merge pull request #6 …" — MIT, © 2026 Bryan Young;
ported third-party skills carry their own licences (`README.md:201-214`).
DSPy `>=3.3.0,<3.4` (validated 3.3.1); Python not pinned, verified with
3.11.15. **Holds on 3.3.1?** Mostly — 633 tests and every dry-run pass,
`check_dspy_surface.py` says "OK," but several *taught* call shapes fail
live: `dspy.load(dir)` without `allow_pickle=True`, `save_as_json` with a
Prediction metric, `BetterTogether.compile` without `strategy=`,
`GEPA(auto=…, max_metric_calls=…)` together (measured across all four
slices: pytest, the surface check, every dry-run, ~30 offline probes —
DummyLM, `inspect.signature`, a real Deno/Pyodide sandbox).

**What it is.** Four slices of one plugin (32 skills, v0.11.0): core
API/eval/GEPA/production/retrieval skills; nine "book" chapters on
datasets/metrics/optimizers/modules/agents/production/text-artifacts; RLM
plus four third-party-wrapped skills; seven knowledge-work skills
(wiki-compile, adversarial-review, clarify, tetraframe, autodialectics,
deep-refine, reflect-loop).

**Took → lives here.** The signature-check pattern →
`scripts/check_dspy_surface.py`; the skill-metadata validator →
`scripts/check_skills.py` (`dspy-agent-skills:tests/test_skill_metadata.py`);
"a dry-run that can reach the network is not a dry-run," from watching this
scan's `dspy-auto-gepa` leak a real call; `graphrag.py`'s MMR-with-a-floor
selection, ported from `scaffolding/kp_canon_retriever.py` (itself from
`dspy-refrag`, MIT) — **corrected, not copied**: the pack's λ is the
*inverse* of upstream's, and the floor's crossover is 0.534, not "≥0.6" as
documented (`retrieval.md`); `InferRules` on `pairs.py`'s ladder, the rung
this pack names but never covers (`optimizers.md`).

**Waits / refused.** `dspy-wiki-compile`'s `decision_legal()` (weights 0.30
citations / 0.25 decisions / 0.20 merge / 0.15 diffs / 0.10 links) is the
reviewed-page rule catalogued for the first promotion — none yet. Refused:
`drg-kg`'s extraction layers (implicit relationships on by default; this
wiki never infers a link, decision 005), `dspy-rlm-hooks` (monkeypatches
private internals), TARA's progressive leniency (outputs any context at the
final retry regardless of score, P15), all 32 skills as a dependency
(pattern, not package).

**Cannot fail / never measured.**
`dspy-agent-skills:skills/dspy-wiki-compile/example_wiki_compile.py:161-163`
— `_mean([])` returns 1.0, so an empty compile scores 0.70 "clean" (T1); also
`dspy-agent-skills:skills/dspy-evaluation-harness/SKILL.md:104` — `assert
result.score >= 0.75` passes for any score ≥ 0.75%, since `.score` is 0–100.
Never measured: `dspy-agent-skills:skills/dspy-gepa-optimizer/SKILL.md`
§2.15/§3 — "20–50 well-chosen beats 500 bland": the pack's own examples show
gains inside baseline spreads as large as the gains, scored on GEPA's own
selection set, never held out.

**2026-09-23 report, corrected.** Ran nothing and trusted the dry-runs, so it
repeated the skills' own errors ("twelve optimizers" is eleven plus a
baseline). Missed that `Evaluate`, `Parallel`, `BestOfN`, `Refine`, `ReAct`
and ChatAdapter all fail *softly*. Adopted wiki-compile's and deep-refine's
scoring as templates without noting both certify exactly what P13 forbids.

**Matters most here.** (1) `.score` is a percentage; `baseline.py` compares
on 0–100 explicitly, never a raw `>= 0.75`. (2) A `dspy.Prediction` metric is
read by truthiness in the BootstrapFewShot family, so `pairs.py`'s ladder
hands that family `.score`, never the Prediction. (3) A dry-run that never
imports `dspy` cannot see a live-path defect; every dry-run here runs against
`.venv-dspy`.

---

## `dspydantic`

github.com/netzkontrast/dspydantic (upstream `davidberenstein1957/dspydantic`).
Read at `1afc528`, 2026-03-20, "fix: validation leakage and unfair baseline
causing inflated 100% metrics (#23)" — license contradictory: `LICENSE`/README
say Apache-2.0, `pyproject.toml` says MIT. DSPy `>=3.0.4`; Python `>=3.11`
(docs say "3.10+"). **Holds on 3.3.1?** Core calls work and the offline unit
suite passes, but several *default* paths break end to end: image/PDF fields
(`Image.from_url` rejects data URIs), the auto-optimizer at n≥20 and n≤2
(needs `optuna`), `optimizer="gepa"` (3-arg metric vs. GEPA's 5). Measured
with a `git archive` copy, pytest under an offline plugin, seven driver
scripts and ten inline checks.

**What it is.** Tunes Pydantic `Field(description=…)` strings for LLM
structured extraction via a per-field `ChainOfThought` rewriter, scored by a
*separate* extraction call compared field by field.

**Took → lives here.** No code installed — one task is on the optimizer
ladder so far, so its ideas are catalogued below. "Check every DSPy kwarg
against `inspect.signature` before running" is already `check_dspy_surface.py`'s
rule, and dspydantic is the sharpest evidence why.

**Waits / refused.** An evaluator registry (`EvaluatorFactory`) waits for a
second evaluator in use (`metrics.md`); optimizer-chosen-from-`n` waits for a
second task on the ladder (`optimizers.md`); contextual signature class names
wait for job 4 underperforming and need re-deriving even then, since a class
name never reaches the 3.3.1 prompt, measured (`text-artifacts.md`). Refused:
installing dspydantic itself (pattern, not package, plus the licence
conflict) and its list-of-model scoring rule specifically (the vacuous shape
below is what this project's metrics ship a failing case against).

**Cannot fail / never measured.**
`dspydantic:src/dspydantic/evaluators/functions.py:437-446,551-553` — a
list-of-model field always scores 1.0 (`None`/`None` at the leaf); the note
calls this "a check that cannot fail" outright. Never measured:
`dspydantic:ABLATION_RESULTS.md`, backed by
`dspydantic:examples/ablation_benchmark_mock.py:169` ("We're not actually
running optimize()") — every headline gain hardcodes its score and errors on
3.3.1 before producing any.

**2026-09-23 report, corrected.** "134 tests, all pass" was `tests/unit`
only — `pytest tests` gives 1 failed / 160 passed / 15 skipped. Missed that a
custom `evaluate_fn` is silently replaced whenever examples carry labels —
the regression this commit claims to fix.

**Matters most here.** (1) Hunt for checks that cannot fail — this project's
per-metric `selftest.py` case exists because of exactly this shape
(`metrics.md`, P23). (2) A signature's class name does not reach the DSPy
3.3.1 prompt — only the docstring and `field_name` do (`api.md`). (3) Score
the exact artifact you return, cache off — single-pass mode here scores a
different sample than it returns, agreeing only via cache hits
(`operations.md`, P18).

---

## `dspy-session`

github.com/netzkontrast/dspy-session (upstream `maximerivest/dspy-session`).
Read at `eb67e76`, 2026-02-26, "docs: add implementation examples for
Approach 2 … Approach 3 …" — license MIT, © 2026 Maxime Rivest. DSPy `>=2.6`
(`uv.lock` pins 3.1.3); Python `>=3.10`. **Holds on 3.3.1?** Imports and its
suite pass (102/1 skipped, offline), but three behaviours break: wrapping
`dspy.RLM` now raises `ValueError` immediately; a deep-copied or forked
`Session` still calls the *original* predictor, so an optimizer compiling
one gets 0 demos; composed programs get `None`-filled history for unmatched
fields.

**What it is.** Wraps any `dspy.Module` in `Session(dspy.Module)`; records
every call as a `Turn`, builds `dspy.History` from past turns, injects it
into nested predictors via a contextvar. `with_memory`/`SessionState` add
per-node and per-user state.

**Took → lives here.** No code installed. `lmrun.py`'s rule — freeze inputs,
raw output and status at call time, never reconstruct later — is this repo's
`Turn` shape (`dspy-session:dspy_session/session.py:61`, a plain *mutable*
`@dataclass`), kept as the idea, not the class: nothing here is multi-turn,
and `lmrun.py` already records per call.

**Waits / refused.** None waits — nothing here has a multi-turn surface for
`Session`/`with_memory` to wrap. Refused: wrapping `dspy.RLM` in a
History-carrying session at all (the repo's own `docs/rlm.md` records RLM
failing every iteration on 3.1.3, and 3.3.1 raises immediately;
`rlm_ingest.py` calls plain `dspy.RLM`); the whole Session apparatus as a
dependency (the pattern, not the package).

**Cannot fail / never measured.** `dspy-session:dspy_session/session.py:1085-1109`
— `session.score()` with `gold=None` builds labels from the turn's own
outputs, so a label-comparing metric compares a prediction with itself and
scores 1.0 trivially. No ABLATION-style number exists here; the closest is a
doc claim that mlflow "logs `turn_score`," which the committed `mlflow.db`
shows it never does.

**2026-09-23 report, corrected.** Said a real API key was baked into old
output — wrong, no key exists anywhere (grepped). Called `Turn` "immutable"
— it is a mutable dataclass and `score()` writes into it, and `override`
"the optimizer path" without noting `BootstrapFewShot.compile(session)`
still calls the *original* predictor, ending with 0 demos.

**Matters most here.** (1) A wrapped predictor keeps calling the *original*
object after `deepcopy`/`fork()`/an optimizer's copy — optimize an unwrapped
module instead. (2) Never wrap `dspy.RLM` in a History injector; on 3.3.1 it
raises immediately (`rlm.md`). (3) An RLM answer can be a forced fallback —
check `final_reasoning == "Extract forced final output"`, the same check
`rlm_ingest.py` makes.

---

## `dspy-optimizer`

github.com/netzkontrast/dspy-optimizer. Read at `a07b3b7`, 2025-07-27, "test:
fix tests with updated strategies" — license MIT, © 2025 Niels van Galen
Last. DSPy `>=2.6.27` (`uv.lock` pins 2.6.27); Python `>=3.12`. **Holds on
3.3.1?** The code and 38 of 43 tests run unmodified; the other 5 (MLflow)
need `mlflow` installed — with mlflow 3.16.1 all 43 pass. Measured across
four environments plus probes for MockLLM calls, scorers, validators and
loop events.

**What it is.** An Evaluator→Refiner→Merger→Validator loop (~700 lines)
patching one `### Block`-structured prompt *string*; not a DSPy teleprompter.
Its flagship `examples/dutch_invoices/` example does not exist in any of its
25 commits.

**Took → lives here.** `MockLLM`'s shape (a `dspy.BaseLM` subclass returning
scripted completions) → half of `lm_fixture.py`
(`dspy-optimizer:tests/conftest.py:9`). `HistoryCallback`'s one-dict-per-hook
shape → `lmrun.py`'s per-call JSONL record
(`dspy-optimizer:dspy_optimizer/callback/history_callback.py:8-59`).

**Waits / refused.** None waits — both shapes taken are already built.
Refused: the Evaluator/Refiner/Merger/Validator loop as a whole — not a
teleprompter, no held-out validation set (it validates against the data it
optimizes), and its flagship example was deleted from the repository while
two READMEs still describe it as present.

**Cannot fail / never measured.**
`dspy-optimizer:dspy_optimizer/strategies/validation/sample.py:60-74` —
`full`, `batched` and `sample` all accept a candidate on an empty dataset;
`sample`'s own comment says so: `return {"is_valid": True, "score": 1.0} #
Vacuously true`. Never measured: `dspy-optimizer:README.md:74-78,153` and
`DESIGN.md:83-87` call `examples/dutch_invoices/` "Complete, end-to-end
example" — no `examples/` path exists in any of the 25 commits, though a
real, deleted 380-line version survives in git history at `19fb8d2`.

**2026-09-23 report, corrected.** Called the 43 tests "against a hand-rolled
MockLLM" — many use fakes or MagicMock instead, and 5 fail outright without
mlflow. Said the numeric scorer "normalises European formats" — it strips
every comma, so `"80,50"` parses to 8050.0. Missed that a model-typed
identifier (`PatchOperation("Append")`) crashes the run uncaught.

**Matters most here.** (1) A validator that passes on an empty dataset is the
same shape as `dspy-agents`' skipped-metric monitor below — `baseline.py`'s
"never let *could not check* collapse into *ok*" rule covers both (P23). (2)
Any identifier a model writes into a typed slot needs to be a `Literal` built
by code, or a free string crashes or mis-patches the run — `pairs.py`'s
`Literal["one-term","two-terms"]` is the same lesson. (3) A test that fakes
`forward` stays green while rendering is broken — assert on
`lm.history[-1]["messages"]` instead (`testing.md`).

---

## `dspy-agents`

github.com/netzkontrast/dspy-agents. Read at `fde0dad`, 2025-09-26, "Re-run
compile/eval after dataset expansion" — no licence file, default copyright,
pattern only. DSPy `dspy-ai>=3.0.3,<4.0` (resolves to 3.3.1 today); no
`pyproject.toml`, Python unpinned. **Holds on 3.3.1?** Everything it
constructs runs offline, with two exceptions: `dspy.load(path)` raises
without `allow_pickle=True` and every caller swallows the error, so the
compiled program is silently never used; `OPENAI_MAX_OUTPUT_TOKENS` does
nothing. Measured across six venvs, a `CountingFillLM(DummyLM)` fixture
running MIPROv2 light, and direct `dspy.LM` construction with the repo's
kwargs.

**What it is.** An Agno AgentOS "Researcher" agent whose tools call one
`ChainOfThought` compiled once with MIPROv2 on a 50-row QA set, with a
SQLite/Postgres baseline-drift monitor and hybrid retrieval around it.

**Took → lives here.** The append-only, floor-compared ledger →
`baseline.py`/`Plan/runs/baselines.jsonl`
(`dspy-agents:dspy_optimize/baselines/{store,monitor,thresholds}.py`), with
its central defect fixed (below); usage/cost-per-call logging → `lmrun.py`
(`dspy-agents:dspy_optimize/compile_rag.py:85-87`); its `RecorderLM` → the
construction-check half of `lm_fixture.py`
(`dspy-agents:tests/test_dspy_config.py:13-122`) — **corrected**, since a
recorder proves DSPy accepted kwargs syntactically, never what it did with
them, so `check_dspy_surface.py` also does one real `dspy.LM(...)`
construction; hashing what a program *is*, not a bumped tag →
`baseline.py`'s `program_hash`.

**Waits / refused.** Per-directory `AGENTS.md` files wait for a directory an
agent here keeps misreading; content-hash cache invalidation waits for any
cached derived output. Refused: the drift monitor's *relative-only*
comparison specifically (`baseline.py` compares against a floor too,
precisely because this one cannot) and Agno/AgentOS/FastAPI wholesale —
nothing here is served.

**Cannot fail / never measured.**
`dspy-agents:dspy_optimize/baselines/thresholds.py:186-187` — `if
current_value is None: return None` skips the rule silently, and its own
test pins the consequence: `dspy-agents:tests/test_baselines_monitor.py:164-179`
(`test_empty_thresholds_disable_checks`) asserts `em_rate=0.0` with `{}`
thresholds is `"ok"`. Never measured: `dspy-agents:README.md:56` — "~28
doc-grounded Q/A pairs"; the dataset has held 50 rows since commit
`8cc8eaf`, and nothing re-derives the documented count against the file.

**2026-09-23 report, corrected.** Read `"total_calls": 0` as "the model was
never called meaningfully" — it is a dead counter, never incremented on
either DSPy version. Said there is "no absolute floor check" — there is one
for the eval but not the compile step, so a compile scoring 0.0 is "ok".
Missed the `dspy.load` break entirely, so its own recommendations would
silently never exercise the compiled program.

**Matters most here.** (1) A drift monitor that skips unmeasured metrics and
compares only with the (always-stored) previous run passes a broken pipeline
forever; compare against a floor and a pinned best (`baseline.py`). (2)
`dspy.load(path)` raises without `allow_pickle=True` from 3.1.0 on; never
wrap it in a bare `except` (`api.md`). (3) `import numpy` before `import
dspy` on 3.3.1, or a later `numpy.typing`/`pyarrow`/`lancedb` import fails —
reproduced in this project's own `.venv-dspy` too.

---

## `dspy-auto-gepa`

github.com/netzkontrast/dspy-auto-gepa (fork of `thememium/dspy-auto-gepa`).
Read at `80a5402`, 2026-07-04, "chore(uv): update version" — license MIT.
DSPy `>=3.2.1` (`uv.lock` pins gepa 0.0.27); `requires-python>=3.12`, but the
code parses and its suite passes on 3.11. **Holds on 3.3.1?** Yes, for every
DSPy call it makes — verified end to end: `AutoGEPA.run()` with fixture LMs,
131 of 132 tests offline, `inspect.signature` against 3.3.1/3.2.1/3.1.0.

**What it is.** A thin wrapper (3,493 lines) turning `rows + dspy.Module`
into `dspy.Example`s; has an LLM (default `dspy.RLM`) draft a metric `.py`
file unless `metric=Path` is given; runs `dspy.GEPA(auto="light")`; compares
baseline vs. optimized.

**Took → lives here.** Confirmation of the 5-argument
`dspy.Prediction(score, feedback)` metric contract, checked at GEPA
construction → `pairs.py`'s metric shape
(`dspy-auto-gepa:src/dspy_auto_gepa/metric_builder.py:12-13,61`,
cross-checked against `dspy-agent-skills`). The `metric=Path(...)` bypass,
taken as the *only* path used — a person writes the metric, never a model.

**Waits / refused.** None waits — the one idea worth porting is already how
`pairs.py` is built. Refused: letting a model draft the metric (its own
few-shot examples are the evidence — 2 of 3 crash on any non-empty answer,
and its own AST guard cannot catch either) and RLM-drafted generation
generally (its unmocked test still reaches OpenRouter at this commit,
reproduced, blocked by this project's offline guard).

**Cannot fail / never measured.**
`dspy-auto-gepa:src/dspy_auto_gepa/metric_builder.py:245-271`
(`_validate_metric_source`) — never executes the metric; passes a bare float
with `dspy.Prediction` only in a comment, `return dict(score=...)`, and both
crashing example metrics. Never measured: `dspy-auto-gepa:README.md:42` —
"saving them as reproducible `.py` files": generation runs against a
cache-on LM by default, so reproducibility was never actually checked.

**2026-09-23 report, corrected.** Called the AST validator "a genuinely good
guard" — it cannot fail on the common defects, and never runs the metric.
Said `force=True` retrains — `log_dir` is resume state, so a cached run
reloads instead. Missed that `val = val or test` makes GEPA's own selection
set the test set it reports the gain against; a real 0.5→1.0 gain was
reported as `improvement=0.0` on a one-row test split.

**Matters most here.** (1) Never select on the set you report on — `val =
val or test` silently makes GEPA's Pareto set the test set (`optimizers.md`).
(2) A metric that raises becomes a silent zero in both `Evaluate` and GEPA,
which then spends its whole budget and returns the seed program unchanged —
execute a candidate metric on sample rows first (`metrics.md`). (3)
`dspy.LM` caches by default and this wrapper never turns it off;
`lmrun.make_lm()` is the fix already here (P18).

---

## `braid-dspy`

github.com/netzkontrast/braid-dspy (metadata points to `ziyacivan/braid-dspy`).
Read at `c50c5b1`, 2025-12-20, "Bump version to 0.2.3 …" — license MIT,
"Braid-DSPy Contributors"; version drifts internally (0.2.3 vs. 0.1.6 in
`setup.py`). DSPy `dspy-ai>=2.0.0` (`uv.lock` resolves 2.6.27/3.0.4 by Python
version); `requires-python>=3.9`. **Holds on 3.3.1?** The library works — all
185 tests pass offline (5.65s), and a DummyLM runs planning plus execution
end to end. The *documented usage* does not: `dspy.OpenAI` no longer exists,
bare `MIPROv2()` needs a metric, 11 of 11 documented snippets fail as
written.

**What it is.** One `dspy.Predict` writes a plan as a Mermaid flowchart;
code parses and orders it with Kahn's algorithm; a second `Predict` executes
each node. Regex "protocol" modules (masking, a critic, cost metrics) sit
around it, mostly unused.

**Took → lives here.** Nothing installed, no line ported. Its one durable
idea — validating a model-written procedure graph *before* executing any
step — is catalogued, not taken, because nothing here has a procedure whose
order is in dispute yet.

**Waits / refused.** "A procedure as a checked graph" (Kahn's algorithm on a
Mermaid plan, validated before any step runs) waits for a contested
procedure; `account.py`'s decompositions are the named candidate
(`patterns.md`). Refused: the wrapper as a whole — its Kahn's-algorithm
order silently drops every node on or after a cycle while `valid` still
reads `True`, and its default metric scores a wrong answer, an
unreachable-LM error string, and a right answer all near 1.0.

**Cannot fail / never measured.** `braid-dspy:braid/module.py:214-237` — a
per-step exception is caught and stored as the step's own answer, dropped
from `reasoning_steps`, while `valid` stays `True`. Never measured:
`braid-dspy:README.md:13` ("significantly improves reliability … compared
to traditional Chain-of-Thought") — no benchmark result exists anywhere in
the repository; its only cited source is a vendor blog post, not a paper.

**2026-09-23 report, corrected.** Called the library "not verified against
DSPy 3.3.1" — now verified, all 185 tests pass, only the docs use
`dspy.OpenAI`. Praised `BraidOptimizer` as "a clean wrapper of DSPy
optimizers" — it compiles `module.plan`, which the default `forward` never
calls, so every optimization is a no-op on the path that actually runs.
Missed that a retry with identical inputs is a cache hit (3 retries, 1 real
completion).

**Matters most here.** (1) A metric must be able to fall — `_default_metric`
scores a wrong answer near 1.0; every metric here ships a case it must fail
(P23). (2) Optimize the predictor your program actually calls — check
`named_predictors()` (`optimizers.md`). (3) A retry under DSPy's default
request cache replays the same answer; `lmrun.make_lm()`'s `cache=False` is
why repeats here measure something (P18).

---

## `dspy-advanced-prompting`

github.com/netzkontrast/dspy-advanced-prompting (README clones `evalops/…`).
Read at `facc1ad`, 2026-04-11, "Update org references from haasonsaas to
evalops (#1)" — license MIT, "Jonathan Haas". DSPy `dspy-ai>=2.4.0`; Python
`>=3.8`. **Holds on 3.3.1?** Everything imports; every DSPy call pattern
works under DummyLM. Its non-LM code is less clean: a regression runner
crashes on its second run, and the `tests/` directory the README claims does
not exist at this commit.

**What it is.** Eleven "techniques," each wrapping one or more
`ChainOfThought` calls around a long instruction *text* passed as an **input
field** (not a signature instruction), with hardcoded "results" around them.

**Took → lives here.** Named for `pairs.py`'s demo selection, not yet
separately coded: the few-shot quality-tier idea — force known-hard
near-matches into every fold
(`dspy-advanced-prompting:src/techniques/few_shot.py:16-20,42-47,78-107`),
the one technique the note calls "a mechanism rather than prompt text." This
project's labelled pairs already contain that shape (`Kern-Welten`/`Kern-Welt`,
`Negentropie`/`Entropie`) (`data.md`).

**Waits / refused.** The hard-negative wiring above waits on `pairs.py`'s
first real-model run; the ladder is `--dry-run` only today. Refused: the
other ten techniques wholesale — each either passes instructions as an
input field no optimizer can reach, or is a keyword/substring check standing
in for a measurement (`patterns.md`, read but not run).

**Cannot fail / never measured.**
`dspy-advanced-prompting:src/evaluations/evaluation_framework.py:77-89,226-268,270-278`
— `edge_case_performance`, `robustness_score`, precision/recall and
`test_coverage` all default to 1.0 on nothing; three FUNCTIONAL tests that
all fail score **0.70** overall. Never measured:
`dspy-advanced-prompting:README.md:89-98` — "FULLY VALIDATED … functional
with real LLMs": the offline "validation" it points to makes no LM call at
all.

**2026-09-23 report, corrected.** Said every module "runs its non-LM code
paths" — the regression runner crashes on its second run, and the suite's
own `custom_evaluator` tests can never pass (a contract mismatch). Praised
the escape-hatch detector without finding its HIGH/UNABLE phrases are
capitalized while the text is lowercased first, so "I don't know" scores
0.95 confidence.

**Matters most here.** (1) Vacuous metric defaults compound — five different
metrics default to 1.0 on nothing, so a 0%-accuracy suite still scores 0.70
overall; every metric here needs its own all-fail case (`metrics.md`, P23).
(2) Keyword and substring checks are not verification. (3) Text passed as an
input field is invisible to every DSPy instruction optimizer; a rule belongs
in `signature.instructions` (`api.md`).

---

## `Agentic-Dspy-Rag`

github.com/netzkontrast/Agentic-Dspy-Rag. Read at `474f107`, 2025-06-18, "m"
— no licence. DSPy unpinned — no `requirements.txt`; the README's own
install line (`"pydantic<2"`) resolves to `dspy-ai==2.3.1`, which predates
`dspy.LM`. Python: README creates a 3.10 env, but its own OCR dependency
needs ≥3.11. **Holds on 3.3.1?** Yes, offline with fakes — the orchestrator
and FastAPI endpoint both ran end to end — but only if `numpy` is imported
before `dspy` (reproduced in this project's own `.venv-dspy` too). The
*documented* setup cannot start at all.

**What it is.** A FastAPI `/query` endpoint: an intent classifier, then
**substring** routing to Simple/Comparative/MultiStep RAG (`ChainOfThought`s),
then Qdrant retrieval with an embedding rerank. No tests exist anywhere.

**Took → lives here.** The shape, not the code: classify → route → quote,
never synthesize → `graphrag.py`'s `answer()` (P13 — its own MultiStepRAG
merges sources into unattributed prose, the operation `graphrag.py` refuses;
`retrieval.md`). The refusal of substring routing → `pairs.py`'s
`Literal["one-term","two-terms"]`, chosen because this repo's `"Comparative"
in user_intent` misroutes 6 of 8 tested paraphrases silently.

**Waits / refused.** None waits beyond what is already built — `ask` and
`bench` exist in `graphrag.py` today. Refused: the code itself, entirely —
substring routing, unattributed synthesis, usage logging that always prints
"Model: unknown," and an install line that cannot start the app it
documents.

**Cannot fail / never measured.** Nothing to cite — there is no test
directory and no metric anywhere (the note's own tag: "No tests at all,"
`[claim]`), so nothing passes vacuously; failure is silent instead, falling
through to the `else` branch with no signal. Never measured:
`Agentic-Dspy-Rag:README.md:68` — the documented install line was never run
against the commit's own dependencies before publishing; it cannot import
`dspy.LM`.

**2026-09-23 report, corrected.** Called the API "pre-2.x style" — wrong;
`dspy.LM(model=...)` is the current 2.5+/3.x API. Said routing was "never
run here" — it now has been, offline, with a table showing 6 of 8 tested
intents misrouted silently. Missed that qdrant-client ≥1.19 removed the
`search`/`vectors_count` calls the code still makes.

**Matters most here.** (1) Never route on a substring of free text — declare
a closed `Literal` output, exactly why `pairs.py`'s decision field is typed
(`api.md`). (2) `import numpy` before `import dspy` on 3.3.1, in any venv
that also imports `qdrant_client`/`pyarrow`/`lancedb`. (3) A synthesizer that
merges passages into one answer without attribution is the operation P13
forbids; `graphrag.py` returns quotations and never prose.

---

## Summary

| repository | commit | DSPy target | verdict |
|---|---|---|---|
| `dspy-agent-skills` | `9d13f98` (2026-09-16) | `>=3.3.0,<3.4`, validated 3.3.1 | take the verification discipline and the MMR floor; refuse `drg-kg`, `dspy-rlm-hooks`, TARA's leniency, `dspy-refrag` whole |
| `dspydantic` | `1afc528` (2026-03-20) | `>=3.0.4` | catalogue the evaluator registry and optimizer-from-n; refuse the package (licence conflict; one task on the ladder so far) |
| `dspy-session` | `eb67e76` (2026-02-26) | `>=2.6`, lock pins 3.1.3 | take the freeze-at-call-time record shape; refuse wrapping `dspy.RLM` in it, and the package (no multi-turn surface here) |
| `dspy-optimizer` | `a07b3b7` (2025-07-27) | `>=2.6.27`, lock pins 2.6.27 | take `MockLLM` and the callback shape; refuse the Evaluator/Refiner/Merger loop (no held-out set, its own example deleted) |
| `dspy-agents` | `fde0dad` (2025-09-26) | `dspy-ai>=3.0.3,<4.0` | take the baseline-ledger shape, fixed to compare against a floor; refuse Agno/AgentOS (nothing here is served) |
| `dspy-auto-gepa` | `80a5402` (2026-07-04) | `>=3.2.1` | take the 5-argument metric contract and the `metric=Path` bypass; refuse letting a model draft the metric |
| `braid-dspy` | `c50c5b1` (2025-12-20) | `dspy-ai>=2.0.0`, lock resolves 2.6.27/3.0.4 | catalogue checked-plan validation for a contested procedure; refuse the wrapper (cycles dropped silently, wrong predictor optimized) |
| `dspy-advanced-prompting` | `facc1ad` (2026-04-11) | `dspy-ai>=2.4.0` | name hard-negative demo tiering for `pairs.py`; refuse the other ten techniques (prompt text, keyword checks) |
| `Agentic-Dspy-Rag` | `474f107` (2025-06-18) | unpinned; own install line resolves to 2.3.1 | take the classify→route→quote shape, already in `graphrag.py`; refuse substring routing and unattributed synthesis |
