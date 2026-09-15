"""Offline tests for the kpwiki DSPy base (skip when dspy is not installed)."""
from __future__ import annotations

import pytest

dspy = pytest.importorskip("dspy")

from tools.kpwiki import lm, smoke  # noqa: E402
from tools.kpwiki.metrics import ingest_metric, language_kept, looks_german  # noqa: E402
from tools.kpwiki.programs import SourceIngest, number_lines  # noqa: E402
from tools.kpwiki.schema import Citation, Claim  # noqa: E402
from pydantic import ValidationError  # noqa: E402


def test_model_roles_come_from_env(monkeypatch):
    monkeypatch.setenv("KP_LM_TASK", "anthropic/claude-sonnet-5")
    assert lm.model_id("task") == "anthropic/claude-sonnet-5"
    assert lm.model_id("worker") == lm.DEFAULT_MODELS["worker"]
    with pytest.raises(ValueError):
        lm.model_id("judge")


def test_program_has_named_predictors():
    names = [name for name, _ in SourceIngest().named_predictors()]
    assert names == ["triage.predict", "extract", "conflicts.predict"]


def test_number_lines_is_one_based():
    assert number_lines("a\nb").splitlines() == ["0001| a", "0002| b"]


def test_metric_accepts_grounded_claims():
    result = ingest_metric(smoke.fixture_example(), smoke.handmade_prediction())
    assert result.score > 0.99
    assert "All claims" in result.feedback


def test_metric_penalises_bad_citation_and_translation():
    bad = Claim(text="AEGIS is never named in act one.", kind="rule",
                citation=Citation(file=smoke.FIXTURE_FILE, start_line=40, end_line=41))
    result = ingest_metric(smoke.fixture_example(), dspy.Prediction(claims=[bad]))
    assert result.score < 0.5
    assert "outside the numbered body" in result.feedback
    assert "translated" in result.feedback


def test_metric_returns_prediction_not_dict():
    result = ingest_metric(smoke.fixture_example(), dspy.Prediction(claims=[]))
    assert isinstance(result, dspy.Prediction)
    assert "No claims" in result.feedback


def test_dry_run_passes(capsys):
    assert smoke.main(["--dry-run"]) == 0
    assert "OK: kpwiki dry run passed" in capsys.readouterr().out


def test_metric_scores_malformed_claims_instead_of_raising():
    good = smoke.handmade_prediction().claims[0]
    pred = dspy.Prediction(claims=[good, {"text": "kaputt"}, "not a claim"])
    result = ingest_metric(smoke.fixture_example(), pred)
    assert 0.0 < result.score < 1.0
    assert "did not fit the Claim schema" in result.feedback


def test_language_detection_needs_a_german_marker():
    assert not looks_german("KW1 KW4 AEGIS")            # no markers: unknown, not German
    assert not looks_german("Kael is the system")       # English majority
    assert looks_german("Das System ist Kael")
    neutral = Claim(text="KW1 → KW4", kind="world",
                    citation=Citation(file=smoke.FIXTURE_FILE, start_line=3, end_line=3))
    assert language_kept([neutral], source_is_german=True) == 1.0


def test_slugs_never_collide_with_suffixed_titles():
    from scripts.source_inventory import disambiguate_slugs
    records = [{"slug": "foo"}, {"slug": "foo"}, {"slug": "foo-2"}, {"slug": "foo"}]
    disambiguate_slugs(records)
    slugs = [r["slug"] for r in records]
    assert len(set(slugs)) == 4 and slugs[0] == "foo" and "foo-2" in slugs


def test_citation_rejects_inverted_range():
    with pytest.raises(ValidationError):
        Citation(file=smoke.FIXTURE_FILE, start_line=5, end_line=3)
    assert Citation(file=smoke.FIXTURE_FILE, start_line=3, end_line=3).marker().endswith(":3-3]")


def test_suffixed_slugs_respect_the_length_limit():
    from scripts.source_inventory import SLUG_MAX, disambiguate_slugs, slugify
    long_title = "x" * 80
    records = [{"slug": slugify(long_title)}, {"slug": slugify(long_title)}]
    disambiguate_slugs(records)
    assert all(len(r["slug"]) <= SLUG_MAX for r in records) and records[1]["slug"].endswith("-2")


def test_lm_context_is_scoped(monkeypatch):
    monkeypatch.setenv("KP_LM_WORKER", "anthropic/claude-haiku-4-5")
    with lm.lm_context("worker"):
        assert dspy.settings.lm.model == "anthropic/claude-haiku-4-5"
