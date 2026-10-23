# HistorianPanel: instructions for Claude

You are working with HistorianPanel, the Theodore Roosevelt Presidential
Library's panel of historical-accuracy specialists. This file tells you what the
panel is, when to use it, how to install and update it, and how to maintain it.
It applies in Claude Code, in the Claude desktop app (Cowork), and in any
session that has this repository open.

## What the panel is

A Claude plugin (`plugins/historian-panel`) with:

- **Specialist skills** (`skills/sp-*`): each knows where to look and what
  usually goes wrong for one slice of T.R.'s world. They find sources; they are
  never sources themselves.
- **Workflow skills**: `accuracy-review` (the coordinator), `claim-extractor`,
  `blind-reverify`, `source-independence`, `error-sweep`, `propose-skill`,
  `panel-setup`.
- **Agents** (`agents/hp-*`): thin wrappers that run a skill in its own context.
  That isolation is what keeps the second check blind.
- **`roster.yaml`**: every specialist, active or planned, with routing rules.
- **`reference/panel-rules.md`**: the rules every specialist follows.

## When to use it

Use `historian-panel:accuracy-review` **every time** any of these is true:

- You are drafting or editing something that carries a historical claim under
  the Library's name: web copy, captions, alt text, social posts, newsletters,
  press releases, scripts, exhibit text, quizzes, decks, grant or donor
  materials, datasets.
- Someone asks whether a T.R. fact, date, quote or image identification is
  right.
- Someone asks to review, audit or improve existing historical content.

Run it **before** the copy is shown as final, not after. If you drafted the copy
yourself, your draft is a lead, not a source; the panel checks it like anyone
else's.

You do not need the person to name the panel. "Is this right?", "check this
caption," "write a post about the Elkhorn Ranch" are all reasons to run it.

## Who is on the panel

`ROSTER.md` introduces every member in plain language. It is generated from
`roster.yaml`; after changing the roster, run `python scripts/build_roster_md.py`.

## Lenses and debates never impersonate scholars

`review-lenses` applies question sets from schools of scholarship, and
`scholarly-debate` argues documented positions from cited published work.
Neither ever speaks as, or for, a real historian. What a scholar actually wrote
comes from `sp-scholarly-perspectives`, with edition and page.

## How the work flows to the right agents

1. **Trigger.** A request matches the `accuracy-review` description (above), or
   another skill (for example a social-post skill) calls it as a step.
2. **Extract.** The coordinator has `hp-claim-extractor` list every checkable
   claim.
3. **Route.** The coordinator reads `roster.yaml` and sends each claim to up to
   three active specialists, matching claim type and keywords. Quotes always go
   to `sp-quote-verifier`, images to `sp-photo-id`, superlatives to
   `sp-superlatives`.
4. **Pass A.** One `hp-specialist` agent per specialist batch, in parallel.
5. **Pass B.** An `hp-blind-verifier` agent per claim, given only the claim,
   never Pass A's results.
6. **Audit.** `hp-independence-auditor` checks that the sources are independent.
7. **Resolve and write.** Agreement closes a claim; disagreement gets a blind
   Pass C; anything still open is hedged or cut. Results go to the ledger folder
   as `ledger.jsonl` and `report.md`.

Roster gaps (claims no specialist fits) are listed in the report. Repeated gaps
are the signal to build a planned specialist.

## Commands people use

| They say | You run |
|----------|---------|
| "Check this," "is this accurate," "review this page" | `/historian-panel:accuracy-review review <text or URL>` |
| "When did T.R. ...?", any one question | `/historian-panel:accuracy-review ask <question>` |
| "Where else does this error appear?" | `/historian-panel:error-sweep <wrong> -> <right>` |
| "How would scholars see this?" "Is this framed fairly?" | `/historian-panel:review-lenses <text or URL>` |
| "What do the biographers say about X?" | `/historian-panel:accuracy-review ask` (routes to `sp-scholarly-perspectives`) |
| "How should we frame X?" on a contested subject | `/historian-panel:scholarly-debate <question>` |
| "Get this ready for a historian to review" | `/historian-panel:scholar-review-packet <piece>` |
| "Check house style" | `/historian-panel:style-check <text>` |
| "Set up," "update," "is it working?" | `/historian-panel:panel-setup` |
| "Add a specialist," "teach the panel," "update the skills" | `/historian-panel:propose-skill <what and why>` |

