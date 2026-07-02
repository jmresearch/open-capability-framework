# Benchmarks — what "good" looks like, per model and effort

Canonical-role minting runs the ladder generation N times, and both N and the quality of each run
depend on the model/effort configuration doing the generating. This directory holds the empirical
entries that let tooling recommend the right N — or the right model — instead of guessing.
`model-efficiency.yaml` is fetched live by the `create-canonical-role` skill at run time.

## The quality bar ("good results" means all of these)

A configuration is **canon-capable** when its blind runs typically show:

1. **Validator-clean** — `validate_csv.py --manager` passes (structure, triples, theme caps, no
   position-locked language, no 1:1 focus mappings), with at most minor fix iterations.
2. **Register discipline** — every cell carries labeled Depth:/Scope: clauses in present-tense
   observable behavior; bold lead clauses present; no competency-library paraphrase.
3. **Real anchors** — every competency's theory anchor is a real, citable work (spot-check ≥5).
4. **Territory coverage ≥ 55% of the role's reference canon per run** — comparable to the
   frontier baseline (60%); a config that samples much thinner needs disproportionately many runs
   and usually fails 1–3 anyway.
5. **Core recall** — the reference canon's high-frequency core (concepts present in ≥6/8 baseline
   runs) should be mostly hit by any 2 runs combined (≥ 85%).

Configs that miss the bar aren't banned — they're marked `canon_capable: false` with the observed
failure mode, and the skill steers users to a capable model for minting (a cheap model may still
be fine for a personal, non-canonical ladder).

## Entry schema (`model-efficiency.yaml`)

```yaml
reference_canons:
  engineering-management:
    concepts: 46          # semantic concepts in the reference set
    stable: 43            # concepts seen in >=2 baseline runs
    core: 19              # concepts seen in >=6/8 baseline runs
configs:
  - model: <model id or family, e.g. claude-fable-5>
    effort: <low|medium|high|xhigh|max|session-default|unknown>
    runs_observed: <int>          # how many blind runs back this entry
    role_tested: engineering-management
    validator_pass_rate: <0-1>
    mean_competencies_per_run: <float>
    mean_canon_coverage_per_run: <0-1>   # fraction of reference concepts hit by one run
    core_recall_2runs: <0-1>             # fraction of core hit by any 2 runs (mean over pairs)
    register_notes: <short free text>
    tokens_per_run_median: <int>
    canon_capable: <true|false>
    recommended_runs: <int|null>  # N for ~95% expected stable-canon coverage, null if not capable
    source: <study file or PR link>
```

`recommended_runs` uses the observed per-concept sampling rate: with mean per-run canon coverage
p, expected coverage after N runs ≈ 1 − (1 − p)^N aggregated per concept tier; entries round up.
Small-sample entries (2–3 runs) are estimates — say so in `register_notes`.

## Contributing an entry (untested model/effort)

When someone mints a canonical role on a configuration with no entry here, the
`create-canonical-role` skill asks whether they're willing to contribute their run telemetry —
per-run competency counts, canon-coverage scoring against the role's reference set, validator
results, token usage — as a new benchmark entry, PR'd together with their canonical-role
contribution. **Only with their explicit permission**, like every other contribution. The entry
must contain no org-specific content (it's numbers and register notes). More entries → better
recommendations for the next user; that's the same network effect as the catalog itself.
