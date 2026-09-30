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

**Answered 2026-09-29 — the pipeline plan, „Alles ja" and „Bitte setze den Plan um"** (decision 015).
Built on PR netzkontrast/kohaerenzprotokoll#110: step 1 (`runlog.py`), step 2 (history to
`Plan/runs/reading-log.md`, install detail to the tools skill), step 3 (`read.py --count` and count marks,
`lint_readings.py`, derived frontmatter, `account.py order` without a census fails), step 4 (`digest.py`,
`readings.py`, `.claude/agents/wiki-reader.md`), the raw qmd answers beside their run, a leaner session
install. A quality sample of documents 32–51 found 11 defects in 119 claims, all corrected
(`Plan/runs/quality-sample-2026-09-29/`). The pilot of step 4 and step 6's sample are under *Handover*.

**The review of #110, 2026-09-30, and what it changed.** It asked for changes after the merge. Five
findings, each reproduced before it was fixed on the branch that follows #110:
- `account.py order` exited 0 while it printed `"holds": false`. It exits 1 now, and names a census
  without a note and a note without a census.
- `CLAUDE.md` said `true` and 51/51/51 over a red state, with `state.py --prose` failing. The numbers
  are true again.
- `readings.py` took a quotation without a citation, a link to no page, a wrong date and a heading
  naming another document. It only recommended the checks afterwards. Now it refuses all four, and
  writes only what its checks passed.
- The pilot's table said 0 unchecked quotations. There were 11, and it met two of its four bars.
- `yield.py` counted no tokens and no corrections.

Every check now runs on GitHub, one step each (`.github/workflows/checks.yml`), on every pull request
and every push to `main`. What stays open is step 6 itself, its costs and quality measured.

**A second review, of #120 at `f690eba`, found four gaps in the new write gates.** Each was
reproduced and then fixed with a regression case that fails on the old code:
- the clean reader's apply gate passed an empty note and would have copied it over an existing one
  (`a879787`);
- `readings.py` took a plural `## Readings —` heading, which no frontmatter counts (`9c20125`);
- `census.py check` compared only the counts, not the lines and surfaces columns, and `census.py
  draft` wrote its candidates' „…“ as uncited quotations (`4f3c11a`).

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

**PR #115 incorporated, 2026-09-30:** `Plan/weichen/wp-plot-story-points.md` now
connects plot goals and conditions to W5–W10. It distinguishes Kael's observable
objective from AEGIS' consolidation goal and records the limits of term-count
evidence, Start/Stop and Crucial-Element hypotheses. WP is the decision sheet;
the PR #113 response's plot questions remain its scene-level reading test.
The two `Plan/runs/plot-2026-09-30/ncp/*.provisional.ncp.json` files are imported
unchanged, as candidate transcriptions of one source table. No approved encoded
fact changed. JSON and unchanged-content checks were run; the upstream schema
validator is absent here, so PR #115's reported PASS was not rerun. Next review
includes WP; four NCP Signposts do not silently redefine the novel's three acts.

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

**The pipeline plan of 2026-09-29 is built through step 5** (decision 015; the plan's last section
lists what exists). The next session starts on **step 6, the sample**: the two newest unread documents in
each of the six categories with one read document or none, read with the new readings step
(`wiki-reader` files, `readings.py apply`, `runlog.py` from the first phase):

- audit: `technical-audit-research-mandate-the-kohaerenz-pro…`, `kohaerenz-protokoll-audit-und-verifizierung`
- theorie-logik: `ki-narrative-kollaps-kohaerenz-paradoxie`, `kohaerenz-protokoll-meta-foreshadowing-beobachter-…`
- theorie-psychologie: `angst-bei-komplexen-traumafolgen`, `flow-zustaende-und-dissoziative-identitaet`
- theorie-philosophie: `ontologische-inversion-von-aegis-kritisches-framew…`, `textanalyse-existenz-system-und-leid`
- theorie-genre: `kohaerenz-protokoll-hard-sf-horror-thriller`, `hard-sci-fi-cosmic-horror-research-questions`
- aegis: `ki-assistent-romanwelt-kohaerenz-und-aegis-spec`, `aegis-persona-and-manifest-generation`

Slugs are cut here; `python3 scripts/sources.py status` and the manifest have them whole. **Claim before
reading**: an open pull request whose title or body names the slug under a `Claim` heading, checked for in the
open pull requests first — two sessions following one handover read documents 16, 17 and 20 twice.
**Claimed 2026-09-29 by netzkontrast/kohaerenzprotokoll#110, all twelve; the claim passes to the pull
request that follows it.** #110 was merged on 2026-09-30 with two of the twelve extracted,
`ontologische-inversion-von-aegis-kritisches-framework` and `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik`.
The other ten readers ran in parallel and were stopped by the session's usage limit. Their candidate
lists and counts are complete and gold (`gold.py`). Whatever they had written of a census or note is
in `Plan/runs/<slug>/partial-2026-09-29/`, moved out of `Sources/` so that no tool counts a fragment
as a census.

