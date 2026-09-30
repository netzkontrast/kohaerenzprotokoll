"""Real GraphQLite snapshot round-trips and refusal tests, offline."""
import json
from pathlib import Path
import sqlite3
import subprocess
import os
import tempfile
import unittest
from unittest.mock import patch

import askdb
import graph_snapshot as snapshot
import kg
from kg_selftest import fixture


class Snapshot(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        self.db = self.root / "original.db"
        self.out = self.root / "restored.db"
        self.directory = self.root / "Graph"
        self.graph = fixture()
        kg.publish(self.graph, self.db, {})
        self.hashes = patch.object(askdb, "inputs", return_value={})
        self.sources = patch.object(askdb, "manifest", return_value=[])
        self.hashes.start()
        self.sources.start()

    def tearDown(self):
        self.hashes.stop()
        self.sources.stop()
        self.tmp.cleanup()

    def export(self):
        return snapshot.export(self.db, self.directory)

    def test_native_roundtrip_preserves_graph_search_labels_and_types(self):
        result = self.export()
        restored = snapshot.restore(self.out, self.directory)
        self.assertEqual(restored["status"], "restored")
        self.assertEqual(kg.read_graph(self.out), self.graph)
        self.assertEqual(kg.search(self.out, "AEGIS", 10), kg.search(self.db, "AEGIS", 10))
        self.assertEqual(kg.around(self.out, "term:a", 1, 10), kg.around(self.db, "term:a", 1, 10))
        other = snapshot.export(self.out, self.root / "Second")
        self.assertEqual(result["logical_sha256"], other["logical_sha256"])
        self.assertNotIn("lines", result["counts"])
        self.assertIn("term:a", (self.directory / "index.md").read_text())
        self.assertNotIn("AEGIS hält", (self.directory / "index.md").read_text())

    def test_deterministic_export(self):
        first = self.export()
        self.assertEqual(first["sha256"], self.export()["sha256"])

    def test_stale_snapshot_does_not_replace_existing_database(self):
        self.export()
        before = self.db.read_bytes()
        with patch.object(askdb, "inputs", return_value={"changed": "source"}):
            with self.assertRaisesRegex(ValueError, "inputs"):
                snapshot.restore(self.db, self.directory)
        self.assertEqual(self.db.read_bytes(), before)

    def test_corrupt_archive_does_not_replace_database(self):
        result = self.export()
        archive = self.directory / result["snapshot"]
        archive.write_bytes(archive.read_bytes()[:-10])
        before = self.db.read_bytes()
        with self.assertRaisesRegex(ValueError, "checksum"):
            snapshot.restore(self.db, self.directory)
        self.assertEqual(self.db.read_bytes(), before)

    def test_wrong_schema_is_refused(self):
        self.export()
        path = self.directory / "manifest.json"
        manifest = json.loads(path.read_text())
        manifest["version"] = -1
        path.write_text(json.dumps(manifest))
        with self.assertRaisesRegex(ValueError, "version"):
            snapshot.restore(self.out, self.directory)
        self.assertFalse(self.out.exists())

    def test_failure_during_restore_preserves_old_database_and_cleans_stage(self):
        self.export()
        before = self.db.read_bytes()
        with patch.object(snapshot, "records", side_effect=RuntimeError("fixture failure")):
            with self.assertRaises(RuntimeError):
                snapshot.restore(self.db, self.directory)
        self.assertEqual(self.db.read_bytes(), before)
        self.assertEqual(list(self.root.glob(".restore-*")), [])

    def test_inputs_change_during_restore_does_not_publish(self):
        self.export()
        before = self.db.read_bytes()
        with patch.object(askdb, "inputs", side_effect=[{}, {"changed": "during restore"}]):
            with self.assertRaisesRegex(ValueError, "inputs changed"):
                snapshot.restore(self.db, self.directory)
        self.assertEqual(self.db.read_bytes(), before)

    def test_session_hook_initializes_local_and_remote_before_work(self):
        scripts = self.root / "scripts"
        scripts.mkdir()
        (scripts / "knowledge.py").write_text("import sys; from pathlib import Path; Path('started').write_text(' '.join(sys.argv[1:])); print('initialized')")
        hook = askdb.ROOT / ".claude/hooks/session-start.sh"
        for remote in ("false", "true"):
            done = subprocess.run(["bash", str(hook)], env={"PATH": os.environ["PATH"], "HOME": os.environ["HOME"],
                "CLAUDE_PROJECT_DIR": str(self.root), "CLAUDE_CODE_REMOTE": remote}, capture_output=True, text=True)
            self.assertEqual(done.returncode, 0)
            self.assertEqual((self.root / "started").read_text(), "init --profile research")
            self.assertIn("initialized", done.stdout)

    def test_index_restores_without_deriving(self):
        self.export()
        with patch.object(snapshot, "DIRECTORY", self.directory):
            # Defaults are bound at definition time; patch the adapter explicitly.
            real_restore = snapshot.restore
            with patch.object(snapshot, "restore", side_effect=lambda db: real_restore(db, self.directory)), patch.object(askdb, "build", side_effect=AssertionError("must restore")):
                self.assertEqual(kg.index(self.out)["status"], "restored")

    def test_missing_snapshot_falls_back_to_builder(self):
        with patch.object(snapshot, "restore", side_effect=FileNotFoundError("missing snapshot")), patch.object(askdb, "build", return_value={"status": "rebuilt"}), patch.object(kg, "metadata", return_value={}):
            self.assertEqual(kg.index(self.out)["status"], "rebuilt")


if __name__ == "__main__":
    unittest.main(verbosity=2)
