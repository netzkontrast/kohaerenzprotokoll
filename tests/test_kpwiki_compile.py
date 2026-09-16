"""Offline tests for BatchCompile and compile_metric (skip when dspy is missing).

No LM is called: the metric runs on the hand-built batch of
``tools/kpwiki/compile_fixture.py`` and ``forward`` runs with its six
predictors replaced by recording stubs, so the two-phase order, the
in-code ``create`` and the bookkeeping are asserted deterministically.
"""
from __future__ import annotations

import pytest

dspy = pytest.importorskip("dspy")

from tools.kpwiki import compile_fixture as fx  # noqa: E402
from tools.kpwiki.compile_metric import (citation_resolves, claims_keep_language, compile_metric,  # noqa: E402
                                         decision_legal, diff_consistent, unverifiable_quotes)
from tools.kpwiki.metrics import language_of  # noqa: E402
from tools.kpwiki.programs import (MAX_DIGEST_CLAIMS, BatchCompile, SourceInput, index_claims,  # noqa: E402
                                   merge_plans)
from tools.kpwiki.schema import (Citation, Claim, ConceptPlan, Diff, Extraction, IngestDecision,  # noqa: E402
                                 PageState, Triage)

TRIAGE = Triage(tier="T3-work", category="kernkonzept", language="de", summary="Working note.")
FLAG = IngestDecision(slug="juna", action="flag", rationale="note B disputes the page",
                      conflicts=["Kernwelt: KW2 vs KW3"])
DIFF = Diff(challenged=["Kernwelt KW2 vs KW3"], gaps=["when Juna moved"])


def stub(program: BatchCompile, calls: list[str], *, plans=None, claims=None) -> BatchCompile:
    """Replace the six predictors with recorders returning fixture data."""
    drafts = {k.title: k for k in fx.concepts()}
    by_file = claims if claims is not None else {e.claims[0].citation.file: e.claims for e in fx.extractions()}

    def recorder(name: str, key: str, fn):
        def call(**kwargs):
            calls.append(name)
            return dspy.Prediction(**{key: fn(**kwargs)})
        return call

    program.triage = recorder("triage", "triage", lambda **kw: TRIAGE)
    program.extract = recorder("extract", "claims", lambda source_file, **kw: by_file.get(source_file, []))
    program.plan = recorder("plan", "plan", lambda **kw: plans if plans is not None else fx.plans())
    program.merge = recorder("merge", "draft", lambda title, **kw: drafts[title])
    program.decide = recorder("decide", "decision", lambda **kw: FLAG)
    program.diff = recorder("diff", "diff", lambda **kw: DIFF)
    return program


def run(calls: list[str], *, sources=None, plans=None, claims=None):
    program = stub(BatchCompile(), calls, plans=plans, claims=claims)
    return program(sources=sources if sources is not None else fx.sources(), pages=fx.pages(),
                   known_entities=fx.KNOWN_ENTITIES).compiled


# --- metric -------------------------------------------------------------------------


def test_handmade_batch_satisfies_every_axis():
    result = compile_metric(fx.gold_example(), dspy.Prediction(compiled=fx.handmade_compiled()))
    assert result.score >= 0.95
    assert result.feedback == "cited, legally decided, merged across sources, consistent diff"


def test_broken_batch_scores_lower_and_names_every_deficit():
    gold = fx.gold_example()
    good = compile_metric(gold, dspy.Prediction(compiled=fx.handmade_compiled()))
    broken = compile_metric(gold, dspy.Prediction(compiled=fx.broken_compiled()))
    assert broken.score < good.score
    for needle in fx.BROKEN_NEEDLES:
        assert needle in broken.feedback, (needle, broken.feedback)


def test_metric_returns_prediction_and_scores_a_missing_result_zero():
    result = compile_metric(fx.gold_example(), dspy.Prediction(compiled=None))
    assert isinstance(result, dspy.Prediction)
    assert result.score == 0.0 and "no Compiled result" in result.feedback


def test_missing_gold_concept_is_named():
    run_without_schleier = fx.handmade_compiled()
    run_without_schleier.concepts = run_without_schleier.concepts[:2]
    result = compile_metric(fx.gold_example(), dspy.Prediction(compiled=run_without_schleier))
    assert "expected concepts missing: ['schleier']" in result.feedback


