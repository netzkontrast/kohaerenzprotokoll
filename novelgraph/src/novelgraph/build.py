"""`novelgraph build`: chunk, lex and embed every landed source, incrementally; then concatenate `_build/`.

Three stages, each skipped when its input is unchanged:

1. **chunks** (committed) **+ lex** (gitignored) — redone for a source when its sha256 or the
   registry's chunker/token/lex sections (`store.method_stamp`) changed, or a file is missing.
2. **vec** (gitignored) — a source's matrix is reused when its `chunk_ids_hash`
   matches; otherwise rows of chunk ids already embedded are copied from the old
   matrix and only new ids are embedded. A chunk id is the embedding cache key.
3. **_build** (gitignored) — the per-source matrices concatenated into one memmap,
   the row map, and the FTS5 table; redone when the hash over every source's
   chunk ids changed.
"""

from __future__ import annotations

import hashlib
import json
import shutil
import sqlite3
import time
from datetime import datetime, timezone

import numpy as np

from . import chunkers, lex, store
from .repo import documents, read_jsonl, write_jsonl

_MODEL = {}


def model(embedder: str):
    if embedder not in _MODEL:
        from huggingface_hub import snapshot_download
        from model2vec import StaticModel
        spec = store.embedders()[embedder]  # pinned: the revision in methods.toml, fetched once, then local
        get = lambda local: snapshot_download(spec["model"], revision=spec["revision"], local_files_only=local,  # noqa: E731
                                              allow_patterns=["config.json", "model.safetensors", "tokenizer.json"])
        try:
            path = get(True)
        except Exception:  # not in the cache yet: fetched once, ~0.5 GB
            path = get(False)
        _MODEL[embedder] = StaticModel.from_pretrained(path)
    return _MODEL[embedder]


def embed(embedder: str, texts: list[str]) -> np.ndarray:
    if not texts:
        return np.zeros((0, model(embedder).dim), dtype=np.float16)
    v = model(embedder).encode(texts, max_length=None, batch_size=1024, show_progress_bar=False)
    v = np.asarray(v, dtype=np.float32)
    norms = np.linalg.norm(v, axis=1, keepdims=True)
    norms[norms == 0] = 1.0
    return (v / norms).astype(np.float16)


def now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def chunk_text(file_lines: list[str], row: dict) -> str:
    return "\n".join(file_lines[row["line_start"] - 1:row["line_end"]])


def vec_key(row: dict) -> str:
    """The embedding cache key: the chunk id and the prefix. The id (as specified) covers the text and the range
    but not the prefix, and the prefix is embedded too — a renamed heading would otherwise keep a stale vector."""
    return row["id"] + ":" + hashlib.sha1(row["prefix"].encode("utf-8")).hexdigest()[:8]


def embed_input(file_lines: list[str], row: dict) -> str:
    return row["prefix"] + "\n" + chunk_text(file_lines, row)


def write_lex(slug: str, method: str, rows: list[dict], file_lines: list[str], lang: str) -> None:
    write_jsonl(store.lex_path(slug, method), [
        {"id": r["id"], "surfaces": lex.surfaces(t), "lemmata": lex.lemmata(t, lang)}
        for r in rows for t in [chunk_text(file_lines, r)]])


