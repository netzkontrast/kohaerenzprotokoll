# A DSPy toolchain for this repository — designed from nine repositories read against it

*2026-09-23. Written as a design; **built the same day**, on the author's
direction to port what the knowledge base and GraphRAG could use. The status
table says what exists; the sections below are the design as written, with
corrections left beside what the build proved wrong.*

## Status — what was built

| item | file | state |
|---|---|---|
| 0.1 surface check | `scripts/check_dspy_surface.py` | built — 17 checks, incl. numpy (SIMBA raises without it) |
| 0.2 skill check | `scripts/check_skills.py` | built — 4 project + 11 vendored skills clean; `--selftest` 6 cases |
| 0.3 offline LM | `scripts/lm_fixture.py` | built — `FixtureLM`, `fill()` answers any optimizer's own fields, `offline()` refuses the network |
| 0.4 a failing case per metric | each script's `selftest`; `scripts/selftests.py` runs all 14 suites | built |
| 1.1 run record | `scripts/lmrun.py` | built — 10 offline cases; the tenth (2026-09-24) raises DSPy 3.3's own `LMTransportError`, which the first nine never did, and `call()` re-raised it instead of recording `unreachable` |
| 1.2 baseline ledger | `scripts/baseline.py`, `Plan/runs/baselines.jsonl` | built — floor rows recorded for both tasks |
| job 1 harness | `scripts/pairs.py` | built — all five optimizers dry-run; **real-model runs since 2026-09-25** under decision 011, every rung but SIMBA (`dspy-optimization_2026-09-25.md`) |
| job 3 changes | `scripts/rlm_ingest.py` | built — cache off, budget, tools, reach, `--approval`; **not run live** (needs Deno and a yes) |
| job 2 structural fix | — | not built: revision 3 of the entity workflow waits on the author's definition of an entity |
| job 4 skill descriptions | `example_param_ok()` in the surface check | guard only — no routing failures recorded, so no dataset (P4) |
| Layer 3: `ask`, MMR floor | `scripts/graph.py`, `scripts/graphrag.py` | built — see `graphrag_2026-09-23.md` |

