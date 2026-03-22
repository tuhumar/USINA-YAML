# Contributing to USINA Media Script

Thank you for helping improve **USINA Media Script**.

This repository is building an open standard for portable, lintable, AI-native media scripting. Contributions are welcome across specification design, examples, schema work, lint rules, tooling, interoperability, and documentation.

---

## Before you open a PR

Please check whether your change affects one or more of these surfaces:
- `SPEC.md`
- `README.md`
- `schema/usina.script.v1.0.schema.json`
- `ROADMAP.md`
- examples / fixtures

As a rule of thumb:
- **spec change** → update spec + schema/docs/examples as needed
- **schema change** → update schema + fixtures/docs
- **lint or semantic rule change** → update docs + valid/invalid fixtures
- **new example/profile** → explain intended use case and compatibility expectations

---

## Types of contributions

### 1. Specification improvements
Use this for:
- clarifying wording
- adding or refining normative requirements
- improving naming or structure
- documenting interoperability boundaries

### 2. Schema improvements
Use this for:
- structural validation updates
- stricter typing
- new fields already accepted by the spec

### 3. Lint and conformance work
Use this for:
- reference checks
- timeline integrity checks
- rule registries
- valid/invalid fixture suites
- error code design

### 4. Tooling and SDKs
Use this for:
- CLI work
- Python/TypeScript SDKs
- formatters
- reference graph tooling
- editor integrations

### 5. Interop and adapters
Use this for:
- FFmpeg render-plan tooling
- OTIO bridges
- Remotion / Shotstack / JSON2Video export paths
- packaging and bundle work

### 6. Documentation and examples
Use this for:
- examples
- profiles
- tutorials
- glossary / naming docs
- competitive landscape writeups

---

## Preferred workflow

1. Open an issue when the change is non-trivial.
2. Explain the problem clearly.
3. Describe compatibility impact.
4. Submit a focused pull request.
5. Include updated docs/examples/fixtures where relevant.

Small typo and docs-only fixes can usually go directly to PR.

---

## Pull request checklist

Please try to include:

- a clear summary of the change
- why the change is needed
- compatibility notes
- which files were intentionally updated
- fixtures/examples when semantics changed
- migration notes if users may be affected

If your change modifies the standard itself, call that out explicitly.

---

## Compatibility expectations

USINA Media Script uses a stable schema identity such as `usina.script/v1.0`.

Please avoid introducing breaking changes casually.

Breaking changes should normally include:
- rationale
- alternatives considered
- migration story
- schema impact
- lint impact
- example updates

Large standard changes should go through the RFC process in `RFC/`.

---

## Style expectations

- Prefer precise, implementation-friendly wording.
- Use normative language carefully: **MUST**, **SHOULD**, **MAY**, etc.
- Keep examples realistic.
- Do not add fields to the spec without explaining how they validate, lint, and interoperate.
- Prefer portable semantics over renderer-specific assumptions.

---

## Labels and contribution areas

Suggested label taxonomy for issues/PRs:
- `spec`
- `schema`
- `lint`
- `docs`
- `example`
- `interop`
- `governance`
- `breaking-change`
- `good-first-issue`

---

## Code of collaboration

Please discuss ideas in good faith, prefer evidence over intuition, and keep changes traceable. The goal is to build a durable open standard, not just a local project format.

---

## Questions

If you are unsure whether something belongs in the core standard, an extension, a profile, or a renderer-specific namespace, open an issue first.
