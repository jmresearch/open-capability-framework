# Platform adoption & deprecation management

- **Proposed id:** OPS-33
- **Domain / focus area:** Systems, Infrastructure & Operations / Operating Mindset
- **Type:** Behavioral
- **Description:** Drives internal adoption of platform capabilities and manages the full lifecycle
  of platform surfaces — migration onto paved roads, long-tail burndown, and safe deprecation and
  sunsetting of what they replace.
- **Why it's missing:** The Platform Engineering Management ladder needs a competency for the
  adoption-and-migration half of platform-as-a-product work: moving internal users onto new
  capabilities, running codemod/automated-migration campaigns, burning down the long tail, and
  operating deprecation policy with credible sunset guarantees. The nearest existing ids do not
  cover it: **PM-10** (Metrics & product analytics) is measurement of impact, not the migration/
  deprecation program itself; **OPS-30** (Progressive Delivery & Release Safety) is per-release
  deploy safety (flags, canaries, rollback), not multi-quarter capability migration; **DR-03**
  (Developer marketing & evangelism) and **CSM-01/02** (customer onboarding & adoption) are outward,
  customer-facing adoption, not internal-platform migration. Adoption and deprecation are the
  load-bearing lifecycle behaviors that distinguish platform work from generic product delivery.

## P1–P6 behavioral profile

- **P1 (Assisted):** Executes assigned migration steps on a defined checklist; updates tracking as
  users move; escalates blockers surfaced during a rollout.
- **P2 (Independent):** Runs the adoption of a single capability end to end — communicates the
  change, provides migration tooling or docs, and clears the common blockers without help.
- **P3 (Proficient):** Owns a capability's adoption and deprecation as a program: sets migration
  tooling (codemods, automated rewrites), burns down the long tail, and enforces a deprecation
  policy with published timelines and support commitments.
- **P4 (Expert):** Designs the migration operating model a domain reuses — adoption instrumentation,
  incentives, and deprecation guarantees — so multiple teams retire and replace surfaces predictably.
- **P5 (Authority):** Sets the organization's adoption and deprecation standards: the sunset
  principles, the guarantee bar, and the mechanisms that keep the platform's surface area from
  sprawling as it grows.
- **P6 (Pioneer):** Establishes adoption-and-lifecycle practice others in the field adopt; makes
  deprecation a trusted, low-friction default rather than a feared event across the industry.
