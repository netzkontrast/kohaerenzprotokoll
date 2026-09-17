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

## J46 — Seelen-Kohärenz-Protokoll / Kohärenz

**two-terms** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a project or document title containing a term is not itself an occurrence of that term
- **mechanised by:** `nothing`
- **features:** substring, project-title-vs-concept

**Question.** is the project title the same term as the abstract concept it contains?

**What was done.** Seelen-Kohärenz-Protokoll (L11, L17) names the document/project itself, quoted once as the title of the Überarbeitete Fassung. Kohärenz is used elsewhere (L19) as an abstract psychological property Michael moves toward.

**Result.** TWO terms. A title that contains a word is not a reading of that word.

## J47 — Seele = Information / Seele=Info

**one-term** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a spacing variant of an already-quoted coined phrase is not a term boundary
- **mechanised by:** `nothing`
- **features:** spacing-variant, quoted-every-time

**Question.** is the spaced form a second term?

**What was done.** Both name the same Guardian paradigm; the document itself uses both spellings for the identical referent, always in quotation marks (13 occurrences total).

**Result.** ONE term. New page seele-info, aliasing both spellings.

## J48 — Kohärenz / Datenkohärenz

**two-terms** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a compound with Daten- names the paradigm's narrow technical sense, not the page's abstract concept
- **mechanised by:** `nothing`
- **features:** substring, paradigm-vocabulary

**Question.** is the Guardians' narrow technical target the same as the page's existing concept?

**What was done.** kohaerenz.md already reads Kohärenz as AEGIS' measurable low-entropy property (kohaerenzprotokoll-aegis-und-systementropie). This document uses Kohärenz for what Michael moves toward (L19) and Datenkohärenz for what the Guardians' failed tools target (L275).

**Result.** TWO terms. Datenkohärenz folded into the seele-info vocabulary cluster instead.

## J49 — Kohärenz / Logische Kohärenz-Analysatoren

**two-terms** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a compound tool-name built on a term is not the term
- **mechanised by:** `nothing`
- **features:** substring, tool-name

**Question.** is a named tool the same term as the concept it is named after?

**What was done.** Logische Kohärenz-Analysatoren (L154) is one of four named Guardian tools with its own function and failure mode. Kohärenz is the abstract concept the tool measures against.

**Result.** TWO terms. See guardian-werkzeuge.

## J50 — Kohärenz / Kohärenz-Analysator

**two-terms** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a compound tool-name built on a term is not the term
- **mechanised by:** `nothing`
- **features:** substring, tool-name

**Question.** same as J49 for the compact-compound naming

**What was done.** Kohärenz-Analysator (L344) is the compact form of the same tool J49 covers under its noun-phrase form.

**Result.** TWO terms, same reasoning as J49.

## J51 — Logische Kohärenz-Analysatoren / Kohärenz-Analysator

**one-term** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a noun-phrase naming and a compact-compound naming introduced by the same document as "the same four tools by example" are one term each
- **mechanised by:** `nothing`
- **features:** two-namings-one-document, flagged-while-reading

**Question.** the census's own flagged merge point 1 — one tool named twice

**What was done.** Noun phrase at L151-154 and compact compound at L344 name the same four Guardian tools by example; Kohärenz-Analysator/-Analysatoren is the only pair sharing a substring, the other three pairs share none.

**Result.** ONE term per tool, four tools total. New page guardian-werkzeuge collects all four pairs.

## J52 — Datenintegration / Integration

**two-terms** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a Daten- prefixed compound belongs to the Guardians' paradigm cluster, not to the DID-therapy sense of the bare noun
- **mechanised by:** `nothing`
- **features:** substring, domain-clash

**Question.** is the Guardians' data-goal the same as the DID-therapy phase?

**What was done.** Datenintegration (L19) is what the Guardians' paradigm targets. Integration (L104, L281) names the third DID-therapy phase, alongside funktionale Multiplizität.

