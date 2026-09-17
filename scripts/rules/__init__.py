"""The rule set — where this project's learned structure lives.

A rule is a small, named, versioned function that derives facts from **one**
document. It is the unit an agent working a step is expected to change: when a
document does not fit, the answer is a new rule, a bumped version, or a recorded
exception -- never a quiet special case in a query.

That is the point. Which structures matter and how contents relate is not known
in advance and is not designed up front; it is worked out by processing documents,
and the rules directory is the residue of that work. Starting this on another
corpus means starting with an empty directory.

## The contract

    NAME     = "structure"          # unique, becomes the key in the cache
    VERSION  = 1                    # bump when derive() changes; stale entries re-derive
    def applies(doc) -> bool        # the rule's own opinion about scope
    def derive(doc) -> dict         # the facts, JSON-serialisable

`doc` carries: slug, category, date, format, sha256, path, body, offset.
`offset` is the file line the body starts on, found per document, never assumed.

## Scope versus exception

`applies()` is the rule saying where it belongs. An **exception** is the opposite
direction: a human saying this rule must not run on that document, and why. It
lives in `Plan/rules/exceptions.jsonl` and is reported, never silent.

A rule that quietly skips what it cannot handle teaches nobody anything. A rule
that has an exception filed against it, with a reason, is a question someone can
come back to.
"""

from __future__ import annotations

import importlib
import pkgutil
from pathlib import Path


def load() -> list:
    """Every module in this package that satisfies the contract."""
    rules = []
    for info in pkgutil.iter_modules([str(Path(__file__).parent)]):
        module = importlib.import_module(f"{__name__}.{info.name}")
        if all(hasattr(module, attr) for attr in ("NAME", "VERSION", "applies", "derive")):
            rules.append(module)
    return sorted(rules, key=lambda m: m.NAME)
