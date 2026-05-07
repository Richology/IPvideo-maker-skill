#!/usr/bin/env python3
"""Create an editable segments.json template for a short self-media video."""

from __future__ import annotations

import argparse
import json
from pathlib import Path


def build_segments(duration: float, count: int) -> list[dict]:
    labels = ["hook", "reframe", "definition", "step", "step", "example", "close"]
    if count > len(labels):
        labels = labels[:-1] + ["step"] * (count - len(labels)) + [labels[-1]]

    starts = [round(i * duration / count, 2) for i in range(count)]
    ends = [round((i + 1) * duration / count, 2) for i in range(count)]
    segments = []
    for i in range(count):
        segments.append(
            {
                "start": starts[i],
                "end": ends[i],
                "type": labels[i] if i < len(labels) else "step",
                "subtitle": f"Segment {i + 1} subtitle",
                "voiceover": f"Segment {i + 1} spoken line",
                "visual": "Describe the on-screen visual",
                "motion": "Describe the animation or camera movement",
            }
        )
    return segments


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--duration", type=float, default=45, help="Video duration in seconds")
    parser.add_argument("--count", type=int, default=7, help="Number of segments")
    parser.add_argument("--out", default="segments.json", help="Output JSON path")
    args = parser.parse_args()

    if args.duration <= 0:
        raise SystemExit("--duration must be positive")
    if args.count < 1:
        raise SystemExit("--count must be at least 1")

    out = Path(args.out)
    out.write_text(json.dumps(build_segments(args.duration, args.count), ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"Wrote {out}")


if __name__ == "__main__":
    main()

