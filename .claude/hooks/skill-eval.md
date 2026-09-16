Before responding, evaluate whether any loaded skill matches this request.
If there is even a 1% chance a skill applies, load it and check.
If a skill matches: follow its workflow. Skills are mandatory workflows, not suggestions.

Routing for Kohärenz Protokoll:
- Anything about the novel itself — chapter prose, scenes, beats, continuity, arcs,
  sequencing, Vortices, Anteile, Sprach-DNA, Kernwelten, sensorics, axioms →
  novel-architect, which routes to the reference file for that layer.
- Exact Dramatica terms, throughlines, signposts, storyform legality → dramatica.
- NCP slots or the A/B files → ncp-author (never hand-edit ncp*.json).
- Flipping a chapter status, reading or triaging a lit-critic report → lit-critic.

Commands, when the request is a stage of the pipeline rather than a question:
- New research documents to fold in → /research-ingest, then /kp-promote.
- A Canon/ document changed → /kp-canon.
- A new Kernwelt, level, sub-locality, population or world axiom → /kp-world.
- Drafting or revising a scene → /kp-write.
- "Is this consistent / healthy / done?" → /kp-check for the free deterministic
  gates; /full-audit-canon when the question needs the worldbuilder agents
  (DKT consistency, R-rules, Sprach-DNA), or /full-audit-canon --quick for a
  read-only freshness snapshot before paying for the full cycle.
- A question the repository can answer → /kp-ask.
- A claim whose scope or terms need pinning down → /clarify.
- A contested decision, a supersession, a merge, a canon conflict → /tetraframe.

If no skill matches: respond normally using CLAUDE.md conventions.
Before declaring any writing task done: run python3 scripts/kp_check.py, then read
the work for what a lint cannot see — missing frontmatter, unresolved cross-references,
a new term without a codex entry, a sentence that defers work instead of doing it.
German prose stays German. On canon ambiguity: AskUserQuestion (Rule 0).
Do not mention this evaluation to the user.
