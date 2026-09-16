"""Hand-built batch for the BatchCompile dry run and its offline tests.

Two short German sources, one reviewed concept page (``juna``), a
``Compiled`` result that satisfies every rule of ``compile_metric`` and a
broken copy that violates five of them (protected update, quote not in the
cited lines, one-source disagreement, ``new`` item already on the page,
German definition sentence). ``BROKEN_NEEDLES`` are the feedback fragments
the broken copy must produce. Kept outside ``tests/`` so ``smoke.py`` never
imports a test module.
"""
from __future__ import annotations

import dspy

from .programs import SourceInput
from .schema import (Citation, CitedStatement, Claim, Compiled, ConceptDraft, ConceptPlan, DefinitionSentence, Diff,
                     Disagreement, Extraction, IngestDecision, PageState, TimelineEntry, Triage)

SLUG_A, SLUG_B = "notiz-kael-a", "notiz-kael-b"
FILE_A, FILE_B = f"Sources/drive/{SLUG_A}.md", f"Sources/drive/{SLUG_B}.md"
DATE_A, DATE_B = "2026-05-01", "2026-06-01"
BODY_A = """# Notiz A zum System Kael
Kael ist ein verteiltes System aus mehreren Anteilen.
Juna lebt in KW2.
Der Schleier hält bis Kapitel 13.
"""
BODY_B = """# Notiz B zum System Kael
Das System Kael besteht aus vier Anteilen.
Juna lebt in KW3.
Der Schleier ist ein Ritual.
"""
PAGE_JUNA_BODY = """---
title: "Juna"
kind: concept
slug: juna
status: reviewed
---

## Definition

Juna lebt in KW2. ^[Sources/drive/notiz-kael-a.md:3-3]
"""
KNOWN_ENTITIES = ["kael", "juna", "schleier", "kw2", "kw3"]
GOLD_CONCEPTS = ["system-kael", "juna", "schleier"]
BROKEN_NEEDLES = ("illegal decision: update on juna", "citation does not resolve",
                  "a disagreement needs two distinct sources", "'new' item already on the page",
                  "definition sentence is not English")


def sources() -> list[SourceInput]:
    return [SourceInput(slug=SLUG_A, title="Notiz A zum System Kael", category_hint="kernkonzept",
                        index_date=DATE_A, source_file=FILE_A, body=BODY_A),
            SourceInput(slug=SLUG_B, title="Notiz B zum System Kael", category_hint="kernkonzept",
                        index_date=DATE_B, source_file=FILE_B, body=BODY_B)]


def pages() -> dict[str, PageState]:
    return {"juna": PageState(slug="juna", kind="concept", status="reviewed", body=PAGE_JUNA_BODY)}


def gold_example() -> dspy.Example:
    return dspy.Example(sources={FILE_A: BODY_A, FILE_B: BODY_B}, pages=pages(), known_entities=KNOWN_ENTITIES,
                        gold_concepts=GOLD_CONCEPTS).with_inputs("sources", "pages", "known_entities")


def cite(file: str, line: int, quote: str) -> Citation:
    return Citation(file=file, start_line=line, end_line=line, quote=quote)


def _triage() -> Triage:
    return Triage(tier="T3-work", category="kernkonzept", language="de",
                  summary="Working note on the Kael system, Juna's Kernwelt and the veil rule.")


def extractions() -> list[Extraction]:
    claims_a = [
        Claim(text="Kael ist ein verteiltes System aus mehreren Anteilen.", kind="definition",
              citation=cite(FILE_A, 2, "Kael ist ein verteiltes System aus mehreren Anteilen."), entities=["kael"]),
        Claim(text="Juna lebt in KW2.", kind="character", citation=cite(FILE_A, 3, "Juna lebt in KW2."),
              entities=["juna", "kw2"]),
        Claim(text="Der Schleier hält bis Kapitel 13.", kind="rule", citation=cite(FILE_A, 4, "hält bis Kapitel 13"),
              entities=["schleier"]),
    ]
    claims_b = [
        Claim(text="Das System Kael besteht aus vier Anteilen.", kind="definition",
              citation=cite(FILE_B, 2, "besteht aus vier Anteilen"), entities=["kael"]),
        Claim(text="Juna lebt in KW3.", kind="character", citation=cite(FILE_B, 3, "Juna lebt in KW3."),
              entities=["juna", "kw3"]),
        Claim(text="Der Schleier ist ein Ritual.", kind="rule", citation=cite(FILE_B, 4, "ist ein Ritual"),
              entities=["schleier"]),
    ]
    return [Extraction(source=SLUG_A, title="Notiz A zum System Kael", triage=_triage(), claims=claims_a),
            Extraction(source=SLUG_B, title="Notiz B zum System Kael", triage=_triage(), claims=claims_b)]


