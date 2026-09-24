export const meta = {
  name: 'tool-review',
  description: 'Test each tool installed 2026-09-24 on documents 5 and 6 through the free-model router, score by code, review what the loop could use',
  whenToUse: 'Re-running the tool review under decision 007. Start the proxy first: .venv-grawiki/bin/python scripts/route.py serve --port 8787. Pass args {date, port, docs}.',
  phases: [
    { title: 'Test', detail: 'one Sonnet tester per tool group, every model call through scripts/route.py', model: 'sonnet' },
    { title: 'Check', detail: 'Jev scores each recommendation against the evidence it cites', model: 'haiku' },
    { title: 'Synthesize', detail: 'one review per phase of the loop' },
  ],
}

// Cost tiers (Plan/concept/tool-review-plan_2026-09-24.md): code for everything
// decidable; free OpenRouter models through the proxy for every extraction a tool
// does; Jev for the one judgement stage; Sonnet testers; the synthesis on the
// session model. Consent is decision 007 and is enforced by route.py, not by
// these prompts: a request carrying another document's text is refused.

const A = args || {}
const DATE = A.date
const PORT = A.port || 8787
const DOCS = A.docs || []
if (!DATE || DOCS.length !== 2) throw new Error('pass args {date, port, docs: [doc5, doc6]}')
const PROXY = `http://127.0.0.1:${PORT}/v1`

const RULES = `Rules that bind you (the repository's CLAUDE.md is already in your context; these are the ones this job turns on):
- Corpus text may leave the container ONLY through the router at ${PROXY} (OpenAI-compatible) or \`python3 scripts/route.py complete|jev\`, and ONLY for these two documents: ${DOCS.join(', ')} (decision 007). The API key you give any tool is the label \`route:<your-tool>:<slug>:<attempt>\` — never a real key. The router refuses other documents' text; if it refuses you, report it, do not work around it. Never use a provider that ignores the base URL (anthropic, google SDKs), never OpenCode's built-in openrouter provider.
- Model names: use \`free\`. Never gpt-5.6-sol, *-pro, *codex*, gpt-6* (langchain then calls /v1/responses, which the proxy does not serve).
- Write only under Plan/runs/tooltest/<your-tool>/ and your review file. Never touch Wiki/, Sources/, the manifest, or another tester's files. Nothing goes to Notion.
- At least two attempts wherever a model is involved (P18): attempt 1 and 2 in the key's last part make the router call afresh.
- A tool that cannot run here is NOT REACHED — say why and what would reach it (P15). Never call that a failure of the tool, never fake a result.
- Every number you report comes from a command you ran; name the command. Names are scored ONLY by \`python3 scripts/entities.py score <slug> --names <file.json>\` (file: {"entities": [{"term": ..., "scope": "world"|"lens"}]}); it refuses names the document does not contain word for word. Paste its first two lines. Two human readers agree at F1 0.66 (P27); the Haiku entity lists scored 0.25 (document 5) and 0.69 (document 6).
- A model's output here is a reading: it may not create a page, write a [[link]], supply a count, merge two surfaces, or detect a conflict (conflict detection is never mechanised). Say where each tool's output could go under those limits.
- Read your tool's row in Plan/concept/tool-review-plan_2026-09-24.md first ("What each tool needs") — it has the config facts with file and line.
- Keep each tool run under about 25 minutes; if it does not finish, stop it and report what completed.

Your review file: Plan/concept/tool-review_${DATE}/<your-tool>.md — English, measured, short: what ran, the numbers with their commands, what broke and why, and what the repository's loop could use (phases in .claude/skills/tools/SKILL.md: 0-check, 1-choose, 2-ingest, 3-reconcile, 4-remeasure, ask, promote, and side tracks entity-lists, bilingual, search, route). Every recommendation names its evidence, what it may not do, and a verdict adopt / trial / park.`

