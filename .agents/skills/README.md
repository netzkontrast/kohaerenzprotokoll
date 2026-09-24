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
| `ingest/SKILL.md` | take one research document from `Sources/drive/` to a reconciled state a person can review |
| `tools/SKILL.md` | run the loop that extends the wiki: which command runs when, and what each consumes and produces |
| `qmd/SKILL.md` | search and read the German corpus with qmd: which collection answers which question |
| `dspy/SKILL.md` | write or change anything that imports `dspy` or `gepa`, or calls a model — DSPy 3.3.1 as this repository uses it |
| `typesafe/SKILL.md` | build with TypeSafe's Jev, a model that answers typed questions |

`ingest`, `dspy` and `typesafe` end in a *Provisional* block: what the skill may
not do, and the evidence that would retire it. `tools` and `qmd` carry none yet.

## Not here: the vendored skills

`.claude/skills/` also holds folders copied unchanged from other repositories —
`jev*`, `hyper*`, `graphify`, `knowledge-graph-extract` and the Notion skills.
They are real folders, not links, because they are not this project's to edit.
`CLAUDE.md`, *Installing anything*, says where each came from and at which
commit; `check_skills.py` reports their findings under their own heading and
never fails on them.
