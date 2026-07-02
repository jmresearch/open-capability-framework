# Proposed capabilities — staging for catalog additions

New capabilities discovered while building ladders land here as PRs, one file per proposal, so
the curated catalog (`data/`, the workbook) only changes when a maintainer folds an accepted
proposal in. Role records may reference a pending proposal via `capability: proposed` +
`proposal_ref`.

## Proposal format (`contrib/<yyyy-mm>-<capability-slug>.md`)

```markdown
# <Capability name>

- **Proposed id:** EM-13            # next free number in the target domain
- **Domain / focus area:** Engineering Management / Culture & Change
- **Type:** Behavioral | Technical
- **Description:** <one line, technology-agnostic, in catalog voice>
- **Why it's missing:** <what ladder/role needed it and why no existing capability covers it —
  name the nearest existing ids and why they don't match>

## P1–P6 behavioral profile

- **P1 (Assisted):** ...
- **P2 (Independent):** ...
- **P3 (Proficient):** ...
- **P4 (Expert):** ...
- **P5 (Authority):** ...
- **P6 (Pioneer):** ...
```

## Amendment format (`contrib/<yyyy-mm>-amend-<capability-id>.md`)

Proposals may also MODIFY an existing capability — refine a description, recalibrate a P-profile,
or split a capability whose description spans two assessable things:

```markdown
# Amend <ID>: <capability name>

- **Type:** description | profile | split | merge
- **Why:** <what surfaced the problem — name the role record or ladder run>
- **Current:** <the field(s) as they stand>
- **Proposed:** <the field(s) as they should read; for a split, the two full replacement rows
  with proposed ids and P1–P6 profiles>
- **Affected role records:** <roles/<slug> entries referencing this id, and how they change>
```

## Maintainer acceptance checklist

On accepting any proposal: assign/confirm the final id; apply the row change to
`data/capabilities.csv` AND `data/capabilities.json`; update the workbook
(`Open_Capability_Framework.xlsx`) or queue it for the next workbook regeneration; update every
role record that referenced the proposal (`capability: proposed` → the real id, or re-pointed ids
for a split); update `data/domains.csv` counts if the capability count changed; delete the
proposal file. Reject with a short note in the PR rather than silently closing.

Requirements: technology-agnostic ("relational data modeling", never "PostgreSQL"); described by
the competence needed, not a tool; six genuinely distinct proficiency bars in the catalog's
observable register; no organization-specific content. On acceptance, a maintainer assigns the
final id, adds the row to `data/capabilities.csv` / `.json` and the workbook, updates any role
records that referenced the proposal, and deletes the proposal file.
