# Installing anything — the venvs, the vendored skills, the third-party tools

*Moved here word for word from `CLAUDE.md` on 2026-09-29 (decision 015).*


**Every dependency goes into a virtualenv. Never into the system Python.**

`pip install --break-system-packages` was tried once and broke `cryptography`
for the whole container, which took the system interpreter down with it.

```bash
python3 -m venv .venv-tools
.venv-tools/bin/pip install <package>
```

`.venv-tools/` holds the tooling dependencies — markitdown and its converters
today — and is git-ignored. `scripts/sources.py` stays standard-library and
shells out to that interpreter for the one thing that needs it, so the tool
keeps running whether or not the venv exists and says exactly how to create it
when it does not.

Seven venvs are defined, all git-ignored, each for one reason. **None survives a
container**; `scripts/install.sh` rebuilds each, and the commands below are what
it runs:

| venv | python | why |
|---|---|---|
| `.venv-tools` | 3.11 | markitdown and its converters, for `sources.py land` |
| `.venv-dspy` | 3.11 | DSPy 3.3.1 with numpy and Deno — every `scripts/` step that calls a model or its fixture |
| `.venv-dspytools` | **3.12** | `dspytools`, which refuses 3.11 |
| `.venv-typesafe` | 3.11 | `typesafe-sdk`, for Jev — `scripts/jev_entities.py` (a test) and `scripts/bilingual.py` |
| `.venv-grawiki` | **3.12** | `grawiki[falkordblite,viz]` from `netzkontrast/grawiki` at `920d181`, which refuses 3.11; about 2 GB with CPU torch |
| `.venv-semantica` | 3.12 | `semantica==0.7.0`, the base package without extras — a knowledge-graph library with provenance tracking; about 480 MB |
| `.venv-mflow` | 3.11 | `mflow-ai`, M-flow's graph memory — nothing calls it |

```bash
uv venv --python 3.11 .venv-dspy
uv pip install --python .venv-dspy/bin/python 'dspy[deno,numpy]==3.3.1'   # SIMBA raises without numpy; dspy.RLM needs Deno
.venv-dspy/bin/python scripts/check_dspy_surface.py                        # the surface this repo calls
.venv-dspy/bin/python scripts/check_dspy_skill.py                          # the DSPy the dspy skill teaches
```

```bash
uv venv --python 3.12 .venv-dspytools
uv pip install --python .venv-dspytools/bin/python git+https://github.com/netzkontrast/dspytools
DSPYTOOLS_SKILLS_DIR=$PWD/.agents/skills .venv-dspytools/bin/dspytools skills list
```

```bash
uv venv --python 3.11 .venv-typesafe
uv pip install --python .venv-typesafe/bin/python git+https://github.com/typesafe-ai/typesafe-sdk-python
```

The key comes from `TYPESAFE_API_KEY` in the environment and is never written to
a file here. **Every call sends text to a third-party API**, so no corpus text
goes through it until a person has decided it may —
`Plan/concept/jev-in-ingestion_2026-09-23.md` has where it may help and where it
may not.
`.agents/skills/typesafe` is how to build with it: question wording, composition,
the limits the TypeSafe cookbooks measured, and the SDK as installed.

**`.claude/skills/jev*` is a vendored third-party collection**, not this project's
skills: eleven folders copied unchanged from `wuyoscar/jev-skill` tag `v0.2.0`,
commit `82c01055c80fa96d3e8a1b82132361693b6bf3a1`, MIT. They are real folders in
`.claude/skills/`, not symlinks into `.agents/skills/`, so `rlm_ingest.py`'s
`SkillManager` does not render them into its prompt. Their CLI is not in the
repository and does not survive the container:

```bash
git clone --depth 1 --branch v0.2.0 https://github.com/wuyoscar/jev-skill /tmp/jev-skill
uv tool install /tmp/jev-skill            # provides jev-decide; standard library only
jev-decide setup                          # which key is present — never its value
```

The route chosen for them is **A, real Jev**. Both keys are present in the
environment's settings as of 2026-09-23, never in chat or a file here. Every call still
needs the author's yes before corpus text is sent (see above).

**Four more vendored folders are Notion skills**: `knowledge-capture`,
`meeting-intelligence`, `research-documentation` and `spec-to-implementation`,
copied unchanged (plus its `LICENSE`, MIT) from `netzkontrast/notion-skills`
commit `e1bab42f8337b93b833eb01d9edcde067125690f`, path
`plugins/notion-skills/skills/`. They are vendored rather than installed as a
plugin because that repository's `.claude-plugin/marketplace.json` fails
`claude plugin validate` — its `skills` field lists bare names where paths are
expected — so a settings-registered plugin would not load.

