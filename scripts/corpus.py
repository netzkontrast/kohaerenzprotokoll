"""Ask questions about every landed document without reading any of them.

The wiki has been built from four documents, 1% of the corpus. The two sharpest
corrections of that work came from querying the whole corpus -- the renaming turned out to
be a cliff on one day rather than a drift, and `Partnerin` turned out to be linked
to `Juna`/`Julia` in 17 documents after four had suggested it never was.

Both were one-off heredocs. Neither was a step, and neither survived.

This is the same idea as scripts/reconcile.py applied to the layer that actually
has scale: the corpus is a variable, questions are code, and **what comes back is
counts and slugs, never document text.** A reader can learn something about 2.46
million words without a single one of them entering a context.

Usage:
    python3 scripts/corpus.py count <term> [<term> ...]
    python3 scripts/corpus.py timeline <term>            # occurrences by index_date
    python3 scripts/corpus.py cooccur <a> <b>            # both / only-a / only-b
    python3 scripts/corpus.py first <term>               # earliest documents
    python3 scripts/corpus.py where <term> [--limit N]   # which documents, with counts
    python3 scripts/corpus.py family <head>              # the surfaces one term wears
    python3 scripts/corpus.py plan <term>                # sub-call batches for reading it everywhere

Matching is whole-word. `--substring` switches it, and every answer says which
it used. Add --json for the machine-readable form.
"""

from __future__ import annotations

import json
import re
import sys
from collections import Counter, defaultdict
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
import subject  # noqa: E402


def indexed() -> list[dict]:
    """Every document as its derived surface index -- no document is opened.

    scripts/derive.py has already applied the `surfaces` rule to every document and
    cached the result against each document's checksum. A term question is then a
    dict lookup per document rather than a scan of 2.46 million words, and it
    stays that way no matter how many questions get asked.
    """
    docs = []
    for row in subject.rows():
        if not row.get("export_path"):
            continue
        entry = subject.facts(row["slug"], "surfaces")
        if not entry:
            continue
        docs.append({"slug": row["slug"], "category": row.get("category", "?"),
                     "date": row.get("index_date") or "?", "tokens": entry["tokens"]})
    return docs


def landed() -> list[dict]:
    """Every document with its body, from the one place that finds the boundary.

    The slow path, used only when a question cannot be answered from the derived
    index -- a lowercase word, or a phrase. `main` says when it fell back here.
    """
    return [
        {"slug": d.slug, "category": d.category, "date": d.date,
         "body": d.body, "offset": d.offset, "has_frontmatter": d.has_frontmatter}
        for d in subject.documents()
    ]


WHOLE_WORD = True


def matcher(term: str) -> re.Pattern:
    """Whole-word by default, because a substring count is a different question.

    Measured on this corpus: `Julia` matches 33 documents as a substring and 26
    as a word -- seven of them are Julian or Julias. `Michael` differs by two.
    A count that does not say which it is cannot be compared to another count,
    and both numbers get quoted as if they were the same fact.
    """
    escaped = re.escape(term)
    if not WHOLE_WORD:
        return re.compile(escaped)
    # `\bterm\b`, its first boundary asked after the literal rather than before
    # it: the same spans, and the engine searches for the literal instead of
    # trying the boundary at every position. `count kohärent`, which reads every
    # document, went from 0.58 seconds to 0.23.
    first = rf"(?<!\w{escaped})" if re.match(r"\w", term) else rf"(?<=\w{escaped})"
    return re.compile(rf"{escaped}{first}\b")


def from_index(docs: list[dict], term: str) -> list[dict]:
    """Documents whose surface index carries this exact token."""
    hits = []
    for doc in docs:
        entry = doc["tokens"].get(term)
        if entry:
            hits.append({"slug": doc["slug"], "date": doc["date"], "category": doc["category"],
                         "n": entry["n"], "first_line": entry["lines"][0] if entry["lines"] else None})
    return sorted(hits, key=lambda h: (h["date"], h["slug"]))


def occurrences(docs: list[dict], term: str) -> list[dict]:
    """Documents containing the term, with count and first file line."""
    if docs and "tokens" in docs[0]:
        return from_index(docs, term)
    pattern = matcher(term)
    hits = []
    for doc in docs:
        found = pattern.findall(doc["body"])
        if not found:
            continue
        line = next(
            (i + doc["offset"] for i, l in enumerate(doc["body"].split("\n")) if pattern.search(l)),
            None,
        )
        hits.append({"slug": doc["slug"], "date": doc["date"],
                     "category": doc["category"], "n": len(found), "first_line": line})
    return sorted(hits, key=lambda h: (h["date"], h["slug"]))


