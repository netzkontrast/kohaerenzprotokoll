"""Pre-classify a document's candidates against the wiki, without reading it.

The reconciliation grows with the wiki if it is done by reading the wiki. This
does it by lookup instead: the wiki is a variable in a program (Wiki/index.json),
and what reaches a reader is the answer to a query -- a few rows -- rather than
the pages themselves.

Three of the four things a reconciliation produces are decidable this way:

    new term       the candidate matches no known surface
    new reading    it matches a page this document has not contributed to
    already there  it matches a page this document is already recorded on

The fourth is not, and that is the point of the split:

    needs judgement  it *nearly* matches -- a fold away, a substring, a shared
                     stem -- and whether that is one term or two is the thing no
                     lookup settles

Measured on document 3, 19 of 20 reconciliation items were of the first kind and
one needed real thought. Sending only the fourth bucket to a person -- or later to
a model -- is where the effort goes.

What this deliberately does NOT do is decide a conflict. Two readings of one term
can only be compared by reading them, and a program that guessed would produce
exactly the false conflicts a shared-string detector produces.

**And it sweeps the document for what the wiki already knows** (decision 012).
A census is selective, by the rule in the briefing, and a lookup can only match
what the census listed. So every surface of every page is also searched for in
the document itself, standing alone, and each page the text names but no
candidate matches is listed as `in_document_not_in_census`. Whether such an
occurrence is a reading, or a title, a reference or a word in its ordinary sense,
is the reconciler's call. It is recorded in `Plan/runs/sweep.jsonl`, and a
sweep hit with no reading and no row there is `open`.

Usage:
    python3 scripts/reconcile.py <slug>
    python3 scripts/reconcile.py --sweep-open      # every read document's undecided hits
    python3 scripts/reconcile.py --selftest
"""

from __future__ import annotations

import json
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
INDEX = ROOT / "Wiki" / "index.json"
RUNS = ROOT / "Plan" / "runs"
SWEEP_LEDGER = RUNS / "sweep.jsonl"

sys.path.insert(0, str(ROOT / "scripts"))
import subject  # noqa: E402
from wiki_index import fold, mention  # noqa: E402


def candidates_of(slug: str) -> list[str]:
    """The candidate list, read the same way `capture.py` reads it.

    There were two parsers for this file and only one was fixed. A candidates
    file also carries prose, and reading every `- ` line put nine sentences into
    the reconciliation — where they came back as `needs_judgement` pairs like
    „V / **`TSDP`.** L35 …". `capture.py` owns the format; this asks it.
    """
    path = RUNS / slug / "03-candidates.md"
    if not path.exists():
        sys.exit(f"no candidate list at {path.relative_to(ROOT)} -- run scripts/capture.py first")
    from capture import candidate_terms
    return candidate_terms(path.read_text(encoding="utf-8"))


SHORTEST_COMPARABLE = 4


def comparable(key: str) -> bool:
    """Whether a folded key may take part in a containment test.

    Containment on a short key is noise, not a signal: `V` folds to `v`, which is
    inside `kerndirektive` and `realitaetsverformung`, and the reconciliation
    duly reported both as „one term or two?". `near_matches` had this guard and
    `intra_list_pairs` did not — the same substring trap that made `capture.py`
    count `V` 198 times, in a third place.
    """
    return len(key) >= SHORTEST_COMPARABLE


def near_matches(key: str, surfaces: dict[str, str]) -> list[tuple[str, str]]:
    """Folded keys that contain or are contained by this one, with their page.

    Containment is the cheap signal for a surface variant -- singular against
    plural, a compound against its head. It is also how two different terms get
    merged by accident, which is why every hit goes to judgement rather than
    being applied.
    """
    hits = []
    for other, page in surfaces.items():
        if other == key or not comparable(other) or not comparable(key):
            continue
        if other in key or key in other:
            hits.append((other, page))
    return sorted(hits)


