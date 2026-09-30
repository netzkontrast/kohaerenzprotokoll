#!/usr/bin/env python3
"""The readings brief, drafted where it is mechanical.

A `wiki-reader` is given a batch, its documents and *a brief on what each document says about each page*
(`.claude/agents/wiki-reader.md`). The briefs of documents 52–55 were written by hand, and most of what they hold
is already on disk once the lookup ran:

- the documents, with their dates and lengths — the manifest;
- the pages a reading may go on — `reconcile-pre.json`'s `new_reading` candidates and the sweep's hits;
- the lines each page's surfaces stand on in the document — `counts.json`, the census's own counts;
- the candidates that stand near a page's surface and are no reading yet — the lookup's `needs_judgement`.

`draft` writes all of that and marks what only the reconciler can say `<brief: …>`: what each document is and how
its readings must be worded, what it says about each page, and which near matches are occurrences. `check` fails on a
mark left, and on a page the brief names that does not exist. It decides nothing: a page gets a reading, or does not,
by the reconciler's word and then by the reader's, and a candidate near a page's surface is an occurrence or a reading
by its sentence (J20, J55, J88).

    python3 scripts/brief.py draft <batch> <slug>[@N] [<slug>[@N] …] [--from N]   # Plan/runs/<batch>/brief-draft.md
    python3 scripts/brief.py check <batch>                                # brief.md: no mark left, every page exists
    python3 scripts/brief.py selftest

Standard library only.
"""

from __future__ import annotations

import json
import re
import sys
import tempfile
from collections import defaultdict
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

MARK = "<brief:"
CENTRAL = 10          # a page whose surfaces stand on this many lines or more is central: 3–12 quotations, not 1–4


def read_jsonl(path: Path) -> list[dict]:
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()] if path.exists() else []


def manifest_row(slug: str, root: Path = ROOT) -> dict:
    for row in read_jsonl(root / "Sources" / "manifest.jsonl"):
        if row["slug"] == slug:
            return row
    raise SystemExit(f"{slug} is not in the manifest")


def length(slug: str, root: Path = ROOT) -> int:
    path = root / "Sources" / "drive" / f"{slug}.md"
    return len(path.read_text(encoding="utf-8").split("\n")) if path.exists() else 0


def run_json(slug: str, name: str, root: Path = ROOT) -> dict:
    path = root / "Plan" / "runs" / slug / name
    if not path.exists():
        raise SystemExit(f"{path.relative_to(root)} is missing — run `python3 scripts/reconcile.py {slug}` "
                         f"(and `capture.py {slug} --count`) first")
    return json.loads(path.read_text(encoding="utf-8"))


def pages_of(slug: str, root: Path = ROOT) -> tuple[dict, list[dict], dict]:
    """What the lookup says a reading may go on: {page: {surface: lines}}, the sweep's hits, and the candidates that stand
    near a page's surface without being a reading — {page: [(candidate, surface)]}."""
    pre, counts = run_json(slug, "reconcile-pre.json", root), run_json(slug, "counts.json", root)["counts"]
    pages: dict[str, dict[str, list[int]]] = defaultdict(dict)
    for row in pre["buckets"]["new_reading"]:
        pages[row["page"]][row["candidate"]] = counts.get(row["candidate"], {}).get("lines", [])
    near: dict[str, list[tuple[str, str]]] = defaultdict(list)
    for row in pre["buckets"]["needs_judgement"]:
        for n in row.get("near", []):
            near[n["page"]].append((row["candidate"], n["surface"]))
    return pages, pre.get("in_document_not_in_census", []), near


def spans(lines: list[int], limit: int = 14) -> str:
    shown = ", ".join(f"L{n}" for n in lines[:limit])
    return shown + (f", … ({len(lines)} lines)" if len(lines) > limit else "")


