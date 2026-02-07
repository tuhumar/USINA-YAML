# USINA-YAML -> Wizard/Render Mapping Map

This document describes, operationally, how `shorts-wizard-app` interprets YAML and applies each field in the pipeline:

1. safe parsing
2. normalization into `spec_data`
3. chapter/scene construction
4. media collection and materialization
5. rendering (video, audio, captions)

The goal is to serve as a specification for any external YAML generator.

## 1) Parsing and security

| Source | Rule | Internal destination |
|---|---|---|
| raw YAML | `yaml.safe_load` | `script_structure` |
| YAML with `<<:`, `!tag`, `&anchor`, `*alias` | blocked | returns empty / security error |
| valid YAML | normalizes asset metadata | `_normalize_assets_metadata` |

## 2) Top-level accepted by the Wizard

| Namespace | Status | Notes |
|---|---|---|
| `usina_schema` | accepted | required only in lint strict mode |
| `project` | accepted | primary in legacy mode |
| `meta` | accepted | used together with `project` |
| `format` | accepted | fallback for `project.format` |
| `style` | accepted | fallback for `project.style` |
| `audio` | accepted | fallback for `project.audio` |
| `assets` | accepted | supports lists and groups |
| `timeline` | accepted | primary for scenes |
| `roteiro`/`scenes`/`cenas` | accepted | compatibility |
| `prompts` | accepted | canonical prompts map |
| `prompts_on_screen` | accepted | compatibility (merged with `prompts`) |
| `voiceover_full` | accepted | long narration text |
| `script.voiceover_full` | accepted | fallback for `voiceover_full` |
| `captions` | accepted | caption/karaoke config |
| `export` | accepted | bitrate/codecs/thumbnail |
| `brand` | partially accepted | used to collect SFX from `identity_sting` |

## 3) Main map to `spec_data` (build_spec)

| Final field (`spec_data`) | YAML source (precedence order) | Notes |
|---|---|---|
| `title` | `project.title` -> `meta.title` -> `video.titulo` | required to start the wizard |
| `language` | `project.language`/`project.idioma` -> `meta.language` | |
| `resolution` | `project.format.resolution`/`resolucao` -> `format.resolution` -> `project.resolution` -> `export.resolucao` | |
| `fps` | `project.format.fps` -> `format.fps` -> `project.fps` -> `video.fps` | limited to 12..60 |
| `aspect_ratio` | `project.format.aspect`/`aspect_ratio`/`proporcao` -> `project.aspect_ratio`/`aspect` | |
| `duration_sec` | `project.duration_s`/`duration_sec`/`duracao_s` -> `meta.duration_s`/`duration_sec` -> top-level `duration_s`/`duration_sec`/`duracao_s` -> `video.duracao_total_s`/`duracao_s` | always interpreted in seconds |
| `content_meta.channel` | `project.channel`/`canal` -> `meta.channel`/`canal` -> top-level `channel`/`canal` | |
| `content_meta.series` | `project.series`/`serie`/`season` -> `meta.series`/`serie` -> top-level `series`/`serie` | |
| `content_meta.template` | `project.template`/`template_id` -> `meta.template` -> top-level `template` | |
| `content_meta.video_type` | `project.video_type`/`tipo_video`/`content_type`/`format` -> `meta.video_type`/`tipo_video` -> top-level `video_type`/`tipo_video` | |
| `format_config` | `project.format` or `format` | raw object |
| `style` | `project.style` or `style` | raw object |
| `audio_source_config` | `project.audio` or `audio` | raw object |
| `captions_config` | `captions` -> fallback `style.captions` if object | if `style.captions` is a string with `burn`, enables burn-in |
| `prompts_on_screen` | merge of `prompts` + `prompts_on_screen` (+ `project.*`) | normalized to map `id -> text` |
| `voiceover_full` | `voiceover_full` -> `script.voiceover_full` | |
| `export_config` | `export` | |
| `licenses_note` | `assets.licenses_note` | |

## 4) Scene map (`timeline`/`roteiro`) -> `chapters`

### 4.1 Scene list

`extract_scene_items` looks in this order:

- `timeline` (list)
- `roteiro` (list)
- `scenes` (list)
- `cenas` (list)
- `roteiro.cenas` / `roteiro.scenes`

### 4.2 Scene fields

