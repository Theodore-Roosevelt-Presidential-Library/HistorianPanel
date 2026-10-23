---
name: propose-skill
description: Create or improve a HistorianPanel skill or agent through a pull request. Use when a review shows a roster gap, a confirmed error reveals a trap no skill covers, someone asks to "add a specialist," "teach the panel," "update the skills," or a planned roster entry should be built. Never edits the main branch directly.
argument-hint: "<new specialist name from roster.yaml, or the skill to improve and why>"
---

# Propose a skill

Read `reference/panel-rules.md` and `reference/skill-standard.md` at the plugin
root first. The skill standard is the contract; the linter enforces it.

## When to use

- A planned entry in `roster.yaml` should become active.
- The coordinator reported the same roster gap more than once.
- A confirmed ledger error shows a pattern no skill's `## Known traps` covers.
- A source a skill points to has moved, closed or changed its terms.
- An agent file needs a change (tools, model, instructions).

## Guardrails

- **Pull requests only.** Work on a branch named `agent/<short-name>-<yyyymmdd>`.
  Never push to `main`, never merge, never approve your own pull request.
- **Label** every pull request `agent-authored`.
- **Weekly cap.** Before opening one, count open or recent pull requests with that
  label from the last 7 days (`gh pr list --label agent-authored --state all
  --search "created:>=<date>"`). If there are already 3, do not open another.
  Add the proposal to `proposals/backlog.md` instead and say so.
- **Pointers and traps, never facts.** See the skill standard. A trap needs a
  ledger ID that is listed in `provenance/claim-ids.txt`, or the `[method]` or
  `[house-rule]` tag.
- **Nothing private.** The repository is public: no licensed text, no internal
  hosts or paths, no ledger contents, no staff names.
- **One change per pull request.** One new specialist, or one improvement.

## Procedure

1. Check `roster.yaml` and the existing skills for overlap. If a skill already
   covers the scope, improve it instead of adding a new one.
2. For a new specialist, copy the section layout from an active specialist (for
   example `skills/sp-badlands/SKILL.md`) and write:
   - Scope and out-of-scope hand-offs that do not overlap other specialists.
   - "Where to look first": real, named repositories, catalogs, official lists
     and standard texts, in order, each with what it is good and bad for. Visit
     each URL you list to confirm it works.
   - Known traps from confirmed ledger patterns and method cautions.
   - Procedure and Output sections.
3. Update `roster.yaml`: set `status: active` and add `routes`.
4. If a trap cites a ledger ID that is not yet in `provenance/claim-ids.txt`,
   add the ID with its status (only `confirmed` or `closed` IDs qualify). Never
   add the claim's text.
5. Run the checks and fix anything they report:
   ```
   python3 -m venv .venv && source .venv/bin/activate
   pip install -r requirements-dev.txt
   python scripts/lint_skills.py
   python scripts/check_provenance.py
   python -m unittest discover -s tests
   ```
6. If you can run the regression test set (it needs an API key, and the private
   cases if you have them), run `python scripts/run_regression.py` and include
   the scores in the pull request.
7. Commit, push the branch, and open the pull request with the repository's
   template filled in: what changed, why (ledger IDs or roster gap), what the
   checks reported, and what a human reviewer should look at first.

## Output

The pull request link and a two-line summary. If the cap stopped you, the
backlog entry instead.