def plans() -> list[ConceptPlan]:
    return [ConceptPlan(slug="system-kael", title="System Kael", kind_detail="concept", claim_ids=[1, 4]),
            ConceptPlan(slug="juna", title="Juna", kind_detail="character", claim_ids=[2, 5], existing_slug="juna"),
            ConceptPlan(slug="schleier", title="Schleier", kind_detail="rule", claim_ids=[3, 6])]


def concepts() -> list[ConceptDraft]:
    kael = ConceptDraft(
        slug="system-kael", title="System Kael", kind_detail="concept",
        definition=[DefinitionSentence(text="Kael is a distributed system made of several parts.",
                                       citations=[cite(FILE_A, 2, "Kael ist ein verteiltes System aus mehreren Anteilen")]),
                    DefinitionSentence(text="One note counts four parts.", citations=[cite(FILE_B, 2, "besteht aus vier Anteilen")])],
        agreements=[CitedStatement(text="Kael consists of several parts.",
                                   citations=[cite(FILE_A, 2, "aus mehreren Anteilen"), cite(FILE_B, 2, "aus vier Anteilen")])],
        timeline=[TimelineEntry(date=DATE_A, source=SLUG_A, what_changed="introduces Kael as a distributed system"),
                  TimelineEntry(date=DATE_B, source=SLUG_B, what_changed="counts four parts")],
        sources=[SLUG_A, SLUG_B], entities=["kael"], confidence="medium", status="tentative")
    juna = ConceptDraft(
        slug="juna", title="Juna", kind_detail="character",
        definition=[DefinitionSentence(text="Juna lives in KW2 according to note A and in KW3 according to note B.",
                                       citations=[cite(FILE_A, 3, "Juna lebt in KW2."), cite(FILE_B, 3, "Juna lebt in KW3.")])],
        disagreements=[Disagreement(topic="Juna's Kernwelt", sources=[SLUG_A, SLUG_B], positions=["KW2", "KW3"],
                                    citations=[cite(FILE_A, 3, "Juna lebt in KW2."), cite(FILE_B, 3, "Juna lebt in KW3.")])],
        timeline=[TimelineEntry(date=DATE_A, source=SLUG_A, what_changed="places Juna in KW2"),
                  TimelineEntry(date=DATE_B, source=SLUG_B, what_changed="places Juna in KW3")],
        sources=[SLUG_A, SLUG_B], entities=["juna", "kw2", "kw3"], confidence="low", status="contradicted")
    schleier = ConceptDraft(
        slug="schleier", title="Schleier", kind_detail="rule",
        definition=[DefinitionSentence(text="The veil holds until chapter 13 and is a ritual.",
                                       citations=[cite(FILE_A, 4, "hält bis Kapitel 13"), cite(FILE_B, 4, "ist ein Ritual")])],
        timeline=[TimelineEntry(date=DATE_A, source=SLUG_A, what_changed="sets the chapter-13 limit"),
                  TimelineEntry(date=DATE_B, source=SLUG_B, what_changed="calls the veil a ritual")],
        sources=[SLUG_A, SLUG_B], entities=["schleier"], confidence="medium", status="tentative")
    return [kael, juna, schleier]


def handmade_compiled() -> Compiled:
    decisions = [IngestDecision(slug="system-kael", action="create", rationale="no page yet"),
                 IngestDecision(slug="juna", action="flag", rationale="note B disputes the reviewed page",
                                conflicts=["Kernwelt: KW2 (page, note A) vs KW3 (note B)"]),
                 IngestDecision(slug="schleier", action="create", rationale="no page yet")]
    diffs = {"juna": Diff(reinforced=["Juna lebt in KW2 (note A)"], challenged=["Kernwelt KW2 vs KW3"],
                          gaps=["when Juna moved, if she did"])}
    return Compiled(extractions=extractions(), concepts=concepts(), decisions=decisions, diffs=diffs, plans=plans())


def broken_compiled() -> Compiled:
    """The handmade batch with five rule violations, one per BROKEN_NEEDLES entry."""
    bad = handmade_compiled().model_copy(deep=True)
    juna, schleier = bad.concepts[1], bad.concepts[2]
    bad.decisions[1] = IngestDecision(slug="juna", action="update", rationale="apply note B",
                                      conflicts=["Kernwelt: KW2 vs KW3"])
    juna.definition[0].citations[0].quote = "Juna wohnt in KW2."
    juna.disagreements[0].sources, juna.disagreements[0].positions = [SLUG_B], ["KW3"]
    bad.diffs["juna"].new = ["Juna lebt in KW2."]
    schleier.definition[0].text = "Der Schleier hält bis Kapitel 13 und ist ein Ritual."
    return bad
