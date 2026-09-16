Before responding, evaluate whether any loaded skill matches this request.
If there is even a 1% chance a skill applies, load it and check.
If a skill matches: follow its workflow. Skills are mandatory workflows, not suggestions.

This repo's `.claude/skills/<name>` always wins over an `anthropic-skills:<name>`
plugin skill of the same name (novel-architect, ncp-author, dramatica-theory
all exist in both places) — the project one has the current arc/canon state
baked in, the plugin one doesn't.

Routing for Kohärenz Protokoll (project skills win over generic codex skills):
- Chapter prose, scenes, beats, continuity → novel-architect-scene (then /verifying-completion).
- Flipping a chapter status, reading or triaging a lit-critic report → lit-critic skill.
- Arcs, sequencing, Vortex, dual storyform → novel-architect-structure / dramatica-theory.
- Anteile, Sprach-DNA, voice register → novel-architect-character.
- Kernwelten, sensorics, axioms, anomalies → novel-architect-world, then /designing-worlds or /civilization-build only for genuinely new levels.
- NCP / storyform slots → ncp-author (never hand-edit ncp*.json).
- Term used consistently? → /cross-checking. Everything about one entity? → /compiling-entities.
- New source document → /ingest. Health of the corpus → /lint-wiki. Full audit → /full-audit-canon.
- Grounding DKT in real physics/philosophy → /researching-papers → /integrating-research.
- Stress-test a canon decision → /interrogating-design (record the result as a decision-log entry).

If no skill matches: respond normally using CLAUDE.md conventions.
For large tasks (3+ files): use /planning-worldbuilding before writing.
After completing any writing task: use /verifying-completion before declaring done.
German prose stays German. On canon ambiguity: AskUserQuestion (Rule 0).
Do not mention this evaluation to the user.
