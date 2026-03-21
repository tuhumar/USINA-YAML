# ROADMAP — USINA Media Script

**Repository:** `tuhumar/USINA-YAML`  
**Canonical schema ID:** `usina.script/v1.0`  
**Canonical extension:** `.usina.yaml`  
**Marketing name:** **USINA Media Script**  
**Roadmap status:** strategic / competitive / execution-ready  
**Primary horizon:** 12 months  
**Secondary horizon:** 24 months  
**Long horizon:** 36–60 months

---

## 1) Executive summary

USINA already has the hardest starting point: a serious normative core. The next phase is not “more fields”; it is becoming the best **open, lintable, AI-native, renderer-neutral media scripting standard**.

USINA Media Script should combine qualities the current market rarely delivers together:

1. readable declarative authoring
2. strict conformance and semantic lint
3. portable interchange across tools
4. prompt, source, rights, and provenance auditability
5. deterministic automation at scale

That combination is the opportunity.

---

## 2) Canonical naming decisions

These decisions should now be treated as canonical.

### Standard identity
- **Repository brand:** `USINA-YAML`
- **Specification / product-facing brand:** **USINA Media Script**
- **Canonical schema ID:** `usina.script/v1.0`
- **Canonical document extension:** `.usina.yaml`

### Example filenames
- `episode_001.usina.yaml`
- `cobra_veneno_short.usina.yaml`
- `air_gen_explainer.usina.yaml`

### Why this naming is strategically strong
- Keeps YAML compatibility explicit
- Gives the format a recognizable identity beyond plain `.yaml`
- Avoids ambiguous proprietary-looking extensions
- Leaves room for a future artifact family

### Future artifact family
- `.usina.yaml` — canonical authoring format
- `.usina.lock` — reproducibility / integrity lockfile
- `.usina.bundle` — portable packaged project bundle
- `.usina.report.json` — machine-readable validation / audit report

---

## 3) Market opportunity

The market is fragmented across three families:

1. **interchange-first timeline formats**
2. **render/edit API schemas**
3. **code-first video frameworks**

USINA can win by sitting above them as a portable truth layer for:
- creative intent
- timing
- prompts
- sources
- rights
- exports
- QA
- automation metadata

---

## 4) Competitive landscape

## 4.1 OpenTimelineIO (OTIO)
### What OTIO does well
- open-source timeline abstraction
- adapters/plugins
- packaging and portability mindset
- serious interoperability discipline

### What OTIO does not provide strongly
- AI-first authoring semantics
- first-class prompts
- first-class citations and factual provenance
- first-class rights metadata and compliance semantics
- creator-facing semantic lint for publishable media manifests

### What USINA should learn from OTIO
- adapter architecture
- explicit lossless vs lossy interop documentation
- bundle/portability discipline

### How USINA can move ahead
- add `prompts`, `sources`, `qa`, rights, and audit semantics as first-class objects
- create OTIO bridges so USINA becomes the richer upstream truth layer
- make conformance creator-friendly, not just integration-friendly

---

## 4.2 FCPXML and legacy XML interchange workflows
### What they do well
- real editorial ecosystem presence
- practical NLE handoff value
- familiarity in post-production

### What they do not provide strongly
- AI-native authoring model
- modern open governance
- rich source / rights / prompt / compliance semantics
- pleasant developer ergonomics for automation pipelines

### What USINA should learn
- respect editorial reality
- build real import/export bridges
- preserve translation logs for unsupported mappings

### How USINA can move ahead
- be easier to read, validate, diff, and automate
- preserve more meaning about why media exists, not only where it sits
- carry provenance and QA context that XML handoff formats usually drop

---

## 4.3 Remotion
### What it does well
- excellent developer experience
- highly expressive composition model
- strong dynamic generation story
- strong preview/render appeal for app ecosystems

### What it does not provide strongly
- neutral interchange semantics
- portable declarative truth layer across non-React systems
- standard-first conformance and public governance
- built-in provenance / rights / citations model

### What USINA should learn
- preview matters
- developer experience matters
- parametric media generation is core to the future

### How USINA can move ahead
- position USINA as the portable contract and Remotion as one backend
- add `x_remotion` conventions without tying core semantics to React
- separate portable authoring intent from renderer-specific implementation

---

## 4.4 Shotstack
### What it does well
- practical render API
- operationally useful timeline model
- scalable cloud rendering
- template/automation orientation

### What it does not provide strongly
- open governance as a standard
- renderer neutrality
- deep provenance / citation / rights semantics
- long-term archival/interchange framing

