#!/usr/bin/env python3
"""Lint the reading sections of wiki pages (standard library only).

A reading section is a `## Reading — `<slug>`…` heading (term, chapter and
overview pages) or a `## <date> — `<slug>`…` record entry, up to the next `## `.

    python3 scripts/lint_readings.py [--doc <slug> ...] [--strict]
    python3 scripts/lint_readings.py selftest

Classes (each printed as `file:line  CLASS  excerpt`):

  COMPARISON      warn-only (pipeline-optimization 3b): a sentence in the section
                  for document D holds a comparison phrase and its paragraph
                  cites no document other than D. A flag for a reviewer; whether
                  the comparison is true stays judgement.
  EMPTY_CODE      an empty code span (3e), the mark of shell damage.
  EMPTY_QUOTE     „ directly followed by “ or ”, or by " and then a closer with no
                  text (3e); `„"AEGIS…"` is a quotation opened with a straight
                  mark, not empty.
  STRAIGHT_QUOTE  a straight " between two „…" quotations on one line (3e); it
                  makes quotes.py read the span as one quotation.
  DOUBLE_SPACE    two spaces between two word characters in prose.
  JOIN            a quotation with […] whose citation is a range Lnn–Lmm.

Exit 0 always, except --strict with any flag other than COMPARISON (P1, P23: the
summary says how many sections it read, so a guard that read none is visible).
"""
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
DIRS = ["candidates", "chapters", "overview", "conflicts", "questions"]
WARN_ONLY = {"COMPARISON"}
CLASSES = ["COMPARISON", "EMPTY_CODE", "EMPTY_QUOTE", "STRAIGHT_QUOTE",
           "DOUBLE_SPACE", "JOIN"]

HEAD = re.compile(
    r"^## (?:Readings?\s*—|\d{4}-\d{2}-\d{2}\s*—)\s*`([^`]+)`")
# A straight " closes a quotation only when no curly closer follows before the
# next „ (otherwise it is inner: „a "b" c“).
QUOTE = re.compile(r'„(?:[^“”"]|"(?=[^„“”]*[“”]))*[“”"]')
QUOTE_CURLY = re.compile(r'„[^“”]*[“”]')  # only these define STRAIGHT_QUOTE's outside
EMPTY_Q = re.compile(r'„(?:[“”]|"[“”"])')
CITE = re.compile(r"\^\[([^\]:]+?)\.md:L")
RANGE_CITE = re.compile(r"\s*\^\[[^\]]*:L\d+\s*[–-]\s*L?\d+[^\]]*\]")
CODE = re.compile(r"`([^`]*)`")
ORD = "second|third|fourth|fifth|sixth"
COMPARE = re.compile(
    r"\bonly (?:one|source|document|read)\b|\bno other\b|\bevery other\b"
    r"|\ball other\b|\bthe first (?:read )?(?:source|document)\b|\bearliest\b"
    r"|\blatest\b|\bunlike\b|\bas in document \d+|\ba (?:%s) (?:position|title|source)\b"
    r"|\bevery read source\b"
    # found by the quality sample of 2026-09-29, both passed by the patterns above
    r"|\bevery (?:later|earlier|older|newer) (?:read )?sources?\b"
    r"|\bthe (?:oldest|newest|youngest) (?:read |whole-novel )?(?:source|document|plan)\b" % ORD, re.I)


def sections(lines):
    """Yield (slug, [(lineno, text)]) for each reading section."""
    cur = None
    for i, ln in enumerate(lines, 1):
        if ln.startswith("## "):
            if cur:
                yield cur
            m = HEAD.match(ln)
            cur = (m.group(1), [(i, ln)]) if m else None
        elif cur:
            cur[1].append((i, ln))
    if cur:
        yield cur


def same_doc(a, b):
    return a == b or a.startswith(b) or b.startswith(a)


def paragraphs(body):
    """Blocks of prose lines, split on blank lines; fences and headings out."""
    paras, cur, fence = [], [], False
    for i, ln in body:
        if ln.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence or ln.startswith("#"):
            continue
        if not ln.strip():
            if cur:
                paras.append(cur)
            cur = []
        else:
            cur.append((i, ln))
    if cur:
        paras.append(cur)
    return paras


