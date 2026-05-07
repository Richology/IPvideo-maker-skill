# IP Video Maker Skill

[中文 README](README.zh-CN.md)

A Codex skill for creators who want to turn articles, scripts, screenshots, and reference videos into repeatable short-video production workflows.

It is designed for self-media creators, newsletter writers, indie hackers, educators, and IP builders who want a practical pipeline instead of a one-off prompt.

## What This Skill Helps You Do

- Turn a copied long-form article into a 30-90 second short-video script.
- Convert the script into an editable `segments.json` storyboard.
- Build a vertical HyperFrames + HTML + GSAP animation project.
- Render the animation into MP4.
- Add a talking-head or voiceover picture-in-picture with ffmpeg.
- Review post-publish data and generate the next iteration.
- Analyze reference videos for structure and rhythm without copying their content.

## Workflow

```mermaid
flowchart LR
  A["Article / Script / Screenshot / Reference Video"] --> B["Short-Video Script"]
  B --> C["segments.json Storyboard"]
  C --> D["HyperFrames HTML Animation"]
  D --> E["MP4 Render"]
  E --> F["Talking-Head / Voiceover PIP"]
  F --> G["Publish"]
  G --> H["Data Review"]
  H --> B
```

## Install

Copy the skill folder into your Codex skills directory:

```bash
mkdir -p ~/.codex/skills
cp -R self-media-video ~/.codex/skills/
```

Then restart Codex or start a new session so the skill is discovered.

## Quick Start

Ask Codex:

```text
Use $self-media-video to turn this article into a 45-second short video.
```

For best results, paste the full article text instead of only providing screenshots:

```text
Use $self-media-video.

Here is my article:
...

Please create:
1. script.md
2. segments.json
3. a HyperFrames animation project
4. a draft MP4
```

## Using Different AI Agents

This repo is not limited to Codex. Codex gets the most native experience because the skill format is built for it, but Claude Code, Cursor, and other agentic coding tools can use the same workflow, scripts, and references.

### Codex

Use the skill directly:

```text
Use $self-media-video to turn this article into a 45-second short video.
```

Codex will read `self-media-video/SKILL.md` plus the bundled references and scripts.

### Claude Code

Open the repository in Claude Code and point it at the same workflow files:

```text
Read README.md, README.zh-CN.md, self-media-video/SKILL.md, and the references folder. Turn this article into a short-video workflow with script.md, segments.json, HyperFrames animation, and ffmpeg composition.
```

Claude Code can follow the same folder structure and run the helper scripts. If you want, you can also add a `CLAUDE.md` file later for a more opinionated repo-specific prompt.

### Cursor

Open the repo in Cursor and ask it to work from the same source files:

```text
Use the repository workflow in README.md and self-media-video/SKILL.md to turn this article into a 45-second short video. Generate script.md, segments.json, and a draft MP4.
```

Cursor works best when you ask it to edit the real project files directly instead of giving it a vague one-shot prompt.

### Other AI Agents

Any agent that can read local files, edit code, and run shell commands can use this workflow. Tell it to:

- read the README and skill files first
- create or update `script.md`
- create or update `segments.json`
- build or edit the HyperFrames project
- render a draft MP4
- optionally compose talking-head PIP with ffmpeg

The exact UI may differ, but the workflow does not depend on Codex alone.

## Example Prompts

```text
Use $self-media-video to turn this WeChat article into a 60-second Xiaohongshu video.
```

```text
Use $self-media-video to convert this newsletter into a 45-second talking-head video with animated key points.
```

```text
Use $self-media-video to analyze this reference video for pacing and visual structure, then create an original segments.json for my topic.
```

```text
Use $self-media-video to review my published video data and suggest the next hook/title test.
```

## Recommended Toolchain

The skill can guide the workflow conceptually, but it becomes much more useful with:

- [HyperFrames](https://hyperframes.heygen.com) for HTML-to-video rendering
- [GSAP](https://gsap.com) for timeline animation
- [ffmpeg](https://ffmpeg.org) for audio, voiceover, and PIP composition
- Python 3 for helper scripts
- Node.js for HyperFrames

For reference-video breakdowns:

- [hahadu4520/videoanalyzer](https://github.com/hahadu4520/videoanalyzer)

## Included Helpers

Create an editable storyboard template:

```bash
self-media-video/scripts/make_segments.py --duration 45 --count 7 --out segments.json
```

Check a rendered video:

```bash
self-media-video/scripts/probe_video.sh renders/final.mp4
```

Add a talking-head PIP and use the talking-head audio:

```bash
self-media-video/scripts/compose_pip.sh base.mp4 talking_head.mp4 final_with_pip.mp4
```

## Typical Output Files

A good project generated with this skill usually contains:

```text
my-video/
  script.md
  segments.json
  index.html
  assets/
    source-screenshot.png
    talking_head.mp4
  renders/
    draft.mp4
    final_with_pip.mp4
```

## Post-Publish Review Template

After publishing, give Codex data like this:

```text
platform:
publish time:
title:
cover text:
duration:
views:
3-second retention:
completion rate:
average watch time:
likes:
saves:
comments:
shares:
follower conversions:
audience comments:
```

Codex will diagnose the main bottleneck and suggest the next test: hook, title, cover, pacing, visual density, or CTA.

## Repository Structure

```text
self-media-video/
  SKILL.md
  agents/
    openai.yaml
  references/
    article-to-video.md
    hyperframes.md
    publish-review.md
    reference-video-analysis.md
  scripts/
    make_segments.py
    probe_video.sh
    compose_pip.sh
```

## Important Notes

- Pasted source text is more accurate than OCR from screenshots.
- Reference videos should be used to learn rhythm and structure, not to copy content.
- The first render is a draft. Always inspect snapshots before final export.
- Talking-head video or voiceover usually makes the output much more publishable.

## License

MIT
