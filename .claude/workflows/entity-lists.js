export const meta = {
  name: 'entity-lists',
  description: 'One Haiku reader per source file: its 50-100 most important entities, each line taken from read.py --find, written to Plan/entities/<slug>.md',
  whenToUse: 'Building or refreshing per-document entity lists for scripts/entities.py. Pass the slugs as args; verify with `python3 scripts/entities.py verify` afterwards.',
  phases: [{ title: 'Read', detail: 'one Haiku agent per Sources/drive file', model: 'haiku' }],
}

// Revision 2, 2026-09-23. Revision 1 (the pilot) let the model type line numbers:
// 94 of 374 rows failed verification -- 39 used a form the document never
// contains, 29 cited the wrong line, 26 were one to three lines off -- and one
// reader stopped at line 1200 of 2498 and called its coverage comprehensive.
// P26: ask for an identifier, never type one. Every line now comes from
// read.py --find, which refuses a form the document does not contain.
// NOT YET RE-PILOTED: run it on the four pilot slugs before the other 342.

const SCHEMA = {
  type: 'object',
  properties: {
    slug: { type: 'string' },
    written: { type: 'boolean' },
    rows: { type: 'integer' },
    total_lines: { type: 'integer' },
    read_to_line: { type: 'integer' },
    refused: { type: 'integer', description: 'entities read.py --find refused and you dropped or rewrote' },
    note: { type: 'string' },
  },
  required: ['slug', 'written', 'rows', 'total_lines', 'read_to_line', 'refused'],
}

const prompt = (slug) => `You read ONE German research document for a term wiki and list its most important entities.

The document: Sources/drive/${slug}.md (repository root is the current directory).

1. READ THE WHOLE FILE, to its last line. Use the Read tool with offset/limit in chunks until you have seen the final line; its line numbers are the file's line numbers. Do not stop early and do not summarise unread parts. Do not read other documents or search the corpus: this list describes this one document and nothing else.

2. Choose the 50-100 most important entities OF THIS DOCUMENT, most central first. An entity is a thing the document treats as a thing: a named person or character, a place, world or level, an organisation, a system, AI, protocol or programme, a coined term or concept of the world, a technology, an event, a work cited (book, film, paper, author), or a real-world concept the document builds on. NOT an entity: ordinary German vocabulary, repeated template field labels, markdown formatting, section numbers. A short document may have fewer than 50 — list fewer. Never pad.

3. NEVER TYPE A LINE NUMBER. For every entity run:
     python3 scripts/read.py ${slug} --find "<entity exactly as written>"
   It answers with one or more ^[Lnn] lines that really contain those words — use one of them. If it answers NOT IN THIS DOCUMENT, the form you wrote does not occur: use the exact form the document has (the nearest lines it prints help), or drop the entity. Count every refusal.
   Write each entity exactly as the document writes it: same spelling, case, hyphens, umlauts; no translation, no added article. An abbreviation or variant the document uses for the same entity is its own row, right after.

4. Write the list with the Write tool to Plan/entities/${slug}.md, in exactly this format and nothing else:

written_by: claude-haiku-4-5, one reader per document, via the entity-lists workflow (revision 2)
source: ${slug}
lines: <total number of lines in the file>

- <entity>  ^[L<line>]  · <kind>

<kind> is one of: person, place, organisation, system, concept, technology, event, work, other.
If any part of the file was not read, end with one line: - UNREAD <which lines and why>. A stated gap is useful; a list reconstructed from memory is not.

Write no other file. Return: slug, whether you wrote the file, rows, the file's total lines, the last line you actually read, how many entities --find refused, and a one-line note only if something went wrong.`

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
  refused: done.reduce((n, r) => n + (r.refused || 0), 0),
  notes: done.filter((r) => r.note).map((r) => ({ slug: r.slug, note: r.note })),
}
