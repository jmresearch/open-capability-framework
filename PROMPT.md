# Career Ladder + Hiring Job Descriptions — the generic prompt

Copy everything below the line, replace `{{JOB TITLE}}` (and optionally fill the context knobs),
and paste it into Claude — claude.ai, the desktop app, or the API. You'll get a complete career
ladder and a set of per-level job descriptions a hiring panel can score candidates against.

---

I need a complete, industry-calibrated career ladder and hiring toolkit for the role:
**{{JOB TITLE}}**

Optional context — use what's filled in, use your defaults for the rest, and state every default
you chose:

- Organization / industry context: {{none}}
- Number of levels or existing level names: {{you decide}}
- Anything org-specific about where levels sit (e.g., "Director here means domain ownership"): {{none}}

## Part 0 — If you have web access: anchor to the Open Capability Framework (read-only)

Fetch `https://raw.githubusercontent.com/jmresearch/open-capability-framework/main/data/capabilities.csv`,
`https://raw.githubusercontent.com/jmresearch/open-capability-framework/main/data/bibliography.csv`,
and `https://raw.githubusercontent.com/jmresearch/open-capability-framework/main/data/capability_levels.csv`,
and check for `https://raw.githubusercontent.com/jmresearch/open-capability-framework/main/roles/<role-slug>/role.yaml`
(kebab-case role name). If a role record exists, use its key areas, focus areas, competency names,
and capability IDs **verbatim**, and per-level cell text MUST be the catalog capability's profile
at the mapped proficiency, copied verbatim, as the bar — role-specific nuance goes only in a
separate "Evidenced by" line, never folded into or rewriting the bar. Otherwise, wherever a catalog
capability matches a competency you'd write, use its canonical name and note its ID. This keeps
independently generated ladders consistent with each other. Read-only: do not attempt to submit
anything. If you have no web access, skip this part and say so.

## Part 1 — Classify and calibrate (show your choices before building)

1. Classify the role into one of three tracks and say which you chose:
   - **Individual contributor / technical** (engineer, analyst, designer, scientist, and similar
     maker-track roles): default to six levels, and mark level 3 (Senior) as the **terminal
     level** — the level a strong professional can stay at indefinitely without being "behind."
     The levels above it are a *different job* defined by multi-team scope, not "more of Senior."
   - **People manager** (manager, director, VP, head-of): default to six levels with scope
     progressing one team → complex/critical team → domain → sub-org → function → organization.
   - **Operational / field / trade** (plant operations, manufacturing, facilities, field service,
     food processing, and similar): default to four or five levels (for example Operator → Senior
     Operator → Team Lead → Shift Supervisor → Operations Manager). Make foundational competence
     explicit at the low levels — the point of these ladders is often to name the basics, not to
     skip them.
2. Calibrate against how the industry actually levels this role: published leveling frameworks
   from real companies, real job postings at each seniority, and the field's actual
   certifications and standards. Do **not** write from generic competency-framework language
   (SFIA and similar libraries may be cited as a comparison, never paraphrased as content).
   State which anchors you used.

## Part 2 — Build the career ladder (competency matrix)

Build a three-tier competency hierarchy:

- **Key areas** (5–7): the major domains of the job.
- **Focus areas** (2–4 per key area): sub-groupings within a key area. Every focus area MUST
  contain two or more competencies — a focus area with exactly one competency means the grouping
  is wrong; merge or re-cut it.
- **Competencies** (25–40 total): each independently observable and ratable. The competency name
  is a short label (under 60 characters), never a sentence.

Write one cell per competency per level, following these rules exactly:

- **Assemble each cell from two parts, in order and separated by a blank line: Bar, then
  Evidenced by.** The **Bar** is the depth behavior: how well they do the thing (does with
  guidance → does independently → owns and designs → sets the standard others follow → drives
  strategy → sets direction). Where a matching Open Capability Framework capability exists, the
  Bar is that capability's profile text at the mapped proficiency level, copied verbatim — never
  paraphrased, never blended with an adjacent level; identical capability+proficiency must read as
  identical bar text. **Evidenced by** is an optional one-sentence, role-specific instance of the
  Bar — same behavior, same autonomy, this role's artifact — that may narrow the Bar to this
  role's work but must never raise, lower, or extend it. **Scope is not part of the cell**: it's
  how far the work reaches (task → component → capability/domain → multiple teams → organization →
  company), stated as reach, never as depth, and it lives on the level (one scope band per level,
  carried by the ladder record), not repeated inside each cell. A rater must be able to see both
  cell parts plus the level's scope; a person can be deep-and-narrow or moderate-and-wide.
- **Cite the bar.** Every proficiency mapping and every level's behavior must carry a named, real,
  verifiable citation — a framework, research finding, standard, or published company ladder —
  plus a one-to-two-sentence why connecting the source to that level. If you have no web access,
  say so plainly in the calibration summary, and still list a per-level source from your own
  knowledge for each competency, flagged for the reader to verify.
- **Present-tense, observable behaviors only.** Every clause must be something peers, leaders, or
  reports could actually witness — in work product, reviews, meetings, incidents, planning. No
  past-tense achievements ("led the migration"), no internal states ("understands distributed
  systems"), no adjectives ("strong communicator"). If it can't be witnessed, rewrite it as the
  observable that would make it visible.
- **Bold the single most distinctive behavior in each cell**, so reading down a level's column
  gives an evidence ladder rather than an adjective ladder.
- **Cumulative but self-contained.** Each level includes everything below it applied more deeply
  and widely, but every cell must read on its own — no "+ also does X" back-references.
- **For manager tracks:** write the senior levels as influence-and-leverage behaviors a person can
  demonstrate *before* holding the title — outcomes achieved through leaders they develop,
  mechanisms and standards other teams adopt, decisions shaped across teams they don't manage.
  Never position-locked language like "manages managers" or "owns a sub-org," which makes the
  level impossible to demonstrate without already having the seat.
- **Give every competency a one-line theory anchor**: the named, citable framework, research
  finding, or standard that explains why this is a competency (e.g., Edmondson on psychological
  safety, DORA/Accelerate on delivery flow, Kotter on change, the field's certification body),
  plus a clause on why it applies. The anchor grounds the competency — the level cells must still
  be written as observable behaviors, never paraphrased from the anchor. End the ladder with a
  Sources section listing each anchor once.

Render the ladder as: (a) a level-overview table — level code, title, scope band, one-line focus;
then (b) the full matrix grouped by key area → focus area → competency with the per-level cells.

## Part 3 — Write one job description per level, built for hiring

For EACH level, produce a job description a hiring panel can score candidates against:

1. **Title and mission** — one sentence on why this level exists.
2. **Scope** — the blast radius of the role at this level.
3. **Responsibilities** — six to ten present-tense bullets drawn directly from this level's column
   of the matrix.
4. **Competency requirements** — grouped by key area, each requirement traceable to a specific
   matrix cell.
5. **Interview evidence guide** — for each key area: one or two behavioral questions to probe it,
   plus what an **at-level answer** sounds like versus a **below-level answer** versus an
   **above-level answer**. Concrete signals, not vibes.
6. **Level boundaries** — "You're at this level if…" and "You're ready for the next level if…" as
   two or three observable statements each.
7. Prefer demonstrated behaviors over years-of-experience requirements. If you include years,
   label them a guideline, not a gate.

## Output

Deliver two artifacts in markdown — **(1) the career ladder** from Part 2 and **(2) the per-level
job descriptions** from Part 3 — preceded by a short calibration summary: the track you chose,
level count, terminal level (if any), the anchors you calibrated against, and any judgment call I
should review.