def build(source: str | None = None, methods: list[str] | None = None, force: bool = False,
          embedder: str | None = None, log=print) -> dict:
    t0 = time.perf_counter()
    embedder = embedder or store.default_embedder()
    all_methods = store.chunkers()
    methods = methods or list(all_methods)
    for m in methods:
        if m not in all_methods:
            raise SystemExit(f"unknown method {m!r}; methods.toml has {', '.join(all_methods)}")
    docs = documents()
    if source:
        docs = [d for d in docs if d.slug == source]
        if not docs:
            raise SystemExit(f"no landed source {source!r}")
    stamp = store.method_stamp()
    old = {r["slug"]: r for r in read_jsonl(store.MANIFEST)} if store.MANIFEST.exists() else {}
    new_manifest = dict(old)
    stats = {"sources": len(docs), "rechunked": 0, "embedded": 0, "reused_vectors": 0, "skipped": 0}

    for doc in docs:
        raw = doc.path.read_bytes()
        sha = hashlib.sha256(raw).hexdigest()
        file_lines = raw.decode("utf-8").split("\n")
        prev = old.get(doc.slug)
        same = (prev and prev.get("sha256") == sha and prev.get("methods_stamp") == stamp
                and (store.source_dir(doc.slug) / "source.json").exists()
                and all(store.chunks_path(doc.slug, m).exists() for m in all_methods))
        title = (_title(doc.slug) or {}).get("title", doc.slug)
        if same and not force:  # lex/ is gitignored: a fresh clone has the chunks and none of it
            lang = json.loads((store.source_dir(doc.slug) / "source.json").read_text())["lang"]
            for m in all_methods:
                if not store.lex_path(doc.slug, m).exists():
                    write_lex(doc.slug, m, read_jsonl(store.chunks_path(doc.slug, m)), file_lines, lang)
                    stats["lex_rebuilt"] = stats.get("lex_rebuilt", 0) + 1
        if force or not same:
            parsed = chunkers.parse(file_lines, doc.offset)
            lang = lex.language(doc.body)
            store.write_json(store.source_dir(doc.slug) / "source.json", {
                "slug": doc.slug, "sha256": sha, "lines": len(file_lines), "body_offset": doc.offset,
                "lang": lang, "title": title, "heading_tree": chunkers.heading_tree(parsed)})
            for m, params in all_methods.items():
                rows = chunkers.chunk(doc.slug, title, file_lines, doc.offset, m, params, parsed)
                write_jsonl(store.chunks_path(doc.slug, m), rows)
                write_lex(doc.slug, m, rows, file_lines, lang)
            new_manifest[doc.slug] = {"slug": doc.slug, "sha256": sha, "lines": len(file_lines), "lang": lang,
                                      "methods_stamp": stamp, "indexed_at": now()}
            stats["rechunked"] += 1
        for m in methods:
            rows = read_jsonl(store.chunks_path(doc.slug, m))
            ids = [r["id"] for r in rows]
            meta_p, vec_p = store.vec_meta_path(doc.slug, m, embedder), store.vec_path(doc.slug, m, embedder)
            meta = json.loads(meta_p.read_text()) if meta_p.exists() else None
            keys = [vec_key(r) for r in rows]
            if meta and vec_p.exists() and meta.get("keys") == keys and not force:
                stats["skipped"] += 1
                continue
            cache = {}
            if meta and vec_p.exists() and not force:
                old_mat = np.load(vec_p)
                cache = {key: old_mat[k] for k, key in enumerate(meta.get("keys", []))}
            missing = [r for r, key in zip(rows, keys) if key not in cache]
            fresh = embed(embedder, [embed_input(file_lines, r) for r in missing])
            for r, v in zip(missing, fresh):
                cache[vec_key(r)] = v
            dim = model(embedder).dim if missing else (len(next(iter(cache.values()))) if cache else _dim(embedder))
            mat = np.stack([cache[key] for key in keys]).astype(np.float16) if ids else np.zeros((0, dim), np.float16)
            vec_p.parent.mkdir(parents=True, exist_ok=True)
            np.save(vec_p, mat)
            spec = store.embedders()[embedder]
            store.write_json(meta_p, {"model": spec["model"], "revision": spec.get("revision"), "dim": int(mat.shape[1]),
                                      "chunk_ids_hash": store.ids_hash(ids), "keys": keys, "built_at": now()})
            stats["embedded"] += len(missing)
            stats["reused_vectors"] += len(ids) - len(missing)

    if not source:  # a source no longer landed leaves the index
        landed = {d.slug for d in docs}
        for slug in list(new_manifest):
            if slug not in landed:
                del new_manifest[slug]
                shutil.rmtree(store.source_dir(slug), ignore_errors=True)
                stats.setdefault("removed", []).append(slug)
    ordered = [new_manifest[s] for s in sorted(new_manifest)]
    if ordered != [old[s] for s in sorted(old)]:
        write_jsonl(store.MANIFEST, ordered)
    stats["concatenated"] = [m for m in methods if concatenate(m, embedder, force)]
    stats["seconds"] = round(time.perf_counter() - t0, 2)
    log(json.dumps(stats, ensure_ascii=False))
    return stats


