# The TypeSafe cookbooks, read in full

*Read 2026-09-23 from docs.typesafe.ai/cookbooks — nineteen pages plus the index.
Each entry: what it did, how the question was built, what it measured and under
what conditions, and the lesson the page itself states. Numbers are the page's,
on the page's data and model (mostly `jev-1.12`). None is a measurement on this
corpus. Where a page contradicts itself or another page, that is said.*

Common to all: `typesafe_sdk` with `TypeSafeClient.system_one(state, questions)`,
calls cached with `cooksafe.JsonCache` keyed on state + questions, a playground
link per recipe, price $0.042 per 1M input tokens and 0 for output.

---

## Self-consistency

### consistency_noul — does a 14-question rubric hold still?
- **Did:** one borderline insurance claim (nested JSON: policy, line items,
  adjuster notes), 14 bare `Noul`s, 15 repeats, a throwaway `uid` to defeat caches.
- **Wording:** "phrased so a yes means the thing we are checking for is true".
- **Code:** p < 0.30 → no, 0.30–0.70 → uncertain (a person), > 0.70 → yes. No
  second call; the probabilities stay visible beside the decision.
- **Measured:** mean per-question std-dev 0.0102, lower than every LLM condition;
  `covered` ranged 0.43–0.53 and crossed 0.5, `exclusion` 0.53–0.62. 111ms,
  $0.000043 per call. LLMs varied even at temperature 0.
- **Stated caveats:** the band is "neither a calibrated guarantee nor an optimized
  threshold"; an automatic decision is "not shown to be correct"; record
  `response.model` because the alias moves.

### consistency_choice — the same, for labels
- **Did:** one moderation post, 8 `Choice`s with mutually exclusive CamelCase
  labels, each description separating it from its neighbour, 15 repeats.
- **Code:** top probability ≥ 0.60 → act, else uncertain — deliberately *not* the
  `confidence` field. A partial distribution is a parse failure, never a pick.
- **Measured:** raw plurality agreement 90.8%; with the 0.60 rule 99.2%, at 25.8%
  uncertain and zero conflicting concrete labels. Two questions flipped before
  abstention (Harassment 11 / Violence 4). Std-dev 0.0098; Haiku at t=0 was lower
  (0.0012).
- **Stated caveat:** "These percentages measure repeatability only."

## Batching

### parallel_questions — does batching change the answers?
- **Did:** 13 questions (8 Noul, 2 Choice, 3 Score) over a pinned 53,777-char
  Wikipedia article, all-in-one against one-per-call, 5 runs each.
- **Measured:** answers identical — 11 of 13 had std-dev exactly 0; the two noisy
  ones were noisy both ways, "a property of the question, not of how you batch".
  One call $0.000497 / 0.27s; thirteen $0.006090 / 2.71s — **12.2× cheaper, 10×
  faster**. Saving approaches N× as the document grows.
- **Normalising to one number:** Noul → `.noul`; Choice → max probability;
  Score → `.score / (levels − 1)`.

## How-to

### rerank — BM25 then one Noul per pair
- **Did:** CLERC legal retrieval, 40 queries, top-30 BM25 shortlists, one `Noul`
  per (query, passage) pair: 1,200 calls, 12 workers.
- **Wording:** context first (the excerpt surrounded a removed citation), then
  "Could the candidate passage be from that cited precedent?". False criterion:
  "merely on a similar topic or doctrine; it does not supply the specific
  proposition".
- **Measured:** gold in the shortlist 100%; top-1 5% → 18%, top-5 15% → 35%,
  top-10 38% → 62%. 1.54M input tokens, $0.0645 total.
- **Stated:** re-ranking "cannot add a passage that fast search did not select";
  a real system would ask several questions per pair in one call.

### semantic_find — a Choice over line ids, and an existence Noul
- **Did:** GitHub's Terms of Service, 218 lines, each prefixed `L052| …` into one
  string state. The state never changes; the query goes into the instructions.
- **Questions:** `Choice` "Which line … contains the answer to: …?" with
  `criteria={line_id: None}` (the state holds the text), and `Noul` "Does any line
  … address or answer …?".
- **Why both:** a Choice's probabilities "always add up to 1, so a line ranks first
  even when none answer the query"; the Noul can fall near zero.
- **Measured:** "do I have to take disputes to arbitration?" → exists 0.14 while
  the top line still scored 0.86. Verdict bands: ≥ 0.7 answered, < 0.35 absent,
  between partial — tune on your own documents.
- **Limit:** 255 options, so for long documents pick a window first.