**Result.** TWO terms. Datenintegration folds to seele-info; Integration folds to the multiplizitaet reading.

## J53 — Systemwächter / Wächter

**two-terms** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a quoted individual character name is never folded into a collective term sharing its root
- **mechanised by:** `nothing`
- **features:** substring-trap, collective-vs-individual

**Question.** is the collective term for the Guardians the same as one Alter's own name?

**What was done.** Systemwächter/Systemhütern (L23, L29) is this document's German collective term for the Guardians, consistent with the existing Wächter alias on guardians.md. "Wächter" in quotation marks at L116 is a specific Alter's own name (Protector archetype, Welt 3), unrelated to the Guardians.

**Result.** TWO terms. Systemwächter/Systemhütern recorded as an alias reading on guardians.md; the Alter "Wächter" recorded only within the alters.md table reading, not promoted.

## J54 — Architekt / Netzwerkarchitektur

**two-terms** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a shared substring across unrelated compounds is not a term match
- **mechanised by:** `nothing`
- **features:** substring-trap

**Question.** do Architekt and Netzwerkarchitektur share anything but a substring?

**What was done.** Architekt (L26, L31) is a named Persona from Blueprint V5, already on personas.md. Netzwerkarchitektur is a generic compound noun describing a possible visualisation of the Überwelt (L173 area), unrelated in referent.

**Result.** TWO terms, no relation beyond the shared substring.

## J55 — Alters / Alter

**one-term** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a German plural is not a term boundary
- **mechanised by:** `nothing`
- **features:** german-plural, already-a-surface

**Question.** plural vs singular of the page's own term

**What was done.** Census (04-counts.txt) confirms Alter at 12 standalone/86 with compounds, with 55 of the 86 being the inflected Alters this document actually uses; both name the same DID concept the alters.md page already holds.

**Result.** ONE term, matching the corpus rule already applied to Riss/Risse (J45) and Anomalie/Anomalien (J44).

## J56 — Alter / Alter Intrusion

**two-terms** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a compound naming one specific clinical symptom-type is not the general concept its head noun names
- **mechanised by:** `nothing`
- **features:** substring, clinical-compound

**Question.** is a named symptom-type the same as the general concept it is built from?

**What was done.** Alter Intrusion/Switch (L246) is one of four named Riss symptom-types on the risse.md reading. Alter alone is the general DID personality-part concept.

**Result.** TWO terms. Alter Intrusion recorded within the risse.md reading, not promoted separately.

## J57 — Integration / Integrationsversagen

**one-term-family** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a morphological derivative in the same domain is recorded with its root rather than as a separate page
- **mechanised by:** `nothing`
- **features:** morphological-derivative, same-domain

**Question.** is failure-of-integration a separate term from integration?

**What was done.** Integrationsversagen (L109-111) is the DID-therapy sense of failed integration, in the same passage that discusses Integration as the third therapy phase (L104).

**Result.** Folded into the same DID-therapy-process reading on multiplizitaet.md rather than promoted or kept apart; kept apart from the Guardians' Datenintegration per J52.

## J58 — Kernpersönlichkeit / Kern

**two-terms** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a polysemous root that a document's own census separates into unrelated senses is never folded with any one of its compounds
- **mechanised by:** `nothing`
- **features:** polysemous-root, census-flagged

**Question.** the census's own warning: Kern compounds into three unrelated things

**What was done.** Kernpersönlichkeit (L59, L104, L109, L137, L158) is the specific rejected "true self" concept. Bare Kern also means Kernkonzept/Kernthema (document-structuring) and Kerntrauma (a plot beat) in this same document -- three unrelated senses census already separated.

**Result.** TWO terms; bare Kern is not itself promoted (too polysemous within one document to be one candidate).

## J59 — Kern / Kerntrauma

**two-terms** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a polysemous root that a document's own census separates into unrelated senses is never folded with any one of its compounds
- **mechanised by:** `nothing`
- **features:** polysemous-root, census-flagged

