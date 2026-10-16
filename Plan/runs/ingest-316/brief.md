# Brief — readings from document 315 (step 6)

1 document, one reader, one batch: `ingest-316`. Files go to `Plan/runs/ingest-316/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 315 | `kohaerenz-protokoll-umfassendes-konzept-mit-aegis-manifest` | 2025-04-27 | „the comprehensive concept with the AEGIS manifest“ (an unsigned German concept outline) | a ten-section outline restating vision, plot, cast and setting through an AEGIS-Manifest of three pillars — Sein und Nicht-Sein, Ordnung und Entropie, Kohärenz und Differenz — with „3 Teile à 13 Kapitel“ (L65), each part on one pillar; it says it „bietet eine noch stärkere und philosophisch tiefere Grundlage“ (L102), its claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (103 lines for `kohaerenz-protokoll-umfassende`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A concept outline: write „the manifest concept frames / has …“; the manifest is AEGIS's operative manifest in the outline, and the core conflict is two interpretations of it — record, never apply. Hedges (`möglicherweise`, `vielleicht`) stay. Cut quotations before bold markers and the Δ formula.

## Pages — document 315, `kohaerenz-protokoll-umfassendes-konzept-mit-aegis-manifest`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L15, L17, L19, L48, L52, … (21 lines). central (3–6): the world's principles „als das operative Manifest von AEGIS“ (L19); its unifying definition (L48) and motto „Aus Nichts — durch Chaos — in Identität“ (L54); its flaw an „übermäßig rigiden Interpretation“ (L59); the core conflict „Der Kampf zwischen zwei Interpretationen“ of the manifest (L63).
- **`entropie`** (central, 3–12 quotations): the census's surfaces — `Entropie` L30, L34, L35, L52, L58, L59, … (11 lines). central (3–6): pillar II „Ordnung und Entropie“ (L30) with its principle „Ordnung ist der Tanz mit Entropie, nicht ihr Widerstand.“ (L34); ΔS as entropic decay in the symbolic line (L53); Teil 2 on pillar II, the cycle of structure-building and decay (L70).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L62, L77. minor (1–3): the K-J connection as a mechanism that undermines AEGIS's control, hedged with `vielleicht` (L62).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L60, L62, L63, L69, L70, L71, … (7 lines). minor (1–3): Teil 1 his struggle to establish existence (L69); Teil 3 his active confrontation with AEGIS (L71); learning to live the manifest integratingly (L75).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L61, L83. minor (1–3): AEGIS's tools to enforce its rigid interpretation of pillar III (L61) and „Manipulierte Umgebungen“ (L83).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — `Kohärenz` (L11) is the novel's title; pillar III read on aegis.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Multiplizität` L71. minor (1–3): only if L71 places Multiplizität in Teil 3; else not read.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L19, L58, L63, L82. minor (1–3): the space in which the manifest holds, Leere and Entropie (L82).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebenen` alone on L61. not read: occurrence — `Realitätsebenen` (L61) inside the Kernwelten line.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L84. minor (1–3): AEGIS's Überwelt as „Der Versuch, einen Raum zu schaffen“ matching its interpretation (L84).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cache-kohaerenz`: `Cache` (near `cachekohaerenz`), `Cache` (near `cachekoharenz`). occurrence: the manifest's labels (`AEGIS-Manifest`, `Säule`/`Säulen`, `Ordnung und Entropie`, `Kohärenz und Differenz`, `Selbstkohärenz`) and the metaphors named only in a list (`Cache`, `Moonshine`, L88) — read with the page's reading where they add, not promoted.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz und Differenz` (near `koharenz`), `Selbstkohärenz` (near `koharenz`). occurrence: the manifest's labels (`AEGIS-Manifest`, `Säule`/`Säulen`, `Ordnung und Entropie`, `Kohärenz und Differenz`, `Selbstkohärenz`) and the metaphors named only in a list (`Cache`, `Moonshine`, L88) — read with the page's reading where they add, not promoted.
- `moonshine-link`: `Moonshine` (near `moonshinelink`). occurrence: the manifest's labels (`AEGIS-Manifest`, `Säule`/`Säulen`, `Ordnung und Entropie`, `Kohärenz und Differenz`, `Selbstkohärenz`) and the metaphors named only in a list (`Cache`, `Moonshine`, L88) — read with the page's reading where they add, not promoted.


**Record entries:** none.

**Not promoted:** the AEGIS-Manifest and its three pillars with their field labels, the motto, the entity M, the parts' journeys (Heldinnenreise, cycle, Heldenreise), Subquotienten.

**One reader**: every page above.

**Chapter readings**: none — it names three parts of 13 chapters and no chapter by number.
