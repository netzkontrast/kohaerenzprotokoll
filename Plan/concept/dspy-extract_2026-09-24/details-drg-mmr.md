# drg-kg side effects, and the MMR λ convention

Background read first: `das-rlm-rag.md`, sections RAG, PROD, TRAP and "Code
worth keeping" (drg-kg auto-config; the pack's MMR vs. upstream refrag).

Method note: every claim below is either a `grep -n`/`sed -n` citation against
installed or cloned source, or the printed output of a script that was
actually executed (path given, reproducible). Nothing here made or could make
a live model call: every probe ran with `OPENROUTER_API_KEY`, `TYPESAFE_API_KEY`,
`OPENAI_API_KEY`, `ANTHROPIC_API_KEY` (and, defensively, `GEMINI_API_KEY`,
`PERPLEXITY_API_KEY`) unset, and with `litellm.completion`/`litellm.acompletion`
monkey-patched to raise before any drg-related import. No file under
`/home/user/kohaerenzprotokoll`, `/home/user/dspy-agent-skills`, or any other
repository under `/home/user` was modified; all scratch work is under
`<scratchpad>/`.

---

## A. drg-kg side effects, as this repository uses it

### A.1 — is drg-kg installed in `.venv-dspy`?

No.

```
$ /home/user/kohaerenzprotokoll/.venv-dspy/bin/python -c "import drg"
ModuleNotFoundError: No module named 'drg'
```

`.venv-dspy` currently holds only `dspy==3.3.1` (checked with
`importlib.metadata`); `drg-kg` was never installed there, and this probe did
**not** install it there.

Built the scratch venv exactly as instructed, at
`<scratchpad>/venvs/drgcheck`:

```
uv venv --python 3.11 drgcheck
uv pip install --python drgcheck/bin/python 'dspy[numpy]==3.3.1'
uv pip install --python drgcheck/bin/python "drg-kg[extract] @ git+https://github.com/netzkontrast/drg-kg"
```

Result: `dspy==3.3.1`, `numpy==2.4.6`, `tiktoken==0.14.0` (the `[extract]`
marker), `drg-kg==0.0.0.dev51` from
`git+https://github.com/netzkontrast/drg-kg@4d6970bcc6c4a5c96940d8d4f551a3c413f6d956`
— the same commit (`g4d6970bcc`) the reader's notes cite, confirmed via that
dist's `direct_url.json`. This is the exact spec `CLAUDE.md` names (no ref
pinned there, so HEAD-of-default-branch at install time; that HEAD is still
this commit). All source paths below are inside this venv's
`site-packages/drg/`.

### A.2 — measured side effects of the import and the call

**Harness**: cwd = a fresh temp dir holding `.env` with `DRGCHECK_SENTINEL=1`;
`*_API_KEY` unset as above; `litellm.completion`/`.acompletion` replaced by a
function that records the call and raises, installed *before* `dspy` or `drg`
is imported. Script:
`<scratchpad>/extract/probe_drg/probe.py`. Full run:

| stage | `dspy.settings.lm` | `DRGCHECK_SENTINEL` in `os.environ` | litellm called? |
|---|---|---|---|
| baseline (`import dspy`) | `None` | unset | no |
| **(a)** `import drg` | `None` (unchanged) | unset (unchanged) | no |
| **(b)/(c)** `from drg.evaluation._runner import _score_sets, _prf` | `None` (unchanged) | unset (unchanged) | no |
| **(d)** `_score_sets(gold, pred, key_fn=str.lower)` | `None` (unchanged) | unset (unchanged) | no |

Answers to A.2, literally:

- **(a)** No. Neither `import drg` nor the `_runner` import changes
  `dspy.settings.lm`; it is `None` before, during and after.
- **(b)** No. `DRGCHECK_SENTINEL` is `None` in `os.environ` at every stage —
  `.env` is never loaded by this import path.
- **(c)** No. The patched `litellm.completion`/`.acompletion` were never
  called (`_litellm_calls == []` throughout).
