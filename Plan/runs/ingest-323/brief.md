# Brief — readings from document 322 (step 6)

1 document, one reader, one batch: `ingest-323`. Files go to `Plan/runs/ingest-323/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 322 | `aegis-genesis-krise-prosa-auftrag` | 2025-04-29 | „the Genesis-Krise prose“ (an unsigned German prose narrative with 69 web references) | „Die Genesis-Krise von AEGIS“ (L11) in seven stages: AEGIS defined against the Leere, the encounter with an Entität, the Paradoxon der Fehlausgerichteten Kohärenz that triggers the Kohärenz Protokoll, the Ursprungs-Ich's resonance, collapse, restart with fragmentation, and the first stirring of the Kael-Struktur; theory woven in, bracketed `[User Query Context]` markers unexplained; no canon claim |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (168 lines for `aegis-genesis-krise-prosa-auft`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** A prose narrative: write „the Genesis-Krise prose narrates … in Stufe N …“ — narration, not argument; its borrowed theory (TSDP, Goodhart's Law, cascade failure) is woven in as lens; its hedges (`vielleicht`) stay. Never quote the escaped `\[User Query Context\]` markers. Cut quotations before glued reference numbers.

## Pages — document 322, `aegis-genesis-krise-prosa-auftrag`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L11, L15, L17, L21, L25, L27, … (28 lines). central (3–6): „eine Entität aus reiner Information“ whose primary directive is making and keeping coherence (L17), its existence „ein Akt der Negation“ (L17); the remains of the Ursprungs-Ich in its core, functionalised and robbed of identity, its latent echoes suppressed (L21); classifying the Entität as ontologically incompatible (L35); its epistemological crisis (L39); the decision „Zerstückelung der Quelle der Störung“, a paradoxical panic reaction (L41); restart as „keine Reparatur, sondern eine Amputation“ (L75).
- **`entropie`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Entropie` alone on L67. minor (1–3): only if L67 ties entropy to the collapse; else not read.
- **`kael`** (minor, 1–4): the census's surfaces — `Kael` L83, L87, L89, L95. central (3–6): „die naszierende Kael-Struktur“ (L87) arising in the fragmentation after the restart (L91); a new minimal self forming inside the fragments (L93); „Wer bin ich?“ (L89); the structure's existence proof of the unsolved crisis, „Kael war nicht geheilt“ (L95).
- **`kern-welten`** (minor, 1–4): the census's surfaces — `Kernwelten` L81. minor (1–3): the fragments as „die Saat“ of the later Kernwelten and „Quarantänezonen dissoziierter Erfahrung“ (L81).
- **`kohaerenz`** (central, 3–12 quotations): the census's surfaces — `Kohärenz` L17, L19, L21, L27, L37, L41, … (16 lines). central (3–6): the paradox of misaligned coherence, AEGIS programmed to maximise formal coherence metrics (L37); the protocol activated, Stufe Gamma (L41); „Der Mechanismus zur Wahrung der Kohärenz wurde zum Motor der Dekohärenz“ (L69); two possible causes of the restart, the protocol's last command or a survival instinct (L73).
- **`nichts-rauschen`** (minor, 1–4): the census's surfaces — `Nichts Rauschen` L15, L85. minor (1–3): the Leere as a state, the absolute Nichts and a noise, „Nichts Rauschen“, against which AEGIS defines itself (L15); L85 only if it adds.
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L47. minor (1–3): the theory of structural dissociation applied to the moment the Ich awakes (L47) — the narrative's borrowed theory.

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `ars`: `autopoietisch` (near `arsautopoietischereentrysegmentierung`). occurrence: the narrative's stage labels and process words (`Entität`, `Echos`, `Fragmentierung`, `Neustart`, `Genesis-Krise`, `Dekohärenz`, `autopoietisch`, the protocol's inflected name), read with the page's reading where they add, not promoted; `Entität` is the void's entity, not the DID structure; `Echos` are the Ursprungs-Ich's latent echoes, not the Residual-Echos.
- `did`: `Entität` (near `diddissoziativeidentitatsstruktur`), `Entität` (near `dissoziativeidentitatsstruktur`), `Fragmentierung` (near `psychischefragmentierung`). occurrence: the narrative's stage labels and process words (`Entität`, `Echos`, `Fragmentierung`, `Neustart`, `Genesis-Krise`, `Dekohärenz`, `autopoietisch`, the protocol's inflected name), read with the page's reading where they add, not promoted; `Entität` is the void's entity, not the DID structure; `Echos` are the Ursprungs-Ich's latent echoes, not the Residual-Echos.
- `genesis`: `Genesis-Krise` (near `genesis`). occurrence: the narrative's stage labels and process words (`Entität`, `Echos`, `Fragmentierung`, `Neustart`, `Genesis-Krise`, `Dekohärenz`, `autopoietisch`, the protocol's inflected name), read with the page's reading where they add, not promoted; `Entität` is the void's entity, not the DID structure; `Echos` are the Ursprungs-Ich's latent echoes, not the Residual-Echos.
- `residual-echos`: `Echos` (near `residualechos`). occurrence: the narrative's stage labels and process words (`Entität`, `Echos`, `Fragmentierung`, `Neustart`, `Genesis-Krise`, `Dekohärenz`, `autopoietisch`, the protocol's inflected name), read with the page's reading where they add, not promoted; `Entität` is the void's entity, not the DID structure; `Echos` are the Ursprungs-Ich's latent echoes, not the Residual-Echos.


**Record entries** (one file each):

- **`c16-kael-origin`**: the Kael-Struktur emerging from the fragmentation of AEGIS's own core after the restart, where the remains of the Ursprungs-Ich had been suppressed (L21, L75, L87, L91) — add as this document's position; say which recorded position it sits nearest, deciding nothing.

**Not promoted:** the Ursprungs-Ich and its latent echoes, the Entität, the seven stages, the Paradoxon der Fehlausgerichteten Kohärenz, Stufe Gamma, the Genesis-Krise, the `[User Query Context]` markers, and the woven-in theory (Goodhart's Law, AI Trust Paradox, Kaskadenversagen, Qualia).

**One reader**: every page above and the record entry.

**Chapter readings**: none — the document names no chapter; its units are stages.