def cmd_count(docs: list[dict], terms: list[str]) -> dict:
    out = {}
    for term in terms:
        hits = occurrences(docs, term)
        out[term] = {
            "documents": len(hits),
            "occurrences": sum(h["n"] for h in hits),
            "first": hits[0]["date"] if hits else None,
            "last": hits[-1]["date"] if hits else None,
            "categories": dict(Counter(h["category"] for h in hits).most_common()),
        }
    return out


def cmd_timeline(docs: list[dict], term: str) -> dict:
    hits = occurrences(docs, term)
    by_date: dict[str, dict] = defaultdict(lambda: {"documents": 0, "occurrences": 0})
    for hit in hits:
        by_date[hit["date"]]["documents"] += 1
        by_date[hit["date"]]["occurrences"] += hit["n"]
    return {"term": term, "by_date": dict(sorted(by_date.items()))}


def cmd_cooccur(docs: list[dict], first: str, second: str) -> dict:
    a = {h["slug"] for h in occurrences(docs, first)}
    b = {h["slug"] for h in occurrences(docs, second)}
    return {
        "a": first, "b": second,
        "both": len(a & b), "only_a": len(a - b), "only_b": len(b - a),
        "neither": len(docs) - len(a | b),
        "both_slugs": sorted(a & b)[:20],
    }


def cmd_first(docs: list[dict], term: str, limit: int = 5) -> dict:
    return {"term": term, "earliest": occurrences(docs, term)[:limit]}


def cmd_family(docs: list[dict], head: str, limit: int = 30) -> dict:
    """Every indexed token beginning with this head, with its corpus-wide count.

    The index counts a compound as one token, so `Kael` and `Kael-Julia-Bindung`
    are separate rows. This command is how that stops being a discrepancy and
    becomes the answer: the surfaces a term actually wears across the corpus.
    """
    if not docs or "tokens" not in docs[0]:
        return {"head": head, "error": "needs the derived index — run scripts/derive.py"}
    total: dict[str, int] = {}
    seen: dict[str, int] = {}
    for doc in docs:
        for token, entry in doc["tokens"].items():
            if token == head or token.startswith(head + "-") or (
                token.startswith(head) and len(token) <= len(head) + 3
            ):
                total[token] = total.get(token, 0) + entry["n"]
                seen[token] = seen.get(token, 0) + 1
    rows = sorted(total.items(), key=lambda kv: -kv[1])[:limit]
    return {"head": head, "surfaces": len(total),
            "rows": [{"token": t, "occurrences": n, "documents": seen[t]} for t, n in rows]}


def cmd_plan(docs: list[dict], term: str, budget: int = 400_000) -> dict:
    """A chunking plan for asking a sub-model about every document carrying a term.

    The RLM strategy, computed rather than improvised: which documents contain the
    term, grouped into batches that fit a sub-call's context, with the character
    cost of each batch. Nothing is read here -- the sizes come from the manifest
    and the document list from the surface index.

    The output is what a `llm_query_batched` call would be given, so the expensive
    half can be wired later without re-deriving the cheap half.
    """
    hits = occurrences(docs, term)
    sizes = {d.slug: d.path.stat().st_size for d in subject.documents()}

    batches: list[dict] = []
    current: list[str] = []
    used = 0
    for hit in sorted(hits, key=lambda h: -h["n"]):
        size = sizes.get(hit["slug"], 0)
        if current and used + size > budget:
            batches.append({"documents": current, "chars": used})
            current, used = [], 0
        current.append(hit["slug"])
        used += size
    if current:
        batches.append({"documents": current, "chars": used})

    return {
        "term": term,
        "documents": len(hits),
        "total_chars": sum(sizes.get(h["slug"], 0) for h in hits),
        "budget_per_call": budget,
        "sub_calls": len(batches),
        "batches": [{"n": len(b["documents"]), "chars": b["chars"],
                     "documents": b["documents"][:6] + (["…"] if len(b["documents"]) > 6 else [])}
                    for b in batches],
    }


def cmd_where(docs: list[dict], term: str, limit: int = 25) -> dict:
    hits = occurrences(docs, term)
    ranked = sorted(hits, key=lambda h: -h["n"])[:limit]
    return {"term": term, "documents": len(hits), "top": ranked}


