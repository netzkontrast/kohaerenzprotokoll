# Trainsets, splits, and where data leaks

This file is about the rows a program is trained and scored on: where this
repository's one trainset comes from, what a `dspy.Example` may and may not
carry, how it is split, and the leaks nine repositories shipped and this one's
own construction avoids by not doing the thing that leaked. `with_inputs` and
`Example`/`Prediction` signature facts already stated in `api.md` are pointed to,
not repeated.

## In this repository

**The judgement ledger is the trainset, and it was not built to be one.**
`Plan/runs/judgements.jsonl` holds 68 <!--state:judgements.total--> records,
written "to keep mechanised rules checkable"
(`scripts/judgements.py`). Each record already carries the two surfaces,
a decision, and — the part that makes it a dataset — `rule`, the person's own
sentence for why. A real record, cut to the fields used here:

```json
{"id": "J4", "surfaces": ["Kern-Welten", "Kern-Welt"], "decision": "one-term",
 "rule": "a German plural ending is not a term boundary",
 "mechanised_by": null, "document": "guardians-und-kern-welten-konzept"}
```

(`Plan/runs/judgements.jsonl`, record J4). `trainset.py`'s own framing: "GEPA's
entry in the optimizer table does not ask for a number of examples — it asks
that 'failures can be described in words, not just scored'. This ledger was
already written that way, for a different reason." (`scripts/trainset.py`).
`surface_pairs()` reads every `records()` entry whose decision is
`one-term`/`two-terms` and whose `surfaces` has exactly two entries, and returns
`{id, first, second, document, decision, rule, features}` per row
(`scripts/trainset.py`).

**`trainset.py --export` writes a file, and `pairs.py` does not read it.**
`Plan/trainsets/surface-pairs.jsonl` is a snapshot of the ledger from the last
time the export ran: the committed one holds 36 rows while the ledger yields
57 <!--state:pairs.labelled-->. `pairs.py rows()` calls `trainset.surface_pairs()` directly
(`scripts/pairs.py`), never the export. This is deliberate, and it is a
correction of a real defect: "The design says job 1 has 'n = 26' … The exported
file had gone stale because nothing compared it to the ledger; `pairs.py` now
reads the ledger live and never the export."
(`Plan/concept/dspy-toolchain_2026-09-23.md`, *Status*). The export exists for
inspection and for anything outside this repository that wants a flat file; it
is never the thing scored.

**Gold candidate lists are written while reading, before any count.**
`Plan/runs/<slug>/03-candidates.md` is the artifact `capture.py` refuses to let
anything count against before it exists — "counting first decides what gets
seen" (`CLAUDE.md`, *Every step keeps its artifact*). `capture.candidate_terms()`
reads only the `- term` lines out of it, deliberately excluding prose bullets
such as an "open while reading" section, because those scored 0 occurrences and
looked exactly like a term the document did not contain
(`scripts/capture.py`). This is what `rlm_ingest.py score()` and
`entities.py cmd_score()` both score a model's list against.

**A reconstruction is refused as gold, in two different scripts.** `rlm_ingest.py`
writes `03-candidates-rlm.md`, never `03-candidates.md`: "the gold list is
written by a reader while reading; a model's list is the thing gold is used to
score, and the two must never be able to become each other"
(`scripts/rlm_ingest.py`). `entities.py cmd_score()` reads the first
section of a `03-candidates.md` file and refuses it outright if it contains the
word "Reconstructed":

```python
if "Reconstructed" in gold_text.split("\n## ")[0]:
    print(f"{slug}'s list is a reconstruction and cannot serve as gold")
    return 1
```

(`scripts/entities.py`). `trainset.blocked()` reports the same refusal
at the level of a whole task: as of the first four documents, every candidate
list was "a reconstruction written after the counts, not while reading …
`capture.py` refuses to count before a list exists, so document 5 onward can
produce real ones — these cannot"
(`scripts/trainset.py`; `CLAUDE.md`, *Every step keeps its artifact*).

## Examples

