# Reference Video Analysis

Use this reference when the user wants to study a successful video or adapt a style.

## Principle

Analyze rhythm, structure, shot language, and packaging. Do not copy scripts, claims, or distinctive creative expression.

## With `hahadu4520/videoanalyzer`

The repository is useful for:

- transcribing dialogue with Whisper
- cutting video into shots
- extracting key frames
- creating a Claude-assisted shot analysis
- exporting structured data for later reuse

Typical usage:

```bash
git clone https://github.com/hahadu4520/videoanalyzer
cd videoanalyzer
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
python main.py start input.mp4 --dialogue-only --language zh --gap-threshold 2.0
python main.py analyze <project-id>
python main.py generate <project-id>
```

## Convert Analysis Into Reusable Patterns

Extract:

- first 3-second hook type
- average shot/segment duration
- subtitle density
- visual devices
- proof structure
- CTA style

Then write a new original `segments.json` for the user's own topic.

