"""Exercise GraphQLite's real extension offline, with disposable graph fixtures.

    .venv-graphqlite/bin/python scripts/kg_selftest.py
"""
import copy
import tempfile
import unittest
from pathlib import Path
from unittest.mock import patch

import kg


def fixture():
    return {"nodes": {
        "term:a": {"id": "term:a", "type": "term", "slug": "a", "term": "AEGIS", "surfaces": ["AEGIS"]},
        "doc:d": {"id": "doc:d", "type": "doc", "slug": "d", "title": "Quelle"}},
        "edges": [
            {"source": "term:a", "target": "doc:d", "type": "reads", "via": "Wiki/candidates/a.md:2"},
            {"source": "term:a", "target": "doc:d", "type": "cites", "via": "Wiki/candidates/a.md:8", "lines": [12]}],
        "evidence": {"a": [{"quote": "AEGIS hält die Tür offen.", "page_line": 8, "section": "Reading — d",
                            "ref": "d.md:L12", "doc": "d", "line": 12, "status": "verified"}]}}


class Integration(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.db = self.root / "graph.db"
        self.graph = fixture()
        self.hashes = kg.inputs(self.root)
        kg.publish(self.graph, self.db, self.hashes)

    def tearDown(self):
        self.tmp.cleanup()

    def test_native_roundtrip_preserves_parallel_edges_and_evidence(self):
        self.assertEqual(kg.read_graph(self.db), self.graph)
        self.assertEqual(list(kg.read_graph(self.db)["nodes"]), list(self.graph["nodes"]))
        g = kg.engine(str(self.db))
        try:
            rows = g.query("MATCH (a:Core)-[r]->(b:Core) RETURN type(r) AS kind ORDER BY kind")
            self.assertEqual([r["kind"] for r in rows], ["CITES", "READS"])
            derived = g.query("MATCH (a)-[r:HAS_EVIDENCE]->(b) RETURN r.via AS via")
            self.assertEqual(derived, [{"via": "Wiki/candidates/a.md:8"}])
        finally:
            g.close()

    def test_native_roundtrip_preserves_double_digit_edge_order(self):
        graph = copy.deepcopy(self.graph)
        graph["edges"] = [dict(graph["edges"][i % 2], via=f"Wiki/candidates/a.md:{i}") for i in range(13)]
        kg.publish(graph, self.db, self.hashes)
        self.assertEqual(kg.read_graph(self.db), graph)

    def test_cypher_traversal_preserves_provenance_and_is_bounded(self):
        result = kg.around(self.db, "term:a", 1, 10)
        self.assertEqual(result["nodes"], {"term:a": 0, "doc:d": 1})
        self.assertEqual({e["via"] for e in result["edges"]}, {e["via"] for e in self.graph["edges"]})
        limited = kg.around(self.db, "term:a", 1, 1)
        self.assertEqual(len(limited["edges"]), 1)
        self.assertTrue(limited["truncated"])
        with self.assertRaises(kg.Refused):
            kg.around(self.db, "term:a') DELETE n //", 1, 10)

    def test_search_and_evidence_ids(self):
        results = kg.search(self.db, 'Tür " OR DELETE', 10)["evidence"]
        self.assertEqual(len(results), 1)
        self.assertEqual(kg.evidence(self.db, [results[0]["id"]])["evidence"][0]["quote"], "AEGIS hält die Tür offen.")
        with self.assertRaises(kg.Refused):
            kg.evidence(self.db, ["invented"])

    def test_context_reuses_retriever_and_returns_indexed_ids(self):
        with patch("graph.proposals", return_value={"nodes": {}, "edges": [], "glosses": []}):
            result = kg.context(self.db, "AEGIS", 2000)
        key = kg.search(self.db, "AEGIS", 10)["evidence"][0]["id"]
        self.assertEqual(result["evidence"][0]["id"], key)
        self.assertEqual(result["evidence"][0]["quote"], self.graph["evidence"]["a"][0]["quote"])
        self.assertLessEqual(len(kg.compact(result).encode()) + 1, 2000)

    def test_unverified_quotes_never_become_search_evidence(self):
        graph = copy.deepcopy(self.graph)
        graph["evidence"]["a"][0]["status"] = "unresolved"
        kg.publish(graph, self.db, self.hashes)
        self.assertEqual(kg.search(self.db, "AEGIS", 10)["evidence"], [])
        key = next(iter(kg.evidence_rows(graph)))
        with self.assertRaises(kg.Refused):
            kg.evidence(self.db, [key])

    def test_added_changed_deleted_source_invalidates_snapshot(self):
        path = self.root / "Sources/drive/d.md"
        path.parent.mkdir(parents=True)
        path.write_text("Original")
        with self.assertRaises(kg.Refused):
            kg.freshness(self.db, self.root)
        kg.publish(self.graph, self.db, kg.inputs(self.root))
        kg.freshness(self.db, self.root)
        path.write_text("Changed")
        with self.assertRaises(kg.Refused):
            kg.freshness(self.db, self.root)
        kg.publish(self.graph, self.db, kg.inputs(self.root))
        path.unlink()
        with self.assertRaises(kg.Refused):
            kg.freshness(self.db, self.root)

    def test_one_freshness_record(self):
        """SPEC.md step 3: the store keeps its inputs once (askdb's stats.input_hash), and kg.py reads that record.
        Before, kp_meta held the inputs a second time and kg.py read only that copy: a store whose stats record
        said stale passed kg.py's check."""
        import askdb
        import sqlite3
        self.assertNotIn("inputs", kg.metadata(self.db))
        kg.freshness(self.db, self.root)
        conn = sqlite3.connect(str(self.db))
        stats = askdb.stats(self.db)
        conn.execute("UPDATE meta SET value=? WHERE key='stats'", (askdb.compact(dict(stats, input_hash="other")),))
        conn.commit()
        conn.close()
        with self.assertRaises(kg.Refused):
            kg.freshness(self.db, self.root)
        self.assertEqual(kg.evidence_rows(self.graph), askdb.evidence_rows(self.graph))

    def test_failed_rebuild_leaves_previous_database_intact(self):
        before = self.db.read_bytes()
        with patch("askdb._graphqlite", side_effect=RuntimeError("fixture failure")):
            with self.assertRaises(RuntimeError):
                kg.publish(self.graph, self.db, {})
        self.assertEqual(self.db.read_bytes(), before)
        self.assertEqual(list(self.root.glob(".ask-*")), [])

    def test_unchanged_index_does_not_build_graph(self):
        with patch("askdb.inputs", return_value=self.hashes), patch("graph.build", side_effect=AssertionError("must not rebuild")):
            self.assertEqual(kg.index(self.db)["status"], "unchanged")

    def test_edit_during_publication_keeps_previous_snapshot(self):
        import askdb
        core = self.graph
        data = askdb.with_core({"nodes": {k: ({}, n["type"].capitalize()) for k, n in core["nodes"].items()},
            "edges": [(e["source"], e["target"], {"via": e["via"]}, e["type"].upper()) for e in core["edges"]],
            "quotes": []}, core)
        before = self.db.read_bytes()
        with patch.object(askdb, "inputs", return_value={"changed": "during publication"}):
            with self.assertRaisesRegex(ValueError, "inputs changed"):
                askdb.publish(data, self.db, self.hashes, [], verify_inputs=True)
        self.assertEqual(self.db.read_bytes(), before)
        self.assertEqual(list(self.root.glob(".ask-*")), [])

    def test_evidence_uses_the_reference_that_actually_verified(self):
        import graph
        text = '„Zitat“ ^[bad.md:L1] ^[good.md:L2]'
        with patch("quotes.resolve", side_effect=lambda raw, default, quote: None if raw == "good.md:L2" else "wrong"):
            rows = graph.evidence_of(Path("Wiki/candidates/fixture.md"), text)
        self.assertEqual(rows[0]["status"], "verified")
        self.assertEqual((rows[0]["doc"], rows[0]["line"], rows[0]["ref"]), ("good", 2, "good.md:L2"))

    def test_one_node_has_typed_and_core_labels(self):
        import askdb
        self.assertEqual(kg.DATABASE, askdb.DB)
        g = kg.engine(str(self.db))
        try:
            self.assertEqual(g.query("MATCH (n:Term:Core) RETURN n.id AS id"), [{"id": "term:a"}])
        finally:
            g.close()

    def test_tampered_properties_detected_without_count_change(self):
        import askdb, sqlite3
        with sqlite3.connect(self.db) as conn:
            before = askdb.storage_hash(conn)
            conn.execute("UPDATE edge_props_text SET value='changed provenance' WHERE value LIKE 'Wiki/%'")
            self.assertNotEqual(askdb.storage_hash(conn), before)

    def test_proposals_do_not_change_path_or_core_ranking(self):
        import askdb
        g = kg.engine(str(self.db))
        g.insert_graph_bulk([("entity:guess", {}, "Entity")], [("term:a", "entity:guess", {}, "P_NAMED_IN"), ("entity:guess", "doc:d", {}, "P_NAMED_IN")])
        g.close()
        store = askdb.Store(self.db, stale_ok=True)
        try:
            self.assertEqual(store.path("term:a", "doc:d")["path"], ["term:a", "doc:d"])
            self.assertEqual(store.path("term:a", "entity:guess")["path"], [])
            self.assertNotIn("entity:guess", dict(store.ppr(["term:a"])))
            self.assertNotIn("entity:guess", store.communities())
            with self.assertRaises(Exception):
                store.cypher("CREATE (n:Term {id:'term:unauthorized'})")
        finally:
            store.close()

    def test_context_budget_keeps_conflicts_and_whole_quotes(self):
        pack = {"query": "AEGIS", "seeds": [], "terms": [], "conflicts": [{"id": "C1"}], "questions": [],
                "evidence": [{"doc": "d", "line": 12, "quote": "x" * 10000},
                             {"doc": "d", "line": 13, "quote": "kurz"}]}
        result = kg.bounded_context(pack, 400)
        self.assertLessEqual(len(kg.compact(result).encode()), 400)
        self.assertEqual(result["conflicts"], pack["conflicts"])
        self.assertEqual([e["quote"] for e in result["evidence"]], ["kurz"])
        self.assertTrue(result["incomplete"])
        with self.assertRaises(kg.Refused):
            kg.bounded_context(pack, 5)


if __name__ == "__main__":
    unittest.main(verbosity=2)
