#!/usr/bin/env python3
"""What each relation type is worth to retrieval, measured — the graph laboratory.

The author, 2026-09-30: „Dont forget we want to einrichten our Graph with useful Information
- for this we Need to Experiment - Even maybe to Treat Everything the Same … Maybe some
Relations or Relation types Need to Rank differentes using another mix of Graph Relations
we can capture with our hyperextract enriched graph".

So the weights of `graphrag.py` are not chosen here, they are asked. One task, the wiki's own
labels: the 24 questions and conflicts, each retrieving the pages that raised or contest it,
with the case's own node left out (`graphrag.bench`'s task). Recall@8 of pages. The labels
were written by the same hand as the pages, which is the caveat the bench already carries;
what a number here can say is which mix does better on this hand's labels, never that a mix
is right.

    python3 scripts/graphlab.py diagnose          # per case: seeds, misses, and how far a miss is
    python3 scripts/graphlab.py core              # E1: the seven stated relation types — uniform,
                                                  #     one alone, one off, learned with cross-validation
    python3 scripts/graphlab.py enrich            # E2: relations the corpus adds — co-occurrence,
                                                  #     co-mention, the BM25 relation — at every weight
    python3 scripts/graphlab.py comention         # E2b: the normalised co-mention relation, sparsified, at every weight
    python3 scripts/graphlab.py hub               # E4: the hub correction and the seed specificity of
                                                  #     `graphrag.pagerank`, each off by default
    python3 scripts/graphlab.py he                # E5: page pairs the HyperExtract contracts read (`hegraph.py`),
                                                  #     by relation family, at every weight
    python3 scripts/graphlab.py selftest

Standard library only; `enrich` reads the shared store (`Plan/derived/ask.db`) with sqlite3
and refuses a stale one, like every reader of it. Every configuration is a row in
`Plan/runs/baselines.jsonl`, so `baseline.py compare` says which beat the floor by the
ledger's tolerance, and every table lands in `Plan/runs/graph-lab-2026-09-30/`.

**What it does not do:** decide a weight for `graphrag.py`. A weight is changed there by a
person, from the paired comparison printed beside it — the mean difference, its 90 %
interval over the cases, and how many cases moved each way. With 24 cases and two of them
finding no seed, a difference below the interval's width is not a difference.
"""

from __future__ import annotations

import json
import math
import random
import sqlite3
import sys
from collections import defaultdict, deque
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import graph as kg  # noqa: E402
import graphrag  # noqa: E402

FOLDER = ROOT / "Plan" / "runs" / "graph-lab-2026-09-30"
DB = ROOT / "Plan" / "derived" / "ask.db"
GRID = (0.0, 0.15, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0)
TYPES = tuple(graphrag.WEIGHTS)                     # the seven stated relation types
K = graphrag.TOP_TERMS


# ── the task ──────────────────────────────────────────────────────────────────

class Lab:
    """The wiki's labelled cases, each with its own node left out and its seeds found once."""

    def __init__(self, graph: dict | None = None):
        self.graph = graph or kg.build()
        self.cases = graphrag.cases(self.graph)
        self.held = {c["id"]: graphrag.without(self.graph, c["id"]) for c in self.cases}
        self.seeded = {c["id"]: graphrag.seeds(self.held[c["id"]], c["query"]) for c in self.cases}
        self.gold = {c["id"]: c["gold"] for c in self.cases}
        self.order = sorted(self.gold)

    def run(self, weights: dict[str, float], extra: list[dict] | None = None,
            ids: list[str] | None = None, k: int = K, hub: float = 0.0, spec: float = 0.0) -> dict[str, dict]:
        """id → recall@k, precision@k and recall@2k, with the extra edges added to each case's graph."""
        rows = {}
        for cid in ids or self.order:
            g = self.held[cid]
            if extra:
                g = {**g, "edges": g["edges"] + extra}
            rank, terms = graphrag.ranked_terms(g, self.seeded[cid], "ppr", 2 * k, weights, hub, spec)
            gold = self.gold[cid]
            top, wide = set(terms[:k]), set(terms)
            hit = len(top & gold)
            rows[cid] = {"recall": hit / len(gold) if gold else None,
                         "precision": hit / len(top) if top else None,
                         "recall_wide": len(wide & gold) / len(gold) if gold else None,
                         "seeded": bool(self.seeded[cid])}
        return rows


def mean(rows: dict[str, dict], key: str = "recall") -> float:
    vals = [r[key] for r in rows.values() if r[key] is not None]
    return sum(vals) / len(vals) if vals else float("nan")


def objective(rows: dict[str, dict]) -> float:
    """recall@8 and recall@16 together: a plateau at 8 has a slope at 16 to climb."""
    return 0.5 * mean(rows, "recall") + 0.5 * mean(rows, "recall_wide")


def paired(a: dict[str, dict], b: dict[str, dict], seed: int = 0, draws: int = 2000) -> dict:
    """b − a over the cases both score: the mean, a 90 % bootstrap interval and who moved which way."""
    ids = [i for i in a if a[i]["recall"] is not None and i in b]
    diff = [b[i]["recall"] - a[i]["recall"] for i in ids]
    if not diff:
        return {"mean": float("nan"), "lo": float("nan"), "hi": float("nan"), "up": 0, "down": 0, "same": 0}
    rng = random.Random(seed)
    boots = sorted(sum(rng.choice(diff) for _ in diff) / len(diff) for _ in range(draws))
    return {"mean": sum(diff) / len(diff), "lo": boots[int(0.05 * draws)], "hi": boots[int(0.95 * draws) - 1],
            "up": sum(d > 1e-9 for d in diff), "down": sum(d < -1e-9 for d in diff),
            "same": sum(abs(d) <= 1e-9 for d in diff)}


