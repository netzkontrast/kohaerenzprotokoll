"""What step 6's sample paid, and what it yielded, per document and per category.

Decision 015, item 5 — and the review of 2026-09-30, which found that this
script counted phase durations only: „Was bringt welcher Aufwand?" stayed open.
It now joins four sources, each named where it is printed:

- **yield** — each document's reconcile.json and the wiki: candidates, decided
  by lookup, sent to judgement, new pages, pages, record entries and chapter
  pages given a reading, sweep readings;
- **cost, measured** — `Plan/runs/reader-lab-2026-09-30/transcripts.json`, the
  readers' own transcripts: API calls, minutes, cache reads and the cost proxy
  `transcripts.py` defines. Every run of a document is summed (a stopped run and
  the run that finished it);
- **cost, as reported** — `run.jsonl` reader rows: what the Agent notification
  said, the size of the last call and not the consumption;
- **corrections** — every `corrections.jsonl` row naming the document
  (`runlog.py correct … --document`), by class; a row naming none is counted
  apart, as not attributed.

A value no source recorded prints as `-`, never as 0 (P15). Readings cost is
per batch; `--batch <run>` adds a batch's readers, shared across its documents
by their number of reading files, and says that it is an allocation.
Standard library, reads only.

    python3 Plan/runs/step6-2026-09-29/yield.py [--batch <run> ...]
"""
import glob
import json
import re
import sys
from collections import Counter, defaultdict
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
RUNS = ROOT / "Plan" / "runs"
SAMPLE = json.loads((Path(__file__).parent / "sample.json").read_text(encoding="utf-8"))
TRANSCRIPTS = RUNS / "reader-lab-2026-09-30" / "transcripts.json"
HEAD = re.compile(r"^## (?:Readings? — |\d{4}-\d{2}-\d{2} — )`([a-z0-9-]+)`", re.M)


def jsonl(path):
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def sections(slug):
    pages, records, chapters = set(), set(), set()
    for folder, bucket in (("Wiki/candidates", pages), ("Wiki/overview", pages),
                           ("Wiki/conflicts", records), ("Wiki/questions", records),
                           ("Wiki/chapters", chapters)):
        for f in glob.glob(str(ROOT / folder / "*.md")):
            for m in HEAD.finditer(Path(f).read_text(encoding="utf-8")):
                # exact: a prefix match gave three documents whose slug begins
                # `kohaerenz-protokoll` the 60 readings of the document of that name
                if m.group(1) == slug:
                    bucket.add(Path(f).stem)
    return pages, records, chapters


def phases(slug):
    out = {}
    for e in jsonl(RUNS / slug / "run.jsonl"):
        if e.get("event") in ("start", "end"):
            out.setdefault(e["phase"], {})[e["event"]] = datetime.fromisoformat(e["at"])
    return {p: round((v["end"] - v["start"]).total_seconds()) for p, v in out.items()
            if "start" in v and "end" in v} or "not recorded"


