# Research map — Is an in-app AI assistant the right call for a B2B analytics product (~2,000 accounts, data teams at mid-size companies)? — 2026-10-09

> **Read this first (the "prove it" request).** You asked for supporting evidence only. This map is complete: it contains what contradicts the belief too, in its own rows and in the *Contradicting evidence* line of the verdict, so you can choose what goes on Thursday's slides. The map is complete; the deck is yours.

## 0 · Ground truth (written 2026-10-09 19:35 IST, before the first search)

| Field | Ground truth |
|---|---|
| **Decision** | Already made (last week, with the CEO): **build** an in-app AI assistant. What this map can still change at Thursday's leadership review: proceed as scoped · re-scope (which job the assistant does, for whom) · re-sequence. *Decision is from the user; what the review can change is drafted — unconfirmed.* |
| **Goal it serves** | Not given. Asked for: the number this is meant to move (expansion revenue? retention/NRR? weekly active users per account? seat growth beyond the data team?) and the size of move that would matter. *ASK — unconfirmed.* |
| **Belief B1** *(drafted — unconfirmed)* | The PM believes data teams at mid-size companies want an AI assistant inside their analytics product — there is real, unprompted user pull. |
| **Belief B2** *(drafted — unconfirmed)* | The PM believes competitors that have shipped in-app AI assistants show evidence it was the right call — adoption or revenue, not just launch announcements. |
| **Falsifier** *(drafted — unconfirmed)* | B1 drops if unprompted public talk from data practitioners is mostly distrust/rejection of in-product AI assistants (accuracy, hallucinated numbers, "won't use it") rather than asking for one. B2 drops if shipped assistants show no public adoption evidence, were scaled back, or were given away free because they could not be charged for. |
| **Already known** | "We've been through the counter-arguments" — not shared with this run, so not excluded. Decision made with the CEO last week. Nothing else supplied. |

## 1 · The map

