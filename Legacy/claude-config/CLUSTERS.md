# Worldbuilding-Codex cluster map

One table of everything the vendored [worldcodex](https://github.com/alainator/worldcodex)
suite (skills, tools, agents, hooks) plus this repo's own project skills and
commands add up to, grouped by the job you're actually doing rather than by
where the files live. Full vendoring rationale and file-by-file mapping:
[docs/worldcodex-integration.md](../docs/worldcodex-integration.md). Skill
list with routing notes: [.claude/skills/README.md](skills/README.md).

Two of the commands below have a `--quick` mode — reach for it first when
you just need a snapshot, not a full audit:

- **`/full-audit-canon --quick`** — one-screen freshness/health check for
  the Codex layer (graph → `Codex/*.md`, chapter lints, pending claims).
- **`/lint-wiki --quick`** — one-screen structure report for the research
  Wiki (`Wiki/**`): page counts by kind/partition, schema contract summary,
  lint health, view freshness.

Quick mode writes nothing — it's a read-only snapshot you run before
deciding whether the full cycle (scope/triage/fix for `/full-audit-canon`,
the semantic corpus review for `/lint-wiki`) is worth the cost.

## Codex (graph-backed worldbuilding entries)

The provenance graph (`.agency/session.db`) is the source of truth;
`Codex/*.md` are generated views. This cluster creates, checks and
audits CodexEntries, WorldAxioms, StoryTimeEvents.

| kind | name | purpose |
|---|---|---|
| command | `/ingest` | source → extraction manifest → graph verbs → re-render `Codex/` |
| command | `/full-audit-canon` | scope → scan → triage → fix → verify, orchestrates the two agents below; `--quick` for a freshness + pending-claims snapshot only |
| skill | `writing-worldbuilding` | new codex entries (civilizations, locations, factions) via verbs |
| skill | `auditing-canon` | locked spellings, frontmatter, R-rules |
| skill | `auditing-physics` | DKT / axiom cross-layer consistency |
| skill | `cross-checking` | one term, everywhere |
| skill | `auditing-human-assumptions` | imported vs. derived assumptions |
| skill | `compiling-entities` / `extracting-entities` | assemble or split entity content |
| skill | `canon-rules` | epistemology + adversarial-review reference, no execution |
| tool | `scripts/render_codex_views.py` | render `GLOSSARY.md` / `MASTER-TIMELINE.md` / `WORLD-AXIOMS.md` from the graph |
| tool | `scripts/lint_chapter.py` | decidable R-rule / Act-I fence lint |
| tool | `scripts/check_enrichment.py` | an enrichment pass only inserts prose |
| agent | `@worldbuilder-physicist` | DKT/Landauer/Coheron-Erason consistency |
| agent | `@worldbuilder-editor` | R-rules, Sprach-DNA, enrichment discipline |

## Prose (drafting and editorial gates)

| kind | name | purpose |
|---|---|---|
| skill | `novel-architect-scene` | scene planning, drafting, local continuity, reveal discipline |
| skill | `novel-architect-character` | Anteile, Sprach-DNA, somatics, reveal timing |
| skill | `novel-architect-structure` | sequencing, dual-storyform weaving, Vortices |
| skill | `novel-architect-world` | KW1–4, sensorics, anomaly design |
| skill | `dramatica-theory` | dual-storyform reasoning + exact vocabulary/slot-mapping discipline |
| skill | `ncp-author` | encoded Storyform/NCP validation and controlled mutation |
| skill | `lit-critic` | editorial prose gate (chapter lints + seven editorial lenses) |
| skill | `writing-style` | `WRITING.md` prose tokens |
| skill | `writing-science` | DKT substrate documents |
| skill | `verifying-completion` | pre-done checklist (lint, enrichment, Codex freshness, decision log) |
| tool | `scripts/lit_critic_gate.py` | run the lit-critic gate for a chapter |
| tool | `agency` (`novel.*` verbs) | editorial gate ladder: `pre_draft_gate` → … → `publication_gate` |
| agent | `@worldbuilder-editor` | prose-quality review |

## Wiki (research layer — `Wiki/**`)

The three-layer knowledge system (`Sources/` → `Wiki/` → `Canon/` + graph).
This cluster is the one the upstream worldcodex suite doesn't cover on its
own — it was built repo-side (`Wiki/SCHEMA.md`, `tools/kpwiki/`) to give the
research layer the same discipline the Codex cluster gives canon.

| kind | name | purpose |
|---|---|---|
| command | `/research-ingest` | batch of exported sources → candidate wiki pages (`BatchCompile`) |
| command | `/lint-wiki` | contradictions, stale claims, orphans, ghost entities across the whole corpus; `--quick` for a structure/health snapshot only |
| skill | `wiki-maintenance` | moves, splits, navigation repair, schema evolution for `Wiki/**` |
| command | `/clarify` | precision gate — makes scope/terms/assumptions explicit before a promotion |
| command | `/tetraframe` | mandatory before a contested decision (D-xx, merge/supersede/delete) |
| tool | `tools/kpwiki/research_ingest_cli.py` (`BatchCompile`) | the DSPy program behind `/research-ingest` |
| tool | `tools/kpwiki/clarify.py` / `clarify_cli.py` | the DSPy program behind `/clarify` |
| tool | `tools/kpwiki/tetraframe.py` / `tetraframe_cli.py` | the DSPy program behind `/tetraframe` |
| tool | `scripts/wiki_lint.py` | deterministic Wiki lint (`--health`, `--fix`, `--suggest`) |
| tool | `scripts/render_wiki_views.py` | render `index.md`, `concept-table.md`, `context-map.md`, `README.md`s |
| tool | `scripts/wiki_fts.py` | candidate finder (full-text search over `Wiki/`) |
| tool | `tools/kpwiki/wiki_schema.py` | loads `Wiki/schema/*.yaml` as the runtime contract |
| reference | `Wiki/SCHEMA.md` + `Wiki/schema/*.yaml` | the four page entities, required fields, enums, ownership zones |

## Research (real-world grounding)

| kind | name | purpose |
|---|---|---|
| skill | `researching-papers` | arXiv/Crossref/PMC/Semantic Scholar/Open Library/SEP search + download |
| skill | `integrating-research` | map a paper onto DKT formalism |
| skill | `deep-reading` | structured content map of one source before use |
| tool | `scripts/research-tool.py` | the search/download/convert CLI behind `researching-papers` |

## Design / planning (new content before it's canon)

| kind | name | purpose |
|---|---|---|
| command | `/civilization-build` | Kernwelt derivation chain, hard checkpoints, orchestrates the skills below |
| skill | `designing-worlds` | physical world foundations |
| skill | `designing-lore` | myths, legends, relics |
| skill | `deriving-social-systems` | biology/cognition/environment → coordination structures |
| skill | `interrogating-design` | stress-test a proposal before it's written |
| skill | `planning-worldbuilding` | decompose a &gt;3-file task into a sequenced plan |
| skill | `novel-architect` / `novel-architect-legacy` | whole-novel architecture; historical-evidence comparison |

## Hooks (always-on, warn-only)

`SessionStart` → `bootstrap.md` + `post-compact-restore.sh` · `UserPromptSubmit`
→ `skill-eval.md` (skill routing) · `PreToolUse` (Write/Edit) → `anti-deferral.sh`
· `PostToolUse` (Write/Edit) → `post-tool-use.sh` (chapter lint, Codex/Canon
discipline warnings) · `PreCompact` → `pre-compact.md` (session-state save).
None of these block a write; they warn.

## Maintenance

This map is hand-maintained, not generated. When a skill, command, tool or
agent is added, removed or reclassified, update the row here in the same
change — do not let it drift from `.claude/skills/README.md` or
`docs/worldcodex-integration.md`.
