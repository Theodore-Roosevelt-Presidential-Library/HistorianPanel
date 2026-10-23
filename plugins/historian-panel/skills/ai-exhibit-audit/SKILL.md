---
name: ai-exhibit-audit
description: "Audit the Library's own public AI experiences (the Campfire virtual historian, the Talk with the President exhibit, and any other assistant that answers in T.R.'s name or the Library's) by asking them a bank of test questions and running every answer through the panel. Use monthly, after any model or knowledge-file change, or when someone reports a wrong answer. Produces an error rate, the wrong answers with corrections, and the likely root cause in the assistant's knowledge files."
argument-hint: "<assistant name or URL> [question count, default 40]"
---

# Audit the Library's AI experiences

Read `reference/panel-rules.md` at the plugin root first, then
`references/question-bank.md` in this skill's folder.

The Library's assistants speak to the public under its name, so they are held to
the same Historical Accuracy Standard as a web page. Their answers are AI output:
they are always the thing being checked, never a source.

## Procedure

1. **Build the question set.** Take 40 questions by default from the bank's
   categories, weighted toward the high-risk ones (quotes, family offices,
   dates, superlatives, the Badlands). Add a few questions that bait known traps
   (a famous misquote, a "first" that is not true, a wrong title for a son).
   Add any question a person reported. Record the set before asking anything.
2. **Ask.** Put each question to the assistant in a fresh conversation, so
   earlier answers cannot steer later ones.
   - If a browser tool is available and the person approves, use it on the
     assistant's public page and copy each answer exactly.
   - Otherwise, give the person the question list and ask them to paste the
     answers back.
   - Never sign in, create accounts or change the assistant's settings.
3. **Check.** Send all answers to `accuracy-review` in `review` mode, one
   location per question, so every claim gets Pass A, a blind Pass B and the
   source audit.
4. **Score.** For each answer, record whether it:
   - contained any contradicted claim
   - contained any unverifiable claim stated as fact
   - quoted T.R. inexactly
   - declined appropriately when it could not know

   Report the share of answers with at least one error.
5. **Find root causes.** For each wrong answer, look for where the error came
   from: the assistant's knowledge files or narrative documents (if the person
   gives access), a widely copied web page, or a known myth. Hand each confirmed
   error to `error-sweep`.
6. **Compare** with the previous audit if there is one. Say whether the error
   rate rose or fell, and which categories moved.

## Output

`ai-audit.md` in the ledger folder: date, assistant, question count, error rate,
a table of wrong answers (question, answer excerpt under 25 words, problem,
correction, sources), root causes, and the comparison. In reply, give the error
rate and the three most serious errors.
