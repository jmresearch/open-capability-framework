# Sourced Derivation Plumbing (R1) Implementation Plan

> **For agentic workers:** REQUIRED SUB-SKILL: Use superpowers:subagent-driven-development (recommended) or superpowers:executing-plans to implement this plan task-by-task. Steps use checkbox (`- [ ]`) syntax for tracking.

**Goal:** Build the schema, renderers, validator, and skill-text changes that make ladder cells mechanically assembled from a sourced catalog (spec: `docs/superpowers/specs/2026-07-09-sourced-derivation-methodology-design.md`).

**Architecture:** Two new data tables (`data/bibliography.csv`, `data/capability_levels.csv`) hold citations; `roles/<slug>/role.yaml` gains per-level `mappings` (proficiency + sources + why) and `evidence`; a new `scripts/render_role_ladder.py` generates `ladder.md`/`ladder.csv` for roles flagged `derived: true`; `check_consistency.py` gains sourcing checks behind `--strict` (report-only by default until R4). The R2 catalog-sourcing sweep and R3 role retrofit are separate follow-on plans that fill these structures with researched content.

**Tech Stack:** Python 3.12 stdlib + openpyxl + pyyaml, pytest for tests, all run via `uv run`.

## Global Constraints

- All Python runs via uv: `uv run --with openpyxl --with pyyaml --with pytest python ...` (never pip).
- Derived files (`data/*.md`, `data/capabilities.xlsx`, `roles/*/ladder.md|csv|xlsx` for derived roles) are never hand-edited; regenerate via scripts.
- Cell format in derived ladders: `Depth: {bar}` + optional ` Evidenced by: {evidence}` + ` Scope: {scope}.` — bar text byte-identical to the catalog profile.
- Generated ladder.csv must pass `skills/career-ladder/scripts/validate_csv.py` (with `--manager` for manager-variant roles). Notably: theme ≤60 chars, no literal substring `anchor:` in level cells, no position-locked phrases in manager ladders.
- `check_consistency.py` default mode stays exit-0 on sourcing gaps (report only). `--strict` fails on them. CI keeps default mode until R4.
- Bibliography source types: `theory | empirical | standard | company-ladder`.
- Every bibliography row added in this plan must be link-verified at execution time (fetch the link; for offline works confirm the work exists via a web search) — no unverified citations, per spec.
- Commit after every task. Conventional Commits, subject ≤50 chars, no AI attribution.

## File Structure

- Create: `data/bibliography.csv` — citation registry (key,type,citation,link,notes).
- Create: `data/capability_levels.csv` — per capability × P-level sourcing (capability_id,level,source_keys,why).
- Create: `scripts/migrate_role_yaml.py` — one-shot `proficiency:` → `mappings:` line-preserving migration.
- Create: `scripts/render_role_ladder.py` — role.yaml + catalog → ladder.md + ladder.csv for `derived: true` roles.
- Modify: `scripts/render_catalog.py` — join sourcing tables into `capabilities.md` / `capabilities.xlsx`.
- Modify: `scripts/render_role_xlsx.py` — add "What it covers" / "Theory anchor & why" matrix columns + "Sources & Theory" sheet.
- Modify: `scripts/check_consistency.py` — sourcing checks + `--strict` + derived-ladder staleness.
- Modify: `.github/workflows/render.yml` — run the new renderer in both jobs; include ladder.csv in staleness diff.
- Modify: `skills/career-ladder/references/capability-framework.md`, `skills/career-ladder/SKILL.md`, `skills/create-canonical-role/SKILL.md`, `PROMPT.md` — normative rule.
- Create: `tests/test_migrate_role_yaml.py`, `tests/test_render_catalog_sources.py`, `tests/test_render_role_ladder.py`, `tests/test_check_consistency_sourcing.py`, `tests/conftest.py`.

Test invocation everywhere: `uv run --with openpyxl --with pyyaml --with pytest python -m pytest tests/ -v`

---

### Task 1: Bibliography + golden capability_levels rows

**Files:**
- Create: `data/bibliography.csv`
- Create: `data/capability_levels.csv`

**Interfaces:**
- Produces: `data/bibliography.csv` with columns `key,type,citation,link,notes`; `data/capability_levels.csv` with columns `capability_id,level,source_keys,why` (source_keys = semicolon-separated bibliography keys). Later tasks read both with `csv.DictReader`.

- [ ] **Step 1: Write `data/bibliography.csv`**

```csv
key,type,citation,link,notes
dreyfus1980,theory,"Dreyfus & Dreyfus, A Five-Stage Model of the Mental Activities Involved in Directed Skill Acquisition (1980)",https://apps.dtic.mil/sti/citations/ADA084551,Basis of the P1-P6 proficiency bands
tuckman1965,theory,"Tuckman, Developmental Sequence in Small Groups, Psychological Bulletin 63(6), 384-399 (1965)",https://doi.org/10.1037/h0022100,Forming-storming-norming-performing team stages
bauer2010,empirical,"Bauer, Onboarding New Employees: Maximizing Success, SHRM Foundation Effective Practice Guidelines (2010)",https://www.shrm.org/topics-tools/research/onboarding-new-employees-maximizing-success,Structured onboarding levels and outcomes
watkins2003,theory,"Watkins, The First 90 Days (Harvard Business Review Press, 2003)",,30/60/90 transition and ramp planning
sfia9,standard,"SFIA Foundation, Skills Framework for the Information Age, version 9 (2024)",https://sfia-online.org/en/sfia-9,Seven-level responsibility descriptors used as leveling standard
gitlab-em-jd,company-ladder,"GitLab Handbook, Engineering Management Job Framework (accessed 2026-07)",https://handbook.gitlab.com/job-families/engineering/engineering-management/,Published EM/Senior EM/Director requirement deltas
skelton-pais2019,theory,"Skelton & Pais, Team Topologies (IT Revolution, 2019)",,Team boundaries; org-level team formation patterns
haspeslagh1991,theory,"Haspeslagh & Jemison, Managing Acquisitions: Creating Value Through Corporate Renewal (Free Press, 1991)",,Integration design for step-change organizational growth
```

