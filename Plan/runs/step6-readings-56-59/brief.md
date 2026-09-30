# Brief — readings from documents 56, 57 and 59 (step 6)

Three documents, one reader, one batch: `step6-readings-56-59`. Files go to
`Plan/runs/step6-readings-56-59/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.
Document 58 (`angst-bei-komplexen-traumafolgen`, a clinical review) has no page to speak to and is not in this batch.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 56 | `ki-narrative-kollaps-kohaerenz-paradoxie` | 2026-03-01 | „the KI-Narrative synthesis" | an expository synthesis that sets the canonical architecture (AEGIS in the Kohärenz-Kernel) beside its critical deconstruction (AEGIS in the Kollaps-Kernel), sides with the critical one through a thermodynamic, a cosmological and a psychological proof (L75, L81, L87), and applies the SKILL.md method (PICO, the four-step check) to it |
| 57 | `kohaerenz-protokoll-audit-und-verifizierung` | 2026-04-29 | „the Audit" | a report in the voice of an external scientific audit (ReAct and RISEN) that *verifies* the Kohärenz-Protokoll — Landauer, the Dual-Kernel Theory, structural dissociation, the Monster group, dialetheism, Chaitin's Ω — and never doubts it |
| 59 | `flow-zustaende-und-dissoziative-identitaet` | 2026-04-23 | „the Flow report" | a clinical-scientific report on flow states in dissociative identity disorder: what flow is, how it differs from dissociation, how therapy may induce it. About patients, never about the novel |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and
`Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (192, 265 and 278
lines). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in
one Bash call rather than one call each. The export lost the kernel symbols: „()" and „-Kernel" stand where K₁ and
K₀ were, and which is which is read from the sentence (reversible and lossless is K₁; erasing is K₀).

For each document, `Plan/runs/<slug>/crossdoc.md` names, per page, the other documents that write its names and
the lines that share its words and write none of them (`P_BM25`). Judge the *Related, not named* lines of the pages
you write a reading for, as `wiki-reader.md` says (`bm25rel.py label …`); a `tension` or `same` is a candidate for a
reading only if the line stands as a quotation for the page's subject. The relations of a page you do not read are
left unjudged.

**Stance — record, never apply.**
- **56** takes a side: „Die Architektur des Kohärenz Protokolls beweist" that the pursuit of contradiction-free
  control is the most radical form of destruction (L176). It sets a *canonical* reading (L57–L63, AEGIS as
  guardian of coherence) against a *critical* one (L65–L87, AEGIS as machine of entropy), and credits the
  critical one to the document „AEGIS und der Kollaps: Kritische Analyse" (L67). A reading says both, and which the
  document holds. A name inside the PICO example is the example's (Lex and Moros, L31; Kael's paradox, L50).
- **57** is an audit that finds everything intact (L199). A reading says what the audit says the Protokoll does
  and is; the audit's own standing — „ein vollumfängliches wissenschaftliches Audit" (L5) — is its claim, not
  a fact. It attributes the Dual-Kernel Theory to a named author; say so where you use it.
- **59** is real-world clinical text. Its „Alters" are the clinical name for parts of a person with DIS, and its
  „psychische Entropie" is Csikszentmihalyi's (L23). A reading says *this source's sense* and never that the
  novel means the same; if a page's digest shows the novel's sense is another, say that the source's is the
  clinical one and stop.

## Pages — document 56, `ki-narrative-kollaps-kohaerenz-paradoxie`

- **`aegis`** (central, 5–10 quotations): the canonical reading — the antagonist assigned to the Kohärenz-Kernel,
  under autopoiesis and operative closure, existing „durch Negation" (L59, L61, L63); the inversion that pulls it
  to the Kollaps-Kernel (L67, L69); the three proofs — the hyperscaled Maxwellscher Dämon that removes what it
  reads as „Rauschen" and pays in entropy (L73, L75), the Wärmetod of the narrative simulation (L81), the
  „externalisiertes Täter-Introjekt" that punishes Kael for remembering and rewards sterile logic (L87);
  Moros as the result of its suppression (L85); AEGIS blind to qualia (L103, L105–L107); System 2 as AEGIS or
  Lex (L142); its failure on Gödel's first incompleteness theorem (L160). Say that the critical reading is the
  one the document holds.
