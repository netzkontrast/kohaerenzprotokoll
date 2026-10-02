"""The retrieval cases, frozen: one versioned, hashed file every bench can be read against.

`ask.bench_cases()` derives its 24 cases live from the conflict and question records, so the gold moves every
time a record is edited, and a score from last week and a score from today are scored against different
answers (evaluation audit §3, item 1; `SPEC.md`, migration step 1). This freezes them:

- **freeze** writes `Plan/eval/retrieval-cases-v<N>.json`: the cases (id, key, question, gold lines), the commit
  they were taken at, and a sha256 over the canonical case list. A frozen file is never edited; a new set is v<N+1>.
- **check** proves the file is what it says (its hash, every gold line inside its landed document and below
  the frontmatter) — exit 1 on any failure — and reports, without failing, how the live records have drifted
  from it: cases added or gone, gold lines added or removed per case.
- **cases** is what every bench reads (`ask.py bench`, `novelgraph bench`, `novelgraph rlm`, the evaluation audit):
  the frozen cases in `ask.bench_cases()`'s shape, refused if the file fails its hash. `live=True` reads the records
  instead, for drift studies and for freezing the next version; a score from it is not comparable across commits.
- **clusters** answers whether a held-out split exists: cases sharing a gold document are linked, and the
  connected groups are the units a split may not cut. It reports them at increasing sharing thresholds, and
  how many cases each gold document is gold for. It decides nothing; it measures the dependence.

Standard library.

    python3 scripts/benchset.py freeze [--version 1]
    python3 scripts/benchset.py check [Plan/eval/retrieval-cases-v1.json]
    python3 scripts/benchset.py clusters [Plan/eval/retrieval-cases-v1.json]
    python3 scripts/benchset.py selftest
"""

from __future__ import annotations

import hashlib
import json
import subprocess
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import subject  # noqa: E402

EVAL = ROOT / "Plan" / "eval"


def live() -> list[dict]:
    import ask
    return [{"id": c["id"], "key": c["key"], "question": c["question"],
             "gold": sorted([d, n] for d, n in c["gold"])} for c in ask.bench_cases()]


def digest(cases: list[dict]) -> str:
    return hashlib.sha256(json.dumps(cases, ensure_ascii=False, sort_keys=True,
                                     separators=(",", ":")).encode("utf-8")).hexdigest()


def path_for(version: int) -> Path:
    return EVAL / f"retrieval-cases-v{version}.json"


def freeze(version: int, cases: list[dict] | None = None, target: Path | None = None) -> Path:
    cases = live() if cases is None else cases
    target = target or path_for(version)
    if target.exists():
        raise SystemExit(f"{target} exists: a frozen set is never rewritten; freeze v{version + 1} instead")
    commit = subprocess.run(["git", "-C", str(ROOT), "rev-parse", "HEAD"], capture_output=True, text=True).stdout.strip()
    target.parent.mkdir(parents=True, exist_ok=True)
    target.write_text(json.dumps({"version": version, "from_commit": commit, "source": "ask.bench_cases()",
                                  "sha256": digest(cases), "cases": cases}, ensure_ascii=False, indent=1) + "\n",
                      encoding="utf-8")
    return target


def load(path: Path) -> dict:
    return json.loads(path.read_text(encoding="utf-8"))


def cases(version: int = 1, live: bool = False, path: Path | None = None) -> list[dict]:
    """The bench cases: frozen (default) or live. Frozen is checked against its hash before any score is computed."""
    if live:
        import ask
        return ask.bench_cases()
    frozen = load(path or path_for(version))
    if digest(frozen["cases"]) != frozen["sha256"]:
        raise SystemExit(f"{(path or path_for(version)).name}: the cases do not hash to the recorded sha256 — "
                         "a frozen set is never edited; freeze a new version")
    return [{"id": c["id"], "key": c["key"], "question": c["question"], "gold": {(d, n) for d, n in c["gold"]},
             "frozen": frozen["version"]} for c in frozen["cases"]]


