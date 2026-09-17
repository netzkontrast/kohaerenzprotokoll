"""How the document is built: headings, tables, formulas, length.

Found by processing four documents. Every field here exists because a document
had it and a reader needed it -- the heading count because one category has a
median of 2 and another 23, the table rows because one document's own summary
renames five of its eight terms.
"""

from __future__ import annotations

import re

NAME = "structure"
VERSION = 1

HEADING = re.compile(r"^#{1,6} ")
BOLD_ONLY = re.compile(r"^\*\*.+\*\*\s*$")
MATH = re.compile(r"[\u2205\u2192\u2261\u2208\u2286\u2227\u2228\u22c3\u03bb\u03a3\u03c3\u03bc\u03a0\u0394\u03b8\u03b1\u03d5\u2295\u22a2]")
INLINE_LABEL = re.compile(r"\*\*([A-ZÄÖÜ][^*\n]{2,40}):\*\*")


def applies(doc: dict) -> bool:
    return True


def derive(doc: dict) -> dict:
    lines = doc["body"].split("\n")
    labels: dict[str, int] = {}
    for label in INLINE_LABEL.findall(doc["body"]):
        labels[label] = labels.get(label, 0) + 1
    return {
        "body_words": sum(len(line.split()) for line in lines),
        "headings": sum(1 for line in lines if HEADING.match(line)),
        "bold_only_lines": sum(1 for line in lines if BOLD_ONLY.match(line)),
        "table_rows": sum(1 for line in lines if line.startswith("|")),
        "math_symbol_lines": sum(1 for line in lines if MATH.search(line)),
        "question_marks": doc["body"].count("?"),
        "longest_line": max((len(line) for line in lines), default=0),
        "has_frontmatter": doc["offset"] > 1,
        "repeated_labels": {k: v for k, v in sorted(labels.items(), key=lambda kv: -kv[1]) if v >= 3},
    }
