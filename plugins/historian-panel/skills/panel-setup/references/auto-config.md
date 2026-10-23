# Automatic configuration

Most people who use the panel are not technical. Configure it for them. Never
ask someone to edit a file, name a server, find a path or join a network.

## Principles

1. **Detect, don't ask.** Look for each resource yourself (table below). Use
   what you find.
2. **Everything optional is optional.** The panel works on public sources
   alone. Many people will not have the book corpus, self-hosted search
   servers, the Library's internal files, a TRPL folder or a claude.ai
   project. That is normal, not an error. Do not mention what they lack unless
   it matters to the task in front of you.
3. **Ask only when the task needs it, and in plain words.** If a specific
   check would be clearly better with a resource you could not find (below,
   "When to ask"), ask once, in one sentence, with an easy way to say no:
   "Do you have the Library's quote archive? If not, no problem: I'll check
   the quote against his published writings." Never mention YAML, MCP,
   Qdrant, servers, VPNs, environment variables or file paths unless the
   person used those words first.
4. **Remember the answer.** If they say no or don't know, add the key to
   `not_available` in the config, if one exists, so you never ask again. If
   they provide the resource later, use it and remove the key.
5. **Report in one or two plain sentences.** Say what works, not what is
   missing. Example: "You're set. Results will be saved in the
   historian-panel-ledger folder." Only someone who asks gets the full list.

## Where the config lives

Look in this order and use the first one you find:

1. `$HP_CONFIG`
2. `historian-panel.config.yaml` in the current working folder
3. `historian-panel.config.yaml` at the top of any folder the person has
   connected to this session (on the desktop app, the folders listed by the
   device tools)

If none exists:

- **A folder is connected:** create `historian-panel.config.yaml` at the top
  of the folder where their work lives. If several are connected, prefer one
  that already has a `historian-panel-ledger` folder, then the one that holds
  the Library's working files, then the first one. Do not ask which.
- **No folder is connected:** create nothing. Use the defaults for this
  session and return results in the conversation (and as files sent to the
  person). Mention connecting a folder only if the work truly needs saving,
  such as a scheduled check or a monitor run.

Relative paths in the config resolve against the folder that holds the config.
That keeps one config working when the same folder is mounted under different
names.

The config is private. Never copy it, or anything it points to, into the
public repository.

## Resources

| Key | Used by | How to find it | If missing | When to ask |
|-----|---------|----------------|------------|-------------|
| `ledger_dir` | every review | an existing `historian-panel-ledger` folder; otherwise create `historian-panel-ledger` beside the config | results stay in the conversation | never; create it |
| `quote_archive_path` | sp-quote-finder, sp-quote-verifier | a file named like `TR-Quotes-TRC-Archive.json` (or .csv), usually in a `Quotes` folder | primary texts and the Theodore Roosevelt Center's public site | the first time someone asks for or about a T.R. quote |
| `verified_quotes_path` | sp-quote-verifier | a spreadsheet or export whose rows carry the tier labels in `verified_quote_tiers` | primary texts only | the first time a quote will be published, if `quote_archive_path` was also missing |
| `tra_chronology_path` | sp-tra, sp-on-this-day | a `source-pdfs` folder beside a Day by Day chronology, or files named like `Chronological Record` | the TRA's public chronology and other dated sources | never; the public route is good enough |
| `author_index_path` | sp-biographies, sp-scholarly-perspectives, scholarly-debate | `hp_author_index/author_index.json` | library catalogs and published bibliographies | never |
| `corpora.books_mcp` | specialists that read biographies | a tool in this session whose name or description mentions the Library's book corpus or `trpl_books` (test it with a one-word search) | public full text (HathiTrust, Internet Archive, Google Books previews) | only for a question that turns on what a modern biography says, and only if the person is the one who hosts it; otherwise silently use public sources |
| `corpora.archive_mcp` | sp-loc-papers, sp-tr-center | a tool whose name or description mentions the Roosevelt archive transcripts | Library of Congress and Theodore Roosevelt Center public sites | never |

Self-hosted resources (a search server running on someone's own machine or
home network) are often unreachable from other people's sessions, and from the
owner's own session when they are away from home. Treat "can't reach it
today" like "doesn't have it": fall back quietly. Don't record it in
`not_available`, because it may work next time.

## Steps

1. Find or decide the config location (above).
2. For each key, check the config. If the key is empty and not listed in
   `not_available`, try to detect it. Test any tool with a tiny query.
3. Write what you found to the config (create it if a folder is connected).
   Keep any value already set by hand.
4. Run the smoke test in the setup skill.
5. Report in one or two plain sentences.
