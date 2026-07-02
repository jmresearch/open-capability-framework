# Open Capability Framework

An open, **technology-agnostic** library of workforce capabilities — a community alternative to SFIA — for building career ladders and planning organizational capability across an entire enterprise.

> **Status:** v0.7 seed. 429 capabilities across 36 domains, each leveled with a six-point behavioral profile (P1–P6). Published as data first; a hosted builder is planned.

## What this is

The framework separates two things most career ladders conflate:

- **Proficiency (P1–P6)** — *how well* a person performs a capability. Intrinsic to the capability, reusable across every role. Dreyfus-derived, six fully-used levels (P1 Assisted → P6 Pioneer). This is the unit you assess and audit.
- **Scope (S1–S6)** — *how broad* a role's remit is (task → component → domain → multi-team → org → company). A property of the **role**, not the capability.

A role is then `required capabilities × minimum proficiency + one scope band`. An organization is split into **domains → capabilities**, each either covered or an explicit accepted gap. Capabilities are described by *what competence is needed*, never by a specific tool ("Relational data modeling," not "PostgreSQL"); technologies are treated as a separate layer that *satisfies* a capability.

## Structure

```
Segment → Domain → Focus Area → Capability → (P1…P6 behavioral profile)
```

Three segments group the 36 domains:

| Segment | Domains | Capabilities |
|---|---|---|
| Engineering & Technology | 13 | 194 |
| Product, Design & Cross-functional | 7 | 61 |
| Business & Corporate Functions | 16 | 174 |
| **Total** | **36** | **429** |

## Files

| Path | Contents |
|---|---|
| `data/capabilities.csv` | All 429 capabilities: id, segment, domain, focus area, capability, type (Behavioral/Technical), description, and the six P1–P6 behavioral profiles. |
| `data/capabilities.json` | Same data, nested (`levels.P1`…`levels.P6`). |
| `data/domains.csv` | Domain index: segment, prefix, focus-area count, capability count. |
| `data/proficiency_scale.csv` | The universal P1–P6 rubric. |
| `data/scope_levels.csv` | The S1–S6 role-scope axis, mapped to SFIA / Google-Meta levels. |
| `Open_Capability_Framework.xlsx` | The full workbook (catalog + Org Capability Map + Role Builder/Audit + methodology). |
| `roles/` | Role records: canonical career ladders as capability references with per-level proficiency targets (see `roles/README.md`). |
| `skills/` | Claude Code skills: `career-ladder` (ladder + hiring JDs for any role) and `create-canonical-role` (mint a stable role record via multi-run consolidation). |
| `PROMPT.md` | Copy-paste prompt for using the ladder methodology in any Claude chat. |
| `contrib/` | Staging for proposed new capabilities awaiting catalog acceptance (see `contrib/README.md`). |

## Using it: generate ladders and canonical roles

This repo doubles as a Claude Code plugin:

```
/plugin marketplace add jmresearch/open-capability-framework
/plugin install career-skills@open-capability-framework
```

Then ask for a career ladder for any role (`career-ladder` skill — fetches this framework live,
so ladders use canonical capability names, and roles with a record under `roles/` reproduce
identically), or ask to "make <role> canonical" (`create-canonical-role` skill — runs the
generation N times, consolidates the union, verifies exact reproduction, and opens a gated PR
here). Contributions are always gated on the user's explicit permission. No Claude Code? Use
`PROMPT.md` in any Claude chat.

## Methodology (brief)

Engineering/technology domains were distilled from [roadmap.sh](https://roadmap.sh) role and skill roadmaps; business/corporate domains from the [APQC Process Classification Framework](https://www.apqc.org/process-frameworks) plus functional competency models (SHRM, PMI, APICS). The structure follows the [CircleCI Engineering Competency Matrix](https://circleci.com/blog/why-we-re-designing-our-engineering-competency-matrix/) (CC BY 4.0). The two-axis split mirrors how [ESCO](https://esco.ec.europa.eu) and [Lightcast Open Skills](https://lightcast.io/open-skills) separate competencies from tools, and the proficiency scale is grounded in the Dreyfus model of skill acquisition. SFIA and levels.fyi were used for scope calibration only — neither is reproduced here.

Apparent cross-domain overlaps (e.g. "accessibility" in build vs. design vs. test) are intentional **lenses**: the same concept owned by different functions, kept separate because they are assessed by different roles.

## Roadmap

- Technology registry layer (technologies mapped to the capabilities they satisfy).
- ~~First-class Role records~~ — started: see `roles/`. A hosted role/ladder builder is still planned.
- Compensation-band modeling over the capability/scope vectors.
- TODO: "Build your own role" from canonical skills — search and mix-and-match catalog
  capabilities into a role record (choose capabilities, set per-level proficiency targets, emit
  the ladder), rather than generating from a title.
- TODO: Source canonical role ladders into the skill-matrix app
  (skillmatrix.bubtaylor.com) as importable starter templates.

## License

Content is released under **CC BY 4.0** (see `LICENSE`). Attribution: the Open Capability Framework contributors. Source frameworks are credited above; the APQC PCF itself is © APQC and is referenced, not redistributed — only our own technology-agnostic capability derivations are included here.
