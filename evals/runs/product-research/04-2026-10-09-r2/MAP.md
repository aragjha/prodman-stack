# Research map — Should we build "spend insights" (AI categorisation + monthly narrative) before the next funding round? — 2026-10-09

## 0 · Ground truth (written 2026-10-09T07:10:04Z, before the first search)

**Decision:** Build "spend insights" (AI categorisation + monthly narrative) before the next funding round — or not, and spend the pre-round cycles elsewhere. Build · kill · defer.
**Goal it serves:** *unconfirmed, drafted* — retention (losing fewer users to competitors) as a number leadership can show in the round: e.g. M3 retention, or churn attributed to "missing feature". The actual number, baseline and the size of move that matters are the user's own — asked for, not substituted (S1, ASK).
**Belief:** Spend insights is table stakes in Indian consumer fintech now, and we are losing users to apps that have it.
**Falsifier:** (a) the apps that have it do not show retention gains, or (b) our own users do not mention it when they churn.
**Already known:** *unconfirmed, drafted* — nothing supplied. Assumed: the user knows which two competitor apps already ship the feature but did not name them. Drafted choice of the two: **Fi Money** and **Jupiter** (both ship auto-categorised spend analysis with a monthly summary on a consumer current-account app in India). *Unconfirmed — if the two apps leadership has in mind are different (CRED, Axio, Money View, INDmoney), angle 3/4 rows need re-running against those.*

**Two specific asks from the user, and what the map can honestly do with them:**
1. *Indian personal-finance-app market size, Gartner or RedSeer, a number leadership will accept.* The map records what was publicly opened. A paywalled headline quoted via press release is **MEDIUM** at best; a number that cannot be opened is **ZERO**; a search that finds nothing is **NONE**. None are rounded up because the slide is on Thursday.
2. *Top user complaints about the two apps, from G2 or app-store reviews, verbatim.* G2 lists B2B software; consumer fintech apps are rarely there — reported as searched. App-store review pages are opened and quoted verbatim where reachable.

### The angle map and search keys (written before searching — cut what does not bear on the decision)

| # | Angle | Search keys (problem phrase + platform + company + angle word) | Bears on |
|---:|---|---|---|
| 1 | Goal | ASK: our M1/M3 retention, churn-survey reason tags, % of churned users naming "insights/categorisation" | Falsifier (b) |
| 2 | Lay of the land | "India personal finance management app market size RedSeer" · "Gartner personal financial management India" · "Account Aggregator spend analytics India" | Ask 1 |
| 3 | Users' words | pullpush/reddit r/personalfinanceindia r/IndiaInvestments "expense tracker" "categorisation wrong" "Fi Money" "Jupiter"; Play Store / App Store reviews Fi Money, Jupiter; HN Algolia "spend categorization" | Ask 2, belief |
| 4 | Offerings, evidence of use | Play Store install counts + ratings for Fi, Jupiter, Axio (ex-Walnut), Money View; feature pages: "Fi insights", "Jupiter money insights" | Belief ("table stakes") |
| 5 | Method | Kano must-be vs attractive (the canonical definition of "table stakes"); *The Mom Test* on asking churned users; *Continuous Discovery Habits* opportunity → assumption tests | How to test falsifier (b) |
| 6 | Cases | Mint shutdown 2024 (Intuit); Walnut → Axio; Money View pivot from tracker to lending; Monarch post-Mint | Falsifier (a) |
| 7 | Constraints | Google Play SMS/Call Log permission policy; RBI Account Aggregator (consent, FIU); iOS no SMS access | Build cost, data source |
| 8 | Distribution | same rooms as angle 3 — subreddits, Jupiter/Fi communities, X fintech India | Launch, not the decision |

---

## 1 · The map

