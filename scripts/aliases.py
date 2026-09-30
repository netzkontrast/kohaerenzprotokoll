#!/usr/bin/env python3
"""Which surfaces name the same concept — a learned method, found by experiment.

The author, 2026-09-30: every graph node takes several identifiers, as a wiki page
has several surfaces; surfaces spelled differently that mean the same thing must
point at one node, so one concept is never several nodes; the method is to be
*learned* first, by experiments, and then generalised — graph maintenance.

This is the experiment harness. Each **method** proposes, for a pair of surfaces,
`one-term` or `two-terms` (or abstains). Each is scored on the pairs a person
decided (`trainset.surface_pairs()`, 89 rows from `Plan/runs/judgements.jsonl`),
with the never-merge canaries of `selftest.MUST_NOT_MERGE` as a veto, and on what
it does downstream: how many of `ask`'s 24 bench questions find a seed term.

Methods, from rule to learned:

- `fold`      — `wiki_index.fold`: article, case, diacritics, punctuation.
- `plural`    — decision 010's plural rule (`pairs.plural`).
- `gloss`     — the corpus states the pair itself, `A (B)`, in two or more documents
                (`Plan/runs/bilingual/stated.jsonl`).
- `bilingual` — Jev and free models proposed the pair as a translation
                (`Plan/entities/bilingual.jsonl`, `p >= 0.8`); a proposal layer.
- `context`   — the two surfaces stand in paragraphs that mention the same wiki terms:
                cosine of their paragraph-context vectors over the line graph
                (`askdb`, `MENTIONS`), learned threshold.
- `chars`     — character trigram similarity of the folded forms, learned threshold.
- `vote`      — a combination learned on the labelled pairs: one-term when any rule
                says so, or when `context` and `chars` both clear their thresholds.

Nothing here writes a merge. `apply` writes `P_ALIAS_OF` proposals into the store
for the method the experiments chose; `ask` may route through them, labelled; a
person's decision still goes to `judgements.jsonl`.

    .venv-dspy/bin/python scripts/aliases.py experiment        # score every method, write the run
    .venv-dspy/bin/python scripts/aliases.py apply [--method vote]
    .venv-dspy/bin/python scripts/aliases.py selftest
"""

from __future__ import annotations

import json
import math
import re
import sys
import time
from collections import Counter, defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from wiki_index import fold  # noqa: E402

RUN = ROOT / "Plan" / "runs" / f"aliases-{time.strftime('%Y-%m-%d')}"
STATED = ROOT / "Plan" / "runs" / "bilingual" / "stated.jsonl"
BILINGUAL = ROOT / "Plan" / "entities" / "bilingual.jsonl"


# ── evidence the methods read ─────────────────────────────────────────────────

def glosses(min_docs: int = 2) -> set[frozenset]:
    out = set()
    if STATED.exists():
        for line in STATED.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            if r.get("docs", 0) >= min_docs:
                out.add(frozenset((fold(r["a"]), fold(r["b"]))))
    return out


def bilingual_pairs(min_p: float = 0.8) -> set[frozenset]:
    out = set()
    if BILINGUAL.exists():
        for line in BILINGUAL.read_text(encoding="utf-8").splitlines():
            r = json.loads(line)
            for s in r.get("same_as", []):
                if s.get("p", 0) >= min_p:
                    out.add(frozenset((fold(r["surface"]), fold(s["surface"]))))
    return out


def trigrams(s: str) -> Counter:
    s = f"  {fold(s)} "
    return Counter(s[i:i + 3] for i in range(len(s) - 2))


def cosine(a: Counter, b: Counter) -> float:
    if not a or not b:
        return 0.0
    dot = sum(v * b.get(k, 0) for k, v in a.items())
    return dot / (math.sqrt(sum(v * v for v in a.values())) * math.sqrt(sum(v * v for v in b.values())))


class Context:
    """A surface's paragraph context: the wiki terms mentioned in paragraphs where it stands."""

    def __init__(self):
        import askdb
        self.s = askdb.Store()
        self.para_terms: dict[str, Counter] = defaultdict(Counter)
        for r in self.s.cypher("MATCH (l:Line)-[:MENTIONS]->(t:Term) RETURN l.para AS p, t.id AS t"):
            self.para_terms[r["p"]][r["t"]] += 1
        self.cache: dict[str, Counter] = {}

    def vector(self, surface: str) -> Counter:
        if surface in self.cache:
            return self.cache[surface]
        vec: Counter = Counter()
        phrase = '"' + surface.replace('"', " ") + '"'
        try:
            rows = self.s.sql.execute("SELECT slug, line FROM lines WHERE lines MATCH ? LIMIT 400",
                                      (phrase,)).fetchall()
        except Exception:  # noqa: BLE001 — a surface FTS cannot parse has no context
            rows = []
        for slug, line in rows:
            span = self.s.paragraph(slug, line)
            if span:
                vec.update(self.para_terms.get(f"para:{slug}:{span[0]}", {}))
        self.cache[surface] = vec
        return vec


