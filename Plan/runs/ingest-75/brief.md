# Brief — readings from document 75 (step 6)

1 document, one reader, one batch: `ingest-75`. Files go to `Plan/runs/ingest-75/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 75 | `romanstruktur-und-philosophische-einleitung` | 2025-12-18 | „the three-part analysis“ (its title: `Narrative Architektur, Psychologische Topologie und Systemische Rekursion – Eine umfassende Analyse`) | a German analytical report (2025-12-18) that retells all 39 chapters and a cyclic `Kapitel 40/0` in the present tense, in three parts — I Heroine's Journey (Kap 1–13), II Systemanalyse (14–26), III Hero's Journey (27–39) — with a table of the alters, a Fazit and eight Drive documents as sources; no canon claim; it hedges (`vermutlich`, `vielleicht`) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (326 lines for `romanstruktur-und-philosophisc`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** **An analysis that retells a plot.** It tells each chapter as if the novel existed, in the present tense, built from the concept papers it cites by number. Write „the three-part analysis tells / reads …“, never as what the novel is. Keep its hedges: where it writes `vermutlich` or `vielleicht`, say so. Its archetype frames (Heroine's Journey after Maureen Murdock, Hero's Journey) are its reading. Escaped dashes in headings (`\-----`): quote prose. This page set gets term readings only; the chapter pages are a separate batch.

## Pages — document 75, `romanstruktur-und-philosophische-einleitung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L55, L61, L69, L87, L97, … (40 lines). central (4–6): the Universal Reboot and KW1 as the domain of logic (L39); AEGIS's binary logic incompatible with trauma (L69); the Wächter as subroutines, not conscious beings (L150); Kap 31, AEGIS offers paradise instead of force (L246); Kap 38, a paraconsistent AEGIS (L274 heading and line); Kap 40/0, the Trennungsprotokoll activated as physical necessity, not malice (L296).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L49, L73, L119, L230, L280, L298. minor (1–2): Tabelle 1 maps the alters of Part I — roles, dominant worlds, development (L119–L130).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L49, L75, L126, L150. minor (1): KW3, the domain of Cerberus (L49); the Cerberus aspects grow less aggressive when their protective function is acknowledged (L75).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L264. not read unless L264 says what emerges: ask `--find`; else occurrence.
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L17, L142, L144, L160, L162, L164, … (8 lines). minor (1–2): Kap 14, the disorder recognised as entropy (L144); Kap 17, entropy as a weapon (L164).
- **`genesis`** (minor, 1–4): the census's surfaces — `Genesis` L81, L242, L290. minor (1): `Text: Genesis (Reprise & Neuinterpretation)` (L290) — Kap 40/0 returns to the ground of origin (L294).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L47. minor (1): the concept of the Guardians introduced in Kap 2 (L47).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L59, L61, L63, L87, L127, L182, … (9 lines). minor (2–3): external reference and emotional anchor, connection to the „Externen Ebene“ beyond the simulation (L61); attachment trauma (L63); Kap 31, AEGIS's paradise with Kael united with Juna (L246).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L35, L39, L41, L43, L47, L49, … (67 lines). central (4–6): wakes in KW1 after the Universal Reboot (L39); accepts he is not one but many (L73); mediator among his parts (L99); Teil II as analyst of his own reality (L140); returns transformed, part of the structure (L272); Kap 40/0, opens his eyes in KW1 not knowing who he is (L306).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L93, L130. minor (1): KW4, the domain of `Kairos/Sophia` (L93); Selene in KW4 (Kairos) (L130).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kern-Welt` L39, L49, L53, L93, L123; `Kernwelten` L150, L234, L280. central (2–3): KW1 the Konstrukt-Stadt (L39), KW3 Cerberus (L49), KW2 an archipel in a fog of forgetting (L53–L55), KW4 Kairos/Sophia (L93); Kael leaves the Kernwelten for the Überwelt in Kap 28 (L234).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L55, L73, L128. minor (1): `Kiko/Lia`, exiles, children (L128).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: title (L11) — occurrence (J9).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L39, L117. minor (1–2): KW1, the Konstrukt-Stadt (L39); seen in Kap 13 as a construct (L117).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L49, L67, L69, L99, L105, L111, … (10 lines). central (2–3): activated to regain control, fails at emotion in Kap 5 (L67–L69); integrated as a tool in Kap 11 (L125).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L55, L128. minor (1): L128 as above.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L39, L53, L150. minor (1): KW1/LogOS (L53); LogOS, Mnemosyne, Cerberus as Wächter of the Kernwelten, subroutines (L150).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L53, L67, L127, L150. minor (1): L150 as above; Rhys in KW2 (Mnemosyne) (L127).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L87, L129. minor (1): „vermutlich Moros“ as the exile carrying the original trauma (L87); bearer of the core wound (L129).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L33, L107. minor (1–2): Part I's central conflict, Fragmentierung vs. Funktionale Multiplizität (L33); Kap 12, the sacred marriage (L107–L109).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L73, L97, L99, L105, L126, L230. minor (1): Kael must convince Nyx that safety comes through trust (L99); from attacker to defender (L126).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L222. minor (1): Part III's dominant domain, the system core & the Potentialmeer (L222).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L73, L111, L127, L230. minor (1): bridge to the emotions, keeps contact with Juna (L127).
- **`risse`** (minor, 1–4): the census's surfaces — `Glitches` L17, L43; `Risse` L43, L53, L117, L162. minor (1–2): Kael perceives visual „Glitches“, organic chaotic forms over the sterile geometry (L43); Kap 23, the glitch becomes the most powerful tool (L198).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L91, L130. minor (1): emerges as the leading force of integration in Kap 12 (L130).
- **`sophia`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Sophia` alone on L93. minor (1): KW4 as `Kairos/Sophia` (L93).
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Trennungsprotokoll` L242, L284, L296. minor (1–2): Kap 40/0 headed „Der Ouroboros und das Trennungsprotokoll“ (L284); activated as physical necessity when complexity crosses a threshold (L296).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L15, L85, L123. minor (1): the Kern-Trauma-Erinnerung as the heart of the TSDP dramaturgy (L85).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L136, L140, L144, L234. central (2–3): Part II's dominant domain, the Überwelt (AEGIS) & Meta-Ebene (L136); Kael analyses data streams in the Überwelt (L144); Kap 28, the administrative heart of AEGIS, pure data architecture (L234).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `Anomalie` (near `mustererkennunganomaliedetektion`). occurrence (J69).
- `isabelle`: `Isabell` (near `isabelle`). reading (1) on `isabelle`: `Isabell` among the aggressive protectors (L97) — the spelling is the document's.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence (J9).
- `mnemosyne-server-architektur`: `Architekt` (near `mnemosyneserverarchitektur`). occurrence (J69): `Architekt` is not the Mnemosyne server.
- `ouroboros-struktur`: `Ouroboros` (near `ouroborosstruktur`). reading (1): Kap 40/0, `Der Ouroboros und das Trennungsprotokoll` (L284), epilogue and prologue at once (L288), Kael waking again in KW1 (L306).
- `sophia`: `Kairos/Sophia` (near `sophia`). reading, above.


**Record entries** (one file each, page = the record's file stem):

- **`q5-guardians-and-kern-welten`**: KW1 LogOS, KW3 Cerberus, KW2 Mnemosyne, KW4 Kairos/Sophia (L39–L53, L93, L150).
- **`q6-nexus-ueberraum-ueberwelt`**: the Überwelt as AEGIS's administrative heart above the Kernwelten (L136, L234).
- **`c13-externe-ebene-beyond-the-simulation`**: Juna's connection to the „Externen Ebene“, a reality beyond the AEGIS simulation (L61); Kap 20, „vielleicht die Existenz der externen Ebene“ as an unprovable truth (L182).
- **`c12-genesis-beats`**: Kap 40/0 — the Trennungsprotokoll as physical necessity at a complexity threshold, the cycle restarting (L296, L306).

One reader writes everything.
