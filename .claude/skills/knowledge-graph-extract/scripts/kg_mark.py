#!/usr/bin/env python3
"""Atomically update one chunk's status/triplet count in <output_dir>/manifest.json.

This is the ONLY safe way to change progress: it re-reads the manifest, mutates a
single chunk, and writes the file back atomically (temp file + rename), so a crash
mid-write can never corrupt the resume anchor. The immutable chunk plan
(start_line/end_line, start_page/end_page, ids) is never touched.

Marking a chunk done|in_progress promotes a 'pending' document to 'in_progress';
when a document's last chunk becomes done, the document is marked done too.

Examples:
  python3 scripts/kg_mark.py OUT notes/curie.md 2 in_progress
  python3 scripts/kg_mark.py OUT notes/curie.md 2 done --triplets 14

Python 3 stdlib only. No network, no subprocess.
"""

import argparse
import json
import sys
from pathlib import Path

STATUSES = ("pending", "in_progress", "done")


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("output_dir", help="extraction output directory")
    parser.add_argument("doc", help="document path as recorded in the manifest (documents[].path)")
    parser.add_argument("chunk", type=int, help="chunk id to update")
    parser.add_argument("status", choices=STATUSES, help="new chunk status")
    parser.add_argument("--triplets", type=int, default=None,
                        help="set the chunk's triplet count (usually with 'done')")
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    manifest_path = out_dir / "manifest.json"
    if not manifest_path.exists():
        print(f"error: {manifest_path} not found — run Phase 2 first", file=sys.stderr)
        return 1
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    doc = next((d for d in manifest.get("documents", []) if d.get("path") == args.doc), None)
    if doc is None:
        print(f"error: document {args.doc!r} not in manifest", file=sys.stderr)
        return 1
    chunk = next((c for c in doc.get("chunks", []) if c.get("id") == args.chunk), None)
    if chunk is None:
        print(f"error: chunk {args.chunk} not in document {args.doc!r}", file=sys.stderr)
        return 1

    chunk["status"] = args.status
    if args.triplets is not None:
        chunk["triplets"] = args.triplets

    chunks = doc.get("chunks", [])
    if all(c.get("status") == "done" for c in chunks):
        doc["status"] = "done"
    elif doc.get("status") == "pending" and args.status in ("in_progress", "done"):
        doc["status"] = "in_progress"

    tmp_path = manifest_path.with_suffix(".json.tmp")
    tmp_path.write_text(json.dumps(manifest, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp_path.replace(manifest_path)

    done = sum(1 for c in chunks if c.get("status") == "done")
    print(f"{args.doc} chunk {args.chunk} -> {args.status}"
          + (f" ({args.triplets} triplets)" if args.triplets is not None else "")
          + f"; document {doc['status']} ({done}/{len(chunks)} chunks done)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
