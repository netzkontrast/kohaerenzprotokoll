---
name: novel-architect
description: The whole authoring surface for Kohärenz Protokoll — arc architecture and chapter roles, the plural character system and Sprach-DNA, scene drafting and reveal discipline, structural sequencing and the Vortices, worldbuilding and sensorics. Use for any planning, drafting or revision of the novel itself; it routes to the reference file for the layer you are working in.
---

# Novel Architect — Kohärenz Protokoll

One skill for the whole novel. Start here, then open the reference file for the
layer the request actually touches. The locks below hold across every layer.

| the request is about | open |
|---|---|
| Kael's parts, arcs, Sprach-DNA, somatics, reveal timing | [reference/character.md](reference/character.md) |
| drafting or revising a scene, local causality, sensorics | [reference/scene.md](reference/scene.md) |
| sequencing, dual-storyform weaving, Vortices, setup/payoff | [reference/structure.md](reference/structure.md) |
| KW1–KW4, levels, axioms, anomaly design | [reference/world.md](reference/world.md) |
| older drafts, removed snapshots, recovering intent | [reference/legacy.md](reference/legacy.md) |

Exact Dramatica vocabulary and storyform slots are the `dramatica` skill.
NCP A/B alignment is `ncp-author`. Prose review is `lit-critic`.

## Read first

- [Shared current reference map](../PROJECT_REFERENCES.md)
- [Current work overview](../../../Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/work.md)
- [Current premise](../../../Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/premise.md)
- [Normative storyform/outline canon](../../../Canon/kohaerenz-protokoll_storyform-und-outline_2026-06-10.md)
- [Akt I plan](../../../Plan/drafting/akt1-arc-optimized_2026-09-11.md) ·
  [Akt II plan](../../../Plan/drafting/akt2-arc-optimized_2026-09-11.md) ·
  [Akt III plan](../../../Plan/drafting/akt3-arc-optimized_2026-09-11.md)

## Current architecture

- **Arc I, Kap. 1–13:** anomaly → system contradiction → counter-register → loss of evidentiary certainty → loss/relationship → conscious plurality → internal practice.
- **Arc II, Kap. 14–26:** **access → knowledge → intervention**. Z1 epistemic, Z2 personal, Z3 ontological/generative; 24–26 convert covert preservation into non-compliance and role loss.
- **Arc III, Kap. 27–40:** **intent → confrontation capacity → truth rotation → insufficient replacement order → plural preservation**. 35/36 are the operative storyform turn; 37 is a real but non-scalable false victory; 38/39 are synthesis; 40 is coda, not explanation.

## Workflow

1. Establish which arc and chapter range the request touches.
2. Read the full optimized arc plan, not only the target chapter.
3. Read existing prose anchors on both sides of the range.
4. State the chapter/scene's unique dramaturgical job in one sentence.
5. Check that it changes state, not merely adds lore or theory.
6. Check cause/effect into the next chapter and backwards payoff from later chapters.
7. Preserve the distinction between Vortex 1 (truth rotation) and Vortex 2 (synthesis).
8. Log any new non-canonical choice as `[V]`; do not silently promote it to canon.

## Locks that hold everywhere

- AEGIS is tragically innocent, not malicious — never a villain.
- Resolution is **functional multiplicity, never fusion**; no eliminated parts.
- Juna is a cosmological constant/witness function, not merely a love interest.
- Theory stays submerged: the reader meets mechanisms through work, objects,
  timing, space, body, logs and omission, never through exposition.
- Kap. 27–34 do not consume the climax reserved for 35/36; Kap. 37 does not
  solve the novel; Kap. 40 does not adjudicate Reset vs. Transfiguration.
- German prose out, English engineering in. On any canon ambiguity, ask
  (Rule 0) rather than deciding.

## Before declaring a piece of work finished

Run the deterministic checks — they are free and they are the repo's memory:

```bash
python3 scripts/lint_chapter.py <chapter.md>   # R-rules + Act-I fences
python3 scripts/kp_check.py                    # every free gate at once
```

Then confirm, by reading rather than by assertion: frontmatter is complete,
every cross-reference resolves, every new term has a codex entry in
`Graph/nodes/codex_entry.jsonl`, and no sentence defers work instead of doing
it. A lint proves a forbidden word is absent; it can never show that something
required is missing, so the reading still has to happen.
