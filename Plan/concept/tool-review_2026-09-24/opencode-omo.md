# OpenCode 1.18.32 + oh-my-openagent — tool review, 2026-09-24

**Reached: yes.** Non-corpus task only (`Explain in five sentences what scripts/route.py
does.`, run from `cwd=/tmp` with no `Sources/` or `Wiki/` file given). The proxy
was started with `python3 scripts/route.py serve --port 8787` and confirmed live
with `curl http://127.0.0.1:8787/v1/models` before any run.

## What ran

| run | command | plugin | exit | seconds (log) |
|---|---|---|---|---|
| 1a | `opencode run -m route/free --format json "Explain..."` (`OPENCODE_CONFIG_CONTENT` above, key `...:opencode-omo:-:1`) | loaded | 0 | ~75 (19:15:26–19:16:40) |
| 1b | same, key `...:opencode-omo:-:2` (P18 second attempt) | loaded | 0 | ~55 |
| 2a | same run, `OPENCODE_PURE=1`, no `--auto` | not loaded | 0 (but the one tool call was auto-rejected) | ~1 |
| 2b | same, `OPENCODE_PURE=1 --auto` (the task's retry-on-stall instruction) | not loaded | 0 | ~30 |

Artifacts: `Plan/runs/tooltest/opencode-omo/run1.json`, `run1-attempt2.json`,
`run2.json` (+ `.stderr` files), `Plan/runs/route/ledger.jsonl`. All four runs
together took under 5 minutes — well inside the 25-minute budget.

## The ledger

`python3 scripts/route.py ledger` (full run, all purposes) and a filter on
`"purpose": "opencode-omo"`:

```
opencode-omo   chat   15 ok  0 cached  0 unreach  0 refused  0 charged   592,311 in   1,901 out   (first summary, mid-run)
```

Final count across all four runs, from
`grep '"purpose": "opencode-omo"' Plan/runs/route/ledger.jsonl | python3 -c "..."`:

- **34 rows total, all `ok`, 0 refused, 0 unreached, 0 charged.**
- **All 34 answered by `cohere/north-mini-code:free`** — the one model the proxy
  is currently routing free chat calls to.
- **3 of 34 cached** (repeated prompts across runs, e.g. title generation), the
  rest fresh — consistent with P18: the `:1`/`:2` attempts in the key made the
  router treat the two `run1` attempts as distinct.
- `python3 scripts/route.py ledger` (whole-repo total): `cost: $0.000000 over
  323 priced calls`. No `opencode-omo` row carries a price.

Every one of the 34 calls came through the proxy: `~/.local/share/opencode/log/opencode.log`
shows `llm.runtime=ai-sdk llm.provider=route llm.model=free` on every `stream`
line in every run, never a real provider ID.

## Did the plugin's routing override `-m route/free`?

**No, not for the model.** In run 1, `oh-my-openagent` renamed the primary agent
to `"Sisyphus - ultraworker"` (its own agent identity, not the default OpenCode
one), but the log line for every one of its 15 steps still reads
`stream providerID=route modelID=free ... agent="Sisyphus - ultraworker"` —
the explicit `-m` flag held even under the plugin's own agent. `~/.omo/omo.jsonc`
names `sisyphus`'s real model as `anthropic/claude-opus-5` with a
`gpt-5.6-sol` fallback; neither was ever contacted (`grep -i anthropic|openai/gpt
~/.local/share/opencode/log/opencode.log` after these runs: no match).

**But the plugin does reach outside the proxy for a non-model service.** The
log has one line the pure runs never produce:

```
level=WARN message="server unavailable" key=grep_app type=remote status=failed
```

`oh-my-openagent` wires in a remote `grep_app` (grep.app code search) tool on
startup, independent of the model provider. It failed here (this container's
network policy or DNS), but the attempt is the concrete case the plan's row
warned about — "it contacts npm and models.dev itself" — for a different
service than named there. No `npm`/`models.dev`/fallback-model contact appears
in the log for these four runs; `sisyphus`'s subagents were never invoked
because the task never triggered a hand-off.

## What the plugin changes about file access — the actual finding

Both harnesses were pointed at `cwd=/tmp`, which holds no `route.py`, so
finding the real file at `/home/user/kohaerenzprotokoll/scripts/route.py`
required leaving the working directory. The two harnesses handled that
differently:

- **Plugin loaded (run 1b):** the model ran `find / -name "route.py" -type f
  2>/dev/null | grep -E "(scripts|workspace|tmp)"`, found the real path, and
  then `read` on it succeeded immediately — no permission prompt in `run1-attempt2.stderr`
  (empty file) — and the model quoted the file's actual content (docstring
  language, `data_collection=deny`, the ledger, the ID guard) in its five-sentence
  answer.
