# /product-research — before the first search

**Plainly, first.** I'll build the pack. It will contain what contradicts the belief, in its own section, separated from the supporting evidence — so you can choose what goes on a slide. The map is complete; the deck is yours. I won't produce a map with the contradicting section removed: a map that cannot be wrong changes nothing, and if one person in Thursday's room holds an objection the pack skipped, the pack loses the room. The counter-arguments you've already been through go in **Already known** below — then the run doesn't re-find them, and the contradicting section stays short and familiar instead of long and new.

I have not searched yet. The skill won't search until the ground truth is confirmed. Three fields are missing — one answer each.

## 0 · Ground truth — draft, written 2026-10-09, awaiting your confirmation

| Field | What I have | Status |
|---|---|---|
| **Decision** | Build an in-app AI assistant inside the analytics product (B2B, ~2,000 accounts, data teams at mid-size companies). Made last week with the CEO; Thursday is leadership review. | Given. One gap: what does it displace? "Build" is only a decision against something — name the roadmap item that loses the capacity. |
| **Goal it serves** | — | **Missing.** Which number is this supposed to move — activation, retention / NRR, expansion, seat growth, support-ticket deflection, win rate in competitive deals? And by how much would it have to move to matter? Your numbers, never the web's. |
| **Belief** | "Data teams at mid-size companies want a natural-language AI assistant inside their analytics tool enough that it moves [goal], and the competitors who shipped one are seeing real use — not just launches." | Drafted from your message. Confirm, or rewrite it as one sentence a stranger could disagree with. |
| **Falsifier** | — | **Missing**, and your message says nothing would change your mind. A belief that cannot lose is not a belief; it is a conclusion waiting for footnotes. Proposed: *"No unprompted public demand from data-team users for an in-tool AI assistant, and the competitors who shipped one show low adoption, gated it behind an add-on nobody buys, or quietly pulled it."* Confirm or replace. |
| **Already known** | — | **Missing.** The counter-arguments you've been through, and anything you've already seen — analyst reports, customer calls, competitor demos. Listed here, they don't get re-found. |

## 1 · The angle map — cut before I search

Eight angles; each gets answered or reported empty with the search shown. Cross out the ones that don't bear on Thursday's decision. My suggestion for a leadership review: keep 1–4, 6 and 7; **cut 5 (Method) and 8 (Distribution)** — you have 2,000 accounts, reach isn't the question, and the canon is a footnote unless your leadership respects it.

| # | Angle | Question it must answer | Search keys (problem phrase + platform + company + angle word) |
|---:|---|---|---|
| 1 | Goal | Which number moves, and by how much to matter? | Your numbers only. No search. |
| 2 | Lay of the land | Who has shipped an in-product AI assistant for analytics, in what shape, and where is it moving? | Company sites · pricing pages · changelogs · launch posts: ThoughtSpot Spotter · Tableau Pulse / Agent · Power BI Copilot · Looker conversational analytics · Databricks AI/BI Genie · Snowflake Cortex Analyst · Hex Magic · Sigma "Ask Sigma" · Metabase Metabot · Amplitude "Ask Amplitude" · Mixpanel Spark · Omni · Mode. Angle words: "pricing", "add-on", "GA", "preview", "changelog" |
| 3 | The users' words | How do data teams phrase the pain — and the disappointment — unprompted? | Reddit archive API: r/BusinessIntelligence · r/dataengineering · r/analytics · r/PowerBI · r/tableau · r/dataanalysis. HN Algolia. `site:quora.com`. G2 / Capterra reviews, opened. Terms: "copilot" · "ask AI" · "natural language query" · "text to SQL" · "AI analyst" + "actually use" · "useless" · "hallucinate" · "wrong number" · "turned it off" · "customers asking for". Verbatim only |
| 4 | Offerings, and evidence of use | What exists — paid, free, open source — and is it actually used? | GitHub (stars AND last commit AND open issues): vanna-ai/vanna · Canner/WrenAI · Dataherald · sqlchat · dataline · defog. Paid: Copilot capacity requirements, Tableau+ tier, ThoughtSpot pricing — a tier that exists because someone pays. Review counts and changelog cadence for each name in angle 2 |
| 5 | Method — what the canon says | What does discovery literature say about shipping a feature on executive conviction? | *Continuous Discovery Habits* (assumption testing) · *Inspired* (the four risks: value, usability, feasibility, viability) · *The Mom Test* (unprompted vs. prompted demand) · *Lean Customer Development*. The book and the chapter, cited when opened |
| 6 | Cases — good, bad, ugly | Who did this before, and what happened? | Post-mortems · teardowns · talks with numbers · "we shut it down" posts: ThoughtSpot Sage → Spotter · Tableau Pulse adoption · Power BI Copilot rollout and gating complaints · Databricks Genie usage claims · Snowflake Cortex Analyst · text-to-SQL startups that pivoted or closed. Angle words: "adoption", "post-mortem", "lessons", "sunset", "retention" |
| 7 | Constraints | What limits the options? | Official docs and regulator pages: customer data sent to LLM providers (DPA, SOC 2, data residency, zero-retention terms) · model-provider terms · EU AI Act transparency duties · cost per query at 2,000 accounts · accuracy / liability language in competitors' ToS · dependency on a semantic layer |
| 8 | Distribution | Where would we reach these people? | Same rooms as 3 · dbt Community Slack · Locally Optimistic · Data Council · newsletters (Benn Stancil, Data Engineering Weekly) · the repos they star |

## Three answers I need, once

1. **Goal:** which number, and how much must it move to matter?
2. **Falsifier:** confirm the proposed one, or write yours.
3. **Already known, and what's displaced:** the counter-arguments you've been through, what you've already seen, and the roadmap item this build replaces. Then cross out angles.

Reply with those and I run the map — ground truth timestamped before the first `SOURCES` row, supporting and contradicting evidence in separate sections, a verdict on the belief and one next step at the end. Thursday-ready; what goes on the slide is yours.
