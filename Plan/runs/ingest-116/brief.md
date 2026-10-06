# Brief — readings from document 116 (step 6)

1 document, one reader, one batch: `ingest-116`. Files go to `Plan/runs/ingest-116/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 116 | `romanplot-kohaerenz-protokoll-teil-1` | 2025-04-18 | „the Teil-1 plot“ (titled `Kohärenz Protokoll: Detaillierte Plot-Entwicklung und Narrative Gestaltung – Teil 1 (Kapitel 1-13)`) | a German plot proposal of 2025-04-18 for Part 1: four proposed side characters, one per Kern-Welt (Lex, Echo, Silas, Anya, L13–L47); thirteen chapters with a Heldinnenreise stage, a song theme, a primary Kern-Welt, a summary and key scenes (L49–L290); a Kern-Welt/Guardian/Psyche matrix (L292–L304); five worked moments (L306–L348); a synthesis (L350–L358). Written in the conditional throughout (`vielleicht`, `möglicherweise`, `könnte`); bracketed numbers like `\[1071-1074\]` are the export of an earlier text's line references |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (359 lines for `romanplot-kohaerenz-protokoll-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A proposal, hedged: write „the Teil-1 plot proposes …“, keep its `vielleicht`, `möglicherweise`, `könnte` as hedges, and never state its chapters as the novel's. Its side characters are proposals that reuse names the corpus uses otherwise — `Lex` as a construct of KW1 („Einheit 734“), `Silas` as a skeptic of KW3, `Echo` as a lost girl of KW2 — say what this document makes of each, without merging it with other sources' figures. Its alters are named by role (`Architekt`, `Kind/Echo`, `Wächter`, `Funke`), not by name. Kael is male. Quote around the bracketed reference numbers.

