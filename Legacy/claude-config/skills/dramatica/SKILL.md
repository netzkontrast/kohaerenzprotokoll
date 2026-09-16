---
name: dramatica
description: Dramatica reasoning and exact vocabulary for the deliberate dual Storyform of Kohärenz Protokoll — throughlines, dynamics, signposts, Crucial Element, Symptom/Response, outcome/judgment, structural legality, and the discipline that separates a structural term from its surface story expression. Use when analysing or encoding the storyform, or when terminology must be exact.
---

# Dramatica — Kohärenz Protokoll

Two jobs in one skill: reasoning about the storyform, and naming its parts
exactly. They share the same sources and the same authority markers.

## Current project data

- [Shared current reference map](../PROJECT_REFERENCES.md)
- [Normative storyform + outline](../../../Canon/kohaerenz-protokoll_storyform-und-outline_2026-06-10.md)
- [Current Dramatica transcription](../../../Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/dramatica.md)
- [Storyform A NCP](../../../Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/ncp.json)
- [Storyform B NCP](../../../Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/ncp-b.json)
- [Phase-1 MC encoding work](../../../Plan/encoding/phase1-mc-a-b_2026-09-11.md)

## Project-specific stance

This novel intentionally uses **two simultaneous Storyforms**. Do not 'repair'
that heterodox design into a single orthodox Dramatica form. Storyform A tracks
Kael/K₁ and Storyform B tracks AEGIS/K₀. The architecture deliberately rotates
interpretation at Vortex 1.

## Authority and validation

- `[K]` = locked project canon. `[V]` = proposal that still needs checking.
- NCP JSON is encoded state, not permission to silently rewrite canon prose.
- When `dramatica.md`, NCP and Canon disagree, identify the discrepancy
  explicitly. Do not auto-normalize it.
- Element-level legality, dynamic pairs, signpost orders and the two
  vocabularies are decidable. Check them rather than recalling them:

```bash
python3 scripts/storyform_check.py                 # both NCP files, all rows
python3 scripts/storyform_check.py --ncp ncp-b.json --json
```

  The checker is `tools/kpstoryform`, reading the vendored NCP v1.3.0 schema
  (463 canonical appreciations, 144 narrative functions). Storyform B's two
  documented heterodox rows are Canon-Lock: the checker reports them, and they
  are never "fixed".
- Mark conclusions the checker cannot settle `[V]`/`[Prüfen]` rather than
  declaring them canonical.

## Analysis workflow

1. Name the Storyform (A or B) and throughline being analysed.
2. Pull the exact canonical slots from the storyform document/NCP.
3. Separate structural term from surface story expression.
4. Check whether the proposed chapter event expresses the point through
   action/behaviour rather than terminology.
5. Check cross-storyform interference: the same event may read differently in
   A and B without being contradictory.
6. Preserve B's steadfast/action/timelock logic until its failure at 35/36;
   preserve A's change/decision/optionlock logic through the same event.

## Vocabulary discipline

- Use the exact project term when discussing structure.
- Distinguish **structural element** from **surface-language synonym**. A
  character may seek more order in prose without that meaning the Dramatica
  element `Control`.
- Do not invent or translate element names ad hoc.
- Preserve the project labels A (Kael/K₁) and B (AEGIS/K₀) in analytical notes
  to prevent cross-storyform contamination.

When resolving a terminology question, report:

`Storyform → Throughline → level/slot → exact term → story expression → source path/status [K|V]`

## Never

- Treat AEGIS's B-Failure as proof that AEGIS was evil.
- Conflate mode boundaries 13/14 or 26/27 with the actual B→A Storyform turn.
- Convert abstract Dramatica vocabulary directly into expositional prose, or
  use it as dialogue because it appears in a planning document.
