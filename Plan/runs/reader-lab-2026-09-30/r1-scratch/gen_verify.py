"""Run every verification command and write the commands with their output, as printed, to
Plan/runs/<slug>/05-verify.txt. Nothing in the output is typed by hand: each block is the
stdout/stderr of the command shown above it."""
import shlex
import subprocess
import sys
from pathlib import Path

ROOT = Path("/home/user/kohaerenzprotokoll")
SP = Path("/tmp/claude-0/-home-user-kohaerenzprotokoll/9312df84-970d-5f58-8110-95cdece16e80/scratchpad")
S = "technical-audit-research-mandate-the-kohaerenz-protokoll-fra"
OUT = ROOT / "Plan" / "runs" / S / "05-verify.txt"

blocks: list[str] = []


def section(letter: str, title: str, note: str) -> None:
    bar = "=" * 78
    blocks.append(f"\n{bar}\n{letter}. {title}\n{note}\n{bar}\n")


def run(cmd: str) -> None:
    res = subprocess.run(cmd, shell=True, executable="/bin/bash", cwd=ROOT, capture_output=True, text=True)
    out = (res.stdout + res.stderr).rstrip("\n")
    blocks.append(f"$ {cmd}\n{out}\n")


def count(*terms: str) -> None:
    for t in terms:
        run(f"python3 scripts/read.py {S} --count {shlex.quote(t)}")


# --------------------------------------------------------------------------------------------
section("A", "The run: profile, size, the candidate list, the counts",
        "Every number the census states about the file's shape, the list and its counts. The census tables are\n"
        "compared with counts.json row by row; counts.json is compared with read.py --count for every term.")
run(f"python3 scripts/profile.py {S}")
run(f"wc -l Sources/drive/{S}.md")
run(f"grep -c '^- ' Plan/runs/{S}/03-candidates.md")
run(f"""python3 - <<'EOF'
import sys, json, re
sys.path.insert(0, 'scripts')
import capture, quotes
slug = '{S}'
md = open(f'Plan/runs/{{slug}}/03-candidates.md', encoding='utf-8').read()
head, _, lens = md.partition('\\n## lens')
lens = lens.partition('\\n## Open while reading')[0]
main, lensT = capture.candidate_terms(head), capture.candidate_terms(lens)
allT = capture.candidate_terms(md)
print('candidates (- lines read as terms):', len(allT), '= world and own terms', len(main), '+ lens', len(lensT))
counts = json.load(open(f'Plan/runs/{{slug}}/counts.json', encoding='utf-8'))
print('read_as_prose in counts.json:', counts['read_as_prose'])
c = counts['counts']
print('terms counted:', len(c), '| same terms, same order as the list:', list(c) == allT)
print('terms at 0 standing alone:', [t for t, v in c.items() if v['n'] == 0])
print('terms at 0 including compounds:', [t for t, v in c.items() if v['n_including_compounds'] == 0])
bad = [t for t, v in c.items() if quotes.count_words(slug, t)[0] != v['n'] or quotes.count_words(slug, t)[2] != v['n_including_compounds']]
print('terms whose counts.json numbers differ from read.py --count (quotes.count_words):', bad)
print('rows where compounds add to the count (alone -> in, lines):')
for t, v in c.items():
    if v['n'] != v['n_including_compounds']:
        print('  ', t, v['n'], '->', v['n_including_compounds'], v['lines'])
print('K\\\\_1 lines:', c['K\\\\_1']['lines'], '| K\\\\_0 lines:', c['K\\\\_0']['lines'])
print('candidates that hold an escaped underscore:', [t for t in allT if '\\\\_' in t])
census = open(f'Sources/terms/{{slug}}.md', encoding='utf-8').read()
rows = re.findall(r'^\\| `(.+?)` \\| (\\d+) \\| (\\d+) \\| ([\\d, ]+) \\|$', census, re.M)
diff = [r[0] for r in rows if (int(r[1]), int(r[2]), r[3].strip()) != (c[r[0]]['n'], c[r[0]]['n_including_compounds'], ', '.join(map(str, c[r[0]]['lines'])))]
print('census table rows:', len(rows), '| rows that differ from counts.json:', diff, '| terms without a row:', [t for t in c if t not in [r[0] for r in rows]])
EOF""")

