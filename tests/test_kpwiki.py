"""Offline tests for the kpwiki DSPy base (skip when dspy is not installed)."""
from __future__ import annotations

import pytest

dspy = pytest.importorskip("dspy")

from tools.kpwiki import lm, smoke  # noqa: E402
from tools.kpwiki.metrics import ingest_metric  # noqa: E402
from tools.kpwiki.programs import SourceIngest, number_lines  # noqa: E402
from tools.kpwiki.schema import Citation, Claim  # noqa: E402


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
