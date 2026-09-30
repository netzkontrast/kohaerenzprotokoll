"""The BM25 relation: a line that shares words with a name without writing it — a proposal, ranked by what readers judged.

The author, 2026-09-30, on „Große Stille" and a line reading „Das große Schweigen":
„Die große Stille darf durchaus mit dem großen Schweigen gematcht werden… hier ergibt
sich eine Spannung zwischen Schweigen und Stille", then: „They Need to have a Special
Graph Relation - we Call it bm25 Relation - and we can learn how to Rank those".

So a loose match is kept, as its own relation, never as a count or a merge:

    (term:<page> | line:<slug>:<n>) -[:P_BM25 {query, score, rank}]-> (line:<slug>:<n>)

- **found** by `askdb.fts_query` over the `lines` table of the shared store,
  `Plan/derived/ask.db` (FTS5 `bm25()`), which refuses a stale store as every
  reader of it does (`kg.py index` rebuilds it). The source's own document is left
  out, so is every line that writes one of the query's surfaces exactly — those
  are the named channel, a count — and every frontmatter line: a `slug:` or
  `title:` line shares a page's words and says nothing about the thing;
- **kept** in `Plan/runs/bm25/relations.jsonl`, one row per relation, its id a hash
  of source, target and method, so a second finding adds nothing;
- **judged** in `Plan/runs/bm25/verdicts.jsonl`: `tension`, `parallel`, `same` or
  `noise`, by whom, with a note. The first three say the relation is worth a
  reader's time, and noise says it is not;
- **loaded** by the store's one build (`kg.py index`, `askdb.py build`) as `P_BM25`
  edges carrying the latest verdict. Like every `P_` type they stay out of the core
  ranking, paths and communities, and no query for stated facts names one;
- **ranked** by `rank`: a logistic model over each relation's features once
  `fit` has enough verdicts of both kinds, and by the raw BM25 score until then.
  `fit` says how many verdicts it has and refuses below `MIN_VERDICTS`. A ranker
  learned from four verdicts is a guess (P18).

    python3 scripts/bm25rel.py find <source> "<query>" [--exclude <slug>] [--k 3]
    python3 scripts/bm25rel.py label <id> tension|parallel|same|noise --by "<who>" [--note "…"]
    python3 scripts/bm25rel.py fit            # learn the weights; refuses with too few verdicts
    python3 scripts/bm25rel.py rank [--top 20]
    python3 scripts/bm25rel.py selftest

A relation says two lines share words. That a reader judged it a tension is a
verdict with a name on it. Neither is a reading, and neither enters `Wiki/`.
Standard library only.
"""

from __future__ import annotations

import datetime
import hashlib
import json
import math
import re
import sqlite3
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

DB = ROOT / "Plan" / "derived" / "ask.db"
FOLDER = ROOT / "Plan" / "runs" / "bm25"
VERDICTS = ("tension", "parallel", "same", "noise")
RELEVANT = {"tension", "parallel", "same"}
MIN_VERDICTS = 12          # of each kind, relevant and noise, before fit learns anything
FEATURES = ("score", "rank", "overlap", "prefix", "target_read", "same_category", "listy", "length")


def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def rel_id(source: str, target: str, method: str = "bm25") -> str:
    return "bm25:" + hashlib.sha1(f"{source}|{target}|{method}".encode()).hexdigest()[:12]


def words(text: str) -> list[str]:
    return [w.lower() for w in re.findall(r"\w[\w-]*", text) if len(w) > 2]


def features(row: dict, read: set[str], category: dict[str, str]) -> dict:
    """What a relation looks like, by code: the numbers a ranker weighs."""
    q, t = set(words(row["query"])), words(row["target_text"])
    tset = set(t)
    src_slug = row["source"].split(":")[1] if row["source"].startswith("line:") else None
    tgt_slug = row["target"].split(":")[1]
    return {"score": -float(row["score"]),                     # FTS5's bm25() is lower-is-better
            "rank": float(row["rank"]),
            "overlap": len(q & tset) / len(q) if q else 0.0,
            "prefix": len({w[:5] for w in q} & {w[:5] for w in tset}) / len(q) if q else 0.0,
            "target_read": 1.0 if tgt_slug in read else 0.0,
            "same_category": 1.0 if src_slug and category.get(src_slug) == category.get(tgt_slug) else 0.0,
            "listy": 1.0 if re.match(r"\s*(?:[-*|]|\d+\.)", row["target_text"]) else 0.0,
            "length": min(len(t), 60) / 60}


