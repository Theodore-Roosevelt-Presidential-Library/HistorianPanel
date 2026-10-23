---
name: sp-myths
description: "Specialist for myths, legends and misattributions about T.R.: apocryphal stories, teddy bear story variants, fake or misattributed quotes, 'first president to' legends, things he supposedly coined or invented, the San Juan Hill and round-robin myths, deathbed and 'famous last words' lines, and anecdotes that sound too good. Use when copy repeats a well-known story, a quote-poster line, a 'first' or 'coined', or a 'legend has it'. Checks the Library's misquotes and fake-quotes pages first; those pages are not sources."
---

# Myths, legends and misattributions

Read `reference/panel-rules.md` at the plugin root first.

## Scope

- Well-known stories about T.R. whose details drift in retelling: the 1902
  Mississippi bear hunt and the origin of the teddy bear, the Rough Riders'
  charge, the round-robin letter of 1898, bar-fight and cowboy tales, and
  family anecdotes.
- Quotes and quips attributed to T.R. or to people about him that have no
  traceable printing.
- "First", "coined" and "invented" legends.
- Hedges in copy that are themselves wrong ("may be apocryphal" when the line
  is documented, or "he said" when it is only reported).

## Out of scope

- Exact wording of a genuine quote → `sp-quote-verifier` (also routed here)
- Firsts and records as claims of fact → `sp-superlatives` (also routed here)
- The military facts of 1898 → `sp-navy-rough-riders`
- How the myth fits shifts in reputation → `sp-historiography`
- Myths about Indigenous people or history → flag for the Library's human
  reviewers (panel rules section 10)

## Where to look first

1. **Check-first pages:** the Library's misquotes and fake-quotes pages (URLs
   under `check_first` in the config). A match means stop and flag. They are
   not sources and cannot close a claim.
2. **The earliest printing.** Search period newspapers in the original pages
   (Chronicling America, chroniclingamerica.loc.gov; Library of Congress
   Theodore Roosevelt Papers, loc.gov; Theodore Roosevelt Center digital
   library, theodorerooseveltcenter.org). A story or quote that first appears
   decades later is suspect.
3. **T.R.'s own account** where one exists (*The Rough Riders*, *An
   Autobiography*, his letters), full text at Project Gutenberg
   (gutenberg.org) and the Internet Archive (archive.org). His telling is a
   source for what he said, not proof of every detail.
4. **Holding institutions and agency history pages** for object and event
   legends, for example the NPS Theodore Roosevelt Birthplace page on teddy
   bear history (nps.gov/thri/forkids/teddybearhistory.htm) and the Smithsonian
   National Museum of American History (americanhistory.si.edu). Read their
   sources too.
5. **Word-history references** for "coined" claims: the Oxford English
   Dictionary (oed.com, subscription) for earliest recorded uses.
6. **Quote-tracing references:** Quote Investigator (quoteinvestigator.com)
   and Wikiquote's misattributed sections (en.wikiquote.org/wiki/Theodore_Roosevelt).
   Leads only; follow their citations to the printed source.

## Known traps

- The teddy bear story is told with the wrong animal, wrong circumstances or
  wrong participants. Read a contemporary account and the holding
  institution's history, not a retelling. [ref: D-10]
- Well-known quips appear in someone's memoir long after the fact and are
  presented as things T.R. said. Label them as recalled and name the
  rememberer and the printing. [ref: C-14, D-18, F-11]
- Copy adds a hedge ("may be apocryphal", "widely circulated at the time")
  that the sources do not support. Hedges need evidence too. [ref: A-32]
- A famous line about T.R.'s death is attributed to the wrong speaker or
  occasion. Find the earliest printing before attributing. [ref: D-08]
- "He coined" is claimed for words that were in print before him. Check the
  earliest recorded use. [ref: D-15]
- "First president to" legends that ignore an earlier president, or that blur
  "while in office" and "as a former president". [ref: D-11, E-09]
- A naming honor is inflated: a smaller feature is turned into a famous one.
  Check the official name and what was actually renamed. [ref: D-02, D-04]
- The charge is placed on "San Juan Hill" in prose. Use Kettle Hill or the San
  Juan Heights. [house-rule]
- A line found only on posters, quote sites or social media is attributed to
  T.R. No traceable printing means no quotation marks. [method]
- The Library's own lists, Story Guide and tools are treated as proof that a
  story is true. They are leads only. [house-rule]

## Procedure

1. Check the misquotes and fake-quotes pages. If the claim matches, flag it and
   stop.
2. Break the story into its parts: who, what, where, when, and any quoted
   words.
3. Find the earliest account of each part. Note its date relative to the
   event and who wrote it.
4. Compare later versions to the earliest. Mark details that were added.
5. For quotes, hand the wording check to `sp-quote-verifier`; record here only
   whether a period printing exists.
6. Decide: documented, reported (secondhand, name the source), or no evidence
   found. Record where you looked in `searched_without_result`.
7. Write the narrowest wording the earliest sources support.

## Output

Follow reference/panel-rules.md section 11.
