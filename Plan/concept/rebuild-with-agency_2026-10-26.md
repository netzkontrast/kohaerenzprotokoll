# Rebuilding Kohärenz Protokoll around the agency substrate — what transfers, what must not

Status: **proposal**, 2026-10-26. Written by a session that surveyed the 31 repositories mounted beside this one
(`netzkontrast/agency` and 29 siblings) with one reading agent per repository, and read `agency`'s engine itself.
Nothing here is decided; the author's questions are in §10. The per-repository survey reports live in the
session's scratchpad and are summarised in §6; every claim about a sibling repository is that survey's reading on
this date, not a measurement in this repository. What this concept already built is in §8, step 0.

The author's instruction behind it: understand the surrounding environment recursively, understand what this
repository tries to achieve, and refactor it so that it includes the core aspect of what the other repositories
offer — with the most weight on `agency`.

## In one paragraph

Agency is a provenance engine: one FastMCP server over one bi-temporal GraphQLite graph, four concepts (Intent ·
Capability · Lifecycle · Memory), three wire verbs, capabilities as self-registering folders, skills as phase-graphs
walked one phase at a time, lifecycle machines as data, specs that flow through state folders behind an ADR hinge.
Kohärenz is a file-authoritative research-and-writing repository whose rules forbid most of what agency does by
default: the graph is disposable here, model output proposes and never decides, conflict detection is never
mechanised, no corpus text leaves the container without a decision, and the mandated next task — the AEGIS pilot —
says in so many words "do not add a database, MCP server, orchestration framework". The refactor that respects both
is therefore **three tiers**: (1) absorb agency's *doctrine* as standard-library patterns in this repository's own
scripts — one writer, state derived from events, machines as data, decidable gates with typed reasons, keep-both
records — which is exactly what the AEGIS pilot needs and what `scripts/aegis.py` now does; (2) run agency as an
**optional host plugin for development sessions only**, with `Manuscript/kanon.md`, `Plan/decisions/`, `Sources/`
and `Wiki/` declared file-authoritative and the graph a derived index, once agency can load an out-of-tree
capability; (3) **later, and only on the author's word**, a thin `kohaerenz` capability that exposes the existing
scripts as relay verbs with provenance, never as a second implementation. Of the 29 other repositories, nine
converge on the same place — the pilot's validator, event log and belief record — and the rest land as small,
offline, self-tested checks or as writing-side coaches that never write prose. Everything is listed in §6 with the
rule that would be broken by taking more.

## 1. What agency is (read in the engine, not only in its docs)

