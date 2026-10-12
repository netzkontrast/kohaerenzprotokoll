# Brief — readings from document 289 (step 6)

1 document, one reader, one batch: `ingest-290`. Files go to `Plan/runs/ingest-290/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 289 | `romananfang-leere-und-systemgenesis` | 2025-04-17 | „the opening analysis and draft“ (an unsigned German analysis with a chapter draft) | an analysis of how to open the novel with emptiness and AEGIS's algorithmic perspective, a protocol-to-narration table, a recommendation to keep a four-part structure, and a draft „Kapitel 1: Genesis im Echo der Leere“ with an English protocol log in AEGIS's voice and a Universal Reboot; it calls itself an analysis and a draft (L11, L154) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (221 lines for `romananfang-leere-und-systemge`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis with a draft: write „the opening analysis proposes / describes …“ for Part I and „the chapter-1 draft has / narrates …“ for Part II (L154 onward); the protocol table's rows are hedged suggestions (`vermutlich`, `möglicherweise`). The log is bold English in AEGIS's voice — cut quotations before bold markers.

## Pages — document 289, `romananfang-leere-und-systemgenesis`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L25, L31, L39, L51, L55, L71, … (44 lines); `Entropic Gatekeeper` L83, L104. central (3–6): „Autonomous Entropic Gatekeeper for Integrity Systems“, regulating entropy and securing coherence (L83); a non-anthropomorphic, purely functional control core (L55, L220); existence based on function (L73); its perspective as an interpreted system log (L75); the Universal Reboot not a mere restart (L93, L117); in the draft's log the threat signature and the reboot (L168–L212).
- **`aegis-teilfunktionen`** (central, 3–12 quotations): the census's surfaces — `Integrity Guardian` L75, L95, L109, L176; `Cognitive Firewall` L95, L110, L178; `SIS` L97, L108, L114, L182, L196, L204, … (7 lines). central (3–6): the protocol table mapping AEGIS's functions to narrative actions (L99–L115): Entropic Gatekeeper (L104), Zero-Trust Execution Model (L105), Real-time self-verification (L106), Integrity Guardian (L109) — suggestions; the Integrity Guardian module's report in the log (L176).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L73. minor (1–3): the threat read as a catastrophic, uncontrolled rise of entropy (L89); L73 only if it adds.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L156. minor (1–3): the draft's chapter title „Genesis im Echo der Leere“ (L156) and „Eine Genesis, diktiert von Algorithmen“ (L208).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L106. not read: occurrence — `Kohärenz` (L106) inside a table cell, read on aegis-teilfunktionen.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L83, L202. minor (1–3): only if L83 or L202 places the Risse; else not read.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L87, L96, L202, L210. minor (1–3): the Überwelt reformed after the reboot, sterile and pure, verified by AEGIS (L210); L87, L96 only if they add.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie`: `digitale Entropie` (near `entropie`). occurrence: `digitale Entropie` read with the entropy reading.
- `genesis`: `Genesis im Echo der Leere` (near `genesis`). reading: the chapter title (L156).


**Record entries:** none.

**Not promoted:** the four-part structure, Śūnyatā and the vacuum analogy, the nicht-lokale Nicht-Existenz, the Universal Reboot Protocol, the AEGIS Functional Protocol v1.4, the source codes S_S03–S_S05.

**One reader**: every page above and the chapter reading below.

**Chapter readings** (the same reader, into `Plan/runs/ingest-290-kap/readings/kap-01--romananfang-leere-und-systemgenesis.md`): Kap 1 — the draft „Kapitel 1: Genesis im Echo der Leere“ (L156): the second-person address on non-existence (L166), the protocol log (L168–L200), the reboot narration (L202–L220); a draft, not the chapter as approved.
