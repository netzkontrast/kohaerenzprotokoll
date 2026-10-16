# Brief — readings from document 340 (step 6)

1 document, one reader, one batch: `ingest-341`. Files go to `Plan/runs/ingest-341/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 340 | `ki-agenten-kohaerenz-und-prompt-generierung` | 2025-08-05 | „the AI-agent whitepaper“ (an unsigned German technical whitepaper) | a specification for AI agents that borrows the name „Kohärenz-Protokoll“ for navigating a Zettelkasten-style knowledge graph through Maps of Content, with a self-evaluating meta-prompt; it names none of the novel's figures and is not about the novel's world; light pass, no readings |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (368 lines for `ki-agenten-kohaerenz-und-promp`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** No readings are written. The document is a technical specification for AI agents; its „Kohärenz-Protokoll“ is a protocol for an agent's knowledge base, not AEGIS's protocol or the novel's coherence. The census and note stand as the record that it was read.

## Pages — document 340, `ki-agenten-kohaerenz-und-prompt-generierung`

- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L44. not read: the whitepaper's `Kohärenz` is the property of an agent's knowledge base, not the novel's term.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz-Protokoll` (near `koharenz`), `Kohärenz-Protokolls` (near `koharenz`), `Kohärenz-Lücke` (near `koharenz`). occurrence: the whitepaper's protocol for AI agents and its coherence gap, another sense; not read.


**Record entries:** none.

**Not promoted:** everything — the agent protocol, the meta-prompt, Maps of Content, the tools and agents it names, and the borrowed concepts (constitutional AI, meta-prompting, Zettelkasten, RAG, RLAIF).

**No reader**: no readings are written.

**Chapter readings**: none — the document is not about the novel.