| Final field (`chapter`) | YAML source | Notes |
|---|---|---|
| `title` | `scene.id` -> `scene.scene_id` -> `scene.cena` -> fallback `Sxx` | |
| `narration` | `scene.narration.text`/`vo`/`narracao` -> `scene.vo` -> `scene.narracao` | fallback per line of `voiceover_full` |
| `duration_sec` | `scene.duracao_s`/`duration_s`/`duration_sec`/`duration` -> calculation by `start/end` -> `tempo` -> automatic fallback | |
| `scene_start_s`/`scene_end_s` | `start_s/end_s` -> `start/end` -> `tempo.ini/fim`/`inicio/final` -> string `tempo: "00:00-00:08"` | |
| `on_screen` | `on_screen` or `texto_tela` -> fallback from `video.layers[type=text].text` | |
| `sfx` | `scene.sfx` + `scene.audio.sfx` + global `project.audio.sfx`/`audio.sfx` | deduplicated |
| `sfx_cues` | `scene.sfx_cues` or `scene.audio.sfx` with `asset_id/sfx_id/id/ref` + `at_s/at_sec/start_s` + `gain_db/volume_db` | absolute times in the episode |
| `scene_assets` | scan `visual`/`visuais`/`shots`/`shot`/`video` for `asset/asset_id/source/file/asset_ref/ref` | |
| `scene_shots` | `scene.shots`/`scene.shot` -> fallback `video.layers` | normalizes shot |
| `prompt_card` | `scene.prompt_card` -> fallback in `scene.inserts[type=prompt_card|prompt]` -> fallback loose fields in the scene (`prompt_ref`, etc.) | see section 5 |

## 5) Prompt map

### 5.1 Global prompt collection

`extract_prompts_map_from_script` merges:

- `prompts`
- `prompts_on_screen`
- `project.prompts`
- `project.prompts_on_screen`

Accepted formats:

- map (`id -> text` or `id -> {text: ...}`)
- list of objects (`id`, `key`, `prompt_id`, `prompt_ref`, `name`)

Accepted text fields per entry:

- `text`, `prompt`, `texto`, `prompt_text`, `value`

### 5.2 Prompt per scene (`prompt_card`)

| Final field | YAML source | Notes |
|---|---|---|
| `prompt_ref` | `prompt_card.prompt_ref`/`prompt_id`/`prompt_key` or scene field `prompt_ref`/`prompt_id`/`prompt_key` | |
| `text` | `prompt_card.text`/`texto`/`prompt_text`/`prompt`, else resolves by `prompt_ref`, else `scene.on_screen_prompt`/`scene.prompt` | |
| `start_s`/`end_s` | `prompt_card.start_s/end_s` or `start/end` | |
| `show` | `prompt_card.show` (default `true`) | |

## 6) Shot map

| Final field (`scene_shots[]`) | YAML source | Notes |
|---|---|---|
| `asset_id` | `asset_id`/`asset`/`ref`/`source` | |
| `asset_type` | `type`/`asset_type`/`tipo` | normalized to `image|video|audio` when possible |
| `duration_sec` | `duration_s`/`duration_sec`/`duracao_s`/`duration` or `end-start` | |
| `notes` | `notes`/`descricao`/`caption`/`instr`/`description` | |
| `start_offset_sec` | `start_offset_s`/`start_offset_sec`/`offset_s` | |
| `shot_start_s`/`shot_end_s` | `start_s`/`end_s` or `start`/`end` | |
| `motion` | `motion` | |
| `fx` | `fx` | normalized list |

## 7) Asset map (external media)

### 7.1 Accepted structures

- `assets.videos[]`
- `assets.images[]`
- `assets.imagens[]`
- `assets.audios[]` / `assets.audio[]`
- `assets.items[]` (mixed)
- `assets` as a simple list
- `assets.<group>` as a map (`id -> object`)

### 7.2 Aliases per asset

| Canonical field | Accepted aliases |
|---|---|
| `source` | `fonte`, `provider` |
| `license` | `license_name`, `licenca` |
| `credit` | `credito` |
| `type` | `tipo` |

When `license/credit` is missing:

- fills defaults by source (`Pexels`, `Unsplash`, `Wikimedia`, etc).

### 7.3 Type classification

`infer_kind_from_hint` uses:

- `type`/`tipo` + group name (`videos`, `images`, `audios`)
- URL extension
- URL patterns (`/video/`, `/photo/`, `/music/`)
- provider heuristics (`unsplash`, `wikimedia`, etc)

## 8) External audio map

### 8.1 Extracting audio assets from YAML

Sources read:

- `audio.music` (list/dict)
- `audio.sfx` (list/dict)
- `audio.music_beds` (map)
- `audio.sfx_library` (map)
- `brand.identity_sting.sfx` (list)

Accepted fields per item:

- `id`/`sfx_id`
- `url`
- `title`
- `gain_db` / `duck_under_vo_db` / `default_gain_db`

These items are collected as `kind=audio` in Step 2.

### 8.2 Normalization for render (`audio_config`)

