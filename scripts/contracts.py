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
| `unverified` | the record cannot show which of the above happened: no `usage.json`, no call, no chunk record, or no kept payload to check an empty list against — **not** knowledge either | — |

`found nothing` is claimed only when the record proves it, because it is read as knowledge about the source: at least one
call, a chunk record in which every chunk is valid, no failed call, and a kept `raw.json` that is the contract's own empty
container (`hx.validate` against the template, zero rows). Anything less is `failed` or `unverified`, never `∅` — an empty
list from a run whose calls failed says nothing about the document, and HyperExtract once swallowed schema errors into
empty lists (review on PR #136). The Haiku runs of 2026-09-30 kept no `raw.json`, so their empty lists are `unverified`.

Each run also says whether its inputs are still the ones it read: `template` is `current`, `changed` (the file's sha256
differs from the recorded one), `gone` (the contract file no longer exists) or `unrecorded`; `source` is `current`,
`changed` (the landed file's sha256 differs) or `unrecorded`. A run with either one not `current` is `stale` — the
outcome describes an earlier contract or an earlier text, and is marked so everywhere it is shown.

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

OUTCOMES = ("yielded", "refused", "found nothing", "not staged", "failed", "unverified")
CELL = {"yielded": None, "refused": "0", "found nothing": "∅", "not staged": "n.s.", "failed": "✗", "unverified": "?"}
DATE = re.compile(r"(\d{4}-\d{2}-\d{2})")


def sha(path: Path) -> str:
    return hashlib.sha256(path.read_bytes()).hexdigest() if path.is_file() else ""


def outcome(run: Path, root: Path = ROOT) -> dict:
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
           "source_sha256": (report or {}).get("source_sha256") or usage.get("source_sha256", ""),
           "rows": 0, "candidates": 0, "refused": {}, "duplicates": 0,
           "labels": {}, "model_choice": usage.get("model_choice")}
    failed = str(usage.get("failed", ""))
    if report is not None:
        rec.update(rows=report["input_rows"], candidates=report["candidates"], duplicates=report["duplicates"],
                   refused=dict(Counter(r["reason"] for r in report["rows"] if r["status"] == "refused")))
        marks = labels()
        rec["labels"] = dict(Counter(marks[r.get("id", "")[6:14]]["label"] for r in report["rows"]
                                     if r.get("id", "")[6:14] in marks))
        rec["outcome"] = "yielded" if report["candidates"] else "refused"
    elif failed.startswith("candidate lacks") and raw:
        rec["rows"] = len(raw.get("items", [])) + len(raw.get("nodes", [])) + len(raw.get("edges", []))
        rec["outcome"] = "not staged"
    elif failed.startswith("empty or invalid candidate list"):
        why = empty_unproven(usage, chunks, raw, rec["contract"], root)
        if why is None:
            rec["outcome"] = "found nothing"
        else:
            rec["outcome"] = "failed" if rec["failed_calls"] or failed_chunks else "unverified"
            rec["why"] = why
    elif not usage:
        rec["outcome"], rec["why"] = "unverified", "no usage.json"
    else:
        rec["outcome"] = "failed"
        rec["why"] = failed[:200] or "no record of the run's result"
    return rec


def empty_unproven(usage: dict, chunks: list, raw, contract: str, root: Path) -> str | None:
    """None when the record proves the contract answered and found nothing; else why it does not."""
    if not usage.get("calls"):
        return "no call was made"
    if usage.get("failed_calls"):
        return f"{usage['failed_calls']} failed calls"
    if not chunks:
        return "no chunk record"
    if not all(c.get("ok") for c in chunks):
        return f"{sum(not c.get('ok') for c in chunks)} chunks without a valid reply"
    if raw is None:
        return "no raw.json kept to check the empty list against"
    template = root / "Plan" / "hyperextract" / f"{contract}.yaml"
    if not template.is_file():
        return "the contract's template is gone; its empty container cannot be checked"
    import hx
    t = hx.load(template)
    keys = {"nodes", "edges"} if t.graphlike else {"items"}
    if not isinstance(raw, dict) or set(raw) != keys:
        return f"raw.json is not the contract's container: keys {sorted(raw) if isinstance(raw, dict) else type(raw).__name__}"
    try:
        data = hx.validate(t, raw)
    except (ValueError, hx.TemplateError) as exc:
        return f"raw.json is not the contract's container: {str(exc)[:120]}"
    if any(data.get(k) for k in ("items", "nodes", "edges")):
        return "raw.json holds rows, yet the run was refused as empty"
    return None


LABELS = ROOT / "Plan" / "runs" / "hyperextract-templates-2026-09-30" / "labels.jsonl"
_LABELS: dict | None = None


def labels() -> dict:
    """A reader's `ok`/`part`/`wrong` on a sample of rows, by the first eight characters of the row's id (`hegraph.labels`)."""
    global _LABELS
    if _LABELS is None:
        from subject import read_jsonl
        _LABELS = {r["id"]: r for r in read_jsonl(LABELS)} if LABELS.is_file() else {}
    return _LABELS


def collect(root: Path = ROOT) -> dict[str, list[dict]]:
    """slug -> every run on it, for the slugs the manifest knows (a scratch directory is not a source)."""
    from subject import read_jsonl
    manifest = root / "Sources" / "manifest.jsonl"
    rows = read_jsonl(manifest) if manifest.is_file() else None
    known = {r["slug"] for r in rows} if rows is not None else None
    category = {r["slug"]: r.get("category", "") for r in rows or []}
    out: dict[str, list[dict]] = {}
    for run in sorted((root / "Plan" / "runs").glob("*/hyperextract/*/")):
        slug = run.parts[-3]
        if known is not None and slug not in known:
            continue
        rec = outcome(run, root)
        template = root / "Plan" / "hyperextract" / f"{rec['contract']}.yaml"
        rec["template"] = ("gone" if not template.is_file() else "unrecorded" if not rec["template_sha256"]
                           else "current" if sha(template) == rec["template_sha256"] else "changed")
        source = root / "Sources" / "drive" / f"{slug}.md"
        rec["source"] = ("unrecorded" if not rec["source_sha256"] else "changed" if not source.is_file()
                         or sha(source) != rec["source_sha256"] else "current")
        rec["stale"] = rec["template"] in ("changed", "gone") or rec["source"] == "changed"
        rec["category"] = category.get(slug, "")
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
                       + (f" · stale (template {r['template']}, source {r['source']})" if r["stale"] else "")
                       + (f" · {r['why']}" if r.get("why") else "") + f" | {r['rows']} | {r['candidates']} | {refused} | {chunks} | ${r['cost_usd']:.3f} |")
    never = [n for n in names if n not in by]
    if never:
        out += ["", "**Never run on this source:** " + ", ".join(f"`{n}`" for n in never) + "."]
    return "\n".join(out) + "\n"


