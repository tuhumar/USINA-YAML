# USINA-YAML v1.0 — Specification (YAML 1.2)

**Canonical schema ID:** `usina.script/v1.0`  
**File format:** YAML 1.2  
**Purpose:** Tool-agnostic, machine-validatable scripts for short-form video production (and compatible long-form), with explicit assets, sources, prompts, and a deterministic timeline.

---

## 0. Status of This Document

This document defines **USINA-YAML v1.0** (the “Standard”). A document is **conformant** if it satisfies all requirements marked **MUST** in this specification.

USINA-YAML is designed to be:
- Human-friendly (YAML),
- Strict enough to validate (schema + lint rules),
- Portable across tools (editors, renderers, AI writers, NLE automation, pipelines).

---

## 1. Terminology

The key words **MUST**, **MUST NOT**, **SHOULD**, **SHOULD NOT**, and **MAY** indicate requirement levels.

- **Document**: One USINA-YAML file.
- **ID**: A unique identifier used to reference entities (assets, prompts, scenes, VO blocks, etc.).
- **Asset**: A declared media resource (video, image, audio, font, subtitles, etc.).
- **Source**: A factual reference (papers, books, web pages, datasets).
- **Prompt**: A recorded instruction used to generate or transform content (writing, images, search, etc.).
- **Timeline**: Ordered scenes covering the full program duration without overlap.
- **Scene**: A time-ranged segment of the episode.
- **Shot**: A media unit within a scene (video clip, image card, text card, generated media, etc.).

---

## 2. Design Goals

USINA-YAML optimizes for:

1. **Single source of truth**: One file for creative intent + compliance metadata + timing.
2. **Deterministic assembly**: Timeline timing is unambiguous.
3. **Traceability**: Claims can cite sources; every asset includes license + credit.
4. **Prompt auditability**: AI prompts are recorded as first-class objects.
5. **Tool-agnostic interchange**: Multiple pipelines can consume the same file.
6. **Rights hygiene**: Background music and SFX are explicit assets (no “mystery audio”).

---

## 3. Non-Goals

- Not a full NLE project format (no keyframes/curves/nested timelines by default).
- Not DRM or rights enforcement; only metadata and rules.
- Not a closed “renderer spec.” Implementations interpret style.

---

## 4. File Conventions

### 4.1 Encoding
Documents **MUST** be UTF-8.

### 4.2 YAML Version
Documents **MUST** be valid YAML 1.2.

### 4.3 Comments & Anchors
- YAML comments are allowed.
- YAML anchors/aliases **MAY** be used, but implementations **SHOULD NOT** require them.

### 4.4 Root Type
The document root **MUST** be a mapping (YAML dictionary).

---

## 5. Top-Level Structure

A USINA-YAML document **MUST** contain these top-level keys:

- `usina_schema` (string; MUST equal `usina.script/v1.0`)
- `meta` (object)
- `format` (object)
- `style` (object)
- `audio` (object)
- `variables` (object)
- `prompts` (array)
- `sources` (array)
- `assets` (array)
- `script` (object)
- `timeline` (array)
- `export` (object)
- `qa` (object)

Implementations **MAY** accept additional keys (extensions), but they **MUST NOT** change the meaning of required keys.

---

## 6. Global ID Rules

USINA-YAML uses IDs to reference entities. IDs **MUST**:
- be unique within their namespace (assets IDs unique among assets, prompts among prompts, etc.),
- use `snake_case`,
- match regex: `^[a-z][a-z0-9_]{1,63}$`.

IDs **MUST NOT** be reused for different entities in the same document.

---

## 7. Section Specifications

### 7.1 `usina_schema` (string)
**Required.** Must be exactly:
```yaml
usina_schema: "usina.script/v1.0"
```

### 7.2 `meta` (object)
Identity + core timing.

**Required fields:**
- `title` (string)
- `episode_id` (string; SHOULD be stable and URL-safe)
- `language` (BCP-47 string, e.g., `en`, `pt-BR`)
- `duration_s` (number; MUST be > 0)
- `created_at` (ISO-8601 string)
- `updated_at` (ISO-8601 string)
- `authors` (array of strings)
- `license` (string; document/spec license)
- `version` (string; recommended SemVer)

**Optional fields (recommended):**
- `description` (string)
- `tags` (array of strings)
- `series` (string)
- `channel` (string)
- `contact` (string)
- `notes` (string)