### What USINA should learn
- practical usefulness wins adoption
- templates and render plans matter
- cloud-targeted adapters are valuable

### How USINA can move ahead
- stay vendor-neutral
- export into service APIs instead of being defined by one
- keep conformance, openness, and portability as differentiators

---

## 4.5 JSON2Video
### What it does well
- simple automation entry point
- good fit for low-friction, faceless automation use cases
- practical content-at-scale orientation

### What it does not provide strongly
- deep conformance story
- rich provenance model
- public standard identity
- archival/interchange-grade semantics

### What USINA should learn
- low-friction onboarding is a feature
- starter templates matter
- simple happy-path profiles matter

### How USINA can move ahead
- offer beginner-friendly profiles without sacrificing rigor
- become the open format that simple APIs can ingest or emit

---

## 4.6 MLT / engine-oriented open ecosystems
### What they do well
- actual execution grounding
- real open-source production infrastructure
- timeline/render practicality

### What they do not provide strongly
- broad positioning as a general AI-era media script standard
- rich prompt/source/rights/QA semantics
- neutral upstream contract for multi-tool automation

### What USINA should learn
- eventually, real execution matters
- abstract specs become stronger when backed by runnable adapters

### How USINA can move ahead
- act as the neutral upstream contract while bridging to execution engines

---

## 5) The category USINA should own

USINA should explicitly aim to own this category:

> **Open, lintable, AI-native, rights-aware, source-aware, renderer-neutral media scripting**

That is stronger than “timeline format”, stronger than “render API schema”, and more portable than “code-first framework”.

---

## 6) Strategic differentiation

USINA should not try to win by merely adding more fields. It should win by deliberately combining strengths competitors rarely combine:

1. **first-class prompts**
2. **first-class citations and sources**
3. **first-class rights metadata**
4. **first-class QA gates**
5. **profiles for real workflows**
6. **conformance fixtures + badges**
7. **render-plan neutrality**
8. **human + agent co-authoring**

---

## 7) Product thesis

USINA Media Script should become the single source of truth for:
- creative intent
- timing
- assets
- prompts
- citations
- rights
- export targets
- QA gates
- automation metadata

This makes it useful for:
- creators
- editors
- automation builders
- AI video pipelines
- research media teams
- agencies
- future enterprise compliance workflows

---

## 8) Guiding principles

1. canonical truth beats convenience
2. strict core, flexible edges
3. schema is not enough; semantic lint matters
4. everything referenced must exist
5. rights metadata is non-optional
6. AI usage must be auditable
7. portable by default
8. versioning must be explicit
9. examples are part of the standard
10. tooling should teach the standard
11. profiles should reduce fragmentation
12. future identity should remain anchored in `.usina.yaml`

---

## 9) Strategic workstreams

### W1 — Canonical standard core
Make spec, schema, README, examples, glossary, and terminology fully coherent.

### W2 — Conformance and lint
Turn v1.0 into a machine-testable contract.

### W3 — Reference CLI
Ship the official validation/linting/inspection toolkit.

### W4 — SDKs and typed models
Python and TypeScript first; Rust and Go later.

### W5 — Authoring UX
Editor support, snippets, profile starters, AI-safe authoring guidance.

### W6 — Interoperability
Render plans, adapters, import/export bridges.

### W7 — Profiles and examples
Cover real workflows, not just toy demos.

### W8 — Governance
RFCs, compatibility policy, release discipline, extension registry.

### W9 — Provenance and rights
Checksums, manifests, lineage, claim coverage, compliance overlays.

### W10 — Ecosystem and adoption
Docs site, badges, comparison pages, showcases, partner adapters.

### W11 — Competitive moat
Build the things competitors do not combine:
- prompt lineage
- rights metadata
- citations / fact coverage
- profile ecosystem
- conformance + badges
- render-plan neutrality

### W12 — Future systems
Prepare for:
- semantic diff/merge
- collaborative editing
- registry ecosystem
- policy packs
- agentic production loops
- reproducible media builds
- provenance graph bridges

---

## 10) Phased roadmap

## Phase 0 — Naming, canonicalization, and repo hardening
**Window:** Weeks 1–2  
**Priority:** P0

### Deliverables
- officially adopt:
  - `usina.script/v1.0`
  - `.usina.yaml`
  - “USINA Media Script”
- rewrite README around canonical naming and current v1.0 structure
- add `CONTRIBUTING.md`
- add `GOVERNANCE.md`
- add `RFC/`
- add docs index and glossary
- remove stale syntax from entry docs

