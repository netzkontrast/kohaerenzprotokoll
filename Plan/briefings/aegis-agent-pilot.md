# AEGIS pilot — implementation handoff

Status: proposed next implementation, 2026-10-13. The author requested an AEGIS
plan and a PR with Claude instructions; this briefing specifies the bounded first
coding task. It neither certifies a runtime nor approves new novel content.
Read `CLAUDE.md` for startup, permissions, authority and completion rules; read
`Plan/concept/aegis-agent_2026-10-13.md` for rationale and source disagreements.

## Scope and inputs

Build a local, standard-library offline pilot with AEGIS and one counterfigure.
Use `Manuscript/kanon.md`, `Plan/storyform/b.json` and `weave.json` as decided
inputs. Read `clock-b.json` and AEGIS' card as proposals where they say so. Do not
load the entire research corpus into a character context. Relevant source ideas
are indexed in the concept plan; research access belongs to the coordinator.

AEGIS is MC/Protagonist/Reason in B, Do-er and Steadfast. Its monolithic endpoint
and plural continuation follow Q8. The five Guardians and the Guardian archetype
are different categories. Do not infer undecided character knowledge or voice
from an older source. Identify every scenario assumption explicitly.

## Start with two manual cases

Before writing a schema, record each case's initial state, perceptions for each
figure, allowed action, expected outcome and authority/assumption references.

1. AEGIS observes a scenario-local anomaly and proposes a permitted sweep. The
   event masks one simulated memory and consumes a specified reserve. Define the
   cost as a test assumption, not Landauer-derived physics or decided canon.
2. AEGIS requests an action without its required observation or sufficient
   reserve. Validation rejects it with a reason and leaves state unchanged.

The counterfigure can perceive the external consequence without knowing the
private operation or the author's future plot. Include one fact visible only to
the author as a leakage probe. The fixtures use invented test state, not new
manuscript prose. Do not make an actual model call for these cases.

## Implement the smallest loop these cases require

Suggested location: `scripts/aegis.py` and scenario fixtures under
`Plan/fixtures/aegis/`. These paths and command names are proposals until built.
Prefer adapting them to the existing script conventions over adding a package.

- Assemble author context separately from each character's perception. Apply
  access filtering in code before any model adapter receives data. Private
  beliefs, observed facts and received claims remain distinguishable.
- Activate only a figure addressed by a scene/event. Persist its identity and
  memory across pause/resume. Do not spawn persistent CLI processes or grant
  characters repository tools. Development-session claims stay in sessions.py;
  fictional activation is a different runtime concern.
- Accept a mock response containing an action type, target, observation references
  and a short explanation. Dialogue/literary logs are separate optional outputs,
  never executable commands or hidden model reasoning.
- Validate allowed action, actor identity, prerequisites, current state version
  and resource bounds. Do not use a model judge to enforce these decidable rules.
- Apply accepted events through one writer. Use atomic persistence and stable
  action IDs; a retry must not execute the same cost or masking twice. On restart,
  derive state from committed events so a failed snapshot cannot invent history.
  Store rejected attempts separately from state-changing events.
- Pin scenario, source revision and response version in the run. Replay consumes
  frozen accepted events/responses without inference. A fork creates an independent
  scenario branch, not a Git branch that automatically merges plot into canon.

Reuse `pack.py`'s byte-budget/incomplete conventions where appropriate; it does
not itself enforce character permissions. Inspect the existing model adapters
before choosing one: `lmrun.py` records DSPy calls, not arbitrary subprocesses.
The offline mock needs no provider. A later live adapter must retain the session
contract's recording and transfer rules without weakening an existing guard.

## Acceptance evidence

Provide an offline command demonstrating both manual cases and pause/resume.
Document its actual invocation only after it exists. Assertions must establish:

- the author-only probe is absent from both character packs and tool responses;
- rejected or stale-version actions leave state and reserve unchanged;
- reserve cannot become negative and a repeated action ID costs nothing twice;
- accepted events replay to the same state without model or network access;
- state survives pause/restart and a fork cannot alter its parent's inputs;
- the monolithic profile cannot continue past its scenario-defined endpoint;
- missing evidence, incomplete context and unavailable model access are named,
  never scored as successful simulation or poor literary output.

Run the relevant existing checks and add the new offline fixture to the existing
selftest runner using its actual interface. Keep mechanical results distinct from
the author's judgement of voice, tension and meaningful choices. Report changed
paths, example transcripts, failures, and what is still unbuilt in the PR.

## Later extensions, in order

1. A single serial recorded model call, only after the offline path works and the
   chosen provider/input scope has existing permission. Repeat evaluation uncached.
2. A static author replay view showing scene, perceptions, proposals and outcomes;
   follow app-refresh for routes, agent exports and verifiable UI data.
3. A short authored Ink/inkjs adaptation with a later consequence and save/load.
   Assign world state to one owner; Ink and Python must not independently mutate
   the same reserve. NCP supplies structure, not a ready-made game runtime.

Do not add a database, MCP server, orchestration framework, unbounded agent swarm,
automatic canon editor or public live-model backend. Do not write manuscript
chapters, rewrite source bytes, resume the stopped backfill, or choose alternative
endings. Propose the next extension from demonstrated missing capability.
