#!/usr/bin/env bash
set -euo pipefail

if [ "$#" -ne 1 ]; then
  echo "Usage: $0 path/to/video.mp4" >&2
  exit 2
fi

ffprobe -v error \
  -show_entries format=duration,size \
  -show_entries stream=codec_type,width,height,r_frame_rate \
  -of default=noprint_wrappers=1 \
  "$1"

