# 001 — Reset to two layers, wiki first

**Date:** 2026-09-16 · **Decided by:** the author · **Status:** done

## What was chosen

The project resets to two layers — `Sources/` and `Wiki/` — and builds a wiki of
its own terms from the research documents. The novel rests. Everything else moves
to `Legacy/`, read by nothing.

`Canon/` loses its normative status and is parked rather than deleted.
`Manuscript/` is parked with it; its prose does not continue.

## What was rejected, and why

**Keeping the five layers.** Measured, three of them were not carrying their
weight: `Wiki/` held 2 promoted pages against 56 candidates, `Sources/` held 26
of 680 documents, and `Canon/` was already not the live source of `Graph/` —
`ingest_canon.py` reads frozen manifests and never opens a Canon file. Each layer
was another place for one fact to be stated differently.

**Deleting `Canon/` outright**, which was the author's first instruction. A
verification pass found it is not covered by the Codex: two of eight documents
have verbatim twins in `Sources/`, six do not, the worst at 30 %. All 223 claim
records point into `Canon/`, and the provenance gate compares string prefixes
without touching the filesystem — so deleting it would leave every check green
while every claim cited a file that was gone. Parking costs nothing and keeps the
content readable, which git history does not, because tools do not read git.

**Keeping the existing wiki machinery.** Five page types, 26 lint rules, three
DSPy programs and a schema across five YAML files had produced two pages. The
schema was written before anyone knew what a page needed to hold.

## What would change our mind

- If the term wiki turns out not to answer the questions actually asked of it —
  if most questions are about chapters and plot rather than terms, the unit is
  wrong and this reset picked the wrong axis.
- If parking `Canon/` proves insufficient because its content is needed daily,
  it comes back as sources rather than as a layer.

## Consequences

`backup/pre-restart-2026-09-16` holds the whole tree at `608cbb5`. `CLAUDE.md`
now describes two layers and nothing else. The archive is enforced as a shelf by
a deny rule on `Write(Legacy/**)`, not only by convention.
