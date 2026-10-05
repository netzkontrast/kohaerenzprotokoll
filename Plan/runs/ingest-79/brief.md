# Brief — readings from document 79 (step 6)

1 document, one reader, one batch: `ingest-79`. Files go to `Plan/runs/ingest-79/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 79 | `kohaerenz-protokoll-projekt-rekonstruktion` | 2026-03-26 | „the project reconstruction“ | a German audit report dated 2026-03-26 that inventories 16 sources (register Q-01 to Q-16), synthesises the project's state, and generates three „master“ documents inside itself — `CANON STATE` (Hard Canon HC-01 to HC-14, Soft Canon SC-01 to SC-07, physics laws, a decision log, written fragments), `OFFENE FRAGEN` (OQ-01 on) and `SESSION-HISTORIE`; it declares them „die alleinige, verbindliche Architektur“ (L314) |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (328 lines for `kohaerenz-protokoll-projekt-re`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** **An audit that declares itself canon, a month before the reset.** Write „the project reconstruction sets as Hard Canon (HC-NN) / as Soft Canon (SC-NN) / leaves open (OQ-NN) …“ — name the row code, it is the document's own tier. Its claim to be binding (L7, L130, L314) and its date (2026-03-26, before the Struktur-Kanon reset of 2026-04-30): record once on `aegis`, never apply. Its OQ rows are questions, never claims. Glued reference digits mark its sources: cut before them. The two kernel symbols before `-Kernel` are lost in the export (L100–L103): don't quote across them.

## Pages — document 79, `kohaerenz-protokoll-projekt-rekonstruktion`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L7, L28, L31, L37, L53, L55, … (34 lines). central (4–5): the canon claim once (L130, L314); HC-02 no physical destruction, Algorithmische Melancholie (L144); HC-11 pathological learning toward paraconsistent logic (L153); HC-14 not evil but determined, a tragic creator god (L156); SC-01 Kap 38–39, AEGIS integrating Juna's noise, a post-quantum log (L163); the escalation ladder of Act I (L169).
- **`alex`** (minor, 1–4): the census's surfaces — `Alex` L43, L82, L123, L168, L274. minor (1): Der Wächter (Alex), a robust protector (L82).
- **`algorithmische-melancholie`** (minor, 1–4): the census's surfaces — `Algorithmische Melancholie` L144, L223. minor (1): HC-02 (L144); OQ-04 asks whether it means eternal torture for the AI (L223) — a question.
- **`alters`** (central, 3–12 quotations): the census's surfaces — `Alters` L35, L43, L74, L78, L143, L146, … (12 lines). central (3): the 11 primary instances (L78–L90) and SC-06's list (L168): Host, Architekt, Wächter (Alex), Kind (Echo), Analytiker (Lex), Schatten (Nyx), Beobachter (Argus), Vermittler, Erinnerungssäule, Taktiker, Fragment (V); HC-04 all alters welcome, none deleted (L146); `11 primäre` against `11+ Kern-Alters` (L143) — record both.
- **`argus`** (minor, 1–4): the census's surfaces — `Argus` L35, L40, L43, L78, L86, L168, … (9 lines). minor (1–2): Der Beobachter, „Archivar der Narben“ (L86); Silas's role transferred to him (L78, L184).
- **`cerberus`** (minor, 1–4): the census's surfaces — `Cerberus` L67, L89, L166. minor (1): KW3, the Grenzfeste / Cerberus-Labyrinth (L67).
- **`dkt`** (minor, 1–4): the census's surfaces — `DKT` L32, L98. The sweep found `Dual-Kernel-Theorie (DKT)` alone on L32. minor (1–2): DKT at the centre of the narrative physics (L98); SC-02 as a stylistic principle (L164); don't quote across the lost kernel symbols.
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L123. not read unless the line says what emerges: occurrence.
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L5. minor (1): L100–L101 or L176, without the lost symbols; else not read.
- **`genesis`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Genesis` alone on L117. minor (1): the prologue „Genesis im Echo der Leere“, a written fragment (L117, L191).
- **`grenzfeste`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Die Grenzfeste` alone on L67. minor (1): KW3 (L67).
- **`guardians`** (minor, 1–4): the census's surfaces — `Guardians` L72, L152, L166. minor (2): HC-10 the guardians canonically active, capable of doubt, dissent and alliances (L152); SC-04's five (L166).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L7, L33, L55, L90, L101, L118, … (14 lines). central (3–4): HC-09 never described, manifest only through effect — gravity, thermal Risse, longing (L151); HC-13 the Juna/V exploit through entanglement, invisible to a Newtonian-local AEGIS (L155); OQ-01 asks what she is (L201–L206) — a question.
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L5, L28, L33, L41, L43, L53, … (31 lines). central (2–3): HC-01 the unknowing host of a TSDP system with 11+ core alters (L143); HC-03 integration as the weapon (L145); waking after the Universal Reboot in an Oblivion state (L80).
- **`kairos`** (minor, 1–4): the census's surfaces — `Kairos` L68, L166. minor (1): KW4, Kairos-Potentialis (L68); SC-04 Kairos (Integration) (L166).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L31, L61, L282. central (2): the four worlds' names — Logos-Prime, Mnemosyne-Archipel, Grenzfeste / Cerberus-Labyrinth, Kairos-Potentialis (L65–L68); SC-03, the acts tied to KW1, KW2, KW3/KW4 (L165).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L1. not read: title — occurrence (J9).
- **`konstrukt-stadt`** (minor, 1–4): the census's surfaces — `Konstrukt-Stadt` L108. minor (1): KW1 Logos-Prime, a sterile hyper-logical metropolis (L65).
- **`lex`** (minor, 1–4): the census's surfaces — `Lex` L43, L84, L123, L168, L274. minor (1): Der Analytiker (Lex / ANP) (L84).
- **`lia`** (minor, 1–4): the census's surfaces — `Lia` L243, L247. minor (1) or not read: only if a line says more than a name.
- **`logos`** (minor, 1–4): the census's surfaces — `LogOS` L65, L152, L166. minor (1): KW1 under LogOS (L65); SC-04 LogOS (Ordnung) (L166).
- **`mnemosyne`** (minor, 1–4): the census's surfaces — `Mnemosyne` L66, L152, L166, L215. minor (1): KW2, the Mnemosyne-Archipel under Mnemosyne (L66).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L30, L55, L255. minor (1): the Kael–Juna link, internally called „Moonshine-Link“ (L55).
- **`moros`** (minor, 1–4): the census's surfaces — `Moros` L35, L92, L247, L259. minor (1): Moros (EP), the ultimate traumatic shutdown, among the sub-identities (L92); L259 if relevant.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L147. minor (1): HC-05 the ending in a choral We-Voice celebrating funktionale Multiplizität (L147).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L57, L154. minor (1): HC-12 an active information vacuum at the simulation's edge (L57, L154).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L43, L85, L168, L184. minor (1): Die Schatten-Instanz (Nyx / Persecutor) (L85).
- **`oblivion`** (minor, 1–4): the census's surfaces — `Oblivion` L41, L80, L243, L247, L259. minor (1): Kael's amnesia after the reboot as an `Oblivion-Zustand` (L80); L247 as a peripheral alter without a profile; L259 if it says equating Oblivion with Moros was wrong.
- **`rhys`** (minor, 1–4): the census's surfaces — `Rhys` L39, L92, L247, L325. minor (1) or not read: only if a line says more than a name.
- **`risse`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Glitches` alone on L109. minor (1–2): the Landauer principle — repressing trauma generates heat that splits KW1's architecture as „thermische Risse“ (L107, L176).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L35, L92. minor (1) or not read: only if a line says more than a name.
- **`silas`** (minor, 1–4): the census's surfaces — `Silas` L40, L78, L184, L259, L290. minor (2): the decision log — Silas eliminated as skeptic, his traits transferred to Argus (L184), at most kept as a synonym for Nyx; L78 and L259 — record the three wordings (übertragen, eliminiert/Synonym, ersetzt).
- **`sophia`** (minor, 1–4): the census's surfaces — `Sophia` L166. minor (1): SC-04 Sophia (Metakognition) (L166).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L5, L28, L72, L76, L126, L143, … (8 lines). minor (1): the therapeutic isomorphism of the three parts with TSDP's clinical phases (L126).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L33. not read unless a line names the Überwelt's sense: occurrence.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `entropie`: `Entropie-Fehler` (near `entropie`). occurrence: `Entropie-Fehler` (J12).
- `genesis`: `Genesis im Echo der Leere` (near `genesis`). reading, above.
- `grenzfeste`: `Die Grenzfeste / Cerberus-Labyrinth` (near `grenzfeste`). reading, above.
- `kohaerenz`: `Kohärenz Protokoll` (near `koharenz`), `Kohärenz Protokolls` (near `koharenz`), `neue Kohärenz` (near `koharenz`). occurrence (J9).
- `kohaerenz-kernel`: `Kernel` (near `kohaerenzkernel`), `Kernel` (near `koharenzkernel`), `Kernel` (near `koharenzkernelk1`). occurrence: the kernel symbol is lost in the export (L100); don't read.
- `kollaps-kernel`: `Kernel` (near `kollapskernel`), `Kernel` (near `kollapskernelk0`). occurrence: as kohaerenz-kernel (L101).
- `mnemosyne-server-architektur`: `Der Architekt` (near `mnemosyneserverarchitektur`). occurrence: `Der Architekt` is an alter (L81).
- `personas`: `Depersonalisation` (near `persona`). occurrence (J69).
- `residual-echos`: `Echo` (near `residualechos`). occurrence: `Echo` is an alter's name (L83).
- `risse`: `thermische Risse` (near `risse`), `Landauer-Risse` (near `risse`). reading, above (`thermische Risse`).
- `vermittler-stimme`: `Der Vermittler` (near `vermittlerstimme`). reading (1) on `vermittler-stimme` only if the page's subject is an alter that mediates: `Der Vermittler` (L87); else occurrence.


**Record entries:**

- **`c6-guardians-count-and-pairing`**: SC-04, five guardians with their roles (L166); HC-10 autonomous, capable of dissent (L152). Dated 2026-03-26, before the reset.
- **`c11-landauer-warmth-or-cold-ozone`**: the Landauer heat produced by Kael's repression, cracking KW1 as thermische Risse (L107, L176) — heat on the side of repression; and HC-09, Juna manifest through thermal Risse (L151).
- **`q3-how-many-kern-welten-and-alters`**: four worlds (L65–L68); 11 primary alters (L78, SC-06 L168) and „11+“ (L143).
- **`q8-aegis-after-the-vortex`**: HC-02 (L144), SC-01 Kap 38–39 (L163), OQ-04 as a question (L223).
- **`c13-externe-ebene-beyond-the-simulation`**: OQ-01, a question whether Juna is a real person outside the simulation (L205) — say it is open in the document.

One reader writes everything.
