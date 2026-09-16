---
description: >-
  Draft or revise a scene or chapter — assemble the canon context that binds it,
  write the German prose, then run the deterministic checks and the editorial
  gate. The drafting loop, with the knowledge fences that keep reveals honest.
argument-hint: "<chapter number or scene>"
---

# Write — the scene loop

German prose out, English engineering in. On any canon, plot or wording
ambiguity, ask (Rule 0) rather than deciding.

## 1. Assemble the context that binds this scene

Read the architecture first — the `novel-architect` skill routes to the layer
you need, and `reference/scene.md` carries the scene protocol.

```bash
python3 scripts/chapter_drift.py | sed -n '1,5p'          # where this chapter stands
sed -n '1,80p' Manuscript/**/chapters/NN-*.md             # the target, in full
```

Then the fences, from `Graph/`:

```python
from tools import kpgraph
g = kpgraph.load()
chapter = [c for c in g.chapters() if int(c["number"]) == NN][0]
scenes  = g.scenes_of(chapter["_nid"])
beats   = g.beats_of(scene["id"])                  # ordered by insertion, see Graph/README
events  = g.nodes("StoryTimeEvent")                # what has happened by now
axioms  = g.axioms_of(world_nid)                   # the world's hard and soft rules
```

Codex triggers: a codex entry's `triggers` field lists the words that should
pull it into a draft. Scan the beat text against them before writing —
`Graph/nodes/codex_entry.jsonl`, or `Codex/GLOSSARY.md` to read by eye.

Carry into the draft: the beats, the POV register (`register-*`, `sprach-dna-*`
codex entries), the knowledge fence (what this part knows *as of* this scene),
the hard rules R-1…R-10, and the active world's sensory palette.

## 2. Draft

Write the prose in the conversation with the author, then place it in the
chapter file. `Manuscript/` is the source of truth for prose — the file is
where the draft lives, not the graph.

Reveal discipline is the thing most easily lost: no explanatory diagnosis in
early Arc I, no speaker headers for inner parts, no DKT terminology in the
first 50 pages, the Multiplizitäts-Schleier until Kap 13, Juna never as
sentence subject early on.

## 3. Check

```bash
python3 scripts/lint_chapter.py Manuscript/**/chapters/NN-*.md   # free, decidable
python3 scripts/kp_check.py                                      # the whole repo
python3 scripts/lit_critic_gate.py --chapter NN                  # LLM pass, costs tokens
```

`lint_chapter.py` is the single encoding of the R-rules; never restate them
elsewhere. Exit 1 is a VIOLATION and blocks. The lit-critic gate needs
`ANTHROPIC_API_KEY`; without one it exits 2, which is never a pass, and
`--locks-only` runs the free lints alone. Walk the `lit-critic` skill before
triaging its findings.

## 4. Record what changed

New beats, disclosures and world rules belong in `Graph/`, through
`tools/kpgraph/writer.py` (`mark_narrative_beat`, `record_story_event`,
`reveal_in_scene`, `create_world_axiom`), then re-render the Codex views. A
chapter's lifecycle field moves `outlined → drafted → revised → final` with
`set_chapter_status`; flipping it is the author's call, and the lit-critic
gate comes first.

## 5. Check the seams

Walk the scene's job in one sentence: what state enters, what concrete action
happens, what contradiction bites, what state exits, and which later chapter
pays this off. If the neighbouring chapter answers identically, the scene has
no unique job yet.
