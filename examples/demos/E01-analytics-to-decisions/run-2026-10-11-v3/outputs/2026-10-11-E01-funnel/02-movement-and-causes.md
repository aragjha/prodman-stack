DRAFT, not reviewed by a person

# 02 · What moved, when, and the candidate causes

All rates below are computed from `metrics-weekly.md`; raw signups and activated-firm counts are
quoted exactly, the rate (activated ÷ signups) is derived and shown.

## A. Activation — the real change in the funnel
Activation rate = activated firms ÷ signups, for each signup week.

| Week | Signups | Activated | Rate |
|---|---|---|---|
| 06-01 | 54 | 33 | 61% |
| 06-08 | 57 | 36 | 63% |
| 06-15 | 53 | 33 | 62% |
| 06-22 | 56 | 34 | 61% |
| 06-29 | 41 | 25 | 61% |
| 07-06 | 55 | 35 | 64% |
| 07-13 | 63 | 39 | 62% |
| 07-20 | 64 | 40 | 63% |
| **07-27** | 62 | **26** | **42%** |
| 08-03 | 65 | 27 | 42% |
| 08-10 | 61 | 24 | 39% |
| 08-17 | 64 | 26 | 41% |
| 08-24 | 66 | 28 | 42% |
| 08-31 | 63 | 25 | 40% |
| 09-07 | 62 | 26 | 42% |
| 09-14 | 65 | 27 | 42% |

Activation sat at ~62% (June–20 July average 61.8%) and dropped to ~41% (27 Jul–14 Sep average 41.1%)
— a fall of about a third — **starting the week of 27 July and sustained for eight weeks.** Signups did
not fall (61–66/week through the drop), so this is a conversion problem, not a traffic problem. At
~63 signups/week, ~20 points is ~13 fewer activated firms every week.

## B. Seats — a step up that is mostly a definition change
Seats added ran 25–29/week from June to 17 August (one holiday-week dip to 17), then 61, 60, 57, 62
from the week of 24 August. But 24 August is exactly when the metric started counting free-trial
seats too (see `01-definitions-check.md`). For the one week we can split, paying-firm seats were 29 —
inside the prior paying-seat range of 25–29 (17 in the one holiday week). The ~34-seat jump is mostly
the 32 newly-counted free-trial seats.

## C. Everything else — flat or seasonal
- **Signups** rose from ~55/week (June) to ~63/week from the week of 13 July on — plausibly the new
  signup page (release 3.9, 14 July: "5 fields instead of 9"). A lift in volume, not a problem.
- **Week of 29 June dip** (signups 41, invoices 5,893, paid 3,371) lines up with "No release. Code
  freeze for the public holiday on Friday 3 July." One-week holiday dip; recovered the next week. Seasonal, not a trend.
- **Invoices sent** (7,512 → 8,042) and **Paid within 30 days** (~4,300–4,600) are roughly flat/up.
- **Churned firms** stay in a 0–2 band — noise at this scale.

## D. Lining movements up against releases (E01 step 4)

| Candidate cause | Evidence | Confidence |
|---|---|---|
| **Release 4.0 (28 Jul) invoice template editor rebuild hurt first-invoice** — activation = sending first invoice within 7 days; 4.0 "rebuilt [the editor] with drag and drop blocks" and "The legacy default template is retired", so a new firm can no longer send from a one-click default. Drop begins the week of 27 Jul; 4.0 shipped Tuesday 28 Jul. | **MEDIUM** — timing is tight and the mechanism (retired default template → harder first invoice) is direct, but correlation with a release is a lead, not proof. |
| **New signup page (3.9, 14 Jul) brought lower-intent signups who don't activate** — a competing story for the same drop. | **Ruled out as the primary cause.** The first two cohorts through the new page (weeks of 13 Jul and 20 Jul) activated at 61.9% and 62.5% — normal. The collapse starts the week of 27 Jul, one release later. The page raised volume without lowering the rate. |
| **Bulk invite (4.1, 25 Aug) drives seat growth** — leadership's question. | **LOW / not demonstrable.** The seat jump coincides with both 4.1 *and* the 24 Aug definition change (fully confounded), and the one decomposable week shows paying seats flat at 29. See `04-decision-brief.md`. |

**Leading cause of the funnel change: Release 4.0's invoice-editor rebuild (retired default
template) depressing 7-day activation.** Stated as a hypothesis, confidence MEDIUM.
