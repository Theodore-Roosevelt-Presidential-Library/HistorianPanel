# HistorianPanel

A team of AI specialists that checks Theodore Roosevelt history before it
carries the Library's name, and reviews existing content to make it better.

> **Claude:** start with [CLAUDE.md](CLAUDE.md). To install for someone, follow
> [INSTALL.md](INSTALL.md).

## Get it

Paste this into Claude:

> Set up HistorianPanel for me. Follow the instructions at
> https://github.com/Theodore-Roosevelt-Presidential-Library/HistorianPanel/blob/main/INSTALL.md
> and walk me through anything I need to click.

In Claude Code you can also install it directly:

```
/plugin install historian-panel --marketplace Theodore-Roosevelt-Presidential-Library/HistorianPanel
```

## Use it

Just ask, in plain words:

- "Is this caption right?" (paste the caption or the image link)
- "Review trlibrary.com/tr/... for accuracy."
- "When did T.R. first come to Dakota?"
- "Where else does this error appear?"

You get back each claim marked keep, fix, hedge or cut, with sources and
corrected wording.

## How it works

1. **Extract.** The copy is broken into individual checkable claims.
2. **Route.** Each claim goes to the specialists who know where to look for that
   kind of fact (quotes, family offices, photographs, the Badlands years, and so
   on).
3. **Check twice.** One specialist verifies it. A second checks it again from
   scratch without seeing the first answer.
4. **Audit the sources.** Two websites copying the same source count as one.
5. **Resolve.** Agreement closes the claim. Disagreement gets a third check.
   Anything still uncertain is hedged or cut.

The specialists are source-finders and skeptics. They never answer from memory,
and nothing an AI writes counts as a source. The rules are in
[panel-rules.md](plugins/historian-panel/reference/panel-rules.md).

## The panel

78 members, all active. [ROSTER.md](ROSTER.md) introduces each one.

- **Periods of T.R.'s life**, from his 1858 birth to his death in 1919.
- **Family and circle**: Edith, Alice, the children, the Badlands partners, friends and rivals.
- **Themes**: conservation, military, foreign and domestic policy, natural history, health, sports, and the hard chapters.
- **Collections**: the Library of Congress, Houghton, the TR Center, NPS, government records, newspapers, T.R.'s texts, museum specimens.
- **Scholarship**: the biographies, Badlands scholarship, how views have changed, myths, book citations, and what historians actually wrote.
- **Era and media**: Gilded Age New York, the open range, Progressive politics, everyday life; photographs, film, maps, objects, sites, namesakes, commemoration and the press.
- **Workflow roles**: the coordinator, the blind re-checker, the source auditor, the error sweeper, house style, **scholarly lenses**, **scholarly debates** between documented positions from different eras, and **review packets** for real historians.

## Keeping it good

Specialists can propose new skills, but only as pull requests a person merges.
Every pull request is linted, checked for provenance, and scored against a test
set of known errors and known-true claims. A weekly report tracks the scores.
See [docs/quality-layer.md](docs/quality-layer.md) and
[CONTRIBUTING.md](CONTRIBUTING.md).

## License

Code and skills: MIT. The panel cites licensed and archival collections; it does
not reproduce them.
