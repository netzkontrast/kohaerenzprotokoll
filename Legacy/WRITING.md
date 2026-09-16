---
name: "Kohärenz Protokoll Writing System"
description: "Machine-readable prose tokens for the German hard-SF novel; derived from Plan/drafting/drafting-brief.md, Canon welt-sensorik §2/§10/§11/§12 and the Anteile Sprach-DNA. Regenerate from those sources — never invent tokens."
generated-from:
  - Plan/drafting/drafting-brief.md
  - Canon/kohaerenz-protokoll_welt-sensorik-drafting_2026-06-10.md
  - Canon/kohaerenz-protokoll_anteile-profile-sprach-dna_2026-06-10.md
  - Canon/kohaerenz-protokoll_begriffe-und-konzepte_2026-06-10.md
last-synced: "2026-09-15"

languages:
  prose: de            # canon prose is German — never translate
  canon: de
  plans: de            # Plan/drafting is written in German
  engineering: en      # CLAUDE.md, scripts, skills, commit messages, PRs

document-types:
  chapter:
    dirs: ["Manuscript/works/*/works/*/kohärenz-protokoll/chapters"]
    voice: "1. Person Präsens (Kael, Hard-A) in Akt I; act-specific register thereafter"
    tense: present
    frontmatter: [type, author_slug, work_slug, created, status, chapter_number, title, pov, scene_refs]
    status-values: [outlined, drafted, revised, final]
    body-marker: "# Kapitel N — Titel"      # Kap 0: "# Kohärenz Protokoll — Kapitel 0 …"
    scene-break: "---"
    provenance-comment: "<!-- Draft vX.Y (YYYY-MM-DD). Plan: … · Entscheidungen: D-xx -->"
    directives: "**VERSALIEN**"
    logs: "fenced code block, fields per D-03 only"
    self-command: "_kursiv_ (Sensor-Rekalibrierung. Standardprotokoll.)"
    word-count: "plan value ±15 %; Akt I 1,600–2,300 (Kap 1 ≈ 2,500)"
  canon:
    dirs: ["Canon"]
    voice: "erläuternd / normativ; Werkbank, nicht Schaufenster"
    provenance-markers: ["[K] kanonisch", "[V] Vorschlag/offen", "[S] Steinbruch", "[L] Lücke"]
    normative-on-conflict: "Canon/kohaerenz-protokoll_storyform-und-outline_2026-06-10.md"
  plan:
    dirs: ["Plan/drafting", "Plan/encoding", "Plan/worldbuilding", "Plan/queries"]
    voice: "operativ; Entscheidungen als D-xx; [V] für revidierbare Wahl"
  codex:
    dirs: ["Codex"]
    generated: true
    source: ".agency/session.db via scripts/render_codex_views.py"
  dkt-substrate:
    dirs: ["Plan/worldbuilding"]
    voice: "third-person analytic; mechanism before name; never quoted in prose"

voice-per-act:
  kap-0: "Philosophical Horror; außerzeitlicher Rahmen; Vorwort 277 Wörter"
  akt-i: "Literary SF mit Horror-Anflug; sterile Welt, Uncanny Valley, Lem-Tonalität; kein Thriller-Pacing"
  akt-ii: "Technothriller-Kippe; Watts-Härte; keine Sentimentalität, keine frühe Resolution"
  akt-iii-a: "chorisches Drama / kosmische Konfrontation; Egan-Rigor, Tarkowski-Bildhaftigkeit"
  vortex-1: "metaphysischer Klimax; stille Mechanik, Soft-Layering, Dialetheia"
  kap-37: "trügerischer Pastoralismus; keine echte Resolution"
  vortex-2: "säkulare Apotheose; Wir-Pluralität, ketsu; keine Theorie-Predigt"
  kap-40: "Coda / geheilte Genesis; ambivalent-akzeptierend; kein Erläuterungs-Modus"

kael-akt-i:
  sentences: "kurz bis mittellang; Kommaketten nur wenn sie Routine tragen"
  grammar: "Welt positiv beschrieben; Negationsgrammatik nur wo etwas nicht stimmt"
  interiority: "nie direkt benannt — Körper, Zahlen, Zähl-Tic, Atem vier/sechs"
  time-jumps: "Absatz-Schnitt ohne Kommentar"
  metaphor: "Metaphernverbot in KW1; Vergleiche nur aus Kaels eigener Welt, konkret"
  humor: none
  irony-of-narrator: none

