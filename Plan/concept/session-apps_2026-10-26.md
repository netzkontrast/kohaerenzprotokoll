# Every session an app on the start page — the record, the channel, the generated prompt

*2026-10-26. The author's instruction: „Alles, was wir bisher sicher haben, ist, dass meine bisherige Arbeit als Sources
eingelesen ist. … ab jetzt [entwickelt] jede Session eine kleine Anwendung — auf der Startseite — mit einem Link zu allen
bisherigen Sessions als Liste, die mit eigener UI markiert. … Jede Session soll mir als Erstes sagen können, was getan
und/oder gedacht wurde, die Prios und was als Nächstes folgen sollte. … eine Methode, wie die App selbst zurück in Git
pushen kann … eine UI, mit der wir kommunizieren: die App generiert aus allen Entscheidungen, die in der App gefällt wurden,
scriptbasiert einen neuen Startprompt … zunächst eine geeignete Datenstruktur, auch im Hinblick auf Graph-Integration und
Ontologien, orientiert an Best Practices für Skills … [Antworten] nach Speichern auf GitHub als PRs … überleg, wie du in
Vercel in Zukunft Daten speichern willst. So können parallele Sessions gemeinsam laufen.“*

Status: **a proposal**. Nothing here is built; the mockup is `Plan/concept/session-apps/mockup.html`. What the author decides
becomes decision 031; what it supersedes is named in §8.

## 1 · What holds, and what changes

| holds (CLAUDE.md, decisions 022, 024, 029) | changes with this concept |
|---|---|
| NOW.md is the one plan; *there is no board, no status field and no backlog* | unchanged: the sessions' records are **accounts of what happened**, derived into the list; the plan stays NOW.md and the generated prompt reads both |
| the author's words are the only authority; a tool proposes | unchanged, made mechanical: an answer is the author's words, written by the author into the app, and it lands in the repository **only through a pull request the author merges** |
| the website is static, no database (022) — *the site has no write path and gets none* (`agent-sessions_2026-10-05.md` §3) | **superseded in one point**: one function (`api/answers.py`, beside `api/rag_server.py` of decision 029) writes the author's answers to GitHub as a pull request. Still no database of record: git is the store; Vercel holds at most a transient inbox (§6) |
| every new kind of content: an address, an index entry, an interactive element, a check that can fail (`app-refresh`) | every session's app follows the same four rules, registered in the session's record |
| no corpus text leaves the container; no prompt the app offers carries corpus text | the generated prompt carries the repository's words and the author's answers, never a source line |

## 2 · The record — one file per session

`Plan/sessions/<id>.json`, written by the session (a script makes the skeleton, the session fills the report; a check
refuses a session without one). The id is the slug `sessions.py` already gives (`writing-workshop`, `full-read-genesis-klammer`),
so NOW.md's plan, the claim line in the pull request and the record name one thing.

```json
{
  "@type": "Session",
  "id": "writing-workshop",
  "claude_session": "session_01LC…",
  "started": "2026-10-23", "ended": null,
  "branch": "claude/adoring-sagan-l2qtnq", "pr": 195,
  "title": "The writing workshop — the six tools before the first scene",
  "mandate": "the author's instruction of 2026-10-26, decision 030",
  "report": {
    "done":    [{"text": "prose_rules.py — 25 rules, 5 confirmed", "refs": ["scripts/prose_rules.py", "Manuscript/regeln.jsonl"]}],
    "thought": [{"text": "nothing approves without the author's words; a tool proposes"}],
    "priorities": [{"rank": 1, "text": "the author answers Kap 1's 11 Weichen"}],
    "next":    [{"text": "beats of Kap 1 Szene 1", "command": "python3 scripts/manuscript.py beats kap-01 1 --words … --beats …"}]
  },
  "app": {"name": "Schreibtisch", "route": "#/manuscript/schreibtisch", "path": "scripts/ui.js", "what": "briefing, scenes, marks per paragraph"},
  "questions": [
    {"@type": "Question", "id": "Q-writing-workshop-01", "depth": 2,
     "text": "Wie lang ist ein Kapitel im Pilot?", "context": "W16 …", "options": [{"key": "A", "text": "1 500–2 000"}, {"key": "B", "text": "3 000–5 000"}],
     "concerns": ["weiche:W16", "chapter:kap-01"], "lands_in": "Plan/weichen/w16-laenge.md", "asked_on": "2026-10-26"}
  ],
  "follows": ["full-read-genesis-klammer"]
}
```

