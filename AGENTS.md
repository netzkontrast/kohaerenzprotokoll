# Repository agents

Read `CLAUDE.md`, `PRINCIPLES.md` and `NOW.md` before substantive work.

At the start of a coordinating session, before corpus reading, research or
delegation, run `python3 scripts/knowledge.py init --profile reader` from the
repository root. Use `--profile research` when DSPy/research capabilities are
needed. This is the Codex startup instruction; Claude additionally has an
executable SessionStart hook. Do not assume the host executes a Codex shell hook.

Delegated agents use `python3 scripts/knowledge.py init --profile reader --check`
(or their research profile), report missing capabilities, and do not rebuild,
restore or export shared stores. Follow `.agents/skills/reader-tools/SKILL.md`.

The initializer keeps a fresh graph, restores a matching `Graph/` snapshot, or
rebuilds from authoritative files. Export is explicit; never edit graph snapshots
or generated Markdown by hand. Source lines are retrieved and cited only when
needed for the assigned claim. Independent source readers do not load graph or
wiki context before their extraction is frozen.
