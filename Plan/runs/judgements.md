# Judgement ledger — rendered

**Derived from `Plan/runs/judgements.jsonl` by `python3 scripts/judgements.py --render`. Do not edit.**

It exists so the decisions are searchable: qmd indexes markdown only, so the ledger itself is invisible to it. Ask the `decisions` collection by name.

## J1 — Die Konstrukt-Stadt / Konstrukt-Stadt

**one-term** · guardians-und-kern-welten-konzept · 2026-09-17 · replay: `agrees`

- **rule:** strip leading der/die/das before folding
- **mechanised by:** `wiki_index.fold`
- **features:** near-match:intra-list, german-article-prefix, worldbuilding

**Question.** one term or two?

**What was done.** compare referents; check whether the prefix appears in any cited name

**Result.** one term — a German definite article is never a term boundary

## J2 — Die Resonanz-Landschaft / Resonanz-Landschaft

**one-term** · guardians-und-kern-welten-konzept · 2026-09-17 · replay: `agrees`

- **rule:** strip leading der/die/das before folding
- **mechanised by:** `wiki_index.fold`
- **features:** near-match:intra-list, german-article-prefix, worldbuilding

**Question.** one term or two?

**What was done.** same as J1

**Result.** one term

## J3 — Die Grenzfeste / Grenzfeste

**one-term** · guardians-und-kern-welten-konzept · 2026-09-17 · replay: `agrees`

- **rule:** strip leading der/die/das before folding
- **mechanised by:** `wiki_index.fold`
- **features:** near-match:intra-list, german-article-prefix, worldbuilding

**Question.** one term or two?

**What was done.** same as J1

**Result.** one term

## J4 — Kern-Welten / Kern-Welt

**one-term** · guardians-und-kern-welten-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a German plural ending is not a term boundary
- **mechanised by:** `nothing`
- **features:** near-match:index, german-plural

**Question.** one term or two?

**What was done.** plural of the same compound, used interchangeably in one document

**Result.** one term

## J5 — Negentropie / Entropie

**two-terms** · entropie-aegis · 2026-09-17 · replay: `agrees`

- **rule:** containment by a negation prefix is never a surface variant
- **mechanised by:** `wiki_index.fold`
- **features:** substring, negation-prefix

**Question.** one term or two?

**What was done.** the longer form negates the shorter

**Result.** TWO terms — and the case that forbids an aggressive stemmer

## J6 — Der Möglichkeits-Garten / Nexus-Vorstufe / Möglichkeits-Garten

**one-term** · guardians-und-kern-welten-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a slash inside a heading is an apposition, not a list separator
- **mechanised by:** `nothing`
- **features:** near-match:intra-list, slash-in-heading, census-artifact

**Question.** one term or two?

**What was done.** read the heading: the slash joins a name and an apposition

**Result.** one term — the candidate was mis-split by the census reconstruction, not by the document

## J7 — Nexus-Vorstufe / Nexus

**two-terms** · guardians-und-kern-welten-konzept · 2026-09-17 · replay: `judgement`

- **rule:** containment where the longer form names a stage or part of the shorter is two terms
- **mechanised by:** `nothing`
- **features:** substring, qualifier-contains-head

**Question.** one term or two?

**What was done.** compare referents: Nexus-Vorstufe qualifies a world as a precursor; Nexus is the meta-space the Guardians appear in

**Result.** TWO terms — containment is a qualifier relation here, not a surface variant

## J8 — Kohärenz-Programm / Kohärenz

**two-terms** · guardians-und-kern-welten-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a compound naming an entity is not a surface of the property it contains
- **mechanised by:** `nothing`
- **features:** near-match:index, compound, names-a-system

**Question.** surface or separate term?

**What was done.** compare referents: Kohärenz is the measurable property, Kohärenz-Programm the system being measured

**Result.** SEPARATE term

## J9 — Das Seelen-Kohärenz-Protokoll / Kohärenz

**two-terms** · guardians-und-kern-welten-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a title containing a term is never a surface of that term
- **mechanised by:** `nothing`
- **features:** near-match:index, compound, names-the-project, quoted

**Question.** surface or separate term?

**What was done.** compare referents: this is the project's own title as this document gives it

**Result.** SEPARATE term, and a project-title variant — other documents say Kohärenz Protokoll

## J10 — Guardians / Integrity Guardian

**two-terms** · entropie-aegis · 2026-09-17 · replay: `judgement`

- **rule:** a shared head noun is not a shared referent
- **mechanised by:** `nothing`
- **features:** substring, shared-head-different-role

**Question.** one term or two?

**What was done.** compare referents: Guardians are the novel's agents; Integrity Guardian is one of AEGIS' named sub-functions

**Result.** TWO terms in one document

## J11 — Zero-Trust / Zero-Trust-Architektur

