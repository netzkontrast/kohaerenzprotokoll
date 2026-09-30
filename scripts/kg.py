"""Local GraphQLite CLI over the existing, source-attributed wiki graph.

Install: scripts/install.sh graphqlite
Run: .venv-graphqlite/bin/python scripts/kg.py --help

The database is a disposable projection of graph.py, never an authoring layer.
Indexing writes only Plan/derived/ask.db. Reads refuse missing or stale
indexes. No model, network, MCP server or conflict inference is involved.
Personalized PageRank and MMR remain graphrag.py's implementation; GraphQLite's
global PageRank is not an equivalent replacement. Context size is capped in
UTF-8 bytes, including JSON metadata, not advertised as an exact token count.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from pathlib import Path
import sqlite3
import sys

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
VERSION = 2
DEPENDENCY = "0.8.0"
DATABASE = ROOT / "Plan/derived/ask.db"


class Refused(Exception):
    pass


def compact(value):
    return json.dumps(value, ensure_ascii=False, separators=(",", ":"), sort_keys=True)


def digest(value):
    return hashlib.sha256(compact(value).encode()).hexdigest()


def payload(value):
    # GraphQLite decodes JSON-looking string properties in query results.
    return value if isinstance(value, dict) else json.loads(value)


def inputs(root=ROOT):
    """Hash authoritative inputs, including source text used by quotes.verdict.

    This scans bytes, not LLM context. On change, rebuild the entire projection;
    unchanged inputs are a no-op. Partial per-file graph updates are not built.
    """
    import askdb
    return askdb.inputs(root)


def engine(path):
    try:
        from importlib.metadata import version
        from graphqlite import Graph
    except ImportError as exc:
        raise Refused("GraphQLite absent: run scripts/install.sh graphqlite, then use .venv-graphqlite/bin/python") from exc
    if version("graphqlite") != DEPENDENCY:
        raise Refused(f"GraphQLite {DEPENDENCY} required: run scripts/install.sh graphqlite")
    return Graph(path)


def evidence_rows(graph):
    rows = {}
    for page, items in sorted(graph["evidence"].items()):
        for item in items:
            row = dict(item, page=page)
            key = "evidence:" + digest(row)
            rows[key] = dict(row, id=key)
    return rows


def metadata(db):
    try:
        with sqlite3.connect(f"{db.resolve().as_uri()}?mode=ro", uri=True) as conn:
            return json.loads(conn.execute("SELECT payload FROM kp_meta").fetchone()[0])
    except (sqlite3.Error, TypeError, ValueError) as exc:
        raise Refused("missing or invalid index: run kg.py index") from exc


def freshness(db, root=ROOT):
    meta = metadata(db)
    current = inputs(root)
    if meta.get("version") != VERSION or meta.get("inputs") != current:
        raise Refused("stale index: run kg.py index; changed or deleted inputs invalidate stored evidence")
    return meta


def publish(graph, db, hashes):
    import askdb
    nodes = {k: ({name: askdb.scalar(value) for name, value in n.items() if name != "id"}, n["type"].capitalize())
             for k, n in graph["nodes"].items()}
    edges = [(e["source"], e["target"], {"via": e["via"]}, e["type"].upper()) for e in graph["edges"]]
    data = askdb.with_core({"nodes": nodes, "edges": edges, "quotes": []}, graph)
    askdb.publish(data, db, hashes, [])
    return metadata(db)


def index(db=DATABASE):
    import askdb
    try:
        result = askdb.build(db)
    except ValueError as exc:
        raise Refused(str(exc)) from exc
    return {**result, **{k: v for k, v in metadata(db).items() if k != "inputs"}}


def read_graph(db):
    """Recover exactly graph.py's core graph, excluding the new Evidence nodes."""
    g = engine(str(db))
    try:
        nodes = [payload(r["payload"]) for r in g.query("MATCH (n:Core) RETURN n.payload AS payload ORDER BY n.ordinal")]
        edges = [payload(r["payload"]) for r in g.query(
            "MATCH (a:Core)-[r]->(b:Core) WHERE r.core = true RETURN r.payload AS payload ORDER BY r.ordinal")]
        evidence = {}
        for r in g.query("MATCH (n:Evidence) RETURN n.payload AS payload"):
            row = payload(r["payload"])
            page = row.pop("page")
            row.pop("id")
            evidence.setdefault(page, []).append(row)
        for node in nodes:
            if node["type"] == "term":
                evidence.setdefault(node["slug"], [])
        return {"nodes": {n["id"]: n for n in nodes}, "edges": edges, "evidence": evidence}
    finally:
        g.close()


def search(db, query, limit):
    # Treat user input as literal FTS words; no query syntax is interpolated.
    import re
    words = re.findall(r"\w+", query)
    if not words:
        return {"evidence": [], "reason": "no search words"}
    match = " OR ".join('"' + w.replace('"', '""') + '"' for w in words)
    with sqlite3.connect(db) as conn:
        rows = conn.execute("SELECT e.payload, bm25(kp_fts) FROM kp_fts JOIN kp_evidence e "
                            "ON e.id=kp_fts.id WHERE kp_fts MATCH ? ORDER BY bm25(kp_fts), e.id LIMIT ?",
                            (match, limit)).fetchall()
    return {"evidence": [{**json.loads(p), "rank": rank} for p, rank in rows]}