def mask(text, rx):
    return rx.sub(lambda m: re.sub(r"[^\n]", "_", m.group(0)), text)


def lint_section(slug, body, path):
    out = []
    add = lambda ln, cls, txt: out.append((path, ln, cls, txt.strip()[:110]))
    for para in paragraphs(body):
        text = "\n".join(t for _, t in para)
        starts, pos = [], 0
        for i, t in para:
            starts.append((pos, i))
            pos += len(t) + 1

        def line_at(off):
            r = para[0][0]
            for p, i in starts:
                if p <= off:
                    r = i
            return r

        cites = set(CITE.findall(text))
        others = {c for c in cites if not same_doc(c, slug)}
        # COMPARISON
        if not others:
            masked = mask(text, QUOTE)
            prev = 0
            bounds = [m.end() for m in re.finditer(r"\. |\n", masked)] + [len(masked)]
            for b in bounds:
                sent = masked[prev:b]
                if COMPARE.search(sent) and not sent.lstrip().startswith("|"):
                    add(line_at(prev + (len(sent) - len(sent.lstrip()))),
                        "COMPARISON", text[prev:b].replace("\n", " "))
                prev = b
        # JOIN
        for m in QUOTE.finditer(text):
            if re.search(r"\[(?:…|\.\.\.)\]", m.group(0)) and \
                    RANGE_CITE.match(text, m.end()):
                add(line_at(m.start()), "JOIN", m.group(0))
        # EMPTY_QUOTE
        for m in EMPTY_Q.finditer(text):
            add(line_at(m.start()), "EMPTY_QUOTE", text[max(0, m.start() - 30):m.end() + 30])
    # per-line checks
    fence = False
    for i, ln in body:
        if ln.lstrip().startswith("```"):
            fence = not fence
            continue
        if fence or ln.startswith("#"):
            continue
        for m in CODE.finditer(ln):
            if not m.group(1).strip():
                add(i, "EMPTY_CODE", ln[max(0, m.start() - 30):m.end() + 30])
        # STRAIGHT_QUOTE: outside the quotations, between two of them
        spans = [m.span() for m in QUOTE_CURLY.finditer(ln)]
        for m in re.finditer(r'"', ln):
            if any(a <= m.start() < b for a, b in spans):
                continue
            if any(b <= m.start() for a, b in spans) and \
                    any(a >= m.start() for a, b in spans):
                add(i, "STRAIGHT_QUOTE", ln[max(0, m.start() - 30):m.start() + 30])
        # DOUBLE_SPACE (not tables, not leading indentation)
        if not ln.lstrip().startswith("|"):
            prose = mask(mask(ln, QUOTE), CODE)
            prose = re.sub(r"\^\[[^\]]*\]", lambda m: "_" * len(m.group(0)), prose)
            m = re.search(r"\w  +\w", prose)
            if m:
                add(i, "DOUBLE_SPACE", ln[max(0, m.start() - 20):m.end() + 20])
    return out


def lint_lines(lines, path, docs=None):
    flags, n = [], 0
    for slug, body in sections(lines):
        if docs and not any(same_doc(slug, d) for d in docs):
            continue
        n += 1
        flags += lint_section(slug, body, path)
    return flags, n


def files():
    for d in DIRS:
        yield from sorted((ROOT / "Wiki" / d).glob("*.md"))


def run(docs, strict):
    flags, n = [], 0
    for f in files():
        fl, k = lint_lines(f.read_text(encoding="utf-8").split("\n"),
                           str(f.relative_to(ROOT)), docs)
        flags += fl
        n += k
    flags.sort(key=lambda x: (x[0], x[1]))
    for p, i, cls, txt in flags:
        print(f"{p}:{i}  {cls}  {txt}")
    counts = {c: sum(1 for x in flags if x[2] == c) for c in CLASSES}
    print(f"\nlint_readings: {n} sections read; " +
          ", ".join(f"{c} {v}" for c, v in counts.items()))
    if n == 0:
        print("lint_readings: no section read — the guard saw nothing (P23)")
    bad = sum(v for c, v in counts.items() if c not in WARN_ONLY)
    return 1 if strict and bad else 0


