# Every script, its surface, and what it leaves behind

The pipeline is scripts, not commands. This is the full surface; the loop that
orders them is in `SKILL.md`.

## The verb

```bash
python3 scripts/account.py <document|term|pair|corpus|order> [id]
```

One operation at several scales. `order` takes no id and answers whether the
pipeline's dependency order holds — it is the check that refuses to pass while
any document is half-processed.

## Per document

| command | writes |
|---|---|
| `read.py <slug> [--from N --to M]` | the document to stdout, each line prefixed `NNN\|` |
| `read.py <slug> --find "<words>"` | `^[Lnn]`, or a refusal naming the nearest lines — exit 1 |
| `capture.py <slug>` | `Plan/runs/<slug>/01-profile.txt`, `02-probes.txt`, `probes.json`, and a `03-candidates.md` header if none exists. No script writes `run.md` |
| `capture.py <slug> --count` | `04-counts.txt`, `counts.json` — refuses without `03-candidates.md` |
| `profile.py <slug>` | structural facts to stdout |
| `profile.py --frontmatter <slug>` | the census header, drawn from the manifest so no identifier is ever typed |
| `reconcile.py <slug>` | `Plan/runs/<slug>/reconcile-pre.json` and a printed classification |
| `agree.py <slug> [<a.md> <b.md>] [--names]` | nothing — every `03-candidates*.md` in the run, or two lists, compared pairwise: F1, containment both ways, surfaces held only inside a longer one, forms the document does not write |

`read.py` serves the same text in both directions and neither stores anything:
the numbers it prints are **file** lines, the ones a citation names, and `--find`
asks exactly the question `quotes.py` will ask later, through the same
`missing_part` on the same normalised line. So a citation `--find` produced
cannot fail the check. When it refuses it says why — the words are on no single
line, or they span two, which cannot be cited at all because the line number is
part of the claim.

`04-counts.txt` reports each term **twice** — standing alone, and including
compounds — because one number cannot answer it in German, and lists the
inflected surfaces found. A term at `0 word` is written differently here, not
absent.

## Corpus-wide

```bash
python3 scripts/corpus.py <count|timeline|cooccur|first|where|family|plan> <term>
python3 scripts/duplicates.py [--term T] [--threshold F] [--groups]
python3 scripts/dedupe.py [--apply]              # default is a dry run
python3 scripts/derive.py                        # apply every rule, cached by (sha256, rule VERSION)
```

`corpus.py` answers from the derived index without reading a document.
`duplicates.py --term` counts a term both ways, over files and over documents.

```bash
python3 scripts/entities.py verify [<slug> ...]    # a model list's cited lines, 90% or it is a reconstruction
python3 scripts/entities.py search <entity> [...]  # multi-word, across line wraps, hyphen compounds counted
python3 scripts/entities.py matrix                 # every verified entity × every document -> Plan/derived/
python3 scripts/entities.py missing [--min-docs N] # used in N+ documents, folds to no wiki surface
python3 scripts/entities.py doc <slug>             # the entities one document uses
python3 scripts/entities.py score <slug>           # against a reader's 03-candidates.md, two difference lists
python3 scripts/entities.py selftest               # token matcher == \bterm\b
```

`entities.py` reads `Plan/entities/<slug>.md`, written by the saved workflow
`.claude/workflows/entity-lists.js`. A list is a model's proposal; every number
comes from the search. Its counts include hyphen compounds and `corpus.py`'s do
not — compare neither to the other.

## Checks

```bash
python3 scripts/state.py [--prose|--check|--get KEY]
python3 scripts/quotes.py [FILE ...]
python3 scripts/judgements.py [--open|--render]
python3 scripts/qmd_coverage.py
python3 scripts/sources.py check
python3 scripts/selftest.py
python3 scripts/relations.py
python3 scripts/trainset.py
```

- `state.py` with no flag derives everything and writes `Plan/state.json`.
  `--prose` reads every `.md` outside `Legacy/` and fails on a stale number.
- `quotes.py` with no argument checks the repository; with a file, that file.
  It reports **unresolved** and **uncheckable** separately and never conflates
  them.
- `judgements.py` re-renders `Plan/runs/judgements.md` on every normal run, so
  the searchable copy cannot lag behind the `.jsonl` it derives from.
- `relations.py` derives the page graph from `[[slug]]` links, the orphans, the
  open statements harvested from every page's Open section, and `--unmarked`:
  where a page writes another page's term in prose and does not link it. A
  backticked `` `Term` `` names a term and is **not** a link (decision 005).