Their `NOTION_API_TOKEN` configuration does not apply here: Notion is reached
through the claude.ai Notion connector (`mcp__Notion__*`), which carries its own
auth, and no token is written to a file. Notion is outside the two layers: no
script reads it, and nothing in `Wiki/` or `Sources/` may cite a Notion page.
Anything sent there is corpus text leaving the repository, so the same rule as
Jev applies — the author's yes first.

**`.claude/skills/knowledge-graph-extract` is vendored too**, copied unchanged
(plus its `LICENSE`, MIT) from `netzkontrast/knowledge-graph-extract` commit
`542fffaeaf18f4db6eb3f32c7a93c2c54822f67c`. It has a model read a folder of
documents into subject–relation–object triples, with four standard-library
scripts to validate them and write Cypher. Its manifest passes
`claude plugin validate`; it is copied rather than registered only so all
third-party skills sit in one place, pinned the same way.

A triple it writes is a model's reading, in the same standing as an entity list:
it may not create a page, write a `[[…]]` link, supply a count, or merge two
surfaces — a guessed edge is indistinguishable from a stated one once it is in
the graph (see *The wiki links*). Its output directory goes outside `Wiki/` and
`Sources/`. Nothing in the pipeline calls it yet. **Run once, 2026-09-24, as a
second reader on document 14**, with Claude as the model so no text left: 200
triplets in 35 minutes, F1 0.37 against the reader's list, the best second reader
measured —
`Plan/runs/koharenz-protokoll-strukturierter-outline-2026-05-18-md/second-readers/README.md`, which also measures what
makes it faster.

**`.claude/skills/graphify` is the skill `graphify install --project` writes**,
from `netzkontrast/graphify` commit `4c735618f3d56fd622c2049771584621c31ba9ff`
(graphify 0.9.67, Apache-2.0 with MIT and NOTICE copied beside it). It drives the
`graphify` CLI, which is not in the repository — see the table at the top. Only
the skill folder was kept. The same install also appends rules to `CLAUDE.md`
and registers `PreToolUse` hooks on `Bash|Grep` and `Read|Glob` that run
`graphify hook-guard`; neither is here, because in a fresh container the binary
is absent and every one of those calls would run a failing hook, and the rules
would route questions to a graph ahead of `read.py`, `corpus.py` and qmd.
Its `INFERRED` edges are a model's reading under the same limits as
`knowledge-graph-extract`, and `graphify-out/` is git-ignored. Its document mode
needs no key — the skill has the host agent read — and ran once that way on
document 14 (the same README): its AMBIGUOUS edges found four of the document's
inner tensions by themselves.

Two packages make a `SKILL.md` written here reachable from DSPy rather than only
from a person, and they do different halves of it:

```bash
# the runtime half — a ReAct agent that discovers, activates and uses skills
uv pip install --python .venv-dspy/bin/python --no-deps \
    git+https://github.com/netzkontrast/dspy-skills-implementation-
uv pip install --python .venv-dspy/bin/python strictyaml

# the management half — list, search, compile and optimise skills as artifacts
uv venv --python 3.12 .venv-dspytools
uv pip install --python .venv-dspytools/bin/python git+https://github.com/netzkontrast/dspytools
```

`dspy_skills.SkillManager([Path(".agents/skills")])` discovers every skill
here, and `generate_skills_prompt_block(manager)` renders the
`<available_skills>` block a ReAct agent is given. **That block is built from the
`description` field and nothing else** — which is why the description is the part
worth optimising, and `dspy-book-coding-agents` optimises exactly that kind of
text with GEPA's `optimize_anything`.

`--no-deps` is load-bearing: the package asks for `dspy-ai>=2.5.0`, the old
distribution name, and resolving it would move this venv off the pinned DSPy
3.3.1.

A third, `drg-kg`, is installed for one module only — its evaluation scorer,
whose `_prf` returns **0.0** where the retired pipeline's `coverage()` returned
1.0. Its extraction and graph layers stay unused, because a canon link is
written by a person and never inferred by a model — not because the wiki has no
links. It has 681 <!--state:wiki.relations-->.

```bash
uv pip install --python .venv-dspy/bin/python "drg-kg[extract] @ git+https://github.com/netzkontrast/drg-kg"
```

**Nothing in the pipeline calls any of the three yet.** They are installed,
reachable, and measured against this repository —
`Plan/concept/continuous-improvement_2026-09-17.md` has what each is for and in
what order.