_BODY: dict[str, int] = {}


def body_starts(slug: str, root: Path = ROOT) -> int:
    """The file line a document's body starts on — `subject.py`'s boundary, the only one."""
    if slug not in _BODY:
        import subject
        path = root / "Sources" / "drive" / f"{slug}.md"
        _BODY[slug] = subject._split(path.read_text(encoding="utf-8"))[1] if path.exists() else 1
    return _BODY[slug]


class Stale(SystemExit):
    pass


def fresh_or_refuse(db: Path = DB) -> None:
    """The shared store's contract: a read refuses a missing or stale snapshot."""
    import askdb
    why = askdb.fresh(db)
    if why:
        raise Stale(why + " — or: .venv-graphqlite/bin/python scripts/kg.py index")


def find(source: str, query: str, exclude: list[str] | None = None, surfaces: list[str] | None = None,
         k: int = 3, db: Path = DB, found_by: str = "", stale_ok: bool = False,
         root: Path = ROOT) -> list[dict]:
    """The k body lines nearest the query by BM25 that write none of its surfaces exactly."""
    import askdb
    match = askdb.fts_query(query)
    if not match or not db.exists():
        return []
    if not stale_ok:
        fresh_or_refuse(db)
    exact = [re.compile(rf"(?<!\w){re.escape(s)}(?!\w)") for s in (surfaces or [query])]
    sql = sqlite3.connect(f"{db.resolve().as_uri()}?mode=ro", uri=True)
    rows = sql.execute("SELECT slug, line, text, bm25(lines) FROM lines WHERE lines MATCH ? "
                       "ORDER BY bm25(lines) LIMIT ?", (match, 50 + 10 * k)).fetchall()
    sql.close()
    out = []
    for slug, line, text, score in rows:
        if slug in (exclude or []) or any(p.search(text) for p in exact):
            continue
        if int(line) < body_starts(slug, root):
            continue
        target = f"line:{slug}:{line}"
        out.append({"id": rel_id(source, target), "source": source, "query": query, "target": target,
                    "target_text": text.strip()[:300], "score": round(score, 4), "rank": len(out) + 1,
                    "method": "bm25", "found_by": found_by, "at": datetime.date.today().isoformat()})
        if len(out) == k:
            break
    return out


def keep(rows: list[dict], folder: Path = FOLDER) -> int:
    """Append the relations not yet kept; the id makes a second finding a no-op."""
    folder.mkdir(parents=True, exist_ok=True)
    have = {r["id"] for r in read_jsonl(folder / "relations.jsonl")}
    new = [r for r in rows if r["id"] not in have]
    with open(folder / "relations.jsonl", "a", encoding="utf-8") as fh:
        for r in new:
            fh.write(json.dumps(r, ensure_ascii=False) + "\n")
    return len(new)


def relations(folder: Path = FOLDER) -> list[dict]:
    """Every kept relation with its latest verdict, as the store loads them."""
    latest = {v["id"]: v for v in read_jsonl(folder / "verdicts.jsonl")}
    return [dict(r, verdict=latest[r["id"]]["verdict"] if r["id"] in latest else "")
            for r in read_jsonl(folder / "relations.jsonl")]


