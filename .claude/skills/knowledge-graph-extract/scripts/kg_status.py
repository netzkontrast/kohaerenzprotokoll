#!/usr/bin/env python3
"""Render extraction progress from <output_dir>/manifest.json.

Python 3 stdlib only. No network, no subprocess. Read-only.
"""

import argparse
import json
import sys
from pathlib import Path


def chunk_span(chunk):
    """Human-readable boundary, whether the chunk is line- or page-addressed."""
    if "start_page" in chunk or "end_page" in chunk:
        return f"pages {chunk.get('start_page')}-{chunk.get('end_page')}"
    return f"lines {chunk.get('start_line')}-{chunk.get('end_line')}"


def main():
    parser = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    parser.add_argument("output_dir", help="extraction output directory")
    args = parser.parse_args()

    out_dir = Path(args.output_dir)
    manifest_path = out_dir / "manifest.json"
    if not manifest_path.exists():
        print(f"no manifest at {manifest_path} — extraction not started")
        return 1
    manifest = json.loads(manifest_path.read_text(encoding="utf-8"))

    total_chunks = done_chunks = total_triplets = 0
    next_chunk = None
    print(f"docs_dir: {manifest.get('docs_dir')}")
    print(f"cap per doc: {manifest.get('max_triplets_per_doc')}, "
          f"schema: {manifest.get('schema_file') or 'none'}")
    print()
    for doc in manifest.get("documents", []):
        chunks = doc.get("chunks", [])
        done = [c for c in chunks if c.get("status") == "done"]
        triplets = sum(c.get("triplets", 0) for c in chunks)
        total_chunks += len(chunks)
        done_chunks += len(done)
        total_triplets += triplets
        marker = "done" if len(done) == len(chunks) else f"{len(done)}/{len(chunks)} chunks"
        print(f"  {doc['path']:<50} {marker:>16}  {triplets:>5} triplets")
        if next_chunk is None:
            for c in chunks:
                if c.get("status") != "done":
                    next_chunk = (doc["path"], c)
                    break

    print()
    print(f"total: {done_chunks}/{total_chunks} chunks done, {total_triplets} triplets extracted")
    if next_chunk:
        doc_path, chunk = next_chunk
        print(f"next: {doc_path} chunk {chunk['id']} "
              f"({chunk_span(chunk)}, status: {chunk.get('status')})")
    else:
        print("next: nothing — extraction complete")
    return 0


if __name__ == "__main__":
    sys.exit(main())
