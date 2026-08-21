#!/usr/bin/env python3
"""Scaffold a Decision System Spec markdown file."""

from __future__ import annotations

import argparse
from pathlib import Path


TEMPLATE = """# Decision System Spec

## Goal
{goal}

## Context Files
{context_files}

## 1. Decision
- Business question:
- Current decision owner:
- Desired system role:

## 2. Objects
| Object | Meaning | Key properties | States |
|---|---|---|---|
| | | | |

## 3. Signals
| Signal | Source | Why it matters | Reliability |
|---|---|---|---|
| | | | |

## 4. Actions
| Action | Target object | Outcome | Execution class |
|---|---|---|---|
| | | | auto/recommend/review/forbidden |

## 5. Permissions and Review
- Human approval points:
- Forbidden actions:
- Logging requirements:
- Escalation triggers:

## 6. Workflow
1. Observe:
2. Interpret:
3. Decide:
4. Act or recommend:
5. Review:
6. Learn:

## 7. Failure Cases
- Failure mode 1:
- Failure mode 2:
- Failure mode 3:

## 8. Evaluation Plan
- Success metrics:
- Guardrail metrics:
- Test cases:
- Human review criteria:

## 9. Missing Data
- Gap:
- Impact:
- How to close it:

## 10. MVP Build Plan
- First decision to implement:
- First data sources:
- First actions:
- First human review flow:
- First delivery milestone:
"""


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Create a Decision System Spec markdown scaffold."
    )
    parser.add_argument("--goal", required=True, help="Business goal or decision")
    parser.add_argument(
        "--context-file",
        action="append",
        default=[],
        help="Local file relevant to the decision system",
    )
    parser.add_argument("--output", required=True, help="Path to write the markdown file")
    return parser


def format_context_files(context_files: list[str]) -> str:
    if not context_files:
        return "- None supplied"
    return "\n".join(f"- {item}" for item in context_files)


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()

    output_path = Path(args.output)
    output_path.parent.mkdir(parents=True, exist_ok=True)
    content = TEMPLATE.format(
        goal=args.goal.strip(),
        context_files=format_context_files(args.context_file),
    )
    output_path.write_text(content, encoding="utf-8")
    print(output_path)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
