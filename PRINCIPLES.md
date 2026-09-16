# Principles — read this before building anything

**This is the one place to look.** Before writing a new skill, a new command, a
new script, a new check or a new page type: read this file. It holds the rules we
follow and the ideas we have decided are worth keeping but have not built yet.

Every principle below was produced by something that actually went wrong or
actually worked in this repository. None is a preference. Where a principle has
evidence, the evidence is named, because a rule whose reason is forgotten gets
argued away within a month.

---

## The two that outrank everything

**P0 — Never assume; ask.**
Where a decision would rest on a guess, stop and ask. Canon facts, wording,
scope, a name, which of two sources wins. Two decisions are never a session's to
make: user-facing flags, and promotion. A question is cheap; a wrong assumption
baked into the corpus is not.

**P1 — If it can be programmatic, it is.**
Anything decidable is a program. Anything not decidable is *named* as judgement.
There is no third state.
**The test:** if a rule can be broken without a check failing, it is prose, not a
rule.
*Evidence:* the R-rules were declared to have one encoding and had four —
`lint_chapter.py`, `WRITING.md`, 99 codex records, and a Canon section. Four of
the ten had no executable encoding at all, and nothing noticed.

---

## What to build, and what not to

**P2 — Describe no more than exists.**
Documentation that runs ahead of reality is the most expensive defect this
project has had. Fix the description in the same change as the thing, or write
the description after.
*Evidence:* `CLAUDE.md` described a `Canon/ → Graph/` pipeline that
`ingest_canon.py` does not perform; it names nine commands where eleven exist;
`bootstrap.md` names four skills where five exist. Seven commands are referenced
that were never written, and 25 of 92 links inside `.claude/` are broken.

**P3 — By hand first. Automate what has proved its shape.**
Do the thing manually a few times, look at what it actually produced, then build
the tool around that. A schema written before its instances describes a guess,
and every later instance pays for the guess.
*Evidence:* five page types, 26 lint rules, three DSPy programs and a schema
across five YAML files produced **two pages**. The `contradiction` type had eight
required fields, its own enum, five prose rules and a 62-line template, and
**zero instances**.

**P4 — No page type, field or check without instances.**
A thing earns existence by being needed, not by being anticipated. If it has no
instances after real use, it is removed rather than kept "for later".

**P5 — Every workflow carries its own proof.**
A workflow ships with a fixture that runs offline, free, with no API key. A
workflow that cannot be exercised drifts silently, and silent drift is how this
repository spent months.
*Evidence:* `lit_critic_gate.py` exits 2 because its source was never installed;
`.venv-dspy` did not exist while three commands invoked it; `/kp-decide` — the
documented exit from every contradiction the system could find — was never
written.

**P6 — One encoding per rule.**
A skill says *run this, here is what the output means*. It does not restate what
the tool enforces. Two encodings of one rule drift apart on the first edit.
*Evidence:* the source-authority hierarchy is stated six times across
`.claude/` and the six disagree. "A lint cannot show what is missing" is stated
in five places.

---

## Checks

**P7 — A check that cannot see the filesystem is not a check.**
Verify against the world, not against a string.
*Evidence:* `audit_graph_claims.py` classifies a claim's provenance by matching
the prefix of `source_uri` and never calls `stat()`. Delete `Canon/` and all 223
claims still pass, green, while every one of them cites a file that is gone.

**P8 — Compare the index against reality, always.**
Whenever there is a manifest, a registry or a list, something must compare it to
what is actually on disk and report the difference.
*Evidence:* 26 of 680 manifest rows had an exported file. Nothing compared them,
so a 3.8 % completion rate silently became the shape of the project.

**P9 — Derived data must not depend on data that does not exist yet.**
Check what a derivation reads before relying on it.
*Evidence:* `context_packet.py` derives each entry's chapter window by scanning
the manuscript prose. Empty the manuscript and every chapter returns an identical
packet — while the tool still exits 0 and prints a cost line that reads like
success.

**P10 — Four buckets, and the fourth is the one that matters.**
Every body of derived knowledge gets asked: what is `FOUND` (cited and
resolvable), what is `INFERRED` (synthesised — judgement, surfaced never
settled), what is `CONFLICTING` (two sources that cannot both hold), and what is
`MISSING`. The first, third and fourth are decidable. `MISSING` is the one no
lint can express and the one that catches "26 of 680".

**P11 — Never collapse several checks into one pass/fail bit.**
Report each check's own status. A single green light hides which of nine things
was actually verified.

---

## Working with sources