**Depth** (Tiefe) is the author's word for how much a question asks of the author, and it decides the control the app
renders and what the answer script accepts:

| depth | the author gives | the app shows | the answer file holds |
|---|---|---|---|
| 1 | yes / no | two buttons | `{"yes": true}` + words optional |
| 2 | one of the options | radio chips, the recommended one marked | `{"option": "B"}` + words optional |
| 3 | an answer in own words, with the context needed to give it | the context (collapsible), a textarea | `{"words": "…"}` required |

**Answers are a separate, append-only file**, never an edit of the record: `Plan/sessions/answers/<id>-<timestamp>.json`:

```json
{"@type": "AnswerSet", "session": "writing-workshop", "by": "author", "given_on": "2026-10-26T18:40:00Z",
 "answers": [{"question": "Q-writing-workshop-01", "option": "B", "words": "3 000–5 000 im Pilot; danach messen"}]}
```

The record is the session's (it writes it on its branch); the answer file is the author's (the app writes it on a branch
of its own, §5). Neither edits the other's file, so two sessions and the author never touch one file at once (§7).

What an answer **settles** is not decided by the app: a question names `lands_in` — a Weiche sheet, a prose rule, a
decision file, `kanon.md` — and the session that picks the answer up runs the tool that already exists for it
(`weiche.py answer`, `prose_rules.py confirm`, `manuscript.py approve`, a decision file by hand), citing the answer file.
The answer file is the provenance; the tool's output is the canon. The app never writes `kanon.md`.

## 3 · The generated prompt

