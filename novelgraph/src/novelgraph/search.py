"""`novelgraph search`: BM25 (FTS5), vectors (brute force over the memmapped matrix), or both fused by RRF.

No model runs at query time except the static embedder, which is a table lookup
and a mean: that is the whole point of this index against qmd's hybrid query.
A hit is a line range of a source; its text is sliced from the file, never stored.
"""

from __future__ import annotations

import hashlib
import json
import re
import sqlite3
from functools import lru_cache

import numpy as np

from . import build, chunkers, lex, store
from .repo import documents, read_jsonl, refresh_documents, catalogue_stat, query_words

MODES = ("bm25", "vec", "hybrid")


class Stale(SystemExit):
    """The index no longer describes the files: a hit would cite lines that now say something else."""


class Index:
    """One method's `_build/` files, loaded once; every query after the first is warm.

    A hit is an address into a source, so the index refuses to answer when the address could point at other text:
    on opening, every landed source must hash to what the index recorded, the index must cover exactly the landed
    sources, and `_build/` must be the concatenation of the current per-source files (its stamp); during warm use,
    a source whose file changed since opening is re-hashed, and a changed one ends the session.
    """

    @store.reader
    def __init__(self, method: str, embedder: str | None = None):
        self.method = method
        self.embedder = embedder or store.default_embedder()
        refresh_documents()
        self.catalogue = catalogue_stat()
        mp = store.build_matrix(method, self.embedder)
        if not mp.exists():
            raise SystemExit(f"{mp} is missing — run `novelgraph build` first")
        self.paths = self._fresh_sources()
        stamp_p = build.build_stamp_path(method, self.embedder)
        if not stamp_p.exists() or stamp_p.read_text().strip() != build.build_stamp(method, self.embedder)[0]:
            raise Stale(f"_build/ for {method} is not the concatenation of the current index — run `novelgraph build`")
        self.stamp = stamp_p.read_text()
        self.settings = store.method_stamp(), store.embedder_fp(self.embedder)
        self.rows = read_jsonl(store.build_rows(method, self.embedder))
        # float16 on disk, memmapped; widened once, because float16 matmul has no fast CPU path
        self.matrix = np.asarray(np.load(mp, mmap_mode="r"), dtype=np.float32)
        if len(self.rows) != len(self.matrix):
            raise Stale("aggregate row/matrix mismatch — run `novelgraph build --force`")
        self.con = sqlite3.connect(f"{store.build_bm25(method).resolve().as_uri()}?mode=ro", uri=True,
                                   check_same_thread=False)
        reg = store.registry()["search"]
        self.k_rrf, self.cand = reg["rrf_k"], reg["candidates"]

    def _fresh_sources(self) -> dict:
        manifest = {r["slug"]: r["sha256"] for r in read_jsonl(store.MANIFEST)}
        landed = {d.slug: d.path for d in documents()}
        if set(manifest) != set(landed):
            gone, new = sorted(set(manifest) - set(landed)), sorted(set(landed) - set(manifest))
            raise Stale(f"the index covers other sources than are landed (gone {gone[:3]}, new {new[:3]}) — run `novelgraph build`")
        self.seen = {}
        for slug, path in landed.items():
            if hashlib.sha256(path.read_bytes()).hexdigest() != manifest[slug]:
                raise Stale(f"{slug} changed since it was indexed — run `novelgraph build`")
            src = json.loads((store.source_dir(slug) / "source.json").read_text())
            if src.get("title") != (build._title(slug) or {}).get("title", slug):
                raise Stale(f"{slug}'s title changed since it was indexed — run `novelgraph build`")
            self.seen[slug] = _stat(path)
        self.sha = manifest
        return landed

    def check(self, slug: str) -> None:
        """Before a hit from `slug` is shown: unchanged since opening, or re-hashed to the indexed bytes."""
        path = self.paths[slug]
        try:
            stat = _stat(path)
        except OSError as exc:
            raise Stale(f"{slug} is no longer readable — rebuild and reopen") from exc
        if stat != self.seen[slug]:
            if hashlib.sha256(path.read_bytes()).hexdigest() != self.sha[slug]:
                raise Stale(f"{slug} changed during this session — run `novelgraph build` and search again")
            self.seen[slug] = _stat(path)

    # ── the two retrievers ─────────────────────────────────────────────────
    def bm25(self, query: str, n: int) -> list[tuple[int, float]]:
        words = query_words(query)   # the repository's one tokenizer and stop list (askdb.query_words)
        lemmata = lex.query_lemmata(query)
        if not words and not lemmata:
            return []
        q = lambda ws: " OR ".join('"' + w.replace('"', '""') + '"' for w in ws)  # noqa: E731
        parts = []
        if words:
            parts.append(f"text : ({q(words)})")
        if lemmata:
            parts.append(f"lemmata : ({q(lemmata)})")
        sql = ("SELECT rowid, bm25(chunks, 1.0, 1.0) AS s FROM chunks WHERE chunks MATCH ? ORDER BY s LIMIT ?")
        return [(int(r) - 1, -s) for r, s in self.con.execute(sql, (" OR ".join(parts), n))]

    def vec(self, query: str, n: int) -> list[tuple[int, float]]:
        if n <= 0 or len(self.matrix) == 0:
            return []
        q = build.embed(self.embedder, [query]).astype(np.float32)[0]
        scores = self.matrix @ q
        n = min(n, len(scores))
        top = np.argpartition(-scores, n - 1)[:n]
        top = top[np.argsort(-scores[top])]
        return [(int(i), float(scores[i])) for i in top]

    @store.reader
    def search(self, query: str, k: int = 8, mode: str = "hybrid") -> list[dict]:
        if k <= 0:
            raise ValueError("k must be positive")
        if mode not in MODES:
            raise ValueError(f"unknown search mode: {mode}")
        if catalogue_stat() != self.catalogue:
            raise Stale("source catalogue changed during this session — rebuild and reopen")
        store.registry.cache_clear()
        if self.settings != (store.method_stamp(), store.embedder_fp(self.embedder)):
            raise Stale("index settings changed during this session — rebuild and reopen")
        if build.build_stamp_path(self.method, self.embedder).read_text() != self.stamp:
            raise Stale("index was rebuilt during this session — reopen search")
        if {d.slug for d in documents()} != set(self.paths):
            raise Stale("landed sources changed during this session — rebuild and reopen")
        for slug in self.paths:
            self.check(slug)
        if mode == "bm25":
            ranked = self.bm25(query, k)
        elif mode == "vec":
            ranked = self.vec(query, k)
        else:
            fused: dict[int, float] = {}
            for hits in (self.bm25(query, self.cand), self.vec(query, self.cand)):
                for rank, (row, _) in enumerate(hits, 1):
                    fused[row] = fused.get(row, 0.0) + 1.0 / (self.k_rrf + rank)
            ranked = sorted(fused.items(), key=lambda kv: -kv[1])[:k]
        hits = [{**self.rows[r], "score": round(s, 5)} for r, s in ranked]
        for h in hits:
            self.check(h["slug"])
        return hits