| Final field | YAML source |
|---|---|
| `audio_config.music[]` | `audio.music[]` + `audio.music_beds.*` |
| `audio_config.music[].asset_id` | `asset_id`/`id` + resolution by aliases |
| `audio_config.music[].start_s/end_s` | `start_s`, `end_s` or `start_sec/end_sec` |
| `audio_config.music[].gain_db` | `duck_under_vo_db` or `gain_db` |
| `audio_config.music[].loop` | `loop` |
| `audio_config.music[].fade.in_s/out_s` | `fade_in_s`/`fade_out_s` or `fade_in_sec`/`fade_out_sec` |
| `audio_config.sfx_cues[]` | `chapter.sfx_cues` + `scene.audio.sfx` with temporal position |
| `audio_config.sfx_cues[].asset_id` | `asset_id`/`sfx_id`/`ref` |
| `audio_config.sfx_cues[].at_s` | `at_s`/`at_sec` (absolutized per scene) |
| `audio_config.sfx_cues[].gain_db` | `gain_db` or convert `volume` to dB |

## 9) Media application in chapters (Step 2 -> spec)

### 9.1 Automatic row construction (`build_auto_rows_for_script`)

- resolves YAML assets by `script_asset_id` and aliases
- tries to match explicit scene shots
- respects scene `duration_sec` and redistributes time per shot
- injects `on_screen`, `prompt_text`, `sfx`, `motion`, `fx`, `start_offset_s`
- fallback: unreferenced assets enter chapters by rotation

### 9.2 Persistence in `spec`

| Destination | Condition |
|---|---|
| `chapters[idx].visuals[]` | item `kind=image|video` |
| `external_assets[]` | any other `kind` (e.g., `audio`) |

Persisted fields per visual:

- `file`, `duration_sec`, `caption`, `notes`, `on_screen`, `prompt_text`, `sfx`
- `scene_id`, `shot_index`, `shot_abs_start_s`, `shot_abs_end_s`
- `shot_type`, `motion`, `fx`, `start_offset_s`, `prompt_start_s`, `prompt_end_s`
- `title`, `kind`, `provider`, `license`, `credit`, `origin_url`, `script_asset_id`

## 10) Caption/karaoke map for render

### 10.1 YAML entries used

- `captions`
- fallback: `style.captions` (object)
- fallback: `style.captions` string (`burn-in` enables burn)
- `style.safe_area` and `captions.safe_area`
- `style.typography` / `style.font_primary`

### 10.2 Render profile fields

| Profile field | Source |
|---|---|
| `caption_position` | `captions.position` |
| `caption_max_chars` | `captions.max_chars_per_line` (with limits per orientation) |
| `caption_box_alpha` | `captions.box_background_alpha` or `captions.box_alpha` |
| `caption_highlight_words` | `captions.highlight_words` |
| `caption_burn_in` | `captions.burn_in` or inferred by `style.captions` |
| `caption_font_size` | `captions.style.font_size` or `captions.font_size` |
| `caption_max_lines` | `captions.style.max_lines` or `captions.max_lines` |
| `font_primary` | `captions.style.font_family` -> `style.font_primary` -> `style.typography.font_primary` |
| `safe_top/bottom/left/right_pct` | `captions.safe_area.*` -> `style.safe_area.*` |

### 10.3 Behavior

- captions rendered via ASS (`subtitles`) with word highlighting (`\kf`)
- safe area enforced in vertical video to avoid captions outside the frame
- Unicode/emojis supported (with escaping for ASS/filtergraph)

## 11) Final export/render map

| Output | YAML source |
|---|---|
| video codec | `export.video_codec` (`h264` -> `libx264`, etc) |
| audio codec | `export.audio_codec` (`aac`, `mp3`, `opus`) |
| video bitrate | `export.video_bitrate` or `export.bitrate` |
| audio bitrate | `export.audio_bitrate` |
| resolution/fps | `resolution`/`fps` already normalized in `spec_data` |
| preview | automatic reduced profile (fps/resolution/bitrate) |
| final | full profile (higher quality) |

## 12) Relevant lint rules for generator

| Code | Rule |
|---|---|
| `E301_PROMPT_REF_NOT_FOUND` | `timeline[].prompt_card.prompt_ref` not found in prompt map |
| `E302_PROMPT_CARD_INVALID` | `prompt_card` missing `text/ref` or (strict) with both |
| `E202_ASSET_REFERENCE_MISSING` | `asset_id` in shot/audio without corresponding asset |
| `E203/E204` | asset without `license`/`credit` (error in strict schema) |
| `E104/E105` | timeline must start at 0 and end with project duration |

## 13) Checklist for generator (100% compatible output)

1. Always emit `project.title` (or `meta.title`) and `project.duration_s` in seconds.
2. Emit `timeline[]` with `start_s`, `end_s`, `vo`, `shots[]`.
3. In `shots[]`, use `asset_id`, `type` (`video|image`) and `duration_s`.
4. Emit `prompts` (or `prompts_on_screen`) and ensure `prompt_card.prompt_ref` exists.
5. For each asset, provide `id`, `source`, `url`, `license`, `credit`.
6. For external audio, prefer `assets.audios`/`assets.items(type=audio)` and reference in `audio.music`/`audio.sfx_cues`.
7. For modern captions, fill `captions` with `mode`, `safe_area`, `style`, `highlight_words`.
8. If using emojis, keep valid UTF-8.
