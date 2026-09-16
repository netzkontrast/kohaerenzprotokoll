"""Tests for scripts/world_check.py — the world-axiom contradiction scan."""
from __future__ import annotations

import json
import sys
from collections import Counter
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))
sys.path.insert(0, str(ROOT / "scripts"))

import world_check as wc  # noqa: E402

WORLD_ID = "world:test0001"


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n"
                            for r in records), encoding="utf-8")


def build(root: Path, axioms: list[str]) -> Path:
    """One world with the given axiom texts, each attached by PART_OF_WORLD."""
    nodes = root / "Graph" / "nodes"
    write_jsonl(nodes / "world.jsonl",
                [{"_nid": 1, "id": WORLD_ID, "name": "KW-Test", "slug": "kw-test"}])
    write_jsonl(nodes / "world_axiom.jsonl",
                [{"_nid": 10 + i, "id": f"worldaxiom:{i}", "text": text, "severity": "hard"}
                 for i, text in enumerate(axioms)])
    write_jsonl(root / "Graph" / "edges.jsonl",
                [{"type": "PART_OF_WORLD", "source": 10 + i, "target": 1}
                 for i in range(len(axioms))])
    return root


def pairs_for(root: Path) -> list[dict]:
    return wc.report(root)["worlds"][0]["pairs"]


def test_words_and_motifs_handle_german(tmp_path):
    tokens = wc.words("Die Temperatur in KW1 ist konstant 21°C; keine Abweichung.")
    assert "temperatur" in tokens and "keine" in tokens
    kept = wc.motifs(tokens)
    assert "temperatur" in kept
    assert "die" not in kept and "ist" not in kept      # stopwords
    assert "keine" not in kept                           # negations are not motifs
    assert "in" not in kept                              # below the length floor


def test_a_negated_and_an_affirmed_axiom_sharing_rare_motifs_are_flagged(tmp_path):
    root = build(tmp_path, [
        "Coheronen sind atemporal und unzerstörbar im Substrat.",
        "Coheronen sind nicht atemporal, sobald das Substrat kollabiert.",
    ])
    found = pairs_for(root)
    assert len(found) == 1
    assert {"coheronen", "atemporal", "substrat"} & set(found[0]["shared"])


def test_two_affirmed_axioms_are_not_flagged(tmp_path):
    root = build(tmp_path, [
        "Coheronen sind atemporal und unzerstörbar im Substrat.",
        "Coheronen bilden das atemporale Substrat der Kohärenz.",
    ])
    assert pairs_for(root) == []


def test_two_negated_axioms_are_not_flagged(tmp_path):
    root = build(tmp_path, [
        "Coheronen sind nicht atemporal im kollabierten Substrat.",
        "Coheronen sind keine Träger des atemporalen Substrats.",
    ])
    assert pairs_for(root) == []


def test_a_shared_common_word_is_not_enough(tmp_path):
    """A motif that appears across the corpus carries no signal."""
    common = ["Die Welt reagiert auf Abweichung.",
              "Die Welt kennt Abweichung als Vorzeichen.",
              "Die Welt speichert Abweichung im Protokoll.",
              "Die Welt hat keine Abweichung ohne Ursache."]
    root = build(tmp_path, common)
    assert pairs_for(root) == []


def test_one_rare_shared_motif_is_below_the_threshold(tmp_path):
    root = build(tmp_path, [
        "Erasonen erzeugen den Zeitpfeil.",
        "Erasonen erzeugen keinen Zeitpfeil ohne Löschung.",
    ])
    found = pairs_for(root)
    assert all(len(p["shared"]) >= wc.MIN_RARE_SHARED for p in found)


def test_motif_frequency_counts_axioms_not_occurrences(tmp_path):
    axioms = [{"text": "Substrat Substrat Substrat"}, {"text": "Substrat Kohärenz"}]
    frequency = wc.motif_frequency(axioms)
    assert frequency["substrat"] == 2 and frequency["kohärenz"] == 1


def test_candidate_pairs_respects_the_frequency_argument():
    axioms = [{"id": "a", "text": "Kohärenz ist reversibel im Kernel."},
              {"id": "b", "text": "Kohärenz ist nicht reversibel im Kernel."}]
    rare = wc.candidate_pairs(axioms, Counter({"kohärenz": 1, "reversibel": 1, "kernel": 1}))
    common = wc.candidate_pairs(axioms, Counter({"kohärenz": 99, "reversibel": 99, "kernel": 99}))
    assert len(rare) == 1 and common == []


def test_orphan_axioms_are_counted(tmp_path):
    root = build(tmp_path, ["Ein Axiom ohne Bezug."])
    write_jsonl(root / "Graph" / "nodes" / "world_axiom.jsonl",
                [{"_nid": 10, "id": "worldaxiom:0", "text": "Ein Axiom.", "severity": "hard"},
                 {"_nid": 99, "id": "worldaxiom:orphan", "text": "Frei schwebend.", "severity": "soft"}])
    assert wc.report(root)["orphan_axioms"] == 1


def test_world_filter_matches_slug_and_name(tmp_path):
    root = build(tmp_path, ["Ein Axiom."])
    assert len(wc.report(root, "kw-test")["worlds"]) == 1
    assert len(wc.report(root, "KW-Test")["worlds"]) == 1
    assert wc.report(root, "nirgendwo")["worlds"] == []


def test_the_real_corpus_stays_narrow():
    """The scan must narrow 111 axioms to a readable set, not flag everything."""
    data = wc.report(ROOT)
    assert sum(w["axioms"] for w in data["worlds"]) == 111
    assert 0 < data["flagged"] <= 15
    assert data["orphan_axioms"] == 0


def test_cli_exit_codes(capsys):
    assert wc.main([]) == wc.EXIT_OK
    assert wc.main(["--strict"]) == wc.EXIT_FLAGGED
    assert wc.main(["--world", "nirgendwo"]) == wc.EXIT_CANNOT_RUN
    assert "no world matches" in capsys.readouterr().err


def test_cli_json_shape(capsys):
    wc.main(["--json", "--world", "kw1"])
    data = json.loads(capsys.readouterr().out)
    assert data["worlds"][0]["slug"].startswith("kw1") and "flagged" in data
