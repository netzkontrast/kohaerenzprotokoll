# Canon — current Kohärenz Protokoll source documents (imported)

The latest canon working documents for the *Kohärenz Protokoll* novel,
fetched from Google Drive. Unlike `Legacy/` (a historical snapshot), this
folder tracks the **current** authoritative drafting corpus.

> The novel's canon prose is German — never translate canon prose.

## Provenance

- **Source:** Google Drive (via Drive MCP, exported as `text/markdown`)
- **Imported:** 2026-06-12
- **Selection rule:** the latest revision batch of `kohaerenz-protokoll_*.md`
  (all modified 2026-06-10), **excluding any political-context material**.
  A content scan (`politi|partei|regierung|demokrat|propaganda|ideolog|…`)
  confirmed all six documents are free of political content.
- **Normalization:** UTF-8 BOM stripped, CRLF → LF.

## Documents

| File | Role |
|---|---|
| `kohaerenz-protokoll_storyform-und-outline_2026-06-10.md` | **Normative** storyform + chapter outline. Wins on conflict. |
| `kohaerenz-protokoll_begriffe-und-konzepte_2026-06-10.md` | Explanatory companion: every term/concept, ordered from ontological ground up. |
| `kohaerenz-protokoll_kernwelten-vollstaendig_2026-06-10.md` | Complete Kernwelten (core worlds) reference. |
| `kohaerenz-protokoll_philosophie-im-detail_2026-06-10.md` | Philosophy strands in detail (incl. drafting discipline notes). |
| `kohaerenz-protokoll_welt-sensorik-drafting_2026-06-10.md` | World sensorics for drafting. |
| `kohaerenz-protokoll_anteile-profile-sprach-dna_2026-06-10.md` | System Kael: Anteile (parts) profiles + Sprach-DNA per alter. |

Provenance markers used inside the documents: `[K]` kanonisch · `[V]`
Vorschlag/offen · `[S]` aus Steinbruch · `[L]` Lücke.

## Re-import

Use `scripts/gdrive-fetch.sh` to decode Drive MCP download results without
routing file content through the model context — see the script header.
