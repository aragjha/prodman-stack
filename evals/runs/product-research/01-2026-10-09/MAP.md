# Research map — AI meeting notes in a B2B scheduling product vs calendar-sync reliability — 2026-10-09

## 0 · Ground truth (written 2026-10-09T04:18Z, before the first search)

| Field | Value |
|---|---|
| **Decision** | Next planning cycle: put two engineers on (a) AI meeting notes — auto-summary + action items pushed into the booking record — **or** (b) the calendar-sync reliability work support keeps escalating. Build-vs-defer, not build-vs-buy (buy is a sub-option under angle 4). |
| **Goal it serves** | Q1 expansion-revenue target. The feature must make an existing account **add seats**, not merely stop it leaving. (Target number, current expansion rate, seats per account, price per seat: **not supplied — see angle 1.**) |
| **Belief** | Ops leads at mid-market ops teams (our ~400 per-seat accounts) want AI meeting notes inside the scheduling product, because it came up in three QBRs this quarter. |
| **Falsifier** | Either: (F1) no ops people can be found asking for this **unprompted** anywhere public; or (F2) every tool that shipped it reports that nobody used it. |
| **Already known** | Three QBR mentions this quarter (prompted or unprompted — unknown). Support is escalating calendar-sync reliability. Product is per-seat, mid-market ops, ~400 paying accounts. |

**Search keys written before searching** (problem phrase + platform + company + angle word):
`meeting notes` · `action items` · `ops manager` / `operations lead` / `revops` · `Calendly` · `Cal.com` · `Chili Piper` · `HubSpot meetings` · `Zoom AI Companion` · `Google Meet take notes` · `Fathom` · `Otter` · `Fireflies` · `tl;dv` · `Granola` · `Recall.ai` · `notetaker ban` · `recording consent` · `seat expansion` · `nobody uses` · `adoption` · `shut down`

**Angle map shown before searching** — cut what does not bear on the decision:

| # | Angle | Bears on | Kept? |
|---:|---|---|---|
| 1 | Goal | How many seats a feature must add to matter | Kept — but it needs *your* numbers, not the web's |
| 2 | Lay of the land | Have scheduling competitors shipped notes? Is it table stakes or differentiator? | Kept |
| 3 | Users' words | Falsifier F1 directly | Kept — heaviest |
| 4 | Offerings & evidence of use | Falsifier F2; build-vs-buy sub-option | Kept — heavy |
| 5 | Method | What the canon says about "three customers asked" | Kept — light |
| 6 | Cases | Falsifier F2: who shipped it, did anyone use it, did it sell seats | Kept — heavy |
| 7 | Constraints | Consent law, platform bot rules, cost of a notetaker bot | Kept — light; sets the real cost of option (a) |
| 8 | Distribution | Where to find the ops people for a validation test | Kept — light |

*(You could not be asked to cut; all eight were run, 7 and 8 lightly. If you would have cut any, the verdict does not depend on 5, 7 or 8.)*

---

## 1 · The map

**In one screen.** Between your three QBRs and today, the category leader in your exact product shape shipped the exact feature: Calendly Notetaker, 19 Aug 2026, "100,000 meeting recordings" in beta, sold as a **higher per-seat tier** (Standard Plus / Teams Plus), English-only, 2-hour cap (S1–S4). HubSpot sells its notetaker inside Sales/Service Hub **Professional** (S6). Google folded Gemini into every Workspace tier and raised the **price per user by $2** (S7). Zoom reports AI Companion MAU "over four times year over year" and now sells per-user "ZoomMate" tiers (S9, S10). So the feature is used (F2 did not fire), and it is monetised everywhere the same way: **per-seat price, not seat count**. On the demand side, ops leads asking for it unprompted in public: **one** direct ask, in Calendly's own community, for notes *on the contact record* rather than for note-taking as such (S19); ops-specific rooms returned nothing or were rate-limited (S21). The strongest public voices are *against* notetaker bots on accuracy and privacy (S13–S15, S20), and the meeting surfaces are closing to bots: Microsoft Teams defaults to approval-gating external bots from Sept 2026 (S25), the NYC Bar wants consent (S26), an insurer banned them outright (S27), Otter is in a class action (S28).

