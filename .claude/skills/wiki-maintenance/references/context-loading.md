# Context-efficient manuscript loading

The goal is the smallest sufficient, spoiler-safe context packet for a
specific writing decision.

## Retrieval ladder

1. Establish task, target chapter, scene, and whether future spoilers are
   allowed. If the answer affects selection and is unknown, ask.
2. Read `Wiki/context-map.md`, not the entire Wiki.
3. Filter by chapter window and require `spoiler_until <= target chapter` for
   spoiler-safe work.
4. Load `core` rows before `supporting`; load `evidence` only when the task
   needs substantiation.
5. Open the smallest matching page and only the relevant heading range.
6. Follow citations to exact source lines only when wording, evidence, or a
   conflict must be verified. Never load a complete raw source by default.
7. Stop when the writing decision is supported; more context is not
   automatically better context.

## Packet order

Build working context in this order:

1. task and chapter constraints;
2. core synthesis/concept summaries;
3. open questions that materially affect the scene;
4. relevant detailed headings;
5. exact evidence excerpts.

Preserve source references in notes so claims can be rechecked without keeping
large source bodies in active context.

## Safety defaults

- Unknown spoiler ceiling means `40`, never “safe everywhere”.
- Unknown chapter range means whole-novel scope until reviewed.
- A summary routes retrieval; it never substitutes for authority or evidence.
- Conflicting pages are loaded together and surfaced to the author; the
  maintenance workflow does not resolve the conflict.
