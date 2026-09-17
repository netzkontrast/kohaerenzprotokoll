"""Fold each group of near-identical exports down to one file.

Drive holds up to five exports of the same document -- a gdoc export, a docx
export, a `kopie` of each, and a second run of both -- and `sources.py` landed
every one, because each is its own `drive_id`. 409 files were 346 documents.

This folds the 63 extra files away: the file leaves `Sources/drive/` and the
manifest row leaves `Sources/manifest.jsonl`, which drops from 680 rows to 617.

**Each removed row moves to `Sources/duplicates.jsonl` in full** -- `drive_id`,
`title`, `sha256`, `export_path`, `category`, `tier`, `index_date` -- plus the
slug it was folded into. Two files, two questions: the manifest says what is in
the corpus, and `duplicates.jsonl` says what Drive also holds and why it is not
here. `sources.py next` filters against it by `drive_id`, so a folded document is
never offered for fetching again, including after a manifest rebuild.

`Plan/runs/dedupe.json` keeps the reasoning -- which slug won each group, on how
many URLs, against what.

## Which copy survives, and why it is not the longest

The obvious rule -- keep the longest -- is wrong, and the diff says so. In 19 of
31 groups every member has an identical word count, so length decides nothing.
Where it does differ, it points both ways, and the reason is that the two export
routes lose different things:

    gdoc export:  keeps the footnote's anchor text, drops the URL behind it,
                  and adds an "end list" marker per list -- 195 of them in
                  `aegis-subplots-kapitelweise-system-exploration`
    docx export:  keeps the URL

So the gdoc export is *longer* while carrying *less*: its extra words are export
artifacts and its missing words are the source links. Measured across the 11
groups holding both formats, **the docx export carries at least as many URLs in
11 of 11, and strictly more in 10.** For a project whose next step is checking
that citations resolve, a lost URL is the expensive loss and a lost "end list"
is none.

Hence, in order:

1. the most source URLs -- the only signal that tracks content
2. the fewest "end list" artifacts
3. no copy marker in the slug (`kopie`, `-2`, `-3`, a leading `2-`)
4. the slug that best matches the slug its own title would produce today --
   see `title_match`, which is where the `ä`/`ae` split gets decided
5. the earliest `index_date`, then the shortest slug, then alphabetical

Rules 3 to 5 only ever run inside a group whose members are already
byte-comparable in content, so they choose a *name*, not a document.

Usage:
    python3 scripts/dedupe.py              # show the decision, change nothing
    python3 scripts/dedupe.py --apply      # delete the files, drop the rows
"""

from __future__ import annotations

import argparse
import json
import re
import sys
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from subject import documents  # noqa: E402
from duplicates import groups  # noqa: E402

MANIFEST = ROOT / "Sources" / "manifest.jsonl"
DUPLICATES = ROOT / "Sources" / "duplicates.jsonl"
DECISION = ROOT / "Plan" / "runs" / "dedupe.json"
URL = re.compile(r"https?://|https?\s")
ENDLIST = re.compile(r"\bend list\b", re.I)
COPY_MARKER = re.compile(r"kopie|-\d$|^\d+-")
UMLAUT = {"ä": "ae", "ö": "oe", "ü": "ue", "ß": "ss"}


def slug_of_title(title: str) -> str:
    """The slug this title would produce today, umlauts expanded."""
    text = unicodedata.normalize("NFC", title).lower()
    for umlaut, expansion in UMLAUT.items():
        text = text.replace(umlaut, expansion)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    return re.sub(r"-+", "-", re.sub(r"[^a-z0-9]+", "-", text)).strip("-")


