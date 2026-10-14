# Brief — readings from document 438 (step 6)

1 document, one reader, one batch: `ingest-439`. Files go to `Plan/runs/ingest-439/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 438 | `kael-uberarbeitung-des-konzepts-unter-tsdp` | 2025-04-28 | „the TSDP revision of Kael“ (an unsigned German character concept, „Kael: Überarbeitung des Konzepts unter dem Primat der Strukturellen Dissoziation“) | makes structural dissociation the primary model for Kael's fragmentation and re-maps the Personas onto its part roles, then reads the Pressure Points, AEGIS and Juna/V through it; calls its frame clinically grounded (L121), no claim of canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (122 lines for `kael-uberarbeitung-des-konzept`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A character concept that proposes: write „the TSDP revision proposes …“; it is fiction about Kael, never anyone's real condition, and its role assignments are hedged („Primär“, „Wahrscheinlich“, „Könnte“). Its Pressure Point codes point to a list it does not contain (L94–L99). Quote the German as written; cut before straight quotes, bold markers and glued footnote digits. No gendered pronoun for Kael, Juna, AEGIS or any part — use the names (quotations stay verbatim, including the document's own pronouns). Never write a real person's name nor a term carrying one (L15).

## Pages — document 438, `kael-uberarbeitung-des-konzepts-unter-tsdp`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L23, L44, L80, L95, L99, … (10 lines). minor (1–4): AEGIS's control methods — surveillance, manipulation, punishment, forced switches? — readable as ongoing traumatisation that maintains the dissociation (L99); AEGIS still more clearly the antagonist that uses or causes dissociation to keep control (L116).
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L22, L95. minor (1–4): the „Cache Kohärenz“-problem as the manifestation of the structural dissociation (L22 — cut before the quote).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L97. minor (1–4): an environment with EP triggers „(Grenzfeste)“ where Rhys's openness becomes dangerous (L97).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L99, L114, L117. minor (1–4): „Juna/V“: the connection gains meaning as a potentially integration-promoting force that could help overcome dissociative barriers (L117); section 6 „Implikationen für AEGIS und Juna/V“ (L114).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L11, L13, L15, L17, L19, L21, … (8 lines). central (4–8): TSDP as „das primäre Erklärungsmodell“ for Kael's fragmented state (L15); Kael's personality not integrated after overwhelming trauma, perhaps connected with the creation, „M“ or early experiences under AEGIS (L17 — cut before the quote); the core problem: structural dissociation, probably tertiary, explaining the complexity of the „Personas“ (L22); the frame as the basis of Kael's characterisation (L121).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L95. minor (1–4): triggers in the Kernwelten — places, sounds, emotions — can activate EPs unbidden (L95).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L48, L62, L94, L95, L97. minor (1–4): „Das Kind“: „Primär ein“ EP carrying the childlike affects and memories of the trauma (L52); carries the core emotions of the trauma (L53); suppressed by Lex, activated by triggers (L94, L95).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: an occurrence — the novel's title (L15).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L44, L97. minor (1–4): Lex's survival and function in structured environments „(Konstrukt-Stadt)“ (L44).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L39, L94, L96. minor (1–4): „Der Logiker“: „Primär ein“ ANP, focused on everyday functioning through logic, control and avoiding emotional triggers (L43); survival in structured environments such as the Konstrukt-Stadt (L44); Lex tries to suppress Kiko and Nyx (L94).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L57, L94, L95. minor (1–4): „Der Schatten“: „Primär ein“ EP, probably fixed on fight/flight defences (L61); protects the system, especially Kiko, by aggressive defence or flight (L62); suppressed by Lex (L94).
- **`personas`** (minor, 1–4): the census's surfaces — `Personas` L22, L35, L37. minor (1–4): „Re-Mapping der „Personas“ auf ANP/EP-Rollen“ (L35 — quote around the nested quote); the complexity of the Personas explained by multiple ANPs and EPs (L22).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L66, L96, L97. minor (1–4): „Der Relationale Anteil“: „Wahrscheinlich ein“ ANP specialised in social interaction and attachment (L70); maintaining social connections (L71); dysfunctional in an environment with EP triggers such as the Grenzfeste (L97).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L84, L88, L112. minor (1–4): „Die Wächterin“: not a specific part in the TSDP sense but „das Potenzial für Integration und erhöhte Persönlichkeitsfunktion“ (L88); „Wächterin/Selene“ represents progress on the way to integration (L112).
- **`tsdp`** (central, 3–12 quotations): the census's surfaces — `TSDP` L11, L15, L33, L43, L52, L61, … (13 lines). central (4–8): the theory placed as the primary model (L15); probably tertiary dissociation with multiple ANPs and EPs (L22); each persona given a „TSDP-Rolle“ (L43, L52, L61, L70, L79, L88); the Pressure Points explained by TSDP dynamics — ANP phobia of EPs (L94), EP intrusions (L95), parts mismatched to the environment (L97).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Funktion` (near `aegisteilfunktionen`). an occurrence: `Funktion` a field label.
- `kaels-wohneinheit`: `Kaels` (near `kaelswohneinheit`), `Kaels` (near `kaelswohneinheit10`). an occurrence: `Kaels` the genitive, not the dwelling.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). an occurrence: the title.
- `multiplizitaet`: `Funktion` (near `funktionalemultiplizitat`). an occurrence: `Funktion` a field label.


**Record entries:** none.

**Not promoted:** Kai (no page exists), ANP, EP, Pressure Points and their codes, Paradoxon X, Juna/V, Die Wächterin as a label, Kernproblem, Systemstruktur, and the borrowed concepts.

**One reader**: every page above.

**Chapter readings**: none — the document names no chapter.
