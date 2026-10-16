# 029 — The project's retrieval tools as a FastMCP server on Vercel

**Date:** 2026-10-16 · **Decided by:** the author (what), the session (how) · **Status:** building

## What was asked

> Oder vielleicht besser noch — als mcp Server deployed auf vercel

and, as the session's goal the same day:

> improve ui and deployment — and even develop an fastmcp Server for the Tools we developed — so that we can Host
> the Search and other Tools as Full rag System in vercel

The concept is `Plan/concept/mcp-server_2026-10-16.md`.

## What was chosen

1. **A FastMCP server in the same Vercel project** (`api/mcp.py`), read-only, built only from `main`: search over the
   landed documents, the wiki's verified quotations and its pages; graph retrieval as `graphrag.py` does it; a line
   window with its numbers; a quotation checked against its line; and the app's items (page, conflict, question,
   chapter, document record, state, sessions).
2. **The retrieval core is the standard library** (`scripts/rag.py`), like every pipeline script: a compact SQLite
   FTS5 index and the graph, both derived at build time, never committed. FastMCP is only the transport and lives in
   its own pinned dependency, never in the system Python.
3. **The landed documents' lines go to Vercel.** A full RAG system searches the sources, so their text is in the
   index the function reads. That is more than decision 022 sent (the wiki's quotations); the author's goal is the
   decision to send it. It stays behind Vercel Authentication.
4. **Access by Vercel's protection-bypass secret** in a request header, which the author creates in Vercel and gives
   to the clients the author names; never in the repository or a chat. A claude.ai connector needs OAuth and is
   built only if the author asks for it.

## What was rejected

- **Serving `Plan/derived/ask.db`** (355 MB, a GraphQLite extension): over a function's size limit, and its proposal
  layers are not for serving.
- **`mcp-handler` with Next.js**: a JavaScript toolchain for one route in a standard-library project.
- **Embeddings in the function** (novelgraph's model, about 0.5 GB): too large for a function; lexical BM25 and the
  graph walk first, vectors only if a measurement says lexical retrieval misses what a reader needs.
- **Answers written by a model**: the server returns evidence with document and line, never prose (P13); a client's
  model may answer from it.

## What would change our mind

- The author wants the wiki in claude.ai → OAuth (concept §4).
- The function cannot read the build's index within Vercel's limits → bundle a smaller index or move search to a
  hosted database.
- A measured retrieval gap that only vectors close → add static vectors to the index.
