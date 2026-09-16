# Codex/ — generated views of the provenance graph

Every file here is **rendered** from `Graph/` by
`python3 scripts/render_codex_views.py` and is write-protected in
`.claude/settings.json`. Do not edit one by hand: change the record in
`Graph/nodes/*.jsonl` — directly, or through `tools/kpgraph/writer.py`
(`create_codex_entry`, `create_world_axiom`, `record_story_event`, …) — and
re-render. A new level or population is derived through `/kp-world`, which ends
by writing those records.

## One convention

```
Codex/<VIEW>.md              navigation only — counts and links, never a body
Codex/<view>/README.md       the rendered index of that view, one row per file
Codex/<view>/<slug>.md       one retrievable unit
```

| Router | Content | Source nodes | One file is |
|---|---|---|---|
| `GLOSSARY.md` | `entries/<category>/` | CodexEntry (602) | one entry — body, triggers, the chapters it is in play in |
| `WORLD-AXIOMS.md` | `axioms/<world-slug>.md` | WorldAxiom (111) + World (7) | one world's complete hard/soft rule set |
| `MASTER-TIMELINE.md` | `timeline/<phase-slug>.md` | StoryTimeEvent (56) + HAPPENS_AT / REVEALED_IN | one story phase |

A "retrievable unit" is whatever a reader asks for in one go. Nobody fetches a
single axiom, so a world is the unit there; everybody fetches a single codex
entry, so an entry is the unit there.

The partition dimension for entries is the `**Kategorie:**` each record already
carries — 22 of them, declared in `Graph/schema.yaml`. Nothing is invented: a
record whose category is not declared renders into `entries/_misfiled/`, which
makes the drift visible instead of silently creating a directory. That folder
being empty is the healthy state.

## Retrieval

```bash
python3 scripts/context_packet.py --chapter 3           # the smallest sufficient packet
python3 scripts/context_packet.py --chapter 3 --paths   # just the files to open
python3 scripts/context_packet.py --chapter 3 --json    # tiers and token cost
```

Three tiers — always-on categories, the entries whose `triggers` occur in that
chapter, and every world axiom. The chapter window is computed on each run from
`triggers` rather than stored, so it cannot go stale and it sharpens as
chapters are written. Membership implies the entry was already in play at or
before that chapter, which is what makes the packet spoiler-safe. The rules,
and the per-entry spoiler ceiling that is not implemented yet, are in
`Graph/schema.yaml`.

Roughly 21,700 tokens for chapter 3, against ~84,400 for every codex body.

## Checks

`python3 scripts/render_codex_views.py --check` exits 1 when a rendered file
lags the graph or when a file survives that the renderer no longer produces
(the session-start hook reports this). `python3 scripts/world_check.py` reports
axiom pairs worth reading together. Both run inside `python3 scripts/kp_check.py`.

Normative on conflict is always `Canon/`, specifically
`kohaerenz-protokoll_storyform-und-outline_2026-06-10.md`. Layout of the source
records: `Graph/README.md`. Provenance of this layer:
`docs/worldcodex-integration.md`.
