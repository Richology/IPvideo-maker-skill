#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -lt 3 ]; then
  cat >&2 <<'EOF'
Usage: compose_pip.sh base.mp4 talking_head.mp4 output.mp4 [pip_size]

Creates a right-bottom square talking-head PIP and uses the talking-head audio.
Default pip_size: 260
EOF
  exit 2
fi

BASE_VIDEO="$1"
TALKING_HEAD="$2"
OUTPUT="$3"
PIP_SIZE="${4:-260}"

ffmpeg -y \
  -i "$BASE_VIDEO" \
  -i "$TALKING_HEAD" \
  -filter_complex "[1:v]scale=${PIP_SIZE}:${PIP_SIZE}:force_original_aspect_ratio=increase,crop=${PIP_SIZE}:${PIP_SIZE},format=rgba[pip];[0:v][pip]overlay=W-w-56:H-h-240[v]" \
  -map "[v]" \
  -map 1:a \
  -c:v libx264 \
  -crf 20 \
  -preset medium \
  -c:a aac \
  -b:a 192k \
  -shortest \
  "$OUTPUT"