| layer | what it is | where |
|---|---|---|
| Engine | one FastMCP server; wire contract exactly `search · get_schema · execute` (code-mode: the agent chains `await call_tool(...)` in a sandbox, only the return crosses back); eight bootstrap "substrate tools"; the same engine over a bash CLI (`agency <cap> <verb>`), so MCP and bash are isomorphic | `agency/engine.py`, `agency/cli.py`, `agency/_substrate_tools.py` |
| Capability | a folder under `agency/capabilities/<name>/` with a `CapabilityBase` subclass, `@verb(role=act|transform|effect)` methods, an `OntologyExtension` (nodes, edges, enums, skills, schemas, templates), a docstring that *derives* its SKILL.md; discovered by reflection; an out-of-tree capability loads via `Engine(extra_capabilities=[…])` — **but the MCP entry point has no way to pass one** (`agency/__main__.py` builds `Engine(db_path)` bare) | `agency/capability.py`, `agency/capabilities/__init__.py` |
| Memory | append-only, bi-temporal (`vfrom`/`vto` ticks), `record · link · supersede · retract · recall(as_of) · project(budget)`; the ontology is enforced on every write; a typed SQLModel projection mirrors the graph | `agency/memory.py`, `agency/ontology.py`, `agency/_entity_store.py` |
| Intent | purpose + deliverable + acceptance, with an owner; every Invocation `SERVES` one; sub-intents chain by `PARENT_INTENT` | `agency/intent.py` |
| Lifecycle | `open · move · close`; `move` is the sole writer of state and validates against a machine; machines are **data** (`a2a`, `remote-async`, `reviewed`, `frugal`, `loop`, `spec`, `decision`) with derived observers | `agency/lifecycle.py`, `agency/_lifecycle_data/machines.json` |
| Skill | a phase-graph: each phase has `produces`, optional `gate: hard`, inline `goal/instructions/done_when`; the walker discloses one phase at a time and records each as provenance; a hard gate pauses at `input-required` and records a `Gate` node both ways | `agency/skill.py` |
| Document | a markdown file bound to a graph node by `<!-- agency-node: id -->` on line 1; `document.ingest` (file → graph, keep-both `DocRevision`), `document.render`/`mirror` (graph → file), `sync` over a tree; "every file is also a prompt" (scored by `prompt.audit`) | `agency/capabilities/document/_main.py` |
| Workflow + ADR | specs live in `Plan/<draft|open|inprogress|superseded|done>/NNN-slug/spec.md`; `open → inprogress` is blocked until the spec's decisions are approved (`adr.spec_decisions_ready`); `architecture.md` is a derived digest the SessionStart hook emits | `agency/capabilities/workflow/`, `adr/`, `architecture.md` |
| Dogfood | observations recorded as nodes; `parse_amendment` → `apply_amendment` folds a lesson into a spec behind a human `confirm_token`; `replay_events` | `agency/capabilities/dogfood/` |
| Boundaries | every external side effect behind a named Driver (git, Jules, web, LLM, Anthropic, tokens) registered as a lazy factory; tests inject fakes | `agency/capability.py` `DriverRegistry` |
| Hooks | one dispatcher for every Claude Code event; raw mutating tool calls are shadowed as `BoundaryUse` provenance; `PreToolUse` suggests the companion verb, never blocks | `agency/engine.py` `_RAW_ROUTES`, `hooks/` |
| Novel capability | 166 verbs in 18 cluster mixins (an AST count by the survey; the module header still says about 45), 16 walkable skills, a vendored Dramatica ontology, NCP schema **1.3.0**, 55 Kohärenz fragments; graph-canonical, disk layout `works/{author}/works/{genre}/{slug}/`; decidable checks for reveal timing, per-scene budgets, motif caps, mode-block vs storyform boundary, no-fusion | `agency/capabilities/novel/`, `examples/kohaerenz-protokoll/` |

Agency's own working rules worth naming because they map onto this repository's: *code is the final decision*
(ADRs are derived from what shipped, never authored ahead); *test behaviour, not implementation*; *no hardcoded
values — compute expectations from the live source*; *never silently truncate captured data*; *the drop-in
capability bar* (adding a capability may touch nothing outside its folder); *keep `TODO.md` current in every
spec-touching commit*.

## 2. What this repository is, in the terms the bridge needs

