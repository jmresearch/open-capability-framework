# Full Stack TypeScript Engineer — Canonical Career Ladder

## Calibration summary

- **Provenance:** canonical consolidation of five independent blind generations (runs fst-r1 … fst-r5, 158 source competencies) by **union, not intersection** — every genuinely distinct competency from any run survives; nothing was voted out. Semantic duplicates were merged into single canonical competencies (clearest name, strongest citable anchor, best observable cell content). Minted 2026-07-02.
- **Variant:** ic_technical (individual-contributor technical track).
- **Levels:** six, E1–E6 — Associate Full Stack Engineer → Full Stack Engineer → Senior Full Stack Engineer → Staff Full Stack Engineer → Senior Staff Full Stack Engineer → Principal Full Stack Engineer.
- **Scope bands:** task (E1) → component (E2) → capability/domain (E3) → multiple teams (E4) → organization (E5) → company (E6), following Google L3–L8 / Meta E3–E8 norms via levels.fyi, with StaffEng (Larson) grounding E4–E6 behaviors.
- **Terminal level: E3 / Senior.** All five runs agree: a strong full stack engineer can remain at E3 indefinitely without being "behind." E4+ is not "more of E3" — it is a different job defined by multi-team scope, influence without authority, and organizational leverage.
- **Register:** CircleCI Engineering Competency Matrix — present-tense observable behaviors; Depth and Scope separated in every cell.
- **Shape:** 8 key areas, 19 focus areas, 47 competencies; every focus area spans 2+ competencies; theme labels are under 60 characters and technology-agnostic where reasonable (TypeScript specifics live in the cell prose).
- **OCF mapping:** every competency carries an Open Capability Framework id on its `OCF:` line — 42 map to existing catalog capabilities; 5 are `proposed` (SWE-08 type-system domain modeling, SWE-09 boundary validation & type integrity, OPS-30 progressive delivery & release safety, PD-07 strategic & commercial awareness, and the pre-existing pending EM-15 technical debt & risk stewardship).
- **Consolidation judgment calls:** (1) The type system keeps first-class treatment (3 competencies) — all five runs independently gave it its own focus area. (2) Frontend and backend stay symmetric key areas; "full stack" is leveled as genuine competence on both sides plus the contracts between them. (3) Run-3's split of compatibility/versioning from API design survives (union rule) — full stack engineers own both sides of the client-server deploy-order problem. (4) Single-run competencies (styling, data fetching, messaging, runtime correctness, advanced types, threat modeling, quality ownership, decision-making, stakeholder communication, ownership, business outcomes) all survive as distinct rows. (5) Code review clusters with code health (a design-quality mechanism); interpersonal feedback clusters with teamwork. (6) Blended source rows (e.g. r4's "Code review & feedback", r3's "Continuous integration & release") were assigned to the concept their cell content leans toward.

## Level overview

| Level | Title | Scope band | Focus |
|---|---|---|---|
| E1 | Associate Full Stack Engineer | task | Ships well-defined tasks across the stack with guidance; learns the codebase, the stack, and the team's practices |
| E2 | Full Stack Engineer | component | Independently delivers complete features spanning UI, API, and data layers; owns components end to end |
| E3 | Senior Full Stack Engineer | capability / domain — **terminal level** | Owns a product capability across the stack; designs for evolution; sets the local bar through reviews and mentoring |
| E4 | Staff Full Stack Engineer | multiple teams | Drives cross-team technical direction; solves problems no single team can; multiplies other engineers |
| E5 | Senior Staff Full Stack Engineer | organization | Sets engineering standards and architecture the organization builds against; grows senior talent |
| E6 | Principal Full Stack Engineer | company | Shapes company-level technical strategy; represents engineering externally; makes bets that define the platform for years |

**Terminal level — E3 / Senior.** Sustained excellence at E3 is a complete, respected career, not a waypoint. Progression beyond E3 is opt-in and changes the nature of the job from building the thing to aligning the people and systems around the thing.

## Competency matrix

## Frontend Engineering

### UI Implementation

#### Component design & composition