**`with_inputs` is the one place a program's inputs are declared** — `api.md`
has the general rule and the `Prediction` truthiness consequence. Concretely:
`pairs.py run()` builds `dspy.Example(**r).with_inputs("first", "second")` from
each trainset row (`scripts/pairs.py`). `first` and `second` — the two
surfaces — are what `SameTerm` receives; `decision`, `rule`, `document`, `id`
and `features` stay labels, read only by the metric through
`example.toDict()` (`scripts/pairs.py`).

**What leaks.** Nothing here leaks by the usual route — a label left inside
`with_inputs` — because `with_inputs("first", "second")` never names `decision`
or `rule`. The leak this repository's split avoids is a different one, shown by
`dspy-auto-gepa`: its metric-writing model is handed
`sample_rows_json=json.dumps(sample_rows[:5], …)`, and the rows passed are the
unsplit `task_rows`, so the first five can include test rows
(`dspy-auto-gepa:src/dspy_auto_gepa/metric_builder.py:229-233,296-301`,
`dspy-auto-gepa:src/dspy_auto_gepa/runner.py:225-231`) — a
metric-writing model can see rows the trainset/valset split was supposed to
hide from it. `pairs.py folds()` takes folds out of `surface_pairs()`'s full
list and holds each one out only for its own score; nothing here writes a
prompt from unsplit rows.

**What starves.** A field left out of `with_inputs` is unavailable to the
program, and here that is deliberate: `document` and `features`
(`env_features` — `near-match:index`, `german-plural`, and similar tags on each
judgement record) sit in every trainset row and are never passed to `SameTerm`.
The model decides from the two bare surfaces, the same information a person has
before opening the source document. This matches the shape of the task itself —
"one term or two?" asked of a pair — not a bug in the conversion.

## Splits and folds

**Stratified, seeded by id, never shuffled.**

```python
def folds(labelled: list[dict], k: int) -> list[list[dict]]:
    """Stratified by decision, deterministic by id: the same rows, the same folds."""
    out: list[list[dict]] = [[] for _ in range(k)]
    for decision in trainset.DECIDED:
        group = sorted((r for r in labelled if r["decision"] == decision),
                       key=lambda r: baseline.digest(r["id"]))
        for i, r in enumerate(group):
            out[i % k].append(r)
    return [f for f in out if f]
```

(`scripts/pairs.py`). `baseline.digest()` is `sha256(json.dumps(parts,
sort_keys=True))[:12]` (`scripts/baseline.py`) — a stable hash of the id,
not a shuffle a person could game by reordering the ledger, and "the same rows,
the same folds" on every run (`scripts/pairs.py`). Each fold is compiled
against `program.deepcopy()`, trained on every *other* fold's rows, and scored
only on its own held-out rows (`scripts/pairs.py`). Grouping by
`decision` before hashing means a small fold still holds both `one-term` and
`two-terms` rows, never all of one class.

**Canaries are pinned to evaluation by never being in the pool at all.**
`selftest.MUST_NOT_MERGE`'s four pairs are not `judgements.jsonl` records — they
are hard-coded in `scripts/selftest.py`, so `surface_pairs()` never returns them
and `folds()` never places one in any fold. They are checked once, after every
fold is scored, against the program compiled on the *full* 57
<!--state:pairs.labelled--> rows (`scripts/pairs.py`). This is stronger
than "held out of training" — a book-style seeded split can still put a canary
in the training set by chance; here it is structurally impossible.

**The sizes the book assumes, and why 57 does not fit them.**
"20–50 examples is enough for GEPA's reflective loop; 100–500 for MIPROv2-style
bootstrapping." "Representativeness beats size. Include edge cases, ambiguity,
adversarial inputs."
(`dspy-agent-skills:skills/dspy-evaluation-harness/SKILL.md:74-77`).
This repository's largest trainset is 57 <!--state:pairs.labelled--> labelled
pairs — inside the GEPA floor, barely, and well under MIPROv2's. `pairs.py`'s
five-fold default leaves 45–47 rows to train each fold and 10–12 to score it
(measured 2026-09-24) — thin by the book's own numbers, which is exactly why `SIMBA`'s
`bsize` is overridden per fold to `min(train_size, 16)` rather than left at its
default of 32 (`scripts/pairs.py`; `api.md` has the DSPy-level assertion
this avoids).