def intra_list_pairs(terms: list[str]) -> list[tuple[str, str]]:
    """Candidates that *nearly* fold into each other inside one document's list.

    Checking only against the wiki misses these entirely and creates two pages
    for one term on the spot, which no later reconciliation would ever notice.

    Proper containment only -- `Kern-Welt` inside `Kern-Welten`. An exact fold
    match is not returned here because it is not a judgement: `fold()` has
    already decided it. `same_surface_groups` reports those instead.

    **This function used to carry `Die Konstrukt-Stadt` beside `Konstrukt-Stadt`
    as its example and could not detect that pair.** The guard read `a != b and
    (a in b or b in a)`, so exact fold-equality -- the article rule's whole
    purpose -- fell through both branches and both surfaces were reported as new
    terms. Document 4 would have created six pages for three worlds.
    """
    keys = {term: fold(term) for term in terms}
    pairs = []
    for i, first in enumerate(terms):
        for second in terms[i + 1:]:
            a, b = keys[first], keys[second]
            if not (comparable(a) and comparable(b)):
                continue
            if a and b and a != b and (a in b or b in a):
                pairs.append((first, second))
    return pairs


def same_surface_groups(terms: list[str]) -> dict[str, list[str]]:
    """Surfaces in one candidate list that fold to the same key: one term.

    Decided by `fold()`, not by a person -- the article, case, diacritic and
    punctuation rules are already mechanised. The group is reported so the
    collapse is visible and the page gets its `aliases`, never silent.
    """
    groups: dict[str, list[str]] = {}
    for term in terms:
        key = fold(term)
        if key:
            groups.setdefault(key, []).append(term)
    return {k: v for k, v in groups.items() if len(v) > 1}


SHORTEST_SWEPT = 2


def sweep(slug: str, index: dict, candidates: list[str]) -> list[dict]:
    """Every page the document names by one of its surfaces, standing alone,
    that no candidate matches — with the first line it stands on.

    A page counts as listed when any candidate folds to any of its surfaces, so
    a census that wrote `Guardians` is not asked about `Guardian`'s other forms.
    The text is searched the way `quotes.py` reads a line (escapes and emphasis
    undone), with the pattern every counting script uses, `mention()`: no
    letter, digit or hyphen on either side.

    Measured 2026-09-25 over the fifteen read documents: 24 hits a page held no
    reading for. Read one by one, 10 were readings the lookup had missed —
    `Guardian` listed where the page's surface is `Guardians`, `Emergenz` on a
    world rather than on AEGIS, a second sense of `Kohärenz` — and 14 were not:
    the novel's title, a book title in a reference, a word in another sense, a
    chapter title a page had chosen not to attach, a term the document's own
    rule kept out (`Plan/runs/sweep.jsonl` has each).

    What it does not see: an inflected form the page does not carry as a
    surface, a surface inside a compound (`Guardian-Prinzipien`), and a name
    split across a line. A surface of one letter would stand alone in every
    `[V]` label, so none is swept; none exists today.
    """
    doc = subject.document(slug)
    import quotes
    text = "\n".join(quotes.unmarked(line) for line in doc.lines())
    listed = {fold(c) for c in candidates}
    rows = []
    for page, entry in sorted(index["terms"].items()):
        surfaces = [s for s in entry["surfaces"] if s != page and len(s) >= SHORTEST_SWEPT]
        if any(fold(s) in listed for s in surfaces):
            continue
        first = None
        for surface in surfaces:
            hit = mention(surface).search(text)
            if hit and (first is None or hit.start() < first[1]):
                first = (surface, hit.start())
        if first:
            rows.append({"page": page, "surface": first[0],
                         "line": text.count("\n", 0, first[1]) + doc.offset,
                         "already_read": slug in entry["ingested"]})
    return rows


def sweep_ledger() -> dict[tuple[str, str], dict]:
    """(document, page) → the recorded decision on a sweep hit."""
    if not SWEEP_LEDGER.exists():
        return {}
    rows = [json.loads(line) for line in SWEEP_LEDGER.read_text(encoding="utf-8").splitlines() if line.strip()]
    return {(r["document"], r["page"]): r for r in rows}


