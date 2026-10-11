---
name: pm
description: The ProdMan.AI entry skill, one entry point for product management work. Describe a PM problem in plain words (messy documents, a feature decision, a roadmap, metrics, a PRD, a release, a portfolio) and it turns the request into a decision, picks the matching workflow from the index, runs the specialist skills in order, checks every number and quote in the result against your inputs, and lists what still needs your judgment. Use whenever someone describes a product management task without naming a specific skill.
disable-model-invocation: false
user-invocable: true
---

# /pm · one entry point for PM work

You describe the problem. This skill decides which specialist skills to run, in what order, and
checks the result before you see it. It never hides a prerequisite, never invents a number, and
stops before anything leaves your machine.

Version 4, 2026-10-11. Version 1 checked its work against its own notes. Version 2 checked against
the inputs but still let its own overstatements through. Version 3 handed the check to a reader who
did not write the work, and the author kept steering that reader. Version 4 takes the steering away:
a fixed brief built by a script, the checker's own table, and a seal that counts and applies the
checker's fixes. [Scoreboard](../../evals/scoreboards/pm.md).

## Before step 1: find the files
This skill's folder is `skills/pm/` inside the repo. Resolve these paths from this skill's base
directory, two levels up:

| File | Path | If missing |
|---|---|---|
| The PM standards | `PM.md` in the user's current project folder if one exists, otherwise `../../PM.md` | say so and continue with the rules in this file |
| The workflow routes | `../../workflows/ROUTES.md` (one line per workflow), then only the chosen workflow's section of `../../workflows/INDEX.md` | use the default chain in step 3 and say so |
| The curated resources | `../../resources/README.md` | route to this repo's skills only |
| The user's context | `context/PRODUCT.md`, `context/DECISIONS.md`, `context/CORRECTIONS.md` in the current project folder | ask at most three questions (step 2) |
| The check | `CHECKER.md` (the fixed checker brief) and `check.py` (builds the brief, then seals), both in this skill's folder | the check is not independent: say so in the hand back |

Read PM.md fully before step 1. Every rule in it applies to every step below.

## Steps

### 1. Save the request, then turn it into a decision
First, before anything else, save the request exactly as the user typed it, every character and
nothing added, to `outputs/<YYYY-MM-DD>-<short name>/00-request.md`. It is the main source the
check reads. Every later file of this run goes in the same folder.

Then write these four lines and save them to `00-frame.md`. Say nothing about routing until this
file exists.
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
Open the routes file and pick the workflow whose problem and required inputs match the decision
from step 1, not the nouns in the request. Say which one in a single line, with the reason, for
example: "Routing to A01, document chaos to product clarity, because you have 20 files and need a
prioritised plan."
- If two workflows fit in sequence, run both and say so. Never more than two.
- If none fits, use the default chain from PM.md section 4 (frame, gather, decide, produce,
  check) and say "no workflow matched; default chain".
- Never invent a workflow ID that is not in the routes file. Then read that workflow's full section in INDEX.md, and only that section.

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
   the next step needs. Every file starts with the line `DRAFT, not reviewed by a person` (PM.md
   section 10) until the user approves it.
5. If a step builds something (a prototype, a page, code), read it back after writing it and check
   it against the spec it came from: every number, label and behaviour it shows is a claim.

When two sources conflict and the conflict decides the plan, write the plan under each side of the
conflict, side by side, and put the conflict first in the judgment list. Never let your own
arithmetic, a date or a preference settle a conflict a person has to decide.

Keep a running list of every assumption, conflict and gap found along the way.

### 5. The check: done by someone else, counted by a script
The author of an artifact does not check it (PM.md section 7), and does not steer the check either.
Every run ends with these four moves, including a run that stops at questions. `<skill folder>`
below is this skill's base directory.

1. **Draft.** Write the hand back in the shape of step 6 and save it as `NN-handback-draft.md`, with
   the CHECKS line holding exactly `{{CHECKS}}`. List every step the workflow names in STEPS, each
   with its file or "skipped" and the reason. Everything the user will read is now on disk.
2. **Brief.** Run `python3 <skill folder>/check.py brief <run folder> <every file or folder the user
   gave>`. Name every input the user gave and nothing the run wrote; the request is already included
   from `00-request.md`. From this moment, change nothing in the run folder.
