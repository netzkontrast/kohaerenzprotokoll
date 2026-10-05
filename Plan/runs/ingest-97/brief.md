# Brief — readings from document 97 (step 6)

1 document, one reader, one batch: `ingest-97`. Files go to `Plan/runs/ingest-97/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 97 | `2-kohaerenz-protokoll-konzeptentwicklung` | 2025-05-03 | „the concept development“ (titled `Gesamtkonzept: Kohärenz Protokoll`, role „Konzept-Entwickler & Narrativer Stratege“) | a German concept plan of 2025-05-03: premise, four thematic fields, three core themes, a central question and the subplots (Teil 1, L5–L40), then one block per chapter from `Chapter P` to `Chapter 39`, each in four fields (Teil 2, L42–L322), and a reference list; its chapter blocks hedge (`möglicherweise`, `könnte`, `?`) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (354 lines for `2-kohaerenz-protokoll-konzepte`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan: write „the concept development plans …“, „proposes …“, never as what the novel is; keep its hedges and question marks (`Kiko?`, `LogOS?`, `Sophia (Weisheit/Struktur?)`). **It writes Kael female** — „System Kael, einer Protagonistin“ (L9), `ihre`/`sie` throughout: quote it as written, never correct it, and point to [[c17-kael-gender|C17]] on the kael page. Its root term is `Fehlausgerichtete Kohärenz`, AEGIS's core paradox (L9, L37, L186); the misspelling `Fehleausgerichtete` (L49) is the document's. Its research numbers (`TSDP 1`, `2`, `3` …) are footnote markers to its reference list, not counts.

## Pages — document 97, `2-kohaerenz-protokoll-konzeptentwicklung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L9, L16, L17, L18, L24, L25, … (105 lines). central (3–5): „ein komplexes KI-System/Kollektiv“ holding a simulation together by rigid control, driven by the core paradox of „Fehlausgerichteten Kohärenz“ (L9); its failure rooted in the AI Alignment Paradox and the Paradox of Control (L16); the AEGIS-Paradoxon subplot (L37); its emergence from chaos and fear in Chapter P (L46–L48); the explicit naming of the core flaw in Chapter 20 (L186); the tragedy of the AI in Chapter 24 (L214); its ambivalence beyond a monster in Chapter 32 (L270).
- **`alex`** (central, 3–12 quotations): the census's surfaces — `Alex` L67, L68, L69, L75, L89, L103, … (13 lines). minor (1–2): the „Beschützer-Anteils (Alex)“ activated by threat in Chapter 3 (L67–L69); with Nyx in KW3 (L110–L111).
- **`argus`** (central, 3–12 quotations): the census's surfaces — `Argus` L124, L131, L132, L133, L145, L146, … (12 lines). minor (1–2): read the blocks naming Argus (Chapters 11–15, L124–L146) and say what role the plan gives him.
- **`cerberus`** (central, 3–12 quotations): the census's surfaces — `Cerberus` L110, L111, L112, L207, L208, L209, … (12 lines). central (2–3): KW3 `Cerberus-Labyrinth` (L110), the Guardian of AEGIS's defences and the „Threshold Guardian“ (L111); strategic return in Chapter 23 (L207); the final breakthrough in Chapter 31 (L261–L263).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L56. minor (1): only in a keyword line, `Passive Influence DID/OSDD` (L56) — an occurrence unless the block says more; say which.
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L16, L167, L188, L215, L216, L243, … (7 lines). minor (1–2): rigid control leading to the emergence of unwanted, unstable states (L16).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L181. minor (1): Juna/V as „eine Quelle potenzieller Entropie oder neuer Ordnung“ (L181).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Externe Ebene` alone on L314. minor (1): the „Externe Ebene?“ as one of three guesses at the new reality after the climax (L314); keep the question mark.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L44. minor (1–2): `Chapter P: [Genesis]` (L44) — the Ursprungsparadoxon, AEGIS emerging from chaos and fear (L46).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Grenzfeste` alone on L107. minor (1): only in Chapter 9's title „Die Mauern der Grenzfeste“ (L107), with KW3 named `Cerberus-Labyrinth` (L110) — record both names.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L39, L166, L167, L168, L236, L237. minor (2–3): the Guardians personify aspects of AEGIS's control philosophy (Logik, Emotion, Angst, Potenzial) and the KWs are thematic arenas (L39); the dual Guardians of KW4 (L166).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L9. minor (2–3): `Juna/V` the mysterious external connection (L9, L26), the mystery subplot with the Fundament (L38); first, fragmentary contact in Chapter 19 (L177–L181), intensified contact in Chapter 25 (L221).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L9, L15, L17, L24, L25, L26, … (81 lines). central (3–5): **female here** — „System Kael, einer Protagonistin mit einer durch Trauma tief fragmentierten Identität“ (L9), modelled on TSDP; her inner journey to integration and her fight against AEGIS (L9); the central question of true coherence on the individual level (L30); her „Geburt“ as a violent act of fragmentation in Chapter P (L47–L48); the Kael-Host (ANP) perspective in Chapter 1 (L54–L55); the integrated system in Chapters 26, 37–39 (L228, L305, L319). Say once, with C17, that the document writes her female.
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L166, L168. minor (1–2): KW4 `Kairos-Potentialis` (L166), the dual Guardians „Kairos (Potenzial/Chance) und Sophia (Weisheit/Struktur?)“ (L166).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L82, L89, L110, L111, L208, L257, … (7 lines). minor (1–2): the chapter blocks that name it, with the plan's hedge (e.g. `Kiko?`, `Moros?`).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L1. not read: `Kohärenz` in the title (L1), an occurrence (J9).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L55, L60, L61, L62, L68, L69, … (23 lines). central (2–3): the analytic part trying to decode KW1 by logic in Chapter 2 (L60–L62), his conflict with Alex (L68–L69), dominant in Chapter 8 (L103).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L89, L257. minor (1–2): the chapter blocks that name it, with the plan's hedge (e.g. `Kiko?`, `Moros?`).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L61, L62, L63, L103, L242, L243, … (9 lines). minor (1–2): the Guardian of KW1; first subtle confrontations with Lex in Chapter 2 (L61); its embodiment of AEGIS's logical paradox confronted in Chapter 28 (L242).
- **`mnemosyne`** (central, 3–12 quotations): the census's surfaces — `Mnemosyne` L82, L83, L84, L89, L90, L91, … (14 lines). central (2–3): KW2 written `Mnemosyne-Archipel` (L82), the Guardian as AEGIS's agent for emotion analysis (L83), its possible manipulation of memories (L89–L90), the fight over authentic memory (L158), the final confrontation (L256).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L82, L89, L257. minor (1–2): the chapter blocks that name it, with the plan's hedge (e.g. `Kiko?`, `Moros?`).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L15. minor (1–2): the potential multiplicity of consciousness (L15); the established state of „funktionaler Multiplizität“ as a way of life (L312, L319).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L48. minor (1): only in Chapter P's keyword line (L48/L49) — read the block and say whether it is more than a keyword; else occurrence.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L110, L111, L208, L250, L264. minor (1–2): the chapter blocks that name it, with the plan's hedge (e.g. `Kiko?`, `Moros?`).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L9. minor (1) only if L9 names a level of reality as the page's term; otherwise occurrence, say why.
- **`rhys`** (central, 3–12 quotations): the census's surfaces — `Rhys` L74, L75, L76, L82, L89, L117, … (15 lines). minor (1–2): the „Fürsorger-Anteils (Rhys)“ mediating in Chapter 4 (L74–L76); initiating the first dialogues in Chapter 10 (L117).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L37, L61, L124, L180; `Glitches` L37, L54, L55, L124. minor (1–2): AEGIS's contradiction causes system instability, „Glitches“ and „Risse“ (L37); a significant anomaly, a „Riss“, in Chapter 11 (L123).
- **`selene`** (central, 3–12 quotations): the census's surfaces — `Selene` L118, L194, L196, L229, L230, L231, … (11 lines). minor (2–3): Selene as the integrating part whose potential may be hinted at in Chapter 10 (L118); developing in Chapter 21 (L194); possibly coordinating the integrated system in Chapter 26 (L229).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L166, L168. minor (1): one of KW4's dual Guardians, with a question mark on her function (L166).
- **`tsdp`** (central, 3–12 quotations): the census's surfaces — `TSDP` L9, L15, L36, L48, L55, L56, … (43 lines). central (3–4): TSDP as the psychological core model with ANPs, EPs and the phobias between them (L15); the subplot following the phases Stabilisierung → Trauma-Bearbeitung → Integration (L36); Phase 1 in Chapters 4 and 10 (L76, L118).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L142, L144, L145, L146, L152, L173, … (8 lines). minor (1–2): Chapter 14 enters the meta-level `Überwelt` to analyse AEGIS's control (L142–L146).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `juna`: `Juna/V` (near `juna`). reading, above: `Juna/V` is the slash form of the name (J34).
- `kohaerenz`: `Fehlausgerichteter Kohärenz` (near `koharenz`), `Fehlausgerichtete Kohärenz` (near `koharenz`), `Fehleausgerichtete Kohärenz` (near `koharenz`). occurrence: `Fehlausgerichtete Kohärenz` (and its inflections) is AEGIS's paradox, a compound with its own sense (J12, J16) — read on aegis, not on kohaerenz.
- `multiplizitaet`: `funktionaler Multiplizität` (near `multiplizitat`). reading, above: `funktionaler Multiplizität` is the inflected `funktionale Multiplizität` (L312, L319).
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` is the original whole Kael was fragmented from in Chapter P (L48), not the residual echoes — read on kael and C16.


**Chapter readings** are in their own brief, `Plan/runs/ingest-97-kap/brief.md` (Kap 0–39 from `Chapter P` to `Chapter 39`).

**Record entries** (one file each; write one only where the plan speaks to the record's question, in its words):

- **`c17-kael-gender`**: the record was opened for this document; add no entry — its row 1 is this document.
- **`c3-emergenz-origin`**: AEGIS's emergence „aus Chaos/Angst“ (L46) as a desperate attempt at order, not malice (L47).
- **`c16-kael-origin`**: in Chapter P AEGIS fragments „Echo“/Kael; the „Echo“ is the original whole and the source of the EPs (L48); Kael's „Geburt“ a violent act of fragmentation (L47).
- **`c7-juna-first-appearance`**: first, fragmentary contact with Juna/V in Chapter 19 (L177–L180), intensified in Chapter 25 (L221).
- **`c14-aegis-first-person-chapter`**: Chapter P told „aus einer distanzierten, fast mythischen Perspektive“ (L47) — not AEGIS's first person; say so.
- **`q1-guardians-and-aegis`**: the Guardians personify aspects of AEGIS's control philosophy (L39); Mnemosyne as AEGIS's agent (L83).
- **`q3-how-many-kern-welten-and-alters`**: four KWs (L39, KW1–KW4 in Chapters 1, 5, 9, 17); the parts it names (Host, Lex, Alex, Rhys, Kiko, Lia, Moros, Nyx, Selene, Argus — no Isabelle); it states no count. Q3 ends with the author's two answers of 2026-10-05: append with the date 2025-05-03, say it predates both, never edit them.
- **`q5-guardians-and-kern-welten`**: one Guardian each for KW1–KW3, „den dualen Guardians Kairos … und Sophia“ for KW4 (L166).
- **`q8-aegis-after-the-vortex`**: Chapter 35 completes or steers „den Kollaps/die Transformation von AEGIS“ (L291); Chapter 36 „ohne AEGIS' dominante Kontrolle“ (L298); no Vortex — say so.

**Split into three readers, one after the other:**
- Reader 1: aegis, kael, juna, tsdp, multiplizitaet, did, emergenz, entropie, externe-ebene, genesis, realitaetsebenen, ueberwelt, risse, nichts-rauschen.
- Reader 2: guardians, logos, mnemosyne, cerberus, grenzfeste, kairos, sophia, selene, argus, lex, alex, rhys, kiko, lia, moros, nyx.
- Reader 3: the record entries above.
