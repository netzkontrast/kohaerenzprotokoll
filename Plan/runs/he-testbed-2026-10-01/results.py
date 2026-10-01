#!/usr/bin/env python3
"""One file per HyperExtract contract with every result of the testbed's two documents.

    python3 Plan/runs/he-testbed-2026-10-01/results.py

Reads what `run.sh` left in `Plan/runs/<doc>/hyperextract/<contract>-sonnet-2026-10-01/` — `report.json` (the rows
staging checked: candidate, refused and why, duplicate, with the lines code placed them on), `raw.json` (the merged
data as the model returned it, kept when staging refused the whole run, as it does for a set or a row shape it does not
know) and `usage.json` (calls, cost, chunks) — and writes `results/<Contract>.md` (to read) and
`results/<Contract>.jsonl` (to compute on), plus `results/README.md`, the table of all 32. Where the Haiku pilot of
2026-09-30 ran the same contract on the same document, the lines each model's admitted rows stand on are set side by
side. Nothing here judges a row: `ok`/`part`/`wrong` is a reader's label, and none is given. Standard library only.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
ROOT = HERE.parents[2]
sys.path.insert(0, str(ROOT / "scripts"))
import read  # noqa: E402
from subject import document  # noqa: E402

DOCS = ["kohaerenz-protokoll-meta-foreshadowing-beobachter-logik", "2026-09-14-kap25-vertiefung-md"]
SUFFIX = "-sonnet-2026-10-01"
OUT = HERE / "results"


def header(template: Path) -> list[str]:
    """The contract's own comment header: what it is, its provisional standing, what it may not do."""
    out = []
    for line in template.read_text(encoding="utf-8").splitlines():
        if not line.startswith("#"):
            break
        out.append(line.lstrip("# ").rstrip())
    return [l for l in out if l]


def rows_of(data: dict) -> list[tuple[str, dict]]:
    if "items" in data:
        return [("item", r) for r in data["items"]]
    return [("node", r) for r in data.get("nodes", [])] + [("edge", r) for r in data.get("edges", [])]


def cell(v) -> str:
    if v is None:
        return ""
    if isinstance(v, list):
        v = ", ".join(map(str, v))
    return str(v).replace("|", "\\|").replace("\n", " ")


def haiku_lines(slug: str, contract: str) -> set[int] | None:
    runs = sorted((ROOT / "Plan/runs" / slug / "hyperextract").glob(f"{contract.lower()}-haiku-2026-09-30"))
    if not runs or not (runs[0] / "report.json").is_file():
        return None
    rep = json.loads((runs[0] / "report.json").read_text(encoding="utf-8"))
    return {l for r in rep["rows"] if r["status"] == "candidate" for l in r["lines"]}


