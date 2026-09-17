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
import re
import subprocess
import sys
from datetime import date
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

@measure("sources.total", "rows in Sources/manifest.jsonl")
def _sources_total() -> int:
    return sum(1 for line in (ROOT / "Sources" / "manifest.jsonl").read_text(
        encoding="utf-8").splitlines() if line.strip())


def _manifest_rows():
    return [json.loads(line) for line in (ROOT / "Sources" / "manifest.jsonl").read_text(
        encoding="utf-8").splitlines() if line.strip()]


@measure("sources.folded", "rows in Sources/duplicates.jsonl — fetched, then found to be a copy")
def _sources_folded() -> int:
    path = ROOT / "Sources" / "duplicates.jsonl"
    if not path.exists():
        return 0
    return sum(1 for line in path.read_text(encoding="utf-8").splitlines() if line.strip())


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


# ---------------------------------------------------------------- wiki

@measure("wiki.pages", "pages counted by the derived Wiki/index.json")
def _wiki_pages() -> int:
    return json.loads(INDEX.read_text(encoding="utf-8"))["pages"]


@measure("wiki.conflicts", "conflict records counted by the derived Wiki/index.json")
def _wiki_conflicts() -> int:
    return json.loads(INDEX.read_text(encoding="utf-8"))["conflicts"]


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


# ---------------------------------------------------------------- checks

def _verdicts() -> list[str]:
    """One replay of the whole ledger, shared by the three measurements."""
    if not hasattr(_verdicts, "cached"):
        from judgements import replay, records
        _verdicts.cached = [replay(r)[0] for r in records()]
    return _verdicts.cached


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


def _quotes() -> dict:
    """One quotes.py run, reused by the three measurements that need it."""
    if not hasattr(_quotes, "cached"):
        out = subprocess.run([sys.executable, str(ROOT / "scripts" / "quotes.py")],
                             capture_output=True, text=True, cwd=ROOT).stdout
        found = re.search(r"(\d+) cited quotes checked, (\d+) unresolved; (\d+)", out)
        _quotes.cached = {"checked": int(found.group(1)), "unresolved": int(found.group(2)),
                          "unchecked": int(found.group(3))} if found else \
                         {"checked": 0, "unresolved": 0, "unchecked": 0}
    return _quotes.cached


# ---------------------------------------------------------------- trainsets

@measure("trainset.surface_pairs", "labelled one-term/two-terms examples in the ledger")
def _ts_pairs() -> int:
    from trainset import surface_pairs
    return len(surface_pairs())


@measure("trainset.fold_baseline_pct", "what fold() scores on them — beat this or do not call an LM")
def _ts_base() -> int:
    from trainset import surface_pairs, fold_baseline
    return round(fold_baseline(surface_pairs())["accuracy"] * 100)


@measure("trainset.gold_candidate_lists", "candidate lists written while reading, not reconstructed")
def _ts_gold() -> int:
    runs = ROOT / "Plan" / "runs"
    return sum(1 for p in runs.glob("*/03-candidates.md")
               if "reconstruct" not in p.read_text(encoding="utf-8")[:300].lower())


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


MARKER = re.compile(r"(?P<number>[\d,]+|true|false|True|False)\**[^\n\d]{0,40}?<!--\s*state:(?P<key>[a-z_.]+)\s*-->")


SKIP = {"Legacy", ".venv-tools", ".venv-dspy", ".venv-dspytools", ".qmd",
        ".tools-node", ".git", "worktrees", "node_modules"}


def marked_files() -> list[Path]:
    """Every markdown file that could carry a marker, not a list of three.

    This used to be `[CLAUDE.md, NOW.md, PRINCIPLES.md]`, and the blind spot
    behaved exactly like an uncovered qmd collection: `Plan/concept/plan_*.md`
    carried three `<!--state:-->` markers, went stale when the corpus was
    deduplicated, and the check stayed green — because it never looked. A guard
    with a hardcoded file list fails silently the first time someone writes a
    marker somewhere new, which is the one moment it was built for.
    """
    return sorted(p for p in ROOT.rglob("*.md")
                  if not SKIP & set(p.relative_to(ROOT).parts))


def check_prose(paths: list[Path]) -> list[dict]:
    """Every <!--state:key--> marker, against the number written before it."""
    current = {k: fn() for k, (_, fn) in _REGISTRY.items()}
    problems = []
    for path in paths:
        if not path.exists():
            continue
        for match in MARKER.finditer(path.read_text(encoding="utf-8")):
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
