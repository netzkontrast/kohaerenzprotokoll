#!/usr/bin/env python3
"""Which free OpenRouter model answers `ask` packs best — measured, pinned, one model per call.

Each free chat model that accepts the data policy answers the same stored `ask` packs
through `route.chat(pin=True)`, so no other model answers in its place (P16), and
each answer is placed and scored by `ask.verify` and `ask.score`, the code every
`ask` answer goes through. There is no second verifier (P6).

The reference is **not gold**. For each pack, `reference` is the set of lines
Sonnet's landed answer placed (`answer.claude-cli.json`). `ref_hit` says how much of
that set a model's placed claims reached. That measures agreement with one other
model's reading; it is not correctness. `precision` (placed / quoted) and
`fabricated` (words on no line of their document) need no reference at all.
Rule 4 of the card asks for `says` in German, and `german` is the share of claims
whose `says` `route.lang` reads as German.

A model's rank is its mean score times its answer rate. A model the repository pins
has to answer first of all: one that answered 1 of 6 is not usable the way one that
answered 6 of 6 is, whatever it scored once. An unreached call is never a score (P15).

`fabricated` counts quotations standing on no line of their document. It is printed,
and it is not a veto in this ranking. On 2026-09-30 it held one English translation
presented as a quotation, which is a real fabrication. The four others were splices:
two passages joined with „…", table cells stitched together, one quotation under the
wrong document. `verify` discards every one of them, and each already lowers
`precision`. `ask.score`'s `vetoed` stays strict for optimizing a card, where the
card should learn not to do it.

    .venv-dspy/bin/python scripts/route_bench.py run --packs ID,ID --models all --repeats 1 [--max-calls 50] [--threads 10]
    .venv-dspy/bin/python scripts/route_bench.py report [--write]   # rank; --write sets Plan/runs/route/best.json
    .venv-dspy/bin/python scripts/route_bench.py selftest

`best.json` is what the repository pins: `route.rotation()` tries its models first,
in rank order, and `ask.py run --backend route` pins its first model unless
`--model` names another.
"""
from __future__ import annotations

import json
import sys
import threading
import time
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import ask  # noqa: E402
import route  # noqa: E402

OUT = ROOT / "Plan" / "runs" / "route" / "bench"
BEST = ROOT / "Plan" / "runs" / "route" / "best.json"
PIN_DEADLINE = 240     # a 60,000-character pack took free models 6–98 s (2026-09-25); 90 s timed out 8 of 18
_LOCK = threading.Lock()


def candidates() -> list[str]:
    """Free chat models the catalogue saw accept the data policy, still listed today."""
    status, body = route._post(route.API + "/models", None, 60)
    listed = {m["id"] for m in body.get("data", []) if route.is_free(m)} if status == 200 else None
    chat = route.catalogue()["chat"]
    ok = [m for m, v in chat.items() if v["status"] in ("ok", "rate-limited")]
    return sorted(m for m in ok if listed is None or m in listed)


def reference(qid: str) -> set[tuple[str, int]]:
    p = ask.run_dir(qid) / "answer.claude-cli.json"
    if not p.exists():
        return set()
    v = json.loads(p.read_text(encoding="utf-8"))
    return {(c["doc"], q["line"]) for c in v["claims"] for q in c["quotes"] if q["status"] == "placed"}


def one(qid: str, model: str, attempt: int) -> dict:
    pack, meta = ask.load_pack(qid)
    started = time.time()
    rec = route.chat({"messages": [{"role": "user", "content": pack}], "max_tokens": 6000, "temperature": 0},
                     purpose="ask", prefer=model, pin=True, attempt=attempt)
    row = {"pack": qid, "model": model, "attempt": attempt, "at": ask.now(),
           "seconds": round(time.time() - started, 1), "pack_hash": meta["hash"]}
    if "unreached" in rec:
        return row | {"status": "unreached", "why": str(rec["unreached"])[:300],
                      "failed_attempts": len(rec.get("tried", []))}
    return row | {"served_by": rec["model"], "failed_attempts": len(rec.get("tried", []))} \
        | judge(qid, rec["content"], meta)


