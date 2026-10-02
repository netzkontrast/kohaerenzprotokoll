"""How the `ask` pack spends its budget, and four ways to spend it better — offline, no model.

On the author's „Überlege wie die ask packs optimiert werden können" (2026-10-01). `ask.build_pack` routes a
question to anchors (file lines found by five finders), groups them by document, ranks the documents, widens each
anchor to its paragraph, caps a document at 60 lines **in file order**, and adds whole document blocks until
60 000 characters — a block that does not fit is cut whole. This script takes the route once per case and replays
the packing step under variants, so every variant sees the same anchors:

- `current`  — `build_pack`'s packing, reimplemented; checked against `build_pack`'s own `shown` (fidelity)
- `body`     — anchors on a frontmatter line dropped (defect 1 of the session README)
- `ranked`   — when a document has more anchored lines than fit in 60, the strongest anchors are kept (more
               finders on the line first, then graph evidence, then file order) instead of the earliest
- `fill`     — a document block that does not fit is trimmed to what does, strongest spans first, instead of cut
- `all`      — body + ranked + fill

Measured on the frozen cases (`Plan/eval/retrieval-cases-v1.json`, the case's own record removed from the graph as
`ask.py bench` does) at three budgets: gold lines sent, gold documents sent, characters used. Two gold views:
**all** gold lines, and **unquoted** — gold lines no wiki page quotes, the 8 % the graph-evidence finder cannot
reach by construction (evaluation audit §0). A gold line in the pack is a line *sent*, not a line an answer used.

    .venv-graphqlite/bin/python Plan/runs/architecture-session-2026-10-01/packs/pack_variants.py
"""

from __future__ import annotations

import json
import random
import sys
import time
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
import ask  # noqa: E402
import askdb  # noqa: E402
import graph as kg  # noqa: E402
import graphrag  # noqa: E402
import subject  # noqa: E402

BUDGETS = (15_000, 30_000, 60_000)
VARIANTS = ("current", "body", "ranked", "fill", "all")
STRENGTH = {"graph-evidence": 0, "co-mention": 1, "parallel": 2, "entity-unread": 3, "bm25-lines": 4, "he-lines": 5}


def spans_of(s, doc: str, lines: list[int]) -> list[list[int]]:
    """`build_pack`'s widening: the paragraph if short, else ±WINDOW; neighbours merged (lines in given order)."""
    out = []
    for line in lines:
        para = s.paragraph(doc, line)
        lo, hi = (para if para and para[1] - para[0] <= 2 * ask.PER_PARA else (line - ask.WINDOW, line + ask.WINDOW))
        lo, hi = max(1, min(lo, line - 1)), max(hi, line + 1)
        out.append([lo, hi])
    return out


def merge(spans: list[list[int]]) -> list[list[int]]:
    out = []
    for lo, hi in sorted(spans):
        if out and lo <= out[-1][1] + 1:
            out[-1][1] = max(out[-1][1], hi)
        else:
            out.append([lo, hi])
    return out


def doc_rows(s, doc: str, anchors: dict[int, set], ranked: bool) -> list[tuple[int, str]]:
    """The lines one document contributes, at most PER_DOC; in file order, or strongest anchors first."""
    if not ranked:
        rows, n = [], 0
        for lo, hi in merge(spans_of(s, doc, sorted(anchors))):
            for number, text in s.window(doc, lo, hi):
                if n >= ask.PER_DOC:
                    break
                rows.append((number, text))
                n += 1
            rows.append((None, "…"))   # build_pack writes one after every span, even past the cap
        return rows
    order = sorted(anchors, key=lambda n: (-len(anchors[n]), min(STRENGTH[f] for f in anchors[n]), n))
    keep: set[int] = set()
    for lo, hi in spans_of(s, doc, order):
        new = [n for n in range(lo, hi + 1) if n not in keep]
        if len(keep) + len(new) > ask.PER_DOC:
            new = new[:ask.PER_DOC - len(keep)]
        keep.update(new)
        if len(keep) >= ask.PER_DOC:
            break
    got = []
    for lo, hi in merge([[n, n] for n in keep]):
        got += s.window(doc, lo, hi)
    return got


