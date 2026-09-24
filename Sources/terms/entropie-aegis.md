---
source: Sources/drive/entropie-aegis.md
drive_id: "1Hx3IAeQUQYHo8TFjUQ8NmHKJIVq0Ba58ye8Vdxy3v7w"
title: "Entropie aegis"
category: theorie-physik
index_date: "2025-04-17"
extracted: "2026-09-16"
candidates: 46
---

# Term census — Entropie aegis

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py entropie-aegis`

```
  lines                100  (frontmatter ends at 9)
  body words           1314
  headings             0   bold-only lines 6
  table rows           0   code fences 0
  question marks       22
  backslash escapes    18
  typographic marks    2   ascii quotes 46
  invisible characters none
  math symbol lines    0
  glued ref numbers    0
  repeated labels      none
  longest line         777 chars
```

**Zero headings against six bold-only lines.** Section structure exists in this
document only as bold text, so nothing here can be cited by section — only by
line.

## Stance — this document marks none

`grep` finds no stance label anywhere: no „Beschreibung", „Bewertung",
`[User Query]` or equivalent. Whatever is said below about how to read it is
**inference from the text**, not something the document declares.

What the text shows: lines 23–83 are a commission — numbered research areas,
detailed questions, and a requested output format — and the document states what
the project already believes so that a researcher can build on it.

Read that way, **its terms are premises, not findings.** Nothing below is
something this document established.

*Format is measured above and is a separate question (decision 004). This
document has zero headings; that is a fact about the export and the author, not
a consequence of it being a commission.*

## Candidates — the project's own vocabulary

| term | n | lines | status | what this document says |
|---|--:|---|---|---|
| AEGIS | 19 | 17,19,21,59,63,65,69,71,81,89,93–99 | defined | „Autonomous Entropic Gatekeeper for Integrity Systems" ^[L19]; regulates the order→disorder transition to preserve coherence and integrity ^[L21] |
| Entropic Gatekeeper | 7 | 13,19,59,65,89,94,97 | role | AEGIS' role; **four occurrences carry no `AEGIS` in the sentence** |
| Überwelt | 10 | 13,17,57,80,89,93,94,97,99 | role | the digital world AEGIS governs; „Domäne des Entropic Gatekeepers" ^[L97] |
| Kern-Welten | 1 | 93 | known | „simulierte Kern-Welten", inside the same system as the Überwelt |
| Risse | 3 | 93,94 | defined | „direkte Manifestationen einer Zunahme von Entropie" beyond AEGIS' capacity ^[L94] |
| Guardians | 3 | 93,96 | role | „spezialisierte Agenten dieses Entropie-Managements" ^[L93] |
| Integrity Guardian | 1 | 65 | known | one of four named sub-functions — **a different term from `Guardians`** |
| Zero-Trust | 2 | 65 | known | a named sub-function |
| Cognitive Firewall | 1 | 65 | known | a named sub-function |
| SIS | 1 | 65 | known | a named sub-function, **not expanded anywhere in this document** |
| Michael | 4 | 95,96 | known | the protagonist, bearer of the DID |
| Julia | 3 | 71,96 | known | „die Verbindung zu einer externen, nicht-digitalen Ebene […] repräsentiert durch \"Julia\"" ^[L71] |
| DID / dissoziative Identitätsstruktur / psychische Fragmentierung | 6 | 63,67,69,81,95 | known | three surfaces, one referent; read as possibly a high-entropy state ^[L95] |
| Alters | 1 | 69 | asked | „die verschiedenen Bewusstseinszustände oder \"Alters\"" ^[L69] |
| Entropie-Signatur | 1 | 69 | asked | a proposed per-alter metric; the only content is the example „Angst als hohe Entropie" ^[L69] |
| Negentropie | 2 | 71,96 | asked | a possible order AEGIS cannot parse ^[L71]; „lebensfördernde Struktur" ^[L96] |
| Multiplizität | 1 | 95 | known | „gesunde Komplexität/Multiplizität" as against „destruktive Entropie/Chaos" |
| Kontrollinstanz | 3 | 13,17,89 | descriptor | „nicht-anthropomorphe Kontrollinstanz namens AEGIS" ^[L17] — never appears without AEGIS beside it |

## The root term is used as known and commissioned at once

`Entropie` occurs **53 times in the body**, more than any other string, and the
document never defines it. It states its status —

> „Diese Definition rückt Entropie von einem potenziellen Nebenthema zu einem
> **fundamentalen Organisationsprinzip und einer treibenden Kraft**" ^[L89]

— and then asks for the definition it has been using, in three senses it marks
as external:

| sense | asked at |
|---|---|
| thermodynamic — „Maß für Unordnung/Zustandsvielfalt", Zweiter Hauptsatz | 29 |
| information-theoretic — Shannon, „Maß für Unsicherheit, Informationsgehalt, Rauschen, Redundanz" | 31 |
| metaphorical — „psychische Entropie", entropy in social systems | 33 |

So the document supports four things called entropy and defines none: three it
names as external and asks about, and a fourth — its own working sense — that
runs through the text without ever being marked as separate.

## Imported from other disciplines

Not the project's terms. Recorded because a later document may adopt one.

| terms | lines | field |
|---|---|---|
| Zweiter Hauptsatz · Statistische Mechanik | 29 | thermodynamics |
| Shannon-Entropie · Informationstheorie · Redundanz · Rauschen | 31,39,51,57 | information theory |
| psychische Entropie · Selbstorganisation · Komplexität | 33,95,96 | systems theory, psychology |
| Systemtheorie · Kybernetik | 33 | — |
| Datenkorruption · Code-Degradation · „Bit Rot" · Signal-Rausch-Verhältnis | 37 | software decay |
| Fehlerkorrekturcodes · Garbage Collection · System-Resets · Selbstheilungsalgorithmen | 39 | software repair |
| Dissoziation · Abwehrmechanismen | 47,67,95 | clinical psychology |

`Rauschen` and `Redundanz` are also ordinary German words, used here as
information-theory terms.

## Coined in this document, inside quotation marks

| term | line | what it is |
|---|---|---|
| „Daten-Verwitterung" | 57 | a proposed visual metaphor for entropy in a digital world |
| „Reinigungswellen" | 59 | a proposed visible AEGIS intervention |
| „Entropie-Signatur" | 69 | a proposed per-alter metric |
| Quarantänezonen | 59 | a proposed containment mechanism |
| „Überwelt" | 13,57 | the world's name, introduced in quotes |

**In this document, quotation marks mark invention.** The document is proposing
vocabulary, not quoting a source.

## Named in one parenthesis, explained nowhere

> „seine spezifischen Funktionen (Zero-Trust, Cognitive Firewall, Integrity
> Guardian, SIS)" ^[L65]

Four terms, treated as already known, none explained. Everything after „z.B." in
that line is the document guessing at its own vocabulary.

## What the extraction ran into

**1. The frontmatter is inside the file.** Lines 1–9 carry `title` and `slug`, so
the frontmatter title `Entropie aegis` ^[L3] and `entropie-aegis` ^[L4] both answer a search for the
term. `Entropie` occurs 53 times in the body and 54 in the file, and a
case-insensitive search adds the slug on top.

Line numbers count from line 1, which is decided (`Sources/README.md`), so
**extraction skips to line 10 while citation does not.** Two line bases over one
file, by design.

**2. Substrings are not terms.** `Guardians` ⊄ `Integrity Guardian`;
`Negentropie` contains `entropie` and means its opposite. A count of „Guardian"
returns 4 and merges two different things.

**3. The converter's escaping sits inside the terms.** `\"Julia\"` at L71 is a
quoted name with backslashes. Every coinage in this document is quoted, so a
matcher that does not normalise misses all of them.

**4. Half the document is questions.** Lines 27–71 are the commission —
45 of 90 body lines. `Alters`, `Entropie-Signatur` and `Negentropie` appear
**only** inside questions, which is why `status: asked` exists: recording a
question as a claim turns the project's uncertainty into its position.