- [ ] **Step 2: Verify every source is real**

For each row with a link: `curl -sIL -o /dev/null -w "%{http_code} " <link>` — expect 200/301/302 (SHRM/GitLab may bot-block; a 403 is acceptable only if a web search confirms the document title verbatim). For link-less books (watkins2003, skelton-pais2019, haspeslagh1991): web-search the exact citation; confirm author/title/year match. Fix any row that does not verify. Record nothing extra — verification is a gate, not an artifact.

- [ ] **Step 3: Write `data/capability_levels.csv` with the EM-13 golden example**

Header + exactly six rows (this is the worked example that exercises the whole pipeline; the R2 sweep fills the other ~2,724 rows):

```csv
capability_id,level,source_keys,why
EM-13,P1,bauer2010,"Executing someone else's onboarding checklist and escalating problems is Bauer's passive/compliance onboarding level — rule-following without adaptation, the Dreyfus novice band."
EM-13,P2,bauer2010;watkins2003,"Independently running a structured 30/60/90 with buddies and early wins is Bauer's proactive-onboarding practice and Watkins' standard line-manager transition toolkit, applied to one team without needing design authority."
EM-13,P3,tuckman1965,"Reading a team's formation stage and intervening live (resetting norms post-merge, naming storming) is applying Tuckman's stage model to real group dynamics — situational judgment beyond procedure."
EM-13,P4,tuckman1965;skelton-pais2019,"Building the onboarding/team-launch playbook other teams adopt and repeatedly standing up new teams is codified, transferable expertise — the shift from doing to defining the approach."
EM-13,P5,haspeslagh1991,"Designing how an organization absorbs step-change growth without culture dilution is acquisition-integration design per Haspeslagh & Jemison — organization-level authority over formation."
EM-13,P6,skelton-pais2019,"Making team formation a predictable org-wide capability with audited machinery is defining the discipline's operating model across a company — pioneer-level practice shaping."
```

- [ ] **Step 4: Sanity-check parse**

Run: `uv run python -c "import csv; b=list(csv.DictReader(open('data/bibliography.csv'))); l=list(csv.DictReader(open('data/capability_levels.csv'))); ks={r['key'] for r in b}; assert len(ks)==len(b)==8, 'dup/missing keys'; assert all(k in ks for r in l for k in r['source_keys'].split(';')), 'unresolved key'; assert {r['level'] for r in l}=={'P1','P2','P3','P4','P5','P6'}; print('OK', len(b), 'sources,', len(l), 'level rows')"`
Expected: `OK 8 sources, 6 level rows`

- [ ] **Step 5: Commit**

```bash
git add data/bibliography.csv data/capability_levels.csv
git commit -m "feat(data): add bibliography and capability_levels tables"
```

---

### Task 2: role.yaml schema migration (`proficiency:` → `mappings:`)

**Files:**
- Create: `scripts/migrate_role_yaml.py`
- Create: `tests/test_migrate_role_yaml.py`, `tests/conftest.py`
- Modify: all `roles/*/role.yaml` (mechanical, via the script)
- Modify: `scripts/render_role_links.py:73`, `scripts/render_role_xlsx.py:205` (both read the old `proficiency` map and break after migration)

**Interfaces:**
- Consumes: nothing from other tasks.
- Produces: `migrate_lines(lines: list[str]) -> list[str]` in `scripts/migrate_role_yaml.py`; every role.yaml competency thereafter has `mappings: {<code>: {p: P<k>, sources: [], why: ""}}` instead of `proficiency: {<code>: P<k>}`. Comments and all other lines byte-preserved. Later tasks (renderer, validator) read `mappings`.

- [ ] **Step 1: Write `tests/conftest.py`**

```python
import os
import sys

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "scripts"))
```

- [ ] **Step 2: Write the failing test**

`tests/test_migrate_role_yaml.py`:

```python
import yaml

from migrate_role_yaml import migrate_lines

SRC = """\
competencies:
  # ---- People ----
  - theme: Onboarding & team formation
    capability: EM-13
    anchor: "Tuckman, Developmental Sequence in Small Groups (1965)"
    proficiency: {M1: P2, M2: P3, M3: P4, M4: P4, M5: P5, M6: P6}
"""


def test_migrates_proficiency_to_mappings():
    out = "".join(migrate_lines(SRC.splitlines(keepends=True)))
    assert "proficiency:" not in out
    data = yaml.safe_load(out)
    m = data["competencies"][0]["mappings"]
    assert m["M1"] == {"p": "P2", "sources": [], "why": ""}
    assert m["M6"] == {"p": "P6", "sources": [], "why": ""}
    assert "# ---- People ----" in out  # comments preserved


def test_idempotent_and_untouched_lines():
    lines = SRC.splitlines(keepends=True)
    once = migrate_lines(lines)
    twice = migrate_lines(once)
    assert once == twice
    assert "  - theme: Onboarding & team formation\n" in once
```

