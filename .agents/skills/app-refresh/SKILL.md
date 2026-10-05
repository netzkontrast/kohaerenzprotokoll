---
name: app-refresh
description: Rebuild, check, look at and publish the project app (scripts/ui.py → the claude.ai canvas and the Vercel website) for the commit a pull request carries, and keep it usable by agents as well as people — every item with an address, a JSON twin in llms.txt/agents/, and an interactive element rather than static text. Use before every pull request (the pre-PR hook refuses one whose app was not rebuilt for HEAD), after a reconciliation or a NOW.md change, when a check names ui.py, web.py or appstamp.py, and when the author asks to keep the UI updated.
---

# Refreshing the project app

The author's standing instruction of 2026-10-05 — *„keep the ui updated"* — made the app part of every change.
`.claude/hooks/pre-pr-app.sh` holds it: before `mcp__github__create_pull_request` or `gh pr create` it asks
`python3 scripts/appstamp.py verify` whether `ui.py --check` passed for HEAD's tree, and refuses the pull
request (exit 2) when not. This skill is what makes it pass, and what makes the pass mean something.

The app shows what the repository states and infers nothing (`scripts/ui.py`'s docstring). Refreshing it
never changes a reading, a page or a decision: when the app looks wrong, the fix is in the repository or in
`ui.py`/`ui.js`/`ui.html`, never in `Plan/derived/` by hand.

## 1 · Commit, then build and check

The stamp names HEAD's tree, so everything the pull request will carry is committed first.

```bash
git status --short                      # nothing staged or modified that belongs in the PR
python3 scripts/ui.py --check           # about two minutes: build, invariants, lint, data, syntax, every address
python3 scripts/web.py --no-build --check   # the website: frames, runtime, llms.txt, agents/
python3 scripts/appstamp.py verify      # what the hook will ask
```

Run `ui.py --check` in the background (it outlasts a two-minute tool call) and wait for it to finish. A `DEFECT` line
is a defect: fix it and run again. **Never waive a defect.** `appstamp.py waive "<reason>"` exists only for a
container that cannot build at all, and the reason goes into the pull request's description.

What the checks catch that matters here: a NOW.md heading the app reads that moved (the panel would be blank —
the rewrite of 2026-10-05 emptied three that way, silently), an address that does not lead back to its item, a
link or citation to nothing, a count that disagrees with `state.py`, an `agents/index.json` path that does not exist.

## 2 · Look at it

A check proves the files are well formed, not that the screen says what was meant. Serve the website and look at
every screen the change touches, wide and narrow:

```bash
python3 -m http.server 8765 -d Plan/derived/web     # in the background
```

Playwright with Chromium (`/opt/pw-browsers`, never `playwright install`): `http://localhost:8765/Main.dc.html#/…`
at 1440×900 and 390×844, a screenshot of each into the scratchpad. Always open `#/now` and one
`#/now/session/<id>`, and the addresses of what the change added (`#/wiki/<slug>`, `#/conflicts/C2`, …). Read the
screenshots: an empty panel, a cut-off title or a horizontal scroll at 390 px is a defect even when `--check` is green.

## 3 · Agents are users too — the rule for anything new

The website is read by people and by agents (`llms.txt`, `agents/sessions.json`, `agents/index.json`,
`agents/state.json`, `agents/data.json`, written by `ui.py`'s `agent_files`). When the change adds a kind of content
to the app, it gets all four, in the same pull request:

| what | where | why |
|---|---|---|
| an **address** | `route()`/`unroute()` in `scripts/ui.js`, and a line in `ROUTE_HARNESS` in `ui.py` | a link survives a rebuild; an agent can name the exact item |
| an **index entry** with its repository path | `agent_index()` in `ui.py` | an agent goes from the app to the file it changes |
| an **interactive element**, not static text | `ui.html` + `ui.js`: a button that goes to the item, a filter, a tab, a copy button for a prompt or command | a list a person can only read is a list nobody acts on |
| a **check that can fail** | `check_data()`/`check()` in `ui.py`, and its case in `selftest()` | an empty or broken panel says so instead of shipping blank |

Prefer an element that hands over work — *Copy prompt for an agent*, a command with its arguments filled in, an
address to paste — over one that only describes it. Nothing interactive inside a `<button>` or `<a>` (the parser
closes the outer one; `--check` names it). A prompt the app offers carries the repository's words and paths, never
corpus text: handing it on must send nothing that has not already left the container.

## 4 · The next sessions

`scripts/sessions.py` reads NOW.md § *Half-done — where the next session starts* and nothing else: each item with
a next step is a session, in NOW.md's order, *ready* or *waits on the author*; items without one are notes that bind
them all. Each prompt comes as blocks (`sessions.py`'s `blocks()`); the Now screen's **start-prompt editor** loads the
picked session (`#/now/session/<id>`, or `#/now/session/free` for a prompt in the author's own words), puts the author's
instruction after *read first*, switches blocks on and off, lets the text be edited by hand, and copies or saves it —
drafts stay in the browser's storage, never in the repository. `agents/sessions.json` serves the same blocks. **To change the plan, change NOW.md** — the plan is NOW.md read again, never a
second list. When `python3 scripts/sessions.py` prints something NOW.md did not mean, fix the wording in NOW.md or
the rule in `sessions.py` (with its selftest case), not the output.

**The session board** — the Now page also coordinates the sessions (the author, 2026-10-05: *„coordinate your work there"*).
`python3 scripts/sessions.py board` (printed at every session start) and the page's *The next sessions* column set the plan
against GitHub's public API: a pull request claims a session with a line `Session: <id>` in its body, a branch pushed in
the last 24 h is active, and active work with no pull request raises a caution beside every session marked *no claim*.
`boardOf` in `ui.js` and `board()` in `sessions.py` are one rule written twice; `ui.py --check` runs both on one case and
fails when they differ — change the rule in both, with the case. Offline the board says *unknown*, never *free*.

**The session editor** — the page's *New session* tab (and *Edit as a session of its own* on a planned session) takes a
title, a next step and files, and gives the prompt, the claim line and an entry for NOW.md § Half-done. The id is the slug
of the title (never typed), because that is the id `sessions.py` will give the entry; `ui.py --check` writes entries with
the page's JavaScript and reads them back with `derive()` — change `slugOf`/`entryOf` and `slug`/`derive` together.
The plan stays in NOW.md: the editor never stores a session, it hands the entry over.

## 5 · Publish

- **The canvas** — https://claude.ai/artifact/1EyhQkX3MpiRTw3TxjTjYL, private to the author. A data refresh
  sends `project/Main.dc.html` alone (root `Plan/derived/ui/canvas`), so the author's arrangement survives;
  `canvas.json` and the frames only when the layout changed. Read the artifact first (the Artifact tool's `read`,
  `path: project/Main.dc.html`) and find the commit it shows (`"meta":{"commit":…}`). **Publish only when that commit
  is an ancestor of HEAD** (`git merge-base --is-ancestor <commit> HEAD`, after `git fetch`): otherwise another
  session's snapshot is live — several sessions publish to one canvas — and yours would overwrite work this branch
  does not hold. Leave it, and say so in the pull request; the canvas catches up from `main` after the merge
  (measured 2026-10-05: a session's snapshot of `e9e262c2`, on no branch this one held, went live minutes before
  this skill's first run). A session without the Artifact tool says in the pull request that the canvas was not
  published.
- **The website** — Vercel project `kohaerenzprotokoll` builds every push itself (`vercel.json` runs
  `python3 scripts/web.py`). After pushing, look for the branch's preview deployment and open
  `/llms.txt` and `/Main.dc.html#/now` on it (the Vercel connector's `web_fetch_vercel_url` gets past the login).
  When the connector cannot reach the team's scope, say in the pull request that the preview was not looked at.

## 6 · Say what was done

The pull request's description names: the tree the app was built for (`appstamp.py show`), the defect count, the
screens looked at, whether the canvas was published, whether the preview was opened, and any waiver with its reason.

## Provisional

```yaml
name: app-refresh        # provisional — the hook and this skill are one day old
# may not: change what the app says (ui.py infers nothing), edit Plan/derived/ by hand,
#          waive a defect, publish layout changes to the canvas without saying so,
#          or put corpus text into a prompt the app offers
# retire when: CI builds and checks the app on every pull request (Plan/concept/vercel-app_2026-10-02.md §4.2)
#              and a published preview is linked from the pull request without a session
```
