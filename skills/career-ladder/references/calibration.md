# Calibration — variants, level anchors, and what to research

Calibration is what makes a ladder "industry-validated" rather than invented. Pick the variant,
decide the levels and terminal level BEFORE writing content, and research the variant's sources to
ground the bar at each level.

## Quick variant decision

- Title contains Engineer / Developer / SRE / Architect / Scientist / Analyst / Designer and the
  role is an individual contributor → **ic_technical**
- Title contains Manager / Director / VP / Head of, or the job is leading leaders and teams →
  **manager**
- Operational, field, or trade role (plant ops, manufacturing, facilities, field service, food
  processing…), or the ladder is for a non-office team → **general**
- Genuinely ambiguous (e.g., "Tech Lead" — IC or manager?) → the one case worth a single
  clarifying question; otherwise default to the maker track and say so.

## ic_technical — individual-contributor technical roles

- **Levels:** six (L1–L6). Use fewer only if the org's banding genuinely has fewer.
- **Terminal level: L3 / Senior.** This is the level a strong professional can stay at
  indefinitely without being "behind." L4+ is not "more of L3" — it is a fundamentally different
  job defined by multi-team scope. Call the terminal level out explicitly in the ladder overview.
- **Scope bands by level:**

  | Level | Typical title    | Scope band                     |
  |-------|------------------|--------------------------------|
  | L1    | Associate        | task                           |
  | L2    | Professional     | component                      |
  | L3    | Senior           | a capability/domain — terminal |
  | L4    | Staff            | multiple teams                 |
  | L5    | Senior Staff     | organization                   |
  | L6    | Principal        | company                        |

- **Anchors to research:** the CircleCI Engineering Competency Matrix
  (https://progression.fyi/f/circle-ci) for the observable-behavior register; Google L3–L8 and
  Meta E3–E8 level norms plus levels.fyi for scope bars; Dropbox's published career framework for
  scope-by-level language; StaffEng for staff-plus behaviors (L4–L6). For platform/infrastructure
  roles add the CNCF Platform Engineering Maturity Model and Team Topologies, and keep "platform
  as a product" first-class — not rebranded ops. Real job postings serve as a coverage check and
  seniority validation. SFIA (sfia-online.org) is overlay-only.
- **Typical shape:** 6–7 key areas, ~20 focus areas, 25–42 competencies. Don't pad — every
  competency must be independently ratable.

## manager — people-leadership roles

- **Levels:** six (M1–M6), unless the org says otherwise.

  | Level | Typical title              | Scope                     |
  |-------|----------------------------|---------------------------|
  | M1    | Manager                    | one team                  |
  | M2    | Senior Manager             | a complex / critical team |
  | M3    | Director                   | a domain (cross-team)     |
  | M4    | Senior Director            | a sub-org                 |
  | M5    | VP                         | a function                |
  | M6    | SVP / Org Lead             | org-wide                  |

- **Terminal level:** usually none in the IC sense — each level is a distinct scope of leadership.
- Where a specific org puts a band matters (some orgs define Director as domain ownership through
  influence and Senior Director as managing managers). Apply any org calibration the user gives.
- **The competency-vs-scope rule is mandatory** (see prose-register.md): write M3–M6 as
  demonstrable influence and leverage behaviors, not position-locked language. Include a short
  "two dimensions" note in the ladder overview: competency is what a person can demonstrate before
  holding the title; scope is what the organization grants when a seat opens.
- **Anchors to research:** the Korn Ferry Leadership Architect competency library; StaffEng and
  engineering-leadership writing for director-plus scope; the CircleCI matrix for the IC-facing
  competencies managers still need to recognize; the user's org calibration.
- **Typical shape:** ~6 key areas, ~25–28 leadership competencies.

## general — operational, field, and trade roles

- **Levels:** typically four or five (e.g., Team Lead → Shift Supervisor → Area Lead → Department
  Manager → Operations Manager, or Operator-anchored variants). No terminal-IC concept; the top
  level is the senior operational owner.
- **Register:** practical, observable, shop-floor behaviors — not office-skill abstractions. The
  point of these ladders is often to make *foundational* competence explicit (checks
  communications at shift start, knows when to perform scheduled maintenance versus escalate), so
  don't skip the basics at the low levels.
- **Anchors to research:** the field's real certifications and standards (for food processing:
  HACCP, GMPs, SQF/BRC; every field has its own), any safety or compliance regime that defines
  observable competence, and real lead/supervisor/manager job postings in that field. No SFIA.
- **Typical shape:** ~6 key areas, ~13 focus areas, ~25 competencies.

## Theory anchors — every competency names its "why"

Every competency in the **markdown ladder** carries a one-line **theory anchor**: the named,
citable framework, research finding, or standard that explains why this is a competency and what
good looks like, plus a clause on why it applies. Under the competency heading, before the level
cells:

```
*Anchor:* Edmondson, The Fearless Organization (2018) — psychological safety is the top
predictor of team effectiveness (Google Project Aristotle). *Why:* safety to speak up is the
substrate the other team-health behaviors depend on.
```

Rules:

- **Real and citable.** Name the author/organization and work (year where it helps). No invented
  or hand-wavy sources; if no credible anchor exists, that's a signal the competency may be
  padding.
- **Anchors ground; they never dictate prose.** The same rule as SFIA — the level cells stay in
  the observable-behavior register. The anchor says *why the competency exists*; the cells say
  *what you can watch someone do*.
- **Markdown only.** The skill-matrix import table has no column for anchors — never fold them
  into `theme` or the level cells. They live in the ladder document (and a Sources section at the
  end listing each anchor once).
- **Typical wells by variant** — ic_technical: DORA/Accelerate, Team Topologies, Google SRE,
  OWASP, StaffEng, the testing-pyramid literature; manager: Kotter, Rumelt, Herzberg /
  Self-Determination Theory, GROW / Google Project Oxygen, Edmondson, Radical Candor,
  Korn Ferry Leadership Architect; general: the field's certifications, standards, and safety
  regimes (HACCP, GMPs, OSHA, and their equivalents).

## SFIA and other competency libraries: overlay only

Never write cell prose by paraphrasing a competency library — it produces generic, past-tense,
trophy-statement language that doesn't reflect what the industry observes at each level. If you
attach SFIA codes, present them as a separate comparison crosswalk (link format:
`https://sfia-online.org/en/sfia-9/skills/{skillcode-lowercased}`). Where SFIA defines a skill
only from level 4 upward, cite that as corroboration that the behavior is staff-plus — don't copy
its words.
