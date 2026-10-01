"""Each case hands the chunkers the defect it must not have. No corpus, no model."""

from __future__ import annotations

from . import chunkers, store


def _doc() -> list[str]:
    lines = ["---", "title: x", "---", "# Teil A", ""]
    lines += [" ".join(["wort"] * 60) for _ in range(3)] + [""]          # 180 tokens of prose
    lines += ["## Kurz", "", "nur zwei", ""]                                # a section under min
    lines += ["| a | b |", "|---|---|"] + [f"| {'z ' * 40}| y |" for _ in range(14)] + [""]  # a 600+ token table
    lines += ["# Teil B", "", " ".join(["lang"] * 900)]                     # one line over max
    return lines


def selftest() -> list[str]:
    fails = []
    lines = _doc()
    p = store.chunkers()
    head = chunkers.chunk("t", "Titel", lines, 4, "heading@v1", p["heading@v1"])
    for r in head:
        if r["line_start"] < 4 or r["line_end"] > len(lines):
            fails.append(f"heading@v1 chunk {r} leaves the body")
        if chunkers.chunk_id("t", "heading@v1", r["line_start"], r["line_end"], r["sha"]) != r["id"]:
            fails.append("chunk id does not recompute")
    table = [i + 1 for i, l in enumerate(lines) if l.startswith("|")]
    holders = [r for r in head if r["line_start"] <= table[0] <= r["line_end"]]
    if not holders or holders[0]["line_end"] < table[-1]:
        fails.append(f"heading@v1 split a table: {holders}")
    long_line = len(lines)
    if not any(r["tokens"] > p["heading@v1"]["max"] and r["line_end"] == long_line
               and r["line_start"] >= lines.index("# Teil B") + 1 for r in head):
        fails.append("a line over max did not stay one chunk")
    kurz = lines.index("## Kurz") + 1
    if any(r["line_start"] == kurz for r in head):
        fails.append("a section under min stood alone instead of joining its neighbour")
    if not any(r["prefix"] == "Titel › Teil A" for r in head):
        fails.append(f"prefix is not 'Titel › H1': {[r['prefix'] for r in head]}")
    if any(r["line_start"] <= lines.index("# Teil B") + 1 <= r["line_end"] and r["line_start"] < lines.index("# Teil B")
           for r in head if r["tokens"] >= p["heading@v1"]["min"] and r["line_end"] > lines.index("# Teil B") + 1):
        fails.append("heading@v1 crossed a heading although the chunk had reached min")
    # one paragraph of lines 300 + 400 tokens: below target_min after the first, but together over max
    para = ["# P", " ".join(["a"] * 300), " ".join(["b"] * 400)]
    cut = chunkers.chunk("p", "P", para, 1, "heading@v1", p["heading@v1"])
    if any(r["tokens"] > p["heading@v1"]["max"] and r["line_start"] != r["line_end"]
           and not (r["line_end"] - r["line_start"] == 1 and para[r["line_start"] - 1].startswith("#")) for r in cut):
        fails.append(f"heading@v1 joined lines past max: {[(r['line_start'], r['line_end'], r['tokens']) for r in cut]}")
    sec = chunkers.chunk("t", "Titel", lines, 4, "section@v1", p["section@v1"])
    if [r["heading_path"] for r in sec] != [["Teil A"], ["Teil B"]]:
        fails.append(f"section@v1 expected two top-level sections, got {[r['heading_path'] for r in sec]}")
    flat = ["ein satz ohne überschrift"] * 5
    if len(chunkers.chunk("f", "F", flat, 1, "section@v1", p["section@v1"])) != 1:
        fails.append("section@v1 without headings is not the whole document")
    prose = [" ".join(["w"] * 50) for _ in range(30)]
    win = chunkers.chunk("w", "W", prose, 1, "window400@v1", p["window400@v1"])
    if len(win) < 2 or not all(a["line_end"] >= b["line_start"] for a, b in zip(win, win[1:])):
        fails.append(f"window400@v1 windows do not overlap: {[(r['line_start'], r['line_end']) for r in win]}")
    if chunkers.chunk("w", "W", prose, 1, "window400@v1", p["window400@v1"]) != win:
        fails.append("a chunker is not deterministic")
    long_prose = [" ".join(["w"] * 100) for _ in range(20)]
    long_win = chunkers.chunk("w", "W", long_prose, 1, "window400@v1", p["window400@v1"])
    if not all(a["line_end"] >= b["line_start"] for a, b in zip(long_win, long_win[1:])):
        fails.append("windows fail to overlap when a source line exceeds the overlap budget")
    if chunkers.clean_heading(r"**2\. F\&E**") != "2. F&E":
        fails.append("heading prefix retains Markdown emphasis or Drive escapes")
    return fails


