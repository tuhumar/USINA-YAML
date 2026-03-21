# ROADMAP — USINA-YAML

**Repository:** `tuhumar/USINA-YAML`  
**Roadmap status:** strategic / execution-ready  
**Scope:** evolve USINA-YAML from a strong v1.0 specification into a complete, adoptable, testable, tool-agnostic audiovisual standard and ecosystem.  
**Primary horizon:** 12 months  
**Secondary horizon:** 24 months

---

## 1) Executive summary

USINA-YAML already has the right foundation: a normative specification, a baseline JSON Schema, an example, and a changelog. That is enough to prove the concept, but not yet enough to make the standard easy to trust, implement, validate, or adopt at scale.

The next stage should not be “add more fields.” It should be **standard hardening + ecosystem creation**.

This roadmap therefore focuses on nine parallel objectives:

1. **Canonicalization** — remove ambiguity between README, spec, schema, and examples.
2. **Conformance** — define what “valid” and “portable” really mean in machine-checkable terms.
3. **Tooling** — deliver a reference CLI, lint engine, and diagnostics.
4. **SDKs** — make the standard easy to consume in Python and TypeScript first.
5. **Authoring UX** — examples, templates, snippets, schema mapping, editor support.
6. **Interoperability** — adapters for FFmpeg pipelines, NLE-adjacent tooling, and AI media stacks.
7. **Governance** — RFC process, compatibility policy, release process, and extension rules.
8. **Trust & provenance** — stronger citation, rights, integrity, and auditability workflows.
9. **Adoption** — docs, profiles, showcases, and implementation guides that make the standard usable outside the repo.

The strategic intent is clear:

> **USINA-YAML should become the Markdown + OpenAPI + package-lock mindset for video production pipelines**: human-readable, machine-validated, portable, auditable, extensible, and implementation-friendly.

---

## 2) Current state assessment

### What already exists
- A v1.0 normative specification centered on `usina.script/v1.0`.
- A baseline JSON Schema validator.
- At least one conformant example workflow.
- A changelog with the initial release.
- A repository layout that already hints at “spec + schema + examples” as the canonical structure.

### What is still missing or immature
- Canonical documentation alignment across all repo entry points.
- A real linter implementation for timeline math and cross-reference resolution.
- A formal conformance test suite with valid/invalid fixtures.
- A reference CLI.
- Published SDKs/parsers.
- CI pipelines enforcing schema/lint correctness.
- Editor tooling and authoring ergonomics.
- Governance, extension registry, and RFC flow.
- Version migration policy.
- Interop adapters and reference render plans.
- Rich example corpus across multiple real production scenarios.

### Strategic diagnosis
USINA-YAML is currently **spec-first**.  
To become a real standard, it must become **spec + tooling + fixtures + governance + adoption**.

---

## 3) Product thesis

USINA-YAML should solve five painful classes of problems simultaneously:

### 3.1 Human-machine gap
Creative documents are readable but not automatable. NLE projects are automatable but opaque. USINA-YAML should remain in the middle ground.

### 3.2 Multi-tool fragmentation
A project may pass through LLMs, FFmpeg, motion graphics, NLEs, subtitle tools, TTS engines, search agents, and publishing pipelines. USINA-YAML should describe the production truth without binding itself to one renderer.

### 3.3 Trust and provenance
Modern AI-assisted media pipelines need source tracking, prompt tracking, and rights tracking. USINA-YAML should treat these as first-class objects, not afterthoughts.

### 3.4 Variation at scale
Shorts, dubs, aspect-ratio variants, thumbnails, captions, metadata packages, and A/B hooks should all be expressible without duplicating logic everywhere.

### 3.5 Long-term portability
The format should outlive any single app, plugin, or model provider.

---

## 4) Guiding principles

1. **Canonical truth beats convenience.**  
   There must be one authoritative interpretation for every required field.

2. **Strict core, flexible edges.**  
   The core format should be small, stable, and strongly validated. Extensions should be explicit and namespaced.