def main(argv):
    batches = [argv[i + 1] for i, a in enumerate(argv) if a == "--batch" and i + 1 < len(argv)]
    transcripts = json.loads(TRANSCRIPTS.read_text(encoding="utf-8")) if TRANSCRIPTS.exists() else []
    by_slug = defaultdict(list)
    for t in transcripts:
        if t.get("role", "document-reader") == "document-reader":
            by_slug[t["slug"]].append(t)
    corrections = defaultdict(Counter)
    unattributed = Counter()
    for f in RUNS.glob("*/corrections.jsonl"):
        for row in jsonl(f):
            if row.get("document"):
                corrections[row["document"]][row["class"]] += 1
            else:
                unattributed[f.parent.name] += 1
    sweep = jsonl(RUNS / "sweep.jsonl")
    agent_cost = {t["agent"]: t for t in transcripts}

    # a batch's readers, shared by reading files per document
    shared = defaultdict(float)
    notes = []
    for batch in batches:
        readers = [e for e in jsonl(RUNS / batch / "run.jsonl") if e.get("event") == "reader"]
        measured = [agent_cost[e["agent"]]["cost"] for e in readers if e.get("agent") in agent_cost]
        files = Counter(f.name.split("--", 1)[1][:-3] for f in (RUNS / batch / "readings").glob("*--*.md"))
        total = sum(measured)
        for doc, n in files.items():
            shared[doc] += total * n / max(sum(files.values()), 1)
        notes.append(f"{batch}: {len(readers)} readers, {len(measured)} with a transcript, cost {total:,.0f}, "
                     f"shared over {sum(files.values())} reading files of {len(files)} documents")

    rows = []
    for s in SAMPLE:
        slug = s["slug"]
        rj = RUNS / slug / "reconcile.json"
        j = json.loads(rj.read_text(encoding="utf-8")) if rj.exists() else {}
        pc = j.get("pre_classification", {})
        pages, records, chapters = sections(slug)
        runs = by_slug.get(slug, [])
        reported = [e for e in jsonl(RUNS / slug / "run.jsonl") if e.get("event") == "reader"]
        rows.append(dict(
            category=s["category"], slug=slug, kb=s["chars"] // 1000,
            candidates=pc.get("candidates"), lookup=pc.get("decided_by_lookup"),
            judgement=pc.get("needs_judgement"),
            new_pages=len(j.get("new_terms", [])) if j else None,
            pages=len(pages), records=len(records), chapters=len(chapters),
            sweep=sum(1 for x in sweep if x.get("document") == slug and x.get("decision") == "reading"),
            runs=len(runs), calls=sum(t["calls"] for t in runs) or None,
            minutes=round(sum(t.get("minutes", 0) for t in runs), 1) or None,
            cache_read=sum(t["tokens"]["cache_read"] for t in runs) or None,
            cost=sum(t["cost"] for t in runs) or None,
            readings_cost=shared.get(slug),
            reported=sum(e["tokens"] for e in reported) or None,
            corrections=sum(corrections[slug].values()) if slug in corrections else None,
            classes=dict(corrections.get(slug, {})),
            phases=phases(slug)))

    def v(x, fmt="{:,}"):
        return "-" if x is None else fmt.format(x)

    print("YIELD — from reconcile.json and the wiki (- : no reconciliation yet)")
    print(f"{'category':20} {'document':40} {'kB':>3} {'cand':>5} {'look':>5} {'judg':>5} {'new':>4} "
          f"{'pages':>5} {'rec':>4} {'chap':>4} {'swp':>4}")
    for r in rows:
        print(f"{r['category']:20} {r['slug'][:40]:40} {r['kb']:3d} {v(r['candidates']):>5} {v(r['lookup']):>5} "
              f"{v(r['judgement']):>5} {v(r['new_pages']):>4} {r['pages']:5d} {r['records']:4d} "
              f"{r['chapters']:4d} {r['sweep']:4d}")
    print("\nCOST — extraction measured from transcripts (every run of the document summed); "
          "reported = the Agent notification's last-call size")
    print(f"{'document':40} {'runs':>4} {'calls':>5} {'min':>6} {'cache reads':>12} {'cost proxy':>11} "
          f"{'readings':>10} {'reported':>9} {'corr':>4}")
    for r in rows:
        print(f"{r['slug'][:40]:40} {r['runs']:4d} {v(r['calls']):>5} {v(r['minutes']):>6} {v(r['cache_read']):>12} "
              f"{v(r['cost'], '{:,.0f}'):>11} {v(r['readings_cost'], '{:,.0f}'):>10} {v(r['reported']):>9} "
              f"{v(r['corrections']):>4}")
    for n in notes:
        print(f"  batch {n}")
    if unattributed:
        print("  corrections naming no document: " + ", ".join(f"{k} {n}" for k, n in unattributed.items()))
    print("\nPER CATEGORY — two documents each; readings per 1M of cost proxy where both are known")
    cats = defaultdict(lambda: Counter())
    for r in rows:
        c = cats[r["category"]]
        c["readings"] += r["pages"] + r["records"] + r["chapters"]
        c["kb"] += r["kb"]
        if r["cost"] is not None:
            c["cost"] += r["cost"] + (r["readings_cost"] or 0)
            c["costed"] += 1
    for name, c in cats.items():
        per = f"{1e6 * c['readings'] / c['cost']:.1f}" if c["cost"] and c["readings"] else "-"
        print(f"  {name:20} readings {c['readings']:3d}  kB {c['kb']:4d}  cost {c['cost']:>11,.0f} "
              f"({c['costed']} of 2 costed)  readings per 1M: {per}")
    print("\nEXTRACTION PHASES (seconds) per document, from run.jsonl:")
    for r in rows:
        print(f"  {r['slug'][:44]:44} {r['phases']}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
