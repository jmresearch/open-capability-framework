# Cognitive-load management & abstraction design

- **Proposed id:** OPS-32            # next free number in Systems, Infrastructure & Operations
- **Domain / focus area:** Systems, Infrastructure & Operations / Operating Mindset
- **Type:** Behavioral
- **Description:** Designs tooling, interfaces, and abstractions to minimize the extraneous cognitive load imposed on the teams that consume them - deciding deliberately what consumers must and must not need to know, and measuring the load imposed.
- **Why it's missing:** The platform-engineering canonical role record (roles/platform-engineering) treats cognitive-load reduction as a first-class, ratable competency (Team Topologies applying Sweller's cognitive load theory) - all five consolidation sources carried it independently. Nearest existing ids: OPS-27 (platform & developer-experience engineering) covers building the platform surface but not the load-budgeting discipline of what users are forced to know; UX-02 (information architecture) is content structuring for end-user products; DR-02 (developer experience & feedback loops) covers gathering feedback, not designing abstractions around load.

## P1-P6 behavioral profile

- **P1 (Assisted):** Names the exact docs, errors, and setup steps that forced them to understand internals a consumer should not need, and files concrete simplification issues.
- **P2 (Independent):** Reduces the concepts and steps a consumer must hold to use their component - collapsing configuration, defaulting decisions, rewriting errors to say what to do next - and shows the before/after.
- **P3 (Proficient):** Designs a capability's abstractions around what consumers must not have to know, so a first-time user succeeds without reading internals; measures load with time-to-first-success and support-ticket themes and treats regressions as defects.
- **P4 (Expert):** Audits cognitive load across team boundaries - quantifying onboarding time, concepts-to-learn, and ticket themes - and drives the cross-boundary simplifications no single team could make.
- **P5 (Authority):** Makes cognitive load a first-class organizational measure with explicit load budgets, vetoing designs that externalize complexity onto consuming teams.
- **P6 (Pioneer):** Shapes company-level technology and team-boundary choices explicitly around team cognitive load, arguing for fewer, deeper abstractions over sprawling optionality.
