---
document: roman-lokalitaeten-konzept-und-ausarbeitung
against: 46 pages, 4 conflicts
ran: "2026-09-17"
candidates: 109
decisions: 123
by_lookup: 68
judgements: 55
new_pages: 10
new_readings: 17
---

# Reconciliation 7 — `roman-lokalitaeten-konzept-und-ausarbeitung` against the wiki

`python3 scripts/reconcile.py roman-lokalitaeten-konzept-und-ausarbeitung`

109 candidates, 123 decisions — **68 by lookup, 55 to judgement.** The decision
count exceeds the candidate count because one term can raise several judgements.

**This is the largest reconciliation so far by every measure**, and the reason is
that the document is a gazetteer: 51 of its 109 candidates are place names, each
asserted in a table row and most of them nowhere else.

## The rule that decided the locations, and why it is a rule rather than a taste

49 candidates matched no page. Creating 49 pages would nearly double the wiki
from one document; creating none would repeat document 5's outcome for a
document that is not a brief.

**The document supplies two mechanical criteria and they were used:**

| criterion | what it is | how it is read |
|---|---|---|
| does the document profile it? | Teil IV holds 17 profiles of eleven fields each | a count of exactly **2** — once in the master table, once as a profile heading |
| did the document invent the name? | the master list carries a `Source` column per row | `Explorative V2` = invented here; `Plot Teil 1`, `Konzept Doc`, `Kontext` = inherited |

A location got a page when **both** held: profiled, and inherited. That set is
11. Two were withheld by judgement and one concept page was added, so **ten pages
were created.**

| withheld | why |
|---|---|
| `Garten der Möglichkeiten` | the wiki already holds `moeglichkeits-garten` from document 4 at a different scale — reading added there, conflict `C5` raised (J35) |
| `Nexus-Interface` | unresolved against `nexus`; creating a page asserts they are two terms, which is the open question (J36) |

| added | why |
|---|---|
| `realitaetsebenen` | not a location. The six-level frame the wiki has been building members of — `kern-welten`, `ueberwelt` and `externe-ebene` are three of the six (J42) |

**The 40 that did not become pages are recorded in `reconcile.json` with their
lines**, split into the 30 the document says it invented and the 10 it inherited
but never profiled. A later document that describes one opens its page with a
reading already attached.

## Pages created

`realitaetsebenen` · `kaels-wohneinheit` · `datenverarbeitungsknoten-7g` ·
`therapie-schnittstelle-alpha` · `vergessener-schrein` · `archiv-des-ungesagten` ·
`schleuse-7` · `grosse-mauer` · `system-monitor` · `junas-ankerpunkt`

## Readings added

Seventeen, and four of them change something the wiki had recorded as open.

| page | what this document adds |
|---|---|
| `kern-welten` | **all four numbered, with a domain bearer each.** The page's own inference — KW1 is `konstrukt-stadt`, KW3 is `grenzfeste` — is now complete for all four and confirmed for the two it could be checked on |
| `guardians` | **`Wächter` twelve times analytically and `Guardian` not once.** The four bearers named in one parenthesis |
| `risse` | **the first mechanism anything read has given.** „eine Form der Umgebungsreaktion auf Systemstress oder steigende Entropie" ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L77] — the environment misfiring, not something arriving |
| `alters` | four named, one per level, each with „wie" — **this page's first reading ever** |
| `ueberwelt` | Interface or Betriebssystem rather than a place; `Simulation` used in the same file for something larger |
| `externe-ebene` | labelled `Verbindung: Juna` where the other five levels read `Domäne` |
| `entropie` | instrumented — Entropiegrad, Entropielevel, Entropie-Hotspots, Entropie-Indikatoren, Ausgleichs-Kammer |
| `aegis` | „Ordnung, Integrität, Effizienz" ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L49], and „Allwissenheit (oder den Anspruch darauf)" ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L467] |
| `kael` · `juna` | the Kern-Welten are his; she is the sixth level's connection and the monitor may not be able to localise her |
| `logos` · `mnemosyne` · `cerberus` · `kairos` · `sophia` | a numbered world and a stated domain each |
| `moeglichkeits-garten` | a region inside KW4 with gates to other regions of KW4 — `C5` |
| `nexus` | a third carrier of the name, inside a Kern-Welt rather than above them |