const TOOLS = [
  { key: 'kge-semantica', task: `knowledge-graph-extract (.claude/skills/knowledge-graph-extract) and semantica (.venv-semantica).
1. For each document, have a free model extract triples in the skill's output format (read its SKILL.md and references/output-format.md) via \`python3 scripts/route.py complete --purpose kge --doc <slug> --json\` — the document may need chunking (the skill's manifest shows how). Write triples.jsonl and entities.jsonl under Plan/runs/tooltest/kge-semantica/<slug>/, run the skill's validate_triples.py and generate_cypher.py on them.
2. Score the entity names (subjects/objects) with entities.py score --names.
3. Load the triples into semantica with provenance: semantica.provenance.ProvenanceManager(storage_path=...) .track_entity(eid, source=<slug>, source_quote=...), semantica.kg.GraphBuilder(merge_entities=True, resolve_conflicts=False).build({...}). Run semantica.deduplication.DuplicateDetector and semantica.conflicts.ConflictDetector over the entities ONLY to measure what they would flag — list it, never act on it. Do not use GraphBuilderWithProvenance (it stamps every entity 'graph_construction').` },
  { key: 'grawiki', task: `grawiki (.venv-grawiki). Env OPENAI_BASE_URL=${PROXY}, OPENAI_API_KEY=route:grawiki:<slug>:<attempt>. Chat model string "openai/free" (slash), embedding "openai:local". Ingest each document into FalkorDBLite (grawiki.db.FalkorGraphDB(name, db_path=Plan/runs/tooltest/grawiki/<slug>/kg.db)) with GraphRAG(..., kg_output_language="German"). If the bundled redis/falkordb server does not start, that is NOT REACHED — report the error. Export the entity names, score them. Note how many model calls one document cost (python3 scripts/route.py ledger).` },
  { key: 'hyperextract', task: `Hyper-Extract (he, he-mcp) with the four project templates in Plan/hyperextract/ (read Plan/concept/hyperextract-templates_2026-09-24.md first — it says how each is scored).
Set TIKTOKEN_CACHE_DIR=$PWD/.venv-dspytools/lib/python3.12/site-packages/litellm/litellm_core_utils/tokenizers. Per document and attempt: he config llm -p openai -u ${PROXY} -k route:hyperextract:<slug>:<attempt> -m free ; he config embedder -p openai -u ${PROXY} -k route:hyperextract:<slug> -m local ; he parse Sources/drive/<slug>.md -t Plan/hyperextract/<Template>.yaml -l en -o Plan/runs/tooltest/hyperextract/<slug>/<Template>-a<attempt> --source <slug> --no-index.
Run TermCensus on both documents (score scope=world names; count lens apart), LocationRegistry on document 6 (score by code against the document's own master table at L185: which Location Name rows came back, and whether each source equals the table's Source cell exactly — write a small script under your folder), TermReadings on document 5 (place each quote with python3 scripts/read.py <slug> --find "<quote>"; count placed vs refused; compare placed lines with the lines Sources/notes/<slug>.md cites). StatedRelations on document 6 once: count relations, place their quotes, keep them for a person. Then with he-mcp tools or \`he info\`/\`he search\` on one Knowledge Abstract, say what the read side does. If he parse cannot run (forced tool calls, parsing), NOT REACHED with the error.` },
  { key: 'graphify-cgr', task: `graphify and code-graph-rag (cgr).
graphify: \`graphify extract scripts --code-only --out Plan/runs/tooltest/graphify-cgr/graphify-code\` (no model); report node/edge counts and whether its graph of scripts/ shows the pipeline (sources.py → capture.py → reconcile.py …). Then its document pass on each document: copy the document alone into Plan/runs/tooltest/graphify-cgr/<slug>/in/ and run with OPENAI_BASE_URL=${PROXY} OPENAI_API_KEY=route:graphify:<slug>:<attempt> graphify extract <that dir> --backend openai --model free --out <dir>; export its node names and score them; say how many edges are INFERRED vs EXTRACTED.
cgr: \`cgr index --repo-path . -o Plan/runs/tooltest/graphify-cgr/cgr-index\` restricted to scripts/ if it allows, and \`cgr verify-index\`. cgr cannot read markdown and \`check\`/\`start\` need Memgraph: say whether docker runs it here; if not, NOT REACHED. What could cgr give the 0-check phase (dangling callers, import cycles in scripts/)?` },
  { key: 'jev', task: `Jev as the judge layer (\`.venv-typesafe/bin/python scripts/route.py jev --purpose jev-judgements --doc <slug>\`, stdin {"state":..., "questions":...}; read .agents/skills/typesafe/SKILL.md first).
Take the 26 rows of Plan/runs/judgements.jsonl whose "document" is one of the two documents. For each: state = the two surfaces plus up to two lines of their context from that document (python3 scripts/read.py <slug> --find is how you find lines); question = a 3-level Score: "one term" / "related, a person decides" / "two terms", plus a Noul "is either not a term at all". Batch questions per document. Map the person's decisions: one-term, two-terms, judgement→middle, not-a-term→the Noul. Report agreement per class with both difference lists by surface pair (P27), and the probabilities where Jev and the person differ. Also run jev-decide setup (presence only). Record Jev's input tokens from the ledger.` },
  { key: 'opencode-omo', task: `OpenCode 1.18.32 + oh-my-openagent. NON-CORPUS task only: never give it a Sources/ or Wiki/ file.
Provider via env, not the config file: OPENCODE_CONFIG_CONTENT='{"provider":{"route":{"npm":"@ai-sdk/openai-compatible","name":"route","options":{"baseURL":"${PROXY}","apiKey":"route:opencode:-:1"},"models":{"free":{"name":"free","tool_call":true,"limit":{"context":128000,"output":8192}}}}}}'.
Run 1 with the plugin: opencode run -m route/free --format json "Explain in five sentences what scripts/route.py does." — and see in python3 scripts/route.py ledger whether its calls came through the proxy; note any call that went elsewhere (fallback models, subagents, npm/models.dev). Run 2 with OPENCODE_PURE=1 (no plugin). If a run stalls on a permission prompt, retry with --auto. Report what the plugin adds or breaks here, and whether OpenCode could ever be a second harness for this repository's loop under its rules.` },
  { key: 'notion', task: `The Notion connector (mcp__Notion__* via ToolSearch) and the four vendored Notion skills (knowledge-capture, meeting-intelligence, research-documentation, spec-to-implementation). READ-ONLY and NO corpus text: use notion-get-tool-access and notion-search for "Kohärenz" to see what the workspace already holds; do not create, update or comment. Read the four SKILL.md files. Review on paper: where Notion could hold something this repository keeps in NOW.md / Plan/decisions / Wiki/questions, and why the two-layer rule (Sources/, Wiki/; Notion outside both) limits it. Name the one use you would trial, if any.` },
  { key: 'install', task: `scripts/install.sh and .claude/hooks/session-start.sh. Run scripts/install.sh --check and --list; time one reinstall of a cheap component (e.g. \`scripts/install.sh jev\` after checking it is present — use a component that reinstalls in seconds); run python3 scripts/selftests.py and paste its summary. Review: what a fresh container still lacks, the cold-cache time that is unmeasured, and whether the hook should stay synchronous.` },
]

