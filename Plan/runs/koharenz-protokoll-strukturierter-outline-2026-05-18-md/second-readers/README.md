# Second readers — document 14, 2026-09-24

Three of the tools installed on 2026-09-24 read
`koharenz-protokoll-strukturierter-outline-2026-05-18-md` after its reader's
candidate list was committed (`a5d32e2`, 19:58:09 UTC). Each started at 19:59 in
the background. **Each ran with Claude as the model, so no corpus text went to a
third party** — the reason these two tools, which the tool review could not
reach through the free-model router, could be run here at all. No second reader
saw the reader's list or the wiki; their prompts said so, and the graphify
reader states it did not open `03-candidates.md`.

**Nothing any of them produced entered a page, a link, a count or a judgement.**
Three self-consistency points one of them raised were checked against their
lines and then written into the census, attributed to the reader that found them.

## What ran

| reader | the tool as designed | model | output | subagent tokens | time |
|---|---|---|---|--:|--:|
| entity list | `.claude/workflows/entity-lists.js`, the prompt verbatim, one agent | Haiku | 80 names → `entities.py place` → `Plan/entities/<slug>.md` | 92,282 | 76 s |
| graphify | `.claude/skills/graphify`, document mode: the extraction spec verbatim, one subagent | Claude (session default) | `graphify/.graphify_chunk_01.json` — 193 nodes, 674 edges, 3 hyperedges; built into a graph and `GRAPH_REPORT.md` | 387,324 | 29 min |
| knowledge-graph-extract | `.claude/skills/knowledge-graph-extract`, open schema, 200-triplet cap, one chunk | Claude (session default) | `kge/` — 174 entities, 200 triplets, 81 relation names; validator 200 of 200 valid | 267,564 | 35 min |

Why the two graph tools took half an hour: both have the model do every step —
read the whole document with the Read tool, then write each node, edge, entity
and triplet itself. The document is one chunk of 1,393 lines for both. The
entity list returns names only; code places the lines.

The graphify reader went beyond its spec in one useful way: it wrote its chunk
from a generator (`graphify/build_chunk.py`) that places every
`source_location` by searching for an anchor string — P26, taken from this
repository's rules — and refuses to build if an anchor is missing. graphify's
spec leaves `source_location` empty. The knowledge-graph-extract triplets carry
no line at all.

## Scored against the reader's list

`python3 scripts/entities.py score <slug> [--names <file>]` — a name the document
does not contain word for word is refused, never scored.

| second reader | names | verified | refused | shared | precision | recall | F1 |
|---|--:|--:|--:|--:|--:|--:|--:|
| entity list (Haiku) | 80 | 78 | 2 | 63 | 0.81 | 0.11 | 0.19 |
| graphify node labels | 193 | 163 | 30 | 89 | 0.55 | 0.16 | 0.24 |
| knowledge-graph-extract entities | 174 | 172 | 2 | 137 | 0.80 | 0.24 | **0.37** |
| … the same, with their aliases | 300 | 289 | 3 | 184 | 0.64 | 0.32 | 0.43 |

**Read the recall as the reader's granularity, not the tools' failure.** The
reader's list is 572 entries after folding: every chapter number and title,
every beat, every Genesis step. A list of 80 to 200 names cannot recall much of
that. Precision is the informative column. Two readers of one document agreed
at F1 0.66 (P27); the Haiku floor on document 5 was 0.25.

**One document, one attempt each (P18): these are measurements, not verdicts.**

### Where they differ from the reader, by name

- **graphify** labels whole headings — `Kap 1 — Erwachen in der Konstrukt-Stadt`,
  `KW1 — Logos-Prime`, `Storyform A — Heuristics of Integration` — where the
  reader listed their parts; 41 of its 74 names that are not on the reader's
  list are chapter headings. Its 30 refusals are glossed or re-cased labels
  (`Decision (Driver A)`, `OQ-A — Naming der finalen Form`, `Lebende Paradoxie`) —
  glossed, re-cased or composed labels.
- **knowledge-graph-extract** names the Dramatica values the reader left out
  (`Change`, `Steadfast`, `Pursuit`, `Universe` …), the formulas, the source
  files L1393 names, and the three modes. Refused: two names it composed,
  `negativ definierte Kohärenz` and `positiv definierte Kohärenz`.
- **The entity list** named `Persistenzgleichung`, **which the document does not
  contain** — named from outside it and stopped by `place` — and translated one
  name, `Landauer warmth`. Its reader reported 98 entities; the file holds 80.
- **What the reader's list lacks and a second reader has**: the bare `Genesis`
  (graphify, knowledge-graph-extract), the second spelling `Erasure-Operator`
  (graphify), `Komp 734` (entity list). A miss is not automatically an error
  (P27): the reader listed `Genesis-Sequenz`, `Komponente 734` and
  `Erasure-Operator-Echo`.

## What the graph tools noticed

**graphify's five AMBIGUOUS edges are four points the census also records**
(self-consistency, surfaces, boundaries), **reached independently**: LogOS absorbed into the Erasure-Pol (L161) and
into Mnemosyne (L172), Kairos absorbed (L161) and latent (L175), `Erason-Operator`
against `Erasure-Operator` (L156, L1017), and `Guardian` as two Guardians and as a
stage of Selene's arc (L136, L158). Its report turns each into a „suggested
question". It did not flag the two Genesis orders. Its reader's text report added
three the census had missed — the Erasure-Pol's open name has no OQ row, KW3 is a
setting in no chapter, Kap 26 sits at `Shō → Ten` — all three checked and now in
the census, attributed.

