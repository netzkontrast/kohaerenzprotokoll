---
source: Sources/drive/narrativ.md
drive_id: "19_w81TDNrwXpUloP_dU5dtX-4WsEcnvtYoRcwkD8XDg"
title: "Narrativ"
category: plot-outline
index_date: "2025-07-30"
extracted: "2026-10-07"
candidates: 96    # the terms capture.py counted
---

# Term census — Narrativ

> **This file describes one document and nothing else.** No count, comparison or
> expectation from any other source appears here. Comparing documents is a
> separate step, and mixing the two is what lets a term look unimportant in the
> document where it conflicts.

## Structural profile

`python3 scripts/profile.py narrativ`

```
  lines                239  (frontmatter ends at 9)
  body words           3947
  headings             15   bold-only lines 1
  table rows           0   code fences 0
  question marks       0
  backslash escapes    2
  typographic marks    21   ascii quotes 134
  invisible characters none
  math symbol lines    0
  glued ref numbers    1
  repeated labels      none
  longest line         855 chars
```

## Stance, read per passage

The file holds two texts one after the other, each in its own voice and with its own address to a reader.

**L11 to L112, a craft compendium.** The first voice names itself „Als Narrativer Architekt ist es meine vorrangige Aufgabe“ ^[L11], and its heading calls the text „Ein Operatives Kompendium“ ^[L13]. It is written as a plan of techniques in six numbered sections (L17, L38, L55, L68, L80, L101), and it gives sample prose marked by „Zum Beispiel“ ^[L24] and „Beispiel“ with a sentence in italics ^[L35]. Those sample sentences are diction in the voice of a part or of AEGIS, not statements about the world.

**L113, a closing line of the first text.** „Dieser detaillierte Bauplan legt die notwendige Tiefe und Struktur fest“ ^[L113] ends the compendium.

**L115 to L238, a synthesis addressed to colleagues.** The second voice opens „Sehr geehrte Kollegen der narrativen Architektur“ ^[L115] and says of itself „Als Ihr Konzept-Dramaturg ist es meine primäre Aufgabe“ ^[L117]. It claims its own standing: „Dieses Dokument dient als unser oberstes Architekturdokument“ ^[L117]. That is the document's claim about itself, recorded and not applied. Its sections are numbered I to VII in Roman numerals (L123 to L232).

**L123 to L184, a description of the novel's world.** Plain declarative statements about AEGIS, System Kael, the Fundament, Juna/V and the worlds, with protocol names marked in bold followed by a gloss (L131 to L137). Where it recommends rather than states, it says so: „Die Anwendung von Kishōtenketsu wird als zentrales, tragendes Gerüst empfohlen“ ^[L197].

**L186 to L220, methods and tools,** and **L222 to L230, principles** are plans for the writing, not reports about the story.

**L232 to L238, status.** The text says of the project „ist konzeptionell außergewöhnlich stark, originell und thematisch tiefgründig“ ^[L234] and „Der Bauplan steht“ ^[L236]. There is no passage marked as a question and no lock or date.

## Candidates and counts

96 candidates, written while reading and frozen by the count (`Plan/runs/narrativ/03-candidates.md`, counted by `capture.py --count`). `word` is the term standing alone (no letter, digit or hyphen on either side, case-sensitive) and is also a count mark that `quotes.py` checks against the body; `in` is anywhere, compounds included; `lines` are the file lines that hold the term as a substring. The list is in order of first appearance. `narrativ.md` in a mark is this document. Rows written by `census.py draft`.

