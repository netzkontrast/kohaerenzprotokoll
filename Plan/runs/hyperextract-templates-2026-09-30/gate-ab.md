# The cue gate against the ungated run — `CausalLinks`, three German documents

U1 is the first ungated run of the scaled pass, U2 a second ungated run, G a gated run (`he_claude.py run --gate`). A cell is a count of lines on which a run admitted a row. *Recall* is the share of U1's lines a run also finds; *of its own*, the share of a run's lines that U1 also has. U2 is what a repeat does to itself; G is the gate.

| document | run | rows | lines | recall of U1's lines | of its own lines in U1 | gold lines (of those in U1) | calls | cost | share of the text sent |
|---|---|---|---|---|---|---|---|---|---|
| `kohaerenz-protokoll-philosophie-im-detail-2026-0` | U1 | 89 | 74 | — | — | 12 (12) | 29 | $0.36 |  |
| `kohaerenz-protokoll-philosophie-im-detail-2026-0` | U2 | 85 | 73 | 91% (67) | 92% | 11 (10) | 29 | $0.36 |  |
| `kohaerenz-protokoll-philosophie-im-detail-2026-0` | G | 23 | 22 | 24% (18) | 82% | 3 (3) | 8 | $0.10 | 24% |
| `kohaerenz-protokoll-philosophischer-bericht-md` | U1 | 102 | 69 | — | — | 17 (17) | 34 | $0.42 |  |
| `kohaerenz-protokoll-philosophischer-bericht-md` | U2 | 100 | 68 | 91% (63) | 93% | 18 (15) | 34 | $0.41 |  |
| `kohaerenz-protokoll-philosophischer-bericht-md` | G | 24 | 16 | 23% (16) | 100% | 6 (6) | 9 | $0.11 | 25% |
| `worldbuilding-konzept-kohaerenzprotokoll-md` | U1 | 76 | 59 | — | — | 18 (18) | 28 | $0.34 |  |
| `worldbuilding-konzept-kohaerenzprotokoll-md` | U2 | 76 | 56 | 81% (48) | 86% | 19 (15) | 28 | $0.34 |  |
| `worldbuilding-konzept-kohaerenzprotokoll-md` | G | 31 | 21 | 32% (19) | 90% | 7 (7) | 9 | $0.11 | 31% |

## Pooled over the three documents

| run | rows | lines | recall of U1's lines | of its own lines in U1 | gold lines | calls | cost |
|---|---|---|---|---|---|---|---|
| U1 | 267 | 202 | — | — | 47 | 91 | $1.11 |
| U2 | 261 | 197 | 88% | 90% | 48 | 91 | $1.11 |
| G | 78 | 59 | 26% | 90% | 16 | 26 | $0.32 |

The gate sent 42,089 of 159,627 characters (26%). Gold lines found by U1 and U2 together: 55; by U1 and G together: 47; U1 alone: 47.
