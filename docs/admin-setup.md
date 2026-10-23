# Admin setup: give the panel to everyone automatically

Most staff should never have to install anything. On a Claude Team or Enterprise
plan, an organization owner can sync this repository once and mark the plugin
required. It then installs itself for every member, in the desktop app and in
Claude Code (as `historian-panel@synced`), and stays in sync with `main`.

## Requirement: the repository must be private or internal

Organization sync works only with private or internal GitHub repositories. This
repository is currently public. Choose one:

| Option | Effect |
|--------|--------|
| **Make it private** (recommended) | Org sync and required install work. The private regression cases and a private denylist can then live in the repository too. The Labs site can still describe the panel. |
| **Keep it public, add a private mirror** | Sync the private mirror for staff; publish the public copy for other institutions. Two repositories to keep in step. |
| **Keep it public only** | Staff install it themselves with the one prompt in INSTALL.md. No forced install or org-wide updates. |

## Steps (once the repository is private or internal)

1. On claude.ai, open **Organization settings**, then **Plugins & skills**.
2. Choose **Add**, then **Sync from GitHub**, and pick
   `Theodore-Roosevelt-Presidential-Library/HistorianPanel`.
3. Leave **Sync automatically** on.
4. Set **Default access** to everyone who writes or edits content.
5. Mark **historian-panel** as **required**, so it installs for everyone and
   cannot be removed.

Members then see it under **Customize**, then **Plugins**.

## Optional: make the panel run without being asked

The plugin's skill descriptions already make Claude reach for it when someone
asks to check or write history. To make it a standing rule, add this to the
organization's or project's instructions:

> Before any historical claim about Theodore Roosevelt, his family, his era or
> his places appears in something published under the Library's name, run
> `historian-panel:accuracy-review` on it. Treat your own drafts as leads, not
> sources.

## Claude Code fleets

For managed Claude Code installs, the same marketplace can be pushed through
managed settings (`extraKnownMarketplaces` with `autoUpdate: true`, and
`enabledPlugins` with `"historian-panel@trpl-historian": true`).
