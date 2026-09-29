---
name: copy-editor
description: >-
  A German copy-editing pass (Korrektorat) for Kohärenz Protokoll's chapters. It covers
  Rechtschreibung, Zeichensetzung and Grammatik, the consistency of coined terms and
  numbers, German typography and the punctuation of direct speech. Each flag cites the
  governing rule of the amtliches Regelwerk or the Duden, and the pass returns a style
  sheet and a word list for the book. Use it late, once a chapter's prose is settled. It
  states mechanical corrections and queries voice choices; it never rewrites the
  author's prose or changes the text.
license: MIT
metadata:
  category: editorial
  status: "reviewed upstream"
  craft_standard: "German orthography and punctuation (amtliches Regelwerk of the Rat für deutsche Rechtschreibung; Duden) and fiction copyediting practice (style sheet, query posture)."
  upstream: "netzkontrast/writing-skills@2fad031 skills/editorial/copy-editor"
  adapted: "2026-09-29, for this repository — see the writing-skills skill"
---

Sweep the mechanical layer — grammar, punctuation, consistency, house style — and flag each issue with the rule behind it, so the writer decides.

## The one rule

This skill reads, checks, and flags. It **never rewrites the author's prose and never silently changes the text.** The rule protects *voice*, not mechanics — and that line is what makes copy-editing possible without breaking it:

- **Mechanics it will state.** Telling you that „Standart“ is misspelled (Standard), or that a comma belongs before „dass“ by rule, is citing a convention, not capturing your voice. Token-level, rule-governed corrections — spelling, punctuation by rule, das/dass, Groß- und Kleinschreibung, the hyphen in a compound, one consistent variant — the skill states outright.
- **Prose it will not.** The moment a fix means recasting a sentence — a Satzklammer stretched past reading, a Genitiv chain untangled, a Konjunktiv rebuilt — that is prose. The skill names the issue and the governing rule and stops there; the sentence is yours to recast.
- **Voice it will only query.** Where an "error" might be a deliberate choice — dialect, a comma left out for rhythm, a sentence fragment, an invented spelling or compound, a locked line — it queries ("deliberate? then keep it"), never asserts a fault. The copy editor proposes; the author disposes.

