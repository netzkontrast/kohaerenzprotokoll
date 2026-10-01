"""Every automated reading of a document, scored against its gold candidate list — one table.

Gold lists exist to be scored against (decision 009), and until 2026-09-30 only two
things ever were: the blind re-readings (`agree.py`) and one entity list at a time
(`entities.py score`). The HyperExtract contracts have run on most gold documents
since (PR #126, #129, #130), and nothing asked how the terms they name compare with
what a careful reader listed. This asks it, for every extractor at once, by the one
comparison `agree.compare` makes: surfaces meet by `fold()`, and a shorter cut of a
longer surface is counted `inside`, never shared.

For each extractor, over every gold document it has read:

| column | the question |
|---|---|
| `docs` | on how many gold documents it ran |
| `names` | distinct surfaces it named, summed over those documents |
| `recall` | how much of the gold list it holds (`agree`'s `a_in_b`), micro over documents |
| `+inside` | the same, counting a gold term that stands inside one of its longer surfaces |
| `precision` | how much of what it named the gold list holds |
| `+part` | the same, counting an extra one of whose parts the gold list holds: `Kernwelt (KW)`, `KW1: Logos-Prime` |
| `extra, verbatim` | named, not on the gold list, and on one line of the document word for word — **a place to look for what the gold list missed**, never a count of its misses |
| `extra, not in text` | named, not on the gold list, and nowhere in the document word for word: a paraphrase, a normalised form, or a phrase with its article |

What it is not. A gold list is one reading, not the truth (P27): two blind readers held
82–95 % of a committed list. A HyperExtract contract is not an enumerator: `TermContrasts`
names the two ends of a tension, not every term, so its recall is low by design and its
precision is the question. Which extra is a real term is a reader's call. Prints only;
`--record` appends the rows to `Plan/runs/gold-eval/runs.jsonl`.

    python3 scripts/goldeval.py                  # every extractor, aggregated
    python3 scripts/goldeval.py --by-doc         # and one row per document
    python3 scripts/goldeval.py --extras <extractor> [--limit N]   # the verbatim extras, by document
    python3 scripts/goldeval.py --json | --record
    python3 scripts/goldeval.py selftest
"""

from __future__ import annotations

import json
import re
import sys
from collections import defaultdict
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from agree import compare, terms_of  # noqa: E402

RUNS = ROOT / "Plan" / "runs"
NAMES = ROOT / "Plan" / "entities" / "names"
RECORD = RUNS / "gold-eval" / "runs.jsonl"
# Where a named surface is a label joining names — `Kernwelt (KW)`, `KW1: Logos-Prime`,
# `KW1 — Konstrukt-Stadt`, `Kael/Juna` — it is cut here, and an extra one of whose parts the
# gold list holds is a difference of cut, not a term the reader missed (the gold rule lists
# `A (B)` whole and then by name, so the reader saw it).
PARTS = re.compile(r"\s*(?:\(|\)|:|\s[—–-]\s|/|\s\+\s|↔|→|=)\s*")
# The raw fields of a HyperExtract row that hold a surface. `type`, `quote` and
# `stance` never do.
SURFACE_FIELDS = ("term", "source", "target")


def he_extractor(run_dir: Path) -> str:
    """`termcontrasts-haiku-2026-09-30` -> `he:termcontrasts`; the date and model are the run's, not the contract's."""
    name = run_dir.name
    base = name.split("-haiku")[0]
    return f"he:{base}"


def he_surfaces(path: Path) -> list[str]:
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        if not line.strip():
            continue
        row = json.loads(line)
        if row.get("status") != "candidate":
            continue
        out += [row["raw"][f].strip() for f in SURFACE_FIELDS
                if isinstance(row.get("raw", {}).get(f), str) and row["raw"][f].strip()]
    return out


def readings(slug: str) -> dict[str, list[str]]:
    """Every automated or second reading of one document: extractor -> surfaces."""
    out: dict[str, list[str]] = {}
    for path in sorted((RUNS / slug / "hyperextract").glob("*/candidates.jsonl")):
        out.setdefault(he_extractor(path.parent), []).extend(he_surfaces(path))
    names = NAMES / f"{slug}.json"
    if names.exists():
        data = json.loads(names.read_text(encoding="utf-8"))
        out["entity-list"] = [e["term"] for e in data.get("entities", []) if e.get("term")]
    for path in sorted((RUNS / slug).glob("03-candidates-blind-*.md")):
        out.setdefault("blind-rereading", []).extend(terms_of(path.read_text(encoding="utf-8")))
    return out