def ascend(lab: Lab, ids: list[str], start: dict[str, float], types: tuple[str, ...] = TYPES,
           grid: tuple[float, ...] = GRID, passes: int = 3, extra: list[dict] | None = None) -> dict:
    """Coordinate ascent on `objective` over `ids`: one weight at a time to its best grid value."""
    weights = dict(start)
    best = objective(lab.run(weights, extra, ids))
    for _ in range(passes):
        moved = False
        for t in types:
            for value in grid:
                if abs(value - weights.get(t, 0.0)) < 1e-9:
                    continue
                trial = {**weights, t: value}
                score = objective(lab.run(trial, extra, ids))
                if score > best + 1e-9:
                    weights, best, moved = trial, score, True
        if not moved:
            break
    return {"weights": weights, "objective": best}


def folds(ids: list[str], n: int) -> list[list[str]]:
    """Deterministic folds over the sorted ids; every case is held out exactly once."""
    return [ids[i::n] for i in range(n)]


def cross_validate(lab: Lab, start: dict[str, float], n: int = 6, extra: list[dict] | None = None,
                   types: tuple[str, ...] = TYPES) -> dict:
    """Each fold's cases are scored with weights fitted on the other folds."""
    scored, learned = {}, []
    for held_out in folds(lab.order, n):
        train = [i for i in lab.order if i not in held_out]
        fit = ascend(lab, train, start, types, extra=extra)
        learned.append(fit["weights"])
        scored.update(lab.run(fit["weights"], extra, held_out))
    spread = {t: (min(w.get(t, 0.0) for w in learned), max(w.get(t, 0.0) for w in learned)) for t in types}
    return {"rows": scored, "learned": learned, "spread": spread}


# ── the ledger and the tables ─────────────────────────────────────────────────

def record(task: str, name: str, rows: dict[str, dict], program: object, lab: Lab, note: str) -> None:
    import baseline
    baseline.append(baseline.row(task, name, {i: r["recall"] for i, r in rows.items()}, program=program,
                                 trainset=[(c["id"], sorted(c["gold"])) for c in lab.cases], note=note))


def table(title: str, lines: list[tuple[str, dict, dict | None]], floor: dict) -> str:
    """name, rows, weights → one markdown row each, with the paired comparison to the floor."""
    out = [f"### {title}", "",
           "| configuration | recall@8 | precision@8 | recall@16 | vs the floor: mean, 90 % interval | up / down / same |",
           "|---|---|---|---|---|---|"]
    for name, rows, _ in lines:
        d = paired(floor, rows)
        out.append(f"| {name} | {mean(rows):.3f} | {mean(rows, 'precision'):.3f} | {mean(rows, 'recall_wide'):.3f} | "
                   f"{d['mean']:+.3f} [{d['lo']:+.3f}, {d['hi']:+.3f}] | {d['up']} / {d['down']} / {d['same']} |")
    return "\n".join(out) + "\n"


