#!/usr/bin/env python3
"""Merge R2 sourcing fragments into the canonical tables.

Reads data/sourcing-fragments/*.levels.csv and *.bib.csv, then:
  - appends new bibliography rows (fails on key collisions with different citations,
    skips exact-duplicate keys, warns on distinct keys whose citations look identical)
  - appends capability_levels rows (fails on (capability_id, level) collisions, on
    unknown capability ids, and on source keys that resolve nowhere)
  - reports *.flags.csv contents as the recalibration list

Dry-run by default; --write commits the merge to data/*.csv (sorted, stable).
Run with:  uv run python scripts/merge_sourcing_fragments.py [--write]
"""

import csv
import glob
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA = os.path.join(ROOT, "data")
FRAG = os.path.join(DATA, "sourcing-fragments")
P_ORDER = {f"P{i}": i for i in range(1, 7)}


def read(path):
    with open(path, encoding="utf-8-sig", newline="") as f:
        return list(csv.DictReader(f))


def norm_citation(c):
    return re.sub(r"[^a-z0-9]+", "", c.lower())[:80]


def main():
    write = "--write" in sys.argv
    problems, warnings = [], []

    bib = {r["key"].strip(): r for r in read(os.path.join(DATA, "bibliography.csv"))}
    levels = {(r["capability_id"].strip(), r["level"].strip()): r
              for r in read(os.path.join(DATA, "capability_levels.csv"))}
    cap_ids = {r["id"].strip() for r in read(os.path.join(DATA, "capabilities.csv"))}

    seen_citations = {norm_citation(r["citation"]): k for k, r in bib.items()}
    new_bib, new_levels, flags = {}, {}, []

    for path in sorted(glob.glob(os.path.join(FRAG, "*.bib.csv"))):
        for r in read(path):
            key = r["key"].strip()
            existing = bib.get(key) or new_bib.get(key)
            if existing:
                if norm_citation(existing["citation"]) != norm_citation(r["citation"]):
                    problems.append(f"{os.path.basename(path)}: key '{key}' collides with a different citation")
                continue  # exact duplicate key: first writer wins
            dup = seen_citations.get(norm_citation(r["citation"]))
            if dup and dup != key:
                warnings.append(f"{os.path.basename(path)}: '{key}' duplicates citation of '{dup}' — remapping")
                continue  # remap handled below via alias
            seen_citations[norm_citation(r["citation"])] = key
            new_bib[key] = r

    def resolve(key):
        if key in bib or key in new_bib:
            return key
        # alias: a fragment key whose citation matched an existing key
        return None

    alias = {}
    for path in sorted(glob.glob(os.path.join(FRAG, "*.bib.csv"))):
        for r in read(path):
            key = r["key"].strip()
            if key not in bib and key not in new_bib:
                dup = seen_citations.get(norm_citation(r["citation"]))
                if dup:
                    alias[key] = dup

    for path in sorted(glob.glob(os.path.join(FRAG, "*.levels.csv"))):
        for r in read(path):
            cid, lvl = r["capability_id"].strip(), r["level"].strip()
            if cid not in cap_ids:
                problems.append(f"{os.path.basename(path)}: unknown capability id '{cid}'")
                continue
            if lvl not in P_ORDER:
                problems.append(f"{os.path.basename(path)}: {cid} bad level '{lvl}'")
                continue
            if (cid, lvl) in levels or (cid, lvl) in new_levels:
                problems.append(f"{os.path.basename(path)}: duplicate row {cid} {lvl}")
                continue
            keys = [alias.get(k.strip(), k.strip()) for k in r["source_keys"].split(";") if k.strip()]
            unresolved = [k for k in keys if resolve(k) is None]
            if unresolved:
                problems.append(f"{os.path.basename(path)}: {cid} {lvl} unresolved source keys {unresolved}")
                continue
            if not keys or not r["why"].strip():
                problems.append(f"{os.path.basename(path)}: {cid} {lvl} empty sources/why")
                continue
            new_levels[(cid, lvl)] = {"capability_id": cid, "level": lvl,
                                      "source_keys": ";".join(keys), "why": r["why"].strip()}

    for path in sorted(glob.glob(os.path.join(FRAG, "*.flags.csv"))):
        flags.extend(read(path))

    print(f"fragments: +{len(new_bib)} bibliography rows, +{len(new_levels)} level rows, "
          f"{len(flags)} recalibration flags")
    for w in warnings:
        print(f"WARN  {w}")
    for p in problems:
        print(f"ERROR {p}")
    if flags:
        print("RECALIBRATION FLAGS:")
        for f_ in flags:
            print(f"  - {f_['capability_id']} {f_['level']}: {f_['reason']}")
    if problems:
        print(f"FAIL — {len(problems)} problem(s); nothing written")
        return 1
    if not write:
        print("dry run OK — rerun with --write to merge")
        return 0

    with open(os.path.join(DATA, "bibliography.csv"), "a", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["key", "type", "citation", "link", "notes"])
        for key in sorted(new_bib):
            w.writerow({k: new_bib[key].get(k, "") for k in w.fieldnames})
    merged = list(levels.values()) + list(new_levels.values())
    merged.sort(key=lambda r: (r["capability_id"], P_ORDER[r["level"]]))
    with open(os.path.join(DATA, "capability_levels.csv"), "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["capability_id", "level", "source_keys", "why"])
        w.writeheader()
        w.writerows(merged)
    print("merged — canonical tables updated")
    return 0


if __name__ == "__main__":
    sys.exit(main())
