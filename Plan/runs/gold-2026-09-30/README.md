# More gold — candidate lists only, 2026-09-30

The author, 2026-09-30: „Extract more Gold for learnings“.

Gold is a candidate list `scripts/gold.py` accepts: written while reading, counted, frozen since
the count, of its document (decision 009). It is the baseline every automated reader is scored
against. So this run does steps 1–3 of `ingest` and stops: profile, the list written while
reading, the count. **No census, no note, no reconciliation, no page.** A list alone is not a
census, so `account.py order` is untouched, and step 6's pause on full readings stands.

## Which documents

One unread document, the newest by `index_date`, from each of the six categories with the fewest gold
lists against their size:

| category | gold before | document | lines |
|---|---|---|---|
| theorie-physik | 2 / 37 | `deconstructing-reality-s-architecture` | 333 |
| theorie-psychologie | 3 / 43 | `angst-und-vermeidung-in-dis-systemen` | 266 |
| aegis | 3 / 38 | `aegis-manifest-genesis-krise-reboot-2` | 303 |
| theorie-mathematik | 2 / 19 | `dual-kernel-erzaehlarchitektur-bewusstsein-symmetrie-ourobor` | 314 |
| theorie-logik | 3 / 24 | `wahrheitstheorien-kohaerenz-vs-korrespondenz` | 436 |
| audit | 2 / 15 | `konsolidierung-des-hard-canon-protokolls` | 52 |

Each is read by one Sonnet subagent that sees the briefing and its document and nothing else.
The task is `task.md`.