# --------------------------------------------------------------------------------------------
section("B", "Names and terms the census and the note count in prose",
        "python3 scripts/read.py <slug> --count \"<words>\" -- whole word case-sensitive, case-insensitive, with compounds.")
count("Kohärenz-Protokoll", "protocol", "the protocol", "the system", "AEGIS", "Kael", "Juna", "alters",
      "Lex", "Nyx", "Kiko", "Lia", "Lex, Nyx, Kiko, and Lia", "Mnemosyne-Archipel", "Kollaps-Kern", "Risse",
      "Nichts-Rauschen", "Algorithmische Melancholie", "Synthese", "cracks", "nothingness static",
      "K\\_1", "K\\_0", "must", "Research Mandate", "Research Mandate -", "Architectural Mandate",
      "substrate", "bedrock", "Axis", "Vortex", "Vortex Inversion", "phone call", "VOA", "storyform",
      "Dramatica quad", "simulation", "deus ex machina", "soft", "magic", "flavor", "broken",
      "Dual-Kernel Theory", "DKT", "Psychological Modularity", "Structural Waveforms", "Monstrous Symmetry",
      "Algorithmic Advance", "Participatory Universe", "5D", "5th", "crack", "advance", "Advance")
count('"Mnemosyne-Archipel"', '"Kollaps-Kern"', '"Risse"', '"Nichts-Rauschen"')
count("trauma", "The Architecture of Verification", "Technical Audit", "computational constraint",
      "primary competitive advantage", "logical necessity", "Immutable bedrock", "Structural resonance",
      "Dimensional rigidity", 'Allows access to "erased" data', "systemic narrative collapse—informational heat death",
      "The Truth-Rotation", "The Climax")
run(f"""python3 - <<'EOF'
import re
t = open('Sources/drive/{S}.md', encoding='utf-8').read().split('\\n')
def where(pat):
    return [(i + 1, len(re.findall(pat, l))) for i, l in enumerate(t) if re.search(pat, l)]
for name, pat in [('AEGIS', r'\\bAEGIS\\b'), ('Kael', r'\\bKael\\b'), ('Juna', r'\\bJuna\\b'), ('alters', r'\\balters\\b'),
                  ('Mnemosyne-Archipel', r'Mnemosyne-Archipel'), ('quoted Mnemosyne-Archipel', r'"Mnemosyne-Archipel"'), ('quoted Kollaps-Kern', r'"Kollaps-Kern"'), ('quoted Risse', r'"Risse"'), ('quoted Nichts-Rauschen', r'"Nichts-Rauschen"'), ('Algorithmische Melancholie', r'Algorithmische Melancholie'), ('substrate', r'\\bsubstrate\\b'), ('bedrock', r'\\bbedrock\\b'),
                  ('the system (any case)', r'\\b[Tt]he system\\b'), ('the protocol', r'\\bthe protocol\\b'), ('Kohärenz-Protokoll', r'Kohärenz-Protokoll'), ('must', r'\\bmust\\b'), ('broken', r'\\bbroken\\b'),
                  ('trauma/Trauma', r'\\b[Tt]rauma\\b'), ('Vortex', r'\\bVortex\\b'), ('Axis', r'\\bAxis\\b'),
                  ('phone call', r'phone call'), ('DKT', r'\\bDKT\\b'), ('Dual-Kernel Theory', r'Dual-Kernel Theory'),
                  ('coherence (any case)', r'\\b[Cc]oherence\\b'), ('writer', r'\\bwriter\\b'), ('We', r'\\bWe\\b'),
                  ('This audit / The audit / This document', r'\\b(This audit|The audit|This document)\\b')]:
    print(f'{{name:42}} (line, uses on it): {{where(pat)}}')
EOF""")

# --------------------------------------------------------------------------------------------
section("C", "Stance markers, and the family of the word verify",
        "The note's stance_markers, each counted with read.py --count; stance_marker_count is their sum.\n"
        "The verify family is asked form by form, case-sensitive.")
