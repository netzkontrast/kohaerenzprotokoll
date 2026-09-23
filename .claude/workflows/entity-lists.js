export const meta = {
  name: 'entity-lists',
  description: 'One Haiku reader per source file names its 50-100 most important entities; code places each line (entities.py place)',
  whenToUse: 'Building or refreshing per-document entity lists for scripts/entities.py. Pass the slugs as args; then run `python3 scripts/entities.py place <slug> Plan/entities/names/<slug>.json` per slug and `verify`.',
  phases: [{ title: 'Read', detail: 'one Haiku agent per Sources/drive file', model: 'haiku' }],
}

// Revision 3, 2026-09-23. Revision 1 let the model type line numbers: 94 of 374
// rows failed verification. Revision 2 asked it to copy each line from
// read.py --find instead: 2 of 4 lists verified, because Haiku still typed forms
// --find had refused, and one reader relabelled its old file instead of rereading.
// A prompt rule did not hold, so the rule is now structure (P26): the reader
// returns NAMES ONLY, into Plan/entities/names/<slug>.json, and
// `scripts/entities.py place` finds each name's first whole-word line and writes
// the list -- dropping and counting any name the document does not contain.
// A line a model never types cannot be wrong.

const SCHEMA = {
  type: 'object',
  properties: {
    slug: { type: 'string' },
    written: { type: 'boolean' },
    rows: { type: 'integer' },
    total_lines: { type: 'integer' },
    read_to_line: { type: 'integer' },
    note: { type: 'string' },
  },
  required: ['slug', 'written', 'rows', 'total_lines', 'read_to_line'],
}

const prompt = (slug) => `You read ONE German research document for a term wiki and list its most important entities.

The document: Sources/drive/${slug}.md (repository root is the current directory).

1. READ THE WHOLE FILE, to its last line. Use the Read tool with offset/limit in chunks until you have seen the final line; its line numbers are the file's line numbers. Do not stop early and do not summarise unread parts. Do not read other documents or search the corpus: this list describes this one document and nothing else.

2. Choose the 50-100 most important entities OF THIS DOCUMENT, most central first. An entity is a thing the document treats as a thing: a named person or character, a place, world or level, an organisation, a system, AI, protocol or programme, a coined term or concept of the world, a technology, an event, a work cited (book, film, paper, author), or a real-world concept the document builds on. NOT an entity: ordinary German vocabulary, repeated template field labels, markdown formatting, section numbers. A short document may have fewer than 50 — list fewer. Never pad.

3. Write each entity exactly as the document writes it: same spelling, case, hyphens, umlauts; no translation, no added article, no gloss or abbreviation in brackets after it. An abbreviation or variant the document uses for the same entity is its own entry, right after. Do NOT give line numbers — code finds the line, and drops any name the document does not contain word for word.

4. Write the names with the Write tool to Plan/entities/names/${slug}.json, as JSON and nothing else:

{"source": "${slug}", "written_by": "claude-haiku-4-5, one reader per document, via the entity-lists workflow (revision 3)", "total_lines": <total number of lines in the file>, "read_to_line": <the last line you actually read>, "entities": [{"term": "<entity>", "kind": "<kind>"}, ...]}

<kind> is one of: person, place, organisation, system, concept, technology, event, work, other. Most central first. If you did not read to the end, say so with read_to_line; a stated gap is useful, a list reconstructed from memory is not.

Write no other file. Return: slug, whether you wrote the file, how many entities, the file's total lines, the last line you actually read, and a one-line note only if something went wrong.`

phase('Read')
const slugs = Array.isArray(args) ? args : []
if (!slugs.length) throw new Error('pass the document slugs as args')
log(`${slugs.length} documents, one Haiku reader each`)
const results = await pipeline(slugs, (slug) =>
  agent(prompt(slug), { label: slug, phase: 'Read', model: 'haiku', effort: 'low', schema: SCHEMA }))
const done = results.filter(Boolean)
const failed = slugs.filter((s, i) => !results[i] || !results[i].written)
const partial = done.filter((r) => r.read_to_line < r.total_lines)
log(`${done.length} returned, ${failed.length} not written, ${partial.length} read partially`)
return {
  failed,
  partial: partial.map((r) => ({ slug: r.slug, read_to: r.read_to_line, of: r.total_lines })),
  place: done.filter((r) => r.written).map((r) => `python3 scripts/entities.py place ${r.slug} Plan/entities/names/${r.slug}.json`),
  notes: done.filter((r) => r.note).map((r) => ({ slug: r.slug, note: r.note })),
}