def sweep_open(index: dict | None = None) -> list[dict]:
    """Sweep hits in every reconciled document that no reading and no ledger row settles.

    Done is a measurement (P24): a hit is settled when the page carries a
    reading from the document, or `Plan/runs/sweep.jsonl` says why it is not one.
    """
    if index is None:
        index = json.loads(INDEX.read_text(encoding="utf-8"))
    ledger = sweep_ledger()
    open_rows = []
    for run in sorted(RUNS.glob("*/reconcile.json")):
        slug = run.parent.name
        if not (run.parent / "03-candidates.md").exists():
            continue
        for row in sweep(slug, index, candidates_of(slug)):
            if not row["already_read"] and (slug, row["page"]) not in ledger:
                open_rows.append({"document": slug, **row})
    return open_rows


def classify(slug: str, index: dict) -> dict:
    surfaces = index["surface_to_page"]
    buckets: dict[str, list] = {"already_there": [], "new_reading": [], "new_term": [], "needs_judgement": []}
    candidates = candidates_of(slug)
    swept = sweep(slug, index, candidates)

    # Surfaces of one term, settled by fold(): keep the first, carry the rest as
    # aliases. Done before classification so one term cannot become two pages.
    same = same_surface_groups(candidates)
    folded_away = {term for group in same.values() for term in group[1:]}
    candidates = [term for term in candidates if term not in folded_away]

    for first, second in intra_list_pairs(candidates):
        buckets["needs_judgement"].append({
            "candidate": f"{first}  /  {second}",
            "question": "two surfaces of one term inside this document, or two terms?",
            "near": [],
        })

    for term in candidates:
        key = fold(term)
        page = surfaces.get(key)
        if page:
            entry = index["terms"][page]
            bucket = "already_there" if slug in entry["ingested"] else "new_reading"
            buckets[bucket].append({"candidate": term, "page": page, "readings": entry["readings"]})
            continue
        near = near_matches(key, surfaces)
        if near:
            buckets["needs_judgement"].append({
                "candidate": term,
                "question": "same term under another surface, or a different term?",
                "near": [{"surface": s, "page": p} for s, p in near],
            })
            continue
        buckets["new_term"].append({"candidate": term})

    seen_in_judgement = {
        part.strip()
        for row in buckets["needs_judgement"]
        for part in row["candidate"].split("  /  ")
    }
    buckets["new_term"] = [r for r in buckets["new_term"] if r["candidate"] not in seen_in_judgement]

    # Bucket entries, not candidates: one term can raise several judgements, so
    # this counts decisions. Reporting it as „N candidates" said 65 for a list of
    # 51 and made the reconciliation look bigger than the document.
    total = sum(len(v) for v in buckets.values())
    decided = total - len(buckets["needs_judgement"])
    return {
        "document": slug,
        "step": "reconcile-pre",
        "at": date.today().isoformat(),
        "by": "scripts/reconcile.py",
        "index_built": index["built"],
        "state": {"pages": index["pages"], "conflicts": index["conflicts"]},
        "candidates": len(candidates),
        "decisions": total,
        "same_surface": same,
        "decided_mechanically": decided,
        "needs_judgement": len(buckets["needs_judgement"]),
        "buckets": buckets,
        "in_document_not_in_census": swept,
        "index_gaps_may_hide_matches": True,
        "not_decidable_here": [
            "whether a new reading conflicts with one already on the page",
            "whether a near match is one term or two",
            "whether a candidate is a term at all",
        ],
    }


