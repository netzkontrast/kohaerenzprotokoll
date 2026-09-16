# Plan/wiki — the knowledge system (research wiki, process, safety skills)

Started 2026-09-15 after the Drive source index landed (680 non-canon
documents). Engineering language is English; canon prose stays German.

- [knowledge-system-concept_2026-09-15.md](knowledge-system-concept_2026-09-15.md) —
  **the concept**: three layers (`Sources/` → `Wiki/` → `Canon/`), the
  ingest → understand → question → decide → lock → verify loop, the skills and
  hooks that keep it safe, the DSPy programs behind it, and the phased setup plan.
- [repo-survey_2026-09-15.md](repo-survey_2026-09-15.md) — what we took from the
  nine surveyed repositories and what we deliberately left out.
- [surveys/](surveys/) — the eight full per-repo survey reports (haiku agents,
  read-only) the synthesis is built on.
- [integration-plan_2026-09-15.md](integration-plan_2026-09-15.md) — **the
  integration plan**: per repo and per concept, which pack skill teaches the
  LLM part, which file here carries the deterministic part, and the phase; the
  three pack skills still to add (v0.6.0) and the Phase-1 PR; adds D-W10, D-W11.
- [../../docs/dspy-base.md](../../docs/dspy-base.md) — the DSPy substrate all
  wiki programs run on (`tools/kpwiki/`).