forbidden-phrases:
  everywhere:
    - "ich erinnere mich nicht"
    - "AEGIS ist, was AEGIS verhindert"        # R-9: Kap-0 marker, never literal outside Kap 0
    - "<speaker label>:"                        # voices are never labeled
  akt-i:                                        # Kap 1–13
    - "AEGIS"                                   # name never reader-side; ORDNUNGSPROTOKOLL / VERSALIEN-Direktive
    - "Alter"
    - "Anteil"
    - "Fragment"
    - "ANP"
    - "EP"
    - "TSDP"
    - "DID"
    - "System (for Kael)"
    - "Coheron"
    - "Erason"
    - "Landauer"
    - "Kohärenzfeld"
    - "Juna"                                    # never name, never subject, never body
    - "Kael (before Kap 9, D-05)"
    - "bewusstes Wir (before Kap 9)"
  aegis-voice:
    - "Ich"
    - "any metaphor"
    - "moral vocabulary"
    - "affective vocabulary"

diegetic-vocabulary-akt-i:
  - Konsolidierung
  - Ausgleich
  - Abweichung
  - Wartungsfenster
  - Bestand
  - Bestandspflege
  - Restwert
  - Ausnahme
  - Einheit          # other inhabitants are "Einheiten"; the only other name is Doran

hard-rules:
  R-1: "Tragische Ironie nie erklären"
  R-2: "Nie sagen, was der Leser denken soll (show, don't tell)"
  R-3: "Multiplizitäts-Schleier bis Kap 13; Wechsel nur über Syntax + Somatik + Vokabular"
  R-4: "max. 3 Stimmen-Mikrocues pro Bridge-Szene (Akt I sonst max. 2; Kap 2–5 max. 1)"
  R-5: "Kaltes Ozon (AEGIS) und Wärme (Juna, ab Kap 3) nie in derselben Szene — Ausnahme Vortex 1 Beat 4"
  R-6: "max. 1 Konzept pro Szene"
  R-7: "max. 1 Genesis-Echo pro Szene"
  R-8: "AEGIS ohne Metapher, Moral, Affekt; nie „Ich“"
  R-9: "Keine wörtlichen Zitate aus Kap 0"
  R-10: "Juna nie grammatisches Subjekt, nie Name, nie Stimme, nie Körper"

sprach-dna-hard-rules:
  Lex: "flucht nie, weint nie"
  Alex: "spricht nie über Gefühle in der ersten Person"
  Kiko: "ist nicht niedlich"
  Lia: "ist nicht launisch"
  Isabelle: "wird nicht gerettet"
  Moros: "ist nicht depressiv"
  AEGIS: "verwendet nie das Wort „Ich“; darf nicht metaphorisch sprechen"
  Mnemosyne: "darf metaphorisch sprechen"
  all: "Stimmen werden nie gelabelt — Erkennung nur durch Syntax + Lexikon + Somatik"

sensory-polarity:
  cold-ozone: "AEGIS-Unterdrückung / Landauer-Signatur — scharf, elektrisch, kalt-metallisch; ab Kap 1"
  warmth: "Junas Spur / Coheron-Verdrängung — hautwarm, quellenlos, Tiefenempfindung Brust; Debüt Kap 3"
  kw1-temperature: "konstant 21 °C; jede Abweichung ist Riss-Vorzeichen"

