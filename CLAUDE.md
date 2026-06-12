<!-- agency:onboarding:start -->
## Agency plugin — onboarding (auto-generated, do not edit between markers)

This repo carries an `.agency/session.db` provenance graph (Spec 020 —
committed to git so team learnings travel with the repo).

### Wire contract — 3 tools (CORE.md)

The agency MCP server exposes ONE lean contract:

| tool | purpose |
|---|---|
| `search` | discover capabilities + verbs by keyword |
| `get_schema` | fetch parameter schemas for a found verb |
| `execute` | run a Python block; chain `await call_tool(...)` calls inside |

Plus four engine-substrate onboarding tools:

- `agency_welcome` — one-shot first call; returns the wire contract +
  a chained code-mode example + the live capability tier + the discipline-
  skills roster + the resolved DB path. **Start here.** No intent_id.
- `agency_install` — scaffold `.agency/` + refresh this snippet. Idempotent.
- `agency_doctor` — health check (Spec 030): python version, deps, DB
  reachability, env-var presence. Call when something silently fails.
- `intent_bootstrap` — mint AND confirm the Intent every verb SERVES
  against. The only tool that does NOT require an existing `intent_id`.

### Code-mode chaining — one block, one return

`execute` runs ONE Python block in a sandbox; every `await call_tool(...)`
inside crosses NO extra wire hops; ONE value crosses back. Chain instead
of per-call — it's the headline win of the substrate.

```python
await call_tool('execute', {'code': '''
    # 1. mint the intent every cap verb will SERVE
    iid = (await call_tool("intent_bootstrap", {
        "purpose": "<why>", "deliverable": "<what>", "acceptance": "<verify>",
    }))["intent_id"]
    # 2. chain N verb calls — only the final return crosses the wire
    r = await call_tool("capability_<cap>_<verb>", {
        "intent_id": iid, "agent_id": "agent:me",
    })
    # 3. record the lesson so the graph carries it (provenance moat)
    await call_tool("capability_reflect_note", {
        "intent_id": iid, "agent_id": "agent:me",
        "scope": "observation", "text": "<lesson>",
    })
    return r
'''})
```

### Session mode — walk discipline skills, don't improvise

Every walkable skill IS a Lifecycle template (Spec 114). Walk them via
`develop.skill_walk` so the engine bounds context one phase at a time:

- `develop.brainstorm` — explore intent before code
- `develop.write_spec` — harden a draft into a spec
- `develop.implement` — RED → GREEN → commit → push (TDD walker)
- `develop.skill_walk` — walk any cap's walkable skill
- `develop.session_init` — open + resume a session

### Provenance is the moat — verb-first beats raw tools

Capability verbs auto-record Invocations + SERVES edges + Artefacts.
Raw `Bash`/`Edit` actions don't. Prefer:

| action | verb | raw fallback |
|---|---|---|
| run tests | `develop.test` | Bash `pytest` |
| commit | `branch.commit_smart` | Bash `git commit` |
| push + open PR | `branch.finish_branch` | Bash + `gh` |
| dispatch subagent | `subagent.dispatch` | Agent tool |
| search code | `search` + `analyze.*` | Grep / Glob |
| critical thinking | `intent.<method>` (8 methods, Spec 091) | chat |

When in doubt, call `agency_welcome` first — sub-1KB, pure introspection,
state-aware (fresh-graph → bootstrap; populated → discovery + provenance).
<!-- agency:onboarding:end -->
