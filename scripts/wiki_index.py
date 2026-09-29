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
    python3 scripts/wiki_index.py --check    # report what the index cannot see, and
                                             # every page whose sources/readings/ingested
                                             # differ from the body (non-zero if any)
    python3 scripts/wiki_index.py --fix-frontmatter   # rewrite exactly those three fields
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


# --- Frontmatter counts, derived (decision 015, pipeline plan step 3c) ---------
#
# `ingested:` is every READ document the page cites -- a citation in a difference
# line counts, not only one in a `## Reading` section. `sources:` is its length and
# `readings:` the number of `## Reading` headings. A document with no census in
# Sources/terms/ is scanned, not read, and is never ingested.

CITE = re.compile(r"\^\[([^\]\n]*)\]")
QUALIFIED = re.compile(r"([A-Za-z0-9][\w-]*)\.md:L\d+")
BARE = re.compile(r"(?:^|[;,]\s*)L\d+")
READING = re.compile(r"^## Readings?\b", re.MULTILINE)
DERIVED_FIELDS = ("sources", "readings", "ingested")


def read_documents(terms_dir=None) -> set[str]:
    """Slugs of the documents that have a census: the read ones."""
    terms_dir = terms_dir or ROOT / "Sources" / "terms"
    return {p.stem for p in terms_dir.glob("*.md")}


def derive_frontmatter(text: str, read: set[str]) -> dict:
    """What `ingested`, `sources` and `readings` follow from in the body.

    `keep_readings` is True for a page with no `## Reading` heading: its readings
    are in an older format and the stored value is kept.
    """
    meta = frontmatter(text)
    body = text.split("---", 2)[2] if text.startswith("---") else text
    cited: list[str] = []
    bare = False
    for m in CITE.finditer(body):
        inner = m.group(1)
        found = QUALIFIED.findall(inner)
        for slug in found:
            if slug not in cited:
                cited.append(slug)
        if not found and BARE.search(inner):
            bare = True
    existing = [s for s in meta.get("ingested", []) if s in read]
    kept = [s for s in existing if s in cited or bare]
    ingested = kept + [s for s in cited if s in read and s not in kept]
    headings = len(READING.findall(body))
    return {"ingested": ingested, "sources": len(ingested),
            "readings": headings, "keep_readings": headings == 0}


def frontmatter_drift(pages_dir=None, terms_dir=None) -> tuple[list[dict], list[str]]:
    """Pages whose three fields differ from the derivation, and pages kept as-is
    because their readings are in the older format (no `## Reading` heading)."""
    pages_dir = pages_dir or PAGES
    read = read_documents(terms_dir)
    drifts, older = [], []
    for path in sorted(pages_dir.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        meta = frontmatter(text)
        want = derive_frontmatter(text, read)
        if want["keep_readings"]:
            older.append(path.stem)
            want["readings"] = int(meta.get("readings", 0) or 0)
        have = {"ingested": meta.get("ingested", []),
                "sources": int(meta.get("sources", 0) or 0),
                "readings": int(meta.get("readings", 0) or 0)}
        changes = {}
        for f in DERIVED_FIELDS:
            if have[f] != want[f]:
                changes[f] = (have[f], want[f])
        if changes:
            drifts.append({"page": path.stem, "path": path, "changes": changes, "want": want})
    return drifts, older


def _describe(field: str, have, want) -> str:
    if field != "ingested":
        return f"{field} {have} -> {want}"
    added = [s for s in want if s not in have]
    removed = [s for s in have if s not in want]
    return "ingested " + ", ".join(
        [f"+{s}" for s in added] + [f"-{s}" for s in removed]
        + (["(order)"] if not added and not removed else []))


def rewrite_frontmatter(text: str, want: dict) -> str:
    """Replace exactly the three fields in the frontmatter block; nothing else."""
    _, block, rest = text.split("---", 2)
    lines = block.split("\n")
    values = {"sources": str(want["sources"]), "readings": str(want["readings"]),
              "ingested": "[" + ", ".join(f'"{s}"' for s in want["ingested"]) + "]"}
    done = set()
    for i, line in enumerate(lines):
        key = line.split(":", 1)[0]
        if key in values and ":" in line:
            lines[i] = f"{key}: {values[key]}"
            done.add(key)
    for key in DERIVED_FIELDS:
        if key not in done:
            at = max([i for i, l in enumerate(lines) if l.split(":", 1)[0] in DERIVED_FIELDS]
                     or [max(len(lines) - 2, 0)]) + 1
            lines.insert(at, f"{key}: {values[key]}")
    return "---" + "\n".join(lines) + "---" + rest


def fix_frontmatter(pages_dir=None, terms_dir=None) -> list[str]:
    report = []
    drifts, _ = frontmatter_drift(pages_dir, terms_dir)
    for d in drifts:
        text = d["path"].read_text(encoding="utf-8")
        d["path"].write_text(rewrite_frontmatter(text, d["want"]), encoding="utf-8")
        report.append(f"{d['page']}: " + "; ".join(
            _describe(f, h, w) for f, (h, w) in d["changes"].items()))
    return report


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
    drifts, older = frontmatter_drift()
    print(f"\n{len(drifts)} pages whose sources/readings/ingested differ from the body:\n")
    for d in drifts:
        print(f"  {d['page']}: " + "; ".join(
            _describe(f, h, w) for f, (h, w) in d["changes"].items()))
    print(f"\n{len(older)} pages have no `## Reading` heading; their readings value is kept: "
          + (", ".join(older) or "none"))
    return 1 if drifts else 0


def main(argv: list[str]) -> int:
    if "--fix-frontmatter" in argv:
        changed = fix_frontmatter()
        for line in changed:
            print(line)
        print(f"{len(changed)} pages rewritten (sources, readings, ingested only)")
        return 0
    index = build()
    if "--check" in argv:
        return check(index)
    INDEX.write_text(json.dumps(index, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
    print(f"wrote {INDEX.relative_to(ROOT)} -- {index['pages']} pages, "
          f"{len(index['surface_to_page'])} surfaces, {index['conflicts']} conflicts")
    return 0


if __name__ == "__main__":
    subject.cli(main)
