# Writing the novel — a plan

**2026-09-29 · a proposal.** A session wrote it on the author's request: „Think about how to Write
the novel and come up with a plan". **Nothing in it is decided.** Every phase ends at a
gate where the author decides. The first four questions are in §11, and `NOW.md` carries them.

**Revised the same day, on two messages from the author sent while it was being written.**
- „The novel in Legacy is Not the quality I want". This changes §2, question A and question B.
- „Install https://github.com/netzkontrast/writing-skills/tree/main into this repo", then „But
  optimieren ihn für dieses repo". The thirteen skills are installed and adapted
  (`.agents/skills/writing-skills/`), and they are now this plan's reading side (§6).
- „I dont Like that the novel does Not Flow Like a scifi novel - i want more Action - its a
  question of the Plot". This makes W2, the engine, the first question of round 1 (§5, *The
  author's plot verdict*).

The plan is in English, the working language. The novel, and everything read against it (the
treatment, the briefs, the rulebook), is German.

---

## The short version

1. **The wiki cannot write the book, by design.** It collects what the sources say and never
   decides between them (decision 006). A novel is a sequence of decisions. The project has no
   place yet where the author's decisions turn into story. More readings will not supply that place.
2. **The record shows two ways this goes wrong.** First, reading converges nothing: two of fifteen
   conflict records are decided, and the author decided both. Second, prose written on decisions
   the author delegated has not become the book. In September a session took thirty-six chapters,
   about 71,000 words, from outline to prose in two days on the instruction „entscheide selbst",
   and took 53 decisions itself. Four days later decision 001 parked the manuscript, and on
   2026-09-29 the author judged it: „The novel in Legacy is Not the quality I want".
3. **So: decide, then tell, then write, one chapter at a time.**
   - **Decide.** Sixteen load-bearing decisions, the *Weichen* W1–W16, go to the author in four
     rounds of four.
   - **Tell.** The story is written out plainly: one page, then one paragraph per movement. Each
     paragraph says what happens, what it costs and what it leaves. The author approves it act by act.
   - **Write.** Chapters are drafted in order. Each draft comes from a short brief derived from
     those decisions. Code checks every rule that code can check. The adapted writing skills
     read the draft line by line, against the book, and cold. None of them writes a word of
     it. It is revised until the author calls it v1.
4. **By hand first.** Kap 1–3 are the pilot. A step becomes a tool only if the pilot used it:
   `brief.py` and `prose_check.py`, each with a fixture it must fail.
5. **What this costs the author is attention, not tokens.** About sixteen decisions, four
   treatment approvals and one review per chapter. The plan keeps that number small and prepares
   every ask in full.

---

## 1. Where the book stands — measured 2026-09-29

| | |
|---|---|
| **Sources** | 586 <!--state:sources.landed--> of 587 <!--state:sources.total--> landed, 93 <!--state:documents.reconciled--> read and reconciled. **Reading is paused on the author's word of 2026-09-28**: „Dont start any new documents" (`NOW.md`). |
| **Wiki** | 106 <!--state:wiki.pages--> term pages, 16 <!--state:wiki.conflicts--> conflict records, 9 <!--state:wiki.questions--> question pages, and 41 <!--state:wiki.chapters--> chapter pages holding 972 <!--state:chapters.readings--> readings |
| **Where the sources part** | 156 bullets under `## Where the sources differ` on the chapter pages, and 8 on `Wiki/overview/plot.md` |
| **What they agree on** | Three parts of thirteen chapters: 1–13, 14–26, 27–39. Akt II's cycles Z1–Z3 fall in 15–17, 18–20 and 21–23, with the Genesis flashbacks in 18–22. Most 2026 plans add a frame, Kap 0 and Kap 40, and the endgame: 27–34, Vortex 1 in 35–36, a false victory in 37, Vortex 2 in 38–39 (`plot.md`, *Where the sources agree*). |
| **What is decided** | C6, the count only: five Guardians. C9: the Konstrukt-Stadt is KW1. Both were decided by the author on 2026-09-24, and C6's pairing is open in Q5. Decision 006 puts every earlier draft back in question. |
| **Prose** | **None the author has approved.** A complete draft is parked under `Legacy/`: 41 chapter files and 82,360 words of prose. Every file from Kap 1 to Kap 40 carries a draft note dated 2026-09-11 or 2026-09-12. The author's verdict, 2026-09-29: „The novel in Legacy is Not the quality I want". |

The commands behind every number are in the appendix.

---

## 2. What the record teaches

### Reading converges nothing

Every document read adds positions to the records. C11 (Landauer warmth or cold ozone) now
holds 41 sources, C7 (Juna's first appearance) 36, C14 (AEGIS' first-person chapter) 31 and
C12 (the Genesis beats) 30 — each record's `sources:` field. By decision 006 no source can
close a record. Only the author can, and the author has closed C6's count and C9. **This is the
wiki working as designed, not a defect.** It follows that reading the 535 unread documents is not
the road to the book: each would add positions, and none would take a decision. Reading keeps one
use, finding what a chapter lacks, and question D in §11 asks when it may.

### Prose on delegated decisions has not become the book

The Act I decision log of the September run opens:

