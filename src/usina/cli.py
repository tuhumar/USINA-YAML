from __future__ import annotations

import argparse
import json
import sys
from pathlib import Path

from .core import Problem, lint, load_yaml, summarize, validate_schema


def _emit_json(problems: list[Problem]) -> None:
    print(json.dumps([p.__dict__ for p in problems], indent=2))


def cmd_validate(args: argparse.Namespace) -> int:
    doc = load_yaml(args.file)
    problems = validate_schema(doc)
    if args.json:
        _emit_json(problems)
    else:
        print(summarize(problems))
    return 1 if problems else 0


def cmd_lint(args: argparse.Namespace) -> int:
    doc = load_yaml(args.file)
    problems = validate_schema(doc)
    if not problems:
        problems = lint(doc)
    if args.json:
        _emit_json(problems)
    else:
        print(summarize(problems))
    return 1 if problems else 0


def cmd_explain(args: argparse.Namespace) -> int:
    doc = load_yaml(args.file)
    schema_problems = validate_schema(doc)
    lint_problems = [] if schema_problems else lint(doc)
    payload = {
        "file": str(Path(args.file)),
        "schema_problem_count": len(schema_problems),
        "lint_problem_count": len(lint_problems),
        "schema_problems": [p.__dict__ for p in schema_problems],
        "lint_problems": [p.__dict__ for p in lint_problems],
    }
    print(json.dumps(payload, indent=2))
    return 1 if schema_problems or lint_problems else 0


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(prog="usina", description="Reference CLI for USINA Media Script")
    sub = parser.add_subparsers(dest="command", required=True)

    p_val = sub.add_parser("validate", help="Validate a .usina.yaml file against the JSON Schema")
    p_val.add_argument("file")
    p_val.add_argument("--json", action="store_true")
    p_val.set_defaults(func=cmd_validate)

    p_lint = sub.add_parser("lint", help="Run schema validation and semantic lint checks")
    p_lint.add_argument("file")
    p_lint.add_argument("--json", action="store_true")
    p_lint.set_defaults(func=cmd_lint)

    p_exp = sub.add_parser("explain", help="Emit a JSON explanation of schema/lint results")
    p_exp.add_argument("file")
    p_exp.set_defaults(func=cmd_explain)

    return parser


def main(argv: list[str] | None = None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    try:
        return args.func(args)
    except Exception as exc:  # pragma: no cover
        print(f"ERROR: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
