"""Cross-document retrieval for the pipeline: who else writes a page's names, and where the graph is thin.

The wiki's graph knows the reconciled documents only; the other landed documents
reach it through search alone (`Plan/concept/ask-sources_2026-09-30.md`, *The gap*).
This asks the whole corpus by code. Which documents write a page's names is a
**count** — `corpus.py`'s whole-word index, never a search rank (CLAUDE.md: a
search result never becomes a number). Who is already read onto a page is the
page's own `ingested:`. It decides nothing: a document that writes a name may say
nothing about the thing, and only a reader can tell.

    python3 scripts/crossdoc.py doc <slug> [--limit 5]   # a reconciliation's context
    python3 scripts/crossdoc.py coverage [--top 15]      # the graph's thin places
    python3 scripts/crossdoc.py selftest

`doc` takes the pages one document reads onto — its readings, or before them its
lookup's pages and sweep hits — and for each names three groups:
- the documents with a reading on the page;
- **read but not on the page**: documents with a census that write its names
  and have no reading on it — a sweep to re-check, or an occurrence;
- **unread**: documents with no census that write its names, the most
  frequent first, each with its first line.

It writes `Plan/runs/<slug>/crossdoc.md` for the readings brief and the record.
The unread group is where `ask` goes next: `ask.py ask` routes over every landed
line, and its verified answer lands as an M-ask source (decision 017).

`coverage` does the same for every page and every open record. A page is thin
where many documents write its names and few are read onto it. A record is thin
where unread documents write the names of several of its pages. The unread
documents that touch the most open records are the reading queue. It writes
`Plan/runs/coverage-<date>/coverage.json` and `README.md`. Standard library only.
"""

from __future__ import annotations

import datetime
import json
import re
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import bm25rel  # noqa: E402
import corpus  # noqa: E402

FRONT = re.compile(r"\A---\n(.*?)\n---\n", re.S)


def frontmatter_list(text: str, key: str) -> list[str]:
    m = FRONT.match(text)
    if not m:
        return []
    found = re.search(rf"^{key}: *\[(.*?)\]", m.group(1), re.M | re.S)
    return re.findall(r'"([^"]+)"', found.group(1)) if found else []


def pages(root: Path = ROOT) -> dict[str, dict]:
    """Every term page: its surfaces (from the index) and the documents read onto it."""
    index = json.loads((root / "Wiki" / "index.json").read_text(encoding="utf-8"))
    out = {}
    for slug, term in index["terms"].items():
        page = root / "Wiki" / "candidates" / f"{slug}.md"
        if not page.exists():
            continue
        surfaces = [s for s in term.get("surfaces") or [] if s != slug]
        out[slug] = {"surfaces": surfaces,
                     "read_on": frontmatter_list(page.read_text(encoding="utf-8"), "ingested")}
    return out


def records(root: Path = ROOT) -> dict[str, dict]:
    """Every conflict and question record: its id, title and the pages it concerns."""
    out = {}
    for folder in ("conflicts", "questions"):
        for f in sorted((root / "Wiki" / folder).glob("[cq][0-9]*.md")):
            text = f.read_text(encoding="utf-8")
            title = re.search(r"^# (.+)$", text, re.M)
            out[f.stem.split("-", 1)[0].upper()] = {
                "file": f.name, "title": title.group(1) if title else f.stem,
                "pages": frontmatter_list(text, "pages") or sorted(set(re.findall(r"\[\[([a-z0-9-]+)", text)))}
    return out


class Corpus:
    """Whole-word counts of any surface in every landed document, from `corpus.py`."""

    def __init__(self):
        self._index = None
        self._bodies = None
        self._cache: dict[str, list[dict]] = {}

    def where(self, surface: str) -> list[dict]:
        if surface not in self._cache:
            if corpus.INDEXABLE.match(surface):
                self._index = self._index if self._index is not None else corpus.indexed()
                docs = self._index
            else:
                self._bodies = self._bodies if self._bodies is not None else corpus.landed()
                docs = self._bodies
            self._cache[surface] = corpus.occurrences(docs, surface)
        return self._cache[surface]

    def named_in(self, surfaces: list[str]) -> dict[str, dict]:
        """document -> {n: all surfaces' counts, first_line, surface: the most frequent}."""
        out: dict[str, dict] = {}
        for s in surfaces:
            for hit in self.where(s):
                d = out.setdefault(hit["slug"], {"n": 0, "first_line": hit["first_line"], "surface": s, "_best": 0})
                d["n"] += hit["n"]
                if hit["n"] > d["_best"]:
                    d["surface"], d["_best"] = s, hit["n"]
                if hit["first_line"] is not None and (d["first_line"] is None or hit["first_line"] < d["first_line"]):
                    d["first_line"] = hit["first_line"]
        for d in out.values():
            d.pop("_best", None)
        return out


