# DSPy base — the LLM tooling substrate for Kohärenz Protokoll

Decided 2026-09-15: every new LLM step in this repo is written as a **DSPy 3.3.x
program** (`tools/kpwiki/`), not as a prompt string. Rationale and the wiki it
serves: [Plan/wiki/knowledge-system-concept_2026-09-15.md](../Plan/wiki/knowledge-system-concept_2026-09-15.md).

## What DSPy gives us (and why it fits a novel project)

- **Signatures instead of prompts.** A `dspy.Signature` is a typed I/O contract;
  its docstring is the instruction. Outputs are Pydantic models with *closed*
  enums (`tools/kpwiki/schema.py`), so a program that cannot fit a value fails
  loudly instead of inventing a category — Rule 0 at the type level.
- **Metrics with feedback are the safety rail.** `tools/kpwiki/metrics.py`
  returns `dspy.Prediction(score, feedback)`; the deterministic axes (citation
  validity, quote grounding, schema validity, language kept) cannot be talked
  around by a better prompt. GEPA optimizes instructions *against* them.
- **Optimization is a later, budgeted step.** Baseline first, `auto="light"`
  first, separate valset, saved artifacts + a regression test — the seven-step
  loop of the `dspy-advanced-workflow` skill.
- **RLM for long documents.** `dspy.RLM` is the tool for the long concept
  papers in the Drive corpus — the `kernkonzept` slice is 8 documents and
  471,211 characters, and the pilot's slowest call was a single 257 s
  extraction over one whole body. It runs its sandbox on Pyodide under Deno,
  so it raises at construction without `deno` on PATH.

  `scripts/setup_dspy.sh --deno` installs it into `$HOME/.deno` and the script
  reports the version on every run; without it the script warns and continues,
  because every other program here works fine. The install does not survive a
  fresh container, so re-run it there. Verified working on Deno 2.9.6 with
  DSPy 3.3.1: `PythonInterpreter()` starts and executes.

  Not used in a live ingest yet — `--merge-role` is the cost lever that is.

## Skills (agent-side)