def judge(qid: str, content: str, meta: dict) -> dict:
    """One answer, placed and scored by ask's own code; the reference is the pack's base run."""
    v = ask.verify(ask.parse(content), meta["shown"])
    sc = ask.score(v, reference(meta.get("repacked_from") or qid), meta["shown"])
    says = [c["says"] for c in v["claims"] + v["unsupported"] if c.get("says")]
    langs = [route.lang(s) for s in says]
    judged = [x for x in langs if x]
    quotes = [len(q["text"].split()) for c in v["claims"] for q in c["quotes"] if q["status"] == "placed"]
    return {"status": v["status"], "why": v.get("why"),
            "counts": v["counts"], "claims": len(v["claims"]), "answerable": v.get("answerable"),
            "score": sc["score"], "precision": sc["precision"], "ref_hit": sc["gold_hit"],
            "fabricated": sc["fabricated"], "spliced": v["counts"].get("spliced", 0), "slug_corrected": v["counts"].get("slug-corrected", 0),
            "quote_words": round(sum(quotes) / len(quotes), 1) if quotes else None,
            "german": round(judged.count("de") / len(judged), 2) if judged else None,
            "content": content}


def sessions(qids: list[str]) -> list[dict]:
    """Score every subagent answer (raw.session*.json) in these runs, grouped by the pack's card."""
    out = []
    for qid in qids:
        _, meta = ask.load_pack(qid)
        for raw in sorted(ask.run_dir(qid).glob("raw.session*.json")):
            try:
                r = ask.loads_lenient(raw.read_text(encoding="utf-8"))
            except json.JSONDecodeError as exc:   # the subagent wrote a broken file: unparsed, never a score
                out.append({"pack": meta.get("repacked_from") or qid, "card": meta.get("rules", "v1"),
                            "file": raw.name, "model": None, "status": "unparsed-file", "why": str(exc),
                            "score": None, "precision": None, "ref_hit": None, "fabricated": 0, "spliced": 0,
                            "german": None, "quote_words": None, "claims": 0, "answerable": None})
                continue
            if r.get("pack_hash") not in (None, meta["hash"]):
                continue
            text = r.get("text") or json.dumps(r.get("answer"), ensure_ascii=False)
            out.append({"pack": meta.get("repacked_from") or qid, "card": meta.get("rules", "v1"),
                        "file": raw.name, "model": r.get("model")} | judge(qid, text, meta))
    return out


def run(packs: list[str], models: list[str], repeats: int, max_calls: int, threads: int) -> Path:
    route.PIN_DEADLINE = PIN_DEADLINE
    OUT.mkdir(parents=True, exist_ok=True)
    out = OUT / f"runs-{time.strftime('%Y-%m-%d')}.jsonl"
    done = {(r["pack"], r["model"], r["attempt"]) for r in rows()} if out.exists() else set()
    jobs = [(p, m, 200 + k) for k in range(repeats) for p in packs for m in models
            if (p, m, 200 + k) not in done][:max_calls]
    print(f"{len(jobs)} calls, {threads} at a time, {len(models)} models × {len(packs)} packs × {repeats}", flush=True)

    def go(job):
        r = one(*job)
        with _LOCK:
            with out.open("a", encoding="utf-8") as f:
                f.write(json.dumps(r, ensure_ascii=False) + "\n")
        print(f"{r['model']:42} {r['pack']}  {r['status']:10} score {r.get('score')}  "
              f"prec {r.get('precision')}  ref {r.get('ref_hit')}  fab {r.get('fabricated')}  "
              f"de {r.get('german')}  {r['seconds']}s  (+{r.get('failed_attempts', 0)} failed attempts)", flush=True)
        return r

    with ThreadPoolExecutor(threads) as pool:
        list(pool.map(go, jobs))
    return out


def rows() -> list[dict]:
    out = []
    for p in sorted(OUT.glob("runs-*.jsonl")):
        out += [json.loads(l) for l in p.read_text(encoding="utf-8").splitlines() if l.strip()]
    return out


def rank(rs: list[dict]) -> list[dict]:
    by: dict[str, list[dict]] = {}
    for r in rs:
        by.setdefault(r["model"], []).append(r)
    table = []
    for m, xs in by.items():
        scored = [x for x in xs if x.get("score") is not None]
        mean = lambda k: (round(sum(x[k] for x in scored if x.get(k) is not None)
                                / max(1, sum(1 for x in scored if x.get(k) is not None)), 3) if scored else None)
        table.append({"model": m, "calls": len(xs), "answered": len(scored),
                      "unreached": sum(1 for x in xs if x["status"] == "unreached"),
                      "invalid": sum(1 for x in xs if x["status"] in ("unparsed", "schema-invalid")),
                      "score": mean("score"), "precision": mean("precision"), "ref_hit": mean("ref_hit"),
                      "german": mean("german"), "fabricated": sum(x.get("fabricated") or 0 for x in xs),
                      "seconds": round(sum(x["seconds"] for x in scored) / len(scored), 1) if scored else None})
    for t in table:
        t["usable"] = round((t["score"] or 0) * t["answered"] / t["calls"], 3)
    # an unmeasured model ranks last; then the score, discounted by the calls it did not answer
    return sorted(table, key=lambda t: (t["answered"] == 0, -t["usable"]))


