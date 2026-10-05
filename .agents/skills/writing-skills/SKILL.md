---
name: writing-skills
description: >-
  Entry point for the thirteen editorial, critique, character and craft skills
  adapted from netzkontrast/writing-skills for Kohärenz Protokoll's German
  manuscript. It says which one to run at which step of making a chapter, and
  the rules all of them share here: what counts as the book's canon (the
  author's decisions and approved chapters, never the wiki's readings), where
  findings are written, how lines are cited, and that none of them writes or
  rewrites the author's prose. Use it before running any of them, and whenever
  asked for a Lektorat, Korrektorat, Testleser, Werkstattkritik, a continuity
  check, character cards or craft drills on the novel. Route plot and NCP development
  to storyform and chapter-beat review to scene-architecture's repository mode;
  preserve the separation between decided structure, canon, working bases and proposals.
license: MIT
metadata:
  upstream: "netzkontrast/writing-skills@2fad031982cbbcb00c4da14c2fc9712d2daa78da"
  adapted: "2026-09-29; repository plot/review routing updated 2026-10-06"
---

# Writing skills — which one, when, and the rules they share here

Thirteen skills that read, critique, simulate a reader or drill the writer. None
of them writes the book. They were copied from `netzkontrast/writing-skills` at
`2fad031` (MIT, © 2026 Rhymenoceros s. r. o. (Calliope); each folder carries the
licence) and adapted to this repository: German prose, this project's canon, its
citation rule and its artifacts. The end of this page lists what was changed.

## Which one, when

The plan for writing the novel is `Plan/concept/novel-writing-plan_2026-09-29.md`,
and these skills are its reading side.

| step | skill | on what |
|---|---|---|
| plot, throughlines, signposts or generated NCP | `storyform` | current source JSON, relevant decisions, chapter proposals; approved structure wins |
| chapter beats or variant comparison | `storyform` → `scene-architecture` (planning/review mode) | all complete variants and the chapter's structural contract; no drill intake |
| the cast, before drafting | `character-card-builder` | the author, interviewed one figure at a time |
| a chapter draft | `line-editor`, `copy-editor` | the chapter file |
| a chapter draft, against the book | `continuity-editor` | the chapter and the approved chapters before it |
| the cold read | `beta-reader-panel` | only the approved chapters up to this one |
| a chapter that stands alone, or the frame | `workshop-critique` | Kap 0, Kap 40 or any single chapter |
| the opening | `agent-first-pages` | the opening chapters, as a submission is read |
| the cast, after drafting | `reverse-character-cards` | an act or the book |
| an act, or the whole draft | `developmental-editor` | drafted acts only; a book not yet drafted is outside its own scope |
| the writer's own practice | `scene-architecture`, `psychic-distance`, `prose-rhythm`, `dialogue-gym` | the writer's attempts, never the manuscript |

## The rules they share here

1. **None writes or rewrites the author's prose.** This is upstream's one rule,
   kept whole. Here it also means that no skill edits a chapter file, the
   treatment's prose or a wiki page. Editorial and coaching output is a file of
   findings (rule 6). The separate `storyform` planning workflow may update authorized
   work-language chapter proposals and regenerate NCP; this is not permission to
   compose manuscript passages.
2. **What counts as the book's canon.** Only three things count:
   - the author's decisions: a record in `Wiki/conflicts/` or `Wiki/questions/`
     that carries a dated decision by the author (`status: decided`), and the
     book's own decision files once they exist;
   - chapters the author has approved;
   - the book's rulebook and treatment only to the extent explicitly approved;
     a chosen draft, plot draft or scene list remains a proposal under decision 025
     step 38, even when used as a working basis.

   **Structural authority:** `Plan/storyform/a.json`, `b.json` and `weave.json`
   carry the approved plot structure and provenance. Use the `storyform` skill to
   interpret them; their generated overview is not independent evidence of approval.
   Distinguish approved casting from provisional wants and approved world bands from
   undecided names. Later corrections in the decision record win.

   **Not canon:**
   - the wiki's readings, and the sources behind them. That includes a source
     that calls itself canon or „Source-of-Truth" (decision 006).
   - unapproved drafts under `Manuscript/`, chapter development in
     `Plan/storyform/development.json`, and scene-list recommendations. Do not infer
     acceptance from a file's name, its recency or its being included in generated NCP.
   - the parked draft under `Legacy/`. The author, 2026-09-29: „The novel in
     Legacy is Not the quality I want".
   - the canon of the account's novel skills (`novel-architect`,
     `chapter-briefing-architect`, `chapter-draft-engine`), which predates
     decision 006.
3. **The wiki is research, and may be quoted as research.** A term page, a
   chapter page or a record may be quoted to say what the sources said. Where the
   author is still undecided, the sources' positions, cited, are the honest
   „contrasting menu" upstream allows. A finding never corrects the text toward a
   source.
