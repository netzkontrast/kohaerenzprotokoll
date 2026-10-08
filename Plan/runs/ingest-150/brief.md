# Brief — readings from document 150 (step 6)

1 document, one reader, one batch: `ingest-150`. Files go to `Plan/runs/ingest-150/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 150 | `digitale-uberwelt-konzept-und-gestaltung` | 2026-03-26 | „the Überwelt concept“ (titled `Ontologie der Kohärenz: Die Architektonische Konstruktion der Digitalen Überwelt`, L11) | a German world concept of 2026-03-26 for the Digitale Überwelt as AEGIS's operative reality: its ontology („Kohärenz statt Wahrheit“, BPoF), the protocols (SIS, RTSV, Zero-Trust Environment Mandate), five Guardians, Kael's TSDP coupled to the Risse, Juna as „das exilierte Ursprungs-Ich“, and a last third that prescribes the staging; it calls itself „einen präzisen Rahmen für eine Erzählung“ (L151) — recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (169 lines for `digitale-uberwelt-konzept-und-`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A world concept that describes and, from L118, prescribes: write „the Überwelt concept describes / prescribes …“; much rests on numbered references — where a line reports „die technische Dokumentation“, say so. German — quote as written; cut before inner straight quotes (it sets many words in them) and before reference digits glued to a word.

## Pages — document 150, `digitale-uberwelt-konzept-und-gestaltung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L13, L15, L17, L21, L25, L50, … (17 lines). central (2–4): the expansion „Autonomous Entropic Gatekeeper for Integrity Systems“ (L13); the Überwelt as the AEGIS-Protokoll's self-reference chain (L17); „Kohärenz statt Wahrheit“ (L17); Systemkohärenz φ(t) validated every millisecond (L25); „ein autistisches Schutzsystem“ (L100); blind to the psychological cause (L110); Juna its target (L141).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `SIS` L45, L66. minor (1–2): SIS, „Systemische Isolation“ (L45) and „Systemic Isolation Shield (SIS)“ under Cerberus (L66); the „Zero-Trust Environment Mandate“ (L78).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L100. minor (1–2): the coupling of the Überwelt to Kael's fragmented psyche (L100); parts sending opposing commands cause the Risse (L104).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L64, L66, L86. minor (1–2): „Cerberus fungiert als das Immunsystem der Überwelt“ (L66); the Entropie-Jäger and the SIS (L66).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L13. minor (1–2): AEGIS as gatekeeper of entropy in the Überwelt's framing (L13); Cerberus's Entropie-Jäger (L66).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L52, L54, L74, L86, L126. central (2–4): „Die Guardians sind keine Avatare, sondern spezialisierte Subsysteme“ and „kein Ich-Bewusstsein im menschlichen Sinne“ (L54); five sections (L56–L74); Encrypted Intent Channels between them (L86); no direct address to AEGIS (L94).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L139, L141, L143. central (2–4): „Das größte Risiko für die Stabilität der Überwelt und das Ziel von AEGIS ist die Entität“ (L141) — cut before the quotes; „Juna repräsentiert das exilierte Ursprungs-Ich“ (L141), entangled with Kael by ER=EPR (L141).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L100, L104, L126, L141, L143. minor (1–2): „der unter einer tertiären strukturellen Dissoziation der Persönlichkeit (TSDP) leidet“ (L100); the Überwelt coupled to his psyche (L100).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L68, L70. minor (1–2): „Kairos repräsentiert das adaptive Element innerhalb der rigiden AEGIS-Struktur“ (L70).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L107. minor (1–2): when Kiko is triggered, „stottert die lokale Zeit“ (L107).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. minor (1–2): „Kohärenz statt Wahrheit“ (L17); the Systemkohärenz φ(t) that quantifies stability (L25).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L50. minor (1–2): „Kernwelt 1 (KW1), auch Logos-Prime oder Konstrukt-Stadt genannt“, the administrative centre of the Überwelt (L50) — cut around the digit if needed; surfaces cooler and smoother than glass (L50).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L56, L58, L66, L70, L86. minor (1–2): „LogOS ist die personifizierte (oder vielmehr konstruierte) Logik des Systems“ (L58).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L60, L62. minor (1–2): „Mnemosyne besetzt die komplexeste Nische innerhalb von AEGIS“ (L62).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L108. minor (1–2): Moros's glitch: the Überwelt's matter decays into grey fragments (L108).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L106. minor (1–2): when Nyx is triggered, violent physical anomalies (L106).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L102, L104, L110. central (2–4): Risse arise „Wenn verschiedene Persönlichkeitsanteile gleichzeitig gegensätzliche Befehle an das System senden“ (L104); three glitch types (L106–L108); AEGIS does not see the cause (L110).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L72, L74. minor (1–2): „Sophia ist die Instanz der ganzheitlichen Analyse und Mustersynthese“ (L74).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L98, L100. minor (1–2): Kael's „tertiären strukturellen Dissoziation der Persönlichkeit (TSDP)“ (L100).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L11, L13, L17, L21, L31, L35, … (27 lines). central (2–4): „der sogenannten Überwelt“ (L13); „Kohärenz statt Wahrheit“ and its difference from simulations (L17); existence conditional on contribution (L21); „unheimlicher Perfektion“ (L31); the staging: shadowless transparency (L120), sterile recycled air (L126) and the sense table, „Geruch nach Ozon und steriler Luft“ (L130–L136).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie`: `Entropie-Jäger` (near `entropie`). a reading — on entropie above.
- `kern-welten`: `Kernwelt 1` (near `kernwelt`). occurrence: Kernwelt 1 is the Konstrukt-Stadt, read there.
- `kohaerenz`: `Systemkohärenz` (near `koharenz`), `Kohärenz statt Wahrheit` (near `koharenz`), `Kohärenzprognose` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`). a reading — on kohaerenz above.
- `nichts-rauschen`: `Nichts-Rauschens` (near `nichtsrauschen`). occurrence: the genitive at L21 in passing; a reading only if the line says what it is.


**Record entries** (one file each):

- **`c16-kael-origin`**: „Juna repräsentiert das exilierte Ursprungs-Ich“, entangled with Kael (L141); dated 2026-03-26.
- **`c11-landauer-warmth-or-cold-ozone`**: the Überwelt's smell „sterile, recycelte Luft“ (L126) and „Geruch nach Ozon und steriler Luft“, cool untextured surfaces (L130–L136).
- **`c6-guardians-count-and-pairing`**: five Guardians LogOS, Mnemosyne, Cerberus, Kairos, Sophia (L56–L74), each a subsystem of AEGIS, no world pairing given except LogOS's KW1.
- **`q1-guardians-and-aegis`**: „keine Avatare, sondern spezialisierte Subsysteme“ (L54); no direct address to AEGIS (L94).

**Not promoted:** BPoF, RTSV, φ(t), Encrypted Intent Channels, Selbstverweisungskette, the glitch types, the sense table, Algorithmischer Horror, ER=EPR, the borrowed theory.

**Two readers**, disjoint: (1) aegis, ueberwelt, kohaerenz, entropie, aegis-teilfunktionen, juna, kael, tsdp, alters, risse, nyx, kiko, moros and the records c16, c11; (2) guardians, logos, mnemosyne, cerberus, kairos, sophia, konstrukt-stadt and the records c6, q1.
