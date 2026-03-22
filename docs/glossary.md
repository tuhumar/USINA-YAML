# Glossary — USINA Media Script

This glossary defines the preferred vocabulary for **USINA Media Script**.

The goal is to keep the standard precise, portable, and easy to discuss across documentation, schema work, linting, examples, and adapters.

---

## Core identity terms

### USINA Media Script
The public/product-facing name of the standard.

### USINA-YAML
The repository brand. This may remain the GitHub repository name even when the specification is presented publicly as **USINA Media Script**.

### `usina.script/v1.0`
The canonical schema identifier for the current stable line.

### `.usina.yaml`
The canonical file extension for authoring documents in the standard.

---

## Document structure terms

### Document
A single `.usina.yaml` file.

### Root object
The top-level YAML mapping that contains sections such as `meta`, `assets`, `script`, and `timeline`.

### Section
A top-level or nested named structure in the document, such as `meta`, `audio`, or `export`.

### ID
A unique snake_case identifier used to reference entities such as assets, prompts, sources, scenes, and VO blocks.

---

## Production semantics

### Asset
A declared media resource, such as a video, image, audio file, font, subtitle file, or related project resource.

### Source
A factual reference used to support claims in the media script.

### Citation
A pointer from a script block or other content element to a declared source.

### Prompt
A recorded instruction used to generate or transform content.

### Script
The narrative and textual truth layer of the document.

### Timeline
The authoritative ordered sequence of scenes that covers the entire episode duration.

### Scene
A time-ranged segment of the production with its own shots and optional VO and audio placements.

### Shot
A media unit inside a scene, such as a video clip, image card, text card, or generated visual.

### VO block
A structured voiceover block defined in `script.vo.blocks`, typically referenced from timeline scenes.

### Audio bed
A default background music layer or other global audio layer referenced from `audio.bed`.

### Audio track
A scene-level audio placement inside `audio_tracks`, typically used for music, SFX, ambience, or dialogue timing.

---

## Validation and conformance terms

### Schema validation
Structural validation against the JSON Schema, such as required fields, types, and basic shapes.

### Lint
Semantic validation beyond the schema, such as timeline order, no-overlap rules, reference resolution, and duration consistency.

### Conformance
The combined idea that a document meets both the structural and semantic expectations of the standard.

### Fixture
A test file used to prove valid or invalid behavior for schema/lint tooling.

### Conformance matrix
A document mapping spec requirements to schema coverage, lint coverage, and fixture coverage.

### Error code
A stable identifier for a validation or lint error.

---

## Ecosystem terms

### Profile
A constrained implementation flavor of the core standard for a specific workflow, such as shortform creator workflows or research explainers.

### Extension
An additional namespaced field or behavior outside the core standard, often prefixed with `x_`.

### Adapter
A bridge between USINA and another system, such as OTIO, FFmpeg, Remotion, Shotstack, or JSON2Video.

### Render plan
A deterministic execution-oriented representation derived from a `.usina.yaml` file for a specific backend.

### Bundle
A portable package or manifest-oriented grouping of the document plus referenced resources.

### Lockfile
A future reproducibility artifact intended to pin and verify the exact resources and integrity assumptions needed to reproduce a build.

---

## Governance terms

### RFC
A design proposal used for meaningful changes to the standard, schema, lint behavior, profiles, or interoperability assumptions.

### Core standard
The renderer-neutral, broadly reusable semantics that belong to the main specification.

### Maintainer
The decision-maker responsible for keeping the standard coherent and preventing accidental semantic drift.

### Breaking change
A change that invalidates existing assumptions, files, or implementations in a way that requires a new schema line or explicit migration story.
