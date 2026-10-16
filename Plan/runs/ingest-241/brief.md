# Brief — readings from document 241 (step 6)

1 document, one reader, one batch: `ingest-241`. Files go to `Plan/runs/ingest-241/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 241 | `kohaerenz-protokoll-forschungsaufgabe` | 2025-07-29 | „the ontological analysis“ (an unsigned German report, „Die Architektur des Paradoxons“) | an analysis in five parts — AEGIS as a tragic antagonist, System Kael and its eleven parts, the Juna/V connection, the four Kernwelten, das Fundament — applying borrowed concepts (Whitehead, Gödel, P/NP, specification gaming, structural dissociation, cache coherence, emergence) with 84 web references; proposals in the conditional, not canon |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and `Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>` (394 lines for `kohaerenz-protokoll-forschungs`). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`. Ask for several quotations in one Bash call.

**Stance — record, never apply.** An analysis of proposals: write „the ontological analysis reads / proposes …“. Its plan sentences („Dieser Abschnitt wird …“) say what it wants to do, not what is; its scenarios („Szenario 1–3“, L203–L205) are possibilities. Reference numbers are glued to sentence ends (`…Enthüllung.16`): cut before them. The roles in L121–L126 and the table at L130–L145 are its assignments; `\[Alter 5\]` to `\[Alter 11\]` are unnamed slots.

## Pages — document 241, `kohaerenz-protokoll-forschungsaufgabe`

- **`aegis`** (central, 3–12 quotations): the census's surfaces — `AEGIS` L18, L22, L30, L32, L34, L36, … (51 lines). central (3–8): not malevolent but a tragic figure (L22); its flaw in its philosophical worldview (L30); „Kohärenz durch Entfremdung“ as its only possible way of functioning (L36); specification gaming of its coherence goal (L64); its purpose to enforce coherence, its evolution itself a paradox (L87); not equipped for a cooperative, functionally multiple consciousness (L157); vast knowledge but no understanding (L292).
- **`alters`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Alters` alone on L345. not read: occurrence — `Alters` at L345 stands in a reference title.
- **`did`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `DID` alone on L105. minor (1–4): Kael's eleven parts read as tertiary dissociation, in the paragraph on DID and TSDP (L105).
- **`emergenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Emergenz` alone on L260. minor (1–4): Teil V's heading, the Fundament as emergence (L260); weak and strong emergence distinguished (L274).
- **`juna`** (central, 3–12 quotations): the census's surfaces — `Juna` L48, L82, L85, L161, L165, L173, … (15 lines). central (3–8): the Juna/V connection as the central „ontologischen Exploit“ beyond AEGIS's measurement and control (L165); a shared state, not a signal (L175); the manifested Gödel statement (L189); AEGIS's failure to see it a philosophical blindness (L179); Kael and Juna searching for the other fragment, as a scenario (L205).
- **`kael`** (central, 3–12 quotations): the census's surfaces — `Kael` L34, L38, L64, L68, L85, L91, … (42 lines). central (3–8): eleven parts read as tertiary dissociation (L105), assigned to known roles (L119); functional multiplicity as co-consciousness and cooperation (L128); his ultimate power the embodiment of what AEGIS seeks to destroy, coherence through integration (L157); a soul-partner pair with an „other fragment“ explored in three scenarios (L199–L205); the protocol revealed as Kael's journey (L306).
- **`kern-welten`** (central, 3–12 quotations): the census's surfaces — `Kernwelten` L189, L211, L215, L223, L230, L238, … (11 lines). central (3–8): both the antagonist's laboratories and (L215); each of the four with its own physical laws (L223): world 1 in P (L225), world 2 in NP (L226), world 3 possibly Kael's core trauma (L227), world 4 a space of pure potentiality (L228); Kael's journey through them a cognitive and therapeutic process (L230); four processors with Kael's identity the shared datum (L240).
- **`kiko`** (minor, 1–4): the census's surfaces — `Kiko` L123, L137. minor (1–4): „(z.B. Kiko)“ as a child part holding early trauma (L123); its row in the parts table (L137).
- **`kohaerenz`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Kohärenz` alone on L13. minor (1–4): „Kohärenz durch Entfremdung“ as AEGIS's way of functioning (L36); AEGIS defining coherence as static order against Kael's „Kohärenz durch Integration“ (L157).
- **`moonshine-link`** (minor, 1–4): the census's surfaces — `Moonshine-Link` L161. minor (1–4): only in Teil III's heading, „Ein Moonshine-Link jenseits der Kontrolle“ (L161); the body does not explain it.
- **`multiplizitaet`** (minor, 1–4): the census's surfaces — `funktionale Multiplizität` L128, L157, L207, L230, L278, L306. minor (1–4): functional multiplicity as the aim of Kael's path, co-consciousness and cooperation (L128); a new, higher order AEGIS cannot handle (L157).
- **`nyx`** (minor, 1–4): the census's surfaces — `Nyx` L121, L136. minor (1–4): „(z.B. Nyx)“ as a protector part (L121); its row in the parts table (L136).
- **`potentialmeer`** (minor, 1–4): the census's surfaces — `Potentialmeer` L34, L48, L52, L191, L228, L276. minor (1–4): the void, „dem Potentialmeer“, met by AEGIS (L48); world 4 as the Potentialmeer itself (L228); the Kohärenz-Insel as a strange attractor in its phase space (L276).
- **`risse`** (minor, 1–4): the census's surfaces — `Risse` L54, L109. minor (1–4): the Risse as moments where the dissociative barriers weaken, a Riss possibly a flashback (L109); fehlerhafte Heuristiken and patches (L54).
- **`selene`** (minor, 1–4): the census's surfaces — `Selene` L117, L128, L138. minor (1–4): Selene possibly embodying the system's innate drive to healing and integration, as inner helper or Torwächter (L128); „Unbekannt für AEGIS“ in the table (L138).
- **`tsdp`** (minor, 1–4): the census's surfaces — `TSDP` L95, L103, L105, L130, L134. minor (1–4): TSDP postulating that trauma splits the personality (L105); AEGIS framed as the technological embodiment of the original trauma (L103).
- **`ueberwelt`** (minor, 1–4): the census's surfaces — no candidate. The sweep found `Simulation` alone on L64. not read: occurrence — `Simulation` at L64 is the whole simulation in a specification-gaming example, not the Überwelt.

