#!/usr/bin/env python3
"""Spawn and drive a Google Jules session — a remote coding agent that works on a GitHub repository.

Ported on 2026-09-26 from `netzkontrast/agency`, `agency/capabilities/jules/`:
the REST client (`api.py`), the dispatch preamble and its tool lint
(`preambles.py`), the `verify` verb (`_main.py`), and the watcher's reading of a
state (`watch.py` `_classify`) as the one-shot `triage`. Rewritten
standard-library (`urllib` for `httpx`, `git ls-remote` for agency's VCS
boundary), because every other script here runs on the system interpreter. Not
ported: the watcher's poll loop and event queue, the probe-and-recover cycle,
the patch-to-GitHub-MCP planner (`patch.py`), aliases in agency's graph, and
bulk plan approval — each needs a long-lived process or a graph this repository
does not have. `.agents/skills/jules/references/agency.md` maps each piece.

Three guards are code, not prose (P1):

- **Approval.** `dispatch` and `message` send text to Google, and a session
  clones the whole repository, corpus included. Each refuses without
  `--approval` naming the author's decision, the rule `lmrun.py` keeps for
  models. Nothing here decides that the author has said yes.
- **The tools are named.** Jules publishes work only through its `submit` tool;
  a prompt that says "open a PR" in prose can end COMPLETED with the work still
  in its VM. `dispatch` prepends a preamble naming every canonical tool and
  refuses a final prompt that does not (`lint`).
- **COMPLETED is not done.** `verify` asks `git ls-remote` whether the branch
  exists on the remote, and any lookup error reads as not done.

Every effect — dispatch, message, plan approval — is a line in
`Plan/runs/jules/ledger.jsonl`, with the full prompt and the approval, answered
or refused.

    python3 scripts/jules.py sources                    # repositories Jules can reach
    python3 scripts/jules.py dispatch --prompt-file P --branch main --title T --approval "…" [--dry-run]
    python3 scripts/jules.py status <session>           # state, url, pull requests
    python3 scripts/jules.py list [--page-size N]
    python3 scripts/jules.py activities <session> [--kinds planGenerated,agentMessaged] [--full]
    python3 scripts/jules.py plan <session>             # the plan waiting for approval
    python3 scripts/jules.py approve <session>          # approve it; that state times out
    python3 scripts/jules.py message <session> --prompt-file P --approval "…"
    python3 scripts/jules.py triage <session>           # what its state means, and what to do next
    python3 scripts/jules.py patch <session> [--out DIR] # size of each diff; --out writes the bodies
    python3 scripts/jules.py verify --state COMPLETED --branch B
    python3 scripts/jules.py lint --prompt-file P       # does it name every canonical tool?
    python3 scripts/jules.py preamble [--source owner/repo] [--scope PATHS]
    python3 scripts/jules.py selftest                   # offline: no key, no network

`JULES_API_KEY` comes from the environment's settings, never a file here or the
chat; `JULES_API_BASE_URL` overrides `https://jules.googleapis.com`.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
import tempfile
import urllib.error
import urllib.parse
import urllib.request
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
LEDGER = ROOT / "Plan" / "runs" / "jules" / "ledger.jsonl"
BASE_URL = os.environ.get("JULES_API_BASE_URL", "https://jules.googleapis.com")

# The repository whose doctrine a session is told to read first. A session on
# any other source gets the tool preamble without it (agency's Mode B cloned its
# own docs read-only into foreign repos; nothing here needs that yet).
SELF_SOURCE = "netzkontrast/kohaerenzprotokoll"


class JulesAPIError(RuntimeError):
    """Non-2xx from the Jules REST API; carries the HTTP status code."""

    def __init__(self, status: int, message: str, body: str = ""):
        super().__init__(message)
        self.status = status
        self.body = body


class Refused(RuntimeError):
    """A call this module will not make: no approval, or a prompt that names too few tools."""


# ── transport ────────────────────────────────────────────────────────────────

def _api_key() -> str:
    # The value is auth material: it goes into the request header and nowhere
    # else — never a ledger line, never a printed result.
    key = os.environ.get("JULES_API_KEY", "")
    if not key:
        raise RuntimeError("JULES_API_KEY is not set. It belongs in the environment's settings "
                           "(never a file in this repository or the chat); a session started "
                           "after it is set inherits it.")
    return key


def _http(method: str, url: str, headers: dict, data: bytes | None) -> tuple[int, str]:
    req = urllib.request.Request(url, data=data, method=method, headers=headers)
    try:
        with urllib.request.urlopen(req, timeout=60) as resp:
            return resp.status, resp.read().decode("utf-8")
    except urllib.error.HTTPError as exc:
        return exc.code, exc.read().decode("utf-8", "replace")


SEND = _http   # the selftest replaces this; nothing else does


def _translate_http_error(code: int, body: str) -> str:
    mapping = {
        400: "400 Bad Request — malformed payload. Body: ",
        401: "401 Unauthorized — JULES_API_KEY rejected.",
        403: "403 Permission Denied — Jules cannot access the source. Connect the GitHub repo via the Jules GitHub app.",
        404: "404 Not Found — resource does not exist.",
        405: "405 Method Not Allowed — endpoint exists but does not accept this verb.",
        409: "409 Conflict — illegal state transition. Check current session state first.",
        429: "429 Quota Exceeded — pause polling and check billing/quota.",
    }
    if 500 <= code < 600:
        return f"5xx Server Error ({code}) — retryable. Body: {body}"
    base = mapping.get(code, f"HTTP {code}")
    return base + body if code == 400 and body else base


def _request(method: str, path: str, body: dict | None = None, params: dict | None = None) -> dict:
    headers = {"x-goog-api-key": _api_key(), "Content-Type": "application/json"}
    url = BASE_URL + path + ("?" + urllib.parse.urlencode(params) if params else "")
    data = json.dumps(body).encode("utf-8") if body is not None else None
    status, text = SEND(method, url, headers, data)
    if status >= 400:
        raise JulesAPIError(status, _translate_http_error(status, text), text)
    return json.loads(text) if text else {}


def _paginate(path: str, params: dict, max_pages: int | None = None) -> list[dict]:
    """Walk to exhaustion. A repeated nextPageToken is the only other stop, so an
    API that returns the same token forever cannot loop unboundedly."""
    items: list[dict] = []
    token = ""
    seen: set[str] = set()
    key: str | None = None
    while True:
        q = dict(params)
        if token:
            q["pageToken"] = token
        raw = _request("GET", path, params=q)
        if key is None:
            key = next((k for k, v in raw.items() if isinstance(v, list)), None)
            if key is None:
                break
        items.extend(raw.get(key) or [])
        token = raw.get("nextPageToken", "")
        if not token or token in seen:
            break
        seen.add(token)
        if max_pages is not None and len(seen) >= max_pages:
            break
    return items


# ── sources ──────────────────────────────────────────────────────────────────

def short_id(name_or_id: str) -> str:
    """Accept 'sessions/123' or '123' and return '123'."""
    return name_or_id.rsplit("/", 1)[-1]


def sources() -> list[dict]:
    """Every repository connected to Jules, as {source, owner, repo, branch}."""
    out = []
    for s in _paginate("/v1alpha/sources", {"pageSize": 100}):
        gh = s.get("githubRepo") or {}
        out.append({"source": s.get("name", ""), "owner": gh.get("owner", ""), "repo": gh.get("repo", ""),
                    "default_branch": (gh.get("defaultBranch") or {}).get("displayName", "")})
    return out


def resolve_source(owner: str, repo: str) -> str:
    """owner/repo → its `sources/…` name. The composition is undocumented, so the direct
    name is asked first — `sources/github/<owner>/<repo>`, 1.2 s on 2026-09-26 — and on a
    404 the listing is walked and matched: 749 sources, 4 minutes, that day."""
    try:
        return _request("GET", f"/v1alpha/sources/github/{owner}/{repo}").get("name") \
            or f"sources/github/{owner}/{repo}"
    except JulesAPIError as exc:
        if exc.status != 404:
            raise
    for s in _paginate("/v1alpha/sources", {"pageSize": 100}):
        gh = s.get("githubRepo") or {}
        if gh.get("owner") == owner and gh.get("repo") == repo:
            return s.get("name", "")
    raise RuntimeError(f"no Jules source connected for github.com/{owner}/{repo}. "
                       "Connect the repository via the Jules GitHub app, then retry.")


def owner_repo(source: str) -> tuple[str, str] | None:
    """'owner/repo', 'sources/github/owner/repo' or a github.com URL → (owner, repo)."""
    s = (source or "").strip()
    if s.startswith("sources/github/"):
        rest = s[len("sources/github/"):]
        return tuple(rest.split("/", 1)) if rest.count("/") == 1 else None  # type: ignore[return-value]
    url = urllib.parse.urlparse(s)
    if url.hostname in ("github.com", "www.github.com"):   # the real host, not a substring
        parts = url.path.strip("/").removesuffix(".git").split("/")
        return (parts[0], parts[1]) if len(parts) >= 2 and all(parts[:2]) else None
    if not url.scheme and s.count("/") == 1 and all(s.split("/")):
        return tuple(s.split("/"))  # type: ignore[return-value]
    return None


def coerce_source(source: str) -> str:
    """Anything a person writes for a repository → the `sources/<id>` Jules expects."""
    s = (source or "").strip()
    if not s:
        raise RuntimeError("source is required ('sources/<id>', 'owner/repo', or a GitHub URL).")
    if s.startswith("sources/") and s.count("/") == 1:
        return s
    pair = owner_repo(s)
    if pair is None:
        raise RuntimeError(f"could not parse source {source!r}.")
    return resolve_source(*pair)


# ── the preamble and its lint ────────────────────────────────────────────────

# The five tools a dispatch prompt must name literally. `submit` is the only
# one that publishes; the rest keep a session from ending silently.
MUST_NAME = ["pre_commit_instructions", "submit", "request_user_input",
             "replace_with_git_merge_diff", "request_code_review"]

TOOLS = (
    "# Dispatch preamble\n"
    "\n"
    "Use these tool symbols literally — prose alone leaves work in the VM:\n"
    "- `pre_commit_instructions()` — mandatory pre-flight before submit.\n"
    "- `submit(branch_name, commit_message, title, description)` — the ONE tool\n"
    "  that publishes work to the remote. Nothing is done until it has run.\n"
    "- `request_user_input(message)` — the blocking ask. Never `message_user`\n"
    "  for a question.\n"
    "- `replace_with_git_merge_diff` — the preferred multi-line edit.\n"
    "- `request_code_review()` — the Jules Critic, before submit.\n"
    "- `reply_to_pr_comments(...)` — when you answer PR review feedback, call it\n"
    "  after `submit(...)` with a one-paragraph summary, or the reviewer does not\n"
    "  see that you pushed.\n"
    "\n"
    "\n"
    "Verify before declaring done: `git ls-remote origin <branch>` is the source\n"
    "of truth — never a local HEAD or a SHA written in chat.\n"
    "\n"
    "If you are blocked, or a push fails, `submit` a branch whose description starts\n"
    "`BLOCKED:` and says why. Never ask in a message and then wait: a session idle\n"
    "on its own question times out and fails. Never write a PR description, notes\n"
    "or a scratch script into a tracked file.\n"
)

DOCTRINE = (
    "\n"
    "# This repository\n"
    "\n"
    "Before drafting any plan, read at the repository root, in this order:\n"
    "- `CLAUDE.md` — the working agreement; a statement in it that is not true of\n"
    "  the repository is a defect to fix in the same change.\n"
    "- `PRINCIPLES.md` — the rules, with the evidence that produced each.\n"
    "- `NOW.md` — what is open, and the questions waiting on the author.\n"
    "\n"
    "Canon prose is German and is never translated. Never write into `Sources/`,\n"
    "and never commit a `Wiki/` page without naming, in the first line of the\n"
    "commit message, the source document the change came from. Where a decision\n"
    "would rest on a guess, ask with `request_user_input` instead.\n"
)


def preamble(source: str, scope: list[str] | None = None) -> str:
    """The text prepended to a dispatch prompt: the tools always, this
    repository's doctrine only when the session works on this repository."""
    text = TOOLS
    if (owner_repo(source) or ()) == tuple(SELF_SOURCE.split("/")):
        text += DOCTRINE
    if scope:
        text += ("\n# Scope\n\nScope is a hard allow-list: " + ", ".join(f"`{p}`" for p in scope) + ".\n"
                 "If you need a path outside it, `submit` a branch whose description starts\n"
                 "`BLOCKED:` and names the paths, and stop. Do not widen the scope silently.\n")
    return text