- [ ] **Step 3: Run test to verify it fails**

Run: `uv run --with pytest --with pyyaml python -m pytest tests/test_migrate_role_yaml.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'migrate_role_yaml'`

- [ ] **Step 4: Write `scripts/migrate_role_yaml.py`**

```python
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
```

- [ ] **Step 5: Run test to verify it passes**

Run: `uv run --with pytest --with pyyaml python -m pytest tests/test_migrate_role_yaml.py -v`
Expected: 2 passed

- [ ] **Step 6: Update the two schema readers BEFORE migrating**

In `scripts/render_role_links.py` line 73, change:

```python
        p = comp["proficiency"][code]
```
to:
```python
        p = comp["mappings"][code]["p"]
```

In `scripts/render_role_xlsx.py` line 205 (inside `sheet_rating`), change:

```python
            p = comp["proficiency"][code]
```
to:
```python
            p = comp["mappings"][code]["p"]
```

- [ ] **Step 7: Run the migration on all roles and re-check consistency**

Run: `uv run --with pyyaml python scripts/migrate_role_yaml.py`
Expected: one `migrated roles/<slug>/role.yaml` line per role that had `proficiency:` (engineering-management, platform-engineering, dairy-plant-operations, ai-engineer, full-stack-typescript, product-manager — plus platform-engineering-manager if its role.yaml exists on this branch).

