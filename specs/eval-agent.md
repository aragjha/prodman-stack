<!-- format: locked-v1 -->
# Spec - the Eval Agent (`run-verify`)

> Owner: Anurag · written 2026-10-09 · WHAT + acceptance criteria, never HOW · inputs: practical
> example 2 (`research/practical/pe2-what-are-evals/`), sheet row "Eval Agent" columns C, D, G, L.

## Purpose
Let a PM test any piece of their own work, not only an AI skill, the way the research skill was tested
today: a written standard, a few tricky test cases, a grader who does not know the intent, a pass bar
the PM owns, and a scoreboard that shows the failures. The PM learns what an eval is by running one.

## The problem, in Anurag's words
*"Very confusing yaar, first explain me what evals are - is it same as success criteria, or KPIs or
metrics... is it related to evaluating LLM only or can be generalised for all forms of product,
design, distribution, launch etc... I should learn too, as the human in loop - don't know what is
verify block and golden set."*

## Who it is for
A PM who has never written an eval, testing (a) a skill or AI feature, (b) a spec, (c) a design, or
(d) a launch.

## What it does
1. **Explains first.** Before anything is set up, the PM gets the one-page explainer (what an eval is;
   how it differs from success criteria, KPIs, metrics, acceptance tests; the parts in plain words).
   Every term is defined the first time it appears. No jargon is used before it is defined.
2. **Writes the standard with the PM.** Asks what "good" means for this piece of work, in at most 7
   yes/no checks, using the matching mode: spec (Cagan's four risks) · design (Nielsen heuristics) ·
   launch (the launch checklist) · AI output (success criteria from the PM's own failures).
3. **Builds the test set.** 5 cases: 1 normal case and 4 tricky ones, each built to break one check,
   each with its trick written down so the PM can audit it. Written before grading starts.
4. **Runs and grades blind.** Each case is produced in a fresh context. Mechanical checks are scored by
   script with the actual value shown. Judgement checks go to graders who are told the criterion and
   nothing about the intent.
5. **The PM labels too.** The PM grades the same outputs. An AI grader's verdict counts only on checks
   where it agreed with the PM's labels.
6. **Writes the scoreboard.** Pass/fail per case in plain words, the worst failure first, the one fix
   most likely to help, the defects found in the test itself, and the date. Red rows stay.
7. **Moves the trust level.** Trust is earned from the score (4 of 5 to be trusted to draft), never
   declared, and is voided by any edit to the thing tested.
8. **Mirrors to the sheet.** One row per case in the Evals tab, readable by someone with no context.

## What it must not do
- Grade its own output, or let the producer see the tricks.
- Edit a run to make it pass.
- Change the test set after a run has been scored (add a case instead).
- Publish anything. The PM publishes.

## Acceptance criteria
| # | Criterion | Fails if |
|---:|---|---|
| 1 | A PM who has never written an eval can say, after the explainer, how an eval differs from a KPI and from success criteria | the PM cannot (checked by asking the PM; Anurag is the first test) |
| 2 | Works for all four modes: spec, design, launch, AI output | any mode has no worked example |
| 3 | The test set exists before the first grade, with every trick written down | a trick is missing, or written after grading |
| 4 | Producers never see the tricks | a trick string appears in any producer's input |
| 5 | Every mechanical check prints the actual value beside the verdict | a bare pass/fail |
| 6 | Judgement graders were not told the intent | the intent appears in a grader's brief |
| 7 | The PM's labels are collected, and an AI grader is trusted only on checks where it agrees with them | AI verdicts used with no PM labels |
| 8 | The scoreboard names the worst failure and one fix, and keeps red rows | a scoreboard with no failure section, or a red row removed |
| 9 | The Evals tab row is understandable to someone with no context | a reviewer with no context cannot say what was tested and why it failed |
| 10 | First real uses: (a) re-grade `product-research` round 4, (b) eval worksheets for three AI products from the author's day job, kept private and outside this repo | either is not run |

## Non-goals (this version)
Automated scheduling of eval runs; a UI beyond the sheet; any dashboard.

## The loop with the research skill
Once this agent passes its own 5 cases, it re-grades `product-research` and checks whether the
research skill's tests were measuring the right things (Anurag's loop). Whatever it finds that is
wrong becomes a new test case for the research skill, never an edit to an old one.