def assemble(source: str, prompt: str, scope: list[str] | None = None) -> str:
    return f"{preamble(source, scope)}\n---\n{prompt}"


def lint(text: str, must_name: list[str] | None = None) -> dict:
    """Does `text` literally name every canonical tool? {ok, missing}."""
    missing = [t for t in (must_name or MUST_NAME) if t not in text]
    return {"ok": not missing, "missing": missing}


# ── the ledger ───────────────────────────────────────────────────────────────

def record(row: dict) -> None:
    """One line per effect, answered or refused. The prompt is kept whole."""
    LEDGER.parent.mkdir(parents=True, exist_ok=True)
    row = {"at": datetime.now(timezone.utc).isoformat(timespec="seconds"), **row}
    with LEDGER.open("a", encoding="utf-8") as fh:
        fh.write(json.dumps(row, ensure_ascii=False) + "\n")


def _approved(what: str, approval: str | None, row: dict) -> None:
    if not (approval or "").strip():
        record({**row, "status": "refused", "error": "no approval"})
        raise Refused(f"{what} sends text to Google, and a session clones the repository with its corpus. "
                      "Pass --approval naming the author's decision that allows it.")


# ── sessions ─────────────────────────────────────────────────────────────────

def dispatch(prompt: str, source: str, branch: str, *, approval: str | None, title: str = "",
             require_plan_approval: bool = True, auto_pr: bool = False, scope: list[str] | None = None,
             raw: bool = False, dry_run: bool = False) -> dict:
    """Spawn a Jules session. Refused without approval, or when the final prompt names too few tools."""
    text = prompt if raw else assemble(source, prompt, scope)
    row = {"verb": "dispatch", "source": source, "branch": branch, "title": title,
           "require_plan_approval": require_plan_approval, "auto_pr": auto_pr,
           "approval": approval, "prompt_sha256": hashlib.sha256(text.encode()).hexdigest(), "prompt": text}
    if not dry_run:
        _approved("dispatch", approval, row)
    check = lint(text)
    if not check["ok"]:
        if not dry_run:
            record({**row, "status": "refused", "error": f"missing tools: {check['missing']}"})
        raise Refused(f"the prompt does not name {', '.join(check['missing'])}; without `submit` a session "
                      "can end COMPLETED with its work unpublished. Drop --raw or name them.")
    body: dict = {"prompt": text,
                  "sourceContext": {"source": source if dry_run else coerce_source(source),
                                    "githubRepoContext": {"startingBranch": branch}},
                  "requirePlanApproval": bool(require_plan_approval)}
    if title:
        body["title"] = title
    if auto_pr:
        body["automationMode"] = "AUTO_CREATE_PR"
    if dry_run:
        return {"dry_run": True, "body": body}
    try:
        s = _request("POST", "/v1alpha/sessions", body)
    except Exception as exc:
        record({**row, "status": "unreached", "error": str(exc)})
        raise
    sid = s.get("id") or short_id(s.get("name", ""))
    record({**row, "status": "answered", "session": sid, "url": s.get("url", ""), "state": s.get("state", "")})
    return {"session": sid, "state": s.get("state", ""), "url": s.get("url", "")}


