# Design — Developmental Enrichment of Kohärenz Protokoll (all chapters)

> Status: `[V]` approved by author 2026-09-12. Engineering language English; all canon
> terms and all prose remain German. Normative on conflict, in order:
> `Canon/kohaerenz-protokoll_storyform-und-outline_2026-06-10.md` → the other Canon files →
> `Plan/drafting/decision-log*.md` → the act arcs → this document.

## 1. Problem

All 41 chapters carry prose (ch 0 `revised`, ch 1–40 `drafted`). Quality is high and the
architecture holds. The defect is **density collapse across the acts**:

| Block | Chapters | Prose words, avg | vs Act I |
|---|---:|---:|---:|
| Act I | 1–13 | 1,677 | — |
| Act II | 14–26 | 1,081 | −36 % |
| Act III | 27–40 | 1,054 | −37 % |

The climax block (33–39) averages **966 words** — the thinnest in the novel. Ch 34 resolves
the central epistemic collision in 912 words; ch 38 carries Juna's only direct appearance
and the Ouroboros decision in 986.

**Root cause, established from the plans, not inferred:** `akt1-plan_2026-09-11.md` sets an
explicit budget (*Akt I ≈ 24 000 Wörter; Kap 1 ≈ 2 500, sonst 1 600–2 300*) and Act I hit it
at 21,803. `akt2-arc-optimized` and `akt3-arc-optimized` state **no word budget at all**.
Act II/III were drafted without a target and landed at ~1,050.

Enrichment therefore does not override a plan. It applies Act I's own standard to the rest
of the novel.

This corroborates three defects already predicted in `written-chapters-audit_2026-09-11.md`
§ *Wiederkehrende Defekte*: world material thins in Act II/III (3), body cost thins as
chapters turn philosophical (5), and the scaling to cosmic function lacks visible
intermediate steps (10). That audit is otherwise stale — it predates the drafting of ch 6–40.

## 2. Goal / non-goals

**Goal.** Raise Act II and Act III to Act I's density by adding the material the audit names
as missing, reaching ~85–100k total prose words.

**Non-goals.**
- No storyform or NCP mutation. No change to ncp.json / ncp-b.json / dramatica.md.
- No re-plotting. Scene plans, beats and hook chains in the act arcs stay as they are.
- No line-editing pass and no copy pass. Those are separate rungs of the gate ladder.
- Act I is not rewritten. It receives the two open audit mandates only.

## 3. Target bands

| Wave | Chapters | Now (avg) | Target band | Rationale |
|---|---|---:|---|---|
| 1 | 33–39 | 966 | 1,900–2,300 | Climax; highest stakes, thinnest prose |
| 2 | 14–32 | 1,070 | 1,700–2,100 | Act II cycles + Act III build |
| 3 | 0–13 | 1,677 | hold | Audit fixes only |

Ch 40 (coda) is exempt from the band: the arc requires it to be *"etwa halb so lang wie
Kap 0"*. Ch 0 is exempt in the other direction — mandate G-01 requires it to shrink.

Projected total ≈ **82–88k**.

## 4. Method — packet before prose

`chapter-enrichment-masterplan_2026-09-11.md` § 2 already makes this binding:
*"Ein Kapitel ohne ausgefülltes Enrichment Packet ist nicht draftbereit."* Packets exist
only for ch 1–5. Every chapter in waves 1–2 therefore gets one first.

Per chapter, in order:

1. **Enrichment Packet** — masterplan § 2 sections A–F (scenic load, information balance,
   body/relationship arc, world materialization, motif ledger, readiness gate), committed to
   `Plan/drafting/enrichment-packets_<range>_2026-09-12.md`.
2. **Prose expansion** against that packet, the Drafting-Brief, and the neighbouring
   chapters' exit/entry chain.
3. **Readiness Gate** (masterplan § 2 F) + Welt-Sensorik § 10.3 self-review.

Packets are written and committed **before** any prose so that structure, hook chain and
information balance are locked before parallel drafting begins.

### What expansion adds

Expansion supplies exactly what the audit says is absent — never more words about the same
thing:

- **Body cost.** The conflict must change breath, gait, temperature, pain, touch or
  time-sense. Audit defect 5.
