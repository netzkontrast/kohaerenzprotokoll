#!/usr/bin/env python3
"""What every HyperExtract contract did on every source — one overview per source, and one matrix — derived from the runs.

On the author's „Zu wissen, dass ein Contract nichts liefert, ist ja auch ein wertvolles Wissen - wir sollten solche
Metainfos zentraler pro Source speichern" (2026-10-01). A run leaves its record in `Plan/runs/<slug>/hyperextract/<run>/`
(`usage.json`, and `report.json` when staging ran); this script reads them all and gives each run **one outcome**:

| outcome | means | read from |
|---|---|---|
| `yielded` | staging admitted at least one row | `report.json` |
| `refused` | the model returned rows and staging admitted none | `report.json` |
| `found nothing` | every call answered and every chunk validated, and the list came back empty — the contract has nothing to say about this document | `usage.json`: `failed` names the empty list, no failed call, no failed chunk |
| `not staged` | the model returned rows of a shape staging does not take (a set template) — kept in `raw.json` | `usage.json`: `failed` names the shape |
| `failed` | a call or a chunk failed and nothing came back — **not** knowledge about the document | `usage.json` |

`found nothing` and `failed` are kept apart on purpose: an empty list from a run whose calls failed says nothing about the
document, and HyperExtract once swallowed schema errors into empty lists (`reading_extract.candidates` refuses both alike;
only the calls' own record tells them apart, as `hegraph.report` already did). A run whose contract has changed since is
marked `stale` when its record names the template's sha256 and the file's sha256 is now different.

    python3 scripts/contracts.py            # writes Plan/runs/<slug>/contracts.{json,md} and Plan/runs/contracts.md
    python3 scripts/contracts.py --check    # exit 1 when any of them is not what the runs say now
    python3 scripts/contracts.py selftest

Derived, committed and checked like `overview.py`'s section: a person reads the overview in the source's run directory
without running anything, and `--check` keeps it true. Standard library only; nothing here judges whether a row is right.
"""

from __future__ import annotations

import hashlib
import json
import re
import sys
import tempfile
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

OUTCOMES = ("yielded", "refused", "found nothing", "not staged", "failed")
CELL = {"yielded": None, "refused": "0", "found nothing": "∅", "not staged": "n.s.", "failed": "✗"}
DATE = re.compile(r"(\d{4}-\d{2}-\d{2})")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else ""


def outcome(run: Path) -> dict:
    """One run's record and its outcome."""
    usage = json.loads((run / "usage.json").read_text(encoding="utf-8")) if (run / "usage.json").is_file() else {}
    report = json.loads((run / "report.json").read_text(encoding="utf-8")) if (run / "report.json").is_file() else None
    raw = json.loads((run / "raw.json").read_text(encoding="utf-8")) if (run / "raw.json").is_file() else None
    contract = (usage.get("template") or "").removesuffix(".yaml")
    if not contract and report and report.get("rows"):
        contract = report["rows"][0].get("template", "")
    chunks = usage.get("chunks") or []
    failed_chunks = sum(not c.get("ok") for c in chunks)
    rec = {"run": run.name, "contract": contract, "model": usage.get("model", ""),
           "date": m.group(1) if (m := DATE.search(run.name)) else "",
           "calls": usage.get("calls", 0), "failed_calls": usage.get("failed_calls", 0),
           "chunks": len(chunks) or None, "failed_chunks": failed_chunks if chunks else None,
           "cost_usd": round(usage.get("cost_usd", 0.0), 4),
           "template_sha256": (report or {}).get("template_sha256") or usage.get("template_sha256", ""),
           "rows": 0, "candidates": 0, "refused": {}, "duplicates": 0}
    failed = str(usage.get("failed", ""))
    if report is not None:
        rec.update(rows=report["input_rows"], candidates=report["candidates"], duplicates=report["duplicates"],
                   refused=dict(Counter(r["reason"] for r in report["rows"] if r["status"] == "refused")))
        rec["outcome"] = "yielded" if report["candidates"] else "refused"
    elif failed.startswith("candidate lacks") and raw:
        rec["rows"] = len(raw.get("items", [])) + len(raw.get("nodes", [])) + len(raw.get("edges", []))
        rec["outcome"] = "not staged"
    elif failed.startswith("empty or invalid candidate list") and not rec["failed_calls"] and not failed_chunks:
        rec["outcome"] = "found nothing"
    else:
        rec["outcome"] = "failed"
        rec["why"] = failed[:200] or "no record of the run's result"
    return rec


