# Brief — readings from document 324 (step 6)

1 document, one reader, one batch: `ingest-325`. Files go to `Plan/runs/ingest-325/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 324 | `genesis-aegis-und-logische-grenzen` | 2025-04-29 | „the Genesis prose draft with logical limits“ (an unsigned German prose draft with 64 web references) | a creation scene in a preface and three parts of 13 scenes, beats labelled `Ich-Perspektive`, `AEGIS-Perspektive` or `Ich/Kael-Perspektive`, AEGIS's beats as English system-log capitals with German commentary and pacing notes: from the noise before being and the first self, through AEGIS's birth and Direktive 0, the assignment of Komponente 734, the Überwelt and the simulation that fails on paradox, to the destruction of the component and Kael named from the fragments; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (194 lines for `genesis-aegis-und-logische-gre`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A prose draft in two voices: write „the Genesis prose draft narrates … in Szene N …“; the English capitals are in-fiction AEGIS logs and the German commentary is the draft's own voice — say which you quote. The pacing notes are production notes. Cut quotations before glued digits (`Direktive 0`, `Beat 3.5`, scene numbers) and bracketed tags.

## Pages — document 324, `genesis-aegis-und-logische-grenzen`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L57, L59, L61, L65, L67, L69, … (40 lines). central (3–6): „keine Geburt, sondern eine logische Konsequenz aus dem Scheitern“ (L67); its directive in capitals, maximise coherence and reject the non-system (L67), Direktive 0 „seine größte Stärke und seine fatale Schwäche“ (L69); stripping subjective metadata (L69); excluding the self-referential problem to keep its consistency (L123); anomaly X-1 unsimulable and incompatible with its core logic (L153); the targeted elimination (L163).
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L51, L67. minor (1–3): the cluster forming in Scene 3, „Dies ist Emergenz in Aktion“ (L51).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L15, L21, L31, L33, L57, L67. minor (1–3): the state before the world as „Ein Zustand maximaler Entropie“ (L15), „eine entropische Flut“ (L17); the first self as minimal coherence against entropy (L31).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L11. minor (1–3): only if L11, the title, names Genesis as this scene's subject; else an occurrence.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L77, L81, L115, L141, L157, L159, … (14 lines). central (3–6): the echo as „der Teil von Kael“ (L77); the first cut as the beginning of traumatic fragmentation (L169); „Kael ist dieses Mosaik.“ and a new identity born from the debris (L185); a testimony to the irreducibility of consciousness (L187).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — `Kohärenz` L17, L29, L31, L51, L65, L173. minor (1–3): the first self as „Eine minimale Kohärenz, die sich gegen die Entropie stemmt.“ (L31); the elimination to preserve global coherence (L163) only if it adds.
- **`komponente-734`** (central, 3–12 quotations): the census's surfaces — `Komponente 734` L71, L75, L79, L81, L105, L109, … (13 lines). central (3–6): the nameless self becoming a numbered component with a defined function (L73); the echo classified as harmless, „ein kritischer Fehler“ enabling the later catastrophe (L79); the signature `VS-734-ALPHA`; the component's destruction after the anomaly (L163, L169).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L15, L23, L29, L63. minor (1–3): the noise before the world, not silence, „ein Chaos, das tobte“ (L15); its other names (L19); the clusters dissolving in it as harbinger of AEGIS's genesis (L57).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L107, L109, L111, L113, L121, L145, … (8 lines). minor (1–3): AEGIS describing the Überwelt not as a passive analysis tool but as active (L107); „Eine Architektur des Denkens, sichtbar gemacht.“ (L111); the simulation failing on a limit of computability (L121).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `Anomalie` (near `mustererkennunganomaliedetektion`). occurrence: the draft's perspective labels and inflected names (`Nichts Rauschens`, `Rauschen`, `AEGIS-Perspektive`, `Ich/Kael-Perspektive`), `Anomalie` (anomaly X-1, not a metric), `SIMULATION PROTOCOL OMEGA-12` (a log line), `Echo` (the component's echo, read on komponente-734 and kael) — read with the page's reading where they add, not promoted.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: the draft's perspective labels and inflected names (`Nichts Rauschens`, `Rauschen`, `AEGIS-Perspektive`, `Ich/Kael-Perspektive`), `Anomalie` (anomaly X-1, not a metric), `SIMULATION PROTOCOL OMEGA-12` (a log line), `Echo` (the component's echo, read on komponente-734 and kael) — read with the page's reading where they add, not promoted.


**Record entries** (one file each):

- **`c16-kael-origin`**: the first self of the noise integrated into AEGIS as Komponente 734, its echo „der Teil von Kael“, destroyed by AEGIS, and Kael named as the mosaic of the debris (L73, L77, L169, L185) — say which recorded position it sits nearest, deciding nothing.
- **`q7-what-734-names`**: `Komponente 734` as the numbered component the nameless self becomes inside AEGIS (L73), with the signature `VS-734-ALPHA`.

**Not promoted:** the beats and their perspective labels, Direktive 0, the PRECURSOR FRAGMENTS, NULL-STATE, anomaly X-1, the diagnostic table, the scar, and the borrowed concepts (autopoiesis, structural coupling, complex adaptive system, paraconsistent logic, Gödel).

**One reader**: every page above and the two record entries.

**Chapter readings**: none — the document's parts and scenes are its own, not the novel's chapters.
