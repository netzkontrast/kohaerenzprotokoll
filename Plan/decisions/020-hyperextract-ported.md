# 020 — HyperExtract is ported into the pipeline; the upstream package only checks the port

**Date:** 2026-10-01 · **Decided by:** the author · **Status:** in use

## What was asked

The `hyper-extract` MCP server failed at session start (`he-mcp` was installed in `~/.local/bin`, which the PATH
Claude Code starts MCP servers with does not hold), and the fix was a link into `/usr/local/bin` (PR #134). The author:

> Oder besser noch - porte hyperextract vollständig in unsere Pipeline

## What was chosen

`scripts/hx.py` is the part of HyperExtract (`netzkontrast/Hyper-Extract` at `395039e`) a contract run uses, in the
standard library: the template loader (a YAML subset, refused outside it), the validator's checks (HE-T002…T008), the
prompt, the JSON schema, LangChain's text splitter, pydantic's lax check of a reply, and the merges (list append; set
and graph by their identifiers with `keep_existing`, `keep_incoming` or `merge_field`; dangling edges dropped).
`he_claude.py`, `reading_extract.py` and `templates.py` run on it, so a contract run, its self-tests and the template
checks need no uv tool, no LangChain, no pydantic and no install, and run on GitHub with the other standard-library
suites.

**What a model is sent did not change.** Measured against the installed upstream package (`hx.py parity`): all 32
templates parse to the same YAML, prompt and schema; all 586 landed documents cut into the same 17,480 chunks; the
merged result of three different canned replies over a four-chunk text is the same for every template with a fixture.
The message `he_claude` sends is the same text it sent through LangChain (no system message; the prompt, then
`JSON_ONLY` and the schema). So the 297 labelled rows, the yields and the cost per megabyte of
`Plan/concept/graph-contracts_2026-09-30.md` describe runs on the port as they described runs on upstream.
`Plan/hyperextract/fixtures/upstream-395039e.json` pins upstream's prompts, schemas and chunks of the four-chunk text,
and `hx.py selftest` holds the port to it without the package.

Upstream stays, demoted: `scripts/install.sh hyperextract` installs it on demand (no longer at session start) for
`hx.py parity`, for `templates.py parse` (`he parse` with a provider) and for the vendored `hyper*` template-design
skills. The `hyper-extract` MCP server is no longer registered in `.mcp.json`: it reads and exports Knowledge
Abstracts, which the pipeline does not write, and it failed every session it was not yet installed in;
`claude mcp add hyper-extract -- he-mcp` brings it back after an install.

## What was not ported, and why

- an `llm_*` merge — a model merging two readings into one (P13; `templates.py` already refused it);
- `two_stage` graph extraction — never run here, and it needs a second prompt fed with the first stage's names;
- the vector index, search, `ask`/`chat`, the exporters, the gallery and the CLI — nothing in the pipeline used them.
A template that asks for one is refused by name, never run differently.

## What would change it

An upstream change worth having (a pin moved past `395039e`): run `hx.py parity` against the new package first; where it
differs, the difference is ported or the pin stays. A template that needs YAML outside the subset: the loader is
extended, with `parity`'s YAML comparison as its check.
