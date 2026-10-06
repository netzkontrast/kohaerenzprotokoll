# Brief — readings from document 124 (step 6)

1 document, one reader, one batch: `ingest-124`. Files go to `Plan/runs/ingest-124/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 124 | `roman-outline-fuer-kohaerenz-protokoll` | 2025-05-03 | „the detailed outline“ (titled `Kohärenz Protokoll - Detaillierte Roman-Outline`, L11) | a German outline of 2025-05-03 for the Prologue and Chapters 1–13, each in the same labelled fields (Core Theme, Kael System Dynamics, AEGIS Strategy/Manifestation, Setting & Atmosphere, Narrative Goals & Pacing, Key Beats with a `Notiz` each, Philo Hint); it breaks off inside Chapter 13 (L885) and claims no canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (902 lines for `roman-outline-fuer-kohaerenz-p`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An outline proposes, mostly hedged („möglicherweise“, „könnte“): write „the detailed outline plans / proposes …“; its `Notiz` lines say what a beat is for, its Philo Hints apply a philosophy — both its own. Chapter numbers are its own (Chapter 1–13, with references to Kap. 19 and 25 it does not contain). Kael is male. Chapter pages are done by the session.

## Pages — document 124, `roman-outline-fuer-kohaerenz-protokoll`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L15, L17, L18, L19, L27, L37, … (109 lines). central (2–4): the Kohärenz Protokoll as „eine kalte, logische Antwort auf eine existenzielle Krise“ (L17); AEGIS as a reactive structuring principle in the Prologue (L16); its paradox as fragmentation for coherence (L56); forcing absolute coherence leads to breaks (L759); the Riss proves its control is not absolute (L789).
- **`alex`** (central, 3–12 quotations): the census's surfaces — `Alex` L214, L215, L216, L217, L218, L226, … (43 lines). central (2–4): „das Erwachen des Beschützer-Anteils (Alex)“ (L214); blind defence as an insufficient strategy (L884).
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L748, L791, L807, L808, L810, L816, … (9 lines). minor (1–2): „der möglicherweise hier stärker hervortretende Argus, der Meta-Beobachter“ (L748).
- **`cerberus`** (central, 3–12 quotations): the census's surfaces — `Cerberus` L611, L613, L614, L615, L624, L632, … (15 lines). central (2–4): KW3, „die Domäne der Angst, der Verteidigung und des Wächters Cerberus“ (L611); „Guardian Cerberus wird eingeführt“ (L624).
- **`emergenz`** (minor, 1–4): the census's surfaces — `Emergenz` L37, L38, L39, L59. minor (1–2): L37–L39 in the Prologue — what the lines say of Emergenz.
- **`externe-ebene`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Externe Ebene` alone on L790. minor (1–2): „Der Riss ist das erste konkrete Tor“ to this level, foreshadowing Kap. 19 and 25 (L790).
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L13. occurrence: `[Genesis]` the Prologue's title (L13) — read on kap-00 only.
- **`grenzfeste`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Grenzfeste` alone on L609. minor (1–2): Chapter 9's title „Die Mauern der Grenzfeste“ (L609) and what L611 says of the place, if it names it.
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L162, L355, L424, L624. minor (1–2): each world's Guardian introduced in turn (L162, L355, L624) — what L424 says.
- **`juna`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Juna` alone on L19. minor (1–2): Juna/V, „ihre Natur bleibt aber mysteriös“ (L58); the Riss as connection to the outside (L788).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L16, L19, L28, L37, L47, L57, … (112 lines). central (2–4): the host, dominant, with „signifikante Amnesie“ of origin and multiplicity (L83); the Prologue on the act of fragmentation before his existence as a system (L15); the turn from victim to actor in Chapter 13 (L883–L884).
- **`kiko`** (central, 3–12 quotations): the census's surfaces — `Kiko` L342, L383, L399, L404, L412, L414, … (13 lines). central (2–4): an EP carrying a core feeling (L383), e.g. „Kiko mit intensiver Angst“ (L404); the broken child's room (L412).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L11. occurrence: the title and the protocol's name (J9); `Fehlausgerichtete Kohärenz` read on aegis.
- **`lex`** (central, 3–12 quotations): the census's surfaces — `Lex` L84, L125, L142, L148, L149, L150, … (52 lines). central (2–4): „latenter Lex“ (L84); much more active in Chapter 2, decoding KW1's rules (L148); the limits of pure logic against LogOS (L150, L172).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L412, L452, L479. minor (1–2): find its lines (L412, L452, L479) — what is said of Lia.
- **`logos`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `LogOS` alone on L150. minor (1–2): Guardian LogOS, KW1's Wächter, „potenzieller Manipulator“ (L150, L162).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Mnemosyne` alone on L343. minor (1–2): Guardian Mnemosyne, „Hüterin und potenzielle Manipulatorin“ (L355); KW2's Mnemosyne-Archipel (L343).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L342, L383, L399, L407, L412, L414, … (9 lines). minor (1–2): an EP with Kiko (L383); grief (L407).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L84. occurrence unless L84's field says more than Kael's amnesia of his multiplicity — then minor (1).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L17, L18, L37, L39, L48, L68, … (7 lines). minor (1–2): the Prologue's setting, „eine prä-existentielle Leere“ (L18).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L612, L623, L656. minor (1–2): only as a possibility, „ein noch unentdeckter Anteil wie Nyx“ (L612).
- **`realitaetsebenen`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Realitätsebene` alone on L829. occurrence: the Fundament as „der tiefsten Realitätsebene“ (L829), nothing said of the page's levels.
- **`rhys`** (central, 3–12 quotations): the census's surfaces — `Rhys` L278, L279, L280, L282, L290, L298, … (35 lines). central (2–4): „Rhys, den Fürsorger-Anteil (ANP)“ (L279) — an ANP here; pure care as insufficient (L884).
- **`risse`** (central, 3–12 quotations): the census's surfaces — `Glitch` L84, L95, L96, L104, L105, L106, … (21 lines). central (2–4): the „Glitches“ of perception (L84); the Riss „als zentrales Symbol für Systeminstabilität“ (L788) and proof AEGIS's control is not absolute (L789).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L16, L28, L59, L682, L722, L885. minor (1–2): a possible integrating instance, hinted (L722); L16, L885.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L478. minor (1–2): the phobias between part types as „Teil der TSDP“ (L478).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — `Überwelt` L18, L79, L750. minor (1–2): `AEGIS-Überwelt` (L18, L79, L750) — what the lines say.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `grenzfeste`: `Die Mauern der Grenzfeste` (near `grenzfeste`). on grenzfeste above.
- `juna`: `Juna/V` (near `juna`). `Juna/V` is how the outline writes Juna (J34) — on juna above.
- `kern-welten`: `Kernwelt 1` (near `kernwelt`), `Kernwelt 2` (near `kernwelt`), `Kernwelt 3` (near `kernwelt`). a reading: Kernwelt 1 (Logos-Prime) „steril, hyper-logisch“ (L86), Kernwelt 2 of emotions and memories (L342), Kernwelt 3 the domain of fear and Cerberus (L611) — read on kern-welten, minor (1–3), by Reader 2.
- `kohaerenz`: `Fehlausgerichtete Kohärenz` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`). occurrence (J9); the misaligned coherence on aegis.
- `logos`: `Logos-Prime` (near `logos`), `Guardian LogOS` (near `logos`). Logos-Prime a world name (J49); Guardian LogOS on logos above.
- `mnemosyne`: `Mnemosyne-Archipel` (near `mnemosyne`), `Guardian Mnemosyne` (near `mnemosyne`). Mnemosyne-Archipel a world name (J49); Guardian Mnemosyne on mnemosyne above.
- `personas`: `Theory of Structural Dissociation of the Personality` (near `persona`). occurrence: the theory's full name, on tsdp.
- `residual-echos`: `Echo` (near `residualechos`). occurrence unless the reader judges the Echo motif (L28, L71) the page's sense — then minor on residual-echos.


**Record entries** (one file each):

- **`q5-guardians-and-kern-welten`**: one Guardian per world — LogOS for KW1 (L150, L162), Mnemosyne for KW2 (L343, L355), Cerberus for KW3 (L611, L624).
- **`c6-guardians-count-and-pairing`**: the same pairing, dated 2025-05-03 — position 1's pairing, three of the five named.
- **`c13-externe-ebene-beyond-the-simulation`**: the Riss as „das erste konkrete Tor“ to the Externe Ebene/Juna/V (L790), the connection to the outside (L788).

**Not promoted:** Echo as a motif (unless on residual-echos), co-consciousness (L719), the phobias between part types, Logik des Gaslichts, the Philo Hints' philosophies.

**Split into two readers, at the same time on disjoint pages:**
- Reader 1: aegis, risse, cerberus, guardians, logos, mnemosyne, emergenz, nichts-rauschen, ueberwelt, externe-ebene, grenzfeste, juna, residual-echos (if read), and the entries q5, c6, c13.
- Reader 2: kael, lex, alex, rhys, kiko, moros, lia, nyx, argus, selene, tsdp, multiplizitaet, kern-welten.
