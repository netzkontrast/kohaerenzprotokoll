# Repo-local skills — Kohärenz Protokoll

These skills are the **current project-facing replacements** for the historical `Legacy/skills/*` snapshot. They point to live repo data and are intended to be read before doing novel architecture, chapter planning, prose drafting, Dramatica analysis or NCP changes.

## Shared data map

Start with [PROJECT_REFERENCES.md](./PROJECT_REFERENCES.md). It defines current source hierarchy, work root, arc plans, canon sources, NCP files, graph-state warnings and drafting rules.

## Skills

- [novel-architect](./novel-architect/SKILL.md) — whole-novel premise, arc architecture, chapter roles, cross-arc causality.
- [novel-architect-structure](./novel-architect-structure/SKILL.md) — sequencing, dual-storyform weaving, mode changes, Vortices, option/timelock.
- [novel-architect-scene](./novel-architect-scene/SKILL.md) — scene planning, prose drafting, local continuity and reveal discipline.
- [novel-architect-character](./novel-architect-character/SKILL.md) — character/parts functions, arcs, Sprach-DNA, somatics and reveal timing.
- [novel-architect-world](./novel-architect-world/SKILL.md) — KW1–KW4, sensorics, anomaly design and world constraints.
- [dramatica-theory](./dramatica-theory/SKILL.md) — project-specific dual-Storyform reasoning.
- [dramatica-vocabulary](./dramatica-vocabulary/SKILL.md) — exact structural terminology and story-expression mapping.
- [ncp-author](./ncp-author/SKILL.md) — encoded Storyform/NCP validation and controlled mutations.
- [novel-architect-legacy](./novel-architect-legacy/SKILL.md) — historical evidence only; current-first comparison workflow.
- [lit-critic](./lit-critic/SKILL.md) — editorial prose gate: run lit-critic over a chapter, read its report, triage findings against canon.
- [wiki-maintenance](./wiki-maintenance/SKILL.md) — maintain wiki partitions, small-page boundaries, local indexes, links and schema/tool alignment without changing Canon.

## Current project state encoded in these skills

- Arc plans exist for **Kap. 1–40**.
- Current opening prose anchors: Kap. 0, 1, 2, 3 and 5; Kap. 4 is the next planned prose gap in the 1–5 block.
- Arc II motor: **access → knowledge → intervention**.
- Arc III motor: **intent → confrontation capacity → truth rotation → insufficient replacement order → plural preservation**.
- Vortex 1 = Kap. 35/36; Vortex 2 = Kap. 38/39; Kap. 40 is an ambiguous coda.
- Canon/NCP are not silently mutated by drafting work.

## Vendored Worldbuilding-Codex skills (generic, project-annotated)

From [alainator/worldcodex](https://github.com/alainator/worldcodex); each carries a "Kohärenz Protokoll adaptation" note after its frontmatter and reads `WRITING.md` + [PROJECT_REFERENCES.md](./PROJECT_REFERENCES.md). The project skills above win when both apply. Map and sync procedure: [docs/worldcodex-integration.md](../../docs/worldcodex-integration.md).

- Audit: [auditing-canon](./auditing-canon/SKILL.md), [auditing-physics](./auditing-physics/SKILL.md), [cross-checking](./cross-checking/SKILL.md), [auditing-human-assumptions](./auditing-human-assumptions/SKILL.md)
- Write: [writing-worldbuilding](./writing-worldbuilding/SKILL.md) (codex entries via verbs), [writing-science](./writing-science/SKILL.md) (DKT substrate), [writing-style](./writing-style/SKILL.md) (WRITING.md)
- Design: [designing-worlds](./designing-worlds/SKILL.md), [designing-lore](./designing-lore/SKILL.md), [deriving-social-systems](./deriving-social-systems/SKILL.md)
- Read/extract: [deep-reading](./deep-reading/SKILL.md), [extracting-entities](./extracting-entities/SKILL.md), [compiling-entities](./compiling-entities/SKILL.md)
- Research: [researching-papers](./researching-papers/SKILL.md), [integrating-research](./integrating-research/SKILL.md)
- Plan/verify: [interrogating-design](./interrogating-design/SKILL.md), [planning-worldbuilding](./planning-worldbuilding/SKILL.md), [verifying-completion](./verifying-completion/SKILL.md)
- Reference: [canon-rules](./canon-rules/SKILL.md) (epistemology, metascience filters, adversarial protocols)

## Maintenance rule

When work-level canon or planning changes materially, update **PROJECT_REFERENCES.md first**, then only the skills whose workflow assumptions changed. Do not fork a new static canon snapshot into the skill itself.
