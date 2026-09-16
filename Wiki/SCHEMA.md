# Wiki — operating contract

This directory is the research layer of the three-layer knowledge system
(`Plan/wiki/knowledge-system-concept_2026-09-15.md`): `Sources/` (raw,
immutable) → `Wiki/` (LLM-maintained, human-promoted) → `Canon/` + the
provenance graph (author-locked). Every agent that reads or writes a page
starts here. The machine-readable contract lives in `schema/`; this file
explains it and never contradicts it — when in doubt the YAML wins.

| file | defines | consumed by |
|---|---|---|
| `schema/entities.yaml` | page kinds, required fields, enums, lifecycle, sections, citation grammar | `tools/kpwiki/wiki_schema.py`, `scripts/wiki_lint.py`, `scripts/render_wiki_views.py`, `tools/kpwiki` programs |
| `schema/edges.yaml` | typed relations in `graph/edges.jsonl` | lint rule `edge-evidence`, `cascade-risk` |
| `schema/xref.yaml` | forward link ⇒ reverse link, written in the same operation | lint rule `xref-symmetry`, `--fix` |
| `schema/conventions.yaml` | slugs, ownership zones, log grammar, batch sizes, promotion pins | every script |
| `schema/writers.yaml` | which command may write what; user-owned flags | lint rule `writer-policy` |

`tools/kpwiki/schema.py` mirrors the enums as Pydantic `Literal`s;
`tests/test_wiki_schema.py` fails when the two drift.

## Directory contract

```
Wiki/
  SCHEMA.md            this file
  schema/              the contract (five YAML files)
  templates/           one .md.tmpl per page kind; {{token}} fields are filled by the writing program
  index.md             RENDERED compact global hub — never edit
  GLOSSARY.md          short operational vocabulary (domain glossary is Codex/GLOSSARY.md)
  concept-table.md     RENDERED compressed map — never edit
  overview.md          what we currently understand the novel to be (versioned synthesis)
  log.md               APPEND-ONLY record of every operation
  sources/<category>/<slug>.md       one page per ingested Drive document
  concepts/<kind_detail>/<slug>.md   one page per merged semantic entity
  questions/<axis>/<slug>.md         one page per focused open question
  syntheses/<YYYY>/<slug>.md         filed /query answers (leaves)
  candidates/<kind-dir>/<partition>/ everything a program wrote and no human has reviewed
  <content-dir>/README.md             RENDERED local navigation — never edit
  graph/edges.jsonl    the wiki's relation index (tools-only)
  graph/coverage.json  RENDERED coverage numbers — never edit
```

Slugs match `conventions.yaml → slug.pattern`; source slugs come from
`Sources/manifest.jsonl` and are never re-derived. Page titles stay as in
the source. Summaries and explanations are English; quotes and Canon-facing
prose stay German and are never translated.

## Navigation and page boundaries

`index.md` is deliberately short. It links to the `README.md` of each page
kind; an occupied partition has another rendered `README.md` listing its
pages. Pages sit exactly one partition below their kind directory. The
partition comes from frontmatter and is never an improvised topic folder:

| kind | canonical path | partition source |
|---|---|---|
| source | `sources/<category>/<slug>.md` | `category` |
| concept | `concepts/<kind_detail>/<slug>.md` | `kind_detail` |
| question | `questions/<axis>/<slug>.md` | `axis` |
| synthesis | `syntheses/<YYYY>/<slug>.md` | year of `filed` |

One page holds one semantic entity or one focused question. Word budgets are
defined per kind in `entities.yaml → kinds.*.page_budget`: the ideal is a
target, `warn_words` requests review, and exceeding `max_words` is a lint
error. Split at a stable semantic boundary, preserve citations and state, and
connect the resulting pages with explicit `[[slug]]` links. Never split only
to satisfy a number when the fragments would not stand on their own.

## Page kinds and lifecycle

Four kinds: `source`, `concept`, `question`, `synthesis`. Required fields,
enums and body sections per kind are in `entities.yaml → kinds`; the
templates carry the sections in the exact order the lint expects
(`sparse-page` checks the level-2 headings by name).

Lifecycle of `status` (`entities.yaml → lifecycle`): `draft` → `reviewed` →
`contested` | `superseded` → `archived`. Transitions not listed there are
illegal. A `reviewed` page is protected: a new source never overwrites it, it
flags it; new material goes under a "Since <date>" heading and the page turns
`contested` when a `contradicts` edge appears. Archiving cascades: links to
the archived page become plain text with a note.

