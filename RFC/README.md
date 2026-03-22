# RFC Process

This directory contains design proposals for meaningful changes to **USINA Media Script**.

RFCs are used when a change may affect:
- core semantics
- compatibility
- schema structure
- lint behavior
- profile definitions
- interoperability expectations
- migration burden

---

## When an RFC is recommended

Open an RFC when the change is more than a typo, wording fix, or narrow documentation clarification.

Typical RFC-worthy topics:
- new fields in the core standard
- changed meaning of existing fields
- new schema line or major version
- new standard profiles
- new compatibility rules
- widely reusable extension patterns
- changes that may invalidate existing files or tooling assumptions

---

## RFC lifecycle

1. Draft the RFC from `0000-template.md`
2. Open a PR adding the RFC file
3. Discuss the proposal in the PR and/or linked issue
4. Revise as needed
5. Maintainer decides: accepted / accepted with revision / postponed / rejected
6. If accepted, implementation work follows in separate PRs when appropriate

---

## Naming convention

Use a numeric prefix and a short slug:

```text
RFC/0001-profile-system.md
RFC/0002-lockfile-concept.md
RFC/0003-otio-bridge.md
```

---

## Important rule

An accepted RFC does not automatically mean the feature is fully implemented.

Implementation still requires:
- spec updates
- schema updates when applicable
- lint/fixture coverage when applicable
- documentation changes
- example updates
- migration notes where relevant

---

## Goal of the RFC process

The RFC process exists to keep USINA Media Script:
- coherent
- portable
- governed by explicit reasoning
- resistant to accidental semantic drift
