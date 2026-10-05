# The next sessions, planned from the website — what is built, and what waits on the author

*2026-10-05. The author asked for a skill that a hook runs before every pull request to bring the app up to date,
with interactive elements that make the repository usable by agents and not only by people, and for a way to
plan the next few agent sessions from the Vercel server. Marked **[built]** where it exists in this commit,
**[proposed]** where it waits on the author.*

## 1 · The constraint everything here keeps

CLAUDE.md: *there is no board, no status field and no backlog*; NOW.md is the handover, one page, *in the order to
act on it*. A second list of planned sessions would be a backlog that drifts from NOW.md on the first edit. So the
plan is **NOW.md read again** — on every build, by a script with written rules — and changing the plan means
changing NOW.md. Decision 022 adds a second constraint: the website is static, with no server, no API and no
database, and that holds here too.

## 2 · What is built

| piece | what it does | status |
|---|---|---|
| `scripts/sessions.py` | reads NOW.md § *Half-done* and nothing else: an item with a `Next:`/`Open:` step is a session, an item that „waits on" the author is a gated one, every other item is a note binding all; each session gets a self-contained prompt (the item, its next step, the files it names, the standing instructions, the notes, *claim before you start*); `selftest` holds every rule | **[built]** |
| the Now screen | the panel that used to list the handover (blank since NOW.md's rewrite renamed the heading it read) lists the sessions — status, next step — and a **start-prompt editor** beside it (the author, 2026-10-05: *„Direkt auf der Startseite … nen Texteditor der startprompts schon mal baut"*): the picked session's prompt as blocks to switch on and off, *Your instruction* placed after *read first*, the text editable by hand, Copy, Save .md, Reset; a free prompt for a session the author names; drafts in the browser's storage only; `#/now/session/<id>` and `#/now/session/free` | **[built]** |
| `llms.txt`, `agents/` | beside the frames, on the website: `sessions.json`, `index.json` (every page, conflict, question, record, decision, draft and session with its repository path and its address), `state.json`, `data.json` | **[built]** |
| `ui.py --check` | refuses an empty NOW.md list the app requires, an index path that does not exist, a session address that does not come back; writes `stamp.json` for the commit's tree | **[built]** |
| `.claude/hooks/pre-pr-app.sh` | before `mcp__github__create_pull_request` or `gh pr create`: refuses (exit 2) unless `scripts/appstamp.py verify` finds a clean build for HEAD's tree | **[built]** |
| skill `app-refresh` | build and check, look at the screens, the agent rule for anything new (address, index entry, interactive element, a check that can fail), publish to the canvas, open the Vercel preview, say what was done | **[built]** |

On 2026-10-05 the derivation finds six sessions — four ready (the storyforms, E4, the ingest, the second relation
reader), two waiting on the author (the HyperExtract backfill, the entity lists) — and three notes. Measure it
again with `python3 scripts/sessions.py`; this page will not stay true.

## 3 · Planning from the server — three levels

**L1 — read [built].** Every Vercel build serves `agents/sessions.json` for its commit. Any session reads it — through
the Vercel connector's `web_fetch_vercel_url`, which gets past the Vercel login, or simply `python3 scripts/sessions.py --json`
in its own clone — and takes the first *ready* session no open pull request claims. The website cannot know the
claims: a Vercel build has no GitHub token, and it should not get one. Checking for a `Claim` pull request stays the
session's first step, and the prompt says so.

**L2 — schedule [proposed].** One Claude Code Routine, a fresh session per firing, whose prompt is: *read the plan,
take the first ready session nobody has claimed, claim it, do it, run app-refresh, open the pull request.* One Routine
firing at most once a day keeps the standing instruction of 2026-09-30 (*starte diese nicht parallel*) and the usage
limit in view; the author's merge is the gate between two runs. It can be limited to named sessions (the ingest is the
obvious one: one document a run, every rule of the `ingest` skill applying). It draws on the author's usage on every
firing, so it waits on a yes: whether, how often, and which sessions.

**L3 — a trigger at Vercel [proposed, not recommended].** Vercel Cron calling a function that starts sessions through
an API. It needs a server function and a secret token stored at Vercel — what decision 022 ruled out — and adds over L2
only that the clock lives at Vercel. Not worth the server.

**Steering from the website.** The site has no write path and gets none. The author steers by editing NOW.md — the order
of *Half-done* is the order of the sessions, a `Next:` makes an item a session, „waits on" gates it — and the next
deployment shows the new plan. Comments left with the Vercel toolbar on a preview could be a second channel a session
reads; the connector could not list them on 2026-10-05 (below).

## 3b · Coordinating the running sessions — the board **[built]**

Two sessions once read the same documents because both handovers named the same next one. The board (the author,
2026-10-05: *„Use the Page … to create an interactive Session ui where you hook the Page into Claude.md as Session start —
coordinate your work there"*) is how that stops: `scripts/sessions.py board` sets NOW.md's plan against GitHub's public
API, prints at every session start (`.claude/hooks/session-start.sh`, `CLAUDE.md` § Read this first) and is live on the
Now page (`#/now`, read in the browser every minute, with a Refresh button).

- **A claim** is an open pull request whose body holds a line `Session: <id>` — the id the board prints, or the session's
  own for work NOW.md does not name. A session claims first, with the pull request, then works.
- **Active** is a branch pushed to in the last 24 h. Active work that holds no claim is listed apart, and raises a caution
  beside every *no claim* session: when it was built, the ingest and storyform branches were pushing with no pull request,
  so „free" for their sessions would have been false.
- **Not inferred:** a branch named like a session has not claimed it. **Offline** (GitHub unreachable) every session reads
  *unknown*, never *free*.
- **Limits:** the unauthenticated API allows 60 requests an hour per address and caches a minute, so the page reads two
  endpoints per minute only while it is open and visible, and a session start reads two. A claim made in a pull request
  body is only as current as the session keeping it; a pull request closed or merged leaves the board at once.

## 4 · What was measured, and what could not be

- The Vercel connector lists the project (`prj_9BQOM2YBSbbiLU2EjB5aIrKYnQmF`, team `team_ihXVTS84lsnPnxS8WmqPbgbv`) but
  refuses its deployments: *403, not authorized for scope "lukewtf" — re-authenticate to this scope*. Toolbar threads
  answered *Unknown error*. Until the connector is re-authorised for the team, no session can open a preview or read
  toolbar comments; the skill says to report that rather than skip it.
- The author's message mentions „die letzten 5 Empfehlungen" — no five recommendations reached this session (not in the
  message, the repository, or the toolbar the connector could reach). Where they are is asked below.

## 5 · Questions for the author

1. **L2**: one scheduled session a day (or none) — and for which sessions: all *ready* ones in NOW.md's order, or the
   ingest only?
2. **The Vercel connector**: re-authorise it for the team's scope, so sessions can open previews and read toolbar comments.
3. **The five recommendations**: where are they — a toolbar comment, a file, another session?