**Normative constraints:**
- `duration_s` **MUST** match the end time of the last timeline scene (see Lint Rules).

### 7.3 `format` (object)
Output constraints.

Recommended fields:
- `aspect_ratio` (string; e.g., `9:16`)
- `resolution` (string; e.g., `1080x1920`)
- `fps` (number; e.g., 30, 60)
- `color_space` (string; e.g., `bt709`)
- `captions` (object; optional: `burn_in`, `sidecar`, `format`)

### 7.4 `style` (object)
Creative direction. Descriptive, not prescriptive.

Recommended fields:
- `tone` (string)
- `pacing` (string)
- `visual_language` (string)
- `on_screen_text_rules` (string)
- `brand` (object; optional)
- `do_not` (array of strings; prohibited claims/styles)

### 7.5 `audio` (object)
Audio policy + defaults.

Recommended fields:
- `voice` (object):
  - `voice_id` (string; renderer-specific)
  - `delivery` (string)
  - `pronunciation_guide` (array; optional)
- `mix_targets` (object):
  - `lufs_integrated` (number; e.g., -14)
  - `true_peak_db` (number; e.g., -1.0)
- `music_policy` (object):
  - `allowed_license_types` (array of strings)
  - `avoid` (array of strings)
- `bed` (object; optional global “default background bed”):
  - `asset_id` (string; MUST reference an audio asset)
  - `gain_db` (number; optional)
  - `notes` (string; optional)

**Normative constraints:**
- If `audio.bed.asset_id` is present, it **MUST** exist in `assets` and that asset **MUST** have `type: "audio"`.

### 7.6 `variables` (object)
Key/value store for templating and reuse.

- Keys **MUST** be `snake_case`.
- Values **MAY** be string/number/boolean/array/object.

Implementations **SHOULD** support variable substitution in prompts and script text using `{{var_name}}`.

### 7.7 `prompts` (array)
Recorded prompts used to generate parts of the episode.

Each prompt **MUST** have:
- `id` (string)
- `purpose` (string)
- `kind` (string; e.g., `writer`, `image`, `broll_search`, `fact_check`)
- `input` (string or object; the prompt body)
- `outputs_expected` (array of strings)
- `constraints` (array of strings)

Prompts **MAY** reference `sources` by ID, `variables`, and `assets`.

### 7.8 `sources` (array)
Citations supporting factual claims.

Each source **MUST** have:
- `id` (string)
- `title` (string)
- `type` (string; e.g., `web`, `paper`, `book`, `dataset`, `interview`)

Recommended fields:
- `publisher` (string)
- `date` (ISO-8601)
- `url` (string)
- `accessed_at` (ISO-8601)
- `credibility` (string; e.g., `primary`, `secondary`)
- `notes` (string)

### 7.9 `assets` (array)
Declared media resources. Assets are declared once, referenced many times.

Each asset **MUST** have:
- `id` (string)
- `type` (string; e.g., `video`, `image`, `audio`, `font`, `subtitle`, `project_file`)
- `uri` (string; URL or local path)
- `license` (string)
- `credit` (string)

Recommended fields:
- `checksum` (string; recommended for immutability)
- `duration_s` (number; recommended for audio/video)
- `dimensions` (string; visuals)
- `tags` (array)
- `notes` (string)

**Normative constraints:**
- Any reference to `asset_id` in the timeline **MUST** match an existing asset `id`.
- Audio track references **MUST** point to assets with `type: "audio"`.

### 7.10 `script` (object)
Narrative + production instructions (textual truth layer).

Recommended structure:
```yaml
script:
  logline: "..."
  hook:
    text: "..."
    citations: [source_a]
  vo:
    blocks:
      - id: vo_01
        text: "..."
        citations: [source_a]
  on_screen_text:
    blocks:
      - id: ost_01
        text: "..."
```

**Normative constraints:**
- VO blocks intended for timeline use **MUST** have `id`.
- `citations` entries **MUST** refer to valid `sources.id`.

### 7.11 `timeline` (array)
The authoritative timeline: scenes cover the full duration.

Each scene **MUST** contain:
- `id` (string)
- `start_s` (number; >= 0)
- `end_s` (number; > start_s)
- `shots` (array; >= 1)

Each scene **SHOULD** include:
- `vo` (object or null; recommended)
- `audio_tracks` (array; optional)

