# Glossary — USINA Media Script

This glossary defines recurring terms used in the USINA ecosystem.

---

## USINA Media Script
The public-facing name of the standard described in this repository.

It refers to the open, tool-agnostic media scripting format centered on the schema identity `usina.script/v1.0` and the canonical file extension `.usina.yaml`.

---

## USINA-YAML
The repository and umbrella project brand.

This name refers to the GitHub project and its broader ecosystem. The public-facing specification name is **USINA Media Script**.

---

## `.usina.yaml`
The canonical file extension for an authored USINA document.

This extension makes the file identity explicit while preserving YAML tooling compatibility.

---

## Schema ID
The stable identifier used to declare which standard line a document follows.

Current canonical value:
- `usina.script/v1.0`

---

## Document
One authored USINA file.

A document is a structured media manifest that may include creative intent, prompts, sources, rights metadata, timing, and export instructions.

---

## Conformant document
A document that satisfies the applicable normative requirements of the specification and the expected schema/lint behavior for its declared schema line.

---

## Specification (spec)
The normative text that defines required and optional behavior, semantics, and constraints for the standard.

In this repository, the main spec lives in `SPEC.md`.

---

## Schema
The machine-readable structural validator for the format.

The schema primarily enforces shape and types. It does not replace semantic lint.

---

## Lint
Semantic validation beyond basic schema structure.

Examples include:
- timeline ordering
- overlap detection
- reference resolution
- end-time consistency
- asset typing expectations

---

## Conformance
The combined idea of structural validity, semantic correctness, and compatibility with the declared standard line.

In practice, conformance is expected to be proven through schema checks, lint checks, and fixture coverage.

---

## Fixture
A sample document used to test expected behavior.

Fixtures may be:
- valid
- invalid
- edge-case oriented

Fixtures are part of the standardization surface because they document intended behavior in executable form.

---

## Profile
A constrained implementation flavor of the core standard.

Profiles allow workflow-specific rules without bloating the core format.

Examples:
- creator shortform
- research explainer
- faceless automation
- studio reviewable
- archive portable

---

## Extension
A namespaced, non-core addition used for renderer-specific, organization-specific, or experimental fields.

Extensions should not silently redefine core semantics.

Examples:
- `x_remotion`
- `x_renderer`
- `x_internal_pipeline`

---

## Asset
A declared media resource referenced by ID.

Assets may include video, image, audio, font, subtitle, or other media-related resources.

---

## Source
A factual reference used to support claims.

A source is not the same thing as an asset. Sources support truth claims; assets support media assembly.

---

## Citation
A reference from script content back to one or more declared sources.

Citations are important for factual media, auditability, and future compliance tooling.

---

## Prompt
A first-class record of an instruction used to generate or transform media, writing, search results, or other production artifacts.

USINA treats prompts as explicit objects rather than hidden application state.

---

## Rights metadata
The licensing and credit information associated with an asset.

This is a core differentiator for USINA because rights are part of the document truth layer, not only external paperwork.

---

## Render plan
A derived execution-oriented representation generated from a USINA document for a specific backend or toolchain.

A render plan is not the same as the authored source document. It is one possible operational output.

---

## Interoperability (interop)
The ability to translate or bridge USINA documents into or out of other ecosystems such as OTIO, FFmpeg workflows, render APIs, or code-first frameworks.

---

## Renderer-neutral
A design principle meaning that the core format should express portable intent without being locked to one execution engine or one vendor-specific schema.

---

## Provenance
The traceable record of where content, claims, prompts, and assets came from.

In the USINA vision, provenance includes sources, citations, prompt lineage, asset lineage, and rights information.

---

## QA
Quality assurance metadata and checks associated with a document.

QA may include lint strictness, legal confirmation, fact review, and future publishing/compliance gates.

---

## Bundle
A future-oriented packaging concept for moving a project and its referenced materials together in a portable form.

This may later appear in artifact types such as `.usina.bundle`.

---

## Lockfile
A future-oriented reproducibility artifact that captures pinned references and integrity expectations.

This may later appear in artifact types such as `.usina.lock`.

---

## Semantic diff
A future capability for comparing two USINA documents by meaning rather than only line-by-line text changes.

---

## Policy pack
A future set of additional lint/compliance rules layered on top of the core standard or a profile.

Examples may include newsroom, medical, legal, or advertising requirements.
