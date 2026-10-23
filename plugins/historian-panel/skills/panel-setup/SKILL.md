---
name: panel-setup
description: "Install, update, configure, check or repair HistorianPanel. Configures itself with no questions for the person. Use when someone asks to set up, install, update, refresh or troubleshoot the historian panel or its specialists, asks whether it is up to date, or when panel skills seem missing or stale. Also use to maintain the panel itself: adding or improving specialists and agents (hands off to propose-skill)."
---

# Panel setup, updates and health check

Read `reference/panel-rules.md` at the plugin root before running any review;
this skill itself does not review history.

The repository is
`https://github.com/Theodore-Roosevelt-Presidential-Library/HistorianPanel`.
The marketplace name is `trpl-historian` and the plugin is
`historian-panel@trpl-historian`.

## 1. Work out where you are running

- **Organization-managed.** If the plugin shows as `historian-panel@synced`, or
  the person says IT installed it, the organization keeps it installed and
  updated. Skip to section 4.
- **Claude Code** (a terminal, or a session where the `claude` command runs in
  the shell). Use section 2.
- **The Claude desktop app** (Cowork). Plugins are added through the app's
  menus, which you cannot click for the person. Use section 3.

## 2. Claude Code: install or update

Ask before changing anything: installing a plugin and changing settings are
configuration changes. With a yes:

```
claude plugin marketplace add Theodore-Roosevelt-Presidential-Library/HistorianPanel
claude plugin install historian-panel@trpl-historian
```

To update later:

```
claude plugin marketplace update trpl-historian
claude plugin update historian-panel@trpl-historian
```

Then tell the person to run `/reload-plugins` or start a new session.

**Automatic updates.** Offer to turn them on. With a yes, add this to the
person's user settings (`~/.claude/settings.json`), merging with what is there:

```json
{
  "extraKnownMarketplaces": {
    "trpl-historian": {
      "source": {"source": "github", "repo": "Theodore-Roosevelt-Presidential-Library/HistorianPanel"},
      "autoUpdate": true
    }
  }
}
```

They can also toggle it under `/plugin`, then Marketplaces.

## 3. Desktop app (Cowork): walk them through it

Give these steps one at a time and wait for each:

1. In the sidebar, open **Customize**, then **Plugins**.
2. Choose **Add marketplace** and paste
   `Theodore-Roosevelt-Presidential-Library/HistorianPanel`.
3. Choose **Browse plugins**, find **HistorianPanel**, and click **Install**.
4. Start a new conversation so the panel loads.

To update: **Customize**, then **Plugins**, find the `trpl-historian`
marketplace, and click **Update**.

If they do not see **Add marketplace**, their organization may manage plugins.
Suggest they ask IT to sync the repository for everyone (see `docs/admin-setup.md`
in the repository).

## 4. Configure and check, automatically

Do this without asking questions. Follow `references/auto-config.md` in this
skill's folder: find or create the config, detect each resource the person
has, fall back quietly to public sources for the rest, and ask in plain words
only when a specific task needs something. Many people won't have the book
corpus, self-hosted servers, the Library's working folder or a claude.ai
project, and the panel works fine for them.

Then check, silently:

1. **Skills present.** You can see `historian-panel:accuracy-review` and the
   active `sp-*` specialists in `roster.yaml`.
2. **Version.** The installed version or commit matches the latest on `main`.
   If not, give the update steps for this environment (section 2 or 3).
3. **Smoke test.** Run `accuracy-review` in `ask` mode on "Theodore Roosevelt
   was born in New York City." Two sources should come back.

**Report in one or two plain sentences**, for example: "HistorianPanel is set
up and working. Results will be saved in your historian-panel-ledger folder."
Mention a problem only if something is actually broken, and then say what you
will do about it or the one thing the person needs to do. Give the full detail
only if they ask.

## 5. Maintaining the panel itself

- Never edit the installed copy of the plugin. Updates overwrite it.
- To add a specialist, improve a skill, or change an agent, work in a clone of
  the repository and use `historian-panel:propose-skill`. Changes reach everyone
  through a reviewed pull request and the next update.
- To see what is planned, read the `planned` entries in `roster.yaml`.
