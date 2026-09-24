"""The repository's state, measured rather than remembered.

Every number about this project has been written down in prose at least once and
has gone stale at least once. In one session `CLAUDE.md` claimed 27 of 680
documents landed, then 3 read and 2 censuses, then 32 wiki pages and 11
judgements and a reconciliation of 19/12/7 — each true when written and none of
them true afterwards. The rule „a statement that is not true of the repository is
the defect" caught them, one at a time, by hand.

**So state is not stored here. It is derived.** Each measurement is a small named
function that reads the repository and returns a value with a note on how it got
it. `Plan/state.json` is the artifact of a run, never the source of truth, and
`--check` re-derives everything and fails if the artifact has drifted.

## Extending it

Add a function and decorate it. Nothing else:

    @measure("wiki.pages", "pages in Wiki/candidates, from the derived index")
    def _wiki_pages() -> int:
        return json.loads(INDEX.read_text())["pages"]

The key is dotted and the group before the first dot is how it prints. A tool
that needs a number asks `value("wiki.pages")` instead of hardcoding one.

## Prose stays readable and stays checked

A sentence that states a number marks the measurement it came from:

    `Wiki/candidates/` holds **46 pages** <!--state:wiki.pages-->

`--prose` finds every marker, reads the number written immediately before it, and
compares. That turns „CLAUDE.md is out of date" from something a person notices
into something a command reports. The prose keeps saying what it means; the
number just stops being able to lie.

Usage:
    python3 scripts/state.py               # derive, write Plan/state.json, print
    python3 scripts/state.py --check       # re-derive; non-zero if the file drifted
    python3 scripts/state.py --prose       # verify the numbers written in prose
    python3 scripts/state.py --get wiki.pages
"""

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from datetime import date
from functools import cache
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
STATE = ROOT / "Plan" / "state.json"
INDEX = ROOT / "Wiki" / "index.json"
sys.path.insert(0, str(ROOT / "scripts"))

_REGISTRY: dict[str, tuple[str, callable]] = {}


def measure(key: str, how: str):
    """Register a measurement. The docstring of `how` is what the output cites."""
    def register(fn):
        _REGISTRY[key] = (how, fn)
        return fn
    return register


# ---------------------------------------------------------------- sources

# Several measurements share one expensive reading. Each such reading is cached
# for the run, so a derive computes it once rather than once per measurement —
# three identical graphrag benches were most of a derive's seven seconds.

@cache
def _manifest_rows() -> list[dict]:
    import subject
    return subject.rows()


@measure("sources.total", "rows in Sources/manifest.jsonl")
def _sources_total() -> int:
    return len(_manifest_rows())


@measure("sources.canon_era", "manifest rows with an index_date from 2026-05-01 on — the canon-era documents")
def _canon_era() -> int:
    return sum(1 for r in _manifest_rows() if (r.get("index_date") or "") >= "2026-05-01")


@measure("sources.canon_era_landed", "of those, rows landed in Sources/drive/")
def _canon_era_landed() -> int:
    return sum(1 for r in _manifest_rows() if (r.get("index_date") or "") >= "2026-05-01"
               and r.get("export_path"))


@measure("sources.folded", "rows in Sources/duplicates.jsonl — fetched, then found to be a copy")
def _sources_folded() -> int:
    import subject
    return len(subject.duplicates())


@measure("sources.landed", "manifest rows carrying an export_path — the files on disk")
def _sources_landed() -> int:
    return sum(1 for r in _manifest_rows() if r.get("export_path"))


@measure("sources.distinct", "landed files minus near-copies, scripts/duplicates.py at 0.8")
def _sources_distinct() -> int:
    from duplicates import groups
    return _sources_landed() - sum(len(g) - 1 for g in groups(0.8))


@measure("sources.near_copies", "landed files that are a near-copy of another")
def _sources_near_copies() -> int:
    from duplicates import groups
    return sum(len(g) - 1 for g in groups(0.8))


# ---------------------------------------------------------------- documents

@measure("documents.with_census", "files in Sources/terms/")
def _with_census() -> int:
    return len(list((ROOT / "Sources" / "terms").glob("*.md")))


@measure("documents.with_note", "files in Sources/notes/")
def _with_note() -> int:
    return len(list((ROOT / "Sources" / "notes").glob("*.md")))


@measure("documents.reconciled", "run directories holding a reconcile.json")
def _reconciled() -> int:
    return len(list((ROOT / "Plan" / "runs").glob("*/reconcile.json")))


# ---------------------------------------------------------------- entities

@cache
def _entity_lists() -> list[dict]:
    import entities
    return [entities.verify(e) for e in entities.lists()]


