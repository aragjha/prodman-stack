---
name: product-research
description: Research a product decision and tell the PM what to do. Writes down the decision, the belief and what would change the PM's mind before searching, looks for the evidence against the belief first, checks every quote against the real page, and returns a short plain report that makes the call and names the test that would reverse it. Use before a feature, a roadmap bet, a positioning call or a build or buy decision.
disable-model-invocation: false
user-invocable: true
---

# /product-research · makes the call, and argues against you first

Most research ends in "themes" and changes nothing. Most AI research also agrees with you: tell a
model what you believe and it leans your way (Wang et al., arXiv 2508.02087: "first-person prompts
(``I believe...'') consistently induce higher sycophancy rates than third-person framings (``They
believe...'')"). This skill does the opposite, and stays short.

**You get two files.** `REPORT.md` is what the PM reads: plain words, under 1,000 words, links inline.
`EVIDENCE.md` is the audit trail: the starting position, every source with how it was checked, the
quote check, and the sweep. The PM never has to open it; anyone who doubts the report can.

## Inputs
- The question and the decision it feeds. **If there is no decision, ask once and wait.** Everything
  else (belief, goal number, what would change their mind) you may draft, marked *not confirmed*.

## Steps

### 1. Write the starting position, before any search
At the top of `EVIDENCE.md`, with the time:
- **Decision:** what will be chosen differently depending on the answer.
- **Goal:** the number the decision should move. From the PM, never from the web.
- **Belief:** written in the third person ("The PM believes ops leads want notes"), never "I believe".
  Split a two part belief into B1 and B2.
- **What would change their mind:** the finding that would make the PM drop the belief.

If the PM wants only supporting evidence, say once that the report will still show what goes against
the belief, then carry on.

### 2. Plan five angles
1. **Goal and limits:** what the number is, and what constrains the options (rules, platforms, cost).
2. **The alternatives:** who already solves this, how, at what price, and whether people actually use it.
3. **The users' own words:** how the people affected describe the problem, unprompted.
4. **What the PM books predict:** see the short card below. A framework is a prediction to test, never
   evidence.
5. **Reach:** where the users are, only if the decision depends on it.

Write the search keys for each angle, **the ones that could prove the belief wrong first**
("<feature> nobody used", "<feature> shut down", "why we stopped <X>").

### 3. Search and open
- Open the page. A search snippet is not a source.
- Stop at about 15 sources, or when every angle has an answer. More is not better.
- Record each source in `EVIDENCE.md`, one line: `S# | angle | exact quote | URL | date read | how checked`
  where how checked is **read on the page**, **second hand** (a credible report of it), **not checked**
  (could not open), **searched, nothing found** (give the search), or **from the PM**.
- Quotes are copied character for character. A cut is shown with "…", only between whole sentences.

### 4. Prove the quotes
Run `python3 verify_quotes.py EVIDENCE.md`. Fix every line it flags, or downgrade that source to
second hand. Then run `python3 verify_quotes.py --crosscheck REPORT.md EVIDENCE.md` once the report is
written: every quote in the report must appear exactly in the evidence file.

### 5. Sweep, then decide
In `EVIDENCE.md`, list every source that **weakens** the belief, judging by what it says, not by what
you hoped. Every one of them must appear in the report, or be listed as dropped with a reason.
Then decide.

### 6. Write REPORT.md
Plain sentences. No source codes, no internal labels, no tables of tables. Links go inline next to the
claim. Never use the words "falsifier", "angle" or "sweep" in the report. No dashes as connectors.

```markdown
# <the question, in the PM's words>

## The call
<One or two sentences: what to do. Make the call even if the evidence is thin; say how thin.>

## What would change this call
<The one test, with a number, that would reverse it, and where to get it. Example: "If 3 of the 5 QBR
accounts name a new person who would need a seat for notes, revisit this.">

## What you believed, and what the evidence did to it
- **<belief, plain>:** held / did not hold / still unknown. <one line why, with a link>

## What we found
1. **<insight as a short claim>** <one or two lines of evidence with the link inline>
   *What it changes:* <one line>
(4 or 5 of these, ordered by how much they move the goal)

## What the PM books predict
- **<framework>:** predicts <x> here. The evidence <agreed / disagreed / could not say>.
(two or three only, the ones that bear on this decision)

## What we could not check
- <each thing the PM should know is unverified, in one line>

## Next step
<one sentence>
```

### 7. Hand back
Show the PM the call, the test that would change it, and the path to both files. Nothing else.

## The short PM books card
| Framework | Predicts | Misuse to avoid |
|---|---|---|
| Jobs to be Done (Christensen) | what people really hire a product to get done, and what they fire for it | listing features as jobs |
| Kano | whether shipping a feature earns anything or only stops losses | judging from competitor counts; Kano needs customer answers |
| The four big risks (Cagan) | which of value, usability, feasibility, viability is still open | filing legal or platform rules under feasibility (they are viability); treating rivals' adoption as proof of your value |
| Obviously Awesome (Dunford) | what to position on: the thing alternatives cannot do | citing it for numbers |
| Opportunity solution tree (Torres) | whether the solution came before the problem was mapped | name dropping it |
| The Mom Test (Fitzpatrick) | how to get honest evidence: ask about past behaviour | treating it as a theory of markets |
| Crossing the Chasm (Moore) | whether you are selling to early adopters or the pragmatic majority | calling an existing customer base a beachhead |

`FRAMEWORKS.md` in this folder has the longer version if a decision needs a framework not listed.

## VERIFY
**Rung:** Observer, earned only from the scoreboard · **Irreversible?** no.

| # | Check | How | Type | Fails if |
|---:|---|---|---|---|
| 1 | Starting position first | Decision, belief and what would change the PM's mind are timed earlier than the first source | auto | missing or later |
| 2 | Every source recorded with how it was checked | Each `EVIDENCE.md` line has a URL or a search and a how checked value | auto | any line missing either |
| 3 | Quotes exact | `verify_quotes.py` and the crosscheck report nothing to fix | auto | anything flagged and left |
| 4 | Report is short and plain | `REPORT.md` under 1,000 words, no source codes, no internal labels | auto | over, or codes present |
| 5 | Every weakening source in the report | The sweep list in the evidence file is fully covered in the report or dropped with a reason | adversarial | a weakening source silently missing |
| 6 | Makes the call and names the reversing test | The call is a choice; the test has a number and a place to get it | adversarial | no call, or a test with no number |
| 7 | Books used as predictions | Each framework line says what it predicts and whether the evidence agreed; none counted as evidence | adversarial | name dropping, or a framework cited as proof |
| 8 | A PM can read it in five minutes | A reader with no context understands the call and why | adversarial | the reader has to decode anything |

**Red flags (any one = rung 0):** an invented source, quote or number · searching before the starting
position is written · raising a confidence to suit the request · getting past a login or a bot wall.

## Example
`/product-research should we build AI meeting notes or fix calendar sync for next quarter's two engineers? I believe ops leads want notes; I'd change my mind if nobody asks for it unprompted.`
