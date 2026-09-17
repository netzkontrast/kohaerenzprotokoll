---
document: kohaerenz-protokoll-konzept
against: 56 pages, 5 conflicts
ran: "2026-09-17"
candidates: 150
decisions: 153
by_lookup: 123
judgements: 30
new_pages: 2
new_readings: 20
---

# Reconciliation 8 — `kohaerenz-protokoll-konzept` against the wiki

`python3 scripts/reconcile.py kohaerenz-protokoll-konzept`

150 candidates (151 written while reading, 1 surface group folded to one term
first), 153 decisions — **123 by lookup, 30 to judgement.** The first
`kernkonzept` document read, and the second-largest census by word count so
far (10,653 words, 151 candidates) after document 6's gazetteer.

## Why two new pages, not fourteen

The category-reset pattern held for `aegis` (14), `guardians-und-kern-welten-konzept`
(14) and `entropie-aegis` (14) on the first document of a category. This
document breaks it downward, to **2**, and the reason is not that it is thin —
it is the second-richest census read — but that **it meets a wiki that already
built out almost everything it talks about.**

This document uses `Michael`/`Julia` and never `AEGIS` (0 occurrences,
checked directly), which is the pre-rename, pre-AEGIS voice five earlier
documents (`entropie-aegis`, `kohaerenzprotokoll-aegis-und-systementropie`,
`guardians-und-kern-welten-konzept`, `aegis-subplots-kapitelweise-system-exploration-docx`,
`roman-lokalitaeten-konzept-und-ausarbeitung`) already gave pages to under
different names — `kael`, `juna`, `guardians`, `did`, `alters`, `kohaerenz`,
`risse`, `ueberwelt`, `externe-ebene`, `personas`, `partnerin`,
`multiplizitaet`, `logos`, `mnemosyne`, `cerberus`, `kairos`, `sophia`,
`realitaetsebenen`, `kern-welten`, `kael-julia-bindung`. Twenty readings landed
on those twenty pages. Only two things this document says had no existing
home: the Guardians' own named paradigm, and the four tools they offer.

**So the curve is a page-count curve, and this document is the one that shows
its limit.** A document can be dense and still add few pages, when what it is
dense *about* is already in the wiki.

## The two new pages

`seele-info` collects the Guardians' paradigm — quoted 13 times, never adopted
by the document itself — and the diagnostic vocabulary it generates
(`Systemfehler`, `Datenkorruption`, `Datenintegration`, `Datenkohärenz` and
nine more), which is one reading's supporting detail rather than nine separate
occurrences.

`guardian-werkzeuge` collects four named tools, each named twice with
different phrasing and neither naming cross-referencing the other — the exact
merge point flagged in `03-candidates.md` while reading, resolved by J51.
Precedent: `aegis-teilfunktionen` already groups a set of four named
sub-functions as one page rather than four.

## What the document itself flagged, and how each was handled

Four things were named in the brief for this run, and none was resolved here —
an ingest proposes, it never resolves:

- **The four Guardian tools, named twice** — folded (J51), page created
  (`guardian-werkzeuge`).
- **Welt 1 given two labels** (`Zerbrochene Stadt` and `Trauma-Loop`, the
  latter nowhere else) — recorded on the new `kern-welten` reading as the
  document's own unflagged inconsistency, not resolved either way.
- **`Blueprint V5` named as predecessor** — recorded as document-provenance
  inside the `personas` and `partnerin` readings it appears in; not promoted
  to its own page, since it names the corpus rather than the fiction.
- **The externe Ebene's nature left undecided, three hypotheses** — recorded
  as a reading on `externe-ebene`, `juna` and `kael-julia-bindung`, none
  chosen, matching the document's own Section X framing as the project's
  first open question rather than a finding.

## What a page may not be built from, applied here

**No page was created from an occurrence.** The Alter-Archetypen table names
seven alters with real content — a role, a world, a conflict each — which
looked, at first, like the same shape that earned `LogOS`/`Mnemosyne`/
`Cerberus`/`Kairos`/`Sophia` five pages from one document's table. **The
difference is the document's own hedge.** That earlier table is asserted
outright; this one is introduced as „mögliche Schlüssel-Alters […]
Beispiele" (L110) and Section X calls it „skizzierte […] Alter-Archetypen"
needing further work (L397). None of the seven names recurs outside that one
table. Recorded as one reading on `alters` — a third, non-one-to-one roster,
feeding `Q3` — rather than as up to seven pages built from one document's own
stated sketch. The 26 candidates this affects are in `reconcile.json`'s
`not_promoted`, with lines.

The same restraint applied to the borrowed monomyth vocabulary (`Ordinary
World` through `Freedom to Live`, `Heldenreise`/`Heldinnenreise`,
`Campbell`/`Murdock`) and to the document's own repeated section-template
labels (`Narrativer Rahmen`, `Psychologischer Rahmen`, `Inhaltlicher Fokus`,
`Pacing`) — structural devices and citations, not readings of a term this
novel defines, the same reasoning the census already applied to the 41
chapter-scene labels it chose not to list.

## Readings added

Twenty pages, one document. Four are worth naming specifically:

