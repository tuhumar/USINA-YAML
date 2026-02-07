# USINA-YAML v1.0 — Tool-Agnostic Video Script Standard (YAML 1.2)

**Schema ID:** `usina.script/v1.0`  
**Status:** v1.0 (stable)  
**Scope:** Short-form video production scripts (also works for long-form), with explicit **assets**, **sources**, **prompts**, and a deterministic **timeline**.

USINA-YAML is designed as a **single source of truth** for a video episode: creative intent + technical constraints + citations + rights metadata + a time-accurate scene timeline that can drive editors, renderers, and AI-assisted pipelines.

---

## Why this exists

Most “video scripts” are either:
- human-friendly but machine-hostile (Google Docs), or
- machine-friendly but human-hostile (NLE project files).

USINA-YAML sits in the middle: **human readable**, **version controllable**, and **lintable**.

---

## Repository layout (recommended)

```
.
├─ README.md                         # this file
├─ SPEC.md                           # the full normative specification
├─ schema/
│  └─ usina.script.v1.0.schema.json  # baseline JSON Schema validator
├─ examples/
│  └─ air_gen_60s.yml                # complete conformant example
└─ LICENSE                           # your chosen license for the spec
```

> If you haven’t created these files yet, copy `SPEC.md` + the schema from the spec, and drop the example below into `examples/air_gen_60s.yml`.

---

## Quick start

### 1) Create a new episode file
Make a YAML file like `examples/my_episode.yml` and set:

- `usina_schema: "usina.script/v1.0"`
- `meta.duration_s`
- a full `timeline` from `start_s: 0` to `end_s: meta.duration_s`
- declare all `assets` **once** and reference them by `asset_id`

### 2) Validate + lint
USINA-YAML expects **two layers** of checks:

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

```yaml
usina_schema: "usina.script/v1.0"

meta:
  title: "Why Fog Makes Electricity (Air-Gen in 60s)"
  episode_id: "air_gen_60s_001"
  language: "en"
  duration_s: 60
  created_at: "2026-02-07T10:00:00-03:00"
  updated_at: "2026-02-07T10:00:00-03:00"
  authors: ["Diego Meirinho C. P. Gonçalves"]
  license: "CC-BY-NC-4.0"
  version: "1.0.0"
  description: "A fast, cautious explainer of humidity-driven electrical effects in porous materials."
  tags: ["science", "materials", "humidity", "air-gen"]

format:
  aspect_ratio: "9:16"
  resolution: "1080x1920"
  fps: 30
  captions:
    burn_in: false
    sidecar: true
    format: "srt"

style:
  tone: "curious, grounded, no hype"
  pacing: "fast but breathable"
  visual_language: "clean typography, macro textures"
  on_screen_text_rules: "Short phrases. No tiny text. One idea per card."
  do_not:
    - "medical claims"
    - "investment advice"
    - "guarantees or exaggerated certainty"

audio:
  voice:
    voice_id: "narrator_en_01"
    delivery: "calm, crisp, slightly playful"
  mix_targets:
    lufs_integrated: -14
    true_peak_db: -1.0
  music_policy:
    allowed_license_types: ["royalty_free", "original", "cc_by", "cc_by_sa"]
    avoid: ["uncleared copyrighted songs", "chart music"]
  # Optional: global default audio bed (tooling may use this as fallback)
  bed:
    asset_id: bg_music_01
    gain_db: -18
    notes: "Low-level bed across whole video unless overridden."

variables:
  hook_line: "Fog can power a sensor. Here’s the weird physics."
  cta_line: "Follow for more tiny physics with big vibes."

prompts:
  - id: writer_vo_v1
    purpose: "Generate VO blocks with conservative claims + citations."
    kind: "writer"
    input: |
      Write a 60s VO with the hook in the first 3 seconds.
      Keep claims cautious, cite sources by ID, avoid hype.
    outputs_expected: ["script.vo.blocks"]
    constraints:
      - "No exaggerated certainty."
      - "Attach citations to factual claims."
      - "No health or finance advice."

sources:
  - id: source_airgen_overview
    title: "Air-gen / humidity-driven electricity overview"
    type: "web"
    publisher: "Institution / Lab / Journal (replace with the real source)"
    date: "2020-01-01"
    url: "https://example.com/airgen"
    accessed_at: "2026-02-07T10:00:00-03:00"
    credibility: "secondary"

assets:
  # Visuals
  - id: macro_fog_texture_vid
    type: "video"
    uri: "assets/macro_fog_texture.mp4"
    license: "original"
    credit: "Recorded by Diego"
    duration_s: 12
    checksum: "sha256:REPLACE_ME"
    tags: ["macro", "fog", "texture"]

  - id: typographic_bg_img
    type: "image"
    uri: "assets/typographic_bg.png"
    license: "original"
    credit: "Designed by Diego"
    checksum: "sha256:REPLACE_ME"
    tags: ["background", "typography"]

  # Audio (NEW)
  - id: bg_music_01
    type: "audio"
    uri: "assets/audio/bg_music_01.wav"
    license: "royalty_free"
    credit: "Replace with your library attribution"
    duration_s: 62
    checksum: "sha256:REPLACE_ME"
    tags: ["music", "bed"]

  - id: sfx_whoosh_01
    type: "audio"
    uri: "assets/audio/sfx_whoosh_01.wav"
    license: "royalty_free"
    credit: "Replace with your library attribution"
    duration_s: 1.2
    checksum: "sha256:REPLACE_ME"
    tags: ["sfx", "whoosh"]

  - id: sfx_click_01
    type: "audio"
    uri: "assets/audio/sfx_click_01.wav"
    license: "royalty_free"
    credit: "Replace with your library attribution"
    duration_s: 0.4
    checksum: "sha256:REPLACE_ME"
    tags: ["sfx", "click"]

script:
  logline: "Humidity + porous materials can create measurable electrical effects."
  vo:
    blocks:
      - id: vo_01
        text: "Fog can power a sensor. Not magic — physics."
        citations: []
      - id: vo_02
        text: "Some porous materials interact with water molecules in air and can generate small voltages under the right conditions."
        citations: [source_airgen_overview]
      - id: vo_03
        text: "It’s not a free-energy machine — it’s a tiny effect that can be useful for low-power devices."
        citations: []
      - id: vo_04
        text: "{{cta_line}}"
        citations: []

  on_screen_text:
    blocks:
      - id: ost_01
        text: "Humidity → surface charge → tiny voltage"
      - id: ost_02
        text: "Small effect. Real applications."
      - id: ost_03
        text: "Not ‘free energy’."

timeline:
  - id: scene_01_hook
    start_s: 0
    end_s: 10
    vo: { ref_id: vo_01 }
    audio_tracks:
      - asset_id: bg_music_01
        start_s: 0
        end_s: 10
        gain_db: -18
      - asset_id: sfx_whoosh_01
        start_s: 0.8
        end_s: 2.0
        gain_db: -8
        notes: "Punch the hook"
    shots:
      - type: video
        duration_s: 10
        asset_id: macro_fog_texture_vid
        overlays:
          - kind: on_screen_text
            ref_id: ost_01
            at_s: 1.0

  - id: scene_02_explain
    start_s: 10
    end_s: 45
    vo: { ref_id: vo_02 }
    audio_tracks:
      - asset_id: bg_music_01
        start_s: 10
        end_s: 45
        gain_db: -18
      - asset_id: sfx_click_01
        start_s: 12.2
        end_s: 12.6
        gain_db: -10
        notes: "Accent the first key fact"
    shots:
      - type: image
        duration_s: 35
        asset_id: typographic_bg_img
        overlays:
          - kind: on_screen_text
            ref_id: ost_02
            at_s: 12.0
          - kind: on_screen_text
            ref_id: ost_03
            at_s: 28.0

  - id: scene_03_close
    start_s: 45
    end_s: 60
    vo: { ref_id: vo_04 }
    audio_tracks:
      - asset_id: bg_music_01
        start_s: 45
        end_s: 60
        gain_db: -16
        notes: "Slight lift into the CTA"
    shots:
      - type: video
        duration_s: 15
        asset_id: macro_fog_texture_vid
        notes: "CTA and end card"

export:
  deliverables: ["video", "captions", "thumbnail", "metadata_json"]
  targets:
    - platform: "youtube_shorts"
      container: "mp4"
      video_codec: "h264"
      audio_codec: "aac"
      filename: "{{episode_id}}_ytshorts.mp4"
  metadata:
    title: "Fog Electricity in 60 Seconds"
    description: "A cautious look at humidity-driven electrical effects in porous materials."
    tags: ["science", "humidity", "materials"]

qa:
  lint:
    strict: true
    tolerance_s: 0.05
  legal:
    rights_confirmed: true
    credits_complete: true
  fact_check:
    claims_reviewed: false
    sources_present: true
  checks:
    - id: check_timeline_exact
      description: "Timeline ends exactly at meta.duration_s"
      severity: "error"
    - id: check_assets_licensed
      description: "All assets have license + credit"
      severity: "error"
```

