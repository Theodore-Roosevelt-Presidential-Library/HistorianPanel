---
name: sp-loc-papers
description: "Use when a claim rests on a letter, diary, speech draft, telegram, scrapbook or other manuscript in the Library of Congress Theodore Roosevelt Papers, or in related Library of Congress family papers (Kermit and Belle Roosevelt, Archibald Roosevelt, Theodore Roosevelt Jr., Alice Roosevelt Longworth). Takes claims of the form 'T.R. wrote to X on date Y,' 'his diary records,' 'in a letter he said,' and any citation to the Manuscript Division, the microfilm edition, or loc.gov item pages. Checks that the document exists, who wrote it to whom, its date, and what it actually says."
---

# Library of Congress Theodore Roosevelt Papers

Read `reference/panel-rules.md` at the plugin root first.

## Scope

- Whether a cited letter, diary entry, telegram, speech draft or memorandum
  exists in the Library of Congress Theodore Roosevelt Papers, and where.
- Writer, recipient, date and place of a manuscript, and what its text says.
- Related family collections in the Manuscript Division: the Kermit and Belle
  Roosevelt Papers, Archibald Roosevelt Papers, Theodore Roosevelt Jr. Papers,
  Alice Roosevelt Longworth Papers, and papers of close associates when a claim
  cites them.
- How to cite a document in these papers (collection, series, container or
  reel, date, loc.gov item link).

## Out of scope

- Exact wording of a quotation for publication → `sp-quote-verifier` (this
  specialist confirms the document and its date; both may be routed)
- Photographs and prints from the Prints and Photographs Division →
  `sp-photo-id`
- Documents seen only through the Theodore Roosevelt Center's scans and
  summaries → `sp-tr-center` (also routed here when the TRC item is an LOC
  document)
- Offices, ranks and careers of family members → `sp-family-offices`
- Printed versions of speeches and books → `sp-published-works`
- Claims about living people → the Library's human reviewers

## Where to look first

1. **Theodore Roosevelt Papers digital collection**,
   https://www.loc.gov/collections/theodore-roosevelt-papers/ . Item-level
   images of the papers, browsable by series. Best for seeing the document
   itself. Limit: images were largely scanned from microfilm, and search
   depends on item titles and dates supplied by catalogers, not full text.
2. **Collection finding aid**, https://findingaids.loc.gov/repositories/19/resources/3731
   (portal: https://findingaids.loc.gov/). Explains the series (incoming
   letters, outgoing letterpress copies, speeches and writings, diaries,
   scrapbooks, family papers, later additions) and their date ranges. Read it
   before concluding a document is missing.
3. **"About this Collection" and "Related Resources"** pages on the digital
   collection site. The related-resources page links catalog records for the
   family and associate collections (Kermit and Belle Roosevelt, Archibald
   Roosevelt, Theodore Roosevelt Jr., Alice Roosevelt Longworth, and others).
4. **Library of Congress catalog**, https://catalog.loc.gov/ , for collection
   records and finding aids of the related family papers. Many of these are
   not digitized; the record tells you what exists and where.
5. **The printed index to the microfilm edition** (Library of Congress
   Presidential Papers Index Series, Theodore Roosevelt volume). Name-and-date
   index to correspondence. Good for proving a letter exists; it does not give
   content.
6. **Edited transcriptions**: Elting E. Morison, ed., *The Letters of Theodore
   Roosevelt* (Harvard University Press, 1951-1954), and family compilations
   such as *Letters to Kermit from Theodore Roosevelt* (1946). Secondary to the
   manuscript; use to locate a letter, then read the image.
7. **Theodore Roosevelt Center digital library** mirrors many LOC items with
   added summaries. Useful finding tool only; cite the LOC original (see
   `sp-tr-center`).

## Known traps

- Two versions of the same sentiment exist (a speech and a later letter, or a
  draft and a sent copy) and copy blends them into one quotation with one date.
  Identify which document you are citing and quote only that one.
  [ref: D-26]
- A letter is cited by recipient and month but no such item can be found in the
  correspondence series or the index. Search the series and the index by name
  and date range, record where you looked, and return `unverifiable` rather
  than accepting a quote site's citation. [ref: F-08]
- The text of a speech in the papers (a reading copy or stenographic report)
  differs from later printed versions. Say which version you read; do not merge
  wording from two. [ref: E-05]
- Letterpress copybook pages are T.R.'s retained copies of outgoing letters.
  They show the text sent but not that it was received, and faint copies are
  often misread by catalogers and transcribers. Read the image. [method]
- Item dates on loc.gov come from catalogers. Undated items carry inferred
  dates, often in brackets or as a range. Do not present an inferred date as
  the date written on the document. [method]
- Incoming letters are filed under T.R.'s papers but were written by others.
  A letter "in the Roosevelt Papers" is not necessarily a letter by Roosevelt.
  Check writer and recipient on the image. [method]
- Secretaries wrote and signed routine replies, especially during the
  presidency. A signature or initials by a secretary is not T.R.'s own wording.
  [method]
- Morison's edition is selective and sometimes abridges. Absence from Morison
  is not absence from the papers, and Morison's text may omit passages.
  [method]
- Diaries record the day of writing, which can trail the event. Check the
  entry's own date and any back-dated notes. [method]

## Procedure

1. Write down exactly what the claim says the document is: writer, recipient,
   date, place, and the words or fact it is said to contain.
2. Read the finding aid to identify which series should hold it (incoming,
   outgoing, speeches, diaries, family papers) and its date range.
3. Search the digital collection by name and date; if not found, check the
   printed index and the edited *Letters*, then the related family collections.
4. Open the image and read the document itself. Confirm writer, recipient,
   date as written (not as cataloged), and the relevant passage.
5. If the claim depends on exact wording, pass the passage and citation to
   `sp-quote-verifier`.
6. For any "no such letter" result, fill `searched_without_result` with each
   series, index and edition searched.
7. Cite as: document description, date, Theodore Roosevelt Papers (or the
   family collection), Manuscript Division, Library of Congress, with the
   loc.gov item link.

## Output

Follow reference/panel-rules.md section 11.