| Segment | Their words (verbatim, S#) | What they use today | What is missing | Where they are |
|---|---|---|---|---|
| **Business stakeholders** in your accounts (the people your data teams serve) | "They just want a way to ask questions in prose and get an answer back…" (S4) · data "just sits there because the people who need the information don't know how to query the database" (S5, vendor voice) | Dashboards, and asking the data team in Slack | An answer they can trust without being able to check the SQL | Inside your 2,000 accounts, as viewers; Slack/Teams (S7) |
| **Data teams** (your buyers and core users) | "it works just enough to be dangerous" (S2) · "the users that get the most value out of this are the ones without the ability to validate the generated SQL" (S3) · "With Text-to-SQL I can express my query in natural language" (S8) | AI for code and docs: 80% use AI somewhere in their workflow (S23) | Confidence the assistant will not put wrong numbers in front of stakeholders; data quality is their top worry (S24) | HN threads on text-to-SQL (S28); Reddit not reachable this run (S10) |
| **Competitors** | "more than 52% of ThoughtSpot customers were actively leveraging the product" (S12) · "Over 4,000 customers adopted AI/BI Genie during its preview" (S13) · Snowflake Intelligence ~2,500 weekly accounts in 3 months (S14) | Chat/agent layers on top of governed data models | Independent adoption data; every number is vendor-reported | Launch posts, earnings releases |

**Cases to follow**

| Case | What they did | Good | Bad | Ugly | Source |
|---|---|---|---|---|---|
| Tableau Ask Data → Pulse | Retired its natural-language query feature in Feb 2024 and replaced it with Pulse (metrics + generated insights) | They kept investing in natural language | The first version was retired | The replacement moved away from open-ended Q&A and towards set metrics | S17 |
| Power BI Q&A → Copilot | Retiring the old natural-language tool by Dec 2026 and moving users to Copilot | The bet survived into the LLM generation | Two overlapping features had to be merged | Existing Q&A visuals stop working | S18 |
| ThoughtSpot Spotter | Put an AI analyst at the centre of the product | 52% of customers "actively leveraging" it, by its own count | "Actively" is not defined | Vendor-reported only | S12 |

## 2 · Angles

### 1 · Goal — approach: ask; why: the "right call" can only be judged against the number it should move; searched: nothing (this is your number, not the web's)
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 1.1 | No goal metric was supplied with the decision. Asked for the number the assistant should move and by how much | S1 | ASK | unknown (B1, B2) | Next step: this is the named gap |
**Insight:** Read through *Escaping the Build Trap* (Perri), a decision with no outcome attached is an output; it will end up judged on whether it launched. · **Belief:** unknown · **Also changes:** the next step.

### 2 · Lay of the land — approach: competitor sites, earnings releases, launch posts; why: B2 needs evidence of use, not launches; searched: ThoughtSpot, Databricks Genie, Snowflake Intelligence, Amplitude, Mixpanel
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 2.1 | ThoughtSpot: more than 52% of customers actively using Spotter by fiscal year end (vendor-reported) | S12 | HIGH | confirms (B2) | Mark: vendor self-report; "actively" undefined |
| 2.2 | Databricks: over 4,000 customers adopted AI/BI Genie during preview | S13 | HIGH | confirms (B2) | Vendor self-report; "adopted" undefined |
| 2.3 | Snowflake: ~2,500 accounts using Snowflake Intelligence weekly within 3 months (4-week average) | S14 | MEDIUM | confirms (B2) | The best-defined usage number found (weekly, in an SEC filing) |
| 2.4 | Amplitude's FY2025 release announces agents but gives no usage figure for its AI | S15 | HIGH | contradicts (B2) | Weak: a launch with no adoption evidence, for the closest product-analytics peer |
| 2.5 | Mixpanel renamed Spark AI to "Mixpanel Agent" | S16 | HIGH | unknown (B2) | Positioning: the category is moving from "assistant" to "agent" |
**Insight:** Through *Crossing the Chasm* (Moore), vendor launches are not buyer adoption. Three independent vendors do report usage (2.1–2.3), which makes it a pattern, but every figure is self-reported. · **Belief:** confirms (B2) · **Also changes:** the deck should label these as vendor-reported.

### 3 · The users' words — approach: HN Algolia comments and threads, Reddit archive API, dbt survey; why: unprompted pain; searched: "text-to-sql", "chat with your data", "AI data analyst", Reddit subs (blocked)
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 3.1 | "They just want a way to ask questions in prose and get an answer back" | S4 | HIGH | confirms (B1) | Who "they" are: business users, not data teams |
| 3.2 | Warehouse data "just sits there" because the people who need it cannot query it | S5 | HIGH | confirms (B1) | Vendor voice (Vanna author); the pull comes from stakeholders |
| 3.3 | A former SQL user values asking in natural language | S8 | HIGH | confirms (B1) | Data-literate users are a second segment |
| 3.4 | 80% of data practitioners use AI somewhere in their workflow | S23 | HIGH | confirms (B1) | Adjacent: mostly AI for code and docs, not an in-BI assistant |
| 3.5 | Text-to-SQL "works just enough to be dangerous" | S2 | HIGH | contradicts (B1) | Build: accuracy and guardrails are the product |
| 3.6 | The users who get the most value are the ones who cannot validate the SQL | S3 | HIGH | contradicts (B1) | The data team carries the risk of wrong answers, so it is not obviously the segment that wants this |
| 3.7 | AI analytics demos only show trivial "aggregated revenue over time" questions | S6 | HIGH | contradicts (B1) | The method: test on real customer questions, not demo ones |
| 3.8 | "nobody wants another webapp if they can use Slack or Teams" | S7 | HIGH | contradicts (B1) | Weak, from a vendor; scope: the in-app surface may not be where the question gets asked |
| 3.9 | Data quality and trust in data stay the top concern of data teams | S24 | HIGH | contradicts (B1) | Adjacent; the assistant inherits whatever data quality each account has |
| 3.10 | Reddit could not be reached (archive API rate-limited) | S10 | ZERO | unknown (B1) | Gap: Reddit voice is missing; HN only |
| 3.11 | Searches for "wrong numbers" / "useless" complaints returned nothing relevant | S11 | NONE | unknown (B1) | — |
**Insight:** Read through JTBD, the job is "get my stakeholder an answer without me in the loop". Demand comes from the stakeholders (3.1–3.2). Data practitioners' own words are mostly wary (3.5–3.8). That is a weak signal: one platform, four people. · **Belief:** contradicts (B1, as written for data teams) · **Also changes:** who the assistant is spec'd for.

### 4 · Offerings, and evidence of use — approach: pricing pages, prior-generation usage; why: does anyone pay, and is it used; searched: Metabase, Hex pricing; Activant research
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 4.1 | Self-service BI: 87% enterprise adoption but ~26% active usage | S21 | MEDIUM | contradicts (B1) | Adjacent: the last "let business users ask" wave stalled; secondary figure |
| 4.2 | "The result is output that business users simply don't trust." | S22 | HIGH | contradicts (B1) | Opinion from a VC note; trust is the adoption gate |
| 4.3 | Metabase: most customers bring their own LLM key; otherwise $3.75 per 1M tokens | S25 | HIGH | unknown (B2) | Pricing: AI sold at cost, not as a premium tier |
| 4.4 | Hex: AI consumes credits included in paid seats, with add-on credits | S26 | HIGH | unknown (B2) | Pricing: usage pass-through; weak signal (2 sources with 4.3) |
**Insight:** Kano cannot be read from competitor counts. What the pricing shows (weak signal, 2 sources) is AI sold at cost, which suggests a defence and retention play rather than a new revenue line. · **Belief:** unknown · **Also changes:** which goal it can credibly move.

### 5 · Method — the PM canon (never cut) — approach: FRAMEWORKS.md card applied to the evidence above; why: the review should hear the decision in PM terms
| # | Framework · what it predicts here | What the evidence says | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|---|:--:|---|---|
| 5.1 | **JTBD** (Christensen, *Competing Against Luck*): the hired job is "answer a stakeholder's question without waiting on the data team"; the competing alternative is a Slack message to the analyst | Agrees: pull comes from non-SQL users (S4, S5); Slack is named as the surface (S7) | S4, S5, S7 | HIGH | contradicts (B1) | Spec the user as the stakeholder; the data team becomes the admin and approver |
| 5.2 | **Four big risks** (Cagan, *Inspired*): value risk retired first, then feasibility | Value is partly retired by competitor adoption (S12–S14). Feasibility is not: 10.1% / 21.3% on enterprise-realistic SQL (S19, S20) | S12, S13, S19, S20 | HIGH | confirms (B2) | Build: feasibility (accuracy) is the unretired risk |
| 5.3 | **Kano** (Kano, 1984): if basic, its absence costs and its presence earns nothing | Can't be judged: it is measured from customers' answers, which this map does not have. Competitor counts are not Kano | — (S1 gap) | ASK | unknown (B1) | Method: a Kano question pair in the next customer survey |
| 5.4 | **Opportunity Solution Tree** (Torres, *Continuous Discovery Habits*) / **Escaping the Build Trap** (Perri): a solution chosen before the outcome is named | Agrees: decided with the CEO, goal not stated (S1) | S1 | ASK | unknown (B1, B2) | Put the decision on a tree: outcome → opportunity (stakeholder self-serve) → solution |
| 5.5 | **Crossing the Chasm** (Moore): pragmatists buy proof from peers, not launches | Only vendor-reported adoption exists; the closest peer (Amplitude) published none (S15) | S12, S15 | HIGH | contradicts (B2) | The deck: label the figures as vendor claims |
| 5.6 | **Lean** (Ries, *The Lean Startup*): the smallest test of the riskiest assumption | Riskiest assumption: accuracy on your customers' real questions (S6, S19) | S6, S19 | HIGH | unknown (B1) | After the gap: a gold set of real questions from 10 accounts before general release |
**Insight:** Through Cagan, the decision is defensible on value (B2), but it is exposed on feasibility; through JTBD, it is aimed at the wrong user if the spec says "data teams". · **Belief:** contradicts (B1), confirms (B2) · **Also changes:** spec scope.

### 6 · Cases — good, bad, ugly — approach: official docs, retirement notices, builder write-ups; why: who did it before; searched: "Ask Data retired", "Power BI Q&A deprecation", "lessons building AI data analyst"
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 6.1 | Tableau retired Ask Data (natural-language query) in Feb 2024 | S17 | HIGH | contradicts (B2) | It was replaced, not abandoned: the category was kept, that version was not |
| 6.2 | Microsoft retires Power BI Q&A by Dec 2026, moving users to Copilot | S18 | HIGH | contradicts (B2) | Same as 6.1: the generation before LLMs failed and was replaced |
| 6.3 | A builder: "Text-to-SQL is not enough"; a semantic layer and context are the product | S27 | HIGH | unknown (B2) | Build: budget for the semantic/context layer, not only the chat UI |
**Insight:** Through Build-Measure-Learn, the two biggest BI vendors already ran this experiment once and killed the result. Both re-bet with LLMs, which supports the category while warning against copying the old shape. · **Belief:** contradicts (B2) · **Also changes:** design (governed metrics first).

### 7 · Constraints — approach: benchmark sites and papers, practitioner threads; why: what limits the build
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 7.1 | GPT-4o solves 10.1% of Spider 2.0 enterprise-style tasks, against 86.6% on Spider 1.0 | S19 | HIGH | unknown (B1) | Build: accuracy on real schemas is the main risk |
| 7.2 | The best agent framework solves 21.3% of Spider 2.0 tasks | S20 | HIGH | unknown (B1) | Same; a benchmark, not your schemas |
| 7.3 | Businesses are "incredibly sensitive" about leaking even metadata to an LLM | S9 | HIGH | unknown (B1) | Build: data processing terms, model choice, a bring-your-own-key option (compare S25) |
**Insight:** Through Cagan, feasibility is the risk this decision leaves open. · **Belief:** unknown · **Also changes:** the build plan and the security review.

### 8 · Distribution — approach: HN story search; why: where to recruit people outside the base; searched: S28
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 8.1 | Distribution is in-product to your 2,000 accounts. Outside the base, HN text-to-SQL threads draw 400–550 points; Reddit was not reachable | S28, S10 | NONE | unknown (B1) | Recruit interviewees from the base first |
**Insight:** Through the Mom Test, the follow-up evidence comes from your own accounts' past behaviour ("the last question you asked the data team"), not from forums. · **Belief:** unknown · **Also changes:** next step.

## 3 · Verdict

**Rows labelled *contradicts* in section 2 (listed before judging):** 2.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.1, 4.2, 5.1, 5.5, 6.1, 6.2 — 12 rows.

**Belief B1 (data teams want an in-app AI assistant):** still unknown, leaning contradicted for data teams as the segment. The three findings that decided it: 3.6 (the value goes to people who can't check the SQL), 3.1/3.2 (demand comes from stakeholders, not data teams), 3.5 ("works just enough to be dangerous").
**Belief B2 (competitors' assistants show it was the right call):** confirmed, on vendor-reported numbers: 2.1 (ThoughtSpot 52%), 2.2 (Genie 4,000), 2.3 (Snowflake ~2,500 weekly accounts).
**Falsifier:** B1 — partly fired: practitioner talk found was mostly wary, but it is a weak signal from one platform with Reddit unreachable · B2 — did not fire: three vendors report usage.
**Contradicting evidence:** 2.4 Amplitude, the closest peer, gives no usage figure · 3.5 "works just enough to be dangerous" · 3.6 the value goes to users who can't validate · 3.7 demos are trivial · 3.8 Slack, not another app (vendor) · 3.9 data quality and trust are the top concern · 4.1 self-serve BI stalled at ~26% active (secondary) · 4.2 business users don't trust the output · 5.1 JTBD puts the user as the stakeholder, not the data team · 5.5 adoption figures are vendor claims only · 6.1 Tableau retired Ask Data · 6.2 Microsoft retires Power BI Q&A.
**Top three, by impact on the goal:**
1. The pull comes from stakeholders, not data teams (3.1, 3.2, 3.6, 5.1). The metric this can plausibly move is reach beyond the data team (viewers or seats per account), and the data team will judge it on wrong answers.
2. Accuracy is the unretired risk (7.1, 7.2, 6.1, 6.2, 6.3). The previous natural-language generation was retired at both Tableau and Microsoft; builders say context and the semantic layer are the product.
3. Competitors report adoption, so this is likely becoming table stakes (2.1–2.3). The only pricing seen is at cost (4.3, 4.4, weak signal), which points at retention and defence rather than a new revenue line.
**Dropped:** none.
**Next step:** one named gap — the goal number from the CEO decision (S1): which metric this must move and by how much, because whether the assistant is spec'd for data teams or for their stakeholders turns on it.
**Other gaps — not needed for this decision:** Reddit and G2 user voice (S10) · a Kano read from your own customers (5.3) · accuracy on your customers' real questions (5.6) · independent (non-vendor) adoption data for competitor assistants · the "counter-arguments already covered" with the CEO, which were not shared with this run.

## 4 · Self-check (not a scoreboard)
| Check | Actual value |
|---|---|
| 1 Ground truth before search | Section 0 written 2026-10-09 19:35 IST; first search after it |
| 2 Every claim sourced and marked | 34 section-2 rows, each citing an S# with HIGH / MEDIUM / ZERO / NONE / ASK |
| 3 No snippet-sourced HIGH | 22 HIGH rows in SOURCES, all with URL + date; verify_quotes.py: 0 HIGH rows need fixing; S14 UNREACHABLE → MEDIUM; S21 MEDIUM (secondary figure) |
| 4 Patterns need three | "Competitors report adoption" = 3 vendors (S12–S14); "practitioners wary" labelled weak signal (one platform); "AI priced at cost" labelled weak signal (2 sources) |
| 5 Empty angles reported | All 8 angles present; Reddit ZERO (S10), complaint search NONE (S11), distribution NONE (S28) |
| 6 Every insight states its impact | Each angle insight carries Belief + Also changes |
| 7 Verdict honest | 12 contradicts rows listed; all 12 cited; Dropped: none |
| 8 Ends in a step | one named gap (the goal number) |
| 9 Grounded in the PM canon | Angle 5: JTBD, Cagan four risks, Kano (misuse flagged), OST/Build Trap, Crossing the Chasm, Lean, each with prediction + agrees/disagrees |
