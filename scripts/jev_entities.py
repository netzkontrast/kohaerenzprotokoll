#!/usr/bin/env python3
"""Entity list by script plus Jev: code finds every candidate and its line, Jev
judges each one. A test of the route NOW.md proposes, not a pipeline step.

    .venv-typesafe/bin/python scripts/jev_entities.py <slug> [--replay]

1. Candidates are mechanical: every capitalised or digit-bearing token, hyphen
   compound, and **bold** / `code` / first-table-cell span of up to five words,
   each with its first file line and its count. A line is never typed by a model,
   so it cannot be wrong (P26).
2. The document is cut into windows of WINDOW lines written as `L052| …`. Each
   candidate is asked about in the window of its first occurrence, one Noul per
   candidate, all candidates of a window in one request, so the window is paid once.
3. Every request and response is written to Plan/runs/jev/<slug>/, and --replay
   answers from there with no key and no network (P5).

Output: Plan/runs/jev/<slug>/list.md in the Plan/entities format, ranked by
Jev's probability and then by count, capped at CAP rows. It is a model's reading
under the same rules as Plan/entities/ — never a census, a page or a count.
"""
from __future__ import annotations

import hashlib
import json
import re
import sys
import time
from collections import Counter
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "Plan" / "runs" / "jev"
WINDOW = 40        # lines of state per request
MAX_Q = 80         # questions per request; a window with more is split
CAP = 100          # rows kept, the size the Haiku lists aim at
WORKERS = 6        # the public endpoint rate-limits above about eight

WORD = r"[A-ZÄÖÜ0-9][\w₀-₉ÄÖÜäöüß]*(?:[-/][\w₀-₉ÄÖÜäöüß]+)*"
TOKEN = re.compile(rf"(?<![\w-])(?:{WORD}|[a-zäöüß]+[A-ZÄÖÜ0-9][\w-]*)(?![\w])")
SPAN = re.compile(r"\*\*([^*\n]{2,60}?)\*\*|`([^`\n]{2,60})`|^\|\s*([^|\n]{2,60}?)\s*\|")
MIN_LEN = 2

QUESTION = ("In this document, is `{c}` an entity: something the document treats as "
            "a thing in its own right — a named person or character, place, world or "
            "level, organisation, system, AI, protocol or programme, a coined term of "
            "the world, a technology, an event, a cited work or author, or a named "
            "real-world concept the document builds on? Look at line L{line}.")
TRUE = "a named or coined thing the document refers to as such"
FALSE = ("ordinary German or English vocabulary, a sentence-initial capitalised "
         "word, a template field label, a heading fragment, or a phrase that "
         "merely describes something without naming it")


def lines_of(slug: str) -> list[str]:
    return (ROOT / "Sources" / "drive" / f"{slug}.md").read_text(encoding="utf-8").splitlines()


def body_start(lines: list[str]) -> int:
    """First file line (1-based) after the frontmatter."""
    if lines and lines[0] == "---":
        for i, l in enumerate(lines[1:], 2):
            if l == "---":
                return i + 1
    return 1


def clean(s: str) -> str:
    return s.strip().strip(":.,;*").strip()


def candidates(lines: list[str]) -> dict[str, dict]:
    """{surface: {line, n}} — first file line and count, both mechanical."""
    found: dict[str, dict] = {}
    count: Counter = Counter()
    start = body_start(lines)
    for no, text in enumerate(lines[start - 1:], start):
        surfaces = [m.group(0) for m in TOKEN.finditer(text)]
        for m in SPAN.finditer(text):
            s = clean(next(g for g in m.groups() if g))
            if s and len(s.split()) <= 5 and not set(s) <= set("-:| "):
                surfaces.append(s)
        for s in surfaces:
            if len(s) < MIN_LEN or s.isdigit():
                continue
            count[s] += 1
            found.setdefault(s, {"line": no})
    for s, d in found.items():
        d["n"] = count[s]
    return found