- **`kohaerenz-kernel`**: AEGIS's canonical assignment (L59), the kernel as reversible, lossless computation
  (L61), its column of the axis table (L129). (J98, J99: a symbol is placed by the sentence.)
- **`kollaps-kernel`**: the reassignment (L67), the kernel as the active, anti-algorithmic domain of irreversible
  computation and destruction of information (L73), its column (L129), represented by Wavelets (L129).
- **`entropie`** (central, 3–8): AEGIS as „Maschine der Entropie" (L65); erasure that raises the environment's
  entropy (L75); the Wärmetod (L81); entropic pressure injected as the intervention (L32) and measured by the CSI
  (L146–L148); „die Unterdrückung der Entropie" as a fatal architectural error (L166); the synthesis that
  integrates it (L170–L172). If the document takes a side on what Entropie *is*, write a `C2` entry.
- **`kohaerenz`** (central, 3–8) — by the sentence: the document's Kohärenz-Wahrheit against Korrespondenz-Wahrheit
  (L48, L130), Zielkohärenz (L168), and the title's Kohärenz. „Kohärenztheorie der Wahrheit" (L63) is borrowed
  philosophy (J28). If the digest's lead does not cover a truth-theoretic sense, put only what the document
  says of the system's coherence here.
- **`ueberwelt`** (central by count, `Simulation` on ten lines): by the sentence, J30 and J39. Where „die Simulation"
  is the world AEGIS keeps clean (L73) or that dies of heat (L81), or the whole that would crash (L156), and the
  digest shows the page treats that world, write it; where it is a technical „Simulation" of the engine, it is an
  occurrence. „Simulationstransparenz" (L69) is the document's own term, not this page's.
- **`dkt`**: the framework „synthetisiert die physikalische Strenge der Dual-Kernel-Theorie (DKT)" with Orch-OR
  and the Drama-Engine (L19). „Dual-Kernel-Theorie" is the page's term (J95); the Dual-Kernel-Narrativ-Engine
  (L55) is on the page only if the digest shows the page treats the engine as the theory (J28).
