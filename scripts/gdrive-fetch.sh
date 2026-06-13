#!/usr/bin/env bash
# gdrive-fetch.sh — decode Google Drive MCP `download_file_content` results
# to disk via pipes, so file content never enters the model context.
#
# Background: the Drive MCP tool returns JSON {content: <base64>, title,
# mimeType, id}. For any real document the result exceeds the context token
# limit and the harness saves it to a tool-results/*.txt path instead of
# inlining it. This script consumes those JSON files (or stdin) and writes
# the decoded document straight to the target directory. Only the one-line
# summaries cross back into context.
#
# Usage:
#   scripts/gdrive-fetch.sh -o Canon path/to/tool-result.txt [more.txt ...]
#   cat tool-result.txt | scripts/gdrive-fetch.sh -o Canon -
#   scripts/gdrive-fetch.sh -o Canon -n override-name.md result.txt
#
# Options:
#   -o DIR   output directory (default: .)
#   -n NAME  override output filename (single input only; default: .title)
#
# Recommended Claude workflow:
#   1. call download_file_content with exportMimeType "text/markdown"
#      (preserves headings; "text/plain" flattens them)
#   2. the oversized result lands in .../tool-results/<name>.txt
#   3. run this script on that path — never `cat`/Read the result file
#
# Output is normalized: UTF-8 BOM stripped, CRLF -> LF.

set -euo pipefail

outdir="."
name=""
while getopts "o:n:" opt; do
  case "$opt" in
    o) outdir="$OPTARG" ;;
    n) name="$OPTARG" ;;
    *) exit 2 ;;
  esac
done
shift $((OPTIND - 1))

if [ $# -eq 0 ]; then
  echo "usage: $0 [-o outdir] [-n name] tool-result.txt [...] (or '-' for stdin)" >&2
  exit 2
fi
if [ -n "$name" ] && [ $# -gt 1 ]; then
  echo "error: -n only valid with a single input" >&2
  exit 2
fi

command -v jq >/dev/null || { echo "error: jq required" >&2; exit 1; }
mkdir -p "$outdir"

decode_one() {
  local src="$1" json title mime out
  if [ "$src" = "-" ]; then json=$(cat); else json=$(cat "$src"); fi
  title=$(jq -r '.title // empty' <<<"$json")
  mime=$(jq -r '.mimeType // "unknown"' <<<"$json")
  out="$outdir/${name:-$title}"
  if [ -z "${name:-}" ] && [ -z "$title" ]; then
    echo "error: no .title in $src and no -n given" >&2
    return 1
  fi
  # pipe chain: extract base64 -> decode -> strip BOM -> CRLF->LF -> disk
  jq -r '.content' <<<"$json" | base64 -d \
    | sed '1s/^\xEF\xBB\xBF//; s/\r$//' > "$out"
  local label="$src"
  [ "$src" = "-" ] && label="stdin"
  printf '%s  <-  %s (%s, %s bytes, %s headings)\n' \
    "$out" "$label" "$mime" "$(wc -c < "$out")" \
    "$(grep -c '^#' "$out" || true)"
}

for src in "$@"; do
  decode_one "$src"
done