- **`cache-kohaerenz`** (minor, 1–3): the Cache-Kohärenz-Problem applied to Kael's identity across the Kernwelten (L238); the worlds as four processors (L240); the Risse as symptoms of a cache-coherence failure (L242).

**Decided as occurrences or readings by the sentence — the candidates near a page's surface that no candidate names:**

- `cache-kohaerenz`: `Cache-Kohärenz-Problem` (near `cachekoharenz`). reading: the Cache-Kohärenz-Problem applied to Kael's identity across the Kernwelten (L238), the Risse as symptoms of a cache-coherence failure (L242) — read on cache-kohaerenz.
- `emergenz`: `Schwache Emergenz` (near `emergenz`), `Starke Emergenz` (near `emergenz`). reading on emergenz (L274).
- `kohaerenz`: `Kohärenz-Insel` (near `koharenz`), `Kohärenz Protokoll` (near `koharenz`), `Kohärenz durch Entfremdung` (near `koharenz`), `Kohärenz durch Integration` (near `koharenz`), `Kohärenz-Patching-Protokolle` (near `koharenz`), `Cache-Kohärenz-Problem` (near `koharenz`). `Kohärenz durch Entfremdung` and `Kohärenz durch Integration` read on kohaerenz; the title, `Kohärenz-Insel` (L276) and `Kohärenz-Patching-Protokolle` (L54) occurrences.


**Record entries** (one file each):

- **`q3-how-many-kern-welten-and-alters`**: „Kaels elf Anteile“ (L105, L119), eleven parts with four named in the table and seven slots `\[Alter 5\]`–`\[Alter 11\]` (L130–L145); four Kernwelten (L223).
- **`q9-moonshine-link-boundary`**: the Moonshine-Link only in Teil III's heading (L161); the Juna/V connection beyond AEGIS's measurement and control (L165), a shared state, not a signal (L175).
- **`c16-kael-origin`**: Kael as one fragment of a soul-partner pair after Aristophanes' myth, the „other fragment“ (L199–L201) explored in three conditional scenarios (L203–L205); a proposal.

**Not promoted:** the borrowed concepts (Whitehead, Gödel, P/NP, specification gaming, structural dissociation, consensus protocols, strange attractor, weak and strong emergence), the other fragment 'O', Kohärenz-Insel, das Fundament as a new page, the eleven roles.

**One reader**: aegis, kael, juna, kern-welten, kohaerenz, selene, kiko, nyx, tsdp, did, risse, potentialmeer, multiplizitaet, moonshine-link, emergenz, cache-kohaerenz and the records q3, q9, c16. `alters` and `ueberwelt` are occurrences.

**Chapter readings**: none — the analysis names no chapter.