**Optimizers pick their own split when none is given, and each picks
differently** — re-verified here against the installed 3.3.1 package: GEPA with
no `valset` sets `valset = valset or trainset`
(`dspy:teleprompt/gepa/gepa.py:571`); MIPROv2 with no `valset` takes
`valset_size = min(1000, max(1, int(len(trainset) * 0.80)))` off the end
(`dspy:teleprompt/mipro_optimizer_v2.py:326`); `BetterTogether`'s default
`valset_ratio` is `0.1`, taken off the *front* of the trainset when no `valset`
is passed (`dspy:teleprompt/bettertogether.py:206,320-345`); `InferRules`
splits `int(0.5 * len(trainset))`, unshuffled, first half for rule induction and
second half to select among the candidate rules
(`dspy:teleprompt/infer_rules.py:25`). None of these shuffles. This is exactly why `pairs.py` never lets an
optimizer choose its own valset: every fold handed to `.compile()` is explicit,
from `folds()`, above.

**A positional split degrades silently where this repository's refuses
silently to be silent.** `dspydantic`'s optimizer split is `split_idx =
max(1, int(len(trainset) * 0.8))`, no shuffle, no stratification; below a
minimum it emits a `UserWarning` and reuses the training set as the validation
set — "scores may be inflated"
(`dspydantic:src/dspydantic/optimizer.py:1738-1751`). Measured sizes (train/val):
n=1 → 1/1 (the *same* example both ways), n=2 → 1/1, n=5 → 4/1, n=57 → 45/12
(`dspydantic:src/dspydantic/optimizer.py:1738-1751`, verified: V/v_run.py). At
n≤20 each accept/reject decision in that repository's optimizer runs on 1–4
validation examples, with no repeats and no significance test
(`dspydantic`, DATA and TRAP; see `metrics.md`, judges). `pairs.py folds()`
never falls back to reusing a fold as its own held-out set: `[f for f in out if
f]` drops only genuinely empty folds, and every non-empty fold is scored on
rows that fold never trained on.

## Difficulty tiers and hard negatives

**The canary set doubles as this repository's hard-negative set** — see
*Splits and folds*, above; not repeated here (P6).

**`fold()`'s own boundary is discovered, not designed.** `trainset.py`'s
docstring names the three actual misses precisely: `J4`, `Kern-Welten` /
`Kern-Welt` — "folding is deliberately not stemming; a stemmer aggressive
enough to merge a plural also merges `Negentropie` with `Entropie`"; `J6`,
`J14`, a slash inside a heading, for which "no rule exists"
(`scripts/trainset.py`). "So the 18% gap is the boundary of what a safe
deterministic rule can claim, not a defect in it." **That sentence is stale as
a number, current as a shape.** It was written when the ledger held 17 rows
(14/17 = 82%); `fold()` now decides 33 <!--state:pairs.fold_correct--> of
57 <!--state:pairs.labelled-->, and the docstring dates its first number and
points at the live one. The one growth step measured at the time, 17 rows to
26, kept the *shape* of every new miss the same: "Every new miss is a plural or
an inflection — `Guardian`/`Guardians`, `Riss`/`Risse`, `Alter`/`Alters`,
`AEGIS`/`Rest-AEGIS`. `fold()` strips the German definite article and does
nothing else." (`NOW.md`). Read one by one at 57 rows (2026-09-24), the
direction still holds and the kinds have widened: all 24 misses are pairs the
person called one term and `fold()` kept apart, never the reverse; eight are
plurals or inflections, and the rest are slashes (four), renames (four), a
prefix or modifier (two), reordered paraphrases (two), a numbered instance, an
abbreviation and an acronym's expansion (three), and one synonym.
`python3 scripts/trainset.py` prints each. This is a *found* difficulty
tier, in contrast with the book's *designed* three tiers — clear (baseline
should pass), boundary (might fail), ambiguous (hard for any model), with
ambiguous cases logged separately as `needs_clarification` rather than forced
into a label because "they tell you where the task definition itself is
incomplete"
(`dspy-agent-skills:skills/dspy-book-datasets/SKILL.md:47-61`,
`reference.md:44-53`). This repository's own analogue of that separate log is a
document that adds no wiki pages on purpose: a brief with "163 hedging words in
13,947" produced sixteen candidates that matched no page, and none became one
— "a page created from an occurrence says nothing and looks like it says
something" (`CLAUDE.md`, *State*). An ambiguous case here becomes a recorded
non-decision, never a forced row in a trainset.

**A tiering recipe to avoid, if demo selection is ever built for `pairs.py`.**
`dspy-advanced-prompting`'s few-shot tiers (GOLD/SILVER/BRONZE/CHALLENGING)
select up to `max_examples` by a fixed priority order and never read the actual
input: two different `input_text` values select the identical demo list,
`['challenging', 'challenging', 'gold', 'gold', 'gold']`
(`dspy-advanced-prompting:src/techniques/few_shot.py:16-20,42-47,78-107`,
verified: probe S3 — demos land in an *input field*, not `predictor.demos`,
so no DSPy optimizer can see, select or replace them either). The part worth
taking is the tiering *policy*, not this implementation: choose demos by the
input, and put them in `predictor.demos`, not in prompt text.

**Hard negatives by design, catalogued, not built.** `dspy-agent-skills`'
tetraframe pattern includes seeds whose answer is genuinely *neither*, "so the
optimizer does not learn that every debate has a winner"
(`dspy-agent-skills:skills/dspy-tetraframe/SKILL.md:168-173`); its deep-refine
pattern includes golds with `answerable_at_hop0 == False`
(`dspy-agent-skills:skills/dspy-deep-refine/SKILL.md:128-130,147-148`). Neither pattern
is built here; the canary set is the one hard-negative mechanism this
repository actually has.

## Error notes as feedback

**The book's recipe is this repository's `rule` field, independently arrived
at.** "Each error gets annotated with what the model predicted, what was
correct, and why it went wrong as a mechanism", so that "the dataset ships the
diagnosis, not just the label"
(`dspy-agent-skills:skills/dspy-book-datasets/SKILL.md:63-71`,
`dspy-agent-skills:skills/dspy-book-eight-steps/reference.md:31`). Every `rule` in `Plan/runs/judgements.jsonl` is exactly
this — not "one-term" but *why*: `"a German plural ending is not a term
boundary"` (J4), `"a slash inside a heading is an alias or a role, never a term
boundary"` (J14). `trainset.score_one`'s feedback string on a miss reads this
field back verbatim (*In this repository*, above) — the same channel the
calibration protocol in `metrics.md` (*Judges*) asks a judge-label pass to build, already built here for a
different reason before either recipe was read.

