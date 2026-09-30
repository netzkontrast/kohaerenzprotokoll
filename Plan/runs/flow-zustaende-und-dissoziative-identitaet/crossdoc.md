# Other documents on the pages `flow-zustaende-und-dissoziative-identitaet` reads onto

`python3 scripts/crossdoc.py doc flow-zustaende-und-dissoziative-identitaet`: whole-word counts of each page's surfaces over every landed document (`corpus.py`), never a search rank. A document that writes a name may say nothing about the thing: open the line before using it.

| page | read on it | read, not on it | unread that write it | the unread, most first (count, line) |
|---|---|---|---|---|
| `alters` | 42 | 1 | 174 | `charakterkonzepte-fuer-kohaerenz-protokoll` 79× L29; `kohaerenz-protokoll-konzept` 55× L19; `kohaerenz-protokoll-plot-blueprint-erstellung` 48× L101; `kohaerenz-protokoll-plot-entwicklungsauftrag` 38× L27; `orte-konzept-fuer-kohaerenz-protokoll` 34× L29 |
| `entropie` | 34 | 1 | 240 | `emergenz-autonomer-systeme-aegis-forschung` 41× L33; `aegis-singularitaet-jenseits-entropiegleichung-2` 41× L25; `umfassendes-lokalitaeten-konzept-fuer-roman` 38× L34; `paradoxien-der-kohaerenz-protokoll-entwicklung` 32× L19; `lokalitaeten-konzept-fuer-roman-simulation` 31× L37 |

**Related, not named (`P_BM25`)** — lines that share a page's words and write none of its names. Each may be a tension, a parallel, the same thing, or noise: judge it with `python3 scripts/bm25rel.py label <id> tension|parallel|same|noise --by "<you>"`.

- `alters` → `line:the-coherence-protocol-a-world-bible:133` — - Lowered amnesic barriers between alters. (`bm25:49aa46fb85bb`)
- `alters` → `line:charakterkonzepte-fuer-kohaerenz-protokoll:738` — 35. gatekeeper alters? : r/DID - Reddit, Zugriff am April 18, 2025, <https://www.reddit.com/r/DID/comments/115qa4y/gatekeeper_alters/> (`bm25:1a59994d6a6b`)
- `alters` → `line:kohaerenz-protokoll-forschungsaufgabe:347` — 38. Types of alters : r/DID - Reddit, Zugriff am Juli 29, 2025, <https://www.reddit.com/r/DID/comments/mwk07k/types_of_alters/> (`bm25:ce8e8e02c24a`)

**Read, but not on the page** — each is a sweep to re-check or an occurrence:

- `alters` ← `aegis-subplots-kapitelweise-system-exploration-docx` 6× L126
- `entropie` ← `aegis-subplots-kapitelweise-system-exploration-docx` 32× L60
