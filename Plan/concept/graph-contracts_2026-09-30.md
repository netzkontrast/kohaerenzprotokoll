# Graph contracts — what HyperExtract can add to the `ask` graph, and what the graph laboratory found instead

**2026-09-30 · Measured, not adopted.** On the author's requests „Explore Even more hyperextract templates that could and should be used to Improve our Graph in ask.dB" and „Now Read /writing-skills and use that Knowledge to Devise eben more hyperextract templates specific for those use cases", after „maybe you should think about additional hyperextract contracts to help Improve the recall Presion of our Graph rag solutions". Nothing here changes what `graphrag.py`, `ask.py` or the store return by default: every measured change is a parameter that is off, a proposal edge type (`P_HE_*`, never in the core) or a command of `graphlab.py`. What the author has to decide is in §8.

Reading done for this note: the thirteen `writing-skills` and their entry page, `Plan/concept/novel-writing-plan_2026-09-29.md`, `GOAL.md` §4–5, `Plan/concept/hyperextract-templates_2026-09-24.md`, the HyperExtract templates already in `Plan/hyperextract/`, and `Plan/runs/graph-lab-2026-09-30/diagnose.md`. No source document was read for it beyond what the contracts extracted, and every label in §4 was written by the working session, not by the author.

## 0. The answer on one page

1. **What moved recall of the wiki's own labels is not a HyperExtract contract.** Two pages standing in one paragraph in at least two documents, weighted by their normalised pointwise mutual information over documents, and added to the walk of `graphrag.pagerank` as a page–page relation: recall@8 **0.688 → 0.788** at weight 30 (+0.100, 90 % interval [+0.030, +0.177], 6 cases up, 1 down; 0.794 with the statistic squared); leaving each of the 24 cases out and letting the other 23 choose among 96 configurations: **0.752** (+0.064 [−0.013, +0.146]). The cases that move are those with the most gold pages — C4 0.44 → 0.89, C6 0.43 → 1.00, Q5 0.29 → 1.00, Q1, Q3, C5. The same pairs counted, not normalised, **lower** recall by 0.10 to 0.13: the normalisation is the whole effect (§5.2).
2. **Re-weighting the stated relation types moves nothing.** Uniform, learned and cross-validated weights all score within 0.006 of the default; `links` alone carries what recall there is (§5.1). A correction for hubs is inconclusive (+0.013 leaving one out) and a seed-specificity weight lowers recall (§5.3).
3. **The contracts are worth their price where they read structure, and not where they read theory as a set of relations.** On 261 records a reader labelled, a contract that classifies the line under a heading — `ChapterBeats`, `StructureBeats`, `ChapterCards`, `CardFields`, `ProseRules`, `EntityFacts`, `Utterances` — was right 83–100 % of the time; `TermDefinitions` and `TermContrasts` 79 %; `AliasPairs` 36 %, `Anchors` 20 %, `Precedence` 18 % (§4.2). Two cheap rules in code, not in the prompt, lift the last two families: an alias without an alias word and an order without an order word are not admitted.
4. **The gate that stages a candidate refused right rows, for three reasons the pilot exposed.** Of 263 rows refused only because a slot was not verbatim in the document, 70 named a figure of under four characters (`Lex`, `Nyx`, `Lia`, `KW1`) — `quotes.parts_of` drops fragments that short, so no three-letter name could ever be found — and 68 carried the word the `Utterances` contract itself tells the model to write when a line has no speaker. Both are fixed in the gate; the other 125 are the model's own wording of a clause or an inflection, and now enter the store on their quotation alone (§4.1).
5. **At the pilot's scale the contracts cannot move the retrieval numbers, and do not.** Eight documents hold 76 of the bench's 1,207 gold lines. Adding the contracts' lines to the `ask` route changes document recall by −0.007 (§5.5). §6 says what a scaled pass over the twelve documents that hold most of the gold measured.
6. **The `ask` finders were measured too**: `bm25-lines` and `graph-evidence` earn their place; `entity-unread` is inert on this bench; the co-mention finder as built *lowers* document recall, and limited to fewer paragraphs raises it (§5.4).
7. **What to do**: §7 orders it. The one thing that needs the author's word first is the co-mention relation in the default walk (§8, question 1).

## 1. The question, and what the laboratory said before any contract was designed

