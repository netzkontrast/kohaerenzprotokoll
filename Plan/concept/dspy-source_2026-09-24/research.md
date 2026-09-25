# Research: the papers and official docs behind DSPy 3.3.1 and GEPA 0.1.4

## 1. Header

**Slice.** Papers and blogs behind DSPy and GEPA — not source code, not tests.
Two parts: (a) nine required arXiv papers (DSPy, DSPy Assertions, MIPRO,
BetterTogether, GEPA, LangProBe, Recursive Language Models, mmGRPO, plus a
search for any paper cited for SIMBA/InferRules/`optimize_anything`/gskill/
`Flex`), read via `WebFetch`/`WebSearch` against arxiv.org; (b) the official
DSPy and GEPA documentation this repository has landed locally.

**Files read, local, in full.**

| file | lines |
|---|--:|
| **Map (read first):** `.agents/skills/dspy/references/repos.md` | 546 |
| **Map (read first):** `.agents/skills/dspy/references/optimizers.md` | 1230 |
| `.agents/skills/dspy/references/rlm.md` (consulted, to calibrate new/same) | 647 |
| `.agents/skills/dspy/references/text-artifacts.md` (consulted, same reason) | 616 |
| `dspy-3.3.1/docs/docs/community/built-with-dspy.md` | 100 |
| `dspy-3.3.1/docs/docs/community/community-resources.md` | 65 |
| `dspy-3.3.1/docs/docs/community/how-to-contribute.md` | 6 |
| `dspy-3.3.1/docs/docs/community/normalized-lm-api-migration.md` | 239 |
| `dspy-3.3.1/docs/docs/community/use-cases.md` | 76 |
| `dspy-3.3.1/docs/docs/tutorials/real_world_examples/index.md` | 35 |
| `dspy-3.3.1/docs/docs/tutorials/index.md` | 72 |
| `dspy-3.3.1/docs/docs/roadmap.md` | 127 |
| `dspy-3.3.1/docs/docs/learn/optimization/overview.md` | 13 |
| `gepa-0.1.4/docs/docs/blog/posts/2026-04-09-gepa-at-scale-with-combee/index.md` | 132 |
| `gepa-0.1.4/docs/docs/blog/posts/2026-05-11-learning-fast-and-slow/index.md` | 187 |
| `gepa-0.1.4/docs/docs/blog/posts/2026-02-18-introducing-optimize-anything/index.md` | 502 |
| `gepa-0.1.4/docs/docs/blog/posts/2026-02-18-automatically-learning-skills-for-coding-agents/index.md` | 144 |
| `gepa-0.1.4/docs/docs/blog/posts/2026-02-13-introducing-the-gepa-blog/index.md` | 17 |
| `gepa-0.1.4/docs/docs/blog/posts/2026-03-17-confidence-adapter-benchmark/index.md` | 444 |
| `gepa-0.1.4/docs/docs/guides/use-cases.md` | 1504 |
| `gepa-0.1.4/docs/docs/about.md` | 192 |
| `gepa-0.1.4/docs/docs/index.md` | 632 |

18 required local files (4487 lines) plus 2 map files (1776 lines) plus 2
skill reference files read to calibrate `skill:` tags (1263 lines) — 22 files,
7526 lines total, every one read in full (not skimmed), including the
1504-line GEPA showcase page and the 632-line landing page's embedded
JavaScript/testimonial carousel.

**Papers fetched (arXiv), abstract and/or full HTML text.** 2310.03714
(DSPy), 2312.13382 (DSPy Assertions), 2406.11695 (MIPRO), 2407.10930
(BetterTogether), 2507.19457 (GEPA, fetched three times — main results table,
abstract-page claims, dataset-size/seed check), 2502.20315 (LangProBe),
2512.24601 (Recursive Language Models), 2508.04660 (mmGRPO). Plus one paper
outside the required list, found while checking what DSPy's docs cite for
`InferRules` (none do): 2507.03620, "Is It Time To Treat Prompts As Code?",
the only paper found anywhere that reports a measured `InferRules` result —
flagged throughout as third-party, not DSPy/GEPA-cited. 15 `WebFetch` calls
and 4 `WebSearch` calls in total (arXiv IDs for RLM and mmGRPO were not in the
brief and had to be found; so did the absence of a paper for SIMBA and
InferRules).

**What I ran to verify.** This slice is papers and prose, not source code —
almost nothing here is offline-probeable the way another reader's `simba.py`
or `gepa.py` reading is. Two exceptions, both run live against the installed
package, offline, `env -u OPENROUTER_API_KEY -u TYPESAFE_API_KEY -u
OPENAI_API_KEY -u ANTHROPIC_API_KEY .venv-dspy/bin/python`: `inspect.signature`
on `gepa.optimize_anything.optimize_anything` (the function the `optimize_anything`
blog post prints a simplified call shape for), and a `TypeError` probe
confirming every parameter but `seed_candidate` is keyword-only. Separately,
`grep -rn -i "arxiv"` against every file in `.agents/skills/dspy/` (all 12
reference files plus `SKILL.md`) returned **zero matches** — the skill cites
no academic paper anywhere, for anything. That single fact is the header
result of this whole read: essentially everything below is `new`.

**What this part of DSPy/GEPA is, in five lines.** DSPy's own paper
introduced signatures/modules/teleprompters and measured that composing and
bootstrapping generic modules turns 4–20% accuracy into 49–88% on GSM8K and
multi-hop QA, with no hand-written prompts. MIPRO and BetterTogether are the
two teleprompters DSPy's roadmap names as the reason a general "compiler" idea
became two concrete, separately-published, separately-measured algorithms.
GEPA is a different lineage — reflective, feedback-driven evolutionary search,
not Bayesian instruction search — published as beating GRPO with up to 35x
fewer rollouts and MIPROv2 by over 10%, and its own `optimize_anything` API,
`gskill`, `Combee` and `ConfidenceAdapter` blog posts are GEPA's authors
applying the same engine to code, agent architectures, skills and confidence
scores. LangProBe and mmGRPO are the two papers that step back from any one
optimizer: LangProBe benchmarks all of them across many tasks and finds
optimization sometimes *hurts*; mmGRPO is the RL-side answer, composed with
prompt optimization rather than against it. Recursive Language Models is
adjacent, not part of the optimizer family — it is what `dspy.RLM` (used by
`rlm_ingest.py`) implements.

---

## 2. Knowledge items

### API

- **`optimize_anything()`'s own top-level signature is nowhere in the skill.** `text-artifacts.md` gives four `surface` lines for `EngineConfig`, `ReflectionConfig`, `GEPAConfig` and `EvaluatorWrapper`, but never the function itself. Verified live against the installed package, 2026-09-24: `seed_candidate: str | dict[str, str] | None = None` is the only positional-or-keyword parameter; `evaluator`, `batch_evaluator`, `dataset`, `valset`, `objective`, `background`, `config` are all keyword-only (`*` in the signature), return type `gepa.core.result.GEPAResult`. `gepa:src/gepa/optimize_anything.py:1114-1124` [api] (verified: ran `inspect.signature`) · skill: new
- **`optimize_anything(seed, evaluator)` (two positional args) raises `TypeError: optimize_anything() takes from 0 to 1 positional arguments but 2 were given`.** Confirmed live. [api] (verified: ran, caught the `TypeError`) · skill: new — see *Probes worth adding*.
- **The blog's own printed call shape for `optimize_anything` is a simplification, not the real signature**: `docs/docs/blog/posts/2026-02-18-introducing-optimize-anything/index.md:154-166` shows seven parameters with no `*` and omits `batch_evaluator` entirely. Not wrong, exactly — a tutorial simplification — but a reader copying it verbatim would never learn the keyword-only rule or that a second entry point exists. [trap] (verified: read + `inspect.signature` cross-check) · skill: new
- **DSPy's own paper names five teleprompters, not the ladder `pairs.py` uses**: `LabeledFewShot`, `BootstrapFewShot`, `BootstrapFewShotWithRandomSearch`, `BootstrapFewShotWithOptuna` (not in the installed 3.3.1 surface at all — worth a source-reader check), `BootstrapFinetune`, `Ensemble`. arXiv:2310.03714 §4 [api] (verified: read, WebFetch) · skill: new (the skill's `optimizers.md` documents the *installed* surface of each; it never states which of these the founding paper itself proposed, and never flags that `BootstrapFewShotWithOptuna` is not one the current package exposes under that name)
- **DSPy is undergoing a typed LM boundary migration (`LMRequest`/`LMResponse`) starting in 3.3, opt-in via `dspy.context(experimental=True)`**, with `forward_contract = "legacy" | "typed_lm"` on `BaseLM` subclasses; legacy stays default through 3.4, becomes default-with-escape-hatch at 3.5, and the untyped `forward(prompt=None, messages=None, **kwargs)` contract is removed at 3.6/4.0. `docs/docs/community/normalized-lm-api-migration.md:39-53,218-227` [claim] (verified: read) · skill: new — nothing in `api.md`'s LM-config coverage mentions this migration plan at all; a custom `BaseLM` written today with no `forward_contract` is silently "legacy" and will start warning at 3.4.

### OPT

**DSPy — "Compiling Declarative Language Model Calls into Self-Improving Pipelines" (arXiv:2310.03714).**

