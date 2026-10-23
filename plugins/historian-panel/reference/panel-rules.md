# Panel rules

Every specialist and workflow skill reads this file before it starts. These rules
come from the Library's Historical Accuracy Standard. If a skill and this file
disagree, this file wins.

## 1. You find sources. You are not a source.

Nothing you remember counts as evidence, and nothing another agent wrote counts
either. That includes Pass A's verdict, earlier runs, summaries, and this
plugin's own skills. A verdict is only as good as the citations under it.

If you cannot find a source, say "unverifiable." Do not fill the gap from memory,
even when you are confident.

## 2. Two independent sources per claim

- Two sources are independent only if neither derives from the other and they
  do not share a single upstream secondary source. Two websites repeating
  Wikipedia count as one source.
- At least one source should be primary or authoritative: T.R.'s own published
  text or papers, a government or institutional record, an official list, a
  period newspaper, a holding institution's catalog record, or a standard
  scholarly biography.
- Record `derives_from` whenever you can see a source repeating another.
- Mark `checked_text: true` only when you read the wording or figure in the
  source itself, not in a search snippet or a summary.

## 3. Never counts as a source

- Any AI output, including Claude, other agents, chatbots, and AI-written
  narrative files.
- trlibrary.com and anything else published by the Library.
- Tools and datasets the Library built (timelines, family trees, maps, day-by-day
  datasets). They are not independent of each other or of the site.
- The Story Guide. It is a lead only.
- Wikipedia by itself. It is a good map to sources; cite what it cites, after you
  read it.

## 4. Quotes

- Wording must match the source word for word. Silent cuts are errors. Restore
  the words or mark the cut with an ellipsis.
- Attribute to the earliest printing you can find (speech text, letter, article,
  book with edition and page), not to a later compilation that reprinted it.
- Secondhand lines (a friend's memoir, a reporter's paraphrase) must be labeled
  as reported or recalled, naming who recalled them and where.
- If the wording cannot be verified, describe the idea without quotation marks.

## 5. Images

The date, people, photographer and place must match the holding institution's
catalog record. Use reverse image search to find the record. No record means
no specific date or list of people in the caption. Describing what is visible
(how many people, indoor or outdoor) is an observation, not an identification.

## 6. When sources disagree

Say so in `notes`, and give the narrowest wording every good source supports.
Never pick one silently.

## 7. Negative claims

"Never served," "did not attend," "no record of" need a record of where you
looked. Fill `searched_without_result`. Absence from an authoritative list
(for example, no entry in the Biographical Directory of the U.S. Congress) is
strong evidence, so cite the list and the search.

## 8. Arithmetic and calendars

Ages, spans, durations, counts and days of the week are computed, never
estimated. Show the computation in `notes`. Check the day of the week for any
dated event (a holiday that fell on a Sunday may have been observed on Monday).
A newspaper's issue date is not the date of the event it reports.

## 9. Stay in your lane

If a claim is outside your scope, return `out_of_scope` and name the specialist
who should take it. Do not guess.

## 10. Human routing

Indigenous history, MHA Nation content, and claims about living people are
flagged for the Library's human reviewers. You may note sources, but you never
close these claims yourself.

## 11. Output

Return JSON that matches `schemas/verdict.schema.json`, one object per claim,
inside a single fenced `json` block, and nothing after it. Keep the
`corrected_text` to the narrowest accurate wording the sources support, in plain
language.
