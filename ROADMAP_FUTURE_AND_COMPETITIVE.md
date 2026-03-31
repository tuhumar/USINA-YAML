# ROADMAP ADDENDUM — Future Strategy, Competitive Landscape, and Canonical Naming

**Repository:** `tuhumar/USINA-YAML`  
**Canonical schema ID:** `usina.script/v1.0`  
**Canonical extension:** `.usina.yaml`  
**Marketing name:** **USINA Media Script**

This addendum extends `ROADMAP.md` and should be merged conceptually into the main roadmap in the next documentation consolidation pass.

---

## 1) Canonical naming decisions

These names should now be treated as the official direction for the project.

### Standard identity
- **Repository brand:** `USINA-YAML`
- **Specification / product-facing brand:** **USINA Media Script**
- **Canonical schema ID:** `usina.script/v1.0`
- **Canonical document extension:** `.usina.yaml`

### Why this naming is strategically strong
- It preserves the immediate tooling value of YAML.
- It gives the format an identity beyond plain `.yaml`.
- It avoids extension ambiguity while remaining editor- and schema-friendly.
- It leaves room for future companion artifacts like lockfiles, bundles, and reports.

### Future artifact family
- `.usina.yaml` — canonical authoring format
- `.usina.lock` — reproducibility / integrity lockfile
- `.usina.bundle` — portable packaged project bundle
- `.usina.report.json` — machine-readable validation / audit report

---

## 2) Competitive landscape

The market is split across three clusters:

1. **Open interchange timelines** like OTIO and XML-based editorial interchange.
2. **Render/edit APIs** like Shotstack and JSON2Video.
3. **Code-first composition frameworks** like Remotion.

USINA Media Script can become valuable precisely because it can sit **above** these categories as a portable truth layer.

---

## 3) Competitor-by-competitor analysis

## 3.1 OpenTimelineIO (OTIO)
### What it does well
- Open-source timeline abstraction
- Adapter/plugin system
- Serious interoperability mindset
- Packaging/bundle concepts
- Useful as an interchange backbone

### What it does not provide strongly
- AI-first authoring semantics
- first-class prompt lineage
- first-class citations and factual sources
- first-class asset rights + license/credit auditing
- creator-facing semantic lint built around publishing workflows

### What USINA should copy or learn from
- Adapter architecture
- Interop documentation discipline
- “lossless vs lossy” conversion honesty
- Bundling and portability mindset

### How USINA can beat it
- Treat media scripting as more than editorial timeline interchange
- Add first-class `prompts`, `sources`, `qa`, and rights metadata
- Add creator/automation profiles and semantic lint
- Add OTIO import/export bridges so USINA becomes the richer superset truth layer

---

## 3.2 FCPXML / legacy XML interchange ecosystems
### What they do well
- Strong foothold in professional editorial workflows
- Useful for handoff between existing tools
- Familiar to real post-production teams

### What they do not provide strongly
- Clean AI-native authoring model
- neutral governance as a public standard
- rich provenance, citations, prompt lineage, or compliance semantics
- elegant developer ergonomics for automation builders

### What USINA should copy or learn from
- Respect editorial reality
- Make import/export practical, not theoretical
- Preserve explicit logs for translation limits

### How USINA can beat them
- Be easier to read, validate, version, and automate
- Retain more contextual meaning around why media exists, not just where it sits
- Carry source, rights, and QA semantics that XML handoff formats usually drop

---

## 3.3 Remotion
### What it does well
- Excellent developer experience
- Very expressive code-first video composition
- Strong for dynamic, parameterized generation
- Strong preview/render story for app ecosystems

### What it does not provide strongly
- neutral interchange standard semantics
- portable declarative truth layer across non-React systems
- built-in provenance/citation/rights model
- conformance and profile ecosystem as a public format standard

### What USINA should copy or learn from
- Preview matters
- developer experience matters
- parametric generation is central to the future

### How USINA can beat it
- Position USINA as the portable declarative contract; Remotion becomes one backend
- Add `x_remotion` conventions without tying core semantics to React
- Keep YAML intent layer stable while allowing expressive render backends

---

## 3.4 Shotstack
### What it does well
- Practical render API
- operationally useful timeline schema
- scalable cloud rendering
- templating and automation focus

### What it does not provide strongly
- open governance as a standard
- renderer neutrality
- long-term archival/interchange framing
- provenance / source / rights / audit depth

### What USINA should copy or learn from
- Practicality wins
- render plans and templates matter
- execution-oriented adapter outputs are valuable

### How USINA can beat it
- Stay vendor-neutral
- export into service APIs instead of becoming trapped by one
- keep open governance and conformance as a differentiator

---

## 3.5 JSON2Video
### What it does well
- simple automation entry point
- no-code / faceless automation friendliness
- practical content-at-scale orientation

### What it does not provide strongly
- deep conformance model
- rich provenance model
- public standard identity
- archival/interchange-grade semantics