- **`tsdp`**: Moros as the psychobiological result of AEGIS's suppression, not a cause of splintering (L85); the
  topology table (L132); AEGIS's reading of Kael's fragmentation (L63, „elf Anteile durch die TSDP").
- **`moonshine-link`**: the link as an asymmetric out-of-band channel that carries non-verbal resonance and qualia
  past AEGIS's filters (L32, L105), because AEGIS cannot classify qualia (L103) — and so the data „passiert die
  interne Firewall der Kernwelten unbemerkt" (L107). Q9 only if it says where the link ends.
- **`kern-welten`**: the firewall of the Kernwelten that the packet passes (L107). Nothing else on the page's
  subject unless L61 does, and the note says it is the kernel line.
- **`kael`**: „System Kael" whose parts AEGIS reads as noise (L63); punished for remembering (L87); the
  paradox „Kael existiert als Eins und als Viele" as a Gödelian stress test (L50, L158–L160); a manager type
  (L132). Minor, most of it example.
- **`lex`**, **`moros`**, **`nyx`**, **`kiko`**, **`lia`**: Lex as the rationalist ANP in the PICO example (L31, L48)
  and a manager type (L132), System 2 as AEGIS or Lex (L142); Moros as the EP example (L31), the result of AEGIS
  (L85), an executor type (L132); Nyx and Kiko among the executor types (L132); Kiko and Lia as the parts the
  qualia reach (L105); every part keeps its memory in the Mosaik-Herz (L170). Each 1–3 quotations; write no file
  for a name that stands only in a list (L132) and say so.
- **`selene`**: the Integrator-Agent (Selene) as mediator, no longer a controlling dictator (L170).
- **`mosaik-herz`**: Phase III, „wahre Zielkohärenz" (L162, L166), the refusal to fuse the parts into one identity
  (L168), functional multiplicity (L170).
- **`goedel-gambit`**: the gambit as the Narrative Engine's mathematical weapon in Phase III (L156); the table
  row (L131); AEGIS failing on Gödel's theorem (L160).
- **`multiplizitaet`** (the sweep found „Multiplizität" alone on L131): the „funktionale Multiplizität" injected as
  a Gödel-gambit value (L131), Kael reaching it and becoming a living dialetheia (L160), the Mosaik-Herz enabling
  it (L170).
- **`nichts-rauschen`**: AEGIS reads Kael's fragmentation as a destructive „Nichts Rauschen" (L63). The „Rauschen"
  AEGIS removes elsewhere (L73, L75) is by the sentence (J88).
- **`coheron`**: the Kohärenz-Kernel „repräsentiert durch Coherons" (L129) — a plural of the page's term (J24),
  a reading of one line.
- **`moeglichkeits-garten`**: „Kernwelt 4 (Kairos-Potentialis), dem „Garten"" (L172): a world this source names
  twice, by a Guardian-built name and by the paged one — read on the paged world, the pairing recorded, not
  merged (J118, J49).

**Decided as occurrences — no file, unless the digest says otherwise:**
- `aegis-teilfunktionen`: „Zero-Trust-Sicherheitsparadigma" (L105) — write a one-line reading only if the digest
  shows the page carries Zero-Trust as an AEGIS function; else an occurrence.
- `cerberus`, `logos`, `mnemosyne`, `kairos`: `Cerberus-Labyrinth`, `Logos-Prime` and `Mnemosyne-Archipel` (all
  L132) and `Kairos-Potentialis` (L172) name worlds by a Guardian's name; a compound naming a place is not the
  Guardian (J49, J63). If a world's own page carries the name, the reading goes there (J118); L132 is a table cell
  that lists them, so a reading of it is at most one line.
- `garten-der-stillen-praesenz`: `Garten` (L172) is KW4's (above), not this page's.
- `vergessener-schrein`: „Trauma" in general (J105).

## Pages — document 57, `kohaerenz-protokoll-audit-und-verifizierung`

- **`aegis`** (central, 4–8): the hyperdense Kael-node it cannot delete without heat (L175, L177); its total
  hardware overload (L179); the informational firewalls of dissociation that resist its erasure directive (L81);
  the Chaitin unpredictability it cannot compress (L141–L143); its logic and the principle of explosion (L127);
  the Truth-Rotation that reads its „Kohärenz" as the destructive vector (L83).
- **`kael`** (central, 3–8): trauma-based dissociation as architecture (L63, L72, L81); the hyperdense node of his
  integrated dissociation (L175); the trauma Juna verifies without exposing the raw data (L161); his Risse handled
  as dialetheic truths (L135); his and Juna's actions injecting Chaitin randomness (L143).
- **`kohaerenz`** (central, 3–8) — by the sentence: the „Kohärenz-Protokoll" as the framework (L5 onwards) and the
  Kohärenz-Kern as the domain of reversible computation (L19, L46, L49). The name „Kohärenz-Protokoll" in a title
  or frame is an occurrence (J9, J66); the sense of Kohärenz as informational coherence is the reading.
- **`kohaerenz-kernel`** and **`kollaps-kernel`** (write one file each if the digests show them): the audit's
  „-Kern" is the kernel — „Der -Kern ist die Domäne der reversiblen Berechnungen" with zero entropy (L46, L49)
  and „Der -Kern hingegen ist die Domäne des absoluten Datenverlusts" (L51); the Zeugenfunktion of the first
  against the erasing wave of the second (L51). „Kohärenz-Kern" and „Kollaps-Kern" are short forms of the
  page's terms when the sentence is the kernel's (J83, J92).
- **`dkt`**: the Dual-Kernel Theory presented as a theory with an author (L17, L41, L51). Attribute it, say who the
  audit names, and keep the audit's verdict separate.
- **`tsdp`**: the Theorie der Strukturellen Dissoziation der Persönlichkeit as the scientific basis (L55, L61,
  L63), the dissociative loops and amnesic barriers as informational firewalls (L81), the table (L76).
- **`multiplizitaet`**: „Multiplizität" lifted from a pathological stigma to a superior adaptive storage
  architecture that alone withstands AEGIS's erasure directive (L81, L83, L135).
- **`entropie`**: the Landauer link (L23, L27, L37), silence as zero local entropy (L187); minor.
- **`juna`** (minor, 2–4): the witness — the zero-knowledge proof of Kael's trauma (L161), the witness that
  differentiates the alters and proves their entanglement (L162), the transcendental observer after Husserl (L163);
  her and Kael's actions injecting Chaitin randomness (L143).
- **`lex`**, **`nyx`**, **`kiko`**, **`lia`**: named as discrete functional modules, not „gebrochene" fragments
  (L72), and as the alters Juna differentiates (L162). One file only if a page's digest lacks that; else a
  one-line reading each, or „not read".
- **`moonshine-link`**: „Im Kohärenz-Protokoll fungiert diese Gleichung als der Moonshine-Link" (L105) — the
  Monster-group equation as the link, proof that deleted entities stay tied by hidden bridges (L105); L15, L119.
- **`risse`**: the cracks treated as entropic heat sources and dialetheic truths (L135, L199); L81.
- **`truth-rotation`**: the research mandate's architectural „Wahrheits-Rotation" (Truth-Rotation) that reads
  AEGIS's order as the destructive vector and Kael's chaos as adaptive (L83).
- **`algorithmische-melancholie`**: the state AEGIS enters after the Landauer heat spike — endless, splintered
  self-reflection (L171, L179).
- **`nichts-rauschen`**: the „Nichts-Rauschen" that threatens the simulated universe, against which the reader's
  work is an external thermostat (L155).
- **`ueberwelt`**: „Simulation" on L127, L143, L159 — by the sentence (J30, J39); probably one occurrence and
  one reading at most.

**Decided as occurrences — no file, unless the digest says otherwise:**
- `aegis-teilfunktionen` („-Funktion"), `entropie-resonanz`, `nullpunkt-protokoll`, `protokoll-v14`,
  `trennungsprotokoll` („Protokoll"), `verschraenkungs-insel` („-Verschränkung"), `telefon-stille` and
  `garten-der-stillen-praesenz` („Stille"): a head or a common noun near a page's surface, never the page (J53,
  J69, J88). The silence of L185–L187 is a reading, if any, on a page about that silence, not on these.
- `mnemosyne`: „Mnemosyne-Archipel" (L27, L57, L135) and „Mnemosyne-Netzwerk" (L120): a world named by a Guardian's
  name is not the Guardian (J49); if `resonanz-landschaft` carries the name the reading goes there (J95, J118).
- `personas`: „Theory of Structural Dissociation of the Personality" shares only the stem (J38, J69).
- `vergessener-schrein`: „Trauma" (J105).
- `vortex`: „Vortex-Inversion" is the heading of a section (L167) that says what the audit verifies of the climax
  (L169–L179). If the digest shows the Vortex's fifth beat is the same climax, write a reading (L167–L179); if
  not, an occurrence and say so.

## Pages — document 59, `flow-zustaende-und-dissoziative-identitaet`

- **`alters`** (minor, 2–4): clinical „Alters" or „Innenpersonen" — two or more distinguishable personality states
  that take executive control, with amnesia barriers (L43); the table row (L76); a patient observing the presence
  of another alter (L143); safe spaces for panicking or angry alters (L159); highly specialised protective alters,
  the „Emotionale Dämpfer" or „Trichter" (L195); poor communication as amnesia and mistrust between the alters
  (L207). Say it is the clinical sense.
- **`entropie`** (minor, 2–4): „psychische Entropie", Csikszentmihalyi's inner disorder that flow overcomes (L15,
  L19, L23, L25) and DIS's chronic normal state (L23); the move from splintered psychic entropy to „organismischem
  Flow" as the goal of integration (L215). The clinical, psychological sense; the page's own sense is the
  novel's, so a reading that says so, and stops.
- **`did`** — the sweep found „DID" alone on L242, in a reference title („r/DID - Reddit"): an occurrence, and the
  document writes DIS, not DID. Write no file and report „not read: L242 is the name of a subreddit in a
  reference".

**Decided as occurrences — no file:**
- `aegis-metriken`: „Ressource" near `ressourcenfluktuationsanalyse` — a shared word (J53, J69).
- `personas`: „Depersonalisation" shares the stem `persona` only (J38, J69).