def block(doc: str, rows, head: str) -> str:
    if any(n is None for n, _ in rows):   # the file-order path: build_pack's own text
        return head + "\n".join("…" if n is None else f"L{n}: {t}" for n, t in rows) + "\n"
    out, prev = [], None
    for number, text in rows:
        if prev is not None and number != prev + 1:
            out.append("…")
        out.append(f"L{number}: {text}")
        prev = number
    return head + "\n".join(out + ["…"]) + "\n"


WHEN, TIERS = ask.dates(), {}


def pack(s, r, budget: int, variant: str, offsets: dict[str, int]) -> dict:
    if not TIERS:
        TIERS.update({x["slug"]: x.get("tier", "") for x in askdb.manifest()})
    body = variant in ("body", "all")
    ranked = variant in ("ranked", "all")
    fill = variant in ("fill", "all")
    per_line: dict[str, dict[int, set]] = {}
    for a in r["anchors"]:
        if body and a["line"] < offsets.get(a["doc"], 1):
            continue
        per_line.setdefault(a["doc"], {}).setdefault(a["line"], set()).add(a["finder"])
    used, shown, cut, trimmed = 0, {}, [], []
    for d in r["docs"]:
        anchors = per_line.get(d["doc"])
        if not anchors:
            continue
        read = "gelesen" if d["doc"] in r["evidence_docs"] else "ungelesen"
        head = (f"\n### `{d['doc']}` — {WHEN.get(d['doc']) or 'undatiert'}, {TIERS.get(d['doc'], '')}, {read}; "
                f"gefunden von: {', '.join(sorted(d['finders']))}\n\n")
        rows = doc_rows(s, d["doc"], anchors, ranked)
        text = block(d["doc"], rows, head)
        if used + len(text) <= budget:
            used += len(text)
            shown[d["doc"]] = [n for n, _ in rows if n is not None]
            continue
        if not fill:
            cut.append(d["doc"])
            continue
        # trim: strongest anchors first, until the remaining budget is full
        room = budget - used - len(head) - 2
        if room < 200:
            cut.append(d["doc"])
            continue
        strong = sorted(anchors, key=lambda n: (-len(anchors[n]), min(STRENGTH[f] for f in anchors[n]), n))
        keep, size = [], 0
        for lo, hi in spans_of(s, d["doc"], strong):
            add = [(n, t) for n, t in s.window(d["doc"], lo, hi) if n not in {k for k, _ in keep}]
            cost = sum(len(t) + 8 for _, t in add)
            if size + cost > room:
                continue
            keep += add
            size += cost
        if not keep:
            cut.append(d["doc"])
            continue
        keep.sort()
        text = block(d["doc"], keep, head)
        used += len(text)
        shown[d["doc"]] = [n for n, _ in keep]
        trimmed.append(d["doc"])
    return {"shown": shown, "used": used, "cut": cut, "trimmed": trimmed}


def interval(diffs: list[float]) -> list[float]:
    rnd = random.Random(7)
    means = sorted(sum(rnd.choice(diffs) for _ in diffs) / len(diffs) for _ in range(10_000))
    return [round(means[500], 3), round(means[9500], 3)]