@measure("entities.lists", "model entity lists in Plan/entities/, one per document")
def _e_lists() -> int:
    return len(_entity_lists())


@measure("entities.readings", "entity lists whose cited lines hold 90%+ of their rows")
def _e_readings() -> int:
    return sum(e["reading"] for e in _entity_lists())


@measure("entities.rows", "rows across all entity lists, cited or not")
def _e_rows() -> int:
    return sum(e["total"] for e in _entity_lists())


@measure("entities.rows_verified", "entity rows whose cited file line contains the entity")
def _e_rows_verified() -> int:
    return sum(e["verified"] for e in _entity_lists())


# ---------------------------------------------------------------- wiki

@cache
def _index() -> dict:
    """The index as it stands on disk — measured, not rebuilt."""
    return json.loads(INDEX.read_text(encoding="utf-8"))


@measure("wiki.pages", "pages counted by the derived Wiki/index.json")
def _wiki_pages() -> int:
    return _index()["pages"]


@measure("wiki.conflicts", "conflict records counted by the derived Wiki/index.json")
def _wiki_conflicts() -> int:
    return _index()["conflicts"]


@measure("wiki.questions", "question pages in Wiki/questions/, excluding the README")
def _wiki_questions() -> int:
    return len([p for p in (ROOT / "Wiki" / "questions").glob("*.md")
                if p.stem != "README"])


@measure("wiki.relations", "a page naming another page as `slug`, scripts/relations.py")
def _wiki_relations() -> int:
    from relations import graph
    return len(graph()["edges"])


@measure("wiki.orphans", "pages nothing links to — the relation layer's gap")
def _wiki_orphans() -> int:
    from relations import graph
    return len(graph()["orphans"])


@measure("wiki.unmarked",
         "a page's term written in another page's prose without being marked a link")
def _wiki_unmarked() -> int:
    from relations import unmarked
    return len(unmarked())


@measure("wiki.open_statements", "statements under an Open heading, the question harvest")
def _wiki_open() -> int:
    from relations import open_questions
    return len(open_questions())


# ---------------------------------------------------------------- graph and retrieval

@measure("graph.nodes", "nodes in scripts/graph.py's typed graph — terms, documents, conflicts, questions")
def _graph_nodes() -> int:
    from graph import build
    return len(build()["nodes"])


@measure("graph.edges", "typed edges in scripts/graph.py, each carrying the file line that states it")
def _graph_edges() -> int:
    from graph import build
    return len(build()["edges"])


@measure("graph.evidence", "quotations on term pages, the unit scripts/graphrag.py serves")
def _graph_evidence() -> int:
    from graph import build
    return sum(len(v) for v in build()["evidence"].values())


@measure("graph.evidence_verified", "of those, verified against their line by quotes.verdict")
def _graph_evidence_verified() -> int:
    from graph import build
    return sum(1 for v in build()["evidence"].values() for e in v if e["status"] == "verified")


@cache
def _bench() -> dict:
    from graphrag import bench
    out = {}
    for method, rows in bench().items():
        scored = [r["recall"] for r in rows if r["recall"] is not None]
        out[method] = (round(sum(scored) / len(scored), 3) if scored else None, len(rows))
    return out


@measure("graphrag.cases", "retrieval cases the wiki labels itself: questions and conflicts")
def _graphrag_cases() -> int:
    return _bench()["ppr"][1]


@measure("graphrag.recall_seeds", "graphrag bench mean recall@8 in whole percent, seeds alone — the floor")
def _graphrag_recall_seeds() -> int:
    return round(100 * _bench()["seeds"][0])


@measure("graphrag.recall_ppr", "graphrag bench mean recall@8 in whole percent, personalized PageRank")
def _graphrag_recall_ppr() -> int:
    return round(100 * _bench()["ppr"][0])


@measure("proposals.entities", "entities from entity lists that verify as readings, graph.proposals()")
def _prop_entities() -> int:
    from graph import proposals
    return len(proposals()["nodes"])


@measure("proposals.entities_paged", "of those, entities whose fold is a wiki page surface")
def _prop_paged() -> int:
    from graph import proposals
    return len({e["source"] for e in proposals()["edges"] if e["type"] == "folds_to"})


@measure("proposals.glosses", "stated `A (B)` glosses in 2+ documents routing to exactly one page")
def _prop_glosses() -> int:
    from graph import proposals
    return len(proposals()["glosses"])


@cache
def _surface_pairs() -> list[dict]:
    from trainset import surface_pairs
    return surface_pairs()


@cache
def _fold_baseline() -> dict:
    from trainset import fold_baseline
    return fold_baseline(_surface_pairs())


