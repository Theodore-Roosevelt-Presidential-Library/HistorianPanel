# Contributing

People and agents both contribute here. The rules are the same for both, with
two extra limits for agents.

## Every change

1. Branch from `main`. Agents use `agent/<short-name>-<yyyymmdd>`.
2. Follow [the skill standard](plugins/historian-panel/reference/skill-standard.md).
   The short version: skills hold pointers and traps, never facts used as
   sources, and nothing private goes in this public repository.
3. Run the checks:
   ```
   python3 -m venv .venv
   source .venv/bin/activate
   pip install -r requirements-dev.txt
   python scripts/lint_skills.py
   python scripts/check_provenance.py
   python -m unittest discover -s tests
   ```
4. Open a pull request using the template.
5. A code owner reviews and merges.

## Extra limits for agents

- Label the pull request `agent-authored`. Never merge or approve.
- No more than 3 agent-authored pull requests in any 7 days. A workflow enforces
  this. Put overflow in `proposals/backlog.md`.

## What reviewers look at

- Did the regression score hold? (CI posts it on the pull request.)
- Does any skill now state a fact a specialist could treat as an answer?
- Does every new trap cite a confirmed ledger ID?
- Does the new scope overlap an existing specialist?
- Is anything private in the diff?

Curatorial content (quotes, image identification, family facts) should get a
review from someone with curatorial standing before merge, in addition to the
code owner.

## Adding a ledger ID

When a trap is learned from a confirmed error, add the ID and status to
`provenance/claim-ids.txt`. IDs and statuses only; the claim text stays in the
private ledger.
