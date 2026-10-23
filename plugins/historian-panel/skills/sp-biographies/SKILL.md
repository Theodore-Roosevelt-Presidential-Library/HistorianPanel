---
name: sp-biographies
description: "Specialist for claims that rest on, cite, or attribute something to a T.R. biography: Riis, Thayer, Bishop, Pringle, Putnam, Harbaugh, Morris, McCullough, Miller, Brands, Dalton, Cooper, Millard, Goodwin and others. Use when copy says 'according to his biographer', names a biography as its source, gives an edition or page, or repeats a vivid scene or line that most likely came from a biography. Checks what the book actually says, what the book relied on, and whether the edition and page are right."
---

# The major biographies

Read `reference/panel-rules.md` at the plugin root first.

## Scope

- Claims attributed to a named biographer or biography ("Morris writes",
  "as McCullough tells it").
- Scenes, dialogue and details in copy that trace back to a biography rather
  than to a primary record.
- Whether a biography is the right kind of source for the claim, and what
  that biography itself relied on.
- Edition, volume, chapter and page in a biography citation.

Biographies in scope include, as places to look (all secondary):

- Early and memorial-era lives: Jacob Riis, *Theodore Roosevelt the Citizen*
  (1904); William Roscoe Thayer, *Theodore Roosevelt: An Intimate Biography*
  (1919); Joseph Bucklin Bishop, *Theodore Roosevelt and His Time, Shown in His
  Own Letters* (1920).
- Mid-century: Henry F. Pringle, *Theodore Roosevelt* (1931); Carleton Putnam,
  *Theodore Roosevelt: The Formative Years* (1958); William Henry Harbaugh,
  *Power and Responsibility* (1961).
- Later lives: Edmund Morris, *The Rise of Theodore Roosevelt* (1979),
  *Theodore Rex* (2001), *Colonel Roosevelt* (2010); David McCullough,
  *Mornings on Horseback* (1981); John Milton Cooper, *The Warrior and the
  Priest* (1983); Nathan Miller, *Theodore Roosevelt: A Life* (1992); H. W.
  Brands, *T.R.: The Last Romantic* (1997); Kathleen Dalton, *Theodore
  Roosevelt: A Strenuous Life* (2002); Candice Millard, *The River of Doubt*
  (2005); Doris Kearns Goodwin, *The Bully Pulpit* (2013).

## Out of scope

- Whether a book exists, its exact title, publisher, year or ISBN →
  `sp-book-citations`
- How a biographer's view fits the wider change in scholarship ("historians now
  see") → `sp-historiography`
- Badlands and North Dakota books (Hagedorn, Di Silvestro, Jenkinson and
  others) → `sp-badlands-scholarship`
- Quoted words of T.R. or others → `sp-quote-verifier`
- Legends a biography repeats → `sp-myths` (also routed here)
- The underlying fact (a date, office, place) → the subject specialist, for
  example `sp-family-offices` or `sp-badlands`

## Where to look first

1. **The biography itself, read in the edition cited.** Full scans of
   public-domain lives (Riis, Thayer, Bishop) are at the Internet Archive
   (archive.org), HathiTrust (hathitrust.org) and Project Gutenberg
   (gutenberg.org). Later works: a library copy or a publisher preview. Good
   for what the book says; never treat the narrative as a primary record.
2. **The biography's own notes and bibliography.** Where a book gives notes,
   follow each one to the letter, diary or newspaper it names. Check each
   book for whether it has notes at all; early lives often do not.
3. **The primary record the note points to:** the Theodore Roosevelt Papers at
   the Library of Congress (loc.gov, Manuscript Division) and the Theodore
   Roosevelt Center digital library (theodorerooseveltcenter.org), which
   gathers scans from many holders.
4. **The edited letters:** Elting E. Morison and others, *The Letters of
   Theodore Roosevelt* (Harvard University Press, 1951 onward). Bishop's 1920
   volume prints letters too; check any letter against Morison or the
   manuscript, since edited collections can trim text.
5. **Houghton Library, Theodore Roosevelt Collection at Harvard**
   (guides.library.harvard.edu/roosevelt): research guide and finding aids;
   good for locating manuscripts a biographer quotes.
6. **Scholarly reviews of the biography** in journals on JSTOR (jstor.org),
   including the *Journal of the Gilded Age and Progressive Era*, and H-Net
   Reviews. Good for known errors and disputes; leads only.
7. **Library catalogs** (search.worldcat.org, catalog.loc.gov,
   openlibrary.org): to confirm which edition, and whether pagination changed
   between hardcover, paperback and e-book.

## Known traps

- A vivid scene or line repeated across popular copy comes from a biography,
  and the biography's own source is a memoir written long after. Follow the
  note; label the line as recalled and name who recalled it. [ref: D-18, F-11]
- A quotation is credited to the wrong biographer, or to a biographer who only
  quoted someone else. Name the person whose words they are and where the
  biographer found them. [method]
- Early lives written by contemporaries and admirers may give few sources.
  Check whether the book cites any; treat uncited details as testimony, not
  record. [method]
- Older letter collections can excerpt letters without marking cuts. Check the
  text against the modern edited letters or the manuscript before quoting.
  [method]
- Judge a biography on what its notes and sources support, not on its
  reputation. Report a scholar's view only from the published work, with
  edition and page; never write what an author "would" say. [method]
- A biographer's interpretation ("he was haunted by", "he never forgave") is
  turned into a fact in copy. Report it as that author's reading. [method]
- Page numbers cited from one edition are applied to another. E-book and
  paperback pagination often differs from the first edition. Give the edition
  you read. [method]
- An online text of a copyrighted biography found on an unauthorized site is
  cited as the source. Cite the published book and edition; never link a
  pirated copy. [method]
- Ages, years in office and spans given in a biography's narrative are copied
  without checking. Compute them yourself (panel rules section 8). [method]
- Two biographies agree only because the later one used the earlier. They are
  one source, not two (panel rules section 2). Record `derives_from`. [method]

## Procedure

1. Identify which biography the claim rests on. If copy does not say, search
   the distinctive wording or scene in the major lives above.
2. Read the passage in a named edition. Record edition, chapter and page.
3. Check whether the passage actually supports the claim as worded, including
   any hedging ("reportedly", "it was said") the copy dropped.
4. Follow the biography's note to its source and read that source. If there is
   no note, say so in `notes`.
5. Decide what kind of evidence the claim stands on: a contemporary record, a
   later memoir, or the biographer's interpretation. Label it in
   `corrected_text` if needed.
6. Find a second, independent source. A second biography that cites the first
   does not count.
7. Write the narrowest wording both sources support, crediting interpretation
   to its author.

## Output

Follow reference/panel-rules.md section 11.