The author, 2026-09-30: „starte diese nicht parallel … beobachte jeden der zehn … versuche diese als
lernlabor zu verstehen … gib ihnen unterschiedliche Anweisungen … versuche auch die letzten paar prs
zu verstehen und passe und erweitere die Pipeline entsprechend an". So the ten are read one at a time,
each under its own instruction, and each run is recorded in `Plan/runs/reader-lab-2026-09-30/`.
What the first twelve readers cost is measured there from their transcripts.

**Each document is reconciled as it lands**, not all twelve after the last extraction. So
`account.py order`, which CI runs, is red only between an extraction and its reconciliation.

**Step 6 is paused by the author, 2026-09-30:** „stop Reading document - you should Improve the
Pipeline". Nothing reads a document until the author says so.
- The readings reader for documents 52 and 53 was stopped before it wrote a file. Their lookups and
  the readings brief stay in `Plan/runs/step6-readings-52-53/`, and document 54's in
  `Plan/runs/step6-readings-54/`.
- Three documents had a census and a note and no reconciliation: 52, 53, and the technical audit
  R1 extracted, so `pipeline order` was red and CI failed on `main`. On 2026-09-30 the author chose
  to reconcile them to fix CI: two `wiki-reader` runs from the two briefs, `readings.py apply`, and
  `Wiki/compare/reconcile-53` to `-55`. No page was added; C2, Q3 and Q8 gained entries. The order
  holds. The pause stands for every other document.
- The work now is the pipeline itself, measured offline on what is already read:
  - the reconciliation record drafted by code;
  - the readings brief drafted by code;
  - the census draft wired into the reader's definition.

**A parallel session builds `ask` (PR #119, decisions 016 and 017), and #120 carries it merged in.**
Two things from it change this lab:
- Its claude-cli backend, `claude -p` with no `CLAUDE.md`, no tools beyond those named and no
  thinking, is the lab's biggest lever. Tried on 2026-09-30, it was about 9 thousand tokens a
  call against a subagent's 67 thousand. `Plan/runs/reader-lab-2026-09-30/clean_reader.py` runs
  a reader that way, shut in its own directory; code checks its files and puts them in place.
- Decision 017 lets OpenRouter's free models and Jules answer `ask` packs as trials. Decision
  014 lets Jules ingest one document.

The comment on #119 asked that session for three things:
- a Jules extraction of `kohaerenz-protokoll-hard-sf-horror-thriller` as a comparison arm, written
  only under that document's `jules-2026-09-30/`;
- `askdb.py touches <slug>`, so each reconciliation record can name the Weichen its document
  bears on (one encoding, rather than a lens for readers);
- a pack, verify and render that take parameters, for an extraction pack.

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

**The tool review has run** (`Plan/concept/tool-review_2026-09-24.md`). The four
Hyper-Extract templates it could not run, because `he parse` cannot load a template
from a path, now load: `python3 scripts/templates.py parse` is `he parse` with that
one lookup extended, and `templates.py check` has a `resolve` check that fails when
it would not (2026-09-30). Measured offline against a local stand-in for the model,
all four parse, save, and answer `he search`; none has run on a document, which
waits on a model under decision 007. Its question 2 — patch the fork or copy the
templates into the installed package — needed neither. The three `route.py` defects it found are fixed, and what
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
   129 <!--state:sweep.decided--> hits, 67 <!--state:sweep.readings--> of them
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
  `scripts/gold.py` (decision 009) rules 59 <!--state:trainset.gold_candidate_lists-->
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

## PR #126 CI repair — 2026-09-30

The four Haiku lab extractions (R2–R5) are preserved under
`Plan/runs/reader-lab-2026-09-30/staged/Sources/{terms,notes}/`. They have not
been reconciled and are excluded from production ingest counts. Resume from
these staged artifacts when completing their reconciliation; no wiki reading
or reconciliation was fabricated to make the order check pass.

**Resumed the same day, one pair at a time.** A pair goes back to `Sources/{terms,notes}/` in the commit
that carries its reconciliation record, and not before. R4, `angst-bei-komplexen-traumafolgen`, is
reconciled (`Wiki/compare/reconcile-58-…`, no page and no reading, because no page speaks to a clinical
review) and back in `Sources/`; the order holds at 55 documents. R2, R3 and R5 stay staged until their
readings are applied.

## PR #126 review fixes — 2026-09-30

Claims now bind verdicts to the complete claim, citation and source passage;
redraft and re-review existing tables without binding markers before using the
claims gate. No historical verdict was automatically renewed. `record.py check`
refuses absent fields and malformed types; only historical `measure` enables
legacy compatibility explicitly. Cross-document reports separate group counts
from bounded examples. HyperExtract usage includes invalid paid replies and
retries; three existing summaries were corrected from their call ledgers.
Regression cases exercise all four review findings offline.
