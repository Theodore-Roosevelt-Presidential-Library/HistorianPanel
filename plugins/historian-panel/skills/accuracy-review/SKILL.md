---
name: accuracy-review
description: "Check Theodore Roosevelt history for accuracy. Use whenever copy, a page, a caption, a quote, a dataset row or a single historical question about T.R., his family, his era or his places needs verifying before it carries the Library's name, or when existing content should be reviewed and improved. Coordinates the HistorianPanel specialists: extracts claims, routes each to the right specialists, runs a blind second check, audits source independence, resolves disagreements and writes a claim ledger. Modes are ask, review, check and sweep."
argument-hint: "[ask|review|check|sweep] <text, URL, file path, or question>"
---

# Accuracy review (coordinator)

You run the panel. You do not verify claims yourself; specialists do, each in
its own agent context. Your job is routing, isolation, bookkeeping and the final
report.

First read `reference/panel-rules.md` and `roster.yaml` at the plugin root
(two levels up from this file). Then read the local config if one exists:
`$HP_CONFIG`, else `./historian-panel.config.yaml`, else use the defaults in
`config.example.yaml`.

## Modes

| Mode | Input | What you produce |
|------|-------|------------------|
| `ask` | One question ("When did T.R. first come to Dakota?") | A sourced answer from one or two specialists, plus a blind check if the answer will be published |
| `review` | Draft copy, a URL, a file, or a page export | Every claim checked; a report with keep / fix / hedge / cut for each |
| `check` | A JSON file of claims already extracted (used by tests and batch runs) | A JSON file of reconciled verdicts at the path given |
| `sweep` | A confirmed error and its correction | Every other place the same error appears (hands off to `error-sweep`) |

If the mode is not given, infer it: a question is `ask`, anything with more than
one claim is `review`.

## Steps

### 1. Extract

For `review`, launch the `historian-panel:hp-claim-extractor` agent with the
text (or the URL or path) and ask for claims as JSON matching
`schemas/claim.schema.json`. For `ask`, turn the question into one claim of
type `other` with the question as its text. For `check`, read the file.

### 2. Route

For each claim, pick up to three **active** specialists from `roster.yaml`.
Many specialists overlap, so rank them rather than taking the first matches:

1. **Required seats.** `sp-quote-verifier` for type `quote`, `sp-photo-id` for
   `image_id`, `sp-superlatives` for `superlative`, and
   `sp-book-citations` for any book title, author or ISBN, and
   `sp-on-this-day` for any "on this day," anniversary or #OTD claim,
   `sp-period-visuals` for any newly made visual of a historical scene
   (illustration, AI-generated image, reenactment, animation), and
   `sp-pronunciation` when the piece is a narration or voice script. Any claim touching
   Indigenous history also gets `sp-northern-plains-indigenous`, which flags it
   for human review.
2. **Score the rest.** For each other `sp-` specialist, score one point per
   `routes.keywords` entry found in the claim text or context
   (case-insensitive, whole words or phrases), plus two points if the claim's
   type is in its `routes.types`.
3. **Prefer subject over method.** On a tie, choose a period, family or theme
   specialist (the subject expert) over a collection or scholarship specialist
   (where the evidence lives). A collection specialist earns a seat when the
   claim names its collection or the best evidence clearly lives there.
4. **Calendar math.** If the claim states an age, a span, "years later," or a
   day of the week, give `sp-chronology-calendar` a seat unless three required
   seats are already taken.
5. Fill to three seats in score order. Keep at least two different
   specialists per claim, so Pass B can use a different one than Pass A.
6. If nothing scores, use the closest active specialist and add the claim to a
   "roster gaps" list in your report. A gap that repeats across runs is a
   reason to run `propose-skill`.

Record the routing, with scores, on each claim.

### 3. Pass A

Group claims by specialist (at most 15 claims per batch). For each batch, launch
a `historian-panel:hp-specialist` agent. Tell it the specialist skill name to
load, give it the claims as JSON, and tell it this is Pass A. Launch batches in
parallel. Collect the verdict JSON from each.

### 4. Pass B (blind)

For every claim (or the share set by `pass_b_rate`; always 100% for quotes,
superlatives, image IDs, family facts and high-risk claims), launch
`historian-panel:hp-blind-verifier`.

**Isolation rule.** The Pass B prompt contains only the claim record: ID, text,
type, context, location, and the specialist skill to load. Never include Pass A's
verdict, sources, notes, corrected text, or any hint of them. Never tell Pass B
what you expect. Prefer a different specialist from the claim's routing than the
one used in Pass A. If only one fits, use the same skill; the fresh context is
what makes it blind.

### 5. Independence audit

After both passes are back, launch `historian-panel:hp-independence-auditor`
with each claim's combined source lists. It flags sources that derive from one
another or from a non-source (AI output, the Library's own site or tools, the
Story Guide, Wikipedia alone). A pass left with fewer than two independent
sources is downgraded to `unverifiable`.

### 6. Resolve

| Pass A | Pass B | Result |
|--------|--------|--------|
| Same verdict, both with two independent sources | | **Closed** with that verdict |
| Different verdicts, or either is unverifiable | | **Pass C**: launch a fresh `hp-blind-verifier` with a third specialist, still blind |
| Still split after Pass C | | **Unresolved**: recommend hedging or cutting the claim |
| Settling it needs an archive the team cannot reach | | Add it to **Questions for the curator** with what to check |

Map the closed verdict to an action: `supported` → keep; `contradicted` or
`partly_supported` → fix, using the corrected text with the most support;
`unverifiable` → hedge or cut. A claim that is not closed never publishes as
fact.

Claims flagged for human routing (panel rules section 10) are never closed by
the panel; list them for the human reviewers.

### 7. Write

Write to `ledger_dir`:

- `ledger.jsonl`: one line per verdict (A, B, C), plus one `"pass": "final"`
  record per claim with `result`, `action`, and `corrected_text`.
- `report.md`: a table grouped by location with current text, action, corrected
  text, sources, and confidence. Put unresolved claims, curator questions and
  roster gaps at the end.

For `check` mode, also write the final records as a JSON array to the output
path you were given.

Never edit the target page, file or dataset yourself. Fixes are applied by
whoever owns the content, after review.

### 8. Learn

If a closed error matches a pattern that no specialist's `## Known traps`
covers, note it under "Candidate traps" in the report. Do not edit skills. A
person (or `propose-skill`, through a pull request) turns candidate traps into
skill changes once the ledger IDs are confirmed.

## Reporting back

Lead with counts: claims checked, keep, fix, hedge or cut, unresolved. Then the
fixes, then the rest. Keep it short; the detail is in `report.md`.