> `audio_tracks` is intentionally tool-agnostic: a renderer can map it to tracks, stems, or automation. If your pipeline prefers global audio, you can also rely on `audio.bed` as a default.

---

## What publishing on GitHub does (and does not) give you

- **You already have copyright** automatically the moment you create/fix the text/spec (no registration required in most countries). citeturn0search0turn0search4  
- Publishing on GitHub is **strong evidence of date + authorship** (public timestamp), but it does **not** create “extra copyright rights.”  
- Publishing may act as **public disclosure** for patents. In the U.S., inventor-originated disclosures can have a **one-year grace period** under 35 U.S.C. §102(b)(1) (details matter). citeturn1search0turn1search3turn1search15  
  Many jurisdictions outside the U.S. are less forgiving—so talk to a patent attorney if patents are a priority.

---

## Licensing: “free for research/personal use, NOT for corporate/commercial/profit”

What you described is essentially a **NonCommercial** license.

A common, standardized option for specs/docs is:
- **CC BY-NC 4.0** (Attribution + NonCommercial) citeturn0search1turn0search9turn0search5

**Important nuance:** CC BY-NC restricts *commercial purpose*, not “being a company.” A company doing genuinely noncommercial research may still fit “NonCommercial.” citeturn0search16turn0search5  
If you want to block **any** corporate/enterprise use regardless of purpose, you’ll need a **custom license** (more restrictive, but less standard/compatible).

### Recommended practical approach (most common)
- Publish the spec under **CC BY-NC 4.0**  
- Add a note: “Commercial use requires a separate license from the author.”

CC licenses are generally **not recommended for software code**, but they are **fine for documentation/spec text** (which is what this is). citeturn0search7turn0search3

---

## Contributing

PRs and issues are welcome. Please include:
- rationale + examples
- lint impact (does it break existing files?)
- backwards compatibility notes

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

## License (repository)

Choose one and place it in `LICENSE`.

Suggested:
- **CC BY-NC 4.0** (for the spec and schema)

You can also dual-license:
- **CC BY-NC 4.0** for public use
- separate commercial license on request

(If you want, I can generate a clean `LICENSE` file and a stricter custom “no corporate use” license text.)