def read_documents(root: Path = ROOT) -> set[str]:
    return {p.stem for p in (root / "Sources" / "terms").glob("*.md")}


def swept(root: Path = ROOT) -> set[tuple[str, str]]:
    """(page, document) pairs the sweep already decided — a reading or an occurrence."""
    f = root / "Plan" / "runs" / "sweep.jsonl"
    rows = [json.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()] if f.exists() else []
    return {(r.get("page"), r.get("document")) for r in rows}


def groups(page: dict, named: dict[str, dict], read: set[str], exclude: str | None = None,
           decided: set[tuple[str, str]] | None = None, slug: str | None = None) -> dict:
    on = [d for d in page["read_on"] if d != exclude]
    not_on = sorted((d for d in named if d in read and d not in page["read_on"] and d != exclude
                     and (slug, d) not in (decided or set())),
                    key=lambda d: -named[d]["n"])
    unread = sorted((d for d in named if d not in read and d != exclude), key=lambda d: -named[d]["n"])
    return {"read_on": on, "read_not_on": not_on, "unread": unread}


def doc_pages(slug: str, root: Path = ROOT) -> list[str]:
    """The pages one document reads onto: its readings, or its lookup's pages and sweep hits."""
    import record
    got = record.derive(slug, root, touches=False)
    if got["new_readings"]:
        return [r["page"] for r in got["new_readings"]]
    pre = json.loads((root / "Plan" / "runs" / slug / "reconcile-pre.json").read_text(encoding="utf-8"))
    found = [b["page"] for b in pre["buckets"].get("new_reading", []) + pre["buckets"].get("already_there", [])]
    found += [h["page"] for h in pre.get("in_document_not_in_census", [])]
    for item in pre["buckets"].get("needs_judgement", []):
        found += [n["page"] for n in item.get("near", []) if isinstance(n, dict) and n.get("page")]
    return list(dict.fromkeys(found))