def one(template: Path) -> dict:
    name = template.stem
    md = [f"# {name} — the testbed's results", ""]
    md += [f"> {l}" for l in header(template)] + [""]
    md += [f"Sonnet through `claude -p`, one run at a time (`run.sh`). Run directory: "
           f"`Plan/runs/<document>/hyperextract/{name.lower()}{SUFFIX}/`. A row's *status* is staging's "
           "(`reading_extract.verify`): `candidate` — its quotation is placed on one line and every name in it stands "
           "in the document; `refused` — and why; `duplicate`; `not staged` — the run's shape is one staging does not "
           "take (a set, or fields it does not know), so the row is shown as the model gave it, its quotation placed "
           "here by `read.locate` where it has one. No row is judged right or wrong.", ""]
    summary = {"contract": name, "documents": {}}
    jsonl = []
    for slug in DOCS:
        run = ROOT / "Plan/runs" / slug / "hyperextract" / f"{name.lower()}{SUFFIX}"
        md += [f"## `{slug}`", ""]
        if not run.is_dir():
            md += ["Not run yet.", ""]
            summary["documents"][slug] = None
            continue
        usage = json.loads((run / "usage.json").read_text(encoding="utf-8"))
        chunks = usage.get("chunks", [])
        failed_chunks = sum(not c["ok"] for c in chunks)
        report = json.loads((run / "report.json").read_text(encoding="utf-8")) if (run / "report.json").is_file() else None
        raw = json.loads((run / "raw.json").read_text(encoding="utf-8")) if (run / "raw.json").is_file() else None
        s = {"calls": usage.get("calls"), "failed_calls": usage.get("failed_calls"), "cost_usd": usage.get("cost_usd"),
             "seconds": usage.get("seconds"), "chunks": len(chunks), "failed_chunks": failed_chunks,
             "failed": usage.get("failed")}
        doc = document(slug)
        if report:
            rows = report["rows"]
            s.update(rows=report["input_rows"], candidates=report["candidates"], refused=report["refused"],
                     duplicates=report["duplicates"])
            listing = [(r["kind"], r["raw"], r["status"], r.get("reason"), r["lines"]) for r in rows]
        else:
            listing = []
            for kind, r in rows_of(raw or {}):
                quote = r.get("quote") if isinstance(r.get("quote"), str) else None
                lines = read.locate(doc, quote) if quote else []
                listing.append((kind, r, "not staged", None, lines))
            s.update(rows=len(listing), candidates=0, refused=0, duplicates=0, not_staged=len(listing))
        line = (f"{s['calls']} calls ({s['failed_calls']} failed), {s['chunks']} chunks ({failed_chunks} without a valid "
                f"reply), ${s['cost_usd']}, {s['seconds']} s. **{s['rows']} rows**: {s['candidates']} candidates, "
                f"{s['refused']} refused, {s['duplicates']} duplicates"
                + (f", {s.get('not_staged')} not staged" if s.get("not_staged") else "") + ".")
        md += [line]
        if s["failed"]:
            md += ["", f"Staging refused the run: `{s['failed'][:300]}`"]
        mine = {l for _, _, st, _, ls in listing if st == "candidate" for l in ls}
        hl = haiku_lines(slug, name)
        if hl is not None:
            s["haiku_lines"], s["sonnet_lines"], s["both_lines"] = len(hl), len(mine), len(hl & mine)
            md += ["", f"Beside the Haiku pilot of 2026-09-30 on this document: the candidates stand on {len(mine)} lines "
                       f"here and {len(hl)} there, {len(hl & mine)} of them the same."]
        md += [""]
        if listing:
            fields = []
            for _, r, *_ in listing:
                for k in r:
                    if k != "quote" and k not in fields:
                        fields.append(k)
            md += ["| # | kind | status | " + " | ".join(fields) + " | quote | lines |",
                   "|" + "---|" * (len(fields) + 5)]
            for i, (kind, r, status, reason, lines) in enumerate(listing, 1):
                st = status + (f": {reason}" if reason else "")
                md += [f"| {i} | {kind} | {st} | " + " | ".join(cell(r.get(k)) for k in fields)
                       + f" | {cell(r.get('quote'))} | {', '.join(map(str, lines))} |"]
                jsonl.append({"document": slug, "kind": kind, "status": status, "reason": reason,
                              "lines": lines, "row": r})
            md += [""]
        else:
            md += ["The model returned no row on this document.", ""]
        summary["documents"][slug] = s
    (OUT / f"{name}.md").write_text("\n".join(md).rstrip() + "\n", encoding="utf-8")
    (OUT / f"{name}.jsonl").write_text("".join(json.dumps(r, ensure_ascii=False) + "\n" for r in jsonl), encoding="utf-8")
    return summary


def main() -> int:
    OUT.mkdir(exist_ok=True)
    summaries = [one(t) for t in sorted((ROOT / "Plan/hyperextract").glob("*.yaml"))]
    a, b = DOCS
    md = ["# The testbed's results, one file per contract", "",
          f"Every contract in `Plan/hyperextract/` on `{a}` (A, 4.2 KB) and `{b}` (B, 10.4 KB), Sonnet. "
          "*rows* — what the model returned; *cand.* — rows staging admitted; *ref.* — refused (the reasons are in "
          "each file); *n.s.* — rows of a run staging does not take, shown as given. Written by `results.py`.", "",
          "| contract | A rows | A cand. | A ref. | A n.s. | B rows | B cand. | B ref. | B n.s. | cost | file |",
          "|---|---|---|---|---|---|---|---|---|---|---|"]
    total = 0.0
    for s in summaries:
        cells, cost = [], 0.0
        for slug in DOCS:
            d = s["documents"].get(slug)
            if d is None:
                cells += ["—"] * 4
                continue
            cells += [str(d["rows"]), str(d["candidates"]), str(d["refused"]), str(d.get("not_staged", 0))]
            cost += d["cost_usd"] or 0
        total += cost
        md.append(f"| `{s['contract']}` | " + " | ".join(cells) + f" | ${cost:.3f} | [{s['contract']}.md]({s['contract']}.md) |")
    md += ["", f"Total cost of the runs present: **${total:.2f}**."]
    (OUT / "README.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    print(f"{len(summaries)} contracts, ${total:.2f}; {OUT.relative_to(ROOT)}/")
    return 0


if __name__ == "__main__":
    sys.exit(main())
