"""Tests for tools/kpgraph: the file-based graph reader and its writer."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools import kpgraph  # noqa: E402
from tools.kpgraph.writer import GraphWriter, derive_id  # noqa: E402

NOVEL_ID = "novel:test0001"
CHAPTER_ID = "chapter:test0001"


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n"
                            for r in records), encoding="utf-8")


@pytest.fixture
def root(tmp_path: Path) -> Path:
    """A tiny graph: one novel, two chapters, one world with two axioms."""
    nodes = tmp_path / "Graph" / "nodes"
    write_jsonl(nodes / "novel.jsonl", [{"_nid": 1, "id": NOVEL_ID, "title": "KP", "vfrom": 1}])
    write_jsonl(nodes / "chapter.jsonl", [
        {"_nid": 3, "id": "chapter:b", "number": 2, "title": "Zwei", "body": "zwei", "vfrom": 3},
        {"_nid": 2, "id": CHAPTER_ID, "number": 1, "title": "Eins", "body": "eins", "vfrom": 2}])
    write_jsonl(nodes / "world.jsonl", [{"_nid": 4, "id": "world:a", "name": "KW1",
                                         "slug": "kw1", "vfrom": 4}])
    write_jsonl(nodes / "world_axiom.jsonl", [
        {"_nid": 5, "id": "worldaxiom:a", "text": "kalt", "severity": "hard", "vfrom": 5},
        {"_nid": 6, "id": "worldaxiom:b", "text": "warm", "severity": "soft", "vfrom": 6}])
    write_jsonl(nodes / "novel_claim.jsonl", [
        {"_nid": 7, "id": "novelclaim:a", "text": "t", "domain": "cultural",
         "source_uri": "Canon/x.md", "vfrom": 7}])
    write_jsonl(tmp_path / "Graph" / "edges.jsonl", [
        {"type": "CHAPTER_OF", "source": 2, "target": 1},
        {"type": "CHAPTER_OF", "source": 3, "target": 1},
        {"type": "PART_OF_WORLD", "source": 5, "target": 4},
        {"type": "PART_OF_WORLD", "source": 6, "target": 4}])
    return tmp_path


def test_labels_and_nodes_load(root):
    g = kpgraph.load(root)
    assert g.labels() == ["Novel", "Chapter", "World", "WorldAxiom", "NovelClaim"]
    assert len(g.nodes("Chapter")) == 2 and g.nodes("Missing") == []


def test_node_resolves_by_nid_and_by_id(root):
    g = kpgraph.load(root)
    assert g.node(1)["id"] == NOVEL_ID
    assert g.node(NOVEL_ID)["_nid"] == 1
    assert g.node("nope:1") is None and g.node(999) is None


def test_chapters_are_ordered_by_number_not_file_order(root):
    assert [c["number"] for c in kpgraph.load(root).chapters()] == [1, 2]


def test_edges_and_both_directions(root):
    g = kpgraph.load(root)
    assert sorted(g.edges("CHAPTER_OF")) == [(2, 1), (3, 1)]
    assert [n["number"] for n in g.sources_of(1, "CHAPTER_OF")] == [1, 2]
    assert g.targets_of(2, "CHAPTER_OF")[0]["id"] == NOVEL_ID
    assert g.edge_types() == ["CHAPTER_OF", "PART_OF_WORLD"]


def test_axioms_of_a_world(root):
    g = kpgraph.load(root)
    assert sorted(a["text"] for a in g.axioms_of(4)) == ["kalt", "warm"]


def test_claims_by_domain(root):
    assert kpgraph.load(root).claims_by_domain() == {
        "cultural": [kpgraph.load(root).node("novelclaim:a")]}


def test_a_malformed_line_names_its_number(tmp_path):
    (tmp_path / "Graph" / "nodes").mkdir(parents=True)
    (tmp_path / "Graph" / "nodes" / "novel.jsonl").write_text("{}\n{bad}\n", encoding="utf-8")
    with pytest.raises(ValueError, match=r"novel\.jsonl:2"):
        kpgraph.load(tmp_path)


def test_an_absent_graph_loads_empty(tmp_path):
    assert kpgraph.load(tmp_path / "nothing").labels() == []


def test_derive_id_is_stable_and_label_scoped():
    assert derive_id("CodexEntry", "risse") == derive_id("CodexEntry", "risse")
    assert derive_id("CodexEntry", "risse") != derive_id("World", "risse")
    assert derive_id("CodexEntry", "risse").startswith("codexentry:")


def test_the_writer_mints_a_node_and_its_parent_edge(root):
    w = GraphWriter(root)
    result = w.apply("create_codex_entry", {"slug": "risse", "name": "Risse",
                                            "kind": "concept", "body": "b", "novel_id": NOVEL_ID})
    w.flush()
    g = kpgraph.load(root)
    entry = g.node(result["entry_id"])
    assert entry["slug"] == "risse" and entry["_nid"] == 8
    assert g.targets_of(entry["_nid"], "CODEX_OF")[0]["id"] == NOVEL_ID


def test_applying_the_same_operation_twice_creates_one_node(root):
    w = GraphWriter(root)
    args = {"slug": "risse", "name": "Risse", "kind": "concept", "body": "b", "novel_id": NOVEL_ID}
    assert w.apply("create_codex_entry", args) == w.apply("create_codex_entry", args)
    w.flush()
    assert len(kpgraph.load(root).nodes("CodexEntry")) == 1
    assert (w.created, w.skipped) == (1, 1)


def test_a_second_writer_over_written_files_adds_nothing(root):
    args = {"slug": "risse", "name": "Risse", "kind": "concept", "body": "b", "novel_id": NOVEL_ID}
    first = GraphWriter(root)
    first.apply("create_codex_entry", args)
    first.flush()
    second = GraphWriter(root)
    second.apply("create_codex_entry", args)
    assert (second.created, second.skipped) == (0, 1)
    assert second.flush() == []


def test_beats_thread_a_precedes_edge(root):
    w = GraphWriter(root)
    scene = w.apply("create_scene", {"slug": "s", "pov": "first", "chapter_id": CHAPTER_ID})
    one = w.apply("mark_narrative_beat", {"scene_id": scene["scene_id"], "beat_label": "one"})
    two = w.apply("mark_narrative_beat", {"scene_id": scene["scene_id"], "beat_label": "two",
                                          "predecessor_id": one["beat_id"]})
    w.flush()
    g = kpgraph.load(root)
    assert g.edges("PRECEDES") == [(g.node(one["beat_id"])["_nid"], g.node(two["beat_id"])["_nid"])]
    assert g.targets_of(g.node(scene["scene_id"])["_nid"], "SCENE_OF")[0]["id"] == CHAPTER_ID


def test_set_chapter_status_updates_in_place(root):
    w = GraphWriter(root)
    w.apply("set_chapter_status", {"chapter_id": CHAPTER_ID, "status": "revised"})
    w.flush()
    assert kpgraph.load(root).node(CHAPTER_ID)["status"] == "revised"
    assert len(kpgraph.load(root).nodes("Chapter")) == 2


def test_reveal_in_scene_links_an_event(root):
    w = GraphWriter(root)
    scene = w.apply("create_scene", {"slug": "s", "pov": "first", "chapter_id": CHAPTER_ID})
    event = w.apply("record_story_event", {"label": "Genesis", "when_story": "vorher"})
    w.apply("reveal_in_scene", {"event_id": event["event_id"], "scene_id": scene["scene_id"]})
    w.flush()
    g = kpgraph.load(root)
    assert g.targets_of(g.node(event["event_id"])["_nid"], "REVEALED_IN")[0]["slug"] == "s"


def test_an_unknown_operation_fails_loudly(root):
    with pytest.raises(KeyError, match="unknown graph operation"):
        GraphWriter(root).apply("summon_daemon", {})


def test_nothing_reaches_disk_before_flush(root):
    before = (root / "Graph" / "nodes" / "world.jsonl").read_bytes()
    w = GraphWriter(root)
    w.apply("create_world", {"slug": "kw2", "name": "KW2"})
    assert (root / "Graph" / "nodes" / "world.jsonl").read_bytes() == before
    w.flush()
    assert len(kpgraph.load(root).nodes("World")) == 2
