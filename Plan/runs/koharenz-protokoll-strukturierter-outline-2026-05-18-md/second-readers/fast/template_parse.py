"""No model: the chapter template of document 14, read by code.

Every chapter entry carries the same bold field labels (profile.py: `POV x41`,
`Charaktere x41`, `Sensorik x41` …). This reads each `**Label:** value` inside
each `### Kap N — Title` section into (subject, relation, object, line) rows, and
splits `Charaktere:` on commas outside brackets. A one-off to measure what code
alone gets from a templated document — not a pipeline step (P3).

    python3 Plan/runs/<slug>/second-readers/fast/template_parse.py
"""
import json
import re
import time
from pathlib import Path

t0 = time.perf_counter()
HERE = Path(__file__).resolve().parent
SLUG = HERE.parents[1].name
ROOT = HERE.parents[4]
lines = (ROOT / "Sources" / "drive" / f"{SLUG}.md").read_text(encoding="utf-8").split("\n")

def clean(s):
    return re.sub(r"\\([\[\]*\"_.\-()#+~])", r"\1", s).replace("**", "").replace("*", "").strip(" ·")

HEAD = re.compile(r"^###\s+(Kap \d+)\s+—\s+(.*)$")
FIELD = re.compile(r"\*\*([^*:]{1,40}):\*\*\s*")
rows, chapter = [], None
for n, raw in enumerate(lines, 1):
    m = HEAD.match(raw)
    if m:
        chapter = m.group(1)
        rows.append((chapter, "HAS_TITLE", clean(m.group(2)), n))
        continue
    if raw.startswith("## ") or chapter is None:
        if raw.startswith("## "):
            chapter = None
        continue
    marks = list(FIELD.finditer(raw))
    for i, f in enumerate(marks):
        label = clean(f.group(1))
        value = clean(raw[f.end(): marks[i + 1].start() if i + 1 < len(marks) else len(raw)])
        if not value:
            continue
        if label == "Charaktere":
            depth, part, parts = 0, "", []
            for ch in value:
                depth += ch == "("; depth -= ch == ")"
                if ch == "," and depth == 0:
                    parts.append(part); part = ""
                else:
                    part += ch
            parts.append(part)
            for p in parts:
                name = re.sub(r"\s*\(.*$", "", p).strip()
                if name:
                    rows.append((chapter, "HAS_CHARACTER", name, n))
        else:
            rel = "HAS_" + re.sub(r"[^A-Za-z0-9]+", "_", label.upper()).strip("_")
            rows.append((chapter, rel, value[:160], n))
elapsed = time.perf_counter() - t0
(HERE / "template.tsv").write_text("".join(f"{s}\t{r}\t{o}\tL{n}\n" for s, r, o, n in rows), encoding="utf-8")
names = sorted({o for s, r, o, n in rows if r in ("HAS_CHARACTER", "HAS_TITLE")} | {s for s, *_ in rows})
(HERE / "template-names.json").write_text(json.dumps(
    {"source": SLUG, "written_by": "template_parse.py, no model", "entities": [{"term": x} for x in names]},
    ensure_ascii=False, indent=1), encoding="utf-8")
from collections import Counter
print(f"{len(rows)} rows from {len({s for s, *_ in rows})} chapters in {elapsed*1000:.0f} ms")
print(Counter(r for _, r, _, _ in rows).most_common(12))
