# Worldbuilding Codex — integration into Kohärenz Protokoll

Vendored from <https://github.com/alainator/worldcodex> (MIT — see
`docs/worldcodex-LICENSE.txt`), upstream commit `4f58f2b42fb6bdb5efbfd24839f91298670c0e39`
(2026-05-02, "feat: 7 learnings from regional derivation …"), integrated 2026-09-15.

## Status — consolidated 2026-09-16

**This document is the provenance record of the vendored layer, not a
description of the current surface.** On 2026-09-16 the Agency plugin was
removed and the suite was consolidated: 19 vendored skills plus 9 project
skills became **4 skills**, 5 commands became **9**, and the provenance graph
moved out of `.agency/session.db` into `Graph/` as plain JSONL. What the
vendored suite contributed survives, but rarely under its original name:

| vendored | where it lives now |
|---|---|
| `writing-worldbuilding`, `designing-worlds`, `designing-lore`, `deriving-social-systems`, `auditing-human-assumptions`, `/civilization-build` | `/kp-world` (the derivation chain, with hard checkpoints) and `novel-architect/reference/world.md` |
| `auditing-canon`, `cross-checking`, `verifying-completion`, `/lint-wiki`, `/full-audit-canon` | `scripts/kp_check.py` (eight deterministic gates) and the reading discipline it names |
| `canon-rules` | `docs/canon-rules/` — reference material, not a workflow |
| `researching-papers`, `integrating-research` | `/kp-ask` and `scripts/research-tool.py` |
| `interrogating-design`, `planning-worldbuilding` | `/tetraframe` and `/clarify` |
| `/ingest` | `/kp-canon` (`Canon/` → `Graph/`) |
| `/query` | `/kp-ask` (a cited answer from the repository) |
| `deep-reading`, `extracting-entities`, `compiling-entities`, `writing-science`, `writing-style`, `code-clarifier` | removed; the capability was generic and the repo's own tools cover it |
| the graph | `Graph/` — one JSONL file per node label, read by `tools/kpgraph` |
| `find_axiom_contradictions` (engine verb) | `scripts/world_check.py`, re-derived for German text |

The hooks and the three agents survive unchanged in purpose. The sections
below describe the 2026-09-15 integration as it was performed, and are kept
because they explain why the mapping is what it is.

## How the suite was adapted (2026-09-15)

The suite is not a drop-in copy. Its generic wiki model (GLOSSARY.md, MASTER-TIMELINE.md,
`_index.md`, `meta/LOG.md`, `physics/` directories) was mapped onto what this repo already
has: a normative `Canon/` corpus, a provenance graph with ~600 codex entries, Plan/ documents,
and a German manuscript with hard drafting rules. Where upstream assumed a hand-maintained
wiki, this integration renders the wiki from the graph and points every skill, command, hook
and agent at the real files. Engineering language is English; canon prose stays German.

## Concept mapping

