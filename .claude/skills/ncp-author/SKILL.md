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

- Never mutate `ncp.json` or `ncp-b.json` as a side effect of prose drafting or chapter planning.
- Before changing an encoded slot, identify the author-approved structural decision and its source/status.
- Preserve the deliberate A/B split; do not merge the two Storyforms into one file.
- Treat engine-invalid-but-canon-locked heterodox rows as explicit project exceptions, not invitations to rewrite canon.
- Validate engine-dependent values with the live novel/Dramatica capability when available.
- After any NCP change, run coherence validation and compare against `dramatica.md` and the normative Canon document.

## Change protocol

1. Name exact file and JSON slot.
2. Cite current value and source.
3. Explain why the current value is wrong/outdated.
4. State proposed value and whether it is `[K]` or `[V]`.
5. Validate schema/coherence.
6. Update `dramatica.md` only if the human-readable transcription truly changed.
7. Record the decision in the relevant planning/decision log.

If the task is only to understand story structure, use `dramatica-theory`; this skill is for encoded state.
