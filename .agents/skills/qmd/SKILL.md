---
name: qmd
description: Search and read this project's German corpus with qmd — which collection answers which question, why search is 0.24s and query is 14.5s, and the rule that a search result is never a number. Use when looking for a passage, a term, a decision already made, or when a search returns less than it should.
allowed-tools: Bash(qmd:*), Bash(scripts/setup_qmd.sh:*), Bash(python3 scripts/qmd_coverage.py:*)
---

# qmd, for this corpus

`qmd` indexes this project's markdown and answers a German phrase with a file
and a line. It is a **place to look**. Every number that goes into a page or a
learning comes from `corpus.py`, `duplicates.py` or a count — never from a
search result. That rule is in `CLAUDE.md` and it is the one this skill exists
to keep.

For the package's own version-matched instructions: `qmd skill show`.
For the full command and flag surface, read `references/commands.md`.
For how the setup is built and restored, read `references/setup.md`.

## Two rules that decide more than the command does

**1. qmd ranks; it does not enumerate.** `Kernwelt` occurs in **144 of 346**
source documents. A 40-hit list cannot be a census of that, and the document
that carries the one line you want may not be in it — measured: the line that
defines `KW1` is at line 152 of its document and does not appear in the top 40,
because **BM25 favours short, early chunks**. The top hits for that query sat at
lines 3, 26, 25, 16, 11.

So: „which documents contain X" and „where in this document" are `grep`,
`corpus.py` or `capture.py --count`. qmd answers „where should I look first".
This is the mechanism behind `CLAUDE.md`'s rule that a search result never
becomes a number.

**2. The language of the query is decided by the collection, not by you.** Canon
is German and engineering is English, so the two halves of the repository are in
two languages:

| collection | query it in |
|---|---|
| `sources`, `census`, `notes` | **German** — that is what the documents are |
| `decisions`, `plan` | **English** — reconciliation records, judgements and concept notes are written in it |
| `wiki` | **both** — English prose around German quotations |

Measured: `„Plural Flexion Term Grenze"` against `decisions` → **0 hits**.
`„plural inflection term boundary"` → **1 hit at 0.92**, the right one.

## Pick the collection first, the query second

Seven collections, named for **purpose** rather than folder.

| ask it when you want | collection |
|---|---|
| a passage in a source document | `sources` |
| what a term page, conflict or question already says | `wiki` |
| every candidate term one document proposed | `census` |
| what one document was read as saying, quoted | `notes` |
| concept notes, decisions, learnings, run artifacts | `plan` |
| **what has already been decided, and why** | `decisions` |
| any layer, when you do not know which | `all` |

`decisions` and `all` are **excluded from default queries** because they overlap
the others — name them explicitly with `-c`.

### Why these seven, and what would justify an eighth

A collection is not a folder with an index attached. It is **a question someone
asks often enough that the answer should not be diluted by everything else.**
Five of the seven happen to be one directory, and two are not: `decisions` spans
five directories, and `all` spans the repository minus the shelf.

The test for a new one is the same test twice:

- **Would a query into it return something a query into an existing collection
  buries?** `decisions` earned its place that way: reconciliation records,
  conflict records and the judgement ledger live in three different directories,
  and a search for „what did we decide about plurals" against `wiki` or `plan`
  drowns in 46 term pages and 40 concept notes.
- **Does it overlap? Then exclude it from default queries.** Two collections
  covering one file means that file answers twice, and the second answer is
  noise. `decisions` and `all` are both `includeByDefault: false` for exactly
  that reason.

**Do not add a collection for a directory just because the directory exists.**
`qmd_coverage.py` already guarantees every file is in *some* collection — that
is a different guarantee, and the one that matters for „nothing is silently
unsearchable".

One collection this project does **not** have and deliberately: a per-document
one. The question „what does document N say about X" is answered by opening the
document, and a ranked list would only hide that it is 620 lines long.

`decisions` is the one worth reaching for first: it spans the reconciliation
records, conflict records, question pages, `Plan/decisions/` and the judgement
ledger. Eight reconciliation records alone are ~950 lines, and a hit plus
`qmd get` reads a dozen.

## The cases this project actually has

Every row measured. `-c` is never optional.

| what you want | command | worked |
|---|---|---|
| **which document might settle an open question** | `qmd search "Guardian autonom Werkzeug AEGIS Agent" -c sources -n 5` | yes — 0.80, top hit, and it is the document that was chosen |
| **has this already been decided?** | `qmd search "plural inflection term boundary" -c decisions -n 4` | yes — 0.92, straight to the judgement. **In English** |
| **where does a term show up across layers** | `qmd search "Prä-Entropie" -c all -n 4` | yes — the ledger, the candidate list and the source, three hits, exactly right |
| **is this document a near-copy of another** | `qmd search "<its title words>" -c sources -n 5` | yes — this is what first exposed the duplicate exports |
| **what does this page already say** | `qmd search "<term>" -c wiki -n 3` | yes |
| **read around a hit** | `qmd get "qmd://decisions/Plan/runs/judgements.md:273:12"` | yes — twelve lines instead of a 950-line record |
| **what is in a collection at all** | `qmd ls wiki/questions` | yes — size and mtime per file |
| **several files at once** | `qmd multi-get "qmd://census/*.md"` | yes |
| **where in THIS document is X** | — | **no. Use `grep -n` or `capture.py --count`** |
| **how many documents contain X** | — | **no. Use `corpus.py` or `grep -rl`** |
| **does a term already have a page** | — | **no. `reconcile.py` reads `Wiki/index.json`**, and must stay `O(census) + O(judgement)` |

