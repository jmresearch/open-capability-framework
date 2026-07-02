# Amend EM-03: Team health & engagement

- **Type:** split
- **Why:** The engineering-management role record (`roles/engineering-management/role.yaml`)
  references EM-03 from two distinct ladder rows — Psychological Safety and Motivation &
  Engagement — because its description spans both. They are assessed differently (safety is
  witnessed in dissent, incident candor, and who speaks in meetings; motivation is witnessed in
  hygiene fixes, recognition, and intrinsic-driver design) and the 8-run ensemble consistently
  generated them as separate competencies (both appeared in 8/8 independent runs).
- **Current:** `EM-03 | People Management | Team health & engagement` — one capability covering
  psychological safety, engagement, motivation, and team-health signals.
- **Proposed:** two capabilities:
  - `EM-03 | People Management | Psychological safety & team health` — creates the conditions
    where people raise problems, dissent, and admit mistakes without penalty; reads and repairs
    team-health signals (conflict, burnout risk, on-call load).
    - **P1 (Assisted):** With guidance, runs meetings where quieter members are heard; escalates
      team-health concerns they notice.
    - **P2 (Independent):** Creates safety on their own team — models fallibility, protects
      dissent, surfaces and resolves conflict early; monitors basic health signals.
    - **P3 (Proficient):** Sustains safety through pressure (incidents, deadlines, change);
      repairs damaged trust; the team measurably speaks up (postmortems name real causes).
    - **P4 (Expert):** Diagnoses and fixes systemic safety failures across teams; other leaders
      seek their help on entrenched conflict and burnout patterns.
    - **P5 (Authority):** Sets the org's team-health bar and mechanisms; safety practices they
      designed are adopted org-wide.
    - **P6 (Pioneer):** Shapes how the industry thinks about team health; published practices
      others implement.
  - `EM-13 | People Management | Motivation & engagement` (next free EM id at time of writing) —
    builds durable intrinsic motivation: removes dissatisfiers, feeds autonomy/mastery/purpose,
    recognizes well.
    - **P1 (Assisted):** Recognizes teammates' good work; flags demotivating friction to their
      manager.
    - **P2 (Independent):** Knows what drives each person on their team; removes hygiene friction
      and matches work to intrinsic drivers; recognition is specific and timely.
    - **P3 (Proficient):** Sustains engagement through hard stretches; diagnoses systemic
      motivation problems (not just individuals) and fixes the conditions.
    - **P4 (Expert):** Builds engagement mechanisms other teams adopt; reverses disengagement
      trends beyond their own span.
    - **P5 (Authority):** Owns the engagement strategy for a function; conditions they designed
      show up in retention and survey trends.
    - **P6 (Pioneer):** Advances the practice of engagement in the field; frameworks others cite
      and use.
- **Affected role records:** `roles/engineering-management/role.yaml` — the Psychological Safety
  row keeps EM-03 (renamed sense); the Motivation & Engagement row re-points from EM-03 to the
  new id. Both rows' `proficiency` targets are unchanged.
