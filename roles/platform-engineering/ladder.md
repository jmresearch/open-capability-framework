# Platform Engineering - Canonical Career Ladder

## Calibration summary

- **Provenance:** canonical consolidation of five independent same-methodology sources (blind runs plat-r1 ... plat-r4 plus an earlier theory-anchored single-run ladder; 163 source competencies) by **union, not intersection** - every genuinely distinct competency from any source survives; nothing was voted out. Semantic duplicates were merged into single canonical competencies (clearest technology-agnostic name, strongest citable anchor, best observable cell content). Minted 2026-07-02.
- **Variant:** ic_technical (individual-contributor technical track).
- **Levels:** six, E1-E6 - Associate Platform Engineer -> Platform Engineer -> Senior Platform Engineer -> Staff Platform Engineer -> Senior Staff Platform Engineer -> Principal Platform Engineer.
- **Scope bands:** task (E1) -> component (E2) -> capability/domain (E3) -> multiple teams (E4) -> organization (E5) -> company (E6), following Google L3-L8 / Meta E3-E8 norms via levels.fyi, with StaffEng (Larson) grounding E4-E6 behaviors.
- **Terminal level: E3 / Senior.** All five sources agree: a strong platform engineer can remain at E3 indefinitely without being behind. E4+ is not "more of E3" - it is a different job defined by multi-team scope, standard-setting, and organizational leverage.
- **Register:** CircleCI Engineering Competency Matrix - present-tense observable behaviors; Depth and Scope separated in every cell. Adoption is leveled as **voluntary use by internal customers**, never mandated compliance.
- **Shape:** 7 key areas, 17 focus areas, 37 competencies; every focus area spans 2+ competencies; theme labels are under 60 characters and technology-agnostic.
- **OCF mapping:** every competency carries an Open Capability Framework reference - 34 map to existing catalog capabilities (including the newly minted OPS-30 progressive delivery & release safety, carried by Deprecation & migration management) and 3 are proposed additions (thinnest viable platform, cognitive load reduction, guardrails & policy as code) staged under contrib/.
- **Consolidation judgment calls:** (1) Platform as a Product is the first key area - user research, adoption metrics, thinnest-viable scoping, golden paths, and cognitive-load reduction are ratable engineering competencies, which is what distinguishes platform engineering from rebranded ops. (2) The trusted source's splits survive under the union rule: coding vs. code review, incident response vs. learning from incidents, and a product-discipline roadmap competency distinct from execution-side prioritization. (3) Blended source rows ("Thinnest viable platform & roadmap", "Code quality & review", "Incident response & learning", "Feedback & review culture") were assigned to the concept their cell content leans toward. (4) Single-source competencies (platform roadmap & prioritization, networking & compute foundations, learning from incidents) all survive as distinct rows. (5) Release engineering merges into deprecation & migration management (its E2 carries versioned releases, flags, and rollback), and progressive delivery lives inside the CI/CD competency at E3. (6) Capacity, performance, and cost consolidate into one competency - every source ties them together through unit economics. (7) Golden paths and self-service provisioning both map to OPS-27 and incident response / learning from incidents both map to OPS-06 - each catalog capability's description spans both rows; flagged as future split candidates rather than forcing a weaker distinct mapping.

## Level overview

| Level | Title | Scope band | Focus |
|---|---|---|---|
| E1 | Associate Platform Engineer | task | Learns the platform and ships well-defined tasks with guidance |
| E2 | Platform Engineer | component | Owns platform components end to end and unblocks internal users independently |
| E3 | Senior Platform Engineer | capability / domain - **terminal level** | Owns a platform capability as a product; terminal level |
| E4 | Staff Platform Engineer | multiple teams | Shapes platform architecture and adoption across multiple teams |
| E5 | Senior Staff Platform Engineer | organization | Sets platform strategy and standards for the engineering organization |
| E6 | Principal Platform Engineer | company | Sets company-wide platform direction and technical bets |

**Terminal level - E3 / Senior.** Sustained excellence at E3 is a complete, respected career, not a waypoint. Progression beyond E3 is opt-in and changes the nature of the job from building the thing to aligning the people and systems around the thing.

## Competency matrix

Each cell separates **Depth** (mastery of the skill) from **Scope** (how far the work reaches). Cells are present-tense behaviors observable by peers, leaders, and internal customers.

---

## Platform as a Product

### Product Discovery & Feedback

#### Internal user research