## Three search commands, and the difference is not small

```bash
qmd search "blinder Fleck kategoriale Unfähigkeit" -c sources    # 0.24s, BM25, no model
qmd query  "blinder Fleck kategoriale Unfähigkeit" -c sources    # 14.5s, expands + reranks
qmd vsearch "Wächter am Tor" -c wiki                             # vectors only
```

**Use `search` by default.** It is BM25, runs no model, and for a corpus of
coined German compounds an exact term is usually what you have.

`query` runs a 1.7B expansion model and a 0.6B reranker on CPU — this container
has no GPU and says so. **14.5s, measured on a query never asked, twice.** A
repeated query returns in 0.24s from the index's `llm_cache`, which is how „about
0.2s" once got written down as a general claim. Never put `query` in a loop.

`vsearch` needs embeddings. `scripts/setup_qmd.sh --check` reports how many are
pending; while any are, `vsearch` returns „No results found" **with a warning
and exit 0** — it looks like an answer.

## Writing a query for German

The corpus is full of coined compounds, and that changes what works:

- **Lowercase is fine.** Matching is case-insensitive.
- **Do not grep for capitalised words** to find terms — German capitalises every
  noun, so the signal is nil.
- **A compound is its own token.** `Entropie` does not match `Entropiegewinn`;
  they are separate tokens in the index. Search for the compound you mean, or
  for both.
- **Structured queries** let you say which leg does what:

```bash
qmd query $'lex: Kern-Welten Guardians\nvec: wer bewacht welche Welt'
qmd query $'hyde: Jeder Guardian ist einer Kernwelt zugeordnet.'
```

`lex:` is BM25, `vec:` is vector similarity, `hyde:` embeds a hypothetical
answer. **`vec:` and `hyde:` contribute nothing until embeddings finish.** A
plain single-line query is implicitly `expand:` and runs the expansion model.

## Read the hit, not the snippet

```bash
qmd search "Wächter" -c decisions -n 3
qmd get "qmd://decisions/Plan/runs/judgements.md:273:12"
```

`get <ref>:<from>:<count>` prints numbered lines, with the collection's context
above them. That is the loop worth learning: **search to find the line, `get` to
read a dozen lines around it** instead of the whole file.

`multi-get` takes a glob or a comma-separated list when you need several.

**`--files` is not as compact as it looks.** It prints
`#docid,score,qmd://path,"context"` — and the context is this project's, which
runs to several lines. For a machine-readable list, `--json` and pick the three
fields you want:

```bash
qmd search "Prä-Entropie" -c all -n 5 --json | python3 -c "
import json,sys
for h in json.load(sys.stdin): print(f\"{h['score']:.2f} {h['file']}:{h['line']}\")"
```

## From Python

```python
from qmd import search, get          # scripts/qmd.py
for hit in search("blinder Fleck", collection="sources"):
    doc = hit.document()             # subject.Document when the hit is a landed source
```

`scripts/qmd.py` parses `--json` once and resolves `qmd://collection/path` to a
real `Path` once. **A `Hit` says where to look and carries no claim about the
corpus**; `hit.document()` is the handoff back to the tools that measure.

## Where `query` earns its 14.5s, and where it does not

`search` fails in one shape: **a term that is common, buried mid-document, or
that you can only describe rather than name.** Case 2 above is the example —
„Kernwelt Logik LogOS" returned four documents and none was the one that
carries the line.

That is what `query` is for, and it is the only thing worth paying 14.5s for:

```bash
qmd query $'intent: which Kern-Welt is LogOS assigned to\nlex: Kernwelt LogOS\nvec: welcher Guardian gehört zu welcher Welt'
```

Write the structured form rather than pasting the question — `lex:` carries the
coined compounds that must match exactly, `vec:` carries the paraphrase. **Until
embeddings finish, the `vec:` and `hyde:` lines contribute nothing**, so during
that time a structured query is a slow `search`.

Never put `query` in a loop, and never use it where `search` already answers.

## When a search returns less than it should

```bash
scripts/setup_qmd.sh --check       # package, config, collections, embeddings, coverage
python3 scripts/qmd_coverage.py    # non-zero if a directory is in no collection
qmd update                         # re-index after files change
qmd doctor                         # device diagnostics — here: 4 math cores, no GPU
qmd cleanup --dry-run              # what stale records would go
```

`cleanup` is worth a dry run after anything that removes files: after the
duplicate exports were folded away it reported **126 inactive document records**
still in the index. It also clears the `llm_cache`, which is what makes a
repeated `query` fast — so a cleanup makes the next one slow again.

**A file in no collection is absent from every search and nothing says so** — the
search just returns less and looks like it worked. That is why coverage is
checked rather than remembered.

Two more silent failures worth knowing:

- **Running `qmd` outside the project queries a different, empty index.** The
  config is found by walking up from the working directory. `cd` to the
  repository root first.
- **`.qmd/index.yml` is committed and `qmd init` overwrites it.** Never run
  `init` here. If the file is missing, it is a restore: `git checkout .qmd/index.yml`.

## What this skill will not do

- Turn a search result into a number. Ranked results are a place to look.
- Replace `Wiki/index.json` in reconciliation, which must stay
  `O(census) + O(judgement)` and never scan the corpus.
- Run `qmd bench` before embeddings exist — it would measure their absence, and
  score the `vector` and `full` backends near zero by construction.
