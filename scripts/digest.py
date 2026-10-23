"""The full read of one term page: every citation opened, every thought written once, the coverage checked.

A candidate page (`Wiki/candidates/<slug>.md`) holds one reading per source document, by
date — the research ledger, attributed and unmerged. At its size (`aegis`: 2,906 distinct
citations) nobody can review it, and nothing checks that the term page written from it
leaves nothing out. **The full read** opens every line the candidate cites, with its context,
and writes every thought about the term once — with every source that carries it and that
source's stance — into a German **thought page** (`Wiki/terms/<slug>.md`, `form: gedanken`).
That page is what the author reviews (the author's answers of 2026-10-23,
`Plan/concept/term-digest_2026-10-23.md` §11).

    form: gedanken           # provisional — planned 2026-10-23, the pilot is genesis-klammer
                             # may not: merge two readings whose words or stance differ, decide which reading
                             #          is right, enter canon, cite a line the writer did not open
                             # retire when: three full reads show the author reviews by source, not by thought

**Whole means every citation is accounted for.** Each distinct citation of the candidate —
and each line of the project's own records that names the term — gets one row in the run's
ledger (`Plan/runs/digest/<slug>/ledger.jsonl`) with a state:

| state | means |
|---|---|
| `used` | a thought cites it (`thoughts` names which) |
| `same-as` | the same line is cited again elsewhere on the page and says nothing new (`note` says where) |
| `context` | it frames another cited line and carries no thought of its own |
| `occurrence` | it names the term and says nothing about it |
| `barred` | it holds an early name, a real person's name, the trauma symbol or a world code's expansion: read, never quoted |
| `defect` | the reading's prose says something the line does not; fixed on the candidate first |

That proves coverage of the evidence, not completeness of the understanding: the second is
a person's judgement, measured in the pilot by a blind second reader.

**The run directory** `Plan/runs/digest/<slug>/`:

- `packet.json` — written by `plan`: the candidate's hash, every reference with its document,
  lines, context window, the page lines that cite it and whether it is barred, and the chunks.
- `chunks/NN.ledger.jsonl`, `chunks/NN.thoughts.jsonl` — one reader per chunk; thought ids are
  local (`c01-01`).
- `thoughts.jsonl` — the session's grouped list; each thought's `from` names the chunk thoughts
  it joins. `groupings.jsonl` — one row per thought that joins two or more documents, with why.
- `ledger.jsonl` — written by `join` from the chunk ledgers, chunk ids mapped to final ones.

A thought (one JSON line):

    {"id": "g-001", "kind": "mechanism", "tag": "S", "text": "Kap 40 erzählt …",
     "sources": [{"ref": "doc.md:L930", "stance": "asserts", "quote": "…"}],
     "from": ["c01-03"], "involves": ["genesis"], "differs_from": [], "links": []}

`kind` is one of `KINDS`; `tag` is `S` (a source says it), `K` (decided: `links` names the
decision), `V` (a proposal), `L` (a gap) or `D` (derived by the writer: `refs` names thoughts
or `links` a file). `stance` is one of `STANCES`. A `quote` must stand on its line; a source
without one is cited, not quoted.

Usage:
    python3 scripts/digest.py plan <slug>        # the packet and the chunks; refuses a page with bare references
    python3 scripts/digest.py show <slug> <NN|records>   # one chunk for its reader: reference, reading, source window
    python3 scripts/digest.py status <slug>      # references per state, chunks done, what is left
    python3 scripts/digest.py join <slug>        # the chunk ledgers into ledger.jsonl, mapped to thoughts.jsonl
    python3 scripts/digest.py write <slug>       # Wiki/terms/<slug>.md from thoughts.jsonl and the ledger
    python3 scripts/digest.py check [<slug>]     # every refusal below; every thought page when no slug is given
    python3 scripts/digest.py selftest
"""

from __future__ import annotations

import datetime
import hashlib
import json
import re
import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT / "scripts"))

CANDIDATES = ROOT / "Wiki" / "candidates"
TERMS = ROOT / "Wiki" / "terms"
RUNS = ROOT / "Plan" / "runs" / "digest"

STATES = ("used", "same-as", "context", "occurrence", "barred", "defect")
STANCES = {"asserts": "behauptet", "proposes": "schlägt vor", "questions": "fragt", "rejects": "verwirft",
           "reports": "berichtet"}
TAGS = "SKVLD"
# The page's sections, in order; a thought's kind decides its section.
KINDS = [("kurz", "Kurz"), ("decided", "Was das Projekt entschieden hat"), ("definition", "Was es ist"),
         ("function", "Was es im Roman tut"), ("mechanism", "Wie es wirkt"), ("origin", "Woher es kommt"),
         ("evolution", "Wie sich das Bild verändert hat"), ("relation", "Bezüge zu anderen Begriffen"),
         ("differ", "Wo die Quellen auseinandergehen"), ("prose", "In der Prosa"), ("open", "Offen")]