Questions use their own status enum (`open`, `answered`, `escalated`,
`parked`): `escalated` needs a `decision_ref` (D-xx), `parked` a `revisit`
date.

## Two axes, one graph (D-W2)

"The graph" in every document of this repo means the provenance graph
`.agency/session.db`. It receives **no page content**: pages are files and
`graph/edges.jsonl` is only the wiki's relation index. Atomic cited claims
enter the graph through `capture_claim` with a `source_uri` under `Sources/`
or `Canon/`, never `Wiki/`. The lint rules `no-page-body-in-graph` and
`no-reverse-into-canon` enforce both directions.

## Canon inside the loop (D-W12)

Every concept starts with `canon_status: unverified`. Canon stays normative
for manuscript work; inside the research loop a Canon/research conflict is an
open question with no default winner. Research pages may quote `[K]`/`[V]`
text from Canon but never emit `[K]` themselves.

## Links, citations, edges

- `[[slug]]` between wiki pages; `codex:<slug>` for glossary entries;
  `canon:<file>#<heading>` for Canon passages. The last two are terminal:
  they receive links, get no reverse link and are never auto-created.
- A forward link implies its reverse in the same operation (`xref.yaml`);
  `scripts/wiki_lint.py --fix` completes what a program forgot.
- Citations are `^[Sources/drive/<slug>.md:L-L]` or `^[Canon/<file>:L-L]`;
  the file must exist, the range must be inside it, and a quoted fragment on
  the citing line must be in those lines (`citation-resolves`).
- Typed edges (`edges.yaml`): `supports`, `extends`, `contradicts`,
  `supersedes`, `same_as`, `mentions`, each with `confidence`, `evidence`,
  `written_by`, `at`. `contradicts` is symmetric and turns both pages
  `contested`; `same_as` is a merge proposal that needs `/tetraframe` first.

## Log grammar

```
## [YYYY-MM-DD] <op> | <title> | skill=<command or program> | sha256=<hash when a page was written>
```

Ops and the `skill` values are closed sets (`conventions.yaml → log.ops`,
`writers.yaml`). The `sha256` of a reviewed body is the promotion pin: a hash
that changed since review refuses promotion. Epistemic claim events
(`created`, `reinforced`, `challenged`, `superseded`, `resolved`) are log
lines with `op=claim`.

## Who writes what

| surface | writes | never |
|---|---|---|
| `/source-inventory`, `scripts/source_dedup.py` | `Sources/manifest.jsonl` | an LLM call |
| `/research-ingest` (`BatchCompile`) | `candidates/`, `graph/edges.jsonl`, `log.md` | `sources/`, `concepts/`, `Canon/` |
| `/wiki-promote` | `sources/`, `concepts/`, `questions/`, `syntheses/`, `log.md` | a candidate that fails lint or whose hash changed |
| `/wiki-understand` (`MergeConcepts`) | `candidates/`, `concept-table.md` (rendered), `overview.md` (candidate) | a reviewed concept page |
| `/interrogate-canon`, `/clarify` | `questions/` (draft), `log.md` | `Canon/` |
| `/tetraframe` | `Plan/decisions/tetraframe/`, `log.md` | a decision |
| `/promote-to-canon` | `Plan/ingest/` proposal | `Canon/` (the author applies the patch) |
| `scripts/render_wiki_views.py` | `index.md`, `concept-table.md`, `graph/coverage.json` | anything else |
| `scripts/wiki_lint.py --fix` | reverse links, default fields, `graph/coverage.json` | page content |

User-facing flags (`writers.yaml → user_flags`) are user-owned: a session
never sets `--promote`, `--apply` or `--write` on its own. `Sources/**`,
`Canon/**`, `ncp.json`, `ncp-b.json` are the author's.

## Free checks before anything is declared done

```bash
python3 scripts/wiki_lint.py --health        # every rule, zero LLM calls; exit 1 on errors
python3 scripts/render_wiki_views.py --check # views in sync with the pages
python3 scripts/wiki_fts.py search "…"       # candidate finder; open the page before citing it
```

The lint runs as a warn-only PostToolUse hook on `Wiki/**` and as a hard
gate before `/wiki-promote`. `/lint-wiki` (LLM) and the adversarial review
(`dspy-adversarial-review`, reviewer ≠ writer) run per milestone. Rule 0
still governs: on any canon, plot, wording or scope ambiguity the session
asks the author instead of assuming.
