---
name: sp-government-records
description: "Use when a claim's best evidence is an official U.S. government record: executive orders and proclamations, messages to Congress, statutes and their dates, the Congressional Record and its predecessors, electoral vote tallies, diplomatic records (FRUS), chiefs-of-mission and officeholder lists, Bioguide entries, and National Archives holdings. Takes claims about what a law, order or message said, when it was signed or sent, official titles and ranks of posts, and election results."
---

# Government records

Read `reference/panel-rules.md` at the plugin root first.

## Scope

- Executive orders, proclamations and messages: number, date, and what they
  say.
- Statutes and joint resolutions: date approved, chapter and Statutes at Large
  citation, and text.
- Proceedings of Congress: the Congressional Record and earlier debates,
  committee documents, and the Serial Set.
- Election returns and electoral votes.
- Diplomatic posts and correspondence: Foreign Relations of the United States,
  chiefs of mission, and the titles of posts (minister versus ambassador).
- Federal service records and the holdings of the National Archives.

## Out of scope

- Who held an office and in what order → `sp-officeholder-sequences` (also
  routed here for official lists)
- Conservation acreage and land orders as totals → `sp-conservation` (also
  routed here for the underlying orders)
- Family members' offices and ranks → `sp-family-offices`
- Exact wording of a message quoted in copy → `sp-quote-verifier`
- Indigenous treaties and policy → the Library's human reviewers

## Where to look first

1. **GovInfo**, https://www.govinfo.gov/ : the bound Congressional Record
   (https://www.govinfo.gov/app/collection/crecb), the Statutes at Large
   (https://www.govinfo.gov/app/collection/statute) and the Serial Set
   (https://www.govinfo.gov/app/collection/serialset). Official page images.
   Coverage of older volumes varies; check the volume exists before concluding
   absence.
2. **Library of Congress, United States Statutes at Large**,
   https://www.loc.gov/collections/united-states-statutes-at-large/ . Scans of
   historical volumes. Use for laws of the T.R. era.
3. **American Presidency Project**, https://www.presidency.ucsb.edu/ :
   messages, proclamations, executive orders
   (https://www.presidency.ucsb.edu/documents/app-categories/written-presidential-orders/presidential/executive-orders)
   and election statistics. Good transcriptions with dates; a secondary
   compilation, so confirm key wording against a printed government source.
4. **Office of the Historian, U.S. Department of State**,
   https://history.state.gov/ : FRUS volumes
   (https://history.state.gov/historicaldocuments) and chiefs of mission by
   country (https://history.state.gov/departmenthistory/people/chiefsofmission).
   Authoritative for diplomatic titles and dates.
5. **Biographical Directory of the U.S. Congress**,
   https://bioguide.congress.gov/ . The standard record of who served in
   Congress. Absence is strong evidence for a negative claim (panel rule 7).
6. **National Archives**, https://www.archives.gov/ and its catalog
   https://catalog.archives.gov/ ; Electoral College results
   (https://www.archives.gov/electoral-college); executive orders disposition
   tables (https://www.archives.gov/federal-register/executive-orders) for
   numbered orders. Check which years the disposition tables cover before
   relying on them for early orders.
7. **Congress.gov**, https://www.congress.gov/congressional-record , for the
   Record's current pages and its guides. The early-twentieth-century Record is
   on GovInfo and in print.
8. **Printed indexes of executive orders**: the Historical Records Survey's
   *List and Index of Presidential Executive Orders: Unnumbered Series,
   1789-1941*, and the State Department's numbered-series lists. Check any
   order number and date against the order text itself.

## Known traps

- Electoral and popular vote figures are copied correctly while the prose
  description of which states or regions a candidate carried is wrong. Check
  the state-by-state table, including split electoral votes. [ref: G-02]
- "Won with a substantial majority" or similar is used where the source gives a
  plurality, or where the electoral and popular margins differ. Use the
  official tallies and the word they support. [ref: F-13]
- Diplomatic titles changed over time; a post's rank (legation or embassy)
  and its head's title (minister or ambassador) get applied to the wrong
  year. Check the chiefs-of-mission list for the title in that year. [ref: G-15, E-07]
- Officeholders' start dates are moved to fit a narrative (tenure dated from
  the second president they served, not from appointment). Use the official
  list's dates. [ref: G-18, G-19, F-20]
- The filing date of a lawsuit, the date of a decision and the date of an
  announcement are confused. Find the docket, case report or official notice
  that fixes each. [ref: G-08]
- A bill's passage, signature and effective date are different dates. State
  which you mean and cite the Statutes at Large chapter. [method]
- Order numbers assigned after the fact are treated as if printed on the
  original, and proclamations or letters are called executive orders. Cite the
  document type and number the official source uses. [method]
- The Congressional Record's daily edition and bound edition paginate
  differently, and remarks may be revised before printing. Cite the edition you
  read. [method]
- Messages to Congress were printed in several government and commercial
  editions with small differences. Prefer the government printing for wording.
  [method]

## Procedure

1. Classify the record type the claim depends on: order, proclamation,
   statute, message, debate, election return, diplomatic record, service record.
2. Find the official printing (GovInfo, Statutes at Large, FRUS, National
   Archives) and read the page image.
3. Cross-check against a second, independent record or list (for example the
   American Presidency Project against the Statutes at Large, or FRUS against
   the chiefs-of-mission list).
4. Pin each date to its meaning (signed, approved, filed, decided, effective)
   and check the day of the week.
5. For negative claims, cite the authoritative list searched and fill
   `searched_without_result`.
6. Cite with volume, page or chapter, date, and URL.

## Output

Follow reference/panel-rules.md section 11.
