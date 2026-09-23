"""Graph retrieval over the wiki: a question in, attributed evidence out, never an answer.

The wiki is for answering questions — that is what the process diagram's last
arrow, `ask`, is — and it cannot yet. This is the retrieval half, and it is
built so that the thing it returns cannot misstate a source:

1. **Seed** — find the term pages the question names, by the surfaces
   `wiki_index` already folds to each page. Matching is `fold()`, the rule every
   other lookup here uses; nothing is embedded and nothing is guessed.
2. **Spread** — personalized PageRank from the seeds over `graph.py`'s typed
   graph (links, conflicts, questions, the documents pages read). A page two
   links away from a seed, contested by the same conflict, ranks above one that
   merely shares a word. This is the step that makes it *graph* retrieval.
3. **Select** — candidate evidence is every **verified** quotation on the
   ranked pages (the exact set `quotes.py` passes). Chosen by Maximal Marginal
   Relevance **with a relevance floor**, ported from
   `netzkontrast/dspy-agent-skills` `scaffolding/kp_canon_retriever.py`
   (itself from `dspy-refrag`, MIT). The floor is not optional: measured there,
   plain MMR picks an unrelated passage over a relevant near-duplicate at every
   λ from 0.5 to 0.8, because zero relevance with zero redundancy outscores
   high relevance with high redundancy.
4. **Return** — the quotations verbatim with document and line, the conflicts
   that touch the ranked pages, the open questions that do, and the documents
   the mass flowed to. **No synthesis** (P13): `Agentic-Dspy-Rag`'s synthesizer
   merges sources into unattributed prose, which is the operation this wiki
   exists to refuse.

`--answer` adds one model step, and it cannot quote: the model is shown the
numbered evidence and returns **numbers** and a list of gaps. Code prints the
quotations those numbers point at. A model that cannot type a quotation cannot
misquote one — P26, applied to answering. It runs through `lmrun.call`, so the
cache is off, the call is recorded, and a real model needs `--approval`.

`bench` scores retrieval against what the wiki already knows: each question
page names the pages that raise it, and each conflict names the pages it
contests. The question or conflict being asked is **removed from the graph**
first — otherwise it would retrieve itself. Two methods, the seeds alone and
PageRank, so the number says whether the graph earns its step.

    python3 scripts/graphrag.py ask "Wie hängen die Guardians mit AEGIS zusammen?"
    python3 scripts/graphrag.py ask "…" --json
    python3 scripts/graphrag.py bench [--k 8] [--record]
    python3 scripts/graphrag.py selftest
    .venv-dspy/bin/python scripts/graphrag.py ask "…" --answer --dry-run
    .venv-dspy/bin/python scripts/graphrag.py ask "…" --answer --model openrouter/… --approval "…"
"""

from __future__ import annotations

import json
import math
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import graph as kg  # noqa: E402
from wiki_index import fold  # noqa: E402

WEIGHTS = {"links": 1.0, "contests": 0.8, "raised_by": 0.8, "concerns": 0.5,
           "reads": 0.3, "cites": 0.3, "asks": 0.3}
DAMPING = 0.85
ITERATIONS = 40
TOP_TERMS = 8
BUDGET = 8
DIVERSITY_LAMBDA = 0.65   # kp_canon_retriever's measured default, above upstream's 0.5
MIN_RELEVANCE = 0.15      # the floor; 0.0 reproduces unguarded MMR
MIN_SURFACE = 4           # a shorter fold is a substring of far too much
STOP = set("aber alle auch dass dem den der des die das ein eine einem einen einer eines "
           "für ist mit nicht noch oder sich sind und von was wie wird zum zur über "
           "the and are does how what which with".split())


# --- text -----------------------------------------------------------------------

def tokens(text: str) -> list[str]:
    return [t for t in (fold(w) for w in re.findall(r"\w+", text))
            if len(t) >= MIN_SURFACE and t not in STOP]


def vector(text: str) -> Counter:
    return Counter(tokens(text))


def cosine(a: Counter, b: Counter) -> float:
    dot = sum(a[k] * b[k] for k in a if k in b)
    na, nb = math.sqrt(sum(v * v for v in a.values())), math.sqrt(sum(v * v for v in b.values()))
    return dot / (na * nb) if na and nb else 0.0