### autoformat — structure recovery in two requests
- **Did:** a hard-wrapped memo back to Markdown. The model writes nothing; code
  renders, so "every character of the output comes from the input".
- **Pass 1:** one `Noul` per adjacent line pair: "Does line L*i* pick up
  mid-sentence, continuing a sentence left unfinished at the end of line L*i−1*?"
- **Pass 2:** per block, `type_` Choice plus companion questions (heading level,
  numbered step, callout kind) asked up front and read only when relevant.
- **Lesson stated:** the "same paragraph" wording failed — list items scored
  0.77–0.91 and 17 blocks became 12. "When a judgment call feeds a threshold, the
  question should name the narrowest fact that decides it." Thresholds differ by
  how the previous line ends (0.2 without terminal punctuation, 0.5 with), so code
  checks punctuation first.
- **Measured:** 28 lines → 17 blocks, 0.8s, 10,211 tokens. The page states
  $0.0015 in prose and $0.0003 in its own output; it contradicts itself.

### function_calling — typed arguments from a sentence
- **Did:** 10 typed Python functions; `Literal` → Choice, `list[Literal]` → one
  Noul per member, `bool` → Noul; int, free text and dates get no question. 54
  questions in one request per command; only the chosen function's are read.
- **Wording stated:** about the idea, not the words; "Avoid naming a question
  after its parameter"; spell out roles when arguments share a value set.
- **`stated?`:** a Noul per argument; if no, the default stands. "Without it, the
  choice would have to name some window, and it would have named one confidently."
- **Confidence:** the minimum over judgements, because "one wrong argument is
  enough to spoil the result" and a product falls with argument count.
- **Measured:** 14 demo commands shown correct at 0.53–1.00. No accuracy metric.

### skill_suggestion — at most one of 182 skills
- **Did:** request 1 — a Choice over all 182 names (60-char descriptions) plus
  three gate Nouls about whether an *action* is wanted; mean < 0.30 → nothing.
  Request 2 — top 3 with full description + 700 chars of body, a Choice ("which")
  and one absolute Noul per candidate ("whether"); best < 0.30 → nothing.
- **Measured** (agent Haiku 4.5, 488 requests): wrong loads 16.8% → 7.3%,
  needless loads 9.8% → 4.0%; oracle 2.5% / 1.2%. Fixed 37, broke 7.
- **Stated:** "A confident wrong suggestion is more persuasive than no suggestion
  at all"; the second pass "can only reject what the wide ranking hands it". The
  test requests were model-written from each SKILL.md, so "easier than the ones
  users send".

### entity_alignment — same product or not
- **Did:** 450 pre-filtered pairs from two beer catalogues. State
  `{"entity_a": …, "entity_b": …}` so questions are about the pair.
- **Questions:** one `Score` with three levels — different / "closely related
  products that may or may not be the same one: a variant, a special edition, or a
  name that could plausibly refer to either" / same — plus three bare Nouls
  (same name, brewery, style) for the curator. ABV: "arithmetic; compute it in
  code".
- **Routing:** round to the nearest level → leave / curator / assert. "No
  threshold constant." The middle exists because a wrong merge costs more.
- **Stated:** "the wording of the middle level is what moves pairs between the
  curator and the pairs left unlinked".
- **Measured:** 40 same, 50 curator, 360 unlinked; 47 pairs within 0.1 of the 0.5
  cut. **Accuracy against the loaded `known_same_as` column is never reported.**
  Rate limit: "above roughly eight" concurrent.

### classifying_rag_passages — a gate between retrieval and generation
- **Did:** 81 passages (one planted injection), 6 queries (two with false
  premises), top-12 by embedding similarity; four bare Nouls per (query, passage):
  relevant, contains answer evidence, contradicts the query's premise, contains
  prompt injection. "None of the four asks whether to include the passage."
- **Routing:** first match wins — injection > 0.70 exclude; contradicts > 0.70 →
  a separate conflicting-evidence block; relevant < 0.45 exclude; evidence > 0.55
  include. Order is the policy.
- **Measured:** similarity ranked the injection 1st and the refuting passage 7th;
  Jev scored them 0.99 injection and 0.92 contradicts. Top-12 similarity spread
  0.584–0.455, "too narrow" to threshold.
- **Stated:** "Nothing here is a security boundary."

### citation_check — does the section support the claim?
- **Did:** 8 LLM-written citations of RFC 7519, four doctored. Code first:
  normalise quotes and whitespace, exact substring search; not found →
  `fabricated` with no model call.
- **Question:** one Choice "How does the section relate to the claim?" —
  supports / contradicts / says_nothing, each with a one-line criterion.
