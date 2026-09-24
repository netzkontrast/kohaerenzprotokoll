#!/usr/bin/env python3
"""Score a Hyper-Extract LocationRegistry Knowledge Abstract against document 6's
own master table (Sources/drive/roman-lokalitaeten-konzept-und-ausarbeitung.md,
starting at L185).

Written for Plan/concept/hyperextract-templates_2026-09-24.md's scoring plan:
"LocationRegistry ... scored by code against the document's own master table
... which Location Name rows came back, and whether each source equals the
table's Source cell exactly." No line field is scored (P26) and nothing here
merges two surfaces.

Usage:
    python3 score_location_registry.py <ka_items.json>

<ka_items.json> is whatever he parse's LocationRegistry output holds its items
as (a list of {name, level, source, function, characters} objects, or a dict
with an "items" key holding that list). This script does not call `he` itself.
"""
import json
import re
import sys
from pathlib import Path

DOC = Path(__file__).resolve().parents[3] / "Sources" / "drive" / "roman-lokalitaeten-konzept-und-ausarbeitung.md"


def load_master_table():
    """Parse the document's own table starting at L185 (1-indexed)."""
    lines = DOC.read_text(encoding="utf-8").splitlines()
    rows = []
    # table body starts two lines after the header row at L185 (header + separator)
    for i, raw in enumerate(lines[184:], start=185):  # L185 is index 184
        if not raw.strip().startswith("|"):
            if rows:
                break
            continue
        cells = [c.strip() for c in raw.strip().strip("|").split("|")]
        if len(cells) != 5:
            continue
        name = re.sub(r"\\?\*\\?\*", "", cells[0]).strip()
        # header row and Kern-Welt section dividers: exactly one non-empty cell
        non_empty = [c for c in cells if c and c not in ("", ":-:")]
        if name in ("Location Name", "") or (len(non_empty) == 1 and cells[0] == non_empty[0]):
            continue
        if all(not c for c in cells[1:]):
            continue  # section header row, e.g. "**Kern-Welt 1 (LogOS)**"
        rows.append({
            "line": i,
            "name": name,
            "level": cells[1],
            "source": cells[2],
            "function": cells[3],
            "characters": cells[4],
        })
    return rows


def load_model_items(path):
    data = json.loads(Path(path).read_text(encoding="utf-8"))
    if isinstance(data, dict):
        items = data.get("items", data.get("data", []))
    else:
        items = data
    out = []
    for it in items:
        out.append({
            "name": (it.get("name") or it.get("Location Name") or "").strip(),
            "source": (it.get("source") or it.get("Source") or "").strip(),
        })
    return out


def norm(s):
    return re.sub(r"\s+", " ", s or "").strip().lower()


def main(argv):
    if len(argv) != 1:
        print(__doc__)
        return 2
    gold = load_master_table()
    gold_by_name = {norm(r["name"]): r for r in gold}
    model = load_model_items(argv[0])
    model_by_name = {}
    for it in model:
        model_by_name.setdefault(norm(it["name"]), it)

    gold_names = set(gold_by_name)
    model_names = set(model_by_name)
    shared = gold_names & model_names
    missing = gold_names - model_names   # in the table, not returned
    extra = model_names - gold_names     # returned, not in the table

    source_exact = 0
    source_mismatches = []
    for n in sorted(shared):
        g = gold_by_name[n]["source"]
        m = model_by_name[n]["source"]
        if m == g:
            source_exact += 1
        else:
            source_mismatches.append((gold_by_name[n]["name"], g, m))

    p = len(shared) / len(model_names) if model_names else 0.0
    r = len(shared) / len(gold_names) if gold_names else 0.0
    f1 = 2 * p * r / (p + r) if (p + r) else 0.0

    print(f"gold rows (document's own table, L185+): {len(gold_names)}")
    print(f"model rows: {len(model_names)}")
    print(f"shared (name match): {len(shared)}")
    print(f"missing (in table, not returned): {len(missing)}")
    print(f"extra (returned, not in table): {len(extra)}")
    print(f"precision={p:.3f} recall={r:.3f} f1={f1:.3f}")
    print(f"source exact match, of {len(shared)} shared rows: {source_exact} ({source_exact/len(shared)*100:.1f}%)" if shared else "source exact match: n/a (no shared rows)")
    if source_mismatches:
        print("mismatches (name, gold source, model source):")
        for name, g, m in source_mismatches:
            print(f"  {name!r}: gold={g!r} model={m!r}")
    if missing:
        print("missing names:", sorted(gold_by_name[n]["name"] for n in missing)[:20], "..." if len(missing) > 20 else "")
    if extra:
        print("extra names:", sorted(model_by_name[n]["name"] for n in extra)[:20], "..." if len(extra) > 20 else "")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
