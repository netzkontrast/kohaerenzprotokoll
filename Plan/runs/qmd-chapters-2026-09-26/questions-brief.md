# Brief — questions per chapter, before any search

The author, 2026-09-26: „For each chapter First Build a List of questions for each
one. Keep dramatica and Everything you know about writing a novel in Mind.
Especially Everything the goal md discribes. ASK more than One question."

The questions come first. They are what the qmd vector search is then asked,
one question at a time, so a candidate source is tied to the questions it came
back for. A question is also navigation in its own right: it says what a reader
of this chapter's sources should be looking for.

## Two kinds: basic, then specialised

The author, later the same day: „Build a few Basic questions every Autor must
ask for a chapter - and then more specialized questions for the chapter".

- **Basic** — `basic-questions.json`, eight questions every author asks of any
  chapter: goal and opposition, stakes, change, point of view and voice, place
  and body, way in and way out, function in the whole, the reader and the
  theme. They are the same for every chapter and are filled with its number
  and titles by `scripts/chapter_sources.py`. Nobody writes them per chapter.
- **Specialised** — the per-chapter files this brief asks for. They go
  **beyond** the eight: never a basic question again in other words. Where a
  specialised question touches the same ground (a hook, the point of view), it
  names what only this chapter has — the named hook from Kap N-1, the
  storyform position, the record, the world.

## What to read