const SCHEMA = {
  type: 'object',
  properties: {
    tool: { type: 'string' },
    reached: { type: 'string', enum: ['yes', 'partial', 'no'] },
    runs: { type: 'array', items: { type: 'object', properties: {
      doc: { type: 'string' }, command: { type: 'string' }, outcome: { type: 'string' }, seconds: { type: 'number' } },
      required: ['command', 'outcome'] } },
    scores: { type: 'array', items: { type: 'object', properties: {
      doc: { type: 'string' }, what: { type: 'string' }, gold: { type: 'integer' }, model: { type: 'integer' },
      shared: { type: 'integer' }, precision: { type: 'number' }, recall: { type: 'number' }, f1: { type: 'number' },
      refused: { type: 'integer' } }, required: ['doc', 'what'] } },
    ledger_purpose: { type: 'string' },
    review_path: { type: 'string' },
    recommendations: { type: 'array', items: { type: 'object', properties: {
      step: { type: 'string' }, proposal: { type: 'string' }, evidence: { type: 'string' },
      may_not: { type: 'string' }, effort: { type: 'string' },
      verdict: { type: 'string', enum: ['adopt', 'trial', 'park'] } },
      required: ['step', 'proposal', 'evidence', 'verdict'] } },
    not_reached: { type: 'string' },
  },
  required: ['tool', 'reached', 'runs', 'review_path', 'recommendations'],
}

