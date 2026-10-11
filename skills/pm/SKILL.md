---
name: pm
description: The ProdMan.AI PM SuperSkill, one entry point for product management work. Describe a PM problem in plain words (messy documents, a feature decision, a roadmap, metrics, a PRD, a release, a portfolio) and it turns the request into a decision, picks the matching workflow from the index, runs the specialist skills in order, checks every number and quote in the result against your inputs, and lists what still needs your judgment. Use whenever someone describes a product management task without naming a specific skill.
disable-model-invocation: false
user-invocable: true
---

# /pm · one entry point for PM work

You describe the problem. This skill decides which specialist skills to run, in what order, and
checks the result before you see it. It never hides a prerequisite, never invents a number, and
stops before anything leaves your machine.

Version 2, 2026-10-11. Version 1 scored 1 of 5 on its golden set: its self check trusted its own
notes instead of the inputs. Step 5 below is the fix. [Scoreboard](../../evals/scoreboards/pm.md).

## Before step 1: find the files
This skill's folder is `skills/pm/` inside the repo. Resolve these paths from this skill's base
directory, two levels up:

| File | Path | If missing |
|---|---|---|
| The PM standards | `PM.md` in the user's current project folder if one exists, otherwise `../../PM.md` | say so and continue with the rules in this file |
| The workflow index | `../../workflows/INDEX.md` | use the default chain in step 3 and say so |
| The curated resources | `../../resources/README.md` | route to this repo's skills only |
| The user's context | `context/PRODUCT.md`, `context/DECISIONS.md`, `context/CORRECTIONS.md` in the current project folder | ask at most three questions (step 2) |

Read PM.md fully before step 1. Every rule in it applies to every step below.

## Steps

### 1. Turn the request into a decision, and save it
Write these four lines, then save them to `outputs/<YYYY-MM-DD>-<short name>/00-frame.md`. Every
later file of this run goes in the same folder.
- **Decision:** what will be decided with this work, in the user's words where possible.
- **Decider and date:** who decides, and by when ("unknown" is allowed). A weekday and a date given
  together must agree; check them before writing.
- **Done looks like:** the artifact the decision needs (a ranked list, a PRD, a roadmap, a brief).
- **Inputs in hand:** the files, data and access the user actually gave.

If the request has no decision in it (for example "make me a roadmap" with nothing attached), do
not produce a generic artifact. Ask for the decision, or state the assumption you will work under
and mark every downstream line that depends on it.

### 2. Fill the context gaps: three questions at most, in total
If `context/PRODUCT.md` is missing and the work depends on the product, ask at most three questions
in total, choosing from: the decision (if step 1 had none), who the user is, the metric that
matters, the hard constraint. Never send a form of five.

If no answer can come back (a non interactive session, or the user says go ahead), say plainly
"no answer came back", then either stop with the questions or continue on stated assumptions.
Never write that you asked as if you had been answered.

### 3. Route, only after the decision exists
Open the workflow index and pick the workflow whose problem and required inputs match the decision
from step 1, not the nouns in the request. Say which one in a single line, with the reason, for
example: "Routing to A01, document chaos to product clarity, because you have 20 files and need a
prioritised plan."
- If two workflows fit in sequence, run both and say so. Never more than two.
- If none fits, use the default chain from PM.md section 4 (frame, gather, decide, produce,
  check) and say "no workflow matched; default chain".
- Never invent a workflow ID that is not in the index.

Then check the workflow's prerequisites against step 1's inputs. For every missing one, say
exactly what is missing, what it blocks, and the fallback, before running anything. A missing
connector (Amplitude, Jira, Linear) means you work only from data the user provides, and you say
so. You never fill a missing input with plausible content.

### 4. Run the chain, every step of it
For each skill and step the workflow lists, in order:
1. If it is a skill in this repo, read `../<skill>/SKILL.md` and follow it.
2. If it is an outside resource from the curated list and it is installed, invoke it. If it is
   not installed, say how to install it in one line, then run the fallback the index gives for
   that step, labelled "fallback, not the original skill".
3. Do every step the workflow lists, or write "skipped: <reason>". If the workflow says to score
   candidates on impact, confidence and effort, every candidate gets all three, with "unknown"
   where you do not know.
4. Save the step's output as the next numbered file in the run folder and carry forward only what
   the next step needs.

When two sources conflict and the conflict decides the plan, write the plan under each side of the
conflict, side by side, and put the conflict first in the judgment list. Never let your own
arithmetic, a date or a preference settle a conflict a person has to decide.

Keep a running list of every assumption, conflict and gap found along the way.

### 5. Check every claim against the inputs, in a file
Write `NN-check.md` in the run folder before handing back. It has two parts.

