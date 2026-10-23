---
name: sp-tr-center
description: "Use when a claim cites, or was likely drawn from, the Theodore Roosevelt Center at Dickinson State University: its digital library item pages, record numbers, item summaries, subject pages, quote pages, timelines, or the Theodore Roosevelt Encyclopedia. Takes claims whose only stated source is 'Theodore Roosevelt Center' or theodorerooseveltcenter.org, and checks them against the underlying document and its holding institution (Library of Congress, Harvard, Sagamore Hill and others)."
---

# Theodore Roosevelt Center digital library

Read `reference/panel-rules.md` at the plugin root first.

## Scope

- Claims sourced to the Theodore Roosevelt Center's digital library, item
  summaries, subject pages, quote pages, timelines or encyclopedia.
- Tracing a Center item to its holding institution and original document.
- Checking the Center's cataloged dates, writers, recipients and summaries
  against the document image.
- How to cite a document found through the Center.

## Out of scope

- Exact quotation wording → `sp-quote-verifier`
- The Library of Congress original once identified → `sp-loc-papers`
- The Harvard original once identified → `sp-houghton`
- Who is in an image → `sp-photo-id`
- Badlands chronology drawn from the Center's timeline → `sp-badlands` (also
  routed here)
- Indigenous history and claims about living people → the Library's human
  reviewers

## Where to look first

1. **The document image on the Center's item page**,
   https://www.theodorerooseveltcenter.org/digital-library/ . Read the scan
   itself, not the summary beside it. Each item page names a holding
   institution (for example the Library of Congress Manuscript Division,
   Harvard, Sagamore Hill) and a record number.
2. **The holding institution's own record**: the Library of Congress
   Theodore Roosevelt Papers (https://www.loc.gov/collections/theodore-roosevelt-papers/),
   HOLLIS for Archival Discovery (https://hollisarchives.lib.harvard.edu/), or
   the NPS museum catalog (https://museum.nps.gov/). Cite this, not the mirror.
3. **The Center's encyclopedia**,
   https://www.theodorerooseveltcenter.org/encyclopedia/ . Short secondary
   essays, often by named scholars. A map to sources; it is secondary and
   counts as one source at most.
4. **Center timelines and subject pages.** Useful leads for dates and names.
   Secondary compilations; check every date against the documents they rest
   on.
5. **Printed primary texts** for items that are publications (pamphlets,
   speeches, articles): see `sp-published-works` for the first printing.

## Known traps

- The Center holds a later reprint pamphlet, and copy dates a passage to the
  pamphlet's year and title instead of the original address. Find the first
  printing and date the words to the occasion they were spoken or written.
  [ref: H-06, H-07]
- Center quote pages attribute a line to a specific letter or date that cannot
  be found in the documents. A quote page is not a document; find the letter
  itself or return `unverifiable`. [ref: F-08]
- Center timeline entries compress or misstate events (a date of sale, a train
  passing through, a stop that was made or not). Treat each entry as a lead and
  confirm it in a contemporary record. [ref: E-15, E-16]
- A Center item's text of a speech differs from other printed versions. Say
  which text you read and do not combine wording. [ref: E-05]
- Item summaries are cataloger paraphrases. They can misname writer or
  recipient, misread a date, or describe content the page does not contain.
  Read the image. [method]
- The Center's item date may be the date of a copy, a reprint, a clipping or an
  estimate, not the date the document was created. Check what the document
  itself says. [method]
- Center items and the holding institution's record are one source, not two.
  A Center scan of an LOC letter plus the LOC page for that letter is a single
  source under panel rule 2. [method]
- Encyclopedia essays and Center timelines repeat each other and secondary
  biographies. Record `derives_from` when one repeats another. [method]
- The Library's own pages, tools and datasets built from Center material are
  not independent sources. [house-rule]

## Procedure

1. Find the Center item, page or entry the claim came from, and note its record
   number and holding institution.
2. Open the document image and read it. Compare writer, recipient, date as
   written, and the relevant passage with both the claim and the Center's
   summary.
3. Go to the holding institution's record for the same item and confirm it
   there; cite that record.
4. If the claim came from a timeline, encyclopedia or quote page, find the
   primary document it rests on. If none can be found, say so and record the
   searches.
5. For publications, hand the passage to `sp-published-works` or
   `sp-quote-verifier` to find the first printing.
6. Write the narrowest correction the document supports, and note any error in
   the Center's summary in `notes`.

## Output

Follow reference/panel-rules.md section 11.
