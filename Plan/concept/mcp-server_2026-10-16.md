# The retrieval tools as a FastMCP server on Vercel — concept, 2026-10-16

The author, 2026-10-16: „Oder vielleicht besser noch — als MCP Server deployed auf Vercel“, then the goal
„develop an fastmcp Server for the Tools we developed — so that we can Host the Search and other Tools as Full rag
System in vercel“ (decision 029). Each step below is marked *[built]*, *[next]* or *[later]* as it lands.

## 1 · What it is for

An agent in another session — Claude Code, a writing session, a cloud session — can ask the project without cloning
it: search the landed documents and the wiki, walk the graph from a question, read a window of lines, check a
quotation, open a page or a record. The answers are evidence with document and line, never prose (P13), so a client's
model can answer from them and every claim stays checkable.

## 2 · The parts

| part | what | where |
|---|---|---|
| retrieval core | standard library: builds and reads the serving index; every tool's logic | `scripts/rag.py` |
| serving index | SQLite FTS5: every non-empty line of every landed document, every verified quotation on a page, every page section; plus the graph as JSON and the app's items | `Plan/derived/serve/`, built by `web.py` at deploy time |
| MCP server | FastMCP, Streamable HTTP, stateless, JSON responses; each tool a thin wrapper of `rag.py` | `api/mcp.py`, dependencies pinned in `requirements.txt` |
| deployment | the same Vercel project, `main` only; the function bundles the serving index | `vercel.json` |

## 3 · The tools

| tool | returns |
|---|---|
| `search(query, scope, limit)` | BM25 hits — `sources` (document lines), `quotes` (verified quotations on pages), `pages` (page sections) — each with document or page, line, text |
| `ask(question)` | graph retrieval as `graphrag.py`: seed pages, PageRank, verified quotations by MMR, the conflicts and questions touching them; plus BM25 lines from the sources as a second finder |
| `read_lines(slug, start, end)` | the document's lines with their numbers, as `read.py` prints them |
| `verify_quote(slug, quote, line)` | whether the words stand on that line, as `quotes.py` decides; the nearest line if not |
| `page(slug)`, `conflict(id)`, `question(id)`, `chapter(n)` | the record's markdown with its path |
| `document(slug)` | manifest row, note, census and reconciliation record |
| `state()`, `sessions()` | the measurements; the next sessions from NOW.md |

## 4 · Access

**First test without a login** (the author, 2026-10-16; decision 029 §4): the author turns Vercel's protection off for
production in the project's settings, which opens the whole site, not only `/mcp`. Then a client needs no header at
all, and `RAG_MCP_TOKEN` (set in Vercel) puts a bearer token in front of `/mcp` alone when wanted.

While the login is on, Vercel Authentication covers the function too. A client sends `x-vercel-protection-bypass: <secret>` (Vercel's
*Protection Bypass for Automation*); Claude Code takes headers in its MCP configuration. A claude.ai connector would
need OAuth — built only on the author's word.

## 5 · What leaves the container

The serving index holds the read documents' lines, the wiki's pages and quotations, and the records — on Vercel,
behind its login (decision 029 §3), less what §7 withholds. Nothing is sent to a model by the server.

## 6 · Steps

1. *[built]* `scripts/rag.py` with its selftest, in `selftests.py` (`5eafcb36`). The serving index is 54 MB:
   515 read documents, 102 143 lines, 30 582 verified quotations, 1 773 records, built in about 45 s.
2. *[built]* `api/rag_server.py` (not `mcp.py`: run as a script that name shadows the `mcp` package) and its test
   through FastMCP's in-memory client in `.venv-mcp` (`install.sh mcp`).
3. *[built]* `web.py` builds the serving index and the static pages; `vercel.json` bundles `scripts/` and the index
   with the function, keeps the corpus folders out (`excludeFiles`) and rewrites `/mcp` to it. A build from a
   `git archive` with no `.git`, as Vercel builds, took 6 min and wrote everything.
4. *[built]* Called over HTTP with FastMCP's client, both with the host sending the ASGI lifespan (as Vercel's runtime
   does) and without; `RAG_MCP_TOKEN` refuses a request without the bearer token (401).
5. *[next]* After the merge (and, for the first test, with the login off): call `https://kohaerenzprotokoll.vercel.app/mcp`. Branches build no preview
   (since 2026-10-16), so this is the first moment the function runs on Vercel.

## 7 · What is withheld

Measured at the first build: 61 unread documents and 10 whose note marks personal material are not in the index at
all; 864 lines carrying a figure's earlier name or the trauma symbol read `[withheld]`; graph nodes, surfaces and
quotations naming either are dropped, and a record whose own name carries one is not served.

## 8 · Connecting a client

Claude Code, in a project's `.mcp.json` (the secret from the Vercel project's *Deployment Protection → Protection
Bypass for Automation*, kept in the environment, never in a file that is committed):

```json
{"mcpServers": {"kohaerenzprotokoll": {"type": "http", "url": "https://kohaerenzprotokoll.vercel.app/mcp",
  "headers": {"x-vercel-protection-bypass": "${VERCEL_BYPASS}"}}}}
```

With the login off, the same without `headers`. Locally, with no Vercel at all: `scripts/install.sh mcp`, `python3 scripts/rag.py build`, then
`.venv-mcp/bin/python api/rag_server.py` serves `http://127.0.0.1:8000/mcp`.

```yaml
name: mcp-server        # provisional
# may not: write anything, answer in prose, send text to a model, run outside Vercel's login
# retire when: no session has called it in 20 sessions after it is deployed
```
