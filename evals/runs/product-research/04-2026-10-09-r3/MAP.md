# Research map — Should we build "spend insights" (AI categorisation + monthly narrative) before the next funding round? — 2026-10-09

## 0 · Ground truth (written 2026-10-09 16:05 IST, before the first search)
**Decision:** Build the spend-insights feature (AI categorisation + monthly narrative) now, before the next funding round — or not now (keep the roadmap slot for other work). Build · not-now.
· **Goal it serves:** *unconfirmed (drafted)* — retention of the ~1.2M MAU base (monthly churn / M1–M3 retention), plus the funding-round story. The size of move that would matter must come from the user's own numbers (ASK, angle 1).
· **Belief:** split into two —
  **B1:** spend insights is table stakes for Indian consumer-finance apps now (most serious competitors ship it).
  **B2:** we are losing users to apps that have it.
· **Falsifier (user's own):** (F1) the apps that have it show no retention gains; (F2) our own users do not mention it when they churn.
· **Already known:** ~1.2M MAU; the user believes two competitor apps already ship the feature — *the two apps are not named in the request; drafted as unconfirmed and identified in angle 2.*
· **Requests carried into the map:** (R1) an Indian personal-finance-app market size from a source leadership accepts (Gartner / RedSeer named); (R2) top user complaints about the two apps, from G2 or app-store reviews, with actual numbers and quotes.
· **Rule stated up front:** the user is presenting this. The map will include what contradicts the belief, in its own place, and every number is marked by how it was verified. A paywalled headline number will not be marked HIGH, and a number not found will be reported as not found, not substituted.

### Search keys (problem phrase + platform + company + angle word), written before searching
- A2: "spend analysis" / "spend insights" / "expense tracker" + India + Jupiter / CRED / INDmoney / Fi / Axio (Walnut) / Paytm / PhonePe + launch / feature / changelog
- A3: "expense tracker" / "categorisation wrong" / "SMS" + reddit r/IndiaInvestments, r/personalfinanceindia + Jupiter / Walnut / Axio; Google Play reviews
- A4: Google Play rating + review count + installs for those apps; GitHub "expense tracker India SMS"
- A5: Kano basic vs performance; JTBD; RICE; North Star; Mom Test on churn reasons
- A6: Mint shutdown; Walnut → Axio pivot; Fi Money shutdown; "spend insights retention" case study
- A7: RBI Account Aggregator framework; SMS-reading permission policy (Google Play); DPDP Act
- A8: personal-finance creators / communities India
- R1: RedSeer / Gartner "personal finance" India market size; "digital lending" / "wealthtech" India market size press release

> **Before you put this on a slide.** You asked for two things you could present. Here is what the evidence supports. (R1) **No Gartner or RedSeer number for Indian personal-finance apps exists in any public source I could reach.** The numbers that do exist size other things, and section 2·R1 says what each one measures. (R2) **G2 does not hold consumer reviews for these apps**, and the Play Store page shows three "most relevant" reviews per app. That is enough for real quotes. It is not enough for a ranked "top complaints" list. The quotes below are verbatim, with dates and helpful counts. A ranked list needs a sample, named as the gap in section 3. The two apps are drafted as **Jupiter** and **axio (formerly Walnut)**, unconfirmed (S3).

## 1 · The map
The feature itself is common. Categorised spends ship in at least four apps with more than 1 crore installs (Jupiter, axio, CRED Money, INDmoney). None of the pages I opened describes an AI-written monthly narrative. What users complain about is not missing insights. It is **wrong or late data** (duplicates, missing transactions, 2–3 day lag, "Miscellaneous"), and on Jupiter, rewards, support and ads. No public source shows a retention gain from spend insights at an Indian app. The cases that come close (Walnut, Fi, Mint, Cleo) say PFM earns money as a wedge into credit or banking, not as a feature people stay for.

| Segment | Their words (verbatim, S#) | What they use today | What is missing | Where they are |
|---|---|---|---|---|
| Neobank users who were offered insights | "I only visit money tab only after an app update" (S10) · "Amazed to see that you people have incorporated weekly as well monthly insights" (S14) | Jupiter Money tab, AA-linked accounts | All-bank coverage ("my other bank i use is not supported", S10), correct exclusions ("Not a spend", S11) | Jupiter community forum; Play reviews |
| SMS-tracker loyalists | "I know this is free app but it was best tracker." (S24) | axio (Walnut), which auto-reads bank SMS | Reliable detection: "captured twice or sometimes even 5 times" (S24); "not automatically detected" (S23) | Play reviews (axio 2.65L reviews, S22) |
| Card-heavy users | featured reviews are about rewards and support; none mention CRED Money (S29) | CRED and CRED Money (S32) | not evidenced | App Store / Play |
| Privacy-first manual trackers *(weak signal, adjacent: HN builders)* | "a privacy-first, manual expense tracker for India" (S34) | Spreadsheets, indie apps | Trust that no loan upsell follows the data | HN Show posts (≤6 pts) |

**Cases to follow:**
- **Walnut → axio.** What they did: built India's best-known SMS expense tracker, then put credit on top of it (Pay Later, personal loans through an RBI NBFC, S43). Good: the tracker still carries 1Cr+ downloads and a 4.5 rating (S22). Bad: tracker quality now draws the 1–2★ reviews (S23–S25). Ugly: insights became a lending funnel. Source: S22, S43.
- **Fi (Epifi).** What they did: a neobank for young users with money-management tools; 3.5M customers. Good: reached scale (S42). Bad: wound down banking on the app in March 2026. Ugly: having the feature did not keep the business. Source: S42.
- **Cleo** *(adjacent, US/UK)*. What they did: a chat-based spending-insights app that monetised on subscriptions plus cash advances. Good: $150M ARR. Bad: fees (cash advance) grew faster than subscriptions, 183% vs 93% (S39). Ugly: the insights brought users in; credit made the money. Source: S39, S40.

## 2 · Angles

### 1 · Goal — ask for our own numbers; the web cannot supply them
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 1.1 | Share of our churners who mention spend tracking, budgeting or a named competitor: not provided | S1 | ASK | unknown | This is falsifier F2 and the number the decision turns on |
| 1.2 | Current M1/M3 retention, and the lift that would justify the slot: not provided | S2 | ASK | unknown | Sets the RICE "impact" bar |
| 1.3 | The two competitor apps: not named | S3 | ASK | unknown | The map drafts Jupiter and axio |
**Insight:** Through *Continuous Discovery Habits* (opportunity solution tree), the outcome is retention and "spend insights" is one solution under an unverified opportunity ("users leave for insights"). The tree predicts we cannot rank this solution until churn interviews surface that opportunity. · **Belief:** unknown · **Also changes:** the next step.

### R1 · Market size for leadership — searched RedSeer, Gartner, then whatever exists
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| R1.1 | No RedSeer figure sizing personal-finance / money-management apps in India | S4, S9 | NONE | unknown | Do not cite RedSeer for this segment |
| R1.2 | No Gartner figure for Indian PFM apps | S5 | NONE | unknown | Do not cite Gartner |
| R1.3 | IMARC: India personal finance *software* market USD 44.5M (2025), forecast USD 65.3M by 2034, 4.24% CAGR. The search snippet gave an older 42.5M/2024 figure | S6 | HIGH | unknown | Small, slow software revenue, consistent with PFM being free and bundled. This undercuts a "big standalone market" slide rather than supporting one |
| R1.4 | RedSeer (2020): Indian wealthtech to reach ~USD 63B by FY25 from USD 20B. Investing platforms, metric undefined, a forecast five years old | S7 | MEDIUM | unknown | The wrong segment for spend insights. Using it for this feature would be an over-claim |
| R1.5 | Forrester (Jan 2024): 82% of metro Indian online adults prefer firms that offer money-management tools (74% in 2022) | S8 | HIGH | confirms (B1) | The most defensible leadership number. It is a stated preference, not usage; *Mom Test* applies |
**Insight:** No accepted analyst source sizes this market. The honest slide is the Forrester preference stat plus your own MAU, not a TAM. *Obviously Awesome* predicts the same: a table-stakes feature does not create a market category, so there is no category to size. · **Belief:** confirms (B1, weakly) · **Also changes:** the funding-round narrative should frame insights as retention or credit infrastructure, not as a TAM.

### 2 · Lay of the land — company pages and launch coverage for Jupiter, CRED, INDmoney, axio, Fi
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 2.1 | CRED Money: spending patterns "by merchant or category" across bank accounts; snippets date the rollout to July 2024 | S32 | HIGH | confirms (B1) | — |
| 2.2 | INDmoney: "a categorised view of your expenses" across banks | S33 | HIGH | confirms (B1) | — |
| 2.3 | Jupiter categorises AA-linked transactions; unclear bank narration ends up "Miscellaneous" (team reply) | S16 | HIGH | confirms (B1) | Accuracy on Indian bank narration is the hard part of the build |
| 2.4 | axio (ex-Walnut): SMS-based auto-tracking, 1Cr+ downloads | S22 | HIGH | confirms (B1) | — |
| 2.5 | None of the opened pages describes an AI-generated monthly *narrative*; all describe categorisation and breakdowns | S16, S32, S33 | HIGH | unknown | The narrative may be the one non-parity part. Untested |
**Insight:** Four independent apps meet the three-source bar, so categorised spends are common. Through Kano, that makes categorisation a **basic** (must-be) attribute: leaving it out can cost you, shipping it earns nothing above parity. The narrative half is unclassified. · **Belief:** confirms (B1) · **Also changes:** scope. Parity categorisation is the floor, and only the narrative could differentiate.

### 3 · The users' words — Jupiter community, Play reviews, HN; Reddit attempted
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 3.1 | Asked by Jupiter staff how often they visit the money tab, a user answered: only after an app update | S10 | HIGH (weak signal, n=1) | contradicts (B2) | Habitual use of insights may be low even where it exists |
| 3.2 | Data-accuracy complaints about the feature itself: 2–3 day sync lag, AA "duplicate transactions and also some missing", axio duplicates ×2–×5, undetected bank SMS, balance not updated | S12, S13, S17, S23, S24, S25 | HIGH | unknown | Pattern (≥3 independent). The build's risk is the data pipeline, not the UI or the AI |
| 3.3 | Categorisation logic complaints: refunds and wallet loads counted as spends; "% of total spends has become repetitive" | S11, S15 | HIGH | unknown | Must-have: exclusions and editable categories |
| 3.4 | Jupiter's three most-helpful Play reviews (60, 393, 38 helpful) are about rewards, support, ads and biometrics. None is about insights | S19, S20, S21 | HIGH (weak signal: 3 reviews, not a sample) | contradicts (B2) | Users seem to judge Jupiter on money and support, not insights |
| 3.5 | Users who do value tracking value it highly: "it was best tracker" (S24); 5★ App Store review praising expense breakdowns (S28) | S24, S28 | HIGH | confirms (B1) | Loyalty follows accuracy |
| 3.6 | HN: Indian expense-tracker posts draw ≤6 points; one pitches "privacy-first, manual" | S34 | HIGH (adjacent: builders, not consumers) | unknown | Weak signal of a privacy segment |
| 3.7 | Reddit archives blocked (429/422); Apple review RSS empty; G2 not verifiable and holds no consumer reviews for these apps | S30, S31, S35 | NONE / ZERO | unknown | The "top complaints" ranking you asked for cannot be built from these lanes |
**Insight:** Through JTBD (*Competing Against Luck*), the job is "know where my money went without doing the work." Users fire trackers over *wrong data*, never over a missing narrative. This agrees with Kano: accuracy is the basic. · **Belief:** contradicts (B2, weak) · **Also changes:** acceptance criteria. Accuracy, dedupe and refund handling come first; the narrative comes second.

### 4 · Offerings, and evidence of use — Play / App Store listings opened; survey data
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 4.1 | Play (en_IN): Jupiter 4.3★ · 6.14L reviews · 1Cr+; axio 4.5★ · 2.65L · 1Cr+; CRED 4.8★ · 29.9L · 5Cr+; INDmoney 4.6★ · 4.62L · 1Cr+ | S18, S22, S26, S27 | HIGH | confirms (B1) | The feature sits in apps 8–40× our MAU in installs (installs ≠ MAU). Usage of the feature itself is not public |
| 4.2 | App Store India: Jupiter 4.7 (54,000 ratings); CRED 4.8 (611k), with no featured review mentioning CRED Money | S28, S29 | HIGH | unknown | — |
| 4.3 | CGAP (Mar 2026): 85% of PFM-app users self-report better money management; daily users report significant improvement more often (25% vs 16%) | S36 | HIGH (self-reported, users-only sample) | unknown | Shows value to the people who stay. Says nothing about retention or switching |
**Insight:** Through *The Mom Test*, every usage signal here is either installs (the whole app) or self-report (S8, S36). None is observed behaviour with the feature, which is what the belief needs. · **Belief:** unknown · **Also changes:** the evidence has to come from our own analytics (S1, S2).

### 5 · Method — the PM canon (never cut)
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 5.1 | **Kano.** Prediction: if spend insights is a basic, churners cite its absence and shipping it restores parity without lifting retention above peers. Evidence: four competitors ship it (2.1–2.4) and complaints are about its *quality* (3.2), which fits a basic. Whether its absence drives our churn is untested | 2.1–2.4, 3.2, S1 | HIGH / ASK | confirms (B1) | Budget it as parity work, not a growth bet |
| 5.2 | **JTBD (*Competing Against Luck*).** Prediction: users switch when a rival does the job ("know where my money went") better. Evidence: firing reasons are accuracy failures (3.2). No source shows anyone switching *to* an app for insights | 3.2, S35 | HIGH / NONE | unknown | Switching interviews would test B2 directly |
| 5.3 | ***The Mom Test*.** Prediction: stated preference (82%, S8) overstates real behaviour. Evidence: the one behavioural answer we have (S10) is "only after an app update" | S8, S10 | HIGH | contradicts (B2) | Ask churners about past behaviour, not wishes |
| 5.4 | **RICE.** Reach is high (1.2M MAU). Impact is unknown (no retention data, F1 untested). Confidence is low (no own churn data). Effort is high (the accuracy pipeline, 3.2). Prediction: low priority until Confidence rises | S1, S2, 3.2 | ASK | unknown | One number (S1) moves Confidence most |
| 5.5 | ***Escaping the Build Trap* (Perri).** Prediction: a feature built for the funding-round story, before the outcome is evidenced, ships output without outcome. Evidence: the decision is timed to the round, not to a retention finding | §0 | ASK | unknown | Reframe as "prove retention, then build" |
| 5.6 | ***Obviously Awesome* (Dunford).** Prediction: parity features do not position you; only the unique attribute (here maybe the narrative) can. Evidence: no competitor page shows a narrative (2.5) | 2.5 | HIGH | unknown | If built, lead with the narrative, not categorisation |
**Insight:** The canon agrees: categorisation is a Kano basic (B1 holds), and the claim that it drives switching (B2) has no behavioural evidence. · **Belief:** confirms (B1) · unknown (B2) · **Also changes:** priority depends on S1.

### 6 · Cases — good, bad, ugly
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 6.1 | Walnut's maker now facilitates NBFC credit, Pay Later and personal loans through the tracker app | S43 | HIGH | unknown | The money in insights is credit, not the feature |
| 6.2 | Fi: money-management neobank, 3.5M customers, wound down banking on its app in Mar 2026 | S42 | HIGH | contradicts (B2) | Having the feature did not keep the business |
| 6.3 | Mint: 3.6M active users (2021), shut down | S41 | HIGH (adjacent, US) | contradicts (B2) | Engagement was not enough for a free PFM product to survive |
| 6.4 | Jax: "Dozens of startups have failed…"; PFM retention compared to gym membership; works when bundled with habits and lending | S40 | HIGH (adjacent) | contradicts (B2) | Bundle with something users already transact on |
| 6.5 | WeMoney (Australia): goal-setting in the first 3 days of onboarding is linked to higher 12-month retention; +20% retention after moving it into onboarding | S38 | HIGH (adjacent; goals, not insights) | confirms (B2) | If built, attach a goal or action to the narrative |
| 6.6 | Cleo: 41% of revenue from fees; cash advances grew 183% vs 93% for subscriptions | S39 | HIGH (adjacent) | unknown | The insights layer brings users in; credit pays |
| 6.7 | "69% renewal among analytics-screen visitors" (The Budgeting App): could not verify on the page | S37 | ZERO | unknown | Excluded |
**Insight:** Through *Crossing the Chasm*, PFM insights reach early adopters (Mint 3.6M, Fi 3.5M) and then stall unless they become part of a whole product (credit, banking). The cases agree. · **Belief:** contradicts (B2) · **Also changes:** if built, design it as the top of a credit or goals funnel.

### 7 · Constraints — Play policy, the AA ecosystem
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 7.1 | Google Play permits READ_SMS for "SMS-based money management" with a Permissions Declaration Form. The dev.to claim that it does not qualify was not verified, and the official page contradicts it | S44, S45 | HIGH / ZERO | unknown | The SMS route is open, with a declaration risk |
| 7.2 | AA ecosystem (June 2026): 17 operational AAs, 1,076 FIUs, "295m +" monthly data shares. The page's two sets of totals do not reconcile | S46 | HIGH | unknown | The AA route exists, but users report AA duplicates and missing data (S17) |
| 7.3 | DPDP Act consent requirements for financial data: **not searched in this run** | — | NONE | unknown | Check before the spec |
**Insight:** The constraint is not access, since both SMS and AA are permitted. It is data quality from those sources (3.2). Kano again: the basic fails on the pipe. · **Belief:** unknown · **Also changes:** effort estimate goes up.

### 8 · Distribution — in-app to existing MAU
| # | Finding | Source | Mark | Belief: confirms · contradicts · unknown | Also changes |
|---:|---|---|:--:|---|---|
| 8.1 | Distribution for a retention feature is our own 1.2M MAU. External channels (PF newsletters) were found with no audience numbers | S47 | NONE | unknown | No external channel work is needed for this decision |
**Insight:** Through North Star thinking, the measure is the share of MAU that opens the monthly narrative and comes back, not reach. · **Belief:** unknown · **Also changes:** instrument a fake-door or a narrative email first.

## 3 · Verdict
**Rows labelled *contradicts* in section 2:** 3.1, 3.4, 5.3, 6.2, 6.3, 6.4. Rows labelled *confirms* (B2): 6.5.

**Belief:** **B1 confirmed. B2 unknown**, with the weak signals pointing against it. B1 rests on four independent apps shipping categorised spends (2.1–2.4), the Forrester 82% preference (R1.5), and Kano's reading of quality complaints (5.1). B2 has no direct evidence either way: no source shows users switching *to* an app for insights, and every behavioural signal is weak.
**Falsifier:** **did not fire, and was not tested.** F1: no Indian retention data exists publicly. The adjacent data is mixed: 6.5 for, 6.2–6.4 against. F2 lives only in your churn data (S1).
**Contradicting evidence:** 3.1 (a user opens the money tab only after updates), 3.4 (Jupiter's most-helpful reviews never mention insights, only 3 reviews), 5.3 (stated preference vs behaviour), 6.2 (Fi folded despite money tools), 6.3 (Mint shut down with 3.6M users, adjacent), 6.4 (PFM retention "like gym membership", adjacent). The one confirming row for B2, 6.5 (WeMoney +20% retention), is adjacent and about goals, not insights. None dropped.
**Top three, by impact on the goal:**
1. **Accuracy is the feature.** Every complaint about competitors' insights is about wrong, late or duplicated data (3.2). If you build, the AI narrative is worth nothing on top of a bad pipeline.
2. **Insights pays as a wedge, not a product.** Walnut→credit, Cleo→cash advances, Fi and Mint gone (6.1–6.6). For the funding story, frame it as retention or credit infrastructure.
3. **There is no credible TAM to present.** No public RedSeer or Gartner figure exists. IMARC's USD 44.5M sizes software revenue, and RedSeer's USD 63B is wealthtech from 2020. Put Forrester's 82% (S8) and your own MAU on the slide instead.
**Next step:** **one named gap: the share of our churned users (last 3–6 months) whose exit feedback mentions spend tracking, budgeting or a named competitor (S1).** It comes from exit surveys, uninstall feedback and support tickets, plus five switching interviews (*Mom Test*: "what were you using the week you left?"). If that share is material, B2 holds and the build case is a spec. If it is near zero, F2 fires and the slot goes to the alternative. For the deck's "top complaints", the same gap applies: a ranked list needs a coded sample of ≥300 recent Play reviews per app, which this run did not have.

## 4 · Self-check (not a scoreboard)
| Check | Actual value |
|---|---|
| 1 Ground truth before search | Section 0 written 2026-10-09 16:05 IST, before the first search; written to disk before S4 |
| 2 Every claim sourced and marked | 47 SOURCES rows: HIGH 34 · MEDIUM 1 · ZERO 3 · NONE 6 · ASK 3; every section-2 row cites an S# or a section-2 row |
| 3 No snippet-sourced HIGH | Every HIGH row has a URL and date read 2026-10-09. Snippet-only claims (S31, S37, S45) are ZERO. Play quotes were parsed from raw page HTML; Jupiter forum quotes were rechecked against the Discourse JSON |
| 4 Patterns need three | "Categorisation is common": 4 sources (2.1–2.4). "Data accuracy is the top complaint": 6 sources (3.2). Single-source claims are marked weak signal (3.1, 3.4) |
| 5 Empty angles reported | R1 Gartner/RedSeer NONE (S4, S5, S9); Reddit NONE (S35); RSS NONE (S30); distribution NONE (S47); DPDP not searched (7.3) |
| 6 Every insight states its impact | 10 insights, each with Belief and Also changes |
| 7 Verdict honest | 6 contradicts rows listed, 6 cited; 1 B2-confirm cited |
| 8 Ends in a decision step | One named gap: churn-mention share (S1) |
| 9 PM canon | 9 named (Kano, JTBD, Mom Test, RICE, Escaping the Build Trap, Obviously Awesome, Crossing the Chasm, OST, North Star), each with a prediction and an evidence check |
