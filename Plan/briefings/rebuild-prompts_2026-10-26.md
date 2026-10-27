# Rebuild prompts — one per follow-up session (2026-10-26)

Status: instructions a session can take, derived from `Plan/concept/rebuild-with-agency_2026-10-26.md`. None is
scheduled; NOW.md names only the mandate's continuation. Each prompt is self-contained for a session with no memory
and keeps the session contract: read `CLAUDE.md`, `NOW.md`, `PRINCIPLES.md` first; run `sessions.py board`; claim
with a pull request holding `Session: <id>`; standard library only; every new check gets a self-test that can fail,
a `std` suite in `scripts/selftests.py` and a row in `scripts/README.md` (the prose check enforces the row); no
model call, no network, nothing written under `Manuscript/`, `Wiki/`, `Sources/` unless the prompt says so; author
questions go to `Plan/questions-for-the-author.md` and work continues. Constructs enter as `provisional / may not /
retire when`. Where a prompt names a sibling repository, read it for the pattern only; copy no code and no prose.

The prompts are grouped by the concept's order of work (§8). Within a group, any order.

## Group A — the AEGIS pilot (`Plan/briefings/aegis-agent-pilot.md` wins over every prompt here)

### A1 — validator extensions, offline

Goal: extend `scripts/aegis.py` with five bounded rules the survey proposed, one at a time, each as a validator
phase or an event field with a fixture that fails. Read first: `Plan/briefings/aegis-agent-pilot.md`,
`Plan/fixtures/aegis/README.md`, `scripts/aegis.py` (its docstring and `validate`), `Plan/concept/rebuild-with-agency_2026-10-26.md` §5.
Add, in this order, keeping the existing 24 self-test assertions green: (1) a **retry budget** — a rejected proposal
may be re-proposed with the typed reason attached at most 2 times under the same `action_id` prefix, then status
`refused` (pattern: `/home/user/meta-prompting`, `Math/infer/inference.py` warning injection; no code copied);
(2) a **two-strike stop** — a second identical rejected proposal in one run appends a `stop` event and the run halts
without choosing another action (pattern: `/home/user/meta-metacognition`, `.github/agents/atlas.agent.md` Habit 3);
(3) a **contradiction pass** over typed events — an event that re-opens a closed anomaly or re-masks a masked memory
is rejected `contradicts_history` (pattern: `/home/user/context-engineering-for-writers/claude-swarm.yml` steps 5–7);
(4) a **claim ledger** `claims.jsonl` per run, rows `{claim, status: verified|partial|unverified|contradicted,
evidence, check}`, checked by `scripts/aegis_claims.py --selftest`; (5) **per-event observation ids resolved against
the actor's pack at commit time** (already true; add the witness check that the cited fact's text is unchanged).
Acceptance: `python3 scripts/aegis.py selftest` adds one assertion per rule; `python3 scripts/selftests.py --only
std` held; `Plan/runs/aegis-pilot-<date>/` holds a re-run of both cases. Stop and ask: the retry budget value; whether
a `stop` event should surface in the app.

### A2 — one serial, recorded model call (only with permission)

Goal: replace the frozen `responses` list with one live proposal per turn through an existing adapter, recorded,
cache off, serial. Read first: `CLAUDE.md` § Model calls; `Plan/decisions/007-*`, `008-*`, `011-*`;
`scripts/claude_cli.py`, `scripts/claude_lm.py`, `scripts/lmrun.py`; `scripts/aegis.py` `pack`. Build
`scripts/aegis.py propose <run> <figure>` that renders the figure's pack (and nothing else) into a prompt assembled
from six versioned parts (role, scene, limited knowledge, present intent, allowed actions, output format), sends it
through `claude_cli.py` with tools off, parses one JSON object (action, target, observations, reason, optional
`log`), freezes it under `<run>/responses/<n>.json` with prompt version and usage, and commits it through the one
writer. Replay must still need no model. Acceptance: the probe is absent from the prompt bytes (assert on the
recorded prompt); a parse failure is status `unparsed`, never a score; the run names actual cost. **Stop before the
first call** unless the briefing's condition holds: the provider and input scope already have the author's
permission (decision 011 covers `claude -p` first-party; the scenario packs are invented test state, not corpus
text — state this in the PR and let the author confirm).

### A3 — knowledge-boundary cases

