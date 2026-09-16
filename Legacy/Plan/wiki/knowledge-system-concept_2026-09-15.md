# Knowledge system concept — wiki, process, safe skills

*Kohärenz Protokoll · 2026-09-15 · status: proposal (`[V]`) — author decisions listed in §7*

## 0. Why

The Drive index (`Plan/research/koharenz-protokoll_google-drive-quellenindex_2026-09-15.md`)
lists 680 documents (693 with the appendix) written between 2025-04 and 2026-09:
concept syntheses, plot outlines, character and world documents, storyform work,
audits, and theory (mathematics, logic, physics, psychology, philosophy, AEGIS).
None of it is canon. `Canon/` (six documents from 2026-06-10) *is* — but it was
distilled from an earlier slice of exactly this corpus, and we have never checked
it against the whole. So the task is not "ingest 680 files"; it is:

1. keep everything we know in one place, with canon and research visibly apart,
2. run a process that keeps sharpening our understanding of the novel
   (what it is, what it must not become) instead of piling up summaries,
3. make that process safe: no invented facts, no silent canon changes, every
   claim traceable to a line in a source, every canon change traceable to a decision.

Three things, three sections: **§3 the wiki**, **§4 the process**, **§5 the skills**.
§2 sets the principles, §6 the DSPy programs that do the LLM work, §8 the
phased setup. Sources: the nine-repo survey (`repo-survey_2026-09-15.md`) and
what this repo already has (agency graph, `Codex/` views, worldcodex commands).

## 1. What already exists (do not rebuild)

| layer | today | keeps its role |
|---|---|---|
| normative canon | `Canon/*.md` (German, `[K]/[V]/[S]/[L]` markers; storyform-und-outline wins) | yes — the wiki never edits it |
| canon provenance | `.agency/session.db`: ~600 CodexEntries, 111 WorldAxioms, StoryTimeEvents, NovelClaims, decisions | yes — canon facts enter the graph via `/ingest` + `scripts/ingest_canon.py` |
| generated canon views | `Codex/GLOSSARY.md`, `MASTER-TIMELINE.md`, `WORLD-AXIOMS.md` (rendered, write-denied) | yes — the wiki's entity matcher reads the glossary triggers |
| decisions | `Plan/drafting/decision-log*.md` (D-xx), `record_storyform_decision` | yes — the only door from research into canon |
| interactive workflows | `/ingest`, `/query`, `/lint-wiki`, `/full-audit-canon`, 19 codex skills, 3 agents, 6 warn-only hooks | yes — extended, not replaced |
| research downloads | `Plan/research/` (papers, `research-tool.py`) | yes — external science lands there; the Drive corpus gets its own layer |
| filed answers | `Plan/queries/` | folded into `Wiki/syntheses/` (D-W4) |

The one thing missing is a **research layer with its own contract**: today a
Drive document either becomes canon (via `/ingest` → graph) or nothing.

## 2. Principles

1. **Three layers, one direction.** `Sources/` (raw, immutable) → `Wiki/`
   (LLM-maintained research understanding) → `Canon/` + graph (author-locked).
   Knowledge only moves *up* through an explicit promotion; nothing flows down
   except references. (Karpathy; AutoSci ownership zones.)
2. **Canon is terminal for the wiki, and unverified until the wiki has checked it (D-W12).**
   Wiki pages link to Canon; Canon never links back, is never auto-created, never
   auto-edited. Inside the wiki loop every Canon claim starts as `unverified`; a
   conflict between Canon and research is an open question with no default
   winner until a verification pass against the populated wiki. Manuscript work
   keeps Canon normative meanwhile. (AutoSci `foundations`; D-W12.)
2a. **Pages stay files, claims keep their door (D-W2).** Wiki *pages* live only
   under `Wiki/**/*.md`; no script copies a page body, or a paraphrase of one,
   into a field of the provenance graph (`.agency/session.db`), and no graph
   node or edge type mirrors a page. Atomic cited *claims* keep the existing
   `capture_claim` channel, sourced from `Sources/` or `Canon/`, never from a
   `Wiki/` path. `Wiki/graph/edges.jsonl` is the wiki's own relation index and
   is not "the graph". (TetraFrame run `Plan/decisions/tetraframe/d-w2-wiki-markdown-vs-graph.json`.)
