#!/usr/bin/env python3
"""One-shot role.yaml migration: flat `proficiency: {M1: P2, ...}` lines become
per-level `mappings:` blocks with empty sources/why, preserving every other
line (including comments) byte-for-byte. Idempotent.

Run with:  uv run --with pyyaml python scripts/migrate_role_yaml.py [slug ...]
"""

import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROF_RE = re.compile(r"^(\s*)proficiency:\s*\{(.*)\}\s*$")


def migrate_lines(lines):
    out = []
    for line in lines:
        m = PROF_RE.match(line)
        if not m:
            out.append(line)
            continue
        indent, body = m.group(1), m.group(2)
        out.append(f"{indent}mappings:\n")
        for pair in body.split(","):
            code, p = (s.strip() for s in pair.split(":", 1))
            out.append(f"{indent}  {code}: {{p: {p}, sources: [], why: \"\"}}\n")
    return out


def main(slugs):
    roles_dir = os.path.join(ROOT, "roles")
    slugs = slugs or sorted(
        d for d in os.listdir(roles_dir)
        if os.path.isfile(os.path.join(roles_dir, d, "role.yaml"))
    )
    for slug in slugs:
        path = os.path.join(roles_dir, slug, "role.yaml")
        with open(path, encoding="utf-8") as f:
            lines = f.readlines()
        migrated = migrate_lines(lines)
        if migrated != lines:
            with open(path, "w", encoding="utf-8", newline="") as f:
                f.writelines(migrated)
            print(f"migrated roles/{slug}/role.yaml")
        else:
            print(f"roles/{slug}/role.yaml already migrated")


if __name__ == "__main__":
    main(sys.argv[1:])