def render(command: str, result: dict) -> str:
    if command == "count":
        rows = [f"{'term':28} {'docs':>5} {'occ':>7}  {'first':10} {'last':10}  categories"]
        for term, data in result.items():
            cats = ", ".join(f"{k}:{v}" for k, v in list(data["categories"].items())[:4])
            rows.append(f"{term:28} {data['documents']:5} {data['occurrences']:7}  "
                        f"{str(data['first']):10} {str(data['last']):10}  {cats}")
        return "\n".join(rows)
    if command == "timeline":
        rows = [f"{result['term']} — by index_date", f"{'date':12} {'docs':>5} {'occ':>7}"]
        rows += [f"{d:12} {v['documents']:5} {v['occurrences']:7}" for d, v in result["by_date"].items()]
        return "\n".join(rows)
    if command == "cooccur":
        return "\n".join([
            f"{result['a']!r} against {result['b']!r}",
            f"  both     {result['both']:4}",
            f"  only {result['a'][:12]:12} {result['only_a']:4}",
            f"  only {result['b'][:12]:12} {result['only_b']:4}",
            f"  neither  {result['neither']:4}",
            "  documents carrying both: " + ", ".join(result["both_slugs"][:6]),
        ])
    if command == "plan":
        rows = [f"{result['term']} — {result['documents']} documents, "
                f"{result['total_chars']:,} chars",
                f"{result['sub_calls']} sub-calls at {result['budget_per_call']:,} chars each",
                "", f"{'call':>5} {'docs':>5} {'chars':>10}  first documents"]
        for i, b in enumerate(result["batches"], 1):
            rows.append(f"{i:5} {b['n']:5} {b['chars']:10,}  {', '.join(b['documents'][:3])}")
        return "\n".join(rows)
    if command == "family":
        if "error" in result:
            return result["error"]
        rows = [f"{result['head']} — {result['surfaces']} surfaces in the corpus",
                f"{'token':36} {'occ':>7} {'docs':>6}"]
        rows += [f"{r['token']:36} {r['occurrences']:7} {r['documents']:6}" for r in result["rows"]]
        return "\n".join(rows)
    if command in ("first", "where"):
        key = "earliest" if command == "first" else "top"
        rows = [f"{result['term']} — {result.get('documents', len(result[key]))} documents",
                f"{'date':12} {'n':>5}  {'category':20} slug"]
        rows += [f"{h['date']:12} {h['n']:5}  {h['category']:20} {h['slug'][:44]}" for h in result[key]]
        return "\n".join(rows)
    return json.dumps(result, indent=2, ensure_ascii=False)


INDEXABLE = re.compile(r"^[A-ZÄÖÜ][A-Za-zäöüß]{2,}(?:-[A-ZÄÖÜa-zäöüß][A-Za-zäöüß]+)*$")


def docs_for(terms: list[str], read: bool = False) -> tuple[list[dict], bool]:
    """(the documents to ask, whether they are the derived index) for these terms.

    The surface index holds capitalised tokens only. Anything else -- a
    lowercase word, a phrase -- is not in it, and reading is the honest answer
    rather than a confidently empty one. `account.py term` asks here too.
    """
    use_index = (
        WHOLE_WORD
        and not read
        and bool(terms)
        and all(INDEXABLE.match(t) for t in terms)
        and subject.DERIVED.exists()
    )
    docs = indexed() if use_index else landed()
    if use_index and not docs:
        return landed(), False
    return docs, use_index


def main(argv: list[str]) -> int:
    if not argv:
        sys.exit(__doc__)
    global WHOLE_WORD
    as_json = "--json" in argv
    WHOLE_WORD = "--substring" not in argv
    read = "--read" in argv
    argv = [a for a in argv if a not in ("--json", "--substring", "--read")]
    limit = 25
    if "--limit" in argv:
        i = argv.index("--limit")
        limit = int(argv[i + 1])
        argv = argv[:i] + argv[i + 2:]

    command, args = argv[0], argv[1:]
    terms = [a for a in args if not a.startswith("-")]
    docs, use_index = docs_for(terms, read)
    handlers = {
        "count": lambda: cmd_count(docs, args),
        "timeline": lambda: cmd_timeline(docs, args[0]),
        "cooccur": lambda: cmd_cooccur(docs, args[0], args[1]),
        "first": lambda: cmd_first(docs, args[0], limit),
        "where": lambda: cmd_where(docs, args[0], limit),
        "family": lambda: cmd_family(docs, args[0], limit),
        "plan": lambda: cmd_plan(docs, args[0]),
    }
    if command not in handlers:
        sys.exit(f"unknown command {command!r} -- one of {', '.join(handlers)}")
    result = handlers[command]()
    bare = sum(1 for d in docs if not d.get("has_frontmatter", True))
    mode = "whole-word" if WHOLE_WORD else "substring"
    if as_json:
        # Wrapped rather than merged: `count` returns one entry per term, and a
        # `matching` key beside them would be read as a term.
        print(json.dumps({"matching": mode, "documents": len(docs),
                          "without_frontmatter": bare, "result": result},
                         indent=2, ensure_ascii=False))
    else:
        print(render(command, result))
        print(f"\nmatching: {mode}  ({'--substring' if WHOLE_WORD else 'default'} for the other)")
        if use_index:
            print(f"{len(docs)} documents, answered from the derived surface index "
                  f"— no document was opened")
        else:
            print(f"{len(docs)} documents read, {bare} of them without frontmatter. "
                  f"Not answerable from the index: the term is not a capitalised token, "
                  f"or --read/--substring was given.")
    return 0


if __name__ == "__main__":
    subject.cli(main)
