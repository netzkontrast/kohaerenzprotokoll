# Brief — readings from document 250 (step 6)

1 document, one reader, one batch: `ingest-250`. Files go to `Plan/runs/ingest-250/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 250 | `strategic-narrative-implementation-for-kohaerenz-protokoll` | 2025-11-03 | „the implementation guide“ (an unsigned English report) | „a strategic guide for the creative team“ (L15) with four strategies — Kernwelt 1 as a world of coherence instead of truth, a scene of AEGIS's genesis from the Ursprungs-Ich to Component 734, three cracks foreshadowing the Bruchpunkt, and a climax in which Kael becomes The Gardener; proposals, not canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (133 lines for `strategic-narrative-implementa`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A guide of proposals: write „the implementation guide proposes / directs …“. Its genesis blueprint translates a German source it names („Einleitung: Genesis der Existenz“, L61) and quotes fragments of it in English: say they are the guide's quotations of that source. Its own name for the dismemberment is „Kohärenz Protokoll“ (L66): record the name as written, do not equate it with another page. Cut quotations before inner straight quotes and bold markers.

## Pages — document 250, `strategic-narrative-implementation-for-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L21, L25, L27, L31, L51, L53, … (22 lines). central (3–8): „pathologically committed to its own internal consistency“ (L25); a tragic antagonist rooted „in pathos, not malice“ (L51–L53); its genesis „a trauma of logic“: the Ursprungs-Ich meeting an unerkennable entity from K₀, a Resonanzkaskade, the pre-AEGIS system reading the suffering as a virus and attacking itself (L57, L64–L65); the dismemberment creating its rigid, trauma-avoidant logic (L69); AEGIS registering Kael's insight as random anomalies (L91).
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L111. minor (1–4): among the Paraiyas AEGIS's protocol must reject as noise, „Emergenz“ (L111).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L51. not read: occurrence — `Genesis` at L51 stands in a heading on AEGIS's genesis, read on aegis.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L89. minor (1–4): Crack 2, „The Juna/V Exploit“ (L89): the non-local Moonshine-Link to Juna/V giving Kael a flash of insight (L91).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L43, L45, L91, L95, L96, L104, … (13 lines). central (3–8): in the sample scene seeing a practical flaw in a celebrated building and dismissed with condescension (L45); a flash of gnosis through the Moonshine-Link (L91); Nyx triggered in Crack 3 (L95); the climax: merging with Kiko, „his most vulnerable EP“, building a dialetheic mind (L118–L119); not finding The Foundation but becoming its reflection, The Gardener (L126).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L118. minor (1–4): the climax: Kael merging with Kiko's trauma, „his most vulnerable EP“ (L118).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — the title (L11); the guide's name for the dismemberment is read on aegis and komponente-734.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L27, L87. minor (1–4): Lex representing AEGIS' worldview in miniature, his domain Kernwelt 1 (L27); in Crack 1 Lex's logic failing at a paradoxical decree (L87).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L91. minor (1–4): the non-local Moonshine-Link to Juna/V in Crack 2, AEGIS classifying the effect as system noise (L91).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L95. minor (1–4): Crack 3 triggering one of Kael's Emotional Personality parts, Nyx (L95).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitch` alone on L85. minor (1–4): the three cracks foreshadowing the Bruchpunkt, moments of „semantic sliding“, „not plot holes“ (L75, L79); Crack 1, the Gödelian Glitch (L85–L87).

- **`kern-welten`** (minor, 1–2): Kernwelt 1, Lex's domain „Co₁ - Ordnung/Logik“, designed flawlessly logical yet dangerously detached (L27).
- **`komponente-734`** (minor, 1–3): the scene blueprint „From "I" to "Component 734"“ (L59); the Ursprungs-Ich gone and Component 734 a functional unit, with a faint, persistent echo of the former self (L67).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Einleitung: Genesis der Existenz` (near `genesis`). occurrence: `Einleitung: Genesis der Existenz` is the title of the source the guide translates (L61).
- `juna`: `Juna/V` (near `juna`). `Juna/V` read on juna (J34).
- `kern-welten`: `Kernwelt 1` (near `kernwelt`), `Kernwelt 1 (KW1)` (near `kernwelt`). reading (J26): `Kernwelt 1 (KW1)`, Lex's domain „Co₁ - Ordnung/Logik“, a world flawlessly logical yet detached (L27).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title, and the guide's name for the dismemberment (L66).
- `nichts-rauschen`: `Das Rauschen` (near `nichtsrauschen`). occurrence: `Das Rauschen`, the conceptual void of the Ursprungs-Ich (L57), quoted from the source; read on aegis.
- `personas`: `Emotional Personality` (near `persona`). occurrence: `Emotional Personality` is TSDP's part, Nyx (L95), not the Personas.
- `risse`: `Gödelian Glitch` (near `glitch`). `Gödelian Glitch` read on risse.


**Record entries** (one file each):

- **`q7-what-734-names`**: Component 734, the functional unit the Ursprungs-Ich becomes after the dismemberment, with an echo of the former self classified as irrelevant latency (L67).
- **`q9-moonshine-link-boundary`**: the Moonshine-Link to Juna/V, non-local; AEGIS registers its effect only as random anomalies, system noise (L91).

**Not promoted:** the four strategies, Social Validation Protocol, Aesthetics of Logic, Mutable Variable, the Bruchpunkt, the three cracks, Paradoxon X, the six Paraiyas, The Foundation, The Gardener, the dialetheic mind, Resonanzkaskade.

**One reader**: aegis, kael, juna, lex, kiko, nyx, moonshine-link, risse, emergenz, kern-welten, komponente-734 and the records q7, q9. `genesis` and `kohaerenz` are occurrences.

**Chapter readings**: none — it names acts, not chapters.