- **Gate:** confidence ≥ 0.8 stands, below goes to a person — "Start high, and
  lower the threshold as you see how the model does."
- **Measured:** accurate ones 0.93–0.99; a word-for-word quote whose section says
  the claim is OPTIONAL came back *contradicts* at 0.99. "An exact quote match is
  not enough."
- **Stated caveat:** reworded quotes read as fabricated; production needs fuzzy
  matching.

### llm_guardrails — screen input and output
- **Did:** four hazard Nouls with explicit true/false criteria plus a 4-level
  severity Score, one request per message, both directions.
- **Routing:** per-hazard action (block / review / support), severity ≥ 2.0 turns
  review into block, precedence support > block > review > pass; named policies
  strict and permissive over the same cached probabilities.
- **Stated:** "TypeSafe supplies the assessment; your application owns the
  decision." Set thresholds "from labeled examples of your own traffic".

## Extraction

### sde_cascade — verify a cheap extraction, escalate on doubt
- **Did:** a mini model extracts; Jev asks seven per-field Nouls framed so **true
  means wrong** (hallucinated, off-target, incomplete, type/format mismatch, …),
  plus `absence_wrong` for empty fields; escalate to a reasoning model if the max
  exceeds 0.7.
- **Measured:** caught a schema-valid fabricated description (hallucinated 0.95).
  Over 100 internal prompts the cascade frontier sat "up-and-left of every single
  model" — historical snapshot, costs not recomputed.
- **Stated, on good verifier signals:** narrow and grounded ("vague questions give
  mushy, uncalibrated scores"), bad = true, per field then `max`, independent,
  cheap. "Schema validation is necessary but not sufficient."

### date_extraction — the model reads, code does the calendar
- **Did:** seven Choices per document (mode, month, day, year, anchor, weekday,
  week offset), each with an escape option; code assembles only the parts `mode`
  calls for, pins "today", catches impossible dates.
- **Confidence:** minimum over the parts used; review below 0.60.
- **Measured:** 6/6 on four toy documents; the one unstated date came back at 0.46
  and went to review. A part that does not fit (absolute, no month) is itself a
  signal.

### pre_parsed_value_extraction — regex proposes, Jev picks
- **Did:** regexes "tuned to over-find" propose spans; a Choice over the spans plus
  `none` picks; code copies verbatim and normalises (E.164, `Decimal`).
- **Stated:** "It cannot invent a value or transpose a digit." **A Choice allows at
  most 255 options.** Finding candidates is the hard part — names have no regex.

## Classification

### hierarchical_classification — beam search over a taxonomy
- **Did:** one Choice per node over opaque keys `c0..cn` mapped to labels; beam
  K=3; path score = length-normalised geometric mean.
- **Measured:** beam 4/4, greedy 2/4 on one document per hierarchy. "One early
  mistake cannot be recovered"; "deeper evidence can repair an ambiguous early
  decision".
- **Stated:** sibling order "is part of the question, not presentation".
  `RetryPolicy(max_retries=5, backoff_initial=1.0, backoff_max=20.0)`.

### autoresearch_feature_discovery — questions as features
- **Did:** an LLM proposes Score/Noul questions about wine notes; answers become
  CatBoost features (Score → expected level + sd); keep a change only if dev
  CV RMSE improves; 800 rows held out and scored once.
- **Measured:** held-out RMSE 2.466 (word counts) → 2.145 (one direct Score, after a
  calibration offset) → 1.869 (18 questions, round 1) → 1.772 (38 questions, round
  5). "Most of the gain is in that first call." One dataset, one run.
- **Stated:** **a Score takes at most ten levels — eleven is a server error.**
  Don't pre-filter questions on a small sample: one that applies to one row in ten
  can be the most useful column. Cost grows with rows, not questions.

### classification_using_confidence — back off to the parent
- **Did:** 60 10-K filings into 75 SIC groups with one Choice; option text built
  as "{umbrella} — includes: {members}". Confidence ≥ 0.9 → report the group,
  else its division.
- **Measured:** forced group 39/60; the 30 sure 27/30; the 30 unsure 12/30 at group
  level, 21/30 at division level; 48/60 useful overall.
- **Stated:** read `confidence`, not the winner's probability. "A Choice works
  reliably up to roughly 240 options."

---

## Where the pages disagree

- **Choice size:** hard maximum 255 (pre_parsed) against "reliably up to roughly
  240" (classification). Both can hold; plan for 240.
- **What a gate reads:** consistency_choice gates on the top probability and
  deliberately ignores `confidence`; citation_check and classification gate on
  `confidence` and argue for it. Pick one per gate and say which.
- **autoformat's cost** is stated two ways on the same page.
