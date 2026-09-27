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

## What happened — measured 2026-09-27

The session ran three hours, 239 activities, and ended COMPLETED at 12:11.
`jules.py verify` found its branch on the remote. The ingest it published is not
one, and its own account of it is false in the places that matter:

| the prompt asked for | the branch holds |
|---|---|
| `03-candidates.md` written while reading | the file's header and **0 candidates** |
| a census and a note | **neither** — no `Sources/terms/` or `Sources/notes/` file |
| judgements with a rule in words | **none** — its description and `reconcile.json` claim 21, J98–J118; `judgements.jsonl` ends at J97 |
| `reconcile-31-<slug>.md` | **absent**, while `reconcile.json` claims 44 new readings |
| the sweep settled | **44 hits open** (`reconcile.py --sweep-open`) |
| its work pushed into pull request #104 | a branch of its own and pull request #106; #104's files copied in by hand, not merged |

What holds: entries on C2, C4, C6, C7, C9, Q1–Q5 and Kap 13, and links. Every
quotation in them resolves (`quotes.py`: 0 unresolved), and `chapters.py` reports
0 defects. Its `NOW.md` says the document „resolves" and „settles" conflicts,
which no ingest may do, and it committed a scratch file,
`submission_description.txt` — agency's lesson 01, repeated.

**`account.py order` held over all of it.** A `reconcile.json` with no census
beside it is not a document the check counts, so a record claiming a
reconciliation that never ran passed green. That is a gap in the check, noted in
`NOW.md`, not fixed here.

Nothing from the session was merged into #104. What to keep from #106 is the
author's call (`NOW.md`).

**The author merged #106, 2026-09-27** („Da ist noch ein offener pr - bitte
merge den in Main"). By then `dual-storyform-hintergruende-md` had been read as
document 30 on `main`, with `reconcile-31` and J98–J99 — the numbers the session
had claimed. So the merge kept both: in every conflict and question record the
two entries stand one after the other, `main`'s first. The rest took `main`'s
side and was re-measured. Two things of the session's did not go in as they
were: `submission_description.txt` was removed, and its `reconcile.json` was
renamed `reconcile-claimed-by-jules.json`, because `state.py` counts every
`reconcile.json` as a reconciliation and this one never ran.
