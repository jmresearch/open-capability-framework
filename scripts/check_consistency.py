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


def main():
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

    if errors:
        print(f"FAIL — {len(errors)} consistency error(s):")
        for e in errors:
            print(f"  - {e}")
        return 1
    print("OK — catalog, domains, and all role records are consistent")
    return 0


if __name__ == "__main__":
    sys.exit(main())