**Corrections as trainset rows, the pattern `judgements.jsonl` already
matches.** `dspy-agent-skills`'s reflect-loop pattern: "HIGH correction with a failing
input" → "`dspy.Example(inputs…, expected_behavior, forbidden_behavior,
feedback)` appended to the program's trainset"
(`dspy-agent-skills:skills/dspy-reflect-loop/reference.md:103-110`).
`Plan/runs/judgements.jsonl` rows becoming `pairs.py`'s labelled pairs is this
same shape, with one difference worth stating rather than glossing over: a
"correction" implies an earlier model answer being corrected, and nothing here
has run a model against these pairs yet — every row is a person's first-pass
judgement, not a correction to a prior wrong one.

## Synthetic data and enrichment (and why not here)

**What the nine repositories do.** `dspy-agent-skills`'s `FactGeneration`
example has "no quality filter, no validation pass and no anti-collapse check"
and draws its diversity only from a random seed string and `temperature=1`
(`dspy-agent-skills:skills/dspy-book-datasets/SKILL.md:102-103`,
`dspy-agent-skills:skills/dspy-book-datasets/reference.md:77-97`) — synthetic
data from the model being optimized carries its own biases into its own
training set. The same skill's *enrichment* pattern is the stated guard against
exactly that: when real outputs exist but inputs do not, synthesize only the
missing input from the known output, never the reverse — "a real joke with a
synthesized topic is far better training data than a synthesized joke"
(`dspy-agent-skills:skills/dspy-book-datasets/SKILL.md:109-112`,
`reference.md:99-110`). `dspy-auto-gepa`'s `AutoData` is a full synthetic
generator with three generation paths (targeted, split, signature); none of its
paths reject a low-judge-score row — the judge never rejects a row
(`dspy-auto-gepa:src/dspy_auto_gepa/generator.py:1193-1227,1399-1403`;
`Plan/concept/dspy-extract_2026-09-24/auto-gepa.md`) — and six
of its config flags (`validators_enabled`, `diversity_enabled`,
`rejection_sampling_enabled`, `balance_tolerance`, `oversample_factor`,
`diversity_threshold`'s range check aside) are read nowhere in the package
(`dspy-auto-gepa:src/`, verified: grep).

**Why not here.** Nothing in this repository generates wiki or judgement
content synthetically. Every row of `pairs.py`'s trainset traces to a person's
decision in `Plan/runs/judgements.jsonl`; every document behind `Sources/terms/`
and `Sources/notes/` traces to a `drive_id` in `Sources/manifest.jsonl`
(`CLAUDE.md`, *Two layers*). The corpus-text approval gate applies to
generation the same way it applies to judgement — „Korpustext an OpenRouter
oder TypeSafe braucht jeweils eine eigene Zustimmung des Autors" (`GOAL.md`,
rule 13) — and no run has asked for synthetic generation. The nearest thing to enrichment this repository has is
`scripts/bilingual.py`'s gloss proposals in `Plan/runs/bilingual/stated.jsonl`
— code finds glosses the corpus already writes, Jev judges which surfaces are
entities, a free model proposes an English counterpart from the German name
alone — and it is explicitly outside the trainset boundary: "It is a list of
proposals: no pair has become a judgement" (`CLAUDE.md`, *Entity lists*). Entity
lists themselves are barred from becoming gold the same way (`entities.py`'s
docstring, quoted in *Not taken*, `metrics.md`).

