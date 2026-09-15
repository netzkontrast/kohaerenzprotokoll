#!/usr/bin/env python3
"""Verify that an enrichment pass only INSERTED prose, never altered it.

Enrichment must preserve every paragraph of the previous draft verbatim and in
order; new material may only appear between existing paragraphs. This checks
that property against any git revision, so a chapter cannot be silently
rewritten under the guise of being expanded.

    python3 scripts/check_enrichment.py [--base REV] [chapter globs ...]

Exit status is non-zero if any chapter lost or reordered a paragraph.
"""
from __future__ import annotations

import argparse
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHAPTERS = "Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/chapters"
BODY = re.compile(r"^# Kapitel ", re.M)
# the draft-provenance comment is expected to change on every pass
DRAFT_COMMENT = re.compile(r"^<!--\s*(Draft|Revision|Anreicherung)\b.*-->$", re.S)


def paragraphs(text: str) -> list[str]:
    """Reader-facing paragraphs, whitespace-normalised.

    Scene-break rules and the draft-provenance comment are dropped: neither is
    prose, and letting a "---" glue two paragraphs together would make any
    insertion between them look like destroyed text.
    """
    m = BODY.search(text)
    if not m:
        return []
    out = []
    for para in text[m.start():].split("\n\n"):
        p = " ".join(para.split())
        if not p or p == "---" or DRAFT_COMMENT.match(p):
            continue
        out.append(p)
    return out


def sentences(paras: list[str]) -> list[str]:
    """Sentences, extracted within each paragraph and never across one.

    Sentences rather than paragraphs are the unit of preservation: splitting a
    paragraph to insert material between its sentences is legitimate
    enrichment, and must not read as destroyed prose. The lookbehind avoids
    breaking on decimal commas and ordinals.
    """
    out = []
    for para in paras:
        parts = re.split(r"(?<=[.!?\u2026])\s+(?=[A-ZÄÖÜ\u201e*\u2014>`])", para)
        out.extend(s for s in (p.strip() for p in parts) if len(s.split()) >= 3)
    return out


def git_show(rev: str, path: str) -> str | None:
    r = subprocess.run(["git", "-C", str(ROOT), "show", f"{rev}:{path}"],
                       capture_output=True, text=True)
    return r.stdout if r.returncode == 0 else None


def check(path: Path, base: str) -> tuple[bool, str]:
    rel = path.relative_to(ROOT).as_posix()
    old_text = git_show(base, rel)
    if old_text is None:
        return True, "new file, nothing to preserve"
    old_paras = paragraphs(old_text)
    new_paras = paragraphs(path.read_text(encoding="utf-8"))
    if not old_paras:
        return True, "no prose body at base"
    old_prose, new_prose = " ".join(old_paras), " ".join(new_paras)

    # every old sentence must still be present, in the same relative order
    old_sents = sentences(old_paras)
    missing, cursor = [], 0
    for sent in old_sents:
        idx = new_prose.find(sent, cursor)
        if idx == -1:
            missing.append(sent)
        else:
            cursor = idx + len(sent)
    ow, nw = len(old_prose.split()), len(new_prose.split())
    if missing:
        detail = "\n".join(f"      - {s[:88]}…" for s in missing[:6])
        more = f"\n      (+{len(missing) - 6} more)" if len(missing) > 6 else ""
        return False, (f"{len(missing)}/{len(old_sents)} sentence(s) altered, dropped or "
                       f"reordered:\n{detail}{more}")
    return True, f"all {len(old_sents)} sentences preserved · {ow} → {nw} words (+{nw - ow})"


def main() -> int:
    ap = argparse.ArgumentParser()
    ap.add_argument("--base", default="HEAD", help="revision to compare against")
    ap.add_argument("globs", nargs="*", default=["*.md"])
    a = ap.parse_args()

    files: list[Path] = []
    for g in a.globs:
        files.extend(sorted((ROOT / CHAPTERS).glob(g)))
    files = [f for f in files if f.name != "README.md"]
    if not files:
        print("no chapter files matched", file=sys.stderr)
        return 2

    failed = 0
    for f in files:
        ok, msg = check(f, a.base)
        print(f"  {'OK  ' if ok else 'FAIL'} {f.name[:44]:44} {msg}")
        failed += not ok
    print(f"\n{len(files) - failed}/{len(files)} chapters preserved their prose.")
    return 1 if failed else 0


if __name__ == "__main__":
    sys.exit(main())
