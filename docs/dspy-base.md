# DSPy base — the LLM tooling substrate for Kohärenz Protokoll

Decided 2026-09-15: every new LLM step in this repo is written as a **DSPy 3.2.x
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
- **RLM for long documents.** `dspy.RLM` (needs Deno) is the tool for the
  100k+-token concept papers in the Drive corpus; not used yet.

## Skills (agent-side)

The skill pack [netzkontrast/dspy-agent-skills](https://github.com/netzkontrast/dspy-agent-skills)
(fork of intertwine/dspy-agent-skills v0.2.3, validated against DSPy 3.2.1;
114 pack tests and all six `--dry-run` examples pass in this environment) provides
`dspy-fundamentals`, `dspy-evaluation-harness`, `dspy-gepa-optimizer`,
`dspy-rlm-module`, `dspy-advanced-workflow`.

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
scripts/setup_dspy.sh              # .venv-dspy (git-ignored) with dspy==3.2.1, then smoke + tests
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

### Package map

| file | role |
|---|---|
| `tools/kpwiki/lm.py` | `configure(role)`; building an LM never hits the network |
| `tools/kpwiki/schema.py` | Pydantic contract: `Citation`, `Claim`, `Triage`, `CanonConflict`, `OpenQuestion`; closed enums for tier, category, kind, canon relation |
| `tools/kpwiki/signatures.py` | `TriageSource`, `ExtractClaims`, `CheckCanonConflict`, `RaiseQuestions` |
| `tools/kpwiki/programs.py` | `SourceIngest` (triage → cited claims → canon conflicts); retrieval injected as a callable |
| `tools/kpwiki/metrics.py` | `ingest_metric` — weighted axes + teachable feedback |
| `tools/kpwiki/smoke.py` | `--dry-run` / `--live` |

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
