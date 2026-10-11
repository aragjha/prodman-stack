DRAFT, not reviewed by a person

# 03 · The cheapest test that confirms or kills the leading cause

Leading cause: Release 4.0's invoice-editor rebuild (retired default template) is depressing 7-day
activation. Confirm it cheaply before building a fix.

## Step 1 — free, do first: retrospective cohort read (hours, no code)
Using existing `invoice_sent` / `firm_signed_up` events, split new-firm journeys for two cohorts:
week of 20 July (pre-4.0) vs week of 27 July (post-4.0). Measure where firms stop between signup and
first `invoice_sent`. If the post-4.0 cohort stalls at the invoice-creation step specifically, the
editor is confirmed as the cause. If the drop is spread evenly, look elsewhere. This settles the
MEDIUM-confidence call at near-zero cost.

## Step 2 — if confirmed: one controlled test of the fix
**Change to test:** restore a one-click default starter template for newly signed-up firms.

- **Population:** new signups, randomised 50/50 (restored default vs current new-editor-only).
- **Primary metric:** 7-day activation rate (first invoice sent within 7 days) — the exact funnel metric that fell.
- **Guardrail metric:** invoices sent per activated firm in the first 30 days, so a faster first
  invoice doesn't come at the cost of firms sending fewer/worse invoices afterward.
- **Stopping rule:** run until ~400 signups per arm (≈3–4 weeks at ~63/week), or stop early if the
  guardrail drops materially. Decide to ship the default if treatment activation beats control with
  the gap large enough to matter against the ~20-point drop.

Reversibility: the retrospective read is read-only; the A/B is a flag that can be switched off.