def status(session: str) -> dict:
    s = _request("GET", f"/v1alpha/sessions/{short_id(session)}")
    ctx = s.get("sourceContext") or {}
    prs = [(o or {}).get("pullRequest") or {} for o in (s.get("outputs") or [])]
    return {"session": s.get("id") or short_id(s.get("name", "")), "state": s.get("state"),
            "title": s.get("title", ""), "source": ctx.get("source"),
            "branch": (ctx.get("githubRepoContext") or {}).get("startingBranch"),
            "url": s.get("url", ""), "has_outputs": bool(s.get("outputs")),
            "pull_requests": [p["url"] for p in prs if p.get("url")],
            "pushed_branches": [p["headRef"] for p in prs if p.get("headRef")]}


def list_sessions(page_size: int = 20, page_token: str = "") -> dict:
    """One page, trimmed. Pass the returned token back to walk further."""
    q: dict = {"pageSize": max(1, min(page_size, 100))}
    if page_token:
        q["pageToken"] = page_token
    raw = _request("GET", "/v1alpha/sessions", params=q)
    return {"sessions": [{"session": s.get("id") or short_id(s.get("name", "")), "state": s.get("state"),
                          "title": s.get("title", ""), "url": s.get("url", "")}
                         for s in raw.get("sessions") or []],
            "next_page_token": raw.get("nextPageToken", "")}


