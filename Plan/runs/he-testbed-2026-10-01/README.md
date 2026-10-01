# HyperExtract testbed — every contract on two small documents, Sonnet

**2026-10-01.** On the author's „Erstelle für jedes hyperextract Template eine Datei mit allen Ergebnissen aus zwei kleinen
Test-sources - nutze sonnet agents für diese Tests", as the first fixture set of step 1b in `docs/README.md` (§3). Sonnet
through `claude -p` (decision 011), on the port (`hx.py`, decision 020), **one run at a time** (`run.sh`).

| | |
|---|---|
| A | `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik` — 4.2 KB, theory, German; 3 chunks; the Haiku pilot of 2026-09-30 ran eleven contracts on it |
| B | `2026-09-14-kap25-vertiefung-md` — 10.4 KB, a chapter outline, German; 8 chunks |
| runs | 64 (32 contracts × 2), 352 calls, **0 failed**, every chunk answered with a valid reply at the first attempt; 43 minutes of model time; **$6.86** |
| results | `results/README.md` — the table of all 32; `results/<Contract>.md` (to read) and `.jsonl` (to compute on), every row of both documents |

`results.py` rebuilds the files from the run directories `Plan/runs/<doc>/hyperextract/<contract>-sonnet-2026-10-01/`. Each
run keeps `raw.json` — the merged data as the model returned it — so a run staging refused as a whole is still readable.

## What it shows — before anyone has labelled a row

No row here is labelled `ok`/`part`/`wrong` yet; everything below is counted, not judged.

1. **Sonnet answered every chunk in the schema.** 352 of 352 replies validated the first time; the Haiku runs needed the
   German-quotation repair and retries (`he_claude.parse_json`). The price is about twice Haiku's per megabyte (A: $0.05–0.07 a
   contract for 4.2 KB).
2. **The two models find different lines.** On document A, where the Haiku pilot ran nine of the same contracts, the
   candidates of the two stand on mostly different lines: `TermReadings` 17 lines (Sonnet) and 4 (Haiku), 3 shared;
   `ThemeMotifs` 5 and 4, 3 shared; `Anchors` 0 and 6 (Haiku's `Anchors` rows were 20 % `ok` when labelled); `TermTaxonomy`
   0 and 7 (43 % `ok`). Which model is right is a labelling question; that they differ this much says a single run of either is
   one reading, not the document's content.
3. **The staging gate refuses right-looking rows of numbers and of emphasised text.** Of 68 refused rows, 29 are refused for a
   name „absent from the document" whose quotation was placed: `1.137 Wörtern` (the document writes `**1.137 Wörtern**`),
   `1.141`, `34`, `41`, `02:10–02:14`, titles with inner quotation marks. Markdown emphasis and numbers defeat
   `reading_extract.stands` as three-letter names did before (graph-contracts §4.1). That is a defect of the gate, for
   `Quantities` above all, and the `text` part of the document schema (`docs/README.md` §2.2) is where it belongs: a match
   runs on a line with its markup removed. Not fixed here; the other refusals are 25 quotations not placed, 12 joined or
   shortened, 2 ambiguous.
4. **Two contracts return a shape staging does not take.** `TermCensus` (18 and 122 rows) and `LocationRegistry` (12) are
   *set* templates whose rows carry no quotation field staging knows; they are shown as given (`n.s.`), with a line where a
   quotation could be placed. A census-like list of 122 terms for an outline is worth comparing with the document's gold
   candidate list (`goldeval.py`).
5. **The outline is where most contracts find something.** On B: `RelationReadings` 97 rows, `TermReadings` 70, `Quantities`
   39, `StatedRelations` 27, `ChapterBeats` 23, `EntityFacts` and `ProseRules` 17 each. On the theory document A, ten runs
   returned nothing — `Anchors`, `LocationRegistry`, `Locks`, `OpenPoints`, `Pitch`, `Precedence`, `StandingClaims`,
   `Storypoints`, `TermTaxonomy` and `Analogies` (one row, refused) — which is what a contract of the wrong kind should do.

## What comes next

- **Label** a sample per contract (`hegraph.py`'s labels file, hash-drawn rows), so the precisions of graph-contracts §4.2 get a
  Sonnet column; without labels nothing here says which contract belongs in step 1b.
- **Score** `TermCensus` and the readings against the two documents' gold candidate lists (`goldeval.py`).
- **Fix the gate** for markup and numbers, measured on these 29 rows (a selftest case each), then re-stage — staging is free.
- **Update-ingest**: these runs are the fixed point; when a contract or the document schema's `text` part changes, a re-stage
  of the same `raw.json` shows exactly which rows move.
