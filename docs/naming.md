# Naming — USINA Media Script

This document defines the canonical naming strategy for the standard and its future companion artifacts.

---

## 1) Canonical names

### Public-facing specification name
**USINA Media Script**

This is the preferred name when referring to the standard itself in documentation, discussions, and future ecosystem positioning.

### Repository / umbrella project name
**USINA-YAML**

This remains the GitHub repository and umbrella project identity.

### Canonical schema ID
`usina.script/v1.0`

This identifies the current stable schema line.

### Canonical authored file extension
`.usina.yaml`

This is the preferred extension for authored documents.

---

## 2) Why `.usina.yaml` is canonical

The canonical extension should:
- preserve YAML tool compatibility
- communicate format identity clearly
- avoid collisions with unrelated file formats
- remain readable and unsurprising to users and tooling

`.usina.yaml` satisfies those goals better than a short opaque extension.

---

## 3) Recommended examples

Preferred filenames:
- `episode_001.usina.yaml`
- `air_gen_explainer.usina.yaml`
- `faceless_short_profile.usina.yaml`
- `research_episode_v2.usina.yaml`

Avoid ambiguous names when possible, such as:
- `episode.yaml`
- `video.yml`
- `script.yaml`

Those names hide the format identity.

---

## 4) Naming guidance for documentation

When referring to the standard:
- prefer **USINA Media Script**
- use **USINA-YAML** when referring to the repository/project brand
- use `usina.script/v1.0` when referring to schema identity
- use `.usina.yaml` when referring to the canonical document extension

---

## 5) Future artifact naming family

Potential future companion artifacts may include:

- `.usina.yaml` — canonical authoring format
- `.usina.lock` — reproducibility / integrity lockfile
- `.usina.bundle` — packaged portable bundle
- `.usina.report.json` — validation / audit output

This naming family keeps the ecosystem coherent while distinguishing authored source from derived artifacts.

---

## 6) Backward wording compatibility

Existing repository history may still refer to the project as “USINA-YAML v1.0” in older material. As docs are updated, the preferred wording should move toward:

- **USINA Media Script** for the standard
- **USINA-YAML** for the repository/project brand

---

## 7) Naming principles

The naming strategy should preserve these principles:

1. readability
2. explicit identity
3. low ambiguity
4. compatibility with YAML tooling
5. room for future artifact types
6. separation between public standard name and repository brand

---

## 8) Decision status

These naming decisions are currently treated as the official direction of the project and should be used consistently across new documentation, examples, and roadmap execution work.