## Leakage guards and the fixes the nine repositories needed

**The most detailed leakage postmortem across all nine notes is one commit,
`dspydantic`'s `1afc528`, fixing four leaks at once.** Quoted in full because
each is a distinct shape: "(1) `_optimize_single_field` always leaked
validation data: `val_single` was always identical to `train_single` due to an
off-by-one in the guard condition after slicing … (2) Empty validation set
silently fell back to training data …, now emits `warnings.warn()`; (3)
`_optimize_prompt`'s metric evaluated candidates with the original field
descriptions instead of Phase 1's optimized ones; (4) Baseline evaluated
WITHOUT few-shot demos while all subsequent evaluations included up to 8 demos
— the 89% to 100% jump was from demos alone, not description optimization."
(`dspydantic:src/dspydantic/optimizer.py`, commit message quoted in the reader's
note; `git show 1afc528`).

**A valset that is the same object as the test set, at small n.**
`dspy-auto-gepa`'s `Datasets(train=train, val=val or test, test=test)` means
GEPA's Pareto-selection valset and the score `compare()` reports on are
literally `ds.val is ds.test → True` whenever no explicit `val` is given and
the split leaves one row per side — which the repository's own README
quickstart does, at n=2
(`dspy-auto-gepa:src/dspy_auto_gepa/runner.py:242-246`; `README.md`,
verified). The article-level version of the same trap: "The committed scores
are GEPA's own cached full-valset evaluations (used for candidate selection)",
the number the optimizers chapter says not to report ("Report the held-out
number.", `dspy-agent-skills:skills/dspy-book-optimizers/SKILL.md:67`) — the
invoice example's own committed
`results.json` records that its genuinely fresh re-evaluation "could not
complete"
(`dspy-agent-skills:articles/03-inside-the-examples.md:112`;
`skills/dspy-book-optimizers/SKILL.md:65-67`; `examples/03-invoice-extraction/results.json`).

**Row order decides the split.** The `dspy-agents` reader named the
consequence: "Appending new domains at the end of the file sends them all to
MIPROv2's valset" (`Plan/concept/dspy-extract_2026-09-24/agents-rag.md`, on `dspy-agents`' own
`compile_rag.py`, which loads a JSONL in file order with no shuffle) — the reason is MIPROv2's own default
behaviour, verified above: `valset = trainset[cutoff:]` takes the *last* 80% of
whatever order the caller handed it, keeping only the first 20% to train on
(`dspy:teleprompt/mipro_optimizer_v2.py:326`). A dataset that grows by
appending silently reshapes its own valset. `pairs.py folds()` refuses that
part: the hash key is the row's own `id`, not its position, so appended
judgements are dealt across every fold instead of piling into one. It does not
keep folds stable as the ledger grows. `folds()` deals round-robin over hash
order, so a new row shifts every row that sorts after it: one appended
judgement moved 15 of 57 rows to another fold (measured 2026-09-24). Two runs
at different ledger sizes trained on different partitions, which is one more
reason `baseline.compare` will not compare across a changed trainset hash
until the floor is re-scored.

