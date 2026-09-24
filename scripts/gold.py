"""Which candidate lists are gold — decided by rule, the same way every time.

A gold list is the baseline an automated extraction is scored against, so what
counts as one cannot be a feeling or a word in a header. Until 2026-09-24 it was
both: `state.py` looked for the word "reader" in a `written_by:` line, and
`trainset.py`, `entities.py` and `capture.py` each looked for "reconstruct" in
their own way. The author then said that the gold lists are this session's to
decide, provided the decision is repeatable (decision 009). This is that
decision, as code, and the one place every script asks.

A list at `Plan/runs/<slug>/03-candidates.md` is gold when all five hold:

| criterion | what it checks | why |
|---|---|---|
| `a list` | at least one `- term` line, read by `capture.candidate_terms` | nothing else is a candidate |
| `not reconstructed` | it does not carry the declaration every reconstruction carries | a list rebuilt from a finished census already reflects counting and judgement |
| `counted` | `counts.json` exists; `capture.py --count` refuses to run before a list does | the count proves the list existed before the counts did |
| `frozen since the count` | its terms are exactly the terms `counts.json` recorded | a term added or dropped after counting was decided with the counts in view |
| `of the document` | at least `IN_DOCUMENT` of its terms occur in the document | the bar `rlm_ingest.judge` sets for a model's list, so both are held to one bar |

**Who wrote it does not decide it.** A person or a session reading the document
writes the same kind of artifact, and every criterion above is about the
artifact. The `written_by:` line is kept verbatim in the verdict, so a score can
say which kind of reader its gold came from — which matters because gold is one
reading, and two readings of one document agreed at F1 0.66 (P27).

Deliberately not criteria, each measured on the thirteen lists before it was
left out: how far the terms' first occurrences reach into the document (the
gazetteer, a full reading, introduces its names early and reaches only half its
tenths), and whether the list follows the document's order (document 5, a
reader's list, correlates no better than two reconstructions).

    python3 scripts/gold.py              # every list: gold or not, and which criterion failed
    python3 scripts/gold.py <slug>       # one list, every criterion with its evidence
    python3 scripts/gold.py --json       # the same, for code
    python3 scripts/gold.py selftest     # each criterion handed a list that must fail it
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "Plan" / "runs"
sys.path.insert(0, str(ROOT / "scripts"))

# RECONSTRUCTED is the declaration every reconstructed list carries; capture.py
# owns it, because it also writes it into counts.json as `candidate_source`.
from capture import RECONSTRUCTED, body_of, candidate_terms, count_both  # noqa: E402
# Share of a list's terms that must occur in the document for the list to be a
# reading of it. rlm_ingest.judge holds a model's list to the same bar.
IN_DOCUMENT = 0.9
CRITERIA = ("a list", "not reconstructed", "counted", "frozen since the count", "of the document")


def decide(list_text: str, counted: set[str] | None, document_text: str) -> dict:
    """The verdict on one list, from its text, the terms its count recorded (None when
    it was never counted) and the document's text. Pure: the same inputs, the same answer."""
    terms = candidate_terms(list_text)
    present = [t for t in terms if count_both(t, document_text)[1] > 0]
    share = round(len(present) / len(terms), 3) if terms else 0.0
    checks = {
        "a list": bool(terms),
        "not reconstructed": RECONSTRUCTED not in list_text,
        "counted": counted is not None,
        "frozen since the count": counted is not None and set(terms) == counted,
        "of the document": bool(terms) and share >= IN_DOCUMENT,
    }
    written_by = next((line.split(":", 1)[1].strip() for line in list_text.splitlines()[:6]
                       if line.startswith("written_by:")), None)
    return {
        "gold": all(checks.values()),
        "failed": [name for name in CRITERIA if not checks[name]],
        "terms": len(terms),
        "in_document": share,
        "added_after_count": sorted(set(terms) - counted) if counted is not None else [],
        "dropped_after_count": sorted(counted - set(terms)) if counted is not None else [],
        "written_by": written_by,
    }