- **GSM8K case study, exact table.** 200 train / 300 dev / 1.3k test, final-numeric-answer accuracy. `Vanilla`+GPT-3.5: 24.0% (dev) → 64.7% dev / 61.7% test with `Bootstrap×2`; `Vanilla`+GPT-3.5+`Bootstrap×2+Ensemble`: 62.7% dev / 61.9% test. `CoT`+GPT-3.5: 50.0% (0-shot) → 80.3% dev / 72.9% test (`Bootstrap`) → 88.3% dev / 81.6% test (`Bootstrap+Ensemble`). `Reflection`+GPT-3.5+`Bootstrap`: 83.0%/76.0%; `+Ensemble`: 86.7% dev. Llama2-13b-chat: `Vanilla` 7.0%→9.4% zero-shot, 37.3%/36.5% `Bootstrap×2`; `CoT`+`Bootstrap`: 43.3% dev; `Reflection`+`Bootstrap+Ensemble`: 49.0%/46.9%. arXiv:2310.03714 Table 1 [number] (verified: read, WebFetch HTML) · skill: new
- **HotpotQA (fullwiki) case study, exact table.** 200 train (70/30 internal split) / 1000 test, Answer EM and Passage-retrieval accuracy. `Vanilla`+GPT-3.5 few-shot: 34.3%/31.5% ans. `CoT_RAG`+GPT-3.5 few-shot: 36.4%/29.8% ans, 36.0%/34.4% psg; `+Bootstrap`: 42.3% dev ans, 36.0% dev psg. `MultiHop`+GPT-3.5+`Bootstrap`: 48.7%/39.6% ans, 47.0%/43.8% psg; `+Ensemble`: 54.7%/45.6%* ans (*on 50% of the test set — a partial-evaluation footnote worth keeping). `MultiHop`+Llama2-13b-chat+`Bootstrap`: 42.0%/36.4% ans, 48.3%/43.5% psg. `MultiHop_T5`+T5-Large: 39.3% dev ans, 46.0% dev psg (no bootstrap needed to place — a 770M model doing multi-hop retrieval unaided). arXiv:2310.03714 Table 2 [number] (verified: read, WebFetch HTML) · skill: new
- **Stated compute cost: "compiling generally runs on the order of minutes (or tens of minutes)", 10–20 trials over 150–300 validation examples.** arXiv:2310.03714 §5 [claim] (verified: read) · skill: new
- **The paper's own headline claim, verbatim in spirit**: composing the right generic modules improved different LMs from 4–20% accuracy to 49–88% accuracy, "over 25%" (GPT-3.5) and "65%" (Llama2-13b-chat) gains vs. standard few-shot prompting, and "5–46%"/"16–40%" vs. expert-created demonstrations. arXiv:2310.03714 abstract [claim] (verified: read) · skill: new — no number from the founding paper appears anywhere in `optimizers.md`, which quotes only the third-party "book" chapter's own from-scratch replication.

**DSPy Assertions (arXiv:2312.13382).**

- **Four case studies, one dataset, one model.** MultiHopQA, LongFormQA, QuizGen, TweetGen, all on the HotpotQA "hard" subset, 300 train / 300 dev / 500 test, gpt-3.5-turbo (`max_tokens=500, temperature=0.7`), ColBERTv2 over Wikipedia 2017 abstracts. arXiv:2312.13382 §5 [number] (verified: read, WebFetch HTML) · skill: new
- **The starkest single number in the paper: QuizGen's `Correct JSON` goes from 37.6% (Vanilla) to 98.8%/100% (Infer w/ Assert / Compile) — a structural-validity gain, not an accuracy gain.** TweetGen's `Engaging` metric: 2.0% (Compile, no assert) → 73.0% (Compile w/ Assert). arXiv:2312.13382 Figure 2 [number] (verified: read, WebFetch HTML) · skill: new
- **Mechanism, exact.** `Assert`: on failure, retries up to `R` times with the prior erring output plus the error message re-injected into the prompt; at `r ≥ R`, raises `AssertionError` and halts the pipeline. `Suggest`: identical retry loop, but at `r ≥ R` it logs a warning and **lets the pipeline continue** rather than halting. Compile-time bootstrapping applies the same assertion-driven backtracking to the *teacher*, so every bootstrapped demo is guaranteed to satisfy the intermediate constraints the metric alone would never see. arXiv:2312.13382 §3–4 [api] (verified: read, WebFetch HTML) · skill: new — `optimizers.md`'s `BootstrapFewShot` section documents the *truthiness trap* in the installed 3.3.1 metric contract in detail but never connects it to Assertions' own constraint-bootstrapping idea, which predates and motivates a stricter metric.
- **No compute-overhead number is given anywhere in the paper** — retries add LM calls per failed assertion, up to `R` per check, but the paper reports no per-example call count or latency. arXiv:2312.13382 (verified: read, WebFetch HTML) · skill: new (absence noted)
- **Aggregate claim: "passing constraints up to 164% more often" and "generating up to 37% more higher-quality responses."** arXiv:2312.13382 abstract [claim] (verified: read) · skill: new

**MIPRO / MIPROv2 — "Optimizing Instructions and Demonstrations for Multi-Stage Language Model Programs" (arXiv:2406.11695), EMNLP 2024.**

- **Seven tasks, with sizes that range far below the "100+" rule this repo's own concept doc states.** HotPotQA 500/500/2000; HotPotQA-Conditional 500/200/200; ScoNe 500/500/1200; HoVeR 500/500/1520; **Iris 75 train, no dev, 75 test; Iris-Typo 75/–/75; Heart Disease 120 train, no dev, 183 test.** arXiv:2406.11695 §5 [number] (verified: read, WebFetch HTML) · skill: new — **this is the single closest published train-set size to this repository's 51–63-row scale of any optimizer paper read for this slice**, see *Evidence by optimizer*, below.
- **Full test-set table** (0-shot instructions / Module-level OPRO / 0-shot MIPRO / Bootstrap Random Search demos-only / MIPRO instructions+demos): ScoNe 56.2 / 73.5 / 71.5 / 75.4 / **79.4**; HotPotQA 36.1 / 39.0 / 36.8 / 45.8 / **46.4**; HoVeR 25.3 / 32.5 / 33.1 / 37.2 / **39.0**; Iris 40.9 / — / 36.4 / **94.1** / 88.6; Heart Disease 26.8 / — / 25.8 / **79.2** / 74.2. arXiv:2406.11695 Table 2 [number] (verified: read, WebFetch HTML) · skill: new — **note Bootstrap-Random-Search-demos-only beats full MIPRO on both classification tasks** (Iris 94.1 vs 88.6, Heart Disease 79.2 vs 74.2): more search over demos, no instruction rewriting, wins at this small a scale.
- **Trial budget scales down with dataset size, not held fixed**: "50 full evaluation trials" for HotpotQA/ScoNe, **"30 full evaluation trials" for Iris/Heart Disease/HotPotQA-Conditional**, "20 full evaluation trials" for HoVeR. Candidate count `N` also varies by task: HotpotQA N=30, ScoNe N=70, HoVeR N=10 (not stated for Iris/Heart Disease). Task model Llama-3-8B (temp 0.7); proposer/prompt LM GPT-3.5 (temp 0.7), **except GPT-4o specifically for ScoNe/HoVeR bootstrapping** — even MIPRO's own paper swaps to a stronger model for particular tasks rather than using one model throughout. arXiv:2406.11695 §4–5 [number] (verified: read, WebFetch HTML) · skill: new — `optimizers.md`'s MIPROv2 section documents the installed package's `auto="light"|"medium"|"heavy"` presets (`n:6/12/18`, `val_size:100/300/1000`) in full but has no paper-side evidence that a *reduced* trial count (30, not 6) was ever validated at Iris/Heart-Disease scale; the skill's presets and the paper's own small-task settings are two different numbers for the same idea.
- **The paper does not define `auto="light"/"medium"/"heavy"` presets at all — those are a later, installed-package addition.** Confirmed by omission across every table and the algorithm description read. arXiv:2406.11695 (verified: read, WebFetch HTML) · skill: unchecked: `optimizers.md` states the preset numbers as installed-package fact (correctly, and separately verified against `dspy:teleprompt/mipro_optimizer_v2.py`) but never notes that the *paper* MIPRO/MIPROv2 was published against does not contain them — a reader could reasonably assume the presets are paper-validated; they are not.

**BetterTogether — "Fine-Tuning and Prompt Optimization: Two Great Steps that Work Better Together" (arXiv:2407.10930), EMNLP 2024.**

