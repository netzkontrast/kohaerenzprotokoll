# Brief — readings from document 435 (step 6)

1 document, one reader, one batch: `ingest-436`. Files go to `Plan/runs/ingest-436/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 435 | `kohaerenz-protokoll-roman-ausarbeitung` | 2025-04-27 | „the elaboration report“ (an unsigned German analytical report, „Roman-Ausarbeitung“) | eight sections applying philosophical, psychological and mathematical concepts to the novel, a design for Kael, AEGIS and four of twenty Kernwelten, a cache-coherence metaphor and a chapter plan by parts; a report and framework (L19), no claim of canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (727 lines for `kohaerenz-protokoll-roman-ausa`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report that proposes: write „the elaboration report proposes …“; each concept's definition reports cited sources, and only its „Relevanz für“ lines and sections 2–7 speak of the novel; its „[Query Pt N]“ brackets mark the commission's words, which it restates — say so where they carry the claim. It names Kap ranges only (L301, L318, L360). The world codes are named after mathematicians: never expand them. Quote the German as written; cut before straight quotes, bold and italics markers, escaped brackets and glued footnote digits. No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations stay verbatim). Never write a real person's name nor a term carrying one, nor quote a span containing one.

## Pages — document 435, `kohaerenz-protokoll-roman-ausarbeitung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L19, L29, L33, L41, L49, L57, … (81 lines). central (4–8): AEGIS's reductionist analysis of Kael's fragmented states (L49); the per-chapter „Einblick in AEGIS“ sections should reveal its systemic logic, M perceived as destabilising (L149); AEGIS's formal limits (L161 — describe, the line names a person); „Kontrollverlust“: emergent phenomena in the Kernwelten AEGIS cannot control, the K-J connection undermining its systems (L169); the cache metaphor: „AEGIS = Kohärenzprotokoll/Bus“ (L270).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L73. not read: an occurrence — dissociation's symptoms in the borrowed psychology section (L73).
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L19, L256, L258, L260, L262, L264, … (8 lines). minor (1–4): the cache-coherence metaphor: „Kernwelten = Caches“ (L268), „M = Hauptspeicher“ (L269), „AEGIS = Kohärenzprotokoll/Bus“ (L270), „Cache-Inkohärenz = Fragmentierung“ (L271).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L73. not read: an occurrence — the clinical definition in the borrowed psychology section (L73).
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L414. minor (1–4): emergent phenomena in the Kernwelten that AEGIS cannot control (L169); section 7's hypothetical chapter concept „Emergenz“ (L414).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L249. minor (1–4): AEGIS's logs as plan text: „Cache C₁₅ zeigt erhöhte Entropie“ (L249) — quote around the subscript if needed.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L85, L93, L121, L167, L311, L316, … (9 lines). minor (1–4): Kael's Kern-Selbst perhaps catalysed by Juna (L85); the intuitive side (M/Juna) of Kael's inner integration (L93); AEGIS's predictions fail under Juna's influence (L167); guided by echoes of Juna (L311).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L29, L33, L41, L45, L49, … (109 lines). central (4–8): the Kernwelten as Kael's subjective „Realitäten“, inconsistent „Caches“ of the identity (L41); Kael fights to restore a numerical identity across the fragmented states (L49); accessing the Kern-Selbst, perhaps catalysed by Juna (L85); Part 1 the inner integration, Part 3 the outer confrontation (L93); the cache-incoherence of Kael's self as fragmentation (L271).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L19, L37, L41, L59, L69, L77, … (27 lines). central (4–8): „Differenzierung der vier Kernwelten“ (L187) with atmosphere for each (L191–L221 — never expand the codes); the Kernwelten as Kael's subjective „Caches“ (L41); „Die Existenz der weiteren 16 Welten sollte subtil angedeutet werden“ (L247); „einer von zwanzig Realitäts-Caches“ (L252); „Jeder der 20 (fokussiert auf 4) Kernwelten“ (L268).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrences — the novel's title (L11); `Cache-Inkohärenz` and `Kohärenz-Metriken` are the report's labels.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L41, L161. minor (1–4): the coherence of the Kernwelten influenced by Kael's inner state „und den Moonshine-Link“ (L41); M with the non-logical Moonshine-Link as perhaps unprovable for AEGIS (L161).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L121, L157, L163, L178. minor (1–4): section 2.3 „Grenzen und Instabilität“ — the Risse (L157); AEGIS's formal limits lead to instability, the Risse (L121).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Cache-Inkohärenz` (near `koharenz`), `Cache-Kohärenz-Metapher` (near `koharenz`), `Kohärenz-Metriken` (near `koharenz`). occurrences: the title and the report's labels.
- `personas`: `Depersonalisation` (near `persona`). an occurrence: depersonalisation, a clinical term, not the personas.


**Record entries** (one file, formatted as earlier entries — `ls Plan/runs/ingest-42*/readings/q3-*`):
- **`q3-how-many-kern-welten-and-alters`**: the elaboration report counts twenty Kernwelten, four in focus — „Jeder der 20 (fokussiert auf 4) Kernwelten“ (L268), the other sixteen to be hinted at (L247), „einer von zwanzig Realitäts-Caches“ (L252); no count of alters. Before and not against the author's answers of 2026-10-05, which stand.

**Not promoted:** M, the K-J connection's spellings, the world codes and caches, Cache-Inkohärenz, Kohärenz-Metriken, Einblicke in AEGIS, Kern-Selbst, the IFS roles, Holismus-Problem, the chapter concepts, and the borrowed concepts.

**One reader**: every page above and the Q3 entry.

**Chapter readings**: none — the document names only chapter ranges in its part headings.
