export const meta = {
  name: 'blind-rereading',
  description: 'Independent blind re-readings of already-read documents, to measure how reproducible a candidate list is',
  whenToUse: 'Measuring how far two readings of one document agree. Pass args {readers, docs: [{slug, short, lines}]}. Write each returned list to Plan/runs/<slug>/03-candidates-blind-<n>.md (never 03-candidates.md), one `- term  ^[Lnn]` per line, then run `python3 scripts/agree.py <slug>`.',
  phases: [
    { title: 'Read', detail: 'two blind readers per document, following Plan/briefings/extract.md sections 0-2, returning the list instead of writing it' },
  ],
}

// Ran once, 2026-09-24, on documents 5, 6, 7 and 10, two readers each: 8 agents,
// 1,054,880 subagent tokens, 25 minutes at two agents at a time. The readers
// agreed with each other at F1 0.82-0.93 and each held 97-100 % of the committed
// list's content (Plan/learnings/extract-terms.md, *Blind re-readings*).
//
// The readers return their list; they write nothing, so a reading can never
// land in 03-candidates.md, the list the census counts. The session then wrote
// each to 03-candidates-blind-<n>.md with a written_by line, read_to_line,
// unread, contamination, and on_cited_line -- how many cited lines hold their
// term by entities.holds, which is code's number, not the reader's.
//
// Every reader reported the same contamination: CLAUDE.md, loaded into every
// session, describes the documents already read. No prompt can remove that.

const DOCS = args.docs
const READERS = args.readers

const SCHEMA = {
  type: 'object',
  properties: {
    read_to_line: { type: 'integer', description: 'the last file line you actually read' },
    last_line: { type: 'integer', description: 'the last file line of the document, as read.py numbers it' },
    unread: { type: 'array', items: { type: 'string' }, description: 'ranges or parts you did not read; empty if none' },
    what_this_document_is: { type: 'string', description: 'at most 120 words, noted before the list, as the briefing asks' },
    candidates: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          term: { type: 'string', description: 'the surface exactly as the document writes it' },
          line: { type: 'integer', description: 'file line of the first occurrence you saw' },
        },
        required: ['term', 'line'],
      },
    },
    contamination: { type: 'string', description: 'anything you saw about this document other than the three permitted sources; "none" if nothing' },
  },
  required: ['read_to_line', 'last_line', 'unread', 'what_this_document_is', 'candidates', 'contamination'],
}

function prompt(doc, r) {
  return `You are reader ${r + 1} of ${READERS} independent readers of one document. Do the reading step of this project's ingest for it, blind, and return the candidate list.

Document: \`${doc.slug}\` — \`Sources/drive/${doc.slug}.md\`, ${doc.lines} file lines.

## Blindness — the whole point of this run

- Read ONLY these, in this order: \`Plan/briefings/extract.md\`; \`Plan/runs/${doc.slug}/01-profile.txt\` and \`Plan/runs/${doc.slug}/02-probes.txt\`; then the document itself through \`python3 scripts/read.py ${doc.slug} --from A --to B\`.
- Do NOT open, list, grep or search anything else about this document or about the wiki: not \`03-candidates.md\` or any other file in \`Plan/runs/${doc.slug}/\`, not \`Sources/terms/\`, \`Sources/notes/\`, \`Wiki/\`, \`NOW.md\`, \`Plan/entities/\`, \`Plan/learnings/\`, \`Plan/concept/\`; no \`git log\` or \`git show\`; no qmd; no grep for the slug anywhere. If you see such content by accident, say exactly what in \`contamination\`.
- Write NO files anywhere, and do not run \`capture.py\` or any script other than \`read.py\`. The list is returned to the caller, not saved.

## The task

Follow the briefing's sections 0–2 only. Sections 3–5 (counting, verifying, recording) are not part of this run, and the commands in section 0 have already been run — their output is the two files you are permitted to read.

Read the whole document from line 1 to line ${doc.lines}, in ranges of about 150–200 lines, and build the candidate list **as you read** — a census lists every candidate term in one document, exhaustively. List each surface as the document writes it: keep variants, inflections, abbreviations and spelled-out forms as separate candidates, and do not normalise, translate or merge. Whether a candidate is really a term, and whether two surfaces are one thing, is decided later by other steps — not by you.

For each candidate give the file line of the first occurrence you saw, as \`read.py\` prints it. List only what you actually read on a line. Never reconstruct, never fill in from memory of what such documents usually contain. If you stop before the last line, set \`read_to_line\` honestly and name what you did not read in \`unread\` — an incomplete reading is a usable fact, a complete-looking reconstruction is not.`
}

phase('Read')
const jobs = []
for (const doc of DOCS) for (let r = 0; r < READERS; r++) jobs.push({ doc, r })
log(`${DOCS.length} documents x ${READERS} readers = ${jobs.length} blind readings`)
const results = await parallel(jobs.map(j => () =>
  agent(prompt(j.doc, j.r), { label: `read:${j.doc.short}:${j.r + 1}`, phase: 'Read', schema: SCHEMA })
    .then(res => ({ slug: j.doc.slug, reader: j.r + 1, result: res }))))
const missing = results.filter(x => !x || !x.result).length
if (missing) log(`${missing} readings returned nothing`)
return results.filter(Boolean)
