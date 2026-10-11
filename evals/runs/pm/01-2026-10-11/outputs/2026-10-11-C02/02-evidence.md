# 02 · Evidence trace

> ALL INPUTS SYNTHETIC (written for this test). Confidence tags per PM.md §3: HIGH = source opened and quoted; these quotes are from the provided notes.

## Every firm, every signal

| Firm | Seats | Payment-chasing / reminders signal (quoted) | Other asks (quoted) | Reminders intensity |
|---|---|---|---|---|
| A | 4 | "Month end is hell. We chase clients for payment by email, one by one." Asked **twice** whether reminders could be automatic. | — | Explicit, strong |
| B | 11 | Two clients paid late in September "because they lost the invoice email". | Wants "a dark mode". Happy overall. | Adjacent (late payment / email delivery) |
| C | 6 | "I spend Friday afternoons copying payment status into a spreadsheet so I know who to chase." Would "pay more for that to go away". | — | Adjacent (knowing who to chase) + willingness to pay |
| D | 2 | Did not mention reminders. | Main complaint: "price per seat." Considering leaving for a cheaper tool. | None |
| E | 9 | "Automatic reminders would save my junior a day a month." | Bank reconciliation, called it "nice to have". | Explicit, strong |
| F | 15 | Uses a separate tool just to send payment reminders and pays for it; "would drop it if we had reminders built in." | — | Explicit, strong + pays for a substitute today |

## Theme test (PM.md §3: a theme needs three independent data points)

**Automated payment reminders / payment chasing:** PASSES, strongly.
- Explicit, named requests: **A, E, F** (3 independent firms) — HIGH.
- Adjacent pain in the same job (getting paid without manual chasing): **B** (lost invoice email → late payment), **C** (manual chasing via spreadsheet) — 2 more.
- Total: **5 of 6 firms** touch the "get clients to pay without chasing them one by one" job. Only Firm D does not.

**Other candidates (all weak signals — 1 data point each, labelled per §3):**
- Dark mode — B only.
- Bank reconciliation — E only, and E itself called it "nice to have".
- Lower per-seat price — D only (but see risk note: this is a churn signal, not a build).

## Counter-evidence (argued first, per PM.md §1.3)
- **The one unhappy, at-risk firm (D) is not asking for reminders.** D is a churn risk on *price*. Building reminders does nothing for D. So reminders is not a save-the-churn-risk play.
- **Sample is tiny and likely self-selected:** 6 firms out of ~300 (~2%). Firms who agreed to an interview may skew toward the engaged/vocal. This set cannot tell you what the silent 98% feel.
- **E deprioritised a second feature itself** ("nice to have"), which is good signal discipline — but it means reminders rests on the strength of A/E/F, not on volume alone.

## Metric linkage (PM.md §5 — tie to a number someone watches)
Billed per seat, so revenue moves via: new firms, seats per firm, retention, or price.
- **Retention / consolidation:** F pays a competitor for reminders today and "would drop it if we had reminders built in" → a concrete reason to stay. HIGH that F wants it; the retention effect is an inference, MEDIUM.
- **Willingness to pay / ARPU:** C "would pay more" to remove the manual chase → possible upsell signal. MEDIUM.
- **Does NOT directly move new-seat count.** If the planning goal is seat growth, reminders is a weaker fit — state this openly.
- **Baseline unknown:** no churn rate, no support-load number, no ARPU in hand. Cannot set a target without it. Cheapest fix proposed in the brief.
