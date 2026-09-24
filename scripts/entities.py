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
    python3 scripts/entities.py place <slug> <names.json> # a model's names -> a list, lines by code

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
    """Every per-document list: a file here named for a landed document. Other
    files share the folder (README.md, bilingual.md) and are not lists."""
    landed = {d.slug for d in subject.documents()}
    paths = [LISTS / f"{s}.md" for s in slugs] if slugs else sorted(LISTS.glob("*.md"))
    return [parse(p) for p in paths if p.exists() and p.stem in landed]


def verify(entry: dict) -> dict:
    """Mark each row verified if its cited file line holds the entity as a whole word.

    Revision 2 asked `rlm_ingest.verified`'s substring question, so `Kontakt` cited
    at a line saying `Kontaktaufnahme` passed. `holds` is the question `place`
    asks, so a list code placed verifies by construction and a typed one is held
    to the same standard.
    """
    doc = subject.document(entry["slug"])
    lines = doc.lines()
    for row in entry["rows"]:
        index = row["line"] - doc.offset
        row["verified"] = 0 <= index < len(lines) and holds(lines[index], row["term"])
    total = len(entry["rows"]) + len(entry["uncited"])
    ok = sum(r["verified"] for r in entry["rows"])
    entry["verified"] = ok
    entry["total"] = total
    entry["reading"] = bool(total) and ok / total >= READING and not entry["unread"]
    return entry


# ── placing: the model names, the code cites ──────────────────────────────────

def plain(text: str) -> str:
    """`quotes.normalise` without its footnote rule, for names rather than quotes.

    `quotes.normalise` drops a number of one or two digits glued to a word, because
    the export glues footnote numbers on (`formen.10`). A quote carries the same
    context on both sides, so the rule is symmetric there — and blind to the
    number, which is why `quotes.missing_number` now compares numbers on their
    own. A name does not: on the
    line `(KW2),` loses its `2` while the bare name `KW2` keeps it, so a name ending
    in a digit could never match — and stripping it from the name as well would
    make `KW1` to `KW4` one name. Escaping, emphasis, wrapping and attribution
    markers are context-free and stay.
    """
    import quotes
    return quotes.unglued(text).strip()


def holds(line: str, term: str) -> bool:
    """Does this one line hold `term` as a whole word? Placing and verifying ask
    this same question, so a placed line verifies by construction (P26)."""
    want = plain(term)
    if not want:
        return False
    pattern = r"(?<!\w)" + r"\s+".join(map(re.escape, want.split())) + r"(?!\w)"
    return re.search(pattern, plain(line)) is not None


def first_line(doc, term: str) -> int | None:
    """The first file line holding `term` as a whole word, on one line.

    Whole-word so that `KI` is not placed inside `KIRA`; one line so that the
    placement passes `verify`, which reads one line. A name the document only
    writes across a wrap, or never writes at all, gets no line — and is refused.
    """
    for index, line in enumerate(doc.lines()):
        if holds(line, term):
            return doc.offset + index
    return None


def place(slug: str, named: dict) -> tuple[str, list[str]]:
    """Revision 3 of the entity lists (P26): a model returns names, code writes lines.

    Revision 2 asked the model to run `read.py --find` and copy the answer; it
    typed lines anyway, and 2 of 4 lists failed `verify`. Here no line is ever
    typed, so a row cannot cite the wrong one — and a name the document does not
    contain is dropped and counted, not rewritten into something that does.
    """
    doc = subject.document(slug)
    # The last line with text on it: a trailing blank line cannot be read or skipped.
    last = doc.offset + max((i for i, l in enumerate(doc.lines()) if l.strip()), default=0)
    rows, refused, seen = [], [], set()
    for item in named.get("entities", []):
        term = " ".join(str(item.get("term", "")).split())
        if not term or term in seen:
            continue
        seen.add(term)
        line = first_line(doc, term)
        if line is None:
            refused.append(term)
            continue
        kind = str(item.get("kind") or "other").strip() or "other"
        rows.append(f"- {term}  ^[L{line}]  · {kind}")
    head = [f"written_by: {named.get('written_by', 'a model')}; lines placed by scripts/entities.py place (revision 3)",
            f"source: {slug}",
            f"lines: {last}",
            f"refused: {len(refused)}" + (f" — {'; '.join(refused)}" if refused else ""),
            ""]
    read_to = int(named.get("read_to_line") or 0)
    tail = [f"- UNREAD L{read_to + 1}-{last}: the reader reported reading to L{read_to}"] if read_to and read_to < last else []
    return "\n".join(head + rows + tail) + "\n", refused