### Definition of done
A new reader understands the name, file identity, and canonical structure in one pass.

---

## Phase 1 — Conformance foundation
**Window:** Weeks 2–6  
**Priority:** P0

### Deliverables
- rule registry with stable error codes
- valid / invalid / edge-case fixtures
- conformance matrix
- CI validation workflow
- diagnostics with human-readable fixes
- JSON output for machine use
- baseline rule set for timeline integrity, references, audio typing, and rights presence

### Definition of done
Conformance becomes objective, testable, and automatable.

---

## Phase 2 — Reference CLI
**Window:** Month 2  
**Priority:** P0

### Commands
- `usina validate`
- `usina lint`
- `usina explain`
- `usina doctor`
- `usina fmt`
- `usina refs`
- `usina stats`
- `usina bundle`
- `usina migrate`

### Nice-to-have features
- timeline visualization in text
- asset/license report
- citation coverage report
- duplicate/unused asset detection
- shadowed variable detection
- simple autofix for canonicalization cases

### Definition of done
USINA becomes usable without custom glue code.

---

## Phase 3 — Profiles and starter kits
**Window:** Months 2–4  
**Priority:** P1

### Initial profiles
- `creator.shortform.v1`
- `research.explainer.v1`
- `faceless.automation.v1`
- `studio.reviewable.v1`
- `archive.portable.v1`

### Deliverables
- profile docs
- starter templates
- stricter profile lint layers
- extension whitelist guidance

### Definition of done
Users start from realistic templates, not blank files.

---

## Phase 4 — SDKs and typed models
**Window:** Months 2–5  
**Priority:** P1

### Deliverables
- Python package
- TypeScript package
- version-aware parsing
- stable round-trip policy
- extension preservation
- transformation helpers

### Definition of done
Third-party tools stop reimplementing the format ad hoc.

---

## Phase 5 — Competitive interop bridges
**Window:** Months 4–8  
**Priority:** P1

### Must-build bridges
- OTIO import/export bridge
- Shotstack export adapter
- JSON2Video export adapter
- Remotion project/export bridge
- FFmpeg render-plan generator
- TTS/subtitle plan generator
- asset bundler and manifest generator

### Principle
Interop should first produce **render plans**, not magic opaque binaries.

### Definition of done
USINA can sit in the middle of real production ecosystems.

---

## Phase 6 — Provenance, rights, and trust layer
**Window:** Months 5–10  
**Priority:** P1

### Deliverables
- checksums
- lockfile concept
- bundle manifest
- rights completeness reports
- prompt lineage metadata
- derivative asset lineage
- citation coverage reports
- unsupported-rights warnings

### Definition of done
USINA becomes suitable for serious automated media workflows.

---

## Phase 7 — Authoring UX and AI-native workflows
**Window:** Months 5–10  
**Priority:** P1

### Deliverables
- VS Code extension
- YAML language server mapping
- snippets
- AI authoring guide
- prompt-safe generation templates
- lint explanations in plain language

### Definition of done
Humans and agents can co-author `.usina.yaml` reliably.

---

## Phase 8 — v1.1 proposal line
**Window:** Months 6–9  
**Priority:** P2

### Candidate additions
- includes / reusable blocks
- localization packs
- variants
- richer overlays
- normalized transitions
- thumbnail spec
- safe-area metadata
- asset groups
- markers/beats
- multi-deliverable inheritance
- deterministic variable interpolation
- richer prompt lineage
- content warnings / safety fields
- renderer hint conventions

### Definition of done
New core features are evidence-based, not speculative.

---

## Phase 9 — Public positioning and adoption
**Window:** Months 6–12  
**Priority:** P2

### Deliverables
- docs site
- “Why USINA Media Script”
- competitive comparison pages
- compatibility badges
- showcase gallery
- implementation guides
- partner adapter docs

### Definition of done
External builders understand the category and the advantage clearly.

---

## 11) Future-forward roadmap (2–5 year horizon)

## 11.1 Semantic diff and merge
Future tooling should understand scenes, prompts, references, and timing semantically rather than only showing line diffs.

### Future deliverables
- scene-aware diff
- timing-aware merge conflict tools
- asset reference conflict detection
- prompt/source lineage diff
- “what changed in the final edit?” reports

---

## 11.2 Agentic production loops
USINA can become the contract that multiple specialized agents share.

