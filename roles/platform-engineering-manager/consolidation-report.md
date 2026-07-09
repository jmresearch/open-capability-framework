# Consolidation report — Platform Engineering Management (canonical mint)

**Minted:** 2026-07-07
**Method:** union consolidation of five independent, blind, same-methodology generations
(`create-canonical-role`, N=5). Model/effort for all breadth runs: `claude-opus-4-8` @ high
(canon-capable per `benchmarks/model-efficiency.yaml`); consolidation and the ADAPT verification
run on `claude-opus-4-8` (session frontier). No prior PEM record existed — every run was greenfield
(no framework fetch, no reading of sibling roles/ladders).

## Inputs

| Run | Competencies | Key areas | Validator |
|-----|--------------|-----------|-----------|
| 1 | 30 | 6 | OK (0 warn) |
| 2 | 30 | 6 | OK (0 warn) |
| 3 | 28 | 6 | OK (0 warn) |
| 4 | 29 | 6 | OK (0 warn) |
| 5 | 29 | 6 | OK (0 warn) |
| **Total source rows** | **146** | — | all pass `--manager` |

Every run independently converged on the same six-ish key areas — People Leadership,
Platform-as-a-Product, Reliability/Operations, Technical Direction/Architecture, Delivery/Execution,
and Strategy/Communication/Influence — which is itself strong evidence the territory is stable.

## Output

**44 canonical competencies**, 7 key areas, 16 focus areas (every focus area spans 2+ competencies;
all `(key_area, key_attribute, theme)` triples unique). Clustered **by meaning** (cell content, not
labels), then re-cut into a clean three-tier grouping. The ensemble union produced **38**; a Fable
consistency review (2026-07-07) added the 6-competency **Self & Personal Effectiveness** key area
(see "Post-review adjustments").

## Agreement histogram (clustered concepts by run presence)

| Appears in | Concepts (approx.) | Examples |
|------------|--------------------|----------|
| 5/5 runs | ~26 | hiring, coaching, performance, psych safety, platform vision & roadmap, internal user research, golden paths, self-service, adoption & migration, SLOs/reliability, incident leadership, toil reduction, capacity & cost, platform architecture, engineering standards, technical strategy, build/buy/adopt, security posture, planning, predictable delivery, dependency & risk, leading change, org design, exec communication, cross-org influence, career development |
| 4/5 | 5 | motivation & retention, platform advocacy, prioritization & trade-offs, strategy formulation, stakeholder management |
| 3/5 | 3 | platform value & business case, process & continuous improvement, capacity & resource allocation |
| 2/5 | 4 | onboarding, observability, technical debt, engineering metrics |

The core (≥4/5) is ~31 concepts — captured in full. The 2–3/5 tail is the distinct coverage the
extra runs paid for; all of it survived into canon.

## Merge map — single-source / low-agreement items folded (maintainer judgment)

Genuine but weakly-generated singletons were folded into their nearest canonical competency rather
than shipped standalone (per the skill's guidance that singletons are a consolidation-time judgment
call, not a sampling result):

| Source concept (runs) | Disposition |
|------------------------|-------------|
| Inclusion & belonging (2/5) | folded into **Psychological safety & team health** (EM-03) |
| Cognitive load / DevEx journey design (2/5) | folded into **Internal user research & discovery** (PM-01) |
| Operating model & governance (2/5) | folded into **Organizational & team design** (EM-04) |
| Written/verbal comms & storytelling (1/5) | folded into **Executive & stakeholder communication** (CC-06) |
| Succession & leadership pipeline (1/5) | folded into **Career development & sponsorship** (EM-02) |
| Thinnest-viable-platform scoping standalone (1/5) | folded into **Platform vision & roadmap** (PM-05) |

Each fold is recoverable as a split in a later re-mint if evidence accrues.

## Capability mapping

