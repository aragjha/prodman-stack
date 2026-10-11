# 02 · Scoring and ranking (C02 steps 3–4)

Scored on **impact / confidence / effort**, every candidate gets all three (PM.md / C02). Effort is **unknown — needs engineering** (user assumption; C02 limit says effort comes from engineers, not the model). Impact is judged as breadth × intensity of the problem in this sample, since the goal-metric is not fixed.

| Rank | Candidate | Impact (why) | Confidence | Effort | Inputs behind the score |
|---|---|---|---|---|---|
| 1 | **Automatic payment reminders** | **High** — 3 direct + 2 adjacent of 6 firms; quantified value; willingness to pay; displaces a competitor | **HIGH** | unknown (likely non-trivial: scheduling, email delivery, templates — assumption) | A, E, F direct; B, C adjacent |
| 2 | Payment-status / "who to chase" view | Medium — 1 firm, would pay more; overlaps #1 | MEDIUM (weak signal) | unknown | C |
| 3 | Bank reconciliation | Low–Med — 1 firm, self-labelled "nice to have" | LOW (weak signal) | unknown | E |
| 4 | Dark mode | Low — 1 firm, cosmetic, already happy | LOW (weak signal) | unknown | B |
| — | Lower price per seat | Not a feature — pricing/packaging decision; conflicts with pay-more signals | MEDIUM (weak signal) | n/a | D |

## The call
**Build automatic payment reminders.** It is the only candidate that clears the three-data-point theme bar, and it carries the strongest supporting signals (quantified time saved, willingness to pay, a customer paying a competitor for exactly this).

## The two closest calls, and what would flip them
1. **Reminders vs. a payment-status/"who to chase" view.** C's problem reads as either — automate the chase, or make status visible. They overlap. *Flips if:* more firms want the at-a-glance status view than the automated send, or if reminders can't ship without the status view anyway (then scope both; ship reminders first). Cheapest consideration: a reminders feature that also exposes "who's unpaid" covers much of C.
2. **Feature vs. price (Firm D).** D's churn risk is price, which no build addresses. *Flips the plan's shape if:* a churn look shows price is driving real logo loss across the ~300 base — then run a pricing/packaging decision in parallel, separate from the build. One firm (the smallest, 2 seats) is not yet enough to act on.
