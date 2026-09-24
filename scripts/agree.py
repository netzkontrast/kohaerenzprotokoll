"""Two candidate lists of one document, compared the way P27 says to compare them.

A candidate list is one reading, not the truth, so a score against it measures
agreement with one reader. This prints that agreement — and separates the two
things one F1 number mixes together:

- **how much each reader lists.** A reader told „exhaustively" lists five to
  fourteen times what a selective one does. F1 then falls however well both
  read, because the extra candidates count against the shorter list.
  `contained` answers the asymmetric question instead: how much of list A does
  list B hold?
- **how each reader cuts a surface.** `Juna` in one list and `Juna/V` in the
  other, `DKT` against `DKT-Physik`: the same passage, read the same way,
  written down at two lengths. `fold()` does not match them, rightly — it is
  not a stemmer. Such a term is counted `inside a longer surface`, never shared,
  and listed by name so it can be looked at.

Measured on 2026-09-24 (`Plan/learnings/extract-terms.md`): two blind
re-readings per document for four documents agreed with each other at F1
0.82–0.93 and held 82–95 % of the committed list (97–100 % counting a
longer surface), while scoring 0.11–0.52 against it.

    python3 scripts/agree.py <slug>                    # every list in Plan/runs/<slug>/, pairwise
    python3 scripts/agree.py <slug> <a.md> <b.md>      # two lists, by path
    python3 scripts/agree.py <slug> ... --names        # and the difference lists by name
    python3 scripts/agree.py selftest

A list is any `03-candidates*.md`: its `- term` lines, read by
`capture.candidate_terms`, with a trailing `^[Lnn]` dropped. Surfaces meet by
`fold()`. A term the document does not contain word for word is counted, by the
question `entities.first_line` asks, because a list that normalises
(`Kern-Welt` where the text has only `Kern-Welten`) is reporting a form the
reader chose rather than one it read.

What it does not do: decide which list is right. A miss is not automatically an
error and an extra is not automatically noise — that stays a reader's call.
Prints only; writes nothing.
"""

from __future__ import annotations

import itertools
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))
from capture import candidate_terms  # noqa: E402
from wiki_index import fold  # noqa: E402

RUNS = ROOT / "Plan" / "runs"
CITE = re.compile(r"\s*\^\[[^\]]*\]\s*$")
SHORTEST_INSIDE = 3          # `V`, `MI`: inside half the corpus, so never counted as inside


def terms_of(markdown: str) -> list[str]:
    """A list file's candidates, each without its trailing citation."""
    return [CITE.sub("", t).strip() for t in candidate_terms(markdown) if CITE.sub("", t).strip()]


def keyed(terms: list[str]) -> dict[str, str]:
    """fold key -> the first surface that produced it."""
    out: dict[str, str] = {}
    for t in terms:
        key = fold(t)
        if key:
            out.setdefault(key, t)
    return out


def compare(a: list[str], b: list[str]) -> dict:
    """Everything the report prints about two lists, as numbers and names."""
    ka, kb = keyed(a), keyed(b)
    shared = ka.keys() & kb.keys()
    only_a = sorted(ka.keys() - shared)
    only_b = sorted(kb.keys() - shared)

    def inside(keys, other):
        pairs = []
        for k in keys:
            if len(k) < SHORTEST_INSIDE:
                continue
            hit = next((o for o in sorted(other, key=len) if k != o and k in o), None)
            if hit:
                pairs.append((k, hit))
        return pairs

    in_b = inside(only_a, kb.keys())
    in_a = inside(only_b, ka.keys())
    p = len(shared) / len(kb) if kb else 0.0
    r = len(shared) / len(ka) if ka else 0.0
    return {
        "a": len(ka), "b": len(kb), "shared": len(shared),
        "f1": 2 * p * r / (p + r) if p + r else 0.0,
        "a_in_b": len(shared) / len(ka) if ka else 0.0,     # contained: how much of A does B hold
        "b_in_a": len(shared) / len(kb) if kb else 0.0,
        "only_a": [ka[k] for k in only_a], "only_b": [kb[k] for k in only_b],
        "only_a_inside_b": [(ka[k], kb[o]) for k, o in in_b],
        "only_b_inside_a": [(kb[k], ka[o]) for k, o in in_a],
    }


def absent(doc, terms: list[str]) -> list[str]:
    """Surfaces the document does not contain word for word, on one line."""
    from entities import first_line
    return [t for t in dict.fromkeys(terms) if first_line(doc, t) is None]


