# Brief — readings from document 117 (step 6)

1 document, one reader, one batch: `ingest-117`. Files go to `Plan/runs/ingest-117/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 117 | `kohaerenz-protokoll-konzeptionelle-themen-struktur` | 2025-11-25 | „the themes exegesis“ (titled `Kohärenz Protokoll: Konzeptionelle Themen & Struktur`, its H1 „Eine Exegese der narrativen Systemarchitektur, Ontologie und Psychodynamik“, L13) | a German expository report of 2025-11-25: the protocol ontology and the two kernels (L25–L56), AEGIS and Paradoxon X (L60–L64), System Kael by TSDP (L72–L77), a gravitational architecture of four zones (L85–L111), 39 numbered themes in three parts each with a `Konzept` bullet (L127–L342), a four-subsystem Dramatica/NCP table (L350–L376) and the Parakonsistente Gambit (L400–L422). It calls itself „eine erschöpfende Analyse“ (L27); footnote numbers 1–5 are glued to sentences |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (431 lines for `kohaerenz-protokoll-konzeption`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An exegesis: write „the themes exegesis says / reads …“; where a footnote number is glued to the sentence it reports a reference — say so. Its 39 numbered items are **themes**, not chapters; it never says they coincide with the Kapitel of its part headings — never write a theme as a chapter. Kael is male.

## Pages — document 117, `kohaerenz-protokoll-konzeptionelle-themen-struktur`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L29, L56, L60, L62, L64, L72, … (34 lines). central (3–5): „kein einfacher Schurke“, an autopoietic, operationally closed system (L60, ref. 3); born of its own traumatic origin, the Paradoxon X, it fragmented its own consciousness by the Trennungsprotokoll (L62, ref. 4); a coherence theory of truth (L64); Kael chooses to prune it, not delete it (L295); its collapse into Algorithmische Melancholie (L321, L410).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L238. minor (1): L238 — the Kernwelt (Cerberus) theme.
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L321, L410. minor (1–2): theme 34's effect, „Algorithmische Melancholie“ (L321), and section 6 (L410).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L237, L238. minor (1): `Kernwelt (Cerberus)` (L237–L238).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L255. occurrence unless more: L255.
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L25, L29, L50, L64, L119, L230, … (7 lines). minor (1–2): K0 as the principle of entropy (L50); negentropy against entropy (L119).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L62, L367. minor (1): Juna/V in the subsystem table, who changes probabilities, not matter (L367, ref. 5); and in the AEGIS passage (L62) only if the line says more.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L29, L64, L68, L72, L77, L119, … (37 lines). central (3–5): „System Kael, ist das physische Gegenstück zu AEGIS' Logik“ (L72), organised by TSDP (L72); the journey to unite ANPs and EPs (L77); the parts named (L74–L75); the Dialetheic mind at the climax (L408); „Hüter der Komplexität“ (L330) and Camus's happy man (L334).
- **`kairos`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kairos` alone on L175. occurrence: `Kairos` is cyclical time against Chronos (L175), not the Guardian.
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelt` L217, L237, L257. minor (1–2): themes 15, 19, 23 headed `Kernwelt 1`, `Kernwelt 3`, `Kernwelt 4`, with `Konzept: Kernwelt (LogOS)` (L217) and `(Cerberus)` (L237); no Kernwelt 2 is written.
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L75, L154. minor (1): an EP (L75); L154.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. not read: the title (L13) — occurrence (J9).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L49. minor (1): K1, defined through consciousness as „die subjektive Signatur der Kohärenz“ (L49, ref. 1).
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L50, L170. minor (1): K0, the principle of entropy and information erasure exerting „erosiven Druck“ (L50); contact with K0 in theme 7, Lex's logic failing (L170).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L74, L144, L145, L170. minor (1): an ANP of the list (L74); Lex's logic fails at the contact with K0 (L170); themes at L144–L145.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L217, L218. minor (1): `Kernwelt (LogOS)` (L217–L218).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L167, L169, L180. minor (1): L167, L169, L180 — what the theme lines say of Moros.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L195. minor (1): theme `Funktionale Multiplizität` (L195).
- **`negentropie`** (minor, 1–4): the census's surfaces — `Negentropie` L119, L190. minor (1): L119, L190 — what the lines say.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L75, L180, L189. minor (1): an EP (L75); L180, L189.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L74, L159, L160. minor (1): an ANP (L74); themes at L159–L160.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L285. minor (1): L285 — read only if the line says what the Risse are here; else occurrence.
- **`trennungsprotokoll`** (minor, 1–4): the census's surfaces — `Trennungsprotokoll` L62. minor (1): AEGIS fragmented its own consciousness by the Trennungsprotokoll (L62).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L27, L72, L137, L152, L172, L182, … (9 lines). minor (1–2): Kael's psyche organised by TSDP (L72); ANPs and EPs (L74–L75) as the correspondence-truth bearers.
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L29. not read: `Simulation` in passing (L29) — occurrence.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `coheron`: `Coherons` (near `coheron`). occurrence unless more: `Coherons` — read on coheron only if a line says what they are.
- `genesis`: `Genesis-Krise` (near `genesis`). occurrence: `Genesis-Krise` as AEGIS's origin, on aegis.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Paradoxon der fehlausgerichteten Kohärenz` (near `koharenz`), `Kohärenztheorie der Wahrheit` (near `koharenz`). occurrence: the title; `Paradoxon der fehlausgerichteten Kohärenz` is AEGIS's Paradoxon X, on aegis; `Kohärenztheorie der Wahrheit` borrowed, on aegis.
- `risse`: `Riss` (near `risse`). `Riss` — with risse above.


**Record entries** (one file each):

- **`q8-aegis-after-the-vortex`**: theme 29, „Kael wählt, AEGIS nicht zu löschen, sondern zu beschneiden“ (L295); theme 34, AEGIS's collapse into `Algorithmische Melancholie` (L317–L321) — a report of 2025-11-25, before the author's answers, changing neither.
- **`q5-guardians-and-kern-welten`**: themes 15, 19, 23 — `Kernwelt (LogOS)`, `Kernwelt (Cerberus)`, `Kernwelt` with no guardian (L217, L237, L257); no Kernwelt 2.

**Not promoted:** the gravitational architecture (black holes, Hawking, wormholes, brane cosmology, L85–L123); Hyper-Autopoiesis; the four-subsystem Dramatica/NCP table (L350–L376); the 39 themes as such; Paradoxon X — on aegis; Dialetheischer Geist — on kael.

**No chapter readings:** its Kapitel ranges (Teil 1 Kap 1–13, Teil 3 Kap 27–39, the table's Akt III 27–34 and Klimax 35–39) carry themes, not chapters; the document never says a theme is a chapter.

**Split into two readers, one after the other:**
- Reader 1: aegis, juna, trennungsprotokoll, kohaerenz-kernel, kollaps-kernel, entropie, negentropie, algorithmische-melancholie, risse, and the entry q8.
- Reader 2: kael, multiplizitaet, tsdp, lex, rhys, kiko, nyx, moros, alex, kern-welten, logos, cerberus, and the entry q5.