markers = ["Research Mandate -", "Architectural Mandate", "Critical Consistency Takeaways", "Stress-Test Requirement",
           "Theoretical Mathematical Claim", "Narrative Requirement", "Alignment Status", "Prescribed", "Mandated",
           "Required", "Verified", "Strategic Executive Summary", "Final Synthese Verdict",
           "definitive structural requirements", "structurally verified", "ready for publication"]
count(*markers)
run(f"""python3 - <<'EOF'
import re, subprocess, sys
sys.path.insert(0, 'scripts')
import quotes
slug = '{S}'
note = open(f'Sources/notes/{{slug}}.md', encoding='utf-8').read()
front = note.split('---')[1]
listed = re.search(r'^stance_markers: \\[(.*)\\]$', front, re.M).group(1)
markers = re.findall(r'"([^"]+)"', listed)
claimed = int(re.search(r'^stance_marker_count: (\\d+)', front, re.M).group(1))
total = 0
for m in markers:
    out = subprocess.run(['python3', 'scripts/read.py', slug, '--count', m], capture_output=True, text=True).stdout
    n = int(out.split()[-1].rsplit('#', 1)[1].rstrip(']'))
    total += n
    print(f'{{n:>2}}  {{m}}')
print('markers listed in the note:', len(markers), '| occurrences, summed from read.py --count:', total, '| stance_marker_count in the note:', claimed, '| equal:', total == claimed)
EOF""")
count("Verification", "verifying", "Verify", "Verified", "verified", "Verifier", "Verifies", "Validates")
run(f"""python3 - <<'EOF'
import re
t = open('Sources/drive/{S}.md', encoding='utf-8').read().split('\\n')
forms = ['Verification', 'verifying', 'Verify', 'Verified', 'verified', 'Verifier', 'Verifies']
tot = 0
for f in forms + ['Validates']:
    pat = r'(?<![\\w-])' + f + r'(?![\\w-])'
    hits = [(i + 1, len(re.findall(pat, l))) for i, l in enumerate(t) if re.search(pat, l)]
    if f in forms:
        tot += sum(n for _, n in hits)
    print(f'{{f:14}} (line, uses on it): {{hits}}')
print('occurrences of the seven verif- forms:', tot, '| lines that hold them:', sorted({{i + 1 for i, l in enumerate(t) if re.search(r'(?<![\\w-])(' + '|'.join(forms) + r')(?![\\w-])', l)}}))
EOF""")

# --------------------------------------------------------------------------------------------
section("D", "Absences: every word an absence claim names, counted",
        "A claim that the document does not write something is asked of the count. Zero standing alone, zero in any\n"
        "case and zero with compounds is the claim; where a word stands only inside a longer word, the output says so.")
count("author", "Author", "source", "Source", "sources", "reference", "references", "cited", "citation")
count("Tarskian", "Tarskian meta-language", "Tarskian Meta-language", "Husserlian", "Husserlian Spectator", "Iserian", "Iserian phenomenology", "Janetian", "Janetian action systems")
count("disputed", "superseded", "deprecated", "http", "2026", "2025", "checked", "tested", "proved", "proof",
      "confirmed", "demonstrated", "quotation", "quote", "quotes", "K1", "K0", "K₁", "K₀", "K_1", "K_0",
      "Tarski", "Husserl", "Iser", "Janet", "vertex operator algebra", "Vertex", "operator", "caller", "called",
      "Kap", "Kapitel", "Chapter", "chapter", "chapters", "German", "translation", "Synthesis",
      "Landauer's Principle", "Landauer’s Principle", "Chaitin's Halting Probability",
      "Chaitin’s Halting Probability", "Juna's Positioning", "Juna’s Positioning")

# --------------------------------------------------------------------------------------------
section("E", "Structure and export damage",
        "Glyphs, line lengths, headings, the table, the formulas, the labels and every number the document writes, each\n"
        "counted from the file by a command that shows how.")
