# Wiki structure contract

Use this decision table before creating a directory or moving a page.

| Content identity | Canonical promoted path | Partition source |
|---|---|---|
| One external research document | `Wiki/sources/<category>/<slug>.md` | `category` |
| One defined concept, entity, motif, rule, or model | `Wiki/concepts/<kind_detail>/<slug>.md` | `kind_detail` |
| One unresolved research or story question | `Wiki/questions/<axis>/<slug>.md` | `axis` |
| One cross-source synthesis | `Wiki/syntheses/<YYYY>/<slug>.md` | year from `created` |

Candidates mirror the same partition below
`Wiki/candidates/<kind-dir>/<partition>/<slug>.md`. Do not create folders for
themes, projects, people, workflow state, or convenience unless the schema is
first changed to make that dimension authoritative.

## Page boundary test

Keep material on one page only when all answers are yes:

1. Does it describe one semantic entity or one focused question?
2. Do all sections share the same lifecycle, ownership, and authority?
3. Would every inbound link reasonably need the whole page?
4. Is it below the hard word budget for its kind?
5. Can its context summary truthfully represent the entire page?

If any answer is no, split at the narrowest stable entity boundary. Copy no
claim without its citation. Add explicit links between the new pages and
repair every inbound `[[slug]]` reference. Never reuse the old slug for a
different semantic entity.

## Move protocol

1. Determine kind and partition from frontmatter.
2. Verify the target path mechanically from the schema.
3. Search the whole repository for the path and slug.
4. Move without changing the slug or factual body.
5. Repair path-based Markdown links; stable wiki links should remain valid.
6. Render navigation and confirm the old partition index disappears when empty.
7. Run structural lint and record the move in `Wiki/log.md` when the workflow
   requires an operation log entry.

## Contract-change protocol

Change these layers together: `Wiki/schema/*.yaml`, templates, parser/lint and
renderer code, tests, `Wiki/SCHEMA.md`, `Wiki/GLOSSARY.md`, and the compact
rules in `AGENTS.md`/`CLAUDE.md`. A directory appearing only in prose is not a
valid partition.

## Codex boundary

`Codex/**` is a generated projection from the provenance graph. Routine Wiki
maintenance may link to it or report defects, but must not reorganize it —
every file there is written by `scripts/render_codex_views.py`.

The Codex has its own contract, parallel to this one and stated in
`Graph/schema.yaml`:

| layer | holds |
|---|---|
| `Graph/nodes/*.jsonl` | the records — the source of truth |
| `Graph/schema.yaml` | the categories, the partition path, the always-on set, the window rule |
| `tools/kpcodex` | the implementation of those rules |
| `Codex/**` | the rendering, disposable and reproducible |

The partition dimension is `**Kategorie:**`, a value the records already carry;
the chapter window is computed from `triggers` on every run and never stored.
Nothing in the Codex is a hand-maintained topical folder, and a category that
is not declared in the schema renders into `Codex/entries/_misfiled/` so the
drift is visible.

Changing that structure means changing the schema, the tool and the tests
together, then re-rendering — the same atomic-contract discipline this document
requires of the Wiki. It is committed separately from Wiki maintenance.
