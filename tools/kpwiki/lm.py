"""LM configuration for kpwiki programs.

Three roles, all overridable through the environment so that no model id is
hard-coded in a program:

    KP_LM_TASK        the model that runs the programs        (default: anthropic/claude-opus-5)
    KP_LM_WORKER      cheap model for bulk sub-steps / judges (default: anthropic/claude-haiku-4-5)
    KP_LM_REFLECTION  GEPA's reflection model, temperature 1  (default: anthropic/claude-opus-5)

``configure(role)`` is process-global (call once at startup); ``lm_context(role)``
scopes a different model to a ``with`` block and is safe under threads.
    DSPY_CACHEDIR     on-disk LM cache (default: .cache/dspy, git-ignored)

Model strings follow DSPy/LiteLLM ``provider/model`` form; the Anthropic
provider reads ANTHROPIC_API_KEY. Constructing a ``dspy.LM`` does not hit the
network, so ``configure()`` is safe in dry runs and tests.
"""
from __future__ import annotations

import os
from pathlib import Path

import dspy

DEFAULT_MODELS = {
    "task": "anthropic/claude-opus-5",
    "worker": "anthropic/claude-haiku-4-5",
    "reflection": "anthropic/claude-opus-5",
}
ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CACHE_DIR = ROOT / ".cache" / "dspy"
REFLECTION_MAX_TOKENS = 32000
TASK_MAX_TOKENS = 16000


def model_id(role: str) -> str:
    """Return the configured model string for ``task``, ``worker`` or ``reflection``."""
    if role not in DEFAULT_MODELS:
        raise ValueError(f"unknown LM role {role!r}; expected one of {sorted(DEFAULT_MODELS)}")
    return os.environ.get(f"KP_LM_{role.upper()}", DEFAULT_MODELS[role])


def build_lm(role: str) -> dspy.LM:
    """Build the ``dspy.LM`` for a role (no network call until first use)."""
    if role == "reflection":
        return dspy.LM(model_id(role), temperature=1.0, max_tokens=REFLECTION_MAX_TOKENS)
    return dspy.LM(model_id(role), temperature=0.0, max_tokens=TASK_MAX_TOKENS)


def ensure_cache_dir() -> Path:
    """Point DSPy's disk cache at a repo-local, git-ignored directory."""
    cache_dir = Path(os.environ.get("DSPY_CACHEDIR", DEFAULT_CACHE_DIR))
    # The cache stores prompts and completions, i.e. source text: owner-only,
    # also when the directory already existed with wider permissions.
    cache_dir.mkdir(parents=True, exist_ok=True)
    os.chmod(cache_dir, 0o700)
    os.environ.setdefault("DSPY_CACHEDIR", str(cache_dir))
    return cache_dir


def configure(role: str = "task") -> dspy.LM:
    """Configure DSPy process-wide with the LM for ``role`` and return it.

    ``dspy.configure`` sets global state: call it once at process start, from
    the main thread. Inside a running program (workers, judges, threads) use
    :func:`lm_context` instead, which scopes the override to a ``with`` block.
    """
    ensure_cache_dir()
    lm = build_lm(role)
    dspy.configure(lm=lm, track_usage=True)
    return lm


def lm_context(role: str):
    """Thread-safe, scoped LM override: ``with lm_context("worker"): ...``."""
    return dspy.context(lm=build_lm(role))