def requests(slug: str, lines: list[str], cands: dict[str, dict]) -> list[dict]:
    start = body_start(lines)
    by_window: dict[int, list[str]] = {}
    for s, d in cands.items():
        by_window.setdefault((d["line"] - start) // WINDOW, []).append(s)
    out = []
    for w, names in sorted(by_window.items()):
        a = start + w * WINDOW
        b = min(a + WINDOW, len(lines) + 1)
        state = {"document": slug,
                 "lines": "\n".join(f"L{i:03d}| {lines[i - 1]}" for i in range(a, b))}
        for k in range(0, len(names), MAX_Q):
            chunk = names[k:k + MAX_Q]
            qs = {f"q{i}": {"surface": s, "text": QUESTION.format(c=s, line=cands[s]["line"])}
                  for i, s in enumerate(chunk)}
            key = hashlib.sha256(json.dumps([state, qs], ensure_ascii=False,
                                            sort_keys=True).encode()).hexdigest()[:16]
            out.append({"key": key, "window": [a, b - 1], "state": state, "questions": qs})
    return out


def call(req: dict, cache: Path, replay: bool) -> dict:
    path = cache / f"{req['key']}.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    if replay:
        return {"key": req["key"], "unreached": "not in the recording"}
    from typesafe_sdk import TypeSafeClient, Noul, NoulCriteria, RetryPolicy
    qs = {k: Noul(instructions=q["text"], criteria=NoulCriteria(true=TRUE, false=FALSE))
          for k, q in req["questions"].items()}
    t = time.time()
    try:
        with TypeSafeClient(timeout=120, retry=RetryPolicy(max_retries=5, backoff_initial=1.0,
                                                           backoff_max=20.0)) as c:
            r = c.system_one(state=req["state"], questions=qs)
    except Exception as e:  # a call that never returned is not an answer (P15)
        return {"key": req["key"], "unreached": f"{type(e).__name__}: {e}"}
    rec = {"key": req["key"], "model": r.model, "seconds": round(time.time() - t, 2),
           "input_tokens": r.usage.input_tokens, "output_tokens": r.usage.output_tokens,
           "window": req["window"], "state": req["state"],
           "answers": {k: {"surface": req["questions"][k]["surface"],
                           "noul": r.nouls[k].noul} for k in qs}}
    path.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
    return rec


def main(argv: list[str]) -> int:
    replay = "--replay" in argv
    slugs = [a for a in argv if not a.startswith("--")]
    if len(slugs) != 1:
        print(__doc__)
        return 2
    slug = slugs[0]
    lines = lines_of(slug)
    cands = candidates(lines)
    reqs = requests(slug, lines, cands)
    cache = OUT / slug / "calls"
    cache.mkdir(parents=True, exist_ok=True)
    t = time.time()
    with ThreadPoolExecutor(WORKERS) as pool:
        recs = list(pool.map(lambda r: call(r, cache, replay), reqs))
    wall = time.time() - t
    unreached = [r for r in recs if "unreached" in r]
    p = {a["surface"]: a["noul"] for r in recs if "answers" in r for a in r["answers"].values()}
    ranked = sorted((s for s in p if p[s] >= 0.5), key=lambda s: (-p[s], -cands[s]["n"]))
    kept = ranked[:CAP]
    model = next((r["model"] for r in recs if "model" in r), "?")
    body = [f"written_by: script candidates + {model} Noul per candidate, via scripts/jev_entities.py",
            f"source: {slug}", f"lines: {len(lines)}", ""]
    body += [f"- {s}  ^[L{cands[s]['line']}]  · p={p[s]:.2f} n={cands[s]['n']}" for s in kept]
    (OUT / slug / "list.md").write_text("\n".join(body) + "\n", encoding="utf-8")
    stats = {"slug": slug, "lines": len(lines), "candidates": len(cands), "requests": len(reqs),
             "unreached": len(unreached), "judged": len(p), "yes": len(ranked), "kept": len(kept),
             "input_tokens": sum(r.get("input_tokens", 0) for r in recs),
             "output_tokens": sum(r.get("output_tokens", 0) for r in recs),
             "wall_seconds": round(wall, 1), "model": model}
    (OUT / slug / "stats.json").write_text(json.dumps(stats, indent=1), encoding="utf-8")
    print(json.dumps(stats))
    for r in unreached[:5]:
        print("unreached:", r["key"], r["unreached"][:200])
    return 1 if unreached else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
