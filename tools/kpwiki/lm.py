"""LM configuration for kpwiki programs.

Three roles, all overridable through the environment so that no model id is
hard-coded in a program:

    KP_LM_TASK        the model that runs the programs        (default: anthropic/claude-opus-5)
    KP_LM_WORKER      cheap model for bulk sub-steps / judges (default: anthropic/claude-haiku-4-5)
    KP_LM_REFLECTION  GEPA's reflection model, temperature 1  (default: anthropic/claude-opus-5)

Two backends (``KP_LM_BACKEND``):

    api          ``dspy.LM`` over LiteLLM. Model strings are ``provider/model``,
                 so any LiteLLM provider works: ``anthropic/…`` reads
                 ANTHROPIC_API_KEY, ``openrouter/…`` reads OPENROUTER_API_KEY.
    claude-cli   ``ClaudeLM`` (tools/kpwiki/local_lm.py, from Hmbown/dspy-local):
                 every call runs ``claude -p`` on the Claude Code subscription,
                 no API key. Role models are ``claude/<alias>`` (KP_LM_CLI_TASK,
                 KP_LM_CLI_WORKER, KP_LM_CLI_REFLECTION).
    auto         (default) ``api`` when any key in ``API_KEY_ENV`` is set, else
                 ``claude-cli`` when a ``claude`` binary is on PATH, else ``api``
                 (so a missing key fails at first call, loudly, not at import).

Mixing providers across roles is supported and is the cheap configuration: a
strong ``task``/``reflection`` model with a cheap ``worker`` costs less than one
model everywhere, and the three roles are resolved independently.

``KP_LM_CLI_LOG`` (default ``.cache/kpwiki/cli.log``) receives one line per call
start, progress (every 5 s) and end, with elapsed time and tokens; ``KP_LM_CLI_CWD``
(default a scratch directory under the system temp dir) is the CLI's working
directory, kept outside the repo so no project hook runs per call.
``KP_LM_CLI_TIMEOUT`` (seconds, default 1800) bounds one CLI call; a stage that
returns a large typed object on ``claude/opus`` was measured above 300 s, so the
default is generous and a run is bounded by its caller, not by this value.
The CLI backend strips ``temperature``, ``max_tokens`` and ``rollout_id`` (the
CLI does not expose them) and must run with ``cache=False``; programs that
rely on ``lm.copy(rollout_id=…)`` for diversity (TetraFrame corners) get it
from the prompt contracts alone there — see docs/dspy-base.md "Local runtime".

``configure(role)`` is process-global (call once at startup); ``lm_context(role)``
scopes a different model to a ``with`` block and is safe under threads.
    DSPY_CACHEDIR     on-disk LM cache (default: .cache/dspy, git-ignored)

Constructing an LM of either backend does not hit the network or spawn a
process, so ``configure()`` is safe in dry runs and tests.
"""
from __future__ import annotations

import os
import shutil
import tempfile
import warnings
from pathlib import Path

import dspy

DEFAULT_MODELS = {
    "task": "anthropic/claude-opus-5",
    "worker": "anthropic/claude-haiku-4-5",
    "reflection": "anthropic/claude-opus-5",
}
DEFAULT_CLI_MODELS = {
    "task": "claude/opus",
    "worker": "claude/haiku",
    "reflection": "claude/opus",
}
BACKENDS = ("api", "claude-cli", "auto")
# The key each LiteLLM provider prefix reads. A provider absent here is still
# usable — it is simply not a signal for `auto` and gets no missing-key warning.
PROVIDER_KEY_ENV = {
    "anthropic": "ANTHROPIC_API_KEY",
    "openrouter": "OPENROUTER_API_KEY",
}
API_KEY_ENV = tuple(PROVIDER_KEY_ENV.values())
ROOT = Path(__file__).resolve().parents[2]
DEFAULT_CACHE_DIR = ROOT / ".cache" / "dspy"
REFLECTION_MAX_TOKENS = 32000
TASK_MAX_TOKENS = 16000
CLI_TIMEOUT_SECONDS = 1800         # 30 min per CLI call by default; KP_LM_CLI_TIMEOUT overrides


