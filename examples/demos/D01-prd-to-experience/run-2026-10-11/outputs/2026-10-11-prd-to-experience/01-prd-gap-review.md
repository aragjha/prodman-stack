# 01 · PRD gap review

Source: `examples/demos/D01-prd-to-experience/input/prd-client-portal.md` (draft v0.2, read
2026-10-11). Every gap below cites the PRD line it comes from. Nothing here adds scope; suggestions
are marked **[suggestion]**.

## A. Requirements with no acceptance criteria
| # | Requirement (PRD line) | Gap |
|---|---|---|
| R6 | "The client can pay by bank transfer" (line 39) | **Acceptance criteria blank.** How does the client get the bank details? Is the invoice marked paid automatically or by hand? The problem statement says accountants "mark invoices paid by hand" (line 7), and R4's "paid within 1 minute" (line 37) is card-only — so bank transfer almost certainly stays manual. This must be stated, because it changes the invoice status model and the accountant's flow. |
| R10 | "The portal shows the firm's logo and brand colours" (line 43) | **Acceptance criteria blank.** Where do the logo and colours come from? What renders if a firm has set none? Is there a contrast floor so brand colours stay legible (see accessibility, D)? |

## B. The conflict that decides the layout: multi-currency vs one total
This is the first thing to settle — it shapes R3, R5 and the main screen.

- Context (lines 28): "Firms can issue invoices in USD, CAD, EUR and GBP, and a client's invoices
  can be in any of these."
- R3 (line 36): "The total equals the sum of all open invoices."
- R5 (line 38): "One payment marks every selected invoice paid."

**You cannot sum USD + EUR into one number, and a single card charge is in one currency.** So:
- R3's "total" must become **one subtotal per currency**, not a single figure.
- R5's "pay several in one payment" must be **constrained to one currency per payment**.

Shown both ways in the flows (02) and specs (04) until you confirm. This is judgment item #1.

## C. Ambiguous lines and missing edge cases (cited)
| Line | Requirement | What's unresolved |
|---|---|---|
| 34 (R1) | Link expires after 30 days; on expiry client "can request a new one by email" | Who/what sends the new link — a person at the firm, or an automated send? An automated send sits close to the "automatic payment reminders" non-goal (line 17); confirm it's allowed. Also: is the link one-per-client-per-firm, or one-per-invoice? Everything downstream (R2 list, R3 total) implies **one portal per client per firm**. Confirm. |
| 35 (R2) | Open first by due date; paid from last 12 months below | No handling for **overdue** (past due date), **partially paid** (created by R8), **void/cancelled**, **disputed**, or **credit notes**. At minimum overdue and partially-paid need a status, since the product exists to chase late payment (line 11–12). |
| 36 (R3) | Total = sum of open invoices | See B. Also: does the total include **overdue**? (It should — they're still owed.) Does a partial payment reduce it? |
| 37 (R4) | Pay one by card; paid within 1 min; emailed receipt | No unhappy paths: **card declined**, **partner page times out**, **client closes the tab mid-payment**, **invoice already paid** (by another method or another person) between load and pay, **double-submit**. These are the states that break in production. |
| 38 (R5) | Select several, pay in one card payment | See B (currency). Also: can the selection include a **partially-paid** invoice (pay its remainder)? Can it mix with **partial payment** (R8)? |
| 39 (R6) | Pay by bank transfer | See A. Also: how long until it shows paid? What does the client see in the gap — a "pending" state? |
| 41 (R8) | Partial payment "when the firm allows it" | How does the client **know** it's allowed — a visible control per invoice? Is there a **minimum**? What **status** results (R2 has no "partially paid")? Does the remaining balance feed back into the R3 total and stay payable? |
| 42 (R9) | Accountant sees "Viewed" with date/time | What counts as "viewed" — opening the **portal**, or opening the **specific invoice**? The acceptance criterion says the Ledgerly invoice list shows it, so it reads per-invoice; confirm. |
| 40 (R7) | Download any invoice as PDF | Does download work on an **expired link**? (Probably yes for "keep a copy" — line 23.) |

## D. Accessibility — not mentioned anywhere in the PRD
The PRD notes the client "Often reads the invoice email on a phone" (line 23) but sets no
accessibility or responsive bar. Starting points (not an audit — see limits):
- **Mobile-first / responsive**: the primary device is a phone; the pay flow must work one-handed.
- **Colour contrast**: R10 lets firms set brand colours (line 43). Brand colours regularly fail
  WCAG contrast. Needs a contrast floor and a fallback so text/buttons stay legible. **[suggestion]**
- **Keyboard + screen reader**: the pay buttons, the multi-select (R5), and the partial-amount
  input (R8) need labels, focus order, and error announcement.
- **Amounts and currency** must be announced, not conveyed by position/colour alone.
- **The partner's hosted card page** (line 29, 37) is outside our control — its accessibility is a
  dependency to confirm with the payments partner, not something the portal can fix.

## E. Trust and security (flagged by the PRD's own risk)
- Risk (line 54): clients may not trust a link and phone the firm. The portal needs visible
  firm branding (R10) and a plain "why am I seeing this" line to earn trust. **[suggestion]**
- No-password access (R1, line 34) means the link is a **bearer token**: anyone with the link can
  see and pay. Forwarded emails and shared devices are a real exposure. Worth a decision on link
  scope and whether any light verification is needed. Judgment item.

## F. Card-off firms
Context (line 29): "Fewer than 50 firms have card payments turned on." Risk (line 55): firms
without card can only offer bank transfer. The portal must render a **bank-transfer-only** variant
(no card buttons, no multi-select pay) — this is a distinct screen state, covered in 04.
