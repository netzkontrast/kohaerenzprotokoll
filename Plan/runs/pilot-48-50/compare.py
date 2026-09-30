"""The pilot's bar (plan step 4): the new readings step on documents 48–50 against
what the old step committed (7f11861), both on the pages as they stood at 3d97d39.

    python3 Plan/runs/pilot-48-50/compare.py <worktree after apply>
"""
import json, re, subprocess, sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[3]
DOCS = ["charakter-kompilation-fuer-kohaerenz-protokoll",
        "the-sensory-rulebook-the-body-as-a-measuring-device-in-the-p",
        "ki-prompt-analyse-hard-problem-of-consciousness"]
HEAD = re.compile(r"^## (?:Readings? — |\d{4}-\d{2}-\d{2} — )`([a-z0-9-]+)`", re.M)
CITE = re.compile(r"\^\[([a-z0-9-]+)\.md:L(\d+)")


def pairs_and_lines(read_file):
    """(page, doc) pairs with a section, and (page, doc, line) citations in those sections."""
    pairs, lines = set(), set()
    for f in ("Wiki/candidates", "Wiki/chapters", "Wiki/conflicts", "Wiki/questions"):
        for path, text in read_file(f):
            page = Path(path).stem
            m = re.match(r"([cq]\d+)", page)
            page = m.group(1) if m and f in ("Wiki/conflicts", "Wiki/questions") else page
            parts = re.split(r"(?m)^(## .*)$", text)
            for i in range(1, len(parts), 2):
                m = HEAD.match(parts[i])
                if not m:
                    continue
                doc = next((d for d in DOCS if d.startswith(m.group(1)) or m.group(1).startswith(d)), None)
                if doc:
                    pairs.add((page, doc))
                    for c in CITE.finditer(parts[i + 1]):
                        if c.group(1) == doc:
                            lines.add((page, doc, int(c.group(2))))
    return pairs, lines


def at_commit(commit):
    def read(folder):
        names = subprocess.run(["git", "-C", str(ROOT), "ls-tree", "--name-only", f"{commit}:{folder}"],
                               capture_output=True, text=True).stdout.split()
        for n in names:
            if n.endswith(".md"):
                yield n, subprocess.run(["git", "-C", str(ROOT), "show", f"{commit}:{folder}/{n}"],
                                        capture_output=True, text=True).stdout
    return read


def in_tree(root):
    def read(folder):
        for p in sorted((Path(root) / folder).glob("*.md")):
            yield p.name, p.read_text(encoding="utf-8")
    return read


def f1(a, b):
    tp = len(a & b)
    p = tp / len(a) if a else 0
    r = tp / len(b) if b else 0
    return tp, p, r, (2 * p * r / (p + r) if p + r else 0)


base_p, base_l = pairs_and_lines(at_commit("3d97d39"))
old_p, old_l = pairs_and_lines(at_commit("7f11861"))
new_p, new_l = pairs_and_lines(in_tree(sys.argv[1]))
old_p, old_l, new_p, new_l = old_p - base_p, old_l - base_l, new_p - base_p, new_l - base_l
tp, p, r, f = f1(new_p, old_p)
print(f"(page, document) pairs: pilot {len(new_p)}, committed {len(old_p)}, both {tp}; "
      f"precision {p:.2f} recall {r:.2f} F1 {f:.2f}  (bar: F1 >= 0.8)")
tp, p, r, f = f1(new_l, old_l)
print(f"cited lines: pilot {len(new_l)}, committed {len(old_l)}, both {tp}; F1 {f:.2f}")
print("only the pilot:", sorted(new_p - old_p))
print("only committed:", sorted(old_p - new_p))
