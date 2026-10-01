"""Warm CPU search over a read-only FTS5 snapshot and float16 mmap."""
import fcntl
import json
import re
import sqlite3
import numpy as np
from .index import EMBEDDER, read_json, sha
from . import repo


class Search:
    def __init__(self, index, method="heading@v1", vectors=True):
        self.index, self.method = index, method
        path = index.path / "_build"
        # Writers and readers cannot observe a mixed publication generation.
        with (index.path / ".lock").open("a") as lock:
            fcntl.flock(lock, fcntl.LOCK_SH)
            self.db = sqlite3.connect(f"file:{path / (method + '.bm25.sqlite')}?mode=ro", uri=True)
            self.meta = json.loads(self.db.execute("SELECT payload FROM metadata").fetchone()[0])
            if self.meta["signature"] != index.fingerprint(method):
                self.db.close()
                raise ValueError("stale build settings or implementation; run novelgraph build")
            self.rows = repo.read_jsonl(path / (method + "~" + EMBEDDER + ".rows.jsonl"))
            self.matrix = np.load(path / (method + "~" + EMBEDDER + ".f16.npy"), mmap_mode="r", allow_pickle=False) if vectors else None
            self.items = [json.loads(r[0]) for r in self.db.execute("SELECT payload FROM chunks ORDER BY rowid")]
            if len(self.rows) != len(self.items) or (vectors and len(self.matrix) != len(self.rows)):
                self.close()
                raise ValueError("matrix/FTS/row count mismatch; run verify")
            if self.rows != [dict(slug=c["slug"], chunk_id=c["id"]) for c in self.items]:
                self.close()
                raise ValueError("row order mismatch; run verify")
        self.positions = {(c["slug"], c["id"]): i for i, c in enumerate(self.items)}
        self.source_paths = {r["slug"]: index.root / r["export_path"] for r in repo.sources(index.root) if r.get("export_path")}
        if set(self.source_paths) != set(self.meta["inputs"]):
            self.close()
            raise ValueError("incomplete or stale source coverage; build the full corpus")
        self.stamps = {}
        # Once per warm session. Subsequent queries check stat identity, never hash the corpus again.
        for slug, expected in self.meta["inputs"].items():
            p = self.source_paths[slug]
            if sha(p.read_text(encoding="utf-8")) != expected["sha256"]:
                self.close()
                raise ValueError(f"stale source {slug}; run build")
            self.stamps[slug] = self.stamp(p)

    @staticmethod
    def stamp(p):
        s = p.stat()
        return s.st_mtime_ns, s.st_ctime_ns, s.st_size, s.st_ino

    def close(self):
        self.db.close()

    def query(self, text, k=8, mode="hybrid"):
        if k < 1:
            raise ValueError("k must be positive")
        if mode not in ("bm25", "vec", "hybrid"):
            raise ValueError("invalid search mode")
        if any(self.stamp(p) != self.stamps[slug] for slug, p in self.source_paths.items()):
            raise ValueError("sources changed during warm search; rebuild and reopen")
        candidates = self.index.config["retrieval"]["candidates"]
        bm, vec = [], []
        if mode in ("bm25", "hybrid"):
            words = re.findall(r"\w+(?:[-:]\w+)*", text)
            words += [repo.fold(w) for w in words]
            expr = " OR ".join('"' + w + '"' for w in dict.fromkeys(words) if w)
            if expr:
                bm = [(self.positions[(s, c)], -float(score)) for s, c, score in self.db.execute(
                    "SELECT slug,chunk_id,bm25(chunks,1,0.5,0.5) AS score FROM chunks "
                    "WHERE chunks MATCH ? ORDER BY score,slug,chunk_id LIMIT ?", (expr, candidates))]
        if mode in ("vec", "hybrid"):
            if self.matrix is None:
                raise ValueError("search opened without vectors")
            q = self.index.embedder(offline=True).encode([text])[0].astype(np.float32)
            scores = np.empty(len(self.matrix), dtype=np.float32)
            # NumPy's half-precision matmul is slow on many CPUs; bounded float32 blocks.
            for start in range(0, len(self.matrix), 8192):
                scores[start:start + 8192] = self.matrix[start:start + 8192].astype(np.float32) @ q
            order = np.lexsort((np.arange(len(scores)), -scores))[:candidates]
            vec = [(int(i), float(scores[i])) for i in order]
        if mode == "hybrid":
            fused = {}
            constant = self.index.config["retrieval"]["rrf_k"]
            for ranking in (bm, vec):
                for rank, (i, _) in enumerate(ranking, 1):
                    fused[i] = fused.get(i, 0) + 1 / (constant + rank)
            ranking = sorted(fused.items(), key=lambda x: (-x[1], x[0]))[:k]
        else:
            ranking = (bm if mode == "bm25" else vec)[:k]
        results = []
        for i, score in ranking:
            c = self.items[i]
            # Original source slice, never search-index text, supplies the preview.
            lines = self.source_paths[c["slug"]].read_text(encoding="utf-8").split("\n")
            preview = "\n".join(lines[c["line_start"] - 1:c["line_end"]])[:200]
            results.append(dict(slug=c["slug"], chunk_id=c["id"], line_start=c["line_start"],
                                line_end=c["line_end"], score=score, heading_path=c["heading_path"], preview=preview))
        return results
