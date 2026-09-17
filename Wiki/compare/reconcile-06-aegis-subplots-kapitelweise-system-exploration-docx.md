---
document: aegis-subplots-kapitelweise-system-exploration-docx
against: 46 pages, 4 conflicts
ran: "2026-09-17"
candidates: 51
decisions: 65
by_lookup: 35
judgements: 30
new_pages: 0
new_readings: 3
---

# Reconciliation 6 — `aegis-subplots-kapitelweise-system-exploration-docx` against the wiki

`python3 scripts/reconcile.py aegis-subplots-kapitelweise-system-exploration-docx`

51 candidates, 65 decisions — **35 by lookup, 30 to judgement.** The decision
count exceeds the candidate count because one term can raise several judgements.

## The unusual outcome: no new pages

Fifteen candidates matched an existing page and sixteen matched nothing. **None
of the sixteen became a page**, and that is a decision rather than an omission.

A term page collects every source's *reading* of a term. This document is a
brief — it hedges once every 86 words, and 32 of its 91 question marks sit in
the field closest to assertion. For `Integration`, `Synthese`,
`Datenkorruption`, `Systemstabilität`, `Systemmonitor`, `Bedrohungsstufe`,
`Kerncode`, `Quellcode`, `Realitätsverformung`, `Architekten`,
`Kernsystemprotokoll`, `KW1`, `KW3` and `TSDP` it supplies **occurrences, not
readings** — the word is used, in a proposal, about something the document is
asking rather than telling.

**A page created from an occurrence is a page that says nothing and looks like it
says something.** These are recorded here with their lines so the next document
that actually defines one can open its page with a reading already attached.

Three exceptions were folded into existing pages instead:

| candidate | went to | why |
|---|---|---|
| `KW1`, `KW3`, `Kernwelt 1` | `kern-welten` | J26 — a numbered instance is a reading on its class |
| `Architekten` | `guardians` | a fourth kind, named in one clause, with `Vollstrecker` and `Monitore` |
| `Rest-AEGIS` | recorded, not written | J29 — a later state of the same bearer |

`Teil 1`, `Teil 2` and `Teil 3` were rejected outright as document structure
(J31), along with the three part titles the count missed because the document
writes them in capitals.

## Readings added

| page | what this document adds |
|---|---|
| `guardians` | the structural placement inside AEGIS, chapter 20's refusal to settle it, the Architekten/Vollstrecker/Monitore taxonomy |
| `kern-welten` | the numbering — KW1 is Logik and LogOS, KW3 is Cerberus — and the inference joining it to document 4's named worlds |
| `c4`, `q1` | the correction: the passage that chose this document is a question |

`aegis`, `entropie`, `kael`, `juna`, `logos`, `cerberus`, `mnemosyne`,
`risse`, `alters`, `kohaerenz`, `externe-ebene` all matched by lookup and
**have no reading added**, for the same reason as the unwritten pages: this
document mentions them without saying anything about them that is not hedged into
a question. That is recorded rather than silently skipped.

## Judgements

Thirteen recorded, `J20`–`J32`. Three are worth naming here:

- **`J20` — `Wächter` has four bearers**, and one of them is an alias already on
  `aegis`. Raised as `Wiki/questions/q4-waechter-four-bearers.md`.
- **`J28` — four compounds of `Entropie` landed in four different places.**
  `Entropiegewinn` is a reading on `entropie`; `Entropiepotenzial` belongs with
  `aegis-metriken`; `Entropiemanagement` is a term with no page;
  `Informationsentropie` is imported theory and not canon at all. The rule is
  that a compound is placed by what it names, never by its head.
- **`J30` — unresolved and recorded as unresolved.** The wiki maps `Simulation`
  to `ueberwelt`; this document uses `Simulation` 17 times and never writes
  `Überwelt`. Whether they are the same cannot be settled from here. It is the
  first judgement in the ledger carrying `rule: null`.

## What the baseline did

The ledger is also the trainset, and adding these thirteen moved it from 17 to
**26 labelled examples, 13 one-term against 13 two-terms.**

**`fold()` fell from 14/17 = 82% to 17/26 = 65%**, and the drop is not noise:
every new miss is a plural or an inflection — `Guardian`/`Guardians`,
`Riss`/`Risse`, `Alter`/`Alters`, `AEGIS`/`Rest-AEGIS`,
`Entropie-Score`/`globaler Entropie-Score`. `fold()` strips the German definite
article and does nothing else, and the first seventeen judgements happened to be
article-heavy.

**So the honest baseline is 65%, the earlier 82% was a property of the sample,
and the misses are systematic rather than random** — which means the next
improvement is a rule, not a model.