**P12 — Quote, do not paraphrase.**
A derived page carries the source's own words with a resolvable line range. A
paraphrase presented as a quotation is the single most-broken rule in the one
real pilot run this project has had.

**P13 — Never merge readings into one definition.**
Where two sources say different things about one term, the page holds both,
attributed. Merging deletes exactly the information the wiki exists to provide.
The page names a disagreement and stops; which side is right is the author's.

**P14 — Not every apparent contradiction is one.**
Before reporting a conflict, exclude the cases that are disagreement by design.
This filter is worth more than the detector it guards: without it, a contradiction
ledger reports the same known-good classes forever and trains the author to
ignore it.

**P15 — Separate "never reached" from "answered badly".**
A thing that could not be evaluated has not been evaluated. Reporting it as a
failure is worse than reporting nothing, because it looks like a verdict.
*Evidence:* the first model sweep reported two models at 0 %. Neither had failed
the task — one returned a 404, the other was restricted to another harness.

---

## Models and measurement

**P16 — Measure per step, never globally.**
A model good at extraction can be bad at merging. Model choice comes from a
benchmark against *that step's* fixture and *that step's* metric.

**P17 — Benchmark the real thing.**
Score the actual program with the actual metric a real run is judged by. A
benchmark-only task drifts away from the workload it claims to stand for.

**P18 — One attempt measures nothing.**
Reliability needs repeats, and the cache must be off. A cache replays the first
completion and an unreliable model scores a perfect 100 %.
*Evidence:* a model scored 1.00 when it worked and failed one attempt in three by
emitting chain-of-thought where JSON belonged. A single attempt would have shown
100 %.

**P19 — Assert non-empty output, and assert the language.**
*Evidence:* a reasoning model spent its whole token budget on reasoning and
returned `content: None` with `finish_reason: length` — no error, nothing to
catch. And the free router returned correct German claims with an **English**
summary; the metric checked the claims' language, not the summary's. The corpus
is German. Both failures were invisible to a benchmark that only checked schema
validity.

---

## Structure

**P20 — Two layers until a third earns itself.**
Every layer is another place for the same fact to be stated differently.

**P21 — The archive is a shelf, not a layer.**
Nothing links to it, no script scans it, `CLAUDE.md` does not describe it.
Exactly one sentence in `README.md` says what it holds and which commit it came
from. If it starts being referenced, it has become a layer again.

**P22 — Prefer a phase chain with a checkpoint per phase.**
Declared inputs, declared outputs, an author decision at each layer.
*Evidence:* `/kp-world` is built this way and is the most reusable artefact in
the old surface. `/clarify` and `/tetraframe` are the same shape and are the
only other two that held.

---

## When building a new skill, command or tool

Answer these before writing it:

1. **Does it restate a rule a tool already enforces?** If yes, delete that part
   (P6). The skill says *run this, read the output this way*.
2. **What is its fixture?** If it cannot be run offline against a known input, it
   is not finished (P5).
3. **What does it read, and does that exist?** (P9, P8)
4. **Which parts are decidable, and which are judgement?** Name both. There is no
   third category (P1).
5. **What does it deliberately not do?** Write it down. Every workflow that held
   in the old surface stated its non-responsibilities explicitly.
6. **Where does the author decide?** (P0)
7. **Has it earned existence?** Is there a real instance asking for it, or is it
   anticipated? (P3, P4)

---

## The catalogue — good ideas kept, not yet built

These survived the reset because they are worth building. None is built. Each is
listed with where it belongs under P1, so that picking one up is a small job
rather than a re-derivation.

### High value, build first

| idea | belongs in | why it matters |
|---|---|---|
| **The five "by design, not a contradiction" cases** | schema value — a list a tool reads | Without it, any conflict detector reports known-good classes forever (P14). Highest single value on this list. |
| **`MISSING` computation** | tool | Terms in notes without pages, pages without readings, sources nothing cites. The one check the old system could not express (P10). |
| **Manifest-against-disk comparison** | tool | Ten lines. It is the check whose absence defined the project's state (P8). |
| **Citation resolution** | tool | File exists, lines exist, quoted text is inside them (P12). **Normalise typographic quotes, apostrophes and dashes to ASCII and strip punctuation enclosing the fragment before comparing — measured: 40 of 46 reported errors were the checker's fault, not the writer's.** After that it must stay strict: character for character, empty fragments rejected, `Nichts-Rauschens` still fails against `Nichts-Rauschen`. |
| **A conflict record, keyed by subject and append-only** | tool + schema | One disagreement, one home, pointed at from every term page it touches. Measured: 2 of 7 conflicts in one live run were the same argument reached from two different concepts. Decision 003. |
| **A gather step proposes; it never resolves** | rule, then metric | A source that claims authority over other sources must not be granted it. Measured: one pipeline believed such a claim and silently dropped the concept out of its own contested count. Contested follows from a disagreement existing, never from its resolution. |

