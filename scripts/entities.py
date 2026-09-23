"""Search every landed document for the entities a per-document model read named.

`Plan/entities/<slug>.md` holds one list per source document, written by a model
reading that document alone: the 50-100 entities it judged most important, each
with the line it was found on. **Those lists are proposals, not a census.** A
census is exhaustive and written by a person (`Sources/terms/`), and the ingest
skill forbids a model list from becoming gold. What a list is good for is being
*searched* — which is this script — and every number it prints is a count over
the documents, never something a model said.

    python3 scripts/entities.py verify [<slug> ...]      # does each cited line hold its entity?
    python3 scripts/entities.py search <entity> [...]    # which documents, how often, first line
    python3 scripts/entities.py doc <slug> [--limit N]   # which known entities one document uses
    python3 scripts/entities.py matrix                   # every verified entity × every document
    python3 scripts/entities.py missing [--min-docs N]   # entities in N+ documents with no wiki page
    python3 scripts/entities.py score <slug>             # a model list against a reader's list

## Matching

Whole-word and case-sensitive, the same question `scripts/corpus.py` asks, but
over token sequences so that a multi-word entity (`Kern-Welt 1`, `Cognitive
Firewall`) is found across a line wrap. A document is split once into `\\w+` runs
and single punctuation marks; an entity matches where its own split appears
contiguously. That is exactly `\\b<entity>\\b` except that any run of whitespace,
including a newline, counts as one space. `selftest` compares the two on every
single-word entity rather than asserting it.

Counts are over the body only — the frontmatter boundary is `subject.py`'s — and
lines are **file** lines, the numbering a citation names.

**This is not `corpus.py count`, and the two numbers must not be compared as if
they were.** `corpus.py` answers from the derived surface index, where
`Guardian-Protokoll` is one token, so it counts `Guardian` standing alone: 334.
This counts every whole-word match, hyphen compounds included, as `\\bGuardian\\b`
does: 448. Both are right about different questions; every answer here says
which one it asked.

## What it may not do

It does not merge surfaces. `Kern-Welt` and `Kern-Welten` are two rows; whether
they are one term is `Plan/runs/judgements.jsonl`'s question and a person's. It
does not rank by importance: a model's order is kept as `rank` and labelled as a
model's. And a list whose cited lines mostly fail is reported as a
reconstruction, never searched as if it were a reading.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import subject  # noqa: E402

LISTS = ROOT / "Plan" / "entities"
DERIVED = ROOT / "Plan" / "derived"
MATRIX = DERIVED / "entities-matrix.json"

# `- Kern-Welt  ^[L152]  · place` — the kind is optional and provisional.
ROW = re.compile(r"^-\s*(?P<term>.+?)\s*\^\[L(?P<line>\d+)\]\s*(?:·\s*(?P<kind>[\w-]+))?\s*$")
TOKEN = re.compile(r"\w+|[^\w\s]")
# A list with fewer verified rows than this share is a reconstruction, not a reading.
READING = 0.9


def tokens(text: str) -> list[str]:
    return TOKEN.findall(text)


# ── the lists ─────────────────────────────────────────────────────────────────

def parse(path: Path) -> dict:
    """One model list: its header fields, its cited rows, and anything else it said."""
    head, rows, unread, other = {}, [], [], []
    for number, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if m := ROW.match(line):
            rows.append({"term": m["term"], "line": int(m["line"]),
                         "kind": m["kind"] or "", "rank": len(rows) + 1})
        elif line.startswith("- UNREAD"):
            unread.append(line[len("- UNREAD"):].strip())
        elif ":" in line and not line.startswith(("-", "#", ">")) and not rows:
            key, _, value = line.partition(":")
            head[key.strip()] = value.strip()
        elif line.startswith("- "):
            other.append(line)
    return {"slug": path.stem, "head": head, "rows": rows, "unread": unread, "uncited": other}


def lists(slugs: list[str] | None = None) -> list[dict]:
    paths = [LISTS / f"{s}.md" for s in slugs] if slugs else sorted(LISTS.glob("*.md"))
    return [parse(p) for p in paths if p.exists() and p.name != "README.md"]


def verify(entry: dict) -> dict:
    """Mark each row verified if its cited file line contains the entity.

    The comparison is `rlm_ingest.verified`'s, which is `quotes.py`'s normalisation,
    so a model list is held to the same test as a model candidate list.
    """
    from rlm_ingest import verified
    good, _ = verified(entry["slug"], [(r["term"], r["line"]) for r in entry["rows"]])
    pool = list(good)
    for row in entry["rows"]:
        row["verified"] = row["term"] in pool
        if row["verified"]:
            pool.remove(row["term"])
    total = len(entry["rows"]) + len(entry["uncited"])
    ok = sum(r["verified"] for r in entry["rows"])
    entry["verified"] = ok
    entry["total"] = total
    entry["reading"] = bool(total) and ok / total >= READING and not entry["unread"]
    return entry


# ── the search ────────────────────────────────────────────────────────────────

class Corpus:
    """Every landed body, tokenised once, with the file line of every token."""

    def __init__(self) -> None:
        self.docs = []
        for doc in subject.documents():
            toks, lines = [], []
            for i, line in enumerate(doc.lines()):
                for t in tokens(line):
                    toks.append(t)
                    lines.append(i + doc.offset)
            self.docs.append({"slug": doc.slug, "category": doc.category,
                              "date": doc.date, "tokens": toks, "lines": lines})

    def search(self, entities: list[str]) -> dict[str, list[dict]]:
        """{entity: [{slug, n, first_line}, ...]} for every entity, in one pass per document."""
        by_first: dict[str, list[tuple[str, list[str]]]] = defaultdict(list)
        for e in entities:
            seq = tokens(e)
            if seq:
                by_first[seq[0]].append((e, seq))
        hits: dict[str, dict[str, dict]] = defaultdict(dict)
        for doc in self.docs:
            toks = doc["tokens"]
            for i, t in enumerate(toks):
                for e, seq in by_first.get(t, ()):
                    if toks[i:i + len(seq)] == seq:
                        h = hits[e].setdefault(doc["slug"], {"slug": doc["slug"], "n": 0,
                                                              "first_line": doc["lines"][i],
                                                              "date": doc["date"],
                                                              "category": doc["category"]})
                        h["n"] += 1
        return {e: sorted(hits.get(e, {}).values(), key=lambda h: (h["date"] or "", h["slug"]))
                for e in entities}


def verified_entities(entries: list[dict]) -> dict[str, dict]:
    """Every verified surface, with which lists named it and at what rank."""
    out: dict[str, dict] = {}
    for entry in entries:
        verify(entry)
        if not entry["reading"]:
            continue
        for row in entry["rows"]:
            if row["verified"]:
                e = out.setdefault(row["term"], {"named_by": [], "kinds": set()})
                e["named_by"].append({"slug": entry["slug"], "rank": row["rank"]})
                if row["kind"]:
                    e["kinds"].add(row["kind"])
    return out


# ── commands ──────────────────────────────────────────────────────────────────

def cmd_verify(slugs: list[str]) -> int:
    entries = [verify(e) for e in lists(slugs or None)]
    readings = sum(e["reading"] for e in entries)
    for e in entries:
        flag = "reading" if e["reading"] else "RECONSTRUCTION"
        extra = f", {len(e['unread'])} unread" if e["unread"] else ""
        print(f"  {e['verified']:>3}/{e['total']:<3} {flag:<14} {e['slug']}{extra}")
    print(f"\n{len(entries)} lists, {readings} readings, "
          f"{len(entries) - readings} reconstructions; "
          f"{sum(e['verified'] for e in entries)} of {sum(e['total'] for e in entries)} rows verified")
    landed = {d.slug for d in subject.documents()}
    have = {e["slug"] for e in entries}
    if not slugs:
        print(f"{len(landed - have)} landed documents have no list")
    return 0 if readings == len(entries) else 1


def cmd_search(terms: list[str], as_json: bool) -> int:
    found = Corpus().search(terms)
    if as_json:
        print(json.dumps(found, ensure_ascii=False, indent=1))
        return 0
    for term, hits in found.items():
        print(f"{term}: {len(hits)} documents, {sum(h['n'] for h in hits)} occurrences "
              f"(whole-word, case-sensitive)")
        for h in sorted(hits, key=lambda h: -h["n"])[:15]:
            print(f"  {h['n']:>5}  {h['slug']}  ^[{h['slug']}.md:L{h['first_line']}]")
    return 0


def build_matrix() -> dict:
    entities = verified_entities(lists())
    found = Corpus().search(sorted(entities))
    matrix = {
        "by": "scripts/entities.py matrix",
        "matching": "whole-word, case-sensitive, whitespace-insensitive token sequence",
        "entities": {
            e: {"named_by": meta["named_by"], "kinds": sorted(meta["kinds"]),
                "documents": len(found[e]), "occurrences": sum(h["n"] for h in found[e]),
                "in": {h["slug"]: [h["n"], h["first_line"]] for h in found[e]}}
            for e, meta in entities.items()
        },
    }
    DERIVED.mkdir(parents=True, exist_ok=True)
    MATRIX.write_text(json.dumps(matrix, ensure_ascii=False), encoding="utf-8")
    return matrix


def load_matrix() -> dict:
    return json.loads(MATRIX.read_text(encoding="utf-8")) if MATRIX.exists() else build_matrix()


def cmd_matrix() -> int:
    m = build_matrix()["entities"]
    print(f"{len(m)} verified entities, searched in every landed document -> "
          f"{MATRIX.relative_to(ROOT)}\n")
    print("  docs  named-by  entity")
    for e, v in sorted(m.items(), key=lambda kv: -kv[1]["documents"])[:40]:
        print(f"  {v['documents']:>4}  {len(v['named_by']):>8}  {e}")
    return 0


def cmd_doc(slug: str, limit: int) -> int:
    m = load_matrix()["entities"]
    here = [(e, v["in"][slug][0], v["documents"]) for e, v in m.items() if slug in v["in"]]
    print(f"{len(here)} known entities occur in {slug}\n\n     n  docs  entity")
    for e, n, docs in sorted(here, key=lambda x: -x[1])[:limit]:
        print(f"  {n:>4}  {docs:>4}  {e}")
    return 0


def cmd_missing(min_docs: int) -> int:
    """P10's MISSING bucket: entities the corpus uses widely and the wiki does not have."""
    from wiki_index import fold
    index = json.loads((ROOT / "Wiki" / "index.json").read_text(encoding="utf-8"))
    have = {fold(s) for t in index["terms"].values() for s in t["surfaces"]}
    m = load_matrix()["entities"]
    rows = [(e, v["documents"], len(v["named_by"])) for e, v in m.items()
            if v["documents"] >= min_docs and fold(e) not in have]
    print(f"{len(rows)} entities occur in {min_docs}+ documents and fold to no wiki surface\n")
    print("  docs  named-by  entity")
    for e, docs, named in sorted(rows, key=lambda r: -r[1]):
        print(f"  {docs:>4}  {named:>8}  {e}")
    return 0


