# Brief — readings from document 226 (step 6)

1 document, one reader, one batch: `ingest-226`. Files go to `Plan/runs/ingest-226/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 226 | `kohaerenz-protokoll-detaillierter-plot-blueprint` | 2026-02-25 | „the master blueprint“ (an unsigned German plot plan) | a short German plan of the book in three parts — Kap 1–13, 14–26, 27–39 — each with a concept, an arc, the research documents it integrates and a pacing note, ending in three answers on Kael, AEGIS and Juna; it calls itself „Master-Blueprint“: a plan, not canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (83 lines for `kohaerenz-protokoll-detaillier`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan: write „the master blueprint plans …“ and name the part (I, II, III) a line belongs to. The titles of the documents it integrates are references, not readings — never quote a title as if it said something. Its three closing answers give three accounts of AEGIS; record each as written. **Privacy:** Part III reads Kael's waking in the Externe Ebene as a character's revelation — write it as the plan's account of Kael, a character; never connect it to any real person, never quote „die Stimme des Autors“ (L76) or the title of the Köln date document, and never speculate about anyone outside the fiction. `--find` drops digits (`Sektor 04`, `2. Hauptsatz`) — quote around them.

## Pages — document 226, `kohaerenz-protokoll-detaillierter-plot-blueprint`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L29, L55, L67, L71, L72, L74, … (7 lines). minor (1–3): AEGIS's algorithms felt as „Messer im Bewusstsein“ in the prologue (L29); AEGIS filtering out Entropie, the trauma, to prevent system death, as LogOS explains (L55); AEGIS initiating the „Purge“ in Part III (L67); in the Externe Ebene Kael recognising AEGIS as a projection of his attempt to suppress his symptoms by pure self-control (L71); the closing answer: „Die internalisierte Scham und das Kontrollbedürfnis“ (L81).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L42. not read: named only in the list of the four Guardians (L42); read on guardians.
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L16, L51, L55, L72. minor (1–3): LogOS's dialogue on the second law: AEGIS must filter Entropie, „das Trauma“, out; Kael: without Entropie no growth (L55); Mnemosyne distorting Kael's memory of Juna by „subjektive Entropie“ (L51); the carnival's chaos mirroring the Entropie in his head (L72).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L17. minor (1–3): Kael breaking through the rendering limits and waking in the „Externen Ebene (Köln, Februar 2026)“, recognising an asymmetric relationship with Juna in reality (L67); the Externe Ebene grounded by a real setting, the carnival (L72); Part III's theme (L17) — quote around the digits.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L25. occurrence: `Genesis` stands in the integrated document's title „Einleitung: Genesis der Existenz“ (L25, L29).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L38, L42, L46. minor (1–3): Part II as the confrontation with the Guardians (L38); Kael meeting the Guardians „LogOS, Mnemosyne, Cerberus, Kairos/Sophia“ in the Nexus (L42); each Guardian staged with its specific „Blinden Fleck“ (L46).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L25, L42, L50, L51, L67, L71, … (9 lines). central (3–5): Juna as a fleeting anomaly Kael cannot grasp in Part I (L25); not a malfunction but „ein Echo einer realen Person“ (L42); LogOS failing at the paraconsistent logic of her existence (L50); in Part III Juna as Kael's partner caught in a carer's role (L71) — the plan's account of characters; the closing answer: „Die Brücke zur Realität“ (L82).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L25, L31, L32, L42, L51, L55, … (14 lines). central (3–5): Kael waking after the „Universal Reboot“ and experiencing the Konstrukt-Stadt as a cold, logic-based prison (L25); Gödelian dead ends (L32); leaving the simulation for the Nexus (L42); fighting the dissolution of his self (L56); waking in the Externe Ebene (L67), seeing himself as a patient with KPTBS, DIS and ADHS — the plan's account of the character (L71); accepting the Mosaik-Herz (L74); the closing answer: „Die Sonde des Lesers“ (L80).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L42, L57. minor (1–3): Kairos discussing the „Orientierungswissenschaft“, making clear that the construct is a philosophical experiment of the „Beobachters“ (L57); „Kairos/Sophia“ among the Guardians (L42).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (L11).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L25, L30. minor (1–3): Kael experiencing the Konstrukt-Stadt as a cold, logic-based prison (L25); the city introduced as an antagonist of its own through ozone sounds and cold geometry (L30).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L42, L50, L55. minor (1–3): LogOS failing at the paraconsistent logic of Juna's existence (L50); LogOS's dialogue on the second law of thermodynamics, AEGIS filtering Entropie (L55).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L42, L51, L56. minor (1–3): Mnemosyne distorting Kael's memory of Juna through „subjektive Entropie“ (L51); showing Kael that his identity is only a relational structure that can be recalibrated (L56).
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L74. minor (1–3): Kael accepting the „Mosaik-Herz“ in the final system report, choosing against AEGIS's sterile order (L74).
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L42. minor (1–3): Kael leaving the simulation level and entering the Nexus, where he meets the Guardians (L42).
- **`partnerin`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Partnerin` alone on L71. occurrence: `Partnerin` is a common noun for Juna (L71), not the term of the page's document.
- **`sektor-04`** (minor, 1–4): the census's surfaces — `Sektor 04` L31. minor (1–3): „In Sektor 04 erlebt Kael „kausale Horizonte““: regions of the city that seem to exist but can never be reached (L31) — quote around the digits.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L42. not read: named only as „Kairos/Sophia“ in the Guardian list (L42); read on guardians.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L38. minor (1–3): Part II's concept: „Die Überwelt und die Konfrontation mit den Guardians.“ (L38).