`python3 scripts/sessions.py prompt --next` (today's `sessions.py` extended, not a second script): the blocks it already
builds from NOW.md, plus

- **`report`** — the previous session's `report` (done / thought / priorities / next), from the newest closed record;
- **`decided`** — every answer since the last prompt, one line each: `Q-id · depth · the author's words · lands in …`,
  with the answer file's path, so the next session knows what it must fold into the tools first;
- **`open`** — the questions without an answer, carried forward with their depth;
- **`apps`** — the sessions with an app and their routes, so the next session extends rather than duplicates;
- **`claim`** — the id the new session will carry (`Session: <id>`), its record path and the command that makes the skeleton.

The app shows the same blocks (the start-prompt editor already does this for NOW.md's blocks) and the author switches
them on and off; `agents/sessions.json` serves them. Nothing is typed by hand into the prompt that a file does not state.

## 4 · Ontology — how it sits in the graph

The record's `@type`s are the node kinds `graph.py` adds (beside `term:`, `doc:`, `conflict:`, `question:`, `record:`,
`thought:`), each node carrying the file line that states it, as every node does today:

| node | from | key fields |
|---|---|---|
| `session:<id>` | `Plan/sessions/<id>.json` | started, ended, branch, pr, mandate |
| `app:<id>` | the record's `app` | route, path |
| `ask:<Q-id>` | the record's `questions[]` | depth, asked_on, lands_in |
| `answer:<file>#<n>` | `Plan/sessions/answers/*.json` | given_on, by, option/yes/words |

| edge | reads |
|---|---|
| `session —asks→ ask` · `answer —answers→ ask` · `answer —settles→ weiche:W16 / rule:L3 / decision:031 / chapter:kap-01` | what was asked, what the author said, where it landed |
| `ask —concerns→ term:… / chapter:… / conflict:…` | the question joins the existing graph here, so `ask` on a term returns the author's open questions beside the sources' readings |
| `session —builds→ app` · `session —follows→ session` · `session —continues→ prompt:<date>` | the chain of sessions, each from the prompt the previous one generated |

Two times on every answer, as the project already keeps on readings: `given_on` (when the author said it) and the
commit that landed it (`git log` of the answer file) — valid time and record time; a prompt generated between the two
says *answered, not yet merged*. Vocabulary stays the project's own, with `@type` names that map to schema.org where a
mapping exists (`Question`, `Answer`, `Action`) in a small `Plan/sessions/context.jsonld`, so an export is JSON-LD without
the records knowing it. No new store: the JSON files are the authority, the graph a derived view, `kg.py` a projection.

## 5 · The write path — how the app pushes back into git

Three ways were weighed:

| | how | verdict |
|---|---|---|
| **A · one function, one token** | `api/answers.py` (Python on Vercel, like `api/rag_server.py`): `POST /api/answers` with the answer set → creates branch `app/antworten-<date>-<session>` from `main`, writes the one answer file through GitHub's Contents API, opens a pull request whose body carries `Session: <id>` and the answers as a list, returns the PR URL. A fine-grained token `GITHUB_ANSWERS_TOKEN` for this repository only (contents + pull requests, write), set at Vercel; the route behind the site's Basic login and the middleware as every `/api/*` path (fail closed without the variable). | **recommended** — one file added per save, no edit of anything that exists, the author's merge is the authority act, CI checks the file (`sessions.py check`: the question exists, the option is one of its options, depth 3 has words) |
| B · GitHub OAuth in the browser | the author signs in to GitHub from the app, the browser calls the API | more moving parts for one author, a client secret anyway |
| C · Vercel storage as the record | answers in Vercel KV/Blob, a session fetches them | a second store of record beside git — ruled out by 022's reason, kept only as an inbox (§6) |

The app's „Speichern → Pull Request“ shows four states: *offen* (nothing saved) · *gespeichert* (the inbox holds it, §6) ·
*PR #n geöffnet* · *gemerged* (the next build reads the file from `main`). Saving never writes to `main`.

## 6 · Data at Vercel

Git is the store of record for everything the author decides. What Vercel may hold is **what is not yet a decision**:

- **drafts of answers** — today in the browser's `localStorage` (the marks, the reading notes, the prompt drafts); with
  Vercel Blob (one JSON per session id, `kp-drafts/<session>.json`) a draft survives the device, and two devices see one draft;
- **presence** — *session X is live on branch Y since Z*, written by a session at start (through the same token route) and read by
  the board, so the board no longer infers activity from a push time alone;
- **the inbox** — an answer set saved but not yet turned into a PR (the token unset, GitHub down): Blob keeps it until the function
  succeeds, so nothing the author typed is lost.

All three are cache: deletable at any time without losing a decision. The data the sessions need is in the repository; the data the
author needs is in the repository; Vercel holds the moment between typing and merging.

## 7 · Parallel sessions

- one record file per session, one answer file per save, no shared file: no merge conflict by construction;
- the claim stays the pull request's `Session:` line; the board reads GitHub; the start page lists the records with their state
  (`ready` / `waits on the author` / `live` / `done`) and marks those with an app;
- a session reads the answers that concern **its** questions (the answer file names the session) and only folds those into the tools;
  an answer to another session's question is left alone and named in the report;
- the generated prompt carries the open questions of every session, so a second session never asks what the first already asked.

## 8 · What the author decides (proposed decision 031)

1. **The write path** — one function with a repository-scoped token, answers as pull requests (§5 A); supersedes the sentence
   *the site has no write path and gets none* of 2026-10-05 and narrows 022 to *no database of record*.
2. **The record** — `Plan/sessions/<id>.json` per session with the four-part report, `questions[]` with depth, and the app's registration;
   a check refuses a session without a report; the start page lists the records.
3. **The prompt** — generated by `sessions.py` from NOW.md plus the records and the answers; the editor keeps the on/off blocks.
4. **Vercel** — Blob for drafts, presence and the inbox, nothing of record.

What this session asks of the author through the app first: the three questions in the mockup's channel, at depth 1, 2 and 3.

## 9 · Order of building

1. `sessions.py record new <id>` (the skeleton), `record check`, this session's own record written by hand from the mockup's content.
2. The start page: the report card, the session list with app badges, the apps grid — the Now screen rebuilt, every item with an
   address (`#/now/session/<id>`, `#/now/app/<id>`), index entries, checks.
3. The channel: questions with depth, answers kept in the browser, the export as a file and the copyable command (no server yet).
4. `api/answers.py` and the token (the author sets it at Vercel), the PR path, `sessions.py check` in CI.
5. `sessions.py prompt --next` with the `decided` / `open` / `apps` blocks; the graph nodes of §4.
6. Vercel Blob for drafts, presence and the inbox — only when 4 shows the need.

## Provisional

```yaml
construct: session record     # provisional — a proposal of 2026-10-26; nothing built
# may not: replace NOW.md as the plan, write kanon.md, decide what an answer settles, carry corpus text into a prompt
# retire when: three sessions have records and the author never opened the start page's report card, or NOW.md
#              and the records say different things twice
```