def cmd_score(slug: str) -> int:
    """P27: two difference lists by name, never one number on its own."""
    from wiki_index import fold
    gold_path = ROOT / "Plan" / "runs" / slug / "03-candidates.md"
    if not gold_path.exists():
        print(f"no reader's list for {slug}")
        return 1
    gold_text = gold_path.read_text(encoding="utf-8")
    if "Reconstructed" in gold_text.split("\n## ")[0]:
        print(f"{slug}'s list is a reconstruction and cannot serve as gold")
        return 1
    gold = {fold(l[2:].split("^[")[0]): l[2:].split("^[")[0].strip()
            for l in gold_text.splitlines() if l.startswith("- ")}
    entry = verify(lists([slug])[0])
    model = {fold(r["term"]): r["term"] for r in entry["rows"] if r["verified"]}
    both = gold.keys() & model.keys()
    p = len(both) / len(model) if model else 0.0
    r = len(both) / len(gold) if gold else 0.0
    f = 2 * p * r / (p + r) if p + r else 0.0
    print(f"reader {len(gold)}, model {len(model)} verified, shared {len(both)} (folded)")
    print(f"precision {p:.2f}  recall {r:.2f}  F1 {f:.2f}  — two readers scored 0.66 (P27)\n")
    print("only the reader:\n  " + "\n  ".join(sorted(gold[k] for k in gold.keys() - both)))
    print("\nonly the model:\n  " + "\n  ".join(sorted(model[k] for k in model.keys() - both)))
    return 0


