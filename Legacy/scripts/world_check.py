#!/usr/bin/env python3
"""Scan the world axioms in Graph/ for pairs that look like they contradict.

    python3 scripts/world_check.py                 # every world
    python3 scripts/world_check.py --world kw1     # one world, by slug
    python3 scripts/world_check.py --json
    python3 scripts/world_check.py --strict        # exit 1 when a pair is flagged

The rule is decidable: two axioms of the same world are reported when exactly
one of them carries a negation and they share at least MIN_RARE_SHARED content
words that are *rare across the whole axiom corpus* (appearing in at most
MAX_MOTIF_FREQUENCY axioms). Rarity is what makes the signal usable — every
axiom mentions "Welt" and "AEGIS", so a shared common word means nothing,
while a shared "Vorher/Nachher" or "Steinbruch" means the two are talking
about the same narrow thing. It cannot know whether they truly conflict; it
narrows 111 axioms to the handful worth reading side by side.

Axiom text is German, so the negation markers and the stop-word list are
German first. The engine-era version of this check used English markers
(`not`, `never`, `no`) against the same German corpus and therefore never
fired; that is why the port is not a transcription.

A flagged pair is a question, never a verdict. Resolving one changes canon, so
it goes to the author through `/tetraframe` and a D-xx decision.
"""
from __future__ import annotations

import argparse
import json
import re
import sys
from collections import Counter
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(ROOT))

from tools import kpgraph  # noqa: E402  (needs ROOT on the path)

MIN_RARE_SHARED = 2
MAX_MOTIF_FREQUENCY = 3
MIN_WORD_LENGTH = 4
EXIT_OK, EXIT_FLAGGED, EXIT_CANNOT_RUN = 0, 1, 2

# German first, then English: a negation on exactly one side of a shared motif
# is what makes a pair worth reading.
NEGATIONS = {
    "nicht", "nie", "niemals", "kein", "keine", "keinen", "keiner", "keines",
    "ohne", "weder", "noch", "nichts", "unmöglich",
    "not", "never", "no", "cannot", "without", "none",
}

# Function words that would otherwise count as shared motifs.
STOPWORDS = {
    "aber", "auch", "auf", "aus", "bei", "beim", "dass", "dem", "den", "der",
    "des", "die", "dies", "diese", "diesem", "diesen", "dieser", "dieses",
    "durch", "ein", "eine", "einem", "einen", "einer", "eines", "für", "hat",
    "ist", "jede", "jedem", "jeden", "jeder", "jedes", "kann", "mehr", "mit",
    "muss", "nach", "nur", "oder", "sein", "seine", "sich", "sie", "sind",
    "über", "und", "vom", "von", "vor", "wenn", "werden", "wie", "wird",
    "wirst", "zum", "zur", "alle", "allen", "aller", "alles", "immer",
    "and", "are", "for", "from", "have", "that", "the", "their", "they",
    "this", "was", "were", "with", "which", "every", "always",
    # Connectives and framing words that carry no motif in this corpus.
    "sondern", "weil", "dabei", "damit", "denen", "deren", "gilt", "etwa",
    "statt", "roman", "realität", "bleibt", "wurde", "worden", "einzige",
}

WORD = re.compile(r"[\wÄÖÜäöüß]+", re.UNICODE)


def words(text: str) -> set[str]:
    """Lower-cased word tokens of `text`."""
    return {match.group(0).lower() for match in WORD.finditer(text or "")}


def motifs(tokens: set[str]) -> set[str]:
    """The content words a shared-motif count should consider."""
    return {w for w in tokens if len(w) >= MIN_WORD_LENGTH
            and w not in STOPWORDS and w not in NEGATIONS and not w.isdigit()}


def motif_frequency(axioms: list[dict]) -> Counter:
    """How many axioms each motif appears in, across the whole corpus."""
    counts: Counter = Counter()
    for axiom in axioms:
        counts.update(motifs(words(axiom.get("text", ""))))
    return counts


def candidate_pairs(axioms: list[dict], frequency: Counter) -> list[dict]:
    """Axiom pairs sharing rare motifs where exactly one side is negated."""
    prepared = [(a, motifs(words(a.get("text", ""))), bool(words(a.get("text", "")) & NEGATIONS))
                for a in axioms]
    found = []
    for index, (left, left_motifs, left_negated) in enumerate(prepared):
        for right, right_motifs, right_negated in prepared[index + 1:]:
            if not (left_negated ^ right_negated):
                continue
            shared = left_motifs & right_motifs
            rare = sorted(m for m in shared if frequency[m] <= MAX_MOTIF_FREQUENCY)
            if len(rare) >= MIN_RARE_SHARED:
                found.append({"a_id": left.get("id"), "b_id": right.get("id"),
                              "shared": rare,
                              "a_text": left.get("text", ""), "b_text": right.get("text", ""),
                              "a_severity": left.get("severity", ""),
                              "b_severity": right.get("severity", "")})
    return found


def report(root: Path, want: str = "") -> dict:
    """Per-world axiom counts and the flagged pairs."""
    graph = kpgraph.load(root)
    frequency = motif_frequency(graph.nodes("WorldAxiom"))
    worlds = graph.nodes("World")
    if want:
        worlds = [w for w in worlds if want.lower() in (w.get("slug", "") + w.get("name", "")).lower()]
    placed, out = set(), []
    for world in worlds:
        axioms = graph.axioms_of(world["_nid"])
        placed.update(a["_nid"] for a in axioms)
        out.append({"world": world.get("name", ""), "slug": world.get("slug", ""),
                    "axioms": len(axioms), "pairs": candidate_pairs(axioms, frequency)})
    orphans = [a for a in graph.nodes("WorldAxiom") if a["_nid"] not in placed] if not want else []
    return {"worlds": out, "orphan_axioms": len(orphans),
            "flagged": sum(len(w["pairs"]) for w in out)}


def render(data: dict) -> str:
    lines = []
    for world in data["worlds"]:
        lines.append(f"{world['world']}  ({world['axioms']} axioms, "
                     f"{len(world['pairs'])} pair(s) to read)")
        for pair in world["pairs"]:
            lines.append(f"  shared: {', '.join(pair['shared'])}")
            lines.append(f"    [{pair['a_severity']}] {pair['a_text'][:96]}")
            lines.append(f"    [{pair['b_severity']}] {pair['b_text'][:96]}")
    if data["orphan_axioms"]:
        lines.append(f"\n{data['orphan_axioms']} axiom(s) carry no world")
    lines.append(f"\n{data['flagged']} pair(s) flagged. A pair is a question, not a verdict: "
                 "resolving one changes canon, so it goes through /tetraframe and a D-xx.")
    return "\n".join(lines)


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__.split("\n\n")[0])
    parser.add_argument("--world", default="", help="limit to one world, matched on slug or name")
    parser.add_argument("--json", action="store_true", help="print the report as JSON")
    parser.add_argument("--strict", action="store_true", help="exit 1 when a pair is flagged")
    args = parser.parse_args(argv)
    if not (ROOT / "Graph").is_dir():
        print(f"no graph at {ROOT / 'Graph'}", file=sys.stderr)
        return EXIT_CANNOT_RUN
    data = report(ROOT, args.world)
    if not data["worlds"]:
        print(f"no world matches {args.world!r}", file=sys.stderr)
        return EXIT_CANNOT_RUN
    print(json.dumps(data, ensure_ascii=False, indent=2) if args.json else render(data))
    return EXIT_FLAGGED if args.strict and data["flagged"] else EXIT_OK


if __name__ == "__main__":
    sys.exit(main())
