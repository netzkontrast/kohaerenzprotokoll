"""Append facts to ``Graph/`` — the write side of the file-based graph.

The canon ingest used to reach an engine through ``agency execute``; each
capability verb minted a node and its edges. The same operations are spelled
out here against the JSONL files, so ``scripts/ingest_canon.py`` keeps working
with no engine and no database:

    from tools.kpgraph.writer import GraphWriter
    w = GraphWriter(root)
    entry = w.apply("create_codex_entry", {"slug": "risse", "name": "Risse",
                                           "kind": "concept", "body": "…"})
    w.flush()                       # one rewrite of the touched files

``apply`` returns the same ``{"<thing>_id": …}`` shape the verbs returned, so
an id can be threaded into the next operation (a beat's predecessor, a
scene's chapter). Nothing reaches disk until :meth:`flush`.

Writes are idempotent by construction. A node's ``id`` is derived from its
label and its natural key (a codex slug, a chapter number, an axiom's text),
so ingesting the same manifest twice produces the same id and the second run
recognises the record instead of duplicating it. That replaces the ledger
file the engine-era driver needed.
"""
from __future__ import annotations

import hashlib
import json
from pathlib import Path

from . import LABELS, Graph, load

ID_HEX = 8
KEY_SEPARATOR = "::"

# verb -> (label, natural key property, parent edge as (type, parent arg) or None)
VERBS: dict[str, tuple[str, str, tuple[str, str] | None]] = {
    "create_codex_entry": ("CodexEntry", "slug", ("CODEX_OF", "novel_id")),
    "create_chapter": ("Chapter", "number", ("CHAPTER_OF", "novel_id")),
    "create_scene": ("Scene", "slug", ("SCENE_OF", "chapter_id")),
    "create_world": ("World", "slug", None),
    "create_world_axiom": ("WorldAxiom", "text", ("PART_OF_WORLD", "world_id")),
    "record_story_event": ("StoryTimeEvent", "label", None),
    "mark_narrative_beat": ("NarrativeBeat", "beat_label", None),
    "capture_claim": ("NovelClaim", "text", None),
    "record_storyform_decision": ("DecisionRecord", "decision", None),
}

# The property each verb's node carries, mapped from the verb's argument name.
FIELDS: dict[str, dict[str, str]] = {
    "create_codex_entry": {"slug": "slug", "name": "name", "kind": "kind",
                           "body": "body", "triggers": "triggers", "novel_id": "novel"},
    "create_chapter": {"number": "number", "title": "title", "body": "body",
                       "status": "status", "novel_id": "novel"},
    "create_scene": {"slug": "slug", "pov": "pov", "chapter_id": "chapter"},
    "create_world": {"slug": "slug", "name": "name"},
    "create_world_axiom": {"text": "text", "severity": "severity"},
    "record_story_event": {"label": "label", "when_story": "when_story", "novel_id": "novel"},
    "mark_narrative_beat": {"beat_label": "label", "scene_id": "scene", "novel_id": "novel"},
    "capture_claim": {"text": "text", "source_uri": "source_uri",
                      "domain": "domain", "verified": "verified"},
    "record_storyform_decision": {"decision": "decision", "rationale": "rationale",
                                  "next_action": "next_action", "subject": "subject"},
}

# The key name ``apply`` returns for each label, matching the old verb results.
RESULT_KEY = {"CodexEntry": "entry_id", "Chapter": "chapter_id", "Scene": "scene_id",
              "World": "world_id", "WorldAxiom": "axiom_id", "StoryTimeEvent": "event_id",
              "NarrativeBeat": "beat_id", "NovelClaim": "claim_id",
              "DecisionRecord": "decision_id"}

STEM = {label: stem for stem, label in LABELS.items()}


def derive_id(label: str, natural_key: str) -> str:
    """``codexentry:1a2b3c4d`` — stable for the same label and key."""
    digest = hashlib.sha1(f"{label}{KEY_SEPARATOR}{natural_key}".encode()).hexdigest()
    return f"{label.lower()}:{digest[:ID_HEX]}"