_ACTIVITY_META = {"name", "id", "createTime", "updateTime", "originator", "description", "artifacts"}
_ACTIVITY_KINDS = ["agentMessaged", "userMessaged", "planGenerated", "planApproved",
                   "progressUpdated", "sessionCompleted", "sessionFailed"]


def activity_kind(a: dict) -> str:
    """A known oneof member first; the first non-meta key only when none matches."""
    for k in _ACTIVITY_KINDS:
        if k in a:
            return k
    return next((k for k in a if k not in _ACTIVITY_META), "unknown")


def activities(session: str, page_size: int = 10, kinds: str = "", page_token: str = "",
               full: bool = False) -> dict:
    """A session's activities, summarised unless `full`. Reads can lag: poll twice before
    trusting a transition."""
    q: dict = {"pageSize": max(1, min(page_size, 100))}
    if page_token:
        q["pageToken"] = page_token
    raw = _request("GET", f"/v1alpha/sessions/{short_id(session)}/activities", params=q)
    wanted = {k.strip() for k in kinds.split(",") if k.strip()}
    out = []
    for a in raw.get("activities") or []:
        kind = activity_kind(a)
        if wanted and kind not in wanted:
            continue
        if full:
            out.append(a)
            continue
        payload = a.get(kind) if isinstance(a.get(kind), dict) else {}
        text = a.get("description") or payload.get("description") or payload.get("message") \
            or payload.get("title") or ""
        out.append({"id": a.get("id") or short_id(a.get("name", "")), "originator": a.get("originator", ""),
                    "kind": kind, "created": a.get("createTime", ""), "summary": str(text)})
    return {"activities": out, "next_page_token": raw.get("nextPageToken", "")}


def plan(session: str, max_pages: int = 5, descriptions: bool = True) -> dict:
    """The newest planGenerated activity. While a session awaits approval no PR exists,
    so this is the only way to see what it intends."""
    best, best_time = None, ""
    for a in _paginate(f"/v1alpha/sessions/{short_id(session)}/activities", {"pageSize": 100},
                       max_pages=max_pages):
        pg = a.get("planGenerated")
        if pg and (best is None or a.get("createTime", "") > best_time):
            best, best_time = pg, a.get("createTime", "")
    if best is None:
        return {"error": "no planGenerated activity found"}
    steps = [{"title": s.get("title", ""), **({"description": s.get("description", "")} if descriptions else {})}
             for s in (best.get("plan") or {}).get("steps") or []]
    return {"steps": steps, "created": best_time}


def approve(session: str) -> dict:
    """Approve the plan. AWAITING_PLAN_APPROVAL is the one state that times out: a plan never
    approved ends COMPLETED with empty outputs."""
    sid = short_id(session)
    _request("POST", f"/v1alpha/sessions/{sid}:approvePlan", body={})
    record({"verb": "approve", "session": sid, "status": "answered"})
    return {"ok": True, "session": sid}


def message(session: str, prompt: str, *, approval: str | None) -> dict:
    """Send a message into a session. Input, not a control plane: poll state afterwards,
    never use it to revive a FAILED session, and there is no cancel."""
    sid = short_id(session)
    row = {"verb": "message", "session": sid, "approval": approval, "prompt": prompt}
    _approved("message", approval, row)
    _request("POST", f"/v1alpha/sessions/{sid}:sendMessage", body={"prompt": prompt})
    record({**row, "status": "answered"})
    return {"ok": True, "session": sid}


def _diff(holder: dict) -> str:
    return (((holder or {}).get("changeSet") or {}).get("gitPatch") or {}).get("unidiffPatch") or ""


def patch(session: str, out: str = "") -> dict:
    """Files, changed lines and bytes of each diff the session holds — never the body on
    stdout. `out` writes each body to `<out>/<session>-<n>.patch` for `git apply`.

    The final diff is an output's `changeSet`; while a session runs, or when it
    finished without one, the newest activity artifact's diff is the one there is.
    Measured on a COMPLETED session, 2026-09-26: the output carried the final
    diff and the pull request, and 17 `progressUpdated` activities one artifact
    each."""
    sid = short_id(session)
    s = _request("GET", f"/v1alpha/sessions/{sid}")
    diffs = [("output", d) for d in (_diff(o) for o in s.get("outputs") or []) if d]
    if not diffs:
        acts = _paginate(f"/v1alpha/sessions/{sid}/activities", {"pageSize": 100}, max_pages=20)
        found = [(a.get("createTime", ""), _diff(art)) for a in acts for art in a.get("artifacts") or []]
        found = [f for f in found if f[1]]
        if found:
            diffs = [("activity", max(found)[1])]
    rows = []
    for n, (where, diff) in enumerate(diffs):
        lines = diff.splitlines()
        row = {"from": where,
               "files": sum(1 for ln in lines if ln.startswith("diff --git ")),
               "lines": sum(1 for ln in lines if ln[:1] in "+-" and not ln.startswith(("+++", "---"))),
               "bytes": len(diff.encode("utf-8"))}
        if out:
            path = Path(out) / f"{sid}-{n}.patch"
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(diff, encoding="utf-8")
            row["written"] = str(path)
        rows.append(row)
    return {"session": sid, "diffs": rows, "files": sum(r["files"] for r in rows)}


# ── COMPLETED is not done ────────────────────────────────────────────────────