- **Full results table, three models × three tasks × six strategies, averaged over 3 seeds.** HotPotQA (Mistral-7B/Llama-2-7B/Llama-3-8B): Vanilla 17.2/13.2/31.6; Prompt-only (Π) 33.8/33.3/46.9; Weights-only (Θ) 22.9/12.2/34.8; Π→Θ 36.3/32.7/42.8; Θ→Π 33.0/34.2/43.6; **Π→Θ→Π 37.6/34.8/46.7** (best or near-best on two of three models). GSM8K: Vanilla 40.3/24.0/72.7; Π 46.4/26.0/77.9; Θ 40.7/24.0/75.1; Π→Θ 47.3/27.3/**77.6**; **Θ→Π 48.3/26.6/78.9**; Π→Θ→Π 46.8/26.3/77.0 (here the *best* strategy differs by model — no single strategy dominates). Iris: Vanilla 26.0/0.0/48.0; Π 57.3/56.7/79.3; Θ 29.3/–/37.3; Π→Θ 30.7/26.7/44.0; **Θ→Π 66.7/–/78.7**; **Π→Θ→Π 52.7/65.3/79.3**. arXiv:2407.10930 Table 1 [number] (verified: read, WebFetch HTML) · skill: new
- **Dataset scales, including the smallest anywhere in this whole read**: HotpotQA 1,000/500/1,500 with prompt-optimization *subsampled* to 100 train/250 val; GSM8K identical shape; **Iris: 150 total, split 50/50/50, prompt-optimization subsampled to 15 train/35 val.** arXiv:2407.10930 §4 [number] (verified: read, WebFetch HTML) · skill: new — BetterTogether's own *prompt* stage runs on 15 train examples in the published paper, well inside this repository's 51–63-row scale; only its *weight* stage needs anything larger.
- **BootstrapFewShotWithRandomSearch is the prompt optimizer used inside every BetterTogether strategy**: "randomly search 6 candidate programs using up to 3 few-shot examples for each module prompt." arXiv:2407.10930 §4 [number] (verified: read, WebFetch HTML) · skill: new
- **Fine-tuning hyperparameters, exact**: LoRA rank 32, alpha 64, dropout 0, 5 epochs, lr 1e-5, batch size 8, bfloat16; inference top-k sampling, temperature 0.1, top_k 0.97, ≤1024 tokens. Total compute: **≈75 A100-GPU-hours** for the whole Table 1. arXiv:2407.10930 §4 [number] (verified: read, WebFetch HTML) · skill: new — this is the number that rules the weight-optimization half out here on cost alone, independent of the "no fine-tunable model" reason `optimizers.md` already gives.
- **Headline claim: "BetterTogether strategies optimizing weights and prompts together outperform directly optimizing weights alone and prompts alone by up to 60% and 6%, respectively."** arXiv:2407.10930 abstract [claim] (verified: read) · skill: new

**GEPA — "Reflective Prompt Evolution Can Outperform Reinforcement Learning" (arXiv:2507.19457).**

- **Main results table, six tasks, Qwen3 8B as task LM (GPT-4.1 Mini used for a separate cross-model check).** Baseline / GRPO / MIPROv2 / GEPA / GEPA+Merge / GEPA-rollouts: HotpotQA 42.33 / 43.33 / 55.33 / **62.33** / 64.33 / 6,871; **IFBench 36.90 / 35.88 / 36.22 / 38.61 / 28.23 / 3,593** (GEPA+Merge is *worse than baseline* here — see TRAP, below); HoVer 35.33 / 38.67 / 47.33 / **52.33** / 51.67 / 7,051; PUPA 80.82 / 86.66 / 81.55 / **91.85** / 86.26 / 2,426; AIME-2025 27.33 / 38.00 / **20.00** / 32.00 / 32.00 / 1,839 (MIPROv2 *worse than baseline* on math); LiveBench-Math 48.70 / 51.26 / 46.60 / 51.95 / 51.95 / 1,839. Aggregate improvement over baseline: **GEPA +9.62%, GRPO +3.68%, MIPROv2 +2.61%** — cross-checked and internally consistent with the per-task numbers. arXiv:2507.19457 Table 2 (verified: read, WebFetch HTML; hand-checked the aggregate arithmetic against the six per-task rows) [number] · skill: new — `optimizers.md`'s own GEPA section is exhaustively source-verified (budget formula, defaults, traps) but carries none of the paper's own headline task-level numbers.
- **GRPO's budget in the same comparison: 24,000 rollouts per task**, against GEPA's 1,839–7,051 — a 3.4×–13×  difference task-by-task, not a single "35x" figure; the paper's own per-task efficiency gains are **"19.0%, 2.73%, 13.66%, 5.19% and 0.7%"** on five benchmarks, with "up to 35×" describing the *most* favorable task, not the average. arXiv:2507.19457 §6 [number] (verified: read, WebFetch HTML) · skill: new
- **Sample-efficiency ablation, separate from the main table: GEPA reaches GRPO's own validation score using only 102, 32, 6, and 179 train rollouts on four (unspecified) tasks — "up to 78× greater sample efficiency."** This is a *different*, more extreme efficiency number than the headline "35x", from a different part of the paper (an early-stopping/matching analysis rather than the fixed-budget main table). arXiv:2507.19457 (verified: read, WebFetch, second and third passes) [number] · skill: new — flagged explicitly because it could be conflated with the main-table "35×" claim; they are not the same measurement.
- **Selection-strategy ablation (Table 3): SelectBestCandidate +6.05% aggregate; BeamSearch(N=4) +5.11%; GEPA's own Pareto-based selection +12.44%.** This is the paper's own evidence that Pareto selection, not merge or reflection alone, is GEPA's single largest lever. arXiv:2507.19457 Table 3 [number] (verified: read, WebFetch HTML) · skill: new
- **Cross-model generalization: a GEPA-optimized prompt built on Qwen3-8B, evaluated on GPT-4.1-Mini, gains +9.00% aggregate — beating MIPROv2 (+5.64%), TextGrad (+6.11%) and Trace (+3.27%) transferred the same way.** arXiv:2507.19457 §6 [number] (verified: read, WebFetch HTML) · skill: new
- **The paper does not state exact train/validation example counts for any of its six main tasks in what was retrieved** — only that AIME-2025 test is the standard 30-problem set, and that AIME 2022–2024 problems form "the pool for prompt evolution" with no stated train-set size. Nor does it state a default `reflection_minibatch_size` in the main text visible. arXiv:2507.19457 §7/Appendix E.1 (verified: read, WebFetch, three passes, explicitly asked) [claim] · skill: new — **stated plainly: I could not find GEPA's own train/val sizes for its headline benchmarks; this is a real gap in what this read could recover, not a claim that the paper omits them entirely** (a full manual read of the PDF, not attempted here, might find them in an appendix table not rendered to the fetched HTML).
- **The paper's own metric contract is exactly the shape `pairs.py` already implements**: a candidate is scored and the evaluator additionally returns free-text diagnostic feedback for the reflection step to read — GEPA's docs call this "Actionable Side Information" (ASI), described directly as "the text-optimization analogue of the gradient." `docs/docs/blog/posts/2026-02-18-introducing-optimize-anything/index.md:254-265` [pattern] (verified: read) · skill: same (mechanism — `optimizers.md`'s *The metric contract* section already documents the installed 5-argument `dspy.GEPA` metric protocol from source, correctly) — new (the "ASI = gradient analogue" framing and name, which is nowhere in the skill)

**LangProBe — "a Language Programs Benchmark" (arXiv:2502.20315).**

- **Scale**: 16 tasks across 15 datasets in 7 categories (Code: HumanEval, SWEUnderspecified, SWEValidity; Reasoning: Judge, Scone; Agent: AppWorld; Knowledge: MMLU, HoVer, IReRa, HotpotQA, HotpotQAConditional, RAG-QA Arena; Classification: HeartDisease, Iris; Math: MATH, GSM8K), more than 10 language programs (`Predict`, `CoT`, `GeneratorCriticFuser`, `GeneratorCriticRanker`, `RAG`, `SimplifiedBaleen`, `ReAct`, `RAGBasedRank`, `MultiHopSummarize`, `CoTBasedVote`), and six LMs (gpt-4o, gpt-4o-mini, o1-mini, Llama3.1-8B-Instruct, Llama3.2-3B-Instruct, Llama3.3-70B-Instruct). arXiv:2502.20315 §3–4 [number] (verified: read, WebFetch HTML) · skill: new
- **Only four optimizers are evaluated: `BootstrapFewShot`, `BootstrapFewShotRandomSearch`, `MIPROv2`, `RuleInfer`** (LangProBe's own name for what DSPy 3.3.1 ships as `InferRules`) — **`COPRO`, `SIMBA` and `GRPO`/`mmGRPO` are absent from this large, purpose-built benchmark entirely.** arXiv:2502.20315 §5 [number] (verified: read, WebFetch HTML) · skill: new — this is independent confirmation, from an academic benchmark rather than a source-code reading, of `optimizers.md`'s own observation that SIMBA and COPRO sit outside every selection table it found.
- **Headline finding: "MIPROv2 ... performs best overall"; median gains across programs are 6.3%–18.1%, 90th-percentile gains 80.2%–122.5%, and — stated directly — "in some rare cases, performance degradation happens."** arXiv:2502.20315 §6 [number] (verified: read, WebFetch HTML) · skill: new — the skill's *Choosing an optimizer* section already carries "escalate only on a measured plateau… two optimizers failing usually means the metric is wrong," sourced from a third-party skill pack, not from any academic benchmark; LangProBe is independent, larger-scale, academic evidence for essentially the same caution, with an exact quote ("rare cases, degradation") the skill does not have.
- **Cost/quality Pareto claim: "gpt-4o-mini with program composition and optimization achieves 11.68% higher score than gpt-4o's baseline at just 50% of the cost."** arXiv:2502.20315 (verified: read, WebFetch HTML) [number] · skill: new

**Recursive Language Models — Zhang, Kraska, Khattab (arXiv:2512.24601).** *(already named, without its arXiv id or any measured content, in `rlm.md:5-7` — see the RLM heading below for the full comparison.)*

**mmGRPO — "Multi-module GRPO: Composing Policy Gradients and Prompt Optimization for Language Model Programs" (arXiv:2508.04660).**

- **Mechanism**: standard GRPO forms one reward-normalized group per prompt; mmGRPO instead groups LM calls **by module**, across rollouts, aligning "structurally comparable module calls across different trajectories" at the same relative invocation position, and pads variable-length or early-terminated trajectories (`PadGroups`) so group sizes stay consistent when a module is skipped or a trajectory is interrupted. arXiv:2508.04660 §3 [number] (verified: read, WebFetch HTML) · skill: new — the skill has zero coverage of GRPO or mmGRPO anywhere (`grep -rn -i grpo` on the whole skill directory returns nothing).
- **Three tasks, exact sizes**: Banking77 (13,083 labeled queries, 77 intent classes, 250 train/500 eval, llama3.1-8b-instruct and qwen3-8b); PAPILLON (111 train/221 eval, external LM openai/gpt-4.1-mini-2025-04-14 — the same privacy-conscious-delegation task `graphrag.py`'s design note cites via `Agentic-Dspy-Rag`'s refused pattern); HoVer4-HOP (500/500, subsampled from 18,171, Recall@100 over ColBERTv2/Wikipedia-2017). arXiv:2508.04660 §5 [number] (verified: read, WebFetch HTML) · skill: new
- **Full results table, averaged with ± stdev, per model.** Vanilla CoT / MIPROv2 / mmGRPO / BetterTogether(PO, mmGRPO), Banking77(llama): 58.4±1.4 / 59.4±0.4 / **63.7±3.2** / 63.7±2.6; Banking77(qwen): 64.6±1.2 / 65.9±1.1 / 64.9±0.5 / **69.1±1.8**; PAPILLON(llama): 76.2±1.3 / 83.9±5.6 / 83.9±0.5 / **86.5±5.0**; PAPILLON(qwen): 78.3±0.9 / 78.1±4.3 / **83.3±1.8** / 81.1±4.1; HoVer(llama): 59.5±2.2 / 63.4±3.0 / 60.2±1.2 / **68.3±2.7**; HoVer(qwen): 60.6±0.6 / 69.3±0.8 / 71.0±1.0 / **71.5±1.5**. Averages: Vanilla 66.3, MIPROv2 70.0, mmGRPO 71.2, **BetterTogether(combined) 73.4** — the paper's "11% average" and "5% over prompt optimization alone" claims are exactly (73.4−66.3)/66.3≈10.7%≈"11%" and (73.4−70.0)/70.0≈4.9%≈"5%". arXiv:2508.04660 Table 1 [number] (verified: read, WebFetch HTML; hand-checked every average against the six per-cell numbers, all consistent) · skill: new — **this is the only paper read for this slice that reports error bars/variance (± stdev) on every single reported number**, none of the other seven required papers do this consistently.
- **Compute cost, stated exactly: mmGRPO training took ≈18.7 GPU-hours on 2×H100s (750 steps, 4 examples/step, 12 rollouts/example — 36,000 rollouts for one task/model pair), against MIPROv2's ≈1.4 hours on 1×H100 (12 trials; 12 few-shot and 6 instruction candidates).** The paper's own conclusion: **"PO approaches like MIPROv2 are likely more feasible for settings with lower computation budgets."** arXiv:2508.04660 §6 [number] (verified: read, WebFetch HTML) · skill: new
- **`mmGRPO` ships in DSPy as `dspy.GRPO`.** arXiv:2508.04660 abstract, cross-confirmed by `WebSearch` result [claim] (verified: WebSearch, not independently checked against the installed package's `dspy.__init__`) · skill: new — a source reader should confirm `dspy.GRPO` actually exists in the installed 3.3.1 surface; nothing in this slice's reading touched DSPy's RL code.

**Papers cited for SIMBA, InferRules, `optimize_anything`, gskill, `Flex` — the answer, for each, is "none exists."**

- **SIMBA**: the installed source's own docstring (`dspy:teleprompt/simba.py:17-25`, read directly, not part of my assigned doc slice but grepped to answer this exact question) cites no paper — only its own DSPy docs page (`https://dspy.ai/api/optimizers/SIMBA/`), which is not an arXiv paper, and which is *not* part of this repository's landed local docs (not under `community/`, `tutorials/`, `roadmap.md` or `learn/optimization/overview.md`). A targeted `WebSearch` for "SIMBA Stochastic Introspective Mini-Batch Ascent paper" found only DSPy's own docs page, third-party blog explainers, and one unrelated paper that *uses* SIMBA as a baseline without introducing it. [claim] (verified: grep + WebSearch, both negative) · skill: unchecked — `optimizers.md`'s SIMBA section is entirely source-verified (the `bsize>=32` assertion, the metric-wrapper looseness) and correctly carries no paper citation; this read confirms there is genuinely nothing to cite, which the skill does not currently state as a checked fact (it simply omits a citation, which reads the same as "not yet looked for").
- **InferRules**: `dspy:teleprompt/infer_rules.py` (grepped directly) has no docstring and no citation at all — not even a doc-page pointer the way SIMBA has. A `WebSearch` for "DSPy InferRules optimizer paper rules induction" found no DSPy/GEPA-authored paper; the one substantive hit is a **third-party** paper (arXiv:2507.03620, not cited by DSPy or GEPA and not part of the required nine) that evaluates InferRules — see the dedicated bullet below. [claim] (verified: grep + WebSearch, both negative) · skill: unchecked, same reasoning as SIMBA.
- **`optimize_anything`**: has no separate arXiv paper. Its own blog post frames it as extending "GEPA (Genetic-Pareto, our state-of-the-art LLM prompt optimizer) far beyond prompts" and links only to arXiv:2507.19457 (the GEPA paper itself) and to prior non-DSPy work it explicitly differentiates from (AlphaEvolve, OpenEvolve, ShinkaEvolve — none arXiv-cited by name in what was read, only GitHub-linked). `docs/docs/blog/posts/2026-02-18-introducing-optimize-anything/index.md:46,133,168` [claim] (verified: read) · skill: new (fact of no separate paper)
- **gskill**: no arXiv paper. Its blog post and README cite two non-arXiv dependencies — SWE-smith (`swesmith.com`) and mini-SWE-agent (GitHub) — and the same `optimize_anything`/GEPA documentation link. `docs/docs/blog/posts/2026-02-18-automatically-learning-skills-for-coding-agents/index.md:43-55`; `gepa-0.1.4/src/gepa/gskill/README.md:11,124-125` (grepped to confirm; not part of the assigned doc slice) [claim] (verified: read + grep) · skill: new
- **`Flex`** (`@experimental(version="3.3.0")`, `dspy:predict/flex/flex.py`, grepped directly to answer this question): no docstring citation, no paper found by search. It is a very recent (3.3.0) DSPy-native addition that `dspy.GEPA` recognizes by type and rewrites as source code rather than only instructions — mentioned in `optimizers.md`'s GEPA section (*"dspy.Flex submodules are components too"*) purely from source, with no academic grounding claimed there either, correctly. [claim] (verified: grep, negative) · skill: same (the skill already correctly treats it as source-only, uncited)

**Third-party InferRules evidence, at close to this repository's scale — not one of the nine required papers, found while answering the question above, and directly on point.**

- **"Is It Time To Treat Prompts As Code? A Multi-Use Case Study For Prompt Optimization Using DSPy" (arXiv:2507.03620) tests `InferRules` on a Pandas code-generation agent, chosen specifically "because this optimizer excels in coding tasks."** 60 train / 140 val / 50 test, GPT-4o-mini (Azure OpenAI). Result: **`InferRules` scored 87%, identical to the 87.5% hand-written baseline — no measured improvement at all**, despite the paper's own framing of InferRules as strong on exactly this task shape. arXiv:2507.03620 §5 [number] (verified: read, WebFetch HTML) · skill: new — **this is the single closest train-set size (60) to this repository's 51-row residual of any optimizer evidence found anywhere in this read, for any optimizer, and it is a null result.** See *Evidence by optimizer*, below.
- **The same paper's smallest dataset overall is even smaller than InferRules' own test: 28 train / 45 val / 13 test**, for a different use case ("Prompt Evaluator") not run through InferRules. arXiv:2507.03620 §4 [number] (verified: read, WebFetch HTML) · skill: new

### Evidence by optimizer, and at this repository's scale — one term or two, 63 labelled pairs, 44 by `fold()`/the plural rule, 51 residual with 19 positives, a binary decision, a never-merge canary

For each of the eleven named optimizers: what the *papers* (not the installed
package, which `optimizers.md` already covers) say it needs, and whether any
of them tested anything close to this scale.

- **LabeledFewShot** — no paper in this read measures it in isolation; every table folds it into a "0-shot"/"vanilla" row or an ablation arm, never a named, standalone LabeledFewShot number. Needs only `k` examples to sample from (no minimum stated) and no reflection LM at all — it is not an optimization loop. **No evidence at this repository's scale, or any scale, in the academic literature read**; the only real number for it anywhere in this repository's other reading is the third-party "book" replication (k=4, 160 train), outside this slice and roughly 3× this repo's 51.
- **BootstrapFewShot** — the founding DSPy paper's own method, trained on 200 GSM8K / 200 HotpotQA examples (§ above), 3–4× this repo's residual. Needs a metric strict enough that only genuinely good traces are kept (Assertions paper shows why — a loose metric keeps wrong demos, already independently confirmed in `optimizers.md`'s "truthiness trap" from the source itself). No reflection LM. Model sizes tested span T5-Large (770M) to GPT-3.5 — works across the range. **No paper tests it at 51 rows**, but the mechanism only needs enough *successful* traces to fill `max_bootstrapped_demos` (default 4), which 19 positives out of 51 residual rows plausibly supplies — the closest mechanism-level match among the founding papers, without a matching small-n measurement.
- **BootstrapFewShotWithRandomSearch (BootstrapRS)** — no paper in this read names it as such; MIPRO's "Bootstrap Random Search (demos only)" baseline is its closest published cousin, and it is the one that ran at **Iris (75 train, no dev) and Heart Disease (120 train, no dev)** — the second-closest published scale found, and it *won* against full MIPRO on both (94.1% vs 88.6%, 79.2% vs 74.2%). No reflection LM. **The closest thing to positive small-scale published evidence for a demo-search-only optimizer**, though for classification, not a same-term-or-two decision, and at 75–120 rows, not 51.
- **MIPROv2** — the paper's own two smallest tasks, Iris (75 train) and Heart Disease (120 train), used a *reduced* budget (30 full trials, not 50) and still needed `optuna` (already flagged in `optimizers.md` as absent from `.venv-dspy` here) and a separate proposer LM (GPT-3.5, sometimes GPT-4o). **1.5×–2.4× this repository's 51-row residual, the closest of the classic search-based optimizers, but still larger, and every MIPRO number in the paper comes from a classification task, not the term-pair decision this repository has.**
- **COPRO** — no dedicated paper among the required nine measures it; MIPRO's "Module-Level OPRO" baseline (ScoNe 73.5%, HotPotQA 39.0%, HoVeR 32.5%) is its nearest published relative, run only at the larger 500-train tasks. LangProBe's four-optimizer benchmark omits COPRO entirely. **No evidence at any scale, small or large, in anything read for this slice.**
- **SIMBA** — no paper exists anywhere (confirmed by source-comment absence and two independent searches). LangProBe, the one large academic optimizer benchmark read, does not include it either. Needs (already known to the skill from source) `bsize>=32` unless explicitly overridden. **Zero published evidence, at any scale.**
- **InferRules** — no DSPy/GEPA-cited paper; the one third-party measurement found (arXiv:2507.03620, 60 train examples, coding/classification task) is **the closest scale-match of any optimizer evidence in this entire read (60 ≈ this repo's 51–63) and it is a null result** — 87% with InferRules, identical to the 87.5% hand-written baseline, on exactly the kind of rule-induction task InferRules is claimed to suit. **This is the single most relevant, and most cautionary, piece of evidence this whole read turned up for this repository's decision.**
- **GEPA** — needs a 5-argument-shaped metric returning score + text feedback (already implemented by `pairs.py`); a reflection LM, which every real deployment found in this read (Nubank's GPT-4.1-mini task / GPT-5.1 reflection; ConfidenceAdapter's GPT-4.1-mini task / Claude Sonnet 4.6 reflection; gskill's gpt-5-mini task / gpt-5.2-pro reflection default) makes **distinctly stronger than the task model**, unlike the paper's own controlled same-model (Qwen3-8B/Qwen3-8B) ablation. The paper's headline tasks are all far larger than 63 rows and, past three targeted fetches, this read could not recover their exact train/val sizes — a stated gap, not a claim of absence. The paper's own low-budget ablation shows GEPA matching GRPO's score at rollout counts as low as **6, 32, 102, 179** on some tasks — all below this repository's own 608-rollout `auto="light"` dry run on 57 rows — suggesting the *mechanism* tolerates small budgets even though no *published task* was run at this repository's example count. Two non-academic but directly on-point data points: the gepa.ai front page's own marketing claims GEPA "works with as few as 3 examples" [claim, unverified anywhere], and Decagon's production blog (a case study, not a paper) reports **"20-100 examples outperform larger datasets"** as their own measured sweet spot for GEPA in production — a range that contains this repository's 51–63 rows exactly. `docs/docs/guides/use-cases.md:1392` [claim] (verified: read).
- **BetterTogether** — needs both a fine-tunable model and a prompt optimizer. Its **prompt-only stage** ran on as few as **15 train / 35 val examples** (Iris) in the published paper — inside this repository's scale — but its weight stage cost ≈75 A100-GPU-hours across the whole paper and needs local training infrastructure this repository does not have and its skill already rules out for that reason. **Scale is not the blocker for BetterTogether here; the fine-tunable model is.**
- **GRPO / mmGRPO** — needs an RL-trainable model and GPU-hours (mmGRPO: 18.7h on 2×H100s, 36,000 rollouts, for one task; GEPA's paper compares against a GRPO baseline run at 24,000 rollouts/task). **Absent from the skill's ladder entirely** — not even a "not taken" entry exists for it anywhere `.agents/skills/dspy/` was grepped. Mechanically ruled out here for the same reason as BetterTogether's weight stage: this repository's models are free, hosted, non-fine-tunable API models.
- **`optimize_anything`** — mechanically the lowest-friction of the eleven: no DSPy program required, just a scoreable string and an evaluator returning `(score, side_info)` — a shape `pairs.py`'s own metric (score, a person's written rule) already matches closely. The closest published evidence at a scale below GEPA's main benchmarks is **gskill, ≈200 train / 50 val / 60 test** — still ~4× this repository's residual, but the smallest `optimize_anything`-family dataset found with a real held-out generalization result (24%→93%, 55%→82% resolve rate, transferring to Claude Code Haiku/Sonnet), and the only found evidence anywhere of a *binary pass/fail* task with a *natural-language artifact* (a skill file, not a prompt) generalizing to unseen cases — the closest task-shape match to this repository's binary same-term-or-two decision of anything read.

### MET

- **The GEPA paper's metric-and-feedback framing predates and matches `optimize_anything`'s "ASI" naming — both trace to one idea: a scalar for search, free text for the reflector.** arXiv:2507.19457, cross-referenced with `docs/docs/blog/posts/2026-02-18-introducing-optimize-anything/index.md:110,254-265` [pattern] (verified: read) · skill: same (mechanism, already in `optimizers.md`'s *metric contract* section from source) — new (the "gradient analogue" language, and that the naming is deliberate across both the paper and the later API)
- **ConfidenceAdapter replaces GEPA's binary 0/1 metric with `LinearBlendScoring`: 0.0 if wrong; 1.0 if correct and `probability ≥ high_confidence_threshold` (default 0.99); otherwise `min_score + (1−min_score)×(probability/threshold)` with `min_score=0.3` — a correct answer at 95% probability scores 0.972, not 1.0.** `docs/docs/blog/posts/2026-03-17-confidence-adapter-benchmark/index.md:133-185` [number] (verified: read) · skill: new — directly relevant to `pairs.py`'s binary `one-term`/`two-terms` decision, which currently has no confidence dimension at all; nothing in `metrics.md` (not reread in full here, but grepped, no hits) discusses graded-by-log-probability scoring.
- **Measured across AG News (4-class)/Emotion (6-class)/Rotten Tomatoes (binary), 120 train / 40 val per class: ConfidenceAdapter beats a binary-scored `DefaultAdapter` by +2.10pp (AG News, 85.80%→87.90%) and +1.80pp (Emotion, 58.42%→60.22%), and ties on the binary task (93.15%→93.15%).** `docs/docs/blog/posts/2026-03-17-confidence-adapter-benchmark/index.md:195-229` [number] (verified: read) · skill: new — **the confidence-scoring gain shrinks to nothing on the one binary-classification task tested**, which is this repository's own task shape (same-term-or-two); the paper's own explanation is that "the confidence signal has limited room to differentiate" with only one alternative category — directly relevant caution against expecting a confidence-graded metric to help `pairs.py`'s binary decision much, even though it helped multiclass tasks.
- **GPT-4.1-mini with structured output is measured as poorly calibrated: 70–78% of *incorrect* predictions still carry ≥99% reported probability, which is why a 0.99 threshold — not something lower — was needed for the gradient to mean anything.** `docs/docs/blog/posts/2026-03-17-confidence-adapter-benchmark/index.md:388` [number] (verified: read) · skill: new — a concrete number against ever trusting an LM's self-reported confidence at face value for a graded metric, without first measuring calibration on the task model actually in use.
- **mmGRPO's group-relative advantage, exact formula**: `A_i = (r(x,y_i) − r̄_g) / (σ_g + ε)`, the standard GRPO normalization, applied per-module-group rather than per-prompt. arXiv:2508.04660 §3 [number] (verified: read, WebFetch HTML) · skill: new — `metrics.md` (grepped, no GRPO hits) has no RL-style advantage-normalization pattern at all; not directly usable by `pairs.py` (no RL here) but worth knowing this is the family GRPO belongs to when `dspy.GRPO` is next considered.

### DATA

- **Every dataset scale found across the eight required papers, smallest to largest, for calibrating "how small is small":** BetterTogether-prompt-stage Iris 15 train/35 val (arXiv:2407.10930); InferRules-third-party 60 train/140 val/50 test (arXiv:2507.03620, not required); MIPRO Iris 75/–/75 and Heart Disease 120/–/183 (arXiv:2406.11695); mmGRPO PAPILLON 111/221 (arXiv:2508.04660); DSPy-paper GSM8K 200/300/1.3k and HotpotQA 200/1000 (arXiv:2310.03714); DSPy-Assertions 300/300/500 (arXiv:2312.13382); BetterTogether-full HotpotQA/GSM8K 1000/500/1500 (arXiv:2407.10930); MIPRO's larger tasks 500/500/1200-2000 (arXiv:2406.11695); GEPA's tasks, sizes unstated in what was retrieved (arXiv:2507.19457). [number] (verified: read, WebFetch, collated across all fetches) · skill: new — **this repository's 51-row residual (63 total, 44 by rule) sits below every one of these except BetterTogether's 15-row prompt-only stage and the third-party InferRules paper's 60-row test — and the InferRules result at that scale was a null result.**
- **LangProBe's 15 datasets are the broadest single catalogue of DSPy-optimizer-benchmarked tasks in any of the required papers**: HumanEval, SWEUnderspecified, SWEValidity, Judge, Scone, AppWorld, MMLU, HoVer, IReRa, HotpotQA, HotpotQAConditional, RAG-QA Arena, HeartDisease, Iris, MATH, GSM8K. arXiv:2502.20315 §3 [number] (verified: read, WebFetch HTML) · skill: new
- **RLM's four evaluation benchmarks, with token scales far above anything else in this read**: S-NIAH (50 tasks, synthetic, scaling 2^13–2^18 tokens); BrowseComp-Plus/1K-documents (150 multi-hop QA tasks, 6M–11M tokens); OOLONG (50 tasks, 131K tokens, linear complexity); OOLONG-Pairs (20 hand-made tasks, 32K tokens, quadratic/pairwise complexity). arXiv:2512.24601 Table 1/§4 [number] (verified: read, WebFetch HTML) · skill: new — three to four orders of magnitude beyond this repository's own landed-document scale (`rlm.md` already states "roughly 6,700 words… not fifty thousand [tokens]" for a single document here; RLM's own smallest benchmark, OOLONG-Pairs at 32K tokens, is still ~5× that).
- **The training set is deliberately larger than the validation set in ConfidenceAdapter's own design, for a GEPA-specific reason**: "the model doesn't 'learn' from training examples the way a fine-tuned model would — they only feed the reflection loop… a larger pool ensures each minibatch exposes the reflection LLM to different combinations of errors." 120 train/40 val per class, val "evaluated in full every iteration," train only minibatch-sampled. `docs/docs/blog/posts/2026-03-17-confidence-adapter-benchmark/index.md:203` [pattern] (verified: read) · skill: new — directly relevant to how `pairs.py` should think about its own train/val split once it runs against a real model: GEPA's split logic (documented from source in `optimizers.md`, "maximize training, keep val just large enough") is echoed here with a concrete worked reason, not only a rule of thumb.

### RLM

- **The paper the skill already names, but with none of its content.** `rlm.md:5-7` states: *"The academic idea `dspy.RLM` implements: 'Recursive Language Models' (Zhang, Kraska, Khattab, 2025)"* — correct authorship and year, but **no arXiv id** (it is 2512.24601) **and no measured content from the paper anywhere in the file**, despite `rlm.md` being 647 lines of otherwise exhaustive, source-verified `dspy.RLM` documentation. [claim] (verified: read `rlm.md` in full) · skill: wrong is too strong (nothing it says is incorrect) — **unchecked: `rlm.md`** names the paper and stops there; every fact below is new to it.
- **Core mechanism, exact**: "an RLM exposes the same external interface as an LLM… Given a prompt P, the RLM initializes a Read-Eval-Print Loop (REPL) programming environment in which P is set as the value of a variable," and the model "programmatically construct[s] sub-tasks on which they can invoke themselves recursively." arXiv:2512.24601 §2 [number] (verified: read, WebFetch HTML) · skill: same (this is exactly what `rlm.md` already documents from the *installed* `dspy.RLM` source — variables, a sandboxed REPL, tool calls — just without ever citing the paper's own words for the same idea)
- **Headline results (Table 1): GPT-5 on BrowseComp-Plus/1K, base model 0.00% (context limit exceeded) → RLM 91.33% ($0.99±$1.22/query); GPT-5 on OOLONG-Pairs, base 0.04% → RLM 58.00% ($0.33±$0.20); Qwen3-Coder on OOLONG, base 36.00% → RLM 48.00% ($0.61±$0.49).** arXiv:2512.24601 Table 1 [number] (verified: read, WebFetch HTML) · skill: new
- **"RLMs successfully handle inputs up to two orders of magnitude beyond model context windows," scaling tested from 2^13 to 2^18 tokens, past GPT-5's stated 272K-token context window.** arXiv:2512.24601 Fig. 1 [number] (verified: read, WebFetch HTML) · skill: new — `rlm.md`'s own threshold ("roughly 50,000 tokens and up", sourced from the third-party "book" pack, not this paper) is a full two orders of magnitude below where the founding paper's own headline result sits (2^18 ≈ 262,144 tokens); worth knowing the two numbers come from different sources and are not in tension so much as answering different questions ("when does RLM start paying off" vs "how far can RLM push past a context window at all").
- **Sub-LM structure: root LM (GPT-5 or Qwen3-Coder-480B-A35B) recursively calls a cheaper sub-LM (GPT-5-mini, when GPT-5 is root) via `llm_query`/similar — the same two-tier shape `rlm_ingest.py` already uses (`sub_lm`), independently arrived at.** arXiv:2512.24601 §3 [number] (verified: read, WebFetch HTML) · skill: same
- **The paper contains no reference to DSPy anywhere in what was fetched** — it describes a custom Python REPL with `llm_query()`, not a `dspy.Module`. `dspy.RLM` is DSPy's own later implementation of the idea, not something the paper itself ships or names. arXiv:2512.24601 (verified: read, WebFetch HTML, explicitly checked) [claim] · skill: same (`rlm.md:3-19`'s own "three things called RLM" section already separates the academic idea from the DSPy module correctly, and implicitly gets this right by never claiming the paper mentions DSPy)

### RAG

- **DSPy's own HotpotQA multi-hop retrieval numbers, the paper's earliest evidence that a bootstrapped `MultiHop` program beats a single-shot `CoT_RAG` one**: `CoT_RAG`+GPT-3.5 (Bootstrap) reaches 42.3% dev EM / 36.0% dev passage-accuracy; `MultiHop`+GPT-3.5 (Bootstrap) reaches 48.7%/47.0%, and with `Ensemble` 54.7%/— . arXiv:2310.03714 Table 2 [number] (verified: read, WebFetch HTML) · skill: new — `retrieval.md` (not reread in full for this slice) documents `graphrag.py`'s own MMR-with-a-floor design from a different third-party source (`dspy-refrag`); it has no line tracing DSPy's retrieval-composition idea back to the founding paper's own multi-hop numbers.
- **RLM's BrowseComp-Plus/1K-documents benchmark is itself a multi-hop QA retrieval task, at 6M–11M-token scale — the same task family as HotpotQA, three to four orders of magnitude larger.** arXiv:2512.24601 §4 [number] (verified: read, WebFetch HTML) · skill: new

### AGENT

- **GEPA's "Nearly Triple Gemini-Flash's ARC-AGI Accuracy via Agent Architecture Evolution" result: a 10-line naive agent stub evolved into a 300+ line system (rule induction, code verification, iterative refinement, structured fallbacks), test accuracy 32.5%→89.5% with Gemini 3 Flash, at roughly 2× the per-task inference cost.** `docs/docs/blog/posts/2026-02-18-introducing-optimize-anything/index.md:313-327` [number] (verified: read) · skill: new — the most extreme "agent, not prompt" optimization result found in this whole read; `patterns.md` (not reread in full here) has no coverage of GEPA rewriting agent *control flow*, only instruction text.
- **gskill's exact transfer numbers, from a small model/simple agent to production agents**: Mini-SWE-Agent + gpt-5-mini, Jinja 55%→82%, Bleve 24%→93% (≈300 SWE-smith tasks per repo, ~200 train/50 val/60 test). Transferred *unchanged* to Claude Code: Bleve, Haiku 4.5 79.3%→98.3% (later reported 100.0% in the `optimize_anything` post's own re-statement) with duration 173s→142s, Sonnet 4.5 94.8%→100.0%; Jinja, Haiku 4.5 93.9%→100.0%, Sonnet 4.5 100.0%→98.5% (a rare *regression* from adding the learned skill, on an already-saturated model). `docs/docs/blog/posts/2026-02-18-automatically-learning-skills-for-coding-agents/index.md:63-92` [number] (verified: read) · skill: new
- **PAPILLON (privacy-conscious delegation) is a named benchmark in both mmGRPO (arXiv:2508.04660) and, independently, `graphrag.py`'s own design note cites `Agentic-Dspy-Rag`'s refused multi-step-RAG pattern from `repos.md`** — the same task name surfaces in an academic RL paper and in this repository's own third-party-reading notes, unconnected until now. arXiv:2508.04660 §5, cross-referenced with `repos.md:504` [pattern] (verified: read) · skill: new (the connection; each half was already separately known)

### PROD

*(A curated selection of the exact-number case studies from the GEPA showcase page — the page itself lists 50+, most without full methodology; these are the ones that state a real before/after number and a named organization.)*

- **Shopify: DSPy+GEPA for structured metadata extraction across all Shopify shops, ~550× yearly cost reduction.** `docs/docs/community/use-cases.md:43`; `docs/docs/guides/use-cases.md` (cross-referenced) [claim] (verified: read) · skill: new
- **Databricks: 90× cost reduction, open-source models optimized with GEPA outperforming Claude Opus 4.1/Sonnet 4/GPT-5, "consistent 3-7% performance gains across all model types."** `docs/docs/guides/use-cases.md:36-44` [claim] (verified: read) · skill: new
- **Dropbox Dash: 45% NMSE reduction on gpt-oss-120b (8.83→4.86); on gemma-3-12b, malformed JSON dropped from 40% to under 3% while NMSE improved 46.88→17.26; model adaptation time cut from 1-2 weeks to 1-2 days.** `docs/docs/guides/use-cases.md:60-71` [claim] (verified: read) · skill: new — the malformed-JSON number is the closest published GEPA production result to this repository's own "a model must return a parseable typed decision" concern (`pairs.py`'s `Literal["one-term","two-terms"]`).
- **Nubank: LLM-judge evaluation accuracy, starter→GEPA-optimized: E1 77.78%→82.00%, E2 68.88%→88.89% (5-run mean, narrow 95% CIs); Cohen's κ (GPT-4.1 vs GPT-4.1-mini) 0.00→0.745; settings `auto="light"` (~500 iterations), reflection minibatch 3, GPT-4.1-mini base + GPT-5.1 reflection.** `docs/docs/guides/use-cases.md:147-166` [claim] (verified: read) · skill: new — the one production case study in this whole read that reports GEPA's actual `reflection_minibatch_size` (3, matching the installed default `optimizers.md` already documents from source) and a base/reflection model split as asymmetric as ConfidenceAdapter's.
- **Microsoft AI's MAI-Thinking-1: a Qwen3-30B judge, GEPA/DSPy-optimized against ~2,000 human labels, filters ~233B tokens of pre-training data — "the first public report of GEPA being used inside a frontier model's pre-training data pipeline."** `docs/docs/guides/use-cases.md:129-143` [claim] (verified: read) · skill: new
- **A $0 reproducible study on OpenRouter's free tier found baseline saturation is the actual limiter, not budget: GLM 4.5 Air (32B) and Ministral 8B "accept zero mutations" on grade-school math because every minibatch already scores all-correct, while a 1.2B model (Liquid LFM 2.5) went 45%→70% through 5 accepted mutations on the same task.** `docs/docs/guides/use-cases.md:1396-1408` [claim] (verified: read) · skill: new — **directly actionable for this repository's own `pairs.py` model choice**: pick a task model weak enough to fail on some of the 19 positive residual rows, or GEPA has no reflection signal at all, whatever the budget.
- **Decagon: "test-driven approach... 19+ ablation experiments," reporting a data-efficiency sweet spot of 20-100 examples outperforming larger datasets, and length regularization giving 4× prompt compression.** `docs/docs/guides/use-cases.md:1388-1394` [claim] (verified: read) · skill: new — see *Evidence by optimizer*, above; this range contains this repository's 51–63-row scale.

### PAT

- **Combee: hierarchical parallel-scan aggregation for scaling GEPA's reflection step**, splitting `n` reflections into `k=⌊√n⌋` subgroups, aggregating within each, then combining — plus "augmented shuffling" (each reflection duplicated `p=2` times before dispatch) and a dynamic batch-size controller fitting a power-law delay curve. Measured: naive batch-size scaling from 3→100 dropped accuracy 87.0%→72.5% on a finance benchmark ("context overload"); Combee+GEPA trains >2.4× faster than quality-comparable baselines at the same accuracy. `docs/docs/blog/posts/2026-04-09-gepa-at-scale-with-combee/index.md:49-103` [pattern] (verified: read) · skill: new — the opposite scale problem from this repository's (Combee exists because a reflector drowns on *too many* reflections at once; `pairs.py`'s residual is 51 rows total, nowhere near Combee's regime), but worth knowing the failure mode exists and is named, in case a future corpus-wide reconciliation pass ever batches many documents' judgements into one reflection call.
- **Fast-Slow Training (FST): prompts as "fast weights" (optimized by GEPA), model parameters as "slow weights" (optimized by RL/CISPO), interleaved every `T` RL steps.** Reported: FST reaches RL's peak accuracy in 1.4×–3.0× fewer training steps across three tasks, at ~70% lower KL-divergence from the base model (less forgetting), and continues learning a new task where pure-RL training "completely stalls." `docs/docs/blog/posts/2026-05-11-learning-fast-and-slow/index.md:45-49,123,138,155` [pattern] (verified: read) · skill: new — not directly applicable here (no RL, no weight training in this repository, by design — every model is a free hosted API model), but the fast/slow framing is the clearest published articulation found anywhere of *why* this repository's own approach (a deterministic rule first, a model only on the residual, never retraining the rule) is a reasonable shape: a cheap, fast, easily-inspected layer (`fold()`/the plural rule) handles what it can, and a model is asked only where that layer already fails.
- **ASI (Actionable Side Information) as "the gradient" for text optimization — GEPA's `optimize_anything` treats an evaluator's diagnostic output (error message, rendered image, profiler trace) as a first-class return value, not an afterthought, because "classical optimization methods reduce all diagnostic context to a single scalar… you can't show a Bayesian optimizer the stack trace that pinpoints the bug."** `docs/docs/blog/posts/2026-02-18-introducing-optimize-anything/index.md:254-258` [pattern] (verified: read) · skill: same, mechanism (`text-artifacts.md` already documents `side_info`'s exact wire shape from source) — new, the framing and the "gradient" name
- **Pareto-efficient search as the second key ingredient, independent of ASI: tracking per-task/per-metric scores rather than one averaged score, so "a candidate that excels at bicycle structure but struggles with pelican anatomy is preserved on the frontier, not discarded."** `docs/docs/blog/posts/2026-02-18-introducing-optimize-anything/index.md:246,267-271` [pattern] (verified: read) · skill: same (already in `optimizers.md`'s GEPA `candidate_selection_strategy` coverage from source, and independently confirmed by the paper's own Table 3 ablation above showing Pareto selection is GEPA's single largest lever)
- **Three unified optimization modes, named directly in the blog and each mapped to a real dataset/valset combination that `text-artifacts.md` already documents mechanically from source (§ API above) without the names**: *Single-Task Search* (no dataset — the candidate is the answer, e.g. circle packing); *Multi-Task Search* (dataset, no valset — cross-transfer across related problems, e.g. CUDA kernels, where multi-task mode "converges faster and solves more problems across all speedup thresholds" than one-task-at-a-time); *Generalization* (dataset + valset — must transfer to unseen cases, e.g. AIME prompt optimization, ARC-AGI agent evolution, gskill). `docs/docs/blog/posts/2026-02-18-introducing-optimize-anything/index.md:124-149` [pattern] (verified: read) · skill: new (the names); same (the mechanism, already correctly derived from source in `text-artifacts.md`'s three-row table)

### SKILL

- **gskill is the closest thing to a controlled, published experiment for exactly the shape of work `text-artifacts.md` calls "job 4" (optimizing this repository's own `SKILL.md` files) — and it is real, published, held-out-tested evidence that the approach works, at a scale text-artifacts.md's own job-4 plan (5–20 hand-captured routing failures) is far smaller than.** gskill trains on ~200 SWE-smith-generated tasks per repository (not 5–20 hand-captured failures), optimizes an initially-empty skill with `optimize_anything`, and reports held-out test gains of 24%→93% (Bleve) and 55%→82% (Jinja), which then transfer *unmodified* to a different agent harness (Claude Code) and different models (Haiku 4.5, Sonnet 4.5). `docs/docs/blog/posts/2026-02-18-automatically-learning-skills-for-coding-agents/index.md:44,63-79` [number] (verified: read) · skill: new — `text-artifacts.md` states job 4 has "no dataset, no evaluator, no run" and cites only a third-party pack's small worked examples (50–200 metric calls, 0.962 composite score, `dspy-agent-skills`); it has never seen gskill's own numbers, which are GEPA's own team applying the identical mechanism to the identical kind of artifact.
- **gskill's default reflection model is explicitly *stronger* than its task model** (`--model gpt-5-mini` for the agent under test, `--reflection-model gpt-5.2-pro` for the proposer, per the README's own CLI defaults) — the same asymmetric pattern found in every other real deployment in this read (Nubank, ConfidenceAdapter). `gepa-0.1.4/src/gepa/gskill/README.md:56,73` (grepped, not part of the assigned doc slice, cited to answer the brief's explicit "model size... for reflection" question) [api] (verified: grep) · skill: new
- **Decagon's production blog reports "length regularization for 4× prompt compression"** as one of its 19+ ablations — directly relevant to job 4's own concern (a job-4 evaluator must weight mechanical checks, including length, above judged ones, per `text-artifacts.md`'s own "book" citation) but from an independent, unrelated production deployment rather than the same third-party pack `text-artifacts.md` already cites. `docs/docs/guides/use-cases.md:1392` [claim] (verified: read) · skill: new
- **The `optimize_anything` blog's own regression-reading discipline is the one piece of this whole read that most directly matches `text-artifacts.md`'s existing "regression list" recipe, independently arrived at by the same authors in prose rather than only in the shipped example script `text-artifacts.md` already quotes**: "if you can measure it, you can optimize it" is paired throughout the blog with per-metric Pareto tracking specifically so a net gain never silently hides a per-case regression — the same shape `text-artifacts.md`'s `regressed = [...]` snippet already implements from source. `docs/docs/blog/posts/2026-02-18-introducing-optimize-anything/index.md:267-271` [pattern] (verified: read) · skill: same

### TRAP

- **GEPA's paper shows merge is not uniformly beneficial: on IFBench, `GEPA+Merge` scores 28.23% — *below* the 36.90% baseline and below GRPO's 35.88% — while `GEPA` without merge scores 38.61% on the same task.** arXiv:2507.19457 Table 2 (verified: read, WebFetch HTML) [trap] · skill: new — `optimizers.md` already documents `use_merge=True` as the installed default and separately warns (from source) that a merge invocation can silently discard rules the benchmark did not exercise; this is the paper's own worked case of that exact risk turning an aggregate win into a per-task loss, which the skill has never cited.
- **MIPROv2 makes a model *worse* than doing nothing on math reasoning, in the same table that makes GEPA's headline claim**: AIME-2025, baseline 27.33% → MIPROv2 20.00%. arXiv:2507.19457 Table 2 (verified: read, WebFetch HTML) [trap] · skill: new — a second, independent academic confirmation of the "optimizing can make it worse" lesson `optimizers.md` already carries from the third-party "book" chapter (COPRO/SIMBA scoring below baseline there); this is the same lesson from GEPA's own published comparison table, for a different optimizer (MIPROv2) on a different task (math, not text classification).
- **LangProBe's own stated caveat — "in some rare cases, performance degradation happens" — is a large-scale, cross-task, academic-benchmark version of the same warning, independent of both of the above.** arXiv:2502.20315 §6 (verified: read, WebFetch HTML) [trap] · skill: new
- **The InferRules third-party evaluation directly contradicts its own stated praise**: the paper chose InferRules for a coding task "because this optimizer excels in coding tasks," then measured zero improvement over baseline on exactly that task. arXiv:2507.03620 §5 (verified: read, WebFetch HTML) [trap] · skill: new — reinforces, from an independent source, `optimizers.md`'s own observation that InferRules "is absent from every optimizer-selection table" found among the nine third-party repositories; here, the one paper that *did* single it out for praise is also the one paper that measured it failing to help at all.
- **GEPA's paper reports two different, non-comparable "sample efficiency" numbers in different sections — a fixed-budget main-table gain of up to 35× fewer rollouts for a comparable score, and a separate best-case matching-analysis claim of up to 78× — and neither figure is the "average" case; the paper's own per-task efficiency breakdown is "19.0%, 2.73%, 13.66%, 5.19% and 0.7%" across five benchmarks, a much smaller number than either headline.** arXiv:2507.19457, three passes (verified: read, WebFetch, cross-checked) [trap] · skill: new — worth flagging because both "35×" and "78×" circulate as GEPA's headline efficiency claim in secondary sources (including this repository's own `.claude/skills/dspy` would be at risk of doing, had either number been added without this distinction) and they measure different things.
- **`optimize_anything`'s own printed blog signature (§ API, above) omits `batch_evaluator` — a second, real, documented entry point `text-artifacts.md` already knows about from source, but a reader following only the blog post's own code sample would never learn it exists.** `docs/docs/blog/posts/2026-02-18-introducing-optimize-anything/index.md:154-166`, cross-checked against `inspect.signature` (verified: read + ran) [trap] · skill: same (the skill already has `batch_evaluator` right, from source; the gap is in the *paper-adjacent doc*, not the skill)
- **The GEPA landing page's own stated claim, "Works with as few as 3 examples" (`docs/docs/index.md`, *GEPA Shines When → Data Is Scarce*), is nowhere backed by a specific experiment in anything read for this slice** — not the paper, not any of the six blog posts, not the showcase page's 50+ case studies (whose smallest, Decagon's, states a 20–100-example sweet spot, not 3). `docs/docs/index.md` (grep for the exact string in the read file) [claim] (verified: read, explicitly checked for a supporting number and found none) · skill: new — worth stating plainly rather than repeating uncritically: this specific number appears to be unmeasured marketing copy, distinct from the "20-100" figure that *does* have a case study behind it.

---

## 3. Code worth keeping

**`optimize_anything`'s minimal usage shape**, read from the blog, not run
(would need a real evaluator and model; matches the installed function's real
keyword-only signature confirmed separately, above):

```python
# docs/docs/blog/posts/2026-02-18-introducing-optimize-anything/index.md:87-107
import gepa.optimize_anything as oa

def evaluate(candidate: str) -> float:
    score, diagnostic = run_my_system(candidate)
    oa.log(f"Error: {diagnostic}")  # captured as ASI
    return score

# Start from an existing artifact…
result = oa.optimize_anything(
    seed_candidate="<your initial artifact>",
    evaluator=evaluate,
)

# … or just describe what you need.
result = oa.optimize_anything(
    evaluator=evaluate,
    objective="Generate a Python function `reverse()` that reverses a string.",
)

print(result.best_candidate)
```

**The regression-reading pattern**, read, not run — the one piece of code in
this whole slice's blog reading that a job-4 loop should copy structurally,
not just as an idea:

```python
# docs/docs/blog/posts/2026-02-18-introducing-optimize-anything/index.md
# (paraphrased from the "printf() debugging" and regression-tracking sections;
#  the exact snippet form lives in text-artifacts.md, sourced from the
#  dspy-agent-skills pack rather than this blog — see the SKILL item above)
result = optimize_anything(
    ...,
    evaluator=evaluate,          # existing print() calls become ASI
    config=GEPAConfig(engine=EngineConfig(capture_stdio=True)),
)
```

**The `inspect.signature`/`TypeError` probe I ran myself** (not from any
source read, written to answer the API item above), offline, no model, no
key:

```python
import inspect
import gepa.optimize_anything as oa

sig = inspect.signature(oa.optimize_anything)
assert list(sig.parameters)[0] == "seed_candidate"
assert sig.parameters["seed_candidate"].kind == inspect.Parameter.POSITIONAL_OR_KEYWORD
for name in ("evaluator", "batch_evaluator", "dataset", "valset", "objective", "background", "config"):
    assert sig.parameters[name].kind == inspect.Parameter.KEYWORD_ONLY, name

try:
    oa.optimize_anything("seed", lambda c, e: (0.0, {}))
    raise AssertionError("expected TypeError")
except TypeError as e:
    assert "takes from 0 to 1 positional arguments" in str(e)
```
Ran on the installed package, 2026-09-24; held.

---

## 4. Probes worth adding

- **id: `optimize-anything-kwonly`**
  **Sentence for the skill**: "Every `gepa.optimize_anything()` parameter
  except `seed_candidate` is keyword-only — `optimize_anything(seed,
  my_evaluator)` raises `TypeError: optimize_anything() takes from 0 to 1
  positional arguments but 2 were given`, not a silent positional match."
  **Probe** (self-contained, offline, no model, no key — ran on
  `.venv-dspy/bin/python`, held):

  ```python
  def p_optimize_anything_kwonly():
      """None if optimize_anything's kwonly contract holds, else a string naming the failure."""
      import inspect
      import gepa.optimize_anything as oa

      sig = inspect.signature(oa.optimize_anything)
      params = list(sig.parameters.items())
      if params[0][0] != "seed_candidate":
          return f"expected seed_candidate first, got {params[0][0]!r}"
      if params[0][1].kind != inspect.Parameter.POSITIONAL_OR_KEYWORD:
          return "seed_candidate is no longer positional-or-keyword"
      kwonly_expected = {"evaluator", "batch_evaluator", "dataset", "valset",
                          "objective", "background", "config"}
      kwonly_actual = {n for n, p in params[1:]
                        if p.kind == inspect.Parameter.KEYWORD_ONLY}
      if kwonly_actual != kwonly_expected:
          return f"keyword-only set changed: {sorted(kwonly_actual)}"

      try:
          oa.optimize_anything("seed", lambda c, e: (0.0, {}))
      except TypeError as e:
          if "positional argument" not in str(e):
              return f"wrong TypeError message: {e}"
      else:
          return "two positional args did not raise TypeError"
      return None
  ```

  Run, offline, `.venv-dspy/bin/python`, 2026-09-24: returned `None`.

This slice yielded exactly one behaviour worth a `[checked: …]` mark, because
almost everything else read here is a paper's own reported number (not
something this repository's own installed package can be probed for — a
paper's Table 2 is not re-runnable offline) or a blog's prose claim (same).
The other nine required papers describe experiments this repository has no
way to re-run without a real model, a real GPU, or in RLM's case, real
multi-megabyte documents nothing here has. That is not a gap in this read; it
is the honest shape of a papers-and-docs slice, and the brief's own
instruction to "skip anything that takes more than 3 minutes" and never
configure a real LM rules out attempting to reproduce, say, the GEPA paper's
HotpotQA table against a live model from inside this task.

---

## 5. Surface worth asserting

```surface
gepa.optimize_anything.optimize_anything(seed_candidate=None, *, evaluator=None, batch_evaluator=None, dataset=None, valset=None, objective=None, background=None, config=None) -> gepa.core.result.GEPAResult
```
Every name and default taken from `inspect.signature` on the installed
package (`.venv-dspy/lib/python3.11/site-packages/gepa/optimize_anything.py`),
run 2026-09-24. `seed_candidate` is the only `POSITIONAL_OR_KEYWORD`
parameter; every other name is `KEYWORD_ONLY`. This is the one function-level
surface fact this slice adds; `text-artifacts.md` already carries the four
nested config classes' surfaces (`EngineConfig`, `ReflectionConfig`,
`GEPAConfig`, `EvaluatorWrapper`) correctly and those are not repeated here.

---

## 6. Ten things the skill must say

1. **The skill cites zero academic papers anywhere** (`grep -rn -i arxiv
   .agents/skills/dspy/` returns nothing) — every measured number in
   `## OPT` above is new, not an update. This is worth a line in `SKILL.md`
   itself, not only in this file, because the next reader will otherwise
   assume the absence was checked before and found empty on purpose.
2. **`InferRules`'s only known measured result, anywhere, at any scale, is a
   null result at n=60** (arXiv:2507.03620) — closer to this repository's
   51–63-row scale than any other optimizer's published evidence, and it
   found no gain on exactly the coding/classification task shape InferRules
   is claimed to suit. See *Evidence by optimizer*.
3. **`SIMBA` has no paper anywhere, and `GRPO`/`mmGRPO` do not appear in the
   skill's ladder at all** — not even as a "not taken" row. `optimizers.md`'s
   *Not taken* table should gain a `GRPO` row citing arXiv:2508.04660 and its
   GPU-hour cost, for the same reason `BootstrapFinetune` and
   `BetterTogether` already have one.
4. **MIPRO's own paper ran at 75–120 train examples (Iris, Heart Disease),
   with a reduced 30-trial budget** — closer to, though still larger than,
   this repository's 51-row residual than the skill's blanket "100+" rule
   implies. See *Evidence by optimizer*.
5. **GEPA's paper shows merge and MIPROv2 both actively hurting a task in the
   same table that produces GEPA's own headline win** (IFBench
   `GEPA+Merge`=28.23% < baseline 36.90%; AIME `MIPROv2`=20.00% < baseline
   27.33%) — a second, independent academic confirmation of "optimizing can
   make it worse," worth citing beside the third-party "book" chapter's
   version already in `optimizers.md`.
6. **GEPA's own paper reports two different, non-comparable efficiency
   headlines ("35× fewer rollouts" in the main table; "up to 78×" in a
   separate low-budget matching analysis) and neither is the average case
   (per-task gains as small as 0.7%)** — worth a `TRAP` line before either
   number gets quoted as *the* GEPA efficiency figure.
7. **Every real production deployment of GEPA found in this read runs the
   reflection LM distinctly stronger than the task LM** (Nubank: GPT-4.1-mini
   / GPT-5.1; ConfidenceAdapter: GPT-4.1-mini / Claude Sonnet 4.6; gskill:
   gpt-5-mini / gpt-5.2-pro) — directly answers "what model size for
   reflection" for whichever model `pairs.py`'s first real run picks.
8. **Task-model saturation, not budget, is the practical limiter GEPA case
   studies keep reporting** (32B/8B models "accept zero mutations" on an
   already-easy task; a 1.2B model gained +25 points on the same task shape)
   — directly relevant to choosing a task model for `pairs.py`'s 19-positive
   residual: it must be weak enough to fail sometimes, or GEPA has nothing to
   reflect on.
9. **`optimize_anything`'s own top-level function signature is missing from
   the skill entirely** (only its four nested `Config` classes are
   documented) — `text-artifacts.md` should gain the verified `surface` line
   in §5, above, including that only `seed_candidate` is positional.
10. **gskill is a real, published, held-out-tested instance of exactly what
    `text-artifacts.md` calls "job 4"** (optimizing this repository's own
    `SKILL.md` files) — 24%→93% and 55%→82% resolve-rate gains that
    transferred unmodified to a different agent and different models. Job 4's
    own section should cite it as the nearest existing evidence that the
    approach works, while being explicit that gskill trained on ~200
    generated tasks, not the 5–20 hand-captured failures job 4 itself plans
    to start from.
