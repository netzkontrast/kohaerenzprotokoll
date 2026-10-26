# Reading one term page whole — the full read, the thought page, and what it changes

*2026-10-23. Asked for by the author: „We Now Need a new process that you Need to Plan intensivly - one where One Page from
the Wiki will be Read completly - including all citatiins - to generate a new Page - that contains every thought that is
needed for this Term. So we can promote the Page - also we Need to Update the ui to Reflect that - as well as improvements in
the ontology of the Graph System“. This is the plan; nothing in it is built or decided. Every construct below is
`provisional` until the author answers §11.*

## 1. Why the existing steps do not do this

The wiki has the two ends of the road and nothing in the middle.

- **A candidate page is a ledger, not an account.** It holds one section per source document, by date, each reading in that
  document's words. That is right for the research (P13: attributed and unmerged), and it is unreadable as a review object at
  the size the pages have reached. Measured 2026-10-23 over the 106 candidates: 25,380 distinct citations and about 850,000
  words; the median page carries 105 distinct citations; eleven pages carry 500 or more; `aegis` carries 2,906 distinct
  citations from 435 documents in 94,177 words, `kael` 2,424, `juna` 1,521.
- **Promotion (decision 026) reviews that ledger.** For Kishōtenketsu (89 citations) the author could do it. For `aegis` nobody
  can, and the sheet (`promote.py sheet`) checks only what code knows: quotations resolve, sources reconciled, links resolve.
  Whether the page *says everything the sources think about the term* is not checked anywhere.
- **The term page (decision 027) is written from a reviewed candidate**, by hand, picking points. Nothing checks that a point
  was not left out, so its completeness is the writer's memory.

So the missing step is the one the author named: **read the page whole, including every line it cites, and write down every
thought about the term once, with all the sources that carry it**. It also needs a check that the result *is* whole, because
„every thought“ is otherwise a claim nobody measured (CLAUDE.md, *A claim is measured, or marked unmeasured*).

## 2. The unit: a thought (Gedanke)

A **thought** is one statement about the term that a source makes. It is written once, in the writer's German. It carries every
citation that makes it, each with that source's stance. Two sources saying the same thing give one thought with two citations.
Two sources saying different things give two thoughts and a difference between them.

```yaml
id: g-017                       # stable within the page; never reused
kind: mechanism                 # definition | function | mechanism | origin | evolution | relation | prose | open
text: Kap 40 erzählt dieselben Ereignisse wie Kap 0, aus der Position nach der pluralen Heilung.
sources:
  - cite: koharenz-protokoll-konzept-konsolidiert-2026-05-08-md.md:L930
    stance: asserts             # asserts | proposes | questions | rejects | reports
    date: 2026-05-08
  - cite: koharenz-protokoll-konzept-iteration-genesis-md.md:L457
    stance: asserts
    date: 2026-05-08
involves: [genesis]             # other terms, only where a cited line names them
differs_from: [g-021]           # only where the page's differences say so
status: draft                   # draft | reviewed
```

```yaml
thought:  # provisional — a guess at the unit a complete account needs
          # may not: merge two readings whose words or stance differ; decide which reading is right;
          #          enter canon; stand for a source the writer did not open at its line
          # retire when: three full reads show the author reviews by source, not by thought
```

**What a thought is not.** It is not a merge of readings: grouping is allowed only where the cited lines state the same thing,
and every source keeps its own citation and stance. „Same thing“ is a judgement, so each grouping of more than one document is
recorded (§4, `groupings.jsonl`), like a judgement about a near match. A thought is not a fact about the novel: it is what
sources think, and a `[K]` mark still needs the author's decision linked (decision 027).

The **kinds** are what a writer needs to know of a term: what it is (`definition`), what it does in the story (`function`), how
it works (`mechanism`), where it comes from in the world (`origin`), how the sources' idea of it changed over time (`evolution`),
how it stands to other terms (`relation`), what the prose must or must not do with it (`prose`), and what no source settles
(`open`). The kinds are the page's sections, so the page is ordered by question, not by document.

## 3. Whole means: every citation is accounted for

