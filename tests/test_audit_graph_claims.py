"""Tests for scripts/audit_graph_claims.py on a tiny Graph/ tree built in tmp_path."""
from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

import audit_graph_claims as audit  # noqa: E402

CLAIMS = {
    1: "Canon/kohaerenz-protokoll_begriffe-und-konzepte_2026-06-10.md",
    2: "Sources/drive/monstergruppe.md",
    3: "Wiki/concepts/schleier.md",
    4: "https://example.org/paper",
    5: "",
    6: None,
}


def write_jsonl(path: Path, records: list[dict]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text("".join(json.dumps(r, ensure_ascii=False, sort_keys=True) + "\n"
                            for r in records), encoding="utf-8")


def build_graph(root: Path, claims: dict[int, str | None] | None = None) -> Path:
    """A repository root whose Graph/ holds the claims plus one non-claim node."""
    nodes = root / "Graph" / "nodes"
    records = []
    for nid, uri in (CLAIMS if claims is None else claims).items():
        record = {"_nid": nid, "id": f"novelclaim:{nid:08x}", "text": "claim text"}
        if uri is not None:
            record["source_uri"] = uri
        records.append(record)
    write_jsonl(nodes / "novel_claim.jsonl", records)
    # A Chapter carrying a Wiki/ uri must not be counted as a claim.
    write_jsonl(nodes / "chapter.jsonl",
                [{"_nid": 99, "id": "chapter:99", "number": 1, "title": "K",
                  "source_uri": "Wiki/not-a-claim.md"}])
    write_jsonl(root / "Graph" / "edges.jsonl", [])
    return root


@pytest.fixture
def graph_root(tmp_path: Path) -> Path:
    return build_graph(tmp_path)


def test_counts_per_class(graph_root):
    report = audit.audit(graph_root)
    assert report["claims"] == 6
    assert report["counts"] == {"canon": 1, "sources": 1, "wiki": 1, "other": 1, "empty": 2}


def test_violations_list_ids_and_uris(graph_root):
    report = audit.audit(graph_root)
    assert report["violations"] == [{"id": 3, "source_uri": "Wiki/concepts/schleier.md"}]
    assert [item["id"] for item in report["empty"]] == [5, 6]
    assert report["other"][0]["source_uri"] == "https://example.org/paper"


def test_non_claim_nodes_are_ignored(graph_root):
    assert all(item["id"] != 99 for item in audit.audit(graph_root)["violations"])


def test_main_exits_1_on_wiki_violation(graph_root, capsys):
    assert audit.main(["--root", str(graph_root)]) == audit.EXIT_VIOLATION
    out = capsys.readouterr().out
    assert "wiki          1" in out and "node 3: Wiki/concepts/schleier.md" in out


def test_main_exits_0_without_violation(tmp_path, capsys):
    clean = {nid: uri for nid, uri in CLAIMS.items() if nid != 3}
    root = build_graph(tmp_path / "clean", claims=clean)
    assert audit.main(["--root", str(root)]) == audit.EXIT_OK
    assert "no claim points into Wiki/" in capsys.readouterr().out


def test_json_output(graph_root, capsys):
    audit.main(["--root", str(graph_root), "--json"])
    report = json.loads(capsys.readouterr().out)
    assert report["counts"]["canon"] == 1 and report["violations"][0]["id"] == 3


def test_missing_graph_exits_2(tmp_path, capsys):
    assert audit.main(["--root", str(tmp_path / "absent")]) == audit.EXIT_CANNOT_RUN
    assert "no graph at" in capsys.readouterr().err


def test_missing_claim_file_exits_2(tmp_path, capsys):
    (tmp_path / "Graph" / "nodes").mkdir(parents=True)
    assert audit.main(["--root", str(tmp_path)]) == audit.EXIT_CANNOT_RUN
    assert "missing" in capsys.readouterr().err


def test_malformed_record_exits_2(tmp_path, capsys):
    root = build_graph(tmp_path)
    (root / "Graph" / "nodes" / "novel_claim.jsonl").write_text("{not json}\n", encoding="utf-8")
    assert audit.main(["--root", str(root)]) == audit.EXIT_CANNOT_RUN
    assert "novel_claim.jsonl:1" in capsys.readouterr().err


def test_the_audit_writes_nothing(graph_root):
    before = {p: p.read_bytes() for p in (graph_root / "Graph").rglob("*.jsonl")}
    audit.audit(graph_root)
    assert {p: p.read_bytes() for p in (graph_root / "Graph").rglob("*.jsonl")} == before


def test_classify_prefixes():
    assert audit.classify("Canon/x.md") == "canon" and audit.classify("Sources/drive/x.md") == "sources"
    assert audit.classify("Wiki/x.md") == "wiki" and audit.classify("canon/x.md") == "other"
    assert audit.classify("") == "empty"