def draft(batch: str, slugs: list[str], first: int, root: Path = ROOT, numbers: dict[str, int] | None = None) -> str:
    """`numbers` gives a document its own number where the batch skips one (`slug@59`); otherwise they run on from `first`."""
    numbers = {s: (numbers or {}).get(s, first + i) for i, s in enumerate(slugs)}
    docs = {s: manifest_row(s, root) for s in slugs}
    low, high = min(numbers.values()), max(numbers.values())
    out = [f"# Brief — readings from document{'s' if high != low else ''} {low}" + (f"–{high}" if high != low else "") + " (step 6)", "",
           f"{len(slugs)} document{'s' if len(slugs) > 1 else ''}, one reader, one batch: `{batch}`. Files go to "
           f"`Plan/runs/{batch}/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.", "",
           "| n | slug | date | prose name | what it is |", "|---|---|---|---|---|"]
    for s, r in docs.items():
        out.append(f"| {numbers[s]} | `{s}` | {r.get('index_date', '')[:10]} | {MARK} the name the reading calls it> | "
                   f"{MARK} what it is, in one clause, and how it stands>|")
    out += ["", "Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and "
            "`Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` "
            f"({', '.join(f'{length(s, root)} lines for `{s[:30]}`' for s in docs)}). For each page, its digest: "
            "`python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.", "",
            f"**Stance — record, never apply.** {MARK} how each document's readings must be worded: a plan says what it wants, a review "
            "what it reports, a proposal what it proposes; a name inside an example is the example's>", ""]
    for s in docs:
        pages, sweep, near = pages_of(s, root)
        out += [f"## Pages — document {numbers[s]}, `{s}`", ""]
        hits = defaultdict(list)
        for h in sweep:
            hits[h["page"]].append(h)
        for page in sorted(set(pages) | set(hits)):
            surfaces = pages.get(page, {})
            lines = sorted({n for ls in surfaces.values() for n in ls} | {h["line"] for h in hits.get(page, [])})
            size = "central, 3–12 quotations" if len(lines) >= CENTRAL else "minor, 1–4"
            cens = "; ".join(f"`{c}` {spans(ls, 6)}" for c, ls in surfaces.items()) or "no candidate"
            sweep_txt = "".join(f" The sweep found `{h['surface']}` alone on L{h['line']}"
                                f"{' (already read from this document)' if h.get('already_read') else ''}." for h in hits.get(page, []))
            out.append(f"- **`{page}`** ({size}): the census's surfaces — {cens}.{sweep_txt} {MARK} what the document says about it, "
                       f"with its lines, or „not read: why“>")
        occurrences = {p: v for p, v in near.items() if p not in pages}
        out += ["", "**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**", ""]
        if occurrences:
            for page, cands in sorted(occurrences.items()):
                out.append(f"- `{page}`: " + ", ".join(f"`{c}` (near `{sf}`)" for c, sf in cands[:6])
                           + (f", … ({len(cands)})" if len(cands) > 6 else "") + f". {MARK} an occurrence, and why — or a reading, and its lines>")
        else:
            out.append("- none")
        out.append("")
    return "\n".join(out) + "\n"


def check(batch: str, root: Path = ROOT) -> list[str]:
    path = root / "Plan" / "runs" / batch / "brief.md"
    if not path.exists():
        return [f"Plan/runs/{batch}/brief.md does not exist"]
    text = path.read_text(encoding="utf-8")
    problems = [f"a mark is left: {m.group(0)[:70]}…" for m in re.finditer(re.escape(MARK) + r"[^>]*>", text)]
    exists = {p.stem for folder in ("candidates", "chapters", "conflicts", "questions") for p in (root / "Wiki" / folder).glob("*.md")}
    for m in re.finditer(r"^- \*\*`([a-z0-9-]+)`\*\*", text, re.M):
        if m.group(1) not in exists:
            problems.append(f"the brief names a page that does not exist: {m.group(1)}")
    return problems