def test_citation_resolves_across_a_line_break_and_refuses_an_empty_quote():
    sources = {"a.md": "Kael ist ein verteiltes\nSystem aus Anteilen."}
    assert citation_resolves(Citation(file="a.md", start_line=1, end_line=2, quote="verteiltes System"), sources)
    assert not citation_resolves(Citation(file="a.md", start_line=1, end_line=2, quote=""), sources)
    assert not citation_resolves(Citation(file="a.md", start_line=1, end_line=9, quote="Kael"), sources)


def test_a_quoted_term_must_stand_in_the_cited_lines():
    sources = {"a.md": "Daten, die dem Modell widersprechen, werden als Rauschen abgelehnt."}
    cite = [Citation(file="a.md", start_line=1, end_line=1, quote="als Rauschen abgelehnt")]
    assert unverifiable_quotes("Das System nennt sie „Rauschen“.", cite, sources) == []
    assert unverifiable_quotes('It rejects them as "noise."', cite, sources) == ['noise.']
    assert unverifiable_quotes("no quotes here", cite, sources) == []
    assert unverifiable_quotes("„Rauschen“", [], sources) == []


def test_the_citation_axis_names_an_unverifiable_quoted_term():
    run = fx.handmade_compiled()
    run.extractions[0].claims[1].text = 'Juna lebt laut Notiz in "KW9".'
    result = compile_metric(fx.gold_example(), dspy.Prediction(compiled=run))
    assert "quoted term not in the cited lines: 'KW9'" in result.feedback
    assert result.score < 1.0


def test_a_disagreement_without_a_position_per_source_is_named():
    run = fx.handmade_compiled()
    run.concepts[1].disagreements[0].positions = ["KW2"]
    result = compile_metric(fx.gold_example(), dspy.Prediction(compiled=run))
    assert "juna: a disagreement needs one position per source" in result.feedback


def test_language_of_is_symmetric_and_admits_it_does_not_know():
    assert language_of("Der Schleier hält bis zum Ende und ist nicht offen.") == "de"
    assert language_of("The veil is not the end of the protocol and is closed.") == "en"
    assert language_of("Kael 42") == "unknown"


def test_claims_leaving_the_source_language_are_penalised_in_both_directions():
    german = Claim(text="Juna lebt in KW2 und ist nicht Teil des Systems.", kind="character",
                   citation=Citation(file=fx.FILE_A, start_line=3, end_line=3, quote="Juna lebt in KW2."))
    english = german.model_copy(update={"text": "Juna lives in KW2 and is not part of the system."})
    english_body = "Juna lives in KW2. The veil is not the end of it and is closed."
    assert claims_keep_language([german], fx.BODY_A)[0] == 1.0
    assert claims_keep_language([english], fx.BODY_A) == (0.0, "de")
    assert claims_keep_language([german], english_body) == (0.0, "en")
    assert claims_keep_language([], fx.BODY_A)[0] == 1.0
    assert claims_keep_language([german], "42 7")[0] == 1.0


def test_decision_legal_protects_a_reviewed_page():
    page = PageState(slug="juna", kind="concept", status="reviewed", body="Juna lebt in KW2.")
    conflicting = IngestDecision(slug="juna", action="update", rationale="apply", conflicts=["KW2 vs KW3"])
    assert not decision_legal(conflicting, page)
    assert decision_legal(conflicting.model_copy(update={"action": "flag"}), page)
    assert decision_legal(conflicting.model_copy(update={"conflicts": []}), page)
    assert not decision_legal(conflicting.model_copy(update={"action": "create"}), page)
    assert decision_legal(IngestDecision(slug="neu", action="create", rationale="no page yet"), None)


def test_diff_consistent_names_both_problems():
    problems = diff_consistent(Diff(challenged=["Wohnort"], new=["Juna lebt in KW2."]),
                               IngestDecision(slug="juna", action="flag", rationale="x"),
                               "Juna lebt in KW2.")
    assert any("challenged item without a conflict" in p for p in problems)
    assert any("already on the page" in p for p in problems)


# --- program ------------------------------------------------------------------------


def test_named_predictors_are_stable():
    assert [name for name, _ in BatchCompile().named_predictors()] == [
        "triage.predict", "extract", "plan.predict", "merge.predict", "decide.predict", "diff.predict"]


