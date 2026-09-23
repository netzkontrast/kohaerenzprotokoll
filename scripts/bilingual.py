#!/usr/bin/env python3
"""German and English names for the same entity, across the whole corpus.

The corpus is German research that borrows English terms and glosses its own:
`Kernwelten (Core Worlds)`, `Handlungsfähigkeit (Agency)`, and `Wächter` and
`Guardian` in complementary distribution with no overlap (NOW.md). Nothing maps
one to the other, so a search for either misses the other half.

    .venv-typesafe/bin/python scripts/bilingual.py all [--replay]
    .venv-typesafe/bin/python scripts/bilingual.py stated|entities|propose|pairs|write [--replay]

Five stages. Each writes Plan/runs/bilingual/<stage>.jsonl and every model call
is cached under Plan/runs/bilingual/calls/, so `--replay` reruns everything with
no key and no network (P5).

1. **stated**: code. Pairs the corpus writes itself: `A (B)`, `A (engl. B)`,
   `A/B`, with every document and line. The strongest evidence and free.
2. **entities**: Jev. For every surface in MIN_DOCS+ documents, both sides of
   every stated pair and every wiki surface, one Noul: is this an entity or key
   term of the corpus, not ordinary vocabulary? Two of its lines are the state.
3. **propose**: a free OpenRouter model, **names only**. No corpus text goes to
   a free endpoint. For each entity it gives its language and up to three
   counterparts. Code keeps a counterpart only if the corpus contains it.
4. **pairs**: Jev. For every stated or proposed pair, a Choice over how the two
   relate, with the lines where both occur (or each alone) as the state.
5. **write**: Plan/entities/bilingual.md (the pairs) and bilingual.jsonl (every
   entity, with its counterparts or none).

What this may not do is decided elsewhere and holds here. **A mapping is a
proposal, not a merge.** Whether two surfaces are one term is
Plan/runs/judgements.jsonl's question and a person's. No page, link or count is
written from a probability. Every count comes from the corpus search, never from
a model.
"""
from __future__ import annotations

import hashlib
import json
import os
import re
import sys
import time
import urllib.request
from collections import Counter, defaultdict
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import entities as E  # noqa: E402
import subject  # noqa: E402

OUT = ROOT / "Plan" / "runs" / "bilingual"
CALLS = OUT / "calls"
LISTS = ROOT / "Plan" / "entities"
REPLAY = "--replay" in sys.argv

MIN_DOCS = 5          # a surface in fewer documents is judged only if a gloss names it
STATED_MIN_DOCS = 1   # a gloss written once is still the corpus's own statement
CONTEXT = 220         # characters of a line shown per example
JEV_BATCH = 40
JEV_WORKERS = 6       # the public endpoint rate-limits above about eight
OR_BATCH = 80
OR_MODELS = ["qwen/qwen3.8-27b:free", "nvidia/nemotron-3-super-120b-a12b:free",
             "google/gemma-4-31b-it:free"]

# ── surfaces ──────────────────────────────────────────────────────────────────

W = r"[A-ZÄÖÜ][\wÄÖÜäöüß]*(?:-[\wÄÖÜäöüß]+)*"
NAME = rf"{W}(?:\s+(?:{W}|of|the|der|des|die|und|and|for)){{0,3}}"
MARK = r"(?:engl\.?|englisch|en\.|dt\.|deutsch|auch|bzw\.|oder|i\.\s?e\.|d\.\s?h\.|=|aka)\s*:?\s*"
PAREN = re.compile(rf"(?<![\w-])({NAME})\s*\(\s*(?:{MARK})?({NAME})\s*\)")
SLASH = re.compile(rf"(?<![\w-])({W})\s?/\s?({W})(?![\w-])")
LEADING = re.compile(r"^(?:Der|Die|Das|Den|Dem|Des|Ein|Eine|The|A|An)\s+")


def strip_article(s: str) -> str:
    return LEADING.sub("", s).strip()


