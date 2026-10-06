# Brief — readings from document 110 (step 6)

1 document, one reader, one batch: `ingest-110`. Files go to `Plan/runs/ingest-110/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 110 | `erlebniswelten-der-anteile-uberlagerung-mit-kernwelten` | 2025-04-29 | „the Erlebniswelten concept“ (titled `Erlebniswelten der Anteile (System Kael) & Überlagerung mit den Kernwelten`) | a German concept of 2025-04-29 that pairs the four Kernwelten with group-theoretical names (KW1 Co₁ … KW4 Ly, L15–L20), describes the inner world of each of eleven Anteile with its place in the three albums, and how each meets each Kernwelt (L22–L154), closing with five narrative functions (L156–L166); it hedges (`könnte`, `vielleicht`) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (167 lines for `erlebniswelten-der-anteile-ube`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A concept: write „the Erlebniswelten concept pairs … with …“, „describes …“; keep its hedges and its own mark „(Interpretation im Romankontext)“ on the KW2 and KW3 pairings (L18, L19). The album titles („Together We Confide“, „Moment der Klarheit“) are the document's frame: name them as such. Kael is male.

## Pages — document 110, `erlebniswelten-der-anteile-uberlagerung-mit-kernwelten`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L50. minor (1): only as Nyx's „äußere Kontrolle (AEGIS)“ (L50) — a reading only if it says more; else occurrence.
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L33, L108. minor (1–2): its Erlebniswelt (Sekundärer ANP - Protektor, L108) and its four overlays KW1–KW4, quote one or two (L108–L118).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L144. minor (1–2): its Erlebniswelt (Entstehender ANP/EP-Mix - Beobachter/Kritiker, L144) and its four overlays KW1–KW4, quote one or two (L144–L154).
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L26. minor (1): Kael's core problem, „das \"Cache Kohärenz\"-Chaos“ breaking into his Erlebniswelt (L26) — quote around the inner quote marks.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L19. minor (1): KW3's guardian (L19).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L20. minor (1): KW4's focus on „Potentialität, Emergenz“ (L20) — read only if more than a cell; else occurrence.
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L19. minor (1): KW3 = B (Baby-Monstergruppe), chaos, defence, boundaries, paranoia (L19).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L84. minor (1–2): its Erlebniswelt (EP - Sexualisiert/Kampf/Kontrolle, L84) and its four overlays KW1–KW4, quote one or two (L84–L94).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L11, L13, L24, L160, L166. central (2): „Kael (Primärer ANP, Host)“ (L24), a grey management level, the pressure to hold everything together (L26); the four overlays (L31–L34).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L20. minor (1): KW4's guardians `Kairos/Sophia` (L20).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L11, L13, L15, L27, L39, L51, … (15 lines). central (2–3): the „Zuordnung der Kernwelten zu Gruppentheoretischen Entsprechungen“ (L15): KW1 Konstrukt-Stadt (LogOS) = Co₁, KW2 Resonanz-Landschaft (Mnemosyne) = McL, KW3 Grenzfeste (Cerberus) = B, KW4 Möglichkeits-Garten (Kairos/Sophia) = Ly (L17–L20), the second and third marked „(Interpretation im Romankontext)“.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L60, L116. minor (1–2): its Erlebniswelt (EP - Kind, Flucht/Einfrieren, L60) and its four overlays KW1–KW4, quote one or two (L60–L70).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L26. not read: inside `Cache Kohärenz` and the title (L26, L11) — occurrence (J16).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L17. minor (1): KW1 = Co₁ (Conway-Gruppe 1), rigid order, structure, logic (L17).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L132, L160, L161. minor (1–2): its Erlebniswelt (Primärer ANP - Rationalist, L132) and its four overlays KW1–KW4, quote one or two (L132–L142).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L72, L116. minor (1–2): its Erlebniswelt (EP - Kind, Flucht/Bindungs-Ambivalenz, L72) and its four overlays KW1–KW4, quote one or two (L72–L82).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L17. minor (1): KW1's guardian (L17).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L18. minor (1): KW2's guardian (L18).
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L20. minor (1): KW4 = Ly (Lyons-Gruppe), potentiality, emergence, creativity (L20).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L96, L122. minor (1–2): its Erlebniswelt (EP - Kollaps/Freeze, L96) and its four overlays KW1–KW4, quote one or two (L96–L106).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L33, L48, L161. minor (1–2): its Erlebniswelt (EP - Kampf, L48) and its four overlays KW1–KW4, quote one or two (L48–L58).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L18. minor (1): KW2 = McL (McLaughlin-Gruppe), networks, emotional resonance, memory (L18).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L120. minor (1–2): its Erlebniswelt (Sekundärer ANP - Pflegender, L120) and its four overlays KW1–KW4, quote one or two (L120–L130).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L134. minor (1): Lex's fight against chaos „(KW2, KW4, Risse)“ (L134) — occurrence unless more; say which.
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L36. minor (1–2): its Erlebniswelt (Modifizierter ANP/Integrationspotenzial, L36) and its four overlays KW1–KW4, quote one or two (L36–L46).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L20, L46. minor (1): KW4's `Kairos/Sophia` (L20); Selene „könnte eine besondere Verbindung zu Sophia haben“ (L46).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `tsdp`: `TSDP-Rolle` (near `tsdp`). occurrence: `TSDP-Rolle` only in the introduction (L13), no reading of the theory.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: eleven Anteile with TSDP roles (L24–L144); the four Kernwelten numbered KW1–KW4 beside Co₁, McL, B, Ly (L17–L20) — the earliest read source to set the early names beside the numbers, two of the four marked an interpretation. Append dated 2025-04-29; it predates the author's two answers of 2026-10-05 and changes neither.
- **`q5-guardians-and-kern-welten`**: one guardian per world, KW4 held by `Kairos/Sophia` (L17–L20).
- **`c15-flight-riss-bearers`**: Kiko „Flucht/Einfrieren“ (L60) and Lia „Flucht/Bindungs-Ambivalenz“ (L72).

**Not promoted:** the three albums and their tracks (L13 and each Erlebniswelt) — the document's frame; Erlebniswelt; the five narrative functions (L160–L164).

**Split into two readers, one after the other:**
- Reader 1: kern-welten, konstrukt-stadt, resonanz-landschaft, grenzfeste, moeglichkeits-garten, logos, mnemosyne, cerberus, kairos, sophia, emergenz, kael, cache-kohaerenz, aegis, risse, and the three record entries.
- Reader 2: selene, nyx, kiko, lia, isabelle, moros, alex, rhys, lex, argus.
