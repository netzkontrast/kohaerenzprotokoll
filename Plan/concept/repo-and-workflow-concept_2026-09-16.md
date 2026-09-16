# Repo and workflow concept — what each part is, what it is for, and what the restart changes

**Date:** 2026-09-16
**Status:** proposal for author review; nothing in it has been executed
**Scope:** the whole repository, ahead of a rethink of every workflow
**Method:** seven parallel readers over the subsystems, one of them a dedicated
verification of the Canon-coverage claim. 1.19 M tokens, 326 tool calls. Every
number below was measured on this checkout, not recalled.

This document answers the question the author asked before any workflow gets
redesigned: *what is what here, and with what goal.* It is a description first
and a proposal second, and the two are kept apart on purpose — §1 to §6 are
findings, §7 to §9 are proposals, §10 is what only the author can settle.

---

## 0. The three decisions this document was written under

The author decided, before the read:

1. **`Canon/` goes away.** Chosen on the stated ground that `Codex/` already
   carries its content.
2. **`Manuscript/` prose restarts from zero.** The 41 existing chapters are
   backed up and become reference only.
3. **Workflows get rethought and consolidated**, with the target count left
   open until this document is reviewed.

Backups exist: branch `backup/pre-restart-2026-09-16` on `origin`, at commit
`608cbb5`. It holds all 41 chapters, all 8 Canon documents, `Graph/` at 1,180
records and `Codex/` at 644 files. Single file back:
`git show backup/pre-restart-2026-09-16:<path>`.

Decision 1 rested on a claim. The claim was checked. It is false in the parts
that matter, and §5 gives the evidence. Decision 2 has a consequence nobody
had costed, and §4 is that consequence. Neither finding overturns the decision —
both change what has to happen first.

---

## 1. What this repository is

Three things that only make sense together:

- **a novel** — *Kohärenz Protokoll*, German hard SF, 41 chapters, dual
  storyform, `novel:9d170c31`;
- **a research corpus** — 680 Drive documents meant to reach the novel only
  through a human decision;
- **deterministic tooling** whose entire job is to stop the first two from
  quietly disagreeing.

The governing idea is `CLAUDE.md` Rule 1: *anything decidable by a program is
written as a program*, and anything left over is named as judgement. The
repository is best read as an ongoing attempt to hold that line — and most of
what follows is a report on where the line currently holds and where it does not.

The second governing idea is Rule 0: research is not canon, a wiki page is not
canon, and promotion is always a human act. Every workflow in the repo ends in
an author checkpoint, and six of the eleven commands end with an explicit
*present, do not decide*.

---

## 2. The layers, as they actually are

`CLAUDE.md` describes five layers. Measured, they are in very different health.

| layer | declared job | measured state |
|---|---|---|
| `Sources/` | immutable research floor, 680 Drive exports | **28 files on disk** against a 680-document manifest |
| `Wiki/` | drafted knowledge, human-promoted | **56 candidates, 2 promoted.** `Wiki/context-map.md` renders `_no routable pages yet_` |
| `Graph/` | the novel's facts as JSONL | **healthy** — 1,180 records across 11 node files + 802 edges |
| `Canon/` | normative German prose | 8 files, 51,967 words, **already not the live source of `Graph/`** (§5.1) |
| `Manuscript/` | the book, source of truth for prose | 41 chapters, 97,361 words, 40 `drafted` + 1 `revised` |

Two entries in that table are the story of the repository right now.

**`Wiki/` is instruction weight with no payload.** `CLAUDE.md`, `AGENTS.md` and
the `wiki-maintenance` skill together spend roughly 3,400 tokens routing
manuscript retrieval through a layer that holds two promoted pages, and
`AGENTS.md` names `Wiki/context-map.md` as the *mandatory first hop* for
manuscript work. That file's table body is the literal string
`_no routable pages yet_`. The research half of the pipeline —
`/research-ingest` → `/kp-promote` → `/clarify` → `/tetraframe`, about 9,900
tokens of command text and three DSPy programs — sits upstream of a layer no
downstream workflow can read.

