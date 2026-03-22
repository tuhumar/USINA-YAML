# Naming — USINA Media Script

This document records the current canonical naming decisions for the project.

## Official naming direction

- Public / product-facing name: **USINA Media Script**
- Repository brand: **USINA-YAML**
- Canonical schema ID: `usina.script/v1.0`
- Canonical file extension: `.usina.yaml`

## Why `.usina.yaml`

The `.usina.yaml` extension was chosen because it:
- keeps YAML compatibility explicit
- preserves tooling friendliness for editors and schema-aware workflows
- gives the format a distinctive identity beyond generic `.yaml`
- avoids ambiguous proprietary-looking extensions
- leaves room for future related artifacts

## Example filenames

- `episode_001.usina.yaml`
- `faceless_science_short.usina.yaml`
- `research_explainer_ptbr.usina.yaml`
- `cobra_veneno_short.usina.yaml`

## Related future artifact names

The ecosystem may later include companion artifacts such as:
- `.usina.lock`
- `.usina.bundle`
- `.usina.report.json`

## Naming guidance for docs and tools

Use **USINA Media Script** in public-facing docs, `USINA-YAML` for the repository identity, `usina.script/v1.0` for schema/version discussions, and `.usina.yaml` for authoring workflows and example filenames.