### Method, when the work reaches it

| idea | belongs in | what it is |
|---|---|---|
| **Authority ordering on conflict** | schema value, not prose | An explicit precedence list. The subtle part worth keeping: already-written prose wins on *details*, and the correct response is to report rather than rewrite. |
| **Research → canon as a traceable chain** | schema fields | real principle → what it claims about reality → the creative analogy → what it fills. `canon_status` records *that* something was checked, never *how* the bridge was built. |
| **"Derived or imported?"** | reference + review question | Does this description follow from the world's premises, or was it carried in from familiar context? Applies hardest to humans in unfamiliar settings. |
| **Layered dependency walkthrough** | skill | Check a design question against the layers in order rather than all at once. |
| **Content map before editing** | skill | Read the whole file, then emit sections with line ranges, named entities and a gap analysis, before changing anything. |
| **Planning duty above three files** | skill | Target files, verification criteria and dependency order before the first write. |
| **One entity per file; plan before writing** | tool + skill | Read the whole source, propose an extraction plan, write only after approval. Never summarise the source away. |
| **Three-tier gate ladder** | skill | Group checks by the maturity they attest — draft-ready, edit-ready, publish-ready — and report each separately (P11). |
| **Completeness checklist per artefact** | part tool, part judgement | Several items are already scripts; the rest are honest judgement and must be marked as such. |

### From outside, worth adopting

| idea | belongs in | what it is |
|---|---|---|
| **`FOUND` / `INFERRED` / `CONFLICTING` / `MISSING`** | tool (3 of 4) + skill | Already promoted to P10. This is where it came from. |
| **Anti-summary rule as a failure condition** | skill | *"If the output only says what each source said, it has failed."* A quality bar stated as a failure is enforceable by a reviewer; stated as an aspiration it is not. |
| **A provisional guess at what a document is for** | schema field, marked `provisional` | Commission, answer, or analysis of something else. **May not explain format or decide how a passage is read** — that was measured and refuted (decision 004). Its use is sequencing and routing: which document answers which, which commissions are still open. Removed once, and the removal is why `CLAUDE.md` now says a construct is demoted rather than deleted. |
| **`foundationality`, `whatThisChanges`, `limitations`** | schema fields | foundational / important / derivative / unclear; what this source changes about the reader's understanding; what it did **not** answer. The last feeds `MISSING` automatically. |
| **No empty placeholders** | tool | A directory or page exists only if it has members (P4). |
| **Stable ids that never renumber** | schema | Provenance that survives re-runs. The Graph's derived node ids already worked this way and it was the right call. |
| **`--trace` mode** | tool flag | Raw LM output kept aside for inspection, out of the main navigation. You cannot reduce a cost you cannot see. |
| **Two-pass discovery → reading** | skill | Separate finding sources from extracting from them; one agent per source, never one agent over many. |
| **Pre-flight check that stops with the exact remedy** | tool | Verify tooling before work rather than failing mid-run. Name the command that fixes it. |
| **Update mode that preserves prior work** | tool | Re-running rewrites only what the new evidence changed. |

### Retired deliberately

World and lore *generators* were dropped on purpose. This project does not need
generators; it needs derivation chains with an author checkpoint at each layer.
Anything that would invent rather than derive stays out.

---

## Claims and constructs are corrected differently

**Be quick to measure a claim and slow to remove a construct.** The full rule,
with the evidence on both sides, is under `Changing your mind` in `CLAUDE.md` —
it governs working method rather than what gets built, which is why it lives
there and is pointed at from here.

The short form: a claim about the repository or the corpus is measured or marked
unmeasured, and a measurement that contradicts it simply wins. A construct — a
field, a category, a folder — is not true or false, so an objection demotes it
(`provisional`, plus what it **may not** do, plus what would retire it) rather
than deleting it. Both failure modes are in this repository's history: a claim
that survived three learnings because nobody counted, and a construct deleted on
first objection.

## Changing this file

A principle is added when something has gone wrong twice, or gone right once in
a way worth repeating — and it is added with its evidence. A principle whose
evidence no longer holds is removed rather than left standing, because a rule
nobody believes teaches people to ignore the rest.