„Every thought“ becomes measurable through the citations. The candidate page's citations are the evidence base the wiki has
for the term, and each one ends in exactly one of these states:

| state | means | example |
|---|---|---|
| `used` | at least one thought cites it | the line is the source for g-017 |
| `same-as` | the same quotation is already cited from the same line on the page | a reading repeats its own L930 under the differences |
| `context` | the line frames another cited line and carries no thought of its own | a heading cited before its table |
| `occurrence` | the line names the term without saying anything about it | a title, a list entry, a reference |
| `barred` | the line holds an early name, a real person's name, the trauma symbol or a world code's expansion | decision 028 and the standing rules: read, never quoted |
| `defect` | the reading's prose says something its line does not say | goes to §5, a fix on the candidate |

The **ledger** `Plan/runs/fullread/<slug>/ledger.jsonl` has one row per distinct citation of the candidate page, with its state,
the thoughts that use it, and the context window the writer opened (`read.py <slug> --from a --to b`). The mechanical claim of
wholeness is: **every distinct citation on the candidate has a row, no row is empty, and every `used` row names a thought that
exists.** The reverse also holds: every citation on the thought page is either on the candidate or added by the full read from
a line the writer opened (`added`, with its reason, e.g. the next line completes the cited sentence).

That proves *coverage of the evidence*, not *completeness of the understanding*. The second is judgement and is tested in the
pilot by a blind second reader (§9).

### What else the full read reads

The term's thoughts are not only on its own page. The full read also opens, and accounts for in the same ledger
(`origin: …`):

- **the conflict records and question pages** that name the page (`Wiki/conflicts/`, `Wiki/questions/`);
- **the other candidate pages' readings that link it** (`[[slug]]`), because a source writing about `nexus` may say what
  `aegis` does there; only the sentences that name the term;
- **the chapter pages' readings** that name it (`Wiki/chapters/`, decision 013);
- **the project's own records**: `terms.py finds` (decisions, Weichen, `Manuscript/kanon.md`, `Plan/storyform/`) — the only
  source of `[K]`;
- **the sweep ledger** `Plan/runs/sweep.jsonl`: occurrences decided for this page, so that the coverage line can say how many
  read documents write the term without a reading here.

What it does **not** read: unread documents (after decision 028 and the end of the ingest of 2026-10-23, 584 documents are read;
the coverage line names those that write the term and are not), `Legacy/`, and the wiki's other pages as authority — they are
evidence of where a source spoke, never a reading of their own.

## 4. The procedure

```
candidate page (ledger of readings)
  │
  ▼ fullread.py plan <slug>        the packet: every distinct citation, grouped by document, with its context window,
  │                              barred lines marked, sizes; chunks of at most ~150 citations or ~1,500 source lines
  ▼ read, chunk by chunk          the writer opens every window, writes thoughts and one ledger row per citation
  │                              (chunks-NN/thoughts.jsonl, chunks-NN/ledger.jsonl, chunks-NN/defects.md)
  ▼ fix the candidate first       each defect is a commit on the candidate page naming the source document (§5)
  ▼ group                         the session joins the chunks: same thought → one, recorded in groupings.jsonl;
  │                              different → two thoughts and a difference; a new contradiction → a conflict record (decision 003)
  ▼ fullread.py write <slug>        renders Wiki/terms/<slug>.md from thoughts.jsonl: sections by kind, [S]/[K]/[L]/[D] bullets,
  │                              citations, the coverage block; the author's block kept
  ▼ fullread.py check <slug>        §6, and quotes.py, terms.py check
  ▼ commit                        „terms/<slug>: full read of the candidate as of <date>, <n> citations“
  ▼ the author reviews the thought page, not the ledger (§7)
```

**Order with the existing pages.** The candidate stays as it is: the ledger, one commit per source document. The thought page
is a new version of the term page of decision 027, written from the full read rather than from points picked by hand. §7 says
what the review then covers, and §11.1 asks the author whether this order — full read *before* promotion — is the one meant.

