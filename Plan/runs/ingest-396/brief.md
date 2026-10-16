# Brief — readings from document 395 (step 6)

1 document, one reader, one batch: `ingest-396`. Files go to `Plan/runs/ingest-396/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 395 | `roman-kapitel-entwurf-mit-kohaerenzprotokoll` | 2026-02-23 | „the consultation report“ (an unsigned German „Konsultationsbericht und Manuskriptentwurf“) | advises on pacing, Lex's sabotage, the Landauer principle and a K1/K0 style table, then holds a draft of „Kapitel Eins: Der Kristalline Käfig“ (L57–L163) and an evaluation ending on a question about Kernwelt 2; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (196 lines for `roman-kapitel-entwurf-mit-koha`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A consultation with a draft inside it: write „the consultation report advises …“ for its advice and „in its Kapitel-Eins draft …“ for the prose; the draft is not the chapter as approved, the advice decides nothing. Quote the German as written; cut before glued footnote digits, escapes, table pipes and straight quotes. No gendered pronoun for Kael, Lex or Juna — use the names (quotations stay verbatim). Never write a real person's name from the reference list.

## Pages — document 395, `roman-kapitel-entwurf-mit-kohaerenzprotokoll`

- **`aegis`** (minor, 1–4): the census's surfaces — `AEGIS` L25, L37, L39, L43, L50, L127, … (9 lines). minor (1–3): the expansion „Autonomous Entropic Gatekeeper for Integrity Systems“ (L25); AEGIS operating on Shannon entropy, trying to erase unpredictability and trauma (L37); in the draft „griff die Zero-Trust-Architektur von AEGIS ein“ (L145).
- **`alex`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alex` alone on L180. not read: an occurrence (see below).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L31, L51. minor (1–3): the sabotage of an everyday act by a personality part (Alters) leaking through (L31); „Kael (Alters)“ in the K0 row of the style table (L51).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L33. minor (1–3): the sabotage showing Kael's suppressed complexity without revealing the secret of the Dissociative Identity Disorder (DID) too early (L33).
- **`entropie`** (minor, 1–4): the census's surfaces — `Entropie` L37, L39, L51, L131, L139, L157, … (9 lines). minor (1–3): AEGIS's basis in Shannon entropy (L37); Entropie in the K0 row beside Kael and Juna (L51).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L39, L51, L53, L113, L121, L133, … (7 lines). minor (1–3): in the draft Juna's image as „das Interface“ and „Der Anker des Systems“ (L115); the name acting on Kael like a chord of the Monster group (L143); Juna in the K0 row (L51).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L25, L27, L33, L51, L63, L75, … (22 lines). central (3–5): Kael at the start as an unknowing host ANP (L27); the sabotage at the dispenser, Lex's compulsion paralysing the host (L33); in the draft Kael's encounters — the arithmetic to a prime (L99), Juna's image (L115), the K1 kernel splintering (L127), the Landauer principle taking its toll (L139).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. not read: an occurrence (see below).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L50. minor (1–3): the style table's row „K1 (Kohärenz-Kernel)“: AEGIS, Konstrukt-Stadt, LogOS, control; minimalist, clinical, paratactic (L50); in the draft the K1-Kernel, AEGIS's flawless order, splintering (L127).
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L51. minor (1–3): the row „K0 (Kollaps-Kernel)“: Kael (Alters), Juna, Entropie, trauma; maximalist, deep POV, hypotactic (L51); the mode switching to K0 at the hologram (L53).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L39, L50, L53, L115, L163, L169, … (7 lines). minor (1–3): „Die Konstrukt-Stadt (KW1) ist die Domäne von LogOS“ in the K1 style (L53); the Konstrukt-Stadt in the draft's last paragraph (L163).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L29, L31, L33, L89. minor (1–3): the analytical manager part „oft als“ Lex or Index named, the compulsion to hyper-logical control (L31); Lex's compulsion to factorise the calories (L33); in the draft the part pushing silently in front of the primary control (L89).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L50, L53, L121, L157. minor (1–3): the Konstrukt-Stadt as „die Domäne von LogOS“ (L53); in the draft „Das Gesetz von LogOS verlangte Vorhersagbarkeit“ (L157).
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L169. minor (1–3): the closing question about „die Architektur der Resonanz-Landschaft“ of Kernwelt 2 (L169).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L37, L51. minor (1–3): the physical grounding of the Risse (Glitches) in the simulation through Shannon entropy (L37); Risse in causality in the K0 row (L51).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L35. minor (1–3): the heading „Thermodynamik der Simulation“ for the Landauer principle (L35).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Zero-Trust-Architektur` (near `zerotrust`). `Logos-Prime` and `Kernwelt 2` on kern-welten-type mentions, not read here beyond the pages above; `Autonomous Entropic Gatekeeper for Integrity Systems` and `Zero-Trust-Architektur` on aegis; `Shannon-Entropie` on entropie; `Kohärenz Protokoll(s)` the title; `Alex` (L180) a real person's name in a reference, not the figure — an occurrence, never written.
- `kern-welten`: `Kernwelt 2` (near `kernwelt`). `Logos-Prime` and `Kernwelt 2` on kern-welten-type mentions, not read here beyond the pages above; `Autonomous Entropic Gatekeeper for Integrity Systems` and `Zero-Trust-Architektur` on aegis; `Shannon-Entropie` on entropie; `Kohärenz Protokoll(s)` the title; `Alex` (L180) a real person's name in a reference, not the figure — an occurrence, never written.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz Protokolls` (near `koharenz`). `Logos-Prime` and `Kernwelt 2` on kern-welten-type mentions, not read here beyond the pages above; `Autonomous Entropic Gatekeeper for Integrity Systems` and `Zero-Trust-Architektur` on aegis; `Shannon-Entropie` on entropie; `Kohärenz Protokoll(s)` the title; `Alex` (L180) a real person's name in a reference, not the figure — an occurrence, never written.


**Pages beyond the draft:**
- `dkt` (minor, 1): the method named Dual Kernel Theory, „DKT“ (L43).

**Pages not read:** `alex` (L180, a reference author, not the figure), `kohaerenz` (L11, the title) — occurrences.

**Record entries:** none.

**Not promoted:** Novel Writing Assistent, Primfaktorzerlegung, Landauer-Prinzip, digitale Abwärme, Preis der Ordnung, Index, the style table's labels; the borrowed concepts.

**One reader**: aegis, alters, did, entropie, juna, kael, kohaerenz-kernel, kollaps-kernel, konstrukt-stadt, lex, logos, resonanz-landschaft, risse, ueberwelt, dkt.

**Chapter readings** (batch `ingest-396-kap`, file `Plan/runs/ingest-396-kap/readings/kap-01--roman-kapitel-entwurf-mit-kohaerenzprotokoll.md`):
- **`kap-01`**: the draft „Kapitel Eins: Der Kristalline Käfig“ (L57) inside the consultation report: Lex pushing in at the dispenser and the arithmetic to a prime (L89, L99), Juna's image as interface and anchor (L115), the K1 kernel splintering (L127), the Landauer principle's toll and the smell of ozone (L139, L141), AEGIS's Zero-Trust intervention (L145), the law of LogOS (L157). A draft inside a report, not the chapter as approved.
