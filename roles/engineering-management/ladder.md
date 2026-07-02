# Engineering Management Career Ladder (M1–M6)

## Calibration Summary

- **Variant:** manager (people-management track). The role is engineering leadership; every level is a leadership job, leveled on demonstrable leadership behavior.
- **Consolidation:** this is a **four-source consolidation** — three independently generated ensemble runs of the career-ladder methodology plus a hand-built engineering-leadership workbook (28 competencies each, ~112 source rows), merged by **union, not intersection**: every genuinely distinct competency from any source survives; nothing was voted out for appearing in only one source. The merge map, agreement statistics, and judgment calls are documented in `runs/consolidation-report.md`.
- **Levels:** six — M1 Engineering Manager (one team) → M2 Senior Engineering Manager (a complex / critical team) → M3 Director (a domain, cross-team) → M4 Senior Director (a sub-org) → M5 VP (a function) → M6 SVP / Org Lead (org-wide). No terminal level in the IC sense: each level is a distinct scope of leadership, not "more of" the level below. Scope widens by adoption breadth and leverage, not headcount.
- **Framework mapping:** every competency carries an `OCF:` reference to the Open Capability Framework catalog (429 capabilities, 36 domains). 32 competencies map to existing capabilities; 11 are proposed additions with contribution drafts under `contrib/`.
- **Counts:** 6 key areas · 18 focus areas · 43 competencies · one citable theory anchor per competency (deduplicated in Sources); every focus area spans at least two competencies.
- **Judgment calls (abridged):** (1) Workbook-derived content is genericized — org-specific calibration and named compliance regimes are generalized to "regulated-industry constraints" where the substance matters. (2) Psychological Safety and Motivation, Engagement & Retention both reference OCF `EM-03`, whose description spans both; a future catalog split is flagged in the report. (3) Build-vs-buy content is folded into Technical Strategy & Investment rather than kept as a separate row. (4) Union preservation puts the competency count slightly above the typical 28–32 for a single-source ladder; the three-tier grouping keeps it ratable.

### Two Dimensions: Competency vs. Scope

This ladder separates two things that org charts blur. **Competency** is what a person does and can demonstrate before they hold the title — behaviors visible to peers, leaders, and reports right now. **Scope** is what the organization grants when a seat opens. The M3–M6 cells are written as indirect-leverage behaviors that are provable early: outcomes achieved through leaders the person develops, mechanisms and standards that teams they do not run choose to adopt, and decisions shaped across the org without formal authority. An honest caveat applies: some accountability at M4–M6 (budget authority, board exposure, final say in a crisis) is only fully exercised in-seat — so read the upper cells as evidence of readiness, not as a claim that the scope is already held.

## Level Overview

| Level | Title | Scope | Focus |
|-------|-------|-------|-------|
| M1 | Engineering Manager | one team | Builds one healthy, delivering team and the management fundamentals — hiring, coaching, planning, delivery. |
| M2 | Senior Engineering Manager | a complex / critical team | Runs a high-stakes, dependency-heavy team independently; multiplies senior ICs; develops practices peers borrow. |
| M3 | Director | a domain (cross-team) | Sets direction and installs mechanisms a cross-team domain adopts; grows leaders; wins outcomes through influence beyond their own team. |
| M4 | Senior Director | a sub-org | Builds the operating system a sub-org runs on — standards, leadership bench, cross-domain trade-offs — so it works without their daily presence. |
| M5 | VP | a function | Drives function-level strategy, talent, and executive partnership; represents engineering to the business. |
| M6 | SVP / Org Lead | org-wide | Sets org-wide direction, culture, and external credibility; makes the company-level bets and builds the succession bench. |

## Competency Matrix

### Leadership & Direction

#### Strategy & Vision

##### Strategy Formulation

