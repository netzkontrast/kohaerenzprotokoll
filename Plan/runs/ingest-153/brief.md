# Brief — readings from document 153 (step 6)

1 document, one reader, one batch: `ingest-153`. Files go to `Plan/runs/ingest-153/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 153 | `kohaerenz-protokoll-narrativer-bauplan` | 2025-07-29 | „the Bauplan review“ (titled `Kohärenz Protokoll: Narrativer Bauplan`) | a German critical analysis of 2025-07-29 of the novel's narrative plan (the „Bauplan“): Kael and funktionale Multiplizität read against DIS literature, AEGIS as the „Entropic Gatekeeper“, the four Kernwelten, the three-part arc (Heldinnenreise, cyclical, Heldenreise), Das Fundament and polyphony; it calls itself „eine umfassende kritische Analyse“ (L22) and judges the plan „von außergewöhnlicher Robustheit“ (L236) — recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (338 lines for `kohaerenz-protokoll-narrativer`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A review that reports a plan and judges it: write „the Bauplan review reports the plan's … / judges …“, and keep the two apart — what the plan says is the plan's (as the review renders it), what the review argues is its own. Outside theory (DIS literature, Schmidt, Campbell, HAL 9000, gnosis) is the review's application. German — quote as written; cut before inner straight quotes and glued reference digits.

## Pages — document 153, `kohaerenz-protokoll-narrativer-bauplan`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L26, L30, L50, L54, L58, L60, … (27 lines); `Entropic Gatekeeper` L58, L64. central (2–4): „das logische und ontologische Gegenstück zu Kaels pluraler Existenz“ (L58); the plan's directive „Sein durch Abgrenzung/Nicht-Widerspruch“ (L62); as Entropic Gatekeeper against the Nichts Rauschen (L64); „ein klassisches systemisches Paradox“ (L76); the plan's narrative voice for AEGIS, objective and clinical (L60).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L126. minor (1–2): a protector part with Cerberus (L126).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L40, L42, L44, L48, L74, L172, … (9 lines). minor (1–2): the plan's alters or Innenpersonen in the review's clinical reading (L40); „die positive Absicht“ of all alters, even persecutors like Nox (L42) — cut before the quotes; the aim avoids „einer erzwungenen Fusion aller Alters“ (L44).
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache Kohärenz` L40. minor (1–2): „Cache Kohärenz“ as „eine treffende narrative Metapher für die dissoziative Amnesie“ (L40) — cut before the quotes.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L126. minor (1–2): here an inner protector part, „Beschützer-Anteilen wie Cerberus und Alex“ (L126) — not a Guardian; say so.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L158. minor (1–2): the table's philosophical analogy for part one, „Emergenz des pluralen Selbst“ (L158).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L122, L126, L159. minor (1–2): „Die Grenzfeste (KW3), eine Welt der Abwehr, des Schutzes und der Paranoia“, the bunker metaphor (L126).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L172. minor (1–2): as `Juna/V`: the first subtle echoes of the connection to Juna/V, outside AEGIS's control (L172); an external ally in part three (L194).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L26, L30, L34, L38, L40, L46, … (39 lines). central (2–4): „Kael repräsentiert eine Realität, die Widersprüche zulässt und integriert“ (L30); his symptoms as DIS criteria (L40); his initial state as Komponente 734 in KW1 (L170); Verstand and Herz at the climax of part one (L173).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L22, L86, L90, L171, L242. minor (1–2): „direkte Spiegelungen von Kaels psychologischen Zuständen“ (L90); the table's primary worlds per part (L158–L160).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L173. minor (1–2): Herz, represented by Kiko and Rhys (L173).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. minor (1–2): the plan's Inkohärenz; occurrence for the title (L13) — read only what the review argues about coherence, else not read.
- **`komponente-734`** (minor, 1–4): the census's surfaces — `Komponente 734` L40, L170. minor (1–2): Kael's initial state „als Komponente 734“ in the hyper-logical order of AEGIS (L170) — cut before the quotes.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L94, L98, L158, L170. minor (1–2): „Die hyper-logische und sterile Konstrukt-Stadt“ (L98).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L173, L331. minor (1–2): Verstand, represented by Lex (L173).
- **`logos`** (minor, 1–4): the census's surfaces — `Logos` L210, L216, L328, L329. occurrence: Das Fundament „als Logos“ (L210, L216) is the philosophical Logos, not LogOS.
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L135, L139, L160. minor (1–2): KW4 „ein Ort des Potenzials und der kreativen Synthese von Widersprüchen“ (L139); beside Das Fundament in the table (L160).
- **`multiplizitaet`** (central, 3–12 quotations): the census's surfaces — `Funktionale Multiplizität` L34; `Multiplizität` L22, L26, L34, L44, L50, L80, … (11 lines). central (2–4): the plan's aim of funktionale Multiplizität, „ein hochentwickeltes und therapeutisch fundiertes Konzept“ (L44), against forced fusion (L44); the therapeutic tension with AEGIS's demand for one identity (L50).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L64. minor (1–2): the chaos AEGIS prevents, „das“ Nichts Rauschen (L64) — cut before the quotes.
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L74, L108, L112, L158, L159. minor (1–2): KW2 „als Welt der Emotion, der Erinnerung und des Traumas“ (L112).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L173. minor (1–2): Herz, represented by Kiko and Rhys (L173).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitches` alone on L170. minor (1–2): the visual glitches and the visible „Riss“ of part one (L170) — cut before the quotes.
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L241. minor (1–2): here an inner part, an archetypal figure like Echo whose insight prepares Das Fundament (L241) — not a Guardian; say so.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `juna`: `Juna/V` (near `juna`). a reading — on juna above.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Inkohärenz` (near `koharenz`). occurrence: the title.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: Echo is an inner figure (L241), and the echoes of the connection (L172) are not the Residual-Echos.
- `risse`: `Riss` (near `risse`). a reading — on risse above.


**Record entries** (one file each):

- **`c6-guardians-count-and-pairing`**: Cerberus and Sophia named as Kael's inner parts — „Beschützer-Anteilen wie Cerberus und Alex“ (L126), „archetypischen Figuren wie Echo oder Sophia“ (L241); dated 2025-07-29.
- **`c14-aegis-first-person-chapter`**: the plan's narrative voice for AEGIS, „objektiv, klinisch, technisch und präzise“ (L60).
- **`q7-what-734-names`**: Kael's initial state „als Komponente 734“ (L170).

**Not promoted:** Das Fundament, dreifache Helix, zyklische Struktur, Innenpersonen, Kernprogrammierung, Heldinnenreise, Heldenreise, Polyphonie, HAL 9000, gnosis, Dialetheismus and the other borrowed theory.

**Two readers**, disjoint: (1) kael, multiplizitaet, alters, cache-kohaerenz, komponente-734, juna, lex, kiko, rhys, alex, risse and the record q7; (2) aegis, kohaerenz, nichts-rauschen, kern-welten, konstrukt-stadt, resonanz-landschaft, grenzfeste, moeglichkeits-garten, emergenz, cerberus, sophia and the records c6, c14.