*Anchor:* React documentation, "Thinking in React" (react.dev) — decomposing UI into a one-way data-flow component hierarchy is the canonical discipline for maintainable interfaces. *Why:* component boundaries are where frontend complexity is either contained or leaks. *OCF:* [FE-01](../../data/capabilities.md#fe-01) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Builds components from an existing design system to spec**, following the patterns in neighboring code and asking when a mockup is ambiguous. Scope: implements single components inside a feature someone else has decomposed.
- **E2:** Depth: **Decomposes a feature into a sensible component hierarchy without being handed the breakdown**, choosing props vs. composition deliberately and reusing shared components rather than forking them. Scope: owns the UI of a component or feature area end to end.
- **E3:** Depth: **Designs the component APIs a capability's UI is built from**, catching prop-drilling, leaky abstractions, and reuse-hostile boundaries in review before they ship, and extends the design system with primitives that get reused. Scope: owns UI architecture for a product capability; other engineers build within the structure they set.
- **E4:** Depth: **Establishes the shared component and design-system patterns several teams build against**, deprecating divergent one-offs with migration paths. Scope: UI conventions across multiple teams trace to structures they authored.
- **E5:** Depth: **Sets the organization's frontend architecture direction** — design-system governance, framework and rendering-model choices — and removes the systemic obstacles blocking it. Scope: org-wide UI platform.
- **E6:** Depth: **Makes the company-level frontend bets** (platform, framework generation, build-vs-buy for the design system) and is the named authority when they're contested. Scope: every product surface in the company.

#### Styling & responsive layout

*Anchor:* MDN Web Docs, CSS layout guides (Mozilla) — flexbox, grid, and cascade mechanics are the standard reference for predictable layout. *Why:* layout skill is the difference between UIs that match design at one width and UIs that hold up everywhere. *OCF:* [FE-09](../../data/capabilities.md#fe-09) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Implements designs to match mockups at standard breakpoints** using the project's styling approach; fixes visual bugs with guidance on cascade and specificity issues. Scope: assigned screens.
- **E2:** Depth: **Builds layouts that hold up across viewports and content lengths without per-case hacks**, choosing flexbox and grid appropriately and using design tokens consistently. Scope: the styling of features they own.
- **E3:** Depth: **Untangles specificity and layout problems others are stuck on** and establishes styling conventions (tokens, layering, theming) that keep the capability's CSS predictable. Scope: styling architecture for a capability.
- **E4:** Depth: **Consolidates styling approaches across teams into one system**, retiring duplicated patterns and writing the migration guide teams actually follow. Scope: multiple teams' styling stacks.
- **E5:** Depth: **Owns the org's theming and visual-consistency strategy**, deciding tooling and token architecture and measuring adoption. Scope: organization-wide.
- **E6:** Depth: **Directs company-level presentation-layer strategy**, including brand-scale theming, white-labeling, or multi-product visual platforms. Scope: company-wide.

### State & Data Flow

#### Client state management & data flow

*Anchor:* Redux documentation, "Three Principles" (redux.js.org) — single source of truth and unidirectional data flow are the reference discipline for predictable UIs. *Why:* most frontend defects are state-synchronization defects; how state is modeled determines whether the UI is debuggable. *OCF:* [FE-05](../../data/capabilities.md#fe-05) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Uses the codebase's existing state patterns correctly** — local state vs. shared store vs. server cache — and traces where a given piece of state lives and why. Scope: state within a single component or screen.
- **E2:** Depth: **Chooses the right home for each piece of state** (local, lifted, global, URL, server-cache) and keeps derived state computed rather than duplicated, with loading, error, and stale states honest in the UI. Scope: state design for the features they own.
- **E3:** Depth: **Designs the state architecture for a capability** — cache invalidation, optimistic updates, real-time sync — and spots stale-data, race-condition, and re-render-prone flows in others' code before they ship. Scope: state conventions for a capability; others copy their patterns.
- **E4:** Depth: **Converges divergent state approaches across teams into shared patterns**, writing the decision record and unwinding the worst legacy state tangles personally. Scope: shared data-flow architecture spanning multiple teams.
- **E5:** Depth: **Sets the org's client-data architecture** (caching strategy, offline posture, real-time sync) and arbitrates when teams' needs conflict. Scope: organization-wide.
- **E6:** Depth: **Owns the long-horizon client-data strategy** — the model the company's products converge on — and sponsors the platform work to get there. Scope: company-wide.

#### Data fetching & caching

*Anchor:* TanStack Query documentation (Tanner Linsley and maintainers) — server state as a cache with staleness, invalidation, and background refetch is the modern reference model for client data fetching. *Why:* fetching discipline determines perceived speed, correctness under concurrency, and backend load. *OCF:* [FE-06](../../data/capabilities.md#fe-06) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Fetches data through the codebase's established client and hooks** and renders loading and error states; reproduces a stale-data bug with guidance. Scope: assigned screens.
- **E2:** Depth: **Implements fetching with correct cache keys, invalidation, and race handling**, and handles pagination and optimistic updates using established patterns. Scope: data flow of features they own.
- **E3:** Depth: **Designs the fetching and caching strategy for a capability** — what is cached, for how long, and what invalidates it — and spots request waterfalls and N+1 patterns in review. Scope: capability-wide client data strategy.
- **E4:** Depth: **Standardizes data-access patterns across teams**, building or selecting the shared data layer and deprecating ad-hoc fetching. Scope: multiple teams' client data layers.
- **E5:** Depth: **Owns the org's client-server data strategy**, including SSR and streaming trade-offs and cache coherence across products. Scope: organization-wide.
- **E6:** Depth: **Sets company-level direction for how clients consume data at scale**, shaping platform investments and vendor-versus-build decisions. Scope: company-wide.

### Frontend Quality

#### Accessibility

*Anchor:* W3C WCAG 2.2 and the WAI-ARIA Authoring Practices — the normative standard and pattern library for accessible web interfaces. *Why:* accessibility is a legal and ethical floor that must be engineered in, not retrofitted. *OCF:* [FE-12](../../data/capabilities.md#fe-12) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Uses semantic HTML and design-system components rather than div soup**, and runs the team's accessibility checks before requesting review. Scope: the elements they touch.
- **E2:** Depth: **Builds keyboard-navigable, screen-reader-usable features** — focus management, labels, ARIA only where semantics fall short — verifying with assistive tech before merge. Scope: the features they own meet WCAG AA.
- **E3:** Depth: **Catches accessibility regressions in review that automated tools miss** (focus traps, reading order, announced state changes) and teaches the patterns that prevent them. Scope: the accessibility bar for a capability; the reviewer teams pull in.
- **E4:** Depth: **Builds accessibility into shared components and CI gates so teams inherit conformance by default**, and drives remediation across surfaces no one team owns. Scope: multiple teams.
- **E5:** Depth: **Owns the org's accessibility standard and audit posture**, reporting conformance to leadership and prioritizing systemic fixes. Scope: organization-wide.
- **E6:** Depth: **Sets company accessibility policy and represents it externally** (compliance commitments, procurement, public conformance statements). Scope: company-wide.

#### Web performance

*Anchor:* Google web.dev Core Web Vitals (LCP, INP, CLS) — the industry-standard user-centric performance metrics tied to real business outcomes. *Why:* frontend performance is a measured product property with direct conversion and retention impact, not a polish pass. *OCF:* [FE-13](../../data/capabilities.md#fe-13) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Reads a Lighthouse or devtools performance report and fixes the flagged issues in their task** — oversized images, blocking scripts, unnecessary re-renders — with guidance on trade-offs. Scope: the pages they touch.
- **E2:** Depth: **Keeps the features they ship within the team's performance budget**, profiling render and bundle cost before merge and lazy-loading what the critical path doesn't need. Scope: their components' contribution to page metrics.
- **E3:** Depth: **Owns Core Web Vitals for a capability**, diagnosing field regressions from RUM data to root cause — hydration cost, main-thread contention, layout shift — and rejecting designs that can't hit budget. Scope: a capability's user-facing performance; consulted by neighboring teams.
- **E4:** Depth: **Builds the performance budgets, CI gates, and monitoring several teams run on**, and leads the cross-team efforts that move p75 metrics. Scope: multiple teams.
- **E5:** Depth: **Sets org-wide performance targets and the platform investments to hit them** — rendering architecture, edge/CDN posture — tied to business metrics leadership acts on. Scope: organization-wide.
- **E6:** Depth: **Makes the company-level performance-architecture bets** and is accountable for user-experience speed as a competitive property of the product. Scope: company-wide.

## Backend & API Engineering

### Services & Runtime

#### Service design & boundaries

*Anchor:* Newman, Building Microservices, 2nd ed. (2021) — service boundaries follow domain seams, and coupling/cohesion trade-offs dominate distributed-system cost. *Why:* where the boundaries sit determines whether the backend evolves or ossifies. *OCF:* [ARC-02](../../data/capabilities.md#arc-02) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Adds endpoints and handlers to an existing Node/TypeScript service** following its layering, error-handling, and config conventions; explains the request path through the service in their own words. Scope: assigned tasks in one service.
- **E2:** Depth: **Designs and ships a well-factored module or small service independently**, separating transport, domain logic, and persistence, and handling errors, timeouts, and idempotency deliberately. Scope: a service component end to end.
- **E3:** Depth: **Draws service boundaries by trade-off in design docs that name the alternatives considered**, designing for failure (retries, idempotency, backpressure) and catching coupling and hidden-dependency problems in others' designs before build. Scope: owns the services behind a capability; runs its design reviews.
- **E4:** Depth: **Restructures the service landscape across teams** — splitting, merging, or extracting services with migration plans that ship incrementally — without stopping delivery. Scope: service architecture spanning multiple teams.
- **E5:** Depth: **Sets the org's service architecture direction** (runtime choices, communication patterns, platform primitives) and retires the patterns that no longer serve it. Scope: organization-wide.
- **E6:** Depth: **Makes company-level backend platform bets** and is the tie-breaking authority on architecture decisions with decade-scale consequences. Scope: company-wide.

#### Runtime & async correctness

*Anchor:* Node.js official guide, "Don't Block the Event Loop" — Node's single-threaded event loop makes blocking and unhandled-rejection bugs systemic. *Why:* full stack TypeScript engineers ship Node services whose failure modes are concurrency failure modes. *OCF:* [CS-04](../../data/capabilities.md#cs-04) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Uses async/await correctly** — awaits promises, handles rejections, avoids sequential awaits where work is parallel — with review catching the misses. Scope: assigned tasks.
- **E2:** Depth: **Keeps the event loop healthy in code they own**, moving CPU-heavy work off the hot path, bounding concurrency, and adding timeouts and cancellation to outbound calls. Scope: components they own.
- **E3:** Depth: **Diagnoses production event-loop stalls, memory leaks, and race conditions from traces and heap snapshots**, and designs backpressure and retry behavior for a capability's services. Scope: runtime health of a capability.
- **E4:** Depth: **Sets the concurrency, timeout, and resilience defaults multiple teams inherit** through shared libraries and service templates. Scope: multiple teams' services.
- **E5:** Depth: **Drives org-wide runtime strategy** — Node versions, worker models, resource limits — from fleet-level performance data. Scope: organization-wide.
- **E6:** Depth: **Owns company-level runtime and platform bets** and is the escalation point for the hardest production mysteries. Scope: company-wide.

### API Contracts

#### API contract design

*Anchor:* Fielding, "Architectural Styles and the Design of Network-based Software Architectures" (2000) and the OpenAPI Specification — resource-oriented contracts with explicit, machine-readable schemas are the durable basis for evolvable APIs. *Why:* the API contract is the seam where frontend and backend work meets; a bad one taxes every consumer forever. *OCF:* [SWE-07](../../data/capabilities.md#swe-07) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Implements endpoints against a specified contract**, returning correct status codes and error shapes, and updates the OpenAPI or schema definition alongside the code. Scope: assigned endpoints.
- **E2:** Depth: **Designs consistent, versionable endpoints for their feature** — naming, pagination, error envelopes — and shares typed clients or generated types so frontend and backend agree by construction. Scope: their component's API surface.
- **E3:** Depth: **Owns the API contract for a capability**, writing the schema first, folding consumers' integration pain back into the design, and rejecting designs in review that leak internals or paint consumers into corners. Scope: a capability's public contracts and their consumers.
- **E4:** Depth: **Sets the API conventions multiple teams follow** (style guide, error taxonomy, schema registry, review gates) and arbitrates contract disputes between producing and consuming teams. Scope: cross-team API governance.
- **E5:** Depth: **Owns the org's API strategy** — REST/GraphQL/RPC posture, gateway, contract-testing infrastructure — and its governance mechanisms. Scope: organization-wide.
- **E6:** Depth: **Shapes the company's external API as a product**, making the compatibility promises the business sells against. Scope: company-wide and partner ecosystem.

#### Compatibility & versioning

*Anchor:* Hyrum's Law (Winters, Manshreck & Wright, Software Engineering at Google, 2020) and Preston-Werner, Semantic Versioning — every observable behavior becomes a dependency. *Why:* full stack changes break real clients unless compatibility is engineered deliberately; the client-server deploy-order problem is owned on both sides by this role. *OCF:* [BE-13](../../data/capabilities.md#be-13) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Asks before changing a response shape or shared type**, and explains why deployed clients constrain the server. Scope: assigned changes.
- **E2:** Depth: **Ships additive, backward-compatible changes by default**, coordinating deploy order between client and server and gating risky changes behind flags. Scope: components they own.
- **E3:** Depth: **Designs the deprecation and migration paths for a capability's contracts** — versioning scheme, sunset timelines, consumer comms — and catches silent breaking changes in review. Scope: a capability's contract lifecycle; consumers trust their deprecation notes.
- **E4:** Depth: **Runs breaking-change processes across teams**, with contract tests and migration tooling that make deprecations routine rather than heroic. Scope: multiple teams' seams.
- **E5:** Depth: **Sets the org's compatibility policy** and the tooling that enforces it automatically. Scope: organization-wide.
- **E6:** Depth: **Owns compatibility strategy for company-critical and external surfaces**, where mistakes are front-page incidents. Scope: company-wide.

### Data & Persistence

#### Data modeling

*Anchor:* Kleppmann, Designing Data-Intensive Applications (2017) — schema design, consistency, and evolution determine what a system can ever safely do. *Why:* the schema outlives the code; modeling errors are the most expensive class of backend mistake. *OCF:* [BE-01](../../data/capabilities.md#be-01) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Writes correct queries and simple schema changes against an existing model**, explaining the main entities and their relationships in their own words. Scope: the data their task reads and writes.
- **E2:** Depth: **Designs sound schemas for their features** — keys, constraints, indexes, normalization judged by access pattern — encoding invariants in the database rather than in application hope, with reversible migrations. Scope: their component's data model.
- **E3:** Depth: **Models a capability's domain so that invalid states are hard to represent**, choosing consistency and transaction boundaries deliberately, designing for schema evolution, and catching modeling errors in others' designs before they calcify. Scope: the capability's data model; the person others consult before touching it.
- **E4:** Depth: **Untangles data models entangled across teams** — ownership of shared entities, duplication vs. reference, event contracts — and lands the migrations. Scope: data architecture spanning multiple teams.
- **E5:** Depth: **Sets the org's data architecture** (store selection, consistency posture, canonical sources of truth) and kills duplicate sources of truth. Scope: organization-wide.
- **E6:** Depth: **Owns company-level data strategy bets** — the storage and consistency platform products build on for years, including regulatory and multi-region posture. Scope: company-wide.

#### Query performance & safe migrations

*Anchor:* Winand, SQL Performance Explained / Use The Index, Luke — index design and execution-plan literacy is a developer responsibility, not a DBA afterthought; with Sadalage & Fowler, "Evolutionary Database Design" (martinfowler.com) for continuous, reversible schema change. *Why:* most production database pain is query-shaped and preventable at review time, and live-data migrations are where full stack changes carry irreversible risk. *OCF:* [BE-04](../../data/capabilities.md#be-04) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Reads a query plan with help and fixes flagged N+1s**, running schema changes only through the migration tooling with review. Scope: queries in their own changes.
- **E2:** Depth: **Reads execution plans unprompted and designs indexes for the access patterns of features they own**, checking query cost against realistic data volumes and rehearsing the rollback before deploying. Scope: their component's persistence layer.
- **E3:** Depth: **Diagnoses production database performance to root cause** — plans, locks, connection pools — and designs zero-downtime migrations (expand/contract, backfill strategy, dual-write windows), reviewing others' migrations for lock and rollback risk. Scope: the capability's database health; on-call escalation point.
- **E4:** Depth: **Leads the multi-team data moves** — resharding, datastore swaps, hot-table decomposition — with staged rollout plans others execute against, and builds the guardrails preventing recurrence. Scope: multiple teams' data stores.
- **E5:** Depth: **Owns org-level capacity and scaling strategy for persistence**, deciding when to shard, replicate, or re-platform, with cost explicitly in the trade-off. Scope: organization-wide.
- **E6:** Depth: **Makes the company's long-horizon storage bets** and is the final technical voice on the migrations where failure is existential. Scope: company-wide.

### Integration & Resilience

#### Asynchronous processing & messaging

*Anchor:* Hohpe & Woolf, Enterprise Integration Patterns (2003) — the canonical pattern language for queues, events, and message reliability. *Why:* async work is where correctness quietly breaks; ordering, retries, and duplicates need designed answers. *OCF:* [BE-09](../../data/capabilities.md#be-09) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Adds jobs or event handlers to an existing queue and worker setup** following team patterns; explains at-least-once delivery and why handlers must tolerate retries. Scope: assigned tasks.
- **E2:** Depth: **Builds idempotent async workflows** with dead-letter handling and visibility into failures; chooses sync-versus-async deliberately for their feature. Scope: their component's async work.
- **E3:** Depth: **Designs the event and job architecture for a capability**, reasoning explicitly about ordering, exactly-once illusions, and poison messages, and catches these gaps in others' designs. Scope: capability-wide async architecture.
- **E4:** Depth: **Standardizes messaging patterns across teams**, owning shared schemas and topics and the contract between producers and consumers. Scope: multi-team eventing.
- **E5:** Depth: **Sets the org's async and eventing strategy**, including platform selection and the delivery-guarantee posture teams inherit. Scope: organization-wide.
- **E6:** Depth: **Directs company-scale event architecture**, making the platform bets that determine how the company's systems compose. Scope: company-wide.

#### Third-party & cross-service resilience

*Anchor:* Nygard, Release It!, 2nd ed. (2018) — timeouts, circuit breakers, and bulkheads as the stability patterns for systems that depend on other systems. *Why:* systems fail at their integration points; resilience is designed in, observably, before the incident. *OCF:* [BE-18](../../data/capabilities.md#be-18) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Sets timeouts and handles error paths in their changes as the team's patterns prescribe**, and explains what happens to their code when a dependency is down. Scope: failure handling in their tasks.
- **E2:** Depth: **Wraps every external dependency with timeouts, retries with backoff, and failure fallbacks** — graceful degradation in the UI when the API stutters — and writes the runbook entry for when the dependency degrades. Scope: resilience of components they own.
- **E3:** Depth: **Designs the resilience posture for a capability** — circuit breakers, bulkheads, dependency criticality tiers, load-testing before launches and sizing for projected growth — and rejects designs in review that fail closed on non-critical dependencies. Scope: a capability's stability under stress.
- **E4:** Depth: **Hardens the seams between teams' systems** — shared dependencies, cascading-failure paths — running failure-injection and game-day exercises and fixing the systemic weak points they expose. Scope: multiple teams' dependency graph.
- **E5:** Depth: **Sets org resilience standards and capacity strategy**, including vendor criticality tiers, exit strategies, and disaster-recovery posture. Scope: organization-wide.
- **E6:** Depth: **Accountable for company-level systemic resilience**, shaping architecture and vendor strategy so no single dependency can take the business down. Scope: company-wide.

## TypeScript & Software Design

### Type System as a Design Tool

#### Type-driven domain modeling

*Anchor:* Vanderkam, Effective TypeScript, 2nd ed. (2024) — "prefer types that always represent valid states"; the type system is a design tool, not annotation. With Wlaschin, Domain Modeling Made Functional (2018) for making illegal states unrepresentable. *Why:* in a TypeScript-centered stack, the type system is the cheapest place to delete whole defect classes before runtime. *OCF:* [proposed](../../contrib/2026-07-type-system-domain-modeling.md) (SWE-08 candidate) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Writes correctly typed code without resorting to `any`**, using the codebase's interfaces, unions, and generics correctly and reading compiler errors to the actual cause. Scope: their own tasks compile clean under strict mode.
- **E2:** Depth: **Models feature domains so invalid states don't type-check** — discriminated unions over boolean flags, literal types over strings, narrowing over assertions. Scope: the types of components they own.
- **E3:** Depth: **Designs the shared domain types a capability is built on**, using generics and inference so call sites stay simple, judging when type-level sophistication pays and when it obscures, and unwinding `any`-creep others have accumulated. Scope: the capability's type architecture; the review stop for tricky types.
- **E4:** Depth: **Sets type-design conventions multiple teams adopt** — branded IDs, result types, strictness policy, shared type libraries — and leads the migrations that raise strictness without halting delivery. Scope: multiple teams' shared type infrastructure.
- **E5:** Depth: **Owns the org's TypeScript platform posture** — compiler-option baselines, monorepo type architecture, upgrade cadence — measured by defect and velocity outcomes. Scope: organization-wide.
- **E6:** Depth: **Makes the company's language and type-platform bets** and represents the company's practice in the external TypeScript community. Scope: company-wide.

#### Type safety at boundaries

*Anchor:* King, "Parse, Don't Validate" (2019) — validate untrusted data into precise types at the boundary once, then rely on the types; with Vanderkam, Effective TypeScript, 2nd ed. (2024) on reconstructing types at runtime. *Why:* full stack TypeScript's distinctive promise — one type system spanning client, server, and wire — is only real if network, storage, and third-party boundaries are actually validated. *OCF:* [proposed](../../contrib/2026-07-boundary-validation-type-integrity.md) (SWE-09 candidate) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Uses the codebase's shared API types and schema validators at boundaries** rather than hand-casting responses, and explains why an `as` cast is a smell. Scope: the boundaries their task crosses.
- **E2:** Depth: **Puts runtime validation at every I/O boundary they touch** — requests, webhooks, queue messages, env config — deriving static types from the schemas so runtime and compile time can't drift. Scope: their features' edges.
- **E3:** Depth: **Designs end-to-end type safety for a capability** — shared contract types or clients generated from schema, contract drift caught in CI — so a server change breaks the client build, not production; flags unsound casts and unvalidated edges in review as blocking. Scope: the capability's inbound and outbound contracts; teams copy their setup.
- **E4:** Depth: **Builds the codegen and contract-typing infrastructure multiple teams inherit**, making boundary safety the default rather than a discipline, and resolves cross-team type drift at its source. Scope: multiple teams.
- **E5:** Depth: **Sets the org's boundary-safety standard and the platform tooling that enforces it**, with incident data showing the failure classes it removed. Scope: organization-wide.
- **E6:** Depth: **Owns the company's contract-integrity strategy** including partner and public-API boundaries where a break is a business event. Scope: company-wide.

#### Advanced types & inference

*Anchor:* The TypeScript Handbook (Microsoft TypeScript team) — generics, conditional and mapped types, and inference behavior as documented by the language team. *Why:* advanced types are leverage; one well-typed utility eliminates whole classes of caller mistakes. *OCF:* [SWE-01](../../data/capabilities.md#swe-01) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Uses generic functions and utility types (Pick, Omit, Partial) correctly** in everyday code; asks for help when inference surprises them. Scope: assigned tasks.
- **E2:** Depth: **Writes their own generic functions and constraints that infer cleanly at call sites**, and debugs inference failures by reading the types rather than adding casts. Scope: their component.
- **E3:** Depth: **Builds the typed utilities and library boundaries others rely on** — mapped and conditional types where they pay for themselves — and pushes back in review on cleverness that hurts readability or compile times. Scope: capability-wide shared code.
- **E4:** Depth: **Owns the hardest type-level infrastructure across teams** (codegen, typed clients, framework glue) and teaches the patterns so they don't bottleneck on one person. Scope: multiple teams.
- **E5:** Depth: **Sets the org's bar for type-level engineering**, balancing expressiveness against build performance and onboarding cost. Scope: organization-wide.
- **E6:** Depth: **Influences the practice beyond the company** — upstream contributions, published patterns — and directs internal investment accordingly. Scope: company-wide and industry.

### Architecture & Code Health

#### Software design & architecture

*Anchor:* Ousterhout, A Philosophy of Software Design (2018) — complexity is incremental and the designer's job is deep modules and information hiding; with Parnas (1972) on decomposing around what will change. *Why:* design quality determines the cost of every future change. *OCF:* [SWE-05](../../data/capabilities.md#swe-05) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Explains the system's architecture in their own words** and navigates its diagrams to find where a change belongs, implementing designs specified by others. Scope: implements within a given design.
- **E2:** Depth: **Designs their features within the existing architecture with clear module boundaries and hidden internals**, writing a short design note for anything non-obvious and naming at least one alternative. Scope: design of their component.
- **E3:** Depth: **Selects patterns by trade-off in design docs that name the alternatives considered**, designs for evolution, and catches coupling and scaling problems in others' designs before build. Scope: owns architecture for a capability; runs its design reviews.
- **E4:** Depth: **Produces the designs that resolve problems spanning multiple teams**, and gets them adopted through review and persuasion rather than mandate. Scope: multi-team architecture.
- **E5:** Depth: **Sets the architectural direction multiple teams build against** and removes the systemic obstacles that block it. Scope: organization-wide.
- **E6:** Depth: **Owns the company's technical architecture narrative** — where the platform is going and why — making the irreversible calls and being publicly accountable for them. Scope: company-wide.

#### Readable, maintainable code

*Anchor:* Fowler, Refactoring, 2nd ed. (2018, JavaScript examples) — code smells and behavior-preserving transformation as the working definition of maintainability. *Why:* code is read far more than written, and full stack code is read by people who don't live in that half of the stack. *OCF:* [SWE-02](../../data/capabilities.md#swe-02) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Writes small, clearly named functions that match the codebase's conventions**, and incorporates review feedback without repeating the same class of issue. Scope: assigned tasks.
- **E2:** Depth: **Leaves code simpler than found as a matter of course** — refactors as part of feature work, keeps modules cohesive, writes comments that explain why, not what; review comments on their PRs trend toward design, not cleanup. Scope: components they own.
- **E3:** Depth: **Sets the maintainability bar for a capability through review** — names the smell and the refactoring, suggests the simplification rather than the workaround, and articulates why a design is too complicated, not just that it is. Scope: a capability's codebase health.
- **E4:** Depth: **Drives code-health initiatives across teams** — dead-code deletion, module restructuring, convention alignment — with before/after evidence. Scope: multiple teams' codebases.
- **E5:** Depth: **Owns org-level code-health strategy**, making maintainability a funded, tracked property rather than a virtue, legible to leadership as risk and velocity. Scope: organization-wide.
- **E6:** Depth: **Sets company engineering-quality standards** and models them in the code they still write. Scope: company-wide.

#### Refactoring & technical debt

*Anchor:* Fowler, Refactoring, 2nd ed. (2018) and Cunningham's debt metaphor (OOPSLA 1992) — behavior-preserving transformation in small steps, and debt as a deliberate, tracked trade-off. *Why:* codebases rot by default; deliberate, safe restructuring is what keeps change cheap. *OCF:* [proposed](../../contrib/2026-07-technical-debt-stewardship.md) (EM-15 candidate) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Leaves touched code cleaner than found within the task's footprint** — naming, dead code, small extractions under existing tests — and flags debt they notice rather than working around it silently. Scope: their own diffs.
- **E2:** Depth: **Refactors opportunistically within features and structures larger changes as reviewable, behavior-preserving steps**, recording debt they take on with the reason and the exit path. Scope: the health of their component.
- **E3:** Depth: **Plans and lands multi-week refactors of a capability without stopping feature delivery**, choosing strangler-style migrations over rewrites, and maintains a costed debt register — distinguishing debt that compounds from debt that can sit — with priorities stakeholders accept. Scope: a capability's long-term structural health.
- **E4:** Depth: **Leads the cross-team refactors and deprecations no single team can justify alone**, with migration tooling that makes following cheap. Scope: multiple teams' codebases.
- **E5:** Depth: **Owns the org's code-health investment strategy** — what gets modernized, deleted, or frozen — and reports the return in delivery terms. Scope: organization-wide.
- **E6:** Depth: **Decides the company's platform modernization bets** (rewrite vs. strangle vs. sunset) with company-level cost consequences. Scope: company-wide.

#### Code review practice

*Anchor:* Winters, Manshreck & Wright, Software Engineering at Google (2020), code-review chapters — review as the primary mechanism for knowledge transfer and a shared quality bar. *Why:* review is where a team's actual standards live, whatever the wiki says. *OCF:* [SWE-04](../../data/capabilities.md#swe-04) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Responds to review feedback promptly and without defensiveness**, applies it beyond the flagged line, and reviews small changes for readability and test presence. Scope: their own PRs plus starter reviews.
- **E2:** Depth: **Gives reviews that catch real defects, not just style** — edge cases, type holes, missing tests — distinguishing blocking issues from preferences and phrasing comments about the code, not the coder. Scope: dependable reviewer for their component.
- **E3:** Depth: **Reviews for design, failure modes, and long-term cost — and teaches through review comments others save and share.** Turns recurring review comments into lint rules or docs, and calibrates comment severity so authors know what blocks. Scope: the review bar for a capability; the requested reviewer for hard changes.
- **E4:** Depth: **Calibrates review standards across teams** so the bar is consistent, reviewing the cross-cutting changes nobody else can judge and coaching senior engineers on how they review. Scope: multiple teams' review culture.
- **E5:** Depth: **Designs the org's review system itself** — ownership rules, required checks, review SLAs, automation — measured by defect escape and flow metrics. Scope: organization-wide.
- **E6:** Depth: **Sets the company's engineering-rigor expectations**, personally reviewing the changes with company-level blast radius. Scope: company-wide.

## Quality & Testing

### Testing Across the Stack

#### Test strategy & the pyramid

*Anchor:* Cohn's test pyramid (Succeeding with Agile, 2009) as refined by Vocke, "The Practical Test Pyramid" (martinfowler.com, 2018) — push tests down to the cheapest layer that gives the needed confidence. *Why:* full stack code fails at the seams; test-suite shape decides whether the suite is a safety net or a tax. *OCF:* [QA-01](../../data/capabilities.md#qa-01) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Writes unit tests for every change following the team's patterns**, and explains what each layer of the pyramid is for in their own words. Scope: coverage of their own tasks.
- **E2:** Depth: **Chooses the right test layer per risk** — unit for logic, integration for seams, few end-to-end — covering the frontend, API, and data layers rather than just the easiest one. Scope: test strategy for their component.
- **E3:** Depth: **Owns the test strategy for a capability and kills tests that cost more than they catch**, rebalancing an inverted pyramid, deciding coverage targets by risk, and defining which user journeys warrant end-to-end coverage — with the data to justify it. Scope: the capability's confidence posture; consulted on what to test where.
- **E4:** Depth: **Aligns test strategy across teams that share seams** — contract tests where E2E suites were the crutch, shared fixtures, flake budgets — so cross-team changes are safe to make. Scope: multiple teams' suites.
- **E5:** Depth: **Sets the organization's testing standards and investment level**, backed by data on escape rates and suite cost. Scope: organization-wide.
- **E6:** Depth: **Owns the company's release-confidence posture**, deciding the quality bar that ships and answering for it when it fails. Scope: company-wide.

#### Test authoring & implementation quality

*Anchor:* Dodds, "Write tests. Not too many. Mostly integration." and the Testing Library guiding principles — test behavior through the interface the user sees, not internals; with Meszaros, xUnit Test Patterns (2007) on test code as designed code. *Why:* tests coupled to implementation punish refactoring; tests coupled to behavior enable it. *OCF:* [SWE-03](../../data/capabilities.md#swe-03) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Writes readable arrange-act-assert tests that assert behavior, not implementation**, using the team's harnesses correctly and fixing a failing test by understanding it rather than snapshot-updating past it. Scope: tests within their tasks.
- **E2:** Depth: **Writes tests that survive refactoring** — queries UI the way a user would, isolates external systems with typed fakes at the right boundary, covers error paths and keeps tests deterministic. Scope: their component's suites stay green and fast.
- **E3:** Depth: **Builds the test infrastructure others write tests with** — factories, fixtures, network mocking — making good tests the path of least resistance, and diagnoses the deep flake causes (async races, shared state, clock) to root cause. Scope: test tooling for a capability; the person paged when the suite lies.
- **E4:** Depth: **Fixes the systemic testing problems across teams** — flake sources, slow suites, mock sprawl — providing shared harnesses and coaching teams out of brittle-test patterns. Scope: multiple teams.
- **E5:** Depth: **Sets org-wide test-authoring standards and the tooling that enforces them**, keeping suite runtime and reliability inside explicit budgets. Scope: organization-wide.
- **E6:** Depth: **Directs company-level test-infrastructure investment** as a productivity multiplier, with authored practice visible in the highest-stakes systems. Scope: company-wide.

#### Integration & end-to-end confidence

*Anchor:* Fowler, "ContractTest" and consumer-driven contracts (martinfowler.com; Pact) — verify integrations at the contract, reserve E2E for critical journeys; with Playwright's testing best practices for flake control. *Why:* the highest-value bugs live at the seams between frontend and backend; those seams are this role's to verify. *OCF:* [QA-06](../../data/capabilities.md#qa-06) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Runs the end-to-end suite locally and reads its failures to the failing step**, updating existing journey tests when their change breaks one, with guidance. Scope: tests for their task.
- **E2:** Depth: **Writes stable integration and end-to-end tests for their features' critical paths** — user-facing selectors, controlled test data, no arbitrary sleeps — and quarantines flake rather than retrying it blind. Scope: their features' journeys.
- **E3:** Depth: **Decides what a capability verifies at which layer** — contract tests at API seams, a thin E2E set for revenue paths — keeping the suite's runtime and flake rate inside budget. Scope: a capability's integration confidence.
- **E4:** Depth: **Establishes contract-testing and integration infrastructure across team boundaries** — environments, seeded data, contract-test governance — so teams deploy independently without integration freezes. Scope: multiple teams' seams.
- **E5:** Depth: **Owns the org's pre-production confidence strategy**, deciding the environment topology and what may only be verified in production behind flags. Scope: organization-wide.
- **E6:** Depth: **Accountable for company-level release-confidence architecture**, including the economics of environments versus production-testing investment. Scope: company-wide.

### Defect Response & Prevention

#### Debugging & root-cause analysis

*Anchor:* Zeller, Why Programs Fail: A Guide to Systematic Debugging (2009) — debugging as hypothesis-driven search, not guesswork. *Why:* full stack defects cross two runtimes and every process boundary; systematic isolation is what keeps them tractable. *OCF:* [SWE-06](../../data/capabilities.md#swe-06) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Reproduces a bug reliably before changing code**, isolating with logs, breakpoints, and browser devtools in either runtime, and asks for help with a written summary of what's ruled out. Scope: defects in their own changes.
- **E2:** Depth: **Traces defects across the stack unaided** — UI symptom to network to service to query — stating a hypothesis before each experiment and using profilers to find hot paths instead of guessing. Scope: their component, wherever the cause lives.
- **E3:** Depth: **Is the debugger of last resort for a capability**, cracking the intermittent, race-condition, and heisenbug class from heap snapshots, CPU profiles, and traces, and turns each root cause into a regression test and a prevention. Scope: the capability's hardest defects; others bring them the hard ones.
- **E4:** Depth: **Leads cross-team investigations where no single team can see the whole failure**, building or standardizing the diagnostic tooling that shortens everyone's time-to-cause, and teaches the method while doing it. Scope: multiple teams' systems.
- **E5:** Depth: **Raises the organization's debugging capability** — runbooks, tooling, teaching — so hard problems stop requiring them personally. Scope: organization-wide.
- **E6:** Depth: **Handles the company-critical unknowns** — the defects with existential stakes — and grows the org's capacity to handle the next one without them. Scope: company-wide.

#### Quality ownership & prevention

*Anchor:* DORA / Forsgren, Humble & Kim, Accelerate (2018) — change failure rate and MTTR are outcomes of engineering practice, not QA headcount. *Why:* in a full stack team, quality is built in by the people who ship, or not at all. *OCF:* [QA-14](../../data/capabilities.md#qa-14) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Verifies their own work before review** — runs it, tests the unhappy paths, checks the acceptance criteria — rather than relying on reviewers to catch problems. Scope: their tasks.
- **E2:** Depth: **Monitors their changes after deploy** and fixes what they broke without being asked, tracking their defects to closure. Scope: their features in production.
- **E3:** Depth: **Owns a capability's quality metrics** — escaped defects, change failure rate — and changes the process, not just the code, when they slip. Scope: a capability's quality bar.
- **E4:** Depth: **Builds the quality gates and review standards several teams operate**, and intervenes with data when a team's failure rate drifts. Scope: multiple teams.
- **E5:** Depth: **Owns org-level quality outcomes**, reporting DORA-style metrics to leadership and directing the practice changes they imply. Scope: organization-wide.
- **E6:** Depth: **Sets the company's quality-vs-speed posture** and is answerable for it in front of customers. Scope: company-wide.

## Delivery & Operations

### Delivery Pipeline

#### Build & CI pipelines

*Anchor:* Forsgren, Humble & Kim, Accelerate (2018) / DORA — continuous integration and trunk-based practices predict both throughput and stability. *Why:* the pipeline is the rate limiter on everything else an engineering team does. *OCF:* [OPS-02](../../data/capabilities.md#ops-02) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Keeps their branch green** — reads CI failures to the root cause, reproduces them locally, and fixes them before asking for review; never merges on red. Scope: their own changes through the pipeline.
- **E2:** Depth: **Integrates small and often and fixes pipeline config for their area** — adds checks, caches dependencies, parallelizes slow stages — treating a broken main build as their interrupt. Scope: their component's pipeline health.
- **E3:** Depth: **Owns pipeline health for a capability and keeps it fast** — build times within budget, flakes quarantined with follow-through, gating on the checks that matter (types, lint, tests, bundle size) — treating a slow pipeline as an incident, not a fact of life. Scope: the capability's build/CI; consulted on pipeline design.
- **E4:** Depth: **Builds or overhauls the shared build platform** (monorepo task graphs, remote caching, merge queues, affected-only builds) that keeps CI fast for many teams at once, measurably improving their lead time. Scope: multiple teams' delivery speed.
- **E5:** Depth: **Owns the org's delivery metrics and pipeline strategy**, reporting DORA-style measures to leadership and directing investment at the biggest bottleneck. Scope: organization-wide.
- **E6:** Depth: **Sets company delivery strategy** — build-vs-buy on CI, engineering-productivity investment — with the business case attached. Scope: company-wide.

#### Release & deployment practices

*Anchor:* Humble & Farley, Continuous Delivery (2010) — small, frequent, automated, reversible releases; decoupling deploy from release. *Why:* how software reaches production determines the blast radius of every mistake. *OCF:* [proposed](../../contrib/2026-07-progressive-delivery-release-safety.md) (OPS-30 candidate) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Follows the release process exactly** — feature flags, staged rollout steps, verification checklists — and watches their change land in production, rolling back with guidance when needed. Scope: their own deploys.
- **E2:** Depth: **Ships behind feature flags with a rollback plan by default**, monitors the rollout dashboards, rolls back on their own judgment when signals degrade, and writes migrations that tolerate both code versions running. Scope: releases of their component.
- **E3:** Depth: **Designs the rollout for risky changes** — canary and progressive rollout criteria, migration sequencing, flag lifecycle, kill switches — and reviews others' rollout plans for blast radius; the person teams ask "how do we ship this safely?" Scope: release safety for a capability.
- **E4:** Depth: **Builds progressive-delivery machinery multiple teams release through** (flag platform, automated canary analysis, automated rollback), retiring the deploy patterns that cause repeat incidents and raising deploy frequency measurably. Scope: multiple teams.
- **E5:** Depth: **Owns org release policy and its DORA metrics** — freeze rules, rollout standards, environment strategy — and dismantles the process that adds ceremony without safety. Scope: organization-wide.
- **E6:** Depth: **Sets company policy for how software reaches customers** — the risk posture products ship under — and defends it to executives, auditors, and regulators. Scope: company-wide.

#### Developer tooling & environment

*Anchor:* Winters, Manshreck & Wright, Software Engineering at Google (2020) — engineering productivity is an engineered system; tooling and fast feedback loops compound. *Why:* on a TypeScript monorepo/stack, build config, typecheck times, and dependency drift silently tax every engineer daily. *OCF:* [OPS-27](../../data/capabilities.md#ops-27) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Sets up and operates the local dev environment from the docs**, fixing their own environment problems before escalating and filing reproducible reports when tooling breaks. Scope: their own workflow.
- **E2:** Depth: **Improves the tooling friction they personally hit** — a slow build, a missing lint rule, a stale README, a tsconfig fix — and upstreams the fix instead of working around it, upgrading dependencies safely with changelogs read before major bumps. Scope: their team's inner loop.
- **E3:** Depth: **Owns the developer experience of a capability's codebase** — TS project references, bundler config, CI caching, lint/format automation, upgrade cadence — measuring dev-loop time before and after changes; new engineers ship in days because of it. Scope: a capability's toolchain.
- **E4:** Depth: **Designs the monorepo and shared-tooling layer multiple teams work inside**, landing the risky upgrades (TypeScript majors, bundler swaps) with codemods and migration docs, and measures adoption rather than assuming it. Scope: multiple teams' toolchain.
- **E5:** Depth: **Drives org developer-productivity strategy** with survey and telemetry data, owning the platform roadmap and its DX metrics. Scope: organization-wide.
- **E6:** Depth: **Makes the company's foundational tooling bets** (build systems, repo topology, language and runtime upgrades, AI-assisted development posture). Scope: company-wide.

### Production Operations

#### Observability & monitoring

*Anchor:* Beyer et al., Site Reliability Engineering (Google, 2016) — golden signals and SLO-based, symptom-driven alerting; with Majors, Fons-Jones & Miranda, Observability Engineering (2022) for high-cardinality tracing. *Why:* you can only operate what you can see, across browser and server alike — and the instrumentation is written by the engineers who ship the code. *OCF:* [OPS-05](../../data/capabilities.md#ops-05) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Finds their change's logs, metrics, traces, and browser error reports in the standard dashboards**, and adds structured log lines with useful context per team conventions. Scope: observability of their own changes.
- **E2:** Depth: **Instruments their features across the stack before shipping** — structured logs, metrics, trace spans that cross the client/server boundary — and answers "is it working?" from telemetry, not vibes. Scope: their component is debuggable from telemetry alone.
- **E3:** Depth: **Defines the SLIs/SLOs for a capability and builds alerts on symptoms, not causes** — dashboards on-call actually uses — deleting noisy alerts as deliberately as adding signal, and rejects unobservable designs in review. Scope: the capability's observability posture; the person who makes outages diagnosable.
- **E4:** Depth: **Standardizes observability across teams** — shared instrumentation libraries, trace propagation, log schema, alert-quality reviews — so cross-team incidents are traceable end to end, with measured pager-load reductions. Scope: multiple teams.
- **E5:** Depth: **Owns the org's observability strategy and SLO program**, including its cost curve, making reliability legible to leadership. Scope: organization-wide.
- **E6:** Depth: **Sets company reliability-measurement standards** and the external commitments (SLAs) grounded in them, answering for the telemetry bill and its value. Scope: company-wide.

#### Incident response & postmortems

*Anchor:* Beyer et al., Site Reliability Engineering (Google, 2016), incident-management and blameless-postmortem chapters; Allspaw's blameless-postmortem practice (Etsy, 2012). *Why:* incident behavior under pressure and honest learning afterward are where operational maturity is visible. *OCF:* [OPS-06](../../data/capabilities.md#ops-06) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Follows the runbook during incidents, escalates early with a clear symptom report, and narrates what they see** in the incident channel rather than debugging silently; contributes accurate timelines to postmortems while shadowing on-call. Scope: assists on incidents touching their tasks.
- **E2:** Depth: **Takes on-call for their component and mitigates common failures unaided**, prioritizing user impact over root cause in the moment, communicating status on the expected cadence, and writing postmortems that name contributing causes, not culprits. Scope: first responder for their component.
- **E3:** Depth: **Runs incident command for a capability's severe incidents** — coordinates responders, makes the mitigate-vs-diagnose call under pressure, communicates to stakeholders in their language — and drives postmortem actions to actual completion, not just filed. Scope: incident leadership for a capability; the calm one on the bridge.
- **E4:** Depth: **Commands incidents that cross team boundaries** and fixes the systemic reliability problems recurring across teams' postmortems, coaching new incident commanders and upgrading the practice itself (severity taxonomy, review quality, on-call health). Scope: multi-team incidents and follow-through.
- **E5:** Depth: **Owns the org's incident program and learning loop** — readiness, postmortem culture, error-budget policy — reviewing severity trends with leadership and directing reliability investment. Scope: organization-wide.
- **E6:** Depth: **Is accountable for company-level major-incident handling**, including executive and customer communication and the credibility of the postmortem process after the worst days. Scope: company-wide.

## Security

### Application Security

#### Secure coding & vulnerability prevention

*Anchor:* OWASP Top 10 (2021) and the OWASP Cheat Sheet Series — the consensus taxonomy of web application risk and its concrete countermeasures. *Why:* a full stack engineer owns the two most attacked surfaces — the browser (XSS, CSP, session state) and the API (injection, SSRF) — and every layer between. *OCF:* [OPS-08](../../data/capabilities.md#ops-08) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Uses the framework's safe defaults and never bypasses them** — parameterized queries, escaping-by-default templates, no unreviewed `dangerouslySetInnerHTML`, no secrets in code, logs, or client bundles — and names the OWASP Top 10 risks their change touches. Scope: their own changes.
- **E2:** Depth: **Prevents the common vulnerability classes by construction** — XSS, injection, CSRF, SSRF — validating input at trust boundaries with schemas, handling tokens and cookies correctly (HttpOnly/SameSite), and fixing scanner findings without being chased. Scope: their component's attack surface.
- **E3:** Depth: **Catches vulnerabilities in review that scanners miss** — authz gaps, unsafe deserialization, SSRF paths, XSS-shaped patterns — turning each finding into a guardrail (lint rule, safe wrapper, doc), and owns the capability's browser-side posture (CSP, third-party script trust, session architecture). Scope: the security bar for a capability; the pre-review security teams ask for.
- **E4:** Depth: **Builds secure-by-default platform pieces multiple teams inherit** (auth libraries, CSP baselines, input-validation layers, paved-path middleware) and drives remediation campaigns across codebases when pentests find systemic issues. Scope: multiple teams.
- **E5:** Depth: **Sets the org's secure-development standard with the security function** — standards, training, tooling, review gates — reporting measurable risk posture to leadership. Scope: organization-wide.
- **E6:** Depth: **Owns company product-security strategy from the engineering side**, accountable in audits, incidents, and board-level risk conversations. Scope: company-wide.

#### Authentication, authorization & data protection

*Anchor:* OWASP Application Security Verification Standard (ASVS 4.0) and NIST SP 800-63 Digital Identity Guidelines — verifiable requirements for session, identity, and access control. *Why:* broken access control is OWASP's #1 category, it is designed in rather than patched in, and the authorization logic is written by product engineers. *OCF:* [BE-15](../../data/capabilities.md#be-15) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Uses the existing auth middleware and permission checks correctly**, never rolling their own crypto or token handling, and checks authorization on the server, never only in the UI. Scope: the auth touchpoints of their tasks.
- **E2:** Depth: **Implements authorization server-side on every path the UI hides** — object-level, not just route-level — tests the negative cases (wrong user, expired session, escalation attempts), and handles tokens, sessions, secrets, and PII per policy without reminders. Scope: access control in components they own.
- **E3:** Depth: **Designs the access-control model for a capability** — roles, resource ownership, tenant isolation, audit trails — documents it, and probes designs for privilege-escalation and data-exposure paths before build; others bring their authorization edge cases to this person. Scope: the capability's identity and data-protection design; the reviewer for permission changes.
- **E4:** Depth: **Owns shared identity and authorization infrastructure multiple teams build on** (session services, permission frameworks, SSO integration) and leads migrations off legacy schemes without lockouts. Scope: multiple teams.
- **E5:** Depth: **Sets the org's identity, access, and data-protection architecture**, treating compliance regimes as engineering requirements and verifying enforcement holds in practice. Scope: organization-wide.
- **E6:** Depth: **Makes company-level trust-architecture bets** (identity platform, encryption posture, data-residency design) and stands behind them with regulators and enterprise customers. Scope: company-wide.

#### Threat modeling & security review

*Anchor:* Shostack, Threat Modeling: Designing for Security (2014) — "what are we building, what can go wrong, what do we do about it" as a design-time discipline. *Why:* the cheapest vulnerability to fix is the one caught in design. *OCF:* [SEC-05](../../data/capabilities.md#sec-05) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Answers "what could go wrong here?" about their change when asked**, and flags anything touching auth, money, or PII for extra review. Scope: assigned tasks.
- **E2:** Depth: **Raises abuse cases in design discussions unprompted** — enumeration, replay, object-level access mistakes — for features they own. Scope: components they own.
- **E3:** Depth: **Runs lightweight threat models for a capability's significant designs**, records the accepted risks, and makes security review a standing part of its design process. Scope: a capability's designs.
- **E4:** Depth: **Facilitates threat modeling across teams and trains engineers to run their own**, focusing effort on the highest-value targets. Scope: multiple teams' design practice.
- **E5:** Depth: **Owns the org's security-review program and risk register**, deciding where scrutiny concentrates. Scope: organization-wide.
- **E6:** Depth: **Shapes company security posture with threat-informed strategy** presented at the executive level. Scope: company-wide.

### Supply Chain & Data Protection

#### Dependency & supply-chain hygiene

*Anchor:* OpenSSF SLSA framework (slsa.dev) and OWASP Top 10 A06 (Vulnerable and Outdated Components) — dependency provenance and currency are first-class security properties. *Why:* a TypeScript stack ships thousands of transitive npm dependencies to servers and browsers; the supply chain is part of the codebase. *OCF:* [SEC-09](../../data/capabilities.md#sec-09) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Adds dependencies only through the team's vetting process**, keeps lockfiles committed and clean, and acts on automated vulnerability alerts for their changes. Scope: dependencies their tasks touch.
- **E2:** Depth: **Evaluates a package before adopting it** — maintenance health, size, license, transitive surface, alternatives including writing it themselves — and keeps the components they own patched without being chased. Scope: their component's dependency tree.
- **E3:** Depth: **Owns the dependency posture of a capability** — upgrade cadence, pinning strategy, CVE triage by real exploitability, pruning abandoned packages before they bite — and leads its major framework and runtime upgrades. Scope: a capability's supply chain.
- **E4:** Depth: **Builds supply-chain tooling and policy multiple teams follow** (allowlists, automated updates, provenance checks, internal registries) and coordinates response when a shared dependency is compromised. Scope: multiple teams.
- **E5:** Depth: **Sets org supply-chain security posture** — SBOM practice, artifact signing, build integrity, vendor risk — with compliance and security functions, reporting exposure to leadership. Scope: organization-wide.
- **E6:** Depth: **Owns company software supply-chain strategy** and represents it to customers and auditors. Scope: company-wide.

#### Data protection & privacy

*Anchor:* GDPR Art. 25 (data protection by design and by default) and Cavoukian, Privacy by Design (2009) — minimization and purpose limitation designed in, not bolted on. *Why:* full stack engineers decide at design time what gets collected, logged, cached, and retained; mishandling personal data is a company-level event. *OCF:* [OPS-09](../../data/capabilities.md#ops-09) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Handles personal data per the team's rules** — no PII in logs, URLs, or analytics, no secrets in code or client bundles — and asks before adding any new data collection. Scope: data their tasks handle.
- **E2:** Depth: **Applies minimization by default in their features** — collects only what's needed, encrypts what the standard requires, keeps PII out of client caches and telemetry, applies retention rules without prompting. Scope: data handled by components they own.
- **E3:** Depth: **Owns the data-protection design of a capability** — classification, encryption expectations, retention, deletion paths that actually delete — and catches privacy problems in design review before legal has to. Scope: a capability's personal-data footprint.
- **E4:** Depth: **Builds privacy-preserving infrastructure multiple teams rely on** (deletion pipelines, consent propagation, PII-safe logging libraries) and remediates cross-team data-handling gaps. Scope: multiple teams.
- **E5:** Depth: **Owns the org's privacy engineering program with legal and security**, translating regulation into platform defaults teams can follow. Scope: organization-wide.
- **E6:** Depth: **Shapes company data strategy where product value and privacy obligations trade off**, and answers for it to regulators and customers. Scope: company-wide.

## Collaboration & Communication

### Communication

#### Technical writing & documentation

*Anchor:* Winters, Manshreck & Wright, Software Engineering at Google (2020), documentation and design-doc practices — the design doc as the unit of technical decision-making at scale; with Procida's Diátaxis framework for doc types. *Why:* at every level past E1, writing is the primary tool of scale; the written artifact is how design survives contact with other people and future selves. *OCF:* [CC-02](../../data/capabilities.md#cc-02) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Writes PR descriptions, bug reports, and status updates a reviewer can act on without asking questions**, and updates the docs their change makes stale. Scope: documentation of their own work.
- **E2:** Depth: **Documents their features so the next engineer needs no meeting** — READMEs, runbooks, ADR-style decision notes stating problem, options, and choice — matched to the reader, not the writer. Scope: their component's documentation.
- **E3:** Depth: **Writes design docs that anchor a capability's decisions** — conclusion first, alternatives named, trade-offs argued, open questions explicit — that get cited months later, and edits others' docs to sharpen the argument, not the grammar. Scope: the capability's written record; their docs are the onboarding path.
- **E4:** Depth: **Writes the RFCs and strategy docs that align multiple teams on contested decisions**, framing trade-offs so disagreement is about substance, not confusion, structured so busy readers reach the decision point fast. Scope: multi-team decision documents.
- **E5:** Depth: **Writes the strategy and standards documents the organization executes against**, legible to both engineers and executives, and raises the org's documentation bar by example. Scope: organization-wide.
- **E6:** Depth: **Writes the company-defining technical narratives** — public engineering posts, architecture visions, board-level briefs — that survive scrutiny from the board, customers, and the industry. Scope: company-wide and external.

#### Stakeholder communication

*Anchor:* Larson, Staff Engineer (2021) — communicating technical work in the audience's terms is a core staff-plus behavior, observable well before the title. *Why:* full stack work touches every function; untranslated technical detail is where trust leaks. *OCF:* [CC-01](../../data/capabilities.md#cc-01) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Gives accurate, honest status in standups and tickets** — says what's blocked and what's at risk instead of "almost done." Scope: their own work's visibility.
- **E2:** Depth: **Explains their technical work to non-engineers in outcome terms** and warns stakeholders of slips as soon as they know, with a revised plan attached. Scope: their component's stakeholders.
- **E3:** Depth: **Translates a capability's technical state for any audience** — risk for product, cost for finance-minded leaders, options for executives — and runs the meetings where those audiences decide. Scope: a capability's external interface.
- **E4:** Depth: **Keeps multiple teams' stakeholders aligned through change** — reorganizations, migrations, slipped bets — with communication others cite as the reason it went smoothly. Scope: multi-team programs.
- **E5:** Depth: **Represents engineering reality to org leadership** in planning and crisis alike, and is trusted to do so unfiltered. Scope: organization-wide.
- **E6:** Depth: **Represents the company's technology externally** — customers, partners, boards — without overclaiming. Scope: company-wide.

#### Technical discussion & decision-making

*Anchor:* Nygard, "Documenting Architecture Decisions" (2011, the ADR practice) — decisions argued openly, recorded with context, and then committed to. *Why:* teams stall on relitigated or invisible decisions; how disagreement is handled is an observable skill. *OCF:* [CC-05](../../data/capabilities.md#cc-05) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Asks questions in design discussions that clarify rather than derail**, and states their own view with its reasoning when asked. Scope: team discussions.
- **E2:** Depth: **Argues positions from evidence and drops them gracefully when out-argued**, committing visibly to decisions they disagreed with. Scope: their component's decisions.
- **E3:** Depth: **Facilitates decisions rather than winning them** — surfacing the quiet dissent, timeboxing the debate, recording the outcome and its rationale where the next person will find it. Scope: capability decision-making.
- **E4:** Depth: **Brokers technical decisions between teams with conflicting interests**, finding the option that unblocks both and getting explicit commitment from each. Scope: cross-team.
- **E5:** Depth: **Designs the org's technical decision-making mechanisms** (review boards, RFC processes) so decisions are fast, owned, and durable. Scope: organization-wide.
- **E6:** Depth: **Carries the company's hardest technical calls to conclusion**, aligning executives and engineering when they disagree. Scope: company-wide.

### Teamwork

#### Feedback & candor

*Anchor:* Scott, Radical Candor (2017) and Edmondson, The Fearless Organization (2018) — direct, caring feedback in a psychologically safe climate is what makes teams learn. *Why:* teams that cannot exchange honest feedback ship the disagreement into the codebase instead. *OCF:* [CC-04](../../data/capabilities.md#cc-04) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Receives feedback without defensiveness and acts on it visibly**; thanks reviewers for hard comments, asks clarifying questions instead of relitigating, and says so when something seems wrong rather than staying silent. Scope: their own working relationships.
- **E2:** Depth: **Gives peers direct, kind, specific feedback near the moment** — in review, retros, and one-on-ones — following up on whether it landed, and raises team-process problems with a proposed fix. Scope: their team.
- **E3:** Depth: **Names the uncomfortable thing in the room** — a slipping standard, a struggling teammate, a design being talked around — early and in a way people can hear, and models receiving hard feedback publicly. Scope: the team's candor bar; others speak up because they do.
- **E4:** Depth: **Gives feedback across team and level boundaries**, including upward to leaders whose decisions are not working and to senior engineers nobody else will, repairing cross-team frictions before they become escalations. Scope: multiple teams.
- **E5:** Depth: **Builds feedback culture deliberately across the org** — coaching senior engineers on candor, intervening where silence has become the norm, and challenging org-level decisions on the record so others can too. Scope: organization-wide.
- **E6:** Depth: **Tells company leadership the truths no one else will**, with the evidence, standing, and framing to change the outcome. Scope: company-wide.

#### Cross-functional collaboration

*Anchor:* Cagan, Inspired, 2nd ed. (2018) — empowered product teams pair engineers with product and design from discovery, not just delivery; with Skelton & Pais, Team Topologies (2019) on interaction modes. *Why:* full stack work sits at the junction of product, design, and platform; the interfaces between people fail more often than the interfaces between services. *OCF:* [CC-03](../../data/capabilities.md#cc-03) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Asks clarifying questions about acceptance criteria before building**, flags when a mock is ambiguous or technically awkward rather than guessing, and raises blockers the day they appear. Scope: their assigned work.
- **E2:** Depth: **Engages design and product early, working from problem statements rather than just tickets** — flags technical constraints while alternatives are still cheap and translates engineering trade-offs into terms partners can decide on. Scope: their feature's cross-functional loop.
- **E3:** Depth: **Operates as the engineering counterpart to product and design for a capability** — negotiates scope with data, shapes the roadmap with technical possibility rather than feasibility vetoes, and disagrees-and-commits visibly. Scope: cross-functional voice of a capability.
- **E4:** Depth: **Untangles cross-team dependency knots**, clarifying interaction modes and ownership so teams stop blocking each other, keeping decisions made in one room honored in the others. Scope: multiple teams and their stakeholders.
- **E5:** Depth: **Designs the org's team boundaries and interaction patterns with leadership**, applying cognitive-load reasoning to reorganizations and partnering with product leadership on the roadmap. Scope: organization-wide.
- **E6:** Depth: **Aligns engineering with company strategy across functions**, trusted by product, design, and executive peers as a co-owner of outcomes. Scope: company-wide.

## Leadership & Business Impact

### Growing People & Direction

#### Mentoring & growing engineers

*Anchor:* Larson, StaffEng / Staff Engineer (2021) and Fournier, The Manager's Path (2017), mentoring chapters — sponsorship and deliberate mentorship as the core leverage mechanisms of senior ICs. *Why:* past E2, an engineer's ceiling is set by how many others they make better. *OCF:* [LI-01](../../data/capabilities.md#li-01) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Asks questions in public channels so the answers help others**, improves the onboarding docs as they onboard, and helps the next new person with what they just learned. Scope: peer-to-peer help; their own onboarding, made reusable.
- **E2:** Depth: **Onboards new teammates and unblocks juniors day to day** — pairing generously, explaining the why behind conventions rather than just the rules — without doing the work for them. Scope: individuals on their team.
- **E3:** Depth: **Mentors engineers deliberately toward independence** — stretch tasks with a safety net, growth-oriented review comments, career conversations, questions rather than answers — with mentees whose progression is visible to others. Scope: the team's default mentor; grows engineers across the capability.
- **E4:** Depth: **Grows senior engineers into capability owners** — sponsoring them into visible problems, coaching their design judgment through rather than taking over — and creates the structures (guilds, review rotations, design shadowing) where mentoring happens without them. Scope: multiple teams' bench strength.
- **E5:** Depth: **Builds the org's talent-growth machinery** — mentoring programs, promotion-calibration input, technical curricula, the hiring bar — and grows the next staff engineers, sponsoring rather than just advising. Scope: organization-wide.
- **E6:** Depth: **Develops the company's senior technical bench** — shaping who its next principals are and what excellence means here — and is the mentor its top engineers seek out. Scope: company-wide.

#### Technical direction & influence

*Anchor:* Larson, Staff Engineer: Leadership Beyond the Management Track (2021) — staff-plus engineers operate through direction-setting, alignment, and organizational influence without authority. *Why:* the E3→E4 jump is precisely the shift from owning work to multiplying others, and this competency is most of that difference — it must be observable before the title. *OCF:* [LI-03](../../data/capabilities.md#li-03) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Drives their own tasks to done** — chases reviews, resolves ambiguity by asking, raises risks early, and proposes next steps rather than waiting for assignment. Scope: self-leadership.
- **E2:** Depth: **Leads small efforts they're part of and drives small technical decisions to conclusion** — proposes, gathers input, decides or escalates — rather than letting them drift. Scope: leads work within their team.
- **E3:** Depth: **Sets technical direction for a capability others follow voluntarily** — a vision people can repeat, work broken down and sequenced risk-first, the team unblocked, contested decisions landed by argument rather than seniority. This is the terminal-level bar: sustained excellence here is a complete career. Scope: technical lead for a capability and its contributors.
- **E4:** Depth: **Aligns multiple teams on a technical direction none of them owns alone** — builds the coalition, does the 1:1 persuasion and the written case, absorbs the disagreement, and stays accountable through delivery. Scope: multi-team initiatives.
- **E5:** Depth: **Sets technical direction an organization executes against** — picks the few bets that matter, kills zombie projects, chooses what not to do as visibly as what to do — and gets it resourced. Scope: organization-wide.
- **E6:** Depth: **Sets company technical direction with the executive team** — the bets, the narrative, and the accountability for them — carried credibly to boards, customers, and the industry. Scope: company-wide.

### Product & Business Impact

#### Product thinking

*Anchor:* Cagan, Inspired, 2nd ed. (2018) — engineers closest to the technology are a primary source of product insight when they engage with users and value, not just tickets. *Why:* full stack engineers sit closest to the whole user experience of anyone in engineering; wasting that seat wastes the role. *OCF:* [PD-06](../../data/capabilities.md#pd-06) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Explains who uses the feature they're building and why it matters in their own words**, tries their own change as a user before calling it done, and flags when a spec seems to contradict the user's goal. Scope: the features they touch.
- **E2:** Depth: **Uses product analytics and user feedback on features they ship** — checks whether the thing worked, not just whether it deployed — and proposes simpler versions that deliver the same outcome. Scope: outcomes of the features they own.
- **E3:** Depth: **Contributes to discovery, not just delivery** — prototypes to de-risk, brings usage data and user pain to planning, challenges requirements with evidence, and kills their own pet solutions when the data says so. Scope: product partner for a capability; knows its user metrics cold.
- **E4:** Depth: **Spots the product opportunities and risks that only cross-team technical vantage reveals**, killing or redirecting initiatives early with evidence rather than late with delivery pain. Scope: multi-team product surface.
- **E5:** Depth: **Influences org product strategy with technical possibility** — opening options product didn't know were cheap and closing ones that look cheap but aren't — as a peer to product leadership. Scope: organization-wide.
- **E6:** Depth: **Shapes company product direction through technology bets**, spotting the platform shifts that change the business. Scope: company-wide.

#### Scoping, prioritization & estimation

*Anchor:* McConnell, Software Estimation: Demystifying the Black Art (2006) and Reinertsen, The Principles of Product Development Flow (2009) — decomposition-based estimates, thin vertical slices, and cost-of-delay economics. *Why:* trustworthy delivery is the currency senior ICs spend on everything else; what an engineer chooses to do next is an economic decision made dozens of times a week. *OCF:* [PD-02](../../data/capabilities.md#pd-02) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Breaks their tasks into day-sized pieces, flags slips the day they're known**, and finishes what they start — working the agreed priority order rather than the interesting order. Scope: their own task queue.
- **E2:** Depth: **Slices features into thin vertical increments that ship value early** — decomposing across frontend, backend, and migration work — estimates with stated assumptions, distinguishes must-have from nice-to-have, and says no to scope creep with a reason. Scope: delivery of their component.
- **E3:** Depth: **Sequences a capability's work by expected impact, risk, and cost of delay** — hardest unknowns first, states what they're deliberately not doing — and is trusted to trade quality, scope, and time inside the capability without escalation; their estimates are the ones planning trusts. Scope: a capability's outcomes, not its output.
- **E4:** Depth: **De-risks and rebalances multi-team programs** — finds the critical path across teams, keeps every team's slice independently shippable, and cancels or shrinks initiatives with sunk costs when the math says to. Scope: multi-team programs and portfolios.
- **E5:** Depth: **Shapes org-level investment allocation** — product vs. platform vs. paydown, honest capacity math, the mechanisms that keep commitments credible — with the economic case written down. Scope: organization-wide.
- **E6:** Depth: **Answers for the company's biggest technical commitments** — to the board, to customers — re-planning publicly when reality changes; their read on feasibility is treated as load-bearing. Scope: company-wide.

#### Strategic & commercial awareness

*Anchor:* Rumelt, Good Strategy Bad Strategy (2011) — good strategy is diagnosis, guiding policy, and coherent action; engineering choices are strategy in code with a cost model attached. *Why:* the top of an IC ladder is measured in business impact, and the habit of connecting work to outcomes starts at E1. *OCF:* [proposed](../../contrib/2026-07-strategic-commercial-awareness.md) (PD-07 candidate) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Can state what business outcome their current task serves** — and how their team's work makes or saves money — asking when they can't; treats cloud and license costs as real. Scope: awareness of their team's context.
- **E2:** Depth: **Checks whether shipped work actually moved its metric and says so plainly when it didn't**, weighing cost — infra spend, build-vs-buy for small tools, maintenance burden — in the technical choices they own. Scope: outcomes of their features.
- **E3:** Depth: **Frames a capability's technical decisions in business terms** — cost of delay, revenue risk, infra spend, support load, unit economics — pushing back on work with weak business rationale and redirecting effort when the numbers say the plan is wrong. Scope: business results of a capability.
- **E4:** Depth: **Builds the business case for the multi-team technical investments with the largest return** and is trusted by directors to have done the math. Scope: multi-team investment cases.
- **E5:** Depth: **Aligns org technical strategy with the company's economics** — cost curves, velocity, risk — owning trade-offs measured in headcount-years and reported in the business's own terms. Scope: organization-wide.
- **E6:** Depth: **Advises company leadership on where technology changes the business model**, and is accountable for company-level technology bets paying off — treated by the executive team as a peer on business strategy. Scope: company-wide.

#### Ownership & follow-through

*Anchor:* Amazon Leadership Principles — Ownership ("act on behalf of the entire company; never say that's not my job"); with DORA/Accelerate's outcome orientation. *Why:* ladders reward shipped outcomes users get, not activity. *OCF:* [PD-05](../../data/capabilities.md#pd-05) · targets: E1:[P1](../../data/proficiency_scale.md#p1) E2:[P2](../../data/proficiency_scale.md#p2) E3:[P3](../../data/proficiency_scale.md#p3) E4:[P4](../../data/proficiency_scale.md#p4) E5:[P5](../../data/proficiency_scale.md#p5) E6:[P6](../../data/proficiency_scale.md#p6).

- **E1:** Depth: **Sees assigned tasks through to verified-in-production**, not just merged, and reports status honestly including the bad news. Scope: assigned tasks.
- **E2:** Depth: **Owns features from ambiguity to adoption** — chases the dependency, fixes the post-launch bug, closes the loop with the requester. Scope: features they own.
- **E3:** Depth: **Answers for a capability's outcomes** — quality, reliability, user impact — and picks up the critical work that has no owner rather than letting it drop. Scope: a capability, end to end.
- **E4:** Depth: **Takes ownership of cross-team outcomes nobody else can carry**, staying accountable through delivery even where they hold no authority. Scope: multi-team outcomes.
- **E5:** Depth: **Answers for org-level technical outcomes to leadership**, including the failures. Scope: organization-wide.
- **E6:** Depth: **Carries personal accountability for company-critical technical outcomes.** Scope: company-wide.

## Sources

- Allspaw, J. — "Blameless PostMortems and a Just Culture" (Etsy, 2012)
- Amazon — Leadership Principles (Ownership)
- Beyer, B., Jones, C., Petoff, J. & Murphy, N.R. — Site Reliability Engineering (Google/O'Reilly, 2016)
- Cagan, M. — Inspired: How to Create Tech Products Customers Love, 2nd ed. (2018)
- Cavoukian, A. — Privacy by Design (2009); GDPR Art. 25 (data protection by design and by default)
- CircleCI Engineering Competency Matrix (progression.fyi/f/circle-ci) — prose-register calibration
- Cohn, M. — Succeeding with Agile (2009), the test pyramid
- Cunningham, W. — the technical-debt metaphor (OOPSLA 1992)
- Dodds, K.C. — "Application State Management with React" (2020); "Write tests. Not too many. Mostly integration." (2019); Testing Library guiding principles
- Edmondson, A. — The Fearless Organization (2018); Google Project Aristotle
- Evans, E. — Domain-Driven Design (2003)
- Fielding, R. — Architectural Styles and the Design of Network-based Software Architectures (2000); the OpenAPI Specification
- Forsgren, N., Humble, J. & Kim, G. — Accelerate (2018) / the DORA research program
- Fournier, C. — The Manager's Path (2017), mentoring and tech-lead chapters
- Fowler, M. — Refactoring, 2nd ed. (2018); "ContractTest" and consumer-driven contracts (martinfowler.com; Pact)
- Frost, B. — Atomic Design (2016)
- Google — Code Review Developer Guide / Engineering Practices (google.github.io/eng-practices); Technical Writing courses; Project Oxygen; web.dev Core Web Vitals and the RAIL model
- Hohpe, G. & Woolf, B. — Enterprise Integration Patterns (2003)
- Humble, J. & Farley, D. — Continuous Delivery (2010)
- King, A. — "Parse, Don't Validate" (2019)
- Kleppmann, M. — Designing Data-Intensive Applications (2017)
- Larson, W. — Staff Engineer: Leadership Beyond the Management Track / StaffEng.com (2021)
- Majors, C., Fons-Jones, L. & Miranda, G. — Observability Engineering (2022)
- McConnell, S. — Software Estimation: Demystifying the Black Art (2006)
- MDN Web Docs — CSS layout guides (Mozilla)
- Meszaros, G. — xUnit Test Patterns (2007)
- Microsoft — REST API Guidelines; the TypeScript Handbook; Playwright testing best practices
- Minto, B. — The Pyramid Principle (1987)
- monorepo.tools (Nx team); npm and Node.js documentation on semantic versioning
- Newman, S. — Building Microservices, 2nd ed. (2021)
- NIST SP 800-63 — Digital Identity Guidelines
- Node.js documentation — "Don't Block the Event Loop (or the Worker Pool)"; diagnostics guides (OpenJS Foundation); Chrome DevTools documentation (Google)
- Nygard, M. — Release It!, 2nd ed. (2018); "Documenting Architecture Decisions" (2011, the ADR practice)
- OpenSSF — SLSA: Supply-chain Levels for Software Artifacts (slsa.dev)
- Ousterhout, J. — A Philosophy of Software Design (2018)
- OWASP — Top 10 (2021), Cheat Sheet Series, Application Security Verification Standard (ASVS 4.0)
- Parnas, D. — "On the Criteria to Be Used in Decomposing Systems into Modules" (1972)
- PostgreSQL documentation — query planning
- Preston-Werner, T. — Semantic Versioning 2.0.0 (semver.org)
- Procida, D. — the Diátaxis documentation framework (diataxis.fr)
- React documentation — "Thinking in React" (react.dev)
- Redux documentation — "Three Principles"; Facebook Flux architecture documentation (2014); the Elm Architecture
- Reinertsen, D. — The Principles of Product Development Flow (2009)
- Rumelt, R. — Good Strategy Bad Strategy (2011)
- Sadalage, P. & Fowler, M. — "Evolutionary Database Design" (martinfowler.com)
- Scott, K. — Radical Candor (2017)
- Shostack, A. — Threat Modeling: Designing for Security (2014)
- Singer, R. — Shape Up (Basecamp, 2019)
- Skelton, M. & Pais, M. — Team Topologies (2019)
- Stone, D. & Heen, S. — Thanks for the Feedback (2014)
- TanStack Query documentation (Tanner Linsley and maintainers)
- Vanderkam, D. — Effective TypeScript, 2nd ed. (2024)
- Vocke, H. — "The Practical Test Pyramid" (martinfowler.com, 2018)
- W3C — WCAG 2.2; WAI-ARIA Authoring Practices
- Winand, M. — SQL Performance Explained / Use The Index, Luke (use-the-index-luke.com, 2012)
- Winters, T., Manshreck, T. & Wright, H. — Software Engineering at Google (2020), including Hyrum's Law
- Wlaschin, S. — Domain Modeling Made Functional (2018)
- Zeller, A. — Why Programs Fail: A Guide to Systematic Debugging (2009)
- Google (L3–L8) and Meta (E3–E8) engineering level norms via levels.fyi — scope-bar calibration
