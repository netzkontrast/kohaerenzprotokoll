"""Per-source index, atomic file publication, exact incremental cache reuse."""
from __future__ import annotations
from contextlib import contextmanager
from datetime import datetime, timezone
from functools import lru_cache
from pathlib import Path
import fcntl
import hashlib
import json
import os
import re
import shutil
import sqlite3
import tempfile
import time
import tomllib
import numpy as np
import simplemma

from . import repo
from .chunking import make_chunks, sha, slice_text
from .embedding import Embedder, ids_hash

EMBEDDER = "potion-m128"


def now():
    return datetime.now(timezone.utc).isoformat()


def canonical(value):
    return json.dumps(value, ensure_ascii=False, sort_keys=True, separators=(",", ":"))


def read_json(path):
    return json.loads(path.read_text(encoding="utf-8"))


def atomic_json(path, value):
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_suffix(path.suffix + ".tmp")
    tmp.write_text(canonical(value) + "\n", encoding="utf-8")
    os.replace(tmp, path)


def lexical(text, chunk):
    # These are lexical surfaces, never claimed to be morphological lemmas.
    terms = re.findall(r"\w+(?:[-:]\w+)*", chunk["prefix"] + "\n" + text)
    surfaces = {repo.fold(t) for t in terms}
    lemmas = {lemma(t) for t in terms}
    return dict(id=chunk["id"], surfaces=sorted(s for s in surfaces if s),
                lemmas=sorted(s for s in lemmas if s))


@lru_cache(maxsize=200000)
def lemma(term):
    return repo.fold(simplemma.lemmatize(term, lang=("de", "en")))


def language(text):
    body, _ = repo.split_body(text)
    guesses = simplemma.langdetect(body[:8000], lang=("de", "en"))
    # Dictionary-based metadata, not a decision about the document's content.
    if guesses and guesses[0][0] in ("de", "en") and guesses[0][1] >= .6:
        return guesses[0][0]
    return "und"