| Upstream concept | Here | Why |
|---|---|---|
| Raw sources (read-only) | `Canon/` (storyform-und-outline normative), `Plan/drafting/sources/` | already the immutable reference layer |
| The wiki (LLM-maintained) | `Graph/` (CodexEntry, StoryTimeEvent, WorldAxiom, World, NovelClaim) — was `.agency/session.db` until 2026-09-16 | one record per line, greppable and diffable; a second hand-maintained Markdown copy would drift (Plan/sessions learnings §2) |
| `GLOSSARY.md` | `Codex/GLOSSARY.md` — **generated** by `scripts/render_codex_views.py` | 602 entries, grouped by codex `kind` + `**Kategorie:**` |
| `MASTER-TIMELINE.md` | `Codex/MASTER-TIMELINE.md` — generated | 56 StoryTimeEvents bucketed by story phase, with HAPPENS_AT / REVEALED_IN scene links |
| physics backend / foundational axiom | DKT (Canon begriffe §1–§2, §14) + `Codex/WORLD-AXIOMS.md` — generated | 111 axioms in 7 Worlds |
| `_index.md` | `Canon/README.md`, `chapters/README.md`, `.claude/skills/PROJECT_REFERENCES.md` | existing indexes |
| `meta/LOG.md` | `Plan/sessions/<date>-learnings.md` | existing session-log convention |
| `meta/plans/` | `Plan/worldbuilding/` (world builds), `Plan/drafting/` (chapters) | existing plan tree |
| `meta/design-decisions/` | `Plan/drafting/decision-log*.md` (D-xx), `Graph/nodes/decision_record.jsonl`, `Plan/worldbuilding/decisions/` | decisions already live there |
| `_source/research/` | `Plan/research/` (downloads git-ignored, INDEX.md committed) | keeps the repo tree |
| `WRITING.md` | `WRITING.md` (root) — generated from drafting brief + Canon §10/§12 + Sprach-DNA | tokens the hooks and lints read |
| `CURRENT_TASK.md` | `.claude/CURRENT_TASK.md` (git-ignored) | unchanged |
| `tools/research-tool.py` | `scripts/research-tool.py` | repo keeps tools in `scripts/` |
| civilization derivation chain | Kernwelt derivation chain (`/kp-world`) | planet→biology becomes Ebene→Logik-Regime→DKT→Sensorik→Bewohner→Ordnung→Register→Geschichte |

## What was vendored and how it was adapted

**Hooks** (`.claude/hooks/`, wired in `.claude/settings.json`; all warn-only, exit 0):

| Hook | Event | Adaptation |
|---|---|---|
| `bootstrap.md` | SessionStart | rewritten: source hierarchy, project skills first, codex commands, deterministic tools, engine ritual, Rule 0 |
| `post-compact-restore.sh` | SessionStart | restores `CURRENT_TASK.md`; additionally reports stale `Codex/` views |
| `skill-eval.md` | UserPromptSubmit | routing table: project skills win over generic codex skills |
| `anti-deferral.sh` | PreToolUse (Write/Edit/MultiEdit) | German deferral patterns added; `[L]` markers and the diegetic word "Platzhalter" are not flagged; graph/JSON/Codex paths skipped |
| `post-tool-use.sh` | PostToolUse (Write/Edit/MultiEdit) | chapter files → `scripts/lint_chapter.py --hook`; Codex/ → "generated" warning; Canon/ and ncp*.json → discipline reminders |
| `pre-compact.md` | PreCompact | session-state template for novel work (engine ids, knowledge fence, D-xx decisions) |

**Commands** (`.claude/commands/`, file names kept for upstream diffing): `/ingest`,
`/query`, `/lint-wiki`, `/full-audit-canon`, `/civilization-build` — each rewritten against
the repo (graph verbs, `Plan/ingest` manifests, `Codex/` re-render, decision logs, the four
audit scopes `physics | canon | continuity | storyform`).

**Agents** (`.claude/agents/`, `memory: project`): `worldbuilder-editor` (R-rules, Sprach-DNA,
enrichment discipline), `worldbuilder-physicist` (DKT substrate), `worldbuilder-researcher`
(read-only corpus lookup). Memory files under `.claude/agent-memory/` are seeded with
project facts (entity index, lock locations, search patterns, known gaps).

**Skills** (`.claude/skills/`, 19 vendored next to the 9 project skills): upstream bodies kept;
each carries a "Kohärenz Protokoll adaptation" note after its frontmatter, and the ones with
repo-structure assumptions were edited in place — `auditing-canon` (checks), `writing-worldbuilding`
(codex entries via verbs), `verifying-completion` (checklist), `researching-papers` (paths),
`planning-worldbuilding`, `interrogating-design` (layer order, record locations),
`compiling-entities`, `cross-checking`, `extracting-entities`, `deep-reading`.
The shared `references/writing-standards.md` copies point at `WRITING.md`.

**Scripts:**

