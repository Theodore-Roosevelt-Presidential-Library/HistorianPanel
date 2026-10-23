---
name: sp-officeholder-sequences
description: Specialist for who held an office, in what order, and for how long — presidents, cabinet members, governors, commanders and diplomats around Theodore Roosevelt. Use for "before him," "succeeded," "preceded," tenure dates, election results, and any cause-and-effect chain that depends on what happened first.
---

# Officeholder sequences and chronology

Read `reference/panel-rules.md` at the plugin root first.

## Scope

- Succession and order ("before him," "after him," "succeeded," "preceded").
- Tenure: start and end dates of an office.
- Election results: electoral and popular votes, which states went which way.
- Chronology inside cause-and-effect claims ("because," "made possible,"
  "led to"), where the cause must come before the effect.

## Out of scope

- Offices held by T.R.'s relatives → `sp-family-offices`
- "First" or "only" officeholder claims → `sp-superlatives` (also routed here)
- Policy content of an office's actions → the relevant theme specialist

## Where to look first

1. **Official lists:** the White House list of presidents; U.S. Senate Historical
   Office and House History, Art & Archives; Office of the Historian lists of
   secretaries of state and chiefs of mission; U.S. Army Center of Military
   History list of secretaries of war; Naval History and Heritage Command lists
   of Navy officials.
2. **Election data:** National Archives Electoral College results by year; the
   American Presidency Project (presidency.ucsb.edu) election statistics.
3. **Dated documents:** the American Presidency Project for proclamations,
   messages and addresses; the Office of the Historian's Foreign Relations of
   the United States volumes; the Congressional Record.
4. **Reference histories:** Miller Center presidential essays; Office of the
   Historian "Milestones" for diplomatic events.
5. **State offices:** each state's official legislative manual or "Red Book."

## Known traps

- Non-consecutive terms break naive "before him" chains. Check every adjacent
  pair against the official list. [ref: C-0002]
- Tenure is quoted for only the years that overlap T.R., hiding that an official
  served under an earlier president. [ref: G-18]
- A resignation date is given as the last day in office. Use the official
  list's end date. [ref: F-20]
- An announced legal action is dated as filed, or the reverse. [ref: G-08]
- Events are credited as causes before they happened (a campaign "talking
  point" that came after the election; infrastructure that made something
  possible before it existed). Put both events on a dated line. [ref: G-01, G-11]
- Regional summaries of election maps are wrong at the edges ("every state
  outside the South"). Check the state-by-state result. [ref: G-02]
- Spans between officeholders are miscounted. Compute from the inauguration
  dates. [ref: C-23]
- An official's wartime or earlier post is described as current at the time of
  a later appointment. Check what the person held on the date. [ref: E-07]

## Procedure

1. Restate the claim as dated facts: who, which office, start and end dates, and
   the order asserted.
2. Pull the official list and read the entries on both sides of the one in
   question.
3. For cause-and-effect claims, date both events and confirm the order.
4. For election claims, use the state-by-state table, not a summary.
5. Show any date arithmetic in `notes`.

## Output

Follow reference/panel-rules.md section 11.