@measure("pairs.labelled", "labelled one-term-or-two pairs derived from the judgement ledger")
def _pairs_labelled() -> int:
    return len(_surface_pairs())


@measure("pairs.fold_correct", "of those, decided correctly by fold() — the floor")
def _pairs_fold_correct() -> int:
    return _fold_baseline()["correct"]


# ---------------------------------------------------------------- checks

@cache
def _verdicts() -> list[str]:
    """One replay of the whole ledger, shared by the three measurements."""
    from judgements import replay, records
    return [replay(r)[0] for r in records()]


@measure("judgements.total", "records in Plan/runs/judgements.jsonl")
def _j_total() -> int:
    return len(_verdicts())


@measure("judgements.mechanised", "judgements a rule now claims and still agrees with")
def _j_mech() -> int:
    return sum(1 for v in _verdicts() if v == "agrees")


@measure("judgements.disagree", "judgements where code now contradicts the record")
def _j_dis() -> int:
    return sum(1 for v in _verdicts() if v == "DISAGREES")


@measure("quotes.unresolved", "cited quotations that do not resolve, scripts/quotes.py")
def _q_unresolved() -> int:
    return _quotes()["unresolved"]


@measure("quotes.checked", "cited quotations verified against their line")
def _q_checked() -> int:
    return _quotes()["checked"]


@measure("quotes.unchecked", "quotations with no citation on their own line")
def _q_unchecked() -> int:
    return _quotes()["unchecked"]


@measure("order.holds", "scripts/account.py order — the pipeline's dependency order")
def _order() -> bool:
    from account import account_order
    return account_order()["holds"]


@measure("rules.count", "modules in scripts/rules/ satisfying the contract")
def _rules() -> int:
    from rules import load
    return len(load())


@cache
def _quotes() -> dict:
    """One quotes.py tally, reused by the three measurements that need it."""
    from quotes import tally
    return tally()


# ---------------------------------------------------------------- trainsets

@measure("trainset.surface_pairs", "labelled one-term/two-terms examples in the ledger")
def _ts_pairs() -> int:
    return len(_surface_pairs())


@measure("trainset.fold_baseline_pct", "what fold() scores on them — beat this or do not call an LM")
def _ts_base() -> int:
    return round(_fold_baseline()["accuracy"] * 100)


@measure("trainset.gold_candidate_lists", "candidate lists written while reading, not reconstructed")
def _ts_gold() -> int:
    """A list says who wrote it. Absent that, the old substring test decides.

    The test used to be „does the first 300 characters contain 'reconstruct'",
    which is a claim about wording rather than about provenance: a list whose
    prose *denies* being a reconstruction matches it, and a model's list that
    never says the word passes as gold. The four lists from documents 1-4 predate
    the marker and still fall back to the substring, because for them the
    substring is what the file actually says.
    """
    runs = ROOT / "Plan" / "runs"
    gold = 0
    for path in runs.glob("*/03-candidates.md"):
        head = path.read_text(encoding="utf-8")[:300]
        written_by = re.search(r"^written_by:\s*(.+)$", head, re.M)
        if written_by:
            gold += "reader" in written_by.group(1).lower()
        elif "reconstruct" not in head.lower():
            gold += 1
    return gold


# ---------------------------------------------------------------- driver

def derive() -> dict:
    measurements = {}
    for key, (how, fn) in sorted(_REGISTRY.items()):
        measurements[key] = {"value": fn(), "how": how}
    return {"generated": date.today().isoformat(), "by": "scripts/state.py",
            "measurements": measurements}


def value(key: str):
    """The current value of one measurement, derived now. For other tools."""
    if key not in _REGISTRY:
        raise KeyError(f"no measurement named {key!r}; have: {', '.join(sorted(_REGISTRY))}")
    return _REGISTRY[key][1]()


# The number may sit on the line above its marker -- prose wraps, and a marker is
# written where the sentence needs it. `[^\n\d]` here meant a wrapped number left
# its marker matching nothing, so the marker was **not checked and looked
# checked**: 8 of 49 markers in this repository were in that state, including
# `order.holds`. A guard that silently covers less than it claims is the same
# defect as the retired pipeline's coverage term.
MARKER = re.compile(r"(?P<number>[\d,]+|true|false|True|False)\**[^\d]{0,40}?<!--\s*state:(?P<key>[a-z_.]+)\s*-->")
ANY_MARKER = re.compile(r"<!--\s*state:([a-z_.]+)\s*-->")
IN_CODE = re.compile(r"`[^`\n]*`")


