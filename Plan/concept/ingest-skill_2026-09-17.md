# The ingest skill — what the predecessor knew, and the one thing it could not measure

*2026-09-17. Design, not a build. Two research passes behind it: the retired
skill set under `Legacy/claude-config/`, and qmd/DSPy measured rather than
assumed. Everything below that is quoted was checked against the file.*

This project has done an ingest by hand five times. A skill should carry what
those five runs settled — and the retired pipeline had a **direct ancestor**,
`Legacy/claude-config/commands/research-ingest.md`, which got several things
right that are worth taking whole, and one thing wrong that is worth more than
all of them.

## The finding that decides the design

The retired pipeline scored its own runs. `Legacy/Plan/wiki/pilot-run_2026-09-16.md`
reports **0.987** and the probe run **0.967**, across 53 LM calls, 54 minutes and
$8.38. Those scores had five weighted axes, all deterministic, and the design
rule above them was good: *„every axis decidable without an LM, so the compiler
cannot be optimized into confident prose."*

One of the five axes was `coverage`. Its implementation, in
`Legacy/tools/kpwiki/metrics.py`:

```python
def coverage(claims: list[Claim], gold_fragments: list[str]) -> float:
    """Share of gold fragments that some predicted claim contains (1.0 without gold)."""
    if not gold_fragments:
        return 1.0
```

And the caller, `Legacy/tools/kpwiki/research_ingest_cli.py`, builds its gold
example from the run's own inputs — `sources`, `pages`, `known_entities` — and
passes **no gold fragments at all.**

**So the recall term was pinned at 1.0 and the score could not fall for missing
anything.** Both live runs measured whether the output was well-formed, legally
shaped, properly cited and still in German. Neither measured whether it *found
what a person would have found*. Verified by reading both files; the docstring
says it outright.

That is the whole reason this project's `trainset.py` refuses the four
reconstructed candidate lists and counts exactly one gold list. **An ingest skill
whose only evidence is its own well-formedness is the failure mode, not the
goal.**

### What follows for the skill

1. **Every ingest run produces a gold artifact or it produces nothing.**
   `03-candidates.md`, written while reading, before any count. `capture.py`
   already refuses to count without it. The skill inherits that refusal and must
   not weaken it.
2. **A model may never both produce and grade a candidate list.** Extraction's
   independence is what makes reconciliation safe, and a self-scored recall term
   is the same defect in a different place.
3. **The baseline is measured live, never written down.** `fold()` was 82% on 17
   examples and is 65% on 26 — the number moved because the set grew, and a
   hardcoded baseline would have hidden that.

## What transplants whole

### The German extraction contract

`Legacy/tools/kpwiki/signatures.py` states five rules for extracting cited claims
from a German document. They are the most directly reusable artifact in the
retired set:

- no citation → drop the claim
- quote verbatim from numbered lines
- **never translate a source**
- **„any term the claim itself puts in quotation marks must stand verbatim in the
  lines that claim cites"**
- do not merge two statements into one claim

The fourth is `scripts/quotes.py`'s job, arrived at independently. The third is
already `CLAUDE.md`'s rule. The first two belong in the skill verbatim.

Its companion is mechanical and cheap: `programs.py` prefixes every line `NNN| `
before the model sees it, so a citation is checkable at all. **The current
pipeline hands a model line-numbered text nowhere.** That is a gap.

### Four German-specific findings, each measured there

| finding | where |
|---|---|
| „German capitalises every noun, so do NOT grep for capitalised words" | `lint-wiki.md` |
| slugs expand umlauts `ae/oe/ue/ss` | `signatures.py` |
| a `de`/`en` detector needs a `language_unknown` escape, or names, numbers and formulas get penalised | `metrics.py` |
| typographic quote/apostrophe/dash normalisation, and **„an empty or punctuation-only fragment is a substring of everything"** | `wiki_lint_rules.py` |

The first explains why `scripts/corpus.py` „holds capitalised tokens only" is a
defect and not a design. The second is the same conclusion `dedupe.py` reached
from Unicode normalisation. The fourth is the substring trap that appeared three
times in one session here.

### The calibration measurement

`Legacy/Plan/wiki/probe-run_2026-09-16.md` reports 46 citation-resolution errors
that reduced to **6 genuinely wrong out of 150 claims** — 19 fixed by unifying
quote glyphs, 21 by stripping enclosing punctuation.