def around(db, node, hops, limit):
    g = engine(str(db))
    try:
        if not g.query("MATCH (n:Core {id: $id}) RETURN n.id AS id", {"id": node}):
            raise Refused(f"no core node {node!r}")
        found, frontier, edges = {node: 0}, {node}, []
        truncated = False
        for depth in range(1, hops + 1):
            nxt = set()
            for key in sorted(frontier):
                rows = g.query("MATCH (a:Core {id: $id})-[r]-(b:Core) "
                               "WHERE r.core = true RETURN b.id AS id, r.payload AS payload ORDER BY b.id, r.ordinal LIMIT " + str(limit + 1), {"id": key})
                if len(rows) > limit:
                    truncated = True
                for r in rows[:limit]:
                    edge = payload(r["payload"])
                    if edge not in edges:
                        if len(edges) >= limit:
                            truncated = True
                            continue
                        edges.append(edge)
                    if r["id"] not in found:
                        found[r["id"]] = depth
                        nxt.add(r["id"])
            frontier = nxt
            if not frontier:
                break
        return {"nodes": found, "edges": edges, "truncated": truncated}
    finally:
        g.close()


def bounded_context(pack, max_bytes):
    """Keep quotations whole, preserve conflict/question metadata, report omissions."""
    result = {k: pack[k] for k in ("query", "seeds", "terms", "conflicts", "questions")}
    result.update(evidence=[], omitted=len(pack["evidence"]), incomplete=True,
                  no_evidence=not pack["evidence"], max_bytes=max_bytes)
    # Reserve the final CLI newline as part of the serialized output budget.
    if len(compact(result).encode()) + 1 > max_bytes:
        raise Refused("budget cannot hold conflict/question metadata: increase --max-bytes")
    seen = set()
    for row in pack["evidence"]:
        identity = (row["doc"], row["line"], row["quote"])
        if identity in seen:
            continue
        seen.add(identity)
        candidate = row
        trial = {**result, "evidence": result["evidence"] + [candidate], "omitted": result["omitted"] - 1}
        if len(compact(trial).encode()) + 1 <= max_bytes:
            result = trial
    result["incomplete"] = result["omitted"] > 0
    # 'false' has one more byte than 'true'; recheck the final serialized form.
    if len(compact(result).encode()) + 1 > max_bytes:
        result["incomplete"] = True
    return result


def context(db, query, max_bytes):
    import graphrag
    graph = read_graph(db)
    pack = graphrag.retrieve(query, graph=graph, budget=64)
    ids = evidence_rows(graph)
    lookup = {(r["page"], r["doc"], r["line"], r["quote"], r["section"], r["page_line"]): key for key, r in ids.items()}
    for row in pack["evidence"]:
        row["id"] = lookup[(row["page"], row["doc"], row["line"], row["quote"], row["section"], row["page_line"])]
    result = bounded_context(pack, max_bytes)
    result["incomplete"] = result["incomplete"] or pack["not_selected"] > 0
    return result


def evidence(db, ids):
    out = []
    with sqlite3.connect(db) as conn:
        for key in ids:
            row = conn.execute("SELECT payload FROM kp_evidence WHERE id=?", (key,)).fetchone()
            if row is None:
                raise Refused(f"no evidence {key!r}; obtain IDs from search/context")
            item = json.loads(row[0])
            if item["status"] != "verified":
                raise Refused(f"evidence {key!r} is {item['status']}")
            out.append(item)
    return {"evidence": out}


def positive(value):
    number = int(value)
    if number <= 0:
        raise argparse.ArgumentTypeError("must be positive")
    return number


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--db", type=Path, default=DATABASE, help="derived index; default Plan/derived/ask.db")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("index", help="rebuild on input change; unchanged input is a no-op")
    commands.add_parser("check", help="fail if absent or stale")
    s = commands.add_parser("search", help="FTS5 over verified evidence")
    s.add_argument("query")
    s.add_argument("--limit", type=positive, default=10)
    c = commands.add_parser("context", help="existing PPR/MMR with a hard UTF-8 output cap")
    c.add_argument("query")
    c.add_argument("--max-bytes", type=positive, default=12000)
    a = commands.add_parser("around", help="bounded Cypher traversal with edge provenance")
    a.add_argument("node")
    a.add_argument("--hops", type=positive, choices=range(1, 4), default=1)
    a.add_argument("--limit", type=positive, default=50)
    e = commands.add_parser("evidence", help="fetch complete verified evidence by returned IDs")
    e.add_argument("ids", nargs="+")
    args = parser.parse_args(argv)
    try:
        if not args.db.resolve().is_relative_to((ROOT / "Plan/derived").resolve()) or args.db.suffix != ".db":
            raise Refused("database must be a .db under Plan/derived; this command writes only derived data")
        if args.command == "index":
            output = index(args.db)
        else:
            meta = freshness(args.db)
            if args.command == "check":
                output = {"status": "fresh", **{k: v for k, v in meta.items() if k != "inputs"}}
            elif args.command == "search":
                output = search(args.db, args.query, min(args.limit, 100))
            elif args.command == "context":
                output = context(args.db, args.query, args.max_bytes)
            elif args.command == "around":
                output = around(args.db, args.node, args.hops, min(args.limit, 100))
            else:
                output = evidence(args.db, args.ids)
            # An edit while reading must not turn old evidence into a fresh answer.
            freshness(args.db)
        print(compact(output))
        return 0
    except (Refused, sqlite3.Error, OSError, ValueError) as exc:
        print(compact({"status": "refused", "reason": str(exc)}), file=sys.stderr)
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