**two-terms** · aegis-emergenz-aus-der-leere · 2026-09-17 · replay: `judgement`

- **rule:** a project term named after an external standard is not that standard
- **mechanised by:** `nothing`
- **features:** substring, project-named-after-external

**Question.** one term or two?

**What was done.** compare referents: one is an AEGIS sub-function, the other the established cybersecurity architecture it was named after, explicitly distinguished by the source

**Result.** TWO terms, related by naming — the corpus's first false conflict

## J12 — Kael / Kael-Julia-Bindung

**two-terms** · corpus-wide · 2026-09-17 · replay: `agrees`

- **rule:** a compound is its own token; corpus.py family <head> makes the difference visible
- **mechanised by:** `rules.surfaces`
- **features:** compound, index-token-semantics, corpus-wide

**Question.** does a compound add to the count of its head?

**What was done.** compare the two views: the surface index counts a compound as one token, a \b-regex counts the head inside it

**Result.** TWO tokens. Kael = 287 documents by index, 293 by regex; the difference is compounds. Neither is wrong — they answer different questions and must never be quoted as the same fact.

## J13 — Kael-Julia-Bindung / Kael-Juna-Verbindung

**open** · corpus-wide · 2026-09-17 · replay: `judgement`

- **rule:** before naming a page from a read sample, ask the corpus what it calls the thing
- **mechanised by:** `nothing`
- **features:** renamed-entity, corpus-vs-read-sample, one-document-term

**Question.** is the term on the page the corpus's name for this thing?

**What was done.** corpus.py count on both

**Result.** OPEN, and the page is probably misnamed. Kael-Julia-Bindung: 1 document, 16 occurrences, 2025-04-19 only. Kael-Juna-Verbindung: 9 documents, 31 occurrences, 2025-04-23 to 2026-06-10. The page is named after the one document that was read.

## J14 — Der Möglichkeits-Garten / Nexus-Vorstufe / Möglichkeits-Garten

**one-term** · guardians-und-kern-welten-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a slash inside a heading is an alias or a role, never a term boundary
- **mechanised by:** `nothing`
- **features:** heading-slash-alias, article

**Question.** one term or two?

**What was done.** read the heading: the slash is the document's own alias notation, naming the world and what it is a precursor to

**Result.** ONE term. The page is Möglichkeits-Garten; `Nexus-Vorstufe` is a role the heading assigns it, not a second name for it.

## J15 — Der Möglichkeits-Garten / Nexus-Vorstufe / Nexus

**two-terms** · guardians-und-kern-welten-konzept · 2026-09-17 · replay: `judgement`

- **rule:** X-Vorstufe is not X; a precursor names a relation, not an identity
- **mechanised by:** `nothing`
- **features:** substring, part-and-whole

**Question.** one term or two?

**What was done.** compare referents: the Möglichkeits-Garten is one of four Kern-Welten; the Nexus is the meta-space above them. The heading says the world is its *Vorstufe* — a precursor is not the thing.

**Result.** TWO terms, related by position in the same hierarchy.

## J16 — Kohärenz-Programm / Kohärenz

**two-terms** · guardians-und-kern-welten-konzept · 2026-09-17 · replay: `agrees`

- **rule:** a compound is its own token
- **mechanised by:** `rules.surfaces`
- **features:** compound, index-token-semantics

**Question.** one term or two?

**What was done.** apply J12's rule: a compound is its own token. Kohärenz is the property the system maintains; the Kohärenz-Programm is the system.

**Result.** TWO terms. Same relation as Kael / Kael-Julia-Bindung.

## J17 — Das Seelen-Kohärenz-Protokoll / Kohärenz

**two-terms** · guardians-und-kern-welten-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a quoted work title beside `Romanprojekt`/`Projekt` names the work, not a concept inside it
- **mechanised by:** `nothing`
- **features:** work-title, compound, quoted

**Question.** one term or two?

**What was done.** read the context: it appears in quotation marks after `Romanprojekts` — it is the novel's title, not a concept in the novel

**Result.** TWO terms, and the second is not a term of the fiction at all. A page may be warranted for the title; it is not a reading of Kohärenz.

## J18 — Nexus / Überraum

**open** · guardians-und-kern-welten-konzept · 2026-09-17 · replay: `judgement`

- **rule:** regularity of position is evidence, not a statement; do not merge on it
- **mechanised by:** `nothing`
- **features:** two-names-same-sentences, field-name-vs-filler, no-statement

**Question.** one term or two?

**What was done.** count and compare positions: the field is named `Repräsentation im Nexus` five times, and all five filled instances open `Im Überraum…`. Nexus 11 occurrences, Überraum 5.

**Result.** OPEN. The pattern is too regular for accident — a field name in one vocabulary, filled in another — but the document never states they are one space. Kept as two pages, cross-referenced, not merged.

