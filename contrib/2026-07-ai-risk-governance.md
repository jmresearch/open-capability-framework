# AI risk assessment & governance

- **Proposed id:** AI-21             # next free number in AI & ML Engineering
- **Domain / focus area:** AI & ML Engineering / AI Quality & Safety
- **Type:** Behavioral
- **Description:** Assesses and governs the risk of AI systems through their lifecycle - classifying systems against recognized risk frameworks, converting findings into engineering requirements with owners, and keeping the evidence trail (evals, controls, incidents) audit-ready as systems and regulation change.
- **Why it's missing:** The AI-engineer canonical role record (roles/ai-engineer) needs a ratable competency for AI risk assessment and governance, carried by four of the five consolidation sources (anchored on NIST AI RMF 1.0 and the EU AI Act). Nearest existing ids: AI-05 (responsible AI & guardrails) is designing safe model behavior, not the assessment/governance/compliance discipline around it; AI-15 (bias, fairness & error analysis) is investigation of model errors, not lifecycle governance; OPS-09 (privacy & compliance engineering) covers privacy/audit controls generally but not AI-specific risk classification, impact assessment, and evidence packs; SEC-15 (security governance, risk & policy) and RISK-08 (policy & standards governance) are security- and enterprise-policy governance, not engineering practice for AI systems.

## P1-P6 behavioral profile

- **P1 (Assisted):** Completes the risk checklist for their change accurately - identifying who is affected if the model is wrong - and escalates anything the checklist doesn't cover.
- **P2 (Independent):** Assesses a feature's failure impact before build (misuse, error harm, disparate performance across user groups) and documents mitigations and residual risk unprompted.
- **P3 (Proficient):** Classifies a domain against the applicable risk framework, keeps its evidence pack (evals, controls, incidents) audit-ready, converts findings into engineering requirements with owners, and flags when a product change alters the risk class.
- **P4 (Expert):** Operates a cross-team AI risk-review process - fast enough that teams use it honestly, rigorous enough to catch real issues - and builds governance tooling that makes compliance a byproduct of normal engineering.
- **P5 (Authority):** Owns an organization's AI governance program jointly with legal and risk functions, translating regulation into engineering requirements without freezing delivery.
- **P6 (Pioneer):** Positions a company ahead of AI regulation; accountable to executives, boards, and regulators for where the risk lines are drawn.
