# Now

*What is open, and what a person still has to decide. **No counts live on this
page.*** Numbers come from `python3 scripts/state.py`; the few that appear in
prose here carry a `<!--state:key-->` marker and `--prose` fails if one drifts.

```bash
python3 scripts/state.py            # everything, derived now
python3 scripts/state.py --prose    # fail on any stale number in this file
```

## Questions for the author — noted, not waited on

**The author's instruction, 2026-09-24: „Notiere in Zukunft einfach deine Fragen
und setze fort"**, and the same day: „Sammle alle Fragen und fahre fort". Every
open question is collected here, with where it came from; the work continues.
When an answer arrives it is recorded where the question lives (a conflict
record, a `Wiki/questions/` page, a decision file) and the line here goes.

**Decided so far:** **C6** — five Guardians (LogOS, Mnemosyne, Cerberus, Kairos,
Sophia). **C9** — the Konstrukt-Stadt is KW1. **Decision 006** — every draft is
back in question; no date or claim to be canon settles anything. **Narrative
texts among the unread sources** (2026-09-26) — „Those arent Texts for the novel -
only Research": read as research, never as the novel's prose.

And the two read ones with them: „Yes, 22 and 23 are research too" (2026-09-26).
`CLAUDE.md`, `aegis`, `aegis-metriken` and the two reconciliation records had called
them the novel's text, and were corrected; the readings quote what they say and stand.
A document may still call itself a draft, and a reading may quote that.

**The parked September draft, 2026-09-29:** „The novel in Legacy is Not the quality I
want". So revising it in place is off the table. Its prose is never a voice reference
for the book. Whether its ideas come back as research is question B below.

**The plot, 2026-09-29:** „I dont Like that the novel does Not Flow Like a scifi novel - i want
more Action - its a question of the Plot". In the plan, W2 (the engine) now opens round 1, framed
as what drives the plot as action. Every treatment paragraph must show a physical event, and the
treatment gains an escalation ledger per act (the plan, §5).

### Writing the novel — a plan, proposed 2026-09-29

On the author's „Think about how to Write the novel and come up with a plan":
`Plan/concept/novel-writing-plan_2026-09-29.md`. Nothing in it is decided.

**The plan in brief:**

- **Decide.** Sixteen load-bearing decisions (the Weichen, W1–W16) go to the author in
  four rounds of four.
- **Tell.** The story is told plainly and approved act by act: one page, then one
  paragraph per movement.
- **Write.** Chapters are written one at a time, each from a derived brief, read by the
  writing skills and cold, and revised until the author approves it.
- **Pilot.** Kap 1–3 go first, by hand. Tools are built only from what the pilot used.

**Four questions come first** (its §11 has the options, the case for and against each,
and the recommendation):

- **A — Who writes the prose?**
  - *Options:* the session whole chapters (A1); scene by scene on beats the author
    approved (A2); the author, with the skills critiquing (A3).
  - *Recommended:* not A1, given the verdict above. Kap 1 by A3, Kap 2 by A2, and Kap 3
    by whichever the author prefers.
- **B — The September draft's ideas.**
  - *Options:* land its premise and drafting record as research, with the 41 chapter
    files staying parked (B1); leave all of it parked (B2).
  - *Recommended:* B1. Doran, `A-0001` and the Gegenregister live in that record.
- **C — Where the book lives.**
  - *Options:* a new top-level `Novel/`, created with its first decision (C1); inside
    `Wiki/` (C2); a repository of its own (C3).
  - *Recommended:* C1.
- **D — Reading on demand while the book is written.**
  - *Options:* allowed for the chapter in hand (D1); each document on the author's yes
    (D2); no reading until the first draft (D3).
  - *Recommended:* D2. It keeps the author's word of 2026-09-28 intact.

**The writing skills are installed and adapted**, on „Install
https://github.com/netzkontrast/writing-skills/tree/main into this repo" and „But
optimieren ihn für dieses repo":

- thirteen skills from upstream, with `writing-skills` as their entry point, in
  `.agents/skills/`;
- German rules in `copy-editor`;
- canon is the author's decisions, never the wiki's readings;
- findings go under `Plan/runs/writing/`.

**One smoke test ran**, of `copy-editor` on the parked Kap 1 (L48–210):
`Plan/runs/writing/legacy-kap-01/copy-editor_2026-09-29.md`. It tested the adaptation, not
the book.

- **It kept the rules.** All 28 of its quotations match their lines, it supplied no rewritten
  sentence, and it recorded the three locked lines without flagging them.
- **It found real things in the text:** every closing quotation mark typed as `"`; 204 floor
  plates to the first junction but 130 at the data node; „das Klick" against the Duden's
  „der Klick".
- **It found five defects in the adaptation**, all fixed the same day:
  - two contradicting instructions on a locked dash;
  - § numbers the repository cannot look up, now cited by subject;
  - no guidance on a capital after a colon in mixed cases;
  - the typewriter `"` not anticipated;
  - no output path for a test target.
- **It called the author „die Autorin"**, a gender nothing had stated. The artifact now
  addresses the author as „du", and `writing-skills` rule 5 requires that of every run.

**The W2 sheet is prepared, 2026-09-29:** `Plan/weichen/w2-motor.md`, in German. It has three
options and a free-text way:
- A: F1 as written, Kael's job as the motor;
- B: journey, break-in and flight, from the Hard-SF-Outline;
- C: the erasure as the opponent, with a visible clock, after Hamilton — new, built from F1's
  Wartungsfenster and the Timelock.

It recommends C, with A as the work inside it. All 20 cited quotations resolve (`quotes.py`
on the file). No document was read.

**Round 1 prepared, 2026-09-30, on the author's “Dann tue das”:**
`Plan/weichen/w1-theorie.md`, `w3-stimme.md` and `w4-form.md` now stand beside
`w2-motor.md`. Each records options, gains, costs, a recommendation and its
dependencies; none is a decision. No new research document was started.

`Plan/concept/treatment-probe_2026-09-30.md` makes the recommendations concrete:
a conditional causal story, an escalation line and opening movements. Its
events are marked new, not attributed to the sources or adopted as canon.
It assumes W1 B, W2 C with A, W3 A and W4 C; alternate answers change the probe.
The old prose remains parked and no NCP value was changed.

**W5–W10 prepared, 2026-09-30:** the six sheets in `Plan/weichen/` cover sensorics,
AEGIS perspective, reader knowledge, Act-II spaces, Juna and cast. Each separates
source positions, recommendations and independent answer fields. Their Dual-Storyform
reading distinguishes throughline bearer, narrative perspective and grammatical person.

**PR #113 incorporated:** the merged Gutachten and five plot research files are on
this branch. `Plan/concept/antwort-pr113_2026-09-30.md` records the response, its evidence
limits and concrete plot questions. W5–W10 now also ask about reactive opposition,
personal loss, the enacted Ich/Wir transition and an event-driven middle. The
Gutachten is a sample-based diagnosis of the parked draft, not a full-book verdict.

**Next:** the author reviews W1–W10 and the conditional probe. Record answers once,
then revise the probe around observable goals, requirements, consequences and both
clocks. W11–W16 and process questions A–D remain open. No new document ingest,
manuscript rewrite or NCP promotion was performed.

**New from the last eight canon-era documents (2026-09-27, documents 32–39, all English, all 2026-05-08):**
- **The Guardian-world pairing, again, on the canon's date.** The Narrative Building Blocks report makes
  LogOS, Mnemosyne and Cerberus the carriers of KW1, the Mnemosyne Archipelago and „The Cerberus Labyrinth
  (KW3)", and the Systemic Architecture Specification names the four worlds Construct-City (Logos-Prime),
  Mnemosyne-Archipelago, Cerberus-Labyrinth, Kairos-Potentialis — while it and two others keep two
  Guardians. Recorded in Q5 and C6; your decision for five stands.
- **Throughline domains disagree between documents of one date**: the Plot/Outline Mining-Report puts
  OS-A in Physics and OS-B in Mind, the Systems Narrative Analysis OS-A Psychology and OS-B Physics. On
  the pages; no record. A record for the domains?
- **Where Functional Multiplicity is reached** has a fourth answer — the Vortex (Companion Guide's fifth
  beat, the Systems Narrative Analysis' fourth point) beside Kap 33 and Kap 39. A record?
- **The Nichts-Rauschen as K0** in the Narrative Building Blocks report (its L100) against every other
  source's K1 union; **Juna's presence as cold** in the Plot/Outline Mining-Report (L37). On the pages.
- **`aegis-teilfunktionen`**: a source now explains two of its four functions; whether to split the page
  is open.

**New from the philosophischer Bericht (2026-09-27):**
- **AEGIS' voice, a new position on C14.** The document gives AEGIS the first person in all of
  Storyform B, collapsing to the third in the Vortex (its L292, L627), and, under the alter table,
  „AEGIS und Guardians in der 3. Person" (L507) — two rules it does not relate. The record holds both.
- **`RIVE`.** A fifth earlier Wächterprogramm beside LogOS, Cerberus, Kairos and Sophia (L296) —
  Mnemosyne not among them. No other read document names it; 27 landed documents do. A page, or a
  record beside C6, once a document that defines it is read?
- **The Überwelt inside the four worlds.** KW3 is „Überwelt / Nexus" and KW4 „Die absolute, externe
  Ebene" (L437–443), where earlier sources count the Überwelt and the Externe Ebene beside KW1–KW4; KW2
  is „Grenz-Zonen", and Akt III opens with KW3 (L447). On the pages and in Q3/Q5; a record of its own?
- **Who brings the paradox in the Vortex.** Here AEGIS confronts Kael with it (L611); every other read
  source that says so has Kael bring it. On `goedel-gambit`'s differ section; no record.
- **Is AEGIS conscious?** „eigene Innensicht" (L247), „stumm zusehenden Bewusstsein" (L284) — against
  the ki-prompt analysis' „Es hat kein Bewusstsein". Not a record.
- **`atemporalitaet`'s lead** says atemporality is why AEGIS cannot see Juna; this document gives
  three other reasons (operational closure, zero-knowledge, Chaitin; L262, L322, L339). The lead is
  unchanged — reword it?

**New from the Kap-25 session log and chapter file (2026-09-26):**
- **The drafting run's six open decisions, OQ-25-A…F, are addressed to you** (the log's L55–60):
  when AEGIS is named to the reader after the naming lock of Kap 1–13, and when its log format
  starts; where the veil sentence „Hier sitzt mehr als einer." goes (Kap 25 mid-scene, the
  dwelling, or Kap 26); whether the click's local absence in Kap 25 anticipates Vortex 1 Beat 3;
  the header's three scenes against the prose's seven (the chapter file has seven breaks, eight
  parts); whether the unit at Station 7 carries on into Kap 27/28. **The largest is C9's**:
  Akt II's drafted chapters all play in the Konstrukt-Stadt while the canon it cites gives 14–22
  to KW2 and 23–28 to KW3 — „Filterregime statt Ortswechsel", or a pass that moves them? Your
  decision (the Konstrukt-Stadt is KW1) stands and the record holds both.
- **Two things the log states that the corpus does not bear out:** it calls Cerberus, Nox, Echo
  and Limina „dekanonisierte Guardians" (L39), where read sources have Nox, Echo and Limina as
  Alters and Cerberus is one of your five; and it says the Sprach-DNA provides AEGIS' log format
  „ab Akt II", which neither landed Sprach-DNA document says. Recorded as its claims.
- **Kap 25 in two plans:** the strukturierter Outline's Kap 25 has Kael suspect that 734 is an
  address or a name; the chapter file's Kap 25 renders no such thought. On `kap-25`; no record.

**New from the philosophy catalogue (2026-09-26):**
- **Three differences its readers found, none yet a record.** Where Funktionale
  Multiplizität is reached: only Kap 39 here („Plurale Apotheose“, L735), Kap 33 in the
  master report and the worldbuilding concept. When the Wir decides to stay: Kap 39 in its
  text (L459), Kap 38 in its own table (L733), Kap 38 Beat 5 elsewhere. The Cache-Konflikt:
  Kap 6's in its table (L699), in Kap 18's title in the Konzept-Iteration Genesis and the
  konsolidiertes Konzept. Should any become a conflict record?
- The Witness-Funktion and the Suppressionsprotokoll, under the question below, are now
  named by one more read document each.

**New from the worldbuilding concept (2026-09-26):**
- **Pages for terms every reading has left unpaged?** The Erasure-Pol is named in 14
  read documents, the Witness-Funktion in 8, the Fragmentierungsnacht and the
  Ursprungs-Ich in 7, the Suppressionsprotokoll and the Korrelat-Achse in 5, and none
  has a page. Each reading so far has left them off; should any become a page?
- **`datenverarbeitungsknoten-7g` or Epsilon?** Only the 2025 Lokalitäten document
  writes `7G`; every 2026 source read writes `Datenverarbeitungsknoten Epsilon`, and
  J65 already treats the two as Kael's one workplace. Rename the page?
- **Rhys' arc.** „Anker Akt I → Kudzu Akt II“ in the worldbuilding concept (L402) and the
  konsolidiertes Konzept, „Akt-II-Anker → Kudzu“ in the master report of the same date.

### The novel — where the sources disagree

Each is a conflict record in `Wiki/conflicts/`, append-only, with the quotations.

