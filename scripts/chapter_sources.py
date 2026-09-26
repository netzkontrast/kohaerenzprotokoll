"""Candidate sources per chapter: its questions asked of qmd's vectors, the unread documents that answer.

A chapter page collects what every *read* source says about a chapter. This
script answers the navigation question beside it — which *unread* landed
documents to open next for that chapter — and it asks by question.

The questions come first and are written by a reader, not by this script:
`Plan/runs/qmd-chapters-2026-09-26/questions/kap-NN.json`, eight to twelve per
chapter, each tagged with the GOAL.md §4.5 generator or §5 structure level it
comes from (`questions-brief.md` in the same directory is how they were asked
for). Each question goes to qmd alone, as a typed `vec:` query against
`sources` with `--no-rerank` — vector similarity only, no expansion model, no
reranker. Hits on documents with a census are dropped: their readings are
already on the page. A document's rank for the chapter is reciprocal-rank
fusion over the chapter's questions, so a document several questions return
ranks above one a single question returns first.

**A hit is a place to look, never a claim or a number** (the `qmd` skill). The
two sections this writes say so, carry no quotation and no citation, and are
replaced whole on every run: navigation, not readings.

    python3 scripts/chapter_sources.py run [--keep 12] [--only 7,12]   # ask, write hits.jsonl
    python3 scripts/chapter_sources.py write                           # the questions, and the sources once asked
    python3 scripts/chapter_sources.py run --terms [--keep 12]         # every term page, to terms.jsonl only
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
PAGES = ROOT / "Wiki" / "candidates"
TERMS = ROOT / "Sources" / "terms"
MANIFEST = ROOT / "Sources" / "manifest.jsonl"
BIN = ROOT / ".tools-node" / "node_modules" / ".bin" / "qmd"
RUN = ROOT / "Plan" / "runs" / "qmd-chapters-2026-09-26"
QUESTIONS = RUN / "questions"
HITS = RUN / "hits.jsonl"
BASIC = RUN / "basic-questions.json"
TERM_HITS = RUN / "terms.jsonl"

ASKED = "## Questions for this chapter"
HEADING = "## Candidate sources — unread, ranked by qmd"
PER_QUESTION = 40     # hits asked for per question, before the read documents are dropped
FUSION_K = 10         # reciprocal-rank fusion: 1 / (K + rank among a question's unread documents)
TITLE = re.compile(r"^Title: „([^“\"]+)[“\"]", re.M)
QUOTE = re.compile(r"„([^“\"]{20,240})[“\"]")
SOURCE_REF = re.compile(r"^qmd://sources/(?P<path>.+\.md)$")


def read_slugs() -> set[str]:
    """Documents with a census: read, so their readings are already on the pages."""
    return {p.stem for p in TERMS.glob("*.md")}


def manifest() -> dict[str, dict]:
    rows = [json.loads(line) for line in MANIFEST.read_text(encoding="utf-8").splitlines() if line.strip()]
    return {r["slug"]: r for r in rows if r.get("export_path")}


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


def unread(rows: list[dict], read: set[str], keep: int | None = None) -> list[dict]:
    """Distinct unread documents in rank order, each at its best-ranked chunk."""
    out, seen = [], set()
    for rank, row in enumerate(rows, 1):
        match = SOURCE_REF.match(row.get("file", ""))
        if not match:
            continue
        slug = Path(match.group("path")).stem
        if slug in read or slug in seen:
            continue
        seen.add(slug)
        out.append({"slug": slug, "rank": rank, "line": int(row.get("line") or 0)})
        if keep is not None and len(out) == keep:
            break
    return out


def fuse(per_question: dict[str, list[dict]]) -> list[dict]:
    """One ranking from every question's: reciprocal-rank fusion, ties by first question."""
    docs: dict[str, dict] = {}
    for qid, hits in per_question.items():
        for position, hit in enumerate(hits, 1):
            doc = docs.setdefault(hit["slug"], {"slug": hit["slug"], "fused": 0.0, "questions": [],
                                                "line": hit["line"], "best": position})
            doc["fused"] += 1.0 / (FUSION_K + position)
            doc["questions"].append(qid)
            if position < doc["best"]:
                doc["best"], doc["line"] = position, hit["line"]
    ranked = sorted(docs.values(), key=lambda d: (-d["fused"], d["best"], d["slug"]))
    for doc in ranked:
        doc["fused"] = round(doc["fused"], 4)
    return ranked


def basic(number: int, text: str) -> list[dict]:
    """The eight questions every author asks of a chapter, filled with this one's number and titles."""
    titles = distinct(TITLE.findall(text))[:2]
    fill = {"N": str(number),
            "titel": " / ".join(titles),
            "weiter": f"in Kapitel {number + 1}" if number < 40 else "aus dem Roman hinaus"}
    out = []
    for q in json.loads(BASIC.read_text(encoding="utf-8"))["questions"]:
        question = q["template"]
        if not titles:
            question = question.replace(" ({titel})", "")
        out.append({"id": f"K{number}-{q['id']}", "label": q["id"], "tag": q["tag"],
                    "question": question.format(**fill),
                    "shown": q["template"].replace(" ({titel})", "").format(**fill),
                    "titles": titles})
    return out


