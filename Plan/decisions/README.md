# `Plan/decisions/` — one file per decision, kept for good

One short file per decision, permanently — what was chosen, what was rejected,
what would change our mind (`CLAUDE.md`, *Tracking work*, which also says where
decisions sit beside `NOW.md` and git).

**This page is checked, not remembered.** 0 <!--state:readme.decisions_drift-->
decision files are missing from it or listed here without existing, and
`python3 scripts/state.py --prose` fails the day that number is not 0.

| file | date | decided |
|---|---|---|
| `001-reset-to-two-layers.md` | 2026-09-16 | Reset to two layers, `Sources/` and `Wiki/`, wiki first |
| `002-normalize-sources-on-write.md` | 2026-09-16 | Normalize source documents on write, mechanically only |
| `003-conflicts-get-their-own-record.md` | 2026-09-16 | A conflict is recorded once, by subject, and term pages point at it |
| `004-no-fixed-document-kinds.md` | 2026-09-16 | Format is measured, stance is read per passage, and neither is a document kind |
| `005-the-wiki-links.md` | 2026-09-17 | A link is `[[slug]]`; a term in backticks is not a link |
| `006-every-draft-is-back-in-question.md` | 2026-09-24 | Every draft is back in question; `Sources/` is the starting point |
| `007-tool-test-consent.md` | 2026-09-24 | Two documents may go to free models and Jev, to test the new tools |
| `008-open-questions-answered-by-delegation.md` | 2026-09-24 | The tool review's open questions, answered by the session on the author's delegation |
| `009-gold-lists-by-rule.md` | 2026-09-24 | Which candidate lists are gold is decided by rule, in `scripts/gold.py` |
| `010-the-plural-rule-by-delegation.md` | 2026-09-24 | A plural ending is not a term boundary, within a stated reach — a scored rule in `pairs.py`, not in `fold()` |
| `011-dspy-runs-on-claude-and-free-models.md` | 2026-09-25 | DSPy runs may use Claude through `claude -p` (first party), and OpenRouter's free models through `route.py`, pinned — never with a line of a document |
| `012-reading-questions-answered-by-delegation.md` | 2026-09-25 | No human anchor; a census is selective by a written rule and reconciliation sweeps the text for every term the wiki knows; a record holds one entry per document with a position |
| `013-the-chapter-is-a-unit.md` | 2026-09-25 | The chapter is a unit of the wiki beside the term: a page per chapter, overview pages that place, `scripts/chapters.py` |
| `014-jules-may-ingest-a-document.md` | 2026-09-27 | A Jules session may ingest one document by the `ingest` skill, `Wiki/` in scope, the plan read before it is approved |
| `015-the-pipeline-plan-accepted.md` | 2026-09-29 | The pipeline plan of 2026-09-29 accepted in full: history out of CLAUDE.md and NOW.md, readers write files that code renders, qmd answers off the chapter pages, `ingested:` is every cited read document, a sampled resumption, a leaner install |
| `016-decision-sheets-worked-in-rounds.md` | 2026-09-30 | Decision sheets are cross-read first and put to the author in rounds: `PROVISIONAL` with `ALT` when unanswered, one decision file per round, a front-matter head on each sheet, a script only after round 1 |
| `017-ask-answers-are-sources.md` | 2026-09-30 | `ask` answers are logged and treated like sources (`Sources/ask/`, tier `M-ask`); OpenRouter free models and Jules may answer, as trials first |
| `018-remaining-questions-by-delegation.md` | 2026-09-30 | The open process questions answered by the session on the author's delegation: W12/W15 sheets via `ask` first, W7 cuts the cycle, claude-cli/Sonnet default, GraphQLite only for `ask` and the sheets until a parity bench |
| `019-the-hyperextract-backfill-stopped.md` | 2026-09-30 | The HyperExtract backfill is stopped after 14 of 137 runs: five more gold-heavy documents read moved `he-lines` by nothing (+0.029 before and after), coverage is not what limits the finder — a committed `STOP` keeps it stopped |
| `020-hyperextract-ported.md` | 2026-10-01 | HyperExtract's engine ported to `scripts/hx.py`, standard library, byte for byte what upstream sends; upstream installed on demand to check it; its MCP server unregistered |
| `021-the-architecture-spec-adopted.md` | 2026-10-01 | `SPEC.md` adopted, its migration order binding; E4 may run on Claude for $20 after steps 2 and 4; `GOAL.md` annotated, not rewritten |

A decision the author still has to make is not here: it is a question under
`NOW.md`, *Questions for the author*, until it is answered.
