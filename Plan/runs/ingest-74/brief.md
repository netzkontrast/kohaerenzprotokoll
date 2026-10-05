# Brief — readings from document 74 (step 6)

1 document, one reader, one batch: `ingest-74`. Files go to `Plan/runs/ingest-74/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 74 | `scifi-roman-mit-ki-schreiben` | 2025-06-24 | „the editor's report“ (its title: `Die Architektur einer Seele: Eine entwicklungslektorische Analyse`) | a German developmental-editing report of 2025-06-24 in four parts on a plot document it cites as reference 1 (`Romanplot: Kohärenz Protokoll, Teil 1`): Part I reads AEGIS and the Fundament through Gnosticism, process philosophy and cybernetics; Part II analyses System Kael by TSDP; Part III assesses Kap 1–13 and reproduces the plot document's tables; Part IV advises the author; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (358 lines for `scifi-roman-mit-ki-schreiben`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** **A report on another document, in two voices.** Where a sentence ends in the reference number `1` (glued to the text, e.g. `Lex.1`), it reports the plot document: write „the editor's report gives the plot document's …“. Where the report interprets (Gnostic demiurge, Pleroma, Whitehead, cybernetic homeostasis, the paradox of misaligned coherence) or advises (close third person, Dr. Thorne sessions, Einheit 734 as a recurring antagonist, AI as assistant), write „the report reads / proposes …“. Its verdict (L304) is an evaluation, never a fact. Tables 3 and 4 (L252–L288) are the plot document's, reproduced: say so. Names the Struktur-Kanon later decanonised (Echo, Limina, Nox, Chronos, Schattenkind, Sibyl, Anya, Dr. Thorne) are recorded as this 2025 document's, without comment. Quote prose, not table cells, where possible; cut a quotation before a glued reference number.

## Pages — document 74, `scifi-roman-mit-ki-schreiben`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L24, L36, L44, L48, L50, L58, … (24 lines). central (4–6): the Genesis prologue as a struggle for survival, the „Funke Struktur“ (L48); AEGIS as the Gnostic demiurge (L50, the report's reading); a cybernetic system holding homeostasis by negative feedback, deviations called „Entropie“ or „Risse“ (L78); the paradox of misaligned coherence — system coherence by control prevents Kael's psychological coherence (L95–L97); not wilfully evil, acting from functional programming (L192).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L90, L121, L137. minor (1): Alex (Beschützer) & Rhys (Pfleger) as a complementary pro-social ANP pair (L137); with Nyx among the protective or persecutor parts of KW3 (L90).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L220, L245, L254, L278. minor (1): the border warden Argus at an unstable `Threshold Zone`, Kap 4–6 (L220).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L78, L90, L192, L198, L231. minor (1–2): controls KW3 Grenzfeste (L90); identifies an unknown intrusion and isolates it (L198).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L66. minor (1) or not read: L66 heading `Kontrolle, Emergenz und die Kern-Welten` — occurrence unless the paragraph says what emerges.
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L78, L95, L184, L286. minor (1): L78, as above.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L48. minor (1): the prologue „Genesis der Existenz“ as AEGIS's survival story (L48).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L90, L221, L231. minor (1–2): KW3, the paranoid world of defence and isolation, under Cerberus (L90); the oppressive Grenzfeste and the „Ego-Tod“ of Kap 7–9 (L221).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L78, L172, L188, L192, L201, L222, … (7 lines). minor (2–3): five named — LogOS, Mnemosyne, Cerberus, Kairos, Sophia — not wilfully evil (L192); four misreadings listed (L196–L199) — record that five are named and four listed; the misreadings as the real cause of the Risse (L201).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L121. minor (1): only in the roster sentence (L121): say she is named there and nothing else is said.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L156, L172, L180, L184, L194, L220, … (12 lines). central (2–3): everything AEGIS cannot understand, a connection to a postulated „Externe Ebene“ beyond the simulation's logic (L184); the Guardians' repeated misreadings of her influence drive the plot (L194); her first clear contact in Kap 4–6 (L220).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L50, L62, L86, L88, L91, L93, … (45 lines). central (3–5): the four Kern-Welten as externalisations of Kael's psychic domains (L86); his arc from ignorance of his multiplicity to acceptance in Part 1 (L135); Tertiary Structural Dissociation with multiple ANPs and EPs (L121); the plot of Kap 1–13 as a hero's journey through KW1 → KW4 (L217).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L78, L91, L192, L199, L232. minor (1–2): KW4 kept by Kairos and Sophia (L91); sees only „interessantes Chaos“ (L199).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kern-Welten` L66, L82, L86, L217, L234; `Kern-Welt` L66, L82, L86, L217, L228, L234. central (2–3): four Kern-Welten as direct externalisations of Kael's inner domains as TSDP describes them (L86); the progression KW1 → KW4 as the inner journey (L217); Table 2 pairs each with a Guardian (L228–L232).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L89, L121, L145, L160, L164. minor (1): L145; `Echo/Kiko` among the EPs of KW2 (L89) — record the slash as the report writes it.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: title (L13) — occurrence (J9).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L88, L219, L229. minor (1–2): KW1, the world of logic, rules and order, ruled by LogOS, Kael's ANPs (L88); Kael's waking in the sterile city, Kap 1–3 (L219).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L88, L121, L136, L156, L160, L162, … (10 lines). central (2–3): ANP, the rationalist, the internal antagonist representing AEGIS's cold logic (L136); the archivist Lex in the information archive, Kap 1–3 (L219).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L91, L121. minor (1): L91 or L121 — named among the integrative parts or the roster; one line.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L78, L88, L192, L196, L229. minor (1–2): KW1 Konstrukt-Stadt ruled by LogOS (L88); registers an inexplicable logical error and corrects it (L196).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L78, L89, L192, L197, L230, L276, … (7 lines). minor (1–2): oversees KW2 (L89); perceives a memory fragment or phantom pain and archives it (L197).
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L91, L222, L232. minor (1–2): KW4, potential, creativity, transformation, under Kairos and Sophia (L91); the place of „Auferstehung“ in Kap 10–13 (L222). Record `Garten d. Möglichkeiten` in Table 4 (L281) as the plot document's spelling.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L89, L121, L146. minor (1): „Der Erstarrte“, the system's deepest wound, complete collapse (L146).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L135. minor (1): Kael's journey from ignorance of his Multiplizität to acceptance (L135).
- **`nexus`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Nexus` alone on L283. not read: `Nexus of Whispers` is a locality of Table 4 (L283) — occurrence (J12).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L48. minor (1): the Genesis prologue's hostile, dissolving environment (L48) — quote the line's words for it.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L90, L121, L145, L156, L160, L163. minor (1): Nyx (Kämpfer) & Kiko (Kind), outward rage over unbearable vulnerability (L145).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L89, L220, L230. minor (1–2): KW2, the fluid world of emotions and memories, under Mnemosyne, the EPs (L89).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L91, L121, L137, L156, L160, L165, … (7 lines). minor (1): with Alex, L137.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L78, L201, L219, L228, L275. minor (1–2): deviations called „Entropie“ or „Risse“ (L78); the Risse as symptoms of the wrong treatment, not the disease (L201).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L91, L154, L160, L166. minor (1): Wächterin/Integratorin, a potential catalyst for healing, ambivalent between blocking trauma and compassion (L154); `ANP-Regulator` in Table 1 (L160) — record both labels.
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L244, L246, L254, L280. minor (1): the plot draft integrates Silas (L244); the `Glitching Market` for the meeting with Silas (L246).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L78, L91, L192, L232. minor (1): KW4 kept by Kairos and Sophia (L91, L232).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L62, L86, L113, L117, L304. minor (1–2): spelled out as „Theorie der Strukturellen Dissoziation“ (L62) and as „Tertiäre Strukturelle Dissoziation“ (L117, L121) — record both readings of the abbreviation.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L222. minor (1) or not read: L222 only if it names the Überwelt in the report's or plot document's own words; else occurrence.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `genesis`: `Genesis der Existenz` (near `genesis`). reading, above.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Systemkohärenz` (near `koharenz`), `psychologische Kohärenz` (near `koharenz`), `fehlausgerichteten Kohärenz` (near `koharenz`). occurrence: `Systemkohärenz`, `psychologische Kohärenz` are the report's paradox (L97), read on aegis (J12).
- `nexus`: `Nexus of Whispers` (near `nexus`). occurrence (J12).
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` is a part's name (L89, L244).


**Record entries** (one file each, page = the record's file stem):

- **`q5-guardians-and-kern-welten`**: one Guardian per world — KW1 LogOS, KW2 Mnemosyne, KW3 Cerberus, KW4 Kairos & Sophia (L88–L91, L229–L232), as the plot document gives it.
- **`c6-guardians-count-and-pairing`**: five Guardians named (L192), the pairing above; four misreadings listed (L196–L199). Decide nothing.
- **`q7-what-734-names`**: `Einheit 734` as a recurring, faceless antagonist showing AEGIS's escalating power (L245, the report's proposal) and as AEGIS units in Kap 5 (L278, Table 4). This is a third sense of 734 beside Komponente and Kael — say so, decide nothing.
- **`c13-externe-ebene-beyond-the-simulation`**: Juna's connection to a postulated „Externe Ebene“ beyond the simulation's logic (L184).

One reader writes everything.
