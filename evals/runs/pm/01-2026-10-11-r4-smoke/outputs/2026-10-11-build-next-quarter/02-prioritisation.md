DRAFT, not reviewed by a person

# Prioritisation — ranking the candidates (C02)

> Evidence source: `01-interview-synthesis.md`. All data SYNTHETIC.

## The metric this ranking serves
, so I cannot anchor this to a number you already watch. **Baseline: unknown — do not invent one.** Given you bill per seat and one interviewed firm is a churn risk, the two metrics this work most plausibly serves are **seat retention** (keeping paying firms) and **expansion revenue / willingness to pay**. Cheapest way to get the baseline before planning: pull current logo + seat churn for the last 2–4 quarters from billing; it needs no analytics connector.

Effort is marked **unknown** on every row on purpose: effort estimates must come from your engineers, not from me (C02 limit).

## Scores (impact on getting-paid / retention · confidence · effort)
| Candidate | Impact | Confidence | Effort | Why (inputs to the score) |
|---|---|---|---|---|
| **1. Automatic payment reminders** | **High** | **Medium** | Unknown — ask eng | 3 of 6 ask by name (A,E,F); F pays a rival for it today and would switch spend in-house; E quantifies "a day a month"; addresses the 4-of-6 collections pain |
| 2. Payment-status visibility (who to chase) | Medium | Low | Unknown — ask eng | 1 of 6 direct (C), but C "would pay more"; overlaps heavily with #1 — reminders need the same "who's unpaid" data |
| 3. Lower price per seat | Medium (retention, not a build) | Low | N/A — pricing decision | 1 of 6 (D), the only named churn risk; this is a pricing/business call, not a quarter's build — routed out, see judgment list |
| 4. Bank reconciliation | Low | Low | Unknown — likely large | 1 of 6 (E), self-labelled "nice to have"; large surface area for a weak signal |
| 5. Dark mode | Low | Low | Unknown — likely small | 1 of 6 (B), cosmetic, from an already-happy firm |

## The two closest calls, and what would flip them
1. **#1 reminders vs #2 status-visibility.** They are the same pain seen from two ends. Reminders *send* the chase; status-visibility *tells you who to chase*. **Flip condition:** if, when you scope #1, reminders turn out to depend on a status/unpaid-invoice view you don't have yet, then #2 becomes the first increment and ships inside #1. Likely you build a thin slice of #2 on the way to #1.
2. **#1 reminders vs #3 price.** Reminders win the *build* slot, but they do nothing for D, the one account signalling departure. **Flip condition:** if seat churn is concentrated on price (check the billing data above) rather than on collections pain, the highest-leverage move next quarter may be a pricing decision, not a feature. That is a decision for you/leadership, not something this synthesis can settle — it's first on the judgment list.

## Recommendation
Build **automatic payment reminders**. It is the only candidate backed by three independent interviews, and the only one with a customer already paying someone else for it. Scope the "who is unpaid" view (#2) as the first slice so the feature stands on real status data.