def main() -> dict:
    frozen = json.loads((ROOT / "Plan" / "eval" / "retrieval-cases-v1.json").read_text(encoding="utf-8"))
    s, g = askdb.Store(), kg.build()
    offsets = {}
    for c in frozen["cases"]:
        for d, _ in c["gold"]:
            offsets.setdefault(d, subject.document(d).offset)
    out = {"cases": [], "fidelity": []}
    started = time.time()
    for c in frozen["cases"]:
        if not c["gold"]:
            continue
        iso = graphrag.without(g, c["key"])
        quoted = {(e["doc"], e["line"]) for rows in iso["evidence"].values() for e in rows}
        r = ask.route(c["question"], "position", s, iso)
        for a in r["anchors"]:
            if a["doc"] not in offsets:
                try:
                    offsets[a["doc"]] = subject.document(a["doc"]).offset
                except KeyError:
                    offsets[a["doc"]] = 1
        gold = {tuple(x) for x in c["gold"]}
        unquoted = {x for x in gold if x not in quoted}
        row = {"id": c["id"], "gold": len(gold), "unquoted": len(unquoted),
               "frontmatter_anchors": sum(1 for a in r["anchors"] if a["line"] < offsets.get(a["doc"], 1)),
               "anchors": len(r["anchors"]), "docs": len(r["docs"]), "v": {}}
        _, meta = ask.build_pack(c["question"], "position", ask.BUDGET, s, iso)
        mine = pack(s, r, ask.BUDGET, "current", offsets)
        out["fidelity"].append({"id": c["id"], "same_docs": set(meta["shown"]) == set(mine["shown"]),
                                "same_lines": all(set(meta["shown"][d]) == set(mine["shown"].get(d, ()))
                                                  for d in meta["shown"])})
        for b in BUDGETS:
            for v in VARIANTS:
                p = pack(s, r, b, v, offsets)
                sent = {(d, n) for d, ns in p["shown"].items() for n in ns}
                row["v"][f"{v}@{b}"] = {
                    "line": round(len(gold & sent) / len(gold), 3),
                    "unquoted": round(len(unquoted & sent) / len(unquoted), 3) if unquoted else None,
                    "doc": round(len({d for d, _ in gold} & set(p["shown"])) / len({d for d, _ in gold}), 3),
                    "chars": p["used"], "docs": len(p["shown"]), "cut": len(p["cut"]), "trimmed": len(p["trimmed"])}
        out["cases"].append(row)
        print(f"{c['id']:4} anchors {row['anchors']:4} (frontmatter {row['frontmatter_anchors']:3}) docs {row['docs']:3}  "
              + "  ".join(f"{v} {row['v'][f'{v}@30000']['line']:.3f}" for v in VARIANTS), flush=True)
    summary = {}
    for b in BUDGETS:
        for v in VARIANTS:
            k = f"{v}@{b}"
            vals = [x["v"][k] for x in out["cases"]]
            base = [x["v"][f"current@{b}"] for x in out["cases"]]
            diffs = [a["line"] - z["line"] for a, z in zip(vals, base)]
            uq = [(a["unquoted"], z["unquoted"]) for a, z in zip(vals, base) if a["unquoted"] is not None]
            summary[k] = {"line": round(sum(x["line"] for x in vals) / len(vals), 3),
                          "unquoted": round(sum(a for a, _ in uq) / len(uq), 3) if uq else None,
                          "doc": round(sum(x["doc"] for x in vals) / len(vals), 3),
                          "chars": round(sum(x["chars"] for x in vals) / len(vals)),
                          "cut": round(sum(x["cut"] for x in vals) / len(vals), 1),
                          "trimmed": round(sum(x["trimmed"] for x in vals) / len(vals), 1)}
            if v != "current":
                summary[k].update({"line_diff": round(sum(diffs) / len(diffs), 3), "interval_90": interval(diffs),
                                   "better": sum(d > 0 for d in diffs), "worse": sum(d < 0 for d in diffs),
                                   "unquoted_diff": round(sum(a - z for a, z in uq) / len(uq), 3) if uq else None})
    out["summary"] = summary
    out["seconds"] = round(time.time() - started)
    out["frozen_sha256"] = frozen["sha256"]
    (HERE / "pack_variants.json").write_text(json.dumps(out, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    return out


if __name__ == "__main__":
    res = main()
    fid = res["fidelity"]
    print(f"\nfidelity against build_pack: same documents {sum(f['same_docs'] for f in fid)}/{len(fid)}, "
          f"same lines {sum(f['same_lines'] for f in fid)}/{len(fid)}")
    for k, v in res["summary"].items():
        extra = (f"  Δ {v['line_diff']:+.3f} {v['interval_90']} +{v['better']}/-{v['worse']}  unquoted Δ {v['unquoted_diff']}"
                 if "line_diff" in v else "")
        print(f"{k:14} line {v['line']:.3f} unquoted {v['unquoted']} doc {v['doc']:.3f} chars {v['chars']:6} "
              f"cut {v['cut']:4} trimmed {v['trimmed']:4}{extra}")
