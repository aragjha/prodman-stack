# Research map — Should a 1.2M-MAU Indian consumer fintech build "spend insights" (AI categorisation + monthly narrative) before the next funding round? — 2026-10-09

## 0 · Ground truth (written 2026-10-09 19:35:37 IST, before the first search)

| Field | What it says |
|---|---|
| **Decision** | Build vs. not-build (now) — whether "spend insights" (AI categorisation + monthly narrative) takes the build slot before the next funding round, versus whatever else holds that slot (the alternative was not named — *unconfirmed*). |
| **Goal it serves** | Not stated. Drafted, *unconfirmed*: 30/90-day retention (the belief is about losing users), and secondarily the funding-round story. The size of move that would matter is the user's number to give (ASK). |
| **Belief** | **B1:** The PM believes spend insights is now table stakes among Indian personal-finance apps (users expect it as a basic). **B2:** The PM believes the company is losing users to apps that have spend insights. |
| **Falsifier** | (user's, confirmed) B1/B2 drop if the apps that have it show no retention gains from it, **or** if the company's own churned users do not mention it when they churn. Added (*unconfirmed*): B1 also drops if public reviews of apps with the feature show users treating it as broken/indifferent rather than as a reason to stay. |
| **Already known** | The user's own framing only. Two named asks: (a) Indian personal-finance-app market size from Gartner or RedSeer; (b) top user complaints about "the two apps that already have this feature" from G2 or app-store reviews. The two apps were **not named** — drafted from the search, *unconfirmed*. |

**Note on the two asks (said up front, per the skill):** the market-size number will be reported at whatever mark it actually earns — a paywalled Gartner/RedSeer figure seen only via a press release or article is MEDIUM, a headline seen only as a snippet is ZERO, and nothing is rounded up because it is going on a slide. G2 is a B2B-software review site and sits behind an anti-bot wall; consumer Indian fintech apps are reviewed on Google Play / App Store, so complaints come from public review pages only, and only quotes actually read on a page are marked HIGH. The map will contain what contradicts the belief, in its own section.

### Angle map and search keys (all 8 kept; angle 1 is ASK-only)
| # | Angle | Keys — contradicting first |
|---:|---|---|
| 1 | Goal | ASK: current D30/D90 retention, churn-survey reasons, what move would matter |
| 2 | Lay of the land | "Fi Money shut down", "Walnut Axio pivot", "Jupiter money insights", "spend analysis UPI app India" |
| 3 | Users' words | "spend tracking app categorisation wrong India review", HN "expense categorization useless", reddit IndiaInvestments "expense tracker" |
| 4 | Offerings + use | Play Store installs/ratings for Axio, Jupiter, CRED, INDmoney, Fi; GitHub open-source Indian SMS expense parsers |
| 5 | Method | JTBD, Kano, Escaping the Build Trap, Cagan four risks, Lean, Mom Test |
| 6 | Cases | "Fi money shutting down", "Mint shut down Intuit", "personal finance app retention insights study" |
| 7 | Constraints | RBI Account Aggregator framework, DPDP Act 2023, SMS-read permission Google Play policy |
| 8 | Distribution | r/IndiaInvestments, r/personalfinanceindia, finance YouTube India |

> All 8 angles kept: none could be cut without losing a limb of the falsifier. Angle 1 is ASK-only (your numbers, not the web's). Everything below was read 2026-10-09; sources in `SOURCES.md`.

## 1 · The map

| Segment | Their words (verbatim, S#) | What they use today | What is missing | Where they are |
|---|---|---|---|---|
| Dedicated trackers (axio-style, SMS-read) | "…Almost all online transactions are captured twice or sometimes even 5 times…" (S10); "…My recent transactions or spending from a specific bank is not automatically detected…" (S11) | axio (1Cr+ installs, S9), Cashew, Money Manager, Fold (S19) | Accuracy: complete and de-duplicated capture | Play Store reviews, r/personalfinanceindia |
| Neobank / payments-app users (Jupiter-style) | "…I only visit money tab only after an app update…" (S16); top complaints are rewards and support (S13, S14), not insights | the app's own spends tab; Google Pay now ships a Gemini spend breakdown free (S7, S8) | Custom categories, correct totals (S17, S18) | Jupiter community forum, App Store / Play |
| Non-trackers | "No tracking. I hate doing it and what it does to me." (S19); "A spreadsheet" is the top answer (S19) | Excel / Google Sheets, or nothing | Not obviously a feature — a reason to care | r/personalfinanceindia |

**Cases to follow:**
- **Google Pay — Ask Google Pay (Jul 2026):** shipped AI categorisation + spend breakdown + cut-back suggestions in 10 Indian languages. Good: sits where UPI data already is. Bad: commoditises the feature you would build. Ugly: no usage data published. (S7, S8)
- **axio (ex-Walnut):** SMS tracker at 1Cr+ installs that pays its bills with Pay Later, loans and FDs. Good: shows the feature gets usage at scale. Bad: complaints are all about accuracy. Ugly: the tracker is the way in, credit is what pays. (S9–S12)
- **Fi Money:** neobank with money-management tools for young users, 3.5M customers; banking wound down in 2026 after non-lending products didn't monetise. Good: real reach. Bad: having the features did not keep the business alive. (S20–S22)

## 2 · Angles

### 1 Goal — ask, never the web's · why: the falsifier's second limb is your own churn data
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 1.1 | Your D30/D90 retention, what churned users say, and the retention move that would justify the build: not given | S1 | ASK | unknown (B1, B2) | Next step: this is the number the decision turns on |
| 1.2 | "The two apps that already have this feature" were not named; drafted as Jupiter and axio | S2 | ASK | unknown (B2) | Swap if wrong; the complaint rows (3.x) change |

**Insight:** Through **North Star / input metrics**, the input this feature has to move is retention of active users. No public source can tell you whether your users want it. · **Belief:** unknown · **Also changes:** the next step.

### 2 Lay of the land — market-size reports, platform launches · why: you asked for a number leadership will accept
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 2.1 | No public Gartner or RedSeer market size for Indian personal-finance apps | S3 | NONE | unknown (B1) | The slide you asked for can't be filled honestly as specified |
| 2.2 | The only RedSeer figure is "$60B wealthtech by FY25" — a 2020 forecast for a different category (investing), page 403, not read | S4 | ZERO | unknown (B1) | Don't use it: wrong category, out of date, unread |
| 2.3 | IMARC: India personal-finance *software* was USD 44.5M in 2025 and is forecast at USD 65.3M by 2034 (4.24% CAGR) | S5 | HIGH | unknown (B1) | Spend insights is a feature, not a market you can sell into. A tiny software market is no case for the round |
| 2.4 | India: 1.7B finance-app downloads (Sensor Tower, via The CapTable) | S6 | MEDIUM | unknown (B1) | A credible context number for the slide, marked secondary |
| 2.5 | Google Pay is rolling out a Gemini assistant that categorises spending and suggests cuts (Jul 2026) | S7, S8 | HIGH | confirms (B1) | Positioning: the feature is now free inside the largest UPI app, so it can't be your differentiator |

**Insight:** Through **Obviously Awesome**, the alternative a user compares you with is now Google Pay's free version, not "no insights". Only an attribute GPay lacks (accuracy across your own products, actions tied to your offers) makes your version worth anything. · **Belief:** confirms B1 on supply only · **Also changes:** the positioning, and the market-size slide.

### 3 Users' words — Play/App Store reviews, Jupiter forum (Discourse JSON), Reddit archive API, HN Algolia · contradicting keys run first
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 3.1 | axio's most-helpful Play reviews complain about accuracy: duplicate captures, missed transactions, wrong balances | S10, S11, S12 | HIGH | confirms (B1) | Weak signal (3 reviews). Build: accuracy is the bar, and a broken version costs you |
| 3.2 | Jupiter's most-helpful Play reviews are about rewards and support, not insights (393 and 60 found helpful) | S13, S14 | HIGH | contradicts (B2) | The app "with it" loses users over other things |
| 3.3 | Own count of 100 recent Jupiter App Store reviews: support 22 · fees/rewards 20 · loan/credit 11 · freeze/KYC 7 · tracking/insights 2, both positive | S15 | MEDIUM | contradicts (B1) | Weak signal: one app, one feed. Insights barely come up |
| 3.4 | Jupiter forum user: visits the money tab "only after an app update"; uses a separate app for insights | S16 | HIGH | contradicts (B1) | Kano read: indifferent for this user |
| 3.5 | Jupiter users ask for custom categories "to make insights actually insightful" and report wrong category totals | S17, S18 | HIGH | unknown (B1) | Build: custom categories plus correct totals are the floor |
| 3.6 | r/personalfinanceindia "which tracker do you use": top answer "A spreadsheet" (13), then "No tracking. I hate doing it" (8); no neobank or payments app named | S19 | HIGH | contradicts (B1) | Weak signal (one thread). JTBD: the competitor is a spreadsheet or nothing |
| 3.7 | Forrester 2019 survey of 3,000 Indian online adults: the top stated reason to switch provider is "the ability to manage financial well-being better" | S29 | HIGH | confirms (B2) | Weak: stated preference, 2019, about banks, and not specific to spend insights |
| 3.8 | No public evidence of Indian users leaving an app *for* spend insights | S30 | NONE | unknown (B2) | B2 can only be tested with your own churn data |
| 3.9 | G2: not applicable (B2B review site; consumer apps not meaningfully listed; anti-bot wall not bypassed) | S34 | NONE | unknown (B2) | Use Play/App Store, as here |

**Insight:** Through **JTBD**, the job is "know where my money went without the effort". The people who hire for it pick a dedicated tracker or a spreadsheet, and many fire the job entirely. Users of an app that already has the feature barely mention it. · **Belief:** contradicts B1 (demand side) · **Also changes:** the build. If you build, accuracy and custom categories are the minimum.

### 4 Offerings and evidence of use — Play listings, install counts, changelogs
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 4.1 | axio: SMS-based tracker, 1Cr+ installs, 2.65L reviews, 4.5★; the same listing sells Pay Later, loans (14–35% p.a.) and FDs | S9 | HIGH | confirms (B1) | Business model: tracking is how users come in, credit is what pays |
| 4.2 | Jupiter has shipped spends tracking since Feb 2023 (pie chart, categories) | S16, S17 | HIGH | confirms (B1) | — |
| 4.3 | Google Pay's AI spend assistant (see 2.5) | S7 | HIGH | confirms (B1) | — |

**Insight:** Through **Kano**, competitor presence says nothing about whether the feature is a basic. Kano is measured from customers' answers, and the customer-side evidence is in angle 3. · **Belief:** confirms B1 on supply · **Also changes:** method. Run a Kano survey with your users before you claim "table stakes" in the deck.

### 5 Method — the PM canon (never cut)
| Framework | What it predicts here | What the evidence says | Agrees / disagrees |
|---|---|---|---|
| **Kano** | If it's a basic, your users feel its absence and its presence earns nothing; if indifferent, nobody notices either way | Supply side: everyone has it (2.5, 4.1–4.3). Demand side: barely mentioned, the tab goes unvisited, spreadsheets win (3.3, 3.4, 3.6). No customer Kano data exists | Disagrees with "table stakes" as stated. Unknown until your users answer the functional/dysfunctional pair |
| **JTBD** (*Competing Against Luck*) | You win only if you beat what users hire now: spreadsheet, dedicated tracker, GPay, or nothing | 3.6 (spreadsheet, nothing), 2.5 (GPay free), 4.1 (axio) | Disagrees: a generic version loses to free or familiar |
| **Escaping the Build Trap** (Perri) | A build timed for "before the round" is driven by a deadline story, not an outcome | The brief names the round as the timing, and gives no retention target | Disagrees: the decision has no outcome number yet (1.1) |
| **Four big risks** (Cagan, *Inspired*) | Value risk is the one not yet retired; feasibility is mostly retired | Value: unknown (3.x). Feasibility: Play allows SMS-based money management (7.1), axio proves it at scale (4.1) | Agrees: value risk is open |
| **Lean / Build-Measure-Learn** + **Mom Test** | The cheapest test of the riskiest assumption comes before a full build: ask churned users about past behaviour, not "would you use insights?" | — (your data) | Sets the next step |

**Insight:** Every framework points the same way. The feature is supply-side table stakes and demand-side unproven, and the one test that would settle it uses your data, not the web's. · **Belief:** contradicts B1 as stated · **Also changes:** the next step.

### 6 Cases — good, bad, ugly · contradicting keys first ("shut down", "nobody used", "low engagement")
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 6.1 | Fi Money: money-management tools for young users, 3.5M customers; banking discontinued in 2026; "weak monetisation across non-lending products" | S20, S21, S22 | HIGH | contradicts (B2) | Weak: Fi failed for business reasons, but having the features did not decide the outcome |
| 6.2 | European bankers (Forrester for Personetics): 77% say fewer than half their customers use money-management tools | S23 | MEDIUM | contradicts (B1) | Adjacent (Europe, vendor-commissioned) |
| 6.3 | Bud/Jaja (UK): +18% daily sessions among users of the feature, 17% repeat visits; **no retention number** | S24, S25 | MEDIUM | unknown (B1) | Adjacent vendor case. The falsifier's first limb can't be tested from it |
| 6.4 | CGAP India (n=274 PFM users, 2025): self-reported benefit; frequency is associated with outcomes | S26 | HIGH | unknown (B1) | Correlational, self-reported; says nothing about retention |
| 6.5 | No public before/after retention number for any app that added spend insights | S27 | NONE | unknown (B1, B2) | The falsifier's first limb is untestable from public data |
| 6.6 | Mint shutdown; JPMorgan Finn (47k accounts) | S28, S35 | ZERO | unknown | Not opened; not used |

**Insight:** Through **Crossing the Chasm**, the vendor and survey cases show early adopters engaging (S24, S26). The pragmatist majority mostly doesn't (S23). Nothing public ties the feature to retention. · **Belief:** contradicts (weak) · **Also changes:** don't put "insights lift retention" on a slide. No public source supports it.

### 7 Constraints — Google Play policy, DPDP
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 7.1 | Google Play allows SMS read for "SMS-based money management" (budget tracking), via a restricted-permission declaration | S31 | HIGH | unknown | Feasible on Android. iOS can't read SMS, so cover it with your own transactions or the Account Aggregator framework (not researched) |
| 7.2 | DPDP Rules notified 13 Nov 2025; the substantive obligations and penalties apply from 14 May 2027 | S32, S33 | MEDIUM | unknown | Build: purpose-specific consent for categorising transaction data must ship with the feature |

**Insight:** Through **Cagan's feasibility risk**, the constraints are manageable rather than blocking. They add cost (declaration, consent flows) to a feature whose value is unproven. · **Belief:** unknown · **Also changes:** effort in any RICE score.

### 8 Distribution — where to reach and test with these users
| # | Finding | Source | Mark | Belief | Also changes |
|---:|---|---|:--:|---|---|
| 8.1 | r/personalfinanceindia and the Jupiter community forum are where Indian users openly compare trackers | S19, S16 | HIGH | unknown | Recruit Mom-Test interviewees here only if your own churned users are too few |

**Insight:** Through **The Mom Test**, the right room is your own churned users first. Public rooms are a fallback. · **Belief:** unknown · **Also changes:** nothing in the decision.

## 3 · Verdict

**Rows labelled *contradicts* in section 2 (listed before judging):** 3.2, 3.3, 3.4, 3.6, 6.1, 6.2. Text sweep: 3.1 (confirms, but the build cost rises), 2.5 (confirms supply, but kills differentiation) and 6.3/6.5 (no retention number exists) all complicate the belief. Their labels are kept, and they are cited below.

**Belief:** **B1 contradicted as stated; B2 still unknown.** B1 holds on supply only: Google Pay, Jupiter and axio all ship it (2.5, 4.1, 4.2). On demand, users of an app that has it barely mention it (3.3, 3.4), and the commonest Indian answer is a spreadsheet or no tracking (3.6). Kano can't be read from competitor counts. B2 has no public evidence for or against (3.8). It lives in your churn data.
**Falsifier:** **did not fire, and can't fire from public data.** Limb 1 (retention gains in apps with it): no public number exists (6.3, 6.5, S27 NONE). Limb 2 (your churned users mention it): ASK (1.1).
**Contradicting evidence:** 3.2 (Jupiter loses users over rewards and support), 3.3 (2/100 reviews mention tracking), 3.4 (money tab visited only after updates), 3.6 (spreadsheet or no tracking wins; weak), 6.1 (Fi had the tools and still failed; weak), 6.2 (most bank customers don't use PFM; adjacent). Also complicating: 2.5 (GPay gives it away free), 3.1 (a broken version is punished).
**Top three, by impact on the goal (retention):**
1. No public source links spend insights to retention (6.3, 6.5). The deck can't claim it, and only your churn data can show it.
2. Google Pay now ships AI spend breakdowns free (2.5). A generic version is parity at best, and the edge must come from something GPay lacks.
3. Where the feature exists, the complaints are about accuracy (3.1, 3.5). A half-accurate v1 costs trust in a finance app.
**Dropped:** none.
**Next step:** one named gap — the share of your last-90-day churned users who mention spend tracking or insights (exit survey, support tickets, or 10 Mom-Test calls), and the app they moved to.
**Other gaps — not needed for this decision:** a Kano survey of active users; Account Aggregator coverage for iOS; build cost (for RICE against the alternative, which was not named); whether a Gartner/RedSeer PF-app number exists behind a paywall (would need a subscription — not bypassed).

## 4 · Self-check (not a scoreboard)
| Check | Actual value |
|---|---|
| 1 Ground truth before search | §0 written 2026-10-09 19:35:37 IST, before the first search (all SOURCES rows are later) |
| 2 Every claim sourced and marked | 35 SOURCES rows; every §2 row cites an S# with HIGH/MEDIUM/ZERO/NONE/ASK |
| 3 No snippet-sourced HIGH | 19 HIGH rows, each with a URL and a 2026-10-09 read date; snippets only (S4, S28, S35) marked ZERO |
| 4 Patterns need three | No "common/trend" claim made. 3.1, 3.3, 3.6 and 6.1 labelled weak signal; 6.2–6.3 labelled adjacent |
| 5 Empty angles reported | No angle empty; the NONE rows show their searches (S3, S27, S30, S34) |
| 6 Every insight states impact | 8/8 angle insights carry Belief + Also changes |
| 7 Verdict honest | 6 rows labelled contradicts in §2; 6 cited in §3; Dropped: none |
| 8 Ends in a step | one named gap — churned-user mention rate |
| 9 PM canon | Angle 5 present: Kano, JTBD, Escaping the Build Trap, Cagan four risks, Lean + Mom Test, each with a prediction and agrees/disagrees |
| verify_quotes.py | Run 3 times. Final: 25 quotes OK; 1 UNREACHABLE (S19, the Reddit archive JSON API it was read from, which was OK on the previous run) → kept HIGH under the API-endpoint rule. Earlier fixes: 12 CUT → "…" added; S15 MISMATCH (Apple RSS rotates content) → downgraded to MEDIUM, quotation marks dropped; S16/S17 UNREACHABLE → re-pointed to Discourse JSON endpoints, now OK. Output in `run-04/verify-output.txt` |
