---
document: charakterkonzepte-fuer-kohaerenz-protokoll
against: 58 pages, 5 conflicts
ran: "2026-09-17"
candidates: 108
decisions: 110
by_lookup: 96
judgements: 14
new_pages: 1
new_readings: 24
---

# Reconciliation 9 — `charakterkonzepte-fuer-kohaerenz-protokoll` against the wiki

`python3 scripts/reconcile.py charakterkonzepte-fuer-kohaerenz-protokoll`

108 candidates, 110 decisions — **96 by lookup, 14 to judgement.** First
document read from `charaktere`: 21 character profiles (10 Alters, 11
Nebencharaktere), each filled to a ten-field template, and every proposed
name carrying `oder ähnlich`. 191 hedging words in 15,436, 52 question marks.

## One new page, and it is a split, not a discovery

`zero-trust.md` splits off the existing `aegis-teilfunktionen.md`, which
named its own trigger when it was written: „this splits into four pages the
moment any source says something about any one of them." This document is
the first to say what Zero-Trust *does* — the segmented isolation that keeps
the Guardians from full awareness of each other (L205) — rather than only
naming it in `entropie-aegis`'s four-item list. `Cognitive Firewall`,
`Integrity Guardian` and `SIS` stay bundled; nothing has been said about them
yet.

**No page was created from an occurrence**, and this document supplied the
largest test of that rule so far: 108 candidates, 21 of them full character
profiles with real content — a role, a psychology, a world-link, an
arc-potential each — which is a far richer shape than document 5's brief or
even `kohaerenz-protokoll-konzept`'s seven-row sketch table. **The difference
is still the document's own hedge.** Every one of the 21 names is followed by
`oder ähnlich`; the document's own Section II calls the roster a refinement
still in progress, not a cast list. None of the 31 name-and-epithet
candidates this affects (ten Alters, eleven Nebencharaktere) became a page.
They are recorded on `alters.md` (the ten Alters, as one large reading) and
in `reconcile.json`'s `not_promoted` (the eleven Nebencharaktere, with
lines), the same treatment `kohaerenz-protokoll-konzept`'s seven-name
Alter-Archetypen table already received, extended to a document three times
its size.

The same restraint applied to the document's clinical-role vocabulary (Host,
ANP, EP, Gatekeeper, Protector, Persecutor, Caretaker, Internal Self-Helper,
Child Alter, Little, Switching, verdeckt, frontet — all recorded on
`alters.md` as this reading's supporting detail) and to AEGIS's own one-off
diagnostic vocabulary (Systemanomalie, Systemintegrität, Kontrollprotokoll,
Gesamtsystem, Kontrollparadigma, Homöostase, Feedbackloops, Nicht-Existenz,
Systemkollaps — recorded on `seele-info.md`, the same page
`kohaerenz-protokoll-konzept`'s equivalent vocabulary cluster already
occupies) and to `Ashby's Law of Requisite Variety` (a real cybernetic
citation the document argues AEGIS's blind spot from, not a corpus concept)
and `Heldenreise` (a writing-craft reference, the same treatment already
given document 5's borrowed monomyth vocabulary).

## The two things this document was flagged for before reading

**Q3.** The summary table (lines 502–511) hedges every Alter's Kern-Welt link
except six, and two of those six break one-alter-one-world *inside the
document's own most confident data*: `Nox` and `Praetor` both to Grenzfeste
(KW3), unhedged, and `Oblivion` given `KW2 (isoliert)/ KW3` — two worlds at
once, also unhedged. This is not the third roster's shape (two alters sharing
a world only in a document that called itself a sketch); it is a document
asserting its plainest data and contradicting the rule inside it. Recorded on
`q3-how-many-kern-welten-and-alters.md` and `alters.md`, unresolved — the
question splits further rather than closes.

**The roster problem.** `strukturelle-dissoziation-system-kael-analyse`
(censused, not reconciled) names eleven Anteile sharing **zero** names with
this document's ten Alters — verified by word-boundary count, both
directions, after two apparent hits (`Lia`/`Lex` as substrings of
`Julia`/`komplex`) turned out to be false. This is `C5`'s shape (two complete
sets, zero overlap) applied to Alters rather than locations, and it is the
fourth roster in this shape counting the ones `Q3` already tracks. **Raised
as `Wiki/conflicts/c6-alter-roster-two-documents.md`, not resolved.** The
other document is not reconciled by this run and is not touched — its own
reconciliation is next in `account.py order`.