**An uncalibrated quote checker reported a model as roughly five to eight times
worse than it was.** `scripts/quotes.py` went through the same discovery
independently and now reports what it could not check rather than passing it.
The number is worth keeping because it sizes the effect.

### Test the checker, not only the model

`Legacy/tools/kpwiki/compile_fixture.py` defines `BROKEN_NEEDLES` — the exact
feedback strings a deliberately defective input must produce — and the smoke test
asserts each appears. Cheap, and this project has no equivalent: `quotes.py` and
`fold()` are both trusted without a fixture that proves they can fail.

### Two halves, two costs

`research-ingest.md` splits an ingest into a cheap per-source half and an
expensive batch half — 6 of 53 LM calls against 47 — on the invariant that
*„extraction depends on the document alone, never on the batch it arrives in."*
The current project reached the same split. The consequence it adds is worth
stating: **the census is a cache**, so re-running resumes rather than restarts.

Its routing rule is sharper still: spend the strong model only where a
cross-source disagreement is structurally possible, because *„43% of merge calls
were spent where no contradiction was possible."* Applied here: **a term
occurring in one document cannot carry a cross-document conflict.**

### A rule that is not enforced is prose

`Legacy/AGENTS.md`: *„a skill explains the tool rather than restating what it
enforces — two encodings of one rule drift. If a rule can be broken without a
check failing, it is prose, not a rule."*

This is the test every line of the ingest skill has to pass. Where the skill
states a rule, either a script enforces it or the skill says plainly that it is
a convention a person upholds.

## What the predecessor got wrong, and the evidence

Four failures, all verified against the files, all the same shape as the one
`CLAUDE.md` already names.

1. **A section declared abolished that 41 pages still carry.**
   `research-ingest.md` states *„`Where they disagree` is not a section any
   more"*, and a `Wiki/contradictions/` ledger is fully specified — in the
   command, as a complete page kind in `entities.yaml`, and as a 61-line
   template. **The directory does not exist, no code writes it, and 41 candidate
   pages on disk carry the abolished section.** This is the archetype.

2. **A rule that let a source grant itself authority.** Resolution was pending
   *„unless one source explicitly supersedes the other"*, so a document's own
   `[DEPRECATED]` claim was honoured — and the metric computed „contradicted"
   from *pending* disagreements only, so such a page would have dropped out of
   the review queue silently. The pilot report says a second disagreement kept it
   visible **by luck**. Two defects lined up and the failure was silent.
   Correction, from the same file: *„an ingest proposes, it never resolves."*

3. **Nine command names referenced that never existed as files** — including in
   `writers.yaml`, the *machine-readable* policy. A rename became unperformable
   across nine files.

4. **Vocabulary invented before any output existed.** Ten log operations
   declared, two ever written. Eight gold sets planned, zero delivered. Every
   source page busted its word budget — 4 of 4. This project's „schema follows
   the pages" is the correction, already made.

## The skill

```yaml
name: ingest            # provisional
# may not: create a wiki page, resolve a conflict, grade its own candidate list,
#          or let any number come from a search result
# retire when: three documents run through it with no correction needed
```

One skill, one document, ending at a reconciled state a person can review. It
wraps the existing scripts rather than replacing them.

| step | command | what the skill adds |
|---|---|---|
| open the run | `capture.py <slug>` | reads `01-profile.txt` before forming an impression — the profile changes the shape of the extraction |
| read the briefing | `Plan/briefings/extract.md` | procedural knowledge only; never document knowledge |
| read the document | line-numbered | **new: hand the reader `NNN| ` prefixed text**, so every citation is checkable as it is written |
| write candidates | `03-candidates.md` | the refusal: no counting before the list exists |
| count | `capture.py --count` | two numbers per term, and the inflected surfaces found |
| census | `Sources/terms/<slug>.md` | describes one document and nothing else |
| note | `Sources/notes/<slug>.md` | every quotation `^[Lnn]`, then `quotes.py` on the file |
| reconcile | `reconcile.py <slug>` | judgements to the ledger with a rule stated in words |
| record | `reconcile.json` + `Wiki/compare/` | `state_before`/`state_after`, so `account.py order` can check it |

**Where qmd belongs: orientation only, and only `search`.** Measured, after
embeddings completed — `search` is 0.22s and `query` is **2m41s**, and
`CLAUDE.md`'s rule stands: a search result is a place to look and never a number
in a page.

