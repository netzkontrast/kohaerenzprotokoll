# 032 — the website opens without a login; `/mcp` keeps its token

**Date:** 2026-10-27 · **Decided by:** the author · **Status:** built on PR #198's branch; live after the merge to `main`

## What was asked

The author, 2026-10-27, verbatim: „Remove https://kohaerenzprotokoll.vercel.app/ sitelogin“ and „Remove the sotelogin and
fix the Kohärenz Protokoll Site“.

The live site answered **503 on every path** that morning (measured with `curl`: `/`, `/Main.dc.html`,
`/agents/sessions.json`, `/mcp`). The cause is decision 029 §5's fail-closed rule: `SITE_PASSWORD` is not set in the
Vercel project, so the middleware served nothing. The deployment itself is healthy (the last production build, of
`main` at `2f5f2d11`, is `READY`).

## What was chosen

- The website — the frames, `llms.txt`, `agents/`, `static/` — is served to anyone, with no login and no variable.
  The `X-Robots-Tag: noindex, nofollow` header stays, so search engines are still asked not to index it.
- `/mcp` and every `/api/*` path keep `Authorization: Bearer <RAG_MCP_TOKEN>`, checked again by `api/rag_server.py`,
  and stay closed (503) while the token is unset. The author asked about the site's login, not the server's.
- `middleware.js` holds the rule; `scripts/auth_selftest.js` holds its 12 cases, among them „the site opens with no
  variable set at all“ and „/mcp without RAG_MCP_TOKEN stays closed“.

This replaces decision 029 §5 for the website; §5 still holds for `/mcp`.

## What was weighed

- **The repository is public on GitHub** (`api.github.com/repos/netzkontrast/kohaerenzprotokoll`: `"private": false`),
  `Sources/drive/` included. The site renders that repository; its login kept out nothing GitHub does not already serve.
- **The app's frames are not filtered the way the static pages are.** `static_pages.py` and the MCP index withhold every
  line holding an earlier name or the trauma symbol (`rag.WITHHELD_LINE`, decisions 028, 029); the frames and
  `agents/data.json` do not. On the build of 2026-10-26, 883 strings in `agents/data.json` match that pattern — wiki
  sections, reading questions (100 of their ids), reconciliation records. Some are the English word „shadow“, which the
  pattern also catches. Opening the site makes them readable at the site's address as well as on GitHub. This is noted
  as a question for the author, not decided here: scrub the frames as the static pages are scrubbed, or leave them.

## What was rejected

- Keeping the login and setting `SITE_PASSWORD` instead: the author asked for the login to go.
- Opening `/mcp` with the site: not asked; the MCP server's token stays.

## What would change our mind

- The author wants the site private again → set the old rule back from git (`git log -- middleware.js`).
- Someone the site was not meant for reads the frames' earlier-name lines → scrub the frames at build time, as
  `static_pages.py` does, before anything else.