3. **Schema is not enough.**  
   USINA-YAML must always distinguish between structural validation and semantic linting.

4. **Everything referenced must exist.**  
   IDs, assets, prompts, sources, VO blocks, and generators should be resolvable.

5. **Rights metadata is non-optional.**  
   Audio, visuals, fonts, and derived assets must stay traceable.

6. **AI usage must be auditable.**  
   Prompt lineage and cited factual blocks should remain inspectable.

7. **Portable by default.**  
   The spec should resist renderer lock-in.

8. **Versioning must be explicit.**  
   Breaking changes require a new schema line.

9. **Examples are part of the standard.**  
   Good examples reduce ambiguity more effectively than prose alone.

10. **Tooling should teach the standard.**  
    The CLI, diagnostics, docs, and editor integration should explain errors in human language.

---

## 5) Strategic workstreams

This roadmap is split into ten major workstreams.

### W1 — Canonical Standard Core
Goal: make the spec, schema, README, examples, and terminology fully coherent.

### W2 — Validation & Conformance
Goal: turn the current “spec says it” model into a machine-tested conformance surface.

### W3 — Tooling & Reference CLI
Goal: make the format practical to author, validate, lint, inspect, and evolve.

### W4 — SDKs & Data Models
Goal: offer stable parsing and manipulation libraries in the languages most likely to drive pipelines.

### W5 — Authoring Experience
Goal: make writing USINA-YAML pleasant in editors, automations, and AI workflows.

### W6 — Interoperability & Render Adapters
Goal: bridge from the abstract format into usable production pipelines.

### W7 — Examples, Fixtures, and Profiles
Goal: represent real-world scenarios, not only a single demo file.

### W8 — Governance & Release Management
Goal: prevent the standard from becoming ad hoc or silently divergent.

### W9 — Provenance, Rights, and Compliance
Goal: make the format safe for research, creator workflows, and future enterprise use.

### W10 — Ecosystem & Adoption
Goal: help external users understand when and why to adopt USINA-YAML.

---

## 6) Phased roadmap

## Phase 0 — Canonicalization and repo hardening
**Target window:** Weeks 1–2  
**Priority:** P0

### Objectives
- Establish a clean canonical entrypoint.
- Remove ambiguity between the README and the normative spec.
- Define the repo as a standards repository, not just a document dump.

### Deliverables
- `ROADMAP.md` added and accepted as the execution plan.
- README rewritten to match the actual v1.0 schema and terminology.
- `CONTRIBUTING.md` added.
- `GOVERNANCE.md` added with maintainer, proposal, and decision flow.
- `RFC/` directory scaffold created.
- GitHub issue templates for:
  - bug in spec
  - schema mismatch
  - linter rule proposal
  - extension proposal
  - interop adapter proposal
- PR template added.
- Label taxonomy defined:
  - `spec`
  - `schema`
  - `lint`
  - `docs`
  - `example`
  - `interop`
  - `governance`
  - `breaking-change`
  - `good-first-issue`
- Standard glossary added to docs.
- Terminology normalized:
  - `usina_schema`
  - `meta`
  - `assets[].uri`
  - `script`
  - `timeline`
  - `qa`
  - `export`

### Definition of done
- A new reader can enter via README and never encounter conflicting field names or old syntax.
- The canonical file layout is documented and stable.
- Every standards change has an obvious contribution path.

---

## Phase 1 — Conformance foundation
**Target window:** Weeks 2–6  
**Priority:** P0

### Objectives
- Convert the v1.0 spec into a tested conformance baseline.
- Separate schema failures from lint failures and reference failures.

### Deliverables
- Reference linter spec document:
  - rule IDs
  - severity levels
  - diagnostic messages
  - fix hints
- `tests/fixtures/valid/` corpus
- `tests/fixtures/invalid/` corpus
- `tests/fixtures/edge_cases/` corpus
- Machine-readable expected results for each fixture.
- Conformance matrix that maps:
  - spec section
  - schema coverage
  - lint coverage
  - fixture coverage