The author asked for a graph enriched with useful information, for experiments including treating every relation the same, and for relation types that rank differently in a mix — using what a HyperExtract-enriched graph can capture. `Plan/runs/graph-lab-2026-09-30/diagnose.md` gave the starting point: over the 24 labelled cases (the wiki's conflicts and questions, each retrieving the pages that raised or contest it, with the case's own node removed), **96 gold pages: 49 hit, 38 reached and outranked, 0 unreachable, 9 with no seed** because the question names no page's surface. The outranked pages are one hop from a seed and stand at rank 10 to 86 (`did`: rank 26, `realitaetsebenen`: rank 50); the ones that outrank them are hubs (`aegis`, `juna`, `kael`, `vortex`).

That says what would help: a relation that puts a seed *closer to specific pages than to hubs*, and a name that reaches a page the question spells differently. It does not say weights help, and §5.1 confirms they do not.

## 2. What was built

| piece | what it is | where |
|---|---|---|
| **32 contracts** | HyperExtract templates, each a reading rule in the template's own guideline, each carrying `provisional`, `may not` and `retire when`, each with a fixture the offline check runs. 8 existed; 24 are new, 11 derived from the diagnosis and the stated graph's gaps and 13 from the writing skills | `Plan/hyperextract/*.yaml`, `fixtures/` |
| **the staging gate** | a candidate's quotation must be placed on one line by code and every name must stand in the document; a name of under four characters now stands as a word on its own, and the word `unlabelled` (a contract's word for „no speaker") needs no line | `scripts/reading_extract.py` |
| **`hegraph.py`** | loads staged rows into the store as `P_HE_<KIND>` edges, grades them by code, reports what each contract yielded, and gates a document so a run sends only the paragraphs that hold a contract's cue | `scripts/hegraph.py` |
| **two footings** | a row enters on *names* (every name the model wrote stands in the document) or on its *quotation* alone (a slot is the model's own wording, the line is placed, and the pages in the line are found by code, never by the slot) | `hegraph.staged` |
| **contract nodes** | every admitted row is an edge from its line to `he:<KIND>`, so „lines a contract read" needs no page; a row's names or its quotation add edges to the pages and entities they contain | `askdb.collect` |
| **a finder, off** | `he-lines`: lines a contract read that concern the question's seeds, by the contract's own edge or by the line's `MENTIONS` | `ask.py` (`--with he-lines`) |
| **the laboratory** | `graphlab.py`: 24 cases, five experiments, paired comparison with a 90 % interval and leave-one-out choice | `scripts/graphlab.py` |

The design choices that follow from the repository's rules: a contract may not carry a page's name in its own text (procedural knowledge only, `templates.py check`); a row keeps the model, run and template that produced it, so a wrong template is one `git log` away; **a proposal never enters the core** (`P_` relation types are excluded from the ranking, the paths and the communities by name); and no finder filters on a grade that was not shown to predict anything (§4.3).

## 3. The catalogue

Thirty-two contracts in four families. The *derived from* column names the artefact that asks for the record; the pilot column is §4's, over eight documents. „Ok" and „ok+part" are the share of labelled rows a reader marked right, and right or near; the number of labelled rows is in the last column.

<!--CATALOGUE-->
| family | contract | relation | derived from | documents | rows: names / quote | labelled | ok / ok+part |
|---|---|---|---|---|---|---|---|
| terms | `TermReadings` | `P_HE_READING` | the notes: what a document says about a term, with its line (#124) | 1 | 66 / 4 |  |  |
|  | `TermDefinitions` | `P_HE_DEFINES` | „what is X“ is best answered by the sentence that defines X; `TermReadings` ranks a definition no higher than a remark | 13 | 1347 / 19 | 26 | 73% / 96% |
|  | `TermContrasts` | `P_HE_CONTRAST` | the author's reading of „Große Stille“ against „das große Schweigen“ as a tension, found by a BM25 relation | 6 | 522 / 30 | 15 | 80% / 100% |
|  | `AliasPairs` | `P_HE_ALIAS` | diagnosis: 9 of 96 gold pages have no seed because the question names a page under a name no page carries | 1 | 32 / 11 | 15 | 40% / 67% |
|  | `Analogies` | `P_HE_ANALOGY` | the census's `lens` sections: a fictional term and the real concept the document says it corresponds to | 2 | 16 / 2 | 15 | 47% / 80% |
|  | `TermTaxonomy` | `P_HE_TAXON` | diagnosis: `[[links]]` are untyped, so a class and its member cannot be told apart | 1 | 7 / 1 | 7 | 43% / 43% |
|  | `StatedRelations` | `P_HE_REL` | #124's comparison of graph tools: nodes and edges a document states | 0 | not run |  |  |
|  | `RelationReadings` | `P_HE_REL` | `StatedRelations` that keeps hedges and questions | 0 | not run |  |  |
|  | `TermCensus` | `P_HE_CENSUS` | the reader's candidate lists | 0 | not run |  |  |
|  | `LocationRegistry` | `P_HE_LOCATION` | document 6's master table of places | 0 | not run |  |  |
| claims and sources | `CausalLinks` | `P_HE_CAUSAL` | the plot model as checkable rules; „why does X happen“ has no stated relation | 1 | 0 / 6 | 6 | 83% / 100% |
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

Eight documents, chosen to give each contract a document of its kind: a foreshadowing plan, a chapter outline, a style guide, a theory document in English, a storyform document, a narrative text, a briefing and the world-concept synthesis. Thirty-seven runs, 313 calls, **$3.63**, Haiku through `claude -p` (decision 011), one run at a time. Each run staged into `Plan/runs/<document>/hyperextract/<contract>-haiku-2026-09-30/`; `yield.md` in `Plan/runs/hyperextract-templates-2026-09-30/` is the report `hegraph.py report` writes. A reader (the working session) labelled 261 rows from the quotation and its line: 150 `ok` (the quotation states what the record says), 80 `part`, 31 `wrong`.

### 4.1 What the gate refused that was right

Of 263 rows refused only for `surface absent from document`, with the quotation placed on one line:

| why the slot was not found | rows | now |
|---|---|---|
| a name of under four characters (`Lex`, `Nyx`, `Lia`, `KW1`, `KW`) | 70 | **stands** — the gate accepts a name of under four characters when it is a word on its own on some line |
| the word `unlabelled`, which `Utterances` tells the model to write when the text tags no speaker | 68 | **stands** — a contract's word for no name needs no line |
| a clause of more than three words, the model's own wording | 99 | enters on its quotation |
| a name inflected or reworded (`Isabellas`, `innere Barrieren`) | 26 | enters on its quotation |

The first is a defect of a rule written for quotations. `quotes.parts_of` drops fragments under four characters because a three-character quotation matches everything; a *name* is not a quotation, and the cast — `Lex`, `Nyx`, `Lia` — is exactly what a fielded contract wants. It affected `TermReadings` as well, which the earlier live pass could not have shown: its census names were longer. `stands()` in `reading_extract.py` judges a name of four characters or more as it always was, so no row a stage accepted changes; three cases in its selftest hold it (25 of 25).

The rows that enter on their quotation are labelled too: of 71 such rows a reader marked, `CausalLinks` 83 % ok (6 rows), `CardFields` 100 % (4), `Utterances` 44 % ok and all `ok+part` (9), `Knowledge` 30 % ok (10), `Anchors` 20 % ok (20). The footing does not lower a contract's precision; the contract does.

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
| `CausalLinks` | 6 | 5 | 1 | 0 | 83% [50%, 96%] | 100% |  |
| `TermContrasts` | 15 | 12 | 3 | 0 | 80% [59%, 92%] | 100% |  |
| `ThemeMotifs` | 4 | 3 | 1 | 0 | 75% [36%, 94%] | 100% |  |
| `TermDefinitions` | 26 | 19 | 6 | 1 | 73% [57%, 85%] | 96% | 12, 67% |
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

- **Contracts that classify a line under a heading** are right about the line and weak about the name: `ChapterBeats` 92 % ok, `StructureBeats` 100 %, `ChapterCards` 83 %, `CardFields` 80 %, `ProseRules` 90 %, `EntityFacts` 90 %. A card field's figure is the *heading* above the bullet (`Lex`, `Argus`), so it is written nowhere on the line; a chapter beat's chapter is a numbered, bolded heading that names no chapter number. Names for these come from the store, not from the model: the line's own `MENTIONS`, and the contract's edge to a page when the model named the figure. That is why `he-lines` joins two ways (§2).
- **Contracts that relate two names in a sentence** depend on the document. `TermContrasts` (79 % ok) and `TermDefinitions` (79 %) hold on theory prose. `AliasPairs` failed in one recurring way — a slash list („Kael/Juna") read as a pair, a copula („Autopoiesis ist ein Funktionsprinzip") as an alias, a management sentence as `role_of` — and the rule the prompt already had („a role is not an alias") did not stop it. `Precedence` inferred an order from the adjacency of list items in 8 of 11 rows. A prompt rule that a Haiku reader ignored 8 times in 11 is not a rule; the repository's own lesson about readers applies: **what is not checked in code is not done.**
- **Contracts that carry a proposition** (`Knowledge`, `Rules`, `Anchors`, `ThemeMotifs`, `OpenPoints`) mostly return the sentence right and the *type* wrong: a premise typed `must_not`, a beat typed `plants`, a fear typed `cannot_yet_know`. Their records are good evidence that the line is *about* the thing and poor evidence of the relation the type names.
- **Contracts that found nothing** are informative: `Locks`, `Quantities`, `Attributions`, `StandingClaims` and `Pitch` answered every call and returned an empty list on the documents they were tried on — a theory document holds no lock, a briefing no standing claim. `reading_extract` refuses an empty list because HyperExtract can swallow a schema error into one; `hegraph report` tells the two apart by the calls' own record (`failed_calls` 0 and a reply of a few tokens), and counts them as „answered, found nothing", never as a failure and never as a yield of zero.

### 4.3 The grade does not predict, and two cues do

`hegraph.quality` grades a row 2 when a cue word of the contract and every name stand in the quotation, 1 when one of the two does, 0 when neither. It was meant as a filter. Against the labels: grade 0, 64 % ok (96 rows); grade 1, 52 % (84); grade 2, 79 % (19). It does not separate. The reason is family two: a list item under a heading is right with no cue word and no name in its quotation.

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

$0.0115 a call, about 4.7 KB of text a call, so $0.03 for a 4 KB document and $0.19 for the 28 KB storyform document, per contract. The 586 landed documents are 25.1 MB: **about $63 per contract for the whole corpus**, and by category $21 for the 218 plot outlines, $9 for the 80 concept documents, $6 for the 43 psychology theories, $4 each for physics, characters, AEGIS and storyform, $3 each for worldbuilding, logic and mathematics. A contract that reads outlines has no use on a physics paper, so the run is *by category*; and `hegraph.gate` keeps only the paragraphs that hold a contract's cue words (with their neighbours), which the pilot did not use.

### 4.6 What the cue gate saves

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

The gate pays for the claim contracts — `StandingClaims`, `Locks`, `Knowledge`, `CausalLinks`, `OpenPoints`, `Attributions` — which read a sentence in a few; it does nothing for `TermDefinitions`, whose cue (`ist`, a colon) stands in every paragraph, or `Quantities`, whose cue is a digit. It is not yet wired into `he_claude.py run`: a gated run must first be shown to find what an ungated one finds.

## 5. Retrieval, measured

Every number below is a row of `Plan/runs/baselines.jsonl`, so `baseline.py compare` reads it; every table is in `Plan/runs/graph-lab-2026-09-30/`. The task is the wiki's own labels — the same hand that wrote the pages wrote them — so what a number can say is which mix does better on this hand's labels, never that a mix is right.

### 5.1 E1 — the seven stated relation types

| configuration | recall@8 | vs the default: mean, 90 % interval |
|---|---|---|
| default weights | 0.694 | — |
| uniform: every type 1.0 | 0.688 | −0.006 [−0.018, +0.000] |
| only `links` | 0.681 | −0.014 [−0.055, +0.022] |
| learned on all 24 (in sample) | 0.694 | +0.000 |
| learned, 6-fold cross-validated | 0.694 | +0.000 |
| seeds alone, no walk | 0.531 | −0.164 [−0.251, −0.085] |

(At the time of E1 the bench read 0.694; after the readings of documents 52–54 it reads 0.688, which is the floor of every later table.) Treating everything the same is as good as tuning. `links` carries the recall; the other six types add nothing a paired comparison can see. The learned weights differ from the default by grid steps and are equal across folds for four of seven types.

### 5.2 E2 and E2b — relations the corpus adds

Derived from the shared store — `MENTIONS` of a page's surface on a line, grouped by paragraph and document — and never from the labels. Each set is added to every case's graph as a page–page relation beside the stated ones.

| relation | scale | best weight | recall@8 | vs the floor |
|---|---|---|---|---|
| learned co-occurrence sets (`askextract`) | lift, capped | 10 | 0.758 | +0.069 [−0.020, +0.160], 6 up / 4 down |
| co-mention, every pair in ≥2 documents | count of documents | 3 | 0.576 | **−0.113** [−0.196, −0.041] |
| co-mention, every pair in ≥2 documents | log of the count | 3 | 0.556 | **−0.133** [−0.219, −0.058] |
| co-mention, ≥2 documents | **normalised PMI** | 10 | 0.786 | **+0.098** [+0.035, +0.170], 6 up / 0 down |
| co-mention, ≥2 documents | normalised PMI, squared | 30 | 0.794 | **+0.105** [+0.040, +0.178], 6 up / 0 down |
| the same, chosen leaving each case out | | | 0.752 | +0.064 [−0.013, +0.146], 6 up / 2 down |
| the walk over the co-mention relation alone (no stated relation) | npmi | 1 | 0.757 | +0.069 [−0.004, +0.151] |

Sparsifying the relation (each page keeps its 5, 10 or 20 strongest neighbours) and the minimum number of documents (2, 3, 5) change nothing; there are only 239 pairs among the 106 pages. **The normalisation is the effect.** The raw pair count ranks a pair by how often two frequent pages meet, which is the hubs again; normalised PMI ranks it by how much more often than chance two pages meet, which is specificity. Precision@8 rises with it, 0.273 → 0.381.

The six cases that move are those with the most gold pages, where the stated graph reached the few and outranked the rest: C4 (9 gold pages) 0.44 → 0.89, C5 0.40 → 0.80, C6 0.43 → 1.00, Q1 (11) 0.18 → 0.45, Q3 0.25 → 0.38, Q5 0.29 → 1.00. The cases at 1.00 stay there; the two with no seed (C10, Q2) stay at 0.

What this does not show: the interval of the honest, leave-one-out estimate still includes zero; 24 cases, six of them moving; the labels are the same hand's. What it does show is a direction with an independent source — the relation is counted over the source documents, never over the wiki. It is the finding to build on, and it is not a HyperExtract contract.

### 5.3 E4 — the hubs

`graphrag.pagerank` gained two corrections, off by default: `hub` divides a node's rank by its degree to a power, `spec` divides a seed's restart weight the same way. Over 24 configurations: `hub 0.25` +0.021 [+0.005, +0.042] in sample and **+0.013 [−0.011, +0.038] leaving one out**; `hub 1.0`, the full degree normalisation, −0.118; `spec` lowers recall at every setting. The gold pages *are* hubs often enough that removing hub-ness removes them. Inconclusive, and not turned on.

### 5.4 E3 — the `ask` finders

`ask.py bench` measures how many of a case's gold documents and lines the pack holds, for a 60,000-character pack. Ablations, paired over the 24 cases:

| configuration | document recall | vs default (90 %) | up / down | line recall |
|---|---|---|---|---|
| default, five finders | 0.262 | — | — | 0.092 |
| without `graph-evidence` | 0.193 | −0.069 [−0.107, −0.034] | 3 / 14 | 0.068 |
| without `bm25-lines` | 0.181 | −0.081 [−0.148, −0.027] | 5 / 10 | 0.053 |
| without `parallel` | 0.248 | −0.014 [−0.025, −0.003] | 1 / 7 | 0.091 |
| without `entity-unread` | 0.262 | 0 | 0 / 0 | 0.092 |
| without `co-mention` | 0.291 | **+0.029** [+0.004, +0.055] | 10 / 4 | 0.096 |
| with `he-lines` (pilot data) | 0.256 | −0.007 [−0.015, +0.001] | 2 / 4 | 0.090 |

The co-mention finder is the only one whose *size* matters, so it was measured at four limits, each against the default of 40:

| co-mention limit | document recall | vs the default of 40 (90 %) | up / down | line recall |
|---|---|---|---|---|
| 40 (until 2026-09-30) | 0.262 | — | — | 0.092 |
| 20 | 0.299 | +0.037 [+0.015, +0.061] | 10 / 2 | 0.098 |
| **10** | **0.304** | **+0.041 [+0.016, +0.068]** | **10 / 1** | **0.100** |
| 5 | 0.303 | +0.041 [+0.017, +0.067] | 10 / 2 | 0.098 |
| none | 0.291 | +0.029 [+0.004, +0.055] | 10 / 4 | 0.096 |

A paragraph is a wide window and forty of them crowd out what the other finders reach; ten keep the finder's contribution and stop the crowding. `ask.py`'s default is now 10 (`COMENTION`), one line, provisional on 24 cases. Adding the contracts' lines with a limit of 10 (`he-lines`) moves nothing either way (0.257, −0.005 [−0.011, +0.001]); putting the counted co-mention relation into the walk that ranks pages (`--pr-comention 10`) moves the *pack* by +0.002 — the relation's effect is on which pages rank (§5.2), and the pack is dominated by `bm25-lines` and `graph-evidence`. A question's wording could choose which contracts' lines may answer it („was ist X“ by a definition, „warum“ by a cause); a map from wording to kind named one on 4 of the bench's 24 questions — they are conflict titles and questions in the form „A, or B“ — so the bench cannot test it and it was not built.

### 5.5 E5 — what the contracts read, as page pairs

620 claims from the pilot are in the store; they touch 36 of the wiki's 106 pages and 25 of the 48 distinct gold pages. Their page pairs — 19 relation pairs (5 not already `links`), 38 pairs of pages one claim holds together (12 new) — added to the walk at every weight change recall by at most one case (+0.006 [0.000, +0.018]); no gold page becomes reachable that was not. The size of what could move is bounded by the pairs, not by the weights. That is the pilot's scale, not the contracts' ceiling.

## 6. The scaled pass

*The pass over the twelve documents that hold most of the bench's gold was still running when this version was pushed; this section, §4.5's cost figures and the tables' scaled columns are filled in the next commit.*

<!--SCALED-->

## 7. What to do, in this order

1. **Bring the normalised co-mention relation to the author** (§8, question 1) — it is the largest measured effect and needs no model call. If the author agrees: derive the pair statistic once, in `askextract` beside the co-occurrence sets; store it as a counted page–page edge; give `graphrag.retrieve` an optional extra relation, off until turned on; add labelled cases first, because 24 cannot support a default.
2. **Run the structure contracts by category** — `ChapterBeats`, `StructureBeats`, `ChapterCards` on the 218 plot outlines ($21 each), `CardFields`, `EntityFacts`, `ProseRules` on the 37 character documents and the style guides (about $4 each): 83–100 % of their records were right, and they give the graph a line-level index of what a chapter holds and what a figure is. Not before the author says what it may cost (§8, question 2).
3. **Run `TermDefinitions` and `TermContrasts` on the concept and theory categories** ($9 + $6 + $4 + $3 …), 79 % ok each; their value is the sentence that defines a term, which no stated relation carries.
4. **Do not run** `Precedence`, `Anchors`, `Rules`, `TermTaxonomy`, `Knowledge` and `AliasPairs` as they are: their records are right about the line and wrong about the relation. Revise, measure again against the same labelled rows, then decide. `AliasPairs` and `Precedence` now carry a cue in code; that is the only change made.
5. **Keep the empty contracts** (`Locks`, `Quantities`, `Attributions`, `StandingClaims`, `Pitch`) for the documents of their kind — a decision log, a numbers table, a review, a briefing — and gate them by category, so that they cost nothing where they find nothing.
6. **Turn on `he-lines` only after a run that covers the documents that hold the gold** (§6).

## 8. Questions for the author

1. **The normalised co-mention relation in `graphrag`'s walk.** It is derived from the documents' own text and never from the wiki; it raised recall of the wiki's labels by 0.06 to 0.10 and moved only the cases with many gold pages. It would be the first relation in the default walk that is not one of the seven the wiki states. Turn it on at weight 10–30, keep it off, or wait for more labelled cases?
2. **A contract pass by category.** About $63 per contract for the whole corpus, $21 to $4 by category (§4.5). Which contracts, on which categories, may run? The pilot's answer is §7, items 2 and 3.
3. **Who labels.** The 261 labels are the working session's reading of a quotation and its line. Five hundred more from the author, or from another reader, would tell whether the contract-level precisions hold.
4. **The `co-mention` finder in the `ask` pack.** Removing it raised document recall by 0.029 [+0.004, +0.055]; limiting it to 20 paragraphs raised it more (§5.4). The finder is another session's; the default is one line in `ask.py`.

## 9. What this does not show

- 24 cases, and the labels are written by the hand that wrote the pages. A difference smaller than its interval is not a difference, and the intervals here are wide.
- The contracts' precisions come from 261 rows, 10 to 14 per contract, labelled by one reader who is also the model family that wrote the contracts. A precision of 79 % on 14 rows is 79 % ± 20 points.
- The pilot's documents were chosen to give each contract a document of its kind, so the yields are not corpus rates, and no contract was run on more than two documents.
- `entity-unread` measures nothing here because every gold document is read; its value is routing to unread documents, which no bench measures.
- The finders are measured by how much of the gold the *pack* holds, not by the answer a model writes from it.