**Question.** same warning, the plot-beat sense

**What was done.** Kerntrauma (L282, L303, L363, L365) names a specific plot beat (the confrontation with the core trauma in Teil 3), unrelated to the Kernpersönlichkeit debate.

**Result.** TWO terms, same reasoning as J58.

## J60 — Persecutoren / Persecutor

**one-term** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a German plural is not a term boundary
- **mechanised by:** `nothing`
- **features:** german-plural, borrowed-clinical-term

**Question.** German plural of a borrowed English clinical term

**What was done.** Persecutoren (L73) and Persecutor (L117, L185) name the same DID Alter-role; the -en suffix is the ordinary German plural applied to an imported noun.

**Result.** ONE term, folded into the alters.md table reading, not promoted separately.

## J61 — Kind-Anteile / Kind

**two-terms** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a document's own recurring-archetype label is a reading of its clinical term, not identical to it
- **mechanised by:** `nothing`
- **features:** scope-mismatch

**Question.** is the recurring archetype the same as the clinical group name?

**What was done.** Kind-Anteile (L73, L185) is the DID clinical term for child alters as a group. Kind (L160) is named separately as an "(Optional) Wiederkehrende Archetyp," a broader interpretive lens the document applies on top of Kind-Anteile.

**Result.** TWO terms, both folded into the alters.md reading as supporting vocabulary rather than promoted.

## J62 — Kairos / Kairos/Sophia

**one-term-as-pair** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a slash between two names the wiki already treats as separable Guardians is read per-document, not folded once for the whole corpus
- **mechanised by:** `nothing`
- **features:** slash, never-separated, cross-document-precedent

**Question.** does this document separate Kairos from Sophia, like document 4, or combine them, like document 6?

**What was done.** "Kairos/Sophia (Optimierung/Potenzial - neu interpretiert)" (L141) is this document's only mention of either name, always combined, matching roman-lokalitaeten-konzept-und-ausarbeitung's treatment rather than guardians-und-kern-welten-konzept's separated one.

**Result.** Reading recorded on both kairos.md and sophia.md, each pointing at the combined content rather than duplicating it, consistent with the existing pattern for this pair.

## J63 — Wächter / wachterdersystemischenstabilitat

**not-related** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a shared normalised substring across unrelated compounds from different documents is not a term match
- **mechanised by:** `nothing`
- **features:** fold-false-positive, substring-trap

**Question.** is the fold() near-match to aegis a real relation?

**What was done.** wiki_index.fold normalises to a shared substring with an unrelated AEGIS-cluster surface from another document. This document's "Wächter" is the Alter-table entry (Protector, L116), which does not occur anywhere near an AEGIS context.

**Result.** NOT related. Recorded within the alters.md table reading; no page or link created from the false match.

## J64 — Gatekeeper / entropicgatekeeper

**not-related** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a shared normalised substring across unrelated compounds from different documents is not a term match
- **mechanised by:** `nothing`
- **features:** fold-false-positive, substring-trap

**Question.** is the fold() near-match to aegis a real relation?

**What was done.** This document's "Gatekeeper" (L119, Der Archivar's archetype role) shares a substring with an unrelated "Entropic Gatekeeper" surface from entropie-aegis, an AEGIS-cluster term this document never mentions.

**Result.** NOT related, same reasoning as J63.

## J65 — Depersonalisation / Persona

**not-related** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a shared normalised substring across unrelated compounds is not a term match
- **mechanised by:** `nothing`
- **features:** fold-false-positive, substring-trap

**Question.** does Depersonalisation relate to Personas via the shared substring persona?

**What was done.** "persona" is a substring of "Depersonalisation" purely orthographically; the clinical symptom (L60, L108, L161) and the V5 Personas concept (L31) share no referent.

**Result.** NOT related.

## J66 — Nexuspunkt / Nexus

**two-terms** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a shared root between a role-word and an established place-name is not itself evidence of one referent
- **mechanised by:** `nothing`
- **features:** shared-root, scope-mismatch

