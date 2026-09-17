---
term: Zero-Trust
status: candidate
sources: 2
readings: 1
conflict: none
split_from: aegis-teilfunktionen
ingested: ["charakterkonzepte-fuer-kohaerenz-protokoll"]
gathered: "2026-09-17"
---

# Zero-Trust

**Split off `aegis-teilfunktionen.md` on 2026-09-17**, the first time any
source said something substantive about this one sub-function specifically
rather than merely naming it in the four-item list — see that page for
`Cognitive Firewall`, `Integrity Guardian` and `SIS`, still bundled because
nothing has been said about them.

## Named, not yet defined — `entropie-aegis`, 2025-04-17, brief

The original naming, in a list of four [[aegis|AEGIS]] sub-functions the document
guesses at rather than defines:

> „Wie könnte AEGIS' Rolle als \"Entropic Gatekeeper\" seine spezifischen
> Funktionen (**Zero-Trust**, Cognitive Firewall, Integrity Guardian, SIS)
> prägen? (z.B. Ist Zero-Trust eine Methode, um die Ausbreitung von
> \"entropischen\" Fehlern zu verhindern? …)"
> ^[entropie-aegis.md:L65]

That question — is Zero-Trust a method for preventing the spread of
"entropic" errors? — is asked and not answered here.

## Reading — `charakterkonzepte-fuer-kohaerenz-protokoll`, 2025-04-18

**The first source to say what Zero-Trust does, rather than only naming it.**
It is given as the cause of the [[guardians|Guardians]]' isolation from one another:

> „Aufgrund der segmentierten Natur des Systems (Zero-Trust-Protokolle,
> Kontext Pt 2) haben sie möglicherweise nur begrenztes Bewusstsein
> voneinander und operieren weitgehend isoliert in ihren jeweiligen Domänen,
> was zu Koordinationsproblemen oder widersprüchlichen Aktionen führen kann."
> ^[charakterkonzepte-fuer-kohaerenz-protokoll.md:L205]

(„sie" refers to the [[guardians|Guardians]], named two sentences earlier in the same
paragraph.)

This answers part of `entropie-aegis`'s own question in one specific
direction: Zero-Trust is read here as a segmentation principle applied to the
[[guardians|Guardians]] themselves — each confined to limited awareness of the others —
rather than (or in addition to) a filter against externally spreading errors.
Neither document contradicts the other; the second simply says more than the
first asked.

**Contributes a named mechanism to [[guardians|Guardians]]' own page**: a
possible cause for their described coordination problems, recorded there and
here.

## Not the same as `Zero-Trust-Architektur`

`Plan/runs/judgements.jsonl` J11 already separated this [[aegis|AEGIS]] sub-function
from the external cybersecurity standard it is named after — „a project term
named after an external standard is not that standard" — the corpus's first
recorded false conflict. This page's `Zero-Trust` is the AEGIS-internal
sub-function throughout, confirmed by this document's own context
(`Kontext Pt 2`, an AEGIS-internal citation) rather than any reference to the
external standard.

## Open

What the "Kontext Pt 2" document this document defers to actually says about
Zero-Trust — not yet read. Whether it is a defence against external
intrusion, an internal segmentation principle, or both.