## Pages — document 116, `romanplot-kohaerenz-protokoll-teil-1`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L68, L103, L104, L188, L198, L214, … (16 lines). minor (2): LogOS escalating within the AEGIS hierarchy (L104); AEGIS registering Kael's integration as a dangerous rise in entropy (L263); Cerberus/AEGIS escalation (L198).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L36. occurrence unless more: `Alters` at L36 — read only if the line says more than in passing.
- **`cerberus`** (central, 3–12 quotations): the census's surfaces — `Cerberus` L37, L38, L160, L161, L178, L188, … (12 lines). minor (2): cold efficiency of surveillance (L161), Juna's connection as contraband (L160), a „Säuberungs“-Protokoll (L198); matrix row (L301).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L84, L132, L138, L179, L232, L244. minor (1–2): the first DID symptom, lost time (L84); a DID intrusion (L138); breakthrough clarity about his DID (L244).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L263, L270, L358. minor (1): AEGIS registers Kael's integrated state as a dangerous entropy rise (L263).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L33, L39, L150, L151, L169, L187, … (8 lines). minor (1–2): KW3, oppressive, distrust and control (L151, L156); matrix: `Wächter-Anteil` (L301).
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L207, L251, L271, L272, L281, L287, … (12 lines). minor (1–2): the Guardians' blind spots as systemic, driving how the Risse and Juna are misread (L304); the Überwelt as their operative domain (L281).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L22, L30, L38, L45, L46, L60, … (29 lines). central (2–4): `Juna-Echo` as an illogical warmth in KW1 (L69); Juna as anchor in KW2 (L122); as contraband in KW3 (L160); her absence at the lowest point (L197); the matrix column `Manifestation Juna-Echo` (L298–L302).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L19, L22, L27, L29, L30, … (90 lines). central (4–6): wakes after the reboot in the Konstrukt-Stadt and accepts it (L60); the first DID symptom, lost time (L84); his inner voices by role — the „Architekt“ (L69, L102), „Kind/Echo“ (L102), the „Wächter“-Anteil switching in KW3 (L179), the „Funke“ (L207); from victim to seeker (L139); the fragile acceptance of his Multiplizität (L244); entering the unstable Überwelt as a conscious entity (L281, L358).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L45, L46, L207, L214, L225, L231, … (9 lines). minor (1–2): Anya perhaps an agent of Kairos (L45); a possible intervention of Kairos (L207); matrix `Kairos & Sophia` (L302).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kern-Welten` L15, L51, L249, L263, L272, L281, … (10 lines); `Kern-Welt` L15, L23, L31, L39, L47, L51, … (29 lines). central (2–3): progression through the Kern-Welten not strictly linear (L51); the Kern-Welt/Guardian/Psyche matrix of four worlds (L294–L304); the boundaries between them collapse at Kap 13 (L281).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: the title (L11) — occurrence (J9).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L17, L21, L23, L59, L60, L77, … (8 lines). minor (1–2): KW1, hyper-logical, accepted as normal after the reboot (L60); matrix row: `Architekt-Anteil`, logic and causality (L299).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L19, L22, L67, L78, L86, L96, … (7 lines). central (2–3): the proposed `Der Archivar` of KW1, „Einheit 734 / „Lex““, a nickname by Kael (L19); an uncanny humanoid construct (L20), a subroutine under LogOS (L21), an information source limited by LogOS's literal logic (L22, L86) — this document's Lex, a construct, not an alter.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L21, L22, L60, L68, L78, L85, … (9 lines). minor (2): KW1's Guardian; Lex a subroutine under it (L21); subtle corrections of the Risse (L68), overt intervention (L85), struggling to contain the large Riss (L104); matrix row (L299).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L29, L30, L114, L122, L123, L142, … (8 lines). minor (1–2): a passive, empathic presence in KW2 (L123); its inability (L142); matrix row (L300).
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L41, L47, L206, L215, L224, L243, … (7 lines). minor (1–2): KW4, guided by intuition and symbols (L225); matrix: `Funke-Anteil` (L302).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Multiplizität` L232, L244, L252, L270, L347, L356. minor (1): a fragile, conscious acceptance of his Multiplizität (L244).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L25, L29, L31, L87, L105, L113, … (9 lines). minor (1–2): KW2, fluid and dreamlike, changing with Kael's emotions (L114); matrix: `Kind/Echo-Anteil` (L300).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L22, L30, L38, L60, L78, L83, … (22 lines). central (2–4): escalation from a small visual glitch (L68) through escalating Risse (L83) and a large Riss event (L103) to the `Sicherheitslücken-Riss` (L178) and rampant Risse (L194), system-wide by Kap 12 (L263); matrix column (L298–L302).
- **`silas`** (central, 3–12 quotations): the census's surfaces — `Silas` L35, L38, L151, L157, L160, L170, … (11 lines). central (2–3): the proposed `Der Skeptiker/Torwächter` of KW3, a weathered, suspicious man (L35–L36), perhaps a projection of Kael's own defences (L37), an obstacle and source of paranoia (L38); meeting him (L157); his possible fate in Kap 8 (L195) — this document's Silas, a skeptic, not a caretaker; say so.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L207, L214, L235, L244, L254, L271, … (7 lines). minor (1): a possible intervention of Sophia restoring balance (L207); a probe by Sophia/AEGIS (L244); matrix (L302).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L243, L262, L263, L272, L280, L281, … (13 lines). central (2–3): Kap 11 with interfaces to Überwelt concepts (L243); Kap 13 the transition into the unstable Überwelt, „die operative Domäne der Guardians“ (L281); the end of Part 1 as Kael's entry into it (L358).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` the world guardians.
- `mnemosyne-server-architektur`: `Architekt` (near `mnemosyneserverarchitektur`). occurrence: `Architekt` is Kael's logical part (L69, L102), not the server architecture.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` the proposed lost child and `Kind/Echo` part (L27, L102), not the residual echoes.


**Record entries** (one file each):

- **`q7-what-734-names`**: `Einheit 734` as the designation of the proposed construct Lex, the archivist of KW1 (L19) — a new bearer of 734, in a proposal of 2025-04-18; recorded, before the author's answers, changing neither.
- **`q4-waechter-four-bearers`**: `Wächter` as a part of Kael — the paranoid, defensive „Wächter“-Anteil that may switch in KW3 (L157, L179, L301) — and Silas as `Skeptiker/Torwächter` (L33); say which bearer each is.
- **`q5-guardians-and-kern-welten`**: the matrix — LogOS–KW1, Mnemosyne–KW2, Cerberus–KW3, `Kairos & Sophia`–KW4 (L299–L302), each with a blind spot.

**Not promoted:** the proposed side character Anya (L41–L47); the Heldinnenreise stages and song themes of each chapter; the alters by role (Architekt, Kind/Echo, Wächter, Funke) — on kael and the world pages; the five worked moments (L306–L348); `Schnittstelle für Mentale Gesundheit`, `Säuberungs`-Protokoll.

**Chapter readings** (Kap 1–13) are written by the session from `Plan/runs/ingest-116-kap/brief.md`, not by the readers.

**Split into two readers, one after the other:**
- Reader 1: kael, juna, aegis, lex, silas, logos, mnemosyne, cerberus, kairos, sophia, guardians, and the entries q7, q4, q5.
- Reader 2: kern-welten, konstrukt-stadt, resonanz-landschaft, grenzfeste, moeglichkeits-garten, ueberwelt, risse, did, multiplizitaet, entropie, alters.