def selftest():
    def sec(body, slug="doc-a"):
        return ["## Reading — `%s`, 2026-01-01" % slug, ""] + body.split("\n")

    def classes(body, slug="doc-a"):
        fl, _ = lint_lines(sec(body, slug), "t.md")
        return {c for _, _, c, _ in fl}

    cases = [
        ("COMPARISON flagged", "It is the only source that names it.", "COMPARISON", True),
        ("COMPARISON: every later source", "Unlike every later source, it fuses.", "COMPARISON", True),
        ("COMPARISON: the oldest read source", "The oldest read source is also the one.", "COMPARISON", True),
        ("COMPARISON cites another document", "It is the only source that names it. ^[doc-b.md:L3]", "COMPARISON", False),
        ("COMPARISON cites itself only", "The earliest use. ^[doc-a.md:L3]", "COMPARISON", True),
        ("COMPARISON inside a quotation", "Er sagt „the only source. unlike all“ ^[doc-a.md:L3]", "COMPARISON", False),
        ("COMPARISON no phrase", "It names the term once. ^[doc-a.md:L3]", "COMPARISON", False),
        ("EMPTY_CODE flagged", "The term `` stands here.", "EMPTY_CODE", True),
        ("EMPTY_CODE spaced flagged", "The term ` ` stands here.", "EMPTY_CODE", True),
        ("EMPTY_CODE two spans near miss", "See `a` `b` here.", "EMPTY_CODE", False),
        ("EMPTY_QUOTE flagged", "Er sagt „“ dort.", "EMPTY_QUOTE", True),
        ("EMPTY_QUOTE near miss", "Er sagt „x“ dort.", "EMPTY_QUOTE", False),
        ("EMPTY_QUOTE straight-open flagged", 'Er sagt „""  dort.'.replace("  "," "), "EMPTY_QUOTE", True),
        ("EMPTY_QUOTE straight-open with text near miss", 'Er sagt „"AEGIS is"" dort.', "EMPTY_QUOTE", False),
        ("DOUBLE_SPACE in straight-closed quotation near miss", 'Er sagt „H1 Virus   P=0.34" dort.', "DOUBLE_SPACE", False),
        ("STRAIGHT_QUOTE flagged", 'Erst „a“ dann "b" dann „c“ hier.', "STRAIGHT_QUOTE", True),
        ("STRAIGHT_QUOTE inside quotation near miss", 'Erst „a "b" c“ dann „d“.', "STRAIGHT_QUOTE", False),
        ("DOUBLE_SPACE flagged", "Two  spaces here.", "DOUBLE_SPACE", True),
        ("DOUBLE_SPACE in table near miss", "| a  b | c |", "DOUBLE_SPACE", False),
        ("DOUBLE_SPACE in quotation near miss", "Er sagt „a  b“ dort.", "DOUBLE_SPACE", False),
        ("JOIN flagged", "„erst […] dann“ ^[doc-a.md:L3–L5]", "JOIN", True),
        ("JOIN single line near miss", "„erst […] dann“ ^[doc-a.md:L3]", "JOIN", False),
        ("JOIN range without ellipsis near miss", "„erst dann“ ^[doc-a.md:L3–L5]", "JOIN", False),
    ]
    ok = 0
    for name, body, cls, want in cases:
        got = cls in classes(body)
        if got == want:
            ok += 1
        else:
            print(f"FAILED: {name} (wanted {want}, got {got})")
    # scope: a section for another heading shape is not read; --doc filters
    other = ["## Open", "", "Two  spaces."]
    fl, n = lint_lines(other, "t.md")
    total = len(cases) + 2
    ok += (n == 0 and not fl)
    if not (n == 0 and not fl):
        print("FAILED: non-reading section was read")
    fl, n = lint_lines(sec("Two  spaces."), "t.md", docs=["doc-z"])
    ok += (n == 0)
    if n != 0:
        print("FAILED: --doc filter did not skip")
    print(f"lint_readings: {ok} of {total} cases hold")
    return 0 if ok == total else 1


def main():
    if len(sys.argv) > 1 and sys.argv[1] == "selftest":
        sys.exit(selftest())
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    ap.add_argument("--doc", action="append", default=[])
    ap.add_argument("--strict", action="store_true")
    a = ap.parse_args()
    sys.exit(run(a.doc, a.strict))


if __name__ == "__main__":
    main()