*Anchor:* Rumelt, Good Strategy Bad Strategy (2011) — real strategy is a kernel of diagnosis, guiding policy, and coherent action, not goals restated as ambition. *Why:* separating strategy from wishful thinking is the leader's first duty at every scope.
*OCF:* [STRAT-01](../../data/capabilities.md#strat-01) — Corporate strategy formulation · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P5](../../data/proficiency_scale.md#p5) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Writes a team charter that names the problem the team exists to solve** and ties each quarter's plan to an honest diagnosis of the team's real constraints; explains in planning why this, why now — and why not the alternatives. Scope: one team's plan, traceable to org priorities.
- **M2** — Depth: **Frames a critical team's strategy as diagnosis, guiding policy, and coherent action in a document others can challenge**; spots when a "strategy" is goals restated as ambition and reframes it around the actual obstacle; kills or re-scopes work that fails the test. Scope: a complex / critical team; peer managers borrow the framing.
- **M3** — Depth: **Writes the domain strategy several teams plan against**, naming the bets, explicit non-goals, and rejected alternatives; kills initiatives that do not serve it, saying why in the open. Scope: a cross-team domain; cited by teams the author does not run.
- **M4** — Depth: **Reconciles competing team strategies into one coherent investment thesis**, cutting real programs to fund the guiding policy; leaders they coach write strategies that pass the same test. Scope: a sub-org's portfolio; funding and staffing follow the document.
- **M5** — Depth: **Sets multi-year direction for a function and defends its trade-offs at the executive table** with market and delivery evidence; product and finance plans reference its bets. Scope: a function; the strategy shapes decisions in rooms they are not in.
- **M6** — Depth: **Frames the company-level technical bets the executive team commits to**, revising the diagnosis publicly when it changes; leaders at every level can defend the logic. Scope: org-wide; visible in board-level material.

##### Vision & Goal Alignment

*Anchor:* Locke & Latham, "Building a Practically Useful Theory of Goal Setting and Task Motivation" (2002) — specific, difficult goals reliably outperform vague or easy ones; corroborated by Collins & Porras on vivid, durable vision (HBR, 1996). *Why:* translating direction into goals people can hit or miss is the mechanism that turns vision into behavior.
*OCF:* [STRAT-02](../../data/capabilities.md#strat-02) — Strategic planning & OKR cascading · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P5](../../data/proficiency_scale.md#p5) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Translates org direction into team goals specific enough that anyone can say whether they were hit**, restates the why at kickoffs so every engineer can explain it to an outsider, and flags work that ladders to no goal. Scope: one team's goals and their upward trace.
- **M2** — Depth: **Paints a one-page picture of where the team is heading in 12–18 months and repairs vague or sandbagged goals during planning** — leading indicators, counter-metrics against gaming; resets targets publicly when the situation changes rather than quietly redefining success. Scope: a critical team; partners repeat the picture unprompted.
- **M3** — Depth: **Runs the goal cadence a domain uses so objectives interlock across teams**, catching collisions — one team's target is another's counter-metric — before the quarter starts. Scope: cross-team; teams outside their span adopt the cascade format.
- **M4** — Depth: **Builds the goal architecture a sub-org runs on — drafting, calibration, and scoring rituals that function without them in the room** — and aligns leaders with conflicting incentives around one destination. Scope: a sub-org; the cascade holds without their weekly presence.
- **M5** — Depth: **Sets function-level outcomes the business plans around**, brokering trade-offs with product and finance and holding the line when teams optimize local metrics against them. Scope: a function; company scorecards carry their measures.
- **M6** — Depth: **Audits the line of sight from mission to every level's goals and publicly retires goals that no longer serve it**; the org's identity — what it intends to be known for — is repeated until hiring and architecture visibly bend toward it. Scope: org-wide; annual planning starts from their frame.

#### Change & Organizational Design

##### Leading Change

*Anchor:* Kotter, Leading Change (1996) — transformations fail without urgency, a guiding coalition, staged wins, and anchoring in culture. *Why:* engineering leadership is a sequence of migrations, reorgs, and practice shifts that live or die on change mechanics.
*OCF:* [EM-12](../../data/capabilities.md#em-12) — Change & transformation management · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Lands a team-level change by naming the why, piloting it, and following through past the initial dip**; the team can explain the reason, not just the rule. Scope: one team; the change sticks after attention moves on.
- **M2** — Depth: **Sequences a disruptive change on a critical team — migration, re-team, practice overhaul — with a stated case for urgency and staged early wins**, and publicly kills a change that is not working rather than letting it linger. Scope: a complex team; peers copy the rollout plan.
- **M3** — Depth: **Builds the coalition for a cross-team change before announcing it** — recruits early adopters, arms them with evidence, converts skeptics on the record; adoption is voluntary before it is mandatory. Scope: a domain; teams they do not run adopt the change.
- **M4** — Depth: **Runs multiple concurrent changes without exceeding the org's absorption capacity**, with explicit reversal criteria and a communication plan that reaches every affected person before the rumor does; grows the leaders who run the workstreams. Scope: a sub-org; the change sticks after they stop pushing.
- **M5** — Depth: **Leads function-wide transformation with an honest cost narrative executives sign up for**, anchoring the change in reviews, incentives, and hiring criteria so the old way cannot quietly return. Scope: a function; the change model is reused for the next transformation.
- **M6** — Depth: **Times and frames org-wide change against market conditions, absorbing the political cost personally** so teams can execute; the change survives leadership churn because it lives in mechanisms and culture, not in their presence. Scope: org-wide, including external partners and customers.

##### Organizational & Team Design

*Anchor:* Skelton & Pais, Team Topologies (2019), building on Conway, "How Do Committees Invent?" (1968) — team boundaries, cognitive load, and interaction modes determine architecture and flow. *Why:* a leader's most durable decisions are the team shapes and interfaces they leave behind.
*OCF:* [EM-04](../../data/capabilities.md#em-04) — Team design & org structuring · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Shapes roles, ownership boundaries, and on-call load inside the team so work flows without waiting on one person**; flags cognitive overload with evidence — missed reviews, hero patterns — before it burns people out. Scope: one team's internal structure.
- **M2** — Depth: **Redraws a team's boundaries and interfaces when the system outgrows them**, proposing splits or charter changes with a written rationale and showing the load reduction afterward — fewer handoffs, fewer pages, clearer ownership. Scope: a critical team and the seams it shares with neighbors.
- **M3** — Depth: **Designs multi-team boundaries for a domain with the Conway's-law consequences named**, grounded in dependency and flow evidence; neighboring leads co-sign the design, and predicted interface fractures are named before they happen. Scope: a domain's topology; adopted by managers who do not answer to them.
- **M4** — Depth: **Designs a sub-org's structure around the work rather than around people** — platform versus stream teams, interaction contracts, new leadership seats — modeling transition costs and dependencies before the announcement. Scope: a sub-org; the structure outlives them.
- **M5** — Depth: **Sets the function's principles for when to split, merge, or platformize teams**, evolving its shape ahead of scale inflections; structural decisions below them come out consistent without escalation. Scope: a function's topology.
- **M6** — Depth: **Publishes the org-wide design principles other leaders use for their own restructures** and times structural change to strategy rather than crisis. Scope: org-wide; Conway effects are anticipated in company architecture.

#### Alignment & Adaptive Leadership

##### Driving Alignment & Decision Clarity

*Anchor:* Bungay, The Art of Action (2011) — mission command: close the knowledge, alignment, and effects gaps by briefing intent and freeing method. *Why:* teams stall on ambiguous decisions more than hard ones, and leaders convert noise into stated intent, owners, and closure.
*OCF:* [LI-05](../../data/capabilities.md#li-05) — Driving Alignment · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Closes decisions in the room — states the call, the owner, the revisit date — and writes it down where the team works**; ambiguous threads get converted to decisions or killed. Scope: one team's decision log.
- **M2** — Depth: **Briefs intent so well the team makes correct calls in their absence** — the what and why stated, the how left free; drift is caught at the weekly, not the postmortem. Scope: a critical team under ambiguity.
- **M3** — Depth: **Aligns teams they do not run on shared intent — one-page briefs, decision forums with real closure rules**; disagreement moves to disagree-and-commit on record instead of slow-rolling. Scope: cross-team execution.
- **M4** — Depth: **Builds a sub-org's decision architecture — what gets decided where, by whom, how fast** — and unblocks stuck decisions by fixing the process, not just the decision. Scope: a sub-org.
- **M5** — Depth: **Aligns a function with company strategy through briefed intent that executives and engineers repeat verbatim** — the strategy survives three retellings intact. Scope: a function.
- **M6** — Depth: **Keeps an entire org pointed at the same intent through noise — repeats the direction until bored, then repeats it again**; org-wide decisions visibly trace to it. Scope: org-wide coherence.

##### Situational & Adaptive Leadership

*Anchor:* Hersey & Blanchard, Management of Organizational Behavior (1969) — match direction and support to readiness; Heifetz, Leadership Without Easy Answers (1994) — distinguish technical from adaptive challenges. *Why:* there is no single right style; the meta-skill is reading what the person, team, and moment need and flexing from a grounded center.
*OCF:* [proposed](../../contrib/2026-07-situational-adaptive-leadership.md) (LI-08 candidate) · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Matches direction and support to each person's readiness on each task — directing, coaching, supporting, or delegating deliberately** — and tells technical problems from adaptive ones before choosing a fix. Scope: one team's range of people and situations.
- **M2** — Depth: **Flexes skillfully across a wider range of people and harder situations without losing a grounded center**; refuses to force technical fixes onto adaptive challenges and names the difference in the room. Scope: a critical team under conflicting demands.
- **M3** — Depth: **Coaches other leads to read what a person, team, or moment needs**, adapting their own approach across diverse teams while staying recognizably consistent in values. Scope: a domain; leaders cite their situational reads.
- **M4** — Depth: **Develops adaptive leadership as a discipline across a sub-org** — teaches leaders to diagnose technical-versus-adaptive at scale and models changing approach when the situation changes. Scope: a sub-org's leadership practice.
- **M5** — Depth: **Sets the tone for adaptive, authentic leadership across a function**, adjusting their own leadership to what the function needs now rather than what worked last time. Scope: a function.
- **M6** — Depth: **Shapes an adaptive, grounded leadership culture org-wide**, keeping the org's leadership style plastic to conditions while its values stay fixed. Scope: org-wide.

### Execution & Operations

#### Planning & Prioritization

##### Planning & Estimation

*Anchor:* McConnell, Software Estimation: Demystifying the Black Art (2006) — estimates carry a cone of uncertainty that narrows with knowledge, and honest ranges beat confident points. *Why:* credible plans state uncertainty explicitly instead of laundering hope into dates.
*OCF:* [PD-04](../../data/capabilities.md#pd-04) — Estimation & Planning · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Publishes a team plan with ranged estimates and named assumptions**, breaking goals into a realistic, sequenced plan within capacity; re-plans visibly when reality diverges instead of quietly slipping. Scope: one team's quarter.
- **M2** — Depth: **Plans a critical team through dependency-heavy work — sequencing around external teams, buffering the riskiest items first**; their dates are the ones stakeholders trust. Scope: a complex team plus its dependency graph.
- **M3** — Depth: **Runs planning across a domain so team plans compose into one deliverable picture**; surfaces cross-team collisions weeks early and brokers the re-sequencing. Scope: cross-team; teams they do not run plan on their calendar.
- **M4** — Depth: **Builds the planning system a sub-org runs on — cadence, templates, dependency review** — and coaches leaders until plan quality is uniform; slips surface in the mechanism, not in hallway surprise. Scope: a sub-org.
- **M5** — Depth: **Converts portfolio uncertainty into ranged function-level commitments the business plans around**, renegotiating them in the open when the cone of uncertainty narrows. Scope: a function's promises to the company.
- **M6** — Depth: **Sets the org's planning philosophy — horizon, cadence, commitment culture** — and arbitrates when annual bets collide. Scope: org-wide.

##### Prioritization & Trade-offs

*Anchor:* Reinertsen, The Principles of Product Development Flow (2009) — cost of delay and queue economics make prioritization quantitative instead of loudest-voice-wins. *Why:* sequencing decisions are the highest-frequency economic decisions a leader makes.
*OCF:* [PD-02](../../data/capabilities.md#pd-02) — Prioritization & Economic Thinking · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Ranks the backlog with explicit cost-of-delay reasoning and says no with the reasons attached**, showing stakeholders what a new ask displaces; protects committed work from drive-by asks. Scope: one team's queue.
- **M2** — Depth: **Trades scope, quality, and date on a critical deliverable with the reasoning written down**; escalations they raise arrive with options, not just problems. Scope: a complex team; their trade-off memos travel.
- **M3** — Depth: **Arbitrates priority conflicts between teams using a shared economic frame they introduced**, documenting the trade-offs each team accepted so re-litigations point at the record, not the meeting. Scope: cross-team queues in a domain.
- **M4** — Depth: **Kills or defers whole initiatives to keep a sub-org's portfolio inside real capacity, delivering the news to sponsors personally** and publishing the rationale so the decision teaches; leaders they develop make the same call one level down. Scope: a sub-org's portfolio.
- **M5** — Depth: **Sets the investment split across run, grow, and transform for a function with an economic case** finance signs off on, defending it against quarter-to-quarter noise. Scope: a function.
- **M6** — Depth: **Makes the org's few irreversible bets explicitly and stages the reversible ones**, saying no to good ideas in public so the org learns the bar. Scope: org-wide capacity and capital.

#### Delivery & Reliability

##### Predictable Delivery & Execution

*Anchor:* Forsgren, Humble & Kim, Accelerate (2018) — software delivery performance predicts organizational performance and is measurable. *Why:* predictability is the currency managers trade with stakeholders, and delivery is the manager's system to run.
*OCF:* [EM-07](../../data/capabilities.md#em-07) — Delivery & program management · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Runs a delivery cadence where commitments are met or renegotiated early, never silently missed**; delegates, coordinates, unblocks, and flags slips with options, not apologies. Scope: one team's delivery.
- **M2** — Depth: **Keeps delivery predictable on a system with heavy dependencies and legacy drag**, recovering a slipping critical program by re-scoping and communicating the new plan before being asked; runs premortems on critical launches and folds the mitigations into the plan. Scope: a critical path other teams depend on.
- **M3** — Depth: **Runs cross-team delivery with dependencies mapped and integration milestones checked**, negotiating buffers and interface contracts between teams before integration, not after. Scope: a domain-wide program.
- **M4** — Depth: **Builds the program mechanisms — dependency maps, integration checkpoints, single-threaded owners — that let multi-quarter, multi-team programs land**, and coaches other leads to run them. Scope: sub-org-scale programs; the review runs in their absence.
- **M5** — Depth: **Gives executives delivery forecasts they plan the business on, and early warning the moment a forecast breaks**, treating misses as prompts for systemic fixes rather than blame. Scope: a function's commitments and delivery reputation.
- **M6** — Depth: **Sets the org's execution bar — what "on time" and "done" mean — and personally intervenes on the few programs whose failure would be existential.** Scope: org-wide.

##### Incident & Reliability Leadership

*Anchor:* Beyer, Jones, Petoff & Murphy (eds.), Site Reliability Engineering (2016) — error budgets, blameless postmortems, and toil caps make reliability an engineering discipline. *Why:* how a leader behaves during and after incidents sets the org's real safety culture.
*OCF:* [EM-10](../../data/capabilities.md#em-10) — Incident & operational risk management · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Runs blameless postmortems that produce completed actions, not filed documents**; keeps on-call humane — load tracked, handoffs clean, pages actionable. Scope: one team's services and pager.
- **M2** — Depth: **Commands sev-1 incidents on a critical system calmly — clear roles, communication cadence, decision log** — and pushes reliability work onto the roadmap with error-budget evidence; failure is rehearsed with game days. Scope: a critical system and its blast radius.
- **M3** — Depth: **Raises the postmortem and readiness bar across a domain** — SLOs and error budgets adopted by teams they do not run — and eliminates recurring incident classes with systemic fixes instead of three local patches. Scope: cross-team reliability.
- **M4** — Depth: **Builds a sub-org's reliability operating model — SLO governance, severity taxonomy, escalation design, an incident-commander bench — and rehearses it**; the org's worst day runs on mechanisms they installed. Scope: a sub-org.
- **M5** — Depth: **Represents operational risk at the executive table in customer and revenue terms**, setting risk tolerance with the business and defending reliability investment in budget season. Scope: a function's risk position.
- **M6** — Depth: **Represents the org's operational integrity to customers, regulators, and the board during the worst incidents**, and turns them into structural investment. Scope: org-wide trust.

##### Risk Management & Governance

*Anchor:* NIST Cybersecurity Framework (2014) — identify, protect, detect, respond, recover: risk managed as a continuous function, not a project; corroborated by PMI, PMBOK Guide (7th ed., 2021) on risk ownership and response planning. *Why:* risk fails at the management layer — unowned exposures, unfunded mitigations, unmanaged dependencies — more often than at the technical one.
*OCF:* [RISK-01](../../data/capabilities.md#risk-01) — Enterprise risk management · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Keeps a team risk register with named owners and trigger conditions**, treats security and compliance findings as scheduled work with deadlines, and escalates when a trigger fires rather than hoping. Scope: one team's plans and attack surface.
- **M2** — Depth: **Leads a critical system through real risk events — an audit, a coordinated disclosure, a failed dependency** — hardening both the system and the process afterward; near-misses get written up, not shrugged off. Scope: a critical system's risk posture.
- **M3** — Depth: **Normalizes risk practice across a domain — shared register format, review cadence, paved-road controls teams adopt because they are easier than the alternative** — and maps dependency risk between teams before integration. Scope: cross-team risk posture.
- **M4** — Depth: **Builds a sub-org's risk governance — risk-appetite statements, exception processes with expiry dates, compliance readiness under regulated-industry constraints** — surfacing systemic exposures like single points of failure and key-person risk, and funding the mitigations. Scope: a sub-org.
- **M5** — Depth: **Trades risk against delivery at function scale with explicit executive sign-off on accepted risks** — no silent acceptance. Scope: a function.
- **M6** — Depth: **Sets the org's risk appetite and answers for its posture to the board, regulators, and customers**, making the hardest calls — disclosure, shutdown, delay — personally and on record. Scope: org-wide.

#### Operational Excellence

##### Engineering Metrics & Delivery Health

*Anchor:* Forsgren, Humble & Kim, Accelerate (2018) — the DORA four keys (lead time, deploy frequency, time to restore, change-fail rate) predict organizational performance. *Why:* delivery health is measurable, and leaders who instrument it stop arguing from anecdote.
*OCF:* [EM-09](../../data/capabilities.md#em-09) — Engineering metrics & productivity · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Reads the team's core health signals — lead time, deploy frequency, change-fail rate, recovery time, test health — on a cadence and acts on one bottleneck at a time**; distinguishes the metric moving from the system improving. Scope: one team's pipeline.
- **M2** — Depth: **Diagnoses a complex team's delivery drag to root cause — flaky tests, review latency, batch size — and shows the improvement in the numbers**, not just the narrative; the fix holds for quarters. Scope: a critical delivery path.
- **M3** — Depth: **Standardizes delivery measurement across a domain so teams are comparable without being gamed**; distinguishes real health from vanity metrics, and managers they do not oversee run retros off the dashboard they built. Scope: cross-team.
- **M4** — Depth: **Sets delivery-health standards and instrumentation for a sub-org and funds the platform work that moves them**, using trends to guide investment and protecting improvement capacity from roadmap pressure quarter after quarter. Scope: a sub-org.
- **M5** — Depth: **Frames engineering productivity for the executive suite in business terms**, resisting vanity metrics; the function's improvement investments trace to measured constraints. Scope: a function.
- **M6** — Depth: **Makes delivery capability a board-legible asset**, benchmarking the org externally, setting the measurement philosophy, and retiring measures that stop informing decisions. Scope: org-wide.

##### Process Design & Continuous Improvement

*Anchor:* Deming, Out of the Crisis (1986) — improvement comes from acting on the system via Plan-Do-Study-Act and reducing variation, not exhorting individuals; Goldratt's Theory of Constraints adds: optimize the bottleneck, not everything. *Why:* engineers work in the system; managers are the ones positioned to work on it.
*OCF:* [EM-08](../../data/capabilities.md#em-08) — Process & operating-cadence design · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Designs lightweight processes that make good outcomes repeatable and runs retrospectives that produce changes which stick** — the same complaint does not appear three retros running; fixes the actual bottleneck, not everything at once. Scope: one team's system of work.
- **M2** — Depth: **Builds robust process and controls for a critical team — reducing variation in quality and delivery while right-sizing governance** — and institutionalizes plan-do-study-act learning loops. Scope: a critical team's end-to-end flow.
- **M3** — Depth: **Sets consistent process and quality controls across a domain and moves improvements from one team to another with credit given**; targets the domain's real constraint so improvement compounds. Scope: a domain; teams volunteer their data.
- **M4** — Depth: **Builds the operations-review rhythm a sub-org trusts** — leaders bring their own bad news to it because the response is problem-solving, not punishment; consistency is institutionalized through the leaders who run each team. Scope: a sub-org.
- **M5** — Depth: **Sets the function's continuous-improvement strategy and operating-efficiency bar**, justifying investments with trend data that survives finance scrutiny. Scope: a function.
- **M6** — Depth: **Shapes an improvement culture org-wide** — process standards, learning loops, and waste elimination that persist because they are cultural, not mandated. Scope: org-wide.

##### Developer Experience & Flow

*Anchor:* Forsgren et al., "The SPACE of Developer Productivity" (ACM Queue, 2021) — developer productivity is multidimensional, never a single output count. *Why:* the manager owns the system engineers work inside; friction there taxes everything.
*OCF:* [OPS-27](../../data/capabilities.md#ops-27) — Platform & developer-experience engineering · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Removes the team's top friction — flaky CI, slow reviews, meeting load — and measures cycle time before and after.** Scope: one team's daily flow.
- **M2** — Depth: **Instruments developer experience on a critical team with surveys plus system metrics** and fixes the top pain point each quarter, showing the delta. Scope: a critical team's toolchain and process.
- **M3** — Depth: **Prioritizes platform and tooling investment across teams by measured friction**, resisting single-metric productivity theater on the record. Scope: a domain's developer platform.
- **M4** — Depth: **Builds a developer-experience feedback loop a sub-org acts on quarterly** — findings become funded work, and engineers can see it. Scope: a sub-org.
- **M5** — Depth: **Makes the function-wide productivity investment case at the executive table** with multidimensional evidence, and reports back honestly on what worked. Scope: a function.
- **M6** — Depth: **Keeps engineering effectiveness a standing strategic priority rather than a slogan**; the org budgets for it in bad years too. Scope: org-wide.

#### Resource Stewardship

##### Capacity & Headcount Planning

*Anchor:* Brooks, The Mythical Man-Month (1975) — adding people to a late project makes it later; capacity is nonlinear in headcount. *Why:* honest capacity math, including ramp and communication cost, is what separates plans from wishes.
*OCF:* [EM-05](../../data/capabilities.md#em-05) — Headcount & resource planning · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Plans the team's quarter against realistic capacity — on-call, ramp time, keep-the-lights-on — and shows the math when asked to take more.** Scope: one team's capacity.
- **M2** — Depth: **Forecasts capacity across attrition and ramp scenarios**, sequencing hiring so the team never lurches between starving and drowning; declines headcount that would slow the team down and says why. Scope: a complex team's pipeline.
- **M3** — Depth: **Models capacity across several teams and proposes moving work or people to where the constraint actually is**, with the trade-offs written down. Scope: a domain's capacity allocation.
- **M4** — Depth: **Builds the headcount plan a sub-org's budget is built on**, defending it line by line and taking cuts strategically rather than spreading them evenly. Scope: a sub-org planning cycle.
- **M5** — Depth: **Sets the function's location, seniority-mix, and build/contract workforce shape**, tying growth to unit economics executives accept. Scope: a function's workforce plan.
- **M6** — Depth: **Shapes org-wide workforce strategy across cycles — growing, freezing, or reducing — with the org's long-run capability protected in the plan.** Scope: org-wide.

##### Budget & Vendor Stewardship

*Anchor:* Korn Ferry Leadership Architect (2014) — Financial Acumen as a core enterprise-leadership competency (comparison overlay only). *Why:* engineering leaders are judged on cost lines as well as delivery, and cloud-era spend is an engineering decision.
*OCF:* [EM-06](../../data/capabilities.md#em-06) — Budget & vendor management · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Tracks the team's spend — cloud, tooling, services — and catches anomalies before finance does**; makes cost visible on the team's own dashboards. Scope: one team's cost lines.
- **M2** — Depth: **Owns a budget with real variance — forecasts it, explains misses, finds savings that do not damage the roadmap** — and negotiates renewals with usage data in hand. Scope: a critical team's budget and vendors.
- **M3** — Depth: **Finds structural savings across teams — duplicate tooling, idle capacity, overlapping contracts — and lands the consolidation**, funding platform work despite feature pressure and defending the split in the open. Scope: domain-level spend.
- **M4** — Depth: **Runs a full budget cycle for a sub-org, connecting each line to a strategic bet** and reallocating mid-year with a rationale the losing team can repeat accurately; kills spend that has outlived its purpose. Scope: a sub-org budget.
- **M5** — Depth: **Stewards a function's cost structure — unit economics, vendor strategy, location mix — and defends it at the executive and finance table.** Scope: a function's economics.
- **M6** — Depth: **Aligns the org's investment envelope with company strategy and makes its largest financial commitments** — deals sized to be existential get diligence sized to match. Scope: org-wide financial exposure.

### People & Talent

#### Hiring & Team Formation

##### Hiring & Selection

*Anchor:* Schmidt & Hunter, "The Validity and Utility of Selection Methods in Personnel Psychology" (1998) — structured interviews and work samples are among the strongest predictors of job performance; unstructured conversation is mostly noise. *Why:* hiring is the highest-leverage near-irreversible decision a manager makes, and structure is what makes it a skill.
*OCF:* [LI-02](../../data/capabilities.md#li-02) — Hiring & Staffing · targets: M1:[P3](../../data/proficiency_scale.md#p3) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Runs a structured hiring loop — defined signals per interview, written rubrics, evidence-based debriefs — and closes candidates personally with an honest pitch.** Scope: one team's openings.
- **M2** — Depth: **Designs the loop itself for senior and hard-to-fill roles — work samples, calibrated rubrics — and defends bar decisions with evidence over gut feel**; interviewers they trained staff other loops. Scope: a critical team's talent needs and beyond.
- **M3** — Depth: **Sets the hiring bar across a domain — rubric library, debrief standards, a bar-raiser bench — so teams they do not run make comparable decisions**; makes calibration visible with data like pass-through rates and first-year outcomes. Scope: cross-team hiring quality.
- **M4** — Depth: **Builds the hiring machinery a sub-org hires through — interviewer training, bar-raiser pools, leveling guides, sourcing strategy — and personally closes the hires that change a trajectory.** Scope: a sub-org's pipeline.
- **M5** — Depth: **Sets the function's talent-acquisition strategy — where to compete for people and on what basis — with recruiting and finance partners**, holding the bar under growth pressure. Scope: a function's brand and bar.
- **M6** — Depth: **Makes the org a destination for the people it most needs — visible externally, credible internally — and personally recruits the leadership that changes the company's capability.** Scope: org-wide talent brand.

##### Onboarding & Team Formation

*Anchor:* Tuckman, "Developmental Sequence in Small Groups" (1965) — teams predictably move through forming, storming, norming, and performing, and the transitions can be led rather than endured. *Why:* every hire, departure, and reorg resets a team's stage, and leaders who read the stage shorten the trough.
*OCF:* [proposed](../../contrib/2026-07-onboarding-team-formation.md) (EM-13 candidate) · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Runs a 30/60/90 onboarding with named buddies and early wins**; new hires ship in their first weeks and say so in check-ins. Scope: one team's ramp.
- **M2** — Depth: **Reads a team's formation stage and intervenes on it — resets norms after a merge, names storming in the room instead of managing it by email.** Scope: a critical team through churn and growth.
- **M3** — Depth: **Builds the onboarding and team-launch playbook a domain uses**; teams they do not run start faster because of materials and rituals they created. Scope: cross-team.
- **M4** — Depth: **Stands up whole new teams — mission, first hires, norms, interfaces — repeatedly**, and coaches leaders through their first team formations. Scope: a sub-org's growth mechanics.
- **M5** — Depth: **Designs how a function absorbs step-change growth — acquisitions, new sites, doubled headcount — without culture dilution**; integration plans carry named cultural mechanisms. Scope: a function.
- **M6** — Depth: **Makes team formation an org-wide capability — the org spins up new groups predictably without heroics** — and audits that the machinery still works. Scope: org-wide.

#### Coaching & Development

##### Coaching & Development

*Anchor:* Whitmore, Coaching for Performance (1992) — the GROW model turns advice-giving into question-led coaching; Google's Project Oxygen independently found "is a good coach" the top manager behavior. *Why:* a manager's lasting output is the capability of the people they grow.
*OCF:* [LI-01](../../data/capabilities.md#li-01) — Mentorship & Coaching · targets: M1:[P3](../../data/proficiency_scale.md#p3) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Holds weekly one-on-ones that are coaching conversations, not status reads — asks before advising**; each person has a live growth plan they co-wrote. Scope: every individual on one team.
- **M2** — Depth: **Coaches senior engineers and first-time leads through ambiguity they cannot solve for them — scoping staff-level work, brokering visibility** — and is sought out as a coach beyond the team. Scope: a critical team's senior bench.
- **M3** — Depth: **Coaches other people-leads on their coaching — sits in on their reviews on request**; leaders demonstrably improve their practice after working with them, and people across the domain cite their questions as the turning point. Scope: cross-team leadership bench.
- **M4** — Depth: **Builds coaching capability at scale — manager forums, feedback training, calibration on what good coaching looks like — that a sub-org adopts** and keeps running without them. Scope: a sub-org.
- **M5** — Depth: **Develops senior leaders across a function, including peers who seek their counsel**, and sponsors development systems rather than only coaching personally. Scope: a function's leadership pipeline.
- **M6** — Depth: **Sets the org-wide philosophy and systems for talent growth**, and the org's leaders visibly coach because the top does. Scope: org-wide leadership culture.

##### Listening & Feedback

*Anchor:* Scott, Radical Candor (2017) — caring personally while challenging directly beats both ruinous empathy and obnoxious aggression; the SBI model (CCL) grounds feedback in situation, behavior, impact. *Why:* communication is bidirectional — the under-practiced half is listening and delivering truth usefully.
*OCF:* [CC-04](../../data/capabilities.md#cc-04) — Feedback · targets: M1:[P3](../../data/proficiency_scale.md#p3) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Gives specific, behavior-anchored feedback within days — kind and clear, not brutal or vague — and listens to understand, soliciting dissent**; feedback flows both directions in their one-on-ones. Scope: one team.
- **M2** — Depth: **Creates feedback-rich norms on a complex team and handles the hardest feedback conversations well** — hears what is not said, and turns hard feedback into changed behavior within weeks. Scope: a critical team.
- **M3** — Depth: **Builds a candor culture across a domain — models seeking and acting on critical feedback at scale**, setting feedback norms teams they do not run follow. Scope: cross-team norms.
- **M4** — Depth: **Institutionalizes feedback norms across a sub-org through mechanisms — training, calibration on feedback quality — that outlast their attention.** Scope: a sub-org.
- **M5** — Depth: **Coaches at the executive seam — peers and senior leaders take their feedback on leadership behavior**, delivered candidly and in private. Scope: a function's leadership.
- **M6** — Depth: **Models candor at the top — publicly requests, receives, and acts on hard feedback**; the org's norms of directness trace to their visible example. Scope: org-wide.

#### Performance & Advancement

##### Performance Management

*Anchor:* Grove, High Output Management (1983) — task-relevant maturity and the review as a performance-improving tool, not a ritual. *Why:* performance problems age like debt, and differentiated, timely signal is among a manager's highest-leverage duties.
*OCF:* [EM-01](../../data/capabilities.md#em-01) — Performance management & accountability · targets: M1:[P3](../../data/proficiency_scale.md#p3) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Sets explicit expectations per person and level, documents evidence continuously, and delivers reviews with no surprises** — underperformance is named early with a concrete support plan. Scope: their direct team.
- **M2** — Depth: **Handles the hard cases — brilliant-but-corrosive, long-tenured-but-plateaued — with documented, humane processes that end in change or exit inside a quarter or two**, and writes promotion cases that survive committee. Scope: a critical team's full performance range.
- **M3** — Depth: **Runs calibration across teams so the same work earns the same rating regardless of manager**, contesting both inflation and harshness with specifics; coaches managers they do not oversee through their first improvement plans. Scope: cross-team fairness.
- **M4** — Depth: **Designs a sub-org's performance system — rubrics, promotion bars, calibration protocols, appeal paths — and audits its outcomes for drift and bias**; hard calls happen earlier because the system backs the people making them. Scope: a sub-org.
- **M5** — Depth: **Holds senior leaders to the same standard as everyone else — visibly acts on underperformance at high levels**, where the cost of avoidance is largest. Scope: a function's leadership accountability.
- **M6** — Depth: **Sets the org's performance philosophy — what is rewarded, tolerated, and exited — and applies it to the most senior and most protected people first.** Scope: org-wide standards.

##### Career Development & Sponsorship

*Anchor:* Hewlett, Forget a Mentor, Find a Sponsor (2013) — sponsorship (spending capital on stretch, visibility, advocacy) moves careers where mentoring (advice) alone does not. *Why:* growth plus active sponsorship is what actually advances and retains talent.
*OCF:* [EM-02](../../data/capabilities.md#em-02) — Career development & sponsorship · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Knows each person's aspirations, creates stretch scope, and gives honest promotion guidance**; sponsors deserving people in calibration rather than just advising them. Scope: one team's careers.
- **M2** — Depth: **Sponsors people into senior and lead roles — writes compelling cases and spends real capital advocating beyond their own team.** Scope: a critical team's senior transitions.
- **M3** — Depth: **Owns fair, consistent advancement across a domain**, sponsoring senior ICs and emerging leaders into scope they would not get alone. Scope: cross-team advancement.
- **M4** — Depth: **Builds career-path and recognition systems a sub-org adopts, so growth does not require leaving**, and audits promotion rates by cohort for equity. Scope: a sub-org.
- **M5** — Depth: **Shapes the function's leveling and advancement architecture with people-team partners**, sponsoring high-potential leaders into visibility before vacancies force it. Scope: a function.
- **M6** — Depth: **Shapes advancement systems org-wide**; the org's promotion decisions still mean something years later, and its leaders credit named sponsorship. Scope: org-wide.

##### Succession & Leadership Pipeline

*Anchor:* Charan, Drotter & Noel, The Leadership Pipeline (2001) — each leadership passage requires new skills and values, so benches must be built deliberately. *Why:* unplanned succession is an organizational single point of failure.
*OCF:* [HR-09](../../data/capabilities.md#hr-09) — Talent management & succession programs · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Names their own successor risk and grows a deputy — delegating real ownership as development, not offloading**; someone can cover their vacation without incident. Scope: one team's bench.
- **M2** — Depth: **Builds bench depth on purpose — tech-lead rotations, stretch scopes with safety nets** — so the team survives its strongest engineer's departure; people they grew succeed after moving elsewhere, and say so. Scope: a critical team as a leadership incubator.
- **M3** — Depth: **Maintains a live succession slate for every key seat in a domain** and exports leaders to other parts of the org rather than hoarding them. Scope: a domain's bench.
- **M4** — Depth: **Runs talent reviews that end in moves — promotions, rotations, exits — not just ratings**, and builds development mechanisms like acting-role assignments a sub-org adopts. Scope: sub-org pipeline health.
- **M5** — Depth: **Ensures every critical role in the function has a named, developing successor**, reviewing succession with executives before vacancies force it. Scope: a function.
- **M6** — Depth: **Builds the pipeline the org promotes from, including the bench for the top jobs and their own**; top seats fill internally more often than not. Scope: org-wide.

#### Team Health & Culture

##### Psychological Safety

*Anchor:* Edmondson, The Fearless Organization (2018) — psychological safety, the belief that speaking up is safe, is the top predictor of team effectiveness (Google Project Aristotle). *Why:* safety to dissent is the substrate every other team behavior — learning, candor, incident honesty — depends on.
*OCF:* [EM-03](../../data/capabilities.md#em-03) — Team health & engagement · targets: M1:[P3](../../data/proficiency_scale.md#p3) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Responds to bad news by thanking the messenger and models fallibility — says "I was wrong" in front of the team**; the quietest person speaks in their meetings, and interruption and ridicule get shut down on the spot. Scope: one team's meetings and channels.
- **M2** — Depth: **Rebuilds safety where it is damaged — post-incident, post-layoff, post-conflict — measurably**; dissent shows up in decision records again, and dissenters are visibly protected from consequences. Scope: a critical team under pressure.
- **M3** — Depth: **Reads safety across teams from signals — who speaks in reviews, what surfaces in retros versus hallways — and coaches the leads whose teams have gone quiet**; runs pre-mortems and challenge sessions others adopt. Scope: a domain's speak-up climate.
- **M4** — Depth: **Builds channels through which bad news travels up fast — skip-levels, anonymous paths, incident amnesty — and proves they are safe by what happens to the people who use them.** Scope: a sub-org's information flow.
- **M5** — Depth: **Makes dissent safe in executive rooms — invites challenge to their own proposals in front of others and rewards the challengers**; kills shoot-the-messenger behavior among senior leaders where it happens. Scope: a function's leadership culture.
- **M6** — Depth: **Makes it safe to tell the org's most powerful people they are wrong — including themselves, publicly**; the org's biggest failures produce learning documents, not scapegoats. Scope: org-wide culture.

##### Motivation, Engagement & Retention

*Anchor:* Deci & Ryan, Self-Determination Theory (2000) — autonomy, competence, and relatedness drive intrinsic motivation; Herzberg (1968) adds that removing dissatisfiers alone does not create drive. *Why:* engagement is designed through the work itself, and retention is its trailing indicator.
*OCF:* [EM-03](../../data/capabilities.md#em-03) — Team health & engagement · targets: M1:[P3](../../data/proficiency_scale.md#p3) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Knows what motivates each person and matches work to it — removing dissatisfiers and feeding autonomy, mastery, and purpose**; catches disengagement in work patterns before the survey does, and regrettable attrition is rare and predicted. Scope: one team.
- **M2** — Depth: **Keeps a critical team engaged through grind — long migrations, incident sieges — by restoring autonomy and purpose where they have eroded**; re-recruits key people proactively, before the resignation letter. Scope: a high-pressure team.
- **M3** — Depth: **Reads attrition and engagement patterns across teams and fixes the systemic causes — career stagnation, meaningless work — not the symptoms**; managers across the domain apply the playbook to their own teams. Scope: cross-team engagement.
- **M4** — Depth: **Builds the conditions of motivation into a sub-org's operating model — team autonomy, mastery paths, recognition systems — and measures their effect rather than their activity.** Scope: a sub-org.
- **M5** — Depth: **Acts publicly on function-level engagement results — survey outcomes drive visible changes**, and tells executives the truth when money is masking a meaning problem. Scope: a function.
- **M6** — Depth: **Builds an employee value proposition people join and stay for — the story engineers tell friends is the one leadership tells** — with regrettable attrition of critical people treated as a serious incident. Scope: org-wide.

##### Inclusion & Belonging

*Anchor:* Ely & Thomas, "Cultural Diversity at Work" (Administrative Science Quarterly, 2001) — diverse teams outperform only under an integration-and-learning climate where people belong and can contribute. *Why:* mitigating bias in hiring, reviews, and airtime is an active leadership responsibility, not a program someone else runs.
*OCF:* [HR-10](../../data/capabilities.md#hr-10) — DEI program management · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Runs inclusive meetings and decisions — every voice heard, bias mitigated in hiring and reviews**; airtime and credit are tracked, not assumed. Scope: one team.
- **M2** — Depth: **Builds inclusion into a critical team's norms and senior-IC growth — closes equity gaps in scope and visibility** and mentors others in inclusive leadership. Scope: a critical team.
- **M3** — Depth: **Owns inclusive practice and equitable outcomes across a domain — addresses systemic barriers and builds diverse pipelines**; promotion and pay patterns are audited, not assumed. Scope: cross-team.
- **M4** — Depth: **Builds inclusion mechanisms — meeting norms, promotion audits, pay-equity checks — that a sub-org adopts and reports on.** Scope: a sub-org.
- **M5** — Depth: **Sets inclusion strategy and accountability for a function**, intervening on systemic patterns rather than the loudest case. Scope: a function.
- **M6** — Depth: **Champions an inclusive culture org-wide — the org's belonging outcomes are measured, published, and owned at the top.** Scope: org-wide.

### Technical Stewardship

#### Technical Judgment & Direction

##### Technical Credibility

*Anchor:* Majors, "The Engineer/Manager Pendulum" (2017) — managers must retain enough depth to earn trust and judge work; corroborated by Fournier, The Manager's Path (2017). *Why:* a leader who cannot evaluate technical work loses the team's trust and cannot coach staff engineers; credibility is retained, not assumed.
*OCF:* [proposed](../../contrib/2026-07-technical-credibility.md) (LI-06 candidate) · targets: M1:[P3](../../data/proficiency_scale.md#p3) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P5](../../data/proficiency_scale.md#p5)

- **M1** — Depth: **Understands the team's systems well enough to review designs, probe trade-offs, and triage incidents** — earns technical respect without taking the keyboard. Scope: one team's systems.
- **M2** — Depth: **Maintains depth across a critical system's stack and hardest problems — a credible thought-partner to staff engineers**, pairing them with the business context they need to choose well. Scope: a critical system and its senior ICs.
- **M3** — Depth: **Retains broad technical credibility across a domain — credible on its hardest cross-team technical questions**, staying current enough to ask the question that changes a design. Scope: a domain.
- **M4** — Depth: **Sustains strategic technical credibility across a sub-org — credible with the principal engineers and architects who set the bar**, and backs their judgment publicly. Scope: a sub-org.
- **M5** — Depth: **Maintains the credibility to guide a function's technology direction — translates architectural risk into business terms without distortion.** Scope: a function.
- **M6** — Depth: **Sustains credibility across the org's technology landscape** — engineers trust their technical judgment because it survives contact with detail. Scope: org-wide.

##### Technical Strategy & Investment

*Anchor:* Larson, An Elegant Puzzle: Systems of Engineering Management (2019) — managing investment across product work, platform quality, and technical debt as flows, not events; Wardley Maps (2016) grounds build-buy-partner choices in a component's evolutionary stage. *Why:* the platform-versus-feature allocation is a strategy decision managers make whether or not they make it consciously.
*OCF:* [LI-03](../../data/capabilities.md#li-03) — Technical Influence & Direction · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Reserves and defends explicit capacity for technical investment each quarter** — names what debt costs in incidents and velocity, and challenges the build-first instinct with a written cost-of-ownership comparison before the team writes custom infrastructure. Scope: one team's technical budget.
- **M2** — Depth: **Writes the technical investment case for a critical system — sunset, rewrite, or double down — with costed options**; makes reversible technology choices fast and irreversible ones deliberately, with spikes and exit criteria. Scope: a critical system's trajectory.
- **M3** — Depth: **Aligns technical direction across a domain — shared platform bets, deprecation calendars, convergence of overlapping technology — through cases teams they do not run choose to fund**, positioning each choice on differentiation versus commodity. Scope: cross-team technical portfolio.
- **M4** — Depth: **Balances a sub-org's build-buy-adopt portfolio and sequences platform migrations across years**, running an investment review so choices compound instead of fragmenting; the sub-org's systems get simpler while shipping more. Scope: a sub-org's technical estate.
- **M5** — Depth: **Puts technical strategy on the executive agenda in business terms — capability unlocked, risk retired, cost curve bent — and wins multi-year funding for unglamorous foundations**, setting the function's build/buy/partner doctrine. Scope: a function.
- **M6** — Depth: **Makes the org's defining technical bets — the platform choices competitors respond to — and communicates them so thousands of local decisions align**; answers for their decade-scale consequences publicly. Scope: org-wide, externally visible.

##### Domain & Business Fluency

*Anchor:* Cagan, Inspired (2008) — durable product decisions come from teams that understand customers, economics, and constraints, not just requirements. *Why:* engineering decisions are only as good as their grasp of product, customer, economics, and regulatory context.
*OCF:* [PD-06](../../data/capabilities.md#pd-06) — Product Thinking · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Explains how the team's work serves customers and the business, and the key constraints it operates under — including regulated-industry constraints where they apply.** Scope: one team's product surface.
- **M2** — Depth: **Connects a critical system's work to business value and cost — makes cost- and compliance-aware trade-offs** stakeholders recognize as commercially literate. Scope: a critical system.
- **M3** — Depth: **Owns the business, customer, and regulatory case for a domain**, aligning its technical work to outcomes and constraints; product partners treat their reasoning as native. Scope: a domain.
- **M4** — Depth: **Aligns multiple teams' work to business and regulatory strategy through the leaders running them** — investment cases read in market terms first. Scope: a sub-org.
- **M5** — Depth: **Shapes how engineering serves company strategy — owns the function's business fluency**, and engineering choices trace to unit economics and customer outcomes. Scope: a function.
- **M6** — Depth: **Connects org-wide engineering to company and market strategy** — the org's technical direction reads as a business thesis. Scope: org-wide.

#### Architecture, Quality & Debt

##### Architecture & Decision Oversight

*Anchor:* Conway, "How Do Committees Invent?" (1968) — systems mirror the communication structures of the organizations that build them; Nygard's architecture decision records (2011) make consequential decisions inspectable. *Why:* leaders shape architecture through decision processes and team boundaries even when they never write the design doc.
*OCF:* [ARC-10](../../data/capabilities.md#arc-10) — Architectural trade-off analysis · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Runs design review as a real gate — asks the trade-off and failure-mode questions that change designs — while leaving the decision with the engineers who own it**; consequential decisions get recorded with alternatives considered. Scope: one team's designs.
- **M2** — Depth: **Spots architecture risk in a critical system before it ships — coupling, scale cliffs, single points of failure — and gets it addressed without designing it themselves**, naming the trade-offs the decision-makers must own. Scope: a critical system.
- **M3** — Depth: **Installs the decision mechanisms a domain designs by — decision records, RFC review, architecture forums — that teams they do not run use**; catches mismatches between team shape and target architecture early. Scope: cross-team technical governance.
- **M4** — Depth: **Pairs org design with architecture direction deliberately — reshaping team boundaries so the target system becomes the path of least resistance**; the sub-org's principal engineers set direction inside guardrails they negotiated together. Scope: a sub-org.
- **M5** — Depth: **Holds the line on function-wide architectural coherence — few platforms, deliberate exceptions with expiry dates — without becoming the bottleneck.** Scope: a function.
- **M6** — Depth: **Answers for the org's technical integrity to the board and customers — knows where the liabilities are buried and funds the excavations**, with a decision record showing the bets were reasoned, not fashionable. Scope: org-wide systems.

##### Engineering Standards & Quality

*Anchor:* Humble & Farley, Continuous Delivery (2010) — pipeline discipline and built-in quality; Accelerate corroborates that quality enables speed rather than trading against it. *Why:* quality is a property of the system of work, and managers own the system of work.
*OCF:* [SWE-02](../../data/capabilities.md#swe-02) — Code Quality & Maintainability · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Holds the quality bar in practice — tests, review discipline, definition of done — and does not waive it under deadline pressure without a written, expiring exception.** Scope: one team's standard.
- **M2** — Depth: **Raises the bar on a system where it has slipped — testability, deploy safety, review quality — while shipping continues, and measures the change** in escaped defects and change-fail rate. Scope: a critical codebase.
- **M3** — Depth: **Harmonizes standards across teams by making the best team's practice everyone's default — documented, tooled, adopted because it is easier**; exceptions exist and each is justified in writing. Scope: a domain's engineering practice.
- **M4** — Depth: **Builds the paved road — golden paths, shared tooling, quality gates in the pipeline — that makes a sub-org's standard the path of least resistance**, funded as a first-class budget line. Scope: a sub-org.
- **M5** — Depth: **Publishes the function's engineering bar and reports honestly against it to executives, including where it is not met**, winning the cost-of-quality trade explicitly rather than smuggling it into estimates. Scope: a function's reputation for quality.
- **M6** — Depth: **Makes engineering excellence part of the org's external identity** — visible in the reliability customers experience, postmortems worth publishing, and the talent it attracts. Scope: org-wide.

##### Technical Debt & Risk Stewardship

*Anchor:* Cunningham, "The WyCash Portfolio Management System" (OOPSLA 1992) — the technical-debt metaphor: shipping on unconsolidated understanding accrues interest paid in every future change. *Why:* debt is invisible in demos, so surfacing and pricing it is a leadership act.
*OCF:* [proposed](../../contrib/2026-07-technical-debt-stewardship.md) (EM-15 candidate) · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Keeps a visible debt register with the cost of carry noted and retires items on a cadence**, defending a steady paydown allocation in planning rather than begging quarter by quarter. Scope: one team's codebases.
- **M2** — Depth: **Distinguishes debt worth carrying from debt that will detonate and sequences remediation by risk**, pricing debt in incident and velocity terms stakeholders accept; lands a major consolidation without stopping the roadmap. Scope: a critical system.
- **M3** — Depth: **Makes debt legible across a domain — a shared taxonomy and reporting rhythm teams they do not run adopt — and aggregates cross-team risk**: the shared library nobody owns, the migration half-finished in three places, owned and funded. Scope: cross-team quality economics.
- **M4** — Depth: **Sets a sub-org's quality strategy — where to gold-plate, where to accept scrappy — and lands multi-quarter remediation programs against feature pressure**, with debt stated in business terms: incident cost, velocity drag, security exposure. Scope: a sub-org's risk portfolio.
- **M5** — Depth: **Carries the function's technical risk onto the executive risk register — top exposures known, sized, owned, and trending** — and prevents the quarterly raid on foundational capacity. Scope: a function.
- **M6** — Depth: **Sets the org's speed-versus-soundness dial explicitly — declares where the org will accept debt for velocity and where it never will — and holds it under growth pressure.** Scope: org-wide.

### Communication & Influence

#### Communication

##### Written & Verbal Communication

*Anchor:* Minto, The Pyramid Principle (1987) — lead with the answer, group the supporting arguments, order them logically. *Why:* leadership runs on documents and rooms, and unclear leaders create unclear organizations.
*OCF:* [CC-01](../../data/capabilities.md#cc-01) — Written & Verbal Communication · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Writes updates and decision docs that lead with the answer and fit on a page**; runs meetings that start with a purpose and end with owners and dates. Scope: one team's information flow.
- **M2** — Depth: **Makes complex technical situations legible to non-engineers without dumbing them down** — an incident narrative a customer team can use, a trade-off memo a product partner can decide on. Scope: a critical team's external interface.
- **M3** — Depth: **Writes the documents cross-team decisions get made from — framing memos, options papers — that people cite weeks later**; several teams execute against them without a clarifying meeting. Scope: domain-level discourse.
- **M4** — Depth: **Sets the writing norms — templates, pre-read culture, decision-doc formats — a sub-org adopts because their versions demonstrably work.** Scope: a sub-org's document culture.
- **M5** — Depth: **Delivers one message coherently across audiences — board slide, all-hands, engineering deep-dive — without the versions contradicting each other.** Scope: a function's narrative.
- **M6** — Depth: **Gives the org its language — the phrases and frames people use to explain the strategy to each other — and lands hard messages with clarity and humanity.** Scope: org-wide and external.

##### Executive & Upward Communication

*Anchor:* Duarte, HBR Guide to Persuasive Presentations (2012) — audience-first structure wins decisions; Minto's answer-first discipline applies doubly under executive time pressure. *Why:* decisions above a leader are made on how the case is communicated, not only on its merits.
*OCF:* [proposed](../../contrib/2026-07-executive-communication.md) (CC-06 candidate) · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P5](../../data/proficiency_scale.md#p5) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Reports upward with the headline and the ask first — never burying the slip in paragraph four**; no surprise reaches their leadership from someone else. Scope: their management chain and immediate stakeholders.
- **M2** — Depth: **Briefs senior leaders under fire — facts, impact, options, and a recommendation inside the first two minutes**; their one-pagers get forwarded unedited. Scope: executive-facing moments for a critical program.
- **M3** — Depth: **Builds the case for a cross-team investment and lands it with an executive audience — pre-wired with the skeptics, sized in business terms, honest about risk**; preps other managers for executive rooms. Scope: domain-level asks and narratives.
- **M4** — Depth: **Runs the operating reviews a sub-org communicates through — the packet, the rhythm, the follow-through — managing a portfolio of executive stakeholders with different agendas** and keeping commitments to all of them consistent. Scope: a sub-org's upward interface.
- **M5** — Depth: **Operates the executive room as a peer — advances a position, absorbs hostile questioning without defensiveness, and changes the room's decision more often than not.** Scope: a function's voice at the top table.
- **M6** — Depth: **Speaks for the org's technical reality to boards, investors, and press — candid about bad news, precise about trade-offs**; the org's credibility survives their appearances. Scope: org-wide and external.

#### Influence & Partnership

##### Stakeholder Management & Partnership

*Anchor:* Freeman, Strategic Management: A Stakeholder Approach (1984) — organizations succeed by systematically identifying and managing everyone with a stake in outcomes; Mitchell, Agle & Wood (1997) add differential engagement by power, legitimacy, and urgency. *Why:* engineering leaders sit in a web of product, design, sales, support, and operations whose trust is built deliberately or lost by default.
*OCF:* [PM-13](../../data/capabilities.md#pm-13) — Stakeholder & executive management · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Runs a genuine triad with product and design — shared goals, early involvement, no surprise commitments** — and closes the loop when things change. Scope: one team's partner set.
- **M2** — Depth: **Maps and works a critical program's stakeholders — who needs consultation versus information — and repairs a damaged partnership** by resetting expectations and rebuilding credibility with delivered commitments. Scope: a program's stakeholder web.
- **M3** — Depth: **Treats their peer group as their first team — argues hard in the room, backs the decision outside it — and builds durable cross-functional relationships**: sales, support, and operations bring them bad news early. Scope: a domain's partner ecosystem.
- **M4** — Depth: **Designs how a sub-org interfaces with the rest of the business — intake paths, escalation contracts, joint planning and shared metrics — so partnership survives personnel changes.** Scope: a sub-org's external seams.
- **M5** — Depth: **Forms function-to-function alliances with product, sales, finance, and legal — reciprocal, durable, tested in a crisis** — trading short-term losses for long-term trust deliberately. Scope: cross-functional executive web.
- **M6** — Depth: **Stewards the org's most consequential external relationships — key customers, strategic partners, board stakeholders — and models one-company leadership**, resolving function-versus-function conflicts by company interest even at cost to their own area. Scope: org-wide and external.

##### Influence Without Authority

*Anchor:* Cohen & Bradford, Influence Without Authority (1989) — influence works through exchange: identifying what others value and trading in those currencies; Cialdini (1984) grounds the persuasion mechanics. *Why:* from Director up, nearly everything a leader needs done is done by people who do not answer to them.
*OCF:* [proposed](../../contrib/2026-07-influence-without-authority.md) (LI-07 candidate) · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Wins cooperation from adjacent teams by trading in their currencies — timing help, review effort, shared credit — rather than escalating.** Scope: one team's dependencies.
- **M2** — Depth: **Secures priority from other teams for a critical program with no borrowed authority** — builds the case in the other team's terms and repays visibly. Scope: a program's dependency network.
- **M3** — Depth: **Moves a domain to a shared position with no mandate — assembles the coalition, converts the skeptic whose objection is best** — and the position holds after they stop pushing. Scope: cross-team direction.
- **M4** — Depth: **Shifts sub-org-level outcomes through people two seams away — standards groups, principal engineers, partner leaders — who advocate the position as their own.** Scope: a sub-org's ecosystem.
- **M5** — Depth: **Influences peer executives and their organizations — lands function-shaping decisions while holding a minority of the formal power in the room.** Scope: cross-functional.
- **M6** — Depth: **Shapes industry and market context in the org's favor — standards bodies, open source, talent narratives — so external forces push where the org wants to go.** Scope: beyond the org.

##### Conflict Resolution & Negotiation

*Anchor:* Fisher & Ury, Getting to Yes (1981) — negotiate on interests, not positions; separate the people from the problem; Lencioni (2002) adds that unmined conflict produces false harmony and drift. *Why:* healthy organizations fight about ideas in the open, and unresolved conflict is one of the most expensive latencies an org carries.
*OCF:* [CC-05](../../data/capabilities.md#cc-05) — Handling Disagreement · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Surfaces simmering disagreement early and mediates it to interests — names the tension, separates people from positions, drives to an agreement both sides can state fairly.** Scope: within one team and its nearest neighbors.
- **M2** — Depth: **Negotiates commitments under pressure — scope, deadlines, contested interfaces — reaching agreements both sides keep, with the trade documented**; reframes turf disputes as interface-design problems. Scope: a critical team's boundaries and stakes.
- **M3** — Depth: **Resolves lead-to-lead conflicts others route around as a trusted broker — finds the interest-based trade and teaches the parties to resolve the next one themselves**; people bring them conflicts they are not even party to. Scope: cross-team disputes in a domain.
- **M4** — Depth: **Redesigns the structures that generate recurring conflict — misaligned incentives, ambiguous ownership — instead of re-mediating the same fight**, and designs escalation paths so conflicts resolve at the lowest capable level. Scope: a sub-org's conflict system.
- **M5** — Depth: **Negotiates function-level conflicts — budget splits, shared-platform terms, charter boundaries — with peer executives and external parties, keeping the relationships intact afterward.** Scope: a function's seams.
- **M6** — Depth: **Turns the org's biggest ideological fights — build versus buy, centralize versus embed — into decision processes the losing side calls fair.** Scope: org-wide.

### Self & Personal Effectiveness

#### Leverage & Delegation

##### Managerial Leverage & Focus

*Anchor:* Grove, High Output Management (1983) — a manager's output is the output of their organization plus the organizations they influence; Drucker, The Effective Executive (1967) — know where the time goes, concentrate on the vital few, abandon the rest. *Why:* time is the one non-renewable managerial input, and leverage is the discipline of spending it where it multiplies.
*OCF:* [proposed](../../contrib/2026-07-managerial-leverage-focus.md) (EM-16 candidate) · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Runs a deliberate calendar that matches stated priorities — one-on-ones, deep work, and team time protected; low-leverage meetings declined with alternatives** — and ends each week with the highest-leverage actions done. Scope: their own week and one team's operating rhythm.
- **M2** — Depth: **Prunes their own involvement ruthlessly as complexity grows — automates, delegates, or kills recurring work every quarter** — and models a sustainable pace through crunch; peers copy the operating cadence. Scope: a complex team's demands on one person.
- **M3** — Depth: **Chooses interventions by multiplier across a domain — the review that shapes ten decisions, the doc that aligns three roadmaps — and declines the rest by policy, not mood**; audits their own time quarterly and publishes the changes. Scope: cross-team attention allocation.
- **M4** — Depth: **Designs their own role top-down from the sub-org's constraints — spends time only where they are the unique unlock — and declines demands that do not map to strategy, visibly and with reasons.** Scope: a sub-org's scarcest resource, senior attention.
- **M5** — Depth: **Allocates attention at function scale like a portfolio — deep on two things, delegated on twenty — and says which is which out loud.** Scope: a function.
- **M6** — Depth: **Spends presence deliberately as an org-wide signal — where they show up moves priorities — and guards the org's focus**: limits concurrent top priorities and abandons stale initiatives by name. Scope: org-wide.

##### Delegation & Empowerment

*Anchor:* Marquet, Turn the Ship Around! (2012) — intent-based leadership: move authority to where the information lives and lead with intent, not instructions. *Why:* under- and over-delegation are the two default manager failure modes, and calibrating per person per task is the skill.
*OCF:* [proposed](../../contrib/2026-07-delegation-empowerment.md) (EM-14 candidate) · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Delegates whole outcomes with context and check-in contracts matched to each person's readiness — not tasks with instructions** — and resists snatching work back when it wobbles. Scope: work within one team.
- **M2** — Depth: **Hands ownership of a critical, visible workstream to someone not yet proven and scaffolds them to success — letting them keep the credit publicly**; the team runs a week without them and nothing stalls. Scope: a complex team's critical path.
- **M3** — Depth: **Pushes decisions down across a domain — publishes decision rights so teams stop escalating what they can decide themselves**; their involvement is exception-based, and everyone knows which is which. Scope: cross-team decision flow.
- **M4** — Depth: **Builds a sub-org that runs on mechanisms rather than their presence — delegated authorities with audit trails, pre-declared tripwires for taking back control.** Scope: a sub-org that does not queue on them.
- **M5** — Depth: **Grants senior leaders genuinely consequential authority and holds them to outcomes, not methods**; the function's decisions get faster as it grows, not slower. Scope: a function.
- **M6** — Depth: **Runs the org on intent — direction and guardrails clear enough that leaders act correctly without asking — and treats every upward escalation as a design flaw to fix.** Scope: org-wide autonomy architecture.

#### Growth & Resilience

##### Self-Awareness & Learning Agility

*Anchor:* Eurich, Insight (2017) — self-awareness is rare, correlates with leadership effectiveness, and is trainable through external feedback; Lombardo & Eichinger (2000) — learning agility predicts leadership potential better than raw performance. *Why:* every level change hands a leader a job they have never done, and blind spots scale with scope.
*OCF:* [proposed](../../contrib/2026-07-self-awareness-learning-agility.md) (LI-09 candidate) · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Asks for feedback on their own management and changes visibly in response — "you said X, I changed Y"** — and approaches first-time situations as learnable, keeping a running list of their own failure patterns. Scope: their own practice, witnessed by one team.
- **M2** — Depth: **Knows their failure modes under pressure and manages them in the moment — staffs deliberately against known weaknesses**, seeking disconfirming input on their hardest calls before deciding. Scope: a critical team's exposure to their blind spots.
- **M3** — Depth: **Runs structured input on themselves — 360s, skip-level themes — and closes the loop publicly on what they heard and changed**; retools openly for first-time challenges so others copy the learning method. Scope: signal gathered across a domain.
- **M4** — Depth: **Compensates deliberately for the seniority feedback vacuum — cultivates truth-tellers and rewards the bearer of unwelcome news about themselves**; retires their own outdated playbook when the sub-org outgrows it. Scope: a sub-org's honest mirror.
- **M5** — Depth: **Reinvents their leadership at function scale — lets go of the operator identity, learns governance and capital skills mid-flight — and says "I don't know" in rooms where pretending is the norm.** Scope: a function watches and learns from it.
- **M6** — Depth: **Institutionalizes challenge to their own judgment — red teams, protected dissent — and studies how their moods and offhand comments get amplified**, regulating accordingly. Scope: an org-wide shadow, managed consciously.

##### Resilience & Sustainable Pace

*Anchor:* Loehr & Schwartz, The Power of Full Engagement (2003) — manage energy, not just time; leadership is an endurance discipline. *Why:* a depleted or brittle leader makes worse decisions and models an unsustainable culture.
*OCF:* [proposed](../../contrib/2026-07-resilience-sustainable-pace.md) (LI-10 candidate) · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Stays effective and steady under pressure — recovers from setbacks, manages their own energy, and models a sustainable pace** the team learns from watching, not from posters. Scope: one team's pace-setting example.
- **M2** — Depth: **Holds up through prolonged pressure — incident sieges, crunch, org turbulence — and helps the team stay resilient**, refusing burnout-driven decisions and naming them when they appear. Scope: a critical team under sustained load.
- **M3** — Depth: **Builds resilience into how teams operate across a domain — on-call health, recovery time after pushes, load balancing between teams** — and repairs burnout risk at scale. Scope: cross-team operating norms.
- **M4** — Depth: **Models and protects sustainable pace across a sub-org, including through the leaders they develop**; pace and recovery are designed into the operating rhythm, not left to heroics. Scope: a sub-org.
- **M5** — Depth: **Stewards organizational resilience at function scale — capacity buffers, crisis rotation, energy management for senior leaders** — and holds the line when business pressure argues for permanent crunch. Scope: a function.
- **M6** — Depth: **Shapes a resilient, sustainable culture org-wide** — the org absorbs shocks without breaking people, and the story of its hardest year is told without casualties as the moral. Scope: org-wide.

#### Judgment & Integrity

##### Decision-Making Under Uncertainty

*Anchor:* Kahneman, Thinking, Fast and Slow (2011) — judgment is systematically biased, and decision quality improves through process, not willpower; the reversible/irreversible framing sets the right speed for each door. *Why:* leaders decide with less information at each level, and unexamined bias scales with the blast radius.
*OCF:* [LI-04](../../data/capabilities.md#li-04) — Decision-Making under Uncertainty · targets: M1:[P2](../../data/proficiency_scale.md#p2) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Sizes the decision process to reversibility — quick calls on two-way doors, written option analysis on one-way doors** — states assumptions and confidence levels, and sets a revisit date. Scope: one team's decisions, made at the pace the team needs.
- **M2** — Depth: **Structures high-stakes calls on incomplete data — options written, disconfirming evidence sought, dissent solicited before their own view is stated** — names tripwires that trigger revisits and kills their own sunk-cost projects. Scope: a critical team's one-way doors.
- **M3** — Depth: **Installs debiasing mechanics across a domain — pre-mortems, red teams, decision journals reviewed against outcomes — and clarifies who decides what** so cross-team decisions stop stalling in consensus. Scope: cross-team decision quality.
- **M4** — Depth: **Calibrates a sub-org's risk appetite decision by decision — pushes gamble-shy teams to bet and bet-happy teams to check — using a scored decision record**, and separates decision quality from outcome luck in reviews. Scope: a sub-org's judgment culture.
- **M5** — Depth: **Makes function-level bets under genuine ambiguity — market shifts, platform discontinuities — sized so being wrong is survivable**, showing the reasoning so the function learns even when the bet loses. Scope: a function.
- **M6** — Depth: **Carries the org's irreversible decisions — the ones with no consensus and no precedent — with a process others trust even when they disagree with the call**, and reserves only the genuine one-way doors. Scope: org-wide consequence.

##### Ethics, Integrity & Trust

*Anchor:* Mayer, Davis & Schoorman, "An Integrative Model of Organizational Trust" (1995) — trust is granted on perceived ability, benevolence, and integrity; the ACM Code of Ethics (2018) holds leaders accountable for the norms their organizations adopt. *Why:* a leader's word is the currency every other competency spends, and courage under pressure is what keeps everything else honest.
*OCF:* [proposed](../../contrib/2026-07-integrity-trust.md) (LI-11 candidate) · targets: M1:[P3](../../data/proficiency_scale.md#p3) M2:[P3](../../data/proficiency_scale.md#p3) M3:[P4](../../data/proficiency_scale.md#p4) M4:[P4](../../data/proficiency_scale.md#p4) M5:[P5](../../data/proficiency_scale.md#p5) M6:[P6](../../data/proficiency_scale.md#p6)

- **M1** — Depth: **Keeps commitments or renegotiates them before the deadline, never after — says the same thing in the room and out of it**, owns mistakes unprompted, and tells stakeholders the true state of the project when the truth is unwelcome. Scope: one team's trust in its manager.
- **M2** — Depth: **Holds the quality or safety line on a critical system under senior pressure — makes the unpopular-but-right call and absorbs the cost personally**, protecting the engineer who raised the flag; handles sensitive information impeccably. Scope: a critical system's integrity.
- **M3** — Depth: **Serves as the honest broker across a domain — parties in a dispute accept their account of the facts** — and carries uncomfortable systemic truths to the room where they can be fixed. Scope: cross-team credibility and ethical tone.
- **M4** — Depth: **Builds the mechanisms that make integrity cheap in a sub-org — ethics review in design, safe escalation with follow-through, fairness systems whose losers affirm the process — and applies them to their own decisions first.** Scope: a sub-org's institutional fairness.
- **M5** — Depth: **Stops function-level launches on ethical or safety grounds and defends the call upward with the business case for trust**; corrects the record when convenient narratives are wrong. Scope: a function's public impact.
- **M6** — Depth: **Holds the org's line with the board, investors, and market when the profitable path and the right path diverge — walks away from revenue, ships the hard disclosure** — and how they handle the worst moments becomes the story the culture tells about itself. Scope: org-wide conscience, for years.

## Sources

- ACM Code of Ethics and Professional Conduct (2018)
- Beyer, Jones, Petoff & Murphy (eds.), Site Reliability Engineering: How Google Runs Production Systems (2016)
- Brooks, The Mythical Man-Month (1975)
- Bungay, The Art of Action (2011)
- Cagan, Inspired: How to Create Products Customers Love (2008)
- Charan, Drotter & Noel, The Leadership Pipeline (2001)
- Cialdini, Influence: The Psychology of Persuasion (1984)
- CircleCI Engineering Competency Matrix (CC BY 4.0) — prose-register reference
- Cohen & Bradford, Influence Without Authority (1989)
- Collins & Porras, "Building Your Company's Vision" (Harvard Business Review, 1996)
- Conway, "How Do Committees Invent?" (Datamation, 1968)
- Cunningham, "The WyCash Portfolio Management System" (OOPSLA, 1992)
- Deci & Ryan, "Self-Determination Theory and the Facilitation of Intrinsic Motivation, Social Development, and Well-Being" (American Psychologist, 2000)
- Deming, Out of the Crisis (1986)
- Drucker, The Effective Executive (1967)
- Duarte, HBR Guide to Persuasive Presentations (2012)
- Edmondson, The Fearless Organization (2018)
- Ely & Thomas, "Cultural Diversity at Work" (Administrative Science Quarterly, 2001)
- Eurich, Insight (2017)
- Fisher & Ury, Getting to Yes (1981)
- Forsgren, Humble & Kim, Accelerate: The Science of Lean Software and DevOps (2018)
- Forsgren et al., "The SPACE of Developer Productivity" (ACM Queue, 2021)
- Fournier, The Manager's Path (2017)
- Freeman, Strategic Management: A Stakeholder Approach (1984)
- Goldratt, The Goal (1984)
- Google re:Work, Project Aristotle team-effectiveness study (2015) — corroborates the Psychological Safety anchor
- Google re:Work, Project Oxygen manager-behaviors study (2008) — corroborates the Coaching & Development anchor
- Grove, High Output Management (1983)
- Heifetz, Leadership Without Easy Answers (1994)
- Hersey & Blanchard, Management of Organizational Behavior (1969)
- Herzberg, "One More Time: How Do You Motivate Employees?" (Harvard Business Review, 1968)
- Hewlett, Forget a Mentor, Find a Sponsor (2013)
- Humble & Farley, Continuous Delivery (2010)
- Kahneman, Thinking, Fast and Slow (2011)
- Korn Ferry Leadership Architect competency library (2014) — comparison overlay only
- Kotter, Leading Change (1996); "What Leaders Really Do" (Harvard Business Review, 1990)
- Larson, An Elegant Puzzle: Systems of Engineering Management (2019)
- Lencioni, The Five Dysfunctions of a Team (2002)
- Locke & Latham, "Building a Practically Useful Theory of Goal Setting and Task Motivation" (American Psychologist, 2002)
- Loehr & Schwartz, The Power of Full Engagement (2003)
- Lombardo & Eichinger, "High Potentials as High Learners" (Human Resource Management, 2000)
- Majors, "The Engineer/Manager Pendulum" (2017)
- Marquet, Turn the Ship Around! (2012)
- Mayer, Davis & Schoorman, "An Integrative Model of Organizational Trust" (Academy of Management Review, 1995)
- McConnell, Software Estimation: Demystifying the Black Art (2006)
- Minto, The Pyramid Principle (1987)
- Mitchell, Agle & Wood, "Toward a Theory of Stakeholder Identification and Salience" (Academy of Management Review, 1997)
- NIST Cybersecurity Framework (2014)
- Nygard, "Documenting Architecture Decisions" (2011)
- Project Management Institute, PMBOK Guide (7th edition, 2021)
- Reinertsen, The Principles of Product Development Flow (2009)
- Rumelt, Good Strategy Bad Strategy (2011)
- Schmidt & Hunter, "The Validity and Utility of Selection Methods in Personnel Psychology" (Psychological Bulletin, 1998)
- Scott, Radical Candor (2017)
- Skelton & Pais, Team Topologies (2019)
- Tuckman, "Developmental Sequence in Small Groups" (Psychological Bulletin, 1965)
- Wardley, Wardley Maps (2016)
- Whitmore, Coaching for Performance (1992)
