#!/usr/bin/env python3
"""Everything a program can read off the source documents, as graph rows — and learned hyperedges.

`askdb.py build` calls `extract()` and loads its rows into `Plan/derived/ask.db`.
The author, 2026-09-30: „keep the bm25 Lines Relations in the Graph - so that Lines that
are within the same Paragraph are related - extract everything you mechanically can from
the source Documents - as Graph relational Data - and also add learned hyperedges".

**Stated by the text** (each fact is a string that stands on a line; nothing is judged):

    (:Doc)-[:HAS_SECTION]->(:Section)-[:SUB]->(:Section)        markdown headings, by level
    (:Section|:Doc)-[:HAS_PARAGRAPH]->(:Paragraph)-[:NEXT]->(:Paragraph)
    (:Paragraph)-[:HAS_LINE]->(:Line)-[:NEXT]->(:Line)           lines of one block are related
    (:Line)-[:MENTIONS]->(:Term)            a page surface standing alone (`wiki_index.mention`)
    (:Line)-[:NAMES_CHAPTER {n}]->(:Chapter)                     `Kap N`, `Kapitel N`, `Chapter N`
    (:Line)-[:LINKS_URL]->(:Url {host})                           every http(s) URL
    Line.stance                                                  `[K]`, `[V]`, `[S]`, `[L]` on the line

A paragraph is a block: consecutive non-empty lines. Its `kind` is `heading`, `table`,
`list`, `quote` or `text`, by its first line.

**Proposals** (relation types start with `P_`; no stated query names one):

    (:Line)-[:P_NAMES]->(:Entity)           a verified entity list's name on the line
    (:Hyperedge)-[:P_MEMBER]->(…)           learned, below

**Learned hyperedges** — counted, never judged; each carries its method and support:

- `cooccur` — a set of two or three terms that stand in the same paragraph in at least
  `MIN_DOCS` documents (frequent itemsets over paragraphs, counted per document so one
  long document cannot make a set frequent). Support is the number of documents; lift
  compares it with what the terms' own frequencies predict.
- `parallel` — paragraphs in different documents that share a run of `SHINGLE` words
  (the length `route.py` treats as the same text), grouped by union-find: the same
  passage carried from document to document. Support is the number of documents.

A hyperedge is a node because a relation of three or more members is not an edge; its
members hang off it by `P_MEMBER`.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

MIN_DOCS = 5          # a co-occurrence set must stand together in at least this many documents
MIN_LIFT = 1.5        # and more often than the terms' own frequencies predict
SHINGLE = 12          # words: the run route.py treats as the same text
HEADING = re.compile(r"^(#{1,6})\s+(.*)$")
CHAPTER = re.compile(r"\b(?:Kap(?:itel)?|Chapter)\.?\s*(\d{1,2})\b")
URL = re.compile(r"https?://([^/\s)\]>\"']+)[^\s)\]>\"']*")
STANCE = re.compile(r"\[([KVSL])\]")
WORD = re.compile(r"\w+")


def kind_of(first: str) -> str:
    s = first.lstrip()
    if s.startswith("#"):
        return "heading"
    if s.startswith("|"):
        return "table"
    if re.match(r"([-*+]|\d+[.)])\s", s):
        return "list"
    if s.startswith(">"):
        return "quote"
    return "text"


def surface_matcher(surfaces: dict[str, str]):
    """One pattern for every surface, longest first, standing alone as `wiki_index.mention` does."""
    ordered = sorted((s for s in surfaces if len(s) >= 3), key=len, reverse=True)
    if not ordered:
        return None, surfaces
    alt = "|".join(re.escape(s) for s in ordered)
    return re.compile(rf"(?<![\w-])(?:{alt})(?![\w-])"), surfaces


def extract(docs: list[tuple[str, Path]], term_surfaces: dict[str, str], entity_names: list[str],
            chapters: set[int]) -> dict:
    """Rows for `askdb.build`: nodes {key: (props, label)}, edges [(a, b, props, type)]."""
    nodes: dict[str, tuple[dict, str]] = {}
    edges: list[tuple[str, str, dict, str]] = []
    term_rx, _ = surface_matcher(term_surfaces)
    ent_rx, _ = surface_matcher({n: n for n in entity_names})
    para_terms: list[tuple[str, str, frozenset]] = []        # (doc, paragraph, terms)
    shingle_owner: dict[int, set[str]] = defaultdict(set)     # shingle -> paragraphs
    para_doc: dict[str, str] = {}

    for slug, path in docs:
        lines = path.read_text(encoding="utf-8").split("\n")
        doc = f"doc:{slug}"
        stack: list[tuple[int, str]] = []                    # (level, section key)
        prev_para = None
        i = 0
        while i < len(lines):
            if not lines[i].strip():
                i += 1
                continue
            first = i
            while i < len(lines) and lines[i].strip():
                i += 1
            block = list(range(first, i))                    # 0-based indices
            head = HEADING.match(lines[first])
            if head:
                level = len(head.group(1))
                sec = f"sec:{slug}:{first + 1}"
                nodes[sec] = ({"slug": slug, "line": first + 1, "level": level,
                               "title": head.group(2).strip()[:200]}, "Section")
                while stack and stack[-1][0] >= level:
                    stack.pop()
                edges.append((stack[-1][1] if stack else doc, sec, {}, "SUB" if stack else "HAS_SECTION"))
                stack.append((level, sec))
            para = f"para:{slug}:{first + 1}"
            para_doc[para] = slug
            nodes[para] = ({"slug": slug, "first": first + 1, "last": i, "kind": kind_of(lines[first])},
                           "Paragraph")
            edges.append((stack[-1][1] if stack else doc, para, {}, "HAS_PARAGRAPH"))
            if prev_para:
                edges.append((prev_para, para, {}, "NEXT"))
            prev_para = para
            found_terms: set[str] = set()
            prev_line = None
            words_in_block: list[str] = []
            for j in block:
                n = j + 1
                text = lines[j]
                key = f"line:{slug}:{n}"
                props = {"slug": slug, "line": n, "para": para}
                st = STANCE.findall(text)
                if st:
                    props["stance"] = "".join(sorted(set(st)))
                nodes[key] = (props, "Line")
                edges.append((para, key, {}, "HAS_LINE"))
                if prev_line:
                    edges.append((prev_line, key, {}, "NEXT"))
                prev_line = key
                if term_rx:
                    for m in {m.group(0) for m in term_rx.finditer(text)}:
                        t = term_surfaces[m]
                        edges.append((key, t, {"surface": m}, "MENTIONS"))
                        found_terms.add(t)
                if ent_rx:
                    for m in {m.group(0) for m in ent_rx.finditer(text)}:
                        edges.append((key, f"entity:{m}", {}, "P_NAMES"))
                for c in {int(x) for x in CHAPTER.findall(text)}:
                    if c in chapters:
                        edges.append((key, f"chapter:kap-{c:02d}", {"n": c}, "NAMES_CHAPTER"))
                for host in {h.lower() for h in URL.findall(text)}:
                    u = f"url:{host}"
                    if u not in nodes:
                        nodes[u] = ({"host": host}, "Url")
                    edges.append((key, u, {}, "LINKS_URL"))
                words_in_block += WORD.findall(text.lower())
            if found_terms:
                para_terms.append((slug, para, frozenset(found_terms)))
            for k in range(len(words_in_block) - SHINGLE + 1):
                shingle_owner[hash(tuple(words_in_block[k:k + SHINGLE]))].add(para)

    hyper = learn_cooccurrence(para_terms) + learn_parallel(shingle_owner, para_doc)
    for h in hyper:
        nodes[h["key"]] = ({k: v for k, v in h.items() if k not in ("key", "members")}, "Hyperedge")
        for m in h["members"]:
            edges.append((h["key"], m, {}, "P_MEMBER"))
    return {"nodes": nodes, "edges": edges, "hyperedges": len(hyper)}


def learn_cooccurrence(para_terms: list[tuple[str, str, frozenset]]) -> list[dict]:
    """Sets of 2–3 terms sharing a paragraph in at least MIN_DOCS documents, with lift."""
    docs_all = {d for d, _, _ in para_terms}
    term_docs: dict[str, set] = defaultdict(set)
    set_docs: dict[frozenset, set] = defaultdict(set)
    for doc, _, terms in para_terms:
        for t in terms:
            term_docs[t].add(doc)
        ts = sorted(terms)[:12]                 # a paragraph naming dozens of terms is a list, not a relation
        for r in (2, 3):
            for combo in combinations(ts, r):
                set_docs[frozenset(combo)].add(doc)
    n = max(len(docs_all), 1)
    out = []
    for combo, docs in set_docs.items():
        if len(docs) < MIN_DOCS:
            continue
        expected = n
        for t in combo:
            expected *= len(term_docs[t]) / n
        lift = len(docs) / expected if expected else 0.0
        if lift < MIN_LIFT:
            continue
        key = "hyper:cooccur:" + hashlib.sha1("|".join(sorted(combo)).encode()).hexdigest()[:12]
        out.append({"key": key, "method": "cooccur", "support": len(docs), "lift": round(lift, 2),
                    "size": len(combo), "learned": True, "members": sorted(combo)})
    return out


def learn_parallel(shingle_owner: dict[int, set[str]], para_doc: dict[str, str]) -> list[dict]:
    """Paragraphs of different documents sharing a SHINGLE-word run, grouped by union-find."""
    parent: dict[str, str] = {}

    def find(x):
        while parent.setdefault(x, x) != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for paras in shingle_owner.values():
        if len({para_doc[p] for p in paras}) < 2 or len(paras) > 50:   # boilerplate shared everywhere
            continue
        ps = sorted(paras)
        for p in ps[1:]:
            ra, rb = find(ps[0]), find(p)
            if ra != rb:
                parent[rb] = ra
    groups: dict[str, list[str]] = defaultdict(list)
    for p in parent:
        groups[find(p)].append(p)
    out = []
    for root, members in groups.items():
        docs = {para_doc[p] for p in members}
        if len(docs) < 2:
            continue
        key = "hyper:parallel:" + hashlib.sha1(root.encode()).hexdigest()[:12]
        out.append({"key": key, "method": "parallel", "support": len(docs), "size": len(members),
                    "learned": True, "members": sorted(members)})
    return out


def selftest() -> list[str]:
    import tempfile
    fails = []
    with tempfile.TemporaryDirectory() as d:
        a, b = Path(d) / "a.md", Path(d) / "b.md"
        shared = "eins zwei drei vier fünf sechs sieben acht neun zehn elf zwölf dreizehn"
        a.write_text("# Kopf\n\nAEGIS und Juna in Kap 38 [K]\nzweite Zeile https://example.org/x\n\n"
                     f"{shared}\n", encoding="utf-8")
        b.write_text(f"Vorwort\n\n{shared} und mehr\n", encoding="utf-8")
        rows = extract([("a", a), ("b", b)], {"AEGIS": "term:aegis", "Juna": "term:juna"}, [], {38})
        n, e = rows["nodes"], rows["edges"]
        types = Counter(t for *_, t in e)
        if "sec:a:1" not in n or n["sec:a:1"][1] != "Section":
            fails.append("heading did not become a section")
        if ("para:a:3", "line:a:4", {}, "HAS_LINE") not in e:
            fails.append("the second line of a paragraph is not in it")
        if ("line:a:3", "line:a:4", {}, "NEXT") not in e:
            fails.append("two lines of one paragraph are not related")
        if n["line:a:3"][0].get("stance") != "K":
            fails.append("stance mark not read")
        if types["MENTIONS"] != 2 or types["NAMES_CHAPTER"] != 1 or types["LINKS_URL"] != 1:
            fails.append(f"mechanical facts wrong: {dict(types)}")
        par = [k for k, (p, lab) in n.items() if lab == "Hyperedge" and p["method"] == "parallel"]
        if len(par) != 1:
            fails.append(f"the passage shared by a and b is not one parallel hyperedge: {par}")
    return fails


if __name__ == "__main__":
    fails = selftest()
    for f in fails:
        print("FAIL", f)
    print(f"askextract selftest: {'held' if not fails else 'FAILED'}")
    sys.exit(1 if fails else 0)
