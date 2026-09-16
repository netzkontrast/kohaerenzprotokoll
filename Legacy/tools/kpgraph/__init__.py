"""Read the novel's facts from ``Graph/`` — plain files, standard library only.

``Graph/`` holds one JSONL file per node label plus ``edges.jsonl``
(``Graph/README.md`` documents the layout). This module loads them once and
answers the questions the repo's scripts ask:

    from tools import kpgraph
    g = kpgraph.load()
    for entry in g.nodes("CodexEntry"):
        print(entry["slug"], entry["name"])
    for axiom_nid, world_nid in g.edges("PART_OF_WORLD"):
        ...
    world = g.node(world_nid)
    axioms = g.sources_of(world_nid, "PART_OF_WORLD")

Nodes are dicts exactly as the files store them; ``_nid`` is the integer an
edge points at and ``id`` is the human-readable handle (``codex:1a2b3c``).
Both resolve through :meth:`Graph.node`. Nothing here writes: the files are
the author's, at the same level as ``Canon/``.
"""
from __future__ import annotations

import json
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
GRAPH_DIR = "Graph"
NODES_DIR = "nodes"
EDGES_FILE = "edges.jsonl"

# The label each file holds, keyed by file stem (the inverse of the exporter's
# CamelCase -> snake_case rule, spelled out so the mapping is greppable).
LABELS = {
    "novel": "Novel",
    "storyform": "Storyform",
    "chapter": "Chapter",
    "scene": "Scene",
    "narrative_beat": "NarrativeBeat",
    "world": "World",
    "world_axiom": "WorldAxiom",
    "codex_entry": "CodexEntry",
    "story_time_event": "StoryTimeEvent",
    "novel_claim": "NovelClaim",
    "decision_record": "DecisionRecord",
}


def read_jsonl(path: Path) -> list[dict]:
    """Records of one JSONL file; a malformed line raises with its number."""
    if not path.is_file():
        return []
    records = []
    for lineno, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        try:
            records.append(json.loads(line))
        except json.JSONDecodeError as exc:
            raise ValueError(f"{path}:{lineno}: {exc}") from exc
    return records


class Graph:
    """Every node and edge of ``Graph/``, indexed for lookup by id and by type."""

    def __init__(self, by_label: dict[str, list[dict]], edge_records: list[dict]) -> None:
        self._by_label = by_label
        self._by_nid = {n["_nid"]: n for nodes in by_label.values() for n in nodes}
        self._by_id = {n["id"]: n for nodes in by_label.values() for n in nodes if "id" in n}
        self._by_type: dict[str, list[tuple[int, int]]] = defaultdict(list)
        self._out: dict[tuple[int, str], list[int]] = defaultdict(list)
        self._in: dict[tuple[int, str], list[int]] = defaultdict(list)
        for record in edge_records:
            source, target, etype = record["source"], record["target"], record["type"]
            self._by_type[etype].append((source, target))
            self._out[(source, etype)].append(target)
            self._in[(target, etype)].append(source)

    # --- nodes ---

    def labels(self) -> list[str]:
        """Labels that carry at least one node, in file order."""
        return [label for label in LABELS.values() if self._by_label.get(label)]

    def nodes(self, label: str) -> list[dict]:
        """Every node of ``label``, in export order (``_nid`` ascending)."""
        return list(self._by_label.get(label, []))

    def node(self, key: int | str) -> dict | None:
        """One node by its ``_nid`` or by its ``id`` handle."""
        return self._by_nid.get(key) if isinstance(key, int) else self._by_id.get(key)

    # --- edges ---

    def edges(self, etype: str) -> list[tuple[int, int]]:
        """``(source_nid, target_nid)`` for every edge of ``etype``."""
        return list(self._by_type.get(etype, []))

    def edge_types(self) -> list[str]:
        return sorted(self._by_type)

    def targets_of(self, source: int, etype: str) -> list[dict]:
        """The nodes ``source`` points at along ``etype``."""
        return [self._by_nid[n] for n in self._out.get((source, etype), []) if n in self._by_nid]

    def sources_of(self, target: int, etype: str) -> list[dict]:
        """The nodes that point at ``target`` along ``etype``."""
        return [self._by_nid[n] for n in self._in.get((target, etype), []) if n in self._by_nid]

    # --- the questions the scripts actually ask ---

    def novel(self) -> dict | None:
        """The single Novel node, or nothing when the graph is empty."""
        found = self.nodes("Novel")
        return found[0] if found else None

    def chapters(self) -> list[dict]:
        """Chapters ordered by their ``number``."""
        return sorted(self.nodes("Chapter"), key=lambda ch: int(ch.get("number", 0)))

    def codex_by_kind(self, kind: str = "") -> list[dict]:
        """Codex entries, optionally of one ``kind``, ordered by slug."""
        entries = [e for e in self.nodes("CodexEntry") if not kind or e.get("kind") == kind]
        return sorted(entries, key=lambda e: e.get("slug", ""))

    def axioms_of(self, world_nid: int) -> list[dict]:
        """The world rules attached to one World node."""
        return self.sources_of(world_nid, "PART_OF_WORLD")

    def scenes_of(self, chapter_nid: int) -> list[dict]:
        return self.sources_of(chapter_nid, "SCENE_OF")

    def beats_of(self, scene_id: str) -> list[dict]:
        """Beats of a scene in insertion order — see Graph/README.md on ordering."""
        return [b for b in self.nodes("NarrativeBeat") if b.get("scene") == scene_id]

    def claims_by_domain(self) -> dict[str, list[dict]]:
        out: dict[str, list[dict]] = defaultdict(list)
        for claim in self.nodes("NovelClaim"):
            out[claim.get("domain", "")].append(claim)
        return dict(out)


def load(root: Path | str | None = None) -> Graph:
    """Load ``Graph/`` under ``root`` (the repository root by default)."""
    base = Path(root or ROOT) / GRAPH_DIR
    by_label = {label: read_jsonl(base / NODES_DIR / f"{stem}.jsonl")
                for stem, label in LABELS.items()}
    return Graph(by_label, read_jsonl(base / EDGES_FILE))
