# Brief — readings from document 131 (step 6)

1 document, one reader, one batch: `ingest-131`. Files go to `Plan/runs/ingest-131/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 131 | `subplot-entwicklung-fuer-romanstruktur` | 2025-05-02 | „the subplot catalogue“ (titled `Subplot-Entwicklungskatalog für einen 39-Kapitel Sci-Fi/Horror Roman`, L11) | a German catalogue of 2025-05-02 of subplot ideas, chapter by chapter, each with an analysis of the chapter's focus under a journey phase (Murdock's Heroine's Journey for Teil 1, Meta for Teil 2), a proposed trope or concept, research questions and three subplot ideas; it breaks off in Kapitel 19 (L576) before its web references; it calls itself a catalogue of potential ideas (L15), no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (799 lines for `subplot-entwicklung-fuer-roman`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A catalogue of possibilities: write „the subplot catalogue proposes / suggests …“; sentences it marks `[Prompt]` are taken from the author's prompt — say so („as the catalogue takes from the prompt“); its hedges (vielleicht ×36, wahrscheinlich ×12) stay. Murdock, Jung, IFS and the tropes are borrowed. Kael is male (the note's „Her parts“ follows the Heroine's Journey frame — do not copy it). Glued footnote digits are cut off quotations. Chapter pages are done by the session.

## Pages — document 131, `subplot-entwicklung-fuer-romanstruktur`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L21, L28, L33, L34, L48, … (70 lines). central (2–4): „einem autonomen System zur Entropie-Kontrolle“ managing the reality, taken from the prompt (L15); the illusory success Kael reaches is „genau der Zustand, den AEGIS für Kael anstrebt“ (L158); its core lie or paradox „könnte darin bestehen“ (L483).
- **`alex`** (central, 3–12 quotations): the census's surfaces — `Alex` L49, L58, L74, L75, L83, L99, … (19 lines). minor (1–2): „Alex, der Protektor, warnt Lex davor, Anomalien zu ignorieren“ (L49); his perimeter check (L74).
- **`alters`** (minor, 1–4): the census's surfaces — `Alters` L15, L65, L139, L647. minor (1–2): „multiplen Persönlichkeitsanteilen ('Alters')“ (L15) — cut before the straight quote.
- **`argus`** (central, 3–12 quotations): the census's surfaces — `Argus` L133, L150, L175, L249, L300, L361, … (14 lines). central (2–4): „Der Argus-Anteil (Beobachter/Kritiker)“ (L300); the potential of Selene/Argus as inner allies (L133).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L74, L100, L123, L225, L468. minor (1–2): „Cerberus (Guardian von“ KW3 (L100); KW3 Cerberus-Labyrinth (L123).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L623. occurrence: `DID` only in a reference title (L623).
- **`entropie`** (central, 3–12 quotations): the census's surfaces — `Entropie` L15, L33, L34, L58, L108, L158, … (16 lines). minor (1–2): AEGIS as a system of entropy control (L15); what L33–L34 say.
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L15, L74, L83, L100, L175, L361, … (14 lines). central (2–4): Guardians named with their worlds in parentheses — LogOS KW1 (L98), Mnemosyne KW2 (L124), Cerberus KW3 (L100, L123); Kapitel 17's Guardian „vielleicht LogOS oder Sophia“ (L506).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L115, L125. minor (1–2): „Isabelle (Sexualisierter/Kontroll-EP)“ (L125).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L133. minor (1–2): Juna/V as an external ally or a cryptic contact (L133, L150); a clearer message in Kapitel 15 or 16 (L398).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L15, L21, L28, L33, L34, L48, … (104 lines). central (2–4): „System Kael, besitzt eine fragmentierte Identität basierend auf der Theorie der Strukturellen Dissoziation der Persönlichkeit“ (L15); the aim „funktionale Multiplizität oder Integration“ (L15); in Teil 1 his inner journey under the Heroine's Journey (L28).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kern-Welt` L74, L83, L150, L249, L360, L406, … (11 lines); `Kern-Welten` L150, L249, L360, L406, L407, L411, … (9 lines). central (2–4): KW1 (Logos-Prime, L98), KW2 Mnemosyne-Archipel (L124), KW3 Cerberus-Labyrinth (L123), KW4 Kairos-Potentialis (L150); the four by theme, Logik, Emotion/Erinnerung, Abwehr, Potenzial (L360); „Die Kern-Welten von AEGIS sind psychologische Landschaften, die Kaels Innenleben spiegeln“ (L415).
- **`kiko`** (central, 3–12 quotations): the census's surfaces — `Kiko` L58, L75, L99, L115, L124, L200, … (19 lines). central (2–4): find Kiko's role in parentheses (L58, L115, L124) and what Kapitel 4–8 propose for the part.
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L325. occurrence: in passing (L325).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L33, L48, L49, L58, L73, L75, … (30 lines). central (2–4): „Lex (Analytiker ANP)“ (L48); his cold logic resisted by Rhys (L73).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L58, L115, L149, L200, L208, L209, … (9 lines). minor (1–2): find Lia's lines (L58, L115, L208) — its role, briefly.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L74, L98, L175, L397, L433, L506. minor (1–2): KW1 (Logos-Prime) with LogOS (L98); L506.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L99, L124, L208. minor (1–2): „Mnemosyne (Guardian) könnte subtil präsent sein“ (L124); KW2 Mnemosyne-Archipel.
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L115, L199, L208, L250, L550. minor (1–2): „Moros (Kollaps EP)“ (L199).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L15, L350, L359. minor (1–2): the outcome of Kapitel 12: „sondern das Erreichen von funktionaler Multiplizität und Ko-Bewusstsein“ (L308); L15.
- **`nyx`** (central, 3–12 quotations): the census's surfaces — `Nyx` L99, L109, L115, L123, L149, L258, … (10 lines). minor (1–2): „Nyx (Kämpfer EP)“ (L123).
- **`rhys`** (central, 3–12 quotations): the census's surfaces — `Rhys` L49, L73, L100, L123, L148, L173, … (17 lines). minor (1–2): „Rhys (Pfleger ANP)“ (L49) — an ANP here.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitch` alone on L84. minor (1–2): the trope „Glitch in the Matrix“ (L84); a persistent Riss AEGIS cannot fix (L150) — cut before the straight quote.
- **`selene`** (central, 3–12 quotations): the census's surfaces — `Selene` L133, L233, L249, L258, L283, L284, … (12 lines). central (2–4): „Selene (Integration/Selbst)“ (L308); its potential surfacing in Kapitel 5 (L133); Kapitel 12's Heilige Hochzeit (L304–L308).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L506. minor (1–2): named once, as a possible Guardian of Kapitel 17 (L506).
- **`tsdp`** (central, 3–12 quotations): the census's surfaces — `TSDP` L15, L16, L34, L39, L48, L59, … (35 lines). central (2–4): the theory of structural dissociation as the base of Kael's identity (L15); ANP and EP as its terms (L48).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L406, L407, L415, L434. minor (1–2): what L406–L434 say of the Überwelt in Kapitel 15–16.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` the role word.
- `juna`: `Juna/V` (near `juna`). `Juna/V` (J34) — on juna above.
- `kairos`: `Kairos-Potentialis` (near `kairos`). occurrence: `Kairos-Potentialis` is KW4's world name (L150, L324, J49) — read on kern-welten.
- `personas`: `Apparently Normal Personality` (near `persona`). occurrence: the expansion of ANP, on tsdp.
- `risse`: `Riss` (near `risse`), `Glitch in the Matrix` (near `glitch`). on risse above; the trope's name is borrowed.


**Record entries** (one file each):

- **`q5-guardians-and-kern-welten`**: LogOS KW1 Logos-Prime (L98), Mnemosyne KW2 Mnemosyne-Archipel (L124), Cerberus KW3 Cerberus-Labyrinth (L100, L123), KW4 Kairos-Potentialis (L150) — dated 2025-05-02.
- **`q3-how-many-kern-welten-and-alters`**: four Kern-Welten by theme (L360); the parts with roles: Lex, Alex, Rhys, Nyx, Isabelle, Moros, Argus, Selene, Kiko, Lia.

**Not promoted:** the journey phases (on the chapter pages), Heilige Hochzeit, Dissoziative-Tisch-Technik, the IFS analogy, Glitch in the Matrix and the other tropes, the research questions.

**Split into two readers, at the same time on disjoint pages:**
- Reader 1: aegis, entropie, guardians, logos, mnemosyne, cerberus, sophia, kern-welten, ueberwelt, juna, risse, and the entry q5.
- Reader 2: kael, lex, alex, rhys, nyx, isabelle, moros, kiko, lia, argus, selene, alters, tsdp, multiplizitaet, and the entry q3.
