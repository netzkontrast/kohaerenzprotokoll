# Brief — readings from document 343 (step 6)

1 document, one reader, one batch: `ingest-344`. Files go to `Plan/runs/ingest-344/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 343 | `kohaerenz-protokoll-als-algorithmische-grundlage-fuer-narrat` | 2025-08-20 | „the narrative-coherence essay“ (an unsigned German essay, PDF-style export) | an essay on narrative coherence and algorithmic systems for it — story bibles, ontologies, NCP and Dramatica, the SCORE framework, planners and validators — that uses „Kohärenz-Protokoll“ for such a system; it names none of the novel's figures and is about narrative systems in general; light pass, no readings |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (1009 lines for `kohaerenz-protokoll-als-algori`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** No readings are written. The document is a general essay on narrative coherence and algorithmic tools; its „Kohärenz-Protokoll“ is such a tool, its `Kontrollinstanz` a generic validator, not AEGIS's protocol or the novel's world. The census and note stand as the record that it was read.

## Pages — document 343, `kohaerenz-protokoll-als-algorithmische-grundlage-fuer-narrat`

- **`aegis`** (minor, 1–4): the census's surfaces — `Kontrollinstanz` L610. not read: the essay's general sense of narrative coherence and control, not the novel's term.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: the essay's general sense of narrative coherence and control, not the novel's term.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `SCORE` (near `globalerentropiescore`). occurrence: the essay's coherence tools and the SCORE framework, another sense; not read.
- `kohaerenz`: `Kohärenz-Protokoll` (near `koharenz`), `Kohärenz-Protokolls` (near `koharenz`), `temporale Kohärenz` (near `koharenz`), `Kohärenz-Detektor` (near `koharenz`). occurrence: the essay's coherence tools and the SCORE framework, another sense; not read.


**Record entries:** none.

**Not promoted:** everything — the essay's protocol, story bibles, ontologies, the SCORE framework, planners and validators, and the borrowed systems (NCP, Dramatica, OntoMedia).

**No reader**: no readings are written.

**Chapter readings**: none — the essay is not about the novel.