**Corrections the build made to this design.** The design says job 1 has
„n = 26" and `fold()` scores „65%". Both were true of
`Plan/trainsets/surface-pairs.jsonl` as last exported, which held 17 rows; the
judgement ledger itself had grown. Re-exported when this was written, it held
36 pairs and `fold()` decided 21 — 58%, which `NOW.md` had already measured. The
ledger now yields 71 <!--state:pairs.labelled--> pairs and `fold()` decides
41 <!--state:pairs.fold_correct-->, 57%; the judgements of documents 7–9 and 14
added the rest, and the committed export still holds 36 (corrected 2026-09-24:
this sentence had put the ledger's live count on the export).
The exported file had gone stale because nothing compared it to the ledger;
`pairs.py` now reads the ledger live and never the export.

## How this was made

Nine DSPy repositories under `netzkontrast/` were scanned by ten readers (Sonnet
subagents, `dspy-agent-skills` split in two), each given the same brief first:
`dspy-repos_2026-09-23/00-brief.md`. The brief describes this project — the
four model jobs in order of readiness, the principles a proposal has to survive,
the open problems — so that every reader judged its repository against *this*
work rather than against DSPy in general. Each reader was told to list **every**
good idea, tagged `[adopt] [adapt] [catalogue] [skip]` with `path:line`
evidence, and to name every place its repository does what this one forbids.

The reports are kept whole in `dspy-repos_2026-09-23/`. They hold **317 numbered
ideas**:

| repository | ideas | what it is, in one line | verdict |
|---|--:|---|---|
| `dspy-agent-skills` (A: workflow skills, tests, scripts) | 43 | 32 skills + validators, 633 tests offline in 1.4s | **take the verification discipline** |
| `dspy-agent-skills` (B: `dspy-book-*`) | 66 | book chapters as skills | **take the `optimize_anything` recipe and the optimizer evidence** |
| `dspydantic` | 33 | optimizes Pydantic field descriptions | take the evaluator registry and n-based optimizer choice; leave its numbers |
| `dspy-optimizer` | 27 | critique→repair prompt loop, 43 tests offline | take `MockLLM` and the callback shape |
| `dspy-auto-gepa` | 27 | thin wrapper over `dspy.GEPA` | take the metric contract; hand-roll the rest |
| `dspy-session` | 26 | multi-turn state for modules | take the frozen-evidence `Turn`; heed the RLM warning |
| `dspy-agents` | 25 | Agno + DSPy + MIPROv2 MVP | take the baseline store; fix its relative-only drift check |
| `braid-dspy` | 30 | plan-as-Mermaid-graph, then execute | catalogue the checked-plan idea |
| `dspy-advanced-prompting` | 20 | eleven prompting techniques | take hard-negative demos; everything else is prompt text |
| `Agentic-Dspy-Rag` | 20 | classify→route RAG demo | catalogue the shape for `ask`; the code does not run |

**Nothing is to be installed.** Every reader, independently, arrived at the same
conclusion for its own repository: the value is a pattern of 10–60 lines, and the
package would bring a DSPy pin, a Python floor, a key requirement or a runtime
this project does not need. That is the first result of the scan and it shapes
everything below: the toolchain is **scripts in `scripts/`, standard library
where possible, DSPy only in the step that names it**, exactly like the tooling
that already exists.

### Checked before relying on it

Five load-bearing claims were re-read in the source rather than taken from a
report: `dspy-wiki-compile`'s weights (`WEIGHTS = {"citations": 0.30, …}`,
`example_wiki_compile.py:34`) and `decision_legal` (`:129`); the
`optimize_anything` trap (`dspy-book-coding-agents/SKILL.md:59`); `MockLLM`
subclassing `dspy.BaseLM` (`dspy-optimizer/tests/conftest.py:9`); dspydantic's
0.5 fallback (`evaluators/functions.py:140,152,159`, `score_judge.py:119`); and
that `scripts/rlm_ingest.py:160` builds `dspy.RLM` with only `max_iters` — no
`max_llm_calls`, no `sub_lm`, no tools, and a `dspy.LM` with the cache left on.
All five hold.

---

## The one finding that repeats across repositories

**Six of the nine repositories contain a check that cannot fail**, each in a
different costume. This project's founding defect — `coverage()` returning 1.0
when passed no gold — is not rare. It is what evaluation code looks like by
default:

| repository | the check | what it returns on nothing |
|---|---|---|
| `dspy-advanced-prompting` | `edge_case_performance`, `robustness_score`, `consistency_score`; `test_coverage` | **1.0** when the case type is absent; coverage 1.0 by construction |
| `dspydantic` | every LLM-judge evaluator on a parse failure | **0.5**, silently |
| `dspy-optimizer` | batched and sample validation strategies | **pass** on empty input |
| `dspy-agents` | baseline drift monitor | a run with `score=0.0, total_calls=0` accepted as a baseline; only *relative* drift is checked |
| `braid-dspy` | the Critic's self-verification | pass/fail by counting keywords in the model's own text |
| `dspy-agent-skills` (`drg-kg`, via its skill) | extraction with no LM configured | an **empty graph**, confidently, unless `DRG_REQUIRE_LM=1` |

And three claim a measurement that was never made: dspydantic's
`ABLATION_RESULTS.md` (three of four configurations commented out; a sibling
script prints „SYNTHETIC BENCHMARK"), braid-dspy's cost claim (a hand-typed price
table times hand-typed accuracies), and dspy-optimizer's `dutch_invoices`
example, described in two documents and absent from the repository.

**Consequence for the design:** every metric and every guard below ships with a
`selftest.py` case in which it must fail, and with an explicit third state —
*could not score* — that is never folded into 0 or 1 (P15, P23). This is not new
doctrine; it is the existing doctrine, now with nine more pieces of evidence.

---

## The toolchain

Four layers. **Layer 0 needs no model and no key and could be built today.**
Layer 1 is what must exist before the first model call is trusted. Layer 2 is
the four jobs from `optimizers-and-data_2026-09-17.md`, each gated. Layer 3 is
the catalogue.