- `scripts/lint_chapter.py` — decidable prose lint (frontmatter/status enum, Act-I fences
  for AEGIS/DKT/Juna/Kael, R-3 vocabulary as WARN, voice labels, R-5 heat polarity per scene,
  R-9 literal Kap-0 quote, "ich erinnere mich nicht", AEGIS "Ich" in logs, deferral markers).
  Calibrated against chapters 0–40: clean. Exit 1 on VIOLATION; `--hook` always exits 0.
- `scripts/render_codex_views.py` — renders `Codex/*.md` from the graph read-only;
  `--check` exits 1 when stale (used by the session-start hook).
- `scripts/research-tool.py` — upstream tool; default dir `Plan/research/`
  (`RESEARCH_TOOL_DIR` overrides), contact via `RESEARCH_TOOL_EMAIL`.

**settings.json:** the existing plugin/marketplace block is unchanged; hooks and a read-only
permission allow-list were added. The upstream deny-list on `.claude/skills/**`, `agents/**`,
`hooks/**` was **not** adopted — this repo's skills README expects sessions to maintain
`PROJECT_REFERENCES.md` and the skills. Only the three generated `Codex/` views are
write-denied (edit the graph and re-render instead).

## Decisions taken without the author (flag if wrong)

1. No write-deny on `Canon/` (git history shows legitimate repairs and imports); the
   post-write hook warns instead.
2. `Codex/` views are committed (like `.agency/session.db`) so clones without the engine can
   still read the glossary; regenerate after any graph write.
3. Ghost-entity detection in `/lint-wiki` is LLM-driven, not scripted: German capitalises every
   noun, so the upstream capitalised-word heuristic is useless here.
4. `Kael`/`Juna`/`AEGIS` fences are scoped to chapters 1–13 (drafting brief §3); R-10's
   "never a name" is applied as a lint only in Act I because Kap 30/38 name Juna by design.
5. The `civilization-build` command keeps its upstream name (slash command stability) but
   builds Kernwelten.

## Hook portability

Hooks are bash + python3, invoked as `bash .claude/hooks/*.sh` / `cat …` (upstream form). On
Windows (the author's Desktop-app setup per Plan/sessions/2026-09-11-learnings.md) they need
Git Bash and `python3` on PATH; if either is missing the hook fails loudly but never blocks a
write (Claude Code treats a non-zero non-2 exit as a warning). The lint and render scripts run
anywhere Python 3.11+ exists; no third-party packages.

## Keeping in sync with upstream

```bash
git clone --depth 1 https://github.com/alainator/worldcodex /tmp/wbc
# compare a vendored file against upstream (project adaptations show as our hunks)
diff -u /tmp/wbc/.claude/skills/canon-rules/SKILL.md .claude/skills/canon-rules/SKILL.md
diff -u /tmp/wbc/tools/research-tool.py scripts/research-tool.py
```

Port upstream changes hunk by hunk; re-apply the adaptation notes; update the commit hash at
the top of this file. Files that were rewritten rather than patched (hooks, commands, agents,
`auditing-canon`, `writing-worldbuilding`, `verifying-completion`) are compared for ideas,
not merged.

## Daily loop (where the suite plugs into the existing workflow)

1. Session start: bootstrap + `CURRENT_TASK.md` restore + stale-Codex check (automatic).
2. Before prose: `/query` or `/compiling-entities` for context; `match_codex_entries` for canon injection.
3. Draft per `novel-architect-scene` + drafting brief; every write is anti-deferral-checked and
   chapter-linted (automatic).
4. Before declaring done: `/verifying-completion` (lint, enrichment check, Codex freshness,
   decision-log entries).
5. New source material: `/ingest` → manifest → `scripts/ingest_canon.py` → re-render `Codex/`.
6. Milestones: `/lint-wiki all`, `/full-audit-canon <scope>`, then the composite gates
   (`developmental_gate`, `line_gate`, …). Status flips additionally pass the repo's
   lit-critic gate (`scripts/lit_critic_gate.py`, skill `lit-critic`) — the codex lint is
   the deterministic pre-check, lit-critic the editorial LLM pass.
