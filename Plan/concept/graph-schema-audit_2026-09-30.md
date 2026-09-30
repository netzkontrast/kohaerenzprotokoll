# Graph content, efficient representation and useful additions

Measured against the complete shared GraphQLite store on 2026-09-30, before the
citation-reference correction. These are observations of that snapshot, not
live counts or claims about unread sources' meanings. No research document was
independently read, source prose rewritten, entity identity promoted or canon
chosen for this review.

## What the graph mostly represents

| Layer | Measured shape | Meaning and recommended treatment |
|---|---|---|
| Source structure | 125,620 Line, 62,932 Paragraph, 10,786 Section nodes | Locations and document structure, not independent knowledge claims. Keep source text in Sources and FTS; load/cite lines only for the task at hand. |
| Paragraph size | 51,439 of 62,932 paragraphs have one line (81.7%) | Do not assume every block deserves both a paragraph record and an individually serialized line record in a future compact layout. |
| Structure edges | 125,620 HAS_LINE, 62,932 HAS_PARAGRAPH, 125,034 NEXT | 313,586 edges (55.9%) are these three types. Membership/relation queries can eventually use source spans and ordered collections instead of materializing every adjacency. |
| Wiki core | 181 Core aliases; 4,418 original relationships | Compact, source-attributed navigation. Preserve order and edge multiplicity for existing PPR/MMR compatibility. |
| Evidence | 9,022 records; 7,270 unique (source,line,quote) slots; 6,931 distinct quote strings | Reading-specific attribution must survive deduplication. Shared quote/span storage may reduce repeated text, but do not merge two readings or their stances. |
| Mentions | 75,964 MENTIONS, 91,617 P_NAMES | Lexical discovery, not assertions about relationships or entity identity. A surface match alone does not justify a claim. |
| Statistical groups | 742 cooccur, 2,495 parallel hyperedges | Keep method, support and provenance. These are computed retrieval proposals, not LM-trained facts. Co-occurrence is not causation or equivalence. |
| URL references | 4,865 Url nodes keyed by host; 16,334 LINKS_URL edges | They actually represent domains. Paths and complete URLs were discarded by extraction. Do not describe these as exact URL citations; a future Site/Resource split is justified if link resolution is needed. |

Text structure (Line + Paragraph + Section) is 199,338 of 217,538 nodes (91.6%).
Line + Paragraph alone account for 86.7%. The three edge families above plus
SUB total 323,649 edges (57.7%). Adding location mentions and link occurrences
makes the operational graph larger again. A large graph here is mostly a
fine-grained index, not evidence of many semantic assertions.

### A reproduced provenance defect, corrected in code

23 evidence records marked verified exported a reference that did not verify
their quotation. `quotes.verdict()` accepted one of several nearby references,
while `graph.evidence_of()` always chose the first. One consequently had no
source ID and pointed at line 63 rather than its actual, source-qualified quote
reference. The fix selects the same reference that resolves the quotation.
Existing correctly attributed evidence IDs remain unchanged; corrected IDs
change because their previously wrong provenance is part of their identity.
An offline regression exercises the wrong-first/right-second case.

## The efficient target schema

| Representation | Keep | Avoid |
|---|---|---|
| Source | stable source ID, content hash, date/version, manifest identity | copied full source text in every export or markdown graph page |
| Span | source ID, first/last line; optionally character offsets and hash | one universal semantic graph node per nonblank source line |
| Reading | source, page, scope, frozen extraction/reconciliation status | reducing read, cited, reconciled and approved to one boolean |
| Assertion | subject, predicate, object/literal, polarity, modality, scope, Reading and Span | flattening denial, hypothesis, question and assertion into one direct fact edge |
| Evidence attachment | links a particular assertion/reading to a verified source span | merging two sources' readings just because their quote strings coincide |
| Concept and identity proposal | stable concept ID; explicit alias/identity candidate with justification | equating case-folded names, surfaces and characters automatically |
| Question/Conflict/Decision | explicit dependencies, recorded options, selected answer only when authored | treating related source passages or co-occurrence as an answered question |
| Derivation | method/template version, input hashes, run, check results | a generic `learned:true` that obscures counted patterns versus model proposals |

