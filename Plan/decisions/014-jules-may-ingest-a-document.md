# 014 — A Jules session may ingest a document

**Date:** 2026-09-27 · **Decided by:** the author, in two sentences · **Status:**
in use, one session

## What was asked

`NOW.md` asked whether a Jules session may work on this repository at all. A
session is Google's agent working on a clone of the whole repository, `Sources/`
included, so `scripts/jules.py dispatch` refuses without `--approval` naming the
author's decision. It also asked whether a session may touch `Wiki/`.

> Use Jules to ingest a new file

> Try it again - now with my explizit permission

The second sentence followed a dispatch the session's permission check had
blocked.

## What was chosen

- **One session, one document, by the `ingest` skill.** Session
  `13693408587293976428`, on `kohaerenz-protokoll-philosophischer-bericht-md`,
  the document `NOW.md` named next. It is the first reader here that is not
  Claude.
- **`Wiki/` is in scope for an ingest**, because an ingest writes readings there;
  the scope was `Plan/`, `Sources/terms/`, `Sources/notes/`, `Wiki/`, `NOW.md` and
  `CLAUDE.md`. `scripts/`, `Sources/drive/` and the manifests stay out.
- **The plan gate stays on**: the session's plan is read before it is approved,
  and its pull request is reviewed like any other.

The approval's words are in `Plan/runs/jules/ledger.jsonl`.

## What it does not cover

Any other session, any task other than an ingest, and any change in `scripts/`.
Each is asked again.

## What would change our mind

The session's reading measured against the rules the checks hold —
`quotes.py`, `account.py order`, `state.py --prose` — and against a Claude
reading of the same document, if one is made (`scripts/agree.py`).