# --- the four steps ---------------------------------------------------------------

def seeds(graph: dict, query: str) -> dict[str, tuple[float, str]]:
    """term node → (weight, the surface that matched). Folded containment only."""
    folded = fold(query)
    words = set(tokens(query))
    found: dict[str, tuple[float, str]] = {}
    for key, node in graph["nodes"].items():
        if node["type"] != "term":
            continue
        best = (0.0, "")
        for surface in node.get("surfaces", []):
            f = fold(surface)
            if len(f) >= MIN_SURFACE and f in folded:
                best = max(best, (1.0 + len(f) / 100, surface))
            elif set(tokens(surface)) & words:
                share = len(set(tokens(surface)) & words) / max(len(set(tokens(surface))), 1)
                best = max(best, (0.5 * share, surface))
        if best[0] > 0:
            found[key] = best
    return found


def pagerank(graph: dict, start: dict[str, float]) -> dict[str, float]:
    """Personalized PageRank: restart at the seeds, walk typed edges both ways."""
    if not start:
        return {}
    out: dict[str, list[tuple[str, float]]] = {}
    for e in graph["edges"]:
        w = WEIGHTS.get(e["type"], 0.0)
        if w and e["source"] in graph["nodes"] and e["target"] in graph["nodes"]:
            out.setdefault(e["source"], []).append((e["target"], w))
            out.setdefault(e["target"], []).append((e["source"], w))
    total = sum(start.values())
    restart = {k: v / total for k, v in start.items()}
    rank = dict(restart)
    for _ in range(ITERATIONS):
        nxt = {k: (1 - DAMPING) * v for k, v in restart.items()}
        for node, mass in rank.items():
            links = out.get(node)
            if not links:
                for k, v in restart.items():  # dangling mass returns to the seeds
                    nxt[k] = nxt.get(k, 0.0) + DAMPING * mass * v
                continue
            norm = sum(w for _, w in links)
            for target, w in links:
                nxt[target] = nxt.get(target, 0.0) + DAMPING * mass * w / norm
        rank = nxt
    return rank


def select_mmr(relevance: list[float], similar, budget: int = BUDGET,
               diversity_lambda: float = DIVERSITY_LAMBDA,
               min_relevance: float = MIN_RELEVANCE) -> list[int]:
    """Maximal Marginal Relevance with a relevance floor.

    Ported from dspy-agent-skills `scaffolding/kp_canon_retriever.py`
    `select_mmr` (itself dspy-refrag `sensor_advanced.py`, MIT), generalised to
    take precomputed relevance and a similarity function. Candidates below
    `min_relevance` are excluded *before* selection — see the module docstring
    for why the floor is the part that matters.
    """
    remaining = [i for i, r in enumerate(relevance) if r >= min_relevance]
    chosen: list[int] = []
    while remaining and len(chosen) < budget:
        best, best_score = remaining[0], -math.inf
        for i in remaining:
            redundancy = max((similar(i, j) for j in chosen), default=0.0)
            score = (1 - diversity_lambda) * relevance[i] - diversity_lambda * redundancy
            if score > best_score:
                best, best_score = i, score
        chosen.append(best)
        remaining.remove(best)
    return chosen


