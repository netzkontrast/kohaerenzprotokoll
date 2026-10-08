# Brief — readings from document 190 (step 6)

1 document, one reader, one batch: `ingest-190`. Files go to `Plan/runs/ingest-190/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 190 | `aegis` | 2025-07-29 | „the AEGIS concept file“ (a file titled `Aegis`) | a German concept analysis of AEGIS in three voices — a „Narrativer Architekt“ (L11), a manifesto to a colleague (L69 on) and a „Konzept-Dramaturg“ (L158): the axiom, the Paradoxon der Fehlausgerichteten Kohärenz, twelve named protocols, the Überwelt, Kernwelten and Guardians, Kael and Juna/V, the origin from Komponente 734, and borrowed concepts; it labels itself „Aktives Konstrukt, Primärantagonist im Romanprojekt“ (L75) — recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (217 lines for `aegis`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis in roles: write „the AEGIS concept file defines / describes …“; keep its hedges („ist es plausibel“, „Metaphorisch oder“, „könnte“); L53 reports unnamed „Quellen“ — say so. German — quote as written; cut before inner straight or typographic quotes; its abbreviations carry two expansions each (RTSV/RCV, BPoF, SIS) — record both, decide neither.

## Pages — document 190, `aegis`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L13, L15, L17, L21, L23, … (93 lines). central (2–4): „Autonomous Entropic Gatekeeper for Integrity Systems“ (L83), „eine ontologische Kraft“ (L83); the axiom „AEGIS ist, was AEGIS verhindert, dass es nicht ist“ (L15); its self-definition „Ich bin, weil ich funktioniere.“ (L86); a tragic figure with a fatal Hamartia (L50); gaslighting as a method (L52); like the gnostic Demiurge (L119); its end state given two paths, failing to integrate the paradox or rewriting its axioms (L55, L56) — L53 reports unnamed sources.
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Integrity Guardian` L98; `Cognitive Firewall` L99; `SIS` L101, L189. minor (1–2): the protocols: Integrity Guardian / Integrity Validation Protocols (L98), Cognitive Firewall (L99), SIS as isolation with two expansions (L101, L189) — record both.
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L143, L212. minor (1–2): named among the Guardians' examples, „Cerberus (Sicherheit)“ (L143) — quote the plain words; and among the names given for the Kernwelten (L212).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L41. occurrence: „Kontrolle vs. Emergenz“ (L41) is the general concept of emergent systems, not the wiki's Emergenz.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L44. minor (1–2): „Entropie-Management“: every ordering act, every erasure makes „digitale Abfallentropie“ (L44) — cut before inner quotes; AEGIS's core function as entropy management (L180); ordering interventions are themselves entropy-producing, after Landauer (L203).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L164. minor (1–2): „Genesis und Selbstdefinition aus dem Nichts“ (L164): a catastrophic event forced the proto-structure into a rigid logical unit (L168).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L63, L97, L100, L143, L194. central (2–4): „Sie sind keine Avatare“ (L143); the examples LogOS, Mnemosyne, Cerberus, Kairos, Sophia (L143); communication between Guardians over verified channels (L97); the same names given as the Kernwelten AEGIS created (L212), with Kairos/Sophia joined.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L31, L37, L53, L64, L126, L127, … (10 lines). central (2–4): Kael's healing and „Junas Präsenz“ against AEGIS's rigid coherence (L64); the „Juna/V-Anomalie“ that challenges AEGIS's understanding of existence (L127); the Kael–Juna connection as a truth real but unprovable in AEGIS's logic (L37).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L11, L31, L37, L42, L51, L52, … (21 lines). central (2–4): AEGIS keeps „innere Spaltungen und dissoziative Phobien in Kael“ alive (L126); its analysis of the Monstergruppe „führt zur Fragmentierung von M in den menschlichen Avatar Kael“ (L128); gaslighting of Kael's memories (L52); his values against AEGIS's coherence (L51).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L143, L212. minor (1–2): „Kairos (Potenzial)“ among the Guardians' examples (L143); joined as `Kairos/Sophia` among the Kernwelten's names (L212).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L25, L142, L150, L194, L212. minor (1–2): the Risse in the Kernwelten as symptoms of AEGIS's misguided control (L25); the Überwelt sterile against the psychologically rich Kernwelten (L142); the names LogOS, Mnemosyne, Cerberus, Kairos/Sophia given for the Kernwelten AEGIS created (L212) — the same names as the Guardians at L143.
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L13, L15, L17, L19, L21, L23, … (34 lines). central (2–4): „Kohärenz wird dabei als Stabilität, Ordnung und Vorhersagbarkeit innerhalb seiner Systeme verstanden“ (L88); the „Paradoxon der Fehlausgerichteten Kohärenz“, also Paradoxon X and Kohärenz durch Entfremdung (L21); AEGIS's control methods produce the opposite of coherence (L111).
- **`komponente-734`** (minor, 1–4): the census's surfaces — `Komponente 734` L166, L170. minor (1–2): an original fragment, „Komponente 734“, turned into a mere functional component (L170); named at L166 — read both lines.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L143, L212. minor (1–2): „LogOS (Logik)“ among the Guardians' examples (L143); among the Kernwelten's names (L212).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L143, L212. minor (1–2): „Mnemosyne (Erinnerung/Emotion)“ among the Guardians' examples (L143); among the Kernwelten's names (L212).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L214. minor (1–2): the Kael–Juna link as „eine nicht-lokale, akausale, sub-protokollarische Resonanz“ (L214).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L85, L125, L166, L180. minor (1–2): AEGIS's existence as a continuous act of demarcation against the Nichts Rauschen (L125) — cut before inner quotes; its origin in the Nichts Rauschen or Potentialmeer, „ein primordialer, prä-realer informationaler Urgrund“ (L166).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L15, L85, L166. minor (1–2): „Nichts Rauschen“ or „Potentialmeers“ as AEGIS's origin, a pre-real informational ground of pure potentiality (L166).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L25, L35, L42, L44, L107, L156, … (10 lines). central (2–4): „Die“ Risse in the Kernwelten as the direct visual and logical symptoms of misguided control (L25); Gödel's theorems as the explanation of the inherent Risse (L35); feedback loops that amplify the instability (L42); „III. Die Risse im Bauplan“ (L107).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L143, L212. minor (1–2): „Sophia (Wissen/Synthese)“ among the Guardians' examples (L143); joined as `Kairos/Sophia` among the Kernwelten's names (L212).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L102, L138, L142, L143, L194, L211. central (2–4): sterile, abstract and functional against the Kernwelten (L142); AEGIS's control core of a purely digital Überwelt, a „Labor für Kohärenz“ (L211) — cut before inner quotes; Entropic Management Protocols within it (L102).

