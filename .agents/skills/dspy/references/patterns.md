# Patterns built on DSPy, mapped onto this repository

Fourteen patterns built on DSPy, from eight of the nine repositories,
organised by what they are *for* rather than by which repository
wrote them. `api.md` has the DSPy facts these patterns lean on; `optimizers.md`
has GEPA/MIPROv2/SIMBA mechanics; `text-artifacts.md` has `gepa.optimize_anything`
in full — this file points there rather than repeating them.

Every pattern is held against this repository's own rules, not against DSPy in
general: **conflict detection is never mechanised** (`CLAUDE.md`, "Conflict
detection is never mechanised. Two readings can only be compared by reading
them, and a program that guessed would reproduce the `Zero-Trust` false
conflict"); **a link is never inferred** (`Plan/decisions/005-the-wiki-links.md`);
**a term page collects every source's reading of one term, attributed and
unmerged** (`CLAUDE.md`, P13); **a source granting itself authority is recorded,
not applied** (`Plan/decisions/006-every-draft-is-back-in-question.md`); and
**a reviewed page has no rule yet** — nothing has been promoted, so the one case
`dspy-wiki-compile` answers (flag a conflict with a promoted page, never update
in place) has no instance here (`NOW.md`, "A reviewed page has no rule yet";
`Plan/concept/wiki-compile-second-opinion_2026-09-17.md`). P1, P12–P15 and P26
of `PRINCIPLES.md` are cited inline throughout rather than restated here.

One repository is absent from this file on purpose: `dspy-auto-gepa` belongs
to `optimizers.md`, `metrics.md` and `data.md`, as the RLM and RAG halves of
`dspy-agent-skills` belong to `rlm.md` and `retrieval.md`. `repos.md` has commits and versions.

## What was taken, waits, or was refused — at a glance

| pattern | source | what it does | verdict here |
|---|---|---|---|
| Compile sources into a cited wiki (six typed stages, a weighted metric) | `dspy-wiki-compile` | triage → extract → merge → decide → diff → answer, each a `ChainOfThought`, `RULE 1–3` deciding `flag`/`update`/`create` by lookup | shape independently converged with decisions 003/005/006 (below); *merge*'s one-definition-per-concept is refused (breaks P13); *decide*'s legality gate is the unbuilt reviewed-page rule; *diff* and citation-checking are kept, stricter, as `Wiki/compare/` and `quotes.py` |
| A second model reviews, never rewrites | `dspy-adversarial-review` | independent-LM guard, F1 judge metric, `dspy.Refine` around the writer | recipe catalogued for a second Jev/TypeSafe opinion on a near match; may only direct attention (P0); its `Refine` wiring is a trap, not a recipe (below) |
| Precision by asking, not guessing | `dspy-clarify` | rewrite → scope/assumptions/questions/verdict (`clear`/`needs-author`/`not-promotable`) | its verdict taxonomy maps onto `NOW.md` questions and conflict records; the rewrite step itself is refused — pages quote (P12), a model never types an identifier (P26) |
| Four isolated corners on a contested claim | `dspy-tetraframe` | P / not-P / both / neither, mapped, transformed, with an eight-check verification suite | shape catalogued for a conflict this contested — `Wiki/conflicts/` already carries P/not-P attributed; its scored suite is refused outright (rewards counting contradictions) |
| Keep a program run honest | `dspy-autodialectics` | immutable contract → thesis/antithesis/synthesis → deterministic verify → slop score → champion/challenger gate | canary-veto-plus-floor is already built, stricter, in `scripts/baseline.py` and `scripts/pairs.py`; its `Verify` trusting the optimized program's own report is the trap to avoid |
| Repair a knowledge base from an unanswerable question | `dspy-deep-refine` | judge answerable → abduce → propose graph edits → apply only after review and explicit approval | the loop's three axes map onto `Wiki/questions/`, `Wiki/conflicts/` and `Plan/runs/judgements.jsonl`; its *actions* (`insert_edge`/`replace_node`/`delete_edge`) are refused outright — an inferred edge breaks decision 005, a merge breaks P13 |
| Turn a correction into a gold example | `dspy-reflect-loop` | signal extraction, a fingerprinted ledger, promotion after ≥ 2 contexts and a human | `Plan/runs/judgements.jsonl` plus `scripts/judgements.py` already do this by identity rather than substring; nothing here extracts a signal from a transcript without the author's yes (P0) |
| Multi-turn state as a typed wrapper | `dspy-session` | `Session`/`Turn`/`History`, `with_memory`, "Push, Don't Peek" | nothing here is a multi-turn agent; the frozen-`Turn` shape is the pattern `lmrun.py`'s per-call record already follows; wrapping `dspy.RLM` in a session is refused explicitly (`Plan/concept/dspy-toolchain_2026-09-23.md`, "Never wraps `dspy.RLM` in a `History`-carrying session") |
| Tool-using agents, MCP, subagents | `dspy-agents`, `Agentic-Dspy-Rag`, `dspy-book-agents` | Agno-wrapped DSPy tools; MCP lifecycle; classify → route → retrieve → rerank → generate | the baseline store's shape is kept, fixed to a floor plus veto, in `scripts/baseline.py`; classify-then-quote is catalogued for `ask`, waiting on `ask` existing at all (`graphrag.py`); substring routing on free text is the anti-pattern `pairs.py`'s `Literal` decision already avoids |
| A model's plan as a checked graph | `braid-dspy` | one `Predict` writes a Mermaid flowchart, code parses and Kahn-orders it, a second `Predict` executes node by node | catalogued as "a procedure as a checked graph"; waits for a procedure whose order is in dispute — `scripts/account.py`'s decompositions are the named candidate (`Plan/concept/dspy-toolchain_2026-09-23.md`) |
| Critique → repair a text artifact | `dspy-optimizer` | Evaluator → Refiner → Merger → Validator patches a `### Block`-structured prompt string | `MockLLM` and the callback shape are kept; the loop itself is refused — job 4 uses `gepa.optimize_anything` (`text-artifacts.md`), which rewrites the whole file under a metric instead of patching named blocks by an unheld-out validator |
| Eleven "techniques used by top AI startups" | `dspy-advanced-prompting` | long instruction text as an **input field** around a `ChainOfThought`, per technique | ten of eleven are prompt text with no DSPy leverage at all; only hard-negative demo tiering is a mechanism, and `pairs.py`'s canary pairs already are that mechanism |
| Schema as prompt: optimize a field description, score the downstream extraction | `dspydantic` | a rewriter `ChainOfThought`, scored by plugging its output into a separate extraction call | the shape is job 4's shape exactly (`text-artifacts.md`); the evaluator registry and n-based optimizer choice are catalogued, every specific number is left behind |
| Seven applications by task shape; a checked build loop | `dspy-book-use-cases`, `dspy-advanced-workflow`, `dspy-context-engineering-book` | gold-answer / no-gold / lookup / arithmetic routing; baseline-before-optimizer; routers as functions | mirrors this repository's own layered toolchain and `scripts/entities.py`/qmd's collection routing; shipping honest failures and reading a GEPA result's diff before accepting it are taken as working method, not code |

---

## Wiki compile and knowledge diffs

**Mechanism.** `dspy-wiki-compile` runs six `ChainOfThought` stages over
pydantic-typed signatures: `TriageSource → Triage{tier, category, language,
truncated}`; `ExtractClaims → list[Claim{text, citation: Citation{file, start,
end, quote}, kind, entities}]`; `MergeConcepts(extractions, known_entities) →
list[ConceptDraft{slug, definition, sources, citations, disagreements:
list[Disagreement{topic, sources, positions, resolution="pending"}], status}]`
over the *whole batch*; `DecideIngest(page, concept) → IngestDecision{slug,
action, rationale, conflicts}`; `KnowledgeDiff(page, concept) → Diff{reinforced,
challenged, new, gaps}`; `AnswerQuery(question, pages) → Answer` (cite pages as
`[[slug]]`, name gaps)
(`dspy-agent-skills:skills/dspy-wiki-compile/example_wiki_compile.py:39-113,245-293`).
Legality is a pure function, not a call:

```python
def decision_legal(d: IngestDecision, page: PageState | None) -> bool:
    """Active-page protection: a reviewed or locked page with conflicts is flagged, never updated."""
    if page is None:
        return d.action == "create"
    if d.action == "create":
        return False
    return not (d.action == "update" and page.status in PROTECTED_STATUSES and d.conflicts)
```
(`dspy-agent-skills:skills/dspy-wiki-compile/example_wiki_compile.py:129-135`).
The metric weights `{"citations": 0.30, "decisions": 0.25, "merge": 0.20,
"diffs": 0.15, "links": 0.10}`, the heaviest axis by a wide margin
(`dspy-agent-skills:skills/dspy-wiki-compile/example_wiki_compile.py:34`) —
independent confirmation that `scripts/quotes.py`, built the same day this skill
was read and before it, targets the right thing (`Plan/concept/wiki-compile-second-opinion_2026-09-17.md`).

**Code versus docs.** The metric's own helper, `_mean([]) == 1.0`
(`dspy-agent-skills:skills/dspy-wiki-compile/example_wiki_compile.py:161-163`),
makes an **empty compile score 0.70** with the feedback "cited, legally
decided, merged across sources, consistent diff", and one extraction with one
claim and nothing merged or decided scores **1.0**; only the citations axis
returns 0.0 for nothing. `citation_resolves` is a literal substring test that
accepts an empty or one-character quote
(`dspy-agent-skills:skills/dspy-wiki-compile/example_wiki_compile.py:122-126`).
Legality reads the model's own `conflicts` list: an `update` with `conflicts=[]`
on a `reviewed` page is legal, and a `contested` page — exactly what
`dspy-adversarial-review`'s demotion produces — is unprotected
(`dspy-agent-skills:skills/dspy-wiki-compile/example_wiki_compile.py:129-135`).
"Challenged ⊆ conflicts" accepts any shared token over two characters, so „…
ist strittig" matches „Kapitel 13 ist falsch" through „ist"
(`dspy-agent-skills:skills/dspy-wiki-compile/example_wiki_compile.py:138-147`).
The metric never compares against expected claims or concepts at all, although
the skill's own gold-set spec calls for "hand-checked claims"
(`dspy-agent-skills:skills/dspy-wiki-compile/SKILL.md:110-111`) — there is no
recall axis, the retired pipeline's version zeroed the merge axis on exactly
this gap and folded in gold-concept coverage, and this pack does not.

**Mapping onto this repository.**

- *Extract* is a census: `scripts/profile.py`, `Plan/briefings/extract.md`, and
  the rule that a census describes one document and nothing else. Both arrived,
  independently, at "sources are never modified" and "drafts go to a candidates
  area, promotion is a human step" (`Plan/concept/wiki-compile-second-opinion_2026-09-17.md`).
- *Merge*'s `ConceptDraft.definition` — one merged sentence per concept — is
  exactly what P13 forbids. The target equivalent is *gather*: attach every
  document's reading to the page with `^[slug.md:Lnn]`, never a synthesised
  definition, and `Disagreement` maps onto a `Wiki/conflicts/` record whose
  `resolution` may only ever be `pending` for a program — never `supersedes`
  (`Plan/decisions/003-conflicts-get-their-own-record.md`: "a source granting
  itself authority" resolving a conflict was "explicitly rejected").
- *Decide*'s `create`-by-lookup is what `scripts/reconcile.py` already does
  against `Wiki/index.json` (68 of 109 candidates decided by lookup in document
  6); `flag`/`update` correspond to "new conflict" / "new reading". The
  protected-page half of `decide` is the reviewed-page rule this repository has
  named and not built (`NOW.md`).
- *Diff*'s `reinforced/challenged/new/gaps` is the per-document table already in
  `Wiki/compare/`; `gaps` is the column the target lacks today and maps onto
  `Wiki/questions/` and P10.
- The weighted sum itself is refused: P11 forbids collapsing several checks into
  one pass/fail number, and "not scored" must stay a third state instead of
  folding into 0.0 or a false 0.70 — the same P15/P23 shape the whole skill pack
  repeats.

**Verdict.** Taken: the citation-line contract (kept stricter, via `read.py
--find` and `quotes.py`'s normalisation, which false-fails less than this
pack's literal check); create-by-lookup; the diff-as-receipt shape. Refused:
the merge step, the weighted single score, and self-reported legality. Waiting:
the reviewed-page rule, for the first page ever promoted out of
`Wiki/candidates/` — nothing has been, so the case has not arisen (`NOW.md`).

---

## Independent review and judges

**Mechanism.** `dspy-adversarial-review` asserts the reviewer differs from the
writer before every call:

```python
def same_lm(a, b) -> bool:
    if a is b:
        return True
    return getattr(a, "model", None) == getattr(b, "model", None) and getattr(a, "kwargs", None) == getattr(b, "kwargs", None)
```
(`dspy-agent-skills:skills/dspy-adversarial-review/example_adversarial_review.py:58-69`),
then runs `ReviewArtifact(artifact, evidence, difficulty) → Review{score 1..10,
overstated: list[Overstated{quote, why, evidence_needed}], unsupported,
strengths, weaknesses}` under `with dspy.context(lm=self.reviewer_lm):`
(`dspy-agent-skills:skills/dspy-adversarial-review/example_adversarial_review.py:129-151`,
`dspy-agent-skills:skills/dspy-adversarial-review/SKILL.md:53-69`).
`demotion(review, demote_at=3)` returns `"contested"` at three or more
overstated claims — "a status change, never an edit"
(`dspy-agent-skills:skills/dspy-adversarial-review/example_adversarial_review.py:72-74`).
`review_refine` wraps the writer in `dspy.Refine(module=writer, N=rounds,
reward_fn=review_reward(reviewer, evidence), threshold=0.8)`, reward = review
score / 10 (`dspy-agent-skills:skills/dspy-adversarial-review/example_adversarial_review.py:170-180`).

**Code versus docs, two findings that matter beyond this one skill.**

1. **`dspy.Refine` does not pass the judge's findings to the writer.** The
   skill's own claim is "the writer learns from the judge, not from itself"
   (`dspy-agent-skills:skills/dspy-adversarial-review/reference.md:62-64`), but
   in DSPy 3.3.1 `Refine`'s feedback is written by `dspy.Predict(OfferFeedback)`
   run on `dspy.settings.lm` — the **writer's own LM** — from the reward
   *number* and the reward function's *source code*; the review's reasoning
   never appears in the advice (`dspy:predict/refine.py:148-167`, read directly
   against the installed package). An offline two-`DummyLM` probe confirms it:
   two feedback calls landed on the writer LM, `"ZZ_REVIEWER_REASON_ZZ"` never
   appeared in either, the reward number did
   (`dspy-agent-skills:skills/dspy-adversarial-review/example_adversarial_review.py:170-180`,
   probe `probe_refine`). If a review is meant to reach the writer, it has to
   go in as a declared input field, not through `Refine`'s own advice channel.
2. **`BestOfN` and `Refine` hide total failure for a small `N`.** `fail_count`
   defaults to `N` and is compared *before* it is decremented each attempt
   (`dspy:predict/best_of_n.py:75-79`, `dspy:predict/refine.py:170-174`): with
   every attempt of the wrapped module raising, `N=2` swallows both failures
   silently and returns `None`; `N=3` raises the underlying exception on the
   last attempt instead. [checked: refine-none-when-all-fail] — the probe in
   `scripts/check_dspy_skill.py` constructs a module whose `forward` always
   raises, wraps it in `BestOfN` and `Refine` at `N=2` and `N=3`, and asserts
   exactly this asymmetry: `None` at `N=2`, the raised exception at `N=3`, for
   both wrappers. A caller that assumes either "it always raises" or "it always
   returns `None`" is wrong for some `N`, and a `None` return is
   indistinguishable from a real answer unless it is checked (P15).

The judge metric itself scores degenerate reviews 1.0: bidirectional substring
matching after normalisation makes an empty flag, a one-word flag ("Kernwelten",
"Kael"), or the whole artifact as one flag each score **1.0** with "every
overstated and unsupported claim found, none invented"
(`dspy-agent-skills:skills/dspy-adversarial-review/example_adversarial_review.py:85-121`).
The independence guard is weak in the same direction as `same_lm`'s own
docstring concedes: two `dspy.LM` objects with the same model string and
different `temperature` pass it
(`dspy-agent-skills:skills/dspy-adversarial-review/reference.md:41-43`).

**Mapping onto this repository.** A second model may only *direct attention*,
never decide: `overstated{quote, why, evidence_needed}` reframed is a list of
page sentences to re-read against their line, and `evidence_needed` names the
next document to fetch — the same role the `jev`/`typesafe` skills already give
a second opinion. `demotion` must never change a page's status; that would
remove exactly the protection the (unbuilt) reviewed-page rule is meant to add.
The judge metric's F1 shape is P27 done right — `Plan/runs/judgements.jsonl`'s
68 human decisions and the twelve conflict records are the labels a judge of
judges would be scored against — but its matching must be line identity (a
`^[slug.md:Lnn]` from `read.py --find`), never containment.

**Verdict.** Taken: the independence assertion pattern, compared on model
string alone; the F1-against-human-labels shape for scoring a second opinion.
Refused: `demotion` writing to a page's status; `Refine` as the feedback
channel between a judge and a writer — a declared input field carries the
review instead. Waiting: nothing here calls a second model on wiki text yet
(`NOW.md`, "How far the yes to TypeSafe reaches").

---

## Clarification and precision gates

**Mechanism.** `dspy-clarify` is `Hmbown/clarify`'s refactoring rules
transposed from code to prose: rename → bindings, magic values → explicit
`scope` only where the source states it, a cryptic condition →
`Ambiguity(phrase, readings: list[str] (min_length=2), question)`
(`dspy-agent-skills:skills/dspy-clarify/reference.md:9-20`). One signature,
`ClarifyClaim(claim_text, source_excerpt, entities, glossary_terms,
canon_context) → Clarification{clarified_text, scope, assumptions,
ambiguities, bindings, verdict}`
(`dspy-agent-skills:skills/dspy-clarify/example_clarify.py:137-161`). Three
verdicts, and only one may propose promotion: `clear`, `needs-author` ("its
questions are the deliverable"), `not-promotable` (not a claim, or self-
contradicting its own citation)
(`dspy-agent-skills:skills/dspy-clarify/SKILL.md:26-31,110-112`). The rule that
makes the gate more than a rewrite: "A second call with the same input must not
resolve an ambiguity the first call raised; only the human (or a source
passage) does" (`dspy-agent-skills:skills/dspy-clarify/SKILL.md:108-120`).

**Code versus docs.** Hedge and quantifier detection is space-delimited
(`_present` looks for `" {m} "`), so „nie." and „immer," are invisible to it:
„AEGIS wird in Akt I beim Namen genannt, nie." scores **1.0** although it drops
„nicht" and adds „nie"
(`dspy-agent-skills:skills/dspy-clarify/example_clarify.py:61-63,100-106`). The
hedge axis is 0 when the hedge count rises even if every hedge is declared, but
the feedback only fires for *undeclared* hedges, so a declared, added
„vielleicht" scores 0.85 with "Clarified without adding or losing meaning."
(`dspy-agent-skills:skills/dspy-clarify/example_clarify.py:100-106`). The
consistency check `(verdict != "clear") == bool(ambiguities)` fails a
`not-promotable` verdict with no ambiguities, contradicting the reference's own
"the metric does not score it differently"
(`dspy-agent-skills:skills/dspy-clarify/example_clarify.py:116-121`;
`reference.md:48-50`). And the metric reads no gold clarification and no
expected verdict at all — an identity rewrite of a hedge-free claim with
verdict `clear` scores **1.0**, and only German → English rewriting is caught,
never English → German (`dspy-agent-skills:skills/dspy-clarify/example_clarify.py:123-128`;
the metric needs no gold, `dspy-agent-skills:skills/dspy-clarify/reference.md:96-99`),
which undercuts the skill's own claim that gold `needs-author` cases "teach the
optimizer" (`SKILL.md:124-126`): the metric cannot see them.

**Mapping onto this repository.** There is no rewrite step here: pages quote
(P12), and a model never types an identifier (P26), so `clarified_text` has no
place on a page. What transfers is the *verdict and the questions*:
`needs-author` → an entry under `NOW.md`'s author-questions heading or a new
`Wiki/questions/` page; `not-promotable` → stays in the note; `clear` → may be
*proposed*, never applied (P0: promotion is the author's alone). The
deterministic checks — no new quantifier, no smuggled slug, scope only where
the source states it — are worth porting as checks over a model's *proposal
text*, with word-boundary matching this time. Scope axes map onto the novel's
Kernwelten, chapters and Alters; bindings map onto `Wiki/index.json`'s slugs
and surfaces (exact match, the way the metric already requires); hedge counting
already exists in this repository's own reading of document 5 (163 hedging
words in 13,947).

**Verdict.** Catalogued, not built: a gate over a model's proposal, scored by
this skill's deterministic checks with word-boundary matching, gated on
`needs-author` reaching a real question record. Refused: the rewrite itself
as anything that lands on a page. Waiting: a model ever proposing wiki text
that needs gating (`NOW.md`).

---

## Dialectics: tetraframe and autodialectics

### Four isolated corners (`dspy-tetraframe`)

**Mechanism.** `DistillSeed → Distilled{…, frame_risk_score}` →
`SelectPredicate → primary_predicate` → `GenerateCorner(view: CornerView) →
Corner` run four times under subclassed signatures `CornerP`/`CornerNotP`/
`CornerBoth`/`CornerNeither`, each seeing **only** its own `CornerView` (seed,
stakes, constraints, hidden assumptions, the primary predicate, evaluation
criteria) under `dspy.context(lm=lm.copy(rollout_id=i, temperature=…))` →
`MapCorners(corners) → Cartography{contradiction_map, complementarity_map,
discriminators, invariants}` → `Transform(...) → Frame{transformed_predicate,
survivors_from_p, survivors_from_not_p, hidden_structure_from_both,
dissolved_false_frame_from_neither, operational_tests}`
(`dspy-agent-skills:skills/dspy-tetraframe/example_tetraframe.py:44-111,245-293,305-324`).
Rule 2 states the discipline this repository already applies to conflicts: "A
failed check blocks the run, not the decision. … never edit a corner by hand to
pass verification"
(`dspy-agent-skills:skills/dspy-tetraframe/SKILL.md:151-164`).

**Code versus docs.** The isolation guard cannot fire: it compares
`view.model_dump()` keys against `CornerView.model_fields`, but pydantic's
default `extra="ignore"` drops unknown kwargs at construction, so the
difference is always empty — leakage through a field's *content* (another
corner's text smuggled into `hidden_assumptions`) passes silently
(`dspy-agent-skills:skills/dspy-tetraframe/example_tetraframe.py:131-134`).
Every similarity check is ASCII-tokenised (`[a-zA-Z_]+`), so „Die Schöpfung
hält Kernwelten zusammen" becomes `{die, kernwelten, pfung, sch, zusammen}` and
German filler scores maximum slop
(`dspy-agent-skills:skills/dspy-tetraframe/example_tetraframe.py:117`). Most
important for this repository: **`contradiction_honesty` rewards the number of
contradictions found** — 0.25 for none, 0.75 for three plus one discriminator,
1.0 for six
(`dspy-agent-skills:skills/dspy-tetraframe/example_tetraframe.py:184-187`) —
which, run as a GEPA metric, pushes a mapper toward inventing more
contradictions, and the whole verification suite is a *mean*, so a cartography
naming no contradiction at all (0.25) still lets the run score **0.893**
(`example_tetraframe.py:233-236`; P11).

**Mapping onto this repository.** The shape maps well onto conflicts already
recorded: C6 (five Guardians versus two) or C11 (Landauer warmth) are exactly
the case the skill is for — "a contested decision" where a decision "has two
camps" (`dspy-agent-skills:skills/dspy-tetraframe/SKILL.md:3,9`). P/not-P are the two sources' readings,
attributed; *both* is a typed split the sources already state themselves —
document 11 puts the character bible's Kap-33 garden down as Juna's *effect*
and her Kap-38 appearance as a `temporal_split` of C7; *neither* would say
the conflict is misframed (P14). `discriminators` names the unread document that
would settle it. The output stays a discussion item — decision 006 already
settled that no run, however framed, resolves anything.

**Verdict.** Refused as a scored program: `contradiction_honesty` is precisely
the shape P14 and the `Zero-Trust` false conflict warn against, and the suite
is not German-aware. Kept as an unscored shape for writing up a contested
conflict by hand. Waiting: a conflict contested enough that the four-corner
write-up earns its cost over the existing P/not-P record.

### Keep a program run honest (`dspy-autodialectics`)

**Mechanism.** Three tiers: Tier 0 is `compile_contract → slop_score → gate`
with no LM calls at all; Tier 1 adds `Dialectic` (Thesis → steps; Antithesis →
`Objection{claim, objection, severity 0..1}`; Synthesis →
`Disposition{objection_index, accepted, how}`, revised steps) plus a `Verify`
that "never sees the plan"; Tier 2 is champion/challenger GEPA with canaries
(`dspy-agent-skills:skills/dspy-autodialectics/SKILL.md:34-43,86-135`). The
gate and promotion are pure functions:

```python
def gate(verdict_pass: bool, confidence: float, score: float, slop: float) -> str:
    if not verdict_pass and confidence < REJECT_CONFIDENCE:
        return "reject"
    if slop > REJECT_SLOP:
        return "reject"
    if verdict_pass and score >= ACCEPT_MIN_SCORE and slop < ACCEPT_MAX_SLOP:
        return "accept"
    return "revise"

def promote(champion, challenger, canaries_passed) -> tuple[bool, str]:
    """(score, slop) pairs; all three conditions are required."""
    if not canaries_passed:
        return False, "canary failed"
    if challenger[1] > champion[1]:
        return False, "slop up"
    if challenger[0] <= champion[0]:
        return False, "score not up"
    return True, "score up, slop not up, canaries pass"
```
(`dspy-agent-skills:skills/dspy-autodialectics/example_autodialectics.py:233-258`,
condensed). "A challenger that 'wins' by sounding confident fails the canary
and is not promoted"
(`dspy-agent-skills:skills/dspy-autodialectics/SKILL.md:172-174`).

**Code versus docs.** The end-to-end GEPA metric trusts the very program it is
optimizing:

```python
def harness_metric(gold, pred, trace=None, pred_name=None, pred_trace=None):
    """End-to-end GEPA metric: verified criteria + slop feedback, one Prediction."""
    import dspy
    slop = slop_score(gold.contract, pred.output, pred.objections)
    score = run_score(gold.contract, pred.checks, slop.dims, pred.objections, pred.dispositions)
    ...
```
(`dspy-agent-skills:skills/dspy-autodialectics/example_autodialectics.py:322-331`).
`pred.checks` comes from the LM's own optimized `Verify` predictor, not from a
deterministic `criterion_checks`, and GEPA can raise the metric purely by
rewriting `Verify`'s instruction to claim more passes — the sloppy demo scores
0.71 (gate: revise) against **0.46** with the deterministic checks
(`dspy-agent-skills:skills/dspy-autodialectics/example_autodialectics.py:326-329`,
probe `AD6`). This is P1 stated as a failure: a model is the verifier exactly
where code could be. Objection coverage is 1.0 when nothing was objected at all
— the anti-pattern the skill itself names and its own code commits
(`dspy-agent-skills:skills/dspy-autodialectics/SKILL.md:183`, `example_autodialectics.py:223`).
An empty `Output(text="")` scores **low slop** (0.825), because the "status
completed with < 50 chars of output" indicator the reference promises is not in
the code (`dspy-agent-skills:skills/dspy-autodialectics/reference.md:97`;
`example_autodialectics.py:176-177`) — P19's "assert non-empty output" in
another costume.

**Mapping onto this repository.** The contract's `source_hash` is this
repository's census-frozen-first rule in another form (`Plan/concept/wiki-process_2026-09-16.md`
is the source concept). `Verify` seeing only the contract and the output, never
the plan, is what `quotes.py`/`read.py` already do deterministically. `promote`
plus canaries is `baseline.py compare` plus `pairs.py`'s never-merge canaries —
stricter here, because this repository's canary is a veto (a candidate that
merges `Negentropie`/`Entropie` is disqualified, not docked one twenty-sixth)
rather than a threshold.

**Verdict.** Refused wholesale as a running program: nothing here has an
executor to keep honest in this sense, and `harness_metric`'s self-trust is
exactly the shape P1 rules out. Kept as vocabulary: gate, canary, and
champion/challenger are already `baseline.py`'s and `pairs.py`'s words for
their own, stricter rules.

---

## Refining a knowledge base, and learning from corrections

### `dspy-deep-refine`

**Mechanism.** A hop loop: `JudgeAnswerable(question, triples) → bool`; on
`len(history) ≤ 1` an early exit with no abduction; otherwise
`AbduceErrors(question, interaction_history) → Abduction{incompleteness,
incorrectness, redundancy}` ("cite the triples or gaps you mean; do not propose
edits") then `ProposeRefinements(question, triples, abduction) →
list[RefinementAction{kind ∈ insert_edge|delete_edge|replace_node, args:
2..3}]`, at most ten, with "never delete unrelated triples; use
source-qualified node names ('file.md::Name') whenever a bare name is
ambiguous"
(`dspy-agent-skills:skills/dspy-deep-refine/SKILL.md:46-75`;
`example_deep_refine.py:168-190,203-217`). Review is deterministic — evidence
strings, then a confidence label:

```python
if warnings:
    confidence = "LOW"
elif any(e.startswith(("Exact edge", "Replacement source")) for e in evidence):
    confidence = "HIGH"
elif evidence:
    confidence = "MEDIUM"
else:
    confidence, warnings = "LOW", ["No node or edge evidence found."]
```
(`dspy-agent-skills:skills/dspy-deep-refine/example_deep_refine.py:96-111`).
`apply_actions` "**never called by the module**"; "a generated action list, a
valid trace, or a successful review is **not** approval"
(`dspy-agent-skills:skills/dspy-deep-refine/SKILL.md:32,120-122`).

**Code versus docs.** The grading measures whether an action is well-formed
against the graph, not whether it is right: `replace_node(Juna → Kael)` — merging two entities — is graded **HIGH**
because the source node exists; deleting an existing edge is HIGH; inserting an
edge that already exists (a no-op) is HIGH
(`dspy-agent-skills:skills/dspy-deep-refine/example_deep_refine.py:96-111`, probe
`DR1`). `replace_node` does not even merge — it only relabels, so two nodes end
up labelled "Kael" and every later action naming Kael is LOW, contradicting the
reference's own "merge into an existing `new` node if present, rewiring edges"
(`dspy-agent-skills:skills/dspy-deep-refine/reference.md:137`;
`example_deep_refine.py:138-141`). `max_hops > 4` crashes with `IndexError`
(`example_deep_refine.py:23,206`), and the trainset applies proposals to
`gold.graph` while `forward` retrieves through a separately bound retriever, so
a real trainset would optimise proposals against one graph and score them
against another
(`dspy-agent-skills:skills/dspy-deep-refine/example_deep_refine.py:165,206,224-229`).

**Mapping onto this repository.** The premise already holds here: a question
the wiki cannot answer names its own next document. Map the three abduction
axes onto this repository's three records, never onto graph edits:
*incompleteness* → a `Wiki/questions/` page naming the unread document (entity
lists already route a question to unread documents that name it, with the
line); *incorrectness* → a conflict record, never resolved by the loop (P13,
P14); *redundancy* → a one-term-or-two judgement for `scripts/pairs.py` and
`Plan/runs/judgements.jsonl`. `refine_metric`'s check of whether the question
becomes answerable has a direct analogue already built: `graphrag.py bench`'s
20 <!--state:graphrag.cases--> labelled cases, recall@8
48 <!--state:graphrag.recall_seeds-->% from seeds alone and
67 <!--state:graphrag.recall_ppr-->% with PageRank — measured
by retrieval over verified quotations, not by applying edits.

**Verdict.** The *actions* are refused outright: `insert_edge` is an inferred
link (decision 005), `replace_node` merges two entities or surfaces (P13, and
the grading logic shows it is graded HIGH exactly when it is wrong to apply).
The transferable part is the refusal machinery alone — closed action enum,
deterministic review, apply never called by the proposer, review not equal to
approval — which is already stricter here: nothing in this repository ever
writes a graph edge from a model at all.

### `dspy-reflect-loop`

**Mechanism.** `ExtractLearningSignal(message, prior_assistant_turn,
program_name) → LearningSignal{is_learning, kind ∈
correction|approval|observation|explicit, confidence ∈ HIGH|MEDIUM|LOW,
old_behavior, new_behavior, learning, scope_hint}` behind a recall-tuned regex
pre-filter over user turns
(`dspy-agent-skills:skills/dspy-reflect-loop/example_reflect_loop.py:23-39,65-68,74-82`).
A ledger row is `Learning{fingerprint = sha256(lower, whitespace-collapsed
text)[:16], learning, kind, confidence, contexts, count, status}`;
`eligible_for_promotion(threshold=2)` requires two contexts and not already
promoted; promotion is `preview → user approval → apply with a backup`, "never
automatic"
(`dspy-agent-skills:skills/dspy-reflect-loop/example_reflect_loop.py:42-62`;
`SKILL.md:115-129`). "A correction is not a markdown section to append — it is
a **gold example plus feedback**"
(`dspy-agent-skills:skills/dspy-reflect-loop/SKILL.md:16-18`).

**Code versus docs.** The pre-filter's German and punctuation anchors mostly
never match: the trailing `\b` after `nein,`, `no,` and `remember:` needs a
word character next, so "Nein, das ist falsch so.", "No, that's the wrong
file." and "Remember: tabs for Makefiles." are all filtered out; "benutzen"
does not match `benutze`
(`dspy-agent-skills:skills/dspy-reflect-loop/example_reflect_loop.py:23-27`).
`corrections_metric` is satisfied by mere coexistence: both "uv pip install"
and "pip install" present in the output score **1.0**
(`dspy-agent-skills:skills/dspy-reflect-loop/example_reflect_loop.py:105-110`).
`reflector_metric` ignores eight never-skipped noise signals and punishes a
correct paraphrase of an accepted learning at 0.0
(`example_reflect_loop.py:114-119`). And the ledger keeps the **first**
confidence seen, not the max the reference promises — LOW then HIGH stays LOW
(`dspy-agent-skills:skills/dspy-reflect-loop/reference.md:74`;
`example_reflect_loop.py:54-58`).

**Mapping onto this repository.** `Plan/runs/judgements.jsonl` already **is**
this idea, done by identity instead of substring, over the whole judgement
history: two surfaces, a decision, a rule, and whether code claims it, replayed
by `scripts/judgements.py` (`agrees` / `DISAGREES` / `judgement`). What the
skill adds worth taking: the recorded `rule` text of a judgement is already the
GEPA feedback string for `pairs.py`'s residual model, and fingerprint + contexts
+ threshold ≥ 2 is a real promotion rule for a judgement to become mechanised —
still a human step. The author's corrections arrive in German (decision 006 is
quoted in German), where this skill's own pre-filter anchors mostly fail, and
nothing here may extract a judgement from a transcript without the author's yes
(P0).

**Verdict.** Kept as confirmation that `Plan/runs/judgements.jsonl` and
`scripts/judgements.py` already do the load-bearing part of this pattern.
Catalogued: the rule-text-as-feedback bridge for `pairs.py`'s model on the
residual. Refused: automatic signal extraction from any transcript.

---

## Sessions, memory and History

**Mechanism.** `dspy-session` wraps any `dspy.Module` in `Session`. Each call
records a `Turn{index, inputs, outputs, history_snapshot: dspy.History,
score}`, snapshotted at call time and never rewritten later — the snapshot is
the whole point: later turns never change it
(`dspy-session:dspy_session/session.py:61-69,689-696`). `to_examples()`
turns turns into independent `dspy.Example`s, cutting a trajectory at the first
failing turn under `strict_trajectory` "because later turns may rely on a
flawed answer" (`dspy-session:dspy_session/session.py:1152-1171`).
`with_memory` adds per-node policies — isolated/shared, persistent/episodic/
stateless, an optional consolidator distilling L1 into an `l2_memory` string
(`dspy-session:dspy_session/session.py:1287-1339`). Projection helpers
(`get_current_history`, `get_outer_history`, `get_node_memory`,
`get_child_l1_ledger`, `get_execution_trace`) are the only sanctioned ways one
node reads another's state, and the design rule is explicit: **"Push, Don't
Peek."** "If Node A needs Node B's data, Node B must push it as an explicit
output." Hidden side channels break optimizer causality: "When the optimizer
tries to figure out why the writer hallucinated, the causal trace is broken.
Optimization fails silently." (`dspy-session:docs/api-usage-examples.md:975-1111`).

**Code versus docs — the load-bearing gaps.** A Session-wrapped predictor's
closure captures the *original* predictor's bound `forward`, so after
`deepcopy`, `fork()` or any optimizer copy, calls keep running the original:
`BootstrapFewShot.compile(session)` prints "Bootstrapped N full traces" while
the compiled predictor carries **0 demos**
(`dspy-session:dspy_session/session.py:557-587`, measured). Plain `sessionify`
on a *composed* program feeds the root history into every nested predictor,
signature-filtered: unmatched outputs render as `None`, and a user turn with no
matching input field is dropped entirely — a "remembering" two-stage chat sends
`travel_advice: None` as its own prior answer
(`dspy-session:dspy_session/session.py:557-587`; README examples 1–2,
measured). And DSPy treats an input as conversation history **only** on exact
annotation, `annotation == dspy.History`
(`dspy:adapters/base.py:604-608`): a `dspy.History` built from
`{"role": "user"/"assistant", "content": …}` dicts instead of the signature's
own field names renders **both** messages as *assistant* turns reading
`[[ ## answer ## ]]\nNone` — the question text never reaches the prompt at all,
and nothing raises
(`dspy-agent-skills:skills/dspy-book-agents/SKILL.md:54-56,124`, measured
against 3.3.1). `dspy.RLM` compounds this: on 3.3.1 wrapping it in a
History-injecting session fails immediately with `ValueError: Unexpected
inputs not declared in the signature: ['history']`
(`dspy-session:dspy_session/session.py:1460-1488`, measured) — which is
exactly why `Plan/concept/dspy-toolchain_2026-09-23.md` states, as a rule
about `lmrun.py`, "Never wraps `dspy.RLM` in a `History`-carrying session"

Metric plumbing hides failure the same way three other families in this file
do: `score()` spends one real metric call probing its arity before scoring
anything; with `gold=None` a label-comparing metric is handed the turn's own
outputs as the label, so it scores **1.0 trivially**; a metric error or a
`None` return both become 0.0, indistinguishable from a genuinely wrong answer
(`dspy-session:dspy_session/session.py:1085-1135`).

**Mapping onto this repository.** Nothing here is a multi-turn agent, so
`Session` itself has no instance yet. What transfers now: the frozen-`Turn`
shape is the pattern `lmrun.py`'s per-call record already follows (input,
output, `finish_reason` and model frozen at call time, never reconstructed);
"Push, Don't Peek" is the same rule as P13 restated for data flow — a later
step may not read another step's private state, only what it declared as
output. The History-annotation trap is a standing warning for any future
signature that carries prior turns: `check_dspy_surface.py` should assert
`annotation is dspy.History` exactly, not merely that a field exists.

**Verdict.** Catalogued for the day a session exists: frozen-`Turn` snapshots,
"Push, Don't Peek", per-predictor (not root-broadcast) history. Refused
outright, already, in writing: `dspy.RLM` inside a `History`-carrying session.
Waiting: a real multi-turn program in this repository (none exists as of
2026-09-24).

---

## Agents, tools and MCP

**Mechanism.** `dspy-agents` wraps one compiled `ChainOfThought("context,
question -> answer")` as Agno tools: a plain function registered with
`Toolkit.register(fn, name=...)`, whose **docstring is the description the
agent model sees** — the same role a `SKILL.md` `description` plays for a
ReAct-style selector
(`dspy-agents:tools/mini_report_toolkit.py:26-52`;
`dspy-agent-skills:skills/dspy-book-agents/reference.md:115-119`).
`Agentic-Dspy-Rag` classifies intent with a bare `Predict`, then routes on a
substring of the free-text answer:

```python
self.classifier = dspy.Predict("question -> intent", n=1)
...
if "Comparative" in user_intent: ... elif "Multi-step" in user_intent: ... else: SimpleRAG
```
(`Agentic-Dspy-Rag:src/agentic_rag/components/agents.py:101-127`).
`dspy-book-agents` states the MCP lifecycle DSPy leaves entirely to the
caller — `stdio_client` → `ClientSession` → `session.initialize()` →
`session.list_tools()` → `[dspy.Tool.from_mcp_tool(session, t) for t in
tools]` → `dspy.ReAct(..., tools=tools, max_iters=10)` → `await
agent.acall(...)` — and sizes `max_iters` by task openness: 5 for a narrow
check, 8 moderate, 12 for a multi-hop lookup, 15 for open research
(`dspy-agent-skills:skills/dspy-book-agents/SKILL.md:22-43,101`;
`reference.md:6-31,94`). Its stated reliability posture is "no retry logic, no
timeouts except one, and no cost caps"; a tool error becomes "graceful
degradation — check the key, return a message string, set a readiness flag,
never raise"
(`dspy-agent-skills:skills/dspy-book-agents/SKILL.md:96-107`). `dspy-book-modules`
gives `CodeAct(signature, tools, max_iters=5, interpreter_factory=…)` a
narrower tool contract than `ReAct`: `inspect.isfunction(tool.func)` must hold,
so bound methods and `functools.partial` raise `ValueError` at construction,
where `ReAct` accepts a callable object or `dspy.Tool`
(`dspy-agent-skills:skills/dspy-book-modules/example_module_choice.py`;
`dspy:predict/code_act.py:64-65`).

**Code versus docs — silent failure, twice.** The book states the async rule
as a hard guarantee: "A synchronous `agent(...)` call with an asynchronous
converted tool raises `ValueError` by default"
(`dspy-agent-skills:skills/dspy-book-agents/reference.md:26-29`). It does not,
in DSPy 3.3.1. `Tool.__call__` does raise, but `ReAct` catches every tool
exception itself and stores it as the *observation*:

```python
try:
    trajectory[f"observation_{idx}"] = self.tools[pred.next_tool_name](**pred.next_tool_args)
except Exception as err:
    trajectory[f"observation_{idx}"] = f"Execution error in {pred.next_tool_name}: {format_error_for_lm(err, ...)}"
```
(`dspy:predict/react.py:112-115`) — the agent logs an `asyncio` warning and
answers anyway, without the tool's data, looking exactly like a normal
completion. Measured: a sync call to an async-wrapped weather lookup still
returned "sunny in Oslo"
(`dspy-agent-skills:skills/dspy-book-agents/example_agent_budget.py:87-92`).
Substring routing fails the same way, silently: offline scripted intents show
`"comparative"`, `"Multi-Step"`, `"Multistep"`, `"Not Comparative"` (negated)
and `"Multi-step (Comparative)"` misrouting with no error: the first three
fall into the `else` default, and the last two reach the comparative agent,
because its substring test runs first
(`Agentic-Dspy-Rag:src/agentic_rag/components/agents.py:109-123`, measured).
Both are P15's "never reached" masquerading as "answered", produced by exactly
the free-text pattern `pairs.py`'s `Literal["one-term","two-terms"]` was built
to avoid (an out-of-set `Literal` output is *unparseable*, not silently
misrouted — `api.md` has this checked against 3.3.1). In the same
repository, a critique step is computed and then never applied: `critique_step`
writes `state["critique"]`, and `finalize_step` reads neither `notes` nor
`edits`, truncating the brief and padding it with four boilerplate bullets
instead (`dspy-agents:workflows/research_report.py:219-222,238,265-277`) — a
concrete instance of the critique→repair family's central failure mode, found
inside an agent rather than an optimizer.

**Mapping onto this repository.** The baseline-store shape (task, program
hash, trainset hash, per-example outcomes, score, cost, date, append-only) is
already kept, corrected, in `scripts/baseline.py`: `dspy-agents`' own monitor
compares only against the *previous* run and skips a `None` metric, so a
compiled program that silently fell back to zero-shot (`dspy.load` needing
`allow_pickle=True` since 3.1.0, unhandled) reported "ok" for months
(`dspy-agents:dspy_optimize/baselines/thresholds.py:150-214,186-187`,
measured) — the case `baseline.py` was built for: "`compare` checks against the
floor, not only the previous row" (`scripts/baseline.py`). `Agentic-Dspy-Rag`'s classify → route →
retrieve → rerank → generate shape is catalogued for `ask`: `graphrag.py`
already does classify (seed by folded surfaces) → route (personalised
PageRank) → quote (verified quotations only), and its multi-step mode's own
defect — synthesising sub-answers into prose with no attribution
(`Agentic-Dspy-Rag:src/agentic_rag/components/agents.py:73-90`) — is exactly
what P13 forbids and what `graphrag.py` already refuses to do ("it returns
quotations… never prose", `CLAUDE.md`). Per-directory `AGENTS.md` guides
(`dspy-agents:AGENTS.md`, ten files) are catalogued for the day a directory in
this repository is repeatedly misread by an agent — none has earned it yet.

**Verdict.** Taken, corrected: the baseline-store shape, with a floor and a
veto instead of relative-only drift. Catalogued: classify → route → quote for
`ask` (waiting on `ask` existing); per-directory `AGENTS.md` (waiting on a
directory being misread). Refused: substring routing on free text anywhere a
closed decision exists; a critique computed and not consumed; tool errors
folded into an answer without a status.

---

## Planning as a checked graph

**Mechanism.** `braid-dspy` runs one `Predict(BraidPlanSignature)(problem) →
grd`, a Mermaid flowchart string ("no numerical results", "action not value",
node labels under 15 tokens); code parses it, validates it, and orders nodes
with Kahn's algorithm; a second `Predict(BraidStepSignature)` executes each
node in that order, accumulating "Previous Steps: …" as context
(`braid-dspy:braid/module.py:48-237`). The ordering is pure Python:

```python
def get_execution_order(self) -> list[str]:
    in_degree = {node.id: 0 for node in self.nodes}
    graph = {node.id: [] for node in self.nodes}
    for edge in self.edges:
        graph[edge.from_node].append(edge.to_node)
        in_degree[edge.to_node] = in_degree.get(edge.to_node, 0) + 1
    queue = [node_id for node_id, degree in in_degree.items() if degree == 0]
    result = []
    while queue:
        node_id = queue.pop(0)
        result.append(node_id)
        for neighbor in graph[node_id]:
            in_degree[neighbor] -= 1
            if in_degree[neighbor] == 0:
                queue.append(neighbor)
    return result
```
(`braid-dspy:braid/parser.py:71-97`).

**Code versus docs.** This is exactly Kahn's algorithm, and it has Kahn's
algorithm's own property, undocumented here: **every node on or downstream of
a cycle is silently omitted**, with no error. Measured on the README's own
verification-loop shape (`Check -->|No| Calc`): the execution order is
`['Start']` — one of four nodes, one LM call, `valid=True`
(`braid-dspy:braid/parser.py:71-97`, probe `C4`). Start/end node identification
iterates a Python `set`, so which end node's output becomes the final answer
changes with `PYTHONHASHSEED` across processes
(`braid-dspy:braid/parser.py:272-286`, measured across six seeds). The
"stateful engine" that would actually execute branches is built and never
wired into the default path at all — it walks a single path, following the
first unlabelled edge at any fan-out, so `Start→A, Start→B, A→C, B→C` runs
`Start, A, C` and the `B` branch never executes
(`braid-dspy:braid/engine.py:262-343`). A critic node invents a retry edge
back to the previous node whenever the diagram names none, so a linear plan
silently gains a loop the model never drew
(`braid-dspy:braid/critic.py:146-163,294-389`). And `validate()` is `parse()`
minus the exception: `"graph TD"` (zero nodes) and even `"graphs are nice /
hello"` both return `(True, None)`
(`braid-dspy:braid/parser.py:186-188,288-302`). The metric hides all of this
under an average: an empty flowchart scores **0.68**, and so does non-Mermaid
text (`braid-dspy:braid/optimizer.py:23-252`, measured).

**Mapping onto this repository.** `Plan/concept/dspy-toolchain_2026-09-23.md`
already names the candidate instance: **"a procedure whose order is in
dispute; `account.py`'s decompositions are the candidate"** — the recursive
`account(subject, question) -> account` operation this repository is built
around already has an implicit dependency order (a document's census before
its note, its note before reconciliation) that no code currently checks.
Adopting the pattern means: the model (or a person) writes the plan as text,
code parses it into a graph, **an explicit cycle check runs before Kahn's
algorithm** rather than after it silently drops the cycle, and the run refuses
rather than executing a truncated order. Sort ties deterministically —
`braid-dspy`'s own bug is the counter-example for why.

**Verdict.** Catalogued as "a procedure as a checked graph", not built.
Kahn's algorithm and the "structural validation gates execution" idea are
worth taking whole; the specific defect (no cycle check, hash-seed-dependent
ties, a fan-out engine that is built and never wired in) is exactly what a port
must add back.

---

## Critique → repair prompt loops

**Mechanism.** `dspy-optimizer` is not a DSPy teleprompter — `PromptOptimizer`
subclasses `dspy.Module` with no `forward`, and `optimize(dataset, scorer)`
returns a prompt **string**, not a program
(`dspy-optimizer:dspy_optimizer/optimizer.py:13-58,195`). Per failing example,
up to `max_refine_iters` rounds: `Evaluator` (a per-call
`with_instructions(prompt)` `ChainOfThought`, so it has **no** `named_predictors`
and is invisible to every DSPy optimizer, save/load and demos —
`dspy-optimizer:dspy_optimizer/evaluator.py:22-43`) → `scorer(example,
prediction) -> bool` → on a miss, `Refiner` proposes `PromptPatch(target_block,
operation ∈ append|replace, content)` from the failure history, with two
worked examples inside its signature's own docstring instead of as demos
(`dspy-optimizer:dspy_optimizer/refiner/signature.py:6-138`) → a
`BlockBasedMerger` finds `^{target_block}.*$` up to the next `^###\s` header
and applies the patch → a `Validator` (`full`/`batched`/`sample`/
`single_example`) checks the *candidate*, and only on `valid` is it adopted and
the loop breaks (`dspy-optimizer:dspy_optimizer/optimizer.py:86-190`). "Self-
critique with a failure history": each attempt sees exactly which previously
proposed patches already failed, so it does not repeat them
(`dspy-optimizer:dspy_optimizer/optimizer.py:106,184-187`).

**Code versus docs.** The README's own stated order, "Evaluator → Refiner →
Validator → Merger"
(`dspy-optimizer:README.md:139`), is not the code's order — merging happens
*before* validation
(`dspy-optimizer:dspy_optimizer/optimizer.py:152-190`, measured). "Validation"
runs on the *same* dataset the candidate is being optimized against — there is
no held-out set, despite the design doc's "a `training_set` and a
`validation_set`"
(`dspy-optimizer:DESIGN.md:33,48`; `dspy_optimizer/optimizer.py:152-158`), so
an accepted patch is fitted to the data it is judged on. All three of `full`,
`batched` and `sample` **pass on an empty dataset** — `True`, or `{"is_valid":
True, "score": 1.0}  # Vacuously true`
(`dspy-optimizer:dspy_optimizer/strategies/validation/{full,batched,sample}.py`,
measured) — the same "a check that cannot fail" shape the whole nine-repository
scan found six times over
(`Plan/concept/dspy-toolchain_2026-09-23.md`, "The one finding that repeats
across repositories": `dspy-advanced-prompting`'s edge-case/robustness/
consistency/coverage metrics default to 1.0 on nothing, `dspydantic`'s judges
default to 0.5, `dspy-optimizer`'s validators pass on empty input,
`dspy-agents`' baseline monitor accepts a `score=0.0, total_calls=0` run,
`braid-dspy`'s critic passes on keyword-count ties, and `dspy-agent-skills`'
`drg-kg` extraction silently returns an empty graph with no LM configured). A
single bad field in the model's output — `PatchOperation("Append")` where the
enum is `APPEND`/`REPLACE` — crashes the whole run uncaught
(`dspy-optimizer:dspy_optimizer/optimizer.py:139-146`;
`dspy_optimizer/refiner/signature.py:134-137`), and block matching is a
case-sensitive prefix match that the Refiner's own worked examples
(upper-case headers) do not match the README's convention (mixed case)
(`dspy-optimizer:dspy_optimizer/strategies/merger/block_based.py:18-59`;
`dspy_optimizer/refiner/signature.py:19-24`).

**Mapping onto this repository.** Job 4 — optimizing a `SKILL.md` description —
is this exact problem, and `dspy-book-coding-agents` already shows the shape
this repository actually uses: `gepa.optimize_anything` over the whole file
text, evaluated by a mix of deterministic checks (weighted above any judge) and
a judge (`text-artifacts.md` has the mechanics; the one fact worth repeating
here is `dspy-book-coding-agents`'s own discipline for reading a result:
"print the regression list, and hand-restore what the optimizer discarded. Then
diff against your current file"
(`dspy-agent-skills:skills/dspy-book-coding-agents/SKILL.md:125-126`) — regression, not net delta, is what a promotion decision needs
(`dspy-agent-skills:skills/dspy-book-coding-agents/SKILL.md:116-130`)). The
self-critique-with-failure-history pattern (never propose the same rejected
fix twice) and worked examples living in the instruction rather than as demos
are both portable ideas independent of the rest of the loop.

**Verdict.** Taken: `MockLLM`'s shape and the callback event list
(`Plan/concept/dspy-toolchain_2026-09-23.md`). Refused: the block-patch loop
itself — validating on the training set, a free-text `operation` field that
crashes uncaught, and case-sensitive block matching are all exactly what P26
and P23 already rule out, and `gepa.optimize_anything` over the whole artifact
is the shape this repository has chosen instead. Kept: reading the
regressions before accepting a rewrite — the chapter's own heading, "Read the
regressions" (`dspy-agent-skills:skills/dspy-book-coding-agents/SKILL.md:116`).

---

## Prompting techniques

**Mechanism.** `dspy-advanced-prompting` packages eleven "techniques used by
top AI startups" as fifteen classes, twenty predictors — nineteen
`ChainOfThought`, one `Predict`, every field unannotated
(`dspy-advanced-prompting:src/techniques/*.py`, probe `S1`). The one technique
that is a mechanism rather than prompt text:

| technique | what carries the content | reaches DSPy's optimizable surface? |
|---|---|---|
| manager-style, role, task-planning, meta-prompting, thinking-traces, escape hatches | a rendered document (up to 7,329 chars) passed as an **input field** value | no — instruction-proposing optimizers rewrite `signature.instructions`, never an input value, so this text is resent unchanged on every call and cannot be optimized (`dspy-advanced-prompting:src/prompts/manager_style.py:184-210`, probe `S2`) |
| structured output | a schema rendered into an input field; JSON lives in an unschemed `str` output | no — DSPy 3.x's own answer is a `Pydantic`-typed output field, which this pack never uses (`dspy-advanced-prompting:src/techniques/structured_output.py:59,118-122`) |
| few-shot | examples formatted into an `examples` input field, `predictor.demos` stays empty | no — `LabeledFewShot`/`BootstrapFewShot` cannot see, select or replace them (`dspy-advanced-prompting:src/techniques/few_shot.py:97-124`, probe `S3`) |
| prompt folding, distillation | recursion/loop over hardcoded or constant "simulated" scores | no — the distillation evaluation calls the model, then reports `0.95 if is_teacher else 0.88`, marked `# Simulated`, whatever it answered (`dspy-advanced-prompting:src/techniques/model_distillation.py:257-288`, probe `S9`) |
| **few-shot's quality tiering (CHALLENGING examples first)** | `select_examples` takes up to two `CHALLENGING`-labelled examples before any `GOLD` ones | **yes, in shape** — this is a real demo-selection policy, not prompt text, and it is the one idea the toolchain design took: "demos include hard negatives … the one technique there that is a mechanism rather than prompt text" (`dspy-advanced-prompting:src/techniques/few_shot.py:16-20,42-47`; `Plan/concept/dspy-toolchain_2026-09-23.md`) |

**Code versus docs.** Ten of the eleven "techniques" are prompt engineering
with no DSPy mechanism under them at all — this is the finding, not a caveat.
Concretely: `ConditionalFolder` compares a free-text boolean as a string,
`.lower() == "true"`, so "True." and "Yes" both count as false
(`dspy-advanced-prompting:src/techniques/prompt_folding.py:196-203`);
`MetaPromptOptimizer.iterative_optimization` never runs the candidate prompt at
all — every case gets a hardcoded `quality_score=8.0`, so `best_prompt` is set
once, to the *input*, and never replaced across all iterations, spending two
real LM calls each anyway
(`dspy-advanced-prompting:src/techniques/meta_prompting.py:149-193`, probe
`S6`); escape-hatch confidence is a hedge-word lookup whose HIGH/UNABLE phrases
are written capitalised and so never match lower-cased text — "I don't know."
scores **0.95** confidence, the same as the guidelines' own recommended
admission phrasing
(`dspy-advanced-prompting:src/techniques/escape_hatches.py:60-96,161-203`,
measured); and an A/B "significance" test on five deterministic (cache-hit)
repeats of the same prompt produces `t ≈ 1e16` and reports "significant: True"
(`dspy-advanced-prompting:src/evaluations/evaluation_framework.py:403-445`,
measured) — P18 ("one attempt measures nothing… the cache must be off") stated
as a defect rather than a rule.

**Mapping onto this repository.** The canary pairs disqualify a candidate
that merges them on any fold. One of them, J5 `Negentropie`/`Entropie`, also
appears in the judgement ledger; before `model_rows()` it entered training
despite the stated holdout. The `labeled` rung now excludes it and reserves
two demo slots for other labelled lookalikes that are different terms. Unlike
the reference implementation, these examples are DSPy demos selected from
each training fold, not a rendered prompt string. Nothing else here transfers: this repository's
signatures are German where the model reads them and the output a person reads
is asserted German (`api.md`, P19), which sits in `signature.instructions`, not
in a rendered input-field document.

**Verdict.** Refused, ten of eleven, as prompt text with nothing DSPy-specific
under it. Taken: hard-negative demo weighting — already present, stricter, in
`pairs.py`.

---

## Schema as prompt

**Mechanism.** `dspydantic` optimizes Pydantic `Field(description=...)` text: a
per-field `ChainOfThought` rewrites one description at a time
(`field_name, field_description, field_type → optimized_field_description`),
and the metric plugs the rewritten schema into a **separate** extraction call
and scores that downstream result field by field
(`dspydantic:src/dspydantic/module.py:50-95`;
`src/dspydantic/optimizer.py:617-691`). Optimize a rewriter, score
downstream: the optimizer's demos and instructions belong to the rewriter,
but the artifact that ships is one rewriter output, judged by what it does one
step removed. Acceptance is coordinate ascent with a rolling baseline: fields
sorted deepest first, one compiled alone at a time holding the rest fixed,
accepted only `if new_score > baseline_score`, reverted to the original on a
tie that grew longer or a final score below baseline
(`dspydantic:src/dspydantic/optimizer.py:499-510,1124-1133,1505-1519`). And an
invariant is checked and reverted on violation, not merely hoped for: a
rewrite's placeholder markers are stripped after the call, duplicates
de-duplicated, and **the whole rewrite is discarded and the original restored
if any placeholder went missing**
(`dspydantic:src/dspydantic/module.py:286-365`, probe `I5`).

**Code versus docs.** The class's own docstring claims three techniques give
MIPROv2's proposer domain context "without bloating token usage", the first
being "Dynamic class name (0 extra tokens — replaces generic name)"
(`dspydantic:src/dspydantic/module.py:50-71`). **The class name reaches no
prompt in DSPy 3.3.1** — not the task call, not any MIPROv2 proposer call: a
five-predictor, `n=2` run put the docstring in 12 of 12 `proposed_instruction`
calls and the class name `OptimizeMedicalRecordFieldDescription` in 0 of 38
proposer requests and 0 of the 92 total
(`dspydantic:src/dspydantic/module.py:67-71`, probes `I4`, `v_proposer.py`).
Domain context has to live in the docstring or an input field — never a class
name — which is exactly what job 4's evaluator must assert about its own
candidate text (`SKILL.md`'s `description` field, not its filename). The
leakage bugs this pack's own maintainers found and fixed are worth reading in
full because every one of them scored something other than what was
shipped: validation data leaked into training through an off-by-one guard; an
empty validation set silently fell back to the training set; prompt-phase
candidates were scored against the *original* descriptions instead of the
phase-one optimized ones; and the baseline was scored **without** few-shot
demos while every later score included up to eight — so the commit's own "89%
→ 100%" number "was from demos alone, not description optimization"
(`dspydantic:src/dspydantic/optimizer.py`, commit `1afc528`, quoted from the
commit message). List-of-model fields score **1.0 regardless of content**,
because the field-aggregation walk only scores leaf paths and both a
completely wrong list and an empty list resolve both sides to `None`
(`dspydantic:src/dspydantic/evaluators/functions.py:437-446,551-553`, probes
`E`, `E'`) — P23's "a guard that covers less than it claims is worse than no
guard" with a number attached.

**Mapping onto this repository.** This is job 4's shape, named exactly:
optimize a SKILL.md's text, score it by a downstream call (a routing decision,
or `check_dspy_skill.py`'s own probes), never the class/file name for context.
`text-artifacts.md` has the mechanics of `gepa.optimize_anything`, which this
repository uses instead of `dspydantic`'s own per-field coordinate ascent
(GEPA rewrites the whole artifact under a metric; `dspydantic` cannot even
drive GEPA — its metric is three-argument and GEPA needs five). What is
catalogued regardless of which optimizer runs: the evaluator registry (a
pluggable `exact`/`levenshtein`/judge behind one interface, waiting for a
second evaluator actually in use) and choosing an optimizer from `n`
(`Plan/concept/dspy-toolchain_2026-09-23.md`, Layer 3).

**Verdict.** Taken as the shape for job 4: rewrite one artifact, score it one
step removed, never let the artifact's own name substitute for content in the
prompt. Catalogued: evaluator registry, optimizer-by-`n`. Left behind
entirely: every specific number this pack reports, several of which its own
maintainers found to be measurement bugs rather than gains.

---

## Applications: book use cases and advanced workflow

**Mechanism.** `dspy-book-use-cases` routes seven applications by task shape,
stated as a table this repository can reuse directly: one label with a fuzzy
boundary (sentiment) → few-shot demos carrying the label definition, not the
prompt; many fields from text with a gold answer (invoice extraction) → partial
credit plus per-field voting; private data behind narrow tools (customer
service) → a sandwich guardrail (cheap regex check → an injection classifier →
narrow tools → deterministic PII redaction, "the cheap check runs first so
most attacks cost nothing"); one question needing many lookups (news
researcher) → decompose, fan out in `Parallel`, "synthesize preserving
conflicts" — and it has no metric at all; numbers over long documents
(financial analyst) → code execution graded on the *trajectory*, because "a
right answer from bad reasoning is a latent failure"; text with no gold (blog
writer) → embedding distance to reference passages; an expensive, irreversible
call (video generator) → `dspy.Refine(module=ImageGenerator(), N=3,
reward_fn=image_reward, threshold=0.8)` gating the call, so only an image that
clears the bar reaches it
(`dspy-agent-skills:skills/dspy-book-use-cases/SKILL.md:22-37,74-87,100`;
`reference.md:6-20,92-100`). The routing rule condensed: gold answer → accuracy
or partial credit plus an optimizer; no gold → a judge or embedding reward
inside `Refine`; a lookup task → retrieval; an arithmetic task → code
execution with a deterministic parser inside the metric.

`dspy-advanced-workflow` states this repository's own method back, arrived at
independently: **"Step 0, not optional: the baseline… Without that number, no
optimizer result means anything"**
(`dspy-agent-skills:skills/dspy-optimizer-selection/SKILL.md:31-38`;
`skills/dspy-advanced-workflow/SKILL.md:160`) — the same rule `baseline.py`
already enforces by failing a candidate that does not beat the floor, not only
one that fell since the last row. `dspy-context-engineering-book`'s router is a
lookup table plus one `find()` function, alias first then substring, with
asserted counts pinning it against drift
(`dspy-agent-skills:skills/dspy-context-engineering-book/example_book_map.py:75-123`)
— the same shape `scripts/entities.py` and qmd's seven named collections
already are: routing by a table and a lookup, never by a model's free
judgement of which collection to search.

**Code versus docs.** PAT-10 in the modules skill states its own honesty gap
plainly: "The chapter contains no stage-level error handling at all: no
try/except, no fallback stage, no validation gate between stages… No module is
flagged as rarely worth using; the tour is uniformly positive"
(`dspy-agent-skills:skills/dspy-book-modules/SKILL.md:121-124`) — a caution
against reading any of these seven recipes as hardened rather than
illustrative. The invoice-extraction application is the strongest evidence for
"ship honest failures" in this whole file: its own committed benchmark "did not
reproduce the book's illustrative table", and the skill's verdict on that is
the practice worth copying: "Shipping that finding, in the repository, is the
practice to copy"
(`dspy-agent-skills:skills/dspy-book-use-cases/SKILL.md:57-63`). Its own gate
(`dspy-agent-skills:skills/dspy-book-use-cases/example_use_case_router.py:74-90`)
calls a judge only after a deterministic numeric parse both succeeds and
matches — but the parser itself keeps the percent scale, so a gold value stored
as a fraction never matches under a 5% tolerance and the judge is silently
never reached
(`dspy-agent-skills:skills/dspy-book-use-cases/example_use_case_router.py:61-71`,
measured) — the deterministic-gate-before-the-judge pattern is right; its own
worked example still has a units bug. And GEPA's own optimized instructions
memorised gold answers verbatim from the training rows in two of the three
committed runs (4 of 15 training answers appearing in one learned instruction,
0 of the held-out 10) — reading the instruction diff before accepting a GEPA
result is offered as the corrective, not a promise that GEPA generalises
(`dspy-agent-skills:examples/*/optimized_program.json`, measured against the
committed artifacts).

**Mapping onto this repository.** The routing table is this repository's own
shape for choosing a document, a collection, or a script — never a model's
guess. The gate-before-the-expensive-step pattern is the same shape as
`lmrun.py`'s approval requirement before any real model call: cheap,
deterministic checks first, an irreversible or costly step only after they
pass. "Grade the trajectory, not just the answer" is P1's "if it can be
programmatic, it is" applied to *how* an answer was reached, not only whether
it matches — relevant the day this repository scores a multi-step reasoning
chain rather than a single decision. The sandwich guardrail (cheap check →
classifier → narrow tools → deterministic redaction) is catalogued for the day
a model-facing tool here touches anything an untrusted source could shape.

**Verdict.** Taken as working method, not code: baseline-before-any-optimizer
(already `baseline.py`); routers as functions with asserted counts (already
`entities.py`/qmd); ship the honest, non-reproducing number rather than an
illustrative one (already `baseline.py`'s vetoed rows and `Plan/runs/README.md`'s
refusal to treat the first four censuses as a gold set). Catalogued: the
sandwich guardrail, gate-before-expensive-call, grade-the-trajectory — each
waiting for an instance this repository does not have yet.

---

## What the patterns share that is worth keeping

Across twelve programs and seven repositories, the same handful of shapes
recur, independently, enough times that they are worth naming once:

- **A metric must be shown to fail before it is trusted.** Six of the nine
  repositories ship at least one check that returns a perfect score on
  nothing — `dspy-advanced-prompting`'s edge-case/robustness/consistency/
  coverage axes default to 1.0, `dspydantic`'s LLM judges default to 0.5 on a
  parse failure, `dspy-optimizer`'s three validators pass an empty dataset,
  `dspy-agents`' baseline monitor accepts `score=0.0, total_calls=0` as a new
  baseline, `braid-dspy`'s critic passes a keyword-count tie, and
  `dspy-agent-skills`'s `drg-kg` extraction returns an empty graph, confidently,
  with no LM configured (`Plan/concept/dspy-toolchain_2026-09-23.md`). This
  repository's own founding defect was the retired pipeline's `coverage()`
  returning 1.0 on no gold fragments. `scripts/selftest.py` and
  `scripts/selftests.py` exist because of exactly this pattern, and
  `[checked: refine-none-when-all-fail]` is this file's own instance of it.
- **Closed action enums, never a free string the model types.** `braid-dspy`'s
  `PatchOperation("Append")` and `dspydantic`'s prefix-matched field paths both
  crash or silently mis-apply on a value outside a closed set; `dspy-clarify`'s
  and `Agentic-Dspy-Rag`'s routing decisions both fail silently on free text.
  This repository's answer, already built, is `pairs.py`'s
  `Literal["one-term", "two-terms"]`, which is unparseable rather than wrong
  when the model steps outside it (P26; `api.md` checks this against 3.3.1).
- **Review is never approval.** `dspy-deep-refine`'s `apply_actions` is
  "never called by the module"; `dspy-reflect-loop` promotes only after ≥ 2
  contexts *and* a human; `dspy-wiki-compile`'s program "never writes pages."
  This repository's version is P0 itself: promotion and user-facing flags are
  never a session's to make.
- **Suppression is visible, never silent.** The compounding-wiki-extension
  plan's own finding: "a suppressed finding never changes exit 0/1 silently;
  it changes it visibly"
  (`dspy-agent-skills:docs/compounding-wiki-extension-plan.md`, quoted in
  `Plan/concept/dspy-toolchain_2026-09-23.md`) — the same shape as P23's "never
  let 'could not check' collapse into 'checked'."
- **Decide by lookup wherever lookup suffices; a model only on the residual.**
  `dspy-wiki-compile`'s `create` is a lookup, not a judgement; this
  repository's `reconcile.py` already answers 68 of 109 candidates by lookup
  against `Wiki/index.json` before any judgement is spent, and `pairs.py`
  runs a rule first — `fold()`, or the plural rule of decision 010 — for the
  same reason.
- **Gate before the expensive or irreversible step.** The video generator's
  `Refine` before a paid render; `lmrun.py`'s `approval=` before any real
  model call reaches a third party.
- **Measure the exact artifact you ship, with the cache off, more than
  once.** `dspydantic`'s single-pass mode returned one sample and scored
  another, agreeing only through a warm cache; `braid-dspy`'s retries under a
  warm cache paid for one completion and reported three; the book's own
  invoice benchmark showed a baseline spread (0.205) larger than its reported
  GEPA gain (0.098) across three DSPy point releases. P18, restated by five
  different failures.

## What none of them may do here

- **Merge two readings into one text.** `dspy-wiki-compile`'s
  `ConceptDraft.definition` is one sentence per concept, across sources — the
  precise shape P13 forbids. A page holds every reading, attributed, and
  stops.
- **Infer an edge, or create a link the prose did not write.**
  `dspy-deep-refine`'s `insert_edge` and `dspy-agent-skills`'s `drg-kg` (whose
  `enable_implicit_relationships` defaults on) both propose graph edges a
  model chose. `Plan/decisions/005-the-wiki-links.md`: "A link is never
  inferred." `scripts/relations.py` derives the graph from `[[…]]` and
  nothing else.
- **Reward finding more contradictions, or let a count of conflicts read as
  progress.** `dspy-tetraframe`'s `contradiction_honesty` scores a run higher
  the more contradictions its cartography names. `CLAUDE.md`: "Conflict
  detection is never mechanised… a program that guessed would reproduce the
  `Zero-Trust` false conflict" (P14).
- **Let a source's own claim of authority resolve a disagreement.**
  `dspy-wiki-compile`'s `Resolution.supersedes` and every "gather step" that
  quietly drops a contested concept from its own contested count are the
  predecessor's defect in a new costume. `Plan/decisions/006-every-draft-is-back-in-question.md`:
  no document's date or claim to be canon retires another; a conflict is an
  agenda item for the author, never a program's ruling.
- **Let a model's self-report stand in for a deterministic check.**
  `dspy-wiki-compile`'s `truncated` flag is the model's own boolean, not
  anything that measured a cap; `dspy-autodialectics`' `harness_metric` scores
  the optimized program's own `Verify` output instead of a deterministic
  check; `dspy-deep-refine` grades its own destructive edits HIGH confidence.
  P1: "if it can be programmatic, it is." P26 already answers the specific
  case this repository has — a citation's line is asked for with `read.py
  --find`, never typed by a model.
- **Apply an edit, or promote a page, without a human decision recorded at
  that step.** Every one of the seven `dspy-agent-skills` knowledge-work
  skills that gets this right says so explicitly, and this repository's
  version is P0 stated once, at the top of `PRINCIPLES.md`, rather than
  per-skill.