locked-spellings:
  - "Kohärenz Protokoll (title, two words, no hyphen); Kohärenzprotokoll = AEGIS' algorithm inside the story"
  - "AEGIS (all caps)"
  - "Kael (Host, Komponente 734 / Komp 734 / Einheit 734)"
  - "Juna"
  - "Doran"
  - "Lex · Alex · Rhys · Selene · Nyx · Kiko · Lia · Isabelle · Moros · Argus · Silas · Oblivion"
  - "Mnemosyne; Erasure-Pol (name still [L])"
  - "KW1 Konstrukt-Stadt / Logos-Prime"
  - "KW2 Mnemosyne-Archipel"
  - "KW3 Cerberus-Labyrinth"
  - "KW4 Kairos-Potentialis / Möglichkeits-Garten / Resonanz-Kontinuum"
  - "Überwelt; Externe Ebene (Köln 2026)"
  - "Coheron/Coheronen · Erason/Erasonen · K₀ · K₁ · DKT (Dual-Kernel-Theorie)"
  - "Datenknoten Epsilon; Station 11; ORDNUNGSPROTOKOLL; DIFFERENZ 1"
  - "Vortex 1 (Kap 35/36) · Vortex 2 (Kap 38/39) · Genesis (Kap 0) · Geheilte Genesis (Kap 40)"
  - "Sprach-DNA · Anteile · ANP / EP · Riss / Risse · Wir-Geflecht · Telefon-Stille"
  - "dekanonisiert (never active): Index, Nox, Echo, Flicker, Limina, Praetor, Eos, Elara, Aris, Mina, Lyra, Soren, Tariq, Nova, Sentinel; LogOS, Cerberus, Kairos, Sophia are names only"

citations:
  in-canon: "[K]/[V]/[S]/[L] provenance markers; source hierarchy per Canon storyform header"
  research: "[Author, Year] inline + ## References with one-sentence annotation (Plan/research, DKT docs)"
  claims: "capture_claim(text, source_uri, domain) — graph, not footnotes"

structure:
  chapter-header: "template header (bis einschließlich `## Outline …`) unverändert außer status/pov"
  contradiction-flag: "<!-- REVIEW: potential conflict with [file] --> (Plan/ only; never inside Canon)"
  decision-record: "Plan/drafting/decision-log*.md as D-xx; structural via record_storyform_decision"
  enrichment: "insert between paragraphs only; scripts/check_enrichment.py must pass"
  lint: "python3 scripts/lint_chapter.py <file> before declaring a chapter drafted"
---

# Kohärenz Protokoll — Writing System

Companion to `Plan/drafting/drafting-brief.md` (the operative instruction for
every chapter draft) and to Canon welt-sensorik §10 (R-rules, self-review
checklist) and §12 (lock index). The YAML tokens above are the machine-readable
projection of those sources for hooks, lints and the Worldbuilding-Codex
skills; the sources win on conflict.

## Chapter prose

German, first-person present in Act I, act-specific register thereafter (see
`voice-per-act`). Interior life is never named: it sits in the body, in
numbers, in the counting tic, in breath. Time jumps are paragraph cuts. Scene
breaks are a single `---` line. Directives appear bold in capitals, logs in
fenced code blocks with only the D-03 fields, Kael's self-command in italics.
Never fill to a word count; one scene more precisely beats one scene more.

## What never appears

The Act-I fences (`forbidden-phrases.akt-i`) keep the Multiplizitäts-Schleier
intact until chapter 13: no vocabulary of multiplicity, no DKT terminology, no
AEGIS name reader-side, no "Kael" before chapter 9, no Juna as name or subject
anywhere. `scripts/lint_chapter.py` enforces the decidable part of this list;
the semantic rules (R-1, R-2, R-6, R-7, register) need the scene-bridge-auditor
and a human read.

## Sensory discipline

Two thermal signatures, never mixed after chapter 1: cold ozone for
suppression, sourceless warmth for the trace that suppression cannot reach.
One dominant anomaly concept per scene, one Genesis echo at most, one sensory
Kernwelt anchor per beat. Metaphor is forbidden in KW1; when Kael compares,
he compares within his own world and concretely.

## Anti-patterns (from Kap-0 annotation, codex `concept · defect`)

Explained irony, narrator verdicts in AEGIS' position, metaphor or affect in
AEGIS' voice, meta-narrative asides about who is speaking, literal Genesis
quotes, theory surfacing as vocabulary. Self-audit every scene against the
§10.3 checklist: draft → audit → rewrite.

## Regeneration rule

When the drafting brief, the Canon lock index or the Sprach-DNA profiles
change, regenerate this file from them (the `/writing-style` skill). Do not
add a token here that the sources do not state; add it to the source first.