| | question | the positions (source, date) |
|---|---|---|
| **C1** | What does AEGIS stand for? | *Autonomous Entropic Gatekeeper for Integrity Systems* (`entropie-aegis` 2025-04-17; konsolidiertes Konzept 2026-05-08) · *Autogenic Emergent General Intelligence System* and *Autonomous Entropic Generative Integrity Substrate* (`aegis-emergenz-aus-der-leere` 2025-04-19) |
| **C2** | What does `Entropie` mean in the novel? | disorder AEGIS fights (`entropie-aegis`) · „schöpferische Matrix", the space things arise from (reported by `aegis-emergenz-aus-der-leere` as a postulate's) · AEGIS *is* the entropy it fights (konsolidiertes Konzept) |
| **C3** | Where does AEGIS come from? | from nothing, before reality (`aegis-emergenz-aus-der-leere`) · from inside the simulation's dynamics (`kohaerenzprotokoll-aegis-und-systementropie`) · from Kael's defence in the Genesis, then became the world (konsolidiertes Konzept) · out of fragments in the void, clusters locking at the Klick, before any world — Kael its remainder (draft text of Kap 0, 2026-05-08) · out of clusters in the void again, and `Emergenz` used once, for the stranger (annotated draft of Kap 0, 2026-05-17) |
| **C4** | Whose is the blind spot — AEGIS' alone, or each Guardian's? | AEGIS' categorical blindness (`kohaerenzprotokoll-aegis-und-systementropie`) · five Guardians, five blind spots (`guardians-und-kern-welten-konzept`) |
| **C5** | Is the Möglichkeits-Garten a whole Kern-Welt or a place inside KW4 — and what is KW4 called? | a Kern-Welt (`guardians-und-kern-welten-konzept`; storyform-und-outline 2026-06-10) · a location in KW4 (`roman-lokalitaeten-konzept-und-ausarbeitung`) · both: KW4 „Kairos-Potentialis (Garten der Möglichkeiten)" with a Möglichkeits-Garten inside it (konsolidiertes Konzept) · KW4 named „Möglichkeits-Garten“, the whole world, no place inside it (Sprach-DNA (2026-05-13)) · KW4 is the Möglichkeits-Garten, the whole world, a logical regime and no place (konzept master report 2026-05-08) |
| **C7** | When does Juna first appear directly? | once, ca. Kap 33, Garten der Stillen Präsenz (Charakter-Bibel 2026-05-08) · first in Kap 38 (storyform-und-outline; konsolidiertes Konzept) · the Kapitel-Kompendium, which C7's record expected to settle it, places none · „Kernwelten vollständig": Kap 33 is her *effect*, Kap 38 her appearance — perhaps not a conflict at all · the strukturierter Outline (2026-05-18): Kap 38 Beat 3, stated five times, nothing in Kap 33 · the drafting manual (2026-06-10): Kap 33 „Setting der Juna-Wirkung“, Kap 38 „Juna erscheint direkt“ — the same split as „Kernwelten vollständig“ · the Alter profiles (2026-06-10): „direkte Stille-Erscheinung Kap 38“, a mode locked 2026-05-30 · the Plot-Konkretisierung (2026-06-10, a proposal): Kap 38 Beat 3, with only effects before it — a line, a channel, a record with no type · Kap 38, from a document that names the Kap-33 source among what it consolidates (Sprach-DNA (2026-05-13)) · **no chapter, a revelation in Akt II** — „KW2/KW3 (Akt II), nicht früher“, the modes of appearance open (konzept master report 2026-05-08) · never a subject, only an effect, by the draft's own rule R-8 — warmth at the first contact, the perturbation AEGIS cannot classify (annotated draft of Kap 0, 2026-05-17) |
| **C8** | AEGIS' Approach in Storyform B — Be-er or Do-er? | Be-er (Charakter-Bibel) · Do-er (storyform-und-outline; konsolidiertes Konzept; Kapitel-Kompendium) · the lock-in of 2026-05-07 mirrored it to Do-er and names Be-er as the value before — the character bible, a day later, carries the old value · Do-er, under a status line that names the 2026-05-07 „Approach-Korrektur“ (konzept master report 2026-05-08) |
| **C10** | Do Kael's knuckles bleed in Kap 1? | yes, the first Landauer trace (Charakter-Bibel) · no, Kap 0 alone (storyform-und-outline; Kapitel-Kompendium 2026-05-31, in the wording document 7 follows) · in the novel's opening image, not in its Kap 1 line (konsolidiertes Konzept) · **a trait, in no chapter**: the Host's bleeding knuckles stand in his profile, in neither Kap 0 nor Kap 1 (strukturierter Outline 2026-05-18) · Kap 0 alone, four times, dated to the Kompendium's lock of 2026-05-31 (drafting manual 2026-06-10) · Kap 0 only, in Kael's profile (Alter profiles 2026-06-10) · the bleeding knuckles in Nyx's voice, in no chapter; the Host's field has none (Sprach-DNA (2026-05-13)) · in the premise, in no chapter, as the konsolidiertes Konzept of its date (konzept master report 2026-05-08) · **Kap 0 as written has no knuckles and no Nyx** — the first draft of 2026-05-08, three weeks before the sources that put the thread in Kap 0 alone · **Kap 0 has them, in Nyx's voice as the separation runs**, annotated as a foreshadow of a Kap-1 opening the writer attributes to the concept; Kael's own first lines carry none (annotated draft of Kap 0, 2026-05-17 — nine days after the draft without them) |
| **C11** | Is the Landauer trace warm (Kap 6, Kap 36) or cold ozone? | warmth (konsolidiertes Konzept) · „Landauer-Hitze/Ozon", a day after the lock (Kapitel-Kompendium) · cold ozone everywhere, warmth only Juna's and at Vortex 1 Beat 4 (storyform-und-outline, citing its lock of 2026-05-30) · warmth in Kap 6 and Kap 36, in the konsolidiertes Konzept's words (strukturierter Outline 2026-05-18) · **one document on both sides**: the drafting manual (2026-06-10) locks cold ozone as the Landauer-Signatur and names its first foreshadowing strand `Landauer`, „Hitze als Symptom der Wahrheitsvertuschung“, accumulating in Kap 6 (J81) · **heat three ways in one document** (Alter profiles 2026-06-10): Juna's Coheron-Spur, Silas' warmth as the only diegetic warmth under the same lock, and Landauer heat from the Silas–Oblivion conflict · **the cold side as a plot** (Plot-Konkretisierung 2026-06-10, a proposal): cold ozone after every Ausgleich, Kap 6 „Sensorik kalt/Ozon“ filtered against the Source-of-Truth's §7 conflict, Kap 36 Beat 4 the „einziger kanonischer Landauer-Wärme-Ort“, Silas' warmth the Coheron-Echo · **Landauer warmth „spürbar als Ozon-Geruch oder Hitzeschlieren“** — both sides as one thing's two renderings, seventeen days before the lock (Sprach-DNA (2026-05-13)) · **heat and ozone as one signature of AEGIS' erasure** — „Landauer wird zu Hitze und Ozon“, no warmth for Juna or Silas, Kap 6 unnamed (konzept master report 2026-05-08) · **warmth as Juna's trace in Kap 0**, the `Wärme-Spur` the Funken-Ich feels before AEGIS' filter, cold only as AEGIS' manner, no ozone, no Landauer — a proposal, from a chat turn (Doppel-Klammer Abhandlung 2026-05-08) · warmth as Juna's frequency, cold as the separation's, ozone in the Konstrukt-Stadt „ohne dass jemand weiß warum“ — as written in the draft of Kap 0 (2026-05-08) · warmth at the first contact as Juna's hint, heat in AEGIS' analysis and in the air beside the bleeding knuckles, cold as the logic that cuts; no ozone, `Landauer` only as a word the first fifty pages may not use (annotated draft of Kap 0, 2026-05-17) |
| **C12** | Three Genesis beats or four — and does Komponente 734 come before the Trennungsprotokoll or out of it? | three, 734 its result (Charakter-Bibel) · four, 734 before it (konsolidiertes Konzept; storyform-und-outline counts a fourth) · both orders and a fourth beat (Kapitel-Kompendium, and already the strukturierter Outline of 2026-05-18) · four beats restated, Einheit → Cluster → Trennungsprotokoll → Wir-AEGIS-plural, 734 no beat (drafting manual 2026-06-10) · four beats cited to the Kompendium, and Alex arising in the fragmentation (Alter profiles 2026-06-10) · no beats counted; 734 consolidated in Kap 0, flashbacks Cluster → Trennungsprotokoll → 734 in Kap 18/21/22, and Kap 40 echoing the Trennungsprotokoll as „Bewegung 4“ (Plot-Konkretisierung 2026-06-10) · three, locked, 734 the separation's remainder — the character bible's count, on the date the konsolidiertes Konzept counts four (konzept master report 2026-05-08) · four, and a place for each: Beat 1 told nowhere, Beats 2 and 3 in Kap 0, Beat 4 in Kap 39 (Doppel-Klammer Abhandlung 2026-05-08) · no beats; 734 before the separation, Kael cut out of it as its remainder (draft text of Kap 0 and Kap 40, 2026-05-08) · four beats, 1–3 in the prologue, Beat 4 in Kap 39 — and **the component becomes Kael**, not its remainder (annotated draft of Kap 0, 2026-05-17) |
| **C14** | Does AEGIS get a first-person chapter? | third person, no inside (Charakter-Bibel; konsolidiertes Konzept, both 2026-05-08; Kernwelten vollständig) · one chapter in Kap 5–8 with a first-person inner view, an exception locked 2026-05-30 (storyform-und-outline; begriffe-und-konzepte) · both, unrelated (welt-sensorik, with „nie Ich") · third person and never prose, its debut in that very chapter (Anteile-Profile, which says it is filtered on the 2026-05-30 iterations) · one chapter in Kap 5–8, „erste Person, Protokollform“, worked out as a routine consolidation (Plot-Konkretisierung 2026-06-10, a proposal) · third person, never `ich`, with an „Operative Interiorität“ — the reader inside its process (Sprach-DNA (2026-05-13), between the 2026-05-08 sources and the lock) · third person for AEGIS and the Guardians, no exception (konzept master report 2026-05-08) · a first person inside AEGIS in Kap 0 — the Funken-Ich's, which becomes 734 — with AEGIS itself in the third (draft text of Kap 0, 2026-05-08) · the formula in the first person „weil das Ich gerade in dem Akt zu AEGIS wird“, then AEGIS in status lines (annotated draft of Kap 0, 2026-05-17) |
| **C15** | Who carries Flight, the spatial riss? | Kiko as her second function, and Lia (Charakter-Bibel 2026-05-08; Anteile-Profile 2026-06-10) · Lia and Isabelle (konsolidiertes Konzept, the bible's date; storyform-und-outline, Kernwelten vollständig, begriffe-und-konzepte, all 2026-06-10) · both, in two tables (welt-sensorik) · Lia and Isabelle, „implizit“, and no alter in its roster is Flight (konzept master report 2026-05-08) |

C1–C5 come from the 2025 research documents and have not been put to the author
before this list.

### The novel — what no source settles

- **Q5 — pairing.** Five Guardians, four Kern-Welten: one per world (2025, Kairos
  and Sophia sharing KW4), or „KEIN Guardian-1:1" (2026)? The drafting manual
  (2026-06-10) names the 2025 pairing and retires it: „KW1=LogOS,
  KW4=Kairos/Sophia" — „Beides ist dekanonisiert"; the worlds are act markers (L42).
- **Q5 — the Erasure-Pol.** Every 2026 source has one, and the name is its own
  open question („Name offen, Forschungsfrage"). A sixth figure, a function of the
  five, or the name for what Cerberus, LogOS and Kairos do together? The Sprach-DNA
  (2026-05-13) labels it `Guardian` beside Mnemosyne, „Name offen — OQ“ (L53), and
  has Mnemosyne dominate KW2, the world named for her (L217).
  The annotated Kap 0 (2026-05-17) hears it as a voice before there are worlds: the
  separation's sweep, „Erasure-Pol-Stimme (Lösch-Vollzug, bürokratisch-knapp)“ (L957).
- **Q5 — where Sophia went.** The 2026 sources absorb the others three different
  ways (LogOS into Mnemosyne, or into the Erasure-Pol; Kairos latent, or into the
  Erasure-Pol). The strukturierter Outline (2026-05-18) holds two of them at once
  — LogOS into the Erasure-Pol (L161) and into Mnemosyne (L172), Kairos absorbed
  and latent — and is the first read 2026 source to place Sophia: „(Kairos/Sophia,
  latent)" in KW4 (L175). Its OQ table has no row for the Erasure-Pol's open name.
  The Alter profiles (2026-06-10) give the konsolidiertes Konzept's version again —
  Cerberus, LogOS and Kairos into the Erasure-Pol — and do not name Sophia.
  The Plot-Konkretisierung (2026-06-10) has the two as two gifts in Kap 31, names LogOS
  only as „dekanonisierte Namen“ (L255), and describes no absorption.
  The konzept master report (2026-05-08) names all five as „Frühere Drafts“ and has
  them absorbed into Mnemosyne and the Erasure-Pol together, without saying which into
  which (L504–L513).
- **Q1 — the Guardians and AEGIS.** Three canon-era sources make the Guardians
  components inside AEGIS' architecture. With five restored, is that still so?
- **Q3 — correspondence.** Four Kern-Welten and thirteen Alters: does any world
  belong to one Alter, or are the worlds act markers only? The drafting manual
  says act markers, and ties Alters to Riss types by trigger, not to worlds (§3).
- **Q4 — `Wächter`.** The word names Guardians, AEGIS, Mnemosyne, Selene, a
  chapter title and a registry. Is one of them *the* Wächter?
- **Q2 — the eight protocols** (ANI, ARS, ECR, PMS, RSA, SNK, ZTV,
  Nullpunkt-Protokoll) exist only as objects of one source's criticism. Are any of
  them the novel's vocabulary?
- **Mosaik-Herz — one thing or two?** A Kap-11 story beat (storyform-und-outline,
  Kapitel-Kompendium, konsolidiertes Konzept) and a Kap-34 place where Kael accepts
  Juna (konsolidiertes Konzept, „Kernwelten vollständig"). The strukturierter
  Outline has both chapters too — Kap 11's stage and „Mosaik-Herz vor Vortex" in
  Kap 34 — and does not say whether they are one. The drafting manual has only the
  Kap-34 place (L274).
- **The world names after C6.** With five Guardians restored, do Cerberus-Labyrinth
  and Kairos-Potentialis name their Guardians again, or stay „mythologisch"
  as „Kernwelten vollständig" proposes (its L946–L947)?
- **The Ursprungs-Ich and Juna (J68).** The glossary glosses the separated
  original self as Juna — „das Ursprungs-Ich (Juna)" — while its Genesis has the
  Ursprungs-Ich resonate *with* Juna. The konsolidiertes Konzept writes the same
  gloss. Is Juna the Ursprungs-Ich, or what it met? **A third answer (J75)**: the
  strukturierter Outline makes AEGIS the Ursprungs-Ich — „AEGIS (Ursprungs-Ich →
  Wächter)" (L237) — and ends „Kael ist als das erkannt, was AEGIS einmal war"
  (L1241). **The konzept master report (2026-05-08) names no one**: the
  Ursprungs-Ich resonates „mit einer fremden Entität in der Leere“ (L463), and
  Kael is what remains when it is split into modules (L465).
  **The worldbuilding concept (2026-05-08) holds both, a month before the glossary**:
  the Ursprungs-Ich meets Juna as a „transzendente Anomalie“ (L179) and becomes
  Komponente 734 (L180), and the Fragmentierungsnacht „spaltet das Ursprungs-Ich (Juna)
  ab“ (L435). It does not relate the two.
- **The final form's name.** Wir-AEGIS / Mosaik-AEGIS / Plurale Kohärenz / Das Wir
  / namenlos — the konsolidiertes Konzept's own OQ-A (L1199). No page until it is
  named. The strukturierter Outline's OQ-A says the same: `Wir-AEGIS-plural` is a
  working term, to be settled in Kap 39 (L1369; J73). The Sprach-DNA (2026-05-13)
  uses it without marking it open: in Kap 39 the Wir becomes „pluralen
  Bewahrungsform (Wir-AEGIS-plural)“ (L173).
- **KW3 has no chapter.** In the strukturierter Outline every other world is a
  setting somewhere (KW1 in Kap 1 and 4, KW2 at Kap 5 and 15 and as the climax
  archipelago, KW4 anticipated in Kap 13 and 20); the Cerberus-Labyrinth stands
  only in the world table (L174). A gap in that plan, or deliberate? Found by the
  graphify reader, checked against the lines. The drafting manual (2026-06-10)
  gives KW3 „Späte Akt II (Kap 23–28)" and the Überwelt-Nexus in Kap 33 (L175),
  so the gap is that outline's, not every plan's. So does the Sprach-DNA
  (2026-05-13): Kernwelten 2–3 are Akt II, Kap 14–26 (L185). And the konzept
  master report (2026-05-08): KW3, Akt II, Kap ~20–26 (L660).
- **KW2 — Resonanz-Landschaft or Mnemosyne-Archipel?** The konzept master
  report (2026-05-08) names KW2 `Resonanz-Landschaft` (its L331, L659) and gives
  the `Mnemosyne-Archipel` to the Vortex, Kap 35–36 (L508). Every other read
  canon-era source that names KW2 calls it the Archipel; the konsolidiertes
  Konzept and the drafting manual give both — „KW2 — Mnemosyne-Archipel
  (Resonanzlandschaft, Klimax-Setting)". One world with two names, or a world and
  the Vortex's setting inside it? No source denies another, so no record. Found
  by the second reading of the report (pull request #94).
- **`kael-julia-bindung` (J13).** One document says `Kael-Julia-Bindung`, nine say
  `Kael-Juna-Verbindung`. The Kapitel-Kompendium now states „Julia→Juna" as a rename
  it applied to its quarry (L13). Should the page be renamed, and is the older
  `Kael-Julia-Bindung` a term of its own or only the old name?
- **Juna's names.** `juna.md` is titled by a name the first read sources do not
  use, and `Partnerin` may be a third surface for her.
- **Alex — in the separation or before it?** The drafting manual names this
  conflict itself (§14.4, L1456–L1466): the character bible has Alex arise „in der
  Sekunde der Fragmentierung", the Kap-0 annotation choreographs an Alex-Vorform
  before the Trennungsprotokoll. It proposes „Funktion vor Person" — voice
  pre-forms as proto-clusters — or rewriting Alex' Genesis, and leaves it to the
  next Kap-0 pass. Recorded under C12.
  **The Kap-0 annotation is read now** (document 23, `kap0-v1-annotiert-md`,
  2026-05-17): it choreographs „Alex-Vorform-Einbruch“ (L301) in the Genesis and
  names the conflict itself — „Konzept-Konflikt?“ (L1205) — and its deeper
  revision would take Alex out (L1134). The `alex` page holds both. Which one —
  and are Vorformen proto-clusters or the alters themselves — is yours.
  The Alter profiles (2026-06-10) flag the same conflict from Alex' side (L219,
  L1079) and call it a „Reviewer-Frage offen“.
- **`Einheit 734` (J80).** The Kap-1 console line is placed under Kael's dwelling
  once (L101) and as Komponente 734 twice (L487, L661) in one document. Which is
  it — or is the ambiguity the point? **The Plot-Konkretisierung proposes the second**:
  the Kap-22 find shows the component's serial is his dwelling's — „Er wohnt in der
  Akte seiner eigenen Quarantäne.“ (its L88), marked `[V]`. Now **Q7**
  (`Wiki/questions/q7-what-734-names.md`), 2026-09-29.
- **Kap 40 — 39 chapters or 41 movements? Mostly answered by the sources, and this
  line was wrong.** It said every read source but the Plot-Konkretisierung ends at
  Kap 39. Reading the chapter outlines onto chapter pages (decision 013) showed
  otherwise: seven of the eight read documents that go chapter by chapter count
  „41 Bewegungen" — Kap 0, Kap 1–39, Kap 40 — and give Kap 40 its own entry, the
  konsolidiertes Konzept first (its L2). The 2025 AEGIS subplots count „39
  Kapitel" with no frame — **and so does the konzept master report, of the
  konsolidiertes Konzept's own date**: „39 Kapitel, 3 Akte, Vortex Kap 35–36“
  (L21), one Vortex, and Kap 37–39 a resolution with no false victory and no
  Vortex 2 (L907). So on 2026-05-08 two plans stand side by side, 39 and 41. The
  Konzept-Iteration Genesis names „Das Spec-Dokument vom 2026-05-08 (drei Modi, 39
  Kapitel)“ as the one to extend (its L818); `three-mode-architecture-39-chapters-md`,
  read as document 24, very likely is: 39 chapters, one Vortex, no frame. `Wiki/overview/plot.md` has the positions. What is still
  open is the coda's content, not its existence: the Plot-Konkretisierung's single
  click „ohne Ozon" is `[V]`. The „Kap0-Kap40-Doppelklammer" and the „Kap40 und
  Kap0 Fassung" (both 2026-05-08), unread when this was written, are documents 21
  and 22.
- **C13 — Köln 2026 beyond the simulation?** Two sources place the `Basisrealität`
  beyond it, while four describe the `Externe Ebene` as not outside it. J54
  equates those names by their shared attributes, so the author's decision is
  whether they name one level with conflicting placement or two conceptions.
  The six cited positions are in `Wiki/conflicts/c13-externe-ebene-beyond-the-simulation.md`.
- **The Doppel-Klammer Abhandlung's three Setzungen** (2026-05-08, document 21). It
  asks you to confirm them and decides none: the Vermittler-Stimme of Kap 0's
  Vorwort *is* Wir-AEGIS-plural, unrecognisable on a first reading (L544); a
  `Wärme-Spur` in Kap 0's Resonanzkaskade, which it says came from „der Probe vom
  letzten Turn" (L315, L556); and the same shards at both ends, of glass or mirror
  glass (L568–L572). Each has a „Konsequenz, falls verworfen". **The draft of Kap 40
  and Kap 0 of the same date (document 22) carries all three**, without naming the
  treatise: „Das waren wir." (L31), the warmth in the Resonanzkaskade (L401), the
  shards after two falling glasses (L271, L473, L513). Drafted, then — whether decided
  is yours to say.
- **Who is Mira?** The Abhandlung names the Wir's voices in Kap 40 as „Lex, Nyx,
  Kiko, Mira, alle" (L327). No other landed document has the name, and no roster of
  thirteen holds it (Q3).
- **Where the Formel-Inversion's second sentence falls** — the turn from Kap 39 to
  Kap 40 (four sources), Vortex 2 or Kap 39 (four, two of them also the turn), or
  Kap 40's Klick (the Abhandlung alone). See `formel-inversion`.
- **`Ursprungs-Ich` has no page.** It is in 53 landed documents and six read ones
  (`corpus.py count`); no read document has defined it yet. Whether it is its own
  figure or a name for the Funken-Ich, AEGIS before the Genesis, is for the reading
  that defines it.
- **Found by the 2026-09-25 scan's page writers, not yet a record.** Ten documents
  were scanned (`Plan/runs/haiku-scan-2026-09-25/`), and new pages quote them
  beside the read ones. Where those pages found the sources parting and no
  conflict or question holds it:
  - **One Vortex or two.** The Dramatica lock-in, the character bible, the
    master report, the 39-chapter spec and the Worldbuilding-Konzept count one.
    The konsolidiertes Konzept and everything later count two. The two lists for
    Vortex 1's five beats also differ, and so does which beats fall in Kap 35 and
    which in Kap 36. The 39-chapter spec adds a third storyform boundary,
    „bei 36/37", beside its own 34/35. See `vortex`, *Where the sources differ*.
  - **Eleven alters or thirteen.** The Inquiry (2025-10-15) and the plan of
    2026-02-26 count eleven, and the Charakter-Kompilation reports a status that
    strikes Silas and Oblivion. Every source from 2026-05-08 on counts thirteen.
    See `tsdp`.
  - **Who is the living Gödel statement?** Kael in five documents, Juna in five,
    Juna alone in the master report, and the Moonshine-Link in the Inquiry.
    See `goedel-gambit`.
  - **Does AEGIS have qualia?** AEGIS erases the pain before it becomes qualia
    (the Hard-Problem analysis). It is a pure functionalist without qualia
    (Philosophie im Detail). It misread its own emerging qualia as an error
    (Charakter-Kompilation). See `thermodynamischer-phaenomenalismus`.
  - **The Ouroboros — an image or a sentence, Kap 1↔39 or Kap 0↔40?** See
    `ouroboros-struktur`.

### The process — the author's call, with the detail under *Open decisions*

- **`account.py order` passes a `reconcile.json` with no census beside it**; it should not.
  Found when the Jules session's claimed reconciliation of the philosophischer Bericht passed green
  (decision 014). The document is now read and reconciled as document 31, so nothing rides on it
  today; the gap in the check stays open.

- **`Coherence Protocol.mp3` is the one row not landed.** markitdown turns audio
  into text only through a speech-recognition service outside this container,
  which sends the recording to a third party — the rule Jev and every model call
  keep. A yes, and a service you are content with, lands it; otherwise it stays.
- **The entity lists and the translation pairs predate the plot outlines.** Both
  were built over the corpus as it stood before 2026-09-26, so the 215 documents
  landed that day get names only from the vocabulary those lists already hold.
  A name that occurs only in them has no entry in `Sources/README.md` until
  `entity-lists` and `bilingual.py` run over them. The first sends text to Haiku
  and the second to free OpenRouter models and Jev, so both wait on your yes.
- **Two sessions are reading the same documents.** Documents 16 and 17 were each
  read twice on 2026-09-25, in the same order, because both handovers named the
  same next document. Main took one session's readings; the second readings
  found C13, C14, C15 and C11's missing bible entry, and their lists are kept as
  blind re-readings (`Plan/learnings/extract-terms.md`). If several sessions are
  meant to read, which one takes which document is yours to divide — nothing in
  `NOW.md` does it yet. Until you do, this session took a document the other
  one's handover did not name: the Sprach-DNA of 2026-05-13 (document 19), while
  that session read `kp-plot-konkretisierung-13-ideen-f1-faden-2026-06-10-md`
  (document 18). The readings did not overlap; they met on 24 pages and seven
  records, and the merge appended one after the other. **It happened again with
  document 20**: both sessions followed the Sprach-DNA's handover to the konzept
  master report and read it in full, independently (pull requests #94 and #95).
  Main took #95's reading; #94's list is a blind re-reading (F1 0.76), and what it
  added that main's did not hold — J92, J93, the KW2 question, two tool fixes —
  went in with the merge. A handover that names one next document sends every
  session there.

- **Decision 011 — confirm or narrow.** On „Use dspy Optimierung on the
  Scripts" and „Add openrouter free Models in the mix" the session let DSPy
  runs use Claude through `claude -p` — treated as first party, the precedent of
  document 14's second readers — and free OpenRouter models through `route.py`,
  pinned, for surfaces and rules only. The `pairs.py` ladder ran under it
  (`Plan/concept/dspy-optimization_2026-09-25.md`). Claude calls draw on your
  usage.
- **A model's merges as a review queue?** Bootstrap on Haiku found 12.7 of the
  19 merges the plural rule misses, with one false merge (J74). Nothing turns a
  model's merge into a ledger entry; listing them for you to judge is one small
  step, and yours to allow.
- **J68 again.** With the document's lines as evidence, Haiku merged
  `Ursprungs-Ich` and `Juna` in every repeat, from the glossary's own „das
  Ursprungs-Ich (Juna)". The ledger says two terms; the question below asks which.
- **SIMBA** — the one rung not run: about $8 of Claude usage, no published
  evidence for it. Run it?
- **`graphrag.py ask --answer` and `rlm_ingest.py`** may now run on Claude under
  decision 011 (never on a free model: they send quotations and documents).
  Neither has.
- **DSPy labeled demo selection, 2026-09-24.** The offline `pairs.py` run now
  excludes every exact never-merge canary from model training, including J5
  (`Negentropie`/`Entropie`) which the ledger also contains. Its labeled rung
  puts two other documented hard negatives in each fold's eight demos and
  records the chosen IDs. This repairs the claimed holdout and makes the
  selection inspectable. The ladder's model runs of 2026-09-25 (above) were
  measured before it merged; their rows name the older harness.
- **TypeSafe/Jev beyond the two uses already approved.**
- **How far `ask` may go** — chosen quotations only, or also a framing sentence
  marked as the model's.
- **M-flow and corpus text.** It is installed and nothing calls it. May any
  corpus text go through it, and to whom? If its one experiment that keeps the
  rules is wanted, how does a page map onto its four levels?
- **A reviewed page and a new source that contradicts it** — needed before the
  first promotion.
- **The quote convention** — a quotation carries its reference in the same table
  cell, or the checker learns tables. Until then those quotations stay unchecked.
- **Whether `fold()` adopts the plural rule** — decision 010 set its reach on
  your delegation, as a scored rule in `pairs.py` that the pipeline does not use.
  Adopting it changes what every reconciliation merges by lookup; widening it to
  `Alter`/`Altern`, which the corpus uses as one term, is the same question.
- **`GOAL.md` against the working agreement** — the manuscript, NCP files and
  claude.ai exports as sources; a conflict detector; the `kg/`/`kp` layout;
  status tags and tiers on pages.
- **The new tools as second readers** — on every document read, on some, or not
  again? Document 14's three cost 747k subagent tokens together;
  knowledge-graph-extract alone, the best of them, 268k and 35 minutes, or about
  90 seconds split four ways in parallel. No corpus text leaves: the model is
  Claude. Their output stays a model's reading (below, *The new tools as second
  readers*).
- **Chapter-level differences as conflict records?** The chapter pages
  (decision 013) state where the sources part per chapter — titles, worlds, what
  happens — under `## Where the sources differ`, and `Wiki/overview/plot.md` does
  the same for the book's shape: the storyform turn at 34/35 or 35/36, Akt III
  from Kap 27 or Kap 29, where Kishōtenketsu's Ten begins. None became a conflict
  record; the fifteen records stay about substance. Which of these, if any, should
  be one is yours to say.
- **Chapters in the graph and the app.** `graph.py` and `ui.py` do not know the
  chapter pages yet; adding `chapter:` nodes changes the graph's self-check and the
  retrieval bench. Wanted, and when?
- **When the project app is rebuilt** — after every reading, as part of phase
  4's re-measure, or only on request. `scripts/ui.py` builds it; a Claude session
  publishes it to the canvas (`CLAUDE.md`, *The project app*).

## Open decisions — these are judgement, not measurement

**How far the yes to TypeSafe reaches.** On 2026-09-23 the author said yes twice.
First to „a small test on the two documents with a reader's list", which sent
those two documents' passages. Then, the same day, to using Jev and OpenRouter's
free models for the German–English entity mapping (below). That run sent Jev up to
two lines of context per surface for 18,026 surfaces and up to four lines per pair
for 11,277 pairs, drawn from across the landed corpus. The free models got **names
only**, because a free endpoint may keep what it is sent. Anything beyond those two
uses should be asked for again, with its cost.
`Plan/concept/jev-in-ingestion_2026-09-23.md` has the three placements and what
each would send.

**A third yes, 2026-09-24 — decision 007.** Documents 5 and 6
(`aegis-subplots-kapitelweise-system-exploration-docx`,
`roman-lokalitaeten-konzept-und-ausarbeitung`) may go to free OpenRouter models,
with `data_collection: deny`, and to Jev, to test the tools installed that day.
No other document, no paid model, nothing to Notion. `scripts/route.py` enforces
it in code and its `selftest` holds. **The tool review ran on 2026-09-24**, at
$0 over 339 priced calls: `Plan/concept/tool-review_2026-09-24.md`. No
extraction tool reached a usable result on this corpus — best F1 0.16 against
the Haiku floor of 0.25 — and none closes the loop's three gaps. Its six
questions, the templates page's four and the three-encodings question below were
**answered by the session on the author's delegation** — decision 008, each
reversible by the author. The two replaced the question's examples because only they
have a genuine reader's `03-candidates.md`; the decision file says why.
Decision 009 has since ruled the session's lists for documents 7 to 14 gold as
well. Decision 007's consent, as decision 008 extended it, still names only
documents 5 and 6.

**Three encodings of one rule.** „No corpus text leaves without the author's
decision" is held by `lmrun.py` (`approval=`), by `rlm_ingest.py` (`--approval`,
its own `dspy.LM`) and by `scripts/route.py` (the consent file of decision 007),
while `bilingual.py` and `jev_entities.py` call out directly. They met in one
merge and agree today; P6 says they will not stay agreed. Which one the others
should call — and whether `route.py`'s record-and-replay or `lmrun`'s
cache-off is the rule for a measured repeat (P18 either way) — is a decision,
not a refactor. **Decision 008: no refactor now**, revisit when one of them
changes its rule and the others do not.

**Both Jev keys are present** in the environment (checked 2026-09-23, presence
only). That removes the technical block and none of the permission one above. A key pasted in chat earlier in
the session that installed this should be treated as spent and rotated.

**A reviewed page has no rule yet.** Nothing has been promoted, so the case has
never arisen: when a new source contradicts a page a person signed off, neither
can silently win. `dspy-wiki-compile` answers it — flag, list the conflicts,
never update in place — and decision 003 does not cover it, because 003 governs
conflicts *between sources*. Needed before the first promotion.
See `Plan/concept/wiki-compile-second-opinion_2026-09-17.md`.

**`kael-julia-bindung` is probably misnamed (J13).** 1 document, 16 occurrences,
one day, against `Kael-Juna-Verbindung` in 9 documents over 14 months. Renaming
needs a rule for what a page is called when the corpus and the read sample
disagree. There is no such rule.

**`juna.md` is titled by a name none of the read sources uses**, and `partnerin`
may be a third surface for the same entity. Nothing read links them.

**The quote convention is in use.** A research-source quotation carries its
citation on the same line and inside its table cell. Source labels and the
wiki's own working sentences use code or emphasis; recorded author decisions
link to their decision record. The checker reports 0
<!--state:quotes.unchecked--> quotations without a resolvable source citation.
`python3 scripts/quotes.py --unchecked` lists any new gaps with file and line.

**Eight pages carry five identical sentences each — measured, not yet decided.**
`ani` `ars` `ecr` `pms` `rsa` `snk` `ztv` `nullpunkt-protokoll` are the eight
protocols of an „AEGIS-Postulat" that one source analyses rather than authors.
Each page restates the same group fact: the doubly-attributed shape, that the
postulate itself is not in the corpus, and that the term exists only as an
object of criticism. 320 lines, most of them the same.

**Left alone on purpose.** The repetition is what makes each page stand alone,
which is a term page's job, and a construct's test here is use rather than
argument. What would settle it: a later source using one of these protocols as
project vocabulary — which each page's Open section already names as the thing
to watch for. Then the group needs a page and the eight can point at it.

**Which qmd backend this corpus actually wants.** `qmd bench` is an IR
evaluation harness — four backends, precision@k, recall@1/3/5, MRR, latency —
and it has never been run here. `CLAUDE.md`'s advice to write structured
`lex:`/`vec:`/`hyde:` queries rather than a plain phrase is reasoning about
German compounds that nothing has tested. The fixture is nearly free: every
`Wiki/questions/` page and conflict record already says „a search finds this in
`<slug>`". Plan: `Plan/concept/skills_2026-09-17.md`.

**The plural rule exists, and `fold()` has not adopted it.** `fold()` removes
the article, case, diacritics and punctuation and nothing morphological, and
every pair it misses is one a person called one term. Decision 010, taken on the
author's delegation, set the reach of a rule that also passes a plural ending:
`pairs.RULES["plural"]` decides 57 <!--state:pairs.plural_correct--> of
89 <!--state:pairs.labelled--> pairs where `fold()` decides
48 <!--state:pairs.fold_correct-->, with no false merge, no canary merged, no two
pages joined and 28 new merges across all 14 candidate lists, each a singular and
its plural. It is a ledger row and the rule a model run asks first;
reconciliation still uses `fold()` alone. Whether `fold()` adopts it is the
author's, above.

**What the plural rule leaves cannot be learned from the input the model is
given.** Of the 19 pairs left, the session reads eight as rules a program could
state (slash aliases, an acronym's expansion, a numbered instance, a
parenthetical index) and eleven as decided from the passage —
`Basisrealität`/`Externe Ebene`, `Therapie-Schnittstelle Gamma`/`Alpha`.
`pairs.py`'s signature takes the two surfaces and nothing else, so a model can
only guess those eleven. Carrying the
lines each judgement cites into the input
(`Plan/concept/continuous-improvement_2026-09-17.md`, step 1) comes before any
model run can learn them — and it widens what that run would send.

**Which model runs are allowed — decision 011, 2026-09-25.** On the author's
„Use dspy Optimierung on the Scripts" and „Add openrouter free Models in the mix":
Claude through `claude -p` for any DSPy program, and one free OpenRouter model
through `route.py`, pinned, for what `pairs.py` sends. The ladder ran —
LabeledFewShot, Bootstrap, InferRules and GEPA on Haiku, LabeledFewShot with
document lines as evidence, and LabeledFewShot on the free models that answered;
`python3 scripts/pairs.py report` reads every row, and
`Plan/concept/dspy-optimization_2026-09-25.md` reads the results. Still one
command each, and not run:

- `pairs.py run --optimizer simba …` — about $8 of Claude usage (above).
- `graphrag.py ask "…" --answer` — a model picks evidence numbers; on Claude only.
- `rlm_ingest.py <slug>` — a whole document, on Claude only; its own `dspy.LM`
  would need `lmrun.make_lm` to reach Claude. Needs Deno as well.

**How far `ask` may go.** `graphrag.py` returns verified quotations and never
prose, because prose over two sources is a merge (P13). Whether an answer should
ever be more than chosen quotations — a framing sentence, a summary marked as
the model's — is the author's to decide, and nothing builds it until then.

**M-flow — installed on 2026-09-24, and nothing calls it.** The author asked for
it to be installed, and it is, in `.venv-mflow`. Its default path has a model
write the graph (`memorize`) and the answer (`search`), and both steps call
OpenAI. The graph would be paraphrase where the wiki quotes, the answer would be
the merge `ask` refuses, and both would send corpus words out. Two entry points
avoid the first two: `manual_ingest` takes structure a person wrote, and
`search(only_context=True)` skips the answer. They make one experiment possible:
load the wiki's own pages and score M-flow on `graphrag.py bench` against
PageRank. It needs two answers first. May the wiki's quotations be embedded by a
third party, or only locally with `fastembed`? And how does a page map onto
Episode, Facet, FacetPoint and Entity? `Plan/concept/m-flow_2026-09-24.md` has
the measurement and the detail.

**Where `GOAL.md` and this repository's rules disagree — the author's to settle
before Phase 0 of the goal starts.** `GOAL.md` is now the project's general
goal. Four places where it and the working agreement cannot both hold as
written:

- **The novel's sources — decided for Drive, open for the rest.** The author
  said on 2026-09-23 that the sources are all in `Sources/`: the manifest
  catalogues every Drive document, the canon-era ones included, so they land
  through `sources.py` like any other. 33 <!--state:sources.canon_era--> rows date
  from May 2026 on and 33 <!--state:sources.canon_era_landed--> are landed, since
  2026-09-24 (see *Landed* below); eight are read — documents 7 to 14, below. Still open: the
  manuscript and the NCP files, which are not Drive documents and sit only under
  `Legacy/`, and the claude.ai exports the goal names, which are in no catalogue.
- **Conflict detection.** The goal wants a detector: deterministic comparison per
  predicate, then model adjudication of candidates, with quotations. `CLAUDE.md`
  says conflict detection is never mechanised, because a guesser reproduced the
  `Zero-Trust` false conflict. The goal's deterministic half may fit P1; its
  model half is the open question.
- **Layout.** The goal specifies `kg/`, `wiki/`, `tools/kpkg/`, a `kp` CLI and
  `SPEC.md`. This repository has `Sources/`, `Wiki/`, `scripts/` and two layers
  (P20). `graph.py` and `graphrag.py` already cover part of `kg/` and `kp ask`.
- **Status tags.** The goal's `[K] [V] [S] [L] [D] [M]` and tiers T0–T5 do not
  exist on any page here; the wiki's pages carry readings attributed by source
  and date. Whether they are added, and how they map, is a schema decision (P4:
  no field without instances).

## Chapters and plot — started 2026-09-25 (decision 013)

**Built:** a page per chapter, Kap 0–40, with every chapter-by-chapter source's
reading of it, and `## Where the sources differ` on 40 of the 41 (Kap 23 has none).
`Wiki/overview/chapters.md` puts every title side by side; `Wiki/overview/plot.md`
the book's shape. `scripts/chapters.py` checks them and counts what is missing.

**The differences that matter most for the plot**, each on its chapter page with
both sides quoted — noted for the author, none settled:

- **The book's shape** (`plot.md`): the storyform turn at 34/35 or 35/36; Akt III
  from Kap 27 or, in Kernwelten vollständig, Kap 29; Ten from Kap 27 or from Vortex 1.
- **Kap 1**: what `734` numbers — Kael's designation, or his unit in Sektor 04.
- **Kap 3**: Juna's first trace as a hologram Kael sees (Konzept-Iteration Genesis)
  or as warmth (storyform outline) — C7 already holds the first.
- **Kap 5 and 10**: KW1, the KW1→KW2 edge, or the McLaughlin world.
- **Kap 6 and 36**: Landauer warmth or cold ozone, chapter by chapter (C11).
- **Kap 13**: KW1 in transition with inner practice, or KW3's Evaluierungseinheit
  „wo Personae kollabieren" (Kernwelten vollständig).
- **Kap 18 and 20**: where the Genesis flashbacks begin, and which beat Kap 18
  carries (C12).
- **Kap 22**: does Kael recognise himself as Komp 734, or only read a number — a
  flashback with its own voice, or a scene with a file?
- **Kap 28**: Purge and Juna in danger together, or one of them, OQ-B-dependent.
- **Kap 31–32 and 36**: the Guardians dissolved in Kap 31, sub-antagonists in Kap 32,
  or Mnemosyne the first Guardian affected in Kap 36.
- **Kap 35/36**: Vortex 1 split 1–3 / 4–5 or 1–2 / 3–5 — the Silence beat changes
  chapter; and what Beat 2 and Beat 3 are.
- **Kap 36 or 39**: when AEGIS-monolithisch goes out.
- **Kap 0**: the two drafts differ nine days apart — no knuckles, Kael the remainder cut
  from 734 (2026-05-08); the knuckles in Nyx's voice, Kael the component itself
  (annotated draft, 2026-05-17). C10, C12.
- **Kap 40**: „Wir tragen die Welt" or „Wir tragen die Scherben". The Doppel-Klammer
  Abhandlung gives the Scherben line „laut Konzept", on the date both concept documents
  read end on „Wir tragen die Welt"; the draft text of Kap 40, same date, ends on the
  shards and „Das Universum hält. Wir sind die, die es halten." (document 22).

**Titles.** Most chapters carry two to four titles. Every Kapitel-Kompendium title
in Akt I but Kap 4 and 5 is the strukturierter Outline's HR-Stufe name, and the
Konzept-Iteration Genesis names Kap 2–5 differently from all the rest.

**Next, in order:** the 98 <!--state:chapters.missing--> chapter mentions no page
holds yet (`chapters.py missing` — the character bible's Kap-33 scene, the drafting
manual's reveal timeline, the Alter profiles' debuts); the Abhandlung and both
drafts of Kap 0 are read; then chapters in `graph.py` and `ui.py` if
the author wants them (*Questions for the author*).

## Reading suggestion — next, by the chapter questions (2026-09-26)

Every chapter page now opens with **what the chapter is about** — its readings
summarised and placed in the Heldinnenreise, Heldenreise, cycles, Kishōtenketsu,
acts, Vortex, brackets and Dramatica A/B, each source named where they differ — and
ends with **eight basic questions filled with its plot, 10–12 of its own, a table of
twelve unread candidate sources, and qmd's raw answers**
(`Plan/runs/qmd-chapters-2026-09-26/README.md`). The table is a place to look,
never a reading or a number.

**Read next, in this order:**

1. ~~`koharenz-protokoll-kapitel-0-v2-md`~~ — read 2026-09-26, document 25 (*Next
   document*, below). No Kap 0 question had returned it: the method's limit, measured.
2. ~~`worldbuilding-konzept-kohaerenzprotokoll-md`~~ — read 2026-09-26, document 26.
3. ~~`kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md`~~ — read 2026-09-26, document 27; it names Kap 11, 12, 15,
   24, 25 and every chapter from Vortex 1 to the end, 35–40.
4. ~~`2026-09-14-kap25-vertiefung-md`~~ and ~~`kp-kap25-2026-09-14-md`~~ — read 2026-09-26,
   documents 28 and 29: the log of a drafting run on Kap 25, and the chapter file it revised.
5. ~~`kohaerenz-protokoll-philosophischer-bericht-md`~~ — read 2026-09-27, document 31. The tables
   had listed it for Kap 3, 6, 7, 17, 24, 32, 35, 36, 38; it names only Ch 35–36 and Kapitel 13.
6. ~~`dual-storyform-hintergruende-md`~~ — read 2026-09-27, document 30, before item 5 on the
   author's „das übernächste"; it names Kap 1, 13, 28, 33 and 35–39, no Kap 22 and no Kap 40.

Four whole-novel plans from before May 2026 — read 2026-09-27, documents 40–43 — are in more than half the tables and marked *in most
chapters* there — `monstergruppe-primzahlen-plot-blueprint`,
`hard-sf-roman-outline-dkt-physik-cosmic-horror`,
`dramatica-storyform-synthese-aegis-analyse-2`,
`roman-konzept-dualitaet-kohaerenz-spannung` — as is the worldbuilding concept.
They are reading for the book's shape, not for one chapter. For a single chapter,
its own table below the shared ones is the list; `chapter_sources.py across`
prints every document with its chapters.

**Noticed, not settled:** for Kap 24, four read sources write „B: OS-Psychology,
Host-System-Verstrickung", where GOAL.md §5.2 has B's OS in Physics and its RS in
Psychology; Kap 29's readings give B's line as RS-Psychology. The summaries repeat
the readings; whether the sources mislabel a throughline or GOAL.md does is the
author's.

## Handover — the next session starts here

**A qmd search over all 347 unread landed documents ran on 2026-09-26** (`Plan/runs/qmd-scan-2026-09-26/`): one to four short queries per open record, hits only, no reading. It placed all fifteen unread canon-era documents and found two the earlier scan had not: a second Kap 0 draft and a philosophischer Bericht. It also showed the stemmer turning „Mira“ into „miracle“ — six hits, none of them the name.

**Ten documents have a triage scan, and three of them are now read** (`Plan/runs/haiku-scan-2026-09-25/`,
chosen by qmd searches over the open records). A scan is not a reading. Its
verdict column says nothing either, since nine of ten said READ NEXT. Each scan
does name the records its document speaks to, with lines. The pages
`vortex`, `goedel-gambit`, `ouroboros-struktur`, `chaitin-konstante`,
`kishotenketsu`, `tsdp`, `thermodynamischer-phaenomenalismus`, `komponente-734`
and `vermittler-stimme` already quote these ten documents. Reading one of them in
full, by `ingest`, would give it the census and reconciliation it lacks — as document
21, `kap0-kap40-doppelklammer-abhandlung-2026-05-08-md`, and document 23,
`kap0-v1-annotiert-md`, now have. The four readings the scan had written from the first
needed no correction; of the six it wrote from the second, one sentence was false — that
the annotated draft came before any Kap 40 — and is corrected on `genesis-klammer`.

Run `python3 scripts/selftests.py` first; it builds nothing and says in one line
per suite what holds. In a fresh container the DSPy suites report `not run`
with the command that creates `.venv-dspy`.

**The tool review has run** (`Plan/concept/tool-review_2026-09-24.md`). What it
leaves as work: the four Hyper-Extract templates, which `he parse` cannot load
from a path — `templates.py check` stays green over that, because it only
validates and loads. The three `route.py` defects it found are fixed, and what
was worth porting from the tools is decided — the review's closing section.

In order, and none of it needs a model:

1. **More retrieval cases.** `graphrag.py bench` has
   24 <!--state:graphrag.cases--> cases, all written by the hand that wrote the
   pages. The `## Open` sections (`relations.py --open`) are a second source;
   write `(question, gold pages)` by hand first. `Plan/concept/graphrag_2026-09-23.md`
   has why and the next four steps after it.
2. **The evidence into the pair input.** The plural rule is on the ledger
   (decision 010); what it leaves was decided from passages the program is not
   shown (above). Each judgement's `action` names its lines, and `read.py`
   serves them — as input, never as a label.
3. **qmd as a second seed source for `graphrag.py`**, measured on the bench
   against folded seeding — the floor row is already in `Plan/runs/baselines.jsonl`.
4. **Record routing failures** — each time an agent loaded the wrong skill or
   none. Five to twenty of them are job 4's dataset; there are none, so it has
   not started.
5. **English retrieval cases, to measure the glosses.** `graphrag.py ask --gloss`
   routes `Core Worlds` to `kern-welten` through a gloss the corpus writes, and
   the bench cannot see it — every case names a German term. The four questions
   asked in English, by hand, are the cheapest honest test.
6. **The entity layer grows with the entity lists, not by itself.** Only lists
   that verify as readings feed `graph.proposals()`, and only one unread
   document has one. The full entity run (above, *Half-done*) is what makes
   `graphrag.py`'s unread-document routes worth having.
7. **The record audit for the documents it has not covered** (decision 012, rule
   3). It ran on documents 7–13. Documents 1–6 were reconciled before ingest
   step 6, and 14–15 after it; `.claude/workflows/record-audit.js` takes them as
   args. The rule for what enters a record is in
   `Plan/runs/record-audit-2026-09-24/README.md`.
8. **Every reconciliation ends with `reconcile.py --sweep-open` printing
   nothing** (decision 012, rule 2). Every read document is settled:
   127 <!--state:sweep.decided--> hits, 66 <!--state:sweep.readings--> of them
   readings, in `Plan/runs/sweep.jsonl`.

Two things the build found, fixed in place:

- `Plan/trainsets/surface-pairs.jsonl` had gone stale — 17 rows against a
  ledger that had grown. Re-exported then; it has drifted again since (below),
  and `pairs.py` reads the ledger live, never the export.
- `graph.py`'s first pairing of quotations to citations disagreed with
  `quotes.py` (14 unresolved against 4). The pairing moved into
  `quotes.pairs` / `quotes.verdict` and both use it; `quotes.py`'s own numbers
  did not change.

## The new tools as second readers — document 14, 2026-09-24

The author's instruction for this session was „nutze die neuen Tools". Of the
tools installed on 2026-09-24, two could be used on a new document without asking
anew: **graphify** and **knowledge-graph-extract** are driven by the agent itself,
so with Claude as the model no corpus text goes to a third party (decision 007
covers only documents 5 and 6 for the rest). Both, and the Haiku entity list,
read document 14 **after** its candidate list was committed, as second readers.
`Plan/runs/koharenz-protokoll-strukturierter-outline-2026-05-18-md/second-readers/README.md` has everything; the short of it:

- **knowledge-graph-extract reached a result** where the tool review's free models
  could not: 174 entities, 200 triplets, F1 **0.37** against the reader's list
  (precision 0.80), the best of the three. graphify 0.24, the entity list 0.19 —
  low recall by construction against a 572-entry list.
- **graphify's AMBIGUOUS edges found four of the document's inner tensions on its
  own**, and its reader three the census had missed (now in the census, checked
  and attributed).
- **Speed** (the author asked): 35 minutes was one agent on one chunk, not token
  volume. Four Haiku readers in parallel took 91 seconds for the same tokens and
  kept the rules worse (F1 0.16–0.21); a template parser got every chapter's
  fields with lines in 6 ms. The session model in parallel blocks is unmeasured.
- Nothing any of them produced entered a page, link, count or judgement.

## The `dspy` skill — landed, and what checking it against the code left open

**DSPy itself was read on 2026-09-24/25**: nine readers over the installed 3.3.1
package, its tests and docs, GEPA 0.1.4 and the papers
(`Plan/concept/dspy-source_2026-09-24/`). Three claims of the skill were wrong and
are corrected with probes; `lmrun.call` re-raised an unparseable answer that DSPy's
JSON fallback lets escape, and records it now. The folder's `README.md` lists what
they found that nothing here acts on yet — start there before changing anything
that imports `dspy` or `gepa`.

`.agents/skills/dspy` (netzkontrast/kohaerenzprotokoll#60) holds what the nine
DSPy repositories contain, re-read in full on 2026-09-24 and sorted by the job
at hand; `scripts/check_dspy_skill.py` holds it to the installed DSPy 3.3.1.
Building it fixed, in place: `lmrun.call` re-raised DSPy 3.3's own
`LMTransportError` instead of recording `unreachable`; `rlm_ingest.py` could
call an answer DSPy forced out of an exhausted REPL a reading; `graphrag.py`'s λ
comment compared two opposite conventions; `trainset.py`, `pairs.py` and
`check_dspy_surface.py` stated numbers two ledgers old; and `install.sh` built
`.venv-dspy` without the numpy and Deno extras. Every quotation in the skill
was checked once against its source, and each whose words were not the
source's was corrected; that check is not a standing one, because the nine
clones it reads are not in a fresh container. Open, none of it needing a
model:

- **`rlm_ingest.py` has no offline run of its RLM loop.** Its selftest covers
  the tools and the reach. `dspy[deno]` now installs the sandbox, and
  `check_dspy_skill.py`'s `rlm-runs-offline` probe is the shape one would take
  (P5).
- **Folds move as the ledger grows.** `folds()` deals round-robin over hash
  order, and one appended judgement moved 15 of 57 rows to another fold
  (measured). Whether a stable assignment is worth less balanced folds is open.
- **The export holds 36 rows.** Nothing reads `Plan/trainsets/surface-pairs.jsonl`;
  refreshing it by hand or demoting it is a construct question.
- **The DSPy surface has two encodings.** `check_dspy_surface.py`'s `USED` list
  and the skill's `surface` blocks both assert parameters by
  `inspect.signature` (P6).
- **The path check covers one skill.** Extending it to every skill needs a
  convention first: `ingest` and `tools` name `Wiki/contradictions/` and
  `Wiki/terms/`, which do not exist, on purpose.
- **Gold is decided by rule, and the rule rests on one untested assumption.**
  `scripts/gold.py` (decision 009) rules 47 <!--state:trainset.gold_candidate_lists-->
  candidate lists gold. On 2026-09-24, eight of them were written by the session
  that read the document, and none of those eight has a second reading of the
  same kind — document 14's three second readers were models asked for 50 to 200
  names or triplets, not an exhaustive list, so their F1 (best 0.37) does not
  test it. The
  assumption is that a session's reading disagrees with another reading no more
  than two readings did before (F1 0.66, P27). One second, independent reading
  of a document from 7 to 14 would test it. The lists of documents 5 and 6 have
  been scored against by the tool review (best F1 0.16), and document 14's by its
  second readers.

## Half-done — the entity lists

`scripts/entities.py` works; the lists it searches exist for five documents.
5 <!--state:entities.lists--> lists exist and 4 <!--state:entities.readings-->
pass verification — 395 <!--state:entities.rows_verified--> of
395 <!--state:entities.rows--> rows cite a line holding the entity.

**Revision 3 made the rule structural, and it held.** The reader returns names
only, into `Plan/entities/names/<slug>.json`; `entities.py place` writes every
line and refuses a name the document does not contain word for word. Re-piloted
on the same four slugs, 2026-09-23:

| list | rows placed | names refused | | F1 (rev 2 → 3) |
|---|--:|--:|---|--:|
| `aegis-subplots-kapitelweise-system-exploration-docx` | 70 | 14 | reading | 0.28 → 0.25 |
| `kohaerenz-protokoll` | 82 | 13 | **one line unread** | — |
| `ki-agenten-kohaerenz-und-prompt-generierung` | 68 | 22 | reading | — |
| `roman-lokalitaeten-konzept-und-ausarbeitung` | 97 | 0 | reading | 0.67 → 0.69 |
| `koharenz-protokoll-strukturierter-outline-2026-05-18-md` (2026-09-24, document 14) | 78 | 2 | reading | — → 0.19 |

- **Document 14's list was made after its reader's list was committed**, with the
  workflow's prompt verbatim, as a second reader. Of its two refusals one is a
  translation (`Landauer warmth`) and one is a term **the document does not
  contain at all**, `Persistenzgleichung` — named from outside the document, and
  stopped by `place`. Its reader reported 98 entities; the file holds 80. F1 0.19
  against a reader's list of 572 is a recall of 0.11 by construction; its
  precision is 0.81.
- **Every row verifies because no row was typed.** The refusals are the forms
  revision 2 would have written anyway: `McLaughlin-Graph` where the text has
  `McLaughlin-Graphen`, `Nicht-Lokalität`, `Koherentz Lücke`. They are listed in
  each file's `refused:` line rather than lost.
- **`kohaerenz-protokoll` is not a reading by one line.** Its reader reported
  `read_to_line` 2497 of 2498. `verify` treats any stated gap as disqualifying,
  and that rule was left alone: whether a one-line gap should demote a list is a
  decision, not a fix. Also: `read_to_line` is still the reader's claim. `place`
  prints the furthest line any name landed on beside it, which is code's — but a
  lower bound only, since a name is placed at its first occurrence.
- **Revision 3 found a defect in the checker, not only in the reader.**
  `quotes.normalise` drops a one- or two-digit number glued to a word (footnote
  debris), so on the line `(KW2),` became `(KW),` while the name stayed `KW2` —
  a name ending in a digit could never verify. Revision 2's gazetteer lost
  `KW2`–`KW4`, `Kern-Welt 1`–`4` and `Silent Hill 2` to it and blamed the reader.
  `entities.py` now asks one question for placing and verifying, `holds()`:
  whole word, one line, the normalisation minus the footnote rule. It is
  stricter than revision 2's substring test (`Kontakt` no longer passes on
  `Kontaktaufnahme`), and `selftest` carries seven cases that prove it can fail.
  Quotations are untouched: there the footnote rule is symmetric.
- The four readers cost 423,531 subagent tokens and about 75 s wall-clock, run
  in parallel as four Haiku agents with the workflow's prompt verbatim, not
  through the Workflow tool.

**Jev was tested on the same two documents, and it lost on quality.**
`scripts/jev_entities.py` takes candidates from a script (every capitalised
token, compound and bold/code/table-cell span, with its first file line) and asks
Jev one Noul per candidate over the 40-line window it first occurs in. Recorded
in `Plan/runs/jev/<slug>/`; `--replay` reruns it with no key.

| | gazetteer F1 | `aegis-subplots` F1 | lines right | time / doc | input tokens / doc |
|---|--:|--:|--:|--:|--:|
| Haiku, revision 1/2 | 0.67 | 0.28 | 85–95% | ~2 min | ~110k |
| Jev, top 100 by p | 0.47 | 0.10 | 99% — by code | 6 s | ~410k |
| every script candidate | 0.09 | 0.04 | — | — | — |

- **Faster by about 20×, cheaper by about 4× in money, not in tokens.** Jev is
  $0.042 per million input tokens and output is free (OpenRouter, 2026-09-23);
  Haiku is $1/$5. The whole corpus, 110,796 lines, is roughly $3 with Jev.
  The token count is high because each of ~2,100 questions per document repeats
  its wording; the state is paid once per window.
- **The candidate script caps recall at 0.80 and 0.63.** It misses multi-word
  names with a space in them (`Externe Ebene`, `Kern-Welt 1`) and splits none of
  the slashed forms (`Juna/V`). That ceiling is code's, and fixable.
- **Jev says yes to 20% of candidates** and ranks cited authors highest
  (`Sartre`, `Camus`, `Chinese_room` from footnote URLs) on `aegis-subplots`. It
  did what the question asked — the definition includes „a cited work or
  author" — which is the same open question the Haiku pilot raised, answered
  more sharply: the definition decides the list, not the model.
- Near-duplicates crowd the top 100 (`Neuromancer`, `Neuromancer (Roman, 1984)`);
  folding parentheticals is code, not judgement.

**What this means:** Jev is not a replacement for a reader here, but it is a
cheap filter behind a better candidate script. The gold lists are noisy too —
each carries a reader's notes as `- ` lines, which no list can match.

**Next, in this order:**

1. Decide whether a one-line stated gap disqualifies a list (above), or have the
   reader of `kohaerenz-protokoll` finish the line.
2. The other landed documents. Four readers cost about 424k subagent tokens; at
   that rate 342 more documents are roughly 36M, scaled by length rather than
   count. Say what the full run costs before starting it, and ask.
3. Then `entities.py matrix`, `missing`, and `doc` on the candidates for the next
   document below.

**Open question the pilot raised:** on `aegis-subplots` the model took the
research vocabulary where the reader took the world (F1 0.13, against 0.67 on the
gazetteer). Which of the two a corpus-wide entity list should hold is the
author's call, and the prompt's definition of an entity is where it would be
written. `Plan/concept/entity-lists_2026-09-23.md` has the argument.

## German and English names — mapped, not merged

`scripts/bilingual.py` maps the German and English surfaces of one entity across
the whole corpus. `Plan/entities/bilingual.md` holds the pairs and
`Plan/entities/bilingual.jsonl` holds every judged entity with its counterparts.

- **stated**: code found 12,526 glosses the corpus writes itself, `A (B)` and `A/B`,
  8,129 of them with at least one side an entity.
- **entities**: Jev accepted 6,989 of 18,026 surfaces as entities or key terms.
  The spot check was sound: `Wächter` 0.83, `Guardian` 0.93, `Ziel` 0.17, `Die` 0.11.
  One article got through, `Das` at 0.73, and the write stage now drops bare articles.
- **propose**: four free models, given names only, proposed counterparts.
  2,312 entities have one the corpus contains, and 34 names were never answered.
- **pairs**: Jev chose one relation for each of the 11,277 pairs:
  3,785 translation (2,474 at p ≥ 0.8), 989 abbreviation, 250 variant,
  2,465 role or part, 3,783 distinct.
- **Cost**: 1,015 Jev calls and 10.9M input tokens, about $0.46. Plus 99 free
  calls, which took 70 minutes, because only `nemotron-3-super` and
  `dots-3-note` answered a batch of 80 reliably.

**What needs a person.** The high tier reads right on the pairs the wiki cares
about: `Kernwelten`/`Core Worlds` in 8 documents, `Überwelt`/`Overworld` in 5,
`Risse`/`Rifts` in 3, `Handlungsfähigkeit`/`Agency`, `Erleben`/`Qualia` in 15.
Even there it holds naming relations Jev called translations: `Logik`/`LogOS` 0.85
is a guardian named for its domain. Below 0.8 the list is noisy, with
`Signposts`/`Transits` 0.63. No pair has entered `judgements.jsonl`. Reviewing the
high tier into it is the next step, and it is a person's.

## Question pages Q6–Q9 — 2026-09-29

On the author's „Read the Wiki and Create new questions in the Wiki“, four questions
that two or more term pages raise, or that the sources name as open themselves, were
promoted to `Wiki/questions/`. Each gathers quotations the term pages already hold; no
document was read, and none was started (the author's word of 2026-09-28 stands).

- **Q6** — the Nexus, the Überraum and the Überwelt: one space, one in another, or three
  (J18, J36, J63, J103). The 2025 Guardians take a form in the Nexus, the worldbuilding
  concept's reside in the Überwelt, the philosophischer Bericht's in KW3 `Überwelt / Nexus`.
- **Q7** — what 734 names: the component, the dwelling, both on purpose (J80).
- **Q8** — AEGIS after the Vortex's fifth beat, and Oblivion taking over its function
  (Appendix C.1 and C.5, OQ-A, OQ-G, as the sources cite them).
- **Q9** — the Moonshine-Link's boundary: what crosses, who feels it, whose it is
  (Appendix C.2, OQ-B, OQ-F).

**What they point at, if reading resumes.** Q8 and Q9 both send the reader to
`kohaerenz-protokoll-struktur-kanon-reset-2026-04-30-md` (792 lines, landed, unread),
whose Appendix C has eight headings, C.1–C.8 (orientation only). Q6 points at
`roman-blueprint-seelen-kohaerenz-protokoll` (2025-04-17; `Überraum` 17, `Nexus` 41 by a
whole-word count) and Q7 at `romanplot-uberarbeitung-kohaerenz-protokoll-teil-1`
(2025-04-18; `Einheit 734` 18). A suggestion, not a start: the author decides when
reading resumes.

**Measured.** `graphrag.py bench` went from 20 cases to 24; the twenty scored as before,
and the four new ones score high because each question names the pages that raise it
(`CLAUDE.md`, *The knowledge graph*).

## Next document — none: the author asked that no new document be started (2026-09-28)

**„Dont start any new documents"** — the author, 2026-09-28, while document 51 was already being read. It
was finished and nothing after it was begun. `chapter_sources.py across` has not been run again, and no next
document is named here. The next session starts from the author's word, not from a reading suggestion.

**Document 51 is done, 2026-09-28**: `an-inquiry-into-the-unresolved-questions-and-thematic-tensio`, the
Inquiry file, about fourteen English reports of 2025, the last of the 2026-09-25 scans. `reconcile-52` is the
record. **No page**; J119 (Dr. Aris Thorne on `lex`), J120 (the English world names on the paged worlds);
readings on 42 pages and `plot.md`; entries in C1, C3, C6, C9, C12, C13, C15 and Q1, Q3, Q5. Retrieval 0.660 →
0.654, only C4. Four Sonnet readers, split by page group; `account.py order` holds again.
- **The file disagrees with itself about the cast**: eight alters with Praetor and Oblivion in four reports,
  eleven with Alex, Lia, Isabelle, Moros and Argus in two, each set calling itself canonical; the last report
  names its sources for the split (Q3). Nyx is „Her" in one report and „his" in the rest. KW4 is the Garden of
  Possibilities in one table and of Potential in another.
- **Readers kept writing comparisons with documents they had not quoted** even with the rule in the brief — „no
  other read source has it", „a year earlier than the 2026 sources", „the only name common to every roster"
  (false: five names stand in both rosters). The session removed each before committing. The rule in a brief
  is not enough; a check that flags „only / no other / first / every other" in a new reading would be.
- **Noticed, no record holds it:** the Inquiry asks what became of the other fragments of AEGIS'
  self-mutilation (L78, on `genesis`); the Assessment's partitioning isolates Juna's resonance from Kael rather
  than splitting AEGIS' Ursprungs-Ich (on `trennungsprotokoll`).

### Previous document — documents 48–50 reconciled

**Documents 48–50 are done, 2026-09-28**: three of the four 2026-09-25 scans — the Charakter-Kompilation
(2026-03-31), the Sensory Rulebook (2025-11-03) and the Hard-Problem-Analyse (2026-04-28).
`reconcile-49` to `reconcile-51` are the records. **No page**; J117 (Landauer-Wärme by the sentence), J118
(a world named twice in one breath goes on the paged world); readings on 33, 20 and 21 pages, Kap 13, 32,
35, 36 and `plot.md`; entries in C1–C6, C8, C9, C11–C15 and Q1, Q3–Q5. Retrieval unchanged at 0.660. Five
Sonnet readers, split by page group.
- **Three absence counts were not zero.** Readers counted `dekanonisiert`, `Ursprungs-Ich` and `Spiegel` in
  document 48 as 0 — the first because the text writes `Dekanonisiert`, the second from a path that did
  not resolve. The session recounted and corrected four Guardian pages, `potentialmeer` and C13, and told
  the readers to count with the full path and case-insensitively as well. A brief should say so from the
  start.
- **Readers again wrote comparisons to documents they did not quote** — „the one read source", „as in
  document 3", „every other read source", „a fourth position", „the earliest-dated source". The session
  removed each before committing. `quotes.py` passes all of them.
- **Noticed, no record holds it:** document 48 gives „Komponente 734" to Lex (C12's entry records it);
  document 49 puts ozone and warmth together in Juna's world, cold or warmth in KW2 (C11); document 50
  attributes thirteen Alters to a „Hard Canon Masterfile" the corpus does not contain, where document 48
  a month earlier counts eleven on a „Hard Canon Status Report" (Q3).

### Previous document — document 47 reconciled

**Document 47 is done, 2026-09-27**: `kohaerenz-protokoll`, the Kohärenz-Protokoll narrative of
2025-04-27, 50k words, read on its own in parts. A foreword, a Genesis of AEGIS told from an Ich, „ab hier
nur Konzept", then 22 chapters of prose — Kael, K-1123, a fragment of M, through Co₁, McL, Beta-Rho-5 and
Ly, each with its own Guardian (LogOS, Netzweber, Chaos-Regulator, Möglichkeits-Weber). Research, like
every narrative text. `reconcile-48` is the record. **No page**; J113–J116; readings on 24 pages, Kap 1–12
and 14–23, `plot.md`, entries in C2–C7, C11, C12, C14 and Q1, Q3–Q5. Retrieval unchanged at 0.660. Six
Sonnet readers, split by page group.
- **Its chapter order does not hold**, and the pages say so without reordering: no Kapitel 13; Kapitel 17
  („Zyklus 2") opens after the collapse Kapitel 18 („Zyklus 1") averts; 17 and 20, 21 and 22 share their
  headers; Kapitel 23's closing report names Kapitel 17's project.
- **21 of 379 candidates counted 0** because they stand only in capitalised system messages and the count
  matches case. A text whose system speaks in capitals needs its list written in the case it stands in, or
  a note beside the count — briefing material.
- **Readers overreached in difference lines, and the session caught it by reading them**: a Wächterin
  made into Juna (`kap-08`), new „positions" on C7 and C11 in chapters that take none, ordinal counts of
  titles no one had counted, `734` called Kael's own designation, a guessed descent of the Mosaik-Herz
  name, sentences joined with `[…]`. `quotes.py` passes all of these; only reading finds them.
- **Noticed, no record holds it:** the Evaluierungseinheit is the room of the first partitioning in its
  Kapitel 2, where other sources make it a later place where personas collapse (on
  `evaluierungseinheit`); `RIVE` is AEGIS' validation engine here and a Guardian in the philosophischer
  Bericht (on `guardians`, `aegis`); M is both what Kael is a fragment of and the Monster group. The unread
  `an-inquiry-into-the-unresolved-questions-and-thematic-tensio` writes the case number `734-K-1123`, which
  joins this document's two designations.


### Previous document — documents 44–46 reconciled

**Documents 44–46 are done, 2026-09-27**: the three unread documents highest in the chapter tables after
the four whole-novel plans — the Duale Storyform-Synthese (2026-04-28), the AEGIS-Analyse (2026-04-30,
the earlier run of document 40's report) and the M-Fundament-Blueprint (2025-04-26, document 43's
companion, in beats). `reconcile-45` to `reconcile-47` are the records. **No page**; J112 (`T-734`);
readings on 28, 26 and 9 pages, Kap 8, 9, 11, 18, 24, 28, 32, 35, 36 and `plot.md` (a twelfth plan with
one Vortex). Retrieval unchanged at 0.660. Four Sonnet readers, split by page group.
- **Noticed, no record holds it:** two runs of one report disagree — document 40 makes AEGIS after the
  Vortex a „parakonsistente Proto-Bewusstheit", document 45 a broken loop (on
  `algorithmische-melancholie`); and their Witness layers fall in different beats (on `vortex`). The
  Duale Storyform-Synthese puts Kael in the MC of *both* storyforms and AEGIS in B's IC, the AEGIS-Analyse
  two days later AEGIS in B's MC — the throughline question C8 assumes settled. The Duale
  Storyform-Synthese's corpus lists the Mosaik-Herz and T-734 among thirteen alters.
- **A reader altered a quotation, and `quotes.py` could only call it unchecked**: C3 quoted „temporäre
  Entitäten", citing a line range in parentheses rather than `^[…]`, so the checker counted it as uncited
  instead of comparing it; the session found the altered words by grepping the corpus. An uncited
  quotation is counted, never compared — the 0-unchecked rule is what catches it.

Next: `kohaerenz-protokoll` (2025-04-27, 50k words, 18 chapters in the tables) — read it on its own, in
parts. Then the four unread 2026-09-25 scans named below.

### Previous document — the four pre-2026 plans reconciled

**Documents 40–43 are done, 2026-09-27**, on the goal „ingest the next sources": the four whole-novel
plans *Reading suggestion — next* named after the canon era. `reconcile-41` to `reconcile-44` are the
records. **No page**; J107 from document 40, J108–J111 from 41–43; readings on 31, 43, 43 and 12 pages,
every chapter page from Kap 1 to Kap 39 from 41–43, `plot.md` (fourteen plans now count no Vortex), entries in every record but C13 and C15.
- **Retrieval** 0.644 → 0.660, C11 and C4 up.
- **A usage limit stopped six readers mid-run.** Their finished files were checked and committed; the
  rest was redone. **The author, 2026-09-27: every subagent runs on Sonnet** — the readers after that
  did, and their files passed `quotes.py` as the others did.
- **Two process traps the readers found**: a straight `"` in prose between two „…" quotations makes
  `quotes.py` read everything between them as one quotation; and a chapter link written as
  `[[../chapters/kap-35|…]]` points at no page — chapter pages are linked `[[kap-35|…]]`.
- **Noticed, no record holds it:** in the Hard-SF-Outline Silas, the Coheron-Echo, is a freezing
  (L108), where nearly every source gives Juna's echo warmth (on `hitze-polaritaetsregel`, not in C11);
  the Ultra-Plot calls both Silas and Rhys „Pfleger" and has Kael *be* AEGIS in Kapitel 35 (C3); the
  Primzahl-Blueprint alone lets the alters fuse (Kapitel 27), against every other read source's „no
  fusion"; the Hard-SF-Outline and the Ultra-Plot both pair five Guardians with four worlds, as the two
  2025 documents do (C6 — the author's five stands, and the pairing is Q5).

Next, by `chapter_sources.py across`, the unread documents in most chapter tables:
`kohaerenz-protokoll` (2025-04-27, 18 chapters), `duale-storyform-synthese-kohaerenz-protokoll`
(2026-04-28, 17), `dramatica-storyform-synthese-aegis-analyse` (2026-04-30, 15 — the earlier run of
document 40's report, check `duplicates.py` first) and `m-als-fundament-der-simulation` (2025-04-26, 15,
beside the Primzahl-Blueprint of its date). Four of the ten 2026-09-25 scans are still unread:
`an-inquiry-into-the-unresolved-questions-and-thematic-tensio`, `charakter-kompilation-fuer-kohaerenz-protokoll`,
`ki-prompt-analyse-hard-problem-of-consciousness`, `the-sensory-rulebook-the-body-as-a-measuring-device-in-the-p`.

### Previous document — the last eight canon-era documents reconciled

**Documents 32–39 are done, 2026-09-27**, on the goal „ingest the next sources": the eight canon-era rows of
2026-05-08 that were still unread, all English. Each has its own candidate list, census and note;
`Wiki/compare/reconcile-33` to `reconcile-40` are the records. **No page**; J104–J106 from document 32;
readings on 23–49 pages each, Kap 1, 35, 36, 39, `plot.md`, entries in every record. **All 33 canon-era
documents are now read.**
- Documents 33–39 were reconciled together by six readers split by **page group**, not by document, so
  no two readers edited one file; each reconciliation record says so.
- **Retrieval**: 0.644 → 0.654 (document 32) → 0.644 (33–39), only C11 each time.
- **Briefing v19** asks about a document in another language, and measures the lens check skipped twice.
- **Readers' process slips**, none in the result: two ran a read-only `git` command, two regenerated
  `Wiki/index.json` mid-run (re-derived at the end), and a shared scratch helper was overwritten once and
  wrote wrong frontmatter on `kohaerenz-kernel`, repaired by its reader. Give each reader its own scratch
  folder in the brief.

Next: the canon era is exhausted. *Reading suggestion — next* is read too. The next sources are the pre-2026
whole-novel plans named there — `monstergruppe-primzahlen-plot-blueprint`,
`hard-sf-roman-outline-dkt-physik-cosmic-horror`, `dramatica-storyform-synthese-aegis-analyse-2`,
`roman-konzept-dualitaet-kohaerenz-spannung` — or whatever `chapter_sources.py run`, rerun, ranks first.

### Previous document — the philosophischer Bericht reconciled

**The thirty-first document is done: `kohaerenz-protokoll-philosophischer-bericht-md`, 2026-09-27.** „Kohärenz Protokoll — Theoretisches Fundament", 2026-05-08 — item 5 of *Reading suggestion — next*, the document the Jules session had half-ingested (decision 014). 475 candidates written while reading, **no page**, readings on 57 pages, `plot.md` and Kap 13, 35, 36, entries in twelve conflicts (C8, C13, C15 read and unchanged) and all five questions, J100–J103, five sweep hits (all readings). `Wiki/compare/reconcile-32-kohaerenz-protokoll-philosophischer-bericht-md.md` has the record.
- **The Jules entries stay.** Their citations (`^[slug:Lnn]`, no `.md`) had never been checked; they are qualified now and hold, one split where it joined two statements. Each record's reconciliation entry follows and says what the document does not bear out. Kap 13's stray section became a reading; a duplicate line the merge left in C7 is gone.
- **J100–J102**: `Separation Protocol`, `Component 734`, `Phone-Silence` placed on the German pages by the sentence, no surface from one source. **J103**: „Überwelt / Nexus" is a reading on both pages.
- **Not promoted**: the Witness-Function, Mutual Information, the Holon-Spiegelachse, the Foundation/Strange Attractor, the Gardener's Axiom, `RIVE`.
- **Its own tensions**, recorded on the pages: two voice rules for AEGIS; Juna invisible (L262) and „nicht, weil sie unsichtbar ist" (L339); the Moonshine mechanism a VOA and VOA „nicht Canon" (L405, L705); „Kaels K₀-Trauma" (L571) against his cycles as the true K₁ (L225).
- **Briefing v18** asks about a figure drawn in spaces that splits a compound across lines.
- **A number after a word cannot be quoted**: „bauen 39 Kapitel“ (L41) — the footnote rule drops `39`, so `read.py --find "39 Kapitel"` refuses the line. The census writes it as a term; the rule is `quotes.py`'s, unchanged.
- **Retrieval**: PageRank recall@8 0.637 → 0.644, only Q5.

Next: every item of *Reading suggestion — next* is read. Rerun `python3 scripts/chapter_sources.py run` so the chapter tables stop listing the seven documents read since, then choose from them — or one of the four whole-novel plans named there. `chapters.py missing` still lists 98 <!--state:chapters.missing--> single-`Kap` mentions.

### Previous document — the Dual-Storyform background document reconciled

**The thirtieth document is done: `dual-storyform-hintergruende-md`, 2026-09-27.** „Dual-Storyform — Hintergründe & konzeptuelle Genealogie", 2026-05-08, the companion to the Dramatica status report of 2026-05-07; read on the author's „Lese das übernächste file ein" — the second of *Reading suggestion — next*, so item 5, `kohaerenz-protokoll-philosophischer-bericht-md`, is still unread. 426 candidates, **no page**, readings on 39 pages, `plot.md` and nine chapters (Kap 1, 13, 28, 33, 35–39), entries in C2, C4, C6, C7, C8, C11, C12, C14 and all five questions, J98 and J99, two sweep hits (a reading, a title). `Wiki/compare/reconcile-31-dual-storyform-hintergruende-md.md` has the record.
- **If another session reads item 5 in parallel**, it will also take document number 30 and `reconcile-31-…`. Whichever merges second renumbers its record to 32 and its prose to document 31; `account.py order` compares `state_before` with the previous run's `state_after`, and both runs here leave 106 pages and 15 conflicts, so the order check holds either way.
- **J98, J99**: the document writes the kernels only as `K1`/`K0` with plain digits; placed on `kohaerenz-kernel` and `kollaps-kernel` by the sentence, not mechanised. Briefing v17 asks about a plain digit for a subscript.
- **Not promoted, and worth a page gathered across the read sources**: Mutual Information (in eight read documents) and Lebende Dialetheia (in twelve), each defined in one glossary line here (L487, L484) — the Truth-Rotation's precedent (document 20).
- **Noticed, not recorded**: which Vortex beat reveals the Genesis — Beat 4 here (L368, a recommendation it attributes to a Reset-Doc), Beat 3 in the strukturierter Outline — a line on `vortex`, not a record. C12 now holds three candidate fourth beats. This is the first read source to count **four** old Guardians where the others count five. It drops the Chaitin constant where the other sources of its date give it to Juna. Inside itself: „12 Protokolle" (L210) against „Reduziert auf 3" (L469), and Akt III from Kap 27 (L335) against „ab \~Kap 28 … Akt-III-Anfang" (L308).
- **Corrected on the way**: `truth-rotation`'s „Kael = K₁, in every reading" and `vortex`'s claim that `plot.md` read one Vortex for the master report alone.
- **`link.py` found 17 unmarked links already pending on `main`**, in readings of earlier documents; only the three in this document's new sections were marked, so as not to change pages without naming their source.
- **Retrieval**: PageRank recall@8 0.637, unchanged.

Next, by *Reading suggestion — next*: `kohaerenz-protokoll-philosophischer-bericht-md`. The chapter tables still list the six documents read since `chapter_sources.py run` was last run.

### Previous document — the Kap-25 session log and chapter file reconciled


**The twenty-eighth and twenty-ninth documents are done: `2026-09-14-kap25-vertiefung-md` and `kp-kap25-2026-09-14-md`, 2026-09-26.** Both of 2026-09-14, the newest in the corpus, and read in that order: the log first, then the chapter it reports on. **No page from either**, no new judgement.
- **Document 28, the session log** — 153 candidates; readings on 15 pages, `plot.md` and Kap 24–26; entries in C6, C9, C11, C14 and Q5; two sweep hits (a reading, a title). `Wiki/compare/reconcile-29-2026-09-14-kap25-vertiefung-md.md`. A log about a chapter it does not contain: every reading says „the log reports". Its largest open question is C9's (above, *Questions for the author*).
- **Document 29, the chapter file** — 166 candidates; readings on 9 pages and Kap 25–26; entries in C9, C11, C14; no sweep hit. `Wiki/compare/reconcile-30-kp-kap25-2026-09-14-md.md`. Research, by the author's word. Its prose names no one — `Kael` and `AEGIS` stand only in its apparatus — so every reading names the voice it quotes and supplies no name: ozone, the Telefon-Stille and Juna's evenings are rendered, never named.
- **Retrieval**: PageRank recall@8 0.643 → 0.637 after document 28, only C4 (`cerberus` out of its top eight, `alters` in — the hub again); document 29 moved nothing.
- **A defect repeated**: an unquoted heredoc ran backticks in the reconciliation script once more and blanked words; it was caught before any write was committed and the record rewritten from a quoted script.
- **Noticed, not fixed**: a quotation that begins with a number the line has after a word („41 Kapiteldateien") does not resolve in `quotes.py`, while the same words from the word before do — the glued-footnote rule drops it on the line side only. `kern-welten`'s frontmatter holds one more `ingested:` entry than `sources:`. `alters`' *Open* is still stale.

Next, by *Reading suggestion — next*: `kohaerenz-protokoll-philosophischer-bericht-md`, then `dual-storyform-hintergruende-md`. The chapter tables still list the five documents read today until `chapter_sources.py run` is rerun.

### Previous document — the philosophy catalogue reconciled

**The twenty-seventh document is done: `kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md`, 2026-09-26.** 403 candidates, **no page**, readings on 39 pages, `plot.md` and nineteen chapters (Kap 0, 1, 3, 6, 8, 11, 15–18, 22, 27, 30, 33, 35, 36, 38–40), entries in nine conflicts (C4–C7, C9, C11–C14) and four questions (Q1–Q3, Q5), no new judgement, three sweep hits (two readings, one title). The seven scan readings of it held against the full document. `Wiki/compare/reconcile-28-kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md.md` has the record. Chosen as next on *Reading suggestion*.

- **A catalogue of schools whose vocabulary the prose may never use** — „Kein philosophischer Begriff erscheint im Prosatext." (L773). Section labels `[K]`/`[V]`/`[S]`/`[L]`, recorded, not applied. Nearly all its unmatched candidates are lens.
- **`plot.md` moved**: 39 fragmented chapters inside a Kap 0/Kap 40 frame, two Vortices, no Kap 37.
- **It places five things twice and flags none** (Gödel-Gambit Kap 30/35, ANP/EP barriers Kap 35/Beat 2, Kap 16's two titles, the Wir's decision Kap 38/39, 39 chapters and a frame); every page concerned gives both.
- **Retrieval fell**: PageRank recall@8 0.659 → 0.643, C11 and Q3, displaced by the hub pages this document read onto. Recorded in `baselines.jsonl`.
- **A defect in my brief**: it cited J32 for world names carrying a Guardian's name; the rule is J49. A reader noticed; `mnemosyne` was corrected in its own commit.
- **Noticed, not fixed**: `read.py --find` refuses a short phrase with a number („Kap 17") — the count still finds it; `alters`' *Open* is still stale.

Next, by *Reading suggestion — next*: `2026-09-14-kap25-vertiefung-md` and `kp-kap25-2026-09-14-md`. The chapter tables still list the three documents read today until `chapter_sources.py run` is rerun.

### Previous document — the worldbuilding concept reconciled

**The twenty-sixth document is done: `worldbuilding-konzept-kohaerenzprotokoll-md`, 2026-09-26.** 418 candidates, **no page**, readings on 56 pages, `plot.md` and nine chapters (Kap 1, 11, 13, 14, 33–36, 39), entries in fourteen conflicts and all five questions (C8 unchanged), no new judgement, four sweep hits (all readings). The six scan readings of it were checked against the full document. `Wiki/compare/reconcile-27-worldbuilding-konzept-kohaerenzprotokoll-md.md` has the record. Chosen as next on *Reading suggestion*.

- **A world bible that ranks itself last**: „nicht als Source-of-Truth" (L968), below „Memory" and a „Reset-Doc" — recorded, not applied. Much of it is the konsolidiertes Konzept's text of the same date, word for word.
- **Two Guardians** (C6, the author's five stand), **three protocols** (Q2), AEGIS' **expansion** (C1), **three Genesis beats**, the fourth „offen" (C12), **heat and ozone one Landauer signature** (C11), **a third 39-chapter plan with one Vortex** — `plot.md` corrected to „every plan but three".
- **Juna in two roles** — the question under *Questions for the author* (J68/J75) now has this document too.
- **`quotes.py` had a blind spot**: a cited quotation under eight characters matched nothing, and a false „(Ch13)" citation of another document stood on `evaluierungseinheit`. Fixed, with three self-test cases.
- **How it was read**: the session read the document and wrote the list, census and note; seven Claude readers in the container wrote readings, record entries and chapter readings from one brief, each file reviewed, quote-checked and committed on its own. Once, the session ran `git stash` on the shared tree by mistake and popped it seconds later; every file was checked afterwards and none had lost an edit.
- **Noticed, not fixed**: `alters`' *Open* says the roster lives in documents not yet read; `realitaetsebenen`' *Open* says six levels rest on one source; `residual-echos`' *Open* says no Kap-40 text is read. All three were stale before this document.

Next, by *Reading suggestion — next*: `kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md`. The chapter tables still list the two documents read today until `chapter_sources.py run` is rerun.

### Previous document — the second narrative text of Kap 0 reconciled

**The twenty-fifth document is done: `koharenz-protokoll-kapitel-0-v2-md`, 2026-09-26.** 153 candidates, **no page**, readings on 15 pages and on Kap 0, six conflicts moved (C3, C7, C10, C11, C12, C14), J97, one sweep hit (a reading). `Wiki/compare/reconcile-26-koharenz-protokoll-kapitel-0-v2-md.md` has the record. Chosen as first of *Reading suggestion — next*, by the morning scan's grep. Research, by the author (2026-09-26), like documents 22 and 23.

- **The annotated text's prose without its apparatus.** 58 of its 102 long lines stand in `kap0-v1-annotiert-md` unchanged, 36 more revised (`Plan/runs/koharenz-protokoll-kapitel-0-v2-md/06-against-v1.txt`). No rules, no annotation, no movement numbers, no „Übergang zu Kap 1" heading.
- **No figure is named — and never was in the prose.** `AEGIS`, `Kael`, `Juna`, `734` and every alter stand 0 times; in the annotated text too every name was in its annotations and rules. So the handover's questions have their answer: the Alex Vorform, Nyx's knuckles, „gerade diese Komponente wird Kael" and warmth as Juna's were all the annotation's claims about the prose, not the prose. Readings here name the register and never the speaker.
- **C10**: the knuckles in Kap 0, in a line with no speaker (L607). **C11**: warmth at the first contact (L99), heat in the analysis and the air of the separation, no ozone, no Landauer. **C12**: a component with its number withheld (L235), a component eliminated (L591), shards, then an unnamed Ich counting tiles (L635–639).
- **The formula in a third form**, „*Es ist, was es verhindert, dass es nicht ist.*" (L211) — `formel-inversion`'s lead extended. `residual-echos`' lead said only one text uses the name; two do, of one date. `komponente-734`'s „the sources agree it becomes Kael" narrowed to the sources that name Kael.
- **J97**: a German case ending is not a term boundary. **Briefing v14** asks about a text whose grammar is its only label. One zero, `innerer Raum`: the `read.py --find` step skipped once.
- **Noticed, not fixed**: `residual-echos`' *Open* says no Kap-40 draft is among the read documents, which the page's own reading of document 22 contradicts; no document of this run caused it.

### Previous document — the 39-chapter spec reconciled

**The twenty-fourth document is done: `three-mode-architecture-39-chapters-md`, 2026-09-25.** 338 candidates, **no page**, readings on 29 pages and on every chapter from Kap 1 to Kap 39, four conflicts and three questions moved (C7, C11, C12, C14, Q1, Q3, Q4), no new judgement, three sweep hits (one reading). `Wiki/compare/reconcile-25-three-mode-architecture-39-chapters-md.md` has the record. Chosen because the annotated Kap 0's handover named it.

- **Very likely the spec the Konzept-Iteration Genesis extends.** A spec of three modes and 39 chapters, 2026-05-08 by the manifest, whose Kap-6 and Kap-36 cells stand in that document word for word. It names no date of its own, so this is the reconciliation's identification, not the document's.
- **39 chapters, one Vortex, no Kap 0, no Kap 40.** `plot.md` said only the master report had one Vortex; corrected to two plans.
- **Its storyform boundary stands twice**: 34/35 as the turn (L83), 36/37 in the closing notes (L634).
- **C11**: warmth in Kap 6 and Kap 36 Beat 4, in nearly the konsolidiertes Konzept's words. **C12**: „Einheit → Trennungsprotokoll → Kael=Komp 734" as flashbacks in Kap 18–22. **C14**: AEGIS-POV scenes from Kap 14, the person unsaid. **Q1**: Guardians as sub-antagonists in Kap 32. **Q4**: an unnamed Wächterin in Kap 8 and 17.
- **Chapter readings from table rows.** The rows are numbered without `Kap`, so `chapters.py missing` cannot see them; all 39 were read from the tables.
- **The five scan readings of it stand** (`vortex`, `kishotenketsu`, `goedel-gambit`, `residual-echos`, `komponente-734`).

Next, by a qmd search over every open record (`Plan/runs/qmd-scan-2026-09-26/README.md`, 2026-09-26): **`koharenz-protokoll-kapitel-0-v2-md`** (2026-05-17, 639 lines) — the annotated Kap 0's clean text with its own review carried out: no passage it marked for deletion stands, Alex's Vorform line is gone, the knuckles stay (L607), and the formula has a third form, „*Es ist, was es verhindert, dass es nicht ist.*" (L211) (`grep`, orientation only). It speaks to the Alex question, C10, C12 and `formel-inversion`. Then `kohaerenz-protokoll-philosophischer-bericht-md` (2026-05-08, hit for 16 records, never scanned), the two Kap-25 documents of 2026-09-14 (the newest in the corpus), and the two scanned ones, `worldbuilding-konzept-kohaerenzprotokoll-md` and `kohaerenz-protokoll-philosophie-im-detail-2026-06-10-md`. `chapters.py missing` still lists 98 <!--state:chapters.missing--> single-`Kap` mentions.

### Previous document — the annotated Kap 0 reconciled

**The twenty-third document is done: `kap0-v1-annotiert-md`, 2026-09-25.** 353 candidates, **no page**, readings on 29 pages, six conflicts and two questions moved (C3, C7, C10, C11, C12, C14, Q3, Q5), J96, one sweep hit (a reading). `Wiki/compare/reconcile-24-kap0-v1-annotiert-md.md` has the record. Chosen because the draft of Kap 40 and Kap 0's handover named it.

- **A draft that reviews itself.** Ten hard rules (R-1 to R-10), the prose, and under every passage its writer's note — Funktion, Was funktioniert, Risiko — then the defects by severity and questions for an external reviewer. A reading from it names its voice: prose or annotation.
- **The handover's two questions, answered: both changed between the drafts.** The knuckles enter Kap 0, in Nyx's voice as the separation runs (L977, C10) — the „Knöchel-Eruption" the later sources put there. And the component becomes Kael, „gerade diese Komponente wird Kael" (L433, C12), where the draft of 2026-05-08 cut Kael out of 734.
- **J96**: an alter's Vorform is not the alter, and gets no page; the annotation states the alter's syntax signature, so it is a reading on the alter's page. Eleven readings, Moros to Oblivion.
- **The formula in the first person**, „*Ich bin, was ich verhindere, dass ich nicht bin.*" (L389) — `formel-inversion`'s lead corrected.
- **H4 without a type** (L689) is `blinder-fleck` shown rather than named; the status lines are `aegis-metriken`'s first reading from a narrative text.
- **The Alex conflict is now read from its source**: the document names it itself (L1205), *Questions for the author*.
- **The scan's `genesis-klammer` reading said this draft came before any Kap 40**; the read draft of both frames is nine days older. Corrected.
- **Briefing v12 held**: five zeros, all the export's escaping (`\_`, a hyphen split by a wrap), none a nominative.

Next, by the open records: `three-mode-architecture-39-chapters-md` (2026-05-08), named twice now — perhaps the „Spec-Dokument vom 2026-05-08 (drei Modi, 39 Kapitel)“ the Konzept-Iteration Genesis says it extends, and one of the ten scanned; it speaks to the Kap-40 question and the one-Vortex-or-two finding. Then the `Ursprungs-Ich` question above.

### Previous document — the draft of Kap 40 and Kap 0 reconciled

**The twenty-second document is done: `kohaerenz-protokoll-kap40-und-kap0-fassung-2026-05-08-md`, 2026-09-25.** 97 candidates, **no page**, readings on 17 pages, seven conflicts moved (C2, C3, C7, C10, C11, C12, C14), J95, two sweep hits (both readings). `Wiki/compare/reconcile-23-kohaerenz-protokoll-kap40-und-kap0-fassung-2026-05-08-md.md` has the record. Chosen because the Abhandlung's handover named it.

- **Narrative text, not a plan** — research, by the author (2026-09-26). It calls itself a first draft, Kap 40 written before Kap 0. Every reading from it is a voice's — the Funken-Ich's first person, AEGIS in the third, Kap 40's Wir.
- **The Abhandlung's three Setzungen are all in it** (*Questions for the author*, above).
- **J95**: `Innere Weite` is an alias of `ueberwelt` — three plans gloss one with the other, and the draft defines it as AEGIS' inner simulation space where Kael's remainder is left.
- **Kael arises twice**: in Kap 0 as what the Trennungsprotokoll cuts away (L485, L505), in Kap 40 as „das Cluster, das aus Komponente 734 herausgetrennt wurde" (L63). C12.
- **Kap 0 as written has no knuckles** (C10), and gives the Konstrukt-Stadt ozone „ohne dass jemand weiß warum" (C11).
- **`formel-inversion`'s lead was false after it** — the draft writes „Wir-AEGIS sind, was Wir-AEGIS bewahren" — and is corrected.
- **The nominative defect again**: five zeros, the morning after briefing v11 asked about it. Briefing v12 makes it a step: `read.py --find` before a phrase goes on the list.

Next, by the open records: `kap0-v1-annotiert-md` (1237 lines, 2026-05-17) — the annotated Kap 0 nine days later, one of the ten scanned. It would say whether the knuckles (C10; `Knöchel` on 2 of its lines, `grep -c`, orientation only) and the Kael/734 order (C12) changed between drafts. Then `three-mode-architecture-39-chapters-md`, still named, and the `Ursprungs-Ich` question above.

### Previous document — the Doppel-Klammer Abhandlung reconciled

**The twenty-first document is done: `kap0-kap40-doppelklammer-abhandlung-2026-05-08-md`, 2026-09-25.** 183 candidates under decision 012's list rule, **one page** (`formel-inversion`, gathered from all eight read sources that name it), readings on 14 pages, five conflicts and Q3 moved, J94, one sweep hit (the title, an occurrence). `Wiki/compare/reconcile-22-kap0-kap40-doppelklammer-abhandlung-2026-05-08-md.md` has the record. Chosen because the master report's handover named it. It was one of the ten scanned documents, so `genesis-klammer`, `vermittler-stimme`, `residual-echos` and `komponente-734` already carried it; their readings stand. And `account.py order` holds again.

- **A proposal, not a plan.** It asks for three Setzungen to be confirmed (*Questions for the author*, above) and decides none.
- **C12**: four beats, Beats 2 and 3 in Kap 0, Beat 4 in Kap 39, Beat 1 nowhere. **C11**: warmth as Juna's trace in Kap 0; cold is AEGIS' manner, never a sensation. **C8**: Be-er / Do-er, Kap 0 and Kap 40 built on the pair. **C14**: Kap 0 in the Funken-Ich's first person. **C7**: Juna felt, not seen. **Q3**: `Mira`.
- **Kap 40's last line**: „laut Konzept" it is „Wir tragen die Scherben" — and both concept documents of the date read end on „Wir tragen die Welt". The Kap 40/Kap 0 Fassung of 2026-05-08, unread, holds the Scherben line (`grep -c`, orientation only).
- **Two findings for the briefing** (version 11): four candidates counted zero because the list wrote phrases in the nominative, and a claim of absence — nothing cold — was false and no check could have caught it. Both are questions in `Plan/briefings/extract.md` now.

Its handover named `kohaerenz-protokoll-kap40-und-kap0-fassung-2026-05-08-md` (513 lines, 2026-05-08) — the prose of both frames, which this treatise prepares and whose Kap 40 ends on the Scherben line. It would say whether the Setzungen were taken. Then `three-mode-architecture-39-chapters-md` (646 lines, 2026-05-08), still named from the master report's handover, and `kap0-v1-annotiert-md` (1237 lines, 2026-05-17).

### Previous document — the konzept master report reconciled

**The twentieth document is done: `kohaerenz-protokoll-konzept-master-md`, 2026-09-25.** 480 candidates under decision 012's list rule, **one page** (`truth-rotation`, gathered from all eight read sources that name it), readings on 46 pages, thirteen conflicts and five questions moved, J89–J91, three sweep hits (all readings). `Wiki/compare/reconcile-21-kohaerenz-protokoll-konzept-master-md.md` has the record. Chosen because the Sprach-DNA's handover named it.

- **The plot**: „39 Kapitel, 3 Akte, Vortex Kap 35–36“ (L21), one Vortex and a resolution in Kap 37–39 — dated the day the konsolidiertes Konzept counts 41 movements and two Vortices. Two lines of `Wiki/overview/plot.md` that said every 2026 plan agrees were false and are corrected there (*Kap 40*, above).
- **C15**: Flight to Lia and Isabelle „implizit“ (L1049), and no alter in the roster carries Flight (J89). **C12**: three beats, locked. **C8**: Do-er, the 2026-05-07 correction named. **C11**: heat and ozone as one signature of AEGIS' erasure. **C7**: a revelation in Akt II, no chapter.
- **Truth-Rotation**: the sources agree AEGIS = K₀ and part on what the name points at — the inversion (this document) or the moment in the Vortex the reading turns (four later sources, which call the inversion the `Große Inversion`; J91). Recorded on the page, no conflict record. Whether it should be one is yours to say.
- **`quotes.py` stopped a case error before commit**: a nominative typed for the line's dative (`Wiki/compare/`, the record's last section).
- **Read twice.** A second, independent reading (pull request #94) is kept as `03-candidates-blind-1.md`: `agree.py` F1 0.76, 361 terms shared, each list holding 76–77 % of the other. It added J92 and J93 (clipped words: `Komp 734`, `Erason-Op`), the KW2 question above, two briefing questions, and two tool fixes: `chapters.py` read `Kap 14–\\\~20` as a single Kap 14, and `link.py` marked a term its page already linked again on every run (24 such links pending on this day's pages). It made the opposite call on one page: it read the report onto `hitze-polaritaetsregel` by J62, where main's reading declines it (no polarity rule is stated) — main's call stands.

Its handover named `kap0-kap40-doppelklammer-abhandlung-2026-05-08-md` (616 lines; `Kap 40` 78 times, `grep -c`, orientation only), which the Plot-Konkretisierung's handover named as well, for the Kap 0/Kap 40 frame now that two plans of 2026-05-08 disagree on it. Then `three-mode-architecture-39-chapters-md` (646 lines, 2026-05-08), which may be the 39-chapter spec the Konzept-Iteration Genesis says must be extended (its L818).

### Previous document — Sprach-DNA reconciled

**The nineteenth document is done: `koharenz-protokoll-sprach-dna-2026-05-13-md`, 2026-09-25.** 194 candidates under decision 012's list rule, no pages, readings on 32 pages, eight conflicts and four questions moved, J88, one sweep hit (the title, an occurrence). `Wiki/compare/reconcile-20-koharenz-protokoll-sprach-dna-2026-05-13-md.md` has the record. Read while the other session read `kp-plot-konkretisierung-13-ideen-f1-faden-2026-06-10-md` (document 18, below), which its handover had named: documents 16 and 17 had each been read twice. Main took that reading first, so this one is document 19, reconciliation 20 and J88.

- **C14**: AEGIS in the third person, never `ich`, with an „Operative Interiorität“ (L37) — a third form beside the older sources' no inner view and the lock's first person.
- **C11**: Landauer warmth „spürbar als Ozon-Geruch oder Hitzeschlieren“ (L233) — both sides in one sentence, before the lock.
- **C7** Kap 38; **C10** the knuckles in Nyx's voice; **C5** KW4 is the garden; **Q3** a dominant voice per world, one of them Mnemosyne.
- **Both sessions found the same two tool defects on the same day**, neither knowing of the other: a prose bullet read as a candidate, and a quotation that begins with a number after a word (document 18's bullets below; `Plan/learnings/extract-terms.md`).
- **The list cannot hold `1. Person`**: a `- ` line with a period and a space is read as prose, so the document's point-of-view vocabulary was counted by hand (`05-verify.txt`).

Next, by the open records: `kohaerenz-protokoll-konzept-master-md` (1123 lines, 2026-05-08) — `Ozon`, `Landauer`, `734`, `Flight`, `Knöchel`, `Be-er`/`Do-er` and `Erasure` all occur (`grep -ci`, orientation only), so it can speak to C8, C10, C11, C12, C14, C15 and Q5. The other session's handover (document 18, below) names `kap0-v1-annotiert-md` and two Kap 40 files, not this one.

### Previous document — Plot-Konkretisierung

**The eighteenth document is done: `kp-plot-konkretisierung-13-ideen-f1-faden-2026-06-10-md`, 2026-09-25.** 581 candidates, no pages, readings on 31 pages, six conflicts and two questions moved, J87, one sweep hit (the title, an occurrence). `Wiki/compare/reconcile-19-kp-plot-konkretisierung-13-ideen-f1-faden-2026-06-10-md.md` has the record. Chosen for C11 and C12. **It is a proposal**: everything is `[V]` unless it cites a `[K]` lock, and every reading from it opens by saying so.

- **C11**: the cold side as a plot. Cold ozone follows every Ausgleich. Kap 6 is cold, filtered against the Source-of-Truth's own §7 conflict. Kap 36 Beat 4 is the „einziger kanonischer Landauer-Wärme-Ort“. Silas' warmth is the Coheron-Echo.
- **C12**: 734 is consolidated in Kap 0. The flashbacks run Cluster → Trennungsprotokoll → 734. No beats are counted. Kap 40 echoes the Trennungsprotokoll as „Bewegung 4“, a numbering this document does not lay out; it uses the same word for its 41 chapter units.
- **C7** Kap 38 Beat 3; **C14** one first-person chapter in Kap 5–8; **C6/Q5** two Guardians, LogOS a decanonised name; **C4** AEGIS „kann einen Innentäter nicht denken“; **Q4** a „Wächterin-Stufe“.
- **`fold()` merged `A:RS` with `ARS`** — Storyform A's Relationship Story filed as a reading on a protocol's page. It keeps the colon now (J87); the self-test fails on the old code. The ledger has 74 labelled pairs.
- **`quotes.py` cannot check a quotation that begins with a number standing after a word on its line.** The footnote rule drops „41“ from „die 41 Bewegungen“ on the line side but not from the quote „41 Bewegungen“, so a correct quotation fails. Worked around by quoting the word before; not fixed. A fix needs a self-test case that fails on the current code.
- **Two lines of the reader's observations were counted as candidates.** `capture.py` reads a `- ` line with a comma as prose and one without as a term, so observations belong in paragraphs, not bullets. The list stays as counted: the census says 581 and names the two.

**Kap-2 evidence pilot.** [`Plan/concept/chapter-evidence-pilot_2026-09-25.md`](Plan/concept/chapter-evidence-pilot_2026-09-25.md) compares the existing draft, dated chapter plan, F1 proposal and read-only NCP. The return of sequence 114, the 204/211 spatial discrepancy and the foreign syntax are already in prose. F1-1 — whether work deviations necessarily are K₁ traces — remains an author decision; the draft does not establish that ontology.

Next, by the open records: `kap0-v1-annotiert-md` (1237 lines, 2026-05-17) — the file this document cites for Kap 0, the `DATENTYP_FEHLT` line and 734's placement, with 45 lines holding `Bewegung` (`grep -c`, orientation only). The drafting manual's Alex conflict sits in its „Bewegung 4“ (C12). Then the Kap 40 question above: `kap0-kap40-doppelklammer-abhandlung-2026-05-08-md` and `kohaerenz-protokoll-kap40-und-kap0-fassung-2026-05-08-md`.

### Previous document — Alter profiles

**The seventeenth document is done: `kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md`, 2026-09-25.** 336 candidates under decision 012's list rule, no pages, readings on 38 pages, six conflicts and four questions moved, J85–J86, one sweep hit (a reading). `Wiki/compare/reconcile-18-kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md.md` has the record. It is the file document 16 pointed to for the Alex conflict and the roster.

- **C11**: heat three ways in one document — Juna's trace, Silas' warmth under the same lock, and Landauer heat from the Silas–Oblivion conflict. None is related to the others.
- **C6/Q5**: two Guardians; Cerberus, LogOS and Kairos absorbed in the Erasure-Pol; no Sophia.
- **The roster**: thirteen named, fifteen names excluded by name (L95), `Limina` among them.

Next, by the open records: `kp-plot-konkretisierung-13-ideen-f1-faden-2026-06-10-md` for C11 and C12 (291 lines; 8 lines with `Ozon`, 8 with `734`, `grep -c`, orientation only). Of the four files the drafting manual calls a quartet, all four are now read.

**A second reading of it, the same day** (pull request #88), found two conflicts
this reading's pages held and no record did — **C14**, whether AEGIS gets a
first-person chapter, and **C15**, who carries Flight — and gave C11 the character
bible's entry. Its list is kept as `03-candidates-blind-1.md`: F1 0.52 against
the committed one, which it holds 92 % of.

### Previous document — drafting manual

**The sixteenth document is done: `kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md`, 2026-09-25.** 542 candidates, no pages, readings on 53 pages, eight conflicts and five questions moved, J80–J84. `Wiki/compare/reconcile-17-kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md.md` has the record. Chosen for C11; it gave C11 a tension inside one document rather than a new side.

- **C11**: cold ozone locked as the Landauer-Signatur, and a foreshadowing strand `Landauer` themed as heat in Kap 6 — J81 keeps strand and signature apart.
- **C6/Q5**: two Guardians, and the 2025 Guardian–world pairing named and retired. The author's five stand.
- **C10**: Kap 0 alone, dated to the Kompendium. **C12**: four beats restated with no 734 beat, and the document's own Alex conflict (above).
- **KW3** has chapters here (Kap 23–28); the strukturierter Outline's gap is its own.
- **C13** surfaced while comparing this reading with five earlier readings of
  Köln 2026; its positions remain open for the author.
- **The pair ledger grew by four labelled rows**: J81 is a two-terms pair both rules get right; J82–J84 are one-term pairs neither sees — a leading numeral (`Zwei Guardians`, `13 Alter`) and a short form decided by content (`Polaritätsregel`). All three are rules a program could state.

Next, by the open records: `kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md` (1129 lines), the quartet's third file — this document sends its reader there for the Alex conflict (its §11) and for the exact roster of the 13 Alters (Q3). For C11 and C12, `kp-plot-konkretisierung-13-ideen-f1-faden-2026-06-10-md` (291 lines; 8 lines with `Ozon`, 8 with `734`, `grep -c`, orientation only).

### Previous document — Genesis iteration

**The fifteenth document is done: `koharenz-protokoll-konzept-iteration-genesis-md`, 2026-09-25.** Its 58 selected candidates yielded one new layer page (`k0-existenz`), a `K1-Reinform` alias on `nichts-rauschen`, readings on 22 pages, and new evidence on C7, C8, C11 and C12. `Wiki/compare/reconcile-16-koharenz-protokoll-konzept-iteration-genesis-md.md` records the work.

Its explicit four-beat event sequence puts Komponente 734 before the separation; its chapter 21–22 flashbacks recall the separation before 734, a different narrative order that the source itself calls a proposal. C12 remains open. The source never writes `Ursprungs-Ich`: its division of subjective Kael and functional AEGIS refines the J68/J75 question but cannot settle the incompatible glosses. A strong next source is `kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md` for C11; choose by the remaining conflicts rather than date.

### Previous document — structured outline

**The fourteenth is done: `koharenz-protokoll-strukturierter-outline-2026-05-18-md`, 2026-09-24.** 576 candidates,
no pages (an outline places; it defines little it does not also name as known),
readings on 43 pages, ten conflicts and four questions moved, J69–J75.
`Wiki/compare/reconcile-15-koharenz-protokoll-strukturierter-outline-2026-05-18-md.md` has the record. Chosen because it
spoke to more open records than any other unread canon-era document.

- **C10 gains a third position**: the knuckles are a standing trait of the Host,
  in no chapter.
- **Q5**: Sophia is placed, latent in KW4; LogOS and Kairos are absorbed two ways
  in one document.
- **C12**: both Genesis orders and a fourth beat, two weeks before the
  Kapitel-Kompendium has the same.
- **J75**: the Ursprungs-Ich glossed as AEGIS — a third answer to J68.
- Reading it found **the quotation check blind to chapter numbers**; fixed, with
  three self-test cases that fail on the old code.
- **The tools installed on 2026-09-24 read it too**, as second readers after the
  candidate list was committed — see *The new tools as second readers* below.

At that point it left 25 canon-era rows landed and unread. By the open records, the
strongest next candidates are `koharenz-protokoll-konzept-iteration-genesis-md`
(C12 and J75: 79 lines on the Genesis) and
`kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md` (C11: 14 lines with
Ozon, the most of any unread document) — a grep over the unread canon era,
orientation only.

**The thirteenth is done: `kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md`, 2026-09-24.** 326 candidates, 7 new
pages (the physics, and `hitze-polaritaetsregel` and `genesis` for C11 and C12),
readings on 43 pages, twelve conflicts and three questions moved, J68. It ranks
itself below the storyform document; recorded, not applied.
`Wiki/compare/reconcile-14-kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md` has the record.

**The twelfth is done: `dramatica-dual-storyform-status-2026-05-07-md`, 2026-09-24.** 206 candidates, no pages,
readings on 16 pages. **C8 is explained**: this is the lock-in that mirrored the
Approach, and the character bible's Be-er is its „vorher". C2, C11, C12 and Q1 also
moved. `Wiki/compare/reconcile-13-dramatica-dual-storyform-status-2026-05-07-md.md` has the record.

**The eleventh is done: `kohaerenz-protokoll-kernwelten-vollstaendig-2026-06-10-md`, 2026-09-24.** 294 candidates, 7 new
pages (places with a canonical chapter anchor), readings on 42 pages, eight
conflicts and four questions moved, J64–J67.
`Wiki/compare/reconcile-12-kohaerenz-protokoll-kernwelten-vollstaendig-2026-06-10-md.md` has the record.

- **C7 may not be a conflict**: Kap 33's garden is Juna's effect, Kap 38 her
  appearance. Put to the author.
- **Two facilities joined by rule** (J64, J65): Therapie-Schnittstelle Gamma is
  the page's Alpha, Datenverarbeitungsknoten Epsilon the page's 7G.
- **Mosaik-Herz** is a Kap-11 beat and a Kap-34 place — a new question.

**The tenth is done: `kapitel-kompendium-gather-2026-05-31-md`, 2026-09-24.** 277 candidates, no new pages
(a gather places, it does not define), readings on 28 pages, ten conflicts and two
questions moved, J63. `Wiki/compare/reconcile-11-kapitel-kompendium-gather-2026-05-31-md.md` has the record.

- **It names its own filter**: „Michael→Kael · Julia→Juna · 20 Kernwelten / 5
  Guardians → 4 KW, 2 Guardians" (L13). Two renames the wiki had inferred from
  dates are now stated.
- **C7's record was wrong** to call this document not in `Sources/`; corrected
  there. It does not settle C7 — it places no direct appearance for Juna.
- **C11** — its first Riss is „Landauer-Hitze/Ozon", and its date is the day after
  the 2026-05-30 cold-ozone lock. Document 7's line for the same Riss is this
  sentence with `Hitze` replaced.
- **C12** — it holds both orders of the Genesis and counts a fourth beat.
- **KW3 is also „Überwelt-Nexus"** (L165) while the Überwelt is outside the worlds
  (L170) — a tension inside one document, recorded on the pages (J63).
- **Every open record was read against it** (the new ingest step): five were
  unchanged and are listed in `reconcile.json`.

**The ninth is done: `koharenz-protokoll-konzept-konsolidiert-2026-05-08-md`, 2026-09-24.** 446 candidates, 2 new pages
(`erason`, `persistenzgleichung`), readings on 45 pages, two new conflicts (C11,
C12), and C5–C10 and Q5 moved. `Wiki/compare/reconcile-10-koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md` has the record.

What it found:

- **The two 2026-05-08 documents disagree with each other** — on C7 and C8 this
  one sides with document 7, and on C12 with neither. No date can order them.
- **C11 is a conflict document 7 had already recorded** against „an outline of
  2026-05-08", quoted in this document's exact words. The wiki now holds both
  sides.
- **C5 got the source the list below asked for**: `Garten der Möglichkeiten` names
  KW4 and `Möglichkeits-Garten` is a place inside it, in one document (L517,
  L530). One source at two scales is a reading, so J35 holds (J61).
- **Q5** — a third absorption: LogOS, Cerberus and Kairos into the Erasure-Pol.
  Sophia is placed nowhere.
- It claims to be „autoritative Spec" (L1395). Recorded, not applied.

What it leaves: 26 canon-era rows landed and unread (after document 13). Its own open table
(OQ-A … OQ-G, L1198–L1218) names what a later document would have to settle —
the name of the plural AEGIS, Juna's modes, the mirror Alters' chapters.

**The eighth is done: `kohaerenz-protokoll-charakter-bibel-2026-05-08-md`, 2026-09-24.** 302 candidates,
16 new pages (the twelve Alters, `moonshine-link`, `telefon-stille`,
`algorithmische-melancholie`, `cache-kohaerenz`), readings on 22 pages, and four
new conflicts. `Wiki/compare/reconcile-09-kohaerenz-protokoll-charakter-bibel-2026-05-08-md.md` has the record.

**Discussion items it raises** — each a place where the two canon-era documents
disagree. **Decision 006 (the author, 2026-09-24): every draft is back in
question and must be discussed; `Sources/` is the new baseline.** So no date and
no source's claim to be canon settles any of these; each is discussed with the
author and closes when the author decides it:

- **C6** — **decided by the author, 2026-09-24: five Guardians** (LogOS,
  Mnemosyne, Cerberus, Kairos, Sophia). Their pairing with the Kern-Welten and
  the Erasure-Pol are open in **Q5**.
- **C7** — Juna's direct appearance: once, ca. Kap 33 (Charakter-Bibel), or
  first in Kap 38 (storyform-und-outline)?
- **C8** — AEGIS' Approach in Storyform B: Be-er or Do-er?
- **C9** — **decided by the author, 2026-09-24: the Konstrukt-Stadt is KW1**
  (a first answer, recorded as „the whole simulation", was corrected the same day).
- **C10** — do Kael's knuckles bleed in Kap 1?

What it leaves for the next document: the consolidated concept
(`koharenz-protokoll-konzept-konsolidiert-2026-05-08-md`, landed, unread) is the
same date as the character bible and is named by document 7 as a source; it may
speak to C7–C10.

**The seventh is done: `kohaerenz-protokoll-storyform-und-outline-2026-06-10-md`, 2026-09-24**, the first canon-era document and the
one the author's goal names as normative. 388 candidates, 4 new pages
(`coheron`, `nichts-rauschen`, `trennungsprotokoll`, `landauer-signatur`), readings
on 17 pages, conflict **C6** (two Guardians against five, and „KEIN
Guardian-1:1"), and Q1, Q3, Q4 and C5 moved. `Wiki/compare/reconcile-08-kohaerenz-protokoll-storyform-und-outline-2026-06-10-md.md`
has the record, including the rule that kept 271 new terms from becoming pages.

What it leaves for the next document:

- **C6** wants a canon-era source relating the two Guardian arrangements. The
  character bible (`kohaerenz-protokoll-charakter-bibel-2026-05-08-md`) and the
  consolidated concept (`koharenz-protokoll-konzept-konsolidiert-2026-05-08-md`)
  are landed and unread; the document names the concept as one of its sources.
- **The 12 Alters** beside Kael have no pages, by the document's own statement
  that its figures are „outline-relevante Kurzanker". The character bible is
  where they would get readings.
- **This document ranks its sources and resolves three conflicts among them
  (§7)**, none of which the wiki can see yet: the sources it resolves between
  are the Kapitel-Kompendium and the 2026-05-30 decision logs, which are not in
  `Sources/` (the logs are claude.ai exports, `GOAL.md` Anhang C1).

**Found while reconciling it, not caused by it:** `link.py` proposes 33 links on
pages this document did not touch — pending on the branch before it was read.
They were left alone so this document's commits change only what it caused; a
link pass over them is a separate commit.

The sixth is done. It was chosen because `kern-welten` asked for `KW2` or `KW4`
and Q4 asked for `Wächter` in an analytic sentence, and it supplied both.

What the wiki now asks for, in its own words:

- **Q1** still wants a document that states the Guardian/AEGIS relation outside a
  question. Two documents now support *components* and neither says it.
- **C5** wants a source that places a garden inside a named Kern-Welt, or that
  uses both `Möglichkeits-Garten` and `Garten der Möglichkeiten`.
- **Q3** wants the alter count. Document 6 bounded the world count and left this
  exactly where it was, because every level names its Alter with „wie".
- **`nexus`** wants anything relating `Nexus`, `Überraum` and `Nexus-Interface`.
  Document 6's table says the third name came from `Plot Teil 1`, which points at
  a plot document. Now **Q6**, with the Überwelt (2026-09-29).

**`Wächter` and `Guardian` do meet, and the corpus says so.** Two read documents
use them in complementary distribution, and that held for those two only. Across
the corpus 44 documents contain both, and
`umfassendes-lokalitaeten-konzept-fuer-roman` L31 writes „den entsprechenden
Wächter (Guardian) von AEGIS". That is the document that line was waiting for:
it states the equation rather than leaving it to be inferred. It has not been
read. Whether the two are one term is still `judgements.jsonl`'s question.

## Postponed, and safe to postpone because the record proves it

**`orte-konzept-fuer-kohaerenz-protokoll` was reconciled twice and both are
stale.** Each recorded `state_before: 46`; the chain now ends at 56, so both must
be redone against the current wiki. The work is not lost — the censuses, notes
and candidate lists in the two worktree branches stand, and only the
reconciliation depends on the state that moved.

Nothing has to remember this: `Plan/runs/<slug>/reconcile.json` holds
`state_before` → `state_after` for every document and `account.py order` compares
them. **Done is a measurement here, not a tick**, which is what makes postponing
a task safe rather than a promise.

That case is also what `Plan/concept/task-queue_2026-09-17.md` is for. Merging
document 6 invalidated those two reconciliations, left ten pages unlinked and
moved the `fold()` baseline from 65% to 58% — three consequences of one
intended change, none of them written down by anyone. The concept's whole
premise is that a task is derived from measured state, so it cannot be forgotten
and cannot go stale in a list.

## Known failing

**`account.py order` holds again.** It was red from the 2026-09-25 scan, whose eleven
pages were written outside a reconciliation, until document 21 started from the 105
pages they left and recorded 106.

**The qmd coverage check reads collection patterns.** The previous version
treated a collection rooted at `.` as covering all descendants, even when its
pattern excluded them. It now checks `.qmd/index.yml`'s path and glob for each
collection, with an offline test that exposes this exact defect. Tool and agent
instructions under `scripts/`, `.agents/skills/` and `.claude/skills/` are
explicit exclusions: qmd searches the novel corpus and process records, while
those files are read directly when working on code. The check needs no qmd
binary; it checks configured coverage, not the contents of an installed index.

**Citation resolution is complete:** 0 <!--state:quotes.unresolved-->
quotations fail `scripts/quotes.py`, and 0 <!--state:quotes.unchecked-->
research-source quotations lack a resolvable citation. The checker audits
research-source wording; an author's recorded decision links to its decision
record and is not treated as a quotation from a research document.

## Landed

**The rest of the manifest, 2026-09-26, on the author's „Download all of the Rest
from the Manifest".** `sources.py fetch --include-md --limit 1000` landed the 241
remaining routable rows in about four minutes, none failing, no model reading any:
227 pre-May-2026 `plot-outline` gdocs, 13 `md`, one `pdf`. `dedupe.py --apply`
folded 26 copies among them (20 groups, `Plan/runs/dedupe.json`), so 215 new
documents stand, and `duplicates.py` reports 0 near-copies again. `dedupe.py` now
never folds a document something cites. It also appends its decision instead of
writing over the last one, which is how the first run's 31 groups were lost.
`qmd update` indexed the new files; embeddings were not built.
**`Sources/README.md` now ends with every document and its most important names**,
written by `scripts/overview.py` after a qmd first scan (*Sources at a glance* in
`CLAUDE.md`). **None of the 215 is read.** The plot outlines were deferred with
the novel, and landing them decides nothing about reading them.

**The canon-era documents, 2026-09-24, on the author's yes.** `sources.py fetch
--since 2026-05-01 --include-md` landed the 29 remaining rows dated May 2026 or
later, none failing. 26 were `md`, which `fetch` skipped before: the two new flags
are opt-in, and `md` takes the same text route that landed the four `md` rows on
2026-09-16. `dedupe.py --apply` then folded four copies — three `-2` exports two
bytes apart, and `25-wegkreuzung-md`, the chapter-25 text of `kp-kap25-2026-09-14-md`
in another escaping — so 37 canon-era rows became 33, all landed. **Eighteen are read**, documents 7 to 24; the first eight were
`kohaerenz-protokoll-storyform-und-outline-2026-06-10-md`, `kohaerenz-protokoll-charakter-bibel-2026-05-08-md`,
`koharenz-protokoll-konzept-konsolidiert-2026-05-08-md`, `kapitel-kompendium-gather-2026-05-31-md`, `kohaerenz-protokoll-kernwelten-vollstaendig-2026-06-10-md`, `dramatica-dual-storyform-status-2026-05-07-md`,
`kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md` and `koharenz-protokoll-strukturierter-outline-2026-05-18-md`, as documents 7 to 14 — see *Next document* for the rest.
(This line said „Five are read" over a list of seven until 2026-09-24.) The copy under `Legacy/Canon/` (six of the 2026-06-10
documents) has not been compared against the landed files.

Pull request netzkontrast/kohaerenzprotokoll#52 merged on 2026-09-23: the TypeSafe
SDK and project skill (`.agents/skills/typesafe`), the Jev concept, the vendored
`jev*` skills, `scripts/entities.py`, the entity pilot and the saved workflow.
Nothing from it is in flight; what it left open is under the headings above.

## Not open

Drafting the novel, until the author has answered the plan's four questions (*Writing the
novel — a plan*, above). The `Legacy/` shelf. Reading the 215 plot outlines landed on
2026-09-26: they are on disk and searchable, and still deferred with the novel
as reading material. The one `mp3` is a question above, not a backlog.
