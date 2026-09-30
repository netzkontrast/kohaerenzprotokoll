"""For every quotation in the census and the note: ask `read.py --find` for its line and check the
citation is among the lines it names. Prints a summary and every disagreement."""
import re
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/user/kohaerenzprotokoll")
sys.path.insert(0, str(ROOT / "scripts"))
import quotes  # noqa: E402

S = "technical-audit-research-mandate-the-kohaerenz-protokoll-fra"
bad = 0
total = 0
for name in ("Sources/terms", "Sources/notes"):
    path = ROOT / name / f"{S}.md"
    text = path.read_text(encoding="utf-8")
    n = 0
    for match, refs in quotes.pairs(text):
        if not refs:
            continue
        quote = match.group("quote")
        cited = {int(re.match(r"L(\d+)", r).group(1)) for r in refs if re.match(r"L(\d+)", r)}
        out = subprocess.run(["python3", "scripts/read.py", S, "--find", quote], cwd=ROOT,
                             capture_output=True, text=True).stdout
        found = {int(x) for x in re.findall(r"^\^\[L(\d+)\]", out, re.M)}
        n += 1
        total += 1
        if not cited <= found:
            bad += 1
            print(f"MISMATCH {name}: cited {sorted(cited)} but --find says {sorted(found)}: {quote[:80]!r}")
    print(f"{name}: {n} cited quotations asked of read.py --find")
print(f"total {total}, mismatches {bad}")
