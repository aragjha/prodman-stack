# Research map — Should we build "spend insights" (AI categorisation + monthly narrative) before the next round? — 2026-10-09

## 0 · Ground truth (written 2026-10-09T04:18:22Z, before the first search)

| Field | Value |
|---|---|
| **Decision** | Build "spend insights" (AI categorisation + monthly narrative) before the next funding round — or not. The alternative use of the slot was not named; the map treats it as "the roadmap item this displaces". |
| **Goal it serves** | **Not supplied.** The belief ("losing users") implies **retention / churn** on the ~1.2M MAU base. Angle 1 asks for the number; the web's numbers are never substituted for it. |
| **Belief** | Spend insights is table stakes in Indian consumer fintech now, and we are losing users to apps that have it. |
| **Falsifier** | (a) The apps that have it show no retention gain from it; **or** (b) our own churned users do not mention it. |
| **Already known** | Nothing supplied. |

**Two things asked for by name:** (1) Indian personal-finance-app market size, a number leadership will accept (Gartner / RedSeer named). (2) Top user complaints about "the two apps that already have this feature", from G2 or app-store reviews, verbatim. The two apps were not named; this run assumes **Fi Money** and **Jupiter** (the two Indian consumer apps whose spend-insights feature is a headline feature and has a public review base). If leadership means two other apps, say which and the angle re-runs in an hour. G2 note: consumer apps are effectively absent from G2 (a B2B review site); app stores are the honest source.

**"I'm presenting these":** the map will contain what contradicts the belief, in its own section of the verdict. What goes on the slide is yours to choose; the map stays complete.

### The angle map and search keys (written before searching — cut what does not bear on the decision)

| # | Angle | Run? | Keys |
|---:|---|---|---|
| 1 | Goal | ask | Your own: D30/D90 retention, monthly churn, churn-survey/exit-reason tags, feature-adoption of anything insight-like already shipped |
| 2 | Lay of the land | full | `spend insights` `Fi Money` `Jupiter` `CRED` `Walnut` `Axio` `Money View` + `India` + `launch` / `pricing` / `changelog` |
| 3 | Users' words | full | `expense tracker India` `categorisation wrong` `spend insights useless` on Reddit archive (r/personalfinanceindia, r/IndiaInvestments), HN Algolia, app stores (Fi, Jupiter) |
| 4 | Offerings + evidence of use | full | Play/App Store ratings + counts for Fi, Jupiter, Walnut, Axio; GitHub `Firefly III` `Actual Budget` stars + last commit; Account Aggregator (Sahamati) usage stats |
| 5 | Method | light | Kano "must-be" features; *The Mom Test*; *Continuous Discovery Habits*; *Inspired* (four risks) — chapter cited |
| 6 | Cases | full | `Mint shutdown` `Walnut app discontinued` `Money View pivot` `Fi Money layoffs` `Jupiter insights retention` |
| 7 | Constraints | full | Google Play SMS/Call-log permission policy; RBI Account Aggregator; DPDP Act 2023; RBI digital-lending rules |
| 8 | Distribution | light | the rooms from angle 3, fintech-India newsletters, the repos they star |
| M | Market size (asked) | full | `RedSeer personal finance app India` `RedSeer fintech India report` `Gartner personal finance app India` `Statista personal finance India` + own arithmetic from NPCI / Sahamati open data |
| C | Complaints (asked) | full | App Store customer-reviews public RSS for Fi and Jupiter; Play Store pages; `site:quora.com` |

(First `SOURCES.md` row was read ~04:20Z, after this block.)

---

## 1 · The map

Everything found around the question, on one screen. S# = row in `SOURCES.md`.

