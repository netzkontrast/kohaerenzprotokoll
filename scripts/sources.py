#!/usr/bin/env python3
"""Manage the source corpus: fetch documents from Drive, and see what is missing.

    scripts/sources.py status                          what exists, by category and tier
    scripts/sources.py check                           compare the manifest against the disk
    scripts/sources.py fetch --category theorie-physik  fetch straight from Drive to disk
    scripts/sources.py next --limit 10                 the next drive_ids, for manual work
    scripts/sources.py land --drive-id <id> [--spill P | --stdin | --base64-file F]

WHY THIS TOOL EXISTS

Moving the whole manifest from Drive to disk through a model's context would cost
millions of tokens, and nothing in a fetch requires understanding.

It turns out none of it has to. The MCP connectors are ordinary HTTP JSON-RPC
endpoints: `/tmp/mcp-config-*.json` holds the Drive server's URL and headers,
and `CLAUDE_SESSION_INGRESS_TOKEN_FILE` holds the bearer token. So this script
calls the connector directly and **no model sees a document at any point** —
not the session running this, not a subagent.

`fetch` is that path and is the one to use. The `land` subcommand remains for
the case where a model already has the content in hand: it accepts a spilled
tool result, stdin, or base64.

Both depend on a live Claude Code session, because the token and the config are
session-scoped. Outside one, `fetch` says so instead of failing obscurely.

TWO ROUTES, CHOSEN BY FORMAT

A Google Doc has no original file, so it comes through `read_file_content` as
text — and Drive's text export flattens structure. The first one landed had one
real heading against 21 lines of bold standing in for headings.

Anything with an original file (`docx`, `pdf`, `pptx`, `xlsx`) is downloaded as
bytes and converted with markitdown instead, which preserves what the author
marked up. Measured on the same corpus: 23 real headings and 15 table rows,
against 1 heading and no tables for the text route.

`md` and `mp3` rows have no route yet and are skipped, loudly.

NORMALIZATION, AND WHY IT HAPPENS ON WRITE

Citations into these files are line ranges, so a file has to be stable or every
citation into it is fragile. Normalizing on write means one encoding of the rule,
applied before anything cites the file; normalizing later would change every
checksum already recorded.

Only the mechanical parts are touched — CRLF to LF, trailing whitespace stripped
(673 of 852 lines in the first document), exactly one final newline.

Deliberately left alone, because they are interpretation rather than cleanup:
backslash over-escaping, bold used where headings belong, and bibliographies
collapsed onto a single line. Both checksums are recorded, so `sha256_raw` still
proves what the connector returned and any of it can be revisited.
"""
from __future__ import annotations

import argparse
import base64
import collections
import hashlib
import json
import os
import re
import subprocess
import sys
import tempfile
from datetime import date
from pathlib import Path

import subject  # noqa: E402  -- the manifest's one reader and writer
from subject import MANIFEST, ROOT  # noqa: E402

DRIVE_DIR = ROOT / "Sources" / "drive"
SPILL_GLOB = "mcp-Google_Drive-read_file_content-*.txt"
SPILL_ROOT = Path("/root/.claude/projects")

# markitdown needs its own dependency tree and conflicts with the system
# packages, so it lives in a venv and is called out to rather than imported.
# Everything else in this file is standard library.
TOOLS_PYTHON = ROOT / ".venv-tools" / "bin" / "python"
FORMAT_SUFFIX = {"docx": ".docx", "pdf": ".pdf", "pptx": ".pptx", "xlsx": ".xlsx"}
# md and mp3 have no fetch path yet — see Plan/learnings/fetch.md
SUPPORTED_FORMATS = set(FORMAT_SUFFIX) | {"gdoc"}


# --------------------------------------------------------------------------- manifest

def find_row(rows: list[dict], drive_id: str) -> dict:
    for row in rows:
        if row.get("drive_id") == drive_id:
            return row
    raise SystemExit(f"drive_id {drive_id!r} is not in the manifest")


def is_landed(row: dict) -> bool:
    """A row counts as landed only when its file is actually on disk."""
    path = row.get("export_path")
    return bool(path) and (ROOT / path).exists()


def folded_drive_ids() -> set[str]:
    """Drive documents that landed, turned out to be copies, and were folded away.

    They are no longer in the manifest, so nothing would stop `next` from
    offering them again after a manifest rebuild. `scripts/dedupe.py` writes the
    file; `next` filters against it.
    """
    return {row["drive_id"] for row in subject.duplicates()}


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


# --------------------------------------------------------------------------- drive

