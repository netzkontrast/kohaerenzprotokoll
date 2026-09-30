"""Portable graph snapshots: logical JSONL in deterministic gzip, never a SQL dump.

Called by kg.py export and automatically by kg.py index on a fresh/stale store.
Graph/manifest.json publishes one complete, content-addressed snapshot. The
Markdown view is navigation only; editing it never modifies stored facts.
"""
from __future__ import annotations

import gzip
import hashlib
import json
import os
from pathlib import Path
import re
import sqlite3
import tempfile

import askdb

ROOT = askdb.ROOT
DIRECTORY = ROOT / "Graph"
FORMAT = 1
TYPES = ("text", "int", "real", "bool", "json")
FTS = {"lines": "slug UNINDEXED, line UNINDEXED, text",
       "quotes": "slug UNINDEXED, line UNINDEXED, text, page UNINDEXED",
       "kp_fts": "id UNINDEXED, quote, page, section"}
TABLES = {"lines": 3, "quotes": 4, "kp_evidence": 2, "kp_fts": 4}


def sha(path):
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def records(conn):
    """External IDs, typed property values and every parallel edge, in order."""
    keys = dict(conn.execute("SELECT id,key FROM property_keys"))
    id_key = next(k for k, v in keys.items() if v == "id")
    ids = dict(conn.execute("SELECT node_id,value FROM node_props_text WHERE key_id=?", (id_key,)))
    labels = {}
    for node, label in conn.execute("SELECT node_id,label FROM node_labels"):
        labels.setdefault(node, []).append(label)
    for kind in ("node", "edge"):
        props = {}
        for typ in TYPES:
            for row, key, value in conn.execute(f"SELECT * FROM {kind}_props_{typ}"):
                props.setdefault(row, {})[keys[key]] = [typ, value]
        if kind == "node":
            for (node,) in conn.execute("SELECT id FROM nodes ORDER BY id"):
                yield {"record": "node", "id": ids[node], "labels": sorted(labels[node]), "props": props.get(node, {})}
        else:
            for edge, source, target, typ in conn.execute("SELECT id,source_id,target_id,type FROM edges ORDER BY id"):
                yield {"record": "edge", "source": ids[source], "target": ids[target], "type": typ, "props": props.get(edge, {})}
    for table in TABLES:
        if table == "lines":
            continue  # source text already lives in immutable Sources/drive
        for row in conn.execute(f"SELECT * FROM {table} ORDER BY rowid"):
            yield {"record": table, "row": row}


def atomic_json(path, value):
    fd, name = tempfile.mkstemp(prefix=".manifest-", dir=path.parent)
    try:
        with os.fdopen(fd, "w", encoding="utf-8") as f:
            f.write(askdb.compact(value) + "\n")
        os.replace(name, path)
    finally:
        Path(name).unlink(missing_ok=True)


def export(db=askdb.DB, directory=DIRECTORY):
    import kg
    hashes = askdb.inputs()
    meta = kg.freshness(db)
    directory.mkdir(parents=True, exist_ok=True)
    archives = directory / "snapshots"
    archives.mkdir(exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".snapshot-", dir=archives)
    os.close(fd)
    temp = Path(name)
    raw_hash, counts = hashlib.sha256(), {}
    try:
        with sqlite3.connect(f"{db.resolve().as_uri()}?mode=ro", uri=True) as conn:
            conn.execute("BEGIN")
            stats = json.loads(conn.execute("SELECT value FROM meta WHERE key='stats'").fetchone()[0])
            if askdb.storage_hash(conn) != stats["storage_hash"]:
                raise ValueError("database integrity changed: rebuild before export")
            header = {"record": "header", "format": FORMAT, "version": askdb.SCHEMA_VERSION,
                      "dependency": askdb.DEPENDENCY, "source_lines": "authoritative-files", "meta": meta, "stats": stats}
            with temp.open("wb") as f, gzip.GzipFile(filename="", fileobj=f, mode="wb", mtime=0) as out:
                for record in (header,):
                    out.write((askdb.compact(record) + "\n").encode())
                for record in records(conn):
                    data = (askdb.compact(record) + "\n").encode()
                    raw_hash.update(data)
                    out.write(data)
                    key = record["record"]
                    counts[key] = counts.get(key, 0) + 1
        if askdb.inputs() != hashes:
            raise ValueError("inputs changed during snapshot export")
        checksum = sha(temp)
        target = archives / f"{checksum}.jsonl.gz"
        os.replace(temp, target)
        manifest = {"format": FORMAT, "version": askdb.SCHEMA_VERSION, "dependency": askdb.DEPENDENCY,
                    "sha256": checksum, "logical_sha256": raw_hash.hexdigest(), "inputs": hashes,
                    "counts": counts, "bytes": target.stat().st_size}
        # Immutable archive first; one atomic pointer publishes the generation.
        atomic_json(directory / "manifest.json", manifest)
        markdown(db, directory, manifest)
        return {"status": "exported", "snapshot": str(target.relative_to(directory)), **manifest}
    finally:
        temp.unlink(missing_ok=True)


