"""What the Drive conversion did to the text, and what it costs a check.

Each of these defeats exact matching or quote verification silently. They were
found one document at a time: zero-width spaces in flattened subscripts, footnote
numbers glued to the words they annotate, backslash escaping inside quoted
coinages, and two quote-glyph families in one file.
"""

from __future__ import annotations

import re

NAME = "export_damage"
VERSION = 1

INVISIBLE = ("\u200b", "\u200c", "\u200d", "\u2060", "\ufeff")
TYPOGRAPHIC = "\u201e\u201c\u201d\u2018\u2019\u2013\u2014"
GLUED_REF = re.compile(r"([A-ZÄÖÜ][A-Za-zäöüß\-]{3,})\s(\d{1,2})\b")
ESCAPE = re.compile(r"\\([\[\]*\"_])")


def applies(doc: dict) -> bool:
    return True


def derive(doc: dict) -> dict:
    body = doc["body"]
    return {
        "invisible_characters": {f"U+{ord(c):04X}": body.count(c) for c in INVISIBLE if c in body},
        "glued_ref_numbers": len(GLUED_REF.findall(body)),
        "backslash_escapes": len(ESCAPE.findall(body)),
        "typographic_marks": sum(body.count(c) for c in TYPOGRAPHIC),
        "ascii_quotes": body.count('"'),
    }