### Future loop
1. research agent gathers sources
2. writing agent drafts script
3. media agent suggests assets
4. compliance agent checks rights and citations
5. render agent produces execution plan
6. review agent audits output
7. optimization agent generates variants

### Why this matters
This turns USINA into the format for agent-to-agent media collaboration.

---

## 11.3 Registry ecosystem
A registry should eventually exist for:
- profiles
- adapters
- validators
- snippets
- templates
- extension namespaces
- house styles
- policy packs

---

## 11.4 Policy packs and compliance overlays
Future organizations may want lint overlays for:
- medical content
- legal claims
- advertising disclosures
- brand safety
- newsroom/editorial standards
- internal publishing requirements

---

## 11.5 Reproducible media builds
The ecosystem should eventually support lockfile-like reproducibility with pinned assets, manifests, seeds, and deterministic execution reports.

---

## 11.6 Provenance graph bridges
USINA should later be able to export rich provenance information into broader authenticity / credential ecosystems without making that dependency part of the core format.

---

## 11.7 Live preview and collaborative editor
A future USINA editor could provide:
- side-by-side YAML + preview
- lint while typing
- scene graph navigation
- source/prompt/rights inspectors
- collaborative comments
- review checkpoints

---

## 11.8 Query language and analytics
A future `usina query` capability could answer questions like:
- which scenes lack citations?
- which assets have weak rights metadata?
- which prompts generated visuals?
- which exports depend on a given asset?
- which scenes changed after review round 2?

---

## 12) Priority backlog

## P0
- canonical naming adoption
- README normalization
- governance + RFCs
- conformance fixtures
- reference linter
- CI validation
- CLI alpha

## P1
- profiles
- SDKs
- VS Code support
- FFmpeg render-plan adapter
- OTIO bridge
- provenance layer
- beginner-friendly starter kits

## P2
- Shotstack / JSON2Video / Remotion bridges
- lockfile and bundle format
- public docs site
- badge ecosystem
- v1.1 line

## P3
- semantic diff/merge
- registry
- policy packs
- collaborative editor
- agentic workflow orchestration
- provenance graph bridges

---

## 13) Immediate next 15 execution tickets

1. officialize “USINA Media Script” in README and docs
2. officialize `.usina.yaml` in spec/docs/examples
3. add naming glossary section
4. rewrite README around canonical v1.0 structure
5. add `CONTRIBUTING.md`
6. add `GOVERNANCE.md`
7. scaffold `RFC/`
8. add issue and PR templates
9. create conformance matrix
10. add minimal valid fixture
11. add invalid overlap fixture
12. add reference linter error code registry
13. add CI validation workflow
14. start `usina` CLI with `validate` and `lint`
15. draft `docs/competitive-landscape.md`

---

## 14) Recommended repository target structure

```text
.
├─ README.md
├─ ROADMAP.md
├─ SPEC.md
├─ CHANGELOG.md
├─ CONTRIBUTING.md
├─ GOVERNANCE.md
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
│  ├─ naming.md
│  ├─ conformance-matrix.md
│  ├─ profiles.md
│  ├─ compatibility-policy.md
│  ├─ competitive-landscape.md
│  ├─ future-directions.md
│  └─ interop/
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

## 15) Success metrics

### Standard maturity
- 100% of v1.0 normative lint rules implemented
- zero contradictions between README, SPEC, schema, and examples
- profile system documented and usable

### Competitive position
- OTIO bridge exists
- at least one cloud render export adapter exists
- at least one code-first framework bridge exists
- provenance and rights story is visibly stronger than competitors

### Adoption
- 10+ official examples
- 3+ profiles
- 2 SDKs
- 1 editor integration
- 1 docs site
- 1 compatibility badge system

### Trust
- reproducible validation outputs
- citation-ready examples
- rights-complete official examples
- machine-readable audit reports

---

## 16) North star

USINA Media Script should become:

> **the open standard truth layer between creative intent, AI generation, editorial structure, media rights, and execution planning**

When that happens, `.usina.yaml` is not just a YAML file. It becomes the portable contract that lets creators, agents, APIs, editors, and renderers collaborate without losing meaning.

---

## 17) Final recommendation

The winning sequence is:

1. lock naming and canonical identity
2. lock conformance
3. ship CLI and fixtures
4. ship profiles
5. ship adapters
6. ship provenance
7. only then expand the core
8. build the long-term moat: semantic tools, registry, agent loops, policy packs

That is how USINA Media Script stops being “a promising spec” and becomes a category-defining standard.