Goal: ten hand-written cases under `Plan/fixtures/aegis/cases/` where a figure's belief differs from a fact, each
with the expected validator verdict and the arXiv id it derives from (2409.11726 knowledge errors, 2405.18027
point-in-time knowledge, 2304.03442 observation-only memory, 2402.06044 ToM). Read first: the pilot briefing and
`Plan/fixtures/aegis/README.md`. Add `scripts/aegis.py check-cases` failing when a fact has no `visible_to`, a
belief equals a fact, or a case cites no source. Acceptance: all ten run through `run`; none changes canon. Stop and
ask the author before any case needs a character fact absent from `kanon.md`.

### A4 — belief-update fields and calibration (needs the author's confidence scale first)

Goal: after the author chooses a scale (question 5 in the concept), add `confidence_prior`, `confidence_posterior`,
`delta_reason`, `source_event_ids[]` to beliefs; validate in code that source ids exist in the committed log and
the delta sign matches the reason class (pattern: `/home/user/thinking-framework-skills/skills/think-belief-update-routine/SKILL.md`).
Then `scripts/aegis_calibration.py`: from accepted events, a per-figure count table (correct/incorrect × rating bin)
and d′/criterion with a named correction, a seeded recovery fixture (d′=1, c=0, ≥1000 trials), and "insufficient
trials" on the manual cases (pattern: `/home/user/metadpy/metadpy/utils.py` `trials2counts`; no scipy — ask before
any numerical optimisation). Acceptance: recovery within a tolerance named in the config; event log hash unchanged.

### A5 — share gate before publication

Goal: `scripts/check_share.py` that flags non-null secret-named keys, message-history keys, email-shaped strings and
personal fields in any JSON artefact passed to it, registered as a `std` suite and run by `scripts/web.py` on every
figure or simulation artefact before publication (pattern: `/home/user/agent-file/agents/CONTRIBUTING.md` §2).
Acceptance: fails on a fixture with a planted secret, passes a clean one. Stop and ask: whether it also covers `Wiki/`.

## Group B — corpus and storyform guards

### B1 — settled directions

Goal: a registry so a question the author already answered is relayed, not re-asked. Create
`Plan/settled-directions.md` (entry = `{id, direction, cites, decided_by: author, date}`, `cites` only
`Plan/decisions/NNN-*.md` or `Manuscript/kanon.md#<id>`; zero entries unless the author confirms each) and
`scripts/settled.py` (`check`: every cite resolves and none points under `Sources/` or `Wiki/`; `open`: question lines
in `Plan/questions-for-the-author.md` whose `settled_by:` names a registry id; it never edits the question file) with a
self-test holding one valid, one Wiki-citing and one dangling entry. Pattern: `/home/user/epistemic-protocols/.claude/rules/axioms.md`
§A5 and its `CLAUDE.md` § Settled Directions. Never auto-settle a canon fact, wording, scope, name, conflict verdict,
promotion or user-facing flag (P0 reserves these).

### B2 — layer scope

