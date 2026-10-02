# The project app on Vercel — what is built, and the plan from here

*2026-10-02. Decision 022 records the choice; this page is the how and the next steps. Everything marked **[built]**
exists in this commit; **[next]** is proposed and not built.*

## 1 · What the canvas is, measured

The canvas https://claude.ai/artifact/1EyhQkX3MpiRTw3TxjTjYL holds seven `.dc.html` frames and a `canvas.json`.
`Main.dc.html` (1.0 MB published, 3.5 MB derived today) is the whole app: markup, data and component. The six other
frames are 600-byte shells that `<dc-import>` it on another screen. Each frame loads `./support.js`, which the canvas
serves from its Design type: a React-based runtime (`artifact-type/dc-runtime.js`, 188 KB) that boots any `<x-dc>`
document, fetching React 18.3.1 from jsdelivr with integrity hashes.

Tested in Chromium in this container: the published frames, served by a plain static server beside a copy of that
runtime, render and navigate the same as on the canvas. **So the app needs no server and no build tool, only its
runtime.** The published version is a snapshot of `bdecc3d` (2026-09-24, 92 pages, 123 graph nodes); `ui.py` derives
today's (106 pages, 187 nodes) in about 90 s with the standard library.

## 2 · What is built

| piece | what | status |
|---|---|---|
| `scripts/web/support.js` | the canvas runtime, vendored, pinned by sha256; provenance in `scripts/web/README.md` | **[built]** |
| `scripts/web.py` | `ui.py --no-checks`, then frames + runtime → `Plan/derived/web/`; `--no-build`, `--check` | **[built]** |
| `ui.py` | names `VERCEL_GIT_COMMIT_SHA` when there is no `.git` (a Vercel build has none), so the rail still names its commit | **[built]** |
| `vercel.json` | no framework, no install, build `python3 scripts/web.py`, output `Plan/derived/web`, `/` → `Main.dc.html`, `noindex` | **[built]** |
| Vercel project | `kohaerenzprotokoll`, Git-connected, Vercel Authentication on all deployments | **[built]** |

Every push to any branch builds a preview; a push to `main` builds production. Tested from a tree holding only the
tracked files, no `.git` and no `Plan/derived/`: 94 s, all eight files written, the app renders with current data.

## 3 · What a person decides

1. **Public or private.** It is private (Vercel login) until the author says otherwise. Public means the wiki's
   quotations from unpublished research are on the open web; `noindex` keeps search engines off, not readers.
   A middle way is Vercel's password protection (a paid Vercel feature) or a shareable link per deployment.
2. **Which branch is production.** `main`, Vercel's default. Previews of every branch cost about 90 s of build each;
   if that is noise, `vercel.json` can skip builds whose diff touches nothing the app reads (`ignoreCommand`).

## 4 · The plan from here **[next]**, in order, each one PR

1. **Run the invariants in the build.** `web.py` calls `ui.py --no-checks`, so the rail shows `—` for prose numbers. With
   the checks the build takes longer (they run `state.py` and the self-tests); measure it on Vercel before turning it
   on. Alternatively, have GitHub's `checks.yml` write its results as an artifact the build reads — only if the
   in-build run is too slow.
2. **A check in CI.** Add `python3 scripts/web.py --no-build --check` after a `ui.py --check` step to `checks.yml`
   once `ui.py --check` is fast enough for every push; until then the Vercel build is the check, and a failed build
   shows on the pull request as a failed Vercel status.
3. **Fit the screen.** The frames are fixed at 1440×900 because a canvas frame is. On the website, a wrapper page
   that scales `Main.dc.html` to the window (or a fluid root under a `web` flag in `ui.py`) — a change to the app, so
   it is measured against the canvas: the canvas must still render byte-identical frames.
4. **Deep links.** The app switches screens in its state, so a URL cannot name a page. `ui.js` reading
   `location.hash` (`#wiki/aegis`) would make every page, conflict and question linkable — and the canvas ignores
   the hash, so it costs the canvas nothing.
5. **Runtime drift.** `web.py` refuses a runtime whose hash it does not know. A small `web.py --compare` that reads
   the canvas's current `dc-runtime.js` (from a Claude session, by the Artifact tool) and reports whether the pin is
   behind would make an update a measured step rather than a surprise.

What is deliberately not planned: a server, an API, a database, or editing through the website. The app shows what
the repository states; changing it is a commit.