- `link.py` marks those, one link per page per target, and refuses to touch the
  frontmatter, code, a heading, a blockquote, anything inside „…", or any line
  carrying a `^[` citation. Dry run by default; `--apply` writes. Run
  `quotes.py` after — the first pass broke two quotations and that is how they
  were found.
- `selftest.py` runs the checkers against deliberate defects and asserts **which**
  one each reports. It cites a real landed document, so the whole resolution path
  runs: frontmatter, slug lookup, export unescaping, emphasis, blockquote
  wrapping, glued footnote numbers.
- `trainset.py` turns the ledger into examples and prints the `fold()` baseline
  live — never hardcoded, because it moves when the ledger grows.

### Every self-test at once

```bash
python3 scripts/selftests.py        # every suite, one line each: held / FAILED / not run
```

It runs each suite under its own interpreter and reports a DSPy suite whose
`.venv-dspy` is absent as **not run**, with the command that creates it — never
as passed (P11, P15).

## The knowledge graph and GraphRAG

```bash
python3 scripts/graph.py                          # node/edge/evidence counts, then the check
python3 scripts/graph.py --around nexus --hops 2 [--mermaid]
python3 scripts/graph.py --json | --graphml | --triples
python3 scripts/graphrag.py ask "<a German or English question>" [--json] [--budget 8]
python3 scripts/graphrag.py bench [--k 8] [--record]
.venv-dspy/bin/python scripts/graphrag.py ask "…" --answer --dry-run
```

- `graph.py` derives a typed graph — `term`, `doc`, `conflict`, `question`
  nodes; `links`, `reads`, `cites`, `contests`, `raised_by`, `asks`, `concerns`
  edges — from frontmatter, `[[links]]` and `^[slug.md:Lnn]` citations. Every
  edge carries `via: file:line`. Nothing is inferred. Its evidence is every
  quotation on a page, paired and judged by `quotes.pairs` / `quotes.verdict` —
  the checker's own code, so the two cannot disagree. Exit 1 when an edge points
  at a missing page or a document no manifest row lands.
- `graphrag.py ask` seeds by folded surfaces, spreads by personalized PageRank,
  and selects **verified** quotations by MMR with a relevance floor. It prints
  quotations, the conflicts and open questions touching the ranked pages, and the
  documents the rank reached. **It never writes an answer.** `--answer` lets a
  model choose evidence *numbers* and name gaps; code prints the quotations.
- `graphrag.py bench` scores retrieval against the wiki's own labels — each
  question's `raised_by`, each conflict's `pages` — with the case's own node
  removed first. `--record` appends both methods to `Plan/runs/baselines.jsonl`.

## Models — DSPy, offline first

Every command below except `score` needs `.venv-dspy` (DSPy 3.3.1 with numpy).

```bash
.venv-dspy/bin/python scripts/check_dspy_surface.py     # the DSPy surface this repo calls
.venv-dspy/bin/python scripts/lm_fixture.py             # the offline LM refuses the network
.venv-dspy/bin/python scripts/lmrun.py                  # the call record's four statuses
python3 scripts/pairs.py score [--rule fold] [--record]  # a rule on one-term-or-two, stdlib
.venv-dspy/bin/python scripts/pairs.py run --optimizer labeled|bootstrap|inferrules|simba|gepa --dry-run
.venv-dspy/bin/python scripts/pairs.py run --optimizer … --model M --approval "…" [--folds 5] [--repeats 3] [--record]
python3 scripts/baseline.py show | compare <task> [--floor NAME] | selftest
python3 scripts/check_skills.py [--selftest]
```

- `lmrun.call` is how `pairs.py` and `graphrag.py` call a model: cache off, a record per
  call in `Plan/runs/<subject>/lm/<step>.jsonl`, status `answered` / `refused`
  / `unparsed` / `unreachable`, and a real model refused without `approval=`.
- `pairs.py` scores a rule, or a compiled program **on the residual the rule
  leaves**, by stratified folds, and asks every candidate the never-merge
  canaries. A merged canary marks the ledger row `vetoed`.
- `baseline.py compare` fails a candidate that does not beat the floor, not only
  one that fell since the last row.
- `--dry-run` everywhere uses `lm_fixture.offline()`: API keys hidden,
  `litellm.completion` replaced by a refusal.

```bash
.venv-dspy/bin/python scripts/rlm_ingest.py <slug> --approval "<decision>"   # a real model run
.venv-dspy/bin/python scripts/rlm_ingest.py <slug> --score                   # against the human list
python3 scripts/rlm_ingest.py --selftest                                     # tools and reach, offline
```