phase('Test')
log(`${TOOLS.length} tool groups on ${DOCS.join(' + ')} through ${PROXY}`)
const tested = await pipeline(TOOLS, (t) => agent(
  `You test one tool group installed in this repository on 2026-09-24, on two German research documents, and write a measured review.\n\nTOOL: ${t.task}\n\n${RULES.replace(/<your-tool>/g, t.key)}\n\nReturn the structured result; review_path is the file you wrote.`,
  { label: t.key, phase: 'Test', model: 'sonnet', effort: 'medium', schema: SCHEMA }))
const results = tested.filter(Boolean)
const missing = TOOLS.filter((t, i) => !tested[i]).map((t) => t.key)
if (missing.length) log(`no result from: ${missing.join(', ')}`)

phase('Check')
const recs = results.flatMap((r) => (r.recommendations || []).map((x, i) => ({ id: `${r.tool}#${i + 1}`, tool: r.tool, ...x })))
log(`${recs.length} recommendations to check against their evidence`)
const checked = recs.length ? await agent(
  `You run one mechanical step. Do not judge anything yourself.

For the recommendations below, call Jev through the router, in batches of at most 20 per call:
  .venv-typesafe/bin/python scripts/route.py jev --purpose tool-review-check --doc -   (stdin: {"state": ..., "questions": ...})
state: {"<id>": {"proposal": ..., "evidence": ..., "may_not": ...}} for the batch.
questions: one per id, {"type": "score", "instructions": "Recommendation <id> in the state: is its proposal supported by the evidence it cites — measured facts from runs described there — rather than by expectation?", "criteria": ["not supported: the evidence does not bear on the proposal, or there is none", "partly: the evidence supports part of it, or it rests on one run", "supported: the evidence is measured and bears directly on the proposal"]}.
If the router refuses or Jev is unreached, record that per id — never substitute your own opinion.

Write the full list with Jev's expected level and probabilities to Plan/runs/tooltest/check.json and return it.

RECOMMENDATIONS:
${JSON.stringify(recs, null, 1)}`,
  { label: 'jev-check', phase: 'Check', model: 'haiku', effort: 'low', schema: {
    type: 'object', properties: { checks: { type: 'array', items: { type: 'object', properties: {
      id: { type: 'string' }, level: { type: 'string' }, score: { type: 'number' }, unreached: { type: 'string' } },
      required: ['id'] } } }, required: ['checks'] } }) : { checks: [] }

phase('Synthesize')
const synthesis = await agent(
  `Write Plan/concept/tool-review_${DATE}.md: the review the author asked for — what this repository could implement in its main workflows, from the tools tested today.

Read every per-tool review in Plan/concept/tool-review_${DATE}/, Plan/runs/tooltest/check.json (Jev's score per recommendation — show it beside each proposal; never drop one because of it), and the output of \`python3 scripts/route.py ledger\` (cost per purpose; it must say $0.000000 — if not, lead with that).

Structure: one short opening (what was tested, on which two documents, under decision 007, at what cost). Then one section per phase of the loop (.claude/skills/tools/SKILL.md: 0-check, 1-choose, 2-ingest, 3-reconcile, 4-remeasure, ask, promote; then side tracks) — for each: what could be implemented, with its evidence and numbers, the tool, its Jev score, the CLAUDE.md limit it must respect, and adopt/trial/park. Then answer the tools skill's "What is missing" list directly: can anything tested close "phase 1 is not automated", "ask does not exist", "extraction is not trainable — one usable gold list"? Then "Not reached" with each reason (P15), and "Questions for the author" (P0).

Every number from a review or a command, with its source. A model's output supplies no page, link or count, and conflict detection is never mechanised — a proposal that breaks either is listed as rejected, with why. English, plain, no filler. Return a one-paragraph summary.

Tester results (structured): ${JSON.stringify(results, null, 1)}
Not returned: ${JSON.stringify(missing)}`,
  { label: 'synthesis', phase: 'Synthesize' })

return { reached: results.map((r) => `${r.tool}: ${r.reached}`), missing, checks: (checked && checked.checks) || [], synthesis }
