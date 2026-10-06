# Brief — readings from document 119 (step 6)

1 document, one reader, one batch: `ingest-119`. Files go to `Plan/runs/ingest-119/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 119 | `romanarchitektur-kael-aegis-entropie-docx` | 2025-08-05 | „the architecture plan“ (titled `Thematische & Narrative Architektur: System Kael vs. AEGIS`) | a German chapter-by-chapter plan of 2025-08-05: a master table of Kapitel 1–39 with Teil, archetypal phase and core theme (L15–L55), then a section per chapter in five fields (`Vertiefende Konzepte`, `Charakter-/Systemdynamik`, `Genre-Tropes & Innovative Interpretation` …) — written in the conditional; the export breaks off inside Kapitel 38 (L593) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (594 lines for `romanarchitektur-kael-aegis-en`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A plan in the conditional: write „the architecture plan proposes / sets …“, keep `möglicherweise`, `vielleicht` as hedges; its `Innovation` lines are its own claims about borrowed tropes, the tropes themselves are not the world's. Name the chapter section a line stands in (Kapitel N). The chapter pages are done by the session; write no chapter reading. Kael is male.

## Pages — document 119, `romanarchitektur-kael-aegis-entropie-docx`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L24, L30, L31, L32, L36, … (178 lines). central (3–5): the expansion „Autonomous Entropic Gatekeeper for“ Integrity Systems (L337); it treats Kael's multiplicity itself as entropy (L337); its central paradox (L281); its broad sense of Entropie (L393); `AEGIS-Guardian` for LogOS and Cerberus (L81, L179); the plan's question „Wird AEGIS zerstört?“ (L565).
- **`alex`** (central, 3–12 quotations): the census's surfaces — `Alex` L19, L93, L95, L96, L98, L99, … (29 lines). minor (1–2): Kapitel 3, Alex's awakening, the protector (L19, L89).
- **`argus`** (central, 3–12 quotations): the census's surfaces — `Argus` L41, L67, L72, L156, L221, L222, … (23 lines). minor (1–2): „Argus (Beobachter/Kritiker)“ (L67); Kapitel 25, from critic to data collector (L41, L401).
- **`cerberus`** (central, 3–12 quotations): the census's surfaces — `Cerberus` L25, L177, L179, L180, L182, L183, … (15 lines). minor (1–2): „Cerberus, dem AEGIS-Guardian“ of security and defence (L179).
- **`entropie`** (central, 3–12 quotations): the census's surfaces — `Entropie` L40, L84, L169, L207, L210, L253, … (27 lines). minor (1–2): AEGIS's Entropie „umfasst alles, was unvorhersehbar, komplex, emotional, verbunden und lebendig ist“ (L393); Kapitel 24, „Die Sprache der Entropie“ (L40).
- **`externe-ebene`** (minor, 1–4): the census's surfaces — `Externe Ebene` L37, L245, L349, L354, L357, L365, … (9 lines). minor (1–2): Kapitel 21 and 28, first hints of Juna/V and the Externe Ebene, contact with it (L37, L44).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — `Grenzfeste` L25, L173, L176, L179, L253. minor (1–2): „Diese Welt repräsentiert Abwehr, Schutzmechanismen, Grenzen“ (L179); Kapitel 9 (L25).
- **`guardians`** (central, 3–12 quotations): the census's surfaces — `Guardians` L67, L165, L171, L267, L268, L271, … (17 lines). minor (1–2): „Guardians erscheinen in der Überwelt als mächtige Wesenheiten“ (L271); Kapitel 15, the AEGIS-Überwelt and its Wächter (L31).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L310, L444, L495. minor (1–2): „Isabelle [Kontrolle]“ (L495).
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L37. minor (1–2): „Juna/V wird mit Konzepten assoziiert, die AEGIS bekämpft“ (L351); Kapitel 27, the uncontrolled variable (L43).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L11, L39, L48, L49, L50, L53, … (162 lines). central (3–5): „Kael (Host) ist primär von Verwirrung und Angst erfüllt“ (L68); the aim of functional multiplicity and its meaning (L337); Ko-Präsenz and Ko-Bewusstsein (L193); the parts by class (L109, L137).
- **`kairos`** (central, 3–12 quotations): the census's surfaces — `Kairos` L33, L267, L286, L293, L295, L296, … (11 lines). minor (1–2): „Kairos (richtiger Zeitpunkt, Gelegenheit) und/oder Sophia“ (L295).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L59, L129, L165, L208, L240, L253, … (15 lines); `Kernwelt` L59, L67, L87, L123, L129, L165, … (23 lines). minor (1–2): the Kernwelten as mirrors of the psyche and AEGIS's domains (L59); what each world represents (L123, L179, L295).
- **`kiko`** (central, 3–12 quotations): the census's surfaces — `Kiko` L110, L137, L142, L143, L151, L198, … (11 lines). minor (1–2): „Kiko [Angst/Freeze]“ (L137).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L425. not read: L425 — occurrence unless the line says more.
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L18, L75, L78, L81. minor (1–2): Kapitel 2, „Echos in der Konstrukt-Stadt“ (L18, L75–L81).
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L18, L68, L72, L79, L81, L82, … (48 lines). minor (1–2): „Der logikorientierte Anteil Lex“ (L68); Kapitel 2 with LogOS (L18).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L137, L310. minor (1–2): „Lia [Ambivalenz]“ (L137).
- **`logos`** (central, 3–12 quotations): the census's surfaces — `LogOS` L18, L67, L68, L79, L81, L82, … (17 lines). minor (1–2): „LogOS, dem AEGIS-Guardian dieser Domäne“ (L81).
- **`mnemosyne`** (central, 3–12 quotations): the census's surfaces — `Mnemosyne` L22, L123, L126, L135, L137, L138, … (12 lines). minor (1–2): „die Domäne von Mnemosyne, der Wächterin der Erinnerung“ with a question mark (L123).
- **`moeglichkeits-garten`** (minor, 1–4): the census's surfaces — `Möglichkeits-Garten` L295. minor (1–2): KW4, growth and creativity, named both „Möglichkeits-Garten“ and „Potenzial-Garten“ (L295); Kapitel 17 (L33).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L236, L310, L495. minor (1–2): „Moros [Kollaps]“ (L495).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L225, L341, L481, L501, L555. minor (1–2): „Kael strebt nach funktionaler Multiplizität“ and what it means (L337); Kapitel 20, functional multiplicity against AEGIS's ideal of singularity (L36).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L137, L151, L310, L327, L440, L500, … (7 lines). minor (1–2): „Nyx [Kampf]“ (L137).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L45. minor (1–2): the Fundament as a „hypothetischen, tieferen, stabileren Realitätsebene“ (L467); `Realitätsebene` at L45.
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L21, L117, L120, L123. minor (1–2): „Diese Welt ist das Gegenteil von“ KW1, chaotic, fluid (L123); Kapitel 5 (L21).
- **`rhys`** (central, 3–12 quotations): the census's surfaces — `Rhys` L20, L86, L87, L107, L109, L110, … (36 lines). minor (1–2): Kapitel 4, Rhys and internal mediation (L20, L103).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Risse` L210, L212, L213, L221, L241, L256, … (13 lines). minor (1–2): Kapitel 11, „Der erste Riss“ — „Dieser Riss repräsentiert eine lokale Manifestation von Entropie“ (L207); the glitch trope as „ein ontologischer Bruch“ (L210).
- **`selene`** (central, 3–12 quotations): the census's surfaces — `Selene` L296, L310, L343, L366, L422, L431, … (16 lines). minor (1–2): „die aufkommende Selene/Selbst-Figur“ (L310) that establishes itself as coordinating centre (L495) — `Selene/Selbst` and `Selene` both written.
- **`sophia`** (central, 3–12 quotations): the census's surfaces — `Sophia` L33, L267, L286, L293, L295, L296, … (13 lines). minor (1–2): „und/oder Sophia (Weisheit, Wissen)“ (L295).
- **`tsdp`** (central, 3–12 quotations): the census's surfaces — `TSDP` L23, L59, L70, L95, L109, L149, … (17 lines). minor (1–2): TSDP dynamics, Kapitel 7, phobias in the system (L23, L145); ANPs and EPs (L109, L137).
- **`ueberwelt`** (central, 3–12 quotations): the census's surfaces — `Überwelt` L31, L208, L240, L245, L265, L267, … (19 lines). minor (1–2): the `AEGIS-Überwelt`, the place „von der aus AEGIS operiert“ (L267); Kapitel 15 (L31).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `aegis-metriken`: `Integrität` (near `integritatvondatenstrukturen`). occurrence: `Integrität` in Kapitel 20's title (L36, L331), AEGIS's ideal — on aegis and multiplizitaet, not the metric.
- `aegis-teilfunktionen`: `Guardian` (near `integrityguardian`). occurrence: `Guardian` the world guardians.
- `juna`: `Juna/V` (near `juna`). J34: `Juna/V` is Juna — on juna above.