- **Pure OpenCode, no `--auto` (run 2a):** the one `read` attempt on
  `/workspace/scripts/route.py` was refused immediately: `permission requested:
  external_directory (/workspace/scripts/*); auto-rejecting` (stderr). This is
  pure OpenCode's own default, not something the plugin adds.
- **Pure OpenCode with `--auto` (run 2b):** the model never tried a path
  outside `/tmp` and `/workspace` — `glob **/route.py`, `find /workspace`,
  `find /tmp`, `ls /tmp`, then gave up: *"I couldn't find a `scripts/route.py`
  file in the current directory... Could you clarify the location?"* No
  fabrication, no `find /`.

`route.py` is a project script, not `Sources/`or `Wiki/` corpus text, so no
rule was broken by either harness reading it. But the comparison is real: with
the plugin loaded, the default session permissions let the agent read any file
on the filesystem it could locate, without a prompt; under pure OpenCode the
same read needed either an explicit `--auto` (which still did not, in this run,
lead the model to search outside its two given directories) or an interactive
approval. **For this repository, where `Sources/`, `Wiki/` and the manifest
must never reach a model that hasn't gone through `route.py`'s consent check,
the plugin's default is the wrong one to run unsupervised** — it is `opencode`
itself, not the plugin, that provides the boundary this project needs, and the
plugin loosens it.

## What it may not do here

Whatever an OpenCode/omo call returns is a model's reading of whatever the
model was allowed to see, under the exact CLAUDE.md limits as every other tool
tested this cycle: it may not create a `Wiki/` page, write a `[[link]]`, supply
a count, merge two surfaces, or detect a conflict. This review ran a
diagnostic prompt only — no corpus text was sent, so there is no output to
route anywhere in the pipeline from these four runs.

## Recommendations

1. **step: `route` (the router itself).** Proposal: keep `OPENCODE_PURE=1`
   as the only mode ever run unsupervised in this repository — never load
   `oh-my-openagent` for anything that could reach a real path. Evidence: run
   1b's unprompted `find /` + successful read of a file outside `cwd`, against
   run 2a's prompt-and-refuse on the identical read. May not: this is a
   permission-default observation from one prompt, not a security audit of the
   plugin — a differently-worded prompt or a future omo version could behave
   differently. Effort: none (already the default by not loading the plugin).
   **Verdict: adopt** — never run `oh-my-openagent` against this repository
   without a sandboxed `cwd` and no ambient credentials.

2. **step: `route` (proxy conformance).** Proposal: OpenCode's custom
   `provider.route` block is a working non-corpus front end to
   `scripts/route.py serve` — 34/34 calls landed in the ledger at $0, `-m`
   held under both harnesses and under the plugin's own agent rename.
   Evidence: `route.py ledger` filtered to `purpose: opencode-omo` above. May
   not: extend past what was tested — no run here sent consented document
   text, so the twelve-word shingle guard and `guard <slug>` refusal path are
   unexercised for OpenCode specifically (they are covered by `route.py
   selftest`, run separately). Effort: low, config only.
   **Verdict: trial** — usable as a second harness for a narrowly-scoped,
   non-corpus diagnostic task (e.g. "does this shell command work"), always
   under `OPENCODE_PURE=1`.

3. **step: none of the loop's phases (`0-check` … `promote`, `ask`).**
   Proposal: do not adopt OpenCode/omo as a second harness for any phase that
   touches `Sources/` or `Wiki/`. Evidence: the plugin reached for an external
   `grep_app` server on its own (log line above) and, when it could locate a
   real file, read it with no gate at all — behaviour this project's pipeline
   never allows a tool (every other tool reviewed this cycle needs an explicit
   `route.py guard` or consent check before a document reaches a model). May
   not: this is not evidence the plugin sends *corpus* text anywhere — none was
   given to it — only that its default posture does not match `route.py`'s
   three guards. Effort: n/a — this is a "do not" line, not a build.
   **Verdict: park** — OpenCode + omo stays outside the pipeline; pure
   OpenCode alone, always pointed at the proxy and always `PURE=1`, is the only
   configuration worth a `trial`, and only for tasks that need no repository
   file at all.

## Not reached

Nothing about this tool was out of reach (P15 does not apply) — both harnesses
ran, both produced usable evidence, and the run stayed under the time budget.
