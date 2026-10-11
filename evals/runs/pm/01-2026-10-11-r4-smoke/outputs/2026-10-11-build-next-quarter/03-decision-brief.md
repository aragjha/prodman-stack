DRAFT, not reviewed by a person

# Decision brief — what to build next quarter
*For the planning meeting (~2026-10-25). Evidence is SYNTHETIC (six interview notes).*

## Decision
Pick the one feature to build next quarter for our per-seat B2B invoicing tool (~300 firms).

## Recommendation
**Build automatic payment reminders.** Ship the "which invoices are unpaid" view as the first slice, then the automatic sending on top.

## The three strongest pieces of evidence
| # | Evidence | Confidence |
|---|---|---|
| 1 | **3 of 6 firms ask for automatic reminders by name** — Firm A ("We chase clients for payment by email, one by one," asked twice whether reminders could be automatic), Firm E, Firm F. It is the only candidate with the 3-interview support a real theme needs. | HIGH — quotes/asks are in the notes |
| 2 | **Firm F already pays a separate tool** just to send payment reminders and "would drop it if we had reminders built in" — proven willingness to pay, plus a retention angle. | HIGH — stated in the notes |
| 3 | **Firm E: "Automatic reminders would save my junior a day a month"** — a quantified cost of today's manual chasing. | HIGH — quoted |

Collections pain shows up more broadly still: 4 of 6 firms (A, C, E, F) describe chasing clients to get paid; a 5th (B) had two clients pay late "because they lost the invoice email."

## What would reverse this call
- **Billing data shows seat churn is driven by price, not collections.** Firm D — the only firm signalling it may leave — complains about price per seat and never mentioned reminders. If churn concentrates there, a pricing decision beats any feature. *(Check this before the meeting; see next step.)*
- **Scoping shows reminders need a status/unpaid view you don't have.** Then the first increment is that view (Firm C's exact pain), still inside this bet.

## Risks
- **Sample is six synthetic interviews.** Below the 8–15 range; counts are patterns, not proportions of your 300 firms. Direction is consistent; magnitude is unknown.
- **Reminders don't retain the one at-risk account (D).** Don't present this build as a churn fix.
- **No baseline metric exists** for seat retention or expansion, so success can't yet be measured — fix below.

## Success measure (to set before build)
- Primary (lagging): seat retention / expansion revenue. **Baseline: unknown — pull from billing, don't invent.**
- Leading (this quarter): share of reminders sent automatically vs manual chases; invoices paid on/before due date. Set targets once the baseline exists.

## Next step, owner, date
1. **You:** pull last 2–4 quarters of seat + logo churn from billing (no connector needed) to test the price-vs-collections reversal — before 2026-10-25.
2. **You + engineering:** get an effort estimate for reminders (and the unpaid-invoice slice) for the planning meeting.
3. **You:** take this brief to planning as the recommended bet.
