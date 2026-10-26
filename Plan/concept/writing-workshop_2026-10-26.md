# The writing workshop — the tools between the structure and the prose

*2026-10-26. The author asked for a long look at the project and how to proceed, „so we can start developing the Tools we Need to
Write the Story“, and answered ten questions the same day (decision 030). This is the plan built on those answers. Every
construct is `provisional` until the pilot Kap 1–3 has used it.*

## 1. Where the project stands, and what is missing

Three layers are finished or load-bearing; one does not exist.

| layer | state on 2026-10-26 |
|---|---|
| research | 584 documents read, 106 candidate pages, 41 chapter pages, graph, search, MCP; the ingest ended on 2026-10-23; the full read (thought pages) has its first page |
| structure | two Dramatica storyforms decided, the chapter scaffold 0–40 (`weave.json`), a treatment of 5,900 words (a proposal), `development.json`, the NCP; 17 canon rows in `Manuscript/kanon.md`; 29 Weichen open, 6 answered |
| prose attempts | Kap 1: ten drafts A–J; Kap 2: one draft on J; three plot drafts; no chapter approved; Kael, Juna and AEGIS are not formally canon as names |
| writing tools | **none.** Every tool serves research or structure. The writing skills read and critique; nothing joins canon, treatment, cards and drafts into one workplace. The four help tables of the 2026-10-06 session (`wissenstabelle.md`, `zeitleiste-akt-1.md`, `hitzegroessen.md`, `spuren-konkordanz.md`) are written by hand and age with every draft |

Between „the structure stands“ and „a scene exists“ there is no repeatable path: each of the eleven drafts was assembled from
what one session held in its head. That is the gap.

## 2. What the author decided (decision 030)

| # | question | answer |
|---|---|---|
| 1 | who writes the prose (question A of the writing plan, open since 2026-09-29) | **a session, scene by scene; the author approves the beats of a scene first and edits it before the next** (A2) |
| 2 | the 29 open Weichen | **only when needed, per chapter**: no round of answers in advance; a chapter's briefing puts the Weichen it touches |
| 3 | Kap 1's working base | **none yet**: no draft is the base until briefing and Weichen stand |
| 4 | the order of the book | **a pilot Kap 1–3, then Akt I in order** |
| 5 | what a briefing carries | **the decided and the proposed, marked apart** (`[K]` canon, storyform, weave, parts, cards; `[V]` treatment, beats, readings; open Weichen as questions before the scene) |
| 6 | continuity data per chapter | **all four**: knowledge (who knows what), time (day, clock, deadline), heat budget and numbers, objects/places/names |
| 7 | the prose rules from the sources | **a register with status, each rule confirmed by the author**; the mechanically checkable ones checked after a yes |
| 8 | chapter length in the pilot | **3,000–5,000 words** (W16 answered for the pilot: several scenes per chapter, about 150,000 words for 41 chapters) |
| 9 | how a scene is reviewed and approved | **marks per paragraph in the app, approval by the author's words** into `kanon.md` |
| 10 | what is built first | **every tool before the first scene** |

Answer 8 is the one that departs from the recommendation, and it decides the shape of a chapter: at 3,000–5,000 words a chapter
is three to six scenes, so the unit of work is the scene and a chapter is a sequence of them.

## 3. The six tools

Each is standard library, has an offline fixture, a selftest in `selftests.py`, and a CI step where it checks a file the
repository commits. Each writes only where the authority table of CLAUDE.md allows: nothing a tool writes is canon; the author's
words are.

### 3.1 `rules.py` — the prose-rule register

