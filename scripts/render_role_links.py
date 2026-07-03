#!/usr/bin/env python3
"""Render each competency's OCF reference in roles/<slug>/ladder.md as a compact table.

Every `*OCF:*` reference becomes a markdown table with all hyperlinks intact:

    | OCF | E1 | E2 | E3 | E4 | E5 | E6 |
    |---|---|---|---|---|---|---|
    | [FE-01](../../data/capabilities.md#fe-01) | [P1](../../data/proficiency_scale.md#p1) | ... |

Level header codes come from the role's own levels (role.yaml); the P cells are the
competency's per-level proficiency targets, each linked to data/proficiency_scale.md.
Catalog ids link into data/capabilities.md#<id-lowercase>; proposed capabilities link
to their contrib proposal file instead.

No other prose is altered. Idempotent across formats: it converts both the raw
`*OCF:* <ID> ...` reference lines and the older inline-link format, and leaves
already-tabled blocks unchanged, so re-runs are safe.
Run with:  uv run --with pyyaml python scripts/render_role_links.py
"""

import os
import re
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
def _discover_roles():
    _base = os.path.join(ROOT, "roles")
    return tuple(sorted(d for d in os.listdir(_base)
                        if os.path.isfile(os.path.join(_base, d, "role.yaml"))))

ROLES = _discover_roles()

MD_LINK = re.compile(r"\[([^\]]*)\]\([^)]*\)")
CAT_ID = re.compile(r"^([A-Z]+-\d+)\s*(?:—\s*(.*?))?\s*$")


def parse_ref(rest, comp):
    """Parse the text after '*OCF:*' (raw or inline-linked form), validated
    against the role.yaml competency. Returns (name, candidate_id)."""
    seg = rest.split("· targets:")[0]
    seg = MD_LINK.sub(r"\1", seg).strip().rstrip(".").strip()
    if comp.get("capability") != "proposed":
        cid = comp["capability"]
        if not re.search(rf"\b{re.escape(cid)}\b", rest):
            raise SystemExit(f"OCF line/role.yaml mismatch: {rest!r} vs {cid}")
        m = CAT_ID.match(seg)
        name = m.group(2) if m else None
        return (name or None), None
    want = os.path.basename(comp["proposal_ref"])
    if want not in rest:
        raise SystemExit(f"proposed OCF line/role.yaml mismatch: {rest!r} vs {want}")
    cm = re.search(r"([A-Z]+-\d+)", seg)
    return None, (cm.group(1) if cm else None)


def table_block(comp, level_codes, name, candidate):
    if comp.get("capability") == "proposed":
        fname = os.path.basename(comp["proposal_ref"])
        cell = f"[proposed](../../contrib/{fname})"
        if candidate:
            cell += f" ({candidate} candidate)"
    else:
        cid = comp["capability"]
        cell = f"[{cid}](../../data/capabilities.md#{cid.lower()})"
        if name:
            cell += f" — {name}"
    plinks = []
    for code in level_codes:
        p = comp["proficiency"][code]
        plinks.append(f"[{p}](../../data/proficiency_scale.md#{p.lower()})")
    return [
        "| OCF | " + " | ".join(level_codes) + " |",
        "|" + "---|" * (len(level_codes) + 1),
        "| " + cell + " | " + " | ".join(plinks) + " |",
    ]


def block_matches(comp, data_row):
    """Sanity-check an existing table's data row against the competency."""
    if comp.get("capability") == "proposed":
        return os.path.basename(comp["proposal_ref"]) in data_row
    return re.search(rf"\b{re.escape(comp['capability'])}\b", data_row) is not None


def process(slug):
    role_dir = os.path.join(ROOT, "roles", slug)
    with open(os.path.join(role_dir, "role.yaml"), encoding="utf-8") as f:
        role = yaml.safe_load(f)
    comps = role["competencies"]
    level_codes = [lv["code"] for lv in role["levels"]]

    path = os.path.join(role_dir, "ladder.md")
    with open(path, encoding="utf-8") as f:
        lines = f.read().split("\n")

    out, idx, converted = [], 0, 0
    i = 0
    while i < len(lines):
        line = lines[i]
        if line.startswith("| OCF |"):  # already a table — leave unchanged
            if idx >= len(comps):
                raise SystemExit(f"{slug}: more OCF references than role.yaml competencies")
            if i + 2 >= len(lines) or not block_matches(comps[idx], lines[i + 2]):
                raise SystemExit(f"{slug}: table at line {i + 1} does not match "
                                 f"competency '{comps[idx]['theme']}'")
            out.extend(lines[i:i + 3])
            i += 3
            idx += 1
            continue
        if "*OCF:*" in line:
            if idx >= len(comps):
                raise SystemExit(f"{slug}: more OCF references than role.yaml competencies")
            comp = comps[idx]
            prefix, rest = line.split("*OCF:*", 1)
            name, candidate = parse_ref(rest, comp)
            if prefix.strip():
                out.append(prefix.rstrip())
            out.append("")
            out.extend(table_block(comp, level_codes, name, candidate))
            i += 1
            idx += 1
            converted += 1
            continue
        out.append(line)
        i += 1
    if idx != len(comps):
        raise SystemExit(f"{slug}: {idx} OCF references but {len(comps)} competencies")

    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write("\n".join(out))
    print(f"{slug}: {converted} OCF reference(s) converted to tables ({idx} total)")


def main():
    for slug in ROLES:
        process(slug)


if __name__ == "__main__":
    sys.exit(main())
