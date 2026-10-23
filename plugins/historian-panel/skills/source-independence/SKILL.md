---
name: source-independence
description: Audit whether the sources behind a historical claim are truly independent. Use after Pass A and Pass B of a HistorianPanel review, or any time two sources for a Theodore Roosevelt fact might be one source repeated.
---

# Source independence audit

Read `reference/panel-rules.md` at the plugin root first.

## Scope

The source lists from every pass on a claim. You judge the sources, not the
claim.

## Procedure

For each claim:

1. List every source cited across passes.
2. Mark any source that never counts (panel rules section 3): AI output, the
   Library's own site or tools, the Story Guide, Wikipedia alone.
3. Look for shared ancestry:
   - A web page that cites, quotes or closely paraphrases another source on the
     list.
   - Several sites with the same wording, which usually means one copied the
     others or all copied a common source.
   - Secondary works that cite the same single primary source. Those are fine as
     a chain to the primary, but they count once.
   - A reprint and its original (a 1916 pamphlet reprinting a 1903 address)
     count once.
4. Open sources when needed to check what they cite. Note what you found.
5. Count independent sources per pass. If a pass has fewer than two, say so.

## Output

A fenced `json` block holding an array with one object per claim:

```
{"claim_id": "...", "independent_count_by_pass": {"A": 2, "B": 1},
 "non_sources": ["..."], "derived_pairs": [["source X", "source Y", "why"]],
 "downgrade": ["B"], "notes": "..."}
```
