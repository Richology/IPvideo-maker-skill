# Self-Media Video Skill

A Codex skill for turning articles, scripts, screenshots, and reference videos into social short-video workflows.

It helps creators build a repeatable pipeline:

```text
source material -> short-video script -> segments.json -> HyperFrames animation -> MP4 render -> talking-head/voiceover composition -> publish review
```

## What It Does

- Converts copied long-form articles into short-video scripts.
- Produces editable `segments.json` storyboards.
- Guides HyperFrames + GSAP animation projects.
- Provides ffmpeg helpers for talking-head picture-in-picture.
- Supports post-publish review using retention and engagement metrics.
- Uses reference videos for rhythm and structure analysis without copying content.

## Install

Copy or symlink the skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R self-media-video ~/.codex/skills/
```

Then ask Codex:

```text
Use $self-media-video to turn this article into a 45-second short video.
```

## Optional Tools

The workflow is most useful with:

- Node.js
- HyperFrames
- ffmpeg
- Python 3
- A talking-head recording or voiceover file

For reference-video analysis, you can also use:

- https://github.com/hahadu4520/videoanalyzer

## Included Helpers

```bash
self-media-video/scripts/make_segments.py --duration 45 --count 7 --out segments.json
self-media-video/scripts/probe_video.sh renders/final.mp4
self-media-video/scripts/compose_pip.sh base.mp4 talking_head.mp4 final_with_pip.mp4
```

## License

MIT

