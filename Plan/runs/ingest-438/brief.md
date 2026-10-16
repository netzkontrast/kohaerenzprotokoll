# Brief — readings from document 437 (step 6)

1 document, one reader, one batch: `ingest-438`. Files go to `Plan/runs/ingest-438/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 437 | `narrative-techniken-fuer-kohaerenz-protokoll` | 2025-04-27 | „the craft report“ (an unsigned German report of narrative techniques for writing the chapters) | reports borrowed craft frameworks and applies them in proposals to Kael, AEGIS, Juna, the Kernwelten, the Guardians and the K-J connection, beside a chapter blueprint it refers to and does not contain; a resource (L17), no claim of canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (633 lines for `narrative-techniken-fuer-kohae`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Craft advice: write „the craft report proposes …“ — its „sollte“ and „könnte“ are advice for the prose, not facts of the novel; what it says the blueprint holds („Blaupause“, L45, L69, L369) is its report of another text. It names no chapter, only the three parts (L406–L408). The world codes are named after mathematicians: never expand them. Quote the German as written; cut before straight and single quotes, bold and italics markers and glued footnote digits. No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations stay verbatim). Never write a real person's name.

## Pages — document 437, `narrative-techniken-fuer-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L29, L41, L45, L46, L47, L51, … (49 lines). minor (1–4): AEGIS's perspective in the blueprint's log format: an analytic, cool voice (L45); the „AEGIS-System“ with a functional, sterile aesthetic of data streams and surveillance (L64); AEGIS's instability as emergent, unpredictable behaviour (L338); AEGIS as logic, analysis and reductionism (L369).
- **`cache-kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Cache Kohärenz` L44, L71, L75, L79, L85, L159, … (13 lines). minor (1–4): the point of view makes „Cache Kohärenz“ experienceable; cache incoherence as inconsistent data across storage locations (L44).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L189. not read: an occurrence — named in the document's general sense.
- **`emergenz`** (central, 3–12 quotations): the census's surfaces — `Emergenz` L210, L216, L221, L222, L223, L225, … (11 lines). minor (1–4): AEGIS's instability as „emergentes, unvorhersehbares Verhalten“ (L338).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L144, L177, L373, L377, L384, L386, … (8 lines). minor (1–4): „Kernwelt-Guardians: Archetypische Verkörperungen von Weltprinzipien“ (L373); each Guardian — `Architekt`, `Netzweber`, `Chaos-Regulator`, `Möglichkeits-Weber` — must embody its world's core principle (L381).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L99, L103, L105, L146, L363, L365, … (9 lines). minor (1–4): the connection between Kael and Juna should manifest subtly (L99); shared experience: a feeling or image that may reflect Juna's state (L363).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L29, L41, L43, L44, L45, L46, … (102 lines). central (4–8): the choice of point of view for Kael makes the cache incoherence experienceable (L44); „Innerer Raum Kaels“ as the most direct mirror of Kael's psychic state (L65); the integration journey toward 'ICH'/Kael-M (L206 — cut before the single quotes); mapping Kael's parts (L298); Part 1 Kael's inner journey, Part 3 an active, more integrated Kael (L406, L408).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelt` L59, L61, L62, L63, L67, L95, … (21 lines); `Kernwelten` L59, L67, L239, L253, L337, L407, … (7 lines). central (4–8): three worlds by code with their principle and how to describe them — order/logic with sterile symmetry (L61), chaos/instability with glitches (L62), potential/liveliness with fluid landscapes (L63) — never expand the codes; each world's principle embodied by its Guardian (L381).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — named in the document's general sense.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L45, L64, L249, L338, L339. minor (1–4): „Instabilität („Risse“)“ — AEGIS's instability not only as technical malfunction but as emergent behaviour or inner conflict (L338 — cut before the nested quote).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenzprotokolle` (near `koharenz`), `Cache-Kohärenz-Metapher` (near `koharenz`). an occurrence: named in the document's general sense.
- `mnemosyne-server-architektur`: `Architekt` (near `mnemosyneserverarchitektur`). an occurrence: named in the document's general sense.
- `moonshine-link`: `Moonshine` (near `moonshinelink`). a reading, on moonshine-link below.
- `personas`: `Depersonalisation` (near `persona`). an occurrence: named in the document's general sense.


**Pages beyond the draft:**
- **`moonshine-link`** (minor, 1–3): „Moonshine/K-J Verbindung (Subtile intuitive Verbindungen)“ (L99); section 3.3 „Die K-J Verbindung (Moonshine)“ (L345); the K-J connection as narrative counterpoint to AEGIS's logic and Kael's fragmentation (L369).

**Record entries:** none.

**Not promoted:** M, Kael-M, Kael-Juna-Einheit, Innerer Raum Kaels, the world codes, the Guardians' names, Log-Format, Sprachwechsel, Blaupause, Kael's parts, and the borrowed craft concepts.

**One reader**: every page above.

**Chapter readings**: none — the document names no chapter, only the three parts.
