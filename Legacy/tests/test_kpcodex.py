"""Tests for tools/kpcodex and scripts/context_packet.py — the partitioned codex."""
from __future__ import annotations

import json
import re
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

from tools import kpcodex, kpgraph  # noqa: E402
import context_packet  # noqa: E402

NOVEL = "novel:test0001"
RULE_BODY = "**Kategorie:** rule  Eine Regel, die immer gilt und nie im Text vorkommt."
CONCEPT_BODY = "**Kategorie:** concept  ## Quelle: Canon/x.md  Der Riss ist ein Phänomen."


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n"
                            for r in records), encoding="utf-8")


@pytest.fixture
def graph(tmp_path: Path):
    """Two entries: one always-on rule, one concept triggered by 'riss'."""
    write_jsonl(tmp_path / "Graph" / "nodes" / "codex_entry.jsonl", [
        {"_nid": 1, "id": "codexentry:1", "slug": "r-1", "name": "R-1",
         "kind": "concept", "body": RULE_BODY, "triggers": "R-1, Regel eins"},
        {"_nid": 2, "id": "codexentry:2", "slug": "risse", "name": "Risse",
         "kind": "concept", "body": CONCEPT_BODY, "triggers": "Riss, Risse"},
    ])
    write_jsonl(tmp_path / "Graph" / "nodes" / "world_axiom.jsonl",
                [{"_nid": 3, "id": "worldaxiom:1", "text": "Kalt.", "severity": "hard"}])
    write_jsonl(tmp_path / "Graph" / "edges.jsonl", [])
    return kpgraph.load(tmp_path)


CHAPTERS = {1: "ein kapitel ganz ohne treffer.", 2: "hier reisst ein riss auf."}


def test_body_helpers_read_the_kategorie_and_source():
    assert kpcodex.kategorie(CONCEPT_BODY) == "concept"
    assert kpcodex.quelle(CONCEPT_BODY) == "Canon/x.md"
    assert kpcodex.first_paragraph(CONCEPT_BODY) == "Der Riss ist ein Phänomen."
    assert kpcodex.kategorie("kein marker hier") == ""


def test_summary_is_capped_at_forty_words():
    long_body = "**Kategorie:** note  " + " ".join(f"wort{i}" for i in range(80))
    assert len(kpcodex.summary(long_body).split()) == 40


def test_partition_uses_the_kategorie_and_misfiles_the_unknown():
    assert kpcodex.partition_of({"body": RULE_BODY, "kind": "concept"}) == "rule"
    assert kpcodex.partition_of({"body": "**Kategorie:** erfunden  x", "kind": "concept"}) == "_misfiled"
    # No Kategorie line at all falls back to the record's kind.
    assert kpcodex.partition_of({"body": "nur text", "kind": "location"}) == "location"


def test_entry_path_is_one_level_below_the_codex_root():
    path = kpcodex.entry_path({"slug": "risse", "body": CONCEPT_BODY, "kind": "concept"})
    assert path == "Codex/entries/concept/risse.md"
    assert path.count("/") == 3


def test_window_is_membership_not_span():
    entry = {"triggers": "Riss, Risse"}
    chapters = {1: "ein riss", 2: "nichts hier", 3: "noch ein riss"}
    assert kpcodex.window_of(entry, chapters) == [1, 3]      # 2 is absent, not filled in


def test_short_triggers_are_ignored():
    """A two-letter trigger would match half the corpus."""
    assert kpcodex.window_of({"triggers": "ab, Riss"}, {1: "ab ovo"}) == []
    assert kpcodex.window_of({"triggers": "ab, Riss"}, {1: "ein riss"}) == [1]


def test_a_chapter_in_the_window_implies_the_entry_was_already_in_play(graph):
    """The spoiler property the packet relies on, stated as a test."""
    for entry in graph.nodes("CodexEntry"):
        window = kpcodex.window_of(entry, CHAPTERS)
        for chapter in window:
            assert min(window) <= chapter


def test_views_render_one_file_per_entry_plus_indexes(graph):
    files = kpcodex.entry_views(graph, CHAPTERS)
    assert "Codex/entries/rule/r-1.md" in files
    assert "Codex/entries/concept/risse.md" in files
    assert "Codex/entries/rule/README.md" in files
    assert "Codex/entries/README.md" in files
    assert "Risse" in files["Codex/entries/concept/README.md"]


def test_the_root_index_lists_every_declared_category(graph):
    root = kpcodex.entry_views(graph, CHAPTERS)["Codex/entries/README.md"]
    for category in kpcodex.categories():
        assert f"({category}/README.md)" in root, category


def test_an_entry_page_carries_its_window_and_triggers(graph):
    page = kpcodex.entry_views(graph, CHAPTERS)["Codex/entries/concept/risse.md"]
    assert "Chapters in play: 2" in page
    assert "Triggers: Riss, Risse" in page
    assert "Canon/x.md" in page
    assert "**Kategorie:**" not in page          # the marker is structure, not content


