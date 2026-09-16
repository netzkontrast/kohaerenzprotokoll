#!/usr/bin/env python3
"""Manage the source corpus: what is fetched, what is missing, and landing new documents.

    scripts/sources.py status                      what exists, by category and tier
    scripts/sources.py check                       compare the manifest against the disk
    scripts/sources.py next --limit 10             the next drive_ids to fetch
    scripts/sources.py land --drive-id <id>        land the newest spilled Drive result
    scripts/sources.py land --drive-id <id> --spill <path>

WHY THIS TOOL EXISTS

Fetching 680 Drive documents through a model's context would cost millions of
tokens to move bytes from one disk to another. It is also pointless: nothing in
the fetch requires understanding.

The Drive connector already helps. A large `read_file_content` result does not
come back inline — it is written to a file under the session's `tool-results/`
directory and the caller is handed the path. So the document body never enters
any model's context, and everything after that point is mechanical: parse,
normalize, write, record, verify. That is this tool's whole job.

The division is therefore:

    agent   one Drive call per document — sees a path, never the content
    tool    everything else

NORMALIZATION, AND WHY IT HAPPENS ON WRITE

The Drive text representation is systematically noisy in ways that are identical
across every document: trailing whitespace on most lines, no final newline,
occasional CRLF. Citations into these files are line ranges, so the file on disk
has to be stable and predictable or every citation is fragile.

Normalizing here means one encoding of the rule, in one place, before anything
cites the file. Normalizing later would change every checksum already recorded.

What is normalized is deliberately only what is mechanical:

    - CRLF and CR become LF
    - trailing whitespace is stripped from every line
    - the file ends with exactly one newline

What is deliberately NOT touched, because it is interpretation rather than
cleanup, and interpretation belongs to a human or to a later reading step:

    - backslash over-escaping (`\\[1\\]`), which the converter emits in bulk
    - bold-as-heading (`**Teil I: ...**`), which most documents use instead of
      real markdown headings
    - very long lines, such as a bibliography collapsed onto one line

Both checksums are recorded: `sha256_raw` proves what Drive returned, and
`sha256` is the file as it sits on disk.
"""
from __future__ import annotations

import argparse
import collections
import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
MANIFEST = ROOT / "Sources" / "manifest.jsonl"
DRIVE_DIR = ROOT / "Sources" / "drive"
SPILL_GLOB = "mcp-Google_Drive-read_file_content-*.txt"
SPILL_ROOT = Path("/root/.claude/projects")


# --------------------------------------------------------------------------- manifest

def load_manifest() -> list[dict]:
    """Every manifest row, in file order."""
    rows = []
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if line:
            rows.append(json.loads(line))
    return rows


def save_manifest(rows: list[dict]) -> None:
    """Rewrite the manifest, one compact JSON object per line."""
    body = "\n".join(json.dumps(r, ensure_ascii=False) for r in rows)
    MANIFEST.write_text(body + "\n", encoding="utf-8")


def find_row(rows: list[dict], drive_id: str) -> dict:
    for row in rows:
        if row.get("drive_id") == drive_id:
            return row
    raise SystemExit(f"drive_id {drive_id!r} is not in the manifest")


def is_landed(row: dict) -> bool:
    """A row counts as landed only when its file is actually on disk."""
    path = row.get("export_path")
    return bool(path) and (ROOT / path).exists()


# --------------------------------------------------------------------------- normalize

def normalize(text: str) -> str:
    """Mechanical cleanup only — see the module docstring for what is left alone."""
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    text = "\n".join(line.rstrip() for line in text.split("\n"))
    return text.rstrip("\n") + "\n"


def sha256(data: str | bytes) -> str:
    raw = data.encode("utf-8") if isinstance(data, str) else data
    return hashlib.sha256(raw).hexdigest()


def frontmatter(row: dict, today: str) -> str:
    """The provenance block every landed document carries, drawn from the manifest."""
    def quote(value: str) -> str:
        return json.dumps(str(value), ensure_ascii=False)

    fields = {
        "drive_id": row.get("drive_id", ""),
        "title": row.get("title", ""),
        "slug": row.get("slug", ""),
        "category": row.get("category", ""),
        "tier": row.get("tier", ""),
        "index_date": row.get("index_date", ""),
        "fetched": today,
    }
    lines = [f"{k}: {quote(v)}" for k, v in fields.items()]
    return "---\n" + "\n".join(lines) + "\n---\n\n"


# --------------------------------------------------------------------------- spill

def newest_spill() -> Path:
    """The most recently written Drive spill file across all sessions."""
    candidates = sorted(SPILL_ROOT.glob(f"*/*/tool-results/{SPILL_GLOB}"),
                        key=lambda p: p.stat().st_mtime, reverse=True)
    if not candidates:
        raise SystemExit(
            f"no Drive spill file found under {SPILL_ROOT}\n"
            "  the agent must call mcp__Google_Drive__read_file_content first")
    return candidates[0]


def read_spill(path: Path) -> str:
    """Pull the document body out of a spilled tool result."""
    payload = json.loads(path.read_text(encoding="utf-8"))
    content = payload.get("fileContent")
    if not content:
        raise SystemExit(f"{path} carries no fileContent")
    return content


# --------------------------------------------------------------------------- commands

