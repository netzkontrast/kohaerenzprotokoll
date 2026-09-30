"""The sampling frame and the sample for the quality audit of documents 32–51.

Every reading section, record entry and chapter or overview reading these
documents added is split into claims — a paragraph or bullet, the unit a reader
writes. A claim is sampled stratified by document and kind with a fixed seed,
uncited claims oversampled because no check can see them. For each sampled claim
the packet carries the cited lines ±1, read from the document by code.

    python3 Plan/runs/quality-sample-2026-09-29/frame.py      # writes frame.json, sample.jsonl, packets/
"""
import glob, json, random, re
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
OUT = Path(__file__).resolve().parent
SEED = 20260929
order = sorted((p.name[:-3] for p in (ROOT / "Sources/terms").glob("*.md")))
ranked = {}
for path in sorted(glob.glob(str(ROOT / "Wiki/compare/reconcile-*.md"))):
    m = re.match(r".*reconcile-(\d+)-(.+)\.md", path)
    ranked.setdefault(m.group(2), int(m.group(1)))
order.sort(key=lambda s: ranked.get(s, 0))
number = {s: i + 1 for i, s in enumerate(order)}
DOCS = {s for s, n in number.items() if 32 <= n <= 51}
HEAD = re.compile(r"^## (?:Readings? — |\d{4}-\d{2}-\d{2} — )`([a-z0-9-]+)`")
CITE = re.compile(r"\^\[([a-z0-9-]+)\.md:L(\d+)(?:[–-]L?(\d+))?\]")


def kind(f):
    return ("record" if "/conflicts/" in f or "/questions/" in f else
            "chapter" if "/chapters/" in f else "overview" if "/overview/" in f else "term")


claims = []
for f in sorted(glob.glob(str(ROOT / "Wiki/**/*.md"), recursive=True)):
    lines = Path(f).read_text(encoding="utf-8").split("\n")
    cur = None
    buf, start = [], 0
    def flush():
        if cur and buf and "".join(buf).strip():
            text = "\n".join(buf).strip()
            claims.append({"file": str(Path(f).relative_to(ROOT)), "line": start + 1, "doc": cur,
                           "n": number[cur], "kind": kind(f), "text": text,
                           "cited": bool(CITE.search(text))})
    for i, line in enumerate(lines):
        m = HEAD.match(line)
        if line.startswith("## "):
            flush(); buf = []
            cur = None
            if m:
                slug = m.group(1)
                full = next((d for d in DOCS if d.startswith(slug) or slug.startswith(d)), None)
                cur = full
            continue
        if cur is None:
            continue
        if not line.strip() or line.startswith("- ") or line.startswith("Title:") or line.startswith("Position:"):
            flush(); buf = []; start = i
            if line.strip():
                buf = [line]; start = i
            continue
        if not buf:
            start = i
        buf.append(line)
    flush()

frame = {"documents": sorted(DOCS, key=number.get), "claims": len(claims),
         "by_kind": {k: sum(1 for c in claims if c["kind"] == k) for k in ("term", "record", "chapter", "overview")},
         "uncited": sum(1 for c in claims if not c["cited"])}
(OUT / "frame.json").write_text(json.dumps(frame, indent=1), encoding="utf-8")

rng = random.Random(SEED)
sample = []
for d in sorted(DOCS, key=number.get):
    mine = [c for c in claims if c["doc"] == d]
    for k, want in (("term", 3), ("record", 1), ("chapter", 1), ("overview", 1)):
        pool = [c for c in mine if c["kind"] == k and c["cited"]]
        sample += rng.sample(pool, min(want, len(pool)))
    unc = [c for c in mine if not c["cited"] and len(c["text"]) > 60]
    sample += rng.sample(unc, min(1, len(unc)))


def lines_of(slug):
    return (ROOT / f"Sources/drive/{slug}.md").read_text(encoding="utf-8").split("\n")


(OUT / "packets").mkdir(exist_ok=True)
with (OUT / "sample.jsonl").open("w", encoding="utf-8") as fh:
    for i, c in enumerate(sample, 1):
        c["id"] = f"S{i:03d}"
        fh.write(json.dumps({k: c[k] for k in ("id", "file", "line", "doc", "n", "kind", "cited")}, ensure_ascii=False) + "\n")
        parts = [f"## {c['id']} — {c['file']}:{c['line']} ({c['kind']}, document {c['n']} `{c['doc']}`)\n",
                 "### The claim as written on the page\n", c["text"], "\n### The cited lines, ±1 (file line numbers)\n"]
        for m in CITE.finditer(c["text"]):
            slug, a = m.group(1), int(m.group(2))
            b = int(m.group(3) or a)
            src = lines_of(slug) if (ROOT / f"Sources/drive/{slug}.md").exists() else []
            parts.append(f"`{slug}` L{a}{'–L'+str(b) if b != a else ''}:")
            for k in range(max(1, a - 1), min(len(src), min(b, a + 6) + 1) + 1):
                parts.append(f"    {k}| {src[k-1][:600]}")
        (OUT / "packets" / f"{c['id']}.md").write_text("\n".join(parts) + "\n", encoding="utf-8")
print(json.dumps(frame["by_kind"]), "claims", frame["claims"], "uncited", frame["uncited"], "sampled", len(sample))
