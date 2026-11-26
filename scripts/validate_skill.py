#!/usr/bin/env python3
"""Minimal standard-library checks for the distributable Skill directory."""

from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]
SKILL = ROOT / "github-collaborator"
manifest = SKILL / "SKILL.md"

if not manifest.is_file():
    sys.exit("FAIL: github-collaborator/SKILL.md is missing")

content = manifest.read_text(encoding="utf-8")
match = re.match(r"\A---\s*\n(.*?)\n---\s*\n", content, re.S)
if not match:
    sys.exit("FAIL: YAML frontmatter is missing or malformed")

frontmatter = match.group(1)
name = re.search(r"^name:\s*([^\s#]+)\s*$", frontmatter, re.M)
description = re.search(r"^description:\s*(.+)$", frontmatter, re.M)
if not name or name.group(1) != "github-collaborator":
    sys.exit("FAIL: skill name must be github-collaborator")
if not description or len(description.group(1)) > 1024:
    sys.exit("FAIL: description is missing or exceeds 1024 characters")
if not re.fullmatch(r"[a-z0-9]+(?:-[a-z0-9]+)*", name.group(1)):
    sys.exit("FAIL: skill name does not follow Agent Skills naming rules")

links = re.findall(r"\]\((references/[^)#]+)", content)
missing = [link for link in links if not (SKILL / link).is_file()]
if missing:
    sys.exit("FAIL: missing referenced files: " + ", ".join(missing))

required = [
    "references/onboarding-and-awareness.md",
    "references/project-and-tasks.md",
    "references/work-and-delivery.md",
    "references/review.md",
    "references/sync-and-recovery.md",
    "references/security.md",
    "references/first-use.md",
    "references/human-interaction.md",
    "references/member-quickstart.md",
    "assets/templates/issue.md",
]
missing = [path for path in required if not (SKILL / path).is_file()]
if missing:
    sys.exit("FAIL: missing required resources: " + ", ".join(missing))

print(f"PASS: {manifest.relative_to(ROOT)}; metadata and {len(required)} resources verified")
