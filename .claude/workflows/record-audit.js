export const meta = {
  name: 'record-audit',
  description: 'Audit how faithfully the conflict and question records hold what a document says, with two-lens adversarial verification of each finding',
  whenToUse: 'After a document is reconciled, or for documents read before ingest step 6. Pass args {docs: [{n, slug, lines, record}]}, record being its Wiki/compare/reconcile-NN-<slug>.md. Findings are proposals: which enter a record is decided by the rule in Plan/runs/record-audit-2026-09-24/README.md, and every citation is re-asked of read.py --find.',
  phases: [
    { title: 'Audit', detail: 'one auditor per document: every attribution checked against the text, then the whole document read for what the records miss' },
    { title: 'Verify', detail: 'two skeptics per document, one checking the text, one checking whether each finding matters' },
  ],
}

// Ran once, 2026-09-24, on documents 7-13: 21 agents, 3,725,408 subagent
// tokens, 65 minutes at two agents at a time. 274 of 289 attributions faithful;
// of 83 findings both skeptics upheld 9, one upheld 30, neither 44
// (Plan/runs/record-audit-2026-09-24/, audit.json and README.md).
//
// What that run taught: an auditor that reads only the records overcounts what
// is missing, because a record does not repeat what a page it links already
// quotes. The text skeptic is told to look in those pages too. Nothing here
// writes to the wiki; conflict detection stays a reading, never a mechanism.

const DOCS = args.docs

const AUDIT = {
  type: 'object',
  properties: {
    read_to_line: { type: 'integer' },
    last_line: { type: 'integer' },
    attributions_checked: {
      type: 'array',
      description: 'every statement in a conflict or question record that attributes something to this document',
      items: {
        type: 'object',
        properties: {
          record: { type: 'string', description: 'file name, e.g. c8-aegis-approach-storyform-b.md' },
          record_line: { type: 'integer', description: 'line in the record file where the attribution stands' },
          record_says: { type: 'string', description: 'what the record attributes to this document, in its words' },
          verdict: { type: 'string', enum: ['faithful', 'distorted', 'unsupported'] },
          doc_line: { type: 'integer', description: 'the document line that decides it, from read.py --find' },
          doc_quote: { type: 'string', description: 'the document words at that line, verbatim' },
          explanation: { type: 'string' },
        },
        required: ['record', 'record_line', 'record_says', 'verdict', 'doc_line', 'doc_quote', 'explanation'],
      },
    },
    misses: {
      type: 'array',
      description: 'passages where the document speaks to a record subject and no record holds it',
      items: {
        type: 'object',
        properties: {
          record: { type: 'string', description: 'the record whose subject this is' },
          kind: { type: 'string', enum: ['position', 'relation', 'contradiction', 'self-contradiction'] },
          doc_line: { type: 'integer', description: 'from read.py --find' },
          doc_quote: { type: 'string', description: 'verbatim' },
          what_it_says: { type: 'string' },
          why_it_matters: { type: 'string' },
          nearest_record_citation: { type: 'string', description: 'the closest thing the record already holds from this document, or "none"' },
        },
        required: ['record', 'kind', 'doc_line', 'doc_quote', 'what_it_says', 'why_it_matters', 'nearest_record_citation'],
      },
    },
    notes: { type: 'string' },
  },
  required: ['read_to_line', 'last_line', 'attributions_checked', 'misses', 'notes'],
}

const VERDICTS = {
  type: 'object',
  properties: {
    verdicts: {
      type: 'array',
      items: {
        type: 'object',
        properties: {
          id: { type: 'string' },
          refuted: { type: 'boolean' },
          reason: { type: 'string' },
        },
        required: ['id', 'refuted', 'reason'],
      },
    },
  },
  required: ['verdicts'],
}

const RULES = `You report; you change nothing. Write no files and run nothing that writes — \`cat\`, \`ls\`, \`grep\` and \`python3 scripts/read.py\` are what you need.`

