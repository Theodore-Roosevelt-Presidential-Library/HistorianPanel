# Quality layer

Checks that keep agent-written skills from degrading the panel. Most are not AI.

| Check | Runs | AI? | Fails the pull request when |
|-------|------|-----|------------------------------|
| **Linter** (`scripts/lint_skills.py`) | Every PR | No | A skill is missing sections, a trap has no tag, a description is too long, a quotation exceeds 25 words, or a secret, private IP, home path or denylisted term appears |
| **Provenance** (`scripts/check_provenance.py`) | Every PR | No | A trap cites a ledger ID that is not listed as confirmed or closed |
| **Unit tests** (`tests/`) | Every PR | No | The scripts themselves break |
| **Plugin validation** (`claude plugin validate`) | Every PR | No | The marketplace or plugin manifest is invalid |
| **Regression set** (`scripts/run_regression.py`) | PRs touching skills or agents, if the API key secret is set | Yes (it runs the panel) | The catch rate on known errors drops, or false alarms on known-true claims rise, beyond the tolerance in `tests/regression/baseline.json` |
| **Red team** (`scripts/redteam_mutate.py`) | Inside the regression run | No (deterministic) | Mutated true claims (shifted years, changed numbers, swapped months) slip through |
| **Skill reviewer** (`agents/hp-skill-reviewer`) | On request, or on agent PRs | Yes, on a different model | Advisory only; a person decides |
| **PR cap** (workflow) | Agent-authored PRs | No | More than 3 agent PRs in 7 days |
| **Drift report** (`scripts/drift_report.py`) | Weekly | No | Never fails; opens an issue with trends |

## The regression set

A fixed set of claims with known answers: confirmed errors (the panel should
catch them) and confirmed-true statements (the panel should keep them). Every
change to a skill reruns it. The score turns "is quality holding?" into a number.

- Public examples (`tests/regression/examples.yaml`) show the format only.
- The real cases are built from the private ledger and loaded through `HP_CASES`.
  They stay private because they mirror errors found on Library pages.
- Every new confirmed error can become a new case.

## Review fatigue

The biggest risk is not one bad skill; it is people approving agent pull
requests without reading them. Hence the cap, the requirement for a human
merge, and a curatorial review for quotes, images and family facts.