run(f"""python3 - <<'EOF'
import re, sys
sys.path.insert(0, 'scripts')
import profile as P
t = open('Sources/drive/{S}.md', encoding='utf-8').read()
lines = t.split('\\n')
def where(pat):
    return [(i + 1, len(re.findall(pat, l))) for i, l in enumerate(lines) if re.search(pat, l)]
print('lines by split:', len(lines), '| last element empty:', lines[-1] == '', '| bytes:', len(t.encode('utf-8')))
print('U+2019 total:', t.count('\\u2019'), '| ASCII apostrophe total:', t.count("'"), 'on lines', where("'"))
print('em dash U+2014 total:', t.count('\\u2014'), 'on lines', where('\\u2014'))
print('ASCII double quote total:', t.count('"'), '| pairs:', sum(len(re.findall(r'"[^"]*"', l)) for l in lines), '| lines holding any:', len(where('"')))
print('double backslash occurrences:', t.count('\\\\\\\\'), '| escapes by the profile pattern:', len(P.ESCAPE.findall(t)), '| all backslashes:', t.count('\\\\'), '| typographic marks by the profile:', sum(t.count(c) for c in P.TYPOGRAPHIC))
print('dollar signs:', t.count('$'), '| formula spans:', sum(len(re.findall(r'\\$[^$]*\\$', l)) for l in lines), '| lines with a span:', len([1 for l in lines if '$' in l]))
print('pipes in L21:', lines[20].count('|'), '| || joins in L21:', lines[20].count('||'), '| lines that start with a pipe:', len([1 for l in lines if l.startswith('|')]))
print('question marks:', where(r'\\?'))
from rules.structure import MATH
print('the profile looks for these Unicode math symbols only:', MATH.pattern, '| lines that hold one:', [i + 1 for i, l in enumerate(lines) if MATH.search(l)])
print('the three longest lines (chars, line):', sorted([(len(l), i + 1) for i, l in enumerate(lines)], reverse=True)[:3])
print('glued reference number matches:', [(m.group(0), t[:m.start()].count(chr(10)) + 1) for m in P.GLUED_REF.finditer(t)])
print('italic spans (single asterisks):', [(i + 1, m.group(0)) for i, l in enumerate(lines) for m in re.finditer(r'(?<![*\\\\])\\*(?!\\*)([^*\\n]+?)(?<![*\\\\])\\*(?!\\*)', l)])
print('a space between a closing emphasis mark and , or . (line, text):', [(i + 1, l[max(0, m.start() - 22):m.end() + 2]) for i, l in enumerate(lines) for m in re.finditer(r'\\* [,.]', l)])
print('hyphen followed by a space inside a word:', [(i + 1, m.group(0)) for i, l in enumerate(lines) for m in re.finditer(r'\\w- \\w', l)])
print('a full stop with no space before the next capital (outside headings glued by **):', [(i + 1, l[max(0, m.start() - 18):m.end() + 12]) for i, l in enumerate(lines) for m in re.finditer(r'[a-z]\\.[A-Z]', l)])
print('month names written:', re.findall(r'\\b(?:January|February|March|April|May|June|July|August|September|October|November|December)\\b', t))
print('digit runs of more than two digits:', [(i + 1, x) for i, l in enumerate(lines) for x in re.findall(r'\\d{{3,}}', l)])
print('digit runs per line:', [(i + 1, re.findall(r'\\d+', l)) for i, l in enumerate(lines) if re.search(r'\\d', l)])
EOF""")
run(f"""python3 - <<'EOF'
import re
t = open('Sources/drive/{S}.md', encoding='utf-8').read()
lines = t.split('\\n')
print('numbered headings (number, line, character position in the line, line length):')
for m in re.finditer(r'\\*\\*(\\d)\\. ([^*]+)\\*\\*', t):
    ln = t[:m.start()].count('\\n') + 1
    ls = t.rfind('\\n', 0, m.start()) + 1
    print('  ', m.group(1), 'L' + str(ln), m.start() - ls, len(lines[ln - 1]), '|', m.group(2))
tbl = lines[20].split('unmodelable by the system.', 1)[1]
cells = [c.strip() for c in tbl.split('|') if c.strip() and not set(c.strip()) <= set('- ')]
print('the sentence that ends the Juna item runs into the first pipe:', 'system.| Theoretical' in lines[20])
print('table cells (header and data):', len(cells), '| distinct:', len(set(cells)), '| rows split at ||:', len(tbl.split('||')))
print('closing ** inside a formula:', '10^{{53}}**$' in lines[20], '196883 + 1**$' in lines[20])
axes = [x.strip() for m in re.finditer(r'Axis ([IVX]+(?: & [IVX]+)?):', t) for x in m.group(1).split('&')]
print('Axis headings:', len(re.findall(r'\\*\\*\\d\\. Axis', t)), '| numerals in them:', axes, '| axes:', len(axes))
m = re.search(r'\\*\\*Final Synthese Verdict:\\*\\*', t)
print('Final Synthese Verdict on L' + str(t[:m.start()].count('\\n') + 1))
bul = [(i + 1, re.match(r'  - \\*\\*(.+?)\\*\\*', l).group(1)) for i, l in enumerate(lines) if l.startswith('  - ')]
grp = [b for b in bul if b[1].startswith('\\\\*\\\\*')]
print('bulleted lines:', len(bul), '| group labels:', len(grp), [g[0] for g in grp], '| items with a bold label:', len(bul) - len(grp))
print('group labels read:', [g[1] for g in grp])
EOF""")
run(f"""python3 - <<'EOF'
import re, sys
sys.path.insert(0, 'scripts')
import capture
slug = '{S}'
t = open(f'Sources/drive/{{slug}}.md', encoding='utf-8').read().split('\\n')
terms = set(capture.candidate_terms(open(f'Plan/runs/{{slug}}/03-candidates.md', encoding='utf-8').read()))
items = [(i + 1, re.match(r'  - \\*\\*(.+?):\\*\\*', l).group(1)) for i, l in enumerate(t) if l.startswith('  - **') and not l.startswith('  - **\\\\*\\\\*')]
print('items with a bold label:', len(items))
miss = []
the = with_article = 0
for ln, lab in items:
    bare = re.sub(r'^The ', '', lab)
    if lab.startswith('The '):
        the += 1
        with_article += lab in terms
    if lab not in terms and bare not in terms:
        miss.append((ln, lab))
print('item labels not on the candidate list:', miss)
print('labels that begin with The:', the, '| of them listed with the article:', with_article)
print('the 26 item labels (line, label):', [(ln, lab) for ln, lab in items])
EOF""")

