#!/usr/bin/env python3
"""Does the retrieval bench measure what we use it for? Seven diagnostics of the bench itself, offline, no model.

    python3 Plan/runs/graph-lab-2026-09-30/eval-audit.py        # prints, and is saved as eval-audit.txt

The bench (`ask.py bench`, `graphrag.py bench`, `graphlab.py`) scores a retrieval change by how much of a case's *gold* a pack
holds, where a case is a conflict or question record and its gold is the file lines the record cites. This script asks of that
design, from the files alone:

  A  two measurements of one configuration, compared by a **paired** difference and not by two intervals laid side by side
  B  the **power**: the smallest true mean effect 24 cases can show
  C  whether the score depends on how many gold documents a case has
  D  whether the cases are independent of each other
  E  whether the gold is lines the wiki's pages already quote (a **circular** gold)
  F  whether every gold document is a read one, so that finding an unread document cannot score
  G  how much of a gold set the default pack could hold at all

Every number is a count over the repository's files; nothing here is a model's opinion. Standard library plus `scripts/graphlab.py`
and `scripts/ask.py`. The finding that follows from it is `Plan/concept/evaluation-audit_2026-09-30.md`.
"""
import json
import math
import statistics as st
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
import ask  # noqa: E402
import graphlab  # noqa: E402

BEFORE = ROOT / "Plan/runs/graph-lab-2026-09-30/ask-finders"            # the store after the scaled pass
AFTER = ROOT / "Plan/runs/hyperextract-backfill-2026-09-30/ask-finders"   # the store after the backfill's 14 runs


def rows(path: Path, key: str) -> dict:
    return {r["id"]: {"recall": r[key]} for r in json.loads(path.read_text(encoding="utf-8"))["rows"]}


def spearman(x: list, y: list) -> float:
    def rank(v):
        order = sorted(range(len(v)), key=lambda i: v[i])
        out = [0.0] * len(v)
        for pos, i in enumerate(order):
            out[i] = pos
        return out
    rx, ry = rank(x), rank(y)
    mx, my = st.mean(rx), st.mean(ry)
    return sum((a - mx) * (b - my) for a, b in zip(rx, ry)) / math.sqrt(sum((a - mx) ** 2 for a in rx) * sum((b - my) ** 2 for b in ry))


def main() -> int:
    print("A. The he-lines gain at 40 lines, before and after the backfill's 14 runs — the paired difference over the cases")
    for key, label in (("doc_recall", "document recall"), ("line_recall", "line recall")):
        p = graphlab.paired(rows(BEFORE / "he-lines-40-scaled.json", key), rows(AFTER / "he-lines-40-interim14.json", key))
        print(f"   {label:16} after minus before {p['mean']:+.4f}  90 % interval [{p['lo']:+.4f}, {p['hi']:+.4f}]  up {p['up']} / down {p['down']} / same {p['same']}")

    default = rows(AFTER / "default-interim14.json", "doc_recall")
    with_he = rows(AFTER / "he-lines-40-interim14.json", "doc_recall")
    effect = [with_he[k]["recall"] - default[k]["recall"] for k in default]
    n, sd = len(effect), st.stdev(effect)
    se = sd / math.sqrt(n)
    print(f"\nB. Power. The he-lines-40 effect per case: mean {st.mean(effect):+.3f}, sd {sd:.3f}, n {n}, standard error {se:.4f}")
    print(f"   The smallest true mean effect shown with 80 % power by a two-sided 90 % interval: about {2.49 * se:.3f} (2.49 standard errors).")
    print(f"   The measured gain is {st.mean(effect):+.3f}: it stands at the detection limit, and one of four limits (10, 20, 40, 80) was picked for it.")

    bench = json.loads((AFTER / "default-interim14.json").read_text(encoding="utf-8"))["rows"]
    gold_docs = [r["gold_docs"] for r in bench]
    recall = [r["doc_recall"] for r in bench]
    print(f"\nC. Spearman(gold documents of a case, the default pack's document recall) = {spearman(gold_docs, recall):+.2f} over {len(bench)} cases")
    print(f"   gold documents per case: min {min(gold_docs)}, median {st.median(gold_docs)}, max {max(gold_docs)}; "
          f"the pack holds {st.median([r['pack_docs'] for r in bench])} documents (median) within a budget of {ask.BUDGET:,} characters")

    cases = [c for c in ask.bench_cases() if c["gold"]]
    docs = {c["id"]: {d for d, _ in c["gold"]} for c in cases}
    ids = sorted(docs)
    jaccard = [len(docs[a] & docs[b]) / len(docs[a] | docs[b]) for i, a in enumerate(ids) for b in ids[i + 1:]]
    holders: dict[str, set] = {}
    for c in cases:
        for d, _ in c["gold"]:
            holders.setdefault(d, set()).add(c["id"])
    print(f"\nD. Independence. Mean pairwise Jaccard of the cases' gold document sets: {st.mean(jaccard):.2f} (median {st.median(jaccard):.2f}, max {max(jaccard):.2f})")
    print(f"   {len(holders)} gold documents, {sum(1 for v in holders.values() if len(v) >= 2)} of them gold in two or more cases; "
          f"the most shared is gold in {max(len(v) for v in holders.values())} of {len(ids)} cases")

    gold = {(d, l) for c in cases for d, l in c["gold"]}
    quoted = set()
    for folder in ("Wiki/candidates", "Wiki/chapters"):
        for page in (ROOT / folder).glob("*.md"):
            for m in ask.REF.finditer(page.read_text(encoding="utf-8")):
                quoted.add((m.group(1), int(m.group(2))))
    shares = [len(set(c["gold"]) & quoted) / len(c["gold"]) for c in cases]
    print(f"\nE. Circularity. Of {len(gold)} gold lines, {len(gold & quoted)} ({len(gold & quoted) / len(gold):.0%}) are lines a term or chapter page also quotes; "
          f"per case the median is {st.median(shares):.0%} (min {min(shares):.0%}, max {max(shares):.0%})")
    print("   A finder that returns the wiki's own verified quotations (`graph-evidence`) is rewarded for returning what the records already cite.")

    read = {p.stem for p in (ROOT / "Sources" / "terms").glob("*.md") if p.stem != "README"}
    gd = {d for d, _ in gold}
    print(f"\nF. Discovery. {len(gd & read)} of the {len(gd)} gold documents are read ones ({len(read)} documents have a census): "
          f"a case's gold is {st.median([len(docs[i]) for i in ids]):.1f} documents (median), {st.median([len(docs[i]) for i in ids]) / len(read):.0%} of the read corpus.")
    print("   No unread document is gold in any case, so finding a relevant unread document cannot score (`entity-unread` measures nothing here).")

    cap = [min(1.0, r["pack_docs"] / r["gold_docs"]) for r in bench]
    over = sum(1 for r in bench if r["gold_docs"] > r["pack_docs"])
    print(f"\nG. Ceiling. A pack of {st.median([r['pack_docs'] for r in bench])} documents (median) caps a case's document recall at min(1, pack documents / gold documents): "
          f"the mean cap is {st.mean(cap):.2f} against a default of {st.mean(recall):.2f}, and in {over} of {len(bench)} cases the gold has more documents than the pack holds.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