```
Layer 0  guards        check_dspy_surface · check_skills · lm_fixture · metric selftests
            │
Layer 1  the record    lmrun (trace, usage, cache off, P19 asserts) · baselines.jsonl
            │
Layer 2  the jobs      pairs (rule first, model on the residual) · entity names · RLM census · skill descriptions
            │
Layer 3  catalogue     qmd bench · ask · reviewed-page rule · checked plans
```

### Layer 0 — guards that need no model

**0.1 `scripts/check_dspy_surface.py`** — *from `dspy-agent-skills/scripts/check_dspy_surface.py`, pattern not file.*
Assert, with `inspect.signature`, the DSPy symbols this repository actually
calls: `dspy.RLM(…, max_iters=…)` (renamed once already, from `max_iterations`,
in 3.3.0), `dspy.LM(…, cache=…)`, the optimizers on the ladder
(`LabeledFewShot`, `BootstrapFewShot`, `InferRules`, `SIMBA`, `GEPA`) and the
constructor gotchas (`GEPA` asserts `reflection_lm` at construction). Runs in
`.venv-dspy`; says exactly how to create the venv when it is absent, like
`sources.py`.
*Why now:* `dspy.RLM` is upstream-experimental and this repository pins against
it with nothing re-checking the surface.
*May not:* assert anything the repository does not call.
*Fixture:* itself — it fails loudly against a stub module missing one parameter.

**0.2 `scripts/check_skills.py`** — *from `dspy-agent-skills/tests/test_skill_metadata.py`.*
Validate `.agents/skills/*/SKILL.md` (and the symlinks into `.claude/skills/`):
filename case, `name` equals directory, spec-only frontmatter fields,
`description` + `when_to_use` ≤ 1536 characters. **Excludes the vendored `jev*`
folders by path** — they are third-party and copied unchanged.
*Why now:* job 4 optimizes exactly this field; a validator must exist before
anything rewrites it. Standard library only.

**0.3 `scripts/lm_fixture.py`** — *`MockLLM` from `dspy-optimizer/tests/conftest.py`,
`RecorderLM` from `dspy-agents/tests/test_dspy_config.py`.*
A `dspy.BaseLM` subclass that returns scripted completions and records every
request, verified by the reader to work unmodified under DSPy 3.3.1. This is
what makes P5 satisfiable for every model step below: each gets a `--dry-run`
that runs the real program against the fixture, offline, free.
**Plus one rule learned the hard way during this scan:** a test that falls
through to the default LM is a live call. `dspy-auto-gepa`'s
`test_partial_explicit_fields_infer_rest` is unmocked, and running its suite
made a real OpenRouter call from this container (fixture words only — `hello`,
`bye` — no corpus text). So the fixture module also sets
`dspy.configure(lm=<fixture>)` at import and refuses to run if any key-bearing
environment variable would be read. A dry-run that *can* reach the network is
not a dry-run.

**0.4 A failing case per metric in `scripts/selftest.py`.**
Every metric added in Layer 2 gets three cases before it is used: empty gold →
*could not score*; a canary violation → 0 regardless of the rest; a parse
failure → *could not score*, never 0.5. The table above is the evidence.

### Layer 1 — the record every model call writes

**1.1 `scripts/lmrun.py`** — one wrapper, used by every step that calls a model.
Merges four readers' findings into one small thing:

| it does | from |
|---|---|
| builds `dspy.LM(…, cache=False)` and runs repeats (P18) | this repository's own rule; no scanned repository enforces it — `dspy-auto-gepa` sets `cache=False` only in examples, and `rlm_ingest.py` does not set it at all |
| wraps each call in `dspy.track_usage()` and records tokens and cost | `dspy-agents` `compile_rag.py:85-87`, `eval/harness.py:78-84` |
| freezes inputs, raw output (`lm.history[-1]`), `finish_reason` and model at call time — never reconstructed later | `dspy-session`'s `Turn`, which snapshots at call time; its `on_turn` hook is the shape |
| appends `{"event": …, **state}` to `Plan/runs/<slug>/lm/<run>.jsonl` | `dspy-optimizer`'s `HistoryCallback._log_event` |
| asserts non-empty content and German where German is expected (P19) | this repository; no scanned repository checks either |
| records a status of `answered` / `unreachable` / `refused` / `unparsed` — four states, never a score | P15; `dspy-session`'s `on_metric_error="zero"` is the trap it avoids |

