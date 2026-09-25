# Continuous improvement — what a model can actually do here, and in what order

*2026-09-17. Written after installing `dspy-skills`, `dspytools` and `drg-kg`
into the venvs and running each against this repository rather than reading
about it. Every number below was produced here.*

The question is „how do we use DSPy to keep improving the knowledge system".
The honest answer has two halves, and the first one is not about DSPy.

## The system already improves itself, three times, with no model

Nothing below needs an LM, and each one has already caught something:

| loop | what it corrects | evidence it works |
|---|---|---|
| `judgements.py` replay | a rule that was mechanised and quietly stopped holding | its first run found `fold()`'s docstring claiming behaviour it did not have, repeated in two other files |
| `state.py --prose` | a number in prose that the repository contradicts | found three stale claims the hour it was widened past a hardcoded three-file list |
| `selftest.py` | a checker that stopped reporting what it claims | built because nobody had ever seen `quotes.py` or `fold()` fail |

**A model added on top of a system with none of these is how the predecessor
scored 0.987 on a coverage term that could not fall.** The order matters:
deterministic loops first, and they exist.

## What blocks every model loop, stated once

**A judgement records its rule and not its evidence.** A row in
`Plan/runs/judgements.jsonl` carries `goal`, `action`, `result`, `rule` and
`mechanised_by` — and nothing about *what made the decision true*. The numbers
exist: `capture.py --count` computes the bounded and unbounded counts and lists
the inflected surfaces found. Nothing carries them into the row.

An optimizer learns from what is in the input. Train on these rows today and it
learns to produce conclusions that look like the recorded ones, from inputs that
never contained the reason. **That is the same defect as a recall term that
cannot fall, moved one step earlier.**

This is the first thing to build, and it is not a model.

## What is trainable today, and what it is worth

One task, and the numbers are live rather than written down:

```
one-term-or-two: 26 labelled examples — 13 one-term, 13 two-terms
all 26 carry a stated rule — which is GEPA feedback, not just a label
baseline (fold() equality, the rule already in the repository): 17/26 = 65%
```

**All nine misses are the same shape**: gold says one term, `fold()` says two.
Not one is a false merge. So `fold()` has **perfect precision and 65% recall**
on this set, and every miss is a plural or an inflection —
`Guardian`/`Guardians`, `Riss`/`Risse`, `Alter`/`Alters`,
`Kern-Welt`/`Kern-Welten`.

That shape decides the next move. A model that raises recall by merging more
aggressively will start merging `Negentropie` with `Entropie`, which
`selftest.py` asserts it must never do. **The canary is already in place**, which
is why this task is safe to try at all.

`drg-kg`'s scorer confirmed it independently. Feeding our own `fold()` in as the
key function to `drg.evaluation._score_sets`:

```
raw surfaces: P0.50 R0.50 F1 0.50   missed: Grenzfeste, Kern-Welt
folded:       P0.50 R0.50 F1 0.50   missed: grenzfeste, kernwelt
```

**Folding changed nothing on the plural pair.** An outside scorer reproduces the
project's own measured failure mode, which is the useful kind of confirmation.

## What is not trainable today

- **Extraction.** One usable gold candidate list exists; the other four are
  reconstructions written after the counts and `trainset.py` refuses them. Two
  or three more documents read by hand come first. There is no shortcut: the
  gold list is the one artifact a program cannot produce.
- **Conflict detection.** Four conflicts and one recorded false positive, and it
  is deliberately never mechanised — two readings can only be compared by
  reading them.

## Where each installed package actually fits

### `dspy-skills` — the skill becomes something the model holds

`SkillManager([Path(".agents/skills")])` discovers all three skills here and
lists `ingest`'s two references without loading them. `generate_skills_prompt_block`
renders the `<available_skills>` block a ReAct agent is given, and **that block
is built from the `description` field and nothing else.**

So the description is the optimisable surface, and it is optimisable *without*
any of the blockers above: the training signal is „did the agent reach for the
right skill", which needs trigger queries, not gold candidate lists.
`dspy-book-coding-agents` optimises exactly this kind of text with GEPA's
`optimize_anything`, where the candidate is the file's text and the dataset is a
handful of captured real failures.

