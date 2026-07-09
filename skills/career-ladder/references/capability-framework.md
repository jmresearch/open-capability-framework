# Open Capability Framework integration — live canon, gated contributions

The methodology in this skill is stable; the *coverage* — which competencies exist for a role and
what they're called — comes from the **Open Capability Framework** (OCF):
https://github.com/jmresearch/open-capability-framework — an open, technology-agnostic library
(429+ capabilities across 36 domains, each with P1–P6 behavioral profiles and an S1–S6 role-scope
axis). Fetching it live at generation time is what makes two runs of this skill produce the same
ladder instead of two different ones — and the contribution gate is what makes the framework more
canonical the more people use it.

## 1. Fetch at generation start (never bundle, never trust a stale copy)

Before building any ladder, fetch the live catalog and check for a role record:

```
https://raw.githubusercontent.com/jmresearch/open-capability-framework/main/data/capabilities.csv
https://raw.githubusercontent.com/jmresearch/open-capability-framework/main/roles/<role-slug>/role.yaml
```

(`<role-slug>` = kebab-case role name, e.g. `engineering-management`, `platform-engineering`.)
Use whatever fetch tool the environment has (WebFetch, curl, git clone --depth 1). If the
environment has no network access, say so, proceed with the methodology alone, and note in the
calibration summary that the ladder was generated unanchored to the framework.

## 2. Three modes, by what the framework already knows

- **Role record exists → ADAPT mode.** The role record *is* the canonical structure: use its key
  areas, focus areas, competency names, capability IDs, anchors, and per-level proficiency targets
  verbatim. Generate only what's role-instance-specific: the org-calibrated cell prose (and reuse
  the bundled canonical cells outright when the user gave no org context). Do not re-derive the
  structure — that would reintroduce the run-to-run variance this exists to kill.
- **No role record, but the catalog covers the role → COMPOSE mode.** Build the competency list
  *from* matching OCF capabilities: use their canonical names as themes (shorten to ≤60 chars if
  needed) and carry their IDs. Add role-specific competencies only where the catalog genuinely has
  no match — those are contribution candidates.
- **Catalog barely covers the role → GENERATE mode.** Build per the methodology, map whatever does
  match, and treat the rest as a proposed new domain/capability set for the gate.

## 3. Mapping rules

- Match semantically, not lexically — "Composure under pressure" and "Resilience & energy" are the
  same capability; check the capability's description and P-profiles, not just its name.
- In the **markdown ladder**, each competency heading carries its reference on the anchor line's
  row: `OCF: EM-03` (or `OCF: proposed` for unmatched ones). The **CSV never carries OCF IDs** —
  the import table has no column for them.

## 4. Cell derivation and mapping (normative)

### Cell derivation rule

A ladder cell is **assembled, never authored**. Every cell has exactly three parts, in order:

1. **Bar — canonical, verbatim.** The catalog capability's profile text at the mapped proficiency
   level, copied byte-for-byte from the catalog. Never paraphrase, never re-flavor, never blend
   adjacent levels. Two roles mapping the same capability at the same proficiency show
   **identical** bar text — that identity is the point of a shared framework.
