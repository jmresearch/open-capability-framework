#!/usr/bin/env python3
"""Validate a career-ladder CSV against the skill-matrix import contract.

Usage:
    python validate_csv.py <ladder.csv> [--manager] [--allow-single-theme]

Exit code 0 = importable; 1 = hard errors (listed). Warnings never fail the run.
Pure stdlib. Contract: see references/skillmatrix-csv.md.
"""

import argparse
import csv
import re
import sys

THEME_CAP = 60
MAX_LEVELS = 7
POSITION_LOCKED = ("manages managers", "through their managers", "reporting line")


def validate(path: str, manager: bool = False, allow_single_theme: bool = False):
    errors, warnings = [], []
    with open(path, encoding="utf-8-sig", newline="") as f:
        rows = list(csv.reader(f))
    if not rows:
        return ["file is empty"], []

    header = rows[0]
    if [c.strip() for c in header[:4]] != ["type", "key_area", "key_attribute", "theme"]:
        errors.append(f"header must start with type,key_area,key_attribute,theme — got {header[:4]}")
    # Optional 5th column: OCF `capability` reference (framework role records carry it;
    # the skill-matrix importer does not — strip it before import). Auto-detected.
    has_capability = len(header) > 4 and header[4].strip() == "capability"
    first_level = 5 if has_capability else 4
    levels = [c.strip() for c in header[first_level:]]
    if not 1 <= len(levels) <= MAX_LEVELS:
        errors.append(f"{len(levels)} level columns — the importer accepts 1-{MAX_LEVELS}")
    if len(set(levels)) != len(levels):
        errors.append(f"level headers must be unique: {levels}")
    if any(not lv for lv in levels):
        errors.append("empty level header")
    width = len(header)

    by_type = {}
    for i, row in enumerate(rows[1:], start=2):
        if not row or not any(c.strip() for c in row):
            continue
        by_type.setdefault(row[0].strip(), []).append((i, row))
        if len(row) > width:
            errors.append(f"row {i}: {len(row)} cells but header has {width} — cells beyond the level count")

    metas = by_type.get("meta_name", [])
    if len(metas) != 1:
        errors.append(f"need exactly one meta_name row, found {len(metas)}")
    elif len(metas[0][1]) < 2 or not metas[0][1][1].strip():
        errors.append("meta_name row has no name in the key_area cell")
    elif len(metas[0][1][1]) > 100:
        errors.append(f"meta_name is {len(metas[0][1][1])} chars (max 100)")
    if len(by_type.get("meta_description", [])) > 1:
        errors.append("more than one meta_description row")

    titles = by_type.get("level_title", [])
    if len(titles) != 1:
        errors.append(f"need exactly one level_title row, found {len(titles)}")
    else:
        vals = (titles[0][1][first_level:] + [""] * len(levels))[: len(levels)]
        if any(not v.strip() for v in vals):
            errors.append("level_title must have a non-empty title in every level column")
    for opt in ("level_scope", "level_focus"):
        if len(by_type.get(opt, [])) > 1:
            errors.append(f"more than one {opt} row")

    known = {"meta_name", "meta_description", "level_title", "level_scope", "level_focus", "skill"}
    for t in by_type:
        if t not in known:
            warnings.append(f"unknown row type '{t}' ({len(by_type[t])} rows) — the importer will reject it")

    skills = by_type.get("skill", [])
    if not skills:
        errors.append("no skill rows — need at least one")
    triples, foci = {}, {}
    for i, row in skills:
        area, focus, theme = (row[1].strip(), row[2].strip(), row[3].strip()) if len(row) >= 4 else ("", "", "")
        if not (area and focus and theme):
            errors.append(f"row {i}: skill row missing key_area/key_attribute/theme")
            continue
        if len(theme) > THEME_CAP:
            errors.append(f"row {i}: theme is {len(theme)} chars (cap {THEME_CAP}; overflow aborts the import) — '{theme[:50]}…'")
        key = (area, focus, theme)
        if key in triples:
            errors.append(f"row {i}: duplicate triple {key} (first at row {triples[key]})")
        triples[key] = i
        foci.setdefault((area, focus), set()).add(theme)
        if has_capability and (len(row) < 5 or not row[4].strip()):
            errors.append(f"row {i} ('{theme}'): capability column present but empty on a skill row")
        cells = (row[first_level:] + [""] * len(levels))[: len(levels)]
        empty = [levels[j] for j, c in enumerate(cells) if not c.strip()]
        if empty:
            warnings.append(f"row {i} ('{theme}'): empty cell(s) at {','.join(empty)} (allowed, but a complete ladder fills them)")
        joined = " ".join(cells).lower()
        if "anchor:" in joined:
            errors.append(f"row {i} ('{theme}'): theory-anchor text in a level cell — anchors are markdown-only")
        if manager:
            # Contract: assembled cells (scripts/render_role_ladder.py assemble_cell) look like
            # "Depth: {verbatim catalog bar}\n\nEvidenced by: {role evidence}" — no trailing Scope
            # clause (level_scope carries that; see the module docstring). Older renders appended
            # "\n\nScope: {scope}." or " Scope: {scope}." (single-space join); the regex below still
            # stops at either legacy separator as well as end-of-string, so old cells keep parsing.
            # The bar segment is role-agnostic catalog canon and may legitimately contain
            # position-locked substrings (e.g. BIZ-02 P1_assisted has "reporting lines") — it is
            # not role-authored, so it is exempt. Only the "Evidenced by:" clause is role-authored
            # and must stay demonstrable pre-seat, so for assembled cells we scan just that clause.
            # Non-assembled (legacy, fully-authored) cells are scanned in full, unchanged.
            manager_texts = []
            for cell in cells:
                stripped = cell.strip()
                if stripped.startswith("Depth: "):
                    m = re.search(r"Evidenced by: (.*?)(?: Scope: |\n\nScope: |$)", stripped, re.S)
                    manager_texts.append(m.group(1) if m else "")
                else:
                    manager_texts.append(cell)
            manager_joined = " ".join(manager_texts).lower()
            for phrase in POSITION_LOCKED:
                if phrase in manager_joined:
                    errors.append(f"row {i} ('{theme}'): position-locked phrase '{phrase}' — write demonstrable influence behaviors")

    singles = [f"{a} > {f}" for (a, f), themes in foci.items() if len(themes) == 1]
    if singles:
        msg = f"focus areas with only one competency (1:1 mapping): {'; '.join(singles)}"
        (warnings if allow_single_theme else errors).append(msg + ("" if allow_single_theme else " — re-cut or pass --allow-single-theme if the source truly has no sibling"))

    return errors, warnings


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("csv_path")
    ap.add_argument("--manager", action="store_true", help="also reject position-locked manager language")
    ap.add_argument("--allow-single-theme", action="store_true", help="downgrade 1:1 focus mappings to warnings")
    args = ap.parse_args()

    errors, warnings = validate(args.csv_path, args.manager, args.allow_single_theme)
    for w in warnings:
        print(f"WARN  {w}")
    for e in errors:
        print(f"ERROR {e}")
    if errors:
        print(f"\nFAIL — {len(errors)} error(s), {len(warnings)} warning(s): this file will not import cleanly")
        sys.exit(1)
    print(f"OK — importable ({len(warnings)} warning(s))")


if __name__ == "__main__":
    main()
