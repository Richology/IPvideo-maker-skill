---
name: self-media-video
description: End-to-end self-media short-video production workflow for Codex. Use when turning articles, copied long-form text, screenshots, PDFs, scripts, or reference videos into social short videos with structured scripts, segments.json storyboards, HyperFrames/HTML/GSAP animations, ffmpeg picture-in-picture talking-head or voiceover composition, and post-publish data review for platforms such as Xiaohongshu, Douyin, TikTok, YouTube Shorts, WeChat Channels, or Bilibili.
---

# Self-Media Video

Use this skill to run a repeatable creator workflow:

`source material -> short-video script -> segments.json -> animation project -> render -> PIP/voiceover -> publish review`

Default to making the smallest useful artifact first: a script and `segments.json`, then a renderable animation, then optional talking-head/voiceover composition.

## Workflow

1. **Ingest the source**
   - Prefer copied article text over screenshots for accuracy.
   - For screenshots, extract only visible structure and ask for source text when precision matters.
   - For reference videos, use `videoanalyzer` only for rhythm and shot-language analysis, not for copying content.

2. **Create the short-video script**
   - Preserve the source's core claim, argument order, examples, and strongest phrases.
   - Convert long-form prose into a spoken script, usually 30-90 seconds.
   - Make the first 3 seconds concrete: pain point, contradiction, result, or surprising claim.

3. **Create `segments.json`**
   - Split into 5-9 timed segments.
   - Include `start`, `end`, `type`, `subtitle`, `visual`, and `motion`.
   - Keep subtitles shorter than the spoken script; subtitles are scanning anchors, not transcripts.
   - Run `scripts/make_segments.py` when a quick editable template is enough.

4. **Build the animation**
   - Prefer HyperFrames when available: initialize with `npx hyperframes init <project> --example blank --skip-skills`.
   - Use HTML/CSS/GSAP with a vertical canvas: `1080 x 1920`, `30fps`.
   - Register paused GSAP timelines on `window.__timelines[compositionId]`.
   - Add `class="clip"` plus `data-start`, `data-duration`, and `data-track-index` to every timed visible element.
   - Run `npm run check` or `npx hyperframes lint && npx hyperframes inspect`.
   - Capture snapshots at segment boundaries and visually inspect mobile readability.

5. **Render**
   - Render draft first: `npx hyperframes render -o renders/draft.mp4 --fps 30 --quality draft`.
   - Verify with `scripts/probe_video.sh renders/draft.mp4`.
   - Use high quality only after the draft is approved.

6. **Add voice and avatar**
   - If the creator has a talking-head video, compose it as right-bottom PIP with `scripts/compose_pip.sh`.
   - If the creator has only audio and an avatar, use ffmpeg overlay manually or adapt `compose_pip.sh`.
   - When voice timing differs from animation timing, adjust segment durations before final render instead of forcing a bad `-shortest` cut.

7. **Review after publishing**
   - Ask the user to provide title, cover text, duration, platform, publish time, views, 3-second retention, completion rate, average watch time, likes, saves, comments, shares, and follower conversions.
   - Diagnose one primary bottleneck: hook, pacing, clarity, promise mismatch, visual density, CTA, or distribution.
   - Produce the next test: revised hook, title, cover text, first 5 seconds, or segment timing.

## Source-Specific Guidance

- **Copied article text:** Use `references/article-to-video.md`.
- **Reference/breakdown video:** Use `references/reference-video-analysis.md`.
- **HyperFrames implementation:** Use `references/hyperframes.md`.
- **Publishing review:** Use `references/publish-review.md`.

## Quality Bar

- Do not treat the first render as final.
- Verify all text fits inside mobile-safe areas.
- Avoid transcript walls; use one idea per screen.
- Make article screenshots a credibility/background element, not the main readable content.
- State when OCR/screenshot interpretation is approximate.
- Keep reusable outputs in the project: `script.md`, `segments.json`, source assets, render commands, and final MP4 paths.