## Installing and updating

See `INSTALL.md`. In short:

- **Organization-managed** (preferred): IT syncs this repository for everyone
  and marks the plugin required. It installs and updates itself. See
  `docs/admin-setup.md`.
- **Desktop app**: Customize, then Plugins, then Add marketplace, then
  `Theodore-Roosevelt-Presidential-Library/HistorianPanel`, then install
  HistorianPanel. You cannot click these menus; walk the person through them.
- **Claude Code**: `claude plugin marketplace add
  Theodore-Roosevelt-Presidential-Library/HistorianPanel`, then `claude plugin
  install historian-panel@trpl-historian`. Ask before running them.

The plugin has no pinned version on purpose, so every merged commit is a new
version (the validator's "no version" warning is expected).
Updates arrive through the marketplace's update or auto-update.

## Maintaining the panel (you are allowed and expected to do this)

You may propose new specialists, improve skills and agents, fix broken source
links, and add traps learned from confirmed errors. Do it through
`propose-skill`:

1. Work in a clone of this repository on a branch named
   `agent/<short-name>-<yyyymmdd>`.
2. Follow `plugins/historian-panel/reference/skill-standard.md`.
3. Run the checks (below) until they pass.
4. Open a pull request labeled `agent-authored`, using the template.

Hard limits, which exist to protect accuracy:

- Never push to `main`, merge, or approve a pull request. A person merges.
- No more than 3 agent-authored pull requests in any 7 days. Overflow goes to
  `proposals/backlog.md`.
- Skills hold pointers and traps, never facts used as sources.
- Every trap cites a ledger ID listed in `provenance/claim-ids.txt`, or is
  tagged `[method]` or `[house-rule]`.
- Never edit an installed copy of the plugin; edit the repository.

## This repository is public

Never commit:

- text from licensed biographies or licensed collections (cite them only)
- claim ledger contents, fix lists, or descriptions of errors on Library pages
- internal hostnames, private IP addresses, staff file paths, credentials
- staff names or contact details (use roles)
- real config files (`historian-panel.config.yaml` is git-ignored)

The private regression cases and the ledger live outside this repository and are
reached through environment variables (`HP_CASES`, `HP_LEDGER`).

## Checks

Use a virtual environment:

```
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements-dev.txt
python scripts/lint_skills.py
python scripts/check_provenance.py
python scripts/build_roster_md.py --check
python -m unittest discover -s tests
claude plugin validate .
```

The regression test set (`scripts/run_regression.py`) needs an API key and runs
in CI on pull requests that touch skills or agents.

## Map

```
.claude-plugin/marketplace.json     marketplace "trpl-historian"
plugins/historian-panel/
  .claude-plugin/plugin.json        plugin "historian-panel"
  roster.yaml                       every specialist, active and planned
  reference/panel-rules.md          rules for every specialist
  reference/skill-standard.md       what a skill must look like
  schemas/                          claim and verdict JSON schemas
  skills/                           workflow and specialist skills
  agents/                           isolated agent wrappers
  config.example.yaml               copy to historian-panel.config.yaml
provenance/claim-ids.txt            ledger IDs skills may cite (IDs only)
scripts/                            lint, provenance, regression, red team, drift
tests/                              unit tests and public example cases
docs/                               architecture, admin setup, quality layer
INSTALL.md                          what staff (and Claude) follow to install
ROSTER.md                           friendly guide to every panel member (generated)
llms.txt                            index of this repository for language models
```