- CI workflow:
  - YAML parse checks
  - JSON Schema validation
  - lint pass
  - docs link checks
- Baseline linter rules implemented:
  - timeline ordering
  - no overlap
  - first scene starts at 0
  - last scene ends at `meta.duration_s`
  - shot duration sum tolerance
  - valid asset references
  - valid prompt references
  - valid citation references
  - valid VO references
  - `audio.bed` and `audio_tracks` audio-type enforcement
- Error code namespace such as:
  - `USINA-SCHEMA-001`
  - `USINA-LINT-014`
  - `USINA-REF-006`

### Definition of done
- The repo can prove which documents are conformant and why non-conformant ones fail.
- Every normative lint rule from v1.0 has at least one passing and one failing fixture.

---

## Phase 2 — Reference CLI
**Target window:** Month 2  
**Priority:** P0

### Objectives
- Ship a reference developer tool that makes the standard operational.

### Proposed CLI name
- `usina`
- or `usina-cli`

### Minimum command set
- `usina validate file.yml`
- `usina lint file.yml`
- `usina explain file.yml`
- `usina init profile`
- `usina doctor file.yml`
- `usina fmt file.yml`
- `usina refs file.yml`
- `usina stats file.yml`
- `usina bundle file.yml`
- `usina migrate file.yml --to usina.script/v1.1`

### Core capabilities
- YAML parsing with stable error messages.
- Schema validation against known schema IDs.
- Lint execution with severity filtering.
- Resolved reference graph output.
- Human-readable summary mode.
- JSON output mode for CI and automation.
- Exit codes suitable for pipelines.
- `--strict` mode.
- `--tolerance-s` override.
- Support for remote schemas and local vendored schemas.

### Nice-to-have capabilities
- auto-fix for simple canonicalization cases
- timeline visualization in text
- asset/license report
- source/citation coverage report
- duplicate/unused asset detection
- shadowed variable detection

### Definition of done
- A user can author or audit a file without writing custom validation code.
- CI can rely on the reference CLI as the enforcement tool.

---

## Phase 3 — SDKs and typed models
**Target window:** Months 2–4  
**Priority:** P1

### Objectives
- Make the format easy to integrate into Python-first and TypeScript-first pipelines.

### Deliverables
#### Python package
- `usina_yaml` or similar
- parse
- validate
- lint
- typed dataclasses / Pydantic models
- reference graph utilities
- fixture-driven tests

#### TypeScript package
- `@usina/core`
- typed interfaces
- schema validation wrappers
- lint bindings
- reference resolution helpers
- AST-like utilities for transformations

#### Shared model goals
- preserve comments where possible
- stable round-trip serialization policy
- deterministic key ordering in formatter mode
- extension preservation (`x_*`)
- version-aware parsing

### Future SDK candidates
- Rust
- Go
- Java/Kotlin for enterprise integrations

### Definition of done
- External tooling no longer needs to scrape YAML ad hoc.
- Integrators can use stable libraries instead of reimplementing the format.

---

## Phase 4 — Authoring UX and editor support
**Target window:** Months 3–5  
**Priority:** P1

### Objectives
- Make authoring fast, safe, and pleasant.

### Deliverables
- VS Code extension:
  - schema association
  - completion
  - hover docs
  - snippets
  - lint diagnostics
- `yaml-language-server` mapping docs
- snippet packs:
  - short explainer
  - science short
  - interview clip
  - slideshow
  - faceless short
  - multilingual variant
- style guide for:
  - IDs
  - naming
  - asset hygiene
  - source quality
  - citation placement
  - prompt recording
- cookbook pages:
  - adding background music
  - scene VO mapping
  - generated image shot
  - source-backed claims
  - localized script variants
  - thumbnail metadata generation
- AI authoring guide:
  - how LLMs should generate conformant files
  - safe prompt patterns
  - anti-hallucination guidance
  - reference completeness checklist

### Definition of done
- New users can generate a conformant file in under 10 minutes.
- The editor experience reduces structural errors before CI even runs.

---

