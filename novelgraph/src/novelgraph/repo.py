"""Thin imports of repository helpers; no copied manifest or folding logic."""
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
import subject
from wiki_index import fold

read_jsonl = subject.read_jsonl
write_jsonl = subject.write_jsonl
split_body = subject._split


def sources(root=ROOT):
    rows = subject.rows() if root == ROOT else read_jsonl(root / "Sources/manifest.jsonl")
    if len({r["slug"] for r in rows}) != len(rows):
        raise ValueError("duplicate source slug in manifest")
    for r in rows:
        slug = r["slug"]
        if not slug or Path(slug).name != slug or slug in (".", ".."):
            raise ValueError(f"unsafe slug: {slug}")
        if r.get("export_path"):
            p = (root / r["export_path"]).resolve()
            if not p.is_relative_to((root / "Sources").resolve()) or not p.is_file():
                raise ValueError(f"source absent or outside Sources: {r['export_path']}")
    return rows