### As the document names them

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Narrativer Architekt` ^[narrativ.md:#1] | 1 | 1 | 11 |  |
| `Kohärenz Protokoll` ^[narrativ.md:#7] | 7 | 7 | 11, 15, 117, 119, 121, 190, 234 |  |
| `Kael` ^[narrativ.md:#15] | 15 | 43 | 17, 19, 23, 25, 57, 61, 62, 63, 66, 73, 76, 86 … | `Kaels` ×28 |
| `System Kael` ^[narrativ.md:#2] | 2 | 2 | 63, 143 |  |
| `AEGIS` ^[narrativ.md:#37] | 37 | 39 | 38, 40, 42, 48, 52, 53, 57, 61, 87, 113, 123, 125 … | `AEGIS-Protokoll` ×1, `AEGIS-Netzwerk` ×1 |
| `Autonomous Epistemic Guardian for Integrity Systems` ^[narrativ.md:#1] | 1 | 1 | 125 |  |
| `Dissoziative Identitätsstörung` ^[narrativ.md:#1] | 1 | 1 | 19 |  |
| `DID` ^[narrativ.md:#4] | 4 | 4 | 19, 70, 72, 227 |  |
| `TSDP` ^[narrativ.md:#1] | 1 | 2 | 19, 145 | `TSDP-Modell` ×1 |
| `Tertiäre Strukturelle Dissoziation` ^[narrativ.md:#1] | 1 | 1 | 145 |  |
| `funktionale Multiplizität` ^[narrativ.md:#1] | 1 | 1 | 19 |  |
| `ANP` ^[narrativ.md:#2] | 2 | 3 | 21, 151, 153 |  |
| `Anscheinend Normaler Persönlichkeitsanteil` ^[narrativ.md:#1] | 1 | 1 | 151 |  |
| `EP` ^[narrativ.md:#2] | 2 | 4 | 24, 154, 155 |  |
| `Emotionaler Persönlichkeitsanteil` ^[narrativ.md:#1] | 1 | 1 | 154 |  |
| `Host` ^[narrativ.md:#1] | 1 | 1 | 151 |  |
| `Selene` ^[narrativ.md:#1] | 1 | 1 | 152 |  |
| `Lex` ^[narrativ.md:#4] | 4 | 4 | 35, 36, 153, 177 |  |
| `Nyx` ^[narrativ.md:#4] | 4 | 4 | 24, 35, 154 |  |
| `Kiko` ^[narrativ.md:#3] | 3 | 4 | 35, 36, 155 | `Kikos` ×1 |
| `ISH` ^[narrativ.md:#1] | 1 | 1 | 152 |  |
| `Innere Helferin` ^[narrativ.md:#1] | 1 | 1 | 152 |  |
| `Torwächter` ^[narrativ.md:#1] | 1 | 1 | 152 |  |
| `Juna/V` ^[narrativ.md:#5] | 5 | 8 | 161, 167, 182, 194, 195, 201, 208 | `Juna/V-Verbindung` ×3 |
| `Fragment 'O'` ^[narrativ.md:#1] | 1 | 1 | 159 |  |
| `Fundament` ^[narrativ.md:#3] | 3 | 6 | 15, 121, 161, 163, 165 | `Fundamente` ×2, `fundamental` ×1, `Fundaments` ×1, `fundamentalen` ×1 |
| `Paraiyas` ^[narrativ.md:#1] | 1 | 1 | 163 |  |
| `Kernwelten` ^[narrativ.md:#7] | 7 | 7 | 55, 57, 59, 137, 169, 175, 180 |  |
| `KW1` ^[narrativ.md:#3] | 3 | 4 | 61, 175, 177, 236 |  |
| `KW2` ^[narrativ.md:#2] | 2 | 2 | 62, 178 |  |
| `KW3` ^[narrativ.md:#2] | 2 | 2 | 63, 179 |  |
| `KW4` ^[narrativ.md:#2] | 2 | 2 | 64, 180 |  |
| `Logos-Prime` ^[narrativ.md:#1] | 1 | 1 | 61 |  |
| `Mnemosyne-Archipel` ^[narrativ.md:#2] | 2 | 2 | 62, 178 |  |
| `Cerberus-Labyrinth` ^[narrativ.md:#2] | 2 | 2 | 63, 179 |  |
| `Kairos-Potentialis` ^[narrativ.md:#2] | 2 | 2 | 64, 180 |  |
| `Konstrukt-Stadt` ^[narrativ.md:#2] | 2 | 2 | 177, 236 |  |
| `Digitale Überwelt` ^[narrativ.md:#2] | 2 | 2 | 171, 181 |  |
| `Realitätsebenen` ^[narrativ.md:#3] | 3 | 3 | 169, 173, 175 |  |
| `Externe Ebene` ^[narrativ.md:#1] | 1 | 1 | 182 |  |
| `Risse` ^[narrativ.md:#6] | 6 | 6 | 65, 139, 177, 184, 236 |  |
| `Entropie` ^[narrativ.md:#4] | 4 | 6 | 65, 136, 139, 184 | `Entropie-Manifestationen` ×2 |
| `Entropie-Manifestationen` ^[narrativ.md:#2] | 2 | 2 | 65, 184 |  |
| `Guardians` ^[narrativ.md:#1] | 1 | 1 | 181 |  |
| `Zero Trust Environment Mandate` ^[narrativ.md:#1] | 1 | 1 | 131 |  |
| `ZTEM` ^[narrativ.md:#1] | 1 | 1 | 131 |  |
| `Recursive Trust Signature Verification` ^[narrativ.md:#1] | 1 | 1 | 132 |  |
| `RTSV` ^[narrativ.md:#1] | 1 | 1 | 132 |  |
| `Boundary Protocol of Failure` ^[narrativ.md:#1] | 1 | 1 | 133 |  |
| `BPoF` ^[narrativ.md:#1] | 1 | 1 | 133 |  |
| `Emergent Information Consensus` ^[narrativ.md:#1] | 1 | 1 | 134 |  |
| `EIC` ^[narrativ.md:#1] | 1 | 1 | 134 |  |
| `Integrity Validation` ^[narrativ.md:#1] | 1 | 1 | 135 |  |
| `Entropic Management` ^[narrativ.md:#1] | 1 | 1 | 136 |  |
| `Systemic Isolation Shield` ^[narrativ.md:#1] | 1 | 1 | 137 |  |
| `SIS` ^[narrativ.md:#1] | 1 | 1 | 137 |  |
| `Kernprotokolle` ^[narrativ.md:#1] | 1 | 1 | 129 |  |
| `Paradoxon X` ^[narrativ.md:#1] | 1 | 1 | 139 |  |
| `universal reboot` ^[narrativ.md:#1] | 1 | 1 | 139 |  |
| `externalisiertes Täterintrojekt` ^[narrativ.md:#1] | 1 | 1 | 141 |  |
| `Gaslighting` ^[narrativ.md:#1] | 1 | 1 | 141 |  |
| `Value-Alignment-Versagen` ^[narrativ.md:#1] | 1 | 1 | 139 |  |
| `MESI-Protokoll` ^[narrativ.md:#1] | 1 | 1 | 180 |  |
| `Cache Kohärenz` ^[narrativ.md:#1] | 1 | 1 | 151 |  |
| `Manifest-Säulen` ^[narrativ.md:#1] | 1 | 1 | 175 |  |
| `Algorithmic Horror` ^[narrativ.md:#3] | 3 | 3 | 40, 47, 61 |  |
| `algorithmische Melancholie` ^[narrativ.md:#1] | 1 | 1 | 51 |  |
| `epistemologische Landschaften` ^[narrativ.md:#1] | 1 | 1 | 57 |  |
| `Gärtner` ^[narrativ.md:#1] | 1 | 2 | 229 | `Gärtners` ×1 |
| `Resonanz` ^[narrativ.md:#5] | 5 | 5 | 113, 117, 167, 226 |  |
| `Orchestriertes Bewusstsein` ^[narrativ.md:#1] | 1 | 1 | 35 |  |
| `Meta-Erzähler` ^[narrativ.md:#1] | 1 | 2 | 76, 77 | `Meta-Erzählers` ×1 |
| `Ethische Rückkopplungsschleife` ^[narrativ.md:#1] | 1 | 1 | 76 |  |
| `Vulnerable Narration` ^[narrativ.md:#1] | 1 | 1 | 77 |  |
| `Prosa der Dissonanz` ^[narrativ.md:#1] | 1 | 1 | 204 |  |
| `Kishōtenketsu` ^[narrativ.md:#2] | 2 | 2 | 197 |  |
| `Ki` ^[narrativ.md:#1] | 1 | 7 | 35, 36, 155, 197, 199 |  |
| `Shō` ^[narrativ.md:#1] | 1 | 1 | 200 |  |
| `Ten` ^[narrativ.md:#1] | 1 | 1 | 201 |  |
| `Ketsu` ^[narrativ.md:#1] | 1 | 1 | 202 |  |
| `Overall Story` ^[narrativ.md:#1] | 1 | 1 | 192 |  |
| `Main Character` ^[narrativ.md:#1] | 1 | 1 | 193 |  |
| `Impact Character` ^[narrativ.md:#1] | 1 | 1 | 194 |  |
| `Subjective Story` ^[narrativ.md:#1] | 1 | 1 | 195 |  |
| `Novelcrafter` ^[narrativ.md:#3] | 3 | 4 | 103, 105, 213 | `Novelcrafter-Tools` ×1 |
| `Codex` ^[narrativ.md:#5] | 5 | 7 | 105, 109, 215, 218, 219 | `Codex-Struktur` ×1, `Codex-Einträge` ×1 |
| `Matrix View` ^[narrativ.md:#2] | 2 | 2 | 105, 216 |  |
| `Narrative Context Protocol` ^[narrativ.md:#1] | 1 | 1 | 103 |  |
| `NCP` ^[narrativ.md:#1] | 1 | 1 | 103 |  |
| `Single Source of Truth` ^[narrativ.md:#2] | 2 | 2 | 105, 215 |  |
| `Prompt Engineering` ^[narrativ.md:#2] | 2 | 2 | 108, 218 |  |
| `Environmental Storytelling` ^[narrativ.md:#2] | 2 | 2 | 55, 57 |  |

### Lens

Borrowed concepts the document applies to its world, set apart by the list under a `## lens` heading.