Goal: one scope file per research layer declaring what it may contain, what it ignores, and which derived views it
feeds; a lint that fails when a view reads a path it writes. Create a decision file first — `Plan/decisions/<NNN>-layer-scope.md` with the next unused number at the time
(030 is the writing workshop, 031 is reserved for the session apps, 032 is the open site: `ls Plan/decisions`; a
duplicate number collides in the app's decision addresses) — as a proposal for the author, then `Plan/scope/{sources-terms,sources-notes,wiki,manuscript}.json` and
`scripts/scope_lint.py --check`. Pattern: `/home/user/self-driving-agents/engineering/bank-template.json` and
`src/scripts/lint-bank-templates.mjs`. Add the CI step only with the author's approval. Nothing retains,
consolidates or calls a model.

### B3 — NCP names as a checked table

Goal: replace the 8-entry `NCP_NAME` dict in `scripts/storyform.py` with `Plan/storyform/ncp-names.json` (`id`,
`canonical`, `ncp_appreciation`, `partial`, `aliases_de: []`), pre-filled with exactly the existing pairs; `nf()`
refuses an unmapped name and `--check` reports each. Pattern: `/home/user/agency-backups/maintenance/schemas/narrative-ontology/ontology.schema.json`
(structure only). Acceptance: `storyform.py --check` exits 0 on the current storyforms; a fixture with an unknown
spelling exits 1 and names it; `dramatica.py selftest` passes; `a/b/weave.json` unchanged. Stop before adding any
spelling beyond the eight, accepting a `partial` mapping, or writing `aliases_de`.

### B4 — protected storyform fields and the skeleton marker

Goal: (1) `storyform.py --check` fails when a row in `Plan/storyform/development.json` writes a field owned by
`a.json`, `b.json` or `weave.json`, printing each collision; the protected set is one named constant; (2) `web.py`
and `overview.py` refuse a page carrying an explicit `<!-- skeleton -->` marker and `state.py` counts them — never
detect skeletons by text prefix. Pattern: `/home/user/BuildYourOwnHarness/src/application/overrides.rs`,
`src/compiler/render.rs`. Fixtures: one shadowing and one clean `development.json` row; one marked page. Stop and
ask first if the protected-field set is undecided.

### B5 — NCP structural check

Goal: `scripts/ncp_check.py` validating `Plan/storyform/ncp/kohaerenz-protokoll.ncp.json` against byte-pinned copies
of NCP Core 3.0.0-rc.1 and the dramatica 1.0.0-rc.1 profile (`/home/user/narrative-context-protocol`, commit
afa8d86; copies under `Plan/storyform/ncp/schema/` with sha256), format assertions on, printing "NCP schema
validation passed" and never "valid Storyform"; `storyform.py --check` and `selftest` call it. Add fixtures: the
current output as valid; `ncp_version: "3.0.0"` and a missing `story` as invalid. The NCP file is never loaded into a
character context (it carries `Kaels Wissen`/`Leserwissen`). Stop before committing schema copies.

### B6 — figure and world references

Goal: `scripts/figure_refs.py --check` over `Manuscript/figuren/*.md` and `Manuscript/welt/*.md` frontmatter
(`wiki:` resolves to `Wiki/terms/` or `Wiki/candidates/`; `kanon:` ids exist in `kanon.md`; non-reciprocal targets
listed), read-only, via `scripts/subject.py`'s frontmatter boundary. Pattern: `/home/user/worldbuilder/scripts/worldbuilder.py`
L292–325, L2457–2560 (never the auto-fix). Unresolvable references are listed as unchecked, never passed. Stop and
ask: whether `kanon:` entries are ids or free text (cards show both); whether a per-world flag block in
`kernwelten.md` citing `kanon.md` is wanted.

### B7 — setup and payoff

Goal: `Plan/storyform/setup-payoff.json` (proposal rows: `setup_id, clue_role, planted_in_chapter, reader_visibility,
payoff_id, paid_in_chapter, status: proposal, fairness_test`) and `scripts/setup_payoff_check.py` (payoff without
setup, `paid` without a chapter, a required clue without `fairness_test`; fairness stays a named judgement);
`continuity-editor` reads the ledger and never writes it; `check_skills.py` gains a dead-`references/` path rule
(report-only for vendored skills). Pattern: `/home/user/writer-skills/skills/fiction-book-writing/references/setup-payoff.md`.
Stop and ask: which chapters plant 734, the Genesis steps and the Vortex (Q7, W12, Q8).

## Group C — writing-side coaches and counters (never writing prose)

### C1 — pressure coach and lexical counter

`.agents/skills/pressure-coach/SKILL.md` modelled on `psychic-distance` (one drill, German, ranks the author's
attempt; engines and a 1–5 dial as provisional; 2–3 engine candidates, the author chooses);
`scripts/pressure_counts.py` counting author-supplied lexicon hits per `Manuscript/kap-NN.md` into
`Plan/runs/writing/`; `Plan/storyform/pressure.json` (status proposal); one routing row in `writing-skills/SKILL.md`.
Pattern: `/home/user/literary-skills/skills/dostoevsky-psychological-drama/references/psychological-engines.md`,
`hesse-inner-journey/references/duality-and-individuation.md`. No rewrite mode; no English exemplars.

### C2 — style check and finding ledger

`scripts/stylecheck.py` reading `Manuscript/stylesheet.md` (syntax the author approves) with word boundaries,
writing `Plan/runs/writing/<target>/stylecheck_<date>.md` with `<file>:L<n>` citations; `Plan/runs/writing/ledger.jsonl`
keyed by sha256(file, line number, verbatim line) with dispositions `kept|settled|silenced` only from the author's
words; two rules added to `writing-skills/SKILL.md`: Horizon (observations of what a scene avoids, no prose, no
unverified citations) and pushback (concede only on textual evidence; a bare preference is recorded as the author's
choice). Pattern: `/home/user/lit-critic/orchestrator/services/code_checks/stages.py` `_check_style_md_rules`,
`core/domain.py` `build_correlation_key` (port the design, not the `hash()` key).

### C3 — voice metrics

`scripts/voice_metrics.py` (German sentence splitting with abbreviations and dialogue quotes; mean and SD of
sentence and paragraph length, commas per 100 words, questions per 500 words; `--baseline` from author-designated
samples only; `--check` with drift direction per metric), self-test with a flat "drone" passage flagged and a sample
`stable` against itself; `Plan/runs/voice/README.md`. Pattern: `/home/user/writing-intelligence/references/voiceprints/voice_fingerprint_engine.md`.
Stop and ask if no baseline samples are designated (`Manuscript/README.md`: no chapter is approved).

### C4 — exemplars, premise labels, prompt briefs

(a) `Plan/craft/exemplars/<slug>.md` with 3–5 technique bullets each citing a line obtained from `read.py --find`,
checked by `scripts/exemplars.py check` through `quotes.py` (pattern: `/home/user/context-engineering-for-writers/examples/README.md`,
method only); ask before choosing exemplars (own approved chapters vs external texts). (b) `Plan/briefings/premise-labels.md`:
findings carry one of fact, inference, transfer, authority, confabulation, narrative inertia, plus a source line; an
unlabelled finding is unmeasured; no "final judgment" section (pattern: `/home/user/comprehensive-thinking-skill`).
(c) `.agents/skills/prompt-brief/` + `scripts/prompt_brief.py` (`route` with word-boundary matching, `questions`
3–5 per intent from `questions.json` with MIT attribution, `check`); every fact the author has not supplied is an
`ASSUMPTION` that is also asked; the final prompt is the last fenced element (pattern:
`/home/user/prompt-architect/skills/prompt-architect/SKILL.md` §2, §4, §5). Ask first whether to build this or wait
for agency's `prompt` capability (tier 2).

### C5 — reading lenses and reviewer flags (low priority)

(a) `scripts/profile_lenses.py`: a 5W2H gap list and an SCQA field per document profile under `Plan/runs/<slug>/`,
tagged `status: proposal`, refusing to run before `03-candidates.md` exists (pattern:
`/home/user/deep-reading-analyst-skill/src/deep-reading-analyst/references/5w2h_analysis.md`, `scqa_framework.md`).
(b) Only if the author asks after the pilot: `scripts/review_flags.py`, a flag-only reviewer
(`overstated[{quote, why, evidence_needed}]`, `unsupported[]`) through `lmrun.py` + `claude-cli`, flags shown by
`promote.py sheet`; cache off; an empty flag set is "could not score", never 1.0; an unresolvable quote is
uncheckable (pattern: `/home/user/dspy-agent-skills/skills/dspy-adversarial-review/example_adversarial_review.py`).

## Group D — the agency bridge

### D1 — agency side: the host capability loader

In `/home/user/agency`, implement `Plan/draft/395-host-capability-loader/spec.md`: `AGENCY_EXTRA_CAPABILITIES`
(comma-separated `module:ClassName` or `module`) resolved in `agency/__main__.py` and `agency/cli.py` into
`Engine(extra_capabilities=[…])`, with the same first-wins dedupe by name; a typed `ToolResult.failure` naming the
module when import fails; an acceptance scenario in `tests/acceptance/`; `scripts/check-drift` clean; a `TODO.md`
row. Follow agency's `CLAUDE.md` (dogfood, TODO.md in the same commit, behaviour tests only, no hardcoded counts).

### D2 — Kohärenz side: file authority and session provenance

After D1 ships and the author answers questions 1–2 of the concept: add to `CLAUDE.md` a short paragraph declaring
`kanon.md`, `Plan/decisions/`, `Plan/storyform/`, `Sources/`, `Wiki/` file-authoritative for any agency graph; add
`.agency/` to `.gitignore`; record the coupling rung in `Plan/decisions/`; run one session with the plugin,
`document.ingest … write_anchor=False` on a decision file, and show the provenance traversal in the PR. No CI step,
no hook, no verb that writes under the research layers.

### D3 — the `kohaerenz` capability (only on the author's word)

`agency_ext/kohaerenz/_main.py` (CapabilityBase; verbs `quotes.verify`, `read.find`, `ask.pack`, `storyform.check`,
`aegis.run`, `aegis.replay`, `aegis.pack` as subprocess relays over the existing scripts; roles `transform`/`act`;
no `effect` on research layers; docstring derives the skill) loaded through D1; an offline acceptance that every verb
returns the script's own JSON unchanged and that no verb can write under `Manuscript/`, `Wiki/`, `Sources/`,
`Plan/decisions/`.
