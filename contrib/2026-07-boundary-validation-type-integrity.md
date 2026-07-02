# Boundary validation & end-to-end type integrity

- **Proposed id:** SWE-09
- **Domain / focus area:** Software Engineering / Design & Architecture
- **Type:** Technical
- **Description:** Validates untrusted data into precise types once at every system boundary (network, storage, configuration, third parties) and propagates a single source of type truth across client, server, and wire so contracts cannot silently drift.
- **Why it's missing:** Four of five runs of the full-stack-typescript canonical consolidation carried this as a distinct competency (anchor: "Parse, Don't Validate"). BE-13 (API contract & versioning design) covers the contract itself, not the runtime-validation and schema-derived-type discipline that keeps code honest against it; CS-09 (Data encoding & serialization) covers formats, not validation-at-the-edge practice; proposed SWE-08 covers internal domain typing, not the seams where static guarantees end. The competence is stack-agnostic: any typed system consuming external data faces it.

## P1–P6 behavioral profile

- **P1 (Assisted):** Uses the codebase's shared contract types and schema validators at boundaries rather than hand-casting external data, and can point to where a type is checked at runtime.
- **P2 (Independent):** Puts runtime validation at every I/O boundary they touch — requests, messages, configuration — deriving static types from the runtime schemas so compile-time and runtime cannot drift.
- **P3 (Proficient):** Designs end-to-end type integrity for a capability — schema-first contracts, generated clients, contract drift caught in continuous integration — and blocks unsound casts and unvalidated edges in review.
- **P4 (Expert):** Builds the code-generation and contract-typing infrastructure multiple teams inherit, making boundary safety the default rather than a discipline, and resolves cross-team type drift at its source.
- **P5 (Authority):** Sets the organization's boundary-safety standard and the platform tooling that enforces it, with incident evidence showing the failure classes it removed.
- **P6 (Pioneer):** Owns contract-integrity strategy across products and external interfaces where a broken contract is a business event, and advances the state of practice publicly.