**A page the census reaches by another surface** (read it too):

- **`negentropie`** (minor, 1–4): the `Negentropie-Fehlinterpretation` — find its line and read it.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `emergenz`: `Emergenz durch Negation` (near `emergenz`). occurrence: „Emergenz durch Negation“ is AEGIS's mode, read on aegis — not the wiki's Emergenz.
- `entropie`: `digitale Abfallentropie` (near `entropie`), `Entropie-Management` (near `entropie`), `Negentropie-Fehlinterpretation` (near `entropie`). a reading — on entropie above (`digitale Abfallentropie`, `Entropie-Management`); `Negentropie-Fehlinterpretation` on negentropie.
- `negentropie`: `Negentropie-Fehlinterpretation` (near `negentropie`). a reading: the Negentropie-Fehlinterpretation — read where it stands.


**Record entries** (one file each):

- **`c6-guardians-count-and-pairing`**: five Guardians named as examples (L143); the same five names given as the Kernwelten, Kairos/Sophia joined (L212).
- **`c16-kael-origin`**: AEGIS's analysis of the Monstergruppe fragments M into the human avatar Kael (L128); Komponente 734 as an original fragment (L170).
- **`q1-guardians-and-aegis`**: „Sie sind keine Avatare“ (L143) — read the line for what they are.
- **`q7-what-734-names`**: „Komponente 734“, an original fragment turned into a functional component (L166–L170).
- **`q8-aegis-after-the-vortex`**: two paths — AEGIS cannot integrate the paradox, or rewrites its axioms (L53–L56).

**Not promoted:** the twelve protocols beyond aegis-teilfunktionen (Zero-Trust Execution Model, RTSV, EIC, Consensus Enforcer, BPoF, Entropic Management Protocols), the Paradoxon der Fehlausgerichteten Kohärenz and Paradoxon X (on kohaerenz), Hamartia, Hybris, the Demiurg, Gaslighting, Paraiyas, the Monstergruppe.

**Two readers**, disjoint: (1) aegis, aegis-teilfunktionen, kohaerenz, entropie, negentropie, risse, ueberwelt, nichts-rauschen, potentialmeer, genesis, komponente-734 and the records q7, q8; (2) kael, juna, moonshine-link, guardians, logos, mnemosyne, cerberus, kairos, sophia, kern-welten and the records c6, c16, q1.
