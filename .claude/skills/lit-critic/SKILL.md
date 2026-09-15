---
name: lit-critic
description: Editorial review of Kohärenz-Protokoll chapter prose with lit-critic — install and projection, running the gate, and triaging its findings against project canon. Use before flipping a chapter status (drafted → revised → final), when a lit-critic report needs reading, when a finding must be accepted or rejected, or when the projection, CANON.md/STYLE.md or the blocking policy need changing.
metadata:
  category: creative-writing
  source: repo
  version: "1.0.0"
  status: active
---

# lit-critic — editorial gate for Kohärenz Protokoll

lit-critic ([lit-pack/lit-critic](https://github.com/lit-pack/lit-critic)) reads
scenes through seven editorial lenses and reports findings. It never writes
prose and never imposes generic "good writing" rules — it checks the manuscript
against **our** rules, in `tools/lit-critic/CANON.md` and
`tools/lit-critic/STYLE.md`.

It argues back. A finding is a proposal, not a verdict, and the tool is built to
hold its ground under pushback. Treat it as a demanding editor whose German is
good but whose canon knowledge is only ever as good as those two files.

## Where it sits in the gate ladder

lit-critic is the **prose-level** gate. It runs between the repo's own
deterministic checks and the agency editorial ladder:

| Order | Gate | What it decides |
|---|---|---|
| 1 | `scripts/check_enrichment.py` | did an enrichment pass only insert prose? |
| 2 | Readiness Gate (`Plan/drafting/chapter-enrichment-masterplan_2026-09-11.md` §F) | is the chapter draftable at all? |
| 3 | **`scripts/lit_critic_gate.py`** | **does the prose hold against CANON/STYLE?** |
| 4 | `novel.line_gate` / `novel.copy_gate` (agency) | graph-recorded editorial ladder |

Run it **before** flipping a chapter to `revised` or `final`, and before
`novel.set_chapter_status`. A blocked chapter does not advance.

## Setup (once per checkout)

```bash
scripts/setup_lit_critic.sh          # pinned clone + venv into .lit-critic-src/ (gitignored)
export ANTHROPIC_API_KEY=...         # or OPENAI_API_KEY
```

The pin lives in `setup_lit_critic.sh`. Bump it deliberately, then re-run
`pytest tests/` — the gate reads lit-critic's internals, so an upstream refactor
shows up there first.

## Running the gate

```bash
python3 scripts/lit_critic_gate.py --chapter 4          # one chapter, deep mode
python3 scripts/lit_critic_gate.py --chapter 1-5        # a range
python3 scripts/lit_critic_gate.py --changed            # every chapter changed vs origin/main
python3 scripts/lit_critic_gate.py --chapter 4 --mode quick     # cheaper checker tier
python3 scripts/lit_critic_gate.py --chapter 4 --report-only    # re-render, no API call
```

Exit codes: **0** pass · **1** blocking findings · **2** the gate could not run.
Exit 2 is never a pass — no key, no install and no stored analysis all land
there deliberately.

Reports go to `Plan/quality/lit-critic/kap-NN.md` (readable) and `.json`
(machine-readable). They are committed, so a chapter's editorial history is
visible in git. Each run overwrites its chapter's report.

**Blocking policy:** only `critical` findings block. `major` and `minor` are
advisory. The `horizon` lens never blocks — it names artistic roads not taken,
which is an invitation, not a defect. To change this, edit
`BLOCKING_SEVERITIES` / `NON_BLOCKING_LENSES` in `scripts/lit_critic_gate.py`
and say so in the commit message; do not silence findings case by case.

## How the manuscript reaches lit-critic

lit-critic wants one plain-text file per scene with a `@@META` Prev/Next chain;
we keep one Markdown file per chapter. `scripts/lit_critic_project.py` bridges
the two:

- prose body = everything after the chapter's own `# Kapitel N — …` heading, so
  front matter, Summary, Outline, Beats and Locks are never analysed;
- scenes = the body split at its `---` separators;
- the Prev/Next chain always spans the **whole** manuscript, even for a
  one-chapter run — a partial chain makes lit-critic report false continuity
  gaps;
- every scene records where its body came from, so a finding at scene line N is
  reported as `chapters/NN-slug.md:LINE` — the line you actually edit.

The projection is rebuilt on every gate run into `.lit-critic/` (gitignored).
It is one-way: **nothing ever writes back into the manuscript.** Inspect it with
`python3 scripts/lit_critic_project.py --check`.

## Triaging findings

Work the report top-down; blocking findings first.

For each finding, decide in this order:

1. **Is it factually right about the text?** Open the chapter at the cited line.
   If the finding misquotes or misreads the prose, reject it — say why in the
   commit or the decision log.
2. **Is it right about the canon?** Check `Canon/` and the chapter plan, not
   `tools/lit-critic/CANON.md` alone. That file is a compilation; on conflict
   `Canon/kohaerenz-protokoll_storyform-und-outline_2026-06-10.md` is normative.
3. **Is the "defect" a deliberate lock?** Much of this book looks wrong by
   generic standards and is right by ours — see the table below. A finding that
   fights a `[K]` lock is rejected, and the recurring ones belong in
   `tools/lit-critic/STYLE.md` so the tool stops raising them.
4. **Only then fix the prose.** German prose stays German; fixes follow the
   chapter plan, not the finding's phrasing.

Never resolve a canon question by inventing canon from a finding. That is a
Rule 0 situation: ask the user (`AskUserQuestion`).

### Findings that are usually wrong here

| Finding shape | Why it is usually wrong |
|---|---|
| "The narrator never explains X" | R-1/R-2: the tragic irony is never resolved, and meaning is the reader's. |
| "Whose voice is this? Label the speaker" | R-3/R-7: voice shifts are carried by syntax, lexicon and somatics — never a header or tag. |
| "This character is never described" | R-10: Juna is never subject, name, voice or body — only effect. |
| "The system's log reads coldly" | R-8: the ordering instance speaks without metaphor, moral or affect, and never says "Ich". |
| English style norms (Oxford comma, `said`-bookisms, Title Case) | The prose is German; feedback comes back in English. Judge the German. |
| "Terminology is introduced without explanation" | Act I runs on diegetic vocabulary only; DKT terms are forbidden before ~p. 50. |

### Findings that are usually right here

Continuity across chapters (a fact, term or time reference that contradicts an
earlier chapter), the heat-polarity rule (cold ozone and sourceless warmth in
one scene, R-5), concept stacking (R-6), a knowledge fence broken (a figure
knows something the reveal timeline still hides), and filter words in deep POV.

## Maintaining CANON.md and STYLE.md

`tools/lit-critic/CANON.md` and `STYLE.md` are the tool's whole picture of the
book. They are **compilations** of `Canon/` and
`Plan/drafting/drafting-brief.md`, hand-maintained and committed.

- Canon changed? Change the source under `Canon/` **first**, then pull the
  change through into the compilation. Never the other way round.
- The same false positive three times? That is a missing rule, not a bad
  finding — add it to `STYLE.md`.
- Keep them specific. "Keep the voice cold" is not checkable; "no metaphors in
  KW1, and comparisons only from Kael's own world" is.

## Changing the integration

| Task | File |
|---|---|
| bump the upstream pin | `scripts/setup_lit_critic.sh` |
| change how chapters split into scenes | `scripts/lit_critic_project.py` |
| change the blocking policy or the report | `scripts/lit_critic_gate.py` |
| the rules lit-critic checks | `tools/lit-critic/CANON.md`, `STYLE.md` |

After any change: `.lit-critic-src/.venv/bin/python -m pytest tests/`. The
projection tests verify every one of the ~230 scenes maps back to its chapter
line verbatim; a wrong offset would send the author to the wrong paragraph, so
they must stay green.

## Known limits

- **Costs money per run.** `--mode deep` runs checker + frontier tiers over
  every scene of the chapter. Use `--mode quick` while iterating.
- **Upstream v5.1.1 imports `httpx` without declaring it** — the setup script
  installs it explicitly. If a future pin fixes that, drop the extra install.
- The gate drives lit-critic's Python internals, not its REST API, because the
  documented session endpoints were removed upstream in v5 while the docs still
  describe them. Read the code, not `docs/technical/api-reference.md`.
- lit-critic's own auto-extracted knowledge (characters, terms, threads) lives
  in `.lit-critic/project/.lit-critic.db` and is disposable — delete the file to
  force a clean re-extraction.