`rlm_ingest.py` reads one document with `dspy.RLM` and writes
`Plan/runs/<slug>/03-candidates-rlm.md`, marked a reading or a reconstruction by
how many of its candidates cite a line that holds them.

## Entity lists by Jev

Both need `.venv-typesafe`, and every call sends text to a third-party API, so a
real run waits on the author's yes. `--replay` answers from the cached calls with
no key and no network.

```bash
.venv-typesafe/bin/python scripts/bilingual.py all [--replay]
.venv-typesafe/bin/python scripts/bilingual.py stated|entities|propose|pairs|write [--replay]
.venv-typesafe/bin/python scripts/jev_entities.py <slug> [--replay]
```

- `bilingual.py` writes each stage to `Plan/runs/bilingual/<stage>.jsonl`,
  caches every call under `Plan/runs/bilingual/calls/`, and writes
  `Plan/entities/bilingual.md` and `.jsonl`.
- `jev_entities.py` writes `Plan/runs/jev/<slug>/`, its `list.md` in the
  `Plan/entities` format. A test of a route, not a pipeline step.

## The project app

```bash
python3 scripts/ui.py              # derive, run the invariants, write Plan/derived/ui/
python3 scripts/ui.py --check      # also check what was written, the way the canvas reads it
python3 scripts/ui.py selftest     # each check handed the defect it exists to name
```

Writes nothing outside `Plan/derived/ui/`. Publishing is a Claude session's
Artifact call, never the script's.

## Fetching

```bash
python3 scripts/sources.py next --category <cat> --limit 5
# → mcp__Google_Drive__read_file_content per drive_id; it spills to a path
python3 scripts/sources.py land --drive-id <id> --consume
python3 scripts/sources.py status
```

**Never open the spill file.** `land --consume` parses it, normalises, writes
`Sources/drive/<slug>.md`, records both checksums and verifies. No model reads a
document's bytes in this step.

`next` filters against `Sources/duplicates.jsonl` by `drive_id`, so a folded
document is never offered again.

## Substrate

`subject.py` is the one place the corpus becomes addressable — every other
script asks it for a document, its body and its frontmatter offset. It raises on
a landed row whose file is gone rather than skipping it, because a silently
shrinking corpus makes every count quietly wrong.

`wiki_index.py` derives `Wiki/index.json` from page frontmatter. `reconcile.py`
answers by lookup against it and never scans the wiki.

`quotes.pairs(text)` and `quotes.verdict(refs, slug, quote)` are the one
implementation of *which reference belongs to which quotation* and *does it
resolve*. `quotes.py` checks with them and `graph.py` serves evidence from them.

`qmd.py` is the Python handoff to search: `search()`, `vsearch()`, `get()`,
`update()`, `collections()`, and `Hit.document()` back to `subject.Document`.

## Setup

```bash
scripts/install.sh [<component> ...]   # everything a fresh container lacks, but qmd-models
scripts/install.sh --check | --list
scripts/setup_qmd.sh [--check | --package]
```

`install.sh` is what the cloud session-start hook runs: every venv, the uv
tools, `Plan/derived/` and qmd's package, each skipped when present. A failed
component is reported and the rest still run.

`setup_qmd.sh` installs what git cannot carry for search: the npm package and
the path shim (`--package` stops there), the three GGUF models, the SQLite
index and the embeddings. The configuration itself is committed at
`.qmd/index.yml`.

## Model calls by third-party tools

```bash
python3 scripts/route.py models             # probe free models under the data policy
python3 scripts/route.py serve [--port N]   # OpenAI-compatible proxy for third-party tools
python3 scripts/route.py ledger             # what was called, by whom, at what cost
python3 scripts/route.py guard <slug>       # would this document's text be refused?
python3 scripts/route.py selftest           # offline: no key, no network
echo PROMPT | python3 scripts/route.py complete --purpose P --doc SLUG
python3 scripts/templates.py check [FILE ...]   # default: Plan/hyperextract/*.yaml
python3 scripts/templates.py selftest           # every check shown to fail on its defect
```

- `route.py` sends only to OpenRouter models whose every listed price is 0,
  refuses a document `Plan/runs/route/consent.json` does not name, and records
  every call under `Plan/runs/route/` so a run replays offline.
- `templates.py` needs `he` (`scripts/install.sh hyperextract`) and writes
  nothing.