def selftest() -> int:
    cases = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "Sources" / "drive").mkdir(parents=True)
        (root / "Sources" / "manifest.jsonl").write_text(json.dumps({"slug": "doc-a", "index_date": "2026-03-01T00:00:00Z"}) + "\n", encoding="utf-8")
        (root / "Sources" / "drive" / "doc-a.md").write_text("a\nb\nc\n", encoding="utf-8")
        run = root / "Plan" / "runs" / "doc-a"
        run.mkdir(parents=True)
        (run / "reconcile-pre.json").write_text(json.dumps({
            "buckets": {"new_reading": [{"candidate": "AEGIS", "page": "aegis", "readings": 5},
                                        {"candidate": "DKT", "page": "dkt", "readings": 2}],
                        "needs_judgement": [{"candidate": "Kohärenz-Wahrheit", "near": [{"surface": "koharenz", "page": "kohaerenz"}]},
                                            {"candidate": "A / B", "near": []}]},
            "in_document_not_in_census": [{"page": "aegis", "surface": "AEGIS", "line": 9, "already_read": False}]}), encoding="utf-8")
        (run / "counts.json").write_text(json.dumps({"counts": {"AEGIS": {"n": 12, "lines": list(range(1, 13))},
                                                               "DKT": {"n": 1, "lines": [3]}}}), encoding="utf-8")
        for folder, name in (("candidates", "aegis"), ("candidates", "dkt"), ("candidates", "kohaerenz")):
            (root / "Wiki" / folder).mkdir(parents=True, exist_ok=True)
            (root / "Wiki" / folder / f"{name}.md").write_text("x", encoding="utf-8")
        for folder in ("chapters", "conflicts", "questions"):
            (root / "Wiki" / folder).mkdir(parents=True, exist_ok=True)
        text = draft("b1", ["doc-a"], 56, root)
        cases.append(("the document is a row with its date from the manifest", "| 56 | `doc-a` | 2026-03-01 |" in text))
        cases.append(("a batch that skips a number names it", "| 59 | `doc-a` |" in draft("b1", ["doc-a"], 56, root, {"doc-a": 59})
                      and "readings from document 59 (step 6)" in draft("b1", ["doc-a"], 56, root, {"doc-a": 59})))
        cases.append(("a page reads central from twelve lines and minor from one",
                      "**`aegis`** (central, 3–12 quotations)" in text and "**`dkt`** (minor, 1–4)" in text))
        cases.append(("a page's surfaces come with their lines", "`AEGIS` L1, L2, L3, L4, L5, L6, … (12 lines)" in text))
        cases.append(("a sweep hit is named with its line", "The sweep found `AEGIS` alone on L9." in text))
        cases.append(("a candidate near a page's surface is listed as an occurrence to decide",
                      "`kohaerenz`: `Kohärenz-Wahrheit` (near `koharenz`)" in text))
        cases.append(("every judgement is a mark, none is decided", text.count(MARK) >= 6))
        (root / "Plan" / "runs" / "b1").mkdir(parents=True)
        (root / "Plan" / "runs" / "b1" / "brief.md").write_text(text, encoding="utf-8")
        cases.append(("a brief with its marks left fails", any("a mark is left" in p for p in check("b1", root))))
        filled = re.sub(re.escape(MARK) + r"[^>]*>", "done", text)
        (root / "Plan" / "runs" / "b1" / "brief.md").write_text(filled, encoding="utf-8")
        cases.append(("a brief with every mark filled passes", check("b1", root) == []))
        (root / "Plan" / "runs" / "b1" / "brief.md").write_text(filled + "\n- **`no-such-page`** (minor, 1–4): x\n", encoding="utf-8")
        cases.append(("a page that does not exist fails", any("no-such-page" in p for p in check("b1", root))))
    failed = [n for n, ok in cases if not ok]
    print(f"brief: {len(cases) - len(failed)} of {len(cases)} cases hold" + (" — FAILED: " + ", ".join(failed) if failed else ""))
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        return selftest()
    if argv[:1] == ["draft"] and len(argv) >= 3:
        rest = argv[1:]
        first = None
        if "--from" in rest:
            first = int(rest[rest.index("--from") + 1])
            del rest[rest.index("--from"):rest.index("--from") + 2]
        batch = rest[0]
        numbers = {a.split("@")[0]: int(a.split("@")[1]) for a in rest[1:] if "@" in a}
        slugs = [a.split("@")[0] for a in rest[1:]]
        if first is None:
            import record
            first = record.next_number()
        text = draft(batch, slugs, first, numbers=numbers)
        out = ROOT / "Plan" / "runs" / batch
        out.mkdir(parents=True, exist_ok=True)
        (out / "brief-draft.md").write_text(text, encoding="utf-8")
        print(f"wrote Plan/runs/{batch}/brief-draft.md — fill every `{MARK}` mark, then save it as brief.md")
        return 0
    if argv[:1] == ["check"] and len(argv) == 2:
        problems = check(argv[1])
        for p in problems:
            print("FAIL", p)
        print(f"brief {argv[1]}: {'holds' if not problems else 'FAILS'}")
        return 1 if problems else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