def load_questions(number: int, text: str) -> list[dict]:
    """Basic questions first, then the chapter's own, each with the label the page shows: B1…, S1…."""
    path = QUESTIONS / f"kap-{number:02d}.json"
    if not path.exists():
        return []
    own = json.loads(path.read_text(encoding="utf-8"))["questions"]
    return basic(number, text) + [dict(q, label=f"S{i}") for i, q in enumerate(own, 1)]


def run(keep: int, only: set[int] | None) -> int:
    read = read_slugs()
    old = {}
    if HITS.exists():
        old = {r["chapter"]: r for r in map(json.loads, HITS.read_text(encoding="utf-8").splitlines())}
    for path in sorted(CHAPTERS.glob("kap-*.md")):
        text = path.read_text(encoding="utf-8")
        number = int(frontmatter(text).get("chapter"))
        questions = load_questions(number, text)
        if (only and number not in only) or not questions:
            continue
        started, per_question = time.time(), {}
        for q in questions:
            per_question[q["id"]] = unread(ask(f"vec: {one_line(q['question'])}", PER_QUESTION), read)
        ranked = fuse(per_question)
        old[number] = {"chapter": number, "seconds": round(time.time() - started, 1),
                       "per_question": per_question, "ranked": ranked[:max(keep, 10)]}
        print(f"Kap {number}: {len(questions)} questions, {len(ranked)} unread documents, "
              f"{old[number]['seconds']}s", flush=True)
        HITS.write_text("".join(json.dumps(old[k], ensure_ascii=False) + "\n" for k in sorted(old)),
                        encoding="utf-8")
    return 0


def questions_section(number: int, questions: list[dict]) -> str:
    basics = [q for q in questions if q["label"].startswith("B")]
    lines = [ASKED, "",
             "What a reader of this chapter's sources should be looking for, asked before any search. "
             "Questions, not readings: none is answered here.", "",
             "### Basic — what every author asks of a chapter", "",
             "The same eight for every chapter (`Plan/runs/qmd-chapters-2026-09-26/basic-questions.json`)."
             + (" Asked of the search with the titles the readings give this chapter: "
                + " / ".join(f"*{t}*" for t in basics[0]["titles"]) + "." if basics and basics[0]["titles"] else ""),
             ""]
    lines += [f"- **{q['label']}** *{q['tag']}* — {q['shown'].strip()}" for q in basics]
    lines += ["", f"### Specific to Kap {number}", "",
              "Written from this page, its neighbours and its records against GOAL.md §4.5 and §5, "
              "Dramatica and craft, going beyond the basic eight "
              "(`Plan/runs/qmd-chapters-2026-09-26/questions-brief.md`).", ""]
    lines += [f"- **{q['label']}** *{q['tag']}* — {q['question'].strip()}"
              for q in questions if q["label"].startswith("S")]
    return "\n".join(lines) + "\n"


def sources_section(ranked: list[dict], questions: list[dict], rows: dict[str, dict]) -> str:
    label = {q["id"]: q["label"] for q in questions}
    order = {q["id"]: i for i, q in enumerate(questions)}
    lines = [HEADING, "",
             "Navigation, not a reading. Landed documents with no census yet, returned by a qmd vector "
             "search for the questions above, one question at a time, and ranked by how high and how "
             "often they came back (`scripts/chapter_sources.py`, 2026-09-26). A hit is a place to look: "
             "it says nothing about what the document holds for this chapter, and its rank is no measure. "
             "*Questions* names the questions above that returned it; the line is where qmd's snippet of its "
             "best passage stands.", "",
             "| # | document | date | category | questions | look at |",
             "|--:|---|---|---|---|---|"]
    for i, doc in enumerate(ranked, 1):
        row = rows.get(doc["slug"], {})
        asked = ", ".join(label[q] for q in sorted((q for q in doc["questions"] if q in label), key=order.get))
        lines.append(f"| {i} | `{doc['slug']}` | {row.get('index_date', '—')} | "
                     f"{row.get('category', '—')} | {asked} | L{doc['line']} |")
    return "\n".join(lines) + "\n"


def with_section(text: str, heading: str, block: str) -> str:
    """The page with the section under `heading` replaced, or appended at the end."""
    start = text.find(heading)
    if start == -1:
        return text.rstrip("\n") + "\n\n" + block
    after = re.search(r"^## ", text[start + len(heading):], re.M)
    end = start + len(heading) + after.start() if after else len(text)
    rest = text[end:]
    return text[:start] + block + ("\n" + rest if rest else "")