def label(rid: str, verdict: str, by: str, note: str = "", folder: Path = FOLDER) -> dict:
    if verdict not in VERDICTS:
        raise SystemExit(f"a verdict is one of {', '.join(VERDICTS)}")
    if rid not in {r["id"] for r in read_jsonl(folder / "relations.jsonl")}:
        raise SystemExit(f"no relation {rid} in {folder / 'relations.jsonl'}")
    row = {"id": rid, "verdict": verdict, "by": by, "note": note, "at": datetime.date.today().isoformat()}
    with open(folder / "verdicts.jsonl", "a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    return row


def context() -> tuple[set[str], dict[str, str]]:
    read = {p.stem for p in (ROOT / "Sources" / "terms").glob("*.md")}
    category = {}
    manifest = ROOT / "Sources" / "manifest.jsonl"
    for r in read_jsonl(manifest):
        category[r.get("slug")] = r.get("category")
    return read, category


def fit(folder: Path = FOLDER, min_verdicts: int = MIN_VERDICTS) -> dict:
    """Logistic weights over FEATURES from the verdicts; refused below min_verdicts of each kind."""
    rels = {r["id"]: r for r in read_jsonl(folder / "relations.jsonl")}
    latest = {v["id"]: v for v in read_jsonl(folder / "verdicts.jsonl") if v["id"] in rels}
    pos = [i for i, v in latest.items() if v["verdict"] in RELEVANT]
    neg = [i for i, v in latest.items() if v["verdict"] == "noise"]
    if len(pos) < min_verdicts or len(neg) < min_verdicts:
        return {"fitted": False, "relevant": len(pos), "noise": len(neg), "needed": min_verdicts,
                "why": f"{len(pos)} relevant and {len(neg)} noise verdicts; each needs {min_verdicts}"}
    read, category = context()
    data = [(features(rels[i], read, category), 1.0) for i in pos] + \
           [(features(rels[i], read, category), 0.0) for i in neg]
    w = {f: 0.0 for f in FEATURES}
    b = 0.0
    for _ in range(2000):                              # plain gradient descent, small L2
        gw, gb = {f: 0.0 for f in FEATURES}, 0.0
        for x, y in data:
            p = 1 / (1 + math.exp(-(b + sum(w[f] * x[f] for f in FEATURES))))
            for f in FEATURES:
                gw[f] += (p - y) * x[f]
            gb += p - y
        for f in FEATURES:
            w[f] -= 0.1 * (gw[f] / len(data) + 0.01 * w[f])
        b -= 0.1 * gb / len(data)
    model = {"fitted": True, "weights": w, "bias": b, "relevant": len(pos), "noise": len(neg),
             "at": datetime.date.today().isoformat()}
    (folder / "ranker.json").write_text(json.dumps(model, indent=2) + "\n", encoding="utf-8")
    return model


def rank(top: int = 20, folder: Path = FOLDER) -> list[tuple[float, dict]]:
    rels = read_jsonl(folder / "relations.jsonl")
    judged = {v["id"] for v in read_jsonl(folder / "verdicts.jsonl")}
    model_file = folder / "ranker.json"
    model = json.loads(model_file.read_text(encoding="utf-8")) if model_file.exists() else {"fitted": False}
    read, category = context()
    scored = []
    for r in rels:
        if r["id"] in judged:
            continue
        x = features(r, read, category)
        s = (model["bias"] + sum(model["weights"][f] * x[f] for f in FEATURES)) if model.get("fitted") else x["score"]
        scored.append((s, r))
    return sorted(scored, key=lambda sr: -sr[0])[:top]


def selftest() -> int:
    cases = []
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp)
        db = folder / "ask.db"
        sql = sqlite3.connect(str(db))
        sql.execute("CREATE VIRTUAL TABLE lines USING fts5(slug, line UNINDEXED, text, tokenize='unicode61 remove_diacritics 2')")
        sql.executemany("INSERT INTO lines VALUES (?,?,?)", [
            ("a", 20, "Kael nennt dies die Große Stille."), ("b", 252, "Das große Schweigen, Isolationskammer."),
            ("c", 3, "Die Große Stille kehrt zurück."), ("d", 9, "Nichts davon hier."),
            ("e", 2, 'title: "Das große Schweigen"')])
        sql.commit()
        drive = folder / "Sources" / "drive"
        drive.mkdir(parents=True)
        (drive / "e.md").write_text('---\ntitle: "Das große Schweigen"\n---\nText.\n', encoding="utf-8")
        try:
            find("line:a:20", "Große Stille", exclude=["a"], k=3, db=db)
            cases.append(("a store without its build's metadata is refused as stale", False))
        except Stale:
            cases.append(("a store without its build's metadata is refused as stale", True))
        rows = find("line:a:20", "Große Stille", exclude=["a"], k=3, db=db, found_by="selftest",
                    stale_ok=True, root=folder)
        cases.append(("the loose match is found: Schweigen for Stille", [r["target"] for r in rows] == ["line:b:252"]))
        cases.append(("a frontmatter line is no relation", all(not r["target"].startswith("line:e:") for r in rows)))
        cases.append(("a line writing the name exactly is the named channel, not a relation",
                      all(r["target"] != "line:c:3" for r in rows)))
        cases.append(("the source's own document is left out", all(not r["target"].startswith("line:a:") for r in rows)))
        cases.append(("a second finding adds nothing", keep(rows, folder) == 1 and keep(rows, folder) == 0))
        row = label(rows[0]["id"], "tension", "selftest", "Schweigen und Stille", folder)
        cases.append(("a verdict is kept with its name", row["verdict"] == "tension" and row["by"] == "selftest"))
        cases.append(("the store loads a relation with its latest verdict",
                      [r["verdict"] for r in relations(folder)] == ["tension"]))
        try:
            label(rows[0]["id"], "interesting", "selftest", "", folder)
            cases.append(("an unknown verdict is refused", False))
        except SystemExit:
            cases.append(("an unknown verdict is refused", True))
        cases.append(("fit refuses with too few verdicts", fit(folder)["fitted"] is False))
        extra = [{"id": f"bm25:x{i}", "source": "term:p", "query": "Große Stille", "target": f"line:z:{i}",
                  "target_text": ("Das große Schweigen" if i % 2 else "- Liste, Punkt, Tabelle"),
                  "score": -5.0 + (i % 2), "rank": 1 + i % 3, "method": "bm25"} for i in range(8)]
        keep(extra, folder)
        for i, r in enumerate(extra):
            label(r["id"], "tension" if i % 2 else "noise", "selftest", "", folder)
        model = fit(folder, min_verdicts=4)
        cases.append(("fit learns from both kinds", model["fitted"] and model["weights"]["listy"] < 0))
    failed = [n for n, ok in cases if not ok]
    print(f"bm25rel: {len(cases) - len(failed)} of {len(cases)} cases hold"
          + (" — FAILED: " + ", ".join(failed) if failed else ""))
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        return selftest()
    if argv[:1] == ["find"] and len(argv) >= 3:
        exclude = [argv[argv.index("--exclude") + 1]] if "--exclude" in argv else []
        k = int(argv[argv.index("--k") + 1]) if "--k" in argv else 3
        rows = find(argv[1], argv[2], exclude=exclude, k=k, found_by=f"bm25rel.py find {argv[1]}")
        print(f"{keep(rows)} new of {len(rows)}")
        for r in rows:
            print(f"  {r['id']}  {r['target']}  {r['score']}  {r['target_text'][:110]}")
        return 0
    if argv[:1] == ["label"] and len(argv) >= 3:
        by = argv[argv.index("--by") + 1] if "--by" in argv else "unnamed"
        note = argv[argv.index("--note") + 1] if "--note" in argv else ""
        print(json.dumps(label(argv[1], argv[2], by, note), ensure_ascii=False))
        return 0
    if argv[:1] == ["fit"]:
        print(json.dumps(fit(), ensure_ascii=False, indent=1))
        return 0
    if argv[:1] == ["rank"]:
        top = int(argv[argv.index("--top") + 1]) if "--top" in argv else 20
        for s, r in rank(top):
            print(f"  {s:8.3f}  {r['id']}  {r['source']} → {r['target']}  {r['target_text'][:90]}")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