*Anchor:* Noda, Storey, Forsgren & Greiler, "DevEx: What Actually Drives Productivity" (ACM Queue, 2023) - *Why:* grounds discovery in evidence about how developers actually experience the platform, not provider assumptions.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [PM-01](../../data/capabilities.md#pm-01) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Shadows platform users and sits in on interviews and support rotations, writing up the friction they hit** - reproduces a reported pain point end to end before proposing a fix, and asks users clarifying questions rather than assuming intent. Scope: observations feed a single task or bug report.
- **E2** - Depth: **Runs structured interviews and support-channel reviews with the internal engineers using their component**, turning raw notes into ranked friction lists the team acts on. Distinguishes what users say from what their workflow shows. Scope: the feedback loop for one component.
- **E3** - Depth: **Designs and runs the discovery process for a capability** - recurring user touchpoints, journey maps, and a friction backlog that visibly drives the roadmap. Separates what users ask for from the workflow problem underneath and shows the evidence for the difference. Scope: all internal users of a platform capability.
- **E4** - Depth: **Synthesizes research across several product teams into shared personas and friction maps other platform teams adopt**, and coaches engineers on interview and synthesis technique instead of letting them guess. Scope: research practice spanning multiple platform teams.
- **E5** - Depth: **Establishes the organization's standing platform research practice** - instrumented feedback loops, research repositories, and a cadence leaders cite in planning. Scope: how the whole platform organization learns about its users.
- **E6** - Depth: **Represents the internal developer experience at company level**, bringing longitudinal user evidence that redirects company-scale platform investment. Scope: company-wide developer population.

#### Adoption & success metrics

*Anchor:* Forsgren, Humble & Kim, *Accelerate* (2018) - *Why:* supplies the outcome metrics that make voluntary platform adoption measurable and defensible.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [PM-10](../../data/capabilities.md#pm-10) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Pulls and charts existing adoption and usage numbers accurately when asked**, and explains what each metric does and does not show. Scope: metrics for a single feature or task.
- **E2** - Depth: **Instruments their component with adoption, retention, and satisfaction signals** and reviews them in team rituals, spotting when a launch quietly failed to land. Scope: one component's metric set.
- **E3** - Depth: **Defines the success metrics for a capability** - voluntary adoption, time-to-onboard, retention, satisfaction - and kills or reworks features the numbers say are not earning use. Explicitly distinguishes mandated usage from chosen usage in reporting. Scope: a capability's product scorecard, reviewed with its internal customers.
- **E4** - Depth: **Standardizes how several platform teams measure adoption so their numbers compose**, and uses cross-team funnels to find where users leak off the paved road. Challenges vanity metrics in other teams' reviews. Scope: comparable measurement across multiple teams.
- **E5** - Depth: **Owns the organization's platform scorecard** - the small set of adoption and developer-outcome metrics leadership steers by - and ties platform investment cases to it. Scope: organization-level platform health.
- **E6** - Depth: **Frames platform value in company terms** - delivery performance, engineering cost, risk - and defends or redirects company-scale investment with that evidence. Scope: company investment decisions.

### Platform Strategy & Scope

#### Thinnest viable platform

*Anchor:* Skelton & Pais, *Team Topologies* (2019) - *Why:* defines the Thinnest Viable Platform - the sizing test every build-buy-adopt and retirement decision here is judged against.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [proposed](../../contrib/2026-07-thinnest-viable-platform.md) (OPS-31 candidate) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Checks for an existing tool, service, or open-source option before writing new code** and asks whether a proposed task is needed by a real user, citing the request that motivates it. Scope: their own task queue.
- **E2** - Depth: **Proposes wrapping or configuring an existing service instead of building new when it meets the need**, writing the comparison down and defending the removal of unused features. Scope: build-versus-reuse choices in one component.
- **E3** - Depth: **Keeps a capability at its thinnest viable size** - makes explicit build-buy-adopt decisions with documented reasoning, scopes to the thinnest version that serves proven demand (often a wrapper, a template, or documentation rather than new software), and retires surface area that no longer earns its maintenance cost. Scope: a capability's whole footprint.
- **E4** - Depth: **Arbitrates overlap and sprawl between platform teams** - merging duplicate offerings, cutting under-used surface, and setting the bar for what deserves to be platform at all. Scope: portfolio boundaries across multiple teams.
- **E5** - Depth: **Shapes the organization's platform boundary** - what the platform will and will not own versus product teams and vendors - and retires whole offerings whose maintenance cost exceeds their leverage. Scope: the organization's platform portfolio.
- **E6** - Depth: **Keeps the company's platform ambition honest** - publicly weighing platform build-out against buying, adopting open source, or doing nothing, in principles executives reference. Scope: company build/buy/retire posture.

#### Platform roadmap & prioritization

*Anchor:* Perri, *Escaping the Build Trap* (2018) - *Why:* holds the platform roadmap to outcome-over-output product discipline rather than an infrastructure ticket queue.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [PM-05](../../data/capabilities.md#pm-05) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Explains why their current task is on the roadmap** and which named internal customer it serves; flags when a task seems disconnected from user need. Scope: their own task queue.
- **E2** - Depth: **Sequences their component's backlog by user impact** - writes short proposals that weigh demand evidence against effort and negotiates scope with their lead. Scope: one component's roadmap.
- **E3** - Depth: **Owns the roadmap for a platform capability** - balances new features, migrations, deprecations, and operational debt with explicit trade-off reasoning, and says no to requests with a documented rationale that users accept. Scope: a capability across its customer teams.
- **E4** - Depth: **Aligns roadmaps across platform teams** - surfaces collisions and gaps between team plans and brokers the sequencing that unblocks shared bets. Scope: multi-team planning cycles.
- **E5** - Depth: **Drives the platform organization's investment strategy** - the annual plan's biggest items trace to cases they built, including the ones that redirect headcount. Scope: organization.
- **E6** - Depth: **Sets multi-year platform direction for the company** - decides which capabilities the company builds, buys, or retires, and the bets hold up over years. Scope: company-wide.

### Developer Experience

#### Golden paths & paved roads

*Anchor:* Spotify Engineering, "How We Use Golden Paths to Solve Fragmentation in Our Software Ecosystem" (2020) - *Why:* the named industry pattern this competency's templates, defaults, and escape hatches implement.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-27](../../data/capabilities.md#ops-27) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Follows the golden path as a real user would and reports exactly where it breaks** - files precise friction reports against templates, docs, and starter kits. Scope: their own use of the paved road.
- **E2** - Depth: **Builds and maintains golden-path assets for their component** - templates, scaffolding, and starter repos kept working, current, and tested - and fixes path breakages users report within the team's SLA. Scope: one segment of the paved road.
- **E3** - Depth: **Designs a golden path for a whole use case end to end** - from repo creation to production - that a new team completes without hand-holding, with visible escape hatches that are not the default. Makes the paved road easier than the workaround rather than mandating it, and tracks completion rates and drop-off points. Scope: the default path for every team using the capability.
- **E4** - Depth: **Reconciles golden paths across teams into coherent journeys**, deciding where paths diverge legitimately versus where fragmentation is accidental, and reviews new paths before launch. Scope: the portfolio of paths across multiple platform teams.
- **E5** - Depth: **Defines the organization's paved-road strategy** - which paths exist, what support each tier gets, and how off-road teams re-board - and drives the long tail of snowflake systems onto supported paths. Scope: organization-wide path portfolio.
- **E6** - Depth: **Makes the paved road the company default by economics and quality, not policy** - visible in most new services starting on-path without a mandate. Scope: company-wide engineering practice.

#### Cognitive load reduction

*Anchor:* Skelton & Pais, *Team Topologies* (2019), applying Sweller's cognitive load theory (1988) - *Why:* makes load reduction the platform's defining purpose rather than optional polish.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [proposed](../../contrib/2026-07-cognitive-load-management.md) (OPS-32 candidate) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Names the exact docs, errors, and setup steps that forced them to understand internals a user should not need**, and files concrete simplification issues. Scope: workflows they personally execute.
- **E2** - Depth: **Reduces the concepts and steps a user must hold to use their component** - collapsing configuration, defaulting decisions, rewriting errors to say what to do next - and shows the before/after. Scope: one component's user-facing surface.
- **E3** - Depth: **Designs a capability's abstractions around what users must not have to know** - a first-time user succeeds without reading internals - measuring load with time-to-first-success and support-ticket themes and treating regressions as defects. Scope: a capability's entire developer-facing surface.
- **E4** - Depth: **Audits cognitive load across team boundaries** - quantifies onboarding time, concepts-to-learn, and ticket themes - and drives the cross-team simplifications no single team could make. Scope: workflows spanning multiple platform teams.
- **E5** - Depth: **Makes cognitive load a first-class organizational measure** - sets load budgets for what a product team must and must not need to know to ship, and vetoes platform designs that externalize complexity onto product teams. Scope: the platform organization's whole surface area.
- **E6** - Depth: **Shapes company technology and team-boundary choices explicitly around team cognitive load**, arguing in writing for fewer, deeper abstractions over sprawling optionality. Scope: company operating model.

---

## Platform Software Engineering

### Design & Architecture

#### Platform system design

*Anchor:* Conway, "How Do Committees Invent?" (Datamation, 1968) - *Why:* platform architecture and team boundaries must be designed together, or Conway's Law designs them for you.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [SWE-05](../../data/capabilities.md#swe-05) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Explains the platform's architecture in their own words** and navigates its diagrams to find the code that matters for a task; implements designs specified by others, asking questions that surface hidden assumptions. Scope: implements within an existing design.
- **E2** - Depth: **Designs a component within an established architecture**, writing a short design note that names the alternatives considered, and spots when a change fights the existing structure. Scope: one component's internal design.
- **E3** - Depth: **Selects patterns by trade-off in design docs that name alternatives, failure modes, and evolution paths** - designs multi-tenant platform services for isolation, quota, and noisy-neighbor behavior, and catches coupling and scaling problems in others' designs before build. Scope: owns architecture for a capability and runs its design reviews.
- **E4** - Depth: **Drives designs that cut across several teams' systems** - shared control planes, tenancy models, extension points - and gets them agreed in writing. Scope: architecture spanning multiple teams' services.
- **E5** - Depth: **Sets the architectural direction the platform organization builds against** and removes the systemic obstacles - legacy coupling, ownership gaps - that block it. Scope: organization-wide platform architecture.
- **E6** - Depth: **Makes the company's foundational architecture bets** - the small number of structural decisions everything else assumes - and answers for the ones that fail. Scope: company architecture.

#### API & interface design

*Anchor:* Winters, Manshreck & Wright, *Software Engineering at Google* (2020) - Hyrum's Law - *Why:* justifies treating interfaces as long-lived contracts and breaking changes as incidents.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [SWE-07](../../data/capabilities.md#swe-07) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Uses the platform's APIs correctly from documentation alone** and files precise reports where docs and behavior diverge; small additions match naming and error conventions without being told. Scope: consumes and extends interfaces on assigned tasks.
- **E2** - Depth: **Extends a component's interface without breaking consumers** - additive changes, correct versioning, honest error messages - and writes contract tests for the behavior promised. Scope: one component's public surface.
- **E3** - Depth: **Designs a capability's interface as a long-lived product contract** - consistent naming, misuse-resistant defaults, explicit versioning and compatibility guarantees, errors a user can act on without reading source - and treats a breaking change to users as an incident. Reviews proposed interfaces for what users will accidentally depend on. Scope: the contract surface of a capability and its review bar.
- **E4** - Depth: **Aligns interface conventions across several teams' APIs so the platform feels like one product**, and adjudicates breaking-change disputes between producers and consumers. Scope: interface consistency across multiple teams.
- **E5** - Depth: **Owns the organization's interface standards** - versioning policy, deprecation windows, compatibility rules - and the review mechanism that enforces them without bottlenecking teams. Scope: organization-wide interface governance.
- **E6** - Depth: **Sets the company's contract with its developers** - which guarantees the company makes, for how long, to whom - and the fundamental interfaces carry their design signature for years. Scope: company-level contracts.

### Code Craft & Quality

#### Coding & implementation

*Anchor:* Fowler, *Refactoring* (2nd ed., 2018) - *Why:* sets the craft bar for platform code that many teams depend on.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [SWE-02](../../data/capabilities.md#swe-02) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Ships small, working changes that follow the codebase's conventions and pass review with minor feedback** - readable diffs, honest naming - and responds to review by fixing the class of problem, not just the instance. Scope: task-sized changes with guidance.
- **E2** - Depth: **Ships production-quality code independently** - handles error paths, concurrency, and upgrade safety in platform code other teams depend on - and leaves code measurably better in the course of feature work without being asked. Scope: the components they own.
- **E3** - Depth: **Writes the code others study to learn how it is done here** - reference implementations, hardened shared libraries, tricky migration code - and holds the quality bar for a capability, judging when good-enough is correct and saying so. Scope: a capability's codebase, including its shared libraries.
- **E4** - Depth: **Raises the code-health baseline across teams** - shared linting, library patterns, exemplar code others copy - measured by falling defect and review-cycle trends, and personally unblocks the hardest technical problems wherever they sit. Scope: multiple teams' codebases.
- **E5** - Depth: **Defines what code quality means for the organization** - the standards, tooling, and paved-road defaults that make the good way the easy way - and shows the results in delivery data. Scope: organization-wide engineering quality.
- **E6** - Depth: **Holds the company's long-horizon code health against short-term pressure**, publicly making the economic case for maintenance investment, and still writes code in the highest-leverage places. Scope: company code health.

#### Code review

*Anchor:* Sadowski et al., "Modern Code Review: A Case Study at Google" (ICSE-SEIP, 2018) - *Why:* grounds the progression from catching defects to calibrating review culture.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [SWE-04](../../data/capabilities.md#swe-04) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Reviews peers' changes for readability and test coverage and asks genuine questions**; responds to feedback on their own changes without defensiveness. Scope: changes within their team.
- **E2** - Depth: **Gives reviews that catch real defects** - correctness, error handling, compatibility - in actionable, kind comments, and distinguishes blocking issues from preferences explicitly. Scope: their component and its neighbors.
- **E3** - Depth: **Reviews for systemic risk, not just correctness** - catches designs-in-disguise, breaking changes to platform users, and operational hazards - and their comments teach the principle behind the correction; engineers seek their review by choice. Scope: review authority across a capability.
- **E4** - Depth: **Calibrates review culture across teams** - sets what blocks a merge platform-wide, coaches reviewers, and steps into contentious reviews as the tiebreaker whose reasoning both sides accept. Scope: multiple teams' review culture.
- **E5** - Depth: **Designs the organization's quality gates** - decides where human review, automation, and ownership boundaries sit so review load scales with the organization. Scope: organization.
- **E6** - Depth: **Reviews the changes that change the company** - the riskiest cross-cutting designs and migrations route to them by reputation, and their judgment is treated as the final technical check. Scope: company.

#### Testing & verification

*Anchor:* Cohn (2009) as refined by Vocke, "The Practical Test Pyramid" (2018) - *Why:* gives the coverage-balance and contract-testing discipline platform release confidence rests on.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [SWE-03](../../data/capabilities.md#swe-03) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Writes unit tests that pin the behavior of their change, including the failure path**, and runs the affected suite before requesting review; reproduces a bug with a failing test before fixing it. Scope: tests for their own tasks.
- **E2** - Depth: **Balances unit, integration, and end-to-end coverage for their component** and fixes flaky tests instead of retrying them, keeping the suite fast and trustworthy. Scope: one component's test strategy.
- **E3** - Depth: **Designs the verification strategy for a capability** - contract tests on its API, upgrade and rollback tests, failure injection where users would feel it - and blocks releases the strategy does not cover, deleting low-value tests as readily as adding good ones. Scope: a capability's release confidence.
- **E4** - Depth: **Builds test infrastructure several teams rely on** - shared harnesses, ephemeral environments, contract-test brokers - and drives down cross-team integration escapes and flake rates. Scope: verification across multiple teams.
- **E5** - Depth: **Sets the organization's testing standards** and invests where escaped defects cluster, visible in trend lines leadership reviews. Scope: organization-wide verification practice.
- **E6** - Depth: **Frames verification as company risk management**, deciding where the company buys confidence with testing versus operational safeguards. Scope: company risk posture.

### Delivery Automation

#### Delivery automation & CI/CD

*Anchor:* Humble & Farley, *Continuous Delivery* (2010) - *Why:* defines the deployment pipeline behind pipeline-as-product and making the safe path the easy path.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-02](../../data/capabilities.md#ops-02) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Ships through the pipeline correctly** - green builds, small batches - and reads pipeline failures to their cause before asking for help. Scope: their own changes.
- **E2** - Depth: **Owns their component's pipeline** - faster feedback, deterministic builds, automated rollback - and treats a red main branch as the team's top interrupt. Scope: one component's delivery path.
- **E3** - Depth: **Designs CI/CD as a product for a capability's users** - reusable pipeline templates, progressive delivery with canaries and feature flags, automated rollback triggers - so risky changes ship safely by default, and tracks its DORA metrics as product metrics. Scope: the delivery system for a capability and its users.
- **E4** - Depth: **Builds delivery infrastructure multiple teams ship through** and improves their aggregate lead time and change-failure rate, with the before/after measured. Scope: delivery across multiple teams.
- **E5** - Depth: **Owns the organization's delivery architecture** - pipeline standards, environment strategy, release policy - and the metrics program that shows it working. Scope: organization-wide delivery performance.
- **E6** - Depth: **Sets company delivery strategy** - the company's tolerance for speed versus control, and the investments that move both. Scope: company-wide delivery.

#### Deprecation & migration management

*Anchor:* Winters, Manshreck & Wright, *Software Engineering at Google* (2020), deprecation chapter - *Why:* treats deprecation as planned, resourced engineering work with migration paths, not neglect.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-30](../../data/capabilities.md#ops-30) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Executes migration and release steps from a runbook accurately** and reports blockers with reproduction detail. Scope: assigned migration tasks and individual releases.
- **E2** - Depth: **Migrates their component's consumers off an old interface** - versioned releases, working codemods or clear guides, targeted notices, stragglers tracked to zero - with rollback paths they have actually exercised. Scope: one component's releases and migrations.
- **E3** - Depth: **Plans and runs a capability-level deprecation as a managed migration** - usage census, automated tooling for the common case, published timelines with dual-support windows, staged shutoffs with real dates, and support for the hard cases - landing it without surprise breakage or executive escalation. Scope: a capability's lifecycle end to end.
- **E4** - Depth: **Coordinates migrations that cross team boundaries** - sequencing dependencies, building shared tooling, keeping a public burn-down - so no team is stranded. Scope: multi-team migrations.
- **E5** - Depth: **Sets the organization's deprecation policy** - support windows, migration funding rules, sunset criteria - so retirement is routine rather than heroic, and drives org-scale migrations to completion. Scope: organization-wide lifecycle management.
- **E6** - Depth: **Sets the company's compatibility promise** - how long things stay supported, what stability means, and when the company breaks its own users - and drives company-scale technology transitions with multi-year plans that survive reorgs. Scope: company technology lifecycle.

---

## Infrastructure & Cloud

### Cloud & Compute

#### Cloud architecture

*Anchor:* Amazon Web Services, *Well-Architected Framework* (2015-) - *Why:* the industry-standard rubric for the cloud trade-offs this competency makes and reviews.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-01](../../data/capabilities.md#ops-01) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Provisions and modifies cloud resources from documented patterns**, explaining what each resource in their change is for and checking cost implications before creating it. Scope: task-level resources in an existing account structure.
- **E2** - Depth: **Designs the cloud footprint for a component** - networking, storage, compute choices - with a written note on cost and failure-mode trade-offs. Scope: one component's infrastructure.
- **E3** - Depth: **Architects a capability's infrastructure for the failure domains that matter** - zones, regions, quotas, tenancy isolation, dependencies - and defends the design in review against well-architected-style criteria, including cost. Catches single points of failure and blast-radius problems in others' designs. Scope: a capability's cloud architecture.
- **E4** - Depth: **Designs shared infrastructure patterns** - landing zones, network topology, account strategy - that multiple teams inherit rather than reinvent. Scope: infrastructure spanning multiple teams.
- **E5** - Depth: **Sets the organization's cloud strategy** - provider posture, region strategy, cost governance - and reviews major designs against it, owning the trade-offs in front of finance and vendors. Scope: organization-wide cloud estate.
- **E6** - Depth: **Owns company-level infrastructure bets** - multi-cloud versus single, build versus buy at the platform layer, decade-scale commitments - and negotiates the vendor relationships behind them. Scope: company infrastructure strategy.

#### Container orchestration & runtime

*Anchor:* Burns, Grant, Oppenheimer, Brewer & Wilkes, "Borg, Omega, and Kubernetes" (ACM Queue, 2016) - *Why:* explains why orchestration is platform machinery - controllers and declarative desired state - not just deployment tooling.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-14](../../data/capabilities.md#ops-14) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Deploys and debugs workloads on the orchestrator with guidance** - reads events, logs, and resource limits to explain why a workload is not running. Scope: task-level workloads.
- **E2** - Depth: **Owns their component's runtime configuration** - requests and limits, probes, disruption budgets, autoscaling - and tunes it from observed behavior. Scope: one component's runtime.
- **E3** - Depth: **Designs and operates cluster-level platform machinery** - operators and controllers, admission rules, tenancy and isolation boundaries, upgrade strategies - and debugs the control plane itself when abstractions leak. Scope: the runtime backing a capability and its tenants.
- **E4** - Depth: **Sets workload standards multiple teams schedule against** - cluster topology, upgrade cadence, multi-tenancy rules - and runs orchestrator upgrades without user-visible disruption. Scope: shared clusters across multiple teams.
- **E5** - Depth: **Owns the organization's runtime strategy** - cluster fleet architecture, workload placement policy, the abstraction level exposed over raw orchestration. Scope: organization-wide runtime estate.
- **E6** - Depth: **Decides company-level runtime direction** - when to adopt, skip, or exit a foundational compute technology - with published reasoning others cite. Scope: company compute strategy.

#### Networking & compute foundations

*Anchor:* Kurose & Ross, *Computer Networking: A Top-Down Approach* (8th ed., 2021) - *Why:* the standard layered model behind tracing requests and designing topologies across abstraction layers.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-19](../../data/capabilities.md#ops-19) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Traces a request through DNS, load balancer, and service to locate a failure**, narrating the path as they go. Scope: single-workload troubleshooting.
- **E2** - Depth: **Configures the networking and compute for their component** - routing, transport security, capacity class - and explains each choice. Scope: one component's foundations.
- **E3** - Depth: **Designs network and compute topology for a capability** - segmentation, ingress and egress, cross-region traffic - and debugs the problems that cross abstraction layers. Scope: a capability's foundation layer.
- **E4** - Depth: **Owns shared foundations several teams depend on** and leads the gnarliest cross-layer incident investigations. Scope: multi-team shared infrastructure.
- **E5** - Depth: **Sets organization standards for network architecture and compute platforms** and drives the consolidation migrations they imply. Scope: organization.
- **E6** - Depth: **Owns company-scale foundation decisions** - backbone, edge, data-center and cloud boundary - with a written multi-year plan. Scope: company.

### Automation & Self-Service

#### Infrastructure as code

*Anchor:* Morris, *Infrastructure as Code* (O'Reilly, 2016) - *Why:* the discipline behind every plan-review-apply and drift-detection behavior at each level.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-10](../../data/capabilities.md#ops-10) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Makes changes through the IaC workflow rather than the console**, reading plans and diffs to predict what will change before applying. Scope: task-level changes in existing modules.
- **E2** - Depth: **Writes reusable, parameterized modules for their component** with sensible defaults and validation, and untangles state problems - drift, imports - safely. Scope: one component's infrastructure code.
- **E3** - Depth: **Designs the IaC architecture for a capability** - module boundaries, state topology, environment promotion, policy checks in the pipeline - so console drift is the exception that pages someone. Reviews others' infrastructure code for blast radius and reversibility. Scope: a capability's infrastructure codebase.
- **E4** - Depth: **Publishes module libraries and IaC conventions multiple teams build on**, and runs breaking upgrades of shared modules without stranding consumers. Scope: shared infrastructure code across multiple teams.
- **E5** - Depth: **Sets the organization's IaC standards** - tooling, structure, testing, drift policy - and retires the exceptions and legacy hand-managed estates. Scope: organization-wide infrastructure codebase.
- **E6** - Depth: **Treats the company's infrastructure definition as a strategic asset** - portability, auditability, disaster recovery - and directs investment accordingly. Scope: company infrastructure posture.

#### Self-service provisioning

*Anchor:* Bottcher, "What I Talk About When I Talk About Platforms" (martinfowler.com, 2018) - *Why:* the definitional source for removing humans from the request path.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-27](../../data/capabilities.md#ops-27) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Uses the self-service tooling as users do and documents the gaps that forced manual steps** - doc corrections, template fixes, clearer prompts. Scope: individual requests.
- **E2** - Depth: **Automates a manual provisioning flow for their component into a self-service action** with validation and sane defaults, and measures the tickets it eliminates. Scope: one component's provisioning.
- **E3** - Depth: **Designs self-service for a capability end to end** - request, policy checks, provisioning, and day-2 operations like resize and teardown - with guardrails so self-service cannot create unsafe states, driving the ticket queue toward zero and time-to-provision down. Scope: a capability's full self-service lifecycle.
- **E4** - Depth: **Unifies self-service across teams behind one coherent interface** - portal, CLI, or API - with a consistent request-to-ready experience, and holds the bar that new platform features ship self-service by default. Scope: self-service spanning multiple teams' offerings.
- **E5** - Depth: **Drives the organization to a self-service operating model**, reporting ticket-elimination and time-to-ready trends to leadership. Scope: organization-wide provisioning experience.
- **E6** - Depth: **Makes self-service the company's default operating model for infrastructure**, with manual provisioning reduced to signed-off exceptions. Scope: company operating model.

---

## Reliability & Operations

### Observability & Service Levels

#### Observability & instrumentation

*Anchor:* Majors, Fong-Jones & Miranda, *Observability Engineering* (O'Reilly, 2022) - *Why:* sets the bar the telemetry offering at each level is measured against.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-05](../../data/capabilities.md#ops-05) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Reads existing dashboards, logs, and traces to locate a fault**, and adds log lines and metrics to their own changes as a matter of course. Scope: debugging their own tasks.
- **E2** - Depth: **Instruments their component so strangers can debug it** - structured events, useful trace spans, dashboards tied to user symptoms - answering 'what changed and who is affected' without adding code. Scope: one component's telemetry.
- **E3** - Depth: **Designs the observability offering for a capability** - cardinality and cost trade-offs, sampling, correlation across services, out-of-the-box dashboards users get without configuration - and debugs novel production questions from telemetry alone. Makes platform telemetry consumable by users debugging their own workloads. Scope: a capability's observability, including its user-facing telemetry.
- **E4** - Depth: **Builds observability infrastructure multiple teams instrument against** - shared pipelines, conventions, cost governance - and raises the floor of what every team can see. Scope: telemetry across multiple teams.
- **E5** - Depth: **Sets the organization's observability strategy and standards**, retiring tool sprawl, owning the cost curve, and making cross-system debugging routine. Scope: organization-wide observability.
- **E6** - Depth: **Frames observability as company capability** - what the business can and cannot see about its own operation - and directs investment at the blind spots with the largest risk. Scope: company-level visibility.

#### SLOs & error budgets

*Anchor:* Beyer, Jones, Petoff & Murphy (eds.), *Site Reliability Engineering* (O'Reilly, 2016) - *Why:* establishes SLOs, error budgets, and symptom-based alerting as the reliability contract.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-04](../../data/capabilities.md#ops-04) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Explains their service's SLOs and reads burn-rate dashboards correctly**, escalating when budget burn is abnormal and responding to alerts on their own work by the runbook. Scope: awareness on the services they touch.
- **E2** - Depth: **Defines SLIs that reflect user experience for their component** - alert thresholds tied to symptoms rather than causes, runbooks a first-time responder can execute - and prunes noisy alerts. Scope: one component's service levels.
- **E3** - Depth: **Negotiates SLOs for a capability with its internal customers**, sets error-budget policy, wires budgets into release decisions, and visibly changes priorities when the budget is exhausted - feature work stops, reliability work starts. Audits alert quality so pages are actionable and rare. Scope: a capability's reliability contract.
- **E4** - Depth: **Aligns SLOs across dependent services so promises compose** - no service promising more than its dependencies allow - and arbitrates budget disputes between teams. Scope: reliability contracts across multiple teams.
- **E5** - Depth: **Owns the organization's SLO framework and review cadence**, making error budgets the shared currency of reliability decisions in planning. Scope: organization-wide reliability governance.
- **E6** - Depth: **Sets company reliability targets against business risk and cost**, deciding where the company deliberately buys less than five nines. Scope: company reliability posture.

### Incident Management

#### Incident response

*Anchor:* PagerDuty, *Incident Response Guide* (2017) - *Why:* grounds the progression from executing runbooks to designing the response system itself.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-06](../../data/capabilities.md#ops-06) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Executes runbook steps accurately during incidents under supervision** - joins the channel, keeps a timeline, and speaks up when reality diverges from the runbook. Scope: assisting on incidents touching their tasks.
- **E2** - Depth: **Serves as primary on-call for their component** - triages, mitigates first, communicates status on a cadence, and escalates with a clear handoff when out of depth. Scope: one component's rotation.
- **E3** - Depth: **Commands complex multi-team incidents** - structures the response, delegates workstreams, makes mitigation calls under uncertainty, and runs the user-facing communications; responders describe the room getting calmer when they join. Scope: incidents spanning a capability and its dependent teams.
- **E4** - Depth: **Designs the incident-management system itself** - severity schemes, escalation paths, tooling, and on-call health across teams - and steps in as commander for the worst cases. Scope: multiple teams' response system.
- **E5** - Depth: **Owns the organization's major-incident readiness** - drives cross-org drills and game days and is the technical authority leadership expects on the bridge in a crisis. Scope: organization.
- **E6** - Depth: **Leads the company's existential incidents and the reforms after them** - the response to company-threatening events, and the structural changes that follow, are theirs to drive. Scope: company.

#### Learning from incidents

*Anchor:* Allspaw, "Blameless PostMortems and a Just Culture" (Etsy Code as Craft, 2012) - *Why:* establishes blameless analysis focused on systemic contributors over human error.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-06](../../data/capabilities.md#ops-06) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Contributes accurate timelines and observations to incident reviews** and completes the follow-up actions assigned to them on time. Scope: incidents they took part in.
- **E2** - Depth: **Writes blameless postmortems for their component's incidents** - timelines, contributing factors beyond the trigger, and actions that get done rather than logged. Scope: one component.
- **E3** - Depth: **Facilitates incident reviews others attend voluntarily** - surfaces systemic and organizational contributors, extracts themes across incidents, and converts them into platform work that measurably reduces repeats. Scope: a capability's incident record.
- **E4** - Depth: **Builds the learning system across teams** - review standards, cross-team pattern analysis, the feedback loop from incidents into roadmaps - and spots the org-level pattern behind separate teams' incidents. Scope: multiple teams.
- **E5** - Depth: **Drives org-level resilience investment from incident evidence** - the organization's biggest reliability bets cite analysis they produced. Scope: organization.
- **E6** - Depth: **Shapes the company's safety culture** - how the company talks about failure, and what it changes after failure, reflects norms they set. Scope: company.

### Operational Excellence

#### Capacity, performance & cost

*Anchor:* Gregg, *Systems Performance* (2nd ed., 2020) - *Why:* grounds profiling-not-guessing and data-driven capacity planning at every level.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-07](../../data/capabilities.md#ops-07) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Reads utilization and saturation dashboards correctly and flags approaching limits with evidence**, checking the resource impact of their own changes before merge. Scope: resources their tasks touch.
- **E2** - Depth: **Load-tests their component and sizes it from measured headroom rather than guesswork**, profiling the hot path before optimizing and tracking its spend. Scope: one component's capacity and performance.
- **E3** - Depth: **Owns capacity planning for a capability** - forecasts demand ahead of organic and launch-driven growth, sets headroom policy, manages tenant quotas so one user cannot starve the rest, and keeps cost-per-tenant visible so demand self-corrects. Catches the scaling cliff before users hit it. Scope: a capability's capacity, performance, and spend.
- **E4** - Depth: **Runs capacity planning across shared pools that multiple teams draw from**, arbitrating contention with data and driving the efficiency work with the largest aggregate payoff. Scope: shared capacity across multiple teams.
- **E5** - Depth: **Owns the organization's capacity and efficiency program** - forecasting discipline, unit economics, commitment strategy with providers - with a forecast finance trusts. Scope: organization-wide capacity and cost.
- **E6** - Depth: **Treats infrastructure economics as company strategy** - negotiating commitments, setting efficiency targets, deciding when scale justifies structural change. Scope: company infrastructure economics.

#### Toil reduction & automation

*Anchor:* Beyer, Jones, Petoff & Murphy (eds.), *Site Reliability Engineering* (O'Reilly, 2016), toil chapter - *Why:* provides the definition and budget ceiling this competency tracks against.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-28](../../data/capabilities.md#ops-28) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Executes operational runbooks accurately and improves the runbook when a step is wrong or missing**, scripting away repetitive steps in their own work and sharing the script. Scope: assigned operational tasks.
- **E2** - Depth: **Automates the recurring manual work in their component** - scripted, scheduled, or eliminated - and shows the hours reclaimed. Scope: one component's operational load.
- **E3** - Depth: **Measures toil for a capability and holds it under an explicit budget**, designing the operational work out - self-healing, auto-remediation, removing the need entirely - rather than scripting it faster. Scope: a capability's operational model.
- **E4** - Depth: **Builds automation multiple teams reuse for their operational work** and drives down the organization's aggregate on-call load, with the trend visible. Scope: operational load across multiple teams.
- **E5** - Depth: **Sets the organization's toil policy** - measurement, budgets, and the planning rule that reclaims time for engineering work. Scope: organization-wide operational efficiency.
- **E6** - Depth: **Makes operational leverage a company-level argument** - headcount that scales sublinearly with growth - and directs automation investment accordingly. Scope: company operational economics.

---

## Security & Compliance

### Secure by Default

#### Guardrails & policy as code

*Anchor:* OWASP, *Application Security Verification Standard* (v4, 2019) - *Why:* gives guardrail and policy rules an external, auditable bar instead of home-grown opinion.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [proposed](../../contrib/2026-07-guardrails-policy-as-code.md) (SEC-18 candidate) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Works within existing guardrails and reads policy failures to their cause** instead of asking for exemptions, and explains what each guardrail protects against. Scope: their own changes.
- **E2** - Depth: **Writes and tests policy rules for their component** - admission checks, pipeline gates - with low false-positive rates and violation messages that say how to fix the problem. Scope: one component's policy surface.
- **E3** - Depth: **Designs the guardrail architecture for a capability** - what is blocked, warned, or audited, with documented threat reasoning - and tunes it so the safe path is the fast path, measured by exemption-request rates falling; runs the exception workflow without becoming the bottleneck. Scope: a capability's preventive controls.
- **E4** - Depth: **Harmonizes policy across teams into a coherent, versioned policy library** with a real exception process - time-boxed, owned, reviewed - and adjudicates the security-versus-velocity disputes teams escalate. Scope: guardrails spanning multiple teams.
- **E5** - Depth: **Owns the organization's guardrail strategy with security partners** - the control catalog, its coverage, and the evidence it works, moving security from review-time to platform-time. Scope: organization-wide preventive posture.
- **E6** - Depth: **Sets the company's balance of enablement and control**, accountable for guardrails that hold under audit and under attack without strangling delivery. Scope: company control posture.

#### Identity, secrets & access

*Anchor:* Ward & Beyer, "BeyondCorp: A New Approach to Enterprise Security" (;login:, 2014) - *Why:* the identity-centric model behind least privilege, workload identity, and short-lived credentials.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [SEC-01](../../data/capabilities.md#sec-01) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Requests and uses credentials through the sanctioned workflow**, never hard-codes a secret, and reports exposed credentials immediately - and spots one in review. Scope: their own access hygiene.
- **E2** - Depth: **Configures workload identity, scoped roles, and secret rotation for their component**, removing standing permissions it no longer needs. Scope: one component's identity surface.
- **E3** - Depth: **Designs the identity model for a capability** - workload identity, short-lived credentials, least-privilege role structure, break-glass with audit - and reviews access designs for privilege-escalation paths before they ship. Scope: a capability's identity and secrets architecture.
- **E4** - Depth: **Builds identity infrastructure multiple teams authenticate through**, and runs credential-model migrations - long-lived to short-lived, shared to workload identity - without breaking users. Scope: identity across multiple teams.
- **E5** - Depth: **Owns the organization's identity architecture and its zero-trust roadmap**, retiring standing privilege and shared secrets as measurable programs. Scope: organization-wide identity.
- **E6** - Depth: **Sets company identity strategy across employee, workload, and customer boundaries**, and represents it to auditors, partners, and executives. Scope: company identity posture.

### Supply Chain & Assurance

#### Software supply chain security

*Anchor:* OpenSSF, *SLSA: Supply-chain Levels for Software Artifacts* (2021) - *Why:* the graded build-integrity standard the signing, provenance, and admission controls here implement.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [SEC-09](../../data/capabilities.md#sec-09) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Keeps dependencies current on their tasks and acts on vulnerability-scanner findings with guidance**, distinguishing exploitable from noise with help. Scope: dependencies in their own changes.
- **E2** - Depth: **Maintains their component's supply-chain hygiene** - pinning, update cadence, accurate software inventories, signed artifacts - and remediates vulnerabilities within the team's SLA. Scope: one component's supply chain.
- **E3** - Depth: **Designs a capability's pipeline to a stated supply-chain integrity level** - provenance generation, signed artifacts, isolated builds, admission verification - and can show the attestation chain for any production artifact; leads the response when a dependency compromise hits. Scope: a capability's build-to-deploy integrity.
- **E4** - Depth: **Builds supply-chain controls into the shared pipeline so every team inherits provenance and scanning by default**. Scope: supply-chain posture across multiple teams.
- **E5** - Depth: **Owns the organization's supply-chain security program** - target levels, coverage, exception burn-down - reported against a public roadmap. Scope: organization-wide supply chain.
- **E6** - Depth: **Sets company supply-chain policy including third-party and vendor software**, and answers for it to customers and regulators. Scope: company supply-chain posture.

#### Compliance & audit readiness

*Anchor:* NIST, *OSCAL - Open Security Controls Assessment Language* (1.0, 2021) - *Why:* makes compliance-by-default and continuous evidence collection a tooled practice rather than paperwork.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [OPS-09](../../data/capabilities.md#ops-09) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Follows the platform's compliance procedures accurately** - change records, access reviews - and asks why a control exists rather than routing around it. Scope: their own work's compliance hygiene.
- **E2** - Depth: **Automates evidence collection for their component's controls** so audit requests are answered from systems, not screenshots. Scope: one component's control evidence.
- **E3** - Depth: **Maps a capability's controls to the frameworks the company answers to and designs them to be inherited** - teams building on the capability get the control satisfied by default - and walks auditors through the design credibly. Scope: a capability's compliance surface.
- **E4** - Depth: **Rationalizes overlapping control implementations across teams into shared, platform-enforced controls**, cutting per-team audit effort measurably. Scope: compliance across multiple teams.
- **E5** - Depth: **Owns the organization's compliance-as-code strategy with legal and security partners** - which frameworks, which inherited controls, what the audit story is. Scope: organization-wide compliance architecture.
- **E6** - Depth: **Shapes company posture on regulatory strategy where infrastructure is implicated** - data residency, certifications worth pursuing - as an input to market decisions. Scope: company regulatory posture.

---

## Communication & Collaboration

### Knowledge & Documentation

#### Technical documentation

*Anchor:* Procida, *Diataxis* (2017-) - *Why:* the framework behind docs organized by user need rather than system internals.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [DR-05](../../data/capabilities.md#dr-05) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Fixes documentation errors they hit instead of working around them**, and writes accurate task-level notes others can follow. Scope: docs for their own tasks.
- **E2** - Depth: **Keeps their component's docs shippable** - a quickstart that works, reference that matches behavior - and treats doc bugs from users as real bugs. Scope: one component's documentation.
- **E3** - Depth: **Designs a capability's documentation as part of the product** - tutorial, how-to, reference, and explanation each doing their distinct job - instrumented for where readers fail, with recurring support questions treated as doc defects to fix at the source. Scope: a capability's doc set and information architecture.
- **E4** - Depth: **Sets documentation conventions multiple teams follow** and builds the docs infrastructure - templates, testable examples, freshness checks - that keeps them true. Scope: documentation across multiple teams.
- **E5** - Depth: **Owns the organization's developer-facing knowledge strategy**, making docs quality a reviewed, measured property of every platform launch. Scope: organization-wide platform documentation.
- **E6** - Depth: **Writes the canonical company documents** - architecture primers, technology strategy - that onboard leaders and engineers alike for years. Scope: company-level canon.

#### Design communication & decision records

*Anchor:* Winters, Manshreck & Wright, *Software Engineering at Google* (2020), design-docs chapters - *Why:* grounds decision-oriented writing as the mechanism by which trade-offs get decided once and stick.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [CC-01](../../data/capabilities.md#cc-01) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Writes clear tickets, PR descriptions, and status updates that need no follow-up questions**, and asks questions in review that improve their understanding. Scope: their own changes and task communication.
- **E2** - Depth: **Writes short design docs that state the problem, options, and recommendation**, readable by a non-expert teammate, and records the decision so others can revisit it. Scope: component decisions.
- **E3** - Depth: **Writes design docs that make complex trade-offs decidable by non-experts** - alternatives honestly weighed, decision record kept - tailoring the same content for engineers, users, and leaders, and runs technical discussions that converge instead of circling. Scope: capability-level decisions.
- **E4** - Depth: **Writes the cross-team proposals that settle contested technical questions**, absorbing objections into the doc rather than the hallway, so decisions are made once and stick. Scope: technical discourse across multiple teams.
- **E5** - Depth: **Sets the organization's bar for decision writing** - templates, norms, decision records, review forums - and models it in documents others circulate as examples. Scope: organization-wide technical communication.
- **E6** - Depth: **Communicates deep technical trade-offs to executives in the language of business risk without losing correctness** - company technical direction in writing both audiences act on. Scope: company-level technical communication.

### Enablement & Stakeholders

#### Platform advocacy & enablement

*Anchor:* CNCF TAG App Delivery, *Platform Engineering Maturity Model* (2023) - *Why:* frames adoption-by-evangelism as a maturity outcome the platform earns, not a mandate.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [DR-01](../../data/capabilities.md#dr-01) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Answers user questions in support channels accurately or routes them fast**, and demos their own work clearly to the team. Scope: individual users' questions.
- **E2** - Depth: **Runs enablement for their component** - demos, office hours, onboarding sessions, launch notes users actually read - and turns repeated questions into docs or fixes. Scope: one component's user community.
- **E3** - Depth: **Drives adoption of a capability through evangelism rather than mandate** - launch communications, migration workshops, early-adopter partnerships, champion networks inside customer teams - converting skeptical teams with working proof, not slideware; adoption curves move when they run a campaign. Scope: a capability's internal market.
- **E4** - Depth: **Builds the enablement machinery platform teams share** - champions programs, internal conferences, onboarding curricula, launch playbooks - that outlive any one campaign. Scope: advocacy infrastructure across multiple teams.
- **E5** - Depth: **Owns the platform's internal brand and narrative** - leaders and engineers describe what the platform is for in the platform team's own words, and internal satisfaction signals show it. Scope: organization-wide platform narrative.
- **E6** - Depth: **Represents the company's engineering platform externally** - talks, publications, community leadership - in ways that visibly aid hiring and credibility; inside, their voice moves executive opinion. Scope: company reputation and industry.

#### Stakeholder management

*Anchor:* Larson, *Staff Engineer: Leadership Beyond the Management Track* (2021) - *Why:* grounds the progression from reporting status to advising leadership as a peer.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [PM-13](../../data/capabilities.md#pm-13) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Communicates status honestly and early - especially bad news** - and asks stakeholders clarifying questions before building. Scope: their own tasks' stakeholders.
- **E2** - Depth: **Manages expectations for their component with its consuming teams** - what is supported, what is coming, what will not happen - in writing, closing the loop on every commitment made. Scope: one component's consumers.
- **E3** - Depth: **Runs the stakeholder relationships for a capability** - chooses and names the interaction mode for each relationship, renegotiates it when it stops fitting, and has the hard conversations about what the platform will not do; escalations from their stakeholders are rare and non-surprising. Scope: a capability's customer and leadership stakeholders.
- **E4** - Depth: **Aligns competing demands from multiple teams into a roadmap each can live with**, making the trade-offs and losers explicit rather than hidden, and steps into the conversations where trust between platform and a customer team has broken. Scope: stakeholders across multiple teams.
- **E5** - Depth: **Manages the platform's relationship with organization leadership** - funding cases, expectation setting, honest reporting when bets miss. Scope: organization-level stakeholders.
- **E6** - Depth: **Operates at executive level as the technical counterpart on company decisions that touch the platform** - vendor deals, diligence, board-visible commitments. Scope: company-level stakeholders.

#### Cross-team collaboration

*Anchor:* Skelton & Pais, *Team Topologies* (2019) - team interaction modes - *Why:* gives platform-to-team relationships a deliberate design vocabulary rather than ad-hoc liaison work.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [CC-03](../../data/capabilities.md#cc-03) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Works in the open** - asks questions in public channels, asks for help before being stuck a full day, shares progress and blockers early, and follows through on commitments to teammates. Scope: within their team.
- **E2** - Depth: **Partners directly with the teams that consume their component** - joins their planning when changes affect them, embeds with a consuming team when needed, and brings what they learn back as platform improvements. Scope: neighboring teams.
- **E3** - Depth: **Builds the working relationships a capability depends on** - negotiates interfaces and timelines with dependent teams, resolves cross-team disagreements by finding the shared goal and proposing options rather than positions - and is who other teams request by name. Scope: the web of teams around a capability.
- **E4** - Depth: **Creates the collaboration structures that let teams decide without escalation** - working groups, RFC forums, decision venues where cross-team platform issues actually get settled. Scope: multiple teams.
- **E5** - Depth: **Brokers alignment between organizations** - platform, product, security, and finance leaders act on shared plans they assembled - and repairs broken inter-team relationships in the organization's most visible forums. Scope: across org boundaries.
- **E6** - Depth: **Aligns the company's technical factions** - the durable settlements between competing technical camps carry their fingerprints. Scope: company.

---

## Execution & Leadership

### Delivery & Planning

#### Planning & estimation

*Anchor:* McConnell, *Software Estimation: Demystifying the Black Art* (2006) - *Why:* establishes estimates as probability ranges refined by decomposition and historical data.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [PD-04](../../data/capabilities.md#pd-04) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Breaks an assigned task into steps, estimates them honestly, and flags slippage as soon as it is visible** rather than at the deadline. Scope: their own task plans.
- **E2** - Depth: **Plans component-level work in increments that ship value early** - milestones, dependencies, a definition of done - and re-plans openly when discovery changes the picture; their estimates are trusted inputs to team commitments. Scope: one component's plan.
- **E3** - Depth: **Plans a capability across quarters with explicit risk buffers** - sequencing platform work against customer-team launch dates, reserving capacity for interrupts - and their dates are ones other teams schedule against; replans visibly when assumptions break. Scope: a capability's roadmap execution.
- **E4** - Depth: **Builds plans that coordinate multiple teams' streams** - dependencies mapped, integration points dated, slack placed where risk is - and keeps them credible through change. Scope: multi-team programs.
- **E5** - Depth: **Runs the organization's platform planning cycle**, reconciling bottom-up team plans with top-down strategy into commitments leadership can rely on. Scope: organization-wide planning.
- **E6** - Depth: **Plans in company horizons** - multi-year technical programs whose sequencing survives reorgs and leadership changes. Scope: company planning horizon.

#### Prioritization & trade-off judgment

*Anchor:* Reinertsen, *The Principles of Product Development Flow* (2009) - *Why:* gives trade-off and scope-cut decisions an economic footing instead of loudest-voice ordering.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [PD-02](../../data/capabilities.md#pd-02) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Works their queue in the agreed order and raises it explicitly when a new ask conflicts with committed work** rather than silently absorbing it. Scope: their own queue.
- **E2** - Depth: **Orders their component's backlog by user impact and cost of delay**, defending the ordering when challenged and saying no with a reason and an alternative. Scope: one component's backlog.
- **E3** - Depth: **Sequences a capability's investment across feature work, reliability, migrations, and toil paydown using explicit cost-of-delay reasoning** - cuts scope deliberately under pressure, publishes the not-doing list, and says no in writing with the reasoning attached. Scope: a capability's investment mix.
- **E4** - Depth: **Arbitrates priority across teams competing for shared platform capacity**, making the economic trade-offs visible so decisions survive the meeting. Scope: prioritization across multiple teams.
- **E5** - Depth: **Sets the organization's platform investment allocation** - run versus grow versus transform - rebalancing it on evidence and killing zombie projects. Scope: organization-wide investment.
- **E6** - Depth: **Advises company leadership on technology sequencing** - what to do now, next, never - with reasoning that holds up years later. Scope: company sequencing.

### Growth & Direction

#### Mentorship & knowledge sharing

*Anchor:* Lave & Wenger, *Situated Learning: Legitimate Peripheral Participation* (1991) - *Why:* expertise spreads through communities of practice, from peripheral participation inward.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [LI-01](../../data/capabilities.md#li-01) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Asks for help effectively - showing what they tried - and passes on what they learn** in docs and team channels where the next new person will find it. Scope: their own learning loop.
- **E2** - Depth: **Onboards new teammates with pairing and honest context**, and gives specific, kind feedback in reviews that juniors visibly act on. Scope: individuals on their team.
- **E3** - Depth: **Mentors engineers deliberately** - stretch work matched to growth edges, questions before answers, honest feedback delivered kindly - and mentees' independence visibly increases; teaches internal users to self-serve rather than doing it for them, and runs the forums where knowledge crosses the team. Scope: engineers on their team and among their capability's users.
- **E4** - Depth: **Grows senior engineers across teams toward staff scope** - sponsoring visible work, delegating real ownership with backup, coaching design judgment - and is named in others' promotion cases as a reason. Scope: engineers across multiple teams.
- **E5** - Depth: **Builds the organization's technical talent systems** - mentoring structures, promotion calibration input, senior hiring bar - that develop engineers at scale. Scope: organization-wide talent development.
- **E6** - Depth: **Develops the company's next generation of principal-level technical leaders** and shapes the culture they inherit. Scope: company technical leadership pipeline.

#### Technical direction & influence

*Anchor:* Nygard, "Documenting Architecture Decisions" (2011) - *Why:* the practice behind written, revisitable decisions from component decision records to company direction.


| OCF | E1 | E2 | E3 | E4 | E5 | E6 |
|---|---|---|---|---|---|---|
| [LI-03](../../data/capabilities.md#li-03) | [P1](../../data/proficiency_scale.md#p1) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |

- **E1** - Depth: **Forms and voices technical opinions in team discussions**, connecting their tasks to the team's direction, and changes their mind visibly when shown better evidence. Scope: their team's decisions.
- **E2** - Depth: **Proposes direction within their component** - a refactor worth doing, a technology worth adopting - with a written case that weighs alternatives, and sees it through decision to done. Scope: one component's direction.
- **E3** - Depth: **Sets technical direction for a capability** - a written strategy naming the diagnosis, the bet, and what is deliberately not being done, decided through proposals that gather real dissent - revisiting it on evidence rather than sunk cost, and disagreeing-and-committing out loud when overruled. Scope: a capability's technical strategy.
- **E4** - Depth: **Aligns multiple teams behind a shared technical direction without authority over them** - the written proposal, the roadshow, the coalition, the early wins that make it real. Scope: direction across multiple teams.
- **E5** - Depth: **Writes the organization's technical strategy and makes it operational** - reflected in funding, staffing, and what teams say no to; teams cite it in their own planning. Scope: organization-wide technical strategy.
- **E6** - Depth: **Sets company-level technical direction** - the few bets that define engineering for years - and is accountable for their outcome. Scope: company technical strategy.

---

## Sources

Each anchor cited in the matrix, listed once. These ground the competencies; the per-level cell prose follows the CircleCI observable-behavior register and does not paraphrase these works.

- Allspaw, "Blameless PostMortems and a Just Culture" (Etsy Code as Craft, 2012)
- Amazon Web Services, *Well-Architected Framework* (2015-)
- Beyer, Jones, Petoff & Murphy (eds.), *Site Reliability Engineering* (O'Reilly, 2016)
- Beyer, Jones, Petoff & Murphy (eds.), *Site Reliability Engineering* (O'Reilly, 2016), toil chapter
- Bottcher, "What I Talk About When I Talk About Platforms" (martinfowler.com, 2018)
- Burns, Grant, Oppenheimer, Brewer & Wilkes, "Borg, Omega, and Kubernetes" (ACM Queue, 2016)
- CNCF TAG App Delivery, *Platform Engineering Maturity Model* (2023)
- Cohn (2009) as refined by Vocke, "The Practical Test Pyramid" (2018)
- Conway, "How Do Committees Invent?" (Datamation, 1968)
- Forsgren, Humble & Kim, *Accelerate* (2018)
- Fowler, *Refactoring* (2nd ed., 2018)
- Gregg, *Systems Performance* (2nd ed., 2020)
- Humble & Farley, *Continuous Delivery* (2010)
- Kurose & Ross, *Computer Networking: A Top-Down Approach* (8th ed., 2021)
- Larson, *Staff Engineer: Leadership Beyond the Management Track* (2021)
- Lave & Wenger, *Situated Learning: Legitimate Peripheral Participation* (1991)
- Majors, Fong-Jones & Miranda, *Observability Engineering* (O'Reilly, 2022)
- McConnell, *Software Estimation: Demystifying the Black Art* (2006)
- Morris, *Infrastructure as Code* (O'Reilly, 2016)
- NIST, *OSCAL - Open Security Controls Assessment Language* (1.0, 2021)
- Noda, Storey, Forsgren & Greiler, "DevEx: What Actually Drives Productivity" (ACM Queue, 2023)
- Nygard, "Documenting Architecture Decisions" (2011)
- OpenSSF, *SLSA: Supply-chain Levels for Software Artifacts* (2021)
- OWASP, *Application Security Verification Standard* (v4, 2019)
- PagerDuty, *Incident Response Guide* (2017)
- Perri, *Escaping the Build Trap* (2018)
- Procida, *Diataxis* (2017-)
- Reinertsen, *The Principles of Product Development Flow* (2009)
- Sadowski et al., "Modern Code Review: A Case Study at Google" (ICSE-SEIP, 2018)
- Skelton & Pais, *Team Topologies* (2019)
- Skelton & Pais, *Team Topologies* (2019) - team interaction modes
- Skelton & Pais, *Team Topologies* (2019), applying Sweller's cognitive load theory (1988)
- Spotify Engineering, "How We Use Golden Paths to Solve Fragmentation in Our Software Ecosystem" (2020)
- Ward & Beyer, "BeyondCorp: A New Approach to Enterprise Security" (;login:, 2014)
- Winters, Manshreck & Wright, *Software Engineering at Google* (2020) - Hyrum's Law
- Winters, Manshreck & Wright, *Software Engineering at Google* (2020), deprecation chapter
- Winters, Manshreck & Wright, *Software Engineering at Google* (2020), design-docs chapters
