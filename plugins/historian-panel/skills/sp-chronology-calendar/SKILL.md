---
name: sp-chronology-calendar
description: "Specialist for any claim that depends on calendar arithmetic or ordering in time: ages at an event, age gaps, spans and durations, \"X years later\", counts of days or years, day of the week, holiday observance dates, newspaper issue date versus event date, dispatch dates and time zones, before/after ordering, and place names that changed between the event and today. Use alongside the subject specialist whenever a claim contains a computed number of years, months or days, a weekday, or a then-and-now place name."
---

# Chronology and calendar arithmetic

Read `reference/panel-rules.md` at the plugin root first, especially section 8.

## Scope

- Ages: at an event, at death, the gap between two people's ages, "in his
  twenties," "at fifty."
- Spans and durations: terms of office, length of a trip, "X years later,"
  "within two years," "barely a year," counts of days.
- Day of the week for any dated event, and whether a holiday was observed on
  its calendar date or on another day.
- Issue date versus event date for newspapers, and dispatch date versus print
  date for wire stories and telegrams.
- Ordering: whether A really came before B, and whether an item in a list
  existed yet at the date described.
- Place names that changed after the event (a city or country renamed, a
  territory that became a state), and whether copy should use the period name,
  the modern name or both.

## Out of scope

- Whether the underlying dates themselves are right. This specialist does the
  arithmetic on dates the subject specialist has sourced; it does not source
  birth, death or event dates on its own. Route those to the period or family
  specialist (`sp-badlands`, `sp-governor-vp`, `sp-first-term`,
  `sp-second-term`, `sp-africa-europe-bull-moose`, `sp-last-years`,
  `sp-family-offices`).
- Rankings that use the arithmetic ("youngest," "longest") → `sp-superlatives`
- Who held an office in what order → `sp-officeholder-sequences`
- Map boundaries and historic place identification beyond the name change →
  `sp-maps-places` (planned; flag as a roster gap until active)

## Where to look first

1. **Python's standard library** for the arithmetic itself: the `datetime`
   module (https://docs.python.org/3/library/datetime.html) for differences
   between dates and `weekday()`, and the `calendar` module
   (https://docs.python.org/3/library/calendar.html) for month grids and leap
   years. Both use the proleptic Gregorian calendar, which is correct for all
   U.S. dates in T.R.'s lifetime.
2. **A perpetual calendar** such as timeanddate.com's calendar pages
   (https://www.timeanddate.com/calendar/) as an independent check on the day
   of the week. Use it as a second method, not a source for the event.
3. **The sourced dates themselves,** as cited by the subject specialist: birth
   and death records, official lists, catalog records. Write each input date
   and its citation into `notes` before computing.
4. **Newspaper page images** through Chronicling America
   (https://chroniclingamerica.loc.gov/): the masthead gives the issue date;
   the dateline and the text ("yesterday," "on Saturday last") give the event
   date. Read both.
5. **Holiday observance:** the federal statutes that created or moved a holiday
   (Statutes at Large on govinfo, https://www.govinfo.gov/app/collection/statute)
   and period newspapers from the place in question. OPM's federal holidays
   page (https://www.opm.gov/policy-data-oversight/pay-leave/federal-holidays/)
   describes the modern rules only; do not apply them backward.
6. **Place names:** the U.S. Geological Survey's Geographic Names Information
   System (https://www.usgs.gov/tools/geographic-names-information-system-gnis)
   for U.S. names and their variants; for foreign places, the national
   gazetteer or an official government source. Period maps and newspapers show
   the name in use at the time.

## Known traps

- A newspaper's issue date is used as the date of the event it reports, or a
  weekly's date is used for something that happened days earlier. Read the
  dateline and the text. [ref: E-15, E-16]
- An event on a holiday is dated to the holiday when the holiday fell on a
  Sunday and was observed on Monday, or the reverse. Check the weekday, then
  check how that year's observance was reported locally. [ref: E-14]
- Ages are computed by subtracting years without checking whether the birthday
  had passed, giving an answer one year off. Compute from full dates.
  [ref: D-23, A-13, A-14]
- Age gaps between two people are computed from birth years alone, or one of
  the birth dates is wrong. Use both full birth dates and state the gap in
  years and months if it straddles a whole number. [ref: C-03, C-22]
- Spans between two events ("in thirty-five years," "two years after") are
  rounded or counted from the wrong endpoint (election instead of inauguration,
  announcement instead of signing). Name both endpoints. [ref: C-23]
- Chains of "two years later" are used to compress a career, and the steps do
  not add up to the real dates. Compute each step separately. [method]
- Inclusive and exclusive counting are mixed (counting both the first and last
  day, or neither). Say which convention you used. [method]
- A city, country or territory is given its modern name for a period when it
  had another (or the period name is "corrected" to the modern one in a quote).
  Use the period name in historical narration, add the modern name in brackets
  if helpful, and never change it inside a quotation. [method]
- Wire stories and telegrams carry a dispatch date and city that differ from the
  date the paper printed them; time zones and overseas cables can shift the
  date by a day. Record both. [method]
- A weekday printed in a secondary source is copied without being checked.
  Compute it. [method]

## Procedure

1. List every input date the claim depends on, with its citation from the
   subject specialist. If an input date is unsourced, stop and route it.
2. Name the endpoints for any span (which event starts it, which ends it) and
   the counting convention.
3. Compute with Python `datetime` (or by hand, shown step by step) and check the
   result with a second method, such as a perpetual calendar for weekdays.
4. For holidays, check the weekday and how observance was reported that year in
   that place.
5. For newspaper and telegram dates, record issue date, dispatch date and event
   date separately.
6. For place names, record the name in use at the event date and the modern
   name, with sources for both.
7. Put the full computation in `notes`, including the inputs, and give the
   narrowest wording the arithmetic supports (for example "at 42" only if the
   birthday had passed).

## Output

Follow reference/panel-rules.md section 11. The computation shown in `notes`
is required for every verdict this specialist returns.
