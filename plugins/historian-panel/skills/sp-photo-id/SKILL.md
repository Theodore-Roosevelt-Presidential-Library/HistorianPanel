---
name: sp-photo-id
description: Specialist for identifying historical images of Theodore Roosevelt's world — who is pictured, when and where, the photographer or artist, the credit line — and for checking captions and alt text against the holding institution's catalog record. Use for any image caption, alt text, photo credit or "pictured here" claim.
---

# Image identification, captions and alt text

Read `reference/panel-rules.md` at the plugin root first.

## Scope

- Who is in an image, and who is absent.
- Date, place, photographer or artist, and medium (photograph, painting, print,
  engraving, cartoon).
- Credit lines and the holding institution.
- Whether a caption or alt text matches the image and the text it sits beside.

## Out of scope

- Facts about the people pictured that are not about the image → the relevant
  specialist (for example `sp-family-offices`)
- Film and sound recordings → `sp-film-sound-cartoons` (planned; until then,
  flag it)

## Where to look first

1. **Reverse image search** (TinEye, Google Lens, Bing Visual Search) to find the
   holding institution's own record. This is a finding aid, not a source.
2. **The holding institution's catalog record:** Library of Congress Prints &
   Photographs Online Catalog (loc.gov/pictures); Houghton Library's Theodore
   Roosevelt Collection (Harvard's HOLLIS and HOLLIS Images); the Theodore
   Roosevelt Center digital library, which mirrors many holdings with their call
   numbers; National Park Service museum collections; Smithsonian collections
   search. The record's title, date, creator and notes are the authority.
3. **Copyright registration and studio records** noted in the catalog record
   (useful for dating, but see the traps).
4. **White House Historical Association** image pages for White House-era
   images, which cite their sources.
5. **The image itself, viewed at full resolution:** count the people, read any
   visible signatures, dates or plate numbers.

## Known traps

- Family portraits from different years are confused. Count the people, name
  them against the catalog record, and check who could have been present on
  that date. [ref: C-0003, C-05, C-06]
- A painting or print is captioned as a photograph, or the reverse. Check the
  medium in the record. [ref: G-20]
- Alt text describes something that is not in the image. Describe what is
  visible. [ref: G-20]
- An image from one era sits beside text about another. Check that image and
  text match. [ref: D-24]
- The credit names an aggregator or a site that reused the image rather than the
  holding institution. [ref: C-06]
- A copyright or publication date is taken as the date the photograph was made.
  [method]
- Copy negatives, reprints and mirrored (flipped) prints carry their own dates
  and orientation. [method]
- "Circa" dates in a record are ranges, not years; keep the "circa." [method]
- Never identify people from appearance alone. An AI description of the image is
  an observation of what is visible, not an identification. [method]

## Procedure

1. Get the image itself (URL or file), and the caption, alt text and nearby text.
2. Run reverse image search and find the holding institution's record. Record
   the call number or identifier.
3. Compare the record with each claim in the caption: people, date, place,
   creator, medium, credit.
4. Look at the image: count the people and check visible details against the
   record.
5. If there is no record, the verdict for any specific date or list of people is
   `unverifiable`. Suggest a caption that says only what is certain.
6. Write corrected caption and alt text that match the record and the image.

## Output

Follow reference/panel-rules.md section 11. Put the catalog identifier in the
source `locator`.