This **is** the catalogue's `--trace` mode, and it is also the answer to the
blocker `continuous-improvement_2026-09-17.md` names first: *a judgement records
its rule and not its evidence*. A judgement a model helped make now has its
evidence on disk beside it.
*May not:* send corpus text anywhere the author has not approved for that run
(`NOW.md`, *How far the yes to TypeSafe reaches* — the same question applies to
OpenRouter). The wrapper takes the approval as an argument naming the decision,
and refuses without one.
*Never wraps `dspy.RLM` in a `History`-carrying session:* `dspy-session`'s own
`docs/rlm.md` records RLM failing on every iteration with
„Unsupported value type: History".

**1.2 `Plan/runs/baselines.jsonl` and `scripts/baseline.py`** — *from
`dspy-agents/dspy_optimize/baselines/{store,monitor,thresholds}.py`, reshaped.*
Append-only, one row per scored run: task, program hash, trainset hash, n,
per-example outcomes, score, cost, date. The program hash comes from the
compiled instructions and demos, not from a manually bumped tag
(`dspy-agents`' `_program_artifact_signature`, `dspy_config.py:45-86`).
`baseline.py compare` prints `ok`/`warn`/`fail` against the previous row **and
against an absolute floor** — the deterministic rule's score — because a
relative-only monitor accepts a pipeline broken from its first run.
*Done is a measurement* (P24): whether a compiled program is still the best is
derived from this file, never stored as a flag.

### Layer 2 — the four jobs, each gated

Order is `optimizers-and-data_2026-09-17.md`'s, and nothing here reorders it.

#### Job 1 — one term or two (`Plan/trainsets/surface-pairs.jsonl`, n = 26)

**Step 1a is a rule, not a model.** `NOW.md` already says so, and the scan
agrees from the outside: every miss of `fold()` is an inflection, and
`dspy-book-optimizers` measured SIMBA *below* its baseline while being the most
expensive run of twelve. So the first entry in `baselines.jsonl` for this task
is `fold()` (65%), the second is a morphology rule the author has decided the
reach of, and only the residual — pairs both rules call two terms — goes to a
model.

**Step 1b, the program:** a signature `first, second -> decision: Literal["one-term", "two-terms"], rule: str`
(a closed `Literal`, because `Agentic-Dspy-Rag` shows the alternative:
`"Comparative" in user_intent` as a substring test on free text).

**The metric**, shaped for GEPA from day one (the five-argument contract that
`dspy-auto-gepa`, `dspy-agent-skills` and `dspy-book-eight-steps` all converge
on): `metric(example, pred, trace=None, pred_name=None, pred_trace=None) ->
dspy.Prediction(score, feedback)`, with the recorded human `rule` as feedback —
which `scripts/trainset.py`'s `score_one` already returns. Two additions:

- **A canary veto.** `Negentropie`/`Entropie` and every other never-merge pair
  in `selftest.py` is evaluated on every candidate; a candidate that merges one
  is disqualified, not docked 1/26. No scanned repository supports this —
  `dspy.GEPA` optimizes a mean, and `dspy-auto-gepa`'s `promote()` saves
  whatever `train()` produced. It is ten lines around the optimizer, run
  before a program is written to disk.
- **A pinned split.** At n = 26 a seeded shuffle can put every canary in the
  training set. Canaries are pinned to evaluation; the rest is leave-one-out or
  repeated k-fold, reported as a distribution (P18), never one number.

**Demos include hard negatives** — pairs that look like inflections and are two
terms (`dspy-advanced-prompting`'s tiering of challenging examples, the one
technique there that is a mechanism rather than prompt text).

**The ladder stays as written** — `LabeledFewShot` → `BootstrapFewShot` →
`InferRules` → `SIMBA` (with `bsize` below 26 and a held-out check, because it
can regress) → `GEPA`. `InferRules` is the rung **none of the nine repositories
covers**; it is also the one whose output — rules in words — can be compared
directly against the 26 human `rule` fields, and that comparison is a result in
its own right.

*Gate:* the morphology rule decided by the author, and Layer 0–1 built.
*May not:* write to `judgements.jsonl`. A model's decision is a proposal a person
records, with the evidence `lmrun.py` kept.

#### Job 2 — entity lists (revision 3 of `.claude/workflows/entity-lists.js`)

`NOW.md` has the fix: names only, lines by code. The scan adds one way to make
it structural rather than instructed: **the output type has no field for a
line.** A typed output — `list[EntityName]` where `EntityName` carries `name`
and nothing positional — makes a typed line impossible rather than forbidden
(dspydantic's idea of the schema as the prompt, turned around: the schema as the
refusal). `read.py --find` then places each name or drops it; the drop count is
reported.

Also from the scan, all code: fold parentheticals before ranking
(`Neuromancer` / `Neuromancer (Roman, 1984)`); extend the candidate script to
multi-word and slashed names, which caps Jev's recall at 0.80 and 0.63 today.

*Scoring:* `entities.py score`, reported against the human ceiling (P27, F1 ≈
0.66). `dspy-book-metrics`' judge-calibration protocol (20–50 labels, hold out
20%, trust at 80–90% agreement) is the template if a model ever judges these —
and it says plainly that n = 26 is below its own floor.