# ── end-to-end gates on a temporary index (review of PR #138) ──────────────────

import contextlib  # noqa: E402
import shutil  # noqa: E402
import tempfile  # noqa: E402
from pathlib import Path  # noqa: E402

import numpy as np  # noqa: E402

from . import build, repo, search, verify  # noqa: E402


class _FakeModel:
    """Deterministic stand-in for the embedder: a hashed bag of words. No download, never a quality claim."""
    dim = 16

    def encode(self, texts, **_):
        import hashlib
        import re
        out = np.zeros((len(texts), self.dim), dtype=np.float32)
        for i, t in enumerate(texts):
            for w in re.findall(r"\w+", t.lower()):
                out[i, int(hashlib.sha1(w.encode()).hexdigest()[:4], 16) % self.dim] += 1
        return out


@contextlib.contextmanager
def fixture(texts: dict[str, str]):
    """A temporary repository with `texts` as its landed sources, the index's paths pointed at it."""
    tmp = Path(tempfile.mkdtemp(prefix="novelgraph-selftest-"))
    drive, index = tmp / "Sources" / "drive", tmp / "Index"
    drive.mkdir(parents=True)
    index.mkdir()
    shutil.copy(store.METHODS, index / "methods.toml")
    for slug, text in texts.items():
        (drive / f"{slug}.md").write_text(text, encoding="utf-8")
    state = {"slugs": list(texts)}

    def docs():
        out = []
        for slug in state["slugs"]:
            p = drive / f"{slug}.md"
            body, offset = repo.subject._split(p.read_text(encoding="utf-8"))
            out.append(repo.subject.Document(slug=slug, category="test", date="?", format="md", sha256="",
                                             path=p, body=body, offset=offset))
        return out

    saved = {(store, k): getattr(store, k) for k in ("METHODS", "MANIFEST", "SOURCES", "BUILD")}
    saved.update({(mod, "documents"): mod.documents for mod in (build, verify, search)})
    saved[(verify, "manifest_rows")] = verify.manifest_rows
    saved[(build, "model")] = build.model
    paths, titles = dict(build._PATHS), dict(build._TITLES)
    try:
        store.METHODS, store.MANIFEST = index / "methods.toml", index / "manifest.jsonl"
        store.SOURCES, store.BUILD = index / "sources", index / "_build"
        store.registry.cache_clear()
        for mod in (build, verify, search):
            mod.documents = docs
        verify.manifest_rows = lambda: [{"slug": s} for s in texts] + [{"slug": "unlanded-audio"}]
        fake = _FakeModel()
        build.model = lambda _name: fake
        build._PATHS.clear()
        build._PATHS.update({s: drive / f"{s}.md" for s in texts})
        build._TITLES.clear()
        build._TITLES.update({s: s.upper() for s in texts})
        search._chunk.cache_clear()
        yield {"root": tmp, "drive": drive, "index": index, "state": state}
    finally:
        for (mod, k), v in saved.items():
            setattr(mod, k, v)
        store.registry.cache_clear()
        build._PATHS.clear()
        build._PATHS.update(paths)
        build._TITLES.clear()
        build._TITLES.update(titles)
        search._chunk.cache_clear()
        shutil.rmtree(tmp, ignore_errors=True)


TEXTS = {"a": "---\ntitle: A\n---\n# A\n\nKael zählt die Sterne über der Stadt.\n\n## Weiter\n\nJuna wartet am Tor.\n",
         "b": "# B\n\nAEGIS löscht das Archiv.\n"}
QUIET = dict(log=lambda *_: None)


def _raises(fn, kind=SystemExit) -> bool:
    try:
        fn()
    except kind:
        return True
    return False


