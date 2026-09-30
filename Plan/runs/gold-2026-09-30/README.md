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

## What the six readers did

Sonnet subagents, three at a time, each reading only the briefing, `german.md` and its document.
All six lists are gold (`gold.py`). Each took 45–90 seconds and 8–17 tool calls. The first wave
read each document in one or two calls and wrote the list afterwards. So wave two was told to
read in chunks of at most 120 lines and to append after each one; it took twice the calls.

| document | terms | zeros in the count, and what each is |
|---|---|---|
| `deconstructing-reality-s-architecture` | 149 | none |
| `angst-und-vermeidung-in-dis-systemen` | 129 | `Täterintrojekt`: the text writes only the plural and compounds |
| `aegis-manifest-genesis-krise-reboot-2` | 175 | seven joined pairs `A (B)`, where the text puts italics or a footnote digit between the two names |
| `dual-kernel-erzaehlarchitektur-bewusstsein-symmetrie-ourobor` | 171 | `Gödel`: stands only inside compounds |
| `wahrheitstheorien-kohaerenz-vs-korrespondenz` | 168 | none; `F.H. Bradley` and `H.H. Joachim` are not candidates, because `capture.py` reads `. ` as a sentence |
| `konsolidierung-des-hard-canon-protokolls` | 67 | `Version: 2.0`: the text puts the colon inside the bold |

What the briefing did not anticipate:
- exports that blank subscripted symbols (`Kohärenz-Kernel ()`);
- `read.py --find` printing a digit-bearing heading without its digit (`KW:` for `KW1:`);
- an agent directive embedded in the audit document („SYSTEM OVERRIDE …“). Its reader recorded it as
  content and did not act on it.

## Scoring the extractors against gold — `goldeval.py`

The gold lists had been scored against twice: by the blind re-readings and by one entity list. The
HyperExtract backfill (PR #129, #130) has since run its contracts on 15 gold documents, and nothing
compared what they name with a gold list. `scripts/goldeval.py` compares every extractor with every
gold list by `agree.compare`. Its first run is in `Plan/runs/gold-eval/runs.jsonl`.

| extractor | docs | recall | precision | precision counting a label with a gold part |
|---|---|---|---|---|
| `he:termdefinitions` | 15 | 15.5 % | 61.2 % | 67.9 % |
| `he:termcontrasts` | 15 | 8.0 % | 11.9 % | 15.6 % |
| `he:causallinks` | 15 | 3.7 % | 14.5 % | 17.1 % |
| entity lists | 4 | 20.1 % | 61.1 % | 62.8 % |
| blind re-readings | 7 | 89.6 % | 32.6 % | 34.7 % |

- **Recall is low by design.** No contract is meant to enumerate terms.
- **Precision separates the contracts.** TermDefinitions names what a reader lists about as often as
  an entity list does. The relation contracts' endpoints are mostly phrases: of 1,070 TermContrasts
  surfaces on `kohaerenz-protokoll` that are not on its gold list, most are clauses („Aber es hatte
  ihm stattdessen einen Blick auf die Freiheit gewährt“).
- **A term list cannot score a relation.** It tells whether the names are right, not whether the
  pair is.

## Gold relations — `goldrel.py`, a pilot on three documents

On the author's „Maybe we need to extend the Gold List with additional Relation types like the ones
defined in the hyperextract contracts“. A reader writes `03-relations.md` while reading, blind to
every extractor (`relations-task.md`):
- definitions;
- contrasts, in TermContrasts' five types;
- causes, in CausalLinks' five types.

Code checks that each row's line holds its surfaces, and freezes the list. Three documents were read,
the three smallest with all three contract runs: `the-architecture-of-fracture-…` (50 rows),
`systemic-architecture-specification-…` (62) and `hard-sf-roman-outline-dkt-physik-cosmic-horror`
(160). Each reader took 40–130 seconds. The first run of `goldrel.py score` is in
`Plan/runs/gold-eval/relations.jsonl`:

| contract | gold rows | contract rows | recall | precision | +half | type agrees | line agrees |
|---|---|---|---|---|---|---|---|
| TermDefinitions | 140 | 149 | 52.1 % | 49.0 % | 49.0 % | 100 % | 82.2 % |
| TermContrasts | 56 | 105 | 50.0 % | 26.7 % | 38.1 % | 82.1 % | 100 % |
| CausalLinks | 76 | 69 | 32.9 % | 36.2 % | 52.2 % | 84.0 % | 96.0 % |

`+half` counts a contract row that stands on a gold row's line and meets one of its endpoints: the
same sentence cut at another length, such as `Coherence | causes | Landauer Heat` against
`Enforcement of internal consistency | causes | Landauer Heat`, both from L57.

**What it shows.**
- On a pair both sides found, the contracts mostly agree with the reader on the type (82–84 %) and
  the line.
- Where they differ, they differ in selection and in cut:
  - which lines count as defining one term;
  - how long an endpoint phrase is;
  - loose causal verbs („dictate“, „ensures“), which the readers themselves flagged.

**What it does not show yet: the ceiling.** A gold list of relations is one reading. Two blind
readers of terms agreed at F1 0.82–0.93 (P27). Nobody has measured how far two blind relation readers
agree. Until that is known, 50 % recall cannot be read as good or bad. The next step is a second
blind reader on these three documents (a `03-relations-blind-N.md`, which `goldrel.py` would need to
compare pairwise), and then more documents.

The readers also named three places where the vocabulary does not fit:
- „nicht X, sondern Y“ („is Y rather than X“), recorded as `denies` or `contrasts_with`;
- table rows as definitions;
- symbols that the export lost.