Run: `uv run --with openpyxl --with pyyaml python scripts/check_consistency.py`
Expected: `OK — catalog, domains, and all role records are consistent` (existing checks don't read `proficiency`).

Then eyeball one diff: `git diff roles/engineering-management/role.yaml | head -30` — only proficiency→mappings lines changed, comments intact.

- [ ] **Step 8: Verify the patched renderers against migrated roles**

Run: `uv run --with pyyaml python scripts/render_role_links.py && git diff --stat -- 'roles/*/ladder.md'`
Expected: no diff (link tables render identically from the new schema).

Run: `uv run --with openpyxl --with pyyaml python scripts/render_role_xlsx.py engineering-management && git checkout -- roles/engineering-management/ladder.xlsx`
Expected: `wrote roles/engineering-management/ladder.xlsx (...)` with no traceback (binary reverted — CI owns xlsx regeneration).

- [ ] **Step 9: Commit**

```bash
git add scripts/migrate_role_yaml.py scripts/render_role_links.py scripts/render_role_xlsx.py tests/ roles/*/role.yaml
git commit -m "feat(roles): migrate proficiency maps to sourced mappings schema"
```

---

### Task 3: Sourced catalog rendering (`render_catalog.py`)

**Files:**
- Modify: `scripts/render_catalog.py`
- Test: `tests/test_render_catalog_sources.py`

**Interfaces:**
- Consumes: Task 1's CSVs.
- Produces: `load_sourcing() -> (bib: dict[key, row], levels: dict[(capability_id, level), row])` in `render_catalog.py` (validator reuses the same file formats); `capabilities.md` P-profile lines gain `— *Why this level:* <why> [source citations]` when a `capability_levels.csv` row exists; `capabilities.xlsx` gains a `Sources & Theory` sheet listing the bibliography.

- [ ] **Step 1: Write the failing test**

`tests/test_render_catalog_sources.py`:

```python
import csv
import os

from render_catalog import load_sourcing, render_capabilities_md, read_csv

ROOT = os.path.join(os.path.dirname(__file__), "..")


def test_sourced_level_renders_why_and_citation():
    caps = read_csv("capabilities.csv")
    scale = read_csv("proficiency_scale.csv")
    domains = read_csv("domains.csv")
    bib, levels = load_sourcing()
    md = render_capabilities_md(caps, scale, domains, bib, levels)
    em13 = md.split('id="em-13"')[1].split('id="em-14"')[0]
    assert "30/60/90 onboarding with named buddies" in em13          # bar text unchanged
    assert "Watkins' standard line-manager transition toolkit" in em13  # why rendered
    assert "Tuckman, Developmental Sequence in Small Groups" in em13    # citation rendered


def test_unsourced_level_renders_without_why():
    caps = read_csv("capabilities.csv")
    scale = read_csv("proficiency_scale.csv")
    domains = read_csv("domains.csv")
    bib, levels = load_sourcing()
    md = render_capabilities_md(caps, scale, domains, bib, levels)
    swe01 = md.split('id="swe-01"')[1].split('id="swe-02"')[0]
    assert "Why this level" not in swe01  # no capability_levels rows yet for SWE-01
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run --with pytest --with openpyxl python -m pytest tests/test_render_catalog_sources.py -v`
Expected: FAIL — `ImportError: cannot import name 'load_sourcing'`

- [ ] **Step 3: Implement in `scripts/render_catalog.py`**

Add after `read_csv`:

```python
def load_sourcing():
    """(bibliography by key, capability_levels by (capability_id, level))."""
    bib = {r["key"].strip(): r for r in read_csv("bibliography.csv")}
    levels = {(r["capability_id"].strip(), r["level"].strip()): r
              for r in read_csv("capability_levels.csv")}
    return bib, levels
```

Change `render_capabilities_md(caps, scale, domains)` signature to `render_capabilities_md(caps, scale, domains, bib, levels)` and replace the per-level loop body:

```python
        for col, lvl, name in p_cols:
            line = (f"- **[{lvl} — {name}](proficiency_scale.md#{lvl.lower()}):** "
                    f"{row[col].strip()}")
            src = levels.get((cid, lvl))
            if src:
                cites = "; ".join(
                    bib[k]["citation"] for k in src["source_keys"].split(";") if k.strip()
                )
                line += f"\n  — *Why this level:* {src['why'].strip()} *Sources:* {cites}."
            out.append(line)
```

In `render_xlsx(caps, scale, scopes, domains)` change the signature to accept `bib` and append before `wb.save`:

```python
    ws = wb.create_sheet("Sources & Theory")
    ws.append(["Key", "Type", "Citation", "Link", "Notes"])
    for r in bib.values():
        ws.append([r["key"], r["type"], r["citation"], r["link"], r["notes"]])
    style_sheet(ws, [18, 14, 70, 40, 40], wrap_cols={3, 5})
```

Update `main()` to load and thread the new args:

```python
    bib, levels = load_sourcing()
    write_text("capabilities.md", render_capabilities_md(caps, scale, domains, bib, levels))
    render_xlsx(caps, scale, scopes, domains, bib)
```

- [ ] **Step 4: Run tests, then regenerate**

Run: `uv run --with pytest --with openpyxl python -m pytest tests/test_render_catalog_sources.py -v`
Expected: 2 passed

Run: `uv run --with openpyxl python scripts/render_catalog.py`
Expected: normal `wrote data/...` lines. Check: `grep -A1 "P2 — Independent.*30/60/90" data/capabilities.md | head -4` shows the `Why this level` line under EM-13 only.

- [ ] **Step 5: Commit**

```bash
git add scripts/render_catalog.py tests/test_render_catalog_sources.py data/capabilities.md data/capabilities.xlsx
git commit -m "feat(catalog): render per-level sources and why lines"
```

---

### Task 4: Derived ladder renderer (`render_role_ladder.py`)

**Files:**
- Create: `scripts/render_role_ladder.py`
- Test: `tests/test_render_role_ladder.py`

**Interfaces:**
- Consumes: `mappings`/`evidence` role.yaml schema (Task 2), sourcing tables (Task 1).
- Produces: `assemble_cell(bar, evidence, scope) -> str`; `render_role(slug, force=False) -> bool` (False = skipped because role lacks `derived: true`); CLI `uv run --with pyyaml python scripts/render_role_ladder.py [--force] [slug ...]`. Writes `roles/<slug>/ladder.md` and `roles/<slug>/ladder.csv`. Validator (Task 6) shells out to this with `--force --stdout-dir` for staleness diffs.

**Behavioral contract (from spec):**
- Only renders roles whose role.yaml has `derived: true` (set per-role during R3), unless `force`.
- Refuses (raises `SystemExit` with message) if any competency has `capability: proposed` or a capability id absent from the catalog — proposals must be accepted before a role goes derived.
- ladder.csv cell = `Depth: {bar} Evidenced by: {evidence} Scope: {scope}.` (evidence clause omitted when absent). Bar comes byte-for-byte from `capabilities.csv` column for the mapped P-level.
- ladder.md per competency: heading, `*Anchor:*` line (bibliography citation via the role.yaml `anchor` key; legacy free-text anchors render as-is), OCF/P-mapping link table (same shape `render_role_links.py` produces today), then per level: bar, optional *Evidenced by*, *Scope*, *Why this level* + sources. Ends with `## Sources` listing every bibliography citation used.

- [ ] **Step 1: Write the failing test**

`tests/test_render_role_ladder.py` — uses a temp fixture role against the real catalog (EM-13 is fully sourced from Task 1):

```python
import csv
import os
import shutil
import subprocess
import sys

import pytest
import yaml

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
FIXTURE_ROLE = {
    "role": "Fixture Manager", "slug": "zz-fixture", "variant": "manager",
    "minted": "2026-07-09", "derived": True,
    "levels": [
        {"code": "M1", "title": "Manager", "scope": "one team", "focus": "one team"},
        {"code": "M2", "title": "Senior Manager", "scope": "a critical team", "focus": "critical team"},
    ],
    "competencies": [
        {"theme": "Onboarding & team formation", "capability": "EM-13",
         "key_area": "People", "key_attribute": "Team Composition",
         "anchor": "tuckman1965",
         "mappings": {
             "M1": {"p": "P2", "sources": ["bauer2010"], "why": "Line manager runs onboarding independently."},
             "M2": {"p": "P3", "sources": ["tuckman1965"], "why": "Reads and intervenes on formation stage."},
         },
         "evidence": {"M1": "New hire ships a real change in their first sprint."}},
        {"theme": "Delegation & empowerment", "capability": "EM-14",
         "key_area": "People", "key_attribute": "Team Composition",
         "anchor": "tuckman1965",
         "mappings": {
             "M1": {"p": "P2", "sources": ["gitlab-em-jd"], "why": "Delegates outcomes within one team."},
             "M2": {"p": "P3", "sources": ["gitlab-em-jd"], "why": "Hands ownership of critical work."},
         }},
    ],
}


@pytest.fixture()
def fixture_role():
    d = os.path.join(ROOT, "roles", "zz-fixture")
    os.makedirs(d, exist_ok=True)
    with open(os.path.join(d, "role.yaml"), "w") as f:
        yaml.safe_dump(FIXTURE_ROLE, f, sort_keys=False)
    yield "zz-fixture"
    shutil.rmtree(d)


def catalog_bar(cap_id, p):
    scale = {r["level"]: r["name"].lower() for r in
             csv.DictReader(open(os.path.join(ROOT, "data", "proficiency_scale.csv")))}
    for r in csv.DictReader(open(os.path.join(ROOT, "data", "capabilities.csv"), encoding="utf-8-sig")):
        if r["id"] == cap_id:
            return r[f"{p}_{scale[p]}"].strip()
    raise KeyError(cap_id)


def test_renders_bar_verbatim_plus_evidence_and_scope(fixture_role):
    from render_role_ladder import render_role
    assert render_role(fixture_role) is True
    md = open(os.path.join(ROOT, "roles", fixture_role, "ladder.md")).read()
    bar = catalog_bar("EM-13", "P2")
    assert bar in md
    assert "*Evidenced by:* New hire ships a real change in their first sprint." in md
    assert "*Why this level:* Line manager runs onboarding independently." in md
    assert "Tuckman, Developmental Sequence in Small Groups" in md  # anchor + sources resolved
    rows = list(csv.reader(open(os.path.join(ROOT, "roles", fixture_role, "ladder.csv"))))
    skill = [r for r in rows if r and r[0] == "skill" and r[3] == "Onboarding & team formation"][0]
    assert skill[5] == f"Depth: {bar} Evidenced by: New hire ships a real change in their first sprint. Scope: one team."
    em14 = [r for r in rows if r and r[0] == "skill" and r[3] == "Delegation & empowerment"][0]
    assert em14[5] == f"Depth: {catalog_bar('EM-14', 'P2')} Scope: one team."  # no evidence clause


def test_generated_csv_passes_ladder_validator(fixture_role):
    from render_role_ladder import render_role
    render_role(fixture_role)
    res = subprocess.run(
        [sys.executable, os.path.join(ROOT, "skills", "career-ladder", "scripts", "validate_csv.py"),
         os.path.join(ROOT, "roles", fixture_role, "ladder.csv"), "--manager"],
        capture_output=True, text=True)
    assert res.returncode == 0, res.stdout


def test_skips_non_derived_and_rejects_proposed(fixture_role):
    from render_role_ladder import render_role
    path = os.path.join(ROOT, "roles", fixture_role, "role.yaml")
    role = yaml.safe_load(open(path))
    role["derived"] = False
    yaml.safe_dump(role, open(path, "w"), sort_keys=False)
    assert render_role(fixture_role) is False
    role["derived"] = True
    role["competencies"][0]["capability"] = "proposed"
    yaml.safe_dump(role, open(path, "w"), sort_keys=False)
    with pytest.raises(SystemExit):
        render_role(fixture_role)
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run --with pytest --with pyyaml --with openpyxl python -m pytest tests/test_render_role_ladder.py -v`
Expected: FAIL — `ModuleNotFoundError: No module named 'render_role_ladder'`

- [ ] **Step 3: Write `scripts/render_role_ladder.py`**

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run --with pytest --with pyyaml --with openpyxl python -m pytest tests/test_render_role_ladder.py -v`
Expected: 3 passed. If `test_generated_csv_passes_ladder_validator` fails on the single-theme rule, the fixture already has two themes in one focus area — read the validator output; do not weaken the test.

- [ ] **Step 5: Confirm real roles are untouched**

Run: `uv run --with pyyaml python scripts/render_role_ladder.py`
Expected: `skip roles/<slug>: not marked derived: true` for every role; `git status --short roles/` shows no modifications.

- [ ] **Step 6: Commit**

```bash
git add scripts/render_role_ladder.py tests/test_render_role_ladder.py
git commit -m "feat(roles): add derived ladder renderer"
```

---

### Task 5: xlsx render — theory columns + Sources & Theory tab

**Files:**
- Modify: `scripts/render_role_xlsx.py`
- Test: extend `tests/test_render_role_ladder.py` (new test function; xlsx render consumes the same fixture)

**Interfaces:**
- Consumes: `load_catalog()` semantics from Task 4 (re-implemented locally; render_role_xlsx already loads role.yaml + ladder.csv via `load_role`/`skill_cells`).
- Produces: role `ladder.xlsx` whose "Competency Matrix" sheet has columns `Key Area, Focus, #, Competency, What it covers, Theory anchor & why, OCF, <levels...>`, and a `Sources & Theory` sheet `Framework | Source | Grounds | Link`. The Korn Ferry crosswalk is NOT added anywhere. Rating Template sheet unchanged.

- [ ] **Step 1: Write the failing test (append to `tests/test_render_role_ladder.py`)**

```python
def test_xlsx_has_theory_columns_and_sources_tab(fixture_role, tmp_path):
    from render_role_ladder import render_role
    render_role(fixture_role)
    subprocess.run(
        [sys.executable, os.path.join(ROOT, "scripts", "render_role_xlsx.py"), fixture_role],
        check=True, capture_output=True, text=True)
    import openpyxl
    wb = openpyxl.load_workbook(os.path.join(ROOT, "roles", fixture_role, "ladder.xlsx"))
    assert "Sources & Theory" in wb.sheetnames
    assert "Korn Ferry Crosswalk" not in wb.sheetnames
    matrix = wb["Competency Matrix"]
    headers = [c.value for c in matrix[1]]
    assert "What it covers" in headers and "Theory anchor & why" in headers
    src = wb["Sources & Theory"]
    assert [c.value for c in src[1]] == ["Framework", "Source", "Grounds", "Link"]
    cells = [str(c.value) for row in src.iter_rows() for c in row if c.value]
    assert any("Tuckman" in v for v in cells)
    os.remove(os.path.join(ROOT, "roles", fixture_role, "ladder.xlsx"))
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run --with pytest --with pyyaml --with openpyxl python -m pytest tests/test_render_role_ladder.py::test_xlsx_has_theory_columns_and_sources_tab -v`
Expected: FAIL (no "Sources & Theory" sheet / missing headers).

- [ ] **Step 3: Implement in `scripts/render_role_xlsx.py`**

Read the file first; it has `sheet_overview`, a matrix-sheet builder, a rating-template builder, and a sources-sheet builder fed by `sources_list(ladder_md)`. Changes:

a) Add loaders near `load_role`:

```python
def load_sourcing():
    def rd(name):
        with open(os.path.join(ROOT, "data", name), encoding="utf-8-sig", newline="") as f:
            return list(csv.DictReader(f))
    caps = {r["id"].strip(): r for r in rd("capabilities.csv")}
    bib = {r["key"].strip(): r for r in rd("bibliography.csv")}
    return caps, bib
```

b) Replace `sheet_matrix` (it currently emits `Key Area, Focus Area, Competency, OCF ID, Theory Anchor` + level codes) with:

```python
def sheet_matrix(wb, role, cells_by_triple, caps, bib):
    ws = wb.create_sheet("Competency Matrix")
    codes = [lv["code"] for lv in role["levels"]]
    ws.append(["Key Area", "Focus Area", "Competency", "OCF ID",
               "What it covers", "Theory anchor & why"] + codes)
    for c in ws[1]:
        c.font = BOLD
    for comp in role["competencies"]:
        triple = (comp["key_area"], comp["key_attribute"], comp["theme"])
        cells = cells_by_triple.get(triple)
        if cells is None:
            raise SystemExit(f"no ladder.csv skill row for {triple}")
        text, url = ocf_link(comp)
        cap_row = caps.get(str(comp.get("capability", "")).strip())
        covers = cap_row["description"] if cap_row else ""
        anchor_key = str(comp.get("anchor", "")).strip()
        anchor = bib[anchor_key]["citation"] if anchor_key in bib else anchor_key
        if comp.get("anchor_why"):
            anchor += f" — {comp['anchor_why']}"
        ws.append([comp["key_area"], comp["key_attribute"], comp["theme"], text,
                   covers, anchor] + cells)
        r = ws.max_row
        for c in ws[r]:
            c.font = BODY
            c.alignment = WRAP
        idc = ws.cell(row=r, column=4)
        idc.hyperlink = url
        idc.font = LINK
    set_widths(ws, [18, 18, 24, 12, 45, 45] + [55] * len(codes))
    ws.freeze_panes = "A2"
```

