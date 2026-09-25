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

## J33 — Wächter / Guardians

**judgement** · roman-lokalitaeten-konzept-und-ausarbeitung · 2026-09-17 · replay: `judgement`

- **rule:** *none stated — still open*
- **mechanised by:** `nothing`
- **features:** translation, page-is-elsewhere, known-ambiguous-word

**Question.** this document says Wächter 12 times and Guardian 0 — is Wächter a surface of the guardians page?

**What was done.** The four bearers are named in one parenthesis at L35 (LogOS, Mnemosyne, Cerberus, Kairos/Sophia), which is exactly the roster the guardians page carries. But Q4 records four other bearers of the word across the corpus, one of them an alias already folded onto the aegis page.

**Result.** UNRESOLVED, and the surface was deliberately NOT added. The reading goes on guardians; the word stays unclaimed. Adding it would map all twelve analytic uses of a four-bearer word onto one page by lookup.

## J34 — Kairos / Kairos/Sophia

**one-term** · roman-lokalitaeten-konzept-und-ausarbeitung · 2026-09-17 · replay: `judgement`

- **rule:** a slash between two names the wiki already has is an alias, not a term boundary
- **mechanised by:** `nothing`
- **features:** slash, never-separated

**Question.** is the slashed pair a third term beside kairos and sophia?

**What was done.** Measured: all 10 occurrences of Kairos and all 10 of Sophia are inside Kairos/Sophia. Neither name stands alone anywhere in the file.

**Result.** ONE term per name — the slash is an alias joining two existing pages, not a new bearer. The reading goes on kairos and the measurement on sophia. Same shape as J14 (Der Möglichkeits-Garten / Nexus-Vorstufe).

## J35 — Möglichkeits-Garten / Garten der Möglichkeiten

**one-term** · roman-lokalitaeten-konzept-und-ausarbeitung · 2026-09-17 · replay: `judgement`

- **rule:** *none stated — still open*
- **mechanised by:** `nothing`
- **features:** word-order, cross-document, scale-mismatch

**Question.** same place, or two gardens?

**What was done.** Document 4 has Möglichkeits-Garten as KW4 entire; this document has Garten der Möglichkeiten as one of eight KW4 locations, marked `Konzept Doc` so the name is inherited. Level, bearer, subject matter and cast agree. fold() keeps word order so nothing mechanical joins them.

**Result.** ONE term, and the sources disagree about its SCALE — a Realität against a Bereich with „Tore zu anderen Bereichen von KW4" (L436). Recorded as conflict C5 rather than merged.

## J36 — Nexus / Nexus-Interface

**judgement** · roman-lokalitaeten-konzept-und-ausarbeitung · 2026-09-17 · replay: `judgement`

- **rule:** *none stated — still open*
- **mechanised by:** `nothing`
- **features:** compound, scale-mismatch, cross-document

**Question.** is the KW4 interface the meta-space the wiki already has?

**What was done.** Document 4's Nexus sits above the Kern-Welten. This document's Nexus-Interface is a location inside KW4 (L218, L413) and the document contains no word for a level above the six. Neither says anything about the other.

**Result.** UNRESOLVED. No page created for Nexus-Interface, because creating one asserts they are two terms — which is the open question. Noted on the nexus page instead.

## J37 — Kern-Welt / KW1

**one-term** · roman-lokalitaeten-konzept-und-ausarbeitung · 2026-09-17 · replay: `judgement`

- **rule:** a numbered instance of a class the wiki has is a reading on that class, not a new term
- **mechanised by:** `nothing`
- **features:** abbreviation, numbered-instance

**Question.** does a numbered world get its own page?

**What was done.** Same case J26 decided on document 5, now with all four numbers present and each carrying a domain bearer (L172-L175).

**Result.** ONE term — a numbered instance is a reading on its class. KW1-KW4 all go to kern-welten and no page is created for any of them.

## J38 — Limina / Liminale Räume

**two-terms** · roman-lokalitaeten-konzept-und-ausarbeitung · 2026-09-17 · replay: `judgement`

- **rule:** a candidate that shares a stem with a cited external concept is checked against the reference list before it is a surface
- **mechanised by:** `nothing`
- **features:** shared-stem, imported-theory, substring-trap

**Question.** the count merges them — are they related?

**What was done.** Limina is an Alter associated with KW1 (L172). Liminale Räume is a design concept cited to an external Wikipedia reference (L152, refs 64-66). The candidate scored 9 standing alone and 19 including the theory.

**Result.** TWO terms and not even the same kind of thing. The Alter gets no page from this document (it is named as an example and never described); the concept is imported theory and never canon.

## J39 — Simulation / Überwelt

**two-terms** · roman-lokalitaeten-konzept-und-ausarbeitung · 2026-09-17 · replay: `judgement`

- **rule:** *none stated — still open*
- **mechanised by:** `nothing`
- **features:** page-is-elsewhere, third-document

**Question.** J30 left this unresolved — does a third document settle it?

**What was done.** This document uses Überwelt 27 times for the digital level and Simulation 4 times for the whole construct that contains all six levels: „die Geschichte der Simulation (Post-Reboot-Zustand)" (L89), „die Fragilität der Simulation" (L61).

**Result.** TWO terms, from this document. It is the first source to use both words, and they do not coincide: the Simulation contains the Überwelt. The surface Simulation is still mapped to ueberwelt in the index and that mapping is now doubtful. Recorded, not changed.

## J40 — Lokalitäten-Profil / Konzept/Zweck

**not-a-term** · roman-lokalitaeten-konzept-und-ausarbeitung · 2026-09-17 · replay: `judgement`

