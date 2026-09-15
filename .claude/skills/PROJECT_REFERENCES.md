# Kohärenz Protokoll — current project reference map

This file is the shared data map for all repo-local skills. **Do not use historical snapshots as authority when a current path below exists.**

## Source hierarchy

1. **Current manuscript/work files** for already-written prose and current work-level framing.
2. **Current Arc plans and drafting decision logs** for chapter intent, scene planning, transitions, and explicitly provisional `[V]` choices.
3. **Canon/** for locked world/storyform/voice constraints. On conflict inside Canon, `kohaerenz-protokoll_storyform-und-outline_2026-06-10.md` is normative unless a later current manuscript decision explicitly supersedes only a drafting detail.
4. **NCP files** for encoded storyform state; do not silently mutate them from prose work.
5. Historical/Legacy material is evidence only, never current authority.

## Work root

`Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/`

- [work.md](../../Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/work.md) — current work overview/logline and whole-novel framing.
- [premise.md](../../Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/premise.md) — current premise and dramatic engine.
- [dramatica.md](../../Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/dramatica.md) — dual-storyform transcription/working reference.
- [ncp.json](../../Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/ncp.json) — Storyform A encoded state.
- [ncp-b.json](../../Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/ncp-b.json) — Storyform B encoded state.
- [chapters/](../../Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/chapters/) — current chapter files. Written and continuity-checked prose now covers Kap. 0–5; chapter 6 is the next planned prose gap.

## Current arc planning

- [Akt I optimized arc, Kap. 1–13](../../Plan/drafting/akt1-arc-optimized_2026-09-11.md)
- [Akt II optimized arc, Kap. 14–26](../../Plan/drafting/akt2-arc-optimized_2026-09-11.md)
- [Akt III optimized arc, Kap. 27–40](../../Plan/drafting/akt3-arc-optimized_2026-09-11.md)
- [Akt I drafting decisions](../../Plan/drafting/decision-log_2026-09-11.md)
- [Akt II/III drafting decisions](../../Plan/drafting/decision-log_akt2-3_2026-09-11.md)
- [Kap. 1–5 coherence pass](../../Plan/drafting/coherence-pass_01-05_2026-09-11.md)
- [Focused enrichment packets, Kap. 1–5](../../Plan/drafting/enrichment-packets_01-05_2026-09-11.md) — normative scene, evidence, reveal and handoff matrix for the opening block.
- [Expanded chapter information, Kap. 0–40](../../Plan/drafting/chapter-information-expanded_2026-09-11.md) — operative Chapter Packets: Auftrag, Informationsverschiebung, Körper/Beziehung, Weltanker, Motive, Exit-State und Hook.
- [Akt-I BeatCards, Kap. 4–13](../../Plan/drafting/akt1-beatcards_04-13_2026-09-11.md) — scene-ready entry/action/pressure/exit cards, Hook chain, knowledge fences and motif transitions for the remaining Act-I drafting range.
- [Shared drafting brief](../../Plan/drafting/drafting-brief.md)

## Canon data

- [Storyform + outline](../../Canon/kohaerenz-protokoll_storyform-und-outline_2026-06-10.md) — normative structural canon.
- [Character/parts profiles + Sprach-DNA](../../Canon/kohaerenz-protokoll_anteile-profile-sprach-dna_2026-06-10.md) — voice, somatics, arcs, switching rules.
- [World + sensorics + drafting discipline](../../Canon/kohaerenz-protokoll_welt-sensorik-drafting_2026-06-10.md) — worlds, sensory polarity, reveal discipline, drafting locks.
- [Core worlds](../../Canon/kohaerenz-protokoll_kernwelten-vollstaendig_2026-06-10.md) — KW1–KW4/world architecture.
- [Terms + concepts](../../Canon/kohaerenz-protokoll_begriffe-und-konzepte_2026-06-10.md) — controlled vocabulary and conceptual definitions.
- [Philosophy in detail](../../Canon/kohaerenz-protokoll_philosophie-im-detail_2026-06-10.md) — theoretical substrate; never dump theory directly into prose.
- [Kap. 0 annotated source](../../Canon/kap0-v1-annotiert.md) — Genesis reference and revision evidence.

## Agency / graph state

- [.agency/novel-config.yaml](../../.agency/novel-config.yaml) — materialization/configuration.
- [.agency/session.db](../../.agency/session.db) — provenance graph. **Graph state may lag disk prose.** Never run materialization over newer chapter prose unless the graph has first been synchronized.
- [CLAUDE.md](../../CLAUDE.md) — current agency/novel capability workflow and engine constraints.

## Quality gates

Run in this order before a chapter advances (`drafted` → `revised` → `final`):

1. [scripts/check_enrichment.py](../../scripts/check_enrichment.py) — an enrichment pass may only insert prose, never rewrite it.
2. Readiness Gate — [chapter-enrichment-masterplan](../../Plan/drafting/chapter-enrichment-masterplan_2026-09-11.md) §F.
3. [scripts/lit_critic_gate.py](../../scripts/lit_critic_gate.py) — kapitelgenaue Canon-Locks ([lit_critic_locks.py](../../scripts/lit_critic_locks.py), lexikalisch, kostenlos, `--locks-only`) und lit-critic's seven editorial lenses against [tools/lit-critic/CANON.md](../../tools/lit-critic/CANON.md) and [STYLE.md](../../tools/lit-critic/STYLE.md). Reports land in [Plan/quality/lit-critic/](../../Plan/quality/lit-critic/). Only `critical` findings block; the `horizon` lens never does. See the [lit-critic skill](./lit-critic/SKILL.md).
4. Agency editorial ladder (`novel.line_gate`, `novel.copy_gate`, …) for graph-recorded provenance.

lit-critic's inputs are **compilations** of `Canon/` and the drafting brief, not a
second canon: change the source under `Canon/` first, then pull the change through.

## Mandatory operating rules

- Read the target chapter plus its previous and next chapter before changing prose or outline.
- For Arc work, read the full corresponding optimized arc plan first.
- Existing prose beats abstract theory when they conflict on telling details; report the conflict rather than silently rewriting canon.
- Preserve `[K]` locked decisions. Treat `[V]` as reviewable drafting choices.
- No new lore merely to repair a continuity problem if an existing source already resolves it.
- German manuscript prose stays German.