c) Replace the existing plain "Sources" sheet with `Sources & Theory`:

```python
def sheet_sources(wb, role, bib, ladder_md):
    ws = wb.create_sheet("Sources & Theory")
    ws.append(["Framework", "Source", "Grounds", "Link"])
    for c in ws[1]:
        c.font = BOLD
    seen = set()
    for comp in role["competencies"]:
        key = str(comp.get("anchor", "")).strip()
        row = bib.get(key)
        grounds = comp["theme"]
        if row:
            if key in seen:
                continue
            seen.add(key)
            ws.append([row["notes"] or comp["theme"], row["citation"], grounds, row["link"]])
        else:
            ws.append([comp["theme"], key or "(unsourced)", grounds, ""])
        for c in ws[ws.max_row]:
            c.font = BODY
            c.alignment = WRAP
    for src in sources_list(ladder_md):          # legacy free-text Sources section, if any
        ws.append(["", src, "", ""])
        for c in ws[ws.max_row]:
            c.font = BODY
            c.alignment = WRAP
    set_widths(ws, [30, 70, 40, 45])
    ws.freeze_panes = "A2"
```

d) Wire it up: replace the old `sheet_sources(wb, ladder_md)` definition with the new one, and update `render(slug)`:

```python
def render(slug):
    role, ladder_md, rows = load_role(slug)
    caps, bib = load_sourcing()
    wb = Workbook()
    sheet_overview(wb, role)
    sheet_matrix(wb, role, skill_cells(rows), caps, bib)
    sheet_rating(wb, role)
    sheet_sources(wb, role, bib, ladder_md)
    out = os.path.join(ROOT, "roles", slug, "ladder.xlsx")
    wb.save(out)
    print(f"wrote roles/{slug}/ladder.xlsx "
          f"({len(role['competencies'])} competencies, {len(role['levels'])} levels)")
```

- [ ] **Step 4: Run the full test file**

Run: `uv run --with pytest --with pyyaml --with openpyxl python -m pytest tests/test_render_role_ladder.py -v`
Expected: 4 passed.

- [ ] **Step 5: Regenerate a real role's xlsx to confirm legacy still renders**