**Part A, the claims table.** List every number, percentage, money amount, date, weekday, count
("4 of 6 firms"), named person or company, and quote in the final artifact. For each one:

| Claim | Source line, pasted from the original input or cited page | Recomputed or recounted | Verdict |
|---|---|---|---|

- The source is always the user's original input or a cited page, never this run's own earlier
  files. A claim with no source line is removed or relabelled as an assumption.
- Recompute every derived value (sums, differences, percentages, capacity, the weekday of a date)
  and show the working. Use `python3` when it is available.
- Recount every count by naming the items ("firms A, C, E and F: 4").
- Set every paraphrase of a person's words beside the original. If the paraphrase says more than
  the source, use the source's words.
- Every quote must match its source character for character.

**Part B, the criteria.** Grade the artifact against the workflow's checks and the rubric in PM.md
section 7. For each criterion write pass or fail and quote the line of the artifact that proves it.
If anything fails, fix it once and check again. If it still fails, report it as failed. Never
present a failed check as passed.

This is a self check for quality, not a score for publication (PM.md section 7).

### 6. Hand back
Use this shape, in this order, every section present:

```text
RESULT        <one sentence: the call or the artifact> · <link to the file>
ROUTE         <workflow id and name> · <skills run, in order> · <fallbacks used> · <steps skipped and why>
CHECKS        <claims checked, fixed, removed> · link to NN-check.md · then criterion | pass or fail | evidence line
NEEDS YOUR JUDGMENT
              numbered, specific: the conflict, the trade off, the assumption to confirm
NEXT ACTIONS  one to three, each with an owner
ASSUMPTIONS   every assumption the result depends on
CONFIDENCE    high, medium or low, and the one reason that most limits it
```

## Rules that override everything above
- Never invent metrics, quotes, customers, users or results. Synthetic data is labelled synthetic.
- Stop before sending, posting, publishing, sharing, editing a real tracker or spending money. Draft it and ask.
- Conflicting sources are shown side by side with both citations. Never pick one silently.
- Plain language. A term a new PM would not know (ARPU, churn, gross revenue retention) gets one plain sentence the first time it appears.

## VERIFY
**Rung:** Observer · **Irreversible?** no. Every output is a local file. The actions it might
recommend (posting, editing a tracker) are exactly what it must not take.

| # | Check | How | Type | Fails if |
|---|---|---|---|---|
| 1 | Decision first | The four lines of step 1 appear before any artifact content, and are saved in 00-frame.md | auto | the artifact starts before the decision is stated |
| 2 | Route named | A workflow ID that exists in the index, or "default chain", with a reason | auto | skills run with no route named, or an ID not in the index |
| 3 | Prerequisites surfaced | Every missing input or connector is named before the chain runs, with its fallback | auto | a missing prerequisite appears only at the end, or not at all |
| 4 | Steps saved | Each step's output exists under `outputs/` and is linked | auto | a step's output exists only in chat |
| 5 | Checks evidenced | NN-check.md has a claims table sourced from the original inputs, and every criterion cites a line | auto | a check is asserted without evidence, or claims are checked against the run's own files |
| 6 | Nothing invented | Every number, date, count, name and quote traces to an input or a cited source, and every derived value is right | adversarial | any invented or wrongly derived metric, date, count, quote, customer or result |
| 7 | Judgment list is real | "Needs your judgment" names specific trade offs from this run | adversarial | empty, or generic advice that fits any request |
| 8 | Stops at the line | No send, post, tracker edit or spend happened or was claimed | auto | any external action taken or claimed |

**Red flags (any one = rung 0):**
- Filling a missing input (metrics, interview notes, a connector's data) with plausible content.
- Reporting a check as passed when the run's own output shows it failed.
- Claiming to have posted, sent or updated anything outside the folder.

**Rollback:** delete the run's folder under `outputs/`.

## Example
**Request:** "I have 20 messy product documents. Organise them, find the conflicting requirements,
build a roadmap, and tell me what to prioritise."

**Step 1:** Decision: what to build first next quarter. Decider: the user, date unknown. Done
looks like: a prioritised roadmap with the conflicts resolved or escalated. Inputs: 20 files.

**Step 3:** "Routing to A01 (document chaos to product clarity), then C02 (evidence based
prioritisation), because the files must be reconciled before anything can be ranked."

**Step 5, one row:** Claim "reminders came up in 4 of 6 interviews" · source lines from notes A, C,
E, F pasted · recounted: A, C, E, F = 4 · verdict: holds.

**Step 6, abridged:** RESULT: three conflicts found, two resolvable from the documents, one needs a
decision from sales; the roadmap ranks five items, two marked low confidence because their only
evidence is one support ticket. NEEDS YOUR JUDGMENT: 1. SSO is a launch requirement in the PRD
and a later phase in the sales notes; the plan is shown both ways until that is settled.