`did`, `kohaerenz`, `blinder-fleck`, `personas`, `partnerin`, `konstrukt-stadt`,
`resonanz-landschaft`, `grenzfeste`, `potentialmeer`, `ueberraum` matched by
lookup or by subject and **have no reading added**. For `kohaerenz` the reason is
the count: 22 occurrences, most of them the novel's own title. For the four
world-name pages and the two meta-space pages the reason is stronger —
**this document contains zero occurrences of any of them.**

## What changed that the wiki had written down as a test

Three records named, in advance, the evidence that would move them. All three got
it, and none of them closed.

| record | the test it wrote | what arrived |
|---|---|---|
| `kern-welten` | *`KW2` and `KW4` appearing anywhere would settle most of it at once* | both, 28 and 18 times, with bearers |
| `c4-guardians-and-aegis` | the same sentence, for the same reason | the same evidence — and document 4 still never mentions AEGIS |
| `q4-waechter-four-bearers` | *Any document using `Wächter` in an analytic sentence would break the register pattern* | twelve analytic uses, and zero `Guardian` |

**Q4's is the one worth dwelling on, because the thing it broke was a
measurement.** The register hypothesis — English is the analytic word, German the
fictional one — was derived from a real distribution in document 5 and it was
wrong. The distribution tracks the document, not the register: one document is an
English-leaning subplot brief and the other a German worldbuilding catalogue, and
each uses one word throughout.

`Q3` splits instead of narrowing: the Kern-Welt count is answered from outside —
four, inside six Realitätsebenen, stated five times without qualification — while
the alter count and the correspondence are untouched, because every level
introduces its Alter with „wie".

## One conflict raised

`C5` — a Kern-Welt in document 4 is a region inside that Kern-Welt here, with
„Tore zu anderen Bereichen von KW4" ^[roman-lokalitaeten-konzept-und-ausarbeitung.md:L436]. **It is the wiki's first conflict about
scale rather than about content**, and everything except the scale agrees.

## Judgements

Thirteen, `J33`–`J45`. Three worth naming:

- **`J33` — `Wächter` was not added as a surface**, although this document would
  justify it twelve times over. The word has five bearers across the corpus and
  one of them is already an alias on `aegis`; adding it would route every
  analytic use here onto the wrong page by lookup.
- **`J39` — `Simulation` and `Überwelt` are two terms**, from the first document
  that uses both. `J30` left this unresolved on document 5, which never wrote
  `Überwelt`. The index still maps the surface `Simulation` to `ueberwelt`, and
  that mapping is now doubtful; it was recorded, not changed.
- **`J38` — `Limina` and `Liminale Räume`.** A candidate that shares a stem with
  an external concept the document cites to its own reference list. The Alter and
  the craft theory are not the same kind of thing, and a plain count merges them.

## A side effect worth more than most of the above

**A bare `^[Lnn]` on a wiki page stops being checked the moment the page gains a
second `ingested:` entry.** `quotes.py` resolves a bare reference against the
single ingested slug and refuses to guess when there are several — correctly.

Adding this document's reading to seventeen pages therefore moved **95
previously-checked quotations into the unchecked bucket, silently**, and the run
that noticed was the one that happened to compare the totals before and after.

Every reference on every page touched here is now in the full
`slug.md:Lnn` form, including on the ten new pages, which have one source each
and did not need it yet. Checked quotations went from 348 to 572 across the
repository; unresolved stayed at the known 17.

**The rule this produces: a bare reference is only safe on a file that can never
gain a second source** — a census or a note, which carry `source:`. On a wiki
page, write the slug.
