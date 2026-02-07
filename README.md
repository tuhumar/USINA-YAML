USINA-YAML 🎬
The Universal Open Source Standard for Audiovisual Engineering

USINA-YAML is a declarative specification for the entire video lifecycle: from initial processing and editing to creation and transport. By transforming creative decisions into structured data, Usina eliminates dependency on proprietary formats and allows videos to be "programmed," versioned, and automated.
🚀 The Vision

The audiovisual industry is currently held hostage by opaque binary files and closed ecosystems. USINA-YAML was born to be the "Markdown of Video"—a plain-text format, human-readable and machine-processable, capable of describing complex assemblies in a software-agnostic way.
Why USINA-YAML?

    True Interoperability: Transport edits between different softwares without data loss (the modern alternative to EDL/XML).

    Native Versioning: Use Git to track every cut, transition, or color grade.

    Scalable Automation: Generate hundreds of video variations (languages, aspect ratios, subtitles) by simply changing variables in the YAML file.

    Agnostic Rendering: Designed to be interpreted by FFMPEG, ML frameworks, or cloud rendering engines.

🛠 How it Works (Syntax Example)

A Usina project defines the logical structure of a video. Below is an example of a "Quick Cut" for Social Media:
YAML

usina_version: "1.0"
metadata:
  title: "Product Launch Teaser"
  format: "1080x1920" # Vertical 9:16
  fps: 30

assets:
  - id: main_clip
    src: "s3://assets/raw_footage_01.mp4"
  - id: background_track
    src: "./audio/lofi_beat.wav"

timeline:
  - layer: 0 (video)
    segments:
      - asset_id: main_clip
        start_at: 00:00:00
        duration: 00:00:15
        crop: "center"
        effects:
          - grayscale: 80%

  - layer: 1 (audio)
    segments:
      - asset_id: background_track
        fade_in: 2s
        volume: -6db

📂 Ecosystem Structure

    /spec: Detailed documentation of every tag and functionality.

    /schema: Official JSON Schema for validation and IDE auto-completion.

    /examples: Templates for YouTube, Cinema, and Dynamic Advertising.

🤝 Contributing

Usina is a community-driven standard. You can help by:

    Suggesting new tags for effects and transitions in the /spec folder.

    Building Parsers for languages like Python, Go, or Rust.

    Developing Plugins for NLEs (Premiere, Resolve) to export/import USINA-YAML.

See CONTRIBUTING.md for more details.
📜 License

This project is licensed under the Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0).

    Free for Personal Use: Use it for your own projects and learning.

    Non-Commercial: For commercial licensing or enterprise partnerships, please contact the author.

Next Step:

Would you like me to generate a LICENSE file with the full legal text for the "Non-Commercial" terms to ensure your rights are protected in the repository?

**Scope:** Short-form video production scripts (also works for long-form), with explicit **assets**, **sources**, **prompts**, and a deterministic **timeline**.

USINA-YAML is designed as a **single source of truth** for a video episode: creative intent + technical constraints + citations + rights metadata + a time-accurate scene timeline that can drive editors, renderers, and AI-assisted pipelines.

---

## Why this exists

Most “video scripts” are either:
- human-friendly but machine-hostile (Google Docs), or
- machine-friendly but human-hostile (NLE project files).

USINA-YAML sits in the middle: **human readable**, **version controllable**, and **lintable**.

> **Title source:** The canonical video title is read from YAML (`project.title` when present, otherwise `meta.title`). Do not infer titles from filenames or external metadata.


1) **Schema validation** (structure/types) using `schema/usina.script.v1.0.schema.json`  
2) **Lint rules** (math + references), e.g.:
- timeline ordered
- no overlap
- first scene starts at 0
- last scene ends exactly at `meta.duration_s`
- every `asset_id` exists
- shot durations sum (≈) scene duration (within tolerance)

> JSON Schema alone can’t reliably enforce “no overlap” and “timeline ends exactly at duration” — that’s why lint exists.

---

## Complete example (includes background audio)

Save this as `examples/air_gen_60s.yml`.

- Includes **background music** (audio bed)
- Includes **SFX** assets (whooshes/clicks)
- Demonstrates a scene-level `audio_tracks` array (portable, tool-agnostic)
- Keeps everything traceable, licensed, and creditable


---

## Licensing: “free for research/personal use, NOT for corporate/commercial/profit”


---

## Citation philosophy

USINA-YAML strongly encourages:
- conservative claims,
- explicit `sources[]`,
- `citations` attached to script blocks containing factual statements.

This makes automated fact-checking and audit trails possible.

---

## Contact / Commercial licensing

If you want commercial rights, enterprise usage, or monetized productions based on the standard, contact the author listed in `meta.authors` (or provide a public email in `meta.contact`).

---
