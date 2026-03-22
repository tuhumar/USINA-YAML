# ROADMAP RESEARCH ADDENDUM — USINA Media Script

This addendum records roadmap improvements derived from competitive and ecosystem research.

It is intended to be merged conceptually into `ROADMAP.md` and treated as part of the active execution plan.

---

## Why this addendum exists

Research across adjacent systems showed recurring strengths that USINA should deliberately absorb without inheriting vendor lock-in.

These areas include:
- template and merge-field ergonomics
- preview and studio-like authoring UX
- callback/status oriented execution workflows
- clearer import/export loss mapping
- low-code / no-code friendliness for simpler automation cases
- stronger bundle/archive portability patterns

---

## New roadmap items to add

## A) Template and variable system hardening

USINA should explicitly grow a more formal template layer.

### Additions
- define template-oriented authoring guidance
- standardize reusable variable substitution semantics
- define profile-safe merge-field behavior
- document how variables interact with prompts, exports, and deliverables
- add template-focused fixtures and examples

### Why
Shotstack and JSON2Video both benefit from template friendliness; USINA should match that ease while remaining open and portable.

---

## B) Preview-oriented authoring UX

USINA should eventually support preview-friendly tooling patterns.

### Additions
- preview-oriented reference render-plan output
- editor guidance for side-by-side YAML + preview workflows
- future Player / Studio style concepts in docs and roadmap
- preview-safe profile starter kits

### Why
Remotion’s strength shows that preview and iteration ergonomics are strategically important.

---

## C) Execution status / callback model

USINA should document a future-neutral way to represent execution status and callback-compatible workflows.

### Additions
- define future status-report artifact expectations
- define webhook/callback integration guidance for adapters
- add roadmap item for render job state reporting
- document separation between portable script and execution telemetry

### Why
Operational render APIs often benefit from callbacks and status tracking; USINA should support this as an interoperable concept rather than a vendor feature.

---

## D) Import/export honesty and interop mapping docs

USINA should document lossless vs lossy mappings more aggressively.

### Additions
- add interop documentation pages per adapter
- add mapping tables for what survives / degrades / is unsupported
- add issue templates for interop mismatch reports

### Why
OTIO’s ecosystem makes clear that trust improves when interop limitations are documented precisely.

---

## E) Low-code / no-code starter flows

USINA should become easier to adopt in simple automation pipelines.

### Additions
- beginner profile kits for faceless automation and templated shortform generation
- variable-first starter examples
- simple import/export examples for API-driven rendering paths
- docs for “minimal useful USINA file” beyond the current minimal valid fixture

### Why
JSON2Video-like ease of use is strategically important for adoption.

---

## F) Bundle and archive improvements

USINA should strengthen future portable packaging work.

### Additions
- define roadmap work for `.usina.bundle`
- define future manifest/checksum expectations
- clarify how bundle artifacts differ from authoring files and lockfiles

### Why
Portable packaging is a major differentiator for long-term interoperability and archival trust.

---

## G) New immediate execution tickets

Add these to the active execution queue:

1. add template-oriented examples and fixtures
2. add docs for variable/merge-field semantics
3. add docs for preview-oriented workflows
4. add callback/status reporting concepts to future docs
5. add adapter mapping docs with lossless/lossy notes
6. add low-code/no-code starter examples
7. add bundle/lockfile concept notes in docs

---

## H) Recommended roadmap wording additions

The main roadmap should explicitly mention:
- template ergonomics as a competitive necessity
- preview/studio/player style UX as a future differentiator
- callback/status compatible execution telemetry
- low-code/no-code adoption as a strategic path
- stronger archive/bundle semantics as a long-term moat

---

## Final note

This addendum is part of the active roadmap direction and should be treated as an authoritative expansion of the strategic plan until it is folded directly back into `ROADMAP.md`.
