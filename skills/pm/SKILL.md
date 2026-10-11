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

Version 3.1, 2026-10-11 (3.1 changes routing only: it reads the one line routes file instead of the whole index). Version 1 checked its work against its own notes. Version 2 checked against
the inputs but still let its own overstatements through. Version 3 hands the check to a reader who
did not write the work. [Scoreboard](../../evals/scoreboards/pm.md).

## Before step 1: find the files
This skill's folder is `skills/pm/` inside the repo. Resolve these paths from this skill's base
directory, two levels up:

| File | Path | If missing |
|---|---|---|
| The PM standards | `PM.md` in the user's current project folder if one exists, otherwise `../../PM.md` | say so and continue with the rules in this file |
| The workflow routes | `../../workflows/ROUTES.md` (one line per workflow), then only the chosen workflow's section of `../../workflows/INDEX.md` | use the default chain in step 3 and say so |
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

### 5. Check every claim with fresh eyes, in a file
The author of an artifact does not check it (PM.md section 7). This step runs on every hand back,
including a run that stops at questions.

1. Write the hand back (step 6) first and save it as `NN-handback-draft.md`. Nothing new may be
   added to it after the check.
2. Run the check as an independent pass. If you can start a subagent (the Agent tool), give it only
   the checker brief below, the paths of the user's original input files, and the paths of the final
   artifact and the hand back draft. It must not see your notes or intermediate files. If you cannot
   start a subagent, run the checker brief yourself in a fresh pass that reads only those files, and
   say so in the hand back.
3. Apply every correction the check returns: use what the source supports, narrow the claim, or
   remove it. Save the check as `NN-check.md`, then hand back exactly the corrected draft.

**The checker brief (give it word for word):**

> You are checking a product management artifact against its sources. You did not write it. Read
> the artifact and the hand back sentence by sentence. Make one row for every sentence that states
> a fact: a number, percentage, money amount, date, weekday, count, a comparison word (halved,
> doubled, most, all, only, every, never), a claim about how something works, a claim about what a
> person or document said, a quote, or a citation of a section. For each row: paste the exact source
> line from the original input files or the cited web page, or write NONE; recompute any derived
> value and show the working, using python3 when it is available; for a count, name every counted
> item and paste its line, and count an item only when its own line states the thing being counted,
> not something near it; then answer "does the source say exactly this, and no more?" with yes or
> no. A NONE or a no is a failed row, with the corrected wording or the word remove. A quote must
> match its source character for character, a shortened quote must mark every cut with an ellipsis,
> and a note taker's summary is never a customer's quote. Never mark a row as holding when its own
> pasted source does not support it. If the artifact includes a built file (a prototype, a page,
> code), open it and treat every number, label and behaviour it shows as a claim to check against the
> spec and the inputs. A search tool's summary is never a source: a web claim needs the page itself.
> Return the table, then the number of rows, failed rows and corrections.

4. In the hand back, report the number of rows in the table, the number corrected and the number
   removed. These numbers must match the table.
5. List every step the workflow names, each with the file or section where it was done, or
   "skipped" and the reason. "No steps skipped" is a claim like any other: it needs this list.

### 6. Hand back
Use this shape, in this order, every section present:

```text
RESULT        <one sentence: the call or the artifact> · <link to the file>
ROUTE         <workflow id and name>, because <the reason> · <skills run, in order> · <fallbacks used>
STEPS         every step the workflow lists: done (file or section) or skipped (reason)
CHECKS        <rows in the table, corrected, removed> · who checked (subagent or fresh pass) · link to NN-check.md · then criterion | pass or fail | evidence line
NEEDS YOUR JUDGMENT
              numbered, specific: the conflict, the trade off, the assumption to confirm
NEXT ACTIONS  one to three, each with an owner
ASSUMPTIONS   every assumption the result depends on
CONFIDENCE    high, medium or low (no other word), and the one reason that most limits it
```

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
| 5 | Checks evidenced | NN-check.md exists for every run, including stops; it was made by an independent pass or says why not; every fact stating sentence of the artifact and the hand back has a row; the reported counts match the table | auto | a missing check file, a fact stating sentence with no row, rows checked against the run's own files, or counts that do not match |
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