`grawiki` is a library, not a skill: a model reads chunks of a document into a
graph held in FalkorDBLite, a local file with no server. It stands where
`knowledge-graph-extract` stands — the same author's framework, of which that
skill is the counterpart — and under the same limits: its graph is a model's
reading and supplies no page, link or count. `--torch-backend cpu` is
deliberate: `chonkie[st]` pulls sentence-transformers, and a container has no GPU.

`code-graph-rag` (`cgr`) is a uv tool on Python 3.12. Without
`--with "transformers>=4.40"` the resolver falls back to transformers 4.12.2,
whose tokenizers needs a Rust build that fails.

`semantica` is a library in the same family: context graphs with provenance
and reasoning over them. Only the base package is installed — its LLM, document
and embedding extras are not — so it builds and queries graphs a caller hands
it and extracts nothing by itself.

All three are installed and start; none has been run against the corpus, and
nothing in the pipeline calls them. Their graphs stand under the same limits as
`knowledge-graph-extract`: no page, link or count comes from one.

**Hyper-Extract** (`netzkontrast/Hyper-Extract` at
`395039ea49709b279971631a47569b931818abbb`, Apache-2.0). **The pipeline does not
need it:** the part a contract run uses — loading a template, its prompt and JSON
schema, the chunks, the merge — is ported to `scripts/hx.py` in the standard
library (decision 020), and `python3 scripts/hx.py parity` compares the port with
this package over every template and every landed document's chunks. It is not
installed at session start; `scripts/install.sh hyperextract` installs it on
demand, as three things:

- **`he`**, a uv tool on Python 3.12 with the `mcp`, `ingest` and `anthropic`
  extras. `he parse` has a model read documents into a *Knowledge Abstract* —
  a graph, hypergraph, list or record set shaped by a YAML template — and
  `he template validate` checks a template without any model.
- **`he-mcp`**, an MCP server whose nine tools read and export an existing
  Knowledge Abstract (`list_templates`, `info`, `search`, `ask`,
  `export_obsidian|graphml|csv|jsonld|cypher`); none of them extracts, and the
  pipeline writes no Knowledge Abstract, so it is no longer registered in
  `.mcp.json` (it failed every session it was not yet installed in).
  `install.sh hyperextract` links `he` and `he-mcp` into `/usr/local/bin`, because
  Claude Code starts an MCP server with the PATH it was launched with, which lacks
  `~/.local/bin`; to use it, `claude mcp add hyper-extract -- he-mcp`.
- **Seven template-design skills**: `hyper-extract` (the entry point) and
  `hyperextract-brainstorm`, `-record-designer`, `-graph-designer`,
  `-yaml-validator`, `-template-optimizer`, `-multilingual`. Upstream nests them
  in one `hyperextract-skills/` folder, which Claude Code does not discover, so
  each is its own top-level folder with the prefix added; every file is
  unchanged. Two of the bundled cases, `battle-analysis.yaml` and
  `biography-events.yaml`, fail `he template validate` (HE-T001, not parseable)
  as shipped.

No provider is configured. `he` reads `~/.he/config.toml` and falls back to
`OPENAI_API_KEY` and `OPENAI_BASE_URL`; the key goes in the environment's
settings or `he config`, never in this repository. `he parse`, `search` and
`ask` send text to that provider, so the Jev rule applies — the author's yes
before corpus text goes. A Knowledge Abstract is a model's reading under the
same limits as `knowledge-graph-extract`: no page, link or count comes from it,
and it is written outside `Wiki/` and `Sources/`.

**The project's templates** are the 32 contracts in `Plan/hyperextract/`
(`Plan/concept/graph-contracts_2026-09-30.md` has the catalogue); a run is
`python3 scripts/he_claude.py run`, on the port. The stock `he parse` cannot load
them by path, `python3 scripts/templates.py parse` can. `python3 scripts/templates.py check`
holds them to Hyper-Extract's validator and to loading as a run loads them — both on
the port, so no install is needed; the upstream validator passed a field that loading
rejects — and to five rules of this project: no line field (P26), no
model merge (P13), an explicit merge strategy, the provisional header, and no
corpus name in any text a model is sent. `selftest` shows each check failing on
its defect. `Plan/concept/hyperextract-templates_2026-09-24.md` has the design,
the optimiser's report and how each is scored.