def gold_slugs() -> list[str]:
    import gold
    return [v["slug"] for v in gold.verdicts() if v["gold"]]


def score(gold_terms: list[str], named: list[str], doc=None) -> dict:
    """One extractor on one document. `doc` (a subject.Document) decides the extras' split;
    without it they are left unsplit."""
    c = compare(gold_terms, named)
    inside = {x for x, _ in c["only_a_inside_b"]}
    row = {"gold": c["a"], "named": c["b"], "shared": c["shared"], "inside": len(inside),
           "extra": c["only_b"]}
    from wiki_index import fold
    have = {fold(t) for t in gold_terms}
    row["extra_part"] = [t for t in c["only_b"]
                         if any(fold(p) in have for p in PARTS.split(t) if p.strip() and p.strip() != t)]
    if doc is not None:
        from agree import absent
        gone = set(absent(doc, c["only_b"]))
        row["extra_verbatim"] = [t for t in c["only_b"] if t not in gone]
        row["extra_absent"] = [t for t in c["only_b"] if t in gone]
    return row


def evaluate(slugs: list[str] | None = None) -> dict:
    import subject
    per_doc: list[dict] = []
    for slug in slugs if slugs is not None else gold_slugs():
        gold_list = RUNS / slug / "03-candidates.md"
        found = readings(slug)
        if not found:
            continue
        gold_terms = terms_of(gold_list.read_text(encoding="utf-8"))
        doc = subject.document(slug)
        for extractor, named in found.items():
            row = score(gold_terms, named, doc)
            row.update(slug=slug, extractor=extractor)
            per_doc.append(row)
    agg: dict[str, dict] = defaultdict(lambda: defaultdict(int))
    for r in per_doc:
        a = agg[r["extractor"]]
        a["docs"] += 1
        for k in ("gold", "named", "shared", "inside"):
            a[k] += r[k]
        a["extra_part"] += len(r["extra_part"])
        a["extra_verbatim"] += len(r["extra_verbatim"])
        a["extra_absent"] += len(r["extra_absent"])
    table = {}
    for ex, a in sorted(agg.items()):
        table[ex] = dict(a, recall=round(a["shared"] / a["gold"], 3) if a["gold"] else 0.0,
                         recall_inside=round((a["shared"] + a["inside"]) / a["gold"], 3) if a["gold"] else 0.0,
                         precision=round(a["shared"] / a["named"], 3) if a["named"] else 0.0,
                         precision_part=round((a["shared"] + a["extra_part"]) / a["named"], 3) if a["named"] else 0.0)
    return {"table": table, "per_doc": per_doc}


def print_table(result: dict, by_doc: bool) -> None:
    print(f"{'extractor':<24}{'docs':>5}{'names':>7}{'recall':>8}{'+inside':>9}{'precision':>11}"
          f"{'+part':>7}{'extra, verbatim':>17}{'extra, not in text':>20}")
    for ex, a in result["table"].items():
        print(f"{ex:<24}{a['docs']:>5}{a['named']:>7}{a['recall']:>8.1%}{a['recall_inside']:>9.1%}"
              f"{a['precision']:>11.1%}{a['precision_part']:>7.1%}{a['extra_verbatim']:>17}{a['extra_absent']:>20}")
    if by_doc:
        print()
        for r in sorted(result["per_doc"], key=lambda r: (r["extractor"], r["slug"])):
            rec = r["shared"] / r["gold"] if r["gold"] else 0
            prec = r["shared"] / r["named"] if r["named"] else 0
            print(f"  {r['extractor']:<22} {r['slug'][:52]:<52} gold {r['gold']:4} named {r['named']:4}"
                  f"  recall {rec:5.1%}  precision {prec:5.1%}")
    print("\nA gold list is one reading; an extra that stands verbatim is a place to look, not a miss.")


def print_extras(result: dict, extractor: str, limit: int) -> None:
    rows = [r for r in result["per_doc"] if r["extractor"] == extractor]
    if not rows:
        print(f"no extractor {extractor!r}; known: {', '.join(result['table'])}")
        return
    for r in sorted(rows, key=lambda r: -len(r["extra_verbatim"])):
        if r["extra_verbatim"]:
            shown = r["extra_verbatim"][:limit]
            more = len(r["extra_verbatim"]) - len(shown)
            print(f"{r['slug']} — {len(r['extra_verbatim'])} verbatim, not on the gold list")
            print("  " + " · ".join(shown) + (f" · … {more} more" if more else ""))


