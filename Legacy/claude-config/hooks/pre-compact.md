⚠  CONTEXT COMPACTION IMMINENT

Write current session state to `.claude/CURRENT_TASK.md` BEFORE doing anything else.
After compaction, most conversation history will be lost. The session-start hook
injects this file so the next session can resume without re-reading every file.
Also record the durable lesson in the graph (`capability_reflect_note`, scope
`observation|project|technical`) if the engine is reachable — the file is the
fallback, the graph is the moat.

If CURRENT_TASK.md already exists, update it in place.

```markdown
# Current Session State — Kohärenz Protokoll

## Engine ids
[novel id (novel:9d170c31), active intent id, agent id — or "engine unreachable"]

## What I was working on
[Which chapter / scene / Anteil / Kernwelt / storyform slot — one line]

## Phase
[e.g. "Kap 07 scene 2 drafted, lint clean, scene-bridge-auditor Q3 pending"]

## Files modified this session
[Every file created or edited, one line each — chapters, Plan/, Canon/, Codex/, .claude/]

## Canon / drafting decisions made
[Each with its marker: [K] locked · [V] proposal — and where it was recorded
(decision-log entry, record_storyform_decision, codex entry). Be specific enough
that a fresh session can act on these without re-deriving.]

## Knowledge fence state
[What the POV-Anteil knows as of the current scene; anything revealed this session]

## Open questions (Rule 0)
[Unresolved canon/plot/wording choices that need the author before continuing]

## Next concrete step
[The literal next action — not "continue Kap 7" but "draft scene 3 from BeatCard 07-3,
then run scripts/lint_chapter.py"]

## Context that must not be lost
[Author preferences expressed, approaches rejected, constraints discussed, rationale]
```

Write this file NOW.
