# The answers' write path — a draft, not wired (2026-10-26/27)

Status: **draft kept for the author's answer to the write-path question** of
`Plan/sessions/every-session-an-app-on-the-start-page.json` (decision 031, open). Nothing here is imported,
deployed or run by CI.

Two sessions built the session records in parallel on 2026-10-26. The author merged the other one (PR #197:
`scripts/records.py`, the start page's tabs); this session's version of the records and the start page was
dropped as a duplicate. What only this session built is the server write path, kept here so it need not be
written twice once the author says yes:

| file | what it does | offline evidence at the time |
|---|---|---|
| `answers_api.py` | validate an answer set, then branch `app/antworten-<date>-<session>` → one new file under `Plan/sessions/answers/` → the pull request carrying `Session: <id>`; each step finds what an earlier attempt left, so a retry after a partial GitHub failure writes nothing twice; the same file name with other bytes is refused (409); never `main`, never a canon file. `Fake` is an in-memory GitHub with injected outages | `selftest` held: refusals, the full path, retry after a completed save, retry after an outage, same-second collision, a second session on its own branch, a cross-session answer refused |
| `answers_function.py` | the Vercel function around it (`api/answers.py` when wired): 503 unless `ANSWERS_WRITE_PATH=on` **and** `GITHUB_ANSWERS_TOKEN` are set; the token never leaves the function | `selftest` held: closed without approval or token, a refusal, a filing, an outage → 502 |

**Before it can run** it must be ported to the merged contract: it validates through the parallel
`sessions.py` functions (`check_answer_set`, `load_records`, `questions_of`) that main does not have — the port
replaces them with `records.py`'s `load`, `questions` and `problems`, and its per-answer `supersedes: "<file>#<n>"`
with `records.py`'s set-level `supersedes: ["<file>"]`. The middleware then needs a rule for `/api/answers`; with the
site open since decision 032, that rule cannot be the site login — it needs its own secret, decided with the path.
