# Graph contracts — what HyperExtract can add to the `ask` graph, and what the graph laboratory found instead

**2026-09-30 · Measured, not adopted.** On the author's requests „Explore Even more hyperextract templates that could and should be used to Improve our Graph in ask.dB" and „Now Read /writing-skills and use that Knowledge to Devise eben more hyperextract templates specific for those use cases", after „maybe you should think about additional hyperextract contracts to help Improve the recall Presion of our Graph rag solutions". Nothing here changes what `graphrag.py` or the store return by default, and one default of `ask.py` changed — the co-mention finder's limit, 40 → 10 paragraphs (§5.4); every other measured change is a parameter that is off, a proposal edge type (`P_HE_*`, never in the core) or a command of `graphlab.py`. What the author has to decide is in §8.

Reading done for this note: the thirteen `writing-skills` and their entry page, `Plan/concept/novel-writing-plan_2026-09-29.md`, `GOAL.md` §4–5, `Plan/concept/hyperextract-templates_2026-09-24.md`, the HyperExtract templates already in `Plan/hyperextract/`, and `Plan/runs/graph-lab-2026-09-30/diagnose.md`. No source document was read for it beyond what the contracts extracted, and every label in §4 and §6.2 was written by the working session, not by the author.

## 0. The answer on one page

1. **What moved recall of the wiki's own labels is not a HyperExtract contract.** Two pages standing in one paragraph in at least two documents, weighted by their normalised pointwise mutual information over documents, and added to the walk of `graphrag.pagerank` as a page–page relation: recall@8 **0.688 → 0.788** at weight 30 (+0.100, 90 % interval [+0.030, +0.177], 6 cases up, 1 down; 0.794 with the statistic squared); leaving each of the 24 cases out and letting the other 23 choose among 96 configurations: **0.760** (+0.072 [−0.007, +0.153]). The cases that move are those with the most gold pages — C4 0.44 → 0.89, C6 0.43 → 1.00, Q5 0.29 → 1.00, Q1, Q3, C5. The same pairs counted, not normalised, **lower** recall by 0.10 to 0.13 (§5.2). **A second label set, the wiki's own links (91 pages, 1,011 gold), says the direction holds and the size does not:** +0.032 [+0.012, +0.052] at weight 3, a third of the first; the weights that gave +0.06 to +0.11 on the conflicts are worth nothing or lose there, and the raw count does as well as the normalised one (§5.2b). Whether to turn it on, and at what weight, is the author's (§8, question 1).
2. **Re-weighting the stated relation types moves nothing.** Uniform, learned and cross-validated weights all score within 0.006 of the default; `links` alone carries what recall there is (§5.1). A correction for hubs lowers recall when chosen leaving one out (−0.041 [−0.082, −0.005]) and a seed-specificity weight lowers it too (§5.3).
3. **The contracts are worth their price where they read structure, and not where they read theory as a set of relations.** On 297 records a reader labelled, a contract that classifies the line under a heading — `ChapterBeats`, `StructureBeats`, `ChapterCards`, `CardFields`, `ProseRules`, `EntityFacts` — was right 86–100 % of the time; `TermDefinitions` 73 % (26 rows), `TermContrasts` 70 % (27), `CausalLinks` 61 % (18); `AliasPairs` 40 %, `Anchors` 20 %, `Precedence` 17 % (§4.2). The three contracts of the scaled pass fell when they left the pilot's documents — 79 → 67 %, 80 → 58 %, 83 → 50 % — and **not one of the 36 rows labelled on the twelve documents was wrong**; 15 were near (`part`), where the pilot's 35 rows of the same three contracts had 6 and one wrong (§6.2). Two cheap rules in code, not in the prompt, lift the weakest families: an alias without an alias word and an order without an order word are not admitted.
4. **The gate that stages a candidate refused right rows, for three reasons the pilot exposed.** Of 263 rows refused only because a slot was not verbatim in the document, 70 named a figure of under four characters (`Lex`, `Nyx`, `Lia`, `KW1`) — `quotes.parts_of` drops fragments that short, so no three-letter name could ever be found — and 68 carried the word the `Utterances` contract itself tells the model to write when a line has no speaker. Both are fixed in the gate; the other 125 are the model's own wording of a clause or an inflection, and now enter the store on their quotation alone (§4.1).
5. **The contracts move retrieval where they have read the documents that hold the gold, and nowhere else the bench can see.** On the pilot's eight documents (76 of the bench's 1,226 gold lines) the contracts' lines changed document recall by −0.007. After three contracts read twelve more documents (493 gold lines, $11.68), adding their lines to the `ask` pack gives **+0.029 [+0.011, +0.049]** with 40 lines, seven of the 24 cases up and none down, and +0.008 line recall (§5.4, §6) — about what `parallel` contributes (0.034) and less than `graph-evidence` (0.079) or `bm25-lines` (0.129), on documents chosen for holding the gold, so an upper bound — and five more of those documents, read afterwards ($11.44, a pass stopped at 14 runs, §6.5), left it at +0.029: the gain is capped by the finder's 40 lines and its seeds, not by what the contracts have read. Their page pairs still cannot move the 24 cases (§5.5), and move the 91 link cases by +0.012 to +0.021 (§5.2b).
6. **The `ask` finders were measured too**: `bm25-lines` (−0.129 without it) and `graph-evidence` (−0.079) earn their place; `entity-unread` is inert on this bench; the co-mention finder as built *lowered* document recall, and limited to ten paragraphs it adds +0.011 (§5.4).
7. **The cue gate saves nothing per line.** A gated `CausalLinks` run on three German documents found 26 % of the lines an ungated run finds for 29 % of the cost, where a repeat of the ungated run finds 88 %: the gate thins the yield in proportion and does not filter it (§4.6). The corpus price stands.
8. **What to do**: §7 orders it. What needs the author's word first is the co-mention relation in the default walk (§8, question 1), the price of a contract pass — about $190 a contract for the whole corpus, not the $63 this note first said (§4.5) — and the contracts' lines in the default pack (§8, question 4).

## 1. The question, and what the laboratory said before any contract was designed

The author asked for a graph enriched with useful information, for experiments including treating every relation the same, and for relation types that rank differently in a mix — using what a HyperExtract-enriched graph can capture. `Plan/runs/graph-lab-2026-09-30/diagnose.md` gave the starting point: over the 24 labelled cases (the wiki's conflicts and questions, each retrieving the pages that raised or contest it, with the case's own node removed), **96 gold pages: 48 hit, 39 reached and outranked, 0 unreachable, 9 with no seed** because the question names no page's surface (49 and 38 at the first run, before documents 55–58). The outranked pages are one hop from a seed and stand at rank 10 to 86 (`did`: rank 26, `realitaetsebenen`: rank 50); the ones that outrank them are hubs (`aegis`, `juna`, `kael`, `vortex`).

That says what would help: a relation that puts a seed *closer to specific pages than to hubs*, and a name that reaches a page the question spells differently. It does not say weights help, and §5.1 confirms they do not.

## 2. What was built

