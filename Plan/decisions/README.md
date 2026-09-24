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

A decision the author still has to make is not here: it is a question under
`NOW.md`, *Questions for the author*, until it is answered.