> `[K]` = durch Autorauftrag „entscheide selbst" verbindlich geschlossen
> (`Legacy/Plan/drafting/decision-log_2026-09-11.md`, L3)

It holds 24 decisions, nine of them marked `[K]`. The Act II/III log holds 29 more, all `[V]`.

- The run's own audit of 2026-09-11 found prose in Kap 0, 1, 2, 3 and 5 only, and outlines
  everywhere else.
- The other thirty-six chapters, 70,738 words, now carry draft notes dated 2026-09-11 or
  2026-09-12.
- On 2026-09-16, four days after the last of those notes, decision 001 parked the manuscript,
  saying „its prose does not continue". Its stated reasons concern the repository's layers, not
  the prose.
- On 2026-09-24 decision 006 put every draft back in question.

The author has since judged the result: „The novel in Legacy is Not the quality I want"
(2026-09-29). So the lesson has two halves:

- **The decisions were delegated.** A session took them, and the author did not.
- **The result is not good enough.** The author says so of the novel itself, not only of how
  it was made.

Speed was not what was missing. What was missing was the author's hand on the story, and a
result the author accepts. The verdict does not say which part fell short: the story, the
sentences, or both. The pilot's reviews will show. This plan addresses the first half with the
Weichen and the treatment. It addresses the second in three ways:

- whoever writes, the author's hand is on every chapter (question A);
- the adapted writing skills read every draft (§6);
- **the parked prose is never a voice reference.** The September drafting brief named its own
  Kap 1 as „Stimm-Referenz für Kael". Here the voice reference is whatever the author approves
  in the pilot.

**The book also keeps being begun.** Kap 1 exists in at least five prose beginnings, each
confirmed by reading its opening:

- 2025-04-19, third person, with Juna on a wall screen: `romanentwurf-kapitel-1-ausformulierung`
- 2025-04-27, a run that stops at Kapitel 23: `kohaerenz-protokoll`
- 2026-02-22, third person, „Der Kristalline Käfig": `kapitel-eins-1-kohaerenz-protokoll`
- 2026-07-31, first person, v0.5: `Legacy/Plan/drafting/sources/CH-01_Erwachen-Zyklus_Draft-v0_5.md`
- 2026-09-11, first person, v1.1, in the parked manuscript

Each restart began again at Kap 1.

### Meaning without events

The Plot-Konkretisierung (2026-06-10) says this of the canon-era outline itself. The outline is
„strukturell vollständig, aber ereignis-arm" ^[kp-plot-konkretisierung-13-ideen-f1-faden-2026-06-10-md.md:L13],
and:

> „Das Projekt besitzt Bedeutungs-Architektur im Überfluss und Handlungs-Substanz im Mangel."
> ^[kp-plot-konkretisierung-13-ideen-f1-faden-2026-06-10-md.md:L29]

The September audit (`Legacy/Plan/drafting/written-chapters-audit_2026-09-11.md`) was written
before most of its own draft existed. It names the same defects:

- „Outline-Summaries sind häufig schon Interpretation." (L107)
- „Nebenfiguren sind Funktionen." (L110)
- „Hooks sind oft Themen statt Ereignisse." (L112)
- „Kapitel 14–23 drohen Seminarfolge zu werden." (L114)

**Part of the concrete material that answers this exists only in the parked draft.** Doran is the
colleague whose consolidation in Kap 5 is the draft's first relational loss (its D-14 and D-23).
He stands in 19 of its 41 chapter files and in no source or wiki page. The same holds for
`A-0001`, the remainder of that consolidation, which the order can only book as its first
exception. Whether that material comes back is question B in §11.

---

## 3. The idea: decide, then tell, then write

```
Sources ──read──→ Wiki: readings, differences — never decides
                    │
          the author decides ──→ decisions, each written once
                    │
          Treatment: the story told, one paragraph per movement,
                    │  every sentence citing a decision or a reading, or marked new
                    ▼
          Brief per chapter — derived, never written freehand
                    │
          Draft (German) ──→ checks (code) ──→ the writing skills: line, copy, continuity
                    │                                      │
                    │                cold read: beta-reader-panel ──→ the author
                    ▼
          Chapter v1 — which itself decides everything it fixes
```

**What is new here is a place where the author's decisions become story.** Everything upstream
of it exists. The wiki stays what it is: research that never decides.

**Three kinds of decision, each taken where it costs least:**

| kind | how many | when | how |
|---|---|---|---|
| **Weichen**: load-bearing, changing many chapters or the ending | 16, W1–W16 (§5) | before the treatment | four rounds of at most four prepared questions (`GOAL.md` §1.9) |
| **Chapter decisions**: the 156 chapter-level differences, titles, C8, C10, C15 and the like | about one set per movement | when the chapter's treatment paragraph is approved | the session proposes a paragraph that names each choice it makes; the author approves it or changes it |
| **Scene decisions**: whatever the prose needs | many | in the draft | listed in the chapter's hand-off and approved with the chapter |

The 164 differences on the chapter pages and `plot.md`, and the 22 open records, become about
sixteen asks, four act approvals and one review per chapter. **No kind is ever taken for the
author.** Not by a session, which was the September route. Not by a source's claim to be canon,
and not by a date (decision 006).

