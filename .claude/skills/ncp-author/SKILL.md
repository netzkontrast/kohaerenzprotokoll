---
name: ncp-author
description: Keeps Kohärenz Protokoll's manuscript, normative storyform and separate NCP A/B files aligned through mandatory drift checks and controlled, source-backed updates.
metadata:
  category: creative-writing
  source: repo
  version: "2.1.0"
  status: active
  date_updated: "2026-09-11"
---

# NCP Author — Kohärenz Protokoll

Use this skill for reading, validating, comparing or intentionally updating the project's Narrative Context Protocol files.

## Current data

- [Shared current reference map](../PROJECT_REFERENCES.md)
- [Storyform A — ncp.json](../../../Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/ncp.json)
- [Storyform B — ncp-b.json](../../../Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/ncp-b.json)
- [Dramatica transcription](../../../Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/dramatica.md)
- [Normative storyform/outline](../../../Canon/kohaerenz-protokoll_storyform-und-outline_2026-06-10.md)
- [Phase-1 MC encoding](../../../Plan/encoding/phase1-mc-a-b_2026-09-11.md)

## Rules

- After every manuscript, chapter-outline or structural planning change, perform an NCP drift check before declaring the work complete.
- Never mutate `ncp.json` or `ncp-b.json` merely because prose wording changed. Synchronize only information represented by the NCP schema and backed by an approved source status.
- If a manuscript change creates an NCP-relevant state change, update the affected NCP file in the same change set. If authorization, schema support or source status is missing, report the exact drift as a blocker instead of silently leaving the files misaligned.
- Before changing an encoded slot, identify the author-approved structural decision and its source/status.
- Preserve the deliberate A/B split; do not merge the two Storyforms into one file.
- Treat engine-invalid-but-canon-locked heterodox rows as explicit project exceptions, not invitations to rewrite canon.
- Validate engine-dependent values with the live novel/Dramatica capability when available.
- After any NCP change, run coherence validation and compare against `dramatica.md` and the normative Canon document.

## Mandatory alignment check

Run this check for every completed manuscript or planning task, even when no NCP edit appears necessary:

1. Identify changed facts that touch players, scenes, storybeats, moments, storyform slots, throughlines, dynamics or encoded chapter/signpost state.
2. Compare those facts with both `ncp.json` and `ncp-b.json`; preserve the deliberate A/B ownership of each value.
3. Classify the result:
   - **Aligned:** no encoded value changed; record no NCP mutation.
   - **Sync required:** an approved `[K]` value or explicitly authorized `[V]` encoding changed; update NCP in the same branch/PR.
   - **Blocked drift:** the manuscript implies a structural change without sufficient approval, schema support or provenance; stop completion and name the exact unresolved slot and source.
4. Validate changed JSON, then compare NCP, `dramatica.md`, normative Canon and the affected manuscript passage bidirectionally.

Alignment is semantic, not textual. NCP does not mirror prose sentences or speculative BeatCards; it encodes supported narrative state. An empty NCP collection is not evidence of alignment when the manuscript contains approved entities of that collection.

## Change protocol

1. Name exact file and JSON slot.
2. Cite current value and source.
3. Explain why the current value is wrong/outdated.
4. State proposed value and whether it is `[K]` or `[V]`.
5. Validate schema/coherence.
6. Update `dramatica.md` only if the human-readable transcription truly changed.
7. Record the decision in the relevant planning/decision log.
8. In the completion report, state whether the result was **Aligned**, **Sync required**, or **Blocked drift**, and list the NCP files changed or deliberately unchanged.

If the task is only to understand story structure, use `dramatica-theory`; this skill is for encoded state.
