from __future__ import annotations

import json
import re
from dataclasses import dataclass
from importlib import resources
from pathlib import Path
from typing import Any

import yaml
from jsonschema import Draft202012Validator

ID_RE = re.compile(r"^[a-z][a-z0-9_]{1,63}$")


@dataclass
class Problem:
    code: str
    level: str
    message: str
    path: str = ""


def load_yaml(path: str | Path) -> dict[str, Any]:
    with open(path, "r", encoding="utf-8") as f:
        data = yaml.safe_load(f)
    if not isinstance(data, dict):
        raise ValueError("USINA document root must be a mapping/object.")
    return data


def load_schema() -> dict[str, Any]:
    text = resources.files("usina.schemas").joinpath("usina.script.v1.0.schema.json").read_text(encoding="utf-8")
    return json.loads(text)


def validate_schema(doc: dict[str, Any]) -> list[Problem]:
    validator = Draft202012Validator(load_schema())
    problems: list[Problem] = []
    for err in sorted(validator.iter_errors(doc), key=lambda e: list(e.absolute_path)):
        path = "/".join(map(str, err.absolute_path))
        problems.append(Problem("USINA-SCHEMA-001", "error", err.message, path))
    return problems


def _id_problems(namespace: str, ids: list[tuple[str, str]]) -> list[Problem]:
    probs: list[Problem] = []
    seen: set[str] = set()
    for ident, path in ids:
        if not isinstance(ident, str) or not ID_RE.fullmatch(ident):
            probs.append(Problem("USINA-LINT-007", "error", f"Invalid ID in {namespace}: {ident!r}", path))
        if ident in seen:
            probs.append(Problem("USINA-LINT-008", "error", f"Duplicate ID in {namespace}: {ident!r}", path))
        seen.add(ident)
    return probs


