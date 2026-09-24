"""Capture every artifact of an extraction run, not only the finished census.

A census is the *output* of six steps. Five of them used to run in a terminal and
vanish, which makes the process impossible to study: you cannot tell how a census
was arrived at, cannot compare a model against a person, and cannot see what a
probe would have caught.

One directory per document under Plan/runs/<slug>/:

    01-profile.txt     structural facts, deterministic
    02-probes.txt      export damage and surface families, deterministic
    03-candidates.md   written by hand WHILE READING, before any counting
    04-counts.txt      occurrences of everything in 03, derived
    05-verify.txt      every number that went into prose, re-checked

Step 03 is the one that matters most and the only one a program cannot produce.
It is the human baseline: what a reader proposed before a count could bias them.

Usage:
    python3 scripts/capture.py <slug>            # writes 01 and 02
    python3 scripts/capture.py <slug> --count    # reads 03, writes 04
"""

from __future__ import annotations

import collections
import json
import re
import subprocess
import sys
import unicodedata
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "Plan" / "runs"

sys.path.insert(0, str(Path(__file__).resolve().parent))
import subject  # noqa: E402
PROFILE = ROOT / "scripts" / "profile.py"
MANIFEST = ROOT / "Sources" / "manifest.jsonl"

INVISIBLE = {"\u200b", "\u200c", "\u200d", "\u2060", "\ufeff"}
TYPOGRAPHIC = "\u201e\u201c\u201d\u2018\u2019\u2013\u2014"
GLUED_REF = re.compile(r"([A-ZÄÖÜ][A-Za-zäöüß\-]{3,})\s(\d{1,2})\b")
ESCAPE = re.compile(r"\\([\[\]*\"_])")
WORD = re.compile(r"[A-ZÄÖÜ][A-Za-zäöüß]{3,}")
PROSE = re.compile(r"\*\*|`|\. |, ")


def candidate_terms(markdown: str) -> list[str]:
    """The `- term` lines, and only those.

    A candidates file also carries prose — an „open while reading" section whose
    bullets are sentences, not terms. Reading every `- ` line counted nine of
    those as candidates and reported them at 0 occurrences, which looks exactly
    like a term the document turned out not to contain.

    **There was a `len(term) <= 40` guard here and it removed real candidates.**
    `Bibliothek der Ungeschriebenen Geschichten` is 42 characters and a term.
    Measured over every candidate list in `Plan/runs/`: 28 `- ` lines exceed
    forty characters, **all 24 that are prose match `PROSE`, and all 4 that are
    terms match none of it.** The guard never removed anything `PROSE` had not
    already removed, and it was silently dropping the rest. Length is not the
    signal; punctuation is.
    """
    out = []
    for line in markdown.split("\n"):
        if not line.startswith("- "):
            continue
        term = line[2:].strip()
        if term and not PROSE.search(term):
            out.append(term)
    return out


def read_as_prose(markdown: str) -> list[str]:
    """The `- ` lines `candidate_terms` leaves out, so the count can name them.

    Punctuation is the signal and it is not a perfect one: a chapter title can
    carry a comma (`Tests, Allies, Enemies`) and a beat an abbreviating period
    (`Genesis 4. Beat`). Measured 2026-09-24 over every candidate list: 34 `- `
    lines match `PROSE`; the 24 in documents 5 and 6 are prose, and **10 are
    terms, in four lists** — `P vs. NP` twice, `Comp. Class`, `AI, general`,
    a formula, and document 14's three chapter titles and beat. All ten were
    left out of their counts with nothing saying so — the P23 shape, a guard
    reporting over a gap it cannot see. So whatever is left out is listed.
    """
    return [line[2:].strip() for line in markdown.split("\n")
            if line.startswith("- ") and line[2:].strip() and PROSE.search(line[2:].strip())]


def surfaces(term: str, text: str) -> list[tuple[str, int]]:
    """The inflected and compounded forms of this candidate the document holds.

    A candidate is proposed in the form a reader has in mind, which in German is
    usually the nominative singular — and the document then only ever uses it
    declined. `Kerndirektive` scored 0 as a word here because the document writes
    `Kerndirektiven`; so did `Guardian-Subroutine` and `Kernsystem`. Three of 53
    candidates looked absent and were not.

    `02-probes.txt` already groups the document's vocabulary into families by
    prefix. This does the same thing pointed the other way: given the candidate,
    show which surfaces of it are actually present, so a zero is readable as
    „written differently here" instead of „not in this document".
    """
    if len(term) < 4 or " " in term:
        return []
    found = collections.Counter(
        re.findall(rf"(?<![\w-]){re.escape(term)}[\w-]+", text, re.IGNORECASE))
    return sorted(((f, n) for f, n in found.items() if f.lower() != term.lower()),
                  key=lambda p: -p[1])[:4]