TAIL = ["Vollständigkeit", "Autor-Notizen", "Herkunft"]
SECTIONS = [title for _, title in KINDS] + TAIL
AUTHOR_OPEN, AUTHOR_CLOSE = "<!-- autor:anfang -->", "<!-- autor:ende -->"

MAX_REFS, MAX_LINES, WINDOW = 150, 1500, 3
REF = re.compile(r"\^\[(?P<ref>(?P<doc>[a-z0-9][a-z0-9-]*)\.md:L(?P<first>\d+)(?:[–-]L?(?P<last>\d+))?)\]")
BARE = re.compile(r"\^\[L\d+")
READING_HEAD = re.compile(r"^## Reading — `([^`]+)`")
THOUGHT_ID = re.compile(r"^- \[[A-Z]\] \((g-\d{3,})\) ")
# What is read and never written (decision 028 and the author's rules): the earlier names, the names the corpus
# gives after „ehem.“, and the trauma symbol. Split so that a search for the names does not find this file.
BARRED = re.compile("|".join(("Mich" "ael", "Jul" "ia", "Sha" "dow", "Lost " "One", "Isab" "ella", "Alex" "ander",
                              "Ste" "fan", r"\bDa" r"ta\b", "Wächt" "erin", "Der " "Kleine", "Beobachter/" "Kritiker",
                              "Kis" "sen", r"\bGe" r"lb")))


# --- reading the candidate -----------------------------------------------------

def refs_of(text: str) -> dict[str, dict]:
    """Every distinct reference on a page: its document, lines and the page lines that cite it."""
    out: dict[str, dict] = {}
    reading = None
    for no, line in enumerate(text.split("\n"), 1):
        head = READING_HEAD.match(line)
        if head:
            reading = head.group(1)
        elif line.startswith("## "):
            reading = None
        for m in REF.finditer(line):
            first = int(m.group("first"))
            last = int(m.group("last") or first)
            row = out.setdefault(m.group("ref"), {"ref": m.group("ref"), "doc": m.group("doc"), "first": first,
                                                  "last": max(first, last), "page_lines": [], "readings": []})
            row["page_lines"].append(no)
            if reading and reading not in row["readings"]:
                row["readings"].append(reading)
    return out


def source_lines(doc: str, first: int, last: int) -> list[tuple[int, str]]:
    import quotes
    out = []
    for n in range(first, last + 1):
        line = quotes.source_line(doc, n)
        if line is not None:
            out.append((n, line))
    return out


def window(doc: str, first: int, last: int) -> list[int]:
    """The cited lines and WINDOW non-blank lines on each side, at most 4 × WINDOW lines away (Drive exports
    put blank lines between paragraphs, so a fixed span often shows nothing but blanks)."""
    import quotes
    lo, seen = first, 0
    while lo > 1 and seen < WINDOW and first - lo < 4 * WINDOW:
        lo -= 1
        line = quotes.source_line(doc, lo)
        if line is None:
            lo += 1
            break
        seen += bool(line.strip())
    hi, seen = last, 0
    while seen < WINDOW and hi - last < 4 * WINDOW:
        line = quotes.source_line(doc, hi + 1)
        if line is None:
            break
        hi += 1
        seen += bool(line.strip())
    return [lo, hi]


def page_hash(text: str) -> str:
    import promote
    return promote.digest(text)


def records(slug: str) -> list[dict]:
    """The project's own lines that name the term — the only source of [K] — as references to account for."""
    import terms
    out = []
    for hit in terms.finds(slug):
        where = hit.split("  ", 1)[0].split(" [", 1)[0]
        if where.startswith("Wiki/questions/reading/"):
            continue  # the generated reading questions are prompts, not the project's records (2026-10-14 concept)
        out.append({"ref": where, "doc": None, "origin": "records", "line": hit.split("  ", 1)[-1]})
    return out


def inbound(slug: str) -> list[dict]:
    """Lines of the other wiki pages that link the term or write its name: where another page's sources speak of it."""
    import promote
    pats = sorted({promote.fold(x) for x in promote.surfaces(slug)}, key=len, reverse=True)
    name = re.compile(r"(?<!\w)(?:" + "|".join(map(re.escape, pats)) + r")(?!\w)") if pats else None
    link = re.compile(r"\[\[" + re.escape(slug) + r"(?:\|[^\]]*)?\]\]")
    out = []
    for folder in ("candidates", "chapters"):
        for path in sorted((ROOT / "Wiki" / folder).glob("*.md")):
            if folder == "candidates" and path.stem == slug:
                continue
            for no, line in enumerate(path.read_text(encoding="utf-8").split("\n"), 1):
                if line.startswith(("---", "ingested:", "aliases:", "term:")):
                    continue
                if link.search(line) or (name and name.search(promote.fold(line))):
                    out.append({"ref": f"{path.relative_to(ROOT)}:{no}", "doc": None, "origin": folder,
                                "line": line.strip()[:200]})
    return out


