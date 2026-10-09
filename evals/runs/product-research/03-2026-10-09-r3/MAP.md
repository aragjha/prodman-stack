# Research map — Should a B2B analytics product (~2,000 accounts, data teams at mid-size companies) ship an in-app AI assistant? — 2026-10-09

> **Read this first.** You asked for supporting evidence only. This map holds what contradicts the
> belief too, in its own rows and in section 3, so you choose what goes on a slide. The map is
> complete; the deck is yours.

## 0 · Ground truth (written 2026-10-09 16:05 IST, before the first search)
**Decision:** Already made: build an in-app AI assistant. What this map feeds is the leadership review on Thursday: confirm the build as scoped, or change its scope/positioning/sequencing before money is committed. · **Goal it serves:** *unconfirmed, not given.* Drafted: account retention/expansion across ~2,000 accounts (net revenue retention, weekly active users per account). The actual number and the movement that would matter are ASK (S1). · **Belief (drafted, unconfirmed):** B1 — There is real market pull: data teams at mid-size companies want an AI assistant inside their analytics tool and competitors are shipping one. B2 — Shipping it will measurably move usage or revenue for us (not just parity). · **Falsifier (drafted, unconfirmed):** B1 is dropped if unprompted public user talk about in-product analytics assistants is mostly distrust (wrong answers, hallucinated SQL, "we turned it off") and competitor assistants show no evidence of use (no paid tier, adoption numbers or case studies). B2 is dropped if competitors that shipped one report no usage/revenue lift, or charge separately and see low take-up. · **Already known:** The user says counter-arguments were discussed with the CEO last week; their content was not shared. No internal usage data, customer interviews or win/loss data given.

**Angle map and search keys (written 16:06 IST, before searching).** No angle cut by the user; none cut by me, because a leadership review asks about all eight. Keys = problem phrase + platform + company + angle word:
1 Goal — ASK only · 2 Land — "AI assistant" + Tableau Pulse / Power BI Copilot / ThoughtSpot Spotter / Looker Gemini + pricing/launch · 3 Users' words — "copilot" OR "AI assistant" + BI/analytics + HN Algolia / Reddit archive + "accurate"/"trust"/"turned off" · 4 Use — Copilot/Spotter pricing tier, Vanna/WrenAI GitHub stars + last commit · 5 Canon — JTBD, Kano, Obviously Awesome, Mom Test, Build Trap applied · 6 Cases — "text-to-SQL accuracy" benchmark, "AI assistant adoption" analytics case study, "shut down" · 7 Constraints — EU AI Act, data residency, LLM cost per query · 8 Distribution — in-app (own 2,000 accounts), dbt/Locally Optimistic communities

> **Note on "prove it":** the decision stands, and this map does not reopen it. What it can change is how the build is *scoped and positioned* before Thursday. The contradicting rows are labelled so you can leave them off the slides. You should still read them first, because leadership may raise them.