_TITLES: dict[str, str] = {}


def _title(slug: str) -> dict | None:
    if not _TITLES:
        from .repo import manifest_rows
        for r in manifest_rows():
            _TITLES.setdefault(r["slug"], r.get("title") or r["slug"])
    return {"title": _TITLES[slug]} if slug in _TITLES else None


def _dim(embedder: str) -> int:
    return model(embedder).dim


def concatenate(method: str, embedder: str, force: bool = False) -> bool:
    """Concatenate every source's matrix, rows and lex into `_build/`; False when already current."""
    slugs = [r["slug"] for r in read_jsonl(store.MANIFEST)]
    parts = []
    for slug in slugs:
        meta = json.loads(store.vec_meta_path(slug, method, embedder).read_text())
        parts.append((slug, meta["chunk_ids_hash"], meta["dim"]))
    stamp = store.ids_hash([f"{s}:{h}" for s, h, _ in parts] + [method, embedder, store.method_stamp()])
    stamp_p = store.BUILD / f"{method}~{embedder}.stamp"
    outs = [store.build_matrix(method, embedder), store.build_rows(method, embedder), store.build_bm25(method)]
    if not force and stamp_p.exists() and stamp_p.read_text().strip() == stamp and all(p.exists() for p in outs):
        return False
    store.BUILD.mkdir(parents=True, exist_ok=True)
    mats = [np.load(store.vec_path(s, method, embedder), mmap_mode="r") for s in slugs]
    total = sum(m.shape[0] for m in mats)
    dim = parts[0][2] if parts else 0
    tmp = outs[0].with_suffix(".tmp.npy")
    big = np.lib.format.open_memmap(tmp, mode="w+", dtype=np.float16, shape=(total, dim))
    rows, k = [], 0
    for slug, mat in zip(slugs, mats):
        big[k:k + mat.shape[0]] = mat
        k += mat.shape[0]
    big.flush()
    del big
    tmp.replace(outs[0])

    db_tmp = outs[2].with_suffix(".tmp")
    db_tmp.unlink(missing_ok=True)
    con = sqlite3.connect(db_tmp)
    # contentless: the text is never stored a second time (it is a slice of the source); rowid = matrix row + 1
    con.execute("CREATE VIRTUAL TABLE chunks USING fts5(text, lemmata, content='', "
                "tokenize='unicode61 remove_diacritics 2')")
    row = 0
    for slug in slugs:
        file_lines = store.read_text_lines(_path(slug))
        lexrows = {r["id"]: r for r in read_jsonl(store.lex_path(slug, method))}
        batch = []
        for c in read_jsonl(store.chunks_path(slug, method)):
            rows.append({"slug": slug, "id": c["id"], "line_start": c["line_start"], "line_end": c["line_end"]})
            row += 1
            batch.append((row, c["prefix"] + "\n" + chunk_text(file_lines, c), lex.expand(lexrows[c["id"]]["lemmata"])))
        con.executemany("INSERT INTO chunks(rowid, text, lemmata) VALUES (?, ?, ?)", batch)
    con.commit()
    con.close()
    db_tmp.replace(outs[2])
    if len(rows) != total:
        raise SystemExit(f"{method}: {len(rows)} chunk rows but {total} matrix rows — a vec/ file is stale")
    write_jsonl(outs[1], rows)
    stamp_p.write_text(stamp + "\n")
    return True


_PATHS: dict[str, object] = {}


def _path(slug: str):
    if not _PATHS:
        for d in documents():
            _PATHS[d.slug] = d.path
    return _PATHS[slug]
