---
description: >-
  Print a read-only freshness/health snapshot of the Codex layer: whether
  generated Codex/ views match the graph, chapter-lint status, and pending
  claim verifications. Simplified companion to /full-audit-canon — a status
  check, not a full audit cycle. Usage: /codex-status
argument-hint: ""
---

# Codex Status — Snapshot

Read-only. Writes nothing, fixes nothing, triages nothing. Use this at
session start or before drafting to see whether the Codex layer is current,
without paying for a full `/full-audit-canon` pass.

## Step 1: Are the generated views fresh?

```bash
python3 scripts/render_codex_views.py --check
```

`Codex/GLOSSARY.md`, `Codex/MASTER-TIMELINE.md`, `Codex/WORLD-AXIOMS.md` are
rendered from the graph — never hand-edited. Stale means a graph write
happened since the last render.

## Step 2: Chapter lint status (deterministic, free)

```bash
for f in Manuscript/works/the-agency-system/works/hard-scifi-cosmic-horror-psychological-thriller/kohärenz-protokoll/chapters/*.md; do
  python3 scripts/lint_chapter.py "$f" >/tmp/lint-out.txt 2>&1
  rc=$?
  [ $rc -ne 0 ] && echo "VIOLATION: $f" && cat /tmp/lint-out.txt
done
echo "lint sweep complete"
```

Report the count of chapters with VIOLATION vs. clean. Do not run the
lit-critic gate here — that needs an API key and is a heavier LLM pass
(`scripts/lit_critic_gate.py`, skill `lit-critic`).

## Step 3: Graph snapshot (agency verbs, read-only)

Inside one `execute` block:

```python
r1 = await call_tool("capability_novel_novel_progress", {"novel_id": "novel:9d170c31"})
r2 = await call_tool("capability_novel_pending_verifications", {})
r3 = await call_tool("capability_novel_chapter_report", {"novel_id": "novel:9d170c31"})
return {"progress": r1, "pending_claims": r2, "chapters": r3}
```

Report: word count, chapters by status (`outlined`/`drafted`/`revised`/`final`),
pending claim count by domain.

## Step 4: Enrichment discipline (only if a base revision is known)

If the caller names a base revision to diff against:

```bash
python3 scripts/check_enrichment.py --base <rev>
```

Otherwise skip this step and say why (no base given).

## Output format

One compact report:

1. **Freshness** — `render_codex_views --check` result
2. **Lint** — clean/violation counts from Step 2
3. **Graph** — progress + pending-claims + chapter-status table from Step 3
4. **Next action** — the single most useful next step (e.g. "views stale →
   re-render", "3 chapters VIOLATION → fix before /full-audit-canon",
   "12 pending claims in `scientific` → run /full-audit-canon physics")

Do not re-render, fix lint violations, or resolve claims from this command
— it only reports. For those, use `/ingest`, `/full-audit-canon`, or the
relevant skill directly.