def load_manifest(directory, hashes):
    manifest = json.loads((directory / "manifest.json").read_text(encoding="utf-8"))
    for key, want in (("format", FORMAT), ("version", askdb.SCHEMA_VERSION), ("dependency", askdb.DEPENDENCY), ("inputs", hashes)):
        if manifest.get(key) != want:
            raise ValueError(f"snapshot {key} does not match current checkout")
    checksum = manifest.get("sha256", "")
    if not re.fullmatch(r"[0-9a-f]{64}", checksum):
        raise ValueError("invalid snapshot checksum")
    archive = directory / "snapshots" / f"{checksum}.jsonl.gz"
    if sha(archive) != checksum:
        raise ValueError("snapshot archive checksum mismatch")
    return manifest, archive


def restore(db=askdb.DB, directory=DIRECTORY):
    hashes = askdb.inputs()
    manifest, archive = load_manifest(directory, hashes)
    db.parent.mkdir(parents=True, exist_ok=True)
    fd, name = tempfile.mkstemp(prefix=".restore-", suffix=".db", dir=db.parent)
    os.close(fd)
    temp, g = Path(name), None
    try:
        g = askdb._graphqlite()(str(temp))
        conn = g.connection.sqlite_connection
        for table, columns in FTS.items():
            tokenizer = f", tokenize='{askdb.TOKENIZER}'" if table in ("lines", "quotes") else ""
            conn.execute(f"CREATE VIRTUAL TABLE {table} USING fts5({columns}{tokenizer})")
        conn.execute("CREATE TABLE kp_evidence(id TEXT PRIMARY KEY, payload TEXT NOT NULL)")
        ids, keys, counts, digest = {}, {}, {}, hashlib.sha256()

        def properties(kind, row, values):
            for key, (typ, value) in values.items():
                if typ not in TYPES:
                    raise ValueError("unsupported property type")
                if key not in keys:
                    conn.execute("INSERT INTO property_keys(key) VALUES (?)", (key,))
                    keys[key] = conn.execute("SELECT last_insert_rowid()").fetchone()[0]
                conn.execute(f"INSERT INTO {kind}_props_{typ} VALUES (?,?,?)", (row, keys[key], value))

        with gzip.open(archive, "rb") as source:
            header = json.loads(next(source))
            if (header.get("record"), header.get("format"), header.get("version"), header.get("dependency")) != ("header", FORMAT, askdb.SCHEMA_VERSION, askdb.DEPENDENCY):
                raise ValueError("invalid snapshot header")
            if header["meta"]["inputs"] != hashes:
                raise ValueError("snapshot header inputs mismatch")
            for raw in source:
                digest.update(raw)
                record = json.loads(raw)
                kind = record["record"]
                counts[kind] = counts.get(kind, 0) + 1
                if kind == "node":
                    key = record["id"]
                    if key in ids or record["props"].get("id") != ["text", key] or not record["labels"]:
                        raise ValueError("invalid or duplicate external node ID")
                    node = counts[kind]
                    conn.execute("INSERT INTO nodes(id) VALUES (?)", (node,))
                    ids[key] = node
                    for label in record["labels"]:
                        conn.execute("INSERT INTO node_labels VALUES (?,?)", (node, label))
                    properties("node", node, record["props"])
                elif kind == "edge":
                    if record["source"] not in ids or record["target"] not in ids:
                        raise ValueError("dangling snapshot edge")
                    edge = counts[kind]
                    conn.execute("INSERT INTO edges(id,source_id,target_id,type) VALUES (?,?,?,?)",
                                 (edge, ids[record["source"]], ids[record["target"]], record["type"]))
                    properties("edge", edge, record["props"])
                elif kind in TABLES:
                    row = record["row"]
                    if len(row) != TABLES[kind]:
                        raise ValueError("invalid snapshot table row")
                    conn.execute(f"INSERT INTO {kind} VALUES ({','.join('?' * len(row))})", row)
                else:
                    raise ValueError("unknown snapshot record")
        if digest.hexdigest() != manifest["logical_sha256"] or counts != manifest["counts"]:
            raise ValueError("snapshot logical checksum or counts mismatch")
        n_lines = 0
        for source in askdb.manifest():
            path = askdb.ROOT / source["export_path"]
            rows = [(source["slug"], i, text) for i, text in enumerate(path.read_text(encoding="utf-8").split("\n"), 1) if text.strip()]
            conn.executemany("INSERT INTO lines VALUES (?,?,?)", rows)
            n_lines += len(rows)
        if n_lines != header["stats"]["lines"]:
            raise ValueError("source line count differs from exported store")
        # Re-export logical rows: the importer must preserve types, labels and order.
        rebuilt = hashlib.sha256()
        for record in records(conn):
            rebuilt.update((askdb.compact(record) + "\n").encode())
        if rebuilt.hexdigest() != manifest["logical_sha256"]:
            raise ValueError("restored graph does not match exported logical records")
        stats = header["stats"]
        stats["storage_hash"] = askdb.storage_hash(conn)
        conn.execute("CREATE TABLE kp_meta(payload TEXT NOT NULL)")
        conn.execute("INSERT INTO kp_meta VALUES (?)", (askdb.compact(header["meta"]),))
        conn.execute("CREATE TABLE meta(key TEXT PRIMARY KEY,value TEXT)")
        conn.execute("INSERT INTO meta VALUES ('stats',?)", (askdb.compact(stats),))
        conn.commit()
        g.close()
        g = None
        if askdb.inputs() != hashes:
            raise ValueError("inputs changed during restoration")
        os.replace(temp, db)
        return {"status": "restored", "sha256": manifest["sha256"], **stats}
    finally:
        if g is not None:
            g.close()
        temp.unlink(missing_ok=True)


def markdown(db, directory, manifest):
    """Small navigation view of the semantic core, never one page per source line."""
    import kg
    core = kg.read_graph(db)
    def escape(value):
        return str(value).replace("|", "\\|").replace("\n", " ")
    parts = ["# Graph navigation", "", "Generated from the complete snapshot; edit Wiki/Sources, not this view.",
             "", f"Snapshot: `{manifest['sha256']}`.", "", "| Node | Type | Authoritative page | Outgoing core relationships |",
             "|---|---|---|---|"]
    for key, node in core["nodes"].items():
        path = node.get("path")
        link = f"[read](../{path})" if path else (f"[source](../Sources/drive/{node['slug']}.md)" if node["type"] == "doc" else "")
        neighbors = [f"{e['type']} → `{e['target']}`" for e in core["edges"] if e["source"] == key]
        summary = "; ".join(neighbors[:8])
        if len(neighbors) > 8:
            summary += f"; {len(neighbors) - 8} more (query the database)"
        parts.append(f"| `{escape(key)}` | {escape(node['type'])} | {link} | {escape(summary)} |")
    (directory / "index.md").write_text("\n".join(parts) + "\n", encoding="utf-8")