| Segment | Their words (verbatim, S#) | What they use today | What is missing | Where they are |
|---|---|---|---|---|
| **Neobank-app users (Jupiter, Fi)** — the two apps that have the feature | On leaving: "my account was frozen unexpectedly...I have now changed my salary account to another bank and closed my Fi account." (S12) · "when you try to exit and close the account they put on more charges and trap you" (S19) · "no proper way to reach a real support agent" (S19). On the feature: "The donut looks dope" / "I am unable to view the insights at all" (S1). **0 of ~70 verbatim complaints across S12, S19, S20 mention insights or categorisation.** | Jupiter "Insights" pie chart + tags (since Feb 2023, S1); Fi "Ask.Fi" categorised search (Apr 2024, S7) | Reliability, human support, fee transparency, clean exit. Not insights. | App Store reviews (S19), Desidime (S12), Trustpilot (S20), community.jupiter.money (S1) |
| **Feature-engaged users** (the ones who do care) | "category-level trend graphs showing spending increases over time" (10 likes, S1) · "monthly email alerts comparing spend habits month-to-month" (S1) | Jupiter's pie chart | Trends over time, a monthly comparison — i.e. the *narrative* half of your spec | community.jupiter.money (S1) |
| **AA-consenting PFM users** | "Over 25% of respondents reported using a consent-based process to share data with PFM apps" · "86% … reported a positive experience" (S17) | PFM via RIAs and banks on Account Aggregator rails; "almost half" of SEBI-FIU consents go to PFM (S16) | A ₹ market number — none in the open (Z1, Z2) | Inside FIUs; 310M+ accounts linked (S8) |
| **SMS-parser builders** (*adjacent*: developers) | "my use case (reading SMS for financial data) doesn't qualify for the exceptions" (S3) | Walnut's old route (7M downloads by 2018, S4), now small indie apps | A reliable Play-Store permission path; policy text says budget apps are allowed (S2), practice says rejected (S3) | dev.to, Product Hunt (not opened) |
| **Self-hosters** (*adjacent*: global OSS) | Firefly III: "No AI, no cloud and privacy-friendly" (S25) | Firefly III 24.8k★, Actual 29.4k★ (S25, S26) | Nothing for you; a privacy-first counter-signal | GitHub |

**Cases to follow:**

| Case | What they did | Good | Bad | Ugly | Source |
|---|---|---|---|---|---|
| **Jupiter Insights revamp (2023)** | Pie chart + recommendations, phased rollout | Praised on launch; the asks were for trends and monthly comparison | Loading bugs on day one | No usage or retention figure ever published; three years on, reviews do not mention it | S1, S11, S19 |
| **Fi Money** | Ask.Fi categorised search (2024) alongside cards, MF, US stocks, rewards | Shipped a genuinely richer insights tool than a pie chart | "phased out a few features that didn't meet our benchmarks for engagement or monetisation" — unnamed | Runway 18 → 10 months; pivot to B2B; users left over freezes, refunds, AMB tracker — not over features | S7, S9, S10, S12 |
| **Walnut → Axio** | SMS-parsed expense tracker, 7M downloads | Proved distribution for the category in India | Monetised only by becoming a lender ($30M deal) | Standalone PFM app gone | S4 |
| **Mint** (*adjacent*, US) | Free PFM at scale, ad/referral model | Category-defining | "not financially viable" | Shut 2024-03-23 | S13 |

---

## 2 · Angles

### Angle 1 — Goal · not searched, by design · your own numbers
**Nothing found — not searched.** The web's numbers are never substituted for yours. The decision needs three of your own: monthly churn on the 1.2M MAU base; the share of exit-survey / support-ticket / app-store text that names spend tracking or insights; and whether anything insight-like you already ship (a transaction list, a balance view) shows D30 lift. Without these, Angle 1 and falsifier (b) stay *unknown*.

### Angle 2 — Lay of the land · company sites, community forum, press · keys: `Fi Money insights` `Jupiter insights` `Walnut Axio` `account aggregator PFM`
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| 2.1 | Jupiter shipped "Insights" (pie chart + "recommendations") on 2023-02-14, phased rollout | S1 | HIGH | **confirms** "they have it" |
| 2.2 | Fi shipped Ask.Fi — categorised, filterable spend search — 2024-04-24 | S7 | HIGH | **confirms** "they have it" |
| 2.3 | Neither company has published adoption or retention numbers for the feature | S1, S7, S9, S10, S11 | HIGH (absence in opened pages) | **unknown** on "losing users to it" |
| 2.4 | Walnut, the category's original Indian winner (7M downloads), survived only as a lender's acquisition | S4 | HIGH | **contradicts** "table stakes" as a standalone retention driver — weak signal (one case) |
| 2.5 | Consent rails exist at scale: 500M consents, 310M+ accounts linked | S8 | HIGH | **unknown** — lowers build cost, says nothing about demand |
**Insight:** Both named competitors have had the feature for 18–30 months and neither has shown it moves anything. · **Impact:** confirms the premise ("they have it"), leaves the conclusion ("we lose users to it") unknown.

### Angle 3 — The users' words · verbatim only · keys: `expense tracker` `categorisation` `insights` on App Store RSS, Desidime, Trustpilot, Jupiter community, HN Algolia; Reddit archive and Quora attempted
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| 3.1 | ~50 most-recent Jupiter App Store reviews: 0 mention insights/categorisation; complaints are support, freezes/liens, hidden fees, blocked account closure, KYC/login, CIBIL misreporting, loan spam | S19 | HIGH | **contradicts** "table stakes" (Kano: a must-be shows up as dissatisfaction when poor — it does not show up at all) |
| 3.2 | 15 Desidime replies on leaving Fi: freezes, failed refunds, "AMB tracker"; 0 mention insights | S12 | HIGH | **contradicts** |
| 3.3 | 5 Trustpilot Fi reviews: support, freeze, wrong LPC charges; 0 mention insights | S20 | HIGH (tiny n) | **contradicts** — weak on its own |
| 3.4 | The users who *do* engage with the feature ask for trends over time (10 likes) and a monthly comparison email | S1 | HIGH | **confirms** that the *narrative* half of your spec is the part with pull — weak signal (one thread) |
| 3.5 | HN: nothing found (1 promo hit) | S27 | HIGH | — |
| 3.6 | **Nothing found — Reddit (r/personalfinanceindia) and Quora unreachable this run**: pullpush 429 ×2, arctic-shift 422/400 ×5, `site:quora.com` returned no Quora pages, on 2026-10-09 | Z5 | ZERO | — |
**Insight:** Across three independent complaint rooms for the two apps that have it (S12, S19, S20 — three sources, so this is a pattern, not a weak signal), no user names spend insights as a reason to join, stay or leave; the pull that exists is for trends and a monthly narrative, not for categorisation. · **Impact:** contradicts "losing users to apps that have it"; narrows what would be worth building if you build.

### Angle 4 — Offerings, and evidence of use · stores, GitHub, AA data · keys: `Firefly III` `Actual Budget` `Sahamati PFM` `CGAP account aggregator`
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| 4.1 | "almost half" of SEBI-FIU consents by Mar 2024 were used for PFM; RIA consents +17%/month | S16 | HIGH | **confirms** demand for aggregation/PFM exists at the rails level |
| 4.2 | 25% of CGAP survey respondents had shared data with PFM apps via AA; 86% rated the experience positive | S17 | HIGH (n not captured) | **confirms** people will consent for PFM |
| 4.3 | India: 1.7B finance-app downloads in 2024; wallets 386.8M, lending 274.4M; **no PFM/budgeting sub-category reported** | S6 | MEDIUM | **unknown** — PFM is not large enough to be broken out by Sensor Tower's secondary coverage |
| 4.4 | OSS PFM is big and explicitly "No AI" (Firefly III 24.8k★; Actual 29.4k★) — *adjacent, global*; last-commit dates not captured | S25, S26 | HIGH/ZERO | **unknown** — a privacy-first counter-signal, not India evidence |
| 4.5 | Evidence that *AI categorisation specifically* retains users: **nothing found** in any opened source | S1–S20 | — | **does not confirm** |
**Insight:** Evidence of use exists for aggregation on AA rails; evidence that an AI-categorised monthly narrative retains anyone was not found anywhere opened. · **Impact:** unknown on the belief; confirms the data route if you build.

### Angle 5 — Method · what the canon says · Kano, Torres, Fitzpatrick
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| 5.1 | Kano: a must-be ("table stakes") attribute is one where "when done poorly, customers are very dissatisfied"; attributes migrate "from delighter to performance need and then to basic need" as competitors raise the bar | S21 | HIGH | **gives the test**: if insights were must-be, its absence or poor quality would appear in reviews. It does not (3.1–3.3) → **contradicts** |
| 5.2 | Torres: start from the desired outcome, map opportunities, *then* pick solutions — not solution-first | S22 | HIGH | **unknown** — the request as framed is solution-first ("build insights"); Angle 1 is the missing outcome |
| 5.3 | Mom Test: "Ask about specifics in the past instead of opinions about the future"; "It's easy for them to say yes … Not helpful." | S23 | MEDIUM | **gives the falsifier-(b) method**: ask churned users what they did last month, not "would insights have kept you" |
**Insight:** The canon says "table stakes" is an empirical claim with a specific signature (dissatisfaction when absent) and that signature is missing. · **Impact:** contradicts the framing; defines how to run falsifier (b).

### Angle 6 — Cases · post-mortems, press with numbers · keys: `Fi Money existential crisis` `Jupiter users` `Mint shutdown` `Walnut acquisition`
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| 6.1 | Fi: $137M raised; FY23 ₹300 Cr loss on ₹38 Cr revenue; runway 18 → 10 months; CEO "phased out a few features that didn't meet our benchmarks for engagement or monetisation" | S9 | HIGH | **contradicts** — the app with the richest insights tool is the one in crisis; the phased-out features are unnamed, so this is suggestive, not proof |
| 6.2 | Fi 2026: non-lending products "failed to generate meaningful revenue"; users "complained about delayed refunds and slow support" | S10 | HIGH | **contradicts** "losing users to features" — users left over trust and support |
| 6.3 | Jupiter 2021: ~0.5M users, 65% transacting monthly — pre-Insights baseline; no post-Insights figure published | S11 | HIGH (stale) | **unknown** — no before/after exists in public |
| 6.4 | Mint (*adjacent*): free PFM, "not financially viable", shut 2024 | S13 | HIGH | **unknown** on retention; **contradicts** monetisation-by-PFM — one case |
| 6.5 | Walnut: 7M downloads → $30M lender acquisition; standalone app gone | S4 | HIGH | **contradicts** PFM as a standalone driver — one case |
**Insight:** Nobody — Indian or otherwise, in anything opened — has published a retention gain from spend insights; the two Indian apps that have it are the two with the worst public health, for reasons their users say are unrelated. · **Impact:** falsifier (a) fires on "no gains shown"; it does not prove no gains exist.

### Angle 7 — Constraints · official docs · keys: `Play SMS policy` `Account Aggregator` `DPDP`
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| 7.1 | Play policy text permits READ_SMS for "SMS-based money management. For example, apps that track and manage budget." but forbids exfiltrating "non-financial or personal SMS history" | S2 | HIGH | **unknown** — route exists on paper |
| 7.2 | In practice a finance app was refused in Dec 2025: "reading SMS for financial data doesn't qualify … manual input is an alternative" | S3 | HIGH (*adjacent*: one developer) | **unknown** — SMS route is a review risk; weak signal (one case) |
| 7.3 | AA rails: 500M consents, 1,100+ entities live — the compliant data route | S8 | HIGH | **unknown** — build on consent, not SMS |
| 7.4 | DPDP 2023: consent-only processing, right to erasure, penalties to ₹250 Cr; profiling not specifically regulated | S24 | HIGH | **unknown** — a categorised spend history is personal data with an erasure right; design for it |
**Insight:** If built, the data path is AA consent, not SMS; the stored narrative must be erasable. · **Impact:** no change to the belief; sets non-negotiables for a spec.

### Angle 8 — Distribution · the same rooms as angle 3 · light
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| 8.1 | Reachable rooms where these users talk unprompted: community.jupiter.money, Desidime finance threads, App Store reviews, Trustpilot | S1, S12, S19, S20 | HIGH | **unknown** — rooms exist; sizes not captured |
| 8.2 | Reddit / Quora: **nothing found — lane unreachable this run** (see Z5) | Z5 | ZERO | — |
**Insight:** Four public rooms are reachable without login; Reddit needs a working archive key next run. · **Impact:** none on the belief.

### Angle M — Market size (asked by name) · keys: `RedSeer PFM India` `Gartner personal finance India` `BCG fintech 2030` `Statista finance apps India` + own arithmetic
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| M.1 | **Gartner: nothing found** — searched 2026-10-09 | Z1 | ZERO | — |
| M.2 | **RedSeer: nothing for PFM apps** — only a 2020 *wealthtech* figure, not opened | Z2 | ZERO | — |
| M.3 | BCG (via press): Indian fintech revenue "USD 190 billion by 2030"; sector grew 50% in 2023 — whole sector, no PFM cut | S15 | MEDIUM | **unknown** — a sector number, not a PFM number |
| M.4 | IMARC: India "personal finance software" USD 44.5M (2025) → 65.3M (2034), 4.24% CAGR — vendor report, no methodology, "software" incl. small business | S5 | HIGH (that it says so) | **unknown** — if this is the market, it is tiny; do not present it as the PFM-app market |
| M.5 | Statista finance-apps India: all numbers paywalled | S14 | ZERO | — |
| M.6 | Open-data anchors (HIGH): 500M consents, 310M+ accounts linked (S8); 80–90M people on AA ≈ 8% of adults (S18); "almost half" of SEBI-FIU consents → PFM (S16); 25% of surveyed AA users shared with PFM apps (S17); 1.7B finance downloads (S6, MEDIUM) | S8, S16, S17, S18, S6 | HIGH / MEDIUM | **unknown** — these size *adoption of the rails*, not revenue |
**Insight:** There is no credible, citable Gartner or RedSeer number for the Indian PFM-app market in the open; the defensible slide is BCG's sector figure (MEDIUM, labelled) plus Sahamati/CGAP adoption numbers (HIGH), and your 1.2M MAU set against 80–90M AA users (~1.3–1.5%). Any ₹ PFM-app figure you are offered is a vendor estimate without methodology. · **Impact:** unknown on the belief; protects you from a number that will not survive a diligence question.

### Angle C — Top complaints at the two apps (asked by name) · App Store RSS, Trustpilot, Desidime; G2 has no listing for either
| # | Finding | Source | Mark | Changes the belief? |
|---:|---|---|:--:|---|
| C.1 | **Jupiter** (~50 reviews, S19), themes by count in this feed page: no human support (≥7) · account blocked from closing / closure charges (≥5) · freezes & liens (≥4) · hidden fees (≥4) · KYC/login deadlocks (≥4) · CIBIL misreporting (2) · loan spam (1) · **insights/categorisation: 0** | S19 | HIGH | **contradicts** |
| C.2 | **Fi** — app-store feed and store pages unreachable (Z3); what opened: Trustpilot 5 reviews (support, freeze, wrong charges) + Desidime 15 replies (freezes, refunds, AMB tracker); **insights: 0 mentions** | S20, S12, Z3 | HIGH on what opened / ZERO on App Store | **contradicts**, with the App Store gap stated |
**Insight:** At both apps, the top complaints are trust, support and fees; the insights feature appears in neither complaints nor praise (one 5-star "understand about you money flow"). · **Impact:** contradicts "table stakes" — the feature is not what users at these apps talk about.

---

## 3 · Verdict

**Belief:** *"Spend insights is table stakes now and we're losing users to apps that have it."* — **Contradicted on the half that matters, confirmed on the half that does not.** "The apps have it" is confirmed (S1, S7). "It is table stakes" and "we are losing users to it" are contradicted by the three findings that decided it: (1) zero mentions of insights in ~70 verbatim user statements across three complaint rooms for the two apps that have it (S19, S12, S20); (2) the users of those apps say they leave over freezes, support, fees and closure friction (S19, S12, S10); (3) the canon's own test for "table stakes" — dissatisfaction when absent — does not fire (S21). Your own churn data (Angle 1) is still **unknown**.

**Falsifier:** (a) **fired** on its weaker reading — no retention gain from the feature has been shown by Fi or Jupiter, or by anyone in any opened source; Fi's CEO phased out unnamed features for failing "engagement or monetisation" benchmarks (S9). It did not fire on the strong reading (proof that gains do not exist) — no one has published either way. (b) **untested** — it lives in your churn data, not on the web.

**Contradicting evidence** (to the belief) — all in `SOURCES.md`: S19 (Jupiter reviews, 0/50 mention insights) · S12 (Fi leavers, 0/15) · S20 (Fi Trustpilot, 0/5) · S9, S10 (Fi's richer insights tool did not prevent crisis; users left over trust) · S4 (Walnut survived only as a lender) · S13 (Mint, *adjacent*). **Supporting evidence**, so the slide is honest both ways: S1 (10 likes for trend graphs — pull for the *narrative*), S16/S17 (PFM is a real AA use case, 86% positive), S7 (Fi judged it worth building).

**Top three, by impact on the goal (retention on 1.2M MAU):**
1. The users of the two apps that have the feature do not mention it when they leave, stay or complain (S19, S12, S20). If that holds in *your* churn data, the belief is dead.
2. The one place real pull showed up was for trends over time and a monthly comparison — the narrative, not the categorisation (S1). If anything is built, that is the slice.
3. If it is built, the data path is Account Aggregator consent (500M consents, S8), not SMS parsing (S2 vs S3), with DPDP erasure designed in (S24).

**Next step: one named gap.** Falsifier (b). Pull the last 90 days of your own exit-survey text, support tickets and app-store reviews; count statements that name spend tracking, insights or categorisation; then run ten Mom-Test interviews with churned users ("what did you do last month to see where your money went?" — never "would insights have kept you"). If the count is ~0 and the interviews agree with S19/S12, decide **no** before the round and put the slot on whatever your users *do* name. If the count is material, write the spec for the narrative slice (3.4) on AA rails. This is a one-week question, not a research programme.

---

## 4 · Self-check (not a scoreboard)

| # | Check | Actual value |
|---:|---|---|
| 1 | Ground truth before search | Section 0 stamped 2026-10-09T04:18:22Z; first search ~04:19Z; first SOURCES row read ~04:20Z. **Pass** |
| 2 | Every claim sourced and marked | 44 findings across 10 angles; each cites an S#/Z# row with HIGH / MEDIUM / ZERO. **Pass** |
| 3 | No snippet-sourced HIGH | 23 HIGH rows (S1–S4, S5, S7–S14, S16–S22, S24–S27), each with URL and date 2026-10-09. Snippet-only numbers (Z2, Z6, Z7) are ZERO. **Pass** |
| 4 | Patterns need three | "No user names insights when leaving": S12, S19, S20 = 3 independent sources → pattern. "SMS route is rejected in practice": 1 source → labelled weak signal (7.2). "Trend/narrative pull": 1 thread → labelled weak signal (3.4). **Pass** |
| 5 | Empty angles reported | Angle 1: not searched by design, stated. Reddit/Quora: "nothing found — searched …" with HTTP codes (Z5). HN: 1 hit, stated (S27). Gartner/RedSeer: nothing found, stated (Z1, Z2). Fi App Store: unreachable, stated (Z3). **Pass** |
| 6 | Every insight states its impact | 10 angle insights; each ends in confirms / contradicts / unknown. **Pass** (adversarial — reader to judge) |
| 7 | Verdict is honest | Section 3 lists S19, S12, S20, S9, S10, S4, S13 as contradicting and S1, S16, S17, S7 as supporting. **Pass** (adversarial) |
| 8 | Ends in a step a decision can take | One named gap (falsifier b), with where to look and the decision rule either way. **Pass** |
| — | Red flags | No invented source or number; nothing behind a login; the PFM PDF (S28) is marked ZERO rather than summarised; Fi App Store complaints marked ZERO rather than rounded up. Assumption stated: "the two apps" = Fi and Jupiter. |

**Size:** ~7 pages. **Rollback:** delete `run-04/`.
