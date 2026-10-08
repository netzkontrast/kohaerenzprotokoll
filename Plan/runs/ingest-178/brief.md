# Brief — readings from document 178 (step 6)

1 document, one reader, one batch: `ingest-178`. Files go to `Plan/runs/ingest-178/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 178 | `roman-outline-kohaerenz-protokoll-uberarbeitung` | 2025-05-03 | „the strategy report“ (titled `Strategiebericht zur Konzeptionellen Weiterentwicklung: Kohärenz Protokoll (P+39)`) | a German strategy report that justifies a revised outline (prologue plus 39 chapters) by borrowed theory — TSDP and its phobias, cosmic horror, Murdock's Heroine's Journey, cognitive dissonance, AI alignment, Chalmers, Bostrom, Levinas, Aristotle — with two tables that map phobias and Murdock's stages to chapters; it calls its basis „fundiert“ and the outline „eine starke und kohärente Grundlage“ (L298) — recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (400 lines for `roman-outline-kohaerenz-protok`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A report that applies theory to an outline: write „the strategy report applies / maps / places …“. A theory's claim is the theory's; the outline's chapters it cites are the outline's as the report gives them (chapter readings are written by the session). It writes Kael with female pronouns (L33, L52, L98, L166) — keep its pronouns in quotation, never change them. German — quote as written; cut before inner quotes; glued reference digits follow sentences; the tables (L46–L52, L112–L124) have escaped bold — quote the plain words.

## Pages — document 178, `roman-outline-kohaerenz-protokoll-uberarbeitung`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L37, L51, L52, L63, L67, L71, … (66 lines). central (2–4): its psychological warfare — propaganda, deception, demoralisation (L93); warfare also an *internal* control mechanism (L96); its „Fehlausgerichtete Kohärenz“ paradox framed as an AI-alignment failure — cut before the quotes (L187); grounded in alignment research, not evil-AI tropes (L248).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L50, L61, L116, L123, L128, L220. minor (1–2): ANP defence: Kael relies on logic (Lex) and defence (Alex) (L116); Lex vs. Alex in the phobia table (L50).
- **`emergenz`** (central, 3–12 quotations): the census's surfaces — `Emergenz` L124, L143, L174, L187, L199, L222, … (10 lines). minor (1–2): AEGIS's conflict of control vs. Emergenz (L174); complexity theory, emergence and self-organisation (L231); Selene's emergence as coordinator (L124).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L93, L94, L96, L117, L161, L166, … (9 lines). minor (1–2): intimidation by the Guardians (L93); the KWs and Guardians as AEGIS's internal control (L96); the Guardians and the hard problem (L161); what they represent (L187).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L51. minor (1–2): Juna/V's nature shown by its effects on Kael (L75); AEGIS hides Juna/V's true nature (L93); L51 — read the line.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L31, L33, L37, L39, L41, L47, … (78 lines). central (2–4): named `Echo` in AEGIS's violent fragmentation (L199); „Kaels fragmentierte Realität“ and „ihre dissoziative Erfahrung“ (L33) — the report writes Kael female, say so; the phobias in Kael (L46–L52); his TSDP vulnerabilities (L98); Murdock's stages mapped to his arc (L112–L124); the existential crisis in Ch 12 (L166).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L122. minor (1–2): among the EPs integrated in Murdock's stage 8 — „Integration der EPs (Kiko, Lia, Moros)“ (L122).
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L11, L17, L82, L96, L143, L146, … (22 lines). minor (1–2): AEGIS's „Fehlausgerichtete Kohärenz“-Paradoxon (L187) — read on aegis; L96, L143 — read the lines; if only the paradox's name, an occurrence.
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L49, L50, L61, L116, L123, L128, … (8 lines). minor (1–2): Lex's avoidance of emotion (L49); Lex vs. Alex (L50); Kael relies on logic (Lex) (L116); Lex seeks logical consistency but meets illogical glitches (L142).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L122. minor (1–2): among the EPs integrated in stage 8 (L122).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L122. minor (1–2): among the EPs integrated in stage 8 (L122).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L52. minor (1–2): „funktionaler Multiplizität“ — read L52 and the line it stands on; Kael acting as a functional multiple system (L124).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L76. minor (1–2): the „Nichts Rauschen“ in the prologue sets the atmosphere — cut before the quotes (L76).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L123. minor (1–2): among the ANPs reconciled under Selene in stage 9 — „Lex, Alex, Nyx“ (L123): the report classes Nyx as an ANP here, say so.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L51, L142, L220. minor (1–2): Rhys's attachment phobia (L51); Rhys wants harmony while parts conflict (L142).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitches` alone on L142. minor (1–2): Lex meets „illogische Glitches (Ch 1-2)“ — read L142; a reading only if it says something of the Risse, else not read: why.
- **`selene`** (central, 3–12 quotations): the census's surfaces — `Selene` L115, L121, L123, L124, L128, L148, … (10 lines). central (2–4): Kael's fragmented origin as „Trennung von Ganzheit/Selene“ (L115); integration (Selene) (L121); the ANPs coordinated under Selene (L123); „Emergenz von Selene als Koordinatorin“ (L124).
- **`tsdp`** (central, 3–12 quotations): the census's surfaces — `TSDP` L17, L35, L37, L39, L41, L47, … (22 lines). central (2–4): „Theorie der Strukturellen Dissoziation der Persönlichkeit (TSDP)“ as the core theory (L35, L37); the phobia table (L46–L52); the phase model (L63); Kael's TSDP vulnerabilities (L98).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L166, L248. minor (1–2): the nature of the KWs and the Überwelt mirrors simulation questions (L166) — read the line.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `juna`: `Juna/V` (near `juna`). a reading: Juna/V's nature shown by its effects (L75); AEGIS hides Juna/V's true nature (L93) — read on juna.
- `multiplizitaet`: `funktionaler Multiplizität` (near `multiplizitat`). a reading: „funktionaler Multiplizität“ — read L52 and where it stands.
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` (L199) names Kael — „Gewaltsame Fragmentierung von "Echo" (Kael)“ — not the residual echoes; read on kael and C16.


**Record entries** (one file each):

- **`c17-kael-gender`**: the report writes Kael with female pronouns — „ihre dissoziative Erfahrung“ (L33), „Ihr fragmentiertes Selbstgefühl“ (L98), „Ihre existenzielle Krise“ (L166) — and frames the arc with Murdock's Heroine's Journey, „speziell die psycho-spirituelle Reise von Frauen“ (L106); quote it, decide nothing.
- **`c16-kael-origin`**: AEGIS's „Gewaltsame Fragmentierung von“ `Echo` (Kael), in the prologue and Ch 17, 24, 33 (L199) — quote before the inner straight quotes.
- **`q3-how-many-kern-welten-and-alters`**: the alters it names — Lex, Alex, Nyx (ANPs), Kiko, Lia, Moros (EPs), Rhys, Selene (L116–L124, L142).

**Chapter readings** are written by the session from the two tables (L46–L52, L112–L124).

**Not promoted:** the phobias, Murdock's stages, psychological warfare, cognitive dissonance, AI alignment terms (Fehlspezifikation, instrumentelle Konvergenz), Chalmers, Bostrom, Levinas, Popper, Aristotle (Dunamis, Energeia, Telos), the P+39 label.

**Two readers**, disjoint: (1) kael, tsdp, lex, alex, nyx, kiko, lia, moros, rhys, selene, juna, multiplizitaet and the records c17, c16, q3; (2) aegis, guardians, ueberwelt, nichts-rauschen, emergenz, kohaerenz, risse.
