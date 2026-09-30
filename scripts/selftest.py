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
import wiki_index  # noqa: E402
import account  # noqa: E402

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

# (name, text, (unresolved, uncited, checked)). Until 2026-09-26 a quotation under
# eight characters matched nothing: a cited „(Ch13)" on a line without it passed.
SHORT_CASES = [
    ("cited, wrong", '„Zauber" ^[L272]', (1, 0, 1)),
    ("uncited", 'Er nennt es „offen" und geht.', (0, 0, 0)),
    ("beside a full one", '„Autonomer Agent oder bloßes Werkzeug" und „Chaos" ^[L272]', (0, 0, 1)),
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

# Count marks: `^[slug.md:#N]` after a code span or „…". Counts verified with grep
# on this document: `Zauber` 0 in any case, `Guardian` 22 whole words and
# `guardian` 0 whole words but 22 case-insensitive.
# (name, text, needle the verdict must hold or None for a mark that must pass).
COUNT_CASES = [
    ("correct zero", "`Zauber` ^[%s.md:#0]" % DOC, None),
    ("correct count", "„Guardian" + "\u201c ^[%s.md:#22]" % DOC, None),
    ("wrong count", "`Guardian` ^[%s.md:#0]" % DOC, "the count is 22, not 0"),
    ("zero only by case", "`guardian` ^[%s.md:#0]" % DOC, "zero only by case: 22"),
    # found by a document-reader, 2026-09-29: a wrap between the words and the mark
    ("mark on the next line", "`Guardian`\n^[%s.md:#22]" % DOC, None),
    ("a mark with no words before it", "Counted: ^[%s.md:#22]" % DOC, "no code span or quotation"),
    # found by a document-reader, 2026-09-30: the export writes `K\_1`, `read.py --count`
    # counts it as written (8), and the check stripped the escape and counted `K_1` (0)
    ("an escaped export form, counted as written",
     "`K\\_1` ^[technical-audit-research-mandate-the-kohaerenz-protokoll-fra.md:#8]", None),
]


def check_counts() -> list[str]:
    failures = []
    for name, body, needle in COUNT_CASES:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "fixture.md"
            path.write_text(f"---\nsource: Sources/drive/{DOC}.md\n---\n\n{body}\n",
                            encoding="utf-8")
            result = quotes.tally([path])
        if result["count_marks"] != 1:
            failures.append(f"count {name}: {result['count_marks']} marks seen, expected 1")
        elif result["checked"] or result["unchecked"]:
            failures.append(f"count {name}: the mark was counted as a quotation citation")
        elif needle is None and result["unresolved"]:
            failures.append(f"count {name}: a correct mark was reported: {result['problems'][0][1]['why']}")
        elif needle is not None and (result["count_wrong"] != 1
                                     or needle not in result["problems"][0][1]["why"]):
            failures.append(f"count {name}: expected a defect naming {needle!r}, "
                            f"got {[p[1]['why'] for p in result['problems']]}")
    # read.py --count asks the same function a census counts with.
    import capture
    for words in ("Guardian", "Untersucht Kernwelt 1", "Kernwelt"):
        want = capture.count_both(words, document(DOC).body)
        got = quotes.count_words(DOC, words)
        if (got[0], got[2]) != want:
            failures.append(f"read --count {words!r}: {(got[0], got[2])} != capture {want}")
    import io
    from contextlib import redirect_stdout
    out = io.StringIO()
    with redirect_stdout(out):
        read.main([DOC, "--count", "Guardian"])
    if f"`Guardian` ^[{DOC}.md:#22]" not in out.getvalue():
        failures.append("read --count: no ready-to-paste mark with the case-sensitive count")
    return failures


# fold() must NOT merge these. Each is a distinction the wiki rests on, and
# scripts/pairs.py asks every rule and every model the same pairs as a veto.
MUST_NOT_MERGE = [
    ("Negentropie", "Entropie"),        # the canary: opposites
    ("Guardian", "Guardians-Subroutine-Log"),
    ("Kern-Welt", "Kern-Programm"),
    ("Riss", "Rissbildung-Protokoll"),
    # Two words the corpus uses, each within one step of the plural rule's reach
    # (decision 010): -er makes a player of a game, and case-blind -s would put
    # a visual logo on the Guardian page fold() spells `logos`.
    ("Spiel", "Spieler"),
    ("Logo", "LogOS"),
    # Storyform notation: a throughline, not the protocol its letters spell (J87).
    ("A:RS", "ARS"),
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
    for info, counted in (("qmd", 0), ("text", 1)):
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "fixture.md"
            path.write_text(f"---\nsource: Sources/drive/{DOC}.md\n---\n\n```{info}\n"
                            "L12  Er sagte „ein Satz ohne jede Quelle hier“ und ging.\n```\n",
                            encoding="utf-8")
            problems, skipped = quotes.check_file(path, DOC)
            total = quotes.tally([path])
        if problems or skipped != counted or total["checked"] != 0:
            failures.append(f"raw fence ```{info}: {skipped} uncited and {total['checked']} checked counted, "
                            f"expected {counted} and 0")
    # Short quotations (quotes.SHORT). A cited one is a claim about a line and is
    # checked; an uncited one is a word the prose mentions and is not counted; and
    # beside a full quotation on the line, a short one does not take its reference.
    for name, body, want in SHORT_CASES:
        with tempfile.TemporaryDirectory() as tmp:
            path = Path(tmp) / "fixture.md"
            path.write_text(f"---\nsource: Sources/drive/{DOC}.md\n---\n\n{body}\n",
                            encoding="utf-8")
            problems, skipped = quotes.check_file(path, DOC)
            total = quotes.tally([path])
        got = (len(problems), skipped, total["checked"])
        if got != want:
            failures.append(f"short {name}: (unresolved, uncited, checked) = {got}, expected {want}")
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


def _page(ingested, sources, readings, body) -> str:
    items = ", ".join(f'"{s}"' for s in ingested)
    return (f"---\nterm: T\nstatus: candidate\nsources: {sources}\nreadings: {readings}\n"
            f"ingested: [{items}]\n---\n\n# T\n\n{body}\n")


def check_frontmatter() -> list[str]:
    """Decision 015 / plan 3c: `ingested:` is every read document a page cites."""
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        tmp = Path(tmp)
        pages, terms = tmp / "pages", tmp / "terms"
        pages.mkdir()
        terms.mkdir()
        for slug in ("doc-a", "doc-b"):
            (terms / f"{slug}.md").write_text("census\n", encoding="utf-8")
        # doc-b is cited in a difference line only; doc-scan has no census.
        (pages / "drift.md").write_text(_page(
            ["doc-a"], 1, 1,
            "## Reading — `doc-a`\n\n> „x\" ^[doc-a.md:L1]\n\n"
            "## Where the sources differ\n\nB says otherwise ^[doc-b.md:L2] "
            "and a scan ^[doc-scan.md:L3]."), encoding="utf-8")
        (pages / "right.md").write_text(_page(
            ["doc-a", "doc-b"], 2, 2,
            "## Reading — `doc-a`\n\n^[doc-a.md:L1]\n\n## Reading — `doc-b`\n\n^[doc-b.md:L2]"
            " and a scan ^[doc-scan.md:L3]."), encoding="utf-8")
        drifts, older = wiki_index.frontmatter_drift(pages, terms)
        names = [d["page"] for d in drifts]
        if names != ["drift"]:
            failures.append(f"frontmatter: expected only `drift` reported, got {names}")
        elif drifts[0]["want"]["ingested"] != ["doc-a", "doc-b"] or drifts[0]["want"]["sources"] != 2:
            failures.append(f"frontmatter: wrong derivation {drifts[0]['want']}")
        wiki_index.fix_frontmatter(pages, terms)
        if wiki_index.frontmatter_drift(pages, terms)[0]:
            failures.append("frontmatter: still drifting after the fix")
        fixed = (pages / "drift.md").read_text(encoding="utf-8")
        if "# T" not in fixed or "doc-scan" in fixed.split("---")[1]:
            failures.append("frontmatter: the fix touched more than the three fields")
    return failures


def check_order() -> list[str]:
    """Plan 3d: a reconcile.json with no census or note beside it fails `order`."""
    failures = []
    with tempfile.TemporaryDirectory() as tmp:
        root = Path(tmp)
        (root / "Sources" / "terms").mkdir(parents=True)
        (root / "Sources" / "notes").mkdir(parents=True)
        run = root / "Plan" / "runs" / "doc-x"
        run.mkdir(parents=True)
        (run / "reconcile.json").write_text("{}", encoding="utf-8")
        result = account.account_order(root)
        kinds = {v["kind"] for v in result["violations"]}
        if result["holds"] or kinds != {"reconciled-without-census", "reconciled-without-note"}:
            failures.append(f"order: reconcile.json without census/note gave {result['holds']}, {kinds}")
    return failures


def main() -> int:
    failures = check_quotes() + check_find() + check_fold() + check_counts() + check_frontmatter() + check_order()
    counting = len(COUNT_CASES) + 3 + 1   # the marks, read --count against capture, the pasted mark
    total = (len(QUOTE_CASES) + 3 + len(SHORT_CASES) + len(FIND_CASES) + 1
             + len(MUST_NOT_MERGE) + len(MUST_MERGE) + 5 + counting)
    for line in failures:
        print(f"  FAIL  {line}")
    print(f"\n{total - len(failures)} of {total} cases hold "
          f"({len(QUOTE_CASES) + 3 + len(SHORT_CASES)} quotation, {len(FIND_CASES) + 1} citation, "
          f"{len(MUST_NOT_MERGE) + len(MUST_MERGE)} fold, {counting} counting, 5 frontmatter and order)")
    if failures:
        print("\nA failure here means a checker other work depends on is not "
              "reporting what it claims to report.")
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
