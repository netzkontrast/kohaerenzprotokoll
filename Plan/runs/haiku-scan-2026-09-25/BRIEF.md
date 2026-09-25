# Brief — one Haiku reader, one unread document

You scan **one** landed source document for what it says about the wiki's open
conflicts and questions. This is a triage scan, not an ingest: it produces no
census, no `03-candidates.md`, no page, no link and no judgement. Its job is to
tell a person whether the document is worth a full reading next, and what that
reading would find.

## Rules

- Canon prose is German and is never translated. Quote it exactly; write your
  own sentences in English.
- **Every quotation carries a line number that code gave you.** Get it with
  `python3 scripts/read.py <slug> --find "<exact words>"`, which answers
  `^[Lnn]` or refuses and names the nearest line. Never type a line number you
  did not get from `read.py`. If `--find` refuses, shorten the quote or drop it.
- Read the document with `python3 scripts/read.py <slug>` (every line prefixed
  by its number). For long documents read it in parts
  (`python3 scripts/read.py <slug> | sed -n '1,400p'`, then the next part).
  Read all of it.
- Record what the document says, attributed and unmerged. Never decide which
  source is right, never say a conflict is settled. „This document says X“ is
  the only form.
- Write **only** your one output file. Do not touch `Wiki/`, `Sources/`, any
  other file, and do not run git.

## Output — `Plan/runs/haiku-scan-2026-09-25/<slug>.md`

```
# <slug>

- title / date / category: (from `Sources/manifest.jsonl`, copied, not typed from memory)
- lines: N
- what it is: one or two sentences — its stance(s), and any claim it makes about
  its own authority (e.g. „Source-of-Truth“, „[K]/[V]“ labels), recorded not applied
- verdict: READ NEXT | READ LATER | LOW VALUE — and one sentence why

## Positions on open records
One subsection per conflict/question the document actually speaks to (skip the rest):
### C11 — Landauer warmth or cold ozone
- „<exact quote>“ ^[Lnn] — what position this is, in one line

## New to the wiki
Terms or claims this document gives that no page listed below covers, each with
one quote ^[Lnn]. At most 15.

## Chapters
Chapters (`Kap N`) it says something concrete about, one line each with ^[Lnn].
At most 15.

## Surprises
Anything that contradicts what the records below say every source says, with ^[Lnn].
```

## The open records (a summary — the records themselves are in `Wiki/conflicts/` and `Wiki/questions/`)

- **C1** What AEGIS stands for (expansions differ).
- **C2** What `Entropie` means (disorder AEGIS fights / creative matrix / AEGIS *is* the entropy).
- **C3** Where AEGIS comes from (from nothing / from the simulation / from Kael's defence in the Genesis).
- **C4** Whose is the blind spot — AEGIS' alone or each Guardian's.
- **C5** Is the Möglichkeits-Garten a whole Kern-Welt (KW4) or a place inside it.
- **C6** How many Guardians (two or five) and are they paired 1:1 with worlds. The author decided five: LogOS, Mnemosyne, Cerberus, Kairos, Sophia.
- **C7** When Juna first appears directly (Kap 33 Garten der Stillen Präsenz / Kap 38 / effect vs appearance).
- **C8** AEGIS' Approach in Storyform B — Be-er or Do-er.
- **C9** The Konstrukt-Stadt (decided: it is KW1).
- **C10** Do Kael's knuckles bleed in Kap 1, Kap 0, or in no chapter.
- **C11** Is the Landauer trace warm (Kap 6, Kap 36) or cold ozone.
- **C12** Three Genesis beats or four; does Komponente 734 come before the Trennungsprotokoll or out of it.
- **C13** Is the Basisrealität / Externe Ebene (Köln 2026) beyond the simulation or not.
- **C14** Does AEGIS get a first-person chapter (Kap 5–8) or only third person.
- **C15** Who carries Flight, the spatial riss (Kiko, Lia, Isabelle).
- **Q1** Are the Guardians components inside AEGIS.
- **Q2** Are the eight protocols (ANI, ARS, ECR, PMS, RSA, SNK, ZTV, Nullpunkt-Protokoll) the novel's vocabulary.
- **Q3** Do Kern-Welten correspond to Alters, or are worlds act markers only.
- **Q4** Who is *the* `Wächter`.
- **Q5** Guardians and Kern-Welten: the pairing, the Erasure-Pol's name, where Sophia went.
- **Open** Mosaik-Herz — one thing (Kap 11 beat) or two (Kap 34 place)? · The Ursprungs-Ich — is it Juna, what met Juna, or AEGIS? · The final form's name (Wir-AEGIS-plural?) · KW3 has no chapter in some plans · KW2 — Resonanz-Landschaft or Mnemosyne-Archipel? · Alex — arising in the separation or a pre-form before it? · `Einheit 734` — Kael's dwelling or Komponente 734? · Kap 40 — 39 chapters or 41 movements; the coda's content.

## Pages the wiki has (`Wiki/candidates/`)

aegis, aegis-metriken, aegis-teilfunktionen, alex, algorithmische-melancholie,
alters, ani, archiv-der-grenzen, archiv-des-ungesagten, argus, ars,
atemporalitaet, blinder-fleck, cache-kohaerenz, cerberus, coheron,
datenverarbeitungsknoten-7g, did, dkt, drei-ontologische-schichten, ecr,
emergenz, entropie, entropie-katastrophe, entropie-resonanz, entropie-signatur,
erason, evaluierungseinheit, externe-ebene, garten-der-stillen-praesenz,
genesis, grenzfeste, grosse-mauer, guardians, hitze-polaritaetsregel, isabelle,
juna, junas-ankerpunkt, k0-existenz, kael, kael-julia-bindung,
kaels-wohneinheit, kairos, kern-welten, kiko, kohaerenz, kohaerenz-kernel,
kohaerenz-programm, kollaps-kernel, konstrukt-stadt, landauer-signatur, lex,
lia, logos, mnemosyne, mnemosyne-server-architektur, moeglichkeits-garten,
moonshine-link, moros, mosaik-herz, multiplizitaet, negentropie, nexus,
nichts-rauschen, nullpunkt-protokoll, nyx, oblivion, partnerin,
persistenzgleichung, personas, pms, potentialmeer, protokoll-v14,
realitaetsebenen, resonanz-landschaft, rhys, risse, rsa, schleuse-7, sektor-04,
selene, silas, snk, sophia, system-monitor, telefon-stille,
therapie-schnittstelle-alpha, trennungsprotokoll, truth-rotation, ueberraum,
ueberwelt, vergessener-schrein, verschraenkungs-insel, ztv
