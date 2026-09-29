"""Where the reading pipeline spends its effort — measured over every read document.

Standard library only; reads the repository and writes nothing. Every number in
Plan/concept/pipeline-optimization_2026-09-29.md comes from this output
(measure.txt beside it) or from a command named there.

    python3 Plan/runs/pipeline-2026-09-29/measure.py > Plan/runs/pipeline-2026-09-29/measure.txt

What it counts, section by section:

  1  the always-loaded context: CLAUDE.md and NOW.md, and how much of each is
     per-document history that Wiki/compare/ already records
  2  what each reconciliation yielded: candidates, lookup, judgement, new pages,
     readings, sweep hits (reconcile.json, sweep.jsonl)
  3  what a wiki page is made of: other documents' readings against the lead,
     the differences and the open questions a reader must keep true
  4  what a reader loads to add one document's readings: the pages it touches,
     whole, against a digest of them; the records and chapter pages
  5  batching: the pages several documents touch, loaded once rather than once
     per document
  6  a NEGATIVE result: giving a reader only the lines around a page's surfaces
     would have missed a third of the lines the committed readings cite
  7  a NEGATIVE result: the unread corpus is not copies of the read one
  8  claims no check reads: absence counts on pages, and comparisons with other
     documents inside a document's reading
"""

from __future__ import annotations

import glob
import json
import os
import re
import unicodedata
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
os.chdir(ROOT)


def sections(text: str) -> list[tuple[str, str]]:
    parts = re.split(r"(?m)^(## .*)$", text)
    return [("_head", parts[0])] + [(parts[i], parts[i + 1]) for i in range(1, len(parts), 2)]


def kind(heading: str) -> str:
    if heading == "_head":
        return "lead"
    if heading.startswith("## Reading"):
        return "reading"
    if "differ" in heading.lower():
        return "differ"
    if heading.startswith("## Open"):
        return "open"
    if "Raw qmd" in heading:
        return "qmd"
    if "Candidate sources" in heading:
        return "candidate-sources"
    if "Questions for this chapter" in heading:
        return "chapter-questions"
    if "What this chapter" in heading:
        return "about"
    return "other"


def digest_size(text: str) -> int:
    """What a reader needs to keep a page true: everything but the readings'
    bodies (their headings stay, one line each) and the chapter navigation that
    code writes."""
    size = 0
    for heading, body in sections(text):
        k = kind(heading)
        if k == "reading":
            size += len(heading) + 1
        elif k in ("qmd", "candidate-sources"):
            continue
        else:
            size += len(heading) + len(body)
    return size


def documents() -> list[tuple[int, str]]:
    """(document number, slug) in reading order: every document with a census,
    ordered by its reconciliation record. The first document's comparison
    predates the numbered records (Wiki/compare/001-…) and one document has two
    records, so the number is the position, not the record's."""
    order = [p.name[:-3] for p in sorted(Path("Sources/terms").glob("*.md"))]
    ranked = {}
    for path in sorted(glob.glob("Wiki/compare/reconcile-*.md")):
        m = re.match(r".*reconcile-(\d+)-(.+)\.md", path)
        ranked.setdefault(m.group(2), int(m.group(1)))
    order.sort(key=lambda slug: ranked.get(slug, 0))
    missing = [slug for slug in order if slug not in ranked]
    if len(missing) > 1:
        raise SystemExit(f"censuses with no reconciliation record: {missing}")
    return [(i + 1, slug) for i, slug in enumerate(order)]


def reconcile(slug: str) -> dict:
    p = Path(f"Plan/runs/{slug}/reconcile.json")
    return json.loads(p.read_text(encoding="utf-8")) if p.exists() else {}


def pages_read(slug: str) -> set[str]:
    out = set()
    for r in reconcile(slug).get("new_readings", []):
        if isinstance(r, dict) and r.get("page"):
            out.add(r["page"])
        elif isinstance(r, str):
            out.add(r)
    return out


def size(path: str) -> int:
    return os.path.getsize(path) if os.path.exists(path) else 0


def page_file(page: str) -> str:
    return f"Wiki/candidates/{page}.md"


def records() -> dict[str, str]:
    out = {}
    for f in glob.glob("Wiki/conflicts/*.md") + glob.glob("Wiki/questions/*.md"):
        m = re.match(r"([cq]\d+)", os.path.basename(f))
        if m:
            out[m.group(1).upper()] = f
    return out


def chapter_files(slug: str) -> list[str]:
    ch = reconcile(slug).get("chapters", {})
    listed = ch.get("readings_on", []) if isinstance(ch, dict) else ch
    out = []
    for c in listed or []:
        m = re.search(r"(\d+)", str(c))
        if m and os.path.exists(f"Wiki/chapters/kap-{int(m.group(1)):02d}.md"):
            out.append(f"Wiki/chapters/kap-{int(m.group(1)):02d}.md")
    return out