4. **A designed crack is not a slip** (`GOAL.md` §1.6). Mosaic breaks,
   unreliable narration, contradictory footnotes and unlabelled voices count as
   designed until the author says otherwise. A contradiction inside the prose is a
   defect only when it breaks a decided rule. Otherwise it is a query: „bewusster
   Riss?".

   Take the list of pre-cleared devices from the book's rulebook. Until the
   rulebook exists, ask the author. `GOAL.md` §5.4 may be offered only as a list
   of candidates.
5. **German.** The manuscript is German, so findings are written in German,
   quotations stay verbatim, and a craft term is explained where it first appears
   (upstream principle 7). Findings address the author directly, as „du", the way
   upstream addresses the writer as „you". They never refer to the author in a
   gendered third person, such as „die Autorin" or „der Autor". A skill's output
   headings may keep their English names, since they are structure and not findings. Wherever German rules differ from
   English ones, the German rules apply; `copy-editor` carries them.
6. **Every run keeps its artifact.** Findings are written to
   `Plan/runs/writing/<target>/<skill>_<YYYY-MM-DD>.md`, where `<target>` is one of:
   - `kap-NN`, `akt-N`, `opening` or `book`, for the book;
   - `drills`, for the four coaches, when the author wants a round kept;
   - a name for any other text, such as `legacy-kap-01` for a test on the parked
     draft.

   The top of the file names the input: file, lines and commit. A variant review
   enumerates every input and separates full prose drafts from comparison notes;
   re-enumerate before claiming completeness. Read all Kap 1 variants A–I and any
   later additions when the author asks for all drafts. The chapter and the wiki
   are never written by an editorial or coaching run.
7. **A line is cited, never typed** (P12, P26). Every quoted line carries
   `<file>:L<n>`, taken from `rg -n` or `nl -ba`. The quotation is the line's
   own words.
8. **The author decides** (P0). A finding is a proposal. Which version holds is
   the author's call, recorded where the plan says. The skill never records it.
9. **Independent readers are separate subagents.** `beta-reader-panel` and
   `workshop-critique` prefer independent contexts. Here that means one Agent per
   reader, given only the text and its lens: never the author's hopes, never the
   brief, never another reader's reaction. Only the synthesis sees them all.
10. **Nothing leaves the container.** These skills run on the session's model.
    The manuscript goes to no third-party service without the author's yes, the
    same rule Jev and every model call keep (`CLAUDE.md`).

## What was changed from upstream

- **Flattened.** Each skill moved from `skills/<category>/<name>/` into
  `.agents/skills/<name>/`, and `.claude/skills/<name>` links to it (P6). Two
  links to `../../editorial/line-editor` now read `../line-editor`.
- **Descriptions rewritten.** Each now says when the skill applies to this book,
  and the refusal is kept.
- **`## With Calliope (MCP)` replaced by `## In this repository`.** The Calliope
  connector does not exist here, and the new section says what does.
- **`copy-editor` follows German rules.** The amtliches Regelwerk and the Duden
  replace the Chicago Manual of Style. German typography and German punctuation
  of direct speech replace the English conventions.
- **Metadata.** `writes_back` is dropped, since it signals Calliope's Map.
  Upstream's `status: reviewed` is kept as upstream's claim, beside `adapted:`.
- **Plot routing added.** `storyform` protects the approved structure and generates
  NCP 3; `scene-architecture` adds a repository planning/review mode alongside its
  unchanged coaching ladder. Variant inventories, knowledge/cost tracking and
  proposal boundaries make that mode usable for chapter work.
- **Editorial rubrics retained.** The other lenses and their critique output shapes
  remain upstream's; training and manuscript review are still separate services.

## Provisional

```yaml
name: writing-skills   # provisional, and so is each of the thirteen adaptations
# may not: write, rewrite or continue prose; decide what is canon; treat a
#          source or the Legacy draft as the book; send the manuscript anywhere
# retire when: the plan's pilot (Kap 1–3) has run them and Plan/learnings/ shows
#          the adaptation added nothing over upstream — then vendor upstream unchanged
```


## Review a chapter against its plot without flattening it

Use three distinct verdicts: **structural compatibility**, **causal execution**,
**reader experience**. Every alleged contradiction names the decided rule and the
observed draft line; every improvement names the gain, cost and open assumption.
Do not call an early refusal a violation of Change, action a violation of Be-er, or
any scene deadline a violation of Optionlock. Do not demand explanatory labels for
an intentional crack merely to make the diagram tidy.

For continuity, track the knowledge of the POV, other figures and the reader,
physical consequences, promises, timing and the next forced choice. For reader
simulation, give only approved/read-so-far text to independent readers; structural
review may use the planning contract but must not leak it into a cold-reader pass.
The practical next edit should strengthen opposition, consequence or a figure's
independent want, rather than accumulate lore that never changes a scene.

Put draft-derived canon candidates in a proposal artifact with exact evidence and
an explicit unresolved choice. Only an author's explicit decision can change
`Manuscript/kanon.md`; do not append it as the automatic result of a positive review.
Use `scripts/storyform.py` to regenerate the current NCP 3 file, then `--check`.
The older 1.3 `ncp-author` validator does not certify this document. Name which
structural, freshness and schema checks actually ran, and keep scene-quality
judgement separate from their results. Follow `app-refresh` before a PR.
