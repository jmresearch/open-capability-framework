# CSV import contract — skillmatrix.bubtaylor.com (optional export)

Only produce this file when the user asks for it or mentions the skill-matrix app. It is the exact
format the app's importer expects, reverse-engineered from its `ladder_skills` table and hardened
against two real import failures. Honor it precisely.

## Row layout

A flat CSV with a `type` column in position 1 that tells the importer how to read each row. Column
order is fixed:

```
type, key_area, key_attribute, theme, L1, L2, L3, … (one level column per level)
```

Rows, in order:

| type               | what it carries                                                                    |
|--------------------|------------------------------------------------------------------------------------|
| (header row)       | literally `type,key_area,key_attribute,theme,<level strings>`                        |
| `meta_name`        | ladder name in the `key_area` cell. ≤ 100 chars. Required, exactly one.             |
| `meta_description` | one-sentence description of the ladder in the `key_area` cell. Optional.            |
| `level_title`      | the role title for each level, in the level columns. Required, all non-empty.       |
| `level_scope`      | the scope band for each level, in the level columns. Optional.                      |
| `level_focus`      | a short phrase capturing each level's intent, in the level columns. Optional.       |
| `skill` (×N)       | one per competency: key_area, key_attribute, theme, then the per-level cell prose.  |

The level-column headers are the level strings themselves (e.g. `E1…E6`, `M1…M6`, or even
`Junior,Mid,Senior`) — they become the level identifiers in the app, so use the ladder's real
codes. Between one and **seven** level columns are accepted, and the headers must be unique.
Human-readable titles ride in the `level_title` row. Empty cells are allowed in the level columns
of `skill` rows (a competency need not have a description at every level), though a complete
ladder fills them all.

## The three-tier hierarchy (the most important rule)

`key_area → key_attribute → theme` is a **genuine nesting**, not three names for the same thing:

- **key_area** — the top grouping (6 is typical). Spans multiple key_attributes.
- **key_attribute** — the focus/sub-grouping. **Spans multiple themes.**
- **theme** — the individual competency. The short leaf label.

A one-to-one mapping between key_attribute and theme is a **structural error**. If a focus has
only one competency under it, re-cut the foci so each spans 2+ themes. Do NOT paper over a
two-tier source by duplicating key_area into key_attribute; design a real middle tier. Every
`(key_area, key_attribute, theme)` triple must be unique.

## Failure mode 1 — the `theme` VARCHAR limit

`theme` maps to a tight `VARCHAR` on `ladder_skills`. A verbose sentence there overflows it and
the import **hard-fails** with SQLAlchemy/MySQL error **1406 (Data too long)**; the whole import
aborts. Therefore: **`theme` is the short competency name only** — keep it under 60 characters
(the real column is tight, so shorter is safer). There is **no description column** on the table;
verbose prose has nowhere to live, so drop it or fold it into the per-level cells.

## Failure mode 2 — prose in the wrong place

Because there's no description column, the temptation is to stuff a competency description into
`theme` (→ failure mode 1) or to invent a column the importer ignores. Don't. The per-level
depth/scope prose belongs in the **level columns** (L1…Ln) on each `skill` row — those columns are
not length-constrained the way `theme` is.

## Formatting rules

- Proper CSV quoting on any cell containing a comma (e.g., `"Food Safety, Quality & Compliance"`).
- Strip `**…**` bold markers from cell prose (the app renders plain text).
- Strip any leading `+ ` additive markers so each level cell reads self-contained.
- Exactly one `meta_name` (≤ 100 chars) and one each of the `level_*` rows, with every level slot
  filled.
- Every row has exactly the header's column count.

## Self-validation before delivering

Confirm: exactly one `meta_name` ≤ 100 chars; one `level_title` with all titles non-empty; 1–7
level columns with unique header strings; at least one `skill` row; all triples unique; longest
`theme` under the cap; no over-wide rows. If any check fails, fix the content — don't ship a file
that will abort on import.