Authority is a ladder, not a graph: `Sources/` (immutable landed documents, census and note per document, frozen
before the wiki is read) → `Wiki/` (attributed, unmerged readings; conflicts and questions as records that decide
nothing) → `Manuscript/kanon.md` (the one place canon stands, by the author's word with a date) → `Plan/decisions/`
(one file per decision, permanently) → `Plan/storyform/{a,b,weave}.json` (approved structure with provenance). Below
the ladder: `Plan/derived/`, `Graph/`, the NCP, the app — disposable, rebuilt, never imported. Everything that
checks is a standard-library script with a self-test that can fail, registered in `scripts/selftests.py`, and a
README row the prose check enforces; `.github/workflows/checks.yml` runs each check as its own step. P0 "never
assume; ask", P1 "decidable means programmatic; the rest is *named* judgement", P2 "describe no more than exists",
P3 "by hand first". Model calls are serial, recorded, cache off, and leave the container only on a per-run decision
(007/008/011). A construct is demoted (`provisional / may not / retire when`), never deleted on first objection.

The mandated next task (author, 2026-10-13; `Plan/briefings/aegis-agent-pilot.md`): an offline, standard-library
simulation of AEGIS and one counterfigure — perception filtered in code, typed proposals, deterministic validation,
one atomic writer with idempotent action ids, replay from frozen responses, pause/resume, fork — *without* a database,
an MCP server, a controller framework or a swarm.

## 3. Where agency and this repository contradict each other

| agency default | this repository's rule | consequence for the bridge |
|---|---|---|
| the graph is canonical; markdown is a (round-tripping) peer | files in git are authoritative; the graph is a disposable derived view (decisions 001, 021) | agency's own CLAUDE.md lets doctrine docs be *file-authoritative* under keep-both — the bridge declares `kanon.md`, `Plan/decisions/`, `Sources/`, `Wiki/` file-authoritative and lets the graph index them; `document.ingest` must run with `write_anchor=False` on them (it stamps `<!-- agency-node -->` on line 1 by default, which would rewrite a source's bytes) |
| `novel.set_canon_status("canonical")`, `record_lock`, `approve_canon(approver_kind=…)` write canon on a self-declared approver | canon is the author's word in `kanon.md`; model output proposes | these verbs are never wired against this repository; a `kohaerenz` capability (tier 3) has no canon-writing verb at all |
| `find_axiom_contradictions` (negation heuristic, writes `CONTRADICTS` edges), `resolve_canon_conflict` (newer wins), `check_continuity` | conflict detection is never mechanised; "newer wins" is suspended (decision 006) | not transferred; a conflict stays a record a person writes |
| `generate_scene_body` / `integrate_scene_body` send a brief to Anthropic when `ANTHROPIC_API_KEY` is set and write prose to `Scene.body` | no corpus text leaves without a per-run decision; no skill writes the author's prose | not transferred; a later live adapter for the pilot goes through `lmrun.py`/`claude_cli.py` with an approval |
| `check_klein_c_inversion` requires all eight dynamics of A and B to be inverse | the author's decided data has growth `stop` on both storyforms; "do not change an answer to pass a check" | the invariant is not adopted; a check that would pressure a decided value is wrong, not the value |
| marker `[S]` = quarry (deprecated stock) | `[S]` = a source says it | agency's `examples/kohaerenz-protokoll/` and Spec 137 use the other meaning; the six example files are dated 2026-06-10 and are stale against `kanon.md` (two Guardians vs five, KW names, AEGIS third person vs five Ich chapters, NCP 1.3.0 vs 3.0.0-rc.1) |
| English lexicons, `[A-Za-z]+` tokenizer, chapter numbers ≥ 1 | German prose, umlauts and ß, Kap 0 | agency's prose checks are not run on this manuscript |
| `.agency/session.db` per project, hooks on every tool call | "there is no board, no status field and no backlog"; no mandatory hook | the plugin is optional, per session, gitignored; nothing in CI depends on it |

## 4. The three tiers

### Tier 1 — agency's doctrine as standard-library patterns (adopted in this PR)

What transfers is not the engine but its shape. The AEGIS pilot is where these shapes were needed first, so
`scripts/aegis.py` is the first materialisation:

| agency pattern | the Kohärenz form | where it is now |
|---|---|---|
| `lifecycle.move` is the sole state writer; machines are data | one writer (`Run.commit`); the allowed actions, their costs and effects are **data in the scenario file**, the validator is the only code that reads them | `scripts/aegis.py` `validate`, `Run.commit`, `Plan/fixtures/aegis/*.json` `actions` |
| append-only memory, state read by projection | state is never stored as truth; it is derived from `events.jsonl`; `final.json` is a recorded snapshot the replay compares against | `derive_state`, `replay` |
| every Invocation records before it runs, so a failure is auditable | every proposal leaves a row — in `events.jsonl` or in `rejections.jsonl` with its typed reason — before anything else happens | `Run.commit` |
| a `Gate` node records both the pause and the resume | a rejection names the first failing rule in a fixed order; nothing is "flaky" or unexplained | `REJECTIONS`, the fixed order in `validate` |
| provenance pins (`scenario_sha256`, `responses_sha256`, source revision) | a replay refuses a run whose pinned scenario changed | `Run.create`, `replay` |
| fork = a new Lifecycle `DISPATCHED_TO`, parent untouched | `Run.fork` copies events; the self-test proves the parent's bytes are unchanged | `Run.fork` |
| no silent truncation of captured data | packs *count* what they omit and never shorten what they include | `pack` → `omitted` |

Beyond the pilot, the same tier names four more patterns this repository should take, each as a check with a
self-test (prompts in `Plan/briefings/rebuild-prompts_2026-10-26.md`): a **settled-directions registry** so a
question the author already answered is relayed, not re-asked (from `epistemic-protocols`); a **layer scope file**
per research layer declaring what it may contain and which derived views it feeds (from `self-driving-agents`); a
**per-claim verification ledger** for run reports (from `meta-metacognition`); and the **specs-in-state-folders**
discipline for `Plan/concept/` → `Plan/decisions/` *only if* the author wants concept documents to carry a state at
all (today a dated file says what was true on its date, which is a different and defensible convention).