def write() -> int:
    rows = manifest()
    by_chapter = {}
    if HITS.exists():
        by_chapter = {r["chapter"]: r for r in map(json.loads, HITS.read_text(encoding="utf-8").splitlines())}
    changed = 0
    for path in sorted(CHAPTERS.glob("kap-*.md")):
        text = path.read_text(encoding="utf-8")
        number = int(frontmatter(text).get("chapter"))
        questions = load_questions(number, text)
        if not questions:
            continue
        new = with_section(text, ASKED, questions_section(number, questions))
        if number in by_chapter:
            new = with_section(new, HEADING, sources_section(by_chapter[number]["ranked"], questions, rows))
        if new != text:
            path.write_text(new, encoding="utf-8")
            changed += 1
    print(f"{changed} chapter pages written")
    return 0


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


def run_terms(keep: int) -> int:
    """One question for every term page. Written to the run only: the pages stay as they are."""
    read = read_slugs()
    out = []
    for path in sorted(PAGES.glob("*.md")):
        text = path.read_text(encoding="utf-8")
        document = query_for_term(frontmatter(text), text)
        started = time.time()
        kept = unread(ask(document, 80), read, keep)
        out.append({"page": path.stem, "query": document,
                    "seconds": round(time.time() - started, 1), "hits": kept})
        print(f"{path.stem}: {len(kept)} unread documents in {out[-1]['seconds']}s", flush=True)
        TERM_HITS.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in out), encoding="utf-8")
    return 0


def selftest() -> int:
    failures = []
    rows = [{"file": "qmd://sources/read.md", "line": 3}, {"file": "qmd://wiki/x.md", "line": 1},
            {"file": "qmd://sources/u1.md", "line": 5}, {"file": "qmd://sources/u1.md", "line": 9},
            {"file": "qmd://sources/u2.md", "line": 7}]
    kept = unread(rows, {"read"})
    if [(k["slug"], k["line"], k["rank"]) for k in kept] != [("u1", 5, 3), ("u2", 7, 5)]:
        failures.append(f"unread: {kept}")
    fused = fuse({"q1": [{"slug": "a", "line": 1}, {"slug": "b", "line": 2}],
                  "q2": [{"slug": "c", "line": 3}, {"slug": "b", "line": 4}],
                  "q3": [{"slug": "b", "line": 5}]})
    if [d["slug"] for d in fused] != ["b", "a", "c"] or fused[0]["questions"] != ["q1", "q2", "q3"] \
            or fused[0]["line"] != 5:
        failures.append(f"fuse: a document three questions return must rank first, at its best line: {fused}")
    questions = [{"id": "K3-01", "label": "B1", "tag": "Kausalität", "question": "Was führt aus Kapitel 2 in Kapitel 3?",
                  "shown": "Was führt aus Kapitel 2 in Kapitel 3?", "titles": []},
                 {"id": "K3-02", "label": "S1", "tag": "Storyform", "question": "Welche Storypoints trägt Kapitel 3?"}]
    block = sources_section([{"slug": "u1", "line": 5, "questions": ["K3-02", "K3-01"]}], questions,
                            {"u1": {"index_date": "2026-05-08", "category": "md"}})
    if "| 1 | `u1` | 2026-05-08 | md | B1, S1 | L5 |" not in block:
        failures.append(f"sources_section: {block}")
    page = "---\nchapter: 3\n---\n\n# Kap 3\n\n## Reading — `a`, 2026\n\nx\n\n## Where the sources differ\n\nNothing.\n"
    once = with_section(with_section(page, ASKED, questions_section(3, questions)), HEADING, block)
    twice = with_section(once, HEADING, sources_section([], questions, {}))
    if once.count(HEADING) != 1 or twice.count(HEADING) != 1 or "`u1`" in twice or twice.count(ASKED) != 1:
        failures.append("with_section does not replace a section whole")
    if once.index(ASKED) < once.index("## Where the sources differ") or once.index(HEADING) < once.index(ASKED):
        failures.append("the sections do not follow the readings, questions first")
    middle = with_section(page.replace("## Where", HEADING + "\n\nSTALE-ROW\n\n## Where"), HEADING, block)
    if "STALE-ROW" in middle or "## Where the sources differ" not in middle:
        failures.append("with_section loses the section after it")
    titled = page.replace("x\n", "Title: „Der Fall“ ^[a.md:L1]\n")
    b = basic(3, titled)
    if len(b) < 8 or b[0]["label"] != "B1" or "Kapitel 3 (Der Fall)" not in b[0]["question"] \
            or "in Kapitel 4" not in next(q["question"] for q in b if q["label"] == "B6"):
        failures.append(f"basic: not filled with the chapter: {b[:1]}")
    if "()" in basic(3, page)[0]["question"] or "aus dem Roman hinaus" not in basic(40, page)[5]["question"]:
        failures.append("basic: an untitled chapter or Kap 40 is filled wrongly")
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
