# Saturation study — how many runs does a canonical role need?

Empirical basis for this skill's run-count default and token-cost warning. Conducted 2026-07-02
on the Engineering Manager / engineering-leadership role.

## Design

Eight fully independent generations of the same role by the `career-ladder` skill (manager
variant, M1–M6), each blind: no framework fetch, no access to sibling runs or any prior ladder.
Every run passed `validate_csv.py --manager` before counting. The 222 resulting competency rows
(27–28 per run) were then clustered **by meaning** (labels differ wildly across runs — "Coaching
& feedback" / "Coaching & Growth" / "Coaching & Development" are one concept) into **46 distinct
concepts**, each tagged with which runs produced it.

## Presence distribution

| Appears in | Concepts | Examples |
|---|---|---|
| 8/8 runs | 11 | strategy, leading change, prioritization, delivery flow, incidents, hiring, coaching, performance mgmt, psych safety, motivation, engineering quality |
| 7/8 | 4 | org design, conflict resolution, developing leaders, executive communication |
| 6/8 | 4 | goal setting, planning, technical strategy, budget stewardship |
| 5/8 | 5 | career development, product partnership, written communication, stakeholder mgmt, decision mechanisms |
| 4/8 | 2 | technical decision oversight, customer/business focus |
| 3/8 | 12 | (the long tail of real but unreliably-generated coverage) |
| 2/8 | 5 | |
| 1/8 | 3 | security & risk, developer experience, driving alignment |

Only 11 of 46 concepts (24%) are guaranteed by any single run. 43 of 46 appeared in ≥2 runs — the
"stable canon."

## Discovery curve (exact rarefaction over all run orderings)

| Runs | Expected concepts found | % of all 46 | % of stable canon (43) | Marginal gain |
|---|---|---|---|---|
| 1 | 27.8 | 60% | 64% | +27.8 |
| 2 | 35.7 | 78% | 81% | +7.9 |
| 3 | 40.0 | 87% | 90% | +4.3 |
| 4 | 42.5 | 93% | 95% | +2.6 |
| 5 | 44.1 | 96% | 98% | +1.6 |
| 6 | 45.1 | 98% | 100%* | +0.9 |
| 7 | 45.6 | 99% | 100% | +0.6 |
| 8 | 46.0 | 100% | 100% | +0.4 |

*rounded; 99.6%.

The curve is the classic collector's shape: the second run is worth ~8 new concepts, the fifth is
worth ~1.6, and everything past the sixth buys mostly single-run singletons whose canon-worthiness
is debatable anyway (a maintainer judgment call at consolidation time, not a sampling problem).

## Cost (observed, this study)

| Stage | Tokens (observed) |
|---|---|
| One generation run | ~80–120k (median ≈ 85k) |
| Consolidation (clustering + union merge + role record) | ~250–350k |
| Verification run (ADAPT mode) | ~100k |
| **Canonical mint at N=5** | **≈ 0.8–1.1M** |
| Single non-canonical ladder, for comparison | ≈ 0.1M |

## Recommendation (encoded in SKILL.md)

- **Default N=5** — 96% of total territory, 98% of the stable canon; the last "reliable" tier
  (concepts in ≥4 runs) is fully captured well before this.
- **N=4 floor** for cost-sensitive minting (95% of stable canon).
- **N=6–8 only on explicit request** for exhaustiveness; never more than 8 — the tail is empty.
- A **single run is the wrong tool for canon**: it misses ~40% of the territory, and *which* 40%
  varies run to run — that is precisely the inconsistency canonical roles exist to kill.

## Caveats

- One role, one variant, one model generation. Engineering management is an unusually
  well-theorized domain (dense anchor literature); thinly-documented roles may saturate slower —
  if consolidation finds an unusually high singleton rate (>15% of concepts), recommend one or
  two supplementary runs before finalizing.
- Cell-prose wording always varies run to run; this study measures competency *territory*, which
  is what the role record pins. Prose variance is eliminated separately, by ADAPT mode.
- Verification in this study reproduced the consolidated structure 43/43 triples exactly on the
  first attempt.
