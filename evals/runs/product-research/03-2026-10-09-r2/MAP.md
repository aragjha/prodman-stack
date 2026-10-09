# Research map — should we build an in-app AI assistant into our B2B analytics product — 2026-10-09

## 0 · Ground truth (written 2026-10-09T07:10:13Z, before the first search)

**Decision:** Build an in-app AI assistant for the analytics product (B2B, ~2,000 accounts, data teams at mid-size companies). Stated by the user as already made with the CEO last week. What the leadership review on Thursday can still choose differently: approve the build as decided · approve a narrower first slice · hold. The alternative the build displaces was not stated — *unconfirmed*.

**Goal it serves:** Not given. Drafted: a retention or expansion number on the existing ~2,000 accounts (weekly-active analyst seats, or net revenue retention). *Unconfirmed — ASK row S1; the map never substitutes the web's number for yours.*

**Belief:** Data teams at mid-size companies want an AI assistant inside their analytics product, and the competitors who shipped one gained measurable usage or revenue from it. *Drafted by the skill from the request ("the market pull, the competitors who've done it, the user demand") — unconfirmed.*

**Falsifier:** No unprompted public demand from data teams for an AI assistant inside their analytics tool, OR the competitors who shipped one report low adoption, accuracy failures, or quietly retired it. *Drafted — unconfirmed.*

**Already known:** The user says the counter-arguments have been "been through" but did not list them, so the run cannot avoid re-finding them. They go in section 3 under *Contradicting evidence*, in their own place, so the deck can leave them out and the map cannot. *Unconfirmed.*

**On the "prove it" request:** this map is built to be complete, not persuasive. Supporting evidence is in sections 1–2. What contradicts the belief is listed in section 3, in its own lines, never mixed into the findings. What goes on a slide is the user's choice; what goes in the map is not.

### Angle map and search keys (written before searching)

| # | Angle | Runs? | Search keys |
|---:|---|---|---|
| 1 | Goal | ASK only | asked for: the number the assistant must move, and by how much |
| 2 | Lay of the land | yes | "AI assistant" + analytics/BI + Amplitude · Mixpanel · PostHog · ThoughtSpot · Tableau · Power BI · Looker · Metabase · Hex · Sigma + launch/pricing |
| 3 | Users' words | yes | "AI" "copilot" "text to SQL" + Hacker News (Algolia) · Reddit (archive API: r/dataengineering, r/BusinessIntelligence, r/analytics, r/PowerBI) · Quora (site:) |
| 4 | Offerings, evidence of use | yes | GitHub: vanna-ai/vanna · Canner/WrenAI · eosphoros-ai/DB-GPT · Dataherald — stars + last commit; vendor pricing tiers that gate the AI feature |
| 5 | Method, canon | light | *The Mom Test* · *Continuous Discovery Habits* · *Inspired* — on researching a decision already made |
| 6 | Cases | yes | Power BI Copilot · Tableau Pulse · Amplitude Ask/AI Agents · PostHog Max · ThoughtSpot Spotter — adoption numbers, teardowns, retirements |
| 7 | Constraints | yes | text-to-SQL accuracy on enterprise schemas (Spider 2.0 / BIRD) · LLM data-handling terms · cost per query |
| 8 | Distribution | light | where mid-size data teams gather: subreddit sizes, dbt community, newsletters — existing 2,000 accounts make this the least decision-bearing angle |

*The user may cut angles; none were cut by the skill. Angles 5 and 8 are run light because they bear least on a decision already made.*

---

## 1 · The map

Every direct competitor opened has shipped the feature; two of five have already renamed or re-architected it. The loudest user voices are not asking for an assistant — they are describing what happened after one shipped.

