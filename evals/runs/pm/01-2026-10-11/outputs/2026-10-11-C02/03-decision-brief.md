# Decision brief — what to build next quarter · DRAFT

> **ALL EVIDENCE SYNTHETIC.** The six interview notes were written for this test. Do not treat as real customer data.
> Owner: PM · For: planning, ~2026-10-25 · One page.

## Decision
Pick the one feature to build next quarter for the per-seat invoicing tool (~300 firms).

## Recommendation
**Build automated payment reminders** (invoicing tool sends scheduled reminders to a firm's clients until paid; firm sees who's been chased and who still owes).

It is the single pain that shows up across the most firms, the only one anyone names a current cost for, and the only one someone already pays a competitor to solve.

## The three strongest pieces of evidence

| # | Evidence (quoted) | Firm | Confidence |
|---|---|---|---|
| 1 | "Uses a separate tool just to send payment reminders and pays for it… would drop it if we had reminders built in." | F (15 seats) | HIGH — a firm paying a competitor *today* for exactly this |
| 2 | "Automatic reminders would save my junior a day a month." | E (9 seats) | HIGH — a quantified cost the feature removes |
| 3 | "Month end is hell. We chase clients for payment by email, one by one." Asked **twice** if reminders could be automatic. | A (4 seats) | HIGH — unprompted, repeated |

Supporting: **5 of 6 firms** touch the "get paid without chasing one by one" job — add C ("Friday afternoons copying payment status… so I know who to chase," and "would pay more" to remove it) and B (two clients paid late "because they lost the invoice email"). Full trace: `02-evidence.md`.

## How sure you can be
- **That reminders is the top pain in this set:** HIGH. Quote-backed, 3 explicit asks + 2 adjacent, only 1 firm silent.
- **That it's the right bet for the business next quarter:** MEDIUM. It most plausibly moves **retention and willingness-to-pay**, not new-seat growth — so it fits only if those are what planning is optimising. And the read rests on **6 firms out of ~300 (~2%)**, possibly self-selected.

## What would reverse the call
- The number planning cares about is **new-seat acquisition**, which reminders does not directly move.
- A wider check (support tickets, a one-question in-app poll to all 300) shows payment-chasing is a vocal-minority issue, not a majority one.
- Reminders already exists or is trivially worked around for most firms in a way these 6 don't represent.

## Risks
- **Churn risk is elsewhere.** The only at-risk firm (D, 2 seats) is leaving on **price**, not features — reminders will not save D. Track price-driven churn separately; don't let this build stand in for it.
- **Scope creep toward reconciliation.** E raised bank reconciliation but called it "nice to have" — keep it out of this quarter.
- **Deliverability is the hard part.** B's pain ("lost the invoice email") means reminders only work if emails actually land; budget for deliverability, not just a scheduler.
- **Small sample.** Don't over-fit the design to 6 firms.

## Success measure (PM.md §6)
- **Primary (lagging):** gross revenue retention / logo churn. **Baseline: unknown — not in hand.**
- **Leading (movable this quarter):** % of invoices with a reminder enabled; count of firms who turn it on; invoices paid before due date vs. baseline.
- **Guardrail:** reminder emails must not trigger client complaints / spam flags to the firms.
- **Cheapest way to get the missing baseline:** pull current logo churn and average days-to-payment from existing billing/invoice data before the meeting (no new instrumentation needed).

## Next step
Take this to planning as the recommended bet; before building, run a one-question in-app poll to all ~300 firms ("Would automatic payment reminders be valuable to you?") to confirm the 6-firm signal generalises. Owner: PM. By: planning, ~2026-10-25.