SKIP = {"Legacy", ".qmd", ".tools-node", ".git", "worktrees", "node_modules"}


def marked_files() -> list[Path]:
    """Every markdown file that could carry a marker, not a list of three.

    This used to be `[CLAUDE.md, NOW.md, PRINCIPLES.md]`, and the blind spot
    behaved exactly like an uncovered qmd collection: `Plan/concept/plan_*.md`
    carried three `<!--state:-->` markers, went stale when the corpus was
    deduplicated, and the check stayed green — because it never looked. A guard
    with a hardcoded file list fails silently the first time someone writes a
    marker somewhere new, which is the one moment it was built for.

    Venvs are skipped by prefix, as `qmd_coverage.py` does. A list of their names
    went stale the same way: it missed `.venv-typesafe`, and it read 96
    markdown files from inside `.venv-mflow`, the day that venv was created.
    A skipped directory is not entered at all: filtering after the walk meant
    reading every directory of every venv first, thousands for `.venv-dspy`.
    """
    def skipped(name: str) -> bool:
        return name in SKIP or name.startswith(".venv")

    found = []
    for folder, dirs, files in os.walk(ROOT):
        dirs[:] = [d for d in dirs if not skipped(d)]
        found += [Path(folder) / f for f in files if f.endswith(".md") and not skipped(f)]
    return sorted(found)


def check_prose(paths: list[Path]) -> list[dict]:
    """Every <!--state:key--> marker, against the number written before it."""
    current = {k: fn() for k, (_, fn) in _REGISTRY.items()}
    problems = []
    for path in paths:
        if not path.exists():
            continue
        text = path.read_text(encoding="utf-8")
        if "state:" not in text:
            continue    # both patterns need the literal; most files have none
        # A marker nothing could read is reported rather than skipped. One inside
        # backticks is prose *about* markers -- this page explains its own format --
        # and is not a claim in either direction, so both loops step over it. The
        # relaxed number pattern would otherwise bind `<!--state:key-->` to whatever
        # digit happened to stand a line above it.
        code = [(m.start(), m.end()) for m in IN_CODE.finditer(text)]
        markers = list(MARKER.finditer(text))
        readable = {m.start("key") for m in markers}
        for stray in ANY_MARKER.finditer(text):
            if stray.start(1) in readable:
                continue
            if any(a <= stray.start() < b for a, b in code):
                continue
            problems.append({"file": path, "key": stray.group(1),
                             "why": "no number this check can read stands before it"})
        for match in markers:
            if any(a <= match.start("key") < b for a, b in code):
                continue    # documentation of the format, not a claim
            key = match.group("key")
            if key not in current:
                problems.append({"file": path, "key": key, "why": "no such measurement"})
                continue
            written = match.group("number").replace(",", "")
            actual = current[key]
            same = (written.lower() == str(actual).lower()
                    if isinstance(actual, bool) else written == str(actual))
            if not same:
                problems.append({"file": path, "key": key,
                                 "why": f"prose says {written}, measured {actual}"})
    return problems


def main() -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="fail if Plan/state.json drifted")
    parser.add_argument("--prose", action="store_true", help="verify numbers written in prose")
    parser.add_argument("--get", help="print one measurement and exit")
    args = parser.parse_args()

    if args.get:
        print(value(args.get))
        return 0

    if args.prose:
        problems = check_prose(marked_files())
        for p in problems:
            print(f"STALE  {p['file'].relative_to(ROOT)}  {p['key']}: {p['why']}")
        print(f"\n{len(problems)} prose claims contradict the repository.")
        return 1 if problems else 0

    fresh = derive()
    if args.check:
        if not STATE.exists():
            print("Plan/state.json does not exist — run without --check to write it.")
            return 1
        stored = json.loads(STATE.read_text(encoding="utf-8"))["measurements"]
        drift = [k for k, v in fresh["measurements"].items()
                 if stored.get(k, {}).get("value") != v["value"]]
        for key in drift:
            print(f"DRIFTED  {key}: file says {stored.get(key, {}).get('value')!r}, "
                  f"measured {fresh['measurements'][key]['value']!r}")
        print(f"\n{len(drift)} of {len(fresh['measurements'])} measurements drifted.")
        return 1 if drift else 0

    STATE.write_text(json.dumps(fresh, indent=2) + "\n", encoding="utf-8")
    group = None
    for key, entry in fresh["measurements"].items():
        head = key.split(".")[0]
        if head != group:
            print(f"\n{head}")
            group = head
        print(f"  {key:26} {str(entry['value']):>8}   {entry['how']}")
    print(f"\nwritten to {STATE.relative_to(ROOT)} — --check re-derives and compares")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
