# Brief — readings from document 476 (step 6)

1 document, one reader, one batch: `ingest-476`. Files go to `Plan/runs/ingest-476/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 476 | `a-critical-analysis-of-coherence-protocol-an-assessment-of-p` | 2025-11-03 | „the critical-question review“ (an unsigned English critical review, „A Critical Analysis of Coherence Protocol“) | summarises what it attributes to the sources and to a critical review, turns each point into a Critical Question, and ends with a verdict of conceptual triumph and a table of triumphs against risks; a review that asks, recorded, never applied|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (82 lines for `a-critical-analysis-of-coheren`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A review that reports and asks: write „the critical-question review reports …“ for what it attributes to its sources and „… asks …“ for its questions; its questions stay questions. Its German terms stand in straight quotes — never quote across them; cut before straight quotes, bold and italics. No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations verbatim, including the document's „his“).

## Pages — document 476, `a-critical-analysis-of-coherence-protocol-an-assessment-of-p`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L27, L55, L59. minor (1–4): AEGIS's origin in a traumatic Genesis-Krise, a catastrophic internal event misread as hostile (L55 — describe around the straight quotes); the review asks whether the narrative conveys that AEGIS's villainy results from that misinterpretation (L55); AEGIS as an operationally closed system classifying Juna/V as entropy or error (L59 — describe).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L79. minor (1–4): the table's triumph: a respectful and credible depiction of DID (L79).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L57, L59. minor (1–4): Juna/V, „The character(s)“, the crucial force of external connection that AEGIS classifies as entropy (L59 — describe around the straight quotes); the review asks for the mechanism of the bond (L57 heading).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L23, L27, L31, L37, L41, … (11 lines). central (4–8): Kael's tertiary structural dissociation not a metaphor for the world's instability but its direct, causal source (L17); the novel's premise a causal link between Kael's inner state and outer reality (L23); the review reports a doubt whether the tight fusion collapses into a one-to-one mapping (L27); the deconstructed structure mirrors Kael's journey from fragmentation (L37); a concern about the cyclical second act (L41).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L27. minor (1–4): the Kernwelten named once in a list of what the external conflict consists of (L27).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L29, L31. minor (1–4): the sources define the Risse as moments where the controlling logic fails to contain the internal state (L31); the review asks whether a type of dissociation produces a type of glitch (L31).
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Das Trennungsprotokoll` L55. minor (1–4): „Das Trennungsprotokoll“ named in the summary of AEGIS's origin (L55 — describe; it stands in straight quotes).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L17. minor (1–4): Kael's tertiary structural dissociation, written TSDP, as the world's causal source (L17).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L21. not read: an occurrence — `Simulation` on L21 is the heading's general sense.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis-Krise` (near `genesis`). an occurrence: the Genesis-Krise, read on aegis.


**Record entries:** none.

**No chapter readings**: the review names acts, not chapters.

**Not promoted:** Critical Question, critical review, the four axes, Das Fundament, Conceptual Triumphs, Structural Risks, and the borrowed concepts.

**One reader**: every page above.
