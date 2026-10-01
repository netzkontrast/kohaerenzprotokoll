"""Verify coverage, reproduction, source slices and exact vector concatenation."""
import json
import sqlite3
import numpy as np
from . import repo
from .chunking import chunk_id, sha, slice_text, make_chunks
from .embedding import ids_hash
from .index import EMBEDDER, read_json, lexical


def verify(index, method="heading@v1"):
    with index.lock():
        return _verify(index, method)


def _verify(index, method):
    errors, expected_rows, expected_vectors, items = [], [], [], []
    source_rows = repo.sources(index.root)
    landed = [r for r in source_rows if r.get("export_path")]
    unlanded = [r["slug"] for r in source_rows if not r.get("export_path")]
    indexed = repo.read_jsonl(index.path / "manifest.jsonl") if (index.path / "manifest.jsonl").exists() else []
    have = {r["slug"]: r for r in indexed}
    if len(have) != len(indexed):
        errors.append("duplicate Index manifest slug")
    expected_slugs = {r["slug"] for r in landed}
    if set(have) != expected_slugs:
        errors.append(f"coverage: missing {sorted(expected_slugs - set(have))}; extra {sorted(set(have) - expected_slugs)}")
    signature = index.fingerprint(method)
    tokenizer = index.embedder(offline=True)
    for source in landed:
        slug = source["slug"]
        try:
            p = index.root / source["export_path"]
            text = p.read_text(encoding="utf-8")
            lines = text.split("\n")
            actual = sha(text)
            base = index.path / "sources" / slug
            info = read_json(base / "source.json")
            if actual != source.get("sha256") or actual != info["sha256"] or info["lines"] != len(lines):
                errors.append(f"source checksum/lines: {slug}")
            if have.get(slug) != dict(slug=slug, **{k: info[k] for k in ("sha256", "lines", "lang", "indexed_at")}):
                errors.append(f"Index manifest/source metadata differ: {slug}")
            cs = repo.read_jsonl(base / "chunks" / (method + ".jsonl"))
            expected, tree = make_chunks(slug, source["title"], text, method, index.config["chunkers"][method], tokenizer.count)
            if cs != expected or info["heading_tree"] != tree or info["title"] != source["title"]:
                errors.append(f"fresh chunk derivation differs: {slug}")
            covered = set()
            for c in cs:
                if set(c) != {"id", "line_start", "line_end", "heading_path", "sha", "tokens", "prefix"}:
                    errors.append(f"invalid chunk fields: {slug}/{c.get('id')}")
                a, b = c["line_start"], c["line_end"]
                if not 1 <= a <= b <= len(lines):
                    errors.append(f"out-of-range source lines: {slug}/{c['id']}")
                    continue
                content_sha = sha(slice_text(lines, a, b))
                if c["sha"] != content_sha or c["id"] != chunk_id(slug, method, a, b, content_sha):
                    errors.append(f"unreproducible chunk ID/hash: {slug}/{c['id']}")
                covered.update(range(a, b + 1))
            _, offset = repo.split_body(text)
            if any(n not in covered for n in range(offset, len(lines) + 1) if lines[n - 1].strip()):
                errors.append(f"nonempty source line has no chunk: {slug}")
            lex = repo.read_jsonl(base / "lex" / (method + ".terms.jsonl"))
            if lex != [lexical(slice_text(lines, c["line_start"], c["line_end"]), c) for c in cs]:
                errors.append(f"lexical derivation differs: {slug}")
            vp = base / "vec" / (method + "~" + EMBEDDER + ".f16.npy")
            meta = read_json(base / "vec" / (method + "~" + EMBEDDER + ".json"))
            matrix = np.load(vp, mmap_mode="r", allow_pickle=False)
            if (matrix.shape != (len(cs), meta["dim"]) or matrix.dtype != np.float16
                    or meta["signature"] != signature or meta["source_sha256"] != actual
                    or meta["chunk_ids_hash"] != ids_hash([c["id"] for c in cs])):
                errors.append(f"vector metadata/order mismatch: {slug}")
            norms = np.linalg.norm(matrix.astype(np.float32), axis=1)
            if not np.isfinite(matrix).all() or np.any((norms > 0) & (abs(norms - 1) > .003)):
                errors.append(f"nonfinite/unnormalized vectors: {slug}")
            if meta.get("input_hashes") != {c["id"]: sha(c["prefix"] + "\n" + slice_text(lines, c["line_start"], c["line_end"])) for c in cs}:
                errors.append(f"embedding input mismatch: {slug}")
            expected_rows += [dict(slug=slug, chunk_id=c["id"]) for c in cs]
            expected_vectors.append(matrix)
            items += [(slug, c, l, slice_text(lines, c["line_start"], c["line_end"])) for c, l in zip(cs, lex)]
        except (OSError, ValueError, KeyError, IndexError) as exc:
            errors.append(f"{slug}: {exc}")
    base = index.path / "_build"
    try:
        rows = repo.read_jsonl(base / (method + "~" + EMBEDDER + ".rows.jsonl"))
        matrix = np.load(base / (method + "~" + EMBEDDER + ".f16.npy"), mmap_mode="r", allow_pickle=False)
        if rows != expected_rows or len(rows) != len(matrix) or matrix.dtype != np.float16:
            errors.append("aggregate row/shape/order mismatch")
        position = 0
        for vectors in expected_vectors:
            if not np.array_equal(matrix[position:position + len(vectors)], vectors):
                errors.append("aggregate vector values differ from source cache")
                break
            position += len(vectors)
        with sqlite3.connect(f"file:{base / (method + '.bm25.sqlite')}?mode=ro", uri=True) as db:
            actual = list(db.execute("SELECT text,lemma,prefix,slug,chunk_id,payload FROM chunks ORDER BY rowid"))
            wanted = [(text, " ".join(l["surfaces"] + l["lemmas"]), c["prefix"], slug, c["id"],
                       json.dumps(dict(c, slug=slug), ensure_ascii=False, sort_keys=True, separators=(",", ":"))) for slug, c, l, text in items]
            if actual != wanted:
                errors.append("FTS content or ordering differs from source slices")
    except (OSError, ValueError, sqlite3.Error) as exc:
        errors.append(f"aggregate missing/invalid: {exc}")
    return dict(method=method, landed=len(landed), manifest_total=len(source_rows), indexed=len(expected_slugs & set(have)),
                landed_coverage=len(expected_slugs & set(have)) / len(landed) if landed else None,
                total_coverage=len(expected_slugs & set(have)) / len(source_rows) if source_rows else None,
                unlanded=unlanded, chunks=len(expected_rows), errors=errors, ok=not errors)