def section_1() -> None:
    print("## 1 · The always-loaded context\n")
    claude = Path("CLAUDE.md").read_text(encoding="utf-8")
    now = Path("NOW.md").read_text(encoding="utf-8")
    # the per-document table and the paragraphs after it, one per document read,
    # up to the judgements line; a missing boundary is reported, never read as 0
    s = claude.find("| document | new terms |")
    e = claude.find("`Plan/runs/judgements.jsonl` holds")
    if not 0 <= s < e:
        raise SystemExit("CLAUDE.md: the per-document history's boundaries were not found")
    history = e - s
    install = 0
    for heading, body in re.findall(r"(?ms)^(## Installing anything)$(.*?)(?=^## )", claude):
        install = len(heading) + len(body)
    prev = sum(len(h) + len(b) for h, b in
               [(h, b) for h, b in re.findall(r"(?ms)^(#{2,3} .*?)$(.*?)(?=^#{2,3} |\Z)", now)]
               if "Previous document" in h)
    print(f"CLAUDE.md {len(claude):7d} characters; per-document table and narrative "
          f"{history:6d} ({100 * history / len(claude):.0f} %), 'Installing anything' "
          f"{install:6d} ({100 * install / len(claude):.0f} %)")
    print(f"NOW.md    {len(now):7d} characters; 'Previous document' sections "
          f"{prev:6d} ({100 * prev / len(now):.0f} %)")
    print(f"per-document records in Wiki/compare/: {len(glob.glob('Wiki/compare/reconcile-*.md'))} files, "
          f"{sum(size(f) for f in glob.glob('Wiki/compare/reconcile-*.md'))} bytes\n")