def record(result: dict) -> None:
    import subprocess
    head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT,
                          capture_output=True, text=True).stdout.strip()
    RECORD.parent.mkdir(parents=True, exist_ok=True)
    with RECORD.open("a", encoding="utf-8") as fh:
        for ex, a in result["table"].items():
            fh.write(json.dumps({"date": date.today().isoformat(), "commit": head, "extractor": ex,
                                 **{k: a[k] for k in ("docs", "gold", "named", "shared", "inside",
                                                      "recall", "recall_inside", "precision", "precision_part", "extra_part",
                                                      "extra_verbatim", "extra_absent")}},
                                ensure_ascii=False) + "\n")
    print(f"appended {len(result['table'])} rows to {RECORD.relative_to(ROOT)}")


def selftest() -> int:
    cases = []

    def case(name, got, want):
        cases.append((name, got == want, got, want))

    gold_terms = ["AEGIS", "Kael", "Juna", "Kern-Welten"]
    r = score(gold_terms, ["AEGIS", "Kael", "Juna/V", "Nexus"])
    case("shared by fold", r["shared"], 2)
    case("a gold term inside a longer named surface counts as inside, not shared", r["inside"], 1)
    case("extras are what the gold list lacks", sorted(r["extra"]), ["Juna/V", "Nexus"])
    case("an article is no boundary", score(["Kohärenzprotokoll"], ["das Kohärenzprotokoll"])["shared"], 1)
    case("a label joining gold names is a difference of cut",
         score(["Kernwelt", "KW1"], ["Kernwelt (KW)", "KW1: Logos-Prime", "Die Form"])["extra_part"],
         ["Kernwelt (KW)", "KW1: Logos-Prime"])
    case("a hyphen inside a compound is no cut", score(["Kern"], ["Kern-Welten"])["extra_part"], [])
    case("an inflection is not shared", score(["Guardian"], ["Guardians"])["shared"], 0)
    case("the extractor name drops model and date",
         he_extractor(Path("x/termcontrasts-haiku-2026-09-30")), "he:termcontrasts")
    case("a variant run keeps its variant",
         he_extractor(Path("x/termreadings-r1a-haiku-2026-09-30")), "he:termreadings-r1a")
    import tempfile
    with tempfile.TemporaryDirectory() as tmp:
        p = Path(tmp) / "candidates.jsonl"
        p.write_text("\n".join(json.dumps(x) for x in [
            {"status": "candidate", "raw": {"source": "Liebe", "target": "Information", "type": "in_tension_with",
                                            "quote": "Ist Liebe Information", "stance": "asks"}},
            {"status": "refused", "raw": {"term": "Nie"}},
            {"status": "candidate", "raw": {"term": " Nexus ", "quote": "q", "stance": "asserts"}},
        ]) + "\n", encoding="utf-8")
        case("surfaces: term, source and target of admitted rows; never type, quote or stance",
             he_surfaces(p), ["Liebe", "Information", "Nexus"])
    import subject
    doc = subject.document("aegis-subplots-kapitelweise-system-exploration-docx")
    split = score(["Kael"], ["AEGIS", "Kern-Welt"], doc)
    case("an extra the document writes verbatim is split from one it never writes",
         (split["extra_verbatim"], split["extra_absent"]), (["AEGIS"], ["Kern-Welt"]))
    bad = 0
    for name, ok, got, want in cases:
        bad += not ok
        print(f"  {'ok ' if ok else 'BAD'} {name}" + ("" if ok else f": got {got!r}, want {want!r}"))
    print(f"goldeval: {len(cases) - bad} of {len(cases)} cases hold")
    return 1 if bad else 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        return selftest()
    if argv[:1] in (["-h"], ["--help"]):
        print(__doc__)
        return 0
    result = evaluate()
    if "--json" in argv:
        print(json.dumps(result, ensure_ascii=False, indent=1))
    elif "--extras" in argv:
        i = argv.index("--extras")
        limit = int(argv[argv.index("--limit") + 1]) if "--limit" in argv else 40
        print_extras(result, argv[i + 1], limit)
    else:
        print_table(result, "--by-doc" in argv)
    if "--record" in argv:
        record(result)
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
