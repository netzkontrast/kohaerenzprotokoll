# Context-efficient manuscript loading

The goal is the smallest sufficient, spoiler-safe context packet for a
specific writing decision.

## Where the knowledge actually is

Read this before following the ladder, because it decides which rung you start
on. Two layers hold two different things, and they are not interchangeable:

| layer | holds | routes by |
|---|---|---|
| `Wiki/` | the *research understanding*, promoted by the author | `Wiki/context-map.md` — chapter window, spoiler ceiling, tier |
| `Codex/` | the *novel's own facts* — 602 entries, 111 axioms, 56 events | `Graph/schema.yaml` — category partition, computed chapter window |

`Wiki/context-map.md` is the right instrument and currently has no rows,
because no page has been promoted yet. The knowledge a chapter needs is in
`Codex/`, which is a rendered view of `Graph/` and is partitioned so it can be
retrieved programmatically rather than read whole.

## Start with the packet

```bash
python3 scripts/context_packet.py --chapter 3           # the packet itself
python3 scripts/context_packet.py --chapter 3 --paths   # just the files to open
python3 scripts/context_packet.py --chapter 3 --json    # tiers and cost, machine-readable
```

Three tiers, all of them derived from fields the records already carry — no
curated list, nothing to maintain by hand:

- **always-on** — the categories that constrain prose without ever appearing in
  it: `rule`, `guidance`, `voice`, `defect`, `theme`, `philosophy`. A trigger
  scan can never surface these, so they are selected by category. Rendered as
  40-word cards; `--full` gives the bodies.
- **chapter-anchored** — every entry whose `triggers` occur in that chapter's
  prose, in full, because this is what the chapter is about.
- **world axioms** — all of them. They are short and none is chapter-local.

Everything else is on-demand: reached by name through the tree below, or by
`python3 scripts/wiki_fts.py search "…"`.

## Navigating by hand

Each root file in `Codex/` is navigation only — counts and links, no bodies.
One convention throughout:

```
Codex/GLOSSARY.md              →  Codex/entries/<category>/<slug>.md
Codex/WORLD-AXIOMS.md          →  Codex/axioms/<world-slug>.md
Codex/MASTER-TIMELINE.md       →  Codex/timeline/<phase-slug>.md
```

Every directory carries a rendered `README.md` listing what is in it with a
40-word summary per row, so you can choose an entry without opening one. A file
is one retrievable unit: an entry for the codex, a whole world's rule set for
the axioms, a story phase for the timeline. Opening
`Codex/entries/rule/README.md` costs a fraction of the corpus and tells you
which of the 99 rules you actually need.

An entry whose `**Kategorie:**` is not in `Graph/schema.yaml` renders into
`Codex/entries/_misfiled/`. That directory existing is a defect report, not a
category — fix the record and re-render.

## What the window does and does not prove

A chapter is in an entry's window when one of the entry's triggers occurs in
that chapter's prose. Membership, never a first-to-last span: an entry that
fires in chapters 3 and 30 has a window of exactly `{3, 30}`, and chapter 12
does not silently inherit it.

This is spoiler-safe by construction. If chapter N is in the window, a trigger
occurs in chapter N, so the entry was already in play at or before N — an entry
introduced in chapter 30 cannot enter the chapter-3 packet.

What it cannot see is an entry introduced early whose *own body* explains a
late reveal. A real per-entry spoiler ceiling depends on the story encoding and
weaving and on worldbuilding, so it is not guessed; `Graph/schema.yaml` records
it under `planned.spoiler_until` with `status: not-implemented` and
`default_when_unknown: 40`. Until it lands, read a body before using it when
the chapter is early and the entry is central.

The window is computed on every run rather than stored, so nothing can go stale
and it sharpens as chapters are written.

## Retrieval ladder

1. Establish task, target chapter, scene, and whether future spoilers are
   allowed. If the answer affects selection and is unknown, ask.
2. Run `scripts/context_packet.py --chapter N`. That is the Codex rung, and it
   is where every chapter starts today.
3. Read `Wiki/context-map.md` for the research layer. When it has no row for
   the target — the case for every chapter until pages are promoted — the
   packet from step 2 is the whole answer from this layer.
4. Where the map does have rows: filter by chapter window, require
   `spoiler_until <= target chapter` for spoiler-safe work, and load `core`
   before `supporting`. Load `evidence` only when the task needs substantiation.
5. Open the smallest matching page and only the relevant heading range. In the
   Codex that means one file under `entries/`, `axioms/` or `timeline/`, never
   a partition index as a reading list.
6. Follow citations to exact source lines only when wording, evidence, or a
   conflict must be verified. Never load a complete raw source by default.
7. Stop when the writing decision is supported; more context is not
   automatically better context.

## Packet order

Build working context in this order:

1. task and chapter constraints;
2. the always-on writing constraints (R-rules, register, active world sensorik);
3. core synthesis/concept summaries;
4. open questions that materially affect the scene;
5. relevant detailed headings;
6. exact evidence excerpts.

Preserve source references in notes so claims can be rechecked without keeping
large source bodies in active context.

## Know what a packet costs

A packet nobody measured is a packet nobody trusts. Every codex body together
is ~84,400 tokens — what "load the glossary" used to mean. A chapter-3 packet
is ~21,700 across 232 files: 8,900 always-on, 8,800 chapter-anchored, 4,000
axioms. `--json` prints that breakdown for any chapter.

Before reporting that a retrieval path works, say what it loaded and roughly
what it cost. A ladder that ends in "and then read the glossary" has not done
its job — and since `Codex/GLOSSARY.md` is now navigation only, that sentence
no longer even reaches the content.

## Safety defaults

- Unknown spoiler ceiling means `40`, never "safe everywhere".
- Unknown chapter range means whole-novel scope until reviewed.
- A summary routes retrieval; it never substitutes for authority or evidence.
- Conflicting pages are loaded together and surfaced to the author; the
  maintenance workflow does not resolve the conflict.