def test_every_source_is_extracted_before_any_concept_is_planned():
    calls: list[str] = []
    run(calls)
    assert calls[:4] == ["triage", "extract", "triage", "extract"]
    assert calls.index("plan") == 4 and calls.count("plan") == 1
    assert calls.count("merge") == 3


def test_create_is_decided_in_code_and_only_an_existing_page_is_diffed():
    calls: list[str] = []
    compiled = run(calls)
    actions = {d.slug: d.action for d in compiled.decisions}
    assert actions == {"system-kael": "create", "juna": "flag", "schleier": "create"}
    assert calls.count("decide") == 1 and calls.count("diff") == 1
    assert list(compiled.diffs) == ["juna"]


def test_truncated_and_empty_sources_are_skipped():
    calls: list[str] = []
    sources = fx.sources() + [
        SourceInput(slug="cut", title="Cut", source_file="Sources/drive/cut.md", body="text", truncated=True),
        SourceInput(slug="leer", title="Leer", source_file="Sources/drive/leer.md", body="  \n")]
    compiled = run(calls, sources=sources)
    assert compiled.skipped == ["cut", "leer"]
    assert calls.count("extract") == 2
    assert {e.source for e in compiled.extractions} == {fx.SLUG_A, fx.SLUG_B}


def test_unknown_claim_ids_are_dropped_and_unused_claims_reported():
    plans = [ConceptPlan(slug="system-kael", title="System Kael", kind_detail="concept", claim_ids=[1, 99])]
    compiled = run([], plans=plans)
    assert [k.slug for k in compiled.concepts] == ["system-kael"]
    assert compiled.unassigned_claims == [f"{fx.SLUG_A}:1", f"{fx.SLUG_A}:2",
                                          f"{fx.SLUG_B}:0", f"{fx.SLUG_B}:1", f"{fx.SLUG_B}:2"]


def test_a_plan_with_no_resolvable_claim_produces_no_concept():
    plans = [ConceptPlan(slug="geist", title="Geist", kind_detail="concept", claim_ids=[42])]
    compiled = run([], plans=plans)
    assert compiled.concepts == [] and compiled.decisions == []


def test_an_existing_slug_wins_over_the_planned_one():
    plans = [ConceptPlan(slug="juna-neu", title="Juna", kind_detail="character", claim_ids=[2, 5],
                         existing_slug="juna")]
    compiled = run([], plans=plans)
    assert [k.slug for k in compiled.concepts] == ["juna"]
    assert compiled.decisions[0].action == "flag"


def test_index_claims_numbers_globally_in_source_order():
    refs = index_claims(fx.extractions())
    assert [r.global_id for r in refs] == [1, 2, 3, 4, 5, 6]
    assert [r.source for r in refs[:4]] == [fx.SLUG_A] * 3 + [fx.SLUG_B]
    assert refs[3].index == 0


def test_merge_plans_unions_claim_ids_of_an_equal_slug():
    merged = merge_plans([ConceptPlan(slug="kael", title="Kael", kind_detail="concept", claim_ids=[1, 2]),
                          ConceptPlan(slug="kael", title="Kael", kind_detail="concept", claim_ids=[2, 7],
                                      existing_slug="kael-system")])
    assert len(merged) == 1
    assert merged[0].claim_ids == [1, 2, 7] and merged[0].existing_slug == "kael-system"


def test_a_digest_longer_than_the_cap_is_planned_in_slices():
    claim = Claim(text="Kael ist ein System.", kind="definition",
                  citation=Citation(file=fx.FILE_A, start_line=2, end_line=2, quote="Kael ist ein System."))
    many = {fx.FILE_A: [claim] * (MAX_DIGEST_CLAIMS + 1), fx.FILE_B: []}
    calls: list[str] = []
    run(calls, plans=[], claims=many)
    assert calls.count("plan") == 2


def test_extractions_carry_their_source_slug_and_title():
    compiled = run([])
    first: Extraction = compiled.extractions[0]
    assert first.source == fx.SLUG_A and first.title == "Notiz A zum System Kael"
    assert first.triage.tier == "T3-work"


def test_citation_without_a_quote_still_constructs():
    assert Citation(file=fx.FILE_A, start_line=1, end_line=1).quote == ""
