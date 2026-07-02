# Model-efficiency study — which configurations are canon-capable, and at what cost

Role tested: **Engineering Manager / engineering leadership** (manager variant, M1–M6).
Conducted 2026-07-02. Companion to `saturation-study.md`, which established the 46-concept
reference canon (43 stable, 19 core) and the N=5 default on the frontier baseline.

## Design

Eleven blind generations across four conditions — fable/low ×3, opus-4-8/high ×3, sonnet-5/high
×3, haiku-4-5/high ×2 — under the identical protocol as the 8-run fable/xhigh baseline (no
framework fetch, no sibling reads, validator required). Conditions ran sequentially so token
costs are cleanly attributable. Every run's competencies were then mapped semantically onto the
46-concept reference canon, giving per-concept hit/miss against the baseline — the gap analysis,
not just aggregate percentages.

## Results

| Config (model/effort) | Coverage/run | Stable-canon/run | 2-run core recall | Systematic gaps | Tokens/run | Concepts per 100k | Canon-capable |
|---|---|---|---|---|---|---|---|
| fable / xhigh (baseline) | 60% | 62% | 99% | 0 | ~85k | 33 | yes — N=5 |
| **fable / low** | 55% | 57% | 91% | 1* | 39.5k | 64 | **yes — N=5** |
| **opus-4-8 / high** | 51% | 54% | 88% | 2* | 29.5k | **80** | **yes — N=5** |
| sonnet-5 / high | 54% | 57% | 90% | 1* | 48.9k | 51 | yes — N=5 |
| haiku-4-5 / high | 41% | 43% | 68% | **6** | 58.3k | 33 | **no** |

\* At 3 observed runs, 1–2 apparent gaps are within chance for a ~55%-coverage config (a concept
hit at p≈0.55 is missed by all three runs ~9% of the time; with 19 core concepts, ~1–2 such
misses are expected by luck). Haiku's six gaps on two runs, concentrated in load-bearing
territory — budget, conflict, executive communication, performance management, prioritization,
succession — are far past noise.

Register findings the table doesn't show:

- **fable/low was the cleanest cheap config**: three first-try validator passes, full Depth/Scope
  discipline in every cell, real anchors.
- **opus/high and sonnet/high leaked position-locked language** ("reporting line") in 3 of 6 runs
  combined, plus one opus run with three 1:1 focus mappings — all caught and fixed by the
  validator loop. The validator is the load-bearing safety net for cheap-config generation.
- **haiku/high failed the register itself**: one of its two runs produced zero Depth:/Scope:
  labeled cells (0/138) while still passing the CSV validator — passing structure checks is not
  the same as writing an assessable ladder. It also produced 9 foci in one run (below the
  three-tier norm) and cost more per run than opus/high.

## Recommendation (encoded in SKILL.md and benchmarks/model-efficiency.yaml)

1. **Hybrid minting is the cost-efficient default.** Run the N breadth generations on a cheap
   canon-capable config — **fable/low** (best fidelity per token, cleanest register) or
   **opus-4-8/high** (cheapest overall) — and keep **consolidation and verification on the
   frontier config**, since the union merge is where quality is gated and singletons are judged.
   Estimated mint cost: 5 × ~35k + ~300k + ~100k ≈ **0.6M tokens**, vs ~1M all-frontier — a
   ~40% saving with the same union coverage after N runs.
2. **N stays 5 for all capable configs.** Their thinner per-run sampling (51–57% vs 60%) still
   reaches ≥95% expected stable-canon coverage at N=5 with the heterogeneity margin; the union
   after five cheap runs is statistically comparable to five frontier runs.
3. **Never mint on a config that fails the bar.** Haiku-class output has territory holes no run
   count fixes economically and can silently drop the assessment register. Drafts only.
4. **Gap lists are role-specific.** These gaps were measured on engineering management; a config
   may miss different territory on a different role. First mints on a new role with a cheap
   config should sanity-check the consolidation report's agreement histogram — an unusually fat
   singleton tail means the breadth runs under-sampled and one more run is warranted.

## Method notes

- Coverage scored by semantic concept-mapping (same method as the saturation study), verified so
  every row lands in exactly one concept.
- `recommended_runs` = smallest N with homogeneous expected coverage ≥95% of the stable canon,
  plus one run as a heterogeneity margin (this reproduces the baseline's empirical N=5).
- Token figures are workflow-measured subagent totals per condition divided by runs; the baseline
  figure (~85k) was measured under a slightly different harness and is comparable, not identical.
- Small samples throughout (2–3 runs per condition): entries are marked as estimates in the
  benchmark file, and the telemetry-contribution flow exists precisely to fatten these samples.