The cost of changing that is measurable, from the one real dollar figure in the
repo (`Plan/wiki/pilot-run_2026-09-16.md`): 3 sources, 53 LM calls, 54 minutes,
$8.38. At that rate the 680-document manifest is **≈ $1,900 and ≈ 8.5 days** of
wall clock. That number, not an opinion, is what makes "is the research layer
funded, deferred, or removed from the retrieval instructions" a real question
(§10, Q4).

**`Graph/` is the healthy layer**, and it is the one the restart proposes to
build on. 602 codex entries, 223 claims, 111 world axioms, 97 beats, 56
story-time events, 41 chapters, 26 decisions, 15 scenes, 7 worlds. Plain JSONL,
greppable, line-diffable, ids derived from label + natural key so re-ingest is
idempotent by construction. `Codex/` is its rendered read surface: 644 files,
2.8 MB, written only by `render_codex_views.py`, and `settings.json` enforces
that with `deny: Write(Codex/**)` — the single machine-enforced ownership rule
in the repository.

---

## 3. The tooling, and where Rule 1 actually holds

22 scripts, 5 tool packages. Eight free deterministic gates behind one umbrella
(`kp_check.py`, 1.97 s; 3.75 s with `--chapters`), one paid editorial gate, one
renderer, one ingest, one retrieval command.

**Where Rule 1 holds well.** Four places in the whole surface honour it rather
than describe it, and they are the models worth copying:

- `/kp-world` — the only fully phase-structured derivation, with an
  `AskUserQuestion` checkpoint at each of its 8 layers and a per-layer test.
- `/clarify` — the only command with typed inputs *and* a typed output record
  and a numeric promotability threshold (≥ 0.9). Described in-repo as "Rule 0 as
  a program", which is accurate.
- `/tetraframe` — a verification table with seven named thresholds that must be
  read *before* the synthesis, and a hard rule that it never decides.
- the `lit-critic` skill — which explicitly **refuses** to restate the rule
  table ("the gate consumes it rather than restating it") and documents the
  procedure for changing a rule instead.

**Where Rule 1 does not hold.** `CLAUDE.md` states that `lint_chapter.py` is the
single encoding of the R-rules and that restating them elsewhere is forbidden.
Measured, the R-rules exist in **four** places:

1. `Canon/…welt-sensorik-drafting….md` §10.1 — the full German text, the
   declared origin;
2. `scripts/lint_chapter.py` — which encodes **R-3, R-5, R-8, R-9, R-10 only**,
   and says so in its own docstring at line 7;
3. `WRITING.md` — 210 lines declared machine-readable and read by **zero**
   scripts (`grep -rn 'WRITING\.md' --include='*.py' --include='*.sh'` returns
   nothing);
4. **99 `CodexEntry` records of category `rule`**, which the context packet ships
   into every chapter at 4,411 tokens.

And `.claude/commands/kp-write.md` restates the Act-I fences in §2, then in §3
correctly says never to restate them. The file contradicts itself one section
apart.

**The consequence that matters for the restart:** `lint_chapter.py`'s docstring
states that **R-1 (tragische Ironie), R-2 (show don't tell), R-6 (max. 1 Konzept
pro Szene), R-7 (max. 1 Genesis-Echo) and voice register are deliberately not
encoded**. Their only definition is the Canon file slated for deletion. Four of
ten hard prose rules would have no definition anywhere in the repository. By
`CLAUDE.md`'s own test — *if a rule can be broken without a check failing, it is
prose, not a rule* — those four need either a check or an explicit judgement
marking, and today they have neither.

**Dead or unwired, verified by grepping for callers:** `scripts/export_graph.py`
(reads `.agency/session.db`, which does not exist), `scripts/source_dedup.py` and
`scripts/source_export_mark.py` (379 lines, called by no command or hook),
`scripts/materialize_manuscript.py` (named in `Graph/README.md` as one of four
renderers; **the file does not exist**), `WRITING.md`, and `.venv-dspy` (absent
until this session built it, while three of eleven commands invoke it).