def count_both(term: str, text: str) -> tuple[int, int]:
    """Occurrences as a standalone word, and anywhere including inside compounds.

    One number cannot answer this in German. `Entropie` occurs 39 times alone and
    46 including `Entropiegewinn`, `Entropiemanagement`, `Entropiepotenzial` —
    and every one of those is a real mention of the concept. But `V` occurs 7
    times alone and 198 inside `Verhalten`, `Verbindung`, `Verteidigung`, and not
    one of those is a mention of anything.

    Counting with a plain substring reported 198, which is the exact trap
    `02-probes.txt` warns about two sections earlier with `Form < Information`.
    Counting only whole words would have lost the compounds. So both, always,
    and the reader sees the ratio.
    """
    escaped = re.escape(term)
    word = len(re.findall(rf"(?<![\w-]){escaped}(?![\w-])", text))
    return word, len(re.findall(escaped, text))


def drive_id_of(slug: str) -> str:
    """The manifest's id for a slug, copied. One was typed once and was invented."""
    for row in subject.rows():
        if row.get("slug") == slug:
            return row["drive_id"]
    sys.exit(f"no manifest row with slug {slug!r}")


def write_json(run: Path, slug: str, step: str, payload: dict, by: str) -> None:
    """One JSON object per step, with the five fields every object carries.

    The rest is free on purpose: no schema is fixed until enough documents exist
    to show what the fields need to be. Plan/runs/CONVENTIONS.md has the rules.
    """
    obj = {
        "document": slug,
        "drive_id": drive_id_of(slug),
        "step": step,
        "at": date.today().isoformat(),
        "by": by,
    }
    obj.update(payload)
    (run / f"{step}.json").write_text(json.dumps(obj, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")


def body_of(slug: str) -> tuple[Path, str, int]:
    """Path, body, and the file line the body starts on -- from `subject`.

    The offset is returned rather than assumed because citations count from line 1
    of the file while extraction skips the frontmatter. Reporting a body-local line
    number as a file line produces a citation that resolves to the wrong text --
    silently, since both are valid line numbers. That bug was live in this
    function once, which is why the boundary now has exactly one implementation.
    """
    try:
        doc = subject.document(slug)
    except KeyError as exc:
        sys.exit(str(exc))
    return doc.path, doc.body, doc.offset


def inflection_families(text: str, minimum: int = 2) -> list[tuple[str, list[str]]]:
    """Capitalised words sharing a 5-character stem, which an exact match splits."""
    stems: dict[str, set[str]] = {}
    for word in set(WORD.findall(text)):
        stems.setdefault(word[:5].lower(), set()).add(word)
    families = [(stem, sorted(words)) for stem, words in stems.items() if len(words) >= minimum]
    return sorted(families, key=lambda pair: (-len(pair[1]), pair[0]))


def substring_pairs(text: str, limit: int = 20) -> list[tuple[str, str]]:
    """Distinct capitalised words where one contains the other: never one term."""
    words = sorted(set(WORD.findall(text)), key=len)
    pairs = []
    for i, short in enumerate(words):
        for long in words[i + 1 :]:
            if short != long and short.lower() in long.lower():
                pairs.append((short, long))
                if len(pairs) >= limit:
                    return pairs
    return pairs


def probes(text: str) -> str:
    """Everything deterministic that has ever defeated an exact match here."""
    invisible = {c: text.count(c) for c in INVISIBLE if c in text}
    out = [
        "# export damage",
        f"  invisible characters   {', '.join(f'U+{ord(c):04X} x{n}' for c, n in invisible.items()) or 'none'}",
        f"  glued ref numbers      {len(GLUED_REF.findall(text))}",
        f"  backslash escapes      {len(ESCAPE.findall(text))}",
        f"  typographic marks      {sum(text.count(c) for c in TYPOGRAPHIC)}",
        f"  ascii quotes           {text.count(chr(34))}",
        "",
        "# inflection families -- one term, several surfaces",
    ]
    families = inflection_families(text)
    out += [f"  {stem:8} {', '.join(words)}" for stem, words in families[:25]] or ["  none"]
    out += ["", "# substring pairs -- never one term, often merged by accident"]
    pairs = substring_pairs(text)
    out += [f"  {short} < {long}" for short, long in pairs] or ["  none"]
    return "\n".join(out)


def capture(slug: str) -> Path:
    path, text, _ = body_of(slug)
    run = RUNS / slug
    run.mkdir(parents=True, exist_ok=True)
    profile = subprocess.run(
        [sys.executable, str(PROFILE), slug], capture_output=True, text=True, check=True
    ).stdout
    (run / "01-profile.txt").write_text(profile, encoding="utf-8")
    (run / "02-probes.txt").write_text(probes(text) + "\n", encoding="utf-8")
    invisible = {f"U+{ord(c):04X}": text.count(c) for c in INVISIBLE if c in text}
    write_json(run, slug, "probes", {
        "invisible_characters": invisible,
        "glued_ref_numbers": len(GLUED_REF.findall(text)),
        "backslash_escapes": len(ESCAPE.findall(text)),
        "typographic_marks": sum(text.count(c) for c in TYPOGRAPHIC),
        "ascii_quotes": text.count(chr(34)),
        "inflection_families": {stem: words for stem, words in inflection_families(text)[:25]},
        "substring_pairs": [list(pair) for pair in substring_pairs(text)],
    }, by="scripts/capture.py")
    if not (run / "03-candidates.md").exists():
        (run / "03-candidates.md").write_text(
            f"# Candidates — {slug}\n\n"
            "Written by hand while reading, **before any counting**. One line per\n"
            "candidate, nothing else. This is the only artifact of the run a program\n"
            "cannot produce, and the baseline any model gets scored against.\n\n",
            encoding="utf-8",
        )
    return run


def count(slug: str) -> Path:
    path, text, offset = body_of(slug)
    run = RUNS / slug
    candidates_file = run / "03-candidates.md"
    if not candidates_file.exists():
        sys.exit(f"write {candidates_file} first -- counting before proposing decides what gets seen")
    terms = candidate_terms(candidates_file.read_text(encoding="utf-8"))
    if not terms:
        sys.exit(f"{candidates_file} has no `- term` lines yet")
    prose = read_as_prose(candidates_file.read_text(encoding="utf-8"))
    if prose:
        print(f"{len(prose)} `- ` line(s) read as prose, not counted: " + " · ".join(prose))
    lines = text.split("\n")
    out = [
        f"# counts for {len(terms)} candidates",
        f"# line numbers are FILE lines, as a citation writes them",
    ]
    if prose:
        out.append(f"# {len(prose)} `- ` line(s) read as prose and not counted: " + " · ".join(prose))
    out += [
        "",
    ]
    out.append("#   word = the term standing alone; in = anywhere, compounds included")
    out.append("")
    for term in terms:
        hits = [i + offset for i, line in enumerate(lines) if term in line]
        word, inside = count_both(term, text)
        flag = "  <-- substring" if inside > 2 * max(word, 1) else ""
        out.append(f"  {term:30} {word:4} word {inside:5} in   {hits[:6]}{flag}")
        for form, n in surfaces(term, text):
            out.append(f"  {'':30} {n:4}      as {form}")
    (run / "04-counts.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
    reconstructed = "Reconstructed, not original" in candidates_file.read_text(encoding="utf-8")
    write_json(run, slug, "counts", {
        "candidate_source": "reconstructed-from-census" if reconstructed else "written-while-reading",
        "usable_as_baseline": not reconstructed,
        "line_base": "file, from line 1, as a citation writes it",
        "read_as_prose": prose,
        "counts": {
            term: {
                "n": count_both(term, text)[0],
                "n_including_compounds": count_both(term, text)[1],
                "lines": [i + offset for i, line in enumerate(lines) if term in line],
            }
            for term in terms
        },
    }, by="scripts/capture.py")
    return run


def main(argv: list[str]) -> int:
    if not argv:
        sys.exit(__doc__)
    slug = argv[0]
    if "--count" in argv:
        print(f"wrote {count(slug) / '04-counts.txt'}")
        return 0
    run = capture(slug)
    print(f"captured {run}/01-profile.txt and 02-probes.txt")
    print(f"next: write {run}/03-candidates.md by hand, then --count")
    return 0


if __name__ == "__main__":
    try:
        import signal

        signal.signal(signal.SIGPIPE, signal.SIG_DFL)
    except (ImportError, AttributeError, ValueError):
        pass
    raise SystemExit(main(sys.argv[1:]))