**Who writes.** The session writes, chunk by chunk, in order. A chunk is the same kind of work as an ingest reading, so a
Sonnet subagent (`full-reader`, write access to its run directory only) can read a chunk, and the session groups and commits.
Model calls are serial except the two Sonnet ingest readers NOW.md allows; whether that allowance extends to full-read chunks
is the author's call (§11.4). Until then: one chunk at a time.

**Stopping and resuming.** The ledger is the progress: `fullread.py status <slug>` counts rows per state and the citations still
without one. A full read of `aegis` spans sessions, and a session continues at the first chunk with an incomplete ledger.

**When the candidate moves.** A source reconciled after the full read adds readings to the candidate (under `## Since review`
if the page is promoted). `fullread.py check` names the citations without a ledger row as **behind**, the same word `terms.py`
uses. The update is a small full read of those citations only.

## 5. What the full read finds on the candidate

Reading every cited line next to its reading is also the first complete audit of the readings themselves. The ingest checked
that each quotation sits on its line (`quotes.py`); it never checked that the prose around the quotation says what the line
says. Found defects are fixed on the candidate **before** the thought page uses that reading, each in a commit naming the source
document whose reading changed (CLAUDE.md, *Committing a wiki page*). Kinds already seen in this project's history: a duplicate
difference line, a stale provenance note (decision 026's first promotion), a reading that cites a barred line (558, 535 in
PR #195), an English paraphrase that hardens a source's hedge into a claim. A defect in a reviewed part of a promoted page
is not fixed in place: it is a question to the author with the fix proposed (decision 026, §3).

## 6. What `fullread.py check` refuses

| check | refuses? |
|---|---|
| every distinct citation of the candidate has exactly one ledger row, none without a state | refuses |
| every `used` row names a thought on the page; every thought has at least one citation | refuses |
| every citation on the thought page resolves (`quotes.py`), none unchecked | refuses |
| no cited line is `barred`: the extended early-name list, real persons' names, the trauma symbol, world-code expansions | refuses |
| a grouping of two or more documents has a `groupings.jsonl` row | refuses |
| `[K]` links a decision, an answered Weiche, `kanon.md` or a decided conflict (as `terms.py` already checks) | refuses |
| every document in the candidate's `ingested:` appears in at least one thought or in the ledger as set aside, with its reason | refuses |
| the page reads as German; the sections by kind are in order | refuses |
| behind: candidate citations newer than the ledger | noted |
| set-aside share per state, thoughts per kind, documents per thought | noted, in the coverage block |

A `selftest` has one fixture per refusing row, each failing on the defect it names (`selftests.py --only std`), and CI runs
`fullread.py check` beside `terms.py check`.

## 7. Promotion after a full read

Today there are two reviews: promotion reviews the candidate (026), approval reviews the term page (027). With a full read
the two collapse into one natural act, and the plan proposes exactly that, as the author's choice:

- The author reads the **thought page**. It is short enough to read: by the pilot estimate below, a few hundred bullets
  for `aegis` instead of 94,000 words.
- The **review sheet** gains the full read's numbers: citations accounted for, by state; thoughts by kind; groupings; defects
  fixed on the candidate; coverage of read documents that write the term.
- **One word from the author** then does both: `promote.py apply <slug> --words "…"` sets the candidate `status: reviewed` and
  pins it (as now), and `terms.py approve` pins the thought page against the same candidate hash. Each thought becomes
  `status: reviewed` by being on the pinned page; no thought is reviewed alone.
- What a review still is **not**: a choice of reading. A reviewed thought page lists differences and stops (decision 026 §1).

If the author prefers two acts, nothing above changes except that `apply` and `approve` stay separate.

## 8. The graph: what the ontology gains

The graph (`scripts/graph.py`) has four node types — `term`, `doc`, `conflict`, `question` — and seven edge types, of which only
`links` joins two terms, untyped. The schema audit of 2026-09-30 (`Plan/concept/graph-schema-audit_2026-09-30.md`) named the
node it lacked: an **Assertion** with polarity, scope and its evidence, so that „AEGIS controls X“ and „AEGIS does not control X“
are two claims rather than one co-mention. A thought is that node, and it comes with its evidence already checked. Proposed,
all derived from files as every edge is now (`via: file:line`, decision 005), none inferred:

| new | from | carries / means |
|---|---|---|
| node `thought:<slug>/<id>` | the thought page | kind, text, status (draft/reviewed), the page's date |
| edge `about` thought → term | the page it is on | the thought is about this term |
| edge `supports` thought → doc, with line and stance | each citation of the thought | which source carries the thought, and how (asserts, proposes, questions, rejects, reports) |
| edge `involves` thought → term | a `[[link]]` inside the thought | a typed term–term relation: the thought's text is the predicate, its citations the proof |
| edge `differs_from` thought → thought | the page's differences | a stated disagreement, never one a program guessed (CLAUDE.md, *Conflict detection is never mechanised*) |
| edge `decided_by` thought → decision / kanon / Weiche | a `[K]` link | the author's decision the thought rests on |
| edge `raises` thought → conflict / question | a link to a record | where the thought feeds an open record |
| attribute on `term` | candidate, promotion ledger, term page | `layer`: candidate, read whole, reviewed, approved — one value instead of today's two fields |

**What it gives.** (1) `graphrag.py ask` and the MCP server's `ask` can return thoughts first — one sentence with all its sources —
before raw quotations; (2) `involves` is the first term–term edge that says *what* the relation is, with evidence; (3) the
differences between sources become edges a retriever can follow to the other side; (4) the `Graph/` atlas gains one page per
thought page with its thoughts. **What it does not do:** no thought from an unreviewed page is trusted more than a quotation;
whether thoughts improve retrieval is measured on the 26 labelled bench cases before `ask` ranks them first (CLAUDE.md,
*Changing what a model's output may do is measured on labels*). The bench's known weakness (92 % of its gold lines are lines the
pages quote) favours thoughts, so the measurement is reported with that caveat.

**Chapters**, a node the author has been asked about (NOW.md item 5: „chapters in the graph and the app“), would make
`thought —occurs_in→ chapter:kap-NN` possible where a thought cites a chapter page. It is listed, not proposed, until that
question is answered.

Also touched: `kg.py` (the GraphQLite projection gains the `Thought` label and the five edges), `kg.py export` (the atlas),
`rag.py` (the serving index of the MCP server serves thoughts with their citations; withheld lines stay withheld), and
`relations.py`, which stays as it is — `links` remains the page-to-page link, and `involves` is separate.

## 9. The pilot, and what it measures

Three pages, in this order, one at a time, each stopped and reported before the next:

| page | distinct citations | documents | why |
|---|---|---|---|
| `genesis-klammer` | 92 | 12 | small, clean on the sheet, a structural term with known differences (Kap 40's last image) |
| `kishotenketsu` | 89 | 29 | already reviewed and has a hand-written term page: the full read is measured against it |
| `nexus` | 94 | 46 | many documents, few citations each: tests grouping across sources |

Then one large page (`entropie`, 538 citations from 188 documents) before anyone starts `aegis`, `kael` or `juna`.

**Measured per page:** minutes and tokens per citation; thoughts per citation; share of each ledger state; defects found on the
candidate; groupings per thought. On `kishotenketsu`: how many points of the hand-written term page the full read also has, and
how many thoughts it has that the hand-written page lacks. **On `genesis-klammer`, once:** a blind second reader writes the
thoughts from the same packet without seeing the first; the two lists are aligned by hand. That gives a ceiling for „every thought“
— the share two readers agree on — which the project has never measured for any reading (`Plan/runs/gold-2026-09-30/README.md`).
Until then, completeness of understanding is reported as unmeasured.

**Extrapolated, to be replaced by the pilot's numbers:** if a page needs about one thought per three to five distinct citations,
`aegis` gives 600–950 thoughts. That is still too long to review in one sitting. A thought page for the largest terms may need a
second level — one summary thought per kind, linked to its thoughts — which the pilot decides, not this plan.

## 10. The app

The app already separates the layers under one address (`#/wiki/<slug>`: *Begriffsseite*, *Quellenlesarten*, *Promotion &
Stand*; `Plan/concept/term-questions-ui_2026-10-14.md`). The full read adds:

- **The thought page as the first view.** Thoughts grouped by kind; each one opens to its sources — document, date, stance,
  the verified quotation on its line — from data `ui.py` already builds for evidence. Filters: kind, stance, document, date,
  „has a difference“. A difference shows both thoughts side by side.
- **A coverage panel** on *Promotion & Stand*: citations by ledger state, documents covered, defects fixed, behind or not, the
  command that continues the read (`python3 scripts/fullread.py status <slug>`).
- **A review mode for the author.** Per thought: „passt“, „Frage“, „falsch“, with a note, kept in the browser and exported as one
  text the author pastes into a session. No button reviews or approves anything: approval stays the author's words in the
  repository (P0; the decision inbox of the 2026-10-14 concept is the same idea).
- **The pipeline state in the wiki list:** Kandidat → in Durcharbeitung (n of m citations) → durchgearbeitet → geprüft → bestätigt,
  as a filter and a chip.
- **Addresses and agents** (the app-refresh rule for anything new): `#/wiki/<slug>/g/<id>` for a thought, in `route()`/`unroute()`
  and `ROUTE_HARNESS`; every thought in `agents/index.json` with its file and address; `agents/data.json` carries the thoughts;
  `ui.py --check` fails on a thought without an address, a thought citing no evidence, or a coverage panel that disagrees with
  `fullread.py status`.
- **The graph view, term first:** the selected term, its thoughts as a ring, `involves` and `differs_from` as the edges, the rest
  of the graph behind a toggle — the „term-first graph“ the 2026-10-14 concept listed as its fourth next change.
- **Now:** a full read in progress is a NOW.md § Half-done entry, so it appears as a session with its prompt and claim line.

## 11. Questions for the author

1. **Order.** The plan reads a page whole *before* promotion, and the thought page becomes what you review (§7). Is that what you
   meant by „so we can promote the page“ — or should the full read come after promotion, as the basis of the term page only?
2. **One review or two.** One word of yours promotes the candidate and approves the thought page together (recommended), or the two
   stay separate acts as now.
3. **Language.** The thought page in German, like the term pages of decision 027 (recommended), or English like the candidates.
4. **Readers.** May a full-read chunk go to a Sonnet subagent, up to two at a time like the ingest (first-party, decision 011), with
   the session grouping and committing — or does the session read every chunk itself?
5. **Which page first.** The pilot order in §9 (`genesis-klammer`, `kishotenketsu`, `nexus`, then `entropie`), or a term the next
   chapters need first.
6. **The graph.** Thoughts as nodes in the core graph (recommended, they are written and checked like readings), or beside it like
   the proposal layer until you have reviewed a thought page.

**Answered 2026-10-23** (the author, through the session's question form): 1 — **before promotion**, the thought page is what
the author reviews; 2 — **one act**, one word promotes the candidate and approves the thought page; 4 — **yes, up to two** Sonnet
subagents read chunks, the session groups and commits; 5 — **`genesis-klammer` first**. Questions 3 (language) and 6 (the graph)
are not answered; the plan proceeds on its recommendations (German; thoughts in the core graph), both provisional.

## 12. What gets built, in order

1. `scripts/fullread.py`: `plan`, `status`, `check`, `write`, `selftest` — standard library, offline fixture first (a three-document
   fixture page with every ledger state and every refusal).
2. `.agents/skills/full-read/SKILL.md` (the procedure above, with its refusals) and `.claude/agents/full-reader.md` (one chunk,
   its run directory only, no wiki writes).
3. The first full read, `genesis-klammer`, by the session, with the blind second reader; numbers into `Plan/learnings/fullread.md`.
4. `terms.py` and `promote.py`: the thought format, the sheet's new numbers, one review if the author says so.
5. `graph.py`, `kg.py`, `rag.py`: the thought node and its five edges, selftests; bench run before any ranking change.
6. `ui.py`, `ui.js`, `ui.html`: §10, with `ui.py --check` cases and a look at 1440 and 390 pixels.
7. A decision file (030) once the author has answered §11; CLAUDE.md's diagram and `Wiki/terms/README.md` updated with it.

Steps 1–3 need none of the answers in §11 except 4 (who reads); steps 4–7 wait for them.