def test_rendering_is_deterministic(graph):
    assert kpcodex.entry_views(graph, CHAPTERS) == kpcodex.entry_views(graph, CHAPTERS)


def test_packet_splits_always_on_from_chapter_anchored(graph):
    data = kpcodex.packet(graph, 2, CHAPTERS)
    assert [e["slug"] for e in data["always_on"]] == ["r-1"]
    assert [e["slug"] for e in data["anchored"]] == ["risse"]
    assert len(data["axioms"]) == 1


def test_an_always_on_entry_is_never_double_counted(graph):
    """A rule that also triggers stays in the always-on tier only."""
    data = kpcodex.packet(graph, 2, {2: "hier reisst ein riss auf und R-1 gilt."})
    slugs = [e["slug"] for e in data["always_on"]] + [e["slug"] for e in data["anchored"]]
    assert len(slugs) == len(set(slugs))


def test_a_chapter_with_no_hits_still_gets_the_always_on_tier(graph):
    data = kpcodex.packet(graph, 1, CHAPTERS)
    assert data["always_on"] and data["anchored"] == []


# --- the CLI -------------------------------------------------------------------------


def test_packet_paths_are_the_files_to_open(graph):
    data = kpcodex.packet(graph, 2, CHAPTERS)
    paths = context_packet.packet_paths(data)
    assert paths == ["Codex/entries/rule/r-1.md", "Codex/entries/concept/risse.md"]


def test_cost_reports_each_tier(graph):
    spend = context_packet.cost(kpcodex.packet(graph, 2, CHAPTERS), full=False)
    assert spend["total_tokens"] == (spend["always_on_tokens"] + spend["anchored_tokens"]
                                     + spend["axiom_tokens"])


def test_full_costs_more_than_cards(graph):
    data = kpcodex.packet(graph, 2, CHAPTERS)
    assert context_packet.cost(data, full=True)["always_on_tokens"] >= \
           context_packet.cost(data, full=False)["always_on_tokens"]


def test_cli_rejects_a_chapter_that_does_not_exist(capsys):
    assert context_packet.main(["--chapter", "99"]) == context_packet.EXIT_CANNOT_RUN
    assert "no chapter 99" in capsys.readouterr().err


def test_cli_paths_prints_only_paths(capsys):
    assert context_packet.main(["--chapter", "3", "--paths"]) == context_packet.EXIT_OK
    lines = [l for l in capsys.readouterr().out.splitlines() if l.strip()]
    assert lines and all(l.startswith("Codex/entries/") and l.endswith(".md") for l in lines)


def test_cli_json_carries_cost_and_paths(capsys):
    context_packet.main(["--chapter", "3", "--json"])
    data = json.loads(capsys.readouterr().out)
    assert data["chapter"] == 3 and data["cost"]["total_tokens"] > 0
    assert len(data["paths"]) == len(data["always_on"]) + len(data["anchored"])


def test_the_real_packet_is_far_smaller_than_the_whole_corpus(capsys):
    """The guiding test from todo.md: a chapter packet must not be the corpus.

    The baseline is every codex body, which is what loading "the glossary"
    used to mean. `Codex/GLOSSARY.md` itself is navigation now, so comparing
    against that file would compare against a router.
    """
    context_packet.main(["--chapter", "3", "--json"])
    data = json.loads(capsys.readouterr().out)
    corpus = kpgraph.load(ROOT).nodes("CodexEntry")
    corpus_tokens = sum(len(e.get("body", "")) for e in corpus) // 4
    assert data["cost"]["total_tokens"] < corpus_tokens / 2
    assert len(data["anchored"]) < 100


def test_the_root_glossary_is_navigation_only():
    """It routes to indexes and never to an entry, so it cannot carry a body."""
    glossary = (ROOT / "Codex" / "GLOSSARY.md").read_text(encoding="utf-8")
    links = re.findall(r"]\(([^)]+)\)", glossary)
    assert links, "a router with no links routes nowhere"
    assert all(link.endswith("README.md") for link in links), links
    assert len(glossary) // 4 < 1_000                      # ~71,700 before the split
    for category in kpcodex.categories():
        assert f"entries/{category}/README.md" in glossary, category


def test_the_reported_baseline_is_the_real_corpus(capsys):
    """The saving is only meaningful if the number it is measured against is."""
    context_packet.main(["--chapter", "3", "--json"])
    reported = json.loads(capsys.readouterr().out)["cost"]["corpus_tokens"]
    actual = sum(len(e.get("body", ""))
                 for e in kpgraph.load(ROOT).nodes("CodexEntry")) // 4
    assert reported == actual
    assert reported > 50_000                     # a router would report a few hundred


def test_every_packet_path_exists_on_disk(capsys):
    context_packet.main(["--chapter", "3", "--paths"])
    for line in capsys.readouterr().out.splitlines():
        assert (ROOT / line).is_file(), line
