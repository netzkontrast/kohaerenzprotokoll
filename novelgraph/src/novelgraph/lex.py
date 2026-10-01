"""The lexical side of a chunk: `fold()` surfaces and lemmata, no model.

- **surfaces** — every capitalised token (the rule of `scripts/rules/surfaces.py`),
  folded by the repository's one `fold()`, so a surface here is the key a wiki
  lookup uses.
- **lemmata** — simplemma (a dictionary lemmatizer, deterministic), lowercased,
  with their count in the chunk; stopwords and tokens without a letter are dropped.

The document's language decides the lemmatizer's language order: a German
stopword majority is `de`, an English one `en`, neither by twice the other `mixed`
(German first, English as fallback).
"""

from __future__ import annotations

import re
from collections import Counter
from functools import lru_cache

import simplemma

from .repo import fold

WORD = re.compile(r"[^\W\d_][\w-]*", re.UNICODE)
CAPITAL = re.compile(r"\b[A-ZÄÖÜ][\w-]*")

DE = set("der die das und ist nicht ein eine zu den von mit sich des auf für im dem als auch es an werden aus er hat "
         "dass sie nach wird bei einer um am sind noch wie einem über einen so zum war haben nur oder aber vor zur "
         "bis mehr durch man sein wurde sei kann ihre seine diese dieser dieses wenn was wo".split())
EN = set("the and of to a in is that it for as with was on be by are this not or from at which an but have has "
         "their its can will they we were been these more such into than how what when".split())
STOP = DE | EN


def language(text: str) -> str:
    words = [w.lower() for w in WORD.findall(text[:200_000])]
    de = sum(1 for w in words if w in DE)
    en = sum(1 for w in words if w in EN)
    if de > 2 * en:
        return "de"
    if en > 2 * de:
        return "en"
    return "mixed"


LANGS = {"de": ("de", "en"), "en": ("en", "de"), "mixed": ("de", "en")}


@lru_cache(maxsize=500_000)
def lemma(word: str, lang: str) -> str:
    return simplemma.lemmatize(word, lang=LANGS[lang]).lower()


def surfaces(text: str) -> str:
    """The folded surfaces, sorted, space-separated (a fold holds no space)."""
    return " ".join(sorted({f for t in CAPITAL.findall(text) if t.lower() not in STOP for f in [fold(t)] if len(f) >= 2}))


def lemmata(text: str, lang: str) -> str:
    """The lemmata, sorted, space-separated, `lemma:n` when it occurs n > 1 times. A string and not a JSON
    object because the object form made `lex/` 104 MB for three chunkers — four times the corpus."""
    counts = Counter()
    for w in WORD.findall(text):
        if w.lower() in STOP or len(w) < 2:
            continue
        counts[lemma(w, lang)] += 1
    return " ".join(w if n == 1 else f"{w}:{n}" for w, n in sorted(counts.items()))


def expand(lemmata_field: str) -> str:
    """The lemma column FTS5 indexes: each lemma repeated by its count, so BM25 sees its frequency."""
    out = []
    for item in lemmata_field.split():
        w, _, n = item.rpartition(":") if ":" in item else (item, "", "1")
        out.extend([w] * int(n))
    return " ".join(out)


def query_lemmata(query: str) -> list[str]:
    """A query's lemmata under both language orders, so a German or English question finds either."""
    out = []
    for w in WORD.findall(query):
        if w.lower() in STOP or len(w) < 2:
            continue
        for lang in ("de", "en"):
            out.append(lemma(w, lang))
    return list(dict.fromkeys(out))