- **`nichts-rauschen`** (minor, 1–2): Juna as the bridge to reality, the only connection strong enough to survive „das Rauschen des Nichts“ (L82); the Nichts (Śūnyatā) not an abyss but the space where integration takes place (L73).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` is a Guardian of Part II (L46), read on guardians, not the Integrity Guardian.
- `did`: `Identität` (near `diddissoziativeidentitatsstruktur`), `Identität` (near `dissoziativeidentitatsstruktur`). occurrence: `Identität` stands in an integrated document's title „Identität: Grenzen und Wandel“ (L56) and Part II's theme (L16).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title `Kohärenz Protokoll` (L11) and the „Roman-Dokument“ it names (L74).
- `nichts-rauschen`: `Nichts` (near `nichtsrauschen`). a reading: Juna as the only connection strong enough to survive „das Rauschen des Nichts“ (L82); the Nichts (Śūnyatā) as the space of integration (L73) — minor, read on nichts-rauschen.
- `tsdp`: `TSDP-Systemik` (near `tsdp`). occurrence: `TSDP-Systemik` is Part II's theme label (L16).


**Record entries** (one file each):

- **`c13-externe-ebene-beyond-the-simulation`**: Kael breaking through the rendering limits and waking in the Externe Ebene, Köln, Februar 2026 (L67); the carnival as its real setting (L72).
- **`c4-guardians-and-aegis`**: each Guardian staged with its specific „Blinden Fleck“ (L46); LogOS failing at Juna's paraconsistent logic (L50).
- **`q5-guardians-and-kern-welten`**: four Guardians named, „Kairos/Sophia“ as one (L42); no world pairing given.
- **`q6-nexus-ueberraum-ueberwelt`**: Part II's concept the Überwelt (L38); Kael leaving the simulation for the Nexus (L42).

**Not promoted:** Universal Reboot, Purge, kausale Horizonte, Gödelsche Sackgassen, Architectural Storytelling, Meta-Twist, Beobachter-Instanz, the integrated documents' titles.

**One reader**: kael, juna, aegis, entropie, externe-ebene, guardians, kairos, konstrukt-stadt, logos, mnemosyne, mosaik-herz, nexus, sektor-04, ueberwelt, nichts-rauschen and the records c13, c4, q5, q6.

**Chapter readings**: Kap 1–39 by the three parts (L15–L17), by the session (`Plan/runs/ingest-226-kap/`).