- **(d)**, same three questions for the call itself: also no, no, no — the
  call is a pure function. It returns (verified output, exact):

  ```
  precision=0.6667 recall=0.6667 f1=0.6667
  tp=2 fp=1 fn=1
  details = {'false_positive_keys': ['nexus'], 'false_negative_keys': ['aegis']}
  ```
  for `gold=["Juna","Kael","AEGIS"]`, `pred=["juna","kael","Nexus"]`,
  `key_fn=str.lower` — matching `_prf`'s formula by hand-check. `_prf(0,0,0)`
  also reproduced as `(0.0, 0.0, 0.0)` (drg's non-vacuous scorer, confirmed
  again on this fresh install).

**Why** (import-chain evidence, this installed copy, `drg-kg==0.0.0.dev51`):

- `drg/__init__.py` imports `.graph` (`KG`) and `.schema` at module level;
  `extract_typed`, `KGExtractor`, `.extract`, `.config`-touching names are
  lazy, resolved only via `__getattr__`'s `lazy_imports` dict (grepped: no
  `.config`/`.extract` entry point is imported eagerly).
- `import drg` **does** put `dspy` in `sys.modules` — but only because
  `drg/graph/relationship_model/_llm_based.py:29-34` does a bare
  `try: import dspy; ... except Exception: DSPY_AVAILABLE = False`, reached
  eagerly via `drg/__init__.py:55 → drg/graph/__init__.py:69 →
  drg/graph/relationship_model/__init__.py:33`. This import is harmless: it
  never calls `dspy.configure`, never touches `.env`, never builds an LM.
- `drg/evaluation/__init__.py:27-49` imports `._compare`, `._io`, `._runner`,
  `._types`, `.graph` (a *different* module,
  `drg/evaluation/graph.py:14` → `from ..graph.validation import
  validate_graph_data`) and `.ontology`
  (`drg/evaluation/ontology.py:14` → `from ..schema import ...`). None of
  these — nor `_runner.py` itself (`drg/evaluation/_runner.py:14-22`, stdlib
  only: `time`, `uuid`, `collections.Counter`, `typing`) — imports
  `drg.config` or `drg.extract`. Confirmed directly: after the `_runner`
  import, `"drg.config" in sys.modules` and `"drg.extract" in sys.modules`
  are both `False`.
- The code that *does* the things CLAUDE.md/the reader describe —
  `load_dotenv(".env", override=False)`, `DRG_MODEL` default
  `"openai/gpt-4o-mini"`, `dspy.configure(lm=lm)` — is
  `drg/config.py`'s `LMConfig._configure_unsafe`
  (`drg/config.py:70,74,77,224,230`), reached only via
  `drg/config.py:238` `configure_lm()` ← `drg/extract/__init__.py:1026-1031`
  `_configure_llm_auto()` ← call sites at `extract/__init__.py:175` and
  `:1051` (both inside `drg.extract`, never inside `drg.evaluation`).

**Contrast, run for completeness** (script `probe_danger.py`, same harness):
calling `drg.config.configure_lm()` directly — i.e. taking the one step the
scorer path never takes —

```
dspy.settings.lm BEFORE: None
UserWarning: Cloud model (openai/gpt-4o-mini) selected but OPENAI_API_KEY not found. ...
dspy.settings.lm AFTER:  <dspy.clients.lm.LM object at 0x...>
DRGCHECK_SENTINEL AFTER configure_lm(): '1'        # .env WAS loaded
dspy.settings.lm("hello") -> LMUnexpectedError: [openai/gpt-4o-mini] PROBE: litellm.completion called
```

