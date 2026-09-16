# Wiki glossary

[Up](index.md)

This is the operational glossary for maintaining the research wiki. The
generated in-universe/domain glossary remains `Codex/GLOSSARY.md`.

| term | meaning |
|---|---|
| page | One Markdown file representing exactly one semantic entity or one focused question. |
| source | A cited digest of one ingested research document. Partition: `category`. |
| concept | A merged idea, character, world, rule, theory, motif, or storyform. Partition: `kind_detail`. |
| question | One unresolved uncertainty about the project. Partition: `axis`. |
| synthesis | A filed answer drawing on at least three wiki pages. Partition: filing year. |
| candidate | Machine-drafted page awaiting human review; it is not yet part of the promoted wiki. |
| partition | The single required subdirectory below a page-kind directory. It is derived from frontmatter, never chosen ad hoc. |
| local index | A rendered `README.md` listing the partitions or pages directly below its directory. |
| global index | `Wiki/index.md`, the short entry page linking to local indexes and global views. |
| concept table | A rendered one-row-per-concept overview; it is not a place for prose. |
| status | Review lifecycle of a page (`draft`, `reviewed`, `contested`, `superseded`, `archived`) or question state. |
| wiki link | `[[slug]]`; slugs are globally unique even though files live in partitions. |
| terminal reference | `codex:<slug>` or `canon:<file>#<heading>`; it receives no reverse wiki link. |
| page budget | Ideal, warning, and hard maximum word counts defined per page kind in `schema/entities.yaml`. |
| split | Replacing an oversized mixed page with focused pages connected by explicit wiki links and preserved citations. |
| stale index | A rendered `README.md` that no longer corresponds to an occupied partition; `index-sync` rejects it. |