def chunked(refs: list[dict]) -> list[dict]:
    """Chunks in page order, whole documents where they fit, never more than MAX_REFS or MAX_LINES."""
    chunks: list[dict] = []
    cur: dict = {"refs": [], "lines": 0}
    for r in refs:
        size = r["window"][1] - r["window"][0] + 1
        if cur["refs"] and (len(cur["refs"]) >= MAX_REFS or cur["lines"] + size > MAX_LINES):
            chunks.append(cur)
            cur = {"refs": [], "lines": 0}
        cur["refs"].append(r["ref"])
        cur["lines"] += size
    if cur["refs"]:
        chunks.append(cur)
    return [{"id": f"{i:02d}", "refs": c["refs"], "lines": c["lines"]} for i, c in enumerate(chunks, 1)]


def plan(slug: str, today: str | None = None, root: Path | None = None) -> dict:
    page = (root or CANDIDATES) / f"{slug}.md"
    if not page.exists():
        raise SystemExit(f"no candidate page {page.relative_to(ROOT) if page.is_relative_to(ROOT) else page}")
    text = page.read_text(encoding="utf-8")
    bare = [no for no, line in enumerate(text.split("\n"), 1) if BARE.search(line)]
    if bare:
        raise SystemExit(f"refused: {page.name} has bare references ^[Lnn] on lines {bare[:10]} — name the document first")
    refs = []
    for r in refs_of(text).values():
        lines = source_lines(r["doc"], r["first"], r["last"])
        r["window"] = window(r["doc"], r["first"], r["last"])
        r["barred"] = any(BARRED.search(line) for _, line in lines)
        r["landed"] = bool(lines)
        refs.append(r)
    refs.sort(key=lambda r: min(r["page_lines"]))
    packet = {"slug": slug, "planned": today or datetime.date.today().isoformat(), "candidate_hash": page_hash(text),
              "refs": refs, "records": (records(slug) + inbound(slug)) if root is None else [], "chunks": chunked(refs),
              "unlanded": [r["ref"] for r in refs if not r["landed"]]}
    return packet


def show(slug: str, chunk_id: str, runs: Path | None = None, candidates: Path | None = None) -> str:
    """One chunk as a reader needs it: each reference, the candidate's lines that cite it, and its source window.

    A barred line is printed as `[gesperrt]`: it is read for its context by the session, never shown to a reader
    who could quote it.
    """
    d = run_dir(slug, runs)
    packet = json.loads((d / "packet.json").read_text(encoding="utf-8"))
    page = ((candidates or CANDIDATES) / f"{slug}.md").read_text(encoding="utf-8").split("\n")
    out = []
    if chunk_id == "records":
        for r in packet.get("records", []):
            path, _, no = r["ref"].rpartition(":")
            lines = (ROOT / path).read_text(encoding="utf-8").split("\n")
            n = int(no)
            out.append(f"=== {r['ref']}  ({r.get('origin', 'records')})")
            for k in range(max(1, n - 1), min(len(lines), n + 1) + 1):
                text = lines[k - 1]
                out.append(f"{'>' if k == n else ' '} {k:>5}  {'[gesperrt]' if BARRED.search(text) else text}")
        return "\n".join(out) + "\n"
    chunk = next((c for c in packet["chunks"] if c["id"] == chunk_id), None)
    if chunk is None:
        raise SystemExit(f"no chunk {chunk_id}; chunks are {', '.join(c['id'] for c in packet['chunks'])} and records")
    by_ref = {r["ref"]: r for r in packet["refs"]}
    for ref in chunk["refs"]:
        r = by_ref[ref]
        out.append(f"=== {ref}  (reading: {', '.join(r['readings']) or 'lead or differences'}){'  BARRED' if r['barred'] else ''}")
        for no in r["page_lines"]:
            out.append(f"  page L{no}: {page[no - 1].strip()[:400]}")
        for n, text in source_lines(r["doc"], r["window"][0], r["window"][1]):
            mark = ">" if r["first"] <= n <= r["last"] else " "
            out.append(f"{mark} {n:>5}  {'[gesperrt]' if BARRED.search(text) else text}")
    return "\n".join(out) + "\n"


# --- the run ---------------------------------------------------------------------

def read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    return [json.loads(line) for line in path.read_text(encoding="utf-8").splitlines() if line.strip()]


def run_dir(slug: str, runs: Path | None = None) -> Path:
    return (runs or RUNS) / slug


