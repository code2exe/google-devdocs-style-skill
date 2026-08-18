#!/usr/bin/env python3
"""Validate the skill: frontmatter, link integrity, and size budget.

Run from the repository root:

    python3 scripts/validate.py

Exits non-zero on failure so it can gate CI.
"""

from __future__ import annotations

import re
import sys
from pathlib import Path

REPO = Path(__file__).resolve().parent.parent
SKILL_DIR = REPO / "skills" / "google-devdocs-style"
SKILL_MD = SKILL_DIR / "SKILL.md"

# SKILL.md loads on every trigger, so its size is a running cost, not a one-off.
MAX_SKILL_LINES = 250
MAX_REFERENCE_LINES = 500

failures: list[str] = []
warnings: list[str] = []


def fail(msg: str) -> None:
    failures.append(msg)


def warn(msg: str) -> None:
    warnings.append(msg)


def check_frontmatter() -> None:
    if not SKILL_MD.exists():
        fail(f"missing {SKILL_MD.relative_to(REPO)}")
        return

    text = SKILL_MD.read_text(encoding="utf-8")
    if not text.startswith("---\n"):
        fail("SKILL.md must open with YAML frontmatter delimited by ---")
        return

    end = text.find("\n---\n", 3)
    if end == -1:
        fail("SKILL.md frontmatter is not closed")
        return

    block = text[4:end]
    fields = dict(
        re.findall(r"^([A-Za-z_-]+):\s*(.*)$", block, flags=re.MULTILINE)
    )

    for required in ("name", "description"):
        if required not in fields or not fields[required].strip():
            fail(f"SKILL.md frontmatter missing required field: {required}")

    name = fields.get("name", "")
    if name and name != SKILL_DIR.name:
        fail(
            f"frontmatter name '{name}' must match directory "
            f"name '{SKILL_DIR.name}'"
        )
    if name and not re.fullmatch(r"[a-z0-9]+(-[a-z0-9]+)*", name):
        fail(f"frontmatter name '{name}' should be lowercase-hyphenated")

    desc = fields.get("description", "")
    if desc and len(desc) < 80:
        warn(
            "description is short; it is the only trigger signal Claude sees, "
            "so it should name both what the skill does and when to use it"
        )
    if desc and len(desc) > 1400:
        warn(f"description is {len(desc)} chars; consider trimming")


def check_links() -> None:
    """Every relative Markdown link inside the skill must resolve."""
    pattern = re.compile(r"\[[^\]]*\]\(([^)]+)\)")

    for md in sorted(SKILL_DIR.rglob("*.md")):
        for lineno, line in enumerate(
            md.read_text(encoding="utf-8").splitlines(), start=1
        ):
            for target in pattern.findall(line):
                if target.startswith(("http://", "https://", "#", "mailto:")):
                    continue
                path_part = target.split("#", 1)[0]
                if not path_part:
                    continue
                resolved = (md.parent / path_part).resolve()
                if not resolved.exists():
                    rel = md.relative_to(REPO)
                    fail(f"{rel}:{lineno} broken link -> {target}")


def check_sizes() -> None:
    if SKILL_MD.exists():
        n = len(SKILL_MD.read_text(encoding="utf-8").splitlines())
        if n > MAX_SKILL_LINES:
            fail(
                f"SKILL.md is {n} lines, over the {MAX_SKILL_LINES}-line budget. "
                "Move detail into references/ and link to it."
            )

    for md in sorted((SKILL_DIR / "references").glob("*.md")):
        n = len(md.read_text(encoding="utf-8").splitlines())
        if n > MAX_REFERENCE_LINES:
            warn(
                f"{md.relative_to(REPO)} is {n} lines; consider splitting "
                "or adding a table of contents"
            )


def check_attribution() -> None:
    """CC BY 4.0 requires attribution, a license link, and a changes notice."""
    for name in ("NOTICE", "LICENSE"):
        path = REPO / name
        if not path.exists():
            fail(f"missing {name}; CC BY 4.0 attribution must ship with the work")
            continue
        text = path.read_text(encoding="utf-8")
        if "creativecommons.org/licenses/by/4.0" not in text:
            fail(f"{name} must link to the CC BY 4.0 license")
        if name == "NOTICE" and "developers.google.com/style" not in text:
            fail("NOTICE must attribute the original source URL")

    for md in sorted((SKILL_DIR / "references").glob("*.md")):
        if "Provenance" not in md.read_text(encoding="utf-8"):
            warn(f"{md.relative_to(REPO)} has no provenance footer")


def main() -> int:
    if not SKILL_DIR.exists():
        print(f"FAIL  skill directory not found: {SKILL_DIR}")
        return 1

    check_frontmatter()
    check_links()
    check_sizes()
    check_attribution()

    for w in warnings:
        print(f"WARN  {w}")
    for f in failures:
        print(f"FAIL  {f}")

    if failures:
        print(f"\n{len(failures)} failure(s), {len(warnings)} warning(s)")
        return 1

    files = len(list(SKILL_DIR.rglob("*.md")))
    print(f"OK    {files} markdown files validated, {len(warnings)} warning(s)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
