# Guardrails & policy as code

- **Proposed id:** SEC-18            # next free number in Security Engineering
- **Domain / focus area:** Security Engineering / Defensive Security
- **Type:** Technical
- **Description:** Encodes preventive controls as versioned, tested, automatically enforced policy - admission checks, pipeline gates, configuration rules - with actionable violation messages and governed exception paths, so the safe way is the default way.
- **Why it's missing:** The platform-engineering canonical role record (roles/platform-engineering) needs a ratable competency for policy-as-code guardrail engineering, carried by all five consolidation sources. Nearest existing ids: SEC-04 (zero-trust & policy-based access control) is authorization-decision policy, not build/deploy/configuration guardrails; SEC-08 (security hardening & baseline configuration) covers hardening baselines but not encoding policy as tested code with exception workflows; SEC-15 (security governance, risk & policy) is organizational policy framing, not its engineering enforcement; RISK-08 (policy & standards governance) is corporate-governance-level.

## P1-P6 behavioral profile

- **P1 (Assisted):** Works within existing guardrails, reads a policy violation to its cause instead of requesting an exception, and explains what each guardrail protects against.
- **P2 (Independent):** Writes and tests policy rules for a component - admission checks, pipeline gates - with low false-positive rates and violation messages that tell the user how to comply.
- **P3 (Proficient):** Designs the guardrail architecture for a capability - what is blocked, warned, or audited, with documented threat reasoning - tuned so the safe path is the fast path, and runs an audited exception workflow without becoming the bottleneck.
- **P4 (Expert):** Harmonizes policy across teams into a coherent, versioned policy library with a governed exception process, and adjudicates escalated safety-versus-velocity disputes.
- **P5 (Authority):** Owns an organization's preventive-control strategy with security partners - the control catalog, its coverage, and the evidence it works - moving enforcement from review-time to platform-time.
- **P6 (Pioneer):** Sets an organization-defining balance of enablement and control, accountable for guardrails that hold under audit and attack without throttling delivery.