def cmd_selftest() -> int:
    """The token matcher must agree with `\\bterm\\b` wherever whitespace cannot differ."""
    corpus = Corpus()
    docs = subject.documents()
    probes = ["AEGIS", "Kern-Welt", "Juna", "Entropie", "Guardian", "Nexus", "Wächter", "KW1"]
    found = corpus.search(probes)
    bad = 0
    for term in probes:
        pattern = re.compile(rf"(?<!\w){re.escape(term)}(?!\w)")
        want = sum(len(pattern.findall(d.body)) for d in docs)
        got = sum(h["n"] for h in found[term])
        mark = "ok " if want == got else "BAD"
        bad += want != got
        print(f"  {mark} {term:<12} regex {want:>6}  tokens {got:>6}")
    return 1 if bad else 0


def main(argv: list[str]) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="cmd", required=True)
    sub.add_parser("verify").add_argument("slugs", nargs="*")
    s = sub.add_parser("search")
    s.add_argument("terms", nargs="+")
    s.add_argument("--json", action="store_true")
    d = sub.add_parser("doc")
    d.add_argument("slug")
    d.add_argument("--limit", type=int, default=50)
    sub.add_parser("matrix")
    m = sub.add_parser("missing")
    m.add_argument("--min-docs", type=int, default=10)
    sub.add_parser("score").add_argument("slug")
    sub.add_parser("selftest")
    a = parser.parse_args(argv)
    if a.cmd == "verify":
        return cmd_verify(a.slugs)
    if a.cmd == "search":
        return cmd_search(a.terms, a.json)
    if a.cmd == "doc":
        return cmd_doc(a.slug, a.limit)
    if a.cmd == "matrix":
        return cmd_matrix()
    if a.cmd == "missing":
        return cmd_missing(a.min_docs)
    if a.cmd == "score":
        return cmd_score(a.slug)
    return cmd_selftest()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