### Tier 2 — agency as an optional host plugin for development sessions

Agency installs into a host repository as a Claude Code plugin: `.mcp.json` points `AGENCY_DB` at
`${CLAUDE_PROJECT_DIR}/.agency/session.db`, and the SessionStart hook scaffolds `.agency/`. In this repository that
would mean: a coding session captures an Intent, its verb calls `SERVES` it, `document.session` writes the session's
Intent · Capability · Lifecycle · Memory into `.agency/sessions/`, and `dogfood.note` records lessons that could fold
back into `Plan/learnings/`. None of that touches the research layers if three conditions hold:

1. **File authority is declared.** `kanon.md`, `Plan/decisions/`, `Plan/storyform/`, `Sources/`, `Wiki/` are
   file-authoritative; the graph only indexes them (ingest with `write_anchor=False`); `.agency/` is gitignored.
2. **The pilot is a capability, not a verb set agency owns.** `scripts/aegis.py` stays the implementation; a
   capability (tier 3) would only *call* it. The briefing's "no MCP server" holds for the pilot's runtime; the plugin
   is a development harness, not the pilot.
3. **Agency can load an out-of-tree capability from the host.** Today only `Engine(extra_capabilities=…)` in code can.
   A draft spec in the agency repository (`Plan/draft/395-host-capability-loader/`) proposes
   `AGENCY_EXTRA_CAPABILITIES=<module:Class>[,…]` resolved in `agency/__main__.py` and `agency/cli.py`, with the
   same dedupe-by-name rule `Engine.__init__` already applies. Until that ships, tier 2 is session provenance only.

### Tier 3 — the `kohaerenz` capability (deferred; author's word)

A folder the host repository ships (proposed `agency_ext/kohaerenz/`), loaded by the tier-2 loader, whose verbs are
**relays** over scripts that already exist and already have self-tests: `quotes.verify(path)`, `read.find(slug,
words)`, `ask.pack(question, budget)`, `storyform.check()`, `aegis.run(scenario, out)`, `aegis.replay(run)`,
`aegis.pack(scenario, figure)`. Every verb is role `transform` or `act`, none is `effect` on the research layers, none
writes under `Manuscript/`, `Wiki/`, `Sources/` or `Plan/decisions/`. The value is provenance (a session's questions
and runs `SERVES` its intent) and discovery (`agency search "quotation"`), not a second implementation. It is deferred
because P3 says a tool earns its shape by hand first, and because the briefing's explicit exclusions apply to the
pilot until the offline path has carried a live model call.

## 5. What `scripts/aegis.py` already does, and what the pilot still lacks

Built and self-tested (24 assertions, each able to fail; `python3 scripts/aegis.py selftest`): the two manual cases
from the briefing as fixtures; perception packs per figure with facts, delivered claims and private beliefs kept
apart; the author-only leakage probe absent from every pack and tool response; the fixed validator order; seven typed
rejections leaving state and reserve unchanged; idempotent action ids; reserve never negative; replay from events with
zero model calls; restart; fork; endpoint guard for the monolithic profile; "not run" reported as such; shape checks
on the fixture that refuse a fact without visibility, a belief restating a fact, a scenario calling itself canon.
Evidence: `Plan/runs/aegis-pilot-2026-10-26/`.

Not built, by the briefing's order and on purpose: a live model adapter (extension 1 — one serial recorded call,
after the provider and input scope have permission); the author replay view (extension 2, via `app-refresh`); an
Ink/inkjs scene (extension 3). Also not built, because the survey raised them and the author has not asked: a retry
budget with the rejection reason fed back (from `meta-prompting`, `meta-context-engineering`); a two-strike stop
(from `meta-metacognition`); a belief-update trace with prior/posterior (from `thinking-framework-skills`); a
calibration count table (from `metadpy`, needs a confidence scale first); a contradiction check over typed events
(from `context-engineering-for-writers`). Each is a bounded extension of the validator or the event shape, and each
has a prompt in the briefing.

## 6. The transfer matrix — one row per surveyed repository

"Lands in" names the tier and path; "must not" names the rule that would be broken by taking more. Nine
repositories converge on the pilot (marked ●).

