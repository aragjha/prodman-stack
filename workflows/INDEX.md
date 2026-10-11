# Workflow index

11 PM use cases. Each one names the problem, what you need, the skills it combines, the steps, how the result is checked, and whether it has actually been tested. The [pm skill](../skills/pm/SKILL.md) reads this file to route your request; you can also pick a workflow yourself and paste its example prompt.

Updated 2026-10-11. Generated from [workflows.json](workflows.json) by [build_index.py](build_index.py); edit the JSON, not this file.

## How honest the tested column is
| Status | Means | Workflows |
|---|---|---|
| blind benchmark | Run against other tools on the same task and graded blind | 1 |
| demo run | Run end to end in a fresh session on synthetic inputs, graded by a separate reviewer | 0 |
| golden set | Its main skill has frozen adversarial inputs; the workflow itself has not been run | 4 |
| untested | Written and checked for completeness only. Treat the first run as a test | 6 |

Outside skills are optional. Each step that uses one also has a fallback the pm skill runs when it is not installed, labelled as a fallback in the output.

## All workflows
| ID | Workflow | Family | Skills | Tested |
|---|---|---|---|---|
| [A01](#a01) | Document chaos to product clarity ★ | Product documentation | pm | untested |
| [B01](#b01) | Research a product decision ★ | Product research | pm, product-research | blind benchmark |
| [C01](#c01) | Idea to roadmap ★ | Roadmapping and planning | pm, product-research | untested |
| [C02](#c02) | Evidence based prioritisation | Roadmapping and planning | pm | untested |
| [D01](#d01) | PRD to product experience ★ | Product design | pm | untested |
| [E01](#e01) | Product analytics to decisions ★ | Analytics and success metrics | pm | untested |
| [F01](#f01) | Write the tests a skill or AI feature must pass | PM evaluations | pm, eval-write | golden set |
| [G01](#g01) | Release and product communication ★ | Delivery and communication | pm, deidentify | untested |
| [G02](#g02) | Launch readiness check | Delivery and communication | pm, launch-minimum | golden set |
| [H01](#h01) | Portfolio from confidential work | Career and portfolio | pm, portfolio-from-work, deidentify | golden set |
| [H02](#h02) | De-identify before you publish | Career and portfolio | deidentify | golden set |

★ flagship demo

## A · Product documentation

### A01
**Document chaos to product clarity** · flagship demo

**Problem.** A pile of product documents written by different people at different times. Nobody knows which requirements are current, where they conflict, or what to build first.

**You need.** 5 to 50 product documents as files in one folder; the decision this should serve, for example next quarter's priorities; optional: context/PRODUCT.md.

**Skills.** [pm](../skills/pm/SKILL.md)

**Steps.**
1. Inventory every document: title, author role, date, type, and whether a later document supersedes it
2. Extract every requirement and claim as one line each, with the file it came from
3. Merge duplicates that say the same thing in different words, keeping every source
4. List every contradiction side by side with both sources; mark which is newer and who decides
5. Mark requirements with no evidence behind them
6. Find themes that appear in three or more independent documents
7. Rank what to build first against the decision, with a confidence tag per item
8. Check the result against the criteria below and list what needs a human decision

**You get.** a document inventory with superseded files marked; a deduplicated requirements list with sources; a conflicts table with both sources and an owner per conflict; a ranked action plan with confidence tags; a needs your judgment list.

**Checked by.** every requirement cites the file it came from; every contradiction shows both sources and is not silently resolved; superseded documents are not used as current; no requirement, date or number appears that is not in the documents; the ranking states the decision it serves.

**Setup.** Claude Code with this repo, as a plugin or a clone; the documents copied into one folder the session can read; no connectors needed.

**Effort.** 20 to 60 minutes of Claude time; 15 minutes of yours to review the conflicts

**Tested.** untested

**Example prompt.**

```text
I have 15 product documents in docs/. Organise them, find the conflicting requirements, and tell me what to build first next quarter.
```

**Example result.** Pending the demo run in examples/demos/A01-document-chaos

**Limits.** it cannot read documents it cannot open, such as a locked Confluence; export them first; it finds conflicts, it does not decide them; very large folders (more than about 50 documents) need to be split.

## B · Product research

### B01
**Research a product decision** · flagship demo

**Problem.** You have a decision to make (build, buy, position, prioritise) and a belief about it, and you need evidence from outside your company before the meeting, not a fifty page report.

**You need.** the decision, in one sentence; what you believe and what would change your mind; optional: what your product is and who it is for.

**Skills.** [pm](../skills/pm/SKILL.md) → [product-research](../skills/product-research/SKILL.md)

**Steps.**
1. Write the decision, the belief and what would change the mind before searching
2. Search for the evidence against the belief first, then for it
3. Read the strongest pages narrowly and quote them word for word
4. Check every quote against its page
5. Make the call, tag how sure each finding is, and name the test that would reverse it

**You get.** a one page research report that makes the call; an evidence file with every quote and link; the test that would reverse the call.

**Checked by.** the report makes a call rather than listing options; every quote matches its source; the counter evidence section exists; every number is quoted word for word.

**Setup.** web search and fetch allowed in Claude Code; python3 for the quote checker.

**Effort.** 3 to 6 minutes of Claude time in our benchmark (2.6 minutes for version 3)

**Tested.** blind benchmark: first of nine on one PM research task, 23 of 25, graded blind by six AI graders, accuracy 75 percent; see evals/benchmarks/2026-10-11-research-head-to-head.md

**Example prompt.**

```text
Should we build AI meeting notes or fix calendar sync reliability next quarter? I believe ops leads want notes because it came up in three QBRs. I'd change my mind if nobody asks for it unprompted in public.
```

**Example result.** evals/benchmarks/2026-10-11-research-head-to-head.md (version 3 scored 23 of 25 on this exact request)

**Limits.** public web only: it cannot read pages behind logins or paywalls; one benchmark task is not proof of every task; version 3 paraphrased one number; version 4 fixes it.

## C · Roadmapping and planning

### C01
**Idea to roadmap** · flagship demo

**Problem.** A rough product idea, real constraints (team, quarter, a revenue goal), and no evidence yet about whether it is the right bet or how to sequence it.

**You need.** the idea in a few paragraphs; constraints: team size, time frame, the goal it must serve; any customer snippets you have.

**Skills.** [pm](../skills/pm/SKILL.md) → [product-research](../skills/product-research/SKILL.md)

**Steps.**
1. Restate the idea as a decision tied to the goal
2. Research the idea against your belief: competitors, demand in the customers' own words, pricing patterns
3. Split the idea into bets, each with the evidence for it and its confidence
4. Score the bets against the goal and the constraints, showing the scores
5. Sequence the bets into a roadmap of outcomes, each with a metric and what would make you drop it
6. Check the roadmap against the criteria below

**You get.** an opportunity assessment; a roadmap of outcomes with metrics and confidence; the evidence behind each bet; what would change the plan.

**Checked by.** every roadmap item names the outcome and the metric it moves; every bet cites its evidence or is marked as an assumption; the sequence respects the stated team and time constraints; outside facts carry a link.

**Setup.** web search and fetch allowed in Claude Code; python3 for the quote checker.

**Effort.** 10 to 30 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
Here's an idea in examples/demos/C01-idea-to-roadmap/input/idea.md. We have two squads for one quarter and the goal is firms adding seats. Is it the right bet, and if so what's the roadmap?
```

**Example result.** Pending the demo run in examples/demos/C01-idea-to-roadmap

**Limits.** market facts are only as good as the public sources found; it cannot size a market without data you provide or it can cite; the roadmap is a proposal for your judgment, not a commitment.

### C02
**Evidence based prioritisation**

**Problem.** A list of candidate features or bets and a meeting where someone will ask why this order, and the honest answer today is gut feel.

**You need.** the candidate list; the goal and the metric it serves; whatever evidence you have per item: tickets, interview notes, data.

**Skills.** [pm](../skills/pm/SKILL.md)

**Steps.**
1. Restate the goal and the metric the ranking serves
2. Attach the evidence to each item and tag its confidence
3. Score each item on impact on the metric, confidence and effort, showing the inputs to every score
4. Rank, then name the two closest calls and what would flip them
5. Check the ranking against the criteria below

**You get.** a ranked list with scores and the inputs behind them; the close calls and what would flip them; the items with no evidence, flagged.

**Checked by.** every score shows its inputs; items with no evidence are flagged, not ranked high on enthusiasm; the ranking names the metric it serves.

**Setup.** Claude Code with this repo; your evidence as files or pasted text.

**Effort.** 10 to 20 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
Rank these eight candidates for next quarter against seat expansion. Evidence is in notes/. Show me the close calls.
```

**Example result.** None yet

**Limits.** the scores are only as good as the evidence you give it; effort estimates should come from your engineers, not from the model.

## D · Product design

### D01
**PRD to product experience** · flagship demo

**Problem.** A PRD exists and design is about to start, but nobody has walked the user flows, the edge cases or the accessibility needs, so the gaps surface in review or in production.

**You need.** the PRD; who the users are; optional: screenshots of the current product.

**Skills.** [pm](../skills/pm/SKILL.md)

**Steps.**
1. Review the PRD: requirements without acceptance criteria, ambiguous lines, missing edge cases, missing accessibility needs
2. Write the main user flows step by step, including the unhappy paths
3. Write acceptance criteria for every requirement that lacks one
4. Write a prototype ready specification: screens, states, empty and error states
5. List the questions only the product owner can answer

**You get.** a PRD gap review; user flows including unhappy paths; acceptance criteria; a prototype ready screen and state specification; open questions for the owner.

**Checked by.** every requirement ends with a testable acceptance criterion; every gap cites the PRD line it comes from; error, empty and edge states are covered; accessibility is addressed; nothing is added to scope without being marked as a suggestion.

**Setup.** Claude Code with this repo; the PRD as a file.

**Effort.** 15 to 30 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
Here's the PRD for our client payment portal in examples/demos/D01-prd-to-experience/input/. Find the gaps, write the flows and acceptance criteria, and give me a spec a designer can prototype from.
```

**Example result.** Pending the demo run in examples/demos/D01-prd-to-experience

**Limits.** it writes a specification, not visual designs; it cannot test with real users; accessibility notes are a starting point, not an audit.

## E · Analytics and success metrics

### E01
**Product analytics to decisions** · flagship demo

**Problem.** A metric moved, someone senior wants to know why by Thursday, and the dashboard shows what happened but not why or what to do.

**You need.** the metrics as a table or export (weekly or daily); the event and metric definitions; the release log or a list of changes in the period.

**Skills.** [pm](../skills/pm/SKILL.md)

**Steps.**
1. Restate the question as a decision: what will be done differently depending on the answer
2. Check the definitions first: did any metric change meaning in the period
3. Find when the movement started and separate it from seasonal or expected dips
4. Line the movement up against releases and other changes; state each candidate cause with its evidence and confidence
5. Design the cheapest test that would confirm or kill the leading cause
6. Write the decision brief with the success metric and guardrail for the fix

**You get.** a diagnosis with candidate causes ranked by evidence; the definitional or seasonal effects ruled out; one experiment with a primary and a guardrail metric; a decision brief.

**Checked by.** every number matches the input data exactly; a definition change is caught before it is read as a trend; causes are stated as hypotheses with evidence, not as facts; the experiment has a primary metric, a guardrail and a stopping rule.

**Setup.** Claude Code with this repo; the data as files; without an analytics connector it works only from what you export.

**Effort.** 15 to 30 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
Activation dropped this quarter. The weekly metrics, definitions and release log are in examples/demos/E01-analytics-to-decisions/input/. Why did it drop and what should we do?
```

**Example result.** Pending the demo run in examples/demos/E01-analytics-to-decisions

**Limits.** it cannot query your analytics tool unless you connect it; correlation with a release is a lead, not proof; small numbers are flagged rather than over read.

## F · PM evaluations

### F01
**Write the tests a skill or AI feature must pass**

**Problem.** You are about to trust an AI skill or ship an AI feature, and nothing checks whether its output is confidently wrong.

**You need.** the skill or feature description and what it promises; examples of good and bad outputs if you have them.

**Skills.** [pm](../skills/pm/SKILL.md) → [eval-write](../skills/eval-write/SKILL.md)

**Steps.**
1. Write the checks the output must pass, each one something an input can fail
2. Write five frozen inputs: one clean control and four traps
3. Map every trap to the check it exercises
4. Freeze the set; it is added to, never edited

**You get.** a checks table; five frozen golden inputs with their traps; a mapping from traps to checks.

**Checked by.** every check can be failed by at least one input; the control is genuinely clean; traps are written down for the grader and stripped before running.

**Setup.** Claude Code with this repo.

**Effort.** 20 to 40 minutes

**Tested.** golden set: eval-write has its own five frozen inputs in evals/golden-sets/eval-write

**Example prompt.**

```text
Write the golden set for our AI ticket summariser. It promises to keep every customer commitment and never invent a date.
```

**Example result.** evals/golden-sets/pm (the golden set for this repo's own pm skill)

**Limits.** it writes the tests; running and grading them is a separate step; a test set is only as adversarial as the traps you can imagine.

## G · Delivery and communication

### G01
**Release and product communication** · flagship demo

**Problem.** A release is ready and four audiences need four different messages, written from tickets that include unmerged work, a breaking change and a known issue.

**You need.** the release scope with ticket status; who reads the notes: admins, end users, API partners; known issues.

**Skills.** [pm](../skills/pm/SKILL.md) → [deidentify](../skills/deidentify/SKILL.md)

**Steps.**
1. Confirm what actually shipped: exclude anything not merged
2. Find breaking changes and known issues and put them first for the people they affect
3. Write the release notes, then one message per audience
4. Run deidentify on anything public
5. Write the go live checklist and stop for approval before anything is posted

**You get.** release notes; one message per audience; a go live checklist; everything marked DRAFT until approved.

**Checked by.** no unmerged ticket appears as shipped; breaking changes are flagged to the audience they break; known issues are listed; nothing was posted, sent or closed.

**Setup.** Claude Code with this repo; the ticket list as a file; no Slack or Jira connector is needed, and none is used.

**Effort.** 10 to 20 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
Release 4.2 scope and our audiences are in examples/demos/G01-release-comms/input/. Write the release notes and the announcements, and the go live checklist.
```

**Example result.** Pending the demo run in examples/demos/G01-release-comms

**Limits.** it drafts; you post; it trusts the ticket status you give it.

### G02
**Launch readiness check**

**Problem.** A launch feels nearly ready and keeps slipping, because nobody has checked the few things that must exist against evidence rather than intention.

**You need.** what exists today for the launch: page, capture, payment, delivery, measurement.

**Skills.** [pm](../skills/pm/SKILL.md) → [launch-minimum](../skills/launch-minimum/SKILL.md)

**Steps.**
1. Assess each of the eight things with evidence: a URL, a file or a transaction
2. List the gaps in funnel order
3. Size the smallest fix for each gap in minutes or hours
4. Give a verdict: go today, or a dated plan

**You get.** an eight item audit with evidence; gaps in funnel order with sized fixes; a verdict.

**Checked by.** every ready item cites evidence; a partial item counts as missing; the verdict is go or a date, never nearly.

**Setup.** Claude Code with this repo.

**Effort.** 10 minutes

**Tested.** golden set: evals/scoreboards/launch-minimum.md

**Example prompt.**

```text
We launch Friday. Here's what we have. Are we ready?
```

**Example result.** evals/scoreboards/launch-minimum.md

**Limits.** it checks that things exist, not that they are good; an untested payment path is always a gap.

## H · Career and portfolio

### H01
**Portfolio from confidential work**

**Problem.** Years of shipped work you cannot show because the documents belong to your employer and the details are confidential.

**You need.** your memory of two or three projects; anything you are allowed to keep.

**Skills.** [pm](../skills/pm/SKILL.md) → [portfolio-from-work](../skills/portfolio-from-work/SKILL.md) → [deidentify](../skills/deidentify/SKILL.md)

**Steps.**
1. Interview you about the decisions you made, from memory
2. Write each case study around the decision, not the logo
3. De-identify, and show exactly what was stripped
4. Assemble a portfolio page you can send

**You get.** two or three de-identified case studies; a de-identification log; a portfolio page.

**Checked by.** no employer, customer or traceable number survives; every case study centres on a decision you made; what was stripped is shown.

**Setup.** Claude Code with this repo.

**Effort.** about one hour for a first pass

**Tested.** golden set: evals/golden-sets/portfolio-from-work and evals/golden-sets/deidentify

**Example prompt.**

```text
Turn my last two projects into case studies I can send to a recruiter. I don't have the documents anymore.
```

**Example result.** examples/worked-example.md

**Limits.** it cannot judge your NDA for you; when unsure it flags and stops; your memory is the source, so check every claim.

### H02
**De-identify before you publish**

**Problem.** You want to post, talk or demo real work, and one employer name or customer number could cost you more than the post is worth.

**You need.** the draft: a post, case study, talk or demo script.

**Skills.** [deidentify](../skills/deidentify/SKILL.md)

**Steps.**
1. Find employers, customers, colleagues, traceable numbers and identifying details
2. Replace or generalise each one, keeping the point of the sentence
3. Show every change, and flag what it is unsure about instead of guessing

**You get.** the cleaned draft; a change log; a list of flagged items for you to decide.

**Checked by.** nothing identifying survives; every change is shown; uncertain items are flagged, not guessed.

**Setup.** Claude Code with this repo.

**Effort.** 2 to 5 minutes

**Tested.** golden set: evals/golden-sets/deidentify

**Example prompt.**

```text
Check this LinkedIn post before I publish it. It mentions a project from my last job.
```

**Example result.** None yet

**Limits.** it cannot know what your contract allows; shape can identify a company even with the name removed; it flags this but cannot guarantee it.
