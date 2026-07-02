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

Requirements: technology-agnostic ("relational data modeling", never "PostgreSQL"); described by
the competence needed, not a tool; six genuinely distinct proficiency bars in the catalog's
observable register; no organization-specific content. On acceptance, a maintainer assigns the
final id, adds the row to `data/capabilities.csv` / `.json` and the workbook, updates any role
records that referenced the proposal, and deletes the proposal file.