**A leakage guard as a regression test, not only a stated rule.** The book's
invoice benchmark asserts, as `unittest`, that train and holdout are disjoint
by id and that each approach draws its six predictions only from holdout ids —
"That is a leakage guard."
(`dspy-agent-skills:skills/dspy-book-use-cases/SKILL.md:39-55`,
`reference.md:57-63`). `judgements.py`'s replay (`agrees` / `DISAGREES` /
`judgement`) is this repository's version of the same discipline generalised
past leakage specifically: an invariant that is re-verified on every run rather
than asserted once and trusted (`scripts/judgements.py`).

**What this repository's own construction already prevents, by mechanism
rather than by rule.** Fold membership by id-hash, so a judgement's position in
the file never decides its fold; canaries excluded from the labelled pool
entirely, not merely held out of a split; `pairs.py` reading the ledger live so
a cached export can never silently diverge from what a judgement replay checks
against (*In this repository*, above); `entities.py score` refusing a "gold"
file that says "Reconstructed" of itself; and `rlm_ingest.py` writing its own
list under a name the gold list never has. None of these is
copied from a nine-repository pattern — each is this repository's own answer to
a leak one of the nine had.

## Not taken

- **`MIPROv2`, `BootstrapFewShotWithRandomSearch`** — refused. They want
  100+ and 50+ examples; this repository's largest trainset is 57
  <!--state:pairs.labelled--> pairs. `dspy-agents` ran MIPROv2 on 50 examples
  while its own documentation said about 28
  (`Plan/concept/dspy-toolchain_2026-09-23.md`, *Deliberately not taken*).
- **Synthetic data generation of any kind** — refused (`AutoData`-style,
  `FactGeneration`-style, or otherwise). Every row must trace to a person's
  judgement or a landed source document; see *Synthetic data*, above.
- **`KNNFewShot`** — refused for job 1 originally ("needs a `dspy.Embedder`"),
  and reopened as a possibility rather than closed: "qmd now has a local
  embedding model, so this becomes cheap if step 0–2 disappoint"
  (`Plan/concept/optimizers-and-data_2026-09-17.md`, quoted in
  `Plan/concept/dspy-toolchain_2026-09-23.md`). The one item here closer to
  *waiting* than *refused*.
- **A model-proposed edge or gloss entering the trainset or the wiki as data**
  — refused structurally, not by policy alone. The bilingual gloss proposals
  and the entity lists both sit in a layer the graph and the census read never
  read from directly: "Beside the graph, never in it: the proposal layer"
  (`CLAUDE.md`, *The knowledge graph*).
