# Brief — readings from documents 52 and 53 (step 6)

Two documents, one reader, one batch: `step6-readings-52-53`. Files go to
`Plan/runs/step6-readings-52-53/readings/<page>--<slug>.md`, as `.claude/agents/wiki-reader.md` says.

| n | slug | date | prose name | what it is |
|---|---|---|---|---|
| 52 | `ontologische-inversion-von-aegis-kritisches-framework` | 2026-03-01 | „the Inversion framework" | a SKILL.md draft in an assistant's voice for the Dual-Kernel-Narrativ-Engine: a method around one worked example that inverts AEGIS from Kohärenz-Kernel to Kollaps-Kernel, an inversion it credits to the addressee (L13) |
| 53 | `kohaerenz-protokoll-meta-foreshadowing-beobachter-logik` | 2026-02-25 | „the Meta-Foreshadowing plan" | a writer's plan for the final twist — Kael as the reader's manifestation, whose world dies when the book is closed — with four sample wordings |

Read first, for each: `Sources/notes/<slug>.md`, the end of `Sources/terms/<slug>.md` and
`Plan/runs/<slug>/05-verify.txt`; then the document with `python3 scripts/read.py <slug>`. Both are
short (166 and 58 lines). For each page, its digest: `python3 scripts/digest.py <page> --doc <slug>`.
Ask for several quotations in one Bash call (`read.py <slug> --find "…"; read.py <slug> --find "…"`)
rather than one call each.

**Stance — record, never apply.**
- 52 marks its examples with „z.B." (L28, L44, L45, L111, L121). A name inside an example is the
  example's, and the reading says so. Its central claim, AEGIS as Kollaps-Kernel, is stated as fact
  (L83) and credited to the addressee's proposal (L13). Say both.
