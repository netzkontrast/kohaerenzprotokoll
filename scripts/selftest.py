"""Prove the checkers can fail, with defects whose exact shape is asserted.

`quotes.py` and `fold()` are trusted by everything downstream, and **nobody has
ever seen either of them fail.** That is the same defect as the retired
pipeline's coverage term, which returned 1.0 whenever no gold fragments were
passed and was never passed any: two live runs scored 0.987 and 0.967 on a
number that could not fall for missing anything.

So each case here carries a *needle* — the exact defect the checker must name.
A case that fails for the wrong reason fails this test. Counting how many
problems were reported would pass while reporting the wrong ones.

The fixture cites a real landed document rather than a synthetic one, so the
whole resolution path runs: frontmatter, slug lookup, export unescaping,
emphasis stripping, blockquote wrapping and glued footnote numbers.

    python3 scripts/selftest.py
"""

from __future__ import annotations

import sys
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
import quotes  # noqa: E402
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
    failures = check_quotes() + check_fold()
    total = len(QUOTE_CASES) + len(MUST_NOT_MERGE) + len(MUST_MERGE)
    for line in failures:
        print(f"  FAIL  {line}")
    print(f"\n{total - len(failures)} of {total} cases hold "
          f"({len(QUOTE_CASES)} quotation, {len(MUST_NOT_MERGE) + len(MUST_MERGE)} fold)")
    if failures:
        print("\nA failure here means a checker other work depends on is not "
              "reporting what it claims to report.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
