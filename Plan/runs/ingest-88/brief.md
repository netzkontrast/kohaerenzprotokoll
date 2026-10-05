# Brief — readings from document 88 (step 6)

1 document, one reader, one batch: `ingest-88`. Files go to `Plan/runs/ingest-88/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 88 | `kontext-outline` | 2025-05-03 | „the outline commission“ (titled `Kontext-Outline`) | a German-and-English briefing of 2025-05-03 for a commissioned outline: a core-concept paragraph (L10), a project context (L14–L16), a „Basis-Glossar (Zur Orientierung für den Autor)“ whose note says the glossary is a basis the commissioned author is to refine (L22–L24, L26–L58), then „Prolog + 39 Kapitel“ (L61–L505) — a prologue and Chapter 1–39 in three acts, each chapter with `Core Theme`, `Plot Summary`, `Kael Sys Focus`, `AEGIS Focus`, `Setting` and `+` notes; open points are written as question marks (`Nyx: … (?)`, `Selene-Potenzial?`); a plan and a brief, no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (505 lines for `kontext-outline`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A commission: write „the commission briefs …“, „the outline plans …“, never as what the novel is; the glossary is „zur Orientierung“ for an author, so each entry is the briefing's gloss, not a definition of the wiki's term. Keep its question marks and hedges (`(?)`, `?`, `potenziell`, `ggf.`) in the quotation. `read.py` drops digits glued to words (`KW1`, `Chapter 13`): quote around them, and quote the chapter's bracketed title without its number. A heading with its own inner „…“ cannot be quoted whole: quote the inner part. Chapter content goes on the chapter pages (a later batch): on a term page, at most one or two beats by chapter number.

## Pages — document 88, `kontext-outline`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L18, L26, L28, L48, L49, … (106 lines). central (4–6): the glossary entry (L26 — „entstanden aus Komponente 734“), the `Paradox (AEGIS)` entry (L51–L52, Fehlausgerichtete Kohärenz), and the `AEGIS Focus` lines across the acts; its end in Act 3 (Kap 33–35).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L40, L100, L101, L102, L104, L157, … (8 lines). minor (1–2): the glossary: Alex as „Beschützer-Anteil“ (L40) — record it; the wiki's pages decide nothing here.
- **`argus`** (central, 3–12 quotations): the census's surfaces — `Argus` L42, L190, L202, L226, L227, L238, … (11 lines). central (3–4): the glossary: „Meta-Beobachter/Analytiker“ among the ANPs (L42) and the chapters where Argus is active (L190, L202 — `Argus (Meta-Beobachter) aktiv?`).
- **`cerberus`** (central, 3–12 quotations): the census's surfaces — `Cerberus` L32, L48, L166, L167, L169, L170, … (15 lines). central (3): KW3 Guardian Cerberus (L32), Chapter 23, Chapter 31.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L71. minor (1–2): what the commission says of it — 1–3 quotations, with the glossary entry or the chapter it sits in.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L352, L494. minor (1–2): L352 and L494 — what the lines say of the external level.
- **`genesis`** (minor, 1–4): the census's surfaces — `Genesis` L63, L405. minor (1–2): what the commission says of it — 1–3 quotations, with the glossary entry or the chapter it sits in.
- **`grenzfeste`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Grenzfeste` alone on L164. minor (1–2): what the commission says of it — 1–3 quotations, with the glossary entry or the chapter it sits in.
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L33, L48, L94, L127, L138, L171, … (16 lines). central (3–5): the glossary entry (L34 on the KWs and their guardians; `Guardians`: LogOS, Mnemosyne, Cerberus, Kairos, Sophia), five names over four worlds.
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L11, L18, L49, L66, L70, L189, … (26 lines). central (3–5): `Juna/V` as „Externe Entität/Anomalie/Kontaktquelle“ (L49), the first contact (Chapter 19) and its deepening (Chapter 25).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L11, L18, L27, L34, L38, L52, … (110 lines). central (4–6): the glossary entries on Kael and the `Kael Sys Focus` lines — Host (Kael) as the original everyday part (L37), the integration arc across the acts.
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L33, L48, L259, L261, L262, L263. minor (1–2): KW4 `Kairos & Sophia` (L33) and Chapter 17.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L47, L123, L134, L168, L328. minor (1–2): what the commission says of it — 1–3 quotations, with the glossary entry or the chapter it sits in.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: the novel's title (L11) — occurrence (J9).
- **`komponente-734`** (minor, 1–4): the census's surfaces — `Komponente 734` L26. minor (1): AEGIS „entstanden aus Komponente 734“ (L26).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Konstrukt-Stadt` alone on L87. minor (1–2): what the commission says of it — 1–3 quotations, with the glossary entry or the chapter it sits in.
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L39, L79, L80, L89, L90, L91, … (20 lines). central (3–4): Lex as „Logischer/Analytischer Anteil“ (L39) and `Lex` in the `Kael Sys Focus` lines.
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L47, L134. minor (1–2): what the commission says of it — 1–3 quotations, with the glossary entry or the chapter it sits in.
- **`logos`** (central, 3–12 quotations): the census's surfaces — `LogOS` L30, L48, L89, L90, L92, L94, … (12 lines). central (3): KW1 Guardian LogOS (L30), Chapter 28 (`Die Logik brechen: Konfrontation mit LogOS`).
- **`mnemosyne`** (central, 3–12 quotations): the census's surfaces — `Mnemosyne` L31, L48, L123, L125, L126, L127, … (19 lines). central (3): KW2 Guardian Mnemosyne (L31), Chapter 16, Chapter 30.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L47, L123, L134. minor (1–2): what the commission says of it — 1–3 quotations, with the glossary entry or the chapter it sits in.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L364, L501. minor (2): `funktionale Multiplizität` L364 and L501.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L69. minor (1–2): what the commission says of it — 1–3 quotations, with the glossary entry or the chapter it sits in.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L43, L168, L328. minor (1–2): the glossary: „Aggressiver/kämpferischer Anteil (?)“ (L43), keeping the question mark.
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L18. minor (1): L18, if the line speaks of levels of reality; else occurrence, say why.
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Resonanz-Landschaft` alone on L120. minor (1–2): what the commission says of it — 1–3 quotations, with the glossary entry or the chapter it sits in.
- **`rhys`** (central, 3–12 quotations): the census's surfaces — `Rhys` L41, L111, L112, L113, L124, L178, … (12 lines). central (3–4): Rhys as „Fürsorger-/Vermittler-Anteil“ (L41) and in Chapter 4–6 (L111–L113, L124, L178).
- **`risse`** (minor, 1–4): the census's surfaces — `Glitches` L79, L189. minor (1): `Glitches` L79 and L189 — what the chapters plan, if the line says what they are.
- **`selene`** (central, 3–12 quotations): the census's surfaces — `Selene` L44, L67, L179, L305, L306, L360, … (12 lines). central (3–4): Selene as „Potenziell integrierter/koordinierender Anteil am Ende“ (L44), the latent `Echo` (potenzielle Selene, L67), Chapter 10 (`Selene-Potenzial?`).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L33, L48, L259, L261, L263. minor (1–2): KW4 `Kairos & Sophia` (L33).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L18, L52, L144. minor (1–2): what the commission says of it — 1–3 quotations, with the glossary entry or the chapter it sits in.
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L53, L69, L192, L215, L223, L226, … (23 lines). central (3–4): the glossary: „Die Meta-Ebene von AEGIS (Kontrollzentrum, Code-Ebene, nicht direkt erlebbar wie KWs)“ (L56) and Act 2's entry into it (Chapter 14).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence (J69): `Guardian` is not the Integrity Guardian.
- `goedel-gambit`: `Gödel` (near `godelgambit`). a reading on `goedel-gambit` only if the line names the Gödel-Gambit; `Gödel` alone among the philosophers (lens) is an occurrence, say which.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Fehlausgerichtete Kohärenz` (near `koharenz`), `Fehlausgerichteten Kohärenz` (near `koharenz`). occurrences: the title and `Fehlausgerichtete Kohärenz` is the Paradox entry's own label — read it on `aegis` (J9, J12).
- `residual-echos`: `Echo` (near `residualechos`). `Echo` alone is the briefing's word for the potential Selene (L67): occurrence on `residual-echos` unless a line names residual echoes.


**Record entries** (one file each; write one only where the commission speaks to the record's question):

- **`c6-guardians-count-and-pairing`** and **`q5-guardians-and-kern-welten`**: the guardian-to-world pairs, five guardians over four worlds (L30–L33, L50).
- **`q3-how-many-kern-welten-and-alters`**: four KWs; the ANP and EP lists (L37–L47), where Nyx is „(?)“.
- **`q7-what-734-names`**: „entstanden aus Komponente 734“ (L26).
- **`q8-aegis-after-the-vortex`**: what Chapter 33–35 plan for AEGIS.

**Split into two readers, one after the other:**
- Reader 1: aegis, kael, juna, guardians, ueberwelt, logos, mnemosyne, cerberus, kairos, sophia, komponente-734, externe-ebene, konstrukt-stadt, resonanz-landschaft, grenzfeste, genesis, emergenz, nichts-rauschen, realitaetsebenen, risse, goedel-gambit, kohaerenz and the five records.
- Reader 2: the alters' pages (lex, alex, argus, rhys, selene, nyx, kiko, lia, moros), multiplizitaet, tsdp.