def render(result: dict) -> str:
    out = [
        f"# reconcile-pre — {result['document']}",
        f"  wiki: {result['state']['pages']} pages, {result['state']['conflicts']} conflicts "
        f"(index built {result['index_built']})",
        f"  {len(result.get('same_surface', {}))} surface groups folded to one term first"
        if result.get("same_surface") else "",
        f"  {result['candidates']} candidates, {result['decisions']} decisions — "
        f"**{result['decided_mechanically']} by lookup, "
        f"{result['needs_judgement']} need judgement**",
        "",
        "  a new_term is only new against what the index can see —",
        "  run `python3 scripts/wiki_index.py --check` for what it cannot.",
        "",
    ]
    for name, label in [
        ("already_there", "already recorded from this document — nothing to do"),
        ("new_reading", "page exists, this document is not on it yet — a reading"),
        ("new_term", "no page, no near match — a new page"),
        ("needs_judgement", "NEAR a known surface — one term or two?"),
    ]:
        rows = result["buckets"][name]
        out.append(f"## {name} ({len(rows)}) — {label}")
        for row in rows:
            if name == "needs_judgement":
                near = ", ".join(f"{n['surface']}→{n['page']}" for n in row["near"]) or "each other"
                out.append(f"  {row['candidate']:44} near: {near}")
            else:
                out.append(f"  {row['candidate']:36} {row.get('page', '')}")
        out.append("")
    swept = result.get("in_document_not_in_census", [])
    out.append(f"## in_document_not_in_census ({len(swept)}) — a page's surface stands alone "
               "in the text and no candidate matches it: a reading, or an occurrence? "
               "Record the call in Plan/runs/sweep.jsonl")
    for row in swept:
        mark = "  (page already reads this document)" if row["already_read"] else ""
        out.append(f"  {row['surface']:36} {row['page']:28} L{row['line']}{mark}")
    out.append("")
    return "\n".join(out)


def selftest() -> int:
    """Each case carries the exact outcome the sweep must produce.

    A real document, so the whole path runs — body offset, unmarking, the
    standing-alone pattern — against an index built here, so no page on disk
    can move the needles.
    """
    slug = "aegis-subplots-kapitelweise-system-exploration-docx"
    index = {"terms": {
        "aegis": {"surfaces": ["AEGIS", "aegis"], "ingested": []},
        "kael": {"surfaces": ["Kael"], "ingested": [slug]},
        "guardian-x": {"surfaces": ["Guardian"], "ingested": []},
        "riss-x": {"surfaces": ["Riss"], "ingested": []},
        "absent-x": {"surfaces": ["Quasikristallgitter"], "ingested": []},
        "simulation": {"surfaces": ["simulation"], "ingested": []},
    }}
    rows = {r["page"]: r for r in sweep(slug, index, ["Die Kontrolle", "kael"])}
    cases = [
        ("a surface no candidate lists is found at its first line", rows.get("aegis", {}).get("line"), 11),
        ("a candidate that folds to a surface lists the page", "kael" in rows, False),
        ("the first line standing alone, not the first substring (Guardians at L47)",
         rows.get("guardian-x", {}).get("line"), 48),
        ("a plural is not the word standing alone (Risse at L93)", rows.get("riss-x", {}).get("line"), 94),
        ("a surface the text never writes is not a hit", "absent-x" in rows, False),
        ("a page's own slug is not swept, though it stands alone at L612", "simulation" in rows, False),
    ]
    read = sweep(slug, {"terms": {"aegis": {"surfaces": ["AEGIS"], "ingested": [slug]}}}, [])
    cases.append(("a page that already reads the document says so", read[0]["already_read"] if read else None, True))
    bad = 0
    for name, got, want in cases:
        ok = got == want
        bad += not ok
        print(f"  {'ok ' if ok else 'BAD'} {name}" + ("" if ok else f": got {got!r}, want {want!r}"))
    print(f"reconcile sweep: {len(cases) - bad} of {len(cases)} cases hold")
    return 1 if bad else 0


def main(argv: list[str]) -> int:
    if not argv:
        sys.exit(__doc__)
    if argv[0] == "--selftest":
        return selftest()
    if not INDEX.exists():
        sys.exit("no Wiki/index.json -- run scripts/wiki_index.py first")
    if argv[0] == "--sweep-open":
        rows = sweep_open()
        for row in rows:
            print(f"  {row['document'][:48]:48} {row['page']:28} {row['surface']!r} L{row['line']}")
        print(f"{len(rows)} sweep hits with no reading and no row in Plan/runs/sweep.jsonl")
        return 1 if rows else 0
    slug = argv[0]
    result = classify(slug, json.loads(INDEX.read_text(encoding="utf-8")))
    (RUNS / slug / "reconcile-pre.json").write_text(
        json.dumps(result, indent=2, ensure_ascii=False) + "\n", encoding="utf-8"
    )
    print(render(result))
    return 0


if __name__ == "__main__":
    subject.cli(main)
