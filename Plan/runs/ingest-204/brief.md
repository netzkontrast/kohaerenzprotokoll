# Brief — readings from document 204 (step 6)

1 document, one reader, one batch: `ingest-204`. Files go to `Plan/runs/ingest-204/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 204 | `als-ihr-narrativer-architekt-blicke-ich-auf-das-r` | 2025-07-30 | „the final causal blueprint“ (an unsigned plot outline) | a German 40-chapter outline in four Kishōtenketsu acts that calls itself a „Finaler Kausaler Bauplan“ fusing the structural and content outlines (L11, L13): chapters 1–13 with `Inhalt` and `Fokus`, 14–40 one line each — its plan recorded, never applied |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (149 lines for `als-ihr-narrativer-architekt-b`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An outline: write „the final causal blueprint plans / has …“ and name the chapter a line belongs to; its `final` is its own claim. German — quote as written; `--find` drops the digit in `KW1`–`KW4` and refuses names under four letters alone (`Lex`, `Nyx`, `Lia`) — quote around them; chapters 14–40 begin with an escaped `14\.`; cut before inner „…“ quotation marks of the document.

## Pages — document 204, `als-ihr-narrativer-architekt-blicke-ich-auf-das-r`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L17, L21, L26, L32, L36, L41, … (20 lines). central (3–8): chapter 2 from AEGIS's cold, analytical perspective assessing „Subjekt Kael“, his fragmentation a variable to manage (L26); its sensors registering the Juna/V resonance as high-entropy system errors (L46); the „perverse Instantiierung“ of its directive, tightening control (L66); classing Kael as an existential threat (L98); developing paraconsistent logic (L110); its transformation forced by the Gödel-Satz (L132), then frozen in „ineffizienter Schönheit“ (L138).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L104. minor (1–2): „Der Beschützer Alex entwickelt Strategien gegen AEGIS' psychologische Kriegsführung“ (L104).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L138. minor (1–2): chapter 35 `Algorithmische Melancholie`: AEGIS frozen in transformation, marked by „ineffizienter Schönheit“ (L138).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L106. minor (1–2): „Der Meta-Beobachter Argus konfrontiert das System mit seiner Hoffnungslosigkeit“, paralysing Lex (L106) — Argus as an inner part here.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L21. minor (1–2): chapter 1's metaphysical prologue „über die Genesis von AEGIS aus der Leere“ (L21).
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L128. minor (1–2): Kael and Juna formulate the „Gödel-Gambit“, a targeted attack on AEGIS's core axioms (L128) — cut before the inner quotation marks; the presentation of the Gödel-Satz as climax (L132).
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L120. minor (1–2): „Die Kontrollstrategie von Isabelle wird als Trauma-Reaktion entlarvt und transformiert“ (L120).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L36, L44, L46, L47, L88, L112, … (10 lines). central (3–8): the first subtle manifestation of the Juna/V connection — a sensory detail that does not exist for AEGIS (L36); chapter 6 `Die Juna-Anomalie`, Juna/V as the central threat to AEGIS's order (L47); Kael learns to heed Juna/V's signals (L88); AEGIS's attempt to cut the connection causes the midpoint wave (L112); the connection becomes a clear channel (L122); Juna/V helps Kael present his paradoxical state to AEGIS's core (L132).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L17, L21, L22, L26, L27, L31, … (33 lines). central (3–8): Kael waking in the sterile Konstrukt-Stadt with amnesia (L21); the split between the functional ANP (Kael) and suppressed trauma (L22); his decision to stop following AEGIS's rules and seek the cause of the Risse (L81); the turn from passive victim to active protagonist (L82); stable inner cooperation (L124); the birth of the Gärtner, ethical guardian of reality (L140).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L36, L42, L71, L76. minor (1–2): the child part Echo/Kiko hinted in a flashback at the See der Tränen (L36); a full intrusion of the child part Kiko in freeze (L71).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the Protokoll's name in the title (L11).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L21, L29. minor (1–2): Kael wakes in „der sterilen Konstrukt-Stadt“ (KW1) (L21); chapter 3 `Echos in der Konstrukt-Stadt` (L29).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L27, L31, L32, L41, L42, L56, … (7 lines). minor (1–2): the Archivar as a manifestation of Lex, giving only censored information (L31); Lex introduced as ANP (L32); Lex's perspective establishing avoidance of KW2 and KW3 (L56).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L102. minor (1–2): in KW4 Kael learns that creativity (Lia) arises from uncertainty (L102) — quote around the short name.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Mnemosyne` alone on L90. minor (1–2): chapter 15: a confrontation with „Guardian Mnemosyne“ in KW2 and her gaslighting through manipulated memories (L90).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L108. minor (1–2): Rhys's attempt to reach „den kollabierten Anteil Moros“ nearly fails (L108).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `Funktionale Multiplizität` L124. minor (1–2): chapter 30 `Funktionale Multiplizität`: a stable state of inner cooperation, the prose taking a choral style (L124).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L76, L100. minor (1–2): the fighter part Nyx takes control with destructive but protective aggression (L76); Kael recognises Nyx's protective function (L100) — quote around the short name.
- **`resonanz-landschaft`** (minor, 1–4): the census's surfaces — `Resonanz-Landschaft` L51. minor (1–2): Kael re-enters „die Resonanz-Landschaft (KW2)“ and meets his fragmented past (L51).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L37, L42, L94, L108. minor (1–2): „Der empathische Anteil Rhys tritt hervor“ to ease the fear (L37); a fragile truce in the inner conference room, mediated by Rhys (L94).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L21, L27, L81; `Glitches` L41. minor (1–2): first subtle „Rissen“ in reality (L21) — cut before the inner quotation marks; a massive Riss in KW1 revealing the simulation's chaotic architecture (L61); AEGIS answering the Riss with a perverse instantiation (L66).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L81. minor (1–2): at the end of act I Kael „sucht bewusst die Überwelt auf“ (L81).

