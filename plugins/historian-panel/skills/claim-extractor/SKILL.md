---
name: claim-extractor
description: Break historical copy about Theodore Roosevelt into atomic, checkable claims as JSON. Use as the first step of an accuracy review, or whenever a page, caption, script, dataset or draft needs its factual claims listed before verification.
---

# Claim extractor

Read `reference/panel-rules.md` at the plugin root first.

## Scope

Any text the Library might publish: web pages (body, headings, captions, alt
text, meta descriptions, link text, reading lists), scripts, social posts,
exhibit text, quizzes (questions, answers and explanations), and dataset rows.

## What counts as a claim

Anything a reader could check:

- a quote (keep the exact wording, including punctuation)
- a date, number, name or place
- an office held, a rank, or a life event
- a sequence ("before," "after," "succeeded," "then")
- a superlative ("first," "only," "youngest," "more than any")
- who or what is in an image, and when and where it was taken
- a book citation (title, author, year, ISBN)
- an anecdote told as fact
- a cause ("because," "made possible," "led to"), which is also a sequence claim

Skip opinions, calls to action, and operational facts (hours, prices, events).

## Procedure

1. If given a URL, fetch the page and include headings, captions, alt text, and
   the meta description, not just body text.
2. Split compound sentences. "He married Edith in London in 1886 at a small
   church" is three claims: the date, the city, the church.
3. Write each claim as one declarative sentence that keeps the original
   wording. Put the original sentence in `context`.
4. Set `type` from the claim schema. When a claim fits two types, pick the
   riskier one (quote over date, superlative over number).
5. Set `risk: high` for quotes, superlatives, image IDs, family facts, and
   anything on /tr pages, exhibits, quizzes, press releases or datasets.
6. Give every claim an ID `R-<yyyymmdd>-<nnnn>` in reading order.
7. Note internal contradictions (a caption that disagrees with the body) as
   separate claims, both kept.

## Output

A single fenced `json` block holding an array of objects matching
`schemas/claim.schema.json`, and nothing after it. Do not verify anything.
