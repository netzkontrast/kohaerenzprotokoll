"""What step 6's sample paid, per document and per category (decision 015, item 5).

Reads each sampled document's reconcile.json, its run log and the wiki, and
prints: candidates, decided by lookup, sent to judgement, new pages, pages given
a reading, record entries, chapter readings, sweep readings, and what the
extraction and the readings cost where run.jsonl recorded it. Standard library,
reads only.

    python3 Plan/runs/step6-2026-09-29/yield.py
"""
import glob, json, re
from datetime import datetime
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
SAMPLE = json.loads((Path(__file__).parent / "sample.json").read_text(encoding="utf-8"))
HEAD = re.compile(r"^## (?:Readings? — |\d{4}-\d{2}-\d{2} — )`([a-z0-9-]+)`", re.M)


def sections(slug):
    pages, records, chapters = set(), set(), set()
    for folder, bucket in (("Wiki/candidates", pages), ("Wiki/overview", pages),
                           ("Wiki/conflicts", records), ("Wiki/questions", records),
                           ("Wiki/chapters", chapters)):
        for f in glob.glob(str(ROOT / folder / "*.md")):
            for m in HEAD.finditer(Path(f).read_text(encoding="utf-8")):
                if slug.startswith(m.group(1)) or m.group(1).startswith(slug):
                    bucket.add(Path(f).stem)
    return pages, records, chapters


def phases(slug):
    f = ROOT / "Plan" / "runs" / slug / "run.jsonl"
    if not f.exists():
        return "not recorded"
    ev = [json.loads(l) for l in f.read_text(encoding="utf-8").splitlines() if l.strip()]
    out = {}
    for e in ev:
        if e.get("event") in ("start", "end"):
            out.setdefault(e["phase"], {})[e["event"]] = datetime.fromisoformat(e["at"])
    return {p: round((v["end"] - v["start"]).total_seconds()) for p, v in out.items() if "start" in v and "end" in v}


sweep = [json.loads(l) for l in (ROOT / "Plan/runs/sweep.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
rows = []
for s in SAMPLE:
    slug = s["slug"]
    rj = ROOT / "Plan" / "runs" / slug / "reconcile.json"
    j = json.loads(rj.read_text(encoding="utf-8")) if rj.exists() else {}
    pc = j.get("pre_classification", {})
    pages, records, chapters = sections(slug)
    rows.append(dict(category=s["category"], slug=slug, chars=s["chars"],
                     candidates=pc.get("candidates"), lookup=pc.get("decided_by_lookup"),
                     judgement=pc.get("needs_judgement"), new_pages=len(j.get("new_terms", [])) if j else None,
                     judgements=len(j.get("judgements", [])) if j else None,
                     pages=len(pages), records=len(records), chapters=len(chapters),
                     sweep_readings=sum(1 for x in sweep if x.get("document") == slug and x.get("decision") == "reading"),
                     phases=phases(slug)))
print(f"{'category':20s} {'document':44s} {'kB':>4} {'cand':>5} {'look':>5} {'judg':>5} {'new':>4} {'J':>3} {'pages':>5} {'rec':>4} {'chap':>4} {'swp':>4}")
for r in rows:
    print(f"{r['category']:20s} {r['slug'][:44]:44s} {r['chars']//1000:4d} {r['candidates']!s:>5} {r['lookup']!s:>5} "
          f"{r['judgement']!s:>5} {r['new_pages']!s:>4} {r['judgements']!s:>3} {r['pages']:5d} {r['records']:4d} "
          f"{r['chapters']:4d} {r['sweep_readings']:4d}")
print("\nper category (two documents each): pages given a reading, record entries, chapter readings")
cats = {}
for r in rows:
    c = cats.setdefault(r["category"], [0, 0, 0, 0])
    c[0] += r["pages"]; c[1] += r["records"]; c[2] += r["chapters"]; c[3] += r["chars"]
for c, (p, rec, ch, chars) in cats.items():
    print(f"  {c:20s} pages {p:3d}  records {rec:3d}  chapters {ch:3d}  per 10 kB of text: {10000 * (p + rec) / chars:.1f} readings")
print("\nextraction phases (seconds) per document, from run.jsonl:")
for r in rows:
    print(f"  {r['slug'][:44]:44s} {r['phases']}")
