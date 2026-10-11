# 01 · Candidates and evidence (C02 steps 1–2)

> Source: six interview notes (Firms A–F), **SYNTHETIC** per the user. Product: B2B invoicing tool, ~300 paying firms, billed per seat, small accounting firms.

## The goal the ranking serves
Not fixed by the user (no `context/PRODUCT.md`; the goal-metric question was declined). **Assumption:** rank on overall strength of evidence across the six notes, and flag where the choice of metric (churn/price vs. stickiness/expansion) would change things. Metric to be confirmed before planning.

## Candidates found in the notes
Each line is tagged HIGH / MEDIUM / ZERO (PM.md §3) and "direct ask" vs "adjacent" (the firm described a problem the feature would solve but asked for something else).

### 1. Automatic payment reminders
| Firm | Seats | Evidence (as written in the notes) | Type | Confidence |
|---|---|---|---|---|
| A | 4 | "Month end is hell. We chase clients for payment by email, one by one." + asked twice whether reminders could be automatic | direct ask | HIGH |
| E | 9 | "Automatic reminders would save my junior a day a month." | direct ask | HIGH |
| F | 15 | Uses a separate tool just to send payment reminders and pays for it; would drop it if we had reminders built in | direct ask | HIGH |
| B | 11 | Two clients paid late in September "because they lost the invoice email" | adjacent | MEDIUM |
| C | 6 | "I spend Friday afternoons copying payment status into a spreadsheet so I know who to chase." | adjacent | MEDIUM |

**Direct asks: 3 firms (A, E, F). Adjacent: 2 firms (B, C). Untouched: 1 firm (D).**
Clears the "a theme needs three independent data points" bar (PM.md §3) on direct asks alone. Extra signals: quantified value ("a day a month", E), willingness to pay (F pays a competitor today), competitor-displacement (F would drop the external tool).

### 2. Payment-status / "who to chase" visibility
| Firm | Seats | Evidence | Type | Confidence |
|---|---|---|---|---|
| C | 6 | "I spend Friday afternoons copying payment status into a spreadsheet so I know who to chase." + "Would pay more for that to go away." | direct ask | MEDIUM |

One direct firm, with willingness to pay. **Weak signal** (fewer than three data points). Overlaps candidate 1 — automated reminders partly solve C's chase, but not the at-a-glance status view.

### 3. Bank reconciliation
| Firm | Seats | Evidence | Type | Confidence |
|---|---|---|---|---|
| E | 9 | Wants bank reconciliation, called it "nice to have" | direct ask, self-deprioritised | LOW |

One firm, explicitly "nice to have." **Weak signal.**

### 4. Dark mode
| Firm | Seats | Evidence | Type | Confidence |
|---|---|---|---|---|
| B | 11 | "Wants a dark mode"; firm is "happy overall" | direct ask | LOW |

One firm, cosmetic, from an already-happy customer. **Weak signal.**

### 5. Lower price per seat
| Firm | Seats | Evidence | Type | Confidence |
|---|---|---|---|---|
| D | 2 | Considering leaving for a cheaper tool; main complaint price per seat; did not mention reminders | direct ask | MEDIUM |

One firm (the smallest, 2 seats). **Not a build** — this is a pricing/packaging decision for a human, and it conflicts with C and F who signal willingness to pay *more*. Routed to the judgment list, not ranked as a feature.

## Counter-evidence (argue against reminders first — PM.md §1.3)
- Only **3 of 6** asked for reminders *directly*; B and C asked for other things first.
- The loudest churn risk (D) is about **price**, and reminders do nothing for it.
- n = 6, synthetic, self-reported. No usage data on how many of the ~300 firms the chasing problem actually affects. The theme is real in this sample; its size across the base is unknown.
