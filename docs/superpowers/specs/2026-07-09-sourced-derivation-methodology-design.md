# Sourced derivation methodology — design

**Date:** 2026-07-09
**Status:** Approved pending user review
**Scope:** Full retrofit — catalog (455 capabilities × P1–P6), all 6 role ladders, generation skills/prompt, renderers, validator.

## Problem

Three related defects in the current framework:

1. **Catalog P-profiles are unsourced.** `data/capabilities.md` (e.g., EM-13, EM-17) states P1–P6
   behaviors with no citation justifying why a behavior sits at a level.
2. **Role-ladder P-mappings are unsourced template defaults.** Ladders map e.g. `EM-13: M1 → P2`
   with a competency-level anchor (Tuckman) but no rationale for why P2 is the M1 bar within that
   anchor. The manager-track pattern "M1≈P2 … M6≈P6" is applied as a convention, not checked
   per competency.
3. **Ladder cells are freshly authored prose, not derived from the catalog.** The
   platform-engineering-manager ladder's EM-13 cells do not match the catalog EM-13 P-profiles;
   the engineering-management ladder's do (the catalog was distilled from it). Two roles sharing
   EM-13 show different depth text for the same proficiency — the shared framework is not actually
   shared.

## Decisions (user-confirmed)

- **Full retrofit now** — entire catalog and all six role ladders, not just go-forward.
- **Cell fidelity:** cell = canonical catalog bar (verbatim) + optional role-specific
  "Evidenced by" line + scope clause. Identical capability+proficiency ⇒ identical bar text
  across roles.
- **Sourcing bar:** named citation per level — every catalog P-level profile and every role-level
  mapping cites ≥1 named external source (theory, empirical, standard, or published company
  ladder) plus a 1–2 sentence "why". Uncited = validator failure (after retrofit completes).
- **Source of truth:** structured, git-diffable files (`data/*.csv`, `roles/<slug>/role.yaml`).
  `ladder.md` / `ladder.csv` / `ladder.xlsx` are always rendered, never hand-edited. The xlsx
  render follows the `Engineering_Leadership_Ladder_2.xlsx` structure minus the Korn Ferry
  crosswalk tab: Overview, Competency Matrix (with "What it covers" and "Theory anchor & why"
  columns), Rating Template, Sources & Theory.

## Normative rule (lands verbatim in the skills and PROMPT.md)

### Cell derivation rule

A ladder cell is **assembled, never authored**. Every cell has exactly three parts, in order:

1. **Bar — canonical, verbatim.** The catalog capability's profile text at the mapped proficiency
   level, copied byte-for-byte from the catalog. Never paraphrase, never re-flavor, never blend
   adjacent levels. Two roles mapping the same capability at the same proficiency show
   **identical** bar text — that identity is the point of a shared framework.
