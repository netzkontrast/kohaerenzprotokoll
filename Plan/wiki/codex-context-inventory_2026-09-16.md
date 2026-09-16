# Codex and Wiki inventory for context-efficient chapter work

Step 1 of `todo.md` ("Codex- und Wiki-Architektur für kontext-effiziente
Romanarbeit"): the inventory, the authority matrix, and a measured proposal.
No folders are created and nothing is migrated here — `todo.md` sets the mode
as a separate Codex-migration PR, and the questions at the end are the
author's to settle first.

The guiding test it has to pass:

> Can an agent work on chapter 3 coherently without loading the full glossary
> and without using knowledge from chapter 20?

Today that test **fails**, and the measurements below say why.

## What exists, and what it costs

| layer | holds | routing metadata | cost to load whole |
|---|---|---|---|
| `Codex/GLOSSARY.md` | 602 CodexEntry | **none** | ~71,700 tokens |
| `Codex/WORLD-AXIOMS.md` | 111 WorldAxiom in 7 Worlds | **none** | ~4,600 tokens |
| `Codex/MASTER-TIMELINE.md` | 56 StoryTimeEvent | `when_story` free text | ~2,200 tokens |
| `Wiki/context-map.md` | the routing table | chapter window, spoiler ceiling, priority, scope | ~155 tokens |
| `Wiki/**` pages | **0 promoted pages** | — | — |

The diagnosis is one sentence: **the routing lives in the layer with no
content, and the content lives in the layer with no routing.** `Wiki/` has a
context map, page budgets, chapter windows and spoiler ceilings, and nothing
to route. `Codex/` has every fact a chapter needs and no way to ask for a
subset, so the only honest answer to "what does chapter 3 need" is today
"all 602 entries".

Node fields, from `Graph/`:

- `CodexEntry` — `slug`, `name`, `kind`, `body`, `triggers`, `novel`.
- `WorldAxiom` — `text`, `severity`, and `PART_OF_WORLD`.
- `StoryTimeEvent` — `label`, `when_story` (free text, not a chapter number).

None of the three carries `introduced_in`, `revealed_in`, `writer_safe_from`
or a spoiler ceiling. That is `todo.md` question 3, and it is the gap.

## The signal that is already in the data

`todo.md` requires the target structure to be derived from stable entity and
graph fields, never from invented topic folders. One such field already
exists and is complete: **every one of the 602 entries carries `triggers`**,
the comma-separated phrases that mark where the entry is in play. Scanning the
41 chapter files for each entry's triggers yields a chapter hit-set per entry —
the `match_codex_entries` mechanism, run backwards over the manuscript.

Measured over the real corpus:

| | |
|---|---|
| entries appearing in at least one chapter | **203** of 602 |
| entries never appearing as words | **399** |
| chapter-3 hit-set | 41 entries, ~10,100 tokens |
| chapter-20 hit-set | 40 entries, ~10,400 tokens |

Two properties matter. First, membership beats span: using the exact hit-set
rather than first-to-last collapses a median 28-chapter window to roughly 40
entries per chapter. Second, **the hit-set is spoiler-safe by construction** —
if chapter 3 is in an entry's hit-set then its first appearance is at or
before chapter 3, so an entry introduced in chapter 20 cannot enter a
chapter-3 packet. Zero violations over the whole corpus.

The 399 entries that never appear as words are not noise. They classify
cleanly by the `**Kategorie:**` they already carry:

| count | category | what it is |
|---|---|---|
| 98 | rule | writing constraints |
| 86 | note | working notes |
| 55 | location | places reached by name |
| 45 | concept | ideas reached by name |
| 25 | guidance | drafting guidance |
| 17 | philosophy | substrate reasoning |
| 15 | defect | known failure modes |
| 14 | theme | thematic constraints |
| 13 · 8 · 8 · 6 | term · voice · question · physics | |

Rules, guidance, voice, defects, themes and philosophy are relevant to every
chapter and never appear as vocabulary — they constrain prose rather than
occur in it. Locations, concepts, terms and notes are lookups: needed when a
name comes up, not before.

## The three tiers this implies

| tier | what | selected by | chapter-3 cost |
|---|---|---|---|
| 1 — always on | writing constraints: rule, guidance, voice, defect, theme, philosophy | `**Kategorie:**`, already present | ~10,900 tokens as 40-word cards |
| 2 — chapter-anchored | entries whose triggers fire in this chapter | derived hit-set | ~8,800 tokens, full bodies |
| 3 — on demand | everything else: locations, terms, notes, concepts | `wiki_fts.py`, triggers | 0 until asked |
| world axioms | all 111, they are short | — | ~4,000 tokens |

**Chapter-3 packet: ~23,600 tokens against ~71,700 today — 3× smaller**, and
spoiler-safe by construction.

## What this proposal does not solve

Three limits, stated plainly rather than discovered later:

1. **3× is not 10×.** Tier 1 is 198 entries, and even compressed to 40-word
   cards it is ~10,900 tokens — nearly half the packet. If the always-on set
   were narrowed to the genuine hard constraints (R-1…R-10, the Sprach-DNA
   registers, the active world's sensorik) the packet would fall much further.
   That is an editorial judgement about which rules a writer must always hold,
   and it belongs to the author.
2. **Body-level spoilers survive.** The hit-set prevents loading an entry
   before it is introduced. It cannot stop an entry introduced in chapter 3
   from explaining the chapter-20 reveal inside its own body. A real
   `spoiler_until` per entry is the only fix, and it cannot be derived — it
   has to be authored or inferred and reviewed.
3. **The derivation reads the manuscript.** A chapter that is still an outline
   stub contributes no hits, so early chapters route well and unwritten ones
   route thinly. The window strengthens as the book is written, which is the
   right direction, but it means the map is not complete on day one.

## Authority matrix

`todo.md` asks for exactly one named source of truth per kind of information.
What the repository already implies, written down:

| information | single source of truth | rendered into |
|---|---|---|
| chapter prose | `Manuscript/**/chapters/` | — |
| normative story facts | `Canon/` (storyform-und-outline wins) | — |
| terms, rules, motifs, locations | `Graph/nodes/codex_entry.jsonl` | `Codex/GLOSSARY.md` |
| world rules | `Graph/nodes/world_axiom.jsonl` | `Codex/WORLD-AXIOMS.md` |
| story chronology | `Graph/nodes/story_time_event.jsonl` | `Codex/MASTER-TIMELINE.md` |
| storyform slots | `ncp.json` (A), `ncp-b.json` (B) | `dramatica.md` |
| research understanding | `Wiki/**` promoted pages | `Wiki/index.md`, `context-map.md` |
| raw research | `Sources/` | `Sources/manifest.jsonl` |
| retrieval routing | the context map | — |

The overlap `todo.md` asks about is real in one place: a codex entry and a
promoted wiki concept page can describe the same thing. The rule that keeps
them apart is epistemic, not topical — `Graph/` holds what the novel *is*,
`Wiki/` holds what the research *understands*, and `canon_status` on a wiki
page records whether the two have been checked against each other (D-W12).

## Questions the author settles before any migration

1. **Which rules are genuinely always-on?** All 198 rule-ish entries, or a
   narrow hard-constraint set with the rest moved to on-demand? This decides
   whether the packet is 3× or closer to 8× smaller.
2. **Is the chapter window stored or computed?** Computed on demand keeps one
   source of truth and costs a manuscript scan per run; stored as a rendered
   field makes it greppable and reviewable but adds a derived field that can
   go stale.
3. **Does `spoiler_until` get authored per entry?** Nothing derivable gives
   it, and without it body-level spoilers remain.
4. **Do codex entries gain a `kind_detail`-style partition** so the Codex
   splits into per-category files, or does `GLOSSARY.md` stay one rendered
   file with the packet assembled by a script?
5. **Which existing paths must stay valid during the migration?**
   `Codex/GLOSSARY.md` is referenced by the hooks, the skills and
   `render_codex_views.py --check`.

## Next step once those are answered

Per `todo.md`: a separate branch and PR, the new renderer running beside the
existing views rather than replacing them, and a chapter-3 packet generated
for a real chapter as the acceptance test. The measurements above are
reproducible from `Graph/` and the manuscript with no API key.
