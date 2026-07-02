# Role records — canonical ladders as capability references

A role record pins the *structure* of a career ladder — which capabilities a role requires, what
the ladder rows are called, and the minimum proficiency per level — so any tool (or person)
building a ladder for that role starts from the same canon instead of re-deriving it. Cell prose
stays free to be org-calibrated; the territory and naming do not drift.

## Layout

```
roles/
└── <role-slug>/            # kebab-case, e.g. engineering-management
    ├── role.yaml           # the record (required)
    ├── ladder.md           # canonical rendering with full per-level prose (optional)
    └── ladder.csv          # skill-matrix-importable rendering (optional)
```

## `role.yaml` schema

```yaml
role: Engineering Management        # display name
slug: engineering-management        # = directory name
variant: manager                    # ic_technical | manager | general
scope_note: >                       # optional, e.g. how levels map to S1-S6
  M1-M6 map to scope S1-S6 on the leadership axis.
levels:
  - {code: M1, title: Engineering Manager, scope: one team, focus: leading one team directly}
  # ... one entry per level, in order (max 7)
competencies:
  - theme: Team health & engagement       # ladder row label, <=60 chars
    capability: EM-03                     # catalog id; or "proposed" + proposal_ref
    key_area: People & Talent             # ladder grouping (top tier)
    key_attribute: Team Health & Culture  # ladder grouping (middle tier)
    anchor: "Edmondson, The Fearless Organization (2018)"   # citable theory anchor
    proficiency: {M1: P2, M2: P3, M3: P3, M4: P4, M5: P5, M6: P6}
  - theme: Executive communication
    capability: proposed
    proposal_ref: contrib/2026-07-executive-communication.md   # pending catalog addition
    # ...
```

Rules:

- Every competency references a catalog capability by id, or `proposed` with a `proposal_ref`
  pointing at the pending addition under `contrib/`. When a proposal is accepted into `data/`,
  update the reference to the real id.
- `key_area` → `key_attribute` → `theme` is a genuine three-tier nesting; every key_attribute
  spans two or more themes.
- Proficiency values use the framework's P1–P6 scale; levels use the role's own codes.

## Contributing

Role records arrive as PRs — typically opened (with the contributor's explicit permission) by
tools that generate ladders from this framework, such as
[jmresearch-career-skills](https://github.com/jmresearch/jmresearch-career-skills). Contributions
must be **generic**: no organization names, internal systems, org-specific compliance regimes, or
headcounts. Updates to an existing record (new competencies, refined proficiency targets) are
welcome as focused diffs — the more ladders flow through, the more canonical the records get.