| Segment | Their words (verbatim, S#) | What they use today | What is missing | Where they are |
|---|---|---|---|---|
| Non-technical execs and business users at mid-size companies | "the non technical CEO got tired of waiting 3 days for numbers that werent on existing dashboards" (S11) · "especially for people with lesser experience in technical data analytics skills" (S14) | Metabase question builder, CSV-upload chat tools, Copilot panes (S11, S9) | "natural language queries work for simple stuff and fall apart on anything with joins" (S11); live-database access | r/analytics; customer advisory boards (S4) |
| Data teams — the stated users of this build | "users loved it honestly and adoption was better than anything they'd ever rolled out before. all was good untill the data team actually checked the numbers." (S12) · "The projects that work all have one thing in common - a team that curated the data, defined the metrics, and built evaluation frameworks before touching the agent layer." (S13) | Internal "AI analyst" deployments, vendor copilots (S12, S9) | Trust: wrong-but-plausible answers; metrics definitions; eval frameworks (S12, S13, S32) | r/analytics (30 and 26 pts threads), dbt community (S36) |
| BI developers on vendor copilots | "My manager started pushing Copilot for Power BI last month and now every report request comes with 'can you just have AI build the first draft.'" (S10) · "it pulled the entire…" (S34) | Power BI Copilot, gated to F2+/P1+ capacity (S32) | Permission-respecting data access (S34); role clarity (S10) | r/PowerBI (75 and 85 pts threads) |
| Engineers building text-to-SQL | "closer to 20-30% rates pre-context engineering" (S16) · "Is text-to-sql a deadend? (I personally think it is, having worked on a project at $work.)" (S17) | Agentic loops over a semantic layer; WrenAI, DB-GPT (S22, S23) | Schema context; a semantic layer "can bring back up" accuracy (S16) | Hacker News; GitHub |

**Cases to follow:**
- **ThoughtSpot Spotter** — what they did: an AI agent across the whole BI product · good: "more than 52% of ThoughtSpot customers were actively leveraging the product" within its first fiscal year (S26) · bad: the only numbers are the vendor's own, and 52% is a stock of customers touched, not a usage rate · ugly: none public · source S26, S27.
- **PostHog Max → PostHog AI** — what they did: shipped a named assistant, then killed the assistant framing and folded AI into "the underlying architecture" (S28) · good: the stated user value survived — "analysts can spend less time as human middleware" (S29) · bad: "The broader vision (AI woven through every product) wasn't landing." (S28) · ugly: the decision was to double down on technical users, not on the self-serve business user most pitches target (S29) · source S28, S29.
- **Mixpanel Spark → Mixpanel Agent** — what they did: natural-language querying in July 2023, still live three years later under a new name (S6) · good: longevity · bad: no public usage number was found for it · ugly: none found · source S6.

---

## 2 · Angles

### 1 · Goal — ASK only · the number is yours, not the web's · nothing searched
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 1.1 | The number the assistant must move, and by how much, was not given and cannot be found on the web | S1 | ASK | unknown | the next step: without it, section 3 cannot end in *decide* |

**Insight:** Every usage number in this map is a vendor's stock; only your own baseline turns it into a rate worth comparing against. · **Belief:** unknown · **Also changes:** the goal metric should be prompts per account per week, not "accounts that have tried it" (see 6.3).

### 2 · Lay of the land — opened the vendors' own pages (blog, pricing, docs) · to see who has shipped it and how it is packaged · searched Amplitude, Mixpanel, PostHog, Metabase, Power BI; Tableau Pulse, Looker, Hex and Sigma were not opened in the budget
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 2.1 | Amplitude reports 219,578 AI prompts in 2025 across Ask Amplitude, AI Agents and MCP, and 122,587 charts built by prompt | S2, S3 | HIGH | confirms — weak confirm: against "over 4,500 customers" (S3) that is ≈49 prompts per customer per year, my arithmetic, not Amplitude's | the slide: cite the per-customer rate next to the headline |
| 2.2 | Amplitude's CEO: "AI Agents were our most-wanted new product at multiple customer advisory boards this year" | S4 | MEDIUM | confirms — trust: vendor CEO, trade-press relay | nothing |
| 2.3 | Amplitude's Feb 2026 agentic-analytics release could not be opened | S5 | ZERO | unknown | nothing — not used |
| 2.4 | Mixpanel shipped Spark in July 2023 and still runs it as "Mixpanel Agent" | S6 | HIGH | confirms (longevity, not usage) | positioning: three years in market means "AI assistant" is table stakes, not differentiation |
| 2.5 | PostHog meters AI by credits: $5 free per month, then "100 AI credits = $1" | S7 | HIGH | unknown | the build: cost per query is a pricing surface, not just a COGS line |
| 2.6 | Metabase puts "Ask questions with AI" in the free open-source tier; Pro ($517.50/month) adds "AI usage auditing and controls" | S8 | HIGH | contradicts — the assistant itself is free at the low end; what is paid is governance | positioning: the paid thing is control and audit, not the chat box |
| 2.7 | Power BI runs three chat surfaces and lets app authors ship "verified answers" | S9 | HIGH | confirms (shipped) · counter-signal: Microsoft is routing answers through human-verified responses | the build: a verified-answers layer belongs in the first slice |

**Insight:** Everyone opened has shipped it, and the pattern in packaging (S6, S8, S9 — three sources) is that the chat box is free or bundled while governance, audit and verified answers are what gets sold. · **Belief:** confirms the "competitors did it" half; contradicts the implied "and it is the thing customers pay for" · **Also changes:** positioning and the first slice.

### 3 · The users' words — Reddit via archive API, HN opened directly · to hear the pain unprompted · searched r/PowerBI "copilot", r/analytics "natural language", HN "text to SQL" comments; r/BusinessIntelligence and r/dataengineering returned 422 (S20); HN stories and Quora returned nothing (S18, S19)
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 3.1 | Unprompted demand exists, from a non-technical CEO: "can we just ask our data questions in english" — and the answer "falls apart on anything with joins" | S11 | HIGH | confirms (demand) · contradicts (reliability) — weak confirm | the build: joins are where it breaks; the eval set must be join-heavy |
| 3.2 | The most-upvoted thread found (30 pts) is a failure story: adoption "better than anything they'd ever rolled out before", then six weeks of wrong numbers from a deprecated table | S12 | HIGH | contradicts | the build: a semantic layer and metric definitions before the chat box |
| 3.3 | A "Global Data Director" (26 pts): projects that work "curated the data, defined the metrics, and built evaluation frameworks before touching the agent layer"; the 40% stall figure inside is unsourced | S13 | HIGH (words) · ZERO (the 40%) | contradicts the sequencing, not the demand | the build order |
| 3.4 | A business-user voice: LLM querying "has become much more convenient, especially for people with lesser experience" | S14 | HIGH | confirms | nothing |
| 3.5 | Two thread titles ask whether conversational analytics is solved or a demo; both at 0 pts | S15 | HIGH | unknown — weak signal, low engagement | nothing |
| 3.6 | An engineer: high-9s accuracy on a clean DB, "closer to 20-30% rates" on the messy schema companies actually have, recoverable by "a clean semantic/presentation layer" | S16 | HIGH | contradicts (as-is) · confirms (with a semantic layer) | the build: semantic layer first |
| 3.7 | An engineer who shipped one: "Is text-to-sql a deadend? (I personally think it is, having worked on a project at $work.)" | S17 | HIGH | contradicts | nothing new beyond 3.6 |
| 3.8 | BI developers' thread (75 pts) is about being replaced by Copilot, not about wanting it | S10 | HIGH | adjacent — contradicts: the data team is the stated user, and the loudest data-team voice is anxiety | positioning to the buyer's own data team |
| 3.9 | Nothing found: HN stories for "AI analyst" / "ask your data" / "chat with your data" (0 hits); no Quora pages for the natural-language-BI query | S18, S19 | NONE | unknown | nothing |

**Insight:** Demand is unprompted and real, but it comes from non-technical users (S11, S14, S4 — three sources, one of them a vendor CEO), while the data teams named as this build's users talk about trust failures (S12, S13, S16 — three independent sources: a pattern). · **Belief:** contradicts as written — "data teams want it" is the half with the weakest support · **Also changes:** who the assistant is for, and the build order.

### 4 · Offerings and evidence of use — GitHub API for stars and last push · to separate live projects from museums · searched vanna, WrenAI, DB-GPT, Dataherald; vendor tiers from angle 2
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 4.1 | Vanna, the best-known open text-to-SQL repo (23,822 stars), is archived; last push 2026-02-02 | S21 | HIGH | counter-signal — the most-starred standalone "chat with your SQL" project stopped | build-vs-buy: the standalone chat approach is being abandoned upstream |
| 4.2 | WrenAI (17,827 stars, pushed 2026-10-08) describes itself as "governed text-to-SQL through an open context layer" | S22 | HIGH | confirms (active) · also changes: the live project sells the context layer, not the chat | the build: context layer is the product |
| 4.3 | DB-GPT (20,097 stars, pushed 2026-10-04) — active, 450 open issues | S23 | HIGH | confirms (active demand among builders) | build-vs-buy candidate |
| 4.4 | Dataherald: 3,650 stars, last push 2024-07-24 — dormant | S24 | HIGH | counter-signal | nothing |
| 4.5 | Paid tiers exist because someone pays: PostHog credits (S7), Metabase Pro governance (S8) | S7, S8 | HIGH | confirms (a paying tier exists) · contradicts (what is paid is governance, not chat) | pricing |

**Insight:** Two of four repos opened are dead or archived and the two alive sell the governed context layer; a weak signal (two dead, two alive — not three) that standalone "chat with your database" is consolidating into semantic-layer products. · **Belief:** unknown — evidence of builder activity, not of end-user usage · **Also changes:** build-vs-buy — WrenAI and DB-GPT are live candidates to compose rather than rebuild.

### 5 · Method — *The Mom Test* via Goodreads reproduction · because the request is for supporting evidence only · *Continuous Discovery Habits* and *Inspired* were not opened in the budget
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 5.1 | "People stop lying when you ask them for money." and "We go through the futile process of asking for opinions and fish for compliments because we crave approval…" | S25 | MEDIUM | unknown — a method, not a market fact | the method: advisory-board "most-wanted" (S4) is an opinion; a pre-sold paid tier is the evidence this map lacks |

**Insight:** The canon says the strongest evidence in this map would be a commitment, and none was found — no competitor's revenue from the feature, no pre-sale. · **Belief:** unknown · **Also changes:** the next step — the named gap is a commitment number, not more opinion.

### 6 · Cases — vendor post-mortems and press releases, opened · to see what happened after shipping · searched ThoughtSpot, PostHog, Amplitude, Mixpanel; Tableau Pulse not opened
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 6.1 | ThoughtSpot: "more than 52% of ThoughtSpot customers were actively leveraging the product" by fiscal year end | S26 | HIGH | confirms — trust: self-reported, and a customer stock, not a usage rate | the slide: label it as vendor-reported |
| 6.2 | ThoughtSpot: "133% year-over-year increase in usage" attributed to agentic demand | S27 | HIGH | confirms — trust: self-reported, base undisclosed | nothing |
| 6.3 | Amplitude's 219,578 prompts across "over 4,500 customers" ≈ 49 prompts per customer per year (own arithmetic from S2 + S3) | S2, S3 | HIGH | weak confirm — usage exists; at roughly one prompt per customer per week it is not evidence of a habit | the goal metric |
| 6.4 | PostHog killed Max: "The mascot was a limiting factor." · "The broader vision (AI woven through every product) wasn't landing." — and re-architected as PostHog AI | S28 | HIGH | contradicts the "assistant" form; confirms AI-in-product | the build: not a chat character in a corner; capabilities inside existing surfaces |
| 6.5 | PostHog's stated value and direction: AI "helps with adoption of PostHog across the org", analysts "spend less time as human middleware", and "We're doubling down on technical users." | S29 | HIGH | confirms (value exists) · counter-signal (the winning user was the technical one) | positioning: build for your data team's throughput, not around them |
| 6.6 | The third-party claim that Max was "weren't adopting" could not be verified — PostHog's post has no usage number | S30 | ZERO | unknown — dropped from the verdict | nothing; not rounded up either way |
| 6.7 | Mixpanel Spark survived three years, renamed Mixpanel Agent | S6 | HIGH | confirms (longevity) | nothing |

**Insight:** Of three competitors with a public outcome, one reports adoption (self-reported), one re-architected away from the assistant framing, one survived quietly — no revenue number was found anywhere. · **Belief:** unknown on "measurable usage or revenue": usage is reported but only by vendors, revenue not at all · **Also changes:** the slide must not say "competitors gained revenue from it"; the map cannot support that sentence.

### 7 · Constraints — benchmark paper and official docs, opened · to find what bounds the build · searched Spider 2.0, Power BI Copilot requirements, the permission PSA
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 7.1 | Spider 2.0: a code agent on o1-preview "successfully solves only 21.3% of the tasks" on real enterprise databases "often containing over 1,000 columns", versus 91.2% on Spider 1.0 | S31 | HIGH | contradicts — on realistic schemas the technology is not yet reliable unaided | the build: an eval on your customers' real schemas before scoping |
| 7.2 | Microsoft gates Copilot to paid F2+/P1+ capacity, says Pro/PPU "alone isn't sufficient", and warns "Without preparation, Copilot can misinterpret the data and return generic or inaccurate results." | S32 | HIGH | contradicts (accuracy warning from the largest vendor) · confirms (they charge capacity for it) | pricing: an upper tier; the build: data-prep tooling is part of the feature |
| 7.3 | Copilot is disabled by default outside the US/EU data boundary until an admin allows data to leave the region | S33 | HIGH | unknown | constraint: a region/residency switch for your accounts |
| 7.4 | Copilot "can pull raw data without BUILD permission" — on by default (85 pts) | S34 | HIGH | counter-signal — the first thing users publicised about a vendor's assistant was a permission leak | the build: the assistant inherits row- and object-level permissions from day one |

**Insight:** Three independent sources (S12, S16, S31) put real-schema accuracy far below demo accuracy — a pattern — and the largest vendor's own docs carry the same warning (S32). · **Belief:** contradicts the falsifier's "accuracy failures" clause is live · **Also changes:** the first slice and the eval gate.

### 8 · Distribution — light · existing accounts make this the least decision-bearing angle · searched subreddit sizes via archive API, dbt community
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 8.1 | r/dataengineering: 255,630 subscribers (archive snapshot from Feb 2025 — stale) | S35 | HIGH | unknown | nothing |
| 8.2 | dbt Community: "over 100,000 data professionals" on Slack, Discourse, meetups | S36 | HIGH | unknown | where to recruit eval participants |
| 8.3 | Sizes for r/analytics, r/BusinessIntelligence, r/PowerBI not retrieved (API 400) | S37 | ZERO | unknown | nothing |

**Insight:** The rooms where the angle-3 quotes live (r/analytics, r/PowerBI, dbt Slack) are also where five accounts for a schema eval can be found in a day. · **Belief:** unknown · **Also changes:** the next step's "where to look".

---

## 3 · Verdict

**Rows labelled contradicts, weak confirm, trust, counter-signal or adjacent in section 2, listed before judging:** S2/S3 (weak confirm, 2.1 and 6.3) · S4 (trust) · S8 (contradicts) · S9 (counter-signal) · S10 (adjacent, contradicts) · S11 (weak confirm) · S12 (contradicts) · S13 (contradicts) · S16 (contradicts) · S17 (contradicts) · S21 (counter-signal) · S24 (counter-signal) · S26 (trust) · S27 (trust) · S28 (contradicts) · S29 (counter-signal) · S31 (contradicts) · S32 (contradicts) · S34 (counter-signal). S30 is ZERO and was dropped: it could not be verified, so it neither helps nor hurts.

**Belief:** still unknown — because the two halves split. "Data teams want it" is contradicted as written: unprompted demand is real but comes from non-technical users (S11, S14, S4), while the data teams named as the users describe trust failures (S12, S13, S16). "Competitors gained measurable usage or revenue" is unproven: the only usage numbers are vendor self-reports (S26, S27, S2), Amplitude's own figure works out to ≈49 prompts per customer per year (6.3), one of three public cases retired the assistant framing (S28), and no revenue attributable to the feature was found in any opened source.

**Falsifier:** fired in part. Clause 1 (no unprompted demand) did not fire — S11, S14, S4. Clause 2 (accuracy failures or retirement) fired — accuracy failures on real schemas in S12, S16, S31, and a retirement of the assistant form, though not of AI, in S28.

**Contradicting evidence:** S8 — the chat is free at Metabase's low end; governance is what is paid. S9 — Microsoft routes to human-verified answers. S10 (adjacent) — the data-team room's top thread is about being replaced, not wanting the tool. S11 (weak confirm) — "fall apart on anything with joins". S12 — six weeks of wrong numbers after the best-adopted rollout they'd had. S13 — the projects that work build metrics and evals before the agent. S16 — 20–30% on messy schemas. S17 — "Is text-to-sql a deadend? (I personally think it is…)". S21, S24 — Vanna archived, Dataherald dormant. S26, S27 (trust) — ThoughtSpot's numbers are its own, and 52% is a stock. S2/S3 (weak confirm) — ≈49 prompts per customer per year. S28 — "The broader vision (AI woven through every product) wasn't landing." S29 (counter-signal) — the user PostHog doubled down on was the technical one. S31 — 21.3% on Spider 2.0. S32 — "Copilot can misinterpret the data and return generic or inaccurate results." S34 — raw data pulled without BUILD permission, on by default. S4 (trust) — "most-wanted" at advisory boards is an opinion, and *The Mom Test* (S25) says what that is worth.

**Top three, by impact on the goal:**
1. Accuracy on real schemas is the make-or-break, not demand (S31, S16, S12 — a pattern on three independent sources, echoed by the largest vendor's docs S32). The failure mode is wrong-but-plausible numbers reaching leadership for weeks. Changes the first slice: semantic layer, metric definitions and verified answers before the chat surface.
2. The demand is from non-technical users; the data team is the gatekeeper that must trust it (S11, S14, S12, S13, S29). PostHog's surviving value was "analysts can spend less time as human middleware". Changes positioning: build for the data team's throughput, with them as authors of verified answers, not as the audience being bypassed.
3. The usage evidence is vendor stock, not rate (S26, S27 versus 6.3). Changes the slide and the goal metric: cite ThoughtSpot's 52% with the Amplitude per-customer arithmetic beside it, and set the success metric as prompts per account per week with a correctness check, not "accounts that tried it".

**Next step:** one named gap — the accuracy your assistant would hit on your own customers' real schemas. The map has 21.3% on Spider 2.0 (S31) and "20-30%" on messy schemas (S16), and no number for yours. Where to look: a 50-question, join-heavy eval across five real accounts, built with your data team, before the build is scoped — a week's work, and it decides whether the first slice is an assistant or a semantic layer. The goal number (S1) is the second thing only you hold; Thursday's review can ask for both.

---

## 4 · Self-check (not a scoreboard)

| Check | Actual value |
|---|---|
| 1 · Ground truth before search | Section 0 written to disk at 2026-10-09T07:10:13Z in the tool turn before the first fetch; every SOURCES row dated 2026-10-09 and read after that write |
| 2 · Every claim sourced and marked | 37 findings across 8 angles; each cites an S# carrying HIGH / MEDIUM / ZERO / NONE / ASK; marks used: 28 HIGH · 2 MEDIUM · 4 ZERO · 2 NONE · 1 ASK |
| 3 · No snippet-sourced HIGH | 28 HIGH rows, each with a URL and date read; Reddit via archive API URL, HN opened on news.ycombinator.com; the Algolia-only comment fragments were not used |
| 4 · Patterns need three | "accuracy fails on real schemas": S12, S16, S31 (3, independent) · "demand from non-technical users": S11, S14, S4 (3, one vendor-sourced, labelled) · "chat free, governance paid": S6, S8, S9 (3) · "standalone text-to-SQL consolidating": S21, S24 (2 — labelled weak signal) · "vendors retreating from the assistant form": S28, S9 (2 — labelled counter-signal, not a pattern) |
| 5 · Empty angles reported | All 8 angles have rows; angle 3's empty lanes recorded as NONE (S18, S19) and ZERO (S20); angle 8's missing counts as ZERO (S37); Tableau Pulse, Looker, Hex, Sigma, *Continuous Discovery Habits* and *Inspired* named as not opened in the budget |
| 6 · Every insight states its impact | 8 angle insights, each with Belief and Also changes; no row carries a dash in the Belief column |
| 7 · The verdict is honest | 19 labelled rows listed before the verdict; all 19 cited in *Contradicting evidence*; S30 dropped and the reason given (ZERO) |
| 8 · Ends in a step a decision can take | one named gap — accuracy on the customers' own schemas, with where to look |
