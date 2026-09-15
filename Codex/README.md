# Codex/ — generated views of the provenance graph

These files are **rendered** from `.agency/session.db` by
`python3 scripts/render_codex_views.py` and are write-protected in
`.claude/settings.json`. Do not edit them by hand: change the graph through
capability verbs (`create_codex_entry`, `update_codex_entry`,
`record_story_event`, `create_world_axiom`, …) and re-render.

| File | Source nodes | Purpose |
|---|---|---|
| `GLOSSARY.md` | CodexEntry (602) | terms, rules, motifs, voices, locations — slug, triggers, first paragraph |
| `MASTER-TIMELINE.md` | StoryTimeEvent (56) + HAPPENS_AT / REVEALED_IN | story-time chronology, bucketed by phase |
| `WORLD-AXIOMS.md` | WorldAxiom (111) + World (7) | hard/soft rules per Kernwelt / Ebene |

`python3 scripts/render_codex_views.py --check` exits 1 when the views lag
the graph (the session-start hook reports this). Normative on conflict is
always `Canon/`, specifically `kohaerenz-protokoll_storyform-und-outline_2026-06-10.md`.
Background: `docs/worldcodex-integration.md`.