*Correction, 2026-09-17.* This paragraph first read „`query` is 14.5s uncached,
0 of 464 documents are embedded". Both halves were wrong together: the 14.5s was
measured against a corpus with **zero** embeddings, so it timed the fallback
rather than the feature. With 8,673 vectors built the same command takes 2m41s —
eleven times slower — which reverses the recommendation the number was supporting.

**Where qmd must not be called:** reconciliation, which reads `Wiki/index.json`
and must stay `O(census) + O(judgement)`; and any loop, because of the 2m41s.

## What the repo survey still offers, and what it does not

`Legacy/Plan/wiki/repo-survey_2026-09-15.md` catalogued nine tool repositories
before this project restarted. Re-read against what now exists, most of its
catalogue is either built here in a stronger form — content-hash dedup and
near-duplicate clustering, line-scoped citations validated deterministically,
staged candidates, a free deterministic check tier, a trace per run — or was
rejected on purpose. Three entries are not, and each is ingest's business.

**Evidence graded on every decision, and LOW refused by default.** DeepRefine
scores each proposed action HIGH (exact evidence) / MEDIUM (inferred) / LOW
(ambiguous) and refuses LOW without approval. A row in
`Plan/runs/judgements.jsonl` already carries `goal`, `action`, `result`, `rule`
and `mechanised_by` — everything except **what made the decision true**. The
numbers exist: `capture.py` computes the word and compound counts and lists the
surfaces found. Nothing carries them into the row, so the evidence of every
judgement is prose in a note. This is the same gap that blocks a model — an
optimizer learns from what is in the input — and the survey supplies the
vocabulary for closing it.

**`truncated` is a field nobody measures.** The manifest carries `truncated` on
every row and it reads `false` for all 346 <!--state:sources.landed--> landed documents. No script in
`scripts/` mentions the word; the value came in with the Drive index and has
never been derived. A field that asserts „this export is complete" without
anything having checked is worse than no field. The cheap heuristic does not
rescue it either, and that is measured: **221 of the 346 <!--state:sources.landed--> documents end without
terminal punctuation**, because they end on a bibliography URL. So it is
demoted rather than deleted — the survey's idea is right and our value is not
evidence.

```yaml
truncated: false     # provisional — carried in from the Drive index, never derived
                     # may not: be cited as evidence that an export is complete
                     # retire when: `sources.py land` derives it, or 20 documents
                     #              show nothing downstream ever reads it
```

**Active-page protection.** A reviewed page is never overwritten by a new
source; a conflicting source flags it instead. It costs nothing today, because
`Wiki/terms/` does not exist and nothing has been promoted — which is exactly
why it has to be decided before the first promotion rather than discovered
after it.

One entry stays rejected, with a measurement rather than an argument.
**Two-phase compile** — extract the whole batch, then merge across it — is the
shape reconciliation was deliberately moved away from: cost per document is
`O(census) + O(judgement)`, not `O(corpus)`.

*Correction, 2026-09-17.* A second entry was listed here as rejected and should
not have been. This paragraph read „the **broken-wikilink lint family** has
nothing to check: `Wiki/` contains zero `[[links]]`". The wiki links with
`` `slug` `` instead of `[[slug]]`, and it has 48 <!--state:wiki.relations-->
such links, 21 <!--state:wiki.orphans--> orphans and
158 <!--state:wiki.unmarked--> mentions the markup does not mark. The lint
family has work; what the survey rejected was a model *inferring* edges, and it
said in the same line that canon links must be **explicit**.

## What is not yet possible, stated plainly

- **Extraction is not trainable.** One usable gold candidate list exists. Two or
  three more hand-read documents come first, and the skill's job until then is to
  produce them, not to be optimised.
- **No train/validation/canary split exists** for the 26 fold-pairs that *are*
  usable. One is needed before any optimizer touches the ledger.
- **A judgement records its rule and not its evidence.** Until it does, a model
  trained on the ledger is trained on the conclusion alone.

## The order

1. ~~The `BROKEN_NEEDLES`-style fixtures for `quotes.py` and `fold()`.~~ Built:
   `scripts/selftest.py`, 13 cases, each asserting *which* defect is named.
2. ~~Line-numbered text into the reading step.~~ Built: `scripts/read.py`, and
   with the reverse direction the predecessor did not have — `--find` answers a
   quote with its citation, or refuses and names the nearest line.
3. The skill itself, drafted against `skill-creator`, which runs it against a
   **baseline without the skill** and grades both — the same discipline this
   project already applies to `fold()`.
4. Two more documents through it by hand.
5. Only then: a split, a metric, and a model.