One specific near-miss inside that conflict was checked directly rather than
left to a lookup that would never see it: `Nyx` (the other document's
roster) against `Nox` (this one's), one letter apart. `Nox` occurs 0 times in
`strukturelle-dissoziation-system-kael-analyse`; `Nyx` occurs 0 times here.
`fold()` correctly keeps them apart — recorded as `J83` because this is
exactly the shape a person, not code, has to judge.

## Readings added

Twenty-four pages, one document. Four worth naming specifically:

| page | what this document adds |
|---|---|
| `alters` | The fourth, disjoint ten-name roster whose own most confident rows break one-alter-one-world directly (see Q3 above). Carries the clinical vocabulary cluster and raises `C6`. |
| `aegis` | Independently confirms `entropie-aegis`'s own acronym expansion, word for word, eleven days later from an unrelated document — corroborates one side of conflict `C1` without choosing it (`J76`). |
| `guardians` | States the collective name is `Guardians` and `Wächter` is never it — the reverse of `roman-lokalitaeten-konzept-und-ausarbeitung`'s distribution, read the day before — and names the mechanism (`Zero-Trust-Protokolle`) behind the Guardians' limited mutual awareness. |
| `blinder-fleck` | Gives the blind spot to AEGIS, to each of the five Guardians, and to Kael himself, inside one profile-set — a third kind of bearer alongside the two `C4` already holds apart. |

Twenty more, each a shorter confirmation or extension: `seele-info`,
`kohaerenz`, `kohaerenz-programm`, `protokoll-v14`, `logos`, `mnemosyne`,
`cerberus`, `kairos`, `sophia`, `kael`, `did`, `konstrukt-stadt`,
`kern-welten`, `resonanz-landschaft`, `grenzfeste`, `externe-ebene`,
`entropie`, `risse`, `juna`, `moeglichkeits-garten`. Full detail and every
citation is on each page and in `reconcile.json`.

**Two readings this run had to override the mechanical near-match, not
follow it.** `Kohärenz Protokoll` (L124, AEGIS's own core programming) looked
by `fold()` like a near-match to `kohaerenz.md`; read in context it matches
`kohaerenz-programm.md`'s existing "the system itself" reading instead
(`J79`). `Systemkohärenz` (L137) is the opposite case — the lookup found no
match at all, and reading it against `kohaerenz.md`'s tracked property
confirms it is the same referent (`J77`).

**Two readings say something the wiki's index could not see coming.**
`Kairos` and `Sophia` are given their own separate paragraphs here — the
first source to write either name without the other, after two prior
documents that never separated them — and Sophia's world differs
(`Überwelt`, not `Möglichkeits-Garten`), recorded as a difference to watch
rather than a conflict, since neither document states the other wrong and
this is the first time either assignment has more than one source. And
`universal reboot` (L26, L146) independently confirms the Universal Reboot
already tracked on `protokoll-v14.md` — invisible to the lookup because that
page never registered the phrase as a tracked surface, the exact shape
`index_gaps_may_hide_matches` warns about in `reconcile.py`'s own output.

## A third spelling, recorded as a surface question

The document writes `Möglichkeiten-Garten` throughout (12 occurrences) and
never the tracked `Möglichkeits-Garten` or document 6's `Garten der
Möglichkeiten`. `fold()` keeps word order and hyphen placement, so nothing
merges the three mechanically. Read as the same world by context (paired
with `Konstrukt-Stadt`, `Resonanz-Landschaft` and `Grenzfeste` in the same
sentence a fourth time), recorded on `moeglichkeits-garten.md` as a third
surface — not resolved into one spelling, per the task's own framing of it
as a surface question rather than a new page.

## Judgements

Fifteen, `J69`–`J83`. Six settle intra-document near-matches (the document's
own candidate list folding against itself); seven settle wiki-lookup
near-matches; one (`J83`, Nyx/Nox) is proactive — not raised by
`reconcile.py` at all, because `Nyx` belongs to a document this run does not
touch, and recorded anyway because the task named it as exactly the kind of
near-miss a lookup cannot see and a person must.

Two worth naming beyond `J76`/`J77`/`J79`/`J83` above:

- **`J78` triggers a page split from its own precedent.** `aegis-teilfunktionen.md`
  named its split condition when it was written a document ago; this is the
  first time any source met it.
- **`J71`/`J73`/`J80` are three more instances of the same substring trap**
  already named `not-related` seven times in the ledger (`J53`, `J64`,
  `J65`, `J68` and others) — `Trauma-Halter` against bare `Alter`,
  `Gatekeeper` against `entropicgatekeeper`, checked and kept apart each
  time by the same rule: a shared normalised substring across unrelated
  compounds is not a term match.

`judgements.py` replays 83 judgements corpus-wide: 7 agree, 0 disagree, 76
still a person's call.

## Citation hygiene

`python3 scripts/quotes.py` before this run reported 17 unresolved (all
pre-existing, none touching this document); after this run, and after
`scripts/link.py --apply`, still 17, the same 17. Four self-inflicted defects
were caught and fixed before that count held:

- **A verbatim mismatch**: `assoziert` (the source's own spelling, missing
  the second `i`) was silently corrected to `assoziiert` while transcribing a
  Cerberus quote. Fixed by matching the source's spelling exactly, even where
  it looks like a typo — the same rule that caught „das Management" for „dem
  Management" the first time `quotes.py` ran.
- **An editorial insertion inside a verbatim quote**: `[die Guardians]` was
  added in brackets to clarify a pronoun, which is not a citation any more
  once the words change. Fixed by quoting the sentence as written and
  explaining the pronoun outside the quote marks.
- **Two mis-cited lines**: a Kael quote cited its own section heading (L28)
  instead of the sentence itself (L29), and a Glitchwyrm quote spanned three
  lines under one citation naming only the first. Both caught by
  `quotes.py`, both split or re-cited rather than patched around.
- **A digit `fold()` treats as a glued footnote number**: `KW2`/`KW3` inside
  a table cell normalise to `KW` for comparison, so a quoted `„KW2
  (isoliert)/ KW3"` could never resolve. Not a defect in the source or the
  citation — the cell is quoted correctly — but a case `read.py --find`
  itself refuses rather than mis-citing, and the fix was to describe the
  cell rather than quote it with `„…"` marks it cannot pass.

## What this run deliberately did not do

- Did not create a page for any of the ten Alters or eleven Nebencharaktere
  this document proposes, despite each carrying a full profile — the hedge
  (`oder ähnlich`, on every name) is what decided this, not the amount of
  content.
- Did not resolve conflict `C6`, the two-document Alter-roster problem, or
  choose which roster (if either) the novel keeps. Raised with its evidence;
  the resolution is an author's call.
- Did not touch `strukturelle-dissoziation-system-kael-analyse` — did not
  read it further, census it again, or reconcile it. It stays exactly as it
  was left: censused, noted, not reconciled, next in `account.py order`.
- Did not resolve the `Möglichkeits-Garten`/`Möglichkeiten-Garten` spelling
  question, or the `Kairos`/`Sophia` world disagreement — both recorded as
  differences to watch, per the rule that an ingest proposes and never
  resolves.
- Did not fix `capture.py`'s `PROSE` filter, which drops `Dr. Aris Thorne`
  from the parsed candidate list because of the abbreviation dot. Noted in
  `reconcile.json`'s `pre_classification`, treated by hand identically to
  the document's other ten Nebencharaktere, and left as a script defect for
  a separate change rather than patched mid-reconciliation.