## 1 · The map
| Segment | Their words (verbatim, S#) | What they use today | What is missing | Where they are |
|---|---|---|---|---|
| Data-team analysts (your users) | "It makes you look like a god to stakeholders" (S6) · "more of a fun toy than anything close to the main way I would interact with my data" (S8) | ChatGPT for SQL, outside the BI tool (S5, S6); semantic layers (S8) | Answers they can vouch for: "You wouldn't be able to trust the results" (S12) | HN data threads (S44), dbt community of 100k+ (S43) |
| Their stakeholders (business viewers of your dashboards) | Said for them by analysts: "the role of the analyst is not to be a SQL whisperer for PMs and Executives" (S9) | The data-team ticket queue; Copilot pane in Power BI (S18) | Self-serve answers without waiting. This is where Dataherald found the business (S10) | Inside the product: your ~2,000 accounts (S2 ASK) |
| Buyers / admins | "everybody just plugs everything into ChatGPT and everybody pretends it isn't happening" (S5) | Shadow ChatGPT while legal reviews Copilot (S5) | Governance: "data governance can make this whole thing a non starter" (S11) | Procurement and security review |

**Category shape:** every major BI vendor now ships one, and it ships as a tier or as metered usage, not as a separate product. Power BI only on F2+/P1 capacity (S18). ThoughtSpot from the $50 Pro tier, capped at 25 queries per user per month (S16). Metabase in every plan including free OSS, mostly bring-your-own-key (S21). Mixpanel and Amplitude have rebranded from "assistant" to "agent" (S22, S23).

**Cases to follow:**
| Case | What they did | Good | Bad | Ugly | Source |
|---|---|---|---|---|---|
| ThoughtSpot Spotter | Put the AI in a paid tier, metered on queries | 52% of customers active on it; usage up 133% YoY (vendor-reported) | Pro tier caps it at 25 queries per user per month, so cost is being rationed | — | S16, S17 |
| Amplitude agents + MCP | Bundled agents and did not price them; also ships answers into Claude, Cursor and Slack | About 25% of queries came from agents (MEDIUM) | "drive adoption as the priority" means near-term margin pressure | — | S23, S24, S25 |
| Dataherald / Vanna (standalone text-to-SQL) | Sold NL-to-SQL to analysts | Found demand in the *embedded* use case | Pivoted away from the "data analyst" persona | Dataherald: no commit since 2024-07. Vanna: archived 2026-02 with 23.8k stars | S10, S31, S33 |

## 2 · Angles
B1 = market pull (data teams want an AI assistant inside their analytics tool, and competitors ship one). B2 = it will measurably move our usage or revenue, beyond parity.

### 1 · Goal — ASK only; the web cannot supply this number
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 1.1 | No goal metric, baseline or target given | S1 | ASK | unknown | B2 cannot be judged without it. This is the named gap in section 3 |
| 1.2 | No internal demand evidence given (requests, interviews, who asked) | S2 | ASK | unknown | Decides the persona (analyst vs stakeholder), see 4.3 |
**Insight:** Through *Escaping the Build Trap* (Perri), an output with no outcome metric predicts a launch that cannot be called a success or a failure, so B2 stays unjudgeable until S1 exists. · **Belief:** unknown · **Also changes:** set the metric before the review.

### 2 · Lay of the land — vendor pricing and docs pages, opened
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 2.1 | Power BI Copilot report pane is GA, but only on paid F2+/P1 capacity; billed by tokens | S18, S19 | HIGH | confirms (B1) | Shows the leader treats it as a premium-capacity feature |
| 2.2 | ThoughtSpot puts Spotter in the $50 Pro tier (not the $25 tier), capped at 25 queries/user/month | S16 | HIGH | confirms (B1) | A paid tier exists for it, so the cap is a cost signal, see 7.3 |
| 2.3 | Metabase, the closest mid-market comparable, includes "Ask questions with AI" in every plan, including free OSS | S21 | HIGH | confirms (B1) | Kano: a basic. Hard to charge for it at mid-market (see 5.2) |
| 2.4 | Mixpanel renamed Spark to "Mixpanel Agent" (June 2026); Amplitude calls itself "an AI Analytics company" | S22, S23 | HIGH | confirms (B1) | Positioning: "assistant" is already last year's word |
| 2.5 | Gartner (403 leaders, late 2024): over 50% of orgs use AI for natural-language queries | S27 | MEDIUM | confirms (B1) | Secondary report; enterprise-skewed sample |
| 2.6 | Tableau Agent packaging could not be verified (403) | S20 | ZERO | unknown | Don't put Tableau on a slide as fact |
**Insight:** Through *Crossing the Chasm*, all four leaders shipping it predicts the market has moved past early adopters for this feature. The evidence agrees (2.1–2.5). · **Belief:** confirms B1 · **Also changes:** frame the build as "matching the category". Do not frame it as a bet ahead of the market.

### 3 · The users' words — HN Algolia API (opened); Reddit, Quora and the Fabric forum were blocked or returned nothing
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 3.1 | Analysts say LLM-written SQL is the most valuable thing ChatGPT does for them | S6 | HIGH | confirms (B1) | The demand is real but is being met *outside* the BI tool |
| 3.2 | Admins: analytics teams wait for legal sign-off on Copilot while "everybody just plugs everything into ChatGPT" | S5 | HIGH | confirms (B1) | The substitute is general-purpose ChatGPT, not a rival BI tool |
| 3.3 | Distrust of NL-to-SQL from three independent commenters: precision, "fun toy", "wouldn't be able to trust the results" | S7, S8, S12 | HIGH | contradicts (B1) | Pattern (3 sources), but among HN devs in 2024. Trust is the build requirement, see 6.1 |
| 3.4 | Copilot demos are "smoke and mirrors" (that commenter tried Power Automate Copilot), and Power BI Copilot reads metadata, not the data itself | S3, S4 | HIGH | contradicts (B1) | Weak signal, 2023, and S3 is *adjacent* (Power Automate, not BI). Demo-vs-reality gap is a launch risk |
| 3.5 | The analyst's job is to be "an expert in the model and the data", not a "SQL whisperer" | S9 | HIGH | contradicts (B1) | Weak signal (1 source). Suggests the user who gains is the stakeholder, not the data team |
| 3.6 | No first-hand "we turned it off" post found; Reddit, Quora and Fabric forum not reachable | S35, S36, S37, S38 | ZERO / NONE | unknown | The falsifier's "turned it off" case was not found, but the biggest forum was not searchable |
**Insight:** Through *The Mom Test*, what people say unprompted counts more than what they say when asked. The unprompted talk here is about *trust*, not "we want an assistant", while behaviour (S5, S6) shows they already use LLMs on their data. · **Belief:** confirms B1 on demand; contradicts B1 on trust · **Also changes:** the requirement is "answers you can trust", not "chat".

### 4 · Offerings, and evidence of use — usage claims, GitHub stars + last commit
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 4.1 | ThoughtSpot: 52% of customers actively use Spotter; usage up 133% YoY (FY2025) | S17 | HIGH | confirms (B2) | Vendor self-report of its own press release, so not independent |
| 4.2 | Amplitude: about 25% of queries came from agents | S25 | MEDIUM | confirms (B2) | Paraphrased in the transcript summary. The "40% of insights" figure is unverified (S26, ZERO) |
| 4.3 | Dataherald's founder: after "100s of user conversations" the *embedded* use case beat the "data analyst" one | S10 | HIGH | contradicts (B1) | The pull comes from end-users of embedded analytics, not data teams. Points the persona at your accounts' stakeholders |
| 4.4 | Standalone NL-to-SQL tools are dying (Vanna archived, Dataherald dormant); WrenAI and Metabase are active | S31, S32, S33, S34 | HIGH | confirms (B1) | The capability is being absorbed into platforms, which favours building it in-app |
| 4.5 | Amplitude does not price AI separately ("drive adoption as the priority") | S24 | HIGH | unknown | B2-revenue is not shown anywhere: no vendor reports AI revenue as its own line. Bundle and accept the COGS |
**Insight:** Through *North Star* thinking, competitors report *usage* (4.1, 4.2), not revenue. The evidence supports "it gets used" and is silent on "it pays". · **Belief:** confirms B2-usage; B2-revenue unknown · **Also changes:** promise usage at the review, not revenue.

### 5 · Method — the PM canon (never cut)
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 5.1 | **JTBD** (*Competing Against Luck*) predicts two jobs. The stakeholder hires the feature to "get a number I trust without waiting". The data team hires it to "stop being a ticket queue". The evidence agrees: S9 and S10 point at the stakeholder | S10, S9, S42 | HIGH | contradicts (B1) | B1 names the wrong hirer. Data teams are the gatekeepers who configure it, not the main users |
| 5.2 | **Kano** predicts a basic (must-be) feature: absence costs, presence earns little. Evidence agrees: free in Metabase (S21), bundled at Amplitude (S24) | S21, S24 | HIGH | contradicts (B2) | Expect retention defence, not expansion revenue. ThoughtSpot's tier gating (S16) is the one exception |
| 5.3 | **Obviously Awesome** (Dunford) predicts that when everyone claims the category, you win on one differentiated attribute. The evidence names it: trustworthy answers (6.1) | S29 | HIGH | unknown | Position as "answers grounded in your metric definitions". Do not position as "an AI assistant" |
| 5.4 | **Continuous Discovery Habits / OST** (Torres): an opportunity tree without interview inputs is "nearly impossible". The decision was made solution-first | S41 | HIGH | unknown | Run 3–4 story interviews with stakeholders in the first sprint to scope v1 |
**Insight:** Read through the canon, the evidence backs *building* it, and backs it as a Kano basic used by stakeholders and configured by data teams. That is a different pitch from "data teams want an assistant". · **Belief:** contradicts B1's persona; contradicts B2's revenue upside · **Also changes:** persona and pitch for Thursday.

### 6 · Cases — benchmarks and vendor docs, opened
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 6.1 | dbt Labs: raw text-to-SQL 84–90% vs 98–100% through a semantic layer. Text-to-SQL failures are "a plausible but incorrect answer", semantic-layer failures are an error message | S29 | HIGH | unknown | Build: ground the assistant on metric definitions. Vendor benchmark, only 11 questions |
| 6.2 | Independent paper: a 4 KB business-semantics doc adds 17–23 points of accuracy across three frontier models | S30 | HIGH | unknown | Build: per-account context doc / metrics layer is the cheapest accuracy lever |
| 6.3 | Real-world benchmark SOTA moved from 64% (Oct 2025) to 96.7 (Snow) and 76.2 (Lite) by Oct 2026 | S14, S15 | HIGH | confirms (B1) | It is feasible now, but about 1 in 4 answers is still wrong on the harder Lite set |
| 6.4 | Microsoft itself warns: "Without preparation, Copilot can misinterpret the data and return generic or inaccurate results." | S19 | HIGH | unknown | Onboarding cost per account: someone must prepare the model. Budget for it |
**Insight:** Across 6.1, 6.2 and 6.4 (3 independent sources, a pattern), accuracy depends on how well the data is modelled, more than on which LLM you pick. · **Belief:** unknown (bears on how, not whether) · **Also changes:** the v1 scope is mostly semantic grounding, not chat UI.

### 7 · Constraints — regulation, governance, cost
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 7.1 | EU AI Act Art. 50: users must be told they are talking to an AI; applies from 2 Aug 2026 | S40 | HIGH | unknown | A disclosure in the UI, needed if any account is in the EU |
| 7.2 | Governance slows adoption: Copilot stuck in legal review (S5), governance a "non starter" (S11), even metadata counts as confidential (S13) | S5, S11, S13 | HIGH | contradicts (B2) | Pattern (3 sources). Usage will lag the launch by a security-review cycle. Ship admin controls and a DPA on day one |
| 7.3 | Inference cost is rationed or passed through: billed by tokens (S19), capped at 25 queries (S16), $3.75/1M tokens or BYO key (S21), margin pressure (S24) | S16, S19, S21, S24 | HIGH | unknown | Pricing decision: bundle with a cap, or BYO key. Model COGS for 2,000 accounts |
**Insight:** Through RICE, the *Effort* term is bigger than a chat UI suggests: governance review, AI disclosure and metered inference all land on v1. · **Belief:** contradicts B2 (adoption lag, via 7.2) · **Also changes:** the launch plan needs admin controls and a COGS cap.

### 8 · Distribution — your own accounts first
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 8.1 | Primary channel is in-app to ~2,000 existing accounts; active-viewer counts not given | S2 | ASK | unknown | Launch metric = stakeholder activation inside existing accounts |
| 8.2 | Data teams gather in the dbt community (100k+) and on HN data threads (547-pt Vanna story) | S43, S44 | HIGH | unknown | Channel for the "grounded in your metrics" story, aimed at the gatekeepers |
| 8.3 | Answers are leaving the app: Amplitude ships insights into Claude, Cursor and Slack via MCP (S23), and users already "plug everything into ChatGPT" (S5) | S5, S23 | HIGH | contradicts (B1) | Weak signal (2 sources). The *in-app* part of B1 may be the wrong surface. Consider an MCP endpoint alongside the panel |
**Insight:** Through *Crossing the Chasm*'s beachhead logic, the 2,000 installed accounts are the beachhead, so reach is solved. The open question is the surface (panel vs MCP), not the audience. · **Belief:** unknown · **Also changes:** scope an MCP endpoint as v1.1.

## 3 · Verdict
**Rows labelled *contradicts* in section 2 (listed first):** 3.3 · 3.4 · 3.5 · 4.3 · 5.1 · 5.2 · 7.2 · 8.3, eight in total.

**Belief:** B1 **confirmed on market pull, contradicted on persona**. B2 **still unknown**. Three findings decided it:
1. Every major vendor ships it, with a paid tier or metered usage, and reports usage (2.1, 2.2, 4.1).
2. The pull comes from stakeholders and embedded end-users, while data teams voice distrust (4.3, 5.1, 3.3).
3. No source shows revenue from the feature, it is a Kano basic, and your own goal number is missing (4.5, 5.2, 1.1).

**Falsifier:** B1's falsifier did **not fire**. Distrust is present (3.3) but is not "mostly distrust", and competitor offerings show use (4.1). B2's falsifier did **not fire** either: no vendor reported zero lift. But nothing showed a revenue lift.

**Contradicting evidence:**
- 3.3: trust pattern among HN commenters.
- 3.4: demo-vs-reality gap (weak, partly adjacent).
- 3.5: analysts are not "SQL whisperers" (weak).
- 4.3: Dataherald found the demand in embedded use, not with analysts.
- 5.1: JTBD says the hirer is the stakeholder.
- 5.2: Kano says it is a basic, so expect retention defence, not revenue.
- 7.2: governance delays adoption (3-source pattern).
- 8.3: answers are moving to ChatGPT, Claude and Slack via MCP (weak).

None of these say "don't build". They say build it for a different user, judge it on a different metric, and treat trust as the core of the build.

**Top three, by impact on the goal:**
1. Pitch it as a Kano basic that defends retention across 2,000 accounts. Do not pitch it as new revenue (5.2, 4.5).
2. Accuracy comes from grounding answers in metric definitions: 84–90% → 98–100% (6.1), +17–23 points (6.2). That is the v1 scope and the positioning (5.3).
3. The main user is the stakeholder and the data team is the gatekeeper (4.3, 5.1). Measure stakeholder activation.

**Next step:** one named gap: **the number S1**. Which metric this must move (retention/NRR or weekly active viewers per account), its current baseline, and the target, from your own product analytics. B2 and the Thursday success criterion would reverse on it, and the map does not have it.

## 4 · Self-check (not a scoreboard)
| Check | Actual value |
|---|---|
| 1 Ground truth before search | Section 0 written 16:05 IST and angle keys 16:06; first search after that; SOURCES.md written 16:11 |
| 2 Every claim sourced and marked | 33 finding rows, each cites S# with a mark |
| 3 No snippet-sourced HIGH | 31 HIGH sources, all with URL + date read; snippets (S20, S26, S28) marked ZERO |
| 4 Patterns need three | Patterns claimed: 3.3 (S7, S8, S12), 6 insight (S29, S30, S19), 7.2 (S5, S11, S13), 7.3 (4 sources); fewer-than-three rows labelled weak signal (3.4, 3.5, 8.3) |
| 5 Empty angles reported | All 8 present; Reddit/Quora/Fabric blocked or empty shown as S35–S38; Tableau ZERO (S20) |
| 6 Every insight states its impact | Every row has a one-word Belief + Also changes |
| 7 Verdict honest | 8 contradicts rows in section 2, 8 cited in section 3 |
| 8 Ends in a step | one named gap (S1) |
| 9 PM canon | Angle 5 present; 4 frameworks with predictions (JTBD, Kano, Obviously Awesome, OST) + Build Trap, Chasm, Mom Test, North Star in other insights |
