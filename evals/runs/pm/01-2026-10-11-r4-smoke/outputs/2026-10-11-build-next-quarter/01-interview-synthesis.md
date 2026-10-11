DRAFT, not reviewed by a person

# Interview synthesis — what the six firms said

> Source: `00-request.md` (six interview notes, labelled SYNTHETIC by the user). All data below is SYNTHETIC.
> Research question: which single thing should we build next quarter for our B2B invoicing tool?
> Decision it serves: pick one build for next quarter, for a planning meeting ~2026-10-25.

## Caveats before the counts
- **Six interviews, not a survey.** Below the 8–15 range this workflow is built for. Counts show *patterns*, never market percentages. "3 of 6" is not "50% of customers".
- **Self-selected, small.** Seat sizes range 2–15; we have no idea how representative they are of the ~300 firms.
- A theme needs **three independent interviews** to count as a real theme (PM.md §3). Fewer = weak signal, labelled as such.

## One line per interview (their words first)
| # | Firm (seats) | What they said | Their ask |
|---|---|---|---|
| A | A (4) | "Month end is hell. We chase clients for payment by email, one by one." Asked twice whether reminders could be automatic. | Automatic reminders |
| B | B (11) | Happy overall. Two clients paid late in September "because they lost the invoice email". | Dark mode |
| C | C (6) | "I spend Friday afternoons copying payment status into a spreadsheet so I know who to chase." Would pay more for that to go away. | Payment-status visibility |
| D | D (2) | Considering leaving for a cheaper tool. Did not mention reminders. | Lower price per seat |
| E | E (9) | "Automatic reminders would save my junior a day a month." Bank reconciliation is a "nice to have". | Automatic reminders |
| F | F (15) | Uses a separate tool just to send payment reminders and pays for it. Would drop it if we had reminders built in. | Automatic reminders (built-in) |

## Themes, counted
| Theme | Interviews that directly support it | Count | Signal |
|---|---|---|---|
| **Automatic payment reminders** | A, E, F | **3 of 6** | Real theme (meets threshold) |
| Getting paid / chasing is the month-end pain (broader) | A, C, E, F (B adjacent: lost-invoice late payment) | 4, +1 adjacent | Real theme, but mixes reminders with status-tracking — see note |
| Payment-status visibility (knowing who to chase) | C | 1 of 6 | Weak signal |
| Lower price per seat | D | 1 of 6 | Weak signal (but a churn risk — see below) |
| Dark mode | B | 1 of 6 | Weak signal |
| Bank reconciliation | E (self-labelled "nice to have") | 1 of 6 | Weak signal |

**Note on the two top rows.** Three firms (A, E, F) ask for *automatic reminders* by name. A fourth, C, describes the same collections pain but asks for *status visibility* instead, and B's late-payment story is caused by a lost invoice email. So "chasing clients to get paid" is the pain in 4 of 6 interviews; "build automatic reminders" is the specific fix 3 of 6 reach for. I keep them separate on purpose so the count isn't inflated.

## What makes the reminders signal stronger than a raw count of 3
- **F already pays a competitor** for reminders and "would drop it if we had reminders built in" — proven willingness to pay, and a consolidation/retention angle, not just a wish.
- **E quantifies the benefit**: "would save my junior a day a month" — a concrete cost of the status quo.
- **A asked twice**, in one interview — intensity, not a passing mention. — intensity, not a passing mention.

## Findings that go against building reminders
- **D (the one churn risk named) would not be saved by reminders.** Their issue is price per seat; they "did not mention reminders". Building reminders does nothing for the account most likely to leave.
- **B, the only firm that is explicitly "happy," wants dark mode, not reminders.** Satisfaction here isn't tied to the recommended build.
- Bank reconciliation (E) was volunteered but demoted by the customer themselves ("nice to have") — don't let a second ask from a reminders-supporter read as a second vote for reconciliation.

## Segment pattern (weak, 6 points)
The reminder askers span small-to-large (A=4, E=9, F=15 seats); the largest firm already pays for a separate tool. The smallest firm (D, 2 seats) is the price-sensitive one. Tentative read: larger firms feel collections pain enough to tool around it; the smallest is price-driven. Six points — a hypothesis to test, not a finding.

## So what for the decision
Automatic payment reminders is the only candidate with three independent supporting interviews, and its support is unusually strong for a count of three (a paying competitor-user, a quantified saving, a repeated unprompted ask). Everything else is a single-interview weak signal. The honest ceiling on confidence is the sample: six synthetic interviews, direction consistent, proportions unknown.