**Question.** is Julia's structural role-word the same as the Guardians' meta-space?

**What was done.** Nexus (existing page) is the meta-representational space where Guardians take visual form, from guardians-und-kern-welten-konzept. Nexuspunkt (L237) is one of three near-synonym role-words this document gives Julia for her connection to the externe Ebene.

**Result.** TWO terms. Nexuspunkt recorded on juna.md/externe-ebene.md as part of the three-hypothesis reading, not folded into nexus.md.

## J67 — Systemgrenzen / Systemgrenze

**two-terms** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a generic plural describing a function is not the same term as one document's specific singular named instance
- **mechanised by:** `nothing`
- **features:** generic-vs-specific, cross-document

**Question.** is Cerberus's generic boundary-guarding the same as the one wall named Die Große Mauer (Systemgrenze)?

**What was done.** roman-lokalitaeten-konzept-und-ausarbeitung names one specific wall in KW3, "Die Große Mauer (Systemgrenze)," already on grosse-mauer.md. This document's "Systemgrenzen" (L140, plural) is Cerberus's general domain -- "zwischen Welten, zwischen Alters, zur Überwelt" -- naming no single boundary.

**Result.** TWO terms. Recorded on cerberus.md as a generic function, not folded into grosse-mauer.md.

## J68 — Kern / Kernwelt

**not-related** · kohaerenz-protokoll-konzept · 2026-09-17 · replay: `judgement`

- **rule:** a shared normalised substring across unrelated compounds from different documents is not a term match
- **mechanised by:** `nothing`
- **features:** fold-false-positive, substring-trap

**Question.** does this document's bare Kern relate to the corpus's Kern-Welten term?

**What was done.** This document never writes Kern-Welt or Kernwelt at all -- it numbers Welt 1-4 instead (see kern-welten.md reading). The fold() near-match is a substring coincidence between the polysemous root Kern (J58/J59) and an unrelated corpus term.

**Result.** NOT related.

## J69 — Alters / Alter

**one-term** · charakterkonzepte-fuer-kohaerenz-protokoll · 2026-09-17 · replay: `judgement`

- **rule:** the German singular of a borrowed collective noun names the same concept as the plural the wiki already tracks
- **mechanised by:** `nothing`
- **features:** singular-plural, intra-document

**Question.** does this document's singular Alter name the same concept as the already-tracked plural Alters?

**What was done.** The document uses "Alter" (singular, e.g. L217 "in verschiedene Anteile, sogenannte Alters, fragmentiert", L265 "Kernfunktion/Rolle") and "Alters" (plural/collective, matching the tracked surface) for the same DID concept throughout, declined normally in German.

**Result.** ONE term. Recorded together on alters.md, which already carries the tracked surface "Alters".

## J70 — Alter / Child Alter

**one-term-family** · charakterkonzepte-fuer-kohaerenz-protokoll · 2026-09-17 · replay: `judgement`

- **rule:** a subtype label in the same domain is recorded with its root term rather than as a separate page
- **mechanised by:** `nothing`
- **features:** generic-vs-subtype, intra-document

**Question.** is "Child Alter" a separate term from the generic "Alter" category?

**What was done.** "Child Alter (Little)" (L317) is a DID role-subtype of the generic "Alter" category, used for Echo and Flicker specifically -- the same shape as the existing role-labels Gatekeeper/Protector/Persecutor/Caretaker/Internal Self-Helper.

**Result.** Recorded with its root term on alters.md as clinical-vocabulary, not split into its own page.

## J71 — Alter / Trauma-Halter

**not-related** · charakterkonzepte-fuer-kohaerenz-protokoll · 2026-09-17 · replay: `judgement`

- **rule:** a shared normalised substring across unrelated compounds is not a term match
- **mechanised by:** `nothing`
- **features:** fold-false-positive, substring-trap

**Question.** does the fold() near-match between Alter and Trauma-Halter reflect a real relation?