**Story-First** (`GOAL.md` §1.5) settles where prose and plan disagree. On details, an approved
chapter wins over its treatment paragraph, and the paragraph is updated. A deviation that
crosses a Weiche is not adopted. It goes to the author.

---

## 4. The phases

Each phase has a deliverable and a gate (P22). No phase starts before the gate of the one before.

### Phase 0 — agree the way of working

- **Deliverable:** the author's answers to the four questions in §11: who writes the prose,
  what becomes of the September draft, where the book lives, and whether reading on demand is allowed.
- **Gate:** the answers, or „proceed as recommended".

### Phase 1 — the Weichen

- **Preparation, which needs no time from the author.** Each Weiche gets a decision sheet in
  German, one to two pages. The sheet holds:
  - the question;
  - the positions, quoted and cited from their records;
  - which chapters each choice changes, taken from the chapter pages' `records:` and their
    differences;
  - what each choice costs and gains, so no option is left bare (`GOAL.md` §1.9);
  - a recommendation, only where the material supports one;
  - a free-text way. The author often answers in four words that lie outside the offered set.

  Many sources report earlier locks of the author's, such as those of 2026-05-30. Where one does,
  the sheet says so, with the source that reports it. Decision 006 puts the lock back in question,
  but re-confirming an earlier decision is the cheapest decision there is. The author's own
  decision logs of 2026-05-30 are claude.ai exports in no catalogue. `GOAL.md` Anhang C1 already
  asks for them. As the author's own records they are the likeliest help for these sheets —
  likelier than any unread document.
- **Asking:** four rounds, most load-bearing first (§5).
- **Recording:** a decision is written once. It goes into the record it closes, dated, as C6
  and C9 were (decision 006). A Weiche with no record gets a file in the book's decision folder
  (question C).
- **Gate:** every Weiche is decided, or deliberately left open with the list of chapters that
  wait for it.

### Phase 2 — the story, told plainly: the treatment

- **2a. The whole book on one page**, Kap 0 to Kap 40, in events: who does what, and what it costs.
- **2b. One paragraph per movement.** Each paragraph names:
  - who;
  - what that figure wants and does, as a repeatable action;
  - with which object, and where;
  - what it costs, and what cannot be undone;
  - the hook-in and the hook-out, as events rather than themes;
  - in Akt I, the chapter's one concrete falsehood, if the rulebook keeps that rule.

  These are the Plot-Konkretisierung's six criteria (L29), extended by the September enrichment
  packet's hooks (`GOAL.md` §5.5). Every sentence cites the reading or the decision it stands on,
  with its line taken from `read.py --find`, or it is marked **new**.
- **2c. Three ledgers**, derived from the paragraphs:
  - **anchors**: planted, echoed, paid or closed. This is the September masterplan's motif
    ledger, which `GOAL.md` §5.5 carries;
  - **reader knowledge per act**: what the reader, Kael and AEGIS each know, wrongly believe and
    cannot yet know;
  - **the cast**: each figure with a want of its own. This answers the audit's „Nebenfiguren sind
    Funktionen". The cast is built with `character-card-builder`, which interviews the author
    one question at a time. It never invents a trait. When the author is stuck, it offers at
    most two cited positions from the sources to react against.
- **2d. The rulebook.** It holds the prose rules the author keeps, each with its chapter range
  and a mark saying whether code can check it. The rules come from the decisions and from the
  sources' own rule lists: `GOAL.md` §5.4 and the drafting brief's R-1 to R-10. Those lists count
  as proposals.
- **2e. The structures as diagnosis**, if W1 so decides. The treatment is laid against
  Dramatica A‖B, the heroine's and the hero's journey, the cycles and Kishōtenketsu. Every place
  where it departs from them is reported as a finding, not a fault.

**Pull, not push.** Before a movement's paragraph is proposed, the read documents naming that
chapter with no reading on its page (`chapters.py missing`, 129 <!--state:chapters.missing-->
mentions in all) are read onto its page. The backlog is worked chapter by chapter, only as the
treatment reaches each one.

**Who does it:** a session proposes, and the author approves or changes each act. A model
proposes and never decides.

**Gate:** a readiness check at the level of the book. Every movement has an event, a cost and a
hook-out. Every anchor planted is paid, or deliberately left open. The author has approved each act.

### Phase 3 — the pilot: Kap 1 to 3, by hand

**Why these three chapters:**

- The voice is set here.
- Kap 1 comes with a set of locks of 2026-05-30/31 that `GOAL.md` Anhang A lists line by
  line, and the three have few open records. Kap 1's records are C9 (decided), C10 and C11.
  Kap 2 has none, and Kap 3 has C7 and C11. So Kap 3 also tests whether the Weichen are enough.
- They hand off to each other, which tests the hook chain.
- Kap 1 already has five prose beginnings, so the pilot measures against something. The
  earlier versions are measured against and never copied from.

**For each chapter:**

1. a brief, written by hand (§6);
2. a draft, by the method question A chooses;
3. a check by hand, with every rule marked as decidable or as judgement;
4. `line-editor`, `copy-editor` and `continuity-editor` on the draft;
5. a cold read, `beta-reader-panel`, with one subagent per reader;
6. the author's review;
7. revision, until the author calls it v1.

