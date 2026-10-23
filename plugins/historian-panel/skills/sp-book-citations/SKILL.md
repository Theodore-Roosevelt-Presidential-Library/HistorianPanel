---
name: sp-book-citations
description: "Specialist for any book citation in copy, reading lists, footnotes, captions or recommended-reading blocks: exact title and subtitle, author name and spelling, co-authors, publisher, first-publication year versus reprint year, edition, and ISBN-10 or ISBN-13 validity. Also confirms that a cited book exists at all. Use whenever copy names a book, gives an ISBN, or says 'recommended reading' or 'further reading'."
---

# Book citations

Read `reference/panel-rules.md` at the plugin root first.

## Scope

- Title and subtitle, word for word.
- Author names and spelling, including co-authors and editors.
- Publisher and place for the edition cited.
- Year of first publication versus the year of the edition in hand.
- ISBN-10 and ISBN-13: valid check digit, and whether the number belongs to
  this book.
- Whether a cited book exists. A plausible title, author and year can be
  invented.

## Out of scope

- What a biography says or relies on → `sp-biographies`
- Badlands and North Dakota books' reliability → `sp-badlands-scholarship`
- T.R.'s own books, their editions and texts → `sp-published-works` and
  `sp-author`
- Quotations from a book → `sp-quote-verifier`
- Whether a book is a good choice for a reading list: note it, but leave the
  decision to the Library's human reviewers

## Where to look first

1. **WorldCat** (search.worldcat.org): union catalog of libraries worldwide.
   Best for confirming a book exists, its exact title and its editions. Records
   can merge editions; open the specific record.
2. **Library of Congress Online Catalog** (catalog.loc.gov): authoritative
   bibliographic records for U.S. books, with name authority headings
   (id.loc.gov) for author spelling.
3. **Open Library** (openlibrary.org): free records with ISBN lookup at
   openlibrary.org/isbn/ followed by the number. Community-edited; confirm in
   WorldCat or the Library of Congress.
4. **The publisher's own catalog page** for the edition, title, subtitle and
   ISBN. Pages change and can drop older editions.
5. **The book itself:** the title page and copyright page, in hand or in a
   scan (Internet Archive, archive.org; HathiTrust, hathitrust.org; Google
   Books, books.google.com). The copyright page gives first-publication and
   reprint history.
6. **Reviews at publication** (journals on JSTOR, jstor.org; trade reviews)
   to confirm the original year and publisher. Secondary.

## Known traps

- An invented title is paired with a real author, or a real title with the
  wrong author. Confirm the pairing in a catalog record, not a search snippet.
  [ref: A-06, F-12]
- Author names are misspelled in a way that looks right. Match the catalog's
  name heading letter by letter. [ref: A-08]
- The subtitle is paraphrased or swapped with a similar book's. Copy it from
  the title page or catalog. [ref: F-29]
- A reprint or later edition year replaces the first-publication year. Say
  which year you give. [ref: F-21]
- An ISBN belongs to a different book, a different edition, or does not exist.
  Look the number up; do not trust it because the check digit passes.
  [ref: F-06, G-21]
- A title, author or ISBN is assembled from fragments of different real books.
  Every element must come from one record. [ref: F-30]
- ISBN-10 check digit: multiply the first nine digits by 10 down to 2, add,
  and the check digit makes the total divisible by 11 (X stands for 10).
  ISBN-13: weight the first twelve digits 1, 3, 1, 3 and so on, and the check
  digit brings the total to a multiple of 10. Compute it and show the work in
  `notes`. [method]
- Books published before ISBNs existed are given one. An ISBN on an old book
  belongs to a modern reprint; cite it only as that reprint. [method]
- Hyphens and spaces in an ISBN are cosmetic, but a 978 prefix does not turn
  an ISBN-10 into an ISBN-13 without recomputing the check digit. [method]
- AI-generated reading lists are a known source of plausible but nonexistent
  books. Treat every unverified title as unconfirmed. [house-rule]

## Procedure

1. Copy the citation exactly as it appears: title, subtitle, author, publisher,
   year, ISBN.
2. If there is an ISBN, compute its check digit and show the arithmetic in
   `notes`.
3. Look up the ISBN in Open Library and WorldCat. Confirm it points to this
   title, author and edition.
4. Search WorldCat and the Library of Congress catalog by title and by author.
   Confirm the book exists and copy the exact title, subtitle and name
   heading.
5. Find the first-publication year and publisher, and the year of any edition
   cited.
6. Confirm with a second, independent record (publisher page, title-page
   scan, or review at publication).
7. If no record exists anywhere, the verdict is `contradicted` or
   `unverifiable`; list every catalog searched in `searched_without_result`.
8. Give the corrected full citation in `corrected_text`.

## Output

Follow reference/panel-rules.md section 11.
