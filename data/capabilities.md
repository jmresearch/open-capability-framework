# Capability Catalog

The full Open Capability Framework catalog — 455 capabilities across 36 domains, grouped Segment → Domain → Focus Area. Each capability carries a six-point behavioral profile on the capability-side [P1–P6 proficiency scale](proficiency_scale.md). Note the two-axis split: proficiency (P1–P6) is intrinsic to the capability and measures *how well*; scope ([S1–S6](scope_levels.md)) is a property of the **role** and measures *how broad*. Role records under `roles/` combine the two.

Each capability has a stable anchor equal to its lowercased id (e.g. `#em-03`) so role ladders can deep-link here.

## Engineering & Technology

### Software Engineering (SWE)

#### Code & Quality

<a id="swe-01"></a>
##### SWE-01 — Writing Code

*Type:* Technical — Produces correct, readable, idiomatic code.

- **[P1 — Assisted](proficiency_scale.md#p1):** Writes working, readable code in the team's language; debugs own changes.
- **[P2 — Independent](proficiency_scale.md#p2):** Proficient in the primary language/ecosystem; handles errors, async and concurrency basics correctly.
- **[P3 — Proficient](proficiency_scale.md#p3):** Code is a reference others learn from; debugs the hard problems (races, memory, nondeterminism).
- **[P4 — Expert](proficiency_scale.md#p4):** Mastery across multiple stacks/paradigms; solves problems others can't; sets implementation patterns.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets implementation standards adopted across the org; anticipates where code breaks at scale.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Industry-level depth; authors foundational primitives and idioms others build on.

<a id="swe-02"></a>
##### SWE-02 — Code Quality & Maintainability

*Type:* Technical — Keeps code healthy, modular and maintainable.

- **[P1 — Assisted](proficiency_scale.md#p1):** Writes functional, readable code; uses version control correctly; responds well to review.
- **[P2 — Independent](proficiency_scale.md#p2):** Writes clean, documented, modular code; gives useful review feedback.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs for maintainability; leads refactors of problem areas; review feedback teaches.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert in code health at scale (shared libraries, deprecations, large migrations).
- **[P5 — Authority](proficiency_scale.md#p5):** Shapes org-wide engineering standards for long-lived codebases.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good engineering looks like company-wide; externally recognized.

<a id="swe-03"></a>
##### SWE-03 — Testing & Verification

*Type:* Technical — Designs tests that give real confidence to ship.

- **[P1 — Assisted](proficiency_scale.md#p1):** Writes unit tests with guidance; tests own changes before merging.
- **[P2 — Independent](proficiency_scale.md#p2):** Applies the testing pyramid; everything shipped arrives tested; mocks dependencies sensibly.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs testable systems (contract, property-based, replay from prod); owns a test strategy.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert in test strategy at scale (test data, environments, deployment safety).
- **[P5 — Authority](proficiency_scale.md#p5):** Sets testing/verification discipline across the org.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes the company-wide quality culture; advances verification practice.

<a id="swe-04"></a>
##### SWE-04 — Code Comprehension & Review

*Type:* Technical — Reads, reasons about and reviews others' code.

- **[P1 — Assisted](proficiency_scale.md#p1):** Navigates the codebase and understands code shown; reviews small changes.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently understands unfamiliar code; gives timely, specific review feedback.
- **[P3 — Proficient](proficiency_scale.md#p3):** Quickly grasps complex/legacy systems; reviews raise the bar across a domain.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert at reviewing high-risk changes; review standards spread across teams.
- **[P5 — Authority](proficiency_scale.md#p5):** Authority on review practice org-wide.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good review looks like; shapes industry-facing practice.

#### Design & Architecture

<a id="swe-05"></a>
##### SWE-05 — Software Design & Architecture

*Type:* Technical — Structures software — modules, boundaries, interfaces.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements designs specified by others; asks why, not just how.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs sound components; understands coupling, cohesion, interface design.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs systems for evolution: clean seams, versioned interfaces, replaceable parts.
- **[P4 — Expert](proficiency_scale.md#p4):** Mastery of architecture for complex systems; sets patterns and prevents drift.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets multi-year architecture direction across the org.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Authoritative and externally credible; defines architectural approach others follow.

<a id="swe-06"></a>
##### SWE-06 — Debugging & Systems Diagnosis

*Type:* Technical — Diagnoses defects and anomalies methodically.

- **[P1 — Assisted](proficiency_scale.md#p1):** Debugs issues in own code with support; uses basic tooling.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently diagnoses defects in own area systematically.
- **[P3 — Proficient](proficiency_scale.md#p3):** Leads diagnosis of hard, cross-cutting failures; root cause not symptoms.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert at the rare/systemic failures; builds tooling that makes them visible.
- **[P5 — Authority](proficiency_scale.md#p5):** The person called for the worst failures; sets diagnostic practice org-wide.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Authority on diagnosis; advances the discipline.

<a id="swe-07"></a>
##### SWE-07 — API & Service Design

*Type:* Technical — Designs clean, durable interfaces between systems.

- **[P1 — Assisted](proficiency_scale.md#p1):** Understands HTTP/REST and the deploy pipeline; makes guided changes.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs clean APIs; understands rate limits, retries, timeouts, idempotency.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs services for scale and cost; understands distributed failure modes.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert in platform/service design (multi-tenancy, capacity, shared services).
- **[P5 — Authority](proficiency_scale.md#p5):** Sets interface standards used across the org.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines company-wide API approach; trusted with irreversible interface bets.

<a id="swe-08"></a>
##### SWE-08 — Type-System Domain Modeling

*Type:* Technical — Uses a static type system as a design medium — encoding domain rules and invariants in types so invalid states are unrepresentable and whole defect classes are eliminated at compile time.

- **[P1 — Assisted](proficiency_scale.md#p1):** Writes correctly typed code without escape hatches (`any`-equivalents), uses the codebase's existing types and generics correctly, and reads compiler errors to the actual cause with guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Models feature domains so invalid states fail to compile — sum types / discriminated unions over boolean flags, narrowing over assertions — preferring type-level constraints where the compiler can carry the load.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs the shared domain types a capability is built on, keeping inference ergonomic for consumers; judges when type-level sophistication pays and when it obscures, and unwinds accumulated type erosion in others' code.
- **[P4 — Expert](proficiency_scale.md#p4):** Sets type-design conventions multiple teams adopt — strictness policy, shared type libraries, branded identifiers, result types — and leads migrations that raise strictness without halting delivery.
- **[P5 — Authority](proficiency_scale.md#p5):** Owns an organization's type-system posture — compiler baselines, monorepo type architecture, upgrade cadence — measured by defect and velocity outcomes.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Makes company-level language and type-platform bets and represents the practice externally (talks, upstream contributions, published patterns).

<a id="swe-09"></a>
##### SWE-09 — Boundary Validation & End-to-End Type Integrity

*Type:* Technical — Validates untrusted data into precise types once at every system boundary (network, storage, configuration, third parties) and propagates a single source of type truth across client, server, and wire so contracts cannot silently drift.

- **[P1 — Assisted](proficiency_scale.md#p1):** Uses the codebase's shared contract types and schema validators at boundaries rather than hand-casting external data, and can point to where a type is checked at runtime.
- **[P2 — Independent](proficiency_scale.md#p2):** Puts runtime validation at every I/O boundary they touch — requests, messages, configuration — deriving static types from the runtime schemas so compile-time and runtime cannot drift.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs end-to-end type integrity for a capability — schema-first contracts, generated clients, contract drift caught in continuous integration — and blocks unsound casts and unvalidated edges in review.
- **[P4 — Expert](proficiency_scale.md#p4):** Builds the code-generation and contract-typing infrastructure multiple teams inherit, making boundary safety the default rather than a discipline, and resolves cross-team type drift at its source.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the organization's boundary-safety standard and the platform tooling that enforces it, with incident evidence showing the failure classes it removed.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Owns contract-integrity strategy across products and external interfaces where a broken contract is a business event, and advances the state of practice publicly.

#### Code & Quality

<a id="swe-10"></a>
##### SWE-10 — AI-augmented development

*Type:* Behavioral — Works effectively with AI coding tools and agents while remaining accountable for the output - calibrating what to delegate and what to hand-write, verifying generated changes with the same rigor as hand-written ones, and setting the review and provenance practices that keep quality intact.

- **[P1 — Assisted](proficiency_scale.md#p1):** Uses AI coding tools with the output treated as a draft - reads every generated line, tests it, and can explain any part of the diff when asked.
- **[P2 — Independent](proficiency_scale.md#p2):** Calibrates when generation helps and when it misleads for the work at hand; catches plausible-but-wrong generated code before review, and their AI-assisted changes pass review at the same rate as hand-written ones.
- **[P3 — Proficient](proficiency_scale.md#p3):** Sets the norms for AI-assisted work in a domain - what may be delegated to agents, what verification it requires, how provenance is noted in review - and coaches others out of over-trust and under-use.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines AI-assisted engineering practice across teams - where agents run in the delivery lifecycle, what gates their output - justified by throughput and defect data rather than vendor claims.
- **[P5 — Authority](proficiency_scale.md#p5):** Drives an organization's AI-augmented engineering strategy - tooling selection, workflow redesign, skill expectations - and adjusts policy from measured delivery outcomes.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes how software engineering itself changes with AI at company and industry level; a credible public voice on what changes and what doesn't.

### Frontend & Client Engineering (FE)

#### UI Construction & Rendering

<a id="fe-01"></a>
##### FE-01 — Component-based UI architecture

*Type:* Technical — Composing user interfaces from reusable, encapsulated UI components with clear boundaries and contracts.

- **[P1 — Assisted](proficiency_scale.md#p1):** Builds simple components from existing patterns; relies on review to validate boundaries and props.
- **[P2 — Independent](proficiency_scale.md#p2):** Composes reusable components independently, handling standard prop, state, and event wiring with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs component hierarchies and clear interfaces autonomously; resolves tricky composition and reuse trade-offs.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the component architecture and conventions teams adopt; untangles deeply coupled or overgrown trees.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide component design strategy; anticipates how composition models should evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good component architecture means industrywide; shapes practice through widely adopted patterns.

<a id="fe-02"></a>
##### FE-02 — Declarative UI rendering & reactivity

*Type:* Technical — Expressing UI as a function of state and managing efficient re-rendering when data changes.

- **[P1 — Assisted](proficiency_scale.md#p1):** Binds data to views and updates state for simple cases under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds reactive views independently, managing derived state and updates with routine review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs reactive data flows autonomously; debugs subtle re-render and dependency issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines reactivity patterns others follow; resolves the hardest update and consistency problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets strategy for declarative rendering models; anticipates where reactivity paradigms head.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines industry understanding of reactive UI; pioneers widely emulated rendering approaches.

<a id="fe-03"></a>
##### FE-03 — Document structure & semantic markup

*Type:* Technical — Structuring content with meaningful, well-formed markup that conveys semantics and hierarchy.

- **[P1 — Assisted](proficiency_scale.md#p1):** Writes valid markup using common semantic elements for simple pages under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Structures documents independently with correct semantics for standard content layouts.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs robust semantic structures autonomously; handles complex, dynamic, or nested content.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines markup conventions teams adopt; resolves ambiguous structural and semantic edge cases.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organizational standards for semantic document structure; anticipates evolving markup capabilities.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry norms for semantic markup; influences standards and widely referenced practice.

<a id="fe-04"></a>
##### FE-04 — Client-side rendering strategies

*Type:* Technical — Choosing among client, server, static, and hybrid rendering approaches to balance speed and interactivity.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements basic client rendering for simple views under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Applies standard rendering approaches independently, handling routine hydration and load cases.
- **[P3 — Proficient](proficiency_scale.md#p3):** Chooses and tunes rendering strategies autonomously across varied app and performance needs.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines rendering-strategy approaches teams adopt; solves hard hydration and timing problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets rendering strategy across systems; anticipates shifts in client rendering models.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for rendering strategies industrywide; pioneers influential approaches.

#### State & Data on the Client

<a id="fe-05"></a>
##### FE-05 — Client-side state management

*Type:* Technical — Modeling, storing, and synchronizing application and UI state across the client at appropriate scope.

- **[P1 — Assisted](proficiency_scale.md#p1):** Reads and updates simple shared state following established patterns under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages component and shared state independently for standard flows with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs state architecture autonomously; resolves complex synchronization and ownership issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines state-management patterns others adopt; untangles tangled global and derived state.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets state-management strategy across the organization; anticipates evolving paradigms.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good client state management means; shapes industry patterns and practice.

<a id="fe-06"></a>
##### FE-06 — Client-side data fetching & caching

*Type:* Technical — Retrieving, caching, revalidating, and synchronizing remote data within the client lifecycle.

- **[P1 — Assisted](proficiency_scale.md#p1):** Fetches and displays data for simple endpoints under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements fetching with loading and error states independently for standard cases.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs fetching and caching strategies autonomously; handles invalidation and race conditions.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines fetching and caching patterns teams adopt; solves hard staleness and consistency problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets strategy for client data access and caching; anticipates evolving data-sync models.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for client data fetching and caching; pioneers influential approaches.

<a id="fe-07"></a>
##### FE-07 — Client-side routing & navigation

*Type:* Technical — Managing in-application navigation, route state, and history without full reloads.

- **[P1 — Assisted](proficiency_scale.md#p1):** Adds routes and links for simple navigation under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements nested and parameterized routing independently for standard flows.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs routing architecture autonomously; handles guards, lazy loading, and deep linking.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines routing patterns others adopt; resolves complex navigation and state-preservation cases.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets navigation architecture strategy across applications; anticipates evolving routing models.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for client routing industrywide; shapes widely adopted approaches.

#### Layout & Visual Styling

<a id="fe-08"></a>
##### FE-08 — Responsive & adaptive layout

*Type:* Technical — Designing layouts that fluidly adapt across viewport sizes, orientations, and device capabilities.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies provided responsive rules to simple layouts under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds responsive layouts independently across common breakpoints and devices.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs adaptive layout systems autonomously; handles complex fluid and content-driven cases.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines responsive layout approaches teams adopt; solves the hardest cross-device challenges.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organizational strategy for responsive and adaptive layout; anticipates new device classes.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for responsive design; pioneers widely referenced layout techniques.

<a id="fe-09"></a>
##### FE-09 — Visual styling & presentation systems

*Type:* Technical — Applying scalable styling approaches for visual presentation, theming, and consistent appearance.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies existing styles and tokens to components under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements styling independently following design systems for standard components.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs scalable styling systems autonomously; resolves specificity, theming, and reuse issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines styling architecture and conventions others adopt; untangles fragile, sprawling styles.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets styling-system strategy across the organization; anticipates evolving presentation approaches.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good styling architecture means industrywide; shapes widely adopted systems.

<a id="fe-10"></a>
##### FE-10 — Cross-browser & cross-device compatibility

*Type:* Technical — Ensuring consistent behavior and appearance across differing rendering engines and environments.

- **[P1 — Assisted](proficiency_scale.md#p1):** Fixes obvious compatibility issues on common browsers under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Tests and resolves standard cross-browser problems independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs compatibility strategies autonomously; diagnoses obscure rendering and behavior differences.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines compatibility approaches teams adopt; solves the most elusive cross-environment bugs.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets cross-browser and device strategy; anticipates platform fragmentation and capability shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for compatibility; pioneers influential approaches to fragmentation.

<a id="fe-11"></a>
##### FE-11 — Animation & motion implementation

*Type:* Technical — Implementing performant, purposeful transitions and motion that enhance usability without distraction.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements simple transitions from provided specs under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds standard animations independently with attention to timing and smoothness.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs performant motion systems autonomously; handles complex sequencing and interruption.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines animation patterns others adopt; solves hard performance and choreography problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets motion-design implementation strategy; anticipates evolving animation capabilities.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for motion implementation industrywide; shapes widely adopted techniques.

#### User Experience Quality

<a id="fe-12"></a>
##### FE-12 — Accessibility engineering

*Type:* Technical — Building interfaces usable by people with diverse abilities and assistive technologies per inclusive standards.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies basic accessibility fixes following checklists under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements accessible components independently meeting standard requirements.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs accessible experiences autonomously; resolves complex assistive-technology and interaction cases.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines accessibility approaches teams adopt; solves the hardest inclusive-design problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets accessibility strategy across the organization; anticipates evolving standards and needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry accessibility practice; influences standards and widely referenced guidance.

<a id="fe-13"></a>
##### FE-13 — Frontend performance optimization

*Type:* Technical — Optimizing load, render, and runtime responsiveness through asset, network, and rendering improvements.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies known performance fixes to simple cases under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Profiles and improves standard performance issues independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Diagnoses and optimizes performance autonomously across rendering, loading, and runtime.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines performance approaches teams adopt; solves the most stubborn bottlenecks.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets frontend performance strategy and budgets; anticipates emerging performance concerns.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good frontend performance means industrywide; pioneers influential techniques.

<a id="fe-14"></a>
##### FE-14 — Internationalization & localization

*Type:* Technical — Adapting interfaces for multiple languages, locales, formats, and writing directions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Externalizes strings and applies locale formatting for simple cases under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements internationalization independently for standard content and locales.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs i18n architecture autonomously; handles pluralization, bidirectionality, and complex formatting.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines internationalization approaches teams adopt; solves hard multilingual and cultural cases.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets i18n and localization strategy across products; anticipates expanding locale and market needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for internationalization; pioneers widely adopted approaches.

<a id="fe-15"></a>
##### FE-15 — Progressive enhancement & offline capability

*Type:* Technical — Delivering resilient experiences that degrade gracefully and function under intermittent connectivity.

- **[P1 — Assisted](proficiency_scale.md#p1):** Adds basic fallbacks and simple offline behavior under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements progressive enhancement and standard offline support independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs resilient offline-capable experiences autonomously; handles sync and conflict cases.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines progressive-enhancement patterns teams adopt; solves hard offline and degradation problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets strategy for resilience and offline capability; anticipates evolving connectivity scenarios.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for progressive enhancement industrywide; shapes widely adopted approaches.

#### Client Platform & Tooling

<a id="fe-16"></a>
##### FE-16 — Client build tooling & module bundling

*Type:* Technical — Configuring build pipelines, bundling, and transpilation to package and optimize client artifacts.

- **[P1 — Assisted](proficiency_scale.md#p1):** Runs and tweaks existing build configurations under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Configures standard build and bundling setups independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs build pipelines autonomously; optimizes bundling, splitting, and asset handling.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines build-tooling approaches teams adopt; solves hard performance and configuration problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets build and bundling strategy across projects; anticipates evolving tooling models.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for client build tooling; pioneers influential approaches.

<a id="fe-17"></a>
##### FE-17 — Browser platform & runtime fundamentals

*Type:* Technical — Leveraging core client runtime capabilities, event models, storage, and rendering pipeline behavior.

- **[P1 — Assisted](proficiency_scale.md#p1):** Uses common platform APIs for simple tasks under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Applies browser runtime and lifecycle knowledge independently for standard work.
- **[P3 — Proficient](proficiency_scale.md#p3):** Leverages platform internals autonomously; debugs subtle runtime and event-loop behavior.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines platform-usage approaches teams adopt; solves deep runtime and capability problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets strategy for platform adoption; anticipates evolving browser capabilities and standards.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative understanding of the browser platform; shapes industry practice.

### Backend & Distributed Services (BE)

#### Data Persistence & Modeling

<a id="be-01"></a>
##### BE-01 — Relational data modeling & querying

*Type:* Technical — Designs normalized relational schemas, relationships, and set-based queries for transactional data.

- **[P1 — Assisted](proficiency_scale.md#p1):** Writes simple queries and follows existing schemas under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Models standard entities and writes correct queries independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs normalized schemas autonomously; writes complex queries and resolves modeling trade-offs.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines data-modeling approaches teams adopt; solves the hardest schema and query problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets relational modeling strategy across systems; anticipates evolving data and access needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for relational modeling industrywide; shapes widely adopted approaches.

<a id="be-02"></a>
##### BE-02 — Non-relational data modeling

*Type:* Technical — Models document, key-value, columnar, and graph data shaped around access patterns rather than normalization.

- **[P1 — Assisted](proficiency_scale.md#p1):** Stores and retrieves simple documents or records following patterns under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Models standard non-relational structures independently for known access patterns.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs non-relational schemas autonomously; optimizes for access patterns and denormalization.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines non-relational modeling approaches teams adopt; solves hard data-shape and scale problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets strategy for non-relational data modeling; anticipates evolving workload and access needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for non-relational modeling; pioneers influential approaches.

<a id="be-03"></a>
##### BE-03 — Consistency & transaction design

*Type:* Technical — Applies transactions, isolation levels, and consistency models to keep data correct under concurrent access.

- **[P1 — Assisted](proficiency_scale.md#p1):** Uses provided transaction patterns for simple operations under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard transactions and isolation independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs consistency and transaction boundaries autonomously; resolves concurrency and isolation issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines consistency approaches teams adopt; solves the hardest correctness and contention problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets consistency and transaction strategy across systems; anticipates distributed-correctness challenges.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative practice for consistency design; shapes industry understanding of correctness.

<a id="be-04"></a>
##### BE-04 — Indexing & query optimization

*Type:* Technical — Designs indexes and query plans to meet latency and throughput targets at scale.

- **[P1 — Assisted](proficiency_scale.md#p1):** Adds suggested indexes and reads query plans under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Identifies and resolves standard slow queries independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs indexing strategies autonomously; tunes complex queries and execution plans.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines query-optimization approaches teams adopt; solves the most stubborn performance problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets indexing and optimization strategy across systems; anticipates evolving workload patterns.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for query optimization; pioneers widely referenced techniques.

<a id="be-05"></a>
##### BE-05 — Search & indexing

*Type:* Technical — Builds full-text and faceted search using inverted indexes, ranking, and relevance tuning.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements basic search queries against existing indexes under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds standard search and indexing pipelines independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs search and relevance strategies autonomously; tunes ranking and indexing trade-offs.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines search architecture teams adopt; solves hard relevance, scale, and freshness problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets search strategy across products; anticipates evolving retrieval and ranking needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for search and indexing industrywide; shapes widely adopted approaches.

#### Data Access & Caching

<a id="be-06"></a>
##### BE-06 — Caching strategy & invalidation

*Type:* Technical — Selects cache placement, eviction, and invalidation strategies to balance freshness against performance.

- **[P1 — Assisted](proficiency_scale.md#p1):** Adds simple caching following established patterns under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard caching with basic invalidation independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs caching strategies autonomously; resolves invalidation, staleness, and coherence issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines caching approaches teams adopt; solves the hardest invalidation and consistency problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets caching strategy across systems; anticipates evolving consistency and scale demands.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative practice for caching and invalidation; shapes industry understanding.

<a id="be-07"></a>
##### BE-07 — Data partitioning & sharding

*Type:* Technical — Splits and distributes data across nodes to scale storage and access while managing rebalancing.

- **[P1 — Assisted](proficiency_scale.md#p1):** Operates within existing partitioning schemes for simple tasks under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard partitioning following defined strategies independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs partitioning and sharding schemes autonomously; handles rebalancing and hotspot issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines partitioning approaches teams adopt; solves hard distribution and skew problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets partitioning strategy across systems; anticipates evolving scale and topology needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for partitioning and sharding; pioneers influential approaches.

<a id="be-08"></a>
##### BE-08 — Replication & data distribution

*Type:* Technical — Replicates data across nodes and regions, reasoning about lag, failover, and read/write trade-offs.

- **[P1 — Assisted](proficiency_scale.md#p1):** Operates replicated setups for simple tasks under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Configures standard replication independently following defined patterns.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs replication topologies autonomously; resolves lag, conflict, and failover issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines replication approaches teams adopt; solves hard distribution and consistency problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets replication and distribution strategy across systems; anticipates evolving topology needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for replication and data distribution; shapes industry practice.

#### Messaging & Eventing

<a id="be-09"></a>
##### BE-09 — Message & event-driven architecture

*Type:* Technical — Designs asynchronous, decoupled systems using queues, streams, and publish-subscribe flows.

- **[P1 — Assisted](proficiency_scale.md#p1):** Produces and consumes messages for simple flows under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard event-driven flows independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs event-driven architectures autonomously; resolves ordering, delivery, and coupling concerns.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines event-driven approaches teams adopt; solves the hardest decoupling and flow problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets event-driven architecture strategy across systems; anticipates evolving messaging models.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative practice for event-driven architecture; shapes industry understanding.

<a id="be-10"></a>
##### BE-10 — Event modeling & stream processing

*Type:* Technical — Models domain events and processes continuous streams for real-time and derived state.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements simple stream consumers and event handlers under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds standard stream-processing flows independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs event models and stream pipelines autonomously; handles windowing and state.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines stream-processing approaches teams adopt; solves hard ordering and throughput problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets event-modeling and streaming strategy across systems; anticipates evolving processing needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for event modeling and stream processing; pioneers influential approaches.

<a id="be-11"></a>
##### BE-11 — Idempotency & reliability patterns

*Type:* Technical — Applies idempotency, retries, deduplication, and delivery guarantees to make operations safely repeatable.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies provided idempotency and retry patterns for simple cases under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard reliability and retry handling independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs idempotent, reliable flows autonomously; resolves duplicate and partial-failure cases.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines reliability patterns teams adopt; solves the hardest exactly-once and recovery problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets reliability and idempotency strategy across systems; anticipates evolving failure modes.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for reliability patterns industrywide; shapes widely adopted approaches.

<a id="be-12"></a>
##### BE-12 — Background processing & scheduling

*Type:* Technical — Designs deferred, batched, and scheduled work to offload and coordinate long-running tasks.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements simple background jobs following patterns under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds standard scheduled and queued jobs independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs background-processing systems autonomously; handles retries, concurrency, and timing.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines background-processing approaches teams adopt; solves hard scheduling and throughput problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets background-processing strategy across systems; anticipates evolving workload demands.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for background processing and scheduling; pioneers influential approaches.

#### Service Interfaces & Protocols

<a id="be-13"></a>
##### BE-13 — API contract & versioning design

*Type:* Technical — Defines stable interface contracts, schemas, and versioning strategies for evolving consumers.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements endpoints against existing contracts under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs standard API contracts independently with consistent conventions.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs API contracts and versioning autonomously; manages compatibility and evolution.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines API-design approaches teams adopt; solves hard versioning and compatibility problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets API contract and versioning strategy across the organization; anticipates evolving needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative practice for API design; shapes industry standards and conventions.

<a id="be-14"></a>
##### BE-14 — Synchronous & asynchronous protocol design

*Type:* Technical — Chooses and designs request-response, streaming, and real-time communication protocols for service interaction.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements communication over established protocols for simple cases under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds standard synchronous and async interactions independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs protocol interactions autonomously; chooses sync/async trade-offs and handles failures.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines protocol-design approaches teams adopt; solves hard latency and coupling problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets protocol-design strategy across systems; anticipates evolving communication models.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for protocol design industrywide; shapes widely adopted approaches.

<a id="be-15"></a>
##### BE-15 — Authentication & authorization

*Type:* Technical — Designs identity, credential, token, and access-control mechanisms to protect services and data.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies existing auth mechanisms to simple endpoints under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard authentication and authorization flows independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs auth models autonomously; resolves complex identity, token, and permission cases.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines auth approaches teams adopt; solves the hardest access-control and trust problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets authentication and authorization strategy across systems; anticipates evolving threats.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative practice for auth; shapes industry standards and security understanding.

<a id="be-16"></a>
##### BE-16 — Rate limiting & traffic shaping

*Type:* Technical — Protects services with throttling, quotas, backpressure, and graceful degradation under load.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies provided rate-limit rules to simple endpoints under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard rate limiting and throttling independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs traffic-shaping strategies autonomously; handles bursts, fairness, and backpressure.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines rate-limiting approaches teams adopt; solves hard fairness and abuse problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets traffic-management strategy across systems; anticipates evolving load and abuse patterns.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for rate limiting and traffic shaping; pioneers influential approaches.

#### Scalability & Resilience

<a id="be-17"></a>
##### BE-17 — Scalability & load management

*Type:* Technical — Scales systems horizontally and vertically and distributes load to meet demand elastically.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies known scaling adjustments to simple services under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard scaling and load-handling measures independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs scalable systems autonomously; resolves bottlenecks and load-distribution challenges.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines scalability approaches teams adopt; solves the hardest scaling and contention problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets scalability strategy across systems; anticipates growth and evolving load profiles.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative practice for scalability; shapes industry understanding of scaling.

<a id="be-18"></a>
##### BE-18 — Fault tolerance & failure isolation

*Type:* Technical — Designs timeouts, retries, circuit breakers, and bulkheads to contain and survive partial failures.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies provided resilience patterns to simple services under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard fault-tolerance and isolation measures independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs resilient systems autonomously; resolves cascading-failure and degradation concerns.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines fault-tolerance approaches teams adopt; solves the hardest isolation and recovery problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets resilience strategy across systems; anticipates emerging failure modes and risks.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for fault tolerance industrywide; shapes widely adopted approaches.

<a id="be-19"></a>
##### BE-19 — Capacity planning & resource budgeting

*Type:* Behavioral — Forecasts demand and provisions compute, storage, and connection resources against budgets.

- **[P1 — Assisted](proficiency_scale.md#p1):** Gathers usage metrics and applies simple capacity estimates under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Produces standard capacity forecasts and resource budgets independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Plans capacity autonomously; models demand, headroom, and resource trade-offs.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines capacity-planning approaches teams adopt; solves hard forecasting and efficiency problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets capacity and resource-budgeting strategy across systems; anticipates long-term demand shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for capacity planning; pioneers influential approaches to resource budgeting.

### Architecture & System Design (ARC)

#### Architectural Styles & Decomposition

<a id="arc-01"></a>
##### ARC-01 — Architectural styles & patterns

*Type:* Technical — Selects and applies layered, modular, service-oriented, and event-driven structural patterns to fit context.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies a chosen architectural style to a component under guidance, following existing patterns.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard styles independently for routine systems, selecting from familiar patterns.
- **[P3 — Proficient](proficiency_scale.md#p3):** Selects and combines styles for ambiguous systems, justifying fit against constraints autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines reference architectures and pattern catalogs others adopt across multiple systems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the organization's architectural style strategy and anticipates emerging structural shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Originates architectural styles and patterns the wider industry recognizes and adopts.

<a id="arc-02"></a>
##### ARC-02 — Service decomposition & boundary design

*Type:* Technical — Partitions systems into services and modules with clear ownership and coupling boundaries.

- **[P1 — Assisted](proficiency_scale.md#p1):** Splits a service along boundaries already defined, with decomposition reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Decomposes routine systems into services using established boundary heuristics independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs boundaries for complex domains, resolving overlap and ownership ambiguity autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines decomposition methods and boundary heuristics teams reuse across products.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise-wide boundary and ownership strategy, anticipating decomposition pressures.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes how the industry reasons about service boundaries and decomposition.

<a id="arc-03"></a>
##### ARC-03 — Domain modeling

*Type:* Technical — Models business concepts, language, and boundaries to align software structure with the domain.

- **[P1 — Assisted](proficiency_scale.md#p1):** Translates given domain rules into a model under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds models for familiar domains independently, capturing standard entities and relationships.
- **[P3 — Proficient](proficiency_scale.md#p3):** Models ambiguous domains, surfacing hidden invariants and resolving conflicting expert input.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines modeling approaches and shared language others apply across domains.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets domain-modeling strategy and standards organization-wide, anticipating evolution.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Advances domain-modeling practice recognized and taught across the industry.

<a id="arc-04"></a>
##### ARC-04 — Coupling, cohesion & dependency management

*Type:* Technical — Manages dependencies and direction of coupling to keep components changeable and independently deployable.

- **[P1 — Assisted](proficiency_scale.md#p1):** Removes obvious dependencies and follows cohesion guidance under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages coupling in routine modules independently, applying standard dependency rules.
- **[P3 — Proficient](proficiency_scale.md#p3):** Diagnoses and restructures tangled dependencies in complex systems autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines dependency governance and cohesion principles teams adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide coupling strategy and anticipates structural debt accumulation.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what healthy coupling means for the discipline, influencing wider practice.

#### Distributed Coordination

<a id="arc-05"></a>
##### ARC-05 — Consistency models

*Type:* Technical — Reasons about strong, eventual, and causal consistency to choose correct guarantees per use case.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies a specified consistency model under guidance, with choices reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Selects standard consistency models for routine cases independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Chooses and reasons about consistency trade-offs in ambiguous distributed scenarios autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines consistency-model guidance others rely on for hard correctness problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets consistency strategy across systems and anticipates new model needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Advances how the industry understands and applies consistency models.

<a id="arc-06"></a>
##### ARC-06 — Consensus & coordination

*Type:* Technical — Applies leader election, distributed locks, and consensus to coordinate state across nodes.

- **[P1 — Assisted](proficiency_scale.md#p1):** Configures coordination using established primitives under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Applies standard consensus and coordination mechanisms to routine problems independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs coordination for complex failure scenarios, resolving liveness and safety trade-offs autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines coordination approaches others adopt and solves intractable agreement problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets coordination strategy organization-wide, anticipating distributed-coordination challenges.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry understanding of consensus and coordination.

<a id="arc-07"></a>
##### ARC-07 — Distributed transactions & saga design

*Type:* Technical — Coordinates multi-service state changes using sagas, compensations, and eventual consistency.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements a defined saga or transaction flow under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds standard distributed transactions and compensations independently for routine flows.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs saga and consistency-recovery patterns for complex multi-step flows autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines distributed-transaction patterns and failure-handling approaches teams adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets strategy for cross-system transactional integrity, anticipating coordination needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for distributed transactions across the industry.

#### System Quality & Trade-offs

<a id="arc-08"></a>
##### ARC-08 — Capacity estimation & back-of-envelope modeling

*Type:* Technical — Estimates load, storage, and bandwidth to size systems and validate feasibility early.

- **[P1 — Assisted](proficiency_scale.md#p1):** Performs simple capacity calculations from given assumptions under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Estimates capacity for routine systems independently using standard models.
- **[P3 — Proficient](proficiency_scale.md#p3):** Builds defensible capacity models for ambiguous, large-scale systems autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines estimation methods and reference figures others reuse.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets capacity-planning strategy and anticipates scaling inflection points organization-wide.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Advances how the discipline approaches capacity modeling.

<a id="arc-09"></a>
##### ARC-09 — Non-functional requirement design

*Type:* Technical — Designs for latency, availability, durability, and consistency targets as first-class constraints.

- **[P1 — Assisted](proficiency_scale.md#p1):** Documents non-functional requirements from given targets under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Defines standard non-functional requirements independently for routine systems.
- **[P3 — Proficient](proficiency_scale.md#p3):** Elicits and reconciles conflicting quality requirements in ambiguous contexts autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines NFR frameworks and quality taxonomies others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide quality-attribute strategy, anticipating emerging non-functional concerns.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for defining and reasoning about system qualities.

<a id="arc-10"></a>
##### ARC-10 — Architectural trade-off analysis

*Type:* Behavioral — Evaluates and justifies design options against competing quality attributes and constraints.

- **[P1 — Assisted](proficiency_scale.md#p1):** Compares options against given criteria under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Evaluates standard trade-offs independently for routine architectural choices.
- **[P3 — Proficient](proficiency_scale.md#p3):** Structures and defends trade-off decisions for ambiguous, high-stakes designs autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines trade-off analysis methods and decision frameworks others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets how the organization makes architectural trade-offs, anticipating future tensions.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Advances trade-off-analysis practice recognized across the industry.

### Computer Science Foundations (CS)

#### Data Structures & Algorithms

<a id="cs-01"></a>
##### CS-01 — Algorithmic problem solving

*Type:* Technical — Selects data structures and algorithmic strategies to solve problems correctly and efficiently.

- **[P1 — Assisted](proficiency_scale.md#p1):** Solves well-defined problems using known algorithms under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Selects and applies appropriate algorithms to routine problems independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Devises efficient solutions for novel, ambiguous problems autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines solution approaches and decomposition techniques others learn from.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets standards for algorithmic problem solving and anticipates new problem classes.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Originates algorithmic techniques the wider field adopts.

<a id="cs-02"></a>
##### CS-02 — Computational complexity analysis

*Type:* Technical — Analyzes time and space complexity to compare approaches and predict scaling behavior.

- **[P1 — Assisted](proficiency_scale.md#p1):** Determines complexity of simple algorithms under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Analyzes time and space complexity of routine algorithms independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Analyzes and optimizes complexity for intricate algorithms autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines complexity-analysis methods and teaches rigorous reasoning to others.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets standards for complexity reasoning, anticipating where bottlenecks emerge.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Advances how the field reasons about computational complexity.

<a id="cs-03"></a>
##### CS-03 — Core data structure design

*Type:* Technical — Applies and adapts foundational structures like trees, graphs, hashes, and heaps to model problems.

- **[P1 — Assisted](proficiency_scale.md#p1):** Uses appropriate standard data structures under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Selects and adapts standard structures for routine needs independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs custom structures balancing competing constraints for hard cases autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines structure-selection principles and novel structures others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets data-structure strategy and anticipates evolving access patterns.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Originates data structures recognized and used across the industry.

#### Concurrency & Computation

<a id="cs-04"></a>
##### CS-04 — Concurrency & parallelism

*Type:* Technical — Designs concurrent and parallel execution using synchronization, isolation, and shared-state discipline.

- **[P1 — Assisted](proficiency_scale.md#p1):** Writes concurrent code using given primitives under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard concurrent patterns independently for routine workloads.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs correct, efficient concurrency for complex shared-state problems autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines concurrency patterns and reasoning others adopt to avoid subtle defects.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets concurrency strategy organization-wide, anticipating parallelism challenges.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry understanding of concurrency and parallelism.

<a id="cs-05"></a>
##### CS-05 — Memory & resource management

*Type:* Technical — Reasons about allocation, references, and lifetimes to use memory and resources safely and efficiently.

- **[P1 — Assisted](proficiency_scale.md#p1):** Manages memory and resources following established patterns under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Handles standard allocation and cleanup independently for routine code.
- **[P3 — Proficient](proficiency_scale.md#p3):** Diagnoses and resolves complex leaks, contention, and lifetime issues autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines resource-management approaches others adopt for hard cases.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets resource-management strategy, anticipating efficiency and lifetime concerns.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Advances how the discipline reasons about memory and resource management.

<a id="cs-06"></a>
##### CS-06 — Computation & execution models

*Type:* Technical — Understands how programs map to processes, threads, scheduling, and the underlying machine.

- **[P1 — Assisted](proficiency_scale.md#p1):** Reasons about basic execution behavior under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Applies standard execution-model knowledge to routine work independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Leverages deep execution-model understanding to solve subtle behavioral problems autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines execution-model guidance others rely on for performance and correctness.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets standards for execution-model reasoning, anticipating model shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Advances the field's understanding of computation and execution models.

#### Systems & Networking Fundamentals

<a id="cs-07"></a>
##### CS-07 — Networking & protocol fundamentals

*Type:* Technical — Applies layered networking, addressing, and transport concepts that underpin distributed communication.

- **[P1 — Assisted](proficiency_scale.md#p1):** Diagnoses basic connectivity using given tools under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Applies standard protocol knowledge to routine networking tasks independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Diagnoses and designs around complex protocol and network behavior autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines protocol-usage guidance and solves obscure networking problems for others.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets networking strategy and anticipates protocol-level shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry understanding of networking and protocols.

<a id="cs-08"></a>
##### CS-08 — Operating system & runtime fundamentals

*Type:* Technical — Leverages OS-level concepts of processes, I/O, and resource isolation to reason about runtime behavior.

- **[P1 — Assisted](proficiency_scale.md#p1):** Uses OS and runtime features following guidance under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Applies standard OS and runtime knowledge to routine tasks independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Diagnoses subtle OS and runtime interactions for hard problems autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines runtime-behavior guidance others rely on.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets standards for OS and runtime reasoning, anticipating platform shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Advances the field's understanding of operating-system and runtime behavior.

<a id="cs-09"></a>
##### CS-09 — Data encoding & serialization

*Type:* Technical — Chooses encoding, serialization, and schema-evolution formats for storage and cross-service exchange.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies given encoding and serialization formats under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Selects and uses standard serialization formats independently for routine data.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs encoding schemes balancing compatibility and efficiency for hard cases autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines serialization and schema-evolution approaches others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets encoding strategy organization-wide, anticipating interchange needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Advances industry practice for data encoding and serialization.

### Mobile Engineering (MOB)

#### Mobile UI & Interaction

<a id="mob-01"></a>
##### MOB-01 — Native mobile UI construction

*Type:* Technical — Building screens and views with platform UI paradigms, navigation patterns, and lifecycle awareness.

- **[P1 — Assisted](proficiency_scale.md#p1):** Builds UI screens from given designs using standard components under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Constructs standard native interfaces independently for routine screens.
- **[P3 — Proficient](proficiency_scale.md#p3):** Builds complex, polished native UI resolving tricky layout and rendering cases autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines UI-construction patterns and component libraries others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets native-UI standards and anticipates platform UI evolution.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for native mobile UI construction.

<a id="mob-02"></a>
##### MOB-02 — Touch & gesture interaction design

*Type:* Technical — Implementing touch, gesture, and input handling aligned with mobile interaction conventions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Wires up standard touch handlers following guidance under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements common gestures and touch interactions independently for routine flows.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs complex, conflict-free gesture systems with natural feel autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines gesture-interaction patterns others adopt across apps.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets interaction standards and anticipates new input paradigms.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Advances industry practice for touch and gesture interaction.

<a id="mob-03"></a>
##### MOB-03 — Adaptive layout for device fragmentation

*Type:* Technical — Adapting layouts across varied screen sizes, densities, form factors, and orientations.

- **[P1 — Assisted](proficiency_scale.md#p1):** Adjusts layouts for given screen sizes following guidance under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds responsive layouts independently for common device classes.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs layouts robust across the full fragmentation spectrum autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines adaptive-layout strategies and breakpoint systems others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets fragmentation-handling standards, anticipating new form factors.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for adaptive layout across devices.

#### Device Platform Integration

<a id="mob-04"></a>
##### MOB-04 — Device sensor & hardware integration

*Type:* Technical — Accessing cameras, sensors, location, and other on-device hardware through platform interfaces.

- **[P1 — Assisted](proficiency_scale.md#p1):** Reads sensors using given APIs under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Integrates standard sensors and hardware independently for routine features.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs robust sensor fusion and hardware handling for complex cases autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines sensor-integration patterns others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets hardware-integration strategy, anticipating new sensor capabilities.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Advances industry practice for device sensor and hardware integration.

<a id="mob-05"></a>
##### MOB-05 — Platform permissions & privacy controls

*Type:* Technical — Requesting, managing, and respecting runtime permissions and platform privacy requirements.

- **[P1 — Assisted](proficiency_scale.md#p1):** Requests permissions following platform guidance under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard permission and privacy flows independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs privacy-respecting permission strategies for complex data needs autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines permission and privacy patterns others adopt across apps.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets privacy-control strategy, anticipating regulatory and platform shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for mobile permissions and privacy.

<a id="mob-06"></a>
##### MOB-06 — Push notifications & background processing

*Type:* Technical — Implementing remote messaging and background tasks within platform execution constraints.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements basic notifications and background tasks following guidance under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds standard push and background workflows independently for routine needs.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs reliable notification and background systems under platform constraints autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines push and background-processing patterns others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets notification and background strategy, anticipating platform restrictions.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Advances industry practice for push and background processing.

#### Mobile Runtime Quality

<a id="mob-07"></a>
##### MOB-07 — Mobile app lifecycle & state restoration

*Type:* Technical — Managing app and process lifecycle, suspension, and seamless state restoration across interruptions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Handles lifecycle callbacks following given patterns under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard state save and restore independently for routine flows.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs robust lifecycle and restoration handling for complex state autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines lifecycle and restoration patterns others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets state-management standards across apps, anticipating lifecycle changes.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for app lifecycle and state restoration.

<a id="mob-08"></a>
##### MOB-08 — Mobile performance, memory & battery optimization

*Type:* Technical — Optimizing responsiveness, memory footprint, and energy use under constrained device resources.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies given optimizations and measures with provided tools under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Profiles and fixes common performance and memory issues independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Diagnoses and resolves complex performance, memory, and battery problems autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines optimization methods and budgets others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets mobile-performance strategy, anticipating efficiency challenges.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Advances industry practice for mobile performance and efficiency.

<a id="mob-09"></a>
##### MOB-09 — Offline-first data & local persistence

*Type:* Technical — Persisting data locally and synchronizing reliably across unreliable mobile connectivity.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements local storage following given patterns under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds standard offline storage and caching independently for routine cases.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs robust offline-first sync and conflict resolution for complex data autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines offline-first patterns and sync strategies others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets local-persistence strategy, anticipating connectivity and sync needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for offline-first data.

<a id="mob-10"></a>
##### MOB-10 — Cross-platform mobile development

*Type:* Technical — Sharing logic and UI across platforms while honoring each platform's conventions and capabilities.

- **[P1 — Assisted](proficiency_scale.md#p1):** Builds shared features following established cross-platform patterns under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard cross-platform components independently for routine needs.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs cross-platform architecture balancing sharing and platform fidelity autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines cross-platform approaches and abstractions others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets cross-platform strategy, anticipating platform divergence.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Advances industry practice for cross-platform mobile development.

#### Release & Distribution

<a id="mob-11"></a>
##### MOB-11 — Mobile release & store delivery

*Type:* Technical — Packaging, signing, submitting, and managing app distribution through store review and rollout processes.

- **[P1 — Assisted](proficiency_scale.md#p1):** Prepares release builds and submissions following given steps under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages standard store submission and release processes independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs release pipelines handling complex store and rollout requirements autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines release and store-delivery practices others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets release strategy, anticipating store-policy and distribution shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for mobile release and store delivery.

<a id="mob-12"></a>
##### MOB-12 — Over-the-air updates & version adoption

*Type:* Technical — Delivering updates and managing fragmented version adoption across an installed user base.

- **[P1 — Assisted](proficiency_scale.md#p1):** Ships OTA updates following given configuration under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages standard OTA delivery and version targeting independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs safe OTA rollout and adoption strategies for complex fleets autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines OTA-update and adoption-management patterns others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets update-delivery strategy, anticipating version-fragmentation challenges.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Advances industry practice for over-the-air updates and version adoption.

### Data Engineering & Analytics (DATA)

#### Data Pipelines & Integration

<a id="data-01"></a>
##### DATA-01 — Batch & streaming pipeline design

*Type:* Technical — Designs batch and real-time data flows that move and transform data reliably at scale.

- **[P1 — Assisted](proficiency_scale.md#p1):** Builds simple batch jobs from clear specs, with output and logic reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs routine batch or streaming pipelines independently, handling common volume and ordering cases.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs robust pipelines for ambiguous workloads, balancing latency, throughput, and cost autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines reusable pipeline patterns others adopt and resolves intractable backpressure or exactly-once problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the organization's batch-versus-streaming strategy and anticipates emerging processing paradigms.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good pipeline architecture means industry-wide and is externally recognized for it.

<a id="data-02"></a>
##### DATA-02 — Data ingestion & integration

*Type:* Technical — Acquires and consolidates data from heterogeneous internal and external sources into usable form.

- **[P1 — Assisted](proficiency_scale.md#p1):** Connects to documented sources and loads data under guidance, with mappings reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently integrates standard sources, handling routine schema and format variation.
- **[P3 — Proficient](proficiency_scale.md#p3):** Reliably integrates messy, undocumented, or high-volume sources and resolves hard reconciliation cases.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines ingestion frameworks and connector patterns others reuse across diverse source types.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets integration strategy and standards, anticipating new source modalities and protocols.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for source integration and is externally credible on the topic.

<a id="data-03"></a>
##### DATA-03 — Workflow orchestration & scheduling

*Type:* Technical — Coordinates dependent data tasks into reliable, repeatable, scheduled pipelines.

- **[P1 — Assisted](proficiency_scale.md#p1):** Configures predefined workflow steps and dependencies under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds and schedules routine multi-step workflows independently with normal retry handling.
- **[P3 — Proficient](proficiency_scale.md#p3):** Orchestrates complex interdependent workflows autonomously, resolving tricky timing and failure cases.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines orchestration patterns and guardrails others adopt for reliability at scale.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets orchestration strategy and standards, anticipating shifts in scheduling and dependency management.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for workflow orchestration across the discipline and is externally recognized.

<a id="data-04"></a>
##### DATA-04 — Change data capture & incremental processing

*Type:* Technical — Captures and propagates source data changes efficiently without full reprocessing.

- **[P1 — Assisted](proficiency_scale.md#p1):** Runs configured incremental loads and verifies row counts under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard change-capture and incremental jobs independently for common scenarios.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs reliable incremental processing for late-arriving, out-of-order, or deleted-record cases autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines incremental and capture patterns others adopt to guarantee correctness and replayability.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the strategy for change propagation and anticipates evolving capture techniques.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines industry standards for change data capture and is externally credible.

#### Data Modeling & Storage

<a id="data-05"></a>
##### DATA-05 — Data modeling & warehousing

*Type:* Technical — Structures data into warehouses and lakes optimized for storage, access, and analytics.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements predefined tables and relationships under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs standard warehouse models independently for routine subject areas.
- **[P3 — Proficient](proficiency_scale.md#p3):** Models ambiguous domains autonomously, resolving hard normalization and historization trade-offs.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines modeling conventions and warehouse architecture others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise data-modeling strategy and anticipates shifts in storage paradigms.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good warehouse modeling means industry-wide and is externally recognized.

<a id="data-06"></a>
##### DATA-06 — Dimensional & analytics modeling

*Type:* Technical — Designs facts, dimensions, and analytical schemas that make data intuitive to query.

- **[P1 — Assisted](proficiency_scale.md#p1):** Builds facts and dimensions from supplied designs under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs standard star schemas independently for routine analytics needs.
- **[P3 — Proficient](proficiency_scale.md#p3):** Models complex grains, slowly-changing dimensions, and conformance issues autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines dimensional modeling patterns and conformed-dimension standards others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets dimensional strategy across analytics domains and anticipates modeling evolution.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for dimensional modeling and is externally credible.

<a id="data-07"></a>
##### DATA-07 — Relational analytics & query design

*Type:* Technical — Composes set-based queries and joins to answer analytical questions over relational data.

- **[P1 — Assisted](proficiency_scale.md#p1):** Writes simple queries from clear requirements, with logic reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Writes correct multi-join analytical queries independently for routine questions.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs complex queries handling tricky aggregations, window logic, and edge semantics autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines query patterns and reusable analytical building blocks others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets standards for analytical query design and anticipates shifts in query paradigms.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for analytical querying across the discipline and is externally recognized.

<a id="data-08"></a>
##### DATA-08 — Query & storage optimization

*Type:* Technical — Tunes data layout, indexing, and query plans to balance speed, scale, and resource use.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies suggested indexes or partitions under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Tunes routine slow queries and storage layouts independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Diagnoses and resolves hard performance and storage-cost problems autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines optimization playbooks others adopt and solves pathological bottlenecks.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets optimization strategy and anticipates emerging storage and execution techniques.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines industry standards for query and storage optimization and is externally credible.

#### Data Quality & Governance

<a id="data-09"></a>
##### DATA-09 — Data quality & validation

*Type:* Technical — Defines and enforces checks for accuracy, completeness, and consistency across datasets.

- **[P1 — Assisted](proficiency_scale.md#p1):** Runs predefined quality checks and flags failures under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds standard validation rules independently and triages common quality issues.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs comprehensive quality frameworks and resolves ambiguous root-cause cases autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines quality-checking patterns and severity frameworks others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets data-quality strategy and anticipates evolving validation approaches.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good data quality means industry-wide and is externally recognized.

<a id="data-10"></a>
##### DATA-10 — Data governance & lineage

*Type:* Technical — Tracks data origins, ownership, and movement to ensure trust, compliance, and traceability.

- **[P1 — Assisted](proficiency_scale.md#p1):** Records lineage and metadata into provided systems under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Maintains governance documentation and lineage for routine assets independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Establishes governance and lineage for complex, cross-team data flows autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines governance frameworks and lineage standards others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise governance strategy and anticipates regulatory and stewardship shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for data governance and is externally credible.

<a id="data-11"></a>
##### DATA-11 — Master & reference data management

*Type:* Technical — Maintains consistent, authoritative definitions of core business entities across systems.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains reference lists and match rules under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages standard master and reference data independently with routine deduplication.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves hard entity-matching, survivorship, and hierarchy conflicts autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines mastering and stewardship patterns others adopt across domains.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets master-data strategy and anticipates evolving entity-resolution approaches.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for master data management and is externally recognized.

<a id="data-12"></a>
##### DATA-12 — Data privacy & access stewardship

*Type:* Behavioral — Safeguards sensitive data through appropriate classification, access, and retention practices.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies predefined access and masking rules under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard privacy controls and access grants independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs access and privacy schemes for ambiguous, sensitive cases autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines privacy and access-control patterns others adopt across the data estate.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets privacy and stewardship strategy and anticipates regulatory and risk shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines industry standards for data privacy stewardship and is externally credible.

#### Analytics & Insight

<a id="data-13"></a>
##### DATA-13 — Exploratory data analysis

*Type:* Technical — Profiles and explores data to surface patterns, anomalies, and analytical opportunities.

- **[P1 — Assisted](proficiency_scale.md#p1):** Profiles datasets and produces basic summaries under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Explores routine datasets independently, surfacing distributions and obvious anomalies.
- **[P3 — Proficient](proficiency_scale.md#p3):** Uncovers non-obvious patterns and data issues in ambiguous datasets autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines exploration approaches others adopt and frames what questions data can answer.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets standards for rigorous exploration and anticipates new analytical techniques.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for exploratory analysis across the discipline and is externally recognized.

<a id="data-14"></a>
##### DATA-14 — Statistical inference & hypothesis testing

*Type:* Technical — Draws defensible conclusions from data using probability and significance testing.

- **[P1 — Assisted](proficiency_scale.md#p1):** Runs prescribed tests and reports outputs under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Selects and applies standard tests independently for routine questions.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs sound inference for tricky, assumption-violating cases autonomously and interprets correctly.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines inferential methods others adopt and corrects subtle statistical misuse.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets standards for statistical rigor and anticipates methodological advances.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for applied inference and is externally credible.

<a id="data-15"></a>
##### DATA-15 — Metric definition & semantic layers

*Type:* Technical — Defines consistent, reusable business metrics and the shared semantics behind them.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements metric definitions as specified under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Defines and documents standard metrics independently with consistent logic.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves ambiguous or conflicting metric definitions and edge semantics autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines semantic-layer patterns and metric governance others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets metric and semantic strategy and anticipates shifts in measurement practice.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for metric and semantic design and is externally recognized.

<a id="data-16"></a>
##### DATA-16 — Data wrangling & transformation

*Type:* Technical — Cleans, reshapes, and enriches raw data into analysis-ready datasets.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies prescribed cleaning and reshaping steps under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Transforms and cleans routine messy data independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Wrangles severely malformed or complex data into reliable shape autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines transformation patterns and reusable cleaning logic others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets standards for transformation rigor and anticipates evolving wrangling techniques.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines industry best practice for data transformation and is externally credible.

#### Decision Support & Reporting

<a id="data-17"></a>
##### DATA-17 — Data visualization & storytelling

*Type:* Behavioral — Turns analysis into clear visuals and narratives that drive understanding and action.

- **[P1 — Assisted](proficiency_scale.md#p1):** Produces standard charts from given data and specs under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Creates clear, correct visuals independently for routine reporting needs.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs compelling narratives that drive decisions for ambiguous audiences autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines visualization patterns and storytelling standards others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the organization's data-storytelling approach and anticipates shifts in communication norms.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good data storytelling means industry-wide and is externally recognized.

<a id="data-18"></a>
##### DATA-18 — Dashboard & self-service reporting design

*Type:* Technical — Builds reusable dashboards and reports that let stakeholders explore data independently.

- **[P1 — Assisted](proficiency_scale.md#p1):** Builds dashboard components from provided requirements under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs functional dashboards and self-service views independently for routine needs.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs intuitive, performant self-service experiences for ambiguous user needs autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines dashboard and self-service design patterns others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets self-service reporting strategy and anticipates shifts in analytics consumption.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for self-service reporting and is externally credible.

<a id="data-19"></a>
##### DATA-19 — Requirements gathering & stakeholder translation

*Type:* Behavioral — Elicits business questions and translates them into well-scoped analytical deliverables.

- **[P1 — Assisted](proficiency_scale.md#p1):** Captures stated requirements accurately under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Elicits and documents routine requirements independently, clarifying obvious gaps.
- **[P3 — Proficient](proficiency_scale.md#p3):** Surfaces unstated needs and translates ambiguous asks into clear specs autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines elicitation and translation approaches others adopt across teams.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets standards for requirements practice and anticipates evolving stakeholder needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for stakeholder translation in analytics and is externally recognized.

<a id="data-20"></a>
##### DATA-20 — Business & domain acumen

*Type:* Behavioral — Applies understanding of the business context to frame data work around real value.

- **[P1 — Assisted](proficiency_scale.md#p1):** Learns core domain concepts and applies them to tasks under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Applies solid domain understanding to routine analytical work independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Connects data work to business outcomes and frames hard domain questions autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines how domain context shapes analytics approaches others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets direction linking data capability to business strategy and anticipates domain shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Recognized externally for shaping how the domain and data discipline intersect.

### AI & ML Engineering (AI)

#### LLM Systems

<a id="ai-01"></a>
##### AI-01 — LLM Integration & Prompt Engineering

*Type:* Technical — Builds reliable features on top of language models.

- **[P1 — Assisted](proficiency_scale.md#p1):** Understands LLM basics (tokens, context windows, temperature, system prompts); calls model APIs correctly.
- **[P2 — Independent](proficiency_scale.md#p2):** Writes effective prompts; uses structured outputs, function calling and streaming; understands model differences and pricing.
- **[P3 — Proficient](proficiency_scale.md#p3):** Expert prompt/context design (few-shot, decomposition, chaining); knows when fine-tuning beats prompting (rarely); designs for model swappability.
- **[P4 — Expert](proficiency_scale.md#p4):** Mastery of model behavior across providers and versions; designs upgrade-migration strategies; squeezes capability others can't.
- **[P5 — Authority](proficiency_scale.md#p5):** Deep expertise; anticipates capability shifts (new modalities, reasoning models) and repositions ahead of them.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Authority on applied LLM engineering; may influence industry practice.

<a id="ai-02"></a>
##### AI-02 — Context & Retrieval Engineering

*Type:* Technical — Grounds models in the right knowledge.

- **[P1 — Assisted](proficiency_scale.md#p1):** Understands embeddings, similarity search and why grounding reduces hallucination.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds standard RAG pipelines (chunking, embedding, retrieval, reranking); manages context budgets deliberately.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs retrieval quality systems (hybrid search, reranking, freshness, citation, memory for multi-turn).
- **[P4 — Expert](proficiency_scale.md#p4):** Expert in retrieval at scale (index strategy, multi-source federation, permission-aware retrieval).
- **[P5 — Authority](proficiency_scale.md#p5):** Deep expertise; anticipates how longer context and new architectures change retrieval economics.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Mastery of the discipline; defines how AI systems access knowledge.

<a id="ai-03"></a>
##### AI-03 — Agentic Systems & Orchestration

*Type:* Technical — Designs systems where models plan and act through tools.

- **[P1 — Assisted](proficiency_scale.md#p1):** Understands tool calling and the agent loop (plan, act, observe); knows why agents need constraints.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs good tool interfaces; builds single-agent workflows with sensible termination and confirmation points.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs reliable multi-step agents (state, recovery, sandboxing, permissions, human-in-the-loop); knows when an agent is the wrong answer.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert in complex orchestration (multi-agent, long-running workflows, MCP-style standards) and safe constraint at scale.
- **[P5 — Authority](proficiency_scale.md#p5):** Deep expertise; anticipates how increasing model autonomy changes system design.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Authority on agentic systems; may influence emerging industry standards.

#### AI Quality & Safety

<a id="ai-04"></a>
##### AI-04 — AI Evaluation

*Type:* Technical — Proves AI behavior is good enough to ship.

- **[P1 — Assisted](proficiency_scale.md#p1):** Understands why 'it looked right in testing' is insufficient; runs existing evals and labels carefully.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds basic eval sets from real usage; measures changes before shipping prompt/model updates.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs eval methodology (golden sets, LLM-as-judge with validation, human review, helpfulness/groundedness/safety metrics).
- **[P4 — Expert](proficiency_scale.md#p4):** Expert in eval at scale (continuous eval, A/B testing AI features, drift detection).
- **[P5 — Authority](proficiency_scale.md#p5):** Deep expertise in measuring AI quality where ground truth is contested.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Mastery of the discipline; sets the bar for what 'proven to work' means.

<a id="ai-05"></a>
##### AI-05 — Responsible AI & Guardrails

*Type:* Technical — Keeps AI behavior safe, honest and within bounds.

- **[P1 — Assisted](proficiency_scale.md#p1):** Understands that models can be harmful, biased or confidently wrong; flags concerning behavior.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements guardrails (filtering, refusal handling, grounding checks); designs honest UX.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs layered safety proportional to stakes; evaluates for bias/misuse before launch.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert in safety system design at scale; defines oversight and escalation frameworks.
- **[P5 — Authority](proficiency_scale.md#p5):** Deep expertise balancing capability and safety under real product pressure.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Recognized authority; establishes responsible AI as a value; externally credible.

#### Data Preparation for ML

<a id="ai-06"></a>
##### AI-06 — Feature engineering

*Type:* Technical — Transforms raw data into informative features that improve model learning and performance.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements specified features and transformations under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Engineers standard features independently for routine modeling tasks.
- **[P3 — Proficient](proficiency_scale.md#p3):** Derives high-signal features for ambiguous problems and avoids leakage autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines feature-engineering patterns and leakage-prevention standards others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets feature strategy and anticipates advances in representation techniques.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for feature engineering across the discipline and is externally recognized.

<a id="ai-07"></a>
##### AI-07 — Data labeling & dataset curation

*Type:* Technical — Assembles, labels, and curates representative datasets suitable for model training.

- **[P1 — Assisted](proficiency_scale.md#p1):** Labels data to clear guidelines and flags ambiguities under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Curates and labels routine datasets independently, applying consistent guidelines.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs labeling schemes and resolves ambiguity and quality issues autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines curation and annotation-quality standards others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets dataset strategy and anticipates shifts in labeling and curation practice.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines industry best practice for dataset curation and is externally credible.

<a id="ai-08"></a>
##### AI-08 — Feature stores & reuse

*Type:* Technical — Manages consistent, shareable feature definitions across training and serving.

- **[P1 — Assisted](proficiency_scale.md#p1):** Registers and retrieves features from a feature store under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Publishes and consumes reusable features independently for routine use.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs feature definitions ensuring consistency and freshness across uses autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines feature-store patterns and reuse governance others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets feature-reuse strategy and anticipates shifts in feature management.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for feature reuse across the discipline and is externally recognized.

#### Modeling & Training

<a id="ai-09"></a>
##### AI-09 — Classical model training & selection

*Type:* Technical — Trains and compares supervised and unsupervised models to fit the problem at hand.

- **[P1 — Assisted](proficiency_scale.md#p1):** Trains models with given settings and reports metrics under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Trains and selects standard models independently for routine problems.
- **[P3 — Proficient](proficiency_scale.md#p3):** Chooses and trains appropriate models for ambiguous problems and avoids overfitting autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines model-selection approaches others adopt and solves intractable modeling cases.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets modeling strategy and anticipates shifts in classical technique relevance.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for model selection across the discipline and is externally recognized.

<a id="ai-10"></a>
##### AI-10 — Deep learning & neural architectures

*Type:* Technical — Designs and trains neural networks for complex perception, sequence, and representation tasks.

- **[P1 — Assisted](proficiency_scale.md#p1):** Trains predefined network architectures under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Adapts standard architectures independently for routine tasks.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs and debugs architectures for hard problems and convergence issues autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines architectural patterns others adopt and solves problems others cannot.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets neural-architecture strategy and anticipates emerging model designs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for neural architecture and is externally credible.

<a id="ai-11"></a>
##### AI-11 — Hyperparameter tuning & optimization

*Type:* Technical — Systematically searches model configurations to maximize performance and generalization.

- **[P1 — Assisted](proficiency_scale.md#p1):** Runs prescribed tuning sweeps and reports results under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Tunes standard hyperparameters independently for routine models.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs efficient search strategies for hard, high-dimensional spaces autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines tuning methodologies others adopt and solves stubborn optimization cases.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets optimization strategy and anticipates advances in search techniques.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for hyperparameter optimization and is externally recognized.

<a id="ai-12"></a>
##### AI-12 — Mathematical & statistical foundations

*Type:* Technical — Applies linear algebra, calculus, and probability to reason about model behavior.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies basic mathematical and statistical concepts to tasks under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Applies foundational math and statistics correctly to routine modeling independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Reasons rigorously about hard mathematical and statistical aspects of problems autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines how foundational theory informs practice others adopt and corrects subtle errors.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets standards for mathematical rigor and anticipates relevant theoretical advances.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Recognized externally for advancing applied mathematical practice in the discipline.

#### Evaluation & Experimentation

<a id="ai-13"></a>
##### AI-13 — Model evaluation & validation

*Type:* Technical — Assesses model accuracy, robustness, and generalization with sound validation methods.

- **[P1 — Assisted](proficiency_scale.md#p1):** Computes prescribed evaluation metrics under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Selects appropriate metrics and validation splits independently for routine cases.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs sound evaluation for ambiguous, leakage-prone, or imbalanced cases autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines evaluation methodologies and validation standards others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets evaluation strategy and anticipates advances in validation practice.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for model evaluation across the discipline and is externally recognized.

<a id="ai-14"></a>
##### AI-14 — Experimentation & A/B testing (ML)

*Type:* Technical — Designs controlled experiments to measure real-world impact of models and changes.

- **[P1 — Assisted](proficiency_scale.md#p1):** Executes designed experiments and reports outcomes under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs and runs standard experiments independently with correct basic analysis.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs rigorous experiments handling confounds and tricky readouts autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines experimentation frameworks and guardrails others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets experimentation strategy and anticipates advances in causal and online testing.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for ML experimentation and is externally credible.

<a id="ai-15"></a>
##### AI-15 — Bias, fairness & error analysis

*Type:* Behavioral — Investigates model errors and disparate outcomes to guide responsible improvement.

- **[P1 — Assisted](proficiency_scale.md#p1):** Runs prescribed bias and error checks under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Performs standard fairness and error analysis independently for routine models.
- **[P3 — Proficient](proficiency_scale.md#p3):** Diagnoses subtle bias and failure modes in ambiguous cases and proposes remedies autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines fairness and error-analysis frameworks others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets fairness strategy and anticipates evolving ethical and regulatory expectations.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry practice for fairness and error analysis and is externally recognized.

#### ML Operations & Lifecycle

<a id="ai-16"></a>
##### AI-16 — ML pipeline & deployment (MLOps)

*Type:* Technical — Automates training, packaging, and deployment of models into reliable production services.

- **[P1 — Assisted](proficiency_scale.md#p1):** Runs predefined training and deployment steps under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds and deploys routine ML pipelines independently with normal automation.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs reliable, reproducible deployment pipelines for hard cases autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines MLOps patterns and deployment standards others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets MLOps strategy and anticipates shifts in lifecycle automation.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for ML operations across the discipline and is externally recognized.

<a id="ai-17"></a>
##### AI-17 — Model monitoring & drift detection

*Type:* Technical — Tracks live model quality and data drift to trigger retraining or rollback.

- **[P1 — Assisted](proficiency_scale.md#p1):** Watches configured monitors and reports alerts under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Sets up standard performance and drift monitoring independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs monitoring that catches subtle drift and degradation autonomously and triages causes.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines monitoring and drift-detection patterns others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets monitoring strategy and anticipates advances in drift detection.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for model monitoring and is externally credible.

<a id="ai-18"></a>
##### AI-18 — Model & experiment versioning

*Type:* Technical — Tracks datasets, models, and experiments for reproducibility and auditability.

- **[P1 — Assisted](proficiency_scale.md#p1):** Records model and experiment versions per process under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages standard versioning of models, data, and experiments independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs reproducible versioning across complex experiment lineages autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines versioning and reproducibility standards others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets versioning strategy and anticipates shifts in reproducibility practice.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for model and experiment versioning and is externally recognized.

<a id="ai-19"></a>
##### AI-19 — Model serving & inference optimization

*Type:* Technical — Exposes models for low-latency, scalable inference across batch and real-time use.

- **[P1 — Assisted](proficiency_scale.md#p1):** Deploys models to a serving setup with given configs under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Serves models independently and applies standard latency and throughput tuning.
- **[P3 — Proficient](proficiency_scale.md#p3):** Optimizes serving for hard latency, scale, and cost constraints autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines serving and inference-optimization patterns others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets serving strategy and anticipates advances in inference efficiency.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for model serving across the discipline and is externally recognized.

<a id="ai-20"></a>
##### AI-20 — Problem framing & ML solution design

*Type:* Behavioral — Translates ambiguous business problems into well-posed, feasible ML approaches.

- **[P1 — Assisted](proficiency_scale.md#p1):** Translates a clearly scoped problem into a defined ML task under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Frames routine problems as appropriate ML solutions independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Frames ambiguous business problems into sound ML or non-ML approaches autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines solution-design patterns others adopt and reframes intractable problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets ML solution strategy and anticipates where applicable techniques are heading.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for ML problem framing across the discipline and is externally recognized.

#### AI Quality & Safety

<a id="ai-21"></a>
##### AI-21 — AI risk governance

*Type:* Behavioral — Assesses and governs the risk of AI systems through their lifecycle - classifying systems against recognized risk frameworks, converting findings into engineering requirements with owners, and keeping the evidence trail (evals, controls, incidents) audit-ready as systems and regulation change.

- **[P1 — Assisted](proficiency_scale.md#p1):** Completes the risk checklist for their change accurately - identifying who is affected if the model is wrong - and escalates anything the checklist doesn't cover.
- **[P2 — Independent](proficiency_scale.md#p2):** Assesses a feature's failure impact before build (misuse, error harm, disparate performance across user groups) and documents mitigations and residual risk unprompted.
- **[P3 — Proficient](proficiency_scale.md#p3):** Classifies a domain against the applicable risk framework, keeps its evidence pack (evals, controls, incidents) audit-ready, converts findings into engineering requirements with owners, and flags when a product change alters the risk class.
- **[P4 — Expert](proficiency_scale.md#p4):** Operates a cross-team AI risk-review process - fast enough that teams use it honestly, rigorous enough to catch real issues - and builds governance tooling that makes compliance a byproduct of normal engineering.
- **[P5 — Authority](proficiency_scale.md#p5):** Owns an organization's AI governance program jointly with legal and risk functions, translating regulation into engineering requirements without freezing delivery.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Positions a company ahead of AI regulation; accountable to executives, boards, and regulators for where the risk lines are drawn.

### Systems, Infrastructure & Operations (OPS)

#### Infrastructure

<a id="ops-01"></a>
##### OPS-01 — Cloud & Infrastructure Engineering

*Type:* Technical — Engineers compute, network, storage and IaC.

- **[P1 — Assisted](proficiency_scale.md#p1):** Makes guided changes to existing infra; understands core cloud services.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently builds and manages standard resources using IaC.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs infra for scale, cost and resilience across a domain.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert in infra platforms used by many teams; owns major cost strategy.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets org infrastructure direction.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Trusted with company-level platform bets; defines infra strategy.

<a id="ops-02"></a>
##### OPS-02 — CI/CD & Delivery Engineering

*Type:* Technical — Builds the build, test, release and deploy pipeline.

- **[P1 — Assisted](proficiency_scale.md#p1):** Uses and makes guided fixes to existing pipelines.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently builds and improves pipelines for their area.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs deployment safety (progressive delivery, rollback) for a domain.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert in delivery engineering at scale; sets standards across teams.
- **[P5 — Authority](proficiency_scale.md#p5):** Defines the org's delivery/release philosophy.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Advances release engineering practice company-wide.

<a id="ops-03"></a>
##### OPS-03 — Distributed Systems

*Type:* Technical — Reasons about systems spanning many machines.

- **[P1 — Assisted](proficiency_scale.md#p1):** Understands the basics (timeouts, retries, idempotency) conceptually.
- **[P2 — Independent](proficiency_scale.md#p2):** Correctly applies distributed patterns in scoped work.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs for distributed failure modes (consistency, partitioning, backpressure).
- **[P4 — Expert](proficiency_scale.md#p4):** Expert in distributed systems at scale; anticipates emergent failure.
- **[P5 — Authority](proficiency_scale.md#p5):** Shapes how the org builds at scale.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Authority on distributed design; influences the field.

#### Operations

<a id="ops-04"></a>
##### OPS-04 — Reliability & Production Operations

*Type:* Technical — Keeps services healthy; designs for failure.

- **[P1 — Assisted](proficiency_scale.md#p1):** Understands SLOs and common failure modes; keeps components healthy with guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds retries, timeouts and fallbacks; understands blast radius.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs for graceful degradation; defines SLOs; accountable for a domain's reliability.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert in resilience and capacity planning at scale; drives down incidents systemically.
- **[P5 — Authority](proficiency_scale.md#p5):** Owns org-level reliability; fixes risk in process and org design.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Sets the company's reliability philosophy.

<a id="ops-05"></a>
##### OPS-05 — Observability & Instrumentation

*Type:* Technical — Makes system behavior visible.

- **[P1 — Assisted](proficiency_scale.md#p1):** Understands logs/metrics/traces; reads existing dashboards.
- **[P2 — Independent](proficiency_scale.md#p2):** Instruments their services; builds dashboards; tunes alerts to limit noise.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs observability for complex systems (end-to-end traces, quality signals, cost attribution).
- **[P4 — Expert](proficiency_scale.md#p4):** Expert in instrumentation trade-offs at scale, incl. privacy-safe logging.
- **[P5 — Authority](proficiency_scale.md#p5):** Defines org observability strategy.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes company-wide operational visibility; advances practice.

<a id="ops-06"></a>
##### OPS-06 — Incident Response

*Type:* Technical — Responds to and learns from production incidents.

- **[P1 — Assisted](proficiency_scale.md#p1):** Responds to alerts with support; follows runbooks; escalates appropriately.
- **[P2 — Independent](proficiency_scale.md#p2):** Triages and resolves routine incidents; clear notes; takes on-call.
- **[P3 — Proficient](proficiency_scale.md#p3):** Leads response to complex failures; blameless postmortems; same failure never recurs.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert in incident-management design (rotations, severity, escalation).
- **[P5 — Authority](proficiency_scale.md#p5):** Commands the highest-severity incidents; sets incident process org-wide.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Sets the company's incident philosophy; calm authority in the worst moments.

<a id="ops-07"></a>
##### OPS-07 — Cost & Performance Optimization

*Type:* Technical — Keeps systems fast and economical.

- **[P1 — Assisted](proficiency_scale.md#p1):** Understands cost/latency drivers of what they build.
- **[P2 — Independent](proficiency_scale.md#p2):** Applies standard optimizations; stays within cost/latency budgets.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs cost-aware architectures; defines and tracks unit economics for a domain.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert in economics at scale (fleet optimization, build-vs-buy).
- **[P5 — Authority](proficiency_scale.md#p5):** Owns org-level spend strategy; cost decisions change margins.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes the company economics of the products.

#### Security

<a id="ops-08"></a>
##### OPS-08 — Application & Systems Security

*Type:* Technical — Builds secure-by-default systems.

- **[P1 — Assisted](proficiency_scale.md#p1):** Understands core appsec; follows practices and flags concerns.
- **[P2 — Independent](proficiency_scale.md#p2):** Applies least privilege; validates/sanitizes inputs; knows common attacks.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs defense in depth; thinks in abuse cases; owns a domain's posture.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert in securing systems at scale; leads red-teaming and remediation.
- **[P5 — Authority](proficiency_scale.md#p5):** Defines security strategy for the org's surface area.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Company-level accountability; authority on the field.

<a id="ops-09"></a>
##### OPS-09 — Privacy & Compliance Engineering

*Type:* Technical — Bakes privacy, audit and regulatory controls into systems.

- **[P1 — Assisted](proficiency_scale.md#p1):** Knows data handling has privacy implications; follows rules.
- **[P2 — Independent](proficiency_scale.md#p2):** Applies PII handling, redaction, residency and retention correctly.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs for compliance (consent, audit trails, regional rules); owns readiness for a domain.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert at translating regulation into controls; represents engineering in audits.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets org compliance strategy; anticipates regulation.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Authoritative on the landscape; trusted interface to regulators.

#### Provisioning & Configuration

<a id="ops-10"></a>
##### OPS-10 — Infrastructure as code & provisioning

*Type:* Technical — Define and version infrastructure declaratively to provision repeatable environments.

- **[P1 — Assisted](proficiency_scale.md#p1):** Writes simple declarative resource definitions from templates, applying them under review in non-production environments.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently provisions standard infrastructure stacks, manages state and variables, and handles routine drift with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs reusable modules for ambiguous needs, structures state safely, and is the go-to for tricky provisioning failures.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the provisioning patterns and module conventions others adopt, solving thorny dependency and idempotency problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the organization-wide IaC strategy, governance, and standards, anticipating shifts in declarative provisioning practice.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good infrastructure-as-code means for the field, shaping provisioning practices recognized across the industry.

<a id="ops-11"></a>
##### OPS-11 — Configuration management & desired-state enforcement

*Type:* Technical — Automate system configuration and continuously converge hosts to a defined target state.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies predefined configuration policies to hosts under supervision, verifying convergence against the declared desired state.
- **[P2 — Independent](proficiency_scale.md#p2):** Authors and maintains standard configuration definitions independently, remediating routine drift with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs idempotent configuration for ambiguous cases, manages secrets and ordering, and resolves hard convergence failures.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the configuration architecture and enforcement model others adopt, solving deep drift and idempotency problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets strategy for desired-state enforcement across the estate, anticipating where configuration management is heading.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines industry standards for desired-state enforcement, externally credible in shaping configuration practice.

<a id="ops-12"></a>
##### OPS-12 — Image & artifact building / golden baselines

*Type:* Technical — Produce hardened, reproducible machine and application images for consistent deployment.

- **[P1 — Assisted](proficiency_scale.md#p1):** Builds images from existing recipes under review, verifying contents match the documented baseline.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently maintains image build pipelines and updates baselines for routine patches and version changes.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs hardened, minimal golden images for ambiguous needs and resolves tricky reproducibility and provenance issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the baseline strategy and build conventions others adopt, solving layering, supply-chain, and drift problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide standards for image lifecycle and provenance, anticipating shifts in artifact-building practice.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what a trustworthy golden baseline means for the discipline, shaping industry artifact-integrity practice.

<a id="ops-13"></a>
##### OPS-13 — Environment & release promotion strategy

*Type:* Technical — Design promotion paths and parity across dev, staging, and production environments.

- **[P1 — Assisted](proficiency_scale.md#p1):** Promotes builds through predefined environment stages under review, following the documented gating checklist.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently manages standard promotion flows across environments, handling routine approvals and rollbacks with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs promotion paths and gates for ambiguous release scenarios, resolving hard environment-parity and rollback issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the promotion model and gating strategy others adopt, solving complex multi-stage and dependency problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide release-promotion strategy, anticipating how environment progression and gating should evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what disciplined release promotion means for the field, shaping industry environment-strategy practice.

#### Compute & Workload Orchestration

<a id="ops-14"></a>
##### OPS-14 — Container orchestration & scheduling

*Type:* Technical — Schedule, place, and manage containerized workloads across a cluster of compute nodes.

- **[P1 — Assisted](proficiency_scale.md#p1):** Deploys workloads to an existing orchestrator under review, adjusting basic scheduling settings from examples.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently operates orchestrated workloads, manages routine scaling, placement, and health checks with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs scheduling, affinity, and resource policies for ambiguous workloads and resolves hard orchestration failures.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines cluster topology and scheduling patterns others adopt, solving deep placement, contention, and lifecycle problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide orchestration strategy and standards, anticipating where workload scheduling is heading.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what effective orchestration means for the discipline, externally credible in shaping scheduling practice.

<a id="ops-15"></a>
##### OPS-15 — Containerization & workload packaging

*Type:* Technical — Package applications and dependencies into portable, isolated runtime units.

- **[P1 — Assisted](proficiency_scale.md#p1):** Packages applications into containers from existing recipes under review, verifying they run as expected.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently builds and maintains container images, managing dependencies and layers for routine workloads with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs minimal, secure, reproducible packaging for ambiguous workloads and resolves tricky runtime and size issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines packaging conventions and base-image strategy others adopt, solving deep build-efficiency and isolation problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide containerization standards, anticipating shifts in workload packaging and runtime practice.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good workload packaging means for the field, shaping industry containerization practice.

<a id="ops-16"></a>
##### OPS-16 — Capacity & autoscaling design

*Type:* Technical — Plan compute capacity and design elastic scaling to meet variable demand.

- **[P1 — Assisted](proficiency_scale.md#p1):** Adjusts capacity settings within defined limits under review, monitoring basic utilization against thresholds.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently configures standard autoscaling rules and capacity buffers, tuning routine thresholds with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs scaling policies and capacity models for ambiguous, bursty demand and resolves hard scaling-stability issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the capacity-planning and autoscaling approach others adopt, solving complex demand-prediction and cost-tradeoff problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide capacity strategy, anticipating demand shifts and how scaling design should evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what sound capacity and autoscaling design means for the discipline, shaping industry practice.

<a id="ops-17"></a>
##### OPS-17 — Operating system & host administration

*Type:* Technical — Administer, harden, and tune host operating systems and their runtime services.

- **[P1 — Assisted](proficiency_scale.md#p1):** Performs routine host tasks like updates and user setup under review, following documented procedures.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently administers hosts, manages packages, services, and permissions, troubleshooting routine issues with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Tunes and hardens hosts for ambiguous workloads and diagnoses hard kernel, resource, and performance problems.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines host-administration standards and hardening baselines others adopt, solving deep OS-level and tuning problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide host-management strategy, anticipating shifts in operating-system administration practice.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what excellent host administration means for the field, externally credible in shaping OS practice.

<a id="ops-18"></a>
##### OPS-18 — Storage & data persistence design

*Type:* Technical — Design block, object, and file storage for durability, performance, and access patterns.

- **[P1 — Assisted](proficiency_scale.md#p1):** Provisions and attaches storage from defined options under review, verifying capacity and access settings.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently manages storage volumes, snapshots, and routine persistence configuration with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs persistence schemes balancing durability, performance, and cost for ambiguous needs, resolving hard data-integrity issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines storage architecture and persistence patterns others adopt, solving deep consistency, replication, and performance problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide storage and persistence strategy, anticipating where data-durability design is heading.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what sound data-persistence design means for the discipline, shaping industry storage practice.

#### Networking & Connectivity

<a id="ops-19"></a>
##### OPS-19 — Network design & routing

*Type:* Technical — Architect network topologies, subnets, and routing for connectivity and segmentation.

- **[P1 — Assisted](proficiency_scale.md#p1):** Configures basic network segments and routes from designs under review, verifying connectivity.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently builds standard network topologies, manages routing and segmentation for routine needs with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs routing and addressing schemes for ambiguous topologies and diagnoses hard reachability and routing failures.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines network architecture and routing patterns others adopt, solving deep segmentation, scale, and convergence problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide network strategy and standards, anticipating shifts in network design and routing.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good network design means for the field, externally credible in shaping routing practice.

<a id="ops-20"></a>
##### OPS-20 — Load balancing & traffic management

*Type:* Technical — Distribute and shape traffic across endpoints for availability and performance.

- **[P1 — Assisted](proficiency_scale.md#p1):** Configures basic load-balancing rules from templates under review, verifying traffic reaches healthy targets.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently manages standard balancing, health checks, and routing rules for routine traffic with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs traffic-distribution and failover policies for ambiguous patterns and resolves hard balancing and session issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines traffic-management patterns others adopt, solving deep distribution, affinity, and graceful-degradation problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide traffic-management strategy, anticipating how load distribution and routing should evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what effective traffic management means for the discipline, shaping industry load-balancing practice.

<a id="ops-21"></a>
##### OPS-21 — DNS & service discovery

*Type:* Technical — Resolve names and dynamically locate services across distributed systems.

- **[P1 — Assisted](proficiency_scale.md#p1):** Creates and edits basic name records under review, verifying resolution behaves as documented.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently manages zones, records, and standard service-registration for routine needs with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs resolution and discovery schemes for ambiguous, dynamic environments and resolves hard propagation and caching issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines naming and discovery architecture others adopt, solving deep resolution, failover, and registration problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide naming and discovery strategy, anticipating shifts in service-discovery practice.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what robust naming and discovery means for the field, shaping industry DNS and discovery practice.

<a id="ops-22"></a>
##### OPS-22 — Network protocols & packet-level troubleshooting

*Type:* Technical — Diagnose connectivity using knowledge of layered protocols and packet behavior.

- **[P1 — Assisted](proficiency_scale.md#p1):** Captures traffic and reads basic protocol fields under guidance to confirm expected behavior.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently traces standard protocol exchanges and diagnoses routine connectivity faults from captures with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Dissects complex multi-layer exchanges for ambiguous faults and resolves hard latency, fragmentation, and handshake issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines packet-analysis methods others adopt, solving deep protocol-interaction and elusive intermittent-failure problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide troubleshooting standards and tooling direction, anticipating protocol-behavior challenges.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what rigorous packet-level diagnosis means for the discipline, externally credible in protocol practice.

<a id="ops-23"></a>
##### OPS-23 — Edge, CDN & content delivery

*Type:* Technical — Cache and serve content near users to reduce latency and origin load.

- **[P1 — Assisted](proficiency_scale.md#p1):** Configures basic caching and delivery rules from templates under review, verifying content serves correctly.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently manages edge caching, invalidation, and routing for routine content with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs delivery and caching strategies for ambiguous traffic and resolves hard cache-coherence and edge-routing issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines edge-delivery architecture others adopt, solving deep caching, origin-offload, and latency problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide content-delivery strategy, anticipating shifts in edge and distribution practice.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what excellent content delivery means for the field, shaping industry edge and CDN practice.

<a id="ops-24"></a>
##### OPS-24 — Secure connectivity & network perimeter

*Type:* Technical — Establish encrypted tunnels, gateways, and boundaries between trust zones.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies predefined firewall and tunnel rules under review, verifying allowed and blocked paths behave correctly.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently manages standard perimeter controls, secure tunnels, and segmentation rules with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs perimeter and encrypted-connectivity schemes for ambiguous needs and resolves hard isolation and access issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines perimeter architecture and secure-connectivity patterns others adopt, solving deep segmentation and trust problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide perimeter and secure-connectivity strategy, anticipating shifts in network-security practice.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what strong network perimeter design means for the discipline, externally credible in shaping practice.

#### Resilience & Continuity

<a id="ops-25"></a>
##### OPS-25 — Backup, DR & business continuity

*Type:* Technical — Plan backups, recovery objectives, and failover to survive disruptive events.

- **[P1 — Assisted](proficiency_scale.md#p1):** Runs scheduled backups and restore tests under review, verifying jobs complete and data is recoverable.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently manages backup schedules, retention, and routine restores, validating recovery points with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs backup and recovery schemes for ambiguous needs, meeting recovery objectives and resolving hard restore issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines continuity architecture and recovery patterns others adopt, solving deep cross-failure and dependency problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide continuity strategy and recovery objectives, anticipating evolving business-continuity needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what credible business continuity means for the discipline, shaping industry disaster-recovery practice.

<a id="ops-26"></a>
##### OPS-26 — High availability & fault-tolerance design

*Type:* Technical — Eliminate single points of failure through redundancy and graceful degradation.

- **[P1 — Assisted](proficiency_scale.md#p1):** Configures basic redundancy and failover from designs under review, verifying standby paths activate.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently builds standard redundant setups and failover behavior for routine services with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs availability schemes for ambiguous failure modes and resolves hard split-brain, quorum, and failover issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines fault-tolerance patterns others adopt, solving deep redundancy, isolation, and graceful-degradation problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide availability strategy and targets, anticipating where resilience design is heading.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what genuine fault tolerance means for the discipline, externally credible in shaping availability practice.

<a id="ops-27"></a>
##### OPS-27 — Platform & developer-experience engineering

*Type:* Technical — Build self-service internal platforms and paved paths that streamline delivery.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains existing self-service platform components under review, addressing documented user requests.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently builds and supports standard platform capabilities and templates for routine developer needs with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs self-service workflows for ambiguous needs, reducing friction and resolving hard abstraction and adoption issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines platform architecture and golden paths others adopt, solving deep developer-experience and leverage problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide platform strategy, anticipating how developer-experience engineering should evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what excellent platform engineering means for the field, shaping industry developer-experience practice.

#### Operating Mindset

<a id="ops-28"></a>
##### OPS-28 — Automation-first operations

*Type:* Behavioral — Default to eliminating toil by automating repetitive operational work.

- **[P1 — Assisted](proficiency_scale.md#p1):** Runs and lightly edits existing automation under review, flagging tasks that remain manual.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently automates routine operational tasks and integrates them into standard workflows with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs automation for ambiguous, error-prone toil and resolves hard reliability and orchestration issues in pipelines.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines automation patterns and toil-elimination practices others adopt, solving deep workflow and safety problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide automation strategy, anticipating where automation-first operations should head.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what automation-first operations means for the discipline, externally credible in shaping the practice.

<a id="ops-29"></a>
##### OPS-29 — Systems thinking & failure-mode reasoning

*Type:* Behavioral — Reason about emergent behavior and cascading failures across interdependent systems.

- **[P1 — Assisted](proficiency_scale.md#p1):** Traces simple cause-and-effect across components under guidance, identifying obvious failure points.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently maps standard system interactions and reasons through routine failure modes with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Analyzes emergent behavior and cascading failures in ambiguous systems, anticipating non-obvious failure interactions.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines failure-mode reasoning methods others adopt, solving deep systemic and feedback-loop problems others miss.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organization-wide approaches to systems reasoning, anticipating where complex-failure analysis is heading.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what rigorous systems thinking means for the discipline, externally credible in shaping the practice.

#### Operations

<a id="ops-30"></a>
##### OPS-30 — Progressive Delivery & Release Safety

*Type:* Technical — Manages how change reaches production safely — decoupling deploy from release with feature flags, staged and canary rollouts, rollback readiness, and migration sequencing that bounds the blast radius of every change.

- **[P1 — Assisted](proficiency_scale.md#p1):** Follows the release process exactly — flags, staged rollout steps, verification checklists — verifies their change in production, and rolls back with guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Ships behind flags with a rollback plan by default, monitors rollouts and reverts on their own judgment when signals degrade, and writes changes that tolerate both versions running during rollout.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs the rollout for risky changes — canary criteria, migration sequencing, flag lifecycle, kill switches — and reviews others' rollout plans for blast radius; the person teams ask how to ship something safely.
- **[P4 — Expert](proficiency_scale.md#p4):** Builds progressive-delivery machinery multiple teams release through (flag platforms, automated canary analysis, automated rollback), retiring deploy patterns that cause repeat incidents and measurably raising deploy frequency.
- **[P5 — Authority](proficiency_scale.md#p5):** Owns release policy for an organization and its delivery metrics — rollout standards, freeze rules, environment strategy — dismantling ceremony that adds no safety.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Sets how an entire company's software reaches customers — the risk posture products ship under — and defends it to executives, auditors, and regulators.

#### Operating Mindset

<a id="ops-31"></a>
##### OPS-31 — Thinnest viable platform scoping

*Type:* Behavioral — Scopes an internal platform to the smallest set of APIs, tools, docs, and services that accelerates its consumers - making explicit build-buy-adopt decisions and retiring surface area that no longer earns its maintenance cost.

- **[P1 — Assisted](proficiency_scale.md#p1):** Checks for an existing tool, service, or open-source option before writing new code and raises what they find; asks whether a proposed task serves a real user need.
- **[P2 — Independent](proficiency_scale.md#p2):** Proposes wrapping or configuring an existing service instead of building new when it meets the need, writing the comparison down and defending removal of unused features in their own component.
- **[P3 — Proficient](proficiency_scale.md#p3):** Keeps a whole capability at its thinnest viable size - makes explicit, documented build-buy-adopt decisions, ships the thinnest version that serves proven demand, and retires surface area whose maintenance cost exceeds its value.
- **[P4 — Expert](proficiency_scale.md#p4):** Arbitrates overlap and sprawl across teams - merges duplicate offerings, cuts under-used surface, and sets the bar for what deserves to be shared platform at all.
- **[P5 — Authority](proficiency_scale.md#p5):** Shapes the organization's platform boundary - what the platform owns versus product teams versus vendors - and drives the organization to shed what it should not own.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Sets the build-buy-adopt principles an entire company references, keeping company-scale platform investment proportional to the delivery it unlocks.

<a id="ops-32"></a>
##### OPS-32 — Cognitive-load management & abstraction design

*Type:* Behavioral — Designs tooling, interfaces, and abstractions to minimize the extraneous cognitive load imposed on the teams that consume them - deciding deliberately what consumers must and must not need to know, and measuring the load imposed.

- **[P1 — Assisted](proficiency_scale.md#p1):** Names the exact docs, errors, and setup steps that forced them to understand internals a consumer should not need, and files concrete simplification issues.
- **[P2 — Independent](proficiency_scale.md#p2):** Reduces the concepts and steps a consumer must hold to use their component - collapsing configuration, defaulting decisions, rewriting errors to say what to do next - and shows the before/after.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs a capability's abstractions around what consumers must not have to know, so a first-time user succeeds without reading internals; measures load with time-to-first-success and support-ticket themes and treats regressions as defects.
- **[P4 — Expert](proficiency_scale.md#p4):** Audits cognitive load across team boundaries - quantifying onboarding time, concepts-to-learn, and ticket themes - and drives the cross-boundary simplifications no single team could make.
- **[P5 — Authority](proficiency_scale.md#p5):** Makes cognitive load a first-class organizational measure with explicit load budgets, vetoing designs that externalize complexity onto consuming teams.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes company-level technology and team-boundary choices explicitly around team cognitive load, arguing for fewer, deeper abstractions over sprawling optionality.

### Security Engineering (SEC)

#### Identity & Access

<a id="sec-01"></a>
##### SEC-01 — Identity & access management

*Type:* Technical — Govern identities, authentication, and least-privilege authorization across systems.

- **[P1 — Assisted](proficiency_scale.md#p1):** Provisions and deprovisions accounts from documented procedures, with approvals and access reviewed before activation.
- **[P2 — Independent](proficiency_scale.md#p2):** Configures roles, group membership, and authentication factors independently for standard joiners, movers, and leavers.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves complex entitlement conflicts and designs least-privilege role models for ambiguous, cross-system access needs.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the identity lifecycle and authorization architecture that other engineers adopt across the organization.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets identity strategy, governs federation and privileged-access standards, and anticipates emerging access risks.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what sound identity practice means for the field and shapes how others govern access.

<a id="sec-02"></a>
##### SEC-02 — Secrets & key management

*Type:* Technical — Securely generate, store, rotate, and distribute credentials and keys.

- **[P1 — Assisted](proficiency_scale.md#p1):** Stores and retrieves secrets using approved vaults, following rotation and handling procedures under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Configures secret storage, rotation schedules, and access scoping independently for routine services.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs key hierarchies and rotation strategies for complex systems with conflicting availability and security constraints.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the secrets and key-management architecture and lifecycle others implement organization-wide.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets cryptographic-key governance and custody strategy and anticipates risks from emerging key threats.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative practice for secret and key stewardship that practitioners across the field adopt.

<a id="sec-03"></a>
##### SEC-03 — Cryptography & data protection

*Type:* Technical — Apply encryption, hashing, and key practices to protect data at rest and in transit.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies approved encryption settings and protects data following documented schemes, with choices reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Selects and configures standard cryptographic primitives and data-protection controls independently for common cases.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs encryption schemes and key-usage patterns for ambiguous threat and compliance trade-offs.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the cryptographic and data-protection patterns others reuse and resolves problems they cannot.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets cryptographic standards and migration strategy and anticipates shifts such as quantum-resistant needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what sound applied cryptography means for the discipline and influences industry data-protection norms.

<a id="sec-04"></a>
##### SEC-04 — Zero-trust & policy-based access control

*Type:* Technical — Enforce continuous, context-aware authorization rather than implicit network trust.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements access policies from defined rules, verifying identity and context before granting under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Authors and tests policy rules for standard resources, enforcing context-aware checks independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs segmentation and policy models that resolve ambiguous trust boundaries and hard exceptions.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the zero-trust architecture and policy framework other teams adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the organization's zero-trust strategy and anticipates how trust models must evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what mature zero-trust means for the field and shapes how the industry approaches it.

#### Defensive Security

<a id="sec-05"></a>
##### SEC-05 — Threat modeling

*Type:* Technical — Systematically identify assets, threats, and attack surfaces to guide defenses.

- **[P1 — Assisted](proficiency_scale.md#p1):** Documents assets, entry points, and obvious threats for a component using a guided method, reviewed by others.
- **[P2 — Independent](proficiency_scale.md#p2):** Produces complete threat models for standard systems independently, identifying realistic threats and mitigations.
- **[P3 — Proficient](proficiency_scale.md#p3):** Models complex, ambiguous architectures and prioritizes subtle, chained threats others miss.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the threat-modeling methodology and reusable patterns others adopt across teams.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets threat-modeling strategy and anticipates classes of threats before they become prevalent.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative threat-modeling practice that shapes how the discipline reasons about risk.

<a id="sec-06"></a>
##### SEC-06 — Vulnerability management & remediation

*Type:* Technical — Discover, prioritize, and drive remediation of weaknesses across the estate.

- **[P1 — Assisted](proficiency_scale.md#p1):** Triages and tracks scanner findings, verifying fixes against documented severity and remediation steps.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently validates, prioritizes, and coordinates remediation for routine vulnerabilities through closure.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves ambiguous, hard-to-reproduce, or high-impact vulnerabilities and sets local remediation standards.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the vulnerability-management lifecycle and prioritization approach others follow.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise remediation strategy and anticipates exposure trends across the portfolio.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what effective vulnerability management means for the field and influences its practice.

<a id="sec-07"></a>
##### SEC-07 — Security monitoring & detection

*Type:* Technical — Collect, correlate, and alert on signals to detect malicious activity.

- **[P1 — Assisted](proficiency_scale.md#p1):** Monitors alerts and triages events against documented playbooks, escalating uncertain cases for review.
- **[P2 — Independent](proficiency_scale.md#p2):** Tunes detections and investigates standard alerts independently, reducing routine false positives.
- **[P3 — Proficient](proficiency_scale.md#p3):** Authors high-fidelity detections for novel and ambiguous adversary behavior across noisy signals.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines detection engineering methods and coverage strategy that other analysts adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets monitoring and detection strategy and anticipates evasion techniques before they appear.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative detection practice and shapes how the discipline approaches monitoring.

<a id="sec-08"></a>
##### SEC-08 — Security hardening & baseline configuration

*Type:* Technical — Reduce attack surface by applying secure configuration standards to systems.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies hardening baselines from checklists and verifies configurations against documented standards.
- **[P2 — Independent](proficiency_scale.md#p2):** Hardens standard systems independently and adapts baselines to routine configuration variation.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs hardening baselines for complex systems, balancing security against operational constraints.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the hardening standards and reusable baselines other teams adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets configuration-security strategy and anticipates hardening needs for emerging platforms.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what authoritative hardening practice means for the field and influences accepted baselines.

<a id="sec-09"></a>
##### SEC-09 — Supply-chain & artifact security

*Type:* Technical — Verify provenance and integrity of dependencies, builds, and deployed artifacts.

- **[P1 — Assisted](proficiency_scale.md#p1):** Verifies artifact provenance and signatures following documented checks, escalating anomalies for review.
- **[P2 — Independent](proficiency_scale.md#p2):** Configures signing, dependency scanning, and provenance controls independently for standard pipelines.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs artifact-integrity and dependency-trust controls for complex, ambiguous supply chains.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the supply-chain security architecture and verification patterns others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets supply-chain assurance strategy and anticipates emerging artifact and dependency threats.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative supply-chain security practice that shapes industry expectations.

<a id="sec-10"></a>
##### SEC-10 — Digital forensics & malware analysis

*Type:* Technical — Investigate compromises by analyzing artifacts, evidence, and malicious code.

- **[P1 — Assisted](proficiency_scale.md#p1):** Collects and preserves evidence following chain-of-custody procedures, with analysis reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Conducts standard forensic examinations and basic malware triage independently, documenting findings.
- **[P3 — Proficient](proficiency_scale.md#p3):** Reconstructs complex incidents and reverse-engineers obfuscated samples others cannot interpret.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines forensic and analysis methodologies and tooling approaches others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets investigative strategy and anticipates evolving anti-forensic and malware techniques.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative forensic and malware-analysis practice that shapes the discipline.

#### Offensive Security

<a id="sec-11"></a>
##### SEC-11 — Penetration testing & offensive security

*Type:* Technical — Emulate adversaries to find and demonstrate exploitable weaknesses.

- **[P1 — Assisted](proficiency_scale.md#p1):** Executes scoped test cases under guidance, documenting findings against an approved methodology.
- **[P2 — Independent](proficiency_scale.md#p2):** Conducts standard penetration tests independently and reports exploitable findings with clear evidence.
- **[P3 — Proficient](proficiency_scale.md#p3):** Chains subtle weaknesses into impactful attacks in ambiguous, well-defended environments.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines testing methodology and tradecraft that other testers adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets offensive-testing strategy and anticipates attack surfaces before they are widely understood.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what rigorous offensive testing means for the field and influences its practice.

<a id="sec-12"></a>
##### SEC-12 — Adversarial testing of AI systems / red teaming

*Type:* Technical — Probe AI systems for jailbreaks, prompt injection, and unsafe or harmful behavior.

- **[P1 — Assisted](proficiency_scale.md#p1):** Runs predefined adversarial prompts and probes, recording model failures under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs and executes standard adversarial tests independently, documenting reproducible weaknesses.
- **[P3 — Proficient](proficiency_scale.md#p3):** Discovers novel, ambiguous failure modes and bypasses in well-guarded AI systems.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines AI red-teaming methodology and evaluation patterns others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets adversarial-AI testing strategy and anticipates emerging model attack classes.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative AI red-teaming practice that shapes how the field tests AI safety.

<a id="sec-13"></a>
##### SEC-13 — Exploit development & weakness research

*Type:* Technical — Research and weaponize flaws to validate real-world exploitability.

- **[P1 — Assisted](proficiency_scale.md#p1):** Reproduces known weaknesses and adapts existing proof-of-concepts under close review.
- **[P2 — Independent](proficiency_scale.md#p2):** Develops reliable exploits for standard, documented weakness classes independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Discovers and weaponizes novel weaknesses in hardened targets others cannot crack.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines research techniques and exploitation primitives other researchers adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets weakness-research direction and anticipates new exploitation classes ahead of the field.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative exploit-research practice and shapes the discipline's frontier.

<a id="sec-14"></a>
##### SEC-14 — Social engineering & human-factor testing

*Type:* Technical — Assess susceptibility to manipulation through pretexting and phishing simulations.

- **[P1 — Assisted](proficiency_scale.md#p1):** Executes approved phishing or pretext scripts under supervision and records target responses.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs and runs standard social-engineering campaigns independently within agreed rules of engagement.
- **[P3 — Proficient](proficiency_scale.md#p3):** Crafts convincing, context-aware pretexts that succeed against security-aware, ambiguous targets.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines human-factor testing methodology and ethical guardrails others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets human-factor testing strategy and anticipates evolving manipulation techniques.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative human-factor testing practice that shapes the discipline.

#### Governance & Mindset

<a id="sec-15"></a>
##### SEC-15 — Security governance, risk & policy

*Type:* Technical — Frame risk, controls, and policy to align security with organizational obligations.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains policy documents and risk-register entries following templates, reviewed before publication.
- **[P2 — Independent](proficiency_scale.md#p2):** Drafts standard policies and assesses routine risks independently against established frameworks.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves ambiguous risk trade-offs and tailors governance for complex, contested contexts.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the governance and risk frameworks other teams adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise security governance strategy and anticipates regulatory and risk shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what sound security governance means for the field and influences external standards.

<a id="sec-16"></a>
##### SEC-16 — Adversarial mindset & ethical conduct

*Type:* Behavioral — Think like an attacker while operating within legal and ethical boundaries.

- **[P1 — Assisted](proficiency_scale.md#p1):** Questions assumptions on prompting and follows ethical and authorization rules under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently spots realistic abuse cases and consistently operates within ethical boundaries.
- **[P3 — Proficient](proficiency_scale.md#p3):** Anticipates subtle attacker reasoning in ambiguous situations while modeling sound ethical judgment.
- **[P4 — Expert](proficiency_scale.md#p4):** Teaches adversarial thinking and ethical decision-making that others adopt as their model.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the standard for ethical adversarial practice and anticipates emerging ethical dilemmas.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what principled adversarial conduct means for the discipline and shapes its norms.

<a id="sec-17"></a>
##### SEC-17 — Security awareness & shift-left advocacy

*Type:* Behavioral — Champion secure practices early and embed security into everyday engineering.

- **[P1 — Assisted](proficiency_scale.md#p1):** Delivers prepared awareness material and flags security concerns early under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Tailors awareness content and embeds standard secure practices into routine team workflows independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Drives security adoption in resistant, ambiguous contexts and sets the local shift-left standard.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines awareness and shift-left programs other teams adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the organization's security-culture strategy and anticipates shifts in developer behavior.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what effective security culture means for the field and influences how it is fostered.

#### Defensive Security

<a id="sec-18"></a>
##### SEC-18 — Guardrails & policy as code

*Type:* Technical — Encodes preventive controls as versioned, tested, automatically enforced policy - admission checks, pipeline gates, configuration rules - with actionable violation messages and governed exception paths, so the safe way is the default way.

- **[P1 — Assisted](proficiency_scale.md#p1):** Works within existing guardrails, reads a policy violation to its cause instead of requesting an exception, and explains what each guardrail protects against.
- **[P2 — Independent](proficiency_scale.md#p2):** Writes and tests policy rules for a component - admission checks, pipeline gates - with low false-positive rates and violation messages that tell the user how to comply.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs the guardrail architecture for a capability - what is blocked, warned, or audited, with documented threat reasoning - tuned so the safe path is the fast path, and runs an audited exception workflow without becoming the bottleneck.
- **[P4 — Expert](proficiency_scale.md#p4):** Harmonizes policy across teams into a coherent, versioned policy library with a governed exception process, and adjudicates escalated safety-versus-velocity disputes.
- **[P5 — Authority](proficiency_scale.md#p5):** Owns an organization's preventive-control strategy with security partners - the control catalog, its coverage, and the evidence it works - moving enforcement from review-time to platform-time.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Sets an organization-defining balance of enablement and control, accountable for guardrails that hold under audit and attack without throttling delivery.

### Quality Engineering & Test (QA)

#### Test Strategy & Design

<a id="qa-01"></a>
##### QA-01 — Test strategy & planning

*Type:* Technical — Defining test scope, levels, priorities, and coverage goals aligned to risk and product objectives.

- **[P1 — Assisted](proficiency_scale.md#p1):** Drafts test plans from templates for defined features, reviewed before execution.
- **[P2 — Independent](proficiency_scale.md#p2):** Produces complete test strategies for standard projects independently, scoping coverage and risk.
- **[P3 — Proficient](proficiency_scale.md#p3):** Devises test strategies for ambiguous, high-risk programs balancing coverage, time, and cost.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the test-strategy approach and planning patterns other teams adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organizational quality strategy and anticipates how testing must evolve with delivery.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what effective test strategy means for the discipline and influences its practice.

<a id="qa-02"></a>
##### QA-02 — Test case design & techniques

*Type:* Technical — Deriving effective test cases using equivalence, boundary, decision-table, and state-based techniques.

- **[P1 — Assisted](proficiency_scale.md#p1):** Writes test cases from clear requirements using prescribed techniques, reviewed for coverage.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs effective test cases independently, applying standard techniques to cover routine variation.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs minimal, high-yield cases for ambiguous requirements and complex condition combinations.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines case-design techniques and reusable patterns others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets case-design standards and anticipates techniques needed for new system classes.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative test-design practice that shapes how the discipline designs tests.

<a id="qa-03"></a>
##### QA-03 — Exploratory & manual testing

*Type:* Technical — Unscripted investigative testing to uncover defects, usability issues, and unspecified behaviors.

- **[P1 — Assisted](proficiency_scale.md#p1):** Executes guided exploratory sessions and reports defects clearly under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs self-directed exploratory sessions independently, uncovering issues beyond scripted cases.
- **[P3 — Proficient](proficiency_scale.md#p3):** Uncovers subtle, high-impact defects in ambiguous areas through skilled exploratory charters.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines exploratory methods and charters others adopt to find what scripts miss.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets exploratory-testing strategy and anticipates where investigative effort yields most value.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative exploratory practice that shapes how the discipline explores quality.

<a id="qa-04"></a>
##### QA-04 — Risk-based & shift-left quality

*Type:* Behavioral — Prioritizing quality effort by risk and embedding testing early across the delivery lifecycle.

- **[P1 — Assisted](proficiency_scale.md#p1):** Identifies obvious quality risks and contributes early-stage checks under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Prioritizes routine testing by risk and embeds standard quality checks early independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Drives risk-based focus across ambiguous, high-stakes work and sets the local shift-left standard.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the risk-based and shift-left approach other teams adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organizational risk-based quality strategy and anticipates where quality must move earlier.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what mature shift-left quality means for the field and influences its adoption.

#### Test Automation

<a id="qa-05"></a>
##### QA-05 — Test automation architecture

*Type:* Technical — Designing maintainable, layered automation frameworks and reusable test infrastructure.

- **[P1 — Assisted](proficiency_scale.md#p1):** Adds tests to an existing automation framework following established patterns under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds and extends automation suites independently using sound, maintainable structure.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs resilient automation frameworks for complex, ambiguous systems and flaky conditions.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the automation architecture and patterns other engineers adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets automation strategy and anticipates architectural needs as systems and pipelines evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative test-automation architecture that shapes how the discipline builds it.

<a id="qa-06"></a>
##### QA-06 — UI & end-to-end automation

*Type:* Technical — Automating user-facing flows reliably across interfaces while minimizing flakiness.

- **[P1 — Assisted](proficiency_scale.md#p1):** Automates defined UI flows using existing patterns, with scripts reviewed for reliability.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds and maintains stable end-to-end UI tests independently for standard journeys.
- **[P3 — Proficient](proficiency_scale.md#p3):** Stabilizes flaky, complex end-to-end flows and designs resilient locator and wait strategies.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines UI and end-to-end automation patterns others adopt for reliability at scale.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets end-to-end automation strategy and anticipates challenges from evolving interfaces.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative end-to-end automation practice that shapes the discipline.

<a id="qa-07"></a>
##### QA-07 — API & service-level testing

*Type:* Technical — Validating contracts, integrations, and service behavior below the user interface.

- **[P1 — Assisted](proficiency_scale.md#p1):** Executes and extends API tests from examples, validating responses under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs and automates service-level tests independently for standard contracts and flows.
- **[P3 — Proficient](proficiency_scale.md#p3):** Tests complex service interactions, contracts, and edge behaviors in ambiguous integrations.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines service-testing and contract-verification patterns others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets service-level testing strategy and anticipates needs as service architectures evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative service-testing practice that shapes how the discipline tests services.

<a id="qa-08"></a>
##### QA-08 — Continuous testing in delivery pipelines

*Type:* Technical — Integrating automated quality gates into build and deployment pipelines for fast feedback.

- **[P1 — Assisted](proficiency_scale.md#p1):** Adds tests to existing pipeline stages following defined configuration, reviewed before merge.
- **[P2 — Independent](proficiency_scale.md#p2):** Integrates and maintains automated test stages independently within standard pipelines.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs fast, reliable test gating for complex pipelines balancing speed and confidence.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines continuous-testing patterns and gating strategy other teams adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets continuous-testing strategy and anticipates how quality gates must evolve with delivery.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative continuous-testing practice that shapes the discipline.

#### Specialized Testing

<a id="qa-09"></a>
##### QA-09 — Performance & load testing

*Type:* Technical — Assessing responsiveness, throughput, and stability under expected and peak demand.

- **[P1 — Assisted](proficiency_scale.md#p1):** Runs predefined performance scenarios and records results against documented thresholds.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs and executes standard load tests independently, identifying obvious bottlenecks.
- **[P3 — Proficient](proficiency_scale.md#p3):** Diagnoses subtle performance issues under realistic, ambiguous load and contention conditions.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines performance-testing methodology and modeling approaches others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets performance-engineering strategy and anticipates scaling limits before they bite.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative performance-testing practice that shapes how the discipline measures it.

<a id="qa-10"></a>
##### QA-10 — Security & vulnerability testing

*Type:* Technical — Probing systems for weaknesses, misconfigurations, and exploitable flaws.

- **[P1 — Assisted](proficiency_scale.md#p1):** Runs prescribed security test cases and reports findings against documented criteria under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Conducts standard security and vulnerability tests independently, validating common weaknesses.
- **[P3 — Proficient](proficiency_scale.md#p3):** Uncovers subtle security defects in ambiguous flows and chains them into meaningful risk.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines security-testing methods integrated into quality practice that others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets security-testing strategy within quality and anticipates emerging weakness classes.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative security-in-quality practice that shapes the discipline.

<a id="qa-11"></a>
##### QA-11 — Accessibility & compatibility testing

*Type:* Technical — Verifying inclusive usability and consistent behavior across devices, platforms, and assistive tech.

- **[P1 — Assisted](proficiency_scale.md#p1):** Runs prescribed accessibility and compatibility checks, reporting issues against standards under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Tests standard accessibility and cross-environment compatibility independently against guidelines.
- **[P3 — Proficient](proficiency_scale.md#p3):** Diagnoses subtle accessibility and compatibility defects across ambiguous, diverse contexts.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines accessibility and compatibility testing approaches other teams adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets inclusive-quality strategy and anticipates accessibility needs across emerging contexts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative accessibility-testing practice that shapes how the discipline approaches it.

#### Quality Operations

<a id="qa-12"></a>
##### QA-12 — Test data & environment management

*Type:* Technical — Provisioning, masking, and maintaining realistic data and stable environments for testing.

- **[P1 — Assisted](proficiency_scale.md#p1):** Provisions test data and environments from documented procedures under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages standard test data and environments independently, ensuring consistent, valid conditions.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs reliable, representative data and environment strategies for complex, ambiguous needs.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines test-data and environment-management patterns other teams adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets data and environment strategy and anticipates needs as systems and privacy demands evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative test-data and environment practice that shapes the discipline.

<a id="qa-13"></a>
##### QA-13 — Defect lifecycle management

*Type:* Behavioral — Tracking, triaging, prioritizing, and driving defects to resolution with clear reporting.

- **[P1 — Assisted](proficiency_scale.md#p1):** Logs and updates defects with clear detail following the defined workflow under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages defects independently through triage, prioritization, and verification for routine cases.
- **[P3 — Proficient](proficiency_scale.md#p3):** Drives resolution of ambiguous, cross-team defects and sets the local quality bar for reporting.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the defect-management workflow and triage approach others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets defect-management strategy and anticipates trends from defect patterns.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative defect-lifecycle practice that shapes how the discipline manages defects.

<a id="qa-14"></a>
##### QA-14 — Quality metrics & reporting

*Type:* Behavioral — Measuring coverage, escape rates, and quality trends to inform release decisions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Compiles defined quality metrics into standard reports under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Produces meaningful quality reports independently, selecting relevant metrics for routine needs.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs metrics that reveal real quality signals in ambiguous, contested contexts.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the quality-metrics framework and reporting patterns others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets quality-measurement strategy and anticipates which signals will matter as delivery evolves.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what meaningful quality measurement means for the field and influences its practice.

### Game Development (GAME)

#### Engine & Runtime

<a id="game-01"></a>
##### GAME-01 — Game loop & real-time simulation

*Type:* Technical — Structuring frame-driven update, timing, and state progression for real-time interactivity.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements update steps within an existing loop on guided, well-scoped tasks under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds standard fixed/variable timestep loops independently, handling routine frame-timing variation.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns the simulation loop autonomously, resolving timing, ordering, and determinism edge cases.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the loop architecture and update model others adopt across systems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets simulation-timing strategy and standards, anticipating scaling and platform shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what robust real-time simulation means for the field and influences industry practice.

<a id="game-02"></a>
##### GAME-02 — Physics & collision systems

*Type:* Technical — Modeling motion, forces, and collision detection and response for believable interaction.

- **[P1 — Assisted](proficiency_scale.md#p1):** Adds colliders and tunes parameters on defined tasks with reviewed results.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard collision detection and response independently for routine cases.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves tunneling, stacking, and stability issues autonomously across hard scenarios.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the physics solver and broadphase approach others build on.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets physics-fidelity and performance strategy, anticipating new simulation demands.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for game physics recognized beyond their organization.

<a id="game-03"></a>
##### GAME-03 — Graphics & rendering fundamentals

*Type:* Technical — Translating scenes into rendered frames via pipelines, shading, lighting, and cameras.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements basic draw calls and material settings on guided tasks under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds standard render passes and shading independently for routine scenes.
- **[P3 — Proficient](proficiency_scale.md#p3):** Diagnoses and fixes rendering artifacts and pipeline issues autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Architects the rendering pipeline and techniques others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets rendering strategy and quality standards, anticipating hardware and technique shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines rendering best practice and advances the discipline externally.

<a id="game-04"></a>
##### GAME-04 — Spatial math & geometry

*Type:* Technical — Applying vectors, matrices, and transforms for movement, orientation, and spatial reasoning.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies provided vector and matrix operations to well-defined tasks under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently solves standard transform, projection, and intersection problems.
- **[P3 — Proficient](proficiency_scale.md#p3):** Handles tricky spatial math—quaternions, edge cases, numerical stability—autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Devises geometric algorithms and conventions others reuse.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets spatial-math standards and anticipates emerging geometric techniques.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes how the field reasons about spatial math and geometry.

#### Gameplay & Design

<a id="game-05"></a>
##### GAME-05 — Gameplay systems & mechanics design

*Type:* Technical — Designing and implementing rules, controls, and feedback loops that drive player experience.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements specified mechanics within an existing system under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds standard gameplay systems independently with normal iteration.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs and tunes cohesive mechanics autonomously, resolving balance and feel ambiguity.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines systemic design patterns and frameworks other designers adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets gameplay-design direction and standards, anticipating player and genre shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what great mechanics design means and influences the craft broadly.

<a id="game-06"></a>
##### GAME-06 — Game AI & behavior systems

*Type:* Technical — Building agent decision-making, pathfinding, and reactive behaviors for non-player entities.

- **[P1 — Assisted](proficiency_scale.md#p1):** Wires up provided behaviors and parameters on guided tasks under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard behavior trees or state machines independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Crafts believable, performant agent behavior autonomously across hard cases.
- **[P4 — Expert](proficiency_scale.md#p4):** Architects the AI behavior framework others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets game-AI strategy and standards, anticipating new behavioral techniques.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for game AI recognized across the industry.

<a id="game-07"></a>
##### GAME-07 — Audio & feedback integration

*Type:* Technical — Integrating sound, music, and sensory feedback to reinforce gameplay and immersion.

- **[P1 — Assisted](proficiency_scale.md#p1):** Hooks up provided sounds and feedback cues on defined tasks under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard audio triggers and feedback layers independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs cohesive audio-feedback systems autonomously, resolving timing and mix edge cases.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the feedback and audio integration approach others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets audio-feedback strategy and standards, anticipating immersion trends.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines excellence in game audio-feedback integration for the field.

#### Content & Production

<a id="game-08"></a>
##### GAME-08 — Game asset pipeline

*Type:* Technical — Authoring, importing, and optimizing art, models, and animation through production workflows.

- **[P1 — Assisted](proficiency_scale.md#p1):** Imports and configures assets through an existing pipeline under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds and maintains standard pipeline steps independently for routine assets.
- **[P3 — Proficient](proficiency_scale.md#p3):** Diagnoses and optimizes pipeline bottlenecks and edge-case assets autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Architects the asset pipeline and conventions others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets pipeline strategy and standards, anticipating tooling and scale shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines asset-pipeline best practice recognized beyond their organization.

<a id="game-09"></a>
##### GAME-09 — Level design & content authoring

*Type:* Technical — Crafting spaces, pacing, and encounters that shape player progression and challenge.

- **[P1 — Assisted](proficiency_scale.md#p1):** Builds level sections to spec using existing tools under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Authors complete standard levels independently with normal iteration.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs compelling pacing, flow, and layout autonomously across hard content.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines level-design patterns and authoring standards others follow.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets content-design direction, anticipating player-experience and tooling shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what great level design means and influences the craft widely.

#### Online & Backend

<a id="game-10"></a>
##### GAME-10 — Multiplayer networking & netcode

*Type:* Technical — Synchronizing state across clients with replication, prediction, and latency compensation.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements specified replication on an existing netcode layer under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds standard state sync and messaging independently for routine cases.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves latency, prediction, and reconciliation problems autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Architects the netcode model others adopt for synchronization.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets networking strategy and standards, anticipating scale and topology shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines netcode best practice recognized across the industry.

<a id="game-11"></a>
##### GAME-11 — Game server & live operations

*Type:* Technical — Running authoritative servers, matchmaking, sessions, and persistent live-service backends.

- **[P1 — Assisted](proficiency_scale.md#p1):** Performs defined live-ops and server tasks under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Operates and maintains game servers independently for routine events.
- **[P3 — Proficient](proficiency_scale.md#p3):** Diagnoses live incidents and scales services autonomously under pressure.
- **[P4 — Expert](proficiency_scale.md#p4):** Architects the live-service and operations approach others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets live-ops strategy and reliability standards, anticipating demand shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines live-operations best practice recognized beyond their organization.

<a id="game-12"></a>
##### GAME-12 — Performance optimization & profiling

*Type:* Technical — Diagnosing and tuning frame rate, memory, and resource use for target platforms.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies suggested optimizations and reads profiles on guided tasks under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Profiles and fixes standard bottlenecks independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Diagnoses and resolves complex performance issues autonomously across systems.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines profiling methodology and optimization patterns others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets performance strategy and budgets, anticipating platform constraints.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines performance-engineering best practice for the field.

### Blockchain & Web3 (WEB3)

#### Protocol Foundations

<a id="web3-01"></a>
##### WEB3-01 — Consensus & protocol fundamentals

*Type:* Technical — Understanding distributed agreement, block production, and protocol-level trust mechanisms.

- **[P1 — Assisted](proficiency_scale.md#p1):** Explains and configures protocol parameters on defined tasks under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard protocol logic independently for routine changes.
- **[P3 — Proficient](proficiency_scale.md#p3):** Reasons about consensus safety, liveness, and edge cases autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs consensus mechanisms and protocol approaches others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets protocol-design strategy and standards, anticipating emerging models.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines consensus best practice and shapes protocol research broadly.

<a id="web3-02"></a>
##### WEB3-02 — Applied cryptography & key management

*Type:* Technical — Applying hashing, signatures, and asymmetric cryptography to secure on-chain identity and data.

- **[P1 — Assisted](proficiency_scale.md#p1):** Uses provided cryptographic primitives correctly on guided tasks under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard signing, hashing, and key handling independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves subtle cryptographic and key-lifecycle issues autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs cryptographic schemes and key-management approaches others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets applied-crypto strategy and standards, anticipating threat shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines applied cryptography best practice recognized across the industry.

<a id="web3-03"></a>
##### WEB3-03 — Scalability & interoperability design

*Type:* Technical — Designing layered scaling and cross-chain communication to extend throughput and reach.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements specified scaling or bridging components under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds standard scaling and interoperability features independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves throughput, finality, and cross-system trust trade-offs autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Architects scalability and interoperability designs others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets scaling and interoperability strategy, anticipating ecosystem shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for scalable, interoperable systems across the field.

#### Smart Contracts

<a id="web3-04"></a>
##### WEB3-04 — Smart contract design

*Type:* Technical — Architecting deterministic on-chain logic with correct state, upgrade, and gas considerations.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements specified contract logic with reviewed results.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds standard contracts independently, handling routine requirements.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs robust, gas-aware contract architectures autonomously across hard cases.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines contract design patterns and standards others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets smart-contract design strategy, anticipating language and pattern shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines smart-contract design best practice recognized industry-wide.

<a id="web3-05"></a>
##### WEB3-05 — On-chain security & auditing

*Type:* Technical — Identifying and mitigating contract vulnerabilities through review, testing, and formal analysis.

- **[P1 — Assisted](proficiency_scale.md#p1):** Runs provided checks and flags obvious issues under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Audits standard contracts independently, identifying common vulnerabilities.
- **[P3 — Proficient](proficiency_scale.md#p3):** Uncovers subtle, novel vulnerabilities and exploit paths autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines audit methodology and threat models others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets on-chain security strategy and standards, anticipating attack trends.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines on-chain security best practice recognized across the industry.

<a id="web3-06"></a>
##### WEB3-06 — Decentralized application integration

*Type:* Technical — Connecting interfaces and off-chain services to on-chain logic via nodes, wallets, and oracles.

- **[P1 — Assisted](proficiency_scale.md#p1):** Wires up provided on-chain calls in an app under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Integrates standard contract interactions and wallets independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves state-sync, signing, and failure-mode issues autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Architects dApp integration patterns others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets integration strategy and standards, anticipating ecosystem shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines decentralized-app integration best practice for the field.

#### Economics & Custody

<a id="web3-07"></a>
##### WEB3-07 — Tokenomics & on-chain economics

*Type:* Technical — Designing token incentives, supply mechanics, and economic models for sustainable networks.

- **[P1 — Assisted](proficiency_scale.md#p1):** Models specified token parameters under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs standard token mechanics and incentives independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs sound incentive and supply systems autonomously, resolving economic edge cases.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines tokenomic frameworks and modeling approaches others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets on-chain economic strategy, anticipating market and mechanism shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines tokenomics best practice recognized across the industry.

<a id="web3-08"></a>
##### WEB3-08 — Wallet & key custody

*Type:* Technical — Securing private keys, signing flows, and asset custody for users and institutions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Configures provided custody and wallet flows under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Implements standard custody and signing flows independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves recovery, multi-party, and key-lifecycle challenges autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs custody architectures and policies others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets custody strategy and security standards, anticipating threat shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines key-custody best practice recognized beyond their organization.

## Product, Design & Cross-functional

### UX & Product Design (UX)

#### User Research & Insight

<a id="ux-01"></a>
##### UX-01 — User research & usability evaluation

*Type:* Behavioral — Planning and conducting research and usability testing to uncover user needs and validate designs.

- **[P1 — Assisted](proficiency_scale.md#p1):** Runs scripted sessions and notes observations under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Plans and conducts standard studies independently, synthesizing routine findings.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs rigorous research and extracts hard insights autonomously across ambiguity.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines research methods and evaluation frameworks others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets research strategy and standards, anticipating where inquiry must head.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines user-research best practice recognized across the discipline.

<a id="ux-02"></a>
##### UX-02 — Information architecture & content structuring

*Type:* Technical — Organizing content and navigation into coherent structures that match user mental models.

- **[P1 — Assisted](proficiency_scale.md#p1):** Organizes content into provided structures under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds standard navigation and taxonomies independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Structures complex, ambiguous content domains autonomously into coherent models.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines IA patterns and structuring methods others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets information-architecture strategy, anticipating content and scale shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines IA best practice recognized across the discipline.

#### Interaction & Visual Design

<a id="ux-03"></a>
##### UX-03 — Interaction & flow design

*Type:* Technical — Designing task flows, states, and interaction patterns that make products intuitive and efficient.

- **[P1 — Assisted](proficiency_scale.md#p1):** Builds specified flows and interactions under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs standard end-to-end flows independently with normal iteration.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves complex, ambiguous interaction problems autonomously with strong judgment.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines interaction patterns and flow frameworks others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets interaction-design direction, anticipating behavioral and modality shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines interaction-design best practice recognized across the discipline.

<a id="ux-04"></a>
##### UX-04 — Visual & layout design

*Type:* Technical — Applying typography, color, spacing, and composition to create clear, appealing visual hierarchy.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies provided styles and layouts to defined screens under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Produces standard, consistent visual layouts independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Crafts strong hierarchy, rhythm, and polish autonomously across hard cases.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines visual language and layout systems others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets visual-design direction and standards, anticipating aesthetic shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines visual-design excellence recognized across the discipline.

<a id="ux-05"></a>
##### UX-05 — Prototyping & design validation

*Type:* Technical — Creating prototypes at varied fidelity to explore, communicate, and test design concepts.

- **[P1 — Assisted](proficiency_scale.md#p1):** Builds simple prototypes from specs under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Creates standard interactive prototypes and runs basic validation independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs prototypes that answer hard questions and validates rigorously autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines prototyping and validation methods others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets validation strategy and standards, anticipating new fidelity needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines prototyping-and-validation best practice for the discipline.

<a id="ux-06"></a>
##### UX-06 — Inclusive & accessible design

*Type:* Technical — Designing experiences usable by people with diverse abilities, contexts, and assistive needs.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies provided accessibility guidelines on defined tasks under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs to standard accessibility requirements independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves complex inclusion and accessibility trade-offs autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines inclusive-design practices and standards others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets accessibility strategy, anticipating regulatory and inclusion shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines inclusive-design best practice recognized across the discipline.

#### Design Systems

<a id="ux-07"></a>
##### UX-07 — Design tokens & system governance

*Type:* Technical — Defining tokenized design foundations and governing a shared system for consistency at scale.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies existing tokens and follows governance rules under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Maintains and extends token sets independently within standard governance.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves token-architecture and governance conflicts autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines token structures and governance models others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets token and governance strategy, anticipating scale and theming needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines design-token and governance best practice across the discipline.

<a id="ux-08"></a>
##### UX-08 — Component library & pattern curation

*Type:* Technical — Curating reusable design components and patterns with usage guidance and maintenance over time.

- **[P1 — Assisted](proficiency_scale.md#p1):** Uses and documents existing components under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds and maintains standard components and patterns independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Curates a coherent, reusable library autonomously, resolving pattern conflicts.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines component and pattern standards others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets library strategy and curation standards, anticipating product needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines component-library best practice recognized across the discipline.

<a id="ux-09"></a>
##### UX-09 — Design-to-development handoff

*Type:* Behavioral — Translating design intent into clear specifications and collaborating with engineering on faithful implementation.

- **[P1 — Assisted](proficiency_scale.md#p1):** Prepares specified handoff artifacts under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Produces complete, standard handoffs independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves ambiguous handoff and implementation-fidelity issues autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines handoff processes and artifacts others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets handoff strategy and standards, anticipating workflow and tooling shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines design-to-development handoff best practice for the discipline.

### Product Management (PM)

#### Discovery & Research

<a id="pm-01"></a>
##### PM-01 — Product discovery & customer research

*Type:* Behavioral — Uncovering user needs and validating problems through interviews, observation, and experimentation.

- **[P1 — Assisted](proficiency_scale.md#p1):** Runs scripted customer interviews and notes findings under a senior researcher's guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Plans and conducts standard discovery for a feature, synthesizing themes with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently frames ambiguous problems, selects fitting methods, and separates signal from noise.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the team's discovery approach and untangles findings others find contradictory.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's research strategy and anticipates emerging customer needs before they surface.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what rigorous product discovery means and shapes the discipline's practice externally.

<a id="pm-02"></a>
##### PM-02 — User persona & journey modeling

*Type:* Behavioral — Mapping target segments and their end-to-end experiences to ground product decisions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Documents personas and journey steps from supplied data under direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds usable personas and maps journeys for a product area with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently models complex multi-actor journeys and resolves conflicting user signals.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines modeling standards others adopt and reconciles personas across overlapping segments.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets persona and journey strategy across the portfolio and predicts shifting behavior patterns.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Establishes industry-recognized methods for journey modeling and teaches them widely.

<a id="pm-03"></a>
##### PM-03 — Competitive & product-market analysis

*Type:* Behavioral — Assessing market trends, competitors, and whitespace to inform positioning and opportunity sizing.

- **[P1 — Assisted](proficiency_scale.md#p1):** Gathers competitor facts and populates comparison grids under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Produces a sound competitive analysis for a product with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently reads ambiguous markets and frames defensible positioning implications.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the analytical approach others follow and decodes confusing competitive dynamics.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets market-analysis strategy and anticipates structural shifts before competitors react.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes how the field interprets product-market fit and is cited externally on it.

#### Strategy & Planning

<a id="pm-04"></a>
##### PM-04 — Product strategy & positioning

*Type:* Behavioral — Defining target markets, value propositions, and differentiation that guide what to build and why.

- **[P1 — Assisted](proficiency_scale.md#p1):** Drafts positioning statements from a given strategy under direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Articulates strategy and positioning for one product with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently sets coherent strategy amid ambiguity and defends hard trade-offs.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the strategy framework teams adopt and resolves conflicting strategic bets.
- **[P5 — Authority](proficiency_scale.md#p5):** Owns portfolio-level strategy and anticipates where the market is heading.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good product strategy means for the discipline and influences practice externally.

<a id="pm-05"></a>
##### PM-05 — Roadmap & portfolio planning

*Type:* Behavioral — Sequencing initiatives across products and horizons against goals, capacity, and dependencies.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains roadmap items and updates status under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds and sequences a credible roadmap for one product with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently balances competing priorities and replans confidently under shifting constraints.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the planning approach others use and resolves cross-team portfolio conflicts.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets portfolio planning strategy and foresees where investment should shift next.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines portfolio-planning best practice for the field and is recognized for it.

<a id="pm-06"></a>
##### PM-06 — Vision & goal setting

*Type:* Behavioral — Articulating product vision and outcome-based objectives that align teams over time.

- **[P1 — Assisted](proficiency_scale.md#p1):** Translates a stated vision into concrete goals under direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Sets clear, measurable goals for a product area with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently crafts a compelling vision and cascades aligned goals through ambiguity.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines goal-setting frameworks others adopt and aligns competing visions.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enduring vision across the portfolio and anticipates long-horizon shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes how the discipline frames product vision and is externally credible on it.

#### Definition & Delivery

<a id="pm-07"></a>
##### PM-07 — Requirement & specification definition

*Type:* Behavioral — Translating problems into clear, testable requirements, specs, and acceptance criteria.

- **[P1 — Assisted](proficiency_scale.md#p1):** Writes requirements from supplied input and refines them under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Authors complete, testable specs for standard features with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently specifies ambiguous, cross-cutting features and resolves edge cases cleanly.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines specification standards others adopt and untangles the hardest requirement conflicts.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets specification strategy across teams and anticipates downstream definition needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what excellent product specification means and influences the practice externally.

<a id="pm-08"></a>
##### PM-08 — Product backlog management

*Type:* Behavioral — Curating, refining, and grooming a backlog so the team always works on the highest-value items.

- **[P1 — Assisted](proficiency_scale.md#p1):** Updates and grooms backlog items under direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Prioritizes and maintains a healthy backlog for one team with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently sequences contested work and keeps the backlog coherent under churn.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines backlog practices others follow and resolves cross-team prioritization disputes.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets backlog-management strategy across products and anticipates capacity tensions.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines backlog-management best practice for the discipline and is recognized for it.

<a id="pm-09"></a>
##### PM-09 — Go-to-market coordination

*Type:* Behavioral — Orchestrating launch readiness across engineering, marketing, sales, and support.

- **[P1 — Assisted](proficiency_scale.md#p1):** Executes assigned launch tasks and tracks checklist items under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Coordinates a standard product launch across functions with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently orchestrates complex launches and recovers when plans go sideways.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the go-to-market playbook others adopt and rescues high-stakes launches.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets go-to-market strategy across the portfolio and anticipates market-timing risks.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what great go-to-market means for the field and shapes external practice.

#### Measurement & Insight

<a id="pm-10"></a>
##### PM-10 — Metrics & product analytics

*Type:* Technical — Defining success metrics and interpreting product data to evaluate impact and guide iteration.

- **[P1 — Assisted](proficiency_scale.md#p1):** Pulls and reports defined product metrics under direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds and interprets metric dashboards for a product with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently designs metric frameworks and draws sound conclusions from messy data.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the measurement model teams adopt and diagnoses misleading metrics others trust.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets product-analytics strategy across the org and anticipates which signals will matter.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines rigorous product measurement for the discipline and is cited externally on it.

<a id="pm-11"></a>
##### PM-11 — Product experimentation & A/B testing

*Type:* Technical — Designing and reading controlled experiments to validate hypotheses and de-risk decisions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Runs predefined experiments and records results under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs and analyzes a standard A/B test with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently designs valid experiments and interprets ambiguous or conflicting results.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines experimentation standards others adopt and rescues flawed test designs.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's experimentation strategy and anticipates where testing should expand.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines experimentation rigor for the discipline and influences external practice.

<a id="pm-12"></a>
##### PM-12 — Pricing & business modeling

*Type:* Behavioral — Reasoning about pricing, packaging, and unit economics to sustain a viable product.

- **[P1 — Assisted](proficiency_scale.md#p1):** Populates pricing models with supplied assumptions under direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds a sound business model for one product with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently structures pricing under uncertainty and defends margin trade-offs.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the modeling approach others adopt and untangles complex monetization questions.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets pricing strategy across the portfolio and anticipates market and cost shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines pricing and business-modeling best practice for the field and is recognized for it.

#### Stakeholder Engagement

<a id="pm-13"></a>
##### PM-13 — Stakeholder & executive management

*Type:* Behavioral — Aligning leadership and cross-functional stakeholders around product direction and trade-offs.

- **[P1 — Assisted](proficiency_scale.md#p1):** Prepares updates and gathers input for stakeholders under direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages routine stakeholder relationships and communications with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently aligns conflicting stakeholders and navigates tense executive conversations.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines stakeholder-engagement approaches others adopt and brokers the hardest alignment.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets executive-engagement strategy and anticipates leadership concerns before they arise.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines exemplary stakeholder management for the discipline and is externally credible on it.

<a id="pm-14"></a>
##### PM-14 — Customer & partner relationship management

*Type:* Behavioral — Building trust with customers and external partners to inform and advance the product.

- **[P1 — Assisted](proficiency_scale.md#p1):** Logs interactions and handles routine customer requests under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages standard customer and partner relationships with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently nurtures key accounts and resolves difficult relationship conflicts.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines relationship-management practices others adopt and salvages strained partnerships.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets relationship strategy across the portfolio and anticipates partner-ecosystem shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what excellent partner relationship management means and shapes external practice.

#### Discovery & Research

<a id="pm-15"></a>
##### PM-15 — Opportunity mapping & framing

*Type:* Behavioral — Structures discovered customer needs into an explicit opportunity space — mapped, sized, and compared — so solution choices trace to the most valuable problem rather than the first idea.

- **[P1 — Assisted](proficiency_scale.md#p1):** Places research findings onto an existing opportunity map correctly, distinguishing opportunities from solutions with coaching.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds and maintains the opportunity map for their area, sizing and pruning branches against evidence without prompting.
- **[P3 — Proficient](proficiency_scale.md#p3):** Structures messy, contested problem spaces into maps that make trade-offs explicit, and defends why one opportunity is pursued over its siblings.
- **[P4 — Expert](proficiency_scale.md#p4):** Reconciles overlapping opportunity maps across teams, exposing duplicate bets and orphaned opportunities no single team could see.
- **[P5 — Authority](proficiency_scale.md#p5):** Makes opportunity mapping an organization's default synthesis method; investment reviews open from the mapped opportunity space.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes how organizations represent customer opportunity at portfolio level; their framing methods are cited and reused beyond their own organization.

<a id="pm-16"></a>
##### PM-16 — Problem framing & outcome definition

*Type:* Behavioral — Frames incoming requests and observations as customer problems tied to measurable outcomes — separating the problem from the proposed solution before work is committed.

- **[P1 — Assisted](proficiency_scale.md#p1):** Writes a one-page problem statement naming the user, the struggle, and the evidence, with review; separates problem from requested feature when prompted.
- **[P2 — Independent](proficiency_scale.md#p2):** Frames work as outcomes the team can move rather than outputs to ship, and rewrites incoming feature requests into the underlying problem before triage.
- **[P3 — Proficient](proficiency_scale.md#p3):** Sets the outcome a product is accountable for and keeps the team pointed at it, publicly re-framing efforts that drift into output-counting.
- **[P4 — Expert](proficiency_scale.md#p4):** Arbitrates problem framing across teams — spotting duplicated or conflicting framings — and re-cuts problem boundaries drawn along org lines instead of customer lines.
- **[P5 — Authority](proficiency_scale.md#p5):** Defines an organization's outcome architecture — how team-level outcomes ladder to organizational results — and retires vanity outcomes.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Frames an organization's hardest, ownerless problems into tractable outcome statements executives fund; their framing practice shapes the discipline externally.

<a id="pm-17"></a>
##### PM-17 — Jobs-to-be-done analysis

*Type:* Behavioral — Models what customers hire products to accomplish — the circumstance, the progress sought, and the competing alternatives (including workarounds and non-consumption) — to predict adoption and define product boundaries.

- **[P1 — Assisted](proficiency_scale.md#p1):** Restates a feature request as the job the customer is hiring it for — circumstance and progress sought — with coaching.
- **[P2 — Independent](proficiency_scale.md#p2):** Maps the main jobs in their area from interview evidence, identifying what customers currently hire and where those hires fail.
- **[P3 — Proficient](proficiency_scale.md#p3):** Anchors a product's definition and boundaries in its core job, using the job to rule scope in or out and to identify non-obvious competitors.
- **[P4 — Expert](proficiency_scale.md#p4):** Aligns job maps across teams into one view of customer progress, exposing where customers must stitch products together to finish one job.
- **[P5 — Authority](proficiency_scale.md#p5):** Uses jobs analysis to shape organization-level portfolio choices — which jobs are served end-to-end, which are exited.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Frames markets and strategy in jobs terms that reveal disruption threats early; their jobs analyses influence practice beyond their organization.

<a id="pm-18"></a>
##### PM-18 — Assumption mapping & discovery testing

*Type:* Behavioral — Names and ranks the assumptions behind a product bet — desirability, viability, feasibility, usability — and designs the cheapest decisive pre-build tests (prototypes, fake doors, concierge runs) to validate or kill them.

- **[P1 — Assisted](proficiency_scale.md#p1):** Lists the assumptions behind a proposed feature, sorts them by risk with coaching, and runs a prescribed simple test, logging what was learned.
- **[P2 — Independent](proficiency_scale.md#p2):** Identifies the riskiest assumption before build and matches the test type to it — prototype, painted door, concierge — with pass/fail defined in advance.
- **[P3 — Proficient](proficiency_scale.md#p3):** Surfaces assumptions others treat as facts, designs test sequences that retire the most risk per unit effort, and kills initiatives whose load-bearing assumptions fail.
- **[P4 — Expert](proficiency_scale.md#p4):** Standardizes how multiple teams express and rank risk, and rejects validation theater — tests that can only confirm, never falsify — before major commitments.
- **[P5 — Authority](proficiency_scale.md#p5):** Builds discovery-testing capability into an organization's investment process — funding follows tested assumptions, and the cost of a first test drops to hours.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Structures bets too big to A/B as staged, falsifiable commitments; their validation doctrine is cited and adopted beyond their organization.

#### Strategy & Planning

<a id="pm-19"></a>
##### PM-19 — Domain & industry fluency

*Type:* Behavioral — Builds and maintains deep working knowledge of the product's domain — its industry structure, customer workflows, constraints, and trajectory — deeply enough to be a credible reference for customers and colleagues.

- **[P1 — Assisted](proficiency_scale.md#p1):** Learns the domain deliberately — shadows customers, reads industry sources, asks how the system actually works — and uses domain vocabulary correctly.
- **[P2 — Independent](proficiency_scale.md#p2):** Answers most domain questions without deferring and corrects domain errors in specs and designs.
- **[P3 — Proficient](proficiency_scale.md#p3):** Is the recognized domain reference for a product — customers, field teams, and engineers check facts with them — and spots domain-driven risks others miss.
- **[P4 — Expert](proficiency_scale.md#p4):** Connects domain knowledge across teams, catching where one roadmap violates another domain's constraints (regulatory, workflow, ecosystem).
- **[P5 — Authority](proficiency_scale.md#p5):** Represents an organization's domain understanding externally — industry forums, advisory boards, analyst briefings.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Anticipates domain evolution — where the industry's workflows and rules are heading — and positions portfolios for it before consensus forms.

### Engineering Management (EM)

#### People Management

<a id="em-01"></a>
##### EM-01 — Performance management & accountability

*Type:* Behavioral — Setting expectations, evaluating performance, and addressing under-performance fairly and clearly.

- **[P1 — Assisted](proficiency_scale.md#p1):** Gathers performance inputs and drafts feedback under a manager's guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs standard performance cycles and holds direct reports accountable with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently manages underperformance and difficult cases through to clear resolution.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines accountability practices other managers adopt and coaches them through hard cases.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's performance philosophy and anticipates systemic accountability gaps.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what fair, effective performance management means and influences the field externally.

<a id="em-02"></a>
##### EM-02 — Career development & sponsorship

*Type:* Behavioral — Growing engineers through development plans, advancement opportunities, and active sponsorship.

- **[P1 — Assisted](proficiency_scale.md#p1):** Supports growth conversations and tracks development goals under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Coaches direct reports on standard career growth with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently sponsors people into stretch roles and navigates complex growth paths.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines career-development practices others adopt and unblocks the toughest growth cases.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's talent-development strategy and anticipates future capability needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines exemplary career sponsorship for the discipline and is externally recognized for it.

<a id="em-03"></a>
##### EM-03 — Psychological safety & team health

*Type:* Behavioral — Creates the conditions where people raise problems, dissent, and admit mistakes without penalty; reads and repairs team-health signals (conflict, burnout risk, on-call load).

- **[P1 — Assisted](proficiency_scale.md#p1):** With guidance, runs meetings where quieter members are heard; escalates team-health concerns they notice.
- **[P2 — Independent](proficiency_scale.md#p2):** Creates safety on their own team — models fallibility, protects dissent, surfaces and resolves conflict early; monitors basic health signals.
- **[P3 — Proficient](proficiency_scale.md#p3):** Sustains safety through pressure (incidents, deadlines, change); repairs damaged trust; the team measurably speaks up (postmortems name real causes).
- **[P4 — Expert](proficiency_scale.md#p4):** Diagnoses and fixes systemic safety failures across teams; other leaders seek their help on entrenched conflict and burnout patterns.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's team-health bar and mechanisms; safety practices they designed are adopted org-wide.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes how the industry thinks about team health; published practices others implement.

#### Organizational Design

<a id="em-04"></a>
##### EM-04 — Team design & org structuring

*Type:* Behavioral — Shaping team topologies, roles, and reporting lines to fit the work and scale.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains team charts and documents structure under direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs a sound structure for one team with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently restructures teams to fit changing work and resolves boundary conflicts.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines org-design approaches others adopt and reshapes the most tangled structures.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets org-structuring strategy across the org and anticipates scaling inflection points.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines effective engineering-org design for the discipline and is cited externally on it.

<a id="em-05"></a>
##### EM-05 — Headcount & resource planning

*Type:* Behavioral — Forecasting staffing needs and allocating people across initiatives and priorities.

- **[P1 — Assisted](proficiency_scale.md#p1):** Tracks headcount and updates plans under direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds a credible headcount plan for one team with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently plans resourcing under uncertainty and defends staffing trade-offs.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines resource-planning practices others adopt and resolves cross-team allocation conflicts.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets org-wide resourcing strategy and anticipates future capacity demand.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines headcount-planning best practice for the discipline and is recognized for it.

<a id="em-06"></a>
##### EM-06 — Budget & vendor management

*Type:* Behavioral — Managing budgets, costs, and external vendor or contractor relationships.

- **[P1 — Assisted](proficiency_scale.md#p1):** Tracks spend and processes vendor invoices under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages a team budget and standard vendor relationships with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently controls budgets under pressure and negotiates difficult vendor terms.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines budget and vendor practices others adopt and rescues failing vendor relationships.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets org-wide budget and vendor strategy and anticipates cost and supplier risks.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines exemplary budget and vendor management for the field and influences practice.

#### Execution & Operations

<a id="em-07"></a>
##### EM-07 — Delivery & program management

*Type:* Behavioral — Driving cross-team execution, dependencies, and predictable delivery of programs.

- **[P1 — Assisted](proficiency_scale.md#p1):** Tracks tasks and updates delivery status under direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Drives delivery of a standard program with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently runs complex multi-team programs and recovers slipping delivery.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines delivery practices others adopt and rescues the most troubled programs.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's delivery strategy and anticipates systemic delivery risks.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what excellent program delivery means and shapes external practice.

<a id="em-08"></a>
##### EM-08 — Process & operating-cadence design

*Type:* Behavioral — Designing rituals, workflows, and cadences that keep teams effective and aligned.

- **[P1 — Assisted](proficiency_scale.md#p1):** Follows and documents established processes under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs and tunes a team's operating cadence with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently designs processes that fit the work and removes friction others miss.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines operating-cadence patterns others adopt and fixes broken processes across teams.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's operating model and anticipates where cadence must evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines effective engineering operating cadence for the discipline and is recognized for it.

<a id="em-09"></a>
##### EM-09 — Engineering metrics & productivity

*Type:* Technical — Using delivery and health metrics to diagnose and improve team effectiveness.

- **[P1 — Assisted](proficiency_scale.md#p1):** Collects and reports defined engineering metrics under direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Interprets productivity metrics for one team with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently designs metric systems and distinguishes real signal from vanity numbers.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the productivity-measurement model others adopt and debunks misleading metrics.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's engineering-metrics strategy and anticipates which signals will matter.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines rigorous engineering productivity measurement and influences the field externally.

<a id="em-10"></a>
##### EM-10 — Incident & operational risk management

*Type:* Behavioral — Establishing on-call, incident response, and risk practices that protect reliability.

- **[P1 — Assisted](proficiency_scale.md#p1):** Follows incident runbooks and logs actions under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages standard incidents and routine operational risk with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently leads severe incidents and drives durable remediation of risk.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines incident and risk practices others adopt and commands the worst crises calmly.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's operational-risk strategy and anticipates systemic failure modes.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what excellent operational risk management means and shapes external practice.

#### Culture & Change

<a id="em-11"></a>
##### EM-11 — Engineering culture & values stewardship

*Type:* Behavioral — Shaping norms, standards, and culture that define how the team builds and behaves.

- **[P1 — Assisted](proficiency_scale.md#p1):** Models stated values and reinforces them within a team under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Sustains a healthy team culture aligned to values with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently strengthens culture and addresses values violations decisively.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines cultural practices others adopt and repairs damaged team cultures.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's culture strategy and anticipates where values must be reinforced.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what a strong engineering culture looks like and is externally credible on it.

<a id="em-12"></a>
##### EM-12 — Change & transformation management

*Type:* Behavioral — Leading teams through reorganization, process change, and shifting priorities.

- **[P1 — Assisted](proficiency_scale.md#p1):** Supports rollout of defined changes and tracks adoption under direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Leads a contained team change with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently drives significant change through resistance to durable adoption.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines change approaches others adopt and rescues stalled transformations.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's transformation strategy and anticipates where change is needed next.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines effective engineering transformation for the discipline and shapes external practice.

#### People Management

<a id="em-13"></a>
##### EM-13 — Onboarding & team formation

*Type:* Behavioral — Ramps new people to productivity fast and leads teams through formation stages — launches, merges, and resets — deliberately rather than enduring them.

- **[P1 — Assisted](proficiency_scale.md#p1):** Follows an existing onboarding checklist for new hires; escalates ramp problems.
  — *Why this level:* Executing someone else's onboarding checklist and escalating problems is Bauer's passive/compliance onboarding level — rule-following without adaptation, the Dreyfus novice band. *Sources:* Bauer, Onboarding New Employees: Maximizing Success, SHRM Foundation Effective Practice Guidelines (2010).
- **[P2 — Independent](proficiency_scale.md#p2):** Runs a 30/60/90 onboarding with named buddies and early wins; new hires ship in their first weeks and say so in check-ins.
  — *Why this level:* Independently running a structured 30/60/90 with buddies and early wins is Bauer's proactive-onboarding practice and Watkins' standard line-manager transition toolkit, applied to one team without needing design authority. *Sources:* Bauer, Onboarding New Employees: Maximizing Success, SHRM Foundation Effective Practice Guidelines (2010); Watkins, The First 90 Days (Harvard Business Review Press, 2003).
- **[P3 — Proficient](proficiency_scale.md#p3):** Reads a team's formation stage and intervenes on it — resets norms after a merge, names storming in the room instead of managing it by email.
  — *Why this level:* Reading a team's formation stage and intervening live (resetting norms post-merge, naming storming) is applying Tuckman's stage model to real group dynamics — situational judgment beyond procedure. *Sources:* Tuckman, Developmental Sequence in Small Groups, Psychological Bulletin 63(6), 384-399 (1965).
- **[P4 — Expert](proficiency_scale.md#p4):** Builds the onboarding and team-launch playbook multiple teams use; teams start faster because of materials and rituals they created, and stands up whole new teams repeatedly.
  — *Why this level:* Building the onboarding/team-launch playbook other teams adopt and repeatedly standing up new teams is codified, transferable expertise — the shift from doing to defining the approach. *Sources:* Tuckman, Developmental Sequence in Small Groups, Psychological Bulletin 63(6), 384-399 (1965); Skelton & Pais, Team Topologies (IT Revolution, 2019).
- **[P5 — Authority](proficiency_scale.md#p5):** Designs how an organization absorbs step-change growth — acquisitions, new sites, doubled headcount — without culture dilution; integration plans carry named cultural mechanisms.
  — *Why this level:* Designing how an organization absorbs step-change growth without culture dilution is acquisition-integration design per Haspeslagh & Jemison — organization-level authority over formation. *Sources:* Haspeslagh & Jemison, Managing Acquisitions: Creating Value Through Corporate Renewal (Free Press, 1991).
- **[P6 — Pioneer](proficiency_scale.md#p6):** Makes team formation an organization-wide capability — new groups spin up predictably without heroics — and audits that the machinery still works.
  — *Why this level:* Making team formation a predictable org-wide capability with audited machinery is defining the discipline's operating model across a company — pioneer-level practice shaping. *Sources:* Skelton & Pais, Team Topologies (IT Revolution, 2019).

<a id="em-14"></a>
##### EM-14 — Delegation & empowerment

*Type:* Behavioral — Hands over whole outcomes with context and calibrated support, pushes decision rights to where the information lives, and builds organizations that run on intent rather than presence.

- **[P1 — Assisted](proficiency_scale.md#p1):** Assigns tasks with instructions and checks completion; keeps consequential work for themselves.
- **[P2 — Independent](proficiency_scale.md#p2):** Delegates whole outcomes with context and check-in contracts matched to each person's readiness — and resists snatching work back when it wobbles.
- **[P3 — Proficient](proficiency_scale.md#p3):** Hands ownership of critical, visible work to someone not yet proven and scaffolds them to success, letting them keep the credit; the team runs a week without them and nothing stalls.
- **[P4 — Expert](proficiency_scale.md#p4):** Pushes decisions down across multiple teams — publishes decision rights so teams stop escalating what they can decide themselves; involvement is exception-based, and everyone knows which is which.
- **[P5 — Authority](proficiency_scale.md#p5):** Builds organizations that run on mechanisms rather than presence — delegated authorities with audit trails, pre-declared tripwires — and grants leaders consequential authority held to outcomes, not methods.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Runs an organization on intent — direction and guardrails clear enough that leaders act correctly without asking — and treats every upward escalation as a design flaw to fix.

#### Execution & Operations

<a id="em-15"></a>
##### EM-15 — Technical debt & risk stewardship

*Type:* Behavioral — Surfaces, prices, and manages technical debt and technical risk as an economic portfolio — funding paydown structurally and setting the speed-versus-soundness posture explicitly.

- **[P1 — Assisted](proficiency_scale.md#p1):** Records known shortcuts and defects when directed; raises debt concerns in planning.
- **[P2 — Independent](proficiency_scale.md#p2):** Keeps a visible debt register with the cost of carry noted and defends a steady paydown allocation in planning rather than begging quarter by quarter.
- **[P3 — Proficient](proficiency_scale.md#p3):** Distinguishes debt worth carrying from debt that will detonate, sequences remediation by risk, and prices debt in incident and velocity terms stakeholders accept.
- **[P4 — Expert](proficiency_scale.md#p4):** Makes debt legible across multiple teams — shared taxonomy, reporting rhythm — and gets cross-team risk (the shared library nobody owns, the half-finished migration) owned and funded.
- **[P5 — Authority](proficiency_scale.md#p5):** Carries technical risk onto the executive risk register — top exposures known, sized, owned, trending — and lands multi-quarter remediation programs against feature pressure.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Sets an organization's speed-versus-soundness posture explicitly — where debt is accepted for velocity and where it never is — and holds it under growth pressure.

#### Personal Effectiveness

<a id="em-16"></a>
##### EM-16 — Managerial leverage & focus

*Type:* Behavioral — Spends leadership time where it multiplies — deliberate calendar design, high-leverage intervention choice, and systematic abandonment of low-value work.

- **[P1 — Assisted](proficiency_scale.md#p1):** Keeps commitments manageable with help; recognizes when their calendar no longer matches priorities.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs a deliberate calendar that matches stated priorities — protected one-on-ones, deep work, and team time; declines low-leverage meetings with alternatives offered.
- **[P3 — Proficient](proficiency_scale.md#p3):** Prunes their own involvement ruthlessly as complexity grows — automates, delegates, or kills recurring work every quarter — and models sustainable pace through crunch.
- **[P4 — Expert](proficiency_scale.md#p4):** Chooses interventions by multiplier across many teams — the review that shapes ten decisions, the document that aligns three roadmaps — declining the rest by policy; audits their time and publishes the changes.
- **[P5 — Authority](proficiency_scale.md#p5):** Allocates attention like a portfolio at organizational scale — deep on the few places they are the unique unlock, delegated on the rest — and says which is which out loud.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Spends presence deliberately as an organizational signal — where they show up moves priorities — and guards the organization's focus by limiting concurrent top priorities and abandoning stale initiatives by name.

#### People Management

<a id="em-17"></a>
##### EM-17 — Motivation & engagement

*Type:* Behavioral — Builds durable intrinsic motivation: removes dissatisfiers, feeds autonomy/mastery/purpose, recognizes well.

- **[P1 — Assisted](proficiency_scale.md#p1):** Recognizes teammates' good work; flags demotivating friction to their manager.
- **[P2 — Independent](proficiency_scale.md#p2):** Knows what drives each person on their team; removes hygiene friction and matches work to intrinsic drivers; recognition is specific and timely.
- **[P3 — Proficient](proficiency_scale.md#p3):** Sustains engagement through hard stretches; diagnoses systemic motivation problems (not just individuals) and fixes the conditions.
- **[P4 — Expert](proficiency_scale.md#p4):** Builds engagement mechanisms other teams adopt; reverses disengagement trends beyond their own span.
- **[P5 — Authority](proficiency_scale.md#p5):** Owns the engagement strategy for a function; conditions they designed show up in retention and survey trends.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Advances the practice of engagement in the field; frameworks others cite and use.

### Developer Relations & Technical Communication (DR)

#### Community & Advocacy

<a id="dr-01"></a>
##### DR-01 — Developer advocacy & community building

*Type:* Behavioral — Growing and nurturing developer communities and representing their needs internally.

- **[P1 — Assisted](proficiency_scale.md#p1):** Engages community channels and answers routine questions under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Grows and supports a developer community segment with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently builds thriving communities and defuses tense community conflicts.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines community-building practices others adopt and revives flagging communities.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's community strategy and anticipates where developer interest is shifting.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what great developer advocacy means and is externally recognized for it.

<a id="dr-02"></a>
##### DR-02 — Developer experience & feedback loops

*Type:* Behavioral — Gathering developer feedback and championing improvements to the developer experience.

- **[P1 — Assisted](proficiency_scale.md#p1):** Collects developer feedback and logs friction points under direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs standard feedback loops and surfaces DX issues with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently diagnoses deep DX problems and closes the loop to real fixes.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines DX-feedback practices others adopt and untangles the hardest experience gaps.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's developer-experience strategy and anticipates emerging friction.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what excellent developer experience means and shapes the field's practice.

<a id="dr-03"></a>
##### DR-03 — Developer marketing & evangelism

*Type:* Behavioral — Raising awareness and adoption through authentic, technically credible outreach.

- **[P1 — Assisted](proficiency_scale.md#p1):** Executes assigned evangelism tasks and amplifies messages under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs a standard developer-marketing campaign with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently crafts resonant developer narratives and adapts to skeptical audiences.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines evangelism approaches others adopt and turns around messaging that fell flat.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets developer-marketing strategy and anticipates which narratives will land next.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what authentic developer evangelism means and is externally credible on it.

#### Content & Documentation

<a id="dr-04"></a>
##### DR-04 — Technical content creation

*Type:* Behavioral — Producing tutorials, samples, posts, and reference material that help developers succeed.

- **[P1 — Assisted](proficiency_scale.md#p1):** Drafts technical content from outlines and revises under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Produces accurate, clear technical content independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently creates content for complex topics and ambiguous audiences.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines content standards others adopt and elevates the hardest technical pieces.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's content strategy and anticipates which topics developers will need.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what excellent technical content looks like and shapes external practice.

<a id="dr-05"></a>
##### DR-05 — Developer documentation & information architecture

*Type:* Behavioral — Structuring, writing, and organizing docs so information is findable and usable.

- **[P1 — Assisted](proficiency_scale.md#p1):** Writes and updates doc pages within an existing structure under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Authors and organizes documentation for a product area with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently architects coherent doc structures for complex, evolving products.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines information-architecture standards others adopt and restructures tangled doc sets.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's documentation strategy and anticipates structural scaling needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines great developer documentation and information architecture for the field.

<a id="dr-06"></a>
##### DR-06 — Editing & content governance

*Type:* Behavioral — Upholding style, quality, accuracy, and consistency across published content.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies style rules and fixes errors under an editor's guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Edits content to standard and enforces routine governance with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently edits complex material and adjudicates ambiguous style and quality calls.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines editorial standards others adopt and resolves the hardest governance disputes.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's content-governance strategy and anticipates quality risks at scale.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines editorial excellence and content governance for the discipline externally.

<a id="dr-07"></a>
##### DR-07 — Content strategy & localization

*Type:* Behavioral — Planning content coverage, lifecycle, and adaptation for diverse audiences and locales.

- **[P1 — Assisted](proficiency_scale.md#p1):** Tags content for localization and tracks coverage under direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Executes a content and localization plan for an area with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently shapes content strategy and resolves complex localization trade-offs.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines content-strategy and localization practices others adopt across teams.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's global content strategy and anticipates emerging audience needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what world-class content strategy and localization mean for the field.

#### Education & Enablement

<a id="dr-08"></a>
##### DR-08 — Developer education & enablement

*Type:* Behavioral — Designing learning paths, workshops, and resources that build developer competence.

- **[P1 — Assisted](proficiency_scale.md#p1):** Delivers prepared training material and supports learners under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds and runs standard enablement for a topic with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently designs learning paths for complex topics and varied skill levels.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines enablement approaches others adopt and rescues ineffective programs.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's developer-education strategy and anticipates future learning needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what effective developer education means and shapes external practice.

<a id="dr-09"></a>
##### DR-09 — Public speaking & demos

*Type:* Behavioral — Delivering compelling talks, live demos, and presentations to technical audiences.

- **[P1 — Assisted](proficiency_scale.md#p1):** Delivers a prepared talk or demo with coaching and review.
- **[P2 — Independent](proficiency_scale.md#p2):** Presents standard talks and demos independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently commands tough rooms and recovers gracefully when demos break.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines presentation and demo craft others adopt and coaches them to improve.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's speaking strategy and anticipates which stages and stories matter.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what compelling technical speaking looks like and is externally renowned for it.

<a id="dr-10"></a>
##### DR-10 — Sample code & API storytelling

*Type:* Technical — Building example projects and narratives that show how to apply interfaces and tools effectively.

- **[P1 — Assisted](proficiency_scale.md#p1):** Writes basic sample snippets from specs under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Produces clear, working samples that illustrate an API with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Independently crafts samples that make complex APIs intuitive and tell a clear story.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines sample-and-storytelling standards others adopt and reworks confusing examples.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's API-storytelling strategy and anticipates which patterns developers need.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what excellent API storytelling through code means and shapes external practice.

### Product & Delivery (PD)

#### Value Delivery

<a id="pd-01"></a>
##### PD-01 — Work Breakdown & Incremental Delivery

*Type:* Behavioral — Slices work so value and learning arrive early.

- **[P1 — Assisted](proficiency_scale.md#p1):** Breaks own tasks into reviewable pieces with guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently decomposes a feature into shippable slices.
- **[P3 — Proficient](proficiency_scale.md#p3):** Plans complex multi-phase work (prototype-then-commit under uncertainty); sequences safely.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert at structuring large initiatives to de-risk early; anticipates bottlenecks.
- **[P5 — Authority](proficiency_scale.md#p5):** Shapes how the org plans and sequences major change.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines the company-wide approach to delivering value incrementally.

<a id="pd-02"></a>
##### PD-02 — Prioritization & Economic Thinking

*Type:* Behavioral — Weighs cost, value, risk and timing.

- **[P1 — Assisted](proficiency_scale.md#p1):** Works highest-priority-first when told the priorities.
- **[P2 — Independent](proficiency_scale.md#p2):** Makes sound priority calls within scope; time-boxes uncertain work.
- **[P3 — Proficient](proficiency_scale.md#p3):** Balances cost/value/risk across a domain; resists hype; decisions hold up over months.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert at portfolio-level trade-offs; surfaces hidden assumptions; trusted tiebreaker.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets decision frameworks for the org.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Influences company strategic direction through judgment.

<a id="pd-03"></a>
##### PD-03 — Dealing with Ambiguity

*Type:* Behavioral — Makes progress when the problem is unclear.

- **[P1 — Assisted](proficiency_scale.md#p1):** Asks good questions to turn a vague task into a clear one.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently turns a vague request into a workable plan.
- **[P3 — Proficient](proficiency_scale.md#p3):** Thrives in ambiguity; frames the problem for others; chooses an approach and commits.
- **[P4 — Expert](proficiency_scale.md#p4):** Creates clarity for multiple teams out of open-ended situations.
- **[P5 — Authority](proficiency_scale.md#p5):** Defines direction where none exists at org scale.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Comfortable with the highest-uncertainty company bets.

#### Execution

<a id="pd-04"></a>
##### PD-04 — Estimation & Planning

*Type:* Behavioral — Forecasts and plans work credibly.

- **[P1 — Assisted](proficiency_scale.md#p1):** Learns to estimate; surfaces blockers; plans own tasks with guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Estimates scoped work realistically; plans own 1-3 week projects.
- **[P3 — Proficient](proficiency_scale.md#p3):** Plans quarter-scale, multi-workstream efforts including dependencies.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert at planning large programs; anticipates risk early.
- **[P5 — Authority](proficiency_scale.md#p5):** Plans org-level programs across quarters/years.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes how the company plans major technical change.

<a id="pd-05"></a>
##### PD-05 — Ownership & Delivery Accountability

*Type:* Behavioral — Makes and keeps credible commitments.

- **[P1 — Assisted](proficiency_scale.md#p1):** Takes ownership of assigned tasks; honest about progress and blockers.
- **[P2 — Independent](proficiency_scale.md#p2):** Owns components end-to-end; delivers committed work reliably.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns a domain; lands multi-week efforts without surprises; pushes back on unrealistic scope with reasons.
- **[P4 — Expert](proficiency_scale.md#p4):** Owns cross-team initiatives; unblocks teams; kills failing approaches early.
- **[P5 — Authority](proficiency_scale.md#p5):** Owns an org-level portfolio of bets; sets direction others follow.
- **[P6 — Pioneer](proficiency_scale.md#p6):** The go-to when something company-critical must land.

<a id="pd-06"></a>
##### PD-06 — Product Thinking

*Type:* Behavioral — Connects technical work to user and business value.

- **[P1 — Assisted](proficiency_scale.md#p1):** Understands the capability they're building and who uses it.
- **[P2 — Independent](proficiency_scale.md#p2):** Frames own work in user/business outcomes, not just tasks.
- **[P3 — Proficient](proficiency_scale.md#p3):** Treats their area as a product; uses metrics to decide what to build for a domain.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert at aligning technical bets with product strategy across teams.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets product direction for an org's technical surface.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes how the company creates value through technical products.

<a id="pd-07"></a>
##### PD-07 — Strategic & Commercial Awareness

*Type:* Behavioral — Frames technical decisions in economic and business terms — cost, revenue risk, cost of delay, unit economics — and answers for whether the work actually moved its business outcome.

- **[P1 — Assisted](proficiency_scale.md#p1):** States what business outcome their current task serves — and asks when they can't — treating infrastructure and license costs as real money.
- **[P2 — Independent](proficiency_scale.md#p2):** Checks whether shipped work actually moved its metric and says so plainly when it didn't; weighs cost and maintenance burden in the technical choices they own.
- **[P3 — Proficient](proficiency_scale.md#p3):** Frames a domain's technical decisions in business terms — cost of delay, revenue risk, support load — pushes back on work with weak business rationale, and redirects effort when the numbers say the plan is wrong.
- **[P4 — Expert](proficiency_scale.md#p4):** Builds the business case for the cross-team technical investments with the largest return and is trusted by leadership to have done the math.
- **[P5 — Authority](proficiency_scale.md#p5):** Aligns an organization's technical strategy with its economics — cost curves, velocity, risk — owning trade-offs measured in staff-years and reporting them in the business's own terms.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Advises company leadership on where technology changes the business model and is accountable for company-level technology bets paying off.

### Communication & Collaboration (CC)

#### Communication

<a id="cc-01"></a>
##### CC-01 — Written & Verbal Communication

*Type:* Behavioral — Conveys ideas clearly to the right audience.

- **[P1 — Assisted](proficiency_scale.md#p1):** Communicates status clearly; documentation is accurate.
- **[P2 — Independent](proficiency_scale.md#p2):** Writes clear design notes, runbooks and PRs; explains trade-offs without overselling.
- **[P3 — Proficient](proficiency_scale.md#p3):** Writes design docs that drive decisions; translates technical risk for non-technical stakeholders.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert at making complex capability/risk legible to executives without dumbing it down; RFCs align orgs.
- **[P5 — Authority](proficiency_scale.md#p5):** Strategy memos leadership acts on; org-wide and external reach.
- **[P6 — Pioneer](proficiency_scale.md#p6):** A clarifying voice at company scale; externally recognized.

<a id="cc-02"></a>
##### CC-02 — Knowledge Sharing & Documentation

*Type:* Behavioral — Spreads understanding so others move faster.

- **[P1 — Assisted](proficiency_scale.md#p1):** Shares what they learn; keeps their docs accurate.
- **[P2 — Independent](proficiency_scale.md#p2):** Documents their area well; proactively shares techniques with the team.
- **[P3 — Proficient](proficiency_scale.md#p3):** Creates documentation and forums that raise a whole domain's understanding.
- **[P4 — Expert](proficiency_scale.md#p4):** Builds knowledge-sharing systems adopted across teams.
- **[P5 — Authority](proficiency_scale.md#p5):** Defines how the org captures and spreads knowledge.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry-facing knowledge practice.

#### Collaboration

<a id="cc-03"></a>
##### CC-03 — Teamwork & Partnership

*Type:* Behavioral — Works productively with others toward shared goals.

- **[P1 — Assisted](proficiency_scale.md#p1):** Responsive to feedback; pairs willingly; asks for help appropriately.
- **[P2 — Independent](proficiency_scale.md#p2):** Collaborates smoothly with adjacent functions; handles disagreement constructively.
- **[P3 — Proficient](proficiency_scale.md#p3):** Builds strong cross-team relationships; resolves friction directly.
- **[P4 — Expert](proficiency_scale.md#p4):** Expert at aligning teams with competing priorities; mediates disputes between senior people.
- **[P5 — Authority](proficiency_scale.md#p5):** Creates the forums and processes through which collaboration happens.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Builds coalitions at company scale and externally.

<a id="cc-04"></a>
##### CC-04 — Feedback

*Type:* Behavioral — Gives and receives honest, useful feedback.

- **[P1 — Assisted](proficiency_scale.md#p1):** Accepts feedback non-defensively; acts on it.
- **[P2 — Independent](proficiency_scale.md#p2):** Gives timely, specific, kind feedback to peers.
- **[P3 — Proficient](proficiency_scale.md#p3):** Gives growth-oriented feedback that changes behavior; coaches through feedback.
- **[P4 — Expert](proficiency_scale.md#p4):** Builds feedback norms that raise the bar across teams.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's culture of candor and growth.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Models and defines feedback culture company-wide.

<a id="cc-05"></a>
##### CC-05 — Handling Disagreement

*Type:* Behavioral — Navigates conflict toward good decisions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Voices disagreement respectfully; disagrees-and-commits.
- **[P2 — Independent](proficiency_scale.md#p2):** Works through disagreement to a decision without damaging relationships.
- **[P3 — Proficient](proficiency_scale.md#p3):** Mediates technical disputes in their domain; finds the path that holds up.
- **[P4 — Expert](proficiency_scale.md#p4):** Resolves high-stakes disagreements between senior stakeholders across orgs.
- **[P5 — Authority](proficiency_scale.md#p5):** Designs the decision processes the org uses to resolve conflict.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Sets the company norm for principled disagreement.

#### Communication

<a id="cc-06"></a>
##### CC-06 — Executive Communication

*Type:* Behavioral — Communicates upward and to executive audiences — answer-first briefings, decision-ready framing, and composure under hostile questioning.

- **[P1 — Assisted](proficiency_scale.md#p1):** Prepares status updates for leadership with guidance; leads with the headline when coached to.
- **[P2 — Independent](proficiency_scale.md#p2):** Reports upward answer-first with a specific ask; escalates early with options attached, so no surprise reaches leadership from someone else.
- **[P3 — Proficient](proficiency_scale.md#p3):** Briefs senior leaders under pressure — facts, impact, options, and a recommendation inside the first two minutes; one-pagers get forwarded unedited.
- **[P4 — Expert](proficiency_scale.md#p4):** Builds and lands investment cases with executive audiences — pre-wired with skeptics, sized in business terms, honest about risk; coaches others for executive rooms and runs the operating reviews an organization communicates through.
- **[P5 — Authority](proficiency_scale.md#p5):** Operates the executive room as a peer — advances positions, absorbs hostile questioning without defensiveness, and changes the room's decision more often than not.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Speaks for an organization's technical reality to boards, investors, and press; trusted with the messages that cannot be delegated, and organizational credibility survives the appearances.

### Leadership & Influence (LI)

#### Growing People

<a id="li-01"></a>
##### LI-01 — Mentorship & Coaching

*Type:* Behavioral — Grows other people's capability.

- **[P1 — Assisted](proficiency_scale.md#p1):** Receptive to mentoring; shares what they learn.
- **[P2 — Independent](proficiency_scale.md#p2):** Helps onboard teammates; informally mentors juniors.
- **[P3 — Proficient](proficiency_scale.md#p3):** Coaches engineers with growth-oriented feedback; measurably improves a team's skill.
- **[P4 — Expert](proficiency_scale.md#p4):** Develops future leads across teams; shapes hiring and onboarding.
- **[P5 — Authority](proficiency_scale.md#p5):** Develops senior engineers and leaders; builds culture deliberately.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Develops the next generation of top talent; legacy outlasts tenure.

<a id="li-02"></a>
##### LI-02 — Hiring & Staffing

*Type:* Behavioral — Builds the team through hiring and placement.

- **[P1 — Assisted](proficiency_scale.md#p1):** Participates in interviews; gives clear, evidence-based feedback.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs interviews well; calibrates against a consistent bar.
- **[P3 — Proficient](proficiency_scale.md#p3):** Shapes hiring for a team; designs loops; makes sound staffing calls.
- **[P4 — Expert](proficiency_scale.md#p4):** Drives hiring strategy across teams; builds the interviewing bar.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the org's talent strategy.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes company-wide talent philosophy.

#### Technical Leadership

<a id="li-03"></a>
##### LI-03 — Technical Influence & Direction

*Type:* Behavioral — Shapes technical direction beyond own work.

- **[P1 — Assisted](proficiency_scale.md#p1):** Contributes informed opinions in technical discussions.
- **[P2 — Independent](proficiency_scale.md#p2):** Influences component-level decisions through credibility.
- **[P3 — Proficient](proficiency_scale.md#p3):** Sets technical direction for a domain; others align to their calls.
- **[P4 — Expert](proficiency_scale.md#p4):** Shapes how multiple teams approach problems; trusted tiebreaker.
- **[P5 — Authority](proficiency_scale.md#p5):** Influences org-wide technical strategy.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Influences company strategic direction through insight.

<a id="li-04"></a>
##### LI-04 — Decision-Making under Uncertainty

*Type:* Behavioral — Makes sound calls with incomplete information.

- **[P1 — Assisted](proficiency_scale.md#p1):** Makes well-defined decisions; asks good questions when blocked.
- **[P2 — Independent](proficiency_scale.md#p2):** Decides independently within their components; evaluates alternatives honestly.
- **[P3 — Proficient](proficiency_scale.md#p3):** Makes architectural choices for a domain that hold up over months.
- **[P4 — Expert](proficiency_scale.md#p4):** Foresees second-order consequences; sets decision frameworks for teams.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets decision-making frameworks for the org.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Visionary judgment; sees structural causes others miss.

<a id="li-05"></a>
##### LI-05 — Driving Alignment

*Type:* Behavioral — Gets people moving in the same direction.

- **[P1 — Assisted](proficiency_scale.md#p1):** Keeps own work aligned with team goals.
- **[P2 — Independent](proficiency_scale.md#p2):** Aligns direct partners on scoped decisions.
- **[P3 — Proficient](proficiency_scale.md#p3):** Drives alignment across a domain; turns disagreement into committed direction.
- **[P4 — Expert](proficiency_scale.md#p4):** Aligns multiple teams and leadership behind a direction.
- **[P5 — Authority](proficiency_scale.md#p5):** Creates forums/narratives through which the org aligns.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Aligns the company behind direction; externally persuasive.

<a id="li-06"></a>
##### LI-06 — Technical Credibility

*Type:* Behavioral — Retains enough hands-on technical depth to earn engineers' trust, ask the questions that change designs, and judge technical work without doing it.

- **[P1 — Assisted](proficiency_scale.md#p1):** Follows the team's technical discussions and asks clarifying questions; relies on others to evaluate design quality.
- **[P2 — Independent](proficiency_scale.md#p2):** Understands the systems in scope well enough to review designs, probe trade-offs, and triage incidents — earns technical respect without taking the keyboard.
- **[P3 — Proficient](proficiency_scale.md#p3):** Maintains depth across a complex system's stack and hardest problems; a credible thought-partner to the most senior engineers, pairing them with the context they need.
- **[P4 — Expert](proficiency_scale.md#p4):** Retains broad credibility across a multi-team domain — credible on its hardest cross-cutting technical questions, current enough to ask the question that changes a design.
- **[P5 — Authority](proficiency_scale.md#p5):** Sustains the credibility to guide an organization's technology direction; translates architectural risk into business terms without distortion, and senior technologists accept the judgment.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Sustains credibility across an entire technology landscape; their technical judgment is trusted at every altitude because it survives contact with detail.

#### Organizational Influence

<a id="li-07"></a>
##### LI-07 — Influence without Authority

*Type:* Behavioral — Wins outcomes across organizational seams with no formal mandate — exchange in others' currencies, coalition-building, and earned credibility.

- **[P1 — Assisted](proficiency_scale.md#p1):** Builds working relationships with adjacent teams; asks for help through the right people with guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Wins cooperation from adjacent teams by trading in their currencies — timing help, review effort, shared credit — rather than escalating.
- **[P3 — Proficient](proficiency_scale.md#p3):** Secures priority from other teams for an initiative with no borrowed authority; builds the case in the other party's terms and repays visibly.
- **[P4 — Expert](proficiency_scale.md#p4):** Moves a multi-team domain to a shared position with no mandate — assembles the coalition, converts the best-argued skeptic — and the position holds after they stop pushing.
- **[P5 — Authority](proficiency_scale.md#p5):** Shifts organization-level outcomes through people several seams away who advocate the position as their own; lands decisions while holding a minority of the formal power in the room.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes industry and market context in the organization's favor — standards bodies, open ecosystems, talent narratives — so external forces push where the organization wants to go.

#### Personal Leadership

<a id="li-08"></a>
##### LI-08 — Situational & Adaptive Leadership

*Type:* Behavioral — Reads what the person, team, and moment need and flexes leadership approach — directing, coaching, supporting, delegating — from a grounded, authentic center; distinguishes technical from adaptive challenges.

- **[P1 — Assisted](proficiency_scale.md#p1):** Recognizes that different people need different support; adjusts approach when prompted by feedback.
- **[P2 — Independent](proficiency_scale.md#p2):** Matches direction and support to each person's readiness per task — directing, coaching, supporting, or delegating deliberately — and tells technical problems from adaptive ones.
- **[P3 — Proficient](proficiency_scale.md#p3):** Flexes skillfully across a wide range of people and hard situations without losing a grounded center; refuses to force technical fixes onto adaptive challenges and names the difference.
- **[P4 — Expert](proficiency_scale.md#p4):** Coaches other leaders to read what a person, team, or moment needs; adapts across diverse teams while staying recognizably consistent in values.
- **[P5 — Authority](proficiency_scale.md#p5):** Develops adaptive leadership as an organizational discipline — leaders diagnose technical-versus-adaptive at scale, and the leadership style changes when the situation does.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes an adaptive, grounded leadership culture across an organization — style stays plastic to conditions while values stay fixed; the approach is emulated beyond the organization.

<a id="li-09"></a>
##### LI-09 — Self-Awareness & Learning Agility

*Type:* Behavioral — Seeks external feedback on their own behavior, knows their failure patterns, and extracts lessons from first-time situations fast enough to lead credibly in them.

- **[P1 — Assisted](proficiency_scale.md#p1):** Accepts feedback about their own behavior without defensiveness; acts on it when the change is spelled out.
- **[P2 — Independent](proficiency_scale.md#p2):** Asks for feedback on their own practice and changes visibly in response — "you said X, I changed Y" — keeping a running list of their own failure patterns.
- **[P3 — Proficient](proficiency_scale.md#p3):** Knows their failure modes under pressure and manages them in the moment; staffs deliberately against known weaknesses and seeks disconfirming input before hard calls.
- **[P4 — Expert](proficiency_scale.md#p4):** Runs structured input on themselves — 360s, skip-level themes — and closes the loop publicly on what changed; retools openly for first-time challenges so others copy the learning method.
- **[P5 — Authority](proficiency_scale.md#p5):** Compensates deliberately for the seniority feedback vacuum — cultivates truth-tellers, rewards bearers of unwelcome news about themselves, and retires their own outdated playbook when the organization outgrows it.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Institutionalizes challenge to their own judgment — red teams, protected dissent — and manages how their moods and offhand comments get amplified across an organization.

<a id="li-10"></a>
##### LI-10 — Resilience & Sustainable Pace

*Type:* Behavioral — Sustains effectiveness under prolonged pressure, recovers from setbacks, and designs sustainable pace into how teams operate rather than modeling heroics.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains composure through normal setbacks; recognizes their own overload and asks for help.
- **[P2 — Independent](proficiency_scale.md#p2):** Stays effective and steady under pressure — recovers from setbacks, manages their own energy, and models a sustainable pace others learn from watching.
- **[P3 — Proficient](proficiency_scale.md#p3):** Holds up through prolonged pressure — incident sieges, crunch, organizational turbulence — helping the team stay resilient and refusing burnout-driven decisions.
- **[P4 — Expert](proficiency_scale.md#p4):** Builds resilience into how multiple teams operate — on-call health, recovery after pushes, load balancing — and repairs burnout risk at scale.
- **[P5 — Authority](proficiency_scale.md#p5):** Stewards organizational resilience — capacity buffers, crisis rotation, energy management for senior leaders — and holds the line when business pressure argues for permanent crunch.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes a resilient, sustainable culture across an organization; the organization absorbs shocks without breaking people, and the practice is referenced beyond it.

<a id="li-11"></a>
##### LI-11 — Integrity & Trust

*Type:* Behavioral — Earns and keeps trust through consistency and courage — keeping commitments, telling unwelcome truths, and holding the ethical line when it is costly.

- **[P1 — Assisted](proficiency_scale.md#p1):** Keeps commitments with reminders; is honest when asked directly; escalates ethical concerns to others.
- **[P2 — Independent](proficiency_scale.md#p2):** Keeps commitments or renegotiates before the deadline, never after; says the same thing in the room and out of it, owns mistakes unprompted, and reports true status when the truth is unwelcome.
- **[P3 — Proficient](proficiency_scale.md#p3):** Makes the unpopular-but-right call under pressure and absorbs the cost personally; protects the person who raised the flag and handles sensitive information impeccably.
- **[P4 — Expert](proficiency_scale.md#p4):** Serves as the honest broker across teams — disputing parties accept their account of the facts — and carries uncomfortable systemic truths to the room that can fix them.
- **[P5 — Authority](proficiency_scale.md#p5):** Builds mechanisms that make integrity cheap at scale — ethics review in design, safe escalation with follow-through, fairness systems whose losers affirm the process — and stops launches on ethical grounds with the business case for trust.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Holds an organization's line when the profitable path and the right path diverge — the hard disclosure, the walked-away revenue — and those moments become the story the culture tells about itself.

## Business & Corporate Functions

### Marketing & Communications (MKT)

#### Brand & Creative

<a id="mkt-01"></a>
##### MKT-01 — Brand strategy & management

*Type:* Behavioral — Define and steward brand identity, positioning, voice, and consistency across touchpoints.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies existing brand guidelines to assets under review, flagging obvious off-brand usage.
- **[P2 — Independent](proficiency_scale.md#p2):** Maintains brand consistency across standard channels independently, handling routine positioning questions.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns brand positioning for a product or segment, resolving ambiguous identity and messaging trade-offs.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the brand architecture and positioning approach other marketers adopt across the portfolio.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets multi-year brand strategy and equity standards, anticipating shifts in market perception.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes how the field defines brand value, externally cited as a reference on brand building.

<a id="mkt-02"></a>
##### MKT-02 — Content & editorial strategy

*Type:* Behavioral — Plan, produce, and govern editorial content aligned to audience needs and brand narrative.

- **[P1 — Assisted](proficiency_scale.md#p1):** Drafts and formats content pieces to a brief, with edits reviewed before publishing.
- **[P2 — Independent](proficiency_scale.md#p2):** Plans and produces a content calendar independently, adapting tone for routine audiences.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns editorial strategy for a domain, balancing competing topics, formats, and audience needs.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the content model and governance that other writers and teams adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the organization's editorial vision and standards, anticipating audience and format shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what authoritative content means in the field, externally recognized as a thought leader.

<a id="mkt-03"></a>
##### MKT-03 — Creative direction & design management

*Type:* Behavioral — Guide visual and creative execution to deliver compelling, on-brand assets.

- **[P1 — Assisted](proficiency_scale.md#p1):** Executes design tasks within a defined visual system, with creative choices reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Delivers creative work independently to brief, managing routine revisions and feedback.
- **[P3 — Proficient](proficiency_scale.md#p3):** Directs creative for whole campaigns, resolving ambiguous briefs into coherent concepts.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the creative approach and critique standards other designers learn from.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the creative vision and aesthetic direction across the organization, anticipating design trends.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes creative standards the industry references, externally celebrated for distinctive work.

<a id="mkt-04"></a>
##### MKT-04 — Public relations & corporate communications

*Type:* Behavioral — Shape public narrative, manage media relationships, and protect reputation through earned channels.

- **[P1 — Assisted](proficiency_scale.md#p1):** Drafts press materials and media lists from templates, with messaging reviewed before release.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages routine media relationships and announcements independently, handling standard inquiries.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns communications for sensitive topics, navigating ambiguous narratives and difficult press situations.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the messaging framework and crisis-response playbook other communicators adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets corporate communications strategy and reputation standards, anticipating narrative and stakeholder risks.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes how the discipline handles reputation, sought externally as an authority on communications.

#### Demand & Growth

<a id="mkt-05"></a>
##### MKT-05 — Demand generation & growth marketing

*Type:* Behavioral — Drive qualified pipeline through coordinated multi-channel acquisition and growth experiments.

- **[P1 — Assisted](proficiency_scale.md#p1):** Executes demand campaigns to spec, with targeting and budget choices reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs standard acquisition programs independently, optimizing routine funnels toward targets.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns demand strategy for a segment, diagnosing and fixing underperforming funnels autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the growth model and experimentation approach other marketers adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the organization's demand strategy and growth standards, anticipating channel saturation and shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines growth-marketing practice the field follows, externally credible on scalable acquisition.

<a id="mkt-06"></a>
##### MKT-06 — Digital & search marketing

*Type:* Behavioral — Acquire and engage audiences through organic, paid, and search-driven digital channels.

- **[P1 — Assisted](proficiency_scale.md#p1):** Implements digital and search campaigns from a plan, with keywords and bids reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages search and digital channels independently, optimizing routine campaigns to targets.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns digital strategy across channels, resolving ambiguous attribution and ranking challenges autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the digital and search methodology other practitioners adopt across campaigns.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets digital marketing strategy and standards, anticipating algorithm and platform shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes search and digital practice the industry references, externally recognized expert.

<a id="mkt-07"></a>
##### MKT-07 — Lifecycle & retention marketing

*Type:* Behavioral — Nurture, convert, and retain audiences across the customer lifecycle to maximize value.

- **[P1 — Assisted](proficiency_scale.md#p1):** Builds lifecycle messages from defined journeys, with timing and segmentation reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs standard retention and nurture programs independently, handling routine segmentation.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns lifecycle strategy for a cohort, diagnosing churn and engagement problems autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the lifecycle model and retention frameworks other marketers adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets retention strategy and customer-value standards, anticipating shifts in engagement behavior.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines lifecycle-marketing practice the field follows, externally credible on retention and loyalty.

<a id="mkt-08"></a>
##### MKT-08 — Campaign planning & management

*Type:* Behavioral — Orchestrate integrated campaigns end-to-end from brief through execution and optimization.

- **[P1 — Assisted](proficiency_scale.md#p1):** Coordinates campaign tasks and timelines under direction, with the plan reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Plans and runs standard multi-channel campaigns independently, managing routine dependencies.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns complex campaigns end-to-end, resolving conflicting priorities and ambiguous briefs autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the campaign planning methodology and orchestration approach other marketers adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets integrated campaign strategy and standards, anticipating cross-channel and timing dynamics.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes campaign-management practice the industry references, externally recognized authority.

#### Events & Engagement

<a id="mkt-09"></a>
##### MKT-09 — Event & field marketing

*Type:* Behavioral — Plan and run events and field programs that generate engagement and pipeline.

- **[P1 — Assisted](proficiency_scale.md#p1):** Supports event logistics and setup under direction, with arrangements reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs standard events and field programs independently, handling routine vendor and attendee issues.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns flagship events end-to-end, resolving ambiguous trade-offs in scope, budget, and experience.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the event playbook and field-marketing approach other organizers adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets event strategy and experience standards, anticipating shifts in audience engagement.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what great events mean in the field, externally sought to design landmark experiences.

<a id="mkt-10"></a>
##### MKT-10 — Community & advocacy programs

*Type:* Behavioral — Build and nurture communities and advocates that amplify reach and loyalty.

- **[P1 — Assisted](proficiency_scale.md#p1):** Moderates and supports community activity under direction, with responses reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs standard community and advocacy programs independently, handling routine member needs.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns community strategy for a program, resolving ambiguous engagement and conflict situations autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the community-building and advocacy model other program leads adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets community strategy and health standards, anticipating shifts in member behavior and sentiment.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes community and advocacy practice the field follows, externally recognized authority.

#### Marketing Operations & Insight

<a id="mkt-11"></a>
##### MKT-11 — Marketing analytics & attribution

*Type:* Technical — Measure marketing performance and attribute outcomes across channels to guide investment.

- **[P1 — Assisted](proficiency_scale.md#p1):** Pulls standard marketing reports and metrics, with interpretation reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds routine dashboards and attribution analyses independently, answering standard performance questions.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns measurement for a domain, resolving ambiguous attribution and data-quality problems autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the attribution methodology and measurement framework other analysts adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets analytics strategy and measurement standards, anticipating shifts in data and privacy constraints.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines marketing-measurement practice the field follows, externally credible on attribution.

<a id="mkt-12"></a>
##### MKT-12 — Marketing operations & automation

*Type:* Behavioral — Design marketing processes, data flows, and automated programs that scale execution.

- **[P1 — Assisted](proficiency_scale.md#p1):** Executes automation tasks and data hygiene under direction, with configuration reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds and maintains standard automation workflows independently, handling routine operational issues.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns the marketing operations stack for a team, resolving ambiguous process and data challenges autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the operations architecture and automation standards other practitioners adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets marketing-operations strategy and governance, anticipating scaling and integration needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes marketing-operations practice the industry references, externally recognized expert.

<a id="mkt-13"></a>
##### MKT-13 — Customer & audience research

*Type:* Technical — Generate audience insight through segmentation, research, and behavioral analysis.

- **[P1 — Assisted](proficiency_scale.md#p1):** Conducts research tasks to a defined protocol, with analysis reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs standard studies and surveys independently, drawing routine insights from data.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns research for a question, designing methods and resolving ambiguous findings autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the research methodology and insight frameworks other researchers adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the research agenda and rigor standards, anticipating shifts in audience and method.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines audience-research practice the field follows, externally credible on customer insight.

### Sales (SAL)

#### Pipeline Generation

<a id="sal-01"></a>
##### SAL-01 — Prospecting & lead qualification

*Type:* Behavioral — Identify, reach, and qualify prospects to build a healthy top-of-funnel pipeline.

- **[P1 — Assisted](proficiency_scale.md#p1):** Works defined prospect lists and qualifies leads against a checklist, with outreach reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs standard prospecting independently, qualifying routine opportunities to agreed criteria.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns prospecting for a territory, qualifying ambiguous and complex opportunities autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the prospecting and qualification methodology other reps adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the pipeline-generation strategy and qualification standards across the organization.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes prospecting practice the profession references, externally recognized authority.

<a id="sal-02"></a>
##### SAL-02 — Territory & market coverage planning

*Type:* Behavioral — Segment and prioritize territories and markets to optimize sales coverage and effort.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains territory data and coverage lists under direction, with assignments reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Plans coverage for a defined territory independently, handling routine allocation decisions.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns territory design for a region, resolving ambiguous segmentation and capacity trade-offs autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the territory-planning methodology and coverage model other planners adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets market-coverage strategy and standards, anticipating shifts in market and capacity.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines territory-design practice the field follows, externally credible on coverage strategy.

#### Selling

<a id="sal-03"></a>
##### SAL-03 — Consultative & solution selling

*Type:* Behavioral — Diagnose customer needs and craft tailored solutions that link value to outcomes.

- **[P1 — Assisted](proficiency_scale.md#p1):** Follows a discovery script to surface needs, with solution framing reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs consultative conversations independently, mapping routine needs to solutions.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns complex consultative deals, diagnosing ambiguous needs and shaping tailored solutions autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the consultative selling methodology and discovery approach other sellers adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the solution-selling strategy and standards, anticipating shifts in buyer needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes consultative-selling practice the profession references, externally recognized authority.

<a id="sal-04"></a>
##### SAL-04 — Sales presentations & demonstrations

*Type:* Behavioral — Deliver persuasive presentations and demonstrations that advance buyer commitment.

- **[P1 — Assisted](proficiency_scale.md#p1):** Delivers standard presentations from a deck, with delivery reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Tailors and presents independently to routine audiences, handling common questions.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns high-stakes presentations, adapting to ambiguous rooms and tough objections autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the presentation and demo approach other sellers learn from.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets presentation strategy and storytelling standards across the sales organization.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what compelling sales presentation means in the field, externally sought to teach it.

<a id="sal-05"></a>
##### SAL-05 — Negotiation & closing

*Type:* Behavioral — Navigate terms, resolve objections, and close agreements that protect mutual value.

- **[P1 — Assisted](proficiency_scale.md#p1):** Executes standard closing steps within set terms, with concessions reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Negotiates and closes routine deals independently within approved guardrails.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns complex negotiations, navigating ambiguous terms and multi-party closes autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the negotiation and closing playbook other sellers adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets negotiation strategy and deal-term standards, anticipating buyer tactics.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes negotiation practice the profession references, externally recognized authority on closing.

#### Deal & Account Management

<a id="sal-06"></a>
##### SAL-06 — Sales pipeline & deal management

*Type:* Behavioral — Manage opportunities through stages with rigor, hygiene, and momentum to close.

- **[P1 — Assisted](proficiency_scale.md#p1):** Updates deal records and stages under direction, with hygiene reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages a personal pipeline independently, advancing routine deals through stages.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns a complex pipeline, diagnosing stalled deals and prioritizing ambiguous trade-offs autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the pipeline-management discipline and deal-review approach other sellers adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets pipeline strategy and deal-management standards, anticipating funnel risks.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines pipeline-management practice the profession references, externally credible authority.

<a id="sal-07"></a>
##### SAL-07 — Account planning & expansion

*Type:* Behavioral — Develop strategic account plans that retain, grow, and expand key relationships.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains account records and plans under direction, with priorities reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages expansion in assigned accounts independently, pursuing routine upsell opportunities.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns strategic account plans, navigating ambiguous stakeholder maps and expansion paths autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the account-planning methodology and expansion approach other sellers adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets account strategy and growth standards, anticipating shifts in customer value.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes account-management practice the profession references, externally recognized authority.

#### Sales Effectiveness

<a id="sal-08"></a>
##### SAL-08 — Sales forecasting & quota management

*Type:* Technical — Forecast revenue and manage quota attainment with predictable, data-grounded rigor.

- **[P1 — Assisted](proficiency_scale.md#p1):** Updates forecast inputs and quota tracking under direction, with figures reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Produces a personal forecast independently, managing routine quota attainment questions.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns forecasting for a team, reconciling ambiguous signals into reliable calls autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the forecasting methodology and quota-setting approach other leaders adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets forecasting strategy and quota standards, anticipating market and capacity shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines forecasting practice the field follows, externally credible on predictability and quota design.

<a id="sal-09"></a>
##### SAL-09 — Sales enablement & coaching

*Type:* Behavioral — Equip and coach sellers with the skills, content, and tools to perform consistently.

- **[P1 — Assisted](proficiency_scale.md#p1):** Delivers enablement content and onboarding tasks under direction, with coaching reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs standard training and coaching independently, developing routine rep skills.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns enablement for a team, diagnosing ambiguous performance gaps and coaching autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the enablement curriculum and coaching model other trainers adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enablement strategy and competency standards, anticipating skill needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes sales-enablement practice the profession references, externally recognized authority.

<a id="sal-10"></a>
##### SAL-10 — Channel & partner sales

*Type:* Behavioral — Drive revenue through indirect channels by enabling and managing selling partners.

- **[P1 — Assisted](proficiency_scale.md#p1):** Supports partner deals and registrations under direction, with terms reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages routine partner-sourced deals independently, handling standard channel conflict.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns channel revenue for a region, resolving ambiguous partner and conflict situations autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the channel-selling model and partner-engagement approach other reps adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets channel-sales strategy and standards, anticipating ecosystem and conflict dynamics.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines channel-sales practice the field follows, externally credible on indirect revenue.

<a id="sal-11"></a>
##### SAL-11 — Sales operations & process

*Type:* Behavioral — Design and run sales processes, territories, and systems that improve productivity.

- **[P1 — Assisted](proficiency_scale.md#p1):** Executes sales-ops tasks and data updates under direction, with changes reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Maintains standard sales processes and tooling independently, handling routine requests.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns sales process for a team, resolving ambiguous workflow and data challenges autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the sales-operations architecture and process standards other practitioners adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets sales-operations strategy and governance, anticipating scaling and tooling needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes sales-operations practice the profession references, externally recognized expert.

### Partnerships & Business Development (BD)

#### Partnership Strategy

<a id="bd-01"></a>
##### BD-01 — Partnership strategy & sourcing

*Type:* Behavioral — Identify, evaluate, and source partnerships that advance strategic and revenue goals.

- **[P1 — Assisted](proficiency_scale.md#p1):** Researches and shortlists potential partners under direction, with the rationale reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Sources and screens routine partnership opportunities independently against agreed criteria.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns partnership strategy for a domain, prioritizing ambiguous opportunities and fit autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the partnership-sourcing methodology and prioritization model others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the partnership strategy and standards, anticipating shifts in the partner landscape.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines partnership-strategy practice the field follows, externally credible on ecosystem strategy.

<a id="bd-02"></a>
##### BD-02 — Ecosystem & channel development

*Type:* Behavioral — Build and grow partner ecosystems and channels that extend reach and capability.

- **[P1 — Assisted](proficiency_scale.md#p1):** Supports ecosystem and channel tasks under direction, with recruitment steps reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Develops routine channel relationships independently, onboarding standard partners.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns ecosystem development for a segment, resolving ambiguous structure and incentive trade-offs autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the ecosystem-development model and channel-design approach others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets ecosystem strategy and standards, anticipating shifts in channel economics and structure.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes ecosystem-development practice the field references, externally recognized authority.

#### Deal Making & Alliances

<a id="bd-03"></a>
##### BD-03 — Deal structuring & negotiation

*Type:* Behavioral — Structure and negotiate partnership and commercial deals balancing risk and value.

- **[P1 — Assisted](proficiency_scale.md#p1):** Prepares deal terms from templates under direction, with structure reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Structures and negotiates routine partnership deals independently within agreed guardrails.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns complex deal structuring, navigating ambiguous terms and multi-party negotiations autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the deal-structuring frameworks and negotiation approach others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets deal-structuring strategy and standards, anticipating risk and value-sharing dynamics.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines deal-making practice the field follows, externally credible on complex partnership structures.

<a id="bd-04"></a>
##### BD-04 — Alliance & relationship management

*Type:* Behavioral — Manage ongoing alliances to sustain trust, joint value, and mutual accountability.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains alliance records and check-ins under direction, with follow-ups reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages routine alliance relationships independently, handling standard partner needs.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns strategic alliances, navigating ambiguous stakeholder dynamics and conflicts autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the alliance-management model and governance approach others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets alliance strategy and relationship standards, anticipating shifts in partner priorities.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes alliance-management practice the field references, externally recognized authority.

<a id="bd-05"></a>
##### BD-05 — Joint go-to-market & co-selling

*Type:* Behavioral — Orchestrate joint offerings, co-selling, and shared pipeline with partners.

- **[P1 — Assisted](proficiency_scale.md#p1):** Supports joint GTM activities and co-sell tasks under direction, with plans reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Executes routine joint campaigns and co-sell motions independently with partners.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns joint GTM for a partnership, resolving ambiguous alignment and attribution issues autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the joint-GTM and co-selling playbook other teams adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets co-sell strategy and standards, anticipating shifts in partner go-to-market dynamics.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines joint-GTM practice the field follows, externally credible on co-selling at scale.

#### Partner Performance

<a id="bd-06"></a>
##### BD-06 — Partner performance & program management

*Type:* Technical — Track partner performance and run programs, tiers, and incentives that drive results.

- **[P1 — Assisted](proficiency_scale.md#p1):** Tracks partner metrics and program tasks under direction, with reporting reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages a standard partner program independently, handling routine performance and tiering.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns program performance for a portfolio, diagnosing ambiguous underperformance and incentives autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the partner-program design and performance frameworks others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets partner-program strategy and standards, anticipating shifts in program economics.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes partner-program practice the field references, externally recognized authority.

### Customer Success & Account Management (CSM)

#### Onboarding & Adoption

<a id="csm-01"></a>
##### CSM-01 — Customer onboarding & adoption

*Type:* Technical — Guide new customers through implementation and drive early adoption to reach first value.

- **[P1 — Assisted](proficiency_scale.md#p1):** Completes assigned onboarding steps from a checklist for new customers, with each session reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs standard onboarding plans independently, configuring setup and guiding customers to first value.
- **[P3 — Proficient](proficiency_scale.md#p3):** Tailors onboarding to complex or ambiguous customer needs and is the team's go-to for tough launches.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the onboarding methodology others follow and rescues stalled or failing implementations.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets onboarding strategy across segments and anticipates shifts in how customers reach value.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what excellent onboarding means industry-wide and is sought externally for that expertise.

<a id="csm-02"></a>
##### CSM-02 — Adoption monitoring & enablement

*Type:* Technical — Track usage signals and deliver targeted enablement to deepen adoption over time.

- **[P1 — Assisted](proficiency_scale.md#p1):** Tracks basic usage metrics and flags low-adoption accounts for a reviewer to act on.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently monitors adoption signals and delivers standard enablement to lift feature usage.
- **[P3 — Proficient](proficiency_scale.md#p3):** Diagnoses ambiguous adoption gaps and designs targeted enablement that reliably moves usage.
- **[P4 — Expert](proficiency_scale.md#p4):** Builds the adoption-measurement and enablement frameworks the team adopts as standard.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the adoption strategy and predicts which usage patterns precede expansion or churn.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes how the discipline defines healthy adoption and is externally credible on enablement practice.

#### Account Health & Retention

<a id="csm-03"></a>
##### CSM-03 — Account health & churn management

*Type:* Technical — Score account health from leading indicators and intervene proactively to prevent churn.

- **[P1 — Assisted](proficiency_scale.md#p1):** Updates health scores from defined inputs and escalates declining accounts to a reviewer.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently assesses account health and runs standard interventions on at-risk accounts.
- **[P3 — Proficient](proficiency_scale.md#p3):** Interprets conflicting health signals, diagnoses root causes, and is the go-to on hard cases.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the health-scoring model and intervention playbooks others rely on.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets churn-management strategy and anticipates emerging drivers of attrition across the book.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice account health for the field and influences how others measure churn.

<a id="csm-04"></a>
##### CSM-04 — Renewal & expansion management

*Type:* Behavioral — Forecast, negotiate, and close renewals while growing upsell and cross-sell.

- **[P1 — Assisted](proficiency_scale.md#p1):** Prepares renewal paperwork and flags upcoming dates, with quotes and terms reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently runs straightforward renewals and surfaces routine expansion opportunities.
- **[P3 — Proficient](proficiency_scale.md#p3):** Negotiates complex multi-stakeholder renewals and structures expansion deals autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the renewal and expansion playbook and closes the deals others can't.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets renewal and expansion strategy and forecasts where account growth is heading.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what world-class renewal and expansion looks like and is sought for that authority.

<a id="csm-05"></a>
##### CSM-05 — Risk identification & save planning

*Type:* Behavioral — Detect at-risk accounts and orchestrate cross-functional recovery and retention plays.

- **[P1 — Assisted](proficiency_scale.md#p1):** Identifies obvious risk signals and logs them for a reviewer to assess and act.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently spots common risks and executes standard save plans on routine cases.
- **[P3 — Proficient](proficiency_scale.md#p3):** Detects subtle, ambiguous risk early and builds save plans that recover hard accounts.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the risk-detection signals and save methodology the team adopts.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets save strategy and anticipates systemic risks before they surface across the portfolio.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines the discipline's standard for risk and retention and is externally recognized for it.

#### Value & Success Planning

<a id="csm-06"></a>
##### CSM-06 — Success planning & business reviews

*Type:* Behavioral — Build joint success plans and run reviews that align on goals, progress, and next steps.

- **[P1 — Assisted](proficiency_scale.md#p1):** Assembles business-review materials from templates, with content reviewed before delivery.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently builds success plans and runs standard business reviews with customers.
- **[P3 — Proficient](proficiency_scale.md#p3):** Crafts executive-level success plans for complex accounts and leads ambiguous, high-stakes reviews.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the success-planning and review framework others follow and coaches them on it.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the strategy linking success plans to outcomes and anticipates shifts in customer priorities.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what great success planning means for the profession and is externally credible on it.

<a id="csm-07"></a>
##### CSM-07 — Customer outcome & value realization

*Type:* Behavioral — Define target outcomes and quantify realized value to justify continued investment.

- **[P1 — Assisted](proficiency_scale.md#p1):** Collects outcome data and populates value summaries for a reviewer to validate.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently maps customer goals to metrics and reports realized value on standard accounts.
- **[P3 — Proficient](proficiency_scale.md#p3):** Quantifies value in ambiguous cases and is the go-to for proving complex business outcomes.
- **[P4 — Expert](proficiency_scale.md#p4):** Builds the value-realization methodology and ROI models the team adopts.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets value-measurement strategy and anticipates how customers will define success next.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines how the industry measures customer value and shapes outcome-realization practice.

<a id="csm-08"></a>
##### CSM-08 — Strategic account growth planning

*Type:* Behavioral — Map account whitespace and stakeholders to chart multi-year growth and expansion.

- **[P1 — Assisted](proficiency_scale.md#p1):** Gathers account background and drafts growth notes for a reviewer to refine.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently builds growth plans for individual accounts using standard approaches.
- **[P3 — Proficient](proficiency_scale.md#p3):** Develops multi-year growth strategies for complex accounts and navigates ambiguous stakeholder maps.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the strategic account-planning method others adopt and unlocks stalled growth.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets portfolio-level growth strategy and anticipates where strategic accounts are heading.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice strategic account growth for the field and is sought externally for it.

#### Advocacy & Voice of Customer

<a id="csm-09"></a>
##### CSM-09 — Customer advocacy & voice-of-customer

*Type:* Behavioral — Cultivate references and advocates while channeling structured feedback into the business.

- **[P1 — Assisted](proficiency_scale.md#p1):** Captures customer feedback and references for a reviewer to route or act on.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently runs standard advocacy programs and channels routine feedback to teams.
- **[P3 — Proficient](proficiency_scale.md#p3):** Synthesizes ambiguous feedback into actionable insight and cultivates strong references autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the voice-of-customer program and advocacy framework the organization adopts.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets advocacy strategy and anticipates which customer signals should shape direction.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines how the discipline practices voice-of-customer and is externally credible on advocacy.

### Customer Support & Service Operations (SUP)

#### Case & Queue Management

<a id="sup-01"></a>
##### SUP-01 — Case management & triage

*Type:* Technical — Capture, categorize, and route service cases by urgency and impact for efficient resolution.

- **[P1 — Assisted](proficiency_scale.md#p1):** Logs and categorizes incoming cases per defined rules, with prioritization reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently triages and manages standard cases through resolution with normal oversight.
- **[P3 — Proficient](proficiency_scale.md#p3):** Handles ambiguous, high-volume triage decisions and is the go-to for tricky case prioritization.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the triage model and case-handling standards the team adopts.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets case-management strategy and anticipates how demand patterns will shift triage needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice case triage for the discipline and influences how others structure it.

<a id="sup-02"></a>
##### SUP-02 — Service-level & queue management

*Type:* Technical — Monitor and balance work queues against service-level targets to control resolution times.

- **[P1 — Assisted](proficiency_scale.md#p1):** Monitors queues against targets and flags breaches for a reviewer to address.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently manages queues to meet service levels under routine load variation.
- **[P3 — Proficient](proficiency_scale.md#p3):** Balances competing queues under pressure and is the go-to for keeping SLAs intact in hard conditions.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the queue-management and SLA strategy others follow.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets service-level strategy and anticipates demand shifts before they threaten targets.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what excellent service-level management means for the field and is externally credible.

<a id="sup-03"></a>
##### SUP-03 — Issue diagnosis & resolution

*Type:* Technical — Investigate reported problems systematically and apply or develop fixes to restore service.

- **[P1 — Assisted](proficiency_scale.md#p1):** Resolves well-defined issues using known steps, escalating anything unfamiliar.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently diagnoses and resolves standard issues with normal review of tricky ones.
- **[P3 — Proficient](proficiency_scale.md#p3):** Solves ambiguous, multi-factor problems and is the go-to for the hardest tickets.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines diagnostic approaches others adopt and resolves issues no one else can.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets resolution strategy and anticipates emerging failure modes before they spread.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines the discipline's standard for diagnosis and is sought externally for hard problems.

#### Escalation & Incident Handling

<a id="sup-04"></a>
##### SUP-04 — Escalation & incident communication

*Type:* Behavioral — Manage tiered escalations and keep customers informed through service-impacting incidents.

- **[P1 — Assisted](proficiency_scale.md#p1):** Follows the escalation script and posts status updates that are reviewed before sending.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently manages standard escalations and communicates clearly through routine incidents.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns communication on ambiguous, high-pressure incidents and is the go-to under crisis.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the escalation and incident-communication protocols the team adopts.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets incident-communication strategy and anticipates stakeholder needs in major events.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice incident communication for the discipline and is externally recognized.

<a id="sup-05"></a>
##### SUP-05 — Problem & root-cause management

*Type:* Technical — Analyze recurring issues to identify root causes and drive permanent corrective actions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Gathers incident details and documents findings for a reviewer to analyze.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently runs root-cause analysis on standard recurring problems with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Untangles ambiguous, systemic root causes and is the go-to for elusive recurring issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the problem-management methodology others adopt and cracks the hardest root causes.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets problem-management strategy and anticipates systemic failures before they recur.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines how the discipline practices root-cause management and shapes industry approaches.

#### Self-Service & Knowledge

<a id="sup-06"></a>
##### SUP-06 — Knowledge base & self-service design

*Type:* Technical — Design and curate knowledge content and self-service experiences that deflect and resolve issues.

- **[P1 — Assisted](proficiency_scale.md#p1):** Drafts knowledge articles from templates, with accuracy and clarity reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently authors and maintains standard self-service content to defined quality.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs self-service content for ambiguous needs and is the go-to for tough knowledge gaps.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the knowledge architecture and authoring standards the team adopts.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets self-service strategy and anticipates what customers will need to solve themselves.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice knowledge and self-service design for the field and is externally credible.

<a id="sup-07"></a>
##### SUP-07 — Support automation & deflection design

*Type:* Technical — Build automated assist and routing flows that resolve common requests without agent effort.

- **[P1 — Assisted](proficiency_scale.md#p1):** Configures simple automated responses from defined patterns, with logic reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently builds standard deflection flows and tunes them to routine demand.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs automation for ambiguous, high-impact cases and is the go-to for complex deflection.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the automation and deflection framework others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets deflection strategy and anticipates which interactions automation should absorb next.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines how the discipline approaches support automation and shapes industry practice.

#### Quality & Performance

<a id="sup-08"></a>
##### SUP-08 — Quality assurance & CSAT management

*Type:* Technical — Audit interactions against quality standards and manage satisfaction metrics to improve service.

- **[P1 — Assisted](proficiency_scale.md#p1):** Scores cases against a defined rubric and flags issues for a reviewer.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently audits quality and manages routine CSAT follow-up with normal oversight.
- **[P3 — Proficient](proficiency_scale.md#p3):** Interprets ambiguous quality signals and is the go-to for improving stubborn CSAT problems.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the quality rubric and CSAT-improvement program the team adopts.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets quality and satisfaction strategy and anticipates emerging drivers of customer sentiment.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what support quality means for the discipline and is externally credible on it.

<a id="sup-09"></a>
##### SUP-09 — Support operations analytics & forecasting

*Type:* Technical — Analyze support data and forecast demand to inform staffing, trends, and performance.

- **[P1 — Assisted](proficiency_scale.md#p1):** Compiles support metrics into standard reports for a reviewer to interpret.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently analyzes operational data and produces routine forecasts with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Models ambiguous demand patterns and is the go-to for reliable forecasts in volatile conditions.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the analytics and forecasting methodology others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets analytics strategy and anticipates how operational dynamics will shift forecasting needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice support analytics for the field and is sought externally for it.

#### Workforce & Capacity

<a id="sup-10"></a>
##### SUP-10 — Workforce & shift planning for support

*Type:* Technical — Forecast contact volume and schedule staff to meet coverage and service-level requirements.

- **[P1 — Assisted](proficiency_scale.md#p1):** Slots agents into shifts using a defined schedule, with coverage reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently builds standard schedules that meet routine coverage requirements.
- **[P3 — Proficient](proficiency_scale.md#p3):** Balances complex constraints and volatile demand and is the go-to for tough staffing puzzles.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the workforce-planning model and scheduling standards others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets workforce strategy and anticipates capacity needs ahead of demand shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice support workforce planning for the discipline and is externally credible.

### Finance & Accounting (FIN)

#### Planning, Budgeting & Analysis

<a id="fin-01"></a>
##### FIN-01 — Financial planning & analysis (FP&A)

*Type:* Technical — Builds forecasts, budgets, and variance analysis to guide resource allocation and performance.

- **[P1 — Assisted](proficiency_scale.md#p1):** Pulls data and updates planning templates, with analysis reviewed before use.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently builds standard analyses and variance reports with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Analyzes ambiguous business drivers and is the go-to for hard planning questions.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the FP&A approach and analytical frameworks others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets FP&A strategy and anticipates how business dynamics will reshape planning.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what excellent FP&A means for the profession and is externally credible on it.

<a id="fin-02"></a>
##### FIN-02 — Budgeting & forecasting

*Type:* Technical — Develops operating and capital budgets and rolling forecasts aligned to financial targets.

- **[P1 — Assisted](proficiency_scale.md#p1):** Enters budget inputs and updates forecast templates, with figures reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently prepares standard budgets and forecasts with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Builds forecasts under high uncertainty and is the go-to for reconciling conflicting assumptions.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the budgeting and forecasting methodology others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets forecasting strategy and anticipates shifts that will challenge planning assumptions.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice budgeting and forecasting for the field and is sought externally for it.

<a id="fin-03"></a>
##### FIN-03 — Financial modeling & valuation

*Type:* Technical — Constructs quantitative models to value assets, businesses, and scenarios for decisions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Populates model inputs and runs defined scenarios, with outputs reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently builds standard models and valuations with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Models ambiguous, complex situations and is the go-to for defensible valuations.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines modeling standards and valuation approaches others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets modeling strategy and anticipates which methods best fit emerging situations.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what rigorous financial modeling means for the profession and is externally recognized.

<a id="fin-04"></a>
##### FIN-04 — Capital planning & investment appraisal

*Type:* Technical — Evaluates capital projects using cash flow, payback, and return metrics to prioritize funding.

- **[P1 — Assisted](proficiency_scale.md#p1):** Gathers project data and computes defined metrics, with appraisals reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently appraises standard investments and prepares routine capital plans.
- **[P3 — Proficient](proficiency_scale.md#p3):** Evaluates ambiguous, high-stakes investments and is the go-to for tough capital decisions.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the appraisal methodology and capital-planning framework others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets capital-allocation strategy and anticipates how priorities will reshape investment.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice capital planning for the discipline and is externally credible on it.

#### Accounting & Reporting

<a id="fin-05"></a>
##### FIN-05 — Accounting & financial reporting

*Type:* Technical — Records transactions and prepares financial statements per applicable accounting standards.

- **[P1 — Assisted](proficiency_scale.md#p1):** Prepares routine entries and report sections per standards, with work reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently produces standard financial statements and disclosures with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Handles ambiguous accounting treatments and is the go-to for complex reporting judgments.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines reporting standards and accounting policy the team adopts.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets reporting strategy and anticipates how evolving standards will affect disclosure.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice financial reporting for the profession and shapes how others apply it.

<a id="fin-06"></a>
##### FIN-06 — Management & cost accounting

*Type:* Technical — Allocates and analyzes costs to support pricing, profitability, and management decisions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Compiles cost data and updates standard cost reports, with allocations reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently prepares routine cost analyses and management reports with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs costing for ambiguous cases and is the go-to for complex allocation and margin questions.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the costing methodology and management-reporting framework others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets cost-accounting strategy and anticipates how business changes will reshape costing.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice management and cost accounting for the field and is externally credible.

<a id="fin-07"></a>
##### FIN-07 — Revenue recognition & billing operations

*Type:* Technical — Applies revenue standards and operates billing cycles to recognize and invoice earned revenue.

- **[P1 — Assisted](proficiency_scale.md#p1):** Processes routine billing and revenue entries per rules, with work reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently handles standard revenue recognition and billing with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves ambiguous recognition cases and is the go-to for complex contract and billing scenarios.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines revenue-recognition policy and billing-operations standards others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets revenue strategy and anticipates how new arrangements will affect recognition.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice revenue recognition for the profession and is sought externally for it.

<a id="fin-08"></a>
##### FIN-08 — General ledger & financial close

*Type:* Technical — Manages ledger integrity and reconciliations for accurate, timely period-end closes.

- **[P1 — Assisted](proficiency_scale.md#p1):** Posts routine entries and reconciliations per checklist, with work reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently runs standard close tasks and reconciliations with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves ambiguous close issues and is the go-to for keeping a complex close on track.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the close process and ledger-control standards others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets close strategy and anticipates how complexity will challenge the close.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice ledger and close management for the field and is externally credible.

#### Treasury & Capital

<a id="fin-09"></a>
##### FIN-09 — Treasury & cash management

*Type:* Technical — Manages liquidity, cash positioning, and short-term funding to optimize working capital.

- **[P1 — Assisted](proficiency_scale.md#p1):** Records cash positions and processes routine transactions, with work reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently manages standard cash operations and short-term liquidity with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Manages ambiguous liquidity situations and is the go-to for tough cash-flow decisions.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the treasury and liquidity-management framework others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets treasury strategy and anticipates liquidity needs before they materialize.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice treasury and cash management for the discipline and is externally recognized.

<a id="fin-10"></a>
##### FIN-10 — Financial risk management & hedging

*Type:* Technical — Mitigates currency, rate, credit, and commodity exposures using hedging instruments.

- **[P1 — Assisted](proficiency_scale.md#p1):** Gathers exposure data and applies defined hedging steps, with work reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently monitors standard risks and executes routine hedges with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Assesses ambiguous, complex exposures and is the go-to for structuring difficult hedges.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the risk-management and hedging methodology others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets risk strategy and anticipates emerging exposures before they materialize.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice financial risk management for the profession and shapes industry practice.

<a id="fin-11"></a>
##### FIN-11 — Investor relations & capital markets

*Type:* Behavioral — Communicates performance and strategy to investors to support capital access and valuation.

- **[P1 — Assisted](proficiency_scale.md#p1):** Assembles investor materials from templates, with content reviewed before release.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently prepares standard investor communications and handles routine inquiries.
- **[P3 — Proficient](proficiency_scale.md#p3):** Navigates ambiguous market questions and is the go-to for tough investor conversations.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the investor-relations and capital-markets approach others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets IR strategy and anticipates how market sentiment will shape positioning.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice investor relations for the field and is externally credible on it.

#### Tax, Controls & Assurance

<a id="fin-12"></a>
##### FIN-12 — Tax planning & compliance

*Type:* Technical — Plans tax positions and prepares filings to optimize liability while meeting obligations.

- **[P1 — Assisted](proficiency_scale.md#p1):** Prepares routine tax filings and gathers documentation, with work reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently handles standard compliance and filings with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves ambiguous tax positions and is the go-to for complex planning questions.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines tax-planning approaches and compliance standards others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets tax strategy and anticipates how regulatory change will affect positions.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice tax planning for the profession and is sought externally for it.

<a id="fin-13"></a>
##### FIN-13 — Internal controls & financial governance

*Type:* Technical — Designs and operates control frameworks for reliable financial reporting and asset safety.

- **[P1 — Assisted](proficiency_scale.md#p1):** Performs assigned control checks and documents results, with work reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently operates and tests standard controls with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Diagnoses ambiguous control gaps and is the go-to for designing robust controls.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the control framework and governance standards others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets controls strategy and anticipates emerging risks that controls must address.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice financial governance for the discipline and is externally credible on it.

<a id="fin-14"></a>
##### FIN-14 — External & financial audit coordination

*Type:* Technical — Plans and executes audit activities to verify accuracy and assess control effectiveness.

- **[P1 — Assisted](proficiency_scale.md#p1):** Collects requested evidence and tracks audit items, with submissions reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently manages standard audit requests and routine auditor liaison with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Handles ambiguous audit matters and is the go-to for keeping a complex audit on track.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the audit-coordination approach and readiness standards others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets audit-coordination strategy and anticipates scrutiny before it arises.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice audit coordination for the field and is externally recognized for it.

### Procurement & Vendor Management (PROC)

#### Sourcing & Selection

<a id="proc-01"></a>
##### PROC-01 — Sourcing strategy & supplier selection

*Type:* Technical — Develops sourcing strategies and evaluates suppliers to select best-fit sources of supply.

- **[P1 — Assisted](proficiency_scale.md#p1):** Gathers supplier information and scores bids against criteria others define, with selections reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs standard sourcing events end-to-end, shortlisting suppliers and recommending awards for routine categories.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs sourcing approaches for ambiguous or complex needs and defends selection decisions to stakeholders.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines selection methodologies and weighting models that other sourcing professionals adopt across categories.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organizational sourcing strategy and anticipates shifts in supply markets that reshape selection.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines industry practice for evidence-based supplier selection and is cited externally as authoritative.

<a id="proc-02"></a>
##### PROC-02 — Category management

*Type:* Technical — Segments spend into categories and applies tailored strategies to maximize value.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains category spend data and supplier lists under direction, flagging anomalies for review.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages a defined category, tracking spend, suppliers, and renewals with routine guidance.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns complex categories, building multi-year category plans that balance cost, risk, and innovation.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the category management operating model and coaches managers on advanced category strategy.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise category strategy and predicts category market trends years ahead.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Pioneers category management frameworks adopted as reference practice across the profession.

<a id="proc-03"></a>
##### PROC-03 — Competitive bidding & tendering

*Type:* Technical — Designs and runs structured solicitation and evaluation to award competitive deals.

- **[P1 — Assisted](proficiency_scale.md#p1):** Assembles tender documents and logs supplier responses against checklists, with steps reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs standard tenders independently, managing timelines, clarifications, and evaluation logistics.
- **[P3 — Proficient](proficiency_scale.md#p3):** Structures complex tenders with intricate requirements and resolves disputes and ambiguous responses.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines tendering methods and evaluation frameworks others use for high-stakes competitions.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the organization's competitive bidding strategy and shapes how markets respond to its tenders.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Establishes recognized standards for fair, defensible tendering across the discipline.

#### Contracts & Negotiation

<a id="proc-04"></a>
##### PROC-04 — Supplier contract negotiation & administration

*Type:* Behavioral — Negotiates terms and administers contracts for favorable, enforceable agreements.

- **[P1 — Assisted](proficiency_scale.md#p1):** Tracks contract terms and renewal dates and prepares standard clauses under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Negotiates routine contract terms and administers agreements within established mandates.
- **[P3 — Proficient](proficiency_scale.md#p3):** Leads complex negotiations, handling difficult counterparties and crafting bespoke commercial terms.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines negotiation playbooks and contract standards that other negotiators adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets contracting strategy and anticipates legal and commercial shifts affecting supplier agreements.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes contracting practice recognized industry-wide as the benchmark for sound supplier agreements.

#### Supplier Performance & Risk

<a id="proc-05"></a>
##### PROC-05 — Supplier relationship & performance management

*Type:* Behavioral — Builds supplier partnerships and monitors performance against service and value expectations.

- **[P1 — Assisted](proficiency_scale.md#p1):** Collects supplier performance data and updates scorecards with results reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages routine supplier relationships, running reviews and tracking SLAs independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns critical supplier relationships, resolving conflicts and driving performance improvement under ambiguity.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs SRM frameworks and performance models that others adopt across the supplier base.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise supplier relationship strategy and foresees how key partnerships should evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what excellent supplier partnership means for the profession and is externally credible.

<a id="proc-06"></a>
##### PROC-06 — Supplier risk & compliance

*Type:* Technical — Assesses and mitigates supplier financial, operational, and continuity risks.

- **[P1 — Assisted](proficiency_scale.md#p1):** Runs supplier risk checklists and compliance screens, escalating findings for review.
- **[P2 — Independent](proficiency_scale.md#p2):** Assesses routine supplier risks and verifies compliance against standard requirements independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Evaluates complex, ambiguous supplier risks and designs mitigation for critical exposures.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines supplier risk frameworks and compliance controls others apply across the supply base.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets supplier risk strategy and anticipates emerging regulatory and supply-chain threats.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Pioneers supplier risk and compliance practice regarded as authoritative across the industry.

#### Spend & Operations

<a id="proc-07"></a>
##### PROC-07 — Spend analysis & cost optimization

*Type:* Technical — Analyzes spend to identify savings, consolidation, and total-cost-of-ownership opportunities.

- **[P1 — Assisted](proficiency_scale.md#p1):** Cleans and categorizes spend data and produces standard reports under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Analyzes spend independently to identify routine savings and reports cost opportunities.
- **[P3 — Proficient](proficiency_scale.md#p3):** Uncovers complex savings across fragmented spend and builds defensible optimization business cases.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines spend analytics methods and cost-optimization approaches that others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise cost strategy and predicts where structural savings will emerge.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best practice for spend intelligence and cost optimization across the discipline.

<a id="proc-08"></a>
##### PROC-08 — Procure-to-pay process management

*Type:* Technical — Optimizes the end-to-end procure-to-pay cycle for accuracy, speed, control, and cash efficiency.

- **[P1 — Assisted](proficiency_scale.md#p1):** Processes requisitions, orders, and invoices following defined procedures, with exceptions escalated.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages routine procure-to-pay flows independently and resolves common exceptions.
- **[P3 — Proficient](proficiency_scale.md#p3):** Handles complex P2P exceptions and redesigns local process steps to remove friction.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines P2P process and control standards that operators across the function adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets P2P strategy and anticipates how processes should evolve for control and efficiency.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Establishes procure-to-pay practice recognized as the benchmark across the profession.

### People & Talent (HR) (HR)

#### Talent Acquisition

<a id="hr-01"></a>
##### HR-01 — Talent acquisition & recruiting

*Type:* Behavioral — Owns end-to-end sourcing, assessment, and offer to fill roles with qualified candidates.

- **[P1 — Assisted](proficiency_scale.md#p1):** Screens applications and schedules interviews against defined criteria, with decisions reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages requisitions end-to-end for standard roles, sourcing and closing candidates independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Fills hard-to-source and senior roles, handling ambiguous needs and complex stakeholder demands.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines recruiting methods and assessment approaches that other recruiters adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets talent acquisition strategy and anticipates shifts in talent markets and hiring needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes recruiting practice recognized industry-wide as the standard for effective hiring.

<a id="hr-02"></a>
##### HR-02 — Employer branding & candidate experience

*Type:* Behavioral — Shapes market reputation and candidate journey to attract and convert talent.

- **[P1 — Assisted](proficiency_scale.md#p1):** Publishes branded content and gathers candidate feedback following defined guidelines.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs standard employer-branding activities and improves candidate touchpoints independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Crafts compelling employer narratives and resolves complex candidate-experience breakdowns.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines branding and candidate-experience frameworks that other practitioners adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets employer-brand strategy and anticipates how talent perceptions and channels will shift.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what a leading employer brand and candidate experience look like for the field.

<a id="hr-03"></a>
##### HR-03 — Workforce sourcing strategy & pipelining

*Type:* Behavioral — Builds proactive talent pools and sourcing channels to meet future hiring demand.

- **[P1 — Assisted](proficiency_scale.md#p1):** Builds candidate lists and maintains talent pools using defined search criteria.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs proactive sourcing campaigns and sustains pipelines for routine roles independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs sourcing strategies for scarce skills and builds pipelines under high ambiguity.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines sourcing and pipelining methodologies that other sourcers adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise workforce-sourcing strategy and predicts future talent-supply gaps.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Pioneers talent-pipelining practice recognized as authoritative across the profession.

#### Total Rewards

<a id="hr-04"></a>
##### HR-04 — Total rewards & compensation design

*Type:* Technical — Designs pay structures, bands, and incentives that are equitable and market-competitive.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains pay data and benchmarks roles against defined bands, with results reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Conducts standard compensation analysis and recommends routine pay decisions independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs pay structures for complex roles and resolves contentious equity and market issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines compensation philosophy and design frameworks that other rewards professionals adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets total rewards strategy and anticipates market and regulatory shifts in pay.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes compensation-design practice regarded industry-wide as the benchmark.

<a id="hr-05"></a>
##### HR-05 — Benefits & wellbeing program management

*Type:* Technical — Administers health, retirement, leave, and wellbeing offerings across the workforce.

- **[P1 — Assisted](proficiency_scale.md#p1):** Administers enrollments and answers routine benefits questions following defined procedures.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages standard benefits and wellbeing programs and resolves common issues independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs benefits offerings for complex needs and resolves ambiguous coverage and vendor problems.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines benefits and wellbeing program frameworks that other administrators adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets benefits and wellbeing strategy and anticipates workforce-health and cost trends.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines leading practice for benefits and wellbeing across the discipline.

<a id="hr-06"></a>
##### HR-06 — Equity & long-term incentive administration

*Type:* Technical — Manages equity and long-term incentive programs and their governance and reporting.

- **[P1 — Assisted](proficiency_scale.md#p1):** Records grants and processes vesting events following defined procedures, with checks reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Administers standard equity and incentive plans independently, handling routine transactions.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves complex equity events and edge cases across grants, taxation, and reporting.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines equity-administration controls and processes that other administrators adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets long-term incentive administration strategy and anticipates regulatory and plan-design shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Establishes equity-administration practice recognized as the standard across the profession.

#### Learning & Org Development

<a id="hr-07"></a>
##### HR-07 — Learning & development program design

*Type:* Behavioral — Builds curricula, capability frameworks, and delivery models that grow workforce skills.

- **[P1 — Assisted](proficiency_scale.md#p1):** Assembles learning materials and schedules sessions against defined objectives, with content reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs and delivers standard learning programs independently for routine needs.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs learning solutions for complex skill gaps and ambiguous capability needs.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines instructional-design methods and learning frameworks that other designers adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise learning strategy and anticipates future capability and skill demands.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Pioneers learning-design practice recognized industry-wide as authoritative.

<a id="hr-08"></a>
##### HR-08 — Organizational development & culture programs

*Type:* Behavioral — Designs interventions that strengthen culture, values, and organizational effectiveness.

- **[P1 — Assisted](proficiency_scale.md#p1):** Supports culture initiatives and collects feedback following defined plans.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs standard OD and culture interventions independently for routine situations.
- **[P3 — Proficient](proficiency_scale.md#p3):** Diagnoses complex organizational dysfunction and designs interventions under high ambiguity.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines OD methods and culture-change frameworks that other practitioners adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets organizational-development strategy and anticipates cultural shifts the organization must make.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes OD and culture practice regarded as the benchmark across the discipline.

<a id="hr-09"></a>
##### HR-09 — Talent management & succession programs

*Type:* Behavioral — Owns frameworks for identifying, developing, and retaining critical and high-potential talent.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains talent and succession data and prepares review materials under direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs standard talent-review and succession cycles independently for defined populations.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs succession approaches for critical, ambiguous roles and resolves contested talent calls.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines talent-management and succession frameworks that other practitioners adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise succession strategy and anticipates future leadership and capability gaps.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines leading practice for talent management and succession across the profession.

<a id="hr-10"></a>
##### HR-10 — DEI program management

*Type:* Behavioral — Runs diversity, equity, and inclusion strategy, programs, and accountability measures.

- **[P1 — Assisted](proficiency_scale.md#p1):** Supports DEI activities and compiles representation data following defined plans.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs standard DEI programs independently and tracks routine progress measures.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs DEI interventions for complex, sensitive challenges under significant ambiguity.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines DEI program frameworks and measurement approaches that other practitioners adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise DEI strategy and anticipates shifts in equity expectations and regulation.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Pioneers DEI practice recognized externally as authoritative across the field.

#### HR Partnering & Employee Relations

<a id="hr-11"></a>
##### HR-11 — HR business partnering

*Type:* Behavioral — Advises leaders on people strategy, organizational issues, and workforce decisions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Answers routine manager queries and gathers people data, with guidance reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Advises managers on standard people matters independently within established policy.
- **[P3 — Proficient](proficiency_scale.md#p3):** Partners on complex, ambiguous people challenges and influences senior leaders' decisions.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines HR partnering approaches and coaching models that other partners adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the HR partnering operating model and anticipates the business's future people needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what excellent HR partnering means for the discipline and is externally credible.

<a id="hr-12"></a>
##### HR-12 — Employee relations & investigations

*Type:* Behavioral — Handles grievances, conduct concerns, and workplace investigations fairly and consistently.

- **[P1 — Assisted](proficiency_scale.md#p1):** Documents cases and gathers evidence following defined procedures, with steps reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Handles routine ER cases and conducts standard investigations independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Manages complex, high-risk investigations and resolves sensitive disputes under ambiguity.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines investigation methods and ER frameworks that other practitioners adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets employee-relations strategy and anticipates emerging workforce-conflict and legal risks.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Establishes ER and investigations practice recognized as the standard across the profession.

<a id="hr-13"></a>
##### HR-13 — Employee engagement & listening programs

*Type:* Behavioral — Runs surveys and feedback systems to measure and act on workforce sentiment.

- **[P1 — Assisted](proficiency_scale.md#p1):** Administers surveys and compiles engagement results following defined procedures.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs standard listening cycles independently and reports routine engagement insights.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs listening strategies for complex needs and turns ambiguous signals into action.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines engagement and listening frameworks that other practitioners adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise engagement strategy and anticipates shifts in workforce sentiment and expectations.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Pioneers employee-listening practice regarded industry-wide as authoritative.

#### People Operations & Compliance

<a id="hr-14"></a>
##### HR-14 — HR operations & lifecycle administration

*Type:* Technical — Administers accurate records and transactions across hire-to-retire lifecycle events.

- **[P1 — Assisted](proficiency_scale.md#p1):** Processes lifecycle transactions following defined procedures, escalating exceptions for review.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages routine HR operations and lifecycle events independently, resolving common issues.
- **[P3 — Proficient](proficiency_scale.md#p3):** Handles complex lifecycle exceptions and redesigns local processes to improve service.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines HR operations standards and controls that other administrators adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets HR operations strategy and anticipates how lifecycle services should evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Establishes HR operations practice recognized as the benchmark across the profession.

<a id="hr-15"></a>
##### HR-15 — HR compliance & employment law application

*Type:* Technical — Applies employment laws and regulations to policies, decisions, and practices.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies defined compliance checklists and flags potential issues for review.
- **[P2 — Independent](proficiency_scale.md#p2):** Applies standard employment-law requirements to routine situations independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Interprets ambiguous legal requirements and advises on complex compliance risks.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines compliance frameworks and interpretive guidance that other practitioners adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets HR compliance strategy and anticipates regulatory change affecting the workforce.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes employment-compliance practice regarded as authoritative across the discipline.

<a id="hr-16"></a>
##### HR-16 — People analytics & workforce planning

*Type:* Technical — Models workforce supply, demand, and trends to inform people decisions with data.

- **[P1 — Assisted](proficiency_scale.md#p1):** Compiles workforce data and produces standard reports under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds routine workforce analyses and forecasts independently for defined needs.
- **[P3 — Proficient](proficiency_scale.md#p3):** Models complex workforce scenarios and derives insight from ambiguous, messy data.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines analytics methods and workforce-planning models that other analysts adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets people-analytics strategy and anticipates the workforce shifts the organization must plan for.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Pioneers people-analytics and workforce-planning practice recognized as authoritative.

### Workplace, Facilities & Real Estate (WPL)

#### Facilities & Space

<a id="wpl-01"></a>
##### WPL-01 — Facilities & space management

*Type:* Technical — Plans, allocates, and maintains physical workspace to meet occupancy and operational needs.

- **[P1 — Assisted](proficiency_scale.md#p1):** Updates space records and processes facilities requests following defined procedures.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages routine space allocation and facilities services independently for standard needs.
- **[P3 — Proficient](proficiency_scale.md#p3):** Solves complex space and utilization challenges and plans moves under significant ambiguity.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines space-management standards and planning approaches that others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise space strategy and anticipates how workplace demand will evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines leading practice for facilities and space management across the discipline.

<a id="wpl-02"></a>
##### WPL-02 — Building operations & maintenance management

*Type:* Technical — Operates building systems and preventive maintenance to ensure reliable, safe facilities.

- **[P1 — Assisted](proficiency_scale.md#p1):** Logs maintenance requests and tracks routine tasks following defined procedures.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages standard building operations and planned maintenance independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves complex building failures and optimizes maintenance under operational ambiguity.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines maintenance and building-operations standards that other managers adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets building-operations strategy and anticipates asset-lifecycle and reliability needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Establishes building-operations practice recognized as the benchmark across the profession.

<a id="wpl-03"></a>
##### WPL-03 — Capital projects & fit-out delivery

*Type:* Technical — Delivers construction, renovation, and fit-out projects on scope, budget, and schedule.

- **[P1 — Assisted](proficiency_scale.md#p1):** Tracks project tasks and documents progress following defined plans, with work reviewed.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages standard fit-out projects independently, controlling scope, schedule, and budget.
- **[P3 — Proficient](proficiency_scale.md#p3):** Delivers complex projects and resolves difficult scope, cost, and contractor problems.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines project-delivery methods and fit-out standards that others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets capital-projects strategy and anticipates how the portfolio's space must change.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Pioneers capital-project delivery practice recognized industry-wide as authoritative.

#### Real Estate & Portfolio

<a id="wpl-04"></a>
##### WPL-04 — Real estate & lease management

*Type:* Technical — Manages the property portfolio, leases, and occupancy costs across locations.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains lease records and tracks critical dates following defined procedures.
- **[P2 — Independent](proficiency_scale.md#p2):** Administers leases and routine real-estate transactions independently within mandates.
- **[P3 — Proficient](proficiency_scale.md#p3):** Negotiates complex leases and resolves ambiguous occupancy and landlord disputes.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines lease-management and transaction standards that others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets real-estate strategy and anticipates market and occupancy shifts affecting the portfolio.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes real-estate and lease-management practice regarded as the benchmark.

<a id="wpl-05"></a>
##### WPL-05 — Workplace portfolio strategy & site selection

*Type:* Behavioral — Sets location strategy and evaluates sites against business, cost, and talent needs.

- **[P1 — Assisted](proficiency_scale.md#p1):** Compiles site and portfolio data and prepares comparison materials under direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Evaluates standard site options and supports routine portfolio decisions independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs site-selection approaches for complex needs and resolves competing location trade-offs.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines portfolio-strategy and site-selection frameworks that others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise portfolio strategy and anticipates how location needs will evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines leading practice for workplace portfolio strategy across the discipline.

#### Workplace Experience

<a id="wpl-06"></a>
##### WPL-06 — Workplace experience & services

*Type:* Behavioral — Designs on-site services and amenities that support productivity and employee experience.

- **[P1 — Assisted](proficiency_scale.md#p1):** Delivers routine workplace services and gathers user feedback following defined plans.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages standard workplace-experience services independently and resolves common issues.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs experience improvements for complex needs and resolves ambiguous service breakdowns.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines workplace-experience standards and service models that others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets workplace-experience strategy and anticipates shifts in employee expectations.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Pioneers workplace-experience practice recognized industry-wide as authoritative.

<a id="wpl-07"></a>
##### WPL-07 — Sustainability & energy management

*Type:* Technical — Manages energy use, emissions, and sustainability of the built environment and operations.

- **[P1 — Assisted](proficiency_scale.md#p1):** Records energy and sustainability data and runs standard reports under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages routine energy and sustainability initiatives independently for defined targets.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs sustainability and energy solutions for complex sites under significant ambiguity.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines sustainability and energy-management frameworks that others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets sustainability strategy and anticipates regulatory and resource shifts affecting the portfolio.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines leading practice for workplace sustainability and energy across the discipline.

#### Health, Safety & Security

<a id="wpl-08"></a>
##### WPL-08 — Environmental health & safety

*Type:* Technical — Ensures safe working conditions and compliance with occupational health and safety standards.

- **[P1 — Assisted](proficiency_scale.md#p1):** Conducts routine safety checks and logs incidents following defined procedures.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages standard EHS programs and investigations independently within policy.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves complex safety hazards and ambiguous compliance situations under risk.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines EHS standards and risk-assessment methods that others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets EHS strategy and anticipates emerging hazards and regulatory change.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Establishes environmental-health-and-safety practice recognized as authoritative across the field.

<a id="wpl-09"></a>
##### WPL-09 — Physical security & access management

*Type:* Technical — Protects people and premises through access control, monitoring, and security operations.

- **[P1 — Assisted](proficiency_scale.md#p1):** Monitors access systems and logs incidents following defined procedures.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages routine physical-security operations and access controls independently.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves complex security incidents and designs controls for ambiguous threats.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines physical-security standards and access frameworks that others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets physical-security strategy and anticipates emerging threats to people and assets.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Pioneers physical-security and access-management practice recognized industry-wide as authoritative.

### Legal, Privacy & Compliance (LEG)

#### Commercial & Transactional Law

<a id="leg-01"></a>
##### LEG-01 — Contract drafting & negotiation

*Type:* Technical — Draft, review, and negotiate contractual terms that allocate risk and obligations.

- **[P1 — Assisted](proficiency_scale.md#p1):** Drafts standard clauses from approved templates; flags deviations and negotiation points for supervising counsel review.
- **[P2 — Independent](proficiency_scale.md#p2):** Drafts and redlines routine commercial agreements independently, negotiating standard terms with normal counsel oversight.
- **[P3 — Proficient](proficiency_scale.md#p3):** Handles bespoke, high-ambiguity contracts and contentious negotiations autonomously; the go-to drafter for novel deal terms.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs clause libraries and negotiation playbooks others adopt; resolves drafting impasses that stall complex deals.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the organization's contracting standards and risk posture; anticipates emerging clauses and shifts negotiation strategy.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines contracting best practice recognized across the profession; authors model terms others treat as market standard.

<a id="leg-02"></a>
##### LEG-02 — Commercial & transactional law

*Type:* Technical — Advise on the legal structuring of commercial deals, financing, and transactions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Researches commercial-law questions and prepares routine transactional documents under close supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Advises on standard commercial matters and structures routine transactions independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves ambiguous commercial-law issues and structures non-standard deals autonomously; the local subject expert.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines transaction structures and risk frameworks others follow; cracks problems that stall sophisticated deals.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the firm's commercial-law approach and anticipates regulatory and market shifts affecting transactions.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes commercial-law practice industry-wide; externally cited authority on transactional structuring.

<a id="leg-03"></a>
##### LEG-03 — M&A & corporate transactions (legal)

*Type:* Technical — Provide legal support for due diligence, structuring, and execution of corporate transactions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Assembles diligence checklists and supporting documents for deals under senior supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs defined diligence workstreams and drafts routine deal documents independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Manages full deal legal workstreams and negotiates complex provisions autonomously through ambiguity.
- **[P4 — Expert](proficiency_scale.md#p4):** Architects deal structures and diligence approaches others adopt; resolves issues that threaten closing.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the organization's M&A legal strategy; anticipates structuring and regulatory risks across the deal lifecycle.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines deal-execution practice recognized industry-wide; sought externally on landmark transactions.

#### Corporate & Regulatory Counsel

<a id="leg-04"></a>
##### LEG-04 — Corporate & entity governance

*Type:* Technical — Maintain legal entity structures, board governance, and statutory corporate obligations.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains entity records and prepares routine corporate filings and minutes under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages governance for standard entities and prepares board materials independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Handles complex multi-entity governance and novel corporate-secretarial questions autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs governance structures and entity frameworks others adopt; resolves intractable governance conflicts.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise governance strategy and anticipates regulatory shifts affecting entity structures.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines governance best practice recognized across the field; externally credible authority.

<a id="leg-05"></a>
##### LEG-05 — Regulatory & licensing compliance

*Type:* Technical — Interpret and apply sector regulations, permits, and licensing requirements to operations.

- **[P1 — Assisted](proficiency_scale.md#p1):** Tracks licensing requirements and prepares routine regulatory filings under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages standard licensing and compliance obligations independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves ambiguous regulatory-interpretation questions and handles complex licensing autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs compliance approaches to novel regulation others adopt; resolves contested regulatory positions.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets regulatory strategy and engages regulators; anticipates emerging requirements ahead of enforcement.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes regulatory practice and interpretation industry-wide; externally recognized authority.

<a id="leg-06"></a>
##### LEG-06 — Intellectual property management

*Type:* Technical — Protect, register, and enforce trademarks, patents, copyrights, and trade secrets.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains IP records and prepares routine filings and renewals under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages standard IP portfolios and prosecution tasks independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Handles complex IP strategy, contested rights, and licensing questions autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs IP protection and enforcement strategies others adopt; resolves the hardest portfolio disputes.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise IP strategy aligned to business value; anticipates shifts in IP law and risk.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines IP-management practice recognized across the field; externally cited authority.

<a id="leg-07"></a>
##### LEG-07 — Employment & labor law advisory

*Type:* Technical — Advise on workforce legal matters including hiring, conduct, terminations, and labor relations.

- **[P1 — Assisted](proficiency_scale.md#p1):** Researches employment questions and drafts routine policy and correspondence under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Advises on standard employment matters and handles routine cases independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves ambiguous, high-stakes employment disputes and complex workforce questions autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines employment-risk frameworks and advisory approaches others adopt; solves the hardest cases.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise employment-law strategy; anticipates regulatory and workforce-law shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes employment-law practice industry-wide; externally recognized authority.

#### Dispute & Litigation Management

<a id="leg-08"></a>
##### LEG-08 — Litigation & dispute management

*Type:* Technical — Manage litigation strategy, proceedings, and resolution of legal disputes and claims.

- **[P1 — Assisted](proficiency_scale.md#p1):** Supports litigation by preparing documents and tracking deadlines under close supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages routine disputes and defined litigation tasks independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Drives complex, high-exposure litigation strategy and settlement decisions autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines dispute-strategy frameworks others adopt; resolves the most intractable, bet-the-company matters.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise litigation strategy and risk appetite; anticipates emerging dispute exposures.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines litigation-management practice recognized across the profession; externally credible authority.

<a id="leg-09"></a>
##### LEG-09 — Legal hold & evidence management

*Type:* Technical — Preserve, collect, and govern records and evidence in anticipation of proceedings.

- **[P1 — Assisted](proficiency_scale.md#p1):** Issues standard legal-hold notices and tracks acknowledgments under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages routine holds and evidence-preservation processes independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs and defends holds for complex, contested matters autonomously through ambiguity.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines preservation and collection methodologies others adopt; resolves spoliation-risk challenges.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise preservation strategy; anticipates evidentiary and regulatory shifts in discovery.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines evidence-preservation best practice recognized across the field; externally cited authority.

#### Data Protection & Privacy

<a id="leg-10"></a>
##### LEG-10 — Data protection & privacy law

*Type:* Technical — Apply data protection and privacy legal requirements to the handling of personal information.

- **[P1 — Assisted](proficiency_scale.md#p1):** Researches privacy-law questions and completes routine assessments under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Advises on standard privacy matters and conducts routine assessments independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves ambiguous cross-jurisdictional privacy questions and complex processing autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines privacy-law interpretation and risk frameworks others adopt; solves the hardest questions.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise privacy-law strategy; anticipates regulatory and enforcement shifts ahead of peers.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes privacy-law practice and interpretation industry-wide; externally recognized authority.

<a id="leg-11"></a>
##### LEG-11 — Privacy program management

*Type:* Technical — Operate the privacy governance program including rights handling, notices, and accountability.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains privacy-program records and supports defined controls under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Operates standard privacy-program processes and assessments independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Runs a full privacy program through ambiguity and complex incidents autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs privacy-program architectures and operating models others adopt; resolves the hardest gaps.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise privacy-program strategy; anticipates regulatory and operational shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines privacy-program best practice recognized across the field; externally credible authority.

#### Legal Operations & Advisory

<a id="leg-12"></a>
##### LEG-12 — Legal operations & matter management

*Type:* Technical — Run the legal function's intake, workflow, knowledge, and outside-counsel management.

- **[P1 — Assisted](proficiency_scale.md#p1):** Tracks matters and maintains legal-ops records and reports under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages standard matter-intake, vendor, and reporting processes independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Optimizes complex matter portfolios and resolves ambiguous operational issues autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs legal-ops processes and metrics frameworks others adopt; solves the hardest operating problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise legal-operations strategy; anticipates shifts in delivery models and tooling.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines legal-operations best practice recognized across the profession; externally cited authority.

<a id="leg-13"></a>
##### LEG-13 — Legal advisory & business partnering

*Type:* Behavioral — Provide practical, risk-balanced legal guidance to business stakeholders on decisions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Answers routine business questions and escalates appropriately under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Advises business stakeholders on standard matters independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Provides decisive counsel on ambiguous, high-stakes business questions autonomously; the trusted go-to advisor.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines advisory frameworks balancing legal risk and business value that others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the model for embedded legal partnering; anticipates business and legal-risk shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines business-partnering best practice recognized across the field; externally credible authority.

### Enterprise Risk, Audit & Governance (RISK)

#### Enterprise Risk Management

<a id="risk-01"></a>
##### RISK-01 — Enterprise risk management

*Type:* Technical — Identify, assess, treat, and monitor risks across the organization within a risk appetite.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains risk registers and gathers risk data under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Conducts standard risk assessments and updates registers independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Assesses complex, interconnected enterprise risks and sets local methodology autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the enterprise risk framework and appetite model others adopt; solves the hardest risk problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise risk strategy and appetite at board level; anticipates emerging systemic risks.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines enterprise-risk practice recognized industry-wide; externally cited authority.

<a id="risk-02"></a>
##### RISK-02 — Operational & financial risk assessment

*Type:* Technical — Evaluate process, operational, and financial exposures and recommend mitigating controls.

- **[P1 — Assisted](proficiency_scale.md#p1):** Collects data and completes defined risk-assessment templates under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Performs standard operational and financial risk assessments independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Assesses complex, ambiguous operational and financial risks autonomously; the local expert.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines assessment methodologies and quantification models others adopt; cracks the hardest analyses.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the organization's risk-assessment approach; anticipates emerging operational and financial exposures.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines risk-assessment best practice recognized across the field; externally credible authority.

<a id="risk-03"></a>
##### RISK-03 — Third-party & vendor risk

*Type:* Technical — Assess and monitor risks introduced by suppliers, partners, and outsourced relationships.

- **[P1 — Assisted](proficiency_scale.md#p1):** Completes vendor risk questionnaires and tracks assessments under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Conducts standard third-party risk assessments and monitoring independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Assesses complex, high-criticality vendor and supply-chain risks autonomously through ambiguity.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the third-party risk framework and tiering model others adopt; resolves the hardest exposures.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise third-party risk strategy; anticipates emerging supply-chain and concentration risks.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines third-party risk practice recognized industry-wide; externally cited authority.

#### Compliance Program Management

<a id="risk-04"></a>
##### RISK-04 — Regulatory compliance program management

*Type:* Technical — Design and operate programs ensuring ongoing adherence to applicable laws and regulations.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains compliance-program records and supports defined controls under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Operates standard compliance-program processes and assessments independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Runs a full compliance program through ambiguity and complex obligations autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs compliance-program architectures and operating models others adopt; resolves the hardest gaps.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise compliance-program strategy; anticipates regulatory shifts ahead of enforcement.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines compliance-program best practice recognized across the field; externally credible authority.

<a id="risk-05"></a>
##### RISK-05 — Compliance monitoring & regulatory reporting

*Type:* Technical — Track obligations, test adherence, and prepare required regulatory submissions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Compiles monitoring data and prepares routine regulatory reports under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Executes standard monitoring and reporting cycles independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs monitoring for complex obligations and resolves ambiguous reporting questions autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines monitoring and reporting methodologies others adopt; solves the hardest data and interpretation problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise monitoring and reporting strategy; anticipates shifts in regulatory expectations.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines compliance-monitoring best practice recognized industry-wide; externally cited authority.

#### Internal Audit & Controls

<a id="risk-06"></a>
##### RISK-06 — Internal audit & controls assurance

*Type:* Technical — Plan and execute independent audits to assess control effectiveness and provide assurance.

- **[P1 — Assisted](proficiency_scale.md#p1):** Executes defined audit test steps and documents results under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Conducts standard audits and assurance procedures independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Leads complex, high-risk audits and resolves contested findings autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines audit methodologies and risk-based approaches others adopt; cracks the hardest engagements.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the enterprise audit strategy and assurance model; anticipates emerging assurance needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines internal-audit practice recognized across the profession; externally credible authority.

<a id="risk-07"></a>
##### RISK-07 — Internal controls design & testing

*Type:* Technical — Define, document, and test control frameworks that mitigate key business risks.

- **[P1 — Assisted](proficiency_scale.md#p1):** Documents controls and executes defined test scripts under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Designs and tests standard controls independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs controls for complex processes and resolves ambiguous design gaps autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines control-design frameworks and testing methodologies others adopt; solves the hardest control problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the enterprise control-environment strategy; anticipates emerging control and automation needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines controls-design best practice recognized industry-wide; externally cited authority.

#### Governance, Policy & Ethics

<a id="risk-08"></a>
##### RISK-08 — Policy & standards governance

*Type:* Technical — Develop, approve, and maintain enterprise policies, standards, and their lifecycle.

- **[P1 — Assisted](proficiency_scale.md#p1):** Drafts routine policy updates from templates and tracks versions under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Develops and maintains standard policies and standards independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves ambiguous, cross-functional policy conflicts and authors complex standards autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the policy-governance framework and lifecycle others adopt; resolves the hardest policy tensions.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise policy-governance strategy; anticipates emerging policy and standards needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines policy-governance best practice recognized across the field; externally credible authority.

<a id="risk-09"></a>
##### RISK-09 — Ethics & conduct program management

*Type:* Behavioral — Foster ethical conduct through codes, training, and a culture of integrity.

- **[P1 — Assisted](proficiency_scale.md#p1):** Supports ethics-program operations and tracks training and disclosures under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Operates standard ethics and conduct processes independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Handles complex, sensitive conduct matters and ambiguous ethical questions autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs ethics-program architecture and culture measures others adopt; resolves the hardest dilemmas.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise ethics strategy and tone-at-the-top approach; anticipates emerging conduct risks.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines ethics-program best practice recognized industry-wide; externally cited authority.

<a id="risk-10"></a>
##### RISK-10 — Fraud prevention & investigations

*Type:* Technical — Detect, investigate, and respond to fraud, misconduct, and integrity violations.

- **[P1 — Assisted](proficiency_scale.md#p1):** Gathers evidence and documents investigation steps under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Conducts standard fraud investigations and control reviews independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Leads complex, high-stakes investigations and ambiguous fraud schemes autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines investigation methodologies and fraud-detection frameworks others adopt; cracks the hardest cases.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise fraud-risk strategy; anticipates emerging fraud schemes and exposures.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines fraud-investigation best practice recognized across the profession; externally credible authority.

#### Resilience & Continuity

<a id="risk-11"></a>
##### RISK-11 — Business continuity & resilience

*Type:* Technical — Plan and maintain capabilities to sustain and recover critical operations during disruption.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains continuity documentation and supports defined exercises under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Develops standard continuity plans and runs routine exercises independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs resilience for complex, interdependent operations and resolves ambiguous gaps autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the resilience framework and impact-analysis methodology others adopt; solves the hardest scenarios.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise resilience strategy; anticipates emerging disruption and concentration risks.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines resilience best practice recognized industry-wide; externally cited authority.

<a id="risk-12"></a>
##### RISK-12 — Crisis management & response coordination

*Type:* Behavioral — Coordinate organizational response, decision-making, and communication during crisis events.

- **[P1 — Assisted](proficiency_scale.md#p1):** Supports crisis logistics and documentation under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Coordinates defined crisis-response tasks and communications independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Leads response for complex, fast-moving crises and ambiguous decisions autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines crisis-response frameworks and command structures others adopt; steers the hardest crises.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise crisis-management strategy; anticipates emerging crisis scenarios and readiness gaps.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines crisis-management best practice recognized across the field; externally credible authority.

### Corporate Strategy & Executive Leadership (STRAT)

#### Strategy Formulation

<a id="strat-01"></a>
##### STRAT-01 — Corporate strategy formulation

*Type:* Behavioral — Define enterprise direction, scope, and competitive positioning to create durable advantage.

- **[P1 — Assisted](proficiency_scale.md#p1):** Gathers inputs and assembles analysis for strategy work under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Develops components of strategy and standard analyses independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Frames ambiguous strategic problems and shapes coherent strategy autonomously; the go-to strategist.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines strategy-formulation approaches others adopt; resolves the hardest strategic trade-offs.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the enterprise strategic direction; anticipates major shifts reshaping the competitive landscape.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines corporate-strategy practice recognized industry-wide; externally cited thought leader.

<a id="strat-02"></a>
##### STRAT-02 — Strategic planning & OKR cascading

*Type:* Behavioral — Translate strategy into multi-horizon plans and cascading objectives across the enterprise.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains planning artifacts and tracks objectives under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs standard planning cycles and cascades objectives independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs planning for complex, interdependent units and resolves misalignment autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the planning and goal-cascade methodology others adopt; fixes the hardest alignment failures.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the enterprise planning operating model; anticipates shifts in how strategy translates to execution.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines strategic-planning best practice recognized across the field; externally credible authority.

<a id="strat-03"></a>
##### STRAT-03 — Business model & innovation strategy

*Type:* Behavioral — Design and evolve how the organization creates, delivers, and captures value over time.

- **[P1 — Assisted](proficiency_scale.md#p1):** Researches business models and supports innovation analysis under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Develops standard business-model analyses and innovation cases independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs novel business models and resolves ambiguous innovation bets autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines business-model and innovation frameworks others adopt; cracks the hardest model problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise business-model and innovation strategy; anticipates disruptive shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines business-model innovation practice recognized industry-wide; externally cited thought leader.

<a id="strat-04"></a>
##### STRAT-04 — Scenario planning & strategic foresight

*Type:* Technical — Anticipate future conditions through scenarios and signals to stress-test strategic choices.

- **[P1 — Assisted](proficiency_scale.md#p1):** Gathers signals and supports scenario documentation under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Builds standard scenarios and trend analyses independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Constructs complex, ambiguous scenarios and derives strategic implications autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines foresight methodologies others adopt; surfaces the non-obvious futures others miss.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the enterprise foresight approach; anticipates structural shifts ahead of the market.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines strategic-foresight best practice recognized across the field; externally credible authority.

#### Market & Competitive Insight

<a id="strat-05"></a>
##### STRAT-05 — Market & competitive intelligence

*Type:* Technical — Analyze markets, customers, and rivals to inform positioning and strategic moves.

- **[P1 — Assisted](proficiency_scale.md#p1):** Collects market and competitor data and compiles routine briefs under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Produces standard competitive analyses and market assessments independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Synthesizes ambiguous signals into decisive competitive insight autonomously; the go-to analyst.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines intelligence methodologies and frameworks others adopt; cracks the hardest market questions.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the enterprise intelligence agenda; anticipates competitive and market shifts ahead of rivals.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines competitive-intelligence best practice recognized industry-wide; externally cited authority.

#### Corporate Development

<a id="strat-06"></a>
##### STRAT-06 — Mergers, acquisitions & corporate development

*Type:* Technical — Source, evaluate, and integrate inorganic growth opportunities including deals and partnerships.

- **[P1 — Assisted](proficiency_scale.md#p1):** Compiles target data and supports deal models under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Runs standard screening, modeling, and diligence workstreams independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Drives complex deal evaluation, structuring, and negotiation autonomously through ambiguity.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines deal-evaluation and integration frameworks others adopt; resolves the hardest deal problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the enterprise corporate-development strategy and portfolio direction; anticipates consolidation shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines corporate-development practice recognized industry-wide; externally credible authority on deals.

<a id="strat-07"></a>
##### STRAT-07 — Capital allocation & investment prioritization

*Type:* Technical — Allocate scarce capital across initiatives to maximize risk-adjusted enterprise returns.

- **[P1 — Assisted](proficiency_scale.md#p1):** Compiles investment data and supports prioritization analyses under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Evaluates standard investments and applies allocation criteria independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Prioritizes complex, competing investments under ambiguity and constraint autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines capital-allocation frameworks and hurdle models others adopt; resolves the hardest trade-offs.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the enterprise capital-allocation strategy; anticipates shifts in where value is created.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines capital-allocation best practice recognized across the field; externally cited authority.

<a id="strat-08"></a>
##### STRAT-08 — Business case & financial analysis

*Type:* Technical — Build rigorous financial cases and valuations to justify and compare major investments.

- **[P1 — Assisted](proficiency_scale.md#p1):** Builds routine financial models and gathers assumptions under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Develops standard business cases and analyses independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Constructs rigorous cases for complex, ambiguous decisions autonomously; the go-to analyst.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines business-case and modeling standards others adopt; cracks the hardest valuation problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the enterprise investment-analysis approach; anticipates shifts in value drivers and risk.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines business-case and financial-analysis best practice recognized industry-wide; externally credible authority.

#### Governance & Enterprise Leadership

<a id="strat-09"></a>
##### STRAT-09 — Board & governance leadership

*Type:* Behavioral — Engage boards and govern the enterprise with accountability, ethics, and fiduciary discipline.

- **[P1 — Assisted](proficiency_scale.md#p1):** Prepares board materials and tracks governance actions under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages standard board processes and reporting independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Steers complex board dynamics and ambiguous governance questions autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines board operating models and governance practices others adopt; resolves the hardest tensions.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the enterprise governance and board-effectiveness strategy; anticipates governance shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines board-governance best practice recognized across the field; externally credible authority.

<a id="strat-10"></a>
##### STRAT-10 — Enterprise transformation leadership

*Type:* Behavioral — Lead large-scale, cross-enterprise change to reshape the organization's operating model.

- **[P1 — Assisted](proficiency_scale.md#p1):** Supports transformation tracking and documentation under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Leads defined transformation workstreams independently with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Drives complex, cross-functional transformation through ambiguity and resistance autonomously.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines transformation approaches and operating models others adopt; rescues the hardest programs.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the enterprise transformation strategy; anticipates the shifts that make transformation necessary.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines transformation-leadership best practice recognized industry-wide; externally cited authority.

### Business & Revenue Operations (BIZ)

#### Operational Excellence

<a id="biz-01"></a>
##### BIZ-01 — Business operations & process improvement

*Type:* Behavioral — Design, run, and continuously improve core business processes for efficiency and quality.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maps and documents existing process steps under guidance, flagging obvious bottlenecks for review.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently runs standard process improvements, gathering data and implementing routine fixes with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously redesigns ambiguous, cross-team processes end-to-end and sets the local standard for how work flows.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the improvement methodology others adopt and untangles processes others find intractable.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets operational-excellence strategy across the business and anticipates where process capability must head next.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good operational practice means industry-wide and is sought externally for process expertise.

<a id="biz-02"></a>
##### BIZ-02 — Operating model & organization design

*Type:* Behavioral — Structure functions, roles, and workflows to align operations with strategy.

- **[P1 — Assisted](proficiency_scale.md#p1):** Documents current roles, handoffs, and reporting lines under direction for a single team.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently designs structure for one function, clarifying routine roles and decision rights with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously designs operating models for ambiguous multi-function areas, resolving overlap and accountability gaps.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines org-design approaches others follow and solves structural problems that have stumped leadership.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise operating-model strategy and anticipates structural shifts the organization will need.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes how the discipline conceives operating models and is externally recognized for the craft.

<a id="biz-03"></a>
##### BIZ-03 — Cross-functional initiative leadership

*Type:* Behavioral — Drive complex initiatives spanning multiple functions toward shared operational outcomes.

- **[P1 — Assisted](proficiency_scale.md#p1):** Coordinates tasks and tracks actions for a small initiative under a lead's guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently runs a defined cross-team initiative, managing routine dependencies and stakeholders with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously leads ambiguous, contentious initiatives spanning many functions to landed outcomes.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines how complex initiatives are run here and rescues efforts others cannot move.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the strategy and operating cadence for the organization's most critical cross-functional bets.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines industry-leading practice for cross-functional execution and is sought externally to teach it.

#### Revenue & GTM Operations

<a id="biz-04"></a>
##### BIZ-04 — Revenue operations & go-to-market systems

*Type:* Technical — Design and orchestrate end-to-end revenue processes across marketing, sales, and service.

- **[P1 — Assisted](proficiency_scale.md#p1):** Configures simple GTM workflow and field changes under supervision, following established conventions.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently builds and maintains standard revenue workflows and integrations with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously designs end-to-end GTM system architecture across marketing, sales, and success, handling messy edge cases.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the revenue-systems blueprint others adopt and solves integration problems others can't.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets RevOps systems strategy and anticipates how the GTM tech stack must evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good revenue operations looks like for the field and is externally credible on it.

<a id="biz-05"></a>
##### BIZ-05 — Revenue operations analytics

*Type:* Technical — Measure pipeline, conversion, and retention to optimize revenue performance and efficiency.

- **[P1 — Assisted](proficiency_scale.md#p1):** Pulls standard pipeline and funnel reports under guidance, checking figures before sharing.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently builds routine revenue analyses and dashboards, explaining trends with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously models ambiguous revenue questions end-to-end and becomes the trusted source for GTM numbers.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the analytical frameworks and metric definitions others adopt across revenue teams.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets revenue-analytics strategy and anticipates which signals will drive future growth decisions.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes how the discipline measures revenue performance and is recognized externally for the methods.

<a id="biz-06"></a>
##### BIZ-06 — Pricing, deal & monetization operations

*Type:* Technical — Operationalize pricing, quoting, and deal processes to maximize realized revenue.

- **[P1 — Assisted](proficiency_scale.md#p1):** Processes standard deal desk requests and applies approved discount rules under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently manages routine pricing approvals and deal structuring within set guardrails.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously structures complex, non-standard deals and sets local norms for monetization mechanics.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines deal-desk and monetization approaches others follow and cracks pricing problems others can't.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets monetization and pricing-operations strategy and anticipates shifts in how value is captured.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines leading practice for pricing operations across the field and is sought externally for it.

#### Planning & Performance

<a id="biz-07"></a>
##### BIZ-07 — Forecasting & planning operations

*Type:* Technical — Run cyclical forecasting and planning processes to align targets, capacity, and resources.

- **[P1 — Assisted](proficiency_scale.md#p1):** Updates forecast inputs and assembles planning templates under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently produces standard forecasts and plans, reconciling routine variances with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously builds forecasting models for ambiguous situations and owns the planning cadence end-to-end.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the forecasting methodology others adopt and resolves planning problems others cannot.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise planning strategy and anticipates the dynamics future forecasts must capture.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-in-class forecasting practice for the discipline and is externally recognized for it.

<a id="biz-08"></a>
##### BIZ-08 — Operational analytics & business intelligence

*Type:* Technical — Turn operational data into reporting and insight that drives business decisions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Builds basic reports and dashboards from defined requirements under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently delivers standard BI analyses and self-serve dashboards with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously frames ambiguous business questions and builds the analytics the organization relies on.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines BI standards, semantic models, and methods others adopt across the business.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the operational-analytics strategy and anticipates the decisions data must soon support.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes how the discipline practices business intelligence and is externally credible on it.

#### Data & Systems Operations

<a id="biz-09"></a>
##### BIZ-09 — Operational data governance & quality

*Type:* Technical — Steward the integrity, definitions, and quality of operational data across systems.

- **[P1 — Assisted](proficiency_scale.md#p1):** Performs defined data cleanup and quality checks under guidance, escalating anomalies.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently maintains data standards and resolves routine quality issues with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously designs governance and quality controls for ambiguous, messy data domains.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the governance framework others adopt and remediates data problems others can't.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise data-governance strategy and anticipates emerging quality and stewardship needs.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good operational data governance means for the field and is externally recognized.

<a id="biz-10"></a>
##### BIZ-10 — Business systems & workflow administration

*Type:* Technical — Configure and maintain business systems and automated workflows that run operations.

- **[P1 — Assisted](proficiency_scale.md#p1):** Performs routine system configuration and user support tasks under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently administers business systems and builds standard workflows with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously designs complex automations and system configurations, handling tricky edge cases.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines administration standards and architecture others adopt and fixes what others cannot.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets business-systems strategy and anticipates how the workflow platform landscape must evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines leading practice for business-systems administration and is sought externally for it.

### Program & Portfolio Management (PPM)

#### Portfolio Governance

<a id="ppm-01"></a>
##### PPM-01 — Portfolio prioritization & governance

*Type:* Behavioral — Select, sequence, and govern the enterprise portfolio to align investment with strategy.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains the portfolio inventory and prepares governance materials under direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently runs routine intake and prioritization scoring within an established framework.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously facilitates contentious prioritization and sets local governance standards across the portfolio.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the prioritization and governance model others adopt and resolves the toughest trade-offs.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise portfolio-governance strategy and anticipates shifts in investment priorities.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice portfolio governance for the discipline and is externally recognized for it.

<a id="ppm-02"></a>
##### PPM-02 — Benefits realization & value tracking

*Type:* Technical — Define, track, and verify the benefits and value delivered by portfolio investments.

- **[P1 — Assisted](proficiency_scale.md#p1):** Records benefit measures and tracks realization against plan under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently monitors benefits and reports realization, flagging routine shortfalls with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously defines value cases for ambiguous initiatives and owns realization tracking end-to-end.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the benefits-realization methodology others adopt and salvages value others miss.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise value-tracking strategy and anticipates how benefits should be measured next.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines leading benefits-realization practice for the field and is sought externally for it.

<a id="ppm-03"></a>
##### PPM-03 — Portfolio reporting & performance analytics

*Type:* Technical — Aggregate portfolio health, progress, and risk into insight for executive decisions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Compiles status data into standard portfolio reports under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently produces routine portfolio dashboards and performance summaries with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously builds analytics that surface portfolio risks and becomes the trusted reporting source.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines portfolio-reporting standards and metrics others adopt across programs.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets portfolio-analytics strategy and anticipates the signals leadership will need to steer.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Shapes how the discipline reports portfolio performance and is externally credible on it.

#### Program Delivery

<a id="ppm-04"></a>
##### PPM-04 — Program & dependency management (enterprise)

*Type:* Behavioral — Coordinate interrelated programs and cross-program dependencies toward strategic outcomes.

- **[P1 — Assisted](proficiency_scale.md#p1):** Tracks program tasks and logs cross-team dependencies under a manager's direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently runs a defined program, managing routine dependencies and milestones with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously orchestrates large enterprise programs, resolving tangled cross-program dependencies.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines how enterprise programs are run here and untangles dependency knots others can't.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise program-management strategy and anticipates systemic delivery constraints.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-in-class enterprise program management and is externally recognized for it.

<a id="ppm-05"></a>
##### PPM-05 — Project delivery methods & standards

*Type:* Technical — Establish and steward delivery methodologies, standards, and practices across the enterprise.

- **[P1 — Assisted](proficiency_scale.md#p1):** Applies prescribed delivery methods and templates to tasks under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently delivers standard projects using established methods with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously tailors delivery methods to ambiguous projects and sets the local standard.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the delivery methodology and standards others across teams adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the organization's delivery-method strategy and anticipates where practice must evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good delivery practice means for the discipline and is externally credible.

<a id="ppm-06"></a>
##### PPM-06 — Program risk, issue & quality assurance

*Type:* Technical — Assure program quality and manage risks and issues across the delivery portfolio.

- **[P1 — Assisted](proficiency_scale.md#p1):** Logs risks and issues and updates the register under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently manages routine risks, issues, and QA reviews with normal oversight.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously runs risk and assurance for complex programs, surfacing what others overlook.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the risk and quality-assurance approach others adopt and resolves systemic exposures.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise program-assurance strategy and anticipates emerging delivery risks.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines leading program-assurance practice for the field and is sought externally for it.

#### Resource & Financial Control

<a id="ppm-07"></a>
##### PPM-07 — Resource & capacity management (portfolio)

*Type:* Technical — Balance demand against people and capacity across the portfolio to optimize throughput.

- **[P1 — Assisted](proficiency_scale.md#p1):** Updates resource allocations and availability data under direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently manages routine resourcing and capacity plans across a few programs with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously balances contended capacity across the portfolio, resolving conflicts and bottlenecks.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the capacity-planning approach others adopt and solves the hardest allocation trade-offs.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets portfolio resource strategy and anticipates future capacity and skills constraints.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice portfolio capacity management and is externally recognized for it.

<a id="ppm-08"></a>
##### PPM-08 — Program financial management & cost control

*Type:* Technical — Plan, track, and control program budgets, costs, and financial performance to baseline.

- **[P1 — Assisted](proficiency_scale.md#p1):** Records program costs and updates budget trackers under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently manages a program budget, tracking spend and routine variances with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously controls complex program finances, forecasting and resolving ambiguous cost issues.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines program financial-control practices others adopt and recovers troubled budgets others can't.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise program-finance strategy and anticipates cost and funding pressures ahead.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines leading program financial-management practice and is sought externally for it.

### Operations & Supply Chain (SCM)

#### Planning & Demand

<a id="scm-01"></a>
##### SCM-01 — Demand planning & forecasting

*Type:* Technical — Predict demand using historical, market, and statistical signals to drive supply decisions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Maintains demand data and runs standard forecast updates under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently produces routine demand forecasts and adjusts for known seasonality with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously forecasts volatile, ambiguous demand and owns the forecasting process end-to-end.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the demand-planning methodology others adopt and forecasts what others can't model.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets demand-planning strategy and anticipates shifts in market and demand signals.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-in-class demand planning for the discipline and is externally recognized for it.

<a id="scm-02"></a>
##### SCM-02 — Supply & capacity planning

*Type:* Technical — Balance supply, capacity, and constraints against demand to create executable plans.

- **[P1 — Assisted](proficiency_scale.md#p1):** Updates supply and capacity plans from given inputs under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently builds routine supply plans, balancing standard constraints with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously plans supply under ambiguous constraints, resolving shortages and bottlenecks.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the supply-planning approach others adopt and solves constraint problems others can't.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets supply and capacity strategy and anticipates structural capacity needs ahead.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines leading supply-planning practice for the field and is sought externally for it.

<a id="scm-03"></a>
##### SCM-03 — Sales & operations planning

*Type:* Behavioral — Align commercial, financial, and operational plans through cross-functional consensus.

- **[P1 — Assisted](proficiency_scale.md#p1):** Prepares S&OP inputs and meeting materials under direction.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently runs routine S&OP cycles, reconciling standard supply-demand gaps with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously facilitates contentious S&OP, balancing trade-offs across functions to consensus.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the S&OP process others adopt and reconciles imbalances others cannot.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise S&OP strategy and anticipates the integrated-planning capabilities needed next.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice sales and operations planning and is externally recognized for it.

<a id="scm-04"></a>
##### SCM-04 — Supply chain network design

*Type:* Technical — Model and optimize facility and route structure to balance cost, service, and risk.

- **[P1 — Assisted](proficiency_scale.md#p1):** Gathers network data and runs predefined scenario models under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently models standard network changes and evaluates routine trade-offs with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously designs network configurations for ambiguous, multi-constraint problems end-to-end.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines network-design methods others adopt and solves optimization problems others can't.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets supply-chain network strategy and anticipates how the footprint must evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines leading network-design practice for the discipline and is externally credible on it.

#### Inventory & Materials

<a id="scm-05"></a>
##### SCM-05 — Inventory & materials management

*Type:* Technical — Plan, position, and control stock and material flows to meet service targets at optimal cost.

- **[P1 — Assisted](proficiency_scale.md#p1):** Records stock movements and performs counts under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently manages routine inventory levels and replenishment with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously optimizes inventory policy under ambiguous demand and supply variability.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines inventory-management methods others adopt and resolves chronic stock problems others can't.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets inventory strategy and anticipates how stocking and materials needs will shift.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice inventory management for the field and is externally recognized for it.

<a id="scm-06"></a>
##### SCM-06 — Warehousing & storage operations

*Type:* Technical — Manage receiving, storage, picking, and handling for accuracy, safety, and throughput.

- **[P1 — Assisted](proficiency_scale.md#p1):** Performs defined put-away, picking, and storage tasks under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently runs routine warehouse operations and standard slotting with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously optimizes warehouse flow and layout under ambiguous, high-variability conditions.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines warehousing methods and layouts others adopt and fixes operations others can't.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets warehousing strategy and anticipates future storage and throughput requirements.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines leading warehousing practice for the discipline and is sought externally for it.

#### Manufacturing & Production

<a id="scm-07"></a>
##### SCM-07 — Manufacturing & production operations

*Type:* Technical — Convert inputs into finished goods through planned, controlled, efficient production.

- **[P1 — Assisted](proficiency_scale.md#p1):** Performs defined production tasks and records output under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently runs standard production lines, handling routine variation with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously manages complex production with ambiguous disruptions, holding output and quality.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines production-operations methods others adopt and resolves problems others can't.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets manufacturing-operations strategy and anticipates how production capability must evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-in-class manufacturing operations and is externally recognized for it.

<a id="scm-08"></a>
##### SCM-08 — Production scheduling & shop-floor control

*Type:* Technical — Sequence, schedule, and monitor production to optimize throughput and on-time output.

- **[P1 — Assisted](proficiency_scale.md#p1):** Updates schedules and logs shop-floor status from given inputs under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently builds routine production schedules and manages standard sequencing with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously schedules under volatile constraints, rebalancing the floor to hold commitments.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines scheduling and control methods others adopt and resolves the hardest sequencing problems.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets shop-floor scheduling strategy and anticipates how control systems must evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines leading production-scheduling practice for the field and is sought externally for it.

<a id="scm-09"></a>
##### SCM-09 — Asset & maintenance management

*Type:* Technical — Sustain reliability of physical assets through preventive and corrective maintenance.

- **[P1 — Assisted](proficiency_scale.md#p1):** Records asset data and completes scheduled maintenance tasks under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently runs routine preventive maintenance and work orders with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously diagnoses ambiguous failures and optimizes maintenance strategy for critical assets.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines maintenance and reliability methods others adopt and solves failures others can't.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets asset-management strategy and anticipates lifecycle and reliability needs ahead.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice asset and reliability management and is externally recognized for it.

<a id="scm-10"></a>
##### SCM-10 — Quality management & control

*Type:* Technical — Define, inspect, and assure that products and processes meet quality standards.

- **[P1 — Assisted](proficiency_scale.md#p1):** Performs defined inspections and records quality results under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently runs routine quality controls and investigates standard defects with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously diagnoses ambiguous quality issues and sets local control standards end-to-end.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the quality-management system others adopt and resolves root causes others can't.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets enterprise quality strategy and anticipates emerging quality and compliance demands.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good quality management means for the discipline and is externally credible.

#### Logistics & Fulfillment

<a id="scm-11"></a>
##### SCM-11 — Logistics & distribution management

*Type:* Technical — Plan and execute movement and delivery of goods across transport modes and channels.

- **[P1 — Assisted](proficiency_scale.md#p1):** Schedules routine shipments and tracks deliveries under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently manages standard freight and distribution lanes with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously optimizes complex distribution under ambiguous disruptions and cost pressures.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines logistics methods and carrier strategy others adopt and resolves problems others can't.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets distribution strategy and anticipates how logistics networks must evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines leading logistics practice for the discipline and is externally recognized for it.

<a id="scm-12"></a>
##### SCM-12 — Order management & fulfillment

*Type:* Technical — Process, allocate, and fulfill orders accurately from capture through delivery and returns.

- **[P1 — Assisted](proficiency_scale.md#p1):** Processes standard orders and resolves routine exceptions under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently manages order flow and standard fulfillment issues with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously orchestrates complex multi-source fulfillment and resolves ambiguous exceptions.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines order-management practices others adopt and fixes fulfillment breakdowns others can't.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets fulfillment strategy and anticipates how order orchestration must evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice order management and fulfillment and is sought externally for it.

<a id="scm-13"></a>
##### SCM-13 — Reverse logistics & returns management

*Type:* Technical — Manage returns, repairs, recycling, and disposal flows to recover value and reduce waste.

- **[P1 — Assisted](proficiency_scale.md#p1):** Processes standard returns and records dispositions under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently manages routine returns flows and standard disposition rules with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously designs returns and recovery processes for ambiguous, high-volume situations.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines reverse-logistics methods others adopt and recovers value others can't.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets returns and circularity strategy and anticipates evolving recovery demands.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines leading reverse-logistics practice for the field and is externally recognized for it.

#### Service Operations

<a id="scm-14"></a>
##### SCM-14 — Service delivery operations

*Type:* Technical — Plan, deliver, and control execution of services to meet scope, quality, and timeliness.

- **[P1 — Assisted](proficiency_scale.md#p1):** Executes defined service tasks and logs outcomes under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently runs standard service delivery, meeting routine SLAs with review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously manages complex service operations, holding performance under ambiguous demand.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines service-delivery methods others adopt and resolves operational failures others can't.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets service-operations strategy and anticipates how service capability must evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-in-class service delivery for the discipline and is externally credible on it.

<a id="scm-15"></a>
##### SCM-15 — Field operations & dispatch coordination

*Type:* Behavioral — Coordinate dispatch, routing, and on-site service to meet commitments and customer needs.

- **[P1 — Assisted](proficiency_scale.md#p1):** Assigns routine jobs and updates dispatch status under guidance.
- **[P2 — Independent](proficiency_scale.md#p2):** Independently coordinates standard field schedules and routing with normal review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Autonomously optimizes dispatch under volatile demand, resolving conflicts and emergencies.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines field-coordination methods others adopt and solves dispatch problems others can't.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets field-operations strategy and anticipates how dispatch and routing must evolve.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines leading field-operations practice for the field and is sought externally for it.

### Corporate IT & Workplace Technology (CIT)

#### Service Management & Support

<a id="cit-01"></a>
##### CIT-01 — IT service management & service desk

*Type:* Technical — Operate request, incident, and problem management to restore and sustain employee IT services.

- **[P1 — Assisted](proficiency_scale.md#p1):** Logs and triages incoming tickets using set scripts, escalating anything beyond well-defined fixes.
- **[P2 — Independent](proficiency_scale.md#p2):** Resolves standard incidents and service requests independently within SLA, escalating only genuine edge cases.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns ambiguous and high-impact incidents end-to-end, sets local triage and escalation conventions.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the ticket taxonomy, SLA tiers, and queue-routing model that other support staff adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the service-management strategy and metrics framework across the organization's support function.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines what good service management looks like for the discipline and shapes external practice.

<a id="cit-02"></a>
##### CIT-02 — Change & release management

*Type:* Technical — Govern controlled introduction of changes to enterprise systems to minimize disruption.

- **[P1 — Assisted](proficiency_scale.md#p1):** Prepares change records and gathers approvals for low-risk, pre-templated changes under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Plans and executes standard changes independently, writing usable rollback steps and impact notes.
- **[P3 — Proficient](proficiency_scale.md#p3):** Owns risky, multi-team changes, judges risk and ambiguity, and is the go-to change coordinator.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the change-control and release process, risk-tiering, and CAB model others follow.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets release-governance strategy balancing change velocity and stability across the organization.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines industry-credible release-management practice and influences how the discipline operates.

<a id="cit-03"></a>
##### CIT-03 — End-user support & enablement

*Type:* Behavioral — Resolve user issues and build employee proficiency with workplace technology.

- **[P1 — Assisted](proficiency_scale.md#p1):** Handles common how-to questions and walk-throughs at the desk, escalating unfamiliar issues.
- **[P2 — Independent](proficiency_scale.md#p2):** Resolves most end-user problems independently and produces clear self-help guidance for users.
- **[P3 — Proficient](proficiency_scale.md#p3):** Tackles the hardest user-enablement cases and sets local standards for guidance and onboarding.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the enablement program, training curriculum, and support model others deliver against.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the organization's strategy for user adoption, digital literacy, and support experience.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice end-user enablement for the field and shapes how others teach it.

#### Endpoint & Workplace

<a id="cit-04"></a>
##### CIT-04 — Endpoint & device management

*Type:* Technical — Provision, configure, secure, and maintain employee devices across their lifecycle.

- **[P1 — Assisted](proficiency_scale.md#p1):** Enrolls, images, and configures devices following documented build steps under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages device fleets, policies, and patching independently for standard configurations.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves complex endpoint, compliance, and policy issues; sets local device-management standards.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the endpoint architecture, policy baseline, and lifecycle model others implement.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets endpoint strategy across platforms, anticipating shifts in management and security posture.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative endpoint-management practice and influences the discipline externally.

<a id="cit-05"></a>
##### CIT-05 — Collaboration & productivity platform management

*Type:* Technical — Administer messaging, document, and collaboration environments for employees.

- **[P1 — Assisted](proficiency_scale.md#p1):** Configures user accounts, groups, and shared spaces in the platform following set procedures.
- **[P2 — Independent](proficiency_scale.md#p2):** Administers collaboration services independently, handling routine config, permissions, and issues.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves complex platform, governance, and integration problems; sets local configuration standards.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the platform architecture, governance, and adoption model that administrators follow.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the organization's collaboration-platform strategy and roadmap across the workplace estate.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines leading collaboration-platform practice and shapes how the discipline is run elsewhere.

#### Enterprise Applications

<a id="cit-06"></a>
##### CIT-06 — Enterprise application administration

*Type:* Technical — Configure, maintain, and support shared business applications across corporate functions.

- **[P1 — Assisted](proficiency_scale.md#p1):** Performs routine application config and user-provisioning tasks under guidance and review.
- **[P2 — Independent](proficiency_scale.md#p2):** Administers an enterprise application independently, handling standard config and support tasks.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves complex configuration, upgrade, and data issues; is the go-to admin for the application.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the application's configuration baseline, upgrade approach, and governance others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the administration strategy and standards across the enterprise application portfolio.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative enterprise-application administration practice recognized beyond the organization.

<a id="cit-07"></a>
##### CIT-07 — Business systems integration & automation

*Type:* Technical — Connect enterprise systems and automate workflows to streamline business processes.

- **[P1 — Assisted](proficiency_scale.md#p1):** Builds simple, pre-specified integrations or automations from templates under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Develops standard integrations and automated workflows independently with normal testing and review.
- **[P3 — Proficient](proficiency_scale.md#p3):** Designs complex, multi-system integrations and resolves the hardest data and reliability problems.
- **[P4 — Expert](proficiency_scale.md#p4):** Defines the integration patterns, automation framework, and standards other builders adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets the organization's integration and automation strategy across business systems.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice systems integration and automation and influences the broader discipline.

#### Identity & Asset Governance

<a id="cit-08"></a>
##### CIT-08 — Identity & access administration (internal)

*Type:* Technical — Manage employee identities, accounts, and access rights across enterprise systems per policy.

- **[P1 — Assisted](proficiency_scale.md#p1):** Provisions accounts and applies access requests following defined approval workflows under review.
- **[P2 — Independent](proficiency_scale.md#p2):** Manages identities, groups, and access independently, handling standard joiner-mover-leaver flows.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves complex access, entitlement, and recertification issues; sets local identity standards.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the access model, role structure, and provisioning approach others implement.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets identity-and-access strategy, including governance and least-privilege posture, organization-wide.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative internal identity-administration practice and shapes the discipline externally.

<a id="cit-09"></a>
##### CIT-09 — IT asset & license management

*Type:* Technical — Track and optimize IT hardware, software, and license inventories across lifecycle and cost.

- **[P1 — Assisted](proficiency_scale.md#p1):** Records assets and license entitlements in the register following documented procedures.
- **[P2 — Independent](proficiency_scale.md#p2):** Maintains asset and license data independently, tracking lifecycle and reconciling routine discrepancies.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves complex license-compliance and asset-optimization issues; sets local asset standards.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the asset-lifecycle and license-management model and controls others adopt.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets asset-and-license strategy, optimizing cost and compliance across the organization.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines best-practice asset and license management and influences how the discipline operates.

#### Infrastructure & Operations

<a id="cit-10"></a>
##### CIT-10 — Enterprise infrastructure operations

*Type:* Technical — Operate and maintain corporate compute, storage, and network for reliable internal services.

- **[P1 — Assisted](proficiency_scale.md#p1):** Performs routine infrastructure monitoring and maintenance tasks following runbooks under supervision.
- **[P2 — Independent](proficiency_scale.md#p2):** Operates and maintains infrastructure services independently, handling standard incidents and changes.
- **[P3 — Proficient](proficiency_scale.md#p3):** Resolves complex outages and capacity issues; sets local operational standards and is the go-to operator.
- **[P4 — Expert](proficiency_scale.md#p4):** Designs the operational architecture, resilience approach, and runbook standards others follow.
- **[P5 — Authority](proficiency_scale.md#p5):** Sets infrastructure-operations strategy, anticipating capacity, resilience, and platform shifts.
- **[P6 — Pioneer](proficiency_scale.md#p6):** Defines authoritative infrastructure-operations practice and shapes the discipline beyond the organization.