class GraphWriter:
    """Stages node and edge records, then rewrites the files they belong to."""

    def __init__(self, root: Path, graph: Graph | None = None) -> None:
        self.root = Path(root)
        self.graph = graph or load(self.root)
        self._nodes = {label: list(self.graph.nodes(label)) for label in LABELS.values()}
        self._edges = [{"type": t, "source": s, "target": d}
                       for t in self.graph.edge_types() for s, d in self.graph.edges(t)]
        every = [n for nodes in self._nodes.values() for n in nodes]
        self._next_nid = max((int(n["_nid"]) for n in every), default=0) + 1
        self._clock = max((int(n.get("vfrom", 0)) for n in every), default=0) + 1
        self._by_id = {n["id"]: n for n in every if "id" in n}
        self._touched: set[str] = set()
        self.created = self.skipped = 0

    # --- staging ---

    def _mint(self, label: str, node_id: str, fields: dict) -> dict:
        record = {"_nid": self._next_nid, "id": node_id, "vfrom": self._clock, **fields}
        self._next_nid += 1
        self._clock += 1
        self._nodes[label].append(record)
        self._by_id[node_id] = record
        self._touched.add(label)
        self.created += 1
        return record

    def _link(self, etype: str, source: int, target_id: str) -> None:
        target = self._by_id.get(target_id)
        if target is None:
            return
        edge = {"type": etype, "source": int(source), "target": int(target["_nid"])}
        if edge not in self._edges:
            self._edges.append(edge)
            self._touched.add("edges")

    def apply(self, verb: str, args: dict) -> dict:
        """Run one operation; return its ``{"<thing>_id": …}`` result."""
        if verb == "reveal_in_scene":
            return self._reveal(args)
        if verb == "set_chapter_status":
            return self._set_status(args)
        if verb not in VERBS:
            raise KeyError(f"unknown graph operation: {verb}")
        label, key_arg, parent = VERBS[verb]
        fields = {prop: args[arg] for arg, prop in FIELDS[verb].items()
                  if args.get(arg) not in (None, "")}
        record = self._by_id.get(derive_id(label, str(args.get(key_arg, ""))))
        if record is None:
            record = self._mint(label, derive_id(label, str(args.get(key_arg, ""))), fields)
        else:
            self.skipped += 1
        if parent:
            self._link(parent[0], record["_nid"], str(args.get(parent[1], "")))
        if verb == "mark_narrative_beat" and args.get("predecessor_id") in self._by_id:
            self._link("PRECEDES", self._by_id[args["predecessor_id"]]["_nid"], record["id"])
        if verb == "record_story_event" and args.get("scene_id"):
            self._link("HAPPENS_AT", record["_nid"], str(args["scene_id"]))
        return {RESULT_KEY[label]: record["id"]}

    def _reveal(self, args: dict) -> dict:
        event = self._by_id.get(str(args.get("event_id", "")))
        if event is not None:
            self._link("REVEALED_IN", event["_nid"], str(args.get("scene_id", "")))
        return {"event_id": args.get("event_id", "")}

    def _set_status(self, args: dict) -> dict:
        chapter = self._by_id.get(str(args.get("chapter_id", "")))
        if chapter is not None and chapter.get("status") != args.get("status"):
            chapter["status"] = args["status"]
            self._touched.add("Chapter")
        return {"chapter_id": args.get("chapter_id", "")}

    # --- disk ---

    def flush(self) -> list[str]:
        """Rewrite every file this writer touched; return their paths."""
        written = []
        base = self.root / "Graph"
        for label in sorted(self._touched - {"edges"}):
            path = base / "nodes" / f"{STEM[label]}.jsonl"
            path.parent.mkdir(parents=True, exist_ok=True)
            records = sorted(self._nodes[label], key=lambda n: int(n["_nid"]))
            path.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n"
                                    for r in records), encoding="utf-8")
            written.append(f"Graph/nodes/{STEM[label]}.jsonl")
        if "edges" in self._touched:
            path = base / "edges.jsonl"
            ordered = sorted(self._edges, key=lambda e: (e["type"], e["source"], e["target"]))
            path.write_text("".join(json.dumps(e, ensure_ascii=False, sort_keys=True) + "\n"
                                    for e in ordered), encoding="utf-8")
            written.append("Graph/edges.jsonl")
        self._touched.clear()
        return written
