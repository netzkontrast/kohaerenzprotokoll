# 026 — A source from outside Drive: github.com/openai/math, landed as twelve documents

**Date:** 2026-10-07 · **Decided by:** the author (what), the session (how) · **Status:** in use, provisional

## What was asked

> Read https://github.com/openai/math and ingest it Completely - and Create for the Most important new found entities new Wiki Pages

## What was chosen

1. **The corpus takes its first source that is not from Drive.** `scripts/sources.py external` registers a row and lands a local copy
   (a clone or a download) through the same `write_document` as every Drive row. The external id goes into `drive_id`, because every
   later step reads provenance from that field; it has the form `github:<owner>/<repo>@<commit>/<path>` and is never a Drive id. The
   URL goes into a new field, `origin_url`. The route carries `provisional` / `may not` / `retire when` in the script.
2. **What counts as the repository's text.** The repository (commit `adc7f12`, 2026-10-06) holds 722 manuscripts in 372 result families:
   about 10 000 preprint files, a Lean library of about 123 000 files, an overview, a manuscript map and ten reasoning summaries.
   Twelve documents land, all `theorie-mathematik`, `T2-theory`:
   - the readme;
   - the manuscript map `CONTENTS.md`, which holds every manuscript's abstract and marks which families have a Lean formalization
     (its HTML table lines are dropped mechanically on landing);
   - the ten reasoning summaries, converted from PDF by markitdown.
3. **What does not land, and why.**
   - `overview.pdf`: 322 of its 362 family descriptions are near-identical to the manuscript map's.
   - The 722 preprints: specialist papers whose abstracts are all in the manuscript map. Reading them is not reading the repository
     „for the novel“; any one of them can land later by the same route.
   - The Lean library, and its 235 scope documents: code and per-family formalization detail. The manuscript map marks which
     families are formalized.
4. **Each document runs the whole ingest**, census to record, and the pages created for the collection's central entities hold its
   readings only, attributed and unmerged like every other page.

## What was rejected

- **Landing the repository whole, or every preprint.** Ten thousand specialist documents would outnumber the corpus seventeen to one,
  and nothing in them is about the novel.
- **A record in `Plan/runs/` without landing.** A page may only cite a landed document, so nothing could reach the wiki.

## What would change our mind

The author names a preprint or a Lean scope document to read, and it lands by the same route. A second external source makes the
`drive_id` field's name a lie twice; then a `source_id` field replaces it everywhere.
