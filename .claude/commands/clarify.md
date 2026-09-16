---
description: >-
  Precision gate for statements: rewrite a research claim, an open question or
  a task statement so scope, terms and assumptions are explicit without adding
  or losing meaning, and turn every remaining ambiguity into a question for the
  author. Mandatory before /promote-to-canon; use whenever accuracy is required.
  Usage: /clarify [Wiki page or claim text | question | task statement]
argument-hint: "[wiki page path, claim text, or the statement to clarify]"
---

# Clarify — say exactly what the source says, ask about the rest

The gate applies the `clarify` principle (reveal intent, make the implicit
explicit, add nothing, never change meaning) to statements. It is the
DSPy program `tools/kpwiki/clarify.py` (`ClarifyGate`, skill `dspy-clarify`)
plus a human decision. Rule 0 as a program: what the source does not settle
becomes a question, never an assumption.

## Step 1: Collect the inputs (deterministic)

- `claim_text` — the statement, verbatim (German stays German)
- `source_excerpt` — the cited lines from `Sources/drive/<slug>.md`
  (`^[file:L-L]`); widen to the paragraph when the claim spans lines
- `entities` — the claim's entity list from the source page
- `glossary_terms` — codex slugs from `Codex/glossary/<kind>/<slug>.md` (or
  `match_codex_entries(novel_id, claim_text)` when the engine is up)
- `canon_context` — matching Canon passages via `scripts/wiki_fts.py search`
  (binding and conflict awareness only; the gate never rewrites from canon)

## Step 2: Run the gate (dry-run; nothing is written)

```bash
.venv-dspy/bin/python -m tools.kpwiki.clarify_cli --claim "<text>" \
    --source Sources/drive/<slug>.md:<start>-<end> --entities AEGIS,Kael \
    --glossary aegis,kael [--canon-context-file <file>] [--dry-run]
```

`--dry-run` prints the assembled inputs without an LM call (needs no key).
The live run prints the `Clarification` as JSON, the metric score, whether it
is promotable, and the feedback. Read the `Clarification`:

| field | meaning |
|---|---|
| `clarified_text` | same claim, explicit; must score ≥ 0.9 on `clarify_metric` |
| `scope` | Kernwelt / Akt / Anteil — only where the source states it |
| `assumptions` | what the text needs that the source does not say |
| `ambiguities` | phrase · readings · question — the author's decisions |
| `bindings` | mention → codex slug |
| `verdict` | `clear` · `needs-author` · `not-promotable` |

## Step 3: Act on the verdict

- **`clear`** → the clarified text replaces the claim on the wiki page (status
  stays `draft` until `/wiki-promote`); it may enter `/promote-to-canon`.
- **`needs-author`** → each ambiguity becomes a `Wiki/questions/` page
  (axis `incorrectness` when readings conflict with Canon, else
  `incompleteness`); AskUserQuestion for the ones that block current work.
  Never answer them yourself.
- **`not-promotable`** → the statement is not a claim (instruction, question,
  fragment) or contradicts its own citation; leave it on the source page, mark
  `canon_relation: unrelated`.

## Step 4: Record

Append `## [YYYY-MM-DD] clarify | <slug> | verdict=<v> score=<s>` to
`Wiki/log.md`; questions carry `evidence` citations. When the author answers a
question, the answer goes to the decision log (D-xx) and the claim is
re-clarified with the answer as `canon_context`.

## Rules

- Never resolve an ambiguity the source does not resolve; ask.
- Never pull scope or quantifiers from Canon into the claim — that is a
  conflict to report, not a correction to apply.
- A score below 0.9 is not promotable regardless of verdict; the feedback names
  what to fix.
- German claims stay German; questions to the author may be German or English.
- Also for non-claims: a vague task statement before `dspy-rlm-workflow`
  decomposition, a query before `dspy-deep-refine`, a correction before it
  becomes gold in `dspy-reflect-loop`.