def write_jsonl(name: str, rows) -> Path:
    OUT.mkdir(parents=True, exist_ok=True)
    path = OUT / f"{name}.jsonl"
    path.write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in rows), encoding="utf-8")
    return path


def read_jsonl(name: str) -> list[dict]:
    path = OUT / f"{name}.jsonl"
    return [json.loads(l) for l in path.read_text(encoding="utf-8").splitlines() if l.strip()]


def stage_stated() -> list[dict]:
    """Every `A (B)` and `A/B` the corpus writes, with the lines that write it."""
    found: dict[tuple[str, str], list] = defaultdict(list)
    for doc in subject.documents():
        for i, raw in enumerate(doc.lines()):
            line = E.plain(raw)
            for rx, shape in ((PAREN, "paren"), (SLASH, "slash")):
                for m in rx.finditer(line):
                    a, b = strip_article(m.group(1)), strip_article(m.group(2))
                    if a == b or min(len(a), len(b)) < 2:
                        continue
                    found[(a, b)].append({"slug": doc.slug, "line": doc.offset + i, "shape": shape})
    rows = []
    for (a, b), where in found.items():
        docs = sorted({w["slug"] for w in where})
        if len(docs) >= STATED_MIN_DOCS:
            rows.append({"a": a, "b": b, "docs": len(docs), "times": len(where),
                         "shape": Counter(w["shape"] for w in where).most_common(1)[0][0],
                         "cites": where[:3]})
    rows.sort(key=lambda r: (-r["docs"], r["a"]))
    write_jsonl("stated", rows)
    print(f"stated: {len(rows)} pairs the corpus writes itself "
          f"({sum(r['docs'] >= 2 for r in rows)} in 2+ documents)")
    return rows


# ── the corpus, once ──────────────────────────────────────────────────────────

class Lines:
    """Occurrences by surface: which documents, how often, and example lines."""

    def __init__(self) -> None:
        self.corpus = E.Corpus()
        self.docs = {d.slug: d for d in subject.documents()}

    def search(self, surfaces: list[str]) -> dict[str, list[dict]]:
        return self.corpus.search(surfaces)

    def text(self, slug: str, line: int) -> str:
        doc = self.docs[slug]
        t = E.plain(doc.lines()[line - doc.offset])
        return t if len(t) <= CONTEXT else t[:CONTEXT] + "…"

    def examples(self, hits: list[dict], k: int = 2) -> list[str]:
        top = sorted(hits, key=lambda h: -h["n"])[:k]
        return [f"{h['slug']}:L{h['first_line']}| {self.text(h['slug'], h['first_line'])}" for h in top]


def universe(stated: list[dict]) -> list[str]:
    """Candidate surfaces: frequent ones, both sides of every gloss, the wiki's own."""
    import jev_entities as J
    docs: Counter = Counter()
    for doc in subject.documents():
        for s in J.candidates(J.lines_of(doc.slug)):
            docs[strip_article(s)] += 1
    out = {s for s, n in docs.items() if n >= MIN_DOCS}
    out |= {r["a"] for r in stated} | {r["b"] for r in stated}
    index = ROOT / "Wiki" / "index.json"
    if index.exists():
        for t in json.loads(index.read_text(encoding="utf-8"))["terms"].values():
            out |= set(t["surfaces"])
    for entry in E.lists():
        out |= {r["term"] for r in entry["rows"]}
    return sorted(s for s in out if len(s) >= 2 and not s.isdigit())


# ── model calls, cached ───────────────────────────────────────────────────────

def cached(kind: str, payload: dict, fetch) -> dict:
    key = hashlib.sha256(json.dumps(payload, ensure_ascii=False, sort_keys=True).encode()).hexdigest()[:20]
    path = CALLS / kind / f"{key}.json"
    if path.exists():
        return json.loads(path.read_text(encoding="utf-8"))
    if REPLAY:
        return {"unreached": "not in the recording"}
    rec = fetch()
    if "unreached" not in rec:  # a call that never returned is not an answer (P15)
        path.parent.mkdir(parents=True, exist_ok=True)
        path.write_text(json.dumps(rec, ensure_ascii=False, indent=1), encoding="utf-8")
    return rec


