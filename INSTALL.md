# Installing HistorianPanel

## For staff: the one prompt

Open Claude (the desktop app or Claude Code) and paste:

> Set up HistorianPanel for me. Follow the instructions at
> https://github.com/Theodore-Roosevelt-Presidential-Library/HistorianPanel/blob/main/INSTALL.md
> and walk me through anything I need to click.

Claude will check whether the panel is already installed, install or update it,
and run a quick test. In the desktop app it will ask you to click through three
menus; it cannot click them for you.

If your organization already manages it, there is nothing to do: the panel
appears on its own and updates itself.

After setup, just ask Claude to check things: "Is this caption right?", "Review
this page for accuracy," "When did T.R. first come to Dakota?"

---

## For Claude: how to carry out the prompt above

Do these in order. Tell the person in one line what you are about to do, then do
it. Ask before installing anything or changing settings.

### Step 1. Is it already here?

If your available skills include `historian-panel:accuracy-review`, the panel is
installed. Skip to Step 4.

If the plugin is listed as `historian-panel@synced`, the organization manages
it. Skip to Step 4.

### Step 2. Which app is this?

- If you can run `claude --version` in a shell, you are in **Claude Code**. Go
  to Step 3a.
- Otherwise you are in the **Claude desktop app**. Go to Step 3b.

### Step 3a. Claude Code

With the person's go-ahead, install in one step (Claude Code 2.1.275 or later),
inside the session:

```
/plugin install historian-panel --marketplace Theodore-Roosevelt-Presidential-Library/HistorianPanel
```

Or from the shell:

```
claude plugin marketplace add Theodore-Roosevelt-Presidential-Library/HistorianPanel
claude plugin install historian-panel@trpl-historian
```

Offer to turn on automatic updates. With a yes, merge this into
`~/.claude/settings.json` (keep everything already there):

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

Ask them to run `/reload-plugins` (or start a new session), then go to Step 4.

### Step 3b. Claude desktop app

Plugins are added through the app's menus. Give these steps one at a time and
wait for the person to confirm each:

1. In the left sidebar, open **Customize**, then **Plugins**.
2. Choose **Add marketplace** and paste:
   `Theodore-Roosevelt-Presidential-Library/HistorianPanel`
3. Choose **Browse plugins**, find **HistorianPanel**, and click **Install**.
4. Start a new conversation and paste the setup prompt again, so you can finish
   with Step 4.

If they do not see **Add marketplace**, their organization manages plugins.
Suggest they ask IT to follow `docs/admin-setup.md`.

### Step 4. Finish with the health check

Run `historian-panel:panel-setup` and follow its health check (section 4). Report
the results in a few lines, and tell the person the three things they can now
ask for: check copy, answer a history question, and find where an error repeats.

## Updating

- Organization-managed: automatic.
- Desktop app: **Customize**, then **Plugins**, find the `trpl-historian`
  marketplace, and click **Update**.
- Claude Code: `claude plugin marketplace update trpl-historian`, then
  `/reload-plugins`. Or turn on auto-update as above.

Or just ask Claude: "Update HistorianPanel."