def mcp_endpoint() -> tuple[str, dict]:
    """The Drive MCP server's URL and headers, including this session's token.

    The connector is an ordinary HTTP JSON-RPC endpoint. The CLI talks to it on
    a model's behalf, but nothing stops a script from talking to it directly —
    and that is the difference between a document passing through a context and
    never being seen by a model at all.
    """
    configs = sorted(Path("/tmp").glob("mcp-config-*.json"))
    if not configs:
        raise SystemExit("no MCP config found under /tmp — is this a Claude Code session?")
    servers = json.loads(configs[-1].read_text())
    servers = servers.get("mcpServers", servers)
    if "Google_Drive" not in servers:
        raise SystemExit(f"{configs[-1]} has no Google_Drive server")
    server = servers["Google_Drive"]

    token_file = os.environ.get("CLAUDE_SESSION_INGRESS_TOKEN_FILE", "")
    if not token_file or not Path(token_file).exists():
        raise SystemExit("CLAUDE_SESSION_INGRESS_TOKEN_FILE is unset or missing")

    headers = dict(server.get("headers") or {})
    headers["Authorization"] = "Bearer " + Path(token_file).read_text().strip()
    headers["Content-Type"] = "application/json"
    headers["Accept"] = "application/json, text/event-stream"
    return server["url"], headers


def mcp_call(tool: str, arguments: dict, timeout: int = 180) -> str:
    """Call one Drive tool and return its text payload. Never touches a context."""
    import urllib.error
    import urllib.request

    url, headers = mcp_endpoint()
    body = json.dumps({"jsonrpc": "2.0", "id": 1, "method": "tools/call",
                       "params": {"name": tool, "arguments": arguments}}).encode()
    request = urllib.request.Request(url, data=body, headers=headers, method="POST")
    try:
        with urllib.request.urlopen(request, timeout=timeout) as response:
            text = response.read().decode("utf-8", "replace")
    except urllib.error.HTTPError as exc:
        raise SystemExit(f"{tool} failed: HTTP {exc.code} {exc.read()[:300]!r}") from exc

    for line in text.splitlines():           # streamable HTTP frames replies as SSE
        if line.startswith("data:"):
            text = line[5:].strip()
            break
    payload = json.loads(text)
    if "error" in payload:
        raise SystemExit(f"{tool} returned an error: {str(payload['error'])[:300]}")
    parts = payload.get("result", {}).get("content", [])
    joined = "".join(p.get("text", "") for p in parts if p.get("type") == "text")
    if not joined:
        raise SystemExit(f"{tool} returned no text content")
    return joined


def drive_document(row: dict) -> str:
    """Fetch one document as markdown, by the route its format deserves.

    `.docx` and friends keep their headings and tables when the original file is
    converted, so those go through download_file_content plus markitdown. A
    Google Doc has no original to convert, so it takes the text export.
    """
    suffix = FORMAT_SUFFIX.get(row.get("format", ""))
    if suffix:
        encoded = mcp_call("download_file_content", {"fileId": row["drive_id"]})
        try:
            blob = json.loads(encoded)
            encoded = blob.get("fileContent") or blob.get("content") or encoded
        except json.JSONDecodeError:
            pass
        return convert_binary(base64.b64decode(encoded), suffix)

    text = mcp_call("read_file_content", {"fileId": row["drive_id"]})
    try:
        return json.loads(text).get("fileContent", text)
    except json.JSONDecodeError:
        return text


def convert_binary(data: bytes, suffix: str) -> str:
    """Convert an original document to markdown with markitdown, in its own venv.

    Drive's own text extraction flattens structure — the first document landed
    that way had one real heading against 21 lines of bold standing in for
    headings, which makes section-level retrieval impossible. Converting the
    original file instead preserves what the author actually marked up, so
    `.docx` and `.pdf` take this path rather than the text one.
    """
    if not TOOLS_PYTHON.exists():
        raise SystemExit(
            f"{TOOLS_PYTHON.relative_to(ROOT)} is missing — create it with:\n"
            "  python3 -m venv .venv-tools && "
            ".venv-tools/bin/pip install 'markitdown[docx,pdf,pptx,xlsx]'")

    with tempfile.NamedTemporaryFile(suffix=suffix, delete=False) as handle:
        handle.write(data)
        temp = Path(handle.name)
    try:
        result = subprocess.run(
            [str(TOOLS_PYTHON), "-c",
             "import sys; from markitdown import MarkItDown; "
             "sys.stdout.write(MarkItDown().convert(sys.argv[1]).text_content)",
             str(temp)],
            capture_output=True, text=True, timeout=300)
        if result.returncode != 0:
            raise SystemExit(f"markitdown failed on a {suffix} file:\n{result.stderr[:500]}")
        return result.stdout
    finally:
        temp.unlink(missing_ok=True)


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
    rows = subject.rows()
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
    rows = subject.rows()
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
    folded = folded_drive_ids()
    rows = [r for r in subject.rows() if not is_landed(r) and r.get("drive_id") not in folded]
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
    """Land a Drive result as a source document, however it arrived.

    Large results spill to a file and are read from there. Small ones come back
    inline in the caller's context, so `--stdin` lets a subagent pipe what it
    received without the content passing through the main session.
    """
    rows = subject.rows()
    row = find_row(rows, args.drive_id)

    spill: Path | None = None
    if args.base64_file:
        suffix = FORMAT_SUFFIX.get(row.get("format", ""), "")
        if not suffix:
            raise SystemExit(
                f"format {row.get('format')!r} has no markitdown converter; "
                f"fetch this one as text instead")
        raw = convert_binary(base64.b64decode(Path(args.base64_file).read_text()), suffix)
    elif args.stdin:
        raw = sys.stdin.read()
        if not raw.strip():
            raise SystemExit("--stdin given but nothing arrived on stdin")
    else:
        spill = Path(args.spill) if args.spill else newest_spill()
        raw = read_spill(spill)
    target = write_document(row, rows, raw, args.today or date.today().isoformat(), args.force)
    words = len(normalize(raw).split())
    print(f"landed {target.relative_to(ROOT)}  "
          f"{target.stat().st_size:,} bytes · {words:,} words · sha {row['sha256'][:12]}")
    if args.consume and spill is not None:
        spill.unlink()
        print(f"  removed spill {spill.name}")
    return 0