**knowledge-graph-extract** kept both sides of both absorptions as triplets
(`Mnemosyne ABSORBS LogOS`, `Erasure-Pol ABSORBS LogOS`) and has `Juna
FIRST_APPEARS_DIRECTLY_IN Kap 38` and `Kap 36 HAS_SENSORY_MOTIF Landauer-Wärme`.
Within its 200-triplet cap it has nothing on the knuckles, Sophia, Mosaik-Herz,
the Ursprungs-Ich or `Wächter` — five of the subjects the reconciliation moved.

## Against the tool review of the same day

`Plan/concept/tool-review_2026-09-24.md` lists knowledge-graph-extract and
graphify's document mode as **not reached** (P15): through the free-model router
the first was rate-limited and the second never answered. With Claude as the
model both reached a result on a canon-era document. That changes the review's
„not reached" for these two, and not its verdicts on the others: nothing here
ran grawiki, semantica, Hyper-Extract, M-flow or OpenCode, and no text went to
Jev or OpenRouter.

## What they may not do

A node, edge, entity or triplet here is a model's reading: it may not create a
page, write a `[[link]]`, supply a count, merge two surfaces or detect a conflict
(`CLAUDE.md`). The entity list is the one exception by design — it feeds
`graph.proposals()`, which says what it is.

## Faster — measured on the same document, the same afternoon

The author asked why knowledge-graph-extract took so long, and how to make it
faster. Two variants were run right after, on the same document:

- **four Haiku readers in parallel**, one per chapter block (L1–342, L343–730,
  L731–1070, L1071–1393). Each wrote 40 to 70 `subject⇥RELATION⇥object` lines
  and nothing else. `fast/merge.py` places every subject and object on a line in
  its block with `entities.holds`, refuses what does not stand there word for
  word, and deduplicates.
- **no model**: `fast/template_parse.py` reads the chapter template, the
  `**Label:** value` fields of all 41 entries.

| variant | wall-clock | subagent tokens | output | names verified | P | R | F1 |
|---|--:|--:|---|--:|--:|--:|--:|
| knowledge-graph-extract: one agent, session model, one chunk, JSONL | 35 min | 267,564 | 200 triplets, no lines | 172 | 0.80 | 0.24 | 0.37 |
| graphify: one agent, session model, JSON | 29 min | 387,324 | 674 edges, lines by its generator | 163 | 0.55 | 0.16 | 0.24 |
| **4 × Haiku in parallel, TSV, lines by code** | **91 s** | 273,062 | 157 of 277 rows kept | 229 | 0.28 | 0.11 | 0.16 |
| … the same, an underscore read as a space | 91 s | 273,062 | 195 of 277 rows kept | 274 | 0.32 | 0.16 | 0.21 |
| **template parser, no model** | **6 ms** | 0 | 603 rows, every one with its line | 114 | 0.66 | 0.13 | 0.22 |
| entity list, Haiku, names only | 76 s | 92,282 | 80 names | 78 | 0.81 | 0.11 | 0.19 |

**What the time was.** Not tokens: the parallel run used as many (273k against
268k) and finished 23 times sooner. It was one agent working through one
1,393-line chunk step by step, writing every row itself — kge appending JSONL in
batches, graphify building and re-checking a 47 KB generator.

**What speed cost here.** Haiku kept less of the rules: 120 of its 277 rows were
refused, 53 for a subject and 61 for an object not in the block word for word —
underscores written for spaces, composed phrases. Reading an underscore as a
space recovers 38. Its names are often fragments (`A`, `Beat 2`, whole clauses),
and within its budget it has nothing on the absorptions, the Landauer trace or
the knuckles, which knowledge-graph-extract has in part.

**What code alone gets.** A templated document hands its table to a parser: every
chapter's title, POV, storyform, bridge, sensory motif, tonal axis and 147
chapter–character rows, each with its line, in 6 ms. That is the unit `GOAL.md`
asks for — the chapter — and none of it needs a model (P1). It gets nothing from
free prose.

**So, ranked by what is measured:**

1. **A parser for the template, where there is one** (`profile.py` already reports
   repeated field labels). Free, instant, every row cited.
2. **Split at headings and read the blocks in parallel.** Wall-clock falls by the
   number of blocks at the same token cost.
3. **Ask for less than JSON**: names or `subject⇥RELATION⇥object` lines, with code
   placing the lines and building the structure (P26) — no types, aliases or
   rationale the project does not use.
4. **Keep the session model for the reading.** Haiku was fast and followed the
   format worst. The one combination not yet measured — the session model, four
   blocks in parallel, TSV — is the likely middle; one run would say.

None of this changes the main loop's pace: every second reader ran in the
background while the reconciliation was done by hand, and the one artifact that
cannot be sped up is the reader's own list.

## Rebuild

```bash
# the graph and report from the chunk (graph.json is derived, not kept)
/root/.local/share/uv/tools/graphifyy/bin/python Plan/runs/koharenz-protokoll-strukturierter-outline-2026-05-18-md/second-readers/graphify/build_graph.py
python3 Plan/runs/koharenz-protokoll-strukturierter-outline-2026-05-18-md/second-readers/fast/merge.py [--repair]
python3 Plan/runs/koharenz-protokoll-strukturierter-outline-2026-05-18-md/second-readers/fast/template_parse.py
python3 scripts/entities.py score koharenz-protokoll-strukturierter-outline-2026-05-18-md --names Plan/runs/koharenz-protokoll-strukturierter-outline-2026-05-18-md/second-readers/graphify/names.json
python3 scripts/entities.py score koharenz-protokoll-strukturierter-outline-2026-05-18-md --names Plan/runs/koharenz-protokoll-strukturierter-outline-2026-05-18-md/second-readers/kge/names.json
python3 .claude/skills/knowledge-graph-extract/scripts/validate_triples.py Plan/runs/koharenz-protokoll-strukturierter-outline-2026-05-18-md/second-readers/kge
```
