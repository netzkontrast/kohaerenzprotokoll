"""Tests for scripts/audit_graph_claims.py on a tiny sqlite graph built in tmp_path."""
from __future__ import annotations

import json
import sqlite3
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


def build_db(path: Path, key_column: str = "name", with_uri_key: bool = True) -> Path:
    con = sqlite3.connect(path)
    con.executescript(f"""
        CREATE TABLE nodes (id INTEGER PRIMARY KEY);
        CREATE TABLE node_labels (node_id INTEGER, label TEXT, PRIMARY KEY (node_id, label));
        CREATE TABLE node_props_text (node_id INTEGER, key_id INTEGER, value TEXT, PRIMARY KEY (node_id, key_id));
        CREATE TABLE property_keys (id INTEGER PRIMARY KEY, {key_column} TEXT UNIQUE NOT NULL);
    """)
    con.execute(f"INSERT INTO property_keys VALUES (1, 'text')")
    if with_uri_key:
        con.execute(f"INSERT INTO property_keys VALUES (2, 'source_uri')")
    for node_id, uri in CLAIMS.items():
        con.execute("INSERT INTO nodes VALUES (?)", (node_id,))
        con.execute("INSERT INTO node_labels VALUES (?, 'NovelClaim')", (node_id,))
        con.execute("INSERT INTO node_props_text VALUES (?, 1, 'claim text')", (node_id,))
        if uri is not None:
            con.execute("INSERT INTO node_props_text VALUES (?, 2, ?)", (node_id, uri))
    con.execute("INSERT INTO nodes VALUES (99)")
    con.execute("INSERT INTO node_labels VALUES (99, 'Chapter')")
    con.execute("INSERT INTO node_props_text VALUES (99, 2, 'Wiki/not-a-claim.md')")
    con.commit()
    con.close()
    return path


@pytest.fixture
def db(tmp_path: Path) -> Path:
    return build_db(tmp_path / "session.db")


def test_counts_per_class(db):
    report = audit.audit(db)
    assert report["claims"] == 6
    assert report["counts"] == {"canon": 1, "sources": 1, "wiki": 1, "other": 1, "empty": 2}


def test_violations_list_ids_and_uris(db):
    report = audit.audit(db)
    assert report["violations"] == [{"id": 3, "source_uri": "Wiki/concepts/schleier.md"}]
    assert [item["id"] for item in report["empty"]] == [5, 6]
    assert report["other"][0]["source_uri"] == "https://example.org/paper"


def test_non_claim_nodes_are_ignored(db):
    assert all(item["id"] != 99 for item in audit.audit(db)["violations"])


def test_main_exits_1_on_wiki_violation(db, capsys):
    assert audit.main(["--db", str(db)]) == audit.EXIT_VIOLATION
    out = capsys.readouterr().out
    assert "wiki          1" in out and "node 3: Wiki/concepts/schleier.md" in out


def test_main_exits_0_without_violation(tmp_path, capsys):
    db = build_db(tmp_path / "clean.db")
    with sqlite3.connect(db) as con:
        con.execute("DELETE FROM node_labels WHERE node_id = 3")
    assert audit.main(["--db", str(db)]) == audit.EXIT_OK
    assert "no claim points into Wiki/" in capsys.readouterr().out


def test_json_output(db, capsys):
    audit.main(["--db", str(db), "--json"])
    report = json.loads(capsys.readouterr().out)
    assert report["counts"]["canon"] == 1 and report["violations"][0]["id"] == 3


def test_key_column_named_key_is_discovered(tmp_path):
    db = build_db(tmp_path / "key.db", key_column="key")
    assert audit.audit(db)["counts"]["wiki"] == 1


def test_missing_source_uri_key_exits_2(tmp_path, capsys):
    db = build_db(tmp_path / "nokey.db", with_uri_key=False)
    assert audit.main(["--db", str(db)]) == audit.EXIT_CANNOT_RUN
    assert "no property key 'source_uri'" in capsys.readouterr().err


def test_missing_table_exits_2(tmp_path, capsys):
    db = tmp_path / "bare.db"
    with sqlite3.connect(db) as con:
        con.execute("CREATE TABLE nodes (id INTEGER PRIMARY KEY)")
    assert audit.main(["--db", str(db)]) == audit.EXIT_CANNOT_RUN
    assert "missing tables" in capsys.readouterr().err


def test_missing_database_exits_2(tmp_path):
    assert audit.main(["--db", str(tmp_path / "absent.db")]) == audit.EXIT_CANNOT_RUN


def test_database_is_opened_read_only(db):
    con = audit.connect_readonly(db)
    with pytest.raises(sqlite3.OperationalError):
        con.execute("INSERT INTO nodes VALUES (500)")
    con.close()


def test_classify_prefixes():
    assert audit.classify("Canon/x.md") == "canon" and audit.classify("Sources/drive/x.md") == "sources"
    assert audit.classify("Wiki/x.md") == "wiki" and audit.classify("canon/x.md") == "other"
    assert audit.classify("") == "empty"
