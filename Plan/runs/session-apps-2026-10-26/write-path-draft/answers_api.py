"""The app's write path for the author's answers, as pure logic over a transport (decision 031.1, open).

An AnswerSet the app composed (Plan/sessions/answers/<session>-<stamp>.json by contract) reaches git this way:

    validate  — scripts/sessions.py check_answer_set, against the records of the deployed tree; refused is refused
    branch    — app/antworten-<YYYY-MM-DD>-<session>, from main; one that exists already is reused
    file      — the answer file on that branch, one PUT; a retry finds it with the same bytes and moves on;
                the same name with other bytes is a collision (a second save in the same second): refused, try again
    pull      — the open pull request for that branch, found or opened, its body carrying `Session: <session>`

It never writes main, never a canon file, never anything but a new file under Plan/sessions/answers/. The server
decides nothing about what an answer settles; the responsible tool reads the merged file as provenance. The GitHub
token stays with the function (GITHUB_ANSWERS_TOKEN): nothing here reads it, and nothing of it reaches the app.

`transport` is an object with `.get(path)` and `.send(method, path, body)` returning `(status, json)`; `Fake` below
is the offline one, with the failures a retry must survive; api/answers.py supplies the urllib one on Vercel.

    python3 scripts/answers_api.py selftest
"""

from __future__ import annotations

import base64
import json
import sys
from datetime import datetime, timezone
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

import sessions as sp  # noqa: E402

REPO = "netzkontrast/kohaerenzprotokoll"
BASE = "main"
FOLDER = "Plan/sessions/answers"


class Refused(Exception):
    """The set does not meet the contract, or the same file exists with other content."""

    def __init__(self, status: int, problems: list[str]):
        super().__init__("; ".join(problems))
        self.status = status
        self.problems = problems


class Upstream(Exception):
    """GitHub answered with something the filing cannot continue from."""


def branch_of(sid: str, given_on: str) -> str:
    return f"app/antworten-{given_on[:10]}-{sid}"


def normalise(payload: dict, now: datetime | None = None) -> dict:
    """The set as the contract writes it: the fixed fields filled, the stamp the file is named by."""
    a = dict(payload or {})
    a.setdefault("@type", "AnswerSet")
    a.setdefault("schema", sp.SCHEMA)
    a.setdefault("by", "author")
    if not a.get("given_on"):
        a["given_on"] = (now or datetime.now(timezone.utc)).strftime("%Y-%m-%dT%H:%M:%SZ")
    return a


def validate(payload: dict, records: Path | None = None, answers: Path | None = None, now: datetime | None = None) -> tuple[dict, str]:
    """(the set, its file name), or Refused(400) with every problem named."""
    a = normalise(payload, now)
    sid = str(a.get("session") or "")
    if not isinstance(a.get("answers"), list) or not a["answers"]:
        raise Refused(400, ["answers: an empty set is not saved"])
    name = f"{sid}-{sp._stamp(str(a['given_on']))}.json"
    recs = sp.load_records(records)
    qs = sp.questions_of(recs)
    checked = dict(a, _file=name)
    bad = sp.check_answer_set(checked, qs, sp.load_answers(answers), ROOT)
    if bad:
        raise Refused(400, bad)
    return a, name


def body_bytes(a: dict) -> bytes:
    return (json.dumps(a, ensure_ascii=False, indent=1) + "\n").encode("utf-8")


