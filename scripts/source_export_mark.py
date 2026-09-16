#!/usr/bin/env python3
"""Step 3+4 of the fetch procedure (Sources/README.md): write one export, mark the manifest.

    python3 scripts/source_export_mark.py --slug <slug> --from-json <tool-result.json>
    python3 scripts/source_export_mark.py --slug <slug> --from-text <body.md>
    python3 scripts/source_export_mark.py --slug <slug> --truncated      # re-mark an existing export
    python3 scripts/source_export_mark.py --slug <slug> --from-json <r.json> --tail-from <plain.txt>

The Drive MCP result is JSON — ``{"fileContent": ...}`` from ``read_file_content``
or ``{"content": <base64>, ...}`` from ``download_file_content``, saved to disk by
the harness for large documents (``--from-json``) — or a plain text file
(``--from-text``). The body is normalised to UTF-8, LF, stripped of
trailing whitespace and terminated by one newline, then written to
``Sources/drive/<slug>.md`` — no frontmatter, no header line. The manifest
record with that slug gets ``export_path``, ``sha256`` (of the file bytes),
``exported_at`` (today, UTC) and ``truncated``. Only the fields of one record
change; every other line of ``Sources/manifest.jsonl`` is rewritten byte for
byte. Exit 2 when the slug is unknown, 3 when the body looks incomplete and
``--truncated`` was not given (under 200 bytes, or it contains a Drive
truncation notice) — the caller then decides and re-runs with the flag.

The markdown read of a Google Doc can stop a few characters before the end
of its last line (the plain-text export of the same document is complete).
``--tail-from <plain.txt>`` completes exactly that: the last line of the
markdown body must be a prefix of a line in the plain text; the rest of that
line is appended, nothing else. Exit 4 when the tail cannot be verified.
"""
from __future__ import annotations

import argparse
import base64
import hashlib
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
MANIFEST = ROOT / "Sources" / "manifest.jsonl"
DRIVE_DIR = ROOT / "Sources" / "drive"
MIN_BODY_BYTES = 200
TRUNCATION_NOTICES = ("[content truncated", "content has been truncated", "…(continued)", "[truncated]")


def normalise(text: str) -> str:
    """CRLF → LF, trailing whitespace per line and at the end removed, one final newline."""
    lines = [line.rstrip() for line in text.replace("\r\n", "\n").replace("\r", "\n").split("\n")]
    return "\n".join(lines).rstrip() + "\n"


def load_body(args: argparse.Namespace) -> str:
    if args.from_json:
        data = json.loads(Path(args.from_json).read_text(encoding="utf-8"))
        if "fileContent" in data:
            return normalise(data["fileContent"])
        return normalise(base64.b64decode(data["content"]).decode("utf-8").lstrip("\ufeff"))
    return normalise(Path(args.from_text).read_text(encoding="utf-8"))


MARKDOWN_WRAPPERS = "<>\\*_`"


def bare(text: str) -> str:
    """Drop the characters the markdown renderer adds around plain text (link brackets, escapes, emphasis)."""
    return "".join(ch for ch in text if ch not in MARKDOWN_WRAPPERS).strip()


def complete_tail(body: str, plain_text: str) -> tuple[str, str]:
    """Append what the plain-text export has after the markdown body's last line.

    Returns ``(body, suffix)``; the suffix is empty when the last line is
    already complete. Raises ``ValueError`` when the bare last line is not a
    prefix of exactly one bare plain-text line (nothing is guessed). A last
    line cut inside a ``<url>`` gets its closing bracket back.
    """
    last = body.rstrip("\n").rsplit("\n", 1)[-1]
    needle = bare(last)
    if len(needle) < 20:
        raise ValueError("last line too short to verify against the plain text")
    matches = [bare(line) for line in plain_text.replace("\r\n", "\n").split("\n") if needle in bare(line)]
    if len(matches) != 1:
        raise ValueError(f"last line matches {len(matches)} plain-text lines, expected 1")
    match = matches[0]
    suffix = match[match.index(needle) + len(needle):]
    if not suffix:
        return body, ""
    if last.count("<") > last.count(">"):
        suffix += ">"
    return body.rstrip("\n") + suffix + "\n", suffix


def looks_truncated(body: str) -> str | None:
    """A reason when the body is obviously incomplete, else None."""
    if len(body.encode("utf-8")) < MIN_BODY_BYTES:
        return f"body is under {MIN_BODY_BYTES} bytes"
    lowered = body.lower()
    for notice in TRUNCATION_NOTICES:
        if notice in lowered:
            return f"body contains the notice {notice!r}"
    return None


def read_manifest() -> list[str]:
    return MANIFEST.read_text(encoding="utf-8").splitlines(keepends=True)


def mark(lines: list[str], slug: str, fields: dict) -> tuple[list[str], dict]:
    """Rewrite only the record whose slug matches; return the new lines and the record."""
    for index, line in enumerate(lines):
        record = json.loads(line)
        if record.get("slug") != slug:
            continue
        record.update(fields)
        lines[index] = json.dumps(record, ensure_ascii=False) + "\n"
        return lines, record
    raise KeyError(slug)


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    ap.add_argument("--slug", required=True)
    source = ap.add_mutually_exclusive_group()
    source.add_argument("--from-json", help="saved read_file_content result ({fileContent: ...})")
    source.add_argument("--from-text", help="plain text/markdown body")
    ap.add_argument("--truncated", action="store_true", help="record the export as incomplete")
    ap.add_argument("--tail-from", help="plain-text export used to complete a cut last line")
    ap.add_argument("--date", default=datetime.now(timezone.utc).strftime("%Y-%m-%d"),
                    help="exported_at (default: today, UTC)")
    ns = ap.parse_args(argv)

    target = DRIVE_DIR / f"{ns.slug}.md"
    if ns.from_json or ns.from_text:
        body = load_body(ns)
        if ns.tail_from:
            try:
                body, suffix = complete_tail(body, Path(ns.tail_from).read_text(encoding="utf-8"))
            except ValueError as exc:
                print(f"cannot complete the tail of {ns.slug}: {exc}", file=sys.stderr)
                return 4
            print(f"{ns.slug}: last line completed with {suffix!r}" if suffix else f"{ns.slug}: last line already complete")
        reason = looks_truncated(body)
        if reason and not ns.truncated:
            print(f"refusing to record {ns.slug} as complete: {reason}; re-run with --truncated "
                  "or fetch the rest", file=sys.stderr)
            return 3
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_bytes(body.encode("utf-8"))
    elif not target.exists():
        print(f"no export at {target.relative_to(ROOT)}; give --from-json or --from-text", file=sys.stderr)
        return 2

    digest = hashlib.sha256(target.read_bytes()).hexdigest()
    fields = {"export_path": target.relative_to(ROOT).as_posix(), "sha256": digest,
              "exported_at": ns.date, "truncated": bool(ns.truncated)}
    try:
        lines, record = mark(read_manifest(), ns.slug, fields)
    except KeyError:
        print(f"unknown slug {ns.slug!r} in {MANIFEST.relative_to(ROOT)}", file=sys.stderr)
        return 2
    MANIFEST.write_text("".join(lines), encoding="utf-8")
    text = target.read_text(encoding="utf-8")
    print(f"{ns.slug}: {len(text.encode('utf-8'))} bytes, {text.count(chr(10))} lines, "
          f"sha256={digest[:12]}…, truncated={record['truncated']}, tier={record['tier']}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