def _check_role(role: str) -> None:
    if role not in DEFAULT_MODELS:
        raise ValueError(f"unknown LM role {role!r}; expected one of {sorted(DEFAULT_MODELS)}")


def backend() -> str:
    """Resolve ``KP_LM_BACKEND`` (``api`` | ``claude-cli`` | ``auto``) to a concrete backend."""
    chosen = os.environ.get("KP_LM_BACKEND", "auto")
    if chosen not in BACKENDS:
        raise ValueError(f"unknown KP_LM_BACKEND {chosen!r}; expected one of {BACKENDS}")
    if chosen != "auto":
        return chosen
    if any(os.environ.get(name) for name in API_KEY_ENV):
        return "api"
    return "claude-cli" if shutil.which("claude") else "api"


def model_id(role: str) -> str:
    """Return the configured model string for ``task``, ``worker`` or ``reflection``."""
    _check_role(role)
    if backend() == "claude-cli":
        _warn_ignored_api_overrides()
        return os.environ.get(f"KP_LM_CLI_{role.upper()}", DEFAULT_CLI_MODELS[role])
    return os.environ.get(f"KP_LM_{role.upper()}", DEFAULT_MODELS[role])


def _warn_ignored_api_overrides() -> None:
    """KP_LM_* names API models; say so once when the CLI backend is the one running."""
    ignored = [f"KP_LM_{r.upper()}" for r in DEFAULT_MODELS if os.environ.get(f"KP_LM_{r.upper()}")]
    if ignored:
        warnings.warn(
            f"{ignored} are API-backend overrides and are ignored while KP_LM_BACKEND resolves to "
            "'claude-cli'; set KP_LM_CLI_TASK / KP_LM_CLI_WORKER / KP_LM_CLI_REFLECTION (claude/<alias>) "
            "or export ANTHROPIC_API_KEY to use the API backend.",
            RuntimeWarning, stacklevel=3)


def _warn_missing_provider_key(role: str, model: str) -> None:
    """Name the key a role's provider needs while the role is still changeable."""
    key = PROVIDER_KEY_ENV.get(model.split("/", 1)[0])
    if key and not os.environ.get(key):
        warnings.warn(
            f"LM role {role!r} resolves to {model!r}, whose provider reads {key} — and {key} is "
            f"not set. Export it, or point KP_LM_{role.upper()} at a provider you hold a key for.",
            RuntimeWarning, stacklevel=4)


def _build_api_lm(role: str) -> dspy.LM:
    model = model_id(role)
    _warn_missing_provider_key(role, model)
    if role == "reflection":
        return dspy.LM(model, temperature=1.0, max_tokens=REFLECTION_MAX_TOKENS)
    return dspy.LM(model, temperature=0.0, max_tokens=TASK_MAX_TOKENS)


def _build_cli_lm(role: str) -> dspy.LM:
    from tools.kpwiki.local_lm import ClaudeLM

    # No temperature / max_tokens: the CLI rejects them; cache must stay off
    # because the CLI has no deterministic sampling to cache against.
    timeout = int(os.environ.get("KP_LM_CLI_TIMEOUT", CLI_TIMEOUT_SECONDS))
    # The CLI runs in a scratch directory outside the repo so the repo's SessionStart
    # hooks do not fire on every call; HOME is isolated by ClaudeLM itself.
    cwd = Path(os.environ.get("KP_LM_CLI_CWD") or Path(tempfile.gettempdir()) / "kpwiki-cli-cwd")
    cwd.mkdir(parents=True, exist_ok=True)
    log_path = os.environ.get("KP_LM_CLI_LOG") or str(ROOT / ".cache" / "kpwiki" / "cli.log")
    return ClaudeLM(model_id(role), repo_root=cwd, timeout_seconds=timeout, cache=False, log_path=log_path)


def build_lm(role: str) -> dspy.LM:
    """Build the LM for a role on the resolved backend (no network call until first use)."""
    _check_role(role)
    if backend() == "claude-cli":
        return _build_cli_lm(role)
    return _build_api_lm(role)


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
