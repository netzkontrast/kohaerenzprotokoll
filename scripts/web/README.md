# `scripts/web/` — the website's one vendored file

`support.js` is the runtime a claude.ai Design canvas serves to each of its frames as `./support.js`. Without it a `.dc.html`
file is inert markup; with it, the frame renders in any browser. `scripts/web.py` puts it beside the frames `ui.py` derives, and
Vercel serves the result (`vercel.json`).

| | |
|---|---|
| copied from | `artifact-type/dc-runtime.js` of https://claude.ai/artifact/1EyhQkX3MpiRTw3TxjTjYL |
| type release | `1790869903-0489` of the Design type, canvas version `1790948666-f8f0` |
| copied on | 2026-10-02 |
| sha256 | `454cb23fe5f5b1c4c7cd178795ec6cf3c32047eae4434e975a6104c53183fbd6` — `web.py` refuses any other |
| loads at run time | React and ReactDOM 18.3.1 from `cdn.jsdelivr.net`, with integrity hashes; the app's fonts from Google Fonts |
| contains | React's production build (MIT, © Facebook, Inc. and its affiliates — the licence header is kept in the file) |

It is pinned, not fetched. If the canvas's type moves to a new release and the website stops matching the canvas, copy the new
`artifact-type/dc-runtime.js` here, update `RUNTIME_SHA256` in `web.py` and this table, and name the release in the commit.
