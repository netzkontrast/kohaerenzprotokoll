# `.agents/skills/` — this project's own skills

A skill is a `SKILL.md` an agent loads by its `description` when the task at hand
matches it. The ones here are this project's; `.claude/skills/<name>` is a
symlink to each (P6: one copy), and `python3 scripts/check_skills.py` holds both
the spec and the links.

**This page is checked, not remembered.** 0 <!--state:readme.skills_drift-->
skills are missing from it or listed here without existing, and
`python3 scripts/state.py --prose` fails the day that number is not 0.

| skill | use it to |
|---|---|
| `reader-tools/SKILL.md` | prepare delegated readers and select initialized source, retrieval and graph CLIs within their assigned scope |
| `hyperextract-learning/SKILL.md` | build and test extraction templates, stage quote-backed proposals and improve guidelines from measured failures |
| `ingest/SKILL.md` | take one research document from `Sources/drive/` to a reconciled state a person can review |
| `tools/SKILL.md` | run the loop that extends the wiki: which command runs when, and what each consumes and produces |
| `graph-context/SKILL.md` | retrieve budgeted evidence and explore the existing graph through the local GraphQLite CLI |
| `qmd/SKILL.md` | search and read the German corpus with qmd: which collection answers which question |
| `dspy/SKILL.md` | write or change anything that imports `dspy` or `gepa`, or calls a model — DSPy 3.3.1 as this repository uses it |
| `typesafe/SKILL.md` | build with TypeSafe's Jev, a model that answers typed questions |
| `storyform/SKILL.md` | read and change the novel's two Dramatica storyforms in `Plan/storyform/`: one question to the author at a time, every value with its provenance |
| `jules/SKILL.md` | spawn a Google Jules session on a GitHub repository, drive it through its plan, and verify it pushed |

`ingest`, `dspy`, `typesafe`, `jules` and `writing-skills` end in a *Provisional* block: what the skill may
not do, and the evidence that would retire it. `tools` and `qmd` carry none yet.

## The writing skills — reading, never writing, the novel

Thirteen skills from `netzkontrast/writing-skills` at `2fad031` (MIT; each folder
carries the licence), adapted on 2026-09-29 to the German manuscript and this
repository's rules. Adapted means they are this project's to edit, so they live
here and not with the vendored skills. `writing-skills/SKILL.md` is their entry
point: which one to use when, the rules they share, and what was changed from
upstream. None of them writes or rewrites the author's prose.

| skill | use it to |
|---|---|
| `writing-skills/SKILL.md` | choose which of the thirteen to run at which step of making a chapter, and read the rules they share here |
| `developmental-editor/SKILL.md` | get a manuscript assessment or edit letter on a drafted act or the whole draft |
| `line-editor/SKILL.md` | find the recurring sentence-level habits in a chapter draft, flagged with the principle and a direction |
| `copy-editor/SKILL.md` | sweep a chapter's mechanics by German rules (amtliches Regelwerk, Duden) and keep the book's style sheet |
| `continuity-editor/SKILL.md` | check a chapter against the book's facts, numbers, timeline and knowledge state as the author has decided them |
| `reverse-character-cards/SKILL.md` | card the players who are actually on the page, and compare them with the cast intended |
| `character-card-builder/SKILL.md` | interview the author, one question at a time, into the cards of the cast ledger |
| `beta-reader-panel/SKILL.md` | read the approved chapters cold, through distinct and blind reader lenses: the plan's cold read |
| `agent-first-pages/SKILL.md` | test the opening as a German agency or publisher would first read it |
| `workshop-critique/SKILL.md` | put one self-contained chapter through a Milford/Clarion-style table |
| `dialogue-gym/SKILL.md` | drill the author's dialogue and the alters' distinct voices |
| `scene-architecture/SKILL.md` | drill how the author builds scenes: goal, conflict, disaster, sequel |
| `psychic-distance/SKILL.md` | drill narrative distance: Gardner's rungs, erlebte Rede, the first-person dial |
| `prose-rhythm/SKILL.md` | drill cadence in German: length, the landing word, sound, syntax as pacing |

## Not here: the vendored skills

`.claude/skills/` also holds folders copied unchanged from other repositories —
`jev*`, `hyper*`, `graphify`, `knowledge-graph-extract` and the Notion skills.
They are real folders, not links, because they are not this project's to edit.
`tools/references/install.md` says where each came from and at which
commit; `check_skills.py` reports their findings under their own heading and
never fails on them.
