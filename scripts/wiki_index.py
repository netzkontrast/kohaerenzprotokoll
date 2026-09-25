"""Build a queryable index of the wiki, so reconciling never has to read it.

Reconciling a new document against the wiki by *reading* the wiki costs context
proportional to the wiki, which is the one thing that grows without bound. At 32
pages that is affordable; at 400 it is the whole budget, and the wiki is the part
that must keep growing.

So the wiki becomes data: this script derives Wiki/index.json from page
frontmatter, and scripts/reconcile.py answers questions against it. **No page
body is ever loaded.** What reaches a reader -- or a model -- is the answer to a
lookup, a handful of rows, not the corpus of pages.

The index is derived and disposable. Pages are the source of truth; delete
index.json and re-run.

Usage:
    python3 scripts/wiki_index.py            # write Wiki/index.json
    python3 scripts/wiki_index.py --check    # report what the index cannot see
"""

from __future__ import annotations

import json
import re
import unicodedata
from datetime import date
from functools import lru_cache

import subject
from subject import CONFLICTS, PAGES, ROOT

INDEX = ROOT / "Wiki" / "index.json"

SCALAR = re.compile(r'^([a-z_]+):\s*"?([^"\n]*?)"?\s*$')
LIST = re.compile(r'^([a-z_]+):\s*\[(.*)\]\s*$')


def frontmatter(text: str) -> dict:
    """Parse the flat subset of YAML the pages actually use: scalars and lists."""
    if not text.startswith("---"):
        return {}
    block = text.split("---", 2)[1]
    out: dict = {}
    for line in block.strip().split("\n"):
        listed = LIST.match(line)
        if listed:
            items = [i.strip().strip('"') for i in listed.group(2).split(",") if i.strip()]
            out[listed.group(1)] = items
            continue
        scalar = SCALAR.match(line)
        if scalar:
            out[scalar.group(1)] = scalar.group(2)
    return out


ARTICLE = re.compile(r"^(der|die|das|den|dem|des)\s+", re.IGNORECASE)
CONFLICT_ID = re.compile(r"\bC\d+\b")


def conflict_ids(value) -> list[str]:
    """The conflict ids a `conflict:` field names — `C4, C6` is two, `none yet` none.

    One reading of the field for every script: `graph.py` learned it when a
    question's `C6, C9` kept one edge of three, and `check()` below still read the
    whole value as one id and reported five pages' `C4, C6` as a missing record.
    """
    return CONFLICT_ID.findall(str(value or ""))


def fold(surface: str) -> str:
    """A comparison key: article, case, diacritics and punctuation removed.

    **Folding is not stemming.** Kern-Welten and Kern-Welt do NOT fold together --
    the plural ending survives, and the pair reaches judgement through containment
    instead. That is the intended behaviour: a stemmer aggressive enough to merge
    a term with its inflections also merges Negentropie with Entropie, which are
    opposites.

    This docstring claimed the opposite until `scripts/judgements.py` replayed the
    recorded decision for that exact pair and disagreed with it.

    The leading definite article is stripped because a German article is never a
    term boundary. That rule came from judgement: it was decided three times in
    one document -- Die Konstrukt-Stadt, Die Resonanz-Landschaft, Die Grenzfeste
    -- before being written down here, and Plan/runs/judgements.jsonl holds the
    three records that produced it.

    **A colon survives.** Storyform notation writes `A:RS` for Storyform A's
    Relationship Story, and with the colon removed it folded to `ars`, the key of
    the ARS protocol's page — the first document that wrote it had the lookup file
    a throughline as a reading on a protocol (J87). No page surface contains a
    colon, so no earlier lookup moves.
    """
    plain = ARTICLE.sub("", surface.strip())
    plain = unicodedata.normalize("NFKD", plain.lower())
    plain = "".join(c for c in plain if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9:]+", "", plain)


@lru_cache(maxsize=None)
def mention(term: str) -> re.Pattern:
    """`term` standing alone as a word: no letter, digit or hyphen on either side.

    One pattern for every script that asks it. `relations.py` counts the
    mentions a page leaves unmarked and `link.py` marks exactly those, so the
    measured number and the edit can never mean two different things;
    `capture.py` counts a candidate standing alone with it.

    The lookbehind stands after the literal, not before it: the same spans
    match, because the literal is fixed-width, and the engine can search for
    the literal instead of trying the assertion at every position. `link.py`'s
    dry run went from 2.3 seconds to 0.2 with it.
    """
    literal = re.escape(term)
    return re.compile(rf"{literal}(?<![\w-]{literal})(?![\w-])")


def build() -> dict:
    terms: dict[str, dict] = {}
    surfaces: dict[str, str] = {}
    for path in sorted(PAGES.glob("*.md")):
        meta = frontmatter(path.read_text(encoding="utf-8"))
        slug = path.stem
        title = meta.get("term", slug)
        known = [title, slug] + meta.get("aliases", []) + meta.get("covers", [])
        terms[slug] = {
            "title": title,
            "surfaces": sorted({s for s in known if s}),
            "ingested": meta.get("ingested", []),
            "sources": int(meta.get("sources", 0) or 0),
            "readings": int(meta.get("readings", 0) or 0),
            "conflict": meta.get("conflict", ""),
        }
        for surface in terms[slug]["surfaces"]:
            surfaces.setdefault(fold(surface), slug)

    conflicts = {}
    for path in sorted(CONFLICTS.glob("*.md")):
        meta = frontmatter(path.read_text(encoding="utf-8"))
        if meta.get("id"):
            conflicts[meta["id"]] = {
                "subject": meta.get("subject", ""),
                "pages": meta.get("pages", []),
                "status": meta.get("status", ""),
            }

    return {
        "built": date.today().isoformat(),
        "by": "scripts/wiki_index.py",
        "pages": len(terms),
        "conflicts": len(conflicts),
        "terms": terms,
        "surface_to_page": surfaces,
        "conflict_records": conflicts,
    }


def check(index: dict) -> int:
    """Name what the index cannot see, rather than letting it look complete."""
    gaps = []
    for slug, term in index["terms"].items():
        if len(term["surfaces"]) <= 2:
            gaps.append(f"{slug}: no aliases -- a second name for it will not be recognised")
        if term["readings"] and not term["ingested"]:
            gaps.append(f"{slug}: has readings but names no source document")
    for cid, conflict in index["conflict_records"].items():
        for page in conflict["pages"]:
            if page not in index["terms"]:
                gaps.append(f"{cid}: points at {page!r}, which is not a page")
    for slug, term in index["terms"].items():
        for cid in conflict_ids(term["conflict"]):
            if cid not in index["conflict_records"]:
                gaps.append(f"{slug}: carries conflict {cid}, which has no record")
    print(f"{index['pages']} pages, {index['conflicts']} conflicts, "
          f"{len(index['surface_to_page'])} known surfaces")
    print(f"{len(gaps)} gaps the index cannot see past:\n")
    for gap in gaps:
        print(f"  {gap}")
    return 0


def main(argv: list[str]) -> int:
    index = build()
    if "--check" in argv:
        return check(index)
    INDEX.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {INDEX.relative_to(ROOT)} -- {index['pages']} pages, "
          f"{len(index['surface_to_page'])} surfaces, {index['conflicts']} conflicts")
    return 0


if __name__ == "__main__":
    subject.cli(main)
