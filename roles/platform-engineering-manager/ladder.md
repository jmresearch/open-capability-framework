# Platform Engineering Management — Career Ladder (M1–M6)

*Manager variant · levels M1–M6 · rendered from the canonical role record (`role.yaml`): 7 key areas, 16 focus areas, 44 competencies.*

## Calibration

This is the **people-leadership track** for internal developer-platform, DevEx, and infrastructure teams. It carries the full engineering-management load — hiring, coaching, performance, delivery, org design, strategy, communication — **and** the platform-specific accountabilities that a generic Engineering Management ladder does not name: platform-as-a-product thinking, developer experience and adoption, paved-road strategy, reliability and operational leverage, self-service infrastructure, and FinOps. Where the generic EM ladder would say "runs a team," this one asks whether the team's *platform* is adopted, reliable, self-service, and cost-aware — the platform character is load-bearing, not relabeled management prose.

**The Self & Personal Effectiveness area is shared, not platform-specific.** Its six competencies — managerial leverage, delegation, self-awareness, resilience, decision-making under uncertainty, and ethics — are borrowed verbatim from the **Engineering Management canon**, sharing capability ids, anchors, and per-level curves. This territory is not platform-contingent; a canon adapted verbatim must not lack judgment, delegation, resilience, or an ethics row on the manager axis, so a platform manager is held to the same self-effectiveness bar as any engineering manager.

**Two dimensions, read separately.** Each cell states **Depth** (what the person can demonstrate, and how deeply) and **Scope** (how wide the blast radius is). They move on different axes: *competency is what a person can demonstrate before the title; scope is what the organization grants when a seat opens.* A strong candidate can show deep competency at narrow scope well before the wider seat exists — that is exactly what makes them ready for it.

**Upper levels are written to stay demonstrable.** M3–M6 are phrased as **indirect-leverage behaviors** a person can show now — outcomes reached through leaders they develop and influence, mechanisms and standards other teams adopt, and decisions shaped across teams they do not manage — rather than position-locked "owns it because they hold the seat" language. **Honest in-seat caveat:** some accountability at the top of this ladder — budget of record, formal headcount authority, board exposure — is only *fully* exercised once the seat is held. The cells show readiness through proxy demonstrations; they do not claim the person already holds structure they have not been granted.

**Proficiency targets** ride the manager curve (P1 novice → P6 pioneer/sets-direction), calibrated per competency against the Engineering Management and Platform Engineering canonical records; every shared capability id carries the same M1–M6 curve as the Engineering Management record. Every cell's bar is set to that competency's target at that level; the per-competency **OCF** table carries the M1–M6 targets so a rater can check the calibration. One competency, **Adoption & migration strategy**, maps to **OPS-33** (Platform adoption & deprecation management), a capability accepted into the catalog with this record because no prior capability covered internal-platform adoption, migration, and deprecation.

## Level overview

| Level | Title | Scope band | Focus |
|-------|-------|------------|-------|
| M1 | Platform Engineering Manager | S1 · one platform team | builds one healthy platform team and the platform-as-a-product fundamentals |
| M2 | Senior Platform Engineering Manager | S2 · a complex / critical platform team | runs a high-stakes platform team and its reliability and DevEx outcomes |
| M3 | Director of Platform Engineering | S3 · a platform domain (cross-team) | sets strategy and paved-road standards for a cross-team platform domain |
| M4 | Senior Director of Platform Engineering | S4 · a platform sub-org | builds the operating system and architecture a platform sub-org runs on |
| M5 | VP of Platform Engineering | S5 · the platform function | sets platform-function direction and represents developer productivity to the business |
| M6 | SVP / Head of Platform | S6 · org-wide platform | sets org-wide platform vision, operating model, and the company-level infrastructure bets |

## Competency matrix

Grouped **key area → focus area → competency**, in canonical order. Each competency shows its anchor, its OCF capability id, its per-level proficiency targets, and the six M1–M6 cells. The **bold clause** in each cell is its most distinctive observable — read a level's bold clauses down the column as an evidence ladder.

### People Leadership & Team Health

#### Hiring & Team Formation

##### Hiring & selection

