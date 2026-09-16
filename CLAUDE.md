# Kohärenz Protokoll — working agreement

A German hard-SF novel (Hard SciFi / Cosmic Horror / Psychological Thriller),
its research corpus, and the deterministic tooling that keeps the two honest.

**Canon prose is German and is never translated. Engineering and work language
is English.**

## Rule 0 — never assume; ask

**Whenever a decision would otherwise rest on an assumption, stop and use the
`AskUserQuestion` tool instead of guessing.** Canon facts, character and plot
choices, German wording, which document wins on a conflict, scope, a name —
a wrong assumption baked into canon prose is expensive to unwind, and a
question is cheap. This is a hard rule, not a preference.

Two decisions that are never a session's to make:

- **User-facing flags are user-owned.** `--write`, `--promote`, `--apply` and
  anything else a skill lists in its `argument-hint`
  (`Wiki/schema/writers.yaml → user_flags`). Never set one on your own; ask,
  with the dry-run output in hand.
- **Promotion and canon.** Research becomes a wiki page, and a wiki page
  becomes canon, only when the author says so.

## Session startup

Read the root `todo.md` at the beginning of every session, before planning or
changing repository content. Treat its highest-priority open task, scope
boundaries, sequencing, and acceptance criteria as active project context.
Do not silently start a deferred migration: follow the task's stated mode and
ask the author when it requires an architectural decision.

## The five layers

| layer | what it is | who writes it |
|---|---|---|
| `Sources/` | raw exported research, immutable | the documented fetch procedure and the inventory scripts, nothing else |
| `Wiki/` | drafted knowledge pages, promoted by a human | `/research-ingest` drafts, `/kp-promote` promotes |
| `Graph/` | the novel's facts as plain JSONL | `/kp-canon`, and the author by hand |
| `Canon/` | normative prose | the author |
| `Manuscript/` | the book — **the source of truth for prose** | the author, through `/kp-write` |

Research is not canon. The 680 Drive documents in
`Plan/research/…quellenindex…` enter through the three-layer knowledge system
(`Plan/wiki/knowledge-system-concept_2026-09-15.md`) and reach `Canon/` only
through a D-xx decision.

**On conflict**, for manuscript work, the storyform/outline document is
normative: `Canon/kohaerenz-protokoll_storyform-und-outline_2026-06-10.md`.
Inside the research-wiki loop Canon is `unverified` until checked against the
populated wiki, and a Canon/research conflict is an open question with no
default winner (D-W12).

## The workflow — nine commands

```
Drive → Sources/ ──/research-ingest──→ Wiki/candidates/ ──/kp-promote──→ Wiki/
                                                                            │
Canon/ ──/kp-canon──┐                                              a D-xx decision
                    ├──→ Graph/ ──renders──→ Codex/                         │
        /kp-world ──┘        │                                              ↓
                             └──/kp-write──→ Manuscript/                 Canon/
```

| command | does |
|---|---|
| `/research-ingest` | exported sources → candidate pages, a knowledge diff, a metric score; chunked by default (3 sources), each concept merged from its whole claim history |
| `/kp-promote` | a reviewed candidate → `Wiki/sources/` or `Wiki/concepts/` |
| `/kp-canon` | `Canon/` → `Graph/`, then re-render the Codex views |
| `/kp-world` | derive a Kernwelt, level or population through the chain, then land it in `Graph/` |
| `/kp-write` | draft or revise a scene, with its knowledge fences and checks |
| `/kp-check` | every free gate at once |
| `/kp-ask` | a cited answer from the repository, never from memory |
| `/clarify` | make scope, terms and assumptions explicit — **mandatory before promotion to canon** |
| `/tetraframe` | four isolated positions on a contested decision — **mandatory before a D-xx**, a merge, a supersession, or anything contradicting Canon |

Four skills carry the craft: **novel-architect** (the whole novel, routing to
`reference/{character,scene,structure,world,legacy}.md`), **dramatica**
(storyform reasoning and exact vocabulary), **ncp-author** (NCP A/B alignment),
**lit-critic** (prose review).

## Before declaring anything done

```bash
python3 scripts/kp_check.py [--chapters]
```

One command, every deterministic gate: wiki health, rendered wiki and Codex
views, the source manifest, claim provenance (D-W2), both storyforms, the world
axioms, chapter drift, and optionally every chapter lint. Free — no API key, no
network — so there is no reason to skip it.

Two results are expected and are not defects: Storyform B fails rows 2 and 10
(its documented heterodox signposts, Canon-Lock), and chapter drift reports
`ahead` for most chapters because `Manuscript/` holds the prose while `Graph/`
holds outline stubs.

