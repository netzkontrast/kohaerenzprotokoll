# Graph — the novel's facts as plain files

This directory is the provenance layer of the three-layer knowledge system
(`Sources/` → `Wiki/` → `Canon/` + graph). It holds the facts that were
seeded from `Canon/` and are referenced by the manuscript: codex entries,
world axioms, chapters, scenes, beats, story-time events, research claims
and recorded decisions.

It used to live in `.agency/session.db`, a property graph owned by a plugin.
The facts are the author's and outlive the tool that wrote them, so they are
kept here instead: one JSONL file per node label, one edge file, greppable
with `grep` and diffable in a pull request.

    grep -l "Landauer" Graph/nodes/*.jsonl
    python3 -c "import json,sys; [print(json.loads(l)['name']) for l in open('Graph/nodes/world.jsonl')]"

Read it in Python through `tools/kpgraph`, which is stdlib-only:

```python
from tools import kpgraph
g = kpgraph.load()
for entry in g.nodes("CodexEntry"):
    print(entry["slug"], entry["name"])
for src, dst in g.edges("CODEX_OF"):
    ...
```

## Layout

| file | records | what it holds |
|---|---|---|
| `nodes/novel.jsonl` | 1 | the Novel node — title, author, genre, status |
| `nodes/storyform.jsonl` | 1 | Storyform A as an embedded JSON body |
| `nodes/chapter.jsonl` | 41 | chapters 0–40 with `number`, `title`, `status`, `body` |
| `nodes/scene.jsonl` | 15 | Kap-0 scenes with `slug`, `pov`, parent `chapter` |
| `nodes/narrative_beat.jsonl` | 97 | beats with `label` and their parent `scene` |
| `nodes/world.jsonl` | 7 | KW1–KW4, Überwelt, Externe Ebene, Kosmos-Meta |
| `nodes/world_axiom.jsonl` | 111 | world rules with `text` and `severity` (hard/soft) |
| `nodes/codex_entry.jsonl` | 602 | codex entries with `slug`, `name`, `kind`, `body`, `triggers` |
| `nodes/story_time_event.jsonl` | 56 | dated events with `label` and `when_story` |
| `nodes/novel_claim.jsonl` | 223 | research claims with `text`, `source_uri`, `domain` |
| `nodes/decision_record.jsonl` | 26 | recorded decisions with `decision`, `rationale`, `next_action` |
| `edges.jsonl` | 802 | typed edges between the nodes above |

## How to read a record

Every node carries `_nid`, an integer that is its identity. Edge records
point at those integers, so an edge resolves by `_nid` and nothing else:

```json
{"_nid": 406, "id": "worldaxiom:d8d0ccfd", "severity": "hard",
 "text": "Die Temperatur in KW1 ist konstant 21°C; …", "vfrom": 375}
{"source": 406, "target": 392, "type": "PART_OF_WORLD"}
```

`vfrom` records when the fact entered the graph. The keys are sorted and one
record sits on one line, so a change to one fact is a one-line diff.

Edge types: `CODEX_OF` (602, entry → novel), `PART_OF_WORLD` (111, axiom →
world), `CHAPTER_OF` (41, chapter → novel), `SCENE_OF` (15, scene → chapter),
`HAPPENS_AT` (15, scene → event), `REVEALED_IN` (15, event → scene),
`PRECEDES` (3, beat → beat).

## What is not here

The source database held 3,953 nodes; 1,180 of them were the novel. The rest
was the plugin's own audit trail — 1,956 `Invocation` nodes, 783 `Event`
nodes, plus `Intent`, `Phase`, `Gate`, `Reflection`, `Artefact`, `Skill` and
`Agent` — recording which tool call performed which write. Those records
describe a tool that is no longer part of this repo, so the export drops
them along with the 3,161 `SERVES` and 1,946 `PERFORMED_BY` edges that only
connected them. `scripts/export_graph.py` names the split.

Beat ordering is thin: 3 of the 97 beats carry a `PRECEDES` edge. The other
94 are grouped by their `scene` property and ordered by `_nid`, which is
insertion order. A topological sort over `PRECEDES` therefore says very
little about narrative order; the scene grouping is the reliable signal.

## Ownership

These files are the author's, at the same level as `Canon/`. Scripts render
*views* from them and never the other way round:

- `scripts/render_codex_views.py` → `Codex/GLOSSARY.md`, `MASTER-TIMELINE.md`, `WORLD-AXIOMS.md`
- `scripts/materialize_manuscript.py` → the chapter files under `Manuscript/`
- `scripts/audit_graph_claims.py` → the claim audit

The generated `Codex/*.md` views are never hand-edited: change the fact here
and re-render. `scripts/export_graph.py` regenerated this directory from the
retired database and is kept so the derivation stays checkable.
