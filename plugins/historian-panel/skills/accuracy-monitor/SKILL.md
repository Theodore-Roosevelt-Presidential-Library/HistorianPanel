---
name: accuracy-monitor
description: "Ongoing accuracy checks from the Historical Accuracy Standard, run on a schedule. Two modes: 'changes' finds trlibrary.com /tr, exhibit and quiz pages edited since the last run and reviews only the changed text; 'recheck' re-verifies a random 5% of previously closed claims to measure the error rate over time. Use from a scheduled task, or when someone asks to check what changed or to re-check past work."
argument-hint: "changes | recheck"
---

# Accuracy monitor

Read `reference/panel-rules.md` at the plugin root first.

This skill only reads pages and reports. It never edits the site. Fixes go to
whoever owns the content.

## Where state lives

Each run needs the date of the last run and, for `changes`, what each page said
then. Keep both in the person's private ledger location (`ledger_dir` in the
config), in `monitor/last-run.json` and `monitor/snapshots/`. Never put page
snapshots in this public repository. If no ledger location is configured, ask
where to keep state before the first run, and in an unattended run say that
state is missing and stop.

## Mode: changes

1. Read the site's XML sitemap (`/sitemap.xml`) and list pages under `/tr/`,
   `/visit/exhibits/` and `/quiz/` whose last-modified date is after the last
   run. If the sitemap has no dates, compare each page's text with its saved
   snapshot.
2. For each changed page, fetch the live page and compare it with its snapshot.
   Keep only added or changed sentences, captions, alt text and quiz items.
3. Send the changed text to `accuracy-review` in `review` mode, one location per
   page. Use `quiz-check` for quiz pages.
4. Save the new snapshots and the run date.
5. Report: pages changed, claims checked, fixes needed, with links.

## Mode: recheck

1. Collect previously closed claims from the ledger (`ledger.jsonl` final
   records with `result` supported, contradicted or partly_supported).
2. Draw a random 5% sample, at least 20 claims, and write the sample's IDs down
   before checking anything.
3. For a claim that was fixed, check the replacement text now on the page, not
   the old wording.
4. Send the sample to `accuracy-review` in `check` mode, with a fresh blind
   check. The new run must not see the old verdicts.
5. Compare. A claim whose result changed is a recheck error.
6. Report the recheck error rate, every changed claim, and the trend against
   earlier rechecks. Record the rate where the audit plan tracks it.

## Output

`monitor-<mode>-<date>.md` in the ledger folder, and a short summary in reply.
In a scheduled run, send the summary to the person through the session's
message tool so it reaches them.