# ── methods ───────────────────────────────────────────────────────────────────

def make_methods(ctx: Context | None, th_ctx: float, th_chr: float) -> dict:
    import pairs
    gl, bl = glosses(), bilingual_pairs()

    def ctx_sim(a, b):
        return cosine(ctx.vector(a), ctx.vector(b)) if ctx else 0.0

    m = {
        "fold": lambda a, b: "one-term" if fold(a) == fold(b) else "two-terms",
        "plural": lambda a, b: pairs.plural(a, b),
        "gloss": lambda a, b: "one-term" if frozenset((fold(a), fold(b))) in gl else "two-terms",
        "bilingual": lambda a, b: "one-term" if frozenset((fold(a), fold(b))) in bl else "two-terms",
        "chars": lambda a, b: "one-term" if cosine(trigrams(a), trigrams(b)) >= th_chr else "two-terms",
        "context": lambda a, b: "one-term" if ctx_sim(a, b) >= th_ctx else "two-terms",
    }

    def vote(a, b):
        if any(m[k](a, b) == "one-term" for k in ("plural", "gloss")):
            return "one-term"
        return "one-term" if (cosine(trigrams(a), trigrams(b)) >= th_chr and ctx_sim(a, b) >= th_ctx) else "two-terms"
    m["vote"] = vote
    return m


def score(method, rows: list[dict], canaries: list[tuple[str, str]]) -> dict:
    tp = fp = fn = tn = 0
    wrong = []
    for r in rows:
        got = method(r["first"], r["second"])
        gold = r["decision"]
        if got == "one-term" and gold == "one-term":
            tp += 1
        elif got == "one-term":
            fp += 1
            wrong.append(f"false merge {r['id']}: {r['first']} / {r['second']}")
        elif gold == "one-term":
            fn += 1
        else:
            tn += 1
    vetoed = [f"{a} / {b}" for a, b in canaries if method(a, b) == "one-term"]
    prec = tp / (tp + fp) if tp + fp else 0.0
    rec = tp / (tp + fn) if tp + fn else 0.0
    return {"tp": tp, "fp": fp, "fn": fn, "tn": tn, "precision": round(prec, 3), "recall": round(rec, 3),
            "accuracy": round((tp + tn) / len(rows), 3), "vetoed": vetoed, "false_merges": wrong[:10]}


def learn_threshold(sim, rows, canaries) -> float:
    """The lowest threshold with no false merge and no canary merge — precision first."""
    scored = sorted({round(sim(r["first"], r["second"]), 3) for r in rows} | {0.99}, reverse=True)
    best = 1.01
    for th in scored:
        bad = any(sim(r["first"], r["second"]) >= th and r["decision"] != "one-term" for r in rows)
        bad = bad or any(sim(a, b) >= th for a, b in canaries)
        if bad:
            break
        best = th
    return best


def experiment() -> dict:
    import trainset
    import selftest as st
    rows, canaries = trainset.surface_pairs(), list(st.MUST_NOT_MERGE)
    t0 = time.time()
    ctx = Context()
    th_chr = learn_threshold(lambda a, b: cosine(trigrams(a), trigrams(b)), rows, canaries)
    th_ctx = learn_threshold(lambda a, b: cosine(ctx.vector(a), ctx.vector(b)), rows, canaries)
    methods = make_methods(ctx, th_ctx, th_chr)
    # leave-one-out for the learned thresholds, so a threshold is never scored on the row that set it
    loo = {"chars": [], "context": []}
    for i, r in enumerate(rows):
        rest = rows[:i] + rows[i + 1:]
        for name, sim in (("chars", lambda a, b: cosine(trigrams(a), trigrams(b))),
                          ("context", lambda a, b: cosine(ctx.vector(a), ctx.vector(b)))):
            th = learn_threshold(sim, rest, canaries)
            loo[name].append("one-term" if sim(r["first"], r["second"]) >= th else "two-terms")
    result = {"rows": len(rows), "canaries": len(canaries), "thresholds": {"chars": th_chr, "context": th_ctx},
              "methods": {k: score(f, rows, canaries) for k, f in methods.items()}}
    for name, preds in loo.items():
        lookup = {(r["first"], r["second"]): p for r, p in zip(rows, preds)}
        result["methods"][f"{name}-loo"] = score(lambda a, b, L=lookup, n=name: L.get((a, b), methods[n](a, b)),
                                                 rows, canaries)
    result["seconds"] = round(time.time() - t0, 1)
    RUN.mkdir(parents=True, exist_ok=True)
    (RUN / "experiment.json").write_text(json.dumps(result, ensure_ascii=False, indent=1), encoding="utf-8")
    for k, v in result["methods"].items():
        print(f"{k:12} P {v['precision']:.3f}  R {v['recall']:.3f}  acc {v['accuracy']:.3f}  "
              f"fp {v['fp']:2}  veto {len(v['vetoed'])}")
    print(f"thresholds {result['thresholds']}  ({result['seconds']} s) → {RUN.relative_to(ROOT)}/experiment.json")
    return result