**Record entries** (one file each):

- **`c1-aegis-expansion`**: position 1 again, „Autonomous Entropic Gatekeeper for“ Integrity Systems (L337), with markup inside.
- **`q5-guardians-and-kern-welten`**: LogOS and Cerberus as `AEGIS-Guardian` of their domains (L81, L179); Mnemosyne with a question mark (L123); `Kairos … und/oder Sophia` for KW4 (L295).
- **`q3-how-many-kern-welten-and-alters`**: the parts named by function — Kael (Host), Argus, Lex, Alex, Rhys, Kiko, Nyx, Lia, Moros, Isabelle and the emerging Selene/Selbst (L67–L68, L137, L495); four Kernwelten.
- **`q8-aegis-after-the-vortex`**: the plan leaves AEGIS's fate open, „Wird AEGIS zerstört?“ (L565), Kapitel 36.

**Not promoted:** the borrowed genre tropes per chapter (The Ghost in the Machine, The Reluctant Guardian, Guardian at the Threshold, Glitch in the Matrix …) and their `Innovation` lines; the five field labels; Ko-Präsenz, Ko-Bewusstsein — on kael; `Potenzial-Garten` — on moeglichkeits-garten; Beschützer-Anteil, Fürsorge-Anteil, Schutzanteile.

**Split into two readers, at the same time on disjoint pages:**
- Reader 1: aegis, juna, guardians, ueberwelt, externe-ebene, realitaetsebenen, risse, entropie, logos, cerberus, mnemosyne, kairos, sophia, and the entries c1, q5, q8.
- Reader 2: kael, selene, argus, lex, alex, rhys, kiko, nyx, lia, moros, isabelle, tsdp, multiplizitaet, kern-welten, konstrukt-stadt, resonanz-landschaft, grenzfeste, moeglichkeits-garten, and the entry q3.
