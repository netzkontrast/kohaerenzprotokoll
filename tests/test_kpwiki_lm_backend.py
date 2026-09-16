"""Backend selection for kpwiki LMs: API (LiteLLM) vs the local Claude CLI (dspy-local)."""
from __future__ import annotations

import pytest

dspy = pytest.importorskip("dspy")

from tools.kpwiki import lm  # noqa: E402
from tools.kpwiki.local_lm import ClaudeLM, build_prompt  # noqa: E402


def _no_claude(monkeypatch):
    monkeypatch.setattr(lm.shutil, "which", lambda name: None)


def _with_claude(monkeypatch):
    monkeypatch.setattr(lm.shutil, "which", lambda name: "/usr/bin/claude" if name == "claude" else None)


def test_auto_prefers_api_when_key_is_set(monkeypatch):
    monkeypatch.delenv("KP_LM_BACKEND", raising=False)
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")
    _with_claude(monkeypatch)
    assert lm.backend() == "api"


def test_auto_falls_back_to_cli_without_key(monkeypatch):
    monkeypatch.delenv("KP_LM_BACKEND", raising=False)
    monkeypatch.delenv("ANTHROPIC_API_KEY", raising=False)
    _with_claude(monkeypatch)
    assert lm.backend() == "claude-cli"
    _no_claude(monkeypatch)
    assert lm.backend() == "api"


def test_explicit_backend_wins_and_unknown_is_rejected(monkeypatch):
    monkeypatch.setenv("ANTHROPIC_API_KEY", "sk-test")
    monkeypatch.setenv("KP_LM_BACKEND", "claude-cli")
    assert lm.backend() == "claude-cli"
    monkeypatch.setenv("KP_LM_BACKEND", "ollama")
    with pytest.raises(ValueError):
        lm.backend()


def test_cli_roles_map_to_claude_aliases(monkeypatch):
    monkeypatch.setenv("KP_LM_BACKEND", "claude-cli")
    assert lm.model_id("worker") == "claude/haiku"
    monkeypatch.setenv("KP_LM_CLI_WORKER", "claude/sonnet")
    assert lm.model_id("worker") == "claude/sonnet"
    # API-side overrides never leak into the CLI backend, and the user is told so.
    monkeypatch.setenv("KP_LM_TASK", "anthropic/claude-sonnet-5")
    with pytest.warns(RuntimeWarning, match="KP_LM_TASK.*ignored"):
        assert lm.model_id("task") == "claude/opus"


def test_cli_lm_is_built_without_spawning_and_strips_sampling_kwargs(monkeypatch):
    monkeypatch.setenv("KP_LM_BACKEND", "claude-cli")
    built = lm.build_lm("reflection")
    assert isinstance(built, ClaudeLM)
    assert built.cache is False
    assert "temperature" not in built.kwargs and "max_tokens" not in built.kwargs
    copied = built.copy(rollout_id=3, temperature=0.9)
    assert isinstance(copied, ClaudeLM)
    assert "rollout_id" not in copied.kwargs and "temperature" not in copied.kwargs


def test_cli_lm_falls_back_to_default_timeout(monkeypatch):
    monkeypatch.setenv("KP_LM_BACKEND", "claude-cli")
    built = lm.build_lm("worker")
    assert built._prepare_call(prompt="x", messages=None, kwargs={}).timeout_seconds == lm.CLI_TIMEOUT_SECONDS
    stripped = built.copy(timeout_seconds=None)
    assert "timeout_seconds" not in stripped.kwargs
    from tools.kpwiki.local_lm import DEFAULT_TIMEOUT_SECONDS
    assert stripped._prepare_call(prompt="x", messages=None, kwargs={}).timeout_seconds == DEFAULT_TIMEOUT_SECONDS


def test_cli_lm_refuses_cache(monkeypatch):
    with pytest.raises(ValueError):
        ClaudeLM("claude/haiku", repo_root=lm.ROOT, cache=True)


def test_prompt_builder_splits_system_from_user_turns():
    parts = build_prompt(messages=[{"role": "system", "content": "Antworte auf Deutsch."},
                                   {"role": "user", "content": "Wer ist Juna?"}])
    assert parts.system == "Antworte auf Deutsch."
    assert "Wer ist Juna?" in parts.prompt


def test_cli_timeout_is_env_configurable(monkeypatch):
    monkeypatch.setenv("KP_LM_BACKEND", "claude-cli")
    monkeypatch.setenv("KP_LM_CLI_TIMEOUT", "900")
    assert lm.build_lm("task")._prepare_call(prompt="x", messages=None, kwargs={}).timeout_seconds == 900