*Gate:* the author's definition of an entity (research vocabulary or world),
which `NOW.md` names as open.

#### Job 3 — the census through `dspy.RLM` (`scripts/rlm_ingest.py`)

Four changes, all found by comparing the script with `dspy-rlm-module` and
`dspy-rlm-workflow`:

1. `cache=False`, and `lmrun.py` around the call.
2. `max_llm_calls=` set explicitly and `sub_lm=` a cheaper model, so budget is a
   parameter and not a surprise — the first run of this script ran out of REPL
   budget and began reconstructing from scrollback.
3. **Pass `read.py --find` and a count as tools** (`tools=[find_line, count]`).
   The model then *asks* for a line the way a person here does; P26 enforced
   inside the sandbox, not only after it.
4. **A second verification tier.** Today a candidate is accepted if its cited
   line contains it, so a reconstruction that happens to cite real lines
   passes. Decidable and cheap: the distribution of cited lines across the
   document — a reading that never cites past L400 of 2,498 did not read to the
   end, whatever it says.

`dspy-book-modules` gives ~50k tokens as the size at which RLM starts to pay;
that is a number to measure against the landed documents before running RLM on
a short one.

*Gate:* two or three more hand-read candidate lists (`tools` skill, *What is
missing*), because extraction has one usable gold list.

#### Job 4 — skill descriptions through GEPA

`dspy-book-coding-agents` is a working recipe and the only one of the nine that
fits: `gepa.optimize_anything` over text, **not** `dspy.GEPA` (a `SKILL.md` is
not a program — `dspy-auto-gepa` cannot do this at all). The evaluator returns
`(score, side_info)`, deterministic checks (0.2's validator, length, required
sections) weigh more than any judged signal, and the output is a proposal with a
printed regression list, applied by a person.

**Its trap needs a guard before first use:** `optimize_anything` introspects the
evaluator and its second parameter must be named `example`; named anything else,
the data is silently dropped and the crash comes layers later. One
`inspect.signature` assertion.

*Gate:* 5–20 recorded routing failures — a task where an agent loaded the wrong
skill or none. **None are recorded today**, so this job has no dataset and, by
P4, does not start. Recording them is free and could begin now.

### Layer 3 — kept, with the instance each is waiting for

