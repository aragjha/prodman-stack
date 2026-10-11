---
name: product-research
description: Research a product decision and tell the PM what to do. Writes down the decision, the belief and what would change the PM's mind before searching, looks for the evidence against the belief first, checks every quote against the real page, and returns a short plain report that makes the call, shows how sure each finding is, and names the test that would reverse it. Use before a feature, a roadmap bet, a positioning call or a build or buy decision.
disable-model-invocation: false
user-invocable: true
---

# /product-research · makes the call, and argues against you first

Most research ends in "themes" and changes nothing. Most AI research also agrees with you: written
"I believe…", a belief makes a model lean your way (arXiv 2508.02087). This skill writes the belief in
the third person, hunts for evidence against it first, and makes a call.

**Output:** `REPORT.md` (what the PM reads, plain, under 900 words, links inline) and `EVIDENCE.md`
(the audit trail). Nothing else.

## Work lean: this skill has a budget
Every extra step costs tokens and time, so:
- **Batch.** Send all searches in one turn, as parallel calls. Fetch pages in at most two parallel batches.
- **At most 8 searches and 10 page reads.** Stop earlier if each part of the plan has an answer.
- **Read narrowly.** Use WebFetch with a prompt asking for the exact sentences or numbers you need.
  Never pull a whole page into the conversation with curl.
- **Write each file once.** No drafts, no rereading your own files.
- **Do not open FRAMEWORKS.md** unless a framework you need is missing from the card below.
- **Check quotes in one command** at the end (step 5).

## Steps

### 1. First turn: starting position plus all searches, together
In one turn, in parallel:
- **Write `EVIDENCE.md`** with the time and the starting position:
  **Decision** (what changes depending on the answer) · **Goal** (the number; from the PM, never the
  web) · **Belief** in the third person ("The PM believes…"), split into B1 and B2 if it has two parts ·
  **What would change their mind**. If the decision is missing, ask once and stop.
- **Run every search.** Cover four things: the alternatives and their prices; real usage or failure
  of the idea where it has shipped; the affected users' own words; and any limits (rules, platforms,
  cost). **Put the searches that could prove the belief wrong first** ("<feature> nobody used",
  "<feature> shut down", "why we stopped <X>").

### 2. Second turn: read the best pages, in one parallel batch
Pick the 6 to 10 results most likely to change the call. Fetch them together with narrow prompts.
A search snippet is not a source; if a page will not open, say so and move on.

### 3. Decide, using the PM books as predictions
Write down, for yourself, every finding that **weakens** the belief, judged by what it says. Then use
two or three frameworks from the card as predictions to test, never as evidence. Then make the call.
Make it even if the evidence is thin, and say how thin.

**Never write "only", "first", "nobody" or "cannot be copied"** unless you searched for the
counterexample. If you did, say what you searched.

### 4. Write both files, once each
**`EVIDENCE.md`** (overwrite, keeping the starting position and its time): one line per source,
`S# | exact quote | URL | how checked`, where how checked is **read on the page**, **vendor's own
number**, **second hand**, **searched, nothing found** (give the search) or **from the PM**. Copy quotes
character for character; show cuts with "…" only between whole sentences. Then list the sources that
weaken the belief, and for each: where it appears in the report, or why it was dropped.

**`REPORT.md`**, plain words, no source codes, no dashes as connectors:

```markdown
# <the question, in the PM's words>

## The call
<One or two sentences: what to do, and how strong the evidence is.>

## What would change this call
<One test with a number, and where to get the answer.>

## What you believed, and what happened to it
- **<belief>:** held / did not hold / still unknown. <one line, with a link>

## What we found
| What we found | The evidence | How sure |
|---|---|---|
| <short claim> | <one line with the link inline> | checked on the page / vendor's own number / one source only |
(4 to 6 rows, ordered by how much they move the goal)

**What it changes:** <two or three short lines, one per key row>

## What the PM books predict
- **<framework>:** predicts <x> here; the evidence <agreed / disagreed / could not say>.

## What we could not check
- <one line each>

## Next step
<one sentence>
```

### 5. Check the quotes, once
`python3 verify_quotes.py EVIDENCE.md --report REPORT.md`
Fix anything it flags with a single edit, or downgrade that source to second hand. Then hand back:
the call, the test that would change it, and the two file paths.

## The PM books card
| Framework | Predicts | Do not |
|---|---|---|
| Jobs to be Done (Christensen) | what people really hire a product for, and what they fire to hire it | list features as jobs |
| Kano | whether shipping it earns anything or only stops losses | judge from competitor counts; Kano needs customer answers |
| The four big risks (Cagan) | which of value, usability, feasibility, viability is still open | file legal or platform rules under feasibility (they are viability); treat rivals' adoption as proof of your value |
| Obviously Awesome (Dunford) | what to position on: what alternatives cannot do | cite it for numbers |
| Opportunity solution tree (Torres) | whether the solution came before the problem was mapped | name drop it |
| The Mom Test (Fitzpatrick) | how to get honest evidence: ask about past behaviour | treat it as a theory of markets |
| Crossing the Chasm (Moore) | early adopters or the pragmatic majority | call an existing customer base a beachhead |

## VERIFY
**Rung:** Observer, earned only from the scoreboard · **Irreversible?** no.

| # | Check | How | Type | Fails if |
|---:|---|---|---|---|
| 1 | Starting position first | It is the first thing written, with a time | auto | missing |
| 2 | Every source has a URL or search and a how checked value | Read `EVIDENCE.md` | auto | any line missing either |
| 3 | Quotes exact | The one command reports nothing left to fix | auto | anything flagged and left |
| 4 | Short and plain | `REPORT.md` under 900 words, no source codes | auto | over, or codes present |
| 5 | Every finding shows how sure it is | Each row of the findings table has a how sure value | auto | any blank |
| 6 | Every weakening source appears or is dropped with a reason | Compare the list in the evidence file with the report | adversarial | one silently missing |
| 7 | Makes the call and names a test with a number | Read the first two sections | adversarial | no call, or a test with no number |
| 8 | No unchecked "only", "first", "nobody" | Each such claim names the search behind it | adversarial | one unsupported |
| 9 | Lean | Under 100,000 tokens for the run | auto | over |

**Red flags (any one = rung 0):** an invented source, quote or number · searching before the starting
position is written · raising a confidence to suit the request · getting past a login or a bot wall.

## Example
`/product-research should we build AI meeting notes or fix calendar sync for next quarter's two engineers? I believe ops leads want notes; I'd change my mind if nobody asks for it unprompted.`
