from __future__ import annotations

import argparse
import json
import os
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import List

try:
    import requests
except ImportError:  # pragma: no cover
    requests = None


DEFAULT_RULE_FILE = "validate-markdown.agent.md"


def find_markdown_files(root: Path) -> List[Path]:
    if not root.exists():
        raise FileNotFoundError(f"Root folder not found: {root}")
    return sorted(p for p in root.rglob("*.md") if p.is_file())


def load_instruction(rule_path: Path) -> str:
    if not rule_path.exists():
        raise FileNotFoundError(f"Validation instruction file not found: {rule_path}")
    return rule_path.read_text(encoding="utf-8")


def build_prompt(file_path: Path, file_contents: str, instruction_text: str) -> str:
    return f"""You are validating a Markdown file.

Use the rule set below exactly.

RULES:
{instruction_text}

FILE PATH:
{file_path}

FILE CONTENTS:
{file_contents}

Return a concise validation report with:
1. PASS or FAIL
2. issues found
3. recommended fixes
"""


def call_openai(prompt: str, model: str) -> str:
    if requests is None:
        raise RuntimeError("The 'requests' package is required for API mode. Install it with: pip install requests")

    api_key = os.getenv("OPENAI_API_KEY")
    if not api_key:
        raise RuntimeError("OPENAI_API_KEY is not set. Configure an API key or use --dry-run.")

    base_url = os.getenv("OPENAI_BASE_URL", "https://api.openai.com/v1")
    url = f"{base_url.rstrip('/')}/chat/completions"

    payload = {
        "model": model,
        "messages": [
            {"role": "system", "content": "You validate Markdown documentation according to the provided rules."},
            {"role": "user", "content": prompt},
        ],
        "temperature": 0.2,
    }

    response = requests.post(
        url,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json",
        },
        json=payload,
        timeout=60,
    )

    if response.status_code != 200:
        raise RuntimeError(
            f"OpenAI API call failed: {response.status_code} {response.text[:500]}"
        )

    data = response.json()
    return data["choices"][0]["message"]["content"].strip()


def validate_file(file_path: Path, instruction_text: str, model: str, dry_run: bool = False) -> str:
    file_contents = file_path.read_text(encoding="utf-8")
    prompt = build_prompt(file_path, file_contents, instruction_text)

    if dry_run:
        return (
            "SKIPPED (dry-run mode)\n"
            "Reason: AI validation was not executed. Set OPENAI_API_KEY and run without --dry-run to send the prompt."
        )

    return call_openai(prompt, model=model)


def write_summary(output_path: Path, root: Path, files: List[Path], results: List[dict]) -> None:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    lines = [
        "# Markdown Validation Results",
        "",
        f"Generated: {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S %Z')}",
        f"Root: `{root}`",
        f"Files scanned: {len(files)}",
        "",
        "| File | Result |",
        "| --- | --- |",
    ]

    for item in results:
        lines.append(f"| {item['file']} | {item['result']} |")

    lines.extend(["", "## Details", ""])
    for item in results:
        lines.append(f"### {item['file']}")
        lines.append(item["details"])
        lines.append("")

    output_path.write_text("\n".join(lines), encoding="utf-8")


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate Markdown files using a supplied AI instruction file.")
    parser.add_argument("--root", type=Path, default=Path("work"), help="Root folder containing Markdown files.")
    parser.add_argument(
        "--instruction",
        type=Path,
        default=None,
        help="Path to the validation instruction file. Defaults to work/module15-task/validate-markdown.agent.md if present.",
    )
    parser.add_argument("--output", type=Path, default=None, help="Output file for the validation report.")
    parser.add_argument("--model", default=os.getenv("OPENAI_MODEL", "gpt-4o-mini"), help="OpenAI-compatible model name.")
    parser.add_argument("--dry-run", action="store_true", help="List files and skip AI API calls.")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    repo_root = Path(__file__).resolve().parents[2]
    root = (repo_root / args.root).resolve() if not args.root.is_absolute() else args.root

    if args.instruction is None:
        candidate = root / "module15-task" / DEFAULT_RULE_FILE
        if not candidate.exists():
            candidate = root / DEFAULT_RULE_FILE
        instruction_path = candidate
    else:
        instruction_path = args.instruction if args.instruction.is_absolute() else (repo_root / args.instruction)

    files = find_markdown_files(root)
    instruction_text = load_instruction(instruction_path)

    output_path = args.output
    if output_path is None:
        output_path = root / "module15-task" / "markdown-validation-results.md"
    else:
        output_path = output_path if output_path.is_absolute() else (repo_root / output_path)

    results = []
    for file_path in files:
        try:
            result_text = validate_file(file_path, instruction_text, model=args.model, dry_run=args.dry_run)
            results.append({
                "file": str(file_path.relative_to(repo_root)),
                "result": "SKIPPED" if args.dry_run else "VALIDATED",
                "details": result_text,
            })
        except Exception as exc:  # pragma: no cover
            results.append({
                "file": str(file_path.relative_to(repo_root)),
                "result": "ERROR",
                "details": f"Error validating file: {exc}",
            })

    write_summary(output_path, root, files, results)

    print(f"Validated {len(files)} Markdown file(s). Report saved to: {output_path}")
    for item in results:
        print(f"- {item['file']}: {item['result']}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
