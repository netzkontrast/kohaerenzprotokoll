# Brief — readings from document 439 (step 6)

1 document, one reader, one batch: `ingest-440`. Files go to `Plan/runs/ingest-440/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 439 | `kohaerenz-protokoll-analyse-und-loglines` | 2025-04-28 | „the logline analysis“ (an unsigned German „Analyse und Loglines“) | a critique of the concept (AEGIS, the Juna-Verbindung, Paradoxon X, the Kernwelten, the Guardians, cache coherence), a pacing strategy for three parts and 39 proposed chapter loglines; calls its loglines „das Kern-Deliverable“ (L208), no claim of canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (315 lines for `kohaerenz-protokoll-analyse-un`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Analysis and proposals: write „the logline analysis proposes …“ or „the logline analysis's Kap 16 logline …“; its critique („Potenzielle Schwachstelle“) is advice, and its loglines are proposals, often hedged („vielleicht“, question marks). Its single-letter tags (S, P, V, G, I, M) are its shorthand. The numbered lists restart at 1 in each part: the chapter number is the bold „Kapitel N“ label (Kap 1–13 L216–L228, Kap 14–26 L236–L248, Kap 27–39 L256–L268). Quote the German as written; cut before straight quotes, bold and italics markers and glued footnote digits. No gendered pronoun for Kael, Juna or AEGIS — use the names (quotations stay verbatim). Never write a real person's name nor a law or theory named after one (L26, L28), nor quote a span containing one.

## Pages — document 439, `kohaerenz-protokoll-analyse-und-loglines`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L21, L25, L26, L27, L28, L29, … (60 lines). central (4–8): AEGIS as an autopoietic system existing by negating a chaotic Potentialmeer, striving for coherence through control (L25); the Juna-Verbindung as an existential threat to it, causing instability („Risse“) (L27 — cut before the quote); AEGIS perhaps lacks the variety to manage Kael's psyche, a possible source of Paradoxon X (L28 — describe the named law); Kap 1: a controlling power (AEGIS) (L216); late loglines: AEGIS prepares a drastic, system-wide measure (L247).
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L76, L140, L143. minor (1–4): „Kael (I) & „Cache Kohärenz“ (IFS Analogie)“ (L76 — quote around the nested quote).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L80, L140, L142, L143, L145, L283. minor (1–4): Kael fragmented into Personas/parts „analog zu DID/IFS“ (L80).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L122. not read: an occurrence — „Kontrolle/Emergenz“ in the list of themes (L122).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L38, L83, L201, L220, L226, L238. minor (1–4): one of the „Vier zentrale Welten“ mirroring Kael's inner states (L38); the loglines set there (L220, L226, L238) — one or two of them.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L38, L40, L110, L133, L161, L212, … (9 lines). minor (1–4): Guardians (G) watch over the worlds (L38); they risk seeming like level bosses (L40); section „Guardians (G)“ (L110); Kap 16: the Juna-Verbindung manifests through a Guardian (L238).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L26, L27, L28, L44, L50, L58, … (30 lines). minor (1–4): the Juna-Verbindung (V) as external, non-logical, essential for Kael's integration (L48); Kap 16: the connection manifests through a Guardian in the Grenzfeste (L238); Kap 22: through it Kael reaches a deeper level of the self (L244); Kap 31: the connection at its maximum strength (L260).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L28, L29, L38, L39, L40, L48, … (81 lines). central (4–8): Kael as protagonist fragmented into Personas/parts distributed over the Kernwelten, analogous to DID/IFS (L80); Kap 1: Kael wakes without memory in the Konstrukt-Stadt (L216); Kap 6: Kael finds traces of „M“, the original entity, and senses the fragmentation was induced (L221 — cut before the quote); Kap 20: other entities, perhaps fragments of other 'M's, trapped in the system (L242); Kap 39: Kael integrated but perhaps marked, the future ambivalent (L268).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L34, L60, L80, L83, L114, L124, … (16 lines); `Kernwelt` L34, L60, L80, L83, L114, L124, … (19 lines). minor (1–4): „Kernwelten Funktionalität“ (L34): four central worlds plus an abstract Überwelt mirroring and activating Kael's inner states (L38); they need clear rules for movement and influence (L39).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence — the novel's title (L11).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L38, L83, L201, L216, L218, L222, … (9 lines). minor (1–4): one of the „Vier zentrale Welten“ mirroring Kael's inner states (L38); the loglines set there (L216, L218, L222, L226, L236, L239) — one or two of them.
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L38, L83, L201, L225, L240. minor (1–4): one of the „Vier zentrale Welten“ mirroring Kael's inner states (L38); the loglines set there (L225, L240) — one or two of them.
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L48. minor (1–4): the Juna-Verbindung operates beyond AEGIS's understanding, the „Moonshine-Link“ — cut before the straight quote (L48); its non-local nature explains its pervasive influence (L49).
- **`personas`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Personas` alone on L80. minor (1–4): Kael fragmented „in Personas/Anteile über Kernwelten verteilt“ (L80).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L25, L26. minor (1–4): AEGIS exists by negating „eines chaotischen Potentialmeers“ (L25), perceived as chaotic (L26).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L38, L83, L144, L201, L217, L223, … (7 lines). minor (1–4): one of the „Vier zentrale Welten“ mirroring Kael's inner states (L38); the loglines set there (L217, L223, L237) — one or two of them.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L27, L28, L59, L256. minor (1–4): the Juna-Verbindung causes instability, the Risse (L27); the system's instabilities as a direct consequence of AEGIS's variety deficit (L28); Paradoxon X's manifestation must be concrete — system failures, the Risse (L59) — cut before each straight quote.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L38, L256, L257. minor (1–4): „plus eine abstrakte Überwelt“ beside the four worlds (L38); the late loglines set in it (L256, L257).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). an occurrence: `Guardian` names the worlds' Guardians.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenzprüfung` (near `koharenz`). occurrences: the title and `Kohärenzprüfung`, the document's self-check.


**Record entries:** none.

**Chapter readings** (batch `ingest-440-kap`, one file per chapter, `Plan/runs/ingest-440-kap/readings/kap-NN--kohaerenz-protokoll-analyse-und-loglines.md`, Kap 1 to Kap 39, formatted as the files in `Plan/runs/ingest-422-kap/readings/`): each chapter's proposed logline — Kap 1–13 L216–L228, Kap 14–26 L236–L248, Kap 27–39 L256–L268, the chapter number from the bold label — one bullet with one or two quotations from its own line. A proposal, not the chapter.

**Not promoted:** Juna-Verbindung (V), Paradoxon X, the single-letter tags, Kernwelten Funktionalität, Kohärenzprüfung, the three part names, the loglines' event labels, and the borrowed concepts.

**One reader**: every page above and the 39 chapter readings.
