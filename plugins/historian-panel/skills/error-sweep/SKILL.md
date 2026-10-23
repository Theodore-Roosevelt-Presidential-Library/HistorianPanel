---
name: error-sweep
description: After a historical error about Theodore Roosevelt is confirmed, find every other place the same error appears and trace where it came from. Use when a correction has been closed in the ledger and needs fixing everywhere, or when someone asks "where else does this appear?"
argument-hint: "<the wrong statement> -> <the correction> [ledger ID]"
---

# Error sweep

Read `reference/panel-rules.md` at the plugin root first.

## Scope

One confirmed error at a time: the wrong wording, the corrected wording, and the
ledger ID. Do not sweep for an error that is not closed in the ledger.

## Where to look

Ask the person which of these you can reach, then search every one you can:

1. The website: site search, plus a crawl for variants (captions, alt text,
   link text, meta descriptions, quiz answers).
2. The Library's Labs tools and their datasets, and their source repositories.
3. Social post archives and the newsletter archive.
4. Internal drafting notes and knowledge bases.
5. AI knowledge files and narrative files that feed chat assistants (a common
   root cause, since they reseed errors).
6. Digital asset management metadata for images.

## Procedure

1. Build search variants: the exact wrong phrase, paraphrases, the wrong number
   or date alone, and the wrong name or title alone.
2. Search each place. Record every hit with location and the surrounding text.
3. For each hit, say whether it is the same error, a related error, or a false
   match.
4. Identify the likely root cause: the earliest source of the wrong wording you
   can find (a knowledge file, an old draft, a widely copied web page).
5. Do not change anything. Produce the list for the content owner.

## Output

`sweep.md` in the ledger folder: a table of hits (location, current text, same
or related, suggested replacement), the root cause, and the places you could not
reach. Report the counts in one line.
