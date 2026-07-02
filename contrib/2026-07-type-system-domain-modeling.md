# Type-system domain modeling

- **Proposed id:** SWE-08
- **Domain / focus area:** Software Engineering / Design & Architecture
- **Type:** Technical
- **Description:** Uses a static type system as a design medium — encoding domain rules and invariants in types so invalid states are unrepresentable and whole defect classes are eliminated at compile time.
- **Why it's missing:** All five runs of the full-stack-typescript canonical consolidation independently gave this first-class treatment (anchors: Effective TypeScript; Domain Modeling Made Functional). SWE-01 (Writing Code) covers language fluency but not design-by-types; ARC-03 (Domain modeling) covers modeling business concepts and boundaries, not encoding them in a compiler-checked type system; SWE-05 (Software Design & Architecture) covers module structure, not type-level invariants. The competence applies to any statically typed stack (TypeScript, Rust, Haskell, Kotlin, Swift).

## P1–P6 behavioral profile

- **P1 (Assisted):** Writes correctly typed code without escape hatches (`any`-equivalents), uses the codebase's existing types and generics correctly, and reads compiler errors to the actual cause with guidance.
- **P2 (Independent):** Models feature domains so invalid states fail to compile — sum types / discriminated unions over boolean flags, narrowing over assertions — preferring type-level constraints where the compiler can carry the load.
- **P3 (Proficient):** Designs the shared domain types a capability is built on, keeping inference ergonomic for consumers; judges when type-level sophistication pays and when it obscures, and unwinds accumulated type erosion in others' code.
- **P4 (Expert):** Sets type-design conventions multiple teams adopt — strictness policy, shared type libraries, branded identifiers, result types — and leads migrations that raise strictness without halting delivery.
- **P5 (Authority):** Owns an organization's type-system posture — compiler baselines, monorepo type architecture, upgrade cadence — measured by defect and velocity outcomes.
- **P6 (Pioneer):** Makes company-level language and type-platform bets and represents the practice externally (talks, upstream contributions, published patterns).