def write(name: str, text: str, data: object) -> None:
    FOLDER.mkdir(parents=True, exist_ok=True)
    (FOLDER / f"{name}.md").write_text(text, encoding="utf-8")
    (FOLDER / f"{name}.json").write_text(json.dumps(data, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")


# ── diagnose: a miss is a ranking miss or a reach miss ────────────────────────

def hops(graph: dict, sources: set[str], weights: dict[str, float]) -> dict[str, int]:
    """Steps from the seeds along the edge types the weights walk, either way."""
    adj = defaultdict(set)
    for e in graph["edges"]:
        if weights.get(e["type"], 0.0) > 0:
            adj[e["source"]].add(e["target"])
            adj[e["target"]].add(e["source"])
    seen = {s: 0 for s in sources}
    queue = deque(sources)
    while queue:
        n = queue.popleft()
        for m in adj[n]:
            if m not in seen:
                seen[m] = seen[n] + 1
                queue.append(m)
    return seen


def cmd_diagnose(lab: Lab) -> str:
    """For every gold page a case misses: unreachable, far, or reached and outranked."""
    weights = dict(graphrag.WEIGHTS)
    out = ["# Diagnosis — why a case misses a page, on the stated graph", "",
           "A miss is one of three, and only one of them is a weight: **no seed** (the question names no page's "
           "surface, so nothing walks), **unreachable** (no path along the walked relation types from any seed to "
           "the page: no weights can bring it), or **outranked** (reached, and eight other terms rank above it).", "",
           "| case | gold | hit | no seed | unreachable | outranked | (page: hops, rank among terms) |", "|---|---|---|---|---|---|---|"]
    tallies = defaultdict(int)
    for cid in lab.order:
        g, seeded, gold = lab.held[cid], lab.seeded[cid], lab.gold[cid]
        rank, terms = graphrag.ranked_terms(g, seeded, "ppr", 10 ** 6, weights)
        top = set(terms[:K])
        reach = hops(g, set(seeded), weights)
        pos = {t: i + 1 for i, t in enumerate(terms)}
        hit = gold & top
        if not seeded:
            tallies["no seed"] += len(gold)
            out.append(f"| {cid} | {len(gold)} | 0 | {len(gold)} | | | the question names no page's surface |")
            continue
        un = {p for p in gold - top if p not in reach}
        ou = (gold - top) - un
        tallies["hit"] += len(hit)
        tallies["unreachable"] += len(un)
        tallies["outranked"] += len(ou)
        detail = "; ".join([f"{p.split(':', 1)[1]}: none" for p in sorted(un)]
                           + [f"{p.split(':', 1)[1]}: {reach[p]}, {pos.get(p, '-')}" for p in sorted(ou)])
        out.append(f"| {cid} | {len(gold)} | {len(hit)} | | {len(un)} | {len(ou)} | {detail} |")
    total = sum(tallies.values())
    out += ["", f"**{total} gold pages over {len(lab.order)} cases:** " + ", ".join(
        f"{tallies[k]} {k}" for k in ("hit", "outranked", "unreachable", "no seed")) + ".",
        "", "Weights can move the *outranked*; the *unreachable* and *no seed* need a relation or a surface the "
        "graph does not have — which is what an alias list, a co-occurrence relation or a contract that extracts "
        "term relations would add."]
    return "\n".join(out) + "\n"


# ── E1: the stated relation types ─────────────────────────────────────────────

def cmd_core(lab: Lab, folds_n: int = 6) -> str:
    default = dict(graphrag.WEIGHTS)
    floor = lab.run(default)
    configs: list[tuple[str, dict, dict]] = [("default (graphrag.WEIGHTS)", floor, default)]
    uniform = {t: 1.0 for t in TYPES}
    configs.append(("uniform: every type 1.0", lab.run(uniform), uniform))
    for t in TYPES:
        alone = {u: (1.0 if u == t else 0.0) for u in TYPES}
        configs.append((f"only {t}", lab.run(alone), alone))
    for t in TYPES:
        off = {**default, t: 0.0}
        configs.append((f"default without {t}", lab.run(off), off))
    seeds_only = {k: {"recall": r["recall"], "precision": r["precision"], "recall_wide": r["recall_wide"],
                      "seeded": r["seeded"]} for k, r in {
        cid: {"recall": len(set(sorted(lab.seeded[cid], key=lambda k: -lab.seeded[cid][k][0])[:K]) & lab.gold[cid]) / len(lab.gold[cid]),
              "precision": None, "recall_wide": None, "seeded": bool(lab.seeded[cid])} for cid in lab.order}.items()}
    configs.append(("seeds alone, no walk (graphrag's `seeds`)", seeds_only, {}))
    full = ascend(lab, lab.order, default)
    in_sample = lab.run(full["weights"])
    configs.append(("learned on all 24 (in sample: an upper bound, not a result)", in_sample, full["weights"]))
    cv = cross_validate(lab, default, folds_n)
    configs.append((f"learned, {folds_n}-fold cross-validated (each case scored by weights fitted without it)", cv["rows"], {}))
    for name, rows, weights in configs:
        record("graph-lab-core", name.split(" (")[0].replace(":", ""), rows, weights, lab, "E1: recall@8 of pages, the case's own node removed")
    text = ("# E1 — the stated relation types\n\n"
            "Seven relation types of `graph.py` walk the personalized PageRank of `graphrag.py`. Each row is the same 24 "
            "cases and the same seeds, with only the weights changed. The floor is the default weights.\n\n"
            + table("recall of the wiki's own labels", configs, floor)
            + "\n**The learned weights** (coordinate ascent over a grid, objective recall@8 + recall@16):\n\n"
            + "| type | default | learned on all 24 | across the folds: min–max |\n|---|---|---|---|\n"
            + "\n".join(f"| {t} | {default[t]} | {full['weights'].get(t, 0.0)} | {cv['spread'][t][0]}–{cv['spread'][t][1]} |"
                        for t in TYPES) + "\n")
    write("e1-core", text, {"configs": [{"name": n, "weights": w, "recall": mean(r), "rows": r} for n, r, w in configs],
                            "learned": full, "folds": cv["learned"]})
    return text


# ── E2b: the co-mention relation, normalised and sparsified ───────────────────

MIN_DOCS = (2, 3, 5)
TOP_K = (0, 5, 10, 20)                # 0: every pair
CO_WEIGHTS = (3.0, 10.0, 30.0, 100.0)


def sparsify(pairs: dict[frozenset, float], k: int) -> dict[frozenset, float]:
    """Keep a pair when it is among either page's k strongest: a page's own neighbourhood, never a hub's whole list."""
    if not k:
        return pairs
    near = defaultdict(list)
    for p, v in pairs.items():
        for x in p:
            near[x].append((v, p))
    keep = set()
    for lst in near.values():
        keep.update(p for _, p in sorted(lst, key=lambda t: (-t[0], sorted(t[1])))[:k])
    return {p: pairs[p] for p in keep}


def cmd_comention(lab: Lab) -> str:
    store = Store()
    default = dict(graphrag.WEIGHTS)
    floor = lab.run(default)
    stored = stored_comention()
    known = set(lab.graph["nodes"])
    grid, sizes = {}, {}
    for m in MIN_DOCS:
        base = {p: v["npmi"] for p, v in stored.items() if v["docs"] >= m and v["npmi"] > 0 and p <= known}
        for square in (False, True):
            scaled = {p: (v * v if square else v) for p, v in base.items()}
            for k in TOP_K:
                pairs = sparsify(scaled, k)
                extra = edges_from(pairs, "comention", "MENTIONS in one paragraph, npmi")
                name = f"≥{m} documents, npmi{'²' if square else ''}, {'every pair' if not k else f'top {k} per page'}"
                sizes[name] = len(pairs)
                for w in CO_WEIGHTS:
                    grid[(name, w)] = lab.run({**default, "comention": w}, extra)
    lines = [("floor: the stated relations at their default weights", floor, default)]
    ranked = sorted(grid, key=lambda k: -objective(grid[k]))
    for name, w in ranked[:14]:
        lines.append((f"{name} ({sizes[name]} pairs), weight {w}", grid[(name, w)], {**default, "comention": w}))
    only = {}
    for name in sizes:
        pass
    for (name, w), rows in grid.items():
        record("graph-lab-comention", f"{name}, weight {w}", rows, {"comention": w}, lab, f"E2b: {sizes[name]} pairs")
    candidates = {**grid, ("none", 0.0): floor}
    held, chosen = {}, {}
    for cid in lab.order:
        rest = [i for i in lab.order if i != cid]
        pick = max(candidates, key=lambda k: (objective({i: candidates[k][i] for i in rest}), k == ("none", 0.0)))
        chosen[cid] = pick
        held[cid] = candidates[pick][cid]
    lines.append((f"chosen leaving each case out, over all {len(grid)} configurations and the floor", held, {}))
    record("graph-lab-comention", "configuration chosen leaving one out", held, {}, lab, "E2b: leave-one-out over sparsification, scale and weight")
    picks = defaultdict(int)
    for k in chosen.values():
        picks[k] += 1
    # the walk over the co-mention relation alone: every stated type off
    best_name = ranked[0][0]
    alone_rows = {}
    for m in MIN_DOCS:
        base = {p: v["npmi"] for p, v in stored.items() if v["docs"] >= m and v["npmi"] > 0 and p <= known}
        extra = edges_from(base, "comention", "MENTIONS in one paragraph, npmi")
        alone_rows[f"co-mention alone, ≥{m} documents, every pair"] = lab.run({"comention": 1.0}, extra)
    for name, rows in alone_rows.items():
        lines.append((name, rows, {"comention": 1.0}))
    text = ("# E2b — the normalised co-mention relation\n\n"
            "E2 found that pages standing in one paragraph, weighted by their normalised pointwise mutual information over "
            "documents, raise recall@8 at a large weight while the raw pair count lowers it. This sweeps what that depends on: "
            "the number of documents a pair must stand together in (2, 3, 5), the scale (npmi, its square), the sparsification "
            "(every pair, or a pair kept only when it is among either page's 5, 10 or 20 strongest), and the weight against "
            "the stated `links` at 1.0. The 14 best of "
            f"{len(grid)} configurations by recall@8 + recall@16 are printed; every one is a row of the ledger. Choosing the "
            "best of many on the cases it is scored on overstates it, so the last rows leave each case out and let the other "
            "23 choose.\n\n"
            + table("recall of the wiki's own labels", lines, floor)
            + "\nLeaving each case out, the configuration the other 23 preferred was: "
            + ", ".join(f"{n}, weight {w} ×{c}" for (n, w), c in sorted(picks.items(), key=lambda x: -x[1])) + ".\n")
    write("e2b-comention", text, {"grid": [{"name": n, "weight": w, "pairs": sizes[n], "recall": mean(r), "recall_wide": mean(r, "recall_wide")}
                                          for (n, w), r in grid.items()],
                                  "leave_one_out": {"recall": mean(held), "chosen": {c: list(k) for c, k in chosen.items()}}})
    return text


# ── E4: the hubs ──────────────────────────────────────────────────────────────

HUBS = (0.0, 0.1, 0.25, 0.5, 0.75, 1.0)
SPECS = (0.0, 0.25, 0.5, 1.0)


def cmd_hub(lab: Lab) -> str:
    """The diagnosis found most misses reached and outranked. Two corrections aimed at exactly that."""
    default = dict(graphrag.WEIGHTS)
    floor = lab.run(default)
    grid = [(a, b) for a in HUBS for b in SPECS]
    runs = {(a, b): lab.run(default, hub=a, spec=b) for a, b in grid}
    lines = [("floor: no correction", floor, default)]
    for a, b in grid:
        if (a, b) != (0.0, 0.0):
            lines.append((f"hub {a}, spec {b}", runs[(a, b)], default))
    for a, b in grid:
        record("graph-lab-hub", f"hub {a} spec {b}", runs[(a, b)], {"hub": a, "spec": b}, lab,
               "E4: degree corrections in graphrag.pagerank, recall@8 of pages")
    # leave one case out: the pair chosen on the other cases scores it — picking the best of 24 on all 24 is not a result
    held, chosen = {}, {}
    for cid in lab.order:
        rest = [i for i in lab.order if i != cid]
        pick = max(grid, key=lambda ab: (objective({i: runs[ab][i] for i in rest}), -ab[0] - ab[1]))
        chosen[cid] = pick
        held[cid] = runs[pick][cid]
    lines.append(("chosen leaving each case out (each case scored by the pair the others prefer)", held, {}))
    record("graph-lab-hub", "hub and spec chosen leaving one out", held, {}, lab, "E4: leave-one-out choice over the grid")
    on_all = max(grid, key=lambda ab: (objective(runs[ab]), -ab[0] - ab[1]))
    picks = defaultdict(int)
    for pick in chosen.values():
        picks[pick] += 1
    text = ("# E4 — the hubs\n\n"
            "The diagnosis (`diagnose.md`) found most missed pages reached by the walk and outranked by eight others, and "
            "the pages that outrank them are the hubs — `aegis`, `juna`, `kael`, `vortex`. Two corrections, both in "
            "`graphrag.pagerank` and both off by default: **hub** divides each node's rank by its degree to the power "
            "a (the walk's stationary mass grows with degree); **spec** divides each seed's restart weight by its degree to "
            "the power b, so a seed touching everything pulls less (HippoRAG's node specificity). The same 24 cases, "
            "seeds and stated weights throughout.\n\n"
            + table("recall of the wiki's own labels", lines, floor)
            + f"\nThe best pair on all 24 cases is hub {on_all[0]}, spec {on_all[1]} — chosen on the cases it is scored on, so "
              f"an upper bound. Leaving each case out, the pair the other 23 preferred was: "
              + ", ".join(f"hub {a} spec {b} ×{n}" for (a, b), n in sorted(picks.items(), key=lambda x: -x[1])) + ".\n")
    write("e4-hub", text, {"grid": [{"hub": a, "spec": b, "recall": mean(runs[(a, b)]),
                                       "recall_wide": mean(runs[(a, b)], "recall_wide"), "rows": runs[(a, b)]} for a, b in grid],
                            "leave_one_out": {"recall": mean(held), "chosen": {c: list(p) for c, p in chosen.items()}}})
    return text


# ── the store, read with sqlite3 ──────────────────────────────────────────────

class Store:
    """The shared store's nodes and edges as arrays: keys, labels, and (source, target, type)."""

    def __init__(self, db: Path = DB):
        import askdb
        why = askdb.fresh(db)
        if why:
            raise SystemExit(why)
        con = sqlite3.connect(f"{db.resolve().as_uri()}?mode=ro", uri=True)
        keys = dict(con.execute("SELECT key, id FROM property_keys"))
        self.key = dict(con.execute("SELECT node_id, value FROM node_props_text WHERE key_id=?", (keys["id"],)))
        self.label = defaultdict(set)
        for n, lab in con.execute("SELECT node_id, label FROM node_labels"):
            self.label[n].add(lab)
        self.edges = con.execute("SELECT source_id, target_id, type FROM edges").fetchall()
        self.props = {}
        for name, table in (("support", "int"), ("lift", "real"), ("method", "text")):
            if name in keys:
                self.props[name] = dict(con.execute(f"SELECT node_id, value FROM node_props_{table} WHERE key_id=?", (keys[name],)))
        con.close()
        self.node = {k: n for n, k in self.key.items()}

    def of(self, label: str) -> list[int]:
        return [n for n, labs in self.label.items() if label in labs]


def term_pairs(store: Store) -> dict[frozenset, dict]:
    """Every pair of pages the corpus's learned co-occurrence sets hold together, with support and lift."""
    members = defaultdict(list)
    for s, t, typ in store.edges:
        if typ == "P_MEMBER" and "Term" in store.label[t]:
            members[s].append(store.key[t])
    pairs: dict[frozenset, dict] = {}
    for h, terms in members.items():
        if store.props["method"].get(h) != "cooccur":
            continue
        for i, a in enumerate(sorted(terms)):
            for b in sorted(terms)[i + 1:]:
                cur = pairs.setdefault(frozenset((a, b)), {"support": 0, "lift": 0.0, "sets": 0})
                cur["support"] = max(cur["support"], store.props["support"].get(h, 0))
                cur["lift"] = max(cur["lift"], store.props["lift"].get(h, 0.0))
                cur["sets"] += 1
    return pairs


def stored_comention(con: sqlite3.Connection | None = None) -> dict[frozenset, dict]:
    """The counted co-mention relation as the store holds it — `graphrag.comention_pairs`, the one reader: page pair →
    the documents that hold it and its normalised PMI. The lab reads it, never recomputes it."""
    return graphrag.comention_pairs(con)


def edges_from(pairs: dict[frozenset, float], kind: str, via: str) -> list[dict]:
    return [{"source": a, "target": b, "type": kind, "w": w, "via": via}
            for p, w in pairs.items() for a, b in [sorted(p)]]


def cmd_enrich(lab: Lab) -> str:
    store = Store()
    default = dict(graphrag.WEIGHTS)
    floor = lab.run(default)
    co = term_pairs(store)
    stored = stored_comention()
    known = {n for n in lab.graph["nodes"]}
    co = {p: v for p, v in co.items() if p <= known}
    together = {p: v["docs"] for p, v in stored.items() if p <= known}
    n_docs = "the landed"

    def npmi(p):
        return max(0.0, stored[p]["npmi"])

    sources = {
        "cooccur, one per pair": edges_from({p: 1.0 for p in co}, "cooccur", "askextract cooccur"),
        "cooccur, log2(1+support)": edges_from({p: math.log2(1 + v["support"]) for p, v in co.items()}, "cooccur", "askextract cooccur"),
        "cooccur, lift/10 (capped)": edges_from({p: min(v["lift"], 10.0) / 10 for p, v in co.items()}, "cooccur", "askextract cooccur"),
        "comention, one per pair, ≥2 documents": edges_from({p: 1.0 for p, v in together.items() if v >= 2}, "comention", "MENTIONS in one paragraph"),
        "comention, log2(1+documents)": edges_from({p: math.log2(1 + v) for p, v in together.items() if v >= 2}, "comention", "MENTIONS in one paragraph"),
        "comention, npmi over documents": edges_from({p: npmi(p) for p, v in together.items() if v >= 2 and npmi(p) > 0}, "comention", "MENTIONS in one paragraph"),
    }
    lines, best = [("floor: the stated relations at their default weights", floor, default)], []
    summary = {"pairs": {"cooccur": len(co), "comention": len(together), "documents": n_docs}, "rows": []}
    grid = {}
    for name, extra in sources.items():
        kind = extra[0]["type"] if extra else "cooccur"
        for w in (0.1, 0.3, 1.0, 3.0, 10.0):
            weights = {**default, kind: w}
            rows = lab.run(weights, extra)
            label = f"{name}, weight {w}"
            lines.append((label, rows, weights))
            grid[(name, w)] = rows
            best.append((paired(floor, rows)["mean"], label))
            summary["rows"].append({"source": name, "weight": w, "recall": mean(rows), "rows": rows})
            record("graph-lab-enrich", label, rows, weights, lab, f"E2: {len(extra)} derived edges added")
    # leave one case out: the source and weight the other 23 cases prefer score the one left out. The floor is a
    # candidate too, so a choice that does not beat it on the others is not made.
    candidates = {**grid, ("none", 0.0): floor}
    held, chosen = {}, {}
    for cid in lab.order:
        rest = [i for i in lab.order if i != cid]
        pick = max(candidates, key=lambda k: (objective({i: candidates[k][i] for i in rest}), k == ("none", 0.0)))
        chosen[cid] = pick
        held[cid] = candidates[pick][cid]
    lines.append(("chosen leaving each case out (the source and weight the other cases prefer; the floor is a candidate)", held, {}))
    record("graph-lab-enrich", "source and weight chosen leaving one out", held, {}, lab, "E2: leave-one-out over sources and weights")
    picks = defaultdict(int)
    for k in chosen.values():
        picks[k] += 1
    summary["leave_one_out"] = {"recall": mean(held), "chosen": {c: list(k) for c, k in chosen.items()}}
    text = ("# E2 — relations the corpus adds\n\n"
            f"Derived from the shared store, never from the wiki's labels: {len(co)} page pairs the corpus's learned "
            f"co-occurrence sets hold together (`askextract.py`: two or three pages in one paragraph in five documents "
            f"or more, above lift 1.5), and {len(together)} pairs standing in one paragraph in any document, over "
            f"{n_docs} documents. Each is added to every case's graph as a term–term relation, beside the stated ones, "
            f"which keep their default weights. A scale — one per pair, log of the support, lift, normalised PMI — is "
            f"the relation's own; the weight is its type's.\n\n" + table("recall of the wiki's own labels", lines, floor)
            + "\nLeaving each case out, the pair of source and weight the other 23 preferred was: "
            + ", ".join(f"{n} {w} ×{c}" for (n, w), c in sorted(picks.items(), key=lambda x: -x[1])) + ".\n")
    write("e2-enrich", text, summary)
    return text


# ── E5: what the contracts read ───────────────────────────────────────────────

def he_claims(db: Path = DB) -> list[dict]:
    """Every proposal edge a contract gave, from the store: the claim, its contract, line, node, role and footing."""
    import askdb
    why = askdb.fresh(db)
    if why:
        raise SystemExit(why)
    con = sqlite3.connect(f"{db.resolve().as_uri()}?mode=ro", uri=True)
    keys = dict(con.execute("SELECT key, id FROM property_keys"))
    node = dict(con.execute("SELECT node_id, value FROM node_props_text WHERE key_id=?", (keys["id"],)))
    props = defaultdict(dict)
    for name in ("id", "role", "admitted", "template", "run"):
        for e, v in con.execute("SELECT edge_id, value FROM edge_props_text WHERE key_id=?", (keys[name],)):
            props[e][name] = v
    rows = [{"edge": e, "line": node[s], "node": node[t], "kind": typ[5:], **props[e]}
            for e, s, t, typ in con.execute("SELECT id, source_id, target_id, type FROM edges WHERE type LIKE 'P\\_HE\\_%' ESCAPE '\\'")]
    con.close()
    return rows


def he_pairs(rows: list[dict]) -> tuple[dict[str, set], set]:
    """Page pairs by relation kind — a claim whose source and target both contain pages — and the pairs of
    pages one claim's quotation or names contain together (at most eight pages a claim: a list is not a relation)."""
    claims = defaultdict(list)
    for r in rows:
        if r["node"].startswith("term:"):
            claims[(r["id"], r["run"])].append(r)
    relation, co = defaultdict(set), set()
    for rs in claims.values():
        by_role = defaultdict(set)
        for r in rs:
            by_role[r["role"]].add(r["node"])
        for a in by_role["source"]:
            for b in by_role["target"]:
                if a != b:
                    relation[rs[0]["kind"]].add(frozenset((a, b)))
        pages = sorted({r["node"] for r in rs})[:8]
        for i, a in enumerate(pages):
            for b in pages[i + 1:]:
                co.add(frozenset((a, b)))
    return relation, co


def cmd_he(lab: Lab) -> str:
    rows = he_claims()
    relation, co = he_pairs(rows)
    default = dict(graphrag.WEIGHTS)
    floor = lab.run(default)
    known = set(lab.graph["nodes"])
    stated = {frozenset((e["source"], e["target"])) for e in lab.graph["edges"] if e["type"] == "links"}
    relation = {k: {p for p in v if p <= known} for k, v in relation.items()}
    co = {p for p in co if p <= known}
    allrel = set().union(*relation.values()) if relation else set()
    pages_with = {r["node"] for r in rows if r["node"].startswith("term:")}
    gold = set().union(*lab.gold.values())
    sources = {f"{k.lower()} pairs": pairs for k, pairs in sorted(relation.items()) if len(pairs) >= 3}
    sources["every relation pair"] = allrel
    sources["co-read: pages one claim holds together"] = co
    lines = [("floor: the stated relations at their default weights", floor, default)]
    summary = {"claims": len({(r["id"], r["run"]) for r in rows}), "pages_touched": len(pages_with), "gold_pages": len(gold),
               "gold_pages_touched": len(gold & pages_with), "families": {}, "rows": []}
    reach = {}
    for name, pairs in sources.items():
        kind = "he_" + name.split()[0].replace(":", "").replace("-", "_")
        extra = edges_from({p: 1.0 for p in pairs}, kind, f"hegraph: {name}")
        summary["families"][name] = {"pairs": len(pairs), "new": len(pairs - stated)}
        for w in (0.1, 0.3, 1.0, 3.0):
            weights = {**default, kind: w}
            rows_ = lab.run(weights, extra)
            lines.append((f"{name} ({len(pairs)} pairs, {len(pairs - stated)} not already `links`), weight {w}", rows_, weights))
            summary["rows"].append({"family": name, "weight": w, "recall": mean(rows_), "rows": rows_})
            record("graph-lab-he", f"{name}, weight {w}", rows_, weights, lab, f"E5: {len(pairs)} pairs read by HyperExtract contracts")
        if name in ("every relation pair", "co-read: pages one claim holds together"):
            walk = {**default, kind: 1.0}
            new = 0
            for cid in lab.order:
                before = hops(lab.held[cid], set(lab.seeded[cid]), default)
                g = {**lab.held[cid], "edges": lab.held[cid]["edges"] + extra}
                after = hops(g, set(lab.seeded[cid]), walk)
                new += len({k for k in lab.gold[cid] if k in after and k not in before})
            reach[name] = new
    summary["newly_reachable_gold"] = reach
    text = ("# E5 — what the HyperExtract contracts read\n\n"
            f"{summary['claims']} claims from the contracts' pilot runs are in the store; they touch {summary['pages_touched']} "
            f"of the wiki's 106 pages, and {summary['gold_pages_touched']} of the {summary['gold_pages']} distinct gold pages of the "
            "24 cases. From them: page pairs a claim relates (its source and its target each contain a page), and pairs of pages "
            "one claim holds together. Each set is added to every case's graph as a term–term relation beside the stated ones, "
            "which keep their default weights. The pilot ran eight documents, so the size of what could move is bounded by "
            "the pairs, not by the weights.\n\n"
            + table("recall of the wiki's own labels", lines, floor)
            + "\nGold pages a case could not reach before and can reach with the pairs added (walking the new type at weight 1): "
            + ", ".join(f"{k}: {v}" for k, v in reach.items()) + ".\n")
    write("e5-he", text, summary)
    return text


# ── self-test ─────────────────────────────────────────────────────────────────

def selftest() -> int:
    cases = []
    # a tiny graph: the question seeds `a`; `b` is reached by `links`, `c` by `weak`, `d` by nothing
    g = {"nodes": {k: {"id": k, "type": "term", "surfaces": [k]} for k in "abcd"},
         "edges": [{"source": "term:a", "target": "term:b", "type": "links"},
                   {"source": "term:a", "target": "term:c", "type": "weak"}],
         "evidence": {}}
    g["nodes"] = {f"term:{k}": {"id": f"term:{k}", "type": "term", "surfaces": [k]} for k in "abcd"}
    rank = graphrag.pagerank(g, {"term:a": 1.0}, {"links": 1.0})
    cases.append(("a type the weights do not name is not walked", rank.get("term:b", 0) > rank.get("term:c", 0)
                  and abs(rank.get("term:c", 0) - 0.0) < 0.2 * rank.get("term:b", 1)))
    heavy = graphrag.pagerank({**g, "edges": [dict(e, w=(0.0 if e["type"] == "weak" else 1.0)) for e in g["edges"]]},
                              {"term:a": 1.0}, {"links": 1.0, "weak": 1.0})
    cases.append(("an edge's own scale multiplies its type's weight", heavy.get("term:c", 0) < heavy.get("term:b", 0)))
    cases.append(("the default weights are unchanged", graphrag.pagerank(g, {"term:a": 1.0})
                  == graphrag.pagerank(g, {"term:a": 1.0}, graphrag.WEIGHTS)))
    star = {"nodes": {f"term:{k}": {"id": f"term:{k}", "type": "term", "surfaces": [k]} for k in ("h", "a", "b", "c", "d")},
            "edges": [{"source": "term:h", "target": f"term:{k}", "type": "links"} for k in "abcd"], "evidence": {}}
    plain = graphrag.pagerank(star, {"term:a": 1.0}, {"links": 1.0})
    cases.append(("a hub correction of zero changes nothing",
                  plain == graphrag.pagerank(star, {"term:a": 1.0}, {"links": 1.0}, hub=0.0, spec=0.0)))
    fixed = graphrag.pagerank(star, {"term:a": 1.0}, {"links": 1.0}, hub=1.0)
    cases.append(("the hub loses rank to a leaf under the correction",
                  plain["term:h"] > plain["term:b"] and fixed["term:h"] < plain["term:h"]
                  and fixed["term:b"] / fixed["term:h"] > plain["term:b"] / plain["term:h"]))
    both = graphrag.pagerank(star, {"term:h": 1.0, "term:a": 1.0}, {"links": 1.0})
    spec = graphrag.pagerank(star, {"term:h": 1.0, "term:a": 1.0}, {"links": 1.0}, spec=1.0)
    cases.append(("a seed that touches everything pulls less under spec",
                  spec["term:a"] / spec["term:h"] > both["term:a"] / both["term:h"]))
    rows = [{"id": "c1", "run": "r", "kind": "ALIAS", "role": "source", "node": "term:a", "line": "line:x:1", "edge": 1},
            {"id": "c1", "run": "r", "kind": "ALIAS", "role": "target", "node": "term:b", "line": "line:x:1", "edge": 2},
            {"id": "c1", "run": "r", "kind": "ALIAS", "role": "line", "node": "he:ALIAS", "line": "line:x:1", "edge": 3},
            {"id": "c2", "run": "r", "kind": "CARD", "role": "quote", "node": "term:a", "line": "line:x:2", "edge": 4},
            {"id": "c2", "run": "r", "kind": "CARD", "role": "quote", "node": "term:c", "line": "line:x:2", "edge": 5},
            {"id": "c3", "run": "r", "kind": "CARD", "role": "term", "node": "term:d", "line": "line:x:3", "edge": 6}]
    relation, co = he_pairs(rows)
    cases.append(("a claim's source and target pages are a relation pair", relation == {"ALIAS": {frozenset(("term:a", "term:b"))}}))
    cases.append(("pages one claim holds together are co-read, and one page alone is not a pair",
                  co == {frozenset(("term:a", "term:b")), frozenset(("term:a", "term:c"))}))
    fx = sqlite3.connect(":memory:")
    fx.executescript("""
        CREATE TABLE property_keys (id INTEGER PRIMARY KEY, key TEXT);
        CREATE TABLE node_props_text (node_id INTEGER, key_id INTEGER, value TEXT);
        CREATE TABLE edges (id INTEGER PRIMARY KEY, source_id INTEGER, target_id INTEGER, type TEXT);
        CREATE TABLE edge_props_int (edge_id INTEGER, key_id INTEGER, value INTEGER);
        CREATE TABLE edge_props_real (edge_id INTEGER, key_id INTEGER, value REAL);
        INSERT INTO property_keys VALUES (1,'id'),(2,'docs'),(3,'npmi');
        INSERT INTO node_props_text VALUES (1,1,'term:a'),(2,1,'term:b'),(3,1,'term:c');
        INSERT INTO edges VALUES (1,1,2,'P_COMENTION'),(2,1,3,'P_COMENTION'),(3,1,2,'LINKS');
        INSERT INTO edge_props_int VALUES (1,2,4),(2,2,2);
        INSERT INTO edge_props_real VALUES (1,3,0.5);""")
    got = stored_comention(fx)
    cases.append(("the stored relation is read as pairs of pages with their documents and npmi, and other types are not it",
                  got == {frozenset(("term:a", "term:b")): {"docs": 4, "npmi": 0.5},
                          frozenset(("term:a", "term:c")): {"docs": 2, "npmi": 0.0}}))
    ring = {frozenset(("a", "b")): 0.9, frozenset(("a", "c")): 0.8, frozenset(("a", "d")): 0.7,
            frozenset(("b", "c")): 0.1, frozenset(("b", "d")): 0.1, frozenset(("c", "d")): 0.1}
    cases.append(("a pair is kept when it is among either page's strongest, and a weak one between two pages that have better is dropped",
                  set(sparsify(ring, 1)) == {frozenset(("a", "b")), frozenset(("a", "c")), frozenset(("a", "d"))}
                  and sparsify(ring, 0) == ring))
    ids = [f"c{i:02d}" for i in range(13)]
    fs = folds(ids, 6)
    cases.append(("each case is held out exactly once", sorted(sum(fs, [])) == ids and all(len(f) in (2, 3) for f in fs)))
    same = {"x": {"recall": 0.5}, "y": {"recall": 1.0}}
    d = paired(same, same)
    cases.append(("a run against itself moves nothing", d["mean"] == 0 and d["lo"] == 0 and d["hi"] == 0 and d["same"] == 2))
    better = {"x": {"recall": 1.0}, "y": {"recall": 1.0}}
    d = paired(same, better)
    cases.append(("a paired difference names who moved", d["up"] == 1 and d["down"] == 0 and d["same"] == 1 and d["mean"] == 0.25))
    # the lab's ranking is graphrag's: the same top terms as `retrieve` on the real graph, three cases
    lab = Lab()
    same_terms = True
    for cid in lab.order[:3]:
        if not lab.seeded[cid]:
            continue
        _, terms = graphrag.ranked_terms(lab.held[cid], lab.seeded[cid], "ppr", K)
        pack = graphrag.retrieve(next(c["query"] for c in lab.cases if c["id"] == cid), lab.held[cid])
        same_terms &= terms == [t["id"] for t in pack["terms"]]
    cases.append(("the lab ranks as graphrag.retrieve does", same_terms))
    # the bench's number is not written here, because the wiki grows and it moves (0.694 until the
    # readings of documents 52–54, which is what broke this case on 2026-09-30); every case is compared
    default = lab.run(dict(graphrag.WEIGHTS))
    same_recall = True
    for c in lab.cases:
        if not lab.seeded[c["id"]]:
            continue
        pack = graphrag.retrieve(c["query"], lab.held[c["id"]])
        got = {t["id"] for t in pack["terms"]}
        same_recall &= abs(default[c["id"]]["recall"] - len(got & c["gold"]) / len(c["gold"])) < 1e-9
    cases.append(("the default weights score each case as graphrag.retrieve does", same_recall))
    failed = [n for n, ok in cases if not ok]
    print(f"graphlab: {len(cases) - len(failed)} of {len(cases)} cases hold"
          + (" — FAILED: " + ", ".join(failed) if failed else ""))
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        return selftest()
    commands = {"diagnose": cmd_diagnose, "core": cmd_core, "enrich": cmd_enrich, "comention": cmd_comention,
                "hub": cmd_hub, "he": cmd_he}
    if argv[:1] and argv[0] in commands:
        text = commands[argv[0]](Lab())
        if argv[0] == "diagnose":
            write("diagnose", text, {})
        print(text)
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