def identity(live: bool = False) -> dict:
    """What a bench result records about the cases it was scored on: the set's name and the sha256 of the cases."""
    got = cases(live=live)
    canon = [{"id": c["id"], "key": c["key"], "question": c["question"], "gold": sorted([d, n] for d, n in c["gold"])}
             for c in got]
    return {"case_set": "live" if live else f"retrieval-cases-v{got[0]['frozen']}", "cases_sha256": digest(canon)}


def consumer_selftest() -> list[str]:
    """The consumers, not the loader: `ask.bench()` and novelgraph's `repo.bench_cases()` read the frozen file by
    default, follow edited records only with `live=True`, and refuse a tampered file before anything is scored.
    Retrieval is stubbed, so this needs no store, no index and no venv."""
    import io
    import tempfile
    import types
    import ask
    import benchset as bs   # the module the consumers import — not `__main__` when this file is run as a script
    fails = []
    frozen_cases = [{"id": "C1", "key": "conflict:C1", "question": "q1", "gold": [["d", 4]]},
                    {"id": "Q1", "key": "question:Q1", "question": "q2", "gold": [["e", 7]]}]
    edited = lambda: [{"id": "C1", "key": "conflict:C1", "question": "q1 edited", "gold": {("d", 5)}}]  # noqa: E731
    stubs = {"askdb": types.SimpleNamespace(Store=lambda: None),
             "graph": types.SimpleNamespace(build=lambda: {}),
             "graphrag": types.SimpleNamespace(without=lambda g, key: g)}
    scored = []

    def pack(question, kind, budget, s, g, **kw):
        scored.append(question)
        return "", {"shown": {"d": [4, 5]}, "chars": 1}
    import sys
    saved = ({k: sys.modules.get(k) for k in stubs}, ask.build_pack, ask.bench_cases, bs.path_for)
    with tempfile.TemporaryDirectory() as tmp:
        f = Path(tmp) / "v1.json"
        f.write_text(json.dumps({"version": 1, "sha256": digest(frozen_cases), "cases": frozen_cases}), encoding="utf-8")
        try:
            sys.modules.update(stubs)
            ask.build_pack, ask.bench_cases = pack, edited
            bs.path_for = lambda version: f
            sys.stdout, quiet = io.StringIO(), sys.stdout   # the bench prints a line per case
            sys.path.insert(0, str(ROOT / "novelgraph" / "src"))
            from novelgraph import repo
            res = ask.bench()
            if [r["id"] for r in res["rows"]] != ["C1", "Q1"] or res["rows"][0]["line_recall"] != 1.0:
                fails.append(f"ask.bench did not score the frozen cases: {res['rows']}")
            if res.get("case_set") != "retrieval-cases-v1" or res.get("cases_sha256") != bs.digest(frozen_cases):
                fails.append(f"ask.bench recorded no case identity: {res.get('case_set')}, {res.get('cases_sha256')}")
            live = ask.bench(live=True)
            if [r["id"] for r in live["rows"]] != ["C1"] or live["rows"][0]["line_recall"] != 1.0 \
                    or live.get("case_set") != "live":
                fails.append(f"ask.bench --live did not follow the records: {live['rows']}")
            if {c["id"]: c["gold"] for c in repo.bench_cases()} != {"C1": {("d", 4)}, "Q1": {("e", 7)}} \
                    or [c["question"] for c in repo.bench_cases(live=True)] != ["q1 edited"]:
                fails.append("novelgraph's repo.bench_cases did not read the frozen file (or live on request)")
            f.write_text(json.dumps({"version": 1, "sha256": digest(frozen_cases),
                                     "cases": [dict(frozen_cases[0], gold=[["d", 9]])]}), encoding="utf-8")
            scored.clear()
            try:
                ask.bench()
                fails.append("ask.bench scored a tampered frozen file")
            except SystemExit:
                if scored:
                    fails.append("ask.bench packed a question before refusing a tampered file")
        finally:
            for k, v in saved[0].items():
                if v is None:
                    sys.modules.pop(k, None)
                else:
                    sys.modules[k] = v
            ask.build_pack, ask.bench_cases, bs.path_for = saved[1], saved[2], saved[3]
            if isinstance(sys.stdout, io.StringIO):
                sys.stdout = quiet
    return fails


