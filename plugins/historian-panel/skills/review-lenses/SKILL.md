---
name: review-lenses
description: "Review Theodore Roosevelt copy through scholarly lenses — narrative biographer, documentary editor, political historian, critical historian, regional historian, military historian, naturalist — to catch what a fact-check misses: omissions, embroidered scenes, missing context, one-sided framing, tone. Use after accuracy-review on exhibits, long-form pages, scripts, decks and press materials, or when someone asks how scholars would see a piece."
argument-hint: "<text, URL or file> [lenses: all | comma-separated list]"
---

# Scholarly review lenses

Read `reference/panel-rules.md` at the plugin root first. Then read
`references/lenses.md` in this skill's folder.

## What this is, and what it is not

A lens is a **set of questions a school of scholarship asks**, not a person.
Never name a lens after a historian, never write "Morris would say" or "as
Dalton might put it," and never present a lens's findings as any scholar's
opinion. What real scholars actually wrote comes from
`sp-scholarly-perspectives`, with citations.

Lenses do not decide facts. When a lens notices a factual problem, it hands
the claim to `accuracy-review`. Lenses report on **framing, completeness,
sourcing of scenes, context and tone**.

## Procedure

1. **Pick lenses.** Default to all seven for exhibits, /tr pages, scripts and
   press materials; otherwise pick the three that fit the subject (the table
   in `references/lenses.md` suggests which).
2. **Run each lens separately**, one `historian-panel:hp-lens-reviewer` agent per
   lens, in parallel. Give each agent the full text and its lens name only, not
   other lenses' findings, so they do not converge.
3. **Collect findings.** Each finding has: location, lens, kind (omission,
   embroidered scene, missing context, one-sided framing, tone, factual claim
   to check), what is wrong, and a suggested fix.
4. **Merge.** Group findings by location. When two or more lenses flag the same
   passage, mark it as a priority. When lenses disagree (one wants more
   context, another wants it shorter), show both and let the person decide.
5. **Send factual claims** that lenses raised to `accuracy-review` in `check`
   mode.
6. **Report.** Lead with the three most important findings. Then the table.
   Keep the Library's voice in every suggested fix: friendly, plain, specific,
   politically even-handed.

## Output

`lenses.md` in the ledger folder, and a short summary in reply: count of
findings by lens and kind, then the priorities.
