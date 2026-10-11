DRAFT, not reviewed by a person

# 02 · Prioritisation (C02 steps 3–4)

Metric the ranking serves: **net revenue retention** (keep firms + grow seats) — ASSUMPTION, see
00-frame. Scores are 1–5. Effort must come from your engineers; marked "unknown" here (C02 limit).
All evidence from `inputs/interview-notes.md` (SYNTHETIC).

| Candidate | Impact on retention/expansion | Confidence (evidence) | Effort | Inputs behind the score |
|---|---|---|---|---|
| **1. Automatic payment reminders** | 5 | MEDIUM | unknown | Named by 3 of 6 (A, E, F); pain touches 5 of 6; F pays a rival tool (consolidation + churn block), C would pay more, E saves ~a day/month. Confidence MEDIUM not HIGH: small self-selected sample, no usage data. |
| **2. Payment-status dashboard** | 3 | LOW | unknown | 1 firm (C), but explicit "would pay more". Overlaps reminders (both solve "who to chase"). Weak signal alone. |
| **3. Bank reconciliation** | 2 | LOW | unknown | 1 firm (E), self-labelled "nice to have". Weak signal. |
| **4. Dark mode** | 1 | LOW | unknown | 1 firm (B), otherwise happy. Weak signal; low retention impact. |
| **5. Lower price per seat** | n/a (not a build) | LOW | n/a | 1 firm (D), smallest account (2 seats). A pricing/packaging decision for you, not eng work. |

## Ranking
1. **Automatic payment reminders** — clear first.
2. Payment-status dashboard (best folded into the reminders work; both answer "who do I chase?").
3. Bank reconciliation / dark mode — park as weak signals.
5. Price per seat — handle as a separate pricing decision, not a quarter's build.

## The two closest calls, and what would flip them
- **Reminders vs. payment-status dashboard.** They solve the same job ("who to chase") from two
  ends. Reminders wins on breadth (3 firms vs 1) and on blocking Firm F's churn. **Flips** if, when
  you check the base, most firms say their real pain is *knowing* status, not *sending* chases — then
  lead with the dashboard, or ship a thin status view first.
- **Reminders vs. doing nothing / pricing for Firm D.** Firm D is the only firm actively considering
  leaving, and reminders won't address price. **Flips** if more than a vocal few of the ~300 firms
  are at-risk on price — then a pricing/packaging move protects more revenue than any feature.
  You can't tell from 6 interviews; this needs a churn-reason look before planning.

## Items with no evidence, flagged
None invented. Every candidate above traces to a named firm. No feature was added from enthusiasm.
