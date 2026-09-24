"""Prove the checkers can fail, with defects whose exact shape is asserted.

`quotes.py`, `read.py --find` and `fold()` are trusted by everything downstream,
and **nobody had ever seen any of them fail.** That is the same defect as the retired
pipeline's coverage term, which returned 1.0 whenever no gold fragments were
passed and was never passed any: two live runs scored 0.987 and 0.967 on a
number that could not fall for missing anything.

So each case here carries a *needle* — the exact defect the checker must name.
A case that fails for the wrong reason fails this test. Counting how many
problems were reported would pass while reporting the wrong ones.

The fixture cites a real landed document rather than a synthetic one, so the
whole resolution path runs: frontmatter, slug lookup, export unescaping,
emphasis stripping, blockquote wrapping and glued footnote numbers.

The citation cases run the same path backwards. A refusal asserts *which* line it
points at, because a refusal that shrugs is worth no more than a wrong number.

    python3 scripts/selftest.py
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import quotes  # noqa: E402
import read  # noqa: E402
from subject import document  # noqa: E402
from wiki_index import fold  # noqa: E402

DOC = "aegis-subplots-kapitelweise-system-exploration-docx"

# (needle, must_resolve, text). The needle is what a failure must be about.
QUOTE_CASES = [
    ("verbatim", True,
     '> „Die Natur eines Guardians - Autonomer Agent oder bloßes Werkzeug?\n'
     '> (Konfrontation)." ^[L272]'),
    ("declension", False,
     '> „Vorläufer von Juna/V" ^[L126]'),
    ("wrong-line", False,
     '> „agiert als spezialisierter Agent innerhalb eines größeren Systems" ^[L50]'),
    ("fabricated", False,
     '> „Jeder Guardian gehorcht AEGIS ohne Ausnahme." ^[L273]'),
    ("emphasis", True,
     '> „von *außerhalb* seiner kontrollierten Umgebung" ^[L420]'),
    ("wrapped", True,
     '> „Untersucht Kernwelt 1 (Logik/LogOS) als direkte Manifestation von\n'
     '> AEGIS\' Kernverarbeitungsstil" ^[L152]'),
]

# `read.py --find` is the other direction: given the words, produce the citation.
# (needle, words, the lines it must answer with, the line a refusal must name).
# A refusal is the half that matters, so each one asserts *which* line it points
# at — a refusal that shrugs is no better than a wrong number.
FIND_CASES = [
    ("locates", "Die Natur eines Guardians - Autonomer Agent oder bloßes Werkzeug?",
     [272], None),
    ("declension-refused", "Die Natur einer Guardians", [], 272),
    ("fabricated-refused", "Jeder Guardian gehorcht AEGIS ohne Ausnahme", [], None),
    ("number-refused", "Untersucht Kernwelt 3 (Logik/LogOS)", [], 152),
    # A quote ending in a number: the line dropped it and the quote kept it,
    # so this was refused as „95% in common" until the end counted as a boundary.
    ("number-at-end-locates", "Untersucht Kernwelt 1", [152], None),
]

# A number is part of the claim. The footnote rule drops a number after a word
# on both sides, so this read as the line's „Kernwelt 1" until numbers were
# compared on their own (2026-09-24: a chapter outline carries 268 such numbers
# and not one footnote). The failure must be about the number, not the words.
NUMBER_CASE = ('> „Untersucht Kernwelt 3 (Logik/LogOS) als direkte Manifestation von\n'
               '> AEGIS\' Kernverarbeitungsstil" ^[L152]')

# A quote crossing two lines cannot be cited at all, and must be told so rather
# than resolved against either half.
SPAN_CASE = ("die Illusion von Normalität (Implizite Kontrolle). "
             "Analyse des AEGIS-Fokus", (21, 22))

# fold() must NOT merge these. Each is a distinction the wiki rests on.
MUST_NOT_MERGE = [
    ("Negentropie", "Entropie"),        # the canary: opposites
    ("Guardian", "Guardians-Subroutine-Log"),
    ("Kern-Welt", "Kern-Programm"),
    ("Riss", "Rissbildung-Protokoll"),
]

# fold() must merge these. Each is a rule the ledger records.
MUST_MERGE = [
    ("Die Konstrukt-Stadt", "Konstrukt-Stadt"),   # the definite-article rule
    ("Der Möglichkeits-Garten", "Möglichkeits-Garten"),
    ("das Nexus", "Nexus"),
]


def check_quotes() -> list[str]:
    failures = []
    for needle, must_resolve, body in QUOTE_CASES:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "fixture.md"
            path.write_text(
                f"---\nsource: Sources/drive/{DOC}.md\n---\n\n{body}\n",
                encoding="utf-8")
            problems, skipped = quotes.check_file(path, DOC)
        resolved = not problems
        if skipped:
            failures.append(f"{needle}: the checker skipped it — it was not checked at all")
        elif resolved != must_resolve:
            failures.append(
                f"{needle}: expected {'resolve' if must_resolve else 'UNRESOLVED'}, "
                f"got {'resolve' if resolved else 'UNRESOLVED'}")
    with tempfile.TemporaryDirectory() as tmp:
        path = Path(tmp) / "fixture.md"
        path.write_text(f"---\nsource: Sources/drive/{DOC}.md\n---\n\n{NUMBER_CASE}\n",
                        encoding="utf-8")
        problems, _ = quotes.check_file(path, DOC)
    if not problems:
        failures.append("number: a wrong number resolved")
    elif "number 3" not in problems[0]["why"]:
        failures.append(f"number: unresolved for another reason — {problems[0]['why']}")
    return failures


def check_find() -> list[str]:
    doc = document(DOC)
    failures = []
    for needle, words, expect, nearest in FIND_CASES:
        hits = read.locate(doc, words)
        if hits != expect:
            failures.append(f"{needle}: expected {expect or 'no line'}, got {hits or 'no line'}")
            continue
        if nearest is not None:
            top = read.nearest(doc, words)
            if not top or top[0][1] != nearest:
                got = top[0][1] if top else "nothing"
                failures.append(f"{needle}: refused, but pointed at L{got} instead of L{nearest}")
    words, expect = SPAN_CASE
    if read.locate(doc, words):
        failures.append("spanning: resolved to a single line, which it does not fit on")
    elif expect not in read.spans(doc, words):
        failures.append(f"spanning: expected L{expect[0]}-{expect[1]}, got {read.spans(doc, words)}")
    return failures


def check_fold() -> list[str]:
    failures = []
    for a, b in MUST_NOT_MERGE:
        if fold(a) == fold(b):
            failures.append(f"fold() merged {a!r} and {b!r} — both fold to {fold(a)!r}")
    for a, b in MUST_MERGE:
        if fold(a) != fold(b):
            failures.append(f"fold() split {a!r} and {b!r} — {fold(a)!r} vs {fold(b)!r}")
    return failures


def main() -> int:
    failures = check_quotes() + check_find() + check_fold()
    total = (len(QUOTE_CASES) + 1 + len(FIND_CASES) + 1
             + len(MUST_NOT_MERGE) + len(MUST_MERGE))
    for line in failures:
        print(f"  FAIL  {line}")
    print(f"\n{total - len(failures)} of {total} cases hold "
          f"({len(QUOTE_CASES) + 1} quotation, {len(FIND_CASES) + 1} citation, "
          f"{len(MUST_NOT_MERGE) + len(MUST_MERGE)} fold)")
    if failures:
        print("\nA failure here means a checker other work depends on is not "
              "reporting what it claims to report.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
