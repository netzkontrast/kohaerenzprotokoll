# 023 — The novel's drafts live in `Manuscript/`, and the app shows them

**Date:** 2026-10-04 · **Decided by:** the author (what), the session (how) · **Status:** in use

## What was asked

> Füge eine manuscript Section in der zu ein - und speichere deine Entwürfe in einem Ordner manuscript

The message reads „in der zu“. The session read it as „in der UI“, the project app, because the request is about a
section. If something else was meant, the folder stays and the app's screen can go.

## What was chosen

1. **A top-level `Manuscript/`**, one folder per chapter (`kap-01/`, …), each with a `README.md` that says what its
   drafts are and what each decides against the sources.
   - This answers question C of the writing plan (`Plan/concept/novel-writing-plan_2026-09-29.md` §11). The plan had
     recommended `Novel/`; the author named the folder.
   - It is capitalised like every other top-level folder (`Sources/`, `Wiki/`, `Plan/`, `Graph/`, `Index/`).
2. **The Kap 1 drafts moved** from `Plan/runs/writing/kap-01/entwuerfe_2026-10-03/` with `git mv`, so their history
   follows them.
   - The findings about them stay in `Plan/runs/writing/`, as the `writing-skills` rule 6 says: the line edit and the
     agent reads.
   - A draft is prose, and a finding is a reading of it. Mixing them would let a skill's output look like part of the book.
3. **A „Manuscript“ screen in the project app** (`scripts/ui.py`, `ui.js`, `ui.html`) and its own artboard,
   `Manuscript.dc.html`.
   - It lists every markdown file under `Manuscript/` and renders each from its own text, as written, the way the app
     renders a wiki page.
   - Lines without a lowercase letter are a console's display (`ZUWEISUNG 388`) and keep their line breaks.
   - The website on Vercel gets the screen with the next build (decision 022). The claude.ai canvas gets it when a
     session republishes `project/Main.dc.html`.

## What was rejected

- **`Wiki/manuscript/`**: `Wiki/` holds readings of sources. A draft placed there would read as one more reading.
- **Leaving the drafts under `Plan/runs/`**: `Plan/runs/` keeps what a run produced. A chapter is not a run artifact
  once the author treats it as the book's.
- **Rendering only the newest draft**: the comparison between drafts is what the author asked for.

## What it does not decide

- **Who writes the prose** (question A). Every draft so far is a session's, written on the author's explicit request,
  and says so in its head.
- **Whether any draft is canon.** None is until the author approves it.

## What would change our mind

- The author names another place or another name.
- A second chapter shows that one folder per chapter does not fit.
