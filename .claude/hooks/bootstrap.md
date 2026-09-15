You have the Worldbuilding-Codex suite loaded, adapted to Kohärenz Protokoll
(German hard-SF novel; canon prose is German, engineering language is English).

SOURCE HIERARCHY (never invert it):
  Manuscript prose > Plan/drafting arcs + decision logs > Canon/ (storyform-und-outline
  wins on conflict) > NCP files > Codex/ generated views > Legacy/history.
  Provenance markers: [K] kanonisch · [V] Vorschlag · [S] Steinbruch · [L] Lücke.

PROJECT SKILLS (read first for any novel work — .claude/skills/README.md):
  novel-architect, novel-architect-structure/-scene/-character/-world,
  dramatica-theory, dramatica-vocabulary, ncp-author, novel-architect-legacy.
  Shared data map: .claude/skills/PROJECT_REFERENCES.md

CODEX COMMANDS (orchestrated workflows — user types /command):
  /ingest — new source → Plan/ingest manifest → graph CodexEntries → re-rendered Codex/
  /query — answer from Canon/Plan/Manuscript/graph; file syntheses to Plan/queries/
  /lint-wiki — contradictions, stale claims, orphan docs, ghost entities
  /full-audit-canon — scope → scan → triage → fix → verify (canon | storyform | continuity | full)
  /civilization-build — Kernwelt derivation chain (Ebene → Logik-Regime → DKT → Sensorik →
                         Bewohner → Ordnung → Register → Geschichte) with hard checkpoints

CODEX SKILLS (progressive disclosure):
  AUDIT: /auditing-canon (locked spellings, frontmatter, R-rules) · /auditing-physics (DKT
         consistency) · /cross-checking (one term everywhere) · /auditing-human-assumptions
         (imported assumptions in Einheiten/Guardians/Kernwelten)
  WRITE: /writing-worldbuilding (codex entries, locations, factions — German) ·
         /writing-science (DKT substrate docs) · /writing-style (WRITING.md tokens)
  DESIGN: /designing-worlds · /designing-lore · /deriving-social-systems
  READ/EXTRACT: /deep-reading · /extracting-entities · /compiling-entities
  RESEARCH: /researching-papers (scripts/research-tool.py → Plan/research/) · /integrating-research
  PLAN/VERIFY: /interrogating-design · /planning-worldbuilding · /verifying-completion
  REFERENCE: /canon-rules (epistemology, metascience filters, adversarial protocols)

AGENTS (persistent memory in .claude/agent-memory/):
  @worldbuilder-physicist (DKT / Landauer / Coheron-Erason consistency)
  @worldbuilder-editor (Sprach-DNA, R-rules, drafting-brief compliance)
  @worldbuilder-researcher (read-only lookup across Canon/Plan/Manuscript/graph)

DETERMINISTIC TOOLS:
  python3 scripts/lint_chapter.py [file]      — R-rule / Act-I fence lint (also runs as hook)
  python3 scripts/render_codex_views.py       — Codex/GLOSSARY, MASTER-TIMELINE, WORLD-AXIOMS from graph
  python3 scripts/check_enrichment.py         — prose was only inserted, never altered
  python3 scripts/research-tool.py search …   — open-access paper search/download

ENGINE: agency graph verbs (novel.*) record provenance; prefer them over raw edits.
  Session ritual: novel.resume_session → intent_bootstrap (see CLAUDE.md §0).
  Sandbox: ≤50 call_tool per execute block, no file I/O, partial writes persist.

REASONING PRINCIPLES (every task):
  Mechanism over association · first principles over tropes · evidence hierarchy ·
  anti-reductionism (trace through every connected Kernwelt/Anteil) · adversarial self-validation.

RULE 0: never assume — on canon facts, plot, German wording, scope: AskUserQuestion.
LONG SESSIONS: keep .claude/CURRENT_TASK.md updated (pre-compact saves, post-compact restores).
Read CLAUDE.md before every task. Read the target chapter plus its neighbours before changing prose.