def section_2() -> None:
    print("## 2 · What each reconciliation yielded\n")
    sweep = [json.loads(l) for l in Path("Plan/runs/sweep.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    print(f"{'doc':>3} {'slug':42s} {'lines':>5} {'cand':>5} {'look':>5} {'judg':>5} "
          f"{'pages':>5} {'read':>5} {'J':>3} {'sweep r/all':>11}")
    zero_page_run = 0
    for n, slug in documents():
        j = reconcile(slug)
        pc = j.get("pre_classification", {})
        lines = sum(1 for _ in open(f"Sources/drive/{slug}.md", encoding="utf-8"))
        sw = [x for x in sweep if x.get("document") == slug]
        new = len(j.get("new_terms", []))
        zero_page_run = zero_page_run + 1 if new == 0 else 0
        print(f"{n:3d} {slug[:42]:42s} {lines:5d} {pc.get('candidates', '-')!s:>5} "
              f"{pc.get('decided_by_lookup', '-')!s:>5} {pc.get('needs_judgement', '-')!s:>5} "
              f"{new:5d} {len(pages_read(slug)):5d} {len(j.get('judgements', [])):3d} "
              f"{sum(1 for x in sw if x.get('decision') == 'reading'):>5d}/{len(sw):<5d}")
    print()


def section_3() -> None:
    print("## 3 · What a page is made of\n")
    for folder in ("Wiki/candidates", "Wiki/chapters"):
        agg: dict[str, int] = {}
        for f in glob.glob(folder + "/*.md"):
            for heading, body in sections(Path(f).read_text(encoding="utf-8")):
                agg[kind(heading)] = agg.get(kind(heading), 0) + len(heading) + len(body)
        total = sum(agg.values())
        parts = ", ".join(f"{k} {100 * v / total:.0f} %" for k, v in sorted(agg.items(), key=lambda x: -x[1]))
        print(f"{folder}: {total} characters — {parts}")
    rows = []
    for f in glob.glob("Wiki/candidates/*.md"):
        t = Path(f).read_text(encoding="utf-8")
        rows.append((len(t.encode()), digest_size(t), len(re.findall(r"(?m)^## Reading", t)), Path(f).stem))
    rows.sort(reverse=True)
    print("\nlargest term pages: bytes, digest, readings")
    for b, d, r, p in rows[:8]:
        print(f"  {p:26s} {b:7d} {d:6d} {r:3d}")
    print()


def section_4_5() -> None:
    print("## 4 · What a reader loads to add one document's readings (pages at today's size)\n")
    recs = records()
    print(f"{'doc':>3} {'slug':36s} {'docKB':>6} {'pages':>5} {'pagesKB':>7} {'digestKB':>8} "
          f"{'recordsKB':>9} {'chaptersKB':>10}")
    docs = documents()
    for n, slug in docs:
        if n < 32:
            continue
        j = reconcile(slug)
        ps = pages_read(slug)
        full = sum(size(page_file(p)) for p in ps)
        dig = sum(digest_size(Path(page_file(p)).read_text(encoding="utf-8")) for p in ps if os.path.exists(page_file(p)))
        rk = sum(size(recs.get(str(c).upper(), "")) for c in j.get("conflicts_changed", []) + j.get("questions_changed", []))
        ck = sum(size(f) for f in chapter_files(slug))
        print(f"{n:3d} {slug[:36]:36s} {size(f'Sources/drive/{slug}.md') / 1000:6.0f} {len(ps):5d} "
              f"{full / 1000:7.0f} {dig / 1000:8.0f} {rk / 1000:9.0f} {ck / 1000:10.0f}")
    print("\n## 5 · Batching: pages loaded once per batch rather than once per document\n")
    d = dict(docs)
    for name, rng in (("33-39", range(33, 40)), ("41-43", range(41, 44)), ("44-46", range(44, 47)),
                      ("48-50", range(48, 51)), ("32-51", range(32, 52))):
        sets = [pages_read(d[k]) for k in rng]
        per_doc = sum(sum(size(page_file(p)) for p in s) for s in sets)
        union = set().union(*sets)
        once = sum(size(page_file(p)) for p in union)
        dig = sum(digest_size(Path(page_file(p)).read_text(encoding="utf-8")) for p in union if os.path.exists(page_file(p)))
        print(f"documents {name:6s}: per document {per_doc / 1e6:5.2f} MB, once per batch {once / 1e6:5.2f} MB "
              f"({len(union)} pages, {per_doc / once:4.1f}x), as digests {dig / 1e6:5.2f} MB")
    print()


def section_6() -> None:
    print("## 6 · NEGATIVE: a reader given only the lines around a page's surfaces\n")
    idx = json.loads(Path("Wiki/index.json").read_text(encoding="utf-8"))["terms"]
    pages = {Path(f).stem: Path(f).read_text(encoding="utf-8") for f in glob.glob("Wiki/candidates/*.md")}
    cite = re.compile(r"\^\[([a-z0-9-]+)\.md:L(\d+)(?:[–-]L?(\d+))?\]")
    ks = (0, 2, 5, 10, 25)
    inside = {k: 0 for k in ks}
    cited_total = 0
    window = {k: 0 for k in ks}
    doc_lines = 0
    for _, slug in documents():
        text = [unicodedata.normalize("NFC", x).lower()
                for x in Path(f"Sources/drive/{slug}.md").read_text(encoding="utf-8").split("\n")]
        n = len(text)
        for page, body in pages.items():
            cited = set()
            for m in cite.finditer(body):
                if m.group(1) != slug:
                    continue
                a = int(m.group(2))
                b = int(m.group(3) or a)
                cited.update(range(a, (b if a <= b <= a + 50 else a) + 1))
            if not cited:
                continue
            term = idx.get(page, {})
            surf = [s.lower() for s in set(term.get("surfaces", [])) | {term.get("title", page)} if len(s) >= 3]
            hits = [i + 1 for i, line in enumerate(text) if any(s in line for s in surf)]
            cited_total += len(cited)
            doc_lines += n
            for k in ks:
                w = set()
                for h in hits:
                    w.update(range(max(1, h - k), min(n, h + k) + 1))
                inside[k] += sum(1 for c in cited if c in w)
                window[k] += len(w)
    for k in ks:
        print(f"±{k:2d} lines: {inside[k]:5d} of {cited_total} cited lines inside "
              f"({inside[k] / cited_total:.2f}); the window is {window[k] / doc_lines:.2f} of the document")
    print()


def section_7() -> None:
    print("## 7 · NEGATIVE: how much of each unread document already stands in a read one\n")
    rows = [json.loads(l) for l in Path("Sources/manifest.jsonl").read_text(encoding="utf-8").splitlines() if l.strip()]
    read = {slug for _, slug in documents()}
    word = re.compile(r"[a-zäöüß0-9]+")

    def shingles(path: str, k: int = 8) -> set[int]:
        t = Path(path).read_text(encoding="utf-8")
        if t.startswith("---"):
            t = t.split("---", 2)[2]
        w = word.findall(unicodedata.normalize("NFC", t.lower()))
        return {hash(" ".join(w[i:i + k])) for i in range(len(w) - k + 1)}

    landed = [r for r in rows if r.get("export_path") and os.path.exists(r["export_path"])]
    seen: set[int] = set()
    read_bytes = 0
    for r in landed:
        if r["slug"] in read:
            seen |= shingles(r["export_path"])
            read_bytes += size(r["export_path"])
    buckets = {">= 0.9": [0, 0], "0.5-0.9": [0, 0], "0.2-0.5": [0, 0], "< 0.2": [0, 0]}
    unread = 0
    for r in landed:
        if r["slug"] in read:
            continue
        s = shingles(r["export_path"])
        if not s:
            continue
        unread += 1
        c = len(s & seen) / len(s)
        key = ">= 0.9" if c >= 0.9 else "0.5-0.9" if c >= 0.5 else "0.2-0.5" if c >= 0.2 else "< 0.2"
        buckets[key][0] += 1
        buckets[key][1] += size(r["export_path"])
    print(f"read: {len(read)} documents, {read_bytes / 1e6:.2f} MB; unread with text: {unread}")
    for key, (count, b) in buckets.items():
        print(f"  share of 8-word shingles already read {key:8s}: {count:4d} documents, {b / 1e6:5.2f} MB")
    print("\nby category: read, unread, unread MB")
    cats: dict[str, list] = {}
    for r in landed:
        c = cats.setdefault(r["category"], [0, 0, 0])
        if r["slug"] in read:
            c[0] += 1
        else:
            c[1] += 1
            c[2] += size(r["export_path"])
    for name, (r_, u, b) in sorted(cats.items(), key=lambda x: -x[1][1]):
        print(f"  {name:20s} {r_:3d} {u:4d} {b / 1e6:6.2f}")
    print()


def section_8() -> None:
    print("## 8 · Claims no check reads\n")
    absence = re.compile(r"(\b0 times\b|stands? 0\b|\bzero times\b|`[^`\n]{1,40}` (?:stands? )?0\b|grep -c)")
    n = files = 0
    for f in glob.glob("Wiki/**/*.md", recursive=True):
        found = len(absence.findall(Path(f).read_text(encoding="utf-8")))
        n += found
        files += bool(found)
    print(f"absence counts written on wiki pages: {n} in {files} files; quotes.py checks none of them")
    compare = re.compile(r"\b(only (?:one|source|document|read)|no other|every other|the first (?:read )?(?:source|document)"
                         r"|earliest|the one read source|as in document \d+|a (?:second|third|fourth|fifth|sixth) "
                         r"(?:position|title|source)|unlike (?:every|all|the other)|all other (?:read )?(?:sources|documents)"
                         r"|in no other)\b", re.I)
    flagged = secs = 0
    for f in (glob.glob("Wiki/candidates/*.md") + glob.glob("Wiki/chapters/*.md")
              + glob.glob("Wiki/conflicts/*.md") + glob.glob("Wiki/questions/*.md")):
        for heading, body in sections(Path(f).read_text(encoding="utf-8")):
            if not (heading.startswith("## Reading") or heading.startswith("## 2026")):
                continue
            secs += 1
            flagged += len(compare.findall(re.sub(r"„[^“\"]*[“\"]", "", body)))
    print(f"comparison phrases inside one document's reading or record entry: {flagged} in {secs} sections")


def section_9() -> None:
    print("\n## 9 · Hand-kept counts in page frontmatter against the page body\n")
    import sys
    sys.path.insert(0, "scripts")
    from wiki_index import frontmatter
    read = {slug for _, slug in documents()}
    counts = {"sources != len(ingested)": [], "readings != reading sections": [],
              "readings kept, no reading heading": [], "cited (qualified), not ingested": []}
    for f in sorted(glob.glob("Wiki/candidates/*.md")):
        t = Path(f).read_text(encoding="utf-8")
        fm = frontmatter(t)
        page = Path(f).stem
        ing = fm.get("ingested", [])
        src, rd = str(fm.get("sources", "")), str(fm.get("readings", ""))
        n = len(re.findall(r"(?m)^## Reading", t))
        if src.isdigit() and int(src) != len(ing):
            counts["sources != len(ingested)"].append(f"{page} {src}/{len(ing)}")
        if rd.isdigit() and n == 0:
            counts["readings kept, no reading heading"].append(page)
        elif rd.isdigit() and int(rd) != n:
            counts["readings != reading sections"].append(f"{page} {rd}/{n}")
        for slug in sorted(set(re.findall(r"\^\[([a-z0-9-]+)\.md:L", t)) - set(ing)):
            if slug in read:
                counts["cited (qualified), not ingested"].append(f"{page}:{slug}")
    for k, v in counts.items():
        pages = sorted({x.split(":")[0].split(" ")[0] for x in v})
        print(f"{k:36s} {len(v):3d} ({len(pages)} pages): {', '.join(v)}")


if __name__ == "__main__":
    for part in (section_1, section_2, section_3, section_4_5, section_6, section_7, section_8, section_9):
        part()
