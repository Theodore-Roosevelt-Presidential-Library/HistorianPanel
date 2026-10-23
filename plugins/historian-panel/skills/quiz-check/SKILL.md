---
name: quiz-check
description: "Check a history quiz, trivia set or game about Theodore Roosevelt as a whole: the question, the marked answer, every wrong option, and the explanation. Catches the errors specific to quizzes: a wrong answer key, a 'wrong' option that is also true, a question with two defensible answers, and explanations that add new errors. Use for /quiz pages, trivia cards, games, classroom materials and social polls."
argument-hint: "<quiz text, URL or file>"
---

# Quiz check

Read `reference/panel-rules.md` at the plugin root first.

A quiz fails in ways a page does not. The marked answer can be wrong. A
distractor can be accidentally true. The wording can allow two correct answers.
The explanation can introduce a new claim the question never needed. Every
option is a claim.

## Procedure

1. **Parse** each item into: question, options, marked answer, explanation.
2. **Turn every option into a claim.**
   - The marked answer becomes "[question premise] is [answer]," expected true.
   - Each distractor becomes "[question premise] is [option]," expected false.
   - The explanation is split into its own claims.
3. **Check** all of them with `accuracy-review` in `check` mode. Quotes,
   superlatives and dates get their required specialists as usual.
4. **Judge each item:**

   | Finding | Meaning | Fix |
   |---------|---------|-----|
   | Marked answer contradicted | Wrong key | Change the key, or rewrite the question |
   | A distractor supported | Two right answers | Replace the distractor with one that is clearly wrong |
   | A distractor partly supported or debatable | Ambiguous item | Tighten the question wording |
   | Explanation claim contradicted | New error | Fix or cut the sentence |
   | Question premise wrong | Bad question | Rewrite or drop |

5. **Check difficulty and fairness:** a distractor that is a trick of wording
   rather than of history, or a question that depends on a disputed date, should
   be rewritten or flagged.
6. **Check the audience.** Language should suit the quiz's readers (families,
   students). Hard chapters are handled with care, not avoided and not
   sensationalized.

## Output

`quiz-check.md` in the ledger folder: one row per item (question, finding,
suggested fix, sources), then counts: items checked, keys wrong, two-answer
items, explanation errors. In reply, give the counts and the items to fix first.