| piece | what it is | where |
|---|---|---|
| **32 contracts** | HyperExtract templates, each a reading rule in the template's own guideline, each carrying `provisional`, `may not` and `retire when`, each with a fixture the offline check runs. 5 were on main; 27 are new — three written for the first trial, 11 derived from the diagnosis and the stated graph's gaps and 13 from the writing skills | `Plan/hyperextract/*.yaml`, `fixtures/` |
| **the staging gate** | a candidate's quotation must be placed on one line by code and every name must stand in the document; a name of under four characters now stands as a word on its own, and the word `unlabelled` (a contract's word for „no speaker") needs no line | `scripts/reading_extract.py` |
| **`hegraph.py`** | loads staged rows into the store as `P_HE_<KIND>` edges, grades them by code, reports what each contract yielded, and gates a document so a run sends only the paragraphs that hold a contract's cue | `scripts/hegraph.py` |
| **two footings** | a row enters on *names* (every name the model wrote stands in the document) or on its *quotation* alone (a slot is the model's own wording, the line is placed, and the pages in the line are found by code, never by the slot) | `hegraph.staged` |
| **contract nodes** | every admitted row is an edge from its line to `he:<KIND>`, so „lines a contract read" needs no page; a row's names or its quotation add edges to the pages and entities they contain | `askdb.collect` |
| **a finder, off** | `he-lines`: lines a contract read that concern the question's seeds, by the contract's own edge or by the line's `MENTIONS` | `ask.py` (`--with he-lines`) |
| **the laboratory** | `graphlab.py`: 24 cases and a second set of 91 (the wiki's own links), six experiments, paired comparison with a 90 % interval and leave-one-out choice | `scripts/graphlab.py` |

The design choices that follow from the repository's rules: a contract may not carry a page's name in its own text (procedural knowledge only, `templates.py check`); a row keeps the model, run and template that produced it, so a wrong template is one `git log` away; **a proposal never enters the core** (`P_` relation types are excluded from the ranking, the paths and the communities by name); and no finder filters on a grade that was not shown to predict anything (§4.3).

## 3. The catalogue

Thirty-two contracts in four families. The *derived from* column names the artefact that asks for the record; *documents* counts the documents a contract ran on — the pilot's eight (§4) and, for `TermDefinitions`, `TermContrasts` and `CausalLinks`, the twelve of §6 as well. „Ok" and „ok+part" are the share of labelled rows a reader marked right, and right or near; the number of labelled rows is before them.

<!--CATALOGUE-->
| family | contract | relation | derived from | documents | rows: names / quote | labelled | ok / ok+part |
|---|---|---|---|---|---|---|---|
| terms | `TermReadings` | `P_HE_READING` | the notes: what a document says about a term, with its line (#124) | 1 | 66 / 4 |  |  |
|  | `TermDefinitions` | `P_HE_DEFINES` | „what is X“ is best answered by the sentence that defines X; `TermReadings` ranks a definition no higher than a remark | 18 | 2004 / 29 | 26 | 73% / 96% |
|  | `TermContrasts` | `P_HE_CONTRAST` | the author's reading of „Große Stille“ against „das große Schweigen“ as a tension, found by a BM25 relation | 18 | 2197 / 140 | 27 | 70% / 100% |
|  | `AliasPairs` | `P_HE_ALIAS` | diagnosis: 9 of 96 gold pages have no seed because the question names a page under a name no page carries | 1 | 32 / 11 | 15 | 40% / 67% |
|  | `Analogies` | `P_HE_ANALOGY` | the census's `lens` sections: a fictional term and the real concept the document says it corresponds to | 2 | 16 / 2 | 15 | 47% / 80% |
|  | `TermTaxonomy` | `P_HE_TAXON` | diagnosis: `[[links]]` are untyped, so a class and its member cannot be told apart | 1 | 7 / 1 | 7 | 43% / 43% |
|  | `StatedRelations` | `P_HE_REL` | #124's comparison of graph tools: nodes and edges a document states | 0 | not run |  |  |
|  | `RelationReadings` | `P_HE_REL` | `StatedRelations` that keeps hedges and questions | 0 | not run |  |  |
|  | `TermCensus` | `P_HE_CENSUS` | the reader's candidate lists | 0 | not run |  |  |
|  | `LocationRegistry` | `P_HE_LOCATION` | document 6's master table of places | 0 | not run |  |  |
| claims and sources | `CausalLinks` | `P_HE_CAUSAL` | the plot model as checkable rules; „why does X happen“ has no stated relation | 17 | 1041 / 410 | 18 | 61% / 100% |
|  | `Rules` | `P_HE_RULE` | GOAL: the plot model as checkable rules; the §5.4 rule table | 2 | 21 / 10 | 11 | 18% / 100% |
|  | `Quantities` | `P_HE_QUANT` | the number 734 and the 39 or 40 chapters: a number is no term | 1 | found nothing |  |  |
|  | `Attributions` | `P_HE_SAYS` | the reader lab: voice was the defect no check saw — what a line reports, not what the document says | 1 | found nothing |  |  |
|  | `StandingClaims` | `P_HE_STANDING` | GOAL: sources tiered by precedence; what a document says of its own standing | 2 | found nothing |  |  |
|  | `OpenPoints` | `P_HE_OPEN` | GOAL: self-generated questions; what a document itself leaves open | 1 | 3 / 0 | 3 | 33% / 67% |
|  | `Locks` | `P_HE_LOCK` | GOAL §4.2 claim schema `lock`; the C11 case | 1 | found nothing |  |  |
| plot and chapters | `ChapterCards` | `P_HE_CHAPTER` | plan Phase 2b: one treatment paragraph per movement — who, want, obstacle, hooks | 1 | 36 / 31 | 15 | 87% / 100% |
|  | `ChapterBeats` | `P_HE_BEAT` | decision 013: the chapter is a unit; 98 chapter mentions have no reading yet | 1 | 32 / 10 | 15 | 93% / 100% |
|  | `StructureBeats` | `P_HE_STRUCT` | developmental-editor's structure criteria; GOAL §5.1 | 1 | 11 / 17 | 12 | 100% / 100% |
|  | `Storypoints` | `P_HE_STORYPOINT` | GOAL §4.3 `Storypoint`, `Throughline`, the dual storyform | 1 | 11 / 10 | 11 | 36% / 100% |
|  | `Precedence` | `P_HE_BEFORE` | no ordering relation in the stated graph | 1 | 33 / 5 | 12 | 17% / 33% |
|  | `Anchors` | `P_HE_ANCHOR` | plan Phase 2c anchors ledger; GOAL §4.3 `Anchor`, `ForeshadowStrand` | 2 | 20 / 20 | 30 | 20% / 70% |
|  | `ThemeMotifs` | `P_HE_THEME` | developmental-editor's spine; workshop-critique's reading of what a piece is about | 1 | 4 / 4 | 4 | 75% / 100% |
|  | `Pitch` | `P_HE_PITCH` | developmental intake; agent-first-pages | 1 | found nothing |  |  |
| cast and voice | `CastRoles` | `P_HE_ROLE` | character pages and storyform documents assign figures to roles | 1 | 15 / 9 | 12 | 58% / 100% |
|  | `CardFields` | `P_HE_CARD` | character-card-builder, reverse-character-cards; the plan's cast ledger | 1 | 39 / 23 | 14 | 86% / 100% |
|  | `EntityFacts` | `P_HE_FACT` | continuity-editor's style sheet | 1 | 60 / 7 | 10 | 90% / 100% |
|  | `Knowledge` | `P_HE_KNOWS` | the plan's reader-knowledge ledger; GOAL §4.3 `ReaderKnowledgeState` | 1 | 2 / 10 | 12 | 25% / 100% |
|  | `ProseRules` | `P_HE_PROSERULE` | the plan's rulebook (Phase 2d); GOAL §5.4 | 1 | 50 / 7 | 11 | 91% / 100% |
|  | `DiegeticTerms` | `P_HE_DIEGETIC` | GOAL §4.3 `DiegeticTerm`: theory shows as image, space or behaviour | 1 | 5 / 0 | 5 | 20% / 100% |
|  | `Utterances` | `P_HE_UTTERANCE` | dialogue-gym voice drills; the character card's voice field | 2 | 3 / 68 | 12 | 58% / 100% |
<!--/CATALOGUE-->

The thirteen derived from the writing skills are the ones that read what the plan's ledgers hold. The plan (`novel-writing-plan_2026-09-29.md`, Phase 2) keeps three ledgers — anchors (planted, echoed, paid), reader knowledge per act, cast — a rulebook of prose rules with a lock and a check kind, and one treatment paragraph per movement; GOAL §4.2 defines a claim with a status, a lock and a tier, §4.3 the ontology (`Anchor`, `DiegeticTerm`, `Storypoint`, `ReaderKnowledgeState`, `Throughline`), §5.4 the rule table. A contract per artefact lets the graph carry, with a line, what a person would otherwise collect by hand; none of them writes or rewrites the author's prose (the writing skills' one rule), and none decides what the book should do.

## 4. The pilot

Eight documents, chosen to give each contract a document of its kind: a foreshadowing plan, a chapter outline, a style guide, a theory document in English, a storyform document, a narrative text, a briefing and the world-concept synthesis. Thirty-seven runs, 313 calls, **$3.70**, Haiku through `claude -p` (decision 011), one run at a time. Each run staged into `Plan/runs/<document>/hyperextract/<contract>-haiku-2026-09-30/`; `yield.md` in `Plan/runs/hyperextract-templates-2026-09-30/` is the report `hegraph.py report` writes. A reader (the working session) labelled 261 rows from the quotation and its line: 150 `ok` (the quotation states what the record says), 80 `part`, 31 `wrong`. The pass of §6 added 36 more (21 `ok`, 15 `part`, none `wrong`): 297 in all, and the tables below count all of them.

### 4.1 What the gate refused that was right

Of 263 rows refused only for `surface absent from document`, with the quotation placed on one line:

| why the slot was not found | rows | now |
|---|---|---|
| a name of under four characters (`Lex`, `Nyx`, `Lia`, `KW1`, `KW`) | 70 | **stands** — the gate accepts a name of under four characters when it is a word on its own on some line |
| the word `unlabelled`, which `Utterances` tells the model to write when the text tags no speaker | 68 | **stands** — a contract's word for no name needs no line |
| a clause of more than three words, the model's own wording | 99 | enters on its quotation |
| a name inflected or reworded (`Isabellas`, `innere Barrieren`) | 26 | enters on its quotation |

The first is a defect of a rule written for quotations. `quotes.parts_of` drops fragments under four characters because a three-character quotation matches everything; a *name* is not a quotation, and the cast — `Lex`, `Nyx`, `Lia` — is exactly what a fielded contract wants. It affected `TermReadings` as well, which the earlier live pass could not have shown: its census names were longer. `stands()` in `reading_extract.py` judges a name of four characters or more as it always was, so no row a stage accepted changes; three cases in its selftest hold it (25 of 25).

The rows that enter on their quotation are labelled too: of 67 such rows a reader marked, `CausalLinks` 78 % ok (9 rows), `CardFields` 100 % (4), `Utterances` 44 % ok and all `ok+part` (9), `Knowledge` 30 % ok (10), `Anchors` 20 % ok (20). Within a contract the two footings show no consistent difference — `CausalLinks` is 44 % ok on names (9) and 78 % on quotation, `TermContrasts` 75 % (24) and 33 % (3) — so the footing does not lower a contract's precision; the contract does.

### 4.2 Precision by contract

<!--PRECISION-->
| contract | labelled | ok | part | wrong | ok share, 90 % interval | ok + part | on the scaled documents: labelled, ok |
|---|---|---|---|---|---|---|---|
| `StructureBeats` | 12 | 12 | 0 | 0 | 100% [82%, 100%] | 100% |  |
| `ChapterBeats` | 15 | 14 | 1 | 0 | 93% [75%, 98%] | 100% |  |
| `ProseRules` | 11 | 10 | 1 | 0 | 91% [68%, 98%] | 100% |  |
| `EntityFacts` | 10 | 9 | 1 | 0 | 90% [65%, 98%] | 100% |  |
| `ChapterCards` | 15 | 13 | 2 | 0 | 87% [67%, 95%] | 100% |  |
| `CardFields` | 14 | 12 | 2 | 0 | 86% [65%, 95%] | 100% |  |
| `ThemeMotifs` | 4 | 3 | 1 | 0 | 75% [36%, 94%] | 100% |  |
| `TermDefinitions` | 26 | 19 | 6 | 1 | 73% [57%, 85%] | 96% | 12, 67% |
| `TermContrasts` | 27 | 19 | 8 | 0 | 70% [55%, 82%] | 100% | 12, 58% |
| `CausalLinks` | 18 | 11 | 7 | 0 | 61% [42%, 77%] | 100% | 12, 50% |
| `CastRoles` | 12 | 7 | 5 | 0 | 58% [36%, 78%] | 100% |  |
| `Utterances` | 12 | 7 | 5 | 0 | 58% [36%, 78%] | 100% |  |
| `Analogies` | 15 | 7 | 5 | 3 | 47% [28%, 67%] | 80% |  |
| `TermTaxonomy` | 7 | 3 | 0 | 4 | 43% [19%, 71%] | 43% |  |
| `AliasPairs` | 15 | 6 | 4 | 5 | 40% [22%, 61%] | 67% |  |
| `Storypoints` | 11 | 4 | 7 | 0 | 36% [18%, 61%] | 100% |  |
| `OpenPoints` | 3 | 1 | 1 | 1 | 33% [8%, 75%] | 67% |  |
| `Knowledge` | 12 | 3 | 9 | 0 | 25% [10%, 49%] | 100% |  |
| `Anchors` | 30 | 6 | 15 | 9 | 20% [11%, 34%] | 70% |  |
| `DiegeticTerms` | 5 | 1 | 4 | 0 | 20% [5%, 56%] | 100% |  |
| `Rules` | 11 | 2 | 9 | 0 | 18% [6%, 43%] | 100% |  |
| `Precedence` | 12 | 2 | 2 | 8 | 17% [6%, 40%] | 33% |  |
<!--/PRECISION-->

Read it by family:

- **Contracts that classify a line under a heading** are right about the line and weak about the name: `ChapterBeats` 93 % ok, `StructureBeats` 100 %, `ChapterCards` 87 %, `CardFields` 86 %, `ProseRules` 91 %, `EntityFacts` 90 %. A card field's figure is the *heading* above the bullet (`Lex`, `Argus`), so it is written nowhere on the line; a chapter beat's chapter is a numbered, bolded heading that names no chapter number. Names for these come from the store, not from the model: the line's own `MENTIONS`, and the contract's edge to a page when the model named the figure. That is why `he-lines` joins two ways (§2).
- **Contracts that relate two names in a sentence** depend on the document. `TermContrasts` (70 % ok over 27 rows) and `TermDefinitions` (73 % over 26) hold on theory prose, and were 80 % and 79 % on the pilot's documents alone. `AliasPairs` failed in one recurring way — a slash list („Kael/Juna") read as a pair, a copula („Autopoiesis ist ein Funktionsprinzip") as an alias, a management sentence as `role_of` — and the rule the prompt already had („a role is not an alias") did not stop it. `Precedence` inferred an order from the adjacency of list items in 8 of 11 rows. A prompt rule that a Haiku reader ignored 8 times in 11 is not a rule; the repository's own lesson about readers applies: **what is not checked in code is not done.**
- **Contracts that carry a proposition** (`Knowledge`, `Rules`, `Anchors`, `ThemeMotifs`, `OpenPoints`) mostly return the sentence right and the *type* wrong: a premise typed `must_not`, a beat typed `plants`, a fear typed `cannot_yet_know`. Their records are good evidence that the line is *about* the thing and poor evidence of the relation the type names.
- **Contracts that found nothing** are informative: `Locks`, `Quantities`, `Attributions`, `StandingClaims` and `Pitch` answered every call and returned an empty list on the documents they were tried on — a theory document holds no lock, a briefing no standing claim. `reading_extract` refuses an empty list because HyperExtract can swallow a schema error into one; `hegraph report` tells the two apart by the calls' own record (`failed_calls` 0 and a reply of a few tokens), and counts them as „answered, found nothing", never as a failure and never as a yield of zero.

### 4.3 The grade does not predict, and two cues do

`hegraph.quality` grades a row 2 when a cue word of the contract and every name stand in the quotation, 1 when one of the two does, 0 when neither. It was meant as a filter. Against the labels: grade 0, 57 % ok (162 rows); grade 1, 54 % (104); grade 2, 71 % (31) — over the 199 rows of the pilot that entered on names, before the quotation footing was counted and before the scaled pass, 64 %, 52 % and 79 %. It does not separate. The reason is family two: a list item under a heading is right with no cue word and no name in its quotation.

Inside three contracts the cue does: an alias with an alias word was `ok` 5 times in 7 and without one 0 in 7; an order with an order word 2 in 2 and without one 0 in 9; a contrast with a contrast word 7 in 8 and without one 4 in 6. Two of them are now a rule in code, `hegraph.CUE_REQUIRED = {"ALIAS", "BEFORE"}`, provisional on seven and nine rows and to be retired when a larger labelled sample says the cue does not matter. **No finder filters on the grade** (`Store.he_lines(min_quality=0)`), and the report prints the table so that a later sample can turn it on.

### 4.4 Agreement with what the pages cite

A term page quotes the lines a reader chose. Of the lines a contract found, the share some page also quotes, and of the lines the pages quote in the documents the contract ran on, the share it found:

| document | contracts | lines the pages cite | found by any contract | of them |
|---|---|---|---|---|
| `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik` | 11 | 20 | 20 | 16 (80 %) |
| `koharenz-protokoll-sprach-dna-2026-05-13-md` | 5 | 52 | 29 | 27 (52 %) |
| `kp-kap25-2026-09-14-md` | 1 (`Utterances`) | 56 | 41 | 12 (21 %) |
| `dual-storyform-hintergruende-md` | 1 (`Storypoints`) | 84 | 20 | 13 (15 %) |

On the style guide `CardFields`, `ProseRules` and `EntityFacts` each found 94–100 % of *their* lines among the lines a page quotes, and together with two more contracts 52 % of what the pages quote. The contracts choose lines a careful reader also chose; each finds a slice. For the four documents no page cites (the synthesis, the outline, the English theory document, the briefing) they find lines nobody has read onto a page: that is the routing value of a pre-reading, not a precision.

### 4.5 What it costs

Measured over the 71 runs of the pilot and the scaled pass (§6), every call counted, failed ones included: **$0.0121 a call and one call for every 1.6 KB of the document**, so **about $7.3 for every megabyte one contract reads once**. The pilot's runs came to $8.05 a megabyte and the scaled pass's to $7.28; by single run the figure runs from $6.4 to $14.5, the dearest being the shortest documents and the chapter outline ($10–12 for `ChapterBeats` and `ChapterCards`). The 586 landed documents are 26.5 MB, so **a contract costs about $190 for the whole corpus**, and by category:

| category | documents | MB | per contract |
|---|---|---|---|
| plot outlines | 218 | 9.0 | $66 |
| concept documents | 80 | 3.6 | $26 |
| psychology theories | 43 | 2.5 | $18 |
| physics | 37 | 1.9 | $14 |
| characters | 37 | 1.7 | $12 |
| AEGIS | 38 | 1.6 | $12 |
| storyform | 34 | 1.5 | $11 |
| worldbuilding, logic | 22 + 24 | 1.3 + 1.3 | $9 each |
| mathematics | 19 | 1.1 | $8 |
| philosophy, audits, genre | 17 + 15 + 2 | 0.6 + 0.4 + 0.1 | $5, $3, $1 |

**This corrects the first version of this section, which said about $63 a contract.** It took „about 4.7 KB of text a call" and $0.0115 a call, and the ledgers do not hold the 4.7 KB: they say 1.6. The sentence contradicted its own example — $0.19 for the 28 KB storyform document is $6.8 a megabyte, which is $180 for the corpus — and was found only when the scaled pass's 957 calls were summed against the 0.53 MB they read. A contract that reads outlines has no use on a physics paper, so the run is *by category*; and `hegraph.gate` keeps only the paragraphs that hold a contract's cue words (with their neighbours), which neither pass used and which, measured on `CausalLinks`, cuts the cost and the yield alike (§4.6).

### 4.6 What the cue gate saves — measured: nothing per line

`hegraph.gate` keeps the paragraphs whose words hold a cue of the contract, with their neighbours, so that a run sends the model less. Mean share of a document sent, over five German documents (a chapter outline, a style guide, a narrative text and two concept documents). An English document is not gated: the cues are German, and the gate would keep a tenth of it and call the rest empty — a selftest holds that.

| contract | share sent | contract | share sent |
|---|---|---|---|
| `TermDefinitions` | 97 % | `Attributions` | 37 % |
| `Quantities` | 92 % | `OpenPoints`, `CausalLinks` | 38 % |
| `AliasPairs` | 75 % | `Knowledge` | 34 % |
| `Utterances` | 73 % | `ChapterBeats` (86 % on an outline, 1–29 % elsewhere) | 26 % |
| `ProseRules` | 71 % | `Locks`, `StandingClaims` | 16 % |
| `Rules` | 70 % | `Anchors` | 48 % |
| `Precedence` | 62 % | `TermContrasts` | 45 % |

The shares said the gate might pay for the claim contracts, and the pilot left it unwired until "a gated run is shown to find what an ungated one finds". **`gate-ab.sh` measured it for `CausalLinks`**, on three German documents of the twelve: each run once more ungated (U2, to see what a repeat does to itself) and once gated (G), $1.42 and 117 calls, against the first ungated run of the scaled pass (U1). The gate sent 26 % of the text (`gate-ab.md`):

| run | rows | lines | recall of U1's lines | of its own lines in U1 | gold lines | calls | cost |
|---|---|---|---|---|---|---|---|
| U1, ungated | 267 | 202 | — | — | 47 | 91 | $1.11 |
| U2, ungated again | 261 | 197 | 88 % | 90 % | 48 | 91 | $1.11 |
| G, gated | 78 | 59 | **26 %** | 90 % | 16 | 26 | $0.32 |

A repeat reproduces 88 % of the first run, so the gated run's 26 % is the gate's doing and not the model's noise. G loses three lines in four and invents none (90 % of its lines are in U1) — and finds the lines it does find at the price the ungated run does, $0.0054 a line against $0.0055: **the gate is a thinning and not a filter.** It finds 16 of the 47 gold lines U1 found and none U1 had not; the repeat finds 48, eight of them new. Offline against U1's rows (`gate-offline.py`, no model) the cue's own paragraphs are dense — 71 % of them hold a row, against 24 % of all paragraphs — but the two neighbours dilute them: 15 % of the text with no neighbour reaches at most 26 % of the lines, 27 % with one neighbour 37 %, 38 % with two 45 %; a wider cue (`durch`, `indem`, `sodass`, `damit`, …) reaches 53 % of the lines from 41 % of the text and 70 % from 60 %. The model finds causal rows through the theory sections and not through the connectives. **So the gate is not wired into `he_claude.py run`, and for `CausalLinks` it should not be**; `StandingClaims`, `Locks`, `Knowledge`, `OpenPoints` and `Attributions` found nothing or little on the pilot's documents, and their gate is untested. A cheaper pass is a pass over fewer documents, at the same price a line.

## 5. Retrieval, measured

Every number below is a row of `Plan/runs/baselines.jsonl`, so `baseline.py compare` reads it; every table is in `Plan/runs/graph-lab-2026-09-30/`. **The tables are of the wiki as this branch leaves it** — 58 documents with a census, 106 pages, the 24 labelled cases (the records of documents 56 and 57 added entries to C2, Q3 and Q8) and, for the finders, a store that holds the scaled contract pass. `rerun.sh` measured everything again after the pass; `first-run/` keeps the first tables, made while the wiki was smaller, and where a number moved both are given. The task is the wiki's own labels — the same hand that wrote the pages wrote them — so what a number can say is which mix does better on this hand's labels, never that a mix is right. §5.2b adds a second, larger label set for the one effect that was found.

### 5.1 E1 — the seven stated relation types

| configuration | recall@8 | vs the default: mean, 90 % interval |
|---|---|---|
| default weights | 0.688 | — |
| uniform: every type 1.0 | 0.688 | +0.000 [+0.000, +0.000] |
| only `links` | 0.681 | −0.008 [−0.051, +0.032] |
| learned on all 24 (in sample) | 0.694 | +0.006 [+0.000, +0.018] |
| learned, 6-fold cross-validated | 0.694 | +0.006 [+0.000, +0.018] |
| seeds alone, no walk | 0.531 | −0.158 [−0.245, −0.079] |

Treating everything the same is as good as tuning: uniform weights equal the default to three decimals, and weights fitted on 23 cases and scored on the 24th gain one case. `links` carries the recall — the default without it falls by 0.079 [−0.158, −0.023] — and the other six types add nothing a paired comparison can see. The learned weights differ from the default by grid steps and are equal across the folds for five of seven types. (The first run, on the wiki before the readings of documents 52–54, read 0.694 for the default and −0.006 for uniform weights; the conclusion did not change.)

### 5.2 E2 and E2b — relations the corpus adds

Derived from the shared store — `MENTIONS` of a page's surface on a line, grouped by paragraph and document — and never from the labels. Each set is added to every case's graph as a page–page relation beside the stated ones.

| relation | scale | best weight | recall@8 | vs the floor |
|---|---|---|---|---|
| learned co-occurrence sets (`askextract`) | lift, capped | 10 | 0.758 | +0.069 [−0.020, +0.160], 6 up / 4 down |
| co-mention, every pair in ≥2 documents | count of documents | 3 | 0.576 | **−0.113** [−0.196, −0.041] |
| co-mention, every pair in ≥2 documents | log of the count | 3 | 0.556 | **−0.133** [−0.219, −0.058] |
| co-mention, ≥2 documents | **normalised PMI** | 10 | 0.774 | **+0.086** [+0.033, +0.147], 6 up / 0 down |
| co-mention, ≥2 documents | normalised PMI | 30 | 0.788 | **+0.100** [+0.030, +0.177], 6 up / 1 down |
| co-mention, ≥2 documents | normalised PMI, squared | 30 | 0.794 | **+0.105** [+0.040, +0.178], 6 up / 0 down |
| the same, chosen leaving each case out | | | 0.760 | +0.072 [−0.007, +0.153], 6 up / 2 down |
| the walk over the co-mention relation alone (no stated relation) | npmi | 1 | 0.757 | +0.069 [−0.004, +0.151] |

(At the first run the weight-10 row read 0.786 [+0.035, +0.170] and the leave-one-out row 0.752 [−0.013, +0.146]; the other rows did not move.) Sparsifying the relation (each page keeps its 5, 10 or 20 strongest neighbours) and the minimum number of documents (2, 3, 5) change nothing; there are only 239 pairs among the 106 pages. **On these 24 cases the normalisation is the effect.** The raw pair count ranks a pair by how often two frequent pages meet, which is the hubs again; normalised PMI ranks it by how much more often than chance two pages meet, which is specificity. Precision@8 rises with it, 0.273 → 0.381.

The six cases that move are those with the most gold pages, where the stated graph reached the few and outranked the rest: C4 (9 gold pages) 0.44 → 0.89, C5 0.40 → 0.80, C6 0.43 → 1.00, Q1 (11) 0.18 → 0.45, Q3 0.25 → 0.38, Q5 0.29 → 1.00 (squared, weight 30). The cases at 1.00 stay there; the two with no seed (C10, Q2) stay at 0; without the square C11 falls from 0.60 to 0.40, the one case down.

What this does not show: the interval of the honest, leave-one-out estimate still includes zero; 24 cases, six of them moving; the labels are the same hand's. What it does show is a direction with an independent source — the relation is counted over the source documents, never over the wiki. §5.2b asks whether that direction holds on other labels.

### 5.2b E2c — a second label set: the wiki's own links

Six cases carry the effect above. To ask whether it belongs to those six or to the relation, the wiki's `[[links]]` are a second, larger label set (`graphlab.py links`, `e2c-links.md`): each of the 91 pages that link, or are linked from, at least three pages is a case. The page is the seed, every `links` edge touching it is removed from the graph, and the gold is the pages it was linked to — 1,011 in all, about eleven a case. The page is left out of what it ranks. The hand is the same; the relation is counted over the source documents and no link enters it.

| configuration | recall@8 | vs the floor: mean, 90 % interval | up / down |
|---|---|---|---|
| the floor: stated relations, the page's own links removed | 0.395 | — | |
| co-mention, npmi, weight 3 | 0.427 | **+0.032** [+0.012, +0.052] | 26 / 10 |
| co-mention, npmi², weight 3 | 0.421 | +0.025 [+0.008, +0.044] | 22 / 6 |
| co-mention, npmi², weight 10 | 0.416 | +0.021 [−0.002, +0.043] | 27 / 11 |
| co-mention, npmi², weight 30 | 0.391 | −0.004 [−0.037, +0.029] | 28 / 28 |
| co-mention, npmi, weight 30 | 0.354 | −0.041 [−0.077, −0.005] | 25 / 40 |
| co-mention, npmi², weight 100 | 0.323 | −0.072 [−0.108, −0.037] | 18 / 50 |
| co-mention, raw: one per pair, weight 1 | 0.426 | +0.031 [+0.007, +0.056] | 28 / 11 |
| co-mention, raw: log2(1 + documents), weight 0.1 | 0.417 | +0.022 [+0.003, +0.041] | 23 / 8 |
| chosen leaving each case out (all 91 chose npmi, weight 3) | 0.427 | +0.032 [+0.012, +0.052] | 26 / 10 |
| the contracts' relation pairs (42), weight 1 | 0.407 | +0.012 [+0.005, +0.019] | 10 / 1 |
| the contracts' co-read pairs (106), weight 1 | 0.415 | +0.020 [+0.006, +0.035] | 14 / 4 |

Three things follow, and the first is the reason to trust the direction.

1. **The direction holds**: a relation counted over the documents adds to how the wiki links its pages, and the honest, leave-one-out estimate is above zero here (+0.032 [+0.012, +0.052]), where on the 24 cases its interval still includes zero.
2. **The size is a third of the first set's and the weight is an order of magnitude smaller.** The weights that gave +0.056 and +0.106 there (squared, 10 and 30) give +0.021 and −0.004 here, and a weight of 100 loses 0.07 to 0.14. The best weight on the links, 3, gives +0.026 [+0.006, +0.049] on the 24 cases. A single weight that neither set contradicts is 3 (npmi) — small on both — and the squared scale at 10 to 30 is the most the conflicts can have without the links losing more than noise.
3. **The normalisation is not the whole effect here.** The raw pair count at weight 1 adds +0.031, as much as npmi at 3; on the conflicts and questions it lowered recall by 0.113. On links the hubs are the answer — 65, 59 and 38 pages link `aegis`, `kael` and `juna` — and on conflicts they are what crowds the answer out. A relation that helps one task and hurts the other should be a parameter of the task, never a default of the graph.

The relation and the links overlap less than one would think. The relation holds 239 pairs; 102 of them (43 %) are linked, and 102 of the wiki's 512 linked pairs (20 %) stand in one paragraph in at least two documents. Co-mention alone, every stated type off, finds 0.198 of the links against the floor's 0.395. **The contracts' own page pairs help a little on the larger set**, where they could not show on 24 cases: +0.012 [+0.005, +0.019] for the 42 pairs a claim relates and +0.020 [+0.006, +0.035] for the 106 a claim holds together — from far fewer pairs than the 239 of the counted relation.

`e2c-links.md` ends with the 40 pairs of highest normalised PMI that no page links, a list for the author and not a set of links (a link is never inferred). **25 of the 40 are pairs among ten pages of the Alters** (`kiko`, `nyx`, `lex`, `rhys`, `alex`, `argus`, `isabelle`, `moros`, `lia`, `selene`), which stand together in 70 to 222 documents and link to each other nowhere; the pages of the Guardians `cerberus`, `kairos`, `logos` and `sophia`, and of the worlds `grenzfeste`, `moeglichkeits-garten`, `resonanz-landschaft` and `konstrukt-stadt`, make eight of the other 15. Whether the wiki wants those links is the author's call.

### 5.3 E4 — the hubs

`graphrag.pagerank` gained two corrections, off by default: `hub` divides a node's rank by its degree to a power, `spec` divides a seed's restart weight the same way. Over 24 configurations no setting beats the floor by more than +0.011 (`hub 0.25`, +0.011 [+0.000, +0.024]; `hub 0.5`, +0.011 [−0.017, +0.040]); `hub 1.0`, the full degree normalisation, loses 0.077; `spec` does nothing at 0.25 and loses 0.056 to 0.059 at 0.5 and 1.0. **Chosen leaving one out, the correction lowers recall: −0.041 [−0.082, −0.005], 1 case up and 5 down** — at the first run it read +0.013 [−0.011, +0.038]; the readings of four more documents and three record entries have been added since, and an inconclusive result is now a negative one. The gold pages *are* hubs often enough that removing hub-ness removes them. Not turned on.

### 5.4 E3 — the `ask` finders

`ask.py bench` measures how many of a case's gold documents and lines the pack holds, for a 60,000-character pack. Ablations on the store after the scaled contract pass, paired over the 24 cases; the default is five finders with `co-mention` limited to 10 paragraphs and the contracts' lines (`he-lines`) off:

| configuration | document recall | vs default (90 %) | up / down | line recall |
|---|---|---|---|---|
| default | 0.301 | — | — | 0.100 |
| without `graph-evidence` | 0.222 | −0.079 [−0.122, −0.042] | 1 / 15 | 0.071 |
| without `bm25-lines` | 0.172 | −0.129 [−0.198, −0.072] | 2 / 15 | 0.046 |
| without `parallel` | 0.267 | −0.034 [−0.051, −0.018] | 0 / 9 | 0.098 |
| without `entity-unread` | 0.301 | 0 | 0 / 0 | 0.100 |
| without `co-mention` | 0.289 | −0.011 [−0.028, +0.002] | 2 / 4 | 0.096 |
| with `he-lines`, 10 lines | 0.310 | +0.009 [+0.003, +0.018] | 4 / 0 | 0.101 |
| with `he-lines`, 20 lines | 0.319 | +0.018 [+0.006, +0.034] | 6 / 0 | 0.104 |
| with `he-lines`, 40 lines | **0.330** | **+0.029 [+0.011, +0.049]** | **7 / 0** | 0.108 |
| with `he-lines`, 80 lines | 0.322 | +0.021 [−0.007, +0.046] | 10 / 2 | **0.116** |

`bm25-lines` and `graph-evidence` carry the pack; `parallel` adds a little; `entity-unread` measures nothing here, because every gold document is read. **`he-lines` turned from a finder that lowered recall (−0.007 [−0.015, +0.001] on the pilot's eight documents, 76 gold lines) into a gain (+0.029 with 40 lines, seven cases up and none down — about what `parallel` adds, a third of `graph-evidence`'s) once the contracts had read the documents that hold the gold.** The curve is flat from 40 to 80 in documents (80 brings two cases down) and keeps rising in lines (+0.016 [+0.001, +0.031] at 80). The caveat is the pass itself: the twelve documents were chosen because they hold 40 % of the gold, so the gain is what contracts add where the answers are, and it is an upper bound for questions the gold does not cover. The finder stays off by default; turning it on at 40 lines is one line in `ask.py` and a question for the author (§8, question 4).

The co-mention finder is the only one whose *size* matters, so at the first run it was measured at four limits, each against the default of 40 (on the store before the scaled pass):

| co-mention limit | document recall | vs the default of 40 (90 %) | up / down | line recall |
|---|---|---|---|---|
| 40 (until 2026-09-30) | 0.262 | — | — | 0.092 |
| 20 | 0.299 | +0.037 [+0.015, +0.061] | 10 / 2 | 0.098 |
| **10** | **0.304** | **+0.041 [+0.016, +0.068]** | **10 / 1** | **0.100** |
| 5 | 0.303 | +0.041 [+0.017, +0.067] | 10 / 2 | 0.098 |
| none | 0.291 | +0.029 [+0.004, +0.055] | 10 / 4 | 0.096 |

A paragraph is a wide window and forty of them crowd out what the other finders reach; ten keep the finder's contribution and stop the crowding. `ask.py`'s default is now 10 (`COMENTION`), one line, provisional on 24 cases; on the store after the scaled pass the finder adds +0.011 [−0.002, +0.028] at that limit. Putting the counted co-mention relation into the walk that ranks pages (`--pr-comention 10`) moves the *pack* by +0.002 — the relation's effect is on which pages rank (§5.2), and the pack is dominated by `bm25-lines` and `graph-evidence`. A question's wording could choose which contracts' lines may answer it („was ist X“ by a definition, „warum“ by a cause); a map from wording to kind named one on 4 of the bench's 24 questions — they are conflict titles and questions in the form „A, or B“ — so the bench cannot test it and it was not built.

### 5.5 E5 — what the contracts read, as page pairs

3,152 claims from the contracts' runs on 19 documents are in the store; they touch 66 of the wiki's 106 pages and 32 of the 48 distinct gold pages (620 claims, 36 pages and 25 gold pages after the pilot). Their page pairs — 42 relation pairs (12 not already `links`), 106 pairs of pages one claim holds together (44 new) — added to the walk on the 24 cases change recall by at most one case (+0.006 [0.000, +0.018]); no gold page becomes reachable that was not, and the co-read pairs at weight 0.3 to 3 *lower* it (−0.031 to −0.082) — the raw count's pathology again. The scaled pass tripled the claims and the pairs, and the 24 cases still cannot see them. On the 91 link cases of §5.2b they can, slightly: +0.012 to +0.021 at weight 1. The contracts' value to retrieval is in the lines they read (§5.4), not in the pairs of pages they relate.

## 6. The scaled pass

The pilot could not move retrieval however its contracts did: eight documents hold 76 of the bench's 1,226 gold lines (6 %). So three contracts ran again on twelve of the fifteen documents that hold the most of them — **493 lines, 40 %** — chosen by the lines the conflict and question records cite and by nothing the contracts had found. Of the fifteen highest it left out the pilot's own `dual-storyform-hintergruende-md`, the 372 KB `kohaerenz-protokoll` (four times the largest of the twelve) and a chapter outline, `koharenz-protokoll-strukturierter-outline-2026-05-18`. The three are the ones a reader had marked right most often on theory text and that add what the stated graph lacks: a sentence that defines a term (`TermDefinitions`), a contrast between two terms (`TermContrasts`), a cause (`CausalLinks`). The documents are the philosophical report, the worldbuilding concept, the systemic architecture specification, the systems-narrative analysis, the consolidated concept, the philosophy in detail, the concept master, the sensory drafting, the Dramatica synthesis, the hard-SF outline, the mining report and the Kael compendium (`scaled.sh`).

### 6.1 What ran

36 runs, one at a time, Haiku through `claude -p` (decision 011): 957 calls, 21 of them failed and retried, 82 minutes of model time, **$11.68**. The pass was paused once, for a readings batch — the author asked for one model run at a time — and finished in `scaled2.sh`. No run failed as a whole and every run staged.

| contract | calls (failed) | minutes | cost | rows the model offered | entered: names / quotation | refused for good, and duplicates |
|---|---|---|---|---|---|---|
| `TermDefinitions` | 319 (8) | 26 | $3.79 | 1,463 | 1,257 / 19 | 176 + 11 |
| `TermContrasts` | 321 (9) | 32 | $4.08 | 1,345 | 1,063 / 60 | 219 + 3 |
| `CausalLinks` | 317 (4) | 25 | $3.80 | 878 | 579 / 189 | 109 + 1 |
| all | 957 (21) | 82 | $11.68 | 3,686 | 2,899 / 268 | 504 + 15 |

Of the 504 rows refused for good, 418 had a quotation the code could not place, 78 a quotation that stands on several lines and 8 a quotation the model had joined or shortened, or another defect. **`CausalLinks` is the contract whose slots the model words itself:** 189 of its 768 admitted rows enter on the quotation because a target is a clause (`die sehr Zerstörung, die es zu verhindern sucht`) — 25 % against 1.5 % of `TermDefinitions`' rows and 5 % of `TermContrasts`'. A cause is not a name, and a contract about causes should not be expected to return names.

### 6.2 Precision on the twelve documents

A reader labelled twelve rows per contract, drawn by the hash of the row's id from the rows not already labelled (`sample2.py`; nothing chose them by how they looked), from the quotation and its line, as in §4.

| contract | pilot: labelled, ok share | twelve documents: ok / part / wrong | ok share |
|---|---|---|---|
| `TermDefinitions` | 14, 79 % | 8 / 4 / 0 | 67 % |
| `TermContrasts` | 15, 80 % | 7 / 5 / 0 | 58 % |
| `CausalLinks` | 6, 83 % | 6 / 6 / 0 | 50 % |
| the three | 35, 80 % [67 %, 89 %] | 21 / 15 / 0 | 58 % [45 %, 71 %] |

**The rows are as near as they were and less often exact.** No row of the 36 was wrong, where the pilot had one in 35; the share that states exactly what the record says fell from 80 % to 58 %, and the two 90 % intervals barely meet. A pilot's 35 rows on documents chosen for their kind over-state the rate a contract has on the documents of the bench. What the 15 near rows have in common is the slot, not the line. Of the nine definition and contrast rows, five carry a verb or a clipped fragment where a term should stand (`ist`, `interne Referenz`, a two-word table cell), three set two things side by side that the line does not set against each other (a coexistence, two smells, a table cell read as two terms) and one is a chapter label beside its contents. Of the six causal rows, four are a type or direction error — an equation typed `causes`, a list of effects after an activation, a reversed direction, an `enables` for „is the position that" — one is circular (a function and its description) and one drops what is triggered. A row whose line is right and whose slot is poor is still what `he-lines` can use, because it joins the line to its pages by the line's own `MENTIONS` and not by the slot (§2).

### 6.3 What the rows reach

In the twelve documents the three contracts admitted rows on **1,456 of their 8,010 lines** (18 %), and 855 of those lines are also cited by a term page — 59 % of them, and 54 % of the 1,580 lines the pages cite there. A contract finds a slice of what a reader chose, as in §4.4; three together find more than one (`TermDefinitions` 36 % of the pages' lines, `TermContrasts` 33 %, `CausalLinks` 24 %).

Against the bench's own gold the lines concentrate it:

| the lines the contract admitted in the twelve documents | lines | of them gold | share of the twelve's 493 gold lines | share of its lines that are gold |
|---|---|---|---|---|
| `TermDefinitions` | 912 | 212 | 43 % | 23 % |
| `TermContrasts` | 852 | 184 | 37 % | 22 % |
| `CausalLinks` | 577 | 145 | 29 % | 25 % |
| the three together | 1,456 | 297 | **60 %** | **20 %** |

The base rate of gold in those documents is 6 %, so the contracts' lines hold it **3.3 times as densely** as the documents do, and 60 % of the gold is on lines some contract read. That is the ceiling for a finder that answers from these rows: 297 of the 1,226 gold lines, about a quarter, at a precision of one line in five. Across every contract and every document the pilot and this pass staged, 1,705 lines are admitted and 320 of them are gold (26 % of the 1,226) — so everything else the pilot staged — the other 29 contracts, and the three's own runs on the pilot's documents — adds 23 gold lines to the 297.

### 6.4 What it moved

Three things, each measured in §5. The `he-lines` finder went from −0.007 to **+0.029 [+0.011, +0.049]** document recall with 40 lines, and from 0.000 to +0.008 [+0.002, +0.015] line recall (§5.4). The contracts' page pairs still cannot move the 24 cases, though the 91 link cases of §5.2b show +0.012 to +0.021 (§5.5). And the cost, which the pilot had under-stated threefold, is now the ledger's own: $7.3 a megabyte a contract, about $190 for the corpus (§4.5).

### 6.5 The backfill, stopped after 14 runs

The author then asked for the three contracts on every document already read — 137 runs over 46 documents, estimated at $56 and six and a half hours, the documents holding most of the bench's gold first, one run at a time (`Plan/runs/hyperextract-backfill-2026-09-30/`). It ran from 19:00 to about 20:30 UTC on 2026-09-30, through two container restarts, and was stopped on the author's question „Is the backfill usefull? If not - stop it“ (decision 019) with **14 runs done**: five documents, 956 calls (12 returned no valid JSON; their chunk yields no rows), 77 minutes, **$11.44**, 2,191 rows admitted on the names and 297 on their quotation alone. That is $7.11 a megabyte a contract, against the $7.3 of §4.5 (`stats.py`).

What the rows reach of the bench's gold (`reach.py`; a reached line is a row on a line the records cite, not a right row):

| | earlier runs, 14 documents | the backfill, 5 documents |
|---|---|---|
| gold lines in those documents | 493 | 175 |
| reached | 297 (60 %) | 93 (53 %) |
| the rows' lines that are gold / the base rate / the lift | 19.3 % / 6.1 % / 3.2 | 7.7 % / 2.9 % / 2.6 |
| cost, and per gold line reached | $12.32, $0.041 | $11.44, $0.123 |

The lift is of the same size; the price of a gold line is three times higher, and it is one document. `kohaerenz-protokoll` (372 KB, 36 gold lines) cost $7.45, $0.35 a line reached; the other four reached 72 lines for $3.99 ($0.055). The plan's order — most gold lines first, then the smallest — is blind to size: ordered by gold reached per dollar, $11 would have reached 62 % of what the remaining documents could.

What it moved (`ask-finders/*-interim14.*` and `paired.py`; the default pack is identical on both stores):

| `he-lines`, document recall against the default | after the scaled pass (15 of the 55 gold documents read, 46 % of the gold lines) | after the 14 runs (19 read, 57 %) |
|---|---|---|
| 10 lines | +0.009 [+0.003, +0.018] | +0.009 [+0.003, +0.018] |
| 20 lines | +0.018 [+0.006, +0.034] | +0.016 [+0.006, +0.028] |
| **40 lines** | **+0.029 [+0.011, +0.049]**, 7 up / 0 down | **+0.029 [+0.012, +0.048]**, 7 up / 0 down |
| 80 lines | +0.021 [−0.007, +0.046], 10 up / 2 down | +0.021 [−0.016, +0.058], 9 up / 2 down |

Reading four more documents that hold gold, and a fifth the pilot had read, raised the share of gold lines in documents some contract has read from 46 % to 57 % and left the gain where it was: the same seven cases up and none down, four cases moved by 0.031 or less in both directions, and the paired difference over the 24 cases is −0.0003 [−0.0028, +0.0021] (`eval-audit.py`). `ceiling.py` says why. Over the 24 cases there are 569 gold-document slots; the default pack finds 139; with 40 lines `he-lines` recovers 24 more, 7 of them in documents the backfill read; 182 are missed although a contract has read the document, and 226 are missed in documents no contract has read. Four recoveries are in documents the scaled store had not read (`kohaerenz-protokoll` in C2, C6 and Q5, `storyform-und-outline` in Q5), and in those cases document recall did not rise: the finder's lines are a fixed budget, and lines of the new documents replaced lines of the old. **Coverage did not move it; that the finder's seeds and ranking are the lever is an inference from these counts, not a test.**

So §7's item 6 — „a bench with every gold document read would say what the finder is worth at its ceiling“ — has a first answer: what it is worth now. It is not an answer for the 226 slots in unread documents. Were they recovered at the rate the finder recovers the read ones (24 of 206, 12 %), that would be about +0.04; a finder that spent its lines better might reach more; the last 14 runs showed no trace of either. What stays unmeasured: the precision of the backfill's rows (none is labelled; `sample.py` draws the rows, and three drawn by eye looked looser), and every retrieval question the bench cannot ask, because its gold is what the records already cite.

## 7. What to do, in this order

1. **Bring the normalised co-mention relation to the author** (§8, question 1) — the largest effect on the conflicts and questions, a third of it on the wiki's links, and no model call. It is built and off: `askextract.learn_comention` derives the pairs, the store holds them as `P_COMENTION`, `graphrag.py --comention W` walks them. What is left is the decision and more labelled cases of both kinds — 24 and 91 cannot support one default for two tasks.
2. **Run the structure contracts by category** — `ChapterBeats`, `StructureBeats`, `ChapterCards` on the 218 plot outlines ($66 each), `CardFields`, `EntityFacts`, `ProseRules` on the 37 character documents and the style guides (about $12 each): 86–100 % of their records were right, and they give the graph a line-level index of what a chapter holds and what a figure is. Label twelve rows per contract on the documents that will be run first — the three contracts of the scaled pass fell by 12 to 33 points between the pilot's documents and the bench's — and not before the author says what it may cost (§8, question 2).
3. **Run `TermDefinitions` and `TermContrasts` on the concept and theory categories** ($26 + $18 + $14 + … each); 73 % and 70 % ok over 26 and 27 rows, 58 % on the scaled documents alone, none wrong there. Their value is the sentence that defines a term, which no stated relation carries, and `he-lines` turned it into +0.029 document recall where the gold is (§5.4).
4. **Do not run** `Precedence`, `Anchors`, `Rules`, `TermTaxonomy`, `Knowledge` and `AliasPairs` as they are: their records are right about the line and wrong about the relation. Revise, measure again against the same labelled rows, then decide. `AliasPairs` and `Precedence` now carry a cue in code; that is the only change made.
5. **Keep the empty contracts** (`Locks`, `Quantities`, `Attributions`, `StandingClaims`, `Pitch`) for the documents of their kind — a decision log, a numbers table, a review, a briefing — and gate them by category, so that they cost nothing where they find nothing.
6. **Do not let the next pass follow the gold, yet.** The contracts have read 19 of the 55 documents that hold gold (701 of 1,226 lines). The first 14 runs of a pass over the rest — $11.44, five documents holding 175 lines — did not raise `he-lines` at all (§6.5), and the pass was stopped (decision 019). More coverage is money without a measured return until a finder spends its lines better, per seed or by the question's wording; then `ceiling.py` names where to read, cheapest first. It is a spend for the author to name (§8, question 2), not a step to take.
7. **Do not wire `hegraph.gate` into `he_claude.py run` for `CausalLinks`**: a gated run found 26 % of the lines an ungated one finds for 29 % of the cost, the same price a line (§4.6). If a contract is to be cheaper it is run on fewer documents (item 6), and a gate for the other claim contracts is to be measured the same way before it is believed.

## 8. Questions for the author

1. **The normalised co-mention relation in `graphrag`'s walk.** Built and off (`--comention W`). It is derived from the documents' own text and never from the wiki. On the 24 conflicts and questions it raises recall by 0.06 to 0.11 at weight 10–30 (leaving one out: +0.072 [−0.007, +0.153]); on the wiki's own links — a second label set of 91 cases — it adds +0.032 [+0.012, +0.052] at weight 3 and loses at 30 and 100 (§5.2b). It would be the first relation in the default walk that is not one of the seven the wiki states. Turn it on at weight 3 (the one neither set contradicts), at 10–30 for questions and conflicts only, keep it off, or wait for more labelled cases?
2. **A contract pass.** About $190 a contract for the whole corpus, $66 to $1 by category (§4.5) — this note first said $63, and the ledger says $7.3 a megabyte. Which contracts, on which categories, may run? The pass the author asked for, over the read documents, was stopped at 14 of 137 runs because five more gold documents moved `he-lines` by nothing (§6.5, decision 019): should any contract run on more, and on what, before the finder can use it?
3. **Who labels.** The 297 labels are the working session's reading of a quotation and its line — from 3 to 30 rows a contract, most 10 to 15 — and the three contracts of the scaled pass fell from 80 % to 58 % `ok` between the pilot's documents and the bench's. Five hundred more from the author, or from another reader, would say what the contracts are worth.
4. **The finders' defaults in `ask.py`.** `he-lines` at 40 lines adds +0.029 [+0.011, +0.049] document recall on the bench, seven cases up and none down — measured on documents chosen for holding the gold, so an upper bound, and unchanged by five more of them (§6.5) — and is off; turning it on is one line, and makes the pack depend on a paid pass's coverage. The `co-mention` finder's limit of 10 paragraphs (40 before) is also a line of another session's code, provisional on 24 cases.
5. **Pages the corpus holds together and the wiki does not link** (§5.2b, `e2c-links.md`). Forty pairs of highest normalised co-mention have no link between them; 25 are among ten pages of the Alters, which stand together in 70 to 222 documents. A list to read, never a set of links. Does the wiki want any of them?

## 9. What this does not show

- 24 cases, and the labels are written by the hand that wrote the pages. A difference smaller than its interval is not a difference, and the intervals here are wide. The 91 link cases are a second label set and the same hand's; they say the co-mention direction holds and that its weight is a task's, not the graph's.
- The contracts' precisions come from 297 rows, 3 to 30 per contract, most 10 to 15, labelled by one reader who is also the model family that wrote the contracts. A precision of 79 % on 14 rows is 79 % ± 20 points, and the scaled pass showed that a pilot over-states it by 12 to 33 points.
- The pilot's documents were chosen to give each contract a document of its kind, and the scaled pass's to hold the bench's gold, so the yields are not corpus rates, and only `TermDefinitions`, `TermContrasts` and `CausalLinks` have run on more than two documents.
- `he-lines` is measured where the contracts read the gold. A question whose gold is in a document no contract has read is helped by nothing here, and the 43 % of the gold lines the contracts have not read (525 of 1,226, after the backfill's 14 runs) are the measure of what a bench would need to show the finder's worth everywhere; five more documents did not move it (§6.5).
- `entity-unread` measures nothing here because every gold document is read; its value is routing to unread documents, which no bench measures.
- The finders are measured by how much of the gold the *pack* holds, not by the answer a model writes from it.
- **The bench's gold is circular and its cases are few.** The gold is the file lines the records cite, and 92 % of them are lines a term or chapter page also quotes; no gold document is unread, so discovery cannot score; the 24 cases overlap (mean Jaccard 0.35) and can show a mean effect of about 0.027 or more, where `he-lines` shows +0.029. `Plan/concept/evaluation-audit_2026-09-30.md` has the audit and what to change.
- The cost per megabyte is one rate over twelve documents (from $6.4 to $14.5 a megabyte by run), and $7.11 over the backfill's five (§6.5); the plot outlines, which are a third of the corpus by size, have not run the three contracts, and the pilot's runs on its chapter outline were among the dearest ($10–12 a megabyte).
