"""Gold relations: what one reader, blind to every extractor, says a document relates — in the contracts' vocabulary.

A gold candidate list (`gold.py`) scores *names*. The HyperExtract contracts the backfill runs
(PR #129, #130) do more than name: `TermDefinitions` places where a term is defined,
`TermContrasts` pairs two things the document sets against each other, `CausalLinks` pairs a
cause with its effect. Scoring only their endpoints against a term list (`goldeval.py`) cannot
tell a right pair from two right names wrongly joined. The author, 2026-09-30: „Maybe we need to
extend the Gold List with additional Relation types like the ones defined in the hyperextract
contracts“. This is that extension, for the three contracts the backfill runs.

**The file**, `Plan/runs/<slug>/03-relations.md`, written by a reader of the document who has
not opened `Plan/runs/<slug>/hyperextract/`:

    written_by: <who>, <date>, while reading, blind to every extractor
    ## definitions
    - <term>  ^[Lnn]
    ## contrasts
    - <source> | <type> | <target>  ^[Lnn]
    ## causal
    - <source> | <type> | <target>  ^[Lnn]

The types are the contracts' own (`TYPES`). A row is **of the document** when its cited line
holds each of its surfaces as a whole word (`entities.holds`, the question every placement here
asks). `freeze` records the rows and the file's hash in `relations.json`, after `check` holds;
a file changed after its freeze is not gold, the way a candidate list changed after its count is not.

**Scoring** (`score`). A contract's row matches a gold row when both are in the same section and
each endpoint meets its counterpart by `fold()` or one stands inside the other (a contract writes
`die Dual-Form` where a reader writes `Dual-Form`). Contrasts are unordered, causes ordered.
Reported per contract: gold rows, contract rows, **recall** and **precision** on pairs, `+half`
(precision counting a leftover contract row on a leftover gold row's line that meets one of its
endpoints — the same sentence cut at another length), how many
matched pairs also agree on the **type**, and on the **line** (±1). A gold list of relations is
one reading, as a list of terms is (P27): a contract's pair the reader did not write is a place
to look, not an error — `--unmatched` prints them.

    python3 scripts/goldrel.py check <slug>      # every row parses, has a known type, and its line holds its surfaces
    python3 scripts/goldrel.py freeze <slug>     # after check holds: relations.json
    python3 scripts/goldrel.py status            # which relation lists exist and are gold
    python3 scripts/goldrel.py score [--unmatched] [--record]
    python3 scripts/goldrel.py selftest
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

RUNS = ROOT / "Plan" / "runs"
RECORD = RUNS / "gold-eval" / "relations.jsonl"
FILE = "03-relations.md"
FROZEN = "relations.json"
TYPES = {
    "definitions": set(),
    "contrasts": {"contrasts_with", "in_tension_with", "opposes", "complements", "denies"},
    "causal": {"causes", "enables", "prevents", "triggers", "requires"},
}
CONTRACT = {"definitions": "TermDefinitions", "contrasts": "TermContrasts", "causal": "CausalLinks"}
ORDERED = {"definitions": False, "contrasts": False, "causal": True}
ROW = re.compile(r"^- (?P<body>.+?)\s+\^\[L(?P<line>\d+)\]\s*$")
SHORTEST_INSIDE = 3


def parse(text: str) -> tuple[list[dict], list[str]]:
    """Rows and the problems met parsing them."""
    rows, problems, section = [], [], None
    for n, raw in enumerate(text.splitlines(), 1):
        line = raw.rstrip()
        if line.startswith("## "):
            section = line[3:].strip().lower()
            if section not in TYPES:
                problems.append(f"line {n}: unknown section {section!r}")
                section = None
            continue
        if not line.startswith("- "):
            continue
        if section is None:
            problems.append(f"line {n}: a row outside a known section")
            continue
        m = ROW.match(line)
        if not m:
            problems.append(f"line {n}: no ^[Lnn] at the end: {line}")
            continue
        parts = [p.strip() for p in m["body"].split(" | ")]
        if section == "definitions":
            if len(parts) != 1 or not parts[0]:
                problems.append(f"line {n}: a definition is one term")
                continue
            rows.append({"section": section, "source": parts[0], "type": "defines", "target": "",
                         "line": int(m["line"])})
        else:
            if len(parts) != 3 or not all(parts):
                problems.append(f"line {n}: a relation is `source | type | target`")
                continue
            if parts[1] not in TYPES[section]:
                problems.append(f"line {n}: {parts[1]!r} is no {section} type ({', '.join(sorted(TYPES[section]))})")
                continue
            rows.append({"section": section, "source": parts[0], "type": parts[1], "target": parts[2],
                         "line": int(m["line"])})
    return rows, problems


def off_line(doc, rows: list[dict]) -> list[str]:
    """Rows whose cited line does not hold every surface as a whole word."""
    from entities import holds
    out = []
    for r in rows:
        index = r["line"] - doc.offset
        text = doc.lines()[index] if 0 <= index < len(doc.lines()) else ""
        for surface in (r["source"], r["target"]):
            if surface and not holds(text, surface):
                out.append(f"L{r['line']}: {surface!r} is not on the line")
    return out


def check(slug: str) -> tuple[list[dict], list[str]]:
    import subject
    path = RUNS / slug / FILE
    if not path.exists():
        return [], [f"no {path.relative_to(ROOT)}"]
    text = path.read_text(encoding="utf-8")
    rows, problems = parse(text)
    if not text.startswith("written_by:"):
        problems.insert(0, "the first line is not `written_by:`")
    problems += off_line(subject.document(slug), rows)
    if not rows:
        problems.append("no rows")
    return rows, problems


def digest(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest()


def is_gold(slug: str) -> tuple[bool, str]:
    frozen = RUNS / slug / FROZEN
    path = RUNS / slug / FILE
    if not path.exists():
        return False, "no list"
    if not frozen.exists():
        return False, "not frozen"
    if json.loads(frozen.read_text(encoding="utf-8"))["sha256"] != digest(path):
        return False, "changed since its freeze"
    rows, problems = check(slug)
    return (not problems, "; ".join(problems[:3]) if problems else "")


def freeze(slug: str) -> int:
    rows, problems = check(slug)
    if problems:
        print("\n".join(problems))
        print(f"not frozen: {len(problems)} problems")
        return 1
    path = RUNS / slug / FILE
    (RUNS / slug / FROZEN).write_text(json.dumps(
        {"slug": slug, "frozen": date.today().isoformat(), "sha256": digest(path), "rows": rows},
        ensure_ascii=False, indent=1) + "\n", encoding="utf-8")
    counts = {s: sum(r["section"] == s for r in rows) for s in TYPES}
    print(f"frozen {slug}: {counts}")
    return 0


# ---- scoring ---------------------------------------------------------------

def meets(a: str, b: str) -> bool:
    from wiki_index import fold
    fa, fb = fold(a), fold(b)
    if not fa or not fb:
        return fa == fb
    if fa == fb:
        return True
    short, long_ = sorted((fa, fb), key=len)
    return len(short) >= SHORTEST_INSIDE and short in long_


def pair_meets(g: dict, c: dict, ordered: bool) -> bool:
    if g["section"] == "definitions":
        return meets(g["source"], c["source"])
    straight = meets(g["source"], c["source"]) and meets(g["target"], c["target"])
    if ordered:
        return straight
    return straight or (meets(g["source"], c["target"]) and meets(g["target"], c["source"]))


def contract_rows(slug: str, section: str) -> list[dict]:
    """The admitted rows of the contract that answers `section`, for one document."""
    out = []
    for path in sorted((RUNS / slug / "hyperextract").glob(f"{CONTRACT[section].lower()}-haiku-*/candidates.jsonl")):
        for line in path.read_text(encoding="utf-8").splitlines():
            if not line.strip():
                continue
            row = json.loads(line)
            if row.get("status") != "candidate":
                continue
            raw = row["raw"]
            out.append({"section": section, "source": (raw.get("term") or raw.get("source") or "").strip(),
                        "target": (raw.get("target") or "").strip(), "type": raw.get("type", "defines"),
                        "line": (row.get("lines") or [None])[0]})
    return out


def match(gold_rows: list[dict], named: list[dict], ordered: bool) -> dict:
    """Greedy one-to-one: each gold row takes the first unused contract row that meets it,
    preferring one on the same line. Recall counts gold rows matched, precision contract rows."""
    used: set[int] = set()
    pairs = []
    for g in gold_rows:
        hits = [i for i, c in enumerate(named) if i not in used and pair_meets(g, c, ordered)]
        if not hits:
            continue
        near = [i for i in hits if named[i]["line"] is not None and abs(named[i]["line"] - g["line"]) <= 1]
        i = (near or hits)[0]
        used.add(i)
        pairs.append((g, named[i]))
    left_gold = [g for g in gold_rows if all(g is not p[0] for p in pairs)]
    left_named = [c for i, c in enumerate(named) if i not in used]
    # Half: a contract row left over that stands on a left-over gold row's line and meets one of
    # its endpoints — the same sentence cut at another length, not a missed or invented relation.
    half = sum(any(c["line"] is not None and abs(c["line"] - g["line"]) <= 1
                   and any(meets(x, y) for x in (g["source"], g["target"]) if x
                           for y in (c["source"], c["target"]) if y)
                   for g in left_gold) for c in left_named)
    return {
        "gold": len(gold_rows), "named": len(named), "matched": len(pairs), "half": half,
        "type_agrees": sum(g["type"] == c["type"] for g, c in pairs),
        "line_agrees": sum(c["line"] is not None and abs(c["line"] - g["line"]) <= 1 for g, c in pairs),
        "unmatched_gold": left_gold,
        "unmatched_named": left_named,
    }


def score(unmatched: bool, record: bool) -> int:
    slugs = sorted(p.parent.name for p in RUNS.glob(f"*/{FILE}"))
    total = {s: {"docs": 0, "gold": 0, "named": 0, "matched": 0, "half": 0, "type_agrees": 0, "line_agrees": 0} for s in TYPES}
    for slug in slugs:
        ok, why = is_gold(slug)
        if not ok:
            print(f"  skipped {slug}: {why}")
            continue
        rows = json.loads((RUNS / slug / FROZEN).read_text(encoding="utf-8"))["rows"]
        for section in TYPES:
            named = contract_rows(slug, section)
            if not named:
                continue
            m = match([r for r in rows if r["section"] == section], named, ORDERED[section])
            t = total[section]
            t["docs"] += 1
            for k in ("gold", "named", "matched", "half", "type_agrees", "line_agrees"):
                t[k] += m[k]
            if unmatched:
                print(f"\n{slug} · {CONTRACT[section]}")
                for g in m["unmatched_gold"]:
                    print(f"  gold only      L{g['line']:<4} {g['source']} | {g['type']} | {g['target']}")
                for c in m["unmatched_named"]:
                    print(f"  contract only  L{c['line']!s:<4} {c['source']} | {c['type']} | {c['target']}")
    print(f"\n{'contract':<16}{'docs':>5}{'gold':>6}{'rows':>6}{'recall':>8}{'precision':>11}{'+half':>7}{'type agrees':>13}{'line agrees':>13}")
    lines = []
    for section, t in total.items():
        if not t["docs"]:
            continue
        rec = t["matched"] / t["gold"] if t["gold"] else 0.0
        prec = t["matched"] / t["named"] if t["named"] else 0.0
        ph = (t["matched"] + t["half"]) / t["named"] if t["named"] else 0.0
        ty = t["type_agrees"] / t["matched"] if t["matched"] else 0.0
        li = t["line_agrees"] / t["matched"] if t["matched"] else 0.0
        print(f"{CONTRACT[section]:<16}{t['docs']:>5}{t['gold']:>6}{t['named']:>6}{rec:>8.1%}{prec:>11.1%}{ph:>7.1%}{ty:>13.1%}{li:>13.1%}")
        lines.append(dict(t, contract=CONTRACT[section], recall=round(rec, 3), precision=round(prec, 3), precision_half=round(ph, 3),
                          type_agrees_share=round(ty, 3), line_agrees_share=round(li, 3)))
    print("\nOne reader's relations are one reading; a contract's pair the reader did not write is a place to look.")
    if record and lines:
        import subprocess
        head = subprocess.run(["git", "rev-parse", "--short", "HEAD"], cwd=ROOT, capture_output=True, text=True).stdout.strip()
        RECORD.parent.mkdir(parents=True, exist_ok=True)
        with RECORD.open("a", encoding="utf-8") as fh:
            for row in lines:
                fh.write(json.dumps({"date": date.today().isoformat(), "commit": head, **row}, ensure_ascii=False) + "\n")
        print(f"appended {len(lines)} rows to {RECORD.relative_to(ROOT)}")
    return 0


def status() -> int:
    for path in sorted(RUNS.glob(f"*/{FILE}")):
        ok, why = is_gold(path.parent.name)
        rows = parse(path.read_text(encoding="utf-8"))[0]
        counts = " ".join(f"{s} {sum(r['section'] == s for r in rows)}" for s in TYPES)
        print(f"  {'GOLD' if ok else 'no  '}  {path.parent.name:<62} {counts}  {why}")
    return 0


def selftest() -> int:
    cases = []

    def case(name, got, want):
        cases.append((name, got == want, got, want))

    text = ("written_by: x\n## definitions\n- Nexus  ^[L3]\n## contrasts\n- Liebe | in_tension_with | Information  ^[L4]\n"
            "## causal\n- Hitze | causes | Riss  ^[L5]\n- Hitze | leads_to | Riss  ^[L5]\n- Hitze | causes  ^[L5]\n"
            "- Kael | causes | Juna\n## lore\n- X  ^[L1]\n")
    rows, problems = parse(text)
    case("three good rows parse", [(r["section"], r["type"]) for r in rows],
         [("definitions", "defines"), ("contrasts", "in_tension_with"), ("causal", "causes")])
    case("an unknown type, a two-part row, a missing citation, an unknown section and a row under it are each named",
         [p.split(":")[1].strip()[:9] for p in problems],
         ["'leads_to", "a relatio", "no ^[Lnn]", "unknown s", "a row out"])
    case("an article meets", meets("die Dual-Form", "Dual-Form"), True)
    case("a shorter cut meets inside a longer", meets("Hitze", "extreme Hitze"), True)
    case("a two-letter cut never meets inside", meets("KI", "KIRA"), False)
    g = {"section": "contrasts", "source": "Liebe", "target": "Information", "type": "in_tension_with", "line": 4}
    rev = {"section": "contrasts", "source": "Information", "target": "Liebe", "type": "opposes", "line": 4}
    case("a contrast is unordered", pair_meets(g, rev, ORDERED["contrasts"]), True)
    gc = dict(g, section="causal", source="Hitze", target="Riss", type="causes")
    case("a cause is ordered", pair_meets(gc, dict(gc, source="Riss", target="Hitze"), ORDERED["causal"]), False)
    m = match([g], [rev, dict(rev)], False)
    case("matching is one to one; the type is counted apart", (m["matched"], m["type_agrees"], len(m["unmatched_named"])), (1, 0, 1))
    cut = match([gc], [dict(gc, source="Die Durchsetzung der Konsistenz")], True)
    case("the same line, one endpoint met, is half — not matched", (cut["matched"], cut["half"]), (0, 1))
    far = dict(rev, line=40)
    m2 = match([g], [far, rev], False)
    case("a row on the cited line is preferred", m2["line_agrees"], 1)
    import subject
    doc = subject.document("aegis-subplots-kapitelweise-system-exploration-docx")
    line = doc.offset + next(i for i, l in enumerate(doc.lines()) if "AEGIS" in l)
    case("a surface not on its cited line is named",
         len(off_line(doc, [{"source": "AEGIS", "target": "Kern-Welt", "line": line}])), 1)
    bad = 0
    for name, ok, got, want in cases:
        bad += not ok
        print(f"  {'ok ' if ok else 'BAD'} {name}" + ("" if ok else f": got {got!r}, want {want!r}"))
    print(f"goldrel: {len(cases) - bad} of {len(cases)} cases hold")
    return 1 if bad else 0


def main(argv: list[str]) -> int:
    if not argv or argv[0] in ("-h", "--help"):
        print(__doc__)
        return 0
    cmd, rest = argv[0], argv[1:]
    if cmd == "selftest":
        return selftest()
    if cmd == "status":
        return status()
    if cmd == "score":
        return score("--unmatched" in rest, "--record" in rest)
    if cmd in ("check", "freeze") and rest:
        if cmd == "freeze":
            return freeze(rest[0])
        rows, problems = check(rest[0])
        print("\n".join(problems) if problems else f"holds: {len(rows)} rows")
        return 1 if problems else 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
