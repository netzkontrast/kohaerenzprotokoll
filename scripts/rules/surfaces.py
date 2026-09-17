"""Every capitalised token, with its count and the file lines it appears on.

This is what makes a corpus question a lookup instead of a re-read. A term wiki
asks about terms, terms are capitalised in German, and the vocabulary of one
document is small -- so the index is small, while the text it replaces is not.

**Two limits, stated rather than discovered later.**

A query for a lowercase word, or for a phrase, is not in here. `scripts/corpus.py`
falls back to reading for those and says when it did.

And a compound is **one** token: `Kael-Julia-Bindung` is counted once, under that
name, and does not add to `Kael`. A `\bKael\b` regex over the raw text counts the
head inside every compound and returns a larger number -- 293 documents against
this index's 287. Neither is wrong; they answer different questions, and the two
must never be quoted as the same fact. `corpus.py family <head>` shows the
compound family so the difference is visible rather than inferred.
"""

from __future__ import annotations

import re

NAME = "surfaces"
VERSION = 1

TOKEN = re.compile(r"\b[A-ZÄÖÜ][A-Za-zäöüß]{2,}(?:-[A-ZÄÖÜa-zäöüß][A-Za-zäöüß]+)*\b")


def applies(doc: dict) -> bool:
    return True


def derive(doc: dict) -> dict:
    counts: dict[str, int] = {}
    lines: dict[str, list[int]] = {}
    for number, line in enumerate(doc["body"].split("\n"), start=doc["offset"]):
        for token in TOKEN.findall(line):
            counts[token] = counts.get(token, 0) + 1
            if token not in lines:
                lines[token] = []
            if len(lines[token]) < 12:
                lines[token].append(number)
    return {"tokens": {t: {"n": counts[t], "lines": lines[t]} for t in sorted(counts)}}