#### 7.11.1 Scene `vo`
A scene VO object SHOULD reference `script.vo.blocks`:

- `ref_id` (string; VO block ID) OR inline `text` (string)
- `mix_priority` (string; optional: `primary`, `secondary`)
- `notes` (string; optional)

If `ref_id` is used, it **MUST** match a VO block ID in `script.vo.blocks`.

#### 7.11.2 Scene `audio_tracks` (optional)
Portable, tool-agnostic audio placements.

Each track item **MUST** contain:
- `asset_id` (string; MUST exist and be an audio asset)
- `start_s` (number; absolute time in the episode timeline)
- `end_s` (number; > start_s)
- `gain_db` (number; optional)
- `role` (string; optional: `music`, `sfx`, `ambience`, `dialogue`)
- `notes` (string; optional)
- `fade_in_s` (number; optional)
- `fade_out_s` (number; optional)

**Normative constraints:**
- `start_s`/`end_s` **MUST** be within the scene bounds when `audio_tracks` is nested in a scene.
- Overlaps between audio tracks are allowed (mixing), but implementations MAY lint clipping risk.

#### 7.11.3 `shots`
Each shot **MUST** contain:
- `type` (string; e.g., `video`, `image`, `generated_image`, `motion_graphics`, `text_card`)
- `duration_s` (number; > 0)
- `asset_id` (string) OR `generator` (object)

Shot optional fields:
- `notes` (string)
- `overlays` (array)
- `transitions` (object)

**Normative constraints:**
- Sum of `shots[].duration_s` in a scene **SHOULD** equal `(end_s - start_s)` within tolerance.
- If `asset_id` is present, it **MUST** exist in `assets`.

### 7.12 `export` (object)
Output targets and deliverables.

Recommended fields:
- `deliverables` (array; e.g., `["video","captions","thumbnail","metadata_json"]`)
- `targets` (array of objects):
  - `platform` (string)
  - `container` (string; `mp4`, `mov`, etc.)
  - `video_codec` (string)
  - `audio_codec` (string)
  - `filename` (string; templates allowed)
- `thumbnail` (object; asset or generator)
- `metadata` (object; title/description/tags)

### 7.13 `qa` (object)
Quality gates/checklists.

Recommended fields:
- `lint`:
  - `strict` (boolean)
  - `tolerance_s` (number; e.g., 0.05)
- `legal`:
  - `rights_confirmed` (boolean)
  - `credits_complete` (boolean)
- `fact_check`:
  - `claims_reviewed` (boolean)
  - `sources_present` (boolean)
- `checks` (array of objects with `id`, `description`, `severity`)

---

## 8. Lint Rules (Normative)

A conformant linter **MUST** implement at least these rules:

### Timeline Integrity
1. `timeline` ordered by `start_s` ascending.
2. No overlap: `scene[i+1].start_s >= scene[i].end_s`.
3. First scene `start_s == 0`.
4. Last scene `end_s == meta.duration_s`.
5. Each scene: `end_s > start_s`.
6. Shot durations sum ≈ scene duration within tolerance (default 0.05s, configurable).

### ID & References
7. IDs match `^[a-z][a-z0-9_]{1,63}$` (snake_case).
8. `asset_id` references exist in `assets`.
9. `vo.ref_id` references exist in `script.vo.blocks`.
10. `generator.prompt_id` references exist in `prompts` (if used).
11. `citations[]` entries exist in `sources`.

### Audio (if present)
12. `audio.bed.asset_id` references an audio asset.
13. Each `audio_tracks[].asset_id` references an audio asset.
14. Scene-level `audio_tracks` times are within scene bounds and `end_s > start_s`.

### Assets & Rights Hygiene
15. Every asset has `license` and `credit`.

---

## 9. Extensibility

- Additional fields are allowed anywhere.
- Extensions **SHOULD** be namespaced with `x_` (e.g., `x_renderer`, `x_tooling`).
- Extensions **MUST NOT** alter required field meanings.

---

## 10. Versioning

- `usina_schema` identifies the major line: `usina.script/v1.0`.
- `meta.version` is the document version (SemVer recommended).
- Breaking changes require a new schema ID (e.g., `usina.script/v2.0`).

---

## 11. Reference Implementation Guidance (Non-Normative)

Preferred validation pipeline:
1) YAML parse → JSON-like object
2) Schema validation (structure/types)
3) Lint pass (timeline math + reference resolution + rights checks)

---