`scripts/lit_critic_gate.py` — the only API-costing gate and the only check that
can see what a lint cannot — **cannot run in this checkout**: `.lit-critic-src`
is absent, so it exits 2, which its own code documents as never a pass.

---

## 4. The dependency that decides the restart

> `scripts/context_packet.py` computes each entry's chapter window by scanning
> `CodexEntry.triggers` against the **manuscript prose**. The retrieval system
> that exists to help write the prose is derived from the prose it is meant to
> help write.

This was verified by simulation against the live graph. With every chapter text
replaced by an empty string, `kpcodex.packet(graph, 3, empty)` returns
`always_on=195, anchored=0, axioms=111`. With title-only stubs, `anchored` is
still 0.

So on day one of the prose restart:

- **the chapter-specific tier collapses to zero.** Every chapter returns an
  identical 12,917-token packet. The tool still exits 0 and still prints a
  cost comment that looks like success. It simply stops discriminating.
- worse, `context_packet.py --chapter N` **exits 2 for every N**, because it
  checks `args.chapter not in chapters` against a dict built from the prose.
  The single most-recommended retrieval command in the repo stops working.
- **218 of the 644 rendered Codex files change content** — every
  "Chapters in play:" line and every chapter-span column across the 20 partition
  READMEs — so `render_codex_views.py --check` goes stale and the SessionStart
  and `kp_check` gates fire until a re-render.
- `chapter_drift.py` flips from `ahead=40 / behind=1` to `behind` on all 41,
  because `Graph/` keeps 55,018 characters of outline while disk goes to zero.
  `CLAUDE.md` and `/kp-check` both document `ahead` as the expected non-defect;
  that documentation inverts.
- the Act-I fences, the Multiplizitäts-Schleier check and the DKT-terminology
  lock become no-ops until prose exists again — a lint over 41 empty files
  passes trivially and proves nothing.

`Plan/wiki/codex-context-inventory_2026-09-16.md` already names this as its
limitation 3, but it was written expecting the window to *strengthen* as the
book gets written. A restart runs that argument backwards into its worst case.

**What the restart therefore requires, and it is not optional:** the chapter
window must move from *derived-from-prose* to *authored-on-the-record*. That
means a real field per `CodexEntry` — `appears_in`, and the `spoiler_until` that
`Graph/schema.yaml` already carries as `status: not-implemented` with
`default_when_unknown: 40`. Without it there is no chapter-N retrieval at all
during the rewrite, which is precisely the period the retrieval exists to serve.

There is a second, quieter version of the same problem. All 15 `Scene` records
and all 97 `NarrativeBeat` records belong to **chapter 0**. `/kp-write` step 1
instructs the agent to call `g.scenes_of(chapter)` then `g.beats_of(scene)`; for
chapters 1–40 both return empty today. The drafting command's "knowledge fence"
step already produces nothing for every chapter the author would write next.

---

## 5. `Canon/` — what leaving actually costs

Verdict from the dedicated verification: **partially covered**. Not covered.

### 5.1 The finding that reframes the question

`scripts/ingest_canon.py` — 552 lines, named for the job, and named in
`CLAUDE.md`'s pipeline diagram as `Canon/ → Graph/` — **never opens a file under
`Canon/`**. It reads only the seven frozen JSON manifests in `Plan/ingest/`
(≈ 580 KB) plus `kap0-clean-body.md`. Its ledger marks all nine phases done,
818 ids, 0 errors.

`/kp-canon` is therefore already a no-op replay of a snapshot, and **`Canon/` is
already not the live source of `Graph/`.** The arrow in `CLAUDE.md` is false
today, before any decision is taken. This cuts both ways: deleting `Canon/` does
not break the ingest — and re-deriving the graph from a corrected source is
already impossible, because the derivation runs from the frozen manifests.

### 5.2 Coverage, per document

