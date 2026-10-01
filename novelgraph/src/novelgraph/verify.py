"""`novelgraph verify`: what the index claims, re-measured against the files. Exit 1 on any failure.

1. **coverage** — every landed manifest slug has an index entry, and nothing else has;
2. **sources** — `source.json` and the index manifest hash to the file as it sits on disk;
3. **chunks** — every range lies inside the file, every `sha` is the slice's sha1,
   every id recomputes from its fields, and the chunker run again yields the same rows;
   `lex/` holds the same ids in the same order;
4. **vec** — each per-source matrix has one row per chunk and its `chunk_ids_hash` matches;
5. **_build** — `rows.jsonl` is the concatenation of the chunk files in manifest order,
   and the matrix and the FTS5 table have exactly that many rows.
"""

from __future__ import annotations

import hashlib
import json
import sqlite3

import numpy as np

from . import chunkers, store
from .build import _title, build_stamp, build_stamp_path, vec_key
from .repo import documents, read_jsonl


def _matrix_problems(mat, dim) -> list[str]:
    """float16, the recorded dimension, finite, every row of unit length (to float16 precision)."""
    out = []
    if mat.dtype != np.float16:
        out.append(f"dtype {mat.dtype}, not float16")
    if dim is not None and mat.ndim == 2 and mat.shape[1] != dim:
        out.append(f"dimension {mat.shape[1]}, the metadata says {dim}")
    if mat.size:
        wide = np.asarray(mat, dtype=np.float32)
        if not np.isfinite(wide).all():
            out.append("non-finite values")
        else:
            norms = np.linalg.norm(wide, axis=1)
            bad = int(np.sum((norms > 0) & (np.abs(norms - 1) > 5e-3)))
            if bad:
                out.append(f"{bad} rows are not unit length")
    return out


