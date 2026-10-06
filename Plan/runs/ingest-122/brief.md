# Brief — readings from document 122 (step 6)

1 document, one reader, one batch: `ingest-122`. Files go to `Plan/runs/ingest-122/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 122 | `ki-roman-architektur-kohaerenz-und-kollaps` | 2026-02-28 | „the architecture report“ (titled `KI-Roman-Architektur: Kohärenz und Kollaps`) | a German report of 2026-02-28 that calls itself „das fundamentale architektonische Regelwerk“ (L15): the two kernels and AEGIS (L31–L39), coherence against correspondence and the Gödel-Gambit (L55–L63), System Kael's eleven parts (L81–L105), a Drama-Engine/NCP software design with a collapse index CSI (L109–L129), three traces (L135–L160), a decision table (L168–L176) and a three-phase plot over Kapitel 1–39 (L182–L186). It closes calling itself a „verifizierte Regelwerk“ (L192) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (217 lines for `ki-roman-architektur-kohaerenz`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A system report: write „the architecture report says / designs …“; its software design (Drama-Engine, NCP moderator, CSI, traces) is its own proposal for an engine, never the novel's world; its claim to be verified (L192) is recorded, never applied. The kernel glyphs K1/K0 are lost in the export (headings „Kernel ()“). Kael is male. Chapter pages are done by the session.

## Pages — document 122, `ki-roman-architektur-kohaerenz-und-kollaps`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L33, L39, L43, L55, L57, L61, … (27 lines). central (3–4): the expansion (find it), AEGIS as the coherence kernel (L33), creating the Kernwelten as closed spaces (L55), relying on the principle of explosion (L63), collapsing in trace 1 into a „Zombie-System“ (L142).
- **`aegis-teilfunktionen`** (minor, 1–4): the census's surfaces — `Zero-Trust` L139. minor (1–2): find its surface's line — read only if it says what AEGIS's sub-function is.
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L91. minor (1–2): an ANP (L89–L92).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L142. minor (1–2): find its line — AEGIS's end state as the report writes it.
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L92. minor (1–2): an ANP (L89–L92).
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `dissoziative Identitätsstruktur` alone on L173. minor (1–2): „dissoziative Identitätsstruktur“ (L173) — what the line says.
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L21, L27. The sweep found `Dual-Kernel-Theorie (DKT)` alone on L21. minor (1–2): the Dual-Kernel-Theorie (DKT) the report builds on (L21).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L160. occurrence unless more: L160.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L23. minor (1–2): L23 and L39 — what the lines say of Entropie.
- **`goedel-gambit`** (minor, 1–4): the census's surfaces — `Gödel-Gambit` L63, L135, L175, L186. minor (1–2): „Das Klimax-Szenario des Romans“ the Gödel-Gambit, which „operationalisiert diese mathematische Schranke“ (L63).
- **`guardians`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Guardians` alone on L184. minor (1–2): L184 — what the line says of the Guardians.
- **`isabelle`** (minor, 1–4): the census's surfaces — `Isabelle` L101. minor (1–2): an EP (L98–L101).
- **`juna`** (minor, 1–4): the census's surfaces — `Juna` L121, L148, L149. minor (1–2): in the NCP's Influence Character slot as `Juna/AEGIS` (L121) and in trace 2 as „Der Spieler (oder das System Juna/V)“ (L148), using the Moonshine-Link (L149) — the report does not say which is meant.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L39, L57, L61, L63, L77, L79, … (22 lines). central (2–3): fragmented „in elf spezialisierte Subsysteme“ (L81), „Der primäre ANP“ (L89); his striving for integration accepts the entropic pressure (L39); functional multiplicity, „simultan als Eins und als Viele“ (L63); integrating Moros in trace 3 (L160); waking in Logos-Prime (L182).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L55, L105, L186. minor (1–2): AEGIS creates the Kernwelten as closed spaces (L55); Logos-Prime as KW1 (L182).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L99, L151. minor (1–2): an EP (L98–L101).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L15. not read: the title — occurrence (J9).
- **`kohaerenz-kernel`** (minor, 1–4): the census's surfaces — `Kohärenz-Kernel` L29, L43. minor (1–2): „repräsentiert die zugrunde liegende Struktur reversibler Berechnungen“ (L31), embodied by AEGIS (L33).
- **`kollaps-kernel`** (minor, 1–4): the census's surfaces — `Kollaps-Kernel` L35. minor (1–2): „die aktive, anti-algorithmische Domäne der irreversiblen Berechnung“ (L37).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L90, L116, L129, L140, L157, L159. minor (1–2): an ANP (L89–L92).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L99, L151. minor (1–2): an EP (L98–L101).
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L184. occurrence: `Logos-Prime` is KW1's world name (J49) — read on kern-welten; LogOS only if a line names the Guardian.
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L184. occurrence: `Mnemosyne-Archipel` a world name (J49).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L144, L149, L176. minor (1–2): trace 2, „Juna nutzt den“ Moonshine-Link (L149).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L100, L160. minor (1–2): „Moros repräsentiert die existentielle Leere“ (L100); integrated in trace 3 (L160).
- **`mosaik-herz`** (minor, 1–4): the census's surfaces — `Mosaik-Herz` L186. minor (1–2): Phase III, „Die Existenzielle Fusion und das Mosaik-Herz“ (L186).
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Multiplizität` alone on L63. minor (1–2): „funktionalen Multiplizität“, Eins und Viele (L63); L63 sweep.
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L39, L182, L184. minor (1–2): „einen Zustand hoch-entropischen Potenzials, aus dem AEGIS einst entflohen ist“ (L39); L184.
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L98, L140. minor (1–2): an EP (L98–L101).
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L91. minor (1–2): an ANP (L89–L92).
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Risse` alone on L39. minor (1–2): the rifts as „die einzige Verbindung zur objektiven Wahrheit“ (L39); Phase I's anomalies as faulty corrections (L182).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L103, L105, L140, L151. minor (1–2): „Sie fungiert als Integratorin“ (L105).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L81, L173. minor (1–2): the TSDP mapping of the parts (find its lines).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L71. not read: `Simulation` in passing (L71) — occurrence.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cerberus`: `Cerberus-Labyrinth` (near `cerberus`). J49: `Cerberus-Labyrinth` a world name — occurrence.
- `coheron`: `Coherons` (near `coheron`). occurrence unless a line says what Coherons are.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Zielkohärenz` (near `koharenz`), `Kohärenztheorie` (near `koharenz`). occurrence: the title; `Zielkohärenz` and `Kohärenztheorie` the report's and borrowed terms.
- `multiplizitaet`: `funktionalen Multiplizität` (near `multiplizitat`). a reading — on the page above.
- `risse`: `Rissen` (near `risse`). `Rissen` — on risse above.
- `thermodynamischer-phaenomenalismus`: `Phaenomena` (near `thermodynamischerphaenomenalismus`). occurrence: `Phaenomena` is a name of the engine's design, not the page.


**Record entries** (one file each):

- **`c1-aegis-expansion`**: the expansion „Autonomous Entropic Gatekeeper for Integrity Systems“ — find its line; position 1 again.
- **`q3-how-many-kern-welten-and-alters`**: „in elf spezialisierte Subsysteme“ (L81): ANPs Kael, Lex, Alex, Rhys, Argus; EPs Nyx, Kiko, Lia, Moros, Isabelle; Selene the integrator (L89–L105).
- **`q8-aegis-after-the-vortex`**: in trace 1 AEGIS „stürzt ab“ into a „Zombie-System“ (L142) — a trace of the engine design, dated 2026-02-28, before the author's answers.
- **`q9-moonshine-link-boundary`**: trace 2, the player or Juna/V using the Moonshine-Link (L148–L149).

**Not promoted:** the Drama-Engine, NCP moderator, CSI and its threshold, AutoCompanion, Player-Dilemma, Akka — the report's engine design; the coherence and correspondence theories; Zombie-System — on aegis and Q8.

**Split into two readers, at the same time on disjoint pages:**
- Reader 1: aegis, kohaerenz-kernel, kollaps-kernel, dkt, nichts-rauschen, risse, entropie, goedel-gambit, algorithmische-melancholie, juna, moonshine-link, aegis-teilfunktionen, guardians, did, and the entries c1, q8, q9.
- Reader 2: kael, multiplizitaet, mosaik-herz, tsdp, lex, alex, rhys, argus, nyx, kiko, lia, isabelle, moros, selene, kern-welten, and the entry q3.