def join(slug: str, runs: Path | None = None) -> list[dict]:
    """The chunk ledgers as one ledger, chunk thought ids mapped to the final thoughts that join them."""
    d = run_dir(slug, runs)
    packet = json.loads((d / "packet.json").read_text(encoding="utf-8"))
    thoughts = read_jsonl(d / "thoughts.jsonl")
    final_of: dict[str, list[str]] = {}
    for t in thoughts:
        for local in t.get("from", []):
            final_of.setdefault(local, []).append(t["id"])
    rows, problems = [], []
    for chunk in packet["chunks"]:
        mine = read_jsonl(d / "chunks" / f"{chunk['id']}.ledger.jsonl")
        for row in mine:
            mapped = sorted({f for local in row.get("thoughts", []) for f in final_of.get(local, [local] if local.startswith("g-") else [])})
            if row.get("state") == "used" and not mapped:
                problems.append(f"chunk {chunk['id']}: {row['ref']} is used by {row.get('thoughts')}, which no final thought joins")
            rows.append({**row, "thoughts": mapped, "chunk": chunk["id"]})
    for row in read_jsonl(d / "records.ledger.jsonl"):
        mapped = sorted({f for local in row.get("thoughts", []) for f in final_of.get(local, [local] if local.startswith("g-") else [])})
        rows.append({**row, "thoughts": mapped, "chunk": "records"})
    if problems:
        raise SystemExit("refused — " + "; ".join(problems[:10]))
    with (d / "ledger.jsonl").open("w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    return rows


def status(slug: str, runs: Path | None = None) -> dict:
    d = run_dir(slug, runs)
    packet = json.loads((d / "packet.json").read_text(encoding="utf-8"))
    seen: dict[str, str] = {}
    done = []
    for chunk in packet["chunks"]:
        rows = {r["ref"]: r.get("state") for r in read_jsonl(d / "chunks" / f"{chunk['id']}.ledger.jsonl")}
        seen.update(rows)
        if all(rows.get(ref) in STATES for ref in chunk["refs"]):
            done.append(chunk["id"])
    for r in read_jsonl(d / "records.ledger.jsonl"):
        seen[r["ref"]] = r.get("state")
    wanted = [r["ref"] for r in packet["refs"]] + [r["ref"] for r in packet.get("records", [])]
    counts = {s: sum(1 for ref in wanted if seen.get(ref) == s) for s in STATES}
    return {"refs": len(wanted), "states": counts, "open": [ref for ref in wanted if seen.get(ref) not in STATES],
            "chunks": len(packet["chunks"]), "chunks_done": done,
            "next": next((c["id"] for c in packet["chunks"] if c["id"] not in done), None)}


# --- the page ----------------------------------------------------------------------

def cite_text(src: dict) -> str:
    stance = "" if src.get("stance", "asserts") == "asserts" else f" ({STANCES.get(src['stance'], src['stance'])})"
    quote = f"„{src['quote']}“ " if src.get("quote") else ""
    return f"{quote}^[{src['ref']}]{stance}"


def bullet(t: dict) -> str:
    text = t["text"].strip()
    parts = [f"- [{t['tag']}] ({t['id']}) {text}"]
    if t.get("sources"):
        parts.append(" — " + " · ".join(cite_text(s) for s in t["sources"]))
    if t.get("refs"):
        parts.append(" (aus " + ", ".join(t["refs"]) + ")")
    if t.get("involves"):
        parts.append(" · Bezug: " + ", ".join(f"[[{s}]]" for s in t["involves"]))
    if t.get("differs_from"):
        parts.append(" · anders als " + ", ".join(t["differs_from"]))
    if t.get("links"):
        parts.append(" (" + ", ".join(f"[{Path(x).stem}]({x})" for x in t["links"]) + ")")
    return "".join(parts)


def coverage_lines(slug: str, ledger: list[dict], thoughts: list[dict], packet: dict) -> list[str]:
    counts = {s: sum(1 for r in ledger if r.get("state") == s) for s in STATES}
    docs = sorted({r["doc"] for r in packet["refs"]})
    used_docs = sorted({s["ref"].split(".md:")[0] for t in thoughts for s in t.get("sources", [])})
    per_kind = {k: sum(1 for t in thoughts if t["kind"] == k) for k, _ in KINDS}
    run = f"Plan/runs/digest/{slug}/"
    return [
        f"- [D] {len(ledger)} Belegstellen gelesen ({len(packet['refs'])} der Kandidatenseite, {len(packet.get('records', []))} aus den Projektunterlagen): "
        + ", ".join(f"{n} {s}" for s, n in counts.items() if n) + f" (`{run}ledger.jsonl`).",
        f"- [D] {len(thoughts)} Gedanken: " + ", ".join(f"{n} {k}" for k, n in per_kind.items() if n)
        + f"; {len(used_docs)} von {len(docs)} Dokumenten tragen mindestens einen (`python3 scripts/digest.py status {slug}`).",
    ]


def write(slug: str, today: str | None = None, runs: Path | None = None, terms_dir: Path | None = None,
          candidates: Path | None = None) -> Path:
    d = run_dir(slug, runs)
    packet = json.loads((d / "packet.json").read_text(encoding="utf-8"))
    thoughts = read_jsonl(d / "thoughts.jsonl")
    ledger = read_jsonl(d / "ledger.jsonl")
    cand = (candidates or CANDIDATES) / f"{slug}.md"
    from wiki_index import frontmatter
    meta = frontmatter(cand.read_text(encoding="utf-8"))
    target = (terms_dir or TERMS) / f"{slug}.md"
    author = f"{AUTHOR_OPEN}\n{AUTHOR_CLOSE}"
    if target.exists():
        old = target.read_text(encoding="utf-8")
        a, b = old.find(AUTHOR_OPEN), old.find(AUTHOR_CLOSE)
        if a >= 0 and b > a:
            author = old[a:b + len(AUTHOR_CLOSE)]
        if frontmatter(old).get("status") == "approved":
            raise SystemExit(f"refused: {target.name} is approved — a new full read starts a draft only on the author's word")
    today = today or datetime.date.today().isoformat()
    out = ["---", f"term: {meta.get('term') or slug}", "status: draft", "kind: konzept", "form: gedanken",
           f"candidate: {slug}", f"candidate_hash: {packet['candidate_hash']}", f"read: {packet['planned']}",
           f"citations: {len(packet['refs'])}", f"thoughts: {len(thoughts)}", f"written: {today}", "by: session", "---", "",
           f"# {meta.get('term') or slug}", ""]
    for kind, title in KINDS:
        out += [f"## {title}", ""]
        mine = [t for t in thoughts if t["kind"] == kind]
        out += [bullet(t) for t in mine] or ["- [L] Die vollständige Lektüre hat hierzu keinen Gedanken gefunden."]
        out.append("")
    out += ["## Vollständigkeit", ""] + coverage_lines(slug, ledger, thoughts, packet) + [""]
    out += ["## Autor-Notizen", "", author, ""]
    out += ["## Herkunft", "",
            f"- [D] Vollständige Lektüre der [Kandidatenseite](../candidates/{slug}.md) im Stand vom {packet['planned']}, "
            f"jede zitierte Zeile mit ihrem Umfeld geöffnet (`Plan/runs/digest/{slug}/`). Ein Entwurf: geprüft und bestätigt ist "
            f"die Seite erst mit dem Wort des Autors.", ""]
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text("\n".join(out), encoding="utf-8")
    return target


# --- the check -----------------------------------------------------------------------

def problems_of(slug: str, runs: Path | None = None, terms_dir: Path | None = None,
                candidates: Path | None = None, verify=None) -> tuple[list[str], list[str]]:
    """(failures, notes) for one thought page and its run."""
    from wiki_index import frontmatter
    fail, note = [], []
    d = run_dir(slug, runs)
    page = (terms_dir or TERMS) / f"{slug}.md"
    if not (d / "packet.json").exists():
        return [f"no run: {d} has no packet.json"], []
    packet = json.loads((d / "packet.json").read_text(encoding="utf-8"))
    thoughts = read_jsonl(d / "thoughts.jsonl")
    ledger = read_jsonl(d / "ledger.jsonl")
    by_id = {t["id"]: t for t in thoughts}
    if len(by_id) != len(thoughts):
        fail.append("thoughts.jsonl repeats an id")

    # Every reference of the candidate and of the project's records has exactly one ledger row with a state.
    wanted = [r["ref"] for r in packet["refs"]] + [r["ref"] for r in packet.get("records", [])]
    rows: dict[str, list[dict]] = {}
    for row in ledger:
        rows.setdefault(row["ref"], []).append(row)
    missing = [ref for ref in wanted if ref not in rows]
    if missing:
        fail.append(f"{len(missing)} reference(s) without a ledger row: {', '.join(missing[:6])}")
    doubled = [ref for ref, rs in rows.items() if len(rs) > 1]
    if doubled:
        fail.append(f"{len(doubled)} reference(s) with more than one ledger row: {', '.join(doubled[:6])}")
    for ref, rs in rows.items():
        state = rs[0].get("state")
        if state not in STATES:
            fail.append(f"{ref}: state {state!r} is not one of {', '.join(STATES)}")
        elif state == "used":
            unknown = [t for t in rs[0].get("thoughts", []) if t not in by_id]
            if not rs[0].get("thoughts") or unknown:
                fail.append(f"{ref}: used, but names no thought on the page" + (f" ({', '.join(unknown)})" if unknown else ""))
        elif state in ("same-as", "defect") and not rs[0].get("note"):
            fail.append(f"{ref}: {state} without a note saying where or what")

    # Every thought is cited, tagged, of a known kind; a joining thought has its grouping.
    groupings = {g["thought"] for g in read_jsonl(d / "groupings.jsonl")}
    barred_refs = {r["ref"] for r in packet["refs"] if r.get("barred")}
    for t in thoughts:
        where = t.get("id", "?")
        if t.get("kind") not in dict(KINDS):
            fail.append(f"{where}: kind {t.get('kind')!r} is not one of {', '.join(k for k, _ in KINDS)}")
        if t.get("tag") not in TAGS:
            fail.append(f"{where}: tag {t.get('tag')!r} is not one of {', '.join(TAGS)}")
        srcs = t.get("sources", [])
        if t.get("tag") in ("S", "V") and not srcs:
            fail.append(f"{where}: [{t.get('tag')}] cites no source")
        if t.get("tag") == "K" and not t.get("links"):
            fail.append(f"{where}: [K] links no decision of the author's")
        if t.get("tag") == "D" and not (t.get("refs") or t.get("links") or srcs):
            fail.append(f"{where}: [D] names nothing it is derived from")
        for r in t.get("refs", []):
            if r not in by_id:
                fail.append(f"{where}: derived from {r}, which is no thought")
        for s in srcs:
            if s.get("stance", "asserts") not in STANCES:
                fail.append(f"{where}: stance {s.get('stance')!r} is not one of {', '.join(STANCES)}")
            if s["ref"] in barred_refs:
                fail.append(f"{where}: cites {s['ref']}, a barred line")
            if s.get("quote") and verify and not verify(s["ref"], s["quote"]):
                fail.append(f"{where}: the quotation is not on {s['ref']}: {s['quote'][:50]!r}")
        if BARRED.search(t.get("text", "")) or any(BARRED.search(s.get("quote", "")) for s in srcs):
            fail.append(f"{where}: writes a name that is read and never written")
        docs = {s["ref"].split(".md:")[0] for s in srcs}
        if len(docs) > 1 and where not in groupings:
            fail.append(f"{where}: joins {len(docs)} documents without a row in groupings.jsonl")
        for other in t.get("differs_from", []):
            if other not in by_id:
                fail.append(f"{where}: differs from {other}, which is no thought")

    # Every document the candidate reads is in a thought or set aside in the ledger.
    covered = {r["doc"] for r in packet["refs"] if rows.get(r["ref"])}
    for doc in sorted({r["doc"] for r in packet["refs"]} - covered):
        fail.append(f"document {doc} has no ledger row")

    # The page is the rendering of the run, and the candidate has not moved under it.
    if not page.exists():
        fail.append(f"no thought page {page.name}")
    else:
        text = page.read_text(encoding="utf-8")
        meta = frontmatter(text)
        if meta.get("form") != "gedanken":
            fail.append("the page is not form: gedanken")
        heads = [line[3:].strip() for line in text.split("\n") if line.startswith("## ")]
        if heads != SECTIONS:
            fail.append(f"sections are {heads}, not {SECTIONS}")
        on_page = {m.group(1) for line in text.split("\n") for m in [THOUGHT_ID.match(line)] if m}
        if on_page != set(by_id):
            fail.append(f"the page and thoughts.jsonl disagree: {len(on_page ^ set(by_id))} thought(s) differ — run write")
        if BARRED.search(text):
            fail.append("the page writes a name that is read and never written")
        cand = (candidates or CANDIDATES) / f"{slug}.md"
        if cand.exists() and page_hash(cand.read_text(encoding="utf-8")) != packet["candidate_hash"]:
            now = refs_of(cand.read_text(encoding="utf-8"))
            new = [ref for ref in now if ref not in {r["ref"] for r in packet["refs"]}]
            note.append(f"behind: the candidate changed since the full read of {packet['planned']}"
                        + (f"; {len(new)} new reference(s) to read" if new else ""))
    return fail, note


def verifier():
    import quotes

    def ok(ref: str, quote: str) -> bool:
        return quotes.resolve(ref, None, quote) is None
    return ok


def check(slug: str | None = None) -> tuple[dict, dict]:
    from wiki_index import frontmatter
    slugs = [slug] if slug else [p.stem for p in sorted(TERMS.glob("*.md"))
                                 if p.stem != "README" and frontmatter(p.read_text(encoding="utf-8")).get("form") == "gedanken"]
    fails, notes = {}, {}
    ok = verifier()
    for s in slugs:
        fails[s], notes[s] = problems_of(s, verify=ok)
    return fails, notes


# --- selftest --------------------------------------------------------------------------

def selftest() -> int:
    results: list[tuple[str, bool]] = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        cands, terms_dir, runs = root / "candidates", root / "terms", root / "runs"
        for d in (cands, terms_dir, runs / "t" / "chunks"):
            d.mkdir(parents=True)
        cand = ("---\nterm: T\nstatus: candidate\ningested: [\"a\", \"b\"]\n---\n\n# T\n\nLead „x“ ^[a.md:L3].\n\n"
                "## Reading — `a`, 2026-01-01\n\nIt says „x“ ^[a.md:L3] and „y“ ^[a.md:L5].\n\n"
                "## Reading — `b`, 2026-02-01\n\nIt agrees: „x“ ^[b.md:L7]. A heading ^[b.md:L9].\n")
        (cands / "t.md").write_text(cand, encoding="utf-8")
        refs = list(refs_of(cand).values())
        results.append(("refs_of finds every distinct reference once", sorted(r["ref"] for r in refs) == ["a.md:L3", "a.md:L5", "b.md:L7", "b.md:L9"]))
        results.append(("refs_of records the reading a reference stands in", refs_of(cand)["a.md:L3"]["readings"] == ["a"]))
        for r in refs:
            r["window"], r["barred"], r["landed"] = [max(1, r["first"] - 2), r["last"] + 2], r["ref"] == "b.md:L9", True
        packet = {"slug": "t", "planned": "2026-10-23", "candidate_hash": page_hash(cand), "refs": refs, "records": [],
                  "chunks": chunked(refs), "unlanded": []}
        d = runs / "t"
        (d / "packet.json").write_text(json.dumps(packet), encoding="utf-8")
        chunk = [{"ref": "a.md:L3", "state": "used", "thoughts": ["c01-01"]},
                 {"ref": "a.md:L5", "state": "used", "thoughts": ["c01-02"]},
                 {"ref": "b.md:L7", "state": "used", "thoughts": ["c01-01"]},
                 {"ref": "b.md:L9", "state": "barred", "thoughts": []}]
        thoughts = [{"id": "g-001", "kind": "definition", "tag": "S", "text": "Der Begriff ist x.", "from": ["c01-01"],
                     "sources": [{"ref": "a.md:L3", "stance": "asserts", "quote": "x"}, {"ref": "b.md:L7", "stance": "proposes"}]},
                    {"id": "g-002", "kind": "mechanism", "tag": "S", "text": "Er wirkt als y.", "from": ["c01-02"],
                     "sources": [{"ref": "a.md:L5", "stance": "asserts"}]},
                    {"id": "g-003", "kind": "kurz", "tag": "D", "text": "Kurz gesagt: x, das als y wirkt.", "refs": ["g-001", "g-002"]}]
        groupings = [{"thought": "g-001", "docs": ["a", "b"], "why": "both lines say x"}]

        def put(name: str, rows: list[dict]) -> None:
            (d / name).write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")

        def run(chunk_rows=None, thought_rows=None, grouping_rows=None, verify=None, page_edit=None):
            put("chunks/01.ledger.jsonl", chunk if chunk_rows is None else chunk_rows)
            put("thoughts.jsonl", thoughts if thought_rows is None else thought_rows)
            put("groupings.jsonl", groupings if grouping_rows is None else grouping_rows)
            try:
                join("t", runs)
            except SystemExit as e:
                return [str(e)], []
            write("t", "2026-10-23", runs, terms_dir, cands)
            if page_edit:
                p = terms_dir / "t.md"
                p.write_text(page_edit(p.read_text(encoding="utf-8")), encoding="utf-8")
            return problems_of("t", runs, terms_dir, cands, verify)

        f, n = run()
        results.append(("a whole run passes", f == [] and n == []))
        page = (terms_dir / "t.md").read_text(encoding="utf-8")
        results.append(("write puts every section in order", [l[3:] for l in page.split("\n") if l.startswith("## ")] == SECTIONS))
        results.append(("write renders a stance that is not asserts", "(schlägt vor)" in page))
        results.append(("an empty kind gets an [L] line", "- [L] Die vollständige Lektüre hat hierzu keinen Gedanken gefunden." in page))
        f, _ = run(chunk_rows=chunk[:3])
        results.append(("a reference without a ledger row fails", any("without a ledger row" in x for x in f)))
        f, _ = run(chunk_rows=chunk + [chunk[0]])
        results.append(("a reference with two rows fails", any("more than one ledger row" in x for x in f)))
        f, _ = run(chunk_rows=chunk[:3] + [{"ref": "b.md:L9", "state": "skipped"}])
        results.append(("an unknown state fails", any("is not one of" in x for x in f)))
        f, _ = run(chunk_rows=chunk[:3] + [{"ref": "b.md:L9", "state": "same-as"}])
        results.append(("same-as without a note fails", any("without a note" in x for x in f)))
        f, _ = run(chunk_rows=[{**chunk[0], "thoughts": ["c01-09"]}] + chunk[1:])
        results.append(("a used row whose thought nobody joins is refused by join", any("no final thought joins" in x for x in f)))
        f, _ = run(thought_rows=[{**thoughts[0], "sources": []}] + thoughts[1:])
        results.append(("[S] without a source fails", any("cites no source" in x for x in f)))
        f, _ = run(grouping_rows=[])
        results.append(("joining two documents without a grouping fails", any("groupings.jsonl" in x for x in f)))
        f, _ = run(thought_rows=[{**thoughts[0], "sources": thoughts[0]["sources"] + [{"ref": "b.md:L9"}]}] + thoughts[1:])
        results.append(("citing a barred line fails", any("a barred line" in x for x in f)))
        early = "Mich" "ael"
        f, _ = run(thought_rows=[{**thoughts[1], "text": f"{early} sagt y."}] + [thoughts[0], thoughts[2]])
        results.append(("writing an early name fails", any("read and never written" in x for x in f)))
        f, _ = run(thought_rows=thoughts[:2] + [{**thoughts[2], "refs": []}])
        results.append(("[D] naming nothing fails", any("[D] names nothing" in x for x in f)))
        f, _ = run(thought_rows=[{**thoughts[0], "kind": "misc"}] + thoughts[1:])
        results.append(("an unknown kind fails", any("kind 'misc'" in x for x in f)))
        f, _ = run(thought_rows=thoughts + [{"id": "g-004", "kind": "decided", "tag": "K", "text": "Entschieden."}])
        results.append(("[K] without a decision fails", any("[K] links no decision" in x for x in f)))
        f, _ = run(verify=lambda ref, quote: False)
        results.append(("a quotation not on its line fails", any("not on" in x for x in f)))
        f, _ = run(page_edit=lambda p: p.replace("- [S] (g-002) ", "- [S] "))
        results.append(("a page that is not the run's rendering fails", any("disagree" in x for x in f)))
        f, _ = run(page_edit=lambda p: p.replace("## Offen", "## Sonstiges"))
        results.append(("a missing section fails", any("sections are" in x for x in f)))
        (cands / "t.md").write_text(cand + "\nMore „z“ ^[b.md:L11].\n", encoding="utf-8")
        f, n = run()
        results.append(("a candidate that moved makes the page behind, not failed", f == [] and any("1 new reference" in x for x in n)))
        (cands / "t.md").write_text(cand, encoding="utf-8")
        thoughts_b = [dict(t) for t in thoughts]
        put("thoughts.jsonl", thoughts_b)
        p = terms_dir / "t.md"
        p.write_text(p.read_text(encoding="utf-8").replace(f"{AUTHOR_OPEN}\n", f"{AUTHOR_OPEN}\nNotiz des Autors.\n"), encoding="utf-8")
        write("t", "2026-10-24", runs, terms_dir, cands)
        results.append(("write keeps the author's block", "Notiz des Autors." in p.read_text(encoding="utf-8")))
        p.write_text(p.read_text(encoding="utf-8").replace("status: draft", "status: approved"), encoding="utf-8")
        try:
            write("t", "2026-10-24", runs, terms_dir, cands)
            results.append(("write refuses an approved page", False))
        except SystemExit as e:
            results.append(("write refuses an approved page", "approved" in str(e)))
        many = [{"ref": f"a.md:L{i}", "window": [i, i + 4]} for i in range(1, 400)]
        cs = chunked(many)
        results.append(("chunks hold at most MAX_REFS references and MAX_LINES lines",
                        all(len(c["refs"]) <= MAX_REFS and c["lines"] <= MAX_LINES for c in cs) and sum(len(c["refs"]) for c in cs) == 399))
        (cands / "bare.md").write_text("---\nterm: B\n---\n\n# B\n\nIt says „x“ ^[L3].\n", encoding="utf-8")
        try:
            plan("bare", "2026-10-23", cands)
            results.append(("plan refuses bare references", False))
        except SystemExit as e:
            results.append(("plan refuses bare references", "bare references" in str(e)))
    for name, held in results:
        print(("held  " if held else "FAILED") + "  " + name)
    failed = sum(1 for _, held in results if not held)
    print(f"{len(results) - failed} of {len(results)} held")
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    verb, rest = argv[0], argv[1:]
    if verb == "selftest":
        return selftest()
    if verb == "plan" and rest:
        packet = plan(rest[0])
        d = run_dir(rest[0])
        (d / "chunks").mkdir(parents=True, exist_ok=True)
        (d / "packet.json").write_text(json.dumps(packet, ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
        barred = sum(1 for r in packet["refs"] if r["barred"])
        print(f"{d.relative_to(ROOT)}/packet.json: {len(packet['refs'])} references from "
              f"{len({r['doc'] for r in packet['refs']})} documents, {len(packet['records'])} record lines, "
              f"{barred} barred, {len(packet['unlanded'])} unlanded, {len(packet['chunks'])} chunk(s)")
        for c in packet["chunks"]:
            print(f"  chunk {c['id']}: {len(c['refs'])} references, {c['lines']} window lines")
        return 0
    if verb == "show" and len(rest) >= 2:
        print(show(rest[0], rest[1]), end="")
        return 0
    if verb == "status" and rest:
        print(json.dumps(status(rest[0]), ensure_ascii=False, indent=1))
        return 0
    if verb == "join" and rest:
        rows = join(rest[0])
        print(f"{len(rows)} ledger rows → {run_dir(rest[0]).relative_to(ROOT)}/ledger.jsonl")
        return 0
    if verb == "write" and rest:
        print(f"wrote {write(rest[0]).relative_to(ROOT)}")
        return 0
    if verb == "check":
        fails, notes = check(rest[0] if rest else None)
        for s in fails:
            for f in fails[s]:
                print(f"FAIL  {s}: {f}")
            for n in notes[s]:
                print(f"note  {s}: {n}")
        total = sum(len(v) for v in fails.values())
        print(f"{len(fails)} thought page(s), {total} problem(s)")
        return 1 if total else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