The sources are full of rules for the prose (the first sentence, no AEGIS voice in Kap 1, no metaphors in KW1, „Trennungsprotokoll“
never on Kael's side, cold ozone once, no mention of amnesia …). Decision 006 says none binds until the author confirms it. Today they
live in the Kap-1 README's lock table, in `sp-sperren-2026-05.md`, and in the chapter pages.

- `Manuscript/regeln.jsonl`: one row per rule — `id`, `text` (German), `source` (`^[slug.md:Lnn]` or a Weiche), `scope`
  (chapters or Kernwelt), `status` (`offen` | `bestätigt` | `verworfen`, with the author's words and date), `check`
  (`none` | a named mechanical check), `added` (date, by).
- `rules.py list [--scope kap-01]`, `confirm <id> --words`, `reject <id> --words`, `check <draft>`.
- The **standing rules** that always hold are in the register as `bestätigt` from the start, by the author's instructions of 2026-10:
  early names and the „ehem.“ names never written, no real persons' names, no gendered pronoun for Kael, Juna, AEGIS or a part,
  world codes never expanded, the trauma symbol never written, „Kernwunde“ only. These are the first mechanical checks.
- Mechanical checks beyond those, built as the pilot needs them: forbidden words per Kernwelt, person and tense of the narration,
  a named line that must be the first, a forbidden word on a figure's side.
- A check never edits. A violation of a `bestätigt` rule fails; of an `offen` one it is a query.

### 3.2 `weiche.py` — the switch board

Answering a Weiche today means editing its sheet and adding a `kanon.md` row by hand.

- `weiche.py list` (status, what each frees), `show <id>`, `answer <id> --words "…" [--option A]`: sets `status: beantwortet`
  with the author's words and date, appends the canon row, names the treatment paragraphs, `development.json` rows and chapters
  the sheet lists as depending on it. `defer`, `replace`.
- `check`: an answered sheet has words and its canon row; a canon row that names a Weiche has an answered sheet.
- Which Weiche a chapter needs comes from the briefing (3.4), not from a round: the author's answer 2.

### 3.3 `continuity.py` — the register per chapter

- `Manuscript/kontinuitaet/kap-NN.json`: what holds **at the start and at the end** of a chapter in four tables — `wissen`
  (Kael, AEGIS, the reader: what each knows, with the chapter it was learnt in), `zeit` (day, clock, the deadline), `zahlen`
  (the heat quantities, 114/251, 734, the Zuweisung …), `dinge` (objects, places, names, each with the chapter it entered).
- Seeded from the four hand tables of 2026-10-06 with their provenance (`provisional` rows, marked as proposals), then written
  from canon and **approved** scenes only: a draft changes nothing in the register until approved.
- `continuity.py show kap-NN`, `check <draft>`: every number, time, name and place in a draft against the register, and every
  fact the draft states against `wissen` — each collision a query with both passages, as the `continuity-editor` skill does by
  hand. It never decides which version holds.

### 3.4 `brief.py` — the chapter briefing

The contract for every scene: what a session writes is in the briefing and nothing else.

- `brief.py kap NN` writes `Manuscript/kap-NN/briefing.md` with these sections, every bullet tagged as on a term page:
  1. **Entschieden** `[K]`: the canon rows that touch the chapter, the storypoints (`a.json`, `b.json`), the weave row,
     the parts' appearances (`anteile.json`), the figure cards' canon blocks, confirmed rules in scope.
  2. **Vorgeschlagen** `[V]`: the treatment paragraph, the `development.json` row (goal, opposition, action, turn, cost,
     knowledge, timing), the scene list with beats, the drafts that exist for the chapter and what each chose.
  3. **Quellen** `[S]`: the chapter page's readings, the thoughts of the term pages the chapter touches (the full read),
     each cited — research, never canon.
  4. **Kontinuität**: the register's state at the start of the chapter (3.3).
  5. **Offen**: the Weichen the chapter touches that are not answered, each with its options and the recommendation — **the
     questions the author answers before the first scene**; the rules in scope that are `offen`.
  6. **Szenen**: the scene list with each scene's status (beats proposed / beats approved / drafted / edited / approved).
- `check`: a briefing names the hash of its inputs; it is **behind** when canon, a Weiche, the treatment, the register or a
  rule in scope changed since. A scene is written only on a current briefing.

### 3.5 `manuscript.py` — scenes, approval, the book

- A scene is `Manuscript/kap-NN/szene-N-<slug>.md` with frontmatter: `kapitel`, `szene`, `status`, `beats` (the approved
  beats, verbatim), `briefing` (hash), `geprueft` (rules, continuity: run and when), `freigegeben` (date, the author's words).
- `manuscript.py status` (the grid 0–40: scenes, words, status), `beats kap-NN szene-N --words` (the author approves beats),
  `approve kap-NN szene-N --words` (refuses while rules or continuity are unrun or red, or the briefing is behind; appends
  to `kanon.md` § Freigegebene Kapitel when every scene of a chapter is approved), `build` (the book as one file, approved
  scenes only, with the drafts behind a marker), `findings kap-NN` (the writing skills' findings in `Plan/runs/writing/`
  registered per scene).
- The Kap-1 drafts A–J and Kap 2 A stay as they are: poles, never the base (answer 3).

### 3.6 The Schreibtisch in the app

A tab in the Manuscript screen (decision 024), `#/manuscript/schreibtisch[/kap-NN[/szene-N]]`:

- the grid Kap 0–40 with status and words; per chapter the briefing (the five sections as panels), the scenes, the findings,
  the open Weichen with their options and a **copyable answer prompt**;
- per scene the text with **marks per paragraph** („passt / Frage / falsch“ and a note), kept in the browser, exported as one
  text the author pastes into a session — the author's answer 9; no button approves anything, the words do;
- the rules register with status and a copyable confirm/reject prompt;
- every item with an address and an `agents/index.json` entry; `ui.py --check` cases for an empty grid, a scene whose
  briefing is behind, a mark on a paragraph that is not there.

## 4. The loop of one scene

```
brief.py kap NN              the briefing; its § Offen → the author answers the Weichen it names (weiche.py answer)
   │                         and confirms or rejects the rules in scope (rules.py confirm)
   ▼
beats                        the session proposes the beats of scene N from § Vorgeschlagen; the author approves them
   │                         (manuscript.py beats --words) — the only text the session writes before the scene
   ▼
the scene                    the session writes szene-N on the approved beats, in the briefing's bounds, 3,000–5,000 words
   │                         per chapter over its scenes
   ▼
rules.py check · continuity.py check · the writing skills (continuity-editor, line-editor as the author asks)
   │
   ▼
the author                   marks per paragraph in the app, edits the file or dictates the changes; the session revises
   │
   ▼
manuscript.py approve --words   the scene is approved; the register (3.3) takes what it establishes; the next scene
```

A chapter is approved when its scenes are; then `kanon.md` lists it, and the briefing of the next chapter starts from the
register the approved chapter left.

## 5. Order of building, and the pilot

The author's answer 10: every tool before the first scene. Order, each a commit with its selftest:

1. `rules.py` with the standing rules as checks (the first thing any draft is held to);
2. `weiche.py`;
3. `continuity.py` with the four tables seeded;
4. `brief.py` for Kap 1 (it needs 1–3);
5. `manuscript.py`;
6. the Schreibtisch.

Then the pilot: `brief.py kap 1` → the author answers Kap 1's Weichen (by the sheets, W2, W3, W5, W7, W28 … whichever the
briefing lists) → beats of scene 1 → the scene. W16 is measured after Kap 3 against the 3,000–5,000 the author set.

## 6. What stays judgement

The beats, the prose, which reading of a source enters a scene, whether a continuity collision is a mistake or a change,
which rule holds — all the author's. The tools say what is decided, what is proposed, what collides and what is unchecked;
they write no prose and promote nothing.

## 7. Provisional

```yaml
writing-workshop:     # provisional — planned 2026-10-26 on the author's ten answers, before any scene
# may not: write or rewrite prose, approve a scene, answer a Weiche, confirm a rule, or let a draft change the register
# retire when: the pilot Kap 1–3 shows the author writes without the briefing or the register
```