def _stat(path) -> tuple:
    st = path.stat()
    return st.st_mtime_ns, st.st_size, st.st_ino


@lru_cache(maxsize=4096)
def _chunk(slug: str, method: str, cid: str) -> dict:
    for r in read_jsonl(store.chunks_path(slug, method)):
        if r["id"] == cid:
            return r
    raise KeyError(cid)


@store.reader
def show(hits: list[dict], method: str) -> str:
    out = []
    for h in hits:
        c = _chunk(h["slug"], method, h["id"])
        lines = store.read_text_lines(build._path(h["slug"]))
        if chunkers.content_sha(lines, c["line_start"], c["line_end"]) != c["sha"]:  # the slice shown is the slice indexed
            raise Stale(f"{h['slug']}.md:L{c['line_start']}–L{c['line_end']} no longer holds the indexed text — run `novelgraph build`")
        text = " ".join(build.chunk_text(lines, c).split())[:200]
        path = " › ".join(c["heading_path"]) or "—"
        out.append(f"{h['score']:.4f}  {h['slug']}.md:L{h['line_start']}–L{h['line_end']}  [{path}]\n        {text}")
    return "\n".join(out)


@store.reader
def as_json(hits: list[dict], method: str) -> str:
    # JSON carries the same citation contract as human-readable output.
    for h in hits:
        c = _chunk(h["slug"], method, h["id"])
        lines = store.read_text_lines(build._path(h["slug"]))
        if chunkers.content_sha(lines, c["line_start"], c["line_end"]) != c["sha"]:
            raise Stale(f"{h['slug']} no longer holds the indexed text — run `novelgraph build`")
    return json.dumps([{**h, "heading_path": _chunk(h["slug"], method, h["id"])["heading_path"]} for h in hits],
                      ensure_ascii=False, indent=1)