def integrity(frozen: dict, document=subject.document) -> list[str]:
    """What must hold of a frozen file for any score against it to mean anything."""
    fails = []
    if digest(frozen["cases"]) != frozen["sha256"]:
        fails.append("the cases no longer hash to the recorded sha256 — the file was edited")
    for c in frozen["cases"]:
        for slug, n in c["gold"]:
            try:
                doc = document(slug)
            except KeyError:
                fails.append(f"{c['id']}: gold names {slug}, which is not landed")
                continue
            last = doc.offset + len(doc.lines()) - 1
            if not doc.offset <= n <= last:
                fails.append(f"{c['id']}: {slug}:L{n} lies outside the body (L{doc.offset}–L{last})")
    return fails


def drift(frozen: dict, current: list[dict]) -> dict:
    old, new = {c["id"]: c for c in frozen["cases"]}, {c["id"]: c for c in current}
    changed = {}
    for cid in sorted(set(old) & set(new)):
        a, b = {tuple(x) for x in old[cid]["gold"]}, {tuple(x) for x in new[cid]["gold"]}
        if a != b or old[cid]["question"] != new[cid]["question"]:
            changed[cid] = {"added": len(b - a), "removed": len(a - b),
                            "question_changed": old[cid]["question"] != new[cid]["question"]}
    return {"gone": sorted(set(old) - set(new)), "new": sorted(set(new) - set(old)), "changed": changed}


def clusters(cases: list[dict], shared: int = 1) -> list[list[str]]:
    """Connected groups of cases, two cases linked when they share at least `shared` gold documents."""
    docs = {c["id"]: {d for d, _ in c["gold"]} for c in cases}
    parent = {cid: cid for cid in docs}

    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    ids = sorted(docs)
    for i, a in enumerate(ids):
        for b in ids[i + 1:]:
            if len(docs[a] & docs[b]) >= shared:
                parent[root(a)] = root(b)
    groups: dict[str, list[str]] = {}
    for cid in ids:
        groups.setdefault(root(cid), []).append(cid)
    return sorted(groups.values(), key=lambda g: (-len(g), g))


def selftest() -> list[str]:
    """Each defect handed to the check that must name it, on a fixture; no corpus file is touched."""
    import tempfile
    from types import SimpleNamespace
    fails = []
    doc = SimpleNamespace(offset=4, lines=lambda: ("a", "b", "c"))       # body L4–L6
    lookup = lambda slug: doc if slug == "d" else (_ for _ in ()).throw(KeyError(slug))  # noqa: E731
    cases = [{"id": "C1", "key": "conflict:C1", "question": "q1", "gold": [["d", 4], ["d", 5]]},
             {"id": "C2", "key": "conflict:C2", "question": "q2", "gold": [["d", 6]]},
             {"id": "Q1", "key": "question:Q1", "question": "q3", "gold": [["e", 9]]}]
    with tempfile.TemporaryDirectory() as tmp:
        f = freeze(1, [dict(c, gold=[g for g in c["gold"] if g[0] == "d"]) for c in cases[:2]], Path(tmp) / "v1.json")
        frozen = load(f)
        if integrity(frozen, lookup):
            fails.append(f"a sound frozen set failed integrity: {integrity(frozen, lookup)}")
        try:
            freeze(1, cases, f)
            fails.append("a frozen file was overwritten")
        except SystemExit:
            pass
        edited = dict(frozen, cases=[dict(frozen["cases"][0], gold=[["d", 4]]), frozen["cases"][1]])
        if not any("hash" in x for x in integrity(edited, lookup)):
            fails.append("an edited case list passed the hash check")
        bad = {"sha256": digest([cases[2], dict(cases[0], gold=[["d", 2]])]),
               "cases": [cases[2], dict(cases[0], gold=[["d", 2]])]}
        problems = integrity(bad, lookup)
        if not any("not landed" in x for x in problems) or not any("outside the body" in x for x in problems):
            fails.append(f"an unlanded document or a frontmatter line passed: {problems}")
        moved = drift(frozen, [dict(cases[0], gold=[["d", 4], ["d", 6]]), cases[2]])
        if moved != {"gone": ["C2"], "new": ["Q1"], "changed": {"C1": {"added": 1, "removed": 1, "question_changed": False}}}:
            fails.append(f"drift misreported: {moved}")
        # the loader reads the frozen file, never the records (consumer_selftest checks the benches that call it)
        import ask
        saved = ask.bench_cases
        ask.bench_cases = lambda: [dict(c, gold={("d", 99)}) for c in cases]   # every record "edited"
        try:
            got = {c["id"]: c["gold"] for c in globals()["cases"](path=f)}
        finally:
            ask.bench_cases = saved
        if got != {"C1": {("d", 4), ("d", 5)}, "C2": {("d", 6)}}:
            fails.append(f"frozen cases followed an edited record: {got}")
        tampered = Path(tmp) / "tampered.json"
        tampered.write_text(json.dumps(edited), encoding="utf-8")
        try:
            globals()["cases"](path=tampered)
            fails.append("a bench read a frozen file that fails its hash")
        except SystemExit:
            pass
    if clusters(cases) != [["C1", "C2"], ["Q1"]] or clusters(cases, shared=2) != [["C1"], ["C2"], ["Q1"]]:
        fails.append(f"clusters wrong: {clusters(cases)} / {clusters(cases, 2)}")
    return fails