2. **Evidenced by — role-specific, optional.** One sentence naming how the bar is observably met
   in *this* role's context. It must be an **instance** of the bar: same behavior, same autonomy
   level, role-specific artifact. ("New platform hire ships a paved-road change in their first
   sprint" instantiates "new hires ship in their first weeks.") It may narrow the bar to this
   role's work; it must never raise, lower, or extend it. **Test:** strip the role nouns — what
   remains must restate the bar's behavior at the bar's autonomy. If your evidence sentence
   describes designing systems others adopt while the bar says "runs independently," you haven't
   written evidence, you've discovered a wrong mapping. Fix the mapping.
3. **Scope.** The role level's scope band from `role.yaml`, stated as reach ("one platform
   team"), never as depth.

### Mapping rule

A proficiency mapping (`EM-13: M1 → P2`) is a **sourced claim, not a template default**:

- Before mapping, read the capability's full P1–P6 profile *and* the proficiency-scale
  definitions. The mapping asserts: "the industry-expected bar for this capability at this role
  level is exactly the Pk profile."
- Every mapping carries a bibliography `source` key and a `why` — one to two sentences connecting
  the source to that level (e.g., "First-line managers are expected to run onboarding
  independently, not design it: Tuckman's arc is led per-team at this level; playbook design
  across teams is the P4 behavior — see also GitLab EM vs Director requirements").
- A ladder-wide pattern ("manager tracks start at P2") is not a per-competency rationale. If the
  honest reason is a convention, cite the convention's source and say so — but check each
  competency against it; conventions have exceptions (the EM ladder already maps LI-01 M1 → P3,
  not P2).
- **If no catalog profile matches the real bar at this level, do not write custom cell text.**
  Either the catalog profile is miscalibrated — file a catalog amendment with sources in the same
  change — or the competency doesn't belong at that level in this ladder.

### Order of operations (hard gate)

Sources first, competencies second, mappings third, cells never:

1. Research and register sources as bibliography entries.
2. Admit a competency only when its catalog P1–P6 profile is fully sourced (one citation + why
   per level). Missing sourcing = supply it as a catalog change in the same PR, or the competency
   is out.
3. Choose per-level mappings, each with source + why.
4. Cells render mechanically from catalog + role.yaml. If you find yourself writing depth prose
   in a ladder, stop — you're either duplicating the catalog or contradicting it.

### Smells that mean you're winging it

- Cell text that doesn't appear in the catalog.
- The same P-row on every competency without per-competency checking.
- An "evidenced by" containing "designs / sets the standard / drives strategy" under a P2/P3 bar.
- A mapping rationale that restates the mapping ("M1 is P2 because M1s operate at P2").
- Writing cells before the bibliography exists.

## 5. Role records (`roles/<slug>/role.yaml`)

The canonical-ladder layer the skill reads and (with permission) writes:

```yaml
role: Engineering Management
slug: engineering-management
variant: manager            # ic_technical | manager | general
levels:
  - {code: M1, title: Engineering Manager, scope: one team, focus: leading one team directly}
  # … one entry per level
competencies:
  - theme: Onboarding & team formation
    capability: EM-13
    key_area: People Leadership & Team Development
    key_attribute: Hiring & Team Composition
    anchor: tuckman1965
    mappings:
      M1: {p: P2, sources: [tuckman1965, gitlab-em-jd], why: "First-line manager runs onboarding independently per team; playbook design across teams is the P4 behavior."}
      M2: {p: P3, sources: [tuckman1965], why: "..."}
      M3: {p: P4, sources: [...], why: "..."}
      M4: {p: P4, sources: [...], why: "Same depth as M3 — the differentiation at M4 is scope (sub-org), not a deeper formation bar."}
      M5: {p: P5, sources: [...], why: "..."}
      M6: {p: P6, sources: [...], why: "..."}
    evidence:
      M1: "New platform hire ships a paved-road change in their first sprint."
```

Alongside `role.yaml`, the role directory may hold `ladder.md` / `ladder.csv` — a canonical
rendering with full cell prose, used as the starting point in ADAPT mode.

## 6. The contribution gate (mandatory, explicit, per-run)

After delivering the ladder, compute what this run produced that the framework doesn't have:

1. **New capabilities** — competencies with no OCF match. For each, draft a catalog row: proposed
   ID in the right domain (next free number, e.g. `EM-13`), technology-agnostic description, and a
   P1–P6 behavioral profile distilled from the ladder's cells.
2. **Amendments** — where a run's evidence disagrees with an existing capability (miscalibrated
   P-profile, a description spanning two assessable things, a needed split/merge), draft an
   amendment proposal per `contrib/README.md`.
3. **Role record** — a new `roles/<slug>/` if none existed, or a diff to the existing one
   (added competencies, refined proficiency targets).
4. **Benchmark entry** — when minting ran on a model/effort with no entry in
   `benchmarks/model-efficiency.yaml`, the run telemetry (coverage, validator results, token
   usage) can become a new entry (see `benchmarks/README.md`).

Then **ask the user's permission** before contributing anything, showing exactly what would be
submitted. Hard rules:

- **Never contribute without an explicit yes from the user in this conversation.** Silence,
  "looks good" about the ladder itself, or a prior run's consent do not carry over.
- **Scrub before showing:** org names, internal system names, compliance regimes tied to the org,
  headcounts, anything identifying. Contributions must read as generic as the rest of the catalog.
- Tell the user plainly: the contribution is a public PR to
  github.com/jmresearch/open-capability-framework under CC BY 4.0.
- New capabilities go under `contrib/` in the PR (maintainers fold them into `data/` and the
  workbook on acceptance); role records go under `roles/`. Open the PR with `gh` or git push to a
  fork/branch — whatever access exists; if none, hand the user the prepared patch and the PR
  instructions instead.
- If the user declines: deliver everything locally, change nothing remotely, and don't ask again
  in the same session.

This is the network effect: every accepted PR makes the next person's ladder — and every rerun of
yours — start from a more complete, more canonical framework.
