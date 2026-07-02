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
- Calibrate cells against the capability's P1–P6 profile: a level's cell should describe the same
  bar as the profile at that level's expected proficiency (IC guide: E1≈P1–P2, E2≈P2, E3≈P3,
  E4≈P4, E5≈P5, E6≈P6; manager levels similar on their axis). Where your cell and the P-profile
  disagree about the bar, flag it — either the cell is miscalibrated or the profile needs a PR.

## 4. Role records (`roles/<slug>/role.yaml`)

The canonical-ladder layer the skill reads and (with permission) writes:

```yaml
role: Engineering Management
slug: engineering-management
variant: manager            # ic_technical | manager | general
levels:
  - {code: M1, title: Engineering Manager, scope: one team, focus: leading one team directly}
  # … one entry per level
competencies:
  - theme: Team health & engagement          # ≤60 chars, the ladder's row label
    capability: EM-03                        # OCF id, or "proposed" with a note
    key_area: People & Talent
    key_attribute: Team Health & Culture
    anchor: "Edmondson, The Fearless Organization (2018)"
    proficiency: {M1: P2, M2: P3, M3: P3, M4: P4, M5: P5, M6: P6}
```

Alongside `role.yaml`, the role directory may hold `ladder.md` / `ladder.csv` — a canonical
rendering with full cell prose, used as the starting point in ADAPT mode.

## 5. The contribution gate (mandatory, explicit, per-run)

After delivering the ladder, compute what this run produced that the framework doesn't have:

1. **New capabilities** — competencies with no OCF match. For each, draft a catalog row: proposed
   ID in the right domain (next free number, e.g. `EM-13`), technology-agnostic description, and a
   P1–P6 behavioral profile distilled from the ladder's cells.
2. **Role record** — a new `roles/<slug>/` if none existed, or a diff to the existing one
   (added competencies, refined proficiency targets).

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