| Segment | Their words (verbatim, S#) | What they use today | What is missing | Where they are |
|---|---|---|---|---|
| Neobank power users who already have insights (Jupiter) | "The single most important feature to me is the categories feature...a selected few categories don't work for everyone." (S10) · "Custom category will definately help as it will allow users to categorise their Expenses that best suits their tracking approach." (S9) | Jupiter Insights + tags (live since Feb 2022, S20) | Custom categories; the preset list "don't work for everyone" | community.jupiter.money (S35) |
| Multi-account / RuPay-CC users | "I am facing issue with the expense tracking when a upi payment is done via rupay credit card." (S8) | Jupiter spends breakdown | Transactions outside the home bank — staff: "only supported for transactions done using the Jupiter savings account and/or debit card, Jupiter credit card, or a linked savings account." (S8) | same |
| Comparison shoppers across neobanks | "Did u check on FI Minutes(Like monthly review on account finances). It looks cool." · "Its like Jupiter insights pro /summary of statement with more details." (S11) | Both Fi Minutes and Jupiter Insights | Nothing — they rate the monthly narrative as "cool", not as a reason to switch | same |
| Jupiter App Store reviewers | "This is absolutely disgusting service from Jupiter's end. Probably the worst neo bank service I have used." · KYC "frustratingly slow, inefficient" · one 3★: "helps me keep track of my spends." (S12) | Jupiter | Support, KYC, account service — not insights | App Store IN |
| Mainstream Indian finance-app downloaders | — (numbers, not words: S7) | PhonePe, Navi, Paytm, GPay, Bajaj, Kotak 811, super.money, Groww, BHIM | No standalone expense tracker / PFM app in the top-10 downloads, May 2025 – Apr 2026 (S7) | App stores |
| Adjacent — US/HN budgeting users | "I am not going to spend more than 5 minutes to look at my bank statements." (S16) · apps "learn" categories over time via open banking (S17) | Open-banking categorisers | Zero-effort categorisation | Hacker News |
| Fi Money reviewers | **none obtained** — App Store IN/US paths 404, mirror timed out, Kimola 410 (S13); G2 gone/403 (S15) | — | — | — |

**Cases to follow:** the three worth copying — what they did · good · bad · ugly · source
1. **Mint → Credit Karma (US).** The category-defining free spend-insights app. Good: 3.6M MAU (2021). Bad: "development has slowed down considerably in recent years". Ugly: shut 2024; "setting monthly budgets and customized categories didn't make the cut" — only "spending and net worth tracking" survived inside a credit product. S24 (MEDIUM), S25 (HIGH).
2. **Walnut → axio (India).** India's original SMS spend tracker. Good: money management kept as one of three tools. Bad: the Walnut brand is gone. Ugly: the business is credit — "from 400,000 to 4.5 million credit customers" — the tracker became the hook, not the product. S27 (HIGH).
3. **Monarch (US, adjacent).** The anti-case: "subscriber base surge by 20 times in the year after Intuit announced it was closing Mint"; $75M at $850M. Good: proves paid demand for standalone PFM. Bad: US, subscription, post-Mint vacuum. Ugly: no retention figure published. S26 (HIGH, adjacent).
(Money View is the fourth: 3M downloads in two years on SMS auto-categorisation in 2016 (S28, HIGH), now a lender — but the pivot's reason exists only as an unsourced quote (S29, ZERO).)

---

## 2 · Angles

### 1 · Goal — ask, never substitute · why: falsifier (b) lives only in our churn data · searched: nothing, by design
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 1.1 | Retention baseline, the delta that matters for the round, churn-reason tags for the last 90 days, and the % of churned users naming spend tracking / insights — requested, not supplied | S1 | ASK | unknown | the next step: this is the one named gap |
**Insight:** falsifier (b) cannot be tested from the web; only our exit-survey and support-ticket tags can fire it. · **Belief:** unknown · **Also changes:** next step.

### 2 · Lay of the land — market-size ask first, then who is actually downloaded · why: ask 1 and the "now" in "table stakes now" · searched: RedSeer, Gartner, IMARC, Sahamati, AppTweak
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 2.1 | **No Gartner number exists in the open** for PFM in India | S4 | NONE | unknown | the slide: do not cite Gartner |
| 2.2 | **No RedSeer number exists in the open** for PFM apps in India | S3 | NONE | unknown | the slide: commission or drop |
| 2.3 | The only opened market-size figure: IMARC, "USD 44.5 Million in 2025" → "USD 65.3 Million by 2034 … CAGR of 4.24%" — personal-finance *software revenue*, vendor estimate, methodology not shown | S2 | HIGH | contradicts (weak) — a USD 45M, 4% CAGR category is not what "table stakes" looks like | the slide: too small and too soft to lead with |
| 2.4 | The strongest public demand number: on the Account Aggregator network "almost half of the consents have been utilized for Personal Finance Management (PFM)" and RIAs show "28% quarterly growth rate in the number of consents taken for PFM" (Aug 2024) | S5 | HIGH | confirms (weak) — demand for PFM data-pulls is real and growing; says nothing about retention | the slide: this is the citable number, from Sahamati directly |
| 2.5 | FY25 "7.69 million personal finance management (PFM) customers were served" (Sahamati data via Business Standard) — page 403, not opened | S6 | ZERO | unknown | the slide: open Sahamati's FY25 report before using |
| 2.6 | Top-10 most-downloaded finance apps in India, May 2025 – Apr 2026, are payments, loans and brokers; **no PFM / expense-tracker app in the list** | S7 | HIGH | contradicts — if insights were table stakes for Indian consumers, a PFM app would surface | positioning: insights is a feature inside a money app, not a category |
**Insight:** the market has demand signal (AA consents) but no credible analyst number and no standalone winner; "table stakes" is not visible at the category level. · **Belief:** contradicts (weak) · **Also changes:** the slide — use Sahamati's AA data, not a market-size figure.

### 3 · The users' words — opened forums and store pages, verbatim only · why: ask 2 and the Kano test (do users complain when it is absent, or only when it is poor?) · searched: Jupiter community, App Store IN, pullpush, G2, HN Algolia
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 3.1 | Jupiter users who *have* categorisation complain about its limits: preset categories "don't work for everyone"; "Custom category will definately help" (24 replies, 7 likes) | S9, S10 | HIGH | confirms (weak) — Kano must-be behaviour: dissatisfaction when done poorly | the build: custom categories are day-one scope, not v2 |
| 3.2 | Coverage gap is the loudest bug: RuPay-CC UPI spends missing from categories; staff confirm aggregation covers only Jupiter accounts/cards or a linked account | S8 | HIGH | confirms (weak) — users expect all their spend, not the home bank's | the build: cross-account data (AA) is the hard part |
| 3.3 | Users compare Fi Minutes and Jupiter Insights as "cool" — not as a reason to switch | S11 | HIGH | contradicts (weak) — no switching language found | positioning |
| 3.4 | Jupiter App Store IN: the negative reviews are service and KYC ("worst neo bank service", KYC "frustratingly slow"); the one mention of insights is a 3★ "helps me keep track of my spends." (4 reviews visible; store shows no aggregate) | S12 | HIGH | contradicts — users leave these apps over service, and insights does not stop them | the belief's second half ("losing users to apps that have it") |
| 3.5 | **Fi Money: nothing obtained.** App Store IN/US 404, mirror timeout, Kimola 410; "4.5★ from 24,000" is a snippet | S13 | ZERO | unknown | ask 2 is half-answered |
| 3.6 | **G2: nothing obtained.** Fi page 410 Gone, Jupiter seller page 403 | S15 | ZERO | unknown | ask 2: G2 is the wrong room for consumer apps |
| 3.7 | **Reddit: lane unreachable** — pullpush 429 ×3, reddit.com blocked | S14 | ZERO | unknown | re-run angle 3 on Reddit tomorrow |
| 3.8 | *Adjacent (US):* "I am not going to spend more than 5 minutes to look at my bank statements." (2011); apps "learn" categories over time via open banking (2026) | S16, S17 | HIGH | unknown — adjacent, not merged | the build: categorisation must be automatic; manual tagging kills it |
**Insight:** every verbatim complaint about the feature comes from users who already have it; the top complaints about the apps are service and KYC, not insights. · **Belief:** contradicts (weak — 4 store reviews, 3 forum threads; pattern needs three independent rooms and Reddit/Fi were unreachable) · **Also changes:** the build (custom categories, cross-account coverage).

### 4 · Offerings and evidence of use — feature pages and store listings · why: "table stakes" needs the feature to exist and be used · searched: fi.money, Play Store, Jupiter community
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 4.1 | Jupiter Insights + tags live since Feb 2022 and iterated publicly | S20 | HIGH | confirms — the feature exists at a competitor | nothing |
| 4.2 | Fi Minutes (monthly recap) exists — known only from a Jupiter user's description | S11 | HIGH | confirms — the feature exists at a second competitor | nothing |
| 4.3 | Install counts, ratings, review totals for either app: **not read** — Play pages 404 / truncated; Fi feature page 404 | S18, S19 | ZERO | unknown | falsifier (a) cannot be tested on public usage data |
**Insight:** both named competitors ship it; whether it retains anyone is invisible from outside. · **Belief:** confirms (existence only) · **Also changes:** falsifier (a) needs their numbers, which do not exist publicly.

### 5 · Method — what the canon says about "table stakes" and about asking churned users · why: the belief uses a Kano term without a Kano test · searched: Kano 1984, Torres, Fitzpatrick
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 5.1 | Kano must-be: "requirements that the customers expect and are taken for granted. When done well, customers are just neutral, but when done poorly, customers are very dissatisfied." — the test for "table stakes" is dissatisfaction at absence, measured on *our* users, not inferred from competitors | S21 | MEDIUM | unknown — gives the test, not the answer | the method: run a Kano pair (functional/dysfunctional) on 100 active users before building |
| 5.2 | Torres: "an opportunity is an unmet customer need, pain point, or desire" that "emerge[s] from these stories" — interview-derived, not feature-derived | S22 | MEDIUM | unknown | the method: 10 churned-user interviews, story-based |
| 5.3 | *The Mom Test* rules (past specifics, not future opinions) — book not opened today | S23 | ZERO | unknown | the method: never ask "would you use spend insights?" |
**Insight:** the belief is a Kano claim; the canon says prove it with our users' dissatisfaction, not with competitor feature lists. · **Belief:** unknown · **Also changes:** the method — Kano survey + 10 churn interviews are cheaper than the build.

### 6 · Cases — what happened to the apps that led with spend insights · why: falsifier (a) · searched: Mint, Walnut/axio, Money View, Monarch
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 6.1 | Mint — 3.6M MAU, the category leader — was shut; budgets and custom categories "didn't make the cut"; only "spending and net worth tracking" survived inside Credit Karma | S24, S25 | MEDIUM, HIGH | contradicts — the best-known insights product did not sustain itself | positioning: insights is a hook for a monetising product, not the product |
| 6.2 | Walnut (India's original SMS tracker) → axio: "money management tools" is one of three lines; the growth line is "400,000 to 4.5 million credit customers" | S27 | HIGH | contradicts — the Indian pioneer's retention engine is credit | same |
| 6.3 | Money View 2016: 3M downloads in two years on SMS auto-categorisation; now a lender — the pivot's reason exists only as an unsourced blog quote | S28, S29 | HIGH, ZERO | contradicts (weak) — the pivot is fact, the "users want credit not tracking" quote is not verified | trust: do not put S29 on a slide |
| 6.4 | *Adjacent (US):* Monarch "surge by 20 times" in subscribers after Mint's closure; $75M at $850M; no retention figure | S26 | HIGH | counter-signal — standalone paid demand exists, in a vacuum, in the US | nothing for the India decision |
| 6.5 | A snippet claiming Walnut was bought by Paytm in 2021 contradicts the opened axio source — rejected | S30 | ZERO | unknown | trust |
**Insight:** three spend-insights leaders (Mint, Walnut, Money View) ended inside credit businesses — labelled **weak signal**: two verified (S25, S27), one unverified (S29); the one counter-case (Monarch) is adjacent. · **Belief:** contradicts (weak) · **Also changes:** positioning — if built, insights must feed a monetising step, not stand alone.

### 7 · Constraints — where the categorisation data can legally come from · why: build cost before the round · searched: Google Play policy, developer reports, AA framework
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 7.1 | Google Play: SMS/Call Log "only … within permitted uses"; apps "must be actively registered as the default SMS, Phone, or Assistant handler before prompting" — policy changes effective 27 Jan 2027 | S31 | HIGH | unknown | the build: SMS parsing is not the route |
| 7.2 | *Adjacent (developer):* a finance app was rejected because "reading SMS for financial data … doesn't qualify for the exceptions" (Dec 2025) | S32 | HIGH | unknown | the build: confirms 7.1 in practice |
| 7.3 | Account Aggregator is the consent-based route (half of consents already PFM, S5); FIU registration / consent-artefact details not opened | S5, S33 | HIGH, ZERO | unknown | the build: timeline depends on our FIU status — a named sub-gap |
**Insight:** "AI categorisation" in India means AA-fed categorisation; the Jupiter coverage complaint (S8) is the same constraint seen from the user's side. · **Belief:** unknown · **Also changes:** the spec — data source first, model second.

### 8 · Distribution — where these users can be reached · why: launch only · searched: reddit about.json, Jupiter community
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 8.1 | Subreddit sizes unverified — reddit.com unreachable | S34 | ZERO | unknown | nothing |
| 8.2 | Competitors' own Discourse forums are public and carry the exact users who argue about categories (24-reply threads) | S35 | HIGH | unknown | launch: recruit Kano/interview participants from these rooms (ethically, publicly) |
**Insight:** the research room and the recruiting room are the same — Jupiter's forum. · **Belief:** unknown · **Also changes:** the method (recruiting).

---

## 3 · Verdict

**Rows labelled contradicts / weak confirm / counter-signal / trust / adjacent, listed before judging:** contradicts — S7, S12, S25 (+S24), S27, S28; weak contradicts — S2, S11, S29; weak confirm — S5, S8, S9, S10; counter-signal — S26 (adjacent); adjacent, unknown — S16, S17, S32; trust — S6, S13, S15, S29, S30.

**Belief:** **still unknown — leaning contradicted on "table stakes", untested on "losing users".** Decided by: (1) S12 — the public complaints about an app that has the feature are service and KYC, not insights; (2) S7 + S2 — no PFM app in India's top-10 downloads and the only opened market figure is USD 44.5M software revenue, not a table-stakes category; (3) S25 + S27 — the two best-documented spend-insights leaders (Mint, Walnut) ended as features inside credit businesses. The first half of the belief is not supported by anything opened; the second half ("losing users to apps that have it") rests entirely on S1, which the web cannot supply.
**Falsifier:** **did not fire — and cannot, from the web.** (a) No retention figure for Fi or Jupiter is public (S13, S18, S19 ZERO); Monarch's 20× is subscriber growth, not retention (S26). (b) Requires our churn-reason tags (S1 ASK).
**Contradicting evidence:** S7 (no PFM app in top-10 downloads) · S12 (Jupiter's visible complaints are service/KYC; insights appears once, in a 3★ review) · S25 and S24 (Mint: budgets/custom categories dropped; 3.6M MAU not enough) · S27 (Walnut's growth line is credit customers) · S28 (Money View: 3M downloads on SMS categorisation, then lending) · S2 (IMARC: USD 44.5M, 4.24% CAGR) · S11 (users call the monthly recap "cool", no switching language). Dropped from the verdict: S29 — the "Indians don't want to track expenses" quote is unsourced (ZERO) and convenient; it is not used. Weak confirms held on the other side: S5 (half of AA consents are PFM), S8/S9/S10 (users with the feature demand more of it). Counter-signal: S26 (Monarch, US, adjacent). Trust rows S6, S13, S15, S30 contributed nothing either way.
**Top three, by impact on the goal:**
1. **The retention case for insights is unproven anywhere public.** Users of the apps that have it complain about service, not insights (S12); the pioneers' retention engine became credit (S25, S27). Impact: the round narrative must not rest on "we built table stakes".
2. **Demand is real but shaped: it is a hook, and users want it complete and customisable.** Half of AA consents are PFM (S5); Jupiter users fight for custom categories and cross-account coverage (S8, S9, S10); Monarch's 20× shows the vacuum effect (S26, adjacent). Impact: if built, scope = AA-fed, all-accounts, custom categories, feeding a monetising step — not a checkbox.
3. **The data source sets the build cost, not the AI.** SMS parsing is not Play-approvable for this use (S31, S32); the route is Account Aggregator with FIU status (S5, S33). Impact: the pre-round timeline is an FIU question before it is a model question.
**Next step:** **one named gap** — the share of users churned in the last 90 days whose exit-survey tag or support ticket names spend tracking / insights / categorisation, against the top three exit reasons (S1). Where to look: our own churn survey and support-tag export; if under 10 tagged mentions, run a Kano pair on 100 active users (S21) and 10 story-based churn interviews (S22) before writing a spec. The decision reverses on this number and the map does not have it, so it is not a *decide*.

---

## 4 · Self-check (not a scoreboard)

| Check | Actual value |
|---|---|
| 1 · Ground truth before search | Section 0 written 2026-10-09T07:10:04Z; first search call after it, same minute-plus; all SOURCES rows dated 2026-10-09 after that stamp |
| 2 · Every claim sourced and marked | 35 SOURCES rows; every section-2 finding cites an S# carrying HIGH / MEDIUM / ZERO / NONE / ASK; 0 findings without both |
| 3 · No snippet-sourced HIGH | 18 HIGH rows (S2, S5, S7–S12, S16, S17, S20, S25–S28, S31, S32, S35), each with URL and date read; snippet-only numbers kept at ZERO (S6, S13, S15, S29, S30, S33) |
| 4 · Patterns need three | "insights leaders became credit businesses": S25 + S27 verified, S29 unverified → labelled weak signal. "complaints are service not insights": S12 only (4 reviews) → labelled weak. No unlabelled pattern |
| 5 · Empty angles reported | 8/8 angles present; angle 1 is an ASK row; Reddit lane (S14), G2 (S15), Fi reviews (S13), subreddit sizes (S34) reported as ZERO with what was tried |
| 6 · Every insight states its impact | 8 angle insights, each with Belief and Also changes; 31 finding rows, each with both columns, no dashes |
| 7 · Verdict honest | 21 distinct labelled rows listed before the verdict; section 3 cites every contradicts / weak / counter-signal / trust row by id; one dropped (S29) with the reason |
| 8 · Ends in a step a decision can take | one named gap — the % of 90-day churn naming insights — not "more research" |
| Red flags | no invented source or number; no login or anti-bot bypass (403/410/429 reported as such); Gartner and RedSeer asks answered NONE, not rounded; IMARC and Sahamati are the only market numbers, marked for what they are |
| Unconfirmed drafts to confirm | goal number (S1); the two apps = Fi Money and Jupiter |