- 53 is a plan in the imperative and the conditional („sollte", „könnte", „müssen wir"). A reading
  says what the plan wants to happen, never that it happens in the novel.

## Pages — document 52

- **`aegis`** (central, 5–10 quotations): the default reading as K\_1 (L79) and the call to invert it
  (L79); the inverted reading (L81, L83); the three proofs — Maxwellscher Dämon erasing Qualia and
  Trauma (L87), „AEGIS erzeugt das Rauschen, das es zu bekämpfen vorgibt" (L87), the Big Freeze
  (L89), Korrespondenz and the Noumena (L91); its failure on Gödel (L100). AEGIS keeping „die
  Simulation" clean (L87) goes here, not on `ueberwelt`.
- **`kollaps-kernel`**: AEGIS as K\_0 (L81, L83); the template's check (L144); K\_0 as an entropic
  pressure to keep up (L57). The note observes that one symbol names a pressure and a kernel. (J99)
- **`kohaerenz-kernel`**: AEGIS as K\_1 by default (L79); true K\_1 coherence only in the Mosaik-Herz,
  Phase III, with paraconsistent logic and Entropie integrated, not erased (L102); the heading (L94);
  the template's check (L145). (J98)
- **`mosaik-herz`**: L102, where the document places true K\_1 coherence („Phase III").
- **`entropie`**: „Maschine der Entropie" (L83); erasure that „generiert massiv Entropie" (L87);
  „maximaler Entropie (Wärmetod)" (L89); „die Entropie (das Trauma)" (L102); „narrativer Entropie"
  (L19). If the document takes a side on what Entropie is, write a `C2` entry (below).
- **`selene`**: the Integrator-Agent (Selene) buffering the contradiction through paraconsistent
  logic gates, the stress test's success case (L123). (J113, J70)
- **`lex`**: an agent as ANP in the example (L44); his system prompt, checked for an isolated
  Korrespondenz (L111). Both are examples.
- **`moros`**: as EP in the example (L44). Minor.
- **`kael`**: the example paradox „Kael existiert als Eins und als Viele" (L121). Minor.
- **`moonshine-link`**: an injection of entropic pressure through the Moonshine-Link or user input,
  in the PICO model's intervention (L45). Minor, an example. Q9 only if it says where the link ends.
- **`dkt`**: the „Ontologischen Inversion" of agent roles inside the Dual-Kernel-Theorie (L31).
  „Dual-Kernel-Theorie" is the page's term (J95). The Dual-Kernel-Narrativ-Engine (L11) is on the
  page only if the digest shows the page already treats the engine as the theory (J28).
- **`kohaerenz`** — by the sentence: the page is the novel's Kohärenz. The document's own
  „Kohärenz-Wahrheit" (L94, L96) and „narrative Kohärenz" (L112) are readings if the digest's lead
  covers what Kohärenz is in the system. „Korrespondenz- und Kohärenztheorien der Wahrheit" (L29)
  is borrowed philosophy (J28). If nothing is left after that, write „not read".

**Decided as occurrences — no file:**
- `kern-welten`: „Kernwelt" is a template placeholder (L137).
- `ueberwelt`: „Simulation" (L87) goes on `aegis` (J30, J39: by the sentence).
- `landauer-signatur`: the Landauer-Prinzip is not the Landauer-Signatur (J53, J62, J81).
- `nichts-rauschen`: „das Rauschen" (L87) is not the Nichts-Rauschen (J88).
- `goedel-gambit`: Gödels Unvollständigkeitssatz (L100) is not the gambit.
- `blinder-fleck`: an LLM's „Ontological Blindness" (L26, L151) is not the blind spot (J53).
- `vergessener-schrein`: „Trauma" in general (J105).

## Pages — document 53

- **`kael`** (central, 4–8):
  - the twist the plan prepares, Kael as the reader's manifestation whose world dies with the
    closing of the book (L13);
  - time in the Konstrukt „getaktet" (L17), the world freezing (L19), the „Große Stille" (L20), the
    sample text (L21);
  - the world falling into text fragments where it is not yet „beschrieben" (L34);
  - Kael as the probe the reader sent into the trauma (L42);
  - the final chapter (L48, L49);
  - the „Du" as Kael's inner voice (L53).
- **`aegis`**:
  - an administrator waiting for a „Signal", not an autonomous god (L25);
  - its status reports' „Primären Beobachtungs-Einheit" and „Externen Taktgeber" (L27);
  - its harsh measures, „das Kohärenz Protokoll" (L27);
  - its fear of the book being closed, and its craving for order as a way to keep the reader, with
    attention as energy (L28);
  - its protocols in italics, querying the „Beobachtungsstatus" (L54);
  - the closing status line (L58).
  - C14 only if a passage says AEGIS speaks in the first person.
- **`juna`**: whispers the truth to Kael (L39); the dialogue hint (L41); „Die Umkehrung" (L42); the
  section's name, „Die Juna-Spiegelung" (L37), whose body does not say what is mirrored. (J70, J113)
- **`entropie`**: the closing of the book framed as the „Wärmetod des Universums" (Entropie) (L46).
  Minor.
- **`risse`** — by the sentence (J28): the plan's „Glitch-Momente" (L13), with the freezing (L19) and
  the decay (L34) it describes. The page carries `Glitch` as a surface. Read the digest and write a
  reading only if the page's Risse or Glitches are breaks in the world's surface of that kind.
  Otherwise write „not read".
- **`kap-39`** (a chapter page, `Wiki/chapters/README.md` has the format): „In Kapitel 39 müssen wir
  beschreiben, …" (L48), under „Das finale Kapitel" (L44), and „Der Schock" (L49).

**Decided as occurrences — no file:**
- `kohaerenz`: L27 writes it only inside the name „Kohärenz Protokoll" (J9, J66). That name glosses
  AEGIS's measures and goes on `aegis`.
- `konstrukt-stadt`: „Konstrukt" (L17) names no city (J88). C9 is not touched.
- `vergessener-schrein`: „Trauma" (L42) is the reader's trauma (J105).

## Records

Write a record entry only for `C2` (Entropie means two incompatible things), and only if a document
takes a side on what Entropie is. The file is `Plan/runs/step6-readings-52-53/readings/c2-entropie-sense--<slug>.md`,
with `page: c2-entropie-sense` and the heading `## 2026-09-30 — \`<slug>\`, <date>, <prose name>`.
For anything else that looks like a conflict or a question, report it and write nothing; the
session decides.

## Before you finish

`python3 scripts/readings.py check step6-readings-52-53` shows no refusal. Report per page: the file
written or „not read" with why, and the lines cited.

Rules that apply: J9, J28, J30, J39, J53, J62, J66, J70, J81, J88, J95, J98, J99, J105, J113
(`Plan/runs/judgements.md`).
