# Brief — readings from document 129 (step 6)

1 document, one reader, one batch: `ingest-129`. Files go to `Plan/runs/ingest-129/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 129 | `lokalitaeten-konzept-fuer-roman-simulation` | 2025-04-18 | „the locations concept“ (titled `Umfassendes Lokalitäten-Konzept: Kohärenz Protokoll`, L11) | a German concept report of 2025-04-18 on the novel's places: worldbuilding principles with borrowed theories (I, L13–L175), „Die Sechs Realitätsebenen“ — four Kern-Welten, the Überwelt, the Externe Ebene (II, L177–L257) with a comparison table (L185–L189), seven key locations (III, L259–L338), implementation and three comparison works (IV), conclusions and 104 web references; proposals in the conditional, it calls itself „eine robuste Grundlage“ (L417) — recorded, not applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (535 lines for `lokalitaeten-konzept-fuer-roma`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A concept proposes: write „the locations concept assigns / describes …“; `[Context]` and `[Insight 1.x]` markers point to a brief not in the file — say the line marks itself so; its comparison works (Blade Runner, Silent Hill 2, Control) and theories (Prospect-Refuge, das Unheimliche) are borrowed. Alter names in quotes ('Index', 'Praetor', 'Nox', 'Limina', 'Eos', 'Echo', 'Flicker', 'Architekt') are its own, of 2025-04-18. Glued footnote digits are cut off quotations. L280 carries export damage in another script — do not quote it. Kael is male.

## Pages — document 129, `lokalitaeten-konzept-fuer-roman-simulation`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L21, L23, L28, L29, L35, L37, … (58 lines). central (2–4): the Überwelt as „die Domäne von AEGIS und den Guardians“ (L239); AEGIS's system logic with Zero-Trust and entropy regulation (L21); the AEGIS-Kern and Analyse-Hub (L244, L307); the worlds' aesthetics described „Post-Reboot“ (L185, L195).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Zero-Trust` L21, L91, L239, L242. minor (1–2): Zero-Trust: access in the Überwelt „durch Berechtigungen kontrolliert (Zero-Trust)“ (L242); L21.
- **`alters`** (central, 3–12 quotations): the census's surfaces — `Alters` L63, L135, L185, L195, L206, L213, … (14 lines). central (2–4): the table's column „Assoziierte(r) Guardian/Alters“ (L185) with names per world — KW1 Index, Architekt, (Praetor, Nox); KW2 Echo, Flicker, Silas, Oblivion; KW3 Limina, Praetor, Oblivion, (Nox); KW4 Eos, Index, Silas, (Nox) (L186–L189); atmosphere filtered through the dominant alter (L135).
- **`cerberus`** (central, 3–12 quotations): the census's surfaces — `Cerberus` L151, L188, L215, L217, L220, L222, … (15 lines). central (2–4): KW3 „Grenzfeste (Cerberus)“ (L215); Cerberus' Kernbunker (L285); Cerberus' Firewall-Nexus in the Überwelt (L244).
- **`did`** (minor, 1–4): the census's surfaces — `DID` L135, L173, L359, L383. minor (1–2): environmental storytelling revealing his DID (L173); „Illustration der DID“ (L359).
- **`entropie`** (central, 3–12 quotations): the census's surfaces — `Entropie` L21, L37, L91, L93, L97, L103, … (34 lines). central (2–4): each world's `Manifestation von Rissen/Entropie` field (L201, L212, L223, L234, L245) — cut before the straight quotes; the Überwelt manages entropy (L242).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L191, L248, L329, L360, L421. minor (1–2): „Eine Realität außerhalb der Kontrolle von AEGIS, verbunden mit der Figur Juna“ (L250); not a world in the table (L191); Junas Zufluchtsort (L329).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L57, L67, L188, L215, L287. minor (1–2): KW3 (L188, L215): brutalist, defensive, claustrophobic (L218).
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L21, L23, L85, L237, L239, L240, … (13 lines). central (2–4): a Guardian per world in the table (L186–L189); Guardian-Hubs in the Überwelt (L244); „LogOS, Mnemosyne, Cerberus, Kairos, Sophia“ as avatars or presences (L246).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L202, L213, L224, L235, L246, L248, … (17 lines). central (2–4): the Externe Ebene „verbunden mit der Figur Juna“ (L250) as „Junas Ursprung oder Domäne“ (L257); Kael might later see it, „möglicherweise geführt von Juna“ (L257); Junas Zufluchtsort (L329).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L25, L28, L29, L31, L33, L37, … (65 lines). central (2–4): „Kaels Wohneinheit (KW1)“ as his starting point after the reboot (L263, L272); atmosphere filtered through his or the dominant alter's perception (L135); confronting repressed memories at the Trauma-Lokus (L283).
- **`kaels-wohneinheit`** (minor, 1–4): the census's surfaces — `Kaels Wohneinheit` L263. minor (1–2): „Der initiale 'Heimat'-Raum für Kael nach dem Reboot innerhalb der Konstrukt-Stadt“ (L265) — cut as findable; small, perfectly geometric (L266).
- **`kairos`** (central, 3–12 quotations): the census's surfaces — `Kairos` L151, L189, L226, L228, L231, L235, … (10 lines). central (2–4): KW4 „Möglichkeits-Garten (Kairos/Sophia)“ (L226); „Kairos und Sophia als leitende Präsenzen oder Schnittstellen“ (L235); Kairos/Sophias Orakel (L244).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kern-Welten` L19, L21, L23, L31, L37, L41, … (41 lines). central (2–4): „Die Sechs Realitätsebenen“ (L177): four Kern-Welten, KW1 Konstrukt-Stadt, KW2 Resonanz-Landschaft, KW3 Grenzfeste, KW4 Möglichkeits-Garten, each with a Guardian (L186–L189); reacting by their core concept (L151); uncanny as Kael's reflections and simulated constructs (L63).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title (J9).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L186, L193, L265. minor (1–2): KW1 (L186, L193), logic and order, „Post-Reboot“ hyper-geometric (L195–L196).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L151, L186, L193, L195, L198, L202, … (9 lines). minor (1–2): KW1's Guardian (L186, L193); a systemic presence (L202); LogOS' Logik-Engine (L244).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L151, L187, L204, L206, L209, L213, … (9 lines). minor (1–2): KW2's Guardian (L187, L204); a fleeting presence trying to catalogue (L213); Mnemosynes Archiv (L244).
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L189, L226, L298. minor (1–2): KW4 (L189, L226): potential, creativity, chaos (L228); the Nexus-Interface Garten (L296, L298).
- **`nexus`** (minor, 1–4): the census's surfaces — `Nexus` L231, L233, L244, L296. minor (1–2): „Die Nexus-Schnittstelle“ in KW4 (L233); the Nexus-Interface Garten (L296); Cerberus' Firewall-Nexus (L244) — say which sense each line has.
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L187, L188, L206, L217, L282, L283. minor (1–2): an alter of KW2 and KW3 (L187, L188, L206, L217); bound to the trauma (L283).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — `Realitätsebenen` L19, L21, L177, L179, L261, L417. minor (1–2): „Dieses Kapitel detailliert die sechs fundamentalen Realitätsebenen des Romans“ (L179); four Kern-Welten, the Überwelt, the Externe Ebene (L191).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L59, L187, L204, L276. minor (1–2): KW2 (L187, L204): emotion, memory, trauma, fluid and dreamlike (L206–L207).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L63, L69, L93, L107, L127, L147, … (28 lines). central (2–4): each world's typical Riss manifestation (L185–L189 last column) and its own field (L201, L212, L223, L234); the Risse as uncanny glitches revealing the artificiality (L63).
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L187, L189, L206, L228, L235, L283. minor (1–2): an alter of KW2 and KW4 (L187, L189, L206, L228); bound to the trauma (L283).
- **`sophia`** (central, 3–12 quotations): the census's surfaces — `Sophia` L151, L189, L226, L228, L231, L235, … (10 lines). central (2–4): the same lines: KW4 shared with Kairos (L226, L235), the Orakel (L244).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L19, L21, L23, L27, L45, L73, … (32 lines). central (2–4): „E. Die Überwelt (AEGIS/Guardians)“ (L237): „Die Kontrollschicht des Systems“, purely digital (L239); architecture as data visualisation (L240); the AEGIS Analyse-Hub (L307).
- **`vergessener-schrein`** (minor, 1–4): the census's surfaces — `Trauma-Lokus` L274, L348, L361, L383. minor (1–2): the „Zentraler Trauma-Lokus (KW2)“ (L274, L276) — read only if the page's sense (a hidden trauma place) matches; else not read.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence (J9).
- `mnemosyne-server-architektur`: `Architekt` (near `mnemosyneserverarchitektur`). occurrence: `Architekt` is an alter name of KW1 (L186), not the page.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` is an alter name of KW2 (L187), not the page.


**Record entries** (one file each):

- **`c6-guardians-count-and-pairing`**: five Guardians on four worlds, Kairos/Sophia sharing KW4 (L186–L189, L226) — dated 2025-04-18.
- **`q5-guardians-and-kern-welten`**: the same pairing, each world's Guardian and alters in one table (L185–L189).
- **`c9-konstrukt-stadt-scale`**: „KW1: Konstrukt-Stadt“ (L186) — KW1 only.
- **`q3-how-many-kern-welten-and-alters`**: four Kern-Welten within six Realitätsebenen (L177–L191); the alter names per world (L186–L189).
- **`q6-nexus-ueberraum-ueberwelt`**: the Nexus as an interface place inside KW4 (L233, L296), the Überwelt as the control layer (L239).

**Not promoted:** the alter names Index, Architekt, Praetor, Nox, Echo, Flicker, Limina, Eos (on alters and Q3 only), Glitch-Zone, AEGIS Analyse-Hub, Cerberus' Kernbunker, Junas Zufluchtsort (on the pages of their worlds), Prospect-Refuge, das Unheimliche, Environmental Storytelling, Panopticon, the three comparison works.

**Split into two readers, at the same time on disjoint pages:**
- Reader 1: aegis, aegis-teilfunktionen, ueberwelt, guardians, logos, mnemosyne, cerberus, kairos, sophia, externe-ebene, juna, entropie, risse, nexus, and the entries c6, q5, q6.
- Reader 2: kael, kaels-wohneinheit, alters, oblivion, silas, did, kern-welten, konstrukt-stadt, resonanz-landschaft, grenzfeste, moeglichkeits-garten, realitaetsebenen, vergessener-schrein, and the entries c9, q3.