def main(argv: list[str]) -> int:
    cmd = argv[0] if argv else "check"
    if cmd == "selftest":
        fails = selftest()
        for f in fails:
            print(f"  FAIL  {f}")
        print(f"benchset: {8 - len(fails)} of 8 cases hold (sound set, no overwrite, edited hash, unlanded and "
              "frontmatter gold, drift, the loader ignores edited records, a tampered file refused, clusters)")
        consumer = consumer_selftest()
        for f in consumer:
            print(f"  FAIL  {f}")
        print(f"benchset consumers: {'held' if not consumer else f'{len(consumer)} failed'} (ask.bench and novelgraph's "
              "repo.bench_cases read the frozen file, follow records only when live, refuse a tampered file before scoring)")
        return 1 if fails or consumer else 0
    if cmd == "freeze":
        version = int(argv[argv.index("--version") + 1]) if "--version" in argv else 1
        target = freeze(version)
        frozen = load(target)
        print(f"froze {len(frozen['cases'])} cases, {sum(len(c['gold']) for c in frozen['cases'])} gold lines "
              f"→ {target.relative_to(ROOT)} (sha256 {frozen['sha256'][:12]})")
        return 0
    path = Path(argv[1]) if len(argv) > 1 else path_for(1)
    frozen = load(path)
    if cmd == "check":
        fails = integrity(frozen)
        for f in fails[:20]:
            print(f"  FAIL  {f}")
        d = drift(frozen, live())
        print(f"{path.name}: {len(frozen['cases'])} cases, sha256 {frozen['sha256'][:12]} — "
              f"{'integrity holds' if not fails else f'{len(fails)} integrity failures'}")
        print(f"drift since {frozen['from_commit'][:8]}: {len(d['changed'])} cases changed, "
              f"{len(d['new'])} new, {len(d['gone'])} gone"
              + "".join(f"\n  {cid}: +{v['added']} −{v['removed']} gold lines"
                        f"{', question changed' if v['question_changed'] else ''}" for cid, v in d["changed"].items()))
        return 1 if fails else 0
    if cmd == "clusters":
        cases = frozen["cases"]
        per_doc = Counter(d for c in cases for d in {g[0] for g in c["gold"]})
        print(f"{len(cases)} cases, {len(per_doc)} gold documents; a document is gold in "
              f"{max(per_doc.values())} cases at most, in ≥ 2 cases for {sum(v >= 2 for v in per_doc.values())}")
        for k in (1, 3, 5, 8, 12):
            groups = clusters(cases, k)
            print(f"  linked by ≥ {k:2} shared documents: {len(groups)} groups, sizes "
                  f"{[len(g) for g in groups]}")
        return 0
    print(__doc__)
    return 2


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