43 of 44 competencies map to existing OCF catalog ids (verified against `data/capabilities.csv`).
One — **Adoption & migration strategy** — had no catalog match (PM-10 is *metrics*, OPS-30 is
*release safety*, DR-03 / CSM-01-02 are *external*-customer adoption), so a new capability,
**OPS-33 Platform adoption & deprecation management**, was proposed and then **accepted into the
catalog** with this record (folded into `data/capabilities.csv`/`.json`, `data/domains.csv`, and
the rendered catalog; the `contrib/` proposal file was removed on acceptance). The role row maps to
`OPS-33`. The mint reuses the anchors of the Engineering Management and Platform Engineering
canonical records for shared capabilities, so a PEM competency and its EM or platform-IC cousin
cite the same source. `OPS-27` (Platform & developer-experience engineering) is referenced twice
under different focus lenses — golden paths vs. self-service — matching the Platform Engineering IC
record's precedent.

## Post-review adjustments (Fable @ high consistency review, 2026-07-07)

The minted record was reviewed read-only against the EM and platform-IC siblings, the catalog, and
the mint protocol. Verdict was BLOCK on one finding; all findings resolved before the gate:

| # | Sev | Finding | Resolution |
|---|-----|---------|------------|
| 1 | blocker | "Adoption & migration strategy" → PM-10 (metrics) is a semantic mismatch; catalog lacks the capability | Proposed **OPS-33** and **accepted it into the catalog**; row maps to `OPS-33` |
| 2 | major | "Incident & reliability leadership" → OPS-06 diverged from the EM sibling's EM-10 for the same behavior | Remapped to **EM-10** (Incident & operational risk management); theme → "Incident & operational-risk leadership" |
| 3 | major | Shipping without the **Self & Personal Effectiveness** area the EM sibling carries (not platform-contingent) | Added the 6 EM rows verbatim (EM-16, EM-14, LI-09, LI-10, LI-04, LI-11) — curves + anchors reused |
| 4 | minor | SEC-18 theme broader than the capability (compliance clauses) | Theme → "Secure-by-default platform & guardrails" |
| 5 | minor | EM-06 theme overstated the capability | Theme → "Vendor & build/buy/adopt strategy" (vendor primary; budget stewardship folded here) |
| 6 | minor | PM-05 covers roadmap; the vision half maps partly to STRAT-02 (which PEM omits) | Accepted asymmetry — STRAT-01 carries direction-setting; noted here |
| 7 | (adj.) | EM-13 / EM-02 at M1:P2 vs sibling P3 rows | **Kept** — mirrors the EM record exactly; cross-ladder consistency for a shared id is the stronger invariant |
| 8 | nit | British spelling ("favouring"); untracked `runs/` | Fixed to US English on re-render; `runs/` kept local (evidence), excluded from the PR |

Every capability id shared with the EM record was confirmed to carry an identical M1-M6 curve.

## Coverage gap — resolved

The blind PEM ensemble **under-covered the Self & Personal Effectiveness territory** that the
Engineering Management sibling carries as a full key area — managerial leverage & delegation
(EM-16/EM-14), decision-making under uncertainty (LI-04), self-awareness & learning agility (LI-09),
resilience & sustainable pace (LI-10), ethics & integrity (LI-11). The five runs consistently
weighted platform-product, people, reliability, delivery, and strategy over personal effectiveness;
none surfaced a self-effectiveness area.

This is a real ensemble signal, not an omission introduced at consolidation — but the missed
territory (delegation, decision-making under uncertainty, ethics, resilience) is **not
platform-contingent**, and a canon meant to be adapted verbatim should not lack an ethics or
delegation row on the manager axis.

**Resolved (option 1):** the Fable review adjudicated that shipping without it was the weaker
choice. The EM sibling's Self & Personal Effectiveness area — 6 competencies across 3 focus areas
(Leverage & Delegation: EM-16, EM-14; Growth & Resilience: LI-09, LI-10; Judgment & Integrity:
LI-04, LI-11) — was borrowed verbatim (curves and anchors already calibrated on the manager axis),
taking the record from 38 to 44. The `scope_note` records the provenance so future re-mints know
these six rows came from cross-ladder parity, not the PEM ensemble.

## Verification

ADAPT-mode regeneration against the draft `role.yaml` — see the mint session log. Structure must
reproduce exactly (all 38 triples, in order); prose wording is free to differ. Result recorded with
the shipped `ladder.md` / `ladder.csv`.
