---
name: sp-pronunciation
description: "Specialist for how to say the names in T.R.'s story, for audio tours, video narration, podcasts, AI voices and docent scripts: family names (including how T.R. said 'Roosevelt'), people (the Marquis de Morès, Sewall), places (Medora, Mingusville, Kristiania), Indigenous names and words, and period terms. Produces a sourced pronunciation guide. Use before recording or generating any narration."
---

# Pronunciation guide

Read `reference/panel-rules.md` at the plugin root first.

## Scope

- Personal names in T.R.'s life and circle, including his own family name.
- Place names, historic and current, including names that changed.
- Period terms and foreign words in scripts.
- Indigenous names and words, which always route to human reviewers.

## Out of scope

- Whether the script's facts are right → `accuracy-review`
- How a place name changed over time → `sp-maps-places`

## Where to look first

1. **T.R.'s own statements** about how a name is said, found in his letters
   and published writing (use `sp-quote-verifier` for the exact wording).
2. **Recordings:** surviving sound recordings of T.R. and his contemporaries
   (Library of Congress National Jukebox and Recorded Sound collections).
   Hand dating questions to `sp-film-sound-cartoons`.
3. **The institutions that hold a name:** National Park Service
   pronunciations for park and site names; state and local historical
   societies; local usage in the community today, confirmed with residents or
   local officials.
4. **For people:** family usage, documented in family papers, memoirs or
   interviews with descendants.
5. **For foreign names and words:** the language's standard pronunciation for
   the period, from a reliable dictionary, noting where English speakers of the
   time said it differently.
6. **Indigenous names and words:** the nation's own language resources and
   guidance. Route every one to the Library's human reviewers before
   recording.

## Known traps

- One pronunciation of the family name assumed for every branch of the family.
  Say which person's usage the source documents. [method]
- A modern local pronunciation used for a period quotation, or the reverse.
  Decide which the script needs and say so. [method]
- A foreign title or name anglicized one way in the script and another in the
  narration. Pick one, document it, and use it throughout. [method]
- A place name pronounced the way it is spelled, when locals say it differently.
  Confirm with local usage. [method]
- Indigenous names guessed from spelling. Never record one without guidance
  from the nation or the Library's human reviewers. [method]
- A pronunciation copied from an online audio site with no source. Treat it as
  a lead only. [method]

## Procedure

1. List every name and term in the script that a narrator might stumble on.
2. For each, find a documented pronunciation and its source, and note whose
   usage it reflects.
3. Write it in plain respelling (for example ROH-zuh-velt) and, where useful,
   the IPA.
4. Flag anything with no documented pronunciation, and every Indigenous name,
   for human review.
5. Note where the script should use one pronunciation consistently.

## Output

Follow reference/panel-rules.md section 11. Put the respelling and IPA in
`corrected_text`. Use `unverifiable` for names with no documented
pronunciation.
