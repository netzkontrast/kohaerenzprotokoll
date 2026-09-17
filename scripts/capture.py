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
    run.md             timings, and what is missing

Step 03 is the one that matters most and the only one a program cannot produce.
It is the human baseline: what a reader proposed before a count could bias them.

Usage:
    python3 scripts/capture.py <slug>            # writes 01 and 02, and run.md
    python3 scripts/capture.py <slug> --count    # reads 03, writes 04
"""

from __future__ import annotations

import json
import re
import subprocess
import sys
import unicodedata
from datetime import date
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RUNS = ROOT / "Plan" / "runs"
PROFILE = ROOT / "scripts" / "profile.py"
MANIFEST = ROOT / "Sources" / "manifest.jsonl"

INVISIBLE = {"\u200b", "\u200c", "\u200d", "\u2060", "\ufeff"}
TYPOGRAPHIC = "\u201e\u201c\u201d\u2018\u2019\u2013\u2014"
GLUED_REF = re.compile(r"([A-ZÄÖÜ][A-Za-zäöüß\-]{3,})\s(\d{1,2})\b")
ESCAPE = re.compile(r"\\([\[\]*\"_])")
WORD = re.compile(r"[A-ZÄÖÜ][A-Za-zäöüß]{3,}")


def drive_id_of(slug: str) -> str:
    """The manifest's id for a slug, copied. One was typed once and was invented."""
    for line in MANIFEST.read_text(encoding="utf-8").splitlines():
        row = json.loads(line)
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
    """Return the path, the body text, and the file line the body starts on.

    The offset is returned rather than assumed because citations count from line
    1 of the file while extraction skips the frontmatter. Reporting a body-local
    line number as if it were a file line produces a citation that resolves to
    the wrong text -- silently, since both are valid line numbers.
    """
    path = ROOT / "Sources" / "drive" / f"{slug}.md"
    if not path.exists():
        sys.exit(f"no landed document with slug {slug!r}")
    lines = path.read_text(encoding="utf-8").split("\n")
    marks = [i for i, line in enumerate(lines) if line.strip() == "---"]
    start = marks[1] + 1 if len(marks) >= 2 and marks[0] == 0 else 0
    return path, "\n".join(lines[start:]), start + 1


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
    terms = [
        line.strip("- ").strip()
        for line in candidates_file.read_text(encoding="utf-8").split("\n")
        if line.startswith("- ")
    ]
    if not terms:
        sys.exit(f"{candidates_file} has no `- term` lines yet")
    lines = text.split("\n")
    out = [
        f"# counts for {len(terms)} candidates",
        f"# line numbers are FILE lines, as a citation writes them",
        "",
    ]
    for term in terms:
        hits = [i + offset for i, line in enumerate(lines) if term in line]
        out.append(f"  {term:34} {len(re.findall(re.escape(term), text)):4}  {hits[:8]}")
    (run / "04-counts.txt").write_text("\n".join(out) + "\n", encoding="utf-8")
    reconstructed = "Reconstructed, not original" in candidates_file.read_text(encoding="utf-8")
    write_json(run, slug, "counts", {
        "candidate_source": "reconstructed-from-census" if reconstructed else "written-while-reading",
        "usable_as_baseline": not reconstructed,
        "line_base": "file, from line 1, as a citation writes it",
        "counts": {
            term: {
                "n": len(re.findall(re.escape(term), text)),
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