def verify(embedder: str | None = None, rechunk: bool = True) -> tuple[list[str], dict]:
    embedder = embedder or store.default_embedder()
    fails, info = [], {}
    docs = {d.slug: d for d in documents()}
    manifest = {r["slug"]: r for r in read_jsonl(store.MANIFEST)} if store.MANIFEST.exists() else {}
    missing, extra = sorted(set(docs) - set(manifest)), sorted(set(manifest) - set(docs))
    info["coverage"] = f"{len(set(docs) & set(manifest))}/{len(docs)} landed sources indexed " \
                       f"({100 * len(set(docs) & set(manifest)) / max(1, len(docs)):.1f} %)"
    fails += [f"coverage: {s} is landed and not indexed" for s in missing]
    fails += [f"coverage: {s} is indexed and not landed" for s in extra]
    methods = store.chunkers()
    counts = {m: 0 for m in methods}
    for slug in sorted(set(docs) & set(manifest)):
        doc = docs[slug]
        raw = doc.path.read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        lines = raw.decode("utf-8").split("\n")
        src = json.loads((store.source_dir(slug) / "source.json").read_text())
        if not (sha == src["sha256"] == manifest[slug]["sha256"]):
            fails.append(f"{slug}: file, source.json and manifest disagree on sha256 — rebuild")
            continue
        if src["lines"] != len(lines):
            fails.append(f"{slug}: source.json says {src['lines']} lines, the file has {len(lines)}")
        parsed = chunkers.parse(lines, doc.offset) if rechunk else None
        title = (_title(slug) or {}).get("title", slug)
        for m, params in methods.items():
            rows = read_jsonl(store.chunks_path(slug, m))
            counts[m] += len(rows)
            for r in rows:
                if not 1 <= r["line_start"] <= r["line_end"] <= len(lines):
                    fails.append(f"{slug} {m} {r['id']}: L{r['line_start']}–L{r['line_end']} outside 1–{len(lines)}")
                    continue
                if chunkers.content_sha(lines, r["line_start"], r["line_end"]) != r["sha"]:
                    fails.append(f"{slug} {m} {r['id']}: the slice no longer hashes to sha")
                if chunkers.chunk_id(slug, m, r["line_start"], r["line_end"], r["sha"]) != r["id"]:
                    fails.append(f"{slug} {m} {r['id']}: id does not recompute")
            if rechunk and chunkers.chunk(slug, title, lines, doc.offset, m, params, parsed) != rows:
                fails.append(f"{slug} {m}: the chunker run again gives different rows")
            if [x["id"] for x in read_jsonl(store.lex_path(slug, m))] != [r["id"] for r in rows]:
                fails.append(f"{slug} {m}: lex ids differ from chunk ids")
            meta_p, vec_p = store.vec_meta_path(slug, m, embedder), store.vec_path(slug, m, embedder)
            if not (meta_p.exists() and vec_p.exists()):
                fails.append(f"{slug} {m}: no vectors for {embedder}")
                continue
            meta = json.loads(meta_p.read_text())
            if meta["chunk_ids_hash"] != store.ids_hash([r["id"] for r in rows]) or \
                    meta.get("keys") != [vec_key(r) for r in rows]:
                fails.append(f"{slug} {m}: vectors are for other chunks or prefixes")
            if meta.get("embedder_fp") != store.embedder_fp(embedder):
                fails.append(f"{slug} {m}: vectors are from another embedder spec than methods.toml names")
            mat = np.load(vec_p, mmap_mode="r")
            if mat.shape[0] != len(rows):
                fails.append(f"{slug} {m}: matrix rows differ from chunks")
            fails += [f"{slug} {m}: {p}" for p in _matrix_problems(mat, meta.get("dim"))]
    info["chunks"] = counts
    order = [r["slug"] for r in read_jsonl(store.MANIFEST)] if store.MANIFEST.exists() else []
    for m in methods:
        rp, mp, bp = store.build_rows(m, embedder), store.build_matrix(m, embedder), store.build_bm25(m)
        if not (rp.exists() and mp.exists() and bp.exists()):
            fails.append(f"_build {m}: missing — run `novelgraph build`")
            continue
        rows = read_jsonl(rp)
        expect = [(s, r["id"]) for s in order for r in read_jsonl(store.chunks_path(s, m))]
        if [(r["slug"], r["id"]) for r in rows] != expect:
            fails.append(f"_build {m}: rows.jsonl is not the concatenation of the chunk files")
        big = np.load(mp, mmap_mode="r")
        n = big.shape[0]
        if n != len(rows):
            fails.append(f"_build {m}: matrix has {n} rows, rows.jsonl {len(rows)}")
        else:  # by value, block by block: the right shape with the wrong vectors is not a pass
            k = 0
            for s in order:
                part = np.load(store.vec_path(s, m, embedder), mmap_mode="r")
                if part.dtype != big.dtype or not np.array_equal(big[k:k + part.shape[0]], part):
                    fails.append(f"_build {m}: rows {k}–{k + part.shape[0] - 1} differ from {s}'s vectors")
                    break
                k += part.shape[0]
        fails += [f"_build {m}: {p}" for p in _matrix_problems(big, None)]
        stamp_p = build_stamp_path(m, embedder)
        try:
            if not stamp_p.exists() or stamp_p.read_text().strip() != build_stamp(m, embedder)[0]:
                fails.append(f"_build {m}: its stamp does not match the current index — run `novelgraph build`")
        except SystemExit as e:
            fails.append(f"_build {m}: {e}")
        con = sqlite3.connect(f"{bp.resolve().as_uri()}?mode=ro", uri=True)
        fts = con.execute("SELECT count(*), coalesce(min(rowid), 1), coalesce(max(rowid), 0) FROM chunks").fetchone()
        if fts[1:] != (1, fts[0]):
            fails.append(f"_build {m}: FTS5 rowids are not 1..{fts[0]}")
        fts = fts[0]
        con.close()
        if fts != len(rows):
            fails.append(f"_build {m}: FTS5 has {fts} rows, rows.jsonl {len(rows)}")
    return fails, info
