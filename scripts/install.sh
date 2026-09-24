#!/usr/bin/env bash
# Install everything a fresh container lacks. Idempotent: a component already
# present is skipped, so a second run costs seconds.
#
#   scripts/install.sh                  # every component below except qmd-models
#   scripts/install.sh derived tools    # only the named components
#   scripts/install.sh --check          # report what is present, change nothing
#   scripts/install.sh --list           # the components and what each is for
#
# The same script runs at cloud session start (.claude/hooks/session-start.sh),
# so what a session gets and what a person gets are one list, not two.
#
# Every Python dependency goes into a virtualenv or a uv tool environment,
# never the system interpreter — `pip install --break-system-packages` once
# broke `cryptography` for the whole container (CLAUDE.md, *Installing anything*).
#
# A component that fails is reported and the rest still run; the exit status is
# non-zero if any failed. No key is read or printed here: OPENROUTER_API_KEY and
# TYPESAFE_API_KEY come from the environment's settings, never from a file.
set -uo pipefail

ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
cd "$ROOT"
export NPM_CONFIG_UPDATE_NOTIFIER=false NPM_CONFIG_FUND=false NPM_CONFIG_AUDIT=false

# Pins. Each is also written in CLAUDE.md beside the reason for it.
DSPY_VERSION="3.3.1"
JEV_TAG="v0.2.0"
GRAPHIFY_REF="4c735618f3d56fd622c2049771584621c31ba9ff"
GRAWIKI_REF="920d181b7e82943f3557ce4debaaabfdeb924cde"
HYPEREXTRACT_REF="395039ea49709b279971631a47569b931818abbb"
SEMANTICA_VERSION="0.7.0"

# name | what it is for — the order is the install order
COMPONENTS=(
  "derived|Plan/derived/ — corpus.py's index path (python3 scripts/derive.py)"
  "tools|.venv-tools — markitdown, for sources.py land"
  "typesafe|.venv-typesafe — typesafe-sdk, for bilingual.py and jev_entities.py"
  "dspy|.venv-dspy — DSPy $DSPY_VERSION, dspy-skills, strictyaml, drg-kg[extract]"
  "dspytools|.venv-dspytools (python 3.12) — dspytools"
  "grawiki|.venv-grawiki (python 3.12) — grawiki[falkordblite,viz], CPU torch"
  "semantica|.venv-semantica (python 3.12) — semantica $SEMANTICA_VERSION, base package"
  "jev|jev-decide CLI (uv tool) — the vendored jev* skills in API mode"
  "graphify|graphify CLI (uv tool) — the vendored graphify skill"
  "cgr|code-graph-rag CLI (uv tool, python 3.12) — cgr"
  "hyperextract|he and he-mcp (uv tool, python 3.12) — Hyper-Extract, the hyper-extract MCP server"
  "qmd|qmd package in .tools-node and the /usr/local/bin/qmd shim"
  "qmd-models|qmd's ~2.1 GB models, index and embeddings — not in the default set"
)
DEFAULT_SKIP="qmd-models"

say() { printf '  %-13s %s\n' "$1" "$2"; }
have() { command -v "$1" >/dev/null 2>&1; }

need_uv() {
  have uv && return 0
  echo "uv is not on PATH — install it (https://docs.astral.sh/uv/) and rerun" >&2
  return 1
}

# ---- presence checks: one per component, used by --check and to skip work ----
present() {
  case "$1" in
    derived)    [[ -d Plan/derived ]] && [[ -n "$(ls -A Plan/derived 2>/dev/null)" ]] ;;
    tools)      .venv-tools/bin/python -c "import markitdown" 2>/dev/null ;;
    typesafe)   .venv-typesafe/bin/python -c "import typesafe_sdk" 2>/dev/null ;;
    dspy)       .venv-dspy/bin/python -c "import dspy, dspy_skills, strictyaml, drg; assert dspy.__version__ == '$DSPY_VERSION'" 2>/dev/null ;;
    dspytools)  [[ -x .venv-dspytools/bin/dspytools ]] ;;
    grawiki)    .venv-grawiki/bin/python -c "import grawiki, redislite" 2>/dev/null ;;
    semantica)  .venv-semantica/bin/python -c "import importlib.metadata as m; assert m.version('semantica') == '$SEMANTICA_VERSION'; import semantica" 2>/dev/null ;;
    jev)        have jev-decide ;;
    graphify)   have graphify ;;
    cgr)        have cgr ;;
    hyperextract) have he && have he-mcp ;;
    qmd)        [[ -x .tools-node/node_modules/.bin/qmd ]] && [[ -x /usr/local/bin/qmd ]] ;;
    qmd-models) scripts/setup_qmd.sh --check 2>/dev/null | grep -q "embeddings *complete" ;;
    *)          return 2 ;;
  esac
}