def file_answers(payload: dict, transport, records: Path | None = None, answers: Path | None = None, now: datetime | None = None,
                 repo: str = REPO) -> dict:
    """Validate, then branch → file → pull request, each step finding what an earlier attempt left."""
    a, name = validate(payload, records, answers, now)
    sid = a["session"]
    branch = branch_of(sid, a["given_on"])
    path = f"{FOLDER}/{name}"
    content = body_bytes(a)
    # the base: main's head
    st, ref = transport.get(f"/repos/{repo}/git/ref/heads/{BASE}")
    if st != 200:
        raise Upstream(f"main not readable: HTTP {st}")
    base_sha = ref["object"]["sha"]
    # the branch, made or found
    st, made = transport.send("POST", f"/repos/{repo}/git/refs", {"ref": f"refs/heads/{branch}", "sha": base_sha})
    if st == 422:
        st2, _ = transport.get(f"/repos/{repo}/git/ref/heads/{branch}")
        if st2 != 200:
            raise Upstream(f"branch {branch} neither made nor found: HTTP {st}/{st2}")
        branch_state = "found"
    elif st == 201:
        branch_state = "made"
    else:
        raise Upstream(f"branch {branch}: HTTP {st}")
    # the file, written or found
    st, existing = transport.get(f"/repos/{repo}/contents/{path}?ref={branch}")
    if st == 200:
        have = base64.b64decode(existing.get("content", "").encode()) if existing.get("content") else b""
        if have != content:
            raise Refused(409, [f"{name} exists on {branch} with other content — a save is one file; try again"])
        file_state = "found"
    elif st == 404:
        st, put = transport.send("PUT", f"/repos/{repo}/contents/{path}", {
            "message": f"answers: {sid} from the app, {a['given_on']}",
            "content": base64.b64encode(content).decode(), "branch": branch})
        if st not in (200, 201):
            raise Upstream(f"file {name}: HTTP {st}")
        file_state = "written"
    else:
        raise Upstream(f"file {name}: HTTP {st}")
    # the pull request, found or opened
    owner = repo.split("/")[0]
    st, pulls = transport.get(f"/repos/{repo}/pulls?state=open&head={owner}:{branch}")
    if st != 200:
        raise Upstream(f"pull requests: HTTP {st}")
    if pulls:
        pr = pulls[0]
        pr_state = "found"
    else:
        st, pr = transport.send("POST", f"/repos/{repo}/pulls", {
            "title": f"Antworten aus der App: {sid} ({a['given_on'][:10]})", "head": branch, "base": BASE,
            "body": f"Antworten der Autorin/des Autors aus der App, wortgetreu, eine Datei je Speichern: `{path}`.\n\n"
                    f"Sie werden erst nach dem Merge vom zuständigen Werkzeug übernommen; die Datei ist die Provenienz.\n\n"
                    f"## Claim\n\nSession: {sid}\n"})
        if st != 201:
            raise Upstream(f"pull request: HTTP {st}")
        pr_state = "opened"
    return {"file": path, "branch": branch, "branch_state": branch_state, "file_state": file_state,
            "pr": pr.get("html_url", ""), "pr_number": pr.get("number"), "pr_state": pr_state, "session": sid, "n": len(a["answers"])}


# ---------------------------------------------------------------- offline transport

class Fake:
    """GitHub's handful of calls, in memory, with failures to inject: `fail_after` stops at the n-th write so a
    retry has to find what the first attempt left; `calls` records every request."""

    def __init__(self, fail_after: int | None = None):
        self.refs = {BASE: "0123abcd"}
        self.files: dict[tuple[str, str], bytes] = {}
        self.pulls: list[dict] = []
        self.calls: list[tuple[str, str]] = []
        self.writes = 0
        self.fail_after = fail_after

    def get(self, path):
        self.calls.append(("GET", path))
        if "/git/ref/heads/" in path:
            b = path.split("/git/ref/heads/")[1]
            return (200, {"object": {"sha": self.refs[b]}}) if b in self.refs else (404, {})
        if "/contents/" in path:
            p, _, ref = path.split("/contents/")[1].partition("?ref=")
            have = self.files.get((ref, p))
            return (200, {"content": base64.b64encode(have).decode(), "sha": "f" * 8}) if have is not None else (404, {})
        if "/pulls?" in path:
            head = path.split("head=")[1].split(":", 1)[1]
            return 200, [p for p in self.pulls if p["head"] == head and p["state"] == "open"]
        return 404, {}

    def send(self, method, path, body):
        self.calls.append((method, path))
        self.writes += 1
        if self.fail_after is not None and self.writes > self.fail_after:
            return 502, {"message": "injected outage"}
        if path.endswith("/git/refs"):
            b = body["ref"].removeprefix("refs/heads/")
            if b in self.refs:
                return 422, {"message": "Reference already exists"}
            self.refs[b] = body["sha"]
            return 201, {}
        if "/contents/" in path and method == "PUT":
            self.files[(body["branch"], path.split("/contents/")[1])] = base64.b64decode(body["content"])
            return 201, {}
        if path.endswith("/pulls") and method == "POST":
            pr = {"number": len(self.pulls) + 1, "head": body["head"], "state": "open", "html_url": f"https://github.com/{REPO}/pull/{len(self.pulls) + 1}", "body": body["body"]}
            self.pulls.append(pr)
            return 201, pr
        return 404, {}


# ---------------------------------------------------------------- selftest

