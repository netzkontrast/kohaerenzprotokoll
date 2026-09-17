"""One operation: give an account of a subject.

Eight scripts grew here, one per pipeline step, each with its own artifact format
and its own learnings file. Looked at from far enough back they are the same
operation with different arguments:

    census      a document   -> a structured account of it
    note        a document   -> a structured account of it
    reconcile   census+wiki  -> a structured account of the difference
    gather      readings     -> a structured account of a term
    corpus      term         -> a structured account
    judgement   two surfaces -> a structured account of whether they are one

All of them are `account(subject, question)`, and each decomposes into the same
operation on smaller subjects: a term across 315 documents is that term in each,
then the merge. That is the recursion -- not as an optimisation, as the shape.

A pipeline of N steps needs N rule sets, N formats and N learnings files, and
grows forever. One recursive operation needs one, and what grows instead is the
library of decompositions in `scripts/rules/` -- which is the part a project
actually learns.

    python3 scripts/account.py document <slug>
    python3 scripts/account.py term <term>
    python3 scripts/account.py pair <a> <b>
    python3 scripts/account.py corpus
    python3 scripts/account.py order            # does the pipeline order hold?

This is a facade, deliberately. It delegates to the scripts that already work
rather than replacing them: the claim that these are one operation is worth
making cheaply and withdrawing cheaply if it turns out to be wrong.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import subject  # noqa: E402
from wiki_index import build as build_index, fold  # noqa: E402


def account_document(slug: str) -> dict:
    """What is known about one document, from the derived cache -- nothing re-read."""
    doc = subject.document(slug)
    derived = subject.derived(slug)
    census = ROOT / "Sources" / "terms" / f"{slug}.md"
    note = ROOT / "Sources" / "notes" / f"{slug}.md"
    run = ROOT / "Plan" / "runs" / slug
    return {
        "subject": {"kind": "document", "id": slug},
        "facts": {
            "category": doc.category, "date": doc.date, "format": doc.format,
            "has_frontmatter": doc.has_frontmatter, "body_offset": doc.offset,
            **{k: v for k, v in subject.facts(slug, "structure").items() if k != "repeated_labels"},
            **subject.facts(slug, "export_damage"),
            "distinct_surfaces": len(subject.facts(slug, "surfaces").get("tokens", {})),
        },
        "derived_rules": sorted(derived),
        "accounts_written": {
            "census": census.exists(), "note": note.exists(),
            "run_artifacts": sorted(p.name for p in run.glob("*")) if run.exists() else [],
        },
        "decomposes_into": ["its candidate terms — `account.py term <term>`"],
    }


def account_term(term: str) -> dict:
    """What is known about one term: in the corpus, and in the wiki."""
    key = fold(term)
    index = build_index()
    page = index["surface_to_page"].get(key)

    docs, occurrences, first, last = 0, 0, None, None
    for row in subject.rows():
        if not row.get("export_path"):
            continue
        entry = subject.facts(row["slug"], "surfaces").get("tokens", {}).get(term)
        if not entry:
            continue
        docs += 1
        occurrences += entry["n"]
        date = row.get("index_date") or "?"
        first = date if first is None or date < first else first
        last = date if last is None or date > last else last

    judgements = [j for j in subject.judgements() if term in j.get("surfaces", [])]
    return {
        "subject": {"kind": "term", "id": term},
        "in_corpus": {"documents": docs, "occurrences": occurrences,
                      "first": first, "last": last,
                      "of_corpus_pct": round(docs / len(subject.documents()) * 100, 1)},
        "in_wiki": ({"page": page, **{k: v for k, v in index["terms"][page].items()
                                      if k in ("sources", "readings", "conflict", "ingested")}}
                    if page else None),
        "judgements": [{"id": j["id"], "decision": j["decision"], "rule": j["rule"]}
                       for j in judgements],
        "decomposes_into": [f"{docs} documents — `scripts/corpus.py plan {term}`"],
    }


def account_pair(first: str, second: str) -> dict:
    """Whether two surfaces are one term -- as far as code can say, and no further."""
    a, b = fold(first), fold(second)
    recorded = [
        j for j in subject.judgements()
        if {fold(s) for s in j.get("surfaces", [])} == {a, b}
    ]
    if a == b:
        verdict, why = "one-term", "the surfaces fold to the same key"
    elif a and b and (a in b or b in a):
        verdict, why = "needs-judgement", "one contains the other — a variant or a different term"
    else:
        verdict, why = "two-terms", "no relation the code can see"
    return {
        "subject": {"kind": "pair", "id": [first, second]},
        "folded": [a, b],
        "code_says": verdict,
        "why": why,
        "recorded": [{"id": j["id"], "decision": j["decision"], "rule": j["rule"],
                      "mechanised_by": j.get("mechanised_by")} for j in recorded],
        "decomposes_into": ["each surface — `account.py term <surface>`"],
    }


def account_order() -> dict:
    """Does the pipeline's dependency order hold, per document?

    The steps have an order — extract before reconcile, and each reconciliation
    against the state the previous one left. Nothing enforced it, and it broke:
    document 4 was first reconciled against 14 pages, the state document 1 left,
    while document 3 had already taken it to 24.

    Borrowed from the RLM-workflow skill's `validate_dag`, whose point is that the
    ordering is plain Python and must never be left to judgement: it will be wrong
    on the day it matters. Here the order is checked rather than assumed.
    """
    runs = ROOT / "Plan" / "runs"
    rows, violations = [], []
    for census in sorted((ROOT / "Sources" / "terms").glob("*.md")):
        slug = census.stem
        note = (ROOT / "Sources" / "notes" / f"{slug}.md").exists()
        record = runs / slug / "reconcile.json"
        state = None
        if record.exists():
            state = json.loads(record.read_text(encoding="utf-8")).get("state_before")
        rows.append({"document": slug, "census": True, "note": note,
                     "reconciled": record.exists(), "state_before": state})
        if not record.exists():
            violations.append({"document": slug, "kind": "not-reconciled",
                               "detail": "has a census, has not been reconciled against the wiki"})

    done = [r for r in rows if r["state_before"]]
    done.sort(key=lambda r: r["state_before"]["pages"])
    seen = -1
    for row in done:
        pages = row["state_before"]["pages"]
        if pages <= seen:
            violations.append({"document": row["document"], "kind": "stale-state",
                               "detail": f"reconciled against {pages} pages, but an earlier "
                                         f"reconciliation had already reached {seen}"})
        seen = max(seen, pages)

    # The wiki is always larger than the state the newest reconciliation *started*
    # from -- that reconciliation is what grew it. Comparing against state_before
    # therefore reports a violation after every successful run, which is a check
    # that is always red and so teaches nothing. What must match is the state the
    # run *left*, when the record says.
    index = build_index()
    if done:
        last = max(done, key=lambda r: r["state_before"]["pages"])
        record = runs / last["document"] / "reconcile.json"
        after = json.loads(record.read_text(encoding="utf-8")).get("state_after")
        if after is None:
            violations.append({
                "document": last["document"], "kind": "no-state-after",
                "detail": "the newest reconciliation does not record the state it left, "
                          "so nothing can check whether the wiki has moved since.",
            })
        elif after["pages"] != index["pages"]:
            violations.append({
                "document": "(wiki)", "kind": "state-moved-since",
                "detail": f"the wiki holds {index['pages']} pages; the newest reconciliation "
                          f"({last['document']}) left it at {after['pages']}. Pages changed "
                          f"outside a reconciliation, or one was not recorded.",
            })

    return {
        "subject": {"kind": "order", "id": "pipeline"},
        "documents": rows,
        "violations": violations,
        "holds": not violations,
    }


def account_corpus() -> dict:
    docs = subject.documents()
    index = build_index()
    judged = subject.judgements()
    return {
        "subject": {"kind": "corpus", "id": "Sources/"},
        "documents": len(docs),
        "without_frontmatter": sum(1 for d in docs if not d.has_frontmatter),
        "with_census": len(list((ROOT / "Sources" / "terms").glob("*.md"))),
        "with_note": len(list((ROOT / "Sources" / "notes").glob("*.md"))),
        "wiki": {"pages": index["pages"], "conflicts": index["conflicts"],
                 "known_surfaces": len(index["surface_to_page"])},
        "judgements": {"total": len(judged),
                       "mechanised": sum(1 for j in judged if j.get("mechanised_by"))},
        "decomposes_into": ["each document — `account.py document <slug>`"],
    }


def main(argv: list[str]) -> int:
    if not argv:
        sys.exit(__doc__)
    kind, args = argv[0], argv[1:]
    handlers = {
        "document": lambda: account_document(args[0]),
        "term": lambda: account_term(args[0]),
        "pair": lambda: account_pair(args[0], args[1]),
        "corpus": account_corpus,
        "order": account_order,
    }
    if kind not in handlers:
        sys.exit(f"unknown subject kind {kind!r} — one of {', '.join(handlers)}")
    print(json.dumps(handlers[kind](), indent=2, ensure_ascii=False))
    return 0


if __name__ == "__main__":
    try:
        import signal

        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (ImportError, AttributeError, ValueError):
        pass
    raise SystemExit(main(sys.argv[1:]))
