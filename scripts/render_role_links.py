#!/usr/bin/env python3
"""Hyperlink the `*OCF:*` reference lines in roles/<slug>/ladder.md.

For each competency's OCF reference:
  - catalog ids become links into data/capabilities.md#<id-lowercase>, followed
    by a compact per-level proficiency-target line linked into
    data/proficiency_scale.md (targets come from role.yaml);
  - proposed capabilities link to their contrib proposal file instead.

No other prose is altered. Idempotent: already-linked lines (containing
"· targets:") are left untouched, so the script is safe to re-run.
Run with:  uv run --with pyyaml python scripts/render_role_links.py
"""

import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ROLES = ("engineering-management", "full-stack-typescript")

CAT_ID = re.compile(r"^([A-Z]+-\d+)\s*(—\s*(.*?))?\s*(\.)?\s*$")
CONTRIB = re.compile(r"contrib/([\w.\-]+\.md)")


def targets_str(comp, level_codes):
    parts = []
    for code in level_codes:
        p = comp["proficiency"][code]
        parts.append(f"{code}:[{p}](../../data/proficiency_scale.md#{p.lower()})")
    return " ".join(parts)


def render_ref(rest, comp, level_codes):
    """Rebuild the text after '*OCF:*' for one competency."""
    targets = targets_str(comp, level_codes)
    if comp.get("capability") != "proposed":
        m = CAT_ID.match(rest.strip())
        if not m or m.group(1) != comp["capability"]:
            raise SystemExit(f"OCF line/role.yaml mismatch: {rest!r} vs {comp['capability']}")
        cid = m.group(1)
        link = f"[{cid}](../../data/capabilities.md#{cid.lower()})"
        name = f" — {m.group(3)}" if m.group(3) else ""
        dot = m.group(4) or ""
        return f"{link}{name} · targets: {targets}{dot}"
    # proposed
    fm = CONTRIB.search(rest)
    want = os.path.basename(comp["proposal_ref"])
    if not fm or fm.group(1) != want:
        raise SystemExit(f"proposed OCF line/role.yaml mismatch: {rest!r} vs {want}")
    link = f"[proposed](../../contrib/{want})"
    cm = re.search(r"([A-Z]+-\d+)", rest)
    cand = f" ({cm.group(1)} candidate)" if cm else ""
    dot = "." if rest.rstrip().endswith(".") else ""
    return f"{link}{cand} · targets: {targets}{dot}"


def process(slug):
    role_dir = os.path.join(ROOT, "roles", slug)
    with open(os.path.join(role_dir, "role.yaml"), encoding="utf-8") as f:
        role = yaml.safe_load(f)
    comps = role["competencies"]
    level_codes = [lv["code"] for lv in role["levels"]]

    path = os.path.join(role_dir, "ladder.md")
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")

    idx = 0
    changed = 0
    for i, line in enumerate(lines):
        if "*OCF:*" not in line:
            continue
        if idx >= len(comps):
            raise SystemExit(f"{slug}: more *OCF:* lines than role.yaml competencies")
        comp = comps[idx]
        idx += 1
        if "· targets:" in line:  # already rendered
            continue
        prefix, rest = line.split("*OCF:*", 1)
        lines[i] = f"{prefix}*OCF:* {render_ref(rest, comp, level_codes)}"
        changed += 1
    if idx != len(comps):
        raise SystemExit(f"{slug}: {idx} *OCF:* lines but {len(comps)} competencies")

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(lines))
    print(f"{slug}: {changed} OCF reference(s) hyperlinked ({idx} total)")


def main():
    for slug in ROLES:
        process(slug)


if __name__ == "__main__":
    sys.exit(main())