def retrieve(query: str, graph: dict | None = None, top_terms: int = TOP_TERMS,
             budget: int = BUDGET, include_unchecked: bool = False, method: str = "ppr") -> dict:
    graph = graph or kg.build()
    seeded = seeds(graph, query)
    if method == "seeds":
        rank = {k: w for k, (w, _) in seeded.items()}
    else:
        rank = pagerank(graph, {k: w for k, (w, _) in seeded.items()})
    terms = sorted((k for k in rank if graph["nodes"].get(k, {}).get("type") == "term"),
                   key=lambda k: (-rank[k], k))[:top_terms]
    peak = max((rank[k] for k in terms), default=1.0) or 1.0

    qv = vector(query)
    pool = []
    for key in terms:
        for ev in graph["evidence"].get(key.split(":", 1)[1], []):
            if ev["status"] == "verified" or (include_unchecked and ev["status"] == "unchecked"):
                pool.append({**ev, "page": key.split(":", 1)[1], "vec": vector(ev["quote"]),
                             "node_rank": rank[key] / peak})
    relevance = [0.5 * p["node_rank"] + 0.5 * cosine(qv, p["vec"]) for p in pool]
    picked = select_mmr(relevance, lambda i, j: cosine(pool[i]["vec"], pool[j]["vec"]), budget)
    evidence = [{k: v for k, v in pool[i].items() if k != "vec"} | {"relevance": round(relevance[i], 3)}
                for i in picked]

    touching = set(terms)
    conflicts, questions = [], []
    for e in graph["edges"]:
        if e["target"] in touching and e["type"] == "contests":
            conflicts.append(e["source"])
        if e["target"] in touching and e["type"] == "raised_by":
            questions.append(e["source"])
    docs = sorted((k for k in rank if k.startswith("doc:")), key=lambda k: -rank[k])
    node = graph["nodes"]
    return {
        "query": query, "method": method,
        "seeds": [{"term": k, "surface": s, "weight": round(w, 3)}
                  for k, (w, s) in sorted(seeded.items(), key=lambda kv: -kv[1][0])],
        "terms": [{"id": k, "term": node[k]["term"], "rank": round(rank[k] / peak, 3),
                   "conflict": node[k].get("conflict")} for k in terms],
        "evidence": evidence,
        "not_selected": len(pool) - len(evidence),
        "below_floor": sum(1 for r in relevance if r < MIN_RELEVANCE),
        "conflicts": [{"id": c, "subject": node[c].get("subject"), "kind": node[c].get("kind")}
                      for c in dict.fromkeys(conflicts) if c in node],
        "questions": [{"id": q, "question": node[q].get("question")}
                      for q in dict.fromkeys(questions) if q in node],
        "documents": [{"id": d, "title": node[d].get("title")} for d in docs[:5]],
    }


# --- rendering --------------------------------------------------------------------

def render(pack: dict) -> str:
    out = [f"# Evidence for: {pack['query']}", ""]
    if not pack["seeds"]:
        out += ["**No page's surface occurs in the question.** Nothing was retrieved — "
                "name a term the wiki has, or search the corpus with qmd.", ""]
        return "\n".join(out)
    out.append("Seeds: " + ", ".join(f"`{s['term'].split(':')[1]}` via „{s['surface']}\""
                                     for s in pack["seeds"][:6]))
    out += ["", "## Pages, by graph rank", ""]
    for t in pack["terms"]:
        flag = f" — conflict: {t['conflict']}" if t["conflict"] and t["conflict"] not in ("none", "none yet") else ""
        out.append(f"- {t['rank']:.2f}  [[{t['id'].split(':')[1]}|{t['term']}]]{flag}")
    out += ["", f"## Evidence — {len(pack['evidence'])} verified quotations, "
            f"{pack['not_selected']} not selected ({pack['below_floor']} below the relevance floor)", ""]
    for i, ev in enumerate(pack["evidence"], 1):
        out.append(f"{i}. „{ev['quote']}\" ^[{ev['doc']}.md:L{ev['line']}]  "
                   f"— on [[{ev['page']}]], {ev['section'] or 'no section'}")
    if pack["conflicts"]:
        out += ["", "## Sources disagree here — read the record before using the evidence", ""]
        out += [f"- {c['id'].split(':')[1]} — {c['subject']}: {c['kind']}" for c in pack["conflicts"]]
    if pack["questions"]:
        out += ["", "## Open questions these pages carry", ""]
        out += [f"- {q['id'].split(':')[1]} — {q['question']}" for q in pack["questions"]]
    out += ["", "## Documents the rank flowed to", ""]
    out += [f"- `{d['id'].split(':')[1]}` — {d['title']}" for d in pack["documents"]]
    return "\n".join(out)


# --- the one model step -------------------------------------------------------------

