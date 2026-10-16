# Brief — readings from document 500 (step 6)

1 document, one reader, one batch: `ingest-500`. Files go to `Plan/runs/ingest-500/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 500 | `roman-kapitel-1-erstellung-analyse` | 2025-12-28 | „the chapter-1 analysis“ (an unsigned German report by a writing assistant) | a preparatory analysis (sections 1.1–1.2), then a draft of „Kapitel 1: Instrumente der Ordnung“ in sequences with analytic inserts, then a closing analysis; a draft and its commentary, recorded, never applied — nothing in it is canon unless `kanon.md` lists it|

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (275 lines for `roman-kapitel-1-erstellung-ana`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A draft with commentary: write „the chapter-1 analysis drafts …“ for the narrative sequences and „the chapter-1 analysis explains/reads …“ for an analytic insert. The report addresses whoever commissioned it (L15) — never write that addressee. „DIS“ is Kael's condition in the novel. The Alter names Nox, Echo, Index and Limina are the draft's own. Borrowed physics concepts carrying a person's name are lens only: never write or quote them. Quote verbatim; cut before bold, escaped brackets, footnote digits and inner quotes. No gendered pronoun for Kael, Juna, AEGIS in our own prose; quotations stay verbatim.

## Pages — document 500, `roman-kapitel-1-erstellung-analyse`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L21, L23, L27, L59, L65, L75, … (13 lines). central (4–8): AEGIS emerging from the Nichts Rauschen (L21); defining itself by negation, its operative closure reading every unpredictability as existential threat (L23); a Zero-Trust-Architektur applied to consciousness too, filtering Kael's perception (L27); the Konstrukt-Stadt as an environment of low entropy that AEGIS keeps (L65 — check); AEGIS's filters making Juna appear distorted by perfection (L75).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L29, L203, L251. minor (1–4): other Alters such as Nox or Echo exerting passive influence (L29); the Alters in the closing analysis (L251).
- **`cache-kohaerenz`** (minor, 1–4): the census's surfaces — `Cache-Kohärenz` L189, L203. minor (1–4): the mirror scene as a failure of Cache-Kohärenz (L189); the analytic insert explaining it as a dissociative symptom (L203).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L246, L261. minor (1–4): Cerberus in the closing analysis (L246) and at L261 — check.
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L255. minor (1–4): the analysis naming DID at L255 — read it; the dissociative frame of the narrative perspective (L27).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L65. minor (1–4): the low-entropy environment (L65); entropy at the fall (L219 — check).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L21. minor (1–4): the „Genesis der Existenz“ as no big bang of matter but an information-theoretic act of resistance against the Nichts Rauschen (L21).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L241, L243, L270. minor (1–4): the closing analysis on the Guardians and their roles (L241, L243 — check each line); Mnemosyne, Kairos and Cerberus as Guardians with their functions (L245–L247).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L33, L73, L75, L83, L93, L99, … (11 lines). central (4–8): Juna appearing as an image on an interface (L73–L75): „die Partnerin“, distorted by perfection through AEGIS's filters (L75); the status query „Statusbericht, Kael“ (L77); the glitch read as a breakthrough of an outer level (L107 — check); the pulsing light at the end (L261 — check).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L23, L27, L29, L33, L39, … (40 lines). central (4–8): at the waking in Chapter 1 Kael is a „System“, acting as Host or ANP (L27); dissociative symptoms and passive influence by other Alters to be shown first as „Systemfehler“ or „Glitches“ (L29); the drafted waking as a brutal switching-on of peripherals (L39); the mirror scene, where the Cache-Kohärenz fails (L189); the fall through the Risse at the chapter's end (L219).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L153, L205, L247. minor (1–4): the Ranke or growth in the city's order (L153 — check that Kairos is named there); the voice (L205 — check); Kairos in the closing analysis (L247).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: an occurrence — the title and the project name (L15).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L23, L33, L109, L119, L153, L175, … (9 lines). minor (1–4): Kael waking in the Konstrukt-Stadt, Kernwelt 1 (L23); the city's sensory detail (L33); the city in the draft (L119) and the analysis of its order (L153).
- **`logos`** (central, 3–12 quotations): the census's surfaces — `LogOS` L23, L83, L85, L107, L151, L165, … (10 lines). central (4–8): LogOS named as the guardian of logic and architect of the crystalline city (L85); the city read as the character LogOS (L151); its rules no longer applying in the Grau (L251 — check).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L109, L245. minor (1–4): the draft's Mnemosyne (L109) and its role in the closing analysis (L245).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L260. minor (1–4): Multiplizität at L260 — read it.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L19, L21. minor (1–4): the Post-Genesis state, the Nichts Rauschen, as the state AEGIS emerged from (L19–L21): not a passive void (L21).
- **`partnerin`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Partnerin` alone on L75. minor (1–4): „Dies war Juna, die Partnerin“ (L75).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L245. minor (1–4): the Resonanz-Landschaft in the closing analysis (L245).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L219, L263; `Glitch` L29, L107, L163, L238. minor (1–4): the symptoms shown as „Glitches“ (L29); the glitch in the draft (L107, L163); the fall through the Risse (L219); the Risse at the end (L263).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L89. minor (1–4): the glitch as an ontological failure of the Simulation (L89).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Zero-Trust-Architektur` (near `zerotrust`). read on aegis (above): the Zero-Trust-Architektur applied to consciousness (L27).
- `entropie`: `Niedrigen Entropie` (near `entropie`), `Niedrige Entropie` (near `entropie`), `Hohe Entropie` (near `entropie`). read on entropie (above).
- `entropie-resonanz`: `Resonanz` (near `entropieresonanz`), `Resonanz` (near `entropieresonanzentropieresonanzprotokolleerp`), `Resonanz` (near `entropieresonanzprotokolle`). an occurrence: `Resonanz` in the Resonanz-Landschaft, read there.
- `genesis`: `Post-Genesis` (near `genesis`), `Genesis der Existenz` (near `genesis`). read on genesis (above): `Post-Genesis` is section 1.1's heading.
- `kern-welten`: `Kernwelt 1` (near `kernwelt`), `Kernwelt 4` (near `kernwelt`). an occurrence: `Kernwelt 1` names the Konstrukt-Stadt, read there; `Kernwelt 4` a mention in the analysis.
- `kohaerenz`: `Kohärenz-Protokoll` (near `koharenz`). an occurrence: the project name.
- `personas`: `Depersonalisation` (near `persona`). an occurrence: `Depersonalisation` is a symptom, not a persona.
- `residual-echos`: `Echo` (near `residualechos`). an occurrence: `Echo` is one of the draft's Alters.


**Record entries:** none.

**Chapter readings** (batch `ingest-500-kap`, `Plan/runs/ingest-500-kap/readings/kap-01--roman-kapitel-1-erstellung-analyse.md`, formatted as the files in `Plan/runs/ingest-466-kap/readings/`): **kap-01** „Instrumente der Ordnung“ (L31) — the draft's sequences (Initialisierung L35, Protokoll der Interaktion L69, and those after) in two to four sentences: the waking in sensory deprivation, Juna's status query on the interface, the glitch, the mirror scene, the fall through the Risse; attributed to the chapter-1 analysis as a draft, never canon.

**Not promoted:** the Alter names Nox, Echo, Index and Limina, Instrumente der Ordnung, Grau, Ranke, the dissociative symptom terms, and the borrowed physics concepts (several carry a person's name).

**One reader**: every page above and the kap-01 reading.
