Warning: truncated output (original token count: 35237)
Total output lines: 1638

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

**Next:** the author reviews round 1 and the probe. Record any answers once,
then prepare the remaining Weichen needed by the treatment. The separate
process questions A–D above remain open; preparing the probe decides none of them.

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
  Bewahrungsform (…21237 tokens truncated…/briefings/extract.md` now.

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
