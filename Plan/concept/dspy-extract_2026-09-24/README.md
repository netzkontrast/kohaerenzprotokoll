# What nine DSPy repositories contain — the readers' notes, 2026-09-24

The evidence behind `.agents/skills/dspy/`. On 2026-09-23 ten readers scanned
the same nine repositories for *ideas this project could use*
(`Plan/concept/dspy-repos_2026-09-23/`). On 2026-09-24 the author asked for
**all the knowledge** in them, organised so the repository can use it. So nine
readers read the repositories again, in full, code included. This time they
recorded every fact rather than a selection of ideas: each API detail, parameter
and default, recipe, number with its conditions, trap and documented mistake,
each with the line it came from. A tenth reader collected what this repository
has itself measured and decided about models.

| file | repository, commit | reader |
|---|---|---|
| `das-core.md` | `dspy-agent-skills` 9d13f98 — core API and operations skills, tests, the check script, CHANGELOG, examples | default model |
| `das-book.md` | `dspy-agent-skills` 9d13f98 — the nine `dspy-book-*` skills, articles | default model |
| `das-rlm-rag.md` | `dspy-agent-skills` 9d13f98 — RLM skills, drg-kg, refrag, TARA, the canon retriever scaffold | default model |
| `das-patterns.md` | `dspy-agent-skills` 9d13f98 — the seven knowledge-work skills and the two plans written about an earlier form of this project | default model |
| `dspydantic.md` | `dspydantic` 1afc528 | default model |
| `session-optimizer.md` | `dspy-session` eb67e76, `dspy-optimizer` a07b3b7 | default model |
| `agents-rag.md` | `dspy-agents` fde0dad, `Agentic-Dspy-Rag` 474f107 | default model |
| `auto-gepa.md` | `dspy-auto-gepa` 80a5402 | default model |
| `braid-prompting.md` | `braid-dspy` c50c5b1, `dspy-advanced-prompting` facc1ad | default model |
| `this-repo.md` | this repository's own record on models: `Plan/`, the scripts, the skills | Sonnet |
| `details-drg-mmr.md` | two details settled for the port: drg-kg's import side effects, the MMR λ convention | Sonnet |

`00-brief.md` is the brief every reader of the nine got, verbatim.

## How to read them

- **They are notes, not the skill.** Each item carries its `path:line` and a tag:
  `[api]`, `[recipe]`, `[number]`, `[trap]`, `[pattern]`, or `[claim]` when the
  repository asserts it and the reader could not verify it. Where a reader ran
  something, the item says what. The skill selects and organises; when the two
  disagree, the skill's `[checked: …]` marks and `surface` blocks have been
  re-run against the installed DSPy 3.3.1 by `scripts/check_dspy_skill.py`, and
  the notes have not.
- **A note's quotation marks are not a promise.** Readers quoted, condensed
  and titled findings in one voice, so words in quotation marks in a note may be
  the reader's own. On 2026-09-24 every quotation in the skill was searched for
  in its sources, and those that were only a note's words were corrected or
  unquoted; the notes themselves were left as the readers wrote them.
- **Paths inside a note are the scanned repository's**, unless the note says
  otherwise. `<scratchpad>` stands for the session's scratch directory, where
  the readers kept their probe scripts and throwaway venvs. Those were not
  kept.
- **Where a note mentions `Legacy/`**, it records where the retired pipeline's
  files now sit. That is provenance, not a dependency: nothing reads them
  (`CLAUDE.md`, `Legacy/`).
- Every reader ran with every `*_API_KEY` unset. On 2026-09-23 an unmocked test
  in `dspy-auto-gepa` made a live call from this container; `auto-gepa.md`
  records that the test is still unmocked at 80a5402 and that the guard blocked
  it this time.

## What the re-read corrected

Each note ends with "The old report, corrected". The corrections that changed
what this repository does:

- `lmrun.py` did not recognise DSPy 3.3's own error types, so a refused
  connection raised instead of being recorded as `unreachable`. Found by
  verifying the API, fixed 2026-09-24.
- `dspy.RLM` answers even when it runs out of iterations. The only marker is
  `final_reasoning == "Extract forced final output"` (`session-optimizer.md`,
  `das-rlm-rag.md`). `rlm_ingest.py` now calls such an answer a
  reconstruction.
- The „Unsupported value type: History" failure that `lmrun.py` cited belongs
  to DSPy 3.1.3. On 3.3.1 the same wrapper fails at once.
- `bool(dspy.Prediction(score=0.0))` is `True`, so the bootstrap family keeps
  wrong demos when given a Prediction-returning metric (`das-core.md`).
  `pairs.py` already unwrapped `.score`.