for q in ['Analyze the application', 'Verify the energy source', 'Account for the fact', 'Ensure narrative time', 'Mandate the use', 'Scrutinize the', 'Verify the VOA construction', 'Treat "Risse" (cracks)', 'Reconcile the three layers']:
    run(f"python3 scripts/read.py {S} --find {shlex.quote(q)}")
# --------------------------------------------------------------------------------------------
section("F", "Compound rows and case rows",
        "The nine rows whose count with compounds exceeds the count alone, the forms behind the extra counts, and the\n"
        "23 candidates whose case-insensitive count differs from the case-sensitive one.")
count("Axis I", "Axis II", "fire", "firewalls", "Moonshine", "Moonshine-Link", "coherence", "coherence-seeking",
      "reader", "readers", "entropy", "high-entropy", "dialetheia", "dialetheias", "storyform", "dual-storyform",
      "Foundation", "foundational", "Trauma", "Multiplicity", "Climax", "silence", "required", "Required")
run(f"""python3 - <<'EOF'
import re
t = open('Sources/drive/{S}.md', encoding='utf-8').read().split('\\n')
for f in ['firewalls', 'coherence-seeking', 'readers', 'high-entropy', 'dialetheias', 'dual-storyform', 'foundational', 'Moonshine-Link', 'Axis III', 'Axis II']:
    pat = r'(?<![\\w-])' + f + r'(?![\\w-])'
    print(f'{{f:18}} (line, uses on it): {{[(i + 1, len(re.findall(pat, l))) for i, l in enumerate(t) if re.search(pat, l)]}}')
EOF""")
run(f"""python3 - <<'EOF'
import sys, json, re
sys.path.insert(0, 'scripts')
import quotes
from wiki_index import mention
from subject import document
slug = '{S}'
c = json.load(open(f'Plan/runs/{{slug}}/counts.json', encoding='utf-8'))['counts']
doc = document(slug)
lines = doc.body.split('\\n')
rows = []
for t, v in c.items():
    w, f, i = quotes.count_words(slug, t)
    if f != w:
        pat = re.compile(mention(t).pattern, re.I)
        other = [(ln, m.group(0)) for ln, l in enumerate(lines, doc.offset) for m in pat.finditer(l) if m.group(0) != t]
        rows.append((t, w, f, other))
print('candidates whose case-insensitive count differs from the case-sensitive one:', len(rows))
for t, w, f, other in rows:
    print(f'  {{t!r}}: case-sensitive {{w}}, any case {{f}}; the other case stands at {{other}}')
EOF""")