The skill pack [netzkontrast/dspy-agent-skills](https://github.com/netzkontrast/dspy-agent-skills)
(fork of intertwine/dspy-agent-skills, v0.11.0, validated against DSPy 3.3.1)
provides 32 skills. The ones this repo builds on are `dspy-fundamentals`,
`dspy-evaluation-harness`, `dspy-gepa-optimizer`, `dspy-rlm-module`,
`dspy-rlm-workflow`, `dspy-deep-refine`, `dspy-reflect-loop`, `dspy-clarify`,
`dspy-tetraframe`, `dspy-autodialectics`, `dspy-wiki-compile`,
`dspy-adversarial-review`, `dspy-local-runtime` and `dspy-advanced-workflow`;
the pack's own README carries the full table.
The wiki programs in this repo instantiate `dspy-wiki-compile` (`SourceIngest`,
`BatchCompile`), `dspy-clarify` (`ClarifyGate`), `dspy-tetraframe` (`TetraFrame`)
and `dspy-adversarial-review` (`AdversarialReview`, Phase 4); the Claude-CLI
backend below is the `dspy-local-runtime` pattern.

Install for the project by adding the marketplace to `.claude/settings.json`
(same pattern as the `agency` marketplace already there):

```json
"enabledPlugins": { "dspy-agent-skills@dspy-agent-skills": true },
"extraKnownMarketplaces": {
  "dspy-agent-skills": { "source": { "source": "github", "repo": "netzkontrast/dspy-agent-skills" } }
}
```

Or per machine: `git clone https://github.com/netzkontrast/dspy-agent-skills && ./scripts/install.sh --claude-only`
(symlinks into `~/.claude/skills/`; `--verify` checks them).

## Runtime (code-side)

```bash
scripts/setup_dspy.sh              # .venv-dspy (git-ignored) with dspy==3.3.1, then smoke + tests
.venv-dspy/bin/python -m tools.kpwiki.smoke --dry-run   # no LM call
.venv-dspy/bin/python -m tools.kpwiki.smoke --live      # one SourceIngest run (ANTHROPIC_API_KEY)
.venv-dspy/bin/python -m pytest tests/test_kpwiki.py -q
```

`tests/test_kpwiki.py` skips itself when `dspy` is not importable, so the
existing `pytest tests/` run of the repo is unaffected.

### Model roles (env-overridable, never hard-coded in programs)

| role | env var | default | used for |
|---|---|---|---|
| task | `KP_LM_TASK` | `anthropic/claude-opus-5` | running programs |
| worker | `KP_LM_WORKER` | `anthropic/claude-haiku-4-5` | bulk sub-steps, LM-as-judge |
| reflection | `KP_LM_REFLECTION` | `anthropic/claude-opus-5` (temperature 1) | GEPA proposals |

`DSPY_CACHEDIR` defaults to `.cache/dspy/` (git-ignored) so repeated runs over
the same source are free. Model strings are DSPy/LiteLLM `provider/model`; the
Anthropic provider reads `ANTHROPIC_API_KEY` (the same key `scripts/lit_critic_gate.py` uses).

### Backends (`KP_LM_BACKEND`)

| value | LM class | needs | role models |
|---|---|---|---|
| `api` | `dspy.LM` (LiteLLM) | `ANTHROPIC_API_KEY` | `KP_LM_TASK` / `KP_LM_WORKER` / `KP_LM_REFLECTION` |
| `claude-cli` | `ClaudeLM` (`tools/kpwiki/local_lm.py`) | the `claude` CLI logged in to a Claude Code subscription | `KP_LM_CLI_TASK` / `KP_LM_CLI_WORKER` / `KP_LM_CLI_REFLECTION` (defaults `claude/opus`, `claude/haiku`, `claude/opus`) |
| `auto` (default) | the first of the two that is available | — | `api` if the key is set, else `claude-cli` if `claude` is on PATH, else `api` (fails loudly at first call) |

`python -c 'from tools.kpwiki import lm; print(lm.backend())'` shows which one a
shell resolves to.

### Local runtime — Claude CLI as the DSPy LM (dspy-local)

`tools/kpwiki/local_lm.py` is the `ClaudeLM` from
[Hmbown/dspy-local](https://github.com/Hmbown/dspy-local) (MIT,
`docs/dspy-local-LICENSE.txt`), vendored unchanged except for the imports, so
the repo stays on its own pinned DSPy (3.3.1) instead of the fork's 3.1.3. Every DSPy call
becomes one `claude -p --output-format json --permission-mode plan
--no-session-persistence [--model …] [--system-prompt …]` process in an
isolated `HOME` (only the credentials are copied in, the session does not
touch the working tree). Verified in the remote session of 2026-09-15: a
`dspy.Predict` with a Pydantic output round-trips through `claude/haiku` in
~9 s without an API key.

What the CLI backend cannot do, and what that means for the programs:

| limitation | consequence |
|---|---|
| no `temperature`, `max_tokens`, `rollout_id` (stripped in `copy()`, rejected in the constructor) | `TetraFrame` corner diversity comes from the four contract docstrings only — read `branch_independence` strictly; GEPA's `reflection_lm` runs at the CLI's default temperature |
| `cache=False` is mandatory | no `DSPY_CACHEDIR` hits; re-runs cost a call each; keep gold sets small and use `dspy.Evaluate(num_threads=1)` |
| one completion per call (`n=1`) | `dspy.BestOfN` / `dspy.Refine` still work (they loop), just slower |
| ~5–10 s latency per short call, minutes for a large typed output; one call is bounded by `KP_LM_CLI_TIMEOUT` (default 1800 s) | budget: a `SourceIngest` run ≈ 3 calls; a `TetraFrame` run ≈ 8 + BestOfN retries; GEPA `auto="light"` on 20 examples ≈ a few hundred calls → run it in the background and set `max_metric_calls` |
| the CLI's `plan` permission mode | the model cannot execute tools; pure text in, text out — exactly what DSPy needs |

Runtime knobs (all env, all optional): `KP_LM_CLI_TIMEOUT` (per-call bound,
default 1800 s), `KP_LM_CLI_LOG` (one line per call start / progress every 5 s /
end with elapsed time and tokens; default `.cache/kpwiki/cli.log`, the
`/tetraframe` CLI points it at `.cache/kpwiki/tetraframe/<slug>.log`),
`KP_LM_CLI_CWD` (the CLI's working directory, a scratch directory outside the
repo by default so no project hook runs per call). Calls stream over
`--output-format stream-json`, so a stalled call is visible in the log within
seconds. The CLI tolerates concurrent processes: three calls launched together
finish in the wall time of one, which `TetraFrame` uses for its four corners
and six pairwise relations (`--workers`, default 4; relations run on the
`worker` model).

GEPA through the CLI: `configure("task")` for the program,
`build_lm("reflection")` as `reflection_lm`, `worker` for LM judges via
`lm_context("worker")`. Start every optimization with `--dry-run`, then a
baseline on the val split, then `auto="light"`; save
`tools/kpwiki/artifacts/<program>.json` as with the API backend — artifacts
are backend-independent (they are instructions + demos).

### Package map

| file | role |
|---|---|
| `tools/kpwiki/lm.py` | `backend()`, `configure(role)`, `lm_context(role)`; building an LM never hits the network |
| `tools/kpwiki/local_lm.py` | `ClaudeLM` — DSPy `BaseLM` over the `claude` CLI (vendored from Hmbown/dspy-local) |
| `tools/kpwiki/schema.py` | Pydantic contract: the ingest models (`Citation`, `Claim`, `Triage`, `CanonConflict`, `OpenQuestion`) and the batch-compile models (`Extraction`, `ConceptPlan`, `ConceptDraft`, `PageState`, `IngestDecision`, `Diff`, `Compiled`); every page enum built from `Wiki/schema/entities.yaml` |
| `tools/kpwiki/signatures.py` | `TriageSource`, `ExtractClaims`, `CheckCanonConflict`, `RaiseQuestions`, `PlanConcepts`, `MergeConcept`, `DecideIngest`, `KnowledgeDiff` |
| `tools/kpwiki/programs.py` | `SourceIngest` (triage → cited claims → canon conflicts) and `BatchCompile` (the two-phase compiler); retrieval injected as a callable |
| `tools/kpwiki/metrics.py` | `ingest_metric` — weighted axes + teachable feedback |
| `tools/kpwiki/compile_metric.py` | `compile_metric` plus the helpers the lint reuses (`citation_resolves`, `decision_legal`, `diff_consistent`, `concept_problems`) |
| `tools/kpwiki/compile_fixture.py` | the hand-built batch the dry run and the offline tests score (a clean and a deliberately broken copy) |
| `tools/kpwiki/clarify.py` | `ClarifyGate` — the precision gate before promotion (skill `dspy-clarify`, command `/clarify`) |
| `tools/kpwiki/clarify_metric.py` | `clarify_metric` — lexical "never change meaning" rule |
| `tools/kpwiki/clarify_cli.py` | `python -m tools.kpwiki.clarify_cli --claim … --source path:L-L [--dry-run]` |
| `tools/kpwiki/tetraframe.py` | `TetraFrame` — four isolated corners → cartography → `BestOfN` P* (skill `dspy-tetraframe`, command `/tetraframe`) |
| `tools/kpwiki/tetraframe_metric.py` | `verify_run`, `transform_reward`, `tetraframe_metric` — the seven upstream checks with their thresholds |
| `tools/kpwiki/tetraframe_cli.py` | `python -m tools.kpwiki.tetraframe_cli --seed … [--context-file …] --out Plan/decisions/tetraframe/<slug>.json [--dry-run]` |
| `tools/kpwiki/smoke.py` | `--dry-run` / `--live` |

## BatchCompile (an instance of `dspy-wiki-compile`)

`BatchCompile` is Phase C of the wiki loop: a batch of exported sources in,
concept drafts plus a knowledge diff out. It writes nothing — `/research-ingest`
renders the drafts into `Wiki/candidates/` and the author promotes them.

| stage | predictor | what is decided in code |
|---|---|---|
| triage | `TriageSource` | a `truncated` or empty source is skipped, never extracted |
| extract | `ExtractClaims` | line-numbered body in, citation with a verbatim quote out |
| plan | `PlanConcepts` | global 1-based claim ids; an id the plan invents is dropped and scored |
| merge | `MergeConcept` | one call per concept, seeing only that concept's claims; an existing page's slug wins over the planned one |
| decide | `DecideIngest` | `create` when no page exists — that is a lookup, not a judgement |
| diff | `KnowledgeDiff` | runs only for a concept that has a page |

Two design points, both about bounded prompts and honest merging:

- **Plan before merge.** The clustering step sees one digest line per claim
  (`N. [source-slug] text — entities: …`), not the claims themselves, so the
  same idea under different names becomes one concept across the whole batch
  instead of one page per source. A digest longer than `MAX_DIGEST_CLAIMS`
  (1200) is planned in consecutive slices and the slice plans are merged by
  slug (union of claim ids).
- **Extract everything before merging anything.** Phase 1 finishes for every
  source before the first concept is written; a concept that appears in three
  sources is one draft with three sources.

`compile_metric` weights citations 0.30, decisions 0.25, merge 0.20, diffs
0.15, links and language 0.10. Every axis is decidable without an LM — a
citation resolves to its lines and its quote or it does not, an `update` on a
`reviewed` page with conflicts is illegal, a disagreement needs two distinct
sources, a `new` diff item must be absent from the page, a definition sentence
is English and never emits `[K]` — so GEPA cannot optimize the compiler into
confident prose. Each failure names its blame in the feedback.

```bash
.venv-dspy/bin/python -m tools.kpwiki.smoke --dry-run     # both programs, both metrics, no LM call
.venv-dspy/bin/python -m pytest tests/test_kpwiki_compile.py -q
```

## Conventions for new programs

1. One Signature per decision; name predictors (GEPA needs the names).
2. Closed enums in `schema.py`; extend the enum, never accept free text.
3. Every claim-like output carries a `Citation`; the metric verifies it against
   the numbered source, the wiki lint verifies it again on disk.
4. German stays German inside outputs (`language_kept` axis); engineering
   English for summaries and explanations.
5. Gold sets live under `tools/kpwiki/data/<program>/{train,val}.jsonl`
   (hand-checked, 20–50 examples). Never evaluate on the trainset.
6. Optimized artifacts: `tools/kpwiki/artifacts/<program>.json`
   (`save_program=False`, version-controlled); logs under `gepa_logs/` (ignored).
7. No direct `anthropic` SDK calls in the wiki tooling — DSPy is the only LM
   surface. `lit_critic_gate.py` keeps its own vendored runtime; it is an
   editorial gate on prose, not part of the wiki loop.

## Existing LLM call sites and how they relate

| site | status |
|---|---|
| `scripts/lit_critic_gate.py` (lit-critic lenses) | unchanged; prose gate, own venv |
| agency `novel.*` verbs (`generate_scene_body`, `storyform_critical_pass`) | unchanged; graph/provenance engine |
| `/query`, `/lint-wiki`, `/ingest` commands (Claude in the session) | keep for interactive work; batch equivalents become kpwiki programs |
| `scripts/research-tool.py` | deterministic, no LLM |

## Research wiki layer — what runs, and the settings the author applies

The deterministic Phase-1 tooling of the knowledge system (`Wiki/SCHEMA.md`)
needs no key and no virtualenv: `python3` plus PyYAML.

| command | does |
|---|---|
| `python3 scripts/wiki_lint.py --health` | every lint rule over `Wiki/`, coverage summary, exit 1 on errors |
| `python3 scripts/wiki_lint.py --hook FILE` | one file, warn-only (the PostToolUse hook in `.claude/hooks/post-tool-use.sh` runs this on `Wiki/**/*.md`) |
| `python3 scripts/wiki_lint.py --fix [--dry-run]` | completes reverse cross-references and default fields |
| `python3 scripts/render_wiki_views.py [--check]` | renders `Wiki/index.md`, `Wiki/concept-table.md`, `Wiki/graph/coverage.json` |
| `python3 scripts/wiki_fts.py build \| search \| stats \| doctor` | FTS5/BM25 candidate finder over `Wiki/`, `Canon/`, `Sources/drive/` (index in `.cache/wiki-fts/`) |
| `python3 scripts/source_inventory.py [--check]` | Drive index → `Sources/manifest.jsonl` (T4 rows excluded, D-W9) |
| `python3 scripts/source_dedup.py [--check]` | byte-equal and near-duplicate clusters → `T0-duplicate`, `T1-superseded` |
| `python3 scripts/audit_graph_claims.py` | read-only D-W2 audit of `NovelClaim.source_uri` in `Graph/` |
| `python3 scripts/source_export_mark.py --slug … --from-json …` | steps 3+4 of the fetch procedure: write one export, hash it, mark its manifest record |

One command in this layer does call an LM, so it needs the virtualenv:

| command | does |
|---|---|
| `.venv-dspy/bin/python -m tools.kpwiki.research_ingest_cli [--slug/--category/--tier/--batch]` | `/research-ingest`: selects a batch from the manifest and prints it; the default is a dry run with no LM call |
| the same with `--write` | runs `BatchCompile`, prints the knowledge diff and the metric score, writes `Wiki/candidates/**`, `Wiki/graph/edges.jsonl`, `Wiki/log.md`, then lints what it wrote. `--write` is user-owned: a session never sets it |

`.claude/settings.json` is the author's file. The lines below complete the
ownership zones of `Wiki/schema/conventions.yaml`; apply them by hand:

```json
"permissions": {
  "allow": [
    "Bash(python3 scripts/wiki_lint.py*)",
    "Bash(python3 scripts/render_wiki_views.py*)",
    "Bash(python3 scripts/wiki_fts.py*)",
    "Bash(python3 scripts/source_inventory.py*)",
    "Bash(python3 scripts/source_dedup.py*)",
    "Bash(python3 scripts/audit_graph_claims.py*)",
    "Bash(python3 scripts/source_export_mark.py*)"
  ],
  "deny": [
    "Write(Sources/drive/**)", "Edit(Sources/drive/**)",
    "Write(Wiki/index.md)", "Edit(Wiki/index.md)",
    "Write(Wiki/concept-table.md)", "Edit(Wiki/concept-table.md)",
    "Write(Wiki/graph/**)", "Edit(Wiki/graph/**)"
  ]
}
```

SessionStart: add `python3 scripts/wiki_lint.py --health` next to the stale-Codex
check so every session opens with the free health report. `Sources/manifest.jsonl`
stays writable for the two inventory scripts; `Sources/README.md` is documentation.
Canon keeps its warn-only PreToolUse treatment (the repo decided against a
write-deny on Canon); the wiki never writes there by construction
(`Wiki/schema/writers.yaml`).