- **`kishotenketsu`** (minor, 1–2): the narrative follows „der thematisch passenden Kishōtenketsu-Struktur in vier Akten“ (L13) — Ki chapters 1–13, Shō 14–26, Ten 27–34, Ketsu 35–40 (L15, L84, L114, L134).
- **`kern-welten`** (minor, 1–3): KW1 the Konstrukt-Stadt (L21), KW2 the Archive, the See der Tränen and the Resonanz-Landschaft (L31, L36, L51), KW3 the Cerberus-Labyrinth as „Inneren Bunker“ (L51), KW4 the Möglichkeiten-Garten (L61) — quote around the digits.
- **`moeglichkeits-garten`** (minor, 1–2): Kael glimpses „KW4 (Möglichkeiten-Garten)“ through a massive Riss (L61); chapter 21 `Ein Garten der unmöglichen Pfade` (L102).
- **`komponente-734`** (minor, 1–2): chapter 2 is titled `Protokoll 734: Kohärenz-Initialisierung` (L24); AEGIS pursues Kael through agents „(Einheit 734)“ (L41) — quote around the digits.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). occurrence: `Cerberus-Labyrinth` is KW3's name (L51, L96), read on kern-welten (J49).
- `kishotenketsu`: `Kishōtenketsu-Struktur` (near `kishotenketsu`), `Ketsu` (near `kishotenketsu`). a reading — see the extra page below.
- `mnemosyne`: `Guardian Mnemosyne` (near `mnemosyne`). `Guardian Mnemosyne` read on mnemosyne (L90).
- `personas`: `Depersonalisation` (near `persona`). occurrence: `Depersonalisation` is the clinical symptom (L27).
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` is the child part Echo/Kiko (L36), not the Residual-Echos.


**Record entries** (one file each):

- **`q7-what-734-names`**: `Protokoll 734` as a chapter title from AEGIS's perspective on „Subjekt Kael“ (L24, L26) and agents „(Einheit 734)“ pursuing Kael (L41).
- **`q8-aegis-after-the-vortex`**: the Gödel-Satz forces AEGIS's transformation (L132); AEGIS frozen in transformation (L138); Kael becomes the Gärtner, the ethical guardian of reality (L140).
- **`q5-guardians-and-kern-welten`**: KW1–KW4 with their places (L21, L51, L61); „Guardian Mnemosyne“ in KW2 (L90); a Guardian fought in chapter 33 (L130).
- **`q3-how-many-kern-welten-and-alters`**: the parts named — Lex, Echo/Kiko, Rhys, Nyx, Lia, Alex, Argus as meta-observer, Moros, Isabelle (L31–L120) — and four Kernwelten.

**Not promoted:** ANP and EP (the structural-dissociation vocabulary, on did), Korrekturprotokoll Delta, Fragment 'O', Axiom der Vermeidung, the See der Tränen, the Innerer Bunker, D2-Modul, the Fundament and its Grounding-Artefakte, the Heldinnenreise.

**Two readers**, disjoint: (1) kael, juna, lex, kiko, rhys, nyx, lia, alex, argus, moros, isabelle, multiplizitaet, kishotenketsu and the record q3; (2) aegis, risse, genesis, goedel-gambit, algorithmische-melancholie, konstrukt-stadt, kern-welten, moeglichkeits-garten, resonanz-landschaft, mnemosyne, ueberwelt, komponente-734 and the records q7, q8, q5.

**Chapter readings**: 40, written by the session (`Plan/runs/ingest-204-kap/`).