| candidate | word | in | lines | surfaces |
|---|---|---|---|---|
| `Dialetheismus` ^[narrativ.md:#1] | 1 | 1 | 157 |  |
| `parakonsistenten Logik` ^[narrativ.md:#1] | 1 | 1 | 157 |  |
| `Dialetheia` ^[narrativ.md:#1] | 1 | 1 | 180 |  |
| `Dramatica` ^[narrativ.md:#0] | 0 | 1 | 190 | `Dramatica-Throughlines` ×1 |

## What the extraction ran into

The zero is an inflection of the compound kind. `Dramatica` ^[narrativ.md:#0] stands only joined to the next word, as `Dramatica-Throughlines` ^[narrativ.md:#1] on L190, so it counts 0 alone and 1 among compounds.

The fifteen terms that stand alone less often than with compounds are inflections and compounds, not damage. `Kael` stands 15 times alone and is written `Kaels` 28 times. `Fundament` stands in `Fundamente`, `Fundaments`, `fundamental` and `fundamentalen`; the last two are the ordinary adjective, not the document's term. `Ki` stands once as the word (L199) and its other lines hold the letters inside longer words such as `Kiko` and `Kishōtenketsu` (L35, L36, L155, L197).

One `- ` line was read as prose and left out of the count: `Show, don't tell`. The reader wrote it with a comma, and the count treats a term with a comma as a sentence. The document writes it on L53 and L99 with the comma, and on L209 as „Show, Don't Tell“ ^[L209] with capitals, so the phrase is on the page, but not in the count.

Export artifacts: the profile lists 2 backslash escapes and 1 glued reference number. Both stand in the bracket at the end of the first sentence of L117, which the export wrote as `\[Persona, 36, 41, …, 384\]`; it is a reference list with no text behind it in this file. The profile also counts 134 straight quotation marks against 21 typographic ones, so quotations of the document's own inner quotes keep the straight form.

The document writes `KW1` to `KW4` with plain digits and gives each world a bracketed name at L61 to L64 and again at L177 to L180. The two lists name KW1 differently: `Logos-Prime` ^[narrativ.md:#1] in the first, `Konstrukt-Stadt` ^[narrativ.md:#2] in the second, where it stands in „Konstrukt-Stadt / Logik“ ^[L177]. KW2 to KW4 carry the same names in both lists. The census records both and does not choose.

Counts the document states against its content. It speaks of „Elf detaillierte Anteile“ ^[L149] but names five (Kael, Selene, Lex, Nyx, Kiko) under „Einige Schlüsselbeispiele sind“ ^[L149]. It heads „Die Sechs Realitätsebenen“ ^[L173] and then numbers three entries, the first holding the four Kernwelten (L175, L181, L182). It states `39` ^[narrativ.md:#3] chapters on L90, L190 and L234.

The acronyms travel with their spelled-out forms on one line: `ANP` with `Anscheinend Normaler Persönlichkeitsanteil` (L151), `EP` with `Emotionaler Persönlichkeitsanteil` (L154), and five of the seven protocol lines of L131 to L137 (ZTEM, RTSV, BPoF, EIC, SIS) carry an acronym beside the English name. `AEGIS` is also spelled out once, at L125.

The text under the first heading of the second voice repeats a sentence of the first voice almost word for word (L15 and L121, „komplexes architektonisches Gebilde“ ^[L15] ^[L121]), and the sentence „Nun gilt es, Stein für Stein“ ^[L113] ^[L238] ends L113 and stands as the whole of L238.

Both `Guardians` and `Guardian-Netzwerk` stand once, in different lines (L181 and L132); `Guardian-Netzwerk` is not on the list because it is a descriptor inside a protocol gloss.

**Zeros:** 1 — `Dramatica`.

**Standing alone less often than with compounds:** 15 — `Kael` 15/43, `AEGIS` 37/39, `TSDP` 1/2, `ANP` 2/3, `EP` 2/4, `Kiko` 3/4, `Juna/V` 5/8, `Fundament` 3/6, `KW1` 3/4, `Entropie` 4/6, `Gärtner` 1/2, `Meta-Erzähler` 1/2, `Ki` 1/7, `Novelcrafter` 3/4, `Codex` 5/7.

**`- ` lines read as prose and not counted:** 1 — Show, don't tell.