def jev(state: dict, questions: dict) -> dict:
    def fetch() -> dict:
        from typesafe_sdk import RetryPolicy, TypeSafeClient
        t = time.time()
        try:
            with TypeSafeClient(timeout=120, retry=RetryPolicy(max_retries=5, backoff_initial=1.0,
                                                               backoff_max=20.0)) as c:
                r = c.system_one(state=state, questions=questions)
        except Exception as e:
            return {"unreached": f"{type(e).__name__}: {e}"[:300]}
        ans = {}
        for k in questions:
            a = r.answers[k]
            if hasattr(a, "noul"):
                ans[k] = {"noul": a.noul}
            else:
                ans[k] = {"choice": a.choice, "probabilities": dict(a.probabilities)}
        return {"model": r.model, "seconds": round(time.time() - t, 2),
                "input_tokens": r.usage.input_tokens, "answers": ans}
    payload = {"state": state, "questions": {k: q.model_dump() if hasattr(q, "model_dump") else repr(q)
                                             for k, q in questions.items()}}
    return cached("jev", payload, fetch)


def openrouter(prompt: str) -> dict:
    def fetch() -> dict:
        key = os.environ.get("OPENROUTER_API_KEY")
        if not key:
            return {"unreached": "OPENROUTER_API_KEY is not set"}
        last = ""
        for attempt in range(6):
            model = OR_MODELS[attempt % len(OR_MODELS)]
            body = json.dumps({"model": model, "temperature": 0, "max_tokens": 12000,
                               "response_format": {"type": "json_object"},
                               "messages": [{"role": "user", "content": prompt}]}).encode()
            req = urllib.request.Request("https://openrouter.ai/api/v1/chat/completions", data=body,
                                         headers={"Authorization": f"Bearer {key}",
                                                  "Content-Type": "application/json"})
            try:
                with urllib.request.urlopen(req, timeout=300) as r:
                    d = json.load(r)
                text = d["choices"][0]["message"]["content"]
                parsed = json.loads(text[text.index("{"):text.rindex("}") + 1])
                return {"model": d.get("model", model), "answer": parsed}
            except Exception as e:
                last = f"{model}: {type(e).__name__}: {e}"[:300]
                time.sleep(5 * (attempt + 1))
        return {"unreached": last}
    return cached("openrouter", {"prompt": prompt, "models": OR_MODELS}, fetch)


# ── stage 2: which surfaces are entities ──────────────────────────────────────

ENTITY_Q = ("Across this corpus (German research notes for a hard-SF novel, which borrow English "
            "terms), is `{s}` an entity or key term: something the texts treat as a thing in its own "
            "right? That means a named person or character, place, world or level, organisation, "
            "system, AI, protocol or programme, a coined term of the fictional world, a technology, "
            "a named theory or cited work, or a named concept the research builds on. Its lines are "
            "under examples[\"{s}\"].")
ENTITY_TRUE = "a named, coined or technical thing the texts refer to as such"
ENTITY_FALSE = ("ordinary German or English vocabulary, a function word, a sentence-initial "
                "capitalised word, a heading or template label, or a phrase that describes "
                "rather than names")