## Phase 5 — Examples, profiles, and fixture expansion
**Target window:** Months 3–6  
**Priority:** P1

### Objectives
- Show breadth, not just one sample.

### Example families
- 15s curiosity short
- 30s educational short
- 60s narrated explainer
- long-form chaptered video
- podcast clip with captions
- image-only infographic short
- B-roll heavy documentary excerpt
- multilingual localization variant
- audio-first workflow
- no-source creative fiction workflow
- source-heavy scientific explainer
- ad-safe product promo profile
- faceless channel automation profile

### Profiles to define
A **profile** is a constrained implementation flavor of the core standard.

Initial proposed profiles:
- `creator.shortform.v1`
- `research.explainer.v1`
- `faceless.automation.v1`
- `studio.reviewable.v1`
- `archive.portable.v1`

Each profile should define:
- required sections
- stricter lint rules
- recommended deliverables
- citation expectations
- rights expectations
- extension whitelist

### Definition of done
- Users can start from examples that resemble their actual workflow.
- Profiles demonstrate how the core standard can remain stable while use cases specialize.

---

## Phase 6 — Interoperability and adapters
**Target window:** Months 4–8  
**Priority:** P1

### Objectives
- Prove that USINA-YAML is not just descriptive; it is operationally useful.

### Adapter priorities
#### A. FFmpeg render-plan adapter
- derive render commands
- map timeline shots to concat/filter graphs
- resolve audio bed and SFX placements
- output render plan JSON before execution

#### B. TTS / subtitle adapter
- map VO blocks to TTS jobs
- emit SRT/VTT sidecars
- align subtitles with scene windows

#### C. Asset fetch / bundle adapter
- create portable project bundles
- copy or manifest referenced local/remote assets
- generate checksums and rights manifest

#### D. AI media adapter
- convert prompts + variables + sources into job plans for image/video/text generation systems

#### E. NLE-adjacent export/import experiments
- OpenTimelineIO mapping where applicable
- EDL/XML compatibility analysis
- import/export boundary docs for Premiere/Resolve/OpenShot-like tooling

### Key principle
Interop should first produce **render plans**, not magic opaque binaries.  
That keeps the standard auditable and debuggable.

### Definition of done
- At least one adapter can take a conformant file and produce a deterministic execution plan.
- The repo documents which parts of interop are lossless, lossy, or unsupported.

---

## Phase 7 — v1.1 feature line
**Target window:** Months 6–9  
**Priority:** P2 unless blocked by real adoption feedback

### Objective
Only after v1.0 is well hardened should new core features be standardized.

### Candidate v1.1 areas
- reusable scene fragments / includes
- localization packs
- variant matrices
- richer overlay model
- normalized transition object
- normalized thumbnail specification
- explicit safe-area metadata
- shot-level source mapping
- asset groups / collections
- timeline markers / beats
- multi-deliverable inheritance
- deterministic variable interpolation rules
- richer prompt lineage fields
- content warnings / safety metadata
- renderer hints namespace conventions

### Constraints
- No breaking changes without new schema ID.
- New features must ship with:
  - schema updates
  - lint updates
  - example coverage
  - migration guidance
  - interop impact notes

### Definition of done
- v1.1 is based on evidence from tooling and examples, not speculation.
- Every new field has a concrete implementation story.

---

## Phase 8 — Governance, RFCs, and compatibility policy
**Target window:** Months 2–9, ongoing  
**Priority:** P1

### Objectives
- Keep the standard coherent as contributions grow.

### Deliverables
- `RFC/README.md`
- RFC template:
  - problem
  - proposal
  - alternatives
  - compatibility impact
  - schema impact
  - lint impact
  - examples required
  - migration story
- Compatibility policy:
  - patch/minor/major expectations
  - schema ID rules
  - deprecation window
  - extension namespace expectations
- Maintainer decision model:
  - accepted
  - accepted with revision
  - postponed
  - rejected
- Release checklist:
  - spec synced
  - schema synced
  - fixtures updated
  - examples updated
  - changelog updated

