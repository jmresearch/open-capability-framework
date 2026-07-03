# AI Engineer - Canonical Career Ladder

## Calibration summary

- **Provenance:** canonical consolidation of six independent same-methodology sources (blind runs ai-r1 ... ai-r4, a supplementary blind run ai-r5 commissioned after a singleton-rate flag, and an earlier trusted same-methodology ladder for this role; 180 source competencies) by **union, not intersection** - every genuinely distinct competency from any source survives; nothing was voted out. Semantic duplicates were merged into single canonical competencies (clearest technology-agnostic name, strongest citable anchor, best observable cell content). Minted 2026-07-02.
- **Variant:** ic_technical (individual-contributor technical track).
- **Levels:** six, E1-E6 - Associate AI Engineer -> AI Engineer -> Senior AI Engineer -> Staff AI Engineer -> Senior Staff AI Engineer -> Principal AI Engineer.
- **Scope bands:** task (E1) -> component (E2) -> capability/domain (E3) -> multiple teams (E4) -> organization (E5) -> company (E6), following Google L3-L8 / Meta E3-E8 norms via levels.fyi, with StaffEng (Larson) grounding E4-E6 behaviors.
- **Terminal level: E3 / Senior.** All six sources agree: a strong AI engineer can remain at E3 indefinitely without being behind. E4+ is not 'more of E3' - it is a different job defined by multi-team scope, standard-setting, and organizational leverage.
- **Register:** CircleCI Engineering Competency Matrix - present-tense observable behaviors; Depth and Scope separated in every cell.
- **Shape:** 7 key areas, 17 focus areas, 43 competencies; every focus area spans 2+ competencies; theme labels are under 60 characters and technology- and model-vendor-agnostic.
- **OCF mapping:** every competency carries an Open Capability Framework reference - 41 map to existing catalog capabilities (using 10 of the 20 AI-domain capabilities, plus SWE, BE, OPS, QA, CC, LI, and PD ids, including the newly minted OPS-30 progressive delivery & release safety carried by Incremental delivery & de-risking) and 2 are proposed additions (AI-augmented development judgment -> SWE-10 candidate; AI risk assessment & governance -> AI-21 candidate) staged under contrib/. AI-01, AI-02, AI-05 (two rows each) and AI-03 (three rows) are flagged as future split candidates rather than forcing weaker distinct mappings.
- **Consolidation judgment calls:** (1) The trusted source's coding-vs-quality split survives under the union rule: Coding & implementation (SWE-01) is distinct from Code quality & review (SWE-02). (2) Blended source rows were assigned to the concept their cell content leans toward: the trusted source's 'LLM Integration & Prompt Engineering' to Prompt design & iteration, 'Context & Retrieval Engineering' to Retrieval & grounding pipelines, 'Agentic Systems & Tool Orchestration' to Agent architecture & orchestration, 'APIs, Services & Infrastructure' to API & service design, 'Privacy & Compliance' to AI risk assessment & governance, 'Problem Solving & Technical Judgment' to Problem framing & solution fit, and r2's 'Mentoring & technical leadership' to Mentoring & knowledge sharing. (3) r1's guardrails/harm split survives: Guardrails & output safety (control mechanisms) and Harm mitigation & safety behavior (harm profiling) are separate rows. (4) Production feedback loops and drift monitoring merged into one competency - all four carriers tie feedback signals and drift detection into the same loop. (5) Single-source competencies (Coding & implementation, Embeddings & semantic search, Harm mitigation & safety behavior, Provider & capacity management, Incremental delivery & de-risking, Ownership & delivery accountability) all survive as distinct rows per the union rule. (6) Names are technology- and model-vendor-agnostic; 'Retrieval & RAG pipelines' was generalized to 'Retrieval & grounding pipelines'. (7) The supplementary run ai-r5 (commissioned after the singleton-rate flag) corroborated the r1-only Harm mitigation & safety behavior row (its 'Harm assessment & release judgment' merged in, contributing the written ship/hold-recommendation bar at E3) and contributed four genuinely new competencies under the union rule: Debugging & systems diagnosis (SWE-06), Structured output & schema design (SWE-09), Agent containment & blast-radius control (AI-03), and Documentation & knowledge sharing (CC-02); its blended rows were assigned by content lean ('Tool orchestration & control flow' -> Agent architecture & orchestration; 'Token economics & performance' -> Token economics & cost optimization; 'Model & build-vs-buy judgment' -> Model selection & integration; 'Explaining model behavior to stakeholders' -> Technical communication & writing).

## Level overview

| Level | Title | Scope band | Focus |
|---|---|---|---|
| E1 | Associate AI Engineer | task | Learns the AI stack and ships well-scoped tasks with guidance |
| E2 | AI Engineer | component | Owns model-backed components end to end, independently |
| E3 | Senior AI Engineer | capability / domain - **terminal level** | Owns an AI capability; the quality bar for a domain; terminal level |
| E4 | Staff AI Engineer | multiple teams | Sets patterns and standards multiple teams build against |
| E5 | Senior Staff AI Engineer | organization | Drives org-wide AI engineering strategy |
| E6 | Principal AI Engineer | company | Sets company-level technical direction for AI |

**Terminal level - E3 / Senior.** Sustained excellence at E3 is a complete, respected career, not a waypoint. Progression beyond E3 is opt-in and changes the nature of the job from building the thing to aligning the people and systems around the thing.

## Competency matrix

Each cell separates **Depth** (mastery of the skill) from **Scope** (how far the work reaches). Cells are present-tense behaviors observable by peers, leaders, and stakeholders.

---

## Software Engineering Craft

### Design & Architecture

#### System design & architecture

