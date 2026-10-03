# 022 — The project app is also a website on Vercel, behind the author's Vercel login

**Date:** 2026-10-02 · **Decided by:** the author (what), the session (how) · **Status:** in use

## What was asked

> Copy https://claude.ai/artifact/1EyhQkX3MpiRTw3TxjTjYL over - and use it to deploy This at vercel - also… Plan how
> you would implement it for this repo

## What was chosen

1. **The app is deployed to Vercel**, project `kohaerenzprotokoll` on the author's Hobby account, connected to this
   GitHub repository. Vercel builds it itself on every push: `python3 scripts/web.py` runs `ui.py --no-checks` and
   puts the frames beside the canvas's runtime in `Plan/derived/web/` (`vercel.json`). Nothing derived is committed.
2. **Only the runtime was copied over.** The canvas's `Main.dc.html` is a snapshot of commit `bdecc3d`
   (2026-09-24: 92 pages); `ui.py` derives the same file from the current commit, so copying it would have committed a
   stale derived file. What a website lacks and the repository did not hold is the canvas's `support.js` — vendored as
   `scripts/web/support.js`, pinned by sha256 (`scripts/web/README.md`).
3. **Vercel Authentication on every deployment** (`ssoProtection: all`), chosen by the session as the default that can
   be widened later and cannot be un-published: Vercel now holds the wiki's text — quotations from the corpus
   included — so it is a third party in the sense of decisions 007, 008 and 011, and this request is the author's
   decision to send it there. It is not a decision to make it public. `X-Robots-Tag: noindex` is set besides.
4. **The canvas stays.** It is still where the author arranges and comments; the website is a second way to open
   the same app, not its replacement.

## What was rejected

- **Committing the canvas's files**: stale at once, and a derived file in git is what `Plan/derived/` exists to prevent.
- **Vercel's `import-claude-design-from-url`**: it wants a self-contained export at a public URL, rebuilt by hand
  from the canvas each time — the canvas would stay the source, not the repository.
- **A GitHub Action deploying with the Vercel CLI**: needs a `VERCEL_TOKEN` secret and duplicates what the Git
  integration does; worth it only if the build needs the venvs (it does not: `ui.py` is standard library).

## What would change our mind

- The author wants it public → change the project's Deployment Protection; nothing in the repository changes.
- A build longer than Vercel's limit, or `ui.py` needing a venv → move the build to a GitHub Action (the plan, §4).
- The canvas's type moves on and the website renders differently → copy the new runtime (`scripts/web/README.md`).