1. `GOAL.md` §4.5 (the nine question generators and „Qualität vor Menge"),
   §5.1–§5.5 (the four structure levels, the dual storyform, the constants of
   the end, scene and chapter discipline, the plot generators and the
   Readiness Gate), and §1 rule 5 (Story-First: theory diagnoses, it does not
   prescribe).
2. The chapter page `Wiki/chapters/kap-NN.md`, whole: every reading, the
   `records:` frontmatter, and `## Where the sources differ`.
3. The neighbours' pages, `kap-(NN-1)` and `kap-(NN+1)`, as far as needed to
   ask about the hook in and the hook out.
4. Where the page names a conflict or question record (`records:`), that record
   in `Wiki/conflicts/` or `Wiki/questions/`.

Read nothing in `Sources/drive/`. The questions are asked of the sources
afterwards, by search; a question written from a source would find that source.

## What a question is

- **German**, as GOAL.md asks for questions; Dramatica terms stay English
  (Storyform, Throughline, Storypoint, MC, IC, OS, RS, Driver, Limit …).
- **Self-contained.** Each one is sent to a vector search alone, with nothing
  around it. So it names `Kapitel N` and the concrete subject — the figure, the
  world, the event, the motif — never „dieses Kapitel" or „die Szene" alone.
- **One question, one thing.** At most about 40 words.
- **Open where the sources are open.** Decision 006: no draft and no lock
  settles anything, so a question never presupposes one reading. Where a
  premise comes from one source, the question attributes it („laut der Outline
  vom 2026-05-18 …", „nach GOAL §5.4 …"), or asks between the readings.
- **A question whose answer changes no writing decision is noise** (§4.5). Ask
  what would block encoding or drafting this chapter.
- **No quotation marks „…", no `^[…]` citations, no `[[links]]`.** The
  quotation checker would count an uncited quotation, and a question is not a
  reading. Name a title or a phrase in plain words or in *italics*.

## How many, and which

**Eight to twelve per chapter**, each tagged with the generator it comes from.
Every chapter gets at least one question from each of:

| tag | from | the question asks |
|---|---|---|
| `Konkretheit` | §4.5 #3 | figure, repeatable action, object, place, loss, direction of escalation — what Kael *does, loses, risks* on this day |
| `Kausalität` | §4.5 #4 | hook in from Kap N-1, hook out to Kap N+1; two genuine losses of a future instead of right/wrong; what is irreversible |
| `Leser-Wissen` | §4.5 #5 | what reader, Kael and AEGIS each know, wrongly believe, cannot yet know at the end of Kap N; which false, plausible reading stays standing |
| `Storyform` | §4.5 #7, §5.2 | which Storypoints the chapter carries in A and in B, whose throughline, the bridge share for its act band, Slot 16 |
| `Struktur` | §5.1, §5.3 | its place in Kishōtenketsu, in the three modes (the Murdock stage for Kap 1–13, the cycle Z1–Z3 for 14–26, the hero's-journey stage for 27–39), the brackets (0↔40, 1↔39, Vortex 1↔2), and whether it sits on one of the three kinds of transition |

and, where the page gives grounds for one:

| tag | from | the question asks |
|---|---|---|
| `Konflikt` | §4.5 #2 | a record in `records:`, or a point under *Where the sources differ*, asked as what would decide it |
| `Lücke` | §4.5 #1 | what no reading on the page says at all — a missing world, POV, beat, sensory anchor, title |
| `Setup/Payoff` | §4.5 #6 | an anchor or foreshadow strand planted or paid off here: where it was planted, where it pays off |
| `Welt/Sensorik` | §5.4 | the Kernwelt, the heat polarity (cold ozone / warmth), the concept and layer per scene, theory as image never naked |
| `Figur` | §5.4, craft | an alter's or Juna's or AEGIS' way of appearing here, voice, the rules for Juna and AEGIS |
| `Impact` | §4.5 #8 | if the author changes X in this chapter, what tips elsewhere |
| `Steinbruch` | §4.5 #9 | which older `[S]` material could fill a `[L]` gap here without breaking a lock |

Craft beyond GOAL.md is welcome where it bears on this chapter — scene goal and
opposition, the chapter's promise as a question, midpoint and pinch functions,
pacing against the neighbours, what the chapter's ending exports. Tag such a
question with the nearest tag above.

## What to write

One file per chapter, `Plan/runs/qmd-chapters-2026-09-26/questions/kap-NN.json`:

```json
{"chapter": 12,
 "questions": [
   {"id": "K12-01", "tag": "Konkretheit",
    "question": "Was tut Kael in Kapitel 12 konkret …?",
    "draws_on": "the reading of three-mode-architecture-39-chapters-md; GOAL §4.5 #3"}
 ]}
```

`draws_on` says what on the page (which reading, which difference, which record)
or in GOAL.md made the question worth asking — in English, a few words. It is
the question's provenance.

Write nothing else. Change no page.

## The basic eight, filled with the plot

The author, after seeing the basic eight filled only with a chapter's number
and titles: „Fill it with what we know about the Plot - Not Numbers".

So each chapter file also gets a `basic` list: the eight questions of
`basic-questions.json`, **rewritten for this chapter with what its readings say
happens in it**. Each keeps its basic question's craft core (B1 goal and
opposition, B2 stakes, B3 change, B4 point of view and voice, B5 place, time
and body, B6 way in and way out, B7 function in the whole, B8 reader and theme)
and fills it with the chapter's plot: who acts, where, what happens, what is
lost, what comes before and after. For example, not „Was will die
Perspektivfigur in Kapitel 12?" but „Was will Kael in der Stille der Mitte,
wenn …, und was stellt sich ihm entgegen — …?".

- **No numbers.** No chapter number, no date, no count carries a question. Name a
  neighbour by what happens in it („nach dem Audit", „vor dem Sprung ins
  Rauschen"), a source by its short name („die strukturierte Outline", „die
  Charakter-Bibel", „das Kapitel-Kompendium", „die Plot-Konkretisierung").
  A name that is a number in the world itself — Komponente 734, KW1 — may stay.
- **Only what the page's readings say.** The facts come from the chapter page
  and its neighbours, nothing else. Where the readings differ, the question asks
  between them („wenn er laut der Charakter-Bibel … und laut der Outline …").
  Where the page says nothing, the question says so („wo keine gelesene Quelle
  einen Ort nennt").
- Everything else in *What a question is* stands: German, self-contained, no
  „…", no `^[…]`, no `[[links]]`, one question, at most about 50 words.

```json
{"chapter": 12, "questions": [...],
 "basic": [
   {"id": "B1", "question": "Was will Kael in der Stille der Mitte …?",
    "draws_on": "readings of X and Y"}
 ]}
```

Exactly eight, `B1` to `B8`, in order. Add the `basic` key to the existing file
and leave its `questions` untouched.

## What the chapter is about

The author, next: „Also add what each chapter is about".

So each chapter file also gets an `about` text: **three to five German
sentences saying what the chapter is about, as its readings tell it** — who,
where, what happens, what changes, what it is for in the whole. It summarises
the readings on the page and decides nothing between them (decision 006):

- Where the readings agree, say it plainly.
- Where they differ, say so and give each version its source by short name
  („Laut der Charakter-Bibel …, laut der strukturierten Outline …"). Never pick
  one, never blend two into a version no source wrote.
- Where no reading says something (a place, a point of view), leave it out; do
  not fill it from craft or from another chapter.
- The same form rules as the basic questions: no chapter numbers, no dates, no
  counts; no „…", no `^[…]`, no `[[links]]`. It is a summary, so no quotation.

```json
{"chapter": 12, "questions": [...], "basic": [...],
 "about": "Kael …",
 "about_draws_on": "readings of X, Y and Z"}
```

It stands on the chapter page above the readings, marked as a summary of them,
and it is sent to the vector search as one more query — a passage describing the
chapter, which finds documents that describe the same thing.
