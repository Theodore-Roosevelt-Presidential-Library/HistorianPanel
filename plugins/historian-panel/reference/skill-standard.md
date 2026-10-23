# Skill standard

What every HistorianPanel skill must look like. The linter
(`scripts/lint_skills.py`) enforces the parts marked **(linted)**.

## The core rule

Skills hold **pointers and traps, never facts used as sources.**

- Allowed: "Check every office held by a family member against the Biographical
  Directory of the U.S. Congress."
- Not allowed: "Ted Jr. never served in Congress." That is a fact. It belongs in
  the claim ledger with its two citations, not in a skill.

A skill tells a specialist where to look and what usually goes wrong. It never
tells the specialist what the answer is. If a skill states a fact, every later
check will trust it, and one error would spread to everything the panel
touches.

## File layout (linted)

- `skills/<name>/SKILL.md`, where `<name>` matches the frontmatter `name`.
- Frontmatter has `name` and `description`. Put the trigger first in the
  description, and keep it under 1,000 characters.
- Every skill is listed in `roster.yaml`.
- SKILL.md stays under 16,000 characters. Split long material into a
  `references/` file in the skill folder.

## Specialist sections (linted, in this order)

1. `## Scope`: what claims this specialist takes.
2. `## Out of scope`: what it hands off, and to whom.
3. `## Where to look first`: an ordered list of sources and record types, with
   what each is good and bad for.
4. `## Known traps`: patterns that have produced real errors.
5. `## Procedure`: the steps, in order.
6. `## Output`: always ends with "Follow reference/panel-rules.md section 11."

## Traps (linted)

Every bullet under `## Known traps` ends with one tag:

- `[ref: <ledger ID>]` for a pattern learned from a confirmed claim. The ID must
  be listed in `provenance/claim-ids.txt`. Several IDs: `[ref: A-01, G-15]`.
- `[method]` for a general method caution that needs no ledger entry (for
  example, "copyright dates are not creation dates").
- `[house-rule]` for a Library style or policy rule.

Describe the pattern, not the page. Write "Titles that changed over time
(Governor and Governor-General) are often mixed up," not "the Ted Jr. page called
him Governor-General of Puerto Rico."

## Content that never goes in this repo (linted where possible)

This repository is public.

- No text from licensed biographies or licensed collections. Cite them; do not
  quote them. No quotation longer than 25 words appears anywhere in a skill.
- No internal hostnames, private IP addresses, file paths on staff machines,
  credentials or tokens.
- No claim ledger entries, fix lists, or descriptions of errors on Library pages.
  Those live in the private ledger.
- No staff names or contact details. Refer to roles ("the Library's curatorial
  reviewer").

## Changing a skill

Skills change only through pull requests. Agent-written pull requests carry the
`agent-authored` label and need a human merge. See CONTRIBUTING.md.