def _ls_remote(branch: str, remote: str) -> dict:
    try:
        proc = subprocess.run(["git", "ls-remote", "--heads", remote, branch], cwd=ROOT,
                              capture_output=True, text=True, timeout=60)
    except (OSError, subprocess.TimeoutExpired) as exc:
        return {"ok": False, "detail": str(exc)}
    if proc.returncode != 0:
        return {"ok": False, "detail": proc.stderr.strip()}
    for line in proc.stdout.splitlines():
        sha, _, ref = line.partition("\t")
        if ref == f"refs/heads/{branch}":
            return {"ok": True, "exists": True, "sha": sha}
    return {"ok": True, "exists": False, "sha": ""}


LS_REMOTE = _ls_remote   # the selftest replaces this; nothing else does


def verify(state: str, branch: str, remote: str = "origin") -> dict:
    """done only when the state is COMPLETED and the branch is on the remote. Fail-closed."""
    if not branch:
        return {"done": False, "state": state, "branch_on_remote": False, "error": "branch is required"}
    chk = LS_REMOTE(branch, remote)
    if not chk.get("ok"):
        return {"done": False, "state": state, "branch_on_remote": False,
                "error": f"remote check failed: {chk.get('detail', '')}"}
    on_remote = bool(chk.get("exists"))
    completed = str(state).upper() == "COMPLETED"
    out = {"done": completed and on_remote, "state": state, "branch_on_remote": on_remote, "sha": chk.get("sha", "")}
    if completed and not on_remote:
        out["warning"] = f"{branch!r} is not on {remote} although the session is COMPLETED — a silent fail"
    return out


# ── what a state means ───────────────────────────────────────────────────────

# Ported from agency's watcher (`watch.py` `_classify`) and AGENCY_PROTOCOL §1, as a
# one-shot reading: no previous state, no event queue. COMPLETED alone says nothing —
# it covers an unapproved plan, a pushed branch, work left in the VM, and a no-op.
ACTIONS = {
    "wait": "Working. Poll `status` again; reads lag, so trust a transition only after two polls.",
    "review_and_approve_plan": "A plan waits. Read it with `plan`, then `approve` — or `message` a revision, "
                               "and check the next state is PLANNING, not COMPLETED.",
    "answer_agent_question": "The session asked something. Answer with `message` (it needs --approval); a "
                             "session left waiting on its own question times out and fails.",
    "verify_pr": "The branch is on the remote. Review the pull request against the scope the prompt set.",
    "open_pr": "The branch is on the remote but no pull request is attached: open one for it.",
    "recover_silent_fail": "COMPLETED, a diff exists, no branch on the remote: the work stayed in the VM. "
                           "Probe once with `message` — push and reply with the PR URL, or reply EMPTY — "
                           "and poll. If it stays silent, `patch --out DIR` and apply the diff by hand. "
                           "Never re-dispatch while a diff exists.",
    "dispatch_fresh": "Nothing to recover. Dispatch again with a narrower prompt; `message` cannot revive "
                      "a FAILED session. After two silent fails on one task, do it locally instead.",
    "inspect_and_resume": "PAUSED — often transient while a message is processed. Read `activities`, poll "
                          "twice, and `message` to resume only if it stays paused.",
    "terminal": "CANCELLED. Nothing to do.",
}


def _plan_unapproved(acts: list[dict]) -> bool:
    """A planGenerated with no planApproved and no code change at or after it."""
    generated = max((a.get("createTime", "") for a in acts if "planGenerated" in a), default="")
    if not generated:
        return False
    later = [a for a in acts if a.get("createTime", "") >= generated
             and ("planApproved" in a or "codeChanges" in a or any(_diff(x) for x in a.get("artifacts") or []))]
    return not later


def triage(session: str, branch: str = "") -> dict:
    """What the session's state means, and what to do next."""
    st = status(session)
    state, sid = st["state"], st["session"]
    acts = _paginate(f"/v1alpha/sessions/{sid}/activities", {"pageSize": 100}, max_pages=20)
    evidence: dict = {"url": st["url"], "pull_requests": st["pull_requests"]}
    if state in ("QUEUED", "PLANNING", "IN_PROGRESS", "STATE_UNSPECIFIED"):
        action = "wait"
    elif state == "AWAITING_PLAN_APPROVAL":
        action = "review_and_approve_plan"
    elif state == "AWAITING_USER_FEEDBACK":
        action = "answer_agent_question"
        asked = [a for a in acts if "agentMessaged" in a]
        if asked:
            last = max(asked, key=lambda a: a.get("createTime", ""))
            evidence["agent_message"] = (last.get("agentMessaged") or {}).get("agentMessage", "") \
                or last.get("description", "")
    elif state == "FAILED":
        action = "dispatch_fresh"
    elif state == "PAUSED":
        action = "inspect_and_resume"
    elif state == "CANCELLED":
        action = "terminal"
    elif state == "COMPLETED":
        branch = branch or next(iter(st["pushed_branches"]), "")
        pair = owner_repo(st["source"] or "")
        remote = f"https://github.com/{pair[0]}/{pair[1]}.git" if pair else "origin"
        check = verify(state, branch, remote) if branch else {"branch_on_remote": False}
        files = patch(sid)["files"]
        evidence.update(branch=branch, branch_on_remote=check["branch_on_remote"], patch_files=files)
        if "error" in check and branch:
            evidence["error"] = check["error"]
        if _plan_unapproved(acts):
            action = "review_and_approve_plan"
            evidence["completed_means"] = "the plan was never approved"
        elif check["branch_on_remote"]:
            action = "verify_pr" if st["pull_requests"] else "open_pr"
        elif files:
            action = "recover_silent_fail"
        else:
            action = "dispatch_fresh"
    else:
        action = "wait"
    return {"session": sid, "state": state, "action": action, "instruction": ACTIONS[action],
            "evidence": evidence}


