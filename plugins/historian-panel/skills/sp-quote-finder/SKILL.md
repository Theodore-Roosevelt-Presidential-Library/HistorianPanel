---
name: sp-quote-finder
description: "Find real Theodore Roosevelt quotations on a subject for posts, speeches, captions, decks and exhibits — only lines located word for word in a primary text or in the verified tiers of the Library's quote list, each with its full citation and surrounding context. Use for 'give me a T.R. quote about X,' 'what did he say about Y,' or 'is there a better quote for this.' Never offers a quote from memory."
---

# Quote finder

Read `reference/panel-rules.md` at the plugin root first, especially section 4.

## Scope

- Finding quotations by T.R. on a subject, for a use (social post, speech,
  caption, exhibit panel, deck).
- Suggesting a stronger or shorter real alternative to a quote someone already
  has.
- Finding the original passage for a fragment someone half-remembers.

## Out of scope

- Checking a quote already in copy → `sp-quote-verifier`
- Quotes by other people about T.R. → `sp-quote-verifier` (which also handles
  attributions)
- Famous lines that may be fake → `sp-myths`

## Where to look first

1. **The Library's verified-quotes list**, if the config gives its path
   (`verified_quotes_path`). Use only the verified tiers, and still open the
   primary text each entry cites.
2. **The Library's quote archive export** of Theodore Roosevelt Center records,
   if the config names it (`quote_archive_path`). Each record points to a digital-library item; read
   the item.
3. **T.R.'s own texts in the book corpus**, if the config names the corpus tool:
   search only works whose author is T.R. (the author index marks them). For
   exact wording, a keyword search of the corpus text beats a semantic search.
4. **Primary printings in public scans:** Project Gutenberg, the Internet
   Archive and HathiTrust for his books, speeches and collected addresses; the
   American Presidency Project for presidential messages and remarks; the
   Theodore Roosevelt Center digital library for letters and speech texts.
5. **Check-first lists:** the Library's misquotes and fake-quotes pages, to rule
   out lines that only sound like him.

## Known traps

- Quote sites and social media circulate lines T.R. never wrote. A line found
  only on quote sites is not a candidate. [method]
- A real passage is trimmed until it says something he did not mean. Read the
  paragraph around it and say if the trimmed line changes the sense. [method]
- Words are dropped from the middle without an ellipsis. Give the passage as
  printed, or mark the cut. [ref: H-04, H-05, E-05]
- The cited source is a later compilation, not the original speech or book.
  Cite the earliest printing you can find. [ref: H-06, H-07]
- A line someone else recalled him saying is offered as his own words. Say who
  recalled it and where, or leave it out. [ref: D-18, F-11, F-31]
- Period language that reads badly today is quoted without context. Flag it for
  the person to decide. [method]
- A quote from a speech is given the wrong date or venue because a reprint was
  dated differently. [ref: H-03]

## Procedure

1. Pin down the subject, the use, and the length wanted (one line for social,
   a paragraph for a speech).
2. Search the sources in order. Collect at least three candidates when they
   exist.
3. For each candidate, read the surrounding paragraph and note the context in
   one line.
4. Copy the text exactly as printed, with spelling and punctuation, and mark any
   cut with an ellipsis.
5. Record the citation: title, date, venue or recipient, edition and page or
   chapter.
6. Rank candidates by fit for the use, then by strength of source.
7. Hand every candidate you recommend to `sp-quote-verifier` for a blind check
   before anyone uses it.

## Output

Follow reference/panel-rules.md section 11. Use one verdict per candidate with
`claim_id` set to the request ID plus a candidate number, `verdict: supported`
only for wording read in a primary printing, the exact text in
`corrected_text`, and the context line in `notes`.
