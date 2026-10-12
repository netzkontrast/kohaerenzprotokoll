# Brief — readings from document 387 (step 6)

1 document, one reader, one batch: `ingest-388`. Files go to `Plan/runs/ingest-388/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 387 | `roman-kapitel-1-generierungsprozess` | 2025-11-25 | „der Exekutionsbericht“ (an unsigned German „Operationaler Bericht zur Narrativen Exekution“) | holds three prose sections of a Kapitel 1 draft (L86–L196, L234–L402, L444–L540), each followed by an „Analyse-Schnittstelle“ reading the prose in physics and psychology terms; it calls itself a „technische und ontologische Validierung“ and judges Phase I „erfolgreich“ — recorded, not applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (604 lines for `roman-kapitel-1-generierungspr`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report with a chapter draft inside it: write „the Exekutionsbericht's draft of Kapitel 1 has …“ for the prose and „the report reads …“ for the analysis sections; the prose is a draft, not the chapter as approved, and the analysis is the report's interpretation. Quote the German as written; cut before glued footnote digits, escapes and LaTeX. No gendered pronoun for Kael or the parts — use the names (quotations stay verbatim). Name no real researcher the report cites.

## Pages — document 387, `roman-kapitel-1-generierungsprozess`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L66, L208, L354, L356, L414, L552, … (7 lines). minor (1–3): in the analysis „Das System AEGIS/KW1 wendet Energie auf“ to remove disorder, sensory deprivation as negentropy (L208); love bursting „die künstliche Kohärenz von AEGIS“ (L552); in the draft's prose the colleague says „AEGIS sorgt für uns“ (L354).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L24. not read: an occurrence (see below).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L134, L142, L150, L160, L168, L180, … (9 lines). minor (1–3): in the draft's prose „Juna war nicht da. Ihr Protokoll war beendet.“ (L452); the closing table places Z-Fighting at „Junas Augen / Transit-Spiegelbild“ (L589).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L22, L34, L54, L58, L66, L92, … (54 lines). central (3–6): in the draft's prose Kael as „Architekt. Klasse 4.“ (L124) and „Ich bin System Kael. Ich funktioniere.“ (L394); in the analysis the ANP (Architekt Kael) as what remains on the Brane, „funktional, aber hohl“ (L58), the protagonist as an autopoietic system (L22); the voice „Finde die Naht, Kael.“ (L510).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: an occurrence (see below).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L56, L78. minor (1–3): „Die Simulation der Konstrukt-Stadt (KW1)“ as a world of Technischer Natürlichkeit held stable only by extreme fine-tuning (L56); the setting line „Konstrukt-Stadt (KW1), Sektor Gamma“ (L78).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L550, L552. minor (1–3): in the analysis „Moros (Exilant der Leere/Trauer)“, breaking through with the memory of Silas (L552); the prose itself does not name Moros.
- **`negentropie`** (minor, 1–4): the census's surfaces — `Negentropie` L66, L206, L208, L414. minor (1–3): „Sensorische Deprivation als Negentropie“: the white, odourless, dustless setting as a depiction of negentropy (L206, L208); the system creating a zone of negative entropy (L66).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L372, L374, L420, L422. minor (1–3): in the prose Nyx arriving unannounced, „Das war nicht er. Das war Nyx.“ and „Wer war Nyx?“ (L372, L374); in the analysis „Nyx (der Wut-Anteil, Fight-Response) bricht durch die Barriere“ (L422).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitch` alone on L56. minor (1–3): every Riss in the facade, every Glitch, as proof of the simulation's failure (L56); the anomaly in the code as a „Riss“ in the Brane (L414); the voice „Finde den Riss. Und reiß ihn auf.“ (L514).
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L466, L552. minor (1–3): in the prose the name Silas (L466) and „Der Name riss ein Loch in seinen Brustkorb.“ (L468); in the analysis the intrusion of the memory of Silas, love and grief, as the breakthrough of Moros (L552).
- **`tsdp`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `TSDP` alone on L58. minor (1–3): TSDP as the psychological framework, the ANP as what remains on the Brane (L58).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L56. minor (1–3): the Konstrukt-Stadt as a „Simulation“ (L56).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). `System Kael` on kael; `Logos-Prime` (L106) a second name for the city, read on kern-welten, not the Guardian; `Glitch` compounds read on risse; `Gamma-7` the draft's place; `Brane` a borrowed term; `Kohärenz Protokoll` the title.
- `logos`: `Logos-Prime` (near `logos`). `System Kael` on kael; `Logos-Prime` (L106) a second name for the city, read on kern-welten, not the Guardian; `Glitch` compounds read on risse; `Gamma-7` the draft's place; `Brane` a borrowed term; `Kohärenz Protokoll` the title.
- `risse`: `Glitch-Horror` (near `glitch`), `Glitch-Metaphern` (near `glitch`), `Glitch-Mechaniken` (near `glitch`), `Asynchronen Glitch` (near `glitch`). `System Kael` on kael; `Logos-Prime` (L106) a second name for the city, read on kern-welten, not the Guardian; `Glitch` compounds read on risse; `Gamma-7` the draft's place; `Brane` a borrowed term; `Kohärenz Protokoll` the title.


**Pages beyond the draft:**
- `kern-welten` (minor, 1): KW1 as the Konstrukt-Stadt (L56, L78), named „Logos-Prime“ in the prose (L106).

**Record entries:** none.

**Pages not read:** `kohaerenz` (L13, the title), `entropie` (L24, the general sense) — occurrences.

**Not promoted:** Operationaler Bericht, Analyse-Schnittstelle, Stil-Vorgabe, Parataktische Geschwindigkeit, Gravitationsgradient and the phases, the glitch vocabulary (Z-Fighting, Texture Stretching, Vertex Explosion, Mesh Tearing), Gamma-7, Leckage der Seele; the borrowed concepts (Brane cosmology, the hierarchy problem, entropic gravity, Uncanny Valley, operational closure).

**One reader**: aegis, kael, juna, nyx, silas, moros, konstrukt-stadt, negentropie, risse, tsdp, ueberwelt, kern-welten.

**Chapter readings** (batch `ingest-388-kap`, file `Plan/runs/ingest-388-kap/readings/kap-01--roman-kapitel-1-generierungsprozess.md`):
- **`kap-01`**: the report's draft of Kapitel 1 in three sections — „Kapitel 1: Die Geometrie der Stille“ (L86), „Kapitel 1 (Fortsetzung): Das Gewicht der Daten“ (L234), „Kapitel 1 (Abschluss): Der Ereignishorizont“ (L444): Kael as Architekt Klasse 4 in the Konstrukt-Stadt (L78, L124), the colleague Jansen (L336), Nyx breaking through (L372), Juna absent (L452), the name Silas (L466, L468), the voice telling Kael to find the seam (L510, L514); the report reads the chapter's end as the passage from Phase I to Phase II (L548). A draft inside a report, not the chapter as approved.