def report(write: bool) -> list[dict]:
    table = rank(rows())
    print(f"{'model':42} {'usable':>6} {'ans':>7} {'score':>6} {'prec':>5} {'ref':>5} {'de':>5} {'fab':>4} {'s':>6}")
    for t in table:
        print(f"{t['model']:42} {t['usable']:>6} {t['answered']:>3}/{t['calls']:<3} {t['score']!s:>6} {t['precision']!s:>5} "
              f"{t['ref_hit']!s:>5} {t['german']!s:>5} {t['fabricated']:>4} {t['seconds']!s:>6}")
    if write:
        top = [t for t in table if t["answered"]][:5]
        BEST.write_text(json.dumps({
            "measured": time.strftime("%Y-%m-%d"), "by": "scripts/route_bench.py",
            "task": "ask packs, scored by ask.verify and ask.score against Sonnet's placed lines (not gold)",
            "ask": [t["model"] for t in top], "table": top}, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        print(f"wrote {BEST.relative_to(ROOT)}: {[t['model'] for t in top]}")
    return table


def selftest() -> list[str]:
    fails = []
    rs = [{"model": "a", "status": "answered", "score": 0.9, "precision": 1, "ref_hit": 0.8, "german": 1,
           "fabricated": 1, "seconds": 3},
          {"model": "b", "status": "answered", "score": 0.6, "precision": 0.6, "ref_hit": 0.5, "german": 1,
           "fabricated": 0, "seconds": 3},
          {"model": "c", "status": "unreached", "seconds": 90},
          {"model": "d", "status": "answered", "score": 0.7, "precision": 0.7, "ref_hit": None, "german": 0,
           "fabricated": 0, "seconds": 3},
          {"model": "d", "status": "unreached", "seconds": 90}]
    order = [t["model"] for t in rank(rs)]
    # a: 0.9 over 1 of 1; b: 0.6; d: 0.7 over 1 of 2 = 0.35; c unmeasured, last
    if order != ["a", "b", "d", "c"]:
        fails.append(f"rank order {order}")
    return fails


def main(argv: list[str]) -> int:
    cmd, rest = (argv[0], argv[1:]) if argv else ("-h", [])

    def opt(name, default=None):
        return rest[rest.index(name) + 1] if name in rest else default
    if cmd == "selftest":
        fails = selftest()
        for f in fails:
            print("FAIL", f)
        print(f"route_bench selftest: {'held' if not fails else 'FAILED'}")
        return 1 if fails else 0
    if cmd == "run":
        models = candidates() if opt("--models", "all") == "all" else opt("--models").split(",")
        run(opt("--packs").split(","), models, int(opt("--repeats", 1)), int(opt("--max-calls", 50)),
            int(opt("--threads", 10)))
        return 0
    if cmd == "sessions":
        rs = sessions(rest[0].split(","))
        out = ROOT / "Plan" / "runs" / "ask" / f"card-ab-{time.strftime('%Y-%m-%d')}" / "rows.jsonl"
        out.parent.mkdir(parents=True, exist_ok=True)
        out.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rs), encoding="utf-8")
        for r in rs:
            print(f"{r['card']:4} {r['pack']:22} {r['file']:24} {r['status']:14} score {r['score']}  "
                  f"prec {r['precision']}  ref {r['ref_hit']}  fab {r['fabricated']}  splice {r['spliced']}  "
                  f"de {r['german']}  words {r['quote_words']}  claims {r['claims']}  {r['answerable']}")
        for card in sorted({r["card"] for r in rs}):
            xs = [r for r in rs if r["card"] == card]
            ok = [r for r in xs if r["score"] is not None]
            m = lambda k: round(sum(r[k] for r in ok if r[k] is not None) / max(1, sum(1 for r in ok if r[k] is not None)), 3)
            print(f"{card}: {len(ok)}/{len(xs)} scored, score {m('score')}, precision {m('precision')}, "
                  f"ref {m('ref_hit')}, fabricated {sum(r['fabricated'] or 0 for r in xs)}, "
                  f"spliced {sum(r['spliced'] for r in xs)}, german {m('german')}, quote words {m('quote_words')}")
        return 0
    if cmd == "report":
        report("--write" in rest)
        return 0
    print(__doc__)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
