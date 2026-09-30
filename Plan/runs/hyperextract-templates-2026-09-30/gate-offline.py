"""Offline, no model: what share of the text a gate keeps, and how many of an ungated run's lines fall inside it, for a cue and
a number of neighbours. The ungated rows are the first `CausalLinks` run of the scaled pass on the German documents among the
twelve (an English document is not gated). Run from the repository root with `.venv-graphqlite/bin/python`; its output is
`gate-offline.txt`. An upper bound on recall: it assumes the model finds every line inside a kept paragraph, which `gate-ab.md`
shows it does not (a repeat finds 88 % of its own first run)."""
import json, re, sys
from pathlib import Path
sys.path.insert(0, "scripts")
import hegraph
DOCS = """kohaerenz-protokoll-philosophischer-bericht-md worldbuilding-konzept-kohaerenzprotokoll-md koharenz-protokoll-konzept-konsolidiert-2026-05-08-md kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md kohaerenz-protokoll-konzept-master-md kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md dramatica-storyform-synthese-aegis-analyse-2 hard-sf-roman-outline-dkt-physik-cosmic-horror""".split()
data = []
for slug in DOCS:
    text = Path(f"Sources/drive/{slug}.md").read_text(encoding="utf-8")
    if hegraph.english(text):
        continue
    rep = json.loads(Path(f"Plan/runs/{slug}/hyperextract/causallinks-haiku-2026-09-30/report.json").read_text())
    lines = {r["lines"][0] for r in rep["rows"] if r.get("quote_status") == "placed" and len(r.get("lines") or []) == 1
             and (r["status"] == "candidate" or (r["status"] == "refused" and r.get("reason") == "surface absent from document"))}
    fl = text.splitlines()
    paras, cur, start = [], [], 1
    for i, l in enumerate(fl, 1):
        if l.strip():
            if not cur: start = i
            cur.append(l)
        elif cur:
            paras.append((start, i - 1, "\n".join(cur))); cur = []
    if cur: paras.append((start, len(fl), "\n".join(cur)))
    data.append((slug, paras, lines))
def evaluate(cue, neighbours):
    kept_chars = all_chars = found = total = 0
    for slug, paras, lines in data:
        keep = set()
        for i, (s, e, p) in enumerate(paras):
            if cue.search(p):
                keep.update(range(max(0, i - neighbours), min(len(paras), i + neighbours + 1)))
        all_chars += sum(len(p) for _, _, p in paras)
        kept_chars += sum(len(paras[i][2]) for i in keep)
        total += len(lines)
        found += sum(1 for l in lines if any(paras[i][0] <= l <= paras[i][1] for i in keep))
    return kept_chars / all_chars, found / total
print(f"{sum(len(l) for _,_,l in data)} ungated lines in {len(data)} German documents")
cur = hegraph.CUES["CAUSAL"]
paragraphs = [(s, e, p, any(s <= l <= e for l in lines)) for _, paras, lines in data for s, e, p in paras]
cued = [x for x in paragraphs if cur.search(x[2])]
print(f"{len(paragraphs)} paragraphs, {sum(x[3] for x in paragraphs)} hold a row ({sum(x[3] for x in paragraphs) / len(paragraphs):.0%}); "
      f"the current cue's {len(cued)} paragraphs ({len(cued) / len(paragraphs):.0%}): {sum(x[3] for x in cued) / len(cued):.0%} hold a row")
print("current cue: neighbours 0/1/2 →", [f"share {evaluate(cur, n)[0]:.0%} recall {evaluate(cur, n)[1]:.0%}" for n in (0, 1, 2)])
GENERIC = {
  "current": cur.pattern,
  "+ durch, indem, sodass, damit, wodurch": cur.pattern + r"|\bdurch\b|\bindem\b|sodass|so dass|\bdamit\b|wodurch|\bdenn\b|aufgrund|resultiert|entsteht|ergibt sich|→|bedingt|zur Folge",
  "+ the above, + kann, wird, zu": cur.pattern + r"|\bdurch\b|\bindem\b|sodass|so dass|\bdamit\b|wodurch|\bdenn\b|aufgrund|resultiert|entsteht|ergibt sich|→|bedingt|zur Folge|\bwird\b|\bkann\b|\bzu\b",
}
for name, pat in GENERIC.items():
    c = re.compile(pat, re.I)
    print(f"{name:45}", [f"n={n}: share {evaluate(c, n)[0]:.0%} recall {evaluate(c, n)[1]:.0%}" for n in (0, 1)])