Once Kap 1 stands, `agent-first-pages` reads the opening too. With a frame, it also reads Kap 0
once Kap 0 exists.

**Deliverables:**

- three chapters at v1, with their briefs, their check records and their cold-read reports;
- `Plan/learnings/write-chapter.md`, recording:
  - what the brief actually needed;
  - which rules code could have checked;
  - which of the writing skills' findings the author acted on, and which the author ignored;
  - how long each step took;
  - how much the author changed, and whether the method of question A held.

**Gate:** the author reads the three chapters and decides whether to continue, change the
method, or stop.

### Phase 4 — build what the pilot used, and nothing else (P3, P4)

| tool | `GOAL.md` name | its fixture (P5) |
|---|---|---|
| `scripts/brief.py <kap>` | `kp context` | §7.4: a fresh subagent given only the brief answers the readiness questions |
| `scripts/prose_check.py <file> --chapter N` | `kp check` | §7.5: a text carrying each violation (an alter's name in Kap 5, a DKT term in Kap 3, warmth in Kap 1, Juna as a subject, a labelled voice) fails, and a locked Kap-1 passage passes |
| a saved workflow that runs `beta-reader-panel` with one subagent per reader, if the pilot ran it more than by hand | — | a chapter whose reader-knowledge line it must contradict |
| `novel.*` measurements in `state.py` | — | the self-test every measurement has |
| a project skill, `write` | — | P6: it says „run this, read it this way" and restates no rule |

**The account's novel skills** (`novel-architect`, `chapter-briefing-architect`,
`chapter-draft-engine`) are ported as procedure, never as canon. The pilot uses their
procedures by hand: the thirteen-section briefing, the twelve-point adversarial check, gates
G1–G7 and R-1 to R-10. `GOAL.md` §5.5 asks for them to be integrated, not replaced, and porting
the procedures does that. Their canon predates decision 006, and `GOAL.md` Anhang B3, B4 and B7
show where it is stale.

### Phase 5 — drafting, one chapter at a time

**Order:**

1. Kap 4–13;
2. then 14–26;
3. then 27–39;
4. then **Kap 0 and Kap 40 together**, „ein einziger Atem in zwei Richtungen"
   ^[kap0-kap40-doppelklammer-abhandlung-2026-05-08-md.md:L25];
5. then Kap 1 once more, for the Ouroboros. Its first sentence is the last one Kael writes in Kap 39.

**Why this order:**

- The ending is decided in Phases 1 and 2, before any prose. That keeps the „retrograde"
  principle where it belongs: every echo is planted in the anchor ledger first.
- Drafting in reading order keeps the hooks and the reader's knowledge honest.
- The frame depends on everything else. The audit found the existing Kap 0 „philosophisch stark,
  aber erklärend".

**A window of one.** At most one chapter is drafted ahead of the author's review, and there is
never parallel drafting. The author may widen the window if the pilot shows that reviews change little.

**At each act's end:**

- the act is re-read;
- the treatment is updated where approved prose changed the story;
- the act is read cold as a whole (`beta-reader-panel`);
- `developmental-editor` gives its assessment of the act;
- `reverse-character-cards` sets the cast on the page beside the cast ledger.

### Phase 6 — revision

- **Whole-book passes:**
  - the anchor ledger: every plant paid;
  - reader knowledge: a cold read of the whole book;
  - continuity of names, numbers and sensorics: code, and `continuity-editor` in a full audit;
  - the frame and the Ouroboros;
  - `developmental-editor`'s full edit letter, and `copy-editor`'s full sweep with the book's
    style sheet.
- **Then the author reads the whole book** and decides about a second draft.

---

## 5. The Weichen — W1 to W16

A *Weiche* is a railway switch. Each of these sets the track for many chapters at once. The
chapter lists come from the chapter pages' `records:`. Where no record exists, they come from the
page or source named.