*Anchor:* Schmidt & Hunter, selection-methods meta-analysis (1998) — structured, work-sample selection predicts platform performance far better than gut feel.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [LI-02](../../data/capabilities.md#li-02) — Hiring & Staffing | [P3](../../data/proficiency_scale.md#p3) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Runs structured platform-role interview loops against a pre-agreed rubric and work-sample exercise. **Defends every hire/no-hire in debrief with recorded signal evidence rather than gut feel.** Scope: fills open roles on one platform team.
- **M2** — Depth: Designs the loop and rubric for hard-to-fill platform and SRE roles and calibrates interviewers. **Rebuilds a loop that is letting weak candidates through by tightening the signals it actually tests.** Scope: staffs a critical platform team, senior and specialist hires included.
- **M3** — Depth: Sets the hiring bar and interview-design pattern that other platform hiring managers pick up. **Publishes the rubric and calibration cadence several teams' loops now run on.** Scope: hiring quality across a cross-team platform domain.
- **M4** — Depth: Builds the selection system a platform sub-org hires through. **Certifies interviewers and installs a bar-raiser mechanism that measurably lifts quality-of-hire.** Scope: the hiring pipeline for a platform sub-org.
- **M5** — Depth: Drives the function's talent strategy, weighing grow-vs-buy for scarce reliability and DevEx skills. **Shapes leveling and headcount decisions across the function from pipeline and labor-market data.** Scope: the platform function's talent supply.
- **M6** — Depth: Sets the org-wide philosophy for hiring platform and infrastructure talent that peer functions benchmark against. **Pioneers selection practice, like work-sample design for platform work, that other organizations copy.** Scope: company-wide platform talent bar and brand.

##### Onboarding & team formation

*Anchor:* Tuckman, Developmental Sequence in Small Groups (1965) — teams cross forming-storming-norming-performing, and the manager's job is to shorten that arc.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [EM-13](../../data/capabilities.md#em-13) — Onboarding & team formation | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Runs a structured onboarding with a buddy, a ramp checklist, and a first paved-road change in week one. **Gets a new platform hire shipping a real change within their first sprint.** Scope: onboarding into one platform team.
- **M2** — Depth: Designs onboarding for a high-stakes team where on-call and blast radius are real, sequencing access, shadowing, and first incident exposure. **Reads where a forming team is stuck in storming and intervenes to move it to performing.** Scope: team formation on a critical platform team.
- **M3** — Depth: Sets the onboarding and team-formation standard other platform leads adopt. **Ships a reusable ramp template and 30/60/90 model that cuts time-to-first-contribution across the domain.** Scope: onboarding quality across a cross-team platform domain.
- **M4** — Depth: Builds the operating rhythm that forms and re-forms teams cleanly through platform re-splits across a sub-org. **Stands up a new platform team from scratch to productive without a delivery trough.** Scope: team formation across a platform sub-org.
- **M5** — Depth: Drives how the function grows, splits, and merges teams as demand shifts while keeping Team-Topologies boundaries clean. **Sets the norms that keep newly formed platform teams productive through function-wide scaling.** Scope: team formation across the platform function.
- **M6** — Depth: Sets the org-wide model for how platform capability is stood up and dissolved as bets change. **Pioneers the team-formation playbook other engineering functions reuse.** Scope: org-wide platform team topology.

#### Coaching & Performance

##### Coaching & development

*Anchor:* Whitmore, Coaching for Performance (1992); Google Project Oxygen — regular coaching, not status-checking, is the top driver of manager effectiveness.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [LI-01](../../data/capabilities.md#li-01) — Mentorship & Coaching | [P3](../../data/proficiency_scale.md#p3) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Holds regular 1:1s that coach rather than status-check, favoring questions over answers. **Turns a specific platform-engineer weakness into a visible skill gain within a quarter.** Scope: coaches the engineers on one platform team.
- **M2** — Depth: Coaches senior engineers and tech leads through ambiguous, high-judgment work such as reliability trade-offs and on-call leadership. **Develops a report into a tech lead who now runs a workstream unaided.** Scope: develops the talent bench of a critical platform team.
- **M3** — Depth: Grows other people-leaders' coaching skill, not just individuals'. **Runs coaching-the-coach sessions that lift how platform leads across the domain develop their own people.** Scope: coaching capability across a cross-team platform domain.
- **M4** — Depth: Builds the leadership-development pipeline a platform sub-org relies on, growing future platform leaders before seats open. **Produces leaders others actively recruit onto their teams.** Scope: the leadership bench of a platform sub-org.
- **M5** — Depth: Drives the function's approach to growing engineering and management talent, tied to the reliability and DevEx skills it will need. **Sets development standards leaders across the function coach against.** Scope: talent development across the platform function.
- **M6** — Depth: Sets the org-wide expectation for how platform leaders are grown. **Pioneers a development model peer functions adopt.** Scope: company-wide platform leadership development.

##### Career development & sponsorship

*Anchor:* Hewlett, Forget a Mentor, Find a Sponsor (2013) — advancement comes from spending capital on people, not just mentoring them.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [EM-02](../../data/capabilities.md#em-02) — Career development & sponsorship | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Holds career conversations and writes growth plans tied to the ladder. **Puts a report's name forward for a visible platform project that stretches them.** Scope: career growth for one platform team.
- **M2** — Depth: Sponsors senior engineers into stretch scope and promotion, building the evidence case ahead of calibration. **Gets a deserving platform engineer promoted through a defensible packet.** Scope: advancement on a critical platform team.
- **M3** — Depth: Sets sponsorship norms other platform leads adopt. **Advocates for talent in cross-team calibration rooms they do not own, moving outcomes for people who are not theirs.** Scope: advancement across a cross-team platform domain.
- **M4** — Depth: Builds the succession and sponsorship system for a platform sub-org so key roles have ready successors. **Spends visible capital to place emerging platform leaders into scope.** Scope: succession across a platform sub-org.
- **M5** — Depth: Drives the function's approach to advancing and retaining top talent, including the scarce staff-plus platform-architect and reliability track. **Sets the sponsorship expectations leaders across the function are held to.** Scope: advancement across the platform function.
- **M6** — Depth: Sets the org-wide standard for how platform careers ladder. **Pioneers a sponsorship model that measurably widens the platform leadership pipeline.** Scope: company-wide platform career paths.

##### Performance management

*Anchor:* Grove, High Output Management (1983) — a manager's output is the team's output, so managing performance is the core lever.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [EM-01](../../data/capabilities.md#em-01) — Performance management & accountability | [P3](../../data/proficiency_scale.md#p3) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Sets clear expectations and gives specific, timely feedback. **Addresses an underperforming platform engineer directly with a documented plan rather than letting it drift.** Scope: performance on one platform team.
- **M2** — Depth: Manages the full performance range on a high-stakes team, rewarding top reliability contributors and fairly turning around or exiting persistent underperformance. **Runs a difficult exit cleanly and defensibly.** Scope: performance on a critical platform team.
- **M3** — Depth: Sets the performance and calibration standard other platform leads apply consistently. **Runs cross-team calibration that holds a fair, comparable bar across the domain.** Scope: performance consistency across a cross-team platform domain.
- **M4** — Depth: Builds the performance system a platform sub-org runs on, from level expectations to calibration mechanics. **Corrects rating drift between teams so the bar means the same everywhere.** Scope: performance management across a platform sub-org.
- **M5** — Depth: Drives the function's performance philosophy and its link to reliability and delivery outcomes. **Sets the standard leaders across the function calibrate to.** Scope: performance across the platform function.
- **M6** — Depth: Sets the org-wide performance expectations for platform leadership. **Pioneers a performance model peer functions adopt.** Scope: company-wide platform performance standard.

#### Team Health & Culture

##### Psychological safety & team health

*Anchor:* Edmondson, The Fearless Organization (2018); Project Aristotle — safety is the top predictor of team performance and the precondition for blameless ops.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [EM-03](../../data/capabilities.md#em-03) — Psychological safety & team health | [P3](../../data/proficiency_scale.md#p3) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Runs blameless retros and incident reviews and invites dissent. **Models admitting their own mistakes so engineers surface problems early instead of hiding them.** Scope: team health on one platform team.
- **M2** — Depth: Sustains safety on a high-pressure on-call team where incidents are public and stressful. **Keeps a severe-outage review blameless so the real contributing causes come out.** Scope: team health on a critical platform team.
- **M3** — Depth: Sets the team-health and blameless-culture standard other platform leads adopt. **Instruments team-health signals across the domain and acts on a declining one before it becomes attrition.** Scope: team health across a cross-team platform domain.
- **M4** — Depth: Builds the culture mechanisms a platform sub-org relies on, from survey cadence to blameless-review norms and safety expectations for leaders. **Turns around an unhealthy team's culture through the leader running it.** Scope: culture across a platform sub-org.
- **M5** — Depth: Drives the function's culture, tying psychological safety explicitly to reliability outcomes. **Sets the health norms leaders across the function are measured against.** Scope: culture across the platform function.
- **M6** — Depth: Sets the org-wide expectation that platform operates blamelessly and safely. **Pioneers a culture model other engineering functions copy.** Scope: company-wide platform culture.

##### Motivation, engagement & retention

*Anchor:* Deci & Ryan, Self-Determination Theory (2000); Herzberg (1968) — autonomy, mastery, and purpose drive durable engagement more than extrinsic rewards.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [EM-17](../../data/capabilities.md#em-17) — Motivation & engagement | [P3](../../data/proficiency_scale.md#p3) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Reads what motivates each engineer and connects platform work to purpose. **Spots a disengaging report early and re-engages them before they start looking.** Scope: engagement on one platform team.
- **M2** — Depth: Sustains engagement on a team doing high-toil, sometimes thankless reliability work by framing impact and rotating growth. **Keeps regrettable attrition low on a critical platform team through a demanding period.** Scope: retention on a critical platform team.
- **M3** — Depth: Sets engagement and retention practices other platform leads adopt. **Reads engagement signals across the domain and fixes a systemic driver of attrition, not just symptoms.** Scope: engagement across a cross-team platform domain.
- **M4** — Depth: Builds the retention strategy a platform sub-org runs on, targeting the drivers specific to platform work such as toil, on-call load, and low visibility. **Shifts a sub-org's engagement trend through the leaders who own each team.** Scope: retention across a platform sub-org.
- **M5** — Depth: Drives the function's engagement and retention strategy, protecting scarce reliability and DevEx talent. **Sets the expectations leaders across the function own for engagement.** Scope: retention across the platform function.
- **M6** — Depth: Sets the org-wide narrative that makes platform a destination rather than a cost center. **Pioneers retention practice for infrastructure talent that peers adopt.** Scope: company-wide platform engagement.

### Platform as a Product

#### Product Strategy & Discovery

##### Platform vision & roadmap

*Anchor:* Perri, Escaping the Build Trap (2018); Skelton & Pais, Team Topologies (2019) — a platform is run as a product with outcomes and sized as a thinnest-viable-platform, not a feature factory.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [PM-05](../../data/capabilities.md#pm-05) — Roadmap & portfolio planning | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Maintains a platform roadmap tied to developer outcomes, not just a feature list. **States the problem each platform capability solves and for whom.** Scope: the roadmap for one platform team's surface.
- **M2** — Depth: Owns the vision and roadmap for a critical platform area, sequencing by developer value and thinnest-viable-platform thinking. **Kills or defers a low-value platform build others wanted, with the outcome argument to back it.** Scope: roadmap for a high-stakes platform team.
- **M3** — Depth: Sets a cross-team platform vision that other teams' roadmaps align to. **Publishes a domain platform strategy that redirects several teams' build priorities.** Scope: platform direction across a cross-team domain.
- **M4** — Depth: Builds the multi-year platform roadmap a sub-org executes against, balancing capability bets, migrations, and retirement. **Frames the platform-as-a-product operating model the sub-org plans within.** Scope: platform strategy for a sub-org.
- **M5** — Depth: Drives the function's vision and its link to business outcomes and developer productivity. **Sets the platform bets the function organizes around and defends them at the exec table.** Scope: vision for the platform function.
- **M6** — Depth: Sets the org-wide platform vision and the make-vs-consume posture for the whole company. **Pioneers a platform strategy the industry recognizes.** Scope: org-wide platform direction.

##### Internal user research & discovery

*Anchor:* Noda, Storey, Forsgren & Greiler, DevEx: What Actually Drives Productivity (ACM Queue, 2023) — platform value is set by developers' lived experience, which must be measured not assumed.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [PM-01](../../data/capabilities.md#pm-01) — Product discovery & customer research | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Talks to platform users regularly and watches them use the tools. **Turns an observed developer pain point into a prioritized platform fix.** Scope: discovery for one platform team's users.
- **M2** — Depth: Runs structured DevEx discovery for a critical platform area through interviews, journey mapping, and friction logs. **Quantifies a cognitive-load or feedback-loop problem the team then designs against.** Scope: discovery for a high-stakes platform team's users.
- **M3** — Depth: Sets the DevEx-research practice other platform teams adopt. **Stands up a developer-experience measurement combining surveys and system signals that several teams now steer by.** Scope: DevEx discovery across a cross-team domain.
- **M4** — Depth: Builds the continuous developer-listening system a platform sub-org runs on, linking perceptual and system metrics. **Makes DevEx evidence the default input to roadmap decisions across the sub-org.** Scope: developer research across a platform sub-org.
- **M5** — Depth: Drives how the function understands and represents developer productivity to the business. **Sets the DevEx metrics the function commits to and reports upward.** Scope: developer insight across the platform function.
- **M6** — Depth: Sets the org-wide definition of developer experience and how it is measured. **Pioneers a DevEx research program other companies reference.** Scope: org-wide developer-experience insight.

##### Platform value & business case

*Anchor:* Cagan, Inspired (2008) — platform investment is justified in value delivered, not output shipped.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [PD-06](../../data/capabilities.md#pd-06) — Product Thinking | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Articulates the value of the team's platform work in developer-time and reliability terms. **Ties a platform initiative to a concrete productivity or cost outcome.** Scope: value case for one platform team.
- **M2** — Depth: Builds the business case for a significant platform investment, quantifying time saved, incidents avoided, or spend reduced. **Wins funding for a platform bet with a defensible value model.** Scope: value case for a critical platform team's investments.
- **M3** — Depth: Sets the value-articulation standard other platform leads use. **Publishes a value and ROI framework several teams justify platform work with.** Scope: platform value cases across a cross-team domain.
- **M4** — Depth: Builds the investment model a platform sub-org allocates by, ranking bets on value and leverage. **Reframes platform from cost center to leverage multiplier for the sub-org's stakeholders.** Scope: investment cases across a platform sub-org.
- **M5** — Depth: Drives how the function proves and communicates its business value. **Sets the value narrative and metrics the function is funded against.** Scope: value case for the platform function.
- **M6** — Depth: Sets the org-wide economic case for platform investment. **Pioneers a platform-value model the business plans capital around.** Scope: org-wide platform economics.

#### Developer Experience & Adoption

##### Golden paths & paved roads

*Anchor:* Spotify Engineering, How We Use Golden Paths (2020) — an opinionated, supported path makes the right way the easy way.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [OPS-27](../../data/capabilities.md#ops-27) — Platform & developer-experience engineering | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Maintains a golden path for a common workflow that is templated, documented, and supported. **Gets the team's users onto the paved road for one high-frequency task.** Scope: golden paths on one platform team's surface.
- **M2** — Depth: Designs paved roads for a critical platform area, balancing opinion with escape hatches. **Retires a fragmented set of bespoke setups onto a single supported golden path.** Scope: paved roads for a high-stakes platform team.
- **M3** — Depth: Sets the golden-path design standard other platform teams adopt. **Defines what paved means across the domain, from support SLA to versioning and deprecation, and gets teams to build to it.** Scope: paved-road strategy across a cross-team domain.
- **M4** — Depth: Builds the paved-road portfolio a platform sub-org offers and the governance that keeps it coherent. **Makes the golden path the default choice across the sub-org, not the exception.** Scope: paved roads across a platform sub-org.
- **M5** — Depth: Drives the function's golden-path strategy and the trade-off between standardization and team autonomy. **Sets the paved-road principles the whole function designs to.** Scope: paved-road direction across the platform function.
- **M6** — Depth: Sets the org-wide philosophy of paved roads versus freedom. **Pioneers a golden-path model other engineering orgs adopt.** Scope: org-wide paved-road strategy.

##### Self-service & platform interfaces

*Anchor:* Bottcher, What I Talk About When I Talk About Platforms (martinfowler.com, 2018) — a platform's job is to cut cognitive load through interfaces developers use without asking anyone.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [OPS-27](../../data/capabilities.md#ops-27) — Platform & developer-experience engineering | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Keeps a self-service interface such as a portal, CLI, API, or template working for a common request so users do not file tickets. **Eliminates a manual request path by making it self-serve.** Scope: self-service on one platform team's surface.
- **M2** — Depth: Designs self-service for a critical platform capability with the right abstraction level and guardrails. **Removes the team as a human bottleneck from a high-volume workflow.** Scope: self-service for a high-stakes platform team.
- **M3** — Depth: Sets the self-service and interface standard other teams adopt. **Defines the interface-contract pattern, whether API, portal, or paved road, that several platform teams now expose.** Scope: self-service design across a cross-team domain.
- **M4** — Depth: Builds the self-service platform model a sub-org runs on, a coherent developer surface rather than scattered tools. **Shifts the sub-org's platforms from ticket-driven to self-service by default.** Scope: platform interfaces across a platform sub-org.
- **M5** — Depth: Drives the function's self-service strategy and its internal-developer-platform vision. **Sets the target that platform work is consumed without human intervention across the function.** Scope: self-service direction across the platform function.
- **M6** — Depth: Sets the org-wide bar for developer self-service. **Pioneers an internal-platform interface model the industry references.** Scope: org-wide self-service platform.

##### Adoption & migration strategy

*Anchor:* Winters, Manshreck & Wright, Software Engineering at Google (2020) - deprecation chapter — a platform only creates value once adopted, and migrations and deprecations must be engineered and finished, not merely mandated.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [OPS-33](../../data/capabilities.md#ops-33) | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Drives adoption of a platform capability by making migration easy with codemods, docs, and hands-on help. **Moves the first cohort of teams onto a new platform version.** Scope: adoption on one platform team's surface.
- **M2** — Depth: Runs a migration for a critical platform area, tracking adoption and burning down the long tail. **Completes a migration including the last stubborn holdouts rather than stalling at eighty percent.** Scope: migration for a high-stakes platform capability.
- **M3** — Depth: Sets the adoption and deprecation strategy other platform teams follow. **Defines the deprecation policy and migration-support standard several teams' rollouts now run on.** Scope: adoption strategy across a cross-team domain.
- **M4** — Depth: Builds the migration operating model a sub-org uses, with incentives, tracking, and deprecation guarantees so platform change lands without stranding teams. **Drives a sub-org-wide migration to completion through the teams that own each service.** Scope: migration across a platform sub-org.
- **M5** — Depth: Drives the function's adoption strategy and its balance of carrots versus mandates. **Sets the adoption and sunsetting principles the function commits to.** Scope: adoption direction across the platform function.
- **M6** — Depth: Sets the org-wide expectation for how platforms are adopted and legacy is retired. **Pioneers a migration model that keeps the org off long-lived forks.** Scope: org-wide adoption and deprecation.

##### Platform advocacy & enablement

*Anchor:* CNCF TAG App Delivery, Platform Engineering Maturity Model (2023) — platforms succeed on enablement and advocacy as much as on the technology.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [DR-01](../../data/capabilities.md#dr-01) — Developer advocacy & community building | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Runs enablement for the platform through docs, office hours, and demos. **Turns a confused user base into a competent one for one capability through documentation and support.** Scope: advocacy for one platform team's users.
- **M2** — Depth: Builds the enablement program for a critical platform area, from onboarding guides to champions and feedback channels. **Grows an internal champion network that advocates the platform without the team present.** Scope: enablement for a high-stakes platform team.
- **M3** — Depth: Sets the advocacy and enablement standard other platform teams adopt. **Stands up a platform-community and docs practice several teams run their enablement through.** Scope: enablement across a cross-team domain.
- **M4** — Depth: Builds the developer-relations model a platform sub-org uses to drive internal awareness and adoption. **Makes platform enablement a repeatable function rather than heroics across the sub-org.** Scope: advocacy across a platform sub-org.
- **M5** — Depth: Drives how the function positions and evangelizes itself to engineering and the business. **Sets the enablement and advocacy strategy the function invests in.** Scope: advocacy across the platform function.
- **M6** — Depth: Sets the org-wide platform-advocacy posture. **Pioneers an internal developer-relations model peer functions and other orgs copy.** Scope: org-wide platform advocacy.

### Reliability & Operations

#### Reliability Engineering

##### Reliability, SLOs & error budgets

*Anchor:* Beyer, Jones, Petoff & Murphy, Site Reliability Engineering (2016) — SLOs and error budgets turn reliability from opinion into an explicit, negotiable target.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [OPS-04](../../data/capabilities.md#ops-04) — Reliability & Production Operations | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Runs the team's services on defined SLOs and error budgets and reviews budget burn. **Uses an error-budget breach to hold a release-versus-reliability trade-off honestly.** Scope: SLOs for one platform team's services.
- **M2** — Depth: Designs the SLO and error-budget model for a critical platform area with meaningful SLIs. **Negotiates and enforces an error-budget policy that pauses feature work when reliability slips.** Scope: reliability targets for a high-stakes platform team.
- **M3** — Depth: Sets the SLO and error-budget standard other platform teams adopt. **Defines the reliability-target framework several teams now run their services against.** Scope: reliability targets across a cross-team domain.
- **M4** — Depth: Builds the reliability operating model a sub-org runs on, from SLO taxonomy to budget governance and reliability reviews. **Makes error-budget policy the mechanism the sub-org's prioritization respects.** Scope: reliability across a platform sub-org.
- **M5** — Depth: Drives the function's reliability strategy and its explicit trade-off with velocity. **Sets the reliability commitments the function makes to the business.** Scope: reliability across the platform function.
- **M6** — Depth: Sets the org-wide reliability philosophy and the availability posture the company commits to customers. **Pioneers a reliability model other orgs adopt.** Scope: org-wide reliability.

##### Incident & operational-risk leadership

*Anchor:* PagerDuty, Incident Response Guide (2017); Allspaw, Blameless PostMortems (2012) — how an org runs incidents and blameless learning decides whether outages recur.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [EM-10](../../data/capabilities.md#em-10) — Incident & operational risk management | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Runs the team's on-call and incident process and acts as commander when needed. **Turns a postmortem's action items into shipped fixes rather than a filed document.** Scope: incident response on one platform team.
- **M2** — Depth: Leads response for severe, cross-team incidents on a critical platform, coordinating comms and command under pressure. **Runs a major-incident review whose systemic fixes prevent the class of failure from recurring.** Scope: incident leadership for a high-stakes platform.
- **M3** — Depth: Sets the incident-management standard other platform teams adopt. **Defines the incident-command and postmortem practice several teams now run.** Scope: incident leadership across a cross-team domain.
- **M4** — Depth: Builds the incident-response operating model a sub-org relies on, from severity taxonomy to comms protocol and learning loop. **Drives a measurable drop in MTTR or repeat incidents across the sub-org through the leaders who own each service.** Scope: incident leadership across a platform sub-org.
- **M5** — Depth: Drives the function's operational-excellence and reliability-leadership strategy. **Sets the incident and reliability standard the function is accountable to.** Scope: reliability leadership across the platform function.
- **M6** — Depth: Sets the org-wide incident-management and reliability-leadership model. **Pioneers an operational-excellence practice other orgs reference.** Scope: org-wide incident and reliability leadership.

##### Observability & health signals

*Anchor:* Majors, Fong-Jones & Miranda, Observability Engineering (2022) — you cannot operate or improve what you cannot see.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [OPS-05](../../data/capabilities.md#ops-05) — Observability & Instrumentation | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Ensures the team's services are observable across metrics, logs, traces, and actionable alerts. **Replaces a noisy or blind alert with a signal that maps to real user pain.** Scope: observability for one platform team's services.
- **M2** — Depth: Designs the observability strategy for a critical platform area, including SLI instrumentation and high-cardinality debugging. **Makes a previously opaque failure mode diagnosable in minutes.** Scope: observability for a high-stakes platform team.
- **M3** — Depth: Sets the observability standard other platform teams adopt. **Defines the instrumentation and alerting baseline several teams now build to.** Scope: observability across a cross-team domain.
- **M4** — Depth: Builds the observability platform and practice a sub-org runs on, controlling cost and cardinality. **Makes health signals consistent and comparable across the sub-org's services.** Scope: observability across a platform sub-org.
- **M5** — Depth: Drives the function's observability strategy and its economics. **Sets the observability standard the function commits to.** Scope: observability across the platform function.
- **M6** — Depth: Sets the org-wide observability model. **Pioneers an approach to health signals other orgs adopt.** Scope: org-wide observability.

#### Operational Leverage

##### Toil reduction & automation

*Anchor:* Beyer, Jones, Petoff & Murphy, Site Reliability Engineering (2016) - toil chapter — unmanaged toil caps leverage; automating it is how platform scales sublinearly with load.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [OPS-28](../../data/capabilities.md#ops-28) — Automation-first operations | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Tracks the team's toil and automates the worst of it to protect engineering time. **Converts a recurring manual operational task into an automated one.** Scope: toil on one platform team.
- **M2** — Depth: Sets a toil budget for a critical platform team and drives it down structurally. **Cuts on-call and operational load enough to visibly change the team's toil ratio.** Scope: toil for a high-stakes platform team.
- **M3** — Depth: Sets the toil-measurement and automation standard other platform teams adopt. **Defines the toil-budget practice several teams now manage their operational load with.** Scope: toil reduction across a cross-team domain.
- **M4** — Depth: Builds the automation strategy a sub-org uses to keep operational cost sublinear as it scales. **Drives a sub-org-wide reduction in toil through the platforms that eliminate it.** Scope: automation leverage across a platform sub-org.
- **M5** — Depth: Drives the function's operational-leverage strategy, targeting where automation investment buys the most headroom. **Sets the toil and automation targets the function commits to.** Scope: operational leverage across the platform function.
- **M6** — Depth: Sets the org-wide expectation that operations scale through automation, not headcount. **Pioneers an operational-leverage model other orgs adopt.** Scope: org-wide operational leverage.

##### Capacity, performance & cost

*Anchor:* Gregg, Systems Performance (2nd ed., 2020) — capacity, performance, and cost are one coupled system, the FinOps lever of a platform.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [OPS-07](../../data/capabilities.md#ops-07) — Cost & Performance Optimization | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Watches the team's capacity, performance, and spend. **Right-sizes a resource or fixes a performance regression to cut cost without hurting reliability.** Scope: capacity and cost for one platform team's services.
- **M2** — Depth: Owns capacity and cost planning for a critical platform area, forecasting demand and managing efficiency. **Lands a material infrastructure-cost reduction while holding SLOs.** Scope: capacity and FinOps for a high-stakes platform team.
- **M3** — Depth: Sets the capacity-planning and cost-efficiency standard other platform teams adopt. **Defines the FinOps and performance practice several teams now manage spend with.** Scope: capacity and cost across a cross-team domain.
- **M4** — Depth: Builds the capacity and FinOps operating model a sub-org runs on, from forecasting to unit economics and efficiency governance. **Makes infrastructure unit cost a managed, trending metric across the sub-org.** Scope: capacity and cost across a platform sub-org.
- **M5** — Depth: Drives the function's infrastructure-efficiency and cost strategy and its business framing. **Sets the unit-economics and capacity commitments the function owns.** Scope: capacity and FinOps across the platform function.
- **M6** — Depth: Sets the org-wide infrastructure-efficiency posture and the company's cloud and capital strategy for platform. **Pioneers a FinOps model the business plans spend around.** Scope: org-wide capacity, performance, and cost.

### Technical Direction & Architecture

#### Architecture & Standards

##### Platform architecture stewardship

*Anchor:* Conway (1968); Nygard, Documenting Architecture Decisions (2011) — platform architecture and org design are coupled, and decisions must be recorded to hold coherence.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [ARC-10](../../data/capabilities.md#arc-10) — Architectural trade-off analysis | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Stewards the team's platform architecture and keeps decisions recorded as ADRs. **Catches an architectural drift or coupling problem in review before it ships.** Scope: architecture for one platform team's surface.
- **M2** — Depth: Owns architectural direction for a critical platform area, weighing evolvability and Conway-aligned boundaries. **Redesigns a component boundary so team and system seams line up.** Scope: architecture for a high-stakes platform team.
- **M3** — Depth: Sets the architecture and ADR standard other platform teams adopt. **Defines the reference architecture and decision-record practice several teams now build within.** Scope: architecture stewardship across a cross-team domain.
- **M4** — Depth: Builds the architecture-governance model a sub-org runs on, from review forums to principles and Conway-aware team-and-system design. **Shapes a sub-org's team topology to fit the platform architecture it needs.** Scope: architecture across a platform sub-org.
- **M5** — Depth: Drives the function's architectural direction and its long-horizon coherence. **Sets the architecture principles the function builds against.** Scope: architecture across the platform function.
- **M6** — Depth: Sets the org-wide platform-architecture vision and the socio-technical structure to realize it. **Pioneers an architecture other orgs study.** Scope: org-wide platform architecture.

##### Engineering standards & quality

*Anchor:* Humble & Farley, Continuous Delivery (2010) — quality is built in through automation and standards, not inspected in afterward.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [SWE-02](../../data/capabilities.md#swe-02) — Code Quality & Maintainability | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Holds the team to engineering standards across CI, testing, code review, and deployment safety. **Raises a slipping quality practice such as test coverage or review rigor on the team.** Scope: standards on one platform team.
- **M2** — Depth: Sets the quality bar for a critical platform team, including continuous delivery, progressive delivery, and change safety. **Installs a delivery-safety practice that measurably cuts change-failure rate.** Scope: standards for a high-stakes platform team.
- **M3** — Depth: Sets the engineering-standards baseline other platform teams adopt. **Defines the CI/CD and quality standard several teams now build to.** Scope: standards across a cross-team domain.
- **M4** — Depth: Builds the engineering-excellence model a sub-org runs on, from golden paths for quality to paved CI/CD and standards governance. **Makes high-quality delivery the default path across the sub-org.** Scope: standards across a platform sub-org.
- **M5** — Depth: Drives the function's engineering-quality strategy and its link to delivery performance. **Sets the quality standard the function commits to.** Scope: standards across the platform function.
- **M6** — Depth: Sets the org-wide engineering-quality bar. **Pioneers a standards model other functions adopt.** Scope: org-wide engineering standards.

##### Technical debt & modernization

*Anchor:* Cunningham, The WyCash Portfolio Management System (1992) — debt is a deliberate liability with interest, paid down on purpose, not neglected mess.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [EM-15](../../data/capabilities.md#em-15) — Technical debt & risk stewardship | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Tracks the team's tech debt and budgets time to pay it down deliberately. **Makes a debt trade-off explicit in planning rather than letting it accrue silently.** Scope: debt on one platform team.
- **M2** — Depth: Manages debt and modernization for a critical platform area, sequencing paydown against risk. **Funds and lands a modernization that removes a systemic drag on the team.** Scope: debt for a high-stakes platform team.
- **M3** — Depth: Sets the debt-management standard other platform teams adopt. **Defines the debt-accounting and modernization practice several teams now prioritize with.** Scope: debt strategy across a cross-team domain.
- **M4** — Depth: Builds the modernization roadmap a sub-org runs on, balancing debt paydown against new capability. **Wins sustained investment for a sub-org-wide modernization others deprioritized.** Scope: modernization across a platform sub-org.
- **M5** — Depth: Drives the function's technical-health and modernization strategy. **Sets the debt and modernization commitments the function makes.** Scope: technical health across the platform function.
- **M6** — Depth: Sets the org-wide posture on technical debt and legacy modernization. **Pioneers a debt-management model the business funds against.** Scope: org-wide modernization.

#### Technical Strategy & Risk

##### Technical strategy & investment

*Anchor:* Larson, An Elegant Puzzle (2019); Wardley Maps (2016) — technical strategy is placing a few high-leverage bets and mapping where value sits.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [LI-03](../../data/capabilities.md#li-03) — Technical Influence & Direction | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Connects the team's technical choices to a coherent direction. **Frames a build decision as a bet with a stated rationale, not an ad-hoc pick.** Scope: technical direction for one platform team.
- **M2** — Depth: Sets multi-quarter technical strategy for a critical platform area, sequencing investment by leverage. **Makes a hard technical-investment call such as rebuild versus extend and defends it with evidence.** Scope: technical strategy for a high-stakes platform team.
- **M3** — Depth: Sets a cross-team technical strategy other teams align to. **Publishes a domain technical strategy or Wardley map that redirects where several teams invest.** Scope: technical strategy across a cross-team domain.
- **M4** — Depth: Builds the technical-investment thesis a sub-org executes, deciding where to concentrate platform bets over years. **Frames the small set of bets the sub-org organizes its roadmap around.** Scope: technical strategy across a platform sub-org.
- **M5** — Depth: Drives the function's technical strategy and its alignment to business strategy. **Sets the technology bets the function commits capital and headcount to.** Scope: technical strategy across the platform function.
- **M6** — Depth: Sets the org-wide platform-technology direction and the long-horizon infrastructure bets. **Pioneers a technical strategy the company's product strategy depends on.** Scope: org-wide technical strategy.

##### Vendor & build/buy/adopt strategy

*Anchor:* Korn Ferry Leadership Architect (2014) - Financial Acumen — build-vs-buy and vendor choices are capital-allocation decisions needing financial judgment.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [EM-06](../../data/capabilities.md#em-06) — Budget & vendor management | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Makes build/buy/adopt calls for the team's tooling with a stated cost and benefit. **Avoids building something a supported off-the-shelf option already solves.** Scope: build/buy for one platform team.
- **M2** — Depth: Runs build/buy/adopt and vendor evaluations for a critical platform area, including total cost of ownership and lock-in risk. **Negotiates or selects a platform vendor on a defensible total-cost basis.** Scope: build/buy for a high-stakes platform team.
- **M3** — Depth: Sets the build/buy/adopt decision standard other platform teams use. **Defines the evaluation and vendor-selection framework several teams now decide with.** Scope: sourcing strategy across a cross-team domain.
- **M4** — Depth: Builds the vendor and sourcing strategy a sub-org runs on, managing the platform supplier portfolio and consolidation. **Drives a sub-org-wide build-versus-buy decision with material budget impact.** Scope: sourcing across a platform sub-org.
- **M5** — Depth: Drives the function's build/buy and vendor strategy and its capital implications. **Sets the sourcing principles and major vendor relationships the function commits to.** Scope: sourcing across the platform function.
- **M6** — Depth: Sets the org-wide platform build-versus-buy posture and negotiates strategic supplier relationships. **Pioneers a sourcing strategy the business plans capital around.** Scope: org-wide sourcing and vendor strategy.

##### Secure-by-default platform & guardrails

*Anchor:* OWASP, Application Security Verification Standard (v4, 2019) — platforms are the leverage point where security is built in for everyone or absent for everyone.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [SEC-18](../../data/capabilities.md#sec-18) — Guardrails & policy as code | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Holds the team to security and compliance baselines. **Bakes a security control into the platform so users get it by default rather than bolting it on.** Scope: security posture for one platform team's surface.
- **M2** — Depth: Owns the security and compliance posture for a critical platform area, managing risk and remediation. **Closes a systemic vulnerability class through a platform control rather than one-off fixes.** Scope: security for a high-stakes platform team.
- **M3** — Depth: Sets the security and compliance standard other platform teams adopt. **Defines the paved-road security controls several teams now inherit by default.** Scope: security posture across a cross-team domain.
- **M4** — Depth: Builds the security and compliance operating model a sub-org runs on, from controls-as-code to audit readiness and risk governance. **Makes secure-by-default the path of least resistance across the sub-org.** Scope: security across a platform sub-org.
- **M5** — Depth: Drives the function's security and risk strategy and its regulatory posture. **Sets the risk commitments and compliance guarantees the function owns.** Scope: security across the platform function.
- **M6** — Depth: Sets the org-wide platform-security and risk posture. **Pioneers a secure-platform model auditors and peers reference.** Scope: org-wide security and risk.

### Delivery & Execution

#### Planning & Prioritization

##### Planning & estimation

*Anchor:* McConnell, Software Estimation (2006) — estimation is a probabilistic forecast to calibrate, not a promise, and platform work is especially uncertain.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [PD-04](../../data/capabilities.md#pd-04) — Estimation & Planning | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Runs the team's planning with realistic, range-based estimates. **Surfaces a schedule risk early instead of discovering the slip at the deadline.** Scope: planning for one platform team.
- **M2** — Depth: Plans complex, cross-dependent platform work with calibrated estimates and buffers. **Replans a high-stakes platform delivery mid-flight without losing the commitment.** Scope: planning for a critical platform team.
- **M3** — Depth: Sets the planning and estimation standard other platform teams adopt. **Defines the forecasting practice several teams now plan with.** Scope: planning across a cross-team domain.
- **M4** — Depth: Builds the planning operating model a sub-org runs on, from commitment framing to capacity-based forecasting and uncertainty comms. **Makes sub-org delivery forecasts credible to stakeholders.** Scope: planning across a platform sub-org.
- **M5** — Depth: Drives the function's planning cadence and its integration with company planning. **Sets the planning discipline the function commits to.** Scope: planning across the platform function.
- **M6** — Depth: Sets the org-wide planning model for platform investment. **Pioneers a forecasting practice other functions adopt.** Scope: org-wide platform planning.

##### Prioritization & trade-offs

*Anchor:* Reinertsen, The Principles of Product Development Flow (2009) — prioritizing by cost of delay and managing queues, not utilization, maximizes economic flow.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [PD-02](../../data/capabilities.md#pd-02) — Prioritization & Economic Thinking | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Prioritizes the team's backlog against value and urgency. **Says no to a low-value request with a clear rationale rather than absorbing everything.** Scope: prioritization for one platform team.
- **M2** — Depth: Makes hard prioritization calls for a critical platform area using cost-of-delay thinking. **Defends a contested platform trade-off between competing stakeholder demands.** Scope: prioritization for a high-stakes platform team.
- **M3** — Depth: Sets the prioritization framework other platform teams adopt. **Installs a cost-of-delay or WSJF practice several teams now sequence with.** Scope: prioritization across a cross-team domain.
- **M4** — Depth: Builds the portfolio-prioritization model a sub-org allocates by, balancing platform bets against keep-the-lights-on. **Arbitrates a sub-org-wide trade-off that reallocates investment.** Scope: prioritization across a platform sub-org.
- **M5** — Depth: Drives how the function prioritizes across competing business demands. **Sets the prioritization principles the function commits capacity against.** Scope: prioritization across the platform function.
- **M6** — Depth: Sets the org-wide framework for prioritizing platform investment. **Pioneers a portfolio-prioritization model other functions adopt.** Scope: org-wide prioritization.

##### Capacity & resource allocation

*Anchor:* Brooks, The Mythical Man-Month (1975) — people and time do not trade linearly, so allocation is a judgment lever.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [EM-05](../../data/capabilities.md#em-05) — Headcount & resource planning | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Allocates the team's capacity across roadmap, on-call, and interrupts. **Protects focus time rather than fragmenting the team across too many fronts.** Scope: capacity for one platform team.
- **M2** — Depth: Balances capacity for a critical platform team across delivery, reliability, and toil. **Rebalances staffing to unblock a priority without wrecking sustainability.** Scope: capacity for a high-stakes platform team.
- **M3** — Depth: Sets the capacity-allocation standard other platform leads use. **Defines the staffing and load-balancing model several teams now allocate with.** Scope: allocation across a cross-team domain.
- **M4** — Depth: Builds the resource-allocation model a sub-org runs on, mapping headcount to bets with realistic ramp and no linear-scaling assumptions. **Reallocates capacity across a sub-org to match investment shifts.** Scope: allocation across a platform sub-org.
- **M5** — Depth: Drives how the function allocates headcount against strategy. **Sets the resourcing principles the function plans against.** Scope: allocation across the platform function.
- **M6** — Depth: Sets the org-wide model for allocating platform capacity. **Pioneers a resourcing approach other functions adopt.** Scope: org-wide capacity allocation.

#### Delivery Management

##### Predictable delivery & flow

*Anchor:* Forsgren, Humble & Kim, Accelerate (2018) — predictable, high-frequency delivery is an engineered property that predicts org performance.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [EM-07](../../data/capabilities.md#em-07) — Delivery & program management | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Runs the team to a predictable delivery cadence with small batches. **Removes a recurring flow blocker such as a handoff, review lag, or big-batch release that stalls delivery.** Scope: delivery flow for one platform team.
- **M2** — Depth: Engineers predictable delivery for a critical platform team under real operational load. **Stabilizes a team's delivery so its commitments become trustworthy.** Scope: flow for a high-stakes platform team.
- **M3** — Depth: Sets the delivery-flow standard other platform teams adopt. **Defines the flow and batch-size practice several teams now deliver with.** Scope: delivery flow across a cross-team domain.
- **M4** — Depth: Builds the delivery operating model a sub-org runs on, from flow metrics to dependency management and cadence. **Makes a sub-org's delivery predictable through the leaders who run each team.** Scope: flow across a platform sub-org.
- **M5** — Depth: Drives the function's delivery performance and its link to business outcomes. **Sets the flow and predictability standard the function commits to.** Scope: delivery across the platform function.
- **M6** — Depth: Sets the org-wide expectation for delivery performance. **Pioneers a flow model other functions adopt.** Scope: org-wide delivery flow.

##### Engineering metrics & delivery health

*Anchor:* Forsgren, Humble & Kim, Accelerate (2018) - DORA four keys; SPACE (2021) — DORA and SPACE give a validated, hard-to-game way to measure delivery, used to improve not to rank.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [EM-09](../../data/capabilities.md#em-09) — Engineering metrics & productivity | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Tracks the team's DORA and SPACE signals and uses them to improve, not to rank people. **Acts on a delivery-metric trend to fix an actual bottleneck.** Scope: metrics for one platform team.
- **M2** — Depth: Runs a metrics practice for a critical platform team that resists gaming and connects to outcomes. **Diagnoses a delivery-health problem from the four keys and fixes its root cause.** Scope: metrics for a high-stakes platform team.
- **M3** — Depth: Sets the delivery-metrics standard other platform teams adopt. **Defines the DORA and SPACE measurement several teams now steer by.** Scope: metrics across a cross-team domain.
- **M4** — Depth: Builds the delivery-health measurement system a sub-org runs on, making metrics comparable and honest. **Makes data-driven delivery improvement the norm across the sub-org.** Scope: metrics across a platform sub-org.
- **M5** — Depth: Drives how the function measures and reports delivery and developer productivity to the business. **Sets the metrics the function commits to and defends against misuse.** Scope: metrics across the platform function.
- **M6** — Depth: Sets the org-wide definition of engineering delivery health. **Pioneers a measurement model other functions adopt.** Scope: org-wide delivery metrics.

##### Process & continuous improvement

*Anchor:* Deming, Out of the Crisis (1986) — throughput comes from improving the system, not exhorting people.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [EM-08](../../data/capabilities.md#em-08) — Process & operating-cadence design | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Runs retros that produce real changes. **Removes a wasteful step from the team's process instead of adding ceremony.** Scope: process for one platform team.
- **M2** — Depth: Drives systemic process improvement on a critical platform team, attacking causes not symptoms. **Lands a process change that measurably improves throughput or quality.** Scope: process for a high-stakes platform team.
- **M3** — Depth: Sets the continuous-improvement practice other platform teams adopt. **Installs an improvement discipline several teams now run.** Scope: improvement across a cross-team domain.
- **M4** — Depth: Builds the operating rhythm and improvement system a sub-org runs on. **Makes systematic improvement, not firefighting, the sub-org's default mode.** Scope: process across a platform sub-org.
- **M5** — Depth: Drives the function's operating model and its improvement discipline. **Sets the process standards the function runs on.** Scope: process across the platform function.
- **M6** — Depth: Sets the org-wide operating model for platform. **Pioneers a continuous-improvement practice other functions adopt.** Scope: org-wide process.

##### Dependency & risk management

*Anchor:* NIST Cybersecurity Framework (2014); PMI PMBOK (2021) — platforms sit on everyone else's critical path, so cross-team dependency and risk work is core.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [RISK-01](../../data/capabilities.md#risk-01) — Enterprise risk management | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Tracks the team's dependencies and risks. **Flags and mitigates a cross-team dependency before it blocks delivery.** Scope: dependencies for one platform team.
- **M2** — Depth: Manages complex cross-team dependencies and risk for a critical platform. **Unblocks a delivery stalled on another team's dependency through negotiation, not escalation alone.** Scope: dependencies for a high-stakes platform team.
- **M3** — Depth: Sets the dependency and risk-management standard other platform teams adopt. **Defines the cross-team dependency and risk practice several teams now coordinate with.** Scope: dependency management across a cross-team domain.
- **M4** — Depth: Builds the risk and dependency-governance model a sub-org runs on, from risk registers to mitigation ownership and cross-team coordination. **De-risks a sub-org-wide initiative with many moving dependencies.** Scope: risk across a platform sub-org.
- **M5** — Depth: Drives the function's approach to systemic and platform-wide risk. **Sets the risk-management standard the function is accountable to.** Scope: risk across the platform function.
- **M6** — Depth: Sets the org-wide model for managing platform and infrastructure risk. **Pioneers a risk practice other functions adopt.** Scope: org-wide risk and dependencies.

### Strategy, Communication & Influence

#### Strategy & Change

##### Strategy formulation

*Anchor:* Rumelt, Good Strategy Bad Strategy (2011) — real strategy is a diagnosis plus a coherent guiding policy and actions, not a list of goals.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [STRAT-01](../../data/capabilities.md#strat-01) — Corporate strategy formulation | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Frames the team's direction as a real strategy of diagnosis, guiding policy, and action. **Names the core problem the team's strategy actually addresses rather than listing goals.** Scope: strategy for one platform team.
- **M2** — Depth: Formulates strategy for a critical platform area with a sharp diagnosis and honest trade-offs. **Produces a platform strategy that says no to things, not just yes.** Scope: strategy for a high-stakes platform team.
- **M3** — Depth: Sets a cross-team platform strategy others align to. **Publishes a domain strategy several teams reorient their plans around.** Scope: strategy across a cross-team domain.
- **M4** — Depth: Drives strategy for a platform sub-org, integrating multiple domains into one coherent guiding policy. **Builds a sub-org strategy that survives exec scrutiny and reallocates real investment.** Scope: strategy across a platform sub-org.
- **M5** — Depth: Drives the function's strategy and its coupling to company strategy. **Sets the strategic bets the function commits to and defends them at the top table.** Scope: strategy across the platform function.
- **M6** — Depth: Sets the org-wide platform strategy. **Pioneers a strategic thesis the company's direction depends on.** Scope: org-wide platform strategy.

##### Leading change & transformation

*Anchor:* Kotter, Leading Change (1996) — durable change needs urgency, coalition, and follow-through, not a mandate.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [EM-12](../../data/capabilities.md#em-12) — Change & transformation management | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Leads change on the team by building buy-in, not decree. **Gets a team through a tooling or process change without losing people or momentum.** Scope: change on one platform team.
- **M2** — Depth: Drives a significant change on a critical platform team against resistance. **Builds the coalition that makes a hard platform migration or reorg stick.** Scope: change for a high-stakes platform team.
- **M3** — Depth: Sets the change-leadership approach other platform leads adopt. **Drives a cross-team transformation through the leaders who own each team.** Scope: change across a cross-team domain.
- **M4** — Depth: Leads sub-org-wide transformation, sequencing urgency, coalition, and consolidation. **Lands a sub-org change that outlives the initial push.** Scope: change across a platform sub-org.
- **M5** — Depth: Drives change across the function and into its partner orgs. **Sets the change the function leads and sustains.** Scope: change across the platform function.
- **M6** — Depth: Sets and leads org-wide platform transformation. **Pioneers a change other functions model theirs on.** Scope: org-wide transformation.

##### Organizational & team design

*Anchor:* Skelton & Pais, Team Topologies (2019); Conway (1968) — team boundaries shape the software, and platform teams exist to cut others' cognitive load.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [EM-04](../../data/capabilities.md#em-04) — Team design & org structuring | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Shapes the team's roles, boundaries, and interaction modes deliberately. **Clarifies a fuzzy team boundary that was causing thrash.** Scope: team design for one platform team.
- **M2** — Depth: Designs the structure of a critical platform team and its interaction modes, whether X-as-a-service or collaboration. **Restructures a team so its boundary matches the platform it owns.** Scope: team design for a high-stakes platform team.
- **M3** — Depth: Sets the team-topology approach other platform leads adopt. **Redesigns team boundaries across the domain to cut cross-team cognitive load.** Scope: org design across a cross-team domain.
- **M4** — Depth: Designs the org structure of a platform sub-org using stream-aligned, platform, and enabling patterns. **Proposes and drives a sub-org reshape that improves flow.** Scope: org design across a platform sub-org.
- **M5** — Depth: Drives the function's org design and its Conway-aligned interfaces to product orgs. **Sets the operating structure the function runs on.** Scope: org design across the platform function.
- **M6** — Depth: Sets the org-wide socio-technical structure for platform. **Pioneers an operating model other functions adopt.** Scope: org-wide org design.

#### Communication & Influence

##### Executive & stakeholder communication

*Anchor:* Duarte, HBR Guide to Persuasive Presentations (2012) — leaders move resources through clear, audience-tuned narrative, not data dumps.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [CC-06](../../data/capabilities.md#cc-06) — Executive Communication | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Communicates the team's work clearly to stakeholders, tuned to the audience. **Translates a technical platform issue into terms a non-engineer decision-maker acts on.** Scope: communication for one platform team.
- **M2** — Depth: Represents a critical platform area to senior stakeholders with a clear narrative under scrutiny. **Gets a skeptical stakeholder to a decision through a well-framed case.** Scope: communication for a high-stakes platform team.
- **M3** — Depth: Sets the communication standard other platform leads adopt. **Crafts the platform narrative several teams reuse to align stakeholders.** Scope: communication across a cross-team domain.
- **M4** — Depth: Drives the platform narrative to executive audiences and wins decisions and funding. **Turns a complex platform investment into an exec-level story that lands the budget.** Scope: exec communication for a platform sub-org.
- **M5** — Depth: Represents developer productivity and platform value to the top of the company. **Sets how the function tells its story to the board and business.** Scope: communication across the platform function.
- **M6** — Depth: Sets the org-wide platform narrative. **Speaks for platform to the board and externally as a recognized voice.** Scope: org-wide and external communication.

##### Stakeholder management & partnership

*Anchor:* Freeman, Strategic Management: A Stakeholder Approach (1984) — platform serves many internal stakeholders with conflicting needs, and managing them is the job.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [PM-13](../../data/capabilities.md#pm-13) — Stakeholder & executive management | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Builds working relationships with the platform's stakeholder teams. **Turns a frustrated internal customer into a collaborating partner.** Scope: stakeholders for one platform team.
- **M2** — Depth: Manages a complex, multi-stakeholder relationship for a critical platform, balancing conflicting needs. **Brokers a durable agreement between platform and a demanding consumer team.** Scope: stakeholders for a high-stakes platform team.
- **M3** — Depth: Sets the stakeholder-partnership approach other platform leads adopt. **Builds the cross-team partnership model several teams manage relationships through.** Scope: stakeholder management across a cross-team domain.
- **M4** — Depth: Builds the stakeholder-governance model a sub-org runs on, from partnership forums to expectation-setting and escalation paths. **Realigns a strained sub-org-level partnership with a major consumer org.** Scope: partnership across a platform sub-org.
- **M5** — Depth: Drives the function's key executive and cross-functional partnerships. **Sets the partnership approach the function relies on.** Scope: partnership across the platform function.
- **M6** — Depth: Sets the org-wide model for platform's partnerships. **Pioneers a stakeholder approach other functions adopt.** Scope: org-wide partnership.

##### Cross-org influence & alignment

*Anchor:* Cohen & Bradford, Influence Without Authority (1989); Bungay, The Art of Action (2011) — platform leaders get outcomes across teams they do not own, through reciprocity and clear intent.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [LI-07](../../data/capabilities.md#li-07) — Influence without Authority | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Gets outcomes from teams they do not manage through reciprocity and clarity. **Aligns another team to a shared platform goal without authority over them.** Scope: influence for one platform team.
- **M2** — Depth: Aligns multiple teams around a critical platform direction under real disagreement. **Builds cross-team agreement on a contested platform standard.** Scope: influence for a high-stakes platform team.
- **M3** — Depth: Sets the alignment approach other platform leads adopt. **Drives alignment across a domain by clear intent, commander's-intent style, rather than escalation.** Scope: influence across a cross-team domain.
- **M4** — Depth: Builds cross-org alignment a sub-org depends on, aligning peer orgs to platform direction. **Wins peer-org buy-in for a sub-org-wide platform initiative.** Scope: influence across a platform sub-org.
- **M5** — Depth: Drives alignment across the function's peer organizations at the leadership level. **Sets the alignment mechanisms the function relies on to move the wider org.** Scope: influence across the platform function.
- **M6** — Depth: Sets org-wide alignment on platform direction. **Pioneers an influence model that aligns the whole company behind platform bets.** Scope: org-wide influence.

### Self & Personal Effectiveness

*Shared verbatim with the Engineering Management canon — same capability ids, anchors, and curves. These competencies are written in the manager-judgment register (leverage, delegation, self-awareness, resilience, decision-making, ethics) and are not platform-contingent.*

#### Leverage & Delegation

##### Managerial leverage & focus

*Anchor:* Grove, High Output Management (1983); Drucker (1967) — a manager's output is the leveraged output of everyone they touch, and time is the one non-renewable resource.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [EM-16](../../data/capabilities.md#em-16) — Managerial leverage & focus | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Spends their own time on the few activities that most move the team, and audits where it actually goes. **Drops a low-leverage habit such as reviewing every change themselves once they see its cost.** Scope: personal leverage on one platform team.
- **M2** — Depth: Redesigns their week around the highest-leverage work on a high-stakes team — the decisions, unblocks, and reviews only they can do — and hands off the rest. **Restructures how they spend time so a critical platform team stops waiting on them.** Scope: personal leverage on a critical platform team.
- **M3** — Depth: Sets the leverage practice other platform leads pick up, favoring mechanisms that multiply reach over adding meetings. **Publishes an operating cadence several leads adopt to reclaim their own high-leverage time.** Scope: leverage practice across a cross-team domain.
- **M4** — Depth: Builds the operating rhythm a platform sub-org runs on so decisions happen at the lowest capable level rather than on one desk. **Removes themselves as a bottleneck across the sub-org by installing the mechanisms that decide without them.** Scope: leverage across a platform sub-org.
- **M5** — Depth: Drives how the function protects its leaders' focus and concentrates effort on the few bets that matter. **Sets the focus and leverage norms leaders across the function organize their time around.** Scope: leverage across the platform function.
- **M6** — Depth: Sets the org-wide expectation for how platform leadership spends its scarce attention. **Pioneers a leverage model peer functions adopt.** Scope: org-wide leadership leverage.

##### Delegation & empowerment

*Anchor:* Marquet, Turn the Ship Around! (2012) — leadership scales by pushing authority to where the information is, creating leaders rather than followers.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [EM-14](../../data/capabilities.md#em-14) — Delegation & empowerment | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Delegates real ownership, not just tasks, and matches each handoff to the engineer's readiness. **Hands a platform workstream to an engineer with the decision rights to run it, then holds back.** Scope: delegation on one platform team.
- **M2** — Depth: Empowers senior engineers and leads to own hard, ambiguous platform work and make the calls themselves. **Grows a report into someone who runs a critical workstream end to end without checking in.** Scope: delegation on a critical platform team.
- **M3** — Depth: Sets the delegation and empowerment standard other platform leads adopt, favoring intent and guardrails over instructions. **Gets outcomes across a domain by stating clear intent and letting other leaders decide how.** Scope: empowerment across a cross-team domain.
- **M4** — Depth: Builds the decision-rights model a platform sub-org runs on so authority sits with the people closest to the work. **Pushes a class of decisions down to team leaders across the sub-org and stops being consulted on them.** Scope: empowerment across a platform sub-org.
- **M5** — Depth: Drives how the function distributes authority, growing decision-makers rather than approvers. **Sets the empowerment norms leaders across the function lead by.** Scope: empowerment across the platform function.
- **M6** — Depth: Sets the org-wide expectation that platform leadership creates leaders, not dependence. **Pioneers a decision-rights model other functions adopt.** Scope: org-wide empowerment.

#### Growth & Resilience

##### Self-awareness & learning agility

*Anchor:* Eurich, Insight (2017); Lombardo & Eichinger (2000) — accurate self-knowledge and the ability to learn from new experience predict leadership growth.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [LI-09](../../data/capabilities.md#li-09) — Self-Awareness & Learning Agility | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Seeks feedback on their own leadership and acts on it visibly. **Changes a specific behavior after hearing it lands badly, rather than defending it.** Scope: personal growth on one platform team.
- **M2** — Depth: Reads their own impact on a high-stakes team accurately and adapts to unfamiliar problems quickly. **Names a blind spot and adjusts before it costs the team, using an outside read to check their own.** Scope: self-awareness on a critical platform team.
- **M3** — Depth: Sets the norm that platform leads solicit and act on feedback, and models learning in the open. **Runs feedback mechanisms several leads adopt to see their own effect on others.** Scope: learning culture across a cross-team domain.
- **M4** — Depth: Builds the leadership-feedback and development practice a sub-org relies on to keep its leaders self-correcting. **Turns a leader's blind spot around across the sub-org by making honest upward feedback safe and routine.** Scope: leader growth across a platform sub-org.
- **M5** — Depth: Drives how the function grows self-aware, adaptable leaders as the technology and org shift. **Sets the learning-agility expectations leaders across the function are developed against.** Scope: leadership growth across the platform function.
- **M6** — Depth: Sets the org-wide expectation that platform leadership learns and adapts in the open. **Pioneers a leadership-development model peer functions adopt.** Scope: org-wide leadership learning.

##### Resilience & sustainable pace

*Anchor:* Loehr & Schwartz, The Power of Full Engagement (2003) — performance is a function of managed energy, not time, and sustainable pace beats heroics.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [LI-10](../../data/capabilities.md#li-10) — Resilience & Sustainable Pace | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Keeps themselves and the team steady through incidents and crunch without burning out. **Protects the team's sustainable pace during an on-call-heavy stretch instead of normalizing heroics.** Scope: resilience on one platform team.
- **M2** — Depth: Holds their composure and the team's under sustained operational pressure on a critical platform. **Absorbs the stress of a severe outage period and keeps the team functioning rather than fraying.** Scope: resilience on a critical platform team.
- **M3** — Depth: Sets the sustainable-pace norms other platform leads adopt, treating on-call and toil load as a health metric. **Acts on a burnout signal across the domain before it becomes attrition, changing the load rather than the people.** Scope: sustainable pace across a cross-team domain.
- **M4** — Depth: Builds the operating norms a platform sub-org uses to keep pace sustainable through scaling and incidents. **Reshapes on-call and workload across the sub-org so resilience does not depend on individual heroics.** Scope: sustainable pace across a platform sub-org.
- **M5** — Depth: Drives how the function sustains its people through the always-on nature of platform work. **Sets the sustainable-pace expectations leaders across the function are held to.** Scope: resilience across the platform function.
- **M6** — Depth: Sets the org-wide expectation that platform delivers durably, not through burnout. **Pioneers a sustainable-operations model peer functions adopt.** Scope: org-wide sustainable pace.

#### Judgment & Integrity

##### Decision-making under uncertainty

*Anchor:* Kahneman, Thinking, Fast and Slow (2011) — sound decisions require guarding against bias and calibrating confidence to the evidence.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [LI-04](../../data/capabilities.md#li-04) — Decision-Making under Uncertainty | [P2](../../data/proficiency_scale.md#p2) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Makes timely calls with incomplete information and states the assumptions behind them. **Makes a reversible platform decision quickly rather than stalling for certainty that will not come.** Scope: decisions on one platform team.
- **M2** — Depth: Makes high-stakes, hard-to-reverse calls on a critical platform and guards against their own bias. **Frames a one-way-door platform decision explicitly and gathers the evidence its weight warrants.** Scope: decisions on a critical platform team.
- **M3** — Depth: Sets the decision-making discipline other platform leads adopt, with clear owners, reversibility tests, and recorded rationale. **Installs a decision framework several teams now use to make calls under ambiguity.** Scope: decision quality across a cross-team domain.
- **M4** — Depth: Builds the decision-rights and judgment norms a sub-org runs on so hard calls get made well and fast across it. **Raises the quality of consequential decisions across the sub-org by making the reasoning and the owner explicit.** Scope: decision-making across a platform sub-org.
- **M5** — Depth: Drives how the function makes irreversible, high-ambiguity bets and lives with the trade-offs. **Sets the decision standard leaders across the function are calibrated to.** Scope: decision-making across the platform function.
- **M6** — Depth: Sets the org-wide expectation for how platform leadership decides under uncertainty. **Pioneers a decision model peer functions adopt.** Scope: org-wide decision-making.

##### Ethics, integrity & trust

*Anchor:* Mayer, Davis & Schoorman (1995); ACM Code of Ethics (2018) — trust is built on ability, benevolence, and integrity, and platform leaders hold outsized access and impact.


| OCF | M1 | M2 | M3 | M4 | M5 | M6 |
|---|---|---|---|---|---|---|
| [LI-11](../../data/capabilities.md#li-11) — Integrity & Trust | [P3](../../data/proficiency_scale.md#p3) | [P3](../../data/proficiency_scale.md#p3) | [P4](../../data/proficiency_scale.md#p4) | [P4](../../data/proficiency_scale.md#p4) | [P5](../../data/proficiency_scale.md#p5) | [P6](../../data/proficiency_scale.md#p6) |


- **M1** — Depth: Acts consistently and honestly, keeps commitments, and is straight about mistakes. **Makes the honest call on a platform reliability or security risk even when it is inconvenient to admit.** Scope: trust on one platform team.
- **M2** — Depth: Holds the ethical line on a critical platform where access, data, and reliability carry real stakes. **Refuses a shortcut that would trade user trust or safety for speed, and says why.** Scope: integrity on a critical platform team.
- **M3** — Depth: Sets the ethical and trust norms other platform leads adopt around access, data, and honest incident disclosure. **Establishes the do-the-right-thing expectations several teams now hold each other to.** Scope: integrity across a cross-team domain.
- **M4** — Depth: Builds the trust and integrity expectations a platform sub-org operates by, from privileged-access ethics to honest reporting. **Makes candid, blameless honesty the norm across the sub-org even when the news is bad.** Scope: integrity across a platform sub-org.
- **M5** — Depth: Drives the function's ethical posture on the outsized access and impact platform holds. **Sets the integrity standard leaders across the function are trusted to uphold.** Scope: ethics across the platform function.
- **M6** — Depth: Sets the org-wide expectation for how platform leadership stewards trust, access, and impact. **Pioneers an ethics model peer functions and the wider field reference.** Scope: org-wide integrity and trust.

## Sources

Each theory anchor listed once, with the competencies that cite it.

- **Schmidt & Hunter, selection-methods meta-analysis (1998)** — Hiring & selection.
- **Tuckman, Developmental Sequence in Small Groups (1965)** — Onboarding & team formation.
- **Whitmore, Coaching for Performance (1992); Google Project Oxygen** — Coaching & development.
- **Hewlett, Forget a Mentor, Find a Sponsor (2013)** — Career development & sponsorship.
- **Grove, High Output Management (1983)** — Performance management.
- **Edmondson, The Fearless Organization (2018); Project Aristotle** — Psychological safety & team health.
- **Deci & Ryan, Self-Determination Theory (2000); Herzberg (1968)** — Motivation, engagement & retention.
- **Perri, Escaping the Build Trap (2018); Skelton & Pais, Team Topologies (2019)** — Platform vision & roadmap.
- **Noda, Storey, Forsgren & Greiler, DevEx: What Actually Drives Productivity (ACM Queue, 2023)** — Internal user research & discovery.
- **Cagan, Inspired (2008)** — Platform value & business case.
- **Spotify Engineering, How We Use Golden Paths (2020)** — Golden paths & paved roads.
- **Bottcher, What I Talk About When I Talk About Platforms (martinfowler.com, 2018)** — Self-service & platform interfaces.
- **Winters, Manshreck & Wright, Software Engineering at Google (2020) - deprecation chapter** — Adoption & migration strategy.
- **CNCF TAG App Delivery, Platform Engineering Maturity Model (2023)** — Platform advocacy & enablement.
- **Beyer, Jones, Petoff & Murphy, Site Reliability Engineering (2016)** — Reliability, SLOs & error budgets.
- **PagerDuty, Incident Response Guide (2017); Allspaw, Blameless PostMortems (2012)** — Incident & operational-risk leadership.
- **Majors, Fong-Jones & Miranda, Observability Engineering (2022)** — Observability & health signals.
- **Beyer, Jones, Petoff & Murphy, Site Reliability Engineering (2016) - toil chapter** — Toil reduction & automation.
- **Gregg, Systems Performance (2nd ed., 2020)** — Capacity, performance & cost.
- **Conway (1968); Nygard, Documenting Architecture Decisions (2011)** — Platform architecture stewardship.
- **Humble & Farley, Continuous Delivery (2010)** — Engineering standards & quality.
- **Cunningham, The WyCash Portfolio Management System (1992)** — Technical debt & modernization.
- **Larson, An Elegant Puzzle (2019); Wardley Maps (2016)** — Technical strategy & investment.
- **Korn Ferry Leadership Architect (2014) - Financial Acumen** — Vendor & build/buy/adopt strategy.
- **OWASP, Application Security Verification Standard (v4, 2019)** — Secure-by-default platform & guardrails.
- **McConnell, Software Estimation (2006)** — Planning & estimation.
- **Reinertsen, The Principles of Product Development Flow (2009)** — Prioritization & trade-offs.
- **Brooks, The Mythical Man-Month (1975)** — Capacity & resource allocation.
- **Forsgren, Humble & Kim, Accelerate (2018)** — Predictable delivery & flow.
- **Forsgren, Humble & Kim, Accelerate (2018) - DORA four keys; SPACE (2021)** — Engineering metrics & delivery health.
- **Deming, Out of the Crisis (1986)** — Process & continuous improvement.
- **NIST Cybersecurity Framework (2014); PMI PMBOK (2021)** — Dependency & risk management.
- **Rumelt, Good Strategy Bad Strategy (2011)** — Strategy formulation.
- **Kotter, Leading Change (1996)** — Leading change & transformation.
- **Skelton & Pais, Team Topologies (2019); Conway (1968)** — Organizational & team design.
- **Duarte, HBR Guide to Persuasive Presentations (2012)** — Executive & stakeholder communication.
- **Freeman, Strategic Management: A Stakeholder Approach (1984)** — Stakeholder management & partnership.
- **Cohen & Bradford, Influence Without Authority (1989); Bungay, The Art of Action (2011)** — Cross-org influence & alignment.
- **Grove, High Output Management (1983); Drucker (1967)** — Managerial leverage & focus.
- **Marquet, Turn the Ship Around! (2012)** — Delegation & empowerment.
- **Eurich, Insight (2017); Lombardo & Eichinger (2000)** — Self-awareness & learning agility.
- **Loehr & Schwartz, The Power of Full Engagement (2003)** — Resilience & sustainable pace.
- **Kahneman, Thinking, Fast and Slow (2011)** — Decision-making under uncertainty.
- **Mayer, Davis & Schoorman (1995); ACM Code of Ethics (2018)** — Ethics, integrity & trust.
