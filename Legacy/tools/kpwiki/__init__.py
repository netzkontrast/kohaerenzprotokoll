"""kpwiki — DSPy base for the Kohärenz Protokoll knowledge system.

Every LLM step of the research wiki (source triage, claim extraction with
line-scoped citations, canon-conflict check, question generation) is a typed
``dspy.Signature`` composed into ``dspy.Module`` programs. No hand-written
prompt strings live in this package: instructions are the Signature
docstrings, and GEPA tunes them against the rich-feedback metrics in
``metrics.py`` (see docs/dspy-base.md and
Plan/wiki/knowledge-system-concept_2026-09-15.md).

Layout:
    lm.py          configure task / worker / reflection LMs from env
    schema.py      Pydantic models shared by signatures, metrics and the lint
    signatures.py  typed I/O contracts (the only place "prompts" are described)
    programs.py    SourceIngest — the first program of the ingest loop
    metrics.py     deterministic + rich-feedback metrics (GEPA-ready)
    smoke.py       ``python -m tools.kpwiki.smoke --dry-run`` (no LM call)
"""

__all__ = ["lm", "schema", "signatures", "programs", "metrics"]
