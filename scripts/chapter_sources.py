"""Candidate sources per chapter: a vector question to qmd, the unread documents it ranks.

A chapter page collects what every *read* source says about a chapter. This
script answers the other half of the navigation question — which *unread*
landed documents to open next for that chapter — by asking qmd.

For each chapter page it builds one typed query document from the page itself:

    intent: the chapter, by number
    vec:    a question — what happens in Kap N, with the titles the sources give it
    hyde:   a hypothetical passage — the titles and the page's first quoted beats

and runs `qmd query` with `--no-rerank`, so the answer is the vector legs fused,
no expansion model and no reranker. Hits on documents with a census are dropped
(their readings are already on the page); the first `--keep` distinct unread
documents stay, each with the line of its best chunk.

**A hit is a place to look, never a claim or a number** (the `qmd` skill). The
section this writes says so, carries no quotation and no citation, and is
replaced whole on every run — it is navigation, not a reading.

    python3 scripts/chapter_sources.py run [--keep 12] [--only 7,12]   # query, write hits.jsonl
    python3 scripts/chapter_sources.py run --terms [--keep 12]           # every term page, to terms.jsonl only
    python3 scripts/chapter_sources.py write                           # the section on every page
    python3 scripts/chapter_sources.py selftest
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import time
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from wiki_index import frontmatter  # noqa: E402

CHAPTERS = ROOT / "Wiki" / "chapters"
TERMS = ROOT / "Sources" / "terms"
MANIFEST = ROOT / "Sources" / "manifest.jsonl"
BIN = ROOT / ".tools-node" / "node_modules" / ".bin" / "qmd"
RUN = ROOT / "Plan" / "runs" / "qmd-chapters-2026-09-26"
HITS = RUN / "hits.jsonl"
TERM_HITS = RUN / "terms.jsonl"
PAGES = ROOT / "Wiki" / "candidates"
QUOTE = re.compile(r"„([^“\"]{20,240})[“\"]")

HEADING = "## Candidate sources — unread, ranked by qmd"
TITLE = re.compile(r"^Title: „([^“\"]+)[“\"]", re.M)
BULLET = re.compile(r"^- [^:]{1,40}: „([^“\"]{12,200})[“\"]", re.M)
SOURCE_REF = re.compile(r"^qmd://sources/(?P<path>.+\.md)$")


def read_slugs() -> set[str]:
    """Documents with a census: read, so their readings are already on the pages."""
    return {p.stem for p in TERMS.glob("*.md")}


def manifest() -> dict[str, dict]:
    rows = [json.loads(line) for line in MANIFEST.read_text(encoding="utf-8").splitlines() if line.strip()]
    return {r["slug"]: r for r in rows if r.get("export_path")}


def query_for(number: int, text: str) -> str:
    """The typed query document for one chapter page, built from the page alone."""
    titles = distinct(TITLE.findall(text))
    beats = distinct(m for body in re.split(r"^## ", text, flags=re.M)[1:]
                     for m in BULLET.findall(body)[:1])
    named = "; ".join(titles[:4])
    question = f"Was geschieht in Kapitel {number} des Romans" + (f" — {named}" if named else "") + "?"
    passage = f"Kapitel {number}. " + " ".join(f"{t}." for t in titles[:3]) + " " + " ".join(beats[:4])
    passage = re.sub(r"\s+", " ", passage).strip()[:700]
    return "\n".join([f"intent: Kapitel {number} des Romans, was darin geschieht",
                      f"vec: {one_line(question)}",
                      f"hyde: {one_line(passage)}"])


def distinct(items) -> list[str]:
    """Each once, ignoring case, and none that another already contains."""
    out = []
    for item in (i.strip() for i in items):
        low = item.casefold()
        if any(low in o.casefold() for o in out):
            continue
        out = [o for o in out if o.casefold() not in low] + [item]
    return out


def query_for_term(meta: dict, text: str) -> str:
    """The typed query document for one term page: its surfaces, and a quotation from each of its first readings."""
    term = meta.get("term", "")
    aliases = [a for a in meta.get("aliases", []) if isinstance(a, str)]
    named = ", ".join([term] + aliases[:3])
    quotes = distinct(m for body in re.split(r"^## Reading", text, flags=re.M)[1:4]
                      for m in QUOTE.findall(body)[:1])
    passage = re.sub(r"\s+", " ", f"{term}. " + " ".join(q.replace("\\\"", "").replace("> ", "") for q in quotes)).strip()[:700]
    return "\n".join([f"intent: {one_line(term)} im Roman Kohärenz Protokoll",
                      f"vec: {one_line(f'Was ist {named} und welche Rolle spielt es in der Geschichte?')}",
                      f"hyde: {one_line(passage)}"])


def one_line(text: str) -> str:
    """A typed line is single-line text with balanced quotes."""
    return re.sub(r"\s+", " ", text.replace('"', "")).strip()


def ask(document: str, n: int) -> list[dict]:
    done = subprocess.run([str(BIN), "query", document, "-c", "sources", "--no-rerank",
                           "-n", str(n), "--format", "json"],
                          capture_output=True, text=True, cwd=ROOT)
    if done.returncode != 0 and not done.stdout:
        raise RuntimeError(done.stderr[:400])
    try:
        return json.loads(done.stdout)
    except json.JSONDecodeError:
        raise RuntimeError(f"unparsed qmd output: {done.stdout[:300]}")


def keep_unread(rows: list[dict], read: set[str], keep: int) -> list[dict]:
    """The first `keep` distinct unread documents, each at its best-ranked chunk."""
    out, seen = [], set()
    for rank, row in enumerate(rows, 1):
        match = SOURCE_REF.match(row.get("file", ""))
        if not match:
            continue
        slug = Path(match.group("path")).stem
        if slug in read or slug in seen:
            continue
        seen.add(slug)
        out.append({"slug": slug, "rank": rank, "line": int(row.get("line") or 0),
                    "score": round(float(row.get("score") or 0.0), 4)})
        if len(out) == keep:
            break
    return out


def run(keep: int, only: set[int] | None) -> int:
    read = read_slugs()
    RUN.mkdir(parents=True, exist_ok=True)
    old = {}
    if HITS.exists():
        old = {r["chapter"]: r for r in map(json.loads, HITS.read_text(encoding="utf-8").splitlines())}
    for path in sorted(CHAPTERS.glob("kap-*.md")):
        number = int(frontmatter(path.read_text(encoding="utf-8")).get("chapter"))
        if only and number not in only:
            continue
        document = query_for(number, path.read_text(encoding="utf-8"))
        started, n, kept = time.time(), 60, []
        while n <= 240:
            kept = keep_unread(ask(document, n), read, keep)
            if len(kept) >= keep:
                break
            n *= 2
        old[number] = {"chapter": number, "query": document, "n": n,
                       "seconds": round(time.time() - started, 1), "hits": kept}
        print(f"Kap {number}: {len(kept)} unread documents from -n {n} in {old[number]['seconds']}s", flush=True)
        HITS.write_text("".join(json.dumps(old[k], ensure_ascii=False) + "\n" for k in sorted(old)),
                        encoding="utf-8")
    return 0


def run_terms(keep: int) -> int:
    """The same question for every term page. Written to the run only: the pages stay as they are."""
    read = read_slugs()
    RUN.mkdir(parents=True, exist_ok=True)
    out = []
    for path in sorted(PAGES.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        document = query_for_term(frontmatter(text), text)
        started, n, kept = time.time(), 60, []
        while n <= 240:
            kept = keep_unread(ask(document, n), read, keep)
            if len(kept) >= keep:
                break
            n *= 2
        out.append({"page": path.stem, "query": document, "n": n,
                    "seconds": round(time.time() - started, 1), "hits": kept})
        print(f"{path.stem}: {len(kept)} unread documents in {out[-1]['seconds']}s", flush=True)
        TERM_HITS.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in out), encoding="utf-8")
    return 0


def section(hits: list[dict], rows: dict[str, dict]) -> str:
    lines = [HEADING, "",
             "Navigation, not a reading. Landed documents with no census yet, in the order "
             "a qmd vector query built from this page's titles and beats ranked them "
             "(`scripts/chapter_sources.py`, 2026-09-26). A hit is a place to look: it says "
             "nothing about what the document holds for this chapter, and its rank is no "
             "measure. The line is where qmd's snippet of its best-ranked passage stands.", "",
             "| # | document | date | category | look at |",
             "|--:|---|---|---|---|"]
    for i, hit in enumerate(hits, 1):
        row = rows.get(hit["slug"], {})
        lines.append(f"| {i} | `{hit['slug']}` | {row.get('index_date', '—')} | "
                     f"{row.get('category', '—')} | L{hit['line']} |")
    return "\n".join(lines) + "\n"


def with_section(text: str, block: str) -> str:
    """The page with the section replaced, or appended at the end."""
    start = text.find(HEADING)
    if start == -1:
        return text.rstrip("\n") + "\n\n" + block
    after = re.search(r"^## ", text[start + len(HEADING):], re.M)
    end = start + len(HEADING) + after.start() if after else len(text)
    rest = text[end:]
    return text[:start] + block + ("\n" + rest if rest else "")


def write() -> int:
    rows = manifest()
    by_chapter = {r["chapter"]: r for r in map(json.loads, HITS.read_text(encoding="utf-8").splitlines())}
    changed = 0
    for path in sorted(CHAPTERS.glob("kap-*.md")):
        text = path.read_text(encoding="utf-8")
        number = int(frontmatter(text).get("chapter"))
        if number not in by_chapter:
            continue
        new = with_section(text, section(by_chapter[number]["hits"], rows))
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1
    print(f"{changed} chapter pages written")
    return 0


def selftest() -> int:
    page = ("---\nchapter: 3\n---\n\n# Kap 3\n\n## Reading — `a`, 2026\n\n"
            "Title: „Der Fall“ ^[a.md:L1]\n\n- Plot beats: „Kael fällt durch die Schicht“ ^[a.md:L2]\n\n"
            "## Where the sources differ\n\nNothing.\n")
    failures = []
    q = query_for(3, page)
    if "vec: Was geschieht in Kapitel 3 des Romans — Der Fall?" not in q:
        failures.append(f"the question: {q!r}")
    if "hyde: Kapitel 3. Der Fall. Kael fällt durch die Schicht" not in q:
        failures.append(f"the passage: {q!r}")
    rows = [{"file": "qmd://sources/read.md", "line": 3}, {"file": "qmd://wiki/x.md", "line": 1},
            {"file": "qmd://sources/u1.md", "line": 5}, {"file": "qmd://sources/u1.md", "line": 9},
            {"file": "qmd://sources/u2.md", "line": 7}]
    kept = keep_unread(rows, {"read"}, 2)
    if [(k["slug"], k["line"], k["rank"]) for k in kept] != [("u1", 5, 3), ("u2", 7, 5)]:
        failures.append(f"keep_unread: {kept}")
    block = section([{"slug": "u1", "line": 5}], {"u1": {"index_date": "2026-05-08", "category": "md"}})
    once = with_section(page, block)
    twice = with_section(once, section([{"slug": "u2", "line": 7}], {}))
    if once.count(HEADING) != 1 or twice.count(HEADING) != 1 or "`u1`" in twice or "`u2`" not in twice:
        failures.append("with_section does not replace the section whole")
    middle = with_section(page.replace("## Where", HEADING + "\n\nSTALE-ROW\n\n## Where"), block)
    if "STALE-ROW" in middle or "## Where the sources differ" not in middle:
        failures.append("with_section loses the section after it")
    for failure in failures:
        print(f"FAILED  {failure}")
    print("chapter_sources selftest: " + ("held" if not failures else f"{len(failures)} failed"))
    return 1 if failures else 0


def main(argv: list[str]) -> int:
    if not argv or argv[0] not in {"run", "write", "selftest"}:
        print(__doc__)
        return 2
    if argv[0] == "selftest":
        return selftest()
    if argv[0] == "write":
        return write()
    keep = int(argv[argv.index("--keep") + 1]) if "--keep" in argv else 12
    if "--terms" in argv:
        return run_terms(keep)
    only = {int(x) for x in argv[argv.index("--only") + 1].split(",")} if "--only" in argv else None
    return run(keep, only)


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
