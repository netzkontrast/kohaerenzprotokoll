# Brief — readings from document 167 (step 6)

1 document, one reader, one batch: `ingest-167`. Files go to `Plan/runs/ingest-167/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 167 | `kohaerenz-protokoll-2` | 2025-04-17 | „the April 2025 concept“ (titled `Umfassendes Roman-Konzept (Arbeitstitel: AEGIS Protokoll / Seelen-Kohärenz)`) | a German novel concept, „Aktueller Stand: 17. April 2025“ (L13), in ten sections: logline, context, themes, characters, six levels, a three-part structure, plot sketches, metaphors, the opening chapter and open questions; it says it replaces the „Roman-Blueprint V5“ (L23) — a plan in its early names (Michael, Julia), much of it marked hypothetical or sketch |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (154 lines for `kohaerenz-protokoll-2`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An early plan: write „the April 2025 concept plans / sketches / leaves open …“. It names the protagonist `Michael` and the co-protagonist `Julia` — the pages are kael and juna; say the name the concept uses, never rename it. Its Kern-Alters are „Hypothetische“ (L53), Teil 2 and 3 „Skizze“ (L98, L111): keep the hedge. German — quote as written; cut before inner straight quotes; escaped arrows `-\>` stand in the text — quote around them.

## Pages — document 167, `kohaerenz-protokoll-2`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L17, L19, L24, L25, L31, … (23 lines); `Entropic Gatekeeper` L24, L67, L140. central (2–4): „Autonomous Entropic Gatekeeper for Integrity Systems“, the non-anthropomorphic core of the Überwelt, „Ich bin, weil ich funktioniere“ — cut before the inner quotes (L67); the AEGIS-Protokoll as the Überwelt's principle, the Entropic Gatekeeper (L24); the opening chapter from AEGIS's perspective initiating a „universal reboot“ (L139, L140) — the expansion is C1's, add a reading only.
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Zero-Trust` L43, L67. minor (1–2): Zero-Trust as AEGIS's systemic isolation (L43); L67 — read the line.
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L37, L53, L129, L131, L148. minor (1–2): „Hypothetische Kern-Alters“, four examples tied to worlds — Architekt, Kind/Echo, Wächter, Funke (L53–L61); integration vs. Funktionale Multiplizität (L37).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L66, L77. minor (1–2): a Guardian of security (L66); the Grenzfeste is Cerberus's world (L77).
- **`did`** (central, 3–12 quotations): the census's surfaces — `DID` L17, L19, L24, L30, L37, L49, … (11 lines). central (2–4): Michael „an einer Dissoziativen Identitätsstörung (DID) leidet“ (L17); the core concept explores DID, trauma and healing (L19); triggered by a trauma still to be defined (L49, L145); a respectful portrayal (L30).
- **`entropie`** (central, 3–12 quotations): the census's surfaces — `Entropie` L23, L31, L40, L65, L66, L67, … (16 lines). central (2–4): AEGIS's „entropie-fixierten System“ (L19); order vs. chaos, digital and psychic entropy (L40); each world's Entropie (L71, L75–L78); Julia read by the system as „Entropie-Quelle“ (L65); the basic principle AEGIS fights (L135).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L25, L65, L83, L122. minor (1–2): „Eine (noch) nicht näher definierte Realitätsebene außerhalb des AEGIS-Systems“, inaccessible to AEGIS and Guardians, Julia's source (L83); one of six levels (L25); open (L146).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L59, L77. minor (1–2): „Grenzfeste (Cerberus)“: protective parts, paranoia, Bunker (L77); the Wächter alter (L59).
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L17, L19, L23, L42, L45, L65, … (14 lines). central (2–4): „Die Guardians (LogOS, Mnemosyne, Cerberus, Kairos, Sophia)“: non-anthropomorphic constructs in the Überwelt under the AEGIS-Protokoll (L66); they misguide Michael (L17); they contact him in Teil 2 with flawed tools (L92, L103–L106); they insist on the info paradigm (L119).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Julia` L17, L24, L25, L41, L42, L43, … (20 lines). central (2–4): `Julia`, „Co-Protagonistin“, seemingly of the Externe Ebene (L65); her connection to Michael invisible to AEGIS and the Guardians — cut before the inner quotes (L65); „Julia/Externe Ebene ist der Schlüssel, unsichtbar für AEGIS“ (L122); the concept names her Julia — say so.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Michael` L17, L24, L25, L31, L33, L42, … (23 lines). central (2–4): `Michael`, „Protagonist“ with DID (L17, L49), trapped unknowingly in a layered simulation (L17); the four worlds his psyche (L25, L71); Teil 2's mission (L92, L106); his DID's origin open (L145); the concept names him Michael — say so.
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L66, L78. minor (1–2): a Guardian of potential (L66); the Möglichkeits-Garten shared „(Kairos/Sophia)“ (L78).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kern-Welten` L23, L25, L71. central (2–4): „Die 4 Kern-Welten (Simuliert, Michaels Psyche)“, each watched by its Guardians (L71); the four named (L75–L78); six levels (L25).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L67. occurrence: AEGIS's task of „Systemintegrität und Kohärenz“ (L67) — the word, on aegis; no reading of Kohärenz.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L57, L75. minor (1–2): „Konstrukt-Stadt (LogOS)“, one of the four worlds: ratio, rules, rigid control (L75); the Architekt alter (L57).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L66, L75. minor (1–2): a Guardian of logic (L66); the Konstrukt-Stadt is LogOS's (L75).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L66, L76. minor (1–2): a Guardian of emotion/memory (L66); the Resonanz-Landschaft is Mnemosyne's (L76).
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L60, L78. minor (1–2): „Möglichkeits-Garten (Kairos/Sophia)“, one of the four worlds: potential, creativity, chaos (L78); the Funke alter (L60).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L37, L128. minor (1–2): „Integration vs. Funktionale Multiplizität“ (L37); shards to mosaic (L128).
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L107. minor (1–2): Michael's first tries with the tools „im Nexus“ (L107) — named once, unexplained.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebenen` alone on L33. minor (1–2): the narrative tension of „den verschiedenen Realitätsebenen“ (L33); the six levels (L25, L69).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L58, L76. minor (1–2): „Resonanz-Landschaft (Mnemosyne)“: emotions, memories, trauma, the deepest link to Julia (L76); the Kind/Echo alter (L58).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L82, L91, L93, L104, L118, L133. minor (1–2): rising Risse and Guardian interference in Teil 1 (L91); escalating in Teil 3 (L93, L118); a metaphor of system instability (L133).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L66, L78, L103. minor (1–2): a Guardian of knowledge (L66); shares the Möglichkeits-Garten with Kairos (L78); speaks for the Guardians in Teil 2 (L103).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L17, L23, L24, L25, L66, L67, … (10 lines). central (2–4): „Die Überwelt (Digital, AEGIS/Guardian-Domäne)“, purely informational, ruled by the AEGIS-Protokoll, permanent struggle with entropy (L82); one of six levels (L25); Michael in the decaying Überwelt (L102).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `Anomalie` (near `mustererkennunganomaliedetektion`). occurrence: `Anomalie` is how the system reads Julia (L65), on juna.
- `garten-der-stillen-praesenz`: `Garten` (near `gartenderstillenpraesenz`), `Garten` (near `gartenderstillenprasenz`). occurrence: `Garten` is the metaphor of the psyche (L130), not that garden.
- `kohaerenz`: `Seelen-Kohärenz` (near `koharenz`), `Kohärenz-Modulator` (near `koharenz`). occurrence: the working title and the tool's name (L11, L105).
- `mnemosyne-server-architektur`: `Der Architekt` (near `mnemosyneserverarchitektur`). occurrence: `Der Architekt` is a hypothetical alter (L57).
- `mosaik-herz`: `Mosaik` (near `mosaikherz`). occurrence: `Mosaik` is the metaphor of shards to mosaic (L128), on multiplizitaet.
- `nichts-rauschen`: `Rauschen` (near `nichtsrauschen`). occurrence: `Rauschen` is how the system reads Julia (L65).


