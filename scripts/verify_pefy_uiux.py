#!/usr/bin/env python3
"""Read-only, standard-library static packaging checks for the PEFY-GG adapter.

This does NOT execute third-party source, certify accessibility/security, or prove
any user/cloud installation. Use separately reviewed functional smoke tests later.
"""
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
REQUIRED = [
    "AGENTS.md",
    "PEFY-GG-INTEGRATION.md",
    ".agents/skills/ui-ux-pro-max/SKILL.md",
    ".claude/skills/ui-ux-pro-max/SKILL.md",
    "src/ui-ux-pro-max/scripts/search.py",
    "src/ui-ux-pro-max/data",
    "LICENSE",
]

def main() -> int:
    failed = []
    for name in REQUIRED:
        item = ROOT / name
        if not item.exists():
            failed.append(f"missing: {name}")
        elif item.is_file() and item.stat().st_size == 0:
            failed.append(f"empty: {name}")

    skill = ROOT / ".agents/skills/ui-ux-pro-max/SKILL.md"
    if skill.is_file():
        body = skill.read_text(encoding="utf-8")
        if not re.search(r"\A---\s*\nname:\s*ui-ux-pro-max\s*\n", body):
            failed.append("invalid or mismatched skill manifest")
        if "PEFY-GG-INTEGRATION.md" not in body:
            failed.append("governance linkage missing")

    guidance = ROOT / "PEFY-GG-INTEGRATION.md"
    if guidance.is_file():
        body = guidance.read_text(encoding="utf-8")
        for token in ("ui-ux-pro-max-cli", "WCAG 2.2", "ChatGPT", "Codex", "release"):
            if token not in body:
                failed.append(f"missing governance topic: {token}")

    if failed:
        for item in failed:
            print(f"FAIL: {item}", file=sys.stderr)
        return 1
    print("PASS: static adapter packaging and governance linkage.")
    print("LIMITATION: live Codex/ChatGPT installation, upstream parity and functional tests not checked.")
    return 0

if __name__ == "__main__":
    raise SystemExit(main())