def cmd_status(args: argparse.Namespace) -> int:
    rows = load_manifest()
    landed = [r for r in rows if is_landed(r)]
    by_cat: dict[str, list[int]] = collections.defaultdict(lambda: [0, 0])
    by_tier: dict[str, list[int]] = collections.defaultdict(lambda: [0, 0])
    for row in rows:
        hit = 1 if is_landed(row) else 0
        for table, key in ((by_cat, row.get("category", "-")), (by_tier, row.get("tier", "-"))):
            table[key][0] += hit
            table[key][1] += 1

    print(f"\nsources: {len(landed)} of {len(rows)} landed "
          f"({len(landed) / len(rows):.1%})\n")
    print(f"  {'category':24s} {'landed':>7s} {'total':>7s}")
    print("  " + "-" * 40)
    for cat, (hit, total) in sorted(by_cat.items(), key=lambda kv: -kv[1][1]):
        mark = " " if hit else "!"
        print(f"{mark} {cat:24s} {hit:7d} {total:7d}")
    print("  " + "-" * 40)
    for tier, (hit, total) in sorted(by_tier.items()):
        print(f"  {tier:24s} {hit:7d} {total:7d}")
    print("\n'!' marks a category with nothing landed yet.")
    return 0


def cmd_check(args: argparse.Namespace) -> int:
    """Compare the manifest against the disk. The check whose absence hid 26-of-680."""
    rows = load_manifest()
    missing_file, no_path, bad_hash, orphans = [], [], [], []

    for row in rows:
        path = row.get("export_path")
        if not path:
            no_path.append(row)
            continue
        full = ROOT / path
        if not full.exists():
            missing_file.append(row)
            continue
        recorded = row.get("sha256")
        if recorded and sha256(full.read_bytes()) != recorded:
            bad_hash.append(row)

    known = {row.get("export_path") for row in rows if row.get("export_path")}
    for found in sorted(DRIVE_DIR.glob("*.md")):
        if str(found.relative_to(ROOT)) not in known:
            orphans.append(found)

    print(f"\nmanifest rows        : {len(rows)}")
    print(f"  landed and verified: {len(rows) - len(no_path) - len(missing_file) - len(bad_hash)}")
    print(f"  never fetched      : {len(no_path)}")
    print(f"  path set, file gone: {len(missing_file)}")
    print(f"  checksum mismatch  : {len(bad_hash)}")
    print(f"files not in manifest: {len(orphans)}")

    for row in missing_file[:10]:
        print(f"  ! missing file: {row['export_path']}")
    for row in bad_hash[:10]:
        print(f"  ! checksum:     {row['export_path']}")
    for path in orphans[:10]:
        print(f"  ! orphan file:  {path.relative_to(ROOT)}")

    broken = bool(missing_file or bad_hash or orphans)
    print("\n" + ("FAIL — see the lines above" if broken
                  else f"ok — every landed row matches its file ({len(no_path)} still to fetch)"))
    return 1 if broken else 0


def cmd_next(args: argparse.Namespace) -> int:
    """Print the next documents to fetch, so the agent never loads the manifest."""
    rows = [r for r in load_manifest() if not is_landed(r)]
    if args.category:
        rows = [r for r in rows if r.get("category") == args.category]
    if args.tier:
        rows = [r for r in rows if r.get("tier") == args.tier]
    rows = [r for r in rows if r.get("tier") != "T0-duplicate"]

    if not rows:
        print("nothing left to fetch for that selection")
        return 0
    for row in rows[:args.limit]:
        print(f"{row['drive_id']}\t{row.get('category','-')}\t{row.get('title','')[:60]}")
    remaining = len(rows) - min(args.limit, len(rows))
    print(f"\n# {min(args.limit, len(rows))} shown, {remaining} more match", file=sys.stderr)
    return 0


def cmd_land(args: argparse.Namespace) -> int:
    """Take a spilled Drive result and land it as a source document."""
    rows = load_manifest()
    row = find_row(rows, args.drive_id)

    spill = Path(args.spill) if args.spill else newest_spill()
    raw = read_spill(spill)
    body = normalize(raw)

    slug = row.get("slug") or re.sub(r"[^a-z0-9]+", "-", row.get("title", "").lower()).strip("-")
    target = DRIVE_DIR / f"{slug}.md"
    if target.exists() and not args.force:
        raise SystemExit(f"{target.relative_to(ROOT)} exists — pass --force to overwrite")

    today = args.today or date.today().isoformat()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(frontmatter(row, today) + body, encoding="utf-8")

    row["export_path"] = str(target.relative_to(ROOT))
    row["sha256"] = sha256(target.read_bytes())
    row["sha256_raw"] = sha256(raw)
    row["exported_at"] = today
    save_manifest(rows)

    words = len(body.split())
    print(f"landed {target.relative_to(ROOT)}  "
          f"{target.stat().st_size:,} bytes · {words:,} words · sha {row['sha256'][:12]}")
    if args.consume:
        spill.unlink()
        print(f"  removed spill {spill.name}")
    return 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("status", help="what exists, by category and tier").set_defaults(fn=cmd_status)
    sub.add_parser("check", help="compare the manifest against the disk").set_defaults(fn=cmd_check)

    nxt = sub.add_parser("next", help="the next drive_ids to fetch")
    nxt.add_argument("--limit", type=int, default=10)
    nxt.add_argument("--category")
    nxt.add_argument("--tier")
    nxt.set_defaults(fn=cmd_next)

    land = sub.add_parser("land", help="land the spilled Drive result for one document")
    land.add_argument("--drive-id", required=True)
    land.add_argument("--spill", help="defaults to the newest spill file")
    land.add_argument("--force", action="store_true", help="overwrite an existing file")
    land.add_argument("--consume", action="store_true", help="delete the spill after landing")
    land.add_argument("--today", help="override the fetch date (for reproducible runs)")
    land.set_defaults(fn=cmd_land)

    args = parser.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    sys.exit(main())
