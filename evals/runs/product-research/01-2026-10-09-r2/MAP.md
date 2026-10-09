# Research map — Build AI meeting notes into the scheduling product, or spend the two engineers on calendar-sync reliability? — 2026-10-09

## 0 · Ground truth (written 2026-10-09T07:10:24Z, before the first search)
**Decision:** Build — AI meeting notes (auto-summary + action items pushed into the booking record) **vs** the calendar-sync reliability work support keeps escalating. Same two engineers, one planning cycle. Build · not-build.
**Goal it serves:** Q1 expansion-revenue target — seat adds on existing accounts (~400 paying, per-seat pricing). Not retention. *The target number itself is not in the request — asked for below (ASK), unconfirmed.*
**Belief:** Ops leads at mid-market ops teams want AI meeting notes inside the scheduling tool, because it came up in three QBRs this quarter.
**Falsifier:** (a) No ops people asking for this unprompted anywhere public; **or** (b) every tool that shipped it reports nobody used it. *(User's own words. A third falsifier is implied by the goal and drafted here, unconfirmed: (c) no evidence anywhere that a notes feature caused seat expansion rather than retention.)*
**Already known:** Three QBR mentions this quarter (sample of 3, solicited in a QBR context). Support is escalating calendar-sync reliability — frequency and revenue-at-risk not given.

### Angle map and search keys (written before searching)
| # | Angle | Kept / cut | Keys |
|---:|---|---|---|
| 1 | Goal | kept — ASK rows only | Q1 expansion target in ₹/$ · current seats-per-account · what moved seats last two quarters |
| 2 | Lay of the land | kept | "calendly" "ai" "meeting notes" launch · "chili piper" AI notes · "cal.com" AI · "zoom ai companion" adoption · "google meet" "take notes for me" · "copilot" "recap" |
| 3 | Users' words | kept | reddit r/revops r/salesops r/operations "meeting notes" "scheduling" · HN "ai meeting notes" · quora "ops" "meeting notes tool" · "calendly" "sync" "not syncing" (the alternative, for contrast) |
| 4 | Offerings + evidence of use | kept | fathom · fireflies · otter · tl;dv pricing + review counts · GitHub "meeting notes" open source stars + last commit · zoom ai companion "accounts" |
| 5 | Method | kept | Mom Test "feature requests" · Continuous Discovery Habits "opportunity" · Inspired "value risk" · Lean Customer Development |
| 6 | Cases | kept | "ai meeting notes" "nobody used" · "shut down" "ai notetaker" · "zoom ai companion" "usage" numbers · scheduling tools that added notes and what happened · "calendar sync" "churn" case |
| 7 | Constraints | kept, light | recording consent two-party · Google Meet bot policy · Zoom app marketplace notetaker · Microsoft Graph calendar throttling |
| 8 | Distribution | **cut** — the decision is build-vs-reliability for existing accounts, not reach. Unconfirmed; restore if the decision widens. | — |

*Cut made by the skill, not the user, because the run allows one question and the decision was present. Confirm or restore in the map.*

## 1 · The map
Everything found, one screen. Direct evidence from mid-market ops leads: **none reached** — the lane was blocked (S16), not empty. Everything below is adjacent, vendor-claimed, or from the alternative's users.

| Segment | Their words (verbatim, S#) | What they use today | What is missing | Where they are |
|---|---|---|---|---|
| **Mid-market ops leads** (the target) | *none found* — r/revops, r/salesops, r/operations never read (S16, ZERO); Quora empty (S17); no HN ask from an ops lead (S18) | unknown — ASK (S1) | unknown | r/revops · r/salesops (unreached this run) |
| Engineering / tech teams (*adjacent*) | "it becomes completely useless when holding meetings in a hybrid fashion … It's a total dealbreaker for us" (S9) · "my note taker has been an incredibly helpful piece of technology in professional meetings where domain decisions had to be recorded" (S11) · "companies banned certain meeting notetakers due to data concerns … So they went back to manual note-taking" (S14) | Granola, local-first OSS (S22–S24) | hybrid-room diarisation (S9); privacy without a bot (S10, S14) | HN |
| Solo practitioner / SMB (*adjacent*) | "I try to bottleneck everything here by getting a Calendly set up … I try to take notes via paper or MS Word while chatting" (S15) | Calendly + paper/Word + TaxDome | notes attached to the booking — unprompted, one voice | r/taxpros |
| Scheduling-tool users (Calendly community) | "not all events are updating to my Calendly meetings and availability causing me to have double-bookings" (S19) · "I used to have notetaker automatically joining my calls and now it's gone" (S20) | Calendly; Notetaker on Plus tiers | sync reliability — staff answer is "disconnecting and reconnecting" (S19); bot-join reliability (S20) | community.calendly.com |
| Enterprise IT / security | — (only search summaries: a university disabling third-party notetakers, S31) | native Zoom/Google/Teams summaries | consent, bot admission (S37, S38) | — |

**Cases to follow:**
- **Calendly Notetaker** (Aug 2026) — what they did: bot-based notes + recap + action items, bundled into *new* Standard Plus / Teams Plus tiers · good: "more than 100,000 meeting recordings" in beta, "highest satisfaction score" (vendor claim) · bad: English only; monetised as a tier, not seats · ugly: bot stopped joining on an AWS-outage day, a new support surface · S3, S6, S20.
- **Cal.com Notes** — what they did: summary "saved to the booking", paid plans only, waitlist · good: the exact shape of the proposed feature exists · bad: gated rollout, no usage numbers · S5.
- **Zoom AI Companion** — what they did: summaries "included with paid Zoom Workplace plans"; the paid tier is a separate $20/user ZoomMate · good: 1M summaries in under two months, MAU 4x YoY · ugly for the seat thesis: the market leader priced notes at zero · S7, S27, S28.
- **Microsoft 365 Copilot** (*adjacent*) — a paid AI add-on across a suite: 15M paid seats = "just 3.3%" of the base after two years · S29.

## 2 · Angles

### 1 · Goal — ASK only · why: the number that must move is the user's, never the web's · nothing searched
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 1.1 | The Q1 expansion target, seats-per-account, ARPA and what drove seat adds in the last two quarters were not in the request | S1 | ASK | unknown | the decision — without it, neither option can be sized |
| 1.2 | Sync escalations: count, accounts, seats, any attributed downgrade — not in the request | S2 | ASK | unknown | the decision — the alternative is unsized too |

**Insight:** Both options are unsized; the request has a direction (seats, not retention) but no number. · **Belief:** unknown · **Also changes:** the next step (section 3).

### 2 · Lay of the land — opened vendor pages · why: if scheduling tools already ship notes, "want" is being tested at scale by others · searched: Calendly, Cal.com, Chili Piper, SavvyCal, Zoom
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 2.1 | Calendly shipped Notetaker + Callie on 2026-08-19, bundled into new Standard Plus / Teams Plus tiers; claims 100k+ beta recordings and 3–4 h/week saved | S3 | HIGH | **weak confirm** — the category leader bet the same way; the usage number is a vendor claim with no method | the build — a direct scheduling competitor now has it |
| 2.2 | Notetaker is an add-on/tier on top of $10 and $16 per-seat plans; not on Free; English only | S6 | HIGH | **contradicts** (the goal link) — monetised as a tier upgrade, not as seat growth | the pricing of the feature, if built |
| 2.3 | Cal.com Notes: summary "saved to the booking", paid plans only, waitlist | S5 | HIGH | **weak confirm** — the exact feature shape exists; no usage evidence | the spec — "saved to the booking" is the pattern |
| 2.4 | Zoom: summaries "included with paid Zoom Workplace plans"; paid agentic tier is a separate $20/user | S7 | HIGH | **contradicts** (the goal link) — the biggest meeting platform priced notes at zero; table stakes, not an upsell | positioning — notes alone cannot carry a price |
| 2.5 | TechCrunch: "There's a litany of note-takers" … "the competition in this space is intense"; Otter and Granola face privacy allegations | S4 | HIGH | **counter-signal** — crowded, and the entrant's differentiator is privacy, not notes | the build — differentiation must be the booking record, not the notes |
| 2.6 | No Chili Piper or SavvyCal notes feature surfaced | S8 | NONE | unknown | nothing |

**Insight:** Three independent vendors (S5, S6, S7) price AI notes as a tier, add-on or free inclusion — never per seat — which is a **pattern on three**: the market does not sell notes as seat expansion. · **Belief:** contradicts (the goal link; the "want" half is weakly confirmed by competitors building it) · **Also changes:** the pricing question becomes the decision.

### 3 · The users' words — archive APIs + HN Algolia + opened community threads · why: falsifier (a) lives here · searched: S16–S18 strings; HN "ai meeting notes", "ai notetaker"; Calendly community
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 3.1 | The ops-lead subreddits were never read — PullPush 429 ×8, Arctic Shift non-JSON ×9 | S16 | ZERO | unknown — **falsifier (a) is undetermined, not passed** | the next step — this lane must be re-run |
| 3.2 | Quora: no results; HN: no ops-lead ask for notes in a scheduling tool | S17, S18 | NONE | unknown — absence in two thin lanes, not in the right room | nothing |
| 3.3 | Unprompted, a solo tax pro: Calendly for scheduling, "notes via paper or MS Word while chatting", can't "keep everything straight … tracking the notes I take for them on discovery calls" | S15 | HIGH | **weak confirm, adjacent** — one voice, wrong segment, right pain (notes next to the booking) | the spec — the job is "notes attached to the booking", not "AI summary" |
| 3.4 | Professionals who use notetakers value them for decisions, todos and later retrieval | S11, S12 | HIGH | **weak confirm, adjacent** — two voices, tech audience | nothing |
| 3.5 | Hybrid rooms make notetakers "completely useless … a total dealbreaker" | S9 | HIGH | **counter-signal, adjacent** | the build — in-office ops teams will hit this |
| 3.6 | Bots are hated and visible; recording disclosure is a legal need in many jurisdictions | S10 | HIGH | **counter-signal, adjacent** | the build — bot vs bot-free is a design decision |
| 3.7 | A client's notetaker emailed all participants the client's own negotiating strategy | S13 | HIGH | **counter-signal** — the failure mode a B2B buyer fears | the build — default delivery scope |
| 3.8 | Companies banning notetakers over data concerns, people "went back to manual note-taking" | S14 | HIGH | **counter-signal, adjacent** — founder's account | positioning — data residency will be asked |
| 3.9 | Calendly user: notetaker vanished, "no idea how to re-activate it" — a user who depended on it; staff: outage broke bot joining | S20 | HIGH | **weak confirm** — one user's dependence; also a new support surface | the build — bot-join reliability is a cost the sync team will inherit |
| 3.10 | Calendly user, 2026-06: calendar events not syncing, "causing me to have double-bookings"; staff answer: disconnect and reconnect | S19 | HIGH | **counter-signal** — the alternative's pain is live, public and unsolved at the category leader | the decision — sync is not a solved problem to deprioritise |
| 3.11 | Six more Calendly sync/double-booking threads surfaced (Oct 2025–Sep 2026), one opened, one 403 | S21 | ZERO | unknown | nothing until opened |

**Insight:** The only unprompted "notes beside the booking" voice is one solo practitioner (S15); the room that could settle falsifier (a) was never entered (S16). · **Belief:** unknown · **Also changes:** the next step — the gap is named in section 3.

### 4 · Offerings, and evidence of use — opened pricing pages, GitHub API, earnings coverage · why: falsifier (b) lives here · searched: Fathom, Fireflies, Zoom, open-source notetakers
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 4.1 | Open-source notetakers are alive: meetily 31.6k stars (pushed 2026-09-15), anarlog/hyprnote 9.5k (pushed today), vibe 7.7k (pushed 2026-10-06) | S22, S23, S24 | HIGH | **confirms** (demand for the capability exists — three active repos) — but among developers, *adjacent* | build-vs-buy — transcription/summarisation is commodity; the booking-record integration is the only non-commodity part |
| 4.2 | Fathom: unlimited free recordings and summaries; Team $19/user/mo | S25 | HIGH | **contradicts** (the goal link) — the standalone leader gives notes away and charges for team features | pricing |
| 4.3 | Fireflies: "thousands of organizations"; no count | S26 | HIGH | unknown | nothing |
| 4.4 | Zoom: 1M summaries in <2 months, 125k accounts (2023); MAU 4x YoY (2025) | S27, S28 | MEDIUM | **confirms** (falsifier (b) did not fire) — the largest shipper reports heavy use, not none; vendor-reported | nothing |

**Insight:** Falsifier (b) did not fire — every tool that shipped notes and reported anything reports use (S3, S27, S28), but all three are vendor-reported and none links use to seat growth. · **Belief:** confirms the "want" half (weak: vendor-claimed) · **Also changes:** build-vs-buy — the notes engine should be bought or open-sourced; only the booking-record push is yours.

### 5 · Method — opened the canon's public pages · why: three QBR mentions are the exact input the literature warns about · searched: Cagan, Torres, Fitzpatrick
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 5.1 | Cagan: value risk is "whether customers will buy it or users will choose to use it" and "the toughest risk is usually value risk" | S34 | HIGH | unknown — a lens: the QBR evidence addresses neither "buy" nor "use" | the method — test value before building |
| 5.2 | Torres: the tree runs from outcome → opportunities → solutions and is "nearly impossible to create when you don't have good inputs" | S35 | HIGH | unknown — "AI notes" entered as a solution, with no opportunity under it | the method — name the opportunity (e.g., "ops leads lose what was agreed in the booked meeting") before the solution |
| 5.3 | Mom Test: "Any time a customer starts giving you ideas and feature requests, it is critical that you get under the hood and understand why"; "I would" is fluff | S36 | MEDIUM | **contradicts** the evidential weight of the three QBRs — solicited requests are the named bad-data type | already known — the three QBRs are reclassified from evidence to leads |

**Insight:** By the canon the three QBR mentions are leads, not evidence; the belief as stated has not yet been tested. · **Belief:** contradicts (the evidence base, not the claim) · **Also changes:** the method for the gap in section 3.

### 6 · Cases — good, bad, ugly — opened press, community and earnings coverage · why: "nobody used it" is falsifier (b) · searched: S31, S33 strings; Calendly, Zoom, Copilot
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 6.1 | Calendly (good): 100k beta recordings, "highest satisfaction score" — vendor claim, no denominator | S3 | HIGH | **weak confirm** | nothing |
| 6.2 | Calendly (ugly): Notetaker stopped joining after an AWS outage; user had "no idea how to re-activate it" | S20 | HIGH | **counter-signal** — the feature adds a reliability surface to a team already behind on sync | the build — ops cost |
| 6.3 | Copilot (bad, *adjacent*): 15M paid seats, "just 3.3%" of the base; DAU up 10x | S29 | MEDIUM | **adjacent, contradicts** — a paid AI add-on across a huge base converted a sliver | pricing — an add-on take-rate assumption must be low |
| 6.4 | Earmark "70% of action items never completed", "four in five miss critical context" — vendor blog, numbers trace to unopened vendor pages | S30 | ZERO | unknown — not usable either way | nothing |
| 6.5 | No shipped notetaker found reported shut down for low usage | S31 | NONE | **confirms** falsifier (b) did not fire — searched, nothing found | nothing |
| 6.6 | No independent case of a notes feature driving seat expansion; only vendor marketing | S33 | NONE | **contradicts** (the goal link) — searched, nothing found | the decision — the seat thesis has no public precedent |
| 6.7 | Zoom summary-quality thread unreadable | S32 | ZERO | unknown | nothing |

**Insight:** The shipped cases show use (vendor-claimed) and no shutdowns, and zero public evidence that notes moved seats. · **Belief:** confirms "want" weakly; contradicts the seat link · **Also changes:** the decision hinges on pricing, not on demand.

### 7 · Constraints — opened secondary reports; primary pages attempted · why: a bot-based build inherits consent law and platform admission rules · searched: Otter lawsuit, Google Meet bot policy, consent law, Graph throttling
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 7.1 | Otter sued (N.D. Cal., Aug 2025) under federal and California wiretap/privacy law for recording non-users | S37 | MEDIUM | **counter-signal** — consent is a product requirement, not a footnote | the build — consent capture per attendee |
| 7.2 | Google Meet (from Mar–Apr 2026) routes bots to a "potentially risky" queue "automatically denied unless the host intervenes" | S38 | MEDIUM | **counter-signal** — a bot-based notetaker needs a host click on every Meet call | the build — bot-free capture or native-platform summaries |
| 7.3 | Calendly's own notetaker: English only | S6 | HIGH | unknown — a constraint they accepted | the spec — language scope |
| 7.4 | All-party-consent state list not read (RCFP sub-pages); Graph calendar throttling section not reached | S39, S40 | ZERO | unknown | nothing until read |

**Insight:** Two platform/legal constraints (S37, S38) plus the bot-aversion in S10 and S14 make a **pattern on four**: a bot that joins calls is the wrong architecture for a 2026 build. · **Belief:** unknown (constrains the how, not the want) · **Also changes:** the build — push native-platform or client-side transcripts into the booking record; do not build a bot.

### 8 · Distribution — **cut** (ground truth, section 0): the decision is for existing accounts. *Unconfirmed cut.* No search run; no SOURCES row.

## 3 · Verdict
**Rows labelled contradicts / weak confirm / counter-signal / adjacent, contradicts in section 2 (listed before judging):** S3 · S5 · S6 · S7 · S4 · S15 · S11 · S12 · S9 · S10 · S13 · S14 · S20 · S19 · S25 · S36 · S29 · S33 · S37 · S38. Every one is cited below.

**Belief:** still unknown — because (1) the only room that could show ops leads asking unprompted was never read (S16, ZERO), so falsifier (a) is undetermined rather than passed; (2) what was found for "want" is adjacent or vendor-claimed — one solo practitioner (S15), two tech users (S11, S12), Calendly's own beta number (S3), Cal.com's waitlist (S5); (3) the three QBR mentions are, by the canon, feature requests to dig under, not evidence (S36). The belief is neither confirmed nor contradicted; it is untested.

**Falsifier:** (a) did not fire and did not pass — lane blocked (S16). (b) did not fire — every shipper that reports anything reports use (S3, S27, S28) and no shutdown for low usage was found (S31). Drafted (c), *unconfirmed*: fired — no public evidence anywhere that notes moved seats (S33), and the three vendors that shipped it price it as a tier, add-on or free inclusion (S5, S6, S7).

**Contradicting evidence:** the goal link — S6 (Calendly: a Plus tier, not seats), S7 (Zoom: free with paid plans), S25 (Fathom: free unlimited), S33 (no seat-expansion case found), S29 (adjacent: a paid AI add-on converted 3.3%); the evidence base — S36 (QBR requests are the named bad-data type); counter-signals on the build — S4 (crowded, privacy is the differentiator), S9 (hybrid rooms), S10 (bots hated, disclosure needed), S13 (transcript leaked a client's strategy), S14 (companies banning notetakers), S20 (bot-join broke on an outage), S19 (sync pain live at the category leader — the alternative is real), S37 (Otter lawsuit), S38 (Meet default-denies bots). Weak confirms that do not outweigh them — S3, S5, S15, S11, S12. None dropped.

**Top three, by impact on the goal:**
1. **Notes are priced as a tier, add-on or giveaway by everyone who shipped them (S5, S6, S7, S25) — never as seat growth.** If the Q1 target is seats, the feature only pays if it is sold as a per-seat add-on your accounts take; no public precedent says they will (S33), and the one adjacent precedent converted 3.3% (S29).
2. **The ops-lead room was not read (S16).** Falsifier (a) is the cheapest test on the map and it is still open; nothing here licenses "ops leads want it".
3. **If built, build it bot-free into the booking record (S5 shape; S10, S14, S37, S38 constraints) and buy or open-source the engine (S22–S24).** The sync team inherits bot-join reliability otherwise (S20) while the sync pain stays public (S19).

**Next step:** **one named gap** — the per-seat add-on take-rate among your own accounts: of the three QBR accounts plus seven more ops leads, how many would pay a stated ₹/$ per seat for a summary and action items landing in the booking record, asked Mom-Test style ("what happened after your last booked meeting; how are the notes handled today; what did it cost you") — not "would you". Where to look: those ten accounts this week (S1, S2 supply the denominator), and r/revops · r/salesops once the archive API unblocks (re-run the S16 strings; a 10-minute retry). The decision reverses on that number — a 3% take-rate funds sync; a 30% take-rate funds notes — so it is not a *decide* with a caveat.

## 4 · Self-check (not a scoreboard)
| Check | Actual value |
|---|---|
| 1 · Ground truth before search | Section 0 written 2026-10-09T07:10:24Z; first search tool call issued after that write returned, same minute; first SOURCES rows read ≥ 07:10:30Z |
| 2 · Every claim sourced and marked | 40 SOURCES rows (S1–S40); every section-2 finding cites ≥1 row; marks used: HIGH 21 · MEDIUM 6 · ZERO 6 · NONE 5 · ASK 2 (S36 carries two URLs, one mark) |
| 3 · No snippet-sourced HIGH | 21 HIGH rows, each with URL and date read 2026-10-09; S15 read via PullPush archive API (noted), S22–S24 via GitHub API (noted) |
| 4 · Patterns need three | "priced as tier/add-on/free" — S5, S6, S7 (+S25) = 4 independent; "bot is the wrong architecture" — S10, S14, S37, S38 = 4; "want" among ops leads — 1 adjacent voice (S15), labelled weak |
| 5 · Empty angles reported | Angles 1–7 have rows; angle 8 cut in section 0 and reported in section 2; ZERO lanes named (S16, S21, S32, S39, S40) |
| 6 · Every insight states its impact | 7 angle insights, each with Belief + Also changes; 37 finding rows, each with a Belief value and an Also-changes value |
| 7 · Verdict honest | 21 labelled finding rows across 20 source ids listed before judging; all 20 ids cited in Contradicting evidence; 0 dropped |
| 8 · Ends in a step | one named gap — the per-seat add-on take-rate among ten own accounts (+ S16 lane re-run) |
