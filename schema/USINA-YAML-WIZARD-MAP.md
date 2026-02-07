# Mapa de Mapeamento USINA-YAML -> Wizard/Render

Este documento descreve, de forma operacional, como o `shorts-wizard-app` interpreta o YAML e aplica cada campo no pipeline:

1. parse seguro
2. normalização para `spec_data`
3. construção de capítulos/cenas
4. coleta e materialização de mídia
5. render (vídeo, áudio, legenda)

O objetivo é servir como especificação para qualquer gerador externo de YAML.

## 1) Parse e segurança

| Origem | Regra | Destino interno |
|---|---|---|
| YAML bruto | `yaml.safe_load` | `script_structure` |
| YAML com `<<:`, `!tag`, `&anchor`, `*alias` | bloqueado | retorna vazio / erro de segurança |
| YAML válido | normaliza metadados de assets | `_normalize_assets_metadata` |

## 2) Top-level aceito pelo Wizard

| Namespace | Status | Observação |
|---|---|---|
| `usina_schema` | aceito | exigido apenas no modo strict do lint |
| `project` | aceito | principal no modo legado |
| `meta` | aceito | usado junto com `project` |
| `format` | aceito | fallback de `project.format` |
| `style` | aceito | fallback de `project.style` |
| `audio` | aceito | fallback de `project.audio` |
| `assets` | aceito | suporta listas e grupos |
| `timeline` | aceito | principal para cenas |
| `roteiro`/`scenes`/`cenas` | aceito | compatibilidade |
| `prompts` | aceito | mapa canônico de prompts |
| `prompts_on_screen` | aceito | compatibilidade (merge com `prompts`) |
| `voiceover_full` | aceito | texto longo da narração |
| `script.voiceover_full` | aceito | fallback de `voiceover_full` |
| `captions` | aceito | config de legenda/karaoke |
| `export` | aceito | bitrate/codecs/thumbnail |
| `brand` | aceito parcial | usado para coletar SFX do `identity_sting` |

## 3) Mapa principal para `spec_data` (build_spec)

| Campo final (`spec_data`) | Origem YAML (ordem de precedência) | Notas |
|---|---|---|
| `title` | `project.title` -> `meta.title` -> `video.titulo` | obrigatório para iniciar wizard |
| `language` | `project.language`/`project.idioma` -> `meta.language` | |
| `resolution` | `project.format.resolution`/`resolucao` -> `format.resolution` -> `project.resolution` -> `export.resolucao` | |
| `fps` | `project.format.fps` -> `format.fps` -> `project.fps` -> `video.fps` | limitado a 12..60 |
| `aspect_ratio` | `project.format.aspect`/`aspect_ratio`/`proporcao` -> `project.aspect_ratio`/`aspect` | |
| `duration_sec` | `project.duration_s`/`duration_sec`/`duracao_s` -> `meta.duration_s`/`duration_sec` -> top-level `duration_s`/`duration_sec`/`duracao_s` -> `video.duracao_total_s`/`duracao_s` | sempre interpretado em segundos |
| `content_meta.channel` | `project.channel`/`canal` -> `meta.channel`/`canal` -> top-level `channel`/`canal` | |
| `content_meta.series` | `project.series`/`serie`/`season` -> `meta.series`/`serie` -> top-level `series`/`serie` | |
| `content_meta.template` | `project.template`/`template_id` -> `meta.template` -> top-level `template` | |
| `content_meta.video_type` | `project.video_type`/`tipo_video`/`content_type`/`format` -> `meta.video_type`/`tipo_video` -> top-level `video_type`/`tipo_video` | |
| `format_config` | `project.format` ou `format` | objeto bruto |
| `style` | `project.style` ou `style` | objeto bruto |
| `audio_source_config` | `project.audio` ou `audio` | objeto bruto |
| `captions_config` | `captions` -> fallback `style.captions` se objeto | se `style.captions` for string com `burn`, ativa burn-in |
| `prompts_on_screen` | merge de `prompts` + `prompts_on_screen` (+ `project.*`) | normalizado para mapa `id -> texto` |
| `voiceover_full` | `voiceover_full` -> `script.voiceover_full` | |
| `export_config` | `export` | |
| `licenses_note` | `assets.licenses_note` | |

