---
name: dramatica-theory
description: Project-specific Dramatica reasoning for the deliberate dual Storyform of Kohärenz Protokoll, including throughlines, dynamics, signposts, story-point expression, and exact vocabulary/slot-mapping discipline (merged from the former dramatica-vocabulary skill 2026-09-16).
metadata:
  category: creative-writing
  source: repo
  version: "2.0.0"
  status: active
  date_updated: "2026-09-11"
---

# Dramatica Theory — Kohärenz Protokoll

Use this skill to reason about the project's dual Storyform, story points, dynamics, throughlines, signposts, Crucial Element, Symptom/Response, outcome/judgment, and structural legality.

## Current project data

- [Shared current reference map](../PROJECT_REFERENCES.md)
- [Normative storyform + outline](../../../Canon/kohaerenz-protokoll_storyform-und-outline_2026-06-10.md)
- [Current Dramatica transcription](../../../Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/dramatica.md)
- [Storyform A NCP](../../../Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/ncp.json)
- [Storyform B NCP](../../../Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/ncp-b.json)
- [Phase-1 MC encoding work](../../../Plan/encoding/phase1-mc-a-b_2026-09-11.md)

## Project-specific stance

This novel intentionally uses **two simultaneous Storyforms**. Do not 'repair' that heterodox design into a single orthodox Dramatica form. Storyform A tracks Kael/K₁ and Storyform B tracks AEGIS/K₀. The architecture deliberately rotates interpretation at Vortex 1.

## Authority and validation

- `[K]` = locked project canon.
- `[V]` = proposal/draft choice that may require engine validation.
- NCP JSON is encoded state, not permission to silently rewrite canon prose.
- When `dramatica.md`, NCP and Canon disagree, identify the discrepancy explicitly. Do not auto-normalize it.
- Element-level legality, dynamic pairs and signpost orders should be checked against the live Dramatica/novel engine when available; do not infer legality from memory.

## Analysis workflow

1. Name the Storyform (A or B) and throughline being analyzed.
2. Pull the exact canonical slots from the storyform document/NCP.
3. Separate structural term from surface story expression.
4. Check whether the proposed chapter event expresses the point through action/behavior rather than terminology.
5. Check cross-storyform interference: the same event may read differently in A and B without being contradictory.
6. Preserve B's steadfast/action/timelock logic until its failure at 35/36; preserve A's change/decision/optionlock logic through the same event.
7. Mark unresolved engine-dependent conclusions `[V]`/`[Prüfen]` rather than declaring them canonical.

## Never

- Treat AEGIS's B-Failure as proof that AEGIS was evil.
- Conflate mode boundaries 13/14 or 26/27 with the actual B→A Storyform turn.
- Convert abstract Dramatica vocabulary directly into expositional prose.

## Exact vocabulary discipline

Use when terminology must be exact: Domains, Concerns, Issues,
Problems/Solutions, Symptom/Response, Dynamics, Story Drivers, Limits,
Outcomes, Judgments, Signposts and Throughlines.

- Use the exact project term when discussing structure.
- Distinguish **structural element** from **surface-language synonym**.
  Example: a character may seek more order in prose without that
  automatically meaning the Dramatica element `Control`.
- Do not invent or translate element names ad hoc.
- If legality or parent/quad membership matters, query the live
  engine/ontology rather than relying on remembered theory.
- Preserve project labels A (Kael/K₁) and B (AEGIS/K₀) in analytical notes
  to prevent cross-storyform contamination.

Output pattern when resolving a terminology question:

`Storyform → Throughline → level/slot → exact term → story expression → source path/status [K|V]`.

Never use Dramatica vocabulary as dialogue or naked exposition merely
because it appears in planning documents.