def selftest() -> list[str]:
    import tempfile
    bad = []
    with tempfile.TemporaryDirectory() as tmp:
        folder = Path(tmp) / "sessions"
        folder.mkdir()
        (folder / "answers").mkdir()
        rec = sp.record_skeleton("pilot-session")
        rec["questions"] = [
            {"id": "Q-pilot-session-01", "depth": 2, "blocking": True, "text": "A or B?", "options": [{"key": "A", "text": "a"}, {"key": "B", "text": "b"}], "lands_in": "Plan/decisions/"},
            {"id": "Q-pilot-session-02", "depth": 1, "text": "Yes?", "lands_in": "Plan/decisions/"},
        ]
        (folder / "pilot-session.json").write_text(json.dumps(rec), encoding="utf-8")
        now = datetime(2026, 10, 26, 12, 0, 0, tzinfo=timezone.utc)
        good = {"session": "pilot-session", "answers": [{"question": "Q-pilot-session-01", "option": "B", "words": "mit Vorbehalt"}]}
        # 1. refusals name the contract's problem and write nothing
        for payload, want in ((dict(good, answers=[]), "empty"), (dict(good, answers=[{"question": "Q-nobody-01", "option": "A"}]), "no record"),
                              (dict(good, answers=[{"question": "Q-pilot-session-01", "option": "Z"}]), "none of"),
                              (dict(good, answers=[{"question": "Q-pilot-session-02", "words": "yes"}]), "yes: true/false")):
            t = Fake()
            try:
                file_answers(payload, t, folder, folder / "answers", now)
                bad.append(f"{want}: accepted")
            except Refused as e:
                if e.status != 400 or want not in str(e):
                    bad.append(f"{want}: refused for another reason — {e}")
            if t.writes:
                bad.append(f"{want}: a refused set reached GitHub")
        # 2. the full path: branch, file, pull request; nothing touches main
        t = Fake()
        out = file_answers(good, t, folder, folder / "answers", now)
        if out["branch"] != "app/antworten-2026-10-26-pilot-session" or out["file"] != f"{FOLDER}/pilot-session-20261026T120000Z.json":
            bad.append(f"branch or file name: {out}")
        if (out["branch"], out["file"]) not in t.files or (BASE, out["file"]) in t.files or t.refs[BASE] != "0123abcd":
            bad.append("the file is not on its branch alone, or main moved")
        if out["pr_state"] != "opened" or "Session: pilot-session" not in t.pulls[0]["body"]:
            bad.append("the pull request is not opened with the claim")
        body = json.loads(t.files[(out["branch"], out["file"])])
        if body["answers"][0]["words"] != "mit Vorbehalt" or body["by"] != "author" or body["given_on"] != "2026-10-26T12:00:00Z":
            bad.append("the filed set is not the author's words with the contract's fields")
        # 3. a retry after the same save: finds branch, file and pull request, writes nothing new
        before = t.writes
        again = file_answers(good, t, folder, folder / "answers", now)
        if (again["branch_state"], again["file_state"], again["pr_state"]) != ("found", "found", "found") or t.writes != before + 1:
            bad.append(f"retry did not find what the first attempt left: {again}, writes {t.writes - before}")
        # 4. a retry after a partial failure (the file was written, the PR not) completes without a second file or PR
        t2 = Fake(fail_after=2)
        try:
            file_answers(good, t2, folder, folder / "answers", now)
            bad.append("an injected outage went unnoticed")
        except Upstream:
            pass
        t2.fail_after = None
        done = file_answers(good, t2, folder, folder / "answers", now)
        if done["file_state"] != "found" or done["pr_state"] != "opened" or len(t2.pulls) != 1 or len(t2.files) != 1:
            bad.append(f"retry after outage: {done}, {len(t2.pulls)} pulls, {len(t2.files)} files")
        # 5. two saves in one second with other content collide (409); a later second is its own file on the same branch
        try:
            file_answers(dict(good, answers=[{"question": "Q-pilot-session-01", "option": "A"}]), t, folder, folder / "answers", now)
            bad.append("same name with other content was accepted")
        except Refused as e:
            if e.status != 409:
                bad.append(f"collision status {e.status}")
        later = file_answers(dict(good, answers=[{"question": "Q-pilot-session-02", "yes": True}]), t, folder, folder / "answers", now.replace(second=5))
        if later["branch"] != out["branch"] or later["pr_state"] != "found" or len(t.files) != 2:
            bad.append(f"a later save did not join the day's branch and pull request: {later}")
        # 6. the second session's answer goes to its own branch and pull request
        rec2 = sp.record_skeleton("other-session")
        rec2["questions"] = [{"id": "Q-other-session-01", "depth": 1, "text": "?", "lands_in": "Plan/decisions/"}]
        (folder / "other-session.json").write_text(json.dumps(rec2), encoding="utf-8")
        other = file_answers({"session": "other-session", "answers": [{"question": "Q-other-session-01", "yes": False}]}, t, folder, folder / "answers", now)
        if other["branch"] == out["branch"] or len(t.pulls) != 2:
            bad.append("sessions share a branch")
        # 7. an answer to another session's question is refused
        try:
            file_answers({"session": "other-session", "answers": [{"question": "Q-pilot-session-02", "yes": True}]}, Fake(), folder, folder / "answers", now)
            bad.append("a cross-session answer was accepted")
        except Refused:
            pass
    return bad


if __name__ == "__main__":
    if sys.argv[1:] == ["selftest"]:
        problems = selftest()
        print("answers api: " + ("FAILED — " + "; ".join(problems) if problems else "held — refusals, branch · file · pull request, retries find what was left, collisions, one branch per session"))
        sys.exit(1 if problems else 0)
    print(__doc__)