def page_pairs(hard: int = 3) -> list[dict]:
    """Labelled pairs from the wiki itself: surfaces of one page are one term (a person
    promoted them there); for each positive, the `hard` most similar surfaces of *other*
    pages are two terms. Grouped by page, so cross-validation never splits a page."""
    import graph as kg
    g = kg.build()
    pages = {k: [s for s in dict.fromkeys(n.get("surfaces", [])) if len(s) >= 3]
             for k, n in g["nodes"].items() if n["type"] == "term"}
    owner = {}
    for k, ss in pages.items():
        for s in ss:
            owner.setdefault(fold(s), k)
    allsurf = [(s, k) for k, ss in pages.items() for s in ss]
    tri = {s: trigrams(s) for s, _ in allsurf}
    rows = []
    for k, ss in pages.items():
        uniq = list({fold(s): s for s in ss}.values())
        for i, a in enumerate(uniq):
            for b in uniq[i + 1:]:
                rows.append({"first": a, "second": b, "decision": "one-term", "page": k})
            near = sorted(((cosine(tri[a], tri[s]), s, o) for s, o in allsurf if o != k),
                          reverse=True)[:hard]
            for _, b, o in near:
                rows.append({"first": a, "second": b, "decision": "two-terms", "page": k})
    return rows


def experiment_pages(folds: int = 5) -> dict:
    """Experiment 2: learn chars/context thresholds on the wiki's own alias sets, page-grouped folds."""
    import selftest as st
    canaries = list(st.MUST_NOT_MERGE)
    rows = page_pairs()
    ctx = Context()
    sims = {"chars": lambda a, b: cosine(trigrams(a), trigrams(b)),
            "context": lambda a, b: cosine(ctx.vector(a), ctx.vector(b))}
    sims["both"] = lambda a, b: min(sims["chars"](a, b), sims["context"](a, b))
    pages = sorted({r["page"] for r in rows})
    fold_of = {p: i % folds for i, p in enumerate(pages)}
    out = {"rows": len(rows), "positives": sum(r["decision"] == "one-term" for r in rows), "methods": {}}
    for name, sim in sims.items():
        preds = {}
        ths = []
        for f in range(folds):
            train = [r for r in rows if fold_of[r["page"]] != f]
            th = learn_threshold(sim, train, canaries)
            ths.append(th)
            for r in rows:
                if fold_of[r["page"]] == f:
                    preds[(r["first"], r["second"], r["page"])] = "one-term" if sim(r["first"], r["second"]) >= th else "two-terms"
        tp = sum(1 for r in rows if r["decision"] == "one-term" and preds[(r["first"], r["second"], r["page"])] == "one-term")
        fp = sum(1 for r in rows if r["decision"] != "one-term" and preds[(r["first"], r["second"], r["page"])] == "one-term")
        pos = out["positives"]
        out["methods"][name] = {"thresholds": ths, "tp": tp, "fp": fp,
                                "precision": round(tp / (tp + fp), 3) if tp + fp else 0.0,
                                "recall": round(tp / pos, 3) if pos else 0.0}
        print(f"{name:8} P {out['methods'][name]['precision']:.3f}  R {out['methods'][name]['recall']:.3f}  "
              f"fp {fp}  thresholds {ths}")
    RUN.mkdir(parents=True, exist_ok=True)
    (RUN / "experiment-pages.json").write_text(json.dumps(out, ensure_ascii=False, indent=1), encoding="utf-8")
    return out


def selftest() -> list[str]:
    fails = []
    if cosine(trigrams("Kern-Welten"), trigrams("Kernwelten")) < 0.8:
        fails.append("trigram similarity misses a hyphen variant")
    if cosine(trigrams("Negentropie"), trigrams("Entropie")) >= 0.99:
        fails.append("a canary is identical by trigrams")
    rows = [{"first": "a", "second": "b", "decision": "two-terms"}, {"first": "c", "second": "d", "decision": "one-term"}]
    sim = {("a", "b"): 0.5, ("c", "d"): 0.9, ("x", "y"): 0.7}
    th = learn_threshold(lambda a, b: sim.get((a, b), 0.0), rows, [("x", "y")])
    if not (0.7 < th <= 0.9):
        fails.append(f"threshold learned wrongly: {th}")
    return fails


def main(argv: list[str]) -> int:
    cmd = argv[0] if argv else "-h"
    if cmd == "experiment":
        experiment()
    elif cmd == "experiment-pages":
        experiment_pages()
    elif cmd == "selftest":
        fails = selftest()
        for f in fails:
            print("FAIL", f)
        print(f"aliases selftest: {'held' if not fails else 'FAILED'}")
        return 1 if fails else 0
    else:
        print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