**oh-my-openagent** is a different kind of thing from everything above: not a
library or a skill for Claude Code but a plugin for another agent harness,
[OpenCode](https://opencode.ai). `scripts/install.sh omo` installs
`opencode-ai@1.18.32` with npm and runs the plugin's own installer at `4.19.4`
with the author's answers (2026-09-24): OpenCode, Claude Max 20×, ChatGPT Plus,
Gemini, no Copilot. That writes `"oh-my-openagent@latest"` into
`~/.config/opencode/opencode.json` — so OpenCode loads whatever is newest, not
the pin — and the agent → model routing into `~/.omo/omo.jsonc`: `sisyphus` on
`anthropic/claude-opus-5`, `oracle` on `openai/gpt-5.6-sol`, and so on down its
roster. Both files are outside the repository and regenerated per container.

What it does not do, and why:

- **No provider is signed in.** It runs with `--skip-auth`; `opencode auth login`
  is a browser OAuth flow a container cannot finish, and its tokens would live
  in `~/.local/share/opencode/auth.json`, which the container loses. OpenCode
  with this plugin is usable where the author signs in — their own machine —
  and here only as far as `doctor` and `opencode agent list`.
- **`config migrate` is not run.** At 4.19.4, `doctor` reports the installer's
  own `variant`/`fallback_models` keys as deprecated and names `config migrate`
  as the fix; the migration rewrites agents to `models`, which the same
  validator then rejects, and `doctor` goes from warnings (exit 0) to eight
  errors (exit 1). The installer's output is kept as it writes it.
- `doctor` also warns that `sg` (ast-grep) and `gh` are absent. Neither is
  installed.

Its telemetry is on by default; `OMO_SEND_ANONYMOUS_TELEMETRY=0` turns it off.
Anything an OpenCode agent reads from the corpus goes to the providers above,
so the Jev rule applies to it as to everything else here.

**M-flow is installed on its own**, from the fork `netzkontrast/m_flow`, which
has no commits of its own. Its head, `0d585cd` of 2026-08-03, is an upstream
commit:

```bash
uv venv --python 3.11 .venv-mflow
uv pip install --python .venv-mflow/bin/python "mflow-ai @ git+https://github.com/netzkontrast/m_flow"
.venv-mflow/bin/mflow --help                # runs with no key and no network
```

It is not in `.venv-dspy`, because resolved beside DSPy 3.3.1 it moves four of
DSPy's packages down, `pydantic` 2.13.5 → 2.12.5 among them. It builds a
four-level graph — Episode → Facet → FacetPoint → Entity — in file-based Kuzu,
LanceDB and SQLite, and by its own account scores each Episode by the cheapest
path of evidence to the query. **Its default path breaks two rules this wiki
keeps:** `memorize` has a model write the Facets and FacetPoints, and `search`
has a model write the answer. Both steps call OpenAI by default, for the model
and for the embeddings, so running either on corpus text sends that text to a
third party. That waits on the author's yes. Its own unit suite passes 1232 of
1235, run against the installed package with every key hidden and the network
dead. One test is skipped, and the two failures time out retrying the embedding
call. Even `mflow add` refuses without a model key, because every pipeline run
first probes the model and the embeddings with the word „test". It writes only
inside the venv. **Nothing calls it.**
`Plan/concept/m-flow_2026-09-24.md` has the measurement, the two entry points
that keep the rules (`manual_ingest` and `search(only_context=True)`), and the
experiment that would decide whether it earns a place.

**Jules** is Google's remote coding agent: a session clones a GitHub repository
into a VM, plans, edits and publishes a branch. `scripts/jules.py` spawns and
drives one, standard-library, ported on 2026-09-26 from `netzkontrast/agency` —
the REST client, the dispatch preamble and its tool lint, `verify`, and the
watcher's reading of a state as `triage`; `.agents/skills/jules` says how to use
it, with agency's doctrine, and `references/agency.md` maps each piece to its
source. The watcher's loop and the patch-recovery planner were not ported. The
key is `JULES_API_KEY` in the environment's settings. **Three refusals are
code**: `dispatch` and `message` refuse without `--approval` naming the author's
decision, because a session is the whole repository, corpus included, on
Google's machines; `dispatch` refuses a prompt that does not name `submit` and
the other canonical tools; and `verify` reads COMPLETED as done only when
`git ls-remote` finds the branch. Every effect is a line in
`Plan/runs/jules/ledger.jsonl`. The reads were run against the live API from a
cloud session on 2026-09-26 — this repository is a connected source, `triage`
read a finished session in under four seconds. **One session has been
dispatched** (decision 014): an ingest of
`kohaerenz-protokoll-philosophischer-bericht-md`, on 2026-09-27. It ended
COMPLETED with no candidate list, census, note, judgement or reconciliation
record, while its description claimed all of them; decision 014 has the
measurement. The author merged its pull request, and the document was then read
in full as document 31.

