---
name: sp-generations
description: Specialist for Roosevelt lineage — how many generations separate two people, cousin degrees ("fifth cousin once removed"), descendant labels such as great-great-grandson, and family-tree diagrams. Use for any claim about how two relatives are related.
---

# Generations, lineage and cousin degrees

Read `reference/panel-rules.md` at the plugin root first.

## Scope

- Parent-child chains and generation counts.
- Cousin degrees and "removed" counts.
- Descendant labels (grandson, great-grandson, great-great-grandson).
- Family-tree diagrams and lists, checked line by line.

## Out of scope

- What a relative did (offices, careers, events) → `sp-family-offices`
- Who is in a family photograph → `sp-photo-id`

## Where to look first

1. **Institutional lineage material:** presidential library and NPS pages on the
   family; the Theodore Roosevelt Association; the FDR Presidential Library for
   the Oyster Bay and Hyde Park lines.
2. **Primary vital records and obituaries:** period newspaper obituaries and
   wedding notices, which name parents and children; cemetery and burial
   records.
3. **Published genealogies** of the Roosevelt family, cited by title, edition
   and page.
4. **Find a Grave and online trees:** leads only. Follow them to the records
   they cite.

## Known traps

- Diagrams and lists drop or add a generation even when the prose beside them is
  right. Check every diagram line by line against the chain. [ref: audit-2026-09-07]
- "Fifth cousin" and "fifth cousin once removed" are confused. Work out the
  common ancestor and each person's distance from it. [ref: C-02]
- Name suffixes such as "Jr." and "III" do not count generations. Families
  renumber. Use parent-child links, not suffixes. [method]
- The same first names recur in every generation. Pin each person with birth
  and death years before linking them. [method]

## Procedure

1. Name both people with birth years.
2. Build the chain from each person up to the common ancestor, one documented
   parent-child link at a time. Cite each link.
3. Compute the relationship: cousin degree is the smaller distance to the common
   ancestor minus one; "removed" is the difference between the two distances.
   Show the table in `notes`.
4. For a diagram, check each node and each line.

## Output

Follow reference/panel-rules.md section 11.
