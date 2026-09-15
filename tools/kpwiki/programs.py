"""kpwiki programs — composed DSPy modules.

``SourceIngest`` is the first program of the ingest loop
(Plan/wiki concept §4, Phase B): triage → claims → canon-conflict check.
Retrieval of Canon passages is injected as a callable so the program stays
testable offline and independent of the search backend (BM25 first, graph
``match_codex_entries`` later).
"""
from __future__ import annotations

from typing import Callable

import dspy

from .schema import Claim
from .signatures import CheckCanonConflict, ExtractClaims, TriageSource

CanonRetriever = Callable[[list[Claim]], str]
BODY_PREVIEW_CHARS = 12000


def number_lines(body: str) -> str:
    """Prefix every line with its 1-based number so citations are verifiable."""
    return "\n".join(f"{i:04d}| {line}" for i, line in enumerate(body.splitlines(), start=1))


def no_canon_retrieval(_claims: list[Claim]) -> str:
    """Retriever used in dry runs: nothing retrieved, so nothing can conflict."""
    return ""


class SourceIngest(dspy.Module):
    """Turn one source export into triage, cited claims and canon conflicts."""

    def __init__(self, retrieve_canon: CanonRetriever = no_canon_retrieval):
        super().__init__()
        self.triage = dspy.ChainOfThought(TriageSource)
        self.extract = dspy.Predict(ExtractClaims)
        self.conflicts = dspy.ChainOfThought(CheckCanonConflict)
        self.retrieve_canon = retrieve_canon

    def forward(self, source_file: str, title: str, category_hint: str,
                body: str, glossary_terms: str = "") -> dspy.Prediction:
        triage = self.triage(title=title, category_hint=category_hint,
                             body=body[:BODY_PREVIEW_CHARS]).triage
        claims = self.extract(source_file=source_file, numbered_body=number_lines(body),
                              glossary_terms=glossary_terms).claims
        passages = self.retrieve_canon(claims)
        conflicts = self.conflicts(claims=claims, canon_passages=passages).conflicts if passages else []
        return dspy.Prediction(triage=triage, claims=claims, conflicts=conflicts)