def gates() -> list[str]:
    """The four defects the review of #138 reproduced, each handed to the code that must refuse it."""
    fails = []
    # 1 · a stale source is refused: on opening, during warm use, and when a source leaves the corpus
    with fixture(TEXTS) as fx:
        build.build(**QUIET)
        if verify.verify(rechunk=True)[0]:
            fails.append(f"fixture index does not verify: {verify.verify()[0][:3]}")
        warm = search.Index("heading@v1")
        if not warm.search("Kael Sterne", 3, "bm25"):
            fails.append("fixture search found nothing")
        a = fx["drive"] / "a.md"
        a.write_text(a.read_text(encoding="utf-8").replace("Kael zählt die Sterne", "Nyx erfindet eine Aussage"),
                     encoding="utf-8")
        if not _raises(lambda: warm.search("Kael Sterne", 3, "bm25"), search.Stale):
            fails.append("a source changed during warm use was still answered from")
        if not _raises(lambda: search.Index("heading@v1"), search.Stale):
            fails.append("an index opened over a changed source")
        if not _raises(lambda: search.show([{"slug": "a", "id": build.read_jsonl(store.chunks_path("a", "heading@v1"))[0]["id"],
                                            "line_start": 4, "line_end": 6, "score": 1.0}], "heading@v1"), search.Stale):
            fails.append("show() printed a slice that no longer holds the indexed text")
        build.build(**QUIET)
        fx["state"]["slugs"] = ["b"]
        if not _raises(lambda: search.Index("heading@v1"), search.Stale):
            fails.append("an index opened although a source left the corpus")
    # 2 · a new embedder revision invalidates every vector, the skip and the aggregate
    with fixture(TEXTS) as fx:
        build.build(**QUIET)
        toml = fx["index"] / "methods.toml"
        toml.write_text(toml.read_text(encoding="utf-8").replace(
            store.embedders()["potion-m128"]["revision"], "0" * 40), encoding="utf-8")
        store.registry.cache_clear()
        if not any("embedder" in f for f in verify.verify()[0]):
            fails.append("verify passed vectors made under another embedder revision")
        if not _raises(lambda: search.Index("heading@v1")):
            fails.append("search opened an aggregate made under another embedder revision")
        total = sum(len(build.read_jsonl(store.chunks_path(s, m))) for s in TEXTS for m in store.chunkers())
        got = build.build(**QUIET)
        if got["embedded"] != total or got["reused_vectors"]:
            fails.append(f"a revision change re-embedded {got['embedded']} of {total} chunks, reused {got['reused_vectors']}")
        if verify.verify()[0]:
            fails.append(f"after the rebuild verify still fails: {verify.verify()[0][:2]}")
    # 3 · an aggregate of the right shape with the wrong vectors fails verify
    with fixture(TEXTS) as fx:
        build.build(**QUIET)
        mp = store.build_matrix("heading@v1", store.default_embedder())
        mat = np.load(mp)
        if len(mat) > 1:
            np.save(mp, mat[::-1].copy())
        else:
            np.save(mp, (np.roll(mat, 1, axis=1)).astype(np.float16))
        if not any("differ from" in f for f in verify.verify()[0]):
            fails.append("verify passed an aggregate whose rows are other (unit-length) vectors")
    # 4 · a table without outer pipes is never split
    rows = [" | ".join(["zelle " * 12] * 2) for _ in range(25)]
    lines = ["# T", "", "a | b", "--- | ---", *rows]
    got = chunkers.chunk("t", "T", lines, 1, "heading@v1", store.chunkers()["heading@v1"])
    if not any(r["line_start"] <= 3 and r["line_end"] >= len(lines) for r in got):
        fails.append(f"a table without outer pipes was split: {[(r['line_start'], r['line_end']) for r in got]}")
    if 4 not in chunkers.table_lines(chunkers.parse(lines, 1)) or 1 in chunkers.table_lines(chunkers.parse(lines, 1)):
        fails.append("table_lines() misreads the header/delimiter rule")
    return fails