## 4) Mapa de cenas (`timeline`/`roteiro`) -> `chapters`

### 4.1 Lista de cenas

`extract_scene_items` procura nesta ordem:

- `timeline` (lista)
- `roteiro` (lista)
- `scenes` (lista)
- `cenas` (lista)
- `roteiro.cenas` / `roteiro.scenes`

### 4.2 Campos de cena

| Campo final (`chapter`) | Origem YAML | Notas |
|---|---|---|
| `title` | `scene.id` -> `scene.scene_id` -> `scene.cena` -> fallback `Sxx` | |
| `narration` | `scene.narration.text`/`vo`/`narracao` -> `scene.vo` -> `scene.narracao` | fallback por linha de `voiceover_full` |
| `duration_sec` | `scene.duracao_s`/`duration_s`/`duration_sec`/`duration` -> cálculo por `start/end` -> `tempo` -> fallback automático | |
| `scene_start_s`/`scene_end_s` | `start_s/end_s` -> `start/end` -> `tempo.ini/fim`/`inicio/final` -> string `tempo: "00:00-00:08"` | |
| `on_screen` | `on_screen` ou `texto_tela` -> fallback de `video.layers[type=text].text` | |
| `sfx` | `scene.sfx` + `scene.audio.sfx` + `project.audio.sfx`/`audio.sfx` globais | deduplica |
| `sfx_cues` | `scene.sfx_cues` ou `scene.audio.sfx` com `asset_id/sfx_id/id/ref` + `at_s/at_sec/start_s` + `gain_db/volume_db` | tempos absolutos no episódio |
| `scene_assets` | varredura em `visual`/`visuais`/`shots`/`shot`/`video` por `asset/asset_id/source/file/asset_ref/ref` | |
| `scene_shots` | `scene.shots`/`scene.shot` -> fallback `video.layers` | normaliza shot |
| `prompt_card` | `scene.prompt_card` -> fallback em `scene.inserts[type=prompt_card|prompt]` -> fallback campos soltos na cena (`prompt_ref`, etc.) | ver seção 5 |

## 5) Mapa de prompts

### 5.1 Coleta de prompts globais

`extract_prompts_map_from_script` mescla:

- `prompts`
- `prompts_on_screen`
- `project.prompts`
- `project.prompts_on_screen`

Formatos aceitos:

- mapa (`id -> texto` ou `id -> {text: ...}`)
- lista de objetos (`id`, `key`, `prompt_id`, `prompt_ref`, `name`)

Textos aceitos por entrada:

- `text`, `prompt`, `texto`, `prompt_text`, `value`

### 5.2 Prompt por cena (`prompt_card`)

| Campo final | Origem YAML | Observação |
|---|---|---|
| `prompt_ref` | `prompt_card.prompt_ref`/`prompt_id`/`prompt_key` ou campo na cena `prompt_ref`/`prompt_id`/`prompt_key` | |
| `text` | `prompt_card.text`/`texto`/`prompt_text`/`prompt`, senão resolve por `prompt_ref`, senão `scene.on_screen_prompt`/`scene.prompt` | |
| `start_s`/`end_s` | `prompt_card.start_s/end_s` ou `start/end` | |
| `show` | `prompt_card.show` (default `true`) | |

## 6) Mapa de shots