def collect(root: Path = ROOT) -> dict[str, list[dict]]:
    """slug -> every run on it, for the slugs the manifest knows (a scratch directory is not a source)."""
    from subject import read_jsonl
    manifest = root / "Sources" / "manifest.jsonl"
    known = {r["slug"] for r in read_jsonl(manifest)} if manifest.is_file() else None
    out: dict[str, list[dict]] = {}
    for run in sorted((root / "Plan" / "runs").glob("*/hyperextract/*/")):
        slug = run.parts[-3]
        if known is not None and slug not in known:
            continue
        rec = outcome(run)
        template = root / "Plan" / "hyperextract" / f"{rec['contract']}.yaml"
        rec["stale"] = bool(rec["template_sha256"]) and template.is_file() and sha(template) != rec["template_sha256"]
        out.setdefault(slug, []).append(rec)
    return out


def contracts(root: Path = ROOT) -> list[str]:
    return sorted(p.stem for p in (root / "Plan" / "hyperextract").glob("*.yaml"))


def cell(rec: dict) -> str:
    c = CELL[rec["outcome"]]
    return (str(rec["candidates"]) if c is None else c) + ("*" if rec["stale"] else "")


def source_md(slug: str, runs: list[dict], names: list[str]) -> str:
    by = {}
    for r in runs:
        by.setdefault(r["contract"], []).append(r)
    tally = Counter(r["outcome"] for r in runs)
    out = [f"# Contracts on `{slug}`", "",
           "Every HyperExtract contract run on this source, one line per run — written by `scripts/contracts.py` from the "
           "run directories beside this file, and checked by `contracts.py --check`. *found nothing* is knowledge about the "
           "document (every call answered, the list came back empty); *failed* is not. *candidates* are rows staging "
           "admitted, not rows anyone judged right.", "",
           f"{len(runs)} runs of {len(by)} contracts: " + ", ".join(f"{tally[o]} {o}" for o in OUTCOMES if tally[o])
           + f"; ${sum(r['cost_usd'] for r in runs):.2f}.", "",
           "| contract | run | model | outcome | rows | candidates | refused | chunks | cost |",
           "|---|---|---|---|---|---|---|---|---|"]
    for name in names:
        for r in by.get(name, []):
            refused = ", ".join(f"{n} {k}" for k, n in sorted(r["refused"].items())) or "—"
            chunks = "—" if r["chunks"] is None else f"{r['chunks']}" + (f" ({r['failed_chunks']} failed)" if r["failed_chunks"] else "")
            out.append(f"| `{name}` | `{r['run']}` | {r['model'].removeprefix('claude-cli/')} | {r['outcome']}"
                       + (" · stale" if r["stale"] else "") + f" | {r['rows']} | {r['candidates']} | {refused} | {chunks} | ${r['cost_usd']:.3f} |")
    never = [n for n in names if n not in by]
    if never:
        out += ["", "**Never run on this source:** " + ", ".join(f"`{n}`" for n in never) + "."]
    return "\n".join(out) + "\n"


def matrix_md(data: dict[str, list[dict]], names: list[str]) -> str:
    out = ["# Contracts × sources", "",
           "Which HyperExtract contract has run on which source, and what came of it — written by `scripts/contracts.py`; "
           "each source's own file is `Plan/runs/<slug>/contracts.md`. A cell is the latest run's outcome: a number is the "
           "candidates staging admitted; `0` the model returned rows and none was admitted; `∅` **found nothing** (every call "
           "answered, the list empty); `n.s.` rows of a shape staging does not take; `✗` failed; blank never run; `*` the "
           "contract has changed since the run. Where a contract ran more than once (two models, repeats), the latest run "
           "shows here and every run is in the source's file.", ""]
    used = [n for n in names if any(r["contract"] == n for runs in data.values() for r in runs)]
    out += ["| source | " + " | ".join(f"`{n}`" for n in used) + " |", "|---|" + "---|" * len(used)]
    for slug in sorted(data):
        latest = {}
        for r in sorted(data[slug], key=lambda r: (r["date"], r["run"])):
            latest[r["contract"]] = r
        out.append(f"| [`{slug}`]({slug}/contracts.md) | "
                   + " | ".join(cell(latest[n]) if n in latest else "" for n in used) + " |")
    tally = Counter(r["outcome"] for runs in data.values() for r in runs)
    out += ["", f"{sum(tally.values())} runs on {len(data)} sources: "
            + ", ".join(f"{tally[o]} {o}" for o in OUTCOMES if tally[o]) + "."]
    unused = [n for n in names if n not in used]
    if unused:
        out += ["", "Never run on any source: " + ", ".join(f"`{n}`" for n in unused) + "."]
    return "\n".join(out) + "\n"


def files(root: Path = ROOT) -> dict[Path, str]:
    data, names = collect(root), contracts(root)
    out = {}
    for slug, runs in data.items():
        base = root / "Plan" / "runs" / slug
        out[base / "contracts.json"] = json.dumps({"source": slug, "runs": runs}, ensure_ascii=False, indent=1) + "\n"
        out[base / "contracts.md"] = source_md(slug, runs, names)
    out[root / "Plan" / "runs" / "contracts.md"] = matrix_md(data, names)
    return out