def stage_entities(lines: Lines) -> list[dict]:
    from typesafe_sdk import Noul, NoulCriteria
    stated = read_jsonl("stated")
    surfaces = universe(stated)
    hits = lines.search(surfaces)
    surfaces = [s for s in surfaces if hits[s]]
    batches = [surfaces[i:i + JEV_BATCH] for i in range(0, len(surfaces), JEV_BATCH)]

    def ask(batch: list[str]) -> dict:
        state = {"examples": {s: lines.examples(hits[s]) for s in batch}}
        qs = {f"q{i}": Noul(instructions=ENTITY_Q.format(s=s),
                            criteria=NoulCriteria(true=ENTITY_TRUE, false=ENTITY_FALSE))
              for i, s in enumerate(batch)}
        return jev(state, qs)

    t = time.time()
    with ThreadPoolExecutor(JEV_WORKERS) as pool:
        recs = list(pool.map(ask, batches))
    rows, unreached = [], 0
    for batch, rec in zip(batches, recs):
        if "unreached" in rec:
            unreached += len(batch)
            continue
        for i, s in enumerate(batch):
            rows.append({"surface": s, "p": round(rec["answers"][f"q{i}"]["noul"], 4),
                         "docs": len(hits[s]), "n": sum(h["n"] for h in hits[s]),
                         "first": {"slug": hits[s][0]["slug"], "line": hits[s][0]["first_line"]}})
    write_jsonl("entities", rows)
    tokens = sum(r.get("input_tokens", 0) for r in recs)
    print(f"entities: {len(surfaces)} surfaces, {len(batches)} Jev requests, {unreached} unreached, "
          f"{sum(r['p'] >= 0.5 for r in rows)} judged entities; {tokens:,} input tokens, "
          f"{time.time() - t:.0f}s")
    return rows


# ── stage 3: counterparts, proposed from names alone ─────────────────────────

PROPOSE = """You help build a German-English glossary for a corpus of German research notes behind a hard-SF novel. The notes mix German and English: German prose that borrows English technical terms, and English research quoted inside German text.

For each term below, give:
- "lang": "de" (German word or compound), "en" (English), "both" (same spelling in both languages, e.g. System, Chaos), "name" (a proper name, acronym or code that is not translated, e.g. Kael, AEGIS, KW1), or "other"
- "counterparts": for "de" up to 3 English forms, for "en" up to 3 German forms, as a writer of such notes would most likely write them, most likely first. Include plural or compound variants only if they differ in meaning. For "both", "name" and "other" give [].

Return JSON only, exactly: {{"terms": [{{"term": "...", "lang": "...", "counterparts": ["..."]}}, ...]}} with one entry per input term, in input order, the term copied exactly.

Terms:
{terms}"""


def stage_propose(lines: Lines) -> list[dict]:
    ents = [r for r in read_jsonl("entities") if r["p"] >= 0.5]
    names = [r["surface"] for r in ents]
    batches = [names[i:i + OR_BATCH] for i in range(0, len(names), OR_BATCH)]
    t = time.time()
    with ThreadPoolExecutor(3) as pool:  # free endpoints share an upstream pool
        # BILINGUAL_REVERSE=1 walks the batches from the other end, so a second process
        # can share a slow free endpoint's work; the cache makes the overlap free.
        order = batches[::-1] if os.environ.get("BILINGUAL_REVERSE") else batches
        done = dict(zip(map(tuple, order),
                        pool.map(lambda b: openrouter(PROPOSE.format(terms="\n".join(b))), order)))
        recs = [done[tuple(b)] for b in batches]
    by_term, unreached, models = {}, 0, Counter()
    for batch, rec in zip(batches, recs):
        if "unreached" in rec:
            unreached += len(batch)
            continue
        models[rec["model"]] += 1
        for item in rec["answer"].get("terms", []):
            if isinstance(item, dict) and item.get("term") in batch:
                by_term[item["term"]] = item
    def forms(c: str) -> list[str]:
        """The proposal as written, and capitalised: a model writes English nouns in
        lower case (`rifts`) and the search is case-sensitive, so `Rifts` would be missed."""
        c = c.strip().rstrip(".")
        return list(dict.fromkeys([c, c[:1].upper() + c[1:]])) if c else []

    wanted = sorted({f for it in by_term.values() for c in it.get("counterparts") or []
                     if isinstance(c, str) for f in forms(c)})
    hits = lines.search(wanted)
    rows = []
    for name in names:
        it = by_term.get(name)
        if not it:
            rows.append({"surface": name, "lang": None, "proposed": [], "present": []})
            continue
        prop = list(dict.fromkeys(f for c in it.get("counterparts") or [] if isinstance(c, str)
                                  for f in forms(c)))
        present = [{"surface": c, "docs": len(hits[c]), "n": sum(h["n"] for h in hits[c])}
                   for c in prop if hits.get(c) and c != name]
        rows.append({"surface": name, "lang": it.get("lang"), "proposed": prop, "present": present})
    write_jsonl("propose", rows)
    print(f"propose: {len(names)} entities, {len(batches)} calls ({dict(models)}), {unreached} unreached; "
          f"{sum(bool(r['proposed']) for r in rows)} got counterparts, "
          f"{sum(bool(r['present']) for r in rows)} with one the corpus contains; {time.time() - t:.0f}s")
    return rows