**What was done.** "Trauma-Halter" (L225, L508 -- Oblivion's specific Freeze-type role) contains "alter" only as a orthographic tail of "-halter" ("holder"); it names a specific character's role, not the generic Alter category.

**Result.** NOT related. Trauma-Halter recorded as Oblivion's role-label on alters.md, not folded with bare Alter.

## J72 — Juna / Junas Fragment

**two-terms** · charakterkonzepte-fuer-kohaerenz-protokoll · 2026-09-17 · replay: `judgement`

- **rule:** a hedged, localised manifestation of a tracked entity is a reading of that entity, not the entity itself and not a new page
- **mechanised by:** `nothing`
- **features:** possessive-derivative, intra-document

**Question.** is Junas Fragment the same referent as Juna, or a distinct manifestation?

**What was done.** "Junas Fragment (Manifestation in einer Kern-Welt)" (L605) is explicitly a partial, localised manifestation of Juna inside one Kern-Welt -- "verletzlicher oder begrenzter als Juna selbst" (L608) -- proposed under the alternate name "Echo / Lichtfunke (oder ähnlich)" (L606), one of the document's eleven hedged Nebencharaktere.

**Result.** TWO terms. Recorded as a reading on juna.md (what a manifestation of her looks like), not folded into Juna nor given its own page -- the document's own hedge ("oder ähnlich") is the same shape document 5's brief carried for every proposed name.

## J73 — Autonomous Entropic Gatekeeper for Integrity Systems / Gatekeeper

**not-related** · charakterkonzepte-fuer-kohaerenz-protokoll · 2026-09-17 · replay: `judgement`

- **rule:** a shared word between an acronym expansion and an unrelated generic role-label is not a term match
- **mechanised by:** `nothing`
- **features:** fold-false-positive, substring-trap, intra-document

**Question.** does the intra-list near-match between the AEGIS acronym and Limina's role-label Gatekeeper reflect a real relation?

**What was done.** The acronym expansion (L118) names AEGIS. "Gatekeeper" (L222, L265, L503) is Limina's DID role-type, an Alter of Kael's -- an unrelated referent that shares the word "Gatekeeper" only because AEGIS's own acronym happens to contain it.

**Result.** NOT related. Gatekeeper recorded on alters.md as Limina's role-label; the acronym recorded on aegis.md.

## J74 — Ashby's Law of Requisite Variety / Requisite Variety

**one-term** · charakterkonzepte-fuer-kohaerenz-protokoll · 2026-09-17 · replay: `judgement`

- **rule:** the short form of one cited external law is the same referent as its full name, and a citation is not promoted to a term page
- **mechanised by:** `nothing`
- **features:** short-form-long-form, intra-document, external-citation

**Question.** are the full and short forms of this cited cybernetic law one term?

**What was done.** L128 states the law in full once ("kybernetischen Prinzipien wie Ashby's Law of Requisite Variety") and the document's Arc-Potenzial section (L146 area) later uses only "requisite variety" for the same cited principle.

**Result.** ONE term -- an external, real-world citation the document uses to argue AEGIS's blind spot, not a corpus-original concept. Recorded as citation vocabulary on aegis.md/seele-info.md, not given its own page.

## J75 — Alter / alters

**one-term** · charakterkonzepte-fuer-kohaerenz-protokoll · 2026-09-17 · replay: `judgement`

- **rule:** the German singular of a borrowed collective noun names the same concept as the plural the wiki already tracks
- **mechanised by:** `nothing`
- **features:** singular-plural, lookup-match

**Question.** does the wiki-lookup near-match between Alter and the tracked alters.md page hold?

**What was done.** Same pair and same reasoning as J69, this time as the lookup (not intra-list) classification.

**Result.** ONE term, confirming J69.

## J76 — Autonomous Entropic Gatekeeper for Integrity Systems / Entropic Gatekeeper

**one-term** · charakterkonzepte-fuer-kohaerenz-protokoll · 2026-09-17 · replay: `judgement`

- **rule:** an independently-supplied expansion identical in wording to an existing reading confirms it rather than adding a new one
- **mechanised by:** `nothing`
- **features:** independent-confirmation, conflict-relevant

**Question.** does this document's acronym expansion (L118) match the tracked entropie-aegis reading on aegis.md?

**What was done.** Compared word-for-word: entropie-aegis.md:L19 gives "AEGIS = Autonomous Entropic Gatekeeper for Integrity Systems"; this document's L118 gives the identical expansion, unprompted, from an unrelated document read eleven days later.

**Result.** ONE term -- an independent confirmation of the first of three incompatible expansions in conflict C1, not a new reading. Recorded on aegis.md as corroboration.

## J77 — Systemkohärenz / Kohärenz

**one-term** · charakterkonzepte-fuer-kohaerenz-protokoll · 2026-09-17 · replay: `judgement`

- **rule:** a "System-" compound of an already-tracked abstract property names the same referent when the usage matches the tracked sense
- **mechanised by:** `nothing`
- **features:** compound-of-tracked-term, lookup-match

**Question.** does AEGIS's "Systemkohärenz" (L137, threatened by Juna) name the same referent as the tracked property on kohaerenz.md?

**What was done.** kohaerenz.md's tracked reading is "a property of a running system... what AEGIS monitors, and what it loses". L137: "Juna... eine fundamentale Bedrohung für die Systemkohärenz" uses the word in exactly that sense -- a system-wide coherence property under threat.

**Result.** ONE term. Reading added to kohaerenz.md.

## J78 — Zero-Trust-Protokolle / Zero-Trust

**one-term** · charakterkonzepte-fuer-kohaerenz-protokoll · 2026-09-17 · replay: `judgement`

- **rule:** the first source to say something substantive about one bundled sub-function triggers that page's own pre-stated split condition
- **mechanised by:** `nothing`
- **features:** lookup-match, page-split-trigger

**Question.** is this document's Zero-Trust-Protokolle the same AEGIS sub-function as the one bundled on aegis-teilfunktionen.md, and does it trigger that page's stated split condition?

**What was done.** L205: "Aufgrund der segmentierten Natur des Systems (Zero-Trust-Protokolle, Kontext Pt 2) haben sie [Guardians] möglicherweise nur begrenztes Bewusstsein voneinander" -- an AEGIS-internal segmentation function, matching aegis-teilfunktionen.md's Zero-Trust sub-function and NOT the external Zero-Trust-Architektur J11 already separated from it.

**Result.** ONE term, and aegis-teilfunktionen.md's own stated rule ("this splits into four pages the moment any source says something about any one of them") now applies: split Zero-Trust into its own page, zero-trust.md, with this reading. Cognitive Firewall, Integrity Guardian and SIS remain bundled -- nothing has been said about them yet.

## J79 — Kohärenz Protokoll / Kohärenz

**two-terms** · charakterkonzepte-fuer-kohaerenz-protokoll · 2026-09-17 · replay: `judgement`

- **rule:** a lookup's near-match is a candidate page, not a verdict -- check the document's actual sense against every tracked reading the substring could mean, not only the one the fold matched
- **mechanised by:** `nothing`
- **features:** lookup-override, scope-mismatch

**Question.** does this document's in-world "Kohärenz Protokoll" (L124) match the near-match the lookup proposed (kohaerenz.md), or a different tracked reading?

**What was done.** L124: "AEGIS wird ausschließlich durch seine Kernprogrammierung, das 'Kohärenz Protokoll', angetrieben" names AEGIS's core programming -- the system itself, not the measurable property kohaerenz.md tracks. That sense already has a home: kohaerenz-programm.md, "the system as a whole", which explicitly keeps `Kohärenz` (property), `Kohärenz-Programm` (the system) and the novel's title apart (J16/J17). Five of this document's seven occurrences of the phrase are its own title/headers and are excluded per that same page's precedent ("not a term of the fiction").

**Result.** NOT the same as kohaerenz.md. Folded instead to kohaerenz-programm.md as a fourth surface confirming the "system itself" reading.

## J80 — Gatekeeper / entropicgatekeeper

**not-related** · charakterkonzepte-fuer-kohaerenz-protokoll · 2026-09-17 · replay: `judgement`

- **rule:** a shared word between an acronym expansion and an unrelated generic role-label is not a term match
- **mechanised by:** `nothing`
- **features:** fold-false-positive, substring-trap, lookup-match

**Question.** does the wiki-lookup near-match between Limina's role-label and aegis.md's tracked alias hold?

**What was done.** Same pair and same reasoning as J73, this time as the lookup (not intra-list) classification -- Limina's generic DID role (L222, L265, L503) against AEGIS's "Entropic Gatekeeper" alias.

**Result.** NOT related, confirming J73.

## J81 — Glitchwyrm / Glitch

**two-terms** · charakterkonzepte-fuer-kohaerenz-protokoll · 2026-09-17 · replay: `judgement`

- **rule:** a named entity that inhabits a tracked phenomenon is not the phenomenon, even when it shares a surface fragment with the phenomenon's alias
- **mechanised by:** `nothing`
- **features:** fold-false-positive, lookup-match

**Question.** is the Nebencharakter "Glitchwyrm" the same term as the Risse alias "Glitch"/"Glitches" tracked on risse.md?

**What was done.** L596: "Name: Leech / Glitchwyrm (oder ähnlich)", "Der Daten-Parasit" -- an entity proposed to feed on Risse ("ernährt sich von den Rissen", L598), not the Risse phenomenon itself. One of the document's eleven hedged Nebencharaktere.

**Result.** TWO terms. A brief mention recorded on risse.md (a proposed creature that inhabits Risse, answering part of that page's own open question), no page for Leech/Glitchwyrm given the same hedge that withheld pages from the other ten Nebencharaktere.

## J82 — Junas Fragment / Juna

**two-terms** · charakterkonzepte-fuer-kohaerenz-protokoll · 2026-09-17 · replay: `judgement`

- **rule:** a hedged, localised manifestation of a tracked entity is a reading of that entity, not the entity itself and not a new page
- **mechanised by:** `nothing`
- **features:** lookup-match, possessive-derivative

**Question.** does the wiki-lookup near-match between Junas Fragment and juna.md hold as identity or as a reading?

**What was done.** Same pair and same reasoning as J72, this time as the lookup (not intra-list) classification.

**Result.** TWO terms, confirming J72 -- recorded as a reading on juna.md.

## J83 — Nyx / Nox

**not-related** · charakterkonzepte-fuer-kohaerenz-protokoll · 2026-09-17 · replay: `judgement`

- **rule:** zero cross-occurrences in either document plus two disjoint named rosters make a one-letter surface resemblance coincidental, not evidence of one character
- **mechanised by:** `nothing`
- **features:** cross-document, one-letter-surface, zero-cross-occurrence

**Question.** does strukturelle-dissoziation-system-kael-analyse's Anteil "Nyx" name the same character as this document's Alter "Nox" (Der Kritiker/Persecutor)?

**What was done.** Word-boundary count: "Nox" occurs 0 times in strukturelle-dissoziation-system-kael-analyse; "Nyx" occurs 0 times in charakterkonzepte-fuer-kohaerenz-protokoll. The two documents name completely disjoint Alter/Anteil rosters (10 names here, 11 there) sharing only Kael/Michael, the host -- not an Alter in either roster.

**Result.** NOT related. fold() correctly keeps them apart; recorded explicitly because the one-letter resemblance is exactly the shape a person, not a lookup, must judge. Feeds the roster conflict raised on alters.md -- see Wiki/conflicts/c6-alter-roster-two-documents.md. Does not reconcile strukturelle-dissoziation-system-kael-analyse, which stays untouched.
