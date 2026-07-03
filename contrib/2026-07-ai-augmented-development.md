# AI-augmented development judgment

- **Proposed id:** SWE-10            # next free number in Software Engineering
- **Domain / focus area:** Software Engineering / Code & Quality
- **Type:** Behavioral
- **Description:** Works effectively with AI coding tools and agents while remaining accountable for the output - calibrating what to delegate and what to hand-write, verifying generated changes with the same rigor as hand-written ones, and setting the review and provenance practices that keep quality intact.
- **Why it's missing:** The AI-engineer canonical role record (roles/ai-engineer) needs a ratable competency for working with AI coding tools and agents - all five consolidation sources carried it independently (DORA's 2024 State of DevOps AI-adoption findings anchor it). Nearest existing ids: SWE-01 (writing code) covers producing code, not the delegation/verification judgment; SWE-04 (code comprehension & review) covers reviewing code generally, not calibrating trust in machine-generated changes or setting provenance practice; QA-04 (risk-based & shift-left quality) is test prioritization; OPS-28 (automation-first operations) is operational toil elimination, not development delegation.

## P1-P6 behavioral profile

- **P1 (Assisted):** Uses AI coding tools with the output treated as a draft - reads every generated line, tests it, and can explain any part of the diff when asked.
- **P2 (Independent):** Calibrates when generation helps and when it misleads for the work at hand; catches plausible-but-wrong generated code before review, and their AI-assisted changes pass review at the same rate as hand-written ones.
- **P3 (Proficient):** Sets the norms for AI-assisted work in a domain - what may be delegated to agents, what verification it requires, how provenance is noted in review - and coaches others out of over-trust and under-use.
- **P4 (Expert):** Defines AI-assisted engineering practice across teams - where agents run in the delivery lifecycle, what gates their output - justified by throughput and defect data rather than vendor claims.
- **P5 (Authority):** Drives an organization's AI-augmented engineering strategy - tooling selection, workflow redesign, skill expectations - and adjusts policy from measured delivery outcomes.
- **P6 (Pioneer):** Shapes how software engineering itself changes with AI at company and industry level; a credible public voice on what changes and what doesn't.