def verdict(slug: str) -> dict:
    """The verdict on one document's list, read from `Plan/runs/<slug>/`."""
    run = RUNS / slug
    listing = run / "03-candidates.md"
    if not listing.exists():
        return {"slug": slug, "gold": False, "failed": ["a list"], "terms": 0, "in_document": 0.0,
                "added_after_count": [], "dropped_after_count": [], "written_by": None}
    counts = run / "counts.json"
    counted = set(json.loads(counts.read_text(encoding="utf-8"))["counts"]) if counts.exists() else None
    text, _ = body_of(slug)
    return {"slug": slug, **decide(listing.read_text(encoding="utf-8"), counted, text)}


def verdicts() -> list[dict]:
    """Every document that has a candidate list, in slug order."""
    return [verdict(p.parent.name) for p in sorted(RUNS.glob("*/03-candidates.md"))]


def gold_slugs() -> list[str]:
    return [v["slug"] for v in verdicts() if v["gold"]]


def refusal(slug: str) -> str | None:
    """None when the list is gold, else one line saying why it may not serve as gold."""
    v = verdict(slug)
    return None if v["gold"] else f"{slug}'s list is not gold: fails {', '.join(v['failed'])} (scripts/gold.py)"


def selftest() -> tuple[int, list[str]]:
    """(cases run, failures). Each criterion is handed a list built to fail it."""
    document = "Die Kern-Welt und der Riss. Kael sieht AEGIS. Der Nexus bricht. Juna schweigt.\n"
    good = "written_by: a reader, while reading\n\n- Kern-Welt\n- Riss\n- Kael\n- AEGIS\n- Nexus\n- Juna\n"
    terms = {"Kern-Welt", "Riss", "Kael", "AEGIS", "Nexus", "Juna"}
    cases = [
        ("a good list is gold", decide(good, terms, document), []),
        # an empty list must not pass "of the document" vacuously: 0 of 0 is not 100%
        ("prose is not a list, and no list is of the document",
         decide("Only prose here, no candidates.\n", set(), document), ["a list", "of the document"]),
        ("a declared reconstruction", decide(f"> **{RECONSTRUCTED}.**\n\n" + good, terms, document),
         ["not reconstructed"]),
        ("never counted", decide(good, None, document), ["counted", "frozen since the count"]),
        ("a term added after the count", decide(good + "- Überraum\n", terms, document),
         ["frozen since the count", "of the document"]),
        ("a term dropped after the count", decide(good.replace("- Juna\n", ""), terms, document),
         ["frozen since the count"]),
        ("a list about another document", decide(good, terms, "Ein ganz anderer Text ohne diese Namen.\n"),
         ["of the document"]),
        ("denying a reconstruction is not declaring one",
         decide("This is not a reconstruction.\n\n" + good, terms, document), []),
    ]
    ran, failures = 0, []
    for name, got, expected_failures in cases:
        ran += 1
        if got["failed"] != expected_failures:
            failures.append(f"{name}: expected {expected_failures or 'gold'}, got {got['failed'] or 'gold'}")
    ran += 1
    if decide(good, terms, document)["written_by"] != "a reader, while reading":
        failures.append("written_by was not kept verbatim")
    return ran, failures


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        ran, failures = selftest()
        for failure in failures:
            print(f"  FAIL  {failure}")
        print(f"gold: {ran - len(failures)} of {ran} cases hold "
              "(every criterion failed on purpose, a denial read as no declaration, the reader kept)")
        return 1 if failures else 0
    if argv[:1] == ["--json"]:
        print(json.dumps(verdicts(), ensure_ascii=False, indent=2))
        return 0
    if argv:
        v = verdict(argv[0])
        for key, value in v.items():
            print(f"  {key:20} {value}")
        return 0
    rows = verdicts()
    for v in rows:
        mark = "GOLD" if v["gold"] else "no  "
        why = "" if v["gold"] else f"  fails {', '.join(v['failed'])}"
        print(f"  {mark}  {v['slug']:60} {v['terms']:4} terms, {v['in_document']:.0%} in the document{why}")
    print(f"\n{sum(v['gold'] for v in rows)} of {len(rows)} candidate lists are gold "
          f"(criteria: {', '.join(CRITERIA)})")
    return 0


if __name__ == "__main__":
    raise SystemExit(main(sys.argv[1:]))
