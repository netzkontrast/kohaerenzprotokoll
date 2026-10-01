"""Paths and the registry. Everything the index writes lives under `Index/`."""

from __future__ import annotations

import hashlib
import json
import tomllib
import os
import tempfile
import fcntl
from contextlib import contextmanager
from functools import wraps
from functools import lru_cache
from pathlib import Path

from .repo import INDEX

METHODS = INDEX / "methods.toml"
MANIFEST = INDEX / "manifest.jsonl"
SOURCES = INDEX / "sources"
BUILD = INDEX / "_build"


@lru_cache(maxsize=1)
def registry() -> dict:
    return tomllib.loads(METHODS.read_text(encoding="utf-8"))


def chunkers() -> dict[str, dict]:
    return registry()["chunker"]


def embedders() -> dict[str, dict]:
    return registry()["embedder"]


def default_embedder() -> str:
    return next(iter(embedders()))


def method_stamp() -> str:
    """What a source's index depends on besides its own bytes: the chunker, token, heading and lex sections.
    Code that changes what one of them does is a change to that section's version."""
    r = registry()
    blob = json.dumps({k: r[k] for k in ("chunker", "tokens", "headings", "lex")}, sort_keys=True)
    return hashlib.sha1(blob.encode()).hexdigest()[:12]


def embedder_fp(name: str) -> str:
    """The embedder as the vectors depend on it: its whole registry entry (model, revision, input, normalisation,
    dtype) and the name. Changing any of them invalidates every vector made under the old one."""
    blob = json.dumps({"name": name, **embedders()[name]}, sort_keys=True)
    return hashlib.sha1(blob.encode()).hexdigest()[:12]


def source_dir(slug: str) -> Path:
    return SOURCES / slug


def chunks_path(slug: str, method: str) -> Path:
    return source_dir(slug) / "chunks" / f"{method}.jsonl"


def lex_path(slug: str, method: str) -> Path:
    return source_dir(slug) / "lex" / f"{method}.terms.jsonl"


def vec_path(slug: str, method: str, embedder: str) -> Path:
    return source_dir(slug) / "vec" / f"{method}~{embedder}.f16.npy"


def vec_meta_path(slug: str, method: str, embedder: str) -> Path:
    return source_dir(slug) / "vec" / f"{method}~{embedder}.json"


def build_matrix(method: str, embedder: str) -> Path:
    return BUILD / f"{method}~{embedder}.f16.npy"


def build_rows(method: str, embedder: str) -> Path:
    return BUILD / f"{method}~{embedder}.rows.jsonl"


def build_bm25(method: str) -> Path:
    return BUILD / f"{method}.bm25.sqlite"


def ids_hash(ids) -> str:
    return hashlib.sha1("\n".join(ids).encode()).hexdigest()


def read_text_lines(path: Path) -> list[str]:
    return path.read_text(encoding="utf-8").split("\n")


def write_json(path: Path, obj) -> None:
    atomic_text(path, json.dumps(obj, ensure_ascii=False, indent=1) + "\n")


def atomic_text(path: Path, text: str) -> None:
    """Publish complete bytes by rename; a failed writer never truncates a live file."""
    path.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".publish-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as out:
            out.write(text)
        os.replace(name, path)
    finally:
        Path(name).unlink(missing_ok=True)


@contextmanager
def lock(write: bool = False):
    """Serialize writers and hold readers outside a publication (Linux flock)."""
    MANIFEST.parent.mkdir(parents=True, exist_ok=True)
    with (MANIFEST.parent / ".lock").open("a") as handle:
        fcntl.flock(handle, fcntl.LOCK_EX if write else fcntl.LOCK_SH)
        try:
            yield
        finally:
            fcntl.flock(handle, fcntl.LOCK_UN)


def dirty_path() -> Path:
    return MANIFEST.parent / ".building"


def reader(fn):
    @wraps(fn)
    def checked(*args, **kwargs):
        with lock():
            if dirty_path().exists():
                raise SystemExit("interrupted novelgraph build — run `novelgraph build` before reading")
            return fn(*args, **kwargs)
    return checked
