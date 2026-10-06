# Brief — readings from document 125 (step 6)

1 document, one reader, one batch: `ingest-125`. Files go to `Plan/runs/ingest-125/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 125 | `konzept-und-story-fuer-den-roman-kohaerenz-protokoll-mit-sub` | 2025-05-02 | „the concept with subplots“ (titled `Konzept und Story für den Roman "Kohärenz Protokoll" (mit Subplots)`, L11) | a German concept of 2025-05-02 that lays the novel over three Teile and 39 chapters, one line per chapter tagged with the five subplots it carries (L21), and closes with what each theme does (L79–L86); a plan with hedges, no canon claim. A version without subplots is in the queue and will be read after it |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (89 lines for `konzept-und-story-fuer-den-rom`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A concept plans: write „the concept with subplots plans / has …“; its „Subplot N“ tags are its own bookkeeping; „könnte“ and „möglicherweise“ mark its hedges. Kael is male. Chapter pages are done by the session.

## Pages — document 125, `konzept-und-story-fuer-den-roman-kohaerenz-protokoll-mit-sub`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L13, L17, L19, L21, L25, L27, … (36 lines). central (2–4): the expansion „Autonomous Entropic Gatekeeper for Integrity Systems (AEGIS)“ (L17); its goal of „Kohärenz“ (L17); the primary antagonist driven by its core paradox (L80); fights entropy and creates it (L84); defeated, transformed or reduced in Kapitel 36 (L72).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L29, L33, L35. minor (1–2): „Alex (Protektor ANP)“ (L29); Kapitel 9 (L35).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L79. minor (1–2): „Die Entwicklung der einzelnen Alters“ (L79).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L48. minor (1–2): „Kael (Lex/Argus)“ identifying the paradox (L48).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L29, L35, L47. minor (1–2): „Cerberus (Guardian KW3)“, embodying AEGIS's defences (L29); L35.
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L17, L37, L48, L51, L67, L84. minor (1–2): „Das zentrale Organisationsprinzip“ (L84); AEGIS's entropy management creates instability (L48).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L21, L25, L37, L43, L53, L61, … (7 lines). minor (1–2): the subplot `Das Mysterium Juna/V & die Externe Ebene` (L21); first hints in Kapitel 22 (L53); the „Andere“ outside AEGIS's control (L82).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L35. minor (1–2): „die Grenzfeste (KW3), die Domäne von Cerberus“ (L35).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L46, L47, L54, L64, L68, L72, … (7 lines). central (2–4): five Guardians „(LogOS, Mnemosyne, Cerberus, Kairos, Sophia)“ (L47), placed in their domains in the Überwelt (L46), with blind spots (L47, L80); enforcers (L64); their fate decided in Kapitel 36 (L72).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L17. central (2–4): Juna/V: first contact in Kapitel 22 and 25 (L53, L56), intervening in Kapitel 30, with its relation to the Fundament (L66); the „Andere“ outside AEGIS's control (L82) — cut the quotation before the straight quotes.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L13, L17, L19, L21, L25, L27, … (45 lines). central (2–4): „dem Host-Anteil eines dissoziativen Systems (Tertiäre Strukturelle Dissoziation)“ (L17); wakes in the Konstrukt-Stadt with amnesia (L27); lives in functional multiplicity, an open end (L75).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L47. minor (1–2): named among the five Guardians (L47) — nothing more.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L25, L46, L52, L68, L81. minor (1–2): KW1 the Konstrukt-Stadt (L27), KW2 the Resonanz-Landschaft (L31), KW3 the Grenzfeste (L35); the worlds as manifestations of Kael's psyche and AEGIS's control (L81).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L30, L32, L79. minor (1–2): the underlying fear (Kiko) Rhys soothes (L30); an EP holding fragments (L32); „Kikos Angst“ (L79).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — `Kohärenz` L11, L13, L17, L39, L48, L67, … (8 lines). occurrence: the title and the protocol's name (J9); the „Paradoxon der Fehlausgerichteten Kohärenz“ is read on aegis.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L27, L28. minor (1–2): Kael wakes „in der Konstrukt-Stadt (KW1)“ (L27); Kapitel 2's title (L28).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L21, L25, L28, L33, L36, L37, … (11 lines). central (2–4): „Lex (Analytiker ANP)“ (L28); identifies the paradox with Argus (L48); his subplot `Lex' Systemanalyse & AEGIS' Paradoxon` (L21).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L32. minor (1–2): an EP with Kiko (L32).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L27, L28, L34, L47. minor (1–2): „LogOS (Guardian KW1)“ (L28).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L31, L32, L34, L47. minor (1–2): „Mnemosyne (Guardian KW2)“ (L31); manipulates or censors memories (L32).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L19, L55, L64, L74. minor (1–2): Kael's struggle for inner integration as „funktionale Multiplizität“ (L19); Kapitel 34 and 39 (L70, L75).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L79. minor (1–2): „Nyx' Wut“ in the list of alters (L79).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L31. minor (1–2): „die Resonanz-Landschaft (KW2)“, chaotic, emotional, the opposite of KW1 (L31).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L30, L33, L36, L79. minor (1–2): „Rhys (Pfleger ANP)“ (L30) — an ANP here; Rhys' Fürsorge (L79).
- **`risse`** (minor, 1–4): the census's surfaces — `Glitches` L27, L28, L34, L38, L45. minor (1–2): „Glitches“ (L27); the first Riss in Kapitel 11 (L37); the Risse „Manifestationen von Entropie/Instabilität“ (L84).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L47. minor (1–2): named among the five Guardians (L47) — nothing more.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L13, L79. minor (1–2): the concept „Basierend auf der Theorie der Strukturellen Dissoziation (TSDP)“ (L13); TSDP & Integration as the psychological backbone (L79).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Simulation` L13, L17, L27, L37, L38, L43, … (11 lines); `Überwelt` L46, L47, L63, L81. central (2–4): the Digitale Überwelt where Kael analyses the architecture (L46); the Guardians placed there (L46–L47); „der Schauplatz der Meta-Analyse und der finalen Konfrontation“ (L81); Kapitel 27 (L63).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `juna`: `Juna/V` (near `juna`). `Juna/V` is how it writes Juna (J34) — on juna above.
- `selene`: `Selenes` (near `selene`). a reading: „Selenes Integration“ (L79) — minor (1), by Reader 2.