| repository | core aspect worth taking | lands in | must not (rule) |
|---|---|---|---|
| **agency** | the doctrine of §4 tier 1; the plugin of tier 2; `loop.egress_consent` (a pure consent/redaction decision); `dogfood.replay_events`; `requires_input` no-assumption phase gates | §4 | graph-canonical novel verbs, canon writers, mechanised conflicts, Klein-c invariant, Anthropic egress (§3) |
| agency-backups (the older governance substrate) | closed ontology table with `kind` and lossy-NCP marker; falsifier-bound status-quo decisions (`retire when` as a predicate an audit runs); FL0–FL3 friction declaration in PR bodies; prompt self-containedness lint | `Plan/storyform/ncp-names.json` replacing the 8-entry `NCP_NAME` dict in `storyform.py` (unmapped names refused); `## Frustration Log` in PR bodies; a `retire when` predicate on decisions 025/027 | `tasks/` + status index (no board, no backlog); blocking Stop/PreToolUse hooks (no mandatory hook); Dramatica prose under Screenplay Systems copyright |
| ● agentic-harness-patterns-skill | one permission gate (allow/deny/ask, bypass-immune asks); fail-closed action registry; terminal states permanent; two-step save | `aegis.py` already fails closed on unregistered actions; `ask_author` as a third outcome is a candidate | auto-memory into Wiki/Manuscript; swarm fan-out; default-allow |
| ● Agent-Skills-for-Context-Engineering | belief record with holder, source and validity interval; probe-based handoff test (recall/artifact/continuation/decision probes with citations) | `beliefs[]` already carry holder/source/status; a handoff probe over NOW.md § Half-done is a separate check | kanban board; RDF stack; OpenAI judge; hash-seeded embeddings |
| ● agent-file (Letta `.af`) | declarative per-turn rules (`run_first`, `constrain_child_tools`, `exit_loop`) as a pure function; per-invocation context with no tool schema; share gate scanning exported state for secrets/PII | rule vocabulary for the validator's later phases; `scripts/check_share.py` before `web.py` publishes any figure artefact | Letta runtime; self-editing memory; `random.random()` judge |
| ● jungian-soul-agent-skills | draft → confirm → versioned record; typed epistemic fields (`user_stated_facts / observed_patterns / tentative_hypotheses{confidence} / unknown_or_counter_evidence`); per-owner keying with refusal | the proposal/commit split and the facts/claims/beliefs split are in `aegis.py`; confidence on beliefs is open (author's scale) | `update_profile` auto-confirm; a "Self that integrates all parts" prompt; the keyword safety gate |
| ● context-engineering-for-writers | validate-then-commit with an append-only narrative log and a decidable contradiction pass; exemplars cited by path with a companion technique note | the contradiction check as a validator phase; `Plan/craft/exemplars/` with `quotes.py`-checked citations | its `NCP.json` (makes Kael the MC — contradicts decision 025); model-run state update and compression; silent userModel update |
| ● meta-prompting | single-object response contract with a stop; execute-feedback loop with a capped retry; exhaustive invariant search on small fixtures; verify the witness, not only the verdict | retry budget as a later validator extension; a breadth-first invariant search over fixtures | `exec` of model-written code; remote-API branch; paper numbers without saved outputs |
| ● meta-context-engineering | signature contract gate for generated artefacts (AST-checked); bounded repair, fail closed; producer cannot write the evaluator (path-scoped denies) | shape check in `aegis.py` (`check_shape`); Write/Edit denies for `scripts/gold*.py` and `Plan/runs/gold-*/` — author's approval needed for `.claude/settings.json` | OpenRouter clients; gold visible to the producer |
| ● meta-metacognition | two-strike rule; per-claim verification ledger (verified/partial/unverified/contradicted with evidence); anti-trigger column in routing tables; coordination ladder (standalone → federated → tracked → governed) | `scripts/aegis_claims.py` + `claims.jsonl` in run dirs; a stop event after two identical rejections; a decision fixing the agency coupling level (ladder rung) | deliberation tallies that "Decide"; "decide autonomously, never ask"; wisdom libraries |
| ● thinking-framework-skills | ladder-of-inference trace; belief-update ledger (prior, evidence, signed delta, reason, next review); premortem with tripwire/kill; evidence-vs-inference sort; trigger-eval case format | authoring-side belief-record fields validated in code (source ids exist, delta sign matches reason) — after the author approves the schema | any thinking skill for a *character*; winner-picking skills; tier-X methods |
| ● metadpy | type-2 calibration (does stated confidence track correctness); parameter-recovery fixtures; trials-to-counts with a named correction | `scripts/aegis_calibration.py` over accepted events, deferred until a confidence scale exists | PyMC fit; in-place mutation of inputs; one-sided tolerances; silent padding |
| ● awesome-llm-role-playing-with-persona | reading targets only: knowledge-error detection (2409.11726), point-in-time knowledge (2405.18027), observation-only memory (2304.03442), ToM belief tests (2402.06044) | provenance for hand-written knowledge-boundary cases in `Plan/fixtures/aegis/` | LLM-judged persona benchmarks; personas from fan/wiki material |
| epistemic-protocols | option-set relay test and Settled Directions registry; differential-future options; "currency is not support-integrity"; velocity partition (slow risks compile to predicates, fast risks are declared out of the epistemic layer); opacity-preserving comprehension probes before promotion | `Plan/settled-directions.md` + `scripts/settled.py` (cites only `Plan/decisions/` or `kanon.md`); a boundary map in the pilot briefing; probes under `Plan/runs/writing/` | relay collapse for canon facts, wording, names, conflict verdicts, promotion; settled entries citing `Sources/` or `Wiki/`; `/steer` writing standing rules |
| self-driving-agents | mission-scoped retention declarations; named derived views with a declared question and refresh rule; derived inputs excluded from their own refresh | `Plan/scope/<layer>.json` + `scripts/scope_lint.py` (a view may not read what it writes) | hosted retention (`api.hindsight…`); consolidation into "stable facts"; self-updating pages |
| BuildYourOwnHarness | explicit skeleton marker gating publication; protected layers refuse shadowing (report each collision); closed registry resolved by file existence; stagnation counter reset only by a recorded correction | `storyform.py --check` fails when `development.json` writes a field owned by `a/b/weave.json`; `web.py`/`overview.py` refuse `<!-- skeleton -->` | LLM-authored overlays; secret masking that rewrites text; numeric confidence cut-offs; automatic rollback |
| narrative-context-protocol | hash-bound attestation shape; typed references; two-tier moments; preserve, do not normalise | `scripts/ncp_check.py` validating the emitted NCP against Core 3.0.0-rc.1 + dramatica 1.0.0-rc.1 (byte-pinned schema copies); the check prints "schema validation passed", never "valid Storyform" | the NCP file or any slice as character context (it carries `Kaels Wissen`/`Leserwissen`); perspectives as knowledge state; moments as simulation events |
| worldbuilder | per-kind schema + reciprocal-reference check; constraint registry with a lock bit citing a decision; in-world calendar | `scripts/figure_refs.py --check` over `Manuscript/figuren/*.md` and `welt/*.md` frontmatter (`wiki:`, `kanon:`) via `subject.py`; a per-world flag block in `kernwelten.md` citing `kanon.md` | `validate` auto-fix that writes inverse links ("a link is never inferred"); keyword anachronism scan; `wizard yolo` |
| writer-skills (not the upstream of our thirteen) | setup/payoff ledger with fair-play clue matrix; per-scene knowledge test (before/after reveal; "acts on information not yet learned"); issue severity + revision queue; dead-`references/` path check; claim-type evidence thresholds | `Plan/storyform/setup-payoff.json` (proposal rows) + `scripts/setup_payoff_check.py`; a `references/` existence rule in `check_skills.py`; a reader-harm routing row for chapters depicting dissociation | story-bible source priority "manuscript first" (no draft becomes canon); a second canon store; `CANON-`/`SETUP-`/`REV-` id prefixes; Korean rules |
| literary-skills | nine psychological engines with escalation ladders; self-defence theory as a belief shape; intensity dial with chapter budget; scene-born image discipline; fake-depth lexicon count | `.agents/skills/pressure-coach/` (augmentation-only, ranks the author's attempt); `scripts/pressure_counts.py`; `Plan/storyform/pressure.json` (proposal) | rewrite modes; default engine choice; English exemplars; unverifiable corpus maps |
| lit-critic | deterministic style-rule scan from the author's own style sheet with line citations; Horizon lens (what a scene avoids, as observations); cross-run finding identity with scoped suppression (port the design, not the `hash()` key); defend-or-concede discipline | `scripts/stylecheck.py` over `Manuscript/stylesheet.md` (syntax the author approves); `Plan/runs/writing/ledger.jsonl` keyed by sha256(file, line, verbatim line); two rules in `writing-skills/SKILL.md` | the runtime (sends scene text to Anthropic/OpenAI); LLM dedup and inter-lens conflict calls; the learning profile's confidence ratchet |
| writing-intelligence | deterministic voice-metric vector with drift direction; flag-only lint on claim sentences; a controlled conflict-kind vocabulary *if* each kind changes what the author is asked | `scripts/voice_metrics.py` (German sentence splitting; baseline from author-designated samples only) | source-priority ladder and `a_wins/b_wins/merge`; voice restoration and Sentence Surgeon rewrites; automatic storyworld-memory updates; English metrics on German prose |
| prompt-architect | gap-question bank per intent (3–5, progressive); output contract (one flat fenced prompt last); skip-when-complete gate | `.agents/skills/prompt-brief/` + `scripts/prompt_brief.py` (word-boundary intent matching; every missing fact an `ASSUMPTION` that is also asked) | 1–10 substring "scores"; "fill missing elements with reasonable defaults"; unbounded "continue until satisfactory"; the 27 template copies (agency's `prompt` capability already holds them) |
| deep-reading-analyst-skill | per-document 5W2H gap list; SCQA structure field; depth-tiered lens loading; inversion questions as a finding type | `scripts/profile_lenses.py` writing proposals under `Plan/runs/<slug>/`, refusing to run before a candidate list exists | the comparison matrix ("Universal Agreement", "Synthesized Insights"); X/10 ratings; time budgets; web results as evidence |
| dspy-agent-skills | flag-only independent reviewer (`overstated[{quote, why, evidence_needed}]`, `unsupported[]`); judge-of-judge metric with a "could not score" branch | `scripts/review_flags.py` through `lmrun.py` + `claude-cli` only, flags shown by `promote.py sheet` — only if the author asks for it after the pilot | content-hash cache; automatic `demotion()`; `dspy.Refine` write-until-score; free models on corpus quotes; its stale `docs/kohaerenz-protokoll-plugin-plan.md` (pre-reset layout) |
| dspy-agents | model identity on every drift row (`compare()` refuses across identities); program signature as the replay namespace (the AEGIS replay key: sha256 of scenario, source revision, prompt, response); tolerance rules as data | `lmrun.lm_identity()`, an `lm` field in `baseline.py` rows; the replay key is already pinned in `meta.json` | silent fallbacks (first two sentences as a "brief", zero-shot on artefact error); MCP `fetch_url`; the unrecorded 9/29-vs-2/29 claim |
| DSPy-Chain-of-Thought-RAG | passage-supported demonstration gate: an answer counts only if it appears in a retrieved passage | a pure `supported(answer, passages)` in `pairs.py` reusing `quotes.normalise` | HotPotQA gold as metric target; model downloads; compiled prompts as artefacts |
| Character_Ontology_Paper (GOLEM) | persistent figure vs instance-in-a-work; typed features (biographical/physical/psychological); typed narrative roles; states bound to events; **no belief or knowledge class** (the gap that matters for AEGIS) | a typed proposal of the Anteile in `Plan/derived/anteile-typing.json` (disposable) | LLM-assisted RDF extraction; G14/G15 as canon tiers; the CIDOC/LRMoo import stack |
| metacognition-engine | four counter-questions (overconfidence, anchoring, sunk cost, confirmation) as human prompts | a checklist line in the pilot briefing, labelled judgement | regex "bias" scores; `would_i_decide_differently` from a count |
| comprehensive-thinking-skill | premise-source labels (fact, inference, transfer, authority, confabulation, narrative inertia); per-finding "what this changed" | `Plan/briefings/premise-labels.md` for critique findings | the always-on five-review output with a "final judgment"; "deep goal" redefinition of a request (P0) |

## 7. What this concept does not do

- It does not add a database, an MCP server, a controller or a swarm to the pilot; the briefing's exclusions stand.
- It does not move this repository's layout toward agency's (`works/{author}/…`), nor `Manuscript/` into a graph.
- It does not rewrite `scripts/` around the engine. The duplications the tooling survey confirmed (four stop lists,
  five `read_jsonl` copies, four frontmatter parsers, a second store in `rag.py` that `SPEC.md` never mentions,
  about a quarter of `scripts/` dormant by decision) are real and are listed in the survey; fixing them is SPEC §9
  work, not this concept's, and `SPEC.md` should gain `rag.py`'s `serve.db` as a named store before anything else.
- It does not adopt agency's `[S]` or its example corpus as inputs; the example files are stale (§3).
- It does not create a second backlog. The prompts in `Plan/briefings/rebuild-prompts_2026-10-26.md` are
  instructions for sessions the author may or may not start; NOW.md names only the one that continues the mandate.

## 8. Order of work, each step with its acceptance

0. **This PR.** `scripts/aegis.py`, the two fixtures, the run evidence, this concept, the prompts briefing.
   Acceptance: `python3 scripts/aegis.py selftest` 24 held; `selftests.py --only std` 73 held; `state.py --prose`
   0 contradictions. Done and recorded in §5.
1. **Pilot extensions in the briefing's order** — a serial recorded model call replacing the frozen `responses`
   (needs permission), then the author replay view, then Ink. Acceptance per the briefing.
2. **Pilot validator extensions the survey proposes** (§5, second list), one at a time, each a validator phase or an
   event field with a fixture that fails: retry budget, two-strike stop, contradiction pass, belief-update fields,
   claim ledger. Acceptance: the existing 24 assertions still hold; each extension adds its own.
3. **Corpus and storyform guards** (tier 1, outside the pilot): settled-directions registry; layer scope lint;
   `ncp-names.json`; `development.json` shadowing check; NCP schema check; figure reference check; setup/payoff
   check; skeleton marker. Acceptance: each is one script, one `std` suite, one README row, a CI step only with
   the author's approval.
4. **Writing-side coaches and counters** (never writing prose): pressure coach, style check, voice metrics,
   exemplars, premise labels, prompt-brief. Acceptance: `check_skills.py` passes; findings only under
   `Plan/runs/writing/`.
5. **The agency bridge** (tier 2): the loader spec in agency ships; this repository declares file authority in
   `CLAUDE.md`; `.agency/` is gitignored; a session proves provenance end to end. Then, on the author's word, tier 3.

## 9. Verification limits of this session

Read in full: agency's engine, capability, memory, ontology, lifecycle, skill, document and persona modules, its
CLAUDE/AGENTS/CORE/GOALS/TESTING, the `__main__` entry point, machines.json, the plugin descriptors; this
repository's CLAUDE, NOW, GOAL (head), SPEC (head), PRINCIPLES (head), the AEGIS briefing and concept, kanon.md,
the AEGIS card and interview, storyform B and weave, clock-b, the CI workflow, selftests, subject.py. Read by
delegated agents, summarised here: the 29 sibling repositories, agency's novel surface, this repository's tooling
and decision layer. Not run: anything needing a venv, a model or the network. Agency's test suite was not run.
Agency's `examples/kohaerenz-protokoll/` staleness was checked by the survey on four named facts, not line by line.

## 10. Questions for the author (noted; work continues without waiting)

Blocking the bridge (tier 2/3), not the pilot:
1. **Coupling level with agency.** Standalone (patterns only, today), federated (optional plugin for sessions), or
   tracked (a `kohaerenz` capability)? The ladder is from `meta-metacognition`; a decision file would fix the rung.
2. **File authority declaration.** May `CLAUDE.md` state that an agency graph, if present, is a derived index of
   `kanon.md`, `Plan/decisions/`, `Sources/`, `Wiki/` and never a writer of them?

Blocking pilot extensions:
3. **Sweep cost and reserve** are test assumptions (`T1`, `T2`); should any value be read from `clock-b.json` as a
   rule, or stay invented until a live run exists?
4. **The counterfigure** is Kael in both cases (`T4`); is that the figure you want beside AEGIS?
5. **A confidence scale for beliefs** (needed before belief-update fields or calibration): none, three steps, or
   a number?
6. **Which chapters plant 734, the Genesis steps and the Vortex** (Q7, W12, Q8) — needed before a setup/payoff
   ledger holds anything but empty rows.

Not blocking anything:
7. Whether `Plan/concept/` documents should carry a state (agency's draft/open/done) or stay dated-and-corrected.
8. Whether a `## Frustration Log` line in PR bodies (from the older agency) is wanted.