def title_match(slug: str, title: str) -> int:
    """How far this slug agrees with the slug its own title would produce.

    The manifest holds two generations of the slug function -- the same document
    is both `aegis-singularitat-…` and `aegis-singularitaet-…` -- so picking by
    slug length silently prefers the one that destroyed the letter. The cause is
    not a changed mapping but Unicode: those titles store `ä` decomposed, as
    `a` plus a combining diaeresis, so a replace of the precomposed character
    missed it and the ASCII fold then dropped the accent. Normalising to NFC
    first separates them cleanly -- the mangled slugs agree with their title for
    12 and 17 characters, the intact ones for 46 to 60.
    """
    expected = slug_of_title(title)
    matched = 0
    for a, b in zip(slug, expected):
        if a != b:
            break
        matched += 1
    return matched


def rank(doc, title: str) -> tuple:
    """Lower sorts first. See the module docstring for why URLs lead."""
    return (
        -len(URL.findall(doc.body)),
        len(ENDLIST.findall(doc.body)),
        bool(COPY_MARKER.search(doc.slug)),
        -title_match(doc.slug, title),
        doc.date,
        len(doc.slug),
        doc.slug,
    )


def titles() -> dict[str, str]:
    return {r["slug"]: r.get("title", "")
            for r in (json.loads(line) for line in
                      MANIFEST.read_text(encoding="utf-8").splitlines() if line.strip())}


def decide(threshold: float) -> list[dict]:
    by = {d.slug: d for d in documents()}
    title = titles()
    decided = []
    for group in groups(threshold):
        ordered = sorted((by[s] for s in group), key=lambda d: rank(d, title.get(d.slug, "")))
        keeper = ordered[0]
        decided.append({
            "keep": keeper.slug,
            "urls": len(URL.findall(keeper.body)),
            "fold": [{"slug": d.slug, "urls": len(URL.findall(d.body)),
                      "end_list": len(ENDLIST.findall(d.body)), "format": d.format}
                     for d in ordered[1:]],
        })
    return sorted(decided, key=lambda d: -len(d["fold"]))


def apply(decided: list[dict]) -> tuple[int, int]:
    folded = {f["slug"]: d["keep"] for d in decided for f in d["fold"]}
    rows = [json.loads(line) for line in MANIFEST.read_text(encoding="utf-8").splitlines()
            if line.strip()]

    kept, dropped, unlinked = [], [], 0
    for row in rows:
        keeper = folded.get(row.get("slug", ""))
        if not keeper:
            kept.append(row)
            continue
        path = ROOT / row["export_path"] if row.get("export_path") else None
        if path and path.exists():
            path.unlink()
            unlinked += 1
        dropped.append(dict(row, duplicate_of=keeper))

    DECISION.parent.mkdir(parents=True, exist_ok=True)
    DECISION.write_text(json.dumps(decided, ensure_ascii=False, indent=2) + "\n",
                        encoding="utf-8")
    existing = ([json.loads(line) for line in
                 DUPLICATES.read_text(encoding="utf-8").splitlines() if line.strip()]
                if DUPLICATES.exists() else [])
    known = {r.get("drive_id") for r in existing}
    DUPLICATES.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n"
                                  for r in existing + [d for d in dropped
                                                       if d.get("drive_id") not in known]),
                          encoding="utf-8")
    MANIFEST.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in kept),
                        encoding="utf-8")
    return len(dropped), unlinked


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--threshold", type=float, default=0.8)
    parser.add_argument("--apply", action="store_true", help="actually delete and mark")
    args = parser.parse_args()

    decided = decide(args.threshold)
    total = sum(len(d["fold"]) for d in decided)
    for entry in decided:
        print(f"  keep  {entry['keep']}  ({entry['urls']} urls)")
        for f in entry["fold"]:
            print(f"    fold  {f['slug']}  ({f['urls']} urls, {f['end_list']} end-list)")
    print(f"\n{len(decided)} groups, {total} files folded away")

    if not args.apply:
        print("nothing changed — pass --apply")
        return 0
    marked, removed = apply(decided)
    print(f"moved {marked} rows to {DUPLICATES.relative_to(ROOT)} and removed {removed} "
          f"files; {len(open(MANIFEST, encoding='utf-8').readlines())} rows remain")
    print(f"decision recorded in {DECISION.relative_to(ROOT)}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
