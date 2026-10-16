# Brief — readings from document 353 (step 6)

1 document, one reader, one batch: `ingest-354`. Files go to `Plan/runs/ingest-354/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 353 | `heilung-der-verlust-von-superkraeften` | 2025-10-16 | „the Superkräfte dossier“ (a German memo-form strategy dossier, AN/BETREFF header, sender a persona) | argues that healing System Kael means losing the Anteile's trauma-born abilities, forecasts Lex's and Nyx's resistance in two chapter scenarios (Kapitel 30 and 33), and reverses the Kintsugi image; it appeals to „der unveränderlichen Lore des Projekts“ (L31), recorded, not applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (254 lines for `heilung-der-verlust-von-superk`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A strategy dossier: write „the Superkräfte dossier argues / forecasts …“; its scenarios are proposals for chapters, its appeal to the project's lore is its own claim. Never name or quote the memo's sender (L19). Say when a line reports borrowed theory (structural dissociation, hyperfocus, PTG critics).

## Pages — document 353, `heilung-der-verlust-von-superkraeften`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L31, L51, L53, L60, L70, L86, … (23 lines). central (3–6): the isolation of the Anteile enforced by AEGIS, milieu control (L53); the Kernwelten as its specialised training environments (L51); a worldview programmed by AEGIS (L107); the Kintsugi gold not neutral but AEGIS's, seams of artful servitude (L179).
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L31, L33, L115, L135, L141, L165, … (9 lines). minor (1–3): System Kael's aim of functional multiplicity, healing dissociative barriers (L31); true healing requiring the irretrievable loss of inhuman perfection (L33); the ultimate act of healing for System Kael (L183).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L51, L72; `Kernwelt` L51, L72, L123. minor (1–3): the Kernwelten functioning as highly specialised training environments (L51).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L74, L111, L142. minor (1–3): Kiko among the vulnerable child parts Nyx protects (L111); Kiko in the emotional division (L74) if the line says so.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L21. not read: an occurrence (see below).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L49, L53, L58, L70, L72, L74, … (17 lines). central (3–6): the abilities of Lex and Nyx as no magical gifts (L49); Lex's hyperfocus (L70); Lex as a primary ANP with an AEGIS-programmed worldview (L107); the resistance of Lex and Nyx not malice (L103); Scenario 1, Lex's empathic error, a cold calculation required (L135).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L111. minor (1–3): Lia among the vulnerable child parts Nyx protects (L111).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L31. minor (1–3): „funktionaler Multiplizität“ as System Kael's aim, the healing of dissociative barriers (L31).
- **`nyx`** (central, 3–12 quotations): the census's surfaces — `Nyx` L49, L53, L58, L70, L72, L74, … (16 lines). central (3–6): the abilities of Lex and Nyx (L49); Nyx as a primary EP embodying the fight defence (L111); protecting the vulnerable child parts (L111); the resistance not malice (L103); Scenario 2, Nyx's moment of hesitation (L139).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L74, L136. minor (1–3): empathy held by Rhys (L74); Lex's access to Rhys's empathic abilities (L136).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). `funktionaler Multiplizität` is read on multiplizitaet; `Kohärenz Protokoll` is the novel's title.
- `multiplizitaet`: `funktionaler Multiplizität` (near `multiplizitat`). `funktionaler Multiplizität` is read on multiplizitaet; `Kohärenz Protokoll` is the novel's title.


**Pages not read:** `kohaerenz` (L21 the title) — an occurrence.

**Record entries:** none.

**Not promoted:** the Superkräfte as a label, Milieukontrolle, the sabotage table, the reversed Kintsugi image, Wabi-Sabi; the borrowed concepts (structural dissociation, hyperfocus, flow, PTG and its critics).

**One reader**: aegis, kael, kern-welten, kiko, lex, lia, multiplizitaet, nyx, rhys — and the chapter readings below.

**Chapter readings** (batch `ingest-354-kap`, files `Plan/runs/ingest-354-kap/readings/kap-NN--heilung-der-verlust-von-superkraeften.md`):

- **`kap-30`**: the dossier's Scenario 1, „Lex' empathischer Fehler (Kapitel 30)“ (L133), the chapter of the „internen Belastungsprobe“ (L131): its situation, the failure and what it confirms (L133–L137). A proposal for the chapter, not the chapter.
- **`kap-33`**: Scenario 2, „Nyx' Moment des Zögerns (Kapitel 33)“ (L139), the chapter of the „Angst vor Re-Traumatisierung“ (L131): situation, failure, consequence (L139–L143). A proposal, not the chapter.
