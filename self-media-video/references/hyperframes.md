# HyperFrames Implementation

Use this reference when building the animation project.

## Project Setup

```bash
npx hyperframes init my-video --example blank --skip-skills
cd my-video
```

Use `package.json` scripts:

```json
{
  "scripts": {
    "dev": "npx --yes hyperframes@0.5.3 preview",
    "check": "npx --yes hyperframes@0.5.3 lint && npx --yes hyperframes@0.5.3 inspect",
    "render": "npx --yes hyperframes@0.5.3 render"
  }
}
```

## Composition Rules

- Use vertical canvas for social videos:

```html
<meta name="viewport" content="width=1080, height=1920" />
<div id="root" data-composition-id="main" data-start="0" data-duration="45" data-width="1080" data-height="1920">
```

- Every timed visible element needs:

```html
class="clip" data-start="0" data-duration="5" data-track-index="1"
```

- Do not overlap clips on the same `data-track-index`.
- Do not animate `visibility` or `display` on `.clip` elements.
- Register GSAP timeline:

```html
<script>
  window.__timelines = window.__timelines || {};
  const tl = gsap.timeline({ paused: true });
  window.__timelines["main"] = tl;
</script>
```

## Visual QA

After edits:

```bash
npm run check
npx hyperframes snapshot --at 2,7,13,21,27,35,42
```

Open the snapshots and check:

- no cropped title text
- subtitles do not cover essential visuals
- cards stay inside safe areas
- screenshots are legible enough for credibility, but not relied on for dense reading
- final CTA is readable on a phone

## Render

Draft:

```bash
npm run render -- -o renders/draft.mp4 --fps 30 --quality draft
```

Final:

```bash
npm run render -- -o renders/final.mp4 --fps 30 --quality high
```