2. **Evidenced by — role-specific, optional.** One sentence naming how the bar is observably met
   in *this* role's context. It must be an **instance** of the bar: same behavior, same autonomy
   level, role-specific artifact. ("New platform hire ships a paved-road change in their first
   sprint" instantiates "new hires ship in their first weeks.") It may narrow the bar to this
   role's work; it must never raise, lower, or extend it. **Test:** strip the role nouns — what
   remains must restate the bar's behavior at the bar's autonomy. If your evidence sentence
   describes designing systems others adopt while the bar says "runs independently," you haven't
   written evidence, you've discovered a wrong mapping. Fix the mapping.
3. **Scope.** The role level's scope band from `role.yaml`, stated as reach ("one platform
   team"), never as depth.

### Mapping rule

A proficiency mapping (`EM-13: M1 → P2`) is a **sourced claim, not a template default**:

- Before mapping, read the capability's full P1–P6 profile *and* the proficiency-scale
  definitions. The mapping asserts: "the industry-expected bar for this capability at this role
  level is exactly the Pk profile."
- Every mapping carries a bibliography `source` key and a `why` — one to two sentences connecting
  the source to that level (e.g., "First-line managers are expected to run onboarding
  independently, not design it: Tuckman's arc is led per-team at this level; playbook design
  across teams is the P4 behavior — see also GitLab EM vs Director requirements").
- A ladder-wide pattern ("manager tracks start at P2") is not a per-competency rationale. If the
  honest reason is a convention, cite the convention's source and say so — but check each
  competency against it; conventions have exceptions (the EM ladder already maps LI-01 M1 → P3,
  not P2).
- **If no catalog profile matches the real bar at this level, do not write custom cell text.**
  Either the catalog profile is miscalibrated — file a catalog amendment with sources in the same
  change — or the competency doesn't belong at that level in this ladder.

### Order of operations (hard gate)

Sources first, competencies second, mappings third, cells never:

1. Research and register sources as bibliography entries.
2. Admit a competency only when its catalog P1–P6 profile is fully sourced (one citation + why
   per level). Missing sourcing = supply it as a catalog change in the same PR, or the competency
   is out.
3. Choose per-level mappings, each with source + why.
4. Cells render mechanically from catalog + role.yaml. If you find yourself writing depth prose
   in a ladder, stop — you're either duplicating the catalog or contradicting it.

### Smells that mean you're winging it

- Cell text that doesn't appear in the catalog.
- The same P-row on every competency without per-competency checking.
- An "evidenced by" containing "designs / sets the standard / drives strategy" under a P2/P3 bar.
- A mapping rationale that restates the mapping ("M1 is P2 because M1s operate at P2").
- Writing cells before the bibliography exists.

## Data schema

### `data/bibliography.csv` (new)

`key,type,citation,link,notes`

- `key`: stable slug, e.g. `tuckman1965`, `gitlab-em-jd`, `sfia9`, `dora2023`.
- `type`: `theory | empirical | standard | company-ladder`.
- Every citation anywhere in the repo is a key into this file. Feeds every "Sources & Theory"
  render. Citations must be verified to exist (real work, real link where applicable) before the
  row is added.

### `data/capability_levels.csv` (new)

`capability_id,level,source_keys,why`

- One row per capability × P1–P6 (~2,730 rows at current catalog size).
- `source_keys`: semicolon-separated bibliography keys, ≥1 required.
- `why`: 1–2 sentences justifying why this behavior sits at this proficiency level per the
  cited source(s).
- Behavior text itself stays in `data/capabilities.csv` (unchanged shape); sourcing is a separate
  table for clean diffs and multi-source support. `render_catalog.py` joins both.

### `roles/<slug>/role.yaml` (extended)

Per-competency entry gains `mappings` (replacing the flat `proficiency` map) and optional
`evidence`; `anchor` becomes a bibliography key:

```yaml
- theme: Onboarding & team formation
  capability: EM-13
  key_area: People Leadership & Team Development
  key_attribute: Hiring & Team Composition
  anchor: tuckman1965
  mappings:
    M1: {p: P2, sources: [tuckman1965, gitlab-em-jd], why: "First-line manager runs onboarding independently per team; playbook design across teams is the P4 behavior."}
    M2: {p: P3, sources: [tuckman1965], why: "..."}
    M3: {p: P4, sources: [...], why: "..."}
    M4: {p: P4, sources: [...], why: "Same depth as M3 — the differentiation at M4 is scope (sub-org), not a deeper formation bar."}
    M5: {p: P5, sources: [...], why: "..."}
    M6: {p: P6, sources: [...], why: "..."}
  evidence:
    M1: "New platform hire ships a paved-road change in their first sprint."
```

### Derived artifacts (never hand-edited)

- `data/capabilities.md` / `.xlsx`: each P-profile line renders with citation(s) + why.
- `roles/<slug>/ladder.md`, `ladder.csv`: rendered from role.yaml + catalog. Cell = bar
  (verbatim catalog text) + "Evidenced by:" line (if present) + "Scope:" clause + mapping
  rationale with linked sources.
- `roles/<slug>/ladder.xlsx`: Overview / Competency Matrix (Key Area, Focus, #, Competency,
  What it covers, Theory anchor & why, one column per level) / Rating Template (kept from
  current render: self, manager, peer raters; 1–N level scale; range flag) / Sources & Theory
  (framework → source → grounds → link, from bibliography). No Korn Ferry crosswalk tab.

## Rendering & validation

### Renderers

- `render_catalog.py`: join `capabilities.csv` + `capability_levels.csv` + `bibliography.csv`;
  emit sourced `capabilities.md` / `.xlsx`.
- New `render_role_ladder.py` (or extension of existing scripts): emit `ladder.md` + `ladder.csv`
  from role.yaml + catalog — this is what makes cells mechanically derived.
- `render_role_xlsx.py`: updated to the example workbook structure above.
- CI continues to regenerate derived renders on merge (existing behavior).

### `check_consistency.py` — hard failures

1. Every capability × level in `capabilities.csv` has a `capability_levels.csv` row with ≥1
   source key and nonempty why.
2. Every source key (catalog, role.yaml anchors, mapping sources) resolves in
   `bibliography.csv`.
3. Every role.yaml mapping has `p`, `sources` (≥1), and nonempty `why`.
4. Rendered `ladder.md`/`ladder.csv`/`capabilities.md` are up to date (regenerate and diff —
   staleness is failure). Verbatim-bar integrity follows from rendering; the diff check makes
   hand edits to derived files impossible to land.
5. Existing structural checks (focus-area ≥2 competencies, unique triples, etc.) unchanged.

### `check_consistency.py` — warnings (human review, not mechanical failure)

- Evidence line under a P1–P3 bar containing above-bar markers ("sets the standard", "drives
  strategy", "org-wide", "other teams adopt").
- Mapping `why` that is shorter than ~8 words or repeats the mapping itself.

## Skill & prompt updates

- `skills/career-ladder/SKILL.md` + `references/capability-framework.md`: normative rule verbatim;
  remove/replace the "IC guide: E1≈P1–P2 … manager levels similar on their axis" calibration
  line (the template-default habit that produced unchecked flat P-rows).
- `skills/create-canonical-role`: consolidation gate — a canonical competency cannot be minted
  without a fully sourced P-profile; union/merge steps operate on capability IDs + mappings, not
  on freshly written cell prose.
- `PROMPT.md`: Part 0/2 updated so external generations fetch the bibliography and catalog and
  follow the derivation rule; ladders produced without repo access must still ship a Sources &
  Theory section with per-level citations.

## Retrofit plan (phased)

- **R1 — plumbing.** Bibliography file, `capability_levels.csv` (empty/partial), role.yaml schema
  migration (mechanical: `proficiency` → `mappings` with placeholder sources), renderers,
  validator in report-only mode.
- **R2 — catalog sourcing sweep.** All 455 capabilities × 6 levels, domain by domain (36
  domains), multi-agent research. Every citation verified to exist before entering the
  bibliography — no hallucinated sources. Levels with no defensible source are flagged into a
  recalibration list → catalog amendment (with sources) or profile rewrite; never silently
  invented.
- **R3 — role retrofit.** All six roles, PEM first (known-bad pilot), then
  engineering-management, platform-engineering, dairy-plant-operations, ai-engineer,
  full-stack-typescript, product-manager. Per role: rebuild mappings with sources + why
  (checking each competency, not applying the row pattern), migrate old cell flavor into
  `evidence:` lines where it passes the instance-test (discard where it doesn't), regenerate all
  derived artifacts.
- **R4 — enforce.** Flip validator to hard-fail; CI green required.

## Verification

- Validator green repo-wide with hard-fail on.
- PEM ladder EM-13 renders exactly the catalog P2/P3/P4/P4/P5/P6 texts as bars (the user's
  "should be" example), with role flavor surviving only as evidence lines.
- Random-sample citation audit (peer-review-style): fetched sources exist and support the `why`
  claims they're attached to.
- Grep-level check: no depth prose in any ladder that does not appear in the catalog.

## Out of scope

- Adding new roles or new catalog capabilities (beyond amendments the retrofit itself forces).
- Changing the P1–P6 scale definitions or level counts of existing ladders.
- The Korn Ferry crosswalk (explicitly excluded from the xlsx structure).
- Automated semantic verification of evidence lines (warning heuristics + human review only).