**A lint proves a forbidden word is absent; it can never show that something
required is missing.** After the gates pass, read the work: frontmatter
complete, cross-references resolving, every new term carrying a codex entry, no
sentence that defers work instead of doing it. Deferral language is a defect —
write it, or mark it `[L]` / a D-xx with an owner, and ask.

The prose gate costs tokens and is separate:
`python3 scripts/lit_critic_gate.py --chapter N` (exit 0 pass · 1 blocking ·
2 could not run; `--locks-only` runs the free lints alone). `lint_chapter.py`
is the single encoding of the R-rules — never restate them elsewhere.

## Graph/ — the novel's facts

`Graph/README.md` is the contract. One JSONL file per node label plus
`edges.jsonl`; `_nid` is the integer edges point at. Read it with
`tools/kpgraph`, write it with `tools/kpgraph/writer.py`, both standard library
only. Node ids are derived from label plus natural key, so re-ingesting is
idempotent by construction.

1,180 records: 602 codex entries, 223 claims, 111 world axioms, 97 beats,
56 story-time events, 41 chapters, 26 decisions, 15 scenes, 7 worlds, the
Novel and the Storyform. Everything under `Codex/` is a **generated view** —
never hand-edit it; change the record and re-render.

`Graph/schema.yaml` is the second half of the contract: it declares how those
records partition into a navigable Codex. One convention, three views:

```
Codex/<VIEW>.md          navigation only — counts and links, never a body
Codex/<view>/README.md   the rendered index of that view
Codex/<view>/<slug>.md   one retrievable unit
```