This is the exact behaviour the reader's notes describe (`drg/config.py:59-230`,
`drg/extract/__init__.py:171-203,1026-1033`) — freshly reproduced here, on
this install, with a real (patched-to-fail) call reaching `litellm.completion`
via `dspy.LMUnexpectedError` (matching DSPy 3.3.1's error-wrapping rule).
It confirms the danger is real **and** that it lives entirely outside the
import path `rlm_ingest.py` actually uses.

### A.3 — the smallest safe way for `rlm_ingest.py score()`

**The import has no side effects, so no change is needed.** The code already
in `/home/user/kohaerenzprotokoll/scripts/rlm_ingest.py:317-332` (the `score`
function; the import/call that matter are lines 322-324 and 332) —

```python
try:
    from drg.evaluation._runner import _score_sets
except ImportError:
    raise SystemExit("drg-kg is not installed in this interpreter")
...
metric = _score_sets(gold, pred, key_fn=fold)
```

— are already the smallest safe way: a submodule import that, on this
version, never crosses into `drg.config`/`drg.extract`, and a pure-function
call. (Today this simply raises `SystemExit` in the real `.venv-dspy`, since
drg-kg isn't installed there — see A.1.)

If a future drg-kg release ever changes `drg/evaluation/__init__.py` to reach
`drg.config` (e.g. if evaluation grew a dependency on extraction), two
fallbacks, ranked:

1. **Bypass the package `__init__` chain with `importlib.util.spec_from_file_location`**
   pointed straight at `.../drg/evaluation/_runner.py`. This does not fully
   work as a drop-in, though: `_runner.py` uses a relative import
   (`from ._types import (...)`, line 22), so the loaded module still needs
   `__package__` set to `"drg.evaluation"` and that package's `__init__`
   partially satisfied — in practice this becomes "load `_types.py` the same
   way first," which is only a little less code than option 2 and more
   fragile to drg-kg's internal layout changing.
2. **Reimplement the set arithmetic**, stdlib-only. Built and verified
   byte-for-byte against the installed scorer (script `probe_drg/reimpl.py`,
   counted with `cat -n`): a minimal `MetricResult`-shaped dataclass
   (9 lines, `:9-17`) + `_prf` (6 lines, `:20-25`) + `_score_sets`
   (13 lines, `:28-40`) + 2-3 stdlib imports = **about 30 lines** of pure
   `collections.Counter`/`dataclasses` code (49 total with the module
   docstring and a `__main__` self-test block). Run against the same
   `gold`/`pred`/`key_fn=str.lower` fixture as A.2(d), it returned the
   identical tuple `(precision=0.6667, recall=0.6667, f1=0.6667, tp=2, fp=1,
   fn=1, false_positive_keys=['nexus'], false_negative_keys=['aegis'])`.

### A — verdict

1. The exact import `rlm_ingest.py` uses,
   `from drg.evaluation._runner import _score_sets`, has zero measured side
   effects — `dspy.settings.lm` stays `None`, `.env` is never read, and
   `litellm` is never touched, both for the import and for calling
   `_score_sets(...)`.
2. The side effects CLAUDE.md/the reader describe (global-LM mutation, `.env`
   read, an attempted live call) are real and freshly reproduced here, but
   they live on a separate path (`drg.config.configure_lm()`, reached only
   through `drg.extract`'s auto-config) that the scorer import never touches.
3. No code change is needed in `rlm_ingest.py`'s `score()`; the ranked
   fallback if that ever stops being true is a verified ~30-line stdlib
   reimplementation, not a submodule-loader trick.

---

## B. The MMR λ convention

### B.1 — three implementations, side by side

| | upstream refrag | dspy-agent-skills (`kp_canon_retriever.py`) | kohaerenzprotokoll (`graphrag.py`) |
|---|---|---|---|
| file | `dspy-refrag@a8688133`, `src/dspy_refrag/sensor_advanced.py` (cloned at `<scratchpad>/src/dspy-refrag`, confirmed commit `a8688133a3fb642866b78463fe499a5c42783549`, clean vs. HEAD) | `/home/user/dspy-agent-skills/scaffolding/kp_canon_retriever.py` | `/home/user/kohaerenzprotokoll/scripts/graphrag.py` |
| function | `AdvancedSensor._select_mmr` (def at `:129`, formula `:166`, `lambda_param` at `:148`) | `select_mmr` (def `:92-95`, formula `:138`) | `select_mmr` (def `:158-160`, formula `:175`) |
| formula | `mmr = λ·relevance − (1−λ)·redundancy` | `score = (1−λ)·relevance − λ·redundancy` | `score = (1−λ)·relevance − λ·redundancy` |
| λ weights | **relevance** (higher λ → less diverse) | **redundancy-avoidance / diversity** (higher λ → more diverse) | same as kp_canon_retriever — **diversity** |
| default λ | `0.5` (`SelectionConfig.diversity_lambda`, `:31`) | `0.65` (`DEFAULT_DIVERSITY_LAMBDA`, `:55`, comment `:51-54`) | `0.65` (`DIVERSITY_LAMBDA`, `:68`) |
| floor field | `min_score: Optional[float] = None` (`:35`) | `min_relevance: float = 0.15` (`DEFAULT_MIN_RELEVANCE`, `:59`) | `min_relevance: float = 0.15` (`MIN_RELEVANCE`, `:69`) |
| floor applied? | **Only in `_select_similarity`** (`:106-127`, check at `:117-118`). `_select_mmr` (`:129-174`) never reads `self.config.min_score` — grepped, zero occurrences in that span. Freshly confirmed by running `AdvancedSensor` with `strategy=MMR, min_score=0.15` vs. without: **identical output at every λ tested**; with `strategy=SIMILARITY, min_score=0.35` it *does* filter (returned only the 2 candidates ≥0.35, dropping "distinct" 0.30 and "unrelated" 0.0). | Excludes candidates below the floor **before** the MMR loop runs (`eligible = [...]`, `:126-127`; `if not eligible: return []`, `:128`) — λ plays no part in the floor. | Identical mechanism, same shape: `remaining = [i for i, r in enumerate(relevance) if r >= min_relevance]` (`:169`), before the `while` loop. |

`kp_canon_retriever.py:92-95,138` and `graphrag.py:158-160,175` are the same
formula on different call shapes (raw vectors vs. precomputed
relevance/similarity-callable) — confirmed dynamically below, not just by
inspection.

Bonus, found while reading `sensor_advanced.py` directly: upstream's own
`example_usage()` calls `diversity_lambda=0.7` **"High diversity"**
(`sensor_advanced.py:303-305`) — but by upstream's own formula (line 166),
λ=0.7 weights *relevance* more and *redundancy* less, i.e. it is **less**
diverse than λ=0.5, not more. Upstream's own example comment gets its own λ
backwards.

### B.2 — offline sweep against graphrag.py's own live code

Script: `<scratchpad>/extract/probe_mmr/sweep.py`, run with
`.venv-dspy`'s interpreter (`sys.dont_write_bytecode = True`, no files
written under `/home/user`), importing the real
`scripts/graphrag.py:select_mmr` — not a re-implementation. Two fixtures,
0=dup0, 1=dup1, 2=distinct, 3=unrelated, λ swept 0.30→0.90 step 0.05 plus the
finer points 0.47/0.48/0.49/0.498/0.50/0.53/0.534/0.54 used by the reader's
notes; budget=2.

**Fixture A — graphrag.py's own `selftest()` fixture, verbatim**
(`scripts/graphrag.py:374-376`: `relevance=[0.9,0.88,0.6,0.0]`,
`sim={(0,1):.97,(0,2):.5,(1,2):.5}`):

| floor | λ≤0.35 | 0.40–0.54 | λ≥0.55 |
|---|---|---|---|
| off (0.0) | dup0+dup1 | **dup0+distinct** | dup0+unrelated |
| on (0.15) | dup0+dup1 | dup0+distinct | dup0+distinct *(never flips to unrelated, any λ up to 1.0)* |

`python3 scripts/graphrag.py selftest` (the standard interpreter, run
read-only from the repo) still passes: `9 of 9 cases hold`, exit 0 — its two
MMR assertions (`3 in select_mmr(..., λ=0.65, floor=0.0)` and
`select_mmr(..., λ=0.65) == [0, 2]`) match this table at λ=0.65.

**Fixture B — the reader's exact vectors**
(`scratchpad/probe/mmr_probe.py:10-11`: `q=[1,0,0]`,
`C=[[.99,.10,0],[.98,.12,0],[.30,.95,0],[0,0,1]]`; relevance/pairwise
recomputed fresh from these vectors, not copied from the notes):

| floor | λ≤0.498 | λ≥0.50 |
|---|---|---|
| off (0.0) | dup0+dup1 | dup0+unrelated |

| floor | λ≤0.53 | λ≥0.534 |
|---|---|---|
| on (0.15) | dup0+dup1 | dup0+distinct |

This **exactly reproduces** the reader's "analytic crossover ≈0.534" and
"analytic unguarded switch ≈0.498" — now against `graphrag.py`'s own
`select_mmr`, not only `kp_canon_retriever.py`'s copy. It never reaches
"distinct" without the floor, at any λ tested (0.0–1.0).

**Fresh run of the real upstream `AdvancedSensor.select` on the same Fixture-B
vectors** (script `upstream_sweep.py`, `dspy-refrag@a8688133`, not a
reimplementation):

| | λ≤0.50 | λ≥0.53 |
|---|---|---|
| `min_score` unset | dup0+unrelated | dup0+dup1 |
| `min_score=0.15` | dup0+unrelated | dup0+dup1 |

Identical row-for-row with and without `min_score` — confirms upstream MMR
ignores it entirely, freshly. The flip direction is the mirror image of the
pack's (low λ → unrelated upstream vs. low λ → dup1 in the pack), which is the
directly-observed signature of the inverted formula in B.1. (Contrast:
`strategy=SIMILARITY, min_score=0.35, budget=4` on the same vectors returned
only `[dup0, dup1]` — upstream's floor works, just not for MMR.)

**Docstring claim 1** (`graphrag.py:18-21`): *"plain MMR picks an unrelated
passage over a relevant near-duplicate at every λ from 0.5 to 0.8"* — this
sentence's "measured there" points at `kp_canon_retriever.py`, i.e. Fixture
B's shape, not at graphrag.py's own bundled numbers. Checked both, floor off,
λ ∈ {0.50, 0.55, 0.60, 0.65, 0.70, 0.75, 0.80}:

- **Fixture B (the fixture actually cited): holds at every step** — all seven
  λ give `dup0+unrelated`.
- **Fixture A (graphrag.py's own selftest fixture): does not hold at λ=0.50**
  — there the choice is `dup0+distinct`, and only flips to `dup0+unrelated`
  from λ=0.55 up. So the claim is true of the fixture it cites and false, at
  exactly one boundary point, of the numbers graphrag.py ships in its own
  selftest.

**Docstring claim 2** (`graphrag.py:68`): *"`DIVERSITY_LAMBDA = 0.65` …
above upstream's 0.5"* — true as bare numbers (0.65 > 0.5), but the two λ's
are not on a shared scale: they are related by λ ↦ 1−λ (B.1). Under that
substitution, the pack's 0.65 corresponds to upstream's 0.35 — **below**
upstream's default, not above it. The comment is arithmetically correct and
semantically misleading in the same breath.

### B — verdict

1. `graphrag.py`'s `select_mmr` is a faithful, behaviourally-identical port of
   `kp_canon_retriever.py`'s (same inverted formula, same floor-before-loop
   mechanism) — confirmed dynamically: run against the real code, it
   reproduces the reader's λ≈0.534/λ≈0.498 crossovers exactly on the fixture
   it cites, and its own bundled `selftest()` still passes 9/9.
2. That formula is the mirror image of upstream's (`λ·relevance −
   (1−λ)·redundancy`, λ weights relevance) — freshly confirmed by running the
   real `AdvancedSensor` on the same vectors: it flips in the opposite
   direction and, unlike the pack, never applies `min_score` inside MMR at
   all (identical output with/without it; only `SIMILARITY` strategy honours
   the floor upstream).
3. The code is internally consistent; the docstring is fixture-specific
   rather than general and one comparison in it is misleading:
   "at every λ from 0.5 to 0.8" holds on the fixture it cites but not at
   λ=0.5 on graphrag.py's own selftest numbers, and "above upstream's 0.5"
   compares 0.65 against 0.5 on two conventions that run in opposite
   directions (0.65 packward ≈ 0.35 upstream-ward — below, not above).