def matrix_md(data: dict[str, list[dict]], names: list[str]) -> str:
    out = ["# Contracts × sources", "",
           "Which HyperExtract contract has run on which source, and what came of it — written by `scripts/contracts.py`; "
           "each source's own file is `Plan/runs/<slug>/contracts.md`. A cell is the latest run's outcome: a number is the "
           "candidates staging admitted; `0` the model returned rows and none was admitted; `∅` **found nothing** (every call "
           "answered, every chunk valid, an empty container kept and checked); `n.s.` rows of a shape staging does not take; "
           "`✗` failed; `?` unverified (the record cannot show what happened); blank never run; `*` stale — the contract "
           "changed or is gone, or the source changed, since the run. Where a contract ran more than once (two models, repeats), the latest run "
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


def model_stats(root: Path = ROOT, data: dict | None = None) -> list[dict]:
    """Per (contract, category, model): runs, found nothing, admitted rows, cost, labelled rows and how many were `ok` —
    what `modelpick.choose` ranks by (labels only) and `Plan/runs/models.md` shows."""
    data = collect(root) if data is None else data
    agg: dict[tuple, dict] = {}
    for slug, runs in data.items():
        for r in runs:
            key = (r["contract"], r["category"], r["model"].removeprefix("claude-cli/"))
            a = agg.setdefault(key, {"contract": key[0], "category": key[1], "model": key[2], "runs": 0, "explored": 0,
                                     "found_nothing": 0, "admitted": 0, "cost_usd": 0.0, "labelled": 0, "ok": 0})
            a["runs"] += 1
            a["explored"] += bool((r.get("model_choice") or {}).get("explored"))
            a["found_nothing"] += r["outcome"] == "found nothing"
            a["admitted"] += r["candidates"]
            a["cost_usd"] += r["cost_usd"]
            a["labelled"] += sum(r["labels"].values())
            a["ok"] += r["labels"].get("ok", 0)
    return [agg[k] for k in sorted(agg)]


def models_md(stats: list[dict]) -> str:
    out = ["# Which model, where", "",
           "Every contract run by model and by the category of its source — written by `scripts/contracts.py`, the table "
           "`scripts/modelpick.py` chooses from (`Plan/hyperextract/models.json`: about a fifth of runs explore a model at "
           "random, the rest take the best **labelled** one). *admitted* rows are staging's, not a judgement; only "
           "*labelled ok* is precision, and a cell with fewer labelled rows than the policy's `min_labels` ranks nothing.", "",
           "| contract | category | model | runs (explored) | found nothing | admitted | $ per admitted row | labelled | ok |",
           "|---|---|---|---|---|---|---|---|---|"]
    for a in stats:
        per = f"{a['cost_usd'] / a['admitted']:.4f}" if a["admitted"] else "—"
        ok = f"{a['ok']} ({a['ok'] / a['labelled']:.0%})" if a["labelled"] else "—"
        out.append(f"| `{a['contract']}` | {a['category'] or '—'} | {a['model'] or '—'} | {a['runs']} ({a['explored']}) | "
                   f"{a['found_nothing']} | {a['admitted']} | {per} | {a['labelled']} | {ok} |")
    return "\n".join(out) + "\n"


def files(root: Path = ROOT) -> dict[Path, str]:
    data, names = collect(root), contracts(root)
    out = {}
    for slug, runs in data.items():
        base = root / "Plan" / "runs" / slug
        out[base / "contracts.json"] = json.dumps({"source": slug, "runs": runs}, ensure_ascii=False, indent=1) + "\n"
        out[base / "contracts.md"] = source_md(slug, runs, names)
    out[root / "Plan" / "runs" / "contracts.md"] = matrix_md(data, names)
    out[root / "Plan" / "runs" / "models.md"] = models_md(model_stats(root, data))
    return out


def write(root: Path = ROOT) -> int:
    out = files(root)
    for path, text in out.items():
        path.write_text(text, encoding="utf-8")
    print(f"{len(out) - 2} source overviews, the matrix and the model table written")
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
        real = (ROOT / "Plan" / "hyperextract" / "TermReadings.yaml").read_text(encoding="utf-8")
        (root / "Plan" / "hyperextract" / "Alpha.yaml").write_text(real, encoding="utf-8")
        (root / "Plan" / "hyperextract" / "Beta.yaml").write_text(real, encoding="utf-8")
        (root / "Sources" / "drive").mkdir(parents=True)
        (root / "Sources" / "drive" / "doc.md").write_text("Alpha steht hier.\n", encoding="utf-8")
        tsha, ssha = sha(root / "Plan" / "hyperextract" / "Alpha.yaml"), sha(root / "Sources" / "drive" / "doc.md")
        EMPTY = "empty or invalid candidate list: not a successful extraction"

        def run(name, usage, report=None, raw=None, template="Alpha.yaml"):
            d = root / "Plan" / "runs" / "doc" / "hyperextract" / name
            d.mkdir(parents=True)
            if usage is not None:
                (d / "usage.json").write_text(json.dumps({"template": template, "model": "claude-cli/sonnet",
                                                          "calls": 2, "failed_calls": 0, "cost_usd": 0.1,
                                                          "template_sha256": tsha, "source_sha256": ssha, **usage}))
            if report is not None:
                (d / "report.json").write_text(json.dumps(report))
            if raw is not None:
                (d / "raw.json").write_text(json.dumps(raw))
            return outcome(d, root)
        ok = [{"ok": True}, {"ok": True}]
        got = run("a-2026-10-01", {"chunks": ok}, {"input_rows": 2, "candidates": 1, "duplicates": 0,
                                                   "template_sha256": tsha, "source_sha256": ssha,
                                                   "rows": [{"status": "candidate", "reason": None},
                                                            {"status": "refused", "reason": "quote not placed"}]})
        cases.append(("admitted rows: yielded, with its refusals", got["outcome"] == "yielded"
                      and got["refused"] == {"quote not placed": 1}))
        got = run("b-2026-10-01", {"chunks": ok}, {"input_rows": 1, "candidates": 0, "duplicates": 0,
                                                   "rows": [{"status": "refused", "reason": "x"}]})
        cases.append(("rows, none admitted: refused", got["outcome"] == "refused"))
        got = run("c-2026-10-01", {"chunks": ok, "failed": EMPTY}, raw={"items": []})
        cases.append(("calls answered, chunks valid, the empty container kept: found nothing",
                      got["outcome"] == "found nothing"))
        for name, usage, raw, want in (
                ("d", {"chunks": [{"ok": True}, {"ok": False}], "failed": EMPTY}, {"items": []}, "failed"),
                ("e", {"failed_calls": 1, "chunks": ok, "failed": EMPTY}, {"items": []}, "failed"),
                ("g", {"calls": 0, "failed": EMPTY}, None, "unverified"),
                ("h", {"failed": EMPTY}, None, "unverified"),
                ("i", {"chunks": ok, "failed": EMPTY}, None, "unverified"),
                ("j", {"chunks": ok, "failed": EMPTY}, {"rows": "not the container"}, "unverified"),
                ("k", {"chunks": ok, "failed": EMPTY}, {"items": [{"term": "x", "quote": "y", "stance": "asserts"}]},
                 "unverified")):
            got = run(f"{name}-2026-10-01", usage, raw=raw)
            cases.append((f"{name}: {got.get('why', '')} — {want}, never found nothing", got["outcome"] == want))
        got = run("l-2026-10-01", None)
        cases.append(("no usage.json: unverified", got["outcome"] == "unverified"))
        got = run("f-2026-10-01", {"chunks": ok, "failed": "candidate lacks nonempty string fields: term"},
                  raw={"items": [{"name": "x"}, {"name": "y"}]})
        cases.append(("a shape staging does not take: not staged, its rows counted",
                      got["outcome"] == "not staged" and got["rows"] == 2))
        run("m-2026-10-01", {"chunks": ok, "failed": EMPTY}, raw={"items": []}, template="Gamma.yaml")
        (root / "Plan" / "hyperextract" / "Alpha.yaml").write_text(real + "# changed\n", encoding="utf-8")
        data = {r["run"]: r for r in collect(root)["doc"]}
        cases.append(("a run of a changed contract is stale", data["a-2026-10-01"]["template"] == "changed"
                      and data["a-2026-10-01"]["stale"]))
        cases.append(("a run of a deleted contract is stale, never current", data["m-2026-10-01"]["template"] == "gone"
                      and data["m-2026-10-01"]["stale"]))
        (root / "Sources" / "drive" / "doc.md").write_text("Alpha steht anders hier.\n", encoding="utf-8")
        data = {r["run"]: r for r in collect(root)["doc"]}
        cases.append(("a run on a changed source is stale", data["c-2026-10-01"]["source"] == "changed"
                      and data["c-2026-10-01"]["stale"]))
        md = matrix_md(collect(root), contracts(root))
        cases.append(("the matrix names a contract never run", "Never run on any source: `Beta`" in md))
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
