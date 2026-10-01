import hashlib
import json
import re
import shutil
import tempfile
import unittest
from pathlib import Path
import numpy as np
from novelgraph import repo
from novelgraph.chunking import make_chunks, sha
from novelgraph.index import Index
from novelgraph.search import Search
from novelgraph.verify import verify


class FakeEmbedder:
    """Offline fixture, never used or reported as production embedding quality."""
    calls = []

    def __init__(self, config, offline=False):
        pass

    def count(self, text):
        return len(re.findall(r"\w+|[^\w\s]", text))

    def encode(self, texts):
        self.calls.extend(texts)
        vectors = []
        for text in texts:
            v = np.zeros(16, dtype=np.float32)
            for w in re.findall(r"\w+", text):
                v[int(hashlib.sha1(w.encode()).hexdigest()[:4], 16) % 16] += 1
            norm = np.linalg.norm(v)
            vectors.append(v / norm if norm else v)
        return np.array(vectors, dtype=np.float16).reshape(len(texts), 16)


class Tests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.root = Path(self.tmp.name)
        (self.root / "Sources/drive").mkdir(parents=True)
        (self.root / "Index").mkdir()
        shutil.copy(repo.ROOT / "Index/methods.toml", self.root / "Index/methods.toml")
        self.rows = []
        for slug, text in (("a", "---\ntitle: A\n---\n# A\n\nKael zählt.\n\n## Change\n\nJuna wartet.\n"),
                           ("b", "# B\n\nAEGIS löscht.\n")):
            (self.root / "Sources/drive" / (slug + ".md")).write_text(text)
            self.rows.append(dict(slug=slug, title=slug.upper(), export_path=f"Sources/drive/{slug}.md", sha256=sha(text)))
        self.save_manifest()
        FakeEmbedder.calls = []
        self.index = Index(self.root, embedder_factory=FakeEmbedder)

    def tearDown(self):
        self.tmp.cleanup()

    def save_manifest(self):
        repo.write_jsonl(self.root / "Sources/manifest.jsonl", self.rows)

    def test_build_rebuild_force_and_single_change(self):
        first = self.index.build()
        self.assertEqual(first["changed_sources"], 2)
        self.assertTrue(verify(self.index)["ok"])
        second = self.index.build()
        self.assertEqual(second["embedded_chunks"], 0)
        self.assertEqual(second["skipped_sources"], 2)
        forced = self.index.build(force=True)
        self.assertEqual(forced["embedded_chunks"], 0)
        p = self.root / self.rows[0]["export_path"]
        text = p.read_text().replace("Juna wartet.", "Juna geht.")
        p.write_text(text)
        self.rows[0]["sha256"] = sha(text)
        self.save_manifest()
        changed = self.index.build()
        self.assertEqual(changed["changed_sources"], 1)
        self.assertEqual(changed["skipped_sources"], 1)
        self.assertGreater(changed["embedded_chunks"], 0)
        self.assertTrue(verify(self.index)["ok"])

    def test_missing_coverage_is_failure(self):
        self.index.build(source="a")
        self.assertFalse(verify(self.index)["ok"])
        with self.assertRaisesRegex(ValueError, "coverage"):
            Search(self.index)

    def test_source_change_refused(self):
        self.index.build()
        engine = Search(self.index)
        (self.root / "Sources/drive/a.md").write_text("changed")
        with self.assertRaises(ValueError):
            engine.query("Kael", mode="bm25")
        engine.close()
        with self.assertRaises(ValueError):
            self.index.build()
        self.assertFalse(verify(self.index)["ok"])

    def test_corrupt_id_and_vectors_are_caught(self):
        self.index.build()
        cp = self.root / "Index/sources/a/chunks/heading@v1.jsonl"
        cs = repo.read_jsonl(cp)
        cs[0]["id"] = "bad"
        repo.write_jsonl(cp, cs)
        self.assertFalse(verify(self.index)["ok"])
        self.index.build(force=True)
        vp = self.root / "Index/_build/heading@v1~potion-m128.f16.npy"
        matrix = np.load(vp)
        matrix[0, 0] = .123
        np.save(vp, matrix)
        self.assertFalse(verify(self.index)["ok"])

    def test_deleted_manifest_source_not_aggregated(self):
        self.index.build()
        self.rows.pop()
        self.save_manifest()
        self.index.build()
        self.assertTrue(verify(self.index)["ok"])
        rows = repo.read_jsonl(self.root / "Index/_build/heading@v1~potion-m128.rows.jsonl")
        self.assertEqual({r["slug"] for r in rows}, {"a"})

    def test_search_and_rrf(self):
        self.index.build()
        s = Search(self.index)
        for mode in ("bm25", "vec", "hybrid"):
            hits = s.query("Kael", mode=mode)
            self.assertTrue(hits)
            self.assertLessEqual(len(hits), 8)
        self.assertEqual(s.query("", mode="bm25"), [])
        s.close()

    def test_all_chunkers_offsets_tables_fences_and_fields(self):
        text = "---\ntitle: test\n---\n# Heading\n\nOne sentence.\n\n|a|b|\n|--|--|\n|v|x|\n\n```\n# not a heading\ncode\n```\n\n## Next\n\nLast sentence."
        for method in self.index.config["chunkers"]:
            cs, tree = make_chunks("a", "Title", text, method, self.index.config["chunkers"][method], FakeEmbedder({}, False).count)
            self.assertEqual([h["line"] for h in tree], [4, 17])
            self.assertTrue(all(c["line_start"] >= 4 for c in cs))
            self.assertTrue(any(c["line_start"] <= 8 and c["line_end"] >= 10 for c in cs))
            self.assertTrue(any(c["line_start"] <= 12 and c["line_end"] >= 15 for c in cs))
            self.assertTrue(all(set(c) == {"id", "line_start", "line_end", "heading_path", "sha", "tokens", "prefix"} for c in cs))


if __name__ == "__main__":
    unittest.main()