# ── selftest ─────────────────────────────────────────────────────────────────

def selftest() -> int:
    """Offline, no key, no network: each case carries the defect it must name."""
    global SEND, LS_REMOTE, LEDGER
    failures: list[str] = []

    def check(name: str, ok: bool) -> None:
        print(f"  {'ok  ' if ok else 'FAIL'} {name}")
        if not ok:
            failures.append(name)

    sent: list[tuple[str, str, dict | None]] = []
    pages = {
        "/v1alpha/sources": [
            {"sources": [{"name": "sources/1", "githubRepo": {"owner": "a", "repo": "b"}}], "nextPageToken": "p2"},
            {"sources": [{"name": "sources/2", "githubRepo": {"owner": "netzkontrast", "repo": "kohaerenzprotokoll"}}]},
        ],
    }

    def fake(method: str, url: str, headers: dict, data: bytes | None) -> tuple[int, str]:
        parsed = urllib.parse.urlparse(url)
        path, q = parsed.path, urllib.parse.parse_qs(parsed.query)
        body = json.loads(data) if data else None
        sent.append((method, path, body))
        if path == "/v1alpha/sources":
            return 200, json.dumps(pages[path][1 if q.get("pageToken") else 0])
        if path == "/v1alpha/sources/github/o/direct":
            return 200, json.dumps({"name": "sources/github/o/direct"})
        if path == "/v1alpha/loop":
            return 200, json.dumps({"items": [{"n": 1}], "nextPageToken": "same"})
        if path == "/v1alpha/sessions" and method == "POST":
            return 200, json.dumps({"name": "sessions/77", "id": "77", "state": "QUEUED", "url": "https://jules/77"})
        if path == "/v1alpha/sessions/403":
            return 403, "nope"
        if path == "/v1alpha/sessions/77/activities":
            return 200, json.dumps({"activities": [
                {"id": "a1", "createTime": "2026-09-26T10:00:00Z", "description": "old",
                 "planGenerated": {"plan": {"steps": [{"title": "old step"}]}}},
                {"id": "a2", "createTime": "2026-09-26T11:00:00Z", "originator": "agent",
                 "planGenerated": {"plan": {"steps": [{"title": "new step", "description": "d"}]}}},
                {"id": "a3", "createTime": "2026-09-26T11:05:00Z", "artifacts": [], "originator": "agent",
                 "agentMessaged": {"agentMessage": "hi"}, "description": "asks a question"},
            ]})
        if path == "/v1alpha/sessions/77":
            diff = "diff --git a/x b/x\n--- a/x\n+++ b/x\n-old\n+new\n+more\n"
            return 200, json.dumps({"id": "77", "state": "COMPLETED", "sourceContext": {"source": "sources/2"},
                                    "outputs": [{"changeSet": {"gitPatch": {"unidiffPatch": diff}}},
                                                {"pullRequest": {"url": "https://github.com/x/y/pull/1"}}]})
        if path.startswith("/v1alpha/sessions/") and path.split("/")[3] in more:
            sess, acts = more[path.split("/")[3]]
            return 200, json.dumps({"activities": acts} if path.endswith("/activities") else sess)
        return 404, ""

    diff = "diff --git a/x b/x\n--- a/x\n+++ b/x\n-old\n+new\n"
    plan_made = {"createTime": "2026-09-26T10:00:00Z", "planGenerated": {"plan": {"steps": []}}}
    approved = [plan_made, {"createTime": "2026-09-26T10:01:00Z", "planApproved": {}}]
    src = {"source": "sources/github/o/r"}
    more = {
        "88": ({"id": "88", "state": "COMPLETED", "sourceContext": src}, [plan_made]),
        "89": ({"id": "89", "state": "COMPLETED", "sourceContext": src, "outputs": [
            {"changeSet": {"gitPatch": {"unidiffPatch": diff}}},
            {"pullRequest": {"url": "https://github.com/o/r/pull/3", "headRef": "feat"}}]}, approved),
        "90": ({"id": "90", "state": "COMPLETED", "sourceContext": src, "outputs": [
            {"changeSet": {"gitPatch": {"unidiffPatch": diff}}}]}, approved),
        "91": ({"id": "91", "state": "COMPLETED", "sourceContext": src}, approved),
        "92": ({"id": "92", "state": "IN_PROGRESS", "sourceContext": src}, approved + [
            {"createTime": "2026-09-26T10:05:00Z", "progressUpdated": {},
             "artifacts": [{"changeSet": {"gitPatch": {"unidiffPatch": "old"}}}]},
            {"createTime": "2026-09-26T10:09:00Z", "progressUpdated": {},
             "artifacts": [{"changeSet": {"gitPatch": {"unidiffPatch": diff}}}]}]),
        "93": ({"id": "93", "state": "FAILED", "sourceContext": src}, []),
    }

    saved = SEND, LS_REMOTE, LEDGER, os.environ.get("JULES_API_KEY")
    tmp = tempfile.TemporaryDirectory()
    SEND, LEDGER = fake, Path(tmp.name) / "ledger.jsonl"
    os.environ["JULES_API_KEY"] = "selftest"
    try:
        print("sources")
        check("owner/repo on the second page resolves", coerce_source("netzkontrast/kohaerenzprotokoll") == "sources/2")
        check("a github URL with .git resolves", coerce_source("https://github.com/a/b.git") == "sources/1")
        n = len(sent)
        check("the direct name answers without walking the listing",
              coerce_source("o/direct") == "sources/github/o/direct" and len(sent) == n + 1)
        check("sources/<id> passes through unasked", (n := len(sent), coerce_source("sources/9"))[1] == "sources/9"
              and len(sent) == n)
        try:
            coerce_source("https://evil.example/github.com/a/b")
            check("a URL naming github.com in its path is not GitHub", False)
        except RuntimeError as exc:
            check("a URL naming github.com in its path is not GitHub", "could not parse" in str(exc))
        try:
            coerce_source("c/d")
            check("an unconnected repository is named, not guessed", False)
        except RuntimeError as exc:
            check("an unconnected repository is named, not guessed", "github.com/c/d" in str(exc))
        check("a repeated page token stops the walk", len(_paginate("/v1alpha/loop", {})) == 2)

        print("preamble and lint")
        own, other = assemble(SELF_SOURCE, "do x"), assemble("a/b", "do x")
        check("the assembled prompt names every tool", lint(own)["ok"] and lint(other)["ok"])
        check("this repository's doctrine only for this repository", "PRINCIPLES.md" in own
              and "PRINCIPLES.md" not in other)
        check("a prompt without submit is named as missing it", lint("use pre_commit_instructions")["missing"][0] == "submit")
        check("a scope is written as an allow-list, and only when given",
              "allow-list: `Wiki/`" in assemble("a/b", "x", ["Wiki/"]) and "allow-list" not in other)

        print("dispatch")
        n = len(sent)
        try:
            dispatch("do x", SELF_SOURCE, "main", approval=None)
            check("dispatch without approval is refused", False)
        except Refused:
            check("dispatch without approval is refused", len(sent) == n)
        try:
            dispatch("do x", SELF_SOURCE, "main", approval="test", raw=True)
            check("a raw prompt naming no tools is refused", False)
        except Refused as exc:
            check("a raw prompt naming no tools is refused", "submit" in str(exc) and len(sent) == n)
        dry = dispatch("do x", SELF_SOURCE, "main", approval=None, dry_run=True)
        check("a dry run sends nothing and needs no approval", dry["dry_run"] and len(sent) == n)
        out = dispatch("do x", SELF_SOURCE, "main", approval="test", title="t", auto_pr=True)
        post = [b for m, p, b in sent if m == "POST" and p == "/v1alpha/sessions"][-1]
        check("the session is created and its id returned", out["session"] == "77")
        check("the body carries source, branch, gate and automation",
              post["sourceContext"] == {"source": "sources/2", "githubRepoContext": {"startingBranch": "main"}}
              and post["requirePlanApproval"] is True and post["automationMode"] == "AUTO_CREATE_PR")
        plain = dispatch("do x", SELF_SOURCE, "main", approval="test")
        post = [b for m, p, b in sent if m == "POST" and p == "/v1alpha/sessions"][-1]
        check("no automationMode unless asked", plain["session"] == "77" and "automationMode" not in post)
        rows = [json.loads(line) for line in LEDGER.read_text(encoding="utf-8").splitlines()]
        check("the ledger keeps refusals and answers, the prompt whole",
              [r["status"] for r in rows] == ["refused", "refused", "answered", "answered"]
              and rows[2]["prompt"] == post["prompt"] and "selftest" not in LEDGER.read_text())

        print("sessions")
        try:
            status("403")
            check("a 403 names the Jules GitHub app", False)
        except JulesAPIError as exc:
            check("a 403 names the Jules GitHub app", exc.status == 403 and "GitHub app" in str(exc))
        st = status("sessions/77")
        check("status keeps the pull request url", st["pull_requests"] == ["https://github.com/x/y/pull/1"])
        check("status names the pushed branch", status("89")["pushed_branches"] == ["feat"])
        acts = activities("77")["activities"]
        check("a known kind wins over a meta key", acts[2]["kind"] == "agentMessaged")
        check("a filter by kind keeps only that kind",
              [a["id"] for a in activities("77", kinds="agentMessaged")["activities"]] == ["a3"])
        check("the newest plan is the one returned", plan("77")["steps"] == [{"title": "new step", "description": "d"}])
        check("patch counts files and changed lines, no body",
              {k: patch("77")["diffs"][0][k] for k in ("files", "lines")} == {"files": 1, "lines": 3})
        check("while a session runs, the newest activity diff is the patch",
              patch("92")["diffs"] == [{"from": "activity", "files": 1, "lines": 2, "bytes": len(diff)}])
        written = patch("90", out=tmp.name)["diffs"][0]["written"]
        check("--out writes the body to a file, not to stdout", Path(written).read_text() == diff)
        try:
            message("77", "hi", approval="")
            check("a message without approval is refused", False)
        except Refused:
            check("a message without approval is refused", True)

        print("verify")
        LS_REMOTE = lambda b, r: {"ok": True, "exists": False, "sha": ""}  # noqa: E731
        v = verify("COMPLETED", "feature")
        check("COMPLETED with no branch on the remote is not done", not v["done"] and "silent fail" in v["warning"])
        LS_REMOTE = lambda b, r: {"ok": False, "detail": "network"}  # noqa: E731
        check("a failed lookup is not done", not verify("COMPLETED", "feature")["done"])
        LS_REMOTE = lambda b, r: {"ok": True, "exists": True, "sha": "abc"}  # noqa: E731
        check("COMPLETED and on the remote is done", verify("COMPLETED", "feature")["done"])
        check("IN_PROGRESS on the remote is not done", not verify("IN_PROGRESS", "feature")["done"])

        print("triage: what COMPLETED means")
        asked: list[tuple[str, str]] = []
        LS_REMOTE = lambda b, r: (asked.append((b, r)), {"ok": True, "exists": b == "feat", "sha": ""})[1]  # noqa: E731
        check("COMPLETED with a plan never approved is an unapproved plan",
              triage("88")["action"] == "review_and_approve_plan")
        t = triage("89")
        check("COMPLETED with its PR branch on the remote is verify_pr",
              t["action"] == "verify_pr" and t["evidence"]["branch"] == "feat")
        check("the branch is checked on the session's own repository",
              asked[-1] == ("feat", "https://github.com/o/r.git"))
        check("COMPLETED, a diff, no branch is a silent fail, not a fresh dispatch",
              triage("90")["action"] == "recover_silent_fail")
        check("COMPLETED, no diff, no branch is a fresh dispatch", triage("91")["action"] == "dispatch_fresh")
        check("IN_PROGRESS waits", triage("92")["action"] == "wait")
        check("FAILED is a fresh dispatch, never a message", triage("93")["action"] == "dispatch_fresh")

        print("key")
        del os.environ["JULES_API_KEY"]
        n = len(sent)
        try:
            status("77")
            check("no key: refused before anything is sent", False)
        except RuntimeError as exc:
            check("no key: refused before anything is sent", "JULES_API_KEY" in str(exc) and len(sent) == n)
    finally:
        SEND, LS_REMOTE, LEDGER, key = saved
        if key is not None:
            os.environ["JULES_API_KEY"] = key
        tmp.cleanup()

    print(f"\n{'FAILED: ' + ', '.join(failures) if failures else 'held'}")
    return 1 if failures else 0


