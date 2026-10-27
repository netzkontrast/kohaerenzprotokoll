"""The app's write path on Vercel: POST /api/answers files one AnswerSet as a pull request (decision 031.1, open).

Off by default. It answers 503 and does nothing unless the author set both
    ANSWERS_WRITE_PATH=on          — the documented approval to run the write path
    GITHUB_ANSWERS_TOKEN=<token>   — a fine-grained token with contents + pull requests on this repository only
The token never leaves this function; `middleware.js` admits the request only with the site's login from the site's
own origin. The logic and its offline selftest are `scripts/answers_api.py`; this file is the transport (urllib) and
the HTTP shape. It writes a new file on its own branch and opens a pull request; never main, never a canon file.

    python3 api/answers.py selftest     # the handler against the fake transport, no network
"""

from __future__ import annotations

import json
import os
import sys
import urllib.error
import urllib.request
from http.server import BaseHTTPRequestHandler
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import answers_api  # noqa: E402

API = "https://api.github.com"
LIMIT = 256 * 1024


class GitHub:
    """urllib over GitHub's REST API with the function's token; (status, json) like the fake."""

    def __init__(self, token: str, timeout: float = 20.0):
        self.token = token
        self.timeout = timeout

    def _call(self, method, path, body=None):
        data = json.dumps(body).encode("utf-8") if body is not None else None
        req = urllib.request.Request(API + path, data=data, method=method, headers={
            "Accept": "application/vnd.github+json", "Authorization": f"Bearer {self.token}",
            "User-Agent": "kp-answers", "X-GitHub-Api-Version": "2022-11-28",
            **({"Content-Type": "application/json"} if data else {})})
        try:
            with urllib.request.urlopen(req, timeout=self.timeout) as r:
                raw = r.read()
                return r.status, (json.loads(raw) if raw else {})
        except urllib.error.HTTPError as e:
            raw = e.read()
            try:
                return e.code, json.loads(raw) if raw else {}
            except ValueError:
                return e.code, {"message": raw.decode("utf-8", "replace")[:200]}

    def get(self, path):
        return self._call("GET", path)

    def send(self, method, path, body):
        return self._call(method, path, body)


def respond(payload: dict | None, env: dict, transport=None, now=None) -> tuple[int, dict]:
    """(status, body) for one request; the transport is injected for the selftest."""
    if env.get("ANSWERS_WRITE_PATH") != "on" or not env.get("GITHUB_ANSWERS_TOKEN"):
        return 503, {"error": "the write path is off: save the file and open the pull request yourself"}
    if not isinstance(payload, dict):
        return 400, {"error": "the body is not a JSON object"}
    try:
        out = answers_api.file_answers(payload, transport or GitHub(env["GITHUB_ANSWERS_TOKEN"]), now=now)
    except answers_api.Refused as e:
        return e.status, {"error": "refused: " + "; ".join(e.problems), "problems": e.problems}
    except answers_api.Upstream as e:
        return 502, {"error": f"GitHub did not take it: {e} — retry; a retry finds what was filed"}
    except Exception as e:  # noqa: BLE001 — the author sees why, not a blank 500
        return 500, {"error": f"{type(e).__name__}: {e}"[:300]}
    return 201, out


class handler(BaseHTTPRequestHandler):  # noqa: N801 — Vercel's Python runtime looks for this name
    def _send(self, status: int, body: dict) -> None:
        raw = json.dumps(body, ensure_ascii=False).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Cache-Control", "no-store")
        self.send_header("Content-Length", str(len(raw)))
        self.end_headers()
        self.wfile.write(raw)

    def do_GET(self):  # noqa: N802
        self._send(405, {"error": "answers are posted"})

    def do_POST(self):  # noqa: N802
        try:
            n = int(self.headers.get("Content-Length") or 0)
        except ValueError:
            n = 0
        if n > LIMIT:
            self._send(413, {"error": "the body is too large for an answer set"})
            return
        try:
            payload = json.loads(self.rfile.read(n).decode("utf-8") or "null")
        except ValueError:
            self._send(400, {"error": "the body is not JSON"})
            return
        status, body = respond(payload, dict(os.environ))
        self._send(status, body)

    def log_message(self, *args):  # the function's log holds no answer text
        return


def selftest() -> list[str]:
    import tempfile
    from datetime import datetime, timezone
    bad = []
    on = {"ANSWERS_WRITE_PATH": "on", "GITHUB_ANSWERS_TOKEN": "t"}
    st, body = respond({"session": "x", "answers": [{"question": "Q-x-01", "yes": True}]}, {"ANSWERS_WRITE_PATH": "on"}, answers_api.Fake())
    if st != 503:
        bad.append(f"without a token the path is not closed: {st}")
    st, body = respond({"session": "x", "answers": []}, {"GITHUB_ANSWERS_TOKEN": "t"}, answers_api.Fake())
    if st != 503:
        bad.append(f"without the approval the path is not closed: {st}")
    st, body = respond(["not", "an", "object"], on, answers_api.Fake())
    if st != 400:
        bad.append(f"a non-object body: {st}")
    with tempfile.TemporaryDirectory() as tmp:
        # the records the function validates against are the tree's; here a temporary one through answers_api
        folder = Path(tmp)
        (folder / "answers").mkdir()
        rec = answers_api.sp.record_skeleton("s")
        rec["questions"] = [{"id": "Q-s-01", "depth": 1, "text": "?", "lands_in": "Plan/decisions/"}]
        (folder / "s.json").write_text(json.dumps(rec), encoding="utf-8")
        keep = answers_api.sp.RECORDS, answers_api.sp.ANSWERS
        answers_api.sp.RECORDS, answers_api.sp.ANSWERS = folder, folder / "answers"
        try:
            fake = answers_api.Fake()
            now = datetime(2026, 10, 26, 13, 0, 0, tzinfo=timezone.utc)
            st, body = respond({"session": "s", "answers": [{"question": "Q-s-01", "words": "no yes given"}]}, on, fake, now)
            if st != 400 or "yes: true/false" not in body["error"] or fake.writes:
                bad.append(f"a refusal: {st} {body}")
            st, body = respond({"session": "s", "answers": [{"question": "Q-s-01", "yes": True, "words": "ja, aber"}]}, on, fake, now)
            if st != 201 or not body.get("pr") or body["file"] != "Plan/sessions/answers/s-20261026T130000Z.json":
                bad.append(f"a filing: {st} {body}")
            st, body = respond({"session": "s", "answers": [{"question": "Q-s-01", "yes": True, "words": "ja, aber"}]}, on, answers_api.Fake(fail_after=0), now)
            if st != 502:
                bad.append(f"an outage: {st} {body}")
        finally:
            answers_api.sp.RECORDS, answers_api.sp.ANSWERS = keep
    return bad


if __name__ == "__main__":
    if sys.argv[1:] == ["selftest"]:
        problems = selftest()
        print("answers function: " + ("FAILED — " + "; ".join(problems) if problems else "held — closed without approval and token, refusals, a filing, an outage"))
        sys.exit(1 if problems else 0)
    print(__doc__)
