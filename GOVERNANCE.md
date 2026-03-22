# Governance — USINA Media Script

This repository maintains the evolving open standard known publicly as **USINA Media Script**.

The goal of governance is to keep the standard coherent, portable, testable, and implementation-friendly as the ecosystem grows.

---

## 1) Scope of governance

Governance applies to:
- normative specification changes
- schema changes
- lint/conformance changes
- profile definitions
- extension guidance
- compatibility policy
- official examples and fixtures
- reference tooling that defines expected behavior

---

## 2) Canonical identity

The current canonical identity is:
- **Specification name:** USINA Media Script
- **Schema ID:** `usina.script/v1.0`
- **Canonical extension:** `.usina.yaml`
- **Repository brand:** `USINA-YAML`

Changes to canonical naming should be treated as high-impact decisions.

---

## 3) Decision model

### Maintainer role
The maintainer is responsible for:
- preserving conceptual coherence
- preventing accidental breaking changes
- requiring docs/schema/examples/fixtures to stay aligned
- deciding whether proposals belong in the core, an extension, a profile, or tooling

### Proposal outcomes
A proposal may be:
- **accepted**
- **accepted with revision**
- **postponed**
- **rejected**

The default bias should be toward a small stable core and explicit extension paths.

---

## 4) Change classes

### Class A — Editorial / documentation-only
Examples:
- wording clarifications
- typo fixes
- non-semantic docs improvements

Usually does not require an RFC.

### Class B — Schema-aligned clarification
Examples:
- clarifying required fields already present in the spec
- documentation updates for existing semantics
- fixture additions that do not change meaning

May not require a full RFC, but should still explain impact.

### Class C — Behavioral / lint / conformance change
Examples:
- new lint rule
- stricter reference resolution
- changed interpretation of valid documents
- profile-level rule introduction

Should normally include issue discussion and fixtures.

### Class D — Core standard change
Examples:
- new required field
- changed field meaning
- new version line
- compatibility-affecting semantics

Should normally require an RFC.

---

## 5) RFC expectations

Substantial changes should go through the `RFC/` process.

An RFC should explain:
- problem
- proposal
- alternatives considered
- compatibility impact
- schema impact
- lint impact
- example/fixture implications
- migration story

No major standard change should land without a traceable design rationale.

---

## 6) Compatibility policy (high level)

### Stable line
`usina.script/v1.0` is the current stable schema line.

### Non-breaking changes
Non-breaking clarifications and additive improvements may occur within the same major schema line when they do not alter required semantics incompatibly.

### Breaking changes
Breaking changes require a new schema line, for example:
- `usina.script/v2.0`

### Migration expectation
Breaking changes should include:
- migration notes
- updated examples
- updated fixtures
- schema and lint changes documented together

---

## 7) Core philosophy

Governance decisions should preserve these principles:

1. canonical truth over convenience
2. schema + lint as complementary layers
3. portable semantics over renderer lock-in
4. explicit references and traceability
5. rights and provenance are first-class
6. strict core, flexible extensions
7. profiles instead of uncontrolled fragmentation
8. examples and fixtures are part of the standardization surface

---

## 8) Required sync surfaces for meaningful changes

When a substantive change lands, reviewers should check whether these files also need updates:
- `SPEC.md`
- `README.md`
- `schema/usina.script.v1.0.schema.json`
- `ROADMAP.md`
- examples
- fixtures
- docs pages

A change is incomplete if it silently alters behavior without updating the relevant surfaces.

---

## 9) Official artifacts and expected future structure

Governance recognizes these artifact types as strategically important:
- spec
- schema
- examples
- fixtures
- profiles
- RFCs
- reference CLI
- SDKs
- interop adapters
- provenance / audit tooling

Future companion artifacts may include:
- `.usina.lock`
- `.usina.bundle`
- `.usina.report.json`

---

## 10) Extension guidance

Extensions should preferably be namespaced and must not silently redefine core semantics.

Examples:
- `x_remotion`
- `x_renderer`
- `x_internal_pipeline`

If an extension pattern becomes widely useful across implementations, it may later be proposed for profile-level or core inclusion.

---

## 11) Profiles vs core

When deciding where a feature belongs:

### Put it in the core when
- it is broadly reusable
- it improves portability
- it can be validated/linted consistently
- it does not overfit to one renderer or workflow

### Put it in a profile when
- it is common but workflow-specific
- it adds stricter rules for a known use case
- it should remain optional for the broader ecosystem

### Put it in an extension when
- it is renderer- or org-specific
- it is experimental
- it is not yet stable enough for general standardization

---

## 12) Review standards

Reviewers should ask:
- Is the meaning clear?
- Is the change portable?
- Does it affect compatibility?
- Does it require schema updates?
- Does it require lint updates?
- Does it require fixture coverage?
- Does it require example changes?
- Should it be core, profile, or extension instead?

---

## 13) Long-term governance goal

The long-term goal is for USINA Media Script to mature into a standard that is:
- open
- predictable
- portable
- testable
- auditable
- implementable by multiple independent tools

Governance exists to protect that outcome.
