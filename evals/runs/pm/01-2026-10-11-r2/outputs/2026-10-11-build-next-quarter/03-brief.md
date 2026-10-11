# Decision brief — what to build next quarter · DRAFT

> For planning (~week of 2026-10-25). Owner: PM. Evidence: six customer interviews, **SYNTHETIC** per the user (n=6; not usage data).

## Decision
Pick the one thing to build next quarter for our B2B invoicing tool (~300 firms, billed per seat).

## Recommendation
**Build automatic payment reminders.** How sure: **medium-high.** It is the only candidate with three or more independent direct asks, and the only one carrying quantified value, willingness to pay, *and* a customer paying a competitor for exactly this today.

## The three strongest pieces of evidence
| # | Evidence (as written in the notes) | Confidence |
|---|---|---|
| 1 | **3 of 6 firms asked for reminders directly** — A ("Month end is hell. We chase clients for payment by email, one by one." + asked twice if reminders could be automatic), E ("Automatic reminders would save my junior a day a month."), F (pays a separate tool for reminders, would drop it if built in). | HIGH |
| 2 | **2 more firms describe the same problem** without naming the feature — B (two clients paid late "because they lost the invoice email"), C ("I spend Friday afternoons copying payment status into a spreadsheet so I know who to chase."). So **5 of 6** touch the chasing / late-payment problem; only D does not. | MEDIUM |
| 3 | **Willingness to pay and competitor displacement** — F already pays an outside tool for reminders and would drop it; C "Would pay more for that to go away." | HIGH (F), MEDIUM (C) |

## What would reverse the call
- Usage or a quick survey shows the chasing problem affects only a small share of the ~300 firms (this sample is 6).
- Engineering effort is too large to ship in the quarter (reminders need scheduling + reliable email delivery + templates — unverified).
- A churn look shows **price** (Firm D) is driving real logo loss at scale — then the quarter's priority is a pricing decision, not this build.

## Risks
- **Sample is tiny and synthetic (n=6).** Real demand across 300 firms is unmeasured.
- **Overlap risk:** C's need may be a payment-status view, not just auto-send; scope reminders to also show "who's unpaid" so one build covers both.
- **Deliverability:** reminder emails that land in spam fail silently and can erode trust — needs a guardrail metric.
- **D's price complaint is unaddressed** by any feature.

## Success measures (propose; baselines unknown — do not invent, PM.md §6)
- **Primary (leading):** % of invoices with a reminder sent automatically, and median days-to-payment on reminded invoices vs. baseline. Baseline **unknown** — cheapest way to get it: pull current avg days-to-payment from existing invoice data before building.
- **Guardrail:** reminder email deliverability / bounce rate; opt-out or complaint rate.
- **Lagging (watch, don't attribute yet):** seat retention among firms that adopt; F-type firms dropping their external tool.

## Next step, owner, date
1. **Get an effort estimate** for reminders (incl. email delivery) — Eng lead — before planning (~2026-10-25).
2. **Pull baseline days-to-payment** from invoice data — PM/Data — before planning.
3. **Decide the goal metric** (retention vs. stickiness vs. revenue) — PM — at or before planning.

---
*DRAFT — needs a human decision (see the "Needs your judgment" list). Nothing here has been sent or shared.*