## J19 — Die Konstrukt-Stadt / Konstrukt-Stadt

**one-term** · guardians-und-kern-welten-konzept · 2026-09-17 · replay: `agrees`

- **rule:** a leading German definite article is never a term boundary
- **mechanised by:** `wiki_index.fold`
- **features:** article, exact-fold-match

**Question.** does the definite article split a term?

**What was done.** fold() both; keys are identical (konstruktstadt). Same for Die Grenzfeste/Grenzfeste and Die Resonanz-Landschaft/Resonanz-Landschaft.

**Result.** ONE term, three times over. reconcile.py reported both surfaces as separate new terms until this run — its containment guard excluded exact equality, so the article rule it was built on never fired.

## J20 — Wächter / Guardian

**judgement** · aegis-subplots-kapitelweise-system-exploration-docx · 2026-09-17 · replay: `judgement`

- **rule:** Wächter is never resolved by the surface — the referent is decided by the sentence, and a page may not claim the word
- **mechanised by:** `nothing`
- **features:** translation, one-word-several-referents, register-split

**Question.** is the German Wächter the same term as the English Guardian?

**What was done.** Counted where each appears. Guardian stands alone 22 times across every analytic field; Wächter appears 3 times, and never in analysis — twice in invented subplot titles and once inside one. The English word is the analytic register and the German one the fictional register — Guardian never appears in a subplot title, Wächter never in analysis.

**Result.** AMBIGUOUS, and worse: across the corpus Wächter carries FOUR referents. The aegis page lists „Wächter der systemischen Stabilität" as an alias of AEGIS; document 4 names a Wächter-Persona who experiences the Grenzfeste (L85); this document uses it for a Guardian at L279 and for Kael's final role at L531.

## J21 — Entropie-Score / globaler Entropie-Score

**one-term** · aegis-subplots-kapitelweise-system-exploration-docx · 2026-09-17 · replay: `judgement`

- **rule:** a leading adjective that names scope does not split a term
- **mechanised by:** `nothing`
- **features:** adjective-qualifier, known-alias

**Question.** is the document's 'Entropie-Score' the metric the wiki already records?

**What was done.** aegis-metriken carries „globaler Entropie-Score" as an alias from document 3. This document writes „einen niedrigen 'Entropie-Score'" at L42, in the same role: a number AEGIS assigns to a state.

**Result.** ONE term. The qualifier globaler names a scope, not a different metric.

## J22 — Guardian / IntegrityGuardian

**two-terms** · aegis-subplots-kapitelweise-system-exploration-docx · 2026-09-17 · replay: `judgement`

- **rule:** containment across a class name and a proper name is not evidence — an instance is a reading on the class, a namesake is not
- **mechanised by:** `nothing`
- **features:** compound, camelcase-name

**Question.** is IntegrityGuardian an instance of Guardian or a separate thing?

**What was done.** IntegrityGuardian is on aegis-teilfunktionen from document 1, as a named subfunction of AEGIS. Guardian here is the general role, of which LogOS, Cerberus, Mnemosyne and the Architekten are instances.

**Result.** TWO terms. Containment matched the word and not the thing: a class and one system's named function are not the same term, even when one name contains the other.

## J23 — Guardian / Guardians

**one-term** · aegis-subplots-kapitelweise-system-exploration-docx · 2026-09-17 · replay: `judgement`

- **rule:** an English plural -s is never a term boundary, the same way a German article is not
- **mechanised by:** `nothing`
- **features:** plural, english-loanword

**Question.** does the English plural split the term?

**What was done.** fold() leaves guardian and guardians distinct because the rule strips German articles, not English plural s.

**Result.** ONE term. The document alternates freely within single sentences.

## J24 — Riss / Risse

**one-term** · aegis-subplots-kapitelweise-system-exploration-docx · 2026-09-17 · replay: `judgement`

- **rule:** a German plural is never a term boundary
- **mechanised by:** `nothing`
- **features:** plural, german-umlaut-plural

**Question.** singular and plural of the same term?

**What was done.** Both appear in the same sentences at L93 and L99; the page risse already exists from document 4.

**Result.** ONE term.

## J25 — Alter / Alters

**one-term** · aegis-subplots-kapitelweise-system-exploration-docx · 2026-09-17 · replay: `judgement`

- **rule:** a German plural is never a term boundary
- **mechanised by:** `nothing`
- **features:** plural, quoted-term

**Question.** same?

**What was done.** The document writes 'Alters' in single quotes 6 times and Alter alone once. The alters page exists.

**Result.** ONE term.

## J26 — Kernwelt 1 / Kern-Welt

**one-term** · aegis-subplots-kapitelweise-system-exploration-docx · 2026-09-17 · replay: `judgement`

- **rule:** a hyphen inside a compound is never a term boundary, and a numbered instance is a reading on its class
- **mechanised by:** `nothing`
- **features:** numbered-instance, hyphenation, abbreviation

