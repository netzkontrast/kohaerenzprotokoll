# Worldbuilder Researcher — Persistent Memory

Auto-injected at startup (first 200 lines). Agent can read/write during execution.
Seeded 2026-09-15 from PROJECT_REFERENCES.md and the ingest manifests.

## Frequently Searched Terms
<!-- Agent: append term → file path(s) -->
- R-1 … R-10 hard rules → Canon/kohaerenz-protokoll_welt-sensorik-drafting_2026-06-10.md §10.1
- Master index of all locks → same file §12; Sprach-DNA hard rules → §12.7
- Hitze-Polarität (Ozon vs Wärme) → same file §2.1; Reveal timeline → §6.2
- 13 Alter + AEGIS voice + Mnemosyne → Canon/…anteile-profile-sprach-dna… §2–§5, §9
- Six levels (KW1–KW4, Überwelt, Externe Ebene) → Canon/…kernwelten-vollstaendig… §1.3
- DKT, Große Inversion, Truth-Rotation → Canon/…begriffe-und-konzepte… §1–§2
- Drafting decisions D-xx → Plan/drafting/decision-log_2026-09-11.md, decision-log_akt2-3_2026-09-11.md
- Chapter word budgets and density → docs/superpowers/specs/2026-09-12-chapter-enrichment-design.md

## Entity Location Index
<!-- Agent: append entity → primary file -->
- Kael (Host, Komponente 734) → anteile-profile §2 "Kael (Host)"; name first in prose Kap 9 (D-05)
- Lex / Alex / Rhys / Selene (ANPs) → anteile-profile §2; Nyx / Kiko / Lia / Isabelle / Moros (EPs) → §3
- Argus → §4; Silas (Juna-Echo) / Oblivion (AEGIS-Echo) → §5
- AEGIS → anteile-profile §9 + begriffe §5; Mnemosyne → §9; Erasure-Pol (name open) → §9
- Juna → begriffe §6 (cosmological constant, Witness function); prose appearance only Kap 38
- Doran → only named person besides Kael in Act I (drafting brief §3)
- Dekanonisiert (never active): Index, Nox, Echo, Flicker, Limina, Praetor, Eos, Elara, Aris,
  Mina, Lyra, Soren, Tariq, Nova, Sentinel; Guardians LogOS, Cerberus, Kairos, Sophia are names only
- Codex entries (602): Codex/GLOSSARY.md; slugs for the KW worlds: kw1-konstrukt-stadt,
  kw2-mnemosyne-archipel, kw3-cerberus-labyrinth, kw4-resonanz-kontinuum, ueberwelt, externe-ebene-koeln

## Effective Search Patterns
<!-- Agent: append use case → grep/find command -->
- Prose only (skip outline headers): `awk '/^# Kapitel /{p=1} p' <chapter.md> | grep -n "<term>"`
- Codex body by slug: `python3 -c "import sqlite3;c=sqlite3.connect('file:.agency/session.db?mode=ro',uri=True);print(c.execute(\"select p.value from node_props_text p join property_keys k on k.id=p.key_id where k.key='body' and p.node_id=(select p2.node_id from node_props_text p2 join property_keys k2 on k2.id=p2.key_id where k2.key='slug' and p2.value=?)\",('<slug>',)).fetchone()[0])"`
- Which chapters mention a term: `grep -l "<term>" Manuscript/works/*/works/*/kohärenz-protokoll/chapters/*.md`
- Lock index lines: `grep -n "^\*\*R-\|^[0-9]*\. Keine" Canon/*welt-sensorik*.md`