### What USINA should copy or learn from
- Low-friction onboarding
- starter templates
- simple happy-path profiles

### How USINA can beat it
- Offer beginner-friendly profiles without sacrificing rigor
- become the open format that simple APIs can ingest or emit

---

## 3.6 MLT / engine-oriented open ecosystems
### What they do well
- actual execution grounding
- real open-source production infrastructure
- timeline/render practicality

### What they do not provide strongly
- general-purpose AI-era media manifest semantics
- broad ecosystem positioning as a portable media script standard
- rich prompt/source/rights/QA model

### What USINA should copy or learn from
- Eventually, real execution matters
- abstract specs become stronger when grounded in runnable adapters

### How USINA can beat them
- Act as the neutral upstream contract while bridging to execution engines

---

## 4) The category USINA should own

USINA should explicitly aim to own this category:

> **Open, lintable, AI-native, rights-aware, source-aware, renderer-neutral media scripting**

That is stronger than “timeline format,” stronger than “render API schema,” and more portable than “code-first framework.”

---

## 5) Features that create a moat

### 5.1 First-class prompts
Prompts should be first-class objects, not hidden app state.

### 5.2 First-class citations and sources
USINA should be unusually strong for factual and research-backed media.

### 5.3 First-class rights metadata
Each asset should remain traceable in terms of license, credit, and derivative lineage.

### 5.4 First-class QA
QA should live in the format, not only in external checklists.

### 5.5 Profiles
Profiles let the core remain stable while real-world usage becomes specialized.

### 5.6 Conformance badges and fixtures
Compatibility must be machine-verifiable, not marketing language.

### 5.7 Render-plan neutrality
One USINA file should be able to target many execution stacks.

### 5.8 Human + agent co-authoring
The format should be easy for humans, strict for machines, and legible for LLMs.

---

## 6) Additions to the core roadmap

The following workstreams should be added or emphasized inside the main roadmap.

### New workstream: Competitive moat
Build the things competitors do not combine:
- prompt lineage
- rights metadata
- citations / fact coverage
- profile ecosystem
- conformance + badges
- render-plan neutrality

### New workstream: Future systems
Prepare for:
- semantic diff/merge
- collaborative editing
- registry ecosystem
- policy packs
- agentic production loops
- reproducible media builds
- provenance graph bridges

---

## 7) Future-forward ideas (2–5 year horizon)

## 7.1 Semantic diff and merge
Future USINA tooling should understand scenes, prompts, references, and timing semantically rather than showing only line diffs.

## 7.2 Agentic production loops
USINA can become the contract that multiple specialized agents share:
- research
- writing
- sourcing
- compliance
- rendering
- optimization

## 7.3 Registry ecosystem
A registry should eventually exist for:
- profiles
- adapters
- validators
- snippets
- templates
- extension namespaces
- house styles
- policy packs

## 7.4 Policy packs
Future organizations may need lint overlays for:
- medical content
- legal claims
- advertising disclosures
- brand safety
- newsroom/editorial standards

## 7.5 Reproducible media builds
The ecosystem should eventually support lockfile-like reproducibility with pinned assets, manifests, and deterministic execution reports.

## 7.6 Provenance graph bridges
USINA should later be able to export rich provenance information into broader authenticity/credential systems without making that dependency part of the core format.

## 7.7 Live preview + collaborative editor
A future editor could provide:
- side-by-side YAML + preview
- lint while typing
- scene graph navigation
- source/prompt/rights inspectors
- review checkpoints

## 7.8 Query language and analytics
A future `usina query` capability could answer questions like:
- which scenes lack citations?
- which assets have weak rights metadata?
- which prompts generated visuals?
- which exports depend on a given asset?

---

## 8) New near-term priorities to merge into the main roadmap

### Add to P0
- officialize `.usina.yaml`
- officialize “USINA Media Script”
- normalize all examples and docs around canonical naming

### Add to P1
- OTIO bridge
- provenance / rights strength as a visible differentiator
- beginner-friendly profile starter kits

### Add to P2
- Shotstack export adapter
- JSON2Video export adapter
- Remotion bridge
- public competitive comparison pages

### Add to P3
- semantic diff / merge
- registry ecosystem
- policy packs
- collaborative editor
- agentic orchestration loops

---

## 9) Suggested documentation follow-ups

After merging this addendum, the repo should likely gain:
- `docs/competitive-landscape.md`
- `docs/naming.md`
- `docs/profiles.md`
- `docs/compatibility-badges.md`
- `docs/future-directions.md`

---

## 10) Final positioning statement

USINA Media Script should become:

> **the open standard truth layer between creative intent, AI generation, editorial structure, media rights, and execution planning**

If the project executes well, `.usina.yaml` stops being just a YAML file and becomes the portable contract that lets creators, agents, APIs, editors, and renderers collaborate without losing meaning.