function auditPrompt(d) {
  return `Audit how faithfully the wiki's conflict and question records hold what ONE document says. ${RULES}

Document: \`${d.slug}\` — ${d.lines} file lines, read as document ${d.n} on 2026-09-24. Its reconciliation record is \`Wiki/compare/${d.record}\`.
Records: the conflict records in \`Wiki/conflicts/\` (C1–C12) and the question records in \`Wiki/questions/\` (Q1–Q5; skip README.md). Canon prose is German; quote it verbatim, never translate it.

1. Read every record, then the reconciliation record.

2. PART A — what the records say about this document. Find every statement in a record that attributes something to this document: it names \`${d.slug}\`, cites \`^[${d.slug}.md:Lnn]\`, or is a table row naming it. For each, read the cited lines with context (\`python3 scripts/read.py ${d.slug} --from A --to B\`) and judge:
   - \`faithful\` — the document says this, in this sense, at that place;
   - \`distorted\` — the document says something there, but the record's paraphrase or position shifts its meaning: a hedge dropped, a proposal read as a fact, a role or column swapped, a count or chapter wrong, a qualifier lost;
   - \`unsupported\` — the document does not say it there or anywhere near.
   Check every one; list the faithful ones too, briefly. A record's own observation about two texts is an attribution only where it claims something about this one.

3. PART B — what the document says that the records miss. Read the whole document, line 1 to ${d.lines}, in ranges of about 200 lines. For each record's subject, look for passages that take a position on it, relate or explain the positions, or contradict a position a record lists — and check whether a record already holds that passage (cites that line or one within a few lines of it, or states the same point attributed to this document). Report only passages no record holds. Also report a place where this document contradicts itself on a record's subject. Do not report a passage that merely mentions the subject, or restates a position the record already lists for this same document.

For every quotation, get the line from \`python3 scripts/read.py ${d.slug} --find "<exact words>"\` — never type a line number yourself. Be concrete and conservative: every finding will be checked by a skeptic, and one that the record holds somewhere you missed counts against you.`
}

function findings(audit, d) {
  const out = []
  audit.attributions_checked.forEach((a, i) => {
    if (a.verdict !== 'faithful') out.push({ id: `${d.n}-A${i + 1}`, type: 'attribution', ...a })
  })
  audit.misses.forEach((m, i) => out.push({ id: `${d.n}-M${i + 1}`, type: 'miss', ...m }))
  return out
}

const LENSES = [
  { key: 'text', ask: `the TEXT lens. For each finding: (1) is the quoted wording really at that document line? Run \`python3 scripts/read.py SLUG --find "<words>"\` and read the surrounding lines. (2) For a \`miss\`: does any record — or a page the record links, via \`grep -rn "SLUG" Wiki/\` — already hold this passage or this point from this document? If so it is refuted. (3) For an \`attribution\` finding: re-read the record line and the document lines yourself — is the record's statement really distorted or unsupported, or did the auditor misread the table, the column, or the section?` },
  { key: 'matters', ask: `the MATERIALITY lens. For each finding decide whether it matters to the record's question as the author would read it: a \`miss\` must be a position, a relation between positions, or a contradiction — not a mention, not a restatement of a position the record already lists for this same document, not a detail the record's question does not ask about. An \`attribution\` finding must change what the author would conclude from the record; a harmless paraphrase or a rounding is refuted.` },
]

function verifyPrompt(d, fs, lens) {
  return `You are a skeptic. Another agent audited the wiki's conflict and question records (\`Wiki/conflicts/\`, \`Wiki/questions/\`) against document \`${d.slug}\` (${d.lines} lines) and reports the findings below. Try to REFUTE each one, through ${lens.ask.replace(/SLUG/g, d.slug)}

Default to refuted=true when you are uncertain. Return one verdict per finding id, with a short reason naming what you checked. ${RULES}

Findings:
${JSON.stringify(fs, null, 1)}`
}

const results = await pipeline(
  DOCS,
  d => agent(auditPrompt(d), { label: `audit:doc${d.n}`, phase: 'Audit', schema: AUDIT }),
  (audit, d) => {
    if (!audit) return { doc: d, audit: null, findings: [], verdicts: {} }
    const fs = findings(audit, d)
    if (!fs.length) { log(`doc${d.n}: no findings to verify`); return { doc: d, audit, findings: fs, verdicts: {} } }
    log(`doc${d.n}: ${fs.length} findings to verify`)
    return parallel(LENSES.map(lens => () =>
      agent(verifyPrompt(d, fs, lens), { label: `verify:doc${d.n}:${lens.key}`, phase: 'Verify', schema: VERDICTS })
        .then(v => ({ lens: lens.key, v }))))
      .then(vs => {
        const verdicts = {}
        for (const x of vs.filter(Boolean)) verdicts[x.lens] = x.v ? x.v.verdicts : null
        return { doc: d, audit, findings: fs, verdicts }
      })
  },
)
return results.filter(Boolean)
