# Brief — readings from document 251 (step 6)

1 document, one reader, one batch: `ingest-251`. Files go to `Plan/runs/ingest-251/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 251 | `report-narrative-methodology-for-kohaerenz-protokoll` | 2025-10-15 | „the methodology report“ (an unsigned English report) | a report of directives for the writing: AEGIS's cold logical voice against Kael's voice from fragmentation to polyphony, three perspectives, the Guardians as thematic tests, and techniques (Risse, metafictional footnotes, found footage); it calls itself „the foundational blueprint for that architecture“ (L17), its claim, not canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (109 lines for `report-narrative-methodology-f`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** Directives for a writer: write „the methodology report directs / proposes …“; its sample sentences illustrate a style, not the novel's text. Cut quotations before inner straight quotes and escaped markup.

## Pages — document 251, `report-narrative-methodology-for-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L21, L23, L25, L51, L55, … (14 lines). central (3–6): its narrative voice a direct expression of an information-based system driven by classical logic, autopoietic and operationally closed (L25); impersonal, technical diction (L27–L28); AEGIS possibly an unreliable narrator (L63); firewalled, low-Φ subsystems (L51); a „system correction“ told by AEGIS's log against Kael's experience (L68).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L70, L72, L74, L76, L79. minor (1–4): not independent actors but functional manifestations of AEGIS's core logic (L72); embodiments of its logic operating within its laws (L78–L79); the Guardian of KW1 (Logik) assaulting Lex's logic (L80).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L96. minor (1–4): ambiguity to be kept about Juna/V and Das Fundament (L96).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L21, L32, L34, L38, L46, … (16 lines). central (3–6): his voice moving from Tertiäre Strukturelle Dissoziation (TSDP) to a functional, co-conscious multiplicity (L34); the fragmented voice of ANPs and EPs (L36–L42); the integrated, polyphonic or choric voice (L44–L46), high Φ (L51).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L48. minor (1–4): „Kiko’s dread“ in the sample sentence (L48).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: occurrence — the title (L11).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L91. minor (1–4): its „sterile, brutally symmetric architecture“ (L91).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L48, L49, L80. minor (1–4): the analytical, hypotactic rhythm of Lex (L49); Kael's analytical part, Lex, assaulted by the Guardian of KW1 (L80).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L49. minor (1–4): Nyx given visceral, staccato phrases (L49).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L92. minor (1–4): the „Risse“ (Rifts) shown as moments where the narrative form itself breaks down (L92).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L34. minor (1–4): Kael's voice starting in „Tertiäre Strukturelle Dissoziation (TSDP)“ (L34).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` is the Guardians' singular, read on guardians.
- `juna`: `Juna/V` (near `juna`). `Juna/V` read on juna (J34).
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`). occurrence: the title.
- `personas`: `depersonalization` (near `persona`). occurrence: depersonalization is a symptom, not the Personas.


**Record entries** (one file each):

- **`q1-guardians-and-aegis`**: the Guardians not independent actors but functional manifestations of AEGIS's core logic (L72, L78–L79).
- **`q5-guardians-and-kern-welten`**: „the Guardian of KW1 (Logik)“ (L80).

**Not promoted:** the voices and perspectives, Algorithmic Horror, the epistemology-shift, the Meta-Narrator, the metafictional techniques, Φ, Das Fundament.

**One reader**: aegis, kael, guardians, lex, nyx, kiko, konstrukt-stadt, risse, tsdp, juna and the records q1, q5. `kohaerenz` is an occurrence.

**Chapter readings**: none.
