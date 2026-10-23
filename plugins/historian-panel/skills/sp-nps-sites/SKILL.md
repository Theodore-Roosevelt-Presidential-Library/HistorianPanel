---
name: sp-nps-sites
description: "Use when a claim cites, or concerns the records of, a National Park Service unit tied to T.R.: Sagamore Hill NHS, Theodore Roosevelt Birthplace NHS, Theodore Roosevelt Inaugural NHS, Theodore Roosevelt National Park, Theodore Roosevelt Island, or the NPS museum collections, historic resource studies, administrative histories, NPS 'people' pages and the NPS History Collection. Takes claims sourced to nps.gov, and claims about the houses, rooms, objects and history of these sites."
---

# National Park Service sites and records

Read `reference/panel-rules.md` at the plugin root first.

## Scope

- Claims sourced to nps.gov pages for the T.R. units and to NPS "people"
  pages about T.R.'s family and circle.
- The history, buildings, rooms and furnishings of Sagamore Hill, the
  Birthplace, the Wilcox House (Inaugural site), the Theodore Roosevelt National
  Park cabins and ranch sites, and Theodore Roosevelt Island.
- NPS museum catalog records for objects at these sites.
- NPS historic resource studies, historic structure reports, furnishings
  reports and administrative histories.

## Out of scope

- T.R.'s Badlands years as events → `sp-badlands` (also routed here for
  Theodore Roosevelt National Park)
- Acreage, monuments and conservation figures → `sp-conservation`
- Family offices and life events → `sp-family-offices`
- Who is in an NPS photograph → `sp-photo-id`
- Objects as artifacts beyond the catalog record → `sp-objects`
- Indigenous history of park lands → the Library's human reviewers

## Where to look first

1. **The unit's own pages**: Sagamore Hill (https://www.nps.gov/sahi/),
   Theodore Roosevelt Birthplace (https://www.nps.gov/thrb/), Theodore
   Roosevelt Inaugural (https://www.nps.gov/thri/), Theodore Roosevelt National
   Park (https://www.nps.gov/thro/), Theodore Roosevelt Island
   (https://www.nps.gov/this/). Interpretive pages: good for orientation,
   uneven in sourcing, and rarely cite.
2. **NPS History Collection**, https://npshistory.com/ . Scans of historic
   resource studies, structure and furnishings reports, administrative
   histories and older park publications. These usually carry footnotes; follow
   them to primary records.
3. **NPS museum collections web catalog**, https://museum.nps.gov/ , and
   Sagamore Hill's collections page
   (https://www.nps.gov/sahi/learn/historyculture/collections.htm). Object
   records with catalog numbers. Descriptions can be brief.
4. **NPS DataStore (IRMA)**, https://irma.nps.gov/DataStore/ , for reports and
   studies not on npshistory.com.
5. **NPGallery**, https://npgallery.nps.gov/ , for NPS images and National
   Register nomination files, which contain sourced site histories.
6. **The documents NPS pages rest on**: T.R.'s own books and letters
   (`sp-published-works`, `sp-loc-papers`), period newspapers
   (`sp-period-newspapers`).

## Known traps

- Spans and ages are computed loosely from birth and death dates on NPS
  people pages ("two years older"). Compute the span from the exact dates and
  show the arithmetic. [ref: C-22]
- Interpretive pages give rounded figures (acres, counts) that copy then
  restates as exact or as a superlative. Trace a figure to its documented
  source and keep the rounding the source uses. [ref: D-13, D-14]
- Different NPS pages date the end of a ranch or property by different
  milestones (operations wound down, house abandoned, land sold). Say which
  milestone you mean. [ref: E-20]
- An NPS page's place name is moved across a territorial or state line in
  copy (Dakota versus Montana). Keep the place the page and the primary record
  give. [ref: D-25]
- Rooms and furnishings shown today are often restorations or reconstructions
  based on furnishings reports. "The desk where he wrote" may be a period
  piece or a reproduction. Check the catalog record or furnishings report.
  [method]
- Some buildings at these sites are reconstructed, moved or heavily
  restored. Before calling a building or room original, check the NPS historic
  structure report or National Register file. [method]
- NPS pages are revised without notice. Record the URL and the date you read
  it, and prefer a dated study over an undated web page. [method]
- An NPS page and a website that copies it are one source. [method]

## Procedure

1. Identify the site, building, room, object or person the claim concerns.
2. Read the unit's page, then look for a historic resource study, structure
   report, furnishings report or administrative history on npshistory.com or
   DataStore.
3. For objects, find the museum catalog record and note its catalog number and
   whether the item is original, period or reproduction.
4. Follow the study's footnotes to primary records and read at least one.
5. Compute any span, age or count yourself and show it in `notes`.
6. Cite the dated NPS study or catalog record in preference to an undated web
   page; give the URL and access date for web pages.

## Output

Follow reference/panel-rules.md section 11.
