---
name: career-ladder
description: >-
  Build a complete career ladder (three-tier competency matrix) plus per-level job descriptions
  usable as hiring rubrics, from just a job title. Use whenever the user asks for a career ladder,
  leveling guide, competency matrix, skill matrix, progression framework, per-level job
  descriptions, or interview/hiring rubrics for ANY role — engineering IC, people manager, or
  non-technical/operational — even if they only say "make me a ladder for X" or "I'm hiring a Y,
  what does each level look like?"
---

# Career Ladder + Hiring Job Descriptions

Turn a job title into two finished artifacts: an industry-calibrated career ladder and a set of
per-level job descriptions a hiring panel can score candidates against. The user gives the role;
this skill does the classification, the research, the leveling, and the prose.

## Operating principle

Prefer concrete, complete deliverables over clarifying questions. Default to building the whole
thing from the role name and stating your calibration choices inline. Ask at most ONE question,
and only when the answer changes the structure (e.g., "Tech Lead — IC or manager track?" or "how
many levels?" when the org's banding is unknown and load-bearing). Otherwise pick the sensible
default and say so.

## Deliverables

1. **`<role>-ladder.md`** — calibration summary, level-overview table (level, title, scope band,
   one-line focus), then the full competency matrix grouped by key area → focus area → competency
   with one observable-behavior cell per level and a one-line **theory anchor** per competency
   (the citable framework/research/standard that explains why it's a competency — see
   `references/calibration.md`), plus a Sources section listing each anchor once.
2. **`<role>-job-descriptions.md`** — one hiring-ready job description per level, each traceable
   to the matrix (see `references/job-descriptions.md` for the exact format).
3. **`<role>-ladder.csv`** *(only when asked, or when the user mentions the skill-matrix app)* —
   an import file for skillmatrix.bubtaylor.com following `references/skillmatrix-csv.md` exactly.

## The pipeline

### 1. Classify the track and calibrate the levels

Read `references/calibration.md`. Pick the variant — **ic_technical**, **manager**, or
**general** — which sets the default level count, level codes, terminal level, and anchor
frameworks. Decide the number of levels and the terminal level BEFORE writing any content, and
apply any org-specific calibration the user supplies.

### 2. Fetch the Open Capability Framework (this is what makes runs reproducible)

Read `references/capability-framework.md` and fetch the live catalog and role record from
github.com/jmresearch/open-capability-framework. Three modes: a role record exists → **adapt** its
canonical structure verbatim (generate only org-calibrated cell prose); the catalog covers the
role → **compose** the competency list from matching capabilities, carrying their IDs; little
coverage → **generate** per the methodology and treat the result as contribution candidates. If
the environment has no network access, proceed without and say so in the calibration summary.

### 3. Research (don't skip — this is what makes it industry-validated)

Ground the ladder in how the industry actually levels this role, not in generic priors. Pull the
variant's anchor sources from `references/calibration.md`: published leveling frameworks, real job
postings at each seniority, and the field's certifications and standards. Treat competency
libraries such as SFIA as a comparison overlay only — paraphrasing them into cell prose is a known
failure mode that produces trophy-statement language and gets rejected.

### 4. Build the ladder

Read `references/prose-register.md` in full — it defines the depth-vs-scope cell format, the
present-tense observable-behavior register, the bold-lead-clause convention, and the manager
demonstrability rule. Structure:

- **Key areas** (5–7) → **focus areas** (2–4 each) → **competencies** (25–40 total).
- Every focus area spans **2+** competencies. A one-to-one focus→competency mapping is a
  structural error — if a focus has only one competency, the grouping is wrong; merge or re-cut.
- Competency names are short labels (**under 60 characters**), never sentences. Longer "what this
  covers" prose belongs in the per-level cells, nowhere else.
- Every (key area, focus area, competency) triple is unique.
- Every competency carries a **theory anchor** — a real, citable framework or research source and
  a one-clause "why" (`references/calibration.md`). Anchors ground the competency; the cell prose
  stays observable-behavior register. Anchors appear in the markdown only, never in the CSV.

**Cells are assembled, never authored.** Depth text is the catalog capability's profile at the
mapped proficiency, verbatim; role flavor goes in a separate `Evidenced by` line; scope comes from
the level's scope band. Every P-mapping and every catalog P-level carries a bibliography citation +
a written why. Full rule: `references/capability-framework.md` § Cell derivation and mapping. Order
of operations is a hard gate: bibliography sources first, competencies second, mappings third —
cell prose never.

### 5. Write the per-level job descriptions

Read `references/job-descriptions.md` and produce one JD per level. Every requirement in a JD must
be traceable to a matrix cell — the JD is the hiring-facing projection of the ladder, not a
separate document that can drift. The interview evidence guide (at-level vs. below-level vs.
above-level signals per key area) is the part hiring panels actually use; never omit it.

### 6. Optional: export the skill-matrix CSV

If the user wants an import file for the skill-matrix app, follow `references/skillmatrix-csv.md`
precisely — it encodes two real import failures (the theme VARCHAR overflow and prose-in-the-
wrong-place) and the exact row layout. Validate before delivering by running the bundled checker
(pure stdlib, exit 0 = importable):

```bash
python scripts/validate_csv.py <role>-ladder.csv            # IC / general ladders
python scripts/validate_csv.py <role>-ladder.csv --manager  # also rejects position-locked language
```

Fix every ERROR it reports and re-run until it prints OK; treat WARNs as review prompts.

### 7. Offer the contribution gate

Per `references/capability-framework.md`: diff what this run produced against the framework
(unmatched competencies → drafted catalog rows with P1–P6 profiles; new or updated role record),
scrub anything org-specific, show the user exactly what a PR would contain, and **ask permission**.
An explicit yes in this conversation is the only thing that authorizes a contribution; declining
changes nothing remotely and ends the matter for the session.

## Hard rules (these prevent the known failures)

- **Three genuine tiers; no 1:1 mappings.** Focus areas span multiple competencies; key areas span
  multiple focus areas.
- **Competency names ≤ 60 characters.** Short label only.
- **Cells are present-tense observable behaviors** that peers, leaders, and reports can witness —
  not past-tense achievements, not internal states, not adjectives.
- **Depth and scope appear separately in every cell.**
- **SFIA (and any competency library) is overlay-only.** Never let it shape the prose.
- **Manager ladders stay demonstrable before the title** — influence/leverage behaviors, never
  position-locked language.
- **IC tracks mark the terminal level** (typically level 3 / Senior) and say what it means.
- **JD requirements trace to matrix cells.** No invented requirements, no years-of-experience
  gates (years may appear only as labeled guidelines).
- **Framework canon wins on structure.** When a role record exists, its areas/foci/competency
  names/IDs are used verbatim — never re-derived. OCF IDs appear in the markdown only, never the
  CSV.
- **Contributions are gated.** Nothing is PR'd to the framework without the user's explicit yes in
  the current conversation, after seeing the exact scrubbed content.

## Reference files

- `references/capability-framework.md` — the Open Capability Framework integration: live fetch,
  adapt/compose/generate modes, role-record schema, and the gated-contribution protocol.
- `references/calibration.md` — the three variants, level anchors, terminal-level guidance, and
  the research source list per variant.
- `references/prose-register.md` — the cell format and register every cell must follow.
- `references/job-descriptions.md` — the per-level JD format and how hiring panels use it.
- `references/skillmatrix-csv.md` — the exact skill-matrix app import contract and its failure
  modes.