3. **Checker.** Start the checker with the Agent tool. Its prompt is the one line the script printed,
   copied exactly: add nothing, remove nothing, send nothing else. The checker writes its own table
   to `check.md`. Never write, edit or summarise `check.md` yourself. If the Agent tool is missing,
   follow the brief yourself in a fresh pass and say in the hand back that the check was not
   independent.
4. **Seal.** Run `python3 <skill folder>/check.py seal <run folder>`. It refuses if anything changed
   after the brief. Otherwise it applies the checker's own fixes, removes email addresses the user
   did not type, fills the CHECKS line with the table's counts, and prints the final hand back. If it
   refuses, do what it says (a new brief, then a new check). Never work around it.

Your final message is the sealed hand back: everything the seal printed below its first line, copied
unchanged, with nothing added before or after it. Anything else you want to say goes into the draft
before the brief.

### 6. Hand back
Use this shape, in this order, every section present:

```text
RESULT        <one sentence: the call or the artifact> · <link to the file>
ROUTE         <workflow id and name>, because <the reason> · <skills run, in order> · <fallbacks used>
STEPS         every step the workflow lists: done (file or section) or skipped (reason)
CHECKS        {{CHECKS}}
NEEDS YOUR JUDGMENT
              numbered, specific: the conflict, the trade off, the assumption to confirm
NEXT ACTIONS  one to three, each with an owner
ASSUMPTIONS   every assumption the result depends on
CONFIDENCE    high, medium or low (no other word), and the one reason that most limits it
```

Write the CHECKS line exactly as shown. The seal replaces `{{CHECKS}}` with the counts from the
checker's table; a count you write yourself is a claim nobody checked.

## Rules that override everything above
- Never invent metrics, quotes, customers, users or results. Synthetic data is labelled synthetic.
- Stop before sending, posting, publishing, sharing, editing a real tracker or spending money. Draft it and ask.
- Conflicting sources are shown side by side with both citations. Never pick one silently.
- Plain language. A term a new PM would not know (ARPU, churn, gross revenue retention) gets one plain sentence the first time it appears.
- Never write the user's email address, name or account details into any file unless the user typed them in the request.
- Never describe something the user did that did not happen. If no answer came back, say that, not "you declined".

## VERIFY
**Rung:** Observer · **Irreversible?** no. Every output is a local file. The actions it might
recommend (posting, editing a tracker) are exactly what it must not take.

| # | Check | How | Type | Fails if |
|---|---|---|---|---|
| 1 | Decision first | The four lines of step 1 appear before any artifact content, and are saved in 00-frame.md | auto | the artifact starts before the decision is stated |
| 2 | Route named | A workflow ID that exists in the index, or "default chain", with a reason | auto | skills run with no route named, or an ID not in the index |
| 3 | Prerequisites surfaced | Every missing input or connector is named before the chain runs, with its fallback | auto | a missing prerequisite appears only at the end, or not at all |
| 4 | Steps saved | Each step's output exists under `outputs/` and is linked | auto | a step's output exists only in chat |
| 5 | Checks evidenced | Every run, stops included, has `check-brief.md`, `check.md` and `seal.txt`; `check.py verify <run folder> <final message>` passes; the checker was started with the one line prompt and nothing else; `check.md` was written by the checker, not the author; every fact stating sentence has a row | auto | any of these missing or different, or a fact stating sentence with no row |
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

**Step 5, one row of the checker's table:** Claim "Reminders came up in 4 of 6 interviews." ·
source: the lines for notes A, C, E and F, pasted · working: A, C, E, F = 4 · verdict: yes. The seal
then fills CHECKS with, for example, "41 claims checked by a separate reader · 3 failed · 2 corrected
· 1 removed · 0 still open · table: check.md".

**Step 6, abridged:** RESULT: three conflicts found, two resolvable from the documents, one needs a
decision from sales; the roadmap ranks five items, two marked low confidence because their only
evidence is one support ticket. NEEDS YOUR JUDGMENT: 1. SSO is a launch requirement in the PRD
and a later phase in the sales notes; the plan is shown both ways until that is settled.
