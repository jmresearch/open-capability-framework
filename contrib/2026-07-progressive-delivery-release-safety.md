# Progressive delivery & release safety

- **Proposed id:** OPS-30
- **Domain / focus area:** DevOps, Platform & Cloud / Operations
- **Type:** Technical
- **Description:** Manages how change reaches production safely — decoupling deploy from release with feature flags, staged and canary rollouts, rollback readiness, and migration sequencing that bounds the blast radius of every change.
- **Why it's missing:** Four of five runs of the full-stack-typescript canonical consolidation carried release/deployment practice as a competency distinct from pipeline engineering (anchor: Continuous Delivery, Humble & Farley). OPS-02 (CI/CD & Delivery Engineering) covers building the pipeline mechanics; OPS-13 (Environment & release promotion strategy) covers environment parity and promotion paths; neither covers the risk-management practice of progressive exposure, flag lifecycle, canary analysis, rollback judgment, and deploy-order choreography for live systems.

## P1–P6 behavioral profile

- **P1 (Assisted):** Follows the release process exactly — flags, staged rollout steps, verification checklists — verifies their change in production, and rolls back with guidance.
- **P2 (Independent):** Ships behind flags with a rollback plan by default, monitors rollouts and reverts on their own judgment when signals degrade, and writes changes that tolerate both versions running during rollout.
- **P3 (Proficient):** Designs the rollout for risky changes — canary criteria, migration sequencing, flag lifecycle, kill switches — and reviews others' rollout plans for blast radius; the person teams ask how to ship something safely.
- **P4 (Expert):** Builds progressive-delivery machinery multiple teams release through (flag platforms, automated canary analysis, automated rollback), retiring deploy patterns that cause repeat incidents and measurably raising deploy frequency.
- **P5 (Authority):** Owns release policy for an organization and its delivery metrics — rollout standards, freeze rules, environment strategy — dismantling ceremony that adds no safety.
- **P6 (Pioneer):** Sets how an entire company's software reaches customers — the risk posture products ship under — and defends it to executives, auditors, and regulators.
