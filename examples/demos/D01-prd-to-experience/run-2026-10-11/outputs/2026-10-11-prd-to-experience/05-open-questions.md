# 05 · What design & engineering need from you before Monday

For Maya. Today is **Sunday 2026-10-11**; design and engineering start **Monday 2026-10-12**. These
are the decisions only the product owner can make. Ordered by what blocks the start of work. Each
names what it blocks and where it bites in the spec.

## Must answer before Monday — these block screen layout and the data model
1. **Multi-currency: one total or one per currency?** The context says invoices can be in USD, CAD,
   EUR, GBP (PRD line 28), but R3 says "the total equals the sum of all open invoices" (line 36) and
   R5 says one payment clears several (line 38). You can't sum or charge across currencies. Confirm:
   **subtotal per currency on the home screen, and multi-pay limited to one currency.** → Blocks S1
   layout, R3, R5, the prototype total line.
2. **What invoice statuses exist?** R2 names only Open and Paid (line 35), but the flows need
   **Overdue, Partially paid, Payment pending** too. Confirm the status set. → Blocks the data model,
   every status badge, S1/S2.
3. **Bank transfer — manual or automatic?** R6 has no acceptance criteria (line 39). The problem
   says accountants mark invoices paid by hand (line 7) and R4's 1-minute auto-paid rule is card-only
   (line 37). Confirm bank transfer stays **manual with a "Payment pending" state**. → Blocks S5, the
   reconciliation flow, R6's criteria.
4. **Partial payment rules (R8).** Is there a **minimum** amount? What **status** results? Can a
   partial-paid invoice be included in multi-select (R5)? → Blocks S7, S2, the multi-select rules.

## Should answer before Monday — avoids rework in the first days
5. **Who sends the "new link" on expiry (R1)?** A person at the firm, or an automated send? An
   automated send sits near the "automatic payment reminders" non-goal (line 17). → Blocks S6 and
   the email system boundary.
6. **Link scope.** One portal link per client per firm (what the list and total imply), or one per
   invoice? → Blocks the link/auth model and R1.
7. **What does "Viewed" mean (R9)?** Opening the portal, or opening the specific invoice? The
   criterion reads per-invoice (line 42). → Blocks the tracking events.
8. **Receipts for bank transfer and for multi-pay.** R4's receipt is card + single-invoice (line 37).
   One receipt per multi-pay or one per invoice? Any receipt for bank transfer? → Blocks the email
   templates.
9. **Open question 2 from the PRD (line 59):** notify the accountant when a client pays, or is the
   Paid status enough? → Blocks whether a payment notification is built at all.

## Can follow in week 1 — not blocking
10. **Brand colour contrast floor (R10).** Confirm a legibility fallback when a firm's colours fail
    contrast (proposed 4.5:1). → Affects S1/R10 but not the skeleton.
11. **PDF on an expired link (R7).** Allowed, so the client can keep a copy (line 23)? → S6 detail.
12. **Link security posture.** No-password links are bearer tokens; forwarded emails/shared devices
    are an exposure (gap E). Decide if any light verification is wanted. → Can be a fast-follow.
13. **Already-paid / double-charge handling.** The PRD has no refund path; if a charge lands on an
    already-paid invoice, what happens? → Edge-case policy, not a Monday blocker.

## What you don't need to decide (already clear from the PRD)
- No passwords, no saved cards/autopay, no auto-reminders, no mobile app (non-goals, lines 15–18).
- Beta is 10 card-enabled firms, then all card-enabled firms (line 51).
- Primary metric: median days invoice-sent-to-paid, baseline 34 days, target 25 by end of
  March 2027 (line 46). Guardrail baseline is **unknown** (line 47) — worth getting a number, but
  it doesn't block design.
