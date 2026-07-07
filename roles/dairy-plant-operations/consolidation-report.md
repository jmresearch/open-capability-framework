# Consolidation report — Dairy Plant Operations (canonical mint)

**Minted:** 2026-07-07
**Method:** union consolidation of five independent, blind, same-methodology generations
(`create-canonical-role`, N=5). All breadth runs, consolidation, and the ADAPT verification run on
`claude-opus-4-8` @ xhigh. No prior record existed — every run greenfield (no framework fetch, no
sibling reads). This is a `general`-variant role with an atypical **unified IC→manager** ladder:
operator craft and operational leadership advance in one 7-level column (L1 Operator I → L4 Lead
Operator, IC-terminal → L7 Plant Operations Manager).

## Inputs

| Run | Competencies | Key areas | Validator |
|-----|--------------|-----------|-----------|
| 1 | 33 | 6 | OK (0 warn) |
| 2 | 32 | 6 | OK (0 warn) |
| 3 | 32 | 6 | OK (0 warn) |
| 4 | 32 | 6 | OK (0 warn) |
| 5 | 34 | 6 | OK (0 warn) |
| **Total source rows** | **163** | — | all pass (general variant) |

Every run independently converged on the same six key areas — Food Safety & Regulatory Compliance,
Process Operations, Sanitation & Hygiene, Equipment/Utilities/Reliability, Safety & Process Safety
Management, and Leadership/People/Continuous Improvement — strong evidence the territory is stable.

## Output

**38 canonical competencies**, 6 key areas, 17 focus areas (every focus area spans 2+ competencies;
all triples unique). Clustered by meaning, re-cut into a clean three-tier grouping.

## Agreement histogram (clustered concepts by run presence)

| Appears in | Concepts (approx.) | Examples |
|------------|--------------------|----------|
| 5/5 runs | ~26 | pasteurization/flow-diversion, HACCP CCP, preventive controls, environmental/Listeria, allergen control, raw-milk receiving, separation, homogenization, filling, cold chain, CIP, cleaning chemistry, ammonia refrigeration, boiler/steam, autonomous maintenance, troubleshooting, wastewater, LOTO, PSM/RMP, emergency response, operator training, huddles/handover, OEE, cost/budget |
| 4/5 | ~6 | pasteurizer operation, COP/manual sanitation, utilities stewardship, hazard/PPE/permits, coaching, shift leadership |
| 3/5 | ~4 | PMO/Grade A recordkeeping, production scheduling, root-cause, thermal legal records |
| 2/5 | ~5 | GFSI audit readiness, GMP/hygiene, hygienic design/3-A, culturing/batch, safety-culture leadership |
| 1/5 (folded) | ~6 | in-process lab testing, documentation integrity, standalone environmental compliance, escalation, cross-functional comms |

The convergent core (≥4/5) is ~32 concepts — captured in full. Low-agreement items were either kept
(distinct tail) or folded into their nearest canonical competency (e.g. standalone environmental
compliance → wastewater; documentation → PMO recordkeeping; in-process testing → HACCP monitoring).

## Capability mapping

**13 competencies** map to existing OCF capabilities (generic operations/maintenance/EHS/leadership/
finance): SCM-07 (OEE), SCM-08 (scheduling), SCM-09 (maintenance), WPL-02 (utilities), WPL-08
(LOTO; hazard/PPE), LI-01 (training), LI-08 (shift leadership), EM-01 (coaching), EM-06 (cost),
CC-01 (huddles), CC-03 (escalation), SUP-05 (root-cause).

**25 competencies** — the dairy/food-plant craft (pasteurization, HACCP, PMO, CIP, allergen/pathogen
control, ammonia refrigeration, PSM/RMP, thermal processing, etc.) — had **no catalog match**; the
catalog's Operations & Supply Chain (SCM) and Workplace/EHS (WPL) capabilities are generic and carry
no food-safety/dairy-process frame. These reference a new **Food & Beverage Manufacturing (FBM)**
capability set proposed under `contrib/` (FBM-01..FBM-25), each with a P1–P6 profile calibrated to
the operator→plant-manager progression.

## Proficiency

Operational curve over 7 levels. Craft competencies climb L1:P1 → L7:P6 with an **L4–L5 depth
plateau** (both P4) — depth holds at the IC-terminal master-operator bar while scope widens from a
line (L4) to a shift crew (L5); leadership competencies start as informal proxies (L1:P1) and rise to
P6 at plant-lead scope.

## Verification

ADAPT-mode regeneration against `role.yaml` reproduced all 38 (key_area, key_attribute, theme,
capability) triples exactly, in order (general variant, `validate_csv.py` clean), both on the initial
render and after the post-review edits below.

## Post-review adjustments (Fable @ high consistency review, 2026-07-07)

Reviewed read-only against the catalog, sibling role records, and the mint/contrib protocols.
Verdict was BLOCK on six findings; all resolved before the gate:

| # | Sev | Finding | Resolution |
|---|-----|---------|------------|
| 1 | blocker | FIN-02 (FP&A) wrong for "Cost, labor & budget ownership" | Remapped to **EM-06** (Budget & vendor management) |
| 2 | blocker | WPL-08 used a 3rd time for "Shift & safety leadership" → dual proficiency curve on one id | Remapped to **LI-08** (Situational & Adaptive Leadership), theme → "Shift leadership & crew coordination"; WPL-08 now 2 rows, one curve |
| 3 | blocker | SUP-04 (customer-support escalation) wrong for shop-floor escalation | Remapped to **CC-03** (Teamwork & Partnership); support-desk cell prose rewritten to floor register |
| 4 | blocker | FBM-22 mischaracterized SCM-09 as "software-flavored" | Justification rewritten honestly; P-bars narrowed to the food-safety-clock / hygienic-restart / product-disposition delta |
| 5 | blocker | Bar bleed across the thermal/records cluster (FBM-01/02/07/12) | P-profiles de-overlapped into kill-step control / legal minima & proof / ordinance-permit records / running the system |
| 6 | blocker | No consolidation report (mint-protocol deliverable) | This report |
| 7 | major | Nearest-id justifications used a strawman set | FBM-03/04/08/14/15/22 justifications name the true nearest ids (SCM-10, RISK-04/05/06, SCM-06/11) and why the food-safety frame still requires the proposal |
| 8-12 | minor | Homogenization theme divergence; FBM-16/17 P4 concentration overlap; WPL-02 rationale | Theme aligned to "Homogenization & product finishing"; FBM-16 P4 references the chemistry standard; WPL-02 rationale softened |

## Note on general-variant shape

Calibration guidance suggests general-variant ladders are "typically four or five" levels / ~25
competencies. This role is deliberately 7 levels / 38 competencies / 17 focus areas because the
brief's atypical unified IC→manager pathway needs the extra rungs (four IC craft levels + three
leadership levels) and the dairy domain is competency-dense (food safety + process + sanitation +
plant engineering + process safety + leadership). The deviation is intentional, not drift.