- **World materialization.** One Kernwelt per beat, with all six sensory parameters, one
  usable object, one spatial obstacle, one change produced by action, and one detail only
  this focalization would notice. Audit defect 3.
- **Counter-figure agency.** At least one figure or force acting from its own goal, not as
  an obstacle, an offer or a mirror. Audit defect 4.
- **Concrete hook-out.** An observable event — a deadline, a trace, a misattribution, a
  missing person, an irreversible act — never a theme or a rhetorical question. Audit
  defect 6.
- **Scaling rungs.** In Act III, the visible intermediate steps between private inner work
  and cosmic preservation function. Audit defect 10, mandate G-05.

## 5. Hard constraints on new prose

Every added sentence is bound by rules already in the repo. Violation is a defect, not a
style choice. The ones most at risk when adding length:

- **R-2 — never state what the reader should think.** The principal hazard. Doubling a
  philosophical chapter is exactly how a novel becomes a seminar. Each packet must name the
  explanations that chapter is forbidden to make.
- **R-1** never explain the tragic irony.
- **R-5** warmth (Juna, skin-warm, sourceless) and cold ozone (the order, sharp, electric)
  never in the same scene.
- **R-6** max one concept per scene — an expanded chapter gets more scenes, not denser ones.
- **R-8** the order / directives carry no metaphor, morality or affect.
- **R-10** Juna is never a grammatical subject, never named, never a voice, never a body.
- **D23-04** the Moonshine boundary transmits presence, salience, simultaneity and affective
  pressure — never words, memories, coordinates, facts or commands.
- **D23-07** after ch 36 the old AEGIS is procedural residue only; never a secretly
  surviving antagonist.
- **D23-12** ch 27–34 build confrontation capability and must not read as climax.
- Locked exact strings: ch 36 last voice *„Es bleibt."*; ch 39 final written sentence
  *„Das Licht ist schon da, als ich erwache."*

Voice references: ch 1 for Kael (Hard-A, 1st person present), ch 5 for the nameless
subjectless order-instance (Hard-B).

## 6. Wave 3 — Act I audit mandates

Two open items, both from the audit, both approved:

- **Ch 1 — remove the Spiegelversatz.** The mirror lagging by a blink is a second objective
  physical impossibility and strips the Korridorriss of its canonical standing as the single
  first break (Ein-Falschheits-Lock). Make the mirror respond synchronously; delete the three
  sentences of time-lag. Keep the imagined route-map as subjective overload, not confirmed
  geometric anomaly.
- **Ch 0 — mandate G-01.** Cut the essay-Vorwort by at least a third and bind the core
  question to a single image; reduce identity/architecture spoilers. Ch 0 stays an
  extratemporal frame outside the Teil-I contract (G-01 decided), so it keeps its register.

## 7. Execution

Packets are authored and committed per wave. Prose is then drafted by one subagent per
chapter, each carrying the full constraint brief of § 5 plus its own packet and its
neighbours' exit/entry chain. A continuity and voice pass across the whole wave follows
before commit.

## 8. Verification

Per chapter: word count inside band; Readiness Gate all-yes; R-1…R-10 scan; hook-in matches
the predecessor's hook-out; frontmatter and template head unchanged except `status` / `pov`.

Per wave: motif ledger updated; information balance consistent across the block; voice
spot-check against ch 1 and ch 5; locked strings verified verbatim.

## 9. Risks

| Risk | Mitigation |
|---|---|
| Voice drift across parallel agents | Strict shared brief; per-wave continuity pass by the orchestrator |
| Expansion becomes explanation (R-2) | Each packet names that chapter's forbidden explanations |
| Graph/disk divergence | **Verified:** the graph holds only ch 0's body plus 400–1,000-char outline stubs for ch 1–40 — every drafted chapter's prose exists on disk only, so the graph is not a source of truth for it. **Not verified:** whether `FileNovelStateDriver.create_chapter` overwrites existing files. The agency package is not installed in this environment, and `materialize_manuscript.py`'s own `skipped` / "already on disk" branch suggests it does not overwrite. The exposure is therefore that a fresh checkout, or any future change to that driver, silently yields stub chapters. A pre-flight guard is added that refuses to run when disk prose exceeds the graph body. |
| `:` in filenames of ch 21, 22, 34 | Known Windows checkout breakage (session learnings § 3). Out of scope here; noted for a separate change. |
