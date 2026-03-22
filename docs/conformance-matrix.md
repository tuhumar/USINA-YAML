# Conformance Matrix — USINA Media Script v1.0

This matrix maps core v1.0 expectations to the current reference implementation surface.

---

## Legend

- **Schema** — enforced by JSON Schema
- **Lint** — enforced by the reference semantic linter
- **Fixture** — covered by at least one valid or invalid fixture
- **Status** — current implementation state in the reference toolkit

---

| Requirement | Schema | Lint | Fixture | Status |
|---|---|---|---|---|
| `usina_schema` must equal `usina.script/v1.0` | Yes | No | Valid | Implemented |
| Required top-level sections must exist | Yes | No | Valid | Implemented |
| `meta.duration_s` must be > 0 | Yes | No | Valid | Implemented |
| Timeline must contain at least one scene | Yes | No | Valid | Implemented |
| Timeline must be ordered by `start_s` | No | Yes | Planned | Implemented |
| Timeline scenes must not overlap | No | Yes | Invalid (`timeline_overlap`) | Implemented |
| First scene must start at `0` | No | Yes | Planned | Implemented |
| Last scene must end at `meta.duration_s` | No | Yes | Planned | Implemented |
| Scene `end_s` must be greater than `start_s` | Partially | Yes | Planned | Implemented |
| Shot duration sum should match scene duration within tolerance | No | Yes | Valid | Implemented |
| `shot.asset_id` must reference an existing asset | No | Yes | Valid | Implemented |
| `vo.ref_id` must reference an existing VO block | No | Yes | Valid | Implemented |
| `generator.prompt_id` must reference an existing prompt | No | Yes | Planned | Implemented |
| `script.vo.blocks[*].citations[]` must reference existing sources | No | Yes | Valid | Implemented |
| `audio.bed.asset_id` must reference an audio asset | No | Yes | Valid | Implemented |
| `audio_tracks[*].asset_id` must reference an audio asset | No | Yes | Valid | Implemented |
| `audio_tracks` must stay within scene bounds | No | Yes | Valid | Implemented |
| Core IDs should follow a stable snake_case-like pattern | No | Yes | Valid | Implemented |
| Duplicate IDs should be rejected within major namespaces | No | Yes | Planned | Implemented |

---

## Current fixture set

### Valid
- `tests/fixtures/valid/minimal_valid.usina.yaml`

### Invalid
- `tests/fixtures/invalid/timeline_overlap.usina.yaml`

---

## Current reference commands

- `usina validate <file>`
- `usina lint <file>`
- `usina explain <file>`

---

## Next recommended expansions

1. add fixtures for out-of-order timelines
2. add fixtures for unknown asset references
3. add fixtures for invalid citation references
4. add fixtures for bad `audio_tracks` bounds
5. add JSON-formatted expected outputs for each fixture
6. split schema and lint error code registries into dedicated docs