**Question.** is KW1 a new term or one of the Kern-Welten?

**What was done.** L152 expands the abbreviation once: „Untersucht Kernwelt 1 (Logik/LogOS)…". The wiki's kern-welten page holds four worlds from document 4. This document never writes the hyphenated form at all — 0 occurrences.

**Result.** ONE term, and KW1 is an instance of it. The hyphen is the wiki's spelling and KW the document's abbreviation; neither is a second term.

## J27 — Entropie / Prä-Entropie

**two-terms** · aegis-subplots-kapitelweise-system-exploration-docx · 2026-09-17 · replay: `judgement`

- **rule:** a prefix that negates or precedes makes a new term; a prefix that qualifies does not
- **mechanised by:** `nothing`
- **features:** prefix, classification-stage

**Question.** does the prefix make a new term?

**What was done.** L35 asks whether AEGIS classifies Kael's states as „niedrigstufiges 'Rauschen' oder potenzielle 'Prä-Entropie'" — a stage before entropy, used to decide whether to act.

**Result.** TWO terms. Prä- names something entropy is not yet.

## J28 — Entropie / Entropiemanagement

**judgement** · aegis-subplots-kapitelweise-system-exploration-docx · 2026-09-17 · replay: `judgement`

- **rule:** a compound is placed by what it names, never by its head — the head predicts nothing
- **mechanised by:** `nothing`
- **features:** german-compound, head-is-known-term

**Question.** where does a compound whose head is a known term belong?

**What was done.** Four in this document: Entropiegewinn (a quantity gained), Entropiepotenzial (a number AEGIS computes about Kael, L178), Entropiemanagement (AEGIS' stated function, L63), Informationsentropie (Shannon's, imported under Konzept/Trope).

**Result.** FOUR different answers. Entropiegewinn is a reading on entropie; Entropiepotenzial belongs with aegis-metriken beside the Entropie-Score; Entropiemanagement is a term of its own and has no page; Informationsentropie is imported theory and is not canon at all.

## J29 — AEGIS / Rest-AEGIS

**one-term** · aegis-subplots-kapitelweise-system-exploration-docx · 2026-09-17 · replay: `judgement`

- **rule:** a prefix naming a later state of the same bearer does not make a new term
- **mechanised by:** `nothing`
- **features:** prefix, state-of-a-thing

**Question.** new term or a state?

**What was done.** L531 describes AEGIS after the climax „nicht mehr als allmächtiger Kontrolleur, sondern vielleicht als eine Art Hausmeister des Kernsystems". One occurrence, inside a subplot, heavily hedged.

**Result.** ONE term. Rest- names a later state of the same entity, and the page can carry it as a reading.

## J30 — Simulation / Simulations-Engine

**judgement** · aegis-subplots-kapitelweise-system-exploration-docx · 2026-09-17 · replay: `judgement`

- **rule:** *none stated — still open*
- **mechanised by:** `nothing`
- **features:** compound, page-is-elsewhere

**Question.** the wiki maps Simulation to the ueberwelt page — does this document mean that?

**What was done.** This document uses Simulation 17 times for the constructed world Kael lives in, and Simulations-Engine for what runs it. The wiki's ueberwelt page came from other documents.

**Result.** UNRESOLVED and recorded as such. Whether this document's Simulation is the wiki's Überwelt cannot be settled from this document, which never uses the word Überwelt.

## J31 — Teil 1 / Teil 2

**not-a-term** · aegis-subplots-kapitelweise-system-exploration-docx · 2026-09-17 · replay: `judgement`

- **rule:** a label that partitions the document is not a term, however often it repeats
- **mechanised by:** `nothing`
- **features:** document-structure, repeated-label

**Question.** are the part headings terms?

**What was done.** Teil 1/2/3 occur 16/17/15 times, every one inside a chapter label like „**Kapitel 7 / Teil 1**". They partition this document and name nothing in the world.

**Result.** NOT terms. Same for INNERE REISE, META-EBENE and ÄUSSERE KONFRONTATION, which the count missed anyway because the document writes them in full capitals.

## J32 — Kernsystem / Kernsystemprotokoll

**two-terms** · aegis-subplots-kapitelweise-system-exploration-docx · 2026-09-17 · replay: `judgement`

- **rule:** a compound is placed by what it names, never by its head
- **mechanised by:** `nothing`
- **features:** german-compound, found-by-surface-scan

**Question.** same?

**What was done.** Kernsystem is what Rest-AEGIS maintains (L531). Kernsystemprotokoll is a document Kael might find that shows how AEGIS computes entropy (L293). Neither was found by the reading as a standalone word; both surfaced only when capture.py started listing inflected forms.

**Result.** TWO terms, and one of them the reading missed entirely.