def write(root: Path = ROOT) -> int:
    out = files(root)
    for path, text in out.items():
        path.write_text(text, encoding="utf-8")
    print(f"{len(out) - 1} source overviews and the matrix written")
    return 0


def check(root: Path = ROOT) -> int:
    stale = [p for p, text in files(root).items() if not p.is_file() or p.read_text(encoding="utf-8") != text]
    for p in stale:
        print(f"STALE {p.relative_to(root)}")
    print(f"contracts: {'every overview matches the runs' if not stale else f'{len(stale)} files stale — run scripts/contracts.py'}")
    return 1 if stale else 0


def selftest() -> int:
    cases = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "Plan" / "hyperextract").mkdir(parents=True)
        (root / "Plan" / "hyperextract" / "Alpha.yaml").write_text("name: Alpha\n", encoding="utf-8")
        (root / "Plan" / "hyperextract" / "Beta.yaml").write_text("name: Beta\n", encoding="utf-8")
        tsha = sha(root / "Plan" / "hyperextract" / "Alpha.yaml")

        def run(name, usage, report=None, raw=None):
            d = root / "Plan" / "runs" / "doc" / "hyperextract" / name
            d.mkdir(parents=True)
            (d / "usage.json").write_text(json.dumps({"template": "Alpha.yaml", "model": "claude-cli/sonnet",
                                                      "calls": 2, "failed_calls": 0, "cost_usd": 0.1, **usage}))
            if report is not None:
                (d / "report.json").write_text(json.dumps(report))
            if raw is not None:
                (d / "raw.json").write_text(json.dumps(raw))
            return outcome(d)
        ok = [{"ok": True}, {"ok": True}]
        row = {"status": "candidate", "reason": None}
        got = run("a-2026-10-01", {"chunks": ok}, {"input_rows": 2, "candidates": 1, "duplicates": 0,
                                                   "template_sha256": tsha,
                                                   "rows": [row, {"status": "refused", "reason": "quote not placed"}]})
        cases.append(("admitted rows: yielded, with its refusals", got["outcome"] == "yielded"
                      and got["refused"] == {"quote not placed": 1}))
        got = run("b-2026-10-01", {"chunks": ok}, {"input_rows": 1, "candidates": 0, "duplicates": 0,
                                                   "rows": [{"status": "refused", "reason": "x"}]})
        cases.append(("rows, none admitted: refused", got["outcome"] == "refused"))
        got = run("c-2026-10-01", {"chunks": ok, "failed": "empty or invalid candidate list: not a successful extraction"})
        cases.append(("every call answered, empty: found nothing", got["outcome"] == "found nothing"))
        got = run("d-2026-10-01", {"chunks": [{"ok": True}, {"ok": False}],
                                   "failed": "empty or invalid candidate list: not a successful extraction"})
        cases.append(("a failed chunk and empty: failed, not found nothing", got["outcome"] == "failed"))
        got = run("e-2026-10-01", {"failed_calls": 1, "failed": "empty or invalid candidate list: not a successful extraction"})
        cases.append(("a failed call and empty: failed", got["outcome"] == "failed"))
        got = run("f-2026-10-01", {"chunks": ok, "failed": "candidate lacks nonempty string fields: term"},
                  raw={"items": [{"name": "x"}, {"name": "y"}]})
        cases.append(("a shape staging does not take: not staged, its rows counted",
                      got["outcome"] == "not staged" and got["rows"] == 2))
        (root / "Plan" / "hyperextract" / "Alpha.yaml").write_text("name: Alpha\nchanged: true\n", encoding="utf-8")
        data = collect(root)
        cases.append(("a run of a changed contract is stale", any(r["stale"] for r in data["doc"] if r["run"] == "a-2026-10-01")))
        md = matrix_md(data, contracts(root))
        cases.append(("the matrix shows the latest run and names a contract never run", "`Beta`" not in md.split("\n\n")[2]
                      and "Never run on any source: `Beta`" in md))
        write(root)
        cases.append(("written files pass the check", check(root) == 0))
        (root / "Plan" / "runs" / "doc" / "contracts.md").write_text("edited by hand\n", encoding="utf-8")
        cases.append(("a hand-edited overview fails the check", check(root) == 1))
    failed = [n for n, ok in cases if not ok]
    for n, ok in cases:
        print(("held " if ok else "FAIL ") + n)
    print(f"contracts: {len(cases) - len(failed)} of {len(cases)} cases hold")
    return 1 if failed else 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        return selftest()
    if argv[:1] == ["--check"]:
        return check()
    if argv:
        print(__doc__)
        return 2
    return write()


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
