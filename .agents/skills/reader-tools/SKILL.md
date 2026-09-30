---
name: reader-tools
description: Prepare and use corpus tools as a delegated document-reader, wiki-reader or research agent. Use at the start of a subagent reading/research task, when an index is missing or stale, when selecting qmd versus corpus measurements versus graph evidence, or when handing HyperExtract candidates back to the coordinator. Includes role-specific access boundaries and the knowledge.py initialization command.
---

# Corpus tools for delegated readers

Read your `.claude/agents/<role>.md` and use its narrower write scope. Before your
first quotation read `references/failures.md`: every failure measured here, the
check that catches it, and what to write instead. Ask the
coordinator for a role, source slugs, task question, output folder, byte budget
and prepared capabilities. Run commands from the repository root.

## Prepare once, check as a worker

The coordinating session initializes before delegation:

```bash
python3 scripts/knowledge.py init --profile reader
# research additionally prepares the existing ask.db and DSPy toolchain
python3 scripts/knowledge.py init --profile research
# explicit full tool suite and qmd semantic models/embeddings
python3 scripts/knowledge.py init --profile full
```

As a worker, use only the check form:

```bash
python3 scripts/knowledge.py init --profile reader --check
```

For research use `--profile research --check`. Report each failed/unavailable
capability to the coordinator with its command. A profile is ready only when
each listed capability passes. Never install, rebuild shared indexes, run
`qmd init`, or race another initializer from a delegated reading. Continue a
source-only task with `read.py` if the assigned source exists and the missing
capability is irrelevant; report the reduced coverage.

## Choose the scope before retrieval

| Role | Read | Retrieval | Handoff |
|---|---|---|---|
| document-reader | assigned source and procedural briefing | `read.py`, `profile.py`, local quote/count checks; **no graph, qmd or wiki context before the independent census and note are frozen** | normal ingest artifacts; optional source-only extraction trial beside this run |
| wiki-reader | assigned sources, their census/note and assigned page digests | bounded graph or candidate windows only when the coordinator includes them in the reconciliation task, among them the document's `crossdoc.md` and its `P_BM25` lines to judge with `bm25rel.py label` | reading files, verdicts; code places their citations |
| corpus-researcher | question, selected corpus candidates and explicitly allowed graph context | qmd discovery, askdb BM25, graph evidence, exact source windows | source-specific claims, gaps, paths and coverage; no automatic landing or wiki writes |
| hyperextract-template-agent | procedural templates and assigned fixture/trial inputs | template design/check/smoke/evaluation only | versioned candidate YAML, fixtures, failure lists and pilot report |

## Ask the appropriate tool

```bash
python3 scripts/read.py <slug> --from 120 --to 150
python3 scripts/read.py <slug> --find "<exact words>"
python3 scripts/read.py <slug> --count "<surface>"
python3 scripts/profile.py <slug>
python3 scripts/corpus.py where "<surface>"
qmd search "<search words>" -c sources --json -n 8
.venv-graphqlite/bin/python scripts/kg.py context "<question>" --max-bytes 12000
.venv-graphqlite/bin/python scripts/kg.py around term:<slug> --hops 1 --limit 12
.venv-dspy/bin/python scripts/askdb.py bm25 "<search words>" --limit 8
.venv-dspy/bin/python scripts/askdb.py touches <document-slug>
python3 scripts/crossdoc.py doc <document-slug>      # who else writes a page's names: counts, and P_BM25 lines
python3 scripts/bm25rel.py find term:<slug> "<its words>" --exclude <document-slug>
```

Load `.agents/skills/qmd/SKILL.md` for collection/backend selection and URI
resolution; `.agents/skills/graph-context/SKILL.md` for the current schema and
freshness behavior. Use `scripts/qmd.py`'s `Hit.document()` in Python instead
of treating a filename stem as a source ID. qmd hits identify places to read;
counts come from corpus/read commands. Graph results must retain evidence IDs,
source IDs and `via`/citation locations. Open the original window before using
a candidate. Report omissions when the byte or result budget cuts coverage.

Both CLIs read `Plan/derived/ask.db`. Typed nodes also carry `:Core` when they belong to the wiki graph; use `r.core = true` to restrict relationships to that projection. Proposal relationships (`P_`) and evidence links do not participate in core ranking. The synthetic Cypher recipes in
`Plan/runs/qmd-discovery-graph-proposal-2026-09-30/` mark current and proposed
schemas; proposed labels are not available in the production stores.

## Optional extraction

Load `.agents/skills/hyperextract-learning/SKILL.md` only when the task includes
template development or extraction. A quote-placed candidate remains unreviewed.
For accepted wiki reading material, write the existing reading file format and
let the coordinator run `readings.py check/apply`; do not turn a relation into
a wiki link or a production graph edge.

Return: inputs and freshness checked, commands used, files written, quotations
placed/refused, distinct sources read, gaps and omitted candidates. Keep each
source's position separate. Record model usage separately from code execution.