### Definition of done
- No substantive standard change can land without a traceable decision and migration story.

---

## Phase 9 — Provenance, integrity, rights, and compliance
**Target window:** Months 5–10  
**Priority:** P1/P2 depending on adoption

### Objectives
- Strengthen the format for serious usage.

### Deliverables
- asset checksum strategy
- source integrity guidance
- rights completeness report format
- optional lockfile / manifest concept
- recommended `bundle.json` or `manifest.json`
- derivative-asset lineage model
- prompt provenance expansion:
  - model
  - provider
  - generation timestamp
  - safety mode
  - seed if applicable
- legal/compliance profile examples
- citation coverage metrics
- risk flags for unsupported rights metadata

### Future direction
- signed manifests
- reproducible bundles
- provenance graph export
- enterprise policy overlays

### Definition of done
- A generated production can be audited for claims, rights, and asset lineage with reasonable confidence.

---

## Phase 10 — Ecosystem, adoption, and public positioning
**Target window:** Months 6–12  
**Priority:** P2

### Objectives
- Make the standard discoverable and legible to external builders.

### Deliverables
- public docs site
- “Why USINA-YAML” page
- “When not to use USINA-YAML” page
- adoption guide for:
  - solo creators
  - AI automation builders
  - research media teams
  - agencies / studios
- implementation badges:
  - schema-compatible
  - lint-compatible
  - profile-compatible
- showcase gallery of real projects
- comparison docs:
  - USINA-YAML vs ad hoc JSON
  - USINA-YAML vs NLE-native project files
  - USINA-YAML vs timeline interchange formats

### Definition of done
- A new adopter can understand the value proposition in one visit.
- Third parties can claim compatibility with a clear meaning.

---

## 7) Proposed milestone map

### Milestone M1 — Canonical v1.0 repository
**Outcome:** repo is coherent, navigable, and contributor-ready.

Includes:
- roadmap
- canonical README
- contributing + governance
- issue/PR templates
- docs index

### Milestone M2 — Conformance kit
**Outcome:** every normative rule has machine-test coverage.

Includes:
- fixture suite
- lint rule registry
- CI enforcement
- conformance matrix

### Milestone M3 — Reference CLI alpha
**Outcome:** users can validate, lint, and inspect a file from the command line.

Includes:
- `validate`
- `lint`
- `doctor`
- `explain`
- JSON output

### Milestone M4 — SDK baseline
**Outcome:** Python and TypeScript integrations become first-class.

Includes:
- typed models
- parser wrappers
- fixture-driven tests
- docs

### Milestone M5 — Authoring DX
**Outcome:** generating correct files becomes easy in editors and AI workflows.

Includes:
- VS Code extension
- snippets
- cookbook
- AI authoring guide

### Milestone M6 — Interop proof
**Outcome:** at least one adapter turns USINA-YAML into deterministic executable work.

Includes:
- FFmpeg render-plan adapter
- bundle/export manifest
- TTS/subtitle mapping

### Milestone M7 — v1.1 proposal package
**Outcome:** next-version changes are evidence-based and migration-ready.

Includes:
- RFCs
- compatibility notes
- migration guide
- examples

---

## 8) Priority backlog by severity

## P0 — Must happen first
- Add roadmap.
- Normalize README to current spec.
- Add contributing/governance/RFC scaffolding.
- Create valid/invalid fixture suite.
- Implement lint engine or at minimum a reference linter.
- Add CI validation workflow.
- Publish CLI alpha.

## P1 — High leverage
- Python and TypeScript SDKs.
- VS Code support.
- Multiple real-world examples.
- Render-plan adapter for FFmpeg.
- Profile system.
- Compatibility policy.

## P2 — Strategic expansion
- NLE interop experiments.
- Lockfile / signed manifest work.
- v1.1 advanced feature line.
- Public docs site and badge ecosystem.

## P3 — Long horizon
- broader language SDKs
- enterprise governance overlays
- signed provenance graph
- large-scale registry / marketplace / template ecosystem

---

## 9) Immediate next 12 execution tickets