class Index:
    def __init__(self, root=repo.ROOT, index=None, embedder_factory=Embedder):
        self.root = Path(root).resolve()
        self.path = Path(index).resolve() if index else self.root / "Index"
        self.config = tomllib.loads((self.path / "methods.toml").read_text(encoding="utf-8"))
        self.embedder_factory = embedder_factory
        self._embedder = None
        self._signatures = {}

    def embedder(self, offline=False):
        if self._embedder is None:
            self._embedder = self.embedder_factory(self.config["embedders"][EMBEDDER], offline=offline)
        return self._embedder

    def fingerprint(self, method):
        if method in self._signatures:
            return self._signatures[method]
        code = {p.name: hashlib.sha256(p.read_bytes()).hexdigest()
                for p in Path(__file__).parent.glob("*.py") if p.name != "cli.py"}
        helpers = {p: hashlib.sha256((repo.ROOT / "scripts" / p).read_bytes()).hexdigest()
                   for p in ("subject.py", "wiki_index.py")}
        signature = sha(canonical(dict(chunker=self.config["chunkers"][method],
                                  embedder=self.config["embedders"][EMBEDDER],
                                  lex=self.config["lex"], code=code, helpers=helpers)))
        self._signatures[method] = signature
        return signature

    @contextmanager
    def lock(self):
        self.path.mkdir(parents=True, exist_ok=True)
        with (self.path / ".lock").open("a") as f:
            fcntl.flock(f, fcntl.LOCK_EX)
            yield

    def build(self, method="heading@v1", source=None, force=False):
        started = time.perf_counter()
        if method not in self.config["chunkers"]:
            raise ValueError(f"unknown method: {method}")
        rows = repo.sources(self.root)
        landed = [r for r in rows if r.get("export_path")]
        if source and source not in {r["slug"] for r in landed}:
            raise ValueError(f"unknown or unlanded source: {source}")
        count = dict(changed_sources=0, skipped_sources=0, embedded_chunks=0, reused_chunks=0)
        signature = self.fingerprint(method)
        with self.lock():
            for row in landed:
                if source and row["slug"] != source:
                    continue
                slug = row["slug"]
                source_path = self.root / row["export_path"]
                raw = source_path.read_bytes()
                source_sha = hashlib.sha256(raw).hexdigest()
                if row.get("sha256") and row["sha256"] != source_sha:
                    raise ValueError(f"source disagrees with authoritative manifest: {slug}")
                text = raw.decode("utf-8")
                base = self.path / "sources" / slug
                cp = base / "chunks" / (method + ".jsonl")
                lp = base / "lex" / (method + ".terms.jsonl")
                vp = base / "vec" / (method + "~" + EMBEDDER + ".f16.npy")
                mp = vp.with_name(method + "~" + EMBEDDER + ".json")
                info = read_json(base / "source.json") if (base / "source.json").exists() else {}
                meta = read_json(mp) if mp.exists() else {}
                if (not force and info.get("sha256") == source_sha and info.get("title") == row["title"]
                        and meta.get("source_sha256") == source_sha and meta.get("signature") == signature
                        and cp.exists() and lp.exists() and vp.exists()):
                    count["skipped_sources"] += 1
                    continue
                old_chunks = repo.read_jsonl(cp) if cp.exists() else []
                cached = {}
                if vp.exists() and meta.get("model") == self.config["embedders"][EMBEDDER]["model"] \
                        and meta.get("revision") == self.config["embedders"][EMBEDDER]["revision"]:
                    old = np.load(vp, mmap_mode="r", allow_pickle=False)
                    if old.ndim == 2 and len(old) == len(old_chunks) and meta.get("chunk_ids_hash") == ids_hash([c["id"] for c in old_chunks]):
                        cached = {c["id"]: (old[i], meta.get("input_hashes", {}).get(c["id"])) for i, c in enumerate(old_chunks)}
                embedder = self.embedder()
                chunks, tree = make_chunks(slug, row["title"], text, method, self.config["chunkers"][method], embedder.count)
                source_lines = text.split("\n")
                inputs = [c["prefix"] + "\n" + slice_text(source_lines, c["line_start"], c["line_end"]) for c in chunks]
                hashes = {c["id"]: sha(t) for c, t in zip(chunks, inputs)}
                missing = [i for i, c in enumerate(chunks) if c["id"] not in cached or cached[c["id"]][1] != hashes[c["id"]]]
                if missing:
                    encoded = embedder.encode([inputs[i] for i in missing])
                    dim = encoded.shape[1]
                elif chunks:
                    dim = len(cached[chunks[0]["id"]][0])
                    encoded = np.empty((0, dim), dtype=np.float16)
                else:
                    encoded = embedder.encode([])
                    dim = encoded.shape[1]
                matrix = np.empty((len(chunks), dim), dtype=np.float16)
                for i, c in enumerate(chunks):
                    if i not in missing:
                        matrix[i] = cached[c["id"]][0]
                for i, value in zip(missing, encoded):
                    matrix[i] = value
                with tempfile.TemporaryDirectory(prefix=".ng-", dir=self.path) as temp:
                    temp = Path(temp)
                    repo.write_jsonl(temp / "chunks.jsonl", chunks)
                    repo.write_jsonl(temp / "lex.jsonl", [lexical(slice_text(source_lines, c["line_start"], c["line_end"]), c) for c in chunks])
                    np.save(temp / "vectors.npy", matrix, allow_pickle=False)
                    # Metadata is published last, so an interrupted update cannot claim freshness.
                    for dest, name in ((cp, "chunks.jsonl"), (lp, "lex.jsonl"), (vp, "vectors.npy")):
                        dest.parent.mkdir(parents=True, exist_ok=True)
                        os.replace(temp / name, dest)
                stamp = now()
                atomic_json(base / "source.json", dict(sha256=source_sha, lines=len(source_lines), lang=language(text),
                            title=row["title"], heading_tree=tree, indexed_at=stamp))
                atomic_json(mp, dict(model=self.config["embedders"][EMBEDDER]["model"],
                            revision=self.config["embedders"][EMBEDDER]["revision"], dim=dim,
                            dtype="float16", chunk_ids_hash=ids_hash([c["id"] for c in chunks]),
                            input_hashes=hashes, source_sha256=source_sha, signature=signature, built_at=stamp))
                count["changed_sources"] += 1
                count["embedded_chunks"] += len(missing)
                count["reused_chunks"] += len(chunks) - len(missing)
            manifest = []
            for row in landed:
                p = self.path / "sources" / row["slug"] / "source.json"
                if p.exists():
                    info = read_json(p)
                    manifest.append(dict(slug=row["slug"], **{k: info[k] for k in ("sha256", "lines", "lang", "indexed_at")}))
            repo.write_jsonl(self.path / "manifest.jsonl", manifest)
            count.update(self.aggregate(method, landed))
        count["seconds"] = round(time.perf_counter() - started, 4)
        return count

    def aggregate(self, method, landed):
        """Always regenerate concatenation; never include deleted manifest sources."""
        rows, matrices, chunks, lexes, inputs = [], [], [], [], {}
        for source in landed:
            slug = source["slug"]
            base = self.path / "sources" / slug
            cp = base / "chunks" / (method + ".jsonl")
            mp = base / "vec" / (method + "~" + EMBEDDER + ".json")
            if not cp.exists() or not mp.exists():
                continue
            info = read_json(base / "source.json")
            meta = read_json(mp)
            actual_sha = hashlib.sha256((self.root / source["export_path"]).read_bytes()).hexdigest()
            if info["sha256"] != actual_sha or meta.get("source_sha256") != actual_sha or meta.get("signature") != self.fingerprint(method):
                raise ValueError(f"cannot aggregate stale source: {slug}; build without --source")
            cs = repo.read_jsonl(cp)
            matrix = np.load(base / "vec" / (method + "~" + EMBEDDER + ".f16.npy"), mmap_mode="r", allow_pickle=False)
            if matrix.ndim != 2 or matrix.shape != (len(cs), meta["dim"]) or meta["chunk_ids_hash"] != ids_hash([c["id"] for c in cs]):
                raise ValueError(f"vector/chunk order mismatch: {slug}")
            ls = repo.read_jsonl(base / "lex" / (method + ".terms.jsonl"))
            if [c["id"] for c in cs] != [l["id"] for l in ls]:
                raise ValueError(f"lex/chunk mismatch: {slug}")
            matrices.append(matrix)
            chunks += [dict(c, slug=slug) for c in cs]
            lexes += ls
            rows += [dict(slug=slug, chunk_id=c["id"]) for c in cs]
            inputs[slug] = dict(sha256=actual_sha, chunks=sha(cp.read_text()), lex=sha((base / "lex" / (method + ".terms.jsonl")).read_text()))
        if not matrices:
            raise ValueError("no vectors to aggregate")
        dims = {m.shape[1] for m in matrices}
        if len(dims) != 1:
            raise ValueError("mixed vector dimensions")
        target = self.path / "_build"
        target.mkdir(exist_ok=True)
        name = method + "~" + EMBEDDER
        with tempfile.TemporaryDirectory(prefix=".publish-", dir=target) as tmp:
            tmp = Path(tmp)
            mmap = np.lib.format.open_memmap(tmp / "matrix.npy", mode="w+", dtype=np.float16, shape=(len(rows), dims.pop()))
            pos = 0
            for matrix in matrices:
                mmap[pos:pos + len(matrix)] = matrix
                pos += len(matrix)
            mmap.flush()
            del mmap
            repo.write_jsonl(tmp / "rows.jsonl", rows)
            db = sqlite3.connect(tmp / "bm25.sqlite")
            db.execute("CREATE VIRTUAL TABLE chunks USING fts5(text, lemma, prefix, slug UNINDEXED, chunk_id UNINDEXED, payload UNINDEXED, tokenize='unicode61 remove_diacritics 2')")
            source_texts = {}
            source_paths = {r["slug"]: self.root / r["export_path"] for r in landed}
            for c, lex in zip(chunks, lexes):
                if c["slug"] not in source_texts:
                    source_texts[c["slug"]] = source_paths[c["slug"]].read_text(encoding="utf-8").split("\n")
                text = slice_text(source_texts[c["slug"]], c["line_start"], c["line_end"])
                db.execute("INSERT INTO chunks VALUES (?,?,?,?,?,?)", (text, " ".join(lex["surfaces"] + lex["lemmas"]), c["prefix"], c["slug"], c["id"], canonical(c)))
            db.execute("CREATE TABLE metadata(payload TEXT)")
            meta = dict(method=method, signature=self.fingerprint(method), inputs=inputs,
                        rows=len(rows), dim=next(iter({m.shape[1] for m in matrices})), built_at=now())
            db.execute("INSERT INTO metadata VALUES (?)", (canonical(meta),))
            db.commit()
            db.close()
            for src, dest in (("matrix.npy", name + ".f16.npy"), ("rows.jsonl", name + ".rows.jsonl"), ("bm25.sqlite", method + ".bm25.sqlite")):
                os.replace(tmp / src, target / dest)
        return dict(chunks=len(rows), indexed_sources=len(inputs),
                    oversized=sum(c["tokens"] > self.config["chunkers"][method].get("max", self.config["chunkers"][method].get("target", 10**12)) for c in chunks),
                    undersized=sum(c["tokens"] < self.config["chunkers"][method].get("min", 0) for c in chunks))
