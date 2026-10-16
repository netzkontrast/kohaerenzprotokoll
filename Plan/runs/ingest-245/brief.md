# Brief — readings from document 245 (step 6)

1 document, one reader, one batch: `ingest-245`. Files go to `Plan/runs/ingest-245/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 245 | `roman-kohaerenz-protokoll` | 2025-04-17 | „the early prose draft“ (unsigned German prose) | a draft of the novel's opening: a Vorwort on the nothing, the Genesis passage „Genesis im Echo der Leere“ (an English system report of AEGIS's reboot with German narration), Kapitel 1 and Kapitel 2 in 40 Moments; a draft, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (588 lines for `roman-kohaerenz-protokoll`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Prose, several voices: AEGIS's English status report (write „the report in the draft …“), the narrator, the characters' speech, and one remark in another voice at L545. Say which. The bracketed names in Kapitel 1 — `(Praetor ?)`, `(Nox ?)`, `(Kairos ?)`, `(Cerberus ?)`, `(Silas ?)` — are the narrator's guesses at the source of an impulse in Kael, with the question mark: never more than guesses. Chapter pages are written by the session (`Plan/runs/ingest-245-kap/`).

## Pages — document 245, `roman-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L128, L240, L242, L244, L250, L272, … (12 lines). central (3–8): in the report, directive „PRESERVE SYSTEM EXISTENCE.“ (L236), risk to the world „acceptable secondary consequence“ (L232), its identity rule (L250); the narrator's „Ein Wächter im Auge des Nichts.“ (L284) and, after the reboot, „ein nicht-anthropomorpher Kontrollkern“ (L344); „AEGIS FUNCTIONALITY: NOMINAL.“ (L314).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `SIS` L192, L255, L280, L320. minor (1–4): in the report the Zero-Trust Execution Model engaged (L146), the Integrity Guardian Module and the Cognitive Firewall Module reporting (L156, L168), the Secure Isolation State for the core during the reboot (L255, L320); the narrator: the core „geschützt im SIS“ (L280) and every component verified by AEGIS' Zero-Trust-Modell (L300).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L401. minor (1–4): the narrator: Kael senses „die Präsenz verschiedener Alters“ (L401).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L377, L389. minor (1–4): the narrator's bracketed guess `(Cerberus ?)` at the source of an impulse in Kael (L389) — a guess, as an alter's name, not the Guardian; L377 is LogOS's surveillance, check the line before using it.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L272. minor (1–4): the narrator: the Risse as „Manifestationen digitaler Entropie“ (L272).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L114. not read: occurrence — `Genesis` at L114 is in the passage's heading; the passage is read on aegis and ueberwelt.
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L359, L365, L367, L381, L391. minor (1–4): the narrator's formal first exchange (L361); her line „Synchronisation mit LogOS erfolgt“ (L365); her image flickering (L367); L381, L391 if they add.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L355, L361, L363, L367, L369, L371, … (15 lines). central (3–8): waking as „reines Gewahrsein“ (L355); „Systeme nominal.“ (L363); the question „Systemfehler oder Ich-Fehler?“ (L371); the architect in him finding his purpose in the data flow (L375); the persistent anomaly (L379); several alters and „Finde die Naht.“ (L401, L405); Zerrissenheit (L413); in Kapitel 2 his feelings forming the place (L537) and the fork (L587).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L379, L407. minor (1–4): the narrator's bracketed guess `(Kairos ?)` at the source of an impulse in Kael (L379 or L407 — use the line the guess stands on) — a guess, as an alter's name, not the Guardian.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L373, L399, L409, L411, L513. minor (1–4): the Datenknotenpunkt Gamma-7 with the cold functionality of the rest of the Konstrukt-Stadt (L373); the city breaking apart, „sterbenden Resten von KW1“ (L409–L411).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L365, L369, L377. minor (1–4): Juna's „Synchronisation mit LogOS erfolgt“ (L365); the omnipresent surveillance by LogOS (L377); L369 if it names LogOS.
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L272, L375, L389, L395, L437. minor (1–4): the narrator sets „Risse“ in quotation marks as manifestations of digital entropy (L272); Kael scanning for further Risse (L389); the Risse in perception (L395); L437.
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L395, L397. minor (1–4): the narrator's bracketed guess `(Silas ?)` at the source of an impulse in Kael (L395 or L397 — use the line the guess stands on).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L270, L300. minor (1–4): the narrator: the reboot dissolving the Überwelt into „ein Meer aus unbestimmten Bits“ (L270); the Überwelt forming anew, sterile and pure, every component verified by Zero-Trust (L300).

