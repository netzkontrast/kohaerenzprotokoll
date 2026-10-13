# Kohärenz Protokoll — session contract

A German hard-SF novel and its research corpus. German manuscript prose stays German; engineering and planning use English. This file contains standing operating rules. `NOW.md` contains current work; `PRINCIPLES.md` contains the reasons and design principles. Do not duplicate their histories or measured counts here.

## Start a session

1. Read `AGENTS.md`, `NOW.md`, this file and `PRINCIPLES.md`. The author's current instruction wins; follow NOW.md's named mandate and linked briefing before choosing unrelated work. Read `SPEC.md` before architecture changes.
2. Run `python3 scripts/knowledge.py init --profile reader` as coordinator (`research` for DSPy work). Claude's SessionStart hook already runs the research initializer; inspect its result before repeating it. Workers use the matching `--check` profile and never rebuild shared stores. Report unavailable capabilities; a source-only task can continue with `read.py` when those capabilities are irrelevant. Install dependencies in virtualenvs, never system Python.
3. Run `python3 scripts/sessions.py board`. Read active branches and open PRs before selecting work. Unknown live state is not free. Claim work with an open PR whose body has `Session: <id>`; a branch name is not a claim. For source ingest also name the source slugs under `Claim`.
4. Load only the skill for the operation below and its needed references. Enumerate current files instead of assuming an old chapter variant, source count or branch remains current.

## Authority and writes

| Input | Authority | Write path |
|---|---|---|
| `Sources/manifest.jsonl`, `Sources/drive/` | Immutable landed research, including narrative-looking sources | `sources.py` only; never model-rewrite bytes |
| `Sources/terms/`, `Sources/notes/`, `Wiki/` | Independent source readings, disagreements and human reviews; not novel canon | Ingest/reconciliation procedures; preserve attribution |
| `Manuscript/kanon.md`, dated author decisions and approved material | Decided content; later explicit corrections win | Author-authorized change only; no automatic promotion |
| `Plan/storyform/a.json`, `b.json`, `weave.json` | Approved structure with provenance | `storyform` workflow; do not change an answer to pass a check |
| `development.json`, cards, drafts, scene lists and simulation runs | Proposals or working bases unless explicitly approved | Preserve their status and assumptions |
| `Plan/derived/`, `Graph/`, generated NCP and overview | Disposable derived views | Regenerate from authoritative inputs; never hand-edit or import the Graph atlas |

`Sources/` and `Wiki/` are the two research layers; `Manuscript/` is what they serve. A source calling itself canon cannot promote itself. `Legacy/` is parked, never runtime input, canon or a prose reference; historical measurements may cite it without reading it at runtime. `GOAL.md` describes the target; it does not certify implemented features.

## Evidence and model calls

- Freeze a document's independent census/note before loading wiki or cross-document context. Reconcile by the existing lookup procedure. Readings remain attributed and unmerged; semantic conflicts remain judgement, not a program's verdict.
- Obtain source lines with `read.py` and `--find`; never invent identifiers or reconstruct quotations. Wiki references name the source slug. `quotes.py` verifies them; uncheckable is not passed. Search ranking is discovery, never a corpus count.
- Model output proposes; it does not decide canon, conflicts, judgements or links. Keep proposal relations out of the core graph. Record actual inputs, outputs, status, usage and cost through the existing compatible model path; evaluation caches stay off.
- No corpus text goes to a third party without the author's decision for that run (007/008/011). Claude CLI's isolated first-party path remains as specified by decision 011. Do not infer a new provider permission from this AEGIS plan.
- Model calls are serial, except up to two Sonnet ingest readers allowed by NOW.md; their reconciliation and commits remain sequential. Do not interpret multiple fictional figures as permission for parallel paid runs.
- Every workflow needs an offline fixture. Name separate mechanical checks and human judgements; `not run`, unavailable and incomplete are not success.

For claim correction, provisional constructs and source-named wiki commits, read [session-method](Plan/concept/session-method.md). Never collapse different sources into one reading or delete a construct merely because its first use is disputed.

## Select the workflow

| Task | Read next |
|---|---|
| Ingest/reconcile a source | `.agents/skills/ingest/SKILL.md`, `tools`; workers: `reader-tools` |
| Bounded research or evidence lookup | `reader-tools` (research scope), `graph-context` or `qmd`; discovery alone is not ingest |
| Plot, casting or NCP | `storyform`; chapter execution: `scene-architecture` planning/review mode |
| Manuscript critique, voice or continuity | `writing-skills`, then the relevant specialist; findings in `Plan/runs/writing/` |
| AEGIS agent implementation | The next section and `Plan/briefings/aegis-agent-pilot.md` |
| Model/template experiment | `dspy` or `hyperextract-learning`; approvals and STOP files still apply |
| NOW/app changes | `app-refresh`; build from sources, keep routes and agent exports consistent |

Project skills live in `.agents/skills/`; `.claude/skills/` links to them. Do not edit two copies or rewrite pinned vendored skills. The coding coordinator implements software; editorial skills critique prose; fictional agents act only inside their scenario. A review skill's no-rewrite rule does not ban an explicitly authorized separate drafting task.

## AEGIS implementation mandate

The author requested the plan on 2026-10-13 and this PR/instruction update. The implementation below is the next proposed coding task, not a claim that a runtime exists or a new canon decision.

Read the [pilot briefing](Plan/briefings/aegis-agent-pilot.md) before coding; the full rationale and source review are in [the plan](Plan/concept/aegis-agent_2026-10-13.md). Start with two manual cases, AEGIS and one counterfigure, then an offline standard-library implementation. Reuse the existing canon, storyforms, pack contracts and model adapters where they fit. A fictional AEGIS is not the research pipeline's canon checker.

Keep perception filtering outside the model. Characters receive only scenario-visible facts and allowed actions, with no repository tools. AEGIS proposes typed actions; deterministic code validates prerequisites, state version and resource costs before committing one event. Preserve mistaken beliefs separately from facts. Pause/reactivate figures from persisted events; replay uses frozen responses and never calls a model. Simulation events and literary logs are separate artifacts.

Keep manuscript/canon untouched. Model integration, Ink/inkjs play, public backend and alternative endings are later steps, each earning its scope through pilot evidence. Do not add a graph database, MCP server, controller framework or swarm before the offline cases need it. The briefing owns deliverables and acceptance criteria; update it when implementation proves a design assumption wrong.

## Finish a change

Run the checks appropriate to the changed inputs and every required CI step from `.github/workflows/checks.yml`. Standard checks include `state.py --prose`, `account.py order --summary`, `quotes.py`, `wiki_index.py --check`, `promote.py check`, `terms.py check`, `judgements.py --open`, `chapters.py`, `overview.py --check`, `storyform.py --check` and `selftests.py --only std`; run `derive.py` first. Skill edits also run `check_skills.py`. Report venv suites separately.

NOW.md changes affect the session UI: derive sessions and run `ui.py --check` / `web.py --no-build --check` using `app-refresh`. The pre-PR app hook was removed on 2026-10-06; do not reintroduce a mandatory hook or claim deployment from a local build. Visual/deployment checks require their actual environment; report any unavailable verification.

Commit complete work with provenance, keep PR descriptions current, and preserve unrelated work. After the author merges an active branch, merge `origin/main` into it rather than rebasing or resetting it; open a new PR when continuing. Decisions belong in `Plan/decisions/`, evidence in `Plan/runs/`, questions in `Plan/questions-for-the-author.md`, next steps in NOW.md, and history in git. The session board derives from NOW.md and live GitHub; do not create a second persistent backlog.
