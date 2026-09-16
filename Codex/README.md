# Codex/ — generated views of the provenance graph

These files are **rendered** from `Graph/` by
`python3 scripts/render_codex_views.py` and are write-protected in
`.claude/settings.json`. Do not edit them by hand: change the record in
`Graph/nodes/*.jsonl` — by hand, or through `tools/kpgraph/writer.py`
(`create_codex_entry`, `create_world_axiom`, `record_story_event`, …) — and
re-render. A new level or population is derived through `/kp-world`, which
ends by writing those records.

| File | Source nodes | Purpose |
|---|---|---|
| `GLOSSARY.md` | CodexEntry (602) | terms, rules, motifs, voices, locations — slug, triggers, first paragraph |
| `MASTER-TIMELINE.md` | StoryTimeEvent (56) + HAPPENS_AT / REVEALED_IN | story-time chronology, bucketed by phase |
| `WORLD-AXIOMS.md` | WorldAxiom (111) + World (7) | hard/soft rules per Kernwelt / Ebene |

`python3 scripts/render_codex_views.py --check` exits 1 when the views lag
the graph (the session-start hook reports this), and
`python3 scripts/world_check.py` reports axiom pairs worth reading together.
Both run inside `python3 scripts/kp_check.py`. Normative on conflict is always
`Canon/`, specifically `kohaerenz-protokoll_storyform-und-outline_2026-06-10.md`.
Layout of the source records: `Graph/README.md`. Provenance of this layer:
`docs/worldcodex-integration.md`.