def cmd_place(slug: str, source: str) -> int:
    named = json.loads(Path(source).read_text(encoding="utf-8"))
    if isinstance(named, dict) and slug in named and "entities" not in named:
        named = named[slug]
    text, refused = place(slug, named)
    out = LISTS / f"{slug}.md"
    out.write_text(text, encoding="utf-8")
    placed = [int(m["line"]) for l in text.splitlines() if (m := ROW.match(l))]
    lines = int(text.split("lines: ", 1)[1].split("\n", 1)[0])
    # A reader's read_to_line is its own claim. The furthest line a placed name
    # lands on is the code's: a list whose names all sit in the first third was
    # not written from the whole document, whatever it reports.
    furthest = max(placed, default=0)
    print(f"{out.relative_to(ROOT)}: {len(placed)} rows placed, {len(refused)} names refused; "
          f"reader says read to L{named.get('read_to_line')}, furthest placed name L{furthest} of {lines}")
    return 0


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


def cmd_score(slug: str, names: str | None = None) -> int:
    """P27: two difference lists by name, never one number on its own.

    With `names`, any tool's output is scored the same way: a names file in the
    shape `place` reads, each name placed by `first_line` exactly as `place` does,
    so a name the document does not contain word for word — a translation, a
    paraphrase — is refused and counted, never scored (P19, P26). A name whose
    `scope` is not `world` (an outside work the document uses as a lens) is set
    apart: the readers' lists hold this world's terms only."""
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
    refused: list[str] = []
    lens: list[str] = []
    if names:
        doc = subject.document(slug)
        model = {}
        for item in json.loads(Path(names).read_text(encoding="utf-8")).get("entities", []):
            term = " ".join(str(item.get("term", "")).split())
            if not term:
                continue
            if item.get("scope", "world") != "world":
                lens.append(term)
            elif first_line(doc, term) is None:
                refused.append(term)
            else:
                model.setdefault(fold(term), term)
    else:
        entry = verify(lists([slug])[0])
        model = {fold(r["term"]): r["term"] for r in entry["rows"] if r["verified"]}
    both = gold.keys() & model.keys()
    p = len(both) / len(model) if model else 0.0
    r = len(both) / len(gold) if gold else 0.0
    f = 2 * p * r / (p + r) if p + r else 0.0
    print(f"reader {len(gold)}, model {len(model)} verified, shared {len(both)} (folded)"
          + (f"; {len(refused)} refused (not in the document word for word), {len(lens)} set apart as lens"
             if names else ""))
    print(f"precision {p:.2f}  recall {r:.2f}  F1 {f:.2f}  — two readers scored 0.66 (P27)\n")
    print("only the reader:\n  " + "\n  ".join(sorted(gold[k] for k in gold.keys() - both)))
    print("\nonly the model:\n  " + "\n  ".join(sorted(model[k] for k in model.keys() - both)))
    if refused:
        print("\nrefused:\n  " + "\n  ".join(sorted(set(refused))))
    if lens:
        print("\nlens, not scored:\n  " + "\n  ".join(sorted(set(lens))))
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
    # `holds` places and verifies every line: each case is a defect it once had
    # or must never have, so a change that breaks one says which.
    cases = [
        ("Emotion und Trauma (KW2), Abwehr", "KW2", True),     # footnote rule ate the 2
        ("Emotion und Trauma (KW2), Abwehr", "KW", False),     # ...and made KW1-4 one name
        ("Das Spiel *Silent Hill 2* nutzt", "Silent Hill 2", True),
        ("die Kern\\-Welt 1 als Labyrinth", "Kern-Welt 1", True),  # export escaping
        ("vor der Kontaktaufnahme", "Kontakt", False),         # revision 2 passed this
        ("die KIRA-Instanz", "KI", False),
        ("des McLaughlin-Graphen", "McLaughlin-Graph", False),
    ]
    for line, term, want in cases:
        got = holds(line, term)
        bad += got != want
        print(f"  {'ok ' if got == want else 'BAD'} holds({term!r}) on {line!r}: {got}")
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
    sc = sub.add_parser("score")
    sc.add_argument("slug")
    sc.add_argument("--names", help="score this names file instead of the model list on disk")
    sub.add_parser("selftest")
    pl = sub.add_parser("place")
    pl.add_argument("slug")
    pl.add_argument("names", help="JSON: {entities: [{term, kind}], read_to_line, written_by}")
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
        return cmd_score(a.slug, a.names)
    if a.cmd == "place":
        return cmd_place(a.slug, a.names)
    return cmd_selftest()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
