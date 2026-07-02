---
name: create-canonical-role
description: >-
  Mint a stable, canonical role record for the Open Capability Framework by running the
  career-ladder generation multiple times and consolidating the union — for when a role should
  become reusable canon that reproduces identically for every future user, not a one-off ladder.
  Use when the user says "make X canonical", "create a canonical role for X", "add X to the
  framework", or complains that repeated generations give different results. Warns about the
  token cost before running anything.
---

# Create a Canonical Role

A single career-ladder generation is a strong draft, but a single run captures only ~60% of a role's
full competency territory, and *which* 60% varies run to run (see `references/saturation-study.md`). This skill
buys consistency the honest way: N independent generations, a union consolidation that keeps every
distinct competency, a verification run that must reproduce the result exactly, and a gated PR
that makes the role canon for everyone. The output is (1) canonical capabilities in the framework,
(2) a role record future runs adapt verbatim, and (3) a genuine, full-prose career ladder.

## Step 0 — Check the framework first

Fetch `roles/<slug>/role.yaml` from github.com/jmresearch/open-capability-framework. If a record
already exists, STOP — tell the user, and offer either an ADAPT-mode ladder (cheap, reproducible)
or an *extension* pass (one generation diffed against the record, gate the additions). Never mint
a duplicate canon.

## Step 1 — The token-cost warning (mandatory, before any generation)

Tell the user plainly what this costs and get an explicit go-ahead:

> Minting a canonical role runs the full generation **N times** plus a consolidation pass and a
> verification run. At roughly 100k tokens per generation and ~250k for consolidation, the default
> N=5 costs on the order of **~1M tokens** — versus ~100k for a single non-canonical ladder. The
> extra runs exist only to capture coverage a single run misses (~40% of the territory); if you
> just need a ladder for your own org today, the single run is the right buy.

Scale N to the ask: **5 is the default** (the saturation study found diminishing returns beyond
this); use 4 as a floor when the user is cost-sensitive, 6–8 only when the user explicitly wants
exhaustive coverage for a broad or unusual role. Never run more than 8 — the study shows the tail
is empty. If the user declines, offer the single-run ladder instead.

## Step 2 — N independent generations

Run the `career-ladder` skill N times, in parallel, each run BLIND: no framework fetch (the role
has no record — simulate greenfield), no reading of sibling runs or prior ladders. Each run writes
`runs/<slug>-runK.md` + `.csv` and must pass `skills/career-ladder/scripts/validate_csv.py`
(with `--manager` for manager-variant roles) before it counts. A failed run is regenerated, not
patched.

## Step 3 — Union consolidation (nothing voted out)

Merge the N runs — plus any trusted existing artifact the user supplies (a hand-built ladder, an
old matrix; genericize org-specific content) — into one canonical ladder:

- Cluster source competencies **by meaning** (read cells, not labels); semantically equivalent
  rows merge into one canonical competency with the clearest name (≤60 chars), the strongest
  citable anchor, and cells that take the best observable content from the sources.
- **Every genuinely distinct competency survives, even single-source.** The distinct tail is the
  value the extra runs paid for.
- Re-cut the three-tier grouping cleanly afterward (every focus area spans 2+ competencies,
  unique triples).
- Map every canonical competency to a framework capability id; draft a `contrib/` proposal (with
  P1–P6 profile) for each one the catalog lacks.
- Build `roles/<slug>/role.yaml` (levels, competency references, per-level proficiency targets)
  plus canonical `ladder.md`/`ladder.csv`, per `roles/README.md`.
- Write a consolidation report: the merge map, and the agreement histogram (how many competencies
  appeared in all runs / most / one) — this is the evidence the canon is holistic.

## Step 4 — Verification (must be exact)

Run one fresh ADAPT-mode generation against the draft role record. It must reproduce the structure
**exactly** — every (key_area, key_attribute, theme) triple, in order. Anything less means the
record is ambiguous; fix it and re-verify. Prose wording may differ; structure may not.

## Step 5 — The contribution gate

Per `skills/career-ladder/references/capability-framework.md`: show the user exactly what would be
contributed (role record, canonical ladder, capability proposals — all scrubbed of org-specific
content), state that it becomes a public PR under CC BY 4.0, and **ask permission**. Only an
explicit yes in this conversation authorizes the PR. Declining delivers everything locally and
ends the matter.

## Deliverables

- `roles/<slug>/` — role record + canonical ladder (the reusable canon)
- `contrib/` proposals for new capabilities
- The full-prose career ladder for immediate use
- The consolidation report with agreement stats

## Reference

- `references/saturation-study.md` — the Engineering Manager 8-run study behind the N=5 default
  and the cost numbers.
