# Tool review — graphify and code-graph-rag (cgr), 2026-09-24

Tested against `scripts/` (code-only) and the two documents consent 007 covers:
`aegis-subplots-kapitelweise-system-exploration-docx`,
`roman-lokalitaeten-konzept-und-ausarbeitung`. Config facts read from
`Plan/concept/tool-review-plan_2026-09-24.md`, "What each tool needs" (graphify
row, cgr row).

## graphify — code-only pass on `scripts/`

```
graphify extract scripts --code-only --out Plan/runs/tooltest/graphify-cgr/graphify-code
```

No model, no API key, 3.3s. Output:
`Plan/runs/tooltest/graphify-cgr/graphify-code/graphify-out/graph.json`.

- **781 nodes, 1685 edges, 24 communities** (script's own report line).
- Edge types (`python3` over `graph.json`, counting `link["relation"]`):
  `calls` 582, `contains` 403, `imports` 227, `rationale_for` 222,
  `references` 98, `imports_from` 83, `indirect_call` 26, `method` 23,
  `defines` 12, `uses` 5, `inherits` 4.
- **Confidence: 1645 EXTRACTED, 40 INFERRED** — the INFERRED edges are all
  `indirect_call` (26), `calls` (9) and `uses` (5); nothing else. So **the
  no-model pass already carries INFERRED edges** — "no API key" does not mean
  "no inference": `--code-only` still guesses some dynamic/indirect call
  targets from static structure. That is a fact worth recording precisely
  because the limit CLAUDE.md states ("a model's reading … may not merge
  surfaces or create a link") is about *model* readings; a heuristic AST
  guess is a different kind of unverified edge and needs its own label if this
  tool is ever used past review.

**Does it show the pipeline (`sources.py → capture.py → reconcile.py`)?**
Not as one chain — and that is correct, not a defect. `sources.py` has no
direct call/import edge to `capture.py` or `reconcile.py`: those are three
separate CLI entry points, connected only by the human-run sequence
`CLAUDE.md`/`.claude/skills/tools/SKILL.md` describe, not by Python imports.
What the graph *does* show, cross-checked against the same edges:

- `capture.py -> subject.py` (calls, imports)
- `reconcile.py -> capture.py` (calls, imports)
- `reconcile.py -> wiki_index.py` (calls ×3, imports, imports_from)

and `subject.py` sits in the top-10 files by edge degree (100 edges), behind
`route.py` (310), `state.py` (304), `sources.py` (166), `entities.py` (153),
`bilingual.py` (150), `graphrag.py` (117), `graph.py` (107), `qmd.py` (104),
ahead of `capture.py` (93). That **confirms in code** the claim CLAUDE.md
makes in prose — "`scripts/subject.py` is the substrate every script asks" —
without needing a model. `state.py`'s high degree matches its role reading
nearly every other module's counters for `Plan/state.json`.

## graphify — document pass, through the router

Setup, per the task and the plan's graphify row:

```
cp Sources/drive/aegis-subplots-kapitelweise-system-exploration-docx.md \
   Plan/runs/tooltest/graphify-cgr/aegis-subplots-kapitelweise-system-exploration-docx/in/
OPENAI_BASE_URL=http://127.0.0.1:8787/v1 \
OPENAI_API_KEY=route:graphify:aegis-subplots-kapitelweise-system-exploration-docx:<attempt> \
graphify extract <dir>/in --backend openai --model free \
  --out <dir>/out-attempt<N>
```

`python3 scripts/route.py guard <slug>` returned "may be sent" for both
documents before anything was sent. The proxy answered `GET /health` with
`{"status": "ok"}` throughout, and `python3 scripts/route.py ledger` showed
other testers' calls (purposes `grawiki`, `hyperextract`) completing by the
hundred on the same proxy in the same window — **so the router and the free
models were reachable and working**; this was not a router outage.

**Neither attempt completed within the run's time budget.** Attempt 1 ran
connected to the proxy (confirmed via `/proc/<pid>/fd` → the socket, and
`strace -p <pid>` showing it parked in `poll()`, i.e. waiting on a response,
not stuck locally) for about 10 minutes with **zero** entries appearing under
`purpose: "graphify"` in `Plan/runs/route/ledger.jsonl`, while `grawiki` and
`hyperextract` accumulated 241+ and 20+ successful chat calls in the same
interval. I killed it and let the script's own loop start attempt 2, gave it
about a minute, then stopped the whole run (`pkill -9 -f "graphify extract"`)
to stay inside the review's time budget. `out-attempt1/` and `out-attempt2/`
are both empty; `grep -c '"purpose": "graphify"' Plan/runs/route/ledger.jsonl`
→ **0**.

**Why no progress showed, reading `scripts/route.py`:** `chat()` (route.py
L293-360) writes exactly **one** ledger row per call, after either a success
or after cycling every free model twice (`for model in models + models`,
L316) — individual per-model failures are kept in an in-memory `tried` list
and only surface in the final row's `why`. So a call that is working through
several 180s-timeout model attempts (`TIMEOUT = 180`, L75) is invisible in the
ledger for however long that takes — up to 2×10 models × 180s in the worst
case. This is a real, reportable gap for anyone trying to babysit a long
tool-test run through this router: **there is no way to see "which model is
being tried right now" from the ledger**, only the final verdict.

This is **not** NOT REACHED in the P15 sense — the tool ran, connected, and
was mid-request — but it did not finish, so per the task's own rule I stopped
it and report exactly this much: two attempts (P18's minimum), neither
answered, no output, no ledger row, and a specific, checkable reason for the
silence. No entity names came out of this pass, so **no `entities.py score`
run is reportable for graphify's document mode** — there is nothing to score.
The `roman-lokalitaeten-konzept-und-ausarbeitung` document pass was not
attempted at all, for the same budget reason.

## cgr — index and verify-index (no model, no database)

```
cgr index --repo-path . -o Plan/runs/tooltest/graphify-cgr/cgr-index \
  --exclude 'Legacy/*' --exclude 'Wiki/*' --exclude 'Sources/*' \
  --exclude 'Plan/*' --exclude '.venv-*/*' --exclude '.git/*'
```

14.7s real. **1315 unique nodes, 3464 unique relationships**, written as a
protobuf index plus `manifest.json` with a sha256 per artifact. Node labels
captured: `Class, Enum, ExternalModule, ExternalPackage, File, Folder,
Function, Interface, Method, Module, ModuleImplementation, ModuleInterface,
Package, Project, Section, Type, Union`. This is Tree-sitter/static analysis,
not a model — no corpus-text or third-party-API rule applies to it, and it
never opened a markdown file (cgr cannot read markdown at all, confirmed by
its own command surface: every subcommand operates on code symbols).

```
cgr verify-index -i Plan/runs/tooltest/graphify-cgr/cgr-index
```
→ `Index verified against its manifest: Plan/runs/tooltest/graphify-cgr/cgr-index`
(exit 0). Both commands ran clean, fast, and need nothing this container
lacks.

## cgr — check / stats / dead-code / duplicates / export / start: NOT REACHED

Confirmed directly, not assumed: `cgr stats` (which reads the same graph
`check`/`dead-code`/`duplicates`/`export` read, over the shared Memgraph
database rather than the offline index) failed with
`mgclient.TransientError: couldn't connect to host: Connection refused`
against `localhost:7687`. `docker ps` and `docker info` both failed with
`failed to connect to the docker API at unix:///var/run/docker.sock: … no
such file or directory` — **the docker CLI (29.3.1) is present but no daemon
is running in this container**, so nothing can bring up a Memgraph container
here. This matches the plan row exactly ("`check`, `export` and `start` need
Memgraph on :7687 — not reached unless docker runs it here"). **NOT REACHED**,
and what would reach it: a container image or environment with a running
`dockerd` (or a remote Memgraph endpoint this container can reach over the
network), so `cgr check`/`start` can open a real connection — that is an
environment decision, not a code fix on either side.

**What `cgr check` could give the 0-check phase, per its own `--help`**
("Report the structural delta of the working tree against a git ref: dangling
callers, arity findings, new duplicates, new import cycles, tests reaching the
edited symbols", with `--fail-on-found` for a red/green exit): that is close
in shape to what `.claude/skills/tools/SKILL.md`'s 0-invariants table already
does with `judgements.py`, `quotes.py`, `relations.py` — a check that is red
or green and names what's wrong. Two differences worth naming before
recommending it: (1) it is scoped to `scripts/`'s Python, so it could only
ever be one more invariant alongside the existing seven, never a replacement
for any of them; (2) it needs Memgraph, i.e. a stateful service this
repository's checks otherwise avoid (every other 0-check is a stdlib script
against files on disk). Untested here — this is a reading of the `--help`
text, not a run.

## Corpus-text rule and route

Both documents were within decision 007's consent (`route.py guard` confirmed
"may be sent" for each), and every API key used the required label
`route:graphify:<slug>:<attempt>`. No call to a provider that ignores the base
URL was made; `--backend openai` was used throughout, pointed at the proxy.
The router refused nothing here — the two attempts never got far enough to be
refused or answered.

## Where output of each tool could go, under CLAUDE.md's limits

- **graphify `--code-only` on `scripts/`**: a model plays no part in this
  pass, so it is not "a model's reading" in the sense CLAUDE.md restricts —
  but its `indirect_call`/`calls`/`uses` INFERRED edges are still a *guess*
  (static-analysis heuristic, not a stated fact), so treat them the same way
  as any other inferred edge: fine as an engineering-diagnostics artifact
  under `Plan/runs/`, never as something that supplies a page, a `[[link]]`,
  or a count about the wiki or corpus. It has nothing to do with `Wiki/` or
  `Sources/` at all — it only ever reads `scripts/`.
- **graphify document mode**: would be a model's reading of German corpus
  text, under the same limits as `knowledge-graph-extract` — no page, no
  link, no count, no conflict detection, output kept outside `Wiki/` and
  `Sources/`. Untested here; nothing to place yet.
- **cgr index/verify-index**: static analysis of `scripts/`, same standing as
  graphify's code-only pass — a diagnostics artifact, never a corpus reading.
  Could sit next to graphify's code graph as a second, independently-built
  cross-check of the same claim (does `subject.py` really carry the load the
  prose says it does), since the two tools use different techniques
  (LLM-assisted clustering vs. pure Tree-sitter) and agreeing would be worth
  more than either alone.
- **cgr check/stats/dead-code/duplicates**: not reached, so no output exists
  to place. If it ever runs, its findings (dangling callers, import cycles)
  are exactly the shape of the existing 0-check outputs and belong beside
  them under `Plan/runs/`, never in `Wiki/`.

## Names scoring

`python3 scripts/entities.py score <slug> --names <file.json>` requires a
names file. **Not run** — the document pass that would have produced names
did not complete (see above), so there is nothing to score. No first-two-lines
to paste.

## Recommendations

1. **`graphify extract scripts --code-only`** as a periodic, no-model
   architecture snapshot. Evidence: 3.3s, 781 nodes/1685 edges, deterministic,
   confirms the `subject.py`-as-substrate claim in code rather than only in
   prose. May not: touch `Wiki/`/`Sources/`, or have its INFERRED edges (2.4%
   of the total) treated as fact. Verdict: **trial** — worth running again
   after a `scripts/` change to see whether the community/edge counts move in
   the direction expected, before it earns a place in the 0-check list.

2. **graphify document mode (`--backend openai` via the router)**: two clean
   attempts, both unanswered within budget, no output, and a located reason
   (the router's per-call, not per-model-attempt, ledger logging hides
   progress during long retries — not graphify's fault, but it makes this
   combination hard to operate and debug together). Evidence: the run logs
   above and `scripts/route.py` L293-360. May not: create a page, link, count,
   or detect a conflict, even if it had produced output. Verdict: **park** —
   not because the idea is bad, but because this test could not tell whether
   the failure is the free-model rotation, the document's size, or something
   about graphify's request shape; re-test with a single, shorter excerpt and
   `route.py complete` directly (bypassing graphify) to isolate which layer is
   slow, before spending another full budget on the combined stack.

3. **`cgr index` + `verify-index` on `scripts/`**: fast (14.7s), verifiable
   (sha256 manifest, `verify-index` passed), needs nothing this container
   lacks. Evidence: run above. May not: read `Wiki/`/`Sources/` at all (cgr
   cannot read markdown), so it can only ever describe `scripts/`. Verdict:
   **trial** — as a second, independently-built cross-check of the same
   architecture claim graphify's code-only pass makes, run alongside it rather
   than in place of it.

4. **`cgr check`/`stats`/`dead-code`/`duplicates`/`export`/`start`**: NOT
   REACHED — confirmed absence of a docker daemon
   (`/var/run/docker.sock` missing) blocks every Memgraph-backed command.
   Evidence: `docker info` and `cgr stats` errors above. What would reach it:
   a container with a running `dockerd`, or network access to an external
   Memgraph. Verdict: **park** — cannot be judged from a state where it
   cannot run; revisit only if the container gains a docker daemon.
