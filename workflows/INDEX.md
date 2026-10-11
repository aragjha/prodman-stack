# Workflow index

56 PM use cases. Each one names the problem, what you need, the skills it combines, the steps, how the result is checked, and whether it has actually been tested. The [pm skill](../skills/pm/SKILL.md) reads this file to route your request; you can also pick a workflow yourself and paste its example prompt.

Updated 2026-10-11. Generated from [workflows.json](workflows.json) by [build_index.py](build_index.py); edit the JSON, not this file.

## How honest the tested column is
| Status | Means | Workflows |
|---|---|---|
| blind benchmark | Run against other tools on the same task and graded blind | 1 |
| demo run | Run end to end in a fresh session on synthetic inputs, graded by a separate reviewer | 5 |
| golden set | Its main skill has frozen adversarial inputs; the workflow itself has not been run | 6 |
| untested | Written and checked for completeness only. Treat the first run as a test | 44 |

Outside skills are optional. Each step that uses one also has a fallback the pm skill runs when it is not installed, labelled as a fallback in the output.

## All workflows
| ID | Workflow | Family | Skills | Tested |
|---|---|---|---|---|
| [A01](#a01) | Document chaos to product clarity ★ | Product documentation | pm | demo run |
| [A02](#a02) | Scattered documents to a product knowledge base | Product documentation | pm, search-company-knowledge | untested |
| [A03](#a03) | Notes to a first PRD | Product documentation | pm, write-spec | untested |
| [A04](#a04) | Decision log from meetings and threads | Product documentation | pm, summarize-meeting | untested |
| [A05](#a05) | Resolve contradictory specs | Product documentation | pm, search-company-knowledge | untested |
| [B01](#b01) | Research a product decision ★ | Product research | pm, product-research | blind benchmark |
| [B02](#b02) | Competitor comparison you can defend | Product research | pm, product-research, competitive-brief | golden set |
| [B03](#b03) | Market size from the bottom up | Product research | pm, product-research | golden set |
| [B04](#b04) | Interview synthesis | Product research | pm, interview-snapshot, synthesize-research | untested |
| [B05](#b05) | Opportunity discovery for an outcome | Product research | pm, opportunity-solution-tree, discover-opportunities | untested |
| [B06](#b06) | Jobs to be done from switching stories | Product research | pm, customer-interviews | untested |
| [B07](#b07) | Evidence backed problem statement | Product research | pm, brief | untested |
| [C01](#c01) | Idea to roadmap ★ | Roadmapping and planning | pm, product-research | demo run |
| [C02](#c02) | Evidence based prioritisation | Roadmapping and planning | pm | untested |
| [C03](#c03) | Feature roadmap to outcome roadmap | Roadmapping and planning | pm, outcome-roadmap | untested |
| [C04](#c04) | Quarterly plan that fits the team | Roadmapping and planning | pm, brainstorm-okrs | untested |
| [C05](#c05) | Sprint preparation | Roadmapping and planning | pm, sprint-planning, deliver-acceptance-criteria | untested |
| [C06](#c06) | Dependencies and risks before you commit | Roadmapping and planning | pm, pre-mortem | untested |
| [C07](#c07) | Stakeholder alignment before the plan is final | Roadmapping and planning | pm, stakeholder-mapping | untested |
| [D01](#d01) | PRD to product experience ★ | Product design | pm | demo run |
| [D02](#d02) | User journey map from evidence | Product design | pm, customer-journey-map, compare-user-journeys | untested |
| [D03](#d03) | Information architecture review | Product design | pm, figma-generate-diagram | untested |
| [D04](#d04) | UX evaluation before build | Product design | pm, design-critique, accessibility-review | untested |
| [D05](#d05) | Usability review from test sessions | Product design | pm, replay-ux-audit | untested |
| [E01](#e01) | Product analytics to decisions ★ | Analytics and success metrics | pm | demo run |
| [E02](#e02) | North star metric and KPI tree | Analytics and success metrics | pm, metrics | untested |
| [E03](#e03) | Activation and conversion funnel | Analytics and success metrics | pm, analyze, compare-user-journeys | untested |
| [E04](#e04) | Retention by cohort | Analytics and success metrics | pm, cohort-analysis | untested |
| [E05](#e05) | Experiment from design to readout | Analytics and success metrics | pm, experiment, statistical-analysis | untested |
| [E06](#e06) | Feature adoption | Analytics and success metrics | pm, measure-instrumentation-spec, cohort-analysis | untested |
| [E07](#e07) | Monthly product performance review | Analytics and success metrics | pm, metrics-review, saas-revenue-growth-metrics | untested |
| [F01](#f01) | Write the tests a skill or AI feature must pass | PM evaluations | pm, eval-write | golden set |
| [F02](#f02) | PRD quality score | PM evaluations | pm, spec, critique | untested |
| [F03](#f03) | Roadmap quality review | PM evaluations | pm, critique | untested |
| [F04](#f04) | Research credibility check | PM evaluations | pm, product-research, critique | untested |
| [F05](#f05) | Strategy completeness review | PM evaluations | pm | untested |
| [F06](#f06) | Release go or no go | PM evaluations | pm | untested |
| [F07](#f07) | Check AI generated work against its inputs | PM evaluations | pm | untested |
| [G01](#g01) | Release and product communication ★ | Delivery and communication | pm, deidentify | demo run |
| [G02](#g02) | Launch readiness check | Delivery and communication | pm, launch-minimum | golden set |
| [G03](#g03) | Weekly status report from the tracker | Delivery and communication | pm, generate-status-report, internal-comms | untested |
| [G04](#g04) | Risk summary for the people who can act | Delivery and communication | pm | untested |
| [G05](#g05) | Post launch review | Delivery and communication | pm, metrics-review | untested |
| [H01](#h01) | Portfolio from confidential work | Career and portfolio | pm, portfolio-from-work, deidentify | golden set |
| [H02](#h02) | De-identify before you publish | Career and portfolio | deidentify | golden set |
| [H03](#h03) | PM interview preparation | Career and portfolio | pm, deidentify, product-sense-interview-answer | untested |
| [H04](#h04) | Product teardown | Career and portfolio | pm, product-research | untested |
| [H05](#h05) | Skills gap to learning plan | Career and portfolio | pm, career, director-readiness-advisor | untested |
| [I01](#i01) | Evals from your AI feature's real outputs | AI product work | pm, eval-write, error-discovery, validate-evaluator | untested |
| [I02](#i02) | Prompt or agent spec | AI product work | pm, eval-write, skill-creator | untested |
| [I03](#i03) | Choose between models with a test | AI product work | pm, eval-write, generate-synthetic-data, write-judge-prompt | untested |
| [I04](#i04) | AI feature risk review | AI product work | pm, eval-write, eval-plan | untested |
| [J01](#j01) | Executive update that asks for something | Stakeholders and leadership | pm, exec-comms | untested |
| [J02](#j02) | Decision memo when leaders disagree | Stakeholders and leadership | pm, decide | untested |
| [J03](#j03) | Saying no with evidence | Stakeholders and leadership | pm | untested |
| [J04](#j04) | One on one preparation | Stakeholders and leadership | pm, meeting-prep | untested |

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

**Tested.** demo run: run 2026-10-11 with skill version 2 on synthetic inputs, graded by a separate reviewer with an answer key: 9 of 10 answer key criteria, but failed 2 of 8 checks: customer quotes shortened without an ellipsis, and the self check covered 13 of 35 quotes. Rerun the same day with version 3: key 8 of 10, 1 red flag; both failed the skill's own checks. See examples/demos/A01-document-chaos/run-2026-10-11/GRADE.md

**Example prompt.**

```text
I have 15 product documents in docs/. Organise them, find the conflicting requirements, and tell me what to build first next quarter.
```

**Example result.** examples/demos/A01-document-chaos/run-2026-10-11/ (unedited outputs and the grade)

**Limits.** it cannot read documents it cannot open, such as a locked Confluence; export them first; it finds conflicts, it does not decide them; very large folders (more than about 50 documents) need to be split.

### A02
**Scattered documents to a product knowledge base**

**Problem.** Product knowledge lives in old PRDs, wiki pages, slide decks and chat threads. New teammates ask the same questions every week, and two people looking for the same answer find different versions of it.

**You need.** the documents as files in one folder, exported from wherever they live; who the knowledge base is for, for example new engineers or the support team; optional: the questions people ask most often; optional: context/PRODUCT.md.

**Skills.** [pm](../skills/pm/SKILL.md) → [search-company-knowledge](https://github.com/atlassian/atlassian-mcp-server/blob/main/skills/search-company-knowledge/SKILL.md) (outside, optional)

**Steps.**
1. Inventory every document: title, owner, date, type, and whether a newer document replaces it
2. List the questions the knowledge base must answer, starting from the questions people actually ask
3. Group the content into topics, with one canonical page per topic that says what is current and links every source
4. Mark superseded documents as replaced, and name the page that replaces each one
5. Write a glossary of internal terms and abbreviations, each defined from a document rather than from general knowledge
6. List the gaps: questions no document answers, and topics where the documents disagree
7. Check every page against the criteria below and list what an owner needs to confirm

**You get.** an index page that routes each common question to one page; one canonical Markdown page per topic, each linking its sources; a glossary of internal terms; a list of superseded documents and what replaces each; a gaps and conflicts list with a suggested owner for each.

**Checked by.** every statement on a canonical page links the document it came from; superseded documents are never presented as current; where documents disagree, both versions are shown and neither is silently picked; every common question routes to exactly one page or appears in the gaps list; no glossary term is defined from outside the documents unless it is marked as general knowledge.

**Setup.** Claude Code with this repo, as a plugin or a clone; the documents exported into one folder the session can read; optional, for search-company-knowledge: an Atlassian Cloud site and Atlassian's plugin, which carries its skills and its MCP server (/plugin marketplace add atlassian/atlassian-mcp-server, then /plugin install atlassian@atlassian, then sign in with /mcp), though an admin may need to allow the connection; optional, if the documents live in Notion: the Notion MCP server instead of an export, which needs a Notion account (claude mcp add --transport http notion https://mcp.notion.com/mcp, then sign in with /mcp).

**Effort.** 20 to 45 minutes of Claude time for about 30 documents; 20 minutes of yours to confirm owners and conflicts

**Tested.** untested

**Example prompt.**

```text
Our product knowledge is spread across old PRDs, a wiki and Slack threads, and I've exported all of it to docs/. Turn it into a knowledge base new engineers can use in their first week, and tell me what's missing.
```

**Example result.** None yet

**Limits.** it organises what the documents say and cannot tell which unwritten team habits are current; documents it cannot open, such as a locked wiki space, are listed rather than guessed at; a knowledge base goes stale unless someone owns it, and while the gaps list suggests owners, you assign them; exports of more than about 50 documents need to be split by area.

Fallback for search-company-knowledge: The pm skill works only from the files in the folder. It lists every document it was told about but could not read.

### A03
**Notes to a first PRD**

**Problem.** A feature has been discussed in meetings, chat threads and customer calls for weeks. Everyone thinks the requirements are agreed, but nobody has written them down, and the first draft keeps slipping.

**You need.** the notes: meeting notes, chat exports, call notes and any sketches, as files; the decision the PRD serves, for example whether engineering starts next sprint; optional: context/PRODUCT.md and context/DECISIONS.md.

**Skills.** [pm](../skills/pm/SKILL.md) → [write-spec](https://github.com/anthropics/knowledge-work-plugins/blob/main/product-management/skills/write-spec/SKILL.md) (outside, optional)

**Steps.**
1. Extract every problem statement, requirement, decision, open question and number from the notes, one line each, with the note it came from
2. Separate what was decided from what was only suggested, and record who decided wherever the notes say so
3. Merge lines that say the same thing, keeping every source
4. Draft the PRD: the problem, who has it and the evidence, goals and non goals, requirements with testable acceptance criteria, success and guardrail metrics, risks and open questions
5. Write unknown wherever the notes are silent, such as a baseline, a target or an owner, and add each one to the open questions
6. Check the draft against the criteria below and mark it DRAFT

**You get.** a first PRD draft marked DRAFT; a table linking each requirement to the note it came from; a list of suggestions that were never decided; open questions, each with who can answer it.

**Checked by.** every requirement cites the note it came from; nothing that was only suggested appears as a decided requirement; every requirement has a testable acceptance criterion or is listed as an open question; no baseline, target, date or owner appears that is not in the notes; non goals are named.

**Setup.** Claude Code with this repo, as a plugin or a clone; the notes as files in one folder; optional: Anthropic's product management plugin for write-spec (claude plugin marketplace add anthropics/knowledge-work-plugins, then claude plugin install product-management@knowledge-work-plugins), which registers remote connectors that read nothing until you sign in to one.

**Effort.** 10 to 25 minutes of Claude time; 20 minutes of yours on the open questions

**Tested.** untested

**Example prompt.**

```text
We've talked about bulk export for a month. The meeting notes, the Slack thread and two customer call notes are in notes/. Write the first PRD so engineering can start next sprint, and tell me what we still haven't decided.
```

**Example result.** None yet

**Limits.** the PRD can only be as complete as the notes, so topics the notes never cover become open questions rather than content; it cannot tell whether a decision in the notes was later reversed somewhere else; effort and dates must come from your engineers; it drafts, and you own the PRD and circulate it.

Fallback for write-spec: The pm skill drafts the PRD itself from the PRD template in PM.md section 5, with the same link from every requirement to its note.

### A04
**Decision log from meetings and threads**

**Problem.** Decisions get made in meetings and chat threads and are never written down. Three months later someone reopens a settled question, and nobody can say who decided it or why.

**You need.** meeting notes, transcripts or chat exports from the period, as files; optional: an existing decision log, or context/DECISIONS.md.

**Skills.** [pm](../skills/pm/SKILL.md) → [summarize-meeting](https://github.com/phuryn/pm-skills/blob/main/pm-execution/skills/summarize-meeting/SKILL.md) (outside, optional)

**Steps.**
1. Read every source and pull out each line where something was decided, quoting it with its source and date
2. Sort each item as decided, proposed or only discussed, and keep only the decided ones in the log
3. For each decision record the date, the decision, who decided, why, the evidence mentioned, and whether it can be reversed
4. Flag decisions with no named decider, and decisions that reverse an earlier one, linking the two
5. Write the log, or append to the existing one, in the format of context/DECISIONS.md without changing existing entries
6. List what needs confirmation: unclear deciders, decisions that seem to conflict, and decisions with no reason given

**You get.** a decision log with date, decision, decider, reason, evidence, reversibility and source for each entry; a list of proposals that were never decided; a list of reversed or conflicting decisions; a needs confirmation list.

**Checked by.** every entry quotes or links the source line where the decision was made; no decider, date or reason appears that is not in the sources; proposals and discussions are not logged as decisions; existing log entries are kept unchanged; every reversal links the decision it reverses.

**Setup.** Claude Code with this repo, as a plugin or a clone; the notes or transcripts as files; optional: Pawel Huryn's pm-execution plugin for summarize-meeting (claude plugin marketplace add phuryn/pm-skills, then claude plugin install pm-execution@pm-skills), but Dean Peters' collection uses the same marketplace name, pm-skills, so adding both can clash; context/DECISIONS.md, which stays on your machine because git ignores it.

**Effort.** 10 to 20 minutes of Claude time for a month of notes; 10 minutes of yours to confirm deciders

**Tested.** untested

**Example prompt.**

```text
We keep reopening decisions about the pricing page. The last six weeks of meeting notes and the Slack export are in notes/. Build me a decision log so we stop arguing about things we already settled.
```

**Example result.** None yet

**Limits.** it logs only decisions someone wrote down, so decisions made in a hallway are invisible to it; when speakers are not labelled in a transcript, the decider is unknown, and it says so; it records decisions without judging whether they were right.

Fallback for summarize-meeting: The pm skill reads each transcript itself and extracts only the lines where a decision was stated, quoting them.

### A05
**Resolve contradictory specs**

**Problem.** Two specs, or a spec and a later decision, say different things about the same requirement. Engineering is blocked or building one version while sales promises the other, and someone has to decide this week.

**You need.** the conflicting documents; who can decide each conflict, if you know; optional: context/DECISIONS.md or another decision log, to check for a later decision.

**Skills.** [pm](../skills/pm/SKILL.md) → [search-company-knowledge](https://github.com/atlassian/atlassian-mcp-server/blob/main/skills/search-company-knowledge/SKILL.md) (outside, optional)

**Steps.**
1. Quote each contradiction from both sources, word for word, with their dates and authors
2. Check whether a later document or logged decision already settles it; if one does, cite it and close that item
3. For each open contradiction, trace both sides to their evidence and their owner
4. Write what each option means for scope, dates, customers already promised something, and cost, marking estimates as estimates
5. Recommend one option with a confidence tag, name who decides, and write the question to put to them
6. After the decision, produce the reconciled spec with a change note, and add the decision to the decision log

**You get.** a conflict brief with both sources quoted side by side; what each option means for scope, dates, customers and cost; a recommendation and the question for the decider; after the decision, a reconciled spec with a change note.

**Checked by.** both sides of every conflict are quoted exactly, with their sources; no conflict is settled by the model's preference, because a named person decides; a conflict that a later decision already settles cites that decision; the reconciled spec changes only what the decision covers, and the change note lists every change.

**Setup.** Claude Code with this repo, as a plugin or a clone; the documents as files; optional, for search-company-knowledge: an Atlassian Cloud site and Atlassian's plugin, which carries its skills and its MCP server (/plugin marketplace add atlassian/atlassian-mcp-server, then /plugin install atlassian@atlassian, then sign in with /mcp), though an admin may need to allow the connection.

**Effort.** 10 to 20 minutes of Claude time per batch of conflicts; the decisions are yours

**Tested.** untested

**Example prompt.**

```text
The v2 PRD says only admins can export, but the sales FAQ and last week's design review say every user can. Engineering starts Monday. Lay out the conflict and tell me who needs to decide what.
```

**Example result.** None yet

**Limits.** it recommends but never decides a conflict for you; it cannot know about spoken agreements that were never written down; what an option means for dates and cost stays an estimate until engineering confirms it.

Fallback for search-company-knowledge: The pm skill checks only the documents and decision log you provide, and says that a later decision may exist elsewhere.

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

### B02
**Competitor comparison you can defend**

**Problem.** Sales or leadership asks how you compare with the competitors you lose deals to. The answer today is a slide from last year, with prices and features nobody has checked since.

**You need.** the competitors to compare, at most three per run, with their websites; what the comparison is for, for example a positioning decision or a sales battle card; optional: lost deal notes or win and loss reasons; optional: context/PRODUCT.md.

**Skills.** [pm](../skills/pm/SKILL.md) → [product-research](../skills/product-research/SKILL.md) → [competitive-brief](https://github.com/anthropics/knowledge-work-plugins/blob/main/product-management/skills/competitive-brief/SKILL.md) (outside, optional)

**Steps.**
1. Name the decision the comparison serves and the capabilities that matter to it, before looking at any competitor
2. Search first for evidence against your current positioning, such as reviews where customers chose a competitor over you
3. For each competitor, gather pricing, plans, the listed capabilities, recent changes, and what their customers praise and complain about, quoting every page with its date
4. Build the comparison: one row per capability, one column per product, a source and date in every cell, and unknown where nothing was found
5. Write where you win, where you lose, and what that means for the decision, with a confidence tag on each point
6. Check every quote and price against its page

**You get.** a comparison table with a source and date in every cell; where you win and where you lose, with confidence tags; what the comparison means for the decision; an evidence file with every quote and link.

**Checked by.** every price and feature claim links a page read on a stated date; every quote matches its page exactly; cells with no evidence say unknown; evidence against your own positioning is included; no claim says only, first or nobody without naming the search behind it.

**Setup.** web search and fetch allowed in Claude Code; python3 for the quote checker; optional: Anthropic's product management plugin for competitive-brief (claude plugin marketplace add anthropics/knowledge-work-plugins, then claude plugin install product-management@knowledge-work-plugins), which registers remote connectors that read nothing until you sign in to one.

**Effort.** 5 to 10 minutes of Claude time per competitor

**Tested.** golden set: evals/golden-sets/product-research

**Example prompt.**

```text
We keep losing deals to three competitors; their names and websites are in notes/competitors.md. Build a comparison I can defend in front of sales, and tell me where we actually lose.
```

**Example result.** None yet

**Limits.** public pages only: it cannot see pricing behind a sales call or a login; competitors change their pages often, so every cell carries the date it was read; product-research reads at most 10 pages per run, so compare at most three competitors at a time; review sites over represent unhappy customers, so a complaint theme stays a weak signal until three sources agree.

Fallback for competitive-brief: The pm skill builds the comparison table itself from product-research's checked evidence, with one row per capability and a source and date in every cell.

### B03
**Market size from the bottom up**

**Problem.** A business case needs a market size, and the number in the draft is a top down analyst figure nobody can trace or defend. The decision needs a size built from buyers you can count and prices you can check.

**You need.** the segment in one sentence: who buys, where, and for what; the decision the size serves, for example whether to enter the segment; your price or price range; optional: your own customer counts and conversion data.

**Skills.** [pm](../skills/pm/SKILL.md) → [product-research](../skills/product-research/SKILL.md)

**Steps.**
1. Write the sizing formula before searching: the number of buyers in the segment, times the share that has the problem, times what they would pay in a year
2. Search first for evidence that the market is smaller than assumed, such as low adoption of similar products
3. Find a sourced number for each input, quoted from its page, or mark it as an assumption with a stated range
4. Calculate a low, middle and high size, showing every multiplication
5. Show which input moves the result most, and what it would take to narrow that input
6. Compare the result with any top down figure in the draft and explain the gap

**You get.** a bottom up market size as a range, with the formula and every input; a sources table with a confidence tag per input; the input the result depends on most, and how to narrow it; a comparison with the top down figure.

**Checked by.** every input is a quoted, sourced number or a labelled assumption; the arithmetic is shown and recomputes exactly; the result is a range, not a single number; no figure from a paywalled analyst report is used as if it had been read.

**Setup.** web search and fetch allowed in Claude Code; python3 for the arithmetic and the quote checker.

**Effort.** 10 to 20 minutes of Claude time

**Tested.** golden set: evals/golden-sets/product-research

**Example prompt.**

```text
Our business case says the market for invoicing software for freelance designers in the UK is 2 billion pounds. I don't believe it. Size it from the bottom up so I can defend the number to finance.
```

**Example result.** None yet

**Limits.** public data on small segments is thin, so expect wide ranges and several assumptions; it cannot read paid analyst reports, so it never treats their figures as checked; a market size says how big the prize could be, not whether you can win it.

### B04
**Interview synthesis**

**Problem.** You ran eight to fifteen customer interviews, the notes are long, and the team is about to decide what they mean from memory. Unless someone counts, the loudest quote wins.

**You need.** the interview transcripts or notes, one file per interview, with participants' personal details removed; the research question the interviews were meant to answer; optional: each participant's segment.

**Skills.** [pm](../skills/pm/SKILL.md) → [interview-snapshot](https://github.com/mshadmanrahman/pm-pilot/blob/main/plugins/pm-discovery/skills/interview-snapshot/SKILL.md) (outside, optional) → [synthesize-research](https://github.com/anthropics/knowledge-work-plugins/blob/main/product-management/skills/synthesize-research/SKILL.md) (outside, optional)

**Steps.**
1. Restate the research question and what the team will decide with the answer
2. Summarise each interview on its own, quoting the participant's words, before looking across interviews
3. Group the findings into themes and count how many separate interviews support each one
4. Label any theme supported by fewer than three interviews as a weak signal
5. Pull out differences between segments, and findings that go against the team's current plan
6. Write the synthesis: each theme with its count, its best quotes and what it means for the decision
7. Check every quote against its transcript

**You get.** a summary of each interview; themes ranked by how many interviews support them, with quotes; weak signals labelled as such; findings that contradict the current plan; what the themes mean for the decision.

**Checked by.** every quote matches its transcript word for word; every theme states how many interviews support it; themes with fewer than three supporting interviews are labelled weak signals; mild comments are not turned into strong claims; contradicting findings have their own section.

**Setup.** Claude Code with this repo, as a plugin or a clone; the transcripts as files; optional: PM Pilot's pm-discovery plugin for interview-snapshot (claude plugin marketplace add mshadmanrahman/pm-pilot, then claude plugin install pm-discovery@pm-pilot); optional: Anthropic's product management plugin for synthesize-research (claude plugin marketplace add anthropics/knowledge-work-plugins, then claude plugin install product-management@knowledge-work-plugins), which registers remote connectors that read nothing until you sign in to one.

**Effort.** 15 to 30 minutes of Claude time for ten interviews; 20 minutes of yours checking the themes against your own memory

**Tested.** untested

**Example prompt.**

```text
I ran 12 interviews with finance managers about month end close. The transcripts are in research/interviews/. What did we actually learn, and does it support building the reconciliation feature?
```

**Example result.** None yet

**Limits.** it can only synthesise what was said and cannot repair leading questions asked in the interviews; twelve interviews show patterns, not proportions, so it never turns counts into market percentages; participants' names and contact details must be removed before the transcripts go in.

Fallback for interview-snapshot: The pm skill writes a one page summary of each interview itself, quoting the participant's own words.

Fallback for synthesize-research: The pm skill groups the summaries into themes itself and counts the interviews behind each one.

### B05
**Opportunity discovery for an outcome**

**Problem.** The team has an outcome to move, such as retention, and a backlog of feature ideas, but nobody has mapped the customer problems in between. Ideas get built because someone senior likes them, not because they address the biggest opportunity.

**You need.** the outcome and its metric; customer evidence: interview notes, feedback, support tickets, survey answers; the current list of solution ideas; optional: product analytics exports.

**Skills.** [pm](../skills/pm/SKILL.md) → [opportunity-solution-tree](https://github.com/phuryn/pm-skills/blob/main/pm-product-discovery/skills/opportunity-solution-tree/SKILL.md) (outside, optional) → [discover-opportunities](https://github.com/amplitude/mcp-marketplace/blob/main/plugins/amplitude/skills/discover-opportunities/SKILL.md) (outside, optional)

**Steps.**
1. State the outcome and its metric, with the baseline or unknown
2. Extract customer problems and needs from the evidence, in customers' words, each with its source
3. Group them into opportunities and give each its evidence and a confidence tag
4. Place every existing solution idea under the opportunity it addresses, and list ideas that address none
5. Rank the opportunities by how much they could move the outcome and how strong their evidence is, showing the inputs to the ranking
6. For the top two opportunities, propose the cheapest test of the riskiest assumption

**You get.** an opportunity solution tree from the outcome down to tests; opportunities ranked with their evidence and confidence; ideas that address no known opportunity; two assumption tests.

**Checked by.** every opportunity is stated as a customer problem, not a feature; every opportunity cites its evidence; the ranking shows its inputs; ideas with no opportunity are flagged rather than quietly dropped; each test names the result that would change the plan.

**Setup.** Claude Code with this repo, as a plugin or a clone; the evidence as files; optional: Pawel Huryn's pm-product-discovery plugin for opportunity-solution-tree (claude plugin marketplace add phuryn/pm-skills, then claude plugin install pm-product-discovery@pm-skills), but Dean Peters' collection uses the same marketplace name, pm-skills, so adding both can clash; optional: an Amplitude account with project access, and Amplitude's plugin for discover-opportunities (claude plugin install amplitude@claude-plugins-official).

**Effort.** 15 to 30 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
Our goal this half is 90 day retention for small teams. Interview notes, support tickets and our idea backlog are in discovery/. Which customer problems should we go after, and which of our ideas don't address any of them?
```

**Example result.** None yet

**Limits.** the tree is only as complete as the evidence, so missing segments stay missing; Amplitude's skill reads only data in Amplitude, and its plugin also has write tools that this workflow never uses; ranking by potential impact is a judgment, so the inputs are shown for you to change.

Fallback for opportunity-solution-tree: The pm skill builds the tree itself as a nested outline: the outcome, then customer opportunities with their evidence, then solutions, then a test for each.

Fallback for discover-opportunities: The pm skill works only from the exports and feedback files you provide, and names the analytics questions it could not answer.

### B06
**Jobs to be done from switching stories**

**Problem.** The team describes the product by its features, and nobody can say in customers' own words what they hire it for, or what they stopped using to hire it. Positioning and roadmap debates go in circles.

**You need.** switching stories: interviews or notes with customers who recently started using you or left you, as files; the decision this serves, for example positioning or next quarter's bets; optional: reviews or sales notes that say why customers chose you or a rival.

**Skills.** [pm](../skills/pm/SKILL.md) → [customer-interviews](https://github.com/menkesu/awesome-pm-skills/blob/main/skills/customer-interviews/SKILL.md) (outside, optional)

**Steps.**
1. For each story, record the timeline of the switch: the first thought, the trigger, what they looked at, what they chose and what they stopped using
2. Record the four forces in each story: the push of the old way, the pull of the new one, the anxiety about switching, and the habit that held them back
3. Write job statements in customers' words: the situation, what they want to achieve, and the result they expect
4. Group the jobs and count how many separate stories support each one; fewer than three is a weak signal
5. Name what customers stopped using to hire you, including spreadsheets and doing nothing
6. Write what the jobs mean for the decision; if there are too few stories, write a switch interview guide instead

**You get.** a switch timeline for each story; a table of the four forces; job statements with the stories behind each one counted; what customers stopped using to hire you; what the jobs mean for the decision, or an interview guide to collect more stories.

**Checked by.** every job statement uses customers' words and cites its stories; jobs describe the progress customers want, not features; every job states how many stories support it; the list of alternatives includes doing nothing and workarounds wherever the stories mention them.

**Setup.** Claude Code with this repo, as a plugin or a clone; the stories as files; optional: Udi Menkes' Awesome PM Skills for customer-interviews (/plugin marketplace add menkesu/awesome-pm-skills, then /plugin install awesome-pm-skills@awesome-pm-skills).

**Effort.** 15 to 30 minutes of Claude time; longer if it writes the interview guide first

**Tested.** untested

**Example prompt.**

```text
I have notes from nine customers who switched to us from spreadsheets or a rival last quarter, in research/switch/. What job are they really hiring us for, and what does that mean for how we position the product?
```

**Example result.** None yet

**Limits.** jobs come from stories, so with fewer than five recent switchers it writes the interview guide rather than a conclusion; it cannot interview customers for you; a job statement is a hypothesis to test in positioning or pricing, not proof of demand.

Fallback for customer-interviews: The pm skill reads each story itself, records the forces that pushed and pulled the customer, and writes the job statements in their words.

### B07
**Evidence backed problem statement**

**Problem.** A request arrives as a solution, such as 'add a dashboard', and nobody has written down who has the problem, how often, what it costs them or what they do today. The team is about to build without knowing whether the problem is real.

**You need.** the request as it arrived; whatever evidence exists: support tickets, call notes, sales notes, usage data; optional: context/PRODUCT.md.

**Skills.** [pm](../skills/pm/SKILL.md) → [brief](https://github.com/mshadmanrahman/pm-pilot/blob/main/plugins/pm-core/skills/brief/SKILL.md) (outside, optional)

**Steps.**
1. Restate the request as the problem behind it: who has it, in what situation, and what it stops them doing
2. Answer the questions in PM.md section 2 from the evidence, writing unknown where there is none
3. Count the evidence: how many separate customers show the problem, with their words quoted
4. Estimate how often it happens and what it costs the customer, only from the evidence, marking estimates as estimates
5. Write the problem statement in one paragraph, followed by the evidence table and the gaps
6. Name the cheapest test that would show whether the problem is real and big enough, such as five interviews or one data pull

**You get.** a one page problem statement; an evidence table with sources and confidence tags; the gaps, each with the cheapest way to fill it; a recommendation: build, test first, or drop.

**Checked by.** the statement describes a problem, not a solution; every claim cites its source or is marked as an assumption; customer quotes are word for word and not made stronger; frequency and cost are sourced or marked as estimates; the recommendation follows from how much evidence there is.

**Setup.** Claude Code with this repo, as a plugin or a clone; the evidence as files or pasted text; optional: PM Pilot's pm-core plugin for brief (claude plugin marketplace add mshadmanrahman/pm-pilot, then claude plugin install pm-core@pm-pilot).

**Effort.** 5 to 15 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
Our biggest customer asked for an admin dashboard. Before we build it, write the problem statement behind the request from the tickets and call notes in evidence/, and tell me whether anyone else has the problem.
```

**Example result.** None yet

**Limits.** it uses your internal evidence, so for outside evidence of the problem run B01 as well; one large customer's many tickets can look like a pattern, so it counts customers rather than tickets; it cannot measure how often the problem happens without data you provide.

Fallback for brief: The pm skill writes the evidence table itself, one claim per row with its source and confidence tag, and lists the evidence that is missing.

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

**Tested.** demo run: run 2026-10-11 with skill version 2 on synthetic inputs, graded by a separate reviewer with an answer key: 7 of 10 answer key criteria and 13 of 16 outside claims verified on their pages, but failed 2 of 8 checks: one quote came from a search summary, and the seat assumption is tested only after both squads are committed. Rerun the same day with version 3: key 7 of 10, 1 red flag, 7 of 14 web claims on their pages; both failed the skill's own checks. See examples/demos/C01-idea-to-roadmap/run-2026-10-11/GRADE.md

**Example prompt.**

```text
Here's an idea in examples/demos/C01-idea-to-roadmap/input/idea.md. We have two squads for one quarter and the goal is firms adding seats. Is it the right bet, and if so what's the roadmap?
```

**Example result.** examples/demos/C01-idea-to-roadmap/run-2026-10-11/ (unedited outputs and the grade)

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

### C03
**Feature roadmap to outcome roadmap**

**Problem.** The roadmap is a list of features with dates. Leadership asks what each item will change for customers or the business, the team cannot say, and every review turns into an argument about dates.

**You need.** the current roadmap as a file or table; the goals and metrics the company or team is measured on; optional: the evidence behind each item.

**Skills.** [pm](../skills/pm/SKILL.md) → [outcome-roadmap](https://github.com/phuryn/pm-skills/blob/main/pm-execution/skills/outcome-roadmap/SKILL.md) (outside, optional)

**Steps.**
1. List every roadmap item with the reason it is there today, quoting any document that explains it
2. For each item, write the customer or business outcome it should change and the metric that would show the change
3. Group items that serve the same outcome, and flag items that serve none of the stated goals
4. Write each outcome as a roadmap item: the outcome, the metric, the bets that might move it, evidence and confidence, and what would make the team drop it
5. Keep a date only where a real commitment exists, and say whose commitment it is
6. List the items that need a decision because no outcome could be found for them

**You get.** an outcome roadmap in the PM.md roadmap item format; a mapping from each old feature to its outcome; items with no outcome, flagged for a decision; the commitments that keep a date, and why.

**Checked by.** every roadmap line is an outcome with a metric, not a feature; every old feature is mapped or flagged, and none disappears silently; no baseline or target is invented, and unknown is used where needed; dates are kept only for named commitments.

**Setup.** Claude Code with this repo, as a plugin or a clone; the roadmap as a file; optional: Pawel Huryn's pm-execution plugin for outcome-roadmap (claude plugin marketplace add phuryn/pm-skills, then claude plugin install pm-execution@pm-skills), but Dean Peters' collection uses the same marketplace name, pm-skills, so adding both can clash.

**Effort.** 10 to 20 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
Our roadmap for the next two quarters is in planning/roadmap.csv, and it's all features and dates. Rewrite it as outcomes tied to our activation and expansion goals, and flag anything that serves neither.
```

**Example result.** None yet

**Limits.** it cannot tell you which outcomes leadership will accept, so the flagged items need that conversation; metrics without baselines stay unknown until someone measures them; a rewrite does not undo commitments already made to customers, so it lists them.

Fallback for outcome-roadmap: The pm skill rewrites each item itself with the roadmap item template in PM.md section 5.

### C04
**Quarterly plan that fits the team**

**Problem.** Quarterly planning is next week. There are company goals, work carried over from last quarter, a ranked list of bets and a fixed team, and the draft plan commits to more than the team can deliver.

**You need.** the company or department goals for the quarter; the team's capacity: people, weeks, known time off and support duty; work carried over from last quarter, with its status; the ranked list of candidate bets, for example from C02, with engineering's estimates; optional: last quarter's results against its goals.

**Skills.** [pm](../skills/pm/SKILL.md) → [brainstorm-okrs](https://github.com/phuryn/pm-skills/blob/main/pm-execution/skills/brainstorm-okrs/SKILL.md) (outside, optional)

**Steps.**
1. Calculate usable capacity: people times working weeks, minus time off, support duty and other fixed work, showing the working
2. Put carried over work first, with an honest estimate of what is left of it
3. Draft objectives tied to the company goals, each with two to four key results that have a baseline or unknown, and a target
4. Fit the ranked bets into the capacity that is left, using engineering's estimates, and stop when it is full
5. Write what is not in the plan and why, so it can be said out loud
6. List the risks and the assumptions behind the plan, then check it against the criteria below

**You get.** a capacity calculation with the working shown; objectives and key results for the quarter; the committed plan and a separate stretch list; what was left out and why; risks and assumptions.

**Checked by.** the committed plan fits the calculated capacity; every key result has a baseline or says unknown, and has a target; every objective ties to a stated company goal; every estimate comes from the team's inputs, not from the model; the list of what is not in the plan exists.

**Setup.** Claude Code with this repo, as a plugin or a clone; the inputs as files; python3 for the arithmetic, shown in the run folder; optional: Pawel Huryn's pm-execution plugin for brainstorm-okrs (claude plugin marketplace add phuryn/pm-skills, then claude plugin install pm-execution@pm-skills), but Dean Peters' collection uses the same marketplace name, pm-skills, so adding both can clash.

**Effort.** 15 to 30 minutes of Claude time; an hour of yours with the team on estimates

**Tested.** untested

**Example prompt.**

```text
Planning is Thursday. Our goals, the carry over list, the ranked bets with estimates and the team calendar are in planning/q1/. We have five engineers and a designer. Build a plan that actually fits, with OKRs, and tell me what we have to say no to.
```

**Example result.** None yet

**Limits.** it uses your estimates and cannot estimate engineering effort itself; capacity arithmetic does not capture unplanned work, so it keeps a buffer only if you set one; draft OKRs mean nothing until the team agrees to them.

Fallback for brainstorm-okrs: The pm skill drafts the objectives and key results itself, one objective per goal, each key result with a baseline or unknown and a target.

### C05
**Sprint preparation**

**Problem.** Sprint planning is tomorrow and the top of the backlog is not ready. Stories lack acceptance criteria, dependencies are unknown, and nobody has checked the total against the team's capacity.

**You need.** the top of the backlog as an export, with estimates if you have them; the sprint goal or the outcome the sprint serves; the team's capacity for the sprint; the team's definition of ready, if it has one.

**Skills.** [pm](../skills/pm/SKILL.md) → [sprint-planning](https://github.com/anthropics/knowledge-work-plugins/blob/main/product-management/skills/sprint-planning/SKILL.md) (outside, optional) → [deliver-acceptance-criteria](https://github.com/product-on-purpose/pm-skills/blob/main/skills/deliver-acceptance-criteria/SKILL.md) (outside, optional)

**Steps.**
1. Restate the sprint goal and check that each candidate story serves it
2. Check each story against the definition of ready: a clear user and need, acceptance criteria, an estimate, known dependencies, and designs where needed
3. Draft acceptance criteria for stories that lack them, failure cases included, marked as drafts for the team
4. List dependencies on other teams or on decisions, and flag the stories they block
5. Fit the ready stories to capacity in priority order, showing the arithmetic
6. List the questions for engineering and design to settle in the planning meeting

**You get.** a readiness table for each candidate story; draft acceptance criteria marked DRAFT; a list of dependencies and blockers; a proposed sprint scope that fits capacity; questions for the planning meeting.

**Checked by.** every proposed story passes the definition of ready or is marked not ready with the reason; the proposed scope fits the stated capacity; drafted acceptance criteria include at least one failure case and are marked as drafts; nothing is changed in the tracker.

**Setup.** Claude Code with this repo, as a plugin or a clone; the backlog as an export file, because without a tracker connector it works only from what you export; optional: the Linear MCP server, which needs a Linear workspace (claude mcp add --transport http linear-server https://mcp.linear.app/mcp, then sign in with /mcp), and this workflow only reads from it; optional: Anthropic's product management plugin for sprint-planning (claude plugin marketplace add anthropics/knowledge-work-plugins, then claude plugin install product-management@knowledge-work-plugins), which registers remote connectors that read nothing until you sign in to one; optional: Product on Purpose's PM skills for deliver-acceptance-criteria (/plugin marketplace add product-on-purpose/agent-plugins, then /plugin install pm-skills@product-on-purpose), which needs Node.js and runs a hook at the start of each session that reads the file names in your folder.

**Effort.** 10 to 20 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
Sprint planning is tomorrow at ten. The top 25 backlog items are in sprint/backlog.csv and we have about 30 points of capacity. Which stories are actually ready, what's blocking the rest, and what should the sprint be?
```

**Example result.** None yet

**Limits.** it reads an export or a connector and never changes tickets in Jira or Linear; estimates come from the team, and it does not estimate for them; drafted acceptance criteria count only after the engineers review them.

Fallback for sprint-planning: The pm skill fits the stories to capacity itself, in priority order, and shows the arithmetic.

Fallback for deliver-acceptance-criteria: The pm skill drafts the acceptance criteria itself in Given, When, Then form, with at least one failure case per story.

### C06
**Dependencies and risks before you commit**

**Problem.** A plan depends on other teams, vendors and approvals, and nobody has listed which of them could make it slip. The risks surface one at a time, after the date has been promised.

**You need.** the plan or PRD with its dates; the teams, vendors and approvals it relies on, as far as you know them; optional: past plans that slipped, and why.

**Skills.** [pm](../skills/pm/SKILL.md) → [pre-mortem](https://github.com/phuryn/pm-skills/blob/main/pm-execution/skills/pre-mortem/SKILL.md) (outside, optional)

**Steps.**
1. List every dependency: what is needed, from whom, by when, and the evidence that they have agreed
2. Mark each dependency as confirmed, assumed or unknown
3. Assume the plan failed and list the most likely reasons, including dull ones such as approvals and holidays
4. Turn each reason into a risk with likelihood, impact, an early warning sign and a mitigation, marking the scores as judgments
5. Find the critical path: the chain of dependencies that sets the earliest finish date
6. List what must be confirmed before the date is promised, each with a named owner or needs owner

**You get.** a dependency map with status and evidence; a risk register with likelihood, impact, warning sign, mitigation and owner; the critical path; the confirmations needed before committing.

**Checked by.** every dependency shows whether it is confirmed, with the evidence; no owner or agreement is invented, and needs owner is written instead; every high risk has a mitigation and an early warning sign; the critical path is stated.

**Setup.** Claude Code with this repo, as a plugin or a clone; the plan as a file; optional: Pawel Huryn's pm-execution plugin for pre-mortem (claude plugin marketplace add phuryn/pm-skills, then claude plugin install pm-execution@pm-skills), but Dean Peters' collection uses the same marketplace name, pm-skills, so adding both can clash.

**Effort.** 10 to 20 minutes of Claude time; 30 minutes of yours confirming dependencies with other teams

**Tested.** untested

**Example prompt.**

```text
We're about to commit to a March launch for the partner API. The plan is in plans/partner_api.md. Before I promise the date, show me every dependency and the risks that could make us slip.
```

**Example result.** None yet

**Limits.** it knows only the dependencies the documents mention, so ask the other teams what it missed; likelihood and impact are judgments, not measurements; it does not contact other teams, so the confirmations are yours to get.

Fallback for pre-mortem: The pm skill runs the premortem itself: it assumes the plan failed, lists the likely reasons, and sorts them by likelihood and impact.

### C07
**Stakeholder alignment before the plan is final**

**Problem.** The quarterly plan goes to a review with eight to twelve stakeholders, each of whom wants something different from it. If the first time they see what they lose is in the meeting, the plan gets reopened there.

**You need.** the draft plan; the stakeholders: role, what they have asked for, and what they influence; optional: notes from past conversations with them, kept on your machine.

**Skills.** [pm](../skills/pm/SKILL.md) → [stakeholder-mapping](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/stakeholder-mapping/SKILL.md) (outside, optional)

**Steps.**
1. List each stakeholder with what they asked for, quoting the request wherever it is written down
2. Mark what the plan gives each of them, what it does not, and what they lose compared with what they expect
3. Place them by influence and interest, and decide who must be spoken to before the review and in what order
4. For each conversation, write the one thing to agree, the evidence behind the plan's choice, and what you can offer
5. List the objections you expect and the evidence that answers each, or note where the plan has no answer
6. Write the plan's summary for the review, naming the trade offs that were already discussed

**You get.** a stakeholder map showing what each person gains and loses; the order of conversations before the review; a one page brief for each key conversation; expected objections and the answers; a summary for the review.

**Checked by.** every stakeholder's request is quoted or marked as your recollection; every loss is stated plainly rather than softened; objections without an answer are listed, not hidden; nothing is sent to anyone, and the conversations stay yours.

**Setup.** Claude Code with this repo, as a plugin or a clone; optional: Dean Peters' stakeholder-mapping skill (/plugin marketplace add deanpeters/Product-Manager-Skills, then /plugin install stakeholder-mapping@pm-skills), but Pawel Huryn's collection uses the same marketplace name, pm-skills, so adding both can clash.

**Effort.** 15 to 25 minutes of Claude time; the conversations are yours

**Tested.** untested

**Example prompt.**

```text
Our Q3 plan goes to the leadership review in two weeks. Sales wants the integrations, support wants the bug backlog, and finance wants the pricing work. The plan and what each of them asked for are in planning/. Help me get them aligned before the meeting.
```

**Example result.** None yet

**Limits.** the outside skill's licence is non commercial: check it before using it for paid work; it maps what you tell it about people and cannot read the room for you; notes about colleagues are sensitive, so keep them out of shared folders and repositories.

Fallback for stakeholder-mapping: The pm skill places each stakeholder on an influence and interest grid itself and suggests how to engage each one.

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

**Tested.** demo run: run 2026-10-11 with skill version 2 on synthetic inputs, graded by a separate reviewer with an answer key: 8 of 9 answer key criteria, which clears the key's bar, but failed 2 of 8 checks: the prototype it built shows wrong totals and was never read back. Rerun the same day with version 3: key 9 of 9; both failed the skill's own checks. See examples/demos/D01-prd-to-experience/run-2026-10-11/GRADE.md

**Example prompt.**

```text
Here's the PRD for our client payment portal in examples/demos/D01-prd-to-experience/input/. Find the gaps, write the flows and acceptance criteria, and give me a spec a designer can prototype from.
```

**Example result.** examples/demos/D01-prd-to-experience/run-2026-10-11/ (unedited outputs and the grade)

**Limits.** it writes a specification, not visual designs; it cannot test with real users; accessibility notes are a starting point, not an audit.

### D02
**User journey map from evidence**

**Problem.** Support, design, sales and data each see a different slice of where customers struggle, and every meeting about the experience becomes a debate between anecdotes. Nobody has one map of the journey with the evidence attached.

**You need.** the segment and the journey to map, for example from sign up to the first invoice sent; evidence: support tickets, interview notes, survey answers, funnel or event data; optional: screenshots of the current product.

**Skills.** [pm](../skills/pm/SKILL.md) → [customer-journey-map](https://github.com/phuryn/pm-skills/blob/main/pm-market-research/skills/customer-journey-map/SKILL.md) (outside, optional) → [compare-user-journeys](https://github.com/amplitude/mcp-marketplace/blob/main/plugins/amplitude/skills/compare-user-journeys/SKILL.md) (outside, optional)

**Steps.**
1. Define the segment, where the journey starts and ends, and the stages in between
2. For each stage, write what the customer is trying to do and what they actually do, from the evidence
3. Attach the evidence to each stage: quotes, ticket counts, and the drop off from the funnel where data exists
4. Mark the pain points, each with how many separate sources support it
5. Compare customers who complete the journey with those who do not, where the data allows
6. Rank the pain points by their evidence and the number of customers affected, and name the opportunities

**You get.** a journey map by stage with the evidence attached; pain points ranked by evidence; differences between customers who complete the journey and those who do not, where data allows; opportunities for the roadmap.

**Checked by.** every stage cites evidence or is marked as an assumption; customers' feelings are quoted, never invented; drop off numbers match the data exactly; every pain point states how many sources support it.

**Setup.** Claude Code with this repo, as a plugin or a clone; the evidence as files; optional: Pawel Huryn's pm-market-research plugin for customer-journey-map (claude plugin marketplace add phuryn/pm-skills, then claude plugin install pm-market-research@pm-skills), but Dean Peters' collection uses the same marketplace name, pm-skills, so adding both can clash; optional: an Amplitude account with project access, and Amplitude's plugin for compare-user-journeys (claude plugin install amplitude@claude-plugins-official).

**Effort.** 15 to 30 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
Map the journey from sign up to the first invoice sent for small agencies. Tickets, interview notes and our funnel export are in journey/. Where do people actually get stuck, and what's the evidence?
```

**Example result.** None yet

**Limits.** a map built from support tickets over represents the customers who complain; without event data the drop off is unknown rather than estimated; it maps the journey as it is today, and designing the new one is a separate step.

Fallback for customer-journey-map: The pm skill draws the map itself as a table: the stage, what the customer does, what they say in their own words, the evidence, and the drop off where data exists.

Fallback for compare-user-journeys: The pm skill compares the two groups only if you export the event data, and otherwise marks behaviour differences as unknown.

### D03
**Information architecture review**

**Problem.** Navigation grew one feature at a time. Customers cannot find things, support answers 'where do I find' questions every day, and the team wants to reorganise the menus without knowing what customers look for.

**You need.** the current structure: a sitemap, menu screenshots, or a list of pages and settings; what customers look for: support tickets, site search terms, interview notes; optional: page visit data.

**Skills.** [pm](../skills/pm/SKILL.md) → [figma-generate-diagram](https://github.com/figma/mcp-server-guide/blob/main/skills/figma-generate-diagram/SKILL.md) (outside, optional)

**Steps.**
1. Inventory every page, menu item and setting, with where it sits today
2. List the top tasks customers come to do, from the evidence, with how often each one appears
3. Find the problems: one thing with two homes, items buried more than three levels deep, labels in internal language, and tasks split across sections
4. Propose one or two new structures with labels in customers' words, and show where each top task lives in each
5. Write a tree test plan and a card sort plan for checking the proposal with real customers, with the tasks and the rule for success
6. Draw the current and proposed structures

**You get.** an inventory of the current structure; the top customer tasks with their evidence; a list of problems; one or two proposed structures; a tree test and card sort plan; diagrams of both structures.

**Checked by.** every top task cites its evidence; every label in the proposal is in customers' words with a source, or is marked as a suggestion; every item in the inventory has a place in the proposal or is marked for removal with a reason; the test plan states which result would reject the proposal.

**Setup.** Claude Code with this repo, as a plugin or a clone; optional: a Figma account and Figma's plugin for figma-generate-diagram (claude plugin install figma@claude-plugins-official), and note that View and Collab seats and the Starter plan get only 6 tool calls a month.

**Effort.** 15 to 30 minutes of Claude time; running the tree test with customers is yours

**Tested.** untested

**Example prompt.**

```text
Our settings area has grown to 60 pages and customers can't find anything. The sitemap and a month of 'where do I find' tickets are in ia/. Propose a better structure and a way to test it with customers before we rebuild it.
```

**Example result.** None yet

**Limits.** it cannot run the tree test or the card sort, so it writes the plan for you to run; Figma is used under Figma's Developer Terms, not an open source licence, and Figma says drawing on the canvas is free during its beta and will become a paid feature; new labels need checking with customers before they ship.

Fallback for figma-generate-diagram: The pm skill writes both structures as indented outlines and Mermaid diagrams in the run folder.

### D04
**UX evaluation before build**

**Problem.** A design is about to go into build, and nobody has checked it against basic usability rules or accessibility standards. The problems will reach customers, and fixing them after launch means building twice.

**You need.** the designs as images, covering every state; who the users are and the main task the design serves; optional: your design system's rules.

**Skills.** [pm](../skills/pm/SKILL.md) → [design-critique](https://github.com/anthropics/knowledge-work-plugins/blob/main/design/skills/design-critique/SKILL.md) (outside, optional) → [accessibility-review](https://github.com/anthropics/knowledge-work-plugins/blob/main/design/skills/accessibility-review/SKILL.md) (outside, optional)

**Steps.**
1. Restate the main task the design serves and walk through it screen by screen
2. Review each screen for usability, hierarchy and consistency, naming the screen and element for each issue
3. Check accessibility: contrast, text size, target size, labels, focus order and error messages
4. Check the states: empty, loading, error, long text, and what users without permission see
5. Rate each issue by severity and say what it stops the user doing
6. List what static screens cannot show and what needs a test with real users or assistive technology

**You get.** an issue list by severity, each with the screen, the element and the rule it breaks; an accessibility checklist marked pass, fail or cannot tell; missing states; what needs a live test.

**Checked by.** every issue names the screen and the element; accessibility results say cannot tell, rather than guess, when static designs cannot show it; severity reflects what the issue stops the user doing; suggestions are marked as suggestions, not requirements.

**Setup.** Claude Code with this repo, as a plugin or a clone; the designs exported as images; optional: Anthropic's design plugin for design-critique and accessibility-review (claude plugin marketplace add anthropics/knowledge-work-plugins, then claude plugin install design@knowledge-work-plugins), which registers remote connectors that read nothing until you sign in to one.

**Effort.** 10 to 25 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
The designs for the new checkout are in design/checkout/ as PNGs, error states included. Before engineering starts, check them for usability and accessibility problems and tell me what we must fix first.
```

**Example result.** None yet

**Limits.** it reviews designs, not working software, and some issues only appear in a live test; an accessibility review of static designs is a starting point, not a compliance audit; it cannot judge brand fit, which is your designer's call.

Fallback for design-critique: The pm skill reviews each screen itself against common usability rules, such as visible status and error prevention, naming the screen and element for every issue.

Fallback for accessibility-review: The pm skill checks what static designs can show, such as text contrast, target size and labels, and lists what needs a test with assistive technology.

### D05
**Usability review from test sessions**

**Problem.** You ran five usability sessions or watched a batch of session replays. The notes are scattered across observers, and the team remembers the most dramatic moment rather than the most common problem.

**You need.** notes or transcripts from each session, one file per participant, or access to session replays; the tasks participants were given and what success looked like; optional: timestamps of key moments in the recordings.

**Skills.** [pm](../skills/pm/SKILL.md) → [replay-ux-audit](https://github.com/amplitude/mcp-marketplace/blob/main/plugins/amplitude/skills/replay-ux-audit/SKILL.md) (outside, optional)

**Steps.**
1. Record, for each participant and task, whether they succeeded, struggled or failed, with the evidence
2. List every usability issue observed, with the participant, the task, and a quote or timestamp
3. Count how many participants hit each issue, written as x of n
4. Rate the severity of each issue by what it stopped participants doing
5. Keep observed behaviour separate from participants' opinions about the design
6. Write recommendations for the top issues, and note what a sample this small cannot tell you

**You get.** a task success table for each participant; an issue list with x of n counts, severity, quotes and timestamps; recommendations for the top issues; what the sample cannot answer.

**Checked by.** every issue cites a participant and a quote or timestamp; counts are written as x of n and recount correctly; opinions are not reported as observed behaviour; five sessions are never turned into percentages of all customers.

**Setup.** Claude Code with this repo, as a plugin or a clone; the session notes as files; optional: an Amplitude account with project access, and Amplitude's plugin for replay-ux-audit (claude plugin install amplitude@claude-plugins-official), which reads only session replays already recorded in Amplitude.

**Effort.** 10 to 20 minutes of Claude time for five sessions

**Tested.** untested

**Example prompt.**

```text
We ran five usability sessions on the new onboarding last week. Each observer's notes are in usability/. What were the real problems, how many people hit each one, and what should we fix first?
```

**Example result.** None yet

**Limits.** small samples find problems but do not measure how common a problem is across all customers; it cannot watch recordings, so it needs notes, transcripts or Amplitude replays; Amplitude's plugin also has write tools that this workflow never uses.

Fallback for replay-ux-audit: The pm skill works from the session notes you provide and marks findings that would need replays as not checked.

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

**Tested.** demo run: run 2026-10-11 with skill version 2 on synthetic inputs, graded by a separate reviewer with an answer key: 7 of 10 answer key criteria: the drop dated to the right release and both decoys ruled out, but failed 2 of 8 checks and one red flag: a wrong count was passed by the self check. Rerun the same day with version 3: key 9 of 10, no red flag; both failed the skill's own checks. See examples/demos/E01-analytics-to-decisions/run-2026-10-11/GRADE.md

**Example prompt.**

```text
Activation dropped this quarter. The weekly metrics, definitions and release log are in examples/demos/E01-analytics-to-decisions/input/. Why did it drop and what should we do?
```

**Example result.** examples/demos/E01-analytics-to-decisions/run-2026-10-11/ (unedited outputs and the grade)

**Limits.** it cannot query your analytics tool unless you connect it; correlation with a release is a lead, not proof; small numbers are flagged rather than over read.

### E02
**North star metric and KPI tree**

**Problem.** The team tracks dozens of metrics and has never agreed which one shows that customers get value. Every review argues about a different number, and no team can see which lever it owns.

**You need.** what the product does and for whom, or context/PRODUCT.md; the metrics you track today, with their definitions; the company goal the metric should lead to, such as revenue or retention; optional: past data for the candidate metrics.

**Skills.** [pm](../skills/pm/SKILL.md) → [metrics](https://github.com/menkesu/awesome-pm-skills/blob/main/skills/metrics/SKILL.md) (outside, optional)

**Steps.**
1. List three to five candidate north stars and test each: does it reflect value customers get, does it lead to the company goal, can teams move it, and can it be measured today
2. Recommend one, with a precise definition: the event, the time window and who counts
3. Break it into the input metrics that drive it, with the formulas that link them, and recompute the formulas
4. Name a team or owner for each input, or write needs owner
5. Add guardrail metrics that would show the north star being gamed or bought at too high a cost
6. Write baselines from your data where they exist and unknown where they do not, and set how often the tree is reviewed

**You get.** a scored comparison of the candidate north stars; the recommended north star and its definition; a KPI tree from the north star down to inputs each team owns, with formulas; guardrail metrics; baselines or unknown, and a review rhythm.

**Checked by.** the tree's formulas recompute exactly from their inputs; every metric has a precise definition; no baseline is invented; at least one guardrail is named; the recommendation says why the other candidates lost.

**Setup.** Claude Code with this repo, as a plugin or a clone; python3 for checking the formulas; optional: Udi Menkes' Awesome PM Skills for metrics (/plugin marketplace add menkesu/awesome-pm-skills, then /plugin install awesome-pm-skills@awesome-pm-skills).

**Effort.** 15 to 30 minutes of Claude time; a meeting of yours to agree the choice

**Tested.** untested

**Example prompt.**

```text
We track 40 metrics and nobody agrees which one matters. Our metric definitions and the last six months of data are in metrics/. Help me pick a north star and break it down so each squad knows which number it owns.
```

**Example result.** None yet

**Limits.** choosing a north star is a leadership decision, so it recommends and shows why; a tree shows how metrics relate by formula, which is not proof of cause; without past data it cannot check that the north star moves with the company goal, and it says the check was skipped.

Fallback for metrics: The pm skill proposes and tests candidate north stars itself, then breaks the chosen one into input metrics, each with a formula and an owner.

### E03
**Activation and conversion funnel**

**Problem.** Sign ups grow, but few new accounts reach the moment where the product proves its value, and the team does not agree what activated means. Effort goes into the top of the funnel while the leak is further down.

**You need.** event or funnel data as an export: sign up, key actions, and whether each account is still active later; your current definition of activation, if there is one; optional: onboarding screens or flows.

**Skills.** [pm](../skills/pm/SKILL.md) → [analyze](https://github.com/anthropics/knowledge-work-plugins/blob/main/data/skills/analyze/SKILL.md) (outside, optional) → [compare-user-journeys](https://github.com/amplitude/mcp-marketplace/blob/main/plugins/amplitude/skills/compare-user-journeys/SKILL.md) (outside, optional)

**Steps.**
1. Write the funnel steps from sign up to first value, and check each event's definition
2. Calculate the conversion between every pair of steps, by week of sign up, and find the biggest drop
3. Test candidate activation definitions: which early actions are most common among accounts still active after 30 days, labelled as correlation
4. Recommend an activation definition with its event, its threshold and its time window
5. Write hypotheses for the biggest drop, each with its evidence, and the cheapest experiment for the leading one
6. Check every number against the export

**You get.** a funnel with the conversion at each step, by sign up week; the biggest drop and its likely causes, as hypotheses; a recommended activation definition; one experiment for the leading hypothesis.

**Checked by.** every number recomputes from the export; correlations are labelled as correlations, not causes; the activation definition names an event, a threshold and a window; small cohorts are flagged rather than over read.

**Setup.** Claude Code with this repo, as a plugin or a clone; python3; the data as an export, or a connection to Amplitude, Mixpanel or PostHog instead, each of which needs an account (the commands are in resources/README.md); optional: Anthropic's data plugin for analyze (claude plugin marketplace add anthropics/knowledge-work-plugins, then claude plugin install data@knowledge-work-plugins), which registers remote connectors that read nothing until you sign in to one; optional: an Amplitude account with project access, and Amplitude's plugin for compare-user-journeys (claude plugin install amplitude@claude-plugins-official).

**Effort.** 10 to 25 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
Sign ups are up 30 percent this quarter but paid conversions are flat. The event export for the last 12 weeks is in data/funnel.csv. Where do new accounts drop off, and what should activated mean for us?
```

**Example result.** None yet

**Limits.** it finds where accounts drop and what retained accounts did, but it cannot prove why without an experiment; it works only with the events you export, so a missing event makes that step unknown; small weekly cohorts give noisy rates, and it flags them.

Fallback for analyze: The pm skill runs the funnel arithmetic itself on the export with python3 and shows the working.

Fallback for compare-user-journeys: The pm skill compares retained and lost accounts using only the events in your export, and names the behaviours it could not see.

### E04
**Retention by cohort**

**Problem.** Churn feels high, but the team looks at one blended churn number. It hides whether newer customers stay longer or shorter than older ones, and which segments leave first.

**You need.** an export of accounts or users with start date, segment, and activity or billing status by month; the decision this serves, for example where to focus next quarter; optional: plan, pricing and onboarding changes with their dates.

**Skills.** [pm](../skills/pm/SKILL.md) → [cohort-analysis](https://github.com/phuryn/pm-skills/blob/main/pm-data-analytics/skills/cohort-analysis/SKILL.md) (outside, optional)

**Steps.**
1. Define retained precisely: the action or billing state that counts, the time window, and who is included
2. Build a cohort table by start month and the retention curve for each cohort
3. Find where the curves flatten, and whether newer cohorts retain better or worse than older ones
4. Split by segment, plan and acquisition channel where the data allows, flagging cohorts too small to read
5. Line up changes in the curves with product, pricing and onboarding changes, stating each link as a hypothesis
6. Write what the decision should be, with its confidence and the next analysis or test

**You get.** a cohort retention table and curves; where retention flattens, and the trend across cohorts; differences between segments, with sample sizes; hypotheses linking changes in the curves to dated changes; a recommendation.

**Checked by.** the retention definition is stated precisely; every rate recomputes from the export; cohorts below a stated size are flagged; every link to a dated change is written as a hypothesis.

**Setup.** Claude Code with this repo, as a plugin or a clone; python3; the data as an export, or a connection to Amplitude, Mixpanel or PostHog instead, each of which needs an account (the commands are in resources/README.md); optional: Pawel Huryn's pm-data-analytics plugin for cohort-analysis (claude plugin marketplace add phuryn/pm-skills, then claude plugin install pm-data-analytics@pm-skills), but Dean Peters' collection uses the same marketplace name, pm-skills, so adding both can clash.

**Effort.** 10 to 25 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
Leadership thinks churn is getting worse. An export of every account since January with plan, channel and monthly status is in data/accounts.csv. Are newer customers leaving faster, and which segment should we focus on?
```

**Example result.** None yet

**Limits.** it measures who stayed but cannot say why customers left without exit reasons or interviews; with activity data alone it reports how many customers stayed, not how much revenue stayed, and it says so; cohorts from the last few months have short curves and are flagged as incomplete.

Fallback for cohort-analysis: The pm skill builds the cohort table itself with python3 and shows the working.

### E05
**Experiment from design to readout**

**Problem.** A change is about to ship as an A/B test with no written hypothesis, primary metric, sample size or stopping rule. When the result arrives, people will pick the metric that looks best and argue about whether it is real.

**You need.** the change and the hypothesis behind it; the metric it should move and the guardrail metrics it must not hurt, with baselines if known; how many users a week would see the change; after the test: the results as an export.

**Skills.** [pm](../skills/pm/SKILL.md) → [experiment](https://github.com/menkesu/awesome-pm-skills/blob/main/skills/experiment/SKILL.md) (outside, optional) → [statistical-analysis](https://github.com/anthropics/knowledge-work-plugins/blob/main/data/skills/statistical-analysis/SKILL.md) (outside, optional)

**Steps.**
1. Before launch, write the hypothesis, the one primary metric, the guardrails, and the smallest effect worth acting on
2. Calculate the sample size and duration from the baseline and the weekly traffic, showing the working, and say so if the test cannot reach it
3. Write the stopping rule and the decision rule, meaning which result leads to ship, hold or stop, and freeze both with the date
4. List the events the test needs and confirm they fire before it starts
5. After the test, check the split between the groups, the run length and the guardrails before reading the primary metric
6. Read the primary metric against the frozen decision rule and make the call, with its confidence

**You get.** an experiment plan frozen and dated before launch; the sample size and duration, with the working; after the test, a readout against the plan: the checks, the call and its confidence.

**Checked by.** the plan names one primary metric and at least one guardrail before launch; the sample size calculation is shown and recomputes; the readout uses the metric and decision rule frozen in the plan; a test that stopped short of its planned sample is reported as inconclusive; the split between the groups is checked before the result is read.

**Setup.** Claude Code with this repo, as a plugin or a clone; python3; the data as an export, or a connection to Amplitude, Mixpanel or PostHog instead, each of which needs an account (the commands are in resources/README.md); optional: Udi Menkes' Awesome PM Skills for experiment (/plugin marketplace add menkesu/awesome-pm-skills, then /plugin install awesome-pm-skills@awesome-pm-skills); optional: Anthropic's data plugin for statistical-analysis (claude plugin marketplace add anthropics/knowledge-work-plugins, then claude plugin install data@knowledge-work-plugins), which registers remote connectors that read nothing until you sign in to one.

**Effort.** 15 to 25 minutes of Claude time before launch, and 10 to 20 minutes after

**Tested.** untested

**Example prompt.**

```text
We want to test a shorter sign up form. About 4,000 people a week reach it and 22 percent finish it today. Write the experiment plan before we launch, and when the results are in I'll ask you to read them against it.
```

**Example result.** None yet

**Limits.** it cannot set up the test in your tool, so you or engineering do that; low traffic can make a useful test impossible, and it says so rather than shrinking the sample; a frozen plan only helps if nobody edits it after launch, so keep it with the date it was written.

Fallback for experiment: The pm skill writes the plan itself: hypothesis, primary and guardrail metrics, the smallest effect worth acting on, sample size, duration, stopping rule and decision rule.

Fallback for statistical-analysis: The pm skill runs the test itself with python3, shows the calculation, and states its assumptions.

### E06
**Feature adoption**

**Problem.** A feature shipped six weeks ago and leadership asks whether it worked. Nobody defined adoption before launch, and some of the events needed to answer are missing.

**You need.** the feature and who it was built for; the goal set at launch, if there was one; usage data as an export; optional: the launch date and any rollout stages.

**Skills.** [pm](../skills/pm/SKILL.md) → [measure-instrumentation-spec](https://github.com/product-on-purpose/pm-skills/blob/main/skills/measure-instrumentation-spec/SKILL.md) (outside, optional) → [cohort-analysis](https://github.com/phuryn/pm-skills/blob/main/pm-data-analytics/skills/cohort-analysis/SKILL.md) (outside, optional)

**Steps.**
1. Define adoption for this feature: who could use it, what counts as trying it, and what counts as using it again
2. Check that the events exist to measure each stage, and specify the missing ones
3. Build the adoption funnel: eligible, aware where it can be measured, tried, used again, and still using after four weeks
4. Split adoption by segment and by the week customers first saw the feature
5. Compare the result with the goal set at launch, or state that none was set
6. Recommend investing more, fixing discovery, fixing the feature, or retiring it, with the evidence and the confidence

**You get.** a definition of adoption for the feature; an adoption funnel by segment and cohort; a specification for the missing events; the comparison with the launch goal; a recommendation.

**Checked by.** the funnel stages are defined before any number is reported; every number recomputes from the export; missing events are listed rather than estimated around; the comparison uses the goal set at launch, never one written afterwards.

**Setup.** Claude Code with this repo, as a plugin or a clone; python3; the data as an export, or a connection to Amplitude, Mixpanel or PostHog instead, each of which needs an account (the commands are in resources/README.md); optional: Product on Purpose's PM skills for measure-instrumentation-spec (/plugin marketplace add product-on-purpose/agent-plugins, then /plugin install pm-skills@product-on-purpose), which needs Node.js and runs a hook at the start of each session that reads the file names in your folder; optional: Pawel Huryn's pm-data-analytics plugin for cohort-analysis (claude plugin marketplace add phuryn/pm-skills, then claude plugin install pm-data-analytics@pm-skills), but Dean Peters' collection uses the same marketplace name, pm-skills, so adding both can clash.

**Effort.** 10 to 25 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
We launched saved reports six weeks ago. The usage export is in data/saved_reports.csv. Did anyone actually adopt it, which customers use it, and should we keep investing?
```

**Example result.** None yet

**Limits.** adoption before the missing events ship cannot be recovered, so it measures from the day they ship; it shows who uses the feature, not whether the feature changed retention or revenue; awareness is usually not measured, and it says so rather than estimating it.

Fallback for measure-instrumentation-spec: The pm skill writes the missing events itself as a table: event name, trigger, properties, and the question each one answers.

Fallback for cohort-analysis: The pm skill builds the adoption table itself with python3 and shows the working.

### E07
**Monthly product performance review**

**Problem.** The monthly product review is a dashboard of twenty metrics read aloud. Nobody explains which movements matter, and the meeting ends without any change to what the team does.

**You need.** this month's metrics and the months before, as an export; the target for each metric; the release log and other changes during the month; optional: billing data for revenue metrics.

**Skills.** [pm](../skills/pm/SKILL.md) → [metrics-review](https://github.com/anthropics/knowledge-work-plugins/blob/main/product-management/skills/metrics-review/SKILL.md) (outside, optional) → [saas-revenue-growth-metrics](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/saas-revenue-growth-metrics/SKILL.md) (outside, optional)

**Steps.**
1. Check that no metric changed its definition during the month
2. Mark each metric on track, at risk or off track against its target
3. Pick the three movements that matter most to the goals and explain each with evidence from the release log, marked as a hypothesis where it is not proven
4. Calculate revenue and retention metrics from billing data where it exists, defining each term in one plain sentence
5. Write what the team will do differently because of each of the three, or say plainly that nothing changes
6. Write the one page review and check every number against the export

**You get.** a status table of every metric against its target; the three movements that matter, explained with evidence; revenue and retention metrics where billing data exists; actions with owners or needs owner; a one page review.

**Checked by.** every number matches the export; definition changes are caught before a movement is read as a trend; explanations are marked as hypotheses unless proven; each of the three movements leads to an action or an explicit no action; every term such as net revenue retention is defined in one plain sentence.

**Setup.** Claude Code with this repo, as a plugin or a clone; python3; the data as an export, or a connection to Amplitude, Mixpanel or PostHog instead, each of which needs an account (the commands are in resources/README.md); optional: Anthropic's product management plugin for metrics-review (claude plugin marketplace add anthropics/knowledge-work-plugins, then claude plugin install product-management@knowledge-work-plugins), which registers remote connectors that read nothing until you sign in to one; optional: Dean Peters' saas-revenue-growth-metrics skill (/plugin marketplace add deanpeters/Product-Manager-Skills, then /plugin install saas-revenue-growth-metrics@pm-skills), but Pawel Huryn's collection uses the same marketplace name, pm-skills, so adding both can clash.

**Effort.** 10 to 20 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
Our monthly product review is Tuesday. September's metrics, targets and release log are in review/2026-09/. Tell me which three things actually matter this month and what we should do about them.
```

**Example result.** None yet

**Limits.** the outside skill's licence is non commercial: check it before using it for paid work; it explains movements with the evidence it has, and only a test proves a cause; it cannot see changes missing from the release log, such as a competitor's launch, unless you add them.

Fallback for metrics-review: The pm skill compares each metric with its target and the months before, and explains only the movements that cross a threshold you set.

Fallback for saas-revenue-growth-metrics: The pm skill calculates the revenue metrics itself with python3 and defines each one in a plain sentence the first time it appears.

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

### F02
**PRD quality score**

**Problem.** A PRD is about to go to engineering review. Its author cannot see its gaps, reviewers give vague feedback such as 'make it clearer', and the real problems surface during the build.

**You need.** the PRD; optional: your team's PRD template or definition of ready.

**Skills.** [pm](../skills/pm/SKILL.md) → [spec](https://github.com/menkesu/awesome-pm-skills/blob/main/skills/spec/SKILL.md) (outside, optional) → [critique](https://github.com/mshadmanrahman/pm-pilot/blob/main/plugins/pm-core/skills/critique/SKILL.md) (outside, optional)

**Steps.**
1. Check that the PRD has every part of the PM.md template: problem, evidence, goals and non goals, requirements with acceptance criteria, metrics with baselines, risks and open questions
2. Grade it on the rubric in PM.md section 7, quoting the line that justifies each score
3. List every requirement without a testable acceptance criterion
4. List every claim without evidence and every number without a source
5. Write the three fixes that would improve it most, in order
6. Leave the PRD unchanged; the author makes the fixes

**You get.** a scorecard with a quoted line behind each score; the template parts that are missing; requirements without testable acceptance criteria; unsupported claims; the top three fixes.

**Checked by.** every score quotes the line of the PRD that justifies it; every unsupported claim is quoted; the review adds no new requirements; each of the top three fixes is specific enough to act on today.

**Setup.** Claude Code with this repo, as a plugin or a clone; the PRD as a file; optional: Udi Menkes' Awesome PM Skills for spec (/plugin marketplace add menkesu/awesome-pm-skills, then /plugin install awesome-pm-skills@awesome-pm-skills); optional: PM Pilot's pm-core plugin for critique (claude plugin marketplace add mshadmanrahman/pm-pilot, then claude plugin install pm-core@pm-pilot).

**Effort.** 5 to 15 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
My PRD for team permissions is in specs/permissions.md and engineering review is Wednesday. Score it honestly and tell me the three things to fix first.
```

**Example result.** None yet

**Limits.** a score from the session that wrote the PRD is not independent, so run it in a fresh session; it judges the document, not whether the product idea is right; rubric scores are judgments, and the quoted lines let you disagree with them.

Fallback for spec: The pm skill grades the PRD itself against the PRD template in PM.md section 5 and returns the three fixes that would improve it most.

Fallback for critique: The pm skill lists every claim in the PRD that has no source and every requirement without a testable acceptance criterion.

### F03
**Roadmap quality review**

**Problem.** A roadmap is going to leadership, or you are reviewing another team's, and you need to know whether it holds up before the meeting. Today the review is a gut reaction to a slide.

**You need.** the roadmap; the goals it should serve; optional: the team's capacity and the evidence behind each item.

**Skills.** [pm](../skills/pm/SKILL.md) → [critique](https://github.com/mshadmanrahman/pm-pilot/blob/main/plugins/pm-core/skills/critique/SKILL.md) (outside, optional)

**Steps.**
1. Check each item: is it an outcome with a metric, and does it have evidence, a confidence, an owner, and a condition for dropping it
2. Check the whole: does it serve the stated goals, fit the stated capacity, name its dependencies, and say what it will not do
3. Score it on the rubric in PM.md section 7, quoting the line behind each score
4. Write the five questions that matter most for the review meeting
5. Leave the roadmap unchanged; if it needs rewriting as outcomes, say so and point to C03

**You get.** a check table, item by item; a scorecard for the whole roadmap with quoted evidence; the five questions for the review; a verdict: ready, ready with fixes, or not ready.

**Checked by.** every finding quotes the roadmap item it is about; capacity is judged only against stated capacity, never guessed; the review does not rewrite the roadmap; the questions are specific to this roadmap.

**Setup.** Claude Code with this repo, as a plugin or a clone; the roadmap as a file; optional: PM Pilot's pm-core plugin for critique (claude plugin marketplace add mshadmanrahman/pm-pilot, then claude plugin install pm-core@pm-pilot).

**Effort.** 10 to 15 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
The platform team's roadmap is in review/platform_roadmap.md and I'm reviewing it on Friday. Does it hold up against our goals for the half, and what should I ask them?
```

**Example result.** None yet

**Limits.** it judges the roadmap as written and cannot see context the team never wrote down; a review is not a rewrite, and C03 does the rewrite; scores are judgments, each with its evidence quoted.

Fallback for critique: The pm skill lists every roadmap item that has no stated outcome, no evidence or no owner, quoting each one.

### F04
**Research credibility check**

**Problem.** A research report or deck recommends a big bet. The findings look convincing, but nobody has checked whether the sources say what the report claims, how many people were asked, or how the questions were worded.

**You need.** the research report or deck; the decision it is meant to inform; optional: the raw data, survey questions or interview guide.

**Skills.** [pm](../skills/pm/SKILL.md) → [product-research](../skills/product-research/SKILL.md) → [critique](https://github.com/mshadmanrahman/pm-pilot/blob/main/plugins/pm-core/skills/critique/SKILL.md) (outside, optional)

**Steps.**
1. List the claims the recommendation depends on, quoting each one
2. Open every cited source and check that it says what the report says, marking each claim supported, partly supported, not supported or could not open
3. Check the method: who was asked, how many, how they were found, how the questions were worded, and when
4. Check the step from findings to recommendation: does the evidence support this bet, or only a smaller one
5. Search for the strongest evidence against the main conclusion
6. Give a verdict: good enough to decide on, usable with caveats, or not usable, and say what would raise it

**You get.** a claims table with a verdict and the source line for each claim; problems with the method; the strongest counter evidence found; an overall verdict and what would raise it.

**Checked by.** every checked claim cites the source line or says could not open; every method problem cites the part of the report it comes from; the verdict follows from the claims table; counter evidence is reported even when the verdict is positive.

**Setup.** web search and fetch allowed in Claude Code; python3 for the quote checker; optional: PM Pilot's pm-core plugin for critique (claude plugin marketplace add mshadmanrahman/pm-pilot, then claude plugin install pm-core@pm-pilot).

**Effort.** 15 to 30 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
An agency sent us a market report, research/agency_report.pdf, saying mid market finance teams will pay for AI forecasting. We're about to bet a quarter on it. How credible is it?
```

**Example result.** None yet

**Limits.** it cannot open paywalled or private sources, so those claims are marked could not open; it can find problems with the method only where the report describes its method; a credible report can still point to the wrong decision, because it checks the evidence, not your strategy.

Fallback for critique: The pm skill lists every claim the recommendation depends on and marks each one supported, partly supported, not supported or could not open.

### F05
**Strategy completeness review**

**Problem.** The product strategy is a long document that never makes a choice. Teams read it and still cannot say who the product is for, what it will not do, or why customers would switch, so every planning cycle starts from scratch.

**You need.** the strategy document; optional: the company goals and context/PRODUCT.md.

**Skills.** [pm](../skills/pm/SKILL.md)

**Steps.**
1. Check that the strategy answers each question in PM.md section 2: who exactly the customer is, their job, what they use today, what would make them switch, why now and why us, and what the product will not do
2. Find the diagnosis, meaning what the strategy says the main challenge is, quoted, or note that none is stated
3. Find the choices: what the strategy commits to and what it gives up, quoted
4. Check that the planned actions follow from the choices and do not contradict each other
5. Check that it says how success will be measured
6. Score it, quoting the line behind each score, and list the missing choices as questions for the strategy owner

**You get.** a completeness table against PM.md section 2; the diagnosis and choices found, quoted; contradictions between the choices and the actions; missing choices, written as questions; a scorecard.

**Checked by.** every finding quotes the strategy or says not found; the review names missing choices rather than making them; every contradiction cites both lines; the review does not add a strategy of its own.

**Setup.** Claude Code with this repo, as a plugin or a clone; the strategy as a file.

**Effort.** 10 to 20 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
Our product strategy for next year is in strategy/2027.md. Teams say they can't plan from it. Tell me what's missing and which choices it never actually makes.
```

**Example result.** None yet

**Limits.** it checks completeness and coherence, not whether the strategy is right; choices leadership made but never wrote down look missing, so confirm before raising them; a complete strategy can still be wrong, and that judgment belongs to people who know the market.

### F06
**Release go or no go**

**Problem.** A release is scheduled for Thursday. Test results, open bugs, the rollback plan and support readiness live in five places, and the go or no go call will be made on mood unless someone checks them against agreed criteria.

**You need.** the release scope with ticket status; test results and open bugs with their severity; the rollback plan, and whether it has been tested; monitoring and alerts for the changed parts; support and documentation status; your go or no go criteria, if the team has them.

**Skills.** [pm](../skills/pm/SKILL.md)

**Steps.**
1. Write the go or no go criteria before looking at the evidence; if the team has none, propose defaults and mark them as proposed
2. Check each criterion against evidence: a test report, a ticket, a dashboard link or a rollback that was tested
3. List the open bugs by severity against the threshold in the criteria
4. Check that the rollback has been tested, and that a named person will watch the release
5. Give a verdict: go, no go, or go with named conditions, each with an owner
6. Write what would change the verdict before the release time

**You get.** the criteria, marked agreed or proposed; a criteria table with the evidence for each; the open bugs against the threshold; a verdict with its conditions and owners.

**Checked by.** every criterion marked as met cites evidence; an untested rollback is never marked ready; the verdict is go, no go, or go with named conditions, never probably fine; proposed criteria are labelled as proposed.

**Setup.** Claude Code with this repo, as a plugin or a clone; the release evidence as files, because without a tracker connector it works only from what you export.

**Effort.** 10 to 15 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
Release 5.3 is set for Thursday. The test report, the open bug list, the rollback plan and the support checklist are in release/5.3/. Should we ship?
```

**Example result.** None yet

**Limits.** it checks that the evidence exists and meets the criteria, not that the software works; the verdict is a recommendation, and the release owner decides; for launching something new to market rather than releasing a change to an existing product, use the launch readiness check in G02.

### F07
**Check AI generated work against its inputs**

**Problem.** An AI tool turned meeting notes, transcripts or tickets into a summary, a PRD or a status report. Before you forward it, you need to know whether it invented a number, dropped a commitment or changed what someone said.

**You need.** the AI generated document; the inputs it was generated from.

**Skills.** [pm](../skills/pm/SKILL.md)

**Steps.**
1. List every number, date, name, commitment and quote in the AI generated document
2. Find each one in the inputs and paste the source line, or mark it not found
3. Recompute derived values such as totals, percentages and weekdays
4. Check in the other direction: list the commitments, decisions and risks in the inputs that the document dropped
5. Mark every paraphrase that says more than its source
6. Give a verdict: safe to forward, safe after the listed fixes, or start again, and write the fixes

**You get.** a claims table with the source line, or not found, for each claim; what the document dropped from the inputs; paraphrases that overstate their source; a verdict and a list of fixes.

**Checked by.** every claim has its source line pasted or is marked not found; derived values are recomputed with the working shown; the list of dropped items exists, even when it is empty; the verdict follows from the table.

**Setup.** Claude Code with this repo, as a plugin or a clone; the document and its inputs as files.

**Effort.** 5 to 15 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
Our AI note taker wrote this summary of yesterday's customer call, and I'm about to send it to the account team. The summary and the full transcript are in check/. Did it get anything wrong or leave anything out?
```

**Example result.** None yet

**Limits.** it checks faithfulness to the inputs, not whether the inputs were right; it cannot check claims whose source you do not provide; for an AI feature you are building, a one off check is not enough, so use F01 or I01 to build tests.

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

**Tested.** demo run: run 2026-10-11 with skill version 2 on synthetic inputs, graded by a separate reviewer with an answer key: 6 of 9 answer key criteria, but failed 2 of 8 checks: it offered the partner an old API version as a fallback the scope never mentions. Rerun the same day with version 3: key 6 of 9; both failed the skill's own checks. See examples/demos/G01-release-comms/run-2026-10-11/GRADE.md

**Example prompt.**

```text
Release 4.2 scope and our audiences are in examples/demos/G01-release-comms/input/. Write the release notes and the announcements, and the go live checklist.
```

**Example result.** examples/demos/G01-release-comms/run-2026-10-11/ (unedited outputs and the grade)

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

### G03
**Weekly status report from the tracker**

**Problem.** Every week someone asks where things stand, and the PM spends an hour copying ticket states into a document that is out of date by the time anyone reads it.

**You need.** a tracker export for the project, or connector access; last week's status report, if there is one; who reads it and what they need from it.

**Skills.** [pm](../skills/pm/SKILL.md) → [generate-status-report](https://github.com/atlassian/atlassian-mcp-server/blob/main/skills/generate-status-report/SKILL.md) (outside, optional) → [internal-comms](https://github.com/anthropics/skills/blob/main/skills/internal-comms/SKILL.md) (outside, optional)

**Steps.**
1. Pull the work items for the period and compare their states with last week's report
2. Flag items whose state has not changed in two weeks, because their status may be stale
3. Mark each workstream on track, at risk or off track, with the evidence for the call
4. List what shipped and what slipped, with the reason for each slip, quoting ticket titles or numbers
5. List the decisions needed, each with an owner and a date
6. Draft the report in the team's format, mark it DRAFT, and stop before anything is published to Confluence, Slack or email

**You get.** a status table by workstream, with evidence; what shipped and what slipped; stale items flagged; decisions needed, with owners; the draft report.

**Checked by.** every status cites the tickets or evidence behind it; nothing shown as shipped is unmerged or still open in the tracker; every slip states its reason or says reason unknown; nothing was published or sent.

**Setup.** Claude Code with this repo, as a plugin or a clone; a tracker export, or a connector; optional, for generate-status-report: an Atlassian Cloud site and Atlassian's plugin, which carries its skills and its MCP server (/plugin marketplace add atlassian/atlassian-mcp-server, then /plugin install atlassian@atlassian, then sign in with /mcp), though an admin may need to allow the connection; optional: the Linear MCP server, which needs a Linear workspace (claude mcp add --transport http linear-server https://mcp.linear.app/mcp, then sign in with /mcp), and this workflow only reads from it; optional: Anthropic's example skills for internal-comms, which the Claude apps already include on paid plans (in Claude Code: /plugin marketplace add anthropics/skills, then /plugin install example-skills@anthropic-agent-skills, which also installs ten other example skills).

**Effort.** 5 to 10 minutes of Claude time each week

**Tested.** untested

**Example prompt.**

```text
Write this week's status for the billing project from Jira, in the same shape as last week's report in status/2026-10-04.md. Don't post it anywhere; I'll send it myself.
```

**Example result.** None yet

**Limits.** it trusts ticket states, so a ticket nobody updated gives a wrong status, which is why it flags the stale ones; Atlassian's skill can publish to Confluence, and this workflow never lets it without your approval; the reason for a slip often lives in someone's head, so it asks rather than guesses.

Fallback for generate-status-report: The pm skill builds the report from the exported ticket list you provide.

Fallback for internal-comms: The pm skill uses the status update template in PM.md section 5.

### G04
**Risk summary for the people who can act**

**Problem.** Delivery risks are scattered across a risk log, ticket comments and standup notes. Leadership sees thirty items or none, and cannot tell which three need a decision from them this week.

**You need.** the risk log, a tracker export, or the notes where risks are recorded; the delivery dates and goals at stake; who the summary is for and what they can decide.

**Skills.** [pm](../skills/pm/SKILL.md)

**Steps.**
1. Collect every risk with its source, its owner and the date it was raised
2. Merge duplicates, and drop risks that are closed, citing what closed them
3. For each open risk, state what it threatens, its likelihood and impact as judgments, its trend since the last summary, and the cost of waiting
4. Pick the three that need a decision from this audience, and for each write the options and what each option costs
5. List the other open risks in a short table, so nothing is hidden
6. Write the one page summary with the decisions first, marked DRAFT

**You get.** a one page risk summary with the decisions needed first; options and their costs for the top three risks; a table of the other open risks; risks closed since the last summary.

**Checked by.** every risk cites where it was recorded; each of the top three asks for a specific decision; likelihood and impact are labelled as judgments; no owner is invented, and needs owner is written instead; nothing was sent.

**Setup.** Claude Code with this repo, as a plugin or a clone; the risk sources as files, because without a tracker connector it works only from what you export.

**Effort.** 10 to 15 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
We have 34 open risks across the risk log and Jira for the platform migration, and leadership meets Monday. Give me a one page summary with the three decisions they need to make.
```

**Example result.** None yet

**Limits.** it can rank only the risks someone recorded, and finding new ones before you commit is C06; likelihood and impact are judgments, and it shows its reasons so you can change them; it drafts, and you send it.

### G05
**Post launch review**

**Problem.** Launches end with a celebration and no review. Nobody compares the result with the goal set at the start, so the same estimate misses, scope changes and communication gaps repeat on the next launch.

**You need.** the launch goal and success metric as written before launch, if they exist; the metrics since launch; the plan compared with what happened: dates, scope changes, incidents; the team's notes on what went well and badly.

**Skills.** [pm](../skills/pm/SKILL.md) → [metrics-review](https://github.com/anthropics/knowledge-work-plugins/blob/main/product-management/skills/metrics-review/SKILL.md) (outside, optional)

**Steps.**
1. Restate the goal and success metric written before launch, quoting the source, or state that none was written
2. Compare the results with the goal, taking every number from the metrics
3. Compare the plan with what happened: dates, scope, incidents and their causes, without blaming people
4. Collect what the team says went well and badly, and count how many people raised each point
5. Decide for the feature whether to scale, iterate, hold or retire it, with the evidence
6. Turn the top three lessons into changes to how the next launch is run, each with an owner

**You get.** the goal compared with the result; the plan compared with what happened; what went well and badly, with counts; a decision for the feature; three changes for the next launch, with owners.

**Checked by.** the goal quoted is the one written before launch, never one written afterwards; every number matches the metrics; the review describes events and decisions, not people's faults; every lesson becomes a change with an owner or needs owner.

**Setup.** Claude Code with this repo, as a plugin or a clone; the data as an export, or a connection to Amplitude, Mixpanel or PostHog instead, each of which needs an account (the commands are in resources/README.md); optional: Anthropic's product management plugin for metrics-review (claude plugin marketplace add anthropics/knowledge-work-plugins, then claude plugin install product-management@knowledge-work-plugins), which registers remote connectors that read nothing until you sign in to one.

**Effort.** 15 to 25 minutes of Claude time; a 30 minute team review of yours

**Tested.** untested

**Example prompt.**

```text
We launched team workspaces 60 days ago. The launch plan, the goal we set, the metrics since then and the team's retro notes are in review/workspaces/. Write the post launch review and tell me what we change next time.
```

**Example result.** None yet

**Limits.** without a goal written before launch it cannot judge success, so it says so and recommends setting one next time; for a closer look at who uses the feature, run the adoption workflow in E06; lessons matter only if the next launch plan uses them, so it lists them for you to apply.

Fallback for metrics-review: The pm skill compares each launch metric with its target itself and shows the numbers.

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

### H03
**PM interview preparation**

**Problem.** A PM interview loop starts next week. Your stories are unstructured, your product sense answers wander, and you are not sure which details from your current job are confidential.

**You need.** the job description and the interview stages, if you know them; your projects from the last three years, from memory; optional: your CV.

**Skills.** [pm](../skills/pm/SKILL.md) → [deidentify](../skills/deidentify/SKILL.md) → [product-sense-interview-answer](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/product-sense-interview-answer/SKILL.md) (outside, optional)

**Steps.**
1. Map the stages of the loop to the question types you will face: product sense, execution, analytics, behavioural and strategy
2. Interview you about your projects and build a story bank around decisions you made yourself, including one where you were wrong
3. Run deidentify on the story bank, so no confidential name or number is said in an interview
4. Write practice questions for each stage, and a structure for answering each type
5. Run a mock interview one question at a time, and give feedback on structure, clarity and evidence
6. List the weak spots to practise before the loop

**You get.** a map of the stages to question types; a story bank stripped of confidential details; practice questions with answer structures; feedback from the mock interview; a practice list.

**Checked by.** every story is built from what you said, with no invented result or metric; no employer name, customer name or exact confidential figure survives in the story bank; each story names a decision you made yourself; feedback quotes the part of your answer it refers to.

**Setup.** Claude Code with this repo, as a plugin or a clone; optional: Dean Peters' product-sense-interview-answer skill (/plugin marketplace add deanpeters/Product-Manager-Skills, then /plugin install product-sense-interview-answer@pm-skills), but Pawel Huryn's collection uses the same marketplace name, pm-skills, so adding both can clash.

**Effort.** 20 to 40 minutes of Claude time across two sessions; an hour or more of your own practice

**Tested.** untested

**Example prompt.**

```text
I have a senior PM loop at a fintech company next week: product sense, execution and a behavioural round. Help me build my stories from my last three projects and run a mock product sense round.
```

**Example result.** None yet

**Limits.** the outside skill's licence is non commercial: check it before using it for paid work; it cannot know what your employment contract allows, so deidentify flags and stops when unsure; practise with a person as well, because a model cannot judge how you come across in a room.

Fallback for product-sense-interview-answer: The pm skill gives you an answer structure itself: clarify the goal, pick a user, list their problems, choose one, propose solutions, pick one and say how you would measure it.

### H04
**Product teardown**

**Problem.** You want to sharpen your product sense or show it in public, and most teardowns you read are opinions about a product with no evidence behind them.

**You need.** the product and the part to focus on, such as onboarding or pricing; screenshots you took while using it, with their dates; optional: what the teardown is for, such as practice or a post.

**Skills.** [pm](../skills/pm/SKILL.md) → [product-research](../skills/product-research/SKILL.md)

**Steps.**
1. Walk through the flow from your screenshots and record what happens at each step, as observation
2. Gather public evidence about the product's strategy and pricing, quoting every page with its date
3. Infer the bets the company seems to be making, each labelled as inference, with its evidence
4. Name what works and what does not, and why, tying each point to an observation or a source
5. Propose what you would change and how you would measure it
6. If the teardown will be published, remove any claim about the company's internal numbers that has no public source

**You get.** a step by step walkthrough with screenshots; the company's likely bets, labelled as inference; what works and what does not, with evidence; your proposed changes and how to measure them; a sources file.

**Checked by.** every claim is marked as observation, sourced fact or inference; no internal metric of the company is stated as fact without a public source; every quote matches its page; every proposed change has a metric.

**Setup.** Claude Code with this repo, as a plugin or a clone; web search and fetch allowed in Claude Code; python3 for the quote checker.

**Effort.** 20 to 40 minutes of Claude time; an hour of yours using the product and taking screenshots

**Tested.** untested

**Example prompt.**

```text
I want to tear down the onboarding of a well known note taking app for my portfolio. My screenshots from signing up yesterday are in teardown/. What are they betting on, and what would I change?
```

**Example result.** None yet

**Limits.** it cannot use the product for you, so your screenshots are the observation; anything about a company's internal data is inference unless the company published it; public pages change, so every source carries its date.

### H05
**Skills gap to learning plan**

**Problem.** You want the next role, such as group PM or director, and the feedback you get is vague, such as 'be more strategic'. You do not know which gaps matter most or how to close them while doing your job.

**You need.** the target role: a job description or your company's career ladder; your current role and evidence of your work, from memory or a self review; optional: feedback you have received, quoted; the hours a week you can spend on learning.

**Skills.** [pm](../skills/pm/SKILL.md) → [career](https://github.com/menkesu/awesome-pm-skills/blob/main/skills/career/SKILL.md) (outside, optional) → [director-readiness-advisor](https://github.com/deanpeters/Product-Manager-Skills/blob/main/skills/director-readiness-advisor/SKILL.md) (outside, optional)

**Steps.**
1. List the target role's expectations, quoted from the ladder or the job description
2. Record your evidence against each expectation from what you tell it, and mark each gap as clear, partial or unknown
3. Rank the gaps by how much they matter for the target role and how much of your feedback points to them
4. For the top three gaps, design learning that produces something each week: a document, a decision, a shipped change or a conversation
5. Fit the plan to the hours you have, week by week, for six to eight weeks
6. Write how you will know each gap is closing, and when to review the plan

**You get.** a table of the role's expectations against your evidence; the top three gaps, with reasons; a six to eight week learning plan where every week ends in an artifact; review points.

**Checked by.** every expectation is quoted from the ladder or the job description; your evidence comes from what you said, with nothing invented; every learning block produces an artifact; the plan fits the stated hours; every course, book or link it recommends is real and one you can open, and none is invented.

**Setup.** Claude Code with this repo, as a plugin or a clone; optional: Udi Menkes' Awesome PM Skills for career (/plugin marketplace add menkesu/awesome-pm-skills, then /plugin install awesome-pm-skills@awesome-pm-skills); optional: Dean Peters' director-readiness-advisor skill (/plugin marketplace add deanpeters/Product-Manager-Skills, then /plugin install director-readiness-advisor@pm-skills), but Pawel Huryn's collection uses the same marketplace name, pm-skills, so adding both can clash.

**Effort.** 20 to 30 minutes of Claude time; the learning itself is yours

**Tested.** untested

**Example prompt.**

```text
I'm a group PM and I want to be ready for a director role within a year. Our career ladder is in career/ladder.md and my last two reviews are in career/reviews/. Where are my real gaps? Give me an eight week plan I can do in four hours a week.
```

**Example result.** None yet

**Limits.** the outside skill's licence is non commercial: check it before using it for paid work; it judges you only on what you tell it, so ask your manager to check the gap table; it suggests a learning resource only when it can name one you can check, and otherwise it says to find a source.

Fallback for career: The pm skill builds the plan itself: gaps ranked by how much they matter for the target role, each with a practice and an artifact.

Fallback for director-readiness-advisor: The pm skill uses the target role's own description as the only standard and says that no director specific guidance was used.

## I · AI product work

### I01
**Evals from your AI feature's real outputs**

**Problem.** Your AI feature has real users or a beta, and the team argues about its quality from a few screenshots. Nobody knows which failures happen most, and the tests you have were imagined before launch.

**You need.** a sample of 50 to 200 real outputs or traces, as JSONL, CSV or JSON, with customers' personal data removed; what the feature promises its users; optional: the feature's spec and any existing tests.

**Skills.** [pm](../skills/pm/SKILL.md) → [eval-write](../skills/eval-write/SKILL.md) → [error-discovery](https://github.com/ai-evals-course/evals-skills/blob/main/skills/error-discovery/SKILL.md) (outside, optional) → [validate-evaluator](https://github.com/ai-evals-course/evals-skills/blob/main/skills/validate-evaluator/SKILL.md) (outside, optional)

**Steps.**
1. Write the checks a good output must pass, from the feature's promise to its users; these are the contract eval-write needs
2. Review a sample of real outputs one by one, writing pass or fail and a short note on what went wrong
3. Group the notes into failure modes and count how often each one occurs
4. For each common failure mode, choose a code check where a rule can catch it, or an LLM judge where it cannot
5. Check every LLM judge against your own labels on outputs it has not seen, and trust it only if it agrees well on both passes and failures
6. Turn the most important failures into frozen golden inputs with eval-write

**You get.** a labelled sample of outputs; failure modes ranked by how often they occur; a code check or a judge for each common failure mode; how often each judge agrees with your labels; new golden inputs.

**Checked by.** every failure mode cites the outputs that show it; the counts recount from the labels; no judge is used without its agreement with human labels reported; the golden inputs come from observed failures, not imagined ones.

**Setup.** Claude Code with this repo, as a plugin or a clone; your outputs or traces as files; optional: Shreya Shankar and Hamel Husain's eval skills for error-discovery and validate-evaluator (/plugin marketplace add ai-evals-course/evals-skills, then /plugin install evals@ai-evals-course); error-discovery needs Python 3 and serves its review app from a local Python server.

**Effort.** 15 to 30 minutes of Claude time; an hour or more of yours labelling outputs

**Tested.** untested

**Example prompt.**

```text
Our AI reply drafter for support has been in beta for a month. I exported 150 conversations to evals/traces.jsonl. Help me find out how it actually fails, and build checks for the failures that matter.
```

**Example result.** None yet

**Limits.** the labels are yours, because the method depends on a person reading real outputs; a judge that agrees with one person's labels may not agree with another's, so label with two people if you can; traces must have customers' personal data removed before they go in.

Fallback for error-discovery: The pm skill shows you the outputs one at a time in the session, records your pass or fail and a note for each, and groups the notes into failure modes.

Fallback for validate-evaluator: The pm skill compares the judge's verdicts with your labels on outputs the judge has not seen, and reports how often they agree on passes and on failures, with the counts.

### I02
**Prompt or agent spec**

**Problem.** Engineering is about to build an AI feature or agent from a one line idea. Nobody has written down what it may do on its own, what it must never do, what it does when unsure, or how anyone will know it works.

**You need.** the idea and the user problem it solves; the data and tools the agent could touch; the actions with real consequences, such as sending, deleting or spending; optional: example inputs and good outputs.

**Skills.** [pm](../skills/pm/SKILL.md) → [eval-write](../skills/eval-write/SKILL.md) → [skill-creator](https://github.com/anthropics/skills/blob/main/skills/skill-creator/SKILL.md) (outside, optional)

**Steps.**
1. Write the job: who uses it, the input it receives, the output it returns, and the event that means success
2. List every tool and data source it may use, and every action it may take on its own
3. List the actions that need a person's approval and the actions it must never take
4. Write what it does when it is unsure, when an input is missing, and when a tool fails
5. Write the output format, the cost and speed budget per task, and what gets logged
6. Write the checks it must pass, then the five frozen golden inputs with eval-write

**You get.** an agent spec: job, inputs, outputs, tools, permissions, refusal rules, failure behaviour, budgets and logging; a checks table; five frozen golden inputs; open questions for engineering.

**Checked by.** every action is classed as allowed, needs approval, or never; every action that cannot be undone needs approval; what it does when unsure is written down; every check can be failed by at least one golden input.

**Setup.** Claude Code with this repo, as a plugin or a clone; optional: Anthropic's example skills for skill-creator, which the Claude apps already include on paid plans (in Claude Code: /plugin marketplace add anthropics/skills, then /plugin install example-skills@anthropic-agent-skills, which also installs ten other example skills); skill-creator runs Python scripts to run and compare evals.

**Effort.** 20 to 40 minutes of Claude time; your time on the permission rules

**Tested.** untested

**Example prompt.**

```text
We want an agent that triages incoming support tickets and drafts replies. Write the spec engineering builds from, including what it may never do on its own, and the tests it has to pass.
```

**Example result.** None yet

**Limits.** a spec does not make an agent safe, while tests and a staged rollout do; it cannot know your security and legal rules, so add them before engineering starts; golden inputs written before launch catch imagined failures, so add real ones later with I01.

Fallback for skill-creator: The pm skill writes the spec as a plain document for your engineers and does not build a skill.

### I03
**Choose between models with a test**

**Problem.** The team picked a model because of a launch announcement or a public benchmark that looks nothing like your task. Nobody has compared the candidates on your own inputs, cost and speed.

**You need.** the task, with 20 to 50 real example inputs and what good outputs look like; the two or three models or prompt versions to compare; API access to each, with keys kept in environment variables and never in prompts or files; a budget for the test runs.

**Skills.** [pm](../skills/pm/SKILL.md) → [eval-write](../skills/eval-write/SKILL.md) → [generate-synthetic-data](https://github.com/ai-evals-course/evals-skills/blob/main/skills/generate-synthetic-data/SKILL.md) (outside, optional) → [write-judge-prompt](https://github.com/ai-evals-course/evals-skills/blob/main/skills/write-judge-prompt/SKILL.md) (outside, optional)

**Steps.**
1. Write the decision, the checks a good output must pass, and the limits on cost and speed
2. Build a frozen test set from real inputs with eval-write, adding labelled synthetic inputs only to cover gaps
3. Get approval for the cost of the runs, then run every candidate on the same set with the same settings
4. Grade the outputs with the model names hidden, using code checks where possible and a judge only for what code cannot check
5. Compare the pass rate for each check, the cost per thousand tasks and the speed, showing every calculation
6. Make the call, name what would reverse it, and keep the set for the next model release

**You get.** a frozen test set; a results table with the pass rate for each check, the cost and the speed of each candidate; the call and what would reverse it.

**Checked by.** every candidate ran on the identical frozen set; grading was done with the model names hidden; cost and speed figures come from the runs, with the working shown; synthetic inputs are labelled synthetic; nothing was spent before approval.

**Setup.** Claude Code with this repo, as a plugin or a clone; an account and an API key for each model, kept in environment variables; python3 to run and score the comparison; optional: Shreya Shankar and Hamel Husain's eval skills for generate-synthetic-data and write-judge-prompt (/plugin marketplace add ai-evals-course/evals-skills, then /plugin install evals@ai-evals-course).

**Effort.** 30 to 60 minutes of Claude time, plus the time the models take to run; your time labelling a sample

**Tested.** untested

**Example prompt.**

```text
We're choosing between two models for summarising sales calls. I have 40 real transcripts and the summaries our team rated good in evals/calls/. Run a fair test and tell me which one to use, with the cost per thousand calls.
```

**Example result.** None yet

**Limits.** running the models costs money, so it stops for your approval first; 40 examples show large differences, not small ones, so close results are reported as a tie; results expire with the next model release, so keep the set and run it again.

Fallback for generate-synthetic-data: The pm skill writes varied test inputs itself and labels every one of them synthetic.

Fallback for write-judge-prompt: The pm skill grades the outputs itself against a written checklist, with the model names hidden, and reports where the checklist could not decide.

### I04
**AI feature risk review**

**Problem.** An AI feature is close to launch, and the usual launch review asks nothing specific to AI: confident wrong answers, harmful output, prompt injection, data leaking between customers, or costs running away.

**You need.** the feature spec, or a description of what it does; the data it reads and the actions it can take; the results of any tests run so far; who uses it and what they rely on it for.

**Skills.** [pm](../skills/pm/SKILL.md) → [eval-write](../skills/eval-write/SKILL.md) → [eval-plan](https://github.com/menkesu/awesome-pm-skills/blob/main/skills/eval-plan/SKILL.md) (outside, optional)

**Steps.**
1. List what the feature reads, writes and does, and who relies on its output
2. Walk through the AI risks: wrong answers stated with confidence, harmful or biased output, prompt injection, data leaking between users or customers, people relying on it too much, outages, and runaway cost
3. For each risk, note its likelihood and impact as judgments, the evidence from tests so far, and the mitigation
4. Turn the top risks into adversarial test inputs with eval-write
5. Write the launch bar: the tests, thresholds and sign offs that must pass before launch, and the monitoring after it
6. List what needs a decision from legal, security or leadership

**You get.** an AI risk register with likelihood, impact, evidence, mitigation and owner; adversarial test inputs for the top risks; a launch bar with thresholds and sign offs; the decisions needed.

**Checked by.** every AI risk on the list is assessed, or marked not applicable with a reason; every high risk has a test in the launch bar; test evidence is cited, or the risk is marked untested; decisions for legal or security are named, not made.

**Setup.** Claude Code with this repo, as a plugin or a clone; optional: Udi Menkes' Awesome PM Skills for eval-plan (/plugin marketplace add menkesu/awesome-pm-skills, then /plugin install awesome-pm-skills@awesome-pm-skills).

**Effort.** 20 to 40 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
In three weeks we launch an AI assistant that answers questions about a customer's own account data. The spec and our test results so far are in ai/assistant/. What could go wrong, and what has to pass before we ship?
```

**Example result.** None yet

**Limits.** it does not replace a security review or legal advice, and it lists what they must decide; a review before launch misses failures that only real use reveals, so run I01 after launch; likelihood and impact stay judgments until tests measure them.

Fallback for eval-plan: The pm skill writes the launch bar itself: for each top risk, the test, the pass threshold and who signs it off.

## J · Stakeholders and leadership

### J01
**Executive update that asks for something**

**Problem.** Leadership reads your update in two minutes between meetings. The current one is a page of activity that buries the one decision you need from them.

**You need.** what happened since the last update: status, metrics, risks; the goals the work serves; the decisions or help you need, from whom, and by when; optional: your draft update.

**Skills.** [pm](../skills/pm/SKILL.md) → [exec-comms](https://github.com/menkesu/awesome-pm-skills/blob/main/skills/exec-comms/SKILL.md) (outside, optional)

**Steps.**
1. Write the asks first: each decision or kind of help needed, from whom, and by when
2. Report outcomes against goals in three to five lines, with numbers from the inputs
3. State the top risk and what you are doing about it
4. Cut activity that does not change a decision or a goal, and keep the cut material separately
5. Check every number against the inputs and mark the update DRAFT

**You get.** an update of five to ten lines with the asks first; the cut material, kept separately in case someone asks; a score against the rubric.

**Checked by.** the first line is an ask, or says there is no ask this time; every number matches its source; it stays under 250 words unless you set another limit; nothing was sent.

**Setup.** Claude Code with this repo, as a plugin or a clone; optional: Udi Menkes' Awesome PM Skills for exec-comms (/plugin marketplace add menkesu/awesome-pm-skills, then /plugin install awesome-pm-skills@awesome-pm-skills).

**Effort.** 5 to 10 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
My draft monthly update to our VP is in updates/october.md and it runs to two pages. I need her to approve a contractor for the data migration. Rewrite it so she reads the ask.
```

**Example result.** None yet

**Limits.** it cannot know your leaders' preferences unless you tell it or record them in context/PRODUCT.md; it drafts, and you send; a short update hides detail, so keep the cut material ready.

Fallback for exec-comms: The pm skill rewrites the update itself with the ask first, outcomes against goals second and detail last, then rates it on the rubric in PM.md section 7.

### J02
**Decision memo when leaders disagree**

**Problem.** Two leaders want different things, such as the enterprise feature or the onboarding fix, and the decision is deferred meeting after meeting while the team waits.

**You need.** the decision and the options on the table; each side's position, quoted wherever it is written down; the evidence for each option; who decides, and by when.

**Skills.** [pm](../skills/pm/SKILL.md) → [decide](https://github.com/menkesu/awesome-pm-skills/blob/main/skills/decide/SKILL.md) (outside, optional)

**Steps.**
1. State the decision in one sentence, with who makes it and by when
2. Write each option in the words its supporters would use, with its evidence and confidence
3. Write what each option costs: what it delays, what it risks and what it needs
4. Recommend one option, say what would reverse the recommendation, and set kill criteria and a review date
5. Check that each side would agree their option is described fairly, and mark the memo DRAFT

**You get.** a one page decision memo; each option described in its supporters' terms, with evidence; what each option costs; a recommendation with kill criteria and a review date.

**Checked by.** each option is described as its supporters would describe it; every piece of evidence cites its source; the memo names who decides and by when; the kill criteria are measurable.

**Setup.** Claude Code with this repo, as a plugin or a clone; optional: Udi Menkes' Awesome PM Skills for decide (/plugin marketplace add menkesu/awesome-pm-skills, then /plugin install awesome-pm-skills@awesome-pm-skills).

**Effort.** 10 to 20 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
Our head of sales wants SSO and audit logs next quarter; our head of growth wants to fix onboarding. It has been deferred three times. Notes from both and the data we have are in decisions/q1/. Write the memo that gets it decided.
```

**Example result.** None yet

**Limits.** it can make the trade off clear but cannot make leaders agree; a fair description of each side needs their own words, so it asks for them rather than paraphrasing; the recommendation is yours to stand behind or change.

Fallback for decide: The pm skill writes the memo itself from the decision brief template in PM.md section 5, adding kill criteria and a review date.

### J03
**Saying no with evidence**

**Problem.** A senior stakeholder or a large customer asks for something that does not fit the plan. Saying yes would displace work that matters more, and a bare no will damage the relationship.

**You need.** the request, in the requester's words; the current plan, and what the request would displace; evidence: how many customers need it, usage data, the strategy; optional: what you could offer instead.

**Skills.** [pm](../skills/pm/SKILL.md)

**Steps.**
1. Restate the request as the need behind it, in the requester's words
2. Check the evidence for the need: how many customers have it, or how much revenue depends on it, from the inputs
3. Show what saying yes would displace, and what that would cost
4. Find what you can offer: a smaller version, a workaround, a later date with a condition, or an existing feature that already helps
5. Draft the reply: what you heard, the decision, the reason with its evidence, the alternative, and when you would look at it again
6. Mark the reply DRAFT and list the risks of sending it

**You get.** a short analysis of the request against the plan; a draft reply with the reason and an alternative; what would change the answer.

**Checked by.** the need is stated in the requester's words; the reason cites evidence, not opinion alone; the reply offers an alternative or says honestly that there is none; nothing was sent.

**Setup.** Claude Code with this repo, as a plugin or a clone.

**Effort.** 5 to 15 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
Our largest customer wants a custom reporting module by March, and it would push back the onboarding work for everyone else. Their email and our plan are in requests/. Help me say no in a way that keeps the relationship.
```

**Example result.** None yet

**Limits.** it drafts, and you decide whether the answer really is no; it cannot know commercial promises sales made unless you include them; a reply is not a relationship, and a call may land better than an email.

### J04
**One on one preparation**

**Problem.** A one on one with your manager or a key stakeholder is in half an hour. Open items are scattered across chat, documents and the tracker, and you will walk out without the decision you needed.

**You need.** who the meeting is with and what they care about; open items since the last meeting: notes, threads, tickets; what you need from this meeting.

**Skills.** [pm](../skills/pm/SKILL.md) → [meeting-prep](https://github.com/mshadmanrahman/pm-pilot/blob/main/plugins/pm-core/skills/meeting-prep/SKILL.md) (outside, optional)

**Steps.**
1. Write the one thing you need to leave the meeting with
2. Gather the open items since the last meeting, and the status of everything you promised them
3. Order the agenda: your ask first, then their likely concerns, then updates
4. For the ask, write the evidence and the options in two or three lines
5. Write the questions you want to ask them

**You get.** a one page agenda with your ask first; the status of your promises to them; the evidence for your ask; your questions.

**Checked by.** the agenda starts with a specific ask, or says there is none; every promise listed cites where it was made; nothing is written about the other person that you did not provide; the agenda fits the length of the meeting.

**Setup.** Claude Code with this repo, as a plugin or a clone; optional: PM Pilot's pm-core plugin for meeting-prep (claude plugin marketplace add mshadmanrahman/pm-pilot, then claude plugin install pm-core@pm-pilot); meeting-prep reads Jira, Slack, Calendar and Granola through connectors you add, so without them you paste the items in; for Jira, use Atlassian's own server from resources/README.md rather than the community server that PM Pilot's README links.

**Effort.** 5 to 10 minutes of Claude time

**Tested.** untested

**Example prompt.**

```text
I have a one on one with my director in 30 minutes. My notes from last time and this week's threads are in 1on1/. I need her to decide whether we pause the reporting work. Prep me.
```

**Example result.** None yet

**Limits.** notes about colleagues are sensitive, so keep them on your machine and out of shared repositories; it prepares you, and the conversation is yours; it cannot read tools you have not connected.

Fallback for meeting-prep: The pm skill builds the agenda from the notes and items you paste in.