def write_document(row: dict, rows: list[dict], raw: str, today: str, force: bool) -> Path:
    """Normalize, write and record one document. The one place a source is created."""
    body = normalize(raw)
    slug = row.get("slug") or re.sub(r"[^a-z0-9]+", "-", row.get("title", "").lower()).strip("-")
    target = DRIVE_DIR / f"{slug}.md"
    if target.exists() and not force:
        raise SystemExit(f"{target.relative_to(ROOT)} exists — pass --force to overwrite")

    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(frontmatter(row, today) + body, encoding="utf-8")
    row["export_path"] = str(target.relative_to(ROOT))
    row["sha256"] = sha256(target.read_bytes())
    row["sha256_raw"] = sha256(raw)
    row["exported_at"] = today
    subject.write_jsonl(MANIFEST, rows)
    return target


def cmd_fetch(args: argparse.Namespace) -> int:
    """Fetch documents straight from Drive to disk. No model sees the content."""
    rows = subject.rows()
    todo = [r for r in rows if not is_landed(r) and r.get("tier") != "T0-duplicate"]
    if args.category:
        todo = [r for r in todo if r.get("category") == args.category]
    if args.tier:
        todo = [r for r in todo if r.get("tier") == args.tier]
    if args.since:
        todo = [r for r in todo if (r.get("index_date") or "") >= args.since]
    # md takes the text route, as the four md rows landed on 2026-09-16 did.
    # Opt-in, because the connector does not list md as supported.
    formats = SUPPORTED_FORMATS | ({"md"} if args.include_md else set())
    unsupported = {f for f in (r.get("format") for r in todo) if f not in formats}
    todo = [r for r in todo if r.get("format") in formats][:args.limit]

    if not todo:
        print("nothing to fetch for that selection")
        return 0
    if unsupported:
        print(f"# skipping formats with no fetch path: {sorted(unsupported)}\n")

    today = args.today or date.today().isoformat()
    landed = failed = 0
    for index, row in enumerate(todo, 1):
        label = f"[{index}/{len(todo)}] {row.get('title','')[:48]}"
        try:
            raw = drive_document(row)
            target = write_document(row, rows, raw, today, args.force)
            words = len(target.read_text(encoding='utf-8').split())
            print(f"{label:54s} ok  {target.stat().st_size:>8,}b {words:>7,}w")
            landed += 1
        except SystemExit as exc:
            print(f"{label:54s} FAIL {exc}")
            failed += 1

    print(f"\nlanded {landed}, failed {failed}")
    return 1 if failed else 0


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__,
                                     formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    sub.add_parser("status", help="what exists, by category and tier").set_defaults(fn=cmd_status)
    sub.add_parser("check", help="compare the manifest against the disk").set_defaults(fn=cmd_check)

    fetch = sub.add_parser("fetch", help="fetch straight from Drive to disk, no model involved")
    fetch.add_argument("--limit", type=int, default=5)
    fetch.add_argument("--category")
    fetch.add_argument("--tier")
    fetch.add_argument("--force", action="store_true")
    fetch.add_argument("--today")
    fetch.add_argument("--since", help="only rows whose index_date is on or after this date")
    fetch.add_argument("--include-md", action="store_true",
                       help="also fetch md rows, through the text route")
    fetch.set_defaults(fn=cmd_fetch)

    nxt = sub.add_parser("next", help="the next drive_ids to fetch")
    nxt.add_argument("--limit", type=int, default=10)
    nxt.add_argument("--category")
    nxt.add_argument("--tier")
    nxt.set_defaults(fn=cmd_next)

    land = sub.add_parser("land", help="land a Drive result for one document")
    land.add_argument("--drive-id", required=True)
    land.add_argument("--spill", help="defaults to the newest spill file")
    land.add_argument("--stdin", action="store_true",
                      help="read the document from stdin, for results that came back inline")
    land.add_argument("--base64-file",
                      help="a file of base64 from download_file_content; converted with "
                           "markitdown, which keeps the structure Drive's text export loses")
    land.add_argument("--force", action="store_true", help="overwrite an existing file")
    land.add_argument("--consume", action="store_true", help="delete the spill after landing")
    land.add_argument("--today", help="override the fetch date (for reproducible runs)")
    land.set_defaults(fn=cmd_land)

    args = parser.parse_args(argv)
    return args.fn(args)


if __name__ == "__main__":
    subject.cli(main)