def cmd_doc(slug: str, limit: int = 5, root: Path = ROOT, write: bool = True) -> dict:
    all_pages, read, decided = pages(root), read_documents(root), swept(root)
    c = Corpus()
    result = {"document": slug, "pages": {}}
    # The shared store is read once it is known fresh; the relations found are kept
    # after the last page, because the ledger is one of the store's inputs.
    bm25rel.fresh_or_refuse()
    found = []
    for p in doc_pages(slug, root):
        if p not in all_pages:
            continue
        named = c.named_in(all_pages[p]["surfaces"])
        g = groups(all_pages[p], named, read, exclude=slug, decided=decided, slug=p)
        # The related channel: lines that share the page's words without writing its
        # names — a P_BM25 relation each, kept in Plan/runs/bm25/ for a reader's verdict
        # (the author, 2026-09-30, on „Große Stille" and „Das große Schweigen").
        related = bm25rel.find(f"term:{p}", " ".join(all_pages[p]["surfaces"]), exclude=[slug],
                               surfaces=all_pages[p]["surfaces"], k=3, found_by=f"crossdoc.py doc {slug}",
                               stale_ok=True)
        found += related
        result["pages"][p] = {"surfaces": all_pages[p]["surfaces"], **{k + "_count": len(v) for k, v in g.items()},
                              "read_not_on": [(d, named[d]["n"], named[d]["first_line"]) for d in g["read_not_on"][:limit]],
                              "unread": [(d, named[d]["n"], named[d]["surface"], named[d]["first_line"])
                                         for d in g["unread"][:limit]],
                              "related": [(r["id"], r["target"], r["target_text"][:140]) for r in related]}
    result["related_new"] = bm25rel.keep(found) if write else 0
    if write:
        run = root / "Plan" / "runs" / slug
        (run / "crossdoc.json").write_text(json.dumps(result, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        (run / "crossdoc.md").write_text(render_doc(result), encoding="utf-8")
    return result


def render_doc(result: dict) -> str:
    out = [f"# Other documents on the pages `{result['document']}` reads onto", "",
           "`python3 scripts/crossdoc.py doc " + result["document"] + "`: whole-word counts of each page's "
           "surfaces over every landed document (`corpus.py`), never a search rank. A document that writes a "
           "name may say nothing about the thing: open the line before using it.", "",
           "| page | read on it | read, not on it | unread that write it | the unread, most first (count, line) |",
           "|---|---|---|---|---|"]
    for p, g in result["pages"].items():
        unread = "; ".join(f"`{d}` {n}× L{line}" for d, n, _, line in g["unread"]) or "—"
        out.append(f"| `{p}` | {g['read_on_count']} | {g['read_not_on_count']} | {g['unread_count']} | {unread} |")
    related = [(p, rid, tgt, txt) for p, g in result["pages"].items() for rid, tgt, txt in g.get("related", [])]
    if related:
        out += ["", "**Related, not named (`P_BM25`)** — lines that share a page's words and write none of its "
                "names. Each may be a tension, a parallel, the same thing, or noise: judge it with "
                "`python3 scripts/bm25rel.py label <id> tension|parallel|same|noise --by \"<you>\"`.", ""]
        out += [f"- `{p}` → `{tgt}` — {txt} (`{rid}`)" for p, rid, tgt, txt in related]
    not_on = [(p, d, n, l) for p, g in result["pages"].items() for d, n, l in g["read_not_on"]]
    if not_on:
        out += ["", "**Read, but not on the page** — each is a sweep to re-check or an occurrence:", ""]
        out += [f"- `{p}` ← `{d}` {n}× L{l}" for p, d, n, l in not_on]
    return "\n".join(out) + "\n"


def cmd_coverage(top: int = 15, root: Path = ROOT) -> dict:
    all_pages, read, recs, decided = pages(root), read_documents(root), records(root), swept(root)
    c = Corpus()
    per_page, touching = {}, defaultdict(set)
    for p, page in all_pages.items():
        named = c.named_in(page["surfaces"])
        g = groups(page, named, read, decided=decided, slug=p)
        per_page[p] = {"named_in": len(named), **{k: len(v) for k, v in g.items()},
                       "coverage": round(len(g["read_on"]) / len(named), 3) if named else None,
                       "unread_top": [(d, named[d]["n"]) for d in g["unread"][:5]]}
        for d in g["unread"]:
            touching[d].add(p)
    per_record = {}
    queue = defaultdict(lambda: {"records": set(), "pages": set()})
    for rid, rec in recs.items():
        rec_pages = [p for p in rec["pages"] if p in all_pages]
        docs = defaultdict(set)
        for p in rec_pages:
            for d in touching:
                if p in touching[d]:
                    docs[d].add(p)
        ranked = sorted(docs.items(), key=lambda kv: -len(kv[1]))
        per_record[rid] = {"title": rec["title"], "pages": rec_pages,
                           "unread_writing_two_or_more": [(d, sorted(ps)) for d, ps in ranked if len(ps) >= 2][:top]}
        for d, ps in ranked:
            if len(ps) >= 2:
                queue[d]["records"].add(rid)
                queue[d]["pages"] |= ps
    reading_queue = sorted(({"document": d, "records": sorted(v["records"]), "pages": len(v["pages"])}
                            for d, v in queue.items()), key=lambda q: (-len(q["records"]), -q["pages"]))[:top]
    thin = sorted(((p, v) for p, v in per_page.items() if v["named_in"]),
                  key=lambda kv: (-kv[1]["unread"], kv[1]["coverage"] or 0))[:top]
    return {"at": datetime.date.today().isoformat(), "pages": len(per_page), "read_documents": len(read),
            "per_page": per_page, "thinnest": [p for p, _ in thin], "per_record": per_record,
            "reading_queue": reading_queue}


def render_coverage(r: dict) -> str:
    pp = r["per_page"]
    named = [v for v in pp.values() if v["named_in"]]
    mean = sum(v["coverage"] for v in named) / len(named) if named else 0
    out = [f"# Where the graph is thin — {r['at']}", "",
           "`python3 scripts/crossdoc.py coverage`: for every term page, the landed documents that write one of "
           "its surfaces as a whole word (`corpus.py`, a count), against the documents read onto the page (its "
           "`ingested:`). A document that writes a name may say nothing about the thing, so every number here "
           "is an upper bound on what reading could add.", "",
           f"**{r['pages']} pages, {r['read_documents']} documents with a census.** On average a page is read "
           f"from {mean:.0%} of the documents that write its names.", "",
           "## The thinnest pages — most unread documents writing their names", "",
           "| page | write its names | read on it | read, not on it | unread | coverage | the unread, most first |",
           "|---|---|---|---|---|---|---|"]
    for p in r["thinnest"]:
        v = pp[p]
        out.append(f"| `{p}` | {v['named_in']} | {v['read_on']} | {v['read_not_on']} | {v['unread']} | "
                   f"{v['coverage']:.0%} | " + ", ".join(f"`{d}` {n}×" for d, n in v["unread_top"][:3]) + " |")
    out += ["", "## Open records — unread documents writing the names of two or more of their pages", ""]
    for rid, rec in r["per_record"].items():
        docs = rec["unread_writing_two_or_more"]
        out.append(f"- **{rid}** {rec['title']} — {len(docs)} unread documents"
                   + (": " + ", ".join(f"`{d}` ({len(ps)})" for d, ps in docs[:4]) if docs else ""))
    out += ["", "## The reading queue — unread documents touching the most open records", "",
            "| document | records | pages of theirs it names |", "|---|---|---|"]
    out += [f"| `{q['document']}` | {', '.join(q['records'])} | {q['pages']} |" for q in r["reading_queue"]]
    return "\n".join(out) + "\n"


def selftest() -> int:
    cases = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "Wiki" / "candidates").mkdir(parents=True)
        (root / "Sources" / "terms").mkdir(parents=True)
        (root / "Wiki" / "candidates" / "probe.md").write_text('---\ningested: ["a"]\n---\n# P\n', encoding="utf-8")
        (root / "Sources" / "terms" / "a.md").write_text("census\n", encoding="utf-8")
        (root / "Sources" / "terms" / "b.md").write_text("census\n", encoding="utf-8")
        page = pages.__wrapped__(root) if hasattr(pages, "__wrapped__") else None
        page = {"surfaces": ["Probe"], "read_on": ["a"]}
        named = {"a": {"n": 3}, "b": {"n": 2}, "c": {"n": 5}, "d": {"n": 1}}
        g = groups(page, named, read_documents(root))
        cases.append(("read on the page, read but not on it, unread — kept apart",
                      g == {"read_on": ["a"], "read_not_on": ["b"], "unread": ["c", "d"]}))
        g = groups(page, named, read_documents(root), exclude="c")
        cases.append(("the document itself is in no group", "c" not in sum(g.values(), [])))
    from unittest.mock import patch
    import contextlib
    page = {"surfaces": ["Probe"], "read_on": ["a"]}
    named = {d: {"n": 1, "surface": "Probe", "first_line": 10} for d in ("a", "b", "c", "d", "e")}
    with contextlib.ExitStack() as stack:
        stack.enter_context(patch(__name__ + ".pages", return_value={"probe": page}))
        stack.enter_context(patch(__name__ + ".read_documents", return_value={"a", "b"}))
        stack.enter_context(patch(__name__ + ".swept", return_value=set()))
        stack.enter_context(patch(__name__ + ".doc_pages", return_value=["probe"]))
        stack.enter_context(patch.object(Corpus, "named_in", return_value=named))
        stack.enter_context(patch.object(bm25rel, "fresh_or_refuse"))
        stack.enter_context(patch.object(bm25rel, "find", return_value=[]))
        small = cmd_doc("source", limit=1, write=False)
        large = cmd_doc("source", limit=5, write=False)
        cases.append(("doc counts survive limiting examples", small["pages"]["probe"]["unread_count"] == 3
                      and large["pages"]["probe"]["unread_count"] == 3
                      and len(small["pages"]["probe"]["unread"]) == 1))
        cases.append(("rendered count columns are numeric", "| `probe` | 1 | 1 | 3 |" in render_doc(small)))
    c = Corpus()
    hits = c.where("AEGIS")
    cases.append(("a count comes from corpus.py's whole-word index", len(hits) > 200 and all("n" in h for h in hits)))
    two = c.named_in(["Große Stille"])
    cases.append(("a phrase is counted whole-word, not ranked",
                  "kohaerenz-protokoll-meta-foreshadowing-beobachter-logik" in two
                  and all(d["n"] >= 1 and d["first_line"] for d in two.values())))
    failed = [n for n, ok in cases if not ok]
    print(f"crossdoc: {len(cases) - len(failed)} of {len(cases)} cases hold"
          + (" — FAILED: " + ", ".join(failed) if failed else ""))
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        return selftest()
    if argv[:1] == ["doc"] and len(argv) >= 2:
        limit = int(argv[argv.index("--limit") + 1]) if "--limit" in argv else 5
        result = cmd_doc(argv[1], limit)
        print(render_doc(result))
        return 0
    if argv[:1] == ["coverage"]:
        top = int(argv[argv.index("--top") + 1]) if "--top" in argv else 15
        r = cmd_coverage(top)
        folder = ROOT / "Plan" / "runs" / f"coverage-{r['at']}"
        folder.mkdir(parents=True, exist_ok=True)
        (folder / "coverage.json").write_text(json.dumps(r, ensure_ascii=False, indent=1, default=list) + "\n",
                                              encoding="utf-8")
        (folder / "README.md").write_text(render_coverage(r), encoding="utf-8")
        print(render_coverage(r))
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