| document | words | covered | what is lost |
|---|---:|---:|---|
| `begriffe-und-konzepte` | 7,560 | **95 %** | formatting only — a verbatim twin exists in `Sources/drive/` |
| `philosophie-im-detail` | 6,929 | **95 %** | formatting only — verbatim twin in `Sources/drive/` |
| `kap0-v1-annotiert` | 9,525 | 55 % | TEIL C/D/E (1,479 words, 0 % elsewhere): the graded defect list, the v2 revision recommendation, the methodical anchors |
| `anteile-profile-sprach-dna` | 6,214 | 45 % | §6 the full alter↔alter conflict matrix (526 words, 0 %), §5 Korrelat-Achse, §0 the profile-format reading guide |
| `storyform-und-outline` | 5,946 | 45 % | §0 Querschnitt-Kanon (691 words, 0 %), §1 Strukturelle Achsen, §6, §7, §8 |
| `welt-sensorik-drafting` | 7,412 | 45 % | §10.1 the R-rule texts, §12 Master-Index aller Locks (584 words, 2 of 31 lines elsewhere) |
| `kernwelten-vollstaendig` | 6,476 | **30 %** | §11 Kapitel-Welt-Mapping, §8 Übergänge, §1 Grundsatz, §13 Anti-Patterns, every Sub-Lokalitäten table |
| `README.md` | 209 | **0 %** | the Drive provenance, import date, selection rule, normalization, re-import procedure and the role table naming `storyform-und-outline` the conflict winner |

Two documents are genuinely safe. Six are not. Verbatim line coverage of
`Canon/` inside `Graph/` + `Codex/` runs from 48.1 % (kap0) down to **9 %**
(storyform).

Four losses deserve naming because nothing else in the repository holds them:

- **`Canon/README.md`** holds the corpus's own provenance: where the six
  2026-06-10 documents came from, the selection rule, the normalization applied,
  the re-import procedure, and the role table naming `storyform-und-outline` the
  winner on conflict. **0 of 11 substantive lines** exist anywhere else.
  *(Correction against an earlier draft of this document: the
  `[K]`/`[V]`/`[S]`/`[L]` marker definitions do **not** die with it — they are
  also stated in `Sources/drive/kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md.md`
  lines 2 and 798–800 and in the `philosophie-im-detail` twin, both of which
  survive the deletion. The markers are safe; the corpus provenance is not.)*
- **`kernwelten` §11** assigns each of the 41 chapters to a world. Neither
  `Graph/nodes/chapter.jsonl` nor `world.jsonl` carries a chapter→world
  relation. This is the setting map for the whole book.
- **`storyform` §0** holds the Zentrale Frage, the Ende-Prinzip, the Große
  Inversion, the Formel-Inversion pair and the Akt-I-Benennungslock. The term
  *Benennungslock* occurs in **zero files outside `Canon/`**.
- **`anteile` §6** is the complete conflict matrix across the 13 alters.
  `Codex/entries/character/` holds 18 individual profiles and **no relation
  records** — the profiles survive, the system between them does not.

### 5.3 The silent-pass trap

**All 223 of 223 `NovelClaim` records point into `Canon/`.** Not one points at
`Sources/`. Breakdown: kernwelten 44, philosophie 39, welt-sensorik 34, begriffe
32, anteile 30, kap0 22, storyform 22.

`scripts/audit_graph_claims.py` classifies **by string prefix** and never touches
the filesystem — it fails only on a `source_uri` under `Wiki/`. So after deleting
`Canon/`, all 223 claims still classify as `canon`, the provenance gate still
exits 0, and **`python3 scripts/kp_check.py` stays fully green** while every
claim in the provenance graph cites a file that does not exist. D-W2 would be
formally satisfied by 223 dangling pointers, and no deterministic gate in the
repository would report it.

The same silence applies twice more: `scripts/wiki_fts.py` loses its `canon`
scope (8 files, **356 of 1,272 index chunks**) and returns empty with no error;
`tools/kpwiki/wiki_lint_rules.py → rule_no_auto_canon_page` goes from 3 real
warnings to 0, invisibly. And 605 of the 644 `Codex/` files literally begin
`## Quelle: Canon/…`, which the renderer copies in — the Codex becomes 605 files
of dangling provenance that no check can see.