| page | what this document adds |
|---|---|
| `partnerin` | **Answers a question the page has carried as open since document 4** — „No read source links Partnerin to Julia, Juna or any name." This document states directly that Partnerin (V5) is replaced by Julia. Recorded as this document's own claim, not as the wiki's finding. |
| `kern-welten` | A fourth world-count confirmation and a **third independent naming layer with zero vocabulary overlap** with document 4's — `Die Zerbrochene Stadt` etc. share no name with `Konstrukt-Stadt` etc., the same "vocabularies do not touch" shape already recorded between documents 4 and 6. |
| `guardians` | Four Guardians (Kairos/Sophia combined, matching the corpus's own prior resolution), and — new — **four named tools**, which no other read document gives them. |
| `alters` | A third roster that **breaks the one-alter-per-world shape** document 6's roster was compatible with — two alters share Welt 1, two share Welt 4. |

Sixteen more readings, each a short, independent confirmation or extension:
`kael`, `juna`, `did`, `logos`, `mnemosyne`, `cerberus`, `kairos`, `sophia`,
`externe-ebene`, `kohaerenz`, `personas`, `ueberwelt`, `multiplizitaet`,
`risse`, `kael-julia-bindung`, `realitaetsebenen`. Full detail, with every
citation, is on each page and in `reconcile.json`.

**Not a conflict, checked explicitly on four pages.** `kohaerenz` now holds
two readings pointed in opposite directions — this document's „authentische
Form von Kohärenz, die über reine Datenintegration hinausgeht" against the
existing „niedrige Entropie, hohe Vorhersagbarkeit" — and neither document
shares a referent (this one never mentions AEGIS) to disagree about. Recorded
unmerged, per the wiki's own rule for attributed readings.

## Judgements

23, `J46`–`J68`, covering all 30 near-matches the pre-classification raised
(some judgements settle more than one near-match at once — J49/J50/J51 all
turn on the same Kohärenz-Analysator tool-naming, and J62 settles all three
Kairos/Sophia lines at once). Three worth naming:

- **`J51` mechanises the census's own flagged merge point** — the four
  Guardian tools, named as a noun phrase once and a compact compound once,
  with the document's own words (`statten ihn mit ungeeigneten Werkzeugen
  aus`, L275) doing the identification rather than any string match.
- **`J58`/`J59`/`J68` are the same finding three times over**: `Kern` is
  polysemous *within this one document* — `Kernpersönlichkeit`, `Kerntrauma`,
  `Kernkonzept`/`Kernthema`, and a fold()-false-positive toward the corpus's
  `Kern-Welten` — and the census had already separated three of the four
  senses before reconciliation began. Bare `Kern` is not itself promoted.
- **`J53` untangles a real substring trap inside one document**:
  `Systemwächter`/`Systemhütern` (the Guardians, collectively, in German) and
  the Alter named `„Wächter"` (a Protector-type character in the archetype
  table) share a root and nothing else. First folded to `guardians` as an
  alias; second recorded only inside the `alters` table reading.

`judgements.py` replays 68 judgements corpus-wide: 7 agree, 0 disagree, 61
still a person's call. (Two of this run's own judgements, `J55` and `J60`,
were first drafted claiming `wiki_index.fold` already merges a German
plural — checked directly against `fold()` and found false: `fold('Alters')`
and `fold('Alter')` normalise to different keys. Corrected before commit,
`mechanised_by: null`, the same shape as the `fold()` docstring defect the
skill's own history already names — a claim about the code that the code
did not support, caught by running it rather than trusting the description.)

## `Q3` updated, not settled

A fourth world-count confirmation (four, inside six) and a third alter roster
that is **not compatible with a one-to-one rule at all** — this document puts
two named alters in Welt 1 and two in Welt 4. Three documents, three rosters,
zero shared names. The possibility space widened; nothing closed.

## Citation hygiene

Every citation added by this run uses the full `kohaerenz-protokoll-konzept.md:Lnn`
form, on every page touched, including the sixteen that already carried other
documents. `python3 scripts/quotes.py` before this run reported 17 unresolved
(all pre-existing, none touching this document); after this run, still 17,
the same 17. Two classes of self-inflicted defect were caught and fixed before
that count held:

- **An ASCII `"..."` scare-quote inside my own prose, shortly after an open
  „…" blockquote, let the checker's greedy quote-matcher run past the real
  closing mark into my own sentence and pair a citation with the wrong text**
  — the same class of defect `quotes.py`'s own docstring names as the reason
  it exists. Fixed by using backticks for my own scare-quotes near a
  blockquote, and by matching the source's own straight-quote style verbatim
  inside quoted German rather than substituting single quotes.
- **Two quotes were mis-cited by one line** (`Datenintegration hinausgeht` and
  an "Integrations"-Werkzeuge quote each landed a line away from their actual
  source line) and one quote silently dropped a clause the ellipsis should
  have marked. All three were caught by `quotes.py`, not by re-reading.

## What this run deliberately did not do

- Did not resolve whether `guardians-und-kern-welten-konzept` is itself an
  instance of the "Blueprint V5" this document names — both are dated
  2025-04-17, and V5 introduces the same `Architekt`/`Echo` names that
  document's table uses, but nothing read states the identity. Left as an
  open observation on `personas.md`, not asserted.
- Did not resolve the externe Ebene's nature, Julia's connection mechanism,
  or the Welt-1 double-label — each recorded as the document's own open
  question or unflagged inconsistency, per the skill's rule that an ingest
  proposes and never resolves.
- Did not create pages for the seven Alter-Archetypen, the borrowed
  Hero's-Journey stage names, or the document's own section-template labels —
  each recorded in `reconcile.json`'s `not_promoted`, with lines, so the
  document that actually commits to a roster or a location opens its page
  with these readings already attached.