# --------------------------------------------------------------------------------------------
section("G", "Evidence for the census's statements about the tools and the export",
        "What read.py --find refuses and why, the count mark for K\\_1 that quotes.py reports wrong, and what census.py's\n"
        "draft does with the six rows that hold an escaped underscore. The scratch files live in the session's scratchpad.")
run(f"""python3 - <<'EOF'
import sys
sys.path.insert(0, 'scripts')
import quotes
for w in ['K\\\\_1', 'K_1', 'Lex', 'Nyx', 'Lia', 'VOA', 'Kiko', 'Kael', 'the Coherence Kernel ( $K\\\\_1$ )']:
    print(f'{{w!r:40}} normalised {{quotes.normalise(w)!r:36}} fragments compared {{quotes.parts_of(w)}}')
print('the line of quotes.parts_of that drops the short fragments:')
import inspect
print(inspect.getsource(quotes.parts_of).splitlines()[-1].strip())
print('the footnote rule quotes.GLUED_REF, which normalise() applies to both sides:')
print(quotes.GLUED_REF.pattern)
print('the line of quotes.check_marks that undoes the escape before it counts:')
print([l.strip() for l in inspect.getsource(quotes.check_marks).splitlines() if 'ESCAPE.sub' in l][0])
print('the line of read.py that counts the words as typed:')
import read
print([l.strip() for l in inspect.getsource(read.main).splitlines() if 'count_words' in l][0])
EOF""")
run(f"python3 scripts/read.py {S} --find {shlex.quote('physics of information.The overarching thesis')}")
for q in ["K\\_1", "K_1", "the Coherence Kernel ( $K\\_1$ )", "Lex", "Lex, Nyx, Kiko, and Lia", "VOA",
          "Verify the VOA construction", "39 fragmented chapters", "resolving 39 fragmented chapters"]:
    run(f"python3 scripts/read.py {S} --find {shlex.quote(q)}")
run(f"""cat > {SP}/marktest.md <<'EOF'
---
source: Sources/drive/{S}.md
---
Test marks. `K\\_1` ^[{S}.md:#8] and `K\\_0` ^[{S}.md:#6] and `K_1` ^[{S}.md:#0] and `K1` ^[{S}.md:#0].
EOF
python3 scripts/quotes.py {SP}/marktest.md""")
run(f"""python3 - <<'EOF'
import sys
sys.path.insert(0, 'scripts')
import census
txt = census.draft('{S}')
open('{SP}/census-draft-scratch.md', 'w', encoding='utf-8').write(txt)
print('census.draft() wrote', len(txt), 'characters to the scratchpad, nothing under Sources/ or Plan/')
print('lines that open a census title in that draft:', txt.count(chr(10) + '# Term census'))
EOF
python3 scripts/quotes.py {SP}/census-draft-scratch.md""")

# --------------------------------------------------------------------------------------------
section("H", "The checks that close the run",
        "quotes.py over the census and the note, and every cited quotation of both asked of read.py --find.")
run(f"python3 scripts/quotes.py Sources/terms/{S}.md")
run(f"python3 scripts/quotes.py Sources/notes/{S}.md")
run(f"python3 {SP}/find_all.py")

header = (f"# 05-verify — {S}\n"
          "# written 2026-09-30 by the document-reader subagent (Sonnet) that finished the run; every command below was\n"
          "# run from the repository root by scripts, and its output is pasted as printed.\n")
OUT.write_text(header + "".join("\n" + b if not b.startswith("\n") else b for b in blocks), encoding="utf-8")
print("wrote", OUT.relative_to(ROOT), OUT.stat().st_size, "bytes,", sum(1 for b in blocks if b.startswith("$ ")), "commands")
