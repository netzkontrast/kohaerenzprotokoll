# Brief — readings from document 397 (step 6)

1 document, one reader, one batch: `ingest-398`. Files go to `Plan/runs/ingest-398/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 397 | `kohaerenz-protokoll-master-outline` | 2026-02-25 | „the Master-Outline“ (an unsigned German „Master-Outline: Das Kohärenz Protokoll (3-Phasen-Modell)“) | an outline of the novel in three parts — Kapitel 1–13, 14–26, 27–39 — and an epilogue, each with genre focus, theme, content points and annotations (Pacing, Kohärenz-Check, Limit-Integration); a plan, no claim of standing beyond it |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (91 lines for `kohaerenz-protokoll-master-out`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan: write „the Master-Outline plans …“ or „in the Master-Outline's Part II …“; its content points say what is to happen, its annotations how to write it — neither is the novel as written. It names chapter ranges only, so no chapter page gets a reading. Quote the German as written; cut before straight and nested quotes and bold markers. No gendered pronoun for Kael or Juna — use the names (quotations stay verbatim). The document names a real mathematician at L27 and borrows concepts named after real people: never write those names.

## Pages — document 397, `kohaerenz-protokoll-master-outline`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L31, L57, L73, L75, L86. minor (1–3): Part I: time dilations and gravity anomalies that are algorithmic error corrections of AEGIS (L31); Part II: the noise the trauma AEGIS tries to order (L57); Part III: „AEGIS verliert die Kontrolle.“ (L73), healing is not winning AEGIS, the order (L75); the epilogue a final system report of AEGIS (L86).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L57, L74, L75. minor (1–3): the noise as „absolute Entropie“ (L57); the external level ruled by „dieselbe Entropie“ (L74); the noise as „die Entropie/das Trauma“ (L75).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L48, L62. minor (1–3): Part II's encounter with the Guardians (L48), LogOS and Mnemosyne as two of them (L52, L53); the annotation: the Guardians act as „Dozenten des Grauens“ (L62).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L26. minor (1–3): Part I's anomaly: „Juna erscheint als flüchtiges Echo, das die Logik der Stadt bricht“ (L26).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L25, L27, L36, L47, L52, L53, … (10 lines). central (3–6): Part I: Kael wakes in the Konstrukt-Stadt (L25) and meets „unentscheidbare Zonen“ (L27); Part II: Kael leaves the city simulation for the Überwelt (L47), LogOS and Mnemosyne explain the axioms and confront Kael with being a fractured information fragment (L52, L53), the noise grows louder the nearer Kael comes to the truth (L57), the insight about borders as Kael's survival strategy (L63); Part III: Kael „erwacht“ briefly on the external level (L74) and recognises that healing means accepting the noise as part of coherence, not winning AEGIS (L75).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. minor (1–3): healing as accepting the noise „als Teil der Kohärenz“ (L75); the epilogue's redefinition: coherence now defined as Mosaik-Herz (L86). L11 (the title) is an occurrence.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L25, L73. minor (1–3): Kael wakes in the Konstrukt-Stadt and feels the cold of the architecture (L25); the undecidable zones as city districts that repeat or end in paradoxes (L27); the borders between Konstrukt-Stadt, Überwelt and external level begin to flicker (L73).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L52. minor (1–3): „LogOS (Grenze der Logik)“: explains that the system rests on axioms that can never be complete; Part I's horror was only the „Leck“ in the logic (L52).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L53. minor (1–3): „Mnemosyne (Grenze der Identität)“: confronts Kael with a document on identity; Kael is no individual but a fractured information fragment (L53).
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L65, L86. minor (1–3): Part III's title „Die Fusion – Das Mosaik-Herz“ (L65); in the epilogue coherence is defined as „Mosaik-Herz“ — „stabil durch akzeptiertes Chaos“ (L86).
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L47. minor (1–3): „Aufstieg in den Nexus“ as Part II's first content point (L47).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts-Rauschen` L37, L57. minor (1–3): Part I: a quiet, disturbing background noise in the empty zones of the city (L37); Part II: the noise is „absolute Entropie“, the trauma AEGIS tries to order, louder the nearer the truth (L57); Part III: to be accepted as part of coherence (L75).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L39, L47, L73. minor (1–3): Part II's title „Die Überwelt – Die Anatomie des Rauschens“ (L39); the Überwelt as „eine abstraktere Ebene der Datenverarbeitung“ (L47); its border flickering in Part III (L73).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `Die Anomalie` (near `mustererkennunganomaliedetektion`). see the pages above: `Die Anomalie` is Part I's label for Juna (read on juna), not the metrics page; `Kohärenz Protokoll` (L76) the title inside the mirror effect, `Kohärenz-Check` an annotation label and `Zielkohärenz` the epilogue's report line — occurrences; `TSDP-Aspekt` read on tsdp (below).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Zielkohärenz` (near `koharenz`), `Kohärenz-Check` (near `koharenz`). see the pages above: `Die Anomalie` is Part I's label for Juna (read on juna), not the metrics page; `Kohärenz Protokoll` (L76) the title inside the mirror effect, `Kohärenz-Check` an annotation label and `Zielkohärenz` the epilogue's report line — occurrences; `TSDP-Aspekt` read on tsdp (below).
- `tsdp`: `TSDP-Aspekt` (near `tsdp`). see the pages above: `Die Anomalie` is Part I's label for Juna (read on juna), not the metrics page; `Kohärenz Protokoll` (L76) the title inside the mirror effect, `Kohärenz-Check` an annotation label and `Zielkohärenz` the epilogue's report line — occurrences; `TSDP-Aspekt` read on tsdp (below).


**Pages beyond the draft:**
- **`externe-ebene`** (central, 3–4): the „externen Ebene“ as the real world of the reader (L73); Kael's brief visit, where the same entropy and incompleteness rule (L74); the annotation: the visit is to be „geglitcht“ so subtly that the reader doubts whether the own world is not also a level of the Konstrukt (L81).
- **`tsdp`** (minor, 1): Mnemosyne's insight that Kael is a fractured information fragment, labelled „TSDP-Aspekt“ (L53).

**Record entries** (one file, as earlier entries on C13, e.g. `ls Plan/runs/ingest-*/readings/c13-*`):
- **`c13-externe-ebene-beyond-the-simulation`**: the Master-Outline plans the external level as the real world of the reader, which Kael visits briefly in Part III (L73, L74), and wants the visit glitched so that the reader doubts the own world (L81) — recorded, not applied and not decided.

**Not promoted:** Master-Outline, Der Erwachen-Zyklus, unentscheidbare Zonen, Der Spiegel-Effekt, Zeitdilatationen, Pacing, Limit-Integration, Annotationen, Genre-Fokus, Inhaltliche Schwerpunkte, Dozenten des Grauens, Architectural Storytelling, Unvollständigkeit, Statusbericht PMAS, Zielkohärenz.

**One reader**: kael, juna, aegis, guardians, konstrukt-stadt, ueberwelt, nexus, logos, mnemosyne, nichts-rauschen, entropie, mosaik-herz, kohaerenz, externe-ebene, tsdp, and the C13 entry.

**Chapter readings:** none — the document names three chapter ranges (L17, L39, L65) and no chapter.