**Record entries** (one file each):

- **`c4-guardians-and-aegis`**: Julia's connection invisible and unintelligible to AEGIS and the Guardians (L65); the Externe Ebene inaccessible to them (L83, L122).
- **`c5-garten-scale`**: the Möglichkeits-Garten is one of the four worlds (L78).
- **`c6-guardians-count-and-pairing`**: five Guardians (L66), four worlds, Kairos and Sophia sharing the Garten (L75–L78).
- **`c9-konstrukt-stadt-scale`**: the Konstrukt-Stadt is one of the four worlds, LogOS's (L75).
- **`q1-guardians-and-aegis`**: constructs in the Überwelt „die dem AEGIS-Protokoll unterstehen“ (L66).
- **`q3-how-many-kern-welten-and-alters`**: four Kern-Welten (L71); hypothetical Kern-Alters, four examples, „(Weitere möglich/nötig)“ (L53–L61).
- **`q5-guardians-and-kern-welten`**: one Guardian per world, two for the Garten (L75–L78).
- **`q6-nexus-ueberraum-ueberwelt`**: the Nexus named once beside the worlds (L107), the Überwelt as the digital level (L82).

**Not promoted:** Seelen-Kohärenz, AEGIS Protokoll (working titles), the four tools (Kohärenz-Modulator, Intent-Kanal-Interface, Entropie-Scanner, Sicherheits-Protokoll-Override), the hypothetical alters' labels, Bunker, the metaphors, Roman-Blueprint V5, Together We Confide (A1), Heldinnenreise/Heldenreise, Meta-Intro.

**Two readers**, disjoint: (1) kael, juna, did, alters, multiplizitaet, externe-ebene, realitaetsebenen, nexus, risse, entropie and the records c4, q3, q6; (2) aegis, aegis-teilfunktionen, guardians, logos, mnemosyne, cerberus, kairos, sophia, kern-welten, konstrukt-stadt, resonanz-landschaft, grenzfeste, moeglichkeits-garten, ueberwelt and the records c5, c6, c9, q1, q5.
