# Brief — readings from document 62 (step 6)

1 document, one reader, one batch: `ingest-62`. Files go to `Plan/runs/ingest-62/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 62 | `hard-sci-fi-cosmic-horror-research-questions` | 2026-01-02 | „the Cosmic-Horror research report“ | an English research report on Hard-SF Cosmic Horror (borrowed theories and narrative techniques, open questions, recommendations, 120 references); its section 6 reports another document, its reference 87 „Plotanalyse: Kohärenz Protokoll Szenario“ (L358), as a case study |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (392 lines for `hard-sci-fi-cosmic-horror-rese`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Everything this document says about the novel is a **report of another document**, its reference 87 (`plotanalyse-kohaerenz-protokoll-szenario`, landed and unread): L143, L187–L205. Every reading says so — „the report says the analysed Plotanalyse proposes …“ — and never gives the claim to this document or to the novel. The theories (Monster Group, Moonshine, Gödel, IFS, IIT, Constructor Theory) are borrowed; their general sections (L141, L241–L242) are no reading. English quotations stay English.

## Pages — document 62, `hard-sci-fi-cosmic-horror-research-questions`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L187, L196, L197, L198, L203, L205. minor (2–4): in the analysed scenario AEGIS is the AI (L187) and stands for „Reductionism (AEGIS)“, „the scientific imperative to dissect and categorize (Eliminativism)“ (L203); Gödel's incompleteness is „The flaw in AEGIS's logic“ (L198), failing because it tries to prove a truth (M) outside its axioms (L198); its violent attempts to force M into a reductionist box fragment Kael's psyche (L205).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L199, L205. minor (1–2): in the analysed scenario IFS gives „The structure of Kael's fragmented mind (DID)“ (L199), and the fragmentation (DID) results from AEGIS's attempts (L205).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L187, L197. minor (1–2): the connection written `Juna/Moonshine` (L187) and Monstrous Moonshine as „The mechanism of the Kael-Juna connection“ (L197). Nothing else about Juna.
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L187, L196, L197, L199, L205. minor-to-central (2–4): in the analysed scenario Kael is „a human avatar of a cosmic entity (Kael/M)“ (L187); the Monster Group defines the nature of the entity M and Kael's psyche (L196 — quote around the inner straight marks); Kael's parts correspond to the Monster's subgroups and his healing is their integration (L199); the fragmentation of his psyche by AEGIS (L205). The page already holds `Kael/M` from other sources; say this report gives it as the analysed document's.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L143. not read: L143 is the analysed document's title only (sweep: occurrence).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L216. not read: L216 is a general heading on the ethics of simulation (sweep: occurrence).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `alex`: `technological explosion` (near `alex`). occurrence: `technological explosion` matches only after folding (J69).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title of the analysed document (J17).
- `moonshine-link`: `Moonshine` (near `moonshinelink`). reading (1–2): the analysed scenario's Monstrous Moonshine as „The mechanism of the Kael-Juna connection“ and „A metaphor for non-local, acausal connection“, a hidden order that bypasses AEGIS's protocols (L197). Reported, not this document's.


**Pages the lookup did not list, added by the reconciler:**

- **`potentialmeer`** (minor, 1): the analysed scenario uses Constructor Theory, the `Potential Sea`, to show reality's raw material before AEGIS collapses it into facts (L205). An English name placed by the sentence (J100): say the report writes `Potential Sea`, never `Potentialmeer`.
- **`goedel-gambit`** (minor, 1): L198 — in the analysed scenario AEGIS fails because it tries to prove a truth (M) outside its axiomatic system, leading to its cognitive instability. Read only if the digest's subject is that move; the report never writes `Gödel-Gambit` (count it).
- **`alters`** (minor, 1): L199 — Kael's parts correspond to the Monster's subgroups and healing is their integration (the analysed scenario's).

Conflicts and questions the reconciler checked: none touched beyond these pages — the report gives no count of parts (Q3), no boundary of the link beyond non-local and acausal (Q9: a one-line entry only if the digest of Q9 lacks that position; else none), nothing on Guardians, worlds or chapters.
