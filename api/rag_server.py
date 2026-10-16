"""The project's retrieval tools as an MCP server: FastMCP over Streamable HTTP, for Vercel (decision 029).

Every tool is a thin wrapper of `scripts/rag.py`, which holds the logic and its selftest; this file only names the
tools, types their arguments and turns a refusal into an MCP error. The server is stateless and answers in JSON, so
each request stands alone — what a serverless function needs. It writes nothing and returns evidence with document
and line, never prose (P13).

    .venv-mcp/bin/python api/rag_server.py              # serve on http://127.0.0.1:8000/mcp
    .venv-mcp/bin/python api/rag_server.py selftest     # every tool through FastMCP's in-memory client

The file is not called `mcp.py`: run as a script, that name would shadow the `mcp` package FastMCP imports.

On Vercel the module-level `app` is the ASGI application; `vercel.json` rewrites `/mcp` to it, and it answers on any
path it is given, and the serving index is the
`Plan/derived/serve/serve.db` that `scripts/web.py` builds in the same deployment. Access is Vercel Authentication;
the project's own login (`middleware.js`) asks for `Authorization: Bearer <RAG_MCP_TOKEN>`, and this app checks it
again; on Vercel (`VERCEL` set) it refuses every request while the token is unset. Locally the token is optional.
"""

from __future__ import annotations

import asyncio
import contextlib
import hmac
import os
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "scripts"))

from fastmcp import FastMCP  # noqa: E402
from fastmcp.exceptions import ToolError  # noqa: E402

import rag  # noqa: E402

PATH = "/api/mcp"
INSTRUCTIONS = """Retrieval over the Kohärenz Protokoll project: a German hard-SF novel's research corpus and its wiki.
Every answer is evidence — a document line, a verified quotation, a wiki record — with where it stands; nothing is
summarised and nothing is canon unless Manuscript/kanon.md lists it. Cite as `slug.md:Lnn`. Use `ask` for a question,
`search` for words, `read_lines` to read around a hit, `verify_quote` before quoting. Canon prose is German."""

mcp = FastMCP("kohaerenzprotokoll", instructions=INSTRUCTIONS)
_store: rag.Store | None = None


def store() -> rag.Store:
    global _store
    if _store is None:
        _store = rag.Store()
    return _store


def call(fn, *args):
    try:
        return fn(*args)
    except rag.Refused as e:
        raise ToolError(str(e)) from None


@mcp.tool
def search(query: str, scope: str = "sources", limit: int = 10) -> dict:
    """BM25 search. scope: `sources` (lines of the read documents), `quotes` (verified quotations on wiki pages),
    `items` (wiki pages, conflicts, questions, chapters, records, notes). Each hit carries its document and line."""
    return call(store().search, query, scope, limit)


@mcp.tool
def ask(question: str, k: int = 8) -> dict:
    """Graph retrieval for a question: the wiki pages it names, PageRank over the wiki's graph, the verified quotations
    chosen by relevance and diversity, the conflicts and questions touching them, plus BM25 lines from the sources.
    Evidence, not an answer."""
    return call(store().ask, question, k)


@mcp.tool
def read_lines(slug: str, start: int, end: int) -> dict:
    """A document's lines with the file line numbers a citation names (at most 200 per call)."""
    return call(store().read_lines, slug, start, end)


@mcp.tool
def verify_quote(slug: str, quote: str, line: int | None = None) -> dict:
    """Whether the words stand on a line of the document, by the project's own quotation check; if not, the nearest
    lines. Pass `line` to check a claimed citation."""
    return call(store().verify_quote, slug, quote, line)


@mcp.tool
def item(kind: str, id: str) -> dict:
    """One record as markdown with its repository path. kind: page (a slug), conflict (C2), question (Q3),
    chapter (13), record, note, census (a document slug), decision (029), now (NOW)."""
    return call(store().item, kind, id)


@mcp.tool
def list_items(kind: str) -> dict:
    """Every id and title of one kind (page, conflict, question, chapter, record, note, census, decision)."""
    return call(store().listing, kind)


@mcp.tool
def document(slug: str) -> dict:
    """A read document's manifest facts and its line range; its text through `read_lines`."""
    d = call(store().document, slug)
    return {k: d[k] for k in ("slug", "title", "category", "date", "tier", "offset")} | {
        "last_line": d["offset"] + len(d["lines"]) - 1, **store().provenance()}


@mcp.tool
def state() -> dict:
    """Every measurement of the repository at the snapshot, with how it was measured."""
    return store().state()


@mcp.tool
def sessions() -> dict:
    """The next working sessions, as NOW.md plans them."""
    return store().sessions()


# ── the ASGI application ───────────────────────────────────────────────────────