def answer(pack: dict, model: str | None, approval: str | None, dry_run: bool) -> dict:
    """The model picks evidence numbers and names gaps; code prints the quotations."""
    import dspy
    from lmrun import call, make_lm

    class ChooseEvidence(dspy.Signature):
        """Wähle aus den nummerierten Belegen diejenigen, die die Frage beantworten.
        Schreibe keine Zitate ab und formuliere keine eigene Antwort: nenne nur die
        Nummern. Wo die Belege die Frage nicht beantworten, nenne die Lücke in `gaps`.
        Widersprechen sich Belege, wähle beide."""
        question: str = dspy.InputField()
        evidence: str = dspy.InputField(desc="nummerierte, zitierte Belege")
        chosen: list[int] = dspy.OutputField(desc="Nummern der Belege, die antworten")
        gaps: list[str] = dspy.OutputField(desc="was die Belege nicht beantworten")

    numbered = "\n".join(f"{i}. „{e['quote']}\" ({e['doc']}, L{e['line']})"
                         for i, e in enumerate(pack["evidence"], 1))
    program = dspy.Predict(ChooseEvidence)
    if dry_run:
        from lm_fixture import FixtureLM, chat, offline
        lm = FixtureLM(lambda m: chat(chosen="[1, 2, 99]", gaps='["Probelauf — keine echte Auswahl"]'))
        with offline(lm):
            import tempfile  # a rehearsal leaves no record in Plan/runs/
            pred, rec = call(program, step="answer", subject="graphrag", out_dir=Path(tempfile.mkdtemp()),
                             question=pack["query"], evidence=numbered)
    else:
        with dspy.context(lm=make_lm(model)):
            pred, rec = call(program, step="answer", subject="graphrag", approval=approval,
                             question=pack["query"], evidence=numbered)
    chosen = list(getattr(pred, "chosen", []) or []) if pred else []
    valid = [n for n in chosen if isinstance(n, int) and 1 <= n <= len(pack["evidence"])]
    return {"status": rec["status"], "chosen": [pack["evidence"][n - 1] for n in dict.fromkeys(valid)],
            "invalid_numbers": [n for n in chosen if n not in valid],
            "gaps": list(getattr(pred, "gaps", []) or []) if pred else [], "record": rec["step"]}


# --- bench ----------------------------------------------------------------------------

def cases(graph: dict) -> list[dict]:
    """What the wiki already knows: questions → the pages raising them; conflicts → pages."""
    out = []
    for key, node in graph["nodes"].items():
        if node["type"] == "question":
            gold = {e["target"] for e in graph["edges"] if e["source"] == key and e["type"] == "raised_by"}
            out.append({"id": key, "query": node["question"], "gold": gold})
        elif node["type"] == "conflict":
            gold = {e["target"] for e in graph["edges"] if e["source"] == key and e["type"] == "contests"}
            out.append({"id": key, "query": f"{node['subject']} — {node['kind']}", "gold": gold})
    return out


def without(graph: dict, key: str) -> dict:
    """The graph with one node and its edges removed, so a case cannot retrieve itself."""
    return {"nodes": {k: v for k, v in graph["nodes"].items() if k != key},
            "edges": [e for e in graph["edges"] if key not in (e["source"], e["target"])],
            "evidence": graph["evidence"]}


def bench(k: int = TOP_TERMS) -> dict:
    graph = kg.build()
    result = {}
    for method in ("seeds", "ppr"):
        rows = []
        for case in cases(graph):
            pack = retrieve(case["query"], without(graph, case["id"]), top_terms=k, method=method)
            got = {t["id"] for t in pack["terms"]}
            hit = len(got & case["gold"])
            rows.append({"id": case["id"], "recall": round(hit / len(case["gold"]), 3) if case["gold"] else None,
                         "precision": round(hit / len(got), 3) if got else None,
                         "seeded": bool(pack["seeds"])})
        result[method] = rows
    return result


