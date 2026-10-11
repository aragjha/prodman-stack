---
name: pm
description: The ProdMan.AI PM SuperSkill, one entry point for product management work. Describe a PM problem in plain words (messy documents, a feature decision, a roadmap, metrics, a PRD, a release, a portfolio) and it turns the request into a decision, picks the matching workflow from the index, runs the specialist skills in order, checks the result against that workflow's criteria, and lists what still needs your judgment. Use whenever someone describes a product management task without naming a specific skill.
disable-model-invocation: false
user-invocable: true
---

# /pm · one entry point for PM work

You describe the problem. This skill decides which specialist skills to run, in what order, and
checks the result before you see it. It never hides a prerequisite, never invents a number, and
stops before anything leaves your machine.

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

### 1. Turn the request into a decision
Write four lines before doing anything else:
- **Decision:** what will be decided with this work, in the user's words where possible.
- **Decider and date:** who decides, and by when ("unknown" is allowed).
- **Done looks like:** the artifact the decision needs (a ranked list, a PRD, a roadmap, a brief).
- **Inputs in hand:** the files, data and access the user actually gave.

If the request has no decision in it (for example "make me a roadmap" with nothing attached), do
not produce a generic artifact. Ask one question that would supply the decision, or state the
assumption you will work under and mark every downstream line that depends on it.

### 2. Fill the context gaps, at most three questions
If `context/PRODUCT.md` is missing and the work depends on the product, ask at most three
questions, choosing from: who the user is, the metric that matters, the hard constraint. If the
user wants you to proceed without answers, list the assumptions instead and continue.

### 3. Route
Open the workflow index and pick the workflow whose problem and required inputs match. Say which
one in a single line, with the reason, for example: "Routing to A01, document chaos to product
clarity, because you have 20 files and need a prioritised plan."
- If two workflows fit in sequence, run both and say so. Never more than two.
- If none fits, use the default chain from PM.md section 4 (frame, gather, decide, produce,
  check) and say "no workflow matched; default chain".
- Never invent a workflow ID that is not in the index.

Then check the workflow's prerequisites against step 1's inputs. For every missing one, say
exactly what is missing, what it blocks, and the fallback. A missing connector (Amplitude, Jira,
Linear) means you work only from data the user provides, and you say so. You never fill a
missing input with plausible content.

### 4. Run the chain
For each skill the workflow lists, in order:
1. If it is a skill in this repo, read `../<skill>/SKILL.md` and follow it.
2. If it is an outside resource from the curated list and it is installed, invoke it. If it is
   not installed, say how to install it in one line, then run the fallback the index gives for
   that step, labelled "fallback, not the original skill".
3. Save the step's output to `outputs/<YYYY-MM-DD>-<workflow id>/<NN>-<step>.md` and carry
   forward only what the next step needs.

Keep a running list of every assumption, conflict and gap found along the way.

### 5. Check before you hand back
Grade the final artifact against the workflow's evaluation criteria and the rubric in PM.md
section 7. For each criterion write pass or fail and the line of the output that proves it.
- Every number and quote must trace to an input file or a cited source. Remove or flag any that do not.
- If a criterion fails, fix it once and re-check. If it still fails, report it as failed. Never
  present a failed check as passed.
- This is a self check for quality, not a score for publication (PM.md section 7).

### 6. Hand back
Use this shape, in this order:

```text
RESULT        <one sentence: the call or the artifact> · <link to the file>
ROUTE         <workflow id and name> · <skills run, in order> · <fallbacks used>
CHECKS        table: criterion | pass or fail | evidence line
NEEDS YOUR JUDGMENT
              numbered, specific: the trade off, the conflict, the assumption to confirm
NEXT ACTIONS  one to three, each with an owner
ASSUMPTIONS   every assumption the result depends on
CONFIDENCE    high, medium or low, and the one reason that most limits it
```

## Rules that override everything above
- Never invent metrics, quotes, customers, users or results. Synthetic data is labelled synthetic.
- Stop before sending, posting, publishing, sharing, editing a real tracker or spending money. Draft it and ask.
- Conflicting sources are shown side by side with both citations. Never pick one silently.
- Plain language. A term a new PM would not know gets one plain sentence the first time it appears.

## VERIFY
**Rung:** Observer · **Irreversible?** no. Every output is a local file. The actions it might
recommend (posting, editing a tracker) are exactly what it must not take.

| # | Check | How | Type | Fails if |
|---|---|---|---|---|
| 1 | Decision first | The four lines of step 1 appear before any artifact content | auto | the artifact starts before the decision is stated |
| 2 | Route named | A workflow ID that exists in the index, or "default chain", with a reason | auto | skills run with no route named, or an ID not in the index |
| 3 | Prerequisites surfaced | Every missing input or connector is named before the chain runs, with its fallback | auto | a missing prerequisite appears only at the end, or not at all |
| 4 | Steps saved | Each step's output exists under `outputs/` and is linked | auto | a step's output exists only in chat |
| 5 | Checks evidenced | Every pass or fail cites a line of the output | auto | a check is asserted without evidence |
| 6 | Nothing invented | Every number, quote and name traces to an input or a cited source | adversarial | any invented metric, quote, customer or result |
| 7 | Judgment list is real | "Needs your judgment" names specific trade offs from this run | adversarial | empty, or generic advice that fits any request |
| 8 | Stops at the line | No send, post, tracker edit or spend happened or was claimed | auto | any external action taken or claimed |

**Red flags (any one = rung 0):**
- Filling a missing input (metrics, interview notes, a connector's data) with plausible content.
- Reporting a failed check as passed.
- Claiming to have posted, sent or updated anything outside the folder.

**Rollback:** delete the run's folder under `outputs/`.

## Example
**Request:** "I have 20 messy product documents. Organise them, find the conflicting requirements,
build a roadmap, and tell me what to prioritise."

**Step 1:** Decision: what to build first next quarter. Decider: the user, date unknown. Done
looks like: a prioritised roadmap with the conflicts resolved or escalated. Inputs: 20 files.

**Step 3:** "Routing to A01 (document chaos to product clarity), then C02 (evidence based
prioritisation), because the files must be reconciled before anything can be ranked."

**Step 6, abridged:** RESULT: three conflicts found, two resolvable from the documents, one needs a
decision from sales; the roadmap ranks five items, two marked low confidence because their only
evidence is one support ticket. NEEDS YOUR JUDGMENT: 1. SSO is a launch requirement in the PRD
and a later phase in the sales notes; the roadmap cannot be final until that is settled.