**Record entries** (one file each):

- **`c1-aegis-expansion`**: „Autonomous Entropic Gatekeeper for Integrity Systems (AEGIS)“ (L17) — position 1 again.
- **`c6-guardians-count-and-pairing`**: five Guardians (L47), three paired: LogOS KW1 (L28), Mnemosyne KW2 (L31), Cerberus KW3 (L29, L35); Kairos and Sophia without a world — dated 2025-05-02.
- **`c9-konstrukt-stadt-scale`**: „in der Konstrukt-Stadt (KW1)“ (L27) — KW1 only.
- **`q5-guardians-and-kern-welten`**: the same pairing, and the Guardians' domains placed in the Überwelt (L46).
- **`q6-nexus-ueberraum-ueberwelt`**: the Digitale Überwelt as the stage of meta-analysis and final confrontation (L46, L81).
- **`c13-externe-ebene-beyond-the-simulation`**: the Externe Ebene/Juna/V as the „Andere“ outside AEGIS's control (L82); first hints in Kapitel 22 (L53).

**Not promoted:** the five subplot titles (read on the pages they touch), the Heroine's/Hero's Journey labels, the tropes list (L85), Gaslighting, Ko-Bewusstsein, Elixier, Paradoxon X (L83).

**Split into two readers, at the same time on disjoint pages:**
- Reader 1: aegis, guardians, logos, mnemosyne, cerberus, kairos, sophia, risse, entropie, externe-ebene, juna, ueberwelt, and the entries c1, c6, q5, q6, c13.
- Reader 2: kael, lex, alex, rhys, kiko, lia, nyx, argus, alters, selene, tsdp, multiplizitaet, konstrukt-stadt, kern-welten, resonanz-landschaft, grenzfeste, and the entry c9.