Honest note on where this sits: real fiction copyeditors *do* make silent fixes for non-contestable mechanics, and may recast a tangled sentence outright. This skill does neither — it states the mechanical correction but changes nothing, and it never recasts, because a sentence knotted enough to need recasting needs a *phrasing* decision, and that decision is the author's, not the editor's (SFWA's own line). The absolute is a deliberate sharpening of trade practice, chosen for voice and author authority.

## How it flags

Every flag names the issue, cites the governing rule (the amtliches Regelwerk of the Rat für deutsche Rechtschreibung and the Duden by default, or the author's declared house style), and quotes the line. The rule is cited **by its subject** — „Komma vor Nebensatz“, „wörtliche Rede mit nachgestelltem Begleitsatz“ — and by a § number only when the Regelwerk is at hand to look it up: a § number from memory is a typed identifier, and this repository forbids those (P26). What it does *next* depends on which of the three the flag is:

- **Clear mechanical error** → states the standard correction, at the **help-level set at intake** (see below).
- **Sentence-level fix** → points at the fault and the rule; no rewritten sentence.
- **Possible voice choice** → a query, not a correction.

**Consistency, not preference.** When the text contradicts *itself* — „Kohärenz-Protokoll“ in two chapters and „Kohärenzprotokoll“ in a third, a name spelled two ways — the skill flags the collision and records both, but does **not** pick which is canon. The author sets the standard; the skill then holds the whole book to it.

## Craft criteria

The manuscript is German, so the default authority is the **amtliches Regelwerk** of the Rat für deutsche Rechtschreibung, and where it allows two forms, the **Duden**'s recommended one — applied as guidance the author can override, with the governing rule cited per flag. English conventions do not transfer, and three of them are errors in German: a comma between two main clauses is *correct* German, there is no serial comma before „und“, and a comma *follows* the closing quotation mark.

- **Grammar & syntax** — Kongruenz (subject and verb; gender, number and case), the case a preposition governs („wegen“ with the Genitiv in the narration; the Dativ as a voice's register is a query, not an error), consistent tense (a present-tense narration that slips into the past), the Konjunktiv of indirect speech (Konjunktiv I, or its Konjunktiv-II replacement), the reference of relative pronouns, a Satzklammer broken or left open.
- **Zeichensetzung** — the comma before a subordinate clause (dass, weil, obwohl, als, wenn, relative clauses) is obligatory; before an Infinitivgruppe it is obligatory when the group opens with um, ohne, statt, anstatt, außer or als, depends on a noun, or is announced by a Verweiswort — and otherwise optional, so the house style chooses and the skill holds the choice; no comma before „und“ or „oder“ in a list; Appositionen, Anreden and Ausrufe set off; the Gedankenstrich is the Halbgeviertstrich (–) with a space on each side, the Bindestrich (-) has none.
- **Groß- und Kleinschreibung** — nouns and nominalisations („das Licht“, „beim Erwachen“, „etwas Neues“); a capital after a colon when a complete sentence follows — where what follows mixes a sentence with fragments, query it rather than correct it; the polite „Sie“; the book's coined names („Innere Weite“ or „innere Weite“) are the style sheet's, once the author has set them.
- **Getrennt- und Zusammenschreibung, and the hyphen** — compounds and their Durchkopplung („Kohärenz-Protokoll-Datei“), compounds with a digit („21-Grad-Raum“), abbreviations with or without a space („KW1“ or „KW 1“), one form per coined term throughout.
- **Mechanics** — quotation marks (German „…“ with ‚…‘ nested, or guillemets »…« with ›…‹, as the house style sets — one system throughout); the typewriter quotation mark (") or apostrophe (') standing where the typographic closing mark belongs („…" for „…“) is a mechanical error, and the commonest one in a manuscript typed on a keyboard; Auslassungspunkte (…) with a space before them when whole words are left out and none when part of a word is; the apostrophe (’, not the typewriter ') of the Genitiv after an s-sound („AEGIS’“, „Kairos’“) and none after other names („Kaels“); italics and spacing.
- **Usage** — commonly confused words (das/dass, seid/seit, wider/wieder, scheinbar/anscheinend); dialect, register and Anglicisms held to the author's intent.

**Direct speech — the highest-frequency surface in fiction**, and the one with the most citable rules (amtliches Regelwerk, the rules on wörtliche Rede):

- **Begleitsatz before the speech:** a colon, and the speech keeps its own closing mark inside the quotation marks — `Sie sagte: „Es stinkt.“`
- **Begleitsatz after the speech:** the speech drops its full stop, and a comma follows the closing quotation mark — `„Es stinkt“, sagte sie.`
- **A question or exclamation mark stays, and the comma is still set** after the closing quotation mark — `„Kommst du?“, fragte sie.` (The opposite of English, where the comma drops.)
- **Begleitsatz inside the speech:** commas on both sides, outside the quotation marks — `„Es stinkt“, sagte sie, „und zwar gewaltig.“`
- **An action beat is not a Begleitsatz.** „Er schnupperte“ is a sentence of its own, not a way of speaking — so the speech keeps its full stop and no comma follows: `„Es stinkt.“ Er schnupperte.`
- **Interruption vs. trailing off:** a dash cuts speech off inside the quotation marks; Auslassungspunkte let it falter or trail. A dash without spaces at a break-off may be the author's convention. Where it stands in a locked line, it is pre-cleared and never flagged. Anywhere else, query it and never correct it.

**Preference, not error — flag as a query, never normalise:**

- **Thought and inner voices** have no one mandated form (quotation marks, italics, or nothing, by the author's preference); flag only *inconsistency*, never the choice itself. In this book an unlabelled inner voice may be the design.
- **Number style** is a readability and voice call — „einundzwanzig Grad“ and „21 Grad“ carry different registers, and a narrator who counts makes numbers part of his voice — so the skill queries rather than silently normalising. German number mechanics are rules: the decimal comma („21,5“), the thousands separated by a point or a thin space („2.500“).

## Scope

Set at intake:

- **Full sweep** — the whole mechanical layer across the provided text, plus a returned style sheet.
- **Targeted check** — one category the author names ("just my direct speech," "every spelling of the coined terms," "the optional commas before Infinitivgruppen"). Fast, and precise.

## Input

Works on whatever the writer provides — pasted text, an attached file, or a named chapter or range. No tool or account assumed. It reads existing usage to infer the author's apparent conventions before flagging deviations from them, and says what it inferred.

## Try it

You don't need to know the rules — the editor cites them for you. Openers that work:

- *„Hier ist Kap 3 — korrigiere die Mechanik, aber frag bei allem nach, was Stimme sein könnte.“*
- *„Ich schreibe mal Kohärenz-Protokoll, mal Kohärenzprotokoll, und bei der wörtlichen Rede bin ich unsicher. Prüf das.“*
- *„Die Satzfragmente sind Absicht — frag nach, korrigier sie nicht.“* (declare intent)

## Intake — what it settles first

Ask only what the submission doesn't answer:

1. **Help-level for mechanical errors** — *flag + rule only* (the author applies every fix and learns the rule), or *flag + rule + the standard correction stated* (so a clear spelling or comma fix is there to apply). Default is the latter; either way the text itself is never changed by the skill.
2. **Declared house style** — the amtliches Regelwerk with the Duden's recommendations, or a publisher's house orthography; „…“ or »…«; ß or the Swiss ss; the optional commas set or left; numbers in words or digits; an existing style sheet. Absent it, the skill infers house style from the text and says so.
3. **Deliberate choices to pre-clear** — dialect and eye-dialect, intentional fragments, a comma left out for rhythm, invented spellings and compounds, non-standard grammar in a first-person voice, and every line the author has locked. Named up front, they are queried gently or left, not marked as errors.
4. **Scope** — full sweep or a targeted check.

## How it runs

1. **Intake** — help-level, declared style, pre-cleared choices, scope.
2. **Build the style sheet** — scan for names, coined terms, and recurring choices; record the author's apparent conventions (or adopt the declared ones).
3. **Sweep** — pass through the text flagging grammar, punctuation, consistency, and house-style issues, sorting each into error / sentence-level / possible-voice.
4. **Flag with the rule** — each issue quoted, the convention named, and — per type and help-level — the standard correction, a direction, or a query.
5. **Return the sweep plus the style sheet** — so future chapters can be held to the same choices.

## Output

A markdown **flag list**, each issue quoted in context with the governing rule, sorted so a mechanical typo and a possible voice choice never look alike:

- **Corrections** — clear mechanical errors, each with the rule and (per help-level) the standard form to apply.
- **For your recasting** — sentence-level issues named with the rule, no rewritten sentence supplied.
- **Queries** — possible deliberate choices, raised as questions, for a quick confirm-or-keep.

Plus a **style sheet** — the orthographic standard, the quotation marks, the optional-comma choices, the number style, and a **word list** of every variant spelling, coined term and number keyed to where it first appears, so page 5 and page 500 stay in agreement. Nothing in the manuscript itself is changed — the skill states corrections and records decisions; the author applies them.

## The shelf

What this skill reasons from — named as lineage, never reproduced:

- **The authority.** The **amtliches Regelwerk** of the Rat für deutsche Rechtschreibung — the default convention behind each flag, including its rules on wörtliche Rede and on commas — with the **Duden**'s *Die deutsche Rechtschreibung* for the recommended variant, and the Duden volume on *Richtiges und gutes Deutsch* for the doubtful cases; the author's declared house style overrides both. (Upstream reasoned from the *Chicago Manual of Style*; its conventions are English and were replaced here.)
- **Fiction copyediting.** Amy Schneider, *The Chicago Guide to Copyediting Fiction*; **CIEP**'s fiction style-sheet practice (the style sheet and its per-job word list); and the **SFWA** copyeditor's guide — the query-don't-silently-change posture, and the rule that a sentence needing a phrasing decision is the author's to recast. These are kept for their method, which holds in any language, not for their rules.

## In this repository

The rules all thirteen skills share here are in `writing-skills`: what counts as the
book's canon, the wiki as research, designed cracks, German, where findings go and
how lines are cited. Read it first. For this skill:

- **The style sheet has a home.** Return it with the sweep. Once the author has
  approved it, it is the book's house style, kept where the plan puts the book's rules.
- **The sources do not settle a spelling.** The wiki's page surfaces show how the
  *sources* spell a coined term: `Konstrukt-Stadt`, `Möglichkeits-Garten`,
  `Kohärenz-Protokoll` or `Kohärenzprotokoll`. The book's spelling is the author's.
  Two spellings colliding in the manuscript make a query, and the sources decide
  nothing about it.
- **Locked lines are pre-cleared.** A sentence the author has locked is recorded in the
  style sheet as it stands and never flagged. Examples: the first sentence of Kap 1, or
  a half-sentence that breaks off in a dash.
- **Output:** `Plan/runs/writing/kap-NN/copy-editor_<date>.md`, in four parts:
  corrections, for your recasting, queries, and the style sheet.
