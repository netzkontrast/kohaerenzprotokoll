# Brief — readings from document 264 (step 6)

1 document, one reader, one batch: `ingest-264`. Files go to `Plan/runs/ingest-264/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 264 | `kernwelten-und-fragmentierte-wahrnehmung` | 2025-04-29 | „the perception report“ (an unsigned German research report) | a two-stage research report on how System Kael's eleven parts perceive the four Kernwelten: research synthesis (Part 1), character-informed world profiles (Part 2), a narrative toolkit with an alter-world matrix excerpt, three voice guides and one scene from three perspectives (Part 3), writing recommendations (Part 4); mostly conditional (`könnte`, `wahrscheinlich`), its TSDP sorting cited from a `User Query Context` it does not reproduce |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (461 lines for `kernwelten-und-fragmentierte-w`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report that proposes: write „the perception report proposes / describes / sorts …“ and keep its hedges (`könnte`, `wahrscheinlich`, `potenziell`) in the reading; the ANP/EP sorting (L93–L94) and the tertiary dissociation (L96) are cited by the document from a `User Query Context`, so say so. The scene of L384–L400 is an illustration written in each part's voice, not story canon. Cut quotations before bold markers and footnote digits glued to words (`Kontrolle 12`).

## Pages — document 264, `kernwelten-und-fragmentierte-wahrnehmung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L48, L49, L76, L115, L141, L147, … (27 lines). central (3–6): AEGIS by world: direct control of environment parameters in KW1 (L151), weaker control and KW2 as a threat to its control paradigm (L193, L195), the architect of threat in KW3 (L235, L237), KW4 as what it fears most (L279); the Post-Reboot State entries (L152, L194, L236, L278); possibly manipulating the parts' cognitive maps or imposing Lex's (L48); KW1 as the order AEGIS favours (L115).
- **`alex`** (central, 3–12 quotations): the census's surfaces — `Alex` L64, L93, L106, L132, L215, L227, … (15 lines). minor (1–3): an ANP sorted with Kael, Lex and Rhys (L93); possibly activated as crisis manager in KW2 (L106); Erlebte Rede and ANP unreliability rows (L294, L329).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L152, L185, L227, L257, L269, L292, … (7 lines). minor (1–3): possible reflecting in KW4 (L269); interior monologue for critical evaluation (L292); not placed by the ANP/EP sorting — say so.
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L31, L152. minor (1–3): Kael's „Cache Kohärenz“ problem, explained by amnesia and time gaps (L31); KW1's post-reboot glitches could mirror it directly (L152); never defined.
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L197, L384. minor (1–3): KW3 titled „Grenzfeste/B (Bedrohung/Grenze)“ (L197), its core principle (L199), the sensory profile (L204–L207); the scene in KW3 (Grenzfeste) (L384).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L49, L82, L94, L173, L257, L325, … (7 lines). minor (1–3): an EP (L94); a colour scheme in KW1 might trigger her (L49); EP unreliability row (L330).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L23, L28, L29, L30, L31, L43, … (34 lines). central (3–6): „System Kael“ with eleven parts (L81) and a tertiary structural dissociation (L96, cited from User Query Context); Kael as an ANP whose experience depersonalisation may shape (L29, L93); his map oriented to efficiency and control (L48); KW1 appeals to him (L105); KW3's architecture could induce derealisation (L49); the „Cache Kohärenz“ problem (L31).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L28, L31, L49, L75, L86, L109, … (11 lines); `Kernwelt` L28, L31, L48, L49, L75, L86, … (16 lines). central (3–6): four worlds with their pairs (L104), headed by slash names (L113, L155, L197, L239), each with a core principle (L115, L157, L199, L241); as active triggers and amplifiers of dissociative states (L49); every part has its own cognitive map of each world (L48); the matrix excerpt is partial (L337).
- **`kiko`** (central, 3–12 quotations): the census's surfaces — `Kiko` L41, L48, L49, L63, L82, L94, … (28 lines). central (3–6): an EP (L94), fear central to her experience (L41), map of danger zones (L48); KW2 sounds trigger flight (L49, L106); the matrix rows (L346–L347); the voice guide (L364–L366); the KW3 scene from her perspective (L390–L392).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — the title (L11).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L113. minor (1–3): KW1 titled „Konstrukt-Stadt/Co₁ (Ordnung/Kontrolle)“ (L113), its core principle of logic, structure, efficiency and control, potentially the order AEGIS favours (L115); the sensory profile only if it adds (L120–L123).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L48, L62, L82, L93, L105, L106, … (32 lines). central (3–6): an ANP (L93); the rationalist whose map AEGIS could impose as standard (L48); KW1 appeals to him (L105) and mirrors his ideal (L115, L123); the matrix rows (L344–L345); the voice guide „Lex (Primärer ANP - Rationalist)“ (L355–L359); the KW3 scene from his perspective (L386–L388).
- **`lia`** (central, 3–12 quotations): the census's surfaces — `Lia` L94, L105, L173, L174, L185, L215, … (13 lines). minor (1–3): an EP (L94); invalidated in KW1 (L105); play in KW4 (L269).
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L239. minor (1–3): KW4 titled „Möglichkeits-Garten/Ly (Potenzial/Möglichkeit)“ (L239), its core principle (L241), what AEGIS fears most (L279).
- **`moros`** (central, 3–12 quotations): the census's surfaces — `Moros` L32, L43, L48, L94, L131, L143, … (14 lines). minor (1–3): an EP (L94); time distortion for his rigidity (L32), emptiness and depression shaping his state (L43), a static or empty map (L48); freezing before possibilities in KW4 (L269).
- **`nyx`** (central, 3–12 quotations): the census's surfaces — `Nyx` L42, L63, L94, L106, L107, L131, … (19 lines). minor (1–3): an EP (L94); anger relevant to her mode of perception (L42); KW2 triggers her fight (L106).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L155. minor (1–3): KW2 titled „Resonanz-Landschaft/McL (Emotion/Chaos)“ (L155), its core principle (L157), a threat to AEGIS's control paradigm (L195).
- **`rhys`** (central, 3–12 quotations): the census's surfaces — `Rhys` L62, L82, L93, L105, L106, L107, … (28 lines). central (3–6): an ANP (L93), invalidated in KW1 (L105), brought to his limits in KW2 (L106); connecting in KW4 (L269); the matrix rows (L348–L349); the voice guide „Rhys (Sekundärer ANP - Pfleger/Beziehungsorientierter)“ (L373–L380); the KW3 scene from his perspective (L394 onward).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L142. minor (1–3): cracks or anomalies in KW1's perfect structure (L142), only if the line places them as Risse of the world.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L185, L257, L269, L326, L329. minor (1–3): placed only with a question mark: the Erlebte Rede and ANP unreliability rows write „Selene?“ (L326, L329); reflecting in KW4 (L269).
- **`tsdp`** (central, 3–12 quotations): the census's surfaces — `TSDP` L84, L86, L88, L104, L107, L111, … (16 lines). central (3–6): TSDP as the frame for the parts' subjective experience (L86); the ANP/EP split (L92) and their perceptual filters (L93–L94); phobies between parts (L95); tertiary structural dissociation (L96); the worlds interacting selectively with the parts' TSDP profiles (L104); action systems as perceptual filter (L107) — the sorting is cited from a User Query Context.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L76. not read: occurrence — `Simulation` at L76 is a media example (Inception), not the Überwelt.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `did`: `Fragmentierung` (near `psychischefragmentierung`). occurrence: `Fragmentierung` is the clinical term of the research synthesis (L30), not the page's term.
- `personas`: `Depersonalisation` (near `persona`). occurrence: `Depersonalisation` is a dissociative symptom (L29), not a persona.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: eleven parts (L81, L285) and four Kernwelten (L104, L111); the matrix would cover „alle 11 Anteile und 4 Welten“ (L337).
- **`c9-konstrukt-stadt-scale`**: KW1 headed „Konstrukt-Stadt/Co₁ (Ordnung/Kontrolle)“ (L113).
- **`c5-garten-scale`**: KW4 headed „Möglichkeits-Garten/Ly (Potenzial/Möglichkeit)“ (L239), a world.

**Not promoted:** the cognitive maps, the alter-world matrix, the voice guides, the media models (Silent Hill, Disco Elysium, Solaris, Inception), `Co₁`, `McL`, `B`, `Ly` as names, the Insight references.

**One reader**: every page above and the records q3, c9, c5.

**Chapter readings**: none — the document names no chapter.