def lint(doc: dict[str, Any]) -> list[Problem]:
    probs: list[Problem] = []
    tol = float(doc.get("qa", {}).get("lint", {}).get("tolerance_s", 0.05) or 0.05)
    timeline = doc.get("timeline", []) or []
    assets = {a.get("id"): a for a in doc.get("assets", []) if isinstance(a, dict)}
    asset_ids = set(assets)
    audio_asset_ids = {k for k, v in assets.items() if isinstance(v, dict) and v.get("type") == "audio"}
    prompt_ids = {p.get("id") for p in doc.get("prompts", []) if isinstance(p, dict)}
    source_ids = {s.get("id") for s in doc.get("sources", []) if isinstance(s, dict)}
    vo_blocks = doc.get("script", {}).get("vo", {}).get("blocks", []) or []
    vo_ids = {b.get("id") for b in vo_blocks if isinstance(b, dict)}

    probs.extend(_id_problems("assets", [(a.get("id"), f"assets/{i}/id") for i, a in enumerate(doc.get("assets", [])) if isinstance(a, dict)]))
    probs.extend(_id_problems("prompts", [(p.get("id"), f"prompts/{i}/id") for i, p in enumerate(doc.get("prompts", [])) if isinstance(p, dict)]))
    probs.extend(_id_problems("sources", [(s.get("id"), f"sources/{i}/id") for i, s in enumerate(doc.get("sources", [])) if isinstance(s, dict)]))
    probs.extend(_id_problems("timeline", [(s.get("id"), f"timeline/{i}/id") for i, s in enumerate(timeline) if isinstance(s, dict)]))
    probs.extend(_id_problems("script.vo.blocks", [(b.get("id"), f"script/vo/blocks/{i}/id") for i, b in enumerate(vo_blocks) if isinstance(b, dict)]))

    if timeline:
        ordered = sorted(timeline, key=lambda s: s.get("start_s", 0))
        if ordered != timeline:
            probs.append(Problem("USINA-LINT-001", "error", "Timeline must be ordered by start_s ascending.", "timeline"))
        first = timeline[0]
        if first.get("start_s") != 0:
            probs.append(Problem("USINA-LINT-003", "error", "First scene start_s must equal 0.", "timeline/0/start_s"))
        last = timeline[-1]
        if float(last.get("end_s", -1)) != float(doc.get("meta", {}).get("duration_s", -2)):
            probs.append(Problem("USINA-LINT-004", "error", "Last scene end_s must equal meta.duration_s.", f"timeline/{len(timeline)-1}/end_s"))

        prev_end = None
        for i, scene in enumerate(timeline):
            start = scene.get("start_s")
            end = scene.get("end_s")
            if end <= start:
                probs.append(Problem("USINA-LINT-005", "error", "Each scene must have end_s > start_s.", f"timeline/{i}"))
            if prev_end is not None and start < prev_end:
                probs.append(Problem("USINA-LINT-002", "error", "Timeline scenes must not overlap.", f"timeline/{i}"))
            prev_end = end
            dur = end - start
            shot_sum = sum(float(sh.get("duration_s", 0)) for sh in scene.get("shots", []) if isinstance(sh, dict))
            if abs(shot_sum - dur) > tol:
                probs.append(Problem("USINA-LINT-006", "error", f"Scene shot durations sum to {shot_sum} but scene duration is {dur}.", f"timeline/{i}/shots"))
            vo = scene.get("vo")
            if isinstance(vo, dict) and "ref_id" in vo and vo.get("ref_id") not in vo_ids:
                probs.append(Problem("USINA-REF-009", "error", f"Unknown vo.ref_id {vo.get('ref_id')!r}.", f"timeline/{i}/vo/ref_id"))
            for j, shot in enumerate(scene.get("shots", [])):
                if not isinstance(shot, dict):
                    continue
                aid = shot.get("asset_id")
                if aid is not None and aid not in asset_ids:
                    probs.append(Problem("USINA-REF-008", "error", f"Unknown shot asset_id {aid!r}.", f"timeline/{i}/shots/{j}/asset_id"))
                gen = shot.get("generator")
                if isinstance(gen, dict) and "prompt_id" in gen and gen.get("prompt_id") not in prompt_ids:
                    probs.append(Problem("USINA-REF-010", "error", f"Unknown generator.prompt_id {gen.get('prompt_id')!r}.", f"timeline/{i}/shots/{j}/generator/prompt_id"))
            for j, track in enumerate(scene.get("audio_tracks", [])):
                if not isinstance(track, dict):
                    continue
                aid = track.get("asset_id")
                if aid not in audio_asset_ids:
                    probs.append(Problem("USINA-LINT-013", "error", f"audio_tracks asset_id must reference an audio asset, got {aid!r}.", f"timeline/{i}/audio_tracks/{j}/asset_id"))
                ts, te = track.get("start_s"), track.get("end_s")
                if te <= ts or ts < start or te > end:
                    probs.append(Problem("USINA-LINT-014", "error", "Scene-level audio_tracks must be within scene bounds and have end_s > start_s.", f"timeline/{i}/audio_tracks/{j}"))

    bed = doc.get("audio", {}).get("bed")
    if isinstance(bed, dict) and "asset_id" in bed and bed.get("asset_id") not in audio_asset_ids:
        probs.append(Problem("USINA-LINT-012", "error", f"audio.bed.asset_id must reference an audio asset, got {bed.get('asset_id')!r}.", "audio/bed/asset_id"))

    for i, block in enumerate(vo_blocks):
        if not isinstance(block, dict):
            continue
        for j, cit in enumerate(block.get("citations", []) or []):
            if cit not in source_ids:
                probs.append(Problem("USINA-REF-011", "error", f"Unknown citation {cit!r}.", f"script/vo/blocks/{i}/citations/{j}"))

    return probs


def summarize(problems: list[Problem]) -> str:
    if not problems:
        return "No problems found."
    lines = []
    for p in problems:
        loc = f" [{p.path}]" if p.path else ""
        lines.append(f"{p.level.upper()} {p.code}{loc}: {p.message}")
    return "\n".join(lines)
