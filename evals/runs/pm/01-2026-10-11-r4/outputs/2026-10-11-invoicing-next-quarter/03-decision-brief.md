DRAFT, not reviewed by a person

# Decision brief — what to build next quarter

**Decision:** Which one thing to build next quarter for the B2B invoicing tool.
**Decider / when:** You (PM), at the planning meeting in two weeks (~2026-10-25).
**Evidence base:** Six synthetic customer interviews (Firms A–F). No usage, revenue or churn data was provided.

---

## Recommendation
**Build automatic payment reminders.** It is the only feature three of the six firms asked for by
name (A, E, F), and it sits inside a get-paid-on-time problem that five of six firms raised in some
form (A, B, C, E, F).

## The three strongest pieces of evidence
| # | Evidence | Confidence |
|---|---|---|
| 1 | Firm A: "Month end is hell. We chase clients for payment by email, one by one." — asked twice whether reminders could be automatic. | HIGH — quoted from the note |
| 2 | Firm E: "Automatic reminders would save my junior a day a month." | HIGH — quoted from the note |
| 3 | Firm F: uses a separate tool just to send payment reminders and pays for it; would drop it if reminders were built in. | HIGH — stated in the note |

Supporting, not counted in the three: Firm C spends Friday afternoons copying payment status into a
spreadsheet to know who to chase; Firm B had two clients pay late in September "because they lost the
invoice email".

## How sure you can be
**Medium confidence.** The signal is consistent and three firms asked by name, which clears this
repo's bar of three independent data points for a real theme. What holds it at medium: only six
interviews (the synthesis workflow is built for 8–15), the notes are synthetic, and there is no
usage, revenue or churn data to show how many of the 300 firms feel this. Six interviews show a
pattern, not a proportion.

## What would reverse the call
- The at-risk firm leaving over price (D) proving churn is driven by pricing, not missing features.
- Reminders turning out to be far larger to build than a cheaper fix that addresses the same pain.

## Risks and what it does not solve
- **Does not help Firm D**, the one firm considering leaving — its complaint is price per seat, a separate problem. Reminders will not retain D.
- **Monetization and churn upside are unmeasured.** F pays for an outside tool and C would pay more, which hint at retention and expansion value, but no revenue figure was given, so none is claimed here.
- **Weak signals parked, not built:** dark mode (B), bank reconciliation (E, its own "nice to have"), standalone payment-status tracking (C).

## Success metric (to set before building)
No baseline was provided, so these are proposed, not measured:
- **Primary (lagging):** share of invoices paid on time, per firm — unknown baseline.
- **Leading (movable in-quarter):** time firms spend chasing payments (e.g. Firm E's junior's "a day a month"); number of firms using reminders at least once.
- **Guardrail:** retention of price-sensitive small firms (like D) does not drop.
- **Cheapest way to get the baseline:** pull current on-time-payment rate from existing invoice data before the quarter starts; if that data does not exist, instrument it as step one.

## Next step
Confirm the above against usage/churn data you can see but I cannot, then take this recommendation
into the planning meeting.
