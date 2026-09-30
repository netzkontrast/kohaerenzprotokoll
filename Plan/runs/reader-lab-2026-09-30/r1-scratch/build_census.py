"""Assemble Sources/terms/<slug>.md from: the generated header (profile.py --frontmatter),
the hand-written prose template, and the two tables generated from counts.json."""
import json
import re
import sys
from pathlib import Path

ROOT = Path("/home/user/kohaerenzprotokoll")
SP = Path("/tmp/claude-0/-home-user-kohaerenzprotokoll/9312df84-970d-5f58-8110-95cdece16e80/scratchpad")
sys.path.insert(0, str(ROOT / "scripts"))
import capture  # noqa: E402

S = "technical-audit-research-mandate-the-kohaerenz-protokoll-fra"
run = ROOT / "Plan" / "runs" / S

counts = json.loads((run / "counts.json").read_text(encoding="utf-8"))["counts"]
md = (run / "03-candidates.md").read_text(encoding="utf-8")
head, _, lens_part = md.partition("\n## lens")
lens_part = lens_part.partition("\n## Open while reading")[0]
main_terms = capture.candidate_terms(head)
lens_terms = capture.candidate_terms(lens_part)
assert len(main_terms) == 188 and len(lens_terms) == 28, (len(main_terms), len(lens_terms))
assert main_terms + lens_terms == list(counts.keys())


def rows(terms):
    out = []
    for t in terms:
        c = counts[t]
        lines = ", ".join(str(n) for n in c["lines"])
        out.append(f"| `{t}` | {c['n']} | {c['n_including_compounds']} | {lines} |")
    return "\n".join(out)


header = (SP / "header.md").read_text(encoding="utf-8")
header = re.sub(r"^candidates: .*$", f"candidates: {len(counts)}", header, count=1, flags=re.M)
template = (SP / "census-template.md").read_text(encoding="utf-8")
template = template.replace("@@TABLE_MAIN@@", rows(main_terms)).replace("@@TABLE_LENS@@", rows(lens_terms))
template = template.replace("SLUG", S)
text = header.rstrip("\n") + "\n\n" + template
(ROOT / "Sources" / "terms" / f"{S}.md").write_text(text, encoding="utf-8")
print("wrote census:", len(text), "chars,", text.count("\n"), "lines")