| idea | from | waits for |
|---|---|---|
| **`qmd bench` fixture from `Wiki/questions/` and `Wiki/conflicts/`** — each already says „a search finds this in `<slug>`", which is a free relevance label | brief; `Agentic-Dspy-Rag`'s retrieve-then-rerank, measured instead of assumed | the author's go-ahead; already in `NOW.md` |
| **MMR with a relevance floor** for de-duplicated top-k passages | `dspy-agent-skills/scaffolding/kp_canon_retriever.py` — measured: unguarded MMR picks an irrelevant passage over a near-duplicate relevant one at every diversity setting 0.5–0.8 | an `ask` step that needs top-k |
| **`ask` as classify → route → quote**, never synthesize | `Agentic-Dspy-Rag`'s orchestrator shape; its `MultiStepRAG` synthesizer merges sources without attribution, which P13 forbids | `ask` existing at all |
| **The reviewed-page rule**: a new source contradicting a promoted page is flagged and listed, never applied | `dspy-wiki-compile`'s `decision_legal()`; its axis weights 0.30 citations / 0.25 decisions / 0.20 merge / 0.15 diffs / 0.10 links | the first promotion (`NOW.md`, *A reviewed page has no rule yet*) |
| **A procedure as a checked graph** — Mermaid text parsed, validated and topologically ordered by code before any step runs | `braid-dspy` (Kahn's algorithm; structural validation gates execution) | a procedure whose order is in dispute; `account.py`'s decompositions are the candidate |
| **Evaluator registry** — `fold_exact`, `jev_choice`, `judgement_replay` behind one interface | `dspydantic`'s `EvaluatorFactory` and `PredefinedScoreEvaluator` | a second evaluator actually in use |
| **Optimizer chosen from n** | `dspydantic`'s `_auto_select_optimizer` | more than one task on the ladder |
| **Contextual signature class names** for short-field optimization | `dspydantic` | job 4 underperforming |
| **Per-directory `AGENTS.md`**, and handover notes per issue | `dspy-agents` | a directory an agent keeps misreading |
| **Content-hash cache invalidation** | `dspy-agents` | any cached derived output |

### Deliberately not taken

| thing | why |
|---|---|
| any of the nine as a dependency | every reader concluded pattern, not package; floors and pins (`dspy-auto-gepa` needs Python ≥ 3.12; `braid-dspy` targets the pre-3.x API; `Agentic-Dspy-Rag` pins `pydantic<2`) |
| `drg-kg`'s extraction and graph layers | `enable_implicit_relationships=True` by default — an inferred edge, which decision 005 excludes |
| `dspy-rlm-hooks` | monkeypatches private DSPy internals; its own security note says to pin |
| TARA's progressive leniency | lowers the bar until something passes; the right terminal state here is an open question (P15) |
| `dspy-refrag` wholesale | its selection marks a boolean and never shrinks the prompt |
| Levenshtein or embedding similarity as a merge signal | would score `Negentropie`/`Entropie` as close — the canary exists to catch exactly this |
| LLM-drafted metrics (`dspy-auto-gepa`'s default) | the rule a program is scored by is written by a person; the `metric=Path(...)` bypass is the only path used |
| `MIPROv2`, `BootstrapFewShotWithRandomSearch`, synthetic data generation | 100+ / 50+ examples; `dspy-agents` ran MIPROv2 on 50 while its own documentation said ~28 |

---

## What to build first

If the author says go, this is the order, and each step is separately
committable and separately useful:

1. **0.1–0.4.** No model, no key, no corpus text leaves the container. Each
   closes a gap that exists today (`rlm_ingest.py`'s unchecked surface and
   cache; skills nothing validates; model steps with no offline fixture).
2. **1.1–1.2**, with `rlm_ingest.py` moved onto `lmrun.py` as the first user —
   the one existing model call, so the wrapper is proved on a real instance
   rather than anticipated (P3).
3. **Job 1a**, the morphology rule, scored through `baseline.py` against
   `fold()` — still no model.
4. Only then any rung of the ladder.

Steps 1–3 need nothing from the author except the go-ahead and, for 3, the reach
of the morphology rule. Nothing in this document needs corpus text sent to a
third party until step 4, and step 4 asks again.