def selftest() -> list[str]:
    """The floor's measured case, the leave-out, and an empty seed — each asserted."""
    failures = []
    # kp_canon_retriever's fixture: two near-duplicates (0, 1), one relevant but
    # distinct (2), one unrelated (3). Relevance, and similarity between passages:
    relevance = [0.9, 0.88, 0.6, 0.0]
    sim = {(0, 1): 0.97, (0, 2): 0.5, (1, 2): 0.5}
    similar = lambda i, j: 1.0 if i == j else sim.get((min(i, j), max(i, j)), 0.0)  # noqa: E731
    if 3 in select_mmr(relevance, similar, budget=2, diversity_lambda=0.65, min_relevance=0.0):
        pass  # unguarded MMR may pick the unrelated passage; that is the defect the floor fixes
    else:
        failures.append("fixture no longer reproduces unguarded MMR choosing the unrelated passage")
    guarded = select_mmr(relevance, similar, budget=2, diversity_lambda=0.65)
    if guarded != [0, 2]:
        failures.append(f"with the floor, expected duplicate + relevant-distinct [0, 2], got {guarded}")
    graph = kg.build()
    for case in cases(graph):
        if case["id"] in without(graph, case["id"])["nodes"]:
            failures.append(f"{case['id']} can retrieve itself in the bench")
            break
    pack = retrieve("xyzzy quux", graph)
    if pack["seeds"] or pack["evidence"]:
        failures.append("a question naming no term retrieved something anyway")
    return failures


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        problems = selftest()
        for p in problems:
            print(f"  FAIL  {p}")
        print(f"graphrag: {4 - len(problems)} of 4 cases hold (unguarded MMR defect reproduced, "
              "floor fixes it, bench leave-out, no seed → nothing)")
        return 1 if problems else 0
    if not argv or argv[0] not in ("ask", "bench"):
        print(__doc__)
        return 2
    if argv[0] == "bench":
        k = int(argv[argv.index("--k") + 1]) if "--k" in argv else TOP_TERMS
        result = bench(k)
        for method, rows in result.items():
            scored = [r["recall"] for r in rows if r["recall"] is not None]
            unseeded = sum(1 for r in rows if not r["seeded"])
            mean = sum(scored) / len(scored) if scored else float("nan")
            print(f"{method:<6} recall@{k} {mean:.3f} over {len(scored)} cases; "
                  f"{unseeded} cases found no seed")
            for r in rows:
                print(f"   {r['id']:<14} recall {r['recall']}  precision {r['precision']}"
                      f"{'' if r['seeded'] else '  (no seed)'}")
        if "--record" in argv:
            import baseline
            graph = kg.build()
            for method, rows in result.items():
                baseline.append(baseline.row(
                    "graphrag-retrieval", method, {r["id"]: r["recall"] for r in rows},
                    program={"method": method, "weights": WEIGHTS, "damping": DAMPING, "k": k,
                             "lambda": DIVERSITY_LAMBDA, "floor": MIN_RELEVANCE},
                    trainset=[(c["id"], sorted(c["gold"])) for c in cases(graph)],
                    note=f"recall@{k} of pages, the case's own node removed"))
            print("recorded to Plan/runs/baselines.jsonl — compare with: "
                  "python3 scripts/baseline.py compare graphrag-retrieval --floor seeds")
        return 0

    query = " ".join(a for a in argv[1:] if not a.startswith("--") and
                     argv[argv.index(a) - 1] not in ("--model", "--approval", "--budget"))
    budget = int(argv[argv.index("--budget") + 1]) if "--budget" in argv else BUDGET
    pack = retrieve(query, budget=budget, include_unchecked="--unchecked" in argv)
    if "--answer" in argv:
        model = argv[argv.index("--model") + 1] if "--model" in argv else None
        approval = argv[argv.index("--approval") + 1] if "--approval" in argv else None
        if not model and "--dry-run" not in argv:
            print("--answer needs --model and --approval, or --dry-run")
            return 2
        pack["answer"] = answer(pack, model, approval, "--dry-run" in argv)
    if "--json" in argv:
        print(json.dumps(pack, ensure_ascii=False, indent=1))
        return 0
    print(render(pack))
    if "answer" in pack:
        a = pack["answer"]
        print(f"\n## The model chose ({a['status']}) — quotations printed by code, not typed by it\n")
        for ev in a["chosen"]:
            print(f"- „{ev['quote']}\" ^[{ev['doc']}.md:L{ev['line']}]")
        if a["invalid_numbers"]:
            print(f"\nDropped: {a['invalid_numbers']} — numbers that name no evidence")
        if a["gaps"]:
            print("\nGaps, in the model's words (not canon):")
            print("\n".join(f"- {g}" for g in a["gaps"]))
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