3. **Every claim has a line.** A research claim without a `^[Sources/…:L-L]`
   citation that a script can verify does not exist. (synthadoc, llm-wiki-compiler.)
4. **The schema is data and the lint is free.** Page kinds, enums, transitions
   and link rules live in `Wiki/schema/*.yaml`; `scripts/wiki_lint.py` enforces
   them with zero LLM calls; the DSPy models mirror the same enums. (AutoSci.)
5. **Reviewed pages are protected.** New sources never overwrite a reviewed
   page; they flag it. (synthadoc RULE 1b.)
6. **Batches, not drips.** Dedup and triage before any LLM call; merge and
   interrogation run every N sources, not every source. (llm-tldr.)
7. **Questions are the product.** The loop's output is a maintained list of
   open questions about the novel, each with evidence, not a pile of summaries.
   (DeepRefine's abduction axes.)
8. **Dry-run first, approval pinned.** Anything that writes into `Wiki/` proper
   or proposes a canon change is shown as a diff first; approval is bound to the
   hash of what was reviewed. (DeepRefine, llm-wiki-compiler.)
9. **Rule 0 unchanged.** Ambiguity → `AskUserQuestion`. The wiki records that a
   question exists; the author answers it.
10. **German in, English around.** Quotes and canon-facing prose stay German;
    summaries, explanations, engineering are English.

## 3. The wiki

### 3.1 Directory contract

```
Sources/                      raw layer — immutable (write-denied for the agent)
  manifest.jsonl              one line per Drive document (built: scripts/source_inventory.py)
  drive/<slug>.md             markdown export, never edited
  originals/                  binaries, git-ignored
Wiki/                         research layer — LLM-maintained, human-reviewed
  SCHEMA.md                   the operating contract (single source of truth for agents)
  schema/{entities,edges,lint}.yaml   enums, required fields, transitions, link rules
  index.md                    catalogue by kind (content navigation)
  log.md                      append-only: ## [YYYY-MM-DD] <op> | <title> | <agent>
  overview.md                 "what we currently understand the novel to be" — versioned synthesis
  concept-table.md            compressed map: concept · definition · sources · status · open questions
  sources/<slug>.md           one page per ingested document (T2/T3)
  concepts/<slug>.md          one page per merged concept / entity / theory / motif
  questions/<slug>.md         open questions about our understanding (the product of §4 C)
  syntheses/<date>-<slug>.md  filed answers from /query (replaces Plan/queries/)
  candidates/                 staging: everything the LLM wrote and no human has reviewed
  graph/                      derived, tools-only: edges.jsonl, contradictions.jsonl, coverage.json
```

`Wiki/` is plain Markdown + YAML in git (Obsidian-readable). The agency graph
is **not** the store for research: it is the canon provenance record, and a
second copy of canon in Markdown would drift (learnings 2026-09-11 §2). The
wiki mirrors only *references* to graph ids (`codex:` slugs, `axiom:` ids).

### 3.2 Page kinds (`Wiki/schema/entities.yaml`)

| kind | one per | required frontmatter | body sections |
|---|---|---|---|
| `source` | Drive document | `title, drive_id, slug, tier, category, language, status, sha256, ingested, supersedes, superseded_by` | Summary · Key claims (each `^[file:L-L]`) · Entities (`[[…]]`, `codex:` refs) · Canon relation (consistent / extends / contradicts, with Canon file + excerpt) · Open questions · Log |
| `concept` | merged idea, entity, rule, theory, motif | `title, aliases, kind_detail (concept|character|world|rule|theory|motif|storyform), status, confidence, sources[], codex_ref, canon_status` | Definition (as research understands it) · What Canon says (quoted, German) · Where sources agree · Where they disagree · Timeline of the idea (oldest → newest source) · Open questions |
| `question` | one question | `title, axis (incompleteness|incorrectness|redundancy), status (open|answered|escalated|parked), concepts[], evidence[], owner, decision_ref` | Question · Evidence (citations) · What Canon says · Candidate answers · Resolution (D-xx or answer + date) |
| `synthesis` | filed `/query` answer | `title, query, sources[], status` | as today in `Plan/queries` |

Shared enums (mirrored in `tools/kpwiki/schema.py`):

- `status`: `draft` (LLM wrote it, in `candidates/`) → `reviewed` (a human promoted it) → `contested` (open contradiction) · `superseded` (newer source or decision) · `archived`.
  Transitions are listed in the YAML; the lint rejects others. Cascade: archiving
  a page rewrites `[[links]]` to it into plain text with a note.
- `confidence`: `high | medium | low` — always with `evidence`.
- `canon_status` (concepts): `unverified` (present in Canon, not yet checked against the wiki — the initial value for every Canon claim, D-W12) · `locked` (present in Canon with `[K]` and verified) · `proposal` (Canon `[V]`) · `absent` · `contradicted` · `promoted` (moved into Canon by a D-xx).
- `tier` (sources): `T0-duplicate · T1-superseded · T2-theory · T3-work · T4-out-of-scope`.
- Markers: research pages may cite `[K]/[V]` text from Canon but **never emit `[K]`** themselves (lint rule `no-k-marker-outside-canon`).

### 3.3 Links and edges

- `[[slug]]` between wiki pages; `codex:<slug>` for glossary entries;
  `canon:<file>#<heading>` for Canon passages. Forward link ⇒ the reverse
  `sources[]` / `concepts[]` entry is written in the same operation
  (`Wiki/schema/edges.yaml`, AutoSci xref).
- Typed edges live in `Wiki/graph/edges.jsonl`, the wiki's own relation index;
  "the graph" in this document always means the provenance graph
  `.agency/session.db` (D-W2):
  `supports | extends | contradicts | supersedes | same_as | mentions`,
  each with `confidence` and `evidence` (a citation). `contradicts` is symmetric.
- Retrieval: `scripts/wiki_fts.py` (SQLite FTS5 BM25 over `Wiki/`, `Canon/`,
  `Sources/drive/`, chunked by heading — port of the Karpathy helper). Candidate
  finder only: the agent opens the page before citing it.

## 4. The process — the loop that improves understanding

```
A  Inventory   (deterministic)   index → manifest → export → hash → dedup/supersede clusters
B  Ingest      (DSPy)            source → triage → cited claims → entities → canon relation → candidates/
C  Understand  (DSPy, batched)   every N sources: merge claims into concept pages; knowledge diff
D  Question    (DSPy + human)    per concept: abduction on 3 axes → Wiki/questions/; human triage
E  Decide      (author)          answer from Canon · park · escalate → D-xx → Canon edit → /ingest → Codex
F  Verify      (free + LLM)      wiki_lint every write; /lint-wiki + adversarial review per milestone
```

**A — Inventory.** `scripts/source_inventory.py` already turns the index into
`Sources/manifest.jsonl` (693 records; 508 T3-work, 172 T2-theory, 13 T4;
246 byte-equal copies flagged). The fetch step (Drive MCP, `drive-markdown-converter`
skill) fills `export_path`, `sha256`, `exported_at`; then `scripts/source_dedup.py`
marks `T0-duplicate` (equal hash) and `T1-superseded` (near-duplicate by shingle
Jaccard ≥ 0.8 with a later `index_date`, or same title with a later date;
`duplicate_of` / `supersedes` filled). Nothing here calls an LLM. Health report:
exported / total, duplicates, unresolved formats.

**B — Ingest** (`tools/kpwiki.programs.SourceIngest`). Order: T3 kernkonzept
and audits first (they carry the most self-understanding), then storyform,
characters, worldbuilding, plot; T2 theory last. Per source: `TriageSource`
(confirms tier/category, summary), `ExtractClaims` (atomic claims with line
citations, entities matched against `Codex/GLOSSARY.md` triggers),
`CheckCanonConflict` (BM25-retrieved Canon passages → conflicts with severity).
Output is a `source` page in `Wiki/candidates/` plus a printed **knowledge diff**
(new claims · reinforce existing concept · challenge Canon · gaps). The
deterministic lint runs on the candidate; a failing candidate is never promoted.

**C — Understand** (batched, every 25 promoted sources or on demand). Two-phase
compile: collect all claims of the batch, cluster by entity/glossary slug, then
`MergeConcept` writes or updates `concepts/` pages — "what the sources say,
where they agree, where they disagree, what Canon says". Updates
`concept-table.md` and `overview.md`. Reviewed concept pages are never
overwritten: new material is appended under "Since <date>" and the page flips
to `contested` if a `contradicts` edge appeared.

**D — Question** (`RaiseQuestions`, DeepRefine loop). For every concept with
≥2 sources, any `contradicts` edge, or `canon_status: absent` for something the
sources treat as central: generate questions on three axes —
*incompleteness* (research assumes what Canon doesn't say), *incorrectness*
(research and Canon disagree; or two work-documents disagree), *redundancy*
(two concepts that are one, or one that is two). Each question carries
evidence citations and an evidence grade (HIGH: exact quote in both;
MEDIUM: inferred across pages; LOW: ambiguous naming). Written to
`Wiki/questions/` as `draft`; the session presents them; the author triages.

**E0 — Clarify (gate before any authority change).** Before a claim may be
proposed for promotion, `ClarifyGate` (`tools/kpwiki/clarify.py`, skill
`dspy-clarify`, command `/clarify`) rewrites it so scope (Kernwelt, Akt,
Anteil), glossary bindings and assumptions are explicit — only where the
source states them — and turns every remaining ambiguity into a question for
the author. Verdicts: `clear` (may be proposed), `needs-author` (questions to
`Wiki/questions/`), `not-promotable`. The deterministic `clarify_metric`
(no smuggled terms, no new quantifiers, grounded scope, resolved hedges,
valid bindings, well-formed questions, language kept) must score ≥ 0.9. The
same gate runs on vague task statements before decomposition
(`dspy-rlm-workflow`) and on queries before `dspy-deep-refine` changes the base.

**E1 — Assess (before a contested decision).** When a question has two
camps, when a `/wiki-understand` merge would supersede or delete a concept
page, when a promotion carries a `contradicts` edge, or when a storyform /
axiom change is on the table, `TetraFrame` (`tools/kpwiki/tetraframe.py`,
skill `dspy-tetraframe`, command `/tetraframe`) runs first: the seed is
distilled to one predicate, four corners are generated in isolation (P,
not-P, both under a typed split, neither with a replacement predicate),
their contradictions and evidence discriminators are mapped, and a
non-averaging P* is produced. The run passes only if all seven checks
hold: branch independence ≥ 0.90, rigor of *both* ≥ 0.78, rigor of *neither*
≥ 0.78, contradiction honesty ≥ 0.75, transformation quality ≥ 0.82,
fake-novelty risk ≥ 0.70, slop risk ≥ 0.70. The
run file under `Plan/decisions/tetraframe/` is what the D-xx cites; the
question page lists the four corners as candidate answers. The run never
decides — the author does (Rule 0).

**E — Decide.** Three outcomes per question: *answered from Canon* (cite it,
close), *parked* (status `parked`, revisit date), *escalated* (a D-xx entry in
the decision log; if Canon changes, the author edits Canon, `/ingest` seeds the
graph, `Codex/` re-renders, the concept page flips to `promoted`). This is the
only path research → canon. The wiki never writes into `Canon/`, `ncp*.json`, and
never writes page content into the provenance graph; atomic cited claims use
`capture_claim` with a `Sources/` or `Canon/` `source_uri` (D-W2). The lint rule
`no-page-body-in-graph` checks every graph-write payload for page-body overlap.
The wiki never writes into
the graph.

**F — Verify.** `scripts/wiki_lint.py` (free): frontmatter enums, required
fields, transition legality, `[[links]]` resolve, citations resolve to existing
lines and the quoted fragment is present, xref symmetry, index/log coverage,
stale `sha256`, orphans, `[K]` outside Canon, candidates older than 30 days.
Runs as a PostToolUse hook on `Wiki/**` (warn-only, like the chapter lint) and
as a gate before promotion. `/lint-wiki` (LLM) and an adversarial review pass
(`worker` model challenges `high`-confidence concept pages) run per milestone.
Coverage metrics in `Wiki/graph/coverage.json`: sources ingested / 680,
concepts with canon_status, open questions by axis, contested pages.

**Cadence.** Sessions start with health (free). Ingest runs in batches of
~25 (about one category slice). After each batch: C, D, then a triage
conversation. `/lint-wiki all` and the adversarial pass before a milestone
(a chapter status flip, a Canon revision).

## 5. Skills, commands, hooks — what makes it safe

New (project-local, `.claude/commands/` + `.claude/skills/`), following the
worldcodex conventions already in the repo:

| surface | does | never |
|---|---|---|
| `/source-inventory` | Phase A: manifest, fetch (Drive MCP), hash, dedup, health | calls an LLM; touches anything outside `Sources/` |
| `/research-ingest <selector>` | Phase B for `--slug`, `--category`, `--tier`, `--batch N`; prints the knowledge diff; writes only `Wiki/candidates/` | writes `Wiki/sources/` directly; invents citations (metric + lint) |
| `/wiki-promote [slug…]` | shows candidate diff, runs lint, moves to `Wiki/`; records reviewer + content hash in `log.md` | promotes a candidate that fails lint or whose hash changed since review |
| `/wiki-understand` | Phase C over promoted-but-unmerged sources; updates concepts, concept-table, overview as candidates | overwrites a `reviewed` concept page |
| `/interrogate-canon <concept|category|all>` | Phase D; questions as drafts; dry-run list first | answers its own questions; writes to Canon |
| `/clarify <page or statement>` | Phase E0: runs `ClarifyGate` (dry-run, nothing written), files `needs-author` questions, records verdict + score in `log.md` | resolves an ambiguity the source does not resolve; rewrites from Canon |
| `/tetraframe <seed>` | Phase E1: runs `TetraFrame` on a clarified seed, writes the run to `Plan/decisions/tetraframe/`, shows corners + contradiction map + P* + verification table, then `AskUserQuestion` | picks a corner or P* itself; edits a corner to pass verification; runs on a vague seed (clarify first) |
| `/promote-to-canon <page>` | Phase E helper: requires a `clear` clarify verdict (score ≥ 0.9), a D-xx id and an `AskUserQuestion` sign-off; produces the Canon patch **proposal** + `Plan/ingest` manifest for `/ingest` | applies the patch itself; accepts a page without a clarify verdict |
| `/wiki-health` | free lint + coverage report | LLM calls |
| `/query` (existing) | adds BM25 step; files to `Wiki/syntheses/` | — |
| `/lint-wiki` (existing) | gains `Wiki/` scope: stale concept vs newer source, questions without evidence | auto-fixes |
| `@wiki-librarian` (agent, read-only) | retrieval + citation across `Sources/`, `Wiki/`, `Canon/`, glossary | writes |

Hooks and permissions (extend `.claude/settings.json`):

- `permissions.deny`: `Write(Sources/**)`, `Edit(Sources/**)` (raw immutability);
  `Wiki/graph/**` and `Wiki/index.md` are tools-only (rendered).
- PostToolUse on `Wiki/**` → `scripts/wiki_lint.py --hook <file>` (warn-only);
  on `Wiki/candidates/**` only the frontmatter check.
- PreToolUse on `Canon/**`: if no `D-xx` appears in the session's
  `CURRENT_TASK.md`, warn "canon edit without decision" (still warn-only, per
  the repo's decision not to write-deny Canon).
- SessionStart: `scripts/wiki_lint.py --health` summary next to the stale-Codex check.

Skill discipline (from AutoSci / dspy-agent-skills): user-facing flags are
user-owned (never auto-set `--promote`, `--apply`, `--write`); each skill's
write set is declared in `Wiki/schema/writers.yaml` and checked by the lint
(`log.md` records which skill wrote which page); one `SKILL.md` per skill with
reference docs, no code inside skills — they call `scripts/` and `tools/kpwiki`.

## 6. DSPy programs (tools/kpwiki) and how they are kept honest

| program | signatures | metric axes (deterministic unless noted) | gold set |
|---|---|---|---|
| `SourceIngest` (built) | `TriageSource`, `ExtractClaims`, `CheckCanonConflict` | citation validity, quote grounding, schema validity, language kept, coverage vs gold fragments | 30 hand-checked sources across categories |
| `MergeConcept` | `MergeConcept` (claims[] + canon excerpt → concept page fields) | every sentence in "what sources say" has ≥1 citation; disagreements list ≥2 sources; canon quote is verbatim (substring of Canon file); no `[K]` emitted; LLM judge (worker) for faithfulness | 20 concepts |
| `RaiseQuestions` (signature built) | `RaiseQuestions` | evidence citations resolve; axis ∈ enum; question is not answerable verbatim from Canon (judge); ≤ 7 per concept | 15 concepts with known gaps |
| `ClarifyGate` (built) | `ClarifyClaim` | meaning kept (no smuggled glossary terms, no dropped entities, no new quantifiers), scope grounded, hedges resolved or declared, bindings valid, questions well-formed + verdict consistent, language kept | 30 claims incl. hand-picked `needs-author` cases |
| `TetraFrame` (built) | `DistillSeed`, `SelectPredicate`, `CornerP/NotP/Both/Neither`, `MapCorners`, `TransformFrame` (BestOfN) | the seven verification heuristics (isolation guard + near-duplicate check in code); gold: expected predicate phrase, allowed `both` bases, expected `neither` failure modes, banned P* phrases | 10–20 seeds from real D-xx candidates, incl. seeds whose right answer is `neither` |
| `BatchCompile` (`DecideIngest`, `KnowledgeDiff`, `AnswerQuery`; skill `dspy-wiki-compile`) | `DecideIngest` (flag \| update \| create), `KnowledgeDiff` (reinforced/challenged/new/gaps), `AnswerQuery` | decision legal vs page status (`update` on a reviewed page with conflicts scores 0), diff consistent with the conflicts, gaps named when retrieval is thin, citations resolve | 20 source/page pairs incl. 5 that must `flag` |
| `AdversarialReview` (`ReviewArtifact`, `CitationSupport`; skill `dspy-adversarial-review`) | `ReviewArtifact` (score, overstated, unsupported), `CitationSupport` (supported \| partial \| unsupported) | reviewer LM ≠ writer LM (asserted); precision/recall of `overstated` + `unsupported` on a labelled set; demotion is a status change | 40 claims, half overstated by construction |
| `CanonConflictJudge` | `CheckCanonConflict` in isolation | precision/recall on a labelled conflict set (incl. the two Storyform A/B non-conflicts) | 40 claim/passage pairs |

Workflow per program (skill `dspy-advanced-workflow`): spec → signature →
gold split (train/val, never evaluated on train) → metric → **baseline** →
GEPA `auto="light"` (then medium) with the reflection model (on the `claude-cli` backend when no API key is present — `docs/dspy-base.md` "Local runtime") → save
`tools/kpwiki/artifacts/<program>.json` → regression test with cached LM in
`tests/`. Cost control: cache dir, `worker` model for judges, `max_metric_calls`
explicit. RLM (`dspy.RLM`, needs Deno) for the 100k+-token documents instead of truncation.

What the metric cannot check, the process does: faithfulness beyond quote
grounding is the promote step (human), and canon relation is only ever a flag
(§4 E).

## 7. Decisions needed from the author (Rule 0)

| id | question | recommendation |
|---|---|---|
| D-W1 | Commit the 680 markdown exports under `Sources/drive/` (est. 20–40 MB text) so citations resolve on any clone? | **decided 2026-09-16: yes, all text exports**; binaries stay out |
| D-W2 | The research wiki lives in Markdown (`Wiki/`), the graph stays canon-only? | **decided 2026-09-16: the two-axis rule** (§2 2a) after the TetraFrame run `Plan/decisions/tetraframe/d-w2-wiki-markdown-vs-graph.json`: pages file-only, claims keep `capture_claim` from `Sources/`/`Canon/` only |
| D-W3 | Ingest order: kernkonzept + audits → storyform → characters → worldbuilding → plot → theory? | yes; plot (247 docs) last among T3 because it is the most superseded |
| D-W4 | Fold `Plan/queries/` into `Wiki/syntheses/`? | yes, with a pointer README |
| D-W5 | Wiki page language: summaries English, quotes German? | yes (engineering English rule) |
| D-W6 | Superseded drafts (T1): ingest as sources anyway (for the "timeline of an idea") or only link them? | **decided 2026-09-16: ingest everything** — all documents of tiers T1–T3 with claims extracted, superseded drafts marked `superseded_by`; only the 13 `T4` rows are dropped (D-W9) |
| D-W7 | Which categories are out of scope for questioning canon (e.g. AEGIS docs pre-dating the Act-I naming decision)? | none excluded; the decision log answers them |
| D-W8 | Register the DSPy marketplace in `.claude/settings.json` (blocked for the agent this session)? | yes — snippet in `docs/dspy-base.md` |
| D-W9 | May Google-Drive document ids and titles live in this public CC0 repo (`Sources/manifest.jsonl`, the source index)? | **decided 2026-09-16: keep ids, drop the 13 appendix (`T4`) rows, review titles of personal documents before Phase 2** |
| D-W10 | Add `dspy-wiki-compile`, `dspy-adversarial-review`, `dspy-local-runtime` to the pack? | **decided 2026-09-16: yes** — [dspy-agent-skills#4](https://github.com/netzkontrast/dspy-agent-skills/pull/4), v0.7.0 |
| D-W11 | Which model is the independent reviewer? | **decided 2026-09-16: `claude/haiku` for wiki pages, `claude/sonnet` for the promotion gate**, both via the CLI; reviewer ≠ writer asserted |
| D-W12 | Is Canon normative while the wiki is being populated? | **decided 2026-09-16: no, for the wiki loop** — every Canon claim starts `unverified`, conflicts are open questions with no default winner until a verification pass against the populated wiki; manuscript work keeps Canon normative (§2 2) |

## 8. Setup plan for this repo

| phase | deliverable | done when |
|---|---|---|
| 0 (this PR) | DSPy base (`tools/kpwiki`, `requirements-dspy.txt`, `scripts/setup_dspy.sh`, `docs/dspy-base.md`), `Sources/manifest.jsonl` + `scripts/source_inventory.py`, the clarify gate (`ClarifyGate`, `clarify_metric`, `/clarify`), the decision assessor (`TetraFrame`, `tetraframe_metric`, `/tetraframe`), the Claude-CLI LM backend (`local_lm.py`, no API key needed), this concept, the survey | smoke + tests pass ✔ |
| 1 | `Wiki/` skeleton: `SCHEMA.md`, `schema/*.yaml`, `index/log/overview/concept-table`, `scripts/wiki_lint.py` (+tests), `scripts/wiki_fts.py`, hooks + deny rules, `Sources/README` fetch procedure, `scripts/source_dedup.py` | lint passes on an empty wiki; one source exported end-to-end by hand |
| 2 | Export of all 680 documents (Drive MCP batch), dedup/supersede pass, coverage report | manifest complete; T0/T1 assigned; health green |
| 3 | `/research-ingest` + `/wiki-promote`; gold set of 30 sources; `SourceIngest` baseline recorded (`tools/kpwiki/eval_runs/`) | first 50 T3 sources reviewed and promoted |
| 4 | `/wiki-understand` (`MergeConcept`), concept-table, overview v1 | kernkonzept + audit slices merged; knowledge diff reviewed |
| 5 | `/interrogate-canon` (`RaiseQuestions` + evidence grading), question triage ritual, `/clarify` gold set + baseline, `/promote-to-canon` with clarify + D-xx gates | first question batch triaged; first D-W decision executed end-to-end into Canon → graph → Codex |
| 6 | GEPA optimization of `SourceIngest` / `MergeConcept`, regression tests, adversarial review pass, `/lint-wiki` extended | optimized artifacts saved; scores ≥ baseline on held-out val |
| 7 | remaining categories ingested (plot, theory); overview v2; NovelClaims for verified T2 theory into the graph | coverage 680/680; open-question backlog owned |

Each phase ends with `python3 scripts/wiki_lint.py`, `/verifying-completion`
and a `Plan/sessions/<date>-learnings.md` entry. Which surveyed repo each
deliverable follows, and which pack skill teaches its LLM part, is in
[integration-plan_2026-09-15.md](integration-plan_2026-09-15.md) (adds D-W10, D-W11).

## 9. Open risks

- **Corpus size vs context**: many T3 documents exceed 100k tokens; RLM or
  heading-chunked ingest is required, with `truncated: true` recorded whenever a body was capped.
- **Superseded drafts dominating**: 247 plot documents, most older than Canon;
  D-W6 keeps them from generating noise questions.
- **Engine availability**: the agency MCP did not connect in this session; the
  wiki must work with plain Python + git, using graph verbs only at promotion.
- **Quote grounding is lexical**: paraphrased claims that are true but reworded
  score low; the gold set must include paraphrase cases so GEPA learns to quote.
- **Two truths**: Storyform A/B and per-Kernwelt logic regimes are not
  contradictions; the conflict judge's gold set encodes that explicitly.