`GLOSSARY.md` → `entries/<category>/<slug>.md` (one entry), `WORLD-AXIOMS.md` →
`axioms/<world-slug>.md` (one world's whole rule set), `MASTER-TIMELINE.md` →
`timeline/<phase-slug>.md` (one story phase). Entries partition by the
`**Kategorie:**` each record already carries; an undeclared category lands in
`entries/_misfiled/` so drift is visible rather than silent.

**Retrieval is a command, not a habit:**

```bash
python3 scripts/context_packet.py --chapter N   # ~21,700 tokens, not ~84,400
```

Three tiers — the always-on categories, every entry whose `triggers` occur in
that chapter, and all world axioms. The chapter window is computed on each run
rather than stored, so it cannot go stale, and membership implies the entry was
already in play at or before that chapter, which is what makes it spoiler-safe.
A per-entry spoiler ceiling depends on the story encoding and worldbuilding and
is recorded in `Graph/schema.yaml` as `not-implemented`, so read a body before
using it when the chapter is early and the entry is central.

Closed enums, all of them enforced:

- **CodexEntry `kind`**: `concept`, `location`, `faction`, `artefact`,
  `minor-character`. Anything else is stored as `concept` with its original
  category as the first body line, `**Kategorie:** <kind>`.
- **Scene `pov`**: `first`, `second`, `third-limited`, `third-omniscient`.
- **WorldAxiom `severity`**: `hard`, `soft`.
- **Chapter status**: `outlined` → `drafted` → `revised` → `final`.
- **Novel status**: `concept` → `outlining` → `drafting` → `revising` →
  `beta` → `querying` → `published`. Currently `outlining`.
- **NovelClaim `domain`**: the ten research domains (historical, scientific,
  cultural, geographical, linguistic, philosophical, religious, political,
  technological, biographical). The canon file goes in `source_uri`.

**D-W2**: "the graph" means `Graph/`, and it never receives wiki page bodies.
A claim's `source_uri` points at `Sources/` or `Canon/`, never `Wiki/`;
`scripts/audit_graph_claims.py` enforces it.

Beat ordering is thin: 3 of the 97 beats carry a `PRECEDES` edge. The rest are
grouped by their `scene` property and ordered by insertion. Scene grouping is
the reliable signal; a topological sort over `PRECEDES` is not.

## The novel

**Registered**: `novel:9d170c31` — "Kohärenz Protokoll", author *The Agency
System*.

**Architecture.** Arc I (Kap. 1–13): anomaly → system contradiction →
counter-register → loss of evidentiary certainty → loss/relationship →
conscious plurality → internal practice. Arc II (14–26): access → knowledge →
intervention. Arc III (27–40): intent → confrontation capacity → truth
rotation → insufficient replacement order → plural preservation. 35/36 are the
operative storyform turn; 37 is a real but non-scalable false victory; 38/39
are synthesis; 40 is coda, not explanation.

**Worlds.** 7 levels carrying 111 axioms. A new Kernwelt, level, sub-locality
or population is derived through `/kp-world` — Ebene → Logik-Regime →
DKT-Ausdruck → Sensorik → Bewohner/Kognition → Ordnung → Sprachregister →
Geschichte, an author checkpoint at every layer — and lands in `Graph/`.
`scripts/world_check.py` reports axiom pairs that share rare motifs where
exactly one side is negated; a flagged pair is a question for the author, and
resolving one goes through `/tetraframe`.

**Storyform.** Deliberately two, simultaneously. `ncp.json` is A (Kael/K₁) and
passes all 13 decidable rows. `ncp-b.json` is B (AEGIS/K₀) and carries two
documented heterodox rows — linear-progressive signposts, Canon-Lock, never
"fixed". `python3 scripts/storyform_check.py` runs both; `tools/kpstoryform`
holds the checks, the vendored NCP v1.3.0 vocabularies (463 appreciations,
144 narrative functions) and the Dramatica ontology.

**Locks that hold everywhere.** AEGIS is tragically innocent, never a villain.
Resolution is functional multiplicity, never fusion; no eliminated parts. Juna
is a cosmological constant and witness function, not a love interest. Theory
stays submerged — mechanisms reach the reader through work, objects, timing,
space, body, logs and omission. No DKT terminology in the first 50 pages; the
Multiplizitäts-Schleier holds until Kap 13.

## Wiki compass (read before `Wiki/**` work)

The concise cross-agent rules live in `AGENTS.md`; the full contract lives in
`Wiki/SCHEMA.md` and `Wiki/schema/*.yaml`. The four page entities are `source`,
`concept`, `question`, and `synthesis`. Store one semantic entity per page at
`sources/<category>/`, `concepts/<kind_detail>/`, `questions/<axis>/`, or
`syntheses/<YYYY>/`; candidates mirror that layout. Start at `Wiki/index.md`
and descend through rendered local `README.md` indexes. Page budgets are
enforced by `scripts/wiki_lint.py`; split before the hard maximum. Never edit
rendered indexes by hand. Use the repo-local `wiki-maintenance` skill for
moves, splits, navigation repair, and schema evolution. Operational terms are
defined in `Wiki/GLOSSARY.md`; the domain glossary is generated under
`Codex/entries/`, routed from `Codex/GLOSSARY.md`. Duplicate slugs, broken navigation links, mispartitioned
pages, oversized pages, and stale local indexes are structural blockers.
For manuscript retrieval, start with `python3 scripts/context_packet.py
--chapter N` for the novel's own facts, and `Wiki/context-map.md` for the
research layer — enforce its chapter/spoiler window, load matching headings
next, and inspect raw source lines only when evidence is required. The
retrieval ladder is `wiki-maintenance` →
`references/context-loading.md`.

## Every LLM step is a DSPy program

Typed Signatures, closed enums, rich-feedback metrics — no prompt strings. They
live in `tools/kpwiki/` and are documented in `docs/dspy-base.md`.
`scripts/setup_dspy.sh` builds `.venv-dspy` and runs the offline smoke test.
Without `ANTHROPIC_API_KEY` they run through the `claude` CLI
(`KP_LM_BACKEND=auto`, `tools/kpwiki/local_lm.py`); GEPA works there too.

The wiki contract is `Wiki/SCHEMA.md` plus `Wiki/schema/*.yaml`, loaded by
`tools/kpwiki/wiki_schema.py` — the YAML is the single source of truth and the
Python enums are derived from it at import time.

The first live `BatchCompile` run is recorded in
`Plan/wiki/pilot-run_2026-09-16.md`: what it cost, what it found, and the
defect classes it exposed. Read it before the next run.

## What runs automatically

Hooks in `.claude/settings.json`, all warn-only:

- **SessionStart** — the roster in `.claude/hooks/bootstrap.md`, plus a
  `CURRENT_TASK.md` restore and a stale-`Codex/` check.
- **UserPromptSubmit** — skill routing.
- **PreToolUse Write/Edit** — the anti-deferral scan (English and German
  patterns; `[L]` is a legitimate marked gap).
- **PostToolUse Write/Edit** — chapter files run `lint_chapter.py --hook`;
  `Codex/`, `Canon/` and `ncp*.json` edits get discipline warnings.
- **PreCompact** — save session state to `.claude/CURRENT_TASK.md`.

No plugins are enabled. Everything the repository needs lives in `scripts/`,
`tools/` and `.claude/`, and runs on the standard library unless it calls an
LLM. Agents with persistent memory: `@worldbuilder-editor`,
`@worldbuilder-physicist`, `@worldbuilder-researcher`
(`.claude/agent-memory/`).

Reasoning reference for hard cases — epistemology, adversarial protocols,
anti-patterns: `docs/canon-rules/README.md`.