*Anchor:* Kleppmann, *Designing Data-Intensive Applications* (2017) - *Why:* AI features live inside distributed systems; the data-flow and consistency trade-offs are the load-bearing design decisions.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [SWE-05](../../data/capabilities.md#swe-05) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **explains the system's architecture in their own words** and implements designs specified by others, asking when a boundary is unclear - including where model calls sit in the request path and why they are isolated behind interfaces. Scope: a task within an existing design.
- **E2** - Depth: **designs a component and writes the short design note for it**, naming at least one alternative considered; isolates model calls behind clear interfaces and uses established patterns correctly. Scope: a component and its immediate neighbors.
- **E3** - Depth: **selects patterns by trade-off in design docs that name the alternatives and failure modes**, designing for evolution - swappable models, versioned prompts, isolated nondeterminism - and catches coupling and scaling problems in others' designs before build. Scope: owns architecture for an AI capability and runs its design reviews.
- **E4** - Depth: **writes the reference architectures other teams instantiate** and arbitrates cross-team design disputes with written trade-off analysis. Scope: multiple teams build against their designs.
- **E5** - Depth: **sets the architectural direction for AI systems across the org**, retiring dead-end patterns explicitly and removing the systemic obstacles that block the target state. Scope: organization.
- **E6** - Depth: **defines the company's long-horizon technical bets for AI systems** - build vs. buy, platform vs. product - in writing executives and engineers both act on. Scope: company.

#### API & service design

*Anchor:* Bloch, "How to Design a Good API and Why It Matters" (2006) - *Why:* AI features leak nondeterminism to consumers unless the contract deliberately contains it.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [SWE-07](../../data/capabilities.md#swe-07) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **implements endpoints to an existing API contract**, including error responses, and flags mismatches between spec and behavior. Scope: single endpoints.
- **E2** - Depth: **designs the API surface for a component** - versioning, streaming semantics, and explicit error shapes for model failures included - and documents it well enough that a consumer needs no walkthrough. Scope: a component's consumers.
- **E3** - Depth: **designs contracts that isolate consumers from model and provider changes** - streaming, partial failure, and nondeterminism handled explicitly in the interface - and rejects designs that leak provider details or raw model output to callers. Scope: the APIs of a capability; reviews neighbors' contracts.
- **E4** - Depth: **sets the API conventions multiple teams follow for model-backed services** and retires inconsistent legacy surfaces with migration paths. Scope: multiple teams.
- **E5** - Depth: **drives the org's interface strategy** - which capabilities become shared platforms, and the deprecation policy that keeps the surface coherent. Scope: organization.
- **E6** - Depth: **shapes the company's external and partner-facing AI interfaces**, balancing product commitments against provider volatility. Scope: company and ecosystem.

### Code Craft & Implementation

#### Coding & implementation

*Anchor:* McConnell, *Code Complete* (2nd ed., 2004) - *Why:* AI code is still code; implementation depth is the base layer the rest of the ladder stands on.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [SWE-01](../../data/capabilities.md#swe-01) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **writes working, readable code in the team's primary language** and debugs their own changes to root cause before asking for help. Scope: small changes delivered with review and guidance.
- **E2** - Depth: **implements features of moderate complexity independently**, handling error paths, async patterns, and concurrency basics correctly in idiomatic code. Scope: a component.
- **E3** - Depth: **writes code others use as the reference for the stack** and debugs the hard problems - race conditions, memory pressure, nondeterministic failures - that stall teammates. Scope: raises implementation quality across a capability.
- **E4** - Depth: **solves the implementation problems other teams can't**, working across multiple stacks and paradigms, and lands the patterns they use as shared libraries. Scope: multiple teams.
- **E5** - Depth: **anticipates where implementations break at scale** and shapes org-wide engineering practice through visible, load-bearing code. Scope: organization.
- **E6** - Depth: **authors foundational primitives used company-wide** and is the benchmark for implementation depth. Scope: company.

#### Code quality & review

*Anchor:* Winters, Manshreck & Wright, *Software Engineering at Google* (2020) - *Why:* review is where a team's quality bar is actually enforced, and AI-generated code raises the volume it must absorb.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [SWE-02](../../data/capabilities.md#swe-02) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **submits small, reviewable changes that pass CI first try more often than not** and responds to review feedback by fixing the pattern, not just the line. Scope: their own changes.
- **E2** - Depth: **reviews peers' changes with substantive comments** - correctness, naming, missed edge cases - and keeps the code they touch consistently readable, separating prototype code from production paths without being told. Scope: a component's codebase.
- **E3** - Depth: **holds the quality bar in review for a whole domain**, including AI-generated code, articulating why a change is risky rather than just that it is, and pays down debt deliberately rather than opportunistically. Scope: a capability; the reviewer others request.
- **E4** - Depth: **codifies review and code-health standards multiple teams adopt** - lint rules, prompt-versioning conventions, review norms - and measurably reduces defect escape in the areas they steward. Scope: multiple teams.
- **E5** - Depth: **changes how the org reviews and maintains code** - tooling, norms, and the standards for machine-authored changes. Scope: organization.
- **E6** - Depth: **sets the company's engineering quality bar**, cited when quality trade-offs reach executive decisions. Scope: company.

#### Debugging & systems diagnosis

*Anchor:* Agans, *Debugging: The 9 Indispensable Rules* (2002) - *Why:* model-backed systems add nondeterminism on top of ordinary bugs; disciplined fault isolation is what separates the two.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [SWE-06](../../data/capabilities.md#swe-06) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **reproduces a reported bug and bisects it to a candidate cause with guidance**, reading logs and stack traces before asking for help. Scope: bugs in their own tasks.
- **E2** - Depth: **isolates faults across service boundaries unaided**, distinguishing deterministic code bugs from model-behavior variance before escalating. Scope: their component and its direct dependencies.
- **E3** - Depth: **debugs the hardest failures in a capability, including intermittent model-dependent ones**, and writes the reproduction others rerun. Scope: a capability; teammates bring them the stuck cases.
- **E4** - Depth: **untangles cross-team failures where no single owner sees the whole path** and leaves behind the instrumentation that makes the next one cheap. Scope: multiple teams' systems.
- **E5** - Depth: **spots systemic failure classes from incident patterns across the org** and drives the architectural fixes. Scope: organization.
- **E6** - Depth: **is the debugger of last resort for company-critical AI incidents** and turns each into a durable prevention mechanism. Scope: company.

### Testing & AI-Assisted Development

#### Deterministic tests vs evals

*Anchor:* Vocke, "The Practical Test Pyramid" (martinfowler.com, 2018); Husain, "Your AI Product Needs Evals" (2024) - *Why:* LLM systems need two verification regimes - deterministic tests for code paths, statistical evals for model behavior - and confusing them breaks both.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [SWE-03](../../data/capabilities.md#swe-03) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **writes unit tests for the deterministic parts of a change** - parsing, templating, tool schemas - and can say which behaviors are testable versus eval-able when asked. Scope: their task.
- **E2** - Depth: **draws the test/eval boundary correctly for a component** - mocks model calls in unit tests, routes behavioral claims to evals - and keeps CI fast and free of flaky model-dependent assertions. Scope: a component's test suite.
- **E3** - Depth: **designs the verification strategy for a capability** - what runs in CI, what runs as evals, what only production monitoring can catch - and rejects flaky model-in-the-loop tests in review with a stated rule. Scope: a capability; the split they define is what teammates follow.
- **E4** - Depth: **standardizes the test-vs-eval discipline across teams** with shared fixtures, replay harnesses, and CI policy for what may block a merge. Scope: multiple teams' pipelines.
- **E5** - Depth: **owns the org's verification strategy for AI systems**, funding the harnesses that make the right split cheap and killing the theater. Scope: organization.
- **E6** - Depth: **sets company policy for what 'verified' means for AI products**, traceable from CI to eval to production evidence. Scope: company.

#### AI-augmented development judgment

*Anchor:* DORA, *Accelerate State of DevOps Report* (2024), AI adoption findings - *Why:* AI assistance boosts throughput but hurts stability without verification discipline; knowing when not to trust the tool is the durable skill.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [proposed](../../contrib/2026-07-ai-augmented-development.md) (SWE-10 candidate) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **uses AI coding tools with the output treated as a draft** - reads every generated line, tests it, and can explain any part of the diff when asked. Scope: their own tasks.
- **E2** - Depth: **calibrates when generation helps and when it misleads** - boilerplate yes, subtle invariants no - and catches plausible-but-wrong generated code before review; their AI-assisted diffs pass review at the same rate as hand-written ones. Scope: a component's workflow.
- **E3** - Depth: **sets the norms for AI-assisted work on their capability** - what may be delegated, what review it requires, how provenance shows up - and coaches others out of over-trust and under-use. Scope: a capability's development practice.
- **E4** - Depth: **defines AI-assisted engineering practice across teams** - where agents run in the delivery lifecycle, what gates their output - backed by throughput and defect data, not vendor claims. Scope: multiple teams.
- **E5** - Depth: **drives the org's AI-augmented engineering strategy**, selecting tooling, measuring its effect on delivery outcomes, and adjusting policy from the data. Scope: organization.
- **E6** - Depth: **shapes how the company builds software in the AI era** and is the credible voice on what changes and what doesn't. Scope: company.

## LLM Integration & Context Engineering

### Model Integration & Prompting

#### Prompt design & iteration

*Anchor:* Anthropic and OpenAI prompt-engineering guides (2023-2025) - *Why:* prompts are load-bearing program text; versioned, tested iteration is what separates engineering from folklore.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [AI-01](../../data/capabilities.md#ai-01) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **makes targeted edits to existing prompts and verifies the effect against known cases before committing**, following the team's prompt-versioning convention. Scope: single prompts within a task.
- **E2** - Depth: **writes production prompts from scratch** - role, constraints, output schema, few-shot examples - and iterates against a saved sample set rather than one lucky output. Scope: a component's prompts.
- **E3** - Depth: **treats prompts as versioned, eval-gated artifacts**; diagnoses failures to the responsible prompt section, documents why each instruction exists, and knows when the fix is retrieval or tooling, not wording. Scope: a capability; teammates adopt their prompt patterns.
- **E4** - Depth: **establishes prompt-engineering standards across teams** - templates, review checklists, migration playbooks for model changes - and untangles the prompt failures others are stuck on. Scope: multiple teams.
- **E5** - Depth: **drives org-wide prompt and context craft**, deciding where prompting ends and fine-tuning or tool-building begins, and re-baselining systematically when providers ship new models. Scope: organization.
- **E6** - Depth: **represents the state of the art to the company**, resetting practice when model generations obsolete current techniques. Scope: company and industry.

#### Model selection & integration

*Anchor:* Huyen, *AI Engineering* (2025) - *Why:* model choice is an engineering trade-off across quality, latency, cost, and provider risk - not a leaderboard beauty contest.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [AI-01](../../data/capabilities.md#ai-01) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **integrates a specified model through the team's client layer** - auth, retries, timeouts, streaming - per existing patterns. Scope: one integration point.
- **E2** - Depth: **runs a small structured comparison before picking a model for a feature** - quality on real samples, latency, price - and records the result; handles provider quirks in code, not tribal knowledge. Scope: a component.
- **E3** - Depth: **owns model choice for a capability** - including fine-tune vs. prompt vs. retrieval trade-offs - re-benchmarks when providers ship new models, and swaps models behind stable interfaces without consumer churn. Scope: a capability; their comparisons are reused by others.
- **E4** - Depth: **defines the model-selection playbook and abstraction layers multiple teams use**, making provider swaps routine instead of rewrites. Scope: multiple teams.
- **E5** - Depth: **sets the org's model portfolio strategy** - hosted vs. self-hosted, single vs. multi-provider - with cost and risk analysis leadership signs off on. Scope: organization.
- **E6** - Depth: **owns the company's model-sourcing strategy and its biggest bets** - build, fine-tune, or buy - and negotiates the strategic provider commitments behind them. Scope: company.

#### Structured output & schema design

*Anchor:* Schick et al., "Toolformer: Language Models Can Teach Themselves to Use Tools" (2023) - *Why:* the schema is the contract between probabilistic text and deterministic code; weak schemas turn model noise into system bugs.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [SWE-09](../../data/capabilities.md#swe-09) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **validates model outputs against a given schema and handles rejects** rather than trusting parses. Scope: one integration point.
- **E2** - Depth: **designs output schemas and tool signatures the model reliably satisfies**, measuring parse and validation failure rates. Scope: a component's model I/O.
- **E3** - Depth: **owns the structured-I/O layer for a capability** - schema evolution, repair strategies, when to constrain decoding versus post-validate - with failure rates on a dashboard. Scope: a capability; teams copy their schema patterns.
- **E4** - Depth: **sets cross-team standards for tool definitions and output contracts**, and audits integrations that skip them. Scope: multiple teams.
- **E5** - Depth: **owns the org's model-I/O reliability strategy**, driving shared validation infrastructure. Scope: organization.
- **E6** - Depth: **defines company-wide norms for machine-actionable model output**, including what external partners may depend on. Scope: company.

### Retrieval & Context

#### Retrieval & grounding pipelines

*Anchor:* Lewis et al., "Retrieval-Augmented Generation for Knowledge-Intensive NLP Tasks" (NeurIPS 2020) - *Why:* most production quality problems in knowledge features are retrieval problems wearing a model costume.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [AI-02](../../data/capabilities.md#ai-02) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **runs and modifies an existing ingestion/retrieval pipeline** - chunking, embedding, indexing - and verifies retrieval hits by inspection. Scope: a task.
- **E2** - Depth: **builds a retrieval pipeline for a corpus end to end** and measures retrieval quality (recall on labeled queries) separately from answer quality. Scope: a component.
- **E3** - Depth: **diagnoses failures to the responsible stage** - chunking, embedding, ranking, or synthesis - with evidence, and chooses hybrid, re-ranking, or structured-lookup strategies by measured trade-off, owning the ingestion, indexing, and freshness story. Scope: owns retrieval for a capability.
- **E4** - Depth: **designs the retrieval architecture several teams share** - index topology, freshness SLAs, evaluation harness - and consolidates duplicated pipelines into shared infrastructure. Scope: multiple teams.
- **E5** - Depth: **sets the org's knowledge-grounding strategy** - what corpora exist, who owns them, entitlement-aware access, and quality accountability. Scope: organization.
- **E6** - Depth: **decides company-level grounding bets** - proprietary-data moats, retrieval vs. long-context vs. fine-tuning - and owns that thesis with executives. Scope: company.

#### Embeddings & semantic search

*Anchor:* Reimers & Gurevych, "Sentence-BERT" (EMNLP 2019) - *Why:* embedding choices silently cap retrieval quality; they must be treated as tunable, evaluable components.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [AI-02](../../data/capabilities.md#ai-02) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **generates and stores embeddings using the team's pipeline** and explains what an embedding represents in plain language. Scope: embedding tasks within a pipeline.
- **E2** - Depth: **evaluates embedding models against the team's retrieval benchmarks** and tunes similarity thresholds and index parameters with evidence. Scope: the embedding layer of a component.
- **E3** - Depth: **selects embedding models, dimensions, and index types by measured trade-off** for a capability, and designs re-embedding and migration plans when models change. Scope: a capability's semantic-search layer.
- **E4** - Depth: **standardizes embedding infrastructure across teams** - shared models, versioning, migration tooling - ending per-team drift. Scope: multiple teams.
- **E5** - Depth: **drives the org's vector-infrastructure strategy**, including build-vs-buy for vector stores and cost and scale planning. Scope: organization.
- **E6** - Depth: **anticipates representation-layer shifts** - multimodal embeddings, new architectures - and positions the company ahead of them. Scope: company.

#### Context budget & memory management

*Anchor:* Liu et al., "Lost in the Middle: How Language Models Use Long Contexts" (TACL 2024) - *Why:* context windows are a scarce, position-sensitive resource; what enters, where, and what is summarized away determines behavior.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [AI-02](../../data/capabilities.md#ai-02) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **keeps requests within the context budget**, truncating per team rules, and notices when overflow or truncation silently degrades output. Scope: a task's context usage.
- **E2** - Depth: **prioritizes what enters the window** - system prompt, history, retrieved content - with explicit truncation rules, and tests the effect of dropping each element. Scope: a component's context assembly.
- **E3** - Depth: **designs the context-assembly strategy for a capability** - token budgets per section, summarization versus omission, memory for long sessions, cache-friendly ordering - and shows with evals where added context stops paying. Scope: a capability; others reuse the assembly design.
- **E4** - Depth: **defines context-management patterns multiple teams reuse** - shared memory stores, summarizers, compaction strategies - and audits high-cost windows for waste. Scope: multiple teams.
- **E5** - Depth: **drives org-level context and memory architecture**, deciding what user and org state is durable memory versus per-request context, with token-quality trade-offs measured at fleet level. Scope: organization.
- **E6** - Depth: **positions the company for context-regime shifts** - window growth, pricing changes, memory architectures - before they invalidate current designs. Scope: company.

## Agentic Systems

### Agent Design & Orchestration

#### Agent architecture & orchestration

*Anchor:* Anthropic, "Building Effective Agents" (2024) - *Why:* the central agentic decision is workflow vs. autonomous loop; over-agentifying is the field's dominant failure mode.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [AI-03](../../data/capabilities.md#ai-03) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **traces an existing agent loop end to end** - model call, tool call, state update - explaining why the agent took each step on a real transcript, and fixes defects in single steps. Scope: a task within an agent.
- **E2** - Depth: **builds single-agent workflows with a bounded tool set** using the simplest pattern that works - chain, router, or loop - with explicit termination conditions and step limits by default. Scope: a component.
- **E3** - Depth: **chooses between workflow and autonomous-loop designs by failure-mode analysis**, decomposing multi-step behavior so each step is independently observable and recoverable, and cuts autonomy when a simpler pipeline scores the same. Scope: owns agent architecture for a capability.
- **E4** - Depth: **sets the agent-architecture patterns multiple teams follow** - orchestration substrate, state and handoff conventions, delegation contracts - and kills over-engineered designs with evidence. Scope: multiple teams.
- **E5** - Depth: **owns the org's agentic-systems strategy**, deciding where autonomy is worth its reliability cost and what the shared platform provides. Scope: organization.
- **E6** - Depth: **sets company direction on agentic products** - where agents act, where humans decide - informed by what current models can actually sustain. Scope: company.

#### Tool & function design for agents

*Anchor:* Anthropic, "Writing Effective Tools for Agents" (2025) - *Why:* agents fail at the tool boundary more than anywhere else; tool design is interface design for a non-human caller.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [AI-03](../../data/capabilities.md#ai-03) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **implements a tool to a given schema** with validation and error strings a model can act on, and tests it standalone before wiring it to a model. Scope: single tools within a task.
- **E2** - Depth: **designs tool schemas a model uses correctly on the first try** - clear descriptions, tight parameters, informative error returns - and iterates on them against transcripts of real misuse. Scope: a component's tool set.
- **E3** - Depth: **curates the tool surface of a capability** - right granularity, idempotency and side-effect discipline, permission boundaries - pruning overlapping tools that confuse routing and rewriting descriptions from observed call failures. Scope: a capability's tool ecosystem.
- **E4** - Depth: **defines tool-design standards and shared registries multiple teams consume**, with review gates for high-risk tools, killing near-duplicate tools across agents. Scope: multiple teams.
- **E5** - Depth: **drives the org's tool and integration platform** - registries, permissioning, audit requirements - deciding which internal systems get first-class tool interfaces. Scope: organization.
- **E6** - Depth: **shapes the company's external tool ecosystem posture** - what third parties may plug in, what the company exposes - as a durable interface bet. Scope: company and partners.

### Autonomy, State & Recovery

#### Human oversight & autonomy boundaries

*Anchor:* NIST AI Risk Management Framework 1.0 (2023) - *Why:* human oversight proportional to impact and reversibility is a designed control, not an afterthought.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [AI-05](../../data/capabilities.md#ai-05) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **implements the approval and confirmation steps a design specifies** - never bypassing a human checkpoint without sign-off - and states which of their feature's actions are reversible and which are not. Scope: a task's approval points.
- **E2** - Depth: **designs approval gates by reversibility and blast radius** - auto-run the undoable, confirm the destructive - with dry-run modes, undo paths, and every escalation logged for audit. Scope: a component's autonomy rules.
- **E3** - Depth: **calibrates autonomy per action class for a capability** - auto-execute, confirm, or escalate - from observed override and failure data rather than assumption, and pushes back with reasons when a design grants an agent more authority than its error rate supports. Scope: a capability's operating envelope.
- **E4** - Depth: **standardizes autonomy tiers and approval mechanisms across teams**, with shared approval UX and audit infrastructure, and reviews escalation designs for high-consequence actions. Scope: multiple teams.
- **E5** - Depth: **owns the org's policy for delegated agent authority**, aligned with legal and security, including the evidence bar for widening autonomy. Scope: organization.
- **E6** - Depth: **decides how much authority the company delegates to AI systems** in its products and operations, and defends that line to regulators and customers. Scope: company.

#### Agent state & failure recovery

*Anchor:* Kapoor et al., "AI Agents That Matter" (2024) - *Why:* multi-step agents compound per-step error - a 95%-reliable step fails 40% of the time across ten steps - so containment must be engineered.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [BE-11](../../data/capabilities.md#be-11) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **reproduces a failed agent run from its transcript** and identifies the step where it went wrong - bad plan, bad tool result, lost state. Scope: task-level debugging.
- **E2** - Depth: **builds checkpointing, retries, loop limits, and budget caps into agent steps** so a wandering run halts cheaply and an interrupted run resumes or fails cleanly instead of duplicating side effects. Scope: a component's run lifecycle.
- **E3** - Depth: **designs the state and containment model for an agentic capability** - what persists across turns, blast-radius limits, compensating actions for tool side effects - quantifying compounded failure rates rather than trusting per-step accuracy, and proves recovery paths with fault injection. Scope: a capability's execution engine.
- **E4** - Depth: **sets durable-execution and recovery patterns multiple teams adopt** - resumable run state, saga-style compensation - with adoption they can show. Scope: multiple teams' agent runtimes.
- **E5** - Depth: **drives the org's strategy for stateful, long-running AI execution**, consolidating bespoke run-state code into platform, with reliability targets and failure drills. Scope: organization.
- **E6** - Depth: **sets company reliability doctrine for autonomous systems**, informing what the company will and won't promise customers. Scope: company.

#### Agent containment & blast-radius control

*Anchor:* Nygard, *Release It!* (2nd ed., 2018), bulkheads - *Why:* an agent with tools is a failure amplifier; containment must be engineered before autonomy is granted.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [AI-03](../../data/capabilities.md#ai-03) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **runs agents in the sandboxed environment provided** and reports containment gaps they notice. Scope: their own agent runs.
- **E2** - Depth: **scopes an agent's credentials and tool permissions to least privilege**, and caps loops, spend, and side effects by construction. Scope: one agent's blast radius.
- **E3** - Depth: **designs containment for a capability's agents** - sandboxing, budget kill-switches, reversible-by-default actions - and red-teams their own boundaries before launch. Scope: a capability; their containment review gates agent launches.
- **E4** - Depth: **builds containment infrastructure several teams inherit rather than reimplement**, and audits exceptions. Scope: multiple teams.
- **E5** - Depth: **sets the org's containment standards for autonomous systems** and verifies them through game days. Scope: organization.
- **E6** - Depth: **owns the company's worst-case analysis for agentic products** and the controls that bound it. Scope: company.

## Evaluation & Observability

### Evaluation Engineering

#### Eval sets & golden data

*Anchor:* Husain, "Your AI Product Needs Evals" (2024) - *Why:* eval sets built by error analysis on real traces are the only ones that measure anything.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [AI-07](../../data/capabilities.md#ai-07) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **adds well-formed cases to an existing eval set** - realistic input, unambiguous expected behavior - labeling edge cases consistently with the rubric and flagging ambiguous ones instead of guessing. Scope: eval cases for their task.
- **E2** - Depth: **builds an eval set for a feature from production traces via error analysis**, balancing common paths and hard cases, versioning golden data like code with documented inclusion criteria. Scope: a component's eval coverage.
- **E3** - Depth: **owns the golden datasets of a capability** - coverage mapped to known failure modes, refresh cadence, contamination and leakage checks - retiring stale cases and tracing every regression escape back to the missing case class. Scope: a capability; their sets gate teammates' merges.
- **E4** - Depth: **sets eval-data standards multiple teams follow** - sampling policy, labeling rubrics, inter-rater checks, dataset versioning - and audits suites whose numbers look too good. Scope: multiple teams.
- **E5** - Depth: **drives the org's evaluation-data strategy** - shared corpora, labeling operations, data governance for eval assets. Scope: organization.
- **E6** - Depth: **defines how the company knows its AI works** - the evidence doctrine cited in launch reviews and external claims. Scope: company.

#### Eval metrics & judge design

*Anchor:* Zheng et al., "Judging LLM-as-a-Judge with MT-Bench and Chatbot Arena" (NeurIPS 2023); Shankar et al., "Who Validates the Validators?" (2024) - *Why:* judges are fallible instruments; an unvalidated judge automates the wrong opinion at scale.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [AI-04](../../data/capabilities.md#ai-04) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **runs the eval harness and reads its reports correctly**, distinguishing a real regression from noise with help and flagging results that look wrong instead of accepting them. Scope: their changes.
- **E2** - Depth: **chooses graders that fit the behavior under test** - exact-match, rubric, pairwise, LLM-judge - and spot-checks judge agreement against their own labels before trusting it. Scope: a component's metrics.
- **E3** - Depth: **designs the measurement itself for a capability** - metrics that track user outcomes, judges validated against human ratings with quantified agreement and bias, significance limits stated before declaring a win. Scope: a capability; measure-before-ship is their default others copy.
- **E4** - Depth: **standardizes eval methodology across teams**, calibrating judge models centrally so scores are comparable, and arbitrates when two teams' numbers disagree about the same behavior. Scope: multiple teams.
- **E5** - Depth: **owns the org's measurement strategy for AI quality**, connecting offline evals to online outcomes and killing metrics that don't predict. Scope: organization.
- **E6** - Depth: **defines what 'good' means for the company's AI products** in measurable terms executives, customers, and regulators accept. Scope: company.

#### Measurement-gated shipping

*Anchor:* Sculley et al., "Hidden Technical Debt in Machine Learning Systems" (NeurIPS 2015) - *Why:* unmeasured behavioral change is the dominant debt in model-backed systems; ship decisions must rest on measured deltas, not demos.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [QA-08](../../data/capabilities.md#qa-08) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **runs the required evals before merging prompt or model changes and pastes results into the review**, flagging regressions instead of explaining them away. Scope: their own changes.
- **E2** - Depth: **attaches eval deltas to every prompt, model, or retrieval change** and blocks their own launches on regressions - shadow or A/B comparisons for risky changes - without being told. Scope: a component's releases.
- **E3** - Depth: **defines the ship gate for a capability** - which evals block release, what regression tolerance is, when human review is required - and holds the line under deadline pressure with the reasoning in writing. Scope: a capability's ship decisions.
- **E4** - Depth: **installs measurement-gated release processes across teams** - eval CI, canary analysis, staged rollouts teams actually use - and audits exceptions. Scope: multiple teams' pipelines.
- **E5** - Depth: **owns the org's ship/no-ship framework for AI behavior changes** and arbitrates escalations where speed and evidence conflict. Scope: organization.
- **E6** - Depth: **sets company policy on the evidence required to ship AI behavior**, balancing speed and risk explicitly. Scope: company.

### Observability & Production Feedback

#### Tracing & instrumentation of AI systems

*Anchor:* OpenTelemetry Generative AI semantic conventions (CNCF, 2024-2025) - *Why:* nondeterministic multi-step systems cannot be debugged from logs alone; traces are the unit of truth.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-05](../../data/capabilities.md#ops-05) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **uses existing traces to debug a failing request** - walking prompt -> retrieval -> tool call -> output - and adds a missing span when told what to capture. Scope: their tasks.
- **E2** - Depth: **instruments a component end to end** - prompts, completions, token counts, tool calls, latencies - as structured spans with the metadata (prompt version, model id) needed to reproduce any output later, with sampling and redaction applied correctly. Scope: a component's telemetry.
- **E3** - Depth: **designs the observability schema for a capability** - what is captured, sampled, retained, and redacted - and builds the views that make failure clusters visible, answering 'why did this output happen' in minutes. Scope: a capability; their traces are where debugging starts.
- **E4** - Depth: **sets tracing conventions multiple teams emit**, aligning attributes so cross-service AI requests join up in one lens, and builds the views on-call engineers actually use. Scope: multiple teams.
- **E5** - Depth: **owns the org's AI observability platform strategy**, including retention, privacy, and cost of trace data. Scope: organization.
- **E6** - Depth: **ensures the company can answer 'why did the model do that?'** for any production decision, as a matter of architecture. Scope: company.

#### Production monitoring & drift detection

*Anchor:* Breck et al., "The ML Test Score" (2017) - *Why:* model-backed quality decays silently as inputs, usage, and providers change; monitoring must watch behavior, not just uptime.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [AI-17](../../data/capabilities.md#ai-17) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **watches the dashboards for their feature after deploys** and escalates anomalies with the trace attached rather than assuming success. Scope: post-ship checks on their tasks.
- **E2** - Depth: **builds behavioral monitors for a component** - refusal rate, format-break rate, user-feedback signals - with alert thresholds they can justify, promoting recurring failures into the eval set. Scope: a component's monitors.
- **E3** - Depth: **detects silent degradation for a capability** - baselines behavior, catches provider-side model changes and input-distribution drift, reruns evals on live samples on a schedule - and has caught a real regression no user reported. Scope: a capability in production.
- **E4** - Depth: **standardizes behavioral monitoring and feedback-to-eval pipelines across teams**, with shared metric definitions so numbers are comparable, correlating cross-product regressions to a common upstream cause. Scope: multiple teams.
- **E5** - Depth: **owns the org's in-production AI quality picture**, making drift review a routine practice with owners and SLAs, briefing leadership on trends rather than incidents. Scope: organization.
- **E6** - Depth: **makes behavioral health a company-level operational metric**, reported alongside availability, defining how the company absorbs provider upgrades without quality surprises. Scope: company.

## Reliability, Cost & Performance

### Production Reliability

#### Fallbacks & graceful degradation

*Anchor:* Nygard, *Release It!* (2nd ed., 2018) - *Why:* provider outages, rate limits, and malformed outputs are routine; stability patterns are the designed defense.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-04](../../data/capabilities.md#ops-04) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **implements the retry, timeout, and fallback behavior a design specifies** and tests the failure path by forcing the failure, not just the happy path. Scope: their tasks.
- **E2** - Depth: **designs the degradation ladder for a component** - retry budgets, circuit breaking on provider errors, cached or smaller-model fallbacks, an honest error - and makes each rung observable. Scope: a component's failure behavior.
- **E3** - Depth: **owns availability design for a capability across providers** - failover routing, brownout modes, load shedding - with explicit SLOs that include behavioral quality, validated with game days rather than hope. Scope: a capability's reliability.
- **E4** - Depth: **builds the shared resilience layer multiple teams depend on** - gateway, routing, quota management - and reviews launches for shared-fate provider risk. Scope: multiple teams.
- **E5** - Depth: **owns org-level continuity for provider failure** - multi-provider posture, capacity reservations, tested playbooks. Scope: organization.
- **E6** - Depth: **answers for company availability of AI products** through provider incidents that make the news, setting the architecture doctrine behind the commitments. Scope: company.

#### Incident response for AI systems

*Anchor:* Beyer et al., *Site Reliability Engineering* (2016) - *Why:* AI incidents add novel failure classes - quality collapse, runaway cost, harmful output - to classic outage response.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-06](../../data/capabilities.md#ops-06) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **follows the runbook during incidents**, keeps the timeline updated, captures the traces responders need, and asks for help early. Scope: a participant in the response.
- **E2** - Depth: **debugs live model-system incidents independently** - distinguishing provider outage from prompt regression from data problem - and writes the postmortem with concrete actions. Scope: a component's on-call.
- **E3** - Depth: **incident-commands for their capability**, including quality and cost incidents that page no one by default; writes the runbooks for model rollback and prompt reversion others copy, and drives postmortems to systemic fixes. Scope: a capability's incident response.
- **E4** - Depth: **raises operational maturity across teams** - severity definitions that include model-quality events, game days for AI failure classes, readiness reviews before launches. Scope: multiple teams.
- **E5** - Depth: **owns the org's incident-management standard for AI systems**, reviewing the postmortems that cross team boundaries and closing systemic gaps. Scope: organization.
- **E6** - Depth: **is the company's senior technical responder in its worst AI incidents** and changes company practice from what they reveal. Scope: company.

#### Provider & capacity management

*Anchor:* Beyer et al., *Site Reliability Engineering* (2016), capacity planning - *Why:* a model provider is a tier-0 dependency the team doesn't operate; quota, deprecations, and capacity must be engineered around.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [BE-19](../../data/capabilities.md#be-19) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **monitors quota and rate-limit dashboards for their service** and escalates approaching limits before they bite. Scope: awareness within a task.
- **E2** - Depth: **implements rate limiting, request queuing, and backoff for a component** and tracks provider deprecation notices that affect it. Scope: a component's capacity behavior.
- **E3** - Depth: **plans capacity for a capability** - load forecasting, quota negotiation inputs, multi-region or multi-provider failover design - and runs model-version migrations without user-visible regression. Scope: a capability's provider posture.
- **E4** - Depth: **runs cross-team capacity and migration programs** - org-wide model deprecation moves, shared quota pooling - that land on schedule. Scope: multiple teams.
- **E5** - Depth: **owns the org's provider risk management** - concentration risk, contractual SLAs, burst capacity. Scope: organization.
- **E6** - Depth: **sets company posture on model-supply resilience** as a business-continuity matter leadership understands. Scope: company.

### Cost & Performance

#### Token economics & cost optimization

*Anchor:* Chen et al., "FrugalGPT" (2023) - *Why:* per-call marginal cost makes unit economics an engineering responsibility, not a finance afterthought.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-07](../../data/capabilities.md#ops-07) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **states what their feature costs per request**, attributing spend to prompt size, output length, and call count correctly, and checks the dashboard after changes ship. Scope: their tasks' spend.
- **E2** - Depth: **cuts a component's cost with measured, quality-neutral levers** - prompt trimming, caching, batching, output caps - and reports the before/after against any quality change. Scope: a component's unit economics.
- **E3** - Depth: **owns the cost model of a capability** - cost per request and per user action tracked against quality, budgets and anomaly alerts set, cost-quality trades explicit in design docs - and catches cost regressions in review before they ship. Scope: a capability's unit economics.
- **E4** - Depth: **finds the cross-team cost structure** - shared caches, duplicated calls, misrouted traffic - and drives the fixes worth the most, with cost governance (attribution, budget reviews) teams adopt. Scope: multiple teams' spend.
- **E5** - Depth: **owns the org's inference-spend strategy** - forecasting at product scale, informing provider negotiations, deciding where cost work beats feature work. Scope: organization.
- **E6** - Depth: **keeps AI gross margins viable at company level**, shaping pricing and architecture together. Scope: company.

#### Latency & model right-sizing

*Anchor:* Huyen, *AI Engineering* (2025), inference-optimization chapters - *Why:* the smallest model that meets the quality bar is usually the right one, and someone has to prove which that is.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [AI-19](../../data/capabilities.md#ai-19) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **measures end-to-end latency for their feature** - including time-to-first-token - and identifies the slowest stage from traces. Scope: their tasks.
- **E2** - Depth: **applies standard latency levers independently** - streaming, parallel calls, speculative work, caching - to hit a stated target, validated with p95, not averages. Scope: a component's latency budget.
- **E3** - Depth: **right-sizes models per task within a capability** - proving with evals that the smaller, faster model holds the quality bar - designs routing that matches request difficulty to model tier, and defines latency SLOs users actually feel. Scope: a capability's performance envelope.
- **E4** - Depth: **builds or mandates the routing and caching infrastructure multiple teams use** to meet shared latency standards, and audits over-provisioned model use. Scope: multiple teams.
- **E5** - Depth: **sets the org's latency/quality/cost frontier** and the serving investments (routing, caching, distillation, self-hosting) that move it. Scope: organization.
- **E6** - Depth: **makes speed a company-level product advantage**, deciding where the company competes on latency and the architectural commitments behind it. Scope: company.

## Safety, Security & Responsible AI

### AI Security & Privacy

#### Prompt injection & untrusted model I/O

*Anchor:* OWASP Top 10 for LLM Applications (2025) - LLM01 Prompt Injection - *Why:* any content a model reads is a potential instruction channel; agents with tools turn injection into action.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-08](../../data/capabilities.md#ops-08) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **treats model output and retrieved content as untrusted** - never executes, renders, or queries with it unescaped, never concatenates untrusted content into instructions - and can explain injection with a real example. Scope: their own code paths.
- **E2** - Depth: **builds injection defenses into a component** - privilege separation between instructions and data, output validation, allowlisted tool arguments - and writes adversarial cases into its tests. Scope: a component's trust boundaries.
- **E3** - Depth: **threat-models a capability's model I/O paths end to end** - including the untrusted-content, private-data, external-communication combination - designs least-privilege mitigations accepted by security review, and red-teams their own features before attackers do. Scope: a capability's attack surface; their threat model is reviewed, not re-derived, by others.
- **E4** - Depth: **sets secure-by-default patterns for model I/O that multiple teams inherit** from shared libraries - sanitization layers, tool-permission frameworks, injection suites in CI - and runs adversarial reviews of high-exposure launches. Scope: multiple teams.
- **E5** - Depth: **owns the org's LLM security program with the security org** - threat models, red-team cadence, incident learnings folded back into platform defaults. Scope: organization.
- **E6** - Depth: **is accountable for the company's AI attack surface** - deciding what the company will and won't expose to untrusted input - and represents the posture to customers, auditors, and researchers. Scope: company.

#### Data privacy & PII handling

*Anchor:* NIST Privacy Framework (2020) - *Why:* prompts, traces, and eval sets are new copies of user data; each is a leak path classic data governance doesn't automatically cover.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-09](../../data/capabilities.md#ops-09) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **follows the team's rules for what may enter prompts, logs, and eval data**, and asks before sending a new data category to a model provider. Scope: data handling in their tasks.
- **E2** - Depth: **implements redaction and minimization in a component's pipelines** - PII scrubbing before model calls, trace redaction, retention limits - and verifies with tests that sensitive fields don't leak into telemetry. Scope: a component's data flows.
- **E3** - Depth: **owns the data-flow map of a capability end to end** - what user data reaches which provider under what retention terms - designing minimization in rather than bolting it on, and catches new leak paths in design review. Scope: a capability's privacy posture.
- **E4** - Depth: **standardizes privacy engineering for AI across teams** - shared redaction tooling, review checklists, provider data-processing requirements - and audits the highest-sensitivity data flows. Scope: multiple teams.
- **E5** - Depth: **owns the org's data posture toward model providers**, partnering with legal on agreements, audits, and the hard cases like eval data versus deletion requests. Scope: organization.
- **E6** - Depth: **answers for the company's AI data-handling promises** - what is committed to customers about their data, and the architecture that keeps it true. Scope: company.

### Responsible AI & Governance

#### Guardrails & output safety

*Anchor:* Bai et al., "Constitutional AI: Harmlessness from AI Feedback" (2022) - *Why:* product-level safety is engineered in layers around the model, not delegated to it.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [AI-05](../../data/capabilities.md#ai-05) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **wires existing guardrails into a feature** - schema validation, content filters, refusal handling - verifies rejects follow the designed path, and escalates outputs that feel harmful rather than shipping past them. Scope: a task.
- **E2** - Depth: **implements layered guardrails for a component** - input filters, output classifiers, safe-completion fallbacks - and measures their false-positive and false-negative rates instead of assuming they work. Scope: a component's safety layer.
- **E3** - Depth: **designs the control stack for a capability from a written risk analysis** - which failures are prevented, detected, or accepted, and where each control lives (prompt, classifier, policy engine, UX) - testing guardrails adversarially before launch and owning the harm/annoyance trade explicitly. Scope: a capability's behavior boundaries.
- **E4** - Depth: **standardizes guardrail patterns and shared safety infrastructure across teams** - common classifiers, a policy taxonomy - with authority to block a ship on control gaps. Scope: multiple teams.
- **E5** - Depth: **owns the org's output-safety standards and red-teaming program**, reporting residual risk honestly to leadership. Scope: organization.
- **E6** - Depth: **defines the company's safety bar for AI products** - what its AI refuses, allows, and how that is defended publicly - including saying no to launches. Scope: company.

#### Harm mitigation & safety behavior

*Anchor:* Weidinger et al., "Taxonomy of Risks Posed by Language Models" (FAccT 2022) - *Why:* deployed models can produce harmful, biased, or overconfident output; mitigation starts from a named harm profile, not a disclaimer.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [AI-15](../../data/capabilities.md#ai-15) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **recognizes and reports harmful or biased outputs found during development** instead of shrugging them off as model quirks. Scope: their task.
- **E2** - Depth: **tests a component against the team's harm checklist** - unsafe advice, bias probes across user groups, overconfident hallucination - and adds mitigations that measurably reduce hits. Scope: a component.
- **E3** - Depth: **defines the harm profile for a capability** - who can be hurt and how - ships mitigations (refusals, hedging, citations, escalation paths) with eval coverage per harm class, and makes a written ship/hold recommendation leadership can act on, escalating when asked to ship past a red line. Scope: a capability; launch reviews use their assessment.
- **E4** - Depth: **sets harm-analysis practice across teams** and reviews launches with meaningful harm potential, arbitrating safety-vs-utility disputes with data. Scope: multiple teams.
- **E5** - Depth: **operationalizes the org's responsible-AI commitments** into engineering requirements teams can actually implement. Scope: organization.
- **E6** - Depth: **shapes the company's public safety posture** and is accountable for it holding under scrutiny. Scope: company.

#### AI risk assessment & governance

*Anchor:* NIST AI Risk Management Framework 1.0 (2023); EU AI Act (2024) - *Why:* AI systems are entering a regulated era; classifying systems by risk and evidencing controls is table stakes for shipping.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [proposed](../../contrib/2026-07-ai-risk-governance.md) (AI-21 candidate) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **completes the launch risk checklist for their change accurately** - identifying who is affected if the model is wrong - and escalates anything the checklist doesn't cover. Scope: their task.
- **E2** - Depth: **assesses a feature's failure impact before build** - misuse, error harm, disparate performance - and documents residual risk and the design choices that reduce it, without being chased. Scope: a component's risk profile.
- **E3** - Depth: **classifies a capability against the applicable risk framework**, keeps its evidence pack (evals, controls, incidents) audit-ready, converts findings into engineering requirements with owners, and flags when a product change alters its risk class. Scope: a capability's risk register.
- **E4** - Depth: **operates the cross-team AI risk-review process** - fast enough that teams use it honestly, rigorous enough to catch real issues - and builds the governance tooling that makes compliance a byproduct of normal engineering. Scope: multiple teams' launches.
- **E5** - Depth: **owns the org's AI governance program jointly with legal and risk**, translating regulation into engineering requirements without freezing delivery. Scope: organization.
- **E6** - Depth: **positions the company ahead of AI regulation**, accountable to executives and boards for the risk posture and shaping its regulatory engagement. Scope: company.

## Delivery, Impact & Leadership

### Product & Business Impact

#### Problem framing & solution fit

*Anchor:* Zinkevich, "Rules of Machine Learning" (Google), Rule #1 - *Why:* the highest-leverage AI engineering decision is whether the problem needs a model at all.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [AI-20](../../data/capabilities.md#ai-20) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **states what user problem their task serves** and raises it when a lookup table or heuristic would do what the ticket asks of a model. Scope: their tasks.
- **E2** - Depth: **prototypes the simplest adequate approach first** - rules, search, classical ML, or a model - and recommends the model only when it beats the baseline, with the comparison documented. Scope: a component's approach.
- **E3** - Depth: **kills LLM-shaped solutions to non-LLM problems in design review with evidence**, reframing vague 'add AI' asks into testable user outcomes product partners agree to, and matches technique to problem across a capability. Scope: a capability's problem space; PMs seek their framing early.
- **E4** - Depth: **installs solution-fit review in how multiple teams take on AI work**, redirecting AI-for-its-own-sake proposals and unwinding the most expensive misfit projects. Scope: multiple teams' portfolios.
- **E5** - Depth: **shapes which problems the org points AI at**, pairing with product leadership on where models genuinely change the offering and cancelling bets the evidence turns against. Scope: organization.
- **E6** - Depth: **advises company leadership on what AI makes newly possible versus fashionable** - and is right often enough to be believed. Scope: company.

#### Outcome measurement & business value

*Anchor:* Forsgren, Humble & Kim, *Accelerate* (2018) - *Why:* AI features are expensive per use; proving they earn their cost is part of the job.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [PD-06](../../data/capabilities.md#pd-06) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **states how their feature's success will be measured** beyond 'it works' and checks the metric after launch rather than moving on. Scope: their features.
- **E2** - Depth: **defines success metrics with product partners before building** and reports post-launch results honestly, including misses, reacting when product metrics and eval scores diverge. Scope: a component's outcomes.
- **E3** - Depth: **connects a capability's engineering metrics to business outcomes** - cost per outcome, retention, task completion - and recommends sunsetting features whose value evidence never arrives, with the data that justifies it. Scope: a capability's return on investment.
- **E4** - Depth: **builds the value-measurement discipline multiple teams use for AI investments**, surfacing which bets are and aren't paying off and reallocating effort when the numbers say so. Scope: multiple teams' portfolios.
- **E5** - Depth: **owns the org's account of AI value delivered**, credible to finance and product alike, and reallocates engineering toward what the evidence supports. Scope: organization.
- **E6** - Depth: **shapes how the company invests in AI based on demonstrated value**, with numbers that survive diligence at board level. Scope: company.

### Delivery Under Uncertainty

#### Planning under model uncertainty

*Anchor:* Yan et al., "What We Learned from a Year of Building with LLMs" (O'Reilly, 2024) - *Why:* model capability is discovered, not specified; plans must buy information before making promises.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [PD-04](../../data/capabilities.md#pd-04) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **breaks their work into small verifiable increments** and flags early - with evidence - when the model can't do what the task assumed, instead of grinding silently. Scope: their tasks.
- **E2** - Depth: **plans feature work as a de-risking sequence** - timeboxed feasibility spike, eval baseline, then build - giving estimates as ranges with stated confidence and re-planning visibly when the spike says no. Scope: a component's plan.
- **E3** - Depth: **structures a capability's roadmap around its riskiest unknowns** - feasibility gates before commitments, kill criteria stated before the spike starts and honored when triggered, a shippable fallback behind every model-dependent bet. Scope: a capability's roadmap; their spikes change roadmaps.
- **E4** - Depth: **teaches teams to plan AI work honestly** - separating engineering certainty from model uncertainty in commitments leaders can rely on - and de-risks the org's biggest AI commitments personally. Scope: multiple teams' planning.
- **E5** - Depth: **shapes the org's portfolio of AI bets**, balancing near-certain delivery against high-variance exploration and keeping leadership expectations calibrated to what evals actually show. Scope: organization.
- **E6** - Depth: **times company bets against the model-capability curve** - what to build now versus wait for - and is accountable for the calls. Scope: company.

#### Incremental delivery & de-risking

*Anchor:* Humble & Farley, *Continuous Delivery* (2010) - *Why:* the safest way to ship nondeterministic behavior is in small, reversible, observable slices.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-30](../../data/capabilities.md#ops-30) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **ships work in small reviewable increments behind flags as directed** and rolls back their own change cleanly when asked. Scope: task-sized increments.
- **E2** - Depth: **designs a component's rollout as canary -> percentage -> full**, watching evals and telemetry at each stage and rolling back on their own signal. Scope: a component's rollout.
- **E3** - Depth: **owns progressive-delivery strategy for a capability** - shadow modes for new models, reversible-by-design changes, automated rollback triggers - and their launches are uneventful. Scope: a capability's release engineering.
- **E4** - Depth: **builds the progressive-delivery machinery multiple teams use for AI changes** - flag conventions, automated rollback on eval regression. Scope: multiple teams.
- **E5** - Depth: **sets the org's release-engineering direction for AI products** and its risk appetite per surface. Scope: organization.
- **E6** - Depth: **makes safe iteration speed a company capability** competitors can't easily copy. Scope: company.

#### Ownership & delivery accountability

*Anchor:* CircleCI Engineering Competency Matrix (progression.fyi/f/circle-ci) - *Why:* ownership is the observable spine of an IC ladder - commitments made, kept, and renegotiated honestly.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [PD-05](../../data/capabilities.md#pd-05) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **takes ownership of assigned tasks and communicates progress and blockers honestly**, driving them to done without waiting to be asked. Scope: answerable for individual work items.
- **E2** - Depth: **owns components end to end and delivers committed work reliably**, raising slips as soon as they are known. Scope: answerable for a component's quality and timeliness.
- **E3** - Depth: **owns a capability and lands multi-week efforts without surprises**, pushing back on unrealistic scope with reasons. Scope: others depend on their systems; answerable for the capability's outcomes.
- **E4** - Depth: **owns cross-team initiatives**, unblocking teams and killing failing approaches early. Scope: answerable to leadership for multi-team program outcomes.
- **E5** - Depth: **owns an org-level portfolio of technical bets**. Scope: answerable for org outcomes; sets direction others follow.
- **E6** - Depth: **owns company-critical technical outcomes** - leadership's go-to when something absolutely must land. Scope: company.

### Communication & Collaboration

#### Technical communication & writing

*Anchor:* Larson, *Staff Engineer* (2021) - *Why:* AI systems are probabilistic and unfamiliar; the engineer who can explain them accurately shapes every decision around them.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [CC-01](../../data/capabilities.md#cc-01) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **writes clear task updates, commit messages, and questions with enough context that responders don't have to ask for it**, summarizing eval results without overstating them. Scope: their team's channels.
- **E2** - Depth: **writes design notes and runbooks peers act on without follow-up questions**, and explains model behavior and its limits to non-experts without jargon or overclaiming. Scope: a component's stakeholders.
- **E3** - Depth: **writes the docs that settle decisions** - options, evidence, recommendation - and translates eval results and AI trade-offs so accurately that product decisions built on their word hold up. Scope: a capability's decision record.
- **E4** - Depth: **aligns multiple teams through writing** - RFCs, strategies, decision records cited months later as the reference - and presents AI capability and risk to leadership without dumbing it down. Scope: multiple teams.
- **E5** - Depth: **communicates org-level technical direction upward and outward**, translating between executive and engineering registers without loss, including bad news early. Scope: organization.
- **E6** - Depth: **is the company's technical voice on AI internally and externally** - talks, publications, customer and regulator conversations that move the company's position. Scope: company and industry.

#### Cross-functional collaboration

*Anchor:* Skelton & Pais, *Team Topologies* (2019) - *Why:* AI features cut across product, design, data, legal, and security; the seams are where they fail.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [CC-03](../../data/capabilities.md#cc-03) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **works effectively with designer and PM counterparts on task details**, surfacing AI-specific constraints - latency, failure modes - early, and incorporates feedback without churn. Scope: their team.
- **E2** - Depth: **partners with product and design on what the model can and can't support**, involving them before the prompt is final and prototyping to resolve disagreements with evidence. Scope: a component's cross-functional loop.
- **E3** - Depth: **runs the cross-functional process for a capability** - brings legal, security, and support in before launch, turns product intent into evaluable requirements - and resolves conflicts between functions without escalation. Scope: a capability's stakeholder set; peers in other functions seek them out.
- **E4** - Depth: **fixes broken cross-team interfaces** - ownership gaps, handoff friction - building the review forums, interface agreements, and shared vocabularies several teams use. Scope: multiple teams' seams.
- **E5** - Depth: **builds the org's operating model between AI engineering and other functions** - data, platform, trust, product - so work flows without heroics. Scope: organization.
- **E6** - Depth: **brokers company-level alignment on AI initiatives across executive functions** with durable results. Scope: company.

#### Documentation & knowledge sharing

*Anchor:* Mitchell et al., "Model Cards for Model Reporting" (FAT* 2019) - *Why:* AI systems decay into folklore fast; written behavior contracts are what survive team turnover.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [CC-02](../../data/capabilities.md#cc-02) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **keeps the docs for what they build current** - setup, known limits, gotchas - and files gaps they find in others'. Scope: their own work.
- **E2** - Depth: **documents a feature's behavior contract** - intended use, eval results, failure modes, escalation paths - findable by the next engineer without asking. Scope: one component.
- **E3** - Depth: **maintains the canonical documentation for a capability** - architecture, prompt rationale, eval history, runbooks - and prunes stale docs as ruthlessly as stale code. Scope: a capability; new joiners onboard from their docs alone.
- **E4** - Depth: **drives documentation standards for AI systems across teams** - behavior cards, decision records - and reviews for compliance. Scope: multiple teams.
- **E5** - Depth: **builds the org's AI knowledge base as infrastructure**, making internal expertise discoverable. Scope: organization.
- **E6** - Depth: **externalizes company knowledge deliberately** - publications, standards participation - where it compounds the company's position. Scope: company.

### Mentoring & Technical Leadership

#### Mentoring & knowledge sharing

*Anchor:* Fournier, *The Manager's Path* (2017), mentoring chapters - *Why:* AI engineering practice changes monthly; teams that don't teach internally re-learn everything the hard way.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [LI-01](../../data/capabilities.md#li-01) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **asks for help effectively and pays it forward**, documenting what they learned where the next person will find it. Scope: their immediate peers.
- **E2** - Depth: **onboards new teammates onto the AI stack and pairs generously**, turning their own review comments and repeated questions into reusable explanations. Scope: their team.
- **E3** - Depth: **mentors engineers deliberately** - stretch tasks matched to gaps, feedback that names behavior and impact - and levels a team up on AI-specific craft (evals, prompting, agent design) it didn't have before; mentees ship independently sooner. Scope: a capability's engineers; the terminal-level expectation, sustainable indefinitely.
- **E4** - Depth: **grows senior engineers across teams**, sponsoring others into leading work they would have led, and builds the guilds and curricula that scale beyond one-on-ones. Scope: multiple teams' talent.
- **E5** - Depth: **builds the org's AI-engineering bench** - hiring bar, growth paths, promotion evidence, succession for critical systems. Scope: organization.
- **E6** - Depth: **develops the company's next generation of principal-level technical leaders**, largely through others, and shapes how the company is known to candidates. Scope: company.

#### Technical leadership & direction setting

*Anchor:* Larson, *Staff Engineer* (2021) and StaffEng archetypes - *Why:* past senior, direction-setting and alignment - not authority - are how technical outcomes land.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [LI-03](../../data/capabilities.md#li-03) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **volunteers for unglamorous work that unblocks others** and raises risks early instead of waiting to be asked. Scope: their team's day-to-day.
- **E2** - Depth: **leads small technical efforts end to end** - a migration, an integration - coordinating the people involved without formal authority or escalation. Scope: a component-sized effort.
- **E3** - Depth: **sets technical direction for a capability** - making and documenting the contentious calls, taking responsibility when wrong - and is the engineer others seek out when an AI decision is stuck. Scope: a capability; the terminal-level leadership bar.
- **E4** - Depth: **creates alignment across teams that don't report to them**, landing multi-team initiatives - platform migrations, model transitions - through writing, relationships, and demonstrated judgment. Scope: multiple teams' roadmaps.
- **E5** - Depth: **drives the org's technical strategy for AI**, choosing the few bets that matter and getting leadership and teams genuinely behind them. Scope: organization.
- **E6** - Depth: **sets the company's long-term technical direction for AI**, accountable for the bets years before they resolve. Scope: company.
