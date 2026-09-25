# What a run writes, exactly

Nine files. Five of them are written by a script and four by a person. Each one
is read by something later, which is why the shape matters.

## `Plan/runs/<slug>/` — the run

| file | written by | what it is |
|---|---|---|
| `01-profile.txt` | `capture.py <slug>` | structural facts, deterministic |
| `02-probes.txt` | `capture.py <slug>` | export damage and surface families |
| `03-candidates.md` | **a reader — a person or the session — while reading** | the gold list, when `scripts/gold.py` rules it so |
| `04-counts.txt`, `counts.json` | `capture.py --count` | two numbers per term, plus surfaces |
| `reconcile-pre.json` | `reconcile.py <slug>` | lookup versus judgement |
| `reconcile.json` | a person | what the run left |
| `03-candidates-rlm.md` | `rlm_ingest.py` | a model's list. **Never gold**, and never merged into the file above |
| `run.md` | a person, when there is something to say | timings, and what is missing. **No script writes it** — `capture.py`'s docstring claimed it did, in three places, and no run had one |

`03-candidates.md` opens with `written_by:` and is one `- term` per line. A
model's list is a **different file**, `03-candidates-rlm.md`, and says so on its
own first line — `state.py` reads that line, because the test it replaced („does
the head contain 'reconstruct'") passed a model's list and failed a list whose
prose denied being a reconstruction. A prose section is allowed and is
filtered out — only `- term` lines count, which was learned when nine sentences
from an „open while reading" section were counted as candidates and reported at
0 occurrences, a shape indistinguishable from a term the document turned out not
to contain.

## `reconcile.json`

`account.py order` reads `state_before` and `state_after` and checks that each
run started from the state the previous one left.

```json
{
  "document": "<slug>",
  "drive_id": "<from the manifest, never typed>",
  "step": "reconcile",
  "at": "YYYY-MM-DD",
  "by": "hand, after scripts/reconcile.py pre-classification",
  "state_before": {"pages": 46, "conflicts": 4},
  "state_after":  {"pages": 46, "conflicts": 4},
  "pre_classification": {
    "candidates": 51, "decisions": 65,
    "decided_by_lookup": 35, "needs_judgement": 30
  },
  "new_terms": [],
  "why_no_new_terms": "<required when new_terms is empty — zero pages is a decision, not an omission>",
  "new_readings": [
    {"page": "<slug>", "lines": [49, 50, 272], "attribution": "premise",
     "note": "<what this document adds to that page>"}
  ],
  "new_surfaces": [], "new_conflicts": [], "conflicts_changed": [],
  "questions_changed": [], "judgements": ["J31", "J32"],
  "not_promoted": [], "found_by_rule_not_by_census": [], "baseline_moved": false
}
```

`decisions` may exceed `candidates`: one term can raise several judgements.

`not_promoted` is where a candidate that matched no page and did not become one
is recorded, with its lines — so the next document that actually *defines* the
term opens its page with a reading already attached, instead of starting from an
occurrence.

## A judgement row — `Plan/runs/judgements.jsonl`

One line per decision a lookup could not settle. `judgements.py` replays every
row against the current code.

```json
{"id": "J1", "surfaces": ["Die Konstrukt-Stadt", "Konstrukt-Stadt"],
 "decision": "one-term",
 "env_features": ["near-match:intra-list", "german-article-prefix", "worldbuilding"],
 "goal": "one term or two?",
 "action": "compare referents; check whether the prefix appears in any cited name",
 "result": "one term — a German definite article is never a term boundary",
 "rule": "strip leading der/die/das before folding",
 "mechanised_by": "wiki_index.fold",
 "success": true, "document": "<slug>", "at": "YYYY-MM-DD"}
```

`rule` is the field that earns the row its keep. „These are the same" teaches
nothing; „a German definite article is never a term boundary" can be mechanised,
and then `mechanised_by` names the function that claims the case and
`judgements.py` replays it forever. A row with no code claiming it stays
`judgement` — that is a normal outcome, not a gap.

**Known gap, stated rather than hidden:** a row records its rule and not its
*evidence*. The numbers exist in `counts.json`; nothing carries them into the
row, so the evidence of every judgement is prose in a note. This is what blocks
training a model on the ledger, because an optimizer learns from what is in the
input.

## A sweep row — `Plan/runs/sweep.jsonl`

One line per page the sweep found in a document's text that the census did not
list (decision 012). `reconcile.py --sweep-open` counts a hit as open until the
page reads the document or a row here says why it does not.

```json
{"document": "<slug>", "page": "emergenz", "surface": "Emergenz", "line": 100,
 "decision": "reading",
 "why": "Kairos' domain — the page keeps Emergenz on a world as well as on AEGIS",
 "at": "YYYY-MM-DD"}
```

`decision` is `reading` (the page now carries it, committed naming the document)
or `occurrence` (a title, a reference, the word in another sense, a term the
document's own rule keeps out). `why` says which, in words.

## `Sources/terms/<slug>.md` — the census

Frontmatter from `profile.py --frontmatter`, never typed:

```yaml
source: Sources/drive/<slug>.md
drive_id: "<id>"
title: "<title>"
category: <cat>
index_date: "YYYY-MM-DD"
extracted: "YYYY-MM-DD"
candidates: <n>
```

Then the structural profile, the stance read per passage, and the candidates
with their counts. **It describes one document and nothing else** — no count,
comparison or expectation from another source, which is what makes reconciliation
safe.

## `Sources/notes/<slug>.md` — the note

Same `source:` line, which is how a bare `^[Lnn]` on the page resolves. Adds
`read:`, `stance_markers:`, `stance_marker_count:` and `reads_as:`.

Stance is read per passage and is **not** a document type. There is no enum of
document kinds: how a document came to be says nothing about how it is built, and
a single document holds several stances and usually marks them itself.

## `Wiki/compare/reconcile-NN-<slug>.md` — the prose record

Frontmatter carries `document`, `against`, `ran`, `candidates`, `decisions`,
`by_lookup`, `judgements`, `new_pages`, `new_readings`. The body says what
happened and, when the answer was „nothing", **why nothing was the right
outcome.** The record is per document and append-only; the first three
comparisons were full re-comparisons and each superseded the last, which is the
step telling us it did not scale.

## And a page, if the document earned one

`Wiki/candidates/<term>.md` collects every source's reading of one term,
**attributed and unmerged**. Where sources disagree the page says so and stops.
One page changed is one commit, and its first line names the source document.
