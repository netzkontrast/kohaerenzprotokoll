"""Offline tests for the clarify gate (skip when dspy is not installed)."""
from __future__ import annotations

import pytest

dspy = pytest.importorskip("dspy")

from tools.kpwiki.clarify import Ambiguity, Binding, Clarification, ClarifyGate, Scope, may_propose_promotion  # noqa: E402
from tools.kpwiki.clarify_metric import clarify_metric  # noqa: E402

GOLD = dspy.Example(
    claim_text="AEGIS wird meist nicht beim Namen genannt.",
    source_excerpt="AEGIS wird in Akt I nicht beim Namen genannt.",
    entities=["AEGIS"], glossary_terms="aegis, kael, kw1, kw3", canon_context="",
).with_inputs("claim_text", "source_excerpt", "entities", "glossary_terms", "canon_context")


def _pred(**kw) -> dspy.Prediction:
    return dspy.Prediction(clarification=Clarification(**kw))


def test_grounded_rewrite_scores_full():
    pred = _pred(clarified_text="AEGIS wird in Akt I nicht beim Namen genannt.", scope=Scope(act="Akt I"),
                 bindings=[Binding(mention="AEGIS", slug="aegis")], verdict="clear")
    result = clarify_metric(GOLD, pred)
    assert result.score > 0.99 and may_propose_promotion(pred.clarification)


def test_asking_scores_as_high_as_resolving():
    pred = _pred(clarified_text="AEGIS wird meist nicht beim Namen genannt.",
                 bindings=[Binding(mention="AEGIS", slug="aegis")],
                 ambiguities=[Ambiguity(phrase="meist", readings=["nur in Akt I", "im ganzen Roman selten"],
                                        question="Gilt 'meist' für Akt I oder den ganzen Roman?")],
                 verdict="needs-author")
    assert clarify_metric(GOLD, pred).score > 0.99
    assert not may_propose_promotion(pred.clarification)


def test_bolder_rewrite_is_penalised_with_named_blame():
    pred = _pred(clarified_text="AEGIS wird meist in KW3 nie beim Namen genannt.", scope=Scope(world="KW3"),
                 bindings=[Binding(mention="AEGIS", slug="aegis-core")], verdict="clear")
    result = clarify_metric(GOLD, pred)
    assert result.score < 0.5
    for blame in ("kw3", "nie", "KW3", "meist", "aegis-core"):
        assert blame in result.feedback


def test_translation_and_inconsistent_verdict_are_penalised():
    pred = _pred(clarified_text="AEGIS is not named in act one.",
                 ambiguities=[Ambiguity(phrase="meist", readings=["a", "b"], question="which")], verdict="clear")
    result = clarify_metric(GOLD, pred)
    assert "translated" in result.feedback and "without a question" in result.feedback
    assert "inconsistent" in result.feedback


def test_missing_clarification_scores_zero():
    assert clarify_metric(GOLD, dspy.Prediction(clarification="nope")).score == 0.0


def test_gate_has_one_named_predictor():
    assert [n for n, _ in ClarifyGate().named_predictors()] == ["clarify.predict"]


def test_entity_check_matches_whole_words_only():
    from tools.kpwiki.clarify_metric import mentions

    assert mentions("Junas Haus in KW2.", "Juna")            # German inflection suffix
    assert mentions("die Kernwelten", "Kernwelt")
    assert not mentions("die Kernwelt", "Kern")               # substring is not a mention
    assert not mentions("Sektor KW20", "KW2")
    gold = dspy.Example(claim_text="Der Kern bleibt.", source_excerpt="Der Kern der Kernwelt bleibt.",
                        entities=["Kern"], glossary_terms="", canon_context="").with_inputs("claim_text")
    pred = dspy.Prediction(clarification=Clarification(clarified_text="Die Kernwelt bleibt.", verdict="clear"))
    result = clarify_metric(gold, pred)
    assert result.score < 1.0 and "Dropped entities: ['Kern']" in result.feedback


def test_cli_refuses_sources_outside_the_repo():
    from tools.kpwiki.clarify_cli import ROOT, resolve_source

    assert resolve_source("CLAUDE.md") == ROOT / "CLAUDE.md"
    for bad in ("/etc/hostname", "../CLAUDE.md", str(ROOT.parent / "x.md")):
        with pytest.raises(SystemExit):
            resolve_source(bad)