_inner = mcp.http_app(path=PATH, stateless_http=True, json_response=True)


class App:
    """The FastMCP app, with two things a serverless host may not give it: its lifespan is entered on the first
    request if the host never sent one, and an optional bearer token is checked before anything runs."""

    def __init__(self, inner):
        self.inner = inner
        self._stack: contextlib.AsyncExitStack | None = None
        self._lock = asyncio.Lock()
        self._host_started = False  # the host sent lifespan.startup and the app completed it (Vercel's runtime does)

    async def _ensure_started(self) -> None:
        if self._stack is None and not self._host_started:
            async with self._lock:
                if self._stack is None:
                    stack = contextlib.AsyncExitStack()
                    await stack.enter_async_context(self.inner.router.lifespan_context(self.inner))
                    self._stack = stack

    async def __call__(self, scope, receive, send):
        if scope["type"] == "lifespan":
            async def watch(message):
                if message.get("type") == "lifespan.startup.complete":
                    self._host_started = True
                await send(message)
            return await self.inner(scope, receive, watch)
        if scope["type"] == "http":
            # a rewrite may hand over `/mcp` or `/api/rag_server`: the MCP route is the one route this app has
            scope = {**scope, "path": PATH, "raw_path": PATH.encode()}
            token = os.environ.get("RAG_MCP_TOKEN")
            if not token and os.environ.get("VERCEL"):
                # on Vercel the server never runs open: middleware.js and this both need the token (decision 029 §4)
                await send({"type": "http.response.start", "status": 503,
                            "headers": [(b"content-type", b"text/plain")]})
                await send({"type": "http.response.body", "body": b"RAG_MCP_TOKEN is not set: the server stays closed"})
                return
            if token:
                got = dict(scope.get("headers") or []).get(b"authorization", b"").decode()
                if not hmac.compare_digest(got, f"Bearer {token}"):
                    await send({"type": "http.response.start", "status": 401,
                                "headers": [(b"content-type", b"text/plain")]})
                    await send({"type": "http.response.body", "body": b"unauthorized"})
                    return
            await self._ensure_started()
        return await self.inner(scope, receive, send)


app = App(_inner)


# ── selftest ───────────────────────────────────────────────────────────────────

async def _selftest() -> list[str]:
    """Every tool through FastMCP's in-memory client, on rag.py's fixture — no built index needed."""
    import tempfile
    from fastmcp import Client
    global _store
    failures = []
    tmp = tempfile.TemporaryDirectory()
    rag.fixture(Path(tmp.name) / "serve.db")
    _store = rag.Store(Path(tmp.name) / "serve.db")
    async with Client(mcp) as client:
        names = {t.name for t in await client.list_tools()}
        want = {"search", "ask", "read_lines", "verify_quote", "item", "list_items", "document", "state", "sessions"}
        if names != want:
            failures.append(f"tools: {sorted(names ^ want)}")
        r = (await client.call_tool("search", {"query": "Juna erscheint", "limit": 3})).data
        if not r["hits"] or "cite" not in r["hits"][0]:
            failures.append("search: no hit with a citation")
        hit = r["hits"][0]
        w = (await client.call_tool("read_lines", {"slug": hit["doc"], "start": hit["line"], "end": hit["line"]})).data
        if w["lines"][0]["text"] != hit["text"]:
            failures.append("read_lines: the hit's own line differs")
        v = (await client.call_tool("verify_quote", {"slug": hit["doc"], "quote": hit["text"][:40], "line": hit["line"]})).data
        if not v.get("holds"):
            failures.append("verify_quote: the hit's own words do not hold on its line")
        try:
            await client.call_tool("item", {"kind": "page", "id": "no-such-page"})
            failures.append("item: a missing page was not refused")
        except Exception:
            pass
        a = (await client.call_tool("ask", {"question": "Wo erscheint Juna?"})).data
        if not a["graph"]["evidence"]:
            failures.append("ask: no evidence")
    _store = None
    tmp.cleanup()
    return failures


if __name__ == "__main__":
    if sys.argv[1:] == ["selftest"]:
        bad = asyncio.run(_selftest())
        print(f"mcp: {'held' if not bad else 'FAILED'} — " + ("every tool answers through FastMCP" if not bad else "; ".join(bad)))
        raise SystemExit(1 if bad else 0)
    import uvicorn
    # RAG_LIFESPAN=on runs it the way Vercel's runtime does (it sends lifespan.startup); off, the way a host that
    # never sends one does — both must answer
    uvicorn.run(app, host="127.0.0.1", port=int(os.environ.get("PORT", 8000)), lifespan=os.environ.get("RAG_LIFESPAN", "off"))
