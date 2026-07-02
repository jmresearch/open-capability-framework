# Prose register — how every cell must read

The content of a ladder lives in the per-level cells. Their quality is the whole game. This is the
register converged on across many real ladders; deviating from it (especially toward competency-
framework paraphrase) produces work that gets rejected.

## The cell format: depth and scope, separated

Each cell encodes two axes explicitly:

```
Depth: <what they can do, and how deeply, at this level>.  Scope: <how wide the blast radius is>.
```

- **Depth** = mastery of the skill itself. It progresses: *does, with guidance* → *does
  independently* → *owns and designs* → *sets the standard others follow* → *drives strategy* →
  *sets direction*.
- **Scope** = how far the work reaches. It widens through **adoption breadth**, not headcount:
  task → component → capability/domain → multiple teams → organization → company.

Keeping the two axes visibly separate is the point. A senior person can have deep skill at narrow
scope, or moderate skill at wide scope; the cell must let a rater see both.

## Present-tense, observable, by everyone around them

Cells describe **present-tense behaviors that the person's peers, leaders, and reports can
actually see** — in work product, reviews, incidents, standups, planning, hallway decisions. Not
past-tense achievements ("led the migration"), not internal states ("understands distributed
systems"), not adjectives ("is a strong communicator"). If a clause can't be witnessed by someone
watching the person work, rewrite it as the observable that would make it visible.

The grounding reference for this register is the CircleCI Engineering Competency Matrix
(https://progression.fyi/f/circle-ci). When in doubt whether a cell reads like an industry matrix
or a paraphrased framework, compare it to CircleCI's cells.

**Example — one competency, "Software Design & Architecture," across levels (abridged):**

- L1: **Explains the system's architecture in their own words and navigates its diagrams to find
  what they need.** Uses pattern names correctly in reviews. *Scope:* implements designs specified
  by others.
- L3: **Selects patterns by trade-off in design docs that name the alternatives considered.**
  Designs for evolution; produces diagrams that anchor design reviews; catches coupling and
  scaling problems in others' designs before build. *Scope:* owns architecture for a capability;
  runs its design reviews.
- L5: **Sets the architectural direction multiple teams build against** and removes the systemic
  obstacles that block it. *Scope:* org-wide.

## The bold-lead-clause convention

Wrap the single most distinctive observable in each cell in `**…**`. Reading **down a level's
column** should give an "evidence ladder" — a skim path of escalating, concrete behaviors — rather
than an "adjective ladder." Put the bold on the behavior that most distinguishes this level from
the one below it.

## Cumulative but self-contained

Each level includes everything below it, applied with more depth and wider scope. But write each
cell so it reads on its own — no literal "+ " prefixes and no "also does X" back-references. The
progression is carried by the words and the column layout, not by punctuation.

## Competency libraries are an overlay, never the source

Do not write cells by paraphrasing SFIA or any competency-library descriptors. That produces
generic, framework-flavored, often past-tense "trophy" language that doesn't reflect what the
industry observes at each level. Write from how the role is actually leveled (the CircleCI
register, published company frameworks, StaffEng for staff-plus, the field's real practice), then
attach library codes as a comparison crosswalk if useful.

## Manager ladders: competency vs. scope (keep high levels demonstrable)

For manager/leadership ladders there's an extra trap. Competency is **what a person does and can
demonstrate before they hold the title**; scope is **what the organization grants when a seat
opens**. If senior cells are written in position-locked language — "manages managers," "owns a
sub-org," "through their managers" — those levels become impossible to *demonstrate* without
already holding the structure, which defeats a ladder meant to show readiness.

Fix: write the upper levels as **indirect-leverage behaviors** the person can show now — outcomes
achieved through other leaders they develop and influence, mechanisms and standards others adopt,
decisions shaped across teams they don't manage. This is the "do the job you want" principle: the
cell names a proxy demonstration of the higher-level competency. Keep an honest caveat that some
accountability is only fully exercised in-seat, so readiness is provable early without overstating
scope already held.
