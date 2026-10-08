# Brief — readings from document 193 (step 6)

1 document, one reader, one batch: `ingest-193`. Files go to `Plan/runs/ingest-193/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 193 | `plot-entwicklung-fuer-kohaerenz-protokoll` | 2025-04-23 | „the plot blueprint“ (titled `Plot-Entwicklung für „Kohärenz Protokoll“`) | a German plot blueprint in nine sections: a modified three-act structure with Kael's journey through the four Kernwelten (Konstrukt-Stadt, Resonanz-Nebel, Schattenlabyrinth, Möglichkeitsstrom) as the middle act, AEGIS and four Guardians, the Kael-Juna-Verbindung rooted in the Kohärenz-Insel, three alternative endings with transcendence recommended, and the Monstergruppe as an unnamed metaphor; it addresses the author and calls itself „eine detaillierte und fundierte Grundlage“ (L247) — recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (248 lines for `plot-entwicklung-fuer-kohaeren`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A blueprint that proposes: write „the plot blueprint proposes / recommends …“, never as settled; keep its hedges (`möglicherweise` and the like); it addresses the author („Sie sollte …“). German — quote as written; the body carries 236 `\[cite: N]` marks pointing to sources it does not contain — cut every quotation before `\[cite`; cut before inner straight quotes; `--find` drops digits glued to words („Akt 1“ shows as „Akt“) — quote around them.

## Pages — document 193, `plot-entwicklung-fuer-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L19, L20, L21, L25, L26, … (77 lines). central (2–4): „AEGIS, das autopoietische, informationsbasierte System“ (L60); it rests on the principle of demarcation and isolates itself from the Potentialmeer (L174); „AEGIS' logikbasierte Systeme sind fundamental unfähig“ to grasp the connection (L139); „AEGIS wird so zum Opfer seiner eigenen rigiden Definition“ (L75); the climax as a clash of principles, not a battle (L192).
- **`alters`** (central, 3–12 quotations): the census's surfaces — `Alters` L20, L36, L37, L44, L45, L46, … (11 lines). central (2–4): Kael's alters appear uncontrolled at first (L36); at the turning point he sees them as valuable parts, not hostile fragments (L50); the table assigns an alter type to each world (L116).
- **`cerberus`** (central, 3–12 quotations): the census's surfaces — `Cerberus` L26, L45, L65, L66, L67, L77, … (10 lines). minor (1–2): the Guardian of KW3, one per Kernwelt (L65–L67); read what L66 says of his intervention.
- **`did`** (minor, 1–4): the census's surfaces — `DID` L25, L36, L60, L157. minor (1–2): Kael's „Dissoziativen Identitätsstörung (DID)“ in the setup (L25) — cut before the cite; his DID as the plainest image of fragmentation (L157).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L30. occurrence: the general word in the Kernwelten's function (L30).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L26. minor (1–2): read the sentence at L26 where AEGIS's struggle against entropy stands — cut before the cite.
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L26, L41, L56, L65, L67, L73, … (13 lines). central (2–4): „Guardians, die jeweils eine Kernwelt überwachen“ (L65); their interventions ineffective or counterproductive (L66); their „blinden Flecken“ from their specialisation (L67) — cut before the inner quotes; they may begin to gather contradictory data (L26).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L19, L20, L21, L25, L26, L27, … (42 lines). central (2–4): the Kael-Juna-Verbindung as „kein gewöhnlicher Kommunikationskanal“ (L127); its effect on Kael's deepest layers, perhaps tied to his origin in the Kohärenz-Insel (L129); „Die Kael-Juna-Verbindung ist der entscheidende Katalysator“ (L133); it is no superpower (L143) — cut before the inner quotes.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L19, L20, L21, L25, L26, … (86 lines). central (2–4): his fragmentation and AEGIS's control in Act 1 (L19); his integration as „eine ontologische Verschiebung“, the integrative way of being of the Kohärenz-Insel, „seine ursprüngliche Natur“ (L54) — cut before cites; the final decision as the culmination (L209); three endings, transcendence recommended (L203–L211).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L26, L46, L65, L66, L67, L107, … (7 lines). minor (1–2): the Guardian of KW4, one per Kernwelt (L65–L67).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L17, L19, L20, L21, L25, L26, … (25 lines). central (2–4): „Die Kernwelten sind somit nicht nur Schauplätze“ (L30); Act 2 as the Kernwelten-Odyssee in four sequences (L20) — quote around the KW digits; „Die Kernwelten existieren an der Schnittstelle von Psyche und System“ (L162); the worlds' table (L116).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the project's name in the title (L11).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L20, L43, L83, L85, L116, L168. minor (1–2): KW1: „In dieser hyper-logischen, rigide geordneten Welt“ (L43); the limits of logic, senseless rules and paradoxes (L168).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L26, L43, L65, L66, L67, L86, … (7 lines). minor (1–2): the Guardian of KW1, whose rigid logic provokes resistance in Kael (L66).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L26, L44, L65, L66, L67, L77, … (8 lines). minor (1–2): the Guardian of KW2, one per Kernwelt (L65–L67).
- **`nexus`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Nexus` alone on L163. minor (1–2): the connection's origin outside AEGIS's system, „in der Kohärenz-Insel“ or a Nexus joined to it (L163) — cut before the cite.
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L25, L54, L163, L174, L192, L204, … (8 lines). minor (1–2): AEGIS isolated from the uncontrollable Potentialmeer (L174); read L54 and L192 for its other lines.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L52. minor (1–2): read the sentence at L52 where the Realitätsebene stands (Kael's final choice).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L20, L26, L30, L68, L118, L151, … (8 lines). minor (1–2): „Die Konsequenz dieser fehlgeschlagenen Kontrollversuche und der internen Datenkonflikte sind die“ Risse (L68) — cut before the inner quotes; read L26 or L151 for a second line.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L160. occurrence: „Realität vs. Simulation“ (L160) is a thematic heading, nothing of the Überwelt.

**A page the census reaches by another surface** (read it too):

- **`kael-julia-bindung`**: central (2–4): J13: the `Kael-Juna-Verbindung` (27 times), the clipped `K-J-Verbindung` and the `Kael-Juna-Resonanz` — three written names (the note, §3); it bypasses AEGIS's protocols (L127); its origin outside AEGIS's system (L163).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` is the Guardians' title, read on guardians.
- `ars`: `autopoietische` (near `arsautopoietischereentrysegmentierung`). occurrence: `autopoietische` describes AEGIS, read on aegis — not the ARS.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz-Insel` (near `koharenz`), `integrative Kohärenz` (near `koharenz`), `Kohärenz durch Abgrenzung` (near `koharenz`), `Kohärenz durch Integration` (near `koharenz`). occurrence: the Protokoll's name; Kohärenz-Insel, integrative Kohärenz and Kohärenz durch Abgrenzung/Integration are the blueprint's constructs, read on kael, juna and kael-julia-bindung.
- `moonshine-link`: `Moonshine` (near `moonshinelink`). occurrence: `Moonshine` is the mathematical analogy for correlations (L46), not the Moonshine-Link.


**Record entries** (one file each):

- **`c4-guardians-and-aegis`**: the Guardians' blind spots from their specialisation drive the escalation (L67).
- **`c6-guardians-count-and-pairing`**: four Guardians, one per Kernwelt — LogOS, Mnemosyne, Cerberus, Kairos; no Sophia (L65–L67).
- **`c16-kael-origin`**: Kael's „ursprüngliche Natur“ as the integrative way of being of the Kohärenz-Insel (L54, L129).
- **`q5-guardians-and-kern-welten`**: one Guardian per Kernwelt (L65).
- **`q8-aegis-after-the-vortex`**: three endings — Kael transcends AEGIS, system collapse and rebirth, partial transcendence/coexistence; transcendence recommended (L203–L211).
- **`q9-moonshine-link-boundary`**: the connection bypasses AEGIS's protocols and surveillance (L127); invisible to AEGIS at first (L129).

**Chapters:** none — the blueprint gives acts and sequences, no chapter numbers.

**Not promoted:** the Kohärenz-Insel (on kael, juna, C16 — a candidate for its own page, left for the author), the three-act labels, the four bold labels of each world section, the Monstergruppe metaphor, Internal Family Systems, Transzendenz.

**Two readers**, disjoint: (1) kael, juna, kael-julia-bindung, alters, did, nexus, realitaetsebenen and the records c16, q8, q9; (2) aegis, guardians, logos, mnemosyne, cerberus, kairos, kern-welten, konstrukt-stadt, potentialmeer, risse, entropie and the records c4, c6, q5.