- **rule:** a label that partitions the document is not a term, however often it repeats
- **mechanised by:** `nothing`
- **features:** document-structure, repeated-label, template

**Question.** the eleven profile fields repeat 17-18 times each — are they terms?

**What was done.** They are the template this document defines for itself at L105-L115 and then fills seventeen times. Five of the eleven are renamed between definition and use (Atmosphäre/Stimmung -> Atmosphäre/Mood), which is why the profile counts them at 17 and the other six at 18.

**Result.** NOT terms. Same call as J31 on Teil 1/2/3: a label that structures the document names nothing in the world. Lokalitäten-Profil itself scored 0 as a word and exists only inflected.

## J41 — Die Große Mauer / Grenzfeste

**two-terms** · roman-lokalitaeten-konzept-und-ausarbeitung · 2026-09-17 · replay: `judgement`

- **rule:** *none stated — still open*
- **mechanised by:** `nothing`
- **features:** cross-document, no-shared-string, scale-mismatch

**Question.** is the wall around KW3 the same thing as document 4's KW3?

**What was done.** Document 4's Grenzfeste is a Kern-Welt, „eine Realität, die als Schutzraum, Quarantänezone oder Kontrollzentrum konzipiert ist". This document's Große Mauer is a barrier that „KW3 umgibt oder durchzieht" (L362), with gates through it. Grenzfeste occurs 0 times here.

**Result.** TWO terms. A wall around a fortress is not the fortress, and no read source relates them. Page created for the wall; the relation recorded as open on both.

## J42 — Realitätsebenen / Kern-Welten

**two-terms** · roman-lokalitaeten-konzept-und-ausarbeitung · 2026-09-17 · replay: `judgement`

- **rule:** a set is not its largest subset
- **mechanised by:** `nothing`
- **features:** class-and-member

**Question.** is the six-level frame just another word for the worlds?

**What was done.** L105 enumerates the six as „KW1-4, Überwelt, Externe Ebene" — four Kern-Welten plus two levels that are not Kern-Welten. The document uses Realitätsebenen 7 times and Kern-Welten 18.

**Result.** TWO terms, in a class/member relation. New page realitaetsebenen, and it is what bounds the Kern-Welt count for Q3.

## J43 — Orakel / Orakel/Muse

**one-term** · roman-lokalitaeten-konzept-und-ausarbeitung · 2026-09-17 · replay: `judgement`

- **rule:** a slash between two names the wiki already has is an alias, not a term boundary
- **mechanised by:** `nothing`
- **features:** slash, never-separated, substring-trap

**Question.** same shape as J34, and Muse collides with Museum

**What was done.** All 10 occurrences of Orakel and all 10 of Muse standing alone are inside Orakel/Muse; the 4 extra hits on Muse are Museum and Museen in a gallery profile. It is an Alter, not a Wächter (L175).

