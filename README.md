# Kohärenz Protokoll

A German hard-SF novel (cosmic horror / psychological thriller), its research
corpus, and the tools used to develop it. Research readings, approved novel
structure and manuscript drafts have separate authority: a source or a model
cannot decide what becomes canon.

## Start here

| Goal | Entry point |
|---|---|
| Read the novel's working material | [Manuscript](Manuscript/README.md), [canon ledger](Manuscript/kanon.md) |
| Understand the approved plot structure | [Dual storyforms](Plan/storyform/README.md) |
| Find attributed research and disagreements | [Wiki](Wiki/README.md), [Sources](Sources/README.md) |
| Continue current work | [NOW.md](NOW.md), then [CLAUDE.md](CLAUDE.md) and [AGENTS.md](AGENTS.md) |
| Change the architecture | [SPEC.md](SPEC.md), [PRINCIPLES.md](PRINCIPLES.md); [GOAL.md](GOAL.md) is the target brief |
| Find a tool or workflow | [Scripts](scripts/README.md), [project skills](.agents/skills/README.md) |
| Explore the graph | [Graph atlas](Graph/README.md) |
| Inspect decisions and run evidence | [Plan](Plan/README.md) |

The wiki records what sources say, attributed and unmerged. Reviewed candidates
remain research; German term pages distinguish decisions, readings, proposals
and gaps. The manuscript workspace holds canon and working drafts. Approved
storyforms take precedence over draft execution; chapter approval comes only
from the author. The AEGIS agent is a proposed offline pilot, described in the
[pilot briefing](Plan/briefings/aegis-agent-pilot.md), rather than an implemented
interactive novel.

## Local setup

Run commands from the repository root. Standard-library checks need Python 3;
optional retrieval, model and MCP tools use their own virtual environments.

```bash
python3 scripts/knowledge.py init --profile reader
python3 scripts/sessions.py board
python3 scripts/state.py --prose
python3 scripts/account.py order --summary
```

The initializer reports missing capabilities and prepares existing indexes;
`research` is the profile for DSPy work. Inspect its result rather than assuming
all dependencies installed. A documentation-only session can continue without
optional retrieval capabilities. `bash scripts/install.sh --list` lists install
components; `bash scripts/install.sh --check` reports availability.

## App and retrieval

The app is built from repository records by `python3 scripts/web.py`, into
`Plan/derived/web/`. It includes manuscript, wiki, reading questions, graph and
session views, plus `llms.txt`, agent JSON exports and plain HTML records.
[Vercel configuration](vercel.json) enables deployments from `main`; branch
previews are disabled. Building locally does not prove a live deployment or its
access settings.

The read-only MCP endpoint `/mcp` wraps [the serving tools](scripts/rag.py)
through [FastMCP](api/rag_server.py). Local setup and access controls are in the
[engineering guide](docs/README.md). Vercel project protection and the optional
`RAG_MCP_TOKEN` are separate controls; see the current [handover](NOW.md).

## Measured state and verification

**586 <!--state:sources.landed--> of 587 <!--state:sources.total--> documents
are landed; 545 <!--state:documents.reconciled--> are reconciled.** The wiki has
106 <!--state:wiki.pages--> candidates, 17 <!--state:wiki.conflicts--> conflict
records and 9 <!--state:wiki.questions--> shared question records. Reading
question banks are a separate proposal collection.

```bash
python3 scripts/state.py             # measure now; writes Plan/state.json
python3 scripts/sources.py check     # manifest against landed files
python3 scripts/derive.py            # rebuild disposable document views
python3 scripts/selftests.py --only std
```

Run every required step in [checks.yml](.github/workflows/checks.yml) before
finishing a change. Optional environment suites have separate results; skipped
or unavailable is not passed. Historical run READMEs describe their recorded
inputs and dates, not the current repository's health.

A model proposes, never decides. Model calls and corpus transfer follow the
specific author decisions in [CLAUDE.md](CLAUDE.md); no README grants new
provider access or spending permission.

`Legacy/` holds the pre-reset project parked at commit `608cbb5`; it is not runtime input, canon or a manuscript voice reference.

## Licence

See [LICENSE](LICENSE).
