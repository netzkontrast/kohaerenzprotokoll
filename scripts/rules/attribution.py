"""Where a document attributes a claim to something outside itself.

Found by document 4, and it is the miss this project was built to expect. The
`[User Query]` marker was document 3's headline finding -- 26 of them, the thing
that made a single `kind` label on that file impossible. Document 4 carries the
same marker once, and **nothing in its extraction saw it**: not the profile, not
the probes, not the candidate list, not the census. That is correct behaviour,
not a bug. A census may not carry knowledge from another document, so it did not
go looking. The rule set is where such knowledge is allowed to live, because a
rule is procedural -- it runs on every document and is re-checkable -- while a
census is a reading of one.

## Unescape first, or undercount by six times

A plain probe for `[User Query]` finds **3 documents**. The same probe after
removing export backslash escaping finds **18**, with 157 occurrences. The Drive
conversion writes the marker three ways -- `[User Query]`, `\[User Query\]` and
`\\\[User Query\\\]` -- and a string search splits one convention into three.
`export_damage` counts that escaping; this rule is the first thing that had to
undo it to get a true number.

So: any probe for a bracketed convention in this corpus must unescape first. The
finding generalises past this marker.
"""

from __future__ import annotations

import re

NAME = "attribution"
VERSION = 1

ESCAPE = re.compile(r"\\+([\[\]*\"_])")

# Each pattern is here because a document had it, with that document named.
MARKERS = {
    # kohaerenzprotokoll-aegis-und-systementropie, 26x -- a passage quoted back
    # from the commission rather than concluded by the research.
    "user_query": re.compile(r"\[User Query[^\]\n]{0,40}\]"),
    # guardians-und-kern-welten-konzept L117, 1x -- the same attribution, written
    # into running prose instead of bracketed after it.
    "user_query_inline": re.compile(r"\((?:laut|gemäß|Kontext aus) User Query[^)\n]{0,200}\)"),
    # kohaerenzprotokoll-aegis-und-systementropie, 13x -- a section declaring
    # which numbered question of its brief it answers.
    "addressed_question": re.compile(r"\(Adressiert [^)\n]{0,60}\)"),
    # guardians-und-kern-welten-konzept L96 -- the document correcting its own
    # body: five Guardians named under a heading that counts four pairs.
    "aside": re.compile(r"\*?\(Anmerkung:[^)\n]{0,200}\)"),
}


def applies(doc: dict) -> bool:
    return True


def derive(doc: dict) -> dict:
    """Marker counts and the file lines they sit on, after undoing export escaping.

    Unescaping is done per line so the reported line numbers stay the file's own.
    """
    found: dict[str, dict] = {}
    for number, line in enumerate(doc["body"].split("\n"), start=doc["offset"]):
        clean = ESCAPE.sub(r"\1", line)
        for name, pattern in MARKERS.items():
            hits = pattern.findall(clean)
            if not hits:
                continue
            entry = found.setdefault(name, {"n": 0, "lines": []})
            entry["n"] += len(hits)
            if len(entry["lines"]) < 12:
                entry["lines"].append(number)
    return {
        "markers": found,
        "marked": sorted(found),
        "escaping_undone": bool(ESCAPE.search(doc["body"])),
    }
