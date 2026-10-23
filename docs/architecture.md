# Architecture

## Three layers

1. **The specialists** do the checking. Each is a skill (the knowledge: scope,
   where to look, known traps) run inside an agent (the isolation).
2. **The quality layer** guards the specialists: mechanical checks, a scored
   test set, and a weekly drift report.
3. **People** merge every change and own every published correction.

A fourth layer of watcher agents would share the same blind spots as the agents
it watches. The quality layer is mostly not AI on purpose.

## Skills hold knowledge; agents give isolation

| | Skill | Agent |
|---|---|---|
| What it is | `skills/<name>/SKILL.md` | `agents/<name>.md` |
| What it holds | Scope, sources to search, traps, procedure | Which skill to load, which tools, which model |
| Why | Any session can load it, in any Claude app | Runs in its own context, so Pass B cannot see Pass A |

One agent (`hp-specialist`) runs any specialist skill named in its prompt. That
keeps 50 specialists from needing 50 agent files.

## How a request reaches the right specialists

```
person's request
   │  matches the accuracy-review description, a standing instruction,
   │  or another skill calls it as a step
   ▼
accuracy-review (coordinator, in the main session)
   ├─ hp-claim-extractor ........ claims as JSON
   ├─ roster.yaml routing ....... up to 3 specialists per claim
   ├─ hp-specialist × N ......... Pass A, in parallel
   ├─ hp-blind-verifier × N ..... Pass B, claim only, different specialist
   ├─ hp-independence-auditor ... are the sources really two?
   ├─ hp-blind-verifier ......... Pass C on disagreements
   └─ ledger.jsonl + report.md
```

Routing rules: a specialist takes a claim when the claim's type is in its
`routes.types` and its text matches `routes.keywords`. Quotes, images and
superlatives always go to their specialists. Unmatched claims are listed as
roster gaps.

## Growing the roster

Planned specialists in `roster.yaml` are the backlog. A repeated roster gap, or a
confirmed error no trap covers, is the signal to build one with `propose-skill`.
It arrives as a pull request; the quality layer scores it; a person merges it;
everyone gets it on the next update.

## Where data lives

| Data | Where | Why |
|------|-------|-----|
| Skills, agents, roster, rules, scripts | This repository | Shared tooling |
| Claim ledger, fix lists, Questions for the curator | Private ledger repository | Evidence, not public |
| Regression cases built from the ledger | Private, via `HP_CASES` | Would reveal page errors |
| Licensed corpora | Their own systems, via config | Licenses cover internal use only |
| Local config | `historian-panel.config.yaml`, git-ignored | Points at internal systems |