def publication_gates() -> list[str]:
    """Interrupted writes, lexical corruption, warm freshness and locking, without a model."""
    import sqlite3
    import subprocess
    import sys
    fails = []
    with fixture(TEXTS):
        original = build._title
        title = ["Original"]
        try:
            build._title = lambda slug: {"title": title[0]}
            build.build(**QUIET)
            ids = build.read_jsonl(store.chunks_path("a", "heading@v1"))
            title[0] = "Renamed"
            got = build.build(**QUIET)
            if [r["id"] for r in ids] != [r["id"] for r in build.read_jsonl(store.chunks_path("a", "heading@v1"))]:
                fails.append("a title change moved chunk ids")
            if not got["embedded"] or got["reused_vectors"]:
                fails.append("a changed prefix reused embeddings made with the old title")
        finally:
            build._title = original
    with fixture(TEXTS) as fx:
        build.build(**QUIET)
        warm = search.Index("heading@v1")
        tracked = [store.MANIFEST, *store.SOURCES.rglob("source.json"), *store.SOURCES.rglob("chunks/*.jsonl")]
        before = {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in tracked}
        again = build.build(**QUIET)
        if again["embedded"] or again["rechunked"] or again["concatenated"]:
            fails.append(f"no-op build changed outputs: {again}")
        if before != {p: (p.read_bytes(), p.stat().st_mtime_ns) for p in tracked}:
            fails.append("no-op build rewrote committed artifacts")
        if not warm.search("Kael", 2, "bm25"):
            fails.append("a no-op build invalidated warm search")
        info = verify.verify()[1]["catalogue"]
        if info != {"total": 3, "landed": 2, "indexed": 2, "unlanded": ["unlanded-audio"]}:
            fails.append(f"catalogue coverage hides unlanded rows: {info}")
        # A source outside the result set must also stop warm queries.
        b = fx["drive"] / "b.md"
        b.write_text("# B\n\nAndere Aussage.\n", encoding="utf-8")
        if not _raises(lambda: warm.search("Kael", 1, "bm25"), search.Stale):
            fails.append("warm search ignored a changed non-hit source")
        build.build(**QUIET)
        if not _raises(lambda: warm.search("Kael", 1, "bm25"), search.Stale):
            fails.append("warm search mixed old and rebuilt generations")
        # Keep row count and rowids, replace every posting: the old count-only gate passed this.
        bp = store.build_bm25("heading@v1")
        with sqlite3.connect(bp) as con:
            n = con.execute("SELECT count(*) FROM chunks").fetchone()[0]
            con.execute("INSERT INTO chunks(chunks) VALUES ('delete-all')")
            con.executemany("INSERT INTO chunks(rowid,text,lemmata) VALUES (?,?,?)",
                            [(i, "fabricated", "fabricated") for i in range(1, n + 1)])
        if not any("FTS postings" in f for f in verify.verify()[0]):
            fails.append("verify accepted wrong FTS postings with correct rowids/count")
        build.build(force=True, **QUIET)
        lp = store.lex_path("a", "heading@v1")
        rows = build.read_jsonl(lp)
        rows[0]["lemmata"] = "fabricated"
        build.write_jsonl(lp, rows)
        if not any("lexical derivation" in f for f in verify.verify()[0]):
            fails.append("verify accepted corrupt lex terms with correct ids")
        # Fail after marking the build dirty; both cold and warm readers must refuse it.
        real = build._build
        try:
            def crash(*args, **kwargs):
                raise OSError("injected publication failure")
            build._build = crash
            if not _raises(lambda: build.build(**QUIET), OSError):
                fails.append("injected build failure did not occur")
        finally:
            build._build = real
        if not store.dirty_path().exists():
            fails.append("failed build left no interruption marker")
        for fn in (lambda: search.Index("heading@v1"), lambda: warm.search("Kael"), lambda: verify.verify()):
            if not _raises(fn):
                fails.append("reader accepted an interrupted publication")
        if not _raises(lambda: build.build(source="a", **QUIET)):
            fails.append("partial build claimed to recover a global interruption")
        build.build(**QUIET)
        if store.dirty_path().exists() or verify.verify()[0]:
            fails.append("full rebuild failed to recover interrupted/corrupt artifacts")
        # Real OS locks, not a mock: both another reader and writer must wait.
        probe = "import fcntl,sys; f=open(sys.argv[1],'a'); fcntl.flock(f, int(sys.argv[2]) | fcntl.LOCK_NB)"
        with store.lock(write=True):
            for flag in (1, 2):  # LOCK_SH, LOCK_EX
                done = subprocess.run([sys.executable, "-c", probe, str(store.MANIFEST.parent / ".lock"), str(flag)],
                                      capture_output=True)
                if done.returncode == 0 or b"BlockingIOError" not in done.stderr:
                    fails.append(f"writer lock did not block competing lock {flag}")
        with store.lock():
            done = subprocess.run([sys.executable, "-c", probe, str(store.MANIFEST.parent / ".lock"), "2"],
                                  capture_output=True)
            if done.returncode == 0:
                fails.append("reader lock did not block a writer")
        # An invalid matrix dimension cannot be concatenated into a plausible empty aggregate.
        mp = store.vec_meta_path("b", "heading@v1", store.default_embedder())
        obj = __import__("json").loads(mp.read_text())
        obj["dim"] += 1
        store.write_json(mp, obj)
        if not _raises(lambda: build.concatenate("heading@v1", store.default_embedder(), force=True)):
            fails.append("concatenation accepted mixed recorded dimensions")
    return fails