- **`kaels-wohneinheit`** (minor, 1–2): the narrator: on the way back to his Wohneinheit, the mirroring wall (L393); alone in it, the silence charged with the day's echoes (L395).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `Anomalie` (near `mustererkennunganomaliedetektion`). occurrence: `Anomalie` is the anomaly in the data stream Kael finds (L379), read on kael.
- `did`: `Fragmentierung` (near `psychischefragmentierung`). occurrence: `Fragmentierung` in the narration, not the clinical term.
- `dkt`: `Kern` (near `dualkerneltheoriedkt`). occurrence: `Kern` is AEGIS's core (L280, L344), read on aegis.
- `entropie-resonanz`: `Resonanz` (near `entropieresonanz`), `Resonanz` (near `entropieresonanzentropieresonanzprotokolleerp`), `Resonanz` (near `entropieresonanzprotokolle`). occurrence: `Resonanz` is chapter 2's title and the place's answering, not the protocol.
- `genesis`: `Genesis im Echo der Leere` (near `genesis`). occurrence: the heading `Genesis im Echo der Leere`.
- `kaels-wohneinheit`: `Wohneinheit` (near `kaelswohneinheit`), `Wohneinheit` (near `kaelswohneinheit10`). reading: Kael alone „in seiner Wohneinheit“ (L393, L395) — read on kaels-wohneinheit.
- `kern-welten`: `Kern` (near `kernwelt`), `Kern` (near `kernwelten`). occurrence: `Kern` is AEGIS's core.
- `kohaerenz-kernel`: `Kern` (near `kohaerenzkernel`), `Kern` (near `koharenzkernel`), `Kern` (near `koharenzkernelk1`). occurrence: `Kern` is AEGIS's core.
- `kollaps-kernel`: `Kern` (near `kollapskernel`), `Kern` (near `kollapskernelk0`). occurrence: `Kern` is AEGIS's core.
- `mnemosyne-server-architektur`: `Architekt` (near `mnemosyneserverarchitektur`). occurrence: `Architekt` is Kael's role at the data node (L375).
- `nichts-rauschen`: `Nichts` (near `nichtsrauschen`). occurrence: `Nichts` is the Vorwort's nothing.
- `personas`: `Depersonalisation` (near `persona`). occurrence: Depersonalisation is a symptom, not the Personas.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` in „Echo der Leere“ and the echoes of the day.
- `resonanz-landschaft`: `Resonanz` (near `resonanzlandschaft`). occurrence: `Resonanz` is chapter 2's title; the place's answering is read on the chapter page.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: five bracketed guesses at voices in Kael — Praetor, Nox, Kairos, Cerberus, Silas — each with a question mark (Kapitel 1), and „die Präsenz verschiedener Alters“ (L401); KW1 once (L411) and KW2 once, in a remark (L545). No count is given.
- **`q4-waechter-four-bearers`**: the narrator calls AEGIS „Ein Wächter im Auge des Nichts.“ (L284).
- **`c9-konstrukt-stadt-scale`**: the Konstrukt-Stadt breaking apart into „sterbenden Resten von KW1“ (L409–L411).

**Not promoted:** the Vorwort's nothing, Absolute Entropy Event, RIC, DRI, Praetor and Nox (guesses only), Datenknotenpunkt Gamma-7, Naht, Zerrissenheit, the 40 Moments, Sog.

**One reader**: aegis, aegis-teilfunktionen, ueberwelt, entropie, risse, kael, juna, logos, konstrukt-stadt, kaels-wohneinheit, alters, kairos, cerberus, silas and the records q3, q4, c9. `genesis` is an occurrence.

**Chapter readings**: Kap 1 (L353–L413) and Kap 2 (L417–L587), by the session (`Plan/runs/ingest-245-kap/`).