# ── stage 4: how does each pair relate ────────────────────────────────────────

RELATIONS = {
    "translation": "the same entity or concept, named once in German and once in English",
    "abbreviation": "one is an abbreviation, acronym or short form of the other",
    "variant": "the same entity in the same language: spelling, inflection, plural, hyphenation or compound variant",
    "role_or_part": "different things where one is a role, part, member, instance, level or attribute of the other",
    "distinct": "two different things that are merely listed, paired, contrasted or related",
}
PAIR_Q = ("How do `{a}` and `{b}` relate in this corpus? pairs[\"{k}\"] holds lines where they occur, "
          "together where the texts write both. Choose the narrowest fact the lines support.")


def stage_pairs(lines: Lines) -> list[dict]:
    from typesafe_sdk import Choice
    ents = {r["surface"]: r for r in read_jsonl("entities")}
    langs = {r["surface"]: r for r in read_jsonl("propose")}
    pairs: dict[tuple[str, str], dict] = {}
    for r in read_jsonl("stated"):
        a, b = r["a"], r["b"]
        if max(ents.get(a, {}).get("p", 0), ents.get(b, {}).get("p", 0)) < 0.5:
            continue
        pairs[tuple(sorted((a, b)))] = {"stated": r, "proposed": False}
    for r in langs.values():
        for c in r["present"]:
            key = tuple(sorted((r["surface"], c["surface"])))
            pairs.setdefault(key, {"stated": None, "proposed": False})["proposed"] = True
    keys = sorted(pairs)
    hits = lines.search(sorted({s for k in keys for s in k}))

    def context(a: str, b: str, info: dict) -> list[str]:
        out = []
        if info["stated"]:
            out += [f"{c['slug']}:L{c['line']}| {lines.text(c['slug'], c['line'])}"
                    for c in info["stated"]["cites"][:2]]
        out += lines.examples(hits[a], 1) + lines.examples(hits[b], 1)
        return list(dict.fromkeys(out))

    batches = [keys[i:i + JEV_BATCH // 2] for i in range(0, len(keys), JEV_BATCH // 2)]

    def ask(batch):
        state = {"pairs": {f"p{i}": {"a": a, "b": b, "lines": context(a, b, pairs[(a, b)])}
                           for i, (a, b) in enumerate(batch)}}
        qs = {f"p{i}": Choice(instructions=PAIR_Q.format(a=a, b=b, k=f"p{i}"), criteria=RELATIONS)
              for i, (a, b) in enumerate(batch)}
        return jev(state, qs)

    t = time.time()
    with ThreadPoolExecutor(JEV_WORKERS) as pool:
        recs = list(pool.map(ask, batches))
    rows, unreached = [], 0
    for batch, rec in zip(batches, recs):
        for i, (a, b) in enumerate(batch):
            info = pairs[(a, b)]
            row = {"a": a, "b": b, "lang_a": langs.get(a, {}).get("lang"),
                   "lang_b": langs.get(b, {}).get("lang"),
                   "docs_a": len(hits[a]), "docs_b": len(hits[b]),
                   "docs_both": len({h["slug"] for h in hits[a]} & {h["slug"] for h in hits[b]}),
                   "stated": info["stated"] and {k: info["stated"][k] for k in ("docs", "times", "shape", "cites")},
                   "proposed": info["proposed"]}
            if "unreached" in rec:
                unreached += 1
                row["relation"] = None
            else:
                ans = rec["answers"][f"p{i}"]
                row["relation"] = ans["choice"]
                row["probabilities"] = {k: round(v, 4) for k, v in ans["probabilities"].items()}
            rows.append(row)
    write_jsonl("pairs", rows)
    print(f"pairs: {len(keys)} pairs ({sum(bool(pairs[k]['stated']) for k in keys)} stated, "
          f"{sum(pairs[k]['proposed'] for k in keys)} proposed), {len(batches)} Jev requests, "
          f"{unreached} unreached; {Counter(r['relation'] for r in rows)}; {time.time() - t:.0f}s")
    return rows


# ── stage 5: the list ─────────────────────────────────────────────────────────

def cite(c: dict) -> str:
    return f"^[{c['slug']}.md:L{c['line']}]"


def stage_write() -> Path:
    ents = read_jsonl("entities")
    langs = {r["surface"]: r for r in read_jsonl("propose")}
    pairs = read_jsonl("pairs")
    kept = [r for r in ents if r["p"] >= 0.5]
    links: dict[str, list[dict]] = defaultdict(list)
    for p in pairs:
        if p["relation"] in ("translation", "abbreviation", "variant"):
            conf = p["probabilities"][p["relation"]]
            links[p["a"]].append({"surface": p["b"], "relation": p["relation"], "p": conf,
                                  "stated": bool(p["stated"])})
            links[p["b"]].append({"surface": p["a"], "relation": p["relation"], "p": conf,
                                  "stated": bool(p["stated"])})
    full = []
    for r in sorted(kept, key=lambda r: (-r["docs"], r["surface"])):
        full.append({"surface": r["surface"], "lang": langs.get(r["surface"], {}).get("lang"),
                     "docs": r["docs"], "n": r["n"], "entity_p": r["p"],
                     "first": r["first"], "same_as": sorted(links.get(r["surface"], []),
                                                            key=lambda x: -x["p"])})
    LISTS.mkdir(parents=True, exist_ok=True)
    (LISTS / "bilingual.jsonl").write_text(
        "".join(json.dumps(r, ensure_ascii=False) + "\n" for r in full), encoding="utf-8")

    def de_en(p):
        """Put the German surface left where the languages say which is which."""
        if p["lang_a"] == "en" and p["lang_b"] != "en":
            return p["b"], p["a"], p["docs_b"], p["docs_a"]
        return p["a"], p["b"], p["docs_a"], p["docs_b"]

    def row(p):
        de, en, dd, de_ = de_en(p)
        conf = p["probabilities"][p["relation"]]
        ev = []
        if p["stated"]:
            ev.append(f"stated in {p['stated']['docs']} doc(s) " + " ".join(cite(c) for c in p["stated"]["cites"][:2]))
        if p["proposed"]:
            ev.append("proposed")
        return f"| {de} | {en} | {conf:.2f} | {dd} | {de_} | {p['docs_both']} | {'; '.join(ev)} |"

    trans = sorted((p for p in pairs if p["relation"] == "translation"),
                   key=lambda p: (-p["probabilities"]["translation"], -(p["docs_a"] + p["docs_b"])))
    abbr = sorted((p for p in pairs if p["relation"] == "abbreviation"),
                  key=lambda p: (-(p["stated"] or {}).get("docs", 0), -p["probabilities"]["abbreviation"]))
    var = sorted((p for p in pairs if p["relation"] == "variant"),
                 key=lambda p: -p["probabilities"]["variant"])
    models = sorted({json.loads(f.read_text()).get("model", "?") for f in (CALLS / "openrouter").glob("*.json")}) \
        if (CALLS / "openrouter").exists() else []
    jevm = sorted({json.loads(f.read_text()).get("model", "?") for f in (CALLS / "jev").glob("*.json")}) \
        if (CALLS / "jev").exists() else []
    head = f"""# German and English names — proposals, not merges

Written by `scripts/bilingual.py`. Every row is a pair of surfaces the corpus
contains, and every count below comes from the corpus search (whole-word,
case-sensitive). No count comes from a model.

- **stated**: the corpus writes the pair itself (`A (B)`, `A/B`). The cite is where.
- **proposed**: a free model ({', '.join(models) or '—'}) suggested the
  counterpart from the **name alone**, with no corpus text, and code found it in the corpus.
- **p**: {', '.join(jevm) or 'Jev'}'s probability for the relation, judged over the
  lines where the two occur. A probability directs attention; it decides nothing.

**Whether two surfaces are one term stays a person's call**
(`Plan/runs/judgements.jsonl`). Nothing here creates a page, a link or a merge.
The complete list, every judged entity with its counterparts or none, is
`bilingual.jsonl` beside this file: {len(full)} entities,
{sum(bool(r['same_as']) for r in full)} with a counterpart.

```yaml
Plan/entities/bilingual: provisional
# may not: merge surfaces, create a page or link, supply a count, enter a census
# retire when: a person has reviewed the translation pairs into judgements.jsonl
```
"""
    table = "| German | English | p | docs (de) | docs (en) | docs (both) | evidence |\n|---|---|--:|--:|--:|--:|---|"
    body = [head,
            f"## Translations — {len(trans)}\n\nThe same entity named in two languages.\n\n{table}",
            *map(row, trans),
            f"\n## Abbreviations — {len(abbr)}\n\n{table.replace('German', 'long').replace('English', 'short')}",
            *map(row, abbr),
            f"\n## Variants — {len(var)}\n\nSame entity, same language: spelling, inflection, plural.\n\n{table.replace('German', 'a').replace('English', 'b')}",
            *map(row, var),
            f"\n## Not the same — {sum(p['relation'] in ('role_or_part', 'distinct') for p in pairs)}\n\n"
            "Pairs a gloss or the model suggested and Jev placed as a role, a part, or a "
            "different thing, with the gloss that suggested them. Kept so a reader can overrule.\n\n"
            "| a | b | relation | p | evidence |\n|---|---|---|--:|---|",
            *(f"| {p['a']} | {p['b']} | {p['relation']} | {p['probabilities'][p['relation']]:.2f} | "
              + ("stated " + cite(p['stated']['cites'][0]) if p["stated"] else "proposed") + " |"
              for p in sorted((p for p in pairs if p["relation"] in ("role_or_part", "distinct")),
                              key=lambda p: -((p["stated"] or {}).get("docs", 0)))[:300])]
    out = LISTS / "bilingual.md"
    out.write_text("\n".join(body) + "\n", encoding="utf-8")
    print(f"write: {out.relative_to(ROOT)} — {len(trans)} translations, {len(abbr)} abbreviations, "
          f"{len(var)} variants; {len(full)} entities in bilingual.jsonl")
    return out


def main(argv: list[str]) -> int:
    args = [a for a in argv if not a.startswith("--")]
    stage = args[0] if args else "all"
    if stage in ("stated", "all"):
        stage_stated()
    if stage in ("entities", "propose", "pairs", "all"):
        lines = Lines()
        if stage in ("entities", "all"):
            stage_entities(lines)
        if stage in ("propose", "all"):
            stage_propose(lines)
        if stage in ("pairs", "all"):
            stage_pairs(lines)
    if stage in ("write", "all"):
        stage_write()
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
