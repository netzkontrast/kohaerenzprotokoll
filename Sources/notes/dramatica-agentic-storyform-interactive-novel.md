---
source: Sources/drive/dramatica-agentic-storyform-interactive-novel.md
read: "2026-10-14, the whole document (L1 to L555) through read.py with line numbers, in ranges of about 100 lines; by a document-reader subagent (Sonnet)"
stance_markers: ["proposes", "proposed", "recommended"]
stance_marker_count: 4
reads_as: "an English research report that proposes an agentic architecture for interactive narrative, with a story theory's model as its constraint system, closing with a reference list"
---

# Note — Dramatica, Agentic Storyform Interactive Novel

What this document says about the terms that matter in it. Every quotation carries its file line on the same line of this note; a number about the whole document is a count mark that `quotes.py` checks. Where the note says **observed**, no quotation is possible (a structure, a gap) and the claim rests on the lines or counts it names. The document speaks as a proposal; its design statements are plans, not reports of a built system, and it names nothing of any novel's world.

## 1 · What kind of text this is, and how it marks itself

- The document announces itself as a proposal: „This report proposes a novel architectural framework“ ^[L31]. `proposes` ^[dramatica-agentic-storyform-interactive-novel.md:#1]
- It marks its design as proposed, and its roll-out advice as advice: `proposed` ^[dramatica-agentic-storyform-interactive-novel.md:#2] and `recommended` ^[dramatica-agentic-storyform-interactive-novel.md:#1]. The three words together stand 4 times (1 + 2 + 1).
- **Observed:** it has six numbered sections, headed `Section I` to `Section VI` (L18, L90, L156, L260, L343, L396), then a German-headed reference list („Referenzen“ ^[L452]) of 102 numbered entries (L454 to L555). It has no chapters: `Kap` ^[dramatica-agentic-storyform-interactive-novel.md:#0], `chapter` ^[dramatica-agentic-storyform-interactive-novel.md:#0].
- Two tables carry mappings (L246 to L256 and L332 to L339), their cells written with escaped asterisks. The first is introduced as a „Rosetta Stone“ ^[L244].

## 2 · The storyform

- The document gives the term as the theory's: a storyform is „a blueprint that encodes the author's intended meaning“ ^[L51].
- It uses the storyform as the agent's own design: „it is the agent's core cognitive architecture“ ^[L86].
- Its four throughlines are listed as constraints that keep the generated narrative faithful: „ensuring that the agent's generated narrative remains true to the author's intended message“ ^[L58].
- The document says the mapping between the story theory and an agent model is more than a comparison: „it is a functional equivalence“ ^[L84].

## 3 · The data format (UNM / NCP)

- The document presents the format under two names: „also referred to as the Narrative Context Protocol“ ^[L101]. It calls it „an open-source initiative designed to encode authorial intent in a portable format“ ^[L101].
- One file holds one storyform: „A single UNM file represents one complete and unique Storyform.“ ^[L119]
- Its three components are defined in turn: Dynamics, „This component captures the broadest strokes of the narrative“ ^[L121]; Storypoints, „This component represents the static, spatial map of the story's conflicts“ ^[L132]; Storybeats, „This component defines the temporal progression of the narrative“ ^[L144].
- The document turns the file into „the agent's narrative constitution“ ^[L150], borrowing the AI-safety notion of a constitution for it.

## 4 · The proposed agent and its layers

- The design has one thinking agent: „is centered around a single, primary agent“ ^[L165]. `Narrative Director` ^[dramatica-agentic-storyform-interactive-novel.md:#16]
- The planner is called „the most critical component of the agent“ ^[L178].
- Static memory is called „the immutable, authoritative source of the author's intent“ ^[L206].
- Characters other than the player are given beliefs, desires and intentions. The document assigns desires by role, for example: „The Antagonist's primary desire is to prevent the achievement of the Story Goal“ ^[L241].
- A table cell calls the whole storyform „The ultimate source of thematic truth“ ^[L249], and another cell calls the state database a „single source of truth for the game state“ ^[L339]. These are the document's claims about its proposed components, recorded and not applied.

## 5 · Control and agency

- The document sets the author's control at one level and the player's at another: „The author retains control at the Storyforming level.“ ^[L369] and the player's agency „operates exclusively at the Storytelling level“ ^[L371].
- Storyforming and storytelling are defined side by side: „Storyforming is the process of defining the underlying structure of the narrative's meaning“ ^[L366] and „Storytelling is the process of expressing that underlying structure“ ^[L367].
- The fixed file cannot be changed by play: „is fixed and cannot be altered by the player's actions“ ^[L369].
- Its name for the goal of balancing the two is `curated agency` ^[dramatica-agentic-storyform-interactive-novel.md:#1], defined as „the ability to make impactful choices within a constrained but coherent and responsive narrative system“ ^[L356].
- Four example responses to a temptation beat are given: „Give in“ ^[L375], „Nobly resist“ ^[L376], „Cleverly outwit“ ^[L377] and „Flee“ ^[L378].
- When a player's action pushes the story off its course, the director is described as „an intelligent agent that monitors the virtual world“ ^[L388]; the document says the response is not to return the player by force: „The agent will not simply force the player back onto the original path“ ^[L392].

## 6 · Roll-out, ethics

- Three deployment phases are named: „Human-in-the-Loop (Authoring and Validation)“ ^[L407], „Semi-Autonomous (Guided Generation)“ ^[L408] and „Fully Autonomous (Live Operation)“ ^[L409].
- On authorship the document proposes a framing: the generated text is a „licensed, derivative performance“ ^[L447] of the storyform, and the player is a „co-creator“ ^[L447].
- On bias it calls the storyform a „debiasing filter“ ^[L449].

## 7 · Said two ways, or left open — recorded, not resolved

- The document gives its format two names, the Universal Narrative Model and the Narrative Context Protocol, as one thing: `Universal Narrative Model` ^[dramatica-agentic-storyform-interactive-novel.md:#5], `Narrative Context Protocol` ^[dramatica-agentic-storyform-interactive-novel.md:#2], while `UNM` ^[dramatica-agentic-storyform-interactive-novel.md:#40] stands alone far more often than the second name.
- **Observed:** the memory is described as three tiers in the text (L204 to L216), and the context assembled for each turn as six items (L317 to L324); the two lists are separate and the document does not say how they correspond.

## 8 · Absent, counted

- The document names no figure of a novel's world: `Kael` ^[dramatica-agentic-storyform-interactive-novel.md:#0], `AEGIS` ^[dramatica-agentic-storyform-interactive-novel.md:#0], `Kohärenz` ^[dramatica-agentic-storyform-interactive-novel.md:#0].
- It writes no chapter reference: `Kapitel` ^[dramatica-agentic-storyform-interactive-novel.md:#0].
