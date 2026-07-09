#!/usr/bin/env python3
"""Deterministic consistency guards for the Open Capability Framework.

Run by CI on every PR and before every post-merge regeneration. No LLM, no
judgment — every check is mechanical:

  1. data/capabilities.csv: required fields present, ids unique.
  2. capabilities.csv and capabilities.json describe the same id set.
  3. data/domains.csv counts match the actual catalog contents.
  4. Every role.yaml competency references a real catalog id (or `proposed`
     with an existing proposal file under contrib/).
  5. Each role's ladder.csv `capability` column agrees with role.yaml.
  6. Each role's ladder.csv passes the ladder validator (--manager for
     manager-variant roles).

Exit 0 = consistent; exit 1 with a list of failures.
"""

import argparse
import csv
import json
import os
import subprocess
import sys
import collections

import yaml

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
VALIDATOR = os.path.join(ROOT, "skills", "career-ladder", "scripts", "validate_csv.py")
errors = []


def fail(msg):
    errors.append(msg)


P_LEVELS = ("P1", "P2", "P3", "P4", "P5", "P6")
ABOVE_BAR = ("sets the standard", "drives strategy", "org-wide", "other teams adopt")


def _read_data_csv(name):
    with open(os.path.join(ROOT, "data", name), encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def sourcing_issues():
    """Spec-mandated sourcing gaps: report-mode lines (strict mode fails on them)."""
    issues = []
    bib = {r["key"].strip() for r in _read_data_csv("bibliography.csv")}
    caps = [r["id"].strip() for r in _read_data_csv("capabilities.csv")]
    lvl_rows = {}
    for r in _read_data_csv("capability_levels.csv"):
        lvl_rows[(r["capability_id"].strip(), r["level"].strip())] = r
        for k in r["source_keys"].split(";"):
            if k.strip() and k.strip() not in bib:
                issues.append(f"capability_levels: {r['capability_id']} {r['level']} unknown source key '{k.strip()}'")
        if not r["why"].strip():
            issues.append(f"capability_levels: {r['capability_id']} {r['level']} empty why")
    missing = sum(1 for cid in caps for p in P_LEVELS if (cid, p) not in lvl_rows)
    if missing:
        issues.append(f"{missing} unsourced capability levels (of {len(caps) * 6})")

    roles_dir = os.path.join(ROOT, "roles")
    for slug in sorted(os.listdir(roles_dir)):
        ry = os.path.join(roles_dir, slug, "role.yaml")
        if not os.path.isfile(ry):
            continue
        with open(ry, encoding="utf-8") as f:
            role = yaml.safe_load(f)
        codes = [lv["code"] for lv in role.get("levels", [])]
        for c in role.get("competencies", []):
            theme = c.get("theme", "?")
            anchor = str(c.get("anchor", "")).strip()
            if anchor and anchor not in bib:
                issues.append(f"{slug}: '{theme}' anchor '{anchor[:40]}' is not a bibliography key")
            mappings = c.get("mappings") or {}
            if set(mappings) != set(codes):
                issues.append(f"{slug}: '{theme}' mappings cover {sorted(mappings)} not {codes}")
            for code, mp in mappings.items():
                if mp.get("p") not in P_LEVELS:
                    issues.append(f"{slug}: '{theme}' {code} invalid p '{mp.get('p')}'")
                if not mp.get("sources"):
                    issues.append(f"{slug}: '{theme}' {code} has no sources")
                else:
                    for k in mp["sources"]:
                        if k not in bib:
                            issues.append(f"{slug}: '{theme}' {code} unknown source key '{k}'")
                if not str(mp.get("why", "")).strip():
                    issues.append(f"{slug}: '{theme}' {code} empty why")
    return issues


def evidence_warnings():
    warns = []
    roles_dir = os.path.join(ROOT, "roles")
    for slug in sorted(os.listdir(roles_dir)):
        ry = os.path.join(roles_dir, slug, "role.yaml")
        if not os.path.isfile(ry):
            continue
        with open(ry, encoding="utf-8") as f:
            role = yaml.safe_load(f)
        for c in role.get("competencies", []):
            for code, ev in (c.get("evidence") or {}).items():
                ev = ev or ""  # `M1:` with no value in yaml parses as None
                p = (c.get("mappings") or {}).get(code, {}).get("p", "")
                if p in ("P1", "P2", "P3") and any(m in ev.lower() for m in ABOVE_BAR):
                    warns.append(f"{slug}: '{c.get('theme')}' {code} evidence exceeds {p} bar: '{ev[:60]}'")
    return warns


def derived_staleness_failures():
    """Hard failures: a derived role's committed ladder differs from a fresh render."""
    import filecmp
    import subprocess as sp
    import tempfile
    fails = []
    roles_dir = os.path.join(ROOT, "roles")
    renderer = os.path.join(ROOT, "scripts", "render_role_ladder.py")
    for slug in sorted(os.listdir(roles_dir)):
        ry = os.path.join(roles_dir, slug, "role.yaml")
        if not os.path.isfile(ry):
            continue
        with open(ry, encoding="utf-8") as f:
            role = yaml.safe_load(f)
        if not role.get("derived"):
            continue
        with tempfile.TemporaryDirectory() as tmp:
            res = sp.run([sys.executable, renderer, slug, "--force", "--out-dir", tmp],
                         capture_output=True, text=True)
            if res.returncode != 0:
                fails.append(f"{slug}: derived render failed: {res.stderr.strip() or res.stdout.strip()}")
                continue
            for name in ("ladder.md", "ladder.csv"):
                committed = os.path.join(roles_dir, slug, name)
                if not os.path.isfile(committed) or not filecmp.cmp(committed, os.path.join(tmp, name), shallow=False):
                    fails.append(f"{slug}: {name} is stale — run scripts/render_role_ladder.py {slug}")
    return fails


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--strict", action="store_true",
                         help="fail on sourcing gaps (report-only by default)")
    args = parser.parse_args()
    strict = args.strict

    # 1 + 2: catalog integrity
    with open(os.path.join(ROOT, "data", "capabilities.csv"), encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    ids = [r["id"] for r in rows]
    dupes = [i for i, n in collections.Counter(ids).items() if n > 1]
    if dupes:
        fail(f"duplicate capability ids: {dupes}")
    for r in rows:
        for col in ("id", "segment", "domain", "focus_area", "capability", "type", "description"):
            if not r.get(col, "").strip():
                fail(f"{r.get('id','<no id>')}: empty required column '{col}'")
    with open(os.path.join(ROOT, "data", "capabilities.json"), encoding="utf-8") as f:
        jids = {e["id"] for e in json.load(f)}
    if jids != set(ids):
        fail(f"csv/json id mismatch: csv-only={sorted(set(ids)-jids)[:5]} json-only={sorted(jids-set(ids))[:5]}")

    # 3: domain counts
    actual = collections.Counter(r["domain"] for r in rows)
    actual_foci = {d: len({r["focus_area"] for r in rows if r["domain"] == d}) for d in actual}
    with open(os.path.join(ROOT, "data", "domains.csv"), encoding="utf-8-sig") as f:
        for d in csv.DictReader(f):
            name = d["domain"]
            if int(d["capabilities"]) != actual.get(name, 0):
                fail(f"domains.csv: {name} says {d['capabilities']} capabilities, catalog has {actual.get(name, 0)}")
            if int(d["focus_areas"]) != actual_foci.get(name, 0):
                fail(f"domains.csv: {name} says {d['focus_areas']} focus areas, catalog has {actual_foci.get(name, 0)}")

    # 4-6: role records
    roles_dir = os.path.join(ROOT, "roles")
    catalog_ids = set(ids)
    for slug in sorted(os.listdir(roles_dir)):
        ry = os.path.join(roles_dir, slug, "role.yaml")
        if not os.path.isfile(ry):
            continue
        with open(ry, encoding="utf-8") as f:
            role = yaml.safe_load(f)
        want = {}
        for c in role.get("competencies", []):
            cap = str(c.get("capability", "")).strip()
            triple = (c.get("key_area", "").strip(), c.get("key_attribute", "").strip(), c.get("theme", "").strip())
            want[triple] = cap
            if cap == "proposed":
                ref = c.get("proposal_ref", "")
                if not ref or not os.path.isfile(os.path.join(ROOT, ref)):
                    fail(f"{slug}: '{c.get('theme')}' is proposed but proposal_ref '{ref}' does not exist")
            elif cap not in catalog_ids:
                fail(f"{slug}: '{c.get('theme')}' references unknown capability id '{cap}'")

        lc = os.path.join(roles_dir, slug, "ladder.csv")
        if os.path.isfile(lc):
            with open(lc, encoding="utf-8-sig", newline="") as f:
                lrows = list(csv.reader(f))
            if lrows and len(lrows[0]) > 4 and lrows[0][4].strip() == "capability":
                for r in lrows[1:]:
                    if r and r[0] == "skill":
                        triple = (r[1].strip(), r[2].strip(), r[3].strip())
                        csv_cap = r[4].strip()
                        expect = want.get(triple)
                        norm = "proposed" if csv_cap.startswith("proposed") else csv_cap
                        if expect is not None and norm != expect:
                            fail(f"{slug}: ladder.csv capability '{csv_cap}' != role.yaml '{expect}' for {triple[2]}")
            flags = ["--manager"] if role.get("variant") == "manager" else []
            res = subprocess.run([sys.executable, VALIDATOR, lc, *flags], capture_output=True, text=True)
            if res.returncode != 0:
                fail(f"{slug}: ladder validator failed:\n{res.stdout.strip()}")

    for f_ in derived_staleness_failures():
        fail(f_)
    for w in evidence_warnings():
        print(f"WARN  {w}")
    src_issues = sourcing_issues()
    if strict:
        for i in src_issues:
            fail(i)
    else:
        for i in src_issues:
            print(f"REPORT {i}")
        if src_issues:
            print(f"REPORT {len(src_issues)} sourcing issue(s) — will fail under --strict (R4)")

    if errors:
        print(f"FAIL — {len(errors)} consistency error(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("OK — catalog, domains, and all role records are consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