# ── command line ─────────────────────────────────────────────────────────────

def _read(path: str | None) -> str:
    return sys.stdin.read() if path in (None, "-") else Path(path).read_text(encoding="utf-8")


def main(argv: list[str] | None = None) -> int:
    ap = argparse.ArgumentParser(description=__doc__.split("\n", 1)[0])
    sub = ap.add_subparsers(dest="cmd", required=True)
    sub.add_parser("sources")
    d = sub.add_parser("dispatch")
    d.add_argument("--prompt-file", help="the task; '-' or absent reads stdin")
    d.add_argument("--source", default=SELF_SOURCE)
    d.add_argument("--branch", default="main", help="the starting branch")
    d.add_argument("--title", default="")
    d.add_argument("--approval", help="the author's decision that allows this session")
    d.add_argument("--no-plan-approval", action="store_true", help="start work without a plan gate")
    d.add_argument("--auto-pr", action="store_true", help="automationMode AUTO_CREATE_PR")
    d.add_argument("--scope", default="", help="comma-separated paths the session may touch")
    d.add_argument("--raw", action="store_true", help="no preamble; the prompt must name the tools itself")
    d.add_argument("--dry-run", action="store_true", help="print the request; send nothing")
    for name in ("status", "plan", "approve"):
        sub.add_parser(name).add_argument("session")
    pa = sub.add_parser("patch")
    pa.add_argument("session")
    pa.add_argument("--out", default="", help="write each diff to <out>/<session>-<n>.patch")
    tr = sub.add_parser("triage")
    tr.add_argument("session")
    tr.add_argument("--branch", default="", help="when the session names no pushed branch")
    ls = sub.add_parser("list")
    ls.add_argument("--page-size", type=int, default=20)
    ls.add_argument("--page-token", default="")
    a = sub.add_parser("activities")
    a.add_argument("session")
    a.add_argument("--page-size", type=int, default=10)
    a.add_argument("--kinds", default="")
    a.add_argument("--page-token", default="")
    a.add_argument("--full", action="store_true")
    m = sub.add_parser("message")
    m.add_argument("session")
    m.add_argument("--prompt-file")
    m.add_argument("--approval")
    v = sub.add_parser("verify")
    v.add_argument("--state", required=True)
    v.add_argument("--branch", required=True)
    v.add_argument("--remote", default="origin")
    li = sub.add_parser("lint")
    li.add_argument("--prompt-file")
    p = sub.add_parser("preamble")
    p.add_argument("--source", default=SELF_SOURCE)
    p.add_argument("--scope", default="")
    sub.add_parser("selftest")
    args = ap.parse_args(argv)

    if args.cmd == "selftest":
        return selftest()
    if args.cmd == "preamble":
        print(preamble(args.source, [s for s in args.scope.split(",") if s]))
        return 0
    try:
        if args.cmd == "sources":
            out = sources()
        elif args.cmd == "dispatch":
            out = dispatch(_read(args.prompt_file), args.source, args.branch, approval=args.approval,
                           title=args.title, require_plan_approval=not args.no_plan_approval,
                           auto_pr=args.auto_pr, scope=[s for s in args.scope.split(",") if s],
                           raw=args.raw, dry_run=args.dry_run)
        elif args.cmd == "status":
            out = status(args.session)
        elif args.cmd == "list":
            out = list_sessions(args.page_size, args.page_token)
        elif args.cmd == "activities":
            out = activities(args.session, args.page_size, args.kinds, args.page_token, args.full)
        elif args.cmd == "plan":
            out = plan(args.session)
        elif args.cmd == "approve":
            out = approve(args.session)
        elif args.cmd == "message":
            out = message(args.session, _read(args.prompt_file), approval=args.approval)
        elif args.cmd == "patch":
            out = patch(args.session, args.out)
        elif args.cmd == "triage":
            out = triage(args.session, args.branch)
        elif args.cmd == "verify":
            out = verify(args.state, args.branch, args.remote)
        else:  # lint
            out = lint(_read(args.prompt_file))
    except (Refused, JulesAPIError, RuntimeError) as exc:
        print(f"{type(exc).__name__}: {exc}", file=sys.stderr)
        return 2
    print(json.dumps(out, ensure_ascii=False, indent=2))
    return 0 if not (isinstance(out, dict) and out.get("ok") is False) else 1


if __name__ == "__main__":
    sys.exit(main())
