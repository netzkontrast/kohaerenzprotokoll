Kohärenz Protokoll — German hard-SF novel. Canon prose is German and is never
translated; engineering and work language is English.

SOURCE HIERARCHY (never invert it):
  Manuscript prose > Plan/drafting arcs + decision logs > Canon/ (storyform-und-outline
  wins on conflict) > NCP files > Codex/ generated views > repository history.
  Provenance markers: [K] kanonisch · [V] Vorschlag · [S] Steinbruch · [L] Lücke.

THE FOUR LAYERS:
  Sources/    raw exported research, immutable, manifest-tracked
  Wiki/       LLM-drafted, human-promoted knowledge pages
  Graph/      the novel's facts as plain JSONL — codex, axioms, chapters, claims
  Canon/      author-locked normative prose
  Manuscript/ the book itself, and the source of truth for prose

SKILLS (4 — .claude/skills/):
  novel-architect   whole novel: arcs, characters, scenes, structure, worlds
                    (routes to reference/{character,scene,structure,world,legacy}.md)
  dramatica         storyform reasoning and exact Dramatica vocabulary
  ncp-author        keeps manuscript, storyform and the NCP A/B files aligned
  lit-critic        editorial review of chapter prose
  Shared data map: .claude/skills/PROJECT_REFERENCES.md

COMMANDS (9 — one per stage of the pipeline):
  /research-ingest  Sources/ → Wiki/candidates/ via BatchCompile
  /kp-promote       a reviewed candidate → Wiki/sources/ or Wiki/concepts/
  /kp-canon         Canon/ → Graph/, then re-render the Codex views
  /kp-world         derive a Kernwelt/level/population, land it in Graph/ → Codex/
  /kp-write         draft or revise a scene; the knowledge fences and the checks
  /kp-check         every free gate at once
  /kp-ask           a cited answer from the repository, never from memory
  /clarify          make scope, terms and assumptions explicit (before promotion)
  /tetraframe       four positions on a contested decision (before a D-xx)

AGENTS (persistent memory in .claude/agent-memory/):
  @worldbuilder-physicist (DKT / Landauer / Coheron-Erason consistency)
  @worldbuilder-editor (Sprach-DNA, R-rules, drafting-brief compliance)
  @worldbuilder-researcher (read-only lookup across Canon/Plan/Manuscript/Graph)

DETERMINISTIC TOOLS (free, no API key, no network — run before declaring done):
  python3 scripts/kp_check.py [--chapters]     — every gate below, at once
  python3 scripts/lint_chapter.py [file]       — R-rule / Act-I fence lint (also a hook)
  python3 scripts/storyform_check.py           — the decidable Dramatica rows on both NCPs
  python3 scripts/world_check.py               — world-axiom pairs worth reading together
  python3 scripts/render_codex_views.py        — Codex views from Graph/
  python3 scripts/chapter_drift.py             — where Graph/ and Manuscript/ diverge
  python3 scripts/check_enrichment.py          — prose was inserted, never altered
  python3 scripts/wiki_fts.py search "…"       — find a wiki page
  python3 scripts/research-tool.py search …    — open-access paper search
  python3 scripts/lit_critic_gate.py --chapter N — LLM editorial gate (needs ANTHROPIC_API_KEY)

REASONING PRINCIPLES (every task):
  Mechanism over association · first principles over tropes · evidence hierarchy ·
  anti-reductionism (trace through every connected Kernwelt/Anteil) · adversarial
  self-validation. Reference: docs/canon-rules/README.md.

RULE 0: never assume — on canon facts, plot, German wording, scope: AskUserQuestion.
LONG SESSIONS: keep .claude/CURRENT_TASK.md updated (pre-compact saves, post-compact restores).
Read CLAUDE.md before every task. Read the target chapter plus its neighbours before changing prose.
