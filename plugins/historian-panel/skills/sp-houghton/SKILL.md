---
name: sp-houghton
description: "Use when a claim rests on material in Harvard's Theodore Roosevelt Collection at Houghton Library: manuscripts and family papers, photographs, cartoons, printed ephemera, or T.R.'s Harvard-era records. Takes claims citing 'Harvard College Library,' 'Houghton Library,' 'Theodore Roosevelt Collection,' a Houghton call number, a HOLLIS or HOLLIS Images record, or a photo credit to Harvard. Checks that the item exists, what its catalog record says, and how to cite it."
---

# Houghton Library, Theodore Roosevelt Collection

Read `reference/panel-rules.md` at the plugin root first.

## Scope

- Whether a manuscript, photograph, printed item or object cited to Harvard's
  Theodore Roosevelt Collection exists, and its catalog description.
- Call numbers, finding aids and record identifiers for that collection.
- What the catalog record says about date, creator, people and place.
- Material on T.R.'s Harvard years held in the collection or in the Harvard
  University Archives.
- How to cite Harvard items correctly.

## Out of scope

- Who is in a photograph and when it was taken, beyond reading the record →
  `sp-photo-id` (also routed here for Harvard-credited images)
- Exact quotation wording → `sp-quote-verifier`
- Letters held at the Library of Congress → `sp-loc-papers`
- Harvard-held items seen only through Theodore Roosevelt Center scans →
  `sp-tr-center` (also routed here)
- T.R.'s Harvard courtship and student life as narrative →
  `sp-harvard-alice-lee`

## Where to look first

1. **Theodore Roosevelt Collection overview**,
   https://library.harvard.edu/collections/theodore-roosevelt-collection .
   What the collection holds and how it is organized. Good orientation; not
   item-level.
2. **Research guide**, https://guides.library.harvard.edu/roosevelt . How to
   search the collection, reading-room rules, and related Harvard holdings.
3. **HOLLIS for Archival Discovery**, https://hollisarchives.lib.harvard.edu/ .
   Finding aids for manuscript collections, with folder-level listings and call
   numbers. Best for proving a letter or folder exists. Folder titles are
   cataloger summaries, not transcriptions.
4. **HOLLIS Images**, https://images.hollis.harvard.edu/ . Catalog records and
   images for photographs and graphic material. Best for photo credits; read
   the full record, including notes on date and attribution.
5. **HOLLIS**, https://hollis.harvard.edu/ . Library catalog for printed works
   and some manuscript records.
6. **Theodore Roosevelt Collection: Dictionary Catalogue and Shelflist**
   (Harvard University Library, published in print). A printed catalog of the
   collection as it then stood. Useful for older call numbers and items not yet
   in online records; it predates later acquisitions.
7. **Theodore Roosevelt Center digital library** holds scans of many Harvard
   items with Harvard credit lines. Use to find an item; cite Harvard's own
   record (see `sp-tr-center`).

## Known traps

- A photo credit "Harvard College Library" is used as if it identified the
  people, date or place. A credit says who holds the print; only the catalog
  record (and its notes) supports an identification. [method]
- Folder titles in finding aids summarize contents ("Letters to [recipient],
  [years]"). A folder title is not evidence that a specific letter or
  sentence is inside. Read the item or its image. [method]
- The collection holds copies, transcripts and photostats of documents whose
  originals are elsewhere. Check whether a Harvard item is an original or a
  copy before citing it as the source. [method]
- Photograph records may carry a date of printing, acquisition or publication
  rather than the date the photograph was taken. Read which date the record
  gives. [method]
- Many items are cataloged but not digitized. "Not online" is not "not held."
  Search the finding aid and catalog, and say if the item could not be viewed.
  [method]
- Cartoons and prints are dated by publication, not by the event they comment
  on. [method]
- Captions copied from a scan elsewhere may name Harvard as holder of an image
  that Harvard's catalog does not list. Confirm the record exists before using
  the credit. [method]

## Procedure

1. Identify the item claimed: type (letter, photograph, print, book), creator,
   date, and any call number or credit line.
2. Search HOLLIS for Archival Discovery for manuscripts, HOLLIS Images for
   photographs and graphics, and HOLLIS for printed works.
3. Open the full record. Note call number, creator, date as cataloged, and any
   notes on attribution, copies or uncertainty.
4. If an image is available, compare it with the claim (what is visible, any
   inscription). Pass identifications of people to `sp-photo-id`.
5. If the item cannot be found, check the printed *Dictionary Catalogue and
   Shelflist* and the research guide, and record each search in
   `searched_without_result`.
6. Cite as: item description, date, call number, Theodore Roosevelt
   Collection, Houghton Library, Harvard University, with the HOLLIS link.

## Output

Follow reference/panel-rules.md section 11.