The human-readable export does not rewrite the database schema. Existing Line
traversal, paragraph co-mentions and query contracts remain available through
the database. Span compression is a separate migration: keep a compatible
virtual/materialized Line view, compare query answers and costs, then choose
physical representation. The atlas omits structural records and source text;
it cannot recreate the database.

For semantic reasoning, an Assertion node is worth its overhead. Two sources
may state `AEGIS controls X` and `AEGIS does not control X`, or use different
world/time scopes. Separate assertions can be supported, challenged and queried
without turning either source position into global canon. DSPy/HyperExtract can
propose these records; extraction placement verifies wording, not truth. No
current query should claim that these proposed labels are already installed.

## Helpful graph information, in implementation order

1. **Source/reading freshness and coverage.** Link source versions to independent
   census/note, reconciliation and page readings. A planning agent can ask which
   source has been landed but never read, which reading is stale, and what cannot
   support a decision yet. Import exact existing run/record metadata first.
2. **Question → cited material → decision → dependency.** The current Question,
   Conflict and Sheet nodes are a useful base. Add authored decision records and
   explicit prerequisite links. `cites` or `uses-source` can be mechanical;
   `answers`, `supports` and `contradicts` need recorded judgement or a clearly
   labeled proposal. An unanswered question remains unanswered.
3. **Source-scoped assertions and polarity.** Integrate the relation-reading
   template's assertion/denial/hedge/question distinctions with source spans and
   scopes. Keep one assertion per reading, even when subjects/predicates match.
   This is the highest-value semantic addition; validate on actual extracted
   fixtures before migrating live data.
4. **Extraction/template lineage.** Link TemplateVersion, ExtractionRun, Candidate
   and CheckResult from existing staged artifacts. Record source/template hashes,
   exact placement/refusal, review outcome and held-out evaluation. Never call a
   counted co-occurrence group a trained extraction template.
5. **A small tools/process map.** Read the actual installer registry, initialization
   phase plan and scripts README: which capability runs which CLI, requires which
   environment and validates which artifact. Useful for delegated agents choosing
   a command and recovering from unavailable tools; facts must come from the
   registry, not a second manual list. No secrets/provider credentials enter it.
6. **Scoped identity candidates.** Alias, rename and same-entity hypotheses with
   source evidence and review status. Distinguish a person's name, a fictional
   persona, a concept and a system sharing a surface. Statistical proposals can
   prioritize review; only a recorded decision promotes identity.
7. **Writing dependencies and knowledge boundaries.** Later, connect approved
   scene/chapter plans to decisions, relevant assertions and perspective/temporal
   scopes. A source date or chapter mention is not a spoiler permission or an
   adopted scene fact. Novel writing remains governed by the open author decisions.

Do not add all seven ontologies upfront. Build the first useful query from
existing records, keep its fixture, measure the gain, then grow the model. The
current database and targeted source access remain available throughout.

## Human-readable export and session handover

The author changed the purpose: Graph is a reading atlas, not a portable backup.
`kg.py export` now writes topic pages and separate sources/conflicts/questions/
decisions views. No full source text, evidence payloads, node-property dumps,
serialized relationships or machine manifest are exported. No restore/import
command exists and builders never read Graph. Text lines are cited only when a
specific statement needs evidence. The view does not invent the source's position.

At session startup: install tools → keep a fresh database or rebuild it from
Sources/Wiki/Plan. Export remains explicit. A human edits authoritative files,
then regenerates the atlas; editing an atlas page cannot change a graph fact.

For context, the discarded cache prototype measured 41 seconds to rebuild,
24 seconds to restore and 19 seconds to export, using installed tools and local
files. That is a modest startup benefit, no token saving, and requires an
unchanged source/code checkout. It did not justify making the readable atlas a
binary archive. The final PR removes that prototype and its archives entirely.

The useful knowledge additions remain the source-scoped assertions, reading
coverage, explicit decisions and template/check lineage prioritized above.