# ---- installers ----
install_one() {
  case "$1" in
    derived)
      python3 scripts/derive.py >/dev/null ;;
    tools)
      need_uv || return 1
      [[ -x .venv-tools/bin/python ]] || uv venv -q --python 3.11 .venv-tools || return 1
      uv pip install -q --python .venv-tools/bin/python 'markitdown[docx,pdf,pptx,xlsx]' ;;
    typesafe)
      need_uv || return 1
      [[ -x .venv-typesafe/bin/python ]] || uv venv -q --python 3.11 .venv-typesafe || return 1
      uv pip install -q --python .venv-typesafe/bin/python \
        git+https://github.com/typesafe-ai/typesafe-sdk-python ;;
    dspy)
      need_uv || return 1
      local py=.venv-dspy/bin/python
      [[ -x $py ]] || uv venv -q --python 3.11 .venv-dspy || return 1
      uv pip install -q --python $py "dspy==$DSPY_VERSION" strictyaml || return 1
      # --no-deps is load-bearing: the package asks for dspy-ai>=2.5.0, the old
      # distribution name, and resolving it would move the venv off the pin.
      uv pip install -q --python $py --no-deps \
        git+https://github.com/netzkontrast/dspy-skills-implementation- || return 1
      uv pip install -q --python $py "drg-kg[extract] @ git+https://github.com/netzkontrast/drg-kg" || return 1
      $py -c "import dspy; assert dspy.__version__ == '$DSPY_VERSION', dspy.__version__" ;;
    dspytools)
      need_uv || return 1
      [[ -x .venv-dspytools/bin/python ]] || uv venv -q --python 3.12 .venv-dspytools || return 1
      uv pip install -q --python .venv-dspytools/bin/python git+https://github.com/netzkontrast/dspytools ;;
    grawiki)
      need_uv || return 1
      [[ -x .venv-grawiki/bin/python ]] || uv venv -q --python 3.12 .venv-grawiki || return 1
      # chonkie[st] pulls sentence-transformers and so torch; the CPU build is
      # a fraction of the CUDA one and a cloud container has no GPU.
      uv pip install -q --python .venv-grawiki/bin/python --torch-backend cpu \
        "grawiki[falkordblite,viz] @ git+https://github.com/netzkontrast/grawiki@$GRAWIKI_REF" ;;
    semantica)
      need_uv || return 1
      [[ -x .venv-semantica/bin/python ]] || uv venv -q --python 3.12 .venv-semantica || return 1
      uv pip install -q --python .venv-semantica/bin/python "semantica==$SEMANTICA_VERSION" ;;
    jev)
      need_uv || return 1
      local src; src="$(mktemp -d)"
      git -c advice.detachedHead=false clone -q --depth 1 --branch "$JEV_TAG" https://github.com/wuyoscar/jev-skill "$src/jev-skill" \
        && uv tool install -q "$src/jev-skill"
      local rc=$?; rm -rf "$src"; return $rc ;;
    graphify)
      need_uv || return 1
      uv tool install -q --python 3.12 \
        "graphifyy @ git+https://github.com/netzkontrast/graphify@$GRAPHIFY_REF" ;;
    cgr)
      need_uv || return 1
      # Without the transformers floor the resolver backtracks to 4.12.2, whose
      # tokenizers 0.10.3 needs a Rust build that fails; 3.11 is refused outright.
      uv tool install -q --python 3.12 "code-graph-rag[treesitter-full,semantic]" \
        --with "transformers>=4.40" ;;
    hyperextract)
      need_uv || return 1
      uv tool install -q --python 3.12 \
        "hyperextract[mcp,ingest,anthropic] @ git+https://github.com/netzkontrast/Hyper-Extract@$HYPEREXTRACT_REF" ;;
    qmd)
      scripts/setup_qmd.sh --package ;;
    qmd-models)
      scripts/setup_qmd.sh ;;
  esac
}

# ---- arguments ----
CHECK=0; WANT=()
for a in "$@"; do
  case "$a" in
    --check) CHECK=1 ;;
    --list)  for c in "${COMPONENTS[@]}"; do say "${c%%|*}" "${c#*|}"; done; exit 0 ;;
    -h|--help) sed -n '2,9p' "$0" | sed 's/^# \{0,1\}//'; exit 0 ;;
    *) WANT+=("$a") ;;
  esac
done

names=()
for c in "${COMPONENTS[@]}"; do names+=("${c%%|*}"); done
if [[ ${#WANT[@]} -eq 0 ]]; then
  for n in "${names[@]}"; do
    [[ " $DEFAULT_SKIP " == *" $n "* ]] && [[ $CHECK -eq 0 ]] && continue
    WANT+=("$n")
  done
fi
for w in "${WANT[@]}"; do
  [[ " ${names[*]} " == *" $w "* ]] || { echo "unknown component: $w (see --list)" >&2; exit 2; }
done

# ---- run ----
failed=()
for n in "${WANT[@]}"; do
  if present "$n"; then say "$n" "ok"; continue; fi
  if [[ $CHECK -eq 1 ]]; then say "$n" "MISSING"; continue; fi
  start=$SECONDS
  if install_one "$n" && present "$n"; then
    say "$n" "installed ($((SECONDS - start))s)"
  else
    say "$n" "FAILED ($((SECONDS - start))s)"; failed+=("$n")
  fi
done

if [[ ${#failed[@]} -gt 0 ]]; then
  echo "failed: ${failed[*]} — rerun: scripts/install.sh ${failed[*]}" >&2
  exit 1
fi
exit 0