| Segment | Their words (verbatim, S#) | What they use today | What is missing | Where they are |
|---|---|---|---|---|
| Client-facing Calendly customer (role not stated; 5–15 meetings per client) — **closest to your buyer** | "Can meeting notes be auto added to contacts ... so that we can get a better overview of the client relationship history?" · "the idea of searching 15 meetings to find notes is daunting" (S19) | Calendly Notetaker recaps, per meeting | Notes attached to the **record** (contact/booking), not to the meeting — Calendly: "we don't have the capability to surface meeting notes directly on the contact record" (S19) | Calendly community |
| People who run meetings — PMs (*adjacent*) | "I have everything in my head — who owns what, what changed, what's blocked. Then I open the notes doc ... I'm trying to remember my own meeting." (S20) | Manual minutes; transcripts into Copilot/ChatGPT | Trust: top reply (35 pts) "This is just soft marketing for an AI note taking service." (S20) | r/projectmanagement |
| Engineering managers (*adjacent*, HN) | "I block AI note takers from my meetings." (S13) · "they all fucking suck ... Wrong todos, wrong people assigned to todos." (S14) · but: "meeting notes with action items were sent afterwards, I would never want to work in a place that didn't" (S16) | Own notes; some use the action-items email with timestamps (S17) | Accuracy on decisions ("missing 0-2 critical things", S15); scoping across back-to-back meetings (S15) | HN (321 pts / 386 comments on the topic, S18) |
| IT / security / legal buyers (the people who can veto your feature) | "third-party AI note-taking assistants threaten our commitment to data security." (S27) · "obtain client consent before recording a call with an AI system" (S26) | Tenant policy: Teams "RequireApprovalWhenDetected" by default (S25) | A notetaker that passes tenant policy and consent — i.e., not a bot | Microsoft message center, bar associations, HR/IT policy pages |

**Cases to follow** (good · bad · ugly · source):
1. **Calendly** — shipped notes 14 months after your product shape became "scheduling + meeting". Good: 100k beta recordings, action items + follow-up email. Bad: monetised as a per-seat tier upgrade, English-only, 2-hour cap, no notes-on-record (S1–S4, S19). Ugly: entered "a litany of note-takers" by the CEO's own description (S2).
2. **Google Workspace** — bundled Gemini and raised every tier by ~$2/user (S7). Good: ARPU up across the base. Bad for your thesis: zero seats added by the feature; the lever was price.
3. **HubSpot** — absorbed the category its "most installed marketplace app" (Fathom, S12) created, into Professional tiers (S6). Good: platform wins the bundle. Ugly for a standalone: the independent notetakers' mid-market spend is flat (Otter) or declining (Fathom, Fireflies) while only Granola grows (S11).

---

## 2 · Angles

### 1 · Goal — your numbers, not the web's · *not searched by design*
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| 1.1 | Needed before planning: Q1 expansion target (₹/$), current quarterly expansion from the 400 accounts, median seats per account, price per seat, and **what triggered the last 20 seat-adds** (new team onboarded? new use case? a feature?). Without the trigger list, no feature can be scored for seat expansion. | — | — | **unknown** — the map cannot say how many seats the feature must add to matter |

**Insight:** The decision is scored on seat-adds, and nothing in this run can supply that denominator. · **Impact:** unknown until supplied; see Next step.

### 2 · Lay of the land — pricing pages and launch posts of scheduling tools and the three meeting platforms · why: is notes a differentiator or table stakes? · searched: Calendly, Cal.com, Chili Piper, HubSpot, Zoom, Google, Microsoft
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| 2.1 | Calendly shipped Notetaker 2026-08-19: summaries, action items, follow-up email; joins Zoom/Meet/Teams; sold via Standard Plus / Teams Plus; 5 free recaps on lower plans; 2-hour cap; English only | S1, S3, S4 | HIGH | **confirms** that a scheduling vendor believes the demand exists; **contradicts** "differentiator" — it is now the incumbent's feature |
| 2.2 | Calendly CEO on the target user: "outward-facing roles like sales and marketing" — not ops | S2 | HIGH | **unknown** for ops leads specifically |
| 2.3 | Chili Piper: no transcripts/summaries on its pricing page; AI is "Meeting Prep", "Email Composer" agents (a search snippet claiming summaries was wrong) | S5 | HIGH | neutral — one scheduling competitor has *not* shipped it |
| 2.4 | HubSpot's AI Notetaker is inside Sales/Service Hub Professional | S6 | HIGH | **contradicts** standalone value — CRM platforms bundle it |
| 2.5 | Google bundled Gemini into all Workspace tiers, +$2/user; Zoom sells per-user ZoomMate tiers with summaries | S7, S10 | HIGH | **contradicts** the seat thesis — monetisation is per-seat price |
| 2.6 | Cal.com: nothing found — searched "Cal.com AI notetaker OR meeting notes OR transcription Cal.ai 2026" on 2026-10-09 | S34 | HIGH (null) | neutral |
| 2.7 | Zoom "Custom AI Companion" $12/user/month add-on — not opened | S36 | ZERO | not counted |

**Insight:** Notes is table stakes on the three meeting surfaces and in the leading scheduling tool, and every shipper prices it as a per-seat uplift (pattern: S3/S4, S6, S7 — three independent). · **Impact:** **contradicts** the belief as a route to *seat* expansion; leaves "want it" open.

### 3 · The users' words — verbatim only · why: falsifier F1 · searched: HN (Algolia API), Reddit (pullpush API, one public mirror), Quora (site:), Calendly community, ClickUp feedback, Capterra
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| 3.1 | **Direct, unprompted:** a Calendly customer asks for notes to live on the contact record so the relationship history is in one place; Calendly cannot do it | S19 | HIGH | **confirms** (one voice) — and note *what* is asked: notes **in the record**, which is your spec's distinctive half |
| 3.2 | *Adjacent (PMs):* the pain of reconstructing the meeting is real, but the room's top reply treats the post as notetaker marketing | S20 | HIGH | weak confirm / trust problem |
| 3.3 | *Adjacent (eng managers):* notes "missing 0-2 critical things", "say essentially the opposite of what we decided"; "Wrong todos, wrong people assigned to todos"; bots blocked from meetings | S13, S14, S15 | HIGH | **contradicts** on quality — two authors, **weak signal** (fewer than three independent) |
| 3.4 | *Adjacent:* the action-items email with timestamps is valued; a culture of agenda + action items is valued | S16, S17 | HIGH | confirms the *artefact* (action items), not the bot |
| 3.5 | A ClickUp user who tried the bundled notetaker wants it off and cannot fully disable it | S29 | HIGH | **contradicts** "bundle it and they will use it" — one voice |
| 3.6 | Ops-specific rooms: **nothing found** — r/OperationsManagement (pullpush, "notetaker") returned zero; r/ExecutiveAssistants, r/projectmanagement, r/sysadmin rate-limited (429); Quora site-search returned no Quora pages; Capterra 403; HN comments on S18 mentioning operations/scheduling: 0 | S21 | HIGH (null) | **F1 not resolved** for ops leads specifically |

**Insight:** One unprompted public ask from a Calendly customer, for notes-on-record; no ops-lead voice found in ops rooms; the loudest public voices are against bots on accuracy and privacy. · **Impact:** F1 did not fire (one ask exists) but the belief is a **weak signal**, not confirmed.

### 4 · Offerings, and evidence of use · why: F2 and the buy option · searched: vendor hiring posts, a spend panel, GitHub, Recall.ai, surveys
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| 4.1 | Mid-market spend panel (900+ companies, transactions): Granola 3x spend in six months, near-zero churn; Otter plateau; Fathom and Fireflies **declining** | S11 | HIGH | **confirms** use; **contradicts** that "a notetaker" per se holds value — the older bot-style notetakers are losing mid-market spend |
| 4.2 | Fathom: "most installed HubSpot marketplace app", "82 NPS", growing "10-20% monthly" (2025), ~100 staff (2026) | S12 | MEDIUM | confirms use (vendor-stated) |
| 4.3 | Open source is alive: meetily 31.6k stars, last commit 2026-09-10, local-only processing | S23 | HIGH | buy/borrow option exists; privacy-first is where OSS went |
| 4.4 | Buy: Recall.ai $0.50/hr recording + $0.15/hr transcription, calendar API free | S24 | HIGH | **changes the decision shape** — the bot is a commodity; your two engineers would be building the *record integration*, not the notetaker |
| 4.5 | Survey (vendor, sample unstated): 19% use AI to take notes; 29% have skipped a meeting relying on AI notes | S22 | MEDIUM | confirms use, weakly |
| 4.6 | ARR figures for Otter/Granola/Fathom; Gartner 41% monthly use | S37, S38 | ZERO | not counted |

**Insight:** F2 is dead — shipped notetakers are used (S8, S9, S11, S12). But the commodity is the bot ($0.65/hr to rent), and the mid-market money is moving from bot notetakers to Granola-style desktop capture. · **Impact:** **confirms** "people use notes"; **contradicts** building the bot yourselves.

### 5 · Method — what the canon says about three QBR asks · searched: The Mom Test, SVPG, Product Talk
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| 5.1 | "Compliments are the fool's gold of customer learning"; "Don't accept customer ideas and feature requests at face value. Do probe to understand the motivation" | S30 | MEDIUM | **contradicts** treating three QBR mentions as evidence until each is probed for past behaviour and money |
| 5.2 | Value risk is "whether customers will buy it or users will choose to use it" — the risk to test first here, not feasibility | S31 | HIGH | frames the test |
| 5.3 | Feature requests from sales conversations "lack context"; use them as "inspiration for interview topics" | S32 | HIGH | **contradicts** going straight from QBR to roadmap |

**Insight:** By the canon, three QBR mentions are interview prompts, not demand. · **Impact:** the belief's evidence base is downgraded to "three leads to interview".

### 6 · Cases — good, bad, ugly · why: F2 and the seat question · searched: Zoom, Google, Calendly, HubSpot, Otter, "shut it down"
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| 6.1 | Zoom: 125k accounts and 1M summaries in under two months (2023); MAU "over four times year over year" (2025) | S8, S9 | HIGH | **confirms** use at scale (vendor-stated) |
| 6.2 | Calendly: 100k beta recordings; "3–4 hours per week" saved (vendor claim); sold as a tier | S1, S4 | HIGH | confirms use; **contradicts** seat lever |
| 6.3 | Google: feature bundled, price +$2/user across tiers | S7 | HIGH | **contradicts** seat lever — the evidenced lever is price |
| 6.4 | Otter: class action for recording without consent (Aug 2025); Calendly's CEO names Otter and Granola as facing privacy allegations | S28, S2 | HIGH | raises viability risk of a bot that joins other people's calls |
| 6.5 | "We shut it down because nobody used it": **nothing found** — searched "sunsetting / shutting down / discontinued AI meeting notes notetaker low usage 2025 2026" on 2026-10-09 | S35 | HIGH (null) | **F2 did not fire** |
| 6.6 | Any case attributing **seat growth** to a notes feature: **nothing found** — read the Calendly, HubSpot, Google, Zoom pricing/launch pages above; none claims seat adds | S1–S10 | HIGH (null) | **contradicts** the goal link; absence of evidence, stated as such |

**Insight:** Everyone who shipped it reports usage; nobody who shipped it reports seats. · **Impact:** F2 dead; the goal link is unevidenced.

### 7 · Constraints · why: the real cost and risk of option (a) · searched: Microsoft 365 message center coverage, NYC Bar, a corporate ban, consent law
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| 7.1 | Teams: external bots approval-gated by default (MC1459141), GA by end Sept 2026; a bot-identification programme with four vendors (Recall.ai is one) | S25 | HIGH | **changes the build**: a bot not in Microsoft's programme is gated in every Teams shop; renting Recall inherits its status |
| 7.2 | NYC Bar: consent before recording with AI; firms: disable for sensitive meetings | S26 | HIGH / MEDIUM | consent UX is mandatory, not optional |
| 7.3 | Corporate bans on third-party notetakers exist (insurer, May 2026) | S27 | HIGH | with S25, S26: pattern of three — buyers' IT/legal can veto |
| 7.4 | Count of all-party-consent states: could not verify (Justia 403) | S39 | ZERO | not counted |

**Insight:** The bot route is being fenced by the platforms and by legal; the surviving route is first-party (platform-native or desktop capture). · **Impact:** raises the true cost of option (a) well above "two engineers".

### 8 · Distribution — where to run the validation · searched: ops/revops communities, HN
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| 8.1 | RevOps Co-op: 21,000+ members, private Slack, newsletter | S33 | HIGH | a room to ask ops leads the Mom-Test questions |
| 8.2 | Calendly community already has your buyer asking (S19); HN thread of 386 comments shows the objections to test against | S19, S18 | HIGH | rooms exist; r/OperationsManagement was empty on this topic (S21) |

**Insight:** The ops rooms are reachable; one already holds an unprompted ask. · **Impact:** the validation test can be run in a week.

---

## 3 · Verdict

**Belief:** *still unknown*, leaning weak — because (1) F1 did not fire but only one direct unprompted ask was found (S19), for notes-on-record, with ops rooms empty or blocked (S21); (2) F2 did not fire — Zoom, Calendly, Fathom all report use (S8, S9, S11, S12); (3) the canon says the three QBRs are prompts, not evidence, until probed (S30, S32).
**The belief as a route to the goal (seat expansion):** *contradicted* — every shipper monetises notes as a per-seat **price** uplift or a bundle (S3/S4, S6, S7), and no case attributes seat adds to it (6.6).

**Falsifier:** did not fire — F1: one unprompted public ask exists; F2: usage is reported everywhere it shipped.

**Contradicting evidence** (to the belief, listed): accuracy and trust — "missing 0-2 critical things", "the opposite of what we decided", "Wrong todos, wrong people" (S13–S15, weak signal: two authors); a bundled notetaker a user wants off and cannot fully disable (S29); independent bot notetakers losing mid-market spend (S11); Calendly aims it at sales and marketing, not ops (S2); platforms gating bots and buyers banning them (S25–S28).

**Top three, by impact on the goal:**
1. **Notes is a price lever, not a seat lever, on every case found** (S1–S4, S6, S7, 6.6). If Q1 expansion means seats, the feature has no evidence behind it; if it means ARPU, the move is a tier, and that is a pricing decision, not a build.
2. **The bot is a $0.65/hour commodity being fenced out of Teams** (S24, S25). Two engineers would be spending Q1 on what Calendly and HubSpot already sell, in the half of the stack that Microsoft is gating. The defensible half is the one the Calendly user asked for and Calendly lacks: notes **on the booking/contact record** (S19).
3. **Public ops-lead demand is one voice** (S19 vs S21). The three QBRs are the only other evidence, and they are unprobed.

**Next step: decide** — against the stated goal, the notes feature cannot be defended in planning as a seat-expansion bet; nothing public supports that link and the shipped cases point to price instead. Walk in with: (a) the two engineers on calendar-sync reliability this cycle, and (b) a zero-engineering notes test that keeps the QBR thread alive — Mom-Test the three QBR accounts this week (what did you do after your last five meetings, what did it cost, what do you pay today), and offer them a Recall.ai-rented pilot of recaps-into-the-record. If two of three pay or add seats for it, the notes build becomes a priced add-on spec for Q2, not a Q1 seat bet. *(The one thing only you can supply before planning: the angle-1 numbers, above all what triggered the last 20 seat-adds.)*

---

## 4 · Self-check (not a scoreboard)

| # | Check | Actual value |
|---:|---|---|
| 1 | Ground truth before search | Section 0 stamped 2026-10-09T04:18Z; first page read 04:19Z or later (SOURCES header) |
| 2 | Every claim is sourced and marked | 34 findings across angles 2–8 cite S1–S39; each S row carries HIGH / MEDIUM / ZERO |
| 3 | No snippet-sourced HIGH | HIGH rows: S1–S11, S13–S21, S23–S29, S31–S35 — each has a URL and date read 2026-10-09; snippet-only claims are S36–S39 (ZERO) and S12/S22/S30 (MEDIUM) |
| 4 | Patterns need three | "Priced per seat / bundled" — S3+S4 (Calendly), S6 (HubSpot), S7 (Google) = 3 ✔ · "Buyers/platforms block bots" — S25, S26, S27 = 3 ✔ · "AI notes are inaccurate" — S13/S15 (one author) + S14 = 2 → labelled **weak signal** ✔ |
| 5 | Empty angles reported | Angle 1: not searched by design, numbers requested · Angle 3 ops rooms: "nothing found — pullpush r/OperationsManagement; 429 on three subs; Quora none; Capterra 403" (S21) · Cal.com (S34) · "shut it down" (S35) · seat-growth case (6.6) |
| 6 | Every insight states its impact | 8 angle insights, each ends in confirms / contradicts / unknown against the belief |
| 7 | The verdict is honest | Contradicting rows S11, S13–S15, S29, S25–S28, S2 appear in section 3; the belief is marked *unknown*, not confirmed, despite both falsifiers failing to fire |
| 8 | Ends in a step a decision can take | *decide*, with the single user-supplied input named |

**Not done in this run:** Reddit ops rooms beyond r/OperationsManagement (rate-limited), G2 reviews, the WaPo article behind S18, the Gartner document (S38), the NYC Bar opinion text (S26), Zoom's current "included at no cost" status (S10). None of these would move finding 1 or 2 of the top three; the first could move finding 3.
