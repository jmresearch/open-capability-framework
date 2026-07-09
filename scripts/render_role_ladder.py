#!/usr/bin/env python3
"""Render roles/<slug>/ladder.md and ladder.csv from role.yaml + the sourced catalog.

Cells are ASSEMBLED, never authored (see docs/superpowers/specs/
2026-07-09-sourced-derivation-methodology-design.md):
  Depth  = the catalog capability's profile text at the mapped proficiency, verbatim.
  Evidenced by = optional role-specific instance of the bar (role.yaml `evidence`).
  Scope  = the role level's scope band.

Only roles with `derived: true` in role.yaml are rendered (--force overrides,
used by tests and the staleness check). Roles with `proposed` capabilities are
refused: accept the proposal into the catalog first.

Run with:  uv run --with pyyaml python scripts/render_role_ladder.py [--force] [slug ...]
"""

import argparse
import csv
import os
import sys

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
CATALOG_MD = "../../data/capabilities.md"
SCALE_MD = "../../data/proficiency_scale.md"


def _read_csv(name):
    with open(os.path.join(DATA, name), encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def load_catalog():
    scale = _read_csv("proficiency_scale.csv")
    p_col = {r["level"].strip(): f"{r['level'].strip()}_{r['name'].strip().lower()}"
             for r in scale}
    caps = {r["id"].strip(): r for r in _read_csv("capabilities.csv")}
    bib = {r["key"].strip(): r for r in _read_csv("bibliography.csv")}
    return caps, p_col, bib


def assemble_cell(bar, evidence, scope):
    parts = [f"Depth: {bar}"]
    if evidence:
        parts.append(f"Evidenced by: {evidence}")
    parts.append(f"Scope: {scope}.")
    return " ".join(parts)


def _cite(bib, key):
    return bib[key]["citation"] if key in bib else key  # legacy free-text anchors render as-is


def render_role(slug, force=False, out_dir=None):
    role_dir = os.path.join(ROOT, "roles", slug)
    with open(os.path.join(role_dir, "role.yaml"), encoding="utf-8") as f:
        role = yaml.safe_load(f)
    if not role.get("derived") and not force:
        print(f"skip roles/{slug}: not marked derived: true")
        return False
    caps, p_col, bib = load_catalog()
    for c in role["competencies"]:
        cap = str(c.get("capability", "")).strip()
        if cap == "proposed" or cap not in caps:
            sys.exit(f"roles/{slug}: '{c.get('theme')}' capability '{cap}' is not an "
                     f"accepted catalog id — accept the proposal before deriving")

    codes = [lv["code"] for lv in role["levels"]]
    scope_by_code = {lv["code"]: lv["scope"] for lv in role["levels"]}
    used_keys = []

    def use(key):
        if key in bib and key not in used_keys:
            used_keys.append(key)

    # ---------------------------------------------------------------- csv --
    rows = [["type", "key_area", "key_attribute", "theme", "capability"] + codes]
    rows.append(["meta_name", role.get("ladder_name", role["role"])] + [""] * (3 + len(codes)))
    desc = role.get("ladder_description", "")
    if desc:
        rows.append(["meta_description", desc] + [""] * (3 + len(codes)))
    rows.append(["level_title", "", "", "", ""] + [lv["title"] for lv in role["levels"]])
    rows.append(["level_scope", "", "", "", ""] + [lv["scope"] for lv in role["levels"]])
    rows.append(["level_focus", "", "", "", ""] + [lv["focus"] for lv in role["levels"]])

    # ----------------------------------------------------------------- md --
    md = [f"# {role.get('ladder_name', role['role'])} — Career Ladder", ""]
    if desc:
        md += [desc, ""]
    md += ["| Level | Title | Scope | Focus |", "|---|---|---|---|"]
    md += [f"| {lv['code']} | {lv['title']} | {lv['scope']} | {lv['focus']} |"
           for lv in role["levels"]]
    md.append("")

    key_area = key_attr = None
    for c in role["competencies"]:
        cap_id = c["capability"].strip()
        cap_row = caps[cap_id]
        if c["key_area"] != key_area:
            key_area, key_attr = c["key_area"], None
            md += [f"## {key_area}", ""]
        if c["key_attribute"] != key_attr:
            key_attr = c["key_attribute"]
            md += [f"#### {key_attr}", ""]
        md += [f"##### {c['theme']}", ""]
        anchor_key = str(c.get("anchor", "")).strip()
        use(anchor_key)
        anchor_line = f"*Anchor:* {_cite(bib, anchor_key)}"
        if c.get("anchor_why"):
            anchor_line += f" — {c['anchor_why']}"
        md += [anchor_line, ""]

        header = f"| OCF | {' | '.join(codes)} |"
        sep = "|" + "---|" * (len(codes) + 1)
        p_cells = []
        for code in codes:
            p = c["mappings"][code]["p"]
            p_cells.append(f"[{p}]({SCALE_MD}#{p.lower()})")
        md += [header, sep,
               f"| [{cap_id}]({CATALOG_MD}#{cap_id.lower()}) — {cap_row['capability']} | "
               + " | ".join(p_cells) + " |", ""]

        cells = []
        for code in codes:
            mp = c["mappings"][code]
            bar = cap_row[p_col[mp["p"]]].strip()
            evidence = (c.get("evidence") or {}).get(code, "").strip()
            scope = scope_by_code[code]
            cells.append(assemble_cell(bar, evidence, scope))
            for k in mp.get("sources", []):
                use(k)
            srcs = "; ".join(_cite(bib, k) for k in mp.get("sources", []))
            bullet = f"- **{code} (= {mp['p']})** — {bar}"
            if evidence:
                bullet += f" *Evidenced by:* {evidence}"
            bullet += f" *Scope:* {scope}."
            if mp.get("why"):
                bullet += f" *Why this level:* {mp['why']}"
                if srcs:
                    bullet += f" ({srcs})"
            md.append(bullet)
        md.append("")
        rows.append(["skill", c["key_area"], c["key_attribute"], c["theme"], cap_id] + cells)

    md += ["## Sources", ""]
    md += [f"- {bib[k]['citation']}" + (f" — {bib[k]['link']}" if bib[k]["link"].strip() else "")
           for k in used_keys]
    md.append("")

    out_dir = out_dir or role_dir
    with open(os.path.join(out_dir, "ladder.csv"), "w", encoding="utf-8", newline="") as f:
        csv.writer(f).writerows(rows)
    with open(os.path.join(out_dir, "ladder.md"), "w", encoding="utf-8", newline="\n") as f:
        f.write("\n".join(md))
    print(f"rendered roles/{slug}/ladder.md + ladder.csv")
    return True


def main():
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[0])
    ap.add_argument("slugs", nargs="*")
    ap.add_argument("--force", action="store_true")
    ap.add_argument("--out-dir", help="write outputs here instead of the role dir")
    args = ap.parse_args()
    roles_dir = os.path.join(ROOT, "roles")
    slugs = args.slugs or sorted(
        d for d in os.listdir(roles_dir)
        if os.path.isfile(os.path.join(roles_dir, d, "role.yaml")))
    for slug in slugs:
        render_role(slug, force=args.force, out_dir=args.out_dir)


if __name__ == "__main__":
    main()