| Campo final (`scene_shots[]`) | Origem YAML | Notas |
|---|---|---|
| `asset_id` | `asset_id`/`asset`/`ref`/`source` | |
| `asset_type` | `type`/`asset_type`/`tipo` | normalizado para `image|video|audio` quando possível |
| `duration_sec` | `duration_s`/`duration_sec`/`duracao_s`/`duration` ou `end-start` | |
| `notes` | `notes`/`descricao`/`caption`/`instr`/`description` | |
| `start_offset_sec` | `start_offset_s`/`start_offset_sec`/`offset_s` | |
| `shot_start_s`/`shot_end_s` | `start_s`/`end_s` ou `start`/`end` | |
| `motion` | `motion` | |
| `fx` | `fx` | lista normalizada |

## 7) Mapa de assets (mídia externa)

### 7.1 Estruturas aceitas

- `assets.videos[]`
- `assets.images[]`
- `assets.imagens[]`
- `assets.audios[]` / `assets.audio[]`
- `assets.items[]` (misto)
- `assets` como lista simples
- `assets.<grupo>` como mapa (`id -> objeto`)

### 7.2 Aliases por asset

| Campo canônico | Aliases aceitos |
|---|---|
| `source` | `fonte`, `provider` |
| `license` | `license_name`, `licenca` |
| `credit` | `credito` |
| `type` | `tipo` |

Quando `license/credit` não vier:

- preenche defaults por fonte (`Pexels`, `Unsplash`, `Wikimedia`, etc).

### 7.3 Classificação de tipo

`infer_kind_from_hint` usa:

- `type`/`tipo` + nome do grupo (`videos`, `images`, `audios`)
- extensão de URL
- padrões de URL (`/video/`, `/photo/`, `/music/`)
- heurística por provider (`unsplash`, `wikimedia`, etc)

## 8) Mapa de áudio externo

### 8.1 Extração de assets de áudio do YAML

Fontes lidas:

- `audio.music` (lista/dict)
- `audio.sfx` (lista/dict)
- `audio.music_beds` (mapa)
- `audio.sfx_library` (mapa)
- `brand.identity_sting.sfx` (lista)

Campos aceitos por item:

- `id`/`sfx_id`
- `url`
- `title`
- `gain_db` / `duck_under_vo_db` / `default_gain_db`

Esses itens entram como `kind=audio` na coleta do Step 2.

### 8.2 Normalização para render (`audio_config`)

| Campo final | Origem YAML |
|---|---|
| `audio_config.music[]` | `audio.music[]` + `audio.music_beds.*` |
| `audio_config.music[].asset_id` | `asset_id`/`id` + resolução por aliases |
| `audio_config.music[].start_s/end_s` | `start_s`, `end_s` ou `start_sec/end_sec` |
| `audio_config.music[].gain_db` | `duck_under_vo_db` ou `gain_db` |
| `audio_config.music[].loop` | `loop` |
| `audio_config.music[].fade.in_s/out_s` | `fade_in_s`/`fade_out_s` ou `fade_in_sec`/`fade_out_sec` |
| `audio_config.sfx_cues[]` | `chapter.sfx_cues` + `scene.audio.sfx` com posição temporal |
| `audio_config.sfx_cues[].asset_id` | `asset_id`/`sfx_id`/`ref` |
| `audio_config.sfx_cues[].at_s` | `at_s`/`at_sec` (absolutizado por cena) |
| `audio_config.sfx_cues[].gain_db` | `gain_db` ou conversão de `volume` para dB |

## 9) Aplicação de mídia em capítulos (Step 2 -> spec)

### 9.1 Construção automática de linhas (`build_auto_rows_for_script`)

- resolve assets do YAML por `script_asset_id` e aliases
- tenta casar por shots explícitos da cena
- respeita `duration_sec` da cena e redistribui tempo por shot
- injeta `on_screen`, `prompt_text`, `sfx`, `motion`, `fx`, `start_offset_s`
- fallback: assets não referenciados entram em capítulos por rotação

### 9.2 Persistência em `spec`

| Destino | Condição |
|---|---|
| `chapters[idx].visuals[]` | item `kind=image|video` |
| `external_assets[]` | qualquer outro `kind` (ex.: `audio`) |

Campos persistidos por visual:

- `file`, `duration_sec`, `caption`, `notes`, `on_screen`, `prompt_text`, `sfx`
- `scene_id`, `shot_index`, `shot_abs_start_s`, `shot_abs_end_s`
- `shot_type`, `motion`, `fx`, `start_offset_s`, `prompt_start_s`, `prompt_end_s`
- `title`, `kind`, `provider`, `license`, `credit`, `origin_url`, `script_asset_id`

## 10) Mapa de captions/karaoke para render

### 10.1 Entradas YAML usadas

- `captions`
- fallback: `style.captions` (objeto)
- fallback: `style.captions` string (`burn-in` ativa burn)
- `style.safe_area` e `captions.safe_area`
- `style.typography` / `style.font_primary`

### 10.2 Campos de perfil de render

| Campo de perfil | Origem |
|---|---|
| `caption_position` | `captions.position` |
| `caption_max_chars` | `captions.max_chars_per_line` (com limites por orientação) |
| `caption_box_alpha` | `captions.box_background_alpha` ou `captions.box_alpha` |
| `caption_highlight_words` | `captions.highlight_words` |
| `caption_burn_in` | `captions.burn_in` ou inferido por `style.captions` |
| `caption_font_size` | `captions.style.font_size` ou `captions.font_size` |
| `caption_max_lines` | `captions.style.max_lines` ou `captions.max_lines` |
| `font_primary` | `captions.style.font_family` -> `style.font_primary` -> `style.typography.font_primary` |
| `safe_top/bottom/left/right_pct` | `captions.safe_area.*` -> `style.safe_area.*` |

### 10.3 Comportamento

- legenda renderizada via ASS (`subtitles`) com highlight por palavra (`\kf`)
- safe area reforçada em vídeo vertical para evitar legenda fora do quadro
- Unicode/emojis suportados (com escaping para ASS/filtergraph)

## 11) Mapa de export/render final

| Saída | Origem YAML |
|---|---|
| codec de vídeo | `export.video_codec` (`h264` -> `libx264`, etc) |
| codec de áudio | `export.audio_codec` (`aac`, `mp3`, `opus`) |
| bitrate vídeo | `export.video_bitrate` ou `export.bitrate` |
| bitrate áudio | `export.audio_bitrate` |
| resolução/fps | `resolution`/`fps` já normalizados em `spec_data` |
| preview | perfil reduzido automático (fps/resolução/bitrate) |
| final | perfil completo (qualidade maior) |

## 12) Regras de lint relevantes para gerador

| Código | Regra |
|---|---|
| `E301_PROMPT_REF_NOT_FOUND` | `timeline[].prompt_card.prompt_ref` não encontrado no mapa de prompts |
| `E302_PROMPT_CARD_INVALID` | `prompt_card` sem `text/ref` ou (strict) com ambos |
| `E202_ASSET_REFERENCE_MISSING` | `asset_id` em shot/audio sem asset correspondente |
| `E203/E204` | asset sem `license`/`credit` (erro no strict schema) |
| `E104/E105` | timeline deve iniciar em 0 e fechar com duração do projeto |

## 13) Checklist para gerador (saída compatível 100%)

1. Sempre emitir `project.title` (ou `meta.title`) e `project.duration_s` em segundos.
2. Emitir `timeline[]` com `start_s`, `end_s`, `vo`, `shots[]`.
3. Em `shots[]`, usar `asset_id`, `type` (`video|image`) e `duration_s`.
4. Emitir `prompts` (ou `prompts_on_screen`) e garantir que `prompt_card.prompt_ref` exista.
5. Para cada asset, enviar `id`, `source`, `url`, `license`, `credit`.
6. Para áudio externo, preferir `assets.audios`/`assets.items(type=audio)` e referenciar em `audio.music`/`audio.sfx_cues`.
7. Para legenda moderna, preencher `captions` com `mode`, `safe_area`, `style`, `highlight_words`.
8. Se usar emojis, manter UTF-8 válido.

