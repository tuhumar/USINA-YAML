# USINA Media Script

**Repository:** `USINA-YAML`  
**Canonical schema ID:** `usina.script/v1.0`  
**Canonical extension:** `.usina.yaml`  
**Serialization:** YAML 1.2  
**Status:** v1.0 (stable)

USINA Media Script is an open, tool-agnostic media scripting standard for audiovisual production.

It is designed to be the **single source of truth** for a production artifact:
- creative intent
- timing and structure
- assets
- prompts
- sources and citations
- rights metadata
- export targets
- QA gates

In practice, a `.usina.yaml` file should be readable by humans, lintable by machines, and portable across automation pipelines, renderers, and future editing adapters.

---

## Why this exists

Most media workflows still split reality into two bad options:
- human-friendly but machine-hostile documents
- machine-friendly but human-hostile project files

USINA Media Script aims to sit in the middle:
- readable like a document
- structured like a schema
- versionable like code
- auditable like a manifest
- portable like an interchange format

---

## Canonical identity

These values should be treated as the official naming direction of the standard:

- **Marketing / product-facing name:** **USINA Media Script**
- **Schema ID:** `usina.script/v1.0`
- **Canonical file extension:** `.usina.yaml`
- **Repository brand:** `USINA-YAML`

### Example filenames
- `episode_001.usina.yaml`
- `air_gen_explainer.usina.yaml`
- `cobra_veneno_short.usina.yaml`

---

## What makes USINA different

USINA is not only a timeline format.

It is intended to combine:
- **portable media scripting**
- **semantic validation and lint**
- **prompt-aware generation workflows**
- **source and citation tracking**
- **rights-aware asset manifests**
- **renderer-neutral execution planning**

That makes it relevant for:
- creators
- editors
- AI automation builders
- research media teams
- agencies and studios
- future compliance-oriented pipelines

---

## Repository layout

```text
.
├─ README.md
├─ ROADMAP.md
├─ SPEC.md
├─ CHANGELOG.md
├─ schema/
│  └─ usina.script.v1.0.schema.json
├─ examples/
└─ LICENSE
```

Recommended future additions:
- `CONTRIBUTING.md`
- `GOVERNANCE.md`
- `RFC/`
- `docs/`
- `tests/fixtures/`
- `tools/usina-cli/`
- `sdk/python/`
- `sdk/typescript/`

---

## Quick start

### 1) Create a `.usina.yaml` file

Create a file such as:

```text
examples/my_episode.usina.yaml
```

At minimum, define:
- `usina_schema: "usina.script/v1.0"`
- `meta.duration_s`
- a `timeline` that starts at `0` and ends at `meta.duration_s`
- all `assets` declared once and referenced by `asset_id`

### 2) Validate structure
Use the JSON Schema in:

```text
schema/usina.script.v1.0.schema.json
```

### 3) Lint semantics
USINA expects semantic checks beyond schema validation, such as:
- timeline ordered by `start_s`
- no scene overlap
- first scene starts at `0`
- last scene ends exactly at `meta.duration_s`
- every `asset_id` exists
- every `vo.ref_id` exists
- every citation points to a valid source
- shot durations approximately match scene duration

JSON Schema alone is not enough for these guarantees. That is why the roadmap includes a reference linter and CLI.

---

## Minimal example

```yaml
usina_schema: "usina.script/v1.0"

meta:
  title: "Example Episode"
  episode_id: "example_episode_001"
  language: "en"
  duration_s: 10
  created_at: "2026-03-21T10:00:00-03:00"
  updated_at: "2026-03-21T10:00:00-03:00"
  authors: ["Diego Meirinho C. P. Gonçalves"]
  license: "CC-BY-NC-4.0"
  version: "1.0.0"

format:
  aspect_ratio: "9:16"
  resolution: "1080x1920"
  fps: 30

style:
  tone: "clean"

audio: {}
variables: {}
prompts: []
sources: []

assets:
  - id: intro_card
    type: "image"
    uri: "assets/intro_card.png"
    license: "original"
    credit: "Diego"

script:
  vo:
    blocks:
      - id: vo_01
        text: "This is an example."
        citations: []

timeline:
  - id: scene_01
    start_s: 0
    end_s: 10
    vo: { ref_id: vo_01 }
    shots:
      - type: image
        duration_s: 10
        asset_id: intro_card

export: {}
qa:
  lint:
    strict: true
    tolerance_s: 0.05
```

---

## Design goals

USINA Media Script is being built to support:

1. **single-source-of-truth media manifests**
2. **strict schema + lint validation**
3. **portable execution across multiple backends**
4. **first-class prompts, sources, and citations**
5. **rights-aware asset declarations**
6. **future AI-native and agentic workflows**

---

## What USINA is not

USINA is not trying to be:
- a full NLE project file replacement on day one
- a renderer-specific private schema
- a binary editing container
- a closed cloud API contract

Instead, it should become the open truth layer between authoring intent and execution targets.

---

## Roadmap direction

The roadmap is focused on turning the standard into a real ecosystem:
- canonical docs alignment
- conformance fixtures
- reference lint rules
- `usina` CLI
- SDKs for Python and TypeScript
- profiles for real workflows
- OTIO / FFmpeg / Remotion / API bridges
- provenance and rights tooling
- long-term semantic diff, registry, and agent workflows

See:
- `ROADMAP.md`
- `SPEC.md`
- `CHANGELOG.md`

---

## Contributing

Contributions are welcome.

Strong future contributions include:
- spec clarifications
- schema improvements
- fixture files
- lint rules
- examples
- adapters
- SDK work
- docs and editor tooling

A full contribution process is planned as part of the roadmap.

---

## Licensing

The repository owner can choose the exact public license strategy, but the intended direction is:
- open public standard/spec distribution
- commercial usage handled explicitly where desired

Typical options for spec/document text include Creative Commons licensing, while implementation code may use a software license separately.

---

## North star

USINA Media Script should become:

> the open standard truth layer between creative intent, AI generation, editorial structure, media rights, and execution planning

When that happens, a `.usina.yaml` file stops being just YAML and becomes a portable media contract.