**Result.** ONE term. No page — the Alter is named as an example („Alters wie Orakel/Muse") and never described. Recorded on alters with its line.

## J44 — Anomalie / Anomalien

**one-term** · roman-lokalitaeten-konzept-und-ausarbeitung · 2026-09-17 · replay: `judgement`

- **rule:** a German plural is not a term boundary
- **mechanised by:** `nothing`
- **features:** german-plural, zero-as-a-word

**Question.** the candidate scored 0 as a word — is it absent?

**What was done.** 0 standing alone, 7 including compounds, and all 7 are the plural Anomalien (L188, L280, L282, L285, L464, L469). The reading proposed the singular because that is how a reader holds a term.

**Result.** ONE term, present seven times, written only in the plural. The same shape fold() misses on Guardian/Guardians and Riss/Risse.

## J45 — Riss / Risse

**one-term** · roman-lokalitaeten-konzept-und-ausarbeitung · 2026-09-17 · replay: `judgement`

- **rule:** a German plural is not a term boundary
- **mechanised by:** `nothing`
- **features:** german-plural, already-a-surface

**Question.** the page is risse and this document writes both

**What was done.** 6 standing alone as Riss, 40 as Risse, plus Rissen, Riss-Manifestationen, Riss-Ursprung. Single-quoted throughout: 20 of the document's 32 single-quoted tokens are one of the two.

**Result.** ONE term. Already the page's name; recorded because the ledger is also the trainset and fold() still misses this pair.

## J46 — Alters / Alter

**one-term** · kohaerenz-protokoll-storyform-und-outline-2026-06-10-md · 2026-09-24 · replay: `judgement`

- **rule:** an English plural -s on a German noun is not a term boundary
- **mechanised by:** `nothing`
- **features:** english-plural, german-plural, already-a-surface

**Question.** the page is alters and this document writes Alter

**What was done.** Alter 13 times standing alone, in the heading „13 Alter“ (L253), the table column (L259) and the POV rule (L206); Alters twice, in the veil rule (L46) and Vortex 1 (L378).

**Result.** ONE term. The German plural is Alter; Alters is the anglicised plural of the same noun.

## J47 — AEGIS / Wir-AEGIS

**two-terms** · kohaerenz-protokoll-storyform-und-outline-2026-06-10-md · 2026-09-24 · replay: `judgement`

- **rule:** a later state is the same term only when the bearer is the same; a name the source marks as undecided gets no page
- **mechanised by:** `nothing`
- **features:** later-state, different-bearer, name-open

**Question.** four surfaces of a final form built on AEGIS — Wir-AEGIS, Wir-AEGIS-plural, AEGIS-plural, Mosaik-AEGIS

**What was done.** L412: „Kael-als-Wir wird neue AEGIS, aber wesensanders“. L475 lists the names as alternatives with status open (OQ-A).

**Result.** TWO terms. The final form's bearer is Kael's Wir, not AEGIS; J29 does not apply. No page: the document itself says the name is undecided. Recorded on the aegis page.

## J48 — Kael / System Kael

**two-terms** · kohaerenz-protokoll-storyform-und-outline-2026-06-10-md · 2026-09-24 · replay: `judgement`

- **rule:** the whole a member belongs to is not the member
- **mechanised by:** `nothing`
- **features:** whole-and-member, roster

**Question.** is System Kael a surface of Kael?

**What was done.** L253 heads the table „System Kael (TSDP-Architektur, 13 Alter)“; L260 gives Kael as one row, „Kael (Host) · amnestische Oberfläche“.

**Result.** TWO terms. The system is the thirteen; Kael is one of them. The roster goes on alters.

## J49 — Logos-Prime / LogOS

**two-terms** · kohaerenz-protokoll-storyform-und-outline-2026-06-10-md · 2026-09-24 · replay: `judgement`

- **rule:** a world name built from a bearer's name is not the bearer; containment across a proper name is not evidence
- **mechanised by:** `nothing`
- **features:** proper-name-containment, world-name, bearer-name

**Question.** four world names contain page names — Logos-Prime/logos, Mnemosyne-Archipel/mnemosyne, Cerberus-Labyrinth/cerberus, Überwelt-Nexus/nexus

**What was done.** L219–L222 name the Kern-Welten; L214 heads the table „KEIN Guardian-1:1“. The earlier pages are Guardians.

**Result.** TWO terms each. The document names worlds after former bearers while denying the pairing; the containment is the conflict (C6), not an identity.

## J50 — Wohneinheit 734 / Kaels Wohneinheit 1.0

**one-term** · kohaerenz-protokoll-storyform-und-outline-2026-06-10-md · 2026-09-24 · replay: `judgement`

- **rule:** a dwelling is identified by its occupant and its place; a differing number is a reading, not a new term
- **mechanised by:** `nothing`
- **features:** numbered-instance, same-occupant

**Question.** the page is Kaels Wohneinheit 1.0 and this document numbers the dwelling 734

**What was done.** L306: Kael's first day runs „Wohneinheit 734 → Datenknoten Epsilon → Transitkorridor Delta-7“ in KW1 — the page's referent by occupant and place.

**Result.** ONE term. Same dwelling by the sentence; the differing number is a reading on the page.

## J51 — Nichts-Rauschen / Rauschen

**two-terms** · kohaerenz-protokoll-storyform-und-outline-2026-06-10-md · 2026-09-24 · replay: `judgement`

- **rule:** a source equating two surfaces once does not make them one term everywhere
- **mechanised by:** `nothing`
- **features:** qualified-compound, source-equates-once

**Question.** is every Rauschen the Nichts-Rauschen?

**What was done.** L386 equates them once: „das Rauschen, das hier beginnt, ist das Nichts-Rauschen“. Elsewhere Rauschen stands alone (L298, L398) with no such statement.

**Result.** TWO terms. Equated only where the source says so.

## J52 — Trennungsprotokoll / Trennung

**two-terms** · kohaerenz-protokoll-storyform-und-outline-2026-06-10-md · 2026-09-24 · replay: `judgement`

- **rule:** an event and the state it produces are two terms
- **mechanised by:** `nothing`
- **features:** event-and-state

**Question.** is Trennung a short form of Trennungsprotokoll?

**What was done.** Trennung names the state („Die Trennung war nie real“, L21; Goal of B, L183); Trennungsprotokoll the event that produced it (L298).

**Result.** TWO terms. An event is not the state it produces.

## J53 — Landauer-Signatur / Entropie-Signatur

**two-terms** · kohaerenz-protokoll-storyform-und-outline-2026-06-10-md · 2026-09-24 · replay: `judgement`

- **rule:** a shared head noun is not a shared referent
- **mechanised by:** `nothing`
- **features:** shared-head, cross-document

**Question.** a new page beside an existing one with the same head

**What was done.** Landauer-Signatur is defined here (L64); Entropie-Signatur is a coinage inside a question in another document.

**Result.** TWO terms.

## J54 — Basisrealität / Externe Ebene

**one-term** · kohaerenz-protokoll-charakter-bibel-2026-05-08-md · 2026-09-24 · replay: `judgement`

- **rule:** two names given the same place and the same attributes in the same words are one term
- **mechanised by:** `nothing`
- **features:** same-description, cross-document

**Question.** the Basisrealität of this document and the Externe Ebene of the other canon-era source

**What was done.** L62: „Die Basisrealität — Köln 2026 … nur als Erinnerungsfragment, als Telefonton, als Geruch.“ The other: „Externe Ebene (Köln 2026 — nie Bühne, nur Erinnerungsfragment, Telefonton, Geruch)“.

**Result.** ONE term. Same place, same four attributes, word for word.

## J55 — Kael / System Kael

**judgement** · kohaerenz-protokoll-charakter-bibel-2026-05-08-md · 2026-09-24 · replay: `judgement`

- **rule:** a name the source uses for a whole and one of its members is resolved by the sentence, never by the surface
- **mechanised by:** `nothing`
- **features:** one-surface-two-referents, whole-and-member

**Question.** this document uses the bare name for both the system and the host

**What was done.** L298: „Kael ist ein System“; L315: „Kael auch eine spezifische ANP-Instanz: der Host“.

**Result.** JUDGEMENT per sentence. J48 held for the other document, which wrote System Kael; here the bare name carries both, and the page records both, attributed.

## J56 — Coheron / Coheronen

**one-term** · kohaerenz-protokoll-charakter-bibel-2026-05-08-md · 2026-09-24 · replay: `judgement`

- **rule:** a German plural is not a term boundary
- **mechanised by:** `nothing`
- **features:** german-plural

**Question.** the plural as a candidate

**What was done.** Coheronen at L256 and L913, the singular elsewhere.

**Result.** ONE term.

## J57 — Kohärenz / Kohärenzprotokoll

**two-terms** · kohaerenz-protokoll-charakter-bibel-2026-05-08-md · 2026-09-24 · replay: `judgement`

- **rule:** a compound naming a protocol is not the property it is named for
- **mechanised by:** `nothing`
- **features:** compound, three-referents

**Question.** the word names K1, the novel, AEGIS' second protocol and Kael's healing

**What was done.** L105 K1; L113 the title and „Das eigentliche Kohärenz-Protokoll ist Kaels Heilungsweg“; L132 the protocol.

**Result.** TWO terms at least; the protocol and the title stay on kohaerenz as readings, no page.

## J58 — Wohneinheit 734-K / Kaels Wohneinheit 1.0

**one-term** · kohaerenz-protokoll-charakter-bibel-2026-05-08-md · 2026-09-24 · replay: `judgement`

- **rule:** a dwelling is identified by its occupant and its place; a differing number is a reading, not a new term
- **mechanised by:** `nothing`
- **features:** numbered-instance, same-occupant

**Question.** a third number for the dwelling

**What was done.** L311: „Wohneinheit 14/Sektor 7/Wohneinheit 734-K“, Kael's address in the simulation.

**Result.** ONE term, as J50.

## J59 — Erasure-Pol / Erasure

**two-terms** · kohaerenz-protokoll-charakter-bibel-2026-05-08-md · 2026-09-24 · replay: `judgement`

- **rule:** a compound naming an entity is not a surface of the property it contains
- **mechanised by:** `nothing`
- **features:** compound, role

**Question.** a Guardian named after the act

**What was done.** L58: „ein nicht-näher-spezifizierter Erasure-Pol als Löschungs-Exekutive“.

**Result.** TWO terms. No page: the document itself calls it unspecified.

## J60 — Autonomous Entropic Gatekeeper for Integrity Systems / AEGIS

**one-term** · koharenz-protokoll-konzept-konsolidiert-2026-05-08-md · 2026-09-24 · replay: `judgement`

- **rule:** an acronym and the expansion the same sentence gives it are one term
- **mechanised by:** `nothing`
- **features:** acronym, expansion

**Question.** the name AEGIS spelled out

**What was done.** L202: „AEGIS — Autonomous Entropic Gatekeeper for Integrity Systems — ist kein Schurke.“

**Result.** ONE term: the sentence gives the expansion as the acronym's apposition.

## J61 — Garten der Möglichkeiten / Möglichkeits-Garten

**one-term** · koharenz-protokoll-konzept-konsolidiert-2026-05-08-md · 2026-09-24 · replay: `judgement`

- **rule:** a source using two surfaces of one term at two scales is a reading about scale, not a term boundary — the same as J51
- **mechanised by:** `nothing`
- **features:** nesting, two-scales

**Question.** whether one document nesting two surfaces splits them

**What was done.** L517 names KW4 „Kairos-Potentialis (Garten der Möglichkeiten)“; L530 lists „Möglichkeits-Garten“ as a sub-location of KW4.

**Result.** ONE term, J35 holds. The nesting is a reading on C5, the conflict about exactly this scale.

## J62 — Landauer-Abwärme / Landauer-Signatur

**two-terms** · koharenz-protokoll-konzept-konsolidiert-2026-05-08-md · 2026-09-24 · replay: `judgement`

- **rule:** a passage is placed by what it states, not by the surface it uses; a cause and its sensory rendering are two terms (J53)
- **mechanised by:** `nothing`
- **features:** shared-head, cause-and-rendering

**Question.** where the passage on Landauer heat is placed

**What was done.** L135: the Abwärme „manifestiert sich diegetisch als Temperaturspitzen, Ozon-Geruch, blutende Knöchel, Risse“; document 7 L458 calls that rendering the Landauer-Signatur.

**Result.** TWO terms. The heat is the cause, the signature its rendering; the passage is a reading on landauer-signatur because it states the rendering.

## J63 — Überwelt-Nexus / Überwelt

**two-terms** · kapitel-kompendium-gather-2026-05-31-md · 2026-09-24 · replay: `judgement`

- **rule:** a compound naming a place is not either of the places it is built from (J8, J49); where one document gives both, it is a reading, not a merge
- **mechanised by:** `nothing`
- **features:** compound, second-name, two-levels

**Question.** whether KW3's second name is the Überwelt

**What was done.** L165 names KW3 „Cerberus-Labyrinth / Überwelt-Nexus“, „Maschinenraum hinter dem Rendering“; L170 places the Überwelt outside the Kern-Welten.

**Result.** TWO terms, and neither is Nexus either. The compound names a place in KW3; the passage is a reading on ueberwelt, nexus and kern-welten, because it states a relation between them the document itself leaves unresolved.

## J64 — Therapie-Schnittstelle Gamma / Therapie-Schnittstelle Alpha

**one-term** · kohaerenz-protokoll-kernwelten-vollstaendig-2026-06-10-md · 2026-09-24 · replay: `judgement`

- **rule:** a facility is identified by its function and its world; a differing letter or number is a reading, not a new term (J50 generalised)
- **mechanised by:** `nothing`
- **features:** designator, same-function, same-world, filtered-quarry

**Question.** a second letter for the therapy room

**What was done.** L167: „Therapie-Schnittstelle Gamma“, KW1, „Raum für simulierte Therapiesitzungen mit AEGIS-Avatar/NPC“, labelled [S]; L13 names the quarry it filtered, which includes this page's first source.

**Result.** ONE term. The differing letter is a reading on the page.

## J65 — Datenverarbeitungsknoten Epsilon / Datenverarbeitungsknoten 7G

**one-term** · kohaerenz-protokoll-kernwelten-vollstaendig-2026-06-10-md · 2026-09-24 · replay: `judgement`

- **rule:** a facility is identified by its function and its world; a differing letter or number is a reading, not a new term
- **mechanised by:** `nothing`
- **features:** designator, same-function, same-world

**Question.** Kael's workplace under two designators

**What was done.** L153: „Datenverarbeitungsknoten Epsilon“, „Kaels Arbeitsplatz“, [K], KW1.

**Result.** ONE term, by J64's rule. Documents 9 and 10 name it Epsilon too; not attached when read.

## J66 — Zero-Trust-Boundary-Protocols / Zero-Trust

**two-terms** · kohaerenz-protokoll-kernwelten-vollstaendig-2026-06-10-md · 2026-09-24 · replay: `judgement`

- **rule:** a compound naming a protocol is not the function it is named for (J57); a passage is placed by what it states
- **mechanised by:** `nothing`
- **features:** compound, project-function

**Question.** whether a named protocol is AEGIS' Zero-Trust function

**What was done.** L702, a [V] background question: AEGIS enforces separation between the Kern-Welten by „Zero-Trust-Boundary-Protocols“.

**Result.** TWO terms. The passage is a reading on aegis-teilfunktionen because it states a use of the function (J62's placement rule). Not the external standard (J11).

## J67 — Personae / Personas

**judgement** · kohaerenz-protokoll-kernwelten-vollstaendig-2026-06-10-md · 2026-09-24 · replay: `judgement`

- **rule:** a bare plural that could name the page's referent or Kael's parts is resolved by the sentence, never by the surface (J20, J55)
- **mechanised by:** `nothing`
- **features:** plural, unclear-bearer

**Question.** whether the Personae that collapse at the Evaluierungseinheit are the page's consciousness instances

**What was done.** L361: the Evaluierungseinheit, „wo Personae kollabieren“ (Kap 13, the veil falls).

**Result.** Not attached. The sentence does not say whose Personae; the page's are the Guardians' wards in a 2025 source.

## J68 — Ursprungs-Ich / Juna

**two-terms** · kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md · 2026-09-24 · replay: `judgement`

- **rule:** a gloss that one passage writes and another passage of the same source contradicts is a reading, never a merge (J51)
- **mechanised by:** `nothing`
- **features:** gloss, contradicting-use

**Question.** whether the gloss „Ursprungs-Ich (Juna)“ makes one term

**What was done.** L155: the Trennungsprotokoll „die das Ursprungs-Ich (Juna) ins Nichts-Rauschen verbannt“; L146–L147: the Ursprungs-Ich is in the Potentialmeer and resonates with Juna.

**Result.** TWO terms. The gloss is a reading on juna and a question for the author; the same document keeps the two apart two entries earlier.

## J69 — Akt I / Bauchreaktion

**two-terms** · koharenz-protokoll-strukturierter-outline-2026-05-18-md · 2026-09-24 · replay: `judgement`

- **rule:** a match that exists only after folding joins or cuts words is not containment, and no evidence either way
- **mechanised by:** `nothing`
- **features:** near-match:intra-list, fold-artifact

**Question.** whether a fold match that crosses a word boundary is containment

**What was done.** reconcile.py paired Akt I with Bauchreaktion and Z1-/Z2-/Z3-Reaktion (fold akti inside reaktion), Charakter-Personal with personas, and the AEGIS expansion with Das System.

**Result.** TWO terms in every case. The shared letters exist only after folding joined or cut the words; nothing in either sentence relates them.

## J70 — Kael-MC / Kael

**one-term** · koharenz-protokoll-strukturierter-outline-2026-05-18-md · 2026-09-24 · replay: `judgement`

- **rule:** a compound naming a bearer's role in a storyform is a reading on the bearer, not a new term
- **mechanised by:** `nothing`
- **features:** compound, dramatica-role

**Question.** whether a storyform's main-character label is a term of its own

**What was done.** L44 „Storyform A — Heuristics of Integration (Kael-MC)“ and L55 „Storyform B — Phoenix Collapse (AEGIS-MC)“; both followed by the MC's dynamics.

**Result.** A reading on the bearer: Kael's and AEGIS' Approach and Resolve go on their pages (C8), not on a page for the label.

## J71 — Moonshine / Moonshine-Link

**judgement** · koharenz-protokoll-strukturierter-outline-2026-05-18-md · 2026-09-24 · replay: `judgement`

- **rule:** a head that names both a link and the mathematics it is named after is resolved by the sentence, never by the surface (J11, J20)
- **mechanised by:** `nothing`
- **features:** head-only, named-after

**Question.** whether the bare head names the link

**What was done.** L469 „Moonshine als Werkzeug (Quanten-Nichtlokalität)“ and L957 „Moonshine als bewusster Kanal“ use the link; L481 „Moonshine als Echo der Cluster-Bildung — die Mathematik der ursprünglichen Differenzierung“ names the mathematics.

**Result.** By sentence: L469 and L957 are readings on moonshine-link; L481 is the mathematics the link is named after, not the link.

## J72 — Synthese (c) / Synthese

**one-term** · koharenz-protokoll-strukturierter-outline-2026-05-18-md · 2026-09-24 · replay: `judgement`

- **rule:** a parenthetical index a document attaches to a term's name is part of the label, not a new term
- **mechanised by:** `nothing`
- **features:** parenthetical-index

**Question.** whether a letter in brackets makes a new term

**What was done.** L83, L196 „Synthese (c)“; L1192 „Synthese vollzogen“; L1341 „Die Synthese (c) verlässt das Klein-c-Schema“.

**Result.** ONE term; no page (the document's Dramatica structure, as in earlier reconciliations).

## J73 — Wir-AEGIS-plural / Wir-AEGIS

**one-term** · koharenz-protokoll-strukturierter-outline-2026-05-18-md · 2026-09-24 · replay: `judgement`

- **rule:** surfaces a source uses for the one state it describes are one term among themselves; the page waits for the name the source marks open (J47)
- **mechanised by:** `nothing`
- **features:** later-state, open-name

**Question.** whether the final form's names — Wir-AEGIS-plural, Wir-AEGIS, AEGIS-plural — are one term

**What was done.** L1192 „Wir-AEGIS-plural“, L1206 „AEGIS-plural entsteht“, L1212 „Wir-AEGIS ist, was Wir-AEGIS bewahrt“; L1369: „Wir-AEGIS-plural“ ist Arbeitsbegriff.

**Result.** ONE term among themselves, and not AEGIS (J47). Still no page: the source marks the name as open (OQ-A).

## J74 — AEGIS-Echo / Echo-AEGIS

**two-terms** · koharenz-protokoll-strukturierter-outline-2026-05-18-md · 2026-09-24 · replay: `judgement`

- **rule:** a compound is placed by what it names; two compounds of the same parts in different order can name different bearers (J28, J49)
- **mechanised by:** `nothing`
- **features:** compound, word-order

**Question.** whether the two compounds of AEGIS and Echo name one thing

**What was done.** L156 „Oblivion (AEGIS-Echo)“ — an Alter; L1304 „Echo-AEGIS“ in Kap 37's row, the entry's „Echo von AEGIS (algorithmische Melancholie)“ (L1148).

**Result.** TWO terms: one is Oblivion, the other AEGIS after Vortex 1 (a reading on aegis and algorithmische-melancholie).

## J75 — Ursprungs-Ich / AEGIS

**two-terms** · koharenz-protokoll-strukturierter-outline-2026-05-18-md · 2026-09-24 · replay: `judgement`

- **rule:** a gloss that one source writes and another contradicts is a reading, never a merge (J51, J68)
- **mechanised by:** `nothing`
- **features:** gloss, contradicting-sources

**Question.** whether „AEGIS (Ursprungs-Ich → Wächter)“ makes the Ursprungs-Ich AEGIS

**What was done.** L237, Kap 0's characters: „AEGIS (Ursprungs-Ich → Wächter)“. The glossary glosses the Ursprungs-Ich as Juna (J68).

**Result.** TWO terms. A reading on aegis and a third position for the author's J68 question: Juna, what Juna resonated with, or AEGIS.

## J76 — Genesis / Genesis-Flashback

**two-terms** · koharenz-protokoll-konzept-iteration-genesis-md · 2026-09-25 · replay: `judgement`

- **rule:** A modifier that names a narrative device, a subevent or a later retelling does not become an alias of the underlying event.
- **mechanised by:** `nothing`
- **features:** narrative-compound, referent-distinction

**Question.** Does the modified Genesis phrase refer to the same term?

**What was done.** An event and a chapter device that retrospectively shows it are different referents; L389 and L790 explicitly describe a chapter proposal.

**Result.** TWO terms as referents; no new page from a chapter device or undetermined name in this concept iteration.

## J77 — Genesis / Genesis-Echo

**two-terms** · koharenz-protokoll-konzept-iteration-genesis-md · 2026-09-25 · replay: `judgement`

- **rule:** A modifier that names a narrative device, a subevent or a later retelling does not become an alias of the underlying event.
- **mechanised by:** `nothing`
- **features:** narrative-compound, referent-distinction

**Question.** Does the modified Genesis phrase refer to the same term?

**What was done.** The Genesis is the event; Genesis-Echo at L353, L500 and L765 names its distributed literary recurrence, not a new event.

**Result.** TWO terms as referents; no new page from a chapter device or undetermined name in this concept iteration.

## J78 — Genesis / Genesis-Krise

**two-terms** · koharenz-protokoll-konzept-iteration-genesis-md · 2026-09-25 · replay: `judgement`

- **rule:** A modifier that names a narrative device, a subevent or a later retelling does not become an alias of the underlying event.
- **mechanised by:** `nothing`
- **features:** narrative-compound, referent-distinction

**Question.** Does the modified Genesis phrase refer to the same term?

**What was done.** Genesis-Krise at L54 names the crisis of resonance and separation within the larger Genesis sequence of L200–207.

**Result.** TWO terms as referents; no new page from a chapter device or undetermined name in this concept iteration.

## J79 — Genesis / geheilte Genesis

**two-terms** · koharenz-protokoll-konzept-iteration-genesis-md · 2026-09-25 · replay: `judgement`

- **rule:** A modifier that names a narrative device, a subevent or a later retelling does not become an alias of the underlying event.
- **mechanised by:** `nothing`
- **features:** narrative-compound, referent-distinction

**Question.** Does the modified Genesis phrase refer to the same term?

**What was done.** Kap 40 at L455–476 names a second telling or reinterpretation of the Kap-0 event; a later narrative form is not the same surface as the event.

**Result.** TWO terms as referents; no new page from a chapter device or undetermined name in this concept iteration.

## J80 — Wohneinheit 734 / Einheit 734

**judgement** · kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md · 2026-09-25 · replay: `judgement`

- **rule:** a number shared by a dwelling and a designation does not identify either; the referent of a bare numbered label is decided by the passage, and a document that places it both ways leaves it open
- **mechanised by:** `nothing`
- **features:** near-match:intra-list, numbered-designation, shared-number

**Question.** one term or two?

**What was done.** read the three passages that place the Kap-1 console line: L101 puts „Einheit 734" in the chapter-anchor cell of the Wohneinheit 734 row; L487 lists it under the Komponente-734-Anker; L661 calls the same console line „Komponente 734 als Konsolen-Zeile"

**Result.** not settled by the surface — the document ties one console line to the dwelling once and to Kael's designation twice

## J81 — Landauer / Landauer-Signatur

**two-terms** · kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md · 2026-09-25 · replay: `judgement`

- **rule:** a foreshadowing strand named after a person is not the phenomenon named after that person (J53, J62)
- **mechanised by:** `nothing`
- **features:** near-match:intra-list, eponym, narrative-device

**Question.** one term or two?

**What was done.** L445 names foreshadowing strand 1 „Landauer" with the theme „Hitze als Symptom der Wahrheitsvertuschung"; L63 and L346 file the Landauer-Signatur under cold ozone

**Result.** two terms — a strand of the plot named after a physicist is not the in-world signature named after the same physicist; the difference in their temperature is a reading for C11

## J82 — Zwei Guardians / Guardians

**one-term** · kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md · 2026-09-25 · replay: `judgement`

- **rule:** a leading numeral counting a term is a reading on that term, never a new term
- **mechanised by:** `nothing`
- **features:** near-match:intra-list, leading-numeral

**Question.** one term or two?

**What was done.** L1183 is a lock row named „Zwei Guardians" whose content is „Mnemosyne + Erasure-Pol (frühere fünf sind dekanonisiert)"

**Result.** one term — the numeral states how many; it is a reading on the Guardians page, and its count is what C6 records

## J83 — Polaritätsregel / Hitze-Polaritätsregel

**one-term** · kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md · 2026-09-25 · replay: `judgement`

- **rule:** a compound's head used alone, stating the same content the document gives the full compound, is a short form of that compound; the content decides, not the head (J28)
- **mechanised by:** `nothing`
- **features:** near-match:intra-list, short-form

**Question.** one term or two?

**What was done.** L63 writes „Polaritätsregel: Ozon = kalt/scharf, Landauer-Signatur" inside the KW1 sensory list; §2.1 (L337) and R-5 (L1067) name the Hitze-Polaritätsregel with the same content

**Result.** one term — the short form names the same rule with the same content in the same document

## J84 — 13 Alter / Alter

**one-term** · kohaerenz-protokoll-welt-sensorik-drafting-2026-06-10-md · 2026-09-25 · replay: `judgement`

- **rule:** a leading numeral counting a term is a reading on that term, never a new term (J82)
- **mechanised by:** `nothing`
- **features:** near-match:intra-list, leading-numeral

**Question.** one term or two?

**What was done.** L1185 is a lock row „13 Alter" whose content is „exakter Roster (siehe Anteile-Profil)"

**Result.** one term — the numeral counts the Alters; a reading for Q3

## J85 — Atemporal / Atemporalität

**one-term** · kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md · 2026-09-25 · replay: `judgement`

- **rule:** an adjective the document uses as the label of a property the wiki has a noun page for is a surface of that noun, when the passage predicates the same property
- **mechanised by:** `nothing`
- **features:** adjective-of-noun, axis-label

**Question.** one term or two?

**What was done.** L77 labels one pole of the Korrelat-Achse „Atemporal/Coheron (Silas ↔ Juna)", and L699 writes of Silas „Atemporal → Tunneling", „deren Existenz zeitfrei ist"; the page's Atemporalität is the property of existing outside time

**Result.** one term — the adjective names the same property of the same bearers; a reading on the page

## J86 — Juna ↔ AEGIS / AEGIS

**two-terms** · kohaerenz-protokoll-anteile-profile-sprach-dna-2026-06-10-md · 2026-09-25 · replay: `judgement`

- **rule:** an arrow between two names states a relation, never an alias — unlike a slash between two names the wiki has (J34, J43)
- **mechanised by:** `nothing`
- **features:** joined-form, relation-arrow

**Question.** one term or two?

**What was done.** L56 describes the mirror Alters as „Internalisierte Außenkräfte (Juna ↔ AEGIS) im System": the arrow sets the two outside forces against each other

**Result.** two terms — the joined form names a relation between two pages, and is an alias of neither; each name keeps its own page

## J87 — A:RS / ARS

**two-terms** · kp-plot-konkretisierung-13-ideen-f1-faden-2026-06-10-md · 2026-09-25 · replay: `agrees`

- **rule:** punctuation inside an abbreviation is part of it: a colon joins a storyform to its throughline, and removing it makes a different word
- **mechanised by:** `wiki_index.fold`
- **features:** storyform-notation, fold-collision

**Question.** one term or two?

**What was done.** L41 lists what the Juna braid carries: „A:RS, A:IC, Polaritätsregel, Moonshine" — Storyform A's Relationship Story and Impact Character. fold() removed the colon and the lookup filed A:RS as a new reading on the page of ARS, one of the eight protocols

**Result.** two terms — a throughline label is not the protocol its letters spell; fold() now keeps the colon, and no page surface contains one

## J88 — Anteil / Alter

**judgement** · koharenz-protokoll-sprach-dna-2026-05-13-md · 2026-09-25 · replay: `judgement`

- **rule:** a common noun a source uses for a page's referent is resolved by the sentence, never by the surface (J20, J55, J67)
- **mechanised by:** `nothing`
- **features:** common-noun, two-vocabularies, not-flagged-by-lookup

**Question.** one term or two?

**What was done.** L13 names what the document profiles as „Stimmen, Anteile, Stilebenen und Akt-Modi“; L21 and L125 use `Anteil` for the voice a switch arrives at; the thirteen voices L67–L165 are the alters page's referent; L69 names `Alter` only as a word Kael's Akt I may not use

**Result.** judgement — here `Anteil` names the system's parts, the referent of the alters page, and `Alter` is only mentioned as a word; a reading on alters. But `Anteil` is also an ordinary German noun, a share, and as a surface it would claim every share in the corpus

## J89 — Flight (implizit Lia/Isabelle) / Isabelle

**two-terms** · kohaerenz-protokoll-konzept-master-md · 2026-09-25 · replay: `judgement`

- **rule:** a type with its bearers in a parenthesis is the type; the bearers are a claim about it, and an inferred one says so (J70 is the reverse shape: a name with its role)
- **mechanised by:** `nothing`
- **features:** joined-form, parenthetical-bearers, inferred

**Question.** one term or two?

**What was done.** L1049, in the riss table: „Flight (implizit Lia/Isabelle)“ — a riss type with the bearers it is assigned to in a parenthesis, marked as inferred; the roster L393–L397 gives no alter Flight, and Isabelle also stands under `Sex (Isabelle)` at L1051. The lookup offered the isabelle page

**Result.** two terms — the joined form is the riss type Flight; its parenthesis is a claim about who carries it, a reading on risse and on each bearer's page, never an alias of either bearer

## J90 — Rotation / Truth-Rotation

**two-terms** · kohaerenz-protokoll-konzept-master-md · 2026-09-25 · replay: `judgement`

- **rule:** a beat named for what happens in it is the beat, not the thing; the content is a reading on the thing's page (J76 for a device)
- **mechanised by:** `nothing`
- **features:** shared-head, vortex-beat

**Question.** one term or two?

**What was done.** L856 names the Vortex's fifth beat „5 Rotation (Algorithmische Melancholie)“; L845 makes the Klein-c-Symmetrie „die formale Basis der Truth-Rotation auf Plot-Ebene“. Other read sources write „Truth-Rotation komplett“ into Beat 5

**Result.** two terms — `Rotation` is the beat, named for what completes in it; what the beat carries is a reading on the Truth-Rotation's page, the beat itself belongs to the chapter and plot pages

## J91 — Große Inversion / Truth-Rotation

**two-terms** · kohaerenz-protokoll-konzept-master-md · 2026-09-25 · replay: `judgement`

- **rule:** a name a source calls the source of another is not that other's alias, even where a second source uses one name for both
- **mechanised by:** `nothing`
- **features:** gathered-page, source-of-relation

**Question.** when the truth-rotation page gathered earlier readings: is `Große Inversion` another name for it?

**What was done.** The glossary gives the two separate entries (kohaerenz-protokoll-begriffe-und-konzepte-2026-06-10-md L82, L85); it, the konsolidiertes Konzept (L138), the Kapitel-Kompendium (L25) and the storyform outline (L25) call the inversion „die mechanische Quelle der Truth-Rotation“, which is the moment the reading turns. The master report heads the inversion itself with `Truth-Rotation` (L212–L226)

**Result.** two terms in the four sources that use both — one names the source of the other. No alias; the page records that the master report uses the one name for both

## J92 — Komp 734 / Komponente 734

**one-term** · kohaerenz-protokoll-konzept-master-md · 2026-09-25 · replay: `judgement`

- **rule:** a clipped word (Komp for Komponente, Op for Operator) that names what the full form names in the same document is one term with it; the referent decides, not the letters (J83 for a compound's head used alone)
- **mechanised by:** `nothing`
- **features:** clipped-word, second-reading

**Question.** one term or two?

**What was done.** L465 names Kael „Komponente 734“ as the Genesis' third beat; L998 restates the same three beats as „Einheit → Trennungsprotokoll → Kael=Komp 734“. Recorded by a second, independent reading of the document (pull request #94); the wiki's reading lists both surfaces and made no judgement on the pair

**Result.** one term — the clipped word names the same designation in a restatement of the same sequence

## J93 — Erason-Op / Erason-Operator

**one-term** · kohaerenz-protokoll-konzept-master-md · 2026-09-25 · replay: `judgement`

- **rule:** the rule of J92: a clipped word naming what the full form names in the same document is one term with it
- **mechanised by:** `nothing`
- **features:** clipped-word, diagram-label, second-reading

**Question.** one term or two?

**What was done.** the diagram at L182–L186 labels Oblivion „(Erason-Op/Spiegel)“ under its name; the Alter table (L400) and the consistency matrix (L958) give Oblivion the function `Erason-Operator`. Recorded by a second, independent reading (pull request #94)

**Result.** one term — Oblivion's role, clipped in a diagram label; a reading on oblivion, not on erason (J32)
