# USINA-YAML v1.0 — Tool-Agnostic Video Script Standard (YAML 1.2)

**Schema ID:** `usina.script/v1.0`  
**Status:** v1.0 (stable)  
**Scope:** Short-form video production scripts (also works for long-form), with explicit **assets**, **sources**, **prompts**, and a deterministic **timeline**.

USINA-YAML is designed as a **single source of truth** for a video episode: creative intent + technical constraints + citations + rights metadata + a time-accurate scene timeline that can drive editors, renderers, and AI-assisted pipelines.

---

## Why this exists

Most “video scripts” are either:
- human-friendly but machine-hostile (Google Docs), or
- machine-friendly but human-hostile (NLE project files).

USINA-YAML sits in the middle: **human readable**, **version controllable**, and **lintable**.


1) **Schema validation** (structure/types) using `schema/usina.script.v1.0.schema.json`  
2) **Lint rules** (math + references), e.g.:
- timeline ordered
- no overlap
- first scene starts at 0
- last scene ends exactly at `meta.duration_s`
- every `asset_id` exists
- shot durations sum (≈) scene duration (within tolerance)

> JSON Schema alone can’t reliably enforce “no overlap” and “timeline ends exactly at duration” — that’s why lint exists.

---

## Complete example (includes background audio)

Save this as `examples/air_gen_60s.yml`.

- Includes **background music** (audio bed)
- Includes **SFX** assets (whooshes/clicks)
- Demonstrates a scene-level `audio_tracks` array (portable, tool-agnostic)
- Keeps everything traceable, licensed, and creditable


---

## Licensing: “free for research/personal use, NOT for corporate/commercial/profit”


---

## Citation philosophy

USINA-YAML strongly encourages:
- conservative claims,
- explicit `sources[]`,
- `citations` attached to script blocks containing factual statements.

This makes automated fact-checking and audit trails possible.

---

## Contact / Commercial licensing

If you want commercial rights, enterprise usage, or monetized productions based on the standard, contact the author listed in `meta.authors` (or provide a public email in `meta.contact`).

---

