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

Vercel Authentication covers the function too. A client sends `x-vercel-protection-bypass: <secret>` (Vercel's
*Protection Bypass for Automation*); Claude Code takes headers in its MCP configuration. A claude.ai connector would
need OAuth — built only on the author's word.

## 5 · What leaves the container

The serving index holds the landed documents' lines, the wiki's pages and quotations, and the records — on Vercel,
behind its login (decision 029 §3). Nothing is sent to a model by the server.

## 6 · Steps

1. `scripts/rag.py` with its selftest, in `selftests.py`.
2. `api/mcp.py` and an in-memory test with FastMCP's client in `.venv-mcp`.
3. `web.py` builds the serving index; `vercel.json` bundles it with the function.
4. Run the ASGI app locally and call it over HTTP with FastMCP's client.
5. After the merge: call the production deployment with the bypass header.

```yaml
name: mcp-server        # provisional
# may not: write anything, answer in prose, send text to a model, run outside Vercel's login
# retire when: no session has called it in 20 sessions after it is deployed
```
