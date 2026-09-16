# Repo-local skills — Kohärenz Protokoll

Four skills carry the craft of writing this novel. They point at live repo
data and are meant to be read before novel architecture, chapter planning,
prose drafting, Dramatica analysis or NCP changes.

## Shared data map

Start with [PROJECT_REFERENCES.md](./PROJECT_REFERENCES.md). It defines the
current source hierarchy, the work root, the arc plans, the canon sources, the
NCP files, the graph-state warnings and the drafting rules.

## Skills

- [novel-architect](./novel-architect/SKILL.md) — the whole novel. Arc
  architecture, chapter roles and cross-arc causality sit in the skill body;
  it routes to a reference file for the layer a request actually touches:
  [character](./novel-architect/reference/character.md) (parts, arcs,
  Sprach-DNA, somatics, reveal timing),
  [scene](./novel-architect/reference/scene.md) (drafting, local continuity,
  reveal discipline, sensorics),
  [structure](./novel-architect/reference/structure.md) (sequencing,
  dual-storyform weaving, mode changes, Vortices, option/timelock),
  [world](./novel-architect/reference/world.md) (KW1–KW4, anomaly design,
  world constraints),
  [legacy](./novel-architect/reference/legacy.md) (historical evidence only,
  current-first comparison).
- [dramatica](./dramatica/SKILL.md) — dual-Storyform reasoning and exact
  structural terminology, with the decidable rows runnable as
  `python3 scripts/storyform_check.py`.
- [ncp-author](./ncp-author/SKILL.md) — encoded Storyform/NCP validation and
  controlled mutations.
- [lit-critic](./lit-critic/SKILL.md) — the editorial prose gate: run
  lit-critic over a chapter, read its report, triage findings against canon.

Reasoning reference for hard cases — epistemology, metascience filters,
adversarial protocols, anti-patterns — is
[docs/canon-rules/README.md](../../docs/canon-rules/README.md). It is
reference material rather than a workflow, which is why it is a doc and not a
skill.

## Current project state encoded in these skills

- Arc plans exist for **Kap. 1–40**.
- Current opening prose anchors: Kap. 0, 1, 2, 3 and 5; Kap. 4 is the next
  planned prose gap in the 1–5 block.
- Arc II motor: **access → knowledge → intervention**.
- Arc III motor: **intent → confrontation capacity → truth rotation →
  insufficient replacement order → plural preservation**.
- Vortex 1 = Kap. 35/36; Vortex 2 = Kap. 38/39; Kap. 40 is an ambiguous coda.
- Canon and the NCP files are never silently mutated by drafting work.

## Maintenance rule

When work-level canon or planning changes materially, update
**PROJECT_REFERENCES.md first**, then only the skills whose workflow
assumptions changed. Do not fork a new static canon snapshot into a skill.
