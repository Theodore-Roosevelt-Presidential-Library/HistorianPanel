---
name: scholarly-debate
description: "Stage a structured, cited debate between the documented positions historians have taken on a Theodore Roosevelt question, often across decades (memorial-era accounts, the 1930s, mid-century, the 1970s-80s, recent work). Use for contested questions of interpretation (Brownsville, Panama, the Bull Moose split, race and empire, the Badlands' effect on him) and for deciding how Library copy should frame a disputed subject. Produces a map of the disagreement, not a winner."
argument-hint: "<the question> [positions or eras to include]"
---

# Scholarly debate

Read `reference/panel-rules.md` at the plugin root first, and the
`sp-scholarly-perspectives` skill, whose sourcing rules every debater follows.

## The ground rules

- **Positions, not people.** Each side is "the case made in" specific works,
  for example "the reading in Pringle (1931) and those who followed him." No
  debater speaks as a historian, in the first person or otherwise. Never write
  dialogue for a real person.
- **Every assertion is cited** to a work, edition and page, or to a primary
  source that the work relies on. A debater may not invent an argument the
  literature does not make. A point the panel itself infers is labeled
  "panel inference" and kept out of the position's case.
- **Evidence beats eloquence.** The moderator strikes uncited points before
  anyone reads the result.
- **No winner.** The output is a map: where positions differ on evidence, where
  they differ on interpretation, and what newer evidence changed.
- Living scholars' positions come only from their published work. Indigenous
  history questions are framed for the Library's human reviewers, not settled
  by debate.

**Choosing works.** If the config sets `author_index_path`, read that index
first. It lists every book in the corpus with author, year, era and genre,
and the specialists whose subjects each book covers most. Use it to pick works
by subject and by era. Its scores measure coverage, not quality or
reliability, and anything marked do-not-cite is excluded.

## Procedure

1. **Frame the question** as one neutral sentence. Check it with the person
   before running.
2. **Choose two to four positions.** Default to positions from different eras.
   Use `sp-historiography` and `sp-biographies` to find which works define each
   position. Write each position as a label plus the works it rests on.
3. **Briefs (isolated).** Launch one `historian-panel:hp-debater` agent per
   position, in parallel. Each researches only its own position's works and
   the primary sources they cite, and writes an opening case: three to five
   cited points.
4. **Rebuttal.** Give each debater the other positions' openings. Each replies
   with cited points: where the others misread evidence, where newer or older
   evidence cuts against them, and what it concedes.
5. **Moderate.** Launch `historian-panel:hp-independence-auditor` on all cited
   sources. Strike points whose citations fail or do not say what is claimed.
   Mark points that rest on the same primary source read differently, since
   those are the true interpretive disputes.
6. **Map.** Write the result:
   - the question, and each position with its works and era
   - points of agreement
   - disputes about evidence (what the record shows) vs. disputes about
     interpretation (what it means)
   - evidence that appeared after a position was formed (newly opened papers,
     published letters) and how it bears on that position
   - **suggested framing for Library copy**: plain, even-handed wording that
     states what is established and names the disagreement where it exists
7. Send any factual claims raised along the way to `accuracy-review`.

## Output

`debate.md` in the ledger folder, and in reply: the question, a one-line
summary of each position, the main fault line, and the suggested framing.
