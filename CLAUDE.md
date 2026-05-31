<!-- agency:onboarding:start -->
## Agency plugin — onboarding (auto-generated, do not edit between markers)

This repo carries an `.agency/` provenance graph (Spec 020). The
agency plugin's MCP server exposes three onboarding tools alongside
the code-mode contract:

- `agency_welcome` — one-shot first call; returns the bootstrap +
  install examples and the live capability list. **Start here.**
- `agency_install` — scaffold `.agency/` + this snippet in any target
  repo. Idempotent.
- `intent_bootstrap` — mint AND confirm an Intent. Every capability
  verb requires an `intent_id`; this is the only tool that doesn't
  (it mints the first one).
- `agency_doctor` — Spec 030 health check: report python version,
  deps, DB reachability, and env-var status (`JULES_API_KEY`
  presence — never the value). Call this when something silently
  fails.

Canonical first-call sequence (inside one `execute` block):

```python
# 1. Get onboarded (no intent_id required)
await call_tool('agency_welcome', {})
# 2. Scaffold .agency/ if missing (idempotent)
await call_tool('agency_install', {})
# 3. Mint the intent every capability verb SERVES against
r = await call_tool('intent_bootstrap', {
    'purpose': 'why', 'deliverable': 'what', 'acceptance': 'verify',
})
# 4. Use it
await call_tool('capability_plugin_help', {'intent_id': r['intent_id']})
```

State lives in `.agency/session.db` (committed to git per Spec 020 —
team learnings travel with the repo).
<!-- agency:onboarding:end -->