| | the question | records, sources | chapters it changes | round |
|---|---|---|---|:-:|
| **W1** | **What theory is for.** Are the architectures — Dramatica A‖B, the Murdock and Campbell stages, the cycles, Kishōtenketsu — the recipe the treatment is written from? Or are they the diagnosis laid on it afterwards? `GOAL.md` §1.5 says „Theorie ist Diagnose, nicht Rezept"; the chapter pages are full of storyform labels. | `GOAL.md` §1.5; Plot-Konkretisierung L13, L29; the audit | all | 1 |
| **W2** | **The engine.** Kael's job as the plot's motor: F1 „Der Sachbearbeiter der Abweichung", with the Gegenregister, the Fundsachen and the rest of its thirteen generators. Or another engine. | `kp-plot-konkretisierung-13-ideen-f1-faden-2026-06-10-md` (`[V]`); September D-15 adopted it for Act I | all | 1 |
| **W3** | **Voice.** Kael in the first person, present tense, as the Kap-1 lock „Das Licht ist schon da, als ich erwache." has it? Or the third person, past tense, of three earlier beginnings? And whose view besides Kael's? | Kap 1 page; the five beginnings (§2) | all | 1 |
| **W4** | **Shape.** 41 movements with a frame, or 39 chapters? One Vortex (35–36, then a resolution) or two (with Kap 37's false victory)? Where B turns to A follows as diagnosis. | `plot.md`, differences 1, 4 and 3 | 0, 35–40 | 1 |
| **W5** | **Heat and cold.** Is the Landauer trace warm or cold ozone? Is warmth Juna's alone? | C11, 41 sources | 0, 1, 3, 6, 8, 11, 12, 25, 36, 37, 38 | 2 |
| **W6** | **AEGIS on the page.** Logs and the third person only? Or one Hard-B chapter in Kap 5–8, in the first person or subjectless? | C14, 31 sources | 0, 5, 6, 7, 8, 14, 22, 25, 34 | 2 |
| **W7** | **The veil.** When may the reader learn what? When is plurality named, may a DKT word ever appear, when does AEGIS' name appear, and when Kael's? | `GOAL.md` B10; September D-05, D-12, D-21 | 1–13 and beyond | 2 |
| **W8** | **Where Act II happens.** KW2 and KW3 as places the book travels through (14–22, 23–28 in the canon-era plans)? Or regimes of one city, „Filterregime statt Ortswechsel"? And does Akt III open at 27 or at 29? | C9's follow-up; the Kap-25 log's OQ-25-F; `plot.md`, difference 5 | 14–28 | 2 |
| **W9** | **Juna.** Is her first direct appearance in Kap 38, with Kap 33 as her effect? Is she ever a subject or a body? Is she the Ursprungs-Ich, or what it met? | C7, 36 sources; J68 | 0, 3, 12, 22, 26, 33, 34, 38 | 3 |
| **W10** | **The cast.** Thirteen alters or eleven? Silas and Oblivion as mirror alters? Doran, who exists only in the September run's draft and record? Mira, named by one source only? | Q3; the parked draft | all | 3 |
| **W11** | **The Guardians on the page.** Five is decided. Are they figures in scenes or components of AEGIS? Which world is whose, and who or what is the Erasure-Pol? | C6 (decided count), Q5, Q1, C4 | 25, 29–32, 36 | 3 |
| **W12** | **The Genesis.** Three beats or four? Is Kael component 734 or its remainder? Where does AEGIS come from? | C12, 30 sources; C3; Q7 | 0, 18–22, 24, 39, 40 | 3 |
| **W13** | **AEGIS after the Vortex.** Oblivion taking over its function; the final form, and its name. | Q8 | 36–40 | 4 |
| **W14** | **Kap 40 and the outer level.** Both readings, reset and transfiguration; the last line, „Welt" or „Scherben"; Köln 2026 inside the simulation or beyond it. | C13; Kap 40 page | 0, 39, 40 | 4 |
| **W15** | **What crosses the Moonshine-Link.** What passes between Kael and Juna, and what does not: the mechanics of the love the book tests. | Q9 | every chapter that carries Juna's trace | 4 |
| **W16** | **Length.** Set after the pilot has measured it. In the September draft, Kap 1–40 ran from 943 to 2,376 words of prose and Kap 0 to 4,340; v0.5 of Kap 1 aimed at about 4,000 (its own header). | the pilot | all | 4 |

### The author's plot verdict, 2026-09-29

> „I dont Like that the novel does Not Flow Like a scifi novel - i want more Action - its a
> question of the Plot"

The verdict names the plot, not the sentences, and it points where the record already did.
The Plot-Konkretisierung calls the canon-era outline „ereignis-arm" (L13). The September
audit warns that Act II threatens to become a seminar and that hooks are themes rather than
events. So the order of round 1 changes, and so does what the treatment must prove.

- **W2, the engine, is asked first.** The question becomes what drives the plot as action: a
  goal Kael pursues against opposition, with stakes that rise and consequences that cannot be
  undone. F1, Kael's job as the motor, is one candidate. It is a bureaucratic engine, so the
  sheet asks whether it can carry pursuit and escalation, or whether another engine is needed.
- **W1 goes second.** Once the engine is chosen, theory serves the action, not the other way
  round.
- **Every treatment paragraph must show a physical event.** Someone does something, something
  resists, and something is lost or gained. A chapter that is only interior or only an idea is
  flagged at the gate unless the treatment declares it a deliberate pause.
- **The treatment gets one more ledger: the escalation line.** Per act, it records what Kael
  wants, who or what stands against him, what the stakes are and how they rise. It is checked
  the way hard SF is read: the world's rules have mechanisms and costs, and the plot turns on
  them.
- **The cold read tests the flow.** `beta-reader-panel`'s Genre Fan lens reads for the promises
  of SF: momentum, mechanism, consequence. Its put-it-down points are the pacing signal the
  verdict asks for.

**What is not a Weiche, and why.** Some records are decided per chapter at the treatment, or
drop away as diagnosis if W1 so decides:

- C8 (AEGIS' Approach) is a Dramatica slot.
- C10 (the knuckles) is decided at Kap 0 and Kap 1.
- C15 (the Flight riss) is decided at the chapters of its bearers.
- C1, C2, C4 and C5 are research questions. They need an answer only where a chapter uses them.
- Q2, Q4 and Q6 are the same.

---

## 6. How one chapter is made

**The brief** is German and at most two pages. It is derived, never written freehand, and after
Phase 4 `brief.py` writes it. It holds:

1. the approved treatment paragraph;
2. the hook-in: the last event of the previous chapter, quoted from its approved prose with its line;
3. the hook-out: the event the next chapter picks up;
4. the decisions in force, each Weiche that touches the chapter in one line;
5. the rules in scope, from the rulebook, each marked *code checks* or *judgement*;
6. the anchors due here: to plant, to echo or to pay;
7. reader knowledge at the chapter's start and end, for the reader, Kael and AEGIS;
8. the cast in the chapter, each with a want;
9. the world: the Kernwelt's sensorics, as the decisions have fixed them;
10. a voice sample of about 200 words from an approved chapter;
11. what is still open: the chapter decisions the draft must take and list.

The chapter page is linked from the brief, not copied into it. At 7,500 to 13,400 words, a
chapter page is research, not a brief.

**The draft** is written in German, in the voice W3 fixes, by whoever question A names. Each
chapter ends with a hand-off listing every decision the draft took. The hand-off is not part of
the prose.

**The check.** Code checks every rule it can decide (after Phase 4). Every other rule is named
as judgement and read by the author. A finding can be accepted as a deliberate riss, but only
with a line saying so (`GOAL.md` §1.6).

**The writing skills read it.** Three reads, each writing a file of findings under
`Plan/runs/writing/kap-NN/`, and none touching the chapter:

- **`line-editor`** looks for the draft's recurring sentence-level habits, flagged with the
  principle and a direction;
- **`copy-editor`** checks the mechanics by German rules, and holds the book's style sheet;
- **`continuity-editor`** reads the chapter against the book's facts as the author has decided
  them, never as the sources claim them.

Their shared rules are in `.agents/skills/writing-skills/SKILL.md`.

**The cold read** is `beta-reader-panel`. Each reader lens runs as its own subagent and is given
only the approved chapters up to this one: no wiki, no brief, no word of the author's hopes.
Each reports where it was confused, bored, gripped or lost. The synthesis is then compared with
the treatment's reader-knowledge line. A confusion the design intends is a hit. One it does not
intend, or a reveal nobody noticed, is the finding.

These reads are a measurement, never a decision (P18, P27). A model is only a proxy for a
reader. But it has read nothing except the text, and neither the author nor the session can
say that.

**The review.** The author reads the draft, the findings, the cold-read report and the hand-off.
The author approves the chapter, changes it, or sends it back.

**What is recorded:**

- the chapter at v1;
- the decisions the hand-off took, as the author approved them;
- the treatment paragraph, updated where the prose changed the story, with a note saying so;
- the time each step took, during the pilot.

**One revision, one commit.** The commit names the chapter and what caused the change: its
brief, a review, or a decision. This is the wiki's commit rule applied to the book (`CLAUDE.md`,
*Committing a wiki page*). With it, `git log` on a chapter shows where every change came from.

---

## 7. What already exists, and what each thing does while the book is written

| thing | while writing |
|---|---|
| **The wiki** | Stays the research layer. The records take the author's decisions. Reading resumes only on demand (question D). |
| **The chapter pages** | Research per chapter. A brief links to its page and never replaces it. |
| **The September draft** | Its ideas depend on question B. Its prose is not continued in place (decision 001), and it is never a voice reference („not the quality I want", 2026-09-29). |
| **The writing skills** | Thirteen editorial, critique, character and craft skills, adapted from `netzkontrast/writing-skills` at `2fad031`, with `writing-skills` as their entry point. They read, critique, simulate a reader or drill the writer, and never write the book (§6). |
| **The account's novel skills** | Their procedure is used, their canon is not (Phase 4). This matters now, not later. `chapter-draft-engine` triggers on „Kapitel X entwerfen", so a session asked to draft a chapter loads a canon that decision 006 put back in question. |
| **The 215 plot outlines of 2026-09-26** | Stay unread unless a chapter asks for one. |
| **qmd** | Finds candidates, and decides nothing. |
| **`read.py`, `quotes.py`** | Every citation in the treatment is asked for, never typed (P26). Extending `quotes.py` to the book's folder is a small change to its target list. |
| **`state.py`** | Measures the book once the book has instances (§10). |

**This plan also answers two open `NOW.md` items, as a proposal:**

- **„Chapter-level differences as conflict records?"** No. They are decided when the chapter's
  treatment paragraph is approved.
- **„Chapters in the graph and the app"** Not needed for writing.

---

## 8. What this plan deliberately does not do

- **No parallel drafting.** No chapter is drafted more than one ahead of the author's review.
- **No chapter drafted while a Weiche it touches is open.**
- **No decision taken for the author.** Not by a session, not by a source's claim, not by a date.
- **No new reports about the novel.** The corpus holds 586 <!--state:sources.landed-->
  documents, and the book has no chapter the author has approved.
- **No theory vocabulary in the prose** beyond what the rulebook allows.
- **No translation.** The prose is German, and so are the treatment, the briefs and the rulebook,
  because they are read against it.
- **No continuing the parked draft in place**, whatever question B decides.
- **No tool before the pilot has needed it.**

---

## 9. Risks, and what meets each

| risk | what meets it |
|---|---|
| The prose is not the quality the author wants — the September risk, now stated by the author | The author's hand is on every chapter (question A), the writing skills read every draft, the pilot compares two ways of writing, and no parked prose serves as a reference. |
| The author's attention is the bottleneck | Asks are batched, prepared in full and kept to about 16 + 4 + one per chapter. Nothing asks for a decision the record could answer. |
| A Weiche stays open | Only the chapters it touches wait. The treatment marks each paragraph's dependencies. |
| The voice drifts across chapters | Approved chapters are the reference, every brief carries a sample, and each act is read cold at its end. |
| The book restarts at Kap 1 once more | After the pilot, Kap 1 is not touched again until the Ouroboros pass. |
| Model prose has tics | The author's review catches them. Later a check can count repeated phrases across chapters; a count is decidable. |
| Theory creeps back into the prose | The rulebook holds the lines, and code checks the vocabulary list. |
| The wiki and the book drift apart | Each decision lives in one place. Briefs are derived from it, and `state.py` measures both. |
| The treatment swells into another report | It is one page plus one paragraph per movement, and every sentence cites a decision or a reading, or is marked new. |

---

## 10. How progress will be measured

Done is a measurement (P24). Once the book has instances, `state.py` gains counts over its
files. Nothing is stored, and nothing is ticked off by hand:

- Weichen decided;
- treatment paragraphs approved;
- chapters at v1;
- words at v1;
- checks failing;
- cold reads that contradict their chapter's line.

**None of these exists before its first instance (P4).**

**A prediction, to be checked against the pilot.** It is not a measurement:

- Phase 1 takes four sittings of the author's.
- Phase 2 takes five: the page, and one per act.
- Each chapter takes one drafting session and one review, so a first draft takes about eighty
  review sittings.

The pilot measures the real time per chapter. The estimate is revised from that, never before.

---

## 11. Four questions for the author — Phase 0

The author's instruction of 2026-09-24 stands: „Notiere in Zukunft einfach deine Fragen und setze
fort". These are noted in `NOW.md`. Preparing Phase 1 needs none of them, so the next session can
start there.

### A — Who writes the prose?

- **A1: a session drafts each chapter whole from its approved brief.** You review it, the
  session revises, and you approve v1.
  - *For:* the least of your time.
  - *Against:* the voice is a model's, shaped by your edits.
  - *In short:* the September method without what went wrong in it. One chapter at a time, on
    your decisions, reviewed before the next.
- **A2: scene by scene.** You approve each scene's beats, the session drafts the scene, and you
  edit it before the next one.
  - *For:* your hand is in every scene.
  - *Against:* it is slower.
  - *Best for:* the chapters that carry the book, Kap 0, 1 and 35–40.
- **A3: you write.** A session prepares the brief and runs the checks and the cold read.
  - *For:* the book is in your voice.
  - *Against:* it costs the most of your time.

*Recommendation, revised after your verdict on the parked draft:* **not A1.** A1 makes a model
the author of the prose, and the September draft is what that method produced; you have said it
is not the quality you want. Let the pilot compare the other two instead:

- **Kap 1 by A3.** You write, and the writing skills read and drill.
- **Kap 2 by A2.** The session drafts scene by scene on beats you approved, and you edit each
  scene before the next.
- **Kap 3 by whichever of the two you prefer** after Kap 1 and Kap 2.

The augmentation-only skills you asked for fit A3 exactly. Their rule is that the words on the
page stay the author's. The learnings file records what each method cost you and what each
produced. Or write your own way.

### B — The parked September draft

*Revising the draft in place is out.* It was option B3 here until your verdict of 2026-09-29, „The
novel in Legacy is Not the quality I want". Two options remain.

- **B1: bring its ideas back as research, not its prose.** Its premise and its drafting record
  land under `Sources/`: the drafting brief, the decision logs, act plans and arcs, beat cards,
  enrichment packets and the audit. They get a category of their own and a landing path from the
  repository, since they are not Drive documents (`GOAL.md` Anhang C1). The 41 chapter files
  stay parked, and so does the Kap-1 draft v0.5 beside the record.
  - *For:* Doran, `A-0001` and the handwritten Gegenregister live in that record, not only in
    the prose. Doran stands in 11 of the record's files in `Legacy/Plan/drafting/`. So the ideas become options a treatment
    paragraph can cite, without the prose you rejected. Decision 001 named this exit for the
    parked `Canon/`, and it fits here too: „it comes back as sources rather than as a layer".
  - *Against:* a landing path has to be built, and more positions enter the records.
- **B2: leave all of it parked.** The treatment starts from the wiki alone.
  - *For:* nothing from a delegated run comes back.
  - *Against:* its inventions return only if they are invented again.

*Recommendation:* **B1, as narrowed here.** No part of the parked prose is ever a voice
reference, whichever you choose.

### C — Where the book lives

- **C1: a new top-level `Novel/`.** It holds the book's decisions (one file per Weiche, like
  `Plan/decisions/`), `treatment.md`, `rules.md`, and per chapter a brief and the prose.
  - *For:* the book is not derived from the sources, so it is not a third copy of anything (P20),
    and the wiki stays research.
  - *Against:* a third top-level layer, which P20 asks to earn itself. The first decided Weiche
    would be its first instance.
- **C2: inside `Wiki/`.**
  - *For:* one tree.
  - *Against:* the wiki's rule is „never decide", and this folder would do nothing but decide.
- **C3: a repository of its own for the manuscript.**
  - *For:* clean separation.
  - *Against:* decisions and research drift apart across two repositories.

*Recommendation:* **C1, created with its first instance and not before (P4).** The name is yours.

### D — Reading on demand

Since 2026-09-28 no new document is started. The plan asks for one kind of exception. A
treatment paragraph or a brief may need something no read source holds, and qmd may find an
unread document that could hold it. In that case a session would read that one document in
full, by `ingest`.

- **D1: allowed for the chapter in hand**, and named in its hand-off.
- **D2: each such document needs your yes.**
- **D3: no reading until the first draft is done.** Gaps are filled by decisions instead.

*Recommendation:* **D2.** It keeps your word of 2026-09-28 intact, and the pilot shows how
often a chapter really needs a new source. If that is often, D1.

---

## 12. The next session

**Preparation completed, 2026-09-30:** W1, W3 and W4 now stand beside W2 in
`Plan/weichen/`. `treatment-probe_2026-09-30.md` provides a conditional causal
story and opening movements on their recommendations. It is a proposal, not
Phase 2's approved treatment; no Weiche has been decided by writing it.

**Further preparation, 2026-09-30:** W5–W10 now have decision sheets, with an
explicit response to merged PR #113 in `antwort-pr113_2026-09-30.md`. They remain
open; the plot research's provisional values are not author decisions.

| sheet | question |
|---|---|
| [W5](../weichen/w5-sensorik.md) | heat, cold, physical costs and sensory signals |
| [W6](../weichen/w6-aegis-perspektive.md) | AEGIS perspective versus B's structural role |
| [W7](../weichen/w7-schleier.md) | separate knowledge thresholds and enacted Ich/Wir transition |
| [W8](../weichen/w8-akt-ii-raeume.md) | spaces, forced transitions and Act-III trigger |
| [W9](../weichen/w9-juna.md) | presence, identity and the cost of connection |
| [W10](../weichen/w10-besetzung.md) | roster, individual goals and reactive opposition |
| [WP](../weichen/wp-plot-story-points.md) | concrete goals and conditions, then optional Type/signpost diagnosis (PR #115) |

PR #115 also supplies two [provisional NCP transcriptions](../runs/plot-2026-09-30/ncp/README.md).
They encode one source position, remain candidates and are unchanged by these
decision sheets. Structural POV is not prose POV; schema validity is not
theoretical or manuscript alignment. WP's Start/Stop and Crucial-Element
questions remain unverified. WP joins the next author review; its answers must
not be inferred from the proposed Type tables.

Unless the author says otherwise, the next session:

1. puts the prepared W1–W10 to the author, with the four questions of §11 if still open;
2. records each answer where it belongs, dated, and revises the conditional probe with
   observable goals, necessary steps, consequences and the two clocks;
3. prepares W11–W16 as needed, using already read material and `read.py --find` for
   citations; starts no new document without a changed author instruction.

The writing skills need nothing further before the pilot. One smoke test of the most-changed
of them, `copy-editor`, ran on the parked Kap 1 when they were installed. It tested the
adaptation, not the book; `NOW.md` has what it found.

---

## Appendix — the measurements, and how to repeat them

```bash
python3 scripts/state.py                  # sources, wiki, chapters, readings, missing mentions
# chapter-level differences: 156
for f in Wiki/chapters/kap-*.md; do awk '/^## Where the sources differ/{p=1;next} /^## /{p=0} p && /^- /' "$f"; done | wc -l
# plot-level differences: 8
awk '/^## Where the sources differ/{p=1;next} /^## /{p=0} p && /^- /' Wiki/overview/plot.md | wc -l
# which chapters each record touches
grep -H '^records:' Wiki/chapters/kap-*.md
# sources per record
grep -H '^sources:' Wiki/conflicts/*.md

M="Legacy/Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/chapters"
grep -o 'Draft v[0-9.]* ([0-9-]*)' "$M"/[0-9]*.md          # the draft notes, dated 2026-09-11 / -12
grep -l Doran "$M"/[0-9]*.md | wc -l                        # 19 (18 as a whole word; one file has only „Dorans")
grep -rl 'Doran\|A-0001' Sources/ Wiki/ | wc -l             # 0
grep -c '^| D-' Legacy/Plan/drafting/decision-log_2026-09-11.md          # 24
grep -cE '^\| D[0-9]+-[0-9]+' Legacy/Plan/drafting/decision-log_akt2-3_2026-09-11.md   # 29
```

The prose count of the parked draft, 82,360 words, counts each chapter file from its prose
heading onward: `# Kapitel N` for Kap 1–40, and `# Kohärenz Protokoll — Kapitel 0` for Kap 0.
The thirty-six chapters the audit of 2026-09-11 found in outline hold 70,738 of those words:
Kap 4 and Kap 6–40, the audit's own L3 ('Kapitel 4 und 6–40 als Outline-Dateien').
The five beginnings of Kap 1 were confirmed by reading their first paragraphs, not by title.
