#!/usr/bin/env python3
"""A deterministic sample of one contract's staged rows on the backfill's documents, not yet labelled, each with its line.

    python3 Plan/runs/hyperextract-backfill-2026-09-30/sample.py <Contract> <n> [--all]

Draws the `n` staged rows (`hegraph.staged()`: admitted on the names or on the quotation alone) of the backfill's runs that
carry no label in `Plan/runs/hyperextract-templates-2026-09-30/labels.jsonl`, in the order of the SHA-256 of their id, so that
the same rows come first whoever draws and whenever — the drawing needs no random number and cannot be steered toward rows
that look right. `--all` draws from every run of the contract, earlier passes included. It prints each row's document, line,
term or relation, quotation and stance, and the line's own words beside it: a label (`ok`: the quotation states what the row
says and the row names what it is about; `part`: right, but loose or incomplete; `wrong`: neither) is written by a reader from
these two, into `labels.jsonl` with `"sample": "backfill documents"` — the working session's label, a proposal for the author to
overrule, never a measurement of the contract's precision on the corpus. Standard library plus `scripts/hegraph.py`.
"""
import hashlib
import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(ROOT / "scripts"))
import hegraph  # noqa: E402
from subject import document  # noqa: E402


def backfill_runs() -> set[tuple[str, str]]:
    """(document, run name) of every run whose approval names the backfill's instruction."""
    out = set()
    for f in (ROOT / "Plan" / "runs").glob("*/hyperextract/*-haiku-2026-09-30/usage.json"):
        if "Backpoet" in json.loads(f.read_text(encoding="utf-8")).get("approval", ""):
            out.add((f.parts[-4], f.parent.name))
    return out


def main(argv: list[str]) -> int:
    args = [a for a in argv if not a.startswith("--")]
    if len(args) != 2:
        print(__doc__)
        return 2
    template, n = args[0], int(args[1])
    mine = backfill_runs()
    labelled = hegraph.labels()
    rows = [(slug, run, row) for slug, run, row in hegraph.staged()
            if row.get("template", "").removesuffix(".yaml") == template
            and ("--all" in argv or (slug, run) in mine)
            and row["id"][6:14] not in labelled and row["id"][:8] not in labelled]
    print(f"## {template}: {len(rows)} unlabelled staged rows on {len({s for s, _, _ in rows})} documents"
          f"{' (every pass)' if '--all' in argv else ' (the backfill)'}")
    rows.sort(key=lambda x: hashlib.sha256(x[2]["id"].encode()).hexdigest())
    for slug, run, row in rows[:n]:
        raw = row["raw"]
        head = raw.get("term") if row["kind"] == "reading" else f"{raw.get('source')} —[{raw.get('type', '')}]→ {raw.get('target')}"
        doc = document(slug)
        ln = row["lines"][0]
        i = ln - doc.offset                      # `offset` is the file line of the body's first line
        body = doc.lines()
        print(f"\n[{row['id'][6:14]}] {slug[:40]} L{ln}  {head}")
        print(f"   quote: „{raw['quote'][:260]}“  stance={raw.get('stance', '')}")
        print(f"   line : {body[i][:300] if 0 <= i < len(body) else '(line out of range)'}")
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