Beyond that: roughly 30 skill, command, agent, hook and schema files carry dead
`Canon/` paths, the Wiki citation grammar (`entities.yaml:213`) accepts a target
that no longer resolves, and `canon:<file>#<heading>` — one of the three declared
link forms in `AGENTS.md` — loses its referent entirely.

### 5.4 What follows

Deleting `Canon/` today is recoverable (it is tracked; the backup branch exists)
but it is not *safe*, because agents and scripts do not read git history. The
honest sequence is in §8.

---

## 6. Where the tokens go

Measured on this checkout. German ≈ words × 1.4, English ≈ words × 1.3.

**The fixed floor, paid before any work begins:** `CLAUDE.md` 2,957 +
`todo.md` 3,029 (read every session by `CLAUDE.md`'s own instruction) +
`bootstrap.md` 548 = **6,534 tokens**.

**The per-turn tax:** `.claude/hooks/skill-eval.md` is injected on *every*
UserPromptSubmit at ~391–500 tokens. Over a 40-turn drafting session that is
**15,600–20,000 tokens** spent on a routing table that duplicates the command
table already in context — and which is stale on two of the eleven commands.

**The `.claude/` surface:** ~43,900 tokens across 40 files. Roughly a third is
duplicated statement of rules that `scripts/` already enforces; roughly a quarter
documents subsystems that are not present (`.agency/`, 19 vendored worldcodex
skills, `.venv-dspy`); the remainder is genuine judgement worth carrying forward.

**The chapter packet:** 21,713 tokens reported for chapter 3, of which
**8,943 (41.2 %) is the always-on tier** — and that tier is *identical for all 41
chapters*. Following the packet's `--paths` to the 232 files it names costs a
further 31,263. A cold `/kp-write` today totals ≈ 31,995 tokens, or 64,825 with
the paths opened.

**Two measurement defects found in passing**, both worth correcting before any
of these numbers are quoted again:

- `context_packet.py`'s `cost()` charges anchored entries at full body while
  `render()` prints 40-word summaries, so **every published figure — in
  `todo.md`, in `/kp-write`, in `Graph/schema.yaml`'s acceptance test — is ~18 %
  high** for default mode.
- `Graph/schema.yaml` declares the chapter-anchored tier as `form: full body`,
  and `tools/kpcodex` **never emits a full body in any mode**
  (`PREVIEW_CHARS=500`, 10,000 under `--full`). Either the tool is wrong or the
  contract is; today they disagree silently.

**Two gates are red by construction**, not by defect: `kp_check.py`'s
`CHAPTER_GLOB` catches `chapters/README.md` and lints it as a chapter (the sole
cause of "41/42"), and all 12 wiki-health errors are inside
`Wiki/candidates/` — unpromoted drafts that by definition have not been reviewed.

**The measured floor for a useful "write chapter N" packet**, built only from
records that survive the restart, is **≈ 1,750 tokens**: the chapter record
(114) + one Kernwelt's axioms (91–914) + the 30 register/Sprach-DNA bodies
(1,539). Against 31,995 today. That gap is the prize, and it is far larger than
anything trimming the always-on list can buy.

Note what this implies: **removing `Canon/` saves nothing per chapter.**
`Canon/` is 72,753 tokens of duplicated prose, but it is not in the `/kp-write`
path today. The cost win comes from §4's authored chapter window, not from the
deletion.

---

## 7. The proposed model — `Codex/` as the data layer

The author's instinct is right, and one measured fact supports it strongly:
**`/kp-write` already works this way.** It reads `context_packet.py`,
`chapter_drift.py` and `tools/kpgraph`, and names no `Canon/` path. It is the
proof that a Codex-first drafting workflow is possible — it already exists.

What "`Codex/` is the data layer" has to mean, precisely, to be more than a
slogan:

1. **`Graph/` is the data; `Codex/` is its rendering.** Keep that. The
   `deny: Write(Codex/**)` rule is the healthiest thing in the repository and
   should be extended, never relaxed. "Codex as data layer" means *the Graph
   record is the unit of truth and the Codex file is how you read it*.
2. **Provenance must point somewhere that exists.** Every `source_uri` and every
   `## Quelle:` line must resolve to a file on disk, and
   `audit_graph_claims.py` must `stat()` the target rather than string-match the
   prefix. That change is a Rule 1 improvement worth making whether or not
   `Canon/` goes.
3. **The chapter window becomes authored data**, per §4. This is the one new
   capability the restart actually requires.
4. **Record types must exist for what currently lives only in Canon prose**:
   a chapter→world relation (`kernwelten` §11), alter↔alter conflict edges
   (`anteile` §6), a lock record type (`welt-sensorik` §12), and a rule record
   carrying the **full German R-rule text** so that R-1/R-2/R-6/R-7 have a
   definition after the deletion.
5. **The corpus's own provenance needs a home.** The `[K]`/`[V]`/`[S]`/`[L]`
   vocabulary survives in `Sources/drive/` (§5.2), but where the Canon documents
   came from, how they were selected and normalized, and which one wins on
   conflict exist only in `Canon/README.md`.

Items 4 and 5 are the price of decision 1. They are not large — roughly 8,150
words of extraction across five documents — but they must happen *before* the
source leaves the working tree, because afterwards nobody can do them from
inside the repo.

---

## 8. The safe order

Nothing here is executed. This is the sequence the evidence implies.

1. **Freeze, do not delete.** `cp -a Canon/ Reference/canon-2026-06-10/` and
   commit. One command, and the urgency disappears — the workflow gains of the
   restart need `Canon/` to stop being *normative*, not to stop *existing*.
2. **Repoint the 223 claims.** 71 (begriffe 32, philosophie 39) move to their
   verified `Sources/drive/` twins. The other 152 point at the frozen copy.
3. **Teach the gate to see.** Extend `audit_graph_claims.py` to `stat()` each
   `source_uri`. Without this step, steps 1–2 cannot be verified and every
   future breakage of this kind stays invisible.
4. **Extract the five content gaps** into real record types (§7.4), or state in
   writing that they live in the frozen copy. Extraction is the Rule 1 answer;
   freezing is the honest answer; silent deletion is neither.
5. **Give R-1/R-2/R-6/R-7 a check or an explicit judgement marking.**
6. **Author the chapter window** (`appears_in` / `spoiler_until`) before the
   prose is cleared, while the existing prose can still seed it — the current
   manuscript is the only evidence of which entry belongs to which chapter, and
   clearing it first destroys the input.
7. **Then** clear `Manuscript/`, and only then.

Step 6 is the one with a deadline. Every other step can be taken at leisure;
that one has to happen while the prose still exists.

---

## 9. What the workflow redesign inherits

Per the author's decision, this document does not fix a workflow count. It
records what the redesign has to absorb.

**Keep — the four Rule 1 citizens** (§3): `/kp-world`'s per-layer checkpoint
chain, `/clarify`'s typed signature with a numeric threshold, `/tetraframe`'s
verification-table-before-answer, and `lit-critic`'s refusal to restate rules
plus its documented rule-change procedure.

**Consolidation candidates, by evidence rather than taste:**

- `/lint-wiki` (202 lines) and `/full-audit-canon` (143 lines) are one audit
  cycle split by vocabulary — same scope selection, same deterministic pre-pass,
  same contradiction and stale-claim detection, same severity triage, same
  refusal to auto-fix, same `Plan/sessions/` sink. ~6,600 tokens, the two
  largest command files.
- **Four front-ends onto one freshness check** (`/kp-check`, `/lint-wiki`
  Check 0, `/full-audit-canon --quick`, `post-compact-restore.sh`), all reporting
  "views stale → re-render" as their headline.
- **Four overlapping scene/chapter protocols** across `/kp-write`,
  `novel-architect/SKILL.md`, `reference/scene.md` and `reference/structure.md`.
- **The source-authority hierarchy is stated six times and they disagree** —
  `bootstrap.md`'s version includes `Codex/`, `worldbuilder-researcher`'s does
  not. The finer rule rescued in `todo.md` item 1 (written prose wins on
  *details*; report rather than rewrite) is not in any of them.
- **"A lint cannot show what is missing" is stated in five places.** This is the
  repository's sharpest epistemic insight and it has no executable form. The
  `FOUND` / `INFERRED` / `CONFLICTING` / **`MISSING`** ledger is the obvious
  answer, and three of its four buckets are decidable.

**Repair before reuse.** 25 of 92 relative links in `.claude/` are broken, and
24 of them are the *entire* link surface of the five `novel-architect/reference/`
files (off-by-one `../`). Seven commands are referenced that do not exist
(`/kp-decide`, `/wiki-promote`, `/promote-to-canon`, `/wiki-understand`,
`/canon-rules`, `/cross-checking`, `/verifying-completion`). All 14 skill names
in the three agents' frontmatter are missing. `.claude/CLUSTERS.md` tabulates 19
skills of which **zero** exist.

`/kp-decide` matters more than the others: it is the documented exit from every
contradiction the surface can find, and it was never written.

**Also inherited:** the 13 concepts rescued in `todo.md` under "Workflows neu
denken", which still need sorting into tool / schema value / skill / reference —
and item 2 of that list, the five-case "by design, not a contradiction" filter,
is the highest-value single item, because the contradiction ledger from PR #41
lacks it and will otherwise report those five classes as open findings forever.

---

## 10. What only the author can settle

1. **`Canon/`** — freeze at `Reference/canon-2026-06-10/` (§8.1), or delete and
   accept the losses in §5.2 in writing? The decision was "delete"; the evidence
   says the content is not covered. Which governs?
2. **The Codex partition** — the `todo.md` collision is still open: 22
   `Kategorie:` directories (PR #41, built) versus 8 `entity_type` values
   (PR #42, proposed). They are not combinable. `Graph/schema.yaml` +
   `tools/kpcodex` + a re-render is the whole cost of switching.
3. **The chapter window** (§4) — this is the one item with a deadline. What is
   the authored source of `appears_in`: the existing prose mined before it is
   cleared, the chapter outlines in `Graph/`, or `kernwelten` §11?
4. **The research layer** — funded (≈ $1,900 / 8.5 days), deferred, or removed
   from the retrieval instructions? Today it costs ~3,400 tokens of instruction
   per session and returns nothing.
5. **The session floor** — is a task-scoped startup acceptable, so that
   `todo.md` (3,029 tok) is read on planning turns rather than every turn? And
   does `skill-eval.md` earn ~400 tokens on every single prompt?
6. **The agency engine** — `.agency/` is absent and four artefacts assume it,
   including `/full-audit-canon --quick`, which cannot complete as written. Is it
   coming back, or does the gate ladder drop from four rungs to three?
7. **`Codex/`** — do the 644 generated files stay versioned, given they
   regenerate in 0.97 s and `render_codex_views.py --check` detects staleness?
8. **`WRITING.md`** — wire it into `lint_chapter.py`, mark it a generated view,
   or drop it? It has been open since `todo.md` item 13.

---

## Appendix — where the evidence lives

Per-agent reports from the 2026-09-16 anatomy read are in this session's
scratchpad, one JSON file per subsystem: Canon coverage, Graph+Codex,
Wiki+Sources, scripts+tools, commands+skills, Manuscript+Plan, cost+performance.
Every figure in this document traces to one of them, and each was measured
against this checkout at `608cbb5` rather than recalled.

Prior architectural work this document builds on and does not supersede:
`Plan/codex-architecture/{codex-inventory,authority-matrix,overlaps-drift,entity-model-proposal,knowledge-dimensions}_2026-09-16.md`
and `Plan/wiki/codex-context-inventory_2026-09-16.md`.