**This is the cheapest real use of DSPy in this repository**, and it is the one
the RLM subagent prompts would benefit from.

### `dspytools` — skills as artifacts

`dspytools skills` lists, searches, compiles and auto-optimises a `SKILL.md`
directory. Pointed at `.agents/skills` it finds all three. It is the management
half of the same idea and needs Python 3.12, hence its own venv.

### `drg-kg` — a recall that can fall

DRG is a schema-driven extraction framework, and the part that matters here is
its evaluation module, not its graph.

`drg.evaluation._prf(tp, fp, fn)` returns precision, recall and F1 with explicit
zero guards. Measured:

```
empty gold, empty pred:   P0.0 R0.0 F1 0.0
empty gold, 5 predicted:  P0.0 R0.0 F1 0.0  (5 false positives)
10 gold, 0 predicted:     P0.0 R0.0 F1 0.0  (10 false negatives)
```

**It returns 0.0 where the retired pipeline's `coverage()` returned 1.0.** That
is the exact defect inverted, and it is the reason this module is worth having:
a metric that scores an empty prediction at zero cannot be optimised into
confident prose.

It also carries the pieces this corpus needs — `_build_alias_lookup` so a term's
surfaces resolve to one canonical name, and `_score_sets` reporting
`false_negative_keys` by name, which is feedback rather than a number.

**And it has one hazard, which is ours and not DRG's.** Document 5 added zero
pages *on purpose*: sixteen candidates matched nothing and none became a page,
because a brief supplies occurrences rather than readings. Under this metric
that run scores 0.0. So the scorer belongs on the **candidate list**, where
„found nothing" really is a failure, and never on the pages, where „promoted
nothing" can be the correct outcome.

### What DRG must not become here

**An inferred graph layer.** What was rejected by decision is a model *guessing*
edges — „expensive at 680 docs, and canon links must be **explicit**". Explicit
links were never the thing rejected, and the wiki has them.

*Correction, 2026-09-17.* This section first read „`Wiki/` contains zero
`[[links]]`" and treated that as a decision against linking. Both halves were
wrong. At the time the wiki linked with `` `slug` `` rather than `[[slug]]` and
had 48 such links; „no `[[…]]`" is a statement about markup and says nothing
about whether pages link. Turning „do not let a model
guess an edge" into „the wiki has no links" is exactly the delete-instead-of-
demote failure `CLAUDE.md` warns about, and it cost a recommendation: it is how
the broken-link lint family got dismissed as having nothing to check.

**It had plenty to check.** 21 of 46 pages had nothing linking to them, and
`relations.py --unmarked` found 158 places where one page wrote another page's
term in prose without marking it — more than three times the marked links.
`aegis`, the most central term in the corpus, was an orphan with its name
standing unmarked in other pages 68 times.

Decision 005 closed it. The wiki now carries 361 <!--state:wiki.relations-->
links across 93 <!--state:wiki.pages--> pages, 28 <!--state:wiki.orphans-->
orphans and 186 <!--state:wiki.unmarked--> mentions the pass may not touch,
because their first occurrence sits inside a quotation or a citation line.

So DRG's extraction and graph modules stay unused, and its evaluation module is
the part with a job — but the reason is cost and the explicit-link rule, not an
imagined ban on linking.

## The order

1. **Carry evidence into the judgement row.** `capture.py` already computes it.
   Until this exists, every model loop trains on conclusions without reasons.
2. **Optimise the skill descriptions** with `optimize_anything`, scored on
   trigger queries. No gold candidate list needed, so it is unblocked today, and
   it is what improves the initial prompt of any subagent that carries skills.
3. **Two or three more documents read by hand**, each producing a real
   `03-candidates.md`. This is the only way extraction becomes trainable.
4. **Then the n=26 ladder** for one-term-or-two: `LabeledFewShot` first, and
   nothing that fails to beat 17/26 is worth an LM call. `selftest.py`'s
   `MUST_NOT_MERGE` canary stays the gate.
5. **Then, and only then, a recall term** over candidate lists, using DRG's
   `_score_sets` with `fold()` as the key — because by then there is gold for it
   to fall against.

**Nothing in the pipeline calls any of the three packages yet.** They are
installed, reachable, and measured against this repository. That is the whole
claim this file makes.