Run: `uv run --with openpyxl --with pyyaml python scripts/render_role_xlsx.py engineering-management`
Expected: writes `roles/engineering-management/ladder.xlsx` without error (anchor is legacy free text → falls back gracefully). Revert the binary: `git checkout -- roles/engineering-management/ladder.xlsx` (CI regenerates xlsx on main; don't commit local binary churn).

- [ ] **Step 6: Commit**

```bash
git add scripts/render_role_xlsx.py tests/test_render_role_ladder.py
git commit -m "feat(xlsx): theory columns and Sources & Theory tab"
```

---

### Task 6: Validator sourcing checks + `--strict`

**Files:**
- Modify: `scripts/check_consistency.py`
- Test: `tests/test_check_consistency_sourcing.py`

**Interfaces:**
- Consumes: Tasks 1–4 file formats.
- Produces: `check_consistency.py --strict` exit-1 on sourcing gaps; default mode prints them as `REPORT` lines and stays exit-0 (unless pre-existing hard checks fail). New module-level function `sourcing_issues() -> list[str]` so tests call it directly. Derived-role ladder staleness is a hard failure in BOTH modes.

**Checks to add (spec §Rendering & validation):**
1. Every `capabilities.csv` id × P1–P6 has a `capability_levels.csv` row with ≥1 source key and non-empty why → gap = sourcing issue.
2. Every source key in `capability_levels.csv` and every role.yaml `mappings.*.sources[]` / `anchor` key resolves in `bibliography.csv` (a role.yaml anchor that is legacy free text — contains a space — is a sourcing issue, not a hard failure).
3. Every role.yaml mapping has `p` in P1–P6 and covers exactly the role's level codes; missing/empty `sources` or `why` = sourcing issue.
4. For each role with `derived: true`: regenerate via `render_role_ladder.py --force --out-dir <tmp>` and diff against the committed `ladder.md`/`ladder.csv`; any difference = HARD failure (both modes).
5. Warning lint: an `evidence` line for a mapping with `p` in {P1, P2, P3} containing any of `sets the standard`, `drives strategy`, `org-wide`, `other teams adopt` → printed as `WARN`, never fails.

- [ ] **Step 1: Write the failing test**

`tests/test_check_consistency_sourcing.py`:

```python
import os
import subprocess
import sys

ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
SCRIPT = os.path.join(ROOT, "scripts", "check_consistency.py")


def run(*flags):
    return subprocess.run([sys.executable, SCRIPT, *flags], capture_output=True, text=True)


def test_default_mode_reports_gaps_but_passes():
    res = run()
    assert res.returncode == 0, res.stdout
    assert "REPORT" in res.stdout            # ~2,724 unsourced catalog levels exist
    assert "unsourced capability levels" in res.stdout


def test_strict_mode_fails_on_gaps():
    res = run("--strict")
    assert res.returncode == 1
    assert "unsourced capability levels" in res.stdout


def test_em13_is_not_reported_unsourced():
    from check_consistency import sourcing_issues
    assert not any("EM-13" in issue for issue in sourcing_issues())
```

- [ ] **Step 2: Run test to verify it fails**

Run: `uv run --with pytest --with pyyaml --with openpyxl python -m pytest tests/test_check_consistency_sourcing.py -v`
Expected: FAIL — no `REPORT` output / no `sourcing_issues` / no `--strict` flag.

- [ ] **Step 3: Implement in `scripts/check_consistency.py`**

Add alongside the existing helpers (reusing its `ROOT`; keep the existing checks untouched):

```python
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
```

Wire into `main()` — parse `--strict` with argparse at the top of `main()`, then before the final error handling:

```python
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
```

- [ ] **Step 4: Run tests to verify they pass**

Run: `uv run --with pytest --with pyyaml --with openpyxl python -m pytest tests/test_check_consistency_sourcing.py -v`
Expected: 3 passed.

Run: `uv run --with openpyxl --with pyyaml python scripts/check_consistency.py`
Expected: exit 0; `REPORT` lines including `2724 unsourced capability levels (of 2730)` (numbers reflect the current 455-cap catalog; recompute if the catalog changed) and per-role `has no sources` / `empty why` reports from the Task 2 migration placeholders.

- [ ] **Step 5: Commit**

```bash
git add scripts/check_consistency.py tests/test_check_consistency_sourcing.py
git commit -m "feat(ci): sourcing checks with report/strict modes"
```

---

### Task 7: CI workflow wiring

**Files:**
- Modify: `.github/workflows/render.yml`

**Interfaces:**
- Consumes: Task 4 renderer, Task 6 validator flags.
- Produces: PR job renders derived ladders and diffs `.md` + `ladder.csv`; push job regenerates and commits them. Default (non-strict) validator until R4.

- [ ] **Step 1: Edit the PR `validate` job**

Replace the "Text renders must not be stale" run block with:

```yaml
      - name: Text renders must not be stale
        run: |
          python scripts/render_catalog.py
          python scripts/render_role_links.py
          python scripts/render_role_ladder.py
          if ! git diff --exit-code -- '*.md' 'roles/*/ladder.csv'; then
            echo '::error::Derived renders are stale. Run scripts/render_catalog.py, scripts/render_role_links.py and scripts/render_role_ladder.py, then commit the result.'
            exit 1
          fi
```

- [ ] **Step 2: Edit the push `regenerate` job**

In "Regenerate all derived renders" add `python scripts/render_role_ladder.py` after `render_role_links.py`, and in the commit step change the `git add` line to:

```yaml
          git add data/*.md data/capabilities.xlsx roles/*/ladder.md roles/*/ladder.csv roles/*/ladder.xlsx
```

Also add `data/bibliography.csv` and `data/capability_levels.csv` to the push-trigger `paths:` list.

- [ ] **Step 3: Validate the workflow file parses**

Run: `uv run --with pyyaml python -c "import yaml; yaml.safe_load(open('.github/workflows/render.yml')); print('yaml OK')"`
Expected: `yaml OK`

- [ ] **Step 4: Commit**

```bash
git add .github/workflows/render.yml
git commit -m "ci: render derived ladders and diff ladder.csv"
```

---

### Task 8: Normative rule into skills and PROMPT.md

**Files:**
- Modify: `skills/career-ladder/references/capability-framework.md`
- Modify: `skills/career-ladder/SKILL.md`
- Modify: `skills/create-canonical-role/SKILL.md`
- Modify: `PROMPT.md`

No code tests; the deliverable is exact text. The full normative rule text lives in the spec (`docs/superpowers/specs/2026-07-09-sourced-derivation-methodology-design.md` § "Normative rule") — copy it VERBATIM from there; do not paraphrase.

- [ ] **Step 1: `skills/career-ladder/references/capability-framework.md`**

Delete the calibration bullet (currently around lines 46–49):

> "- Calibrate cells against the capability's P1–P6 profile: … (IC guide: E1≈P1–P2, E2≈P2, E3≈P3, E4≈P4, E5≈P5, E6≈P6; manager levels similar on their axis). Where your cell and the P-profile disagree about the bar, flag it — either the cell is miscalibrated or the profile needs a PR."

Replace with a new `## Cell derivation and mapping (normative)` section containing the spec's full normative rule (all four subsections: Cell derivation rule, Mapping rule, Order of operations, Smells). Update the example `role.yaml` snippet in section 4 of that file to the new `mappings:`/`evidence:` schema (copy the schema example from the spec § "Data schema").

- [ ] **Step 2: `skills/career-ladder/SKILL.md`**

Where the skill describes writing ladder cells / building the matrix, add a short pointer (do not duplicate the full rule):

> **Cells are assembled, never authored.** Depth text is the catalog capability's profile at the mapped proficiency, verbatim; role flavor goes in a separate `Evidenced by` line; scope comes from the level's scope band. Every P-mapping and every catalog P-level carries a bibliography citation + a written why. Full rule: `references/capability-framework.md` § Cell derivation and mapping. Order of operations is a hard gate: bibliography sources first, competencies second, mappings third — cell prose never.

- [ ] **Step 3: `skills/create-canonical-role/SKILL.md`**

Add to the consolidation/minting flow (wherever canonical competencies are accepted):

> **Sourcing gate (hard):** a canonical competency cannot be minted unless its catalog capability has a fully sourced P1–P6 profile — one bibliography citation + why per level (`data/capability_levels.csv`). If the capability is new or unsourced, supplying those six sourced rows is part of the same change. Consolidation operates on capability IDs and per-level mappings, never on freshly written cell prose; ladder cells are rendered by `scripts/render_role_ladder.py`, not authored.

- [ ] **Step 4: `PROMPT.md`**

In Part 0, extend the fetch list with `data/bibliography.csv` and `data/capability_levels.csv` and state: when a role record exists, per-level cell text MUST be the catalog profile verbatim (bar), with role nuance only in a separate "Evidenced by" line. In Part 2, replace the cell-writing rules' first bullet ("Separate depth from scope in every cell...") intro with the assembled-cell structure (Bar / Evidenced by / Scope) and add: every proficiency mapping and every level behavior must carry a named, real, verifiable citation plus a one-to-two-sentence why; ladders produced without web access must say so and still list per-level sources from the author's knowledge, flagged for verification. Keep the rest of Part 2 (observable behaviors, cumulative, manager-track influence language) unchanged.

- [ ] **Step 5: Re-run the full test suite (guard against accidental script edits)**

Run: `uv run --with pytest --with pyyaml --with openpyxl python -m pytest tests/ -v`
Expected: all pass.

- [ ] **Step 6: Commit**

```bash
git add skills/career-ladder skills/create-canonical-role PROMPT.md
git commit -m "docs(skills): sourced derivation rule and gates"
```

---

### Task 9: End-to-end verification sweep

**Files:** none new — verification only.

- [ ] **Step 1: Full suite**

Run: `uv run --with pytest --with pyyaml --with openpyxl python -m pytest tests/ -v`
Expected: all tests pass (≈10).

- [ ] **Step 2: Validator both modes**

Run: `uv run --with openpyxl --with pyyaml python scripts/check_consistency.py`
Expected: exit 0, REPORT lines only (plus existing OK line).
Run: `uv run --with openpyxl --with pyyaml python scripts/check_consistency.py --strict; echo "exit=$?"`
Expected: `exit=1` (unsourced backlog is real until R2/R3).

- [ ] **Step 3: Render idempotency**

Run: `uv run --with openpyxl python scripts/render_catalog.py && git diff --stat -- data/`
Expected: no diff (renders committed in Task 3 are current).

- [ ] **Step 4: Confirm EM-13 golden path renders end-to-end**

Run: `grep -c "Why this level" data/capabilities.md`
Expected: `6` (exactly the EM-13 rows).

- [ ] **Step 5: Commit anything stray, then report**

`git status --short` must be clean. Report completion + the two follow-on plans below.

---

## Follow-on plans (write AFTER this plan lands; not tasks here)

- **R2 — catalog sourcing sweep plan:** research campaign filling `capability_levels.csv` for all 455 capabilities × P1–P6, domain-by-domain, multi-agent, every citation link-verified before entry; unresolvable levels → recalibration list → catalog amendments. Gate: `check_consistency.py` REPORT count for unsourced capability levels reaches 0.
- **R3 — role retrofit plan:** per role (PEM first): fill mapping `sources`/`why` per competency (checked individually, not pattern-applied), migrate salvageable old cell flavor into `evidence:` (instance-test), resolve `proposed` capabilities into the catalog, set `derived: true`, render, review diff. Gate per role: no REPORT lines for that role; derived staleness green.
- **R4 — enforce:** flip CI to `check_consistency.py --strict` (one-line render.yml change) once R2+R3 gates are green.