1. Add `ROADMAP.md`.
2. Rewrite README to the actual v1.0 canonical structure.
3. Add `CONTRIBUTING.md`.
4. Add `GOVERNANCE.md`.
5. Scaffold `RFC/` with template and process.
6. Add GitHub issue templates and PR template.
7. Add `docs/glossary.md`.
8. Create `tests/fixtures/valid/minimal_valid.yml`.
9. Create `tests/fixtures/invalid/timeline_overlap.yml`.
10. Add conformance matrix doc.
11. Add CI workflow for schema validation.
12. Start reference CLI with `validate` and `lint` commands.

---

## 10) Risks and mitigations

### Risk 1 — The standard expands faster than tooling
**Mitigation:** freeze new core fields until conformance tooling is real.

### Risk 2 — README/spec/schema drift
**Mitigation:** require all standard PRs to update all three surfaces together.

### Risk 3 — Overfitting to one renderer or one creator workflow
**Mitigation:** use profiles and namespaced extensions instead of polluting core semantics.

### Risk 4 — Ambiguous interop expectations
**Mitigation:** document lossless vs lossy mappings explicitly.

### Risk 5 — AI-generated invalid files
**Mitigation:** publish strict authoring guidelines, snippets, and machine-readable diagnostics.

### Risk 6 — Enterprise/commercial adoption blocked by trust concerns
**Mitigation:** prioritize checksums, manifests, provenance, and rights reporting.

---

## 11) Success metrics

### Standard maturity
- 100% of normative v1.0 lint rules implemented in reference tooling.
- 100% of normative rules covered by fixtures.
- zero known contradictions between README, spec, and schema.

### Tooling adoption
- reference CLI published and used in CI
- Python and TypeScript packages published
- editor support available

### Ecosystem growth
- at least 10 example files across distinct workflows
- at least 3 profiles documented
- at least 1 real adapter producing deterministic execution plans

### Quality and trust
- reproducible validation results
- explicit rights metadata in all official examples
- citation-ready examples for factual content

---

## 12) Long-term north star

USINA-YAML should eventually support this full loop:

1. A creator or agent writes a conformant YAML file.
2. The file validates structurally and semantically.
3. Tooling resolves assets, citations, prompts, and timeline intent.
4. Adapters generate execution plans for rendering, TTS, captions, thumbnails, metadata, and packaging.
5. Outputs remain traceable back to sources, prompts, and assets.
6. The same project can be ported across tools without losing the editorial truth layer.

When that loop is stable, USINA-YAML stops being “a spec repo” and becomes a real production standard.

---

## 13) Recommended repository target structure

```text
.
├─ README.md
├─ ROADMAP.md
├─ SPEC.md
├─ CHANGELOG.md
├─ CONTRIBUTING.md
├─ GOVERNANCE.md
├─ LICENSE
├─ LICENSE_OPTION_CC_BY_NC.md
├─ RFC/
│  ├─ README.md
│  └─ 0000-template.md
├─ schema/
│  └─ usina.script.v1.0.schema.json
├─ examples/
│  ├─ shortform/
│  ├─ longform/
│  ├─ profiles/
│  └─ localization/
├─ docs/
│  ├─ glossary.md
│  ├─ conformance-matrix.md
│  ├─ profiles.md
│  ├─ compatibility-policy.md
│  ├─ interop/
│  └─ cookbook/
├─ tests/
│  ├─ fixtures/
│  │  ├─ valid/
│  │  ├─ invalid/
│  │  └─ edge_cases/
│  └─ expected/
├─ tools/
│  └─ usina-cli/
└─ sdk/
   ├─ python/
   └─ typescript/
```

---

## 14) Final recommendation

Do not treat the next phase as “write more documentation.”

Treat it as:

- **lock the canonical model**
- **build the conformance surface**
- **ship the reference tooling**
- **prove interoperability**
- **only then expand the core**

That sequencing gives USINA-YAML the best chance of becoming durable, credible, and genuinely useful across creator workflows, AI pipelines, and future production systems.