def report(slug: str, paths: list[Path], names: bool) -> int:
    import subject
    doc = subject.document(slug)
    lines = len(doc.path.read_text(encoding="utf-8").splitlines())
    lists = {p.stem.removeprefix("03-candidates").lstrip("-") or "committed":
             terms_of(p.read_text(encoding="utf-8")) for p in paths}
    print(f"{slug} — {lines} file lines\n")
    for name, terms in lists.items():
        k = keyed(terms)
        gone = absent(doc, terms)
        print(f"  {name:<12} {len(k):5} candidates  {100 * len(k) / lines:6.1f} per 100 lines"
              f"  {len(gone):3} not in the document word for word")
        if names and gone:
            print("               " + " · ".join(gone))
    print()
    for (na, a), (nb, b) in itertools.combinations(lists.items(), 2):
        c = compare(a, b)
        print(f"  {na} ~ {nb}: F1 {c['f1']:.2f}  shared {c['shared']}  "
              f"{nb} holds {c['a_in_b']:.0%} of {na}, {na} holds {c['b_in_a']:.0%} of {nb}")
        print(f"      only {na} {len(c['only_a'])}, {len(c['only_a_inside_b'])} of them inside a longer "
              f"surface of {nb};  only {nb} {len(c['only_b'])}, {len(c['only_b_inside_a'])} inside {na}")
        if names:
            for label, only, inside in ((na, c["only_a"], c["only_a_inside_b"]),
                                        (nb, c["only_b"], c["only_b_inside_a"])):
                cut = {x for x, _ in inside}
                print(f"      only {label}, not inside the other ({len(only) - len(cut)}): "
                      + " · ".join(t for t in only if t not in cut))
                if inside:
                    print(f"      only {label}, inside a longer surface: "
                          + " · ".join(f"{x} ⊂ {y}" for x, y in inside))
        print()
    return 0


def selftest() -> int:
    """Each case carries the exact outcome it must produce, so a case that holds
    for the wrong reason fails."""
    import subject
    doc = subject.document("aegis-subplots-kapitelweise-system-exploration-docx")
    cases = []

    def case(name, got, want):
        cases.append((name, got == want, got, want))

    same = compare(["AEGIS", "Kael"], ["AEGIS", "Kael"])
    case("identical lists: F1 1", round(same["f1"], 3), 1.0)
    case("an article is no boundary", compare(["Die unsichtbare Grenze"], ["unsichtbare Grenze"])["shared"], 1)
    case("an inflection is not shared (fold is no stemmer)", compare(["Guardian"], ["Guardians"])["shared"], 0)
    cut = compare(["Juna", "Kael"], ["Juna/V", "Kael"])
    case("a shorter cut of one surface counts as inside", cut["only_a_inside_b"], [("Juna", "Juna/V")])
    case("...and is never counted shared", cut["shared"], 1)
    case("inside means anywhere, not only at the start",
         compare(["Amnesie-Barrieren"], ["ANP/EP-Amnesie-Barrieren"])["only_a_inside_b"],
         [("Amnesie-Barrieren", "ANP/EP-Amnesie-Barrieren")])
    case("a one-letter term is never inside", compare(["V"], ["Juna/V"])["only_a_inside_b"], [])
    sub = compare(["AEGIS"], ["AEGIS", "Kael", "Riss", "Risse"])
    case("containment is asymmetric: A in B", sub["a_in_b"], 1.0)
    case("containment is asymmetric: B in A", sub["b_in_a"], 0.25)
    case("F1 is symmetric", round(sub["f1"], 6),
         round(compare(["AEGIS", "Kael", "Riss", "Risse"], ["AEGIS"])["f1"], 6))
    case("a prose bullet is no candidate, a citation no part of the term",
         terms_of("- Kael  ^[L13]\n- This reads, like a sentence. It is not a term\n"), ["Kael"])
    case("a normalised form the text never writes is caught", absent(doc, ["Kern-Welt", "AEGIS"]), ["Kern-Welt"])
    bad = 0
    for name, ok, got, want in cases:
        bad += not ok
        print(f"  {'ok ' if ok else 'BAD'} {name}" + ("" if ok else f": got {got!r}, want {want!r}"))
    print(f"agree: {len(cases) - bad} of {len(cases)} cases hold")
    return 1 if bad else 0


def main(argv: list[str]) -> int:
    if argv[:1] == ["selftest"]:
        return selftest()
    names = "--names" in argv
    args = [a for a in argv if a != "--names"]
    if not args or args[0].startswith("-"):
        print(__doc__)
        return 2
    slug, rest = args[0], args[1:]
    paths = [Path(p) for p in rest] if rest else sorted((RUNS / slug).glob("03-candidates*.md"))
    missing = [p for p in paths if not p.exists()]
    if missing or len(paths) < 2:
        print(f"need two lists; missing {', '.join(map(str, missing))}" if missing
              else f"fewer than two lists in Plan/runs/{slug}/")
        return 1
    return report(slug, paths, names)


if __name__ == "__main__":
    from subject import cli
    cli(main)
